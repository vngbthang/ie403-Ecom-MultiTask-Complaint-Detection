"""
Standalone evaluation module cho NER task.
Tinh entity-level F1 (seqeval) va token-level P/R/F1 (sklearn),
bo qua label -100, hien thi classification report cho O, B-COMP, I-COMP.
"""
import json
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seqeval.metrics import (
    precision_score as seqeval_precision,
    recall_score as seqeval_recall,
    f1_score as seqeval_f1,
    classification_report as seqeval_classification_report,
)
from sklearn.metrics import (
    classification_report as sklearn_classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
)


LABEL_LIST = ["O", "B-COMP", "I-COMP"]
ID2LABEL = {0: "O", 1: "B-COMP", 2: "I-COMP"}
LABEL2ID = {"O": 0, "B-COMP": 1, "I-COMP": 2}


# =============================================================================
# Core Metrics
# =============================================================================

def compute_ner_metrics(
    y_true: List[List[str]],
    y_pred: List[List[str]],
    label_list: Optional[List[str]] = None,
    digits: int = 4,
) -> Dict[str, Any]:
    """
    Tinh day du metrics cho NER task.

    Bao gom:
    - Entity-level (seqeval): Precision, Recall, F1 tren entity spans
    - Token-level (sklearn): Precision, Recall, F1 tren tung token tag

    Args:
        y_true: List of true tag sequences (string tags, ví dụ: [["O", "B-COMP", "I-COMP"], ...])
        y_pred: List of predicted tag sequences (cùng format)
        label_list: Danh sach nhãn. None = tu dong lay tu data.
        digits: So chu so thap phan trong report (mặc định: 4)

    Returns:
        Dict chứa:
        - entity_precision, entity_recall, entity_f1
        - token_precision_macro, token_recall_macro, token_f1_macro
        - per_label (dict: O, B-COMP, I-COMP với P/R/F1/support)
        - classification_report (string)
        - num_samples, total_tokens
    """
    if label_list is None:
        all_tags = set()
        for seq in y_true:
            all_tags.update(seq)
        for seq in y_pred:
            all_tags.update(seq)
        label_list = sorted(all_tags)

    # --- Entity-level (seqeval) ---
    entity_precision = seqeval_precision(y_true, y_pred)
    entity_recall = seqeval_recall(y_true, y_pred)
    entity_f1 = seqeval_f1(y_true, y_pred)

    # --- Token-level (sklearn) ---
    all_true_flat = [tag for seq in y_true for tag in seq]
    all_pred_flat = [tag for seq in y_pred for tag in seq]

    # Overall token metrics (macro average) — truyen 1D arrays, khong wrap trong list
    token_precision_macro = precision_score(
        all_true_flat, all_pred_flat,
        average="macro", zero_division=0,
    )
    token_recall_macro = recall_score(
        all_true_flat, all_pred_flat,
        average="macro", zero_division=0,
    )
    token_f1_macro = f1_score(
        all_true_flat, all_pred_flat,
        average="macro", zero_division=0,
    )

    # Per-label token metrics
    per_label = {}
    for label in LABEL_LIST:
        if label not in label_list:
            continue
        true_flat_bin = [1 if t == label else 0 for t in all_true_flat]
        pred_flat_bin = [1 if p == label else 0 for p in all_pred_flat]

        tp = sum(1 for t, p in zip(true_flat_bin, pred_flat_bin) if t == 1 and p == 1)
        fp = sum(1 for t, p in zip(true_flat_bin, pred_flat_bin) if t == 0 and p == 1)
        fn = sum(1 for t, p in zip(true_flat_bin, pred_flat_bin) if t == 1 and p == 0)

        p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0

        per_label[label] = {
            "precision": float(p),
            "recall": float(r),
            "f1": float(f),
            "support": int(sum(true_flat_bin)),
        }

    # Classification report cho token-level (O, B-COMP, I-COMP)
    token_report = sklearn_classification_report(
        all_true_flat,
        all_pred_flat,
        labels=LABEL_LIST,
        target_names=LABEL_LIST,
        digits=digits,
        zero_division=0,
    )

    # Seqeval report cho entity-level
    entity_report = seqeval_classification_report(y_true, y_pred, digits=digits)

    metrics = {
        # Entity-level
        "entity_precision": float(entity_precision),
        "entity_recall": float(entity_recall),
        "entity_f1": float(entity_f1),
        # Token-level
        "token_precision_macro": float(token_precision_macro),
        "token_recall_macro": float(token_recall_macro),
        "token_f1_macro": float(token_f1_macro),
        # Per-label
        "per_label": per_label,
        # Reports
        "token_classification_report": token_report,
        "entity_classification_report": entity_report,
        # Metadata
        "num_samples": len(y_true),
        "total_tokens": len(all_true_flat),
    }

    return metrics


