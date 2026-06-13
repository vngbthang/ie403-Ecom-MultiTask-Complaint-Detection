# Nhận diện và rút trích vùng khiếu nại trong đánh giá thương mại điện tử tiếng Việt bằng PhoBERT và quy trình gán nhãn hỗ trợ bởi AI

## Mục tiêu chỉnh sửa báo cáo

Báo cáo mới cần chuyển trọng tâm từ bài toán phân loại khiếu nại ở mức toàn review sang bài toán rút trích vùng khiếu nại trong nội dung review. Dataset chính chỉ sử dụng UIT-ViOCD. Shopee Reviews và rating mapping không còn là pipeline chính.

Câu chuyện chính:

UIT-ViOCD classification-only -> AI-assisted complaint span annotation -> validation, repair, overlap resolving -> BIO conversion -> PhoBERT NER với class-weighted loss -> đánh giá trên full AI-assisted complaint span dataset.

---

## Chương 1. Giới thiệu

### Mục tiêu chương

Giới thiệu bài toán, động lực nghiên cứu và lý do cần mở rộng từ phân loại complaint review sang rút trích vùng khiếu nại cụ thể trong review.

### Các mục con nên có

1. Bối cảnh thương mại điện tử và đánh giá người dùng tiếng Việt
2. Bài toán phát hiện khiếu nại trong review
3. Hạn chế của nhãn review-level
4. Mục tiêu nghiên cứu mới
5. Đóng góp chính của đồ án
6. Cấu trúc báo cáo

### Nội dung chính cần viết

- Review thương mại điện tử thường chứa cả phần khen, phần mô tả trung tính và phần phàn nàn.
- Nhãn review-level Complaint / Non-Complaint chỉ cho biết toàn review có khiếu nại hay không, nhưng không chỉ ra cụm từ nào thể hiện vấn đề.
- Rút trích complaint span giúp phân tích cụ thể hơn: lỗi giao hàng, sản phẩm sai mô tả, chất lượng kém, ứng dụng bị lỗi, dịch vụ không phản hồi.
- Đề xuất quy trình xây dựng dữ liệu span từ UIT-ViOCD bằng AI-assisted annotation, sau đó huấn luyện PhoBERT NER.

### Số liệu/kết quả cần đưa vào

- UIT-ViOCD processed:
  - train: 4387 reviews, Complaint 2292, Non-Complaint 2095
  - val: 548 reviews, Complaint 283, Non-Complaint 265
  - test: 549 reviews, Complaint 279, Non-Complaint 270
- Tổng complaint candidates đã annotate span: 2854.

### Hình/bảng nên có

- Hình pipeline tổng quan từ raw UIT-ViOCD đến NER dataset.
- Bảng phân bố nhãn Complaint / Non-Complaint theo train / val / test.
- Ví dụ một review có nhãn Complaint nhưng chỉ một phần nhỏ là complaint span.

---

## Chương 2. Cơ sở lý thuyết và nghiên cứu liên quan

### Mục tiêu chương

Trình bày nền tảng về complaint detection, sequence labeling, BIO tagging, PhoBERT và các hướng annotation hỗ trợ bởi AI.

### Các mục con nên có

1. Complaint detection trong văn bản đánh giá
2. Named Entity Recognition và sequence labeling
3. BIO tagging cho rút trích span
4. Mô hình Transformer và PhoBERT cho tiếng Việt
5. Class imbalance trong NER
6. AI-assisted annotation và kiểm soát chất lượng nhãn

### Nội dung chính cần viết

- Complaint classification xử lý toàn văn bản, trong khi NER xử lý từng token.
- BIO scheme:
  - `B-COMP`: token bắt đầu vùng khiếu nại
  - `I-COMP`: token tiếp theo trong vùng khiếu nại
  - `O`: ngoài vùng khiếu nại
