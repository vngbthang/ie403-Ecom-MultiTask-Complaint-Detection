# Needs Review - Annotation Sample Train 100 V2

## `train_000054`

- Domain: `app`
- Split: `train`

**Text gốc:**

> tôi rất thích game này nhưng càng lúc cấu hình game càng nặng, thật sự rất lag luôn, máy bên tôi lúc nào cũng trễ hơn bên đồng đội vài giây, có khi còn bị đứng hình hay cứ bị chạy giật lùi do kết nối mạng nữa. mong game có cách khắc phục chứ game càng lúc càng nặng thì người không có điều kiện đổi m... bài đánh giá đầy đủ

**Spans hiện tại:**
- #0 [29:61] `càng lúc cấu hình game càng nặng` label=`COMP`
- #1 [71:83] `rất lag luôn` label=`COMP`
- #2 [110:139] `trễ hơn bên đồng đội vài giây` label=`COMP`
- #3 [152:164] `bị đứng hình` label=`COMP`
- #4 [175:188] `chạy giật lùi` label=`COMP`

**Warning reasons:**
- nhiều hơn 4 spans (5)

**Token/BIO hiện tại:**

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

**Action:** KEEP / FIX / DROP

**Suggested fixed spans:**

**Notes:**

---

## `train_000747`

- Domain: `app`
- Split: `train`

**Text gốc:**

> không có khống chế phần tải về nội dung khoá học. bé cứ bấm vào tải về quá trời làm máy đơ luôn. cả phần chơi sticker nữa. hov gì  thì không học cứ bấm vào phần chọn sticker nghịch hoài.

**Spans hiện tại:**
- #0 [0:48] `không có khống chế phần tải về nội dung khoá học` label=`COMP`
- #1 [84:95] `máy đơ luôn` label=`COMP`
- #2 [156:185] `phần chọn sticker nghịch hoài` label=`COMP`

**Warning reasons:**
- span #0 bắt đầu từ đầu text và dài > 8 tokens

**Token/BIO hiện tại:**

| idx | token | tag |
|---:|---|---|
| 0 | không | `B-COMP` |
| 1 | có | `I-COMP` |
| 2 | khống | `I-COMP` |
| 3 | chế | `I-COMP` |
| 4 | phần | `I-COMP` |
| 5 | tải | `I-COMP` |
| 6 | về | `I-COMP` |
| 7 | nội | `I-COMP` |
| 8 | dung | `I-COMP` |
| 9 | khoá | `I-COMP` |
| 10 | học. | `I-COMP` |
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

**Action:** KEEP / FIX / DROP

**Suggested fixed spans:**

**Notes:**

---

## `train_001926`

- Domain: `app`
- Split: `train`

**Text gốc:**

> aP có một số nhược điểm: thứ một là nhiều bài hạn chế, tìm không thấy. thứ 2 là việc aP tự động đăng nhập tài khoản zalo mỗi lần truy cập là rất phiền. cuối cùng là khi tôi dùng các ứng dụng chỉnh video như kinemaster, inshot, viva video ... muốn chèn bài hát đã tải ở zing về nhưng tìm không có, chỉ có ... bài đánh giá đầy đủ

**Spans hiện tại:**
- #0 [36:69] `nhiều bài hạn chế, tìm không thấy` label=`COMP`
- #1 [85:150] `aP tự động đăng nhập tài khoản zalo mỗi lần truy cập là rất phiền` label=`COMP`
- #2 [283:295] `tìm không có` label=`COMP`

**Warning reasons:**
- span #1 dài >= 15 tokens (15)

**Token/BIO hiện tại:**

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

**Action:** KEEP / FIX / DROP

**Suggested fixed spans:**

**Notes:**

---

## `train_003290`

- Domain: `app`
- Split: `train`

**Text gốc:**

> xin nhà phát hành game cho thêm stop ở bà rịa - vũng tàu, thành phố bà rịa, đương số 43, ấp đông, xã hoà long nha. nhiều khi muốn chơi nhưng cứ vô là không có gym với stop nên buồn

**Spans hiện tại:**
- None

**Warning reasons:**
- spans=[] nhưng cls_label=1

**Token/BIO hiện tại:**

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
| 35 | không | `O` |
| 36 | có | `O` |
| 37 | gym | `O` |
| 38 | với | `O` |
| 39 | stop | `O` |
| 40 | nên | `O` |
| 41 | buồn | `O` |

**Action:** KEEP / FIX / DROP

**Suggested fixed spans:**

**Notes:**

---
