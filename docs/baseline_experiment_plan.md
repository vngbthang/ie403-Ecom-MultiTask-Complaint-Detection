# Baseline experiment plan for UIT-ViOCD complaint span extraction

## Mục tiêu

Đề tài cần so sánh ít nhất 04 phương pháp trên cùng bài toán complaint span extraction. Các thí nghiệm dưới đây đều dùng dữ liệu derived from UIT-ViOCD, không dùng Shopee Reviews và không dùng rating mapping.

Bài toán chung:

- Input: Vietnamese e-commerce review.
- Output: complaint spans hoặc BIO labels `O`, `B-COMP`, `I-COMP`.
- Evaluation chính: Entity Precision, Entity Recall, Entity-F1, Token-F1 macro.

Lưu ý quan trọng:

- Full AI-assisted complaint span labels không phải fully human gold-standard labels.
- Kết quả nên được diễn giải là evaluation trên constructed AI-assisted span dataset.

---

## 1. Rule-based keyword span extractor

### Input

- Review text từ UIT-ViOCD complaint span dataset.
- Có thể dùng tokenized text hoặc raw text.

### Output

- Predicted complaint spans hoặc token-level BIO tags.
- Span có thể được tạo bằng cách tìm các cụm chứa keyword complaint như:
  - `lỗi`
  - `không được`
  - `không có`
  - `tệ`
  - `thất vọng`
  - `chậm`
  - `lag`
  - `đơ`
  - `thiếu`
  - `sai`
  - `hư`
  - `bể`
  - `lừa đảo`

### Training/evaluation data

- Không cần training.
- Evaluate trên cùng test split của:
  - Pilot100 nếu cần smoke check.
  - Full AI-assisted complaint span dataset là chính.

### Metrics

- Entity Precision / Recall / F1.
- Token-F1 macro.
- Có thể thêm exact-match span count và partial-overlap count nếu muốn phân tích sâu.

### Expected role in comparison

- Baseline đơn giản nhất.
- Cho thấy mức hiệu quả của keyword matching so với mô hình học máy.
- Dự kiến precision có thể ổn với keyword mạnh, nhưng recall và boundary quality thấp.

### Implementation difficulty

- Thấp.
- Không cần GPU.
- Có thể chạy local nhanh.

### Files/scripts cần tạo hoặc tận dụng

Tạo mới:

- `src/evaluation/rule_based_span_baseline.py`

Tận dụng:

- `data/processed/uit_viocd_full_complaint_bio.jsonl`
- `data/processed/uit_viocd_full_complaint_ner_test.json`
- Có thể tận dụng logic metric trong `src/training/train_phobert_ner.py` nếu tách được evaluation helper.

---

## 2. BiLSTM NER token classifier hoặc BiLSTM-CRF

### Input

- Token sequence từ NER JSON:
  - `tokens`
  - `ner_tags`

### Output

- BIO tag sequence cho từng token.

### Training/evaluation data

- Train/val/test trên:
  - `data/processed/uit_viocd_full_complaint_ner_train.json`
  - `data/processed/uit_viocd_full_complaint_ner_val.json`
  - `data/processed/uit_viocd_full_complaint_ner_test.json`

Có thể thử Pilot100/Pilot300 nếu muốn so sánh theo quy mô dữ liệu, nhưng full dataset nên là kết quả chính.

### Metrics

- Entity Precision / Recall / F1.
- Token-F1 macro.
- Average loss nếu training script hỗ trợ.

### Expected role in comparison

- Classical neural baseline.
- Đứng giữa rule-based và transformer-based PhoBERT.
- Nếu dùng BiLSTM-CRF, có thể kiểm tra lợi ích của sequence decoding với BIO constraints.

### Implementation difficulty

- Trung bình.
- Cần embedding:
  - đơn giản nhất: trainable token embeddings từ vocabulary của train split.
  - tốt hơn: pretrained Vietnamese word embeddings nếu repo đã có, nhưng không nên thêm phụ thuộc lớn nếu không cần.
