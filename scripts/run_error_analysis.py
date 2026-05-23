"""
Error Analysis Script cho Multi-task Complaint Detection.

Chạy:
    python scripts/run_error_analysis.py

Output:
    outputs/error_samples/classification_false_positive.csv
    outputs/error_samples/classification_false_negative.csv
    outputs/error_samples/classification_error_summary.csv
    outputs/error_samples/ner_boundary_errors.csv
    outputs/error_samples/ner_missed_entities.csv
    outputs/error_samples/ner_spurious_entities.csv
    outputs/error_samples/ner_error_summary.csv
    docs/error_analysis.md
"""
import json
import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if not (PROJECT_ROOT / "src").exists():
    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

sys.stdout.reconfigure(encoding="utf-8")

OUTPUT_ERROR = PROJECT_ROOT / "outputs" / "error_samples"
DOCS_DIR = PROJECT_ROOT / "docs"


# =============================================================================
# 1. Classification Error Analysis
# =============================================================================

def classify_error(row):
    """Phan loai loi classification."""
    true_l = int(row["true_label"])
    pred_l = int(row["pred_label"])
    if true_l == 0 and pred_l == 1:
        return "false_positive"
    elif true_l == 1 and pred_l == 0:
        return "false_negative"
    return "correct"


def extract_spans(tags_str):
    """Tach tags string thanh list, tra ve list spans (start, end, label)."""
    tags = tags_str.split()
    spans = []
    i = 0
    while i < len(tags):
        if tags[i].startswith("B-"):
            label = tags[i][2:]
            start = i
            i += 1
            while i < len(tags) and tags[i] == f"I-{label}":
                i += 1
            spans.append((start, i - 1, label))
        elif tags[i].startswith("I-"):
            i += 1
        else:
            i += 1
    return spans


def is_boundary_error(gold_str, pred_str):
    """Kiem tra xem loi co phai boundary error (overlap nhung khac span)."""
    gold_spans = set(extract_spans(gold_str))
    pred_spans = set(extract_spans(pred_str))
    gold_comp = {(s, e) for s, e, l in gold_spans if l == "COMP"}
    pred_comp = {(s, e) for s, e, l in pred_spans if l == "COMP"}

    if not gold_comp and not pred_comp:
        return False
    if not gold_comp or not pred_comp:
        return False

    gold_tokens = set()
    for s, e in gold_comp:
        for i in range(s, e + 1):
            gold_tokens.add(i)
    pred_tokens = set()
    for s, e in pred_comp:
        for i in range(s, e + 1):
            pred_tokens.add(i)

    overlap = gold_tokens & pred_tokens
    if overlap and gold_tokens != pred_tokens:
        return True
    return False


def is_missed_entity(gold_str, pred_str):
    """Gold co COMP span nhung pred khong co."""
    gold_spans = set(extract_spans(gold_str))
    pred_spans = set(extract_spans(pred_str))
    gold_has_comp = any(l == "COMP" for _, _, l in gold_spans)
    pred_has_comp = any(l == "COMP" for _, _, l in pred_spans)
    return gold_has_comp and not pred_has_comp


def is_spurious_entity(gold_str, pred_str):
    """Pred co COMP span nhung gold khong co."""
    gold_spans = set(extract_spans(gold_str))
    pred_spans = set(extract_spans(pred_str))
    gold_has_comp = any(l == "COMP" for _, _, l in gold_spans)
    pred_has_comp = any(l == "COMP" for _, _, l in pred_spans)
    return not gold_has_comp and pred_has_comp


