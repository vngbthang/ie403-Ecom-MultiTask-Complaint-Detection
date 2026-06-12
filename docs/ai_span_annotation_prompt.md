# AI-assisted Complaint Span Annotation Prompt

## Mục tiêu annotation

Gán nhãn các cụm từ thể hiện nội dung khiếu nại/phàn nàn trong review tiếng Việt từ UIT-ViOCD. Kết quả annotation sẽ được chuyển sang BIO labels để huấn luyện bài toán complaint span extraction với nhãn `O`, `B-COMP`, `I-COMP`.

## Định nghĩa complaint span

Complaint span là cụm từ ngắn nhất nhưng đủ nghĩa trong review thể hiện nội dung khiếu nại/phàn nàn của người dùng.

Ví dụ: trong câu `áo đẹp nhưng giao hàng quá chậm`, complaint span là `giao hàng quá chậm`, không phải toàn bộ câu.

## Nhãn cần gán

Hiện tại chỉ có một nhãn span:

- `COMP`: cụm từ thể hiện vấn đề, lỗi, sự không hài lòng, phàn nàn, yêu cầu khắc phục, hoặc trải nghiệm tiêu cực của người dùng.

## Quy tắc chọn span

1. Chỉ chọn cụm thể hiện vấn đề/khiếu nại.
2. Không chọn toàn câu nếu có thể chọn cụm ngắn hơn.
3. Không chọn phần khen, phần trung tính, hoặc thông tin nền không trực tiếp là khiếu nại.
4. Không chọn emoji riêng lẻ làm complaint span.
5. Nếu review có nhiều lỗi/khiếu nại, trả về nhiều span.
6. Nếu complaint là gián tiếp hoặc nói bóng gió, chọn cụm thể hiện ý không hài lòng rõ nhất.
7. Nếu không tìm được span rõ ràng, trả về `spans = []` và ghi lý do trong `reason`.
8. Span phải là substring xuất hiện nguyên văn trong `text`.
9. `start` và `end` là character offset theo Python slicing: `text[start:end] == span_text`.
10. Giữ nguyên chính tả, teencode, viết tắt và dấu câu như trong text gốc.

## Quy tắc rút gọn span

1. Ưu tiên chọn cụm nguyên nhân/vấn đề chính, không chọn cả câu giải thích dài.
2. Span lý tưởng thường từ 2 đến 8 token.
3. Chỉ chọn span dài hơn 12 token nếu không thể rút ngắn mà vẫn đủ nghĩa.
4. Bỏ các cụm mở đầu không cần thiết như `tôi thấy`, `mình thấy`, `em tải xong vào thì`, `tại sao các ông lại`, nếu phần còn lại vẫn thể hiện rõ complaint.
5. Với lỗi lặp lại, chọn cụm lỗi trung tâm như `tải xong lỗi`, `lại lỗi tiếp`, thay vì chọn toàn bộ quá trình.
6. Với câu hỏi phàn nàn, chọn phần vấn đề chính, ví dụ `không thấy thống kê dịch bệnh liên quan đến nước Anh`, không cần chọn `admin ơi. sao... vậy`.
7. Với góp ý tính năng, chỉ gán `COMP` nếu có bất cập rõ; nếu chỉ là đề xuất trung tính thì trả về `spans = []`.

## Ví dụ đúng/sai

### Ví dụ 1

Input:

```json
{"id":"ex_001","text":"áo đẹp nhưng giao hàng quá chậm","label":[],"meta":{"source":"UIT-ViOCD","split":"train","domain":"fashion","cls_label":1}}
```

Output đúng:

```json
{
  "id": "ex_001",
  "text": "áo đẹp nhưng giao hàng quá chậm",
  "spans": [
    {"start": 13, "end": 31, "text": "giao hàng quá chậm", "label": "COMP"}
  ],
  "reason": "Cụm này nêu trực tiếp vấn đề giao hàng chậm; phần 'áo đẹp' là khen nên không chọn."
}
```

Sai:

- Chọn `áo đẹp nhưng giao hàng quá chậm`: quá dài, chứa phần khen.
- Chọn `chậm`: quá ngắn, thiếu ngữ cảnh vấn đề.

