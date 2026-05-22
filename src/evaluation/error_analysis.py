"""
Error Analysis cho Multi-task PhoBERT model.
Nhận checkpoint, NER test JSON, và classification test CSV.
Xuất các file CSV vào outputs/error_samples/.

Mỗi dòng: text, gold_label, predicted_label, gold_spans, predicted_spans, error_type

Error types:
    Classification: false_positive, false_negative
    NER: boundary_error, missed_entity, spurious_entity
"""
import os
import sys
import json
import csv
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any

import torch
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.models.multitask_model import PhobertCRFMultiTask
from src.data_processing.multitask_dataset import normalize_for_match
from src.evaluation.evaluate_classification import compute_classification_metrics
from src.evaluation.evaluate_ner import compute_ner_metrics

ID2LABEL = {0: "O", 1: "B-COMP", 2: "I-COMP"}
LABEL2ID = {"O": 0, "B-COMP": 1, "I-COMP": 2}

OUTPUT_DIR = PROJECT_ROOT / "outputs" / "error_samples"


# =============================================================================
# Entity Span Helpers
# =============================================================================

def extract_spans(tags: List[str], tokens: List[str]) -> List[Dict[str, Any]]:
    """
    Trích xuất entity spans từ chuỗi tags theo chuẩn BIO.

    Returns list of {start, end, label, text}
    """
    spans = []
    i = 0
    while i < len(tags):
        tag = tags[i]
        if tag.startswith("B-"):
            label = tag[2:]
            start = i
            end = i
            j = i + 1
            while j < len(tags) and tags[j] == f"I-{label}":
                end = j
                j += 1
            span_text = " ".join(tokens[start : end + 1])
            spans.append({
                "start": start,
                "end": end,
                "label": label,
                "text": span_text,
            })
            i = j
        elif tag.startswith("I-"):
            # Orphan I-tag (không có B- trước đó) — treat as O
            i += 1
        else:
            i += 1
    return spans


def spans_match(gold: List[Dict], pred: List[Dict], strict: bool = False) -> bool:
    """
    Kiểm tra xem hai danh sách spans có khớp nhau không.
    strict=True: phải cùng start, end, label
    strict=False: cùng label và cùng token indices
    """
    if len(gold) != len(pred):
        return False
    if strict:
        return gold == pred
    gold_set = {(s["start"], s["end"], s["label"]) for s in gold}
    pred_set = {(s["start"], s["end"], s["label"]) for s in pred}
    return gold_set == pred_set


def classify_ner_error(
    gold_tags: List[str],
    pred_tags: List[str],
    tokens: List[str],
) -> str:
    """
    Phân loại loại lỗi NER cho một câu.

    Returns:
        "correct"          - khớp hoàn toàn
        "boundary_error"   - cùng nhãn nhưng start/end khác
        "missed_entity"    - có trong gold nhưng không có trong pred
        "spurious_entity"  - có trong pred nhưng không có trong gold
        "mixed"            - nhiều loại lỗi cùng lúc
    """
    gold_spans = extract_spans(gold_tags, tokens)
    pred_spans = extract_spans(pred_tags, tokens)

    if spans_match(gold_spans, pred_spans):
        return "correct"

    gold_keys = {(s["start"], s["end"], s["label"]) for s in gold_spans}
    pred_keys = {(s["start"], s["end"], s["label"]) for s in pred_spans}

    missed = gold_keys - pred_keys
    spurious = pred_keys - gold_keys

    # Phân biệt boundary vs entity-level
    gold_labels = {(s["start"], s["end"]) for s in gold_spans}
    pred_labels = {(s["start"], s["end"]) for s in pred_spans}

    # Cùng spans nhưng label khác = boundary error về label
    same_span_diff_label = set()
    for s, p in zip(gold_spans, pred_spans):
        if s["start"] == p["start"] and s["end"] == p["end"] and s["label"] != p["label"]:
            same_span_diff_label.add((s["start"], s["end"], s["label"]))

    # Xác định loại lỗi chính
    if missed and spurious:
        return "mixed"
    elif missed:
        # Tất cả gold bị miss → kiểm tra có phải boundary hay không
        if any(s["label"] in {p["label"] for p in pred_spans} for s in gold_spans):
            return "boundary_error"
        return "missed_entity"
    elif spurious:
        if any(s["label"] in {g["label"] for g in gold_spans} for s in pred_spans):
            return "boundary_error"
        return "spurious_entity"
    else:
        # Cùng số lượng spans nhưng khác → boundary error
        return "boundary_error"