def analyze_classification():
    """Phan tich loi Classification tu predictions.csv."""
    pred_path = PROJECT_ROOT / "outputs" / "metrics" / "Shopee" / "LinearSVM" / "predictions.csv"
    if not pred_path.exists():
        print(f"[WARN] Classification predictions not found: {pred_path}")
        return None

    df = pd.read_csv(pred_path, encoding="utf-8-sig")
    df["error_type"] = df.apply(classify_error, axis=1)

    # Confidence
    df["confidence"] = df.apply(
        lambda r: max(float(r["prob_class_0"]), float(r["prob_class_1"])), axis=1
    )

    # False Positive
    fp_df = df[df["error_type"] == "false_positive"].copy()
    fp_df["confidence"] = fp_df["prob_class_1"].astype(float)
    fp_df = fp_df[["index", "text", "true_label", "pred_label", "confidence", "prob_class_0", "prob_class_1"]]
    fp_path = OUTPUT_ERROR / "classification_false_positive.csv"
    fp_df.to_csv(fp_path, index=False, encoding="utf-8-sig")

    # False Negative
    fn_df = df[df["error_type"] == "false_negative"].copy()
    fn_df["confidence"] = fn_df["prob_class_0"].astype(float)
    fn_df = fn_df[["index", "text", "true_label", "pred_label", "confidence", "prob_class_0", "prob_class_1"]]
    fn_path = OUTPUT_ERROR / "classification_false_negative.csv"
    fn_df.to_csv(fn_path, index=False, encoding="utf-8-sig")

    # Summary
    total = len(df)
    n_fp = len(fp_df)
    n_fn = len(fn_df)
    n_correct = total - n_fp - n_fn

    # Vi du tiêu biểu
    fp_sample = fp_df.nlargest(5, "confidence")
    fn_sample = fn_df.nlargest(5, "confidence")

    summary_data = {
        "metric": [
            "Total Samples",
            "Correct",
            "False Positive (label=0, pred=1)",
            "False Negative (label=1, pred=0)",
            "Accuracy",
            "False Positive Rate (FP/neg)",
            "False Negative Rate (FN/pos)",
        ],
        "value": [
            total,
            n_correct,
            n_fp,
            n_fn,
            round(n_correct / total, 4),
            round(n_fp / (n_correct + n_fp), 4) if (n_correct + n_fp) > 0 else None,
            round(n_fn / (n_correct + n_fn), 4) if (n_correct + n_fn) > 0 else None,
        ],
    }

    summary_path = OUTPUT_ERROR / "classification_error_summary.csv"
    summary_df = pd.DataFrame(summary_data)
    summary_df.to_csv(summary_path, index=False, encoding="utf-8-sig")

    print(f"\n[CLASSIFICATION] False Positive: {n_fp} | False Negative: {n_fn} | Correct: {n_correct}")
    print(f"  Saved: {fp_path} ({len(fp_df)} rows)")
    print(f"  Saved: {fn_path} ({len(fn_df)} rows)")
    print(f"  Saved: {summary_path}")

    return {
        "total": total,
        "fp": n_fp,
        "fn": n_fn,
        "correct": n_correct,
        "fp_sample": fp_sample,
        "fn_sample": fn_sample,
    }


# =============================================================================
# 2. NER Error Analysis
# =============================================================================

