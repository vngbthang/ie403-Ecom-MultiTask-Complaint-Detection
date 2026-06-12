# Annotation Review - Sample Train 20

Manual checklist for reviewing AI-assisted complaint span annotations.

## 1. `train_000193`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đầm thun hơi mỏng nhưng mặc vào mát  cám ơn   cửa hàng 

**Spans:**

- #0 [0:17] `đầm thun hơi mỏng` label=`COMP`

**Reason:** Cụm 'đầm thun hơi mỏng' nêu trực tiếp vấn đề về chất lượng vải; phần 'mặc vào mát' và 'cám ơn cửa hàng' là trung tính/khen nên không chọn.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đầm | `B-COMP` |
| 1 | thun | `I-COMP` |
| 2 | hơi | `I-COMP` |
| 3 | mỏng | `I-COMP` |
| 4 | nhưng | `O` |
| 5 | mặc | `O` |
| 6 | vào | `O` |
| 7 | mát | `O` |
| 8 | cám | `O` |
| 9 | ơn | `O` |
| 10 | cửa | `O` |
| 11 | hàng | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 2. `train_000203`

- Domain: `app`
- Split: `train`

**Text gốc:**

> game hay. ít nhiệm vụ lấy đồ để cày hơn.. thực tiễn hơn.. không như mấy game khác nhiệm vụ cho đồ khác thì theo một khuôn khổ chán quá trời ra..

**Spans:**

- #0 [10:41] `ít nhiệm vụ lấy đồ để cày hơn..` label=`COMP`
- #1 [107:144] `theo một khuôn khổ chán quá trời ra..` label=`COMP`

**Reason:** Có hai ý phàn nàn: thiếu nhiệm vụ lấy đồ, và game khác bị chê là khuôn khổ nhàm chán; phần 'game hay' và 'thực tiễn hơn' là khen.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | game | `O` |
| 1 | hay. | `O` |
| 2 | ít | `B-COMP` |
| 3 | nhiệm | `I-COMP` |
| 4 | vụ | `I-COMP` |
| 5 | lấy | `I-COMP` |
| 6 | đồ | `I-COMP` |
| 7 | để | `I-COMP` |
| 8 | cày | `I-COMP` |
| 9 | hơn.. | `I-COMP` |
| 10 | thực | `O` |
| 11 | tiễn | `O` |
| 12 | hơn.. | `O` |
| 13 | không | `O` |
| 14 | như | `O` |
| 15 | mấy | `O` |
| 16 | game | `O` |
| 17 | khác | `O` |
| 18 | nhiệm | `O` |
| 19 | vụ | `O` |
| 20 | cho | `O` |
| 21 | đồ | `O` |
| 22 | khác | `O` |
| 23 | thì | `O` |
| 24 | theo | `B-COMP` |
| 25 | một | `I-COMP` |
| 26 | khuôn | `I-COMP` |
| 27 | khổ | `I-COMP` |
| 28 | chán | `I-COMP` |
| 29 | quá | `I-COMP` |
| 30 | trời | `I-COMP` |
| 31 | ra.. | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 3. `train_000221`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> thấy trả lời bình luận 1m5x 55 60 không vẫn vừa  cỡ  l, mình có 51 không mặc  cỡ  lồn vẫn chật! chán chả buồn nói 😒😒😒

**Spans:**

- #0 [86:95] `vẫn chật!` label=`COMP`
- #1 [96:113] `chán chả buồn nói` label=`COMP`

**Reason:** Cụm 'vẫn chật!' nêu trực tiếp vấn đề size không đúng; 'chán chả buồn nói' thể hiện sự thất vọng rõ rệt.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | thấy | `O` |
| 1 | trả | `O` |
| 2 | lời | `O` |
| 3 | bình | `O` |
| 4 | luận | `O` |
| 5 | 1m5x | `O` |
| 6 | 55 | `O` |
| 7 | 60 | `O` |
| 8 | không | `O` |
| 9 | vẫn | `O` |
| 10 | vừa | `O` |
| 11 | cỡ | `O` |
| 12 | l, | `O` |
| 13 | mình | `O` |
| 14 | có | `O` |
| 15 | 51 | `O` |
| 16 | không | `O` |
| 17 | mặc | `O` |
| 18 | cỡ | `O` |
| 19 | lồn | `O` |
| 20 | vẫn | `B-COMP` |
| 21 | chật! | `I-COMP` |
| 22 | chán | `B-COMP` |
| 23 | chả | `I-COMP` |
| 24 | buồn | `I-COMP` |
| 25 | nói | `I-COMP` |
| 26 | 😒😒😒 | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 4. `train_000249`

- Domain: `app`
- Split: `train`

**Text gốc:**

> facebOk làm ăn kiểu gì vậy, tài khoản cá nhân của tôi không vi phạm tiêu chuẩn cộng đồng gì cả, mà tại sao các ông lại vô hiệu hoá tài khoảng của tôi, tôi thấy facebOk làm ăn quá tệ!!, tài khoản của tôi là chính chủ tên thật có cả cmnd mà facebOk lại vô hiệu hoá tài khoản của tôi không có lý do g... bài đánh giá đầy đủ

**Spans:**

- #0 [0:26] `facebOk làm ăn kiểu gì vậy` label=`COMP`
- #1 [99:149] `tại sao các ông lại vô hiệu hoá tài khoảng của tôi` label=`COMP`
- #2 [151:183] `tôi thấy facebOk làm ăn quá tệ!!` label=`COMP`
- #3 [239:297] `facebOk lại vô hiệu hoá tài khoản của tôi không có lý do g` label=`COMP`

