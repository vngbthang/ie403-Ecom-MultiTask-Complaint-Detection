"""
Standalone evaluation module cho Classification task.
Cung cap cac ham tinh metrics, luu ket qua, ve confusion matrix.
"""
import json
from pathlib import Path
from typing import Optional, Dict, Any, List

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)


CLASS_NAMES = ["Non-Complaint (0)", "Complaint (1)"]


# =============================================================================
# Core Metrics
# =============================================================================

def compute_classification_metrics(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_prob: Optional[np.ndarray] = None,
) -> Dict[str, Any]:
    """
    Tinh toan bo metrics cho binary complaint classification.

    Args:
        y_true: Mang nhan thuc te (shape: n_samples,)
        y_pred: Mang nhan du doan (shape: n_samples,)
        y_prob: Mang xac suat du doan (shape: n_samples, num_classes).
               Optional, neu co se tinh them AUC.

    Returns:
        Dict chua:
        - accuracy, precision_macro, recall_macro, f1_macro
        - precision_complaint, recall_complaint, f1_complaint
        - confusion_matrix (list), classification_report (string)
        - num_samples, tn, fp, fn, tp
        - y_prob neu duoc truyen vao
    """
    y_true = np.asarray(y_true).flatten()
    y_pred = np.asarray(y_pred).flatten()

    accuracy = accuracy_score(y_true, y_pred)
    precision_macro = precision_score(y_true, y_pred, average="macro", zero_division=0)
    recall_macro = recall_score(y_true, y_pred, average="macro", zero_division=0)
    f1_macro = f1_score(y_true, y_pred, average="macro", zero_division=0)

    # Per-class (class 1 = Complaint)
    precision_complaint = precision_score(y_true, y_pred, pos_label=1, zero_division=0)
    recall_complaint = recall_score(y_true, y_pred, pos_label=1, zero_division=0)
    f1_complaint = f1_score(y_true, y_pred, pos_label=1, zero_division=0)

    # Confusion matrix components
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    tn, fp, fn, tp = cm.ravel()

    report_text = classification_report(
        y_true, y_pred,
        labels=[0, 1],
        target_names=CLASS_NAMES,
        digits=4,
        zero_division=0,
    )

    metrics = {
        "accuracy": float(accuracy),
        "precision_macro": float(precision_macro),
        "recall_macro": float(recall_macro),
        "f1_macro": float(f1_macro),
        "precision_complaint": float(precision_complaint),
        "recall_complaint": float(recall_complaint),
        "f1_complaint": float(f1_complaint),
        "tn": int(tn),
        "fp": int(fp),
        "fn": int(fn),
        "tp": int(tp),
        "confusion_matrix": cm.tolist(),
        "classification_report": report_text,
        "num_samples": int(len(y_true)),
    }

    # Tinh AUC neu co y_prob
    if y_prob is not None:
        try:
            from sklearn.metrics import roc_auc_score
            if y_prob.ndim == 2 and y_prob.shape[1] == 2:
                auc = roc_auc_score(y_true, y_prob[:, 1])
            else:
                auc = roc_auc_score(y_true, y_prob)
            metrics["auc"] = float(auc)
        except Exception:
            pass  # AUC fails if only one class present

    return metrics


# =============================================================================
# Save Functions
# =============================================================================

def save_metrics_json(metrics: Dict[str, Any], output_dir: str) -> Path:
    """
    Luu metrics ra file JSON, truong 'classification_report' ghi rieng ra .txt.

    Args:
        metrics: Dict tu compute_classification_metrics
        output_dir: Thu muc luu ket qua

    Returns:
        Duong dan file metrics.json
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Ghi metrics.json (loai bo report_text de JSON dep hon)
    json_metrics = {k: v for k, v in metrics.items() if k != "classification_report"}
    json_path = output_dir / "metrics.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_metrics, f, ensure_ascii=False, indent=2)

    # Ghi classification_report.txt
    if "classification_report" in metrics:
        report_path = output_dir / "classification_report.txt"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(metrics["classification_report"])

    return json_path


def save_predictions_csv(
    y_true: np.ndarray,
    y_pred: np.ndarray,
    y_prob: Optional[np.ndarray],
    texts: Optional[List[str]],
    output_dir: str,
) -> Path:
    """
    Luu predictions ra CSV.

    Args:
        y_true, y_pred: Mang nhan
        y_prob: Mang xac suat (optional)
        texts: Danh sach text goc (optional)
        output_dir: Thu muc luu

    Returns:
        Duong dan file predictions.csv
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    records = []
    for i in range(len(y_true)):
        record = {
            "index": i,
            "text": texts[i] if texts is not None else "",
            "true_label": int(y_true[i]),
            "pred_label": int(y_pred[i]),
            "correct": bool(y_true[i] == y_pred[i]),
        }
        if y_prob is not None and i < len(y_prob):
            for j in range(y_prob.shape[1]):
                record[f"prob_class_{j}"] = float(y_prob[i, j])
        records.append(record)

    df = pd.DataFrame(records)
    csv_path = output_dir / "predictions.csv"
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")
    return csv_path