# =============================================================================
# Data Loading
# =============================================================================

def load_classification_data(path: str) -> pd.DataFrame:
    """Load classification CSV, tự nhận cột nhãn."""
    df = pd.read_csv(path, encoding="utf-8-sig")
    df.columns = df.columns.str.strip()

    # Nhận diện cột text
    text_col = None
    for col in ["review", "text"]:
        if col in df.columns:
            text_col = col
            break
    if text_col is None:
        raise ValueError(f"Không tìm thấy cột text. Cột: {df.columns.tolist()}")

    # Nhận diện cột label
    label_col = None
    for col in ["complaint_label", "label"]:
        if col in df.columns:
            label_col = col
            break
    if label_col is None:
        raise ValueError(f"Không tìm thấy cột nhãn. Cột: {df.columns.tolist()}")

    df = df.dropna(subset=[text_col]).reset_index(drop=True)
    df["label_int"] = df[label_col].astype(float).astype(int)

    return df[[text_col, "label_int"]].rename(columns={text_col: "text"})


def load_ner_data(path: str) -> List[Dict]:
    """Load NER JSON."""
    with open(path, encoding="utf-8-sig") as f:
        return json.load(f)


# =============================================================================
# Model Loading & Inference
# =============================================================================

def load_multitask_model(checkpoint_path: str, device: str = "cpu") -> PhobertCRFMultiTask:
    """Load checkpoint vào model."""
    model = PhobertCRFMultiTask(num_classes=2, num_ner_tags=3)
    ckpt = torch.load(checkpoint_path, map_location=device)
    model.load_state_dict(ckpt["model_state_dict"])
    model.to(device)
    model.eval()
    return model


def classify_batch(model, texts: List[str], tokenizer, max_len: int = 256, device: str = "cpu"):
    """
    Chạy classification inference trên danh sách texts.
    Trả về (y_pred_list, y_prob_list)
    """
    results_pred = []
    results_prob = []

    for text in texts:
        tokens = tokenizer.encode(text, add_special_tokens=True, max_length=max_len, truncation=True)
        input_ids = torch.tensor([tokens], dtype=torch.long, device=device)
        attn_mask = torch.tensor([[1] * len(tokens)], dtype=torch.long, device=device)

        with torch.no_grad():
            logits, _ = model(input_ids=input_ids, attention_mask=attn_mask)
            probs = torch.softmax(logits, dim=-1)
            pred = logits.argmax(dim=-1).item()

        results_pred.append(pred)
        results_prob.append(probs[0].cpu().tolist())

    return results_pred, results_prob


def predict_ner_for_item(model, tokens: List[str], tokenizer, max_len: int = 256, device: str = "cpu") -> List[str]:
    """Dự đoán NER tags cho một câu."""
    input_ids = [tokenizer.cls_token_id]
    label_ids = [-100]

    for word in tokens:
        word_tokens = tokenizer.tokenize(word)
        if not word_tokens:
            continue
        w_ids = tokenizer.convert_tokens_to_ids(word_tokens)
        input_ids.extend(w_ids)
        label_ids.append(0)  # placeholder
        label_ids.extend([-100] * (len(w_ids) - 1))

    input_ids.append(tokenizer.sep_token_id)
    label_ids.append(-100)

    if len(input_ids) > max_len:
        input_ids = input_ids[: max_len - 1] + [tokenizer.sep_token_id]
        label_ids = label_ids[: max_len - 1] + [-100]

    attention_mask = [1] * len(input_ids)
    pad_len = max_len - len(input_ids)
    if pad_len > 0:
        input_ids.extend([tokenizer.pad_token_id] * pad_len)
        attention_mask.extend([0] * pad_len)
        label_ids.extend([-100] * pad_len)

    input_ids_t = torch.tensor([input_ids], dtype=torch.long, device=device)
    attention_mask_t = torch.tensor([attention_mask], dtype=torch.long, device=device)

    with torch.no_grad():
        _, ner_predictions = model(input_ids=input_ids_t, attention_mask=attention_mask_t)
    pred_ids = ner_predictions[0]

    # Decode: bo qua -100
    true_seq = []
    pred_seq = []
    for pos in range(min(len(pred_ids), len(label_ids))):
        gold = int(label_ids[pos])
        if gold == -100:
            continue
        pred_seq.append(ID2LABEL.get(int(pred_ids[pos]), "O"))
        true_seq.append(ID2LABEL.get(gold, "O"))

    return pred_seq


