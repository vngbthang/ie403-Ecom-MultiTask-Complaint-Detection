# Error Analysis

## 1. Overview

Classification trên Shopee đạt kết quả cao (LinearSVM: Accuracy 0.9431, F1-Macro 0.9428) nhờ TF-IDF n-grams (1,2) với feature 10,000 chiều. Trong khi đó, NER khó hơn nhiều vì cần xác định ranh giới chính xác của cụm khiếu nại trong bình luận/review TMĐT tiếng Việt.

PhoBERT Linear NER và PhoBERT + CRF NER single-task đạt Entity-F1 chỉ ~0.02, gần như không có khả năng trích xuất span. Multi-task PhoBERT + CRF cải thiện rõ rệt: Entity-F1 đạt ~0.33, Token-F1 đạt ~0.66. Tuy nhiên recall vẫn còn thấp, cho thấy model bỏ sót nhiều entity.

---

## 2. Classification Error Analysis

### 2.1 Overall Error Distribution

| Metric | Value |
|---|---|
| Total Samples | 1564 |
| Correct | 1475 |
| False Positive (true=0, pred=1) | 43 |
| False Negative (true=1, pred=0) | 46 |
| Accuracy | 0.9431 |

### 2.2 False Positive Examples (Non-Complaint predicted as Complaint)

- **FP** (conf=0.999): "Giao hàng nhanh. Nhưng bên vận chuyển ném vứt làm bục vỡ chẩy sữa hỏng 3 bịch, sữa bị chẩy ra lên men hỏng gây mùi khó c"
- **FP** (conf=0.996): "Sữa đỗ bể chảy tùm lum k giải quyết 😡😡😡😡"
- **FP** (conf=0.991): "Sản phẩm nhận không như mong đợi, mỏng, nón không được cứng cáp, đội mất form không đẹp 👎👎"
- **FP** (conf=0.978): "Bao bì:dep Mẹo:khong co Lợi ích:sach gau  Mình hay mua túi cho tiết kiệm nhưng lần này mình mua chai lớn. Tưởng được tặn"
- **FP** (conf=0.949): "chưa dùng thử, do tui không đọc kĩ cách mua nên không có quà đi kèm:("

**Phân tích FP:**
- Bình luận không yêu cầu nhưng chứa từ tiêu cực nhẹ hoặc mô tả vấn đề nhỏ.
- Một số review ghi nhận đăng ký sản phẩm nhưng không có complaint thực sự.
- Rating-label noise: nhãn được gán từ rating 4-5★ nên có thể có nhiều khi rating thấp nhưng không phải complaint.

### 2.3 False Negative Examples (Complaint predicted as Non-Complaint)

- **FN** (conf=0.999): "Độ sáng:ok Làm sạch:sạch, mới dùng nên chưa biêt Dịu nhẹ:dễ chịu  Luôn ủng hộ hàng việt nam. Nên mình cũng mong là sản p"
- **FN** (conf=0.999): "Hình ảnh chỉ mang tính chất nhận xu thôi ship cũng nhánh chóng. Hi vọng dùng tốt lần sau sẽ mua lại"
- **FN** (conf=0.999): "Dùng thích mùi thơm mua lại nhiều lần. Rồi sẽ ủng hộ thêm nhiều lần, khôgng thấy quà tặng"
- **FN** (conf=0.990): "Giao hàng nhanh đóng gói chắc chắn sp tốt sẽ ủng hộ thêm nữa hikdkc giao tới bị móp 3 hộp gói hàng cần cẩn thận hơn"
- **FN** (conf=0.990): "Mẹo:minh chua dung Kinh nghiệm sử dụng:minh su dung lan dau tien Hương thơm:dung lan dau nen chua biet  Mình dùng lần đầ"

**Phân tích FN:**
- Complaint ngầm: không có từ khóa tiêu cực rõ ràng, chỉ mô tả trải nghiệm.
- Mixed sentiment: câu vừa khen vừa chê, model lấy trung bình thành non-complaint.
- Informal Vietnamese: teencode, lỗi chính tả, từ viết tắt làm giảm confidence.

### 2.4 Root Causes

1. **Rating-label noise**: Nhãn Shopee được suy ra từ rating (1-2★ = complaint, 4-5★ = non-complaint). Rating thấp có thể do nhiều lý do khác ngoài complaint (ví dụ: giao chậm, đóng gói kém, không ưng ý).
2. **Mixed sentiment**: Người dùng thường vừa khen vừa chê trong cùng một bình luận. TF-IDF có thể bị đánh giá bởi phần tích cực.
3. **Implicit complaint**: Complaint không nói rõ, chỉ nghi ngờ hoặc đề cập gián tiếp.

---

## 3. NER Error Analysis

### 3.1 NER Metrics Summary

