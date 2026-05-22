"""
Collect experiment results from outputs/metrics/.
Reads all JSON and CSV metrics files and produces summary tables:
    - classification_summary.csv
    - ner_summary.csv
    - ablation_summary.csv

Each table includes: model, dataset, accuracy, macro_f1, complaint_f1,
entity_f1, token_f1 (where applicable).

Files are identified by naming convention:
    - classical_baselines.csv           → classification
    - phobert_ner_single_task.json      → ner (no CRF)
    - phobert_crf_ner_single_task.json  → ner (with CRF)
    - phobert_multitask_*.json          → multitask
    - ner_metrics_epoch{N}.json          → per-epoch NER metrics
"""
import json
import re
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Any

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
METRICS_DIR = PROJECT_ROOT / "outputs" / "metrics"


# =============================================================================
# File Pattern Definitions
# =============================================================================

CLASSIFICATION_FILES = [
    "classical_baselines.csv",
]

NER_FILES = [
    "phobert_ner_single_task.json",
    "phobert_crf_ner_single_task.json",
    "ner_single_task.json",
    "ner_crf_single_task.json",
]

MULTITASK_FILES = [
    "phobert_multitask.json",
    "multitask.json",
]

ABLATABLE_FILES = [
    "ner_multitask_alpha",
    "multitask_alpha",
]


# =============================================================================
# Classification Parsing
# =============================================================================

def parse_classical_baselines_csv(csv_path: Path) -> List[Dict[str, Any]]:
    """Parse classical_baselines.csv — one row per model."""
    rows = []
    df = pd.read_csv(csv_path, encoding="utf-8-sig")

    for _, row in df.iterrows():
        rows.append({
            "model": str(row.get("model", "")),
            "dataset": str(row.get("dataset", "")),
            "accuracy": _safe_float(row.get("accuracy")),
            "macro_f1": _safe_float(row.get("f1_macro")),
            "complaint_f1": _safe_float(row.get("f1_complaint")),
            "precision_macro": _safe_float(row.get("precision_macro")),
            "recall_macro": _safe_float(row.get("recall_macro")),
            "tn": _safe_int(row.get("TN")),
            "fp": _safe_int(row.get("FP")),
            "fn": _safe_int(row.get("FN")),
            "tp": _safe_int(row.get("TP")),
            "num_samples": _safe_int(row.get("num_samples")),
            "entity_f1": None,
            "token_f1": None,
            "source_file": str(csv_path.resolve().relative_to(PROJECT_ROOT)),
        })

    return rows


def parse_multitask_metrics_json(json_path: Path) -> List[Dict[str, Any]]:
    """
    Parse multitask checkpoint metrics JSON.
    Checkpoint format stores classification + ner metrics under various keys.
    """
    rows = []
    with open(json_path, encoding="utf-8-sig") as f:
        data = json.load(f)

    dataset = _infer_dataset_from_path(json_path)

    # Infer model name: data["model"] > path-based
    if "model" in data and data["model"]:
        base_model = str(data["model"])
    else:
        base_model = "PhoBERT-MultiTask"

    # Classification part
    cls_metrics = _extract_classification_metrics(data)
    if cls_metrics:
        rows.append({
            "model": base_model,
            "dataset": dataset,
            "accuracy": cls_metrics.get("accuracy"),
            "macro_f1": cls_metrics.get("f1_macro"),
            "complaint_f1": cls_metrics.get("f1_complaint"),
            "precision_macro": cls_metrics.get("precision_macro"),
            "recall_macro": cls_metrics.get("recall_macro"),
            "entity_f1": None,
            "token_f1": None,
            "num_samples": cls_metrics.get("num_samples"),
            "source_file": str(json_path.resolve().relative_to(PROJECT_ROOT)),
        })

    # NER part
    ner_metrics = _extract_ner_metrics(data)
    if ner_metrics:
        ner_model = base_model + "-NER" if base_model else "PhoBERT-MultiTask-NER"
        rows.append({
            "model": ner_model,
            "dataset": dataset,
            "accuracy": None,
            "macro_f1": None,
            "complaint_f1": None,
            "precision_macro": None,
            "recall_macro": None,
            "entity_f1": ner_metrics.get("entity_f1"),
            "token_f1": ner_metrics.get("token_f1_macro"),
            "entity_precision": ner_metrics.get("entity_precision"),
            "entity_recall": ner_metrics.get("entity_recall"),
            "num_samples": ner_metrics.get("num_samples"),
            "source_file": str(json_path.resolve().relative_to(PROJECT_ROOT)),
        })

    return rows