def save_all_results(
    metrics: Dict[str, Any],
    output_dir: str,
    y_true: Optional[np.ndarray] = None,
    y_pred: Optional[np.ndarray] = None,
    y_prob: Optional[np.ndarray] = None,
    texts: Optional[List[str]] = None,
    class_names: Optional[List[str]] = None,
    model_name: str = "",
    dataset_name: str = "",
) -> Dict[str, Path]:
    """
    Luu tat ca ket qua: metrics.json, classification_report.txt,
    confusion_matrix.png, predictions.csv.

    Args:
        metrics: Dict tu compute_classification_metrics
        output_dir: Thu muc goc luu ket qua
        y_true, y_pred, y_prob, texts: Du lieu goc cho predictions.csv
        class_names: Ten class cho confusion matrix
        model_name: Ten model (dung lam phan cua ten file)
        dataset_name: Ten dataset (dung lam phan cua ten file)

    Returns:
        Dict cac duong dan da luu: {filename: path}
    """
    if class_names is None:
        class_names = CLASS_NAMES

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    saved = {}

    # 1. metrics.json + classification_report.txt
    json_path = save_metrics_json(metrics, output_dir)
    saved["metrics.json"] = json_path
    saved["classification_report.txt"] = output_dir / "classification_report.txt"

    # 2. Confusion matrix
    if "confusion_matrix" in metrics:
        cm = np.array(metrics["confusion_matrix"])
        cm_path = output_dir / "confusion_matrix.png"
        plot_confusion_matrix(
            cm,
            class_names=class_names,
            output_path=str(cm_path),
            title=f"Confusion Matrix — {model_name}\n({dataset_name})" if model_name else "Confusion Matrix",
        )
        saved["confusion_matrix.png"] = cm_path

    # 3. Predictions CSV
    if y_true is not None and y_pred is not None:
        csv_path = save_predictions_csv(y_true, y_pred, y_prob, texts, output_dir)
        saved["predictions.csv"] = csv_path

    return saved


# =============================================================================
# Visualization
# =============================================================================

def plot_confusion_matrix(
    cm: np.ndarray,
    class_names: Optional[List[str]] = None,
    output_path: Optional[str] = None,
    normalize: bool = False,
    title: str = "Confusion Matrix",
    cmap: str = "Blues",
    figsize: tuple = (7, 6),
    annot_fmt: str = "d",
    annot_fs: int = 14,
) -> plt.Figure:
    """
    Ve va luu confusion matrix.

    Args:
        cm: Ma tran confusion (numpy array)
        class_names: Danh sach ten class
        output_path: Duong dan luu file. Neu None, chi ve khong luu.
        normalize: Hien thi % thay vi so dem
        title: Tieu de figure
        cmap: Colormap (Blues, Reds, viridis...)
        figsize: (width, height)
        annot_fmt: Format annotation ('d'=so nguyen, '.2%'=phan tram)
        annot_fs: Font size annotation

    Returns:
        matplotlib Figure
    """
    if class_names is None:
        class_names = CLASS_NAMES

    if normalize:
        cm_norm = cm.astype(float) / cm.sum(axis=1)[:, np.newaxis]
        fmt = ".2%"
    else:
        cm_norm = cm
        fmt = annot_fmt

    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(
        cm_norm,
        annot=True,
        fmt=fmt,
        cmap=cmap,
        xticklabels=class_names,
        yticklabels=class_names,
        ax=ax,
        linewidths=1.2,
        linecolor="gray",
        cbar_kws={"label": "Proportion" if normalize else "Count"},
        annot_kws={"size": annot_fs},
    )
    ax.set_xlabel("Predicted Label", fontsize=13, labelpad=8)
    ax.set_ylabel("True Label", fontsize=13, labelpad=8)
    ax.set_title(title, fontsize=14, fontweight="bold", pad=12)
    plt.xticks(rotation=15, ha="right", fontsize=11)
    plt.yticks(rotation=0, fontsize=11)
    plt.tight_layout()

    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=150, bbox_inches="tight")

    return fig


