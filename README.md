# Khai thác dữ liệu truyền thông xã hội

Dự án phân loại và trích xuất cụm từ khiếu nại (Span Extraction) từ các bình luận thương mại điện tử tiếng Việt.

## Cấu trúc thư mục

```text
.
├── data/
│   ├── raw/                # Dữ liệu gốc chưa qua xử lý
│   └── processed/          # Dữ liệu đã làm sạch, gán nhãn, sẵn sàng cho model
├── docs/                   # Tài liệu dự án (setup, labeling guideline...)
├── notebooks/              # Jupyter notebooks để EDA và thử nghiệm nhanh
├── src/                    # Source code chính của dự án
│   ├── data_processing/    # Scripts tiền xử lý, tokenize (Pyvi), chia tập train/test
│   ├── models/             # Định nghĩa mô hình (PhoBERT + CRF), loss functions
│   └── utils/              # Các hàm hỗ trợ (tính metrics seqeval, logging, helper)
├── .gitignore              # Chỉ định các file không đẩy lên GitHub
├── README.md               # Tổng quan dự án
└── requirements.txt        # Danh sách các thư viện phụ thuộc
```