# =============================================================================
# NER Parsing
# =============================================================================

def parse_ner_metrics_json(json_path: Path) -> List[Dict[str, Any]]:
    """Parse NER single-task metrics JSON."""
    rows = []
    with open(json_path, encoding="utf-8-sig") as f:
        data = json.load(f)

    dataset = _infer_dataset_from_path(json_path)

    # Uu tien: data["model"] > path-based inference
    if "model" in data and data["model"]:
        model = str(data["model"])
    else:
        model = _infer_ner_model_name(json_path)

    rows.append({
        "model": model,
        "dataset": dataset,
        "accuracy": None,
        "macro_f1": None,
        "complaint_f1": None,
        "precision_macro": None,
        "recall_macro": None,
        "entity_f1": _safe_float(data.get("entity_f1")),
        "token_f1": _safe_float(data.get("token_f1_macro")),
        "entity_precision": _safe_float(data.get("entity_precision")),
        "entity_recall": _safe_float(data.get("entity_recall")),
        "num_samples": _safe_int(data.get("num_samples")),
        "source_file": str(json_path.resolve().relative_to(PROJECT_ROOT)),
    })

    return rows


def parse_ner_epoch_json(json_path: Path) -> Optional[Dict[str, Any]]:
    """Parse per-epoch NER metrics JSON (e.g. checkpoint/ner_metrics_epoch1.json)."""
    try:
        with open(json_path, encoding="utf-8-sig") as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return None

    dataset = _infer_dataset_from_path(json_path)
    epoch = _extract_epoch_number(json_path)

    # Uu tien: data["model"] > path-based inference
    if "model" in data and data["model"]:
        model = str(data["model"])
    else:
        model = _infer_ner_model_name(json_path)

    return {
        "model": model,
        "dataset": dataset,
        "epoch": epoch,
        "accuracy": None,
        "macro_f1": None,
        "complaint_f1": None,
        "precision_macro": None,
        "recall_macro": None,
        "entity_f1": _safe_float(data.get("entity_f1")),
        "token_f1": _safe_float(data.get("token_f1_macro")),
        "entity_precision": _safe_float(data.get("entity_precision")),
        "entity_recall": _safe_float(data.get("entity_recall")),
        "num_samples": _safe_int(data.get("num_samples")),
        "source_file": str(json_path.resolve().relative_to(PROJECT_ROOT)),
    }


def parse_ablation_json(json_path: Path) -> Optional[Dict[str, Any]]:
    """Parse ablation metrics JSON (e.g. ner_multitask_alpha_0.5.json)."""
    try:
        with open(json_path, encoding="utf-8-sig") as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return None

    dataset = _infer_dataset_from_path(json_path)
    epoch = _extract_epoch_number(json_path)

    # Extract alpha from filename
    alpha = _extract_alpha_from_path(json_path)

    # Uu tien: data["model"] > path-based inference
    if "model" in data and data["model"]:
        model = str(data["model"])
    else:
        model = "PhoBERT-MultiTask"

    # Extract NER metrics
    ner_metrics = _extract_ner_metrics(data)

    return {
        "model": model,
        "dataset": dataset,
        "alpha": alpha,
        "epoch": epoch,
        "accuracy": None,
        "macro_f1": None,
        "complaint_f1": None,
        "precision_macro": None,
        "recall_macro": None,
        "entity_f1": ner_metrics.get("entity_f1") if ner_metrics else None,
        "token_f1": ner_metrics.get("token_f1_macro") if ner_metrics else None,
        "entity_precision": ner_metrics.get("entity_precision") if ner_metrics else None,
        "entity_recall": ner_metrics.get("entity_recall") if ner_metrics else None,
        "num_samples": ner_metrics.get("num_samples") if ner_metrics else None,
        "source_file": str(json_path.resolve().relative_to(PROJECT_ROOT)),
    }