- PhoBERT phù hợp cho tiếng Việt vì được tiền huấn luyện trên corpus tiếng Việt lớn.
- Class imbalance trong NER thường làm model thiên về nhãn `O`; do đó dùng class-weighted CrossEntropyLoss.
- AI-assisted annotation giúp mở rộng nhãn nhanh hơn nhưng cần validation, repair và review.

### Số liệu/kết quả cần đưa vào

- Full span dataset:
  - total records: 2854
  - total tokens: 109783
  - O: 27286
  - B-COMP: 10195
  - I-COMP: 72302
  - COMP token ratio: 75.15%

### Hình/bảng nên có

- Bảng mô tả BIO labels.
- Hình minh họa tokenization và BIO tagging từ một review.
- Bảng so sánh review-level classification và span-level extraction.

---

## Chương 3. Phân tích dữ liệu UIT-ViOCD và hạn chế của nhãn review-level

### Mục tiêu chương

Phân tích dataset UIT-ViOCD, schema dữ liệu, phân bố nhãn/domain và lý do cần bổ sung span labels.

### Các mục con nên có

1. Giới thiệu UIT-ViOCD
2. Schema raw và processed
3. Phân bố nhãn Complaint / Non-Complaint
4. Phân bố domain
5. Hạn chế của nhãn review-level
6. Định nghĩa complaint span

### Nội dung chính cần viết

- Raw UIT-ViOCD gồm các cột: `review`, `review_tokenize`, `label`, `domain`.
- Processed schema mới:
  - `id`
  - `review`
  - `review_tokenize`
  - `complaint_label`
  - `domain`
  - `split`
- Chỉ các review có `complaint_label = 1` được đưa vào annotation span.
- Complaint span được định nghĩa là cụm từ ngắn nhất nhưng đủ nghĩa thể hiện nội dung khiếu nại/phàn nàn.

### Số liệu/kết quả cần đưa vào

- Complaint candidates:
  - train: 2292
  - val: 283
  - test: 279
  - total: 2854
- Full complaint span dataset:
  - records with spans: 2773
  - records without spans: 81
  - total spans: 10195
  - average spans per record: 3.5722
- Domain distribution:
  - app: 1510
  - cosmetic: 475
  - fashion: 732
  - mobile: 137

### Hình/bảng nên có

- Bảng schema raw và processed UIT-ViOCD.
- Bảng complaint candidates theo split.
- Bảng domain distribution.
- Ví dụ review có nhiều complaint spans.

---

## Chương 4. Phương pháp đề xuất

### Mục tiêu chương

Mô tả toàn bộ pipeline đề xuất: chuẩn hóa dữ liệu, gán nhãn span bằng AI, kiểm soát chất lượng annotation, chuyển BIO và huấn luyện PhoBERT NER.

### Các mục con nên có

1. Tổng quan pipeline đề xuất
2. Chuẩn hóa UIT-ViOCD
3. AI-assisted span annotation
4. Quy tắc gán nhãn complaint span
5. Offset validation
6. Offset repair
7. Overlap resolving
8. BIO conversion
9. PhoBERT NER architecture
10. Class-weighted CrossEntropyLoss
11. Quy trình kiểm soát chất lượng annotation

### Nội dung chính cần viết

#### 4.1. AI-assisted span annotation

- Dùng prompt/guideline để AI gán nhãn `COMP` cho complaint spans.
- Output mỗi record gồm:
  - `id`
  - `text`
  - `spans`
  - `reason`
- Span phải là substring nguyên văn trong text.
- `start/end` dùng Python slicing: `text[start:end] == span_text`.

#### 4.2. Offset validation

Validator kiểm tra:

- JSONL hợp lệ
- đủ trường `id`, `text`, `spans`, `reason`
- id tồn tại trong candidates
- text khớp source text
- span offsets hợp lệ
- `span["text"] == text[start:end]`
- label chỉ là `COMP`
- không duplicate id
- không missing id

#### 4.3. Offset repair

- Nếu `start/end` sai nhưng `span.text` là substring đúng trong text, tự tìm lại exact substring.
- Nếu có nhiều vị trí trùng, chọn vị trí gần offset cũ nhất.
- Không tự sửa nội dung span text bằng đoán nghĩa.

