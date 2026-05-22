"""
Evaluation metrics cho Multi-task Complaint Detection.
Hỗ trợ cả Classification (Accuracy, Precision, Recall, F1, Confusion Matrix)
và NER (Entity-level + Token-level Precision, Recall, F1).
"""
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    label_ranking_average_precision_score,
)
from seqeval.metrics import (
    precision_score as seqeval_precision,
    recall_score as seqeval_recall,
    f1_score as seqeval_f1,
    classification_report as seqeval_classification_report,
    entity_metrics,
)


# =============================================================================
# Classification Metrics
# =============================================================================

def compute_classification_metrics(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    class_names: Optional[List[str]] = None,
    target_names: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Tính toàn bộ metrics cho bài toán Classification.

    Args:
        y_true: Mảng nhãn thực tế (shape: n_samples,)
        y_pred: Mảng nhãn dự đoán (shape: n_samples,)
        class_names: Danh sách tên class theo thứ tự index
        target_names: Tên hiển thị trong classification report

    Returns:
        Dict chứa accuracy, precision, recall, f1 (macro + per-class),
        confusion_matrix, classification_report
    """
    if class_names is None:
        class_names = [f"class_{i}" for i in range(int(max(max(y_true), max(y_pred)) + 1))]
    if target_names is None:
        target_names = class_names

    labels = list(range(len(class_names)))

    accuracy = accuracy_score(y_true, y_pred)
    precision_macro = precision_score(y_true, y_pred, average="macro", zero_division=0)
    recall_macro = recall_score(y_true, y_pred, average="macro", zero_division=0)
    f1_macro = f1_score(y_true, y_pred, average="macro", zero_division=0)
    precision_weighted = precision_score(y_true, y_pred, average="weighted", zero_division=0)
    recall_weighted = recall_score(y_true, y_pred, average="weighted", zero_division=0)
    f1_weighted = f1_score(y_true, y_pred, average="weighted", zero_division=0)

    # Per-class F1
    f1_per_class = f1_score(y_true, y_pred, average=None, zero_division=0)
    precision_per_class = precision_score(y_true, y_pred, average=None, zero_division=0)
    recall_per_class = recall_score(y_true, y_pred, average=None, zero_division=0)

    per_class_metrics = {}
    for i, name in enumerate(class_names):
        if i < len(f1_per_class):
            per_class_metrics[name] = {
                "precision": float(precision_per_class[i]),
                "recall": float(recall_per_class[i]),
                "f1": float(f1_per_class[i]),
                "support": int(np.sum(y_true == i)),
            }

    report_text = classification_report(
        y_true, y_pred,
        labels=labels,
        target_names=target_names,
        digits=4,
        zero_division=0,
    )

    cm = confusion_matrix(y_true, y_pred, labels=labels)

    metrics = {
        "accuracy": float(accuracy),
        "precision_macro": float(precision_macro),
        "recall_macro": float(recall_macro),
        "f1_macro": float(f1_macro),
        "precision_weighted": float(precision_weighted),
        "recall_weighted": float(recall_weighted),
        "f1_weighted": float(f1_weighted),
        "per_class": per_class_metrics,
        "confusion_matrix": cm.tolist(),
        "classification_report": report_text,
        "num_samples": int(len(y_true)),
    }

    return metrics


def save_classification_results(
    metrics: Dict[str, Any],
    output_path: str,
    save_report: bool = True,
    save_confusion_matrix: bool = True,
    save_predictions: bool = True,
    y_true: Optional[np.ndarray] = None,
    y_pred: Optional[np.ndarray] = None,
    texts: Optional[List[str]] = None,
    probs: Optional[np.ndarray] = None,
    class_names: Optional[List[str]] = None,
) -> None:
    """
    Lưu toàn bộ kết quả classification: metrics.json, report.txt, confusion_matrix.png,
    và optionally predictions.csv.

    Args:
        metrics: Dict từ compute_classification_metrics
        output_path: Đường dẫn thư mục output (sẽ tạo nếu chưa có)
        save_report: Lưu classification_report.txt
        save_confusion_matrix: Lưu confusion_matrix.png
        save_predictions: Lưu predictions.csv
        y_true, y_pred, texts, probs: Dữ liệu gốc cho predictions.csv
        class_names: Tên class để map index → string
    """
    output_path = Path(output_path)
    output_path.mkdir(parents=True, exist_ok=True)

    # 1. Metrics JSON
    metrics_json = {k: v for k, v in metrics.items() if k != "classification_report"}
    with open(output_path / "metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics_json, f, ensure_ascii=False, indent=2)

    # 2. Report text
    if save_report:
        with open(output_path / "classification_report.txt", "w", encoding="utf-8") as f:
            f.write(metrics["classification_report"])

    # 3. Confusion Matrix figure
    if save_confusion_matrix:
        cm = np.array(metrics["confusion_matrix"])
        n_classes = cm.shape[0]

        if class_names is None:
            class_names = [f"Class {i}" for i in range(n_classes)]

        fig, ax = plt.subplots(figsize=(max(6, n_classes * 1.5), max(5, n_classes * 1.2)))
        sns.heatmap(
            cm,
            annot=True,
            fmt="d",
            cmap="Blues",
            xticklabels=class_names,
            yticklabels=class_names,
            ax=ax,
            linewidths=1,
            linecolor="gray",
            cbar_kws={"label": "Count"},
        )
        ax.set_xlabel("Predicted Label", fontsize=12)
        ax.set_ylabel("True Label", fontsize=12)
        ax.set_title("Confusion Matrix", fontsize=14, fontweight="bold")

        plt.tight_layout()
        fig.savefig(output_path / "confusion_matrix.png", dpi=150, bbox_inches="tight")
        plt.close(fig)

    # 4. Predictions CSV
    if save_predictions and y_true is not None and y_pred is not None:
        records = []
        for i in range(len(y_true)):
            record = {
                "index": i,
                "text": texts[i] if texts is not None else "",
                "true_label": int(y_true[i]),
                "pred_label": int(y_pred[i]),
                "correct": bool(y_true[i] == y_pred[i]),
            }
            if probs is not None and i < len(probs):
                for j, prob in enumerate(probs[i]):
                    record[f"prob_class_{j}"] = float(prob)
            records.append(record)

        df = pd.DataFrame(records)
        df.to_csv(output_path / "predictions.csv", index=False, encoding="utf-8-sig")


def plot_confusion_matrix(
    cm: np.ndarray,
    class_names: List[str],
    output_path: str,
    normalize: bool = False,
    title: str = "Confusion Matrix",
    cmap: str = "Blues",
) -> None:
    """
    Vẽ và lưu confusion matrix.

    Args:
        cm: Ma trận confusion matrix (numpy array)
        class_names: Danh sách tên class
        output_path: Đường dẫn lưu file
        normalize: Chuẩn hóa theo hàng (true label)
        title: Tiêu đề figure
        cmap: Colormap
    """
    if normalize:
        cm = cm.astype(float) / cm.sum(axis=1)[:, np.newaxis]
        fmt = ".2%"
    else:
        fmt = "d"

    fig, ax = plt.subplots(figsize=(len(class_names) * 1.5 + 1, len(class_names) * 1.2))
    sns.heatmap(
        cm,
        annot=True,
        fmt=fmt,
        cmap=cmap,
        xticklabels=class_names,
        yticklabels=class_names,
        ax=ax,
        linewidths=0.5,
        linecolor="gray",
    )
    ax.set_xlabel("Predicted Label", fontsize=12)
    ax.set_ylabel("True Label", fontsize=12)
    ax.set_title(title, fontsize=14, fontweight="bold")
    plt.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


# =============================================================================
# NER Metrics
# =============================================================================

def compute_ner_metrics(
    y_true: List[List[str]],
    y_pred: List[List[str]],
    label_list: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Tính toàn bộ metrics cho bài toán NER.

    Args:
        y_true: List of true tag sequences, each sequence is a list of string tags
        y_pred: List of predicted tag sequences, same format
        label_list: Danh sách tất cả nhãn có thể có

    Returns:
        Dict chứa entity-level P/R/F1, token-level P/R/F1, per-label report
    """
    if label_list is None:
        all_tags = set()
        for seq in y_true:
            all_tags.update(seq)
        for seq in y_pred:
            all_tags.update(seq)
        label_list = sorted(all_tags)

    # Entity-level (seqeval)
    entity_precision = seqeval_precision(y_true, y_pred)
    entity_recall = seqeval_recall(y_true, y_pred)
    entity_f1 = seqeval_f1(y_true, y_pred)

    # Token-level
    all_true_flat = [tag for seq in y_true for tag in seq]
    all_pred_flat = [tag for seq in y_pred for tag in seq]

    token_precision = precision_score(
        all_true_flat, all_pred_flat,
        average="macro", zero_division=0,
    )
    token_recall = recall_score(
        all_true_flat, all_pred_flat,
        average="macro", zero_division=0,
    )
    token_f1 = f1_score(
        all_true_flat, all_pred_flat,
        average="macro", zero_division=0,
    )

    # Per-label token metrics
    per_label = {}
    for label in label_list:
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

    # Seqeval report
    report_text = seqeval_classification_report(y_true, y_pred, digits=4)

    metrics = {
        "entity_precision": float(entity_precision),
        "entity_recall": float(entity_recall),
        "entity_f1": float(entity_f1),
        "token_precision": float(token_precision),
        "token_recall": float(token_recall),
        "token_f1": float(token_f1),
        "per_label": per_label,
        "classification_report": report_text,
        "num_samples": len(y_true),
        "total_tokens": len(all_true_flat),
    }

    return metrics


def save_ner_results(
    metrics: Dict[str, Any],
    output_path: str,
    save_report: bool = True,
    save_entity_breakdown: bool = True,
    y_true: Optional[List[List[str]]] = None,
    y_pred: Optional[List[List[str]]] = None,
    texts: Optional[List[List[str]]] = None,
) -> None:
    """
    Lưu kết quả NER: metrics.json, ner_report.txt, entity_breakdown.png.

    Args:
        metrics: Dict từ compute_ner_metrics
        output_path: Đường dẫn thư mục output
        save_report: Lưu ner_report.txt
        save_entity_breakdown: Vẽ bar chart per-label F1
        y_true, y_pred, texts: Dữ liệu gốc
    """
    output_path = Path(output_path)
    output_path.mkdir(parents=True, exist_ok=True)

    # 1. Metrics JSON
    metrics_json = {k: v for k, v in metrics.items() if k != "classification_report"}
    with open(output_path / "metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics_json, f, ensure_ascii=False, indent=2)

    # 2. Report text
    if save_report:
        with open(output_path / "ner_report.txt", "w", encoding="utf-8") as f:
            f.write(metrics["classification_report"])

    # 3. Entity breakdown bar chart
    if save_entity_breakdown and "per_label" in metrics:
        per_label = metrics["per_label"]
        labels = list(per_label.keys())
        f1_scores = [per_label[l]["f1"] for l in labels]
        precisions = [per_label[l]["precision"] for l in labels]
        recalls = [per_label[l]["recall"] for l in labels]

        x = np.arange(len(labels))
        width = 0.25

        fig, ax = plt.subplots(figsize=(max(8, len(labels) * 1.5), 6))
        bars1 = ax.bar(x - width, precisions, width, label="Precision", color="steelblue")
        bars2 = ax.bar(x, recalls, width, label="Recall", color="coral")
        bars3 = ax.bar(x + width, f1_scores, width, label="F1", color="seagreen")

        ax.set_xlabel("NER Tag", fontsize=12)
        ax.set_ylabel("Score", fontsize=12)
        ax.set_title("NER Performance per Tag", fontsize=14, fontweight="bold")
        ax.set_xticks(x)
        ax.set_xticklabels(labels, fontsize=11)
        ax.set_ylim(0, 1.1)
        ax.legend(fontsize=11)
        ax.grid(axis="y", alpha=0.3)

        for bar in bars3:
            height = bar.get_height()
            ax.annotate(f"{height:.2f}", xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3), textcoords="offset points", ha="center", va="bottom", fontsize=9)

        plt.tight_layout()
        fig.savefig(output_path / "ner_entity_breakdown.png", dpi=150, bbox_inches="tight")
        plt.close(fig)

    # 4. Predictions CSV
    if y_true is not None and y_pred is not None:
        records = []
        for i in range(len(y_true)):
            record = {
                "index": i,
                "tokens": " ".join(texts[i]) if texts else "",
                "gold_tags": " ".join(y_true[i]),
                "pred_tags": " ".join(y_pred[i]),
                "correct": (y_true[i] == y_pred[i]),
            }
            records.append(record)

        df = pd.DataFrame(records)
        df.to_csv(output_path / "ner_predictions.csv", index=False, encoding="utf-8-sig")


def compute_token_level_metrics(
    y_true: List[List[int]],
    y_pred: List[List[int]],
    id2label: Dict[int, str],
) -> Tuple[Dict[str, float], pd.DataFrame]:
    """
    Tính token-level precision/recall/F1 cho từng nhãn.

    Args:
        y_true: List of true tag ID sequences
        y_pred: List of predicted tag ID sequences
        id2label: Mapping from tag ID to tag name

    Returns:
        (metrics_dict, per_label_df)
    """
    all_true_flat = [tag for seq in y_true for tag in seq]
    all_pred_flat = [tag for seq in y_pred for tag in seq]

    results = []
    for tag_id, tag_name in sorted(id2label.items(), key=lambda x: x[0]):
        true_bin = [1 if t == tag_id else 0 for t in all_true_flat]
        pred_bin = [1 if p == tag_id else 0 for p in all_pred_flat]

        tp = sum(1 for t, p in zip(true_bin, pred_bin) if t == 1 and p == 1)
        fp = sum(1 for t, p in zip(true_bin, pred_bin) if t == 0 and p == 1)
        fn = sum(1 for t, p in zip(true_bin, pred_bin) if t == 1 and p == 0)

        p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f = 2 * p * r / (p + r) if (p + r) > 0 else 0.0

        results.append({
            "label": tag_name,
            "precision": p,
            "recall": r,
            "f1": f,
            "support": sum(true_bin),
            "TP": tp,
            "FP": fp,
            "FN": fn,
        })

    df = pd.DataFrame(results)

    metrics = {
        "token_precision_macro": df["precision"].mean(),
        "token_recall_macro": df["recall"].mean(),
        "token_f1_macro": df["f1"].mean(),
        "token_accuracy": sum(1 for t, p in zip(all_true_flat, all_pred_flat) if t == p) / max(len(all_true_flat), 1),
    }

    return metrics, df


def print_ner_comparison_table(
    results: Dict[str, Dict[str, float]],
    output_path: Optional[str] = None,
) -> str:
    """
    Tạo bảng so sánh NER giữa nhiều phương pháp.

    Args:
        results: Dict[method_name, Dict[metric_name, value]]
            Ví dụ: {"CRF": {"entity_f1": 0.35}, "noCRF": {"entity_f1": 0.30}}
        output_path: Đường dẫn lưu bảng (txt)

    Returns:
        Chuỗi bảng ASCII
    """
    headers = ["Method", "Entity P", "Entity R", "Entity F1", "Token P", "Token R", "Token F1"]
    rows = []

    for method, metrics in results.items():
        row = [
            method,
            f"{metrics.get('entity_precision', 0):.4f}",
            f"{metrics.get('entity_recall', 0):.4f}",
            f"{metrics.get('entity_f1', 0):.4f}",
            f"{metrics.get('token_precision', 0):.4f}",
            f"{metrics.get('token_recall', 0):.4f}",
            f"{metrics.get('token_f1', 0):.4f}",
        ]
        rows.append(row)

    col_widths = [max(len(row[i]) for row in [headers] + rows) for i in range(len(headers))]

    def format_row(row):
        return " | ".join(cell.ljust(col_widths[i]) for i, cell in enumerate(row))

    lines = []
    lines.append(format_row(headers))
    lines.append("-" * (sum(col_widths) + 3 * (len(headers) - 1)))
    for row in rows:
        lines.append(format_row(row))

    table = "\n".join(lines)

    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(table)

    return table


def print_classification_comparison_table(
    results: Dict[str, Dict[str, float]],
    output_path: Optional[str] = None,
) -> str:
    """
    Tạo bảng so sánh Classification giữa nhiều phương pháp.

    Args:
        results: Dict[method_name, Dict[metric_name, value]]
        output_path: Đường dẫn lưu bảng (txt)

    Returns:
        Chuỗi bảng ASCII
    """
    headers = ["Method", "Accuracy", "Precision", "Recall", "F1-Macro", "F1-Complaint"]
    rows = []

    for method, metrics in results.items():
        row = [
            method,
            f"{metrics.get('accuracy', 0):.4f}",
            f"{metrics.get('precision_macro', 0):.4f}",
            f"{metrics.get('recall_macro', 0):.4f}",
            f"{metrics.get('f1_macro', 0):.4f}",
            f"{metrics.get('f1_complaint', metrics.get('f1_class_1', 0)):.4f}",
        ]
        rows.append(row)

    col_widths = [max(len(row[i]) for row in [headers] + rows) for i in range(len(headers))]

    def format_row(row):
        return " | ".join(cell.ljust(col_widths[i]) for i, cell in enumerate(row))

    lines = []
    lines.append(format_row(headers))
    lines.append("-" * (sum(col_widths) + 3 * (len(headers) - 1)))
    for row in rows:
        lines.append(format_row(row))

    table = "\n".join(lines)

    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(table)

    return table


if __name__ == "__main__":
    # Quick sanity check
    print("=== Classification Metrics Demo ===")
    y_t = np.array([0, 1, 1, 0, 1, 0, 1])
    y_p = np.array([0, 1, 0, 0, 1, 1, 1])
    cls_metrics = compute_classification_metrics(
        y_t, y_p,
        class_names=["Non-Complaint", "Complaint"],
        target_names=["Non-Complaint (0)", "Complaint (1)"],
    )
    print(f"Accuracy : {cls_metrics['accuracy']:.4f}")
    print(f"F1-Macro : {cls_metrics['f1_macro']:.4f}")
    print(cls_metrics["classification_report"])

    print("\n=== NER Metrics Demo ===")
    y_t_ner = [["O", "O", "B-COMP", "I-COMP"], ["O", "B-COMP", "I-COMP", "O"]]
    y_p_ner = [["O", "O", "B-COMP", "I-COMP"], ["O", "B-COMP", "O", "O"]]
    ner_metrics = compute_ner_metrics(y_t_ner, y_p_ner)
    print(f"Entity F1 : {ner_metrics['entity_f1']:.4f}")
    print(ner_metrics["classification_report"])