**Reason:** Review có nhiều khiếu nại: chất lượng dịch vụ tệ, vô hiệu hoá tài khoản không lý do, thể hiện bức xúc rõ ràng.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | facebOk | `B-COMP` |
| 1 | làm | `I-COMP` |
| 2 | ăn | `I-COMP` |
| 3 | kiểu | `I-COMP` |
| 4 | gì | `I-COMP` |
| 5 | vậy, | `I-COMP` |
| 6 | tài | `O` |
| 7 | khoản | `O` |
| 8 | cá | `O` |
| 9 | nhân | `O` |
| 10 | của | `O` |
| 11 | tôi | `O` |
| 12 | không | `O` |
| 13 | vi | `O` |
| 14 | phạm | `O` |
| 15 | tiêu | `O` |
| 16 | chuẩn | `O` |
| 17 | cộng | `O` |
| 18 | đồng | `O` |
| 19 | gì | `O` |
| 20 | cả, | `O` |
| 21 | mà | `O` |
| 22 | tại | `B-COMP` |
| 23 | sao | `I-COMP` |
| 24 | các | `I-COMP` |
| 25 | ông | `I-COMP` |
| 26 | lại | `I-COMP` |
| 27 | vô | `I-COMP` |
| 28 | hiệu | `I-COMP` |
| 29 | hoá | `I-COMP` |
| 30 | tài | `I-COMP` |
| 31 | khoảng | `I-COMP` |
| 32 | của | `I-COMP` |
| 33 | tôi, | `I-COMP` |
| 34 | tôi | `B-COMP` |
| 35 | thấy | `I-COMP` |
| 36 | facebOk | `I-COMP` |
| 37 | làm | `I-COMP` |
| 38 | ăn | `I-COMP` |
| 39 | quá | `I-COMP` |
| 40 | tệ!!, | `I-COMP` |
| 41 | tài | `O` |
| 42 | khoản | `O` |
| 43 | của | `O` |
| 44 | tôi | `O` |
| 45 | là | `O` |
| 46 | chính | `O` |
| 47 | chủ | `O` |
| 48 | tên | `O` |
| 49 | thật | `O` |
| 50 | có | `O` |
| 51 | cả | `O` |
| 52 | cmnd | `O` |
| 53 | mà | `O` |
| 54 | facebOk | `B-COMP` |
| 55 | lại | `I-COMP` |
| 56 | vô | `I-COMP` |
| 57 | hiệu | `I-COMP` |
| 58 | hoá | `I-COMP` |
| 59 | tài | `I-COMP` |
| 60 | khoản | `I-COMP` |
| 61 | của | `I-COMP` |
| 62 | tôi | `I-COMP` |
| 63 | không | `I-COMP` |
| 64 | có | `I-COMP` |
| 65 | lý | `I-COMP` |
| 66 | do | `I-COMP` |
| 67 | g... | `I-COMP` |
| 68 | bài | `O` |
| 69 | đánh | `O` |
| 70 | giá | `O` |
| 71 | đầy | `O` |
| 72 | đủ | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 5. `train_000645`

- Domain: `app`
- Split: `train`

**Text gốc:**

> hãy cho tính năng chưa mở là phần cho mọi người dùng những bộ đồ mình có để ghép thành những bộ đồ mới theo ý mọi người muốn đi , và trong ngôi nhà nhỏ có phố đi dạo để đến nhà những người bạn , có quán cà phê , quán ăn ,... và có thể thay đồ cho con chưa nhắn tin i trong ngôi nhà nhỏ nữa

**Spans:**

- None

**Reason:** Toàn bộ review là đề xuất tính năng mới, không có cụm khiếu nại/phàn nàn rõ ràng nào.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hãy | `O` |
| 1 | cho | `O` |
| 2 | tính | `O` |
| 3 | năng | `O` |
| 4 | chưa | `O` |
| 5 | mở | `O` |
| 6 | là | `O` |
| 7 | phần | `O` |
| 8 | cho | `O` |
| 9 | mọi | `O` |
| 10 | người | `O` |
| 11 | dùng | `O` |
| 12 | những | `O` |
| 13 | bộ | `O` |
| 14 | đồ | `O` |
| 15 | mình | `O` |
| 16 | có | `O` |
| 17 | để | `O` |
| 18 | ghép | `O` |
| 19 | thành | `O` |
| 20 | những | `O` |
| 21 | bộ | `O` |
| 22 | đồ | `O` |
| 23 | mới | `O` |
| 24 | theo | `O` |
| 25 | ý | `O` |
| 26 | mọi | `O` |
| 27 | người | `O` |
| 28 | muốn | `O` |
| 29 | đi | `O` |
| 30 | , | `O` |
| 31 | và | `O` |
| 32 | trong | `O` |
| 33 | ngôi | `O` |
| 34 | nhà | `O` |
| 35 | nhỏ | `O` |
| 36 | có | `O` |
| 37 | phố | `O` |
| 38 | đi | `O` |
| 39 | dạo | `O` |
| 40 | để | `O` |
| 41 | đến | `O` |
| 42 | nhà | `O` |
| 43 | những | `O` |
| 44 | người | `O` |
| 45 | bạn | `O` |
| 46 | , | `O` |
| 47 | có | `O` |
| 48 | quán | `O` |
| 49 | cà | `O` |
| 50 | phê | `O` |
| 51 | , | `O` |
| 52 | quán | `O` |
| 53 | ăn | `O` |
| 54 | ,... | `O` |
| 55 | và | `O` |
| 56 | có | `O` |
| 57 | thể | `O` |
| 58 | thay | `O` |
| 59 | đồ | `O` |
| 60 | cho | `O` |
| 61 | con | `O` |
| 62 | chưa | `O` |
| 63 | nhắn | `O` |
| 64 | tin | `O` |
| 65 | i | `O` |
| 66 | trong | `O` |
| 67 | ngôi | `O` |
| 68 | nhà | `O` |
| 69 | nhỏ | `O` |
| 70 | nữa | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 6. `train_000686`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> son muùi cực kì kinh khủng. mình xem mfg ngày apr2019. mình không biết dòng son này màu nào cũng mùi này hay chỉ có màu đỏ đất- thriLer nude là hôi rình. để xem mấy hôm nữa mùi có tản bớt không, chứ mùi nghe xong là ngất luôn.

