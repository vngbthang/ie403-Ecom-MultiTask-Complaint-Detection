# Priority Annotation Review - Batch 200 for Pilot300

## Summary

- Total records: `200`
- MUST_FIX_OVERLAP records: `5`
- NEEDS_REVIEW_HIGH records: `61`
- NEEDS_REVIEW_LOW records: `0`
- LIKELY_OK records: `63`
- Recommended action: Fix MUST_FIX_OVERLAP first, then review NEEDS_REVIEW_HIGH. NEEDS_REVIEW_LOW can be spot-checked before merge.

## A. MUST_FIX_OVERLAP

### train_000055

Text: nói là  được  tặng khi mua hoá đơn 486k trở lên mà không thấy có gì.rất thất vọng.

Current spans:
- #0 [51:67] COMP (4 tok): `không thấy có gì`
- #1 [68:81] COMP (3 tok): `rất thất vọng`

Overlap pairs:
- warning span_index=1: Span overlaps tokens already labeled by an earlier span; earlier span labels were kept.

Suggested action: `keep longer / keep shorter / split / drop duplicate`

Human action: KEEP_LONGER / KEEP_SHORTER / SPLIT / DROP_DUPLICATE / OTHER
Notes:

### train_001937

Text: những đoạn chuyện chêm voice bị thiếu rất nhiều lại còn thiếu những chỗ cần nghe để điền từ.ví dụ như unit 7 trang 71 của sách phiên bản cũ thì mất luôn cái dòng đối thoại thứ nhất , ở trang 79 của unit 8 cũng mất hẳng đoạn voice dài 3 dòng ở cuối đoạn chuyện chêm và còn nhiều nữa. thế thì biết cái ... bài đánh giá đầy...

Current spans:
- #0 [56:91] COMP (8 tok): `thiếu những chỗ cần nghe để điền từ`
- #1 [92:180] COMP (21 tok): `ví dụ như unit 7 trang 71 của sách phiên bản cũ thì mất luôn cái dòng đối thoại thứ nhất`
- #2 [183:281] COMP (23 tok): `ở trang 79 của unit 8 cũng mất hẳng đoạn voice dài 3 dòng ở cuối đoạn chuyện chêm và còn nhiều nữa`

Overlap pairs:
- warning span_index=1: Span overlaps tokens already labeled by an earlier span; earlier span labels were kept.

Suggested action: `keep longer / keep shorter / split / drop duplicate`

Human action: KEEP_LONGER / KEEP_SHORTER / SPLIT / DROP_DUPLICATE / OTHER
Notes:

### train_002813

Text: mình đặt 2 đơn là 10 áo,sao  cửa hàng  giao thiếu 2 đơn là 4 áo,rất thất vọng,mong cửa hàng gửi lại số áo đang còn thiếu,ko cho kiểm hàng giờ giao thiếu sản phẩm cho khách rồi

Current spans:
- #0 [0:23] COMP (7 tok): `mình đặt 2 đơn là 10 áo`
- #1 [24:63] COMP (10 tok): `sao  cửa hàng  giao thiếu 2 đơn là 4 áo`
- #2 [64:77] COMP (3 tok): `rất thất vọng`
- #3 [115:120] COMP (1 tok): `thiếu`
- #4 [121:175] COMP (12 tok): `ko cho kiểm hàng giờ giao thiếu sản phẩm cho khách rồi`

Overlap pairs:
- warning span_index=1: Span overlaps tokens already labeled by an earlier span; earlier span labels were kept.
- warning span_index=2: Span overlaps tokens already labeled by an earlier span; earlier span labels were kept.
- warning span_index=4: Span overlaps tokens already labeled by an earlier span; earlier span labels were kept.

Suggested action: `keep longer / keep shorter / split / drop duplicate`

Human action: KEEP_LONGER / KEEP_SHORTER / SPLIT / DROP_DUPLICATE / OTHER
Notes:

### train_003489

Text: đéo mẹ game như C vào tạo nv là đứng nếu chplay cho đánh giá âm sao bố cho âm luôn rồi.tốt nhất anh em đừng tải mất công lại xoá

Current spans:
- #0 [0:86] COMP (22 tok): `đéo mẹ game như C vào tạo nv là đứng nếu chplay cho đánh giá âm sao bố cho âm luôn rồi`
- #1 [87:128] COMP (10 tok): `tốt nhất anh em đừng tải mất công lại xoá`

Overlap pairs:
- warning span_index=1: Span overlaps tokens already labeled by an earlier span; earlier span labels were kept.

Suggested action: `keep longer / keep shorter / split / drop duplicate`

Human action: KEEP_LONGER / KEEP_SHORTER / SPLIT / DROP_DUPLICATE / OTHER
Notes:

### train_004295

Text: rõ ràng mình đã nhắn tin hỏi  cửa hàng ..mình cũng đặt như này ta cái bảng kèm hàng tặng. vậy mà hàng gửi về vẫn lồn có hàng tặng..hơi thất vọng

Current spans:
- #0 [41:88] COMP (11 tok): `mình cũng đặt như này ta cái bảng kèm hàng tặng`
- #1 [97:129] COMP (8 tok): `hàng gửi về vẫn lồn có hàng tặng`
- #2 [131:144] COMP (3 tok): `hơi thất vọng`

Overlap pairs:
- warning span_index=2: Span overlaps tokens already labeled by an earlier span; earlier span labels were kept.

Suggested action: `keep longer / keep shorter / split / drop duplicate`

Human action: KEEP_LONGER / KEEP_SHORTER / SPLIT / DROP_DUPLICATE / OTHER
Notes:


## B. NEEDS_REVIEW_HIGH

### train_003601

Text: kem nền có mùi cồn nhiều mà còn nồng nặc nữa, tets thử lên tay thì kem dạng lỏng và tets bị lộ vân kem và khô. nắp thì hờ hừng không khít nói chung là rất luồn không biết có phải hàng chính hãng k. thực sự là rất buồn 😥😥😢😢😢

Warning reasons:
- span #0 bắt đầu từ đầu text và dài > 8 tokens
- span #1 dài >= 15 tokens (19)
- COMP ratio > 60% (69.2%)

Current spans:
- #0 [0:44] COMP (11 tok): `kem nền có mùi cồn nhiều mà còn nồng nặc nữa`
- #1 [111:196] COMP (19 tok): `nắp thì hờ hừng không khít nói chung là rất luồn không biết có phải hàng chính hãng k`
- #2 [198:223] COMP (6 tok): `thực sự là rất buồn 😥😥😢😢😢`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002332