def compute_ner_metrics_from_ids(
    y_true_ids: List[List[int]],
    y_pred_ids: List[List[int]],
    id2label: Optional[Dict[int, str]] = None,
    digits: int = 4,
) -> Dict[str, Any]:
    """
    Tinh NER metrics tu ID sequences (thay vi string tags).
    Tu dong loc bo -100.

    Args:
        y_true_ids: List of true tag ID sequences (ví dụ: [[0, 1, 2, 0], ...])
        y_pred_ids: List of predicted tag ID sequences
        id2label: Mapping tu tag ID sang string. None = su dung ID2LABEL mac dinh.
        digits: So chu so thap phan

    Returns:
        Dict nhu compute_ner_metrics
    """
    if id2label is None:
        id2label = ID2LABEL

    y_true_str = []
    y_pred_str = []

    for true_seq, pred_seq in zip(y_true_ids, y_pred_ids):
        true_str = [id2label.get(t, "O") for t in true_seq if t != -100]
        pred_str = [id2label.get(p, "O") for p in pred_seq if p != -100]

        if true_str and pred_str:
            y_true_str.append(true_str)
            y_pred_str.append(pred_str)

    return compute_ner_metrics(y_true_str, y_pred_str, digits=digits)


# =============================================================================
# Save Functions
# =============================================================================

def save_ner_metrics_json(metrics: Dict[str, Any], output_dir: str) -> Path:
    """
    Luu metrics ra JSON, tach report ra file rieng.

    Args:
        metrics: Dict tu compute_ner_metrics
        output_dir: Thu muc luu ket qua

    Returns:
        Duong dan file metrics.json
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Loai bo reports khoi JSON
    json_metrics = {
        k: v for k, v in metrics.items()
        if k not in ("token_classification_report", "entity_classification_report")
    }
    # Chuyen per_label dict tu nested thanh flat
    if "per_label" in json_metrics:
        for label, vals in json_metrics["per_label"].items():
            for metric_key, val in vals.items():
                json_metrics[f"token_{label}_{metric_key}"] = val
        del json_metrics["per_label"]

    json_path = output_dir / "ner_metrics.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_metrics, f, ensure_ascii=False, indent=2)

    return json_path


def save_ner_reports(metrics: Dict[str, Any], output_dir: str) -> Dict[str, Path]:
    """
    Luu entity report va token report ra .txt.

    Returns:
        Dict {filename: path}
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    saved = {}

    if "entity_classification_report" in metrics:
        p = output_dir / "ner_entity_report.txt"
        with open(p, "w", encoding="utf-8") as f:
            f.write("=== ENTITY-LEVEL CLASSIFICATION REPORT (seqeval) ===\n\n")
            f.write(metrics["entity_classification_report"])
        saved["ner_entity_report.txt"] = p

    if "token_classification_report" in metrics:
        p = output_dir / "ner_token_report.txt"
        with open(p, "w", encoding="utf-8") as f:
            f.write("=== TOKEN-LEVEL CLASSIFICATION REPORT (sklearn) ===\n\n")
            f.write(metrics["token_classification_report"])
        saved["ner_token_report.txt"] = p

    return saved


