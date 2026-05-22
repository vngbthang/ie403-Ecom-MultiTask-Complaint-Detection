import argparse
import os
import sys
from transformers import AutoTokenizer

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.data_processing.multitask_dataset import MultiTaskDataset


def main():
    parser = argparse.ArgumentParser(description="Diagnose alignment between classification and NER data")
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
    print("DATA ALIGNMENT REPORT")
    print("=" * 60)
    print(f"Classification samples : {report['total_classification_samples']}")
    print(f"Matched NER samples    : {report['matched_samples']}")
    print(f"Missing NER samples    : {report['missing_samples']}")
    print(f"Matched ratio          : {report['matched_ratio'] * 100:.2f}%")
    print(f"Matched with complaint : {report['matched_with_complaint']}")
    print("=" * 60)


if __name__ == "__main__":
    main()
