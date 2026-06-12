# Annotation Review - Sample Train 20

Manual checklist for reviewing AI-assisted complaint span annotations.

## 1. `train_000054`

- Domain: `app`
- Split: `train`

**Text gốc:**

> tôi rất thích game này nhưng càng lúc cấu hình game càng nặng, thật sự rất lag luôn, máy bên tôi lúc nào cũng trễ hơn bên đồng đội vài giây, có khi còn bị đứng hình hay cứ bị chạy giật lùi do kết nối mạng nữa. mong game có cách khắc phục chứ game càng lúc càng nặng thì người không có điều kiện đổi m... bài đánh giá đầy đủ

**Spans:**

- #0 [29:61] `càng lúc cấu hình game càng nặng` label=`COMP`
- #1 [71:83] `rất lag luôn` label=`COMP`
- #2 [110:139] `trễ hơn bên đồng đội vài giây` label=`COMP`
- #3 [152:164] `bị đứng hình` label=`COMP`
- #4 [175:188] `chạy giật lùi` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tôi | `O` |
| 1 | rất | `O` |
| 2 | thích | `O` |
| 3 | game | `O` |
| 4 | này | `O` |
| 5 | nhưng | `O` |
| 6 | càng | `B-COMP` |
| 7 | lúc | `I-COMP` |
| 8 | cấu | `I-COMP` |
| 9 | hình | `I-COMP` |
| 10 | game | `I-COMP` |
| 11 | càng | `I-COMP` |
| 12 | nặng, | `I-COMP` |
| 13 | thật | `O` |
| 14 | sự | `O` |
| 15 | rất | `B-COMP` |
| 16 | lag | `I-COMP` |
| 17 | luôn, | `I-COMP` |
| 18 | máy | `O` |
| 19 | bên | `O` |
| 20 | tôi | `O` |
| 21 | lúc | `O` |
| 22 | nào | `O` |
| 23 | cũng | `O` |
| 24 | trễ | `B-COMP` |
| 25 | hơn | `I-COMP` |
| 26 | bên | `I-COMP` |
| 27 | đồng | `I-COMP` |
| 28 | đội | `I-COMP` |
| 29 | vài | `I-COMP` |
| 30 | giây, | `I-COMP` |
| 31 | có | `O` |
| 32 | khi | `O` |
| 33 | còn | `O` |
| 34 | bị | `B-COMP` |
| 35 | đứng | `I-COMP` |
| 36 | hình | `I-COMP` |
| 37 | hay | `O` |
| 38 | cứ | `O` |
| 39 | bị | `O` |
| 40 | chạy | `B-COMP` |
| 41 | giật | `I-COMP` |
| 42 | lùi | `I-COMP` |
| 43 | do | `O` |
| 44 | kết | `O` |
| 45 | nối | `O` |
| 46 | mạng | `O` |
| 47 | nữa. | `O` |
| 48 | mong | `O` |
| 49 | game | `O` |
| 50 | có | `O` |
| 51 | cách | `O` |
| 52 | khắc | `O` |
| 53 | phục | `O` |
| 54 | chứ | `O` |
| 55 | game | `O` |
| 56 | càng | `O` |
| 57 | lúc | `O` |
| 58 | càng | `O` |
| 59 | nặng | `O` |
| 60 | thì | `O` |
| 61 | người | `O` |
| 62 | không | `O` |
| 63 | có | `O` |
| 64 | điều | `O` |
| 65 | kiện | `O` |
| 66 | đổi | `O` |
| 67 | m... | `O` |
| 68 | bài | `O` |
| 69 | đánh | `O` |
| 70 | giá | `O` |
| 71 | đầy | `O` |
| 72 | đủ | `O` |

**Heuristic warnings:**

- record có nhiều hơn 4 spans (5 spans)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 2. `train_000193`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đầm thun hơi mỏng nhưng mặc vào mát  cám ơn   cửa hàng 

**Spans:**

- #0 [9:17] `hơi mỏng` label=`COMP`

**Reason:** Cụm 'hơi mỏng' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đầm | `O` |
| 1 | thun | `O` |
| 2 | hơi | `B-COMP` |
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

## 3. `train_000203`

- Domain: `app`
- Split: `train`

**Text gốc:**

> game hay. ít nhiệm vụ lấy đồ để cày hơn.. thực tiễn hơn.. không như mấy game khác nhiệm vụ cho đồ khác thì theo một khuôn khổ chán quá trời ra..

**Spans:**

- #0 [10:35] `ít nhiệm vụ lấy đồ để cày` label=`COMP`
- #1 [107:139] `theo một khuôn khổ chán quá trời` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

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
| 9 | hơn.. | `O` |
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
| 31 | ra.. | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 4. `train_000221`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> thấy trả lời bình luận 1m5x 55 60 không vẫn vừa  cỡ  l, mình có 51 không mặc  cỡ  lồn vẫn chật! chán chả buồn nói 😒😒😒

**Spans:**

- #0 [86:95] `vẫn chật!` label=`COMP`
- #1 [96:113] `chán chả buồn nói` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

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

## 5. `train_000249`

- Domain: `app`
- Split: `train`

**Text gốc:**

> facebOk làm ăn kiểu gì vậy, tài khoản cá nhân của tôi không vi phạm tiêu chuẩn cộng đồng gì cả, mà tại sao các ông lại vô hiệu hoá tài khoảng của tôi, tôi thấy facebOk làm ăn quá tệ!!, tài khoản của tôi là chính chủ tên thật có cả cmnd mà facebOk lại vô hiệu hoá tài khoản của tôi không có lý do g... bài đánh giá đầy đủ

**Spans:**

- #0 [119:149] `vô hiệu hoá tài khoảng của tôi` label=`COMP`
- #1 [160:183] `facebOk làm ăn quá tệ!!` label=`COMP`
- #2 [251:295] `vô hiệu hoá tài khoản của tôi không có lý do` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | facebOk | `O` |
| 1 | làm | `O` |
| 2 | ăn | `O` |
| 3 | kiểu | `O` |
| 4 | gì | `O` |
| 5 | vậy, | `O` |
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
| 22 | tại | `O` |
| 23 | sao | `O` |
| 24 | các | `O` |
| 25 | ông | `O` |
| 26 | lại | `O` |
| 27 | vô | `B-COMP` |
| 28 | hiệu | `I-COMP` |
| 29 | hoá | `I-COMP` |
| 30 | tài | `I-COMP` |
| 31 | khoảng | `I-COMP` |
| 32 | của | `I-COMP` |
| 33 | tôi, | `I-COMP` |
| 34 | tôi | `O` |
| 35 | thấy | `O` |
| 36 | facebOk | `B-COMP` |
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
| 54 | facebOk | `O` |
| 55 | lại | `O` |
| 56 | vô | `B-COMP` |
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
| 67 | g... | `O` |
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

## 6. `train_000252`

- Domain: `app`
- Split: `train`

**Text gốc:**

> game thi cux hay . nhung ma tôi thich parkout . nhung tôi tai map parkout sao no không  được  . game tôi tai = 200k đi đéo mẹ . admin xem rồi sua lai loi game  gì đăng @@

**Spans:**

- #0 [81:92] `không  được` label=`COMP`
- #1 [142:158] `sua lai loi game` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | game | `O` |
| 1 | thi | `O` |
| 2 | cux | `O` |
| 3 | hay | `O` |
| 4 | . | `O` |
| 5 | nhung | `O` |
| 6 | ma | `O` |
| 7 | tôi | `O` |
| 8 | thich | `O` |
| 9 | parkout | `O` |
| 10 | . | `O` |
| 11 | nhung | `O` |
| 12 | tôi | `O` |
| 13 | tai | `O` |
| 14 | map | `O` |
| 15 | parkout | `O` |
| 16 | sao | `O` |
| 17 | no | `O` |
| 18 | không | `B-COMP` |
| 19 | được | `I-COMP` |
| 20 | . | `O` |
| 21 | game | `O` |
| 22 | tôi | `O` |
| 23 | tai | `O` |
| 24 | = | `O` |
| 25 | 200k | `O` |
| 26 | đi | `O` |
| 27 | đéo | `O` |
| 28 | mẹ | `O` |
| 29 | . | `O` |
| 30 | admin | `O` |
| 31 | xem | `O` |
| 32 | rồi | `O` |
| 33 | sua | `B-COMP` |
| 34 | lai | `I-COMP` |
| 35 | loi | `I-COMP` |
| 36 | game | `I-COMP` |
| 37 | gì | `O` |
| 38 | đăng | `O` |
| 39 | @@ | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 7. `train_000329`

- Domain: `app`
- Split: `train`

**Text gốc:**

> tôi không biết tại vì sao . tự nhiên tài khoản của tôi mất hết biệt hiệu và màu sắc cũng như mất cả cảm xúc. tôi cài đặt lại thì không có phần biệu tượng cảm xúc màu và biệt hiệu để thay đổi. tôi xoá mes đi tải lại cũng không được. mong admin xem xét lại chứ cư như này thì không  được  đâu.

**Spans:**

- #0 [55:107] `mất hết biệt hiệu và màu sắc cũng như mất cả cảm xúc` label=`COMP`
- #1 [129:190] `không có phần biệu tượng cảm xúc màu và biệt hiệu để thay đổi` label=`COMP`
- #2 [274:290] `không  được  đâu` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tôi | `O` |
| 1 | không | `O` |
| 2 | biết | `O` |
| 3 | tại | `O` |
| 4 | vì | `O` |
| 5 | sao | `O` |
| 6 | . | `O` |
| 7 | tự | `O` |
| 8 | nhiên | `O` |
| 9 | tài | `O` |
| 10 | khoản | `O` |
| 11 | của | `O` |
| 12 | tôi | `O` |
| 13 | mất | `B-COMP` |
| 14 | hết | `I-COMP` |
| 15 | biệt | `I-COMP` |
| 16 | hiệu | `I-COMP` |
| 17 | và | `I-COMP` |
| 18 | màu | `I-COMP` |
| 19 | sắc | `I-COMP` |
| 20 | cũng | `I-COMP` |
| 21 | như | `I-COMP` |
| 22 | mất | `I-COMP` |
| 23 | cả | `I-COMP` |
| 24 | cảm | `I-COMP` |
| 25 | xúc. | `I-COMP` |
| 26 | tôi | `O` |
| 27 | cài | `O` |
| 28 | đặt | `O` |
| 29 | lại | `O` |
| 30 | thì | `O` |
| 31 | không | `B-COMP` |
| 32 | có | `I-COMP` |
| 33 | phần | `I-COMP` |
| 34 | biệu | `I-COMP` |
| 35 | tượng | `I-COMP` |
| 36 | cảm | `I-COMP` |
| 37 | xúc | `I-COMP` |
| 38 | màu | `I-COMP` |
| 39 | và | `I-COMP` |
| 40 | biệt | `I-COMP` |
| 41 | hiệu | `I-COMP` |
| 42 | để | `I-COMP` |
| 43 | thay | `I-COMP` |
| 44 | đổi. | `I-COMP` |
| 45 | tôi | `O` |
| 46 | xoá | `O` |
| 47 | mes | `O` |
| 48 | đi | `O` |
| 49 | tải | `O` |
| 50 | lại | `O` |
| 51 | cũng | `O` |
| 52 | không | `O` |
| 53 | được. | `O` |
| 54 | mong | `O` |
| 55 | admin | `O` |
| 56 | xem | `O` |
| 57 | xét | `O` |
| 58 | lại | `O` |
| 59 | chứ | `O` |
| 60 | cư | `O` |
| 61 | như | `O` |
| 62 | này | `O` |
| 63 | thì | `O` |
| 64 | không | `B-COMP` |
| 65 | được | `I-COMP` |
| 66 | đâu. | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 8. `train_000346`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> điện thoại đẹp nhưng sạc nhanh 15w kiểu gì mà mắc ghét, chậm như rùa. có 13% pin mà báo sạc 39 phút nữa mới đầy. chẳng bù với vsmart live sạc trong vòng một tiếng bảo đảm100% pin.

**Spans:**

- #0 [46:54] `mắc ghét` label=`COMP`
- #1 [56:68] `chậm như rùa` label=`COMP`
- #2 [92:111] `39 phút nữa mới đầy` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | điện | `O` |
| 1 | thoại | `O` |
| 2 | đẹp | `O` |
| 3 | nhưng | `O` |
| 4 | sạc | `O` |
| 5 | nhanh | `O` |
| 6 | 15w | `O` |
| 7 | kiểu | `O` |
| 8 | gì | `O` |
| 9 | mà | `O` |
| 10 | mắc | `B-COMP` |
| 11 | ghét, | `I-COMP` |
| 12 | chậm | `B-COMP` |
| 13 | như | `I-COMP` |
| 14 | rùa. | `I-COMP` |
| 15 | có | `O` |
| 16 | 13% | `O` |
| 17 | pin | `O` |
| 18 | mà | `O` |
| 19 | báo | `O` |
| 20 | sạc | `O` |
| 21 | 39 | `B-COMP` |
| 22 | phút | `I-COMP` |
| 23 | nữa | `I-COMP` |
| 24 | mới | `I-COMP` |
| 25 | đầy. | `I-COMP` |
| 26 | chẳng | `O` |
| 27 | bù | `O` |
| 28 | với | `O` |
| 29 | vsmart | `O` |
| 30 | live | `O` |
| 31 | sạc | `O` |
| 32 | trong | `O` |
| 33 | vòng | `O` |
| 34 | một | `O` |
| 35 | tiếng | `O` |
| 36 | bảo | `O` |
| 37 | đảm100% | `O` |
| 38 | pin. | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 9. `train_000352`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

>  cửa hàng  nói  cỡ  mình .nặng từ 56 không trở xuống mà mình 50 không mặt không vừa

**Spans:**

- #0 [74:83] `không vừa` label=`COMP`

**Reason:** Cụm 'không vừa' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | cửa | `O` |
| 1 | hàng | `O` |
| 2 | nói | `O` |
| 3 | cỡ | `O` |
| 4 | mình | `O` |
| 5 | .nặng | `O` |
| 6 | từ | `O` |
| 7 | 56 | `O` |
| 8 | không | `O` |
| 9 | trở | `O` |
| 10 | xuống | `O` |
| 11 | mà | `O` |
| 12 | mình | `O` |
| 13 | 50 | `O` |
| 14 | không | `O` |
| 15 | mặt | `O` |
| 16 | không | `B-COMP` |
| 17 | vừa | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 10. `train_000417`

- Domain: `app`
- Split: `train`

**Text gốc:**

> rất tệ. lừa đảo tiền. không có nút huỷ đơn hàng. nếu bạn mò mò mà ấn nhầm thì xác định là phải trả tiền trong nước mắt thôi. phí giao hàng đã cao rồi mà còn tính thêm cả phí dịch vụ  positive  toàn kiếm cách moi móc tiền. nói chung là mình xoá aP.

**Spans:**

- #0 [8:20] `lừa đảo tiền` label=`COMP`
- #1 [22:47] `không có nút huỷ đơn hàng` label=`COMP`
- #2 [157:181] `tính thêm cả phí dịch vụ` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | rất | `O` |
| 1 | tệ. | `O` |
| 2 | lừa | `B-COMP` |
| 3 | đảo | `I-COMP` |
| 4 | tiền. | `I-COMP` |
| 5 | không | `B-COMP` |
| 6 | có | `I-COMP` |
| 7 | nút | `I-COMP` |
| 8 | huỷ | `I-COMP` |
| 9 | đơn | `I-COMP` |
| 10 | hàng. | `I-COMP` |
| 11 | nếu | `O` |
| 12 | bạn | `O` |
| 13 | mò | `O` |
| 14 | mò | `O` |
| 15 | mà | `O` |
| 16 | ấn | `O` |
| 17 | nhầm | `O` |
| 18 | thì | `O` |
| 19 | xác | `O` |
| 20 | định | `O` |
| 21 | là | `O` |
| 22 | phải | `O` |
| 23 | trả | `O` |
| 24 | tiền | `O` |
| 25 | trong | `O` |
| 26 | nước | `O` |
| 27 | mắt | `O` |
| 28 | thôi. | `O` |
| 29 | phí | `O` |
| 30 | giao | `O` |
| 31 | hàng | `O` |
| 32 | đã | `O` |
| 33 | cao | `O` |
| 34 | rồi | `O` |
| 35 | mà | `O` |
| 36 | còn | `O` |
| 37 | tính | `B-COMP` |
| 38 | thêm | `I-COMP` |
| 39 | cả | `I-COMP` |
| 40 | phí | `I-COMP` |
| 41 | dịch | `I-COMP` |
| 42 | vụ | `I-COMP` |
| 43 | positive | `O` |
| 44 | toàn | `O` |
| 45 | kiếm | `O` |
| 46 | cách | `O` |
| 47 | moi | `O` |
| 48 | móc | `O` |
| 49 | tiền. | `O` |
| 50 | nói | `O` |
| 51 | chung | `O` |
| 52 | là | `O` |
| 53 | mình | `O` |
| 54 | xoá | `O` |
| 55 | aP. | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 11. `train_000497`

- Domain: `app`
- Split: `train`

**Text gốc:**

> tôi một người xài 5 năm facebook lite rất là thích. rồi càng ngày càng tệ. mỗi lần bị đăng xuất hay lí do gì không biết vào ứng dụng rất là lâu. có khi một ngày trời vẫn không vào được cứ một chấm đang tải trong khi wifi rất mạnh. tốc độ thì vẫn vậy cải thiện đâu chả thấy, càng tệ thêm.

**Spans:**