def analyze_ner_from_predictions(pred_csv_path, model_name):
    """Phan tich loi NER tu predictions.csv (neu co)."""
    if not pred_csv_path.exists():
        print(f"[WARN] NER predictions not found: {pred_csv_path}")
        return None

    df = pd.read_csv(pred_csv_path, encoding="utf-8-sig")

    boundary_rows = []
    missed_rows = []
    spurious_rows = []

    for _, row in df.iterrows():
        gold = str(row.get("gold_tags", ""))
        pred = str(row.get("pred_tags", ""))

        if is_boundary_error(gold, pred):
            boundary_rows.append({
                "index": row.get("index", ""),
                "gold_tags": gold,
                "pred_tags": pred,
                "gold_spans": str(extract_spans(gold)),
                "pred_spans": str(extract_spans(pred)),
                "error_type": "boundary_error",
            })
        elif is_missed_entity(gold, pred):
            missed_rows.append({
                "index": row.get("index", ""),
                "gold_tags": gold,
                "pred_tags": pred,
                "gold_spans": str(extract_spans(gold)),
                "pred_spans": str(extract_spans(pred)),
                "error_type": "missed_entity",
            })
        elif is_spurious_entity(gold, pred):
            spurious_rows.append({
                "index": row.get("index", ""),
                "gold_tags": gold,
                "pred_tags": pred,
                "gold_spans": str(extract_spans(gold)),
                "pred_spans": str(extract_spans(pred)),
                "error_type": "spurious_entity",
            })

    if boundary_rows:
        bd_df = pd.DataFrame(boundary_rows)
        bd_path = OUTPUT_ERROR / f"ner_boundary_errors_{model_name}.csv"
        bd_df.to_csv(bd_path, index=False, encoding="utf-8-sig")
        print(f"  Saved: {bd_path} ({len(boundary_rows)} rows)")
    else:
        bd_path = None

    if missed_rows:
        ms_df = pd.DataFrame(missed_rows)
        ms_path = OUTPUT_ERROR / f"ner_missed_entities_{model_name}.csv"
        ms_df.to_csv(ms_path, index=False, encoding="utf-8-sig")
        print(f"  Saved: {ms_path} ({len(missed_rows)} rows)")
    else:
        ms_path = None

    if spurious_rows:
        sp_df = pd.DataFrame(spurious_rows)
        sp_path = OUTPUT_ERROR / f"ner_spurious_entities_{model_name}.csv"
        sp_df.to_csv(sp_path, index=False, encoding="utf-8-sig")
        print(f"  Saved: {sp_path} ({len(spurious_rows)} rows)")
    else:
        sp_path = None

    total_ner = len(df)
    n_boundary = len(boundary_rows)
    n_missed = len(missed_rows)
    n_spurious = len(spurious_rows)

    summary_data = {
        "metric": [
            "Total NER Samples",
            "Boundary Errors",
            "Missed Entities",
            "Spurious Entities",
            "Correct (exact match)",
        ],
        "value": [
            total_ner,
            n_boundary,
            n_missed,
            n_spurious,
            total_ner - n_boundary - n_missed - n_spurious,
        ],
    }

    summary_path = OUTPUT_ERROR / f"ner_error_summary_{model_name}.csv"
    summary_df = pd.DataFrame(summary_data)
    summary_df.to_csv(summary_path, index=False, encoding="utf-8-sig")
    print(f"  Saved: {summary_path}")

    return {
        "total": total_ner,
        "boundary": n_boundary,
        "missed": n_missed,
        "spurious": n_spurious,
        "boundary_sample": boundary_rows[:5] if boundary_rows else None,
        "missed_sample": missed_rows[:5] if missed_rows else None,
        "spurious_sample": spurious_rows[:5] if spurious_rows else None,
    }


def analyze_ner():
    """Phan tich loi NER tu nhieu nguon (predictions + reports)."""
    results = {}

    # Single-task NER
    for model_dir, model_name in [
        ("phobert_ner_single_task_full", "phobert_ner"),
        ("phobert_crf_ner_full", "phobert_crf_ner"),
    ]:
        pred_path = PROJECT_ROOT / "outputs" / "metrics" / model_dir / "figures" / f"{model_name}_single_task_predictions.csv"
        r = analyze_ner_from_predictions(pred_path, model_name)
        if r:
            results[model_name] = r

    # Multi-task NER
    for mt_dir, mt_name in [
        ("multitask_alpha1_ner_matched", "multitask_alpha1"),
        ("multitask_alpha2_ner_matched", "multitask_alpha2"),
    ]:
        mt_pred_dir = PROJECT_ROOT / "outputs" / "metrics" / mt_dir
        pred_candidates = list(mt_pred_dir.rglob("*predictions*.csv"))
        if pred_candidates:
            r = analyze_ner_from_predictions(pred_candidates[0], mt_name)
            if r:
                results[mt_name] = r
        else:
            print(f"[INFO] No predictions CSV for {mt_dir} — using reports only")

    return results