Text: gọi xe cứ bị huỷ chuyến rất mất thời gian.. có lần tài xế đi rồi.. lại gọi điện thoại bảo mình huỷ chuyến.. chưa kịp huỷ đang tìm grab để đi thì cứ gọi đến giục huỷ chuyến đi. rất mất thời gian và bất tiện. đang lúc gấp gáp cứ bị huỷ chuyến liên tục rất là bực mình..

Warning reasons:
- span #0 bắt đầu từ đầu text và dài > 8 tokens
- span #2 dài >= 15 tokens (16)
- nhiều hơn 4 spans (5)
- COMP ratio > 60% (90.2%)

Current spans:
- #0 [0:41] COMP (10 tok): `gọi xe cứ bị huỷ chuyến rất mất thời gian`
- #1 [67:105] COMP (8 tok): `lại gọi điện thoại bảo mình huỷ chuyến`
- #2 [108:174] COMP (16 tok): `chưa kịp huỷ đang tìm grab để đi thì cứ gọi đến giục huỷ chuyến đi`
- #3 [176:205] COMP (7 tok): `rất mất thời gian và bất tiện`
- #4 [207:265] COMP (14 tok): `đang lúc gấp gáp cứ bị huỷ chuyến liên tục rất là bực mình`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_001369

Text: tôi rất thích tựa game này nhưng tôi không hài lòng với việc mỗi khi cập nhật oby mới thì hãy đặt chính xác số giờ hết bảo trì chứ cứ nói lúc 11h đến 6h30 sau đó lại nói là 12h đến 7h30 rồi tiếp đó thì lại nói là 12h đến 8h30 tôi cảm thấy khá bực mình về chuyện này mong admin giúp đỡ và tôi cũng nghỉ là nê... bài đánh ...

Warning reasons:
- span #0 dài >= 15 tokens (66)
- COMP ratio > 60% (84.6%)

Current spans:
- #0 [33:307] COMP (66 tok): `tôi không hài lòng với việc mỗi khi cập nhật oby mới thì hãy đặt chính xác số giờ hết bảo trì chứ cứ nói lúc 11h đến 6h30 sau đó lại nói là 12h đến 7h30 rồi tiếp đó thì lại nói là 12h đến 8h30 tôi cảm thấy khá bực mình về chuyện này mong admin giúp đỡ và tôi cũng nghỉ là nê`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_000561

Text: đây là từ điển nhật - việt chứ đâu phải từ điển nhật - anh đâu mà chỉ có tuếng anh khi tra vậy? tôi thấy rất tiếc khi cho   1star   nhưng thật sự mà nói điều này không phù hợp cho người không giỏi tiếng anh. rất mong khắc phục.

Warning reasons:
- span #0 dài >= 15 tokens (24)
- span #0 bắt đầu từ đầu text và dài > 8 tokens
- COMP ratio > 60% (70.6%)

Current spans:
- #0 [0:94] COMP (24 tok): `đây là từ điển nhật - việt chứ đâu phải từ điển nhật - anh đâu mà chỉ có tuếng anh khi tra vậy`
- #1 [149:206] COMP (12 tok): `nói điều này không phù hợp cho người không giỏi tiếng anh`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_003574

Text: hàng  được  nhưng dải hơi mỏng nhưng được lắm đẹp như hình... nhưng mà mình thất vọng về shiper của lazada quá kêu giao tận nhà mà không khi nào

Warning reasons:
- span #0 bắt đầu từ đầu text và dài > 8 tokens
- span #1 dài >= 15 tokens (16)
- COMP ratio > 60% (93.3%)

Current spans:
- #0 [0:58] COMP (12 tok): `hàng  được  nhưng dải hơi mỏng nhưng được lắm đẹp như hình`
- #1 [71:144] COMP (16 tok): `mình thất vọng về shiper của lazada quá kêu giao tận nhà mà không khi nào`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002643

Text: tôi sử dụng dịch vụ nạp tiền điện thoại qua ví điện tử grabpay. tôi có thao tác mua mã thẻ cào vieTel mệnh giá 30.000d và nhận  được  yêu cầu chờ xử lý trong vòng 1h. tôi vui vẻ chờ đợi nhưng 3h sau vẫn không nhận được mã thẻ nạp cũng không có hoàn trả vào ví điện tử grabpay của tôi. tôi có gửi email m... bài đánh giá ...

Warning reasons:
- span #0 dài >= 15 tokens (21)

Current spans:
- #0 [192:283] COMP (21 tok): `3h sau vẫn không nhận được mã thẻ nạp cũng không có hoàn trả vào ví điện tử grabpay của tôi`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002068

Text: điện thoại mà bọc hàng chán không chịu  được , không có lót gì bên trong hộp, không đề hàng dễ rơi vớ. cạch lazada đến già  quả  mua hàng đắt tiền thế này.

Warning reasons:
- COMP ratio > 60% (70.6%)

Current spans:
- #0 [14:44] COMP (6 tok): `bọc hàng chán không chịu  được`
- #1 [47:76] COMP (7 tok): `không có lót gì bên trong hộp`
- #2 [103:154] COMP (11 tok): `cạch lazada đến già  quả  mua hàng đắt tiền thế này`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_003691

Text: tin tưởng phân phối chính hãng và mua hàng, mở hộp thì trên seal màn hình dính bụi, mặt sau 4 camera thì bị lệch hết 2 cam dưới. gia công tệ kinh khủng. có lẽ do mua đợt đèn flash sale nên vậy

Warning reasons:
- span #0 bắt đầu từ đầu text và dài > 8 tokens

Current spans:
- #0 [0:42] COMP (9 tok): `tin tưởng phân phối chính hãng và mua hàng`
- #1 [84:127] COMP (11 tok): `mặt sau 4 camera thì bị lệch hết 2 cam dưới`
- #2 [129:151] COMP (5 tok): `gia công tệ kinh khủng`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_001961

Text: màn hình có phần kim cương hoặc dấu cộng rất vướng víu khi tìm kiếm. nếu nhóm sáng chế có thể cài phím này dịch chuyển giống phím home của iphone thì sẽ tiện lợi hơn nhiều.

Warning reasons:
- span #0 dài >= 15 tokens (15)

