import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import pandas as pd
import json
import os

# Them duong dan root vao sys.path de co the import tu src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.utils.utils import clean_vietnamese_text

def prepare_annotation_data(shopee_path, uit_path, output_path):
    print("[INFO] Dang tai du lieu...")

    # Doc 2 bo du lieu
    df_shopee = pd.read_csv(shopee_path)
    df_uit = pd.read_csv(uit_path)

    # Lay cac dong co nhan khieu nai (1 hoac 1.0)
    shopee_complaints = df_shopee[df_shopee['complaint_label'] == 1.0].copy()
    uit_complaints = df_uit[df_uit['label'] == 1.0].copy()

    print(f"[INFO] Shopee complaints: {len(shopee_complaints)} | UIT-VIOCD complaints: {len(uit_complaints)}")

    # Sample ngau nhien 250 dong tu moi bo
    shopee_sample = shopee_complaints.sample(n=250, random_state=42)
    uit_sample = uit_complaints.sample(n=250, random_state=42)

    print("[INFO] Dang lam sach van ban...")
    # Ap dung ham clean_vietnamese_text cho ca 2 bo
    shopee_sample['cleaned_text'] = shopee_sample['review'].apply(clean_vietnamese_text)

    # Cot chua van ban cua UIT-VIOCD la 'review'
    uit_sample['cleaned_text'] = uit_sample['review'].apply(clean_vietnamese_text)

    # Tao danh sach dict chuan dinh dang JSONL (tuong thich Label Studio / Doccano / UBIAI)
    annotation_data = []

    for text in shopee_sample['cleaned_text']:
        if pd.isna(text) or str(text).strip() == "":
            continue
        annotation_data.append({
            "text": text,
            "label": [],
            "meta": {"source": "shopee"}
        })

    for text in uit_sample['cleaned_text']:
        if pd.isna(text) or str(text).strip() == "":
            continue
        annotation_data.append({
            "text": text,
            "label": [],
            "meta": {"source": "uit-viocd"}
        })

    # Chuyen sang DataFrame de tron deu (shuffle) toan bo du lieu
    df_annotation = pd.DataFrame(annotation_data)
    df_annotation = df_annotation.sample(frac=1, random_state=42).reset_index(drop=True)

    # Ghi ra file JSONL
    print(f"[INFO] Dang ghi ket qua ra: {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        for record in df_annotation.to_dict(orient='records'):
            # ensure_ascii=False de hien thi dung tieng Viet
            f.write(json.dumps(record, ensure_ascii=False) + '\n')

    print(f"[OK] Da xuat {len(df_annotation)} records san sang de gan nhan.")

if __name__ == "__main__":
    # Duong dan tuong doi tu thu muc root du an
    SHOPEE_FILE = "data/processed/shopee_mapped.csv"
    UIT_FILE = "data/raw/UIT-ViOCD/train.csv"
    OUTPUT_FILE = "data/processed/annotation_sample.jsonl"

    prepare_annotation_data(SHOPEE_FILE, UIT_FILE, OUTPUT_FILE)