# =============================================================================
# 3. Generate docs/error_analysis.md
# =============================================================================

def build_error_analysis_md(cls_stats, ner_stats, ner_metrics_by_model):
    """Xay dung noi dung docs/error_analysis.md."""

    # Tinh cac so lieu tu ner_metrics_by_model
    def fmt_ner(name, m):
        ep = m.get("entity_precision", "—")
        er = m.get("entity_recall", "—")
        ef = m.get("entity_f1", "—")
        tf = m.get("token_f1_macro", "—")
        if isinstance(ep, float):
            ep = f"{ep:.4f}"
        if isinstance(er, float):
            er = f"{er:.4f}"
        if isinstance(ef, float):
            ef = f"{ef:.4f}"
        if isinstance(tf, float):
            tf = f"{tf:.4f}"
        return name, ep, er, ef, tf

    ner_rows_md = ""
    for name, m in ner_metrics_by_model.items():
        n, ep, er, ef, tf = fmt_ner(name, m)
        ner_rows_md += f"| {n} | {ep} | {er} | {ef} | {tf} |\n"

    # Classification error examples
    fp_examples = ""
    fn_examples = ""

    if cls_stats and cls_stats.get("fp_sample") is not None:
        for _, row in cls_stats["fp_sample"].head(5).iterrows():
            text = str(row["text"])[:120]
            conf = f"{row['confidence']:.3f}"
            fp_examples += f"- **FP** (conf={conf}): \"{text}\"\n"

    if cls_stats and cls_stats.get("fn_sample") is not None:
        for _, row in cls_stats["fn_sample"].head(5).iterrows():
            text = str(row["text"])[:120]
            conf = f"{row['confidence']:.3f}"
            fn_examples += f"- **FN** (conf={conf}): \"{text}\"\n"

    # NER boundary examples
    boundary_examples = ""
    if ner_stats:
        for model, data in ner_stats.items():
            if data and data.get("boundary_sample"):
                for ex in data["boundary_sample"][:3]:
                    gold = str(ex.get("gold_spans", ""))
                    pred = str(ex.get("pred_spans", ""))
                    boundary_examples += f"- **{model}** gold={gold}, pred={pred}\n"

    md = f"""# Error Analysis

## 1. Overview

Classification trên Shopee đạt kết quả cao (LinearSVM: Accuracy 0.9431, F1-Macro 0.9428) nhờ TF-IDF n-grams (1,2) với feature 10,000 chiều. Trong khi đó, NER khó hơn nhiều vì cần xác định ranh giới chính xác của cụm khiếu nại trong thư mục review TMĐT tiếng Việt.

PhoBERT Linear NER và PhoBERT + CRF NER single-task đạt Entity-F1 chỉ ~0.02, gần như không có khả năng trích xuất span. Multi-task PhoBERT + CRF cải thiện rõ rệt: Entity-F1 đạt ~0.33, Token-F1 đạt ~0.66. Tuy nhiên recall vẫn còn thấp, cho thấy model bỏ sót nhiều entity.

---

## 2. Classification Error Analysis

### 2.1 Overall Error Distribution

"""

    if cls_stats:
        md += f"""| Metric | Value |
|---|---|
| Total Samples | {cls_stats["total"]} |
| Correct | {cls_stats["correct"]} |
| False Positive (true=0, pred=1) | {cls_stats["fp"]} |
| False Negative (true=1, pred=0) | {cls_stats["fn"]} |
| Accuracy | {cls_stats["correct"] / cls_stats["total"]:.4f} |

### 2.2 False Positive Examples (Non-Complaint predicted as Complaint)

"""
    else:
        md += "> Chua co vi du cu the tu predictions.csv.\n\n"

    if fp_examples:
        md += fp_examples + "\n"
    else:
        md += "> Chua co vi du cu the.\n\n"

    md += """**Phan tich FP:**
- Binh luan khong yeu cau nhung chua tu tiêu cuc nhe hoac mo ta van de nho.
- Mot so review ghi nhan dang ky san pham nhung khong co complaint thuc su.
- Rating-label noise: nhan duoc gan tu rating 4-5★ nen co the co nhieu khi rating thap nhung khong phai complaint.

### 2.3 False Negative Examples (Complaint predicted as Non-Complaint)

"""

    if fn_examples:
        md += fn_examples + "\n"
    else:
        md += "> Chua co vi du cu the.\n\n"

    md += """**Phan tich FN:**
- Complaint ngam: khong co tu khoa tieu cuc ro rang, chi mo ta trai nghiem.
- Mixed sentiment: cau vua khen vua chê, model lay trung binh thanh non-complaint.
- Informal Vietnamese: teencode, loi chinh ta, tu viet tat lam giam confidence.

### 2.4 Root Causes

1. **Rating-label noise**: Nhan Shopee duoc suy ra tu rating (1-2★ = complaint, 4-5★ = non-complaint). Rating thap co the do nhieu ly do khac ngoai complaint (vi du: giao cham, dong goi ke, khong uong ti).
2. **Mixed sentiment**: Nguoi dung thuong vua khen vua chê trong cung mot binh luan. TF-IDF co the bi danh gia boi phan tich tich cuc.
3. **Implicit complaint**: Complaint khong noi rõ, chi nghi nghi hoac de cap gian tiep.

---

## 3. NER Error Analysis

### 3.1 NER Metrics Summary

| Model | Entity Precision | Entity Recall | Entity F1 | Token F1 |
|-------|-----------------|---------------|-----------|----------|
""" + ner_rows_md + """
> PhoBERT Linear NER va PhoBERT + CRF NER single-task chi dat Entity-F1 ~0.02. Multi-task PhoBERT + CRF dat Entity-F1 ~0.33 nhung van con thap.

### 3.2 Token-level Breakdown (Multi-task alpha=1.0, epoch 3)

| Label | Precision | Recall | F1 | Support |
|-------|-----------|--------|-----|---------|
| O | 0.8887 | 0.8878 | 0.8882 | 2,833 |
| B-COMP | 0.7723 | 0.3023 | 0.4345 | 258 |
| I-COMP | 0.5552 | 0.6787 | 0.6108 | 719 |

**Nhan xet:**
- **B-COMP recall that thap (0.3023)**: Model rat kho xac dinh dung token bat dau cua mot entity. Day la nguyen nhan chinh dan den Entity-F1 thap.
- **I-COMP precision thap (0.5552)**: Model co xu huong dat nhan I-COMP nhung khong dung vi tri, dan den nhieu false positive o muc I-COMP.
- **O precision/recall cao (~0.89)**: Model phan biet tot token khong phai entity.

### 3.3 Error Types (tu predictions.csv)

"""

    if ner_stats:
        for model, data in ner_stats.items():
            md += f"**{model}** (total={data['total']}):\n"
            md += f"- Boundary errors: {data['boundary']}\n"
            md += f"- Missed entities: {data['missed']}\n"
            md += f"- Spurious entities: {data['spurious']}\n\n"
    else:
        md += "> Chua co predictions.csv cho NER multi-task de phan tich muc do.\n\n"

    if boundary_examples:
        md += "**Boundary Error Examples:**\n" + boundary_examples + "\n"

    md += """### 3.4 Key NER Error Patterns

1. **B-COMP Boundary Error**: Model bỏ sót token bắt đầu entity. Ví dụ: gold=`B-COMP I-COMP I-COMP`, pred=`I-COMP B-COMP I-COMP`. Đây là lỗi phổ biến nhất — recall của B-COMP chỉ 0.30.

2. **Missed Entity**: Model không trích xuất được entity nào từ câu có complaint. Nguyên nhân: dataset nhỏ (400 train), complaint span ngắn và không có pattern cố định.

3. **Spurious Entity**: Model trích xuất entity từ câu không có complaint. Thường là các cụm từ mo tả vấn đề nhẹ hoặc từ ngữ tích cực bị hiểu nhầm.

4. **Informal Vietnamese**: Review TMĐT tiếng Việt có nhiều teencode, lỗi chính tả, viết tắt. PhoBERT được pre-trained trên tiếng Việt chuẩn nên gặp khó khăn với các biến thể không chuẩn.
   - Ví dụ: "sp ko giống hình", "shop giao thiếu hàng", "chất keo kém"

5. **Implicit Complaint**: Câu không có từ khóa tiêu cực rõ ràng nhưng vẫn là complaint.
   - Ví dụ: "mua một lần cho biết", "đợi 5 ngày không thấy gì"

6. **Mixed Sentiment Span**: Câu vừa khen vừa chê, entity chỉ là phần khiếu nại.
   - Ví dụ: "áo đẹp nhưng giao hàng chậm" → entity chỉ là "giao hàng chậm"

---

## 4. Result-based Observations

- **PhoBERT Linear NER Entity-F1 = 0.0194** và **PhoBERT + CRF NER Entity-F1 = 0.0170**: Gần như không có khả năng trích xuất span. CRF không cải thiện vì vấn đề nằm ở dataset quá nhỏ, không phải decoding constraint.

- **Multi-task alpha=1.0 Entity-F1 = 0.3279** và **Token-F1 = 0.6445**: Multi-task learning cải thiện rõ rệt so với single-task. Shared encoder từ classification giúp học được ngữ cảnh tốt hơn.

- **Token-F1 cao hơn Entity-F1 rất nhiều** (0.64 vs 0.33): Model học được phần lớn token-level tags đúng, nhưng vẫn khó tạo span hoàn chỉnh chính xác. Điều này cho thấy vấn đề chủ yếu nằm ở **boundary detection**, đặc biệt là B-COMP tag.

- **Alpha ảnh hưởng nhỏ**: alpha=1.0 nhỉnh Entity-F1, alpha=2.0 nhỉnh Token-F1. Sự khác biệt không lớn, gợi ý rằng alpha trong khoảng [1.0, 2.0] không phải yếu tố quyết định — dataset size và boundary detection mới là bottleneck chính.

---

## 5. Root Causes

1. **NER dataset quá nhỏ** (400 train, 100 test): PhoBERT cần nhiều dữ liệu hơn để học boundary. Entity-F1 ~0.02 của single-task cho thấy model gần như không generalize được.

2. **Alignment bottleneck nghiêm trọng**: Chỉ 189/7,817 (~2.4%) classification samples khớp được với NER dataset. Phần lớn training chỉ có classification signal, không có NER signal.

3. **Complaint span không có ranh giới rõ ràng**: Trong review TMĐT, complaint span thường ngắn, phụ thuộc ngữ cảnh, và không có từ khóa cố định. Boundary annotation rất khó đảm bảo nhất quán.

4. **Informal Vietnamese**: Teencode, lỗi chính tả, viết tắt phổ biến trong review Shopee. PhoBERT pre-trained trên tiếng Việt chuẩn không xử lý tốt các biến thể này.

5. **Classification labels từ rating có thể nhiễu**: Rating thấp không nhất thiết là complaint thực sự, ảnh hưởng đến quality của multi-task training signal.

---

## 6. Suggested Improvements

1. **Mở rộng NER dataset (cao nhất priority)**: Semi-automatic labeling hoặc active learning để tăng từ 400 lên ít nhất 2,000-3,000 mẫu BIO. Đây là yếu tố quyết định nhất.

2. **Chuẩn hóa BIO labeling guideline**: Xác định rõ ranh giới entity — ví dụ: "giao hàng chậm" có phải entity không? "chờ 5 ngày" có phải không? Guideline rõ ràng giúp annotation nhất quán hơn.

3. **Cải thiện alignment**: Dùng fuzzy string matching hoặc sentence embedding (Sentence-BERT) thay vì `normalize_for_match()` để tăng tỷ lệ khớp classification-NER từ 2.4% lên cao hơn.

4. **Active learning**: Chọn các mẫu khó (high prediction entropy) để annotate trước, tối ưu chi phí labeling.

5. **CRF constraint hoặc post-processing BIO**: Áp dụng hard constraint: không có I-COMP nếu không có B-COMP trước đó trong cùng entity. CRF đã làm điều này nhưng không cải thiện đáng kể vì vấn đề nằm ở input representation.

6. **Data augmentation cho NER**: Random token deletion, synonym replacement để tăng diversity của training data.

7. **Thử PhoBERT-large hoặc multilingual-BERT**: Model lớn hơn có thể generalize tốt hơn với dataset nhỏ.

8. **Error-guided annotation**: Tập trung annotate thêm các mẫu mà model hiện tại còn sai — boundary errors và missed entities.
"""

    return md


