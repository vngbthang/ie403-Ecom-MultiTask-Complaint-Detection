import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import pandas as pd
import json

def process_shopee_data(input_path, output_path):
    print(f"[INFO] Doc du lieu tu: {input_path}...")
    
    # Sử dụng pandas để đọc file JSONL (lines=True)
    try:
        df = pd.read_json(input_path, lines=True)
    except ValueError:
        # Fallback nếu pd.read_json gặp lỗi định dạng
        print("[INFO] Doc fallback bang thu vien json...")
        data = []
        with open(input_path, 'r', encoding='utf-8') as f:
            for line in f:
                data.append(json.loads(line))
        df = pd.DataFrame(data)
        
    print(f"[INFO] Tong records ban dau: {len(df)}")
    
    # 1. Drop các dòng bị NaN ở cột 'review'
    df = df.dropna(subset=['review'])
    
    # 2. Bỏ qua rating 3
    df = df[df['rating'] != 3].copy()
    
    # 3. Áp dụng logic tạo complaint_label
    def map_complaint(rating):
        if rating in [1, 2]:
            return 1
        elif rating in [4, 5]:
            return 0
        return None
        
    df['complaint_label'] = df['rating'].apply(map_complaint)
    
    # 4. Lưu lại dữ liệu ra CSV
    # Chỉ giữ các cột cần thiết để tiết kiệm dung lượng
    columns_to_keep = ['review', 'rating', 'complaint_label']
    df_output = df[columns_to_keep]
    
    df_output.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"[OK] Da luu {len(df_output)} records vao: {output_path}")

if __name__ == "__main__":
    # Đường dẫn tương đối từ thư mục root của dự án
    INPUT_FILE = "data/raw/ShopeeReviewsSentiment/shopee_reviews_dataset.jsonl"
    OUTPUT_FILE = "data/processed/shopee_mapped.csv"
    
    process_shopee_data(INPUT_FILE, OUTPUT_FILE)
