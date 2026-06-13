"""
Build summary tables for UIT-ViOCD NER experiments.

This script reads available metrics and dataset summaries, then writes CSV and
Markdown artifacts for report editing. Missing metrics files are tolerated and
recorded in the note column.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


DEFAULT_OUTPUT_DIR = "outputs/metrics/summary"

EXPERIMENTS = [
    {
        "experiment_name": "Rule-based Keyword Span Extractor",
        "dataset": "UIT-ViOCD full AI-assisted test split",
        "metrics_path": "outputs/metrics/rule_based_keyword_ner_baseline/metrics/rule_based_ner_metrics.json",
        "loss_type": "None",
        "epochs_fallback": 0,
        "train_records_override": 0,
        "test_records_override": 291,
        "note": "simple keyword matching baseline with very low exact-span recall",
    },
    {
        "experiment_name": "Pilot100 Unweighted PhoBERT NER",
        "dataset": "UIT-ViOCD pilot 100",
        "metrics_path": "outputs/metrics/uit_viocd_pilot_100_phobert_ner_3epoch_clean/metrics/phobert_ner_single_task.json",
        "loss_type": "CrossEntropy",
        "epochs_fallback": 3,
        "note": "model biased to O on small pilot data; train_records shows pilot dataset size",
    },
    {
        "experiment_name": "Pilot100 Weighted PhoBERT NER",
        "dataset": "UIT-ViOCD pilot 100",
        "metrics_path": "outputs/metrics/uit_viocd_pilot_100_phobert_ner_weighted_10epoch/metrics/phobert_ner_single_task.json",
        "loss_type": "Weighted CrossEntropy",
        "epochs_fallback": 10,
        "note": "class weights improved COMP prediction on pilot data but performance remained limited",
    },
    {
        "experiment_name": "Full Complaint Weighted PhoBERT NER",
        "dataset": "UIT-ViOCD full AI-assisted complaint span dataset",
        "metrics_path": "outputs/metrics/uit_viocd_full_complaint_phobert_ner_weighted_5epoch/metrics/phobert_ner_single_task.json",
        "loss_type": "Weighted CrossEntropy",
        "epochs_fallback": 5,
        "note": "strong full-data result, but not the best among full-data settings",
    },
    {
        "experiment_name": "Full Complaint Unweighted PhoBERT NER",
        "dataset": "UIT-ViOCD full AI-assisted complaint span dataset",
        "metrics_path": "outputs/metrics/uit_viocd_full_complaint_phobert_ner_unweighted_5epoch/metrics/phobert_ner_single_task.json",
        "loss_type": "CrossEntropy",
        "epochs_fallback": 5,
        "note": "best result; full data reduced the need for class weighting",
    },
]

COLUMNS = [
    "experiment_name",
    "dataset",
    "train_records",
    "test_records",
    "loss_type",
    "epochs",
    "entity_precision",
    "entity_recall",
    "entity_f1",
    "token_f1_macro",
    "avg_loss",
    "note",
]


def load_json_if_exists(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8-sig") as f:
        data = json.load(f)
    return data if isinstance(data, dict) else {}


def fmt_float(value: Any) -> str:
    if value is None or value == "":
        return ""
    try:
        return f"{float(value):.4f}"
    except (TypeError, ValueError):
        return ""


def dataset_sizes(dataset: str, pilot_summary: dict[str, Any], full_split: dict[str, Any]) -> tuple[str, str]:
    if dataset == "UIT-ViOCD pilot 100":
        records = pilot_summary.get("records", "")
        return str(records), ""
    if dataset == "UIT-ViOCD full AI-assisted complaint span dataset":
        return str(full_split.get("train", "")), str(full_split.get("test", ""))
    return "", ""


def build_rows(
    experiments: list[dict[str, Any]],
    pilot_summary: dict[str, Any],
    full_split: dict[str, Any],
) -> tuple[list[dict[str, str]], list[str]]:
    rows: list[dict[str, str]] = []
    loaded_metrics: list[str] = []

    for experiment in experiments:
        metrics_path = Path(experiment["metrics_path"])
        metrics = load_json_if_exists(metrics_path)
        train_records, test_records = dataset_sizes(experiment["dataset"], pilot_summary, full_split)
        if "train_records_override" in experiment:
            train_records = str(experiment["train_records_override"])
        if "test_records_override" in experiment:
            test_records = str(experiment["test_records_override"])

        note = experiment["note"]
        if metrics:
            loaded_metrics.append(str(metrics_path))
        else:
            note = f"{note}; metrics file missing: {metrics_path}"

        rows.append(
            {
                "experiment_name": experiment["experiment_name"],
                "dataset": experiment["dataset"],
                "train_records": train_records,
                "test_records": test_records,
                "loss_type": experiment["loss_type"],
                "epochs": str(metrics.get("epoch", experiment["epochs_fallback"])),
                "entity_precision": fmt_float(metrics.get("entity_precision")),
                "entity_recall": fmt_float(metrics.get("entity_recall")),
                "entity_f1": fmt_float(metrics.get("entity_f1")),
                "token_f1_macro": fmt_float(metrics.get("token_f1_macro")),
                "avg_loss": fmt_float(metrics.get("avg_loss")),
                "note": note,
            }
        )

    return rows, loaded_metrics


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def markdown_table(rows: list[dict[str, str]], columns: list[str]) -> str:
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(col, "")) for col in columns) + " |")
    return "\n".join(lines)


def write_experiment_markdown(path: Path, rows: list[dict[str, str]]) -> None:
    content = "\n".join(
        [
            "# NER Experiment Summary",
            "",
            markdown_table(rows, COLUMNS),
            "",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def dict_lines(data: dict[str, Any]) -> list[str]:
    return [f"- {key}: `{value}`" for key, value in data.items()]


def write_report_key_numbers(
    path: Path,
    rows: list[dict[str, str]],
    pilot_summary: dict[str, Any],
    full_summary: dict[str, Any],
    full_split: dict[str, Any],
    loaded_metrics: list[str],
) -> None:
    best_row = max(
        rows,
        key=lambda row: float(row["entity_f1"]) if row.get("entity_f1") else -1.0,
    )

    lines: list[str] = [
        "# Report Key Numbers - UIT-ViOCD NER",
        "",
        "## Dataset Statistics",
        "",
        f"- Pilot 100 records: `{pilot_summary.get('records', '')}`",
        f"- Full complaint records: `{full_summary.get('total_records', '')}`",
        f"- Full records with spans: `{full_summary.get('records_with_spans', '')}`",
        f"- Full records without spans: `{full_summary.get('records_without_spans', '')}`",
        f"- Full total tokens: `{full_summary.get('total_tokens', '')}`",
        f"- Full COMP token count: `{full_summary.get('COMP_token_count', '')}`",
        f"- Full COMP token ratio: `{fmt_float(full_summary.get('COMP_token_ratio'))}`",
        "",
        "Domain distribution:",
        *dict_lines(full_summary.get("domain_distribution", {})),
        "",
        "Split for model training:",
    ]
    split_items = full_split.get("splits", {})
    for split_name in ("train", "val", "test"):
        stats = split_items.get(split_name, {})
        lines.append(
            f"- {split_name}: `{stats.get('records', '')}` records, "
            f"`{stats.get('tokens', '')}` tokens, `{stats.get('comp_tokens', '')}` COMP tokens"
        )

    lines.extend(
        [
            "",
            "## Annotation Pipeline Statistics",
            "",
            "- Dataset source: `UIT-ViOCD` only.",
            "- Pilot 100 was used to validate the AI-assisted span annotation workflow.",
            "- Batch 200 was added and manually fixed for overlap cases before pilot300.",
            "- Remaining 2554 complaint reviews were processed in 13 AI annotation batches.",
            "- Automatic validation, offset repair, and overlap resolving were applied before merging.",
            f"- Final total spans: `{full_summary.get('total_spans', '')}`",
            f"- Average spans per record: `{fmt_float(full_summary.get('average_spans_per_record'))}`",
            "",
            "## Experiment Results",
            "",
            markdown_table(rows, COLUMNS),
            "",
            "Loaded metrics files:",
        ]
    )
    if loaded_metrics:
        lines.extend(f"- `{path}`" for path in loaded_metrics)
    else:
        lines.append("- None")

    lines.extend(
        [
            "",
            "## Key Findings",
            "",
            f"- Best available Entity F1: `{best_row.get('entity_f1', '')}` from `{best_row.get('experiment_name', '')}`.",
            "- Rule-based baseline performs poorly, showing that keyword matching is insufficient for exact complaint span extraction.",
            "- Pilot100 unweighted collapses to O predictions in the low-data setting.",
            "- Weighted loss helps in the low-data pilot setting.",
            "- Expanding AI-assisted span annotation to the full complaint set leads to the largest improvement.",
            "- Full unweighted PhoBERT NER achieves the best result: Entity-F1 0.8561 and Token-F1 0.8732.",
            "- Weighted loss is useful for pilot data but not the best full-data setting.",
            "",
            "## Limitations To Mention In Report",
            "",
            "- Full span labels are AI-assisted annotations, not fully human gold-standard labels.",
            "- Automatic validation, offset repair, overlap resolving and partial manual review were used to improve consistency.",
            "- Results should be interpreted as evaluation on the constructed AI-assisted span dataset.",
            "- The proposed contribution should be described as an AI-assisted complaint span annotation pipeline combined with PhoBERT NER, not as weighted loss alone.",
            "",
        ]
    )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build NER experiment summary tables.")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--full-summary", default="data/processed/uit_viocd_full_complaint_summary.json")
    parser.add_argument("--full-split-summary", default="data/processed/uit_viocd_full_complaint_ner_split_summary.json")
    parser.add_argument("--pilot100-summary", default="data/processed/uit_viocd_pilot_100_summary.json")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    full_summary = load_json_if_exists(Path(args.full_summary))
    full_split = load_json_if_exists(Path(args.full_split_summary))
    pilot_summary = load_json_if_exists(Path(args.pilot100_summary))

    rows, loaded_metrics = build_rows(EXPERIMENTS, pilot_summary, full_split)

    csv_path = output_dir / "ner_experiment_summary.csv"
    md_path = output_dir / "ner_experiment_summary.md"
    key_path = output_dir / "report_key_numbers.md"

    write_csv(csv_path, rows)
    write_experiment_markdown(md_path, rows)
    write_report_key_numbers(key_path, rows, pilot_summary, full_summary, full_split, loaded_metrics)

    print(f"CSV output             : {csv_path}")
    print(f"Markdown output        : {md_path}")
    print(f"Report key numbers     : {key_path}")
    print("Loaded metrics files:")
    if loaded_metrics:
        for path in loaded_metrics:
            print(f"  {path}")
    else:
        print("  none")
    print("\nExperiment summary:")
    print(markdown_table(rows, COLUMNS))


if __name__ == "__main__":
    main()