**Spans:**

- #0 [0:26] `son muùi cực kì kinh khủng` label=`COMP`
- #1 [128:152] `thriLer nude là hôi rình` label=`COMP`
- #2 [199:225] `mùi nghe xong là ngất luôn` label=`COMP`

**Reason:** Có nhiều cụm phàn nàn về mùi son: mùi kinh khủng, màu cụ thể hôi rình, mùi đến mức ngất; đây đều là khiếu nại về chất lượng sản phẩm.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | son | `B-COMP` |
| 1 | muùi | `I-COMP` |
| 2 | cực | `I-COMP` |
| 3 | kì | `I-COMP` |
| 4 | kinh | `I-COMP` |
| 5 | khủng. | `I-COMP` |
| 6 | mình | `O` |
| 7 | xem | `O` |
| 8 | mfg | `O` |
| 9 | ngày | `O` |
| 10 | apr2019. | `O` |
| 11 | mình | `O` |
| 12 | không | `O` |
| 13 | biết | `O` |
| 14 | dòng | `O` |
| 15 | son | `O` |
| 16 | này | `O` |
| 17 | màu | `O` |
| 18 | nào | `O` |
| 19 | cũng | `O` |
| 20 | mùi | `O` |
| 21 | này | `O` |
| 22 | hay | `O` |
| 23 | chỉ | `O` |
| 24 | có | `O` |
| 25 | màu | `O` |
| 26 | đỏ | `O` |
| 27 | đất- | `O` |
| 28 | thriLer | `B-COMP` |
| 29 | nude | `I-COMP` |
| 30 | là | `I-COMP` |
| 31 | hôi | `I-COMP` |
| 32 | rình. | `I-COMP` |
| 33 | để | `O` |
| 34 | xem | `O` |
| 35 | mấy | `O` |
| 36 | hôm | `O` |
| 37 | nữa | `O` |
| 38 | mùi | `O` |
| 39 | có | `O` |
| 40 | tản | `O` |
| 41 | bớt | `O` |
| 42 | không, | `O` |
| 43 | chứ | `O` |
| 44 | mùi | `B-COMP` |
| 45 | nghe | `I-COMP` |
| 46 | xong | `I-COMP` |
| 47 | là | `I-COMP` |
| 48 | ngất | `I-COMP` |
| 49 | luôn. | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 7. `train_000748`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> mình mua hàng đã xem rất rõ là có tặng kèm quà hay không mà vẫn không có. mua rất nhiều lần và lần đầu tiên mình thất vọng đến vậy 😔

**Spans:**

- #0 [60:72] `vẫn không có` label=`COMP`
- #1 [108:130] `mình thất vọng đến vậy` label=`COMP`

**Reason:** Cụm 'vẫn không có' nêu vấn đề không nhận được quà tặng như cam kết; 'mình thất vọng đến vậy' thể hiện sự không hài lòng rõ ràng.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mình | `O` |
| 1 | mua | `O` |
| 2 | hàng | `O` |
| 3 | đã | `O` |
| 4 | xem | `O` |
| 5 | rất | `O` |
| 6 | rõ | `O` |
| 7 | là | `O` |
| 8 | có | `O` |
| 9 | tặng | `O` |
| 10 | kèm | `O` |
| 11 | quà | `O` |
| 12 | hay | `O` |
| 13 | không | `O` |
| 14 | mà | `O` |
| 15 | vẫn | `B-COMP` |
| 16 | không | `I-COMP` |
| 17 | có. | `I-COMP` |
| 18 | mua | `O` |
| 19 | rất | `O` |
| 20 | nhiều | `O` |
| 21 | lần | `O` |
| 22 | và | `O` |
| 23 | lần | `O` |
| 24 | đầu | `O` |
| 25 | tiên | `O` |
| 26 | mình | `B-COMP` |
| 27 | thất | `I-COMP` |
| 28 | vọng | `I-COMP` |
| 29 | đến | `I-COMP` |
| 30 | vậy | `I-COMP` |
| 31 | 😔 | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 8. `train_000828`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> màu trắng không gửi gửi màu xanh quá nhỏ luôn

**Spans:**

- #0 [0:19] `màu trắng không gửi` label=`COMP`
- #1 [20:45] `gửi màu xanh quá nhỏ luôn` label=`COMP`

