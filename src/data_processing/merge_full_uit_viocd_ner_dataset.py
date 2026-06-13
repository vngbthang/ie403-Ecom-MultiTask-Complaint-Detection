"""
Merge all UIT-ViOCD complaint span annotations into the full NER dataset.

Sources:
    - pilot100 final artifacts
    - batch200 fixed artifacts
    - remaining full annotation batches no-overlap artifacts

The script validates annotation/BIO/NER consistency, writes merged full
artifacts, and creates a reproducible train/val/test split. It does not modify
source files and does not train any model.
"""

from __future__ import annotations

import argparse
import glob
import json
import random
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


DEFAULT_PILOT100_ANN = "data/processed/uit_viocd_pilot_100_annotations.jsonl"
DEFAULT_BATCH200_ANN = "data/processed/annotation_batch_200_new_for_pilot300_ai_repaired_fixed.jsonl"
DEFAULT_PILOT100_BIO = "data/processed/uit_viocd_pilot_100_bio.jsonl"
DEFAULT_BATCH200_BIO = "data/processed/annotation_batch_200_new_for_pilot300_bio_fixed.jsonl"
DEFAULT_PILOT100_NER = "data/processed/uit_viocd_pilot_100_ner.json"
DEFAULT_BATCH200_NER = "data/processed/annotation_batch_200_new_for_pilot300_ner_fixed.json"
DEFAULT_BATCH_DIR = "data/processed/full_annotation_batches"
DEFAULT_MANIFEST = "data/processed/full_annotation_batches/full_annotation_batches_manifest.json"

DEFAULT_OUT_ANN = "data/processed/uit_viocd_full_complaint_annotations.jsonl"
DEFAULT_OUT_BIO = "data/processed/uit_viocd_full_complaint_bio.jsonl"
DEFAULT_OUT_NER = "data/processed/uit_viocd_full_complaint_ner.json"
DEFAULT_OUT_SUMMARY_JSON = "data/processed/uit_viocd_full_complaint_summary.json"
DEFAULT_OUT_SUMMARY_MD = "data/processed/uit_viocd_full_complaint_summary.md"
DEFAULT_OUT_TRAIN = "data/processed/uit_viocd_full_complaint_ner_train.json"
DEFAULT_OUT_VAL = "data/processed/uit_viocd_full_complaint_ner_val.json"
DEFAULT_OUT_TEST = "data/processed/uit_viocd_full_complaint_ner_test.json"
DEFAULT_OUT_SPLIT_SUMMARY = "data/processed/uit_viocd_full_complaint_ner_split_summary.json"

EXPECTED_TOTAL = 2854
VALID_NER_LABELS = {"O", "B-COMP", "I-COMP"}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8-sig") as f:
        return json.load(f)


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
    data = load_json(path)
    if not isinstance(data, list):
        raise ValueError(f"Expected JSON list: {path}")
    if not all(isinstance(record, dict) for record in data):
        raise ValueError(f"Expected all records to be objects: {path}")
    return data