# =============================================================================
# Helper Parsers
# =============================================================================

def _extract_classification_metrics(data: Dict) -> Optional[Dict]:
    """Trích classification metrics từ dict gốc."""
    # Direct keys
    if "accuracy" in data:
        return {
            "accuracy": _safe_float(data.get("accuracy")),
            "f1_macro": _safe_float(data.get("f1_macro")),
            "f1_complaint": _safe_float(data.get("f1_complaint")),
            "precision_macro": _safe_float(data.get("precision_macro")),
            "recall_macro": _safe_float(data.get("recall_macro")),
            "num_samples": _safe_int(data.get("num_samples")),
        }

    # Nested under "classification"
    if "classification" in data and isinstance(data["classification"], dict):
        cls = data["classification"]
        return {
            "accuracy": _safe_float(cls.get("accuracy")),
            "f1_macro": _safe_float(cls.get("f1_macro")),
            "f1_complaint": _safe_float(cls.get("f1_complaint")),
            "precision_macro": _safe_float(cls.get("precision_macro")),
            "recall_macro": _safe_float(cls.get("recall_macro")),
            "num_samples": _safe_int(cls.get("num_samples")),
        }

    return None


def _extract_ner_metrics(data: Dict) -> Optional[Dict]:
    """Trích NER metrics từ dict gốc."""
    # Direct keys
    if "entity_f1" in data:
        return {
            "entity_f1": _safe_float(data.get("entity_f1")),
            "entity_precision": _safe_float(data.get("entity_precision")),
            "entity_recall": _safe_float(data.get("entity_recall")),
            "token_f1_macro": _safe_float(data.get("token_f1_macro")),
            "num_samples": _safe_int(data.get("num_samples")),
        }

    # Nested under "ner"
    if "ner" in data and isinstance(data["ner"], dict):
        ner = data["ner"]
        return {
            "entity_f1": _safe_float(ner.get("entity_f1")),
            "entity_precision": _safe_float(ner.get("entity_precision")),
            "entity_recall": _safe_float(ner.get("entity_recall")),
            "token_f1_macro": _safe_float(ner.get("token_f1_macro")),
            "num_samples": _safe_int(ner.get("num_samples")),
        }

    return None


def _infer_dataset_from_path(path: Path) -> str:
    """Infer dataset name from file path."""
    path_str = str(path).lower()
    if "shopee" in path_str:
        return "Shopee"
    elif "uocvd" in path_str or "viocd" in path_str:
        return "UIT-ViOCD"
    elif "ner" in path_str:
        return "NER"
    return "Unknown"


def _infer_ner_model_name(path: Path) -> str:
    """
    Infer model name from file path for NER files.
    Fallback khi JSON khong co key 'model'.
    """
    path_str = str(path).lower()

    if "multitask" in path_str:
        return "Multi-task PhoBERT + CRF"
    elif "phobert_crf_ner" in path_str:
        return "PhoBERT + CRF NER"
    elif "phobert_ner_single_task" in path_str:
        return "PhoBERT Linear NER"
    elif "crf" in path_str:
        return "PhoBERT-CRF-NER"
    else:
        return "PhoBERT-Linear-NER"


