# Annotation V1 vs V2 Comparison

## Summary

- Total records: `20`
- Total tokens: `765`
- COMP tokens V1: `328`
- COMP tokens V2: `249`
- Absolute reduction: `79`
- Percent reduction: `24.09%`
- Records reduced: `12`
- Records unchanged: `8`
- Records increased: `0`
- Avg span token length V1: `8.63`
- Avg span token length V2: `6.38`

## Per-record Table

| id | comp_v1 | comp_v2 | delta | spans_v1 | spans_v2 |
|---|---:|---:|---:|---:|---:|
| `train_000193` | 4 | 2 | -2 | 1 | 1 |
| `train_000203` | 16 | 14 | -2 | 2 | 2 |
| `train_000221` | 6 | 6 | 0 | 2 | 2 |
| `train_000249` | 39 | 29 | -10 | 4 | 4 |
| `train_000645` | 0 | 0 | 0 | 0 | 0 |
| `train_000686` | 17 | 14 | -3 | 3 | 3 |
| `train_000748` | 8 | 7 | -1 | 2 | 2 |
| `train_000828` | 10 | 10 | 0 | 2 | 2 |
| `train_001059` | 24 | 20 | -4 | 2 | 2 |
| `train_001547` | 7 | 3 | -4 | 1 | 1 |
| `train_001727` | 37 | 10 | -27 | 1 | 2 |
| `train_001758` | 15 | 12 | -3 | 2 | 2 |
| `train_001836` | 7 | 7 | 0 | 2 | 2 |
| `train_001926` | 35 | 35 | 0 | 3 | 3 |
| `train_002144` | 51 | 32 | -19 | 5 | 5 |
| `train_003263` | 4 | 4 | 0 | 1 | 1 |
| `train_003285` | 16 | 14 | -2 | 1 | 1 |
| `train_003930` | 8 | 8 | 0 | 1 | 1 |
| `train_004260` | 18 | 16 | -2 | 2 | 2 |
| `train_004263` | 6 | 6 | 0 | 1 | 1 |

## Largest Reductions

### `train_001727`

- Delta COMP tokens: `-27`
- Text: anh chị xem khắc phục lại lỗi hộ em với ạ, em tải xong vào thì bảo tải dữ liệu, vừa hiện tải xong lỗi, thử lại thì lại hiện tải xong lại lỗi tiếp,cứ như vậy dù em đã xoá đi tải lại 3 lần rồi ạ, em nghe nói aP này tốt nên tải dùng, mong ac fix nhanh để em trải nghiệm thử ạ, em xin cảm ơn ạ.
- V1 spans: [43:192] `em tải xong vào thì bảo tải dữ liệu, vừa hiện tải xong lỗi, thử lại thì lại hiện tải xong lại lỗi tiếp,cứ như vậy dù em đã xoá đi tải lại 3 lần rồi ạ` (37 tok)
- V2 spans: [89:101] `tải xong lỗi` (3 tok)<br>[115:145] `lại hiện tải xong lại lỗi tiếp` (7 tok)

### `train_002144`

- Delta COMP tokens: `-19`
- Text: game không hề cân bằng, nạp và không nạp quá khác biệt, hệ thống tìm trận không cân xứng lực chiến 5k gặp 10k 3 ván liền thì chơi gì? và ngoài việc nạp thẻ thì đá cường hoá lấy ở đâu ra??? hay là vng không quan tâm đến người chơi mà chỉ quan tâm đến tiền thu từ nạp thẻ? game hút máu à?
- V1 spans: [0:22] `game không hề cân bằng` (5 tok)<br>[24:54] `nạp và không nạp quá khác biệt` (7 tok)<br>[56:133] `hệ thống tìm trận không cân xứng lực chiến 5k gặp 10k 3 ván liền thì chơi gì?` (18 tok)<br>[196:270] `vng không quan tâm đến người chơi mà chỉ quan tâm đến tiền thu từ nạp thẻ?` (17 tok)<br>[271:286] `game hút máu à?` (4 tok)
- V2 spans: [0:22] `game không hề cân bằng` (5 tok)<br>[24:54] `nạp và không nạp quá khác biệt` (7 tok)<br>[56:98] `hệ thống tìm trận không cân xứng lực chiến` (9 tok)<br>[160:185] `đá cường hoá lấy ở đâu ra` (7 tok)<br>[271:286] `game hút máu à?` (4 tok)

### `train_000249`

- Delta COMP tokens: `-10`
- Text: facebOk làm ăn kiểu gì vậy, tài khoản cá nhân của tôi không vi phạm tiêu chuẩn cộng đồng gì cả, mà tại sao các ông lại vô hiệu hoá tài khoảng của tôi, tôi thấy facebOk làm ăn quá tệ!!, tài khoản của tôi là chính chủ tên thật có cả cmnd mà facebOk lại vô hiệu hoá tài khoản của tôi không có lý do g... bài đánh giá đầy đủ
- V1 spans: [0:26] `facebOk làm ăn kiểu gì vậy` (6 tok)<br>[99:149] `tại sao các ông lại vô hiệu hoá tài khoảng của tôi` (12 tok)<br>[151:183] `tôi thấy facebOk làm ăn quá tệ!!` (7 tok)<br>[239:297] `facebOk lại vô hiệu hoá tài khoản của tôi không có lý do g` (14 tok)
- V2 spans: [0:26] `facebOk làm ăn kiểu gì vậy` (6 tok)<br>[119:149] `vô hiệu hoá tài khoảng của tôi` (7 tok)<br>[160:183] `facebOk làm ăn quá tệ!!` (5 tok)<br>[251:295] `vô hiệu hoá tài khoản của tôi không có lý do` (11 tok)

### `train_001059`

- Delta COMP tokens: `-4`
- Text: mỗi lần cập nhật lại tốn mấy trăm mình dung lượng. lần này cũng vậy chả lẻ mỗi điện thoại chỉ tải  được  một game như thế này thôi sao? iG nên xem xét lại mà giảm bớt dung lượng game lại đi, còn không có thể iG sẽ giảm bớt nhiều người chơi đấy nhé! mỗi lần cập nhật đa phần không có tính năng nào hay ho ngoại... bài đánh giá đầy đủ
- V1 spans: [0:49] `mỗi lần cập nhật lại tốn mấy trăm mình dung lượng` (11 tok)<br>[249:303] `mỗi lần cập nhật đa phần không có tính năng nào hay ho` (13 tok)
- V2 spans: [8:49] `cập nhật lại tốn mấy trăm mình dung lượng` (9 tok)<br>[257:303] `cập nhật đa phần không có tính năng nào hay ho` (11 tok)

### `train_001547`

- Delta COMP tokens: `-4`
- Text: cứ nói to là được nhưng nó bảo là bạn nhắn tin o không nghe rõ
- V1 spans: [34:62] `bạn nhắn tin o không nghe rõ` (7 tok)
- V2 spans: [49:62] `không nghe rõ` (3 tok)