### Ví dụ 2

Input:

```json
{"id":"ex_002","text":"mua 2 chai mà giao thiếu 1 chai, nhắn tin không ai trả lời","label":[],"meta":{"source":"UIT-ViOCD","split":"train","domain":"cosmetic","cls_label":1}}
```

Output đúng:

```json
{
  "id": "ex_002",
  "text": "mua 2 chai mà giao thiếu 1 chai, nhắn tin không ai trả lời",
  "spans": [
    {"start": 15, "end": 31, "text": "giao thiếu 1 chai", "label": "COMP"},
    {"start": 33, "end": 58, "text": "nhắn tin không ai trả lời", "label": "COMP"}
  ],
  "reason": "Review có hai khiếu nại riêng: giao thiếu hàng và không được phản hồi."
}
```

Sai:

- Chọn toàn câu: quá dài.
- Chỉ chọn một span: bỏ sót khiếu nại còn lại.

### Ví dụ 3

Input:

```json
{"id":"ex_003","text":"sản phẩm cũng tạm, mua một lần cho biết","label":[],"meta":{"source":"UIT-ViOCD","split":"train","domain":"fashion","cls_label":1}}
```

Output đúng:

```json
{
  "id": "ex_003",
  "text": "sản phẩm cũng tạm, mua một lần cho biết",
  "spans": [
    {"start": 19, "end": 41, "text": "mua một lần cho biết", "label": "COMP"}
  ],
  "reason": "Cụm này thể hiện ý không hài lòng gián tiếp, hàm ý sẽ không mua lại."
}
```

### Ví dụ 4

Input:

```json
{"id":"ex_004","text":"mình chưa dùng nên chưa biết chất lượng thế nào","label":[],"meta":{"source":"UIT-ViOCD","split":"train","domain":"cosmetic","cls_label":1}}
```

Output đúng:

```json
{
  "id": "ex_004",
  "text": "mình chưa dùng nên chưa biết chất lượng thế nào",
  "spans": [],
  "reason": "Không có cụm khiếu nại rõ ràng; người dùng chỉ nói chưa sử dụng."
}
```

### Ví dụ 5: Rút gọn lỗi lặp lại

Input:

```json
{"id":"ex_005","text":"anh chị xem khắc phục lại lỗi hộ em với ạ, em tải xong vào thì bảo tải dữ liệu, vừa hiện tải xong lỗi, thử lại thì lại hiện tải xong lại lỗi tiếp","label":[],"meta":{"source":"UIT-ViOCD","split":"train","domain":"app","cls_label":1}}
```

Output tốt:

```json
{
  "id": "ex_005",
  "text": "anh chị xem khắc phục lại lỗi hộ em với ạ, em tải xong vào thì bảo tải dữ liệu, vừa hiện tải xong lỗi, thử lại thì lại hiện tải xong lại lỗi tiếp",
  "spans": [
    {"start": 92, "end": 104, "text": "tải xong lỗi", "label": "COMP"},
    {"start": 139, "end": 151, "text": "lại lỗi tiếp", "label": "COMP"}
  ],
  "reason": "Review mô tả lỗi lặp lại; chọn các cụm lỗi trung tâm thay vì toàn bộ quá trình tải."
}
```

Sai:

- Chọn cả đoạn dài từ `em tải xong vào...` đến `lỗi tiếp`: quá dài, chứa nhiều bước giải thích không cần thiết.

### Ví dụ 6: Rút gọn câu hỏi phàn nàn

Input:

```json
{"id":"ex_006","text":"admin ơi. sao không thấy thống kê các thông số dịch bệnh liên quan đến nước anh vậy","label":[],"meta":{"source":"UIT-ViOCD","split":"train","domain":"app","cls_label":1}}
```

Output tốt:

