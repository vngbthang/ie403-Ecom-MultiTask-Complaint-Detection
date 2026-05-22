import json
import torch
from torch.utils.data import Dataset


class MultiTaskDataset(Dataset):
    """
    Dataset da nhiem vu: classification + NER.

    - 7817 cau phan loai: co class_labels, co the co hoac khong co ner_labels
    - 500 cau NER (tap con): co ca class_labels va ner_labels

    I/O Contract:
        __getitem__ tra ve dict voi dung 4 keys:
            - input_ids
            - attention_mask
            - class_labels
            - ner_labels (toan -100 neu khong co nhan NER)
    """

    LABEL2ID = {"O": 0, "B-COMP": 1, "I-COMP": 2}
    ID2LABEL = {0: "O", 1: "B-COMP", 2: "I-COMP"}

    def __init__(
        self,
        classification_data_path: str,
        ner_data_path: str,
        tokenizer,
        max_len: int = 256,
    ):
        self.tokenizer = tokenizer
        self.max_len = max_len

        # Tap hop IDs cua cac cau co nhan NER
        self.ner_sample_ids = set()

        # Nap du lieu NER
        self.ner_data = {}
        if ner_data_path:
            with open(ner_data_path, encoding="utf-8") as f:
                ner_records = json.load(f)
            for idx, record in enumerate(ner_records):
                self.ner_sample_ids.add(idx)
                self.ner_data[idx] = {
                    "tokens": record["tokens"],
                    "ner_tags": [
                        self.LABEL2ID.get(t, 0)
                        for t in record.get("labels", record.get("ner_tags", []))
                    ],
                }

        # Nap du lieu phan loai
        all_samples = []
        with open(classification_data_path, encoding="utf-8") as f:
            if classification_data_path.endswith(".csv"):
                import csv
                reader = csv.DictReader(f)
                for i, row in enumerate(reader):
                    all_samples.append({
                        "id": i,
                        "text": row["review"],
                        "class_label": int(row["complaint_label"]),
                    })
            else:
                for i, line in enumerate(f):
                    obj = json.loads(line)
                    all_samples.append({
                        "id": i,
                        "text": obj["review"],
                        "class_label": 1 if obj["label"] == "negative" else 0,
                    })

        self.samples = all_samples

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, idx: int) -> dict:
        sample = self.samples[idx]
        text = sample["text"]
        class_label = sample["class_label"]

        # Tokenize
        encoding = self.tokenizer(
            text,
            max_length=self.max_len,
            padding="max_length",
            truncation=True,
            return_tensors="pt",
        )

        input_ids = encoding["input_ids"].squeeze(0)
        attention_mask = encoding["attention_mask"].squeeze(0)

        # Nhan NER
        if idx in self.ner_sample_ids and idx in self.ner_data:
            ner_record = self.ner_data[idx]
            ner_labels = self._align_ner_labels(
                text, ner_record["tokens"], ner_record["ner_tags"], input_ids
            )
        else:
            # Mau khong co nhan NER -> toan -100
            ner_labels = torch.full((self.max_len,), -100, dtype=torch.long)

        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "class_labels": torch.tensor(class_label, dtype=torch.long),
            "ner_labels": ner_labels,
        }

    def _align_ner_labels(
        self, text: str, tokens: list, ner_tags: list, input_ids: torch.Tensor
    ) -> torch.Tensor:
        """Map nhan NER tu token-level sang subword-level."""
        labels = []
        char_to_byte_offset = []
        text_clean = text.replace("\xa0", " ")

        # Build character-to-token mapping
        token_start = 0
        for tok in tokens:
            start = text_clean.find(tok, token_start)
            if start == -1:
                start = token_start
            char_to_byte_offset.append((start, start + len(tok)))
            token_start = start + len(tok)

        # Map nhan NER sang subword
        word_ids = input_ids.word_ids()
        current_word_idx = None

        for word_idx, word_id in enumerate(word_ids):
            if word_id is None:
                labels.append(-100)
            elif word_id != current_word_idx:
                current_word_idx = word_id
                if word_id < len(ner_tags):
                    labels.append(ner_tags[word_id])
                else:
                    labels.append(-100)
            else:
                labels.append(-100)

        result = torch.tensor(labels, dtype=torch.long)
        if len(result) < self.max_len:
            result = torch.cat([result, torch.full((self.max_len - len(result),), -100, dtype=torch.long)])
        elif len(result) > self.max_len:
            result = result[:self.max_len]
        return result


if __name__ == "__main__":
    print("=" * 60)
    print("Test cua MultiTaskDataset")
    print("=" * 60)

    # Kiem tra xem cac file du lieu co ton tai khong
    import os
    data_dir = "../data/processed"
    cls_path = os.path.join(data_dir, "shopee_mapped.csv")
    ner_path = os.path.join(data_dir, "ner_train.json")

    if not os.path.exists(cls_path):
        print(f"[WARN] Khong tim thay: {cls_path}")
        print("Tao dummy data de test...")
        cls_path = None
        ner_path = None

    if cls_path and os.path.exists(ner_path):
        from transformers import AutoTokenizer
        print(f"classification_data: {cls_path}")
        print(f"ner_data           : {ner_path}")

        tokenizer = AutoTokenizer.from_pretrained(
            "vinai/phobert-base-v2",
            use_fast=False
        )

        dataset = MultiTaskDataset(
            classification_data_path=cls_path,
            ner_data_path=ner_path,
            tokenizer=tokenizer,
            max_len=64,
        )

        # Lay 1 mau co NER (idx 0)
        if len(dataset) > 0:
            sample = dataset[0]
            print(f"\n[MAU ID=0] co nhan NER:")
            print(f"  input_ids  shape: {sample['input_ids'].shape}")
            print(f"  attention_mask: {sample['attention_mask'].shape}")
            print(f"  class_labels  : {sample['class_labels'].item()}")
            print(f"  ner_labels    : {sample['ner_labels'].shape}")
            has_ner = (sample['ner_labels'] != -100).any().item()
            print(f"  -> Co nhan NER thuc su: {has_ner}")

        # Lay 1 mau KHONG co NER (idx 499 - khong co trong tap NER)
        non_ner_idx = len(dataset) - 1
        sample_no_ner = dataset[non_ner_idx]
        print(f"\n[MAU ID={non_ner_idx}] KHONG co nhan NER (ner_labels = -100):")
        print(f"  class_labels : {sample_no_ner['class_labels'].item()}")
        print(f"  ner_labels   : shape={sample_no_ner['ner_labels'].shape}")
        print(f"  -> Tat ca -100: {(sample_no_ner['ner_labels'] == -100).all().item()}")
        print(f"  -> So luong -100: {(sample_no_ner['ner_labels'] == -100).sum().item()} / {len(sample_no_ner['ner_labels'])}")

        print(f"\nTong so mau: {len(dataset)}")
    else:
        print("Bo qua test - file du lieu chua co san.")
        print("Can chuan bi:")
        print(f"  1. {cls_path}")
        print(f"  2. {ner_path}")

    print("=" * 60)