- #0 [120:143] `vào ứng dụng rất là lâu` label=`COMP`
- #1 [152:184] `một ngày trời vẫn không vào được` label=`COMP`
- #2 [274:286] `càng tệ thêm` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tôi | `O` |
| 1 | một | `O` |
| 2 | người | `O` |
| 3 | xài | `O` |
| 4 | 5 | `O` |
| 5 | năm | `O` |
| 6 | facebook | `O` |
| 7 | lite | `O` |
| 8 | rất | `O` |
| 9 | là | `O` |
| 10 | thích. | `O` |
| 11 | rồi | `O` |
| 12 | càng | `O` |
| 13 | ngày | `O` |
| 14 | càng | `O` |
| 15 | tệ. | `O` |
| 16 | mỗi | `O` |
| 17 | lần | `O` |
| 18 | bị | `O` |
| 19 | đăng | `O` |
| 20 | xuất | `O` |
| 21 | hay | `O` |
| 22 | lí | `O` |
| 23 | do | `O` |
| 24 | gì | `O` |
| 25 | không | `O` |
| 26 | biết | `O` |
| 27 | vào | `B-COMP` |
| 28 | ứng | `I-COMP` |
| 29 | dụng | `I-COMP` |
| 30 | rất | `I-COMP` |
| 31 | là | `I-COMP` |
| 32 | lâu. | `I-COMP` |
| 33 | có | `O` |
| 34 | khi | `O` |
| 35 | một | `B-COMP` |
| 36 | ngày | `I-COMP` |
| 37 | trời | `I-COMP` |
| 38 | vẫn | `I-COMP` |
| 39 | không | `I-COMP` |
| 40 | vào | `I-COMP` |
| 41 | được | `I-COMP` |
| 42 | cứ | `O` |
| 43 | một | `O` |
| 44 | chấm | `O` |
| 45 | đang | `O` |
| 46 | tải | `O` |
| 47 | trong | `O` |
| 48 | khi | `O` |
| 49 | wifi | `O` |
| 50 | rất | `O` |
| 51 | mạnh. | `O` |
| 52 | tốc | `O` |
| 53 | độ | `O` |
| 54 | thì | `O` |
| 55 | vẫn | `O` |
| 56 | vậy | `O` |
| 57 | cải | `O` |
| 58 | thiện | `O` |
| 59 | đâu | `O` |
| 60 | chả | `O` |
| 61 | thấy, | `O` |
| 62 | càng | `B-COMP` |
| 63 | tệ | `I-COMP` |
| 64 | thêm. | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 12. `train_000516`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đàm đẹp vãi hơi mõng

**Spans:**

- #0 [12:20] `hơi mõng` label=`COMP`

**Reason:** Cụm 'hơi mõng' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đàm | `O` |
| 1 | đẹp | `O` |
| 2 | vãi | `O` |
| 3 | hơi | `B-COMP` |
| 4 | mõng | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 13. `train_000532`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

>  chất  vải quá tệ. day lưng quần thì  không  phải nói nó nhỏ tí mỏng te.

**Spans:**

- #0 [11:17] `quá tệ` label=`COMP`
- #1 [64:71] `mỏng te` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | chất | `O` |
| 1 | vải | `O` |
| 2 | quá | `B-COMP` |
| 3 | tệ. | `I-COMP` |
| 4 | day | `O` |
| 5 | lưng | `O` |
| 6 | quần | `O` |
| 7 | thì | `O` |
| 8 | không | `O` |
| 9 | phải | `O` |
| 10 | nói | `O` |
| 11 | nó | `O` |
| 12 | nhỏ | `O` |
| 13 | tí | `O` |
| 14 | mỏng | `B-COMP` |
| 15 | te. | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 14. `train_000589`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> hàng không đúng mẫu

**Spans:**

- #0 [5:19] `không đúng mẫu` label=`COMP`

**Reason:** Cụm 'không đúng mẫu' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hàng | `O` |
| 1 | không | `B-COMP` |
| 2 | đúng | `I-COMP` |
| 3 | mẫu | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (75.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 15. `train_000595`

- Domain: `app`
- Split: `train`

**Text gốc:**

> mình chỉ cho 4 sao thôi vì game rất không công bằng người ta hơn 2,3 leve không nói gì ở đây hơn 5,6... leve vẫn cho đánh , xong còn người khác nạp vào tài khoản vip hơn đồ ngon hơn súng khoẻ người ta cày cực khổ mới được súng ngon , chỉ cần nạp là có súng vip rồi! thế game mới mất cân bằng mong nhà phát... bài đánh giá đầy đủ

**Spans:**

- #0 [32:51] `rất không công bằng` label=`COMP`
- #1 [144:191] `nạp vào tài khoản vip hơn đồ ngon hơn súng khoẻ` label=`COMP`
- #2 [234:264] `chỉ cần nạp là có súng vip rồi` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mình | `O` |
| 1 | chỉ | `O` |
| 2 | cho | `O` |
| 3 | 4 | `O` |
| 4 | sao | `O` |
| 5 | thôi | `O` |
| 6 | vì | `O` |
| 7 | game | `O` |
| 8 | rất | `B-COMP` |
| 9 | không | `I-COMP` |
| 10 | công | `I-COMP` |
| 11 | bằng | `I-COMP` |
| 12 | người | `O` |
| 13 | ta | `O` |
| 14 | hơn | `O` |
| 15 | 2,3 | `O` |
| 16 | leve | `O` |
| 17 | không | `O` |
| 18 | nói | `O` |
| 19 | gì | `O` |
| 20 | ở | `O` |
| 21 | đây | `O` |
| 22 | hơn | `O` |
| 23 | 5,6... | `O` |
| 24 | leve | `O` |
| 25 | vẫn | `O` |
| 26 | cho | `O` |
| 27 | đánh | `O` |
| 28 | , | `O` |
| 29 | xong | `O` |
| 30 | còn | `O` |
| 31 | người | `O` |
| 32 | khác | `O` |
| 33 | nạp | `B-COMP` |
| 34 | vào | `I-COMP` |
| 35 | tài | `I-COMP` |
| 36 | khoản | `I-COMP` |
| 37 | vip | `I-COMP` |
| 38 | hơn | `I-COMP` |
| 39 | đồ | `I-COMP` |
| 40 | ngon | `I-COMP` |
| 41 | hơn | `I-COMP` |
| 42 | súng | `I-COMP` |
| 43 | khoẻ | `I-COMP` |
| 44 | người | `O` |
| 45 | ta | `O` |
| 46 | cày | `O` |
| 47 | cực | `O` |
| 48 | khổ | `O` |
| 49 | mới | `O` |
| 50 | được | `O` |
| 51 | súng | `O` |
| 52 | ngon | `O` |
| 53 | , | `O` |
| 54 | chỉ | `B-COMP` |
| 55 | cần | `I-COMP` |
| 56 | nạp | `I-COMP` |
| 57 | là | `I-COMP` |
| 58 | có | `I-COMP` |
| 59 | súng | `I-COMP` |
| 60 | vip | `I-COMP` |
| 61 | rồi! | `I-COMP` |
| 62 | thế | `O` |
| 63 | game | `O` |
| 64 | mới | `O` |
| 65 | mất | `O` |
| 66 | cân | `O` |
| 67 | bằng | `O` |
| 68 | mong | `O` |
| 69 | nhà | `O` |
| 70 | phát... | `O` |
| 71 | bài | `O` |
| 72 | đánh | `O` |
| 73 | giá | `O` |
| 74 | đầy | `O` |
| 75 | đủ | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 16. `train_000645`

- Domain: `app`
- Split: `train`

**Text gốc:**

> hãy cho tính năng chưa mở là phần cho mọi người dùng những bộ đồ mình có để ghép thành những bộ đồ mới theo ý mọi người muốn đi , và trong ngôi nhà nhỏ có phố đi dạo để đến nhà những người bạn , có quán cà phê , quán ăn ,... và có thể thay đồ cho con chưa nhắn tin i trong ngôi nhà nhỏ nữa

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý, khen, hoặc mô tả trung tính.

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

## 17. `train_000666`

- Domain: `app`
- Split: `train`

**Text gốc:**

> cho em hỏi em đăng nhập vào xong em bị lỗi gì đó em xoá em tải lại em đăng nhập vào lại thì nó bảo là tại khoản này đã liên kết chỗ khác là sao ạ em phải làm sao

**Spans:**

- #0 [102:136] `tại khoản này đã liên kết chỗ khác` label=`COMP`

**Reason:** Cụm 'tại khoản này đã liên kết chỗ khác' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | cho | `O` |
| 1 | em | `O` |
| 2 | hỏi | `O` |
| 3 | em | `O` |
| 4 | đăng | `O` |
| 5 | nhập | `O` |
| 6 | vào | `O` |
| 7 | xong | `O` |
| 8 | em | `O` |
| 9 | bị | `O` |
| 10 | lỗi | `O` |
| 11 | gì | `O` |
| 12 | đó | `O` |
| 13 | em | `O` |
| 14 | xoá | `O` |
| 15 | em | `O` |
| 16 | tải | `O` |
| 17 | lại | `O` |
| 18 | em | `O` |
| 19 | đăng | `O` |
| 20 | nhập | `O` |
| 21 | vào | `O` |
| 22 | lại | `O` |
| 23 | thì | `O` |
| 24 | nó | `O` |
| 25 | bảo | `O` |
| 26 | là | `O` |
| 27 | tại | `B-COMP` |
| 28 | khoản | `I-COMP` |
| 29 | này | `I-COMP` |
| 30 | đã | `I-COMP` |
| 31 | liên | `I-COMP` |
| 32 | kết | `I-COMP` |
| 33 | chỗ | `I-COMP` |
| 34 | khác | `I-COMP` |
| 35 | là | `O` |
| 36 | sao | `O` |
| 37 | ạ | `O` |
| 38 | em | `O` |
| 39 | phải | `O` |
| 40 | làm | `O` |
| 41 | sao | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 18. `train_000679`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> du đep nhung rat tiec la nho qua.chi mot nguoi đi la vua

**Spans:**

- #0 [25:32] `nho qua` label=`COMP`

**Reason:** Cụm 'nho qua' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | du | `O` |
| 1 | đep | `O` |
| 2 | nhung | `O` |
| 3 | rat | `O` |
| 4 | tiec | `O` |
| 5 | la | `O` |
| 6 | nho | `B-COMP` |
| 7 | qua.chi | `I-COMP` |
| 8 | mot | `O` |
| 9 | nguoi | `O` |
| 10 | đi | `O` |
| 11 | la | `O` |
| 12 | vua | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 19. `train_000686`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> son muùi cực kì kinh khủng. mình xem mfg ngày apr2019. mình không biết dòng son này màu nào cũng mùi này hay chỉ có màu đỏ đất- thriLer nude là hôi rình. để xem mấy hôm nữa mùi có tản bớt không, chứ mùi nghe xong là ngất luôn.

**Spans:**

- #0 [4:26] `muùi cực kì kinh khủng` label=`COMP`
- #1 [141:152] `là hôi rình` label=`COMP`
- #2 [199:225] `mùi nghe xong là ngất luôn` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | son | `O` |
| 1 | muùi | `B-COMP` |
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
| 28 | thriLer | `O` |
| 29 | nude | `O` |
| 30 | là | `B-COMP` |
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

## 20. `train_000709`

- Domain: `app`
- Split: `train`

**Text gốc:**

> game rất hay và vui. có thể kết bạn được. có thể chơi trò chuyện và nhắn tin với nhau. nhưng tôi muốn có nhiều skin mua bằng đậu mini hoặc từ các mảnh họp lại được bộ bộ để cho hững người không nạp được tiền vẫn có skin đẹp để mặc cho nhìn nó phong cách một xíu. chứ tôi thấy lâu lâu tự nhiên có ngườ... bài đánh giá đầy đủ

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý, khen, hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | game | `O` |
| 1 | rất | `O` |
| 2 | hay | `O` |
| 3 | và | `O` |
| 4 | vui. | `O` |
| 5 | có | `O` |
| 6 | thể | `O` |
| 7 | kết | `O` |
| 8 | bạn | `O` |
| 9 | được. | `O` |
| 10 | có | `O` |
| 11 | thể | `O` |
| 12 | chơi | `O` |
| 13 | trò | `O` |
| 14 | chuyện | `O` |
| 15 | và | `O` |
| 16 | nhắn | `O` |
| 17 | tin | `O` |
| 18 | với | `O` |
| 19 | nhau. | `O` |
| 20 | nhưng | `O` |
| 21 | tôi | `O` |
| 22 | muốn | `O` |
| 23 | có | `O` |
| 24 | nhiều | `O` |
| 25 | skin | `O` |
| 26 | mua | `O` |
| 27 | bằng | `O` |
| 28 | đậu | `O` |
| 29 | mini | `O` |
| 30 | hoặc | `O` |
| 31 | từ | `O` |
| 32 | các | `O` |
| 33 | mảnh | `O` |
| 34 | họp | `O` |
| 35 | lại | `O` |
| 36 | được | `O` |
| 37 | bộ | `O` |
| 38 | bộ | `O` |
| 39 | để | `O` |
| 40 | cho | `O` |
| 41 | hững | `O` |
| 42 | người | `O` |
| 43 | không | `O` |
| 44 | nạp | `O` |
| 45 | được | `O` |
| 46 | tiền | `O` |
| 47 | vẫn | `O` |
| 48 | có | `O` |
| 49 | skin | `O` |
| 50 | đẹp | `O` |
| 51 | để | `O` |
| 52 | mặc | `O` |
| 53 | cho | `O` |
| 54 | nhìn | `O` |
| 55 | nó | `O` |
| 56 | phong | `O` |
| 57 | cách | `O` |
| 58 | một | `O` |
| 59 | xíu. | `O` |
| 60 | chứ | `O` |
| 61 | tôi | `O` |
| 62 | thấy | `O` |
| 63 | lâu | `O` |
| 64 | lâu | `O` |
| 65 | tự | `O` |
| 66 | nhiên | `O` |
| 67 | có | `O` |
| 68 | ngườ... | `O` |
| 69 | bài | `O` |
| 70 | đánh | `O` |
| 71 | giá | `O` |
| 72 | đầy | `O` |
| 73 | đủ | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 21. `train_000740`

- Domain: `app`
- Split: `train`

**Text gốc:**

> tại sao khi bị mất số điện thoại mà người khác vào được zalo của mình? mong zalo chỉnh sửa bảo mật giúp mọi người được yên tâm khi bị mất số điện thoại nhưng zalo vẫn được bảo vệ tuyệt đối, để người khác không lạm dụng tài khoản riêng tư của mình vào những mục đích tiêu cực. chân thành cảm ơn.

**Spans:**

- #0 [36:69] `người khác vào được zalo của mình` label=`COMP`

**Reason:** Cụm 'người khác vào được zalo của mình' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tại | `O` |
| 1 | sao | `O` |
| 2 | khi | `O` |
| 3 | bị | `O` |
| 4 | mất | `O` |
| 5 | số | `O` |
| 6 | điện | `O` |
| 7 | thoại | `O` |
| 8 | mà | `O` |
| 9 | người | `B-COMP` |
| 10 | khác | `I-COMP` |
| 11 | vào | `I-COMP` |
| 12 | được | `I-COMP` |
| 13 | zalo | `I-COMP` |
| 14 | của | `I-COMP` |
| 15 | mình? | `I-COMP` |
| 16 | mong | `O` |
| 17 | zalo | `O` |
| 18 | chỉnh | `O` |
| 19 | sửa | `O` |
| 20 | bảo | `O` |
| 21 | mật | `O` |
| 22 | giúp | `O` |
| 23 | mọi | `O` |
| 24 | người | `O` |
| 25 | được | `O` |
| 26 | yên | `O` |
| 27 | tâm | `O` |
| 28 | khi | `O` |
| 29 | bị | `O` |
| 30 | mất | `O` |
| 31 | số | `O` |
| 32 | điện | `O` |
| 33 | thoại | `O` |
| 34 | nhưng | `O` |
| 35 | zalo | `O` |
| 36 | vẫn | `O` |
| 37 | được | `O` |
| 38 | bảo | `O` |
| 39 | vệ | `O` |
| 40 | tuyệt | `O` |
| 41 | đối, | `O` |
| 42 | để | `O` |
| 43 | người | `O` |
| 44 | khác | `O` |
| 45 | không | `O` |
| 46 | lạm | `O` |
| 47 | dụng | `O` |
| 48 | tài | `O` |
| 49 | khoản | `O` |
| 50 | riêng | `O` |
| 51 | tư | `O` |
| 52 | của | `O` |
| 53 | mình | `O` |
| 54 | vào | `O` |
| 55 | những | `O` |
| 56 | mục | `O` |
| 57 | đích | `O` |
| 58 | tiêu | `O` |
| 59 | cực. | `O` |
| 60 | chân | `O` |
| 61 | thành | `O` |
| 62 | cảm | `O` |
| 63 | ơn. | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 22. `train_000747`

- Domain: `app`
- Split: `train`

**Text gốc:**

> không có khống chế phần tải về nội dung khoá học. bé cứ bấm vào tải về quá trời làm máy đơ luôn. cả phần chơi sticker nữa. hov gì  thì không học cứ bấm vào phần chọn sticker nghịch hoài.

**Spans:**

- #0 [0:30] `không có khống chế phần tải về` label=`COMP`
- #1 [84:95] `máy đơ luôn` label=`COMP`
- #2 [156:185] `phần chọn sticker nghịch hoài` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | không | `B-COMP` |
| 1 | có | `I-COMP` |
| 2 | khống | `I-COMP` |
| 3 | chế | `I-COMP` |
| 4 | phần | `I-COMP` |
| 5 | tải | `I-COMP` |
| 6 | về | `I-COMP` |
| 7 | nội | `O` |
| 8 | dung | `O` |
| 9 | khoá | `O` |
| 10 | học. | `O` |
| 11 | bé | `O` |
| 12 | cứ | `O` |
| 13 | bấm | `O` |
| 14 | vào | `O` |
| 15 | tải | `O` |
| 16 | về | `O` |
| 17 | quá | `O` |
| 18 | trời | `O` |
| 19 | làm | `O` |
| 20 | máy | `B-COMP` |
| 21 | đơ | `I-COMP` |
| 22 | luôn. | `I-COMP` |
| 23 | cả | `O` |
| 24 | phần | `O` |
| 25 | chơi | `O` |
| 26 | sticker | `O` |
| 27 | nữa. | `O` |
| 28 | hov | `O` |
| 29 | gì | `O` |
| 30 | thì | `O` |
| 31 | không | `O` |
| 32 | học | `O` |
| 33 | cứ | `O` |
| 34 | bấm | `O` |
| 35 | vào | `O` |
| 36 | phần | `B-COMP` |
| 37 | chọn | `I-COMP` |
| 38 | sticker | `I-COMP` |
| 39 | nghịch | `I-COMP` |
| 40 | hoài. | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 23. `train_000748`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> mình mua hàng đã xem rất rõ là có tặng kèm quà hay không mà vẫn không có. mua rất nhiều lần và lần đầu tiên mình thất vọng đến vậy 😔

**Spans:**

- #0 [60:72] `vẫn không có` label=`COMP`
- #1 [113:130] `thất vọng đến vậy` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

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
| 26 | mình | `O` |
| 27 | thất | `B-COMP` |
| 28 | vọng | `I-COMP` |
| 29 | đến | `I-COMP` |
| 30 | vậy | `I-COMP` |
| 31 | 😔 | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 24. `train_000828`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> màu trắng không gửi gửi màu xanh quá nhỏ luôn

**Spans:**

- #0 [0:19] `màu trắng không gửi` label=`COMP`
- #1 [24:45] `màu xanh quá nhỏ luôn` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | màu | `B-COMP` |
| 1 | trắng | `I-COMP` |
| 2 | không | `I-COMP` |
| 3 | gửi | `I-COMP` |
| 4 | gửi | `O` |
| 5 | màu | `B-COMP` |
| 6 | xanh | `I-COMP` |
| 7 | quá | `I-COMP` |
| 8 | nhỏ | `I-COMP` |
| 9 | luôn | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (90.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 25. `train_000953`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> rất đẹp nhưng vải hơi mỏng vậy cũng được rồi

**Spans:**

- #0 [14:26] `vải hơi mỏng` label=`COMP`

**Reason:** Cụm 'vải hơi mỏng' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | rất | `O` |
| 1 | đẹp | `O` |
| 2 | nhưng | `O` |
| 3 | vải | `B-COMP` |
| 4 | hơi | `I-COMP` |
| 5 | mỏng | `I-COMP` |
| 6 | vậy | `O` |
| 7 | cũng | `O` |
| 8 | được | `O` |
| 9 | rồi | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 26. `train_001052`

- Domain: `app`
- Split: `train`

**Text gốc:**

> gửi trả hàng vì lí do sai mẫu,  cửa hàng  không nhận trả về cho khách, khách lại phải chịu thêm tiền vận chuyển gửi trả, chẳng lẽ lazada không bảo vệ được quyền lợi của người tiêu dùng?  quả người cáo thì nói được đổi trả nếu sai mẫu, bây giờ thì vậy? ban  quả nó lí không có biện pháp xử lí những việc như thế này... bài đánh giá đầy đủ

**Spans:**

- #0 [42:69] `không nhận trả về cho khách` label=`COMP`
- #1 [81:119] `phải chịu thêm tiền vận chuyển gửi trả` label=`COMP`
- #2 [137:184] `không bảo vệ được quyền lợi của người tiêu dùng` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | gửi | `O` |
| 1 | trả | `O` |
| 2 | hàng | `O` |
| 3 | vì | `O` |
| 4 | lí | `O` |
| 5 | do | `O` |
| 6 | sai | `O` |
| 7 | mẫu, | `O` |
| 8 | cửa | `O` |
| 9 | hàng | `O` |
| 10 | không | `B-COMP` |
| 11 | nhận | `I-COMP` |
| 12 | trả | `I-COMP` |
| 13 | về | `I-COMP` |
| 14 | cho | `I-COMP` |
| 15 | khách, | `I-COMP` |
| 16 | khách | `O` |
| 17 | lại | `O` |
| 18 | phải | `B-COMP` |
| 19 | chịu | `I-COMP` |
| 20 | thêm | `I-COMP` |
| 21 | tiền | `I-COMP` |
| 22 | vận | `I-COMP` |
| 23 | chuyển | `I-COMP` |
| 24 | gửi | `I-COMP` |
| 25 | trả, | `I-COMP` |
| 26 | chẳng | `O` |
| 27 | lẽ | `O` |
| 28 | lazada | `O` |
| 29 | không | `B-COMP` |
| 30 | bảo | `I-COMP` |
| 31 | vệ | `I-COMP` |
| 32 | được | `I-COMP` |
| 33 | quyền | `I-COMP` |
| 34 | lợi | `I-COMP` |
| 35 | của | `I-COMP` |
| 36 | người | `I-COMP` |
| 37 | tiêu | `I-COMP` |
| 38 | dùng? | `I-COMP` |
| 39 | quả | `O` |
| 40 | người | `O` |
| 41 | cáo | `O` |
| 42 | thì | `O` |
| 43 | nói | `O` |
| 44 | được | `O` |
| 45 | đổi | `O` |
| 46 | trả | `O` |
| 47 | nếu | `O` |
| 48 | sai | `O` |
| 49 | mẫu, | `O` |
| 50 | bây | `O` |
| 51 | giờ | `O` |
| 52 | thì | `O` |
| 53 | vậy? | `O` |
| 54 | ban | `O` |
| 55 | quả | `O` |
| 56 | nó | `O` |
| 57 | lí | `O` |
| 58 | không | `O` |
| 59 | có | `O` |
| 60 | biện | `O` |
| 61 | pháp | `O` |
| 62 | xử | `O` |
| 63 | lí | `O` |
| 64 | những | `O` |
| 65 | việc | `O` |
| 66 | như | `O` |
| 67 | thế | `O` |
| 68 | này... | `O` |
| 69 | bài | `O` |
| 70 | đánh | `O` |
| 71 | giá | `O` |
| 72 | đầy | `O` |
| 73 | đủ | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 27. `train_001059`

- Domain: `app`
- Split: `train`

**Text gốc:**

> mỗi lần cập nhật lại tốn mấy trăm mình dung lượng. lần này cũng vậy chả lẻ mỗi điện thoại chỉ tải  được  một game như thế này thôi sao? iG nên xem xét lại mà giảm bớt dung lượng game lại đi, còn không có thể iG sẽ giảm bớt nhiều người chơi đấy nhé! mỗi lần cập nhật đa phần không có tính năng nào hay ho ngoại... bài đánh giá đầy đủ

**Spans:**

- #0 [8:49] `cập nhật lại tốn mấy trăm mình dung lượng` label=`COMP`
- #1 [274:303] `không có tính năng nào hay ho` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mỗi | `O` |
| 1 | lần | `O` |
| 2 | cập | `B-COMP` |
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
| 56 | mỗi | `O` |
| 57 | lần | `O` |
| 58 | cập | `O` |
| 59 | nhật | `O` |
| 60 | đa | `O` |
| 61 | phần | `O` |
| 62 | không | `B-COMP` |
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

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 28. `train_001080`

- Domain: `app`
- Split: `train`

**Text gốc:**

> trò chơi rõ chán nạp tiền nhiều thì giết được một guild dễ dàng thế thì đưa mấy đứa nạp tiền vô lên thẳng đi  positive ) luyện làm gì cho mệt. trò chơi thì ưu tiên những người chơi nạp tiền là vì lợi ích nph là đúng nhưng làm nó quá khác biệt với số còn lại thì lại làm mất đi tính hay.

**Spans:**

- #0 [0:16] `trò chơi rõ chán` label=`COMP`
- #1 [17:63] `nạp tiền nhiều thì giết được một guild dễ dàng` label=`COMP`
- #2 [229:257] `quá khác biệt với số còn lại` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | trò | `B-COMP` |
| 1 | chơi | `I-COMP` |
| 2 | rõ | `I-COMP` |
| 3 | chán | `I-COMP` |
| 4 | nạp | `B-COMP` |
| 5 | tiền | `I-COMP` |
| 6 | nhiều | `I-COMP` |
| 7 | thì | `I-COMP` |
| 8 | giết | `I-COMP` |
| 9 | được | `I-COMP` |
| 10 | một | `I-COMP` |
| 11 | guild | `I-COMP` |
| 12 | dễ | `I-COMP` |
| 13 | dàng | `I-COMP` |
| 14 | thế | `O` |
| 15 | thì | `O` |
| 16 | đưa | `O` |
| 17 | mấy | `O` |
| 18 | đứa | `O` |
| 19 | nạp | `O` |
| 20 | tiền | `O` |
| 21 | vô | `O` |
| 22 | lên | `O` |
| 23 | thẳng | `O` |
| 24 | đi | `O` |
| 25 | positive | `O` |
| 26 | ) | `O` |
| 27 | luyện | `O` |
| 28 | làm | `O` |
| 29 | gì | `O` |
| 30 | cho | `O` |
| 31 | mệt. | `O` |
| 32 | trò | `O` |
| 33 | chơi | `O` |
| 34 | thì | `O` |
| 35 | ưu | `O` |
| 36 | tiên | `O` |
| 37 | những | `O` |
| 38 | người | `O` |
| 39 | chơi | `O` |
| 40 | nạp | `O` |
| 41 | tiền | `O` |
| 42 | là | `O` |
| 43 | vì | `O` |
| 44 | lợi | `O` |
| 45 | ích | `O` |
| 46 | nph | `O` |
| 47 | là | `O` |
| 48 | đúng | `O` |
| 49 | nhưng | `O` |
| 50 | làm | `O` |
| 51 | nó | `O` |
| 52 | quá | `B-COMP` |
| 53 | khác | `I-COMP` |
| 54 | biệt | `I-COMP` |
| 55 | với | `I-COMP` |
| 56 | số | `I-COMP` |
| 57 | còn | `I-COMP` |
| 58 | lại | `I-COMP` |
| 59 | thì | `O` |
| 60 | lại | `O` |
| 61 | làm | `O` |
| 62 | mất | `O` |
| 63 | đi | `O` |
| 64 | tính | `O` |
| 65 | hay. | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 29. `train_001184`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> lưng rộng mà ống lại hơi ngắn

