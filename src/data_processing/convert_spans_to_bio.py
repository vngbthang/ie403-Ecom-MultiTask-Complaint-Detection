"""
Convert validated span annotations to BIO labels for NER training.

Default input:
    data/processed/annotation_sample_train_20_ai_repaired.jsonl

Default outputs:
    data/processed/annotation_sample_train_20_bio.jsonl
    data/processed/annotation_sample_train_20_ner.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


DEFAULT_ANNOTATIONS = "data/processed/annotation_sample_train_20_ai_repaired.jsonl"
DEFAULT_CANDIDATES = "data/processed/annotation_sample_train_20.jsonl"
DEFAULT_BIO_OUTPUT = "data/processed/annotation_sample_train_20_bio.jsonl"
DEFAULT_NER_OUTPUT = "data/processed/annotation_sample_train_20_ner.json"
DEFAULT_REPORT = "data/processed/annotation_sample_train_20_bio_conversion_report.json"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON at {path}:{line_no}: {exc}") from exc
            if not isinstance(record, dict):
                raise ValueError(f"Expected JSON object at {path}:{line_no}")
            records.append(record)
    return records


def load_candidate_meta(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}

    meta_by_id: dict[str, dict[str, Any]] = {}
    for record in load_jsonl(path):
        record_id = str(record.get("id", ""))
        if not record_id:
            continue
        meta = record.get("meta")
        if isinstance(meta, dict):
            meta_by_id[record_id] = meta
    return meta_by_id


def whitespace_tokens_with_offsets(text: str) -> list[dict[str, Any]]:
    return [
        {
            "token": match.group(0),
            "start": match.start(),
            "end": match.end(),
        }
        for match in re.finditer(r"\S+", text)
    ]


def spans_overlap(start_a: int, end_a: int, start_b: int, end_b: int) -> bool:
    return start_a < end_b and start_b < end_a


def convert_record_to_bio(
    record: dict[str, Any],
    meta_by_id: dict[str, dict[str, Any]],
    warnings: list[dict[str, Any]],
) -> dict[str, Any]:
    record_id = str(record.get("id", ""))
    text = str(record.get("text", ""))
    spans = record.get("spans", [])
    reason = record.get("reason", "")
    token_offsets = whitespace_tokens_with_offsets(text)
    tokens = [item["token"] for item in token_offsets]
    ner_tags = ["O"] * len(tokens)
    occupied = [False] * len(tokens)

    if not isinstance(spans, list):
        warnings.append(
            {
                "id": record_id,
                "warning_type": "invalid_spans_type",
                "message": "spans is not a list; treated as empty.",
            }
        )
        spans = []

    for span_idx, span in enumerate(spans):
        if not isinstance(span, dict):
            warnings.append(
                {
                    "id": record_id,
                    "warning_type": "invalid_span_type",
                    "span_index": span_idx,
                    "message": "span is not an object; skipped.",
                }
            )
            continue

        if span.get("label") != "COMP":
            warnings.append(
                {
                    "id": record_id,
                    "warning_type": "unsupported_label",
                    "span_index": span_idx,
                    "message": f"Unsupported label {span.get('label')!r}; skipped.",
                }
            )
            continue

        start = span.get("start")
        end = span.get("end")
        if not isinstance(start, int) or not isinstance(end, int):
            warnings.append(
                {
                    "id": record_id,
                    "warning_type": "invalid_offsets",
                    "span_index": span_idx,
                    "message": "start/end are not integers; skipped.",
                }
            )
            continue

        overlapping_indices = [
            idx
            for idx, token in enumerate(token_offsets)
            if spans_overlap(token["start"], token["end"], start, end)
        ]

        if not overlapping_indices:
            warnings.append(
                {
                    "id": record_id,
                    "warning_type": "span_without_token_overlap",
                    "span_index": span_idx,
                    "span_text": span.get("text"),
                    "message": "Span does not overlap any whitespace token.",
                }
            )
            continue

        writable_indices = []
        overlapped_existing = []
        for idx in overlapping_indices:
            if occupied[idx]:
                overlapped_existing.append(idx)
            else:
                writable_indices.append(idx)

        if overlapped_existing:
            warnings.append(
                {
                    "id": record_id,
                    "warning_type": "overlapping_spans",
                    "span_index": span_idx,
                    "span_text": span.get("text"),
                    "message": (
                        "Span overlaps tokens already labeled by an earlier span; "
                        "earlier span labels were kept."
                    ),
                    "overlapped_token_indices": overlapped_existing,
                }
            )

        if not writable_indices:
            continue

        first = True
        for idx in writable_indices:
            ner_tags[idx] = "B-COMP" if first else "I-COMP"
            occupied[idx] = True
            first = False

    meta = dict(meta_by_id.get(record_id, {}))
    if not meta:
        meta = {"source": "UIT-ViOCD", "split": "train", "cls_label": 1}
    else:
        meta.setdefault("source", "UIT-ViOCD")
        meta.setdefault("split", "train")
        meta.setdefault("cls_label", 1)

    return {
        "id": record_id,
        "text": text,
        "tokens": tokens,
        "ner_tags": ner_tags,
        "spans": spans,
        "reason": reason,
        "meta": meta,
    }


def write_jsonl(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def write_json(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def write_report(report: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)


def convert_spans_to_bio(
    annotations_path: Path,
    candidates_path: Path,
    bio_output_path: Path,
    ner_output_path: Path,
    report_path: Path,
    token_source: str,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if token_source != "whitespace":
        raise ValueError("Only --token-source whitespace is currently supported.")

    annotations = load_jsonl(annotations_path)
    meta_by_id = load_candidate_meta(candidates_path)
    warnings: list[dict[str, Any]] = []
    bio_records = [
        convert_record_to_bio(record, meta_by_id=meta_by_id, warnings=warnings)
        for record in annotations
    ]

    ner_records = [
        {
            "id": record["id"],
            "tokens": record["tokens"],
            "ner_tags": record["ner_tags"],
        }
        for record in bio_records
    ]

    tokens_total = sum(len(record["tokens"]) for record in bio_records)
    comp_tokens = sum(
        1
        for record in bio_records
        for tag in record["ner_tags"]
        if tag in ("B-COMP", "I-COMP")
    )
    records_with_spans = sum(1 for record in bio_records if record.get("spans"))
    records_without_spans = len(bio_records) - records_with_spans

    report = {
        "summary": {
            "records": len(bio_records),
            "tokens_total": tokens_total,
            "comp_tokens": comp_tokens,
            "records_with_spans": records_with_spans,
            "records_without_spans": records_without_spans,
            "warnings": len(warnings),
        },
        "warnings": warnings,
    }

    write_jsonl(bio_records, bio_output_path)
    write_json(ner_records, ner_output_path)
    write_report(report, report_path)
    return bio_records, report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert validated COMP spans to whitespace-token BIO labels."
    )
    parser.add_argument("--annotations", default=DEFAULT_ANNOTATIONS)
    parser.add_argument("--bio-output", default=DEFAULT_BIO_OUTPUT)
    parser.add_argument("--ner-output", default=DEFAULT_NER_OUTPUT)
    parser.add_argument("--token-source", default="whitespace", choices=["whitespace"])
    parser.add_argument("--candidates", default=DEFAULT_CANDIDATES)
    parser.add_argument("--report-out", default=DEFAULT_REPORT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    bio_records, report = convert_spans_to_bio(
        annotations_path=Path(args.annotations),
        candidates_path=Path(args.candidates),
        bio_output_path=Path(args.bio_output),
        ner_output_path=Path(args.ner_output),
        report_path=Path(args.report_out),
        token_source=args.token_source,
    )

    bad_lengths = [
        record["id"]
        for record in bio_records
        if len(record["tokens"]) != len(record["ner_tags"])
    ]
    if bad_lengths:
        raise RuntimeError(f"Found records with token/tag length mismatch: {bad_lengths}")

    summary = report["summary"]
    print(f"BIO output       : {args.bio_output}")
    print(f"NER output       : {args.ner_output}")
    print(f"Report output    : {args.report_out}")
    print(f"Records          : {summary['records']}")
    print(f"Tokens total     : {summary['tokens_total']}")
    print(f"COMP tokens      : {summary['comp_tokens']}")
    print(f"Records w spans  : {summary['records_with_spans']}")
    print(f"Records no spans : {summary['records_without_spans']}")
    print(f"Warnings         : {summary['warnings']}")

    print("\nFirst 3 records:")
    for record in bio_records[:3]:
        print(json.dumps(record, ensure_ascii=False))


if __name__ == "__main__":
    main()