Current spans:
- #0 [2:67] COMP (15 tok): `n hình có phần kim cương hoặc dấu cộng rất vướng víu khi tìm kiếm`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002360

Text: nói khuyến mại sữa rửa mặt nhưng lại không hề có và cũng không hề thông báo cho khách hàng. thất vọng về  cửa hàng .

Warning reasons:
- COMP ratio > 60% (69.2%)

Current spans:
- #0 [33:90] COMP (13 tok): `lại không hề có và cũng không hề thông báo cho khách hàng`
- #1 [92:114] COMP (5 tok): `thất vọng về  cửa hàng`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_001530

Text: không thấy sản phẩm tặng kèm thật thất vọng với chất lượng dịch vụ như thế đóng gói sản phẩm rất tốt

Warning reasons:
- span #0 dài >= 15 tokens (22)
- span #0 bắt đầu từ đầu text và dài > 8 tokens
- COMP ratio > 60% (100.0%)

Current spans:
- #0 [0:100] COMP (22 tok): `không thấy sản phẩm tặng kèm thật thất vọng với chất lượng dịch vụ như thế đóng gói sản phẩm rất tốt`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_000020

Text: em có một tài khoản lần đầu em bị mất xim nên em đã thêm số điện thoại mới. thế mà mới vừa rồi em đổi mật khẩu quên khuấy mất. nên em dùng số mới để quên mật khẩu mà nó cứ đòi gửi mã về số điện thoại cũ kia. bây giờ em không biết làm như thế này cả, tài khoản ấy em chơi mấy năm rồi .

Warning reasons:
- span #0 dài >= 15 tokens (19)
- span #0 bắt đầu từ đầu text và dài > 8 tokens

Current spans:
- #0 [0:74] COMP (19 tok): `em có một tài khoản lần đầu em bị mất xim nên em đã thêm số điện thoại mới`
- #1 [83:125] COMP (10 tok): `mới vừa rồi em đổi mật khẩu quên khuấy mất`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002483

Text: tưởng mua được samsung mới mà ai dè máy đã bị kích hoạt 2 tháng bảo hành rồi 😭

Warning reasons:
- spans=[] nhưng cls_label=1

Current spans:
- _No spans_

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002047

Text: dép nhẹ, đẹp được nhưng đặt  cỡ  37 mà giao  cỡ  38 mang rộng chân không  được  đẹp lắm. cửa hàng  rút kinh nghiệm lần sau đừng nhầm lẩn nha  cửa hàng .

Warning reasons:
- COMP ratio > 60% (69.7%)

Current spans:
- #0 [39:87] COMP (10 tok): `giao  cỡ  38 mang rộng chân không  được  đẹp lắm`
- #1 [89:150] COMP (13 tok): `cửa hàng  rút kinh nghiệm lần sau đừng nhầm lẩn nha  cửa hàng`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_003969

Text: kaka, đồ mỏng le áo còn bị dơ, đúng tiền nào của nấy.

Warning reasons:
- spans=[] nhưng cls_label=1

Current spans:
- _No spans_

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_003083

Text: điện thoại cảm ứng không được nhảy cho lắm đóng gói không chắc chắn còn lại đều rất ngon trong tầm giá này

Warning reasons:
- span #0 dài >= 15 tokens (23)
- span #0 bắt đầu từ đầu text và dài > 8 tokens
- COMP ratio > 60% (100.0%)

Current spans:
- #0 [0:106] COMP (23 tok): `điện thoại cảm ứng không được nhảy cho lắm đóng gói không chắc chắn còn lại đều rất ngon trong tầm giá này`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_003604

Text: liên quân phiên bản 3.0 thật sự quá tệ. tôi chơi liên quân từ khi mới ra nhưng phiên bản hiện tại làm tôi rất thất vọng . bản đồ giao diện thật sự nhìn rất tệ . thật sự tôi phải xoá game bởi vì nó rất tệ khôg phải riêng tôi mà là tất cả mọi người đều quen với bản đồ cũ. mong lần cập nhật tiếp theo sẽ... bài đánh giá đầ...

Warning reasons:
- span #3 dài >= 15 tokens (27)
- COMP ratio > 60% (64.9%)

Current spans:
- #0 [22:38] COMP (5 tok): `0 thật sự quá tệ`
- #1 [79:119] COMP (9 tok): `phiên bản hiện tại làm tôi rất thất vọng`
- #2 [122:158] COMP (9 tok): `bản đồ giao diện thật sự nhìn rất tệ`
- #3 [161:269] COMP (27 tok): `thật sự tôi phải xoá game bởi vì nó rất tệ khôg phải riêng tôi mà là tất cả mọi người đều quen với bản đồ cũ`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_004137

Text: không hiểu vì sao điện thoại của mình là điện thoại mới. mình tải twiTer về trên dưới 20 lần rồi. và mỗi lần đăng kí đều không được. nhờ người khác  được  để mình đăng nhập nó cứ để là   rất tiếc lỗi đã xảy ra. mong thử lại sao 

Warning reasons:
- span #1 dài >= 15 tokens (18)

Current spans:
- #0 [98:131] COMP (8 tok): `và mỗi lần đăng kí đều không được`
- #1 [133:209] COMP (18 tok): `nhờ người khác  được  để mình đăng nhập nó cứ để là   rất tiếc lỗi đã xảy ra`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_004203

Text: mình không biết các bạn tải như thế nào nha chứ mình là có tải 3 trò ( 2 trò kia đã tải từ trước rồi nên mình không nghi ngờ)nhưng khi mới tải guNy, mình chơi mới có một ngày mà bị hack facebOk qua tiếng trung quốc rồi còn bị aD thêm mấy cái  quả người cáo bla...bla...bla vào những cái bài viết ở facebOk của mình... bà...

Warning reasons:
- spans=[] nhưng cls_label=1

Current spans:
- _No spans_

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_003695

Text: khôi phục lại tin nhắn cũ đã sao lưu thì bị mất hết những tin nhắn mới (mặc dù các tin nhắn mới này đều đã  được  sao lưu). và không cách nào lấy lại  được . rất không hài lòng. nếu khôi phục lại tin nhắn cũ để rồi mất hết những tin nhắn mới thì tính năng này thà không có còn hơn

Warning reasons:
- span #0 dài >= 15 tokens (29)
- span #0 bắt đầu từ đầu text và dài > 8 tokens
- span #2 dài >= 15 tokens (24)
- COMP ratio > 60% (87.7%)