def plot_f1_comparison_bar(
    results: List[Dict[str, Any]],
    output_path: Optional[str] = None,
    dataset_name: str = "",
    figsize: tuple = (9, 5),
) -> plt.Figure:
    """
    Ve bar chart so sanh F1-Macro giua cac models.

    Args:
        results: List of metric dicts (moi dict can co 'model' va 'f1_macro')
        output_path: Duong dan luu
        dataset_name: Ten dataset hien thi trong title
        figsize: (width, height)

    Returns:
        matplotlib Figure
    """
    results = sorted(results, key=lambda x: x.get("f1_macro", 0), reverse=True)

    model_names = [r.get("model", f"Model_{i}") for i, r in enumerate(results)]
    f1_scores = [r.get("f1_macro", 0) for r in results]

    colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(model_names)))[::-1]

    fig, ax = plt.subplots(figsize=figsize)
    bars = ax.bar(
        model_names,
        f1_scores,
        color=colors,
        edgecolor="gray",
        linewidth=1.2,
        width=0.6,
    )

    for bar, score in zip(bars, f1_scores):
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

    title = f"F1-Macro Comparison — Classical Baselines"
    if dataset_name:
        title += f"\n({dataset_name})"

    ax.set_xlabel("Model", fontsize=12)
    ax.set_ylabel("F1-Macro", fontsize=12)
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

def build_summary_table(results: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Tao bang tong hop tu nhieu results.

    Args:
        results: List of metric dicts

    Returns:
        DataFrame voi cac cot: model, dataset, accuracy, precision_macro,
        recall_macro, f1_macro, f1_complaint, num_samples
    """
    rows = []
    for r in results:
        rows.append({
            "model": r.get("model", "Unknown"),
            "dataset": r.get("dataset", "Unknown"),
            "accuracy": r.get("accuracy", 0),
            "precision_macro": r.get("precision_macro", 0),
            "recall_macro": r.get("recall_macro", 0),
            "f1_macro": r.get("f1_macro", 0),
            "precision_complaint": r.get("precision_complaint", 0),
            "recall_complaint": r.get("recall_complaint", 0),
            "f1_complaint": r.get("f1_complaint", 0),
            "TN": r.get("tn", 0),
            "FP": r.get("fp", 0),
            "FN": r.get("fn", 0),
            "TP": r.get("tp", 0),
            "num_samples": r.get("num_samples", 0),
        })
    return pd.DataFrame(rows)


def save_summary_csv(results: List[Dict[str, Any]], output_path: str) -> Path:
    """Luu bang tong hop ra CSV."""
    df = build_summary_table(results)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    return output_path


# =============================================================================
# Standalone CLI
# =============================================================================

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Evaluate Classification Results")
    parser.add_argument("--predictions", required=True, help="Duong dan file predictions CSV (can cot: true_label, pred_label)")
    parser.add_argument("--output-dir", default="outputs/evaluation", help="Thu muc luu ket qua")
    args = parser.parse_args()

    df = pd.read_csv(args.predictions, encoding="utf-8-sig")
    y_true = df["true_label"].values
    y_pred = df["pred_label"].values
    texts = df["text"].tolist() if "text" in df.columns else None

    y_prob_cols = [c for c in df.columns if c.startswith("prob_class_")]
    y_prob = df[y_prob_cols].values if y_prob_cols else None

    print(f"Loaded {len(df)} predictions")
    metrics = compute_classification_metrics(y_true, y_pred, y_prob)

    print(f"\nAccuracy         : {metrics['accuracy']:.4f}")
    print(f"F1-Macro         : {metrics['f1_macro']:.4f}")
    print(f"F1-Complaint     : {metrics['f1_complaint']:.4f}")
    print(f"Precision-Macro  : {metrics['precision_macro']:.4f}")
    print(f"Recall-Macro     : {metrics['recall_macro']:.4f}")
    print(f"\nClassification Report:")
    print(metrics["classification_report"])

    saved = save_all_results(
        metrics=metrics,
        output_dir=args.output_dir,
        y_true=y_true,
        y_pred=y_pred,
        y_prob=y_prob,
        texts=texts,
    )

    print(f"\nSaved: {list(saved.keys())}")