**Reason:** Hai khiếu nại riêng: không gửi đúng màu đã đặt, và màu gửi kèm quá nhỏ.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | màu | `B-COMP` |
| 1 | trắng | `I-COMP` |
| 2 | không | `I-COMP` |
| 3 | gửi | `I-COMP` |
| 4 | gửi | `B-COMP` |
| 5 | màu | `I-COMP` |
| 6 | xanh | `I-COMP` |
| 7 | quá | `I-COMP` |
| 8 | nhỏ | `I-COMP` |
| 9 | luôn | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 9. `train_001059`

- Domain: `app`
- Split: `train`

**Text gốc:**

> mỗi lần cập nhật lại tốn mấy trăm mình dung lượng. lần này cũng vậy chả lẻ mỗi điện thoại chỉ tải  được  một game như thế này thôi sao? iG nên xem xét lại mà giảm bớt dung lượng game lại đi, còn không có thể iG sẽ giảm bớt nhiều người chơi đấy nhé! mỗi lần cập nhật đa phần không có tính năng nào hay ho ngoại... bài đánh giá đầy đủ

**Spans:**

- #0 [0:49] `mỗi lần cập nhật lại tốn mấy trăm mình dung lượng` label=`COMP`
- #1 [249:303] `mỗi lần cập nhật đa phần không có tính năng nào hay ho` label=`COMP`

**Reason:** Hai khiếu nại rõ ràng: cập nhật tốn quá nhiều dung lượng, và cập nhật không mang lại tính năng mới hữu ích.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mỗi | `B-COMP` |
| 1 | lần | `I-COMP` |
| 2 | cập | `I-COMP` |
| 3 | nhật | `I-COMP` |
| 4 | lại | `I-COMP` |
| 5 | tốn | `I-COMP` |
| 6 | mấy | `I-COMP` |
| 7 | trăm | `I-COMP` |
| 8 | mình | `I-COMP` |
| 9 | dung | `I-COMP` |
| 10 | lượng. | `I-COMP` |
| 11 | lần | `O` |
| 12 | này | `O` |
| 13 | cũng | `O` |
| 14 | vậy | `O` |
| 15 | chả | `O` |
| 16 | lẻ | `O` |
| 17 | mỗi | `O` |
| 18 | điện | `O` |
| 19 | thoại | `O` |
| 20 | chỉ | `O` |
| 21 | tải | `O` |
| 22 | được | `O` |
| 23 | một | `O` |
| 24 | game | `O` |
| 25 | như | `O` |
| 26 | thế | `O` |
| 27 | này | `O` |
| 28 | thôi | `O` |
| 29 | sao? | `O` |
| 30 | iG | `O` |
| 31 | nên | `O` |
| 32 | xem | `O` |
| 33 | xét | `O` |
| 34 | lại | `O` |
| 35 | mà | `O` |
| 36 | giảm | `O` |
| 37 | bớt | `O` |
| 38 | dung | `O` |
| 39 | lượng | `O` |
| 40 | game | `O` |
| 41 | lại | `O` |
| 42 | đi, | `O` |
| 43 | còn | `O` |
| 44 | không | `O` |
| 45 | có | `O` |
| 46 | thể | `O` |
| 47 | iG | `O` |
| 48 | sẽ | `O` |
| 49 | giảm | `O` |
| 50 | bớt | `O` |
| 51 | nhiều | `O` |
| 52 | người | `O` |
| 53 | chơi | `O` |
| 54 | đấy | `O` |
| 55 | nhé! | `O` |
| 56 | mỗi | `B-COMP` |
| 57 | lần | `I-COMP` |
| 58 | cập | `I-COMP` |
| 59 | nhật | `I-COMP` |
| 60 | đa | `I-COMP` |
| 61 | phần | `I-COMP` |
| 62 | không | `I-COMP` |
| 63 | có | `I-COMP` |
| 64 | tính | `I-COMP` |
| 65 | năng | `I-COMP` |
| 66 | nào | `I-COMP` |
| 67 | hay | `I-COMP` |
| 68 | ho | `I-COMP` |
| 69 | ngoại... | `O` |
| 70 | bài | `O` |
| 71 | đánh | `O` |
| 72 | giá | `O` |
| 73 | đầy | `O` |
| 74 | đủ | `O` |

**Heuristic warnings:**

- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 10. `train_001547`

- Domain: `app`
- Split: `train`

**Text gốc:**

> cứ nói to là được nhưng nó bảo là bạn nhắn tin o không nghe rõ

**Spans:**

- #0 [34:62] `bạn nhắn tin o không nghe rõ` label=`COMP`

**Reason:** Cụm này thể hiện vấn đề ứng dụng không nhận diện giọng nói rõ ràng dù người dùng nói to; phần trước là thông tin nền.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | cứ | `O` |
| 1 | nói | `O` |
| 2 | to | `O` |
| 3 | là | `O` |
| 4 | được | `O` |
| 5 | nhưng | `O` |
| 6 | nó | `O` |
| 7 | bảo | `O` |
| 8 | là | `O` |
| 9 | bạn | `B-COMP` |
| 10 | nhắn | `I-COMP` |
| 11 | tin | `I-COMP` |
| 12 | o | `I-COMP` |
| 13 | không | `I-COMP` |
| 14 | nghe | `I-COMP` |
| 15 | rõ | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 11. `train_001727`

- Domain: `app`
- Split: `train`

**Text gốc:**