def write_jsonl(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def id_list(records: list[dict[str, Any]]) -> list[str]:
    return [str(record.get("id", "")) for record in records]


def duplicate_count(records: list[dict[str, Any]]) -> int:
    ids = id_list(records)
    return len(ids) - len(set(ids))


def spans_overlap(a: dict[str, Any], b: dict[str, Any]) -> bool:
    return a["start"] < b["end"] and b["start"] < a["end"]


def get_annotation_spans(record: dict[str, Any]) -> list[Any]:
    spans = record.get("spans", record.get("label", []))
    return spans if isinstance(spans, list) else []


def validate_annotations(records: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    if len(records) != EXPECTED_TOTAL:
        errors.append(f"Expected {EXPECTED_TOTAL} annotation records, found {len(records)}")

    for idx, record in enumerate(records):
        record_id = str(record.get("id", ""))
        if not record_id:
            errors.append(f"Annotation #{idx} missing id")
            continue
        if record_id in seen:
            errors.append(f"Duplicate annotation id: {record_id}")
        seen.add(record_id)

        text = record.get("text")
        if not isinstance(text, str):
            errors.append(f"{record_id}: text must be string")
            continue

        valid_spans = []
        for span_idx, span in enumerate(get_annotation_spans(record)):
            if not isinstance(span, dict):
                errors.append(f"{record_id}: span #{span_idx} is not object")
                continue
            start = span.get("start")
            end = span.get("end")
            span_text = span.get("text")
            label = span.get("label")
            if label != "COMP":
                errors.append(f"{record_id}: span #{span_idx} label != COMP")
            if not isinstance(start, int) or not isinstance(end, int):
                errors.append(f"{record_id}: span #{span_idx} start/end not int")
                continue
            if not (0 <= start < end <= len(text)):
                errors.append(f"{record_id}: span #{span_idx} invalid offset")
                continue
            if isinstance(span_text, str) and text[start:end] != span_text:
                errors.append(f"{record_id}: span #{span_idx} text mismatch")
            valid_spans.append(span)

        for left_idx in range(len(valid_spans)):
            for right_idx in range(left_idx + 1, len(valid_spans)):
                if spans_overlap(valid_spans[left_idx], valid_spans[right_idx]):
                    errors.append(f"{record_id}: span #{left_idx} overlaps span #{right_idx}")
    return errors


def validate_ner(records: list[dict[str, Any]], expected_total: int, label: str) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    if len(records) != expected_total:
        errors.append(f"{label}: expected {expected_total} records, found {len(records)}")

    for idx, record in enumerate(records):
        record_id = str(record.get("id", ""))
        if not record_id:
            errors.append(f"{label}: record #{idx} missing id")
            continue
        if record_id in seen:
            errors.append(f"{label}: duplicate id {record_id}")
        seen.add(record_id)
        tokens = record.get("tokens")
        tags = record.get("ner_tags")
        if not isinstance(tokens, list) or not isinstance(tags, list):
            errors.append(f"{label}: {record_id} tokens/ner_tags must be lists")
            continue
        if len(tokens) != len(tags):
            errors.append(f"{label}: {record_id} len(tokens) != len(ner_tags)")
        invalid = sorted(set(tags) - VALID_NER_LABELS)
        if invalid:
            errors.append(f"{label}: {record_id} invalid labels {invalid}")
    return errors


def validate_bio(records: list[dict[str, Any]]) -> list[str]:
    errors = validate_ner(records, EXPECTED_TOTAL, "BIO")
    for idx, record in enumerate(records):
        record_id = str(record.get("id", f"#{idx}"))
        if "text" not in record:
            errors.append(f"BIO: {record_id} missing text")
        if "spans" not in record:
            errors.append(f"BIO: {record_id} missing spans")
    return errors


def read_remaining_paths_from_manifest(manifest_path: Path, batch_dir: Path) -> tuple[list[Path], list[Path], list[Path]]:
    if manifest_path.exists():
        manifest = load_json(manifest_path)
        batch_items = manifest.get("batches", [])
        ann_paths = []
        bio_paths = []
        ner_paths = []
        for item in batch_items:
            input_path = Path(item["input_jsonl"])
            if not input_path.is_absolute():
                input_path = Path(input_path)
            stem = input_path.stem
            parent = input_path.parent
            ann_paths.append(parent / f"{stem}_ai_repaired_no_overlap.jsonl")
            bio_paths.append(parent / f"{stem}_bio_no_overlap.jsonl")
            ner_paths.append(parent / f"{stem}_ner_no_overlap.json")
        return ann_paths, bio_paths, ner_paths

    ann_paths = sorted(Path(path) for path in glob.glob(str(batch_dir / "full_annotation_batch_*_ai_repaired_no_overlap.jsonl")))
    bio_paths = sorted(Path(path) for path in glob.glob(str(batch_dir / "full_annotation_batch_*_bio_no_overlap.jsonl")))
    ner_paths = sorted(Path(path) for path in glob.glob(str(batch_dir / "full_annotation_batch_*_ner_no_overlap.json")))
    return ann_paths, bio_paths, ner_paths


def load_many_jsonl(paths: list[Path]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in paths:
        if not path.exists():
            raise FileNotFoundError(f"Missing JSONL source: {path}")
        records.extend(load_jsonl(path))
    return records


def load_many_json_lists(paths: list[Path]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in paths:
        if not path.exists():
            raise FileNotFoundError(f"Missing JSON source: {path}")
        records.extend(load_json_list(path))
    return records


def has_comp(record: dict[str, Any]) -> bool:
    return any(tag in ("B-COMP", "I-COMP") for tag in record.get("ner_tags", []))


def domain_for_id(record_id: str, bio_by_id: dict[str, dict[str, Any]]) -> str:
    meta = bio_by_id.get(record_id, {}).get("meta", {})
    if isinstance(meta, dict):
        return str(meta.get("domain", ""))
    return ""


def split_for_id(record_id: str, bio_by_id: dict[str, dict[str, Any]]) -> str:
    meta = bio_by_id.get(record_id, {}).get("meta", {})
    if isinstance(meta, dict):
        return str(meta.get("split", ""))
    if "_" in record_id:
        return record_id.split("_", 1)[0]
    return ""


def split_group(records: list[dict[str, Any]], train_ratio: float, val_ratio: float, rng: random.Random) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    shuffled = list(records)
    rng.shuffle(shuffled)
    total = len(shuffled)
    n_train = int(total * train_ratio)
    n_val = int(total * val_ratio)
    return shuffled[:n_train], shuffled[n_train : n_train + n_val], shuffled[n_train + n_val :]


def stratified_split(records: list[dict[str, Any]], bio_by_id: dict[str, dict[str, Any]], seed: int, train_ratio: float, val_ratio: float, test_ratio: float) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    if abs((train_ratio + val_ratio + test_ratio) - 1.0) > 1e-6:
        raise ValueError("Split ratios must sum to 1.0")
    groups: dict[tuple[bool, str], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        record_id = str(record["id"])
        groups[(has_comp(record), domain_for_id(record_id, bio_by_id))].append(record)

    rng = random.Random(seed)
    train: list[dict[str, Any]] = []
    val: list[dict[str, Any]] = []
    test: list[dict[str, Any]] = []
    for key in sorted(groups, key=lambda item: (item[0], item[1])):
        group_train, group_val, group_test = split_group(groups[key], train_ratio, val_ratio, rng)
        train.extend(group_train)
        val.extend(group_val)
        test.extend(group_test)
    rng.shuffle(train)
    rng.shuffle(val)
    rng.shuffle(test)
    return train, val, test


def split_stats(records: list[dict[str, Any]], bio_by_id: dict[str, dict[str, Any]]) -> dict[str, Any]:
    label_counts = Counter(tag for record in records for tag in record.get("ner_tags", []))
    domain_counts = Counter(domain_for_id(str(record["id"]), bio_by_id) for record in records)
    split_counts = Counter(split_for_id(str(record["id"]), bio_by_id) for record in records)
    return {
        "records": len(records),
        "has_comp": sum(1 for record in records if has_comp(record)),
        "no_comp": sum(1 for record in records if not has_comp(record)),
        "tokens": sum(len(record.get("tokens", [])) for record in records),
        "O_count": label_counts["O"],
        "B-COMP_count": label_counts["B-COMP"],
        "I-COMP_count": label_counts["I-COMP"],
        "comp_tokens": label_counts["B-COMP"] + label_counts["I-COMP"],
        "domain_distribution": dict(sorted(domain_counts.items())),
        "original_split_distribution": dict(sorted(split_counts.items())),
    }


def overlap_ids(*splits: list[dict[str, Any]]) -> list[str]:
    seen: set[str] = set()
    overlaps: set[str] = set()
    for split_records in splits:
        for record in split_records:
            record_id = str(record["id"])
            if record_id in seen:
                overlaps.add(record_id)
            seen.add(record_id)
    return sorted(overlaps)


def build_summary(
    annotations: list[dict[str, Any]],
    bio_records: list[dict[str, Any]],
    ner_records: list[dict[str, Any]],
    source_counts: dict[str, int],
    duplicate_ids_count: int,
    validation_pass: bool,
) -> dict[str, Any]:
    label_counts = Counter(tag for record in ner_records for tag in record.get("ner_tags", []))
    total_tokens = sum(label_counts.values())
    comp_tokens = label_counts["B-COMP"] + label_counts["I-COMP"]
    total_spans = sum(len(get_annotation_spans(record)) for record in annotations)
    records_with_spans = sum(1 for record in annotations if get_annotation_spans(record))
    domain_counts = Counter()
    split_counts = Counter()
    for record in bio_records:
        meta = record.get("meta", {})
        if isinstance(meta, dict):
            domain_counts[str(meta.get("domain", ""))] += 1
            split_counts[str(meta.get("split", ""))] += 1
    return {
        "dataset": "UIT-ViOCD",
        "subset": "full_complaint_span_ner",
        "total_records": len(annotations),
        "source_counts": source_counts,
        "records_with_spans": records_with_spans,
        "records_without_spans": len(annotations) - records_with_spans,
        "total_tokens": total_tokens,
        "O_count": label_counts["O"],
        "B-COMP_count": label_counts["B-COMP"],
        "I-COMP_count": label_counts["I-COMP"],
        "COMP_token_count": comp_tokens,
        "COMP_token_ratio": comp_tokens / total_tokens if total_tokens else 0.0,
        "total_spans": total_spans,
        "average_spans_per_record": total_spans / len(annotations) if annotations else 0.0,
        "duplicate_ids_count": duplicate_ids_count,
        "validation_pass": validation_pass,
        "domain_distribution": dict(sorted(domain_counts.items())),
        "split_distribution": dict(sorted(split_counts.items())),
        "notes": [
            "Only UIT-ViOCD complaint candidates are included.",
            "Shopee/rating mapping is not used.",
            "Remaining full batches use no-overlap annotations.",
        ],
    }


def render_summary_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# UIT-ViOCD Full Complaint NER Dataset Summary",
        "",
        "## Overview",
        "",
        f"- Total records: `{summary['total_records']}`",
        f"- Validation pass: `{summary['validation_pass']}`",
        f"- Duplicate ids count: `{summary['duplicate_ids_count']}`",
        f"- Records with spans: `{summary['records_with_spans']}`",
        f"- Records without spans: `{summary['records_without_spans']}`",
        f"- Total spans: `{summary['total_spans']}`",
        f"- Average spans per record: `{summary['average_spans_per_record']:.4f}`",
        "",
        "## Source Counts",
        "",
    ]
    for source, count in summary["source_counts"].items():
        lines.append(f"- {source}: `{count}`")
    lines.extend(
        [
            "",
            "## Token / Label Distribution",
            "",
            f"- Total tokens: `{summary['total_tokens']}`",
            f"- O: `{summary['O_count']}`",
            f"- B-COMP: `{summary['B-COMP_count']}`",
            f"- I-COMP: `{summary['I-COMP_count']}`",
            f"- COMP token count: `{summary['COMP_token_count']}`",
            f"- COMP token ratio: `{summary['COMP_token_ratio']:.4%}`",
            "",
            "## Domain Distribution",
            "",
        ]
    )
    for domain, count in summary["domain_distribution"].items():
        lines.append(f"- {domain}: `{count}`")
    lines.extend(["", "## Original Split Distribution", ""])
    for split, count in summary["split_distribution"].items():
        lines.append(f"- {split}: `{count}`")
    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Merge full UIT-ViOCD complaint NER dataset.")
    parser.add_argument("--pilot100-annotations", default=DEFAULT_PILOT100_ANN)
    parser.add_argument("--batch200-annotations", default=DEFAULT_BATCH200_ANN)
    parser.add_argument("--pilot100-bio", default=DEFAULT_PILOT100_BIO)
    parser.add_argument("--batch200-bio", default=DEFAULT_BATCH200_BIO)
    parser.add_argument("--pilot100-ner", default=DEFAULT_PILOT100_NER)
    parser.add_argument("--batch200-ner", default=DEFAULT_BATCH200_NER)
    parser.add_argument("--batch-dir", default=DEFAULT_BATCH_DIR)
    parser.add_argument("--manifest", default=DEFAULT_MANIFEST)
    parser.add_argument("--annotations-output", default=DEFAULT_OUT_ANN)
    parser.add_argument("--bio-output", default=DEFAULT_OUT_BIO)
    parser.add_argument("--ner-output", default=DEFAULT_OUT_NER)
    parser.add_argument("--summary-json", default=DEFAULT_OUT_SUMMARY_JSON)
    parser.add_argument("--summary-md", default=DEFAULT_OUT_SUMMARY_MD)
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
    batch_ann_paths, batch_bio_paths, batch_ner_paths = read_remaining_paths_from_manifest(
        Path(args.manifest),
        Path(args.batch_dir),
    )

    pilot_annotations = load_jsonl(Path(args.pilot100_annotations))
    batch200_annotations = load_jsonl(Path(args.batch200_annotations))
    remaining_annotations = load_many_jsonl(batch_ann_paths)

    pilot_bio = load_jsonl(Path(args.pilot100_bio))
    batch200_bio = load_jsonl(Path(args.batch200_bio))
    remaining_bio = load_many_jsonl(batch_bio_paths)

    pilot_ner = load_json_list(Path(args.pilot100_ner))
    batch200_ner = load_json_list(Path(args.batch200_ner))
    remaining_ner = load_many_json_lists(batch_ner_paths)

    annotations = pilot_annotations + batch200_annotations + remaining_annotations
    bio_records = pilot_bio + batch200_bio + remaining_bio
    ner_records = pilot_ner + batch200_ner + remaining_ner

    duplicate_ids_count = duplicate_count(annotations) + duplicate_count(bio_records) + duplicate_count(ner_records)
    errors: list[str] = []
    errors.extend(validate_annotations(annotations))
    errors.extend(validate_bio(bio_records))
    errors.extend(validate_ner(ner_records, EXPECTED_TOTAL, "NER"))

    annotation_ids = set(id_list(annotations))
    bio_ids = set(id_list(bio_records))
    ner_ids = set(id_list(ner_records))
    if annotation_ids != bio_ids or annotation_ids != ner_ids:
        errors.append(
            "annotation ids, BIO ids, and NER ids differ: "
            f"ann_only={len(annotation_ids - bio_ids - ner_ids)} "
            f"bio_only={len(bio_ids - annotation_ids)} "
            f"ner_only={len(ner_ids - annotation_ids)}"
        )

    validation_pass = not errors
    if errors:
        print("Validation failed:")
        for error in errors[:80]:
            print(f"- {error}")
        if len(errors) > 80:
            print(f"... and {len(errors) - 80} more errors")
        raise SystemExit(1)

    write_jsonl(annotations, Path(args.annotations_output))
    write_jsonl(bio_records, Path(args.bio_output))
    write_json(Path(args.ner_output), ner_records)

    source_counts = {
        "pilot100": len(pilot_annotations),
        "batch200": len(batch200_annotations),
        "remaining_full_batches": len(remaining_annotations),
    }
    summary = build_summary(
        annotations=annotations,
        bio_records=bio_records,
        ner_records=ner_records,
        source_counts=source_counts,
        duplicate_ids_count=duplicate_ids_count,
        validation_pass=validation_pass,
    )
    write_json(Path(args.summary_json), summary)
    Path(args.summary_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.summary_md).write_text(render_summary_markdown(summary), encoding="utf-8")

    bio_by_id = {str(record["id"]): record for record in bio_records}
    train, val, test = stratified_split(
        ner_records,
        bio_by_id=bio_by_id,
        seed=args.seed,
        train_ratio=args.train_ratio,
        val_ratio=args.val_ratio,
        test_ratio=args.test_ratio,
    )
    split_overlaps = overlap_ids(train, val, test)
    if split_overlaps:
        raise RuntimeError(f"Split overlap ids found: {split_overlaps[:20]}")

    write_json(Path(args.train_output), train)
    write_json(Path(args.val_output), val)
    write_json(Path(args.test_output), test)
    split_summary = {
        "total": len(ner_records),
        "train": len(train),
        "val": len(val),
        "test": len(test),
        "seed": args.seed,
        "overlap_ids": split_overlaps,
        "splits": {
            "train": split_stats(train, bio_by_id),
            "val": split_stats(val, bio_by_id),
            "test": split_stats(test, bio_by_id),
        },
    }
    write_json(Path(args.split_summary_output), split_summary)

    print(f"Annotations output : {args.annotations_output}")
    print(f"BIO output         : {args.bio_output}")
    print(f"NER output         : {args.ner_output}")
    print(f"Summary JSON       : {args.summary_json}")
    print(f"Summary Markdown   : {args.summary_md}")
    print(f"Train output       : {args.train_output}")
    print(f"Val output         : {args.val_output}")
    print(f"Test output        : {args.test_output}")
    print(f"Split summary      : {args.split_summary_output}")
    print(f"Validation pass    : {validation_pass}")
    print(f"Total records      : {summary['total_records']}")
    print(f"Duplicate ids      : {summary['duplicate_ids_count']}")
    print(f"Total tokens       : {summary['total_tokens']}")
    print(f"O/B/I              : {summary['O_count']} / {summary['B-COMP_count']} / {summary['I-COMP_count']}")
    print(f"COMP token ratio   : {summary['COMP_token_ratio']:.4f}")
    print(f"Total spans        : {summary['total_spans']}")
    for split_name in ("train", "val", "test"):
        stats = split_summary["splits"][split_name]
        print(
            f"{split_name}: records={stats['records']} has_comp={stats['has_comp']} "
            f"no_comp={stats['no_comp']} tokens={stats['tokens']} comp_tokens={stats['comp_tokens']}"
        )


if __name__ == "__main__":
    main()