Current spans:
- #0 [0:122] COMP (29 tok): `khôi phục lại tin nhắn cũ đã sao lưu thì bị mất hết những tin nhắn mới (mặc dù các tin nhắn mới này đều đã  được  sao lưu)`
- #1 [158:176] COMP (4 tok): `rất không hài lòng`
- #2 [178:280] COMP (24 tok): `nếu khôi phục lại tin nhắn cũ để rồi mất hết những tin nhắn mới thì tính năng này thà không có còn hơn`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_003659

Text: giao hàng nhanh hàng đúng mẫu,có điều hơi chảy ,nóng chắc do giao giữa trưa(mà sao nhìn ảnh thấy có quà tặng kèm giờ nhận hàng rồi không thấy)

Warning reasons:
- COMP ratio > 60% (69.0%)

Current spans:
- #0 [0:29] COMP (6 tok): `giao hàng nhanh hàng đúng mẫu`
- #1 [79:142] COMP (14 tok): `sao nhìn ảnh thấy có quà tặng kèm giờ nhận hàng rồi không thấy)`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_004035

Text: sử dụng zing id đăng nhập không được , cứ báo mật khẩu hoặc tài khoảng không chính xác , tưởng mình nhập sai đi lên trang zing id lấy mật khẩu qua đăng nhập cũng không được , nghi là lỗi do mật khẩu lên trang chủ đổi lại vào đăng nhập game lại báo mật khẩu hoặc tài khoảng không chính xác bình chọn   1star   cho... bài ...

Warning reasons:
- span #1 dài >= 15 tokens (18)
- span #2 dài >= 15 tokens (29)
- COMP ratio > 60% (75.3%)

Current spans:
- #0 [0:36] COMP (8 tok): `sử dụng zing id đăng nhập không được`
- #1 [89:172] COMP (18 tok): `tưởng mình nhập sai đi lên trang zing id lấy mật khẩu qua đăng nhập cũng không được`
- #2 [175:312] COMP (29 tok): `nghi là lỗi do mật khẩu lên trang chủ đổi lại vào đăng nhập game lại báo mật khẩu hoặc tài khoảng không chính xác bình chọn   1star   cho`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_001278

Text: mọi người không nên đăng kí học online nhé tải sử dụng thôi chứ giáo viên hỗ trợ gần như không có tác dụng gì mấy đâu bài giảng xem cũng hết sức bình thường không hẳn là dễ hiểu lắm khi nên bài cao, mọi người có thể rất sánh với các video hướng dẫn khác trên mạng thì video giảng bài không hữu ích lắm, n... bài đánh giá...

Warning reasons:
- span #0 dài >= 15 tokens (45)
- span #0 bắt đầu từ đầu text và dài > 8 tokens
- COMP ratio > 60% (61.6%)

Current spans:
- #0 [0:197] COMP (45 tok): `mọi người không nên đăng kí học online nhé tải sử dụng thôi chứ giáo viên hỗ trợ gần như không có tác dụng gì mấy đâu bài giảng xem cũng hết sức bình thường không hẳn là dễ hiểu lắm khi nên bài cao`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_001364

Text: tôi không hiểu vì sao facebOk lại bắt xác nhận danh tính và không cho người dùng đổi tên, mà lại bắt buộc dùng đúng tên của mình, tôi thấy khá khó chịu về điều này, cứ cho là vì facebOk muốn  quả nó lý chặt hơn để tránh những tài khoản giả mạo đi, nhưng mà gần đây lại có vấn đề xảy ra làm tôi càng k... bài đánh giá đầy...

Warning reasons:
- span #0 dài >= 15 tokens (19)
- span #0 bắt đầu từ đầu text và dài > 8 tokens
- span #2 dài >= 15 tokens (19)
- COMP ratio > 60% (62.2%)

Current spans:
- #0 [0:88] COMP (19 tok): `tôi không hiểu vì sao facebOk lại bắt xác nhận danh tính và không cho người dùng đổi tên`
- #1 [130:163] COMP (8 tok): `tôi thấy khá khó chịu về điều này`
- #2 [165:246] COMP (19 tok): `cứ cho là vì facebOk muốn  quả nó lý chặt hơn để tránh những tài khoản giả mạo đi`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002866

Text: game trải nghiệm rất tuyệt vời. nhưng bị hack nhiều quá với lại có những người chơi dùng thiết bị hổ trợ còn giả lập nữa, chơi như vậy thì những người chơi bằng di động hay máy tính bảng thì chắc không địch lại nổi,,,, huy vọng nhà phát hành game xem lại... vì một cộng đồng game công bằng...

Warning reasons:
- spans=[] nhưng cls_label=1

Current spans:
- _No spans_

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_000003

Text: máy khá đẹp,pin trâu vân tay nhạy nhận diện khuôn mặt nhanh nói chung ổn.tuy chơi game frE fire bị chậm khung hình không mượt lắm nhưng với giá giẫm ngày 1111 được aD mã giảm giá 200k còn hơn 2tr6 thì vậy là ngon rồi

Warning reasons:
- span #0 dài >= 15 tokens (31)
- COMP ratio > 60% (67.4%)

Current spans:
- #0 [77:216] COMP (31 tok): `chơi game frE fire bị chậm khung hình không mượt lắm nhưng với giá giẫm ngày 1111 được aD mã giảm giá 200k còn hơn 2tr6 thì vậy là ngon rồi`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_000457

Text: sản phẩm dùng rất tốt và hiệu  quả  . giao hàng cũng rất nhanh . nhưng sản phẩm có mùi không được thơm làm khi nhỏ giọt ra tay xài cũng khó chịu. sản phẩm hơi mắc chỉ đợi đến giảm giá mới mua .

Warning reasons:
- span #1 dài >= 15 tokens (17)

Current spans:
- #0 [38:62] COMP (5 tok): `giao hàng cũng rất nhanh`
- #1 [71:144] COMP (17 tok): `sản phẩm có mùi không được thơm làm khi nhỏ giọt ra tay xài cũng khó chịu`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_001130

Text: hiện tại tôi dùng oPo a37 để chơi nhưng vào được khoảng 30s và làm vài thao tác là game bị đứng và không thể làm gì khác ngoài thoát game. dù tôi không chạy thêm ứng dụng ngầm nào của bên thứ ba nữa.

Warning reasons:
- span #0 dài >= 15 tokens (22)
- COMP ratio > 60% (80.0%)