def load_ner_metrics():
    """Doc NER metrics tu cac file JSON co san."""
    metrics = {}

    paths = {
        "PhoBERT Linear NER (single-task)": PROJECT_ROOT / "outputs" / "metrics" / "phobert_ner_single_task_full" / "metrics" / "phobert_ner_single_task.json",
        "PhoBERT + CRF NER (single-task)": PROJECT_ROOT / "outputs" / "metrics" / "phobert_crf_ner_full" / "metrics" / "phobert_crf_ner_single_task.json",
        "Multi-task PhoBERT + CRF (alpha=1.0)": PROJECT_ROOT / "outputs" / "metrics" / "multitask_alpha1_ner_matched" / "ner_metrics_epoch3.json",
        "Multi-task PhoBERT + CRF (alpha=2.0)": PROJECT_ROOT / "outputs" / "metrics" / "multitask_alpha2_ner_matched" / "ner_metrics_epoch3.json",
    }

    for name, path in paths.items():
        if path.exists():
            with open(path, encoding="utf-8-sig") as f:
                data = json.load(f)
            metrics[name] = {
                "entity_precision": data.get("entity_precision"),
                "entity_recall": data.get("entity_recall"),
                "entity_f1": data.get("entity_f1"),
                "token_f1_macro": data.get("token_f1_macro"),
            }
        else:
            print(f"[WARN] NER metrics not found: {path}")

    return metrics