def _extract_epoch_number(path: Path) -> Optional[int]:
    """Extract epoch number from file path."""
    match = re.search(r"epoch[_\s-]*(\d+)", str(path), re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None


def _extract_alpha_from_path(path: Path) -> Optional[float]:
    """Extract alpha value from ablation filename."""
    match = re.search(r"alpha[_\s-]*(\d+\.?\d*)", str(path), re.IGNORECASE)
    if match:
        return float(match.group(1))
    return None


def _safe_float(value) -> Optional[float]:
    try:
        return float(value) if value is not None and str(value) not in ("", "nan") else None
    except (ValueError, TypeError):
        return None


def _safe_int(value) -> Optional[int]:
    try:
        return int(float(value)) if value is not None and str(value) not in ("", "nan") else None
    except (ValueError, TypeError):
        return None


# =============================================================================
# Collection Logic
# =============================================================================

def collect_all_results(metrics_dir: Path = METRICS_DIR) -> tuple:
    """
    Quét toàn bộ metrics_dir và trả về 3 list dicts:
        (classification_rows, ner_rows, ablation_rows)
    """
    if not metrics_dir.exists():
        print(f"[WARN] Metrics directory not found: {metrics_dir}")
        return [], [], []

    classification_rows = []
    ner_rows = []
    ablation_rows = []

    # Scan all JSON and CSV files recursively
    for json_path in metrics_dir.rglob("*.json"):
        try:
            stem = json_path.stem.lower()

            # Ablation files
            if any(kw in stem for kw in ABLATABLE_FILES):
                row = parse_ablation_json(json_path)
                if row:
                    ablation_rows.append(row)
                    continue

            # NER epoch files
            if re.search(r"ner_metrics[_\s]?epoch", stem):
                row = parse_ner_epoch_json(json_path)
                if row:
                    ner_rows.append(row)
                    continue

            # NER single-task files
            if any(kw in stem for kw in NER_FILES):
                rows = parse_ner_metrics_json(json_path)
                ner_rows.extend(rows)
                continue

            # Multi-task files
            if any(kw in stem for kw in MULTITASK_FILES):
                rows = parse_multitask_metrics_json(json_path)
                classification_rows.extend([r for r in rows if r.get("macro_f1") is not None])
                ner_rows.extend([r for r in rows if r.get("entity_f1") is not None])
                continue

        except Exception as e:
            print(f"[SKIP] Error parsing {json_path}: {e}")
            continue

    # Scan CSV files
    for csv_path in metrics_dir.rglob("*.csv"):
        try:
            stem = csv_path.stem.lower()
            if "classical_baselines" in stem or "baseline" in stem:
                rows = parse_classical_baselines_csv(csv_path)
                classification_rows.extend(rows)
        except Exception as e:
            print(f"[SKIP] Error parsing CSV {csv_path}: {e}")
            continue

    print(f"[COLLECT] Classification: {len(classification_rows)} rows")
    print(f"[COLLECT] NER           : {len(ner_rows)} rows")
    print(f"[COLLECT] Ablation      : {len(ablation_rows)} rows")

    return classification_rows, ner_rows, ablation_rows


# =============================================================================
# Summary Table Builders
# =============================================================================

def build_classification_summary(rows: List[Dict]) -> pd.DataFrame:
    """
    Build classification summary table.

    Columns: model, dataset, accuracy, macro_f1, complaint_f1,
             precision_macro, recall_macro, num_samples, source_file
    """
    if not rows:
        df = pd.DataFrame(columns=[
            "model", "dataset", "accuracy", "macro_f1", "complaint_f1",
            "precision_macro", "recall_macro", "num_samples", "source_file",
        ])
        return df

    df = pd.DataFrame(rows)

    # Select and order columns
    cols = [
        "model", "dataset", "accuracy", "macro_f1", "complaint_f1",
        "precision_macro", "recall_macro", "num_samples", "source_file",
    ]
    cols_present = [c for c in cols if c in df.columns]
    df = df[cols_present]

    # Sort: dataset, then model
    df = df.sort_values(["dataset", "model"], ascending=[True, True]).reset_index(drop=True)

    # Round floats
    for col in ["accuracy", "macro_f1", "complaint_f1", "precision_macro", "recall_macro"]:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: round(x, 4) if pd.notna(x) else None)

    return df


def build_ner_summary(rows: List[Dict]) -> pd.DataFrame:
    """
    Build NER summary table.

    Columns: model, dataset, epoch, entity_f1, entity_precision,
             entity_recall, token_f1, num_samples, source_file
    """
    if not rows:
        df = pd.DataFrame(columns=[
            "model", "dataset", "epoch", "entity_f1", "entity_precision",
            "entity_recall", "token_f1", "num_samples", "source_file",
        ])
        return df

    df = pd.DataFrame(rows)

    cols = [
        "model", "dataset", "epoch", "entity_f1", "entity_precision",
        "entity_recall", "token_f1", "num_samples", "source_file",
    ]
    cols_present = [c for c in cols if c in df.columns]
    df = df[cols_present]

    # Sort
    df = df.sort_values(["dataset", "model", "epoch"], ascending=[True, True, True]).reset_index(drop=True)

    # Round
    for col in ["entity_f1", "entity_precision", "entity_recall", "token_f1"]:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: round(x, 4) if pd.notna(x) else None)

    return df