> anh chị xem khắc phục lại lỗi hộ em với ạ, em tải xong vào thì bảo tải dữ liệu, vừa hiện tải xong lỗi, thử lại thì lại hiện tải xong lại lỗi tiếp,cứ như vậy dù em đã xoá đi tải lại 3 lần rồi ạ, em nghe nói aP này tốt nên tải dùng, mong ac fix nhanh để em trải nghiệm thử ạ, em xin cảm ơn ạ.

**Spans:**

- #0 [43:192] `em tải xong vào thì bảo tải dữ liệu, vừa hiện tải xong lỗi, thử lại thì lại hiện tải xong lại lỗi tiếp,cứ như vậy dù em đã xoá đi tải lại 3 lần rồi ạ` label=`COMP`

**Reason:** Cụm này mô tả chi tiết lỗi lặp lại khi tải dữ liệu dù đã xoá và cài lại nhiều lần; đây là khiếu nại kỹ thuật rõ ràng.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | anh | `O` |
| 1 | chị | `O` |
| 2 | xem | `O` |
| 3 | khắc | `O` |
| 4 | phục | `O` |
| 5 | lại | `O` |
| 6 | lỗi | `O` |
| 7 | hộ | `O` |
| 8 | em | `O` |
| 9 | với | `O` |
| 10 | ạ, | `O` |
| 11 | em | `B-COMP` |
| 12 | tải | `I-COMP` |
| 13 | xong | `I-COMP` |
| 14 | vào | `I-COMP` |
| 15 | thì | `I-COMP` |
| 16 | bảo | `I-COMP` |
| 17 | tải | `I-COMP` |
| 18 | dữ | `I-COMP` |
| 19 | liệu, | `I-COMP` |
| 20 | vừa | `I-COMP` |
| 21 | hiện | `I-COMP` |
| 22 | tải | `I-COMP` |
| 23 | xong | `I-COMP` |
| 24 | lỗi, | `I-COMP` |
| 25 | thử | `I-COMP` |
| 26 | lại | `I-COMP` |
| 27 | thì | `I-COMP` |
| 28 | lại | `I-COMP` |
| 29 | hiện | `I-COMP` |
| 30 | tải | `I-COMP` |
| 31 | xong | `I-COMP` |
| 32 | lại | `I-COMP` |
| 33 | lỗi | `I-COMP` |
| 34 | tiếp,cứ | `I-COMP` |
| 35 | như | `I-COMP` |
| 36 | vậy | `I-COMP` |
| 37 | dù | `I-COMP` |
| 38 | em | `I-COMP` |
| 39 | đã | `I-COMP` |
| 40 | xoá | `I-COMP` |
| 41 | đi | `I-COMP` |
| 42 | tải | `I-COMP` |
| 43 | lại | `I-COMP` |
| 44 | 3 | `I-COMP` |
| 45 | lần | `I-COMP` |
| 46 | rồi | `I-COMP` |
| 47 | ạ, | `I-COMP` |
| 48 | em | `O` |
| 49 | nghe | `O` |
| 50 | nói | `O` |
| 51 | aP | `O` |
| 52 | này | `O` |
| 53 | tốt | `O` |
| 54 | nên | `O` |
| 55 | tải | `O` |
| 56 | dùng, | `O` |
| 57 | mong | `O` |
| 58 | ac | `O` |
| 59 | fix | `O` |
| 60 | nhanh | `O` |
| 61 | để | `O` |
| 62 | em | `O` |
| 63 | trải | `O` |
| 64 | nghiệm | `O` |
| 65 | thử | `O` |
| 66 | ạ, | `O` |
| 67 | em | `O` |
| 68 | xin | `O` |
| 69 | cảm | `O` |
| 70 | ơn | `O` |
| 71 | ạ. | `O` |

**Heuristic warnings:**

- span #0 quá dài (37 tokens >= 15)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 12. `train_001758`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> kem nền thì ổn rồi mà quà thì quá tệ tặng cũng có tâm chút đi để màu này tặng cây son hồng bé rồi sao xài, thiệt hết nói nỗi 😑😑😑😑

**Spans:**

- #0 [22:36] `quà thì quá tệ` label=`COMP`
- #1 [62:105] `để màu này tặng cây son hồng bé rồi sao xài` label=`COMP`

**Reason:** Hai cụm phàn nàn về quà tặng: chất lượng quà tệ, và quà tặng kèm (son hồng bé) không phù hợp/không dùng được; phần 'kem nền thì ổn' là khen.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | kem | `O` |
| 1 | nền | `O` |
| 2 | thì | `O` |
| 3 | ổn | `O` |
| 4 | rồi | `O` |
| 5 | mà | `O` |
| 6 | quà | `B-COMP` |
| 7 | thì | `I-COMP` |
| 8 | quá | `I-COMP` |
| 9 | tệ | `I-COMP` |
| 10 | tặng | `O` |
| 11 | cũng | `O` |
| 12 | có | `O` |
| 13 | tâm | `O` |
| 14 | chút | `O` |
| 15 | đi | `O` |
| 16 | để | `B-COMP` |
| 17 | màu | `I-COMP` |
| 18 | này | `I-COMP` |
| 19 | tặng | `I-COMP` |
| 20 | cây | `I-COMP` |
| 21 | son | `I-COMP` |
| 22 | hồng | `I-COMP` |
| 23 | bé | `I-COMP` |
| 24 | rồi | `I-COMP` |
| 25 | sao | `I-COMP` |
| 26 | xài, | `I-COMP` |
| 27 | thiệt | `O` |
| 28 | hết | `O` |
| 29 | nói | `O` |
| 30 | nỗi | `O` |
| 31 | 😑😑😑😑 | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 13. `train_001836`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> vải không đẹp nút gài quá lỏng

