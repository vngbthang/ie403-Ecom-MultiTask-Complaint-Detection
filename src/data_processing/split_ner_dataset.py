"""
Split a NER JSON dataset into train/val/test subsets.

Default input:
    data/processed/uit_viocd_pilot_100_ner.json
"""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from typing import Any


DEFAULT_INPUT = "data/processed/uit_viocd_pilot_100_ner.json"
DEFAULT_TRAIN = "data/processed/uit_viocd_pilot_100_ner_train.json"
DEFAULT_VAL = "data/processed/uit_viocd_pilot_100_ner_val.json"
DEFAULT_TEST = "data/processed/uit_viocd_pilot_100_ner_test.json"
DEFAULT_SUMMARY = "data/processed/uit_viocd_pilot_100_ner_split_summary.json"


def load_dataset(path: Path) -> list[dict[str, Any]]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"Expected a JSON list: {path}")
    return data


def validate_records(records: list[dict[str, Any]]) -> None:
    seen_ids: set[str] = set()
    for idx, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"Record #{idx} is not an object")
        for field in ("id", "tokens", "ner_tags"):
            if field not in record:
                raise ValueError(f"Record #{idx} missing field: {field}")
        record_id = str(record["id"])
        if record_id in seen_ids:
            raise ValueError(f"Duplicate id in input dataset: {record_id}")
        seen_ids.add(record_id)
        if not isinstance(record["tokens"], list) or not isinstance(record["ner_tags"], list):
            raise ValueError(f"Record {record_id} tokens/ner_tags must be lists")
        if len(record["tokens"]) != len(record["ner_tags"]):
            raise ValueError(
                f"Record {record_id} length mismatch: "
                f"tokens={len(record['tokens'])}, ner_tags={len(record['ner_tags'])}"
            )


def has_comp(record: dict[str, Any]) -> bool:
    return any(tag in ("B-COMP", "I-COMP", 1, 2) for tag in record.get("ner_tags", []))


def split_group(
    group: list[dict[str, Any]],
    train_ratio: float,
    val_ratio: float,
    rng: random.Random,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    shuffled = list(group)
    rng.shuffle(shuffled)
    total = len(shuffled)
    n_train = int(total * train_ratio)
    n_val = int(total * val_ratio)
    train = shuffled[:n_train]
    val = shuffled[n_train : n_train + n_val]
    test = shuffled[n_train + n_val :]
    return train, val, test


def stratified_split(
    records: list[dict[str, Any]],
    train_ratio: float,
    val_ratio: float,
    test_ratio: float,
    seed: int,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    ratio_sum = train_ratio + val_ratio + test_ratio
    if abs(ratio_sum - 1.0) > 1e-6:
        raise ValueError(f"Ratios must sum to 1.0, got {ratio_sum}")

    rng = random.Random(seed)
    comp_records = [record for record in records if has_comp(record)]
    no_comp_records = [record for record in records if not has_comp(record)]

    comp_train, comp_val, comp_test = split_group(comp_records, train_ratio, val_ratio, rng)
    no_train, no_val, no_test = split_group(no_comp_records, train_ratio, val_ratio, rng)

    train = comp_train + no_train
    val = comp_val + no_val
    test = comp_test + no_test
    rng.shuffle(train)
    rng.shuffle(val)
    rng.shuffle(test)
    return train, val, test


def write_json(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def split_stats(records: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "records": len(records),
        "has_comp": sum(1 for record in records if has_comp(record)),
        "no_comp": sum(1 for record in records if not has_comp(record)),
        "tokens": sum(len(record.get("tokens", [])) for record in records),
        "comp_tokens": sum(
            1
            for record in records
            for tag in record.get("ner_tags", [])
            if tag in ("B-COMP", "I-COMP", 1, 2)
        ),
    }


def overlap_ids(*splits: list[dict[str, Any]]) -> list[str]:
    seen: set[str] = set()
    overlaps: set[str] = set()
    for split in splits:
        for record in split:
            record_id = str(record["id"])
            if record_id in seen:
                overlaps.add(record_id)
            seen.add(record_id)
    return sorted(overlaps)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Split NER JSON dataset into train/val/test.")
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--train-output", default=DEFAULT_TRAIN)
    parser.add_argument("--val-output", default=DEFAULT_VAL)
    parser.add_argument("--test-output", default=DEFAULT_TEST)
    parser.add_argument("--train-ratio", type=float, default=0.8)
    parser.add_argument("--val-ratio", type=float, default=0.1)
    parser.add_argument("--test-ratio", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--summary-output", default=DEFAULT_SUMMARY)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    records = load_dataset(Path(args.input))
    validate_records(records)

    train, val, test = stratified_split(
        records,
        train_ratio=args.train_ratio,
        val_ratio=args.val_ratio,
        test_ratio=args.test_ratio,
        seed=args.seed,
    )

    write_json(train, Path(args.train_output))
    write_json(val, Path(args.val_output))
    write_json(test, Path(args.test_output))

    overlaps = overlap_ids(train, val, test)
    summary = {
        "total": len(records),
        "train": len(train),
        "val": len(val),
        "test": len(test),
        "seed": args.seed,
        "overlap_ids": overlaps,
        "splits": {
            "train": split_stats(train),
            "val": split_stats(val),
            "test": split_stats(test),
        },
    }
    write_json(summary, Path(args.summary_output))

    print(f"Train output  : {args.train_output}")
    print(f"Val output    : {args.val_output}")
    print(f"Test output   : {args.test_output}")
    print(f"Summary output: {args.summary_output}")
    print(f"Total         : {summary['total']}")
    for split_name in ("train", "val", "test"):
        stats = summary["splits"][split_name]
        print(
            f"{split_name}: records={stats['records']} "
            f"has_comp={stats['has_comp']} no_comp={stats['no_comp']} "
            f"tokens={stats['tokens']} comp_tokens={stats['comp_tokens']}"
        )
    print(f"Overlap ids   : {overlaps}")


if __name__ == "__main__":
    main()
