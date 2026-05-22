# Experiment Plan — Multi-task Complaint Detection

## 1. Mục tiêu

Đề xuất mô hình **PhoBERT-based Multi-task Learning** cho bài toán:
1. **Classification**: Nhận diện bình luận có khiếu nại (complaint) hay không (non-complaint)
2. **NER**: Rút trích cụm từ thể hiện nội dung khiếu nại (BIO tagging: O, B-COMP, I-COMP)

So sánh với các baseline: TF-IDF + Logistic Regression, TF-IDF + SVM, BiLSTM, PhoBERT Classification, PhoBERT NER.

---

## 2. Datasets

### 2.1 Classification Datasets

| Dataset | File | Split | Samples | Description |
|---------|------|-------|---------|-------------|
| **UIT-ViOCD** | `data/raw/UIT-ViOCD/train.csv`, `val.csv`, `test.csv` | Provided | ~11k total | Tiêu chuẩn, từ bài báo ViOCD |
| **Shopee Reviews** | `data/processed/shopee_mapped.csv` | To split | ~7.8k | Gán nhãn từ rating (1-2★=complaint, 4-5★=normal) |

### 2.2 NER Dataset

| Dataset | File | Split | Samples | Description |
|---------|------|-------|---------|-------------|
| **BIO Annotations** | `data/processed/ner_train.json`, `ner_test.json` | 80/20 | ~1-2k | Gán nhãn BIO tay từ review khiếu nại |

---

## 3. Experiment Groups

### Group 1: Classification trên UIT-ViOCD
Huấn luyện và đánh giá **04-05 phương pháp** trên tập test UIT-ViOCD.

| # | Method | Script/Notebook | Notes |
|---|--------|----------------|-------|
| 1.1 | TF-IDF + Logistic Regression | `src/training/train_logistic.py` | Baseline truyền thống |
| 1.2 | TF-IDF + SVM | `src/training/train_svm.py` | Linear SVM với class_weight='balanced' |
| 1.3 | BiLSTM | `src/training/train_bilstm.py` | Embedding + BiLSTM + Dense |
| 1.4 | PhoBERT Classification | `src/training/train_phobert_classification.py` | Fine-tune `vinai/phobert-base-v2` |
| 1.5 | **Proposed: Multi-task PhoBERT (CLS head)** | `src/training/train_multitask.py` | Classification head từ multi-task model |

**Metrics**: Accuracy, Precision, Recall, F1-score (per-class + macro), Confusion Matrix.

### Group 2: Classification trên Shopee Reviews
Huấn luyện và đánh giá trên Shopee (train/val/test split).

| # | Method | Script/Notebook | Notes |
|---|--------|----------------|-------|
| 2.1 | TF-IDF + Logistic Regression | `src/training/train_logistic.py` | |
| 2.2 | TF-IDF + SVM | `src/training/train_svm.py` | |
| 2.3 | BiLSTM | `src/training/train_bilstm.py` | |
| 2.4 | PhoBERT Classification | `src/training/train_phobert_classification.py` | |
| 2.5 | **Proposed: Multi-task PhoBERT (CLS head)** | `src/training/train_multitask.py` | |

**Metrics**: Accuracy, Precision, Recall, F1-score (per-class + macro), Confusion Matrix.

### Group 3: NER trên BIO Subset
Huấn luyện và đánh giá trên `ner_train.json` / `ner_test.json`.

| # | Method | Script/Notebook | Notes |
|---|--------|----------------|-------|
| 3.1 | Rule-based Keyword Matching | `src/training/train_rule_based_ner.py` | Baseline đơn giản, match từ khóa |
| 3.2 | PhoBERT Token Classification (no CRF) | `src/training/train_phobert_ner.py` | Linear head, không CRF |
| 3.3 | PhoBERT + CRF | `src/training/train_phobert_ner.py` | Linear + CRF layer |
| 3.4 | **Proposed: Multi-task PhoBERT + CRF** | `src/training/train_multitask.py` | Multi-task với CRF |

**Metrics**: Entity-level Precision, Recall, F1 (seqeval), Token-level F1, Classification Report cho O/B-COMP/I-COMP.

### Group 4: Ablation Study
Phân tích đóng góp từng thành phần trong multi-task model.