Current spans:
- #0 [40:137] COMP (22 tok): `vào được khoảng 30s và làm vài thao tác là game bị đứng và không thể làm gì khác ngoài thoát game`
- #1 [139:198] COMP (14 tok): `dù tôi không chạy thêm ứng dụng ngầm nào của bên thứ ba nữa`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_003770

Text: tôi dùng 2 tài khoản facebOk, cài meSenger. trong khi tài khoản cũ vẫn bình thường, tài khoản mới tôi vừa nhắn vài tin bỗng mất hết lịch sử tin nhắn, và người khác gửi tin nhắn có thông báo nhưng mở ra không thấy đâu cả. mỗi lần chuyển tài khoản đăng xuất mất 4-5 phút. đề nghị nC sớm sửa lỗi.

Warning reasons:
- span #0 dài >= 15 tokens (15)

Current spans:
- #0 [84:148] COMP (15 tok): `tài khoản mới tôi vừa nhắn vài tin bỗng mất hết lịch sử tin nhắn`
- #1 [196:219] COMP (6 tok): `mở ra không thấy đâu cả`
- #2 [221:268] COMP (10 tok): `mỗi lần chuyển tài khoản đăng xuất mất 4-5 phút`
- #3 [270:292] COMP (6 tok): `đề nghị nC sớm sửa lỗi`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_004087

Text: chất lượng sản phẩm tốt theo đơn hàng là có  sản phẩm  tặng kèm nhưng giao về

Warning reasons:
- span #0 dài >= 15 tokens (17)
- span #0 bắt đầu từ đầu text và dài > 8 tokens
- COMP ratio > 60% (100.0%)

Current spans:
- #0 [0:77] COMP (17 tok): `chất lượng sản phẩm tốt theo đơn hàng là có  sản phẩm  tặng kèm nhưng giao về`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002079

Text: đồ đẹp như bi giờ lỗi ở cổ áo không  được  không lắm nhưng còn lại bộ này cũng đẹp (•‿•)(✷‿✷)

Warning reasons:
- span #0 dài >= 15 tokens (21)
- span #0 bắt đầu từ đầu text và dài > 8 tokens
- COMP ratio > 60% (100.0%)

Current spans:
- #0 [0:93] COMP (21 tok): `đồ đẹp như bi giờ lỗi ở cổ áo không  được  không lắm nhưng còn lại bộ này cũng đẹp (•‿•)(✷‿✷)`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002536

Text: vận chuyển chậm hàng đã bị kích hoạt bảo hành trước

Warning reasons:
- spans=[] nhưng cls_label=1

Current spans:
- _No spans_

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_001688

Text:  cửa hàng  đăng hình là quần ống rộng và lai cuốn mà lại gửi cho mình quần 9 tất ống ôm nhẹ . quần thì đẹp nhưng mình không thích quần 9 tất tí nào cả , mặc cũng không được thoải mái ngồi xuống rất chật , đùi mình hơi to nên thích ống rộng cho thoải mái . quần không được ưng ý nhưng mặc đi làm ai cũng khen đẹp nên mình...

Warning reasons:
- span #2 dài >= 15 tokens (22)

Current spans:
- #0 [113:150] COMP (9 tok): `mình không thích quần 9 tất tí nào cả`
- #1 [153:202] COMP (10 tok): `mặc cũng không được thoải mái ngồi xuống rất chật`
- #2 [256:355] COMP (22 tok): `quần không được ưng ý nhưng mặc đi làm ai cũng khen đẹp nên mình đánh giá lại cho  cửa hàng   5star`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_001368

Text: kem thì được nhưng quà tặng thì đã hết hạn sử dụng ... tặng thì nên tặng có tâm xíu còn không tặng cũng không sao chứ không nên tặng kèm chỉ để cho có thôi ạ

Warning reasons:
- span #0 dài >= 15 tokens (16)

Current spans:
- #0 [88:157] COMP (16 tok): `không tặng cũng không sao chứ không nên tặng kèm chỉ để cho có thôi ạ`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002396

Text: thiết kế đơn giản nhưng rất chắc chắn nhưng có một điểm trừ đối với cá nhân mình là phần thân son được phủ như tráng gương khi cầm vào hay môi chạm vào sẽ để lại vân môi hoặc vân tay. về chất son khi lên môi thì khá mịn mượt khi bặm môi thì tạo cảm giác hơi dính dính nhưng không hề làm nặng môi. màu hồng hơi hướng đỏ đ...

Warning reasons:
- span #0 dài >= 15 tokens (42)
- span #0 bắt đầu từ đầu text và dài > 8 tokens
- span #2 dài >= 15 tokens (34)
- span #3 dài >= 15 tokens (51)
- nhiều hơn 4 spans (5)
- COMP ratio > 60% (70.6%)

Current spans:
- #0 [0:182] COMP (42 tok): `thiết kế đơn giản nhưng rất chắc chắn nhưng có một điểm trừ đối với cá nhân mình là phần thân son được phủ như tráng gương khi cầm vào hay môi chạm vào sẽ để lại vân môi hoặc vân tay`
- #1 [274:295] COMP (5 tok): `không hề làm nặng môi`
- #2 [351:492] COMP (34 tok): `chỉ son thôi thì vẫn xinh chứ không dừ ( mình nghĩ nên tẩy da chết cho môi rồi thêm một lớp son dưỡng mỏng thôi rồi son em này lên là được  )`
- #3 [494:718] COMP (51 tok): `vì bản chất em này cũng là son có thành phần dưỡng rồi nên mình nghĩ không thể rất với các dòng khác về mặt lâu trôi được nhưng mình đã sử dụng qua và không dặm lại nhưng đến cuối ngày vẫn thấy còn lại trên môi màu hồng phớt`
- #4 [830:873] COMP (10 tok): `giao hàng cũng nhanh nữa nên rất hài lòng 😊`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_001423

Text: bài hát thì càng ngày càng ít và hạn chế đặc biệt là những ca khúc tiếng anh cùng theo đó thì lại bắt người tiêu dùng xem nhiều  quả người cáo trong một lần nghe những ca khúc tiếng anh  được  nghe . ứng dụng càng ngày càng tệ hại chỉ vì cái mà anh duy mạnh gọi là kiếm lợi nhuận càng nhiều càng tốt bất chấp ngườ... bài...