#### 4.4. Overlap resolving

- Với các spans chồng lấn ở char offset hoặc cùng chạm một whitespace token, merge thành một span `COMP`.
- Span mới:
  - `start = min(start_i, start_j)`
  - `end = max(end_i, end_j)`
  - `text = source_text[start:end]`
  - `label = COMP`
- Sau resolve, conversion warnings còn 0.

#### 4.5. BIO conversion

- Tokenization dùng whitespace để giữ offset đơn giản và reproducible.
- Token overlap với span đầu tiên được gán `B-COMP`.
- Các token tiếp theo trong cùng span được gán `I-COMP`.
- Token ngoài span là `O`.

#### 4.6. PhoBERT NER

- Encoder: `vinai/phobert-base-v2`
- Token classifier: linear head với 3 labels `O`, `B-COMP`, `I-COMP`
- Evaluation decode đã dùng mask `labels != -100` để tránh lệch subword/special token.

#### 4.7. Class-weighted CrossEntropyLoss

- Dùng để giảm bias về nhãn `O`.
- Công thức balanced:

```text
weight_c = total_labeled_tokens / (num_classes * count_c)
```

- Loss:

```text
CrossEntropyLoss(weight=class_weights, ignore_index=-100)
```

### Số liệu/kết quả cần đưa vào

- Pilot 100:
  - records: 100
  - tokens: 3399
  - COMP tokens: 836
  - records with spans: 95
  - records without spans: 5
- Full annotation:
  - total records: 2854
  - full batches remaining: 2554
  - validation passed batches: 13
  - overlap warnings before: 334
  - overlap warnings after: 0

### Hình/bảng nên có

- Hình pipeline chi tiết:
  - raw UIT-ViOCD
  - processed CSV
  - annotation candidates
  - AI annotation
  - validation/repair/overlap resolving
  - BIO
  - PhoBERT NER
- Bảng các bước quality control và mục đích.
- Bảng label mapping `O`, `B-COMP`, `I-COMP`.
- Pseudocode hoặc flowchart cho overlap resolving.

---

## Chương 5. Thực nghiệm và đánh giá

### Mục tiêu chương

Trình bày thiết lập thực nghiệm, dữ liệu train/val/test, metric đánh giá và kết quả so sánh giữa các mốc: pilot100 unweighted, pilot100 weighted, full complaint weighted.

### Các mục con nên có

1. Thiết lập thực nghiệm
2. Dataset splits
3. Metrics đánh giá
4. Kết quả pilot100
5. Kết quả full complaint span dataset
6. Phân tích kết quả
7. Lỗi thường gặp và nhận xét

### Nội dung chính cần viết

- Metrics:
  - Entity Precision
  - Entity Recall
  - Entity F1
  - Token F1 macro
  - Avg loss
- Pilot100 unweighted bị bias về `O`, Entity F1 = 0.
- Weighted loss giúp model bắt đầu dự đoán COMP labels, Entity F1 tăng lên 0.1370.
- Mở rộng annotation lên toàn bộ complaint reviews giúp cải thiện mạnh, Entity F1 đạt 0.8455.

### Bảng kết quả cần đưa vào

| Thí nghiệm | Dataset | Loss | Epoch | Entity P | Entity R | Entity F1 | Token F1 macro | Avg loss |
|---|---|---|---:|---:|---:|---:|---:|---:|
| Pilot100 Unweighted PhoBERT NER | UIT-ViOCD pilot 100 | CrossEntropy | 3 | 0.0000 | 0.0000 | 0.0000 | 0.3002 | 0.6437 |
| Pilot100 Weighted PhoBERT NER | UIT-ViOCD pilot 100 | Weighted CrossEntropy | 7 | 0.0893 | 0.2941 | 0.1370 | 0.5845 | 0.3660 |
| Full Complaint Weighted PhoBERT NER | UIT-ViOCD full AI-assisted complaint span dataset | Weighted CrossEntropy | 5 | 0.7937 | 0.9045 | 0.8455 | 0.8620 | 0.2486 |