# =============================================================================
# Error Analysis
# =============================================================================

def analyze_classification_errors(
    df: pd.DataFrame,
    y_pred: List[int],
    output_dir: Path,
):
    """
    Phân tích lỗi classification và lưu false_positive/negative CSVs.
    """
    df = df.copy()
    df["pred_label"] = y_pred
    df["correct"] = df["label_int"] == df["pred_label"]

    # False Negative: thực sự là complaint (1) nhưng dự đoán là 0
    fn_df = df[(df["label_int"] == 1) & (df["pred_label"] == 0)].copy()
    fn_df["error_type"] = "false_negative"
    fn_df["gold_label"] = "Complaint (1)"
    fn_df["predicted_label"] = "Non-Complaint (0)"
    fn_df["gold_spans"] = ""
    fn_df["predicted_spans"] = ""
    fn_df = fn_df[["text", "gold_label", "predicted_label", "gold_spans", "predicted_spans", "error_type"]]
    fn_df.to_csv(output_dir / "false_negative_classification.csv", index=False, encoding="utf-8-sig")

    # False Positive: thực sự là non-complaint (0) nhưng dự đoán là 1
    fp_df = df[(df["label_int"] == 0) & (df["pred_label"] == 1)].copy()
    fp_df["error_type"] = "false_positive"
    fp_df["gold_label"] = "Non-Complaint (0)"
    fp_df["predicted_label"] = "Complaint (1)"
    fp_df["gold_spans"] = ""
    fp_df["predicted_spans"] = ""
    fp_df = fp_df[["text", "gold_label", "predicted_label", "gold_spans", "predicted_spans", "error_type"]]
    fp_df.to_csv(output_dir / "false_positive_classification.csv", index=False, encoding="utf-8-sig")

    print(f"  Classification errors: FN={len(fn_df)}, FP={len(fp_df)}")
    return fn_df, fp_df


def analyze_ner_errors(
    ner_records: List[Dict],
    model,
    tokenizer,
    max_len: int = 256,
    device: str = "cpu",
    output_dir: Path = None,
):
    """
    Phân tích lỗi NER và lưu boundary/missed/spurious CSVs.
    """
    boundary_records = []
    missed_records = []
    spurious_records = []
    mixed_records = []

    for item in ner_records:
        tokens = item.get("tokens", [])
        gold_tags = item.get("ner_tags", [])
        if not tokens or len(tokens) != len(gold_tags):
            continue

        # Dự đoán
        pred_tags = predict_ner_for_item(model, tokens, tokenizer, max_len, device)

        # Trích xuất spans
        gold_spans = extract_spans(gold_tags, tokens)
        pred_spans = extract_spans(pred_tags, tokens)

        # Phân loại lỗi
        error_type = classify_ner_error(gold_tags, pred_tags, tokens)

        gold_spans_str = " | ".join(
            f"{s['label']}[{s['start']}:{s['end']}] {s['text']}"
            for s in gold_spans
        ) if gold_spans else ""
        pred_spans_str = " | ".join(
            f"{s['label']}[{s['start']}:{s['end']}] {s['text']}"
            for s in pred_spans
        ) if pred_spans else ""

        record = {
            "text": " ".join(tokens),
            "gold_label": "N/A",
            "predicted_label": "N/A",
            "gold_spans": gold_spans_str,
            "predicted_spans": pred_spans_str,
            "error_type": error_type,
        }

        if error_type == "boundary_error":
            boundary_records.append(record)
        elif error_type == "missed_entity":
            missed_records.append(record)
        elif error_type == "spurious_entity":
            spurious_records.append(record)
        elif error_type == "mixed":
            mixed_records.append(record)

    # Lưu CSVs
    def save_ner_error_csv(records, filename):
        if not records:
            # Tạo file rỗng với header
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            pd.DataFrame(columns=[
                "text", "gold_label", "predicted_label",
                "gold_spans", "predicted_spans", "error_type"
            ]).to_csv(output_dir / filename, index=False, encoding="utf-8-sig")
            return 0
        df = pd.DataFrame(records)
        df = df[["text", "gold_label", "predicted_label", "gold_spans", "predicted_spans", "error_type"]]
        df.to_csv(output_dir / filename, index=False, encoding="utf-8-sig")
        return len(df)

    n_boundary = save_ner_error_csv(boundary_records, "ner_boundary_errors.csv")
    n_missed = save_ner_error_csv(missed_records, "ner_missed_entities.csv")
    n_spurious = save_ner_error_csv(spurious_records, "ner_spurious_entities.csv")
    save_ner_error_csv(mixed_records, "ner_mixed_errors.csv")

    print(f"  NER errors: boundary={n_boundary}, missed={n_missed}, spurious={n_spurious}, mixed={len(mixed_records)}")

    return {
        "boundary": boundary_records,
        "missed": missed_records,
        "spurious": spurious_records,
        "mixed": mixed_records,
    }