| # | Experiment | Purpose |
|---|-----------|---------|
| 4.1 | Multi-task (alpha=0.5) | Giảm trọng số NER loss |
| 4.2 | Multi-task (alpha=1.0) | Cân bằng classification + NER |
| 4.3 | Multi-task (alpha=1.5) | Tăng trọng số NER loss |
| 4.4 | Multi-task (alpha=2.0) | NER loss có trọng số cao |
| 4.5 | Multi-task (no CRF) | Chỉ có Linear head, không CRF |
| 4.6 | Multi-task (weighted sampler) vs (uniform) | Ảnh hưởng của sampling strategy |

---

## 4. Output Files

Mỗi experiment lưu kết quả vào `outputs/metrics/` và `outputs/figures/`:

```
outputs/
├── metrics/
│   ├── cls_uocvd_logistic.json
│   ├── cls_uocvd_svm.json
│   ├── cls_uocvd_bilstm.json
│   ├── cls_uocvd_phobert.json
│   ├── cls_uocvd_multitask.json
│   ├── cls_shopee_logistic.json
│   ├── ...
│   └── ner_*.json
├── figures/
│   ├── cls_uocvd_confusion_matrix.png
│   ├── cls_shopee_confusion_matrix.png
│   ├── ner_classification_report.png
│   └── ...
└── error_samples/
    ├── ner_errors_boundary.csv
    ├── ner_errors_mixed_sentiment.csv
    └── ner_errors_informal.csv
```

### Metrics JSON format:

```json
{
  "experiment_name": "cls_uocvd_multitask",
  "dataset": "UIT-ViOCD",
  "split": "test",
  "num_samples": 1234,
  "accuracy": 0.9123,
  "precision": 0.9089,
  "recall": 0.9156,
  "f1_macro": 0.9112,
  "f1_complaint": 0.9234,
  "f1_non_complaint": 0.8990,
  "classification_report": "...",
  "confusion_matrix": [[TN, FP], [FN, TP]]
}
```

---

## 5. Hướng dẫn chạy

### 5.1 Classification Baseline (UIT-ViOCD)

```bash
# Logistic Regression
python src/training/train_logistic.py \
    --data data/raw/UIT-ViOCD/train.csv \
    --output outputs/metrics/cls_uocvd_logistic.json

# SVM
python src/training/train_svm.py \
    --data data/raw/UIT-ViOCD/train.csv \
    --output outputs/metrics/cls_uocvd_svm.json

# BiLSTM
python src/training/train_bilstm.py \
    --data data/raw/UIT-ViOCD/train.csv \
    --output outputs/metrics/cls_uocvd_bilstm.json

# PhoBERT Classification
python src/training/train_phobert_classification.py \
    --data data/raw/UIT-ViOCD/train.csv \
    --output outputs/metrics/cls_uocvd_phobert.json
```

### 5.2 Multi-task Training

```bash
python src/training/train_multitask.py \
    --cls-path data/raw/UIT-ViOCD/train.csv \
    --ner-train-path data/processed/ner_train.json \
    --ner-test-path data/processed/ner_test.json \
    --output-dir checkpoints \
    --epochs 5 \
    --batch-size 8 \
    --alpha 1.0
```

### 5.3 Ablation

```bash
# Alpha sweep
for alpha in 0.5 1.0 1.5 2.0; do
    python src/training/train_multitask.py \
        --cls-path data/raw/UIT-ViOCD/train.csv \
        --ner-train-path data/processed/ner_train.json \
        --ner-test-path data/processed/ner_test.json \
        --alpha $alpha \
        --output outputs/metrics/ner_multitask_alpha_${alpha}.json
done
```

---

## 6. Expected Timeline

| Week | Tasks |
|------|-------|
| 1 | Run Group 1 & 2 (Classification baselines on both datasets) |
| 2 | Run Group 3 (NER baselines) |
| 3 | Run Group 4 (Ablation study) |
| 4 | Error analysis & report writing |

---

## 7. Ghi chú

- UIT-ViOCD đã có sẵn train/val/test split từ bài báo gốc.
- Shopee cần chia train/val/test bằng `src/data_processing/prepare_shopee_split.py`.
- NER dataset cần align với classification data qua `normalize_for_match()`.
- Fixed seed: `torch.manual_seed(42)` + `numpy.random.seed(42)`.
- Kết quả chưa có sẵn — cần chạy experiments thực tế trên GPU.
