# Hướng dẫn Gán nhãn BIO: Trích xuất Cụm từ Khiếu nại (Complaint Span Extraction)

## 1. Mục tiêu và Hệ nhãn
Nhiệm vụ của team là tìm và trích xuất các cụm từ thể hiện sự khiếu nại, chê bai, hoặc phản ánh lỗi sản phẩm/dịch vụ từ bình luận e-commerce. 
Chúng ta sử dụng quy tắc gán nhãn **BIO** cho từng từ đơn (token):

- **B-COMP (Begin - Complaint):** Từ BẮT ĐẦU của một cụm từ khiếu nại.
- **I-COMP (Inside - Complaint):** Các từ BÊN TRONG (tiếp nối ngay sau B-COMP) của cụm khiếu nại.
- **O (Outside):** Các từ nằm NGOÀI cụm khiếu nại, không mang ý nghĩa chê bai.

## 2. Nguyên tắc Gán nhãn Cốt lõi
1. **Bao trọn ý nghĩa lõi:** Gán sao cho khi rút trích đoạn text ra, người đọc hiểu chính xác lỗi là gì mà không cần đọc cả câu.
2. **Gộp chung Trạng từ chỉ mức độ / Từ phủ định:** Các từ như "rất", "quá", "không", "chẳng" **PHẢI** được gộp vào cụm khiếu nại (gán B/I-COMP) vì chúng làm rõ bản chất và sắc thái của lỗi.
3. **Loại trừ Liên từ / Từ nối:** Các từ như "nhưng", "tuy nhiên", "mà" KHÔNG thuộc về cụm khiếu nại (gán nhãn O).

## 3. Các Ví dụ Dễ Gây Tranh Cãi (Cần lưu ý kỹ)

### Ví dụ 1: Xử lý Trạng từ chỉ mức độ ("quá", "rất", "cực kỳ")
**Bình luận:** "Shop giao hàng quá chậm"
**Quy tắc:** Không chỉ gán chữ "chậm" hay "quá chậm". Phải gán toàn bộ sự việc "giao hàng quá chậm" để xác định rõ đối tượng bị khiếu nại.

| Từ | Nhãn |
|---|---|
| Shop | O |
| giao | B-COMP |
| hàng | I-COMP |
| quá | I-COMP |
| chậm | I-COMP |

### Ví dụ 2: Xử lý Từ phủ định ("không", "chưa")
**Bình luận:** "Sản phẩm này không giống hình quảng cáo"
**Quy tắc:** "không giống hình" là cốt lõi của sự khiếu nại. Cụm "Sản phẩm này" chỉ là chủ ngữ chung chung, lược bỏ đi vẫn hiểu được lỗi. Từ "không" đóng vai trò bắt đầu cụm khiếu nại.

| Từ | Nhãn |
|---|---|
| Sản | O |
| phẩm | O |
| này | O |
| không | B-COMP |
| giống | I-COMP |
| hình | I-COMP |
| quảng | I-COMP |
| cáo | I-COMP |

### Ví dụ 3: Xử lý Liên từ chuyển ý ("nhưng")
**Bình luận:** "Giày êm nhưng form rất nhỏ"
**Quy tắc:** "Giày êm" là lời khen (O). Chữ "nhưng" là từ nối (O). Phần khiếu nại bắt đầu từ "form rất nhỏ", lưu ý phải giữ lại trạng từ "rất".

| Từ | Nhãn |
|---|---|
| Giày | O |
| êm | O |
| nhưng | O |
| form | B-COMP |
| rất | I-COMP |
| nhỏ | I-COMP |
