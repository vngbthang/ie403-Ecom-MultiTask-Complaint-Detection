import csv
import json
import argparse
import os
import sys
import torch
from torch.utils.data import Dataset

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.utils.utils import clean_vietnamese_text


def normalize_for_match(text: str) -> str:
    if text is None:
        return ""
    cleaned = clean_vietnamese_text(str(text))
    return "".join(cleaned.split()).lower()

class MultiTaskDataset(Dataset):
    def __init__(self, classification_data_path, ner_data_path, tokenizer, max_len=128):
        self.max_len = max_len
        self.tokenizer = tokenizer
        
        # Đọc file phân loại (CSV)
        self.texts = []
        self.class_labels = []
        with open(classification_data_path, encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.texts.append(row["review"])
                self.class_labels.append(int(row["complaint_label"]))
                
        # Đọc file NER (JSON)
        with open(ner_data_path, encoding="utf-8-sig") as f:
            ner_raw = json.load(f)
            
        self.label2id = {"O": 0, "B-COMP": 1, "I-COMP": 2}
        
        # Khớp câu NER
        self.ner_dict = {}
        for item in ner_raw:
            text_key = normalize_for_match(" ".join(item["tokens"]))
            self.ner_dict[text_key] = item

        self.alignment_report = self._build_alignment_report()

    def _build_alignment_report(self):
        matched = 0
        matched_with_comp = 0
        missing = 0

        for text in self.texts:
            text_key = normalize_for_match(text)
            ner_item = self.ner_dict.get(text_key, None)
            if ner_item is None:
                missing += 1
                continue

            matched += 1
            tags = ner_item.get("ner_tags", [])
            if any(tag in ("B-COMP", "I-COMP", 1, 2) for tag in tags):
                matched_with_comp += 1

        total = len(self.texts)
        matched_ratio = (matched / total) if total else 0.0
        return {
            "total_classification_samples": total,
            "matched_samples": matched,
            "missing_samples": missing,
            "matched_ratio": matched_ratio,
            "matched_with_complaint": matched_with_comp,
        }

    def get_alignment_report(self):
        return dict(self.alignment_report)

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = str(self.texts[idx])
        class_label = self.class_labels[idx]
        
        text_key = normalize_for_match(text)
        ner_item = self.ner_dict.get(text_key, None)
        ner_has_labels = 0
        ner_has_complaint = 0
        
        if ner_item is not None:
            ner_has_labels = 1
            tokens = ner_item["tokens"]
            tags = ner_item.get("ner_tags", [])
            
            input_ids = [self.tokenizer.cls_token_id]
            ner_labels = [-100]
            
            for word, tag in zip(tokens, tags):
                word_tokens = self.tokenizer.tokenize(word)
                if not word_tokens: continue
                
                w_ids = self.tokenizer.convert_tokens_to_ids(word_tokens)
                input_ids.extend(w_ids)
                
                mapped_label = self.label2id[tag] if isinstance(tag, str) else tag
                ner_labels.append(mapped_label)
                ner_labels.extend([-100] * (len(w_ids) - 1))
                if mapped_label in (1, 2):
                    ner_has_complaint = 1
                
            input_ids.append(self.tokenizer.sep_token_id)
            ner_labels.append(-100)
            
            # Cắt chuỗi an toàn
            if len(input_ids) > self.max_len:
                input_ids = input_ids[:self.max_len-1] + [self.tokenizer.sep_token_id]
                ner_labels = ner_labels[:self.max_len-1] + [-100]
                
            # Đệm padding
            attention_mask = [1] * len(input_ids)
            pad_len = self.max_len - len(input_ids)
            if pad_len > 0:
                input_ids.extend([self.tokenizer.pad_token_id] * pad_len)
                attention_mask.extend([0] * pad_len)
                ner_labels.extend([-100] * pad_len)
        else:
            encoded = self.tokenizer(
                text,
                truncation=True,
                max_length=self.max_len,
                padding="max_length"
            )
            input_ids = encoded["input_ids"]
            attention_mask = encoded["attention_mask"]
            ner_labels = [-100] * self.max_len

        return {
            "input_ids": torch.tensor(input_ids, dtype=torch.long),
            "attention_mask": torch.tensor(attention_mask, dtype=torch.long),
            "class_labels": torch.tensor(class_label, dtype=torch.long),
            "ner_labels": torch.tensor(ner_labels, dtype=torch.long),
            "ner_has_labels": torch.tensor(ner_has_labels, dtype=torch.long),
            "ner_has_complaint": torch.tensor(ner_has_complaint, dtype=torch.long),
        }


if __name__ == "__main__":
    from transformers import AutoTokenizer

    parser = argparse.ArgumentParser(description="Diagnose alignment from MultiTaskDataset")
    parser.add_argument("--cls-path", default="data/processed/shopee_mapped.csv")
    parser.add_argument("--ner-path", default="data/processed/ner_train.json")
    parser.add_argument("--max-len", type=int, default=256)
    args = parser.parse_args()

    tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base-v2", use_fast=False)
    dataset = MultiTaskDataset(
        classification_data_path=args.cls_path,
        ner_data_path=args.ner_path,
        tokenizer=tokenizer,
        max_len=args.max_len,
    )
    report = dataset.get_alignment_report()

    print("=" * 60)
    print("MULTITASK DATASET ALIGNMENT REPORT")
    print("=" * 60)
    print(f"Classification samples : {report['total_classification_samples']}")
    print(f"Matched NER samples    : {report['matched_samples']}")
    print(f"Missing NER samples    : {report['missing_samples']}")
    print(f"Matched ratio          : {report['matched_ratio'] * 100:.2f}%")
    print(f"Matched with complaint : {report['matched_with_complaint']}")
    print("=" * 60)