**Spans:**

- #0 [0:13] `vải không đẹp` label=`COMP`
- #1 [14:30] `nút gài quá lỏng` label=`COMP`

**Reason:** Hai khiếu nại riêng biệt: chất liệu vải không đẹp và nút gài lỏng.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | vải | `B-COMP` |
| 1 | không | `I-COMP` |
| 2 | đẹp | `I-COMP` |
| 3 | nút | `B-COMP` |
| 4 | gài | `I-COMP` |
| 5 | quá | `I-COMP` |
| 6 | lỏng | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 14. `train_001926`

- Domain: `app`
- Split: `train`

**Text gốc:**

> aP có một số nhược điểm: thứ một là nhiều bài hạn chế, tìm không thấy. thứ 2 là việc aP tự động đăng nhập tài khoản zalo mỗi lần truy cập là rất phiền. cuối cùng là khi tôi dùng các ứng dụng chỉnh video như kinemaster, inshot, viva video ... muốn chèn bài hát đã tải ở zing về nhưng tìm không có, chỉ có ... bài đánh giá đầy đủ

**Spans:**

- #0 [36:69] `nhiều bài hạn chế, tìm không thấy` label=`COMP`
- #1 [85:150] `aP tự động đăng nhập tài khoản zalo mỗi lần truy cập là rất phiền` label=`COMP`
- #2 [242:295] `muốn chèn bài hát đã tải ở zing về nhưng tìm không có` label=`COMP`

**Reason:** Ba khiếu nại rõ ràng: nhiều bài bị hạn chế không tìm được, tự động đăng nhập zalo gây phiền, và bài đã tải không dùng được trong app chỉnh video.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | aP | `O` |
| 1 | có | `O` |
| 2 | một | `O` |
| 3 | số | `O` |
| 4 | nhược | `O` |
| 5 | điểm: | `O` |
| 6 | thứ | `O` |
| 7 | một | `O` |
| 8 | là | `O` |
| 9 | nhiều | `B-COMP` |
| 10 | bài | `I-COMP` |
| 11 | hạn | `I-COMP` |
| 12 | chế, | `I-COMP` |
| 13 | tìm | `I-COMP` |
| 14 | không | `I-COMP` |
| 15 | thấy. | `I-COMP` |
| 16 | thứ | `O` |
| 17 | 2 | `O` |
| 18 | là | `O` |
| 19 | việc | `O` |
| 20 | aP | `B-COMP` |
| 21 | tự | `I-COMP` |
| 22 | động | `I-COMP` |
| 23 | đăng | `I-COMP` |
| 24 | nhập | `I-COMP` |
| 25 | tài | `I-COMP` |
| 26 | khoản | `I-COMP` |
| 27 | zalo | `I-COMP` |
| 28 | mỗi | `I-COMP` |
| 29 | lần | `I-COMP` |
| 30 | truy | `I-COMP` |
| 31 | cập | `I-COMP` |
| 32 | là | `I-COMP` |
| 33 | rất | `I-COMP` |
| 34 | phiền. | `I-COMP` |
| 35 | cuối | `O` |
| 36 | cùng | `O` |
| 37 | là | `O` |
| 38 | khi | `O` |
| 39 | tôi | `O` |
| 40 | dùng | `O` |
| 41 | các | `O` |
| 42 | ứng | `O` |
| 43 | dụng | `O` |
| 44 | chỉnh | `O` |
| 45 | video | `O` |
| 46 | như | `O` |
| 47 | kinemaster, | `O` |
| 48 | inshot, | `O` |
| 49 | viva | `O` |
| 50 | video | `O` |
| 51 | ... | `O` |
| 52 | muốn | `B-COMP` |
| 53 | chèn | `I-COMP` |
| 54 | bài | `I-COMP` |
| 55 | hát | `I-COMP` |
| 56 | đã | `I-COMP` |
| 57 | tải | `I-COMP` |
| 58 | ở | `I-COMP` |
| 59 | zing | `I-COMP` |
| 60 | về | `I-COMP` |
| 61 | nhưng | `I-COMP` |
| 62 | tìm | `I-COMP` |
| 63 | không | `I-COMP` |
| 64 | có, | `I-COMP` |
| 65 | chỉ | `O` |
| 66 | có | `O` |
| 67 | ... | `O` |
| 68 | bài | `O` |
| 69 | đánh | `O` |
| 70 | giá | `O` |
| 71 | đầy | `O` |
| 72 | đủ | `O` |

**Heuristic warnings:**

- span #1 quá dài (15 tokens >= 15)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 15. `train_002144`

- Domain: `app`
- Split: `train`

**Text gốc:**

> game không hề cân bằng, nạp và không nạp quá khác biệt, hệ thống tìm trận không cân xứng lực chiến 5k gặp 10k 3 ván liền thì chơi gì? và ngoài việc nạp thẻ thì đá cường hoá lấy ở đâu ra??? hay là vng không quan tâm đến người chơi mà chỉ quan tâm đến tiền thu từ nạp thẻ? game hút máu à?

**Spans:**