Warning reasons:
- span #0 dài >= 15 tokens (43)
- span #0 bắt đầu từ đầu text và dài > 8 tokens
- span #1 dài >= 15 tokens (26)
- COMP ratio > 60% (92.0%)

Current spans:
- #0 [0:197] COMP (43 tok): `bài hát thì càng ngày càng ít và hạn chế đặc biệt là những ca khúc tiếng anh cùng theo đó thì lại bắt người tiêu dùng xem nhiều  quả người cáo trong một lần nghe những ca khúc tiếng anh  được  nghe`
- #1 [200:313] COMP (26 tok): `ứng dụng càng ngày càng tệ hại chỉ vì cái mà anh duy mạnh gọi là kiếm lợi nhuận càng nhiều càng tốt bất chấp ngườ`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002531

Text: mất một tháng để người chơi mới như tôi có thể đạt được 1m5 sức mạnh, và với một cuộc xâm lược của kẻ 30m sức mạnh, tôi mất tất cả.... tôi từng yêu game này, đến mức dùng rất nhiều thời gian và giờ đây tôi chẳng còn gì. tạm biệt, tôi từ bỏ cái trò chơi khốn nạn này.

Warning reasons:
- span #0 dài >= 15 tokens (16)
- span #0 bắt đầu từ đầu text và dài > 8 tokens

Current spans:
- #0 [0:68] COMP (16 tok): `mất một tháng để người chơi mới như tôi có thể đạt được 1m5 sức mạnh`
- #1 [116:130] COMP (4 tok): `tôi mất tất cả`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002684

Text: 48 mỹ phẩm không chuẩn như các hãng điện thoại khác , nhìn như khoảng 32 mỹ phẩm là cùng , được bổ sung thêm xài mạng 5g còn được hơn

Warning reasons:
- span #0 bắt đầu từ đầu text và dài > 8 tokens

Current spans:
- #0 [0:51] COMP (11 tok): `48 mỹ phẩm không chuẩn như các hãng điện thoại khác`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_004213

Text: là một ứng dụng tốt, nên cài đặt, nhưng mà mong sẽ thay đổi một chức năng hơi bất tiện tiện. ẩn trò chuyện chỉ có thể áp dụng đối với bạn có sẵn trong danh bạ, còn người lạ bật ẩn trò chuyện lên rồi tìm lại thì không thấy đâu cả. có những người mình chưa kịp kết bạn, phải ẩn vì lí do riêng, sau kiếm... bài đánh giá đầy...

Warning reasons:
- span #1 dài >= 15 tokens (15)

Current spans:
- #0 [43:91] COMP (11 tok): `mong sẽ thay đổi một chức năng hơi bất tiện tiện`
- #1 [164:228] COMP (15 tok): `người lạ bật ẩn trò chuyện lên rồi tìm lại thì không thấy đâu cả`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_004352

Text: về phần sao lưu tin nhắn, tôi muốn hỏi là tin nhắn trong smartphone sẽ tự động biến mất dần theo năm tháng lý do là giản lược bộ nhớ, điều này sẽ dẫn đến việc sao lưu tin nhắn hằng ngày. file mới sẽ ghi đè lên file cũ trên máy chủ zalo, và khi điều này xảy ra thì tin nhắn thực tế chỉ sao lưu lại nhữ... bài đánh giá đầy...

Warning reasons:
- span #0 dài >= 15 tokens (24)

Current spans:
- #0 [26:132] COMP (24 tok): `tôi muốn hỏi là tin nhắn trong smartphone sẽ tự động biến mất dần theo năm tháng lý do là giản lược bộ nhớ`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_001725

Text: sữa rửa mặt ok, hàng chính hãng, nếu không tạo bọt kĩ thì khi rửa mấy bạn da thường sẽ khô một tí và rít rít, nhưng yên tâm chỉ khoảng 5p sau là sẽ không còn rít nữa. còn về nước tẩy trang thì có mùi trà xanh nhẹ, sạch sẽ và không phải sạch bong kin kít đâu, khi tẩy trang xong vẫn còn độ ẩm, chai 70ml xài cũng khoảng m...

Warning reasons:
- span #0 dài >= 15 tokens (19)

Current spans:
- #0 [33:108] COMP (19 tok): `nếu không tạo bọt kĩ thì khi rửa mấy bạn da thường sẽ khô một tí và rít rít`
- #1 [158:165] COMP (2 tok): `rít nữa`
- #2 [171:212] COMP (10 tok): `về nước tẩy trang thì có mùi trà xanh nhẹ`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_000800

Text: tôi đặt 2 cái ngày 2409 nhưng lazada chỉ giao một cái ngày 279. một cái đến chiều 309 vẫn đang ở tình trạng đóng gói, tôi phải gọi lên tổng đài để hỏi và được giải thích rằng đơn hàng có thể bị huỷ và không giao đến được. quá hạn giao hàng đơn hàng sẽ tự động huỷ. và khuyến khích tôi huỷ đơn hàng đặt lại.tôi đã viết em...

Warning reasons:
- span #0 dài >= 15 tokens (24)
- span #5 dài >= 15 tokens (24)
- nhiều hơn 4 spans (7)
- COMP ratio > 60% (65.0%)

Current spans:
- #0 [118:220] COMP (24 tok): `tôi phải gọi lên tổng đài để hỏi và được giải thích rằng đơn hàng có thể bị huỷ và không giao đến được`
- #1 [222:263] COMP (10 tok): `quá hạn giao hàng đơn hàng sẽ tự động huỷ`
- #2 [265:305] COMP (9 tok): `và khuyến khích tôi huỷ đơn hàng đặt lại`
- #3 [379:434] COMP (14 tok): `do tôi cần gấp nên khuya đó tôi đã phải đặt 01 đơn khác`
- #4 [436:484] COMP (11 tok): `sáng hôm sau tôi phát hiện 02 đơn đang giao hàng`
- #5 [509:606] COMP (24 tok): `không tự động huỷ và 01 đơn đặt vào tối đó vì tôi sợ qua ngày mai sẽ không còn giá khuyến mãi tốt`
- #6 [645:687] COMP (10 tok): `rất thất vọng về xử lý đơn hàng của lazada`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_003368

Text: giáo hàng chậm, phải gọi lên tổng đài mới được lưu ý giao nhanh hơn

Warning reasons:
- spans=[] nhưng cls_label=1

Current spans:
- _No spans_

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_001472

