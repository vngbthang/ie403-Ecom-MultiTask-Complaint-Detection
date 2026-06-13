"""
Merge UIT-ViOCD pilot100 and fixed batch200 into pilot300 NER artifacts.

This script validates annotations, BIO and NER records, writes merged pilot300
files, and creates a reproducible train/val/test split. It does not modify the
source pilot100 or batch200 files.
"""

from __future__ import annotations

import argparse
import json
import random
from collections import Counter
from pathlib import Path
from typing import Any


DEFAULT_PILOT100_ANN = "data/processed/uit_viocd_pilot_100_annotations.jsonl"
DEFAULT_BATCH200_ANN = "data/processed/annotation_batch_200_new_for_pilot300_ai_repaired_fixed.jsonl"
DEFAULT_PILOT100_BIO = "data/processed/uit_viocd_pilot_100_bio.jsonl"
DEFAULT_BATCH200_BIO = "data/processed/annotation_batch_200_new_for_pilot300_bio_fixed.jsonl"
DEFAULT_PILOT100_NER = "data/processed/uit_viocd_pilot_100_ner.json"
DEFAULT_BATCH200_NER = "data/processed/annotation_batch_200_new_for_pilot300_ner_fixed.json"

DEFAULT_OUT_ANN = "data/processed/uit_viocd_pilot_300_annotations.jsonl"
DEFAULT_OUT_BIO = "data/processed/uit_viocd_pilot_300_bio.jsonl"
DEFAULT_OUT_NER = "data/processed/uit_viocd_pilot_300_ner.json"
DEFAULT_OUT_SUMMARY = "data/processed/uit_viocd_pilot_300_summary.json"
DEFAULT_OUT_TRAIN = "data/processed/uit_viocd_pilot_300_ner_train.json"
DEFAULT_OUT_VAL = "data/processed/uit_viocd_pilot_300_ner_val.json"
DEFAULT_OUT_TEST = "data/processed/uit_viocd_pilot_300_ner_test.json"
DEFAULT_OUT_SPLIT_SUMMARY = "data/processed/uit_viocd_pilot_300_ner_split_summary.json"

VALID_LABELS = {"O", "B-COMP", "I-COMP"}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8-sig") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            if not isinstance(record, dict):
                raise ValueError(f"Expected JSON object at {path}:{line_no}")
            records.append(record)
    return records