def save_all_ner_results(
    metrics: Dict[str, Any],
    output_dir: str,
    y_true: Optional[List[List[str]]] = None,
    y_pred: Optional[List[List[str]]] = None,
    tokens: Optional[List[List[str]]] = None,
    model_name: str = "",
    dataset_name: str = "",
) -> Dict[str, Path]:
    """
    Luu tat ca ket qua NER: ner_metrics.json, entity_report.txt,
    token_report.txt, ner_entity_breakdown.png, ner_predictions.csv.

    Args:
        metrics: Dict tu compute_ner_metrics
        output_dir: Thu muc goc
        y_true, y_pred, tokens: Du lieu goc cho predictions.csv
        model_name, dataset_name: Ten model/dataset cho figure title

    Returns:
        Dict cac duong dan da luu
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    saved = {}

    # 1. Metrics JSON
    json_path = save_ner_metrics_json(metrics, output_dir)
    saved["ner_metrics.json"] = json_path

    # 2. Reports
    report_paths = save_ner_reports(metrics, output_dir)
    saved.update(report_paths)

    # 3. Per-label breakdown bar chart
    if "per_label" in metrics and metrics["per_label"]:
        fig = plot_ner_entity_breakdown(
            metrics["per_label"],
            model_name=model_name,
            dataset_name=dataset_name,
        )
        fig_path = output_dir / "ner_entity_breakdown.png"
        fig.savefig(fig_path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        saved["ner_entity_breakdown.png"] = fig_path

    # 4. Predictions CSV
    if y_true is not None and y_pred is not None:
        csv_path = output_dir / "ner_predictions.csv"
        records = []
        for i in range(min(len(y_true), len(y_pred))):
            record = {
                "index": i,
                "tokens": " ".join(tokens[i]) if tokens and i < len(tokens) else "",
                "gold_tags": " ".join(y_true[i]),
                "pred_tags": " ".join(y_pred[i]),
                "correct": (y_true[i] == y_pred[i]),
            }
            records.append(record)
        df = pd.DataFrame(records)
        df.to_csv(csv_path, index=False, encoding="utf-8-sig")
        saved["ner_predictions.csv"] = csv_path

    return saved


# =============================================================================
# Visualization
# =============================================================================

def plot_ner_entity_breakdown(
    per_label: Dict[str, Dict[str, float]],
    output_path: Optional[str] = None,
    model_name: str = "",
    dataset_name: str = "",
    figsize: Tuple[int, int] = (9, 5),
) -> plt.Figure:
    """
    Ve bar chart breakdown per NER tag (O, B-COMP, I-COMP).

    Args:
        per_label: Dict tu compute_ner_metrics["per_label"]
        output_path: Duong dan luu. None = chi ve khong luu.
        model_name, dataset_name: Phan cua title
        figsize: (width, height)

    Returns:
        matplotlib Figure
    """
    labels = LABEL_LIST
    precisions = [per_label.get(l, {}).get("precision", 0) for l in labels]
    recalls = [per_label.get(l, {}).get("recall", 0) for l in labels]
    f1_scores = [per_label.get(l, {}).get("f1", 0) for l in labels]

    x = np.arange(len(labels))
    width = 0.25
    bar_colors = ["#4C72B0", "#DD8452", "#55A868"]  # blue, orange, green

    fig, ax = plt.subplots(figsize=figsize)
    ax.bar(x - width, precisions, width, label="Precision", color=bar_colors[0], edgecolor="gray")
    ax.bar(x, recalls, width, label="Recall", color=bar_colors[1], edgecolor="gray")
    ax.bar(x + width, f1_scores, width, label="F1", color=bar_colors[2], edgecolor="gray")

    ax.set_xlabel("NER Tag", fontsize=12)
    ax.set_ylabel("Score", fontsize=12)
    title = "NER Performance per Tag"
    if model_name or dataset_name:
        title += f" — {model_name}" if model_name else ""
        title += f" ({dataset_name})" if dataset_name else ""
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=12)
    ax.set_ylim(0, 1.15)
    ax.legend(fontsize=11, loc="upper right")
    ax.grid(axis="y", alpha=0.3, linestyle="--")

    for bar, score in zip(ax.patches[len(labels):len(labels)*2], f1_scores):
        ax.annotate(
            f"{score:.2f}",
            xy=(bar.get_x() + bar.get_width() / 2, score),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold",
        )

    plt.tight_layout()

    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=150, bbox_inches="tight")

    return fig


def plot_ner_entity_f1_comparison(
    results: List[Dict[str, Any]],
    output_path: Optional[str] = None,
    dataset_name: str = "",
    figsize: Tuple[int, int] = (9, 5),
) -> plt.Figure:
    """
    Ve bar chart so sanh Entity F1 giua cac models.

    Args:
        results: List of metric dicts (can lay tu compute_ner_metrics)
        output_path: Duong dan luu
        dataset_name: Ten dataset cho title

    Returns:
        matplotlib Figure
    """
    results = sorted(results, key=lambda x: x.get("entity_f1", 0), reverse=True)
    model_names = [r.get("model", f"Model_{i}") for i, r in enumerate(results)]
    entity_f1s = [r.get("entity_f1", 0) for r in results]

    colors = plt.cm.Greens(np.linspace(0.4, 0.9, len(model_names)))[::-1]

    fig, ax = plt.subplots(figsize=figsize)
    bars = ax.bar(
        model_names,
        entity_f1s,
        color=colors,
        edgecolor="gray",
        linewidth=1.2,
        width=0.6,
    )

    for bar, score in zip(bars, entity_f1s):
        ax.annotate(
            f"{score:.4f}",
            xy=(bar.get_x() + bar.get_width() / 2, score),
            xytext=(0, 5),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold",
        )

    title = "NER Entity F1 Comparison"
    if dataset_name:
        title += f" ({dataset_name})"
    ax.set_xlabel("Model", fontsize=12)
    ax.set_ylabel("Entity F1", fontsize=12)
    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.set_ylim(0, 1.12)
    ax.grid(axis="y", alpha=0.3, linestyle="--")
    plt.xticks(rotation=15, ha="right", fontsize=11)
    plt.tight_layout()

    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=150, bbox_inches="tight")

    return fig


# =============================================================================
# Summary Table
# =============================================================================

def build_ner_summary_table(results: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Tao bang tong hop NER metrics tu nhieu experiments.

    Args:
        results: List of metric dicts (tu compute_ner_metrics, co them 'model', 'dataset')

    Returns:
        DataFrame
    """
    rows = []
    for r in results:
        row = {
            "model": r.get("model", "Unknown"),
            "dataset": r.get("dataset", "Unknown"),
            "entity_precision": r.get("entity_precision", 0),
            "entity_recall": r.get("entity_recall", 0),
            "entity_f1": r.get("entity_f1", 0),
            "token_precision_macro": r.get("token_precision_macro", 0),
            "token_recall_macro": r.get("token_recall_macro", 0),
            "token_f1_macro": r.get("token_f1_macro", 0),
            "num_samples": r.get("num_samples", 0),
            "total_tokens": r.get("total_tokens", 0),
        }
        # Per-label
        per_label = r.get("per_label", {})
        for label in LABEL_LIST:
            if label in per_label:
                row[f"token_{label}_f1"] = per_label[label].get("f1", 0)
                row[f"token_{label}_precision"] = per_label[label].get("precision", 0)
                row[f"token_{label}_recall"] = per_label[label].get("recall", 0)
                row[f"token_{label}_support"] = per_label[label].get("support", 0)
        rows.append(row)
    return pd.DataFrame(rows)