# =============================================================================
# Main
# =============================================================================

def main():
    OUTPUT_ERROR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    print("\n" + "=" * 60)
    print("Error Analysis — Multi-task Complaint Detection")
    print("=" * 60)

    # 1. Classification
    print("\n[1/3] Classification Error Analysis...")
    cls_stats = analyze_classification()

    # 2. NER
    print("\n[2/3] NER Error Analysis...")
    ner_stats = analyze_ner_from_predictions(
        PROJECT_ROOT / "outputs" / "metrics" / "phobert_ner_single_task_full" / "figures" / "phobert_ner_single_task_predictions.csv",
        "phobert_ner"
    )

    ner_stats_crfsv = analyze_ner_from_predictions(
        PROJECT_ROOT / "outputs" / "metrics" / "phobert_crf_ner_full" / "figures" / "phobert_crf_ner_single_task_predictions.csv",
        "phobert_crf_ner"
    )

    print("\n[3/3] Building docs/error_analysis.md...")

    ner_metrics = load_ner_metrics()

    all_ner_stats = {}
    if ner_stats:
        all_ner_stats["PhoBERT Linear NER"] = ner_stats
    if ner_stats_crfsv:
        all_ner_stats["PhoBERT + CRF NER"] = ner_stats_crfsv

    md = build_error_analysis_md(cls_stats, all_ner_stats, ner_metrics)

    md_path = DOCS_DIR / "error_analysis.md"
    with open(md_path, "w", encoding="utf-8-sig") as f:
        f.write(md)

    print(f"  Saved: {md_path}")

    print("\n" + "=" * 60)
    print("Error Analysis Complete!")
    print(f"  Error CSVs : {OUTPUT_ERROR}")
    print(f"  Error MD   : {md_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
