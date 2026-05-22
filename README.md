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
| `data/processed/ner_train.json` | 400 | Gán nhãn BIO tay từ review khiếu nại |
| `data/processed/ner_test.json` | 100 | Tập test NER |

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
│   │   ├── ner_train.json           # NER training set (400 mẫu)
│   │   └── ner_test.json            # NER test set (100 mẫu)
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
│   │   ├── collect_results.py          # Tổng hợp metrics từ nhiều experiments
│   │   └── metrics.py                  # Shared utilities
│   │
│   └── utils/
│       └── utils.py                    # clean_vietnamese_text, helpers
│
├── outputs/
│   ├── metrics/                       # Metrics JSON/CSV từ experiments
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
| PhoBERT + Linear NER | PhoBERT + Linear token classifier (single-task) |
| PhoBERT + CRF NER | PhoBERT + Linear + CRF (single-task) |

---

## Cài đặt

### Yêu cầu

- Python 3.9+
- GPU khuyến nghị (CUDA 11.8+ / CUDA 12.x)
- RAM >= 16GB nếu dùng CPU

### Các bước

```bash
# 1. Clone repo
git clone https://github.com/vngbthang/ie403-Ecom-MultiTask-Complaint-Detection.git
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

### PhoBERT + Linear NER (Single-task)

```bash
python src/training/train_phobert_ner.py \
    --train-json data/processed/ner_train.json \
    --test-json data/processed/ner_test.json \
    --epochs 5 \
    --batch-size 8 \
    --lr 2e-5
```

Output: `outputs/metrics/phobert_ner_single_task_full/metrics/phobert_ner_single_task.json` (hoặc tương tự trong thư mục con của `outputs/metrics/`)

### PhoBERT + CRF NER (Single-task)

```bash
python src/training/train_phobert_crf_ner.py \
    --train-json data/processed/ner_train.json \
    --test-json data/processed/ner_test.json \
    --epochs 5 \
    --batch-size 8 \
    --lr 2e-5
```

Output: `outputs/metrics/phobert_crf_ner_full/metrics/phobert_crf_ner_single_task.json` (hoặc tương tự trong thư mục con của `outputs/metrics/`)

### PhoBERT Multi-task (Classification + NER)

```bash
# alpha = 1.0, only_ner_matched
python src/training/train_multitask.py \
    --cls-path data/processed/shopee_mapped.csv \
    --ner-train-path data/processed/ner_train.json \
    --ner-test-path data/processed/ner_test.json \
    --output-dir checkpoints \
    --epochs 5 \
    --batch-size 8 \
    --lr 2e-5 \
    --alpha 1.0 \
    --only-ner-matched

# alpha = 2.0, only_ner_matched
python src/training/train_multitask.py \
    --cls-path data/processed/shopee_mapped.csv \
    --ner-train-path data/processed/ner_train.json \
    --ner-test-path data/processed/ner_test.json \
    --output-dir checkpoints \
    --epochs 5 \
    --batch-size 8 \
    --lr 2e-5 \
    --alpha 2.0 \
    --only-ner-matched
```

Các tham số quan trọng:

| Tham số | Ý nghĩa | Mặc định |
|---------|---------|-----------|
| `--alpha` | Hệ số nhân NER loss | 1.0 |
| `--only-ner-matched` | Chỉ train trên samples khớp NER | false |
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

### Tổng hợp kết quả

```bash
python src/evaluation/collect_results.py \
    --metrics-dir outputs/metrics \
    --output-dir outputs/metrics