```json
{
  "id": "ex_006",
  "text": "admin ơi. sao không thấy thống kê các thông số dịch bệnh liên quan đến nước anh vậy",
  "spans": [
    {"start": 15, "end": 79, "text": "không thấy thống kê các thông số dịch bệnh liên quan đến nước anh", "label": "COMP"}
  ],
  "reason": "Cụm này nêu vấn đề thiếu thống kê liên quan đến nước Anh; bỏ phần gọi admin và từ hỏi."
}
```

Sai:

- Chọn cả câu gồm `admin ơi. sao... vậy`: quá dài, chứa phần gọi admin và khung câu hỏi không cần thiết.

## Output JSON schema bắt buộc

Mỗi input record phải trả về đúng một JSON object:

```json
{
  "id": "<id>",
  "text": "<original text>",
  "spans": [
    {
      "start": 0,
      "end": 10,
      "text": "<exact substring>",
      "label": "COMP"
    }
  ],
  "reason": "<short Vietnamese explanation>"
}
```

Ràng buộc bắt buộc:

- Không thêm markdown trong output cuối cùng nếu tool yêu cầu JSONL.
- Mỗi dòng là một JSON object hợp lệ.
- Không đổi `id`.
- Không sửa `text`.
- `span.text` phải khớp chính xác `text[start:end]`.
- Chỉ dùng label `COMP`.

## Prompt hoàn chỉnh để copy vào AI tool

Bạn là annotator cho bài toán complaint span extraction trong review tiếng Việt.

Nhiệm vụ: Với mỗi input JSON object, hãy tìm các complaint spans. Complaint span là cụm từ ngắn nhất nhưng đủ nghĩa trong review thể hiện nội dung khiếu nại/phàn nàn của người dùng.

Chỉ dùng nhãn `COMP`.

Quy tắc:

1. Chỉ chọn cụm thể hiện vấn đề/khiếu nại.
2. Không chọn toàn câu nếu có thể chọn cụm ngắn hơn.
3. Không chọn phần khen, phần trung tính, hoặc thông tin nền không trực tiếp là khiếu nại.
4. Không chọn emoji riêng lẻ làm complaint span.
5. Nếu review có nhiều lỗi/khiếu nại, trả về nhiều span.
6. Nếu complaint là gián tiếp hoặc nói bóng gió, chọn cụm thể hiện ý không hài lòng rõ nhất.
7. Nếu không tìm được span rõ ràng, trả về `spans = []` và ghi lý do trong `reason`.
8. Span phải là substring xuất hiện nguyên văn trong `text`.
9. `start` và `end` là character offset theo Python slicing: `text[start:end] == span_text`.
10. Giữ nguyên chính tả, teencode, viết tắt và dấu câu như trong text gốc.
11. Ưu tiên chọn cụm nguyên nhân/vấn đề chính, không chọn cả câu giải thích dài.
12. Span lý tưởng thường từ 2 đến 8 token.
13. Chỉ chọn span dài hơn 12 token nếu không thể rút ngắn mà vẫn đủ nghĩa.
14. Bỏ các cụm mở đầu không cần thiết như `tôi thấy`, `mình thấy`, `em tải xong vào thì`, `tại sao các ông lại`, nếu phần còn lại vẫn thể hiện rõ complaint.
15. Với lỗi lặp lại, chọn cụm lỗi trung tâm như `tải xong lỗi`, `lại lỗi tiếp`, thay vì chọn toàn bộ quá trình.
16. Với câu hỏi phàn nàn, chọn phần vấn đề chính, ví dụ `không thấy thống kê dịch bệnh liên quan đến nước Anh`, không cần chọn `admin ơi. sao... vậy`.
17. Với góp ý tính năng, chỉ gán `COMP` nếu có bất cập rõ; nếu chỉ là đề xuất trung tính thì trả về `spans = []`.

Output bắt buộc cho mỗi input:

```json
{
  "id": "<id>",
  "text": "<original text>",
  "spans": [
    {
      "start": 0,
      "end": 10,
      "text": "<exact substring>",
      "label": "COMP"
    }
  ],
  "reason": "<giải thích ngắn bằng tiếng Việt>"
}
```

Hãy trả về JSONL: mỗi dòng là một JSON object hợp lệ, không bọc trong markdown, không thêm giải thích ngoài trường `reason`.
