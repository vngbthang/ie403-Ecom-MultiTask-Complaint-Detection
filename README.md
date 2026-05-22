# Multi-task Complaint Detection cho E-Commerce tiếng Việt

Đồ án nghiên cứu xây dựng mô hình **PhoBERT-based Multi-task Learning** giải quyết đồng thời hai bài toán trên dữ liệu bình luận thương mại điện tử tiếng Việt:

1. **Classification**: Nhận diện bình luận có chứa khiếu nại (Complaint) hay không (Non-Complaint)
2. **NER**: Trích xuất cụm từ thể hiện nội dung khiếu nại theo chuẩn BIO (B-COMP, I-COMP, O)

---

## Mục lục

- [Dữ liệu](#dữ-liệu)
- [Cấu trúc repo](#cấu-trúc-repo)
- [Kiến trúc model](#kiến-trúc-model)
- [Cài đặt](#cài-đặt)
- [Huấn luyện](#huấn-luyện)
- [Đánh giá](#đánh-giá)
- [Demo Streamlit](#demo-streamlit)
- [Kết quả](#kết-quả)
- [Hạn chế và hướng cải thiện](#hạn-chế-và-hướng-cải-thiện)

---

## Dữ liệu

### Classification Datasets

| Dataset | File | Mẫu | Mô tả |
|---------|------|------|--------|
| **UIT-ViOCD** | `data/raw/UIT-ViOCD/{train,val,test}.csv` | ~4,300 train | Tiêu chuẩn, từ bài báo ViOCD |
| **Shopee Reviews** | `data/processed/shopee_mapped.csv` | ~7,800 | Gán nhãn từ rating (1-2★ = complaint, 4-5★ = normal) |

### NER Dataset

| File | Mẫu | Mô tả |
|------|------|--------|
| `data/processed/ner_train.json` | ~800+ | Gán nhãn BIO tay từ review khiếu nại |
| `data/processed/ner_test.json` | ~200+ | Tập test NER |

**Định dạng NER JSON:**

```json
{
  "tokens": ["đặt", "hàng", "mấy", "ngày", "không", "thấy", ...],
  "ner_tags": ["O", "O", "O", "O", "B-COMP", "I-COMP", ...]
}
```

**Nhãn BIO:**
- `O`: Token không phải thực thể khiếu nại
- `B-COMP`: Token bắt đầu một cụm từ khiếu nại
- `I-COMP`: Token tiếp theo trong cùng cụm khiếu nại

---

## Cấu trúc repo

```
ie403-Ecom-MultiTask-Complaint-Detection/
├── app.py                          # Demo Streamlit
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   │   ├── ShopeeReviewsSentiment/  # Dữ liệu gốc Shopee
│   │   └── UIT-ViOCD/               # Dữ liệu tiêu chuẩn ViOCD
│   ├── processed/
│   │   ├── shopee_mapped.csv        # Shopee đã gán nhãn
│   │   ├── ner_train.json           # NER training set
│   │   └── ner_test.json            # NER test set
│   └── splits/                      # Chia train/test cho Shopee
│
├── docs/
│   ├── bio_labeling_guideline.md
│   ├── experiment_plan.md
│   └── error_analysis.md
│
├── notebooks/                       # Jupyter notebooks EDA
│
├── src/
│   ├── data_processing/
│   │   ├── multitask_dataset.py     # Dataset multi-task alignment
│   │   ├── prepare_annotation.py
│   │   ├── convert_ls_to_hf.py
│   │   ├── convert_bio_to_ner.py
│   │   └── map_labels.py
│   │
│   ├── models/
│   │   ├── multitask_model.py       # PhoBERT + CRF multi-task
│   │   ├── phobert_token_classifier.py  # PhoBERT + Linear NER
│   │   └── phobert_crf_ner.py       # PhoBERT + CRF NER single-task
│   │
│   ├── training/
│   │   ├── train_classical_baselines.py   # TF-IDF + LR / SVM / NB
│   │   ├── train_multitask.py             # Multi-task training
│   │   ├── train_phobert_ner.py           # PhoBERT + Linear NER
│   │   ├── train_phobert_crf_ner.py       # PhoBERT + CRF NER
│   │   └── diagnose_alignment.py           # Kiểm tra alignment
│   │
│   ├── evaluation/
│   │   ├── evaluate_classification.py  # Classification metrics
│   │   ├── evaluate_ner.py             # NER metrics (entity + token)
│   │   ├── error_analysis.py           # Phân tích lỗi
│   │   └── metrics.py                  # Shared utilities
│   │
│   └── utils/
│       └── utils.py                    # clean_vietnamese_text, helpers
│
├── outputs/
│   ├── metrics/                       # Metrics JSON/SV từ experiments
│   ├── figures/                       # Confusion matrix, bar charts
│   └── error_samples/                 # Error analysis CSVs
│
└── checkpoints/                       # Model checkpoints (KHÔNG push Git)
```

---

## Kiến trúc model

### PhoBERT-based Multi-task (Proposed)

```
vinai/phobert-base-v2
    │
    ├── <s> token ──► Linear(768 → 2)        → Classification (Complaint / Non-Complaint)
    │
    └── Full sequence ──► Linear(768 → 3) ──► CRF(3) → NER tags (O / B-COMP / I-COMP)
```

**Hàm mất mát:**

```
Total_Loss = CrossEntropy(cls_logits, class_labels) + α × NER_Loss(CRF)
```

### Baseline Models

| Model | Mô tả |
|-------|--------|
| TF-IDF + Logistic Regression | Bag-of-n-grams (1,2), max 10,000 features |
| TF-IDF + Linear SVM | LinearSVC + CalibratedClassifierCV |
| TF-IDF + Naive Bayes | MultinomialNB, alpha=0.1 |
| PhoBERT + Linear | PhoBERT + Linear token classifier |
| PhoBERT + CRF | PhoBERT + Linear + CRF (single-task) |

---

## Cài đặt

### Yêu cầu

- Python 3.9+
- GPU khuyến nghị (CUDA 11.8+ / CUDA 12.x)
- RAM >= 16GB nếu dùng CPU

### Các bước

```bash
# 1. Clone repo
git clone https://github.com/your-repo/ie403-Ecom-MultiTask-Complaint-Detection.git
cd ie403-Ecom-MultiTask-Complaint-Detection

# 2. Tạo virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# Hoặc: .\.venv\Scripts\Activate  # Windows

# 3. Cài đặt dependencies
pip install -r requirements.txt

# 4. Tải PhoBERT tokenizer (tự động khi chạy script)
# Lần đầu chạy sẽ tải ~400MB

# 5. Kiểm tra GPU
python -c "import torch; print('CUDA:', torch.cuda.is_available())"
```

---

## Huấn luyện

### Classical Baselines (TF-IDF)

```bash
# Shopee (mặc định) — tự chia 80/20
python src/training/train_classical_baselines.py

# UIT-ViOCD với split có sẵn
python src/training/train_classical_baselines.py \
    --train data/raw/UIT-ViOCD/train.csv \
    --test data/raw/UIT-ViOCD/test.csv

# Tùy chỉnh TF-IDF
python src/training/train_classical_baselines.py \
    --train data/raw/UIT-ViOCD/train.csv \
    --max-features 15000 \
    --ngram-range "1,3"
```

Output: `outputs/metrics/classical_baselines.csv`, `outputs/figures/`

### PhoBERT + Linear NER (Single-task, no CRF)

```bash
python src/training/train_phobert_ner.py \
    --train-json data/processed/ner_train.json \
    --test-json data/processed/ner_test.json \
    --epochs 5 \
    --batch-size 8 \
    --lr 2e-5
```

Output: `outputs/metrics/phobert_ner_single_task.json`

### PhoBERT + CRF NER (Single-task, có CRF)

```bash
python src/training/train_phobert_crf_ner.py \
    --train-json data/processed/ner_train.json \
    --test-json data/processed/ner_test.json \
    --epochs 5 \
    --batch-size 8 \
    --lr 2e-5
```

Output: `outputs/metrics/phobert_crf_ner_single_task.json`

### PhoBERT Multi-task (Classification + NER)

```bash
python src/training/train_multitask.py \
    --cls-path data/processed/shopee_mapped.csv \
    --ner-train-path data/processed/ner_train.json \
    --ner-test-path data/processed/ner_test.json \
    --output-dir checkpoints \
    --epochs 5 \
    --batch-size 8 \
    --lr 2e-5 \
    --alpha 1.0
```

Các tham số quan trọng:

| Tham số | Ý nghĩa | Mặc định |
|---------|---------|-----------|
| `--alpha` | Hệ số nhân NER loss | 1.0 |
| `--use-weighted-sampler` | Ưu tiên mẫu có complaint | true |
| `--max-len` | Độ dài tối đa chuỗi | 256 |

Output: `checkpoints/checkpoint_epoch_{N}.pt`, `checkpoints/ner_metrics_epoch{N}.json`

### Resume từ checkpoint

```bash
python src/training/train_multitask.py \
    --resume-checkpoint checkpoints/checkpoint_epoch_3.pt \
    --cls-path data/processed/shopee_mapped.csv \
    --ner-train-path data/processed/ner_train.json \
    --ner-test-path data/processed/ner_test.json \
    --epochs 3
```

---

## Đánh giá

### Classification Metrics

```bash
python -m src.evaluation.evaluate_classification \
    --predictions outputs/metrics/Shopee/LogisticRegression/predictions.csv
```

### NER Metrics

```bash
python -m src.evaluation.evaluate_ner \
    --predictions outputs/figures/phobert_crf_ner_single_task_predictions.csv \
    --output-dir outputs/evaluation/ner
```

### Error Analysis (Multi-task model)

```bash
python src/evaluation/error_analysis.py \
    --checkpoint checkpoints/checkpoint_epoch_5.pt \
    --ner-test data/processed/ner_test.json \
    --cls-test data/raw/UIT-ViOCD/test.csv \
    --output-dir outputs/error_samples
```

Output: `outputs/error_samples/` chứa:
- `false_positive_classification.csv`
- `false_negative_classification.csv`
- `ner_boundary_errors.csv`
- `ner_missed_entities.csv`
- `ner_spurious_entities.csv`

---

## Demo Streamlit

```bash
# Cài thêm streamlit
pip install streamlit

# Chạy app (cần có checkpoint trong thư mục checkpoints/)
streamlit run app.py --server.port 8501
```

App cho phép:
- Chọn checkpoint từ dropdown hoặc nhập đường dẫn
- Nhập bình luận sản phẩm để phân tích
- Xem kết quả phân loại (Complaint / Non-Complaint)
- Xem các cụm từ khiếu nại được trích xuất (BIO spans)
- Xem chi tiết từng token và nhãn BIO

> **Lưu ý:** App yêu cầu checkpoint đã được huấn luyện. Checkpoint không có trong repo — xem mục [Checkpoint](#checkpoint-không-push-github).

---

## Kết quả

> **Chưa có kết quả huấn luyện.** Bảng dưới là placeholder chờ chạy experiments thực tế trên GPU.

### Classification (UIT-ViOCD Test Set)

| Model | Accuracy | Precision (Macro) | Recall (Macro) | F1 (Macro) | F1 (Complaint) |
|-------|----------|-------------------|----------------|------------|----------------|
| TF-IDF + Logistic Regression | — | — | — | — | — |
| TF-IDF + Linear SVM | — | — | — | — | — |
| TF-IDF + Naive Bayes | — | — | — | — | — |
| PhoBERT Classification | — | — | — | — | — |
| **PhoBERT Multi-task** | — | — | — | — | — |

### NER (ner_test.json)

| Model | Entity Precision | Entity Recall | Entity F1 | Token F1 (Macro) |
|-------|-----------------|---------------|-----------|------------------|
| PhoBERT + Linear | — | — | — | — |
| PhoBERT + CRF | — | — | — | — |
| **PhoBERT Multi-task** | — | — | — | — |

### Ablation Study (Multi-task)

| Alpha | NER Loss Weight | Entity F1 | F1 (Macro) |
|-------|----------------|-----------|------------|
| 0.5 | 0.5× | — | — |
| 1.0 | 1.0× | — | — |
| 1.5 | 1.5× | — | — |
| 2.0 | 2.0× | — | — |

---

## Hạn chế và hướng cải thiện

### Hạn chế hiện tại

1. **Chưa huấn luyện thực tế**: Toàn bộ code đã sẵn sàng nhưng chưa chạy experiments trên GPU.
2. **NER dataset nhỏ**: Dữ liệu gán nhãn BIO còn hạn chế (~1,000 mẫu), có thể gây overfitting.
3. **Alignment độ chính xác chưa cao**: Việc khớp classification samples với NER samples qua `normalize_for_match()` có thể miss hoặc sai một số cases.
4. **Không có cross-validation**: Chỉ dùng fixed train/val/test split.
5. **Shopee labels từ rating**: Có thể không chính xác hoàn toàn (rating thấp không phải lúc nào cũng là complaint thực sự).
6. **Không dùng data augmentation**.

### Hướng cải thiện

1. **Huấn luyện đầy đủ experiments** trên GPU với nhiều epoch và hyperparameter tuning.
2. **Tăng NER dataset**: Sử dụng semi-automatic labeling hoặc active learning.
3. **Cross-validation** (5-fold) để đánh giá ổn định hơn.
4. **Thử PhoBERT-large** thay vì phobert-base-v2.
5. **Cải thiện alignment** bằng sentence-level matching thay vì word-normalized matching.
6. **Error analysis chi tiết** trên từng loại lỗi (boundary, missed, spurious).
7. **Thêm domain adaptation** nếu muốn model hoạt động tốt trên domain Shopee khác nhau.

---

## Checkpoint không push GitHub

Các file checkpoint (`.pt`) trong `checkpoints/` và `outputs/` được liệt kê trong `.gitignore`, **không bao giờ được push lên GitHub**.

Để chia sẻ checkpoint:
- Upload lên Google Drive / Hugging Face Hub
- Hoặc dùng Git LFS (`git lfs track "*.pt"`)

---

## License

MIT License