def load_json_list(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig") as f:
        records = json.load(f)
    if not isinstance(records, list):
        raise ValueError(f"Expected JSON list: {path}")
    if not all(isinstance(record, dict) for record in records):
        raise ValueError(f"Expected all records to be objects: {path}")
    return records


def write_jsonl(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def write_json(records: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def duplicate_count(records: list[dict[str, Any]]) -> int:
    ids = [str(record.get("id", "")) for record in records]
    return len(ids) - len(set(ids))


def spans_overlap(a: dict[str, Any], b: dict[str, Any]) -> bool:
    return a["start"] < b["end"] and b["start"] < a["end"]


def validate_annotations(records: list[dict[str, Any]], expected_total: int) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    if len(records) != expected_total:
        errors.append(f"Expected {expected_total} annotation records, found {len(records)}")

    for idx, record in enumerate(records):
        record_id = str(record.get("id", ""))
        if not record_id:
            errors.append(f"Annotation #{idx} missing id")
            continue
        if record_id in seen:
            errors.append(f"Duplicate annotation id: {record_id}")
        seen.add(record_id)

        text = record.get("text")
        spans = record.get("spans", record.get("label", []))
        if not isinstance(text, str) or not text:
            errors.append(f"{record_id}: missing/non-string text")
        if not isinstance(spans, list):
            errors.append(f"{record_id}: spans/label is not a list")
            continue

        valid_spans: list[dict[str, Any]] = []
        for span_idx, span in enumerate(spans):
            if not isinstance(span, dict):
                errors.append(f"{record_id}: span #{span_idx} is not an object")
                continue
            for field in ("start", "end", "text", "label"):
                if field not in span:
                    errors.append(f"{record_id}: span #{span_idx} missing {field}")
            start = span.get("start")
            end = span.get("end")
            span_text = span.get("text")
            label = span.get("label")
            if not isinstance(start, int) or not isinstance(end, int):
                errors.append(f"{record_id}: span #{span_idx} start/end must be int")
                continue
            if not isinstance(span_text, str):
                errors.append(f"{record_id}: span #{span_idx} text must be string")
                continue
            if label != "COMP":
                errors.append(f"{record_id}: span #{span_idx} invalid label {label!r}")
            if not (0 <= start < end <= len(text)):
                errors.append(f"{record_id}: span #{span_idx} invalid offset range")
                continue
            if text[start:end] != span_text:
                errors.append(f"{record_id}: span #{span_idx} text mismatch")
            valid_spans.append(span)

        for left_idx in range(len(valid_spans)):
            for right_idx in range(left_idx + 1, len(valid_spans)):
                if spans_overlap(valid_spans[left_idx], valid_spans[right_idx]):
                    errors.append(f"{record_id}: span #{left_idx} overlaps span #{right_idx}")

    return errors


def validate_ner_records(records: list[dict[str, Any]], expected_total: int) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    if len(records) != expected_total:
        errors.append(f"Expected {expected_total} NER records, found {len(records)}")
    for idx, record in enumerate(records):
        record_id = str(record.get("id", ""))
        if not record_id:
            errors.append(f"NER record #{idx} missing id")
            continue
        if record_id in seen:
            errors.append(f"Duplicate NER id: {record_id}")
        seen.add(record_id)
        tokens = record.get("tokens")
        tags = record.get("ner_tags")
        if not isinstance(tokens, list) or not isinstance(tags, list):
            errors.append(f"{record_id}: tokens/ner_tags must be lists")
            continue
        if len(tokens) != len(tags):
            errors.append(f"{record_id}: len(tokens) != len(ner_tags)")
        unknown = sorted(set(tags) - VALID_LABELS)
        if unknown:
            errors.append(f"{record_id}: invalid labels {unknown}")
    return errors


def validate_bio_records(records: list[dict[str, Any]], expected_total: int) -> list[str]:
    errors = validate_ner_records(records, expected_total=expected_total)
    for idx, record in enumerate(records):
        record_id = str(record.get("id", f"#{idx}"))
        if "text" not in record:
            errors.append(f"{record_id}: BIO record missing text")
        if "spans" not in record:
            errors.append(f"{record_id}: BIO record missing spans")
    return errors


def has_comp(record: dict[str, Any]) -> bool:
    return any(tag in ("B-COMP", "I-COMP") for tag in record.get("ner_tags", []))


def split_group(
    records: list[dict[str, Any]],
    train_ratio: float,
    val_ratio: float,
    rng: random.Random,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    shuffled = list(records)
    rng.shuffle(shuffled)
    total = len(shuffled)
    n_train = int(total * train_ratio)
    n_val = int(total * val_ratio)
    return shuffled[:n_train], shuffled[n_train : n_train + n_val], shuffled[n_train + n_val :]


def stratified_split(
    records: list[dict[str, Any]],
    train_ratio: float,
    val_ratio: float,
    test_ratio: float,
    seed: int,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    if abs((train_ratio + val_ratio + test_ratio) - 1.0) > 1e-6:
        raise ValueError("Split ratios must sum to 1.0")
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
            if tag in ("B-COMP", "I-COMP")
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


def build_summary(
    annotations: list[dict[str, Any]],
    bio_records: list[dict[str, Any]],
    ner_records: list[dict[str, Any]],
    duplicate_ids: int,
    validation_pass: bool,
) -> dict[str, Any]:
    label_counts = Counter(
        tag
        for record in ner_records
        for tag in record.get("ner_tags", [])
    )
    total_tokens = sum(label_counts.values())
    comp_tokens = label_counts["B-COMP"] + label_counts["I-COMP"]
    domain_counter = Counter()
    for record in bio_records:
        meta = record.get("meta", {})
        domain = meta.get("domain", "") if isinstance(meta, dict) else ""
        domain_counter[str(domain)] += 1

    records_with_spans = sum(1 for record in annotations if record.get("spans"))

    return {
        "dataset": "UIT-ViOCD",
        "subset": "pilot_300_train_complaint_reviews",
        "total_records": len(annotations),
        "source_pilot100_records": 100,
        "source_batch200_records": 200,
        "records_with_spans": records_with_spans,
        "records_without_spans": len(annotations) - records_with_spans,
        "total_tokens": total_tokens,
        "O_count": label_counts["O"],
        "B-COMP_count": label_counts["B-COMP"],
        "I-COMP_count": label_counts["I-COMP"],
        "COMP_token_count": comp_tokens,
        "COMP_token_ratio": comp_tokens / total_tokens if total_tokens else 0.0,
        "domain_distribution": dict(sorted(domain_counter.items())),
        "duplicate_ids_count": duplicate_ids,
        "validation_pass": validation_pass,
        "notes": [
            "Only UIT-ViOCD data is used.",
            "Shopee/rating mapping is not used.",
            "Pilot300 is built by merging pilot100 with fixed batch200 annotations.",
        ],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Merge pilot100 and fixed batch200 into pilot300.")
    parser.add_argument("--pilot100-annotations", default=DEFAULT_PILOT100_ANN)
    parser.add_argument("--batch200-annotations", default=DEFAULT_BATCH200_ANN)
    parser.add_argument("--pilot100-bio", default=DEFAULT_PILOT100_BIO)
    parser.add_argument("--batch200-bio", default=DEFAULT_BATCH200_BIO)
    parser.add_argument("--pilot100-ner", default=DEFAULT_PILOT100_NER)
    parser.add_argument("--batch200-ner", default=DEFAULT_BATCH200_NER)
    parser.add_argument("--annotations-output", default=DEFAULT_OUT_ANN)
    parser.add_argument("--bio-output", default=DEFAULT_OUT_BIO)
    parser.add_argument("--ner-output", default=DEFAULT_OUT_NER)
    parser.add_argument("--summary-output", default=DEFAULT_OUT_SUMMARY)
    parser.add_argument("--train-output", default=DEFAULT_OUT_TRAIN)
    parser.add_argument("--val-output", default=DEFAULT_OUT_VAL)
    parser.add_argument("--test-output", default=DEFAULT_OUT_TEST)
    parser.add_argument("--split-summary-output", default=DEFAULT_OUT_SPLIT_SUMMARY)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--train-ratio", type=float, default=0.8)
    parser.add_argument("--val-ratio", type=float, default=0.1)
    parser.add_argument("--test-ratio", type=float, default=0.1)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pilot100_annotations = load_jsonl(Path(args.pilot100_annotations))
    batch200_annotations = load_jsonl(Path(args.batch200_annotations))
    pilot100_bio = load_jsonl(Path(args.pilot100_bio))
    batch200_bio = load_jsonl(Path(args.batch200_bio))
    pilot100_ner = load_json_list(Path(args.pilot100_ner))
    batch200_ner = load_json_list(Path(args.batch200_ner))

    annotations = pilot100_annotations + batch200_annotations
    bio_records = pilot100_bio + batch200_bio
    ner_records = pilot100_ner + batch200_ner

    duplicate_ids = (
        duplicate_count(annotations)
        + duplicate_count(bio_records)
        + duplicate_count(ner_records)
    )
    errors = []
    errors.extend(validate_annotations(annotations, expected_total=300))
    errors.extend(validate_bio_records(bio_records, expected_total=300))
    errors.extend(validate_ner_records(ner_records, expected_total=300))
    validation_pass = not errors
    if errors:
        print("Validation failed:")
        for error in errors[:50]:
            print(f"- {error}")
        if len(errors) > 50:
            print(f"... and {len(errors) - 50} more errors")
        raise SystemExit(1)

    write_jsonl(annotations, Path(args.annotations_output))
    write_jsonl(bio_records, Path(args.bio_output))
    write_json(ner_records, Path(args.ner_output))

    summary = build_summary(
        annotations=annotations,
        bio_records=bio_records,
        ner_records=ner_records,
        duplicate_ids=duplicate_ids,
        validation_pass=validation_pass,
    )
    write_json(summary, Path(args.summary_output))

    train, val, test = stratified_split(
        ner_records,
        train_ratio=args.train_ratio,
        val_ratio=args.val_ratio,
        test_ratio=args.test_ratio,
        seed=args.seed,
    )
    write_json(train, Path(args.train_output))
    write_json(val, Path(args.val_output))
    write_json(test, Path(args.test_output))
    split_summary = {
        "total": len(ner_records),
        "train": len(train),
        "val": len(val),
        "test": len(test),
        "seed": args.seed,
        "overlap_ids": overlap_ids(train, val, test),
        "splits": {
            "train": split_stats(train),
            "val": split_stats(val),
            "test": split_stats(test),
        },
    }
    write_json(split_summary, Path(args.split_summary_output))

    print(f"Annotations output : {args.annotations_output}")
    print(f"BIO output         : {args.bio_output}")
    print(f"NER output         : {args.ner_output}")
    print(f"Summary output     : {args.summary_output}")
    print(f"Train output       : {args.train_output}")
    print(f"Val output         : {args.val_output}")
    print(f"Test output        : {args.test_output}")
    print(f"Split summary      : {args.split_summary_output}")
    print(f"Validation pass    : {validation_pass}")
    print(f"Duplicate ids count: {duplicate_ids}")
    print(f"Total records      : {summary['total_records']}")
    print(f"Records w spans    : {summary['records_with_spans']}")
    print(f"Records no spans   : {summary['records_without_spans']}")
    print(f"Total tokens       : {summary['total_tokens']}")
    print(f"COMP tokens        : {summary['COMP_token_count']}")
    print(f"COMP ratio         : {summary['COMP_token_ratio']:.4f}")
    print("Domain distribution:")
    for domain, count in summary["domain_distribution"].items():
        print(f"  {domain}: {count}")
    for split_name in ("train", "val", "test"):
        stats = split_summary["splits"][split_name]
        print(
            f"{split_name}: records={stats['records']} "
            f"has_comp={stats['has_comp']} no_comp={stats['no_comp']} "
            f"tokens={stats['tokens']} comp_tokens={stats['comp_tokens']}"
        )
    print(f"Split overlap ids  : {split_summary['overlap_ids']}")


if __name__ == "__main__":
    main()