def compute_overall_metrics(
    cls_df: pd.DataFrame,
    cls_preds: List[int],
    ner_records: List[Dict],
    model,
    tokenizer,
    max_len: int,
    device: str,
) -> Dict[str, Any]:
    """Tính overall metrics cho cả classification và NER."""
    y_true = cls_df["label_int"].values.tolist()
    y_pred = cls_preds

    cls_metrics = compute_classification_metrics(y_true, y_pred)

    # NER metrics
    y_true_ner = []
    y_pred_ner = []
    for item in ner_records:
        tokens = item.get("tokens", [])
        gold_tags = item.get("ner_tags", [])
        if not tokens or len(tokens) != len(gold_tags):
            continue
        pred_tags = predict_ner_for_item(model, tokens, tokenizer, max_len, device)
        y_true_ner.append(gold_tags)
        y_pred_ner.append(pred_tags)

    ner_metrics = compute_ner_metrics(y_true_ner, y_pred_ner) if y_true_ner else {}

    return {
        "classification": cls_metrics,
        "ner": ner_metrics,
    }


# =============================================================================
# Main
# =============================================================================

def run_error_analysis(
    checkpoint_path: str,
    ner_test_path: str,
    cls_test_path: str,
    output_dir: Optional[str] = None,
    max_len: int = 256,
    device: str = None,
):
    """
    Chạy error analysis đầy đủ.

    Args:
        checkpoint_path: Đường dẫn checkpoint .pt
        ner_test_path: Đường dẫn ner_test.json
        cls_test_path: Đường dẫn classification test CSV
        output_dir: Thư mục lưu error CSVs
        max_len: Độ dài tối đa chuỗi
        device: 'cuda' hoặc 'cpu'
    """
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"

    if output_dir is None:
        output_dir = OUTPUT_DIR
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print("Error Analysis — Multi-task PhoBERT")
    print(f"{'='*60}")
    print(f"Checkpoint : {checkpoint_path}")
    print(f"NER test   : {ner_test_path}")
    print(f"Cls test   : {cls_test_path}")
    print(f"Output     : {output_dir}")
    print(f"Device     : {device}")

    # Load model
    print("\n[LOAD] Loading model...")
    model = load_multitask_model(checkpoint_path, device)

    # Load tokenizer
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base-v2", use_fast=False)

    # Load data
    print("[LOAD] Loading classification data...")
    cls_df = load_classification_data(cls_test_path)
    print(f"  Classification samples: {len(cls_df)}")
    print(f"  Label dist: {dict(cls_df['label_int'].value_counts().sort_index())}")

    print("[LOAD] Loading NER data...")
    ner_records = load_ner_data(ner_test_path)
    print(f"  NER samples: {len(ner_records)}")

    # Classification inference
    print("\n[INFER] Classification inference...")
    cls_preds, cls_probs = classify_batch(
        model, cls_df["text"].tolist(), tokenizer, max_len, device
    )

    # NER inference
    print("[INFER] NER inference...")
    print("  (This may take a while for large datasets...)")

    # Compute overall metrics
    print("\n[ANALYZE] Computing overall metrics...")
    overall = compute_overall_metrics(
        cls_df, cls_preds, ner_records, model, tokenizer, max_len, device
    )

    print(f"\n  Classification:")
    print(f"    Accuracy      : {overall['classification']['accuracy']:.4f}")
    print(f"    F1-Macro      : {overall['classification']['f1_macro']:.4f}")
    print(f"    F1-Complaint : {overall['classification']['f1_complaint']:.4f}")

    if overall["ner"]:
        print(f"\n  NER:")
        print(f"    Entity F1    : {overall['ner']['entity_f1']:.4f}")
        print(f"    Token F1     : {overall['ner']['token_f1_macro']:.4f}")

    # Error analysis: Classification
    print("\n[ANALYZE] Classification errors...")
    fn_df, fp_df = analyze_classification_errors(cls_df, cls_preds, output_dir)

    # Error analysis: NER
    print("[ANALYZE] NER errors...")
    ner_errors = analyze_ner_errors(
        ner_records, model, tokenizer, max_len, device, output_dir
    )

    # Lưu overall metrics
    metrics_out = {
        "classification": {
            "accuracy": overall["classification"]["accuracy"],
            "f1_macro": overall["classification"]["f1_macro"],
            "f1_complaint": overall["classification"]["f1_complaint"],
            "precision_macro": overall["classification"]["precision_macro"],
            "recall_macro": overall["classification"]["recall_macro"],
            "confusion_matrix": overall["classification"]["confusion_matrix"],
        },
        "ner": {
            "entity_f1": overall["ner"].get("entity_f1", 0),
            "entity_precision": overall["ner"].get("entity_precision", 0),
            "entity_recall": overall["ner"].get("entity_recall", 0),
            "token_f1_macro": overall["ner"].get("token_f1_macro", 0),
        },
        "error_counts": {
            "classification": {
                "false_positive": len(fp_df),
                "false_negative": len(fn_df),
            },
            "ner": {
                "boundary_error": len(ner_errors["boundary"]),
                "missed_entity": len(ner_errors["missed"]),
                "spurious_entity": len(ner_errors["spurious"]),
                "mixed": len(ner_errors["mixed"]),
            },
        },
    }
    metrics_path = output_dir / "error_analysis_metrics.json"
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics_out, f, ensure_ascii=False, indent=2)

    # Summary
    print(f"\n{'='*60}")
    print("Error Analysis Hoàn Tất!")
    print(f"Output: {output_dir}")
    print(f"Files:")
    for f in sorted(output_dir.iterdir()):
        print(f"  - {f.name}")
    print(f"{'='*60}")

    return metrics_out