| Model | Entity Precision | Entity Recall | Entity F1 | Token F1 |
|-------|-----------------|---------------|-----------|----------|
| PhoBERT Linear NER (single-task) | 0.0166 | 0.0233 | 0.0194 | 0.4231 |
| PhoBERT + CRF NER (single-task) | 0.0134 | 0.0233 | 0.0170 | 0.4172 |
| Multi-task PhoBERT + CRF (alpha=1.0) | 0.2841 | 0.3876 | 0.3279 | 0.6445 |
| Multi-task PhoBERT + CRF (alpha=2.0) | 0.3003 | 0.3527 | 0.3244 | 0.6627 |

> PhoBERT Linear NER và PhoBERT + CRF NER single-task chỉ đạt Entity-F1 ~0.02. Multi-task PhoBERT + CRF đạt Entity-F1 ~0.33 nhưng vẫn còn thấp.

### 3.2 Token-level Breakdown (Multi-task alpha=1.0, epoch 3)

| Label | Precision | Recall | F1 | Support |
|-------|-----------|--------|-----|---------|
| O | 0.8887 | 0.8878 | 0.8882 | 2,833 |
| B-COMP | 0.7723 | 0.3023 | 0.4345 | 258 |
| I-COMP | 0.5552 | 0.6787 | 0.6108 | 719 |

**Nhận xét:**
- **B-COMP recall thấp thấp (0.3023)**: Model rất khó xác định đúng token bắt đầu của một entity. Đây là nguyên nhân chính dẫn đến Entity-F1 thấp.
- **I-COMP precision thấp (0.5552)**: Model có xu hướng đặt nhãn I-COMP nhưng không đúng vị trí, dẫn đến nhiều false positive ở mức I-COMP.
- **O precision/recall cao (~0.89)**: Model phân biệt tốt token không phải entity.

### 3.3 Error Types (từ predictions.csv)

**PhoBERT Linear NER** (total=100):
- Boundary errors: 89
- Missed entities: 3
- Spurious entities: 1

**PhoBERT + CRF NER** (total=100):
- Boundary errors: 5
- Missed entities: 94
- Spurious entities: 0

**Boundary Error Examples:**
- **PhoBERT Linear NER** gold=[(0, 2, 'COMP')], pred=[(1, 4, 'COMP')]
- **PhoBERT Linear NER** gold=[(13, 17, 'COMP'), (56, 60, 'COMP')], pred=[(14, 18, 'COMP'), (30, 34, 'COMP'), (44, 47, 'COMP'), (57, 62, 'COMP'), (64, 68, 'COMP')]
- **PhoBERT Linear NER** gold=[(11, 12, 'COMP')], pred=[(10, 10, 'COMP'), (12, 13, 'COMP')]
- **PhoBERT + CRF NER** gold=[(6, 7, 'COMP'), (14, 14, 'COMP'), (48, 49, 'COMP'), (50, 55, 'COMP'), (57, 59, 'COMP')], pred=[(7, 13, 'COMP')]
- **PhoBERT + CRF NER** gold=[(8, 12, 'COMP'), (19, 22, 'COMP'), (46, 50, 'COMP')], pred=[(48, 51, 'COMP')]
- **PhoBERT + CRF NER** gold=[(0, 3, 'COMP'), (22, 26, 'COMP'), (49, 51, 'COMP')], pred=[(1, 8, 'COMP')]

### 3.4 Key NER Error Patterns

1. **B-COMP Boundary Error**: Model bỏ sót token bắt đầu entity. Ví dụ: gold=`B-COMP I-COMP I-COMP`, pred=`I-COMP B-COMP I-COMP`. Đây là lỗi phổ biến nhất — recall của B-COMP chỉ 0.30.

2. **Missed Entity**: Model không trích xuất được entity nào từ câu có complaint. Nguyên nhân: dataset nhỏ (400 train), complaint span ngắn và không có pattern cố định.

3. **Spurious Entity**: Model trích xuất entity từ câu không có complaint. Thường là các cụm từ mô tả vấn đề nhẹ hoặc từ ngữ tích cực bị hiểu nhầm.

4. **Informal Vietnamese**: Bình luận/review TMĐT tiếng Việt có nhiều teencode, lỗi chính tả, viết tắt. PhoBERT được pre-trained trên tiếng Việt chuẩn nên gặp khó khăn với các biến thể không chuẩn.
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

3. **Complaint span không có ranh giới rõ ràng**: Trong bình luận/review TMĐT, complaint span thường ngắn, phụ thuộc ngữ cảnh, và không có từ khóa cố định. Boundary annotation rất khó đảm bảo nhất quán.

4. **Informal Vietnamese**: Teencode, lỗi chính tả, viết tắt phổ biến trong bình luận Shopee. PhoBERT pre-trained trên tiếng Việt chuẩn không xử lý tốt các biến thể này.

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