- BiLSTM-CRF khó hơn BiLSTM softmax vì cần CRF layer.

### Files/scripts cần tạo hoặc tận dụng

Tạo mới nếu repo chưa có:

- `src/models/bilstm_ner.py`
- `src/training/train_bilstm_ner.py`

Tận dụng:

- NER JSON splits:
  - `data/processed/uit_viocd_full_complaint_ner_train.json`
  - `data/processed/uit_viocd_full_complaint_ner_val.json`
  - `data/processed/uit_viocd_full_complaint_ner_test.json`
- Metric/export style từ `src/training/train_phobert_ner.py`.

Nếu repo đã có CRF dependency thì có thể làm BiLSTM-CRF. Nếu chưa có, ưu tiên BiLSTM token classifier để giảm rủi ro.

---

## 3. PhoBERT NER without class weights

### Input

- NER JSON train/val/test.
- PhoBERT tokenizer input từ tokens/review text theo script hiện có.

### Output

- BIO tag sequence `O`, `B-COMP`, `I-COMP`.
- Predictions CSV và metrics JSON.

### Training/evaluation data

Đề xuất chạy thêm trên full dataset:

- `data/processed/uit_viocd_full_complaint_ner_train.json`
- `data/processed/uit_viocd_full_complaint_ner_val.json`
- `data/processed/uit_viocd_full_complaint_ner_test.json`

Hiện đã có kết quả Pilot100 unweighted:

- Entity-F1 = 0.0000
- Token-F1 macro = 0.3002

Nhưng để so sánh công bằng với proposed method, nên có thêm Full unweighted.

### Metrics

- Entity Precision / Recall / F1.
- Token-F1 macro.
- Average loss.
- Prediction label distribution.

### Expected role in comparison

- Transformer baseline hiện đại không dùng class weights.
- Dùng để chứng minh Weighted CrossEntropy giúp cải thiện so với PhoBERT mặc định.

### Implementation difficulty

- Thấp đến trung bình.
- Training script đã có.
- Cần GPU nếu chạy full dataset.

### Files/scripts cần tạo hoặc tận dụng

Tận dụng:

- `src/training/train_phobert_ner.py`
- `scripts/run_pilot_100_phobert_ner_smoke.py` làm mẫu runner.

Có thể tạo runner mới:

- `scripts/run_full_phobert_ner_unweighted.py`

Output đề xuất:

- `outputs/metrics/uit_viocd_full_complaint_phobert_ner_unweighted_5epoch/`

---

## 4. PhoBERT NER with class weights as proposed method

### Input

- Full NER train/val/test JSON.

### Output

- BIO predictions.
- Metrics JSON.
- Predictions CSV.

### Training/evaluation data

Đã có kết quả chính trên full AI-assisted dataset:

- Train records: 2,280
- Test records: 291

Files:

- `data/processed/uit_viocd_full_complaint_ner_train.json`
- `data/processed/uit_viocd_full_complaint_ner_val.json`
- `data/processed/uit_viocd_full_complaint_ner_test.json`

### Metrics

- Entity Precision = 0.7937
- Entity Recall = 0.9045
- Entity-F1 = 0.8455
- Token-F1 macro = 0.8620
- Avg loss = 0.2486

### Expected role in comparison

- Proposed method.
- Cho thấy hiệu quả của PhoBERT + class-weighted CrossEntropyLoss trên full AI-assisted complaint span dataset.

### Implementation difficulty

- Đã hoàn tất.
- Chỉ cần giữ kết quả và chuẩn hóa bảng báo cáo.

### Files/scripts cần tạo hoặc tận dụng

Tận dụng:

