"""
Chuyen doi file ghi nhan NER tu dinh dang JSONL sang JSON.

Dau vao : data/processed/bio_annotations_final.jsonl
Dau ra   : data/processed/ner_train.json (80%)
           data/processed/ner_test.json  (20%)

Dinh dang dau vao moi dong:
    {"text": ["token1", "token2", ...], "label": ["O", "B-COMP", ...], ...}

Dinh dang dau ra:
    [{"tokens": [...], "ner_tags": [...]}, ...]
"""

import json
import os
from sklearn.model_selection import train_test_split

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INPUT_PATH = os.path.join(BASE_DIR, "data", "processed", "bio_annotations_final.jsonl")
OUTPUT_TRAIN = os.path.join(BASE_DIR, "data", "processed", "ner_train.json")
OUTPUT_TEST = os.path.join(BASE_DIR, "data", "processed", "ner_test.json")


def load_jsonl(path: str) -> list[dict]:
    records = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def transform_record(record: dict) -> dict | None:
    text = record.get("text")
    labels = record.get("label")

    if not text or not labels:
        return None
    if not isinstance(text, list) or not isinstance(labels, list):
        return None
    if len(text) != len(labels):
        return None

    return {
        "tokens": text,
        "ner_tags": labels,
    }


def main():
    print("Doc file dau vao...")
    raw_records = load_jsonl(INPUT_PATH)
    print(f"  Tong so mau doc duoc: {len(raw_records)}")

    print("Chuyen doi va loc mau hop le...")
    converted = []
    skipped = 0
    for rec in raw_records:
        out = transform_record(rec)
        if out is not None:
            converted.append(out)
        else:
            skipped += 1

    print(f"  Mau hop le : {len(converted)}")
    print(f"  Mau bi bo  : {skipped}")

    print("Chia tap Train / Test (80/20, random_state=42)...")
    train_data, test_data = train_test_split(
        converted,
        test_size=0.2,
        random_state=42,
    )
    print(f"  Train: {len(train_data)} mau")
    print(f"  Test : {len(test_data)} mau")

    print(f"Luu {OUTPUT_TRAIN}...")
    with open(OUTPUT_TRAIN, "w", encoding="utf-8") as f:
        json.dump(train_data, f, ensure_ascii=False, indent=2)

    print(f"Luu {OUTPUT_TEST}...")
    with open(OUTPUT_TEST, "w", encoding="utf-8") as f:
        json.dump(test_data, f, ensure_ascii=False, indent=2)

    # Thong ke nhan NER
    all_tags = set()
    for rec in converted:
        all_tags.update(rec["ner_tags"])
    print(f"\nCac nhan NER co mat: {sorted(all_tags)}")

    train_b_comp = sum(1 for r in train_data for t in r["ner_tags"] if t == "B-COMP")
    train_i_comp = sum(1 for r in train_data for t in r["ner_tags"] if t == "I-COMP")
    test_b_comp = sum(1 for r in test_data for t in r["ner_tags"] if t == "B-COMP")
    test_i_comp = sum(1 for r in test_data for t in r["ner_tags"] if t == "I-COMP")

    print(f"\nThong ke nhan:")
    print(f"  Train - B-COMP: {train_b_comp}, I-COMP: {train_i_comp}")
    print(f"  Test  - B-COMP: {test_b_comp}, I-COMP: {test_i_comp}")
    print("\nHoan tat!")


if __name__ == "__main__":
    main()