- #0 [0:22] `game không hề cân bằng` label=`COMP`
- #1 [24:54] `nạp và không nạp quá khác biệt` label=`COMP`
- #2 [56:133] `hệ thống tìm trận không cân xứng lực chiến 5k gặp 10k 3 ván liền thì chơi gì?` label=`COMP`
- #3 [196:270] `vng không quan tâm đến người chơi mà chỉ quan tâm đến tiền thu từ nạp thẻ?` label=`COMP`
- #4 [271:286] `game hút máu à?` label=`COMP`

**Reason:** Nhiều khiếu nại: game mất cân bằng, chênh lệch nạp/không nạp quá lớn, hệ thống ghép trận không công bằng, nhà phát hành chỉ quan tâm đến tiền, và game bị chê là hút máu.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | game | `B-COMP` |
| 1 | không | `I-COMP` |
| 2 | hề | `I-COMP` |
| 3 | cân | `I-COMP` |
| 4 | bằng, | `I-COMP` |
| 5 | nạp | `B-COMP` |
| 6 | và | `I-COMP` |
| 7 | không | `I-COMP` |
| 8 | nạp | `I-COMP` |
| 9 | quá | `I-COMP` |
| 10 | khác | `I-COMP` |
| 11 | biệt, | `I-COMP` |
| 12 | hệ | `B-COMP` |
| 13 | thống | `I-COMP` |
| 14 | tìm | `I-COMP` |
| 15 | trận | `I-COMP` |
| 16 | không | `I-COMP` |
| 17 | cân | `I-COMP` |
| 18 | xứng | `I-COMP` |
| 19 | lực | `I-COMP` |
| 20 | chiến | `I-COMP` |
| 21 | 5k | `I-COMP` |
| 22 | gặp | `I-COMP` |
| 23 | 10k | `I-COMP` |
| 24 | 3 | `I-COMP` |
| 25 | ván | `I-COMP` |
| 26 | liền | `I-COMP` |
| 27 | thì | `I-COMP` |
| 28 | chơi | `I-COMP` |
| 29 | gì? | `I-COMP` |
| 30 | và | `O` |
| 31 | ngoài | `O` |
| 32 | việc | `O` |
| 33 | nạp | `O` |
| 34 | thẻ | `O` |
| 35 | thì | `O` |
| 36 | đá | `O` |
| 37 | cường | `O` |
| 38 | hoá | `O` |
| 39 | lấy | `O` |
| 40 | ở | `O` |
| 41 | đâu | `O` |
| 42 | ra??? | `O` |
| 43 | hay | `O` |
| 44 | là | `O` |
| 45 | vng | `B-COMP` |
| 46 | không | `I-COMP` |
| 47 | quan | `I-COMP` |
| 48 | tâm | `I-COMP` |
| 49 | đến | `I-COMP` |
| 50 | người | `I-COMP` |
| 51 | chơi | `I-COMP` |
| 52 | mà | `I-COMP` |
| 53 | chỉ | `I-COMP` |
| 54 | quan | `I-COMP` |
| 55 | tâm | `I-COMP` |
| 56 | đến | `I-COMP` |
| 57 | tiền | `I-COMP` |
| 58 | thu | `I-COMP` |
| 59 | từ | `I-COMP` |
| 60 | nạp | `I-COMP` |
| 61 | thẻ? | `I-COMP` |
| 62 | game | `B-COMP` |
| 63 | hút | `I-COMP` |
| 64 | máu | `I-COMP` |
| 65 | à? | `I-COMP` |

**Heuristic warnings:**