Text: hàng nguyên seal, nhưng  cửa hàng  chính hãng mà đóng gói thùng ngoài to hơn hộp điện thoại mà không có thêm gì chống sốc khi vận chuyển khiến hộp điện thoại không góc và cạnh rất nhiều, thất vọng hãng lớn mà đóng gói quá sơ sài

Warning reasons:
- span #0 dài >= 15 tokens (19)
- COMP ratio > 60% (60.4%)

Current spans:
- #0 [95:185] COMP (19 tok): `không có thêm gì chống sốc khi vận chuyển khiến hộp điện thoại không góc và cạnh rất nhiều`
- #1 [187:228] COMP (10 tok): `thất vọng hãng lớn mà đóng gói quá sơ sài`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_001640

Text: đã  cỡ  không chuẩn rồi còn lươn lẹo, đã liên hệ đổi lại  cỡ  thì báo tự trả phí giao hàng mình vẫn ok, nhưng một tuần lễ không thấy hồi âm,  nhắn tin  hỏi thì báo sẽ hối giao hàng này nọ cuối cùng tới nay vẫn chưa nhận được, tôi mua hàng để đi du lịch mà đi về rồi còn chưa nhận được hàng đổi?  cửa hàng  tệ hại !

Warning reasons:
- span #1 dài >= 15 tokens (16)
- span #3 dài >= 15 tokens (19)
- span #4 dài >= 15 tokens (17)
- nhiều hơn 4 spans (6)
- COMP ratio > 60% (89.0%)

Current spans:
- #0 [28:36] COMP (2 tok): `lươn lẹo`
- #1 [38:102] COMP (16 tok): `đã liên hệ đổi lại  cỡ  thì báo tự trả phí giao hàng mình vẫn ok`
- #2 [110:139] COMP (7 tok): `một tuần lễ không thấy hồi âm`
- #3 [142:224] COMP (19 tok): `nhắn tin  hỏi thì báo sẽ hối giao hàng này nọ cuối cùng tới nay vẫn chưa nhận được`
- #4 [226:293] COMP (17 tok): `tôi mua hàng để đi du lịch mà đi về rồi còn chưa nhận được hàng đổi`
- #5 [296:312] COMP (4 tok): `cửa hàng  tệ hại`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_001947

Text: màu lên đẹp nhưng lúc mình ngửi có mùi như mùi cồn rất khó chịu. sản phẩm được bọc lại cẩn thận, có ghi bên ngoài là hàng dễ vỡ để mọi người giao hàng cẩn thận hơn. nhân viên giao hàng rất thân thiện.

Warning reasons:
- span #1 dài >= 15 tokens (16)
- COMP ratio > 60% (75.6%)

Current spans:
- #0 [18:63] COMP (11 tok): `lúc mình ngửi có mùi như mùi cồn rất khó chịu`
- #1 [97:163] COMP (16 tok): `có ghi bên ngoài là hàng dễ vỡ để mọi người giao hàng cẩn thận hơn`
- #2 [165:199] COMP (7 tok): `nhân viên giao hàng rất thân thiện`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_003594

Text: tôi đã chơi game này 3 tháng rồi và giờ các phiên bản gần đây tôi không thể chơi game quá một phút bởi vì vào game chưa làm được gì đã đứng màn hình và game ngừng hoạt động, tôi đã yêu cầu trợ giúp arena từ facebOk và họ nói phiên bản mới này sẽ khắc phục được, nhưng mà khi cập nhật xong tôi chỉ thấy... bài đánh giá đầ...

Warning reasons:
- span #0 dài >= 15 tokens (40)
- span #0 bắt đầu từ đầu text và dài > 8 tokens

Current spans:
- #0 [0:172] COMP (40 tok): `tôi đã chơi game này 3 tháng rồi và giờ các phiên bản gần đây tôi không thể chơi game quá một phút bởi vì vào game chưa làm được gì đã đứng màn hình và game ngừng hoạt động`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_003957

Text: giao hàng nhanh nhưng  cửa hàng  không đóng gói bưu kiện chuẩn không có lót  gì  may nhận hàng không bị sao.vấn đi này  cửa hàng  cần lưu ý nhé.oke về sản phẩm.

Warning reasons:
- span #0 dài >= 15 tokens (18)

Current spans:
- #0 [23:107] COMP (18 tok): `cửa hàng  không đóng gói bưu kiện chuẩn không có lót  gì  may nhận hàng không bị sao`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002487

Text: trò chơi này theo cảm nghĩ của tôi và những thứ tôi cảm nhận được dựa theo kiến thức của tôi và tôi đã áp dụng kiến thức của mình vào cái nhận xét lz này là trò chơi như C . chơi đeo hay  quả người cáo liên tục ngấy con mẹ nó rồi mong game sớm phá sản . tao tặng bọn làm game một câu cuối : game như C quảng cáo lz gì q....

Warning reasons:
- span #0 dài >= 15 tokens (17)

Current spans:
- #0 [254:319] COMP (17 tok): `tao tặng bọn làm game một câu cuối : game như C quảng cáo lz gì q`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_000978

Text: nhà phát hành nên làm lại tính năng bán nhân vật, hãy làm cho mọi nhân vật có thể bị bán đi để thu về vật phẩm chứ không giới hạn chỉ bán được nhân vật màu xanh lá. tính năng trên cần xem xét lại, phần còn lại của game thì rất hay, từ đồ hoạ đến hiệu ứng là rất tốt. tôi rất thích game này và chúc ga... bài đánh giá đầy...

Warning reasons:
- spans=[] nhưng cls_label=1

Current spans:
- _No spans_

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_001163

Text: sao em đặt 2 lần đều không đung mau đung  cỡ  sao em mang mong  cửa hàng  phan hoi dùm em

Warning reasons:
- span #0 dài >= 15 tokens (21)
- span #0 bắt đầu từ đầu text và dài > 8 tokens
- COMP ratio > 60% (100.0%)

Current spans:
- #0 [0:89] COMP (21 tok): `sao em đặt 2 lần đều không đung mau đung  cỡ  sao em mang mong  cửa hàng  phan hoi dùm em`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_001308

Text: hàng giao nhanh, chất lượng thì không như mong muốn dùng 2 lần vẫn chưa thấy có hiểu  quả 

Warning reasons:
- span #0 dài >= 15 tokens (16)
- COMP ratio > 60% (84.2%)