### Số liệu dataset split cần đưa vào

Full complaint NER split:

- Train: 2280 records, 87726 tokens, 65946 COMP tokens
- Val: 283 records, 10569 tokens, 8015 COMP tokens
- Test: 291 records, 11488 tokens, 8536 COMP tokens

### Hình/bảng nên có

- Bảng kết quả NER chính.
- Bảng thống kê split train/val/test.
- Biểu đồ Entity F1 theo thí nghiệm.
- Biểu đồ Token F1 macro theo thí nghiệm.
- Một số ví dụ prediction đúng/sai nếu có predictions CSV.

---

## Chương 6. Kết luận và hướng phát triển

### Mục tiêu chương

Tổng kết kết quả đạt được, đóng góp của pipeline, các hạn chế và hướng phát triển tiếp theo.

### Các mục con nên có

1. Kết luận chính
2. Đóng góp của đồ án
3. Hạn chế
4. Hướng phát triển

### Nội dung chính cần viết

- Đồ án đã chuyển từ classification-only sang span extraction trên UIT-ViOCD.
- Đã xây dựng pipeline annotation hỗ trợ bởi AI có kiểm soát:
  - validation
  - offset repair
  - overlap resolving
  - BIO conversion
- Đã huấn luyện và đánh giá PhoBERT NER với weighted loss.
- Kết quả tốt nhất trên full AI-assisted span dataset đạt Entity F1 = 0.8455.

### Limitations bắt buộc phải ghi rõ

- Full span labels are AI-assisted annotations, not fully human gold-standard labels.
- Automatic validation, offset repair, overlap resolving and partial manual review were used to improve consistency.
- Results should be interpreted as evaluation on the constructed AI-assisted span dataset.
- Cần human review nhiều hơn nếu muốn công bố một benchmark chuẩn hơn.

### Hướng phát triển

- Human review toàn bộ hoặc review theo active learning để nâng chất lượng gold labels.
- Thử CRF head hoặc constrained decoding để cải thiện BIO boundary.
- So sánh với các mô hình tiếng Việt khác.
- Mở rộng sang multi-task learning:
  - Classification: Complaint / Non-Complaint
  - NER: `O`, `B-COMP`, `I-COMP`
- Error analysis theo domain: app, cosmetic, fashion, mobile.

### Hình/bảng nên có

- Bảng tổng kết đóng góp.
- Bảng limitations và mitigation.
- Sơ đồ hướng phát triển multi-task.

---

## Danh sách bảng/hình nên đưa vào báo cáo

### Bảng

1. Phân bố nhãn UIT-ViOCD processed theo train/val/test.
2. Schema raw và processed UIT-ViOCD.
3. Domain distribution của full complaint span dataset.
4. BIO label mapping.
5. Thống kê annotation pipeline: pilot100, batch200, remaining full batches, full dataset.
6. Split train/val/test của full complaint NER.
7. Bảng kết quả NER experiments.
8. Bảng limitations.

### Hình

1. Pipeline tổng quan của đồ án mới.
2. Ví dụ review và complaint spans.
3. Flow validation/repair/overlap resolving.
4. BIO conversion minh họa.
5. Kiến trúc PhoBERT token classification.
6. Biểu đồ Entity F1 qua các thí nghiệm.
7. Biểu đồ Token F1 macro qua các thí nghiệm.

---

## Các file số liệu nên trích dẫn khi viết báo cáo

- `data/processed/uit_viocd_full_complaint_summary.json`
- `data/processed/uit_viocd_full_complaint_ner_split_summary.json`
- `data/processed/uit_viocd_pilot_100_summary.json`
- `outputs/metrics/summary/ner_experiment_summary.csv`
- `outputs/metrics/summary/ner_experiment_summary.md`
- `outputs/metrics/summary/report_key_numbers.md`
