"""
Create a tiny NER overfit subset from the UIT-ViOCD pilot 100 train split.

The subset is intended to test whether the PhoBERT NER training pipeline can
memorize COMP entities on a very small dataset.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


DEFAULT_INPUT = "data/processed/uit_viocd_pilot_100_ner_train.json"
DEFAULT_OUTPUT = "data/processed/uit_viocd_pilot_100_ner_overfit5.json"
VALID_LABELS = {"O", "B-COMP", "I-COMP"}


def load_records(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig") as f:
        records = json.load(f)
    if not isinstance(records, list):
        raise ValueError(f"Expected JSON list: {path}")
    return records


def validate_record(record: dict[str, Any], index: int) -> None:
    if not isinstance(record, dict):
        raise ValueError(f"Record #{index} is not a JSON object")
    for field in ("id", "tokens", "ner_tags"):
        if field not in record:
            raise ValueError(f"Record #{index} missing field: {field}")
    if not isinstance(record["tokens"], list) or not isinstance(record["ner_tags"], list):
        raise ValueError(f"Record {record['id']} tokens/ner_tags must be lists")
    if len(record["tokens"]) != len(record["ner_tags"]):
        raise ValueError(
            f"Record {record['id']} length mismatch: "
            f"tokens={len(record['tokens'])}, ner_tags={len(record['ner_tags'])}"
        )
    unknown = sorted(set(record["ner_tags"]) - VALID_LABELS)
    if unknown:
        raise ValueError(f"Record {record['id']} has unknown labels: {unknown}")


def record_stats(record: dict[str, Any]) -> dict[str, int | str]:
    counts = Counter(record["ner_tags"])
    b_count = counts["B-COMP"]
    i_count = counts["I-COMP"]
    return {
        "id": str(record["id"]),
        "tokens": len(record["tokens"]),
        "B-COMP": b_count,
        "I-COMP": i_count,
        "total_COMP": b_count + i_count,
    }


def select_overfit_records(records: list[dict[str, Any]], n: int) -> list[dict[str, Any]]:
    candidates = []
    for index, record in enumerate(records):
        stats = record_stats(record)
        has_b = stats["B-COMP"] > 0
        has_i = stats["I-COMP"] > 0
        if has_b and has_i:
            candidates.append((stats["total_COMP"], stats["B-COMP"], stats["I-COMP"], -index, record))

    if len(candidates) < n:
        raise ValueError(f"Only found {len(candidates)} records with both B-COMP and I-COMP; need {n}")

    candidates.sort(reverse=True)
    return [item[-1] for item in candidates[:n]]


def write_records(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    compact_records = [
        {
            "id": record["id"],
            "tokens": record["tokens"],
            "ner_tags": record["ner_tags"],
        }
        for record in records
    ]
    with path.open("w", encoding="utf-8") as f:
        json.dump(compact_records, f, ensure_ascii=False, indent=2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create NER overfit-5 subset.")
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--num-records", type=int, default=5)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    records = load_records(input_path)
    for index, record in enumerate(records):
        validate_record(record, index)

    selected = select_overfit_records(records, args.num_records)
    write_records(selected, output_path)

    print(f"Input : {input_path}")
    print(f"Output: {output_path}")
    print(f"Selected records: {len(selected)}")
    print("=" * 72)
    for stats in [record_stats(record) for record in selected]:
        print(
            f"{stats['id']}: tokens={stats['tokens']} "
            f"B-COMP={stats['B-COMP']} I-COMP={stats['I-COMP']} "
            f"total_COMP={stats['total_COMP']}"
        )


if __name__ == "__main__":
    main()