- `src/training/train_phobert_ner.py`
- `outputs/metrics/uit_viocd_full_complaint_phobert_ner_weighted_5epoch/metrics/phobert_ner_single_task.json`
- `outputs/metrics/uit_viocd_full_complaint_phobert_ner_weighted_5epoch/figures/phobert_ner_single_task_predictions.csv`
- `outputs/metrics/summary/ner_experiment_summary.md`

---

## Dataset settings đề xuất

### Pilot100

Mục đích:

- Smoke test pipeline.
- Kiểm tra model có học được không khi dữ liệu rất nhỏ.

Files:

- `data/processed/uit_viocd_pilot_100_ner.json`
- `data/processed/uit_viocd_pilot_100_ner_train.json`
- `data/processed/uit_viocd_pilot_100_ner_val.json`
- `data/processed/uit_viocd_pilot_100_ner_test.json`

Hiện có kết quả:

- PhoBERT unweighted: Entity-F1 0.0000
- PhoBERT weighted: Entity-F1 0.1370

### Pilot300

Mục đích:

- Trung gian giữa pilot100 và full dataset.
- Hữu ích nếu cần chứng minh tăng dữ liệu giúp cải thiện dần.

Files đã có:

- `data/processed/uit_viocd_pilot_300_ner.json`
- `data/processed/uit_viocd_pilot_300_ner_train.json`
- `data/processed/uit_viocd_pilot_300_ner_val.json`
- `data/processed/uit_viocd_pilot_300_ner_test.json`

Ưu tiên thấp hơn full dataset nếu thời gian hạn chế.

### Full AI-assisted complaint span dataset

Mục đích:

- Dataset chính cho kết quả cuối.
- Nên dùng cho bảng so sánh 04 phương pháp.

Files:

- `data/processed/uit_viocd_full_complaint_ner.json`
- `data/processed/uit_viocd_full_complaint_ner_train.json`
- `data/processed/uit_viocd_full_complaint_ner_val.json`
- `data/processed/uit_viocd_full_complaint_ner_test.json`

Summary:

- Total records: 2,854
- Train: 2,280
- Val: 283
- Test: 291
- Total tokens: 109,783
- COMP token ratio: 75.15%

---

## Đề xuất bảng so sánh cuối cùng

| Method | Dataset | Uses training | Modern ML | Entity-P | Entity-R | Entity-F1 | Token-F1 | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Rule-based keyword span extractor | Full AI-assisted test | No | No | TBD | TBD | TBD | TBD | Simple lexical baseline |
| BiLSTM NER / BiLSTM-CRF | Full AI-assisted | Yes | Yes | TBD | TBD | TBD | TBD | Neural sequence baseline |
| PhoBERT NER without class weights | Full AI-assisted | Yes | Yes | TBD | TBD | TBD | TBD | Transformer baseline |
| PhoBERT NER with class weights | Full AI-assisted | Yes | Yes | 0.7937 | 0.9045 | 0.8455 | 0.8620 | Proposed method |

---

## Thứ tự chạy thí nghiệm ít tốn công nhất

1. **Rule-based baseline trước**
   - Không cần training.
   - Chạy nhanh local.
   - Đủ tạo một baseline yếu nhưng giải thích được.

2. **PhoBERT full unweighted**
   - Dùng script training hiện có.
   - Cho comparison trực tiếp với weighted proposed method.
   - Nên chạy 5 epochs hoặc cùng config với full weighted.

3. **BiLSTM baseline nếu đủ thời gian**
   - Cần thêm model/training script.
   - Nếu không đủ thời gian, chọn BiLSTM token classifier trước, chưa cần CRF.

4. **Giữ PhoBERT weighted full làm proposed method**
   - Kết quả đã có.
   - Đây là dòng chính trong bảng kết quả.

---

## Ràng buộc báo cáo

- Tất cả dataset settings đều derived from UIT-ViOCD.
- Không dùng Shopee.
- Không dùng rating mapping.
- Full AI-assisted labels không phải human gold-standard.
- Không trình bày Entity-F1 0.8455 như official benchmark của UIT-ViOCD gốc.