def build_ablation_summary(rows: List[Dict]) -> pd.DataFrame:
    """
    Build ablation summary table.

    Columns: model, dataset, alpha, epoch, entity_f1, token_f1,
             entity_precision, entity_recall, num_samples, source_file
    """
    if not rows:
        df = pd.DataFrame(columns=[
            "model", "dataset", "alpha", "epoch", "entity_f1",
            "token_f1", "entity_precision", "entity_recall",
            "num_samples", "source_file",
        ])
        return df

    df = pd.DataFrame(rows)

    cols = [
        "model", "dataset", "alpha", "epoch", "entity_f1",
        "token_f1", "entity_precision", "entity_recall",
        "num_samples", "source_file",
    ]
    cols_present = [c for c in cols if c in df.columns]
    df = df[cols_present]

    # Sort: alpha ascending, then epoch
    sort_cols = [c for c in ["alpha", "epoch"] if c in df.columns]
    df = df.sort_values(sort_cols, ascending=[True] * len(sort_cols)).reset_index(drop=True)

    # Round
    for col in ["entity_f1", "token_f1", "entity_precision", "entity_recall"]:
        if col in df.columns:
            df[col] = df[col].apply(lambda x: round(x, 4) if pd.notna(x) else None)

    return df


# =============================================================================
# Main
# =============================================================================

def collect(
    metrics_dir: Optional[str] = None,
    output_dir: Optional[str] = None,
):
    """
    Quét toàn bộ metrics và xuất 3 summary CSVs.

    Args:
        metrics_dir: Thư mục chứa metrics (mặc định: outputs/metrics)
        output_dir: Thư mục lưu summary CSVs (mặc định: outputs/metrics)
    """
    if metrics_dir:
        metrics_dir = Path(metrics_dir)
    else:
        metrics_dir = METRICS_DIR

    if output_dir:
        output_dir = Path(output_dir)
    else:
        output_dir = METRICS_DIR

    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print("Collecting Experiment Results")
    print(f"Metrics dir : {metrics_dir}")
    print(f"Output dir  : {output_dir}")
    print(f"{'='*60}")

    # Collect
    cls_rows, ner_rows, abl_rows = collect_all_results(metrics_dir)

    # Build summaries
    cls_df = build_classification_summary(cls_rows)
    ner_df = build_ner_summary(ner_rows)
    abl_df = build_ablation_summary(abl_rows)

    # Save
    cls_path = output_dir / "classification_summary.csv"
    ner_path = output_dir / "ner_summary.csv"
    abl_path = output_dir / "ablation_summary.csv"

    cls_df.to_csv(cls_path, index=False, encoding="utf-8-sig")
    ner_df.to_csv(ner_path, index=False, encoding="utf-8-sig")
    abl_df.to_csv(abl_path, index=False, encoding="utf-8-sig")

    print(f"\n[SAVE] {cls_path}  ({len(cls_df)} rows)")
    print(f"[SAVE] {ner_path}  ({len(ner_df)} rows)")
    print(f"[SAVE] {abl_path}  ({len(abl_df)} rows)")

    # Print tables
    if not cls_df.empty:
        print(f"\n{'='*60}")
        print("Classification Summary")
        print(cls_df.to_string(index=False))

    if not ner_df.empty:
        print(f"\n{'='*60}")
        print("NER Summary")
        print(ner_df.to_string(index=False))

    if not abl_df.empty:
        print(f"\n{'='*60}")
        print("Ablation Summary")
        print(abl_df.to_string(index=False))

    print(f"\n{'='*60}")
    print("Done!")

    return cls_df, ner_df, abl_df


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Collect experiment results from outputs/metrics/"
    )
    parser.add_argument(
        "--metrics-dir",
        default=None,
        help="Thư mục chứa metrics JSON/CSV (mặc định: outputs/metrics)",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Thư mục lưu summary CSVs (mặc định: outputs/metrics)",
    )
    args = parser.parse_args()

    collect(
        metrics_dir=args.metrics_dir,
        output_dir=args.output_dir,
    )