- span #2 quá dài (18 tokens >= 15)
- span #3 quá dài (17 tokens >= 15)
- record có nhiều hơn 4 spans (5 spans)
- tỉ lệ COMP token > 60% (77.3%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 16. `train_003263`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> vay bong đường chỉ

**Spans:**

- #0 [0:18] `vay bong đường chỉ` label=`COMP`

**Reason:** Toàn bộ cụm nêu lỗi sản phẩm (váy bị bong đường chỉ); đây là khiếu nại về chất lượng may.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | vay | `B-COMP` |
| 1 | bong | `I-COMP` |
| 2 | đường | `I-COMP` |
| 3 | chỉ | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 17. `train_003285`

- Domain: `app`
- Split: `train`

**Text gốc:**

> admin ơi. sao không thấy thông kê các thông số dịch bệnh liên quan đến nước anh vậy

**Spans:**

- #0 [10:83] `sao không thấy thông kê các thông số dịch bệnh liên quan đến nước anh vậy` label=`COMP`

**Reason:** Cụm này thể hiện khiếu nại về việc ứng dụng thiếu thông tin dịch bệnh của nước Anh.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | admin | `O` |
| 1 | ơi. | `O` |
| 2 | sao | `B-COMP` |
| 3 | không | `I-COMP` |
| 4 | thấy | `I-COMP` |
| 5 | thông | `I-COMP` |
| 6 | kê | `I-COMP` |
| 7 | các | `I-COMP` |
| 8 | thông | `I-COMP` |
| 9 | số | `I-COMP` |
| 10 | dịch | `I-COMP` |
| 11 | bệnh | `I-COMP` |
| 12 | liên | `I-COMP` |
| 13 | quan | `I-COMP` |
| 14 | đến | `I-COMP` |
| 15 | nước | `I-COMP` |
| 16 | anh | `I-COMP` |
| 17 | vậy | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (16 tokens >= 15)
- tỉ lệ COMP token > 60% (88.9%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 18. `train_003930`

- Domain: `app`
- Split: `train`

**Text gốc:**

> game chơi hay. mình xin góp ý một số ý kiến. game nên tách biệt giữa 2 nhóm người chơi đó là chơi giả lập trên pc chơi với nhau và chơi trên điện thoại với nhau để tránh tình trạng thao tác xử lí trên pc tốt hơn. và game nên bỏ hoàn toàn tự ngắm. như thế giúp game thật hơn. cảm ơn game...

**Spans:**

- #0 [181:211] `thao tác xử lí trên pc tốt hơn` label=`COMP`

**Reason:** Cụm này nêu bất cập người chơi PC có lợi thế thao tác hơn điện thoại; phần còn lại là góp ý tính năng và lời khen.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | game | `O` |
| 1 | chơi | `O` |
| 2 | hay. | `O` |
| 3 | mình | `O` |
| 4 | xin | `O` |
| 5 | góp | `O` |
| 6 | ý | `O` |
| 7 | một | `O` |
| 8 | số | `O` |
| 9 | ý | `O` |
| 10 | kiến. | `O` |
| 11 | game | `O` |
| 12 | nên | `O` |
| 13 | tách | `O` |
| 14 | biệt | `O` |
| 15 | giữa | `O` |
| 16 | 2 | `O` |
| 17 | nhóm | `O` |
| 18 | người | `O` |
| 19 | chơi | `O` |
| 20 | đó | `O` |
| 21 | là | `O` |
| 22 | chơi | `O` |
| 23 | giả | `O` |
| 24 | lập | `O` |
| 25 | trên | `O` |
| 26 | pc | `O` |
| 27 | chơi | `O` |
| 28 | với | `O` |
| 29 | nhau | `O` |
| 30 | và | `O` |
| 31 | chơi | `O` |
| 32 | trên | `O` |
| 33 | điện | `O` |
| 34 | thoại | `O` |
| 35 | với | `O` |
| 36 | nhau | `O` |
| 37 | để | `O` |
| 38 | tránh | `O` |
| 39 | tình | `O` |
| 40 | trạng | `O` |
| 41 | thao | `B-COMP` |
| 42 | tác | `I-COMP` |
| 43 | xử | `I-COMP` |
| 44 | lí | `I-COMP` |
| 45 | trên | `I-COMP` |
| 46 | pc | `I-COMP` |
| 47 | tốt | `I-COMP` |
| 48 | hơn. | `I-COMP` |
| 49 | và | `O` |
| 50 | game | `O` |
| 51 | nên | `O` |
| 52 | bỏ | `O` |
| 53 | hoàn | `O` |
| 54 | toàn | `O` |
| 55 | tự | `O` |
| 56 | ngắm. | `O` |
| 57 | như | `O` |
| 58 | thế | `O` |
| 59 | giúp | `O` |
| 60 | game | `O` |
| 61 | thật | `O` |
| 62 | hơn. | `O` |
| 63 | cảm | `O` |
| 64 | ơn | `O` |
| 65 | game... | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 19. `train_004260`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> quần chất đẹp, nhưng bị chật. mà  cửa hàng  có mỗi chuyện gửi địa chỉ để khách đổi hàng cũng không làm được.

**Spans:**

- #0 [21:28] `bị chật` label=`COMP`
- #1 [34:107] `cửa hàng  có mỗi chuyện gửi địa chỉ để khách đổi hàng cũng không làm được` label=`COMP`

**Reason:** Hai khiếu nại: quần bị chật, và cửa hàng không hỗ trợ đổi hàng dù chỉ cần gửi địa chỉ; phần 'quần chất đẹp' là khen.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | quần | `O` |
| 1 | chất | `O` |
| 2 | đẹp, | `O` |
| 3 | nhưng | `O` |
| 4 | bị | `B-COMP` |
| 5 | chật. | `I-COMP` |
| 6 | mà | `O` |
| 7 | cửa | `B-COMP` |
| 8 | hàng | `I-COMP` |
| 9 | có | `I-COMP` |
| 10 | mỗi | `I-COMP` |
| 11 | chuyện | `I-COMP` |
| 12 | gửi | `I-COMP` |
| 13 | địa | `I-COMP` |
| 14 | chỉ | `I-COMP` |
| 15 | để | `I-COMP` |
| 16 | khách | `I-COMP` |
| 17 | đổi | `I-COMP` |
| 18 | hàng | `I-COMP` |
| 19 | cũng | `I-COMP` |
| 20 | không | `I-COMP` |
| 21 | làm | `I-COMP` |
| 22 | được. | `I-COMP` |

**Heuristic warnings:**

- span #1 quá dài (16 tokens >= 15)
- tỉ lệ COMP token > 60% (78.3%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 20. `train_004263`

- Domain: `app`
- Split: `train`

**Text gốc:**

>  không  quay ngang duoc dien thoai.

**Spans:**

- #0 [1:34] `không  quay ngang duoc dien thoai` label=`COMP`

**Reason:** Toàn bộ cụm nêu lỗi ứng dụng không hỗ trợ xoay ngang màn hình điện thoại.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | không | `B-COMP` |
| 1 | quay | `I-COMP` |
| 2 | ngang | `I-COMP` |
| 3 | duoc | `I-COMP` |
| 4 | dien | `I-COMP` |
| 5 | thoai. | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---
