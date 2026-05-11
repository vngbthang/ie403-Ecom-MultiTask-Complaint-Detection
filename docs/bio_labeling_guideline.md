# Hướng dẫn gán nhãn BIO cho Task Span Extraction

Trong bài toán trích xuất cụm từ khiếu nại (Complaint Span Extraction), chúng ta sử dụng hệ nhãn **BIO** (Begin - Inside - Outside) để đánh dấu chính xác vị trí và độ dài của cụm từ thể hiện sự phàn nàn/khiếu nại từ bình luận của khách hàng.

## 1. Định nghĩa hệ nhãn
- **B-COMP (Begin - Complaint)**: Từ **ĐẦU TIÊN** của một cụm từ khiếu nại.
- **I-COMP (Inside - Complaint)**: Các từ **TIẾP THEO** nằm bên trong cụm từ khiếu nại đó.
- **O (Outside)**: Các từ **KHÔNG** thuộc bất kỳ cụm khiếu nại nào (những từ bình thường).

## 2. Nguyên tắc gán nhãn
- Cụm từ khiếu nại cần bao gồm cả các từ chỉ mức độ (ví dụ: *rất, quá, cực kỳ*) nếu chúng bổ nghĩa trực tiếp cho trạng thái lỗi/khiếu nại.
- Các từ phủ định (ví dụ: *không, chả, chưa*) đi kèm với tính từ/động từ kỳ vọng cũng phải được gộp vào cụm khiếu nại.
- Chỉ gán nhãn phần cốt lõi mang ý nghĩa phàn nàn, tránh gán dư thừa các từ nối không cần thiết (ví dụ: *nhưng, mà*).

## 3. Ví dụ minh họa chi tiết

### Ví dụ 1: Tính từ chỉ mức độ kết hợp với lỗi
**Bình luận:** "Giao hàng quá chậm, sản phẩm bị móp méo"
- Việc khách hàng phàn nàn là tốc độ giao hàng và tình trạng sản phẩm. Từ "quá" nhấn mạnh mức độ chậm nên cần đưa vào cụm.

| Token | Nhãn |
|---|---|
| Giao | O |
| hàng | O |
| quá | **B-COMP** |
| chậm | **I-COMP** |
| , | O |
| sản | O |
| phẩm | O |
| bị | **B-COMP** |
| móp | **I-COMP** |
| méo | **I-COMP** |

### Ví dụ 2: Từ phủ định đi kèm từ kỳ vọng
**Bình luận:** "Giày đẹp nhưng mang không vừa chân"
- Từ "nhưng" là từ nối, không mang nghĩa khiếu nại -> nhãn O.
- Cụm phàn nàn chính là việc mang không vừa, cần bao gồm cả từ phủ định "không".

| Token | Nhãn |
|---|---|
| Giày | O |
| đẹp | O |
| nhưng | O |
| mang | O |
| không | **B-COMP** |
| vừa | **I-COMP** |
| chân | **I-COMP** |

### Ví dụ 3: Lỗi do chất lượng hoặc dịch vụ rõ ràng
**Bình luận:** "Shop phục vụ rất tệ, nhắn tin chả ai thèm rep"

| Token | Nhãn |
|---|---|
| Shop | O |
| phục | O |
| vụ | O |
| rất | **B-COMP** |
| tệ | **I-COMP** |
| , | O |
| nhắn | O |
| tin | O |
| chả | **B-COMP** |
| ai | **I-COMP** |
| thèm | **I-COMP** |
| rep | **I-COMP** |

## 4. Các trường hợp cần lưu ý (Edge Cases)
- **Cụm từ đứt gãy:** Nếu bình luận là "áo thì rách, quần thì tuột chỉ", gán "rách" (B-COMP) và "tuột chỉ" (B-COMP, I-COMP). Không gán các từ "thì".
- **Lỗi chính tả:** Giữ nguyên lỗi chính tả của người dùng khi gán nhãn, không tự ý sửa đổi token.