# =============================================================================
# CLI
# =============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Error Analysis cho Multi-task PhoBERT")
    parser.add_argument(
        "--checkpoint",
        required=True,
        help="Đường dẫn checkpoint .pt",
    )
    parser.add_argument(
        "--ner-test",
        default="data/processed/ner_test.json",
        help="Đường dẫn ner_test.json",
    )
    parser.add_argument(
        "--cls-test",
        default=None,
        help="Đường dẫn classification test CSV. "
             "Mặc định: dò tìm trong data/raw/UIT-ViOCD/test.csv",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Thư mục lưu error CSVs. Mặc định: outputs/error_samples",
    )
    parser.add_argument("--max-len", type=int, default=256)
    args = parser.parse_args()

    # Auto-detect classification test CSV
    if args.cls_test is None:
        candidates = [
            PROJECT_ROOT / "data" / "raw" / "UIT-ViOCD" / "test.csv",
            PROJECT_ROOT / "data" / "processed" / "shopee_test.csv",
        ]
        for candidate in candidates:
            if candidate.exists():
                args.cls_test = str(candidate)
                print(f"[AUTO] Detected classification test: {args.cls_test}")
                break
        if args.cls_test is None:
            print("ERROR: Không tìm thấy classification test CSV. Dùng --cls-test.")
            sys.exit(1)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    run_error_analysis(
        checkpoint_path=args.checkpoint,
        ner_test_path=args.ner_test,
        cls_test_path=args.cls_test,
        output_dir=args.output_dir,
        max_len=args.max_len,
        device=device,
    )