Current spans:
- #0 [17:89] COMP (16 tok): `chất lượng thì không như mong muốn dùng 2 lần vẫn chưa thấy có hiểu  quả`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002200

Text: đóng gói cẩn thận, tuy nhiên hơi thất vọng xíu khi mua hàng ở khung giờ 0-2h 11.11 đưọc tặng kèm sản phẩm khác nhưng đặt xong hỏi hãng báo hết sản phẩm tặng kèm

Warning reasons:
- COMP ratio > 60% (65.7%)

Current spans:
- #0 [23:79] COMP (13 tok): `nhiên hơi thất vọng xíu khi mua hàng ở khung giờ 0-2h 11`
- #1 [117:160] COMP (10 tok): `đặt xong hỏi hãng báo hết sản phẩm tặng kèm`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_003268

Text: thông tin đăng tải khi mua sẽ được tặng một lọ kem chống nắng mini  cỡ , tuy nhiên khi nhận hàng không có.

Warning reasons:
- span #0 dài >= 15 tokens (16)
- span #0 bắt đầu từ đầu text và dài > 8 tokens
- COMP ratio > 60% (91.7%)

Current spans:
- #0 [0:70] COMP (16 tok): `thông tin đăng tải khi mua sẽ được tặng một lọ kem chống nắng mini  cỡ`
- #1 [77:105] COMP (6 tok): `nhiên khi nhận hàng không có`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002036

Text: lừa đảo liên hệ fanpage không trả lời có dấu hiệu lừa tiền người chơi nếu đánh giá  được  0. 5star  là đánh rồi

Warning reasons:
- span #0 dài >= 15 tokens (20)
- span #0 bắt đầu từ đầu text và dài > 8 tokens
- COMP ratio > 60% (83.3%)

Current spans:
- #0 [0:91] COMP (20 tok): `lừa đảo liên hệ fanpage không trả lời có dấu hiệu lừa tiền người chơi nếu đánh giá  được  0`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_004334

Text: tôi đã nhận được tin nhắn kích hoạt bảo hành. nhưng tại sao kiểm tra trên trang chủ samsung + nhắn tin qua tổng đài 6060 lại báo là thông tin về điện thoại không đúng ạ

Warning reasons:
- span #0 dài >= 15 tokens (26)
- COMP ratio > 60% (70.3%)

Current spans:
- #0 [52:168] COMP (26 tok): `tại sao kiểm tra trên trang chủ samsung + nhắn tin qua tổng đài 6060 lại báo là thông tin về điện thoại không đúng ạ`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_003202

Text: đặt giao hàng hoả tốc ngày hôm trước, đến mãi 20h ngày hôm sau mới gọi giao hàng trong khi địa chỉ giao hàng ghi rất rõ là cơ quan làm việc. chất lượng dịch vụ rất tệ

Warning reasons:
- span #1 dài >= 15 tokens (24)
- COMP ratio > 60% (100.0%)

Current spans:
- #0 [0:36] COMP (8 tok): `đặt giao hàng hoả tốc ngày hôm trước`
- #1 [38:139] COMP (24 tok): `đến mãi 20h ngày hôm sau mới gọi giao hàng trong khi địa chỉ giao hàng ghi rất rõ là cơ quan làm việc`
- #2 [141:166] COMP (6 tok): `chất lượng dịch vụ rất tệ`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002466

Text: xung quanh tôi có nhiều tài xế đang chờ nhưng không hiểu sao lại chọn tài xế có vị trí cách tôi 10 dãy nhà. máy tôi không có chức năng  chất  với tài xế để nhắn vị trí đón. không hiện ảnh tài xế trong khi ứng dụng của tài xế thì có. nên có chức năng tích điểm như grab. chọn vị trí đón thì không hiện r... bài đánh giá đ...

Warning reasons:
- span #0 dài >= 15 tokens (15)

Current spans:
- #0 [108:171] COMP (15 tok): `máy tôi không có chức năng  chất  với tài xế để nhắn vị trí đón`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002543

Text: + chất lượng, giá cả hợp lý phù hợp với nhu cầu cơ bản. + dung lượng pin lớn xài rất thoải mái. có kèm củ sạc nhanh 15w. - hàng đóng gói không có lót mút hay nilon đệm khí, may mà điện thoại bên trong không vấn đề gì. - hàng có logo cam kết giao đúng hẹn và tôi sử dụng loại giao hàng hoả tốc thế nhưng đến cuối ngày nhậ...

Warning reasons:
- span #2 dài >= 15 tokens (26)

Current spans:
- #0 [123:171] COMP (11 tok): `hàng đóng gói không có lót mút hay nilon đệm khí`
- #1 [180:216] COMP (8 tok): `điện thoại bên trong không vấn đề gì`
- #2 [303:430] COMP (26 tok): `đến cuối ngày nhận thông báo hàng giao không thành công vì người nhận không nghe máy trong khi tôi chẳng nhận được cuộc gọi nào`
- #3 [542:582] COMP (9 tok): `đổ lỗi cho khách hàng không nghe máy nữa`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_002535

Text: không có quà tặng kèm như  quả người cáo. nhắn tin  cửa hàng  báo kiểm tra lại nhưng rồi im luôn. cách xử lý quá thiếu chuyên nghiệp! sản phẩm giao tới dính muối tôm, bốc mùi, kém vệ sinh.

Warning reasons:
- span #0 bắt đầu từ đầu text và dài > 8 tokens

Current spans:
- #0 [0:40] COMP (9 tok): `không có quà tặng kèm như  quả người cáo`
- #1 [98:132] COMP (7 tok): `cách xử lý quá thiếu chuyên nghiệp`
- #2 [167:174] COMP (2 tok): `bốc mùi`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:

### train_004217

Text: giao hang nhanh dung mẫu  cỡ  hơi rộng vẫn cho  5star  và sẽ ủng hộ tiếp

Warning reasons:
- span #0 dài >= 15 tokens (16)
- span #0 bắt đầu từ đầu text và dài > 8 tokens
- COMP ratio > 60% (100.0%)

Current spans:
- #0 [0:72] COMP (16 tok): `giao hang nhanh dung mẫu  cỡ  hơi rộng vẫn cho  5star  và sẽ ủng hộ tiếp`

Human action: KEEP / FIX / DROP
Suggested fixed spans:
Notes:


## C. NEEDS_REVIEW_LOW

_None_

## D. LIKELY_OK

- Count: `63`
- Details omitted by design.