def save_ner_summary_csv(results: List[Dict[str, Any]], output_path: str) -> Path:
    """Luu bang NER tong hop ra CSV."""
    df = build_ner_summary_table(results)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    return output_path


# =============================================================================
# Standalone CLI
# =============================================================================

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Evaluate NER Results")
    parser.add_argument(
        "--predictions",
        required=True,
        help="Duong dan file predictions CSV (can cot: gold_tags, pred_tags)",
    )
    parser.add_argument(
        "--output-dir",
        default="outputs/evaluation/ner",
        help="Thu muc luu ket qua",
    )
    args = parser.parse_args()

    df = pd.read_csv(args.predictions, encoding="utf-8-sig")

    y_true = [seq.split() for seq in df["gold_tags"].tolist()]
    y_pred = [seq.split() for seq in df["pred_tags"].tolist()]
    tokens = None
    if "tokens" in df.columns:
        tokens = [str(t).split() for t in df["tokens"].tolist()]

    print(f"Loaded {len(df)} NER predictions")
    metrics = compute_ner_metrics(y_true, y_pred)

    print(f"\nEntity  - P: {metrics['entity_precision']:.4f}  R: {metrics['entity_recall']:.4f}  F1: {metrics['entity_f1']:.4f}")
    print(f"Token   - P: {metrics['token_precision_macro']:.4f}  R: {metrics['token_recall_macro']:.4f}  F1: {metrics['token_f1_macro']:.4f}")

    print("\n=== Token Classification Report ===")
    print(metrics["token_classification_report"])

    print("\n=== Entity Classification Report (seqeval) ===")
    print(metrics["entity_classification_report"])

    saved = save_all_ner_results(
        metrics=metrics,
        output_dir=args.output_dir,
        y_true=y_true,
        y_pred=y_pred,
        tokens=tokens,
    )

    print(f"\nSaved: {list(saved.keys())}")