```

Output: `outputs/metrics/classification_summary.csv`, `outputs/metrics/ner_summary.csv`

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

## Kết quả thực nghiệm

> Kết quả được chạy trên tập **Shopee** (7,817 mẫu, split 80/20) và tập **NER test** (`ner_test.json`, 100 mẫu). Model checkpoint không có trong repo.

### Classification (Shopee Test Set, 1,564 mẫu)

| Model | Accuracy | Precision (Macro) | Recall (Macro) | F1 (Macro) | F1 (Complaint) |
|-------|----------|-------------------|----------------|------------|-----------------|
| TF-IDF + **LinearSVM** | **0.9431** | **0.9427** | **0.9429** | **0.9428** | **0.9470** |
| TF-IDF + Logistic Regression | 0.9393 | 0.9386 | 0.9394 | 0.9390 | 0.9431 |
| TF-IDF + Naive Bayes | 0.9341 | 0.9334 | 0.9346 | 0.9339 | 0.9381 |

### NER (ner_test.json, 100 mẫu)

> Chỉ **189/7,817** classification samples khớp được với NER dataset qua `normalize_for_match()`. Multi-task model huấn luyện với `--only-ner-matched`.

| Model | Alpha | Entity Precision | Entity Recall | Entity F1 | Token F1 (Macro) |
|-------|-------|-----------------|---------------|-----------|------------------|
| PhoBERT + Linear NER (single-task) | — | — | — | 0.0194 | 0.4231 |
| PhoBERT + CRF NER (single-task) | — | — | — | 0.0170 | 0.4172 |
| **Multi-task PhoBERT + CRF** | 1.0 | 0.2841 | **0.3876** | **0.3279** | 0.6445 |
| **Multi-task PhoBERT + CRF** | 2.0 | **0.3003** | 0.3527 | 0.3244 | **0.6627** |

> Baseline single-task chưa ghi precision/recall — bảng chủ yếu nhấn mạnh Entity F1 và Token F1 để thể hiện sự khác biệt với multi-task.

### Ablation Study

> Chỉ thử 2 cấu hình `alpha=1.0` và `alpha=2.0` với `--only-ner-matched`. Chưa chạy trên UIT-ViOCD test set.

---

## Key Findings

1. **LinearSVM là classical baseline tốt nhất** cho bài toán classification trên Shopee (F1-Macro 0.9428, F1-Complaint 0.9470). TF-IDF n-grams (1,2) đủ hiệu quả với dữ liệu complaint detection trong thương mại điện tử.

2. **Multi-task PhoBERT + CRF cải thiện rõ rệt so với single-task baseline**: PhoBERT Linear NER và PhoBERT + CRF NER single-task đạt Entity-F1 chỉ ~0.02 (gần như không có khả năng trích xuất span). Trong khi multi-task đạt Entity-F1 ~0.33 và Token-F1 ~0.66. Điều này cho thấy multi-task learning có lợi khi dataset NER nhỏ.

3. **Alpha ảnh hưởng khác nhau lên entity và token level**:
   - `alpha=1.0` nhỉnh hơn về **Entity-F1** (0.3279 vs 0.3244) và **Entity Recall** (0.3876 vs 0.3527)
   - `alpha=2.0` nhỉnh hơn về **Entity Precision** (0.3003 vs 0.2841) và **Token-F1** (0.6627 vs 0.6445)
   - Kết quả gợi ý rằng alpha lớn hơn có thể giúp model tăng precision và Token-F1, tuy nhiên cần thêm ablation với nhiều giá trị alpha để kết luận chắc chắn.

4. **Dataset alignment là bottleneck lớn**: Chỉ 189/7,817 samples (~2.4%) được khớp giữa classification và NER, giới hạn hiệu quả của multi-task learning.

---

## Hạn chế và hướng cải thiện

1. **NER dataset nhỏ**: Chỉ 400 mẫu train và 100 mẫu test — không đủ để PhoBERT học đầy đủ các complaint patterns đa dạng. PhoBERT single-task NER baseline đạt Entity-F1 chỉ ~0.02, cho thấy model gần như không thể trích xuất span khi thiếu dữ liệu.

2. **Alignment bottleneck**: Chỉ 189/7,817 (~2.4%) classification samples khớp được với NER dataset qua `normalize_for_match()`. Phần lớn samples chỉ được train classification, không train NER — giảm hiệu quả của shared encoder.

3. **Entity boundary khó xác định**: Complaint spans trong review thương mại điện tử thường ngắn, mơ hồ, hoặc phụ thuộc ngữ cảnh. Labeling thủ công theo BIO rất tốn công và có thể không nhất quán giữa các annotators.

4. **Classification labels từ rating**: Shopee labels được gán tự động từ rating (1-2★ = complaint, 4-5★ = normal). Không chính xác hoàn toàn vì rating thấp có thể do nhiều lý do khác ngoài complaint thực sự.

5. **Không có cross-validation**: Chỉ dùng fixed train/test split. Kết quả có thể biến đổi tùy split.

### Hướng cải thiện

1. **Mở rộng NER dataset**: Semi-automatic labeling hoặc active learning để tăng số mẫu BIO.
2. **Cải thiện alignment**: Dùng fuzzy matching hoặc sentence embedding để tăng tỷ lệ khớp classification-NER.
3. **Cross-validation** (5-fold) để đánh giá ổn định hơn.
4. **Thử PhoBERT-large** thay vì phobert-base-v2.
5. **Chạy ablation đầy đủ**: Nhiều giá trị alpha hơn (0.5, 1.5, 3.0), nhiều epoch hơn.
6. **Error analysis chi tiết** trên từng loại lỗi (boundary, missed, spurious).
7. **Domain adaptation** nếu muốn model hoạt động tốt trên domain Shopee khác nhau.

---

## Checkpoint không push GitHub

Các file checkpoint (`.pt`) trong `checkpoints/` và `outputs/` được liệt kê trong `.gitignore`, **không bao giờ được push lên GitHub**.

Để chia sẻ checkpoint:
- Upload lên Google Drive / Hugging Face Hub
- Hoặc dùng Git LFS (`git lfs track "*.pt"`)

---

## License

MIT License
