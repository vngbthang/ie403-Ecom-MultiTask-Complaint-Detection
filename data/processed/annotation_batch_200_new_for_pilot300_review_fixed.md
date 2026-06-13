# Annotation Review - Sample Train 20

Manual checklist for reviewing AI-assisted complaint span annotations.

## 1. `train_003601`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> kem nền có mùi cồn nhiều mà còn nồng nặc nữa, tets thử lên tay thì kem dạng lỏng và tets bị lộ vân kem và khô. nắp thì hờ hừng không khít nói chung là rất luồn không biết có phải hàng chính hãng k. thực sự là rất buồn 😥😥😢😢😢

**Spans:**

- #0 [0:44] `kem nền có mùi cồn nhiều mà còn nồng nặc nữa` label=`COMP`
- #1 [111:196] `nắp thì hờ hừng không khít nói chung là rất luồn không biết có phải hàng chính hãng k` label=`COMP`
- #2 [198:223] `thực sự là rất buồn 😥😥😢😢😢` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | kem | `B-COMP` |
| 1 | nền | `I-COMP` |
| 2 | có | `I-COMP` |
| 3 | mùi | `I-COMP` |
| 4 | cồn | `I-COMP` |
| 5 | nhiều | `I-COMP` |
| 6 | mà | `I-COMP` |
| 7 | còn | `I-COMP` |
| 8 | nồng | `I-COMP` |
| 9 | nặc | `I-COMP` |
| 10 | nữa, | `I-COMP` |
| 11 | tets | `O` |
| 12 | thử | `O` |
| 13 | lên | `O` |
| 14 | tay | `O` |
| 15 | thì | `O` |
| 16 | kem | `O` |
| 17 | dạng | `O` |
| 18 | lỏng | `O` |
| 19 | và | `O` |
| 20 | tets | `O` |
| 21 | bị | `O` |
| 22 | lộ | `O` |
| 23 | vân | `O` |
| 24 | kem | `O` |
| 25 | và | `O` |
| 26 | khô. | `O` |
| 27 | nắp | `B-COMP` |
| 28 | thì | `I-COMP` |
| 29 | hờ | `I-COMP` |
| 30 | hừng | `I-COMP` |
| 31 | không | `I-COMP` |
| 32 | khít | `I-COMP` |
| 33 | nói | `I-COMP` |
| 34 | chung | `I-COMP` |
| 35 | là | `I-COMP` |
| 36 | rất | `I-COMP` |
| 37 | luồn | `I-COMP` |
| 38 | không | `I-COMP` |
| 39 | biết | `I-COMP` |
| 40 | có | `I-COMP` |
| 41 | phải | `I-COMP` |
| 42 | hàng | `I-COMP` |
| 43 | chính | `I-COMP` |
| 44 | hãng | `I-COMP` |
| 45 | k. | `I-COMP` |
| 46 | thực | `B-COMP` |
| 47 | sự | `I-COMP` |
| 48 | là | `I-COMP` |
| 49 | rất | `I-COMP` |
| 50 | buồn | `I-COMP` |
| 51 | 😥😥😢😢😢 | `I-COMP` |

**Heuristic warnings:**

- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- span #1 quá dài (19 tokens >= 15)
- tỉ lệ COMP token > 60% (69.2%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 2. `train_000426`

- Domain: `app`
- Split: `train`

**Text gốc:**

> nạp 1$ tặng vàng gì gì dau? hình ảnh trong game còn lag màu vào nó một cục màu ngay nhân vật,game chơi một lát lại diS ra giao diện đăng nhập,  quả người cáo lừa đảo... làm eo  được  thì đừng  quả người cáo

**Spans:**

- #0 [52:92] `lag màu vào nó một cục màu ngay nhân vật` label=`COMP`
- #1 [144:165] `quả người cáo lừa đảo` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | nạp | `O` |
| 1 | 1$ | `O` |
| 2 | tặng | `O` |
| 3 | vàng | `O` |
| 4 | gì | `O` |
| 5 | gì | `O` |
| 6 | dau? | `O` |
| 7 | hình | `O` |
| 8 | ảnh | `O` |
| 9 | trong | `O` |
| 10 | game | `O` |
| 11 | còn | `O` |
| 12 | lag | `B-COMP` |
| 13 | màu | `I-COMP` |
| 14 | vào | `I-COMP` |
| 15 | nó | `I-COMP` |
| 16 | một | `I-COMP` |
| 17 | cục | `I-COMP` |
| 18 | màu | `I-COMP` |
| 19 | ngay | `I-COMP` |
| 20 | nhân | `I-COMP` |
| 21 | vật,game | `I-COMP` |
| 22 | chơi | `O` |
| 23 | một | `O` |
| 24 | lát | `O` |
| 25 | lại | `O` |
| 26 | diS | `O` |
| 27 | ra | `O` |
| 28 | giao | `O` |
| 29 | diện | `O` |
| 30 | đăng | `O` |
| 31 | nhập, | `O` |
| 32 | quả | `B-COMP` |
| 33 | người | `I-COMP` |
| 34 | cáo | `I-COMP` |
| 35 | lừa | `I-COMP` |
| 36 | đảo... | `I-COMP` |
| 37 | làm | `O` |
| 38 | eo | `O` |
| 39 | được | `O` |
| 40 | thì | `O` |
| 41 | đừng | `O` |
| 42 | quả | `O` |
| 43 | người | `O` |
| 44 | cáo | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 3. `train_002332`

- Domain: `app`
- Split: `train`

**Text gốc:**

> gọi xe cứ bị huỷ chuyến rất mất thời gian.. có lần tài xế đi rồi.. lại gọi điện thoại bảo mình huỷ chuyến.. chưa kịp huỷ đang tìm grab để đi thì cứ gọi đến giục huỷ chuyến đi. rất mất thời gian và bất tiện. đang lúc gấp gáp cứ bị huỷ chuyến liên tục rất là bực mình..

**Spans:**

- #0 [0:41] `gọi xe cứ bị huỷ chuyến rất mất thời gian` label=`COMP`
- #1 [67:105] `lại gọi điện thoại bảo mình huỷ chuyến` label=`COMP`
- #2 [108:174] `chưa kịp huỷ đang tìm grab để đi thì cứ gọi đến giục huỷ chuyến đi` label=`COMP`
- #3 [176:205] `rất mất thời gian và bất tiện` label=`COMP`
- #4 [207:265] `đang lúc gấp gáp cứ bị huỷ chuyến liên tục rất là bực mình` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | gọi | `B-COMP` |
| 1 | xe | `I-COMP` |
| 2 | cứ | `I-COMP` |
| 3 | bị | `I-COMP` |
| 4 | huỷ | `I-COMP` |
| 5 | chuyến | `I-COMP` |
| 6 | rất | `I-COMP` |
| 7 | mất | `I-COMP` |
| 8 | thời | `I-COMP` |
| 9 | gian.. | `I-COMP` |
| 10 | có | `O` |
| 11 | lần | `O` |
| 12 | tài | `O` |
| 13 | xế | `O` |
| 14 | đi | `O` |
| 15 | rồi.. | `O` |
| 16 | lại | `B-COMP` |
| 17 | gọi | `I-COMP` |
| 18 | điện | `I-COMP` |
| 19 | thoại | `I-COMP` |
| 20 | bảo | `I-COMP` |
| 21 | mình | `I-COMP` |
| 22 | huỷ | `I-COMP` |
| 23 | chuyến.. | `I-COMP` |
| 24 | chưa | `B-COMP` |
| 25 | kịp | `I-COMP` |
| 26 | huỷ | `I-COMP` |
| 27 | đang | `I-COMP` |
| 28 | tìm | `I-COMP` |
| 29 | grab | `I-COMP` |
| 30 | để | `I-COMP` |
| 31 | đi | `I-COMP` |
| 32 | thì | `I-COMP` |
| 33 | cứ | `I-COMP` |
| 34 | gọi | `I-COMP` |
| 35 | đến | `I-COMP` |
| 36 | giục | `I-COMP` |
| 37 | huỷ | `I-COMP` |
| 38 | chuyến | `I-COMP` |
| 39 | đi. | `I-COMP` |
| 40 | rất | `B-COMP` |
| 41 | mất | `I-COMP` |
| 42 | thời | `I-COMP` |
| 43 | gian | `I-COMP` |
| 44 | và | `I-COMP` |
| 45 | bất | `I-COMP` |
| 46 | tiện. | `I-COMP` |
| 47 | đang | `B-COMP` |
| 48 | lúc | `I-COMP` |
| 49 | gấp | `I-COMP` |
| 50 | gáp | `I-COMP` |
| 51 | cứ | `I-COMP` |
| 52 | bị | `I-COMP` |
| 53 | huỷ | `I-COMP` |
| 54 | chuyến | `I-COMP` |
| 55 | liên | `I-COMP` |
| 56 | tục | `I-COMP` |
| 57 | rất | `I-COMP` |
| 58 | là | `I-COMP` |
| 59 | bực | `I-COMP` |
| 60 | mình.. | `I-COMP` |

**Heuristic warnings:**

- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- span #2 quá dài (16 tokens >= 15)
- record có nhiều hơn 4 spans (5 spans)
- tỉ lệ COMP token > 60% (90.2%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 4. `train_000229`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> không hợp với da mình, không hiệu  quả 

**Spans:**

- #0 [0:21] `không hợp với da mình` label=`COMP`
- #1 [23:38] `không hiệu  quả` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | không | `B-COMP` |
| 1 | hợp | `I-COMP` |
| 2 | với | `I-COMP` |
| 3 | da | `I-COMP` |
| 4 | mình, | `I-COMP` |
| 5 | không | `B-COMP` |
| 6 | hiệu | `I-COMP` |
| 7 | quả | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 5. `train_001369`

- Domain: `app`
- Split: `train`

**Text gốc:**

> tôi rất thích tựa game này nhưng tôi không hài lòng với việc mỗi khi cập nhật oby mới thì hãy đặt chính xác số giờ hết bảo trì chứ cứ nói lúc 11h đến 6h30 sau đó lại nói là 12h đến 7h30 rồi tiếp đó thì lại nói là 12h đến 8h30 tôi cảm thấy khá bực mình về chuyện này mong admin giúp đỡ và tôi cũng nghỉ là nê... bài đánh giá đầy đủ

**Spans:**

- #0 [33:307] `tôi không hài lòng với việc mỗi khi cập nhật oby mới thì hãy đặt chính xác số giờ hết bảo trì chứ cứ nói lúc 11h đến 6h30 sau đó lại nói là 12h đến 7h30 rồi tiếp đó thì lại nói là 12h đến 8h30 tôi cảm thấy khá bực mình về chuyện này mong admin giúp đỡ và tôi cũng nghỉ là nê` label=`COMP`

**Reason:** Cụm 'tôi không hài lòng với việc mỗi khi cập nhật oby mới thì hãy đặt chính xác số giờ hết bảo trì chứ cứ nói lúc 11h đến 6h30 sau đó lại nói là 12h đến 7h30 rồi tiếp đó thì lại nói là 12h đến 8h30 tôi cảm thấy khá bực mình về chuyện này mong admin giúp đỡ và tôi cũng nghỉ là nê' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tôi | `O` |
| 1 | rất | `O` |
| 2 | thích | `O` |
| 3 | tựa | `O` |
| 4 | game | `O` |
| 5 | này | `O` |
| 6 | nhưng | `O` |
| 7 | tôi | `B-COMP` |
| 8 | không | `I-COMP` |
| 9 | hài | `I-COMP` |
| 10 | lòng | `I-COMP` |
| 11 | với | `I-COMP` |
| 12 | việc | `I-COMP` |
| 13 | mỗi | `I-COMP` |
| 14 | khi | `I-COMP` |
| 15 | cập | `I-COMP` |
| 16 | nhật | `I-COMP` |
| 17 | oby | `I-COMP` |
| 18 | mới | `I-COMP` |
| 19 | thì | `I-COMP` |
| 20 | hãy | `I-COMP` |
| 21 | đặt | `I-COMP` |
| 22 | chính | `I-COMP` |
| 23 | xác | `I-COMP` |
| 24 | số | `I-COMP` |
| 25 | giờ | `I-COMP` |
| 26 | hết | `I-COMP` |
| 27 | bảo | `I-COMP` |
| 28 | trì | `I-COMP` |
| 29 | chứ | `I-COMP` |
| 30 | cứ | `I-COMP` |
| 31 | nói | `I-COMP` |
| 32 | lúc | `I-COMP` |
| 33 | 11h | `I-COMP` |
| 34 | đến | `I-COMP` |
| 35 | 6h30 | `I-COMP` |
| 36 | sau | `I-COMP` |
| 37 | đó | `I-COMP` |
| 38 | lại | `I-COMP` |
| 39 | nói | `I-COMP` |
| 40 | là | `I-COMP` |
| 41 | 12h | `I-COMP` |
| 42 | đến | `I-COMP` |
| 43 | 7h30 | `I-COMP` |
| 44 | rồi | `I-COMP` |
| 45 | tiếp | `I-COMP` |
| 46 | đó | `I-COMP` |
| 47 | thì | `I-COMP` |
| 48 | lại | `I-COMP` |
| 49 | nói | `I-COMP` |
| 50 | là | `I-COMP` |
| 51 | 12h | `I-COMP` |
| 52 | đến | `I-COMP` |
| 53 | 8h30 | `I-COMP` |
| 54 | tôi | `I-COMP` |
| 55 | cảm | `I-COMP` |
| 56 | thấy | `I-COMP` |
| 57 | khá | `I-COMP` |
| 58 | bực | `I-COMP` |
| 59 | mình | `I-COMP` |
| 60 | về | `I-COMP` |
| 61 | chuyện | `I-COMP` |
| 62 | này | `I-COMP` |
| 63 | mong | `I-COMP` |
| 64 | admin | `I-COMP` |
| 65 | giúp | `I-COMP` |
| 66 | đỡ | `I-COMP` |
| 67 | và | `I-COMP` |
| 68 | tôi | `I-COMP` |
| 69 | cũng | `I-COMP` |
| 70 | nghỉ | `I-COMP` |
| 71 | là | `I-COMP` |
| 72 | nê... | `I-COMP` |
| 73 | bài | `O` |
| 74 | đánh | `O` |
| 75 | giá | `O` |
| 76 | đầy | `O` |
| 77 | đủ | `O` |

**Heuristic warnings:**

- span #0 quá dài (66 tokens >= 15)
- tỉ lệ COMP token > 60% (84.6%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 6. `train_001734`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> bị rách ở đầu

**Spans:**

- #0 [0:13] `bị rách ở đầu` label=`COMP`

**Reason:** Cụm 'bị rách ở đầu' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | bị | `B-COMP` |
| 1 | rách | `I-COMP` |
| 2 | ở | `I-COMP` |
| 3 | đầu | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 7. `train_002823`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> mình mua 2 combo một mua sữa rửa mặt để tặng dầu tẩy trang mà chỉ có sữa rửa mặt không có dầu tẩy trang combo2 mua nước tẩy trang để tặng sữa rửa mặt xanh dương mà chỉ có nước tẩy trang bông tẩy trang lần đầu mua mà không có tặng gì cả, thất vọng  cửa hàng  quá đặt lúc 27.3

**Spans:**

- #0 [216:235] `không có tặng gì cả` label=`COMP`
- #1 [237:272] `thất vọng  cửa hàng  quá đặt lúc 27` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mình | `O` |
| 1 | mua | `O` |
| 2 | 2 | `O` |
| 3 | combo | `O` |
| 4 | một | `O` |
| 5 | mua | `O` |
| 6 | sữa | `O` |
| 7 | rửa | `O` |
| 8 | mặt | `O` |
| 9 | để | `O` |
| 10 | tặng | `O` |
| 11 | dầu | `O` |
| 12 | tẩy | `O` |
| 13 | trang | `O` |
| 14 | mà | `O` |
| 15 | chỉ | `O` |
| 16 | có | `O` |
| 17 | sữa | `O` |
| 18 | rửa | `O` |
| 19 | mặt | `O` |
| 20 | không | `O` |
| 21 | có | `O` |
| 22 | dầu | `O` |
| 23 | tẩy | `O` |
| 24 | trang | `O` |
| 25 | combo2 | `O` |
| 26 | mua | `O` |
| 27 | nước | `O` |
| 28 | tẩy | `O` |
| 29 | trang | `O` |
| 30 | để | `O` |
| 31 | tặng | `O` |
| 32 | sữa | `O` |
| 33 | rửa | `O` |
| 34 | mặt | `O` |
| 35 | xanh | `O` |
| 36 | dương | `O` |
| 37 | mà | `O` |
| 38 | chỉ | `O` |
| 39 | có | `O` |
| 40 | nước | `O` |
| 41 | tẩy | `O` |
| 42 | trang | `O` |
| 43 | bông | `O` |
| 44 | tẩy | `O` |
| 45 | trang | `O` |
| 46 | lần | `O` |
| 47 | đầu | `O` |
| 48 | mua | `O` |
| 49 | mà | `O` |
| 50 | không | `B-COMP` |
| 51 | có | `I-COMP` |
| 52 | tặng | `I-COMP` |
| 53 | gì | `I-COMP` |
| 54 | cả, | `I-COMP` |
| 55 | thất | `B-COMP` |
| 56 | vọng | `I-COMP` |
| 57 | cửa | `I-COMP` |
| 58 | hàng | `I-COMP` |
| 59 | quá | `I-COMP` |
| 60 | đặt | `I-COMP` |
| 61 | lúc | `I-COMP` |
| 62 | 27.3 | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 8. `train_003779`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> không phải hàng mới. hàng lướt, mặt bị xước trước và sau

**Spans:**

- #0 [32:56] `mặt bị xước trước và sau` label=`COMP`

**Reason:** Cụm 'mặt bị xước trước và sau' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | không | `O` |
| 1 | phải | `O` |
| 2 | hàng | `O` |
| 3 | mới. | `O` |
| 4 | hàng | `O` |
| 5 | lướt, | `O` |
| 6 | mặt | `B-COMP` |
| 7 | bị | `I-COMP` |
| 8 | xước | `I-COMP` |
| 9 | trước | `I-COMP` |
| 10 | và | `I-COMP` |
| 11 | sau | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 9. `train_003010`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đầm hơi mỏng, mặc vào cũng đẹp nhưng váy hơi bị phồng nhìn như bà bầu 😶

**Spans:**

- #0 [0:12] `đầm hơi mỏng` label=`COMP`

**Reason:** Cụm 'đầm hơi mỏng' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đầm | `B-COMP` |
| 1 | hơi | `I-COMP` |
| 2 | mỏng, | `I-COMP` |
| 3 | mặc | `O` |
| 4 | vào | `O` |
| 5 | cũng | `O` |
| 6 | đẹp | `O` |
| 7 | nhưng | `O` |
| 8 | váy | `O` |
| 9 | hơi | `O` |
| 10 | bị | `O` |
| 11 | phồng | `O` |
| 12 | nhìn | `O` |
| 13 | như | `O` |
| 14 | bà | `O` |
| 15 | bầu | `O` |
| 16 | 😶 | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 10. `train_002870`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> tang một thung bia ma không tang sao

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tang | `O` |
| 1 | một | `O` |
| 2 | thung | `O` |
| 3 | bia | `O` |
| 4 | ma | `O` |
| 5 | không | `O` |
| 6 | tang | `O` |
| 7 | sao | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 11. `train_003062`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> màu rất vừa ý. độ bám tốt, cảm giác dính hơi khó chịu.

**Spans:**

- #0 [27:53] `cảm giác dính hơi khó chịu` label=`COMP`

**Reason:** Cụm 'cảm giác dính hơi khó chịu' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | màu | `O` |
| 1 | rất | `O` |
| 2 | vừa | `O` |
| 3 | ý. | `O` |
| 4 | độ | `O` |
| 5 | bám | `O` |
| 6 | tốt, | `O` |
| 7 | cảm | `B-COMP` |
| 8 | giác | `I-COMP` |
| 9 | dính | `I-COMP` |
| 10 | hơi | `I-COMP` |
| 11 | khó | `I-COMP` |
| 12 | chịu. | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 12. `train_000561`

- Domain: `app`
- Split: `train`

**Text gốc:**

> đây là từ điển nhật - việt chứ đâu phải từ điển nhật - anh đâu mà chỉ có tuếng anh khi tra vậy? tôi thấy rất tiếc khi cho   1star   nhưng thật sự mà nói điều này không phù hợp cho người không giỏi tiếng anh. rất mong khắc phục.

**Spans:**

- #0 [0:94] `đây là từ điển nhật - việt chứ đâu phải từ điển nhật - anh đâu mà chỉ có tuếng anh khi tra vậy` label=`COMP`
- #1 [149:206] `nói điều này không phù hợp cho người không giỏi tiếng anh` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đây | `B-COMP` |
| 1 | là | `I-COMP` |
| 2 | từ | `I-COMP` |
| 3 | điển | `I-COMP` |
| 4 | nhật | `I-COMP` |
| 5 | - | `I-COMP` |
| 6 | việt | `I-COMP` |
| 7 | chứ | `I-COMP` |
| 8 | đâu | `I-COMP` |
| 9 | phải | `I-COMP` |
| 10 | từ | `I-COMP` |
| 11 | điển | `I-COMP` |
| 12 | nhật | `I-COMP` |
| 13 | - | `I-COMP` |
| 14 | anh | `I-COMP` |
| 15 | đâu | `I-COMP` |
| 16 | mà | `I-COMP` |
| 17 | chỉ | `I-COMP` |
| 18 | có | `I-COMP` |
| 19 | tuếng | `I-COMP` |
| 20 | anh | `I-COMP` |
| 21 | khi | `I-COMP` |
| 22 | tra | `I-COMP` |
| 23 | vậy? | `I-COMP` |
| 24 | tôi | `O` |
| 25 | thấy | `O` |
| 26 | rất | `O` |
| 27 | tiếc | `O` |
| 28 | khi | `O` |
| 29 | cho | `O` |
| 30 | 1star | `O` |
| 31 | nhưng | `O` |
| 32 | thật | `O` |
| 33 | sự | `O` |
| 34 | mà | `O` |
| 35 | nói | `B-COMP` |
| 36 | điều | `I-COMP` |
| 37 | này | `I-COMP` |
| 38 | không | `I-COMP` |
| 39 | phù | `I-COMP` |
| 40 | hợp | `I-COMP` |
| 41 | cho | `I-COMP` |
| 42 | người | `I-COMP` |
| 43 | không | `I-COMP` |
| 44 | giỏi | `I-COMP` |
| 45 | tiếng | `I-COMP` |
| 46 | anh. | `I-COMP` |
| 47 | rất | `O` |
| 48 | mong | `O` |
| 49 | khắc | `O` |
| 50 | phục. | `O` |

**Heuristic warnings:**

- span #0 quá dài (24 tokens >= 15)
- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (70.6%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 13. `train_004130`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> không dung mau hình mẫu

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | không | `O` |
| 1 | dung | `O` |
| 2 | mau | `O` |
| 3 | hình | `O` |
| 4 | mẫu | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 14. `train_003624`

- Domain: `app`
- Split: `train`

**Text gốc:**

> game cứ lặp đi lặp lại theo vòng tuần hoàn, cứ ra event qài, event là nạp nạp nạp, chán, đứng top mà thấy chán, vui lúc đầu nhưng càng chơi càng chán vì chả còn gì mới lạ để chơi . quá tệ

**Spans:**

- #0 [83:87] `chán` label=`COMP`
- #1 [101:110] `thấy chán` label=`COMP`
- #2 [130:178] `càng chơi càng chán vì chả còn gì mới lạ để chơi` label=`COMP`
- #3 [181:187] `quá tệ` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | game | `O` |
| 1 | cứ | `O` |
| 2 | lặp | `O` |
| 3 | đi | `O` |
| 4 | lặp | `O` |
| 5 | lại | `O` |
| 6 | theo | `O` |
| 7 | vòng | `O` |
| 8 | tuần | `O` |
| 9 | hoàn, | `O` |
| 10 | cứ | `O` |
| 11 | ra | `O` |
| 12 | event | `O` |
| 13 | qài, | `O` |
| 14 | event | `O` |
| 15 | là | `O` |
| 16 | nạp | `O` |
| 17 | nạp | `O` |
| 18 | nạp, | `O` |
| 19 | chán, | `B-COMP` |
| 20 | đứng | `O` |
| 21 | top | `O` |
| 22 | mà | `O` |
| 23 | thấy | `B-COMP` |
| 24 | chán, | `I-COMP` |
| 25 | vui | `O` |
| 26 | lúc | `O` |
| 27 | đầu | `O` |
| 28 | nhưng | `O` |
| 29 | càng | `B-COMP` |
| 30 | chơi | `I-COMP` |
| 31 | càng | `I-COMP` |
| 32 | chán | `I-COMP` |
| 33 | vì | `I-COMP` |
| 34 | chả | `I-COMP` |
| 35 | còn | `I-COMP` |
| 36 | gì | `I-COMP` |
| 37 | mới | `I-COMP` |
| 38 | lạ | `I-COMP` |
| 39 | để | `I-COMP` |
| 40 | chơi | `I-COMP` |
| 41 | . | `O` |
| 42 | quá | `B-COMP` |
| 43 | tệ | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 15. `train_003574`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> hàng  được  nhưng dải hơi mỏng nhưng được lắm đẹp như hình... nhưng mà mình thất vọng về shiper của lazada quá kêu giao tận nhà mà không khi nào

**Spans:**

- #0 [0:58] `hàng  được  nhưng dải hơi mỏng nhưng được lắm đẹp như hình` label=`COMP`
- #1 [71:144] `mình thất vọng về shiper của lazada quá kêu giao tận nhà mà không khi nào` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hàng | `B-COMP` |
| 1 | được | `I-COMP` |
| 2 | nhưng | `I-COMP` |
| 3 | dải | `I-COMP` |
| 4 | hơi | `I-COMP` |
| 5 | mỏng | `I-COMP` |
| 6 | nhưng | `I-COMP` |
| 7 | được | `I-COMP` |
| 8 | lắm | `I-COMP` |
| 9 | đẹp | `I-COMP` |
| 10 | như | `I-COMP` |
| 11 | hình... | `I-COMP` |
| 12 | nhưng | `O` |
| 13 | mà | `O` |
| 14 | mình | `B-COMP` |
| 15 | thất | `I-COMP` |
| 16 | vọng | `I-COMP` |
| 17 | về | `I-COMP` |
| 18 | shiper | `I-COMP` |
| 19 | của | `I-COMP` |
| 20 | lazada | `I-COMP` |
| 21 | quá | `I-COMP` |
| 22 | kêu | `I-COMP` |
| 23 | giao | `I-COMP` |
| 24 | tận | `I-COMP` |
| 25 | nhà | `I-COMP` |
| 26 | mà | `I-COMP` |
| 27 | không | `I-COMP` |
| 28 | khi | `I-COMP` |
| 29 | nào | `I-COMP` |

**Heuristic warnings:**

- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- span #1 quá dài (16 tokens >= 15)
- tỉ lệ COMP token > 60% (93.3%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 16. `train_002643`

- Domain: `app`
- Split: `train`

**Text gốc:**

> tôi sử dụng dịch vụ nạp tiền điện thoại qua ví điện tử grabpay. tôi có thao tác mua mã thẻ cào vieTel mệnh giá 30.000d và nhận  được  yêu cầu chờ xử lý trong vòng 1h. tôi vui vẻ chờ đợi nhưng 3h sau vẫn không nhận được mã thẻ nạp cũng không có hoàn trả vào ví điện tử grabpay của tôi. tôi có gửi email m... bài đánh giá đầy đủ

**Spans:**

- #0 [192:283] `3h sau vẫn không nhận được mã thẻ nạp cũng không có hoàn trả vào ví điện tử grabpay của tôi` label=`COMP`

**Reason:** Cụm '3h sau vẫn không nhận được mã thẻ nạp cũng không có hoàn trả vào ví điện tử grabpay của tôi' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tôi | `O` |
| 1 | sử | `O` |
| 2 | dụng | `O` |
| 3 | dịch | `O` |
| 4 | vụ | `O` |
| 5 | nạp | `O` |
| 6 | tiền | `O` |
| 7 | điện | `O` |
| 8 | thoại | `O` |
| 9 | qua | `O` |
| 10 | ví | `O` |
| 11 | điện | `O` |
| 12 | tử | `O` |
| 13 | grabpay. | `O` |
| 14 | tôi | `O` |
| 15 | có | `O` |
| 16 | thao | `O` |
| 17 | tác | `O` |
| 18 | mua | `O` |
| 19 | mã | `O` |
| 20 | thẻ | `O` |
| 21 | cào | `O` |
| 22 | vieTel | `O` |
| 23 | mệnh | `O` |
| 24 | giá | `O` |
| 25 | 30.000d | `O` |
| 26 | và | `O` |
| 27 | nhận | `O` |
| 28 | được | `O` |
| 29 | yêu | `O` |
| 30 | cầu | `O` |
| 31 | chờ | `O` |
| 32 | xử | `O` |
| 33 | lý | `O` |
| 34 | trong | `O` |
| 35 | vòng | `O` |
| 36 | 1h. | `O` |
| 37 | tôi | `O` |
| 38 | vui | `O` |
| 39 | vẻ | `O` |
| 40 | chờ | `O` |
| 41 | đợi | `O` |
| 42 | nhưng | `O` |
| 43 | 3h | `B-COMP` |
| 44 | sau | `I-COMP` |
| 45 | vẫn | `I-COMP` |
| 46 | không | `I-COMP` |
| 47 | nhận | `I-COMP` |
| 48 | được | `I-COMP` |
| 49 | mã | `I-COMP` |
| 50 | thẻ | `I-COMP` |
| 51 | nạp | `I-COMP` |
| 52 | cũng | `I-COMP` |
| 53 | không | `I-COMP` |
| 54 | có | `I-COMP` |
| 55 | hoàn | `I-COMP` |
| 56 | trả | `I-COMP` |
| 57 | vào | `I-COMP` |
| 58 | ví | `I-COMP` |
| 59 | điện | `I-COMP` |
| 60 | tử | `I-COMP` |
| 61 | grabpay | `I-COMP` |
| 62 | của | `I-COMP` |
| 63 | tôi. | `I-COMP` |
| 64 | tôi | `O` |
| 65 | có | `O` |
| 66 | gửi | `O` |
| 67 | email | `O` |
| 68 | m... | `O` |
| 69 | bài | `O` |
| 70 | đánh | `O` |
| 71 | giá | `O` |
| 72 | đầy | `O` |
| 73 | đủ | `O` |

**Heuristic warnings:**

- span #0 quá dài (21 tokens >= 15)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 17. `train_002019`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> giày cũng đẹp nhưng mà mùi ghê lắm

**Spans:**

- #0 [23:34] `mùi ghê lắm` label=`COMP`

**Reason:** Cụm 'mùi ghê lắm' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | giày | `O` |
| 1 | cũng | `O` |
| 2 | đẹp | `O` |
| 3 | nhưng | `O` |
| 4 | mà | `O` |
| 5 | mùi | `B-COMP` |
| 6 | ghê | `I-COMP` |
| 7 | lắm | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 18. `train_004164`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đặt màu đen mà đi giao màu vàng

**Spans:**

- #0 [0:31] `đặt màu đen mà đi giao màu vàng` label=`COMP`

**Reason:** Cụm 'đặt màu đen mà đi giao màu vàng' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đặt | `B-COMP` |
| 1 | màu | `I-COMP` |
| 2 | đen | `I-COMP` |
| 3 | mà | `I-COMP` |
| 4 | đi | `I-COMP` |
| 5 | giao | `I-COMP` |
| 6 | màu | `I-COMP` |
| 7 | vàng | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 19. `train_001829`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> eo hơi nhỏ đường may hơi túm

**Spans:**

- #0 [0:28] `eo hơi nhỏ đường may hơi túm` label=`COMP`

**Reason:** Cụm 'eo hơi nhỏ đường may hơi túm' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | eo | `B-COMP` |
| 1 | hơi | `I-COMP` |
| 2 | nhỏ | `I-COMP` |
| 3 | đường | `I-COMP` |
| 4 | may | `I-COMP` |
| 5 | hơi | `I-COMP` |
| 6 | túm | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 20. `train_002068`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> điện thoại mà bọc hàng chán không chịu  được , không có lót gì bên trong hộp, không đề hàng dễ rơi vớ. cạch lazada đến già  quả  mua hàng đắt tiền thế này.

**Spans:**

- #0 [14:44] `bọc hàng chán không chịu  được` label=`COMP`
- #1 [47:76] `không có lót gì bên trong hộp` label=`COMP`
- #2 [103:154] `cạch lazada đến già  quả  mua hàng đắt tiền thế này` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | điện | `O` |
| 1 | thoại | `O` |
| 2 | mà | `O` |
| 3 | bọc | `B-COMP` |
| 4 | hàng | `I-COMP` |
| 5 | chán | `I-COMP` |
| 6 | không | `I-COMP` |
| 7 | chịu | `I-COMP` |
| 8 | được | `I-COMP` |
| 9 | , | `O` |
| 10 | không | `B-COMP` |
| 11 | có | `I-COMP` |
| 12 | lót | `I-COMP` |
| 13 | gì | `I-COMP` |
| 14 | bên | `I-COMP` |
| 15 | trong | `I-COMP` |
| 16 | hộp, | `I-COMP` |
| 17 | không | `O` |
| 18 | đề | `O` |
| 19 | hàng | `O` |
| 20 | dễ | `O` |
| 21 | rơi | `O` |
| 22 | vớ. | `O` |
| 23 | cạch | `B-COMP` |
| 24 | lazada | `I-COMP` |
| 25 | đến | `I-COMP` |
| 26 | già | `I-COMP` |
| 27 | quả | `I-COMP` |
| 28 | mua | `I-COMP` |
| 29 | hàng | `I-COMP` |
| 30 | đắt | `I-COMP` |
| 31 | tiền | `I-COMP` |
| 32 | thế | `I-COMP` |
| 33 | này. | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (70.6%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 21. `train_003691`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> tin tưởng phân phối chính hãng và mua hàng, mở hộp thì trên seal màn hình dính bụi, mặt sau 4 camera thì bị lệch hết 2 cam dưới. gia công tệ kinh khủng. có lẽ do mua đợt đèn flash sale nên vậy

**Spans:**

- #0 [0:42] `tin tưởng phân phối chính hãng và mua hàng` label=`COMP`
- #1 [84:127] `mặt sau 4 camera thì bị lệch hết 2 cam dưới` label=`COMP`
- #2 [129:151] `gia công tệ kinh khủng` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tin | `B-COMP` |
| 1 | tưởng | `I-COMP` |
| 2 | phân | `I-COMP` |
| 3 | phối | `I-COMP` |
| 4 | chính | `I-COMP` |
| 5 | hãng | `I-COMP` |
| 6 | và | `I-COMP` |
| 7 | mua | `I-COMP` |
| 8 | hàng, | `I-COMP` |
| 9 | mở | `O` |
| 10 | hộp | `O` |
| 11 | thì | `O` |
| 12 | trên | `O` |
| 13 | seal | `O` |
| 14 | màn | `O` |
| 15 | hình | `O` |
| 16 | dính | `O` |
| 17 | bụi, | `O` |
| 18 | mặt | `B-COMP` |
| 19 | sau | `I-COMP` |
| 20 | 4 | `I-COMP` |
| 21 | camera | `I-COMP` |
| 22 | thì | `I-COMP` |
| 23 | bị | `I-COMP` |
| 24 | lệch | `I-COMP` |
| 25 | hết | `I-COMP` |
| 26 | 2 | `I-COMP` |
| 27 | cam | `I-COMP` |
| 28 | dưới. | `I-COMP` |
| 29 | gia | `B-COMP` |
| 30 | công | `I-COMP` |
| 31 | tệ | `I-COMP` |
| 32 | kinh | `I-COMP` |
| 33 | khủng. | `I-COMP` |
| 34 | có | `O` |
| 35 | lẽ | `O` |
| 36 | do | `O` |
| 37 | mua | `O` |
| 38 | đợt | `O` |
| 39 | đèn | `O` |
| 40 | flash | `O` |
| 41 | sale | `O` |
| 42 | nên | `O` |
| 43 | vậy | `O` |

**Heuristic warnings:**

- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 22. `train_001471`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> điện thoại không có tai nghe hả  cửa hàng ?

**Spans:**

- #0 [0:41] `điện thoại không có tai nghe hả  cửa hàng` label=`COMP`

**Reason:** Cụm 'điện thoại không có tai nghe hả  cửa hàng' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | điện | `B-COMP` |
| 1 | thoại | `I-COMP` |
| 2 | không | `I-COMP` |
| 3 | có | `I-COMP` |
| 4 | tai | `I-COMP` |
| 5 | nghe | `I-COMP` |
| 6 | hả | `I-COMP` |
| 7 | cửa | `I-COMP` |
| 8 | hàng | `I-COMP` |
| 9 | ? | `O` |

**Heuristic warnings:**

- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (90.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 23. `train_003096`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> giao hàng nhanh. đóng gói không có xốp hay nilon chống sốc. nhưng may là không có va đập gì. hộp vuông vắn nguyên seal. mở máy cảm giác ban đầu rất đẹp mượt mà long lanh. ngày hôm sau  cửa hàng  đã kích hoạt bảo hành. mua được sản phẩm chính hãng nguyên seal giá rẻ rất ưng ý. cảm ơn  cửa hàng  rất nhiều... sẽ ủng hộ  cửa hàng  trong đơn hàng tiếp theo.

**Spans:**

- #0 [0:15] `giao hàng nhanh` label=`COMP`
- #1 [17:58] `đóng gói không có xốp hay nilon chống sốc` label=`COMP`
- #2 [66:91] `may là không có va đập gì` label=`COMP`
- #3 [308:353] `sẽ ủng hộ  cửa hàng  trong đơn hàng tiếp theo` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | giao | `B-COMP` |
| 1 | hàng | `I-COMP` |
| 2 | nhanh. | `I-COMP` |
| 3 | đóng | `B-COMP` |
| 4 | gói | `I-COMP` |
| 5 | không | `I-COMP` |
| 6 | có | `I-COMP` |
| 7 | xốp | `I-COMP` |
| 8 | hay | `I-COMP` |
| 9 | nilon | `I-COMP` |
| 10 | chống | `I-COMP` |
| 11 | sốc. | `I-COMP` |
| 12 | nhưng | `O` |
| 13 | may | `B-COMP` |
| 14 | là | `I-COMP` |
| 15 | không | `I-COMP` |
| 16 | có | `I-COMP` |
| 17 | va | `I-COMP` |
| 18 | đập | `I-COMP` |
| 19 | gì. | `I-COMP` |
| 20 | hộp | `O` |
| 21 | vuông | `O` |
| 22 | vắn | `O` |
| 23 | nguyên | `O` |
| 24 | seal. | `O` |
| 25 | mở | `O` |
| 26 | máy | `O` |
| 27 | cảm | `O` |
| 28 | giác | `O` |
| 29 | ban | `O` |
| 30 | đầu | `O` |
| 31 | rất | `O` |
| 32 | đẹp | `O` |
| 33 | mượt | `O` |
| 34 | mà | `O` |
| 35 | long | `O` |
| 36 | lanh. | `O` |
| 37 | ngày | `O` |
| 38 | hôm | `O` |
| 39 | sau | `O` |
| 40 | cửa | `O` |
| 41 | hàng | `O` |
| 42 | đã | `O` |
| 43 | kích | `O` |
| 44 | hoạt | `O` |
| 45 | bảo | `O` |
| 46 | hành. | `O` |
| 47 | mua | `O` |
| 48 | được | `O` |
| 49 | sản | `O` |
| 50 | phẩm | `O` |
| 51 | chính | `O` |
| 52 | hãng | `O` |
| 53 | nguyên | `O` |
| 54 | seal | `O` |
| 55 | giá | `O` |
| 56 | rẻ | `O` |
| 57 | rất | `O` |
| 58 | ưng | `O` |
| 59 | ý. | `O` |
| 60 | cảm | `O` |
| 61 | ơn | `O` |
| 62 | cửa | `O` |
| 63 | hàng | `O` |
| 64 | rất | `O` |
| 65 | nhiều... | `O` |
| 66 | sẽ | `B-COMP` |
| 67 | ủng | `I-COMP` |
| 68 | hộ | `I-COMP` |
| 69 | cửa | `I-COMP` |
| 70 | hàng | `I-COMP` |
| 71 | trong | `I-COMP` |
| 72 | đơn | `I-COMP` |
| 73 | hàng | `I-COMP` |
| 74 | tiếp | `I-COMP` |
| 75 | theo. | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 24. `train_003073`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> máy đẹp chính hãng, đã test game mượt, cầm nắm khá là ok, tuy giao hàng chập chút nhưng vẫn ủng hộ  cửa hàng   5star  , còn sử dụng lâu dài xem sao

**Spans:**

- #0 [62:116] `giao hàng chập chút nhưng vẫn ủng hộ  cửa hàng   5star` label=`COMP`

**Reason:** Cụm 'giao hàng chập chút nhưng vẫn ủng hộ  cửa hàng   5star' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | máy | `O` |
| 1 | đẹp | `O` |
| 2 | chính | `O` |
| 3 | hãng, | `O` |
| 4 | đã | `O` |
| 5 | test | `O` |
| 6 | game | `O` |
| 7 | mượt, | `O` |
| 8 | cầm | `O` |
| 9 | nắm | `O` |
| 10 | khá | `O` |
| 11 | là | `O` |
| 12 | ok, | `O` |
| 13 | tuy | `O` |
| 14 | giao | `B-COMP` |
| 15 | hàng | `I-COMP` |
| 16 | chập | `I-COMP` |
| 17 | chút | `I-COMP` |
| 18 | nhưng | `I-COMP` |
| 19 | vẫn | `I-COMP` |
| 20 | ủng | `I-COMP` |
| 21 | hộ | `I-COMP` |
| 22 | cửa | `I-COMP` |
| 23 | hàng | `I-COMP` |
| 24 | 5star | `I-COMP` |
| 25 | , | `O` |
| 26 | còn | `O` |
| 27 | sử | `O` |
| 28 | dụng | `O` |
| 29 | lâu | `O` |
| 30 | dài | `O` |
| 31 | xem | `O` |
| 32 | sao | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 25. `train_001961`

- Domain: `app`
- Split: `train`

**Text gốc:**

> màn hình có phần kim cương hoặc dấu cộng rất vướng víu khi tìm kiếm. nếu nhóm sáng chế có thể cài phím này dịch chuyển giống phím home của iphone thì sẽ tiện lợi hơn nhiều.

**Spans:**

- #0 [2:67] `n hình có phần kim cương hoặc dấu cộng rất vướng víu khi tìm kiếm` label=`COMP`

**Reason:** Cụm 'n hình có phần kim cương hoặc dấu cộng rất vướng víu khi tìm kiếm' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | màn | `B-COMP` |
| 1 | hình | `I-COMP` |
| 2 | có | `I-COMP` |
| 3 | phần | `I-COMP` |
| 4 | kim | `I-COMP` |
| 5 | cương | `I-COMP` |
| 6 | hoặc | `I-COMP` |
| 7 | dấu | `I-COMP` |
| 8 | cộng | `I-COMP` |
| 9 | rất | `I-COMP` |
| 10 | vướng | `I-COMP` |
| 11 | víu | `I-COMP` |
| 12 | khi | `I-COMP` |
| 13 | tìm | `I-COMP` |
| 14 | kiếm. | `I-COMP` |
| 15 | nếu | `O` |
| 16 | nhóm | `O` |
| 17 | sáng | `O` |
| 18 | chế | `O` |
| 19 | có | `O` |
| 20 | thể | `O` |
| 21 | cài | `O` |
| 22 | phím | `O` |
| 23 | này | `O` |
| 24 | dịch | `O` |
| 25 | chuyển | `O` |
| 26 | giống | `O` |
| 27 | phím | `O` |
| 28 | home | `O` |
| 29 | của | `O` |
| 30 | iphone | `O` |
| 31 | thì | `O` |
| 32 | sẽ | `O` |
| 33 | tiện | `O` |
| 34 | lợi | `O` |
| 35 | hơn | `O` |
| 36 | nhiều. | `O` |

**Heuristic warnings:**

- span #0 quá dài (15 tokens >= 15)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 26. `train_000765`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đầm đẹp đáng giá tiền nhưng ở ngoài đầm hơi ôm chứ  không xoè nên  không thích lắm

**Spans:**

- #0 [28:82] `ở ngoài đầm hơi ôm chứ  không xoè nên  không thích lắm` label=`COMP`

**Reason:** Cụm 'ở ngoài đầm hơi ôm chứ  không xoè nên  không thích lắm' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đầm | `O` |
| 1 | đẹp | `O` |
| 2 | đáng | `O` |
| 3 | giá | `O` |
| 4 | tiền | `O` |
| 5 | nhưng | `O` |
| 6 | ở | `B-COMP` |
| 7 | ngoài | `I-COMP` |
| 8 | đầm | `I-COMP` |
| 9 | hơi | `I-COMP` |
| 10 | ôm | `I-COMP` |
| 11 | chứ | `I-COMP` |
| 12 | không | `I-COMP` |
| 13 | xoè | `I-COMP` |
| 14 | nên | `I-COMP` |
| 15 | không | `I-COMP` |
| 16 | thích | `I-COMP` |
| 17 | lắm | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (66.7%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 27. `train_000444`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> tốt nhưng hôi cực

**Spans:**

- #0 [10:17] `hôi cực` label=`COMP`

**Reason:** Cụm 'hôi cực' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tốt | `O` |
| 1 | nhưng | `O` |
| 2 | hôi | `B-COMP` |
| 3 | cực | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 28. `train_001396`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> sản phẩm tốt , tuy có giao trễ hơn dự kiến vài hôm.

**Spans:**

- #0 [19:50] `có giao trễ hơn dự kiến vài hôm` label=`COMP`

**Reason:** Cụm 'có giao trễ hơn dự kiến vài hôm' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | sản | `O` |
| 1 | phẩm | `O` |
| 2 | tốt | `O` |
| 3 | , | `O` |
| 4 | tuy | `O` |
| 5 | có | `B-COMP` |
| 6 | giao | `I-COMP` |
| 7 | trễ | `I-COMP` |
| 8 | hơn | `I-COMP` |
| 9 | dự | `I-COMP` |
| 10 | kiến | `I-COMP` |
| 11 | vài | `I-COMP` |
| 12 | hôm. | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (61.5%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 29. `train_000587`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> son có mùi như mùi bút sáp màu nên ngửi hơi khó chịu, không phải kiểu son mượt môi như mình kì vọng. màu đẹp

**Spans:**

- #0 [29:52] `u nên ngửi hơi khó chịu` label=`COMP`

**Reason:** Cụm 'u nên ngửi hơi khó chịu' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | son | `O` |
| 1 | có | `O` |
| 2 | mùi | `O` |
| 3 | như | `O` |
| 4 | mùi | `O` |
| 5 | bút | `O` |
| 6 | sáp | `O` |
| 7 | màu | `B-COMP` |
| 8 | nên | `I-COMP` |
| 9 | ngửi | `I-COMP` |
| 10 | hơi | `I-COMP` |
| 11 | khó | `I-COMP` |
| 12 | chịu, | `I-COMP` |
| 13 | không | `O` |
| 14 | phải | `O` |
| 15 | kiểu | `O` |
| 16 | son | `O` |
| 17 | mượt | `O` |
| 18 | môi | `O` |
| 19 | như | `O` |
| 20 | mình | `O` |
| 21 | kì | `O` |
| 22 | vọng. | `O` |
| 23 | màu | `O` |
| 24 | đẹp | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 30. `train_002179`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> giao hàng chậm 3 ngày. đóng gói chắc chắn. hàng không móp không hay hư hỏng. máy mới nguyên. không như tgD, đưa máy đã qua tay nhiều người cho mình thử và bắt phải mua cái đó. máy trầy mình không lấy, lên mạng đặt cái m21 này luôn. trước mắt thấy rất hài lòng.

**Spans:**

- #0 [0:21] `giao hàng chậm 3 ngày` label=`COMP`
- #1 [43:75] `hàng không móp không hay hư hỏng` label=`COMP`
- #2 [176:199] `máy trầy mình không lấy` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | giao | `B-COMP` |
| 1 | hàng | `I-COMP` |
| 2 | chậm | `I-COMP` |
| 3 | 3 | `I-COMP` |
| 4 | ngày. | `I-COMP` |
| 5 | đóng | `O` |
| 6 | gói | `O` |
| 7 | chắc | `O` |
| 8 | chắn. | `O` |
| 9 | hàng | `B-COMP` |
| 10 | không | `I-COMP` |
| 11 | móp | `I-COMP` |
| 12 | không | `I-COMP` |
| 13 | hay | `I-COMP` |
| 14 | hư | `I-COMP` |
| 15 | hỏng. | `I-COMP` |
| 16 | máy | `O` |
| 17 | mới | `O` |
| 18 | nguyên. | `O` |
| 19 | không | `O` |
| 20 | như | `O` |
| 21 | tgD, | `O` |
| 22 | đưa | `O` |
| 23 | máy | `O` |
| 24 | đã | `O` |
| 25 | qua | `O` |
| 26 | tay | `O` |
| 27 | nhiều | `O` |
| 28 | người | `O` |
| 29 | cho | `O` |
| 30 | mình | `O` |
| 31 | thử | `O` |
| 32 | và | `O` |
| 33 | bắt | `O` |
| 34 | phải | `O` |
| 35 | mua | `O` |
| 36 | cái | `O` |
| 37 | đó. | `O` |
| 38 | máy | `B-COMP` |
| 39 | trầy | `I-COMP` |
| 40 | mình | `I-COMP` |
| 41 | không | `I-COMP` |
| 42 | lấy, | `I-COMP` |
| 43 | lên | `O` |
| 44 | mạng | `O` |
| 45 | đặt | `O` |
| 46 | cái | `O` |
| 47 | m21 | `O` |
| 48 | này | `O` |
| 49 | luôn. | `O` |
| 50 | trước | `O` |
| 51 | mắt | `O` |
| 52 | thấy | `O` |
| 53 | rất | `O` |
| 54 | hài | `O` |
| 55 | lòng. | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 31. `train_002360`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> nói khuyến mại sữa rửa mặt nhưng lại không hề có và cũng không hề thông báo cho khách hàng. thất vọng về  cửa hàng .

**Spans:**

- #0 [33:90] `lại không hề có và cũng không hề thông báo cho khách hàng` label=`COMP`
- #1 [92:114] `thất vọng về  cửa hàng` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | nói | `O` |
| 1 | khuyến | `O` |
| 2 | mại | `O` |
| 3 | sữa | `O` |
| 4 | rửa | `O` |
| 5 | mặt | `O` |
| 6 | nhưng | `O` |
| 7 | lại | `B-COMP` |
| 8 | không | `I-COMP` |
| 9 | hề | `I-COMP` |
| 10 | có | `I-COMP` |
| 11 | và | `I-COMP` |
| 12 | cũng | `I-COMP` |
| 13 | không | `I-COMP` |
| 14 | hề | `I-COMP` |
| 15 | thông | `I-COMP` |
| 16 | báo | `I-COMP` |
| 17 | cho | `I-COMP` |
| 18 | khách | `I-COMP` |
| 19 | hàng. | `I-COMP` |
| 20 | thất | `B-COMP` |
| 21 | vọng | `I-COMP` |
| 22 | về | `I-COMP` |
| 23 | cửa | `I-COMP` |
| 24 | hàng | `I-COMP` |
| 25 | . | `O` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (69.2%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 32. `train_002369`

- Domain: `app`
- Split: `train`

**Text gốc:**

> đăng kí chưa xong mới ghi 2 chữ trong paS thì bay vô nói tài khoản có vấn đề và vi phạm gì gì đó trong khi tôi còn chưa tạo nó! bạn cần xác minh điều gì khi mà tôi còn chưa hề tạo tài khoản? và tôi đã làm tất cả để xác minh như aP bắt từ gmail đến số điện thoại nhưng chờ mãi mà sms vẫn không hề gửi mã! các bạn... bài đánh giá đầy đủ

**Spans:**

- #0 [279:302] `sms vẫn không hề gửi mã` label=`COMP`

**Reason:** Cụm 'sms vẫn không hề gửi mã' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đăng | `O` |
| 1 | kí | `O` |
| 2 | chưa | `O` |
| 3 | xong | `O` |
| 4 | mới | `O` |
| 5 | ghi | `O` |
| 6 | 2 | `O` |
| 7 | chữ | `O` |
| 8 | trong | `O` |
| 9 | paS | `O` |
| 10 | thì | `O` |
| 11 | bay | `O` |
| 12 | vô | `O` |
| 13 | nói | `O` |
| 14 | tài | `O` |
| 15 | khoản | `O` |
| 16 | có | `O` |
| 17 | vấn | `O` |
| 18 | đề | `O` |
| 19 | và | `O` |
| 20 | vi | `O` |
| 21 | phạm | `O` |
| 22 | gì | `O` |
| 23 | gì | `O` |
| 24 | đó | `O` |
| 25 | trong | `O` |
| 26 | khi | `O` |
| 27 | tôi | `O` |
| 28 | còn | `O` |
| 29 | chưa | `O` |
| 30 | tạo | `O` |
| 31 | nó! | `O` |
| 32 | bạn | `O` |
| 33 | cần | `O` |
| 34 | xác | `O` |
| 35 | minh | `O` |
| 36 | điều | `O` |
| 37 | gì | `O` |
| 38 | khi | `O` |
| 39 | mà | `O` |
| 40 | tôi | `O` |
| 41 | còn | `O` |
| 42 | chưa | `O` |
| 43 | hề | `O` |
| 44 | tạo | `O` |
| 45 | tài | `O` |
| 46 | khoản? | `O` |
| 47 | và | `O` |
| 48 | tôi | `O` |
| 49 | đã | `O` |
| 50 | làm | `O` |
| 51 | tất | `O` |
| 52 | cả | `O` |
| 53 | để | `O` |
| 54 | xác | `O` |
| 55 | minh | `O` |
| 56 | như | `O` |
| 57 | aP | `O` |
| 58 | bắt | `O` |
| 59 | từ | `O` |
| 60 | gmail | `O` |
| 61 | đến | `O` |
| 62 | số | `O` |
| 63 | điện | `O` |
| 64 | thoại | `O` |
| 65 | nhưng | `O` |
| 66 | chờ | `O` |
| 67 | mãi | `O` |
| 68 | mà | `O` |
| 69 | sms | `B-COMP` |
| 70 | vẫn | `I-COMP` |
| 71 | không | `I-COMP` |
| 72 | hề | `I-COMP` |
| 73 | gửi | `I-COMP` |
| 74 | mã! | `I-COMP` |
| 75 | các | `O` |
| 76 | bạn... | `O` |
| 77 | bài | `O` |
| 78 | đánh | `O` |
| 79 | giá | `O` |
| 80 | đầy | `O` |
| 81 | đủ | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 33. `train_001937`

- Domain: `app`
- Split: `train`

**Text gốc:**

> những đoạn chuyện chêm voice bị thiếu rất nhiều lại còn thiếu những chỗ cần nghe để điền từ.ví dụ như unit 7 trang 71 của sách phiên bản cũ thì mất luôn cái dòng đối thoại thứ nhất , ở trang 79 của unit 8 cũng mất hẳng đoạn voice dài 3 dòng ở cuối đoạn chuyện chêm và còn nhiều nữa. thế thì biết cái ... bài đánh giá đầy đủ

**Spans:**

- #0 [56:91] `thiếu những chỗ cần nghe để điền từ` label=`COMP`
- #1 [144:180] `mất luôn cái dòng đối thoại thứ nhất` label=`COMP`
- #2 [183:281] `ở trang 79 của unit 8 cũng mất hẳng đoạn voice dài 3 dòng ở cuối đoạn chuyện chêm và còn nhiều nữa` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | những | `O` |
| 1 | đoạn | `O` |
| 2 | chuyện | `O` |
| 3 | chêm | `O` |
| 4 | voice | `O` |
| 5 | bị | `O` |
| 6 | thiếu | `O` |
| 7 | rất | `O` |
| 8 | nhiều | `O` |
| 9 | lại | `O` |
| 10 | còn | `O` |
| 11 | thiếu | `B-COMP` |
| 12 | những | `I-COMP` |
| 13 | chỗ | `I-COMP` |
| 14 | cần | `I-COMP` |
| 15 | nghe | `I-COMP` |
| 16 | để | `I-COMP` |
| 17 | điền | `I-COMP` |
| 18 | từ.ví | `I-COMP` |
| 19 | dụ | `O` |
| 20 | như | `O` |
| 21 | unit | `O` |
| 22 | 7 | `O` |
| 23 | trang | `O` |
| 24 | 71 | `O` |
| 25 | của | `O` |
| 26 | sách | `O` |
| 27 | phiên | `O` |
| 28 | bản | `O` |
| 29 | cũ | `O` |
| 30 | thì | `O` |
| 31 | mất | `B-COMP` |
| 32 | luôn | `I-COMP` |
| 33 | cái | `I-COMP` |
| 34 | dòng | `I-COMP` |
| 35 | đối | `I-COMP` |
| 36 | thoại | `I-COMP` |
| 37 | thứ | `I-COMP` |
| 38 | nhất | `I-COMP` |
| 39 | , | `O` |
| 40 | ở | `B-COMP` |
| 41 | trang | `I-COMP` |
| 42 | 79 | `I-COMP` |
| 43 | của | `I-COMP` |
| 44 | unit | `I-COMP` |
| 45 | 8 | `I-COMP` |
| 46 | cũng | `I-COMP` |
| 47 | mất | `I-COMP` |
| 48 | hẳng | `I-COMP` |
| 49 | đoạn | `I-COMP` |
| 50 | voice | `I-COMP` |
| 51 | dài | `I-COMP` |
| 52 | 3 | `I-COMP` |
| 53 | dòng | `I-COMP` |
| 54 | ở | `I-COMP` |
| 55 | cuối | `I-COMP` |
| 56 | đoạn | `I-COMP` |
| 57 | chuyện | `I-COMP` |
| 58 | chêm | `I-COMP` |
| 59 | và | `I-COMP` |
| 60 | còn | `I-COMP` |
| 61 | nhiều | `I-COMP` |
| 62 | nữa. | `I-COMP` |
| 63 | thế | `O` |
| 64 | thì | `O` |
| 65 | biết | `O` |
| 66 | cái | `O` |
| 67 | ... | `O` |
| 68 | bài | `O` |
| 69 | đánh | `O` |
| 70 | giá | `O` |
| 71 | đầy | `O` |
| 72 | đủ | `O` |

**Heuristic warnings:**

- span #2 quá dài (23 tokens >= 15)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 34. `train_001481`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> mua lúc  được  tặng quà mas nhưng  cửa hàng  giao không tặng

**Spans:**

- #0 [35:60] `cửa hàng  giao không tặng` label=`COMP`

**Reason:** Cụm 'cửa hàng  giao không tặng' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mua | `O` |
| 1 | lúc | `O` |
| 2 | được | `O` |
| 3 | tặng | `O` |
| 4 | quà | `O` |
| 5 | mas | `O` |
| 6 | nhưng | `O` |
| 7 | cửa | `B-COMP` |
| 8 | hàng | `I-COMP` |
| 9 | giao | `I-COMP` |
| 10 | không | `I-COMP` |
| 11 | tặng | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 35. `train_001530`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> không thấy sản phẩm tặng kèm thật thất vọng với chất lượng dịch vụ như thế đóng gói sản phẩm rất tốt

**Spans:**

- #0 [0:100] `không thấy sản phẩm tặng kèm thật thất vọng với chất lượng dịch vụ như thế đóng gói sản phẩm rất tốt` label=`COMP`

**Reason:** Cụm 'không thấy sản phẩm tặng kèm thật thất vọng với chất lượng dịch vụ như thế đóng gói sản phẩm rất tốt' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | không | `B-COMP` |
| 1 | thấy | `I-COMP` |
| 2 | sản | `I-COMP` |
| 3 | phẩm | `I-COMP` |
| 4 | tặng | `I-COMP` |
| 5 | kèm | `I-COMP` |
| 6 | thật | `I-COMP` |
| 7 | thất | `I-COMP` |
| 8 | vọng | `I-COMP` |
| 9 | với | `I-COMP` |
| 10 | chất | `I-COMP` |
| 11 | lượng | `I-COMP` |
| 12 | dịch | `I-COMP` |
| 13 | vụ | `I-COMP` |
| 14 | như | `I-COMP` |
| 15 | thế | `I-COMP` |
| 16 | đóng | `I-COMP` |
| 17 | gói | `I-COMP` |
| 18 | sản | `I-COMP` |
| 19 | phẩm | `I-COMP` |
| 20 | rất | `I-COMP` |
| 21 | tốt | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (22 tokens >= 15)
- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 36. `train_000043`

- Domain: `app`
- Split: `train`

**Text gốc:**

> cho hỏi aP là tại sao khi mới tải xong ấn vào để chơi mà nó cứ xoay vòng vòng mãi không được thế 💁💁💁. mong aP giải đáp thắc mắc này.

**Spans:**

- #0 [57:100] `nó cứ xoay vòng vòng mãi không được thế 💁💁💁` label=`COMP`

**Reason:** Cụm 'nó cứ xoay vòng vòng mãi không được thế 💁💁💁' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | cho | `O` |
| 1 | hỏi | `O` |
| 2 | aP | `O` |
| 3 | là | `O` |
| 4 | tại | `O` |
| 5 | sao | `O` |
| 6 | khi | `O` |
| 7 | mới | `O` |
| 8 | tải | `O` |
| 9 | xong | `O` |
| 10 | ấn | `O` |
| 11 | vào | `O` |
| 12 | để | `O` |
| 13 | chơi | `O` |
| 14 | mà | `O` |
| 15 | nó | `B-COMP` |
| 16 | cứ | `I-COMP` |
| 17 | xoay | `I-COMP` |
| 18 | vòng | `I-COMP` |
| 19 | vòng | `I-COMP` |
| 20 | mãi | `I-COMP` |
| 21 | không | `I-COMP` |
| 22 | được | `I-COMP` |
| 23 | thế | `I-COMP` |
| 24 | 💁💁💁. | `I-COMP` |
| 25 | mong | `O` |
| 26 | aP | `O` |
| 27 | giải | `O` |
| 28 | đáp | `O` |
| 29 | thắc | `O` |
| 30 | mắc | `O` |
| 31 | này. | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 37. `train_004077`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> giao nhầm super volcanic peL oF mask 2x

**Spans:**

- #0 [0:39] `giao nhầm super volcanic peL oF mask 2x` label=`COMP`

**Reason:** Cụm 'giao nhầm super volcanic peL oF mask 2x' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | giao | `B-COMP` |
| 1 | nhầm | `I-COMP` |
| 2 | super | `I-COMP` |
| 3 | volcanic | `I-COMP` |
| 4 | peL | `I-COMP` |
| 5 | oF | `I-COMP` |
| 6 | mask | `I-COMP` |
| 7 | 2x | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 38. `train_000020`

- Domain: `app`
- Split: `train`

**Text gốc:**

> em có một tài khoản lần đầu em bị mất xim nên em đã thêm số điện thoại mới. thế mà mới vừa rồi em đổi mật khẩu quên khuấy mất. nên em dùng số mới để quên mật khẩu mà nó cứ đòi gửi mã về số điện thoại cũ kia. bây giờ em không biết làm như thế này cả, tài khoản ấy em chơi mấy năm rồi .

**Spans:**

- #0 [0:74] `em có một tài khoản lần đầu em bị mất xim nên em đã thêm số điện thoại mới` label=`COMP`
- #1 [83:125] `mới vừa rồi em đổi mật khẩu quên khuấy mất` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | em | `B-COMP` |
| 1 | có | `I-COMP` |
| 2 | một | `I-COMP` |
| 3 | tài | `I-COMP` |
| 4 | khoản | `I-COMP` |
| 5 | lần | `I-COMP` |
| 6 | đầu | `I-COMP` |
| 7 | em | `I-COMP` |
| 8 | bị | `I-COMP` |
| 9 | mất | `I-COMP` |
| 10 | xim | `I-COMP` |
| 11 | nên | `I-COMP` |
| 12 | em | `I-COMP` |
| 13 | đã | `I-COMP` |
| 14 | thêm | `I-COMP` |
| 15 | số | `I-COMP` |
| 16 | điện | `I-COMP` |
| 17 | thoại | `I-COMP` |
| 18 | mới. | `I-COMP` |
| 19 | thế | `O` |
| 20 | mà | `O` |
| 21 | mới | `B-COMP` |
| 22 | vừa | `I-COMP` |
| 23 | rồi | `I-COMP` |
| 24 | em | `I-COMP` |
| 25 | đổi | `I-COMP` |
| 26 | mật | `I-COMP` |
| 27 | khẩu | `I-COMP` |
| 28 | quên | `I-COMP` |
| 29 | khuấy | `I-COMP` |
| 30 | mất. | `I-COMP` |
| 31 | nên | `O` |
| 32 | em | `O` |
| 33 | dùng | `O` |
| 34 | số | `O` |
| 35 | mới | `O` |
| 36 | để | `O` |
| 37 | quên | `O` |
| 38 | mật | `O` |
| 39 | khẩu | `O` |
| 40 | mà | `O` |
| 41 | nó | `O` |
| 42 | cứ | `O` |
| 43 | đòi | `O` |
| 44 | gửi | `O` |
| 45 | mã | `O` |
| 46 | về | `O` |
| 47 | số | `O` |
| 48 | điện | `O` |
| 49 | thoại | `O` |
| 50 | cũ | `O` |
| 51 | kia. | `O` |
| 52 | bây | `O` |
| 53 | giờ | `O` |
| 54 | em | `O` |
| 55 | không | `O` |
| 56 | biết | `O` |
| 57 | làm | `O` |
| 58 | như | `O` |
| 59 | thế | `O` |
| 60 | này | `O` |
| 61 | cả, | `O` |
| 62 | tài | `O` |
| 63 | khoản | `O` |
| 64 | ấy | `O` |
| 65 | em | `O` |
| 66 | chơi | `O` |
| 67 | mấy | `O` |
| 68 | năm | `O` |
| 69 | rồi | `O` |
| 70 | . | `O` |

**Heuristic warnings:**

- span #0 quá dài (19 tokens >= 15)
- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 39. `train_002483`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> tưởng mua được samsung mới mà ai dè máy đã bị kích hoạt 2 tháng bảo hành rồi 😭

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tưởng | `O` |
| 1 | mua | `O` |
| 2 | được | `O` |
| 3 | samsung | `O` |
| 4 | mới | `O` |
| 5 | mà | `O` |
| 6 | ai | `O` |
| 7 | dè | `O` |
| 8 | máy | `O` |
| 9 | đã | `O` |
| 10 | bị | `O` |
| 11 | kích | `O` |
| 12 | hoạt | `O` |
| 13 | 2 | `O` |
| 14 | tháng | `O` |
| 15 | bảo | `O` |
| 16 | hành | `O` |
| 17 | rồi | `O` |
| 18 | 😭 | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 40. `train_004117`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> có quà  cửa hàng  không gửi

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | có | `O` |
| 1 | quà | `O` |
| 2 | cửa | `O` |
| 3 | hàng | `O` |
| 4 | không | `O` |
| 5 | gửi | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 41. `train_002047`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> dép nhẹ, đẹp được nhưng đặt  cỡ  37 mà giao  cỡ  38 mang rộng chân không  được  đẹp lắm. cửa hàng  rút kinh nghiệm lần sau đừng nhầm lẩn nha  cửa hàng .

**Spans:**

- #0 [39:87] `giao  cỡ  38 mang rộng chân không  được  đẹp lắm` label=`COMP`
- #1 [89:150] `cửa hàng  rút kinh nghiệm lần sau đừng nhầm lẩn nha  cửa hàng` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | dép | `O` |
| 1 | nhẹ, | `O` |
| 2 | đẹp | `O` |
| 3 | được | `O` |
| 4 | nhưng | `O` |
| 5 | đặt | `O` |
| 6 | cỡ | `O` |
| 7 | 37 | `O` |
| 8 | mà | `O` |
| 9 | giao | `B-COMP` |
| 10 | cỡ | `I-COMP` |
| 11 | 38 | `I-COMP` |
| 12 | mang | `I-COMP` |
| 13 | rộng | `I-COMP` |
| 14 | chân | `I-COMP` |
| 15 | không | `I-COMP` |
| 16 | được | `I-COMP` |
| 17 | đẹp | `I-COMP` |
| 18 | lắm. | `I-COMP` |
| 19 | cửa | `B-COMP` |
| 20 | hàng | `I-COMP` |
| 21 | rút | `I-COMP` |
| 22 | kinh | `I-COMP` |
| 23 | nghiệm | `I-COMP` |
| 24 | lần | `I-COMP` |
| 25 | sau | `I-COMP` |
| 26 | đừng | `I-COMP` |
| 27 | nhầm | `I-COMP` |
| 28 | lẩn | `I-COMP` |
| 29 | nha | `I-COMP` |
| 30 | cửa | `I-COMP` |
| 31 | hàng | `I-COMP` |
| 32 | . | `O` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (69.7%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 42. `train_003969`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> kaka, đồ mỏng le áo còn bị dơ, đúng tiền nào của nấy.

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | kaka, | `O` |
| 1 | đồ | `O` |
| 2 | mỏng | `O` |
| 3 | le | `O` |
| 4 | áo | `O` |
| 5 | còn | `O` |
| 6 | bị | `O` |
| 7 | dơ, | `O` |
| 8 | đúng | `O` |
| 9 | tiền | `O` |
| 10 | nào | `O` |
| 11 | của | `O` |
| 12 | nấy. | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 43. `train_001226`

- Domain: `app`
- Split: `train`

**Text gốc:**

> hay lắm! nhưng rất dễ bức xúc. sao mọi người lại chọn những bộ trang phục đẹp nhưng lại không thích hợp với chủ đề trong khi thi và bình chọn? ai cũng dùng mấy bộ trang phục không thích hợp với chủ đề cả! người chơi như vậy rất khó kiếm. mong admin cho thêm  hợp với chủ đề  vào phần đánh giá nha! ^^

**Spans:**

- #0 [84:141] `lại không thích hợp với chủ đề trong khi thi và bình chọn` label=`COMP`
- #1 [143:203] `ai cũng dùng mấy bộ trang phục không thích hợp với chủ đề cả` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hay | `O` |
| 1 | lắm! | `O` |
| 2 | nhưng | `O` |
| 3 | rất | `O` |
| 4 | dễ | `O` |
| 5 | bức | `O` |
| 6 | xúc. | `O` |
| 7 | sao | `O` |
| 8 | mọi | `O` |
| 9 | người | `O` |
| 10 | lại | `O` |
| 11 | chọn | `O` |
| 12 | những | `O` |
| 13 | bộ | `O` |
| 14 | trang | `O` |
| 15 | phục | `O` |
| 16 | đẹp | `O` |
| 17 | nhưng | `O` |
| 18 | lại | `B-COMP` |
| 19 | không | `I-COMP` |
| 20 | thích | `I-COMP` |
| 21 | hợp | `I-COMP` |
| 22 | với | `I-COMP` |
| 23 | chủ | `I-COMP` |
| 24 | đề | `I-COMP` |
| 25 | trong | `I-COMP` |
| 26 | khi | `I-COMP` |
| 27 | thi | `I-COMP` |
| 28 | và | `I-COMP` |
| 29 | bình | `I-COMP` |
| 30 | chọn? | `I-COMP` |
| 31 | ai | `B-COMP` |
| 32 | cũng | `I-COMP` |
| 33 | dùng | `I-COMP` |
| 34 | mấy | `I-COMP` |
| 35 | bộ | `I-COMP` |
| 36 | trang | `I-COMP` |
| 37 | phục | `I-COMP` |
| 38 | không | `I-COMP` |
| 39 | thích | `I-COMP` |
| 40 | hợp | `I-COMP` |
| 41 | với | `I-COMP` |
| 42 | chủ | `I-COMP` |
| 43 | đề | `I-COMP` |
| 44 | cả! | `I-COMP` |
| 45 | người | `O` |
| 46 | chơi | `O` |
| 47 | như | `O` |
| 48 | vậy | `O` |
| 49 | rất | `O` |
| 50 | khó | `O` |
| 51 | kiếm. | `O` |
| 52 | mong | `O` |
| 53 | admin | `O` |
| 54 | cho | `O` |
| 55 | thêm | `O` |
| 56 | hợp | `O` |
| 57 | với | `O` |
| 58 | chủ | `O` |
| 59 | đề | `O` |
| 60 | vào | `O` |
| 61 | phần | `O` |
| 62 | đánh | `O` |
| 63 | giá | `O` |
| 64 | nha! | `O` |
| 65 | ^^ | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 44. `train_003083`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> điện thoại cảm ứng không được nhảy cho lắm đóng gói không chắc chắn còn lại đều rất ngon trong tầm giá này

**Spans:**

- #0 [0:106] `điện thoại cảm ứng không được nhảy cho lắm đóng gói không chắc chắn còn lại đều rất ngon trong tầm giá này` label=`COMP`

**Reason:** Cụm 'điện thoại cảm ứng không được nhảy cho lắm đóng gói không chắc chắn còn lại đều rất ngon trong tầm giá này' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | điện | `B-COMP` |
| 1 | thoại | `I-COMP` |
| 2 | cảm | `I-COMP` |
| 3 | ứng | `I-COMP` |
| 4 | không | `I-COMP` |
| 5 | được | `I-COMP` |
| 6 | nhảy | `I-COMP` |
| 7 | cho | `I-COMP` |
| 8 | lắm | `I-COMP` |
| 9 | đóng | `I-COMP` |
| 10 | gói | `I-COMP` |
| 11 | không | `I-COMP` |
| 12 | chắc | `I-COMP` |
| 13 | chắn | `I-COMP` |
| 14 | còn | `I-COMP` |
| 15 | lại | `I-COMP` |
| 16 | đều | `I-COMP` |
| 17 | rất | `I-COMP` |
| 18 | ngon | `I-COMP` |
| 19 | trong | `I-COMP` |
| 20 | tầm | `I-COMP` |
| 21 | giá | `I-COMP` |
| 22 | này | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (23 tokens >= 15)
- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 45. `train_000993`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> mình đặt 2 sản phẩm hada labo nhưng giao nhầm nhãn_hiệu

**Spans:**

- #0 [36:55] `giao nhầm nhãn_hiệu` label=`COMP`

**Reason:** Cụm 'giao nhầm nhãn_hiệu' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mình | `O` |
| 1 | đặt | `O` |
| 2 | 2 | `O` |
| 3 | sản | `O` |
| 4 | phẩm | `O` |
| 5 | hada | `O` |
| 6 | labo | `O` |
| 7 | nhưng | `O` |
| 8 | giao | `B-COMP` |
| 9 | nhầm | `I-COMP` |
| 10 | nhãn_hiệu | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 46. `train_001034`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> mua đợt sale sốc 18 mà đắt đơn ngày dưng. hỏi chăm sóc khách hàng thì lờ tịt đi. quá chán.

**Spans:**

- #0 [23:40] `đắt đơn ngày dưng` label=`COMP`
- #1 [81:89] `quá chán` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mua | `O` |
| 1 | đợt | `O` |
| 2 | sale | `O` |
| 3 | sốc | `O` |
| 4 | 18 | `O` |
| 5 | mà | `O` |
| 6 | đắt | `B-COMP` |
| 7 | đơn | `I-COMP` |
| 8 | ngày | `I-COMP` |
| 9 | dưng. | `I-COMP` |
| 10 | hỏi | `O` |
| 11 | chăm | `O` |
| 12 | sóc | `O` |
| 13 | khách | `O` |
| 14 | hàng | `O` |
| 15 | thì | `O` |
| 16 | lờ | `O` |
| 17 | tịt | `O` |
| 18 | đi. | `O` |
| 19 | quá | `B-COMP` |
| 20 | chán. | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 47. `train_003604`

- Domain: `app`
- Split: `train`

**Text gốc:**

> liên quân phiên bản 3.0 thật sự quá tệ. tôi chơi liên quân từ khi mới ra nhưng phiên bản hiện tại làm tôi rất thất vọng . bản đồ giao diện thật sự nhìn rất tệ . thật sự tôi phải xoá game bởi vì nó rất tệ khôg phải riêng tôi mà là tất cả mọi người đều quen với bản đồ cũ. mong lần cập nhật tiếp theo sẽ... bài đánh giá đầy đủ

**Spans:**

- #0 [22:38] `0 thật sự quá tệ` label=`COMP`
- #1 [79:119] `phiên bản hiện tại làm tôi rất thất vọng` label=`COMP`
- #2 [122:158] `bản đồ giao diện thật sự nhìn rất tệ` label=`COMP`
- #3 [161:269] `thật sự tôi phải xoá game bởi vì nó rất tệ khôg phải riêng tôi mà là tất cả mọi người đều quen với bản đồ cũ` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | liên | `O` |
| 1 | quân | `O` |
| 2 | phiên | `O` |
| 3 | bản | `O` |
| 4 | 3.0 | `B-COMP` |
| 5 | thật | `I-COMP` |
| 6 | sự | `I-COMP` |
| 7 | quá | `I-COMP` |
| 8 | tệ. | `I-COMP` |
| 9 | tôi | `O` |
| 10 | chơi | `O` |
| 11 | liên | `O` |
| 12 | quân | `O` |
| 13 | từ | `O` |
| 14 | khi | `O` |
| 15 | mới | `O` |
| 16 | ra | `O` |
| 17 | nhưng | `O` |
| 18 | phiên | `B-COMP` |
| 19 | bản | `I-COMP` |
| 20 | hiện | `I-COMP` |
| 21 | tại | `I-COMP` |
| 22 | làm | `I-COMP` |
| 23 | tôi | `I-COMP` |
| 24 | rất | `I-COMP` |
| 25 | thất | `I-COMP` |
| 26 | vọng | `I-COMP` |
| 27 | . | `O` |
| 28 | bản | `B-COMP` |
| 29 | đồ | `I-COMP` |
| 30 | giao | `I-COMP` |
| 31 | diện | `I-COMP` |
| 32 | thật | `I-COMP` |
| 33 | sự | `I-COMP` |
| 34 | nhìn | `I-COMP` |
| 35 | rất | `I-COMP` |
| 36 | tệ | `I-COMP` |
| 37 | . | `O` |
| 38 | thật | `B-COMP` |
| 39 | sự | `I-COMP` |
| 40 | tôi | `I-COMP` |
| 41 | phải | `I-COMP` |
| 42 | xoá | `I-COMP` |
| 43 | game | `I-COMP` |
| 44 | bởi | `I-COMP` |
| 45 | vì | `I-COMP` |
| 46 | nó | `I-COMP` |
| 47 | rất | `I-COMP` |
| 48 | tệ | `I-COMP` |
| 49 | khôg | `I-COMP` |
| 50 | phải | `I-COMP` |
| 51 | riêng | `I-COMP` |
| 52 | tôi | `I-COMP` |
| 53 | mà | `I-COMP` |
| 54 | là | `I-COMP` |
| 55 | tất | `I-COMP` |
| 56 | cả | `I-COMP` |
| 57 | mọi | `I-COMP` |
| 58 | người | `I-COMP` |
| 59 | đều | `I-COMP` |
| 60 | quen | `I-COMP` |
| 61 | với | `I-COMP` |
| 62 | bản | `I-COMP` |
| 63 | đồ | `I-COMP` |
| 64 | cũ. | `I-COMP` |
| 65 | mong | `O` |
| 66 | lần | `O` |
| 67 | cập | `O` |
| 68 | nhật | `O` |
| 69 | tiếp | `O` |
| 70 | theo | `O` |
| 71 | sẽ... | `O` |
| 72 | bài | `O` |
| 73 | đánh | `O` |
| 74 | giá | `O` |
| 75 | đầy | `O` |
| 76 | đủ | `O` |

**Heuristic warnings:**

- span #3 quá dài (27 tokens >= 15)
- tỉ lệ COMP token > 60% (64.9%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 48. `train_002384`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> ổn, chưa có lỗi gì, slow motion hơi giật, cam hơi đậm

**Spans:**

- #0 [4:18] `chưa có lỗi gì` label=`COMP`
- #1 [20:40] `slow motion hơi giật` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | ổn, | `O` |
| 1 | chưa | `B-COMP` |
| 2 | có | `I-COMP` |
| 3 | lỗi | `I-COMP` |
| 4 | gì, | `I-COMP` |
| 5 | slow | `B-COMP` |
| 6 | motion | `I-COMP` |
| 7 | hơi | `I-COMP` |
| 8 | giật, | `I-COMP` |
| 9 | cam | `O` |
| 10 | hơi | `O` |
| 11 | đậm | `O` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (66.7%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 49. `train_001420`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> đóng gói kĩ tuy cái bình hơi bẩn một tí

**Spans:**

- #0 [16:39] `cái bình hơi bẩn một tí` label=`COMP`

**Reason:** Cụm 'cái bình hơi bẩn một tí' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đóng | `O` |
| 1 | gói | `O` |
| 2 | kĩ | `O` |
| 3 | tuy | `O` |
| 4 | cái | `B-COMP` |
| 5 | bình | `I-COMP` |
| 6 | hơi | `I-COMP` |
| 7 | bẩn | `I-COMP` |
| 8 | một | `I-COMP` |
| 9 | tí | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 50. `train_004137`

- Domain: `app`
- Split: `train`

**Text gốc:**

> không hiểu vì sao điện thoại của mình là điện thoại mới. mình tải twiTer về trên dưới 20 lần rồi. và mỗi lần đăng kí đều không được. nhờ người khác  được  để mình đăng nhập nó cứ để là   rất tiếc lỗi đã xảy ra. mong thử lại sao 

**Spans:**

- #0 [98:131] `và mỗi lần đăng kí đều không được` label=`COMP`
- #1 [133:209] `nhờ người khác  được  để mình đăng nhập nó cứ để là   rất tiếc lỗi đã xảy ra` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | không | `O` |
| 1 | hiểu | `O` |
| 2 | vì | `O` |
| 3 | sao | `O` |
| 4 | điện | `O` |
| 5 | thoại | `O` |
| 6 | của | `O` |
| 7 | mình | `O` |
| 8 | là | `O` |
| 9 | điện | `O` |
| 10 | thoại | `O` |
| 11 | mới. | `O` |
| 12 | mình | `O` |
| 13 | tải | `O` |
| 14 | twiTer | `O` |
| 15 | về | `O` |
| 16 | trên | `O` |
| 17 | dưới | `O` |
| 18 | 20 | `O` |
| 19 | lần | `O` |
| 20 | rồi. | `O` |
| 21 | và | `B-COMP` |
| 22 | mỗi | `I-COMP` |
| 23 | lần | `I-COMP` |
| 24 | đăng | `I-COMP` |
| 25 | kí | `I-COMP` |
| 26 | đều | `I-COMP` |
| 27 | không | `I-COMP` |
| 28 | được. | `I-COMP` |
| 29 | nhờ | `B-COMP` |
| 30 | người | `I-COMP` |
| 31 | khác | `I-COMP` |
| 32 | được | `I-COMP` |
| 33 | để | `I-COMP` |
| 34 | mình | `I-COMP` |
| 35 | đăng | `I-COMP` |
| 36 | nhập | `I-COMP` |
| 37 | nó | `I-COMP` |
| 38 | cứ | `I-COMP` |
| 39 | để | `I-COMP` |
| 40 | là | `I-COMP` |
| 41 | rất | `I-COMP` |
| 42 | tiếc | `I-COMP` |
| 43 | lỗi | `I-COMP` |
| 44 | đã | `I-COMP` |
| 45 | xảy | `I-COMP` |
| 46 | ra. | `I-COMP` |
| 47 | mong | `O` |
| 48 | thử | `O` |
| 49 | lại | `O` |
| 50 | sao | `O` |

**Heuristic warnings:**

- span #1 quá dài (18 tokens >= 15)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 51. `train_004203`

- Domain: `app`
- Split: `train`

**Text gốc:**

> mình không biết các bạn tải như thế nào nha chứ mình là có tải 3 trò ( 2 trò kia đã tải từ trước rồi nên mình không nghi ngờ)nhưng khi mới tải guNy, mình chơi mới có một ngày mà bị hack facebOk qua tiếng trung quốc rồi còn bị aD thêm mấy cái  quả người cáo bla...bla...bla vào những cái bài viết ở facebOk của mình... bài đánh giá đầy đủ

**Spans:**

- None

**Reason:** Không có khiếu nại rõ ràng; đây chủ yếu là góp ý, mong muốn hoặc đề xuất.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mình | `O` |
| 1 | không | `O` |
| 2 | biết | `O` |
| 3 | các | `O` |
| 4 | bạn | `O` |
| 5 | tải | `O` |
| 6 | như | `O` |
| 7 | thế | `O` |
| 8 | nào | `O` |
| 9 | nha | `O` |
| 10 | chứ | `O` |
| 11 | mình | `O` |
| 12 | là | `O` |
| 13 | có | `O` |
| 14 | tải | `O` |
| 15 | 3 | `O` |
| 16 | trò | `O` |
| 17 | ( | `O` |
| 18 | 2 | `O` |
| 19 | trò | `O` |
| 20 | kia | `O` |
| 21 | đã | `O` |
| 22 | tải | `O` |
| 23 | từ | `O` |
| 24 | trước | `O` |
| 25 | rồi | `O` |
| 26 | nên | `O` |
| 27 | mình | `O` |
| 28 | không | `O` |
| 29 | nghi | `O` |
| 30 | ngờ)nhưng | `O` |
| 31 | khi | `O` |
| 32 | mới | `O` |
| 33 | tải | `O` |
| 34 | guNy, | `O` |
| 35 | mình | `O` |
| 36 | chơi | `O` |
| 37 | mới | `O` |
| 38 | có | `O` |
| 39 | một | `O` |
| 40 | ngày | `O` |
| 41 | mà | `O` |
| 42 | bị | `O` |
| 43 | hack | `O` |
| 44 | facebOk | `O` |
| 45 | qua | `O` |
| 46 | tiếng | `O` |
| 47 | trung | `O` |
| 48 | quốc | `O` |
| 49 | rồi | `O` |
| 50 | còn | `O` |
| 51 | bị | `O` |
| 52 | aD | `O` |
| 53 | thêm | `O` |
| 54 | mấy | `O` |
| 55 | cái | `O` |
| 56 | quả | `O` |
| 57 | người | `O` |
| 58 | cáo | `O` |
| 59 | bla...bla...bla | `O` |
| 60 | vào | `O` |
| 61 | những | `O` |
| 62 | cái | `O` |
| 63 | bài | `O` |
| 64 | viết | `O` |
| 65 | ở | `O` |
| 66 | facebOk | `O` |
| 67 | của | `O` |
| 68 | mình... | `O` |
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

## 52. `train_004058`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> lưng khá rộng mặc dù đã chọn  cỡ  sao với quần khá ngắn nhưng cũng không sao

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | lưng | `O` |
| 1 | khá | `O` |
| 2 | rộng | `O` |
| 3 | mặc | `O` |
| 4 | dù | `O` |
| 5 | đã | `O` |
| 6 | chọn | `O` |
| 7 | cỡ | `O` |
| 8 | sao | `O` |
| 9 | với | `O` |
| 10 | quần | `O` |
| 11 | khá | `O` |
| 12 | ngắn | `O` |
| 13 | nhưng | `O` |
| 14 | cũng | `O` |
| 15 | không | `O` |
| 16 | sao | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 53. `train_001508`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> mình không để ý nên đặt sau ngày nhưng chả hiểu sao quá 2 ngày rồi vẫn còn để hiện combo trên aP, kết  quả  mình đặt combo mà chỉ nhận được một lọ kem chống nắng

**Spans:**

- None

**Reason:** Không có khiếu nại rõ ràng; đây chủ yếu là góp ý, mong muốn hoặc đề xuất.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mình | `O` |
| 1 | không | `O` |
| 2 | để | `O` |
| 3 | ý | `O` |
| 4 | nên | `O` |
| 5 | đặt | `O` |
| 6 | sau | `O` |
| 7 | ngày | `O` |
| 8 | nhưng | `O` |
| 9 | chả | `O` |
| 10 | hiểu | `O` |
| 11 | sao | `O` |
| 12 | quá | `O` |
| 13 | 2 | `O` |
| 14 | ngày | `O` |
| 15 | rồi | `O` |
| 16 | vẫn | `O` |
| 17 | còn | `O` |
| 18 | để | `O` |
| 19 | hiện | `O` |
| 20 | combo | `O` |
| 21 | trên | `O` |
| 22 | aP, | `O` |
| 23 | kết | `O` |
| 24 | quả | `O` |
| 25 | mình | `O` |
| 26 | đặt | `O` |
| 27 | combo | `O` |
| 28 | mà | `O` |
| 29 | chỉ | `O` |
| 30 | nhận | `O` |
| 31 | được | `O` |
| 32 | một | `O` |
| 33 | lọ | `O` |
| 34 | kem | `O` |
| 35 | chống | `O` |
| 36 | nắng | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 54. `train_004050`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> áo vừa quần chật không mặt vừa luôn 53  không vừa lấy đâu 55

**Spans:**

- #0 [0:60] `áo vừa quần chật không mặt vừa luôn 53  không vừa lấy đâu 55` label=`COMP`

**Reason:** Cụm 'áo vừa quần chật không mặt vừa luôn 53  không vừa lấy đâu 55' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | áo | `B-COMP` |
| 1 | vừa | `I-COMP` |
| 2 | quần | `I-COMP` |
| 3 | chật | `I-COMP` |
| 4 | không | `I-COMP` |
| 5 | mặt | `I-COMP` |
| 6 | vừa | `I-COMP` |
| 7 | luôn | `I-COMP` |
| 8 | 53 | `I-COMP` |
| 9 | không | `I-COMP` |
| 10 | vừa | `I-COMP` |
| 11 | lấy | `I-COMP` |
| 12 | đâu | `I-COMP` |
| 13 | 55 | `I-COMP` |

**Heuristic warnings:**

- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 55. `train_002082`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

>  cỡ  quần giao sai ạ

**Spans:**

- #0 [1:20] `cỡ  quần giao sai ạ` label=`COMP`

**Reason:** Cụm 'cỡ  quần giao sai ạ' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | cỡ | `B-COMP` |
| 1 | quần | `I-COMP` |
| 2 | giao | `I-COMP` |
| 3 | sai | `I-COMP` |
| 4 | ạ | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 56. `train_000999`

- Domain: `app`
- Split: `train`

**Text gốc:**

> tại sao trước khi vào client, game load đến 79% rồi một hồi lâu sau mới lên tới 92% và một lúc nữa mới được 100%? khi vào được client thì mọi thứ khá bình thường ngoại trừ việc không hiển thị biểu tượng anh hùng, biểu tượng vật phẩm, hình động của tướng và có khi không tải vào trận?

**Spans:**

- #0 [234:282] `hình động của tướng và có khi không tải vào trận` label=`COMP`

**Reason:** Cụm 'hình động của tướng và có khi không tải vào trận' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tại | `O` |
| 1 | sao | `O` |
| 2 | trước | `O` |
| 3 | khi | `O` |
| 4 | vào | `O` |
| 5 | client, | `O` |
| 6 | game | `O` |
| 7 | load | `O` |
| 8 | đến | `O` |
| 9 | 79% | `O` |
| 10 | rồi | `O` |
| 11 | một | `O` |
| 12 | hồi | `O` |
| 13 | lâu | `O` |
| 14 | sau | `O` |
| 15 | mới | `O` |
| 16 | lên | `O` |
| 17 | tới | `O` |
| 18 | 92% | `O` |
| 19 | và | `O` |
| 20 | một | `O` |
| 21 | lúc | `O` |
| 22 | nữa | `O` |
| 23 | mới | `O` |
| 24 | được | `O` |
| 25 | 100%? | `O` |
| 26 | khi | `O` |
| 27 | vào | `O` |
| 28 | được | `O` |
| 29 | client | `O` |
| 30 | thì | `O` |
| 31 | mọi | `O` |
| 32 | thứ | `O` |
| 33 | khá | `O` |
| 34 | bình | `O` |
| 35 | thường | `O` |
| 36 | ngoại | `O` |
| 37 | trừ | `O` |
| 38 | việc | `O` |
| 39 | không | `O` |
| 40 | hiển | `O` |
| 41 | thị | `O` |
| 42 | biểu | `O` |
| 43 | tượng | `O` |
| 44 | anh | `O` |
| 45 | hùng, | `O` |
| 46 | biểu | `O` |
| 47 | tượng | `O` |
| 48 | vật | `O` |
| 49 | phẩm, | `O` |
| 50 | hình | `B-COMP` |
| 51 | động | `I-COMP` |
| 52 | của | `I-COMP` |
| 53 | tướng | `I-COMP` |
| 54 | và | `I-COMP` |
| 55 | có | `I-COMP` |
| 56 | khi | `I-COMP` |
| 57 | không | `I-COMP` |
| 58 | tải | `I-COMP` |
| 59 | vào | `I-COMP` |
| 60 | trận? | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 57. `train_003397`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> cục sạc bị hỏng lazada qua te

**Spans:**

- #0 [0:29] `cục sạc bị hỏng lazada qua te` label=`COMP`

**Reason:** Cụm 'cục sạc bị hỏng lazada qua te' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | cục | `B-COMP` |
| 1 | sạc | `I-COMP` |
| 2 | bị | `I-COMP` |
| 3 | hỏng | `I-COMP` |
| 4 | lazada | `I-COMP` |
| 5 | qua | `I-COMP` |
| 6 | te | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 58. `train_003695`

- Domain: `app`
- Split: `train`

**Text gốc:**

> khôi phục lại tin nhắn cũ đã sao lưu thì bị mất hết những tin nhắn mới (mặc dù các tin nhắn mới này đều đã  được  sao lưu). và không cách nào lấy lại  được . rất không hài lòng. nếu khôi phục lại tin nhắn cũ để rồi mất hết những tin nhắn mới thì tính năng này thà không có còn hơn

**Spans:**

- #0 [0:122] `khôi phục lại tin nhắn cũ đã sao lưu thì bị mất hết những tin nhắn mới (mặc dù các tin nhắn mới này đều đã  được  sao lưu)` label=`COMP`
- #1 [158:176] `rất không hài lòng` label=`COMP`
- #2 [178:280] `nếu khôi phục lại tin nhắn cũ để rồi mất hết những tin nhắn mới thì tính năng này thà không có còn hơn` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | khôi | `B-COMP` |
| 1 | phục | `I-COMP` |
| 2 | lại | `I-COMP` |
| 3 | tin | `I-COMP` |
| 4 | nhắn | `I-COMP` |
| 5 | cũ | `I-COMP` |
| 6 | đã | `I-COMP` |
| 7 | sao | `I-COMP` |
| 8 | lưu | `I-COMP` |
| 9 | thì | `I-COMP` |
| 10 | bị | `I-COMP` |
| 11 | mất | `I-COMP` |
| 12 | hết | `I-COMP` |
| 13 | những | `I-COMP` |
| 14 | tin | `I-COMP` |
| 15 | nhắn | `I-COMP` |
| 16 | mới | `I-COMP` |
| 17 | (mặc | `I-COMP` |
| 18 | dù | `I-COMP` |
| 19 | các | `I-COMP` |
| 20 | tin | `I-COMP` |
| 21 | nhắn | `I-COMP` |
| 22 | mới | `I-COMP` |
| 23 | này | `I-COMP` |
| 24 | đều | `I-COMP` |
| 25 | đã | `I-COMP` |
| 26 | được | `I-COMP` |
| 27 | sao | `I-COMP` |
| 28 | lưu). | `I-COMP` |
| 29 | và | `O` |
| 30 | không | `O` |
| 31 | cách | `O` |
| 32 | nào | `O` |
| 33 | lấy | `O` |
| 34 | lại | `O` |
| 35 | được | `O` |
| 36 | . | `O` |
| 37 | rất | `B-COMP` |
| 38 | không | `I-COMP` |
| 39 | hài | `I-COMP` |
| 40 | lòng. | `I-COMP` |
| 41 | nếu | `B-COMP` |
| 42 | khôi | `I-COMP` |
| 43 | phục | `I-COMP` |
| 44 | lại | `I-COMP` |
| 45 | tin | `I-COMP` |
| 46 | nhắn | `I-COMP` |
| 47 | cũ | `I-COMP` |
| 48 | để | `I-COMP` |
| 49 | rồi | `I-COMP` |
| 50 | mất | `I-COMP` |
| 51 | hết | `I-COMP` |
| 52 | những | `I-COMP` |
| 53 | tin | `I-COMP` |
| 54 | nhắn | `I-COMP` |
| 55 | mới | `I-COMP` |
| 56 | thì | `I-COMP` |
| 57 | tính | `I-COMP` |
| 58 | năng | `I-COMP` |
| 59 | này | `I-COMP` |
| 60 | thà | `I-COMP` |
| 61 | không | `I-COMP` |
| 62 | có | `I-COMP` |
| 63 | còn | `I-COMP` |
| 64 | hơn | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (29 tokens >= 15)
- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- span #2 quá dài (24 tokens >= 15)
- tỉ lệ COMP token > 60% (87.7%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 59. `train_001200`

- Domain: `app`
- Split: `train`

**Text gốc:**

> tại sao phải trả tiền chứ!

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tại | `O` |
| 1 | sao | `O` |
| 2 | phải | `O` |
| 3 | trả | `O` |
| 4 | tiền | `O` |
| 5 | chứ! | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 60. `train_002717`

- Domain: `app`
- Split: `train`

**Text gốc:**

> này có âm sao cho âm luôn. để giành mấy trợ giúp được kha khá khi cần dùng đến, đang chơi gần hồi kết tự trò chơi bật thoát ra ngoai,vào lại mất hết những phần trợ giúp lại phai chơi từ đầu. định lừa nhau ah. gỡ bỏ ứng dụng ngay luôn. tào lao hết pít. chơi miết mày bao ngày mới được vậy. vả lại nhie... bài đánh giá đầy đủ

**Spans:**

- #0 [133:189] `vào lại mất hết những phần trợ giúp lại phai chơi từ đầu` label=`COMP`
- #1 [235:250] `tào lao hết pít` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | này | `O` |
| 1 | có | `O` |
| 2 | âm | `O` |
| 3 | sao | `O` |
| 4 | cho | `O` |
| 5 | âm | `O` |
| 6 | luôn. | `O` |
| 7 | để | `O` |
| 8 | giành | `O` |
| 9 | mấy | `O` |
| 10 | trợ | `O` |
| 11 | giúp | `O` |
| 12 | được | `O` |
| 13 | kha | `O` |
| 14 | khá | `O` |
| 15 | khi | `O` |
| 16 | cần | `O` |
| 17 | dùng | `O` |
| 18 | đến, | `O` |
| 19 | đang | `O` |
| 20 | chơi | `O` |
| 21 | gần | `O` |
| 22 | hồi | `O` |
| 23 | kết | `O` |
| 24 | tự | `O` |
| 25 | trò | `O` |
| 26 | chơi | `O` |
| 27 | bật | `O` |
| 28 | thoát | `O` |
| 29 | ra | `O` |
| 30 | ngoai,vào | `B-COMP` |
| 31 | lại | `I-COMP` |
| 32 | mất | `I-COMP` |
| 33 | hết | `I-COMP` |
| 34 | những | `I-COMP` |
| 35 | phần | `I-COMP` |
| 36 | trợ | `I-COMP` |
| 37 | giúp | `I-COMP` |
| 38 | lại | `I-COMP` |
| 39 | phai | `I-COMP` |
| 40 | chơi | `I-COMP` |
| 41 | từ | `I-COMP` |
| 42 | đầu. | `I-COMP` |
| 43 | định | `O` |
| 44 | lừa | `O` |
| 45 | nhau | `O` |
| 46 | ah. | `O` |
| 47 | gỡ | `O` |
| 48 | bỏ | `O` |
| 49 | ứng | `O` |
| 50 | dụng | `O` |
| 51 | ngay | `O` |
| 52 | luôn. | `O` |
| 53 | tào | `B-COMP` |
| 54 | lao | `I-COMP` |
| 55 | hết | `I-COMP` |
| 56 | pít. | `I-COMP` |
| 57 | chơi | `O` |
| 58 | miết | `O` |
| 59 | mày | `O` |
| 60 | bao | `O` |
| 61 | ngày | `O` |
| 62 | mới | `O` |
| 63 | được | `O` |
| 64 | vậy. | `O` |
| 65 | vả | `O` |
| 66 | lại | `O` |
| 67 | nhie... | `O` |
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

## 61. `train_001341`

- Domain: `app`
- Split: `train`

**Text gốc:**

> cái phần từ điển việt anh đó, cần có sự đầu tư ví dụ như khi tìm kiếm từ tiếng việt sang anh mà không biết cái từ nó cho ra là động từ, danh từ, tính từ hay loại gì. chỉ xuất hiện đại loại là một hạn chế lớn đối với phần này!!!

**Spans:**

- #0 [166:224] `chỉ xuất hiện đại loại là một hạn chế lớn đối với phần này` label=`COMP`

**Reason:** Cụm 'chỉ xuất hiện đại loại là một hạn chế lớn đối với phần này' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | cái | `O` |
| 1 | phần | `O` |
| 2 | từ | `O` |
| 3 | điển | `O` |
| 4 | việt | `O` |
| 5 | anh | `O` |
| 6 | đó, | `O` |
| 7 | cần | `O` |
| 8 | có | `O` |
| 9 | sự | `O` |
| 10 | đầu | `O` |
| 11 | tư | `O` |
| 12 | ví | `O` |
| 13 | dụ | `O` |
| 14 | như | `O` |
| 15 | khi | `O` |
| 16 | tìm | `O` |
| 17 | kiếm | `O` |
| 18 | từ | `O` |
| 19 | tiếng | `O` |
| 20 | việt | `O` |
| 21 | sang | `O` |
| 22 | anh | `O` |
| 23 | mà | `O` |
| 24 | không | `O` |
| 25 | biết | `O` |
| 26 | cái | `O` |
| 27 | từ | `O` |
| 28 | nó | `O` |
| 29 | cho | `O` |
| 30 | ra | `O` |
| 31 | là | `O` |
| 32 | động | `O` |
| 33 | từ, | `O` |
| 34 | danh | `O` |
| 35 | từ, | `O` |
| 36 | tính | `O` |
| 37 | từ | `O` |
| 38 | hay | `O` |
| 39 | loại | `O` |
| 40 | gì. | `O` |
| 41 | chỉ | `B-COMP` |
| 42 | xuất | `I-COMP` |
| 43 | hiện | `I-COMP` |
| 44 | đại | `I-COMP` |
| 45 | loại | `I-COMP` |
| 46 | là | `I-COMP` |
| 47 | một | `I-COMP` |
| 48 | hạn | `I-COMP` |
| 49 | chế | `I-COMP` |
| 50 | lớn | `I-COMP` |
| 51 | đối | `I-COMP` |
| 52 | với | `I-COMP` |
| 53 | phần | `I-COMP` |
| 54 | này!!! | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 62. `train_002700`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> giao hàng chậm nhưng sản phẩm ok, nguyên seal.

**Spans:**

- #0 [0:32] `giao hàng chậm nhưng sản phẩm ok` label=`COMP`

**Reason:** Cụm 'giao hàng chậm nhưng sản phẩm ok' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | giao | `B-COMP` |
| 1 | hàng | `I-COMP` |
| 2 | chậm | `I-COMP` |
| 3 | nhưng | `I-COMP` |
| 4 | sản | `I-COMP` |
| 5 | phẩm | `I-COMP` |
| 6 | ok, | `I-COMP` |
| 7 | nguyên | `O` |
| 8 | seal. | `O` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (77.8%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 63. `train_000600`

- Domain: `app`
- Split: `train`

**Text gốc:**

> chưa thấy nph nào óc chó, mất dạy như bọn gamota này, cập nhật xong bây giờ mất mẹ luôn tài khoản, lúc trước đăng nhập tài khoản khách, bây giờ cập nhật xong liên kết tài khoản khách thì ra cái iG mới, vậy tài khoản cũ đâu, láo thật, khuyên mọi người tẩy chay game mất dạy này

**Spans:**

- #0 [0:24] `chưa thấy nph nào óc chó` label=`COMP`
- #1 [26:52] `mất dạy như bọn gamota này` label=`COMP`
- #2 [54:97] `cập nhật xong bây giờ mất mẹ luôn tài khoản` label=`COMP`
- #3 [234:276] `khuyên mọi người tẩy chay game mất dạy này` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | chưa | `B-COMP` |
| 1 | thấy | `I-COMP` |
| 2 | nph | `I-COMP` |
| 3 | nào | `I-COMP` |
| 4 | óc | `I-COMP` |
| 5 | chó, | `I-COMP` |
| 6 | mất | `B-COMP` |
| 7 | dạy | `I-COMP` |
| 8 | như | `I-COMP` |
| 9 | bọn | `I-COMP` |
| 10 | gamota | `I-COMP` |
| 11 | này, | `I-COMP` |
| 12 | cập | `B-COMP` |
| 13 | nhật | `I-COMP` |
| 14 | xong | `I-COMP` |
| 15 | bây | `I-COMP` |
| 16 | giờ | `I-COMP` |
| 17 | mất | `I-COMP` |
| 18 | mẹ | `I-COMP` |
| 19 | luôn | `I-COMP` |
| 20 | tài | `I-COMP` |
| 21 | khoản, | `I-COMP` |
| 22 | lúc | `O` |
| 23 | trước | `O` |
| 24 | đăng | `O` |
| 25 | nhập | `O` |
| 26 | tài | `O` |
| 27 | khoản | `O` |
| 28 | khách, | `O` |
| 29 | bây | `O` |
| 30 | giờ | `O` |
| 31 | cập | `O` |
| 32 | nhật | `O` |
| 33 | xong | `O` |
| 34 | liên | `O` |
| 35 | kết | `O` |
| 36 | tài | `O` |
| 37 | khoản | `O` |
| 38 | khách | `O` |
| 39 | thì | `O` |
| 40 | ra | `O` |
| 41 | cái | `O` |
| 42 | iG | `O` |
| 43 | mới, | `O` |
| 44 | vậy | `O` |
| 45 | tài | `O` |
| 46 | khoản | `O` |
| 47 | cũ | `O` |
| 48 | đâu, | `O` |
| 49 | láo | `O` |
| 50 | thật, | `O` |
| 51 | khuyên | `B-COMP` |
| 52 | mọi | `I-COMP` |
| 53 | người | `I-COMP` |
| 54 | tẩy | `I-COMP` |
| 55 | chay | `I-COMP` |
| 56 | game | `I-COMP` |
| 57 | mất | `I-COMP` |
| 58 | dạy | `I-COMP` |
| 59 | này | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 64. `train_002343`

- Domain: `app`
- Split: `train`

**Text gốc:**

> trước đây có tính năng ghim ra màn hình chính biểu tượng của người mình muốn liên lạc thường xuyên như bên zalo, giờ thì tìm mãi chẳng thấy, tìm kiếm trên gOgle cũng chẳng ra. giờ muốn ghim biểu tượng liên lạc ra màn hình như xưa mà đành bó tay. hy vọng nhà phát triển cập nhật lại tính năng này

**Spans:**

- None

**Reason:** Không có khiếu nại rõ ràng; đây chủ yếu là góp ý, mong muốn hoặc đề xuất.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | trước | `O` |
| 1 | đây | `O` |
| 2 | có | `O` |
| 3 | tính | `O` |
| 4 | năng | `O` |
| 5 | ghim | `O` |
| 6 | ra | `O` |
| 7 | màn | `O` |
| 8 | hình | `O` |
| 9 | chính | `O` |
| 10 | biểu | `O` |
| 11 | tượng | `O` |
| 12 | của | `O` |
| 13 | người | `O` |
| 14 | mình | `O` |
| 15 | muốn | `O` |
| 16 | liên | `O` |
| 17 | lạc | `O` |
| 18 | thường | `O` |
| 19 | xuyên | `O` |
| 20 | như | `O` |
| 21 | bên | `O` |
| 22 | zalo, | `O` |
| 23 | giờ | `O` |
| 24 | thì | `O` |
| 25 | tìm | `O` |
| 26 | mãi | `O` |
| 27 | chẳng | `O` |
| 28 | thấy, | `O` |
| 29 | tìm | `O` |
| 30 | kiếm | `O` |
| 31 | trên | `O` |
| 32 | gOgle | `O` |
| 33 | cũng | `O` |
| 34 | chẳng | `O` |
| 35 | ra. | `O` |
| 36 | giờ | `O` |
| 37 | muốn | `O` |
| 38 | ghim | `O` |
| 39 | biểu | `O` |
| 40 | tượng | `O` |
| 41 | liên | `O` |
| 42 | lạc | `O` |
| 43 | ra | `O` |
| 44 | màn | `O` |
| 45 | hình | `O` |
| 46 | như | `O` |
| 47 | xưa | `O` |
| 48 | mà | `O` |
| 49 | đành | `O` |
| 50 | bó | `O` |
| 51 | tay. | `O` |
| 52 | hy | `O` |
| 53 | vọng | `O` |
| 54 | nhà | `O` |
| 55 | phát | `O` |
| 56 | triển | `O` |
| 57 | cập | `O` |
| 58 | nhật | `O` |
| 59 | lại | `O` |
| 60 | tính | `O` |
| 61 | năng | `O` |
| 62 | này | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 65. `train_003659`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> giao hàng nhanh hàng đúng mẫu,có điều hơi chảy ,nóng chắc do giao giữa trưa(mà sao nhìn ảnh thấy có quà tặng kèm giờ nhận hàng rồi không thấy)

**Spans:**

- #0 [0:29] `giao hàng nhanh hàng đúng mẫu` label=`COMP`
- #1 [79:142] `sao nhìn ảnh thấy có quà tặng kèm giờ nhận hàng rồi không thấy)` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | giao | `B-COMP` |
| 1 | hàng | `I-COMP` |
| 2 | nhanh | `I-COMP` |
| 3 | hàng | `I-COMP` |
| 4 | đúng | `I-COMP` |
| 5 | mẫu,có | `I-COMP` |
| 6 | điều | `O` |
| 7 | hơi | `O` |
| 8 | chảy | `O` |
| 9 | ,nóng | `O` |
| 10 | chắc | `O` |
| 11 | do | `O` |
| 12 | giao | `O` |
| 13 | giữa | `O` |
| 14 | trưa(mà | `O` |
| 15 | sao | `B-COMP` |
| 16 | nhìn | `I-COMP` |
| 17 | ảnh | `I-COMP` |
| 18 | thấy | `I-COMP` |
| 19 | có | `I-COMP` |
| 20 | quà | `I-COMP` |
| 21 | tặng | `I-COMP` |
| 22 | kèm | `I-COMP` |
| 23 | giờ | `I-COMP` |
| 24 | nhận | `I-COMP` |
| 25 | hàng | `I-COMP` |
| 26 | rồi | `I-COMP` |
| 27 | không | `I-COMP` |
| 28 | thấy) | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (69.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 66. `train_001179`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> ổn, nhưng form không được chuẩn.

**Spans:**

- #0 [10:31] `form không được chuẩn` label=`COMP`

**Reason:** Cụm 'form không được chuẩn' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | ổn, | `O` |
| 1 | nhưng | `O` |
| 2 | form | `B-COMP` |
| 3 | không | `I-COMP` |
| 4 | được | `I-COMP` |
| 5 | chuẩn. | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (66.7%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 67. `train_004035`

- Domain: `app`
- Split: `train`

**Text gốc:**

> sử dụng zing id đăng nhập không được , cứ báo mật khẩu hoặc tài khoảng không chính xác , tưởng mình nhập sai đi lên trang zing id lấy mật khẩu qua đăng nhập cũng không được , nghi là lỗi do mật khẩu lên trang chủ đổi lại vào đăng nhập game lại báo mật khẩu hoặc tài khoảng không chính xác bình chọn   1star   cho... bài đánh giá đầy đủ

**Spans:**

- #0 [0:36] `sử dụng zing id đăng nhập không được` label=`COMP`
- #1 [89:172] `tưởng mình nhập sai đi lên trang zing id lấy mật khẩu qua đăng nhập cũng không được` label=`COMP`
- #2 [175:312] `nghi là lỗi do mật khẩu lên trang chủ đổi lại vào đăng nhập game lại báo mật khẩu hoặc tài khoảng không chính xác bình chọn   1star   cho` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | sử | `B-COMP` |
| 1 | dụng | `I-COMP` |
| 2 | zing | `I-COMP` |
| 3 | id | `I-COMP` |
| 4 | đăng | `I-COMP` |
| 5 | nhập | `I-COMP` |
| 6 | không | `I-COMP` |
| 7 | được | `I-COMP` |
| 8 | , | `O` |
| 9 | cứ | `O` |
| 10 | báo | `O` |
| 11 | mật | `O` |
| 12 | khẩu | `O` |
| 13 | hoặc | `O` |
| 14 | tài | `O` |
| 15 | khoảng | `O` |
| 16 | không | `O` |
| 17 | chính | `O` |
| 18 | xác | `O` |
| 19 | , | `O` |
| 20 | tưởng | `B-COMP` |
| 21 | mình | `I-COMP` |
| 22 | nhập | `I-COMP` |
| 23 | sai | `I-COMP` |
| 24 | đi | `I-COMP` |
| 25 | lên | `I-COMP` |
| 26 | trang | `I-COMP` |
| 27 | zing | `I-COMP` |
| 28 | id | `I-COMP` |
| 29 | lấy | `I-COMP` |
| 30 | mật | `I-COMP` |
| 31 | khẩu | `I-COMP` |
| 32 | qua | `I-COMP` |
| 33 | đăng | `I-COMP` |
| 34 | nhập | `I-COMP` |
| 35 | cũng | `I-COMP` |
| 36 | không | `I-COMP` |
| 37 | được | `I-COMP` |
| 38 | , | `O` |
| 39 | nghi | `B-COMP` |
| 40 | là | `I-COMP` |
| 41 | lỗi | `I-COMP` |
| 42 | do | `I-COMP` |
| 43 | mật | `I-COMP` |
| 44 | khẩu | `I-COMP` |
| 45 | lên | `I-COMP` |
| 46 | trang | `I-COMP` |
| 47 | chủ | `I-COMP` |
| 48 | đổi | `I-COMP` |
| 49 | lại | `I-COMP` |
| 50 | vào | `I-COMP` |
| 51 | đăng | `I-COMP` |
| 52 | nhập | `I-COMP` |
| 53 | game | `I-COMP` |
| 54 | lại | `I-COMP` |
| 55 | báo | `I-COMP` |
| 56 | mật | `I-COMP` |
| 57 | khẩu | `I-COMP` |
| 58 | hoặc | `I-COMP` |
| 59 | tài | `I-COMP` |
| 60 | khoảng | `I-COMP` |
| 61 | không | `I-COMP` |
| 62 | chính | `I-COMP` |
| 63 | xác | `I-COMP` |
| 64 | bình | `I-COMP` |
| 65 | chọn | `I-COMP` |
| 66 | 1star | `I-COMP` |
| 67 | cho... | `I-COMP` |
| 68 | bài | `O` |
| 69 | đánh | `O` |
| 70 | giá | `O` |
| 71 | đầy | `O` |
| 72 | đủ | `O` |

**Heuristic warnings:**

- span #1 quá dài (18 tokens >= 15)
- span #2 quá dài (29 tokens >= 15)
- tỉ lệ COMP token > 60% (75.3%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 68. `train_000332`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đặt  cỡ  39-40 giao  cỡ  37-38..... muốn giao gì là giao ... làm ăn ẩu .... không uy tín

**Spans:**

- #0 [0:30] `đặt  cỡ  39-40 giao  cỡ  37-38` label=`COMP`
- #1 [61:70] `làm ăn ẩu` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đặt | `B-COMP` |
| 1 | cỡ | `I-COMP` |
| 2 | 39-40 | `I-COMP` |
| 3 | giao | `I-COMP` |
| 4 | cỡ | `I-COMP` |
| 5 | 37-38..... | `I-COMP` |
| 6 | muốn | `O` |
| 7 | giao | `O` |
| 8 | gì | `O` |
| 9 | là | `O` |
| 10 | giao | `O` |
| 11 | ... | `O` |
| 12 | làm | `B-COMP` |
| 13 | ăn | `I-COMP` |
| 14 | ẩu | `I-COMP` |
| 15 | .... | `O` |
| 16 | không | `O` |
| 17 | uy | `O` |
| 18 | tín | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 69. `train_001278`

- Domain: `app`
- Split: `train`

**Text gốc:**

> mọi người không nên đăng kí học online nhé tải sử dụng thôi chứ giáo viên hỗ trợ gần như không có tác dụng gì mấy đâu bài giảng xem cũng hết sức bình thường không hẳn là dễ hiểu lắm khi nên bài cao, mọi người có thể rất sánh với các video hướng dẫn khác trên mạng thì video giảng bài không hữu ích lắm, n... bài đánh giá đầy đủ

**Spans:**

- #0 [0:197] `mọi người không nên đăng kí học online nhé tải sử dụng thôi chứ giáo viên hỗ trợ gần như không có tác dụng gì mấy đâu bài giảng xem cũng hết sức bình thường không hẳn là dễ hiểu lắm khi nên bài cao` label=`COMP`

**Reason:** Cụm 'mọi người không nên đăng kí học online nhé tải sử dụng thôi chứ giáo viên hỗ trợ gần như không có tác dụng gì mấy đâu bài giảng xem cũng hết sức bình thường không hẳn là dễ hiểu lắm khi nên bài cao' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mọi | `B-COMP` |
| 1 | người | `I-COMP` |
| 2 | không | `I-COMP` |
| 3 | nên | `I-COMP` |
| 4 | đăng | `I-COMP` |
| 5 | kí | `I-COMP` |
| 6 | học | `I-COMP` |
| 7 | online | `I-COMP` |
| 8 | nhé | `I-COMP` |
| 9 | tải | `I-COMP` |
| 10 | sử | `I-COMP` |
| 11 | dụng | `I-COMP` |
| 12 | thôi | `I-COMP` |
| 13 | chứ | `I-COMP` |
| 14 | giáo | `I-COMP` |
| 15 | viên | `I-COMP` |
| 16 | hỗ | `I-COMP` |
| 17 | trợ | `I-COMP` |
| 18 | gần | `I-COMP` |
| 19 | như | `I-COMP` |
| 20 | không | `I-COMP` |
| 21 | có | `I-COMP` |
| 22 | tác | `I-COMP` |
| 23 | dụng | `I-COMP` |
| 24 | gì | `I-COMP` |
| 25 | mấy | `I-COMP` |
| 26 | đâu | `I-COMP` |
| 27 | bài | `I-COMP` |
| 28 | giảng | `I-COMP` |
| 29 | xem | `I-COMP` |
| 30 | cũng | `I-COMP` |
| 31 | hết | `I-COMP` |
| 32 | sức | `I-COMP` |
| 33 | bình | `I-COMP` |
| 34 | thường | `I-COMP` |
| 35 | không | `I-COMP` |
| 36 | hẳn | `I-COMP` |
| 37 | là | `I-COMP` |
| 38 | dễ | `I-COMP` |
| 39 | hiểu | `I-COMP` |
| 40 | lắm | `I-COMP` |
| 41 | khi | `I-COMP` |
| 42 | nên | `I-COMP` |
| 43 | bài | `I-COMP` |
| 44 | cao, | `I-COMP` |
| 45 | mọi | `O` |
| 46 | người | `O` |
| 47 | có | `O` |
| 48 | thể | `O` |
| 49 | rất | `O` |
| 50 | sánh | `O` |
| 51 | với | `O` |
| 52 | các | `O` |
| 53 | video | `O` |
| 54 | hướng | `O` |
| 55 | dẫn | `O` |
| 56 | khác | `O` |
| 57 | trên | `O` |
| 58 | mạng | `O` |
| 59 | thì | `O` |
| 60 | video | `O` |
| 61 | giảng | `O` |
| 62 | bài | `O` |
| 63 | không | `O` |
| 64 | hữu | `O` |
| 65 | ích | `O` |
| 66 | lắm, | `O` |
| 67 | n... | `O` |
| 68 | bài | `O` |
| 69 | đánh | `O` |
| 70 | giá | `O` |
| 71 | đầy | `O` |
| 72 | đủ | `O` |

**Heuristic warnings:**

- span #0 quá dài (45 tokens >= 15)
- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (61.6%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 70. `train_002790`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> hàng chuẩn xài tốt giao hơi lâu

**Spans:**

- #0 [0:31] `hàng chuẩn xài tốt giao hơi lâu` label=`COMP`

**Reason:** Cụm 'hàng chuẩn xài tốt giao hơi lâu' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hàng | `B-COMP` |
| 1 | chuẩn | `I-COMP` |
| 2 | xài | `I-COMP` |
| 3 | tốt | `I-COMP` |
| 4 | giao | `I-COMP` |
| 5 | hơi | `I-COMP` |
| 6 | lâu | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 71. `train_000391`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> dù quá yếu

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | dù | `O` |
| 1 | quá | `O` |
| 2 | yếu | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 72. `train_000716`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> mình đặt 115 nhưng lại giao màu 125

**Spans:**

- #0 [19:35] `lại giao màu 125` label=`COMP`

**Reason:** Cụm 'lại giao màu 125' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mình | `O` |
| 1 | đặt | `O` |
| 2 | 115 | `O` |
| 3 | nhưng | `O` |
| 4 | lại | `B-COMP` |
| 5 | giao | `I-COMP` |
| 6 | màu | `I-COMP` |
| 7 | 125 | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 73. `train_002330`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> giao đúng hàng . gói kĩ . tốt. màu khá sáng nếu đánh nên lấy ít lại nhưng mà cây son tặng của tôi đâu . lúc đặt thì trên đó có ghi tặng cây son . sao giờ chỉ có một chai này thôi vậy . không hài lòng à nghen 🥴

**Spans:**

- #0 [0:14] `giao đúng hàng` label=`COMP`
- #1 [104:143] `lúc đặt thì trên đó có ghi tặng cây son` label=`COMP`
- #2 [146:182] `sao giờ chỉ có một chai này thôi vậy` label=`COMP`
- #3 [185:209] `không hài lòng à nghen 🥴` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | giao | `B-COMP` |
| 1 | đúng | `I-COMP` |
| 2 | hàng | `I-COMP` |
| 3 | . | `O` |
| 4 | gói | `O` |
| 5 | kĩ | `O` |
| 6 | . | `O` |
| 7 | tốt. | `O` |
| 8 | màu | `O` |
| 9 | khá | `O` |
| 10 | sáng | `O` |
| 11 | nếu | `O` |
| 12 | đánh | `O` |
| 13 | nên | `O` |
| 14 | lấy | `O` |
| 15 | ít | `O` |
| 16 | lại | `O` |
| 17 | nhưng | `O` |
| 18 | mà | `O` |
| 19 | cây | `O` |
| 20 | son | `O` |
| 21 | tặng | `O` |
| 22 | của | `O` |
| 23 | tôi | `O` |
| 24 | đâu | `O` |
| 25 | . | `O` |
| 26 | lúc | `B-COMP` |
| 27 | đặt | `I-COMP` |
| 28 | thì | `I-COMP` |
| 29 | trên | `I-COMP` |
| 30 | đó | `I-COMP` |
| 31 | có | `I-COMP` |
| 32 | ghi | `I-COMP` |
| 33 | tặng | `I-COMP` |
| 34 | cây | `I-COMP` |
| 35 | son | `I-COMP` |
| 36 | . | `O` |
| 37 | sao | `B-COMP` |
| 38 | giờ | `I-COMP` |
| 39 | chỉ | `I-COMP` |
| 40 | có | `I-COMP` |
| 41 | một | `I-COMP` |
| 42 | chai | `I-COMP` |
| 43 | này | `I-COMP` |
| 44 | thôi | `I-COMP` |
| 45 | vậy | `I-COMP` |
| 46 | . | `O` |
| 47 | không | `B-COMP` |
| 48 | hài | `I-COMP` |
| 49 | lòng | `I-COMP` |
| 50 | à | `I-COMP` |
| 51 | nghen | `I-COMP` |
| 52 | 🥴 | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 74. `train_000427`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> thấy để tăng trai nước tẩy trang nhỏ mà không thấy

**Spans:**

- #0 [40:50] `không thấy` label=`COMP`

**Reason:** Cụm 'không thấy' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | thấy | `O` |
| 1 | để | `O` |
| 2 | tăng | `O` |
| 3 | trai | `O` |
| 4 | nước | `O` |
| 5 | tẩy | `O` |
| 6 | trang | `O` |
| 7 | nhỏ | `O` |
| 8 | mà | `O` |
| 9 | không | `B-COMP` |
| 10 | thấy | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 75. `train_001364`

- Domain: `app`
- Split: `train`

**Text gốc:**

> tôi không hiểu vì sao facebOk lại bắt xác nhận danh tính và không cho người dùng đổi tên, mà lại bắt buộc dùng đúng tên của mình, tôi thấy khá khó chịu về điều này, cứ cho là vì facebOk muốn  quả nó lý chặt hơn để tránh những tài khoản giả mạo đi, nhưng mà gần đây lại có vấn đề xảy ra làm tôi càng k... bài đánh giá đầy đủ

**Spans:**

- #0 [0:88] `tôi không hiểu vì sao facebOk lại bắt xác nhận danh tính và không cho người dùng đổi tên` label=`COMP`
- #1 [130:163] `tôi thấy khá khó chịu về điều này` label=`COMP`
- #2 [165:246] `cứ cho là vì facebOk muốn  quả nó lý chặt hơn để tránh những tài khoản giả mạo đi` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tôi | `B-COMP` |
| 1 | không | `I-COMP` |
| 2 | hiểu | `I-COMP` |
| 3 | vì | `I-COMP` |
| 4 | sao | `I-COMP` |
| 5 | facebOk | `I-COMP` |
| 6 | lại | `I-COMP` |
| 7 | bắt | `I-COMP` |
| 8 | xác | `I-COMP` |
| 9 | nhận | `I-COMP` |
| 10 | danh | `I-COMP` |
| 11 | tính | `I-COMP` |
| 12 | và | `I-COMP` |
| 13 | không | `I-COMP` |
| 14 | cho | `I-COMP` |
| 15 | người | `I-COMP` |
| 16 | dùng | `I-COMP` |
| 17 | đổi | `I-COMP` |
| 18 | tên, | `I-COMP` |
| 19 | mà | `O` |
| 20 | lại | `O` |
| 21 | bắt | `O` |
| 22 | buộc | `O` |
| 23 | dùng | `O` |
| 24 | đúng | `O` |
| 25 | tên | `O` |
| 26 | của | `O` |
| 27 | mình, | `O` |
| 28 | tôi | `B-COMP` |
| 29 | thấy | `I-COMP` |
| 30 | khá | `I-COMP` |
| 31 | khó | `I-COMP` |
| 32 | chịu | `I-COMP` |
| 33 | về | `I-COMP` |
| 34 | điều | `I-COMP` |
| 35 | này, | `I-COMP` |
| 36 | cứ | `B-COMP` |
| 37 | cho | `I-COMP` |
| 38 | là | `I-COMP` |
| 39 | vì | `I-COMP` |
| 40 | facebOk | `I-COMP` |
| 41 | muốn | `I-COMP` |
| 42 | quả | `I-COMP` |
| 43 | nó | `I-COMP` |
| 44 | lý | `I-COMP` |
| 45 | chặt | `I-COMP` |
| 46 | hơn | `I-COMP` |
| 47 | để | `I-COMP` |
| 48 | tránh | `I-COMP` |
| 49 | những | `I-COMP` |
| 50 | tài | `I-COMP` |
| 51 | khoản | `I-COMP` |
| 52 | giả | `I-COMP` |
| 53 | mạo | `I-COMP` |
| 54 | đi, | `I-COMP` |
| 55 | nhưng | `O` |
| 56 | mà | `O` |
| 57 | gần | `O` |
| 58 | đây | `O` |
| 59 | lại | `O` |
| 60 | có | `O` |
| 61 | vấn | `O` |
| 62 | đề | `O` |
| 63 | xảy | `O` |
| 64 | ra | `O` |
| 65 | làm | `O` |
| 66 | tôi | `O` |
| 67 | càng | `O` |
| 68 | k... | `O` |
| 69 | bài | `O` |
| 70 | đánh | `O` |
| 71 | giá | `O` |
| 72 | đầy | `O` |
| 73 | đủ | `O` |

**Heuristic warnings:**

- span #0 quá dài (19 tokens >= 15)
- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- span #2 quá dài (19 tokens >= 15)
- tỉ lệ COMP token > 60% (62.2%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 76. `train_003686`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> chưa nhận hàng ... đã thông báo giao hàng thành công

**Spans:**

- #0 [19:52] `đã thông báo giao hàng thành công` label=`COMP`

**Reason:** Cụm 'đã thông báo giao hàng thành công' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | chưa | `O` |
| 1 | nhận | `O` |
| 2 | hàng | `O` |
| 3 | ... | `O` |
| 4 | đã | `B-COMP` |
| 5 | thông | `I-COMP` |
| 6 | báo | `I-COMP` |
| 7 | giao | `I-COMP` |
| 8 | hàng | `I-COMP` |
| 9 | thành | `I-COMP` |
| 10 | công | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (63.6%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 77. `train_001106`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> máy xài đươc ,không có tai nghe

**Spans:**

- #0 [14:31] `không có tai nghe` label=`COMP`

**Reason:** Cụm 'không có tai nghe' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | máy | `O` |
| 1 | xài | `O` |
| 2 | đươc | `O` |
| 3 | ,không | `B-COMP` |
| 4 | có | `I-COMP` |
| 5 | tai | `I-COMP` |
| 6 | nghe | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 78. `train_003066`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> mua sản phẩm với giá khả rẻ nhưng không có quà tặng kèm. mở hộp hàng mà thấy hụt hẫng ghê gớm. không biết quá trình đóng gói có vấn đề gì không nhỉ. dù sao mình cũng sẽ bình chọn  1star   vì không có quà tặng kèm.

**Spans:**

- #0 [34:55] `không có quà tặng kèm` label=`COMP`
- #1 [72:93] `thấy hụt hẫng ghê gớm` label=`COMP`
- #2 [149:212] `dù sao mình cũng sẽ bình chọn  1star   vì không có quà tặng kèm` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mua | `O` |
| 1 | sản | `O` |
| 2 | phẩm | `O` |
| 3 | với | `O` |
| 4 | giá | `O` |
| 5 | khả | `O` |
| 6 | rẻ | `O` |
| 7 | nhưng | `O` |
| 8 | không | `B-COMP` |
| 9 | có | `I-COMP` |
| 10 | quà | `I-COMP` |
| 11 | tặng | `I-COMP` |
| 12 | kèm. | `I-COMP` |
| 13 | mở | `O` |
| 14 | hộp | `O` |
| 15 | hàng | `O` |
| 16 | mà | `O` |
| 17 | thấy | `B-COMP` |
| 18 | hụt | `I-COMP` |
| 19 | hẫng | `I-COMP` |
| 20 | ghê | `I-COMP` |
| 21 | gớm. | `I-COMP` |
| 22 | không | `O` |
| 23 | biết | `O` |
| 24 | quá | `O` |
| 25 | trình | `O` |
| 26 | đóng | `O` |
| 27 | gói | `O` |
| 28 | có | `O` |
| 29 | vấn | `O` |
| 30 | đề | `O` |
| 31 | gì | `O` |
| 32 | không | `O` |
| 33 | nhỉ. | `O` |
| 34 | dù | `B-COMP` |
| 35 | sao | `I-COMP` |
| 36 | mình | `I-COMP` |
| 37 | cũng | `I-COMP` |
| 38 | sẽ | `I-COMP` |
| 39 | bình | `I-COMP` |
| 40 | chọn | `I-COMP` |
| 41 | 1star | `I-COMP` |
| 42 | vì | `I-COMP` |
| 43 | không | `I-COMP` |
| 44 | có | `I-COMP` |
| 45 | quà | `I-COMP` |
| 46 | tặng | `I-COMP` |
| 47 | kèm. | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 79. `train_002866`

- Domain: `app`
- Split: `train`

**Text gốc:**

> game trải nghiệm rất tuyệt vời. nhưng bị hack nhiều quá với lại có những người chơi dùng thiết bị hổ trợ còn giả lập nữa, chơi như vậy thì những người chơi bằng di động hay máy tính bảng thì chắc không địch lại nổi,,,, huy vọng nhà phát hành game xem lại... vì một cộng đồng game công bằng...

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | game | `O` |
| 1 | trải | `O` |
| 2 | nghiệm | `O` |
| 3 | rất | `O` |
| 4 | tuyệt | `O` |
| 5 | vời. | `O` |
| 6 | nhưng | `O` |
| 7 | bị | `O` |
| 8 | hack | `O` |
| 9 | nhiều | `O` |
| 10 | quá | `O` |
| 11 | với | `O` |
| 12 | lại | `O` |
| 13 | có | `O` |
| 14 | những | `O` |
| 15 | người | `O` |
| 16 | chơi | `O` |
| 17 | dùng | `O` |
| 18 | thiết | `O` |
| 19 | bị | `O` |
| 20 | hổ | `O` |
| 21 | trợ | `O` |
| 22 | còn | `O` |
| 23 | giả | `O` |
| 24 | lập | `O` |
| 25 | nữa, | `O` |
| 26 | chơi | `O` |
| 27 | như | `O` |
| 28 | vậy | `O` |
| 29 | thì | `O` |
| 30 | những | `O` |
| 31 | người | `O` |
| 32 | chơi | `O` |
| 33 | bằng | `O` |
| 34 | di | `O` |
| 35 | động | `O` |
| 36 | hay | `O` |
| 37 | máy | `O` |
| 38 | tính | `O` |
| 39 | bảng | `O` |
| 40 | thì | `O` |
| 41 | chắc | `O` |
| 42 | không | `O` |
| 43 | địch | `O` |
| 44 | lại | `O` |
| 45 | nổi,,,, | `O` |
| 46 | huy | `O` |
| 47 | vọng | `O` |
| 48 | nhà | `O` |
| 49 | phát | `O` |
| 50 | hành | `O` |
| 51 | game | `O` |
| 52 | xem | `O` |
| 53 | lại... | `O` |
| 54 | vì | `O` |
| 55 | một | `O` |
| 56 | cộng | `O` |
| 57 | đồng | `O` |
| 58 | game | `O` |
| 59 | công | `O` |
| 60 | bằng... | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 80. `train_001469`

- Domain: `app`
- Split: `train`

**Text gốc:**

> ứng dụng đơn giản mà hiệu  quả . tiếc là chưa có tiếng việt. mình chạy grab đã từng dùng qua rất nhiều aPs gOgle maps, here we go, sygic...nhưng  quá ze ưng hơn cả.

**Spans:**

- #0 [0:30] `ứng dụng đơn giản mà hiệu  quả` label=`COMP`

**Reason:** Cụm 'ứng dụng đơn giản mà hiệu  quả' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | ứng | `B-COMP` |
| 1 | dụng | `I-COMP` |
| 2 | đơn | `I-COMP` |
| 3 | giản | `I-COMP` |
| 4 | mà | `I-COMP` |
| 5 | hiệu | `I-COMP` |
| 6 | quả | `I-COMP` |
| 7 | . | `O` |
| 8 | tiếc | `O` |
| 9 | là | `O` |
| 10 | chưa | `O` |
| 11 | có | `O` |
| 12 | tiếng | `O` |
| 13 | việt. | `O` |
| 14 | mình | `O` |
| 15 | chạy | `O` |
| 16 | grab | `O` |
| 17 | đã | `O` |
| 18 | từng | `O` |
| 19 | dùng | `O` |
| 20 | qua | `O` |
| 21 | rất | `O` |
| 22 | nhiều | `O` |
| 23 | aPs | `O` |
| 24 | gOgle | `O` |
| 25 | maps, | `O` |
| 26 | here | `O` |
| 27 | we | `O` |
| 28 | go, | `O` |
| 29 | sygic...nhưng | `O` |
| 30 | quá | `O` |
| 31 | ze | `O` |
| 32 | ưng | `O` |
| 33 | hơn | `O` |
| 34 | cả. | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 81. `train_000017`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> mới dùng 2 ngày chưa thấy hiệu  quả  lắm.  được  cái nhìn da min và láng hơn. tinh chất thấm nhanh và không gây dầu nữa. mỗi tội lazada vận chuyển hàng tẹ quá, không hết vỏ hộp bung lọ tinh chất ra ngoài làm mình cứ lo hàng giả nhưng test lại với thuốc sát trùng thì vẫn đúng. hy vọng dùng một thời gian nữa da sẽ có cải thiện

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mới | `O` |
| 1 | dùng | `O` |
| 2 | 2 | `O` |
| 3 | ngày | `O` |
| 4 | chưa | `O` |
| 5 | thấy | `O` |
| 6 | hiệu | `O` |
| 7 | quả | `O` |
| 8 | lắm. | `O` |
| 9 | được | `O` |
| 10 | cái | `O` |
| 11 | nhìn | `O` |
| 12 | da | `O` |
| 13 | min | `O` |
| 14 | và | `O` |
| 15 | láng | `O` |
| 16 | hơn. | `O` |
| 17 | tinh | `O` |
| 18 | chất | `O` |
| 19 | thấm | `O` |
| 20 | nhanh | `O` |
| 21 | và | `O` |
| 22 | không | `O` |
| 23 | gây | `O` |
| 24 | dầu | `O` |
| 25 | nữa. | `O` |
| 26 | mỗi | `O` |
| 27 | tội | `O` |
| 28 | lazada | `O` |
| 29 | vận | `O` |
| 30 | chuyển | `O` |
| 31 | hàng | `O` |
| 32 | tẹ | `O` |
| 33 | quá, | `O` |
| 34 | không | `O` |
| 35 | hết | `O` |
| 36 | vỏ | `O` |
| 37 | hộp | `O` |
| 38 | bung | `O` |
| 39 | lọ | `O` |
| 40 | tinh | `O` |
| 41 | chất | `O` |
| 42 | ra | `O` |
| 43 | ngoài | `O` |
| 44 | làm | `O` |
| 45 | mình | `O` |
| 46 | cứ | `O` |
| 47 | lo | `O` |
| 48 | hàng | `O` |
| 49 | giả | `O` |
| 50 | nhưng | `O` |
| 51 | test | `O` |
| 52 | lại | `O` |
| 53 | với | `O` |
| 54 | thuốc | `O` |
| 55 | sát | `O` |
| 56 | trùng | `O` |
| 57 | thì | `O` |
| 58 | vẫn | `O` |
| 59 | đúng. | `O` |
| 60 | hy | `O` |
| 61 | vọng | `O` |
| 62 | dùng | `O` |
| 63 | một | `O` |
| 64 | thời | `O` |
| 65 | gian | `O` |
| 66 | nữa | `O` |
| 67 | da | `O` |
| 68 | sẽ | `O` |
| 69 | có | `O` |
| 70 | cải | `O` |
| 71 | thiện | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 82. `train_000003`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> máy khá đẹp,pin trâu vân tay nhạy nhận diện khuôn mặt nhanh nói chung ổn.tuy chơi game frE fire bị chậm khung hình không mượt lắm nhưng với giá giẫm ngày 1111 được aD mã giảm giá 200k còn hơn 2tr6 thì vậy là ngon rồi

**Spans:**

- #0 [77:216] `chơi game frE fire bị chậm khung hình không mượt lắm nhưng với giá giẫm ngày 1111 được aD mã giảm giá 200k còn hơn 2tr6 thì vậy là ngon rồi` label=`COMP`

**Reason:** Cụm 'chơi game frE fire bị chậm khung hình không mượt lắm nhưng với giá giẫm ngày 1111 được aD mã giảm giá 200k còn hơn 2tr6 thì vậy là ngon rồi' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | máy | `O` |
| 1 | khá | `O` |
| 2 | đẹp,pin | `O` |
| 3 | trâu | `O` |
| 4 | vân | `O` |
| 5 | tay | `O` |
| 6 | nhạy | `O` |
| 7 | nhận | `O` |
| 8 | diện | `O` |
| 9 | khuôn | `O` |
| 10 | mặt | `O` |
| 11 | nhanh | `O` |
| 12 | nói | `O` |
| 13 | chung | `O` |
| 14 | ổn.tuy | `O` |
| 15 | chơi | `B-COMP` |
| 16 | game | `I-COMP` |
| 17 | frE | `I-COMP` |
| 18 | fire | `I-COMP` |
| 19 | bị | `I-COMP` |
| 20 | chậm | `I-COMP` |
| 21 | khung | `I-COMP` |
| 22 | hình | `I-COMP` |
| 23 | không | `I-COMP` |
| 24 | mượt | `I-COMP` |
| 25 | lắm | `I-COMP` |
| 26 | nhưng | `I-COMP` |
| 27 | với | `I-COMP` |
| 28 | giá | `I-COMP` |
| 29 | giẫm | `I-COMP` |
| 30 | ngày | `I-COMP` |
| 31 | 1111 | `I-COMP` |
| 32 | được | `I-COMP` |
| 33 | aD | `I-COMP` |
| 34 | mã | `I-COMP` |
| 35 | giảm | `I-COMP` |
| 36 | giá | `I-COMP` |
| 37 | 200k | `I-COMP` |
| 38 | còn | `I-COMP` |
| 39 | hơn | `I-COMP` |
| 40 | 2tr6 | `I-COMP` |
| 41 | thì | `I-COMP` |
| 42 | vậy | `I-COMP` |
| 43 | là | `I-COMP` |
| 44 | ngon | `I-COMP` |
| 45 | rồi | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (31 tokens >= 15)
- tỉ lệ COMP token > 60% (67.4%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 83. `train_000197`

- Domain: `app`
- Split: `train`

**Text gốc:**

> hình ảnh lưu trong album ảnh , nên có thêm tính nắng xoá hình đơn lẻ, trước mắt chỉ có thể xoá cả album ,rất mong cải tiến, để thuận tiện hơn trong việc  quả nó lý ảnh

**Spans:**

- #0 [31:68] `nên có thêm tính nắng xoá hình đơn lẻ` label=`COMP`

**Reason:** Cụm 'nên có thêm tính nắng xoá hình đơn lẻ' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hình | `O` |
| 1 | ảnh | `O` |
| 2 | lưu | `O` |
| 3 | trong | `O` |
| 4 | album | `O` |
| 5 | ảnh | `O` |
| 6 | , | `O` |
| 7 | nên | `B-COMP` |
| 8 | có | `I-COMP` |
| 9 | thêm | `I-COMP` |
| 10 | tính | `I-COMP` |
| 11 | nắng | `I-COMP` |
| 12 | xoá | `I-COMP` |
| 13 | hình | `I-COMP` |
| 14 | đơn | `I-COMP` |
| 15 | lẻ, | `I-COMP` |
| 16 | trước | `O` |
| 17 | mắt | `O` |
| 18 | chỉ | `O` |
| 19 | có | `O` |
| 20 | thể | `O` |
| 21 | xoá | `O` |
| 22 | cả | `O` |
| 23 | album | `O` |
| 24 | ,rất | `O` |
| 25 | mong | `O` |
| 26 | cải | `O` |
| 27 | tiến, | `O` |
| 28 | để | `O` |
| 29 | thuận | `O` |
| 30 | tiện | `O` |
| 31 | hơn | `O` |
| 32 | trong | `O` |
| 33 | việc | `O` |
| 34 | quả | `O` |
| 35 | nó | `O` |
| 36 | lý | `O` |
| 37 | ảnh | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 84. `train_003784`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> nhờ  cửa hàng  kích hoạt bảo hành chính hãng, về đơn hàng không có gì phàn nàn nhưng đóng gói sơ xài vận chuyển móp không

**Spans:**

- #0 [85:121] `đóng gói sơ xài vận chuyển móp không` label=`COMP`

**Reason:** Cụm 'đóng gói sơ xài vận chuyển móp không' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | nhờ | `O` |
| 1 | cửa | `O` |
| 2 | hàng | `O` |
| 3 | kích | `O` |
| 4 | hoạt | `O` |
| 5 | bảo | `O` |
| 6 | hành | `O` |
| 7 | chính | `O` |
| 8 | hãng, | `O` |
| 9 | về | `O` |
| 10 | đơn | `O` |
| 11 | hàng | `O` |
| 12 | không | `O` |
| 13 | có | `O` |
| 14 | gì | `O` |
| 15 | phàn | `O` |
| 16 | nàn | `O` |
| 17 | nhưng | `O` |
| 18 | đóng | `B-COMP` |
| 19 | gói | `I-COMP` |
| 20 | sơ | `I-COMP` |
| 21 | xài | `I-COMP` |
| 22 | vận | `I-COMP` |
| 23 | chuyển | `I-COMP` |
| 24 | móp | `I-COMP` |
| 25 | không | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 85. `train_000545`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> quần đẹp lắm nha mọi người chỉ là hơi ngắn xíu

**Spans:**

- #0 [0:46] `quần đẹp lắm nha mọi người chỉ là hơi ngắn xíu` label=`COMP`

**Reason:** Cụm 'quần đẹp lắm nha mọi người chỉ là hơi ngắn xíu' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | quần | `B-COMP` |
| 1 | đẹp | `I-COMP` |
| 2 | lắm | `I-COMP` |
| 3 | nha | `I-COMP` |
| 4 | mọi | `I-COMP` |
| 5 | người | `I-COMP` |
| 6 | chỉ | `I-COMP` |
| 7 | là | `I-COMP` |
| 8 | hơi | `I-COMP` |
| 9 | ngắn | `I-COMP` |
| 10 | xíu | `I-COMP` |

**Heuristic warnings:**

- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 86. `train_000457`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> sản phẩm dùng rất tốt và hiệu  quả  . giao hàng cũng rất nhanh . nhưng sản phẩm có mùi không được thơm làm khi nhỏ giọt ra tay xài cũng khó chịu. sản phẩm hơi mắc chỉ đợi đến giảm giá mới mua .

**Spans:**

- #0 [38:62] `giao hàng cũng rất nhanh` label=`COMP`
- #1 [71:144] `sản phẩm có mùi không được thơm làm khi nhỏ giọt ra tay xài cũng khó chịu` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | sản | `O` |
| 1 | phẩm | `O` |
| 2 | dùng | `O` |
| 3 | rất | `O` |
| 4 | tốt | `O` |
| 5 | và | `O` |
| 6 | hiệu | `O` |
| 7 | quả | `O` |
| 8 | . | `O` |
| 9 | giao | `B-COMP` |
| 10 | hàng | `I-COMP` |
| 11 | cũng | `I-COMP` |
| 12 | rất | `I-COMP` |
| 13 | nhanh | `I-COMP` |
| 14 | . | `O` |
| 15 | nhưng | `O` |
| 16 | sản | `B-COMP` |
| 17 | phẩm | `I-COMP` |
| 18 | có | `I-COMP` |
| 19 | mùi | `I-COMP` |
| 20 | không | `I-COMP` |
| 21 | được | `I-COMP` |
| 22 | thơm | `I-COMP` |
| 23 | làm | `I-COMP` |
| 24 | khi | `I-COMP` |
| 25 | nhỏ | `I-COMP` |
| 26 | giọt | `I-COMP` |
| 27 | ra | `I-COMP` |
| 28 | tay | `I-COMP` |
| 29 | xài | `I-COMP` |
| 30 | cũng | `I-COMP` |
| 31 | khó | `I-COMP` |
| 32 | chịu. | `I-COMP` |
| 33 | sản | `O` |
| 34 | phẩm | `O` |
| 35 | hơi | `O` |
| 36 | mắc | `O` |
| 37 | chỉ | `O` |
| 38 | đợi | `O` |
| 39 | đến | `O` |
| 40 | giảm | `O` |
| 41 | giá | `O` |
| 42 | mới | `O` |
| 43 | mua | `O` |
| 44 | . | `O` |

**Heuristic warnings:**

- span #1 quá dài (17 tokens >= 15)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 87. `train_003307`

- Domain: `app`
- Split: `train`

**Text gốc:**

> game chơi ăn gian như chó sự kiện giải nhất được 180.000 giải nhì 90.000 giải ba... trong game cày để dành tiền được 44.000 thấy sự kiện giải nhất được nhiều tiền tranh giành giải nhất sữ dụng hết 44.000 mua lượt thêm mua bom hết tiền cuối cùng cũng giành giải nhất. cứ nghĩ xài hết số tiền 44.000 dàn... bài đánh giá đầy đủ

**Spans:**

- None

**Reason:** Không có khiếu nại rõ ràng; đây chủ yếu là góp ý, mong muốn hoặc đề xuất.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | game | `O` |
| 1 | chơi | `O` |
| 2 | ăn | `O` |
| 3 | gian | `O` |
| 4 | như | `O` |
| 5 | chó | `O` |
| 6 | sự | `O` |
| 7 | kiện | `O` |
| 8 | giải | `O` |
| 9 | nhất | `O` |
| 10 | được | `O` |
| 11 | 180.000 | `O` |
| 12 | giải | `O` |
| 13 | nhì | `O` |
| 14 | 90.000 | `O` |
| 15 | giải | `O` |
| 16 | ba... | `O` |
| 17 | trong | `O` |
| 18 | game | `O` |
| 19 | cày | `O` |
| 20 | để | `O` |
| 21 | dành | `O` |
| 22 | tiền | `O` |
| 23 | được | `O` |
| 24 | 44.000 | `O` |
| 25 | thấy | `O` |
| 26 | sự | `O` |
| 27 | kiện | `O` |
| 28 | giải | `O` |
| 29 | nhất | `O` |
| 30 | được | `O` |
| 31 | nhiều | `O` |
| 32 | tiền | `O` |
| 33 | tranh | `O` |
| 34 | giành | `O` |
| 35 | giải | `O` |
| 36 | nhất | `O` |
| 37 | sữ | `O` |
| 38 | dụng | `O` |
| 39 | hết | `O` |
| 40 | 44.000 | `O` |
| 41 | mua | `O` |
| 42 | lượt | `O` |
| 43 | thêm | `O` |
| 44 | mua | `O` |
| 45 | bom | `O` |
| 46 | hết | `O` |
| 47 | tiền | `O` |
| 48 | cuối | `O` |
| 49 | cùng | `O` |
| 50 | cũng | `O` |
| 51 | giành | `O` |
| 52 | giải | `O` |
| 53 | nhất. | `O` |
| 54 | cứ | `O` |
| 55 | nghĩ | `O` |
| 56 | xài | `O` |
| 57 | hết | `O` |
| 58 | số | `O` |
| 59 | tiền | `O` |
| 60 | 44.000 | `O` |
| 61 | dàn... | `O` |
| 62 | bài | `O` |
| 63 | đánh | `O` |
| 64 | giá | `O` |
| 65 | đầy | `O` |
| 66 | đủ | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 88. `train_002813`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> mình đặt 2 đơn là 10 áo,sao  cửa hàng  giao thiếu 2 đơn là 4 áo,rất thất vọng,mong cửa hàng gửi lại số áo đang còn thiếu,ko cho kiểm hàng giờ giao thiếu sản phẩm cho khách rồi

**Spans:**

- #0 [24:63] `sao  cửa hàng  giao thiếu 2 đơn là 4 áo` label=`COMP`
- #1 [121:175] `ko cho kiểm hàng giờ giao thiếu sản phẩm cho khách rồi` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mình | `O` |
| 1 | đặt | `O` |
| 2 | 2 | `O` |
| 3 | đơn | `O` |
| 4 | là | `O` |
| 5 | 10 | `O` |
| 6 | áo,sao | `B-COMP` |
| 7 | cửa | `I-COMP` |
| 8 | hàng | `I-COMP` |
| 9 | giao | `I-COMP` |
| 10 | thiếu | `I-COMP` |
| 11 | 2 | `I-COMP` |
| 12 | đơn | `I-COMP` |
| 13 | là | `I-COMP` |
| 14 | 4 | `I-COMP` |
| 15 | áo,rất | `I-COMP` |
| 16 | thất | `O` |
| 17 | vọng,mong | `O` |
| 18 | cửa | `O` |
| 19 | hàng | `O` |
| 20 | gửi | `O` |
| 21 | lại | `O` |
| 22 | số | `O` |
| 23 | áo | `O` |
| 24 | đang | `O` |
| 25 | còn | `O` |
| 26 | thiếu,ko | `B-COMP` |
| 27 | cho | `I-COMP` |
| 28 | kiểm | `I-COMP` |
| 29 | hàng | `I-COMP` |
| 30 | giờ | `I-COMP` |
| 31 | giao | `I-COMP` |
| 32 | thiếu | `I-COMP` |
| 33 | sản | `I-COMP` |
| 34 | phẩm | `I-COMP` |
| 35 | cho | `I-COMP` |
| 36 | khách | `I-COMP` |
| 37 | rồi | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 89. `train_001488`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> không hiểu sao dùng gần cả tuần rồi nhưng không thấy có dấu hiệu mờ thâm . còn nổi mấy cái mụn li ti nhỏ .có thể là do da mình không hợp

**Spans:**

- #0 [42:72] `không thấy có dấu hiệu mờ thâm` label=`COMP`
- #1 [106:136] `có thể là do da mình không hợp` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | không | `O` |
| 1 | hiểu | `O` |
| 2 | sao | `O` |
| 3 | dùng | `O` |
| 4 | gần | `O` |
| 5 | cả | `O` |
| 6 | tuần | `O` |
| 7 | rồi | `O` |
| 8 | nhưng | `O` |
| 9 | không | `B-COMP` |
| 10 | thấy | `I-COMP` |
| 11 | có | `I-COMP` |
| 12 | dấu | `I-COMP` |
| 13 | hiệu | `I-COMP` |
| 14 | mờ | `I-COMP` |
| 15 | thâm | `I-COMP` |
| 16 | . | `O` |
| 17 | còn | `O` |
| 18 | nổi | `O` |
| 19 | mấy | `O` |
| 20 | cái | `O` |
| 21 | mụn | `O` |
| 22 | li | `O` |
| 23 | ti | `O` |
| 24 | nhỏ | `O` |
| 25 | .có | `B-COMP` |
| 26 | thể | `I-COMP` |
| 27 | là | `I-COMP` |
| 28 | do | `I-COMP` |
| 29 | da | `I-COMP` |
| 30 | mình | `I-COMP` |
| 31 | không | `I-COMP` |
| 32 | hợp | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 90. `train_000152`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> nắp thì bị hở ra. kiểu như hàng cũ. nhìn không  được  mới.

**Spans:**

- #0 [36:57] `nhìn không  được  mới` label=`COMP`

**Reason:** Cụm 'nhìn không  được  mới' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | nắp | `O` |
| 1 | thì | `O` |
| 2 | bị | `O` |
| 3 | hở | `O` |
| 4 | ra. | `O` |
| 5 | kiểu | `O` |
| 6 | như | `O` |
| 7 | hàng | `O` |
| 8 | cũ. | `O` |
| 9 | nhìn | `B-COMP` |
| 10 | không | `I-COMP` |
| 11 | được | `I-COMP` |
| 12 | mới. | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 91. `train_001130`

- Domain: `app`
- Split: `train`

**Text gốc:**

> hiện tại tôi dùng oPo a37 để chơi nhưng vào được khoảng 30s và làm vài thao tác là game bị đứng và không thể làm gì khác ngoài thoát game. dù tôi không chạy thêm ứng dụng ngầm nào của bên thứ ba nữa.

**Spans:**

- #0 [40:137] `vào được khoảng 30s và làm vài thao tác là game bị đứng và không thể làm gì khác ngoài thoát game` label=`COMP`
- #1 [139:198] `dù tôi không chạy thêm ứng dụng ngầm nào của bên thứ ba nữa` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hiện | `O` |
| 1 | tại | `O` |
| 2 | tôi | `O` |
| 3 | dùng | `O` |
| 4 | oPo | `O` |
| 5 | a37 | `O` |
| 6 | để | `O` |
| 7 | chơi | `O` |
| 8 | nhưng | `O` |
| 9 | vào | `B-COMP` |
| 10 | được | `I-COMP` |
| 11 | khoảng | `I-COMP` |
| 12 | 30s | `I-COMP` |
| 13 | và | `I-COMP` |
| 14 | làm | `I-COMP` |
| 15 | vài | `I-COMP` |
| 16 | thao | `I-COMP` |
| 17 | tác | `I-COMP` |
| 18 | là | `I-COMP` |
| 19 | game | `I-COMP` |
| 20 | bị | `I-COMP` |
| 21 | đứng | `I-COMP` |
| 22 | và | `I-COMP` |
| 23 | không | `I-COMP` |
| 24 | thể | `I-COMP` |
| 25 | làm | `I-COMP` |
| 26 | gì | `I-COMP` |
| 27 | khác | `I-COMP` |
| 28 | ngoài | `I-COMP` |
| 29 | thoát | `I-COMP` |
| 30 | game. | `I-COMP` |
| 31 | dù | `B-COMP` |
| 32 | tôi | `I-COMP` |
| 33 | không | `I-COMP` |
| 34 | chạy | `I-COMP` |
| 35 | thêm | `I-COMP` |
| 36 | ứng | `I-COMP` |
| 37 | dụng | `I-COMP` |
| 38 | ngầm | `I-COMP` |
| 39 | nào | `I-COMP` |
| 40 | của | `I-COMP` |
| 41 | bên | `I-COMP` |
| 42 | thứ | `I-COMP` |
| 43 | ba | `I-COMP` |
| 44 | nữa. | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (22 tokens >= 15)
- tỉ lệ COMP token > 60% (80.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 92. `train_003770`

- Domain: `app`
- Split: `train`

**Text gốc:**

> tôi dùng 2 tài khoản facebOk, cài meSenger. trong khi tài khoản cũ vẫn bình thường, tài khoản mới tôi vừa nhắn vài tin bỗng mất hết lịch sử tin nhắn, và người khác gửi tin nhắn có thông báo nhưng mở ra không thấy đâu cả. mỗi lần chuyển tài khoản đăng xuất mất 4-5 phút. đề nghị nC sớm sửa lỗi.

**Spans:**

- #0 [84:148] `tài khoản mới tôi vừa nhắn vài tin bỗng mất hết lịch sử tin nhắn` label=`COMP`
- #1 [196:219] `mở ra không thấy đâu cả` label=`COMP`
- #2 [221:268] `mỗi lần chuyển tài khoản đăng xuất mất 4-5 phút` label=`COMP`
- #3 [270:292] `đề nghị nC sớm sửa lỗi` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tôi | `O` |
| 1 | dùng | `O` |
| 2 | 2 | `O` |
| 3 | tài | `O` |
| 4 | khoản | `O` |
| 5 | facebOk, | `O` |
| 6 | cài | `O` |
| 7 | meSenger. | `O` |
| 8 | trong | `O` |
| 9 | khi | `O` |
| 10 | tài | `O` |
| 11 | khoản | `O` |
| 12 | cũ | `O` |
| 13 | vẫn | `O` |
| 14 | bình | `O` |
| 15 | thường, | `O` |
| 16 | tài | `B-COMP` |
| 17 | khoản | `I-COMP` |
| 18 | mới | `I-COMP` |
| 19 | tôi | `I-COMP` |
| 20 | vừa | `I-COMP` |
| 21 | nhắn | `I-COMP` |
| 22 | vài | `I-COMP` |
| 23 | tin | `I-COMP` |
| 24 | bỗng | `I-COMP` |
| 25 | mất | `I-COMP` |
| 26 | hết | `I-COMP` |
| 27 | lịch | `I-COMP` |
| 28 | sử | `I-COMP` |
| 29 | tin | `I-COMP` |
| 30 | nhắn, | `I-COMP` |
| 31 | và | `O` |
| 32 | người | `O` |
| 33 | khác | `O` |
| 34 | gửi | `O` |
| 35 | tin | `O` |
| 36 | nhắn | `O` |
| 37 | có | `O` |
| 38 | thông | `O` |
| 39 | báo | `O` |
| 40 | nhưng | `O` |
| 41 | mở | `B-COMP` |
| 42 | ra | `I-COMP` |
| 43 | không | `I-COMP` |
| 44 | thấy | `I-COMP` |
| 45 | đâu | `I-COMP` |
| 46 | cả. | `I-COMP` |
| 47 | mỗi | `B-COMP` |
| 48 | lần | `I-COMP` |
| 49 | chuyển | `I-COMP` |
| 50 | tài | `I-COMP` |
| 51 | khoản | `I-COMP` |
| 52 | đăng | `I-COMP` |
| 53 | xuất | `I-COMP` |
| 54 | mất | `I-COMP` |
| 55 | 4-5 | `I-COMP` |
| 56 | phút. | `I-COMP` |
| 57 | đề | `B-COMP` |
| 58 | nghị | `I-COMP` |
| 59 | nC | `I-COMP` |
| 60 | sớm | `I-COMP` |
| 61 | sửa | `I-COMP` |
| 62 | lỗi. | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (15 tokens >= 15)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 93. `train_001882`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> cổ may hơi lỗi, ổn trong tầm giá

**Spans:**

- #0 [0:14] `cổ may hơi lỗi` label=`COMP`

**Reason:** Cụm 'cổ may hơi lỗi' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | cổ | `B-COMP` |
| 1 | may | `I-COMP` |
| 2 | hơi | `I-COMP` |
| 3 | lỗi, | `I-COMP` |
| 4 | ổn | `O` |
| 5 | trong | `O` |
| 6 | tầm | `O` |
| 7 | giá | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 94. `train_000061`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

>  cửa hàng  giao thiếu quà tặng là nước tẩy trang rồi!

**Spans:**

- #0 [1:52] `cửa hàng  giao thiếu quà tặng là nước tẩy trang rồi` label=`COMP`

**Reason:** Cụm 'cửa hàng  giao thiếu quà tặng là nước tẩy trang rồi' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | cửa | `B-COMP` |
| 1 | hàng | `I-COMP` |
| 2 | giao | `I-COMP` |
| 3 | thiếu | `I-COMP` |
| 4 | quà | `I-COMP` |
| 5 | tặng | `I-COMP` |
| 6 | là | `I-COMP` |
| 7 | nước | `I-COMP` |
| 8 | tẩy | `I-COMP` |
| 9 | trang | `I-COMP` |
| 10 | rồi! | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 95. `train_001077`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> vải không đẹp lắm nhưng củng được

**Spans:**

- #0 [0:33] `vải không đẹp lắm nhưng củng được` label=`COMP`

**Reason:** Cụm 'vải không đẹp lắm nhưng củng được' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | vải | `B-COMP` |
| 1 | không | `I-COMP` |
| 2 | đẹp | `I-COMP` |
| 3 | lắm | `I-COMP` |
| 4 | nhưng | `I-COMP` |
| 5 | củng | `I-COMP` |
| 6 | được | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 96. `train_001684`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> chất liệu vải ok, khích thước hơi nhỏ

**Spans:**

- #0 [18:37] `khích thước hơi nhỏ` label=`COMP`

**Reason:** Cụm 'khích thước hơi nhỏ' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | chất | `O` |
| 1 | liệu | `O` |
| 2 | vải | `O` |
| 3 | ok, | `O` |
| 4 | khích | `B-COMP` |
| 5 | thước | `I-COMP` |
| 6 | hơi | `I-COMP` |
| 7 | nhỏ | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 97. `train_004087`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> chất lượng sản phẩm tốt theo đơn hàng là có  sản phẩm  tặng kèm nhưng giao về

**Spans:**

- #0 [0:77] `chất lượng sản phẩm tốt theo đơn hàng là có  sản phẩm  tặng kèm nhưng giao về` label=`COMP`

**Reason:** Cụm 'chất lượng sản phẩm tốt theo đơn hàng là có  sản phẩm  tặng kèm nhưng giao về' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | chất | `B-COMP` |
| 1 | lượng | `I-COMP` |
| 2 | sản | `I-COMP` |
| 3 | phẩm | `I-COMP` |
| 4 | tốt | `I-COMP` |
| 5 | theo | `I-COMP` |
| 6 | đơn | `I-COMP` |
| 7 | hàng | `I-COMP` |
| 8 | là | `I-COMP` |
| 9 | có | `I-COMP` |
| 10 | sản | `I-COMP` |
| 11 | phẩm | `I-COMP` |
| 12 | tặng | `I-COMP` |
| 13 | kèm | `I-COMP` |
| 14 | nhưng | `I-COMP` |
| 15 | giao | `I-COMP` |
| 16 | về | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (17 tokens >= 15)
- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 98. `train_003352`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> sản phẩm như hình như tôi không được tặng kèm sản phẩm. ☹🙂

**Spans:**

- #0 [0:54] `sản phẩm như hình như tôi không được tặng kèm sản phẩm` label=`COMP`

**Reason:** Cụm 'sản phẩm như hình như tôi không được tặng kèm sản phẩm' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | sản | `B-COMP` |
| 1 | phẩm | `I-COMP` |
| 2 | như | `I-COMP` |
| 3 | hình | `I-COMP` |
| 4 | như | `I-COMP` |
| 5 | tôi | `I-COMP` |
| 6 | không | `I-COMP` |
| 7 | được | `I-COMP` |
| 8 | tặng | `I-COMP` |
| 9 | kèm | `I-COMP` |
| 10 | sản | `I-COMP` |
| 11 | phẩm. | `I-COMP` |
| 12 | ☹🙂 | `O` |

**Heuristic warnings:**

- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (92.3%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 99. `train_002079`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đồ đẹp như bi giờ lỗi ở cổ áo không  được  không lắm nhưng còn lại bộ này cũng đẹp (•‿•)(✷‿✷)

**Spans:**

- #0 [0:93] `đồ đẹp như bi giờ lỗi ở cổ áo không  được  không lắm nhưng còn lại bộ này cũng đẹp (•‿•)(✷‿✷)` label=`COMP`

**Reason:** Cụm 'đồ đẹp như bi giờ lỗi ở cổ áo không  được  không lắm nhưng còn lại bộ này cũng đẹp (•‿•)(✷‿✷)' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đồ | `B-COMP` |
| 1 | đẹp | `I-COMP` |
| 2 | như | `I-COMP` |
| 3 | bi | `I-COMP` |
| 4 | giờ | `I-COMP` |
| 5 | lỗi | `I-COMP` |
| 6 | ở | `I-COMP` |
| 7 | cổ | `I-COMP` |
| 8 | áo | `I-COMP` |
| 9 | không | `I-COMP` |
| 10 | được | `I-COMP` |
| 11 | không | `I-COMP` |
| 12 | lắm | `I-COMP` |
| 13 | nhưng | `I-COMP` |
| 14 | còn | `I-COMP` |
| 15 | lại | `I-COMP` |
| 16 | bộ | `I-COMP` |
| 17 | này | `I-COMP` |
| 18 | cũng | `I-COMP` |
| 19 | đẹp | `I-COMP` |
| 20 | (•‿•)(✷‿✷) | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (21 tokens >= 15)
- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 100. `train_002536`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> vận chuyển chậm hàng đã bị kích hoạt bảo hành trước

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | vận | `O` |
| 1 | chuyển | `O` |
| 2 | chậm | `O` |
| 3 | hàng | `O` |
| 4 | đã | `O` |
| 5 | bị | `O` |
| 6 | kích | `O` |
| 7 | hoạt | `O` |
| 8 | bảo | `O` |
| 9 | hành | `O` |
| 10 | trước | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 101. `train_001688`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

>  cửa hàng  đăng hình là quần ống rộng và lai cuốn mà lại gửi cho mình quần 9 tất ống ôm nhẹ . quần thì đẹp nhưng mình không thích quần 9 tất tí nào cả , mặc cũng không được thoải mái ngồi xuống rất chật , đùi mình hơi to nên thích ống rộng cho thoải mái . quần không được ưng ý nhưng mặc đi làm ai cũng khen đẹp nên mình đánh giá lại cho  cửa hàng   5star  . lần sau lại ủng hộ

**Spans:**

- #0 [113:150] `mình không thích quần 9 tất tí nào cả` label=`COMP`
- #1 [153:202] `mặc cũng không được thoải mái ngồi xuống rất chật` label=`COMP`
- #2 [256:355] `quần không được ưng ý nhưng mặc đi làm ai cũng khen đẹp nên mình đánh giá lại cho  cửa hàng   5star` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | cửa | `O` |
| 1 | hàng | `O` |
| 2 | đăng | `O` |
| 3 | hình | `O` |
| 4 | là | `O` |
| 5 | quần | `O` |
| 6 | ống | `O` |
| 7 | rộng | `O` |
| 8 | và | `O` |
| 9 | lai | `O` |
| 10 | cuốn | `O` |
| 11 | mà | `O` |
| 12 | lại | `O` |
| 13 | gửi | `O` |
| 14 | cho | `O` |
| 15 | mình | `O` |
| 16 | quần | `O` |
| 17 | 9 | `O` |
| 18 | tất | `O` |
| 19 | ống | `O` |
| 20 | ôm | `O` |
| 21 | nhẹ | `O` |
| 22 | . | `O` |
| 23 | quần | `O` |
| 24 | thì | `O` |
| 25 | đẹp | `O` |
| 26 | nhưng | `O` |
| 27 | mình | `B-COMP` |
| 28 | không | `I-COMP` |
| 29 | thích | `I-COMP` |
| 30 | quần | `I-COMP` |
| 31 | 9 | `I-COMP` |
| 32 | tất | `I-COMP` |
| 33 | tí | `I-COMP` |
| 34 | nào | `I-COMP` |
| 35 | cả | `I-COMP` |
| 36 | , | `O` |
| 37 | mặc | `B-COMP` |
| 38 | cũng | `I-COMP` |
| 39 | không | `I-COMP` |
| 40 | được | `I-COMP` |
| 41 | thoải | `I-COMP` |
| 42 | mái | `I-COMP` |
| 43 | ngồi | `I-COMP` |
| 44 | xuống | `I-COMP` |
| 45 | rất | `I-COMP` |
| 46 | chật | `I-COMP` |
| 47 | , | `O` |
| 48 | đùi | `O` |
| 49 | mình | `O` |
| 50 | hơi | `O` |
| 51 | to | `O` |
| 52 | nên | `O` |
| 53 | thích | `O` |
| 54 | ống | `O` |
| 55 | rộng | `O` |
| 56 | cho | `O` |
| 57 | thoải | `O` |
| 58 | mái | `O` |
| 59 | . | `O` |
| 60 | quần | `B-COMP` |
| 61 | không | `I-COMP` |
| 62 | được | `I-COMP` |
| 63 | ưng | `I-COMP` |
| 64 | ý | `I-COMP` |
| 65 | nhưng | `I-COMP` |
| 66 | mặc | `I-COMP` |
| 67 | đi | `I-COMP` |
| 68 | làm | `I-COMP` |
| 69 | ai | `I-COMP` |
| 70 | cũng | `I-COMP` |
| 71 | khen | `I-COMP` |
| 72 | đẹp | `I-COMP` |
| 73 | nên | `I-COMP` |
| 74 | mình | `I-COMP` |
| 75 | đánh | `I-COMP` |
| 76 | giá | `I-COMP` |
| 77 | lại | `I-COMP` |
| 78 | cho | `I-COMP` |
| 79 | cửa | `I-COMP` |
| 80 | hàng | `I-COMP` |
| 81 | 5star | `I-COMP` |
| 82 | . | `O` |
| 83 | lần | `O` |
| 84 | sau | `O` |
| 85 | lại | `O` |
| 86 | ủng | `O` |
| 87 | hộ | `O` |

**Heuristic warnings:**

- span #2 quá dài (22 tokens >= 15)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 102. `train_000809`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> quần quá mỏng , mặc vào chả biết bị rách lúc nào

**Spans:**

- #0 [0:13] `quần quá mỏng` label=`COMP`
- #1 [16:48] `mặc vào chả biết bị rách lúc nào` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | quần | `B-COMP` |
| 1 | quá | `I-COMP` |
| 2 | mỏng | `I-COMP` |
| 3 | , | `O` |
| 4 | mặc | `B-COMP` |
| 5 | vào | `I-COMP` |
| 6 | chả | `I-COMP` |
| 7 | biết | `I-COMP` |
| 8 | bị | `I-COMP` |
| 9 | rách | `I-COMP` |
| 10 | lúc | `I-COMP` |
| 11 | nào | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (91.7%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 103. `train_001368`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> kem thì được nhưng quà tặng thì đã hết hạn sử dụng ... tặng thì nên tặng có tâm xíu còn không tặng cũng không sao chứ không nên tặng kèm chỉ để cho có thôi ạ

**Spans:**

- #0 [88:157] `không tặng cũng không sao chứ không nên tặng kèm chỉ để cho có thôi ạ` label=`COMP`

**Reason:** Cụm 'không tặng cũng không sao chứ không nên tặng kèm chỉ để cho có thôi ạ' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | kem | `O` |
| 1 | thì | `O` |
| 2 | được | `O` |
| 3 | nhưng | `O` |
| 4 | quà | `O` |
| 5 | tặng | `O` |
| 6 | thì | `O` |
| 7 | đã | `O` |
| 8 | hết | `O` |
| 9 | hạn | `O` |
| 10 | sử | `O` |
| 11 | dụng | `O` |
| 12 | ... | `O` |
| 13 | tặng | `O` |
| 14 | thì | `O` |
| 15 | nên | `O` |
| 16 | tặng | `O` |
| 17 | có | `O` |
| 18 | tâm | `O` |
| 19 | xíu | `O` |
| 20 | còn | `O` |
| 21 | không | `B-COMP` |
| 22 | tặng | `I-COMP` |
| 23 | cũng | `I-COMP` |
| 24 | không | `I-COMP` |
| 25 | sao | `I-COMP` |
| 26 | chứ | `I-COMP` |
| 27 | không | `I-COMP` |
| 28 | nên | `I-COMP` |
| 29 | tặng | `I-COMP` |
| 30 | kèm | `I-COMP` |
| 31 | chỉ | `I-COMP` |
| 32 | để | `I-COMP` |
| 33 | cho | `I-COMP` |
| 34 | có | `I-COMP` |
| 35 | thôi | `I-COMP` |
| 36 | ạ | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (16 tokens >= 15)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 104. `train_002396`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> thiết kế đơn giản nhưng rất chắc chắn nhưng có một điểm trừ đối với cá nhân mình là phần thân son được phủ như tráng gương khi cầm vào hay môi chạm vào sẽ để lại vân môi hoặc vân tay. về chất son khi lên môi thì khá mịn mượt khi bặm môi thì tạo cảm giác hơi dính dính nhưng không hề làm nặng môi. màu hồng hơi hướng đỏ đất nên khi không trang điểm mà chỉ son thôi thì vẫn xinh chứ không dừ ( mình nghĩ nên tẩy da chết cho môi rồi thêm một lớp son dưỡng mỏng thôi rồi son em này lên là được  ). vì bản chất em này cũng là son có thành phần dưỡng rồi nên mình nghĩ không thể rất với các dòng khác về mặt lâu trôi được nhưng mình đã sử dụng qua và không dặm lại nhưng đến cuối ngày vẫn thấy còn lại trên môi màu hồng phớt. ai ít trang điểm chỉ thích đánh một ít son khi ra ngoài thì cân nhắc em này nha ! tổng quan mình cho  5star , giao hàng cũng nhanh nữa nên rất hài lòng 😊

**Spans:**

- #0 [0:182] `thiết kế đơn giản nhưng rất chắc chắn nhưng có một điểm trừ đối với cá nhân mình là phần thân son được phủ như tráng gương khi cầm vào hay môi chạm vào sẽ để lại vân môi hoặc vân tay` label=`COMP`
- #1 [274:295] `không hề làm nặng môi` label=`COMP`
- #2 [351:492] `chỉ son thôi thì vẫn xinh chứ không dừ ( mình nghĩ nên tẩy da chết cho môi rồi thêm một lớp son dưỡng mỏng thôi rồi son em này lên là được  )` label=`COMP`
- #3 [494:718] `vì bản chất em này cũng là son có thành phần dưỡng rồi nên mình nghĩ không thể rất với các dòng khác về mặt lâu trôi được nhưng mình đã sử dụng qua và không dặm lại nhưng đến cuối ngày vẫn thấy còn lại trên môi màu hồng phớt` label=`COMP`
- #4 [830:873] `giao hàng cũng nhanh nữa nên rất hài lòng 😊` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | thiết | `B-COMP` |
| 1 | kế | `I-COMP` |
| 2 | đơn | `I-COMP` |
| 3 | giản | `I-COMP` |
| 4 | nhưng | `I-COMP` |
| 5 | rất | `I-COMP` |
| 6 | chắc | `I-COMP` |
| 7 | chắn | `I-COMP` |
| 8 | nhưng | `I-COMP` |
| 9 | có | `I-COMP` |
| 10 | một | `I-COMP` |
| 11 | điểm | `I-COMP` |
| 12 | trừ | `I-COMP` |
| 13 | đối | `I-COMP` |
| 14 | với | `I-COMP` |
| 15 | cá | `I-COMP` |
| 16 | nhân | `I-COMP` |
| 17 | mình | `I-COMP` |
| 18 | là | `I-COMP` |
| 19 | phần | `I-COMP` |
| 20 | thân | `I-COMP` |
| 21 | son | `I-COMP` |
| 22 | được | `I-COMP` |
| 23 | phủ | `I-COMP` |
| 24 | như | `I-COMP` |
| 25 | tráng | `I-COMP` |
| 26 | gương | `I-COMP` |
| 27 | khi | `I-COMP` |
| 28 | cầm | `I-COMP` |
| 29 | vào | `I-COMP` |
| 30 | hay | `I-COMP` |
| 31 | môi | `I-COMP` |
| 32 | chạm | `I-COMP` |
| 33 | vào | `I-COMP` |
| 34 | sẽ | `I-COMP` |
| 35 | để | `I-COMP` |
| 36 | lại | `I-COMP` |
| 37 | vân | `I-COMP` |
| 38 | môi | `I-COMP` |
| 39 | hoặc | `I-COMP` |
| 40 | vân | `I-COMP` |
| 41 | tay. | `I-COMP` |
| 42 | về | `O` |
| 43 | chất | `O` |
| 44 | son | `O` |
| 45 | khi | `O` |
| 46 | lên | `O` |
| 47 | môi | `O` |
| 48 | thì | `O` |
| 49 | khá | `O` |
| 50 | mịn | `O` |
| 51 | mượt | `O` |
| 52 | khi | `O` |
| 53 | bặm | `O` |
| 54 | môi | `O` |
| 55 | thì | `O` |
| 56 | tạo | `O` |
| 57 | cảm | `O` |
| 58 | giác | `O` |
| 59 | hơi | `O` |
| 60 | dính | `O` |
| 61 | dính | `O` |
| 62 | nhưng | `O` |
| 63 | không | `B-COMP` |
| 64 | hề | `I-COMP` |
| 65 | làm | `I-COMP` |
| 66 | nặng | `I-COMP` |
| 67 | môi. | `I-COMP` |
| 68 | màu | `O` |
| 69 | hồng | `O` |
| 70 | hơi | `O` |
| 71 | hướng | `O` |
| 72 | đỏ | `O` |
| 73 | đất | `O` |
| 74 | nên | `O` |
| 75 | khi | `O` |
| 76 | không | `O` |
| 77 | trang | `O` |
| 78 | điểm | `O` |
| 79 | mà | `O` |
| 80 | chỉ | `B-COMP` |
| 81 | son | `I-COMP` |
| 82 | thôi | `I-COMP` |
| 83 | thì | `I-COMP` |
| 84 | vẫn | `I-COMP` |
| 85 | xinh | `I-COMP` |
| 86 | chứ | `I-COMP` |
| 87 | không | `I-COMP` |
| 88 | dừ | `I-COMP` |
| 89 | ( | `I-COMP` |
| 90 | mình | `I-COMP` |
| 91 | nghĩ | `I-COMP` |
| 92 | nên | `I-COMP` |
| 93 | tẩy | `I-COMP` |
| 94 | da | `I-COMP` |
| 95 | chết | `I-COMP` |
| 96 | cho | `I-COMP` |
| 97 | môi | `I-COMP` |
| 98 | rồi | `I-COMP` |
| 99 | thêm | `I-COMP` |
| 100 | một | `I-COMP` |
| 101 | lớp | `I-COMP` |
| 102 | son | `I-COMP` |
| 103 | dưỡng | `I-COMP` |
| 104 | mỏng | `I-COMP` |
| 105 | thôi | `I-COMP` |
| 106 | rồi | `I-COMP` |
| 107 | son | `I-COMP` |
| 108 | em | `I-COMP` |
| 109 | này | `I-COMP` |
| 110 | lên | `I-COMP` |
| 111 | là | `I-COMP` |
| 112 | được | `I-COMP` |
| 113 | ). | `I-COMP` |
| 114 | vì | `B-COMP` |
| 115 | bản | `I-COMP` |
| 116 | chất | `I-COMP` |
| 117 | em | `I-COMP` |
| 118 | này | `I-COMP` |
| 119 | cũng | `I-COMP` |
| 120 | là | `I-COMP` |
| 121 | son | `I-COMP` |
| 122 | có | `I-COMP` |
| 123 | thành | `I-COMP` |
| 124 | phần | `I-COMP` |
| 125 | dưỡng | `I-COMP` |
| 126 | rồi | `I-COMP` |
| 127 | nên | `I-COMP` |
| 128 | mình | `I-COMP` |
| 129 | nghĩ | `I-COMP` |
| 130 | không | `I-COMP` |
| 131 | thể | `I-COMP` |
| 132 | rất | `I-COMP` |
| 133 | với | `I-COMP` |
| 134 | các | `I-COMP` |
| 135 | dòng | `I-COMP` |
| 136 | khác | `I-COMP` |
| 137 | về | `I-COMP` |
| 138 | mặt | `I-COMP` |
| 139 | lâu | `I-COMP` |
| 140 | trôi | `I-COMP` |
| 141 | được | `I-COMP` |
| 142 | nhưng | `I-COMP` |
| 143 | mình | `I-COMP` |
| 144 | đã | `I-COMP` |
| 145 | sử | `I-COMP` |
| 146 | dụng | `I-COMP` |
| 147 | qua | `I-COMP` |
| 148 | và | `I-COMP` |
| 149 | không | `I-COMP` |
| 150 | dặm | `I-COMP` |
| 151 | lại | `I-COMP` |
| 152 | nhưng | `I-COMP` |
| 153 | đến | `I-COMP` |
| 154 | cuối | `I-COMP` |
| 155 | ngày | `I-COMP` |
| 156 | vẫn | `I-COMP` |
| 157 | thấy | `I-COMP` |
| 158 | còn | `I-COMP` |
| 159 | lại | `I-COMP` |
| 160 | trên | `I-COMP` |
| 161 | môi | `I-COMP` |
| 162 | màu | `I-COMP` |
| 163 | hồng | `I-COMP` |
| 164 | phớt. | `I-COMP` |
| 165 | ai | `O` |
| 166 | ít | `O` |
| 167 | trang | `O` |
| 168 | điểm | `O` |
| 169 | chỉ | `O` |
| 170 | thích | `O` |
| 171 | đánh | `O` |
| 172 | một | `O` |
| 173 | ít | `O` |
| 174 | son | `O` |
| 175 | khi | `O` |
| 176 | ra | `O` |
| 177 | ngoài | `O` |
| 178 | thì | `O` |
| 179 | cân | `O` |
| 180 | nhắc | `O` |
| 181 | em | `O` |
| 182 | này | `O` |
| 183 | nha | `O` |
| 184 | ! | `O` |
| 185 | tổng | `O` |
| 186 | quan | `O` |
| 187 | mình | `O` |
| 188 | cho | `O` |
| 189 | 5star | `O` |
| 190 | , | `O` |
| 191 | giao | `B-COMP` |
| 192 | hàng | `I-COMP` |
| 193 | cũng | `I-COMP` |
| 194 | nhanh | `I-COMP` |
| 195 | nữa | `I-COMP` |
| 196 | nên | `I-COMP` |
| 197 | rất | `I-COMP` |
| 198 | hài | `I-COMP` |
| 199 | lòng | `I-COMP` |
| 200 | 😊 | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (42 tokens >= 15)
- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- span #2 quá dài (34 tokens >= 15)
- span #3 quá dài (51 tokens >= 15)
- record có nhiều hơn 4 spans (5 spans)
- tỉ lệ COMP token > 60% (70.6%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 105. `train_001423`

- Domain: `app`
- Split: `train`

**Text gốc:**

> bài hát thì càng ngày càng ít và hạn chế đặc biệt là những ca khúc tiếng anh cùng theo đó thì lại bắt người tiêu dùng xem nhiều  quả người cáo trong một lần nghe những ca khúc tiếng anh  được  nghe . ứng dụng càng ngày càng tệ hại chỉ vì cái mà anh duy mạnh gọi là kiếm lợi nhuận càng nhiều càng tốt bất chấp ngườ... bài đánh giá đầy đủ

**Spans:**

- #0 [0:197] `bài hát thì càng ngày càng ít và hạn chế đặc biệt là những ca khúc tiếng anh cùng theo đó thì lại bắt người tiêu dùng xem nhiều  quả người cáo trong một lần nghe những ca khúc tiếng anh  được  nghe` label=`COMP`
- #1 [200:313] `ứng dụng càng ngày càng tệ hại chỉ vì cái mà anh duy mạnh gọi là kiếm lợi nhuận càng nhiều càng tốt bất chấp ngườ` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | bài | `B-COMP` |
| 1 | hát | `I-COMP` |
| 2 | thì | `I-COMP` |
| 3 | càng | `I-COMP` |
| 4 | ngày | `I-COMP` |
| 5 | càng | `I-COMP` |
| 6 | ít | `I-COMP` |
| 7 | và | `I-COMP` |
| 8 | hạn | `I-COMP` |
| 9 | chế | `I-COMP` |
| 10 | đặc | `I-COMP` |
| 11 | biệt | `I-COMP` |
| 12 | là | `I-COMP` |
| 13 | những | `I-COMP` |
| 14 | ca | `I-COMP` |
| 15 | khúc | `I-COMP` |
| 16 | tiếng | `I-COMP` |
| 17 | anh | `I-COMP` |
| 18 | cùng | `I-COMP` |
| 19 | theo | `I-COMP` |
| 20 | đó | `I-COMP` |
| 21 | thì | `I-COMP` |
| 22 | lại | `I-COMP` |
| 23 | bắt | `I-COMP` |
| 24 | người | `I-COMP` |
| 25 | tiêu | `I-COMP` |
| 26 | dùng | `I-COMP` |
| 27 | xem | `I-COMP` |
| 28 | nhiều | `I-COMP` |
| 29 | quả | `I-COMP` |
| 30 | người | `I-COMP` |
| 31 | cáo | `I-COMP` |
| 32 | trong | `I-COMP` |
| 33 | một | `I-COMP` |
| 34 | lần | `I-COMP` |
| 35 | nghe | `I-COMP` |
| 36 | những | `I-COMP` |
| 37 | ca | `I-COMP` |
| 38 | khúc | `I-COMP` |
| 39 | tiếng | `I-COMP` |
| 40 | anh | `I-COMP` |
| 41 | được | `I-COMP` |
| 42 | nghe | `I-COMP` |
| 43 | . | `O` |
| 44 | ứng | `B-COMP` |
| 45 | dụng | `I-COMP` |
| 46 | càng | `I-COMP` |
| 47 | ngày | `I-COMP` |
| 48 | càng | `I-COMP` |
| 49 | tệ | `I-COMP` |
| 50 | hại | `I-COMP` |
| 51 | chỉ | `I-COMP` |
| 52 | vì | `I-COMP` |
| 53 | cái | `I-COMP` |
| 54 | mà | `I-COMP` |
| 55 | anh | `I-COMP` |
| 56 | duy | `I-COMP` |
| 57 | mạnh | `I-COMP` |
| 58 | gọi | `I-COMP` |
| 59 | là | `I-COMP` |
| 60 | kiếm | `I-COMP` |
| 61 | lợi | `I-COMP` |
| 62 | nhuận | `I-COMP` |
| 63 | càng | `I-COMP` |
| 64 | nhiều | `I-COMP` |
| 65 | càng | `I-COMP` |
| 66 | tốt | `I-COMP` |
| 67 | bất | `I-COMP` |
| 68 | chấp | `I-COMP` |
| 69 | ngườ... | `I-COMP` |
| 70 | bài | `O` |
| 71 | đánh | `O` |
| 72 | giá | `O` |
| 73 | đầy | `O` |
| 74 | đủ | `O` |

**Heuristic warnings:**

- span #0 quá dài (43 tokens >= 15)
- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- span #1 quá dài (26 tokens >= 15)
- tỉ lệ COMP token > 60% (92.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 106. `train_001430`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> đặt màu 125 mà lại giao màu 230

**Spans:**

- #0 [0:31] `đặt màu 125 mà lại giao màu 230` label=`COMP`

**Reason:** Cụm 'đặt màu 125 mà lại giao màu 230' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đặt | `B-COMP` |
| 1 | màu | `I-COMP` |
| 2 | 125 | `I-COMP` |
| 3 | mà | `I-COMP` |
| 4 | lại | `I-COMP` |
| 5 | giao | `I-COMP` |
| 6 | màu | `I-COMP` |
| 7 | 230 | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 107. `train_003642`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> săn  được  giá quá được cho chiếc điện thoại đẹp. mong lazada kích hoạt bảo hành điện tử giúp mình. sử dụng  được  vài hôm rồi vẫn chưa thấy bảo hành điện tử.

**Spans:**

- None

**Reason:** Không có khiếu nại rõ ràng; đây chủ yếu là góp ý, mong muốn hoặc đề xuất.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | săn | `O` |
| 1 | được | `O` |
| 2 | giá | `O` |
| 3 | quá | `O` |
| 4 | được | `O` |
| 5 | cho | `O` |
| 6 | chiếc | `O` |
| 7 | điện | `O` |
| 8 | thoại | `O` |
| 9 | đẹp. | `O` |
| 10 | mong | `O` |
| 11 | lazada | `O` |
| 12 | kích | `O` |
| 13 | hoạt | `O` |
| 14 | bảo | `O` |
| 15 | hành | `O` |
| 16 | điện | `O` |
| 17 | tử | `O` |
| 18 | giúp | `O` |
| 19 | mình. | `O` |
| 20 | sử | `O` |
| 21 | dụng | `O` |
| 22 | được | `O` |
| 23 | vài | `O` |
| 24 | hôm | `O` |
| 25 | rồi | `O` |
| 26 | vẫn | `O` |
| 27 | chưa | `O` |
| 28 | thấy | `O` |
| 29 | bảo | `O` |
| 30 | hành | `O` |
| 31 | điện | `O` |
| 32 | tử. | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 108. `train_003017`

- Domain: `app`
- Split: `train`

**Text gốc:**

> thấy vui vui, nhưng  quả người cáo quá nhiều, các bạn muốn không có  quả người cáo tắt wi-fi hoặc 4g đi

**Spans:**

- #0 [46:103] `các bạn muốn không có  quả người cáo tắt wi-fi hoặc 4g đi` label=`COMP`

**Reason:** Cụm 'các bạn muốn không có  quả người cáo tắt wi-fi hoặc 4g đi' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | thấy | `O` |
| 1 | vui | `O` |
| 2 | vui, | `O` |
| 3 | nhưng | `O` |
| 4 | quả | `O` |
| 5 | người | `O` |
| 6 | cáo | `O` |
| 7 | quá | `O` |
| 8 | nhiều, | `O` |
| 9 | các | `B-COMP` |
| 10 | bạn | `I-COMP` |
| 11 | muốn | `I-COMP` |
| 12 | không | `I-COMP` |
| 13 | có | `I-COMP` |
| 14 | quả | `I-COMP` |
| 15 | người | `I-COMP` |
| 16 | cáo | `I-COMP` |
| 17 | tắt | `I-COMP` |
| 18 | wi-fi | `I-COMP` |
| 19 | hoặc | `I-COMP` |
| 20 | 4g | `I-COMP` |
| 21 | đi | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 109. `train_001194`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> cho trước 3star  vì lần đầu sử dụng. xài  được  vài ngày, aPly lên da thấy có sáng lên, lỗ chân lông có cải thiện nhẹ, nhưng cũng đi đôi với mụn. để tiếp tục theo dõi xem mụn do sản phẩm hay do nội tiết

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | cho | `O` |
| 1 | trước | `O` |
| 2 | 3star | `O` |
| 3 | vì | `O` |
| 4 | lần | `O` |
| 5 | đầu | `O` |
| 6 | sử | `O` |
| 7 | dụng. | `O` |
| 8 | xài | `O` |
| 9 | được | `O` |
| 10 | vài | `O` |
| 11 | ngày, | `O` |
| 12 | aPly | `O` |
| 13 | lên | `O` |
| 14 | da | `O` |
| 15 | thấy | `O` |
| 16 | có | `O` |
| 17 | sáng | `O` |
| 18 | lên, | `O` |
| 19 | lỗ | `O` |
| 20 | chân | `O` |
| 21 | lông | `O` |
| 22 | có | `O` |
| 23 | cải | `O` |
| 24 | thiện | `O` |
| 25 | nhẹ, | `O` |
| 26 | nhưng | `O` |
| 27 | cũng | `O` |
| 28 | đi | `O` |
| 29 | đôi | `O` |
| 30 | với | `O` |
| 31 | mụn. | `O` |
| 32 | để | `O` |
| 33 | tiếp | `O` |
| 34 | tục | `O` |
| 35 | theo | `O` |
| 36 | dõi | `O` |
| 37 | xem | `O` |
| 38 | mụn | `O` |
| 39 | do | `O` |
| 40 | sản | `O` |
| 41 | phẩm | `O` |
| 42 | hay | `O` |
| 43 | do | `O` |
| 44 | nội | `O` |
| 45 | tiết | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 110. `train_001072`

- Domain: `app`
- Split: `train`

**Text gốc:**

> bạn nên cho thêm những bài hát kpop vì giới trẻ tuổi tEn hiện nay họ rất cô chuộng những dòng nhạc đó ví dụ như những nhóm nhạc twice  bình thường sao black pink exo mamamO những nhóm nhạc này thường được nhiều bạn tuổi tEn ưa chuộng vậy nên tôi nghĩ nên cho thêm những bài hát của những nhóm nhạc này sẽ khiến... bài đánh giá đầy đủ

**Spans:**

- None

**Reason:** Không có khiếu nại rõ ràng; đây chủ yếu là góp ý, mong muốn hoặc đề xuất.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | bạn | `O` |
| 1 | nên | `O` |
| 2 | cho | `O` |
| 3 | thêm | `O` |
| 4 | những | `O` |
| 5 | bài | `O` |
| 6 | hát | `O` |
| 7 | kpop | `O` |
| 8 | vì | `O` |
| 9 | giới | `O` |
| 10 | trẻ | `O` |
| 11 | tuổi | `O` |
| 12 | tEn | `O` |
| 13 | hiện | `O` |
| 14 | nay | `O` |
| 15 | họ | `O` |
| 16 | rất | `O` |
| 17 | cô | `O` |
| 18 | chuộng | `O` |
| 19 | những | `O` |
| 20 | dòng | `O` |
| 21 | nhạc | `O` |
| 22 | đó | `O` |
| 23 | ví | `O` |
| 24 | dụ | `O` |
| 25 | như | `O` |
| 26 | những | `O` |
| 27 | nhóm | `O` |
| 28 | nhạc | `O` |
| 29 | twice | `O` |
| 30 | bình | `O` |
| 31 | thường | `O` |
| 32 | sao | `O` |
| 33 | black | `O` |
| 34 | pink | `O` |
| 35 | exo | `O` |
| 36 | mamamO | `O` |
| 37 | những | `O` |
| 38 | nhóm | `O` |
| 39 | nhạc | `O` |
| 40 | này | `O` |
| 41 | thường | `O` |
| 42 | được | `O` |
| 43 | nhiều | `O` |
| 44 | bạn | `O` |
| 45 | tuổi | `O` |
| 46 | tEn | `O` |
| 47 | ưa | `O` |
| 48 | chuộng | `O` |
| 49 | vậy | `O` |
| 50 | nên | `O` |
| 51 | tôi | `O` |
| 52 | nghĩ | `O` |
| 53 | nên | `O` |
| 54 | cho | `O` |
| 55 | thêm | `O` |
| 56 | những | `O` |
| 57 | bài | `O` |
| 58 | hát | `O` |
| 59 | của | `O` |
| 60 | những | `O` |
| 61 | nhóm | `O` |
| 62 | nhạc | `O` |
| 63 | này | `O` |
| 64 | sẽ | `O` |
| 65 | khiến... | `O` |
| 66 | bài | `O` |
| 67 | đánh | `O` |
| 68 | giá | `O` |
| 69 | đầy | `O` |
| 70 | đủ | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 111. `train_000743`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> sop giao đồ lâu , nhưng sản phẩm phù hợp với giá tiền ,giao đúng màu .ok

**Spans:**

- #0 [0:15] `sop giao đồ lâu` label=`COMP`
- #1 [55:68] `giao đúng màu` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | sop | `B-COMP` |
| 1 | giao | `I-COMP` |
| 2 | đồ | `I-COMP` |
| 3 | lâu | `I-COMP` |
| 4 | , | `O` |
| 5 | nhưng | `O` |
| 6 | sản | `O` |
| 7 | phẩm | `O` |
| 8 | phù | `O` |
| 9 | hợp | `O` |
| 10 | với | `O` |
| 11 | giá | `O` |
| 12 | tiền | `O` |
| 13 | ,giao | `B-COMP` |
| 14 | đúng | `I-COMP` |
| 15 | màu | `I-COMP` |
| 16 | .ok | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 112. `train_002531`

- Domain: `app`
- Split: `train`

**Text gốc:**

> mất một tháng để người chơi mới như tôi có thể đạt được 1m5 sức mạnh, và với một cuộc xâm lược của kẻ 30m sức mạnh, tôi mất tất cả.... tôi từng yêu game này, đến mức dùng rất nhiều thời gian và giờ đây tôi chẳng còn gì. tạm biệt, tôi từ bỏ cái trò chơi khốn nạn này.

**Spans:**

- #0 [0:68] `mất một tháng để người chơi mới như tôi có thể đạt được 1m5 sức mạnh` label=`COMP`
- #1 [116:130] `tôi mất tất cả` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mất | `B-COMP` |
| 1 | một | `I-COMP` |
| 2 | tháng | `I-COMP` |
| 3 | để | `I-COMP` |
| 4 | người | `I-COMP` |
| 5 | chơi | `I-COMP` |
| 6 | mới | `I-COMP` |
| 7 | như | `I-COMP` |
| 8 | tôi | `I-COMP` |
| 9 | có | `I-COMP` |
| 10 | thể | `I-COMP` |
| 11 | đạt | `I-COMP` |
| 12 | được | `I-COMP` |
| 13 | 1m5 | `I-COMP` |
| 14 | sức | `I-COMP` |
| 15 | mạnh, | `I-COMP` |
| 16 | và | `O` |
| 17 | với | `O` |
| 18 | một | `O` |
| 19 | cuộc | `O` |
| 20 | xâm | `O` |
| 21 | lược | `O` |
| 22 | của | `O` |
| 23 | kẻ | `O` |
| 24 | 30m | `O` |
| 25 | sức | `O` |
| 26 | mạnh, | `O` |
| 27 | tôi | `B-COMP` |
| 28 | mất | `I-COMP` |
| 29 | tất | `I-COMP` |
| 30 | cả.... | `I-COMP` |
| 31 | tôi | `O` |
| 32 | từng | `O` |
| 33 | yêu | `O` |
| 34 | game | `O` |
| 35 | này, | `O` |
| 36 | đến | `O` |
| 37 | mức | `O` |
| 38 | dùng | `O` |
| 39 | rất | `O` |
| 40 | nhiều | `O` |
| 41 | thời | `O` |
| 42 | gian | `O` |
| 43 | và | `O` |
| 44 | giờ | `O` |
| 45 | đây | `O` |
| 46 | tôi | `O` |
| 47 | chẳng | `O` |
| 48 | còn | `O` |
| 49 | gì. | `O` |
| 50 | tạm | `O` |
| 51 | biệt, | `O` |
| 52 | tôi | `O` |
| 53 | từ | `O` |
| 54 | bỏ | `O` |
| 55 | cái | `O` |
| 56 | trò | `O` |
| 57 | chơi | `O` |
| 58 | khốn | `O` |
| 59 | nạn | `O` |
| 60 | này. | `O` |

**Heuristic warnings:**

- span #0 quá dài (16 tokens >= 15)
- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 113. `train_000129`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> dùng 3 hôm mới thấy viền 2 bên không cảm ứng  được  . bấn 10 lần mới  được  một lần

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | dùng | `O` |
| 1 | 3 | `O` |
| 2 | hôm | `O` |
| 3 | mới | `O` |
| 4 | thấy | `O` |
| 5 | viền | `O` |
| 6 | 2 | `O` |
| 7 | bên | `O` |
| 8 | không | `O` |
| 9 | cảm | `O` |
| 10 | ứng | `O` |
| 11 | được | `O` |
| 12 | . | `O` |
| 13 | bấn | `O` |
| 14 | 10 | `O` |
| 15 | lần | `O` |
| 16 | mới | `O` |
| 17 | được | `O` |
| 18 | một | `O` |
| 19 | lần | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 114. `train_003295`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> hàng rất được nha :3 . có điều shiPer hơi khó chịu 😅

**Spans:**

- #0 [31:52] `shiPer hơi khó chịu 😅` label=`COMP`

**Reason:** Cụm 'shiPer hơi khó chịu 😅' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hàng | `O` |
| 1 | rất | `O` |
| 2 | được | `O` |
| 3 | nha | `O` |
| 4 | :3 | `O` |
| 5 | . | `O` |
| 6 | có | `O` |
| 7 | điều | `O` |
| 8 | shiPer | `B-COMP` |
| 9 | hơi | `I-COMP` |
| 10 | khó | `I-COMP` |
| 11 | chịu | `I-COMP` |
| 12 | 😅 | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 115. `train_002780`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> bôi thấy nóng không thấy tác dụng

**Spans:**

- #0 [0:33] `bôi thấy nóng không thấy tác dụng` label=`COMP`

**Reason:** Cụm 'bôi thấy nóng không thấy tác dụng' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | bôi | `B-COMP` |
| 1 | thấy | `I-COMP` |
| 2 | nóng | `I-COMP` |
| 3 | không | `I-COMP` |
| 4 | thấy | `I-COMP` |
| 5 | tác | `I-COMP` |
| 6 | dụng | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 116. `train_003912`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> hàng giả gội không hết gàu

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hàng | `O` |
| 1 | giả | `O` |
| 2 | gội | `O` |
| 3 | không | `O` |
| 4 | hết | `O` |
| 5 | gàu | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 117. `train_001517`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> chất liệu ok, dép hơi nhỏ nhưng không sao

**Spans:**

- #0 [14:41] `dép hơi nhỏ nhưng không sao` label=`COMP`

**Reason:** Cụm 'dép hơi nhỏ nhưng không sao' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | chất | `O` |
| 1 | liệu | `O` |
| 2 | ok, | `O` |
| 3 | dép | `B-COMP` |
| 4 | hơi | `I-COMP` |
| 5 | nhỏ | `I-COMP` |
| 6 | nhưng | `I-COMP` |
| 7 | không | `I-COMP` |
| 8 | sao | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (66.7%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 118. `train_000590`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> sản phẩm cũng đẹp  cửa hàng  chú ý lại mình đặt màu đen nhưng  cửa hàng  giao màu trắng ,

**Spans:**

- #0 [63:87] `cửa hàng  giao màu trắng` label=`COMP`

**Reason:** Cụm 'cửa hàng  giao màu trắng' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | sản | `O` |
| 1 | phẩm | `O` |
| 2 | cũng | `O` |
| 3 | đẹp | `O` |
| 4 | cửa | `O` |
| 5 | hàng | `O` |
| 6 | chú | `O` |
| 7 | ý | `O` |
| 8 | lại | `O` |
| 9 | mình | `O` |
| 10 | đặt | `O` |
| 11 | màu | `O` |
| 12 | đen | `O` |
| 13 | nhưng | `O` |
| 14 | cửa | `B-COMP` |
| 15 | hàng | `I-COMP` |
| 16 | giao | `I-COMP` |
| 17 | màu | `I-COMP` |
| 18 | trắng | `I-COMP` |
| 19 | , | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 119. `train_002437`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> tại sao trong điện thoại không có gì hết vậy

**Spans:**

- #0 [0:44] `tại sao trong điện thoại không có gì hết vậy` label=`COMP`

**Reason:** Cụm 'tại sao trong điện thoại không có gì hết vậy' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tại | `B-COMP` |
| 1 | sao | `I-COMP` |
| 2 | trong | `I-COMP` |
| 3 | điện | `I-COMP` |
| 4 | thoại | `I-COMP` |
| 5 | không | `I-COMP` |
| 6 | có | `I-COMP` |
| 7 | gì | `I-COMP` |
| 8 | hết | `I-COMP` |
| 9 | vậy | `I-COMP` |

**Heuristic warnings:**

- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 120. `train_001418`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> với mức giá này thì chiếc điện thoại này quá tuyệt. có điều tôi không thích chức năng camera lấy góc rộng của samsung, không thực lắm. nhưng mọi thứ thật sự rất tốt. hi vọng bạn kích hoạt bảo hành giúp mình. cảm ơn

**Spans:**

- #0 [60:117] `tôi không thích chức năng camera lấy góc rộng của samsung` label=`COMP`

**Reason:** Cụm 'tôi không thích chức năng camera lấy góc rộng của samsung' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | với | `O` |
| 1 | mức | `O` |
| 2 | giá | `O` |
| 3 | này | `O` |
| 4 | thì | `O` |
| 5 | chiếc | `O` |
| 6 | điện | `O` |
| 7 | thoại | `O` |
| 8 | này | `O` |
| 9 | quá | `O` |
| 10 | tuyệt. | `O` |
| 11 | có | `O` |
| 12 | điều | `O` |
| 13 | tôi | `B-COMP` |
| 14 | không | `I-COMP` |
| 15 | thích | `I-COMP` |
| 16 | chức | `I-COMP` |
| 17 | năng | `I-COMP` |
| 18 | camera | `I-COMP` |
| 19 | lấy | `I-COMP` |
| 20 | góc | `I-COMP` |
| 21 | rộng | `I-COMP` |
| 22 | của | `I-COMP` |
| 23 | samsung, | `I-COMP` |
| 24 | không | `O` |
| 25 | thực | `O` |
| 26 | lắm. | `O` |
| 27 | nhưng | `O` |
| 28 | mọi | `O` |
| 29 | thứ | `O` |
| 30 | thật | `O` |
| 31 | sự | `O` |
| 32 | rất | `O` |
| 33 | tốt. | `O` |
| 34 | hi | `O` |
| 35 | vọng | `O` |
| 36 | bạn | `O` |
| 37 | kích | `O` |
| 38 | hoạt | `O` |
| 39 | bảo | `O` |
| 40 | hành | `O` |
| 41 | giúp | `O` |
| 42 | mình. | `O` |
| 43 | cảm | `O` |
| 44 | ơn | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 121. `train_001228`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> máy mới như hình, độ bền chờ sử dụng mới biết, giao hàng hơi lâu, cả hơn một tuần,  cửa hàng  có đăng tặng thùng bia, nhưng không có, giờ hỏi lại bảo là chờ hệ thống quay trúng thưởng mới có, hic,( chắc mấy ngàn người thể nào cũng có người được) ?

**Spans:**

- #0 [47:64] `giao hàng hơi lâu` label=`COMP`
- #1 [124:132] `không có` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | máy | `O` |
| 1 | mới | `O` |
| 2 | như | `O` |
| 3 | hình, | `O` |
| 4 | độ | `O` |
| 5 | bền | `O` |
| 6 | chờ | `O` |
| 7 | sử | `O` |
| 8 | dụng | `O` |
| 9 | mới | `O` |
| 10 | biết, | `O` |
| 11 | giao | `B-COMP` |
| 12 | hàng | `I-COMP` |
| 13 | hơi | `I-COMP` |
| 14 | lâu, | `I-COMP` |
| 15 | cả | `O` |
| 16 | hơn | `O` |
| 17 | một | `O` |
| 18 | tuần, | `O` |
| 19 | cửa | `O` |
| 20 | hàng | `O` |
| 21 | có | `O` |
| 22 | đăng | `O` |
| 23 | tặng | `O` |
| 24 | thùng | `O` |
| 25 | bia, | `O` |
| 26 | nhưng | `O` |
| 27 | không | `B-COMP` |
| 28 | có, | `I-COMP` |
| 29 | giờ | `O` |
| 30 | hỏi | `O` |
| 31 | lại | `O` |
| 32 | bảo | `O` |
| 33 | là | `O` |
| 34 | chờ | `O` |
| 35 | hệ | `O` |
| 36 | thống | `O` |
| 37 | quay | `O` |
| 38 | trúng | `O` |
| 39 | thưởng | `O` |
| 40 | mới | `O` |
| 41 | có, | `O` |
| 42 | hic,( | `O` |
| 43 | chắc | `O` |
| 44 | mấy | `O` |
| 45 | ngàn | `O` |
| 46 | người | `O` |
| 47 | thể | `O` |
| 48 | nào | `O` |
| 49 | cũng | `O` |
| 50 | có | `O` |
| 51 | người | `O` |
| 52 | được) | `O` |
| 53 | ? | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 122. `train_000791`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> áo thì mặc vừa còn quần như cho con nít mặt làm ăn kì quá 👎👎👎

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | áo | `O` |
| 1 | thì | `O` |
| 2 | mặc | `O` |
| 3 | vừa | `O` |
| 4 | còn | `O` |
| 5 | quần | `O` |
| 6 | như | `O` |
| 7 | cho | `O` |
| 8 | con | `O` |
| 9 | nít | `O` |
| 10 | mặt | `O` |
| 11 | làm | `O` |
| 12 | ăn | `O` |
| 13 | kì | `O` |
| 14 | quá | `O` |
| 15 | 👎👎👎 | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 123. `train_002684`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> 48 mỹ phẩm không chuẩn như các hãng điện thoại khác , nhìn như khoảng 32 mỹ phẩm là cùng , được bổ sung thêm xài mạng 5g còn được hơn

**Spans:**

- #0 [0:51] `48 mỹ phẩm không chuẩn như các hãng điện thoại khác` label=`COMP`

**Reason:** Cụm '48 mỹ phẩm không chuẩn như các hãng điện thoại khác' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | 48 | `B-COMP` |
| 1 | mỹ | `I-COMP` |
| 2 | phẩm | `I-COMP` |
| 3 | không | `I-COMP` |
| 4 | chuẩn | `I-COMP` |
| 5 | như | `I-COMP` |
| 6 | các | `I-COMP` |
| 7 | hãng | `I-COMP` |
| 8 | điện | `I-COMP` |
| 9 | thoại | `I-COMP` |
| 10 | khác | `I-COMP` |
| 11 | , | `O` |
| 12 | nhìn | `O` |
| 13 | như | `O` |
| 14 | khoảng | `O` |
| 15 | 32 | `O` |
| 16 | mỹ | `O` |
| 17 | phẩm | `O` |
| 18 | là | `O` |
| 19 | cùng | `O` |
| 20 | , | `O` |
| 21 | được | `O` |
| 22 | bổ | `O` |
| 23 | sung | `O` |
| 24 | thêm | `O` |
| 25 | xài | `O` |
| 26 | mạng | `O` |
| 27 | 5g | `O` |
| 28 | còn | `O` |
| 29 | được | `O` |
| 30 | hơn | `O` |

**Heuristic warnings:**

- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 124. `train_004213`

- Domain: `app`
- Split: `train`

**Text gốc:**

> là một ứng dụng tốt, nên cài đặt, nhưng mà mong sẽ thay đổi một chức năng hơi bất tiện tiện. ẩn trò chuyện chỉ có thể áp dụng đối với bạn có sẵn trong danh bạ, còn người lạ bật ẩn trò chuyện lên rồi tìm lại thì không thấy đâu cả. có những người mình chưa kịp kết bạn, phải ẩn vì lí do riêng, sau kiếm... bài đánh giá đầy đủ

**Spans:**

- #0 [43:91] `mong sẽ thay đổi một chức năng hơi bất tiện tiện` label=`COMP`
- #1 [164:228] `người lạ bật ẩn trò chuyện lên rồi tìm lại thì không thấy đâu cả` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | là | `O` |
| 1 | một | `O` |
| 2 | ứng | `O` |
| 3 | dụng | `O` |
| 4 | tốt, | `O` |
| 5 | nên | `O` |
| 6 | cài | `O` |
| 7 | đặt, | `O` |
| 8 | nhưng | `O` |
| 9 | mà | `O` |
| 10 | mong | `B-COMP` |
| 11 | sẽ | `I-COMP` |
| 12 | thay | `I-COMP` |
| 13 | đổi | `I-COMP` |
| 14 | một | `I-COMP` |
| 15 | chức | `I-COMP` |
| 16 | năng | `I-COMP` |
| 17 | hơi | `I-COMP` |
| 18 | bất | `I-COMP` |
| 19 | tiện | `I-COMP` |
| 20 | tiện. | `I-COMP` |
| 21 | ẩn | `O` |
| 22 | trò | `O` |
| 23 | chuyện | `O` |
| 24 | chỉ | `O` |
| 25 | có | `O` |
| 26 | thể | `O` |
| 27 | áp | `O` |
| 28 | dụng | `O` |
| 29 | đối | `O` |
| 30 | với | `O` |
| 31 | bạn | `O` |
| 32 | có | `O` |
| 33 | sẵn | `O` |
| 34 | trong | `O` |
| 35 | danh | `O` |
| 36 | bạ, | `O` |
| 37 | còn | `O` |
| 38 | người | `B-COMP` |
| 39 | lạ | `I-COMP` |
| 40 | bật | `I-COMP` |
| 41 | ẩn | `I-COMP` |
| 42 | trò | `I-COMP` |
| 43 | chuyện | `I-COMP` |
| 44 | lên | `I-COMP` |
| 45 | rồi | `I-COMP` |
| 46 | tìm | `I-COMP` |
| 47 | lại | `I-COMP` |
| 48 | thì | `I-COMP` |
| 49 | không | `I-COMP` |
| 50 | thấy | `I-COMP` |
| 51 | đâu | `I-COMP` |
| 52 | cả. | `I-COMP` |
| 53 | có | `O` |
| 54 | những | `O` |
| 55 | người | `O` |
| 56 | mình | `O` |
| 57 | chưa | `O` |
| 58 | kịp | `O` |
| 59 | kết | `O` |
| 60 | bạn, | `O` |
| 61 | phải | `O` |
| 62 | ẩn | `O` |
| 63 | vì | `O` |
| 64 | lí | `O` |
| 65 | do | `O` |
| 66 | riêng, | `O` |
| 67 | sau | `O` |
| 68 | kiếm... | `O` |
| 69 | bài | `O` |
| 70 | đánh | `O` |
| 71 | giá | `O` |
| 72 | đầy | `O` |
| 73 | đủ | `O` |

**Heuristic warnings:**

- span #1 quá dài (15 tokens >= 15)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 125. `train_004147`

- Domain: `app`
- Split: `train`

**Text gốc:**

> làm game thì phải biết lắng nghe người chơi họ nói mà sửa lỗi, chứ mà im lặng chỉ biết lấy tiền người ta như vậy, thế thì còn gì là game nữa, tôi đã chơi game này từ hồi còn trên pc giờ tới mobil , cũng không tệ, nhưng mỗi cái, cũng phải sửa lại cho người chơi thổi mái hơn nhé

**Spans:**

- #0 [54:61] `sửa lỗi` label=`COMP`
- #1 [198:211] `cũng không tệ` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | làm | `O` |
| 1 | game | `O` |
| 2 | thì | `O` |
| 3 | phải | `O` |
| 4 | biết | `O` |
| 5 | lắng | `O` |
| 6 | nghe | `O` |
| 7 | người | `O` |
| 8 | chơi | `O` |
| 9 | họ | `O` |
| 10 | nói | `O` |
| 11 | mà | `O` |
| 12 | sửa | `B-COMP` |
| 13 | lỗi, | `I-COMP` |
| 14 | chứ | `O` |
| 15 | mà | `O` |
| 16 | im | `O` |
| 17 | lặng | `O` |
| 18 | chỉ | `O` |
| 19 | biết | `O` |
| 20 | lấy | `O` |
| 21 | tiền | `O` |
| 22 | người | `O` |
| 23 | ta | `O` |
| 24 | như | `O` |
| 25 | vậy, | `O` |
| 26 | thế | `O` |
| 27 | thì | `O` |
| 28 | còn | `O` |
| 29 | gì | `O` |
| 30 | là | `O` |
| 31 | game | `O` |
| 32 | nữa, | `O` |
| 33 | tôi | `O` |
| 34 | đã | `O` |
| 35 | chơi | `O` |
| 36 | game | `O` |
| 37 | này | `O` |
| 38 | từ | `O` |
| 39 | hồi | `O` |
| 40 | còn | `O` |
| 41 | trên | `O` |
| 42 | pc | `O` |
| 43 | giờ | `O` |
| 44 | tới | `O` |
| 45 | mobil | `O` |
| 46 | , | `O` |
| 47 | cũng | `B-COMP` |
| 48 | không | `I-COMP` |
| 49 | tệ, | `I-COMP` |
| 50 | nhưng | `O` |
| 51 | mỗi | `O` |
| 52 | cái, | `O` |
| 53 | cũng | `O` |
| 54 | phải | `O` |
| 55 | sửa | `O` |
| 56 | lại | `O` |
| 57 | cho | `O` |
| 58 | người | `O` |
| 59 | chơi | `O` |
| 60 | thổi | `O` |
| 61 | mái | `O` |
| 62 | hơn | `O` |
| 63 | nhé | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 126. `train_002692`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> mới nhận máy, tạm thời cứ cho  5star  đã. đóng gói sơ xài, vận chuyển 2 ngày mà không lót bất kỳ một lớp mút hay bao nào bảo vê máy cả.

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mới | `O` |
| 1 | nhận | `O` |
| 2 | máy, | `O` |
| 3 | tạm | `O` |
| 4 | thời | `O` |
| 5 | cứ | `O` |
| 6 | cho | `O` |
| 7 | 5star | `O` |
| 8 | đã. | `O` |
| 9 | đóng | `O` |
| 10 | gói | `O` |
| 11 | sơ | `O` |
| 12 | xài, | `O` |
| 13 | vận | `O` |
| 14 | chuyển | `O` |
| 15 | 2 | `O` |
| 16 | ngày | `O` |
| 17 | mà | `O` |
| 18 | không | `O` |
| 19 | lót | `O` |
| 20 | bất | `O` |
| 21 | kỳ | `O` |
| 22 | một | `O` |
| 23 | lớp | `O` |
| 24 | mút | `O` |
| 25 | hay | `O` |
| 26 | bao | `O` |
| 27 | nào | `O` |
| 28 | bảo | `O` |
| 29 | vê | `O` |
| 30 | máy | `O` |
| 31 | cả. | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 127. `train_002335`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> pin trâu , camera khá không chuẩn 48mp

**Spans:**

- #0 [11:38] `camera khá không chuẩn 48mp` label=`COMP`

**Reason:** Cụm 'camera khá không chuẩn 48mp' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | pin | `O` |
| 1 | trâu | `O` |
| 2 | , | `O` |
| 3 | camera | `B-COMP` |
| 4 | khá | `I-COMP` |
| 5 | không | `I-COMP` |
| 6 | chuẩn | `I-COMP` |
| 7 | 48mp | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (62.5%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 128. `train_000104`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> hang ok,dong goi can than.. chưa nhận được hoá đơn

**Spans:**

- #0 [28:50] `chưa nhận được hoá đơn` label=`COMP`

**Reason:** Cụm 'chưa nhận được hoá đơn' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hang | `O` |
| 1 | ok,dong | `O` |
| 2 | goi | `O` |
| 3 | can | `O` |
| 4 | than.. | `O` |
| 5 | chưa | `B-COMP` |
| 6 | nhận | `I-COMP` |
| 7 | được | `I-COMP` |
| 8 | hoá | `I-COMP` |
| 9 | đơn | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 129. `train_003410`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đường may không khéo lắm , nhưng với giá này thì quá được luôn 👍👍👍

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đường | `O` |
| 1 | may | `O` |
| 2 | không | `O` |
| 3 | khéo | `O` |
| 4 | lắm | `O` |
| 5 | , | `O` |
| 6 | nhưng | `O` |
| 7 | với | `O` |
| 8 | giá | `O` |
| 9 | này | `O` |
| 10 | thì | `O` |
| 11 | quá | `O` |
| 12 | được | `O` |
| 13 | luôn | `O` |
| 14 | 👍👍👍 | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 130. `train_000005`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đặc mẫu xanh mà sao giao mẫu này vậy  cửa hàng 

**Spans:**

- #0 [16:46] `sao giao mẫu này vậy  cửa hàng` label=`COMP`

**Reason:** Cụm 'sao giao mẫu này vậy  cửa hàng' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đặc | `O` |
| 1 | mẫu | `O` |
| 2 | xanh | `O` |
| 3 | mà | `O` |
| 4 | sao | `B-COMP` |
| 5 | giao | `I-COMP` |
| 6 | mẫu | `I-COMP` |
| 7 | này | `I-COMP` |
| 8 | vậy | `I-COMP` |
| 9 | cửa | `I-COMP` |
| 10 | hàng | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (63.6%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 131. `train_001107`

- Domain: `app`
- Split: `train`

**Text gốc:**

>  không em 8 của tôi không thể chạy  được , ứng dụng chạy 79% rồi ngừng hẳn, tôi yêu cầu admin phải fix lại lỗi của ứng dụng này, tôi không thể hiểu tại sao các bạn có thể làm như vậy với hãng samsung máy của tôi như vậy mà biết bao người dùng giống tôi đã lên tiếng mà các bạn không hề làm, quá đáng đã 3 thán... bài đánh giá đầy đủ

**Spans:**

- #0 [1:40] `không em 8 của tôi không thể chạy  được` label=`COMP`
- #1 [76:127] `tôi yêu cầu admin phải fix lại lỗi của ứng dụng này` label=`COMP`
- #2 [269:289] `các bạn không hề làm` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | không | `B-COMP` |
| 1 | em | `I-COMP` |
| 2 | 8 | `I-COMP` |
| 3 | của | `I-COMP` |
| 4 | tôi | `I-COMP` |
| 5 | không | `I-COMP` |
| 6 | thể | `I-COMP` |
| 7 | chạy | `I-COMP` |
| 8 | được | `I-COMP` |
| 9 | , | `O` |
| 10 | ứng | `O` |
| 11 | dụng | `O` |
| 12 | chạy | `O` |
| 13 | 79% | `O` |
| 14 | rồi | `O` |
| 15 | ngừng | `O` |
| 16 | hẳn, | `O` |
| 17 | tôi | `B-COMP` |
| 18 | yêu | `I-COMP` |
| 19 | cầu | `I-COMP` |
| 20 | admin | `I-COMP` |
| 21 | phải | `I-COMP` |
| 22 | fix | `I-COMP` |
| 23 | lại | `I-COMP` |
| 24 | lỗi | `I-COMP` |
| 25 | của | `I-COMP` |
| 26 | ứng | `I-COMP` |
| 27 | dụng | `I-COMP` |
| 28 | này, | `I-COMP` |
| 29 | tôi | `O` |
| 30 | không | `O` |
| 31 | thể | `O` |
| 32 | hiểu | `O` |
| 33 | tại | `O` |
| 34 | sao | `O` |
| 35 | các | `O` |
| 36 | bạn | `O` |
| 37 | có | `O` |
| 38 | thể | `O` |
| 39 | làm | `O` |
| 40 | như | `O` |
| 41 | vậy | `O` |
| 42 | với | `O` |
| 43 | hãng | `O` |
| 44 | samsung | `O` |
| 45 | máy | `O` |
| 46 | của | `O` |
| 47 | tôi | `O` |
| 48 | như | `O` |
| 49 | vậy | `O` |
| 50 | mà | `O` |
| 51 | biết | `O` |
| 52 | bao | `O` |
| 53 | người | `O` |
| 54 | dùng | `O` |
| 55 | giống | `O` |
| 56 | tôi | `O` |
| 57 | đã | `O` |
| 58 | lên | `O` |
| 59 | tiếng | `O` |
| 60 | mà | `O` |
| 61 | các | `B-COMP` |
| 62 | bạn | `I-COMP` |
| 63 | không | `I-COMP` |
| 64 | hề | `I-COMP` |
| 65 | làm, | `I-COMP` |
| 66 | quá | `O` |
| 67 | đáng | `O` |
| 68 | đã | `O` |
| 69 | 3 | `O` |
| 70 | thán... | `O` |
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

## 132. `train_004352`

- Domain: `app`
- Split: `train`

**Text gốc:**

> về phần sao lưu tin nhắn, tôi muốn hỏi là tin nhắn trong smartphone sẽ tự động biến mất dần theo năm tháng lý do là giản lược bộ nhớ, điều này sẽ dẫn đến việc sao lưu tin nhắn hằng ngày. file mới sẽ ghi đè lên file cũ trên máy chủ zalo, và khi điều này xảy ra thì tin nhắn thực tế chỉ sao lưu lại nhữ... bài đánh giá đầy đủ

**Spans:**

- #0 [26:132] `tôi muốn hỏi là tin nhắn trong smartphone sẽ tự động biến mất dần theo năm tháng lý do là giản lược bộ nhớ` label=`COMP`

**Reason:** Cụm 'tôi muốn hỏi là tin nhắn trong smartphone sẽ tự động biến mất dần theo năm tháng lý do là giản lược bộ nhớ' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | về | `O` |
| 1 | phần | `O` |
| 2 | sao | `O` |
| 3 | lưu | `O` |
| 4 | tin | `O` |
| 5 | nhắn, | `O` |
| 6 | tôi | `B-COMP` |
| 7 | muốn | `I-COMP` |
| 8 | hỏi | `I-COMP` |
| 9 | là | `I-COMP` |
| 10 | tin | `I-COMP` |
| 11 | nhắn | `I-COMP` |
| 12 | trong | `I-COMP` |
| 13 | smartphone | `I-COMP` |
| 14 | sẽ | `I-COMP` |
| 15 | tự | `I-COMP` |
| 16 | động | `I-COMP` |
| 17 | biến | `I-COMP` |
| 18 | mất | `I-COMP` |
| 19 | dần | `I-COMP` |
| 20 | theo | `I-COMP` |
| 21 | năm | `I-COMP` |
| 22 | tháng | `I-COMP` |
| 23 | lý | `I-COMP` |
| 24 | do | `I-COMP` |
| 25 | là | `I-COMP` |
| 26 | giản | `I-COMP` |
| 27 | lược | `I-COMP` |
| 28 | bộ | `I-COMP` |
| 29 | nhớ, | `I-COMP` |
| 30 | điều | `O` |
| 31 | này | `O` |
| 32 | sẽ | `O` |
| 33 | dẫn | `O` |
| 34 | đến | `O` |
| 35 | việc | `O` |
| 36 | sao | `O` |
| 37 | lưu | `O` |
| 38 | tin | `O` |
| 39 | nhắn | `O` |
| 40 | hằng | `O` |
| 41 | ngày. | `O` |
| 42 | file | `O` |
| 43 | mới | `O` |
| 44 | sẽ | `O` |
| 45 | ghi | `O` |
| 46 | đè | `O` |
| 47 | lên | `O` |
| 48 | file | `O` |
| 49 | cũ | `O` |
| 50 | trên | `O` |
| 51 | máy | `O` |
| 52 | chủ | `O` |
| 53 | zalo, | `O` |
| 54 | và | `O` |
| 55 | khi | `O` |
| 56 | điều | `O` |
| 57 | này | `O` |
| 58 | xảy | `O` |
| 59 | ra | `O` |
| 60 | thì | `O` |
| 61 | tin | `O` |
| 62 | nhắn | `O` |
| 63 | thực | `O` |
| 64 | tế | `O` |
| 65 | chỉ | `O` |
| 66 | sao | `O` |
| 67 | lưu | `O` |
| 68 | lại | `O` |
| 69 | nhữ... | `O` |
| 70 | bài | `O` |
| 71 | đánh | `O` |
| 72 | giá | `O` |
| 73 | đầy | `O` |
| 74 | đủ | `O` |

**Heuristic warnings:**

- span #0 quá dài (24 tokens >= 15)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 133. `train_001631`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> dù hơi nhỏ thân yếu.  cửa hàng  gởi 2 cái mà màu đen không.vải được. nói chung giá như vậy là tốt rồi, tiền nào của nấy mà

**Spans:**

- #0 [0:19] `dù hơi nhỏ thân yếu` label=`COMP`

**Reason:** Cụm 'dù hơi nhỏ thân yếu' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | dù | `B-COMP` |
| 1 | hơi | `I-COMP` |
| 2 | nhỏ | `I-COMP` |
| 3 | thân | `I-COMP` |
| 4 | yếu. | `I-COMP` |
| 5 | cửa | `O` |
| 6 | hàng | `O` |
| 7 | gởi | `O` |
| 8 | 2 | `O` |
| 9 | cái | `O` |
| 10 | mà | `O` |
| 11 | màu | `O` |
| 12 | đen | `O` |
| 13 | không.vải | `O` |
| 14 | được. | `O` |
| 15 | nói | `O` |
| 16 | chung | `O` |
| 17 | giá | `O` |
| 18 | như | `O` |
| 19 | vậy | `O` |
| 20 | là | `O` |
| 21 | tốt | `O` |
| 22 | rồi, | `O` |
| 23 | tiền | `O` |
| 24 | nào | `O` |
| 25 | của | `O` |
| 26 | nấy | `O` |
| 27 | mà | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 134. `train_001725`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> sữa rửa mặt ok, hàng chính hãng, nếu không tạo bọt kĩ thì khi rửa mấy bạn da thường sẽ khô một tí và rít rít, nhưng yên tâm chỉ khoảng 5p sau là sẽ không còn rít nữa. còn về nước tẩy trang thì có mùi trà xanh nhẹ, sạch sẽ và không phải sạch bong kin kít đâu, khi tẩy trang xong vẫn còn độ ẩm, chai 70ml xài cũng khoảng một tháng đối với những người dùng một lần một ngày như mình ❤

**Spans:**

- #0 [33:108] `nếu không tạo bọt kĩ thì khi rửa mấy bạn da thường sẽ khô một tí và rít rít` label=`COMP`
- #1 [158:165] `rít nữa` label=`COMP`
- #2 [171:212] `về nước tẩy trang thì có mùi trà xanh nhẹ` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | sữa | `O` |
| 1 | rửa | `O` |
| 2 | mặt | `O` |
| 3 | ok, | `O` |
| 4 | hàng | `O` |
| 5 | chính | `O` |
| 6 | hãng, | `O` |
| 7 | nếu | `B-COMP` |
| 8 | không | `I-COMP` |
| 9 | tạo | `I-COMP` |
| 10 | bọt | `I-COMP` |
| 11 | kĩ | `I-COMP` |
| 12 | thì | `I-COMP` |
| 13 | khi | `I-COMP` |
| 14 | rửa | `I-COMP` |
| 15 | mấy | `I-COMP` |
| 16 | bạn | `I-COMP` |
| 17 | da | `I-COMP` |
| 18 | thường | `I-COMP` |
| 19 | sẽ | `I-COMP` |
| 20 | khô | `I-COMP` |
| 21 | một | `I-COMP` |
| 22 | tí | `I-COMP` |
| 23 | và | `I-COMP` |
| 24 | rít | `I-COMP` |
| 25 | rít, | `I-COMP` |
| 26 | nhưng | `O` |
| 27 | yên | `O` |
| 28 | tâm | `O` |
| 29 | chỉ | `O` |
| 30 | khoảng | `O` |
| 31 | 5p | `O` |
| 32 | sau | `O` |
| 33 | là | `O` |
| 34 | sẽ | `O` |
| 35 | không | `O` |
| 36 | còn | `O` |
| 37 | rít | `B-COMP` |
| 38 | nữa. | `I-COMP` |
| 39 | còn | `O` |
| 40 | về | `B-COMP` |
| 41 | nước | `I-COMP` |
| 42 | tẩy | `I-COMP` |
| 43 | trang | `I-COMP` |
| 44 | thì | `I-COMP` |
| 45 | có | `I-COMP` |
| 46 | mùi | `I-COMP` |
| 47 | trà | `I-COMP` |
| 48 | xanh | `I-COMP` |
| 49 | nhẹ, | `I-COMP` |
| 50 | sạch | `O` |
| 51 | sẽ | `O` |
| 52 | và | `O` |
| 53 | không | `O` |
| 54 | phải | `O` |
| 55 | sạch | `O` |
| 56 | bong | `O` |
| 57 | kin | `O` |
| 58 | kít | `O` |
| 59 | đâu, | `O` |
| 60 | khi | `O` |
| 61 | tẩy | `O` |
| 62 | trang | `O` |
| 63 | xong | `O` |
| 64 | vẫn | `O` |
| 65 | còn | `O` |
| 66 | độ | `O` |
| 67 | ẩm, | `O` |
| 68 | chai | `O` |
| 69 | 70ml | `O` |
| 70 | xài | `O` |
| 71 | cũng | `O` |
| 72 | khoảng | `O` |
| 73 | một | `O` |
| 74 | tháng | `O` |
| 75 | đối | `O` |
| 76 | với | `O` |
| 77 | những | `O` |
| 78 | người | `O` |
| 79 | dùng | `O` |
| 80 | một | `O` |
| 81 | lần | `O` |
| 82 | một | `O` |
| 83 | ngày | `O` |
| 84 | như | `O` |
| 85 | mình | `O` |
| 86 | ❤ | `O` |

**Heuristic warnings:**

- span #0 quá dài (19 tokens >= 15)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 135. `train_002887`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đặt 5 cái sao  cửa hàng  giao có 3 cái vậy

**Spans:**

- #0 [0:42] `đặt 5 cái sao  cửa hàng  giao có 3 cái vậy` label=`COMP`

**Reason:** Cụm 'đặt 5 cái sao  cửa hàng  giao có 3 cái vậy' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đặt | `B-COMP` |
| 1 | 5 | `I-COMP` |
| 2 | cái | `I-COMP` |
| 3 | sao | `I-COMP` |
| 4 | cửa | `I-COMP` |
| 5 | hàng | `I-COMP` |
| 6 | giao | `I-COMP` |
| 7 | có | `I-COMP` |
| 8 | 3 | `I-COMP` |
| 9 | cái | `I-COMP` |
| 10 | vậy | `I-COMP` |

**Heuristic warnings:**

- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 136. `train_000800`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> tôi đặt 2 cái ngày 2409 nhưng lazada chỉ giao một cái ngày 279. một cái đến chiều 309 vẫn đang ở tình trạng đóng gói, tôi phải gọi lên tổng đài để hỏi và được giải thích rằng đơn hàng có thể bị huỷ và không giao đến được. quá hạn giao hàng đơn hàng sẽ tự động huỷ. và khuyến khích tôi huỷ đơn hàng đặt lại.tôi đã viết email phàn nàn và không một email phản hồi vào chiều hôm ấy. do tôi cần gấp nên khuya đó tôi đã phải đặt 01 đơn khác. sáng hôm sau tôi phát hiện 02 đơn đang giao hàng. một đơn giao trễ nhưng không tự động huỷ và 01 đơn đặt vào tối đó vì tôi sợ qua ngày mai sẽ không còn giá khuyến mãi tốt. kết  quả  dư bây giờ dư một cái máy. rất thất vọng về xử lý đơn hàng của lazada

**Spans:**

- #0 [118:220] `tôi phải gọi lên tổng đài để hỏi và được giải thích rằng đơn hàng có thể bị huỷ và không giao đến được` label=`COMP`
- #1 [222:263] `quá hạn giao hàng đơn hàng sẽ tự động huỷ` label=`COMP`
- #2 [265:305] `và khuyến khích tôi huỷ đơn hàng đặt lại` label=`COMP`
- #3 [379:434] `do tôi cần gấp nên khuya đó tôi đã phải đặt 01 đơn khác` label=`COMP`
- #4 [436:484] `sáng hôm sau tôi phát hiện 02 đơn đang giao hàng` label=`COMP`
- #5 [509:606] `không tự động huỷ và 01 đơn đặt vào tối đó vì tôi sợ qua ngày mai sẽ không còn giá khuyến mãi tốt` label=`COMP`
- #6 [645:687] `rất thất vọng về xử lý đơn hàng của lazada` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tôi | `O` |
| 1 | đặt | `O` |
| 2 | 2 | `O` |
| 3 | cái | `O` |
| 4 | ngày | `O` |
| 5 | 2409 | `O` |
| 6 | nhưng | `O` |
| 7 | lazada | `O` |
| 8 | chỉ | `O` |
| 9 | giao | `O` |
| 10 | một | `O` |
| 11 | cái | `O` |
| 12 | ngày | `O` |
| 13 | 279. | `O` |
| 14 | một | `O` |
| 15 | cái | `O` |
| 16 | đến | `O` |
| 17 | chiều | `O` |
| 18 | 309 | `O` |
| 19 | vẫn | `O` |
| 20 | đang | `O` |
| 21 | ở | `O` |
| 22 | tình | `O` |
| 23 | trạng | `O` |
| 24 | đóng | `O` |
| 25 | gói, | `O` |
| 26 | tôi | `B-COMP` |
| 27 | phải | `I-COMP` |
| 28 | gọi | `I-COMP` |
| 29 | lên | `I-COMP` |
| 30 | tổng | `I-COMP` |
| 31 | đài | `I-COMP` |
| 32 | để | `I-COMP` |
| 33 | hỏi | `I-COMP` |
| 34 | và | `I-COMP` |
| 35 | được | `I-COMP` |
| 36 | giải | `I-COMP` |
| 37 | thích | `I-COMP` |
| 38 | rằng | `I-COMP` |
| 39 | đơn | `I-COMP` |
| 40 | hàng | `I-COMP` |
| 41 | có | `I-COMP` |
| 42 | thể | `I-COMP` |
| 43 | bị | `I-COMP` |
| 44 | huỷ | `I-COMP` |
| 45 | và | `I-COMP` |
| 46 | không | `I-COMP` |
| 47 | giao | `I-COMP` |
| 48 | đến | `I-COMP` |
| 49 | được. | `I-COMP` |
| 50 | quá | `B-COMP` |
| 51 | hạn | `I-COMP` |
| 52 | giao | `I-COMP` |
| 53 | hàng | `I-COMP` |
| 54 | đơn | `I-COMP` |
| 55 | hàng | `I-COMP` |
| 56 | sẽ | `I-COMP` |
| 57 | tự | `I-COMP` |
| 58 | động | `I-COMP` |
| 59 | huỷ. | `I-COMP` |
| 60 | và | `B-COMP` |
| 61 | khuyến | `I-COMP` |
| 62 | khích | `I-COMP` |
| 63 | tôi | `I-COMP` |
| 64 | huỷ | `I-COMP` |
| 65 | đơn | `I-COMP` |
| 66 | hàng | `I-COMP` |
| 67 | đặt | `I-COMP` |
| 68 | lại.tôi | `I-COMP` |
| 69 | đã | `O` |
| 70 | viết | `O` |
| 71 | email | `O` |
| 72 | phàn | `O` |
| 73 | nàn | `O` |
| 74 | và | `O` |
| 75 | không | `O` |
| 76 | một | `O` |
| 77 | email | `O` |
| 78 | phản | `O` |
| 79 | hồi | `O` |
| 80 | vào | `O` |
| 81 | chiều | `O` |
| 82 | hôm | `O` |
| 83 | ấy. | `O` |
| 84 | do | `B-COMP` |
| 85 | tôi | `I-COMP` |
| 86 | cần | `I-COMP` |
| 87 | gấp | `I-COMP` |
| 88 | nên | `I-COMP` |
| 89 | khuya | `I-COMP` |
| 90 | đó | `I-COMP` |
| 91 | tôi | `I-COMP` |
| 92 | đã | `I-COMP` |
| 93 | phải | `I-COMP` |
| 94 | đặt | `I-COMP` |
| 95 | 01 | `I-COMP` |
| 96 | đơn | `I-COMP` |
| 97 | khác. | `I-COMP` |
| 98 | sáng | `B-COMP` |
| 99 | hôm | `I-COMP` |
| 100 | sau | `I-COMP` |
| 101 | tôi | `I-COMP` |
| 102 | phát | `I-COMP` |
| 103 | hiện | `I-COMP` |
| 104 | 02 | `I-COMP` |
| 105 | đơn | `I-COMP` |
| 106 | đang | `I-COMP` |
| 107 | giao | `I-COMP` |
| 108 | hàng. | `I-COMP` |
| 109 | một | `O` |
| 110 | đơn | `O` |
| 111 | giao | `O` |
| 112 | trễ | `O` |
| 113 | nhưng | `O` |
| 114 | không | `B-COMP` |
| 115 | tự | `I-COMP` |
| 116 | động | `I-COMP` |
| 117 | huỷ | `I-COMP` |
| 118 | và | `I-COMP` |
| 119 | 01 | `I-COMP` |
| 120 | đơn | `I-COMP` |
| 121 | đặt | `I-COMP` |
| 122 | vào | `I-COMP` |
| 123 | tối | `I-COMP` |
| 124 | đó | `I-COMP` |
| 125 | vì | `I-COMP` |
| 126 | tôi | `I-COMP` |
| 127 | sợ | `I-COMP` |
| 128 | qua | `I-COMP` |
| 129 | ngày | `I-COMP` |
| 130 | mai | `I-COMP` |
| 131 | sẽ | `I-COMP` |
| 132 | không | `I-COMP` |
| 133 | còn | `I-COMP` |
| 134 | giá | `I-COMP` |
| 135 | khuyến | `I-COMP` |
| 136 | mãi | `I-COMP` |
| 137 | tốt. | `I-COMP` |
| 138 | kết | `O` |
| 139 | quả | `O` |
| 140 | dư | `O` |
| 141 | bây | `O` |
| 142 | giờ | `O` |
| 143 | dư | `O` |
| 144 | một | `O` |
| 145 | cái | `O` |
| 146 | máy. | `O` |
| 147 | rất | `B-COMP` |
| 148 | thất | `I-COMP` |
| 149 | vọng | `I-COMP` |
| 150 | về | `I-COMP` |
| 151 | xử | `I-COMP` |
| 152 | lý | `I-COMP` |
| 153 | đơn | `I-COMP` |
| 154 | hàng | `I-COMP` |
| 155 | của | `I-COMP` |
| 156 | lazada | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (24 tokens >= 15)
- span #5 quá dài (24 tokens >= 15)
- record có nhiều hơn 4 spans (7 spans)
- tỉ lệ COMP token > 60% (65.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 137. `train_000616`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> sản phẩm chính hãng, đóng gói cẩn thận nhưng giao hàng hơi lâu.

**Spans:**

- #0 [45:62] `giao hàng hơi lâu` label=`COMP`

**Reason:** Cụm 'giao hàng hơi lâu' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | sản | `O` |
| 1 | phẩm | `O` |
| 2 | chính | `O` |
| 3 | hãng, | `O` |
| 4 | đóng | `O` |
| 5 | gói | `O` |
| 6 | cẩn | `O` |
| 7 | thận | `O` |
| 8 | nhưng | `O` |
| 9 | giao | `B-COMP` |
| 10 | hàng | `I-COMP` |
| 11 | hơi | `I-COMP` |
| 12 | lâu. | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 138. `train_000860`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> máy mới như gì vậy chơi game laG tệ hại.

**Spans:**

- #0 [0:39] `máy mới như gì vậy chơi game laG tệ hại` label=`COMP`

**Reason:** Cụm 'máy mới như gì vậy chơi game laG tệ hại' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | máy | `B-COMP` |
| 1 | mới | `I-COMP` |
| 2 | như | `I-COMP` |
| 3 | gì | `I-COMP` |
| 4 | vậy | `I-COMP` |
| 5 | chơi | `I-COMP` |
| 6 | game | `I-COMP` |
| 7 | laG | `I-COMP` |
| 8 | tệ | `I-COMP` |
| 9 | hại. | `I-COMP` |

**Heuristic warnings:**

- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 139. `train_000537`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> hàng đẹp vải được , eo hơi rộng xíu

**Spans:**

- #0 [20:35] `eo hơi rộng xíu` label=`COMP`

**Reason:** Cụm 'eo hơi rộng xíu' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hàng | `O` |
| 1 | đẹp | `O` |
| 2 | vải | `O` |
| 3 | được | `O` |
| 4 | , | `O` |
| 5 | eo | `B-COMP` |
| 6 | hơi | `I-COMP` |
| 7 | rộng | `I-COMP` |
| 8 | xíu | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 140. `train_001321`

- Domain: `app`
- Split: `train`

**Text gốc:**

> ứng dụng rất hay. nhưng mỗi lần tôi đọc thì cứ bảo là không nhận diện  được  giọng nói.

**Spans:**

- #0 [24:86] `mỗi lần tôi đọc thì cứ bảo là không nhận diện  được  giọng nói` label=`COMP`

**Reason:** Cụm 'mỗi lần tôi đọc thì cứ bảo là không nhận diện  được  giọng nói' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | ứng | `O` |
| 1 | dụng | `O` |
| 2 | rất | `O` |
| 3 | hay. | `O` |
| 4 | nhưng | `O` |
| 5 | mỗi | `B-COMP` |
| 6 | lần | `I-COMP` |
| 7 | tôi | `I-COMP` |
| 8 | đọc | `I-COMP` |
| 9 | thì | `I-COMP` |
| 10 | cứ | `I-COMP` |
| 11 | bảo | `I-COMP` |
| 12 | là | `I-COMP` |
| 13 | không | `I-COMP` |
| 14 | nhận | `I-COMP` |
| 15 | diện | `I-COMP` |
| 16 | được | `I-COMP` |
| 17 | giọng | `I-COMP` |
| 18 | nói. | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (73.7%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 141. `train_003843`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> máy thiết kế đẹp. đóng gói chắc chắn lâu lâu cs đơ giật, nhưng với tầm giá này thì  không  đòi hỏi gì nhiều... khuyên mặt nạ nên mua

**Spans:**

- #0 [18:55] `đóng gói chắc chắn lâu lâu cs đơ giật` label=`COMP`

**Reason:** Cụm 'đóng gói chắc chắn lâu lâu cs đơ giật' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | máy | `O` |
| 1 | thiết | `O` |
| 2 | kế | `O` |
| 3 | đẹp. | `O` |
| 4 | đóng | `B-COMP` |
| 5 | gói | `I-COMP` |
| 6 | chắc | `I-COMP` |
| 7 | chắn | `I-COMP` |
| 8 | lâu | `I-COMP` |
| 9 | lâu | `I-COMP` |
| 10 | cs | `I-COMP` |
| 11 | đơ | `I-COMP` |
| 12 | giật, | `I-COMP` |
| 13 | nhưng | `O` |
| 14 | với | `O` |
| 15 | tầm | `O` |
| 16 | giá | `O` |
| 17 | này | `O` |
| 18 | thì | `O` |
| 19 | không | `O` |
| 20 | đòi | `O` |
| 21 | hỏi | `O` |
| 22 | gì | `O` |
| 23 | nhiều... | `O` |
| 24 | khuyên | `O` |
| 25 | mặt | `O` |
| 26 | nạ | `O` |
| 27 | nên | `O` |
| 28 | mua | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 142. `train_001572`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

>  sản phẩm  tốt nhưng không  được  tặg quà như  quả g cáo

**Spans:**

- #0 [21:56] `không  được  tặg quà như  quả g cáo` label=`COMP`

**Reason:** Cụm 'không  được  tặg quà như  quả g cáo' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | sản | `O` |
| 1 | phẩm | `O` |
| 2 | tốt | `O` |
| 3 | nhưng | `O` |
| 4 | không | `B-COMP` |
| 5 | được | `I-COMP` |
| 6 | tặg | `I-COMP` |
| 7 | quà | `I-COMP` |
| 8 | như | `I-COMP` |
| 9 | quả | `I-COMP` |
| 10 | g | `I-COMP` |
| 11 | cáo | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (66.7%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 143. `train_003368`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> giáo hàng chậm, phải gọi lên tổng đài mới được lưu ý giao nhanh hơn

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | giáo | `O` |
| 1 | hàng | `O` |
| 2 | chậm, | `O` |
| 3 | phải | `O` |
| 4 | gọi | `O` |
| 5 | lên | `O` |
| 6 | tổng | `O` |
| 7 | đài | `O` |
| 8 | mới | `O` |
| 9 | được | `O` |
| 10 | lưu | `O` |
| 11 | ý | `O` |
| 12 | giao | `O` |
| 13 | nhanh | `O` |
| 14 | hơn | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 144. `train_001472`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> hàng nguyên seal, nhưng  cửa hàng  chính hãng mà đóng gói thùng ngoài to hơn hộp điện thoại mà không có thêm gì chống sốc khi vận chuyển khiến hộp điện thoại không góc và cạnh rất nhiều, thất vọng hãng lớn mà đóng gói quá sơ sài

**Spans:**

- #0 [95:185] `không có thêm gì chống sốc khi vận chuyển khiến hộp điện thoại không góc và cạnh rất nhiều` label=`COMP`
- #1 [187:228] `thất vọng hãng lớn mà đóng gói quá sơ sài` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hàng | `O` |
| 1 | nguyên | `O` |
| 2 | seal, | `O` |
| 3 | nhưng | `O` |
| 4 | cửa | `O` |
| 5 | hàng | `O` |
| 6 | chính | `O` |
| 7 | hãng | `O` |
| 8 | mà | `O` |
| 9 | đóng | `O` |
| 10 | gói | `O` |
| 11 | thùng | `O` |
| 12 | ngoài | `O` |
| 13 | to | `O` |
| 14 | hơn | `O` |
| 15 | hộp | `O` |
| 16 | điện | `O` |
| 17 | thoại | `O` |
| 18 | mà | `O` |
| 19 | không | `B-COMP` |
| 20 | có | `I-COMP` |
| 21 | thêm | `I-COMP` |
| 22 | gì | `I-COMP` |
| 23 | chống | `I-COMP` |
| 24 | sốc | `I-COMP` |
| 25 | khi | `I-COMP` |
| 26 | vận | `I-COMP` |
| 27 | chuyển | `I-COMP` |
| 28 | khiến | `I-COMP` |
| 29 | hộp | `I-COMP` |
| 30 | điện | `I-COMP` |
| 31 | thoại | `I-COMP` |
| 32 | không | `I-COMP` |
| 33 | góc | `I-COMP` |
| 34 | và | `I-COMP` |
| 35 | cạnh | `I-COMP` |
| 36 | rất | `I-COMP` |
| 37 | nhiều, | `I-COMP` |
| 38 | thất | `B-COMP` |
| 39 | vọng | `I-COMP` |
| 40 | hãng | `I-COMP` |
| 41 | lớn | `I-COMP` |
| 42 | mà | `I-COMP` |
| 43 | đóng | `I-COMP` |
| 44 | gói | `I-COMP` |
| 45 | quá | `I-COMP` |
| 46 | sơ | `I-COMP` |
| 47 | sài | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (19 tokens >= 15)
- tỉ lệ COMP token > 60% (60.4%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 145. `train_001640`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đã  cỡ  không chuẩn rồi còn lươn lẹo, đã liên hệ đổi lại  cỡ  thì báo tự trả phí giao hàng mình vẫn ok, nhưng một tuần lễ không thấy hồi âm,  nhắn tin  hỏi thì báo sẽ hối giao hàng này nọ cuối cùng tới nay vẫn chưa nhận được, tôi mua hàng để đi du lịch mà đi về rồi còn chưa nhận được hàng đổi?  cửa hàng  tệ hại !

**Spans:**

- #0 [28:36] `lươn lẹo` label=`COMP`
- #1 [38:102] `đã liên hệ đổi lại  cỡ  thì báo tự trả phí giao hàng mình vẫn ok` label=`COMP`
- #2 [110:139] `một tuần lễ không thấy hồi âm` label=`COMP`
- #3 [142:224] `nhắn tin  hỏi thì báo sẽ hối giao hàng này nọ cuối cùng tới nay vẫn chưa nhận được` label=`COMP`
- #4 [226:293] `tôi mua hàng để đi du lịch mà đi về rồi còn chưa nhận được hàng đổi` label=`COMP`
- #5 [296:312] `cửa hàng  tệ hại` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đã | `O` |
| 1 | cỡ | `O` |
| 2 | không | `O` |
| 3 | chuẩn | `O` |
| 4 | rồi | `O` |
| 5 | còn | `O` |
| 6 | lươn | `B-COMP` |
| 7 | lẹo, | `I-COMP` |
| 8 | đã | `B-COMP` |
| 9 | liên | `I-COMP` |
| 10 | hệ | `I-COMP` |
| 11 | đổi | `I-COMP` |
| 12 | lại | `I-COMP` |
| 13 | cỡ | `I-COMP` |
| 14 | thì | `I-COMP` |
| 15 | báo | `I-COMP` |
| 16 | tự | `I-COMP` |
| 17 | trả | `I-COMP` |
| 18 | phí | `I-COMP` |
| 19 | giao | `I-COMP` |
| 20 | hàng | `I-COMP` |
| 21 | mình | `I-COMP` |
| 22 | vẫn | `I-COMP` |
| 23 | ok, | `I-COMP` |
| 24 | nhưng | `O` |
| 25 | một | `B-COMP` |
| 26 | tuần | `I-COMP` |
| 27 | lễ | `I-COMP` |
| 28 | không | `I-COMP` |
| 29 | thấy | `I-COMP` |
| 30 | hồi | `I-COMP` |
| 31 | âm, | `I-COMP` |
| 32 | nhắn | `B-COMP` |
| 33 | tin | `I-COMP` |
| 34 | hỏi | `I-COMP` |
| 35 | thì | `I-COMP` |
| 36 | báo | `I-COMP` |
| 37 | sẽ | `I-COMP` |
| 38 | hối | `I-COMP` |
| 39 | giao | `I-COMP` |
| 40 | hàng | `I-COMP` |
| 41 | này | `I-COMP` |
| 42 | nọ | `I-COMP` |
| 43 | cuối | `I-COMP` |
| 44 | cùng | `I-COMP` |
| 45 | tới | `I-COMP` |
| 46 | nay | `I-COMP` |
| 47 | vẫn | `I-COMP` |
| 48 | chưa | `I-COMP` |
| 49 | nhận | `I-COMP` |
| 50 | được, | `I-COMP` |
| 51 | tôi | `B-COMP` |
| 52 | mua | `I-COMP` |
| 53 | hàng | `I-COMP` |
| 54 | để | `I-COMP` |
| 55 | đi | `I-COMP` |
| 56 | du | `I-COMP` |
| 57 | lịch | `I-COMP` |
| 58 | mà | `I-COMP` |
| 59 | đi | `I-COMP` |
| 60 | về | `I-COMP` |
| 61 | rồi | `I-COMP` |
| 62 | còn | `I-COMP` |
| 63 | chưa | `I-COMP` |
| 64 | nhận | `I-COMP` |
| 65 | được | `I-COMP` |
| 66 | hàng | `I-COMP` |
| 67 | đổi? | `I-COMP` |
| 68 | cửa | `B-COMP` |
| 69 | hàng | `I-COMP` |
| 70 | tệ | `I-COMP` |
| 71 | hại | `I-COMP` |
| 72 | ! | `O` |

**Heuristic warnings:**

- span #1 quá dài (16 tokens >= 15)
- span #3 quá dài (19 tokens >= 15)
- span #4 quá dài (17 tokens >= 15)
- record có nhiều hơn 4 spans (6 spans)
- tỉ lệ COMP token > 60% (89.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 146. `train_003598`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> không còn sợ mua không đúng chính hãng nữa rùi, về chất lượng thì khỏi bàn nhé, xài rất hiệu  quả , giảm thâm cực tốt, thấm nhanh dù hơi châm chít nhưng xài vài ngày là quen

**Spans:**

- #0 [10:46] `sợ mua không đúng chính hãng nữa rùi` label=`COMP`

**Reason:** Cụm 'sợ mua không đúng chính hãng nữa rùi' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | không | `O` |
| 1 | còn | `O` |
| 2 | sợ | `B-COMP` |
| 3 | mua | `I-COMP` |
| 4 | không | `I-COMP` |
| 5 | đúng | `I-COMP` |
| 6 | chính | `I-COMP` |
| 7 | hãng | `I-COMP` |
| 8 | nữa | `I-COMP` |
| 9 | rùi, | `I-COMP` |
| 10 | về | `O` |
| 11 | chất | `O` |
| 12 | lượng | `O` |
| 13 | thì | `O` |
| 14 | khỏi | `O` |
| 15 | bàn | `O` |
| 16 | nhé, | `O` |
| 17 | xài | `O` |
| 18 | rất | `O` |
| 19 | hiệu | `O` |
| 20 | quả | `O` |
| 21 | , | `O` |
| 22 | giảm | `O` |
| 23 | thâm | `O` |
| 24 | cực | `O` |
| 25 | tốt, | `O` |
| 26 | thấm | `O` |
| 27 | nhanh | `O` |
| 28 | dù | `O` |
| 29 | hơi | `O` |
| 30 | châm | `O` |
| 31 | chít | `O` |
| 32 | nhưng | `O` |
| 33 | xài | `O` |
| 34 | vài | `O` |
| 35 | ngày | `O` |
| 36 | là | `O` |
| 37 | quen | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 147. `train_002935`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> đóng gói hơi sơ sài, cũng không có ghi chú hàng dễ vỡ, hơi thất vọng với lazada . hàng thì còn nguyên seal hộp mà hộp hơi xấu tí.

**Spans:**

- #0 [21:53] `cũng không có ghi chú hàng dễ vỡ` label=`COMP`
- #1 [55:79] `hơi thất vọng với lazada` label=`COMP`
- #2 [114:128] `hộp hơi xấu tí` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đóng | `O` |
| 1 | gói | `O` |
| 2 | hơi | `O` |
| 3 | sơ | `O` |
| 4 | sài, | `O` |
| 5 | cũng | `B-COMP` |
| 6 | không | `I-COMP` |
| 7 | có | `I-COMP` |
| 8 | ghi | `I-COMP` |
| 9 | chú | `I-COMP` |
| 10 | hàng | `I-COMP` |
| 11 | dễ | `I-COMP` |
| 12 | vỡ, | `I-COMP` |
| 13 | hơi | `B-COMP` |
| 14 | thất | `I-COMP` |
| 15 | vọng | `I-COMP` |
| 16 | với | `I-COMP` |
| 17 | lazada | `I-COMP` |
| 18 | . | `O` |
| 19 | hàng | `O` |
| 20 | thì | `O` |
| 21 | còn | `O` |
| 22 | nguyên | `O` |
| 23 | seal | `O` |
| 24 | hộp | `O` |
| 25 | mà | `O` |
| 26 | hộp | `B-COMP` |
| 27 | hơi | `I-COMP` |
| 28 | xấu | `I-COMP` |
| 29 | tí. | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 148. `train_003783`

- Domain: `app`
- Split: `train`

**Text gốc:**

> game hay lắm nhưng  quả nó cáo nhiều

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | game | `O` |
| 1 | hay | `O` |
| 2 | lắm | `O` |
| 3 | nhưng | `O` |
| 4 | quả | `O` |
| 5 | nó | `O` |
| 6 | cáo | `O` |
| 7 | nhiều | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 149. `train_001310`

- Domain: `app`
- Split: `train`

**Text gốc:**

> hay nhưng không thích ở điểm là những nhạc khác đưa vào thì nhanh không bấm kịp luôn còn nhiều lúc đang khúc nhanh thì phải canh sao cho ở chính giữa nếu không các phím bé tẹo luôn mà còn xa nữa nhưng không thích nhất là nhiều lúc xem  quả người cáo lấy nhạc mới mà không  được  nhưng chỉ cần bật mạng hay wi-fi lên là lag r... bài đánh giá đầy đủ

**Spans:**

- #0 [285:324] `chỉ cần bật mạng hay wi-fi lên là lag r` label=`COMP`

**Reason:** Cụm 'chỉ cần bật mạng hay wi-fi lên là lag r' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hay | `O` |
| 1 | nhưng | `O` |
| 2 | không | `O` |
| 3 | thích | `O` |
| 4 | ở | `O` |
| 5 | điểm | `O` |
| 6 | là | `O` |
| 7 | những | `O` |
| 8 | nhạc | `O` |
| 9 | khác | `O` |
| 10 | đưa | `O` |
| 11 | vào | `O` |
| 12 | thì | `O` |
| 13 | nhanh | `O` |
| 14 | không | `O` |
| 15 | bấm | `O` |
| 16 | kịp | `O` |
| 17 | luôn | `O` |
| 18 | còn | `O` |
| 19 | nhiều | `O` |
| 20 | lúc | `O` |
| 21 | đang | `O` |
| 22 | khúc | `O` |
| 23 | nhanh | `O` |
| 24 | thì | `O` |
| 25 | phải | `O` |
| 26 | canh | `O` |
| 27 | sao | `O` |
| 28 | cho | `O` |
| 29 | ở | `O` |
| 30 | chính | `O` |
| 31 | giữa | `O` |
| 32 | nếu | `O` |
| 33 | không | `O` |
| 34 | các | `O` |
| 35 | phím | `O` |
| 36 | bé | `O` |
| 37 | tẹo | `O` |
| 38 | luôn | `O` |
| 39 | mà | `O` |
| 40 | còn | `O` |
| 41 | xa | `O` |
| 42 | nữa | `O` |
| 43 | nhưng | `O` |
| 44 | không | `O` |
| 45 | thích | `O` |
| 46 | nhất | `O` |
| 47 | là | `O` |
| 48 | nhiều | `O` |
| 49 | lúc | `O` |
| 50 | xem | `O` |
| 51 | quả | `O` |
| 52 | người | `O` |
| 53 | cáo | `O` |
| 54 | lấy | `O` |
| 55 | nhạc | `O` |
| 56 | mới | `O` |
| 57 | mà | `O` |
| 58 | không | `O` |
| 59 | được | `O` |
| 60 | nhưng | `O` |
| 61 | chỉ | `B-COMP` |
| 62 | cần | `I-COMP` |
| 63 | bật | `I-COMP` |
| 64 | mạng | `I-COMP` |
| 65 | hay | `I-COMP` |
| 66 | wi-fi | `I-COMP` |
| 67 | lên | `I-COMP` |
| 68 | là | `I-COMP` |
| 69 | lag | `I-COMP` |
| 70 | r... | `I-COMP` |
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

## 150. `train_002592`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> hộp bị móp méo, điện thoại chưa sử dụng nên chưa nhận xét được. nhìn chung là ổn.  cửa hàng  kích hoạt bảo hành điện tử giúp. cảm ơn!

**Spans:**

- #0 [0:14] `hộp bị móp méo` label=`COMP`

**Reason:** Cụm 'hộp bị móp méo' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hộp | `B-COMP` |
| 1 | bị | `I-COMP` |
| 2 | móp | `I-COMP` |
| 3 | méo, | `I-COMP` |
| 4 | điện | `O` |
| 5 | thoại | `O` |
| 6 | chưa | `O` |
| 7 | sử | `O` |
| 8 | dụng | `O` |
| 9 | nên | `O` |
| 10 | chưa | `O` |
| 11 | nhận | `O` |
| 12 | xét | `O` |
| 13 | được. | `O` |
| 14 | nhìn | `O` |
| 15 | chung | `O` |
| 16 | là | `O` |
| 17 | ổn. | `O` |
| 18 | cửa | `O` |
| 19 | hàng | `O` |
| 20 | kích | `O` |
| 21 | hoạt | `O` |
| 22 | bảo | `O` |
| 23 | hành | `O` |
| 24 | điện | `O` |
| 25 | tử | `O` |
| 26 | giúp. | `O` |
| 27 | cảm | `O` |
| 28 | ơn! | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 151. `train_001947`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> màu lên đẹp nhưng lúc mình ngửi có mùi như mùi cồn rất khó chịu. sản phẩm được bọc lại cẩn thận, có ghi bên ngoài là hàng dễ vỡ để mọi người giao hàng cẩn thận hơn. nhân viên giao hàng rất thân thiện.

**Spans:**

- #0 [18:63] `lúc mình ngửi có mùi như mùi cồn rất khó chịu` label=`COMP`
- #1 [97:163] `có ghi bên ngoài là hàng dễ vỡ để mọi người giao hàng cẩn thận hơn` label=`COMP`
- #2 [165:199] `nhân viên giao hàng rất thân thiện` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | màu | `O` |
| 1 | lên | `O` |
| 2 | đẹp | `O` |
| 3 | nhưng | `O` |
| 4 | lúc | `B-COMP` |
| 5 | mình | `I-COMP` |
| 6 | ngửi | `I-COMP` |
| 7 | có | `I-COMP` |
| 8 | mùi | `I-COMP` |
| 9 | như | `I-COMP` |
| 10 | mùi | `I-COMP` |
| 11 | cồn | `I-COMP` |
| 12 | rất | `I-COMP` |
| 13 | khó | `I-COMP` |
| 14 | chịu. | `I-COMP` |
| 15 | sản | `O` |
| 16 | phẩm | `O` |
| 17 | được | `O` |
| 18 | bọc | `O` |
| 19 | lại | `O` |
| 20 | cẩn | `O` |
| 21 | thận, | `O` |
| 22 | có | `B-COMP` |
| 23 | ghi | `I-COMP` |
| 24 | bên | `I-COMP` |
| 25 | ngoài | `I-COMP` |
| 26 | là | `I-COMP` |
| 27 | hàng | `I-COMP` |
| 28 | dễ | `I-COMP` |
| 29 | vỡ | `I-COMP` |
| 30 | để | `I-COMP` |
| 31 | mọi | `I-COMP` |
| 32 | người | `I-COMP` |
| 33 | giao | `I-COMP` |
| 34 | hàng | `I-COMP` |
| 35 | cẩn | `I-COMP` |
| 36 | thận | `I-COMP` |
| 37 | hơn. | `I-COMP` |
| 38 | nhân | `B-COMP` |
| 39 | viên | `I-COMP` |
| 40 | giao | `I-COMP` |
| 41 | hàng | `I-COMP` |
| 42 | rất | `I-COMP` |
| 43 | thân | `I-COMP` |
| 44 | thiện. | `I-COMP` |

**Heuristic warnings:**

- span #1 quá dài (16 tokens >= 15)
- tỉ lệ COMP token > 60% (75.6%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 152. `train_000838`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> hàng giao không giống hình

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hàng | `O` |
| 1 | giao | `O` |
| 2 | không | `O` |
| 3 | giống | `O` |
| 4 | hình | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 153. `train_001980`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> thấy ghi được tặng son mà không thấy ....giao hàng nhanh đóng gói chắc chắn

**Spans:**

- #0 [26:36] `không thấy` label=`COMP`
- #1 [41:75] `giao hàng nhanh đóng gói chắc chắn` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | thấy | `O` |
| 1 | ghi | `O` |
| 2 | được | `O` |
| 3 | tặng | `O` |
| 4 | son | `O` |
| 5 | mà | `O` |
| 6 | không | `B-COMP` |
| 7 | thấy | `I-COMP` |
| 8 | ....giao | `B-COMP` |
| 9 | hàng | `I-COMP` |
| 10 | nhanh | `I-COMP` |
| 11 | đóng | `I-COMP` |
| 12 | gói | `I-COMP` |
| 13 | chắc | `I-COMP` |
| 14 | chắn | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 154. `train_003594`

- Domain: `app`
- Split: `train`

**Text gốc:**

> tôi đã chơi game này 3 tháng rồi và giờ các phiên bản gần đây tôi không thể chơi game quá một phút bởi vì vào game chưa làm được gì đã đứng màn hình và game ngừng hoạt động, tôi đã yêu cầu trợ giúp arena từ facebOk và họ nói phiên bản mới này sẽ khắc phục được, nhưng mà khi cập nhật xong tôi chỉ thấy... bài đánh giá đầy đủ

**Spans:**

- #0 [0:172] `tôi đã chơi game này 3 tháng rồi và giờ các phiên bản gần đây tôi không thể chơi game quá một phút bởi vì vào game chưa làm được gì đã đứng màn hình và game ngừng hoạt động` label=`COMP`

**Reason:** Cụm 'tôi đã chơi game này 3 tháng rồi và giờ các phiên bản gần đây tôi không thể chơi game quá một phút bởi vì vào game chưa làm được gì đã đứng màn hình và game ngừng hoạt động' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tôi | `B-COMP` |
| 1 | đã | `I-COMP` |
| 2 | chơi | `I-COMP` |
| 3 | game | `I-COMP` |
| 4 | này | `I-COMP` |
| 5 | 3 | `I-COMP` |
| 6 | tháng | `I-COMP` |
| 7 | rồi | `I-COMP` |
| 8 | và | `I-COMP` |
| 9 | giờ | `I-COMP` |
| 10 | các | `I-COMP` |
| 11 | phiên | `I-COMP` |
| 12 | bản | `I-COMP` |
| 13 | gần | `I-COMP` |
| 14 | đây | `I-COMP` |
| 15 | tôi | `I-COMP` |
| 16 | không | `I-COMP` |
| 17 | thể | `I-COMP` |
| 18 | chơi | `I-COMP` |
| 19 | game | `I-COMP` |
| 20 | quá | `I-COMP` |
| 21 | một | `I-COMP` |
| 22 | phút | `I-COMP` |
| 23 | bởi | `I-COMP` |
| 24 | vì | `I-COMP` |
| 25 | vào | `I-COMP` |
| 26 | game | `I-COMP` |
| 27 | chưa | `I-COMP` |
| 28 | làm | `I-COMP` |
| 29 | được | `I-COMP` |
| 30 | gì | `I-COMP` |
| 31 | đã | `I-COMP` |
| 32 | đứng | `I-COMP` |
| 33 | màn | `I-COMP` |
| 34 | hình | `I-COMP` |
| 35 | và | `I-COMP` |
| 36 | game | `I-COMP` |
| 37 | ngừng | `I-COMP` |
| 38 | hoạt | `I-COMP` |
| 39 | động, | `I-COMP` |
| 40 | tôi | `O` |
| 41 | đã | `O` |
| 42 | yêu | `O` |
| 43 | cầu | `O` |
| 44 | trợ | `O` |
| 45 | giúp | `O` |
| 46 | arena | `O` |
| 47 | từ | `O` |
| 48 | facebOk | `O` |
| 49 | và | `O` |
| 50 | họ | `O` |
| 51 | nói | `O` |
| 52 | phiên | `O` |
| 53 | bản | `O` |
| 54 | mới | `O` |
| 55 | này | `O` |
| 56 | sẽ | `O` |
| 57 | khắc | `O` |
| 58 | phục | `O` |
| 59 | được, | `O` |
| 60 | nhưng | `O` |
| 61 | mà | `O` |
| 62 | khi | `O` |
| 63 | cập | `O` |
| 64 | nhật | `O` |
| 65 | xong | `O` |
| 66 | tôi | `O` |
| 67 | chỉ | `O` |
| 68 | thấy... | `O` |
| 69 | bài | `O` |
| 70 | đánh | `O` |
| 71 | giá | `O` |
| 72 | đầy | `O` |
| 73 | đủ | `O` |

**Heuristic warnings:**

- span #0 quá dài (40 tokens >= 15)
- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 155. `train_000037`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> hàng đẹp lắm ạ nhưng thiếu 2 sticker🤦‍♀

**Spans:**

- #0 [21:39] `thiếu 2 sticker🤦‍♀` label=`COMP`

**Reason:** Cụm 'thiếu 2 sticker🤦‍♀' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hàng | `O` |
| 1 | đẹp | `O` |
| 2 | lắm | `O` |
| 3 | ạ | `O` |
| 4 | nhưng | `O` |
| 5 | thiếu | `B-COMP` |
| 6 | 2 | `I-COMP` |
| 7 | sticker🤦‍♀ | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 156. `train_003215`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> mình mua cho chị gái, không biết có phải do da nhạy cảm không mà da mặt chị ấy bị mẩn đỏ lên sau khi sử dung. mình đang cầm về dùng thử rồi gửi lại đánh giá sau vậy. mua có 3 món đồ mà bị giao hàng làm 3 lần, nhận  được  2 món rồi, còn một món (theo lịch) sang tuần mới  được  giao

**Spans:**

- #0 [185:207] `bị giao hàng làm 3 lần` label=`COMP`

**Reason:** Cụm 'bị giao hàng làm 3 lần' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mình | `O` |
| 1 | mua | `O` |
| 2 | cho | `O` |
| 3 | chị | `O` |
| 4 | gái, | `O` |
| 5 | không | `O` |
| 6 | biết | `O` |
| 7 | có | `O` |
| 8 | phải | `O` |
| 9 | do | `O` |
| 10 | da | `O` |
| 11 | nhạy | `O` |
| 12 | cảm | `O` |
| 13 | không | `O` |
| 14 | mà | `O` |
| 15 | da | `O` |
| 16 | mặt | `O` |
| 17 | chị | `O` |
| 18 | ấy | `O` |
| 19 | bị | `O` |
| 20 | mẩn | `O` |
| 21 | đỏ | `O` |
| 22 | lên | `O` |
| 23 | sau | `O` |
| 24 | khi | `O` |
| 25 | sử | `O` |
| 26 | dung. | `O` |
| 27 | mình | `O` |
| 28 | đang | `O` |
| 29 | cầm | `O` |
| 30 | về | `O` |
| 31 | dùng | `O` |
| 32 | thử | `O` |
| 33 | rồi | `O` |
| 34 | gửi | `O` |
| 35 | lại | `O` |
| 36 | đánh | `O` |
| 37 | giá | `O` |
| 38 | sau | `O` |
| 39 | vậy. | `O` |
| 40 | mua | `O` |
| 41 | có | `O` |
| 42 | 3 | `O` |
| 43 | món | `O` |
| 44 | đồ | `O` |
| 45 | mà | `O` |
| 46 | bị | `B-COMP` |
| 47 | giao | `I-COMP` |
| 48 | hàng | `I-COMP` |
| 49 | làm | `I-COMP` |
| 50 | 3 | `I-COMP` |
| 51 | lần, | `I-COMP` |
| 52 | nhận | `O` |
| 53 | được | `O` |
| 54 | 2 | `O` |
| 55 | món | `O` |
| 56 | rồi, | `O` |
| 57 | còn | `O` |
| 58 | một | `O` |
| 59 | món | `O` |
| 60 | (theo | `O` |
| 61 | lịch) | `O` |
| 62 | sang | `O` |
| 63 | tuần | `O` |
| 64 | mới | `O` |
| 65 | được | `O` |
| 66 | giao | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 157. `train_003957`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> giao hàng nhanh nhưng  cửa hàng  không đóng gói bưu kiện chuẩn không có lót  gì  may nhận hàng không bị sao.vấn đi này  cửa hàng  cần lưu ý nhé.oke về sản phẩm.

**Spans:**

- #0 [23:107] `cửa hàng  không đóng gói bưu kiện chuẩn không có lót  gì  may nhận hàng không bị sao` label=`COMP`

**Reason:** Cụm 'cửa hàng  không đóng gói bưu kiện chuẩn không có lót  gì  may nhận hàng không bị sao' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | giao | `O` |
| 1 | hàng | `O` |
| 2 | nhanh | `O` |
| 3 | nhưng | `O` |
| 4 | cửa | `B-COMP` |
| 5 | hàng | `I-COMP` |
| 6 | không | `I-COMP` |
| 7 | đóng | `I-COMP` |
| 8 | gói | `I-COMP` |
| 9 | bưu | `I-COMP` |
| 10 | kiện | `I-COMP` |
| 11 | chuẩn | `I-COMP` |
| 12 | không | `I-COMP` |
| 13 | có | `I-COMP` |
| 14 | lót | `I-COMP` |
| 15 | gì | `I-COMP` |
| 16 | may | `I-COMP` |
| 17 | nhận | `I-COMP` |
| 18 | hàng | `I-COMP` |
| 19 | không | `I-COMP` |
| 20 | bị | `I-COMP` |
| 21 | sao.vấn | `I-COMP` |
| 22 | đi | `O` |
| 23 | này | `O` |
| 24 | cửa | `O` |
| 25 | hàng | `O` |
| 26 | cần | `O` |
| 27 | lưu | `O` |
| 28 | ý | `O` |
| 29 | nhé.oke | `O` |
| 30 | về | `O` |
| 31 | sản | `O` |
| 32 | phẩm. | `O` |

**Heuristic warnings:**

- span #0 quá dài (18 tokens >= 15)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 158. `train_002487`

- Domain: `app`
- Split: `train`

**Text gốc:**

> trò chơi này theo cảm nghĩ của tôi và những thứ tôi cảm nhận được dựa theo kiến thức của tôi và tôi đã áp dụng kiến thức của mình vào cái nhận xét lz này là trò chơi như C . chơi đeo hay  quả người cáo liên tục ngấy con mẹ nó rồi mong game sớm phá sản . tao tặng bọn làm game một câu cuối : game như C quảng cáo lz gì q... bài đánh giá đầy đủ

**Spans:**

- #0 [254:319] `tao tặng bọn làm game một câu cuối : game như C quảng cáo lz gì q` label=`COMP`

**Reason:** Cụm 'tao tặng bọn làm game một câu cuối : game như C quảng cáo lz gì q' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | trò | `O` |
| 1 | chơi | `O` |
| 2 | này | `O` |
| 3 | theo | `O` |
| 4 | cảm | `O` |
| 5 | nghĩ | `O` |
| 6 | của | `O` |
| 7 | tôi | `O` |
| 8 | và | `O` |
| 9 | những | `O` |
| 10 | thứ | `O` |
| 11 | tôi | `O` |
| 12 | cảm | `O` |
| 13 | nhận | `O` |
| 14 | được | `O` |
| 15 | dựa | `O` |
| 16 | theo | `O` |
| 17 | kiến | `O` |
| 18 | thức | `O` |
| 19 | của | `O` |
| 20 | tôi | `O` |
| 21 | và | `O` |
| 22 | tôi | `O` |
| 23 | đã | `O` |
| 24 | áp | `O` |
| 25 | dụng | `O` |
| 26 | kiến | `O` |
| 27 | thức | `O` |
| 28 | của | `O` |
| 29 | mình | `O` |
| 30 | vào | `O` |
| 31 | cái | `O` |
| 32 | nhận | `O` |
| 33 | xét | `O` |
| 34 | lz | `O` |
| 35 | này | `O` |
| 36 | là | `O` |
| 37 | trò | `O` |
| 38 | chơi | `O` |
| 39 | như | `O` |
| 40 | C | `O` |
| 41 | . | `O` |
| 42 | chơi | `O` |
| 43 | đeo | `O` |
| 44 | hay | `O` |
| 45 | quả | `O` |
| 46 | người | `O` |
| 47 | cáo | `O` |
| 48 | liên | `O` |
| 49 | tục | `O` |
| 50 | ngấy | `O` |
| 51 | con | `O` |
| 52 | mẹ | `O` |
| 53 | nó | `O` |
| 54 | rồi | `O` |
| 55 | mong | `O` |
| 56 | game | `O` |
| 57 | sớm | `O` |
| 58 | phá | `O` |
| 59 | sản | `O` |
| 60 | . | `O` |
| 61 | tao | `B-COMP` |
| 62 | tặng | `I-COMP` |
| 63 | bọn | `I-COMP` |
| 64 | làm | `I-COMP` |
| 65 | game | `I-COMP` |
| 66 | một | `I-COMP` |
| 67 | câu | `I-COMP` |
| 68 | cuối | `I-COMP` |
| 69 | : | `I-COMP` |
| 70 | game | `I-COMP` |
| 71 | như | `I-COMP` |
| 72 | C | `I-COMP` |
| 73 | quảng | `I-COMP` |
| 74 | cáo | `I-COMP` |
| 75 | lz | `I-COMP` |
| 76 | gì | `I-COMP` |
| 77 | q... | `I-COMP` |
| 78 | bài | `O` |
| 79 | đánh | `O` |
| 80 | giá | `O` |
| 81 | đầy | `O` |
| 82 | đủ | `O` |

**Heuristic warnings:**

- span #0 quá dài (17 tokens >= 15)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 159. `train_000891`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> hàng rất được nha :3 . có điều shiPer hơi khó chịu 😅

**Spans:**

- #0 [31:52] `shiPer hơi khó chịu 😅` label=`COMP`

**Reason:** Cụm 'shiPer hơi khó chịu 😅' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hàng | `O` |
| 1 | rất | `O` |
| 2 | được | `O` |
| 3 | nha | `O` |
| 4 | :3 | `O` |
| 5 | . | `O` |
| 6 | có | `O` |
| 7 | điều | `O` |
| 8 | shiPer | `B-COMP` |
| 9 | hơi | `I-COMP` |
| 10 | khó | `I-COMP` |
| 11 | chịu | `I-COMP` |
| 12 | 😅 | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 160. `train_003658`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> vãi mỏng

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | vãi | `O` |
| 1 | mỏng | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 161. `train_004295`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> rõ ràng mình đã nhắn tin hỏi  cửa hàng ..mình cũng đặt như này ta cái bảng kèm hàng tặng. vậy mà hàng gửi về vẫn lồn có hàng tặng..hơi thất vọng

**Spans:**

- #0 [97:129] `hàng gửi về vẫn lồn có hàng tặng` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | rõ | `O` |
| 1 | ràng | `O` |
| 2 | mình | `O` |
| 3 | đã | `O` |
| 4 | nhắn | `O` |
| 5 | tin | `O` |
| 6 | hỏi | `O` |
| 7 | cửa | `O` |
| 8 | hàng | `O` |
| 9 | ..mình | `O` |
| 10 | cũng | `O` |
| 11 | đặt | `O` |
| 12 | như | `O` |
| 13 | này | `O` |
| 14 | ta | `O` |
| 15 | cái | `O` |
| 16 | bảng | `O` |
| 17 | kèm | `O` |
| 18 | hàng | `O` |
| 19 | tặng. | `O` |
| 20 | vậy | `O` |
| 21 | mà | `O` |
| 22 | hàng | `B-COMP` |
| 23 | gửi | `I-COMP` |
| 24 | về | `I-COMP` |
| 25 | vẫn | `I-COMP` |
| 26 | lồn | `I-COMP` |
| 27 | có | `I-COMP` |
| 28 | hàng | `I-COMP` |
| 29 | tặng..hơi | `I-COMP` |
| 30 | thất | `O` |
| 31 | vọng | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 162. `train_000978`

- Domain: `app`
- Split: `train`

**Text gốc:**

> nhà phát hành nên làm lại tính năng bán nhân vật, hãy làm cho mọi nhân vật có thể bị bán đi để thu về vật phẩm chứ không giới hạn chỉ bán được nhân vật màu xanh lá. tính năng trên cần xem xét lại, phần còn lại của game thì rất hay, từ đồ hoạ đến hiệu ứng là rất tốt. tôi rất thích game này và chúc ga... bài đánh giá đầy đủ

**Spans:**

- None

**Reason:** Không có khiếu nại rõ ràng; đây chủ yếu là góp ý, mong muốn hoặc đề xuất.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | nhà | `O` |
| 1 | phát | `O` |
| 2 | hành | `O` |
| 3 | nên | `O` |
| 4 | làm | `O` |
| 5 | lại | `O` |
| 6 | tính | `O` |
| 7 | năng | `O` |
| 8 | bán | `O` |
| 9 | nhân | `O` |
| 10 | vật, | `O` |
| 11 | hãy | `O` |
| 12 | làm | `O` |
| 13 | cho | `O` |
| 14 | mọi | `O` |
| 15 | nhân | `O` |
| 16 | vật | `O` |
| 17 | có | `O` |
| 18 | thể | `O` |
| 19 | bị | `O` |
| 20 | bán | `O` |
| 21 | đi | `O` |
| 22 | để | `O` |
| 23 | thu | `O` |
| 24 | về | `O` |
| 25 | vật | `O` |
| 26 | phẩm | `O` |
| 27 | chứ | `O` |
| 28 | không | `O` |
| 29 | giới | `O` |
| 30 | hạn | `O` |
| 31 | chỉ | `O` |
| 32 | bán | `O` |
| 33 | được | `O` |
| 34 | nhân | `O` |
| 35 | vật | `O` |
| 36 | màu | `O` |
| 37 | xanh | `O` |
| 38 | lá. | `O` |
| 39 | tính | `O` |
| 40 | năng | `O` |
| 41 | trên | `O` |
| 42 | cần | `O` |
| 43 | xem | `O` |
| 44 | xét | `O` |
| 45 | lại, | `O` |
| 46 | phần | `O` |
| 47 | còn | `O` |
| 48 | lại | `O` |
| 49 | của | `O` |
| 50 | game | `O` |
| 51 | thì | `O` |
| 52 | rất | `O` |
| 53 | hay, | `O` |
| 54 | từ | `O` |
| 55 | đồ | `O` |
| 56 | hoạ | `O` |
| 57 | đến | `O` |
| 58 | hiệu | `O` |
| 59 | ứng | `O` |
| 60 | là | `O` |
| 61 | rất | `O` |
| 62 | tốt. | `O` |
| 63 | tôi | `O` |
| 64 | rất | `O` |
| 65 | thích | `O` |
| 66 | game | `O` |
| 67 | này | `O` |
| 68 | và | `O` |
| 69 | chúc | `O` |
| 70 | ga... | `O` |
| 71 | bài | `O` |
| 72 | đánh | `O` |
| 73 | giá | `O` |
| 74 | đầy | `O` |
| 75 | đủ | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 163. `train_001163`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> sao em đặt 2 lần đều không đung mau đung  cỡ  sao em mang mong  cửa hàng  phan hoi dùm em

**Spans:**

- #0 [0:89] `sao em đặt 2 lần đều không đung mau đung  cỡ  sao em mang mong  cửa hàng  phan hoi dùm em` label=`COMP`

**Reason:** Cụm 'sao em đặt 2 lần đều không đung mau đung  cỡ  sao em mang mong  cửa hàng  phan hoi dùm em' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | sao | `B-COMP` |
| 1 | em | `I-COMP` |
| 2 | đặt | `I-COMP` |
| 3 | 2 | `I-COMP` |
| 4 | lần | `I-COMP` |
| 5 | đều | `I-COMP` |
| 6 | không | `I-COMP` |
| 7 | đung | `I-COMP` |
| 8 | mau | `I-COMP` |
| 9 | đung | `I-COMP` |
| 10 | cỡ | `I-COMP` |
| 11 | sao | `I-COMP` |
| 12 | em | `I-COMP` |
| 13 | mang | `I-COMP` |
| 14 | mong | `I-COMP` |
| 15 | cửa | `I-COMP` |
| 16 | hàng | `I-COMP` |
| 17 | phan | `I-COMP` |
| 18 | hoi | `I-COMP` |
| 19 | dùm | `I-COMP` |
| 20 | em | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (21 tokens >= 15)
- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 164. `train_003006`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> giao hàng rất nhanh và đúng mẫu gói cẩn thận nhưng tiếc một điều là để có tặng kèm cây son trên sản phẩm nhưng giao không thấy có tặng🙁

**Spans:**

- #0 [111:135] `giao không thấy có tặng🙁` label=`COMP`

**Reason:** Cụm 'giao không thấy có tặng🙁' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | giao | `O` |
| 1 | hàng | `O` |
| 2 | rất | `O` |
| 3 | nhanh | `O` |
| 4 | và | `O` |
| 5 | đúng | `O` |
| 6 | mẫu | `O` |
| 7 | gói | `O` |
| 8 | cẩn | `O` |
| 9 | thận | `O` |
| 10 | nhưng | `O` |
| 11 | tiếc | `O` |
| 12 | một | `O` |
| 13 | điều | `O` |
| 14 | là | `O` |
| 15 | để | `O` |
| 16 | có | `O` |
| 17 | tặng | `O` |
| 18 | kèm | `O` |
| 19 | cây | `O` |
| 20 | son | `O` |
| 21 | trên | `O` |
| 22 | sản | `O` |
| 23 | phẩm | `O` |
| 24 | nhưng | `O` |
| 25 | giao | `B-COMP` |
| 26 | không | `I-COMP` |
| 27 | thấy | `I-COMP` |
| 28 | có | `I-COMP` |
| 29 | tặng🙁 | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 165. `train_001308`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> hàng giao nhanh, chất lượng thì không như mong muốn dùng 2 lần vẫn chưa thấy có hiểu  quả 

**Spans:**

- #0 [17:89] `chất lượng thì không như mong muốn dùng 2 lần vẫn chưa thấy có hiểu  quả` label=`COMP`

**Reason:** Cụm 'chất lượng thì không như mong muốn dùng 2 lần vẫn chưa thấy có hiểu  quả' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hàng | `O` |
| 1 | giao | `O` |
| 2 | nhanh, | `O` |
| 3 | chất | `B-COMP` |
| 4 | lượng | `I-COMP` |
| 5 | thì | `I-COMP` |
| 6 | không | `I-COMP` |
| 7 | như | `I-COMP` |
| 8 | mong | `I-COMP` |
| 9 | muốn | `I-COMP` |
| 10 | dùng | `I-COMP` |
| 11 | 2 | `I-COMP` |
| 12 | lần | `I-COMP` |
| 13 | vẫn | `I-COMP` |
| 14 | chưa | `I-COMP` |
| 15 | thấy | `I-COMP` |
| 16 | có | `I-COMP` |
| 17 | hiểu | `I-COMP` |
| 18 | quả | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (16 tokens >= 15)
- tỉ lệ COMP token > 60% (84.2%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 166. `train_000055`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> nói là  được  tặng khi mua hoá đơn 486k trở lên mà không thấy có gì.rất thất vọng.

**Spans:**

- #0 [51:81] `không thấy có gì.rất thất vọng` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | nói | `O` |
| 1 | là | `O` |
| 2 | được | `O` |
| 3 | tặng | `O` |
| 4 | khi | `O` |
| 5 | mua | `O` |
| 6 | hoá | `O` |
| 7 | đơn | `O` |
| 8 | 486k | `O` |
| 9 | trở | `O` |
| 10 | lên | `O` |
| 11 | mà | `O` |
| 12 | không | `B-COMP` |
| 13 | thấy | `I-COMP` |
| 14 | có | `I-COMP` |
| 15 | gì.rất | `I-COMP` |
| 16 | thất | `I-COMP` |
| 17 | vọng. | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 167. `train_003489`

- Domain: `app`
- Split: `train`

**Text gốc:**

> đéo mẹ game như C vào tạo nv là đứng nếu chplay cho đánh giá âm sao bố cho âm luôn rồi.tốt nhất anh em đừng tải mất công lại xoá

**Spans:**

- #0 [18:36] `vào tạo nv là đứng` label=`COMP`
- #1 [87:128] `tốt nhất anh em đừng tải mất công lại xoá` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đéo | `O` |
| 1 | mẹ | `O` |
| 2 | game | `O` |
| 3 | như | `O` |
| 4 | C | `O` |
| 5 | vào | `B-COMP` |
| 6 | tạo | `I-COMP` |
| 7 | nv | `I-COMP` |
| 8 | là | `I-COMP` |
| 9 | đứng | `I-COMP` |
| 10 | nếu | `O` |
| 11 | chplay | `O` |
| 12 | cho | `O` |
| 13 | đánh | `O` |
| 14 | giá | `O` |
| 15 | âm | `O` |
| 16 | sao | `O` |
| 17 | bố | `O` |
| 18 | cho | `O` |
| 19 | âm | `O` |
| 20 | luôn | `O` |
| 21 | rồi.tốt | `B-COMP` |
| 22 | nhất | `I-COMP` |
| 23 | anh | `I-COMP` |
| 24 | em | `I-COMP` |
| 25 | đừng | `I-COMP` |
| 26 | tải | `I-COMP` |
| 27 | mất | `I-COMP` |
| 28 | công | `I-COMP` |
| 29 | lại | `I-COMP` |
| 30 | xoá | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 168. `train_000264`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> hàng chất lượng nhưng đóng gói hàng cần thêm lót để đảm bảo sản phẩm không bị nứt, bể.

**Spans:**

- #0 [22:81] `đóng gói hàng cần thêm lót để đảm bảo sản phẩm không bị nứt` label=`COMP`
- #1 [83:85] `bể` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hàng | `O` |
| 1 | chất | `O` |
| 2 | lượng | `O` |
| 3 | nhưng | `O` |
| 4 | đóng | `B-COMP` |
| 5 | gói | `I-COMP` |
| 6 | hàng | `I-COMP` |
| 7 | cần | `I-COMP` |
| 8 | thêm | `I-COMP` |
| 9 | lót | `I-COMP` |
| 10 | để | `I-COMP` |
| 11 | đảm | `I-COMP` |
| 12 | bảo | `I-COMP` |
| 13 | sản | `I-COMP` |
| 14 | phẩm | `I-COMP` |
| 15 | không | `I-COMP` |
| 16 | bị | `I-COMP` |
| 17 | nứt, | `I-COMP` |
| 18 | bể. | `B-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (78.9%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 169. `train_002200`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> đóng gói cẩn thận, tuy nhiên hơi thất vọng xíu khi mua hàng ở khung giờ 0-2h 11.11 đưọc tặng kèm sản phẩm khác nhưng đặt xong hỏi hãng báo hết sản phẩm tặng kèm

**Spans:**

- #0 [23:79] `nhiên hơi thất vọng xíu khi mua hàng ở khung giờ 0-2h 11` label=`COMP`
- #1 [117:160] `đặt xong hỏi hãng báo hết sản phẩm tặng kèm` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đóng | `O` |
| 1 | gói | `O` |
| 2 | cẩn | `O` |
| 3 | thận, | `O` |
| 4 | tuy | `O` |
| 5 | nhiên | `B-COMP` |
| 6 | hơi | `I-COMP` |
| 7 | thất | `I-COMP` |
| 8 | vọng | `I-COMP` |
| 9 | xíu | `I-COMP` |
| 10 | khi | `I-COMP` |
| 11 | mua | `I-COMP` |
| 12 | hàng | `I-COMP` |
| 13 | ở | `I-COMP` |
| 14 | khung | `I-COMP` |
| 15 | giờ | `I-COMP` |
| 16 | 0-2h | `I-COMP` |
| 17 | 11.11 | `I-COMP` |
| 18 | đưọc | `O` |
| 19 | tặng | `O` |
| 20 | kèm | `O` |
| 21 | sản | `O` |
| 22 | phẩm | `O` |
| 23 | khác | `O` |
| 24 | nhưng | `O` |
| 25 | đặt | `B-COMP` |
| 26 | xong | `I-COMP` |
| 27 | hỏi | `I-COMP` |
| 28 | hãng | `I-COMP` |
| 29 | báo | `I-COMP` |
| 30 | hết | `I-COMP` |
| 31 | sản | `I-COMP` |
| 32 | phẩm | `I-COMP` |
| 33 | tặng | `I-COMP` |
| 34 | kèm | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (65.7%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 170. `train_003268`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> thông tin đăng tải khi mua sẽ được tặng một lọ kem chống nắng mini  cỡ , tuy nhiên khi nhận hàng không có.

**Spans:**

- #0 [0:70] `thông tin đăng tải khi mua sẽ được tặng một lọ kem chống nắng mini  cỡ` label=`COMP`
- #1 [77:105] `nhiên khi nhận hàng không có` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | thông | `B-COMP` |
| 1 | tin | `I-COMP` |
| 2 | đăng | `I-COMP` |
| 3 | tải | `I-COMP` |
| 4 | khi | `I-COMP` |
| 5 | mua | `I-COMP` |
| 6 | sẽ | `I-COMP` |
| 7 | được | `I-COMP` |
| 8 | tặng | `I-COMP` |
| 9 | một | `I-COMP` |
| 10 | lọ | `I-COMP` |
| 11 | kem | `I-COMP` |
| 12 | chống | `I-COMP` |
| 13 | nắng | `I-COMP` |
| 14 | mini | `I-COMP` |
| 15 | cỡ | `I-COMP` |
| 16 | , | `O` |
| 17 | tuy | `O` |
| 18 | nhiên | `B-COMP` |
| 19 | khi | `I-COMP` |
| 20 | nhận | `I-COMP` |
| 21 | hàng | `I-COMP` |
| 22 | không | `I-COMP` |
| 23 | có. | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (16 tokens >= 15)
- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (91.7%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 171. `train_001261`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> ô không  gì ong với hình.

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | ô | `O` |
| 1 | không | `O` |
| 2 | gì | `O` |
| 3 | ong | `O` |
| 4 | với | `O` |
| 5 | hình. | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 172. `train_000986`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> quá ngon ... nhưng thiếu tai nghe thôi

**Spans:**

- #0 [19:38] `thiếu tai nghe thôi` label=`COMP`

**Reason:** Cụm 'thiếu tai nghe thôi' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | quá | `O` |
| 1 | ngon | `O` |
| 2 | ... | `O` |
| 3 | nhưng | `O` |
| 4 | thiếu | `B-COMP` |
| 5 | tai | `I-COMP` |
| 6 | nghe | `I-COMP` |
| 7 | thôi | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 173. `train_003839`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> pin 6000 nhưng không trâu cho lắm, chỉ tầm như 4500 thôi, chụp hình bị đẩy màu lên quá rực, làm ảnh bị sai màu hết, cài gcam mới cải thiện được phần nào! hơi thất vọng!

**Spans:**

- #0 [35:56] `chỉ tầm như 4500 thôi` label=`COMP`
- #1 [92:114] `làm ảnh bị sai màu hết` label=`COMP`
- #2 [154:167] `hơi thất vọng` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | pin | `O` |
| 1 | 6000 | `O` |
| 2 | nhưng | `O` |
| 3 | không | `O` |
| 4 | trâu | `O` |
| 5 | cho | `O` |
| 6 | lắm, | `O` |
| 7 | chỉ | `B-COMP` |
| 8 | tầm | `I-COMP` |
| 9 | như | `I-COMP` |
| 10 | 4500 | `I-COMP` |
| 11 | thôi, | `I-COMP` |
| 12 | chụp | `O` |
| 13 | hình | `O` |
| 14 | bị | `O` |
| 15 | đẩy | `O` |
| 16 | màu | `O` |
| 17 | lên | `O` |
| 18 | quá | `O` |
| 19 | rực, | `O` |
| 20 | làm | `B-COMP` |
| 21 | ảnh | `I-COMP` |
| 22 | bị | `I-COMP` |
| 23 | sai | `I-COMP` |
| 24 | màu | `I-COMP` |
| 25 | hết, | `I-COMP` |
| 26 | cài | `O` |
| 27 | gcam | `O` |
| 28 | mới | `O` |
| 29 | cải | `O` |
| 30 | thiện | `O` |
| 31 | được | `O` |
| 32 | phần | `O` |
| 33 | nào! | `O` |
| 34 | hơi | `B-COMP` |
| 35 | thất | `I-COMP` |
| 36 | vọng! | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 174. `train_001499`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đồ đẹp vãi được shiPer vui tính nhưq trừ điểm khi đặc một màu mà giao hai màu  cửa hàng  giao hàng nhanh đóng gói kỉ

**Spans:**

- #0 [76:116] `u  cửa hàng  giao hàng nhanh đóng gói kỉ` label=`COMP`

**Reason:** Cụm 'u  cửa hàng  giao hàng nhanh đóng gói kỉ' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đồ | `O` |
| 1 | đẹp | `O` |
| 2 | vãi | `O` |
| 3 | được | `O` |
| 4 | shiPer | `O` |
| 5 | vui | `O` |
| 6 | tính | `O` |
| 7 | nhưq | `O` |
| 8 | trừ | `O` |
| 9 | điểm | `O` |
| 10 | khi | `O` |
| 11 | đặc | `O` |
| 12 | một | `O` |
| 13 | màu | `O` |
| 14 | mà | `O` |
| 15 | giao | `O` |
| 16 | hai | `O` |
| 17 | màu | `B-COMP` |
| 18 | cửa | `I-COMP` |
| 19 | hàng | `I-COMP` |
| 20 | giao | `I-COMP` |
| 21 | hàng | `I-COMP` |
| 22 | nhanh | `I-COMP` |
| 23 | đóng | `I-COMP` |
| 24 | gói | `I-COMP` |
| 25 | kỉ | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 175. `train_002301`

- Domain: `app`
- Split: `train`

**Text gốc:**

> ở phần  quả người cáo thấy mình có các sự lựa chọn để fix các thứ trông rất hay. nhưng đến lúc chơi lại không có. cảm giác như kiểu treo đầu dê bán thịt chó vậy? hay là mình chưa lên level đủ cao ạ?

**Spans:**

- #0 [87:112] `đến lúc chơi lại không có` label=`COMP`
- #1 [114:160] `cảm giác như kiểu treo đầu dê bán thịt chó vậy` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | ở | `O` |
| 1 | phần | `O` |
| 2 | quả | `O` |
| 3 | người | `O` |
| 4 | cáo | `O` |
| 5 | thấy | `O` |
| 6 | mình | `O` |
| 7 | có | `O` |
| 8 | các | `O` |
| 9 | sự | `O` |
| 10 | lựa | `O` |
| 11 | chọn | `O` |
| 12 | để | `O` |
| 13 | fix | `O` |
| 14 | các | `O` |
| 15 | thứ | `O` |
| 16 | trông | `O` |
| 17 | rất | `O` |
| 18 | hay. | `O` |
| 19 | nhưng | `O` |
| 20 | đến | `B-COMP` |
| 21 | lúc | `I-COMP` |
| 22 | chơi | `I-COMP` |
| 23 | lại | `I-COMP` |
| 24 | không | `I-COMP` |
| 25 | có. | `I-COMP` |
| 26 | cảm | `B-COMP` |
| 27 | giác | `I-COMP` |
| 28 | như | `I-COMP` |
| 29 | kiểu | `I-COMP` |
| 30 | treo | `I-COMP` |
| 31 | đầu | `I-COMP` |
| 32 | dê | `I-COMP` |
| 33 | bán | `I-COMP` |
| 34 | thịt | `I-COMP` |
| 35 | chó | `I-COMP` |
| 36 | vậy? | `I-COMP` |
| 37 | hay | `O` |
| 38 | là | `O` |
| 39 | mình | `O` |
| 40 | chưa | `O` |
| 41 | lên | `O` |
| 42 | level | `O` |
| 43 | đủ | `O` |
| 44 | cao | `O` |
| 45 | ạ? | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 176. `train_001390`

- Domain: `app`
- Split: `train`

**Text gốc:**

> tôi từng chơi cũng thấy vui nhưng từ chiều giờ vào game thì nó để tải tài nguyên long cốt tải hoài không vô  được 

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tôi | `O` |
| 1 | từng | `O` |
| 2 | chơi | `O` |
| 3 | cũng | `O` |
| 4 | thấy | `O` |
| 5 | vui | `O` |
| 6 | nhưng | `O` |
| 7 | từ | `O` |
| 8 | chiều | `O` |
| 9 | giờ | `O` |
| 10 | vào | `O` |
| 11 | game | `O` |
| 12 | thì | `O` |
| 13 | nó | `O` |
| 14 | để | `O` |
| 15 | tải | `O` |
| 16 | tài | `O` |
| 17 | nguyên | `O` |
| 18 | long | `O` |
| 19 | cốt | `O` |
| 20 | tải | `O` |
| 21 | hoài | `O` |
| 22 | không | `O` |
| 23 | vô | `O` |
| 24 | được | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 177. `train_002036`

- Domain: `app`
- Split: `train`

**Text gốc:**

> lừa đảo liên hệ fanpage không trả lời có dấu hiệu lừa tiền người chơi nếu đánh giá  được  0. 5star  là đánh rồi

**Spans:**

- #0 [0:91] `lừa đảo liên hệ fanpage không trả lời có dấu hiệu lừa tiền người chơi nếu đánh giá  được  0` label=`COMP`

**Reason:** Cụm 'lừa đảo liên hệ fanpage không trả lời có dấu hiệu lừa tiền người chơi nếu đánh giá  được  0' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | lừa | `B-COMP` |
| 1 | đảo | `I-COMP` |
| 2 | liên | `I-COMP` |
| 3 | hệ | `I-COMP` |
| 4 | fanpage | `I-COMP` |
| 5 | không | `I-COMP` |
| 6 | trả | `I-COMP` |
| 7 | lời | `I-COMP` |
| 8 | có | `I-COMP` |
| 9 | dấu | `I-COMP` |
| 10 | hiệu | `I-COMP` |
| 11 | lừa | `I-COMP` |
| 12 | tiền | `I-COMP` |
| 13 | người | `I-COMP` |
| 14 | chơi | `I-COMP` |
| 15 | nếu | `I-COMP` |
| 16 | đánh | `I-COMP` |
| 17 | giá | `I-COMP` |
| 18 | được | `I-COMP` |
| 19 | 0. | `I-COMP` |
| 20 | 5star | `O` |
| 21 | là | `O` |
| 22 | đánh | `O` |
| 23 | rồi | `O` |

**Heuristic warnings:**

- span #0 quá dài (20 tokens >= 15)
- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (83.3%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 178. `train_003825`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> sao mà 2 cái màu trắng không Z

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | sao | `O` |
| 1 | mà | `O` |
| 2 | 2 | `O` |
| 3 | cái | `O` |
| 4 | màu | `O` |
| 5 | trắng | `O` |
| 6 | không | `O` |
| 7 | Z | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 179. `train_002062`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> mua trong dịp khuyến mãi kèm quà tặng mà đến khi nhận hàng thì không thấy quà đâu 🥺🥺🥺

**Spans:**

- #0 [41:85] `đến khi nhận hàng thì không thấy quà đâu 🥺🥺🥺` label=`COMP`

**Reason:** Cụm 'đến khi nhận hàng thì không thấy quà đâu 🥺🥺🥺' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mua | `O` |
| 1 | trong | `O` |
| 2 | dịp | `O` |
| 3 | khuyến | `O` |
| 4 | mãi | `O` |
| 5 | kèm | `O` |
| 6 | quà | `O` |
| 7 | tặng | `O` |
| 8 | mà | `O` |
| 9 | đến | `B-COMP` |
| 10 | khi | `I-COMP` |
| 11 | nhận | `I-COMP` |
| 12 | hàng | `I-COMP` |
| 13 | thì | `I-COMP` |
| 14 | không | `I-COMP` |
| 15 | thấy | `I-COMP` |
| 16 | quà | `I-COMP` |
| 17 | đâu | `I-COMP` |
| 18 | 🥺🥺🥺 | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 180. `train_004337`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đường máy quá xấu

**Spans:**

- #0 [0:17] `đường máy quá xấu` label=`COMP`

**Reason:** Cụm 'đường máy quá xấu' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đường | `B-COMP` |
| 1 | máy | `I-COMP` |
| 2 | quá | `I-COMP` |
| 3 | xấu | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 181. `train_003946`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> vừa nhận may, mở  được  có vài tiếng đã bị sọc màn hình. S làm ăn chán quá.

**Spans:**

- #0 [57:74] `S làm ăn chán quá` label=`COMP`

**Reason:** Cụm 'S làm ăn chán quá' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | vừa | `O` |
| 1 | nhận | `O` |
| 2 | may, | `O` |
| 3 | mở | `O` |
| 4 | được | `O` |
| 5 | có | `O` |
| 6 | vài | `O` |
| 7 | tiếng | `O` |
| 8 | đã | `O` |
| 9 | bị | `O` |
| 10 | sọc | `O` |
| 11 | màn | `O` |
| 12 | hình. | `O` |
| 13 | S | `B-COMP` |
| 14 | làm | `I-COMP` |
| 15 | ăn | `I-COMP` |
| 16 | chán | `I-COMP` |
| 17 | quá. | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 182. `train_003500`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> để chương trình khuyến mãi nhưng không nhận được khuyến mãi

**Spans:**

- #0 [33:59] `không nhận được khuyến mãi` label=`COMP`

**Reason:** Cụm 'không nhận được khuyến mãi' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | để | `O` |
| 1 | chương | `O` |
| 2 | trình | `O` |
| 3 | khuyến | `O` |
| 4 | mãi | `O` |
| 5 | nhưng | `O` |
| 6 | không | `B-COMP` |
| 7 | nhận | `I-COMP` |
| 8 | được | `I-COMP` |
| 9 | khuyến | `I-COMP` |
| 10 | mãi | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 183. `train_002508`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> sản phẩm đẹp nhưng mà bị rách một lỗ bên không nên chỉ cho 4 sao thôi

**Spans:**

- #0 [22:69] `bị rách một lỗ bên không nên chỉ cho 4 sao thôi` label=`COMP`

**Reason:** Cụm 'bị rách một lỗ bên không nên chỉ cho 4 sao thôi' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | sản | `O` |
| 1 | phẩm | `O` |
| 2 | đẹp | `O` |
| 3 | nhưng | `O` |
| 4 | mà | `O` |
| 5 | bị | `B-COMP` |
| 6 | rách | `I-COMP` |
| 7 | một | `I-COMP` |
| 8 | lỗ | `I-COMP` |
| 9 | bên | `I-COMP` |
| 10 | không | `I-COMP` |
| 11 | nên | `I-COMP` |
| 12 | chỉ | `I-COMP` |
| 13 | cho | `I-COMP` |
| 14 | 4 | `I-COMP` |
| 15 | sao | `I-COMP` |
| 16 | thôi | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (70.6%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 184. `train_001796`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> màu lên hơi cam, thoa xong bặm môi lại trôi hầu hết son.

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | màu | `O` |
| 1 | lên | `O` |
| 2 | hơi | `O` |
| 3 | cam, | `O` |
| 4 | thoa | `O` |
| 5 | xong | `O` |
| 6 | bặm | `O` |
| 7 | môi | `O` |
| 8 | lại | `O` |
| 9 | trôi | `O` |
| 10 | hầu | `O` |
| 11 | hết | `O` |
| 12 | son. | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 185. `train_004334`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> tôi đã nhận được tin nhắn kích hoạt bảo hành. nhưng tại sao kiểm tra trên trang chủ samsung + nhắn tin qua tổng đài 6060 lại báo là thông tin về điện thoại không đúng ạ

**Spans:**

- #0 [52:168] `tại sao kiểm tra trên trang chủ samsung + nhắn tin qua tổng đài 6060 lại báo là thông tin về điện thoại không đúng ạ` label=`COMP`

**Reason:** Cụm 'tại sao kiểm tra trên trang chủ samsung + nhắn tin qua tổng đài 6060 lại báo là thông tin về điện thoại không đúng ạ' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | tôi | `O` |
| 1 | đã | `O` |
| 2 | nhận | `O` |
| 3 | được | `O` |
| 4 | tin | `O` |
| 5 | nhắn | `O` |
| 6 | kích | `O` |
| 7 | hoạt | `O` |
| 8 | bảo | `O` |
| 9 | hành. | `O` |
| 10 | nhưng | `O` |
| 11 | tại | `B-COMP` |
| 12 | sao | `I-COMP` |
| 13 | kiểm | `I-COMP` |
| 14 | tra | `I-COMP` |
| 15 | trên | `I-COMP` |
| 16 | trang | `I-COMP` |
| 17 | chủ | `I-COMP` |
| 18 | samsung | `I-COMP` |
| 19 | + | `I-COMP` |
| 20 | nhắn | `I-COMP` |
| 21 | tin | `I-COMP` |
| 22 | qua | `I-COMP` |
| 23 | tổng | `I-COMP` |
| 24 | đài | `I-COMP` |
| 25 | 6060 | `I-COMP` |
| 26 | lại | `I-COMP` |
| 27 | báo | `I-COMP` |
| 28 | là | `I-COMP` |
| 29 | thông | `I-COMP` |
| 30 | tin | `I-COMP` |
| 31 | về | `I-COMP` |
| 32 | điện | `I-COMP` |
| 33 | thoại | `I-COMP` |
| 34 | không | `I-COMP` |
| 35 | đúng | `I-COMP` |
| 36 | ạ | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (26 tokens >= 15)
- tỉ lệ COMP token > 60% (70.3%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 186. `train_003283`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> hàng tốt nhưng không thấy quà tặng

**Spans:**

- #0 [15:34] `không thấy quà tặng` label=`COMP`

**Reason:** Cụm 'không thấy quà tặng' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hàng | `O` |
| 1 | tốt | `O` |
| 2 | nhưng | `O` |
| 3 | không | `B-COMP` |
| 4 | thấy | `I-COMP` |
| 5 | quà | `I-COMP` |
| 6 | tặng | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 187. `train_000827`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> dép đẹp hơi nhỏ

**Spans:**

- #0 [0:15] `dép đẹp hơi nhỏ` label=`COMP`

**Reason:** Cụm 'dép đẹp hơi nhỏ' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | dép | `B-COMP` |
| 1 | đẹp | `I-COMP` |
| 2 | hơi | `I-COMP` |
| 3 | nhỏ | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 188. `train_003202`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> đặt giao hàng hoả tốc ngày hôm trước, đến mãi 20h ngày hôm sau mới gọi giao hàng trong khi địa chỉ giao hàng ghi rất rõ là cơ quan làm việc. chất lượng dịch vụ rất tệ

**Spans:**

- #0 [0:36] `đặt giao hàng hoả tốc ngày hôm trước` label=`COMP`
- #1 [38:139] `đến mãi 20h ngày hôm sau mới gọi giao hàng trong khi địa chỉ giao hàng ghi rất rõ là cơ quan làm việc` label=`COMP`
- #2 [141:166] `chất lượng dịch vụ rất tệ` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đặt | `B-COMP` |
| 1 | giao | `I-COMP` |
| 2 | hàng | `I-COMP` |
| 3 | hoả | `I-COMP` |
| 4 | tốc | `I-COMP` |
| 5 | ngày | `I-COMP` |
| 6 | hôm | `I-COMP` |
| 7 | trước, | `I-COMP` |
| 8 | đến | `B-COMP` |
| 9 | mãi | `I-COMP` |
| 10 | 20h | `I-COMP` |
| 11 | ngày | `I-COMP` |
| 12 | hôm | `I-COMP` |
| 13 | sau | `I-COMP` |
| 14 | mới | `I-COMP` |
| 15 | gọi | `I-COMP` |
| 16 | giao | `I-COMP` |
| 17 | hàng | `I-COMP` |
| 18 | trong | `I-COMP` |
| 19 | khi | `I-COMP` |
| 20 | địa | `I-COMP` |
| 21 | chỉ | `I-COMP` |
| 22 | giao | `I-COMP` |
| 23 | hàng | `I-COMP` |
| 24 | ghi | `I-COMP` |
| 25 | rất | `I-COMP` |
| 26 | rõ | `I-COMP` |
| 27 | là | `I-COMP` |
| 28 | cơ | `I-COMP` |
| 29 | quan | `I-COMP` |
| 30 | làm | `I-COMP` |
| 31 | việc. | `I-COMP` |
| 32 | chất | `B-COMP` |
| 33 | lượng | `I-COMP` |
| 34 | dịch | `I-COMP` |
| 35 | vụ | `I-COMP` |
| 36 | rất | `I-COMP` |
| 37 | tệ | `I-COMP` |

**Heuristic warnings:**

- span #1 quá dài (24 tokens >= 15)
- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 189. `train_003483`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> cho đổi  được  không ạ,  cỡ  giao đúng đẹp nhưng hơi nhỏ co thể đổi  được  không ạ

**Spans:**

- #0 [49:82] `hơi nhỏ co thể đổi  được  không ạ` label=`COMP`

**Reason:** Cụm 'hơi nhỏ co thể đổi  được  không ạ' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | cho | `O` |
| 1 | đổi | `O` |
| 2 | được | `O` |
| 3 | không | `O` |
| 4 | ạ, | `O` |
| 5 | cỡ | `O` |
| 6 | giao | `O` |
| 7 | đúng | `O` |
| 8 | đẹp | `O` |
| 9 | nhưng | `O` |
| 10 | hơi | `B-COMP` |
| 11 | nhỏ | `I-COMP` |
| 12 | co | `I-COMP` |
| 13 | thể | `I-COMP` |
| 14 | đổi | `I-COMP` |
| 15 | được | `I-COMP` |
| 16 | không | `I-COMP` |
| 17 | ạ | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 190. `train_002466`

- Domain: `app`
- Split: `train`

**Text gốc:**

> xung quanh tôi có nhiều tài xế đang chờ nhưng không hiểu sao lại chọn tài xế có vị trí cách tôi 10 dãy nhà. máy tôi không có chức năng  chất  với tài xế để nhắn vị trí đón. không hiện ảnh tài xế trong khi ứng dụng của tài xế thì có. nên có chức năng tích điểm như grab. chọn vị trí đón thì không hiện r... bài đánh giá đầy đủ

**Spans:**

- #0 [108:171] `máy tôi không có chức năng  chất  với tài xế để nhắn vị trí đón` label=`COMP`

**Reason:** Cụm 'máy tôi không có chức năng  chất  với tài xế để nhắn vị trí đón' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | xung | `O` |
| 1 | quanh | `O` |
| 2 | tôi | `O` |
| 3 | có | `O` |
| 4 | nhiều | `O` |
| 5 | tài | `O` |
| 6 | xế | `O` |
| 7 | đang | `O` |
| 8 | chờ | `O` |
| 9 | nhưng | `O` |
| 10 | không | `O` |
| 11 | hiểu | `O` |
| 12 | sao | `O` |
| 13 | lại | `O` |
| 14 | chọn | `O` |
| 15 | tài | `O` |
| 16 | xế | `O` |
| 17 | có | `O` |
| 18 | vị | `O` |
| 19 | trí | `O` |
| 20 | cách | `O` |
| 21 | tôi | `O` |
| 22 | 10 | `O` |
| 23 | dãy | `O` |
| 24 | nhà. | `O` |
| 25 | máy | `B-COMP` |
| 26 | tôi | `I-COMP` |
| 27 | không | `I-COMP` |
| 28 | có | `I-COMP` |
| 29 | chức | `I-COMP` |
| 30 | năng | `I-COMP` |
| 31 | chất | `I-COMP` |
| 32 | với | `I-COMP` |
| 33 | tài | `I-COMP` |
| 34 | xế | `I-COMP` |
| 35 | để | `I-COMP` |
| 36 | nhắn | `I-COMP` |
| 37 | vị | `I-COMP` |
| 38 | trí | `I-COMP` |
| 39 | đón. | `I-COMP` |
| 40 | không | `O` |
| 41 | hiện | `O` |
| 42 | ảnh | `O` |
| 43 | tài | `O` |
| 44 | xế | `O` |
| 45 | trong | `O` |
| 46 | khi | `O` |
| 47 | ứng | `O` |
| 48 | dụng | `O` |
| 49 | của | `O` |
| 50 | tài | `O` |
| 51 | xế | `O` |
| 52 | thì | `O` |
| 53 | có. | `O` |
| 54 | nên | `O` |
| 55 | có | `O` |
| 56 | chức | `O` |
| 57 | năng | `O` |
| 58 | tích | `O` |
| 59 | điểm | `O` |
| 60 | như | `O` |
| 61 | grab. | `O` |
| 62 | chọn | `O` |
| 63 | vị | `O` |
| 64 | trí | `O` |
| 65 | đón | `O` |
| 66 | thì | `O` |
| 67 | không | `O` |
| 68 | hiện | `O` |
| 69 | r... | `O` |
| 70 | bài | `O` |
| 71 | đánh | `O` |
| 72 | giá | `O` |
| 73 | đầy | `O` |
| 74 | đủ | `O` |

**Heuristic warnings:**

- span #0 quá dài (15 tokens >= 15)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 191. `train_002934`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> hàng như mô tả, đánh giá chi tiết như sau: cấu hình thì cũng khá, pin trâu, camera đạt mức ổn chứ không cao, màn hình không bị ám, thiết kế không để lại vết bẩn phần vỏ, loa ngoài bình thường và hởi nhỏ hơn nhiều  sản phẩm  khác. phụ kiện kèm theo thì có mỗi cái cục sạc với cáp

**Spans:**

- #0 [111:129] `n hình không bị ám` label=`COMP`
- #1 [131:168] `thiết kế không để lại vết bẩn phần vỏ` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | hàng | `O` |
| 1 | như | `O` |
| 2 | mô | `O` |
| 3 | tả, | `O` |
| 4 | đánh | `O` |
| 5 | giá | `O` |
| 6 | chi | `O` |
| 7 | tiết | `O` |
| 8 | như | `O` |
| 9 | sau: | `O` |
| 10 | cấu | `O` |
| 11 | hình | `O` |
| 12 | thì | `O` |
| 13 | cũng | `O` |
| 14 | khá, | `O` |
| 15 | pin | `O` |
| 16 | trâu, | `O` |
| 17 | camera | `O` |
| 18 | đạt | `O` |
| 19 | mức | `O` |
| 20 | ổn | `O` |
| 21 | chứ | `O` |
| 22 | không | `O` |
| 23 | cao, | `O` |
| 24 | màn | `B-COMP` |
| 25 | hình | `I-COMP` |
| 26 | không | `I-COMP` |
| 27 | bị | `I-COMP` |
| 28 | ám, | `I-COMP` |
| 29 | thiết | `B-COMP` |
| 30 | kế | `I-COMP` |
| 31 | không | `I-COMP` |
| 32 | để | `I-COMP` |
| 33 | lại | `I-COMP` |
| 34 | vết | `I-COMP` |
| 35 | bẩn | `I-COMP` |
| 36 | phần | `I-COMP` |
| 37 | vỏ, | `I-COMP` |
| 38 | loa | `O` |
| 39 | ngoài | `O` |
| 40 | bình | `O` |
| 41 | thường | `O` |
| 42 | và | `O` |
| 43 | hởi | `O` |
| 44 | nhỏ | `O` |
| 45 | hơn | `O` |
| 46 | nhiều | `O` |
| 47 | sản | `O` |
| 48 | phẩm | `O` |
| 49 | khác. | `O` |
| 50 | phụ | `O` |
| 51 | kiện | `O` |
| 52 | kèm | `O` |
| 53 | theo | `O` |
| 54 | thì | `O` |
| 55 | có | `O` |
| 56 | mỗi | `O` |
| 57 | cái | `O` |
| 58 | cục | `O` |
| 59 | sạc | `O` |
| 60 | với | `O` |
| 61 | cáp | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 192. `train_001091`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> vừa nhận hang.tôi ở hcm mà hoả tốc 2 hơi lâu rất với tôi nghi. hàng ổn định. dùng thêm thời gian mấy đánh giá chi tiết được.  cửa hàng  kích hoạt bảo hành giúp nha

**Spans:**

- #0 [27:61] `hoả tốc 2 hơi lâu rất với tôi nghi` label=`COMP`

**Reason:** Cụm 'hoả tốc 2 hơi lâu rất với tôi nghi' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | vừa | `O` |
| 1 | nhận | `O` |
| 2 | hang.tôi | `O` |
| 3 | ở | `O` |
| 4 | hcm | `O` |
| 5 | mà | `O` |
| 6 | hoả | `B-COMP` |
| 7 | tốc | `I-COMP` |
| 8 | 2 | `I-COMP` |
| 9 | hơi | `I-COMP` |
| 10 | lâu | `I-COMP` |
| 11 | rất | `I-COMP` |
| 12 | với | `I-COMP` |
| 13 | tôi | `I-COMP` |
| 14 | nghi. | `I-COMP` |
| 15 | hàng | `O` |
| 16 | ổn | `O` |
| 17 | định. | `O` |
| 18 | dùng | `O` |
| 19 | thêm | `O` |
| 20 | thời | `O` |
| 21 | gian | `O` |
| 22 | mấy | `O` |
| 23 | đánh | `O` |
| 24 | giá | `O` |
| 25 | chi | `O` |
| 26 | tiết | `O` |
| 27 | được. | `O` |
| 28 | cửa | `O` |
| 29 | hàng | `O` |
| 30 | kích | `O` |
| 31 | hoạt | `O` |
| 32 | bảo | `O` |
| 33 | hành | `O` |
| 34 | giúp | `O` |
| 35 | nha | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 193. `train_003416`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> giao đúng màu có cái là hơi nho

**Spans:**

- #0 [0:31] `giao đúng màu có cái là hơi nho` label=`COMP`

**Reason:** Cụm 'giao đúng màu có cái là hơi nho' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | giao | `B-COMP` |
| 1 | đúng | `I-COMP` |
| 2 | màu | `I-COMP` |
| 3 | có | `I-COMP` |
| 4 | cái | `I-COMP` |
| 5 | là | `I-COMP` |
| 6 | hơi | `I-COMP` |
| 7 | nho | `I-COMP` |

**Heuristic warnings:**

- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 194. `train_001880`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> đừng để bị lưa nhé đầm hai lớp mà co môt hoa thì không ra hoa quá tệ 😌😌

**Spans:**

- #0 [34:71] `co môt hoa thì không ra hoa quá tệ 😌😌` label=`COMP`

**Reason:** Cụm 'co môt hoa thì không ra hoa quá tệ 😌😌' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đừng | `O` |
| 1 | để | `O` |
| 2 | bị | `O` |
| 3 | lưa | `O` |
| 4 | nhé | `O` |
| 5 | đầm | `O` |
| 6 | hai | `O` |
| 7 | lớp | `O` |
| 8 | mà | `O` |
| 9 | co | `B-COMP` |
| 10 | môt | `I-COMP` |
| 11 | hoa | `I-COMP` |
| 12 | thì | `I-COMP` |
| 13 | không | `I-COMP` |
| 14 | ra | `I-COMP` |
| 15 | hoa | `I-COMP` |
| 16 | quá | `I-COMP` |
| 17 | tệ | `I-COMP` |
| 18 | 😌😌 | `I-COMP` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 195. `train_000434`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> chất lượng kém

**Spans:**

- None

**Reason:** Không có cụm khiếu nại rõ ràng; đây chủ yếu là góp ý hoặc mô tả trung tính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | chất | `O` |
| 1 | lượng | `O` |
| 2 | kém | `O` |

**Heuristic warnings:**

- spans=[] nhưng cls_label=1

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 196. `train_002543`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> + chất lượng, giá cả hợp lý phù hợp với nhu cầu cơ bản. + dung lượng pin lớn xài rất thoải mái. có kèm củ sạc nhanh 15w. - hàng đóng gói không có lót mút hay nilon đệm khí, may mà điện thoại bên trong không vấn đề gì. - hàng có logo cam kết giao đúng hẹn và tôi sử dụng loại giao hàng hoả tốc thế nhưng đến cuối ngày nhận thông báo hàng giao không thành công vì người nhận không nghe máy trong khi tôi chẳng nhận được cuộc gọi nào. ngày mua là ngày 10 nhưng tới ngày 12 mới nhận được cũng như giao hàng bình thường vậy hoả tốc chỗ nào mà còn đổ lỗi cho khách hàng không nghe máy nữa. tới giờ vẫn chưa thấy lazada phản hồi gì. - kiểm tra bảo hành trên website samsung thấy đã  được  kích hoạt từ ngày 510 trong khi tôi mua vào ngày 10.

**Spans:**

- #0 [123:171] `hàng đóng gói không có lót mút hay nilon đệm khí` label=`COMP`
- #1 [180:216] `điện thoại bên trong không vấn đề gì` label=`COMP`
- #2 [303:430] `đến cuối ngày nhận thông báo hàng giao không thành công vì người nhận không nghe máy trong khi tôi chẳng nhận được cuộc gọi nào` label=`COMP`
- #3 [542:582] `đổ lỗi cho khách hàng không nghe máy nữa` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | + | `O` |
| 1 | chất | `O` |
| 2 | lượng, | `O` |
| 3 | giá | `O` |
| 4 | cả | `O` |
| 5 | hợp | `O` |
| 6 | lý | `O` |
| 7 | phù | `O` |
| 8 | hợp | `O` |
| 9 | với | `O` |
| 10 | nhu | `O` |
| 11 | cầu | `O` |
| 12 | cơ | `O` |
| 13 | bản. | `O` |
| 14 | + | `O` |
| 15 | dung | `O` |
| 16 | lượng | `O` |
| 17 | pin | `O` |
| 18 | lớn | `O` |
| 19 | xài | `O` |
| 20 | rất | `O` |
| 21 | thoải | `O` |
| 22 | mái. | `O` |
| 23 | có | `O` |
| 24 | kèm | `O` |
| 25 | củ | `O` |
| 26 | sạc | `O` |
| 27 | nhanh | `O` |
| 28 | 15w. | `O` |
| 29 | - | `O` |
| 30 | hàng | `B-COMP` |
| 31 | đóng | `I-COMP` |
| 32 | gói | `I-COMP` |
| 33 | không | `I-COMP` |
| 34 | có | `I-COMP` |
| 35 | lót | `I-COMP` |
| 36 | mút | `I-COMP` |
| 37 | hay | `I-COMP` |
| 38 | nilon | `I-COMP` |
| 39 | đệm | `I-COMP` |
| 40 | khí, | `I-COMP` |
| 41 | may | `O` |
| 42 | mà | `O` |
| 43 | điện | `B-COMP` |
| 44 | thoại | `I-COMP` |
| 45 | bên | `I-COMP` |
| 46 | trong | `I-COMP` |
| 47 | không | `I-COMP` |
| 48 | vấn | `I-COMP` |
| 49 | đề | `I-COMP` |
| 50 | gì. | `I-COMP` |
| 51 | - | `O` |
| 52 | hàng | `O` |
| 53 | có | `O` |
| 54 | logo | `O` |
| 55 | cam | `O` |
| 56 | kết | `O` |
| 57 | giao | `O` |
| 58 | đúng | `O` |
| 59 | hẹn | `O` |
| 60 | và | `O` |
| 61 | tôi | `O` |
| 62 | sử | `O` |
| 63 | dụng | `O` |
| 64 | loại | `O` |
| 65 | giao | `O` |
| 66 | hàng | `O` |
| 67 | hoả | `O` |
| 68 | tốc | `O` |
| 69 | thế | `O` |
| 70 | nhưng | `O` |
| 71 | đến | `B-COMP` |
| 72 | cuối | `I-COMP` |
| 73 | ngày | `I-COMP` |
| 74 | nhận | `I-COMP` |
| 75 | thông | `I-COMP` |
| 76 | báo | `I-COMP` |
| 77 | hàng | `I-COMP` |
| 78 | giao | `I-COMP` |
| 79 | không | `I-COMP` |
| 80 | thành | `I-COMP` |
| 81 | công | `I-COMP` |
| 82 | vì | `I-COMP` |
| 83 | người | `I-COMP` |
| 84 | nhận | `I-COMP` |
| 85 | không | `I-COMP` |
| 86 | nghe | `I-COMP` |
| 87 | máy | `I-COMP` |
| 88 | trong | `I-COMP` |
| 89 | khi | `I-COMP` |
| 90 | tôi | `I-COMP` |
| 91 | chẳng | `I-COMP` |
| 92 | nhận | `I-COMP` |
| 93 | được | `I-COMP` |
| 94 | cuộc | `I-COMP` |
| 95 | gọi | `I-COMP` |
| 96 | nào. | `I-COMP` |
| 97 | ngày | `O` |
| 98 | mua | `O` |
| 99 | là | `O` |
| 100 | ngày | `O` |
| 101 | 10 | `O` |
| 102 | nhưng | `O` |
| 103 | tới | `O` |
| 104 | ngày | `O` |
| 105 | 12 | `O` |
| 106 | mới | `O` |
| 107 | nhận | `O` |
| 108 | được | `O` |
| 109 | cũng | `O` |
| 110 | như | `O` |
| 111 | giao | `O` |
| 112 | hàng | `O` |
| 113 | bình | `O` |
| 114 | thường | `O` |
| 115 | vậy | `O` |
| 116 | hoả | `O` |
| 117 | tốc | `O` |
| 118 | chỗ | `O` |
| 119 | nào | `O` |
| 120 | mà | `O` |
| 121 | còn | `O` |
| 122 | đổ | `B-COMP` |
| 123 | lỗi | `I-COMP` |
| 124 | cho | `I-COMP` |
| 125 | khách | `I-COMP` |
| 126 | hàng | `I-COMP` |
| 127 | không | `I-COMP` |
| 128 | nghe | `I-COMP` |
| 129 | máy | `I-COMP` |
| 130 | nữa. | `I-COMP` |
| 131 | tới | `O` |
| 132 | giờ | `O` |
| 133 | vẫn | `O` |
| 134 | chưa | `O` |
| 135 | thấy | `O` |
| 136 | lazada | `O` |
| 137 | phản | `O` |
| 138 | hồi | `O` |
| 139 | gì. | `O` |
| 140 | - | `O` |
| 141 | kiểm | `O` |
| 142 | tra | `O` |
| 143 | bảo | `O` |
| 144 | hành | `O` |
| 145 | trên | `O` |
| 146 | website | `O` |
| 147 | samsung | `O` |
| 148 | thấy | `O` |
| 149 | đã | `O` |
| 150 | được | `O` |
| 151 | kích | `O` |
| 152 | hoạt | `O` |
| 153 | từ | `O` |
| 154 | ngày | `O` |
| 155 | 510 | `O` |
| 156 | trong | `O` |
| 157 | khi | `O` |
| 158 | tôi | `O` |
| 159 | mua | `O` |
| 160 | vào | `O` |
| 161 | ngày | `O` |
| 162 | 10. | `O` |

**Heuristic warnings:**

- span #2 quá dài (26 tokens >= 15)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 197. `train_002535`

- Domain: `cosmetic`
- Split: `train`

**Text gốc:**

> không có quà tặng kèm như  quả người cáo. nhắn tin  cửa hàng  báo kiểm tra lại nhưng rồi im luôn. cách xử lý quá thiếu chuyên nghiệp! sản phẩm giao tới dính muối tôm, bốc mùi, kém vệ sinh.

**Spans:**

- #0 [0:40] `không có quà tặng kèm như  quả người cáo` label=`COMP`
- #1 [98:132] `cách xử lý quá thiếu chuyên nghiệp` label=`COMP`
- #2 [167:174] `bốc mùi` label=`COMP`

**Reason:** Các cụm này nêu trực tiếp các vấn đề chính trong review.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | không | `B-COMP` |
| 1 | có | `I-COMP` |
| 2 | quà | `I-COMP` |
| 3 | tặng | `I-COMP` |
| 4 | kèm | `I-COMP` |
| 5 | như | `I-COMP` |
| 6 | quả | `I-COMP` |
| 7 | người | `I-COMP` |
| 8 | cáo. | `I-COMP` |
| 9 | nhắn | `O` |
| 10 | tin | `O` |
| 11 | cửa | `O` |
| 12 | hàng | `O` |
| 13 | báo | `O` |
| 14 | kiểm | `O` |
| 15 | tra | `O` |
| 16 | lại | `O` |
| 17 | nhưng | `O` |
| 18 | rồi | `O` |
| 19 | im | `O` |
| 20 | luôn. | `O` |
| 21 | cách | `B-COMP` |
| 22 | xử | `I-COMP` |
| 23 | lý | `I-COMP` |
| 24 | quá | `I-COMP` |
| 25 | thiếu | `I-COMP` |
| 26 | chuyên | `I-COMP` |
| 27 | nghiệp! | `I-COMP` |
| 28 | sản | `O` |
| 29 | phẩm | `O` |
| 30 | giao | `O` |
| 31 | tới | `O` |
| 32 | dính | `O` |
| 33 | muối | `O` |
| 34 | tôm, | `O` |
| 35 | bốc | `B-COMP` |
| 36 | mùi, | `I-COMP` |
| 37 | kém | `O` |
| 38 | vệ | `O` |
| 39 | sinh. | `O` |

**Heuristic warnings:**

- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 198. `train_004217`

- Domain: `fashion`
- Split: `train`

**Text gốc:**

> giao hang nhanh dung mẫu  cỡ  hơi rộng vẫn cho  5star  và sẽ ủng hộ tiếp

**Spans:**

- #0 [0:72] `giao hang nhanh dung mẫu  cỡ  hơi rộng vẫn cho  5star  và sẽ ủng hộ tiếp` label=`COMP`

**Reason:** Cụm 'giao hang nhanh dung mẫu  cỡ  hơi rộng vẫn cho  5star  và sẽ ủng hộ tiếp' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | giao | `B-COMP` |
| 1 | hang | `I-COMP` |
| 2 | nhanh | `I-COMP` |
| 3 | dung | `I-COMP` |
| 4 | mẫu | `I-COMP` |
| 5 | cỡ | `I-COMP` |
| 6 | hơi | `I-COMP` |
| 7 | rộng | `I-COMP` |
| 8 | vẫn | `I-COMP` |
| 9 | cho | `I-COMP` |
| 10 | 5star | `I-COMP` |
| 11 | và | `I-COMP` |
| 12 | sẽ | `I-COMP` |
| 13 | ủng | `I-COMP` |
| 14 | hộ | `I-COMP` |
| 15 | tiếp | `I-COMP` |

**Heuristic warnings:**

- span #0 quá dài (16 tokens >= 15)
- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 199. `train_002394`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> đóng gói tệ không lót giấy làm camera bi trầy

**Spans:**

- #0 [0:45] `đóng gói tệ không lót giấy làm camera bi trầy` label=`COMP`

**Reason:** Cụm 'đóng gói tệ không lót giấy làm camera bi trầy' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | đóng | `B-COMP` |
| 1 | gói | `I-COMP` |
| 2 | tệ | `I-COMP` |
| 3 | không | `I-COMP` |
| 4 | lót | `I-COMP` |
| 5 | giấy | `I-COMP` |
| 6 | làm | `I-COMP` |
| 7 | camera | `I-COMP` |
| 8 | bi | `I-COMP` |
| 9 | trầy | `I-COMP` |

**Heuristic warnings:**

- span #0 bắt đầu từ token đầu/text đầu và dài hơn 8 tokens
- tỉ lệ COMP token > 60% (100.0%)

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---

## 200. `train_000896`

- Domain: `mobile`
- Split: `train`

**Text gốc:**

> mới nhận  sản phẩm  2 ngày. cảm quan khá ok. để xài thử vài hôm nữa xem sao. màu xanh nhìn đẹp hơn ảnh nhìu. sau một ngày đã  được  kích hoạt bảo hành. nói chung khá ưng. mỗi tội cảm biến vân tay hơi không nhạy một tẹo. phải để đúng vị trí nó mới chịu nhận dạng.

**Spans:**

- #0 [179:218] `cảm biến vân tay hơi không nhạy một tẹo` label=`COMP`

**Reason:** Cụm 'cảm biến vân tay hơi không nhạy một tẹo' nêu trực tiếp vấn đề chính.

**Token/BIO:**

| idx | token | tag |
|---:|---|---|
| 0 | mới | `O` |
| 1 | nhận | `O` |
| 2 | sản | `O` |
| 3 | phẩm | `O` |
| 4 | 2 | `O` |
| 5 | ngày. | `O` |
| 6 | cảm | `O` |
| 7 | quan | `O` |
| 8 | khá | `O` |
| 9 | ok. | `O` |
| 10 | để | `O` |
| 11 | xài | `O` |
| 12 | thử | `O` |
| 13 | vài | `O` |
| 14 | hôm | `O` |
| 15 | nữa | `O` |
| 16 | xem | `O` |
| 17 | sao. | `O` |
| 18 | màu | `O` |
| 19 | xanh | `O` |
| 20 | nhìn | `O` |
| 21 | đẹp | `O` |
| 22 | hơn | `O` |
| 23 | ảnh | `O` |
| 24 | nhìu. | `O` |
| 25 | sau | `O` |
| 26 | một | `O` |
| 27 | ngày | `O` |
| 28 | đã | `O` |
| 29 | được | `O` |
| 30 | kích | `O` |
| 31 | hoạt | `O` |
| 32 | bảo | `O` |
| 33 | hành. | `O` |
| 34 | nói | `O` |
| 35 | chung | `O` |
| 36 | khá | `O` |
| 37 | ưng. | `O` |
| 38 | mỗi | `O` |
| 39 | tội | `O` |
| 40 | cảm | `B-COMP` |
| 41 | biến | `I-COMP` |
| 42 | vân | `I-COMP` |
| 43 | tay | `I-COMP` |
| 44 | hơi | `I-COMP` |
| 45 | không | `I-COMP` |
| 46 | nhạy | `I-COMP` |
| 47 | một | `I-COMP` |
| 48 | tẹo. | `I-COMP` |
| 49 | phải | `O` |
| 50 | để | `O` |
| 51 | đúng | `O` |
| 52 | vị | `O` |
| 53 | trí | `O` |
| 54 | nó | `O` |
| 55 | mới | `O` |
| 56 | chịu | `O` |
| 57 | nhận | `O` |
| 58 | dạng. | `O` |

**Heuristic warnings:**

- None

**Human review:** OK / NEED_FIX / DROP

**Notes:**

---
