"""Create report figures for the UIT-ViOCD complaint span extraction paper.

This script only reads processed summaries and experiment metrics. It does not
modify datasets, training code, or LaTeX files.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


DEFAULT_SUMMARY_CSV = Path("outputs/metrics/summary/ner_experiment_summary.csv")
DEFAULT_DATASET_SUMMARY = Path("data/processed/uit_viocd_full_complaint_summary.json")
DEFAULT_SPLIT_SUMMARY = Path("data/processed/uit_viocd_full_complaint_ner_split_summary.json")
DEFAULT_OUTPUT_DIR = Path("figures")

METHOD_LABELS = {
    "Rule-based Keyword Span Extractor": "Rule-based",
    "Pilot100 Unweighted PhoBERT NER": "Pilot100 CE",
    "Pilot100 Weighted PhoBERT NER": "Pilot100 Weighted",
    "Full Complaint Weighted PhoBERT NER": "Full Weighted",
    "Full Complaint Unweighted PhoBERT NER": "Full CE",
}

FULL_UNWEIGHTED_PRED_DISTRIBUTION = {
    "O": 2473,
    "B-COMP": 1143,
    "I-COMP": 7851,
}

FULL_UNWEIGHTED_GOLD_DISTRIBUTION = {
    "O": 2931,
    "B-COMP": 1089,
    "I-COMP": 7447,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create figures for the revised UIT-ViOCD NER report."
    )
    parser.add_argument("--summary-csv", type=Path, default=DEFAULT_SUMMARY_CSV)
    parser.add_argument("--dataset-summary", type=Path, default=DEFAULT_DATASET_SUMMARY)
    parser.add_argument("--split-summary", type=Path, default=DEFAULT_SPLIT_SUMMARY)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def read_experiment_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def require_files(paths: list[Path]) -> None:
    missing = [str(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing required input files: " + ", ".join(missing))


def setup_axes(ax: plt.Axes, title: str) -> None:
    ax.set_title(title, fontsize=13, pad=12, weight="bold")
    ax.grid(axis="y", linestyle="--", alpha=0.35)
    ax.set_axisbelow(True)


def draw_pipeline(
    steps: list[str],
    output_path: Path,
    title: str,
    box_color: str = "#e8f2ff",
    edge_color: str = "#2f5f8f",
) -> None:
    fig, ax = plt.subplots(figsize=(11, 2.8))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_title(title, fontsize=14, weight="bold", pad=10)

    n_steps = len(steps)
    box_width = 0.115
    box_height = 0.28
    y = 0.43
    start_x = 0.03
    gap = (0.94 - n_steps * box_width) / (n_steps - 1)

    centers: list[tuple[float, float]] = []
    for idx, step in enumerate(steps):
        x = start_x + idx * (box_width + gap)
        rect = FancyBboxPatch(
            (x, y),
            box_width,
            box_height,
            boxstyle="round,pad=0.018,rounding_size=0.025",
            linewidth=1.4,
            edgecolor=edge_color,
            facecolor=box_color,
        )
        ax.add_patch(rect)
        ax.text(
            x + box_width / 2,
            y + box_height / 2,
            step,
            ha="center",
            va="center",
            fontsize=8.5,
            wrap=True,
        )
        centers.append((x + box_width / 2, y + box_height / 2))

    for idx in range(n_steps - 1):
        x1 = centers[idx][0] + box_width / 2 + 0.006
        x2 = centers[idx + 1][0] - box_width / 2 - 0.006
        arrow = FancyArrowPatch(
            (x1, centers[idx][1]),
            (x2, centers[idx + 1][1]),
            arrowstyle="-|>",
            mutation_scale=14,
            linewidth=1.2,
            color="#333333",
        )
        ax.add_patch(arrow)

    fig.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def create_annotation_pipeline(output_dir: Path) -> Path:
    output_path = output_dir / "annotation_pipeline.png"
    steps = [
        "UIT-ViOCD\nReview-level\nLabels",
        "Complaint\nCandidate\nSelection",
        "AI-assisted\nSpan\nAnnotation",
        "Offset\nValidation\nand Repair",
        "Overlap\nResolving",
        "BIO\nConversion",
        "PhoBERT NER\nTraining",
    ]
    draw_pipeline(steps, output_path, "AI-assisted Complaint Span Annotation Pipeline")
    return output_path


def create_phobert_architecture(output_dir: Path) -> Path:
    output_path = output_dir / "phobert_ner_architecture.png"
    steps = [
        "Input\nReview",
        "PhoBERT\nTokenizer",
        "PhoBERT-\nbase-v2",
        "Linear Token\nClassification\nLayer",
        "BIO Tags:\nO / B-COMP /\nI-COMP",
    ]
    draw_pipeline(
        steps,
        output_path,
        "PhoBERT NER Architecture for Complaint Span Extraction",
        box_color="#eef8ee",
        edge_color="#3d7a3d",
    )
    return output_path


def get_ordered_experiments(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    ordered = []
    by_name = {row["experiment_name"]: row for row in rows}
    for full_name, short_name in METHOD_LABELS.items():
        if full_name not in by_name:
            raise ValueError(f"Missing experiment row in summary CSV: {full_name}")
        row = by_name[full_name]
        ordered.append(
            {
                "full_name": full_name,
                "short_name": short_name,
                "entity_f1": float(row["entity_f1"]),
                "token_f1_macro": float(row["token_f1_macro"]),
            }
        )
    return ordered


def create_metric_bar_chart(
    experiments: list[dict[str, Any]],
    metric_key: str,
    ylabel: str,
    title: str,
    output_path: Path,
    color: str,
) -> Path:
    labels = [item["short_name"] for item in experiments]
    values = [item[metric_key] for item in experiments]

    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    bars = ax.bar(labels, values, color=color, edgecolor="#333333", linewidth=0.7)
    setup_axes(ax, title)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_ylim(0, 1.0)
    ax.tick_params(axis="x", labelrotation=25, labelsize=9)
    ax.tick_params(axis="y", labelsize=9)

    best_idx = max(range(len(values)), key=values.__getitem__)
    bars[best_idx].set_color("#2ca02c")
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.018,
            f"{value:.4f}",
            ha="center",
            va="bottom",
            fontsize=8.5,
        )

    fig.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return output_path


def create_label_distribution(split_summary: dict[str, Any], output_dir: Path) -> Path:
    output_path = output_dir / "full_test_label_distribution.png"
    labels = ["O", "B-COMP", "I-COMP"]
    gold_values = [FULL_UNWEIGHTED_GOLD_DISTRIBUTION[label] for label in labels]
    pred_values = [FULL_UNWEIGHTED_PRED_DISTRIBUTION[label] for label in labels]

    fig, ax = plt.subplots(figsize=(6.8, 4.2))
    x_positions = range(len(labels))
    width = 0.36
    ax.bar(
        [x - width / 2 for x in x_positions],
        gold_values,
        width=width,
        label="Gold",
        color="#4c78a8",
        edgecolor="#333333",
        linewidth=0.7,
    )
    ax.bar(
        [x + width / 2 for x in x_positions],
        pred_values,
        width=width,
        label="Predicted",
        color="#f58518",
        edgecolor="#333333",
        linewidth=0.7,
    )
    setup_axes(ax, "Full Test Label Distribution (Full CE)")
    ax.set_ylabel("Token count", fontsize=11)
    ax.set_xticks(list(x_positions))
    ax.set_xticklabels(labels, fontsize=10)
    ax.legend(fontsize=10)

    ymax = max(gold_values + pred_values)
    for x, value in zip([x - width / 2 for x in x_positions], gold_values):
        ax.text(x, value + ymax * 0.02, f"{value:,}", ha="center", fontsize=8.5)
    for x, value in zip([x + width / 2 for x in x_positions], pred_values):
        ax.text(x, value + ymax * 0.02, f"{value:,}", ha="center", fontsize=8.5)

    fig.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return output_path


def create_dataset_span_statistics(dataset_summary: dict[str, Any], output_dir: Path) -> Path:
    output_path = output_dir / "dataset_span_statistics.png"
    labels = ["Total records", "With spans", "Without spans"]
    values = [
        int(dataset_summary["total_records"]),
        int(dataset_summary["records_with_spans"]),
        int(dataset_summary["records_without_spans"]),
    ]
    colors = ["#4c78a8", "#54a24b", "#e45756"]

    fig, ax = plt.subplots(figsize=(6.5, 4.0))
    bars = ax.bar(labels, values, color=colors, edgecolor="#333333", linewidth=0.7)
    setup_axes(ax, "Full Complaint Span Dataset Statistics")
    ax.set_ylabel("Records", fontsize=11)
    ax.tick_params(axis="x", labelrotation=15, labelsize=10)
    ymax = max(values)
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + ymax * 0.025,
            f"{value:,}",
            ha="center",
            va="bottom",
            fontsize=9,
        )
    ax.set_ylim(0, ymax * 1.15)

    fig.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return output_path


def write_readme(output_dir: Path, paths: list[Path]) -> Path:
    output_path = output_dir / "README.md"
    content = [
        "# Report Figures",
        "",
        "Generated by `python -m src.evaluation.create_report_figures`.",
        "",
        "## Figures",
        "",
        "- `annotation_pipeline.png`: AI-assisted annotation workflow from UIT-ViOCD review-level labels to PhoBERT NER training.",
        "- `phobert_ner_architecture.png`: PhoBERT token classification architecture for BIO complaint span extraction. It does not include a classification branch or CRF layer.",
        "- `ner_method_comparison.png`: Entity-F1 comparison across five methods/settings from `outputs/metrics/summary/ner_experiment_summary.csv`.",
        "- `ner_token_f1_comparison.png`: Token-F1 macro comparison across five methods/settings from `outputs/metrics/summary/ner_experiment_summary.csv`.",
        "- `full_test_label_distribution.png`: Gold and predicted label counts for the best Full Complaint Unweighted PhoBERT NER run use the provided report numbers. Gold: `O=2931`, `B-COMP=1089`, `I-COMP=7447`; predicted: `O=2473`, `B-COMP=1143`, `I-COMP=7851`.",
        "- `dataset_span_statistics.png`: Full AI-assisted complaint span dataset record counts from `data/processed/uit_viocd_full_complaint_summary.json`.",
        "",
        "## Generated files",
        "",
    ]
    content.extend(f"- `{path.name}`" for path in paths)
    output_path.write_text("\n".join(content) + "\n", encoding="utf-8")
    return output_path


def main() -> int:
    args = parse_args()
    require_files([args.summary_csv, args.dataset_summary, args.split_summary])
    args.output_dir.mkdir(parents=True, exist_ok=True)

    rows = read_experiment_rows(args.summary_csv)
    dataset_summary = read_json(args.dataset_summary)
    split_summary = read_json(args.split_summary)
    experiments = get_ordered_experiments(rows)

    outputs = [
        create_annotation_pipeline(args.output_dir),
        create_phobert_architecture(args.output_dir),
        create_metric_bar_chart(
            experiments,
            "entity_f1",
            "Entity-F1",
            "NER Method Comparison by Entity-F1",
            args.output_dir / "ner_method_comparison.png",
            "#72b7b2",
        ),
        create_metric_bar_chart(
            experiments,
            "token_f1_macro",
            "Token-F1 macro",
            "NER Method Comparison by Token-F1 Macro",
            args.output_dir / "ner_token_f1_comparison.png",
            "#b279a2",
        ),
        create_label_distribution(split_summary, args.output_dir),
        create_dataset_span_statistics(dataset_summary, args.output_dir),
    ]
    readme_path = write_readme(args.output_dir, outputs)

    print(f"Output directory: {args.output_dir}")
    for path in outputs:
        print(f"Created: {path}")
    print(f"Created: {readme_path}")
    print(
        "Note: full_test_label_distribution.png uses hardcoded predicted counts "
        "and gold counts for the best Full Complaint Unweighted PhoBERT NER run."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
