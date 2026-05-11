# 🏷️ BIO Annotation Tool - Hướng dẫn Team Collaboration

## 📊 Setup Dữ liệu

✅ **Đã chia 500 samples thành 4 files:**

```
data/processed/
├── annotation_sample_A.jsonl   (Sample 0-124)    → Người A
├── annotation_sample_B.jsonl   (Sample 125-249)  → Người B
├── annotation_sample_C.jsonl   (Sample 250-374)  → Người C
├── annotation_sample_D.jsonl   (Sample 375-499)  → Người D
```

**Mỗi người: ~125 samples**

---

## 🚀 Cách chạy cho 4 người

### **Lựa chọn 1: Cùng 1 máy (Local)**

Terminal 1:
```bash
py -3.11 -m streamlit run bio_annotation_tool_A.py --logger.level=warning
```
👉 Người A vào: http://localhost:8501

Terminal 2:
```bash
py -3.11 -m streamlit run bio_annotation_tool_B.py --client.toolbarMode=minimal --server.port=8502
```
👉 Người B vào: http://localhost:8502

Terminal 3:
```bash
py -3.11 -m streamlit run bio_annotation_tool_C.py --client.toolbarMode=minimal --server.port=8503
```
👉 Người C vào: http://localhost:8503

Terminal 4:
```bash
py -3.11 -m streamlit run bio_annotation_tool_D.py --client.toolbarMode=minimal --server.port=8504
```
👉 Người D vào: http://localhost:8504

---

### **Lựa chọn 2: Trên máy khác (Network)**

**Máy A chạy Streamlit:**
```bash
py -3.11 -m streamlit run bio_annotation_tool_A.py --server.address 0.0.0.0
```

**3 máy khác truy cập:**
- Máy B: `http://<IP_máy_A>:8501`
- Máy C: Chạy `bio_annotation_tool_C.py --server.port=8503` trên máy C, truy cập `http://localhost:8503`
- Máy D: Tương tự

---

## 📝 Quy trình Annotation

### **Mỗi người làm:**
1. Mở tool của mình (A, B, C hoặc D)
2. Đọc bình luận tiếng Việt
3. Click B/I/O cho từng từ:
   - 🔴 **B** = Từ **ĐẦU** khiếu nại
   - 🟠 **I** = Từ **TIẾP THEO** khiếu nại
   - ⚪ **O** = Từ **BÌNH THƯỜNG**
4. Click **✅ Lưu & Tiếp theo** khi xong sample
5. Lặp lại tới sample cuối

### **Ví dụ:**
```
"sản phẩm bị hỏng nặng lắm"

sản        → O (bình thường)
phẩm       → O (bình thường)
bị         → B-COMP (bắt đầu khiếu nại)
hỏng       → I-COMP (tiếp theo khiếu nại)
nặng       → I-COMP (tiếp theo khiếu nại)
lắm        → O (bình thường)
```

---

## 💾 Export Results

### **Khi hoàn tất:**
1. Mỗi người click **"📥 Export JSONL"** → lưu vào file của mình
2. System tự động lưu:
   - `data/processed/bio_annotations_A.jsonl`
   - `data/processed/bio_annotations_B.jsonl`
   - `data/processed/bio_annotations_C.jsonl`
   - `data/processed/bio_annotations_D.jsonl`

---

## 🔗 Gộp Results

**Khi tất cả 4 người xong, chạy:**

```bash
py -3.11 merge_annotations.py
```

Output:
```
🔄 Đang gộp annotations từ 4 người...
============================================================
✅ Người A: 125 annotations
✅ Người B: 125 annotations
✅ Người C: 125 annotations
✅ Người D: 125 annotations
============================================================

📊 Tổng cộng: 500 annotations
✅ Đã lưu vào: data/processed/bio_annotations_merged.jsonl

📈 THỐNG KÊ:
...
```

---

## 📁 File Output Cuối cùng

```
data/processed/bio_annotations_merged.jsonl
```

**Format mỗi record:**
```json
{
  "text": "sản phẩm bị hỏng nặng lắm",
  "tokens": ["sản", "phẩm", "bị", "hỏng", "nặng", "lắm"],
  "labels": ["O", "O", "B-COMP", "I-COMP", "I-COMP", "O"],
  "source": "uit-viocd",
  "annotator": "A",
  "timestamp": "2026-05-11T15:30:00"
}
```

---

## ⚡ Tips

✅ **Nhanh hơn**: Click buttons liên tục, không cần chờ load  
✅ **Không mất dữ liệu**: Mỗi click B/I/O đã lưu ngay  
✅ **Quay lại được**: Click ⬅️ để chỉnh sửa sample trước  
✅ **Bỏ qua được**: Click ⏭️ để bỏ qua sample khó  
✅ **Hỏi thắc mắc**: Xem help section ("ℹ️ Hướng dẫn") bên trong tool  

---

## 🐛 Troubleshooting

**Tool không chạy:**
```bash
py -3.11 -m pip install streamlit --upgrade
py -3.11 -m streamlit run bio_annotation_tool_A.py
```

**Streamlit port bị chiếm:**
Thay đổi `--server.port` thành `8505`, `8506`, ...

---

**Hết rồi! 🎉 Các bạn cứ bắt đầu gán nhãn thôi!**