**Spans:**

- #0 [0:9] `lưng rộng` label=`COMP`
- #1 [13:29] `ống lại hơi ngắn` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | lưng | `B-COMP` |
| 1 | rộng | `I-COMP` |
| 2 | mà | `O` |
| 3 | ống | `B-COMP` |
| 4 | lại | `I-COMP` |
| 5 | hơi | `I-COMP` |
| 6 | ngắn | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (85.7%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 30. `train_001216`

- Domain: `app`
- Split: `train`

**Text gốc:**

> không hiểu ứng dụng hoạt động kiểu gì. tại sao lúc trưa tôi vẫn còn vào được, nhưng chiều thì twiTer bảo nhập mật khẩu, số điên thoại, và tên, tôi đều làm đúng hết nhưng cuối cùng tôi vẫn không thể đăng nhập. thật tồi tệ

**Spans:**

- #0 [188:207] `không thể đăng nhập` label=`COMP`
- #1 [209:220] `thật tồi tệ` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | không | `O` |
| 1 | hiểu | `O` |
| 2 | ứng | `O` |
| 3 | dụng | `O` |
| 4 | hoạt | `O` |
| 5 | động | `O` |
| 6 | kiểu | `O` |
| 7 | gì. | `O` |
| 8 | tại | `O` |
| 9 | sao | `O` |
| 10 | lúc | `O` |
| 11 | trưa | `O` |
| 12 | tôi | `O` |
| 13 | vẫn | `O` |
| 14 | còn | `O` |
| 15 | vào | `O` |
| 16 | được, | `O` |
| 17 | nhưng | `O` |
| 18 | chiều | `O` |
| 19 | thì | `O` |
| 20 | twiTer | `O` |
| 21 | bảo | `O` |
| 22 | nhập | `O` |
| 23 | mật | `O` |
| 24 | khẩu, | `O` |
| 25 | số | `O` |
| 26 | điên | `O` |
| 27 | thoại, | `O` |
| 28 | và | `O` |
| 29 | tên, | `O` |
| 30 | tôi | `O` |
| 31 | đều | `O` |
| 32 | làm | `O` |
| 33 | đúng | `O` |
| 34 | hết | `O` |
| 35 | nhưng | `O` |
| 36 | cuối | `O` |
| 37 | cùng | `O` |
| 38 | tôi | `O` |
| 39 | vẫn | `O` |
| 40 | không | `B-COMP` |
| 41 | thể | `I-COMP` |
| 42 | đăng | `I-COMP` |
| 43 | nhập. | `I-COMP` |
| 44 | thật | `B-COMP` |
| 45 | tồi | `I-COMP` |
| 46 | tệ | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 31. `train_001236`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

>  cửa hàng  giao  cỡ  lồn nho hon m... buon

**Spans:**

- #0 [25:32] `nho hon` label=`COMP`

**Reason:** Cụm 'nho hon' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | cửa | `O` |
| 1 | hàng | `O` |
| 2 | giao | `O` |
| 3 | cỡ | `O` |
| 4 | lồn | `O` |
| 5 | nho | `B-COMP` |
| 6 | hon | `I-COMP` |
| 7 | m... | `O` |
| 8 | buon | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 32. `train_001241`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đầm đẹp nhưng mà cái bông ở trong hình là màu giống với màu áo nhưng mà cái của mình cái bông màu đận hơn nhưng không sao đầm vẫn đẹp cám ơn  cửa hàng 

**Spans:**

- #0 [85:105] `cái bông màu đận hơn` label=`COMP`

**Reason:** Cụm 'cái bông màu đận hơn' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đầm | `O` |
| 1 | đẹp | `O` |
| 2 | nhưng | `O` |
| 3 | mà | `O` |
| 4 | cái | `O` |
| 5 | bông | `O` |
| 6 | ở | `O` |
| 7 | trong | `O` |
| 8 | hình | `O` |
| 9 | là | `O` |
| 10 | màu | `O` |
| 11 | giống | `O` |
| 12 | với | `O` |
| 13 | màu | `O` |
| 14 | áo | `O` |
| 15 | nhưng | `O` |
| 16 | mà | `O` |
| 17 | cái | `O` |
| 18 | của | `O` |
| 19 | mình | `O` |
| 20 | cái | `B-COMP` |
| 21 | bông | `I-COMP` |
| 22 | màu | `I-COMP` |
| 23 | đận | `I-COMP` |
| 24 | hơn | `I-COMP` |
| 25 | nhưng | `O` |
| 26 | không | `O` |
| 27 | sao | `O` |
| 28 | đầm | `O` |
| 29 | vẫn | `O` |
| 30 | đẹp | `O` |
| 31 | cám | `O` |
| 32 | ơn | `O` |
| 33 | cửa | `O` |
| 34 | hàng | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 33. `train_001295`

- Domain: `app`
- Split: `train`

**Text gốc:**

> tài khoản đang sử dụng tự nhiên bị hết phiên đăng nhập. xong rồi đăng nhập lại bị mật khẩu sai, ấn quên mật khẩu thì lại thấy email của người lạ, còn không sử dụng được số điện thoại để đăng nhập mà lấy lại mật khẩu. admin xem lại xem nào.

**Spans:**

- #0 [35:54] `hết phiên đăng nhập` label=`COMP`
- #1 [82:94] `mật khẩu sai` label=`COMP`
- #2 [126:144] `email của người lạ` label=`COMP`
- #3 [150:182] `không sử dụng được số điện thoại` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tài | `O` |
| 1 | khoản | `O` |
| 2 | đang | `O` |
| 3 | sử | `O` |
| 4 | dụng | `O` |
| 5 | tự | `O` |
| 6 | nhiên | `O` |
| 7 | bị | `O` |
| 8 | hết | `B-COMP` |
| 9 | phiên | `I-COMP` |
| 10 | đăng | `I-COMP` |
| 11 | nhập. | `I-COMP` |
| 12 | xong | `O` |
| 13 | rồi | `O` |
| 14 | đăng | `O` |
| 15 | nhập | `O` |
| 16 | lại | `O` |
| 17 | bị | `O` |
| 18 | mật | `B-COMP` |
| 19 | khẩu | `I-COMP` |
| 20 | sai, | `I-COMP` |
| 21 | ấn | `O` |
| 22 | quên | `O` |
| 23 | mật | `O` |
| 24 | khẩu | `O` |
| 25 | thì | `O` |
| 26 | lại | `O` |
| 27 | thấy | `O` |
| 28 | email | `B-COMP` |
| 29 | của | `I-COMP` |
| 30 | người | `I-COMP` |
| 31 | lạ, | `I-COMP` |
| 32 | còn | `O` |
| 33 | không | `B-COMP` |
| 34 | sử | `I-COMP` |
| 35 | dụng | `I-COMP` |
| 36 | được | `I-COMP` |
| 37 | số | `I-COMP` |
| 38 | điện | `I-COMP` |
| 39 | thoại | `I-COMP` |
| 40 | để | `O` |
| 41 | đăng | `O` |
| 42 | nhập | `O` |
| 43 | mà | `O` |
| 44 | lấy | `O` |
| 45 | lại | `O` |
| 46 | mật | `O` |
| 47 | khẩu. | `O` |
| 48 | admin | `O` |
| 49 | xem | `O` |
| 50 | lại | `O` |
| 51 | xem | `O` |
| 52 | nào. | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 34. `train_001478`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đồ rất đẹp nha mọi người giống hình lắm luôn giá rẻ nhưng giặc ra màu mặc một lần đổ lông rồi  nagative  giao hàng lâu nói chung giá vậy là rất được sẽ ủng hộ lần sao

**Spans:**

- #0 [58:69] `giặc ra màu` label=`COMP`
- #1 [82:93] `đổ lông rồi` label=`COMP`
- #2 [105:118] `giao hàng lâu` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đồ | `O` |
| 1 | rất | `O` |
| 2 | đẹp | `O` |
| 3 | nha | `O` |
| 4 | mọi | `O` |
| 5 | người | `O` |
| 6 | giống | `O` |
| 7 | hình | `O` |
| 8 | lắm | `O` |
| 9 | luôn | `O` |
| 10 | giá | `O` |
| 11 | rẻ | `O` |
| 12 | nhưng | `O` |
| 13 | giặc | `B-COMP` |
| 14 | ra | `I-COMP` |
| 15 | màu | `I-COMP` |
| 16 | mặc | `O` |
| 17 | một | `O` |
| 18 | lần | `O` |
| 19 | đổ | `B-COMP` |
| 20 | lông | `I-COMP` |
| 21 | rồi | `I-COMP` |
| 22 | nagative | `O` |
| 23 | giao | `B-COMP` |
| 24 | hàng | `I-COMP` |
| 25 | lâu | `I-COMP` |
| 26 | nói | `O` |
| 27 | chung | `O` |
| 28 | giá | `O` |
| 29 | vậy | `O` |
| 30 | là | `O` |
| 31 | rất | `O` |
| 32 | được | `O` |
| 33 | sẽ | `O` |
| 34 | ủng | `O` |
| 35 | hộ | `O` |
| 36 | lần | `O` |
| 37 | sao | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 35. `train_001547`

- Domain: `app`
- Split: `train`

**Text gốc:**

> cứ nói to là được nhưng nó bảo là bạn nhắn tin o không nghe rõ

**Spans:**

- #0 [49:62] `không nghe rõ` label=`COMP`

**Reason:** Cụm 'không nghe rõ' nêu trực tiếp vấn đề chính.

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
| 9 | bạn | `O` |
| 10 | nhắn | `O` |
| 11 | tin | `O` |
| 12 | o | `O` |
| 13 | không | `B-COMP` |
| 14 | nghe | `I-COMP` |
| 15 | rõ | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 36. `train_001648`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> theo đơn là phải được tặng thêm một tuýp cùng loại. nhưng đến khi giao mở hàng ra lại không thấy hàng tặng đâu cả. rất cần lời giải thích

**Spans:**

- #0 [86:113] `không thấy hàng tặng đâu cả` label=`COMP`

**Reason:** Cụm 'không thấy hàng tặng đâu cả' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | theo | `O` |
| 1 | đơn | `O` |
| 2 | là | `O` |
| 3 | phải | `O` |
| 4 | được | `O` |
| 5 | tặng | `O` |
| 6 | thêm | `O` |
| 7 | một | `O` |
| 8 | tuýp | `O` |
| 9 | cùng | `O` |
| 10 | loại. | `O` |
| 11 | nhưng | `O` |
| 12 | đến | `O` |
| 13 | khi | `O` |
| 14 | giao | `O` |
| 15 | mở | `O` |
| 16 | hàng | `O` |
| 17 | ra | `O` |
| 18 | lại | `O` |
| 19 | không | `B-COMP` |
| 20 | thấy | `I-COMP` |
| 21 | hàng | `I-COMP` |
| 22 | tặng | `I-COMP` |
| 23 | đâu | `I-COMP` |
| 24 | cả. | `I-COMP` |
| 25 | rất | `O` |
| 26 | cần | `O` |
| 27 | lời | `O` |
| 28 | giải | `O` |
| 29 | thích | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 37. `train_001665`

- Domain: `app`
- Split: `train`

**Text gốc:**

> luyện tập phần việt-anh thì suôn sẻ, nhưng đến phần âm thanh và anh-việt lại tự động hack ra, không thể làm được. chưa kể ứng dụng còn nhiều lần bị đơ, cập nhật phiên bản mới vẫn như vậy, không hiểu thế nào. cho 3 sao vì chưa hài lòng lắm, cần cải thiện hơn.

**Spans:**

- #0 [94:112] `không thể làm được` label=`COMP`
- #1 [135:150] `nhiều lần bị đơ` label=`COMP`
- #2 [175:186] `vẫn như vậy` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | luyện | `O` |
| 1 | tập | `O` |
| 2 | phần | `O` |
| 3 | việt-anh | `O` |
| 4 | thì | `O` |
| 5 | suôn | `O` |
| 6 | sẻ, | `O` |
| 7 | nhưng | `O` |
| 8 | đến | `O` |
| 9 | phần | `O` |
| 10 | âm | `O` |
| 11 | thanh | `O` |
| 12 | và | `O` |
| 13 | anh-việt | `O` |
| 14 | lại | `O` |
| 15 | tự | `O` |
| 16 | động | `O` |
| 17 | hack | `O` |
| 18 | ra, | `O` |
| 19 | không | `B-COMP` |
| 20 | thể | `I-COMP` |
| 21 | làm | `I-COMP` |
| 22 | được. | `I-COMP` |
| 23 | chưa | `O` |
| 24 | kể | `O` |
| 25 | ứng | `O` |
| 26 | dụng | `O` |
| 27 | còn | `O` |
| 28 | nhiều | `B-COMP` |
| 29 | lần | `I-COMP` |
| 30 | bị | `I-COMP` |
| 31 | đơ, | `I-COMP` |
| 32 | cập | `O` |
| 33 | nhật | `O` |
| 34 | phiên | `O` |
| 35 | bản | `O` |
| 36 | mới | `O` |
| 37 | vẫn | `B-COMP` |
| 38 | như | `I-COMP` |
| 39 | vậy, | `I-COMP` |
| 40 | không | `O` |
| 41 | hiểu | `O` |
| 42 | thế | `O` |
| 43 | nào. | `O` |
| 44 | cho | `O` |
| 45 | 3 | `O` |
| 46 | sao | `O` |
| 47 | vì | `O` |
| 48 | chưa | `O` |
| 49 | hài | `O` |
| 50 | lòng | `O` |
| 51 | lắm, | `O` |
| 52 | cần | `O` |
| 53 | cải | `O` |
| 54 | thiện | `O` |
| 55 | hơn. | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 38. `train_001671`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> chất vải hơi xấu

**Spans:**

- #0 [9:16] `hơi xấu` label=`COMP`

**Reason:** Cụm 'hơi xấu' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | chất | `O` |
| 1 | vải | `O` |
| 2 | hơi | `B-COMP` |
| 3 | xấu | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 39. `train_001698`

- Domain: `app`
- Split: `train`

**Text gốc:**

> nên bổ xung thêm tiếng việt nam vào.

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý, khen, hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | nên | `O` |
| 1 | bổ | `O` |
| 2 | xung | `O` |
| 3 | thêm | `O` |
| 4 | tiếng | `O` |
| 5 | việt | `O` |
| 6 | nam | `O` |
| 7 | vào. | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 40. `train_001727`

- Domain: `app`
- Split: `train`

**Text gốc:**

> anh chị xem khắc phục lại lỗi hộ em với ạ, em tải xong vào thì bảo tải dữ liệu, vừa hiện tải xong lỗi, thử lại thì lại hiện tải xong lại lỗi tiếp,cứ như vậy dù em đã xoá đi tải lại 3 lần rồi ạ, em nghe nói aP này tốt nên tải dùng, mong ac fix nhanh để em trải nghiệm thử ạ, em xin cảm ơn ạ.

**Spans:**

- #0 [89:101] `tải xong lỗi` label=`COMP`
- #1 [115:145] `lại hiện tải xong lại lỗi tiếp` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

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
| 11 | em | `O` |
| 12 | tải | `O` |
| 13 | xong | `O` |
| 14 | vào | `O` |
| 15 | thì | `O` |
| 16 | bảo | `O` |
| 17 | tải | `O` |
| 18 | dữ | `O` |
| 19 | liệu, | `O` |
| 20 | vừa | `O` |
| 21 | hiện | `O` |
| 22 | tải | `B-COMP` |
| 23 | xong | `I-COMP` |
| 24 | lỗi, | `I-COMP` |
| 25 | thử | `O` |
| 26 | lại | `O` |
| 27 | thì | `O` |
| 28 | lại | `B-COMP` |
| 29 | hiện | `I-COMP` |
| 30 | tải | `I-COMP` |
| 31 | xong | `I-COMP` |
| 32 | lại | `I-COMP` |
| 33 | lỗi | `I-COMP` |
| 34 | tiếp,cứ | `I-COMP` |
| 35 | như | `O` |
| 36 | vậy | `O` |
| 37 | dù | `O` |
| 38 | em | `O` |
| 39 | đã | `O` |
| 40 | xoá | `O` |
| 41 | đi | `O` |
| 42 | tải | `O` |
| 43 | lại | `O` |
| 44 | 3 | `O` |
| 45 | lần | `O` |
| 46 | rồi | `O` |
| 47 | ạ, | `O` |
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

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 41. `train_001731`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> quần hơi ngắn

**Spans:**

- #0 [5:13] `hơi ngắn` label=`COMP`

**Reason:** Cụm 'hơi ngắn' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | quần | `O` |
| 1 | hơi | `B-COMP` |
| 2 | ngắn | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (66.7%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 42. `train_001732`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đặt  cỡ  36.37 mà giao  cỡ  39 . khỏi mang

**Spans:**

- #0 [18:30] `giao  cỡ  39` label=`COMP`

**Reason:** Cụm 'giao  cỡ  39' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đặt | `O` |
| 1 | cỡ | `O` |
| 2 | 36.37 | `O` |
| 3 | mà | `O` |
| 4 | giao | `B-COMP` |
| 5 | cỡ | `I-COMP` |
| 6 | 39 | `I-COMP` |
| 7 | . | `O` |
| 8 | khỏi | `O` |
| 9 | mang | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 43. `train_001735`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> giao hàng quá lâu

**Spans:**

- #0 [0:17] `giao hàng quá lâu` label=`COMP`

**Reason:** Cụm 'giao hàng quá lâu' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | giao | `B-COMP` |
| 1 | hàng | `I-COMP` |
| 2 | quá | `I-COMP` |
| 3 | lâu | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 44. `train_001758`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> kem nền thì ổn rồi mà quà thì quá tệ tặng cũng có tâm chút đi để màu này tặng cây son hồng bé rồi sao xài, thiệt hết nói nỗi 😑😑😑😑

**Spans:**

- #0 [22:36] `quà thì quá tệ` label=`COMP`
- #1 [73:105] `tặng cây son hồng bé rồi sao xài` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

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
| 16 | để | `O` |
| 17 | màu | `O` |
| 18 | này | `O` |
| 19 | tặng | `B-COMP` |
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

## 45. `train_001797`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> quần  gì ean đúng  cỡ  đúng mẫu tư vấn nhiệt tình cạp quần hơi rộngxíu nhìn chung hài lòng

**Spans:**

- #0 [50:70] `cạp quần hơi rộngxíu` label=`COMP`

**Reason:** Cụm 'cạp quần hơi rộngxíu' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | quần | `O` |
| 1 | gì | `O` |
| 2 | ean | `O` |
| 3 | đúng | `O` |
| 4 | cỡ | `O` |
| 5 | đúng | `O` |
| 6 | mẫu | `O` |
| 7 | tư | `O` |
| 8 | vấn | `O` |
| 9 | nhiệt | `O` |
| 10 | tình | `O` |
| 11 | cạp | `B-COMP` |
| 12 | quần | `I-COMP` |
| 13 | hơi | `I-COMP` |
| 14 | rộngxíu | `I-COMP` |
| 15 | nhìn | `O` |
| 16 | chung | `O` |
| 17 | hài | `O` |
| 18 | lòng | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 46. `train_001806`

- Domain: `app`
- Split: `train`

**Text gốc:**

> như l. đồ ăn cắp. bên trong đài vieTheo báo bạn đã giao dịch thành công và trừ đi 22000trong tài khoản. rồi vào gem thì thấy giao dịch không thành công. Lon

**Spans:**

- #0 [7:16] `đồ ăn cắp` label=`COMP`
- #1 [125:151] `giao dịch không thành công` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | như | `O` |
| 1 | l. | `O` |
| 2 | đồ | `B-COMP` |
| 3 | ăn | `I-COMP` |
| 4 | cắp. | `I-COMP` |
| 5 | bên | `O` |
| 6 | trong | `O` |
| 7 | đài | `O` |
| 8 | vieTheo | `O` |
| 9 | báo | `O` |
| 10 | bạn | `O` |
| 11 | đã | `O` |
| 12 | giao | `O` |
| 13 | dịch | `O` |
| 14 | thành | `O` |
| 15 | công | `O` |
| 16 | và | `O` |
| 17 | trừ | `O` |
| 18 | đi | `O` |
| 19 | 22000trong | `O` |
| 20 | tài | `O` |
| 21 | khoản. | `O` |
| 22 | rồi | `O` |
| 23 | vào | `O` |
| 24 | gem | `O` |
| 25 | thì | `O` |
| 26 | thấy | `O` |
| 27 | giao | `B-COMP` |
| 28 | dịch | `I-COMP` |
| 29 | không | `I-COMP` |
| 30 | thành | `I-COMP` |
| 31 | công. | `I-COMP` |
| 32 | Lon | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 47. `train_001836`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> vải không đẹp nút gài quá lỏng

**Spans:**

- #0 [0:13] `vải không đẹp` label=`COMP`
- #1 [14:30] `nút gài quá lỏng` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

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

## 48. `train_001839`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> mình đặt hàng hôm 9.9 mà giao hàng cực nhanh. hàng fitme thì không còn  gì  để bàn. cho  cửa hàng   5star  .tiếc là không nhận được bộ quà tặng

**Spans:**

- #0 [116:143] `không nhận được bộ quà tặng` label=`COMP`

**Reason:** Cụm 'không nhận được bộ quà tặng' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mình | `O` |
| 1 | đặt | `O` |
| 2 | hàng | `O` |
| 3 | hôm | `O` |
| 4 | 9.9 | `O` |
| 5 | mà | `O` |
| 6 | giao | `O` |
| 7 | hàng | `O` |
| 8 | cực | `O` |
| 9 | nhanh. | `O` |
| 10 | hàng | `O` |
| 11 | fitme | `O` |
| 12 | thì | `O` |
| 13 | không | `O` |
| 14 | còn | `O` |
| 15 | gì | `O` |
| 16 | để | `O` |
| 17 | bàn. | `O` |
| 18 | cho | `O` |
| 19 | cửa | `O` |
| 20 | hàng | `O` |
| 21 | 5star | `O` |
| 22 | .tiếc | `O` |
| 23 | là | `O` |
| 24 | không | `B-COMP` |
| 25 | nhận | `I-COMP` |
| 26 | được | `I-COMP` |
| 27 | bộ | `I-COMP` |
| 28 | quà | `I-COMP` |
| 29 | tặng | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 49. `train_001925`

- Domain: `app`
- Split: `train`

**Text gốc:**

> không thể hiểu tại sao khi gõ tra từ vào cửa sổ anh việt anh trên cùng lại không thể ra được các từ tiếng anh mà lại toàn ra tiếng việt nữa. muốn dịch tiếng anh thì phải vào phần dịch văn bản. có chỉnh thế nào cũng không được. ai giúp mình với được ko?

**Spans:**

- #0 [75:109] `không thể ra được các từ tiếng anh` label=`COMP`
- #1 [117:139] `toàn ra tiếng việt nữa` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | không | `O` |
| 1 | thể | `O` |
| 2 | hiểu | `O` |
| 3 | tại | `O` |
| 4 | sao | `O` |
| 5 | khi | `O` |
| 6 | gõ | `O` |
| 7 | tra | `O` |
| 8 | từ | `O` |
| 9 | vào | `O` |
| 10 | cửa | `O` |
| 11 | sổ | `O` |
| 12 | anh | `O` |
| 13 | việt | `O` |
| 14 | anh | `O` |
| 15 | trên | `O` |
| 16 | cùng | `O` |
| 17 | lại | `O` |
| 18 | không | `B-COMP` |
| 19 | thể | `I-COMP` |
| 20 | ra | `I-COMP` |
| 21 | được | `I-COMP` |
| 22 | các | `I-COMP` |
| 23 | từ | `I-COMP` |
| 24 | tiếng | `I-COMP` |
| 25 | anh | `I-COMP` |
| 26 | mà | `O` |
| 27 | lại | `O` |
| 28 | toàn | `B-COMP` |
| 29 | ra | `I-COMP` |
| 30 | tiếng | `I-COMP` |
| 31 | việt | `I-COMP` |
| 32 | nữa. | `I-COMP` |
| 33 | muốn | `O` |
| 34 | dịch | `O` |
| 35 | tiếng | `O` |
| 36 | anh | `O` |
| 37 | thì | `O` |
| 38 | phải | `O` |
| 39 | vào | `O` |
| 40 | phần | `O` |
| 41 | dịch | `O` |
| 42 | văn | `O` |
| 43 | bản. | `O` |
| 44 | có | `O` |
| 45 | chỉnh | `O` |
| 46 | thế | `O` |
| 47 | nào | `O` |
| 48 | cũng | `O` |
| 49 | không | `O` |
| 50 | được. | `O` |
| 51 | ai | `O` |
| 52 | giúp | `O` |
| 53 | mình | `O` |
| 54 | với | `O` |
| 55 | được | `O` |
| 56 | ko? | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 50. `train_001926`

- Domain: `app`
- Split: `train`

**Text gốc:**

> aP có một số nhược điểm: thứ một là nhiều bài hạn chế, tìm không thấy. thứ 2 là việc aP tự động đăng nhập tài khoản zalo mỗi lần truy cập là rất phiền. cuối cùng là khi tôi dùng các ứng dụng chỉnh video như kinemaster, inshot, viva video ... muốn chèn bài hát đã tải ở zing về nhưng tìm không có, chỉ có ... bài đánh giá đầy đủ

**Spans:**

- #0 [36:69] `nhiều bài hạn chế, tìm không thấy` label=`COMP`
- #1 [88:137] `tự động đăng nhập tài khoản zalo mỗi lần truy cập` label=`COMP`
- #2 [283:295] `tìm không có` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

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
| 20 | aP | `O` |
| 21 | tự | `B-COMP` |
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
| 32 | là | `O` |
| 33 | rất | `O` |
| 34 | phiền. | `O` |
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
| 52 | muốn | `O` |
| 53 | chèn | `O` |
| 54 | bài | `O` |
| 55 | hát | `O` |
| 56 | đã | `O` |
| 57 | tải | `O` |
| 58 | ở | `O` |
| 59 | zing | `O` |
| 60 | về | `O` |
| 61 | nhưng | `O` |
| 62 | tìm | `B-COMP` |
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

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 51. `train_001942`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> vừa mới nhận được hàng, nhưng vẫn chưa được kích hoạt bảo hành

**Spans:**

- #0 [34:62] `chưa được kích hoạt bảo hành` label=`COMP`

**Reason:** Cụm 'chưa được kích hoạt bảo hành' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | vừa | `O` |
| 1 | mới | `O` |
| 2 | nhận | `O` |
| 3 | được | `O` |
| 4 | hàng, | `O` |
| 5 | nhưng | `O` |
| 6 | vẫn | `O` |
| 7 | chưa | `B-COMP` |
| 8 | được | `I-COMP` |
| 9 | kích | `I-COMP` |
| 10 | hoạt | `I-COMP` |
| 11 | bảo | `I-COMP` |
| 12 | hành | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 52. `train_002061`

- Domain: `app`
- Split: `train`

**Text gốc:**

> tôi muốn xoá tài khoản thì làm thế nào tải ứng dụng mà bị quấy nhiễu quá hết gọi điện tới gửi email nếu cần tự liên lạc thôi cứ gọi rồi hộp thư tự động quá phiền

**Spans:**

- #0 [55:72] `bị quấy nhiễu quá` label=`COMP`
- #1 [73:99] `hết gọi điện tới gửi email` label=`COMP`
- #2 [136:161] `hộp thư tự động quá phiền` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tôi | `O` |
| 1 | muốn | `O` |
| 2 | xoá | `O` |
| 3 | tài | `O` |
| 4 | khoản | `O` |
| 5 | thì | `O` |
| 6 | làm | `O` |
| 7 | thế | `O` |
| 8 | nào | `O` |
| 9 | tải | `O` |
| 10 | ứng | `O` |
| 11 | dụng | `O` |
| 12 | mà | `O` |
| 13 | bị | `B-COMP` |
| 14 | quấy | `I-COMP` |
| 15 | nhiễu | `I-COMP` |
| 16 | quá | `I-COMP` |
| 17 | hết | `B-COMP` |
| 18 | gọi | `I-COMP` |
| 19 | điện | `I-COMP` |
| 20 | tới | `I-COMP` |
| 21 | gửi | `I-COMP` |
| 22 | email | `I-COMP` |
| 23 | nếu | `O` |
| 24 | cần | `O` |
| 25 | tự | `O` |
| 26 | liên | `O` |
| 27 | lạc | `O` |
| 28 | thôi | `O` |
| 29 | cứ | `O` |
| 30 | gọi | `O` |
| 31 | rồi | `O` |
| 32 | hộp | `B-COMP` |
| 33 | thư | `I-COMP` |
| 34 | tự | `I-COMP` |
| 35 | động | `I-COMP` |
| 36 | quá | `I-COMP` |
| 37 | phiền | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 53. `train_002069`

- Domain: `app`
- Split: `train`

**Text gốc:**

> công tình yêu lớn mà làm ăn như lừa đảo. làm chương trình km làm gì để khách dô đặt xong rồi không giao, còn kêu giao lộn. số điện thoại địa chỉ tên rõ ràng vậy mà lộn cái gì. làm mất thời gian chờ đợi. còn không có chính sách đền bù. chăm sóc khách hàng có tốt cũng vô dụng. từ nay xoá aP, không bao giờ ... bài đánh giá đầy đủ

**Spans:**

- #0 [21:39] `làm ăn như lừa đảo` label=`COMP`
- #1 [93:103] `không giao` label=`COMP`
- #2 [207:233] `không có chính sách đền bù` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | công | `O` |
| 1 | tình | `O` |
| 2 | yêu | `O` |
| 3 | lớn | `O` |
| 4 | mà | `O` |
| 5 | làm | `B-COMP` |
| 6 | ăn | `I-COMP` |
| 7 | như | `I-COMP` |
| 8 | lừa | `I-COMP` |
| 9 | đảo. | `I-COMP` |
| 10 | làm | `O` |
| 11 | chương | `O` |
| 12 | trình | `O` |
| 13 | km | `O` |
| 14 | làm | `O` |
| 15 | gì | `O` |
| 16 | để | `O` |
| 17 | khách | `O` |
| 18 | dô | `O` |
| 19 | đặt | `O` |
| 20 | xong | `O` |
| 21 | rồi | `O` |
| 22 | không | `B-COMP` |
| 23 | giao, | `I-COMP` |
| 24 | còn | `O` |
| 25 | kêu | `O` |
| 26 | giao | `O` |
| 27 | lộn. | `O` |
| 28 | số | `O` |
| 29 | điện | `O` |
| 30 | thoại | `O` |
| 31 | địa | `O` |
| 32 | chỉ | `O` |
| 33 | tên | `O` |
| 34 | rõ | `O` |
| 35 | ràng | `O` |
| 36 | vậy | `O` |
| 37 | mà | `O` |
| 38 | lộn | `O` |
| 39 | cái | `O` |
| 40 | gì. | `O` |
| 41 | làm | `O` |
| 42 | mất | `O` |
| 43 | thời | `O` |
| 44 | gian | `O` |
| 45 | chờ | `O` |
| 46 | đợi. | `O` |
| 47 | còn | `O` |
| 48 | không | `B-COMP` |
| 49 | có | `I-COMP` |
| 50 | chính | `I-COMP` |
| 51 | sách | `I-COMP` |
| 52 | đền | `I-COMP` |
| 53 | bù. | `I-COMP` |
| 54 | chăm | `O` |
| 55 | sóc | `O` |
| 56 | khách | `O` |
| 57 | hàng | `O` |
| 58 | có | `O` |
| 59 | tốt | `O` |
| 60 | cũng | `O` |
| 61 | vô | `O` |
| 62 | dụng. | `O` |
| 63 | từ | `O` |
| 64 | nay | `O` |
| 65 | xoá | `O` |
| 66 | aP, | `O` |
| 67 | không | `O` |
| 68 | bao | `O` |
| 69 | giờ | `O` |
| 70 | ... | `O` |
| 71 | bài | `O` |
| 72 | đánh | `O` |
| 73 | giá | `O` |
| 74 | đầy | `O` |
| 75 | đủ | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 54. `train_002070`

- Domain: `app`
- Split: `train`

**Text gốc:**

> ứng dụng hay, có thư mục từ của bạn để nhắc nhỉ từ mới rất hay. nếu có thể thêm chức năng nhắc một từ theo thời gian như: 5 phút, 2 giờ, 24 giờ, một tuần, một tháng thì hay. vì nhắc kiểu này sẽ làm cho từ đó ăn vào trí nhớ dài hạn của bạn và sẽ khó mà quên được từ đó. bình chọn 5 star  ủng hộ, mình cũng đã mua l... bài đánh giá đầy đủ

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý, khen, hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | ứng | `O` |
| 1 | dụng | `O` |
| 2 | hay, | `O` |
| 3 | có | `O` |
| 4 | thư | `O` |
| 5 | mục | `O` |
| 6 | từ | `O` |
| 7 | của | `O` |
| 8 | bạn | `O` |
| 9 | để | `O` |
| 10 | nhắc | `O` |
| 11 | nhỉ | `O` |
| 12 | từ | `O` |
| 13 | mới | `O` |
| 14 | rất | `O` |
| 15 | hay. | `O` |
| 16 | nếu | `O` |
| 17 | có | `O` |
| 18 | thể | `O` |
| 19 | thêm | `O` |
| 20 | chức | `O` |
| 21 | năng | `O` |
| 22 | nhắc | `O` |
| 23 | một | `O` |
| 24 | từ | `O` |
| 25 | theo | `O` |
| 26 | thời | `O` |
| 27 | gian | `O` |
| 28 | như: | `O` |
| 29 | 5 | `O` |
| 30 | phút, | `O` |
| 31 | 2 | `O` |
| 32 | giờ, | `O` |
| 33 | 24 | `O` |
| 34 | giờ, | `O` |
| 35 | một | `O` |
| 36 | tuần, | `O` |
| 37 | một | `O` |
| 38 | tháng | `O` |
| 39 | thì | `O` |
| 40 | hay. | `O` |
| 41 | vì | `O` |
| 42 | nhắc | `O` |
| 43 | kiểu | `O` |
| 44 | này | `O` |
| 45 | sẽ | `O` |
| 46 | làm | `O` |
| 47 | cho | `O` |
| 48 | từ | `O` |
| 49 | đó | `O` |
| 50 | ăn | `O` |
| 51 | vào | `O` |
| 52 | trí | `O` |
| 53 | nhớ | `O` |
| 54 | dài | `O` |
| 55 | hạn | `O` |
| 56 | của | `O` |
| 57 | bạn | `O` |
| 58 | và | `O` |
| 59 | sẽ | `O` |
| 60 | khó | `O` |
| 61 | mà | `O` |
| 62 | quên | `O` |
| 63 | được | `O` |
| 64 | từ | `O` |
| 65 | đó. | `O` |
| 66 | bình | `O` |
| 67 | chọn | `O` |
| 68 | 5 | `O` |
| 69 | star | `O` |
| 70 | ủng | `O` |
| 71 | hộ, | `O` |
| 72 | mình | `O` |
| 73 | cũng | `O` |
| 74 | đã | `O` |
| 75 | mua | `O` |
| 76 | l... | `O` |
| 77 | bài | `O` |
| 78 | đánh | `O` |
| 79 | giá | `O` |
| 80 | đầy | `O` |
| 81 | đủ | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 55. `train_002091`

- Domain: `app`
- Split: `train`

**Text gốc:**

> ý tưởng hay , thú vị nhưng sao cái game nó còn lag hơn cái  quả người cáo vậy. lag đơ máy ấy.  quả người cáo ta nói nó mượt gì đâu á. fix game đi rồi tính tiếp

**Spans:**

- #0 [79:92] `lag đơ máy ấy` label=`COMP`

**Reason:** Cụm 'lag đơ máy ấy' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | ý | `O` |
| 1 | tưởng | `O` |
| 2 | hay | `O` |
| 3 | , | `O` |
| 4 | thú | `O` |
| 5 | vị | `O` |
| 6 | nhưng | `O` |
| 7 | sao | `O` |
| 8 | cái | `O` |
| 9 | game | `O` |
| 10 | nó | `O` |
| 11 | còn | `O` |
| 12 | lag | `O` |
| 13 | hơn | `O` |
| 14 | cái | `O` |
| 15 | quả | `O` |
| 16 | người | `O` |
| 17 | cáo | `O` |
| 18 | vậy. | `O` |
| 19 | lag | `B-COMP` |
| 20 | đơ | `I-COMP` |
| 21 | máy | `I-COMP` |
| 22 | ấy. | `I-COMP` |
| 23 | quả | `O` |
| 24 | người | `O` |
| 25 | cáo | `O` |
| 26 | ta | `O` |
| 27 | nói | `O` |
| 28 | nó | `O` |
| 29 | mượt | `O` |
| 30 | gì | `O` |
| 31 | đâu | `O` |
| 32 | á. | `O` |
| 33 | fix | `O` |
| 34 | game | `O` |
| 35 | đi | `O` |
| 36 | rồi | `O` |
| 37 | tính | `O` |
| 38 | tiếp | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 56. `train_002095`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> 1m60 46 không mặc  không  vừa quần ngắn chặt

**Spans:**

- #0 [30:44] `quần ngắn chặt` label=`COMP`

**Reason:** Cụm 'quần ngắn chặt' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | 1m60 | `O` |
| 1 | 46 | `O` |
| 2 | không | `O` |
| 3 | mặc | `O` |
| 4 | không | `O` |
| 5 | vừa | `O` |
| 6 | quần | `B-COMP` |
| 7 | ngắn | `I-COMP` |
| 8 | chặt | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 57. `train_002107`

- Domain: `app`
- Split: `train`

**Text gốc:**

> dich sai hoan toan

**Spans:**

- #0 [0:18] `dich sai hoan toan` label=`COMP`

**Reason:** Cụm 'dich sai hoan toan' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | dich | `B-COMP` |
| 1 | sai | `I-COMP` |
| 2 | hoan | `I-COMP` |
| 3 | toan | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 58. `train_002144`

- Domain: `app`
- Split: `train`

**Text gốc:**

> game không hề cân bằng, nạp và không nạp quá khác biệt, hệ thống tìm trận không cân xứng lực chiến 5k gặp 10k 3 ván liền thì chơi gì? và ngoài việc nạp thẻ thì đá cường hoá lấy ở đâu ra??? hay là vng không quan tâm đến người chơi mà chỉ quan tâm đến tiền thu từ nạp thẻ? game hút máu à?

**Spans:**

- #0 [0:22] `game không hề cân bằng` label=`COMP`
- #1 [24:54] `nạp và không nạp quá khác biệt` label=`COMP`
- #2 [56:98] `hệ thống tìm trận không cân xứng lực chiến` label=`COMP`
- #3 [271:286] `game hút máu à?` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

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
| 21 | 5k | `O` |
| 22 | gặp | `O` |
| 23 | 10k | `O` |
| 24 | 3 | `O` |
| 25 | ván | `O` |
| 26 | liền | `O` |
| 27 | thì | `O` |
| 28 | chơi | `O` |
| 29 | gì? | `O` |
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
| 45 | vng | `O` |
| 46 | không | `O` |
| 47 | quan | `O` |
| 48 | tâm | `O` |
| 49 | đến | `O` |
| 50 | người | `O` |
| 51 | chơi | `O` |
| 52 | mà | `O` |
| 53 | chỉ | `O` |
| 54 | quan | `O` |
| 55 | tâm | `O` |
| 56 | đến | `O` |
| 57 | tiền | `O` |
| 58 | thu | `O` |
| 59 | từ | `O` |
| 60 | nạp | `O` |
| 61 | thẻ? | `O` |
| 62 | game | `B-COMP` |
| 63 | hút | `I-COMP` |
| 64 | máu | `I-COMP` |
| 65 | à? | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 59. `train_002166`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> mẹ mình thích lắm mặc dù đế nhựa vậy không đẹp lắm nhưng hợp giá

**Spans:**

- #0 [25:50] `đế nhựa vậy không đẹp lắm` label=`COMP`

**Reason:** Cụm 'đế nhựa vậy không đẹp lắm' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mẹ | `O` |
| 1 | mình | `O` |
| 2 | thích | `O` |
| 3 | lắm | `O` |
| 4 | mặc | `O` |
| 5 | dù | `O` |
| 6 | đế | `B-COMP` |
| 7 | nhựa | `I-COMP` |
| 8 | vậy | `I-COMP` |
| 9 | không | `I-COMP` |
| 10 | đẹp | `I-COMP` |
| 11 | lắm | `I-COMP` |
| 12 | nhưng | `O` |
| 13 | hợp | `O` |
| 14 | giá | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 60. `train_002171`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> hơi rộng tí, nhưng mà hàng y hình, vải đẹp

**Spans:**

- #0 [0:11] `hơi rộng tí` label=`COMP`

**Reason:** Cụm 'hơi rộng tí' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hơi | `B-COMP` |
| 1 | rộng | `I-COMP` |
| 2 | tí, | `I-COMP` |
| 3 | nhưng | `O` |
| 4 | mà | `O` |
| 5 | hàng | `O` |
| 6 | y | `O` |
| 7 | hình, | `O` |
| 8 | vải | `O` |
| 9 | đẹp | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 61. `train_002259`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> hơi buồn chút xíu vì đăt gì  cỡ 37 rồi màDi vẫn bé . (mặc dù đi thử của chị cỡ 36 và vẫn vừa thậmchis còn thừa một chút) còn đi cũng được

**Spans:**

- #0 [44:50] `vẫn bé` label=`COMP`

**Reason:** Cụm 'vẫn bé' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hơi | `O` |
| 1 | buồn | `O` |
| 2 | chút | `O` |
| 3 | xíu | `O` |
| 4 | vì | `O` |
| 5 | đăt | `O` |
| 6 | gì | `O` |
| 7 | cỡ | `O` |
| 8 | 37 | `O` |
| 9 | rồi | `O` |
| 10 | màDi | `O` |
| 11 | vẫn | `B-COMP` |
| 12 | bé | `I-COMP` |
| 13 | . | `O` |
| 14 | (mặc | `O` |
| 15 | dù | `O` |
| 16 | đi | `O` |
| 17 | thử | `O` |
| 18 | của | `O` |
| 19 | chị | `O` |
| 20 | cỡ | `O` |
| 21 | 36 | `O` |
| 22 | và | `O` |
| 23 | vẫn | `O` |
| 24 | vừa | `O` |
| 25 | thậmchis | `O` |
| 26 | còn | `O` |
| 27 | thừa | `O` |
| 28 | một | `O` |
| 29 | chút) | `O` |
| 30 | còn | `O` |
| 31 | đi | `O` |
| 32 | cũng | `O` |
| 33 | được | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 62. `train_002291`

- Domain: `app`
- Split: `train`

**Text gốc:**

> sao không đánh giá  1star    được  nhỉ!? tiếc cái công 2 tháng chơi game, anh em nào tưởng hay thì chớ có dại nhé, sau hối không kịp

**Spans:**

- #0 [4:33] `không đánh giá  1star    được` label=`COMP`

**Reason:** Cụm 'không đánh giá  1star    được' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | sao | `O` |
| 1 | không | `B-COMP` |
| 2 | đánh | `I-COMP` |
| 3 | giá | `I-COMP` |
| 4 | 1star | `I-COMP` |
| 5 | được | `I-COMP` |
| 6 | nhỉ!? | `O` |
| 7 | tiếc | `O` |
| 8 | cái | `O` |
| 9 | công | `O` |
| 10 | 2 | `O` |
| 11 | tháng | `O` |
| 12 | chơi | `O` |
| 13 | game, | `O` |
| 14 | anh | `O` |
| 15 | em | `O` |
| 16 | nào | `O` |
| 17 | tưởng | `O` |
| 18 | hay | `O` |
| 19 | thì | `O` |
| 20 | chớ | `O` |
| 21 | có | `O` |
| 22 | dại | `O` |
| 23 | nhé, | `O` |
| 24 | sau | `O` |
| 25 | hối | `O` |
| 26 | không | `O` |
| 27 | kịp | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 63. `train_002451`

- Domain: `app`
- Split: `train`

**Text gốc:**

> nếu không vì garena đã làm quá tốt trước kia để có những tiếc nuối thì thì cái qv98 2.0 này cũng không nhiều người chơi đến vậy đâu, thật sự thất vọng

**Spans:**

- #0 [133:150] `thật sự thất vọng` label=`COMP`

**Reason:** Cụm 'thật sự thất vọng' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | nếu | `O` |
| 1 | không | `O` |
| 2 | vì | `O` |
| 3 | garena | `O` |
| 4 | đã | `O` |
| 5 | làm | `O` |
| 6 | quá | `O` |
| 7 | tốt | `O` |
| 8 | trước | `O` |
| 9 | kia | `O` |
| 10 | để | `O` |
| 11 | có | `O` |
| 12 | những | `O` |
| 13 | tiếc | `O` |
| 14 | nuối | `O` |
| 15 | thì | `O` |
| 16 | thì | `O` |
| 17 | cái | `O` |
| 18 | qv98 | `O` |
| 19 | 2.0 | `O` |
| 20 | này | `O` |
| 21 | cũng | `O` |
| 22 | không | `O` |
| 23 | nhiều | `O` |
| 24 | người | `O` |
| 25 | chơi | `O` |
| 26 | đến | `O` |
| 27 | vậy | `O` |
| 28 | đâu, | `O` |
| 29 | thật | `B-COMP` |
| 30 | sự | `I-COMP` |
| 31 | thất | `I-COMP` |
| 32 | vọng | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 64. `train_002463`

- Domain: `app`
- Split: `train`

**Text gốc:**

> tính đến thời điểm hiện tại thì tôi đã mất 6 tài khoản facebook rồi . một phần là nhờ hacker , một phần là nhờ xác nhận tài khoản . tôi có đăng nhập hay làm gì sai đâu mà cứ mất tài khoản hoài , cứ mỗi lần tôi bị vậy là phải tạo tài khoản lại , đã thế còn mất công đi tìm lại bạn mình để kết bạn lại , ai ai cũng than phiền... bài đánh giá đầy đủ

**Spans:**

- #0 [39:67] `mất 6 tài khoản facebook rồi` label=`COMP`
- #1 [171:192] `cứ mất tài khoản hoài` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tính | `O` |
| 1 | đến | `O` |
| 2 | thời | `O` |
| 3 | điểm | `O` |
| 4 | hiện | `O` |
| 5 | tại | `O` |
| 6 | thì | `O` |
| 7 | tôi | `O` |
| 8 | đã | `O` |
| 9 | mất | `B-COMP` |
| 10 | 6 | `I-COMP` |
| 11 | tài | `I-COMP` |
| 12 | khoản | `I-COMP` |
| 13 | facebook | `I-COMP` |
| 14 | rồi | `I-COMP` |
| 15 | . | `O` |
| 16 | một | `O` |
| 17 | phần | `O` |
| 18 | là | `O` |
| 19 | nhờ | `O` |
| 20 | hacker | `O` |
| 21 | , | `O` |
| 22 | một | `O` |
| 23 | phần | `O` |
| 24 | là | `O` |
| 25 | nhờ | `O` |
| 26 | xác | `O` |
| 27 | nhận | `O` |
| 28 | tài | `O` |
| 29 | khoản | `O` |
| 30 | . | `O` |
| 31 | tôi | `O` |
| 32 | có | `O` |
| 33 | đăng | `O` |
| 34 | nhập | `O` |
| 35 | hay | `O` |
| 36 | làm | `O` |
| 37 | gì | `O` |
| 38 | sai | `O` |
| 39 | đâu | `O` |
| 40 | mà | `O` |
| 41 | cứ | `B-COMP` |
| 42 | mất | `I-COMP` |
| 43 | tài | `I-COMP` |
| 44 | khoản | `I-COMP` |
| 45 | hoài | `I-COMP` |
| 46 | , | `O` |
| 47 | cứ | `O` |
| 48 | mỗi | `O` |
| 49 | lần | `O` |
| 50 | tôi | `O` |
| 51 | bị | `O` |
| 52 | vậy | `O` |
| 53 | là | `O` |
| 54 | phải | `O` |
| 55 | tạo | `O` |
| 56 | tài | `O` |
| 57 | khoản | `O` |
| 58 | lại | `O` |
| 59 | , | `O` |
| 60 | đã | `O` |
| 61 | thế | `O` |
| 62 | còn | `O` |
| 63 | mất | `O` |
| 64 | công | `O` |
| 65 | đi | `O` |
| 66 | tìm | `O` |
| 67 | lại | `O` |
| 68 | bạn | `O` |
| 69 | mình | `O` |
| 70 | để | `O` |
| 71 | kết | `O` |
| 72 | bạn | `O` |
| 73 | lại | `O` |
| 74 | , | `O` |
| 75 | ai | `O` |
| 76 | ai | `O` |
| 77 | cũng | `O` |
| 78 | than | `O` |
| 79 | phiền... | `O` |
| 80 | bài | `O` |
| 81 | đánh | `O` |
| 82 | giá | `O` |
| 83 | đầy | `O` |
| 84 | đủ | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 65. `train_002527`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> không tặng son như  quả người cáo

**Spans:**

- #0 [0:14] `không tặng son` label=`COMP`

**Reason:** Cụm 'không tặng son' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | không | `B-COMP` |
| 1 | tặng | `I-COMP` |
| 2 | son | `I-COMP` |
| 3 | như | `O` |
| 4 | quả | `O` |
| 5 | người | `O` |
| 6 | cáo | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 66. `train_002628`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> hay bị kẹt chất lượng trung quốc bình, không nên mua

**Spans:**

- #0 [0:10] `hay bị kẹt` label=`COMP`
- #1 [39:52] `không nên mua` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hay | `B-COMP` |
| 1 | bị | `I-COMP` |
| 2 | kẹt | `I-COMP` |
| 3 | chất | `O` |
| 4 | lượng | `O` |
| 5 | trung | `O` |
| 6 | quốc | `O` |
| 7 | bình, | `O` |
| 8 | không | `B-COMP` |
| 9 | nên | `I-COMP` |
| 10 | mua | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 67. `train_002656`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

>  cửa hàng  giao đồ  không  đúng như mẫu mình đã đặt nha..... hơi thất vọng síu với lại đồ hơi nhân đồ củng được nói chung củng chấp nhận  được  mà đề ngị lần sau  cửa hàng  nên cho khách hàng kiểm tra hàng trước thì hay hơn  gì i nếu hàng lỗi còn đổi liền  được  chứ  không  cho kiểm hàng thì hàng lỗi thì lổ cho khách hàng rồi..... đây là ý kiến riêng của mình nếu  cửa hàng  cho kiểm hàng trước thì lần sau mình ủng hộ tiếp nha

**Spans:**

- #0 [11:51] `giao đồ  không  đúng như mẫu mình đã đặt` label=`COMP`
- #1 [275:301] `cho kiểm hàng thì hàng lỗi` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | cửa | `O` |
| 1 | hàng | `O` |
| 2 | giao | `B-COMP` |
| 3 | đồ | `I-COMP` |
| 4 | không | `I-COMP` |
| 5 | đúng | `I-COMP` |
| 6 | như | `I-COMP` |
| 7 | mẫu | `I-COMP` |
| 8 | mình | `I-COMP` |
| 9 | đã | `I-COMP` |
| 10 | đặt | `I-COMP` |
| 11 | nha..... | `O` |
| 12 | hơi | `O` |
| 13 | thất | `O` |
| 14 | vọng | `O` |
| 15 | síu | `O` |
| 16 | với | `O` |
| 17 | lại | `O` |
| 18 | đồ | `O` |
| 19 | hơi | `O` |
| 20 | nhân | `O` |
| 21 | đồ | `O` |
| 22 | củng | `O` |
| 23 | được | `O` |
| 24 | nói | `O` |
| 25 | chung | `O` |
| 26 | củng | `O` |
| 27 | chấp | `O` |
| 28 | nhận | `O` |
| 29 | được | `O` |
| 30 | mà | `O` |
| 31 | đề | `O` |
| 32 | ngị | `O` |
| 33 | lần | `O` |
| 34 | sau | `O` |
| 35 | cửa | `O` |
| 36 | hàng | `O` |
| 37 | nên | `O` |
| 38 | cho | `O` |
| 39 | khách | `O` |
| 40 | hàng | `O` |
| 41 | kiểm | `O` |
| 42 | tra | `O` |
| 43 | hàng | `O` |
| 44 | trước | `O` |
| 45 | thì | `O` |
| 46 | hay | `O` |
| 47 | hơn | `O` |
| 48 | gì | `O` |
| 49 | i | `O` |
| 50 | nếu | `O` |
| 51 | hàng | `O` |
| 52 | lỗi | `O` |
| 53 | còn | `O` |
| 54 | đổi | `O` |
| 55 | liền | `O` |
| 56 | được | `O` |
| 57 | chứ | `O` |
| 58 | không | `O` |
| 59 | cho | `B-COMP` |
| 60 | kiểm | `I-COMP` |
| 61 | hàng | `I-COMP` |
| 62 | thì | `I-COMP` |
| 63 | hàng | `I-COMP` |
| 64 | lỗi | `I-COMP` |
| 65 | thì | `O` |
| 66 | lổ | `O` |
| 67 | cho | `O` |
| 68 | khách | `O` |
| 69 | hàng | `O` |
| 70 | rồi..... | `O` |
| 71 | đây | `O` |
| 72 | là | `O` |
| 73 | ý | `O` |
| 74 | kiến | `O` |
| 75 | riêng | `O` |
| 76 | của | `O` |
| 77 | mình | `O` |
| 78 | nếu | `O` |
| 79 | cửa | `O` |
| 80 | hàng | `O` |
| 81 | cho | `O` |
| 82 | kiểm | `O` |
| 83 | hàng | `O` |
| 84 | trước | `O` |
| 85 | thì | `O` |
| 86 | lần | `O` |
| 87 | sau | `O` |
| 88 | mình | `O` |
| 89 | ủng | `O` |
| 90 | hộ | `O` |
| 91 | tiếp | `O` |
| 92 | nha | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 68. `train_002678`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> mua  cỡ  39  cửa hàng  gửi 38 chẳng nhẽ lại không nhận hàng. cửa hàng  chốt đơn chán ghê

**Spans:**

- #0 [23:29] `gửi 38` label=`COMP`
- #1 [71:88] `chốt đơn chán ghê` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mua | `O` |
| 1 | cỡ | `O` |
| 2 | 39 | `O` |
| 3 | cửa | `O` |
| 4 | hàng | `O` |
| 5 | gửi | `B-COMP` |
| 6 | 38 | `I-COMP` |
| 7 | chẳng | `O` |
| 8 | nhẽ | `O` |
| 9 | lại | `O` |
| 10 | không | `O` |
| 11 | nhận | `O` |
| 12 | hàng. | `O` |
| 13 | cửa | `O` |
| 14 | hàng | `O` |
| 15 | chốt | `B-COMP` |
| 16 | đơn | `I-COMP` |
| 17 | chán | `I-COMP` |
| 18 | ghê | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 69. `train_002774`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> đã nhận hàng nhưng không thấy có hàng tặng kèm như viết trong chương trình khuyến mại

**Spans:**

- #0 [19:85] `không thấy có hàng tặng kèm như viết trong chương trình khuyến mại` label=`COMP`

**Reason:** Cụm 'không thấy có hàng tặng kèm như viết trong chương trình khuyến mại' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đã | `O` |
| 1 | nhận | `O` |
| 2 | hàng | `O` |
| 3 | nhưng | `O` |
| 4 | không | `B-COMP` |
| 5 | thấy | `I-COMP` |
| 6 | có | `I-COMP` |
| 7 | hàng | `I-COMP` |
| 8 | tặng | `I-COMP` |
| 9 | kèm | `I-COMP` |
| 10 | như | `I-COMP` |
| 11 | viết | `I-COMP` |
| 12 | trong | `I-COMP` |
| 13 | chương | `I-COMP` |
| 14 | trình | `I-COMP` |
| 15 | khuyến | `I-COMP` |
| 16 | mại | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (76.5%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 70. `train_002798`

- Domain: `app`
- Split: `train`

**Text gốc:**

> em không vào aP  được  ạ. bấm vào cứ out ra thôi ạ

**Spans:**

- #0 [3:21] `không vào aP  được` label=`COMP`
- #1 [34:48] `cứ out ra thôi` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | em | `O` |
| 1 | không | `B-COMP` |
| 2 | vào | `I-COMP` |
| 3 | aP | `I-COMP` |
| 4 | được | `I-COMP` |
| 5 | ạ. | `O` |
| 6 | bấm | `O` |
| 7 | vào | `O` |
| 8 | cứ | `B-COMP` |
| 9 | out | `I-COMP` |
| 10 | ra | `I-COMP` |
| 11 | thôi | `I-COMP` |
| 12 | ạ | `O` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (61.5%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 71. `train_002814`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> vải quá xấu . giao  không đúng màu

**Spans:**

- #0 [0:11] `vải quá xấu` label=`COMP`
- #1 [14:34] `giao  không đúng màu` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | vải | `B-COMP` |
| 1 | quá | `I-COMP` |
| 2 | xấu | `I-COMP` |
| 3 | . | `O` |
| 4 | giao | `B-COMP` |
| 5 | không | `I-COMP` |
| 6 | đúng | `I-COMP` |
| 7 | màu | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (87.5%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 72. `train_002815`

- Domain: `app`
- Split: `train`

**Text gốc:**

> guNy làm ăn  gì  vậy 2 ngay rồi mà mua gói 1000xu tiền thì lấy rùi vậy xu của tôi đâu tôi nạp để nhận các nhiệm vụ nạp lần đầu tiên mà hôm nay ngày cuối rồi mà chua chuyển xu là sao ngày mai chuyển xu chả phải tôi chịu thiệt à guNy đóng cửa đi 6 ngày từ khi nạp không nhận  được  xu

**Spans:**

- #0 [5:20] `làm ăn  gì  vậy` label=`COMP`
- #1 [160:181] `chua chuyển xu là sao` label=`COMP`
- #2 [262:282] `không nhận  được  xu` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | guNy | `O` |
| 1 | làm | `B-COMP` |
| 2 | ăn | `I-COMP` |
| 3 | gì | `I-COMP` |
| 4 | vậy | `I-COMP` |
| 5 | 2 | `O` |
| 6 | ngay | `O` |
| 7 | rồi | `O` |
| 8 | mà | `O` |
| 9 | mua | `O` |
| 10 | gói | `O` |
| 11 | 1000xu | `O` |
| 12 | tiền | `O` |
| 13 | thì | `O` |
| 14 | lấy | `O` |
| 15 | rùi | `O` |
| 16 | vậy | `O` |
| 17 | xu | `O` |
| 18 | của | `O` |
| 19 | tôi | `O` |
| 20 | đâu | `O` |
| 21 | tôi | `O` |
| 22 | nạp | `O` |
| 23 | để | `O` |
| 24 | nhận | `O` |
| 25 | các | `O` |
| 26 | nhiệm | `O` |
| 27 | vụ | `O` |
| 28 | nạp | `O` |
| 29 | lần | `O` |
| 30 | đầu | `O` |
| 31 | tiên | `O` |
| 32 | mà | `O` |
| 33 | hôm | `O` |
| 34 | nay | `O` |
| 35 | ngày | `O` |
| 36 | cuối | `O` |
| 37 | rồi | `O` |
| 38 | mà | `O` |
| 39 | chua | `B-COMP` |
| 40 | chuyển | `I-COMP` |
| 41 | xu | `I-COMP` |
| 42 | là | `I-COMP` |
| 43 | sao | `I-COMP` |
| 44 | ngày | `O` |
| 45 | mai | `O` |
| 46 | chuyển | `O` |
| 47 | xu | `O` |
| 48 | chả | `O` |
| 49 | phải | `O` |
| 50 | tôi | `O` |
| 51 | chịu | `O` |
| 52 | thiệt | `O` |
| 53 | à | `O` |
| 54 | guNy | `O` |
| 55 | đóng | `O` |
| 56 | cửa | `O` |
| 57 | đi | `O` |
| 58 | 6 | `O` |
| 59 | ngày | `O` |
| 60 | từ | `O` |
| 61 | khi | `O` |
| 62 | nạp | `O` |
| 63 | không | `B-COMP` |
| 64 | nhận | `I-COMP` |
| 65 | được | `I-COMP` |
| 66 | xu | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 73. `train_002844`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> hàng có mùi cồn rất nặng.

**Spans:**

- #0 [8:24] `mùi cồn rất nặng` label=`COMP`

**Reason:** Cụm 'mùi cồn rất nặng' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hàng | `O` |
| 1 | có | `O` |
| 2 | mùi | `B-COMP` |
| 3 | cồn | `I-COMP` |
| 4 | rất | `I-COMP` |
| 5 | nặng. | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (66.7%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 74. `train_002871`

- Domain: `app`
- Split: `train`

**Text gốc:**

> phần mềm có nhiều điểm mới rất bổ ích, cám ơn 😍😘😗😙😚 mới cập nhật phần mềm - bữa giờ không còn tra được từ như lúc trước nữa. mình dùng android 😔 chúc phần mềm ngày càng phát triển 😊

**Spans:**

- #0 [84:123] `không còn tra được từ như lúc trước nữa` label=`COMP`

**Reason:** Cụm 'không còn tra được từ như lúc trước nữa' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | phần | `O` |
| 1 | mềm | `O` |
| 2 | có | `O` |
| 3 | nhiều | `O` |
| 4 | điểm | `O` |
| 5 | mới | `O` |
| 6 | rất | `O` |
| 7 | bổ | `O` |
| 8 | ích, | `O` |
| 9 | cám | `O` |
| 10 | ơn | `O` |
| 11 | 😍😘😗😙😚 | `O` |
| 12 | mới | `O` |
| 13 | cập | `O` |
| 14 | nhật | `O` |
| 15 | phần | `O` |
| 16 | mềm | `O` |
| 17 | - | `O` |
| 18 | bữa | `O` |
| 19 | giờ | `O` |
| 20 | không | `B-COMP` |
| 21 | còn | `I-COMP` |
| 22 | tra | `I-COMP` |
| 23 | được | `I-COMP` |
| 24 | từ | `I-COMP` |
| 25 | như | `I-COMP` |
| 26 | lúc | `I-COMP` |
| 27 | trước | `I-COMP` |
| 28 | nữa. | `I-COMP` |
| 29 | mình | `O` |
| 30 | dùng | `O` |
| 31 | android | `O` |
| 32 | 😔 | `O` |
| 33 | chúc | `O` |
| 34 | phần | `O` |
| 35 | mềm | `O` |
| 36 | ngày | `O` |
| 37 | càng | `O` |
| 38 | phát | `O` |
| 39 | triển | `O` |
| 40 | 😊 | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 75. `train_002940`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

>  cửa hàng  làm ăn kỳ vậy? lúc mua là có tặng son giờ lại nói không có.

**Spans:**

- #0 [26:69] `lúc mua là có tặng son giờ lại nói không có` label=`COMP`

**Reason:** Cụm 'lúc mua là có tặng son giờ lại nói không có' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | cửa | `O` |
| 1 | hàng | `O` |
| 2 | làm | `O` |
| 3 | ăn | `O` |
| 4 | kỳ | `O` |
| 5 | vậy? | `O` |
| 6 | lúc | `B-COMP` |
| 7 | mua | `I-COMP` |
| 8 | là | `I-COMP` |
| 9 | có | `I-COMP` |
| 10 | tặng | `I-COMP` |
| 11 | son | `I-COMP` |
| 12 | giờ | `I-COMP` |
| 13 | lại | `I-COMP` |
| 14 | nói | `I-COMP` |
| 15 | không | `I-COMP` |
| 16 | có. | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (64.7%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 76. `train_002949`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> không hài lòng lắm vì màu không đúng như mình chọn. nhưng chất lượng dù khá tốt như hình mẫu. đóng gói chắc chắn.

**Spans:**

- #0 [22:50] `màu không đúng như mình chọn` label=`COMP`

**Reason:** Cụm 'màu không đúng như mình chọn' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | không | `O` |
| 1 | hài | `O` |
| 2 | lòng | `O` |
| 3 | lắm | `O` |
| 4 | vì | `O` |
| 5 | màu | `B-COMP` |
| 6 | không | `I-COMP` |
| 7 | đúng | `I-COMP` |
| 8 | như | `I-COMP` |
| 9 | mình | `I-COMP` |
| 10 | chọn. | `I-COMP` |
| 11 | nhưng | `O` |
| 12 | chất | `O` |
| 13 | lượng | `O` |
| 14 | dù | `O` |
| 15 | khá | `O` |
| 16 | tốt | `O` |
| 17 | như | `O` |
| 18 | hình | `O` |
| 19 | mẫu. | `O` |
| 20 | đóng | `O` |
| 21 | gói | `O` |
| 22 | chắc | `O` |
| 23 | chắn. | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 77. `train_002951`

- Domain: `app`
- Split: `train`

**Text gốc:**

> mới vô thật sự nản game luôn . đã thế nạp xong vô không biết kc nó đi đâu.. mong nhà điều hành xem lại kc nó đi đâu...

**Spans:**

- #0 [50:73] `không biết kc nó đi đâu` label=`COMP`

**Reason:** Cụm 'không biết kc nó đi đâu' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mới | `O` |
| 1 | vô | `O` |
| 2 | thật | `O` |
| 3 | sự | `O` |
| 4 | nản | `O` |
| 5 | game | `O` |
| 6 | luôn | `O` |
| 7 | . | `O` |
| 8 | đã | `O` |
| 9 | thế | `O` |
| 10 | nạp | `O` |
| 11 | xong | `O` |
| 12 | vô | `O` |
| 13 | không | `B-COMP` |
| 14 | biết | `I-COMP` |
| 15 | kc | `I-COMP` |
| 16 | nó | `I-COMP` |
| 17 | đi | `I-COMP` |
| 18 | đâu.. | `I-COMP` |
| 19 | mong | `O` |
| 20 | nhà | `O` |
| 21 | điều | `O` |
| 22 | hành | `O` |
| 23 | xem | `O` |
| 24 | lại | `O` |
| 25 | kc | `O` |
| 26 | nó | `O` |
| 27 | đi | `O` |
| 28 | đâu... | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 78. `train_003076`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> sac lan dau tien tren 7tieg ma hien thi 98%. không đay pin la sao?

**Spans:**

- #0 [31:43] `hien thi 98%` label=`COMP`
- #1 [45:58] `không đay pin` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | sac | `O` |
| 1 | lan | `O` |
| 2 | dau | `O` |
| 3 | tien | `O` |
| 4 | tren | `O` |
| 5 | 7tieg | `O` |
| 6 | ma | `O` |
| 7 | hien | `B-COMP` |
| 8 | thi | `I-COMP` |
| 9 | 98%. | `I-COMP` |
| 10 | không | `B-COMP` |
| 11 | đay | `I-COMP` |
| 12 | pin | `I-COMP` |
| 13 | la | `O` |
| 14 | sao? | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 79. `train_003110`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> cái hộp bị móp, nên hơi lo lắng..nhưng bên trong không sao, máy rất phù hợp với nhu cầu cơ bản. ladaza nhớ kích hoạt bảo hành dùm nhé.

**Spans:**

- #0 [0:14] `cái hộp bị móp` label=`COMP`

**Reason:** Cụm 'cái hộp bị móp' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | cái | `B-COMP` |
| 1 | hộp | `I-COMP` |
| 2 | bị | `I-COMP` |
| 3 | móp, | `I-COMP` |
| 4 | nên | `O` |
| 5 | hơi | `O` |
| 6 | lo | `O` |
| 7 | lắng..nhưng | `O` |
| 8 | bên | `O` |
| 9 | trong | `O` |
| 10 | không | `O` |
| 11 | sao, | `O` |
| 12 | máy | `O` |
| 13 | rất | `O` |
| 14 | phù | `O` |
| 15 | hợp | `O` |
| 16 | với | `O` |
| 17 | nhu | `O` |
| 18 | cầu | `O` |
| 19 | cơ | `O` |
| 20 | bản. | `O` |
| 21 | ladaza | `O` |
| 22 | nhớ | `O` |
| 23 | kích | `O` |
| 24 | hoạt | `O` |
| 25 | bảo | `O` |
| 26 | hành | `O` |
| 27 | dùm | `O` |
| 28 | nhé. | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 80. `train_003128`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> giao hạn sử dụng cũ sản xuất tận một năm trc. có mùi không thơm như sử dụng trước đó. mùi kì kì. mong  cửa hàng  phản hồi

**Spans:**

- #0 [5:44] `hạn sử dụng cũ sản xuất tận một năm trc` label=`COMP`
- #1 [49:63] `mùi không thơm` label=`COMP`
- #2 [86:95] `mùi kì kì` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | giao | `O` |
| 1 | hạn | `B-COMP` |
| 2 | sử | `I-COMP` |
| 3 | dụng | `I-COMP` |
| 4 | cũ | `I-COMP` |
| 5 | sản | `I-COMP` |
| 6 | xuất | `I-COMP` |
| 7 | tận | `I-COMP` |
| 8 | một | `I-COMP` |
| 9 | năm | `I-COMP` |
| 10 | trc. | `I-COMP` |
| 11 | có | `O` |
| 12 | mùi | `B-COMP` |
| 13 | không | `I-COMP` |
| 14 | thơm | `I-COMP` |
| 15 | như | `O` |
| 16 | sử | `O` |
| 17 | dụng | `O` |
| 18 | trước | `O` |
| 19 | đó. | `O` |
| 20 | mùi | `B-COMP` |
| 21 | kì | `I-COMP` |
| 22 | kì. | `I-COMP` |
| 23 | mong | `O` |
| 24 | cửa | `O` |
| 25 | hàng | `O` |
| 26 | phản | `O` |
| 27 | hồi | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 81. `train_003263`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> vay bong đường chỉ

**Spans:**

- #0 [0:18] `vay bong đường chỉ` label=`COMP`

**Reason:** Cụm 'vay bong đường chỉ' nêu trực tiếp vấn đề chính.

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

## 82. `train_003285`

- Domain: `app`
- Split: `train`

**Text gốc:**

> admin ơi. sao không thấy thông kê các thông số dịch bệnh liên quan đến nước anh vậy

**Spans:**

- #0 [14:79] `không thấy thông kê các thông số dịch bệnh liên quan đến nước anh` label=`COMP`

**Reason:** Cụm 'không thấy thông kê các thông số dịch bệnh liên quan đến nước anh' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | admin | `O` |
| 1 | ơi. | `O` |
| 2 | sao | `O` |
| 3 | không | `B-COMP` |
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
| 17 | vậy | `O` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (77.8%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 83. `train_003290`

- Domain: `app`
- Split: `train`

**Text gốc:**

> xin nhà phát hành game cho thêm stop ở bà rịa - vũng tàu, thành phố bà rịa, đương số 43, ấp đông, xã hoà long nha. nhiều khi muốn chơi nhưng cứ vô là không có gym với stop nên buồn

**Spans:**

- #0 [150:171] `không có gym với stop` label=`COMP`

**Reason:** Cụm 'không có gym với stop' nêu trực tiếp bất cập khiến người dùng không chơi được như mong muốn; phần còn lại là đề xuất địa điểm.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | xin | `O` |
| 1 | nhà | `O` |
| 2 | phát | `O` |
| 3 | hành | `O` |
| 4 | game | `O` |
| 5 | cho | `O` |
| 6 | thêm | `O` |
| 7 | stop | `O` |
| 8 | ở | `O` |
| 9 | bà | `O` |
| 10 | rịa | `O` |
| 11 | - | `O` |
| 12 | vũng | `O` |
| 13 | tàu, | `O` |
| 14 | thành | `O` |
| 15 | phố | `O` |
| 16 | bà | `O` |
| 17 | rịa, | `O` |
| 18 | đương | `O` |
| 19 | số | `O` |
| 20 | 43, | `O` |
| 21 | ấp | `O` |
| 22 | đông, | `O` |
| 23 | xã | `O` |
| 24 | hoà | `O` |
| 25 | long | `O` |
| 26 | nha. | `O` |
| 27 | nhiều | `O` |
| 28 | khi | `O` |
| 29 | muốn | `O` |
| 30 | chơi | `O` |
| 31 | nhưng | `O` |
| 32 | cứ | `O` |
| 33 | vô | `O` |
| 34 | là | `O` |
| 35 | không | `B-COMP` |
| 36 | có | `I-COMP` |
| 37 | gym | `I-COMP` |
| 38 | với | `I-COMP` |
| 39 | stop | `I-COMP` |
| 40 | nên | `O` |
| 41 | buồn | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 84. `train_003334`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> dép hơi cứng. đi đau mũi chân

**Spans:**

- #0 [0:12] `dép hơi cứng` label=`COMP`
- #1 [14:29] `đi đau mũi chân` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | dép | `B-COMP` |
| 1 | hơi | `I-COMP` |
| 2 | cứng. | `I-COMP` |
| 3 | đi | `B-COMP` |
| 4 | đau | `I-COMP` |
| 5 | mũi | `I-COMP` |
| 6 | chân | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 85. `train_003497`

- Domain: `app`
- Split: `train`

**Text gốc:**

> nói chung là  được  cơ mà đọc hơi nhanh và có thêm phần viết chữ cái để ghi nhớ sẽ tốt hơn

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý, khen, hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | nói | `O` |
| 1 | chung | `O` |
| 2 | là | `O` |
| 3 | được | `O` |
| 4 | cơ | `O` |
| 5 | mà | `O` |
| 6 | đọc | `O` |
| 7 | hơi | `O` |
| 8 | nhanh | `O` |
| 9 | và | `O` |
| 10 | có | `O` |
| 11 | thêm | `O` |
| 12 | phần | `O` |
| 13 | viết | `O` |
| 14 | chữ | `O` |
| 15 | cái | `O` |
| 16 | để | `O` |
| 17 | ghi | `O` |
| 18 | nhớ | `O` |
| 19 | sẽ | `O` |
| 20 | tốt | `O` |
| 21 | hơn | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 86. `train_003521`

- Domain: `app`
- Split: `train`

**Text gốc:**

> game khá hay nhưng bây giờ tôi muốn hoàn tiền lại nhưng sao tôi không hoàn tiền  được  ạ

**Spans:**

- #0 [64:85] `không hoàn tiền  được` label=`COMP`

**Reason:** Cụm 'không hoàn tiền  được' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | game | `O` |
| 1 | khá | `O` |
| 2 | hay | `O` |
| 3 | nhưng | `O` |
| 4 | bây | `O` |
| 5 | giờ | `O` |
| 6 | tôi | `O` |
| 7 | muốn | `O` |
| 8 | hoàn | `O` |
| 9 | tiền | `O` |
| 10 | lại | `O` |
| 11 | nhưng | `O` |
| 12 | sao | `O` |
| 13 | tôi | `O` |
| 14 | không | `B-COMP` |
| 15 | hoàn | `I-COMP` |
| 16 | tiền | `I-COMP` |
| 17 | được | `I-COMP` |
| 18 | ạ | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 87. `train_003563`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> chưa xài thử nên không biết công dụng nhưng mà ấn tượng đầu tiên là sản phẩm được bỏ vào hộp chắc chắn không như những  cửa hàng  khác nhìn siU xịn, giao hàng lâu chắc tại dịch còn lại được hết luôn, ai muốn thử nên mua

**Spans:**

- #0 [149:162] `giao hàng lâu` label=`COMP`

**Reason:** Cụm 'giao hàng lâu' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | chưa | `O` |
| 1 | xài | `O` |
| 2 | thử | `O` |
| 3 | nên | `O` |
| 4 | không | `O` |
| 5 | biết | `O` |
| 6 | công | `O` |
| 7 | dụng | `O` |
| 8 | nhưng | `O` |
| 9 | mà | `O` |
| 10 | ấn | `O` |
| 11 | tượng | `O` |
| 12 | đầu | `O` |
| 13 | tiên | `O` |
| 14 | là | `O` |
| 15 | sản | `O` |
| 16 | phẩm | `O` |
| 17 | được | `O` |
| 18 | bỏ | `O` |
| 19 | vào | `O` |
| 20 | hộp | `O` |
| 21 | chắc | `O` |
| 22 | chắn | `O` |
| 23 | không | `O` |
| 24 | như | `O` |
| 25 | những | `O` |
| 26 | cửa | `O` |
| 27 | hàng | `O` |
| 28 | khác | `O` |
| 29 | nhìn | `O` |
| 30 | siU | `O` |
| 31 | xịn, | `O` |
| 32 | giao | `B-COMP` |
| 33 | hàng | `I-COMP` |
| 34 | lâu | `I-COMP` |
| 35 | chắc | `O` |
| 36 | tại | `O` |
| 37 | dịch | `O` |
| 38 | còn | `O` |
| 39 | lại | `O` |
| 40 | được | `O` |
| 41 | hết | `O` |
| 42 | luôn, | `O` |
| 43 | ai | `O` |
| 44 | muốn | `O` |
| 45 | thử | `O` |
| 46 | nên | `O` |
| 47 | mua | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 88. `train_003566`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> giao không đúng mẫu,lần này mua quá thất vọng .

**Spans:**

- #0 [0:19] `giao không đúng mẫu` label=`COMP`
- #1 [32:45] `quá thất vọng` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | giao | `B-COMP` |
| 1 | không | `I-COMP` |
| 2 | đúng | `I-COMP` |
| 3 | mẫu,lần | `I-COMP` |
| 4 | này | `O` |
| 5 | mua | `O` |
| 6 | quá | `B-COMP` |
| 7 | thất | `I-COMP` |
| 8 | vọng | `I-COMP` |
| 9 | . | `O` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (70.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 89. `train_003589`

- Domain: `app`
- Split: `train`

**Text gốc:**

> tôi đánh giá  1star   ! game rất tệ khi tôi vừa tải về chơi thì tôi vô game , game load tới 50% rồi mà lại bị văn game và tôi vô lại một lần nữa thì nó cũng bị vậy !! tôi mong nhà phát hành sửa lỗi này.

**Spans:**

- #0 [107:118] `bị văn game` label=`COMP`

**Reason:** Cụm 'bị văn game' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tôi | `O` |
| 1 | đánh | `O` |
| 2 | giá | `O` |
| 3 | 1star | `O` |
| 4 | ! | `O` |
| 5 | game | `O` |
| 6 | rất | `O` |
| 7 | tệ | `O` |
| 8 | khi | `O` |
| 9 | tôi | `O` |
| 10 | vừa | `O` |
| 11 | tải | `O` |
| 12 | về | `O` |
| 13 | chơi | `O` |
| 14 | thì | `O` |
| 15 | tôi | `O` |
| 16 | vô | `O` |
| 17 | game | `O` |
| 18 | , | `O` |
| 19 | game | `O` |
| 20 | load | `O` |
| 21 | tới | `O` |
| 22 | 50% | `O` |
| 23 | rồi | `O` |
| 24 | mà | `O` |
| 25 | lại | `O` |
| 26 | bị | `B-COMP` |
| 27 | văn | `I-COMP` |
| 28 | game | `I-COMP` |
| 29 | và | `O` |
| 30 | tôi | `O` |
| 31 | vô | `O` |
| 32 | lại | `O` |
| 33 | một | `O` |
| 34 | lần | `O` |
| 35 | nữa | `O` |
| 36 | thì | `O` |
| 37 | nó | `O` |
| 38 | cũng | `O` |
| 39 | bị | `O` |
| 40 | vậy | `O` |
| 41 | !! | `O` |
| 42 | tôi | `O` |
| 43 | mong | `O` |
| 44 | nhà | `O` |
| 45 | phát | `O` |
| 46 | hành | `O` |
| 47 | sửa | `O` |
| 48 | lỗi | `O` |
| 49 | này. | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 90. `train_003822`

- Domain: `app`
- Split: `train`

**Text gốc:**

> game rất hay nhưng bản cập nhật gần đây có rất nhiều lỗi khi vào trận thì bị đứng không vào  được  lại phải kết nối lại khiến tôi bị trừ rất nhiều uy tín nếu game cứ như vậy chắc chẳng còn mấy người chơi nữa mong garena có cách khắc phục và khôi phục lại uy tín cho tôi cũng như những người cũng gặp lỗi như th... bài đánh giá đầy đủ

**Spans:**

- #0 [40:56] `có rất nhiều lỗi` label=`COMP`
- #1 [77:97] `đứng không vào  được` label=`COMP`
- #2 [130:153] `bị trừ rất nhiều uy tín` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | game | `O` |
| 1 | rất | `O` |
| 2 | hay | `O` |
| 3 | nhưng | `O` |
| 4 | bản | `O` |
| 5 | cập | `O` |
| 6 | nhật | `O` |
| 7 | gần | `O` |
| 8 | đây | `O` |
| 9 | có | `B-COMP` |
| 10 | rất | `I-COMP` |
| 11 | nhiều | `I-COMP` |
| 12 | lỗi | `I-COMP` |
| 13 | khi | `O` |
| 14 | vào | `O` |
| 15 | trận | `O` |
| 16 | thì | `O` |
| 17 | bị | `O` |
| 18 | đứng | `B-COMP` |
| 19 | không | `I-COMP` |
| 20 | vào | `I-COMP` |
| 21 | được | `I-COMP` |
| 22 | lại | `O` |
| 23 | phải | `O` |
| 24 | kết | `O` |
| 25 | nối | `O` |
| 26 | lại | `O` |
| 27 | khiến | `O` |
| 28 | tôi | `O` |
| 29 | bị | `B-COMP` |
| 30 | trừ | `I-COMP` |
| 31 | rất | `I-COMP` |
| 32 | nhiều | `I-COMP` |
| 33 | uy | `I-COMP` |
| 34 | tín | `I-COMP` |
| 35 | nếu | `O` |
| 36 | game | `O` |
| 37 | cứ | `O` |
| 38 | như | `O` |
| 39 | vậy | `O` |
| 40 | chắc | `O` |
| 41 | chẳng | `O` |
| 42 | còn | `O` |
| 43 | mấy | `O` |
| 44 | người | `O` |
| 45 | chơi | `O` |
| 46 | nữa | `O` |
| 47 | mong | `O` |
| 48 | garena | `O` |
| 49 | có | `O` |
| 50 | cách | `O` |
| 51 | khắc | `O` |
| 52 | phục | `O` |
| 53 | và | `O` |
| 54 | khôi | `O` |
| 55 | phục | `O` |
| 56 | lại | `O` |
| 57 | uy | `O` |
| 58 | tín | `O` |
| 59 | cho | `O` |
| 60 | tôi | `O` |
| 61 | cũng | `O` |
| 62 | như | `O` |
| 63 | những | `O` |
| 64 | người | `O` |
| 65 | cũng | `O` |
| 66 | gặp | `O` |
| 67 | lỗi | `O` |
| 68 | như | `O` |
| 69 | th... | `O` |
| 70 | bài | `O` |
| 71 | đánh | `O` |
| 72 | giá | `O` |
| 73 | đầy | `O` |
| 74 | đủ | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 91. `train_003877`

- Domain: `app`
- Split: `train`

**Text gốc:**

> chơi càng ngày càng khó. mà qua màng có mấy đồng. mà bán trợ giúp mất muốn chết. mua được 3 cái à. chơi biết bao nhiêu mang mới mua được. mất quá đi. xin khắc phục lại giùm.. không thôi mọi người sẽ chán và không chơi nữa.

**Spans:**

- #0 [0:23] `chơi càng ngày càng khó` label=`COMP`
- #1 [53:79] `bán trợ giúp mất muốn chết` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | chơi | `B-COMP` |
| 1 | càng | `I-COMP` |
| 2 | ngày | `I-COMP` |
| 3 | càng | `I-COMP` |
| 4 | khó. | `I-COMP` |
| 5 | mà | `O` |
| 6 | qua | `O` |
| 7 | màng | `O` |
| 8 | có | `O` |
| 9 | mấy | `O` |
| 10 | đồng. | `O` |
| 11 | mà | `O` |
| 12 | bán | `B-COMP` |
| 13 | trợ | `I-COMP` |
| 14 | giúp | `I-COMP` |
| 15 | mất | `I-COMP` |
| 16 | muốn | `I-COMP` |
| 17 | chết. | `I-COMP` |
| 18 | mua | `O` |
| 19 | được | `O` |
| 20 | 3 | `O` |
| 21 | cái | `O` |
| 22 | à. | `O` |
| 23 | chơi | `O` |
| 24 | biết | `O` |
| 25 | bao | `O` |
| 26 | nhiêu | `O` |
| 27 | mang | `O` |
| 28 | mới | `O` |
| 29 | mua | `O` |
| 30 | được. | `O` |
| 31 | mất | `O` |
| 32 | quá | `O` |
| 33 | đi. | `O` |
| 34 | xin | `O` |
| 35 | khắc | `O` |
| 36 | phục | `O` |
| 37 | lại | `O` |
| 38 | giùm.. | `O` |
| 39 | không | `O` |
| 40 | thôi | `O` |
| 41 | mọi | `O` |
| 42 | người | `O` |
| 43 | sẽ | `O` |
| 44 | chán | `O` |
| 45 | và | `O` |
| 46 | không | `O` |
| 47 | chơi | `O` |
| 48 | nữa. | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 92. `train_003930`

- Domain: `app`
- Split: `train`

**Text gốc:**

> game chơi hay. mình xin góp ý một số ý kiến. game nên tách biệt giữa 2 nhóm người chơi đó là chơi giả lập trên pc chơi với nhau và chơi trên điện thoại với nhau để tránh tình trạng thao tác xử lí trên pc tốt hơn. và game nên bỏ hoàn toàn tự ngắm. như thế giúp game thật hơn. cảm ơn game...

**Spans:**

- #0 [181:211] `thao tác xử lí trên pc tốt hơn` label=`COMP`

**Reason:** Cụm 'thao tác xử lí trên pc tốt hơn' nêu trực tiếp vấn đề chính.

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

## 93. `train_003971`

- Domain: `app`
- Split: `train`

**Text gốc:**

> game deo ca vao  được 

**Spans:**

- #0 [5:15] `deo ca vao` label=`COMP`

**Reason:** Cụm 'deo ca vao' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | game | `O` |
| 1 | deo | `B-COMP` |
| 2 | ca | `I-COMP` |
| 3 | vao | `I-COMP` |
| 4 | được | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 94. `train_004166`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> giao hàng không đúng  cỡ , tôi mua một m, một lồn giao 2 mình đề nghị đổi lại

**Spans:**

- #0 [0:24] `giao hàng không đúng  cỡ` label=`COMP`

**Reason:** Cụm 'giao hàng không đúng  cỡ' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | giao | `B-COMP` |
| 1 | hàng | `I-COMP` |
| 2 | không | `I-COMP` |
| 3 | đúng | `I-COMP` |
| 4 | cỡ | `I-COMP` |
| 5 | , | `O` |
| 6 | tôi | `O` |
| 7 | mua | `O` |
| 8 | một | `O` |
| 9 | m, | `O` |
| 10 | một | `O` |
| 11 | lồn | `O` |
| 12 | giao | `O` |
| 13 | 2 | `O` |
| 14 | mình | `O` |
| 15 | đề | `O` |
| 16 | nghị | `O` |
| 17 | đổi | `O` |
| 18 | lại | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 95. `train_004184`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> giao hàng hơi lâu á

**Spans:**

- #0 [0:19] `giao hàng hơi lâu á` label=`COMP`

**Reason:** Cụm 'giao hàng hơi lâu á' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | giao | `B-COMP` |
| 1 | hàng | `I-COMP` |
| 2 | hơi | `I-COMP` |
| 3 | lâu | `I-COMP` |
| 4 | á | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 96. `train_004204`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> áo  được .. cũng đẹp.. cũng vừa.. đặt màu hồng mà giao màu đỏ thấy là không thích không hài lòng rồi..!!

**Spans:**

- #0 [50:61] `giao màu đỏ` label=`COMP`
- #1 [70:100] `không thích không hài lòng rồi` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | áo | `O` |
| 1 | được | `O` |
| 2 | .. | `O` |
| 3 | cũng | `O` |
| 4 | đẹp.. | `O` |
| 5 | cũng | `O` |
| 6 | vừa.. | `O` |
| 7 | đặt | `O` |
| 8 | màu | `O` |
| 9 | hồng | `O` |
| 10 | mà | `O` |
| 11 | giao | `B-COMP` |
| 12 | màu | `I-COMP` |
| 13 | đỏ | `I-COMP` |
| 14 | thấy | `O` |
| 15 | là | `O` |
| 16 | không | `B-COMP` |
| 17 | thích | `I-COMP` |
| 18 | không | `I-COMP` |
| 19 | hài | `I-COMP` |
| 20 | lòng | `I-COMP` |
| 21 | rồi..!! | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 97. `train_004260`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> quần chất đẹp, nhưng bị chật. mà  cửa hàng  có mỗi chuyện gửi địa chỉ để khách đổi hàng cũng không làm được.

**Spans:**

- #0 [21:28] `bị chật` label=`COMP`
- #1 [58:107] `gửi địa chỉ để khách đổi hàng cũng không làm được` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

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
| 7 | cửa | `O` |
| 8 | hàng | `O` |
| 9 | có | `O` |
| 10 | mỗi | `O` |
| 11 | chuyện | `O` |
| 12 | gửi | `B-COMP` |
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

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 98. `train_004263`

- Domain: `app`
- Split: `train`

**Text gốc:**

>  không  quay ngang duoc dien thoai.

**Spans:**

- #0 [8:34] `quay ngang duoc dien thoai` label=`COMP`

**Reason:** Cụm 'quay ngang duoc dien thoai' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | không | `O` |
| 1 | quay | `B-COMP` |
| 2 | ngang | `I-COMP` |
| 3 | duoc | `I-COMP` |
| 4 | dien | `I-COMP` |
| 5 | thoai. | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (83.3%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 99. `train_004319`

- Domain: `app`
- Split: `train`

**Text gốc:**

> khuyên anh em đùng nên chơi trò này. vì tôi tải về xong thì nó hướng dẫn tôi xây các công trình. nó hướng dẫn tôi xây trạm liên lạc. xây xong nó bảo tôi nhấn vào một cái nút. nhấn xong nó đơ luôn. hỏi nó nói mình bị khoá tài khoản. nó đưa ra một cái lí do không thể nào chấp nhận được. nó nói do mình bấm không the... bài đánh giá đầy đủ

**Spans:**

- #0 [185:195] `nó đơ luôn` label=`COMP`
- #1 [213:230] `bị khoá tài khoản` label=`COMP`
- #2 [256:284] `không thể nào chấp nhận được` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | khuyên | `O` |
| 1 | anh | `O` |
| 2 | em | `O` |
| 3 | đùng | `O` |
| 4 | nên | `O` |
| 5 | chơi | `O` |
| 6 | trò | `O` |
| 7 | này. | `O` |
| 8 | vì | `O` |
| 9 | tôi | `O` |
| 10 | tải | `O` |
| 11 | về | `O` |
| 12 | xong | `O` |
| 13 | thì | `O` |
| 14 | nó | `O` |
| 15 | hướng | `O` |
| 16 | dẫn | `O` |
| 17 | tôi | `O` |
| 18 | xây | `O` |
| 19 | các | `O` |
| 20 | công | `O` |
| 21 | trình. | `O` |
| 22 | nó | `O` |
| 23 | hướng | `O` |
| 24 | dẫn | `O` |
| 25 | tôi | `O` |
| 26 | xây | `O` |
| 27 | trạm | `O` |
| 28 | liên | `O` |
| 29 | lạc. | `O` |
| 30 | xây | `O` |
| 31 | xong | `O` |
| 32 | nó | `O` |
| 33 | bảo | `O` |
| 34 | tôi | `O` |
| 35 | nhấn | `O` |
| 36 | vào | `O` |
| 37 | một | `O` |
| 38 | cái | `O` |
| 39 | nút. | `O` |
| 40 | nhấn | `O` |
| 41 | xong | `O` |
| 42 | nó | `B-COMP` |
| 43 | đơ | `I-COMP` |
| 44 | luôn. | `I-COMP` |
| 45 | hỏi | `O` |
| 46 | nó | `O` |
| 47 | nói | `O` |
| 48 | mình | `O` |
| 49 | bị | `B-COMP` |
| 50 | khoá | `I-COMP` |
| 51 | tài | `I-COMP` |
| 52 | khoản. | `I-COMP` |
| 53 | nó | `O` |
| 54 | đưa | `O` |
| 55 | ra | `O` |
| 56 | một | `O` |
| 57 | cái | `O` |
| 58 | lí | `O` |
| 59 | do | `O` |
| 60 | không | `B-COMP` |
| 61 | thể | `I-COMP` |
| 62 | nào | `I-COMP` |
| 63 | chấp | `I-COMP` |
| 64 | nhận | `I-COMP` |
| 65 | được. | `I-COMP` |
| 66 | nó | `O` |
| 67 | nói | `O` |
| 68 | do | `O` |
| 69 | mình | `O` |
| 70 | bấm | `O` |
| 71 | không | `O` |
| 72 | the... | `O` |
| 73 | bài | `O` |
| 74 | đánh | `O` |
| 75 | giá | `O` |
| 76 | đầy | `O` |
| 77 | đủ | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 100. `train_004363`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> quần đẹp nhưng  cỡ  lồn hơi ngắn

**Spans:**

- #0 [16:32] `cỡ  lồn hơi ngắn` label=`COMP`

**Reason:** Cụm 'cỡ  lồn hơi ngắn' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | quần | `O` |
| 1 | đẹp | `O` |
| 2 | nhưng | `O` |
| 3 | cỡ | `B-COMP` |
| 4 | lồn | `I-COMP` |
| 5 | hơi | `I-COMP` |
| 6 | ngắn | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---
