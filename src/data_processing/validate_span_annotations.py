"""
Validate AI-assisted complaint span annotation JSONL output.

Default candidates:
    data/processed/annotation_sample_train_20.jsonl

Default annotations:
    data/processed/annotation_sample_train_20_ai.jsonl
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


REQUIRED_RECORD_FIELDS = ("id", "text", "spans", "reason")
REQUIRED_SPAN_FIELDS = ("start", "end", "text", "label")
VALID_LABELS = {"COMP"}


def load_candidates(path: Path) -> dict[str, dict[str, Any]]:
    candidates: dict[str, dict[str, Any]] = {}
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            record_id = str(record.get("id", ""))
            if record_id:
                candidates[record_id] = record
    return candidates


def add_error(
    errors: list[dict[str, Any]],
    line: int | None,
    record_id: str | None,
    error_type: str,
    message: str,
) -> None:
    errors.append(
        {
            "line": line,
            "id": record_id,
            "error_type": error_type,
            "message": message,
        }
    )


def validate_span(
    span: Any,
    text: str,
    line_no: int,
    record_id: str,
    span_index: int,
    errors: list[dict[str, Any]],
) -> None:
    if not isinstance(span, dict):
        add_error(
            errors,
            line_no,
            record_id,
            "invalid_span_type",
            f"Span #{span_index} must be an object.",
        )
        return

    for field in REQUIRED_SPAN_FIELDS:
        if field not in span:
            add_error(
                errors,
                line_no,
                record_id,
                "missing_span_field",
                f"Span #{span_index} is missing field: {field}",
            )

    if not all(field in span for field in REQUIRED_SPAN_FIELDS):
        return

    start = span["start"]
    end = span["end"]
    span_text = span["text"]
    label = span["label"]

    if not isinstance(start, int) or not isinstance(end, int):
        add_error(
            errors,
            line_no,
            record_id,
            "invalid_offset_type",
            f"Span #{span_index} start/end must be integers.",
        )
        return

    if not (0 <= start < end <= len(text)):
        add_error(
            errors,
            line_no,
            record_id,
            "invalid_offset_range",
            f"Span #{span_index} offsets out of range: start={start}, end={end}, len={len(text)}.",
        )
        return

    expected_text = text[start:end]
    if span_text != expected_text:
        add_error(
            errors,
            line_no,
            record_id,
            "span_text_mismatch",
            f"Span #{span_index} text mismatch: expected {expected_text!r}, got {span_text!r}.",
        )

    if label not in VALID_LABELS:
        add_error(
            errors,
            line_no,
            record_id,
            "invalid_label",
            f"Span #{span_index} label must be 'COMP', got {label!r}.",
        )


def validate_record(
    record: Any,
    line_no: int,
    candidates: dict[str, dict[str, Any]],
    seen_ids: set[str],
    duplicate_ids: set[str],
    errors: list[dict[str, Any]],
) -> bool:
    before_error_count = len(errors)

    if not isinstance(record, dict):
        add_error(errors, line_no, None, "invalid_record_type", "Record must be a JSON object.")
        return False

    record_id = str(record.get("id", "")) if "id" in record else None

    for field in REQUIRED_RECORD_FIELDS:
        if field not in record:
            add_error(
                errors,
                line_no,
                record_id,
                "missing_record_field",
                f"Record is missing field: {field}",
            )

    if not all(field in record for field in REQUIRED_RECORD_FIELDS):
        return False

    record_id = str(record["id"])
    text = record["text"]
    spans = record["spans"]
    reason = record["reason"]

    if record_id in seen_ids:
        duplicate_ids.add(record_id)
        add_error(
            errors,
            line_no,
            record_id,
            "duplicate_id",
            f"Duplicate annotation id: {record_id}",
        )
    seen_ids.add(record_id)

    if record_id not in candidates:
        add_error(
            errors,
            line_no,
            record_id,
            "unknown_id",
            f"Annotation id does not exist in input candidates: {record_id}",
        )
    else:
        candidate_text = candidates[record_id].get("text")
        if text != candidate_text:
            add_error(
                errors,
                line_no,
                record_id,
                "text_mismatch",
                "Annotation text does not match candidate text for the same id.",
            )

    if not isinstance(text, str):
        add_error(errors, line_no, record_id, "invalid_text_type", "Field text must be a string.")
        return False

    if not isinstance(spans, list):
        add_error(errors, line_no, record_id, "invalid_spans_type", "Field spans must be a list.")
        return False

    if not isinstance(reason, str) or not reason.strip():
        add_error(errors, line_no, record_id, "empty_reason", "Field reason must be a non-empty string.")

    for span_index, span in enumerate(spans):
        validate_span(span, text, line_no, record_id, span_index, errors)

    return len(errors) == before_error_count


def validate_annotations(
    input_candidates: Path,
    annotations: Path,
    report_out: Path,
    allow_missing: bool,
) -> int:
    if not input_candidates.exists():
        print(f"Input candidates file not found: {input_candidates}")
        return 2

    if not annotations.exists():
        print(
            "Annotation file not found. Please create it by running AI annotation first.\n"
            f"Expected path: {annotations}"
        )
        return 2

    candidates = load_candidates(input_candidates)
    errors: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    duplicate_ids: set[str] = set()
    total_annotation_records = 0
    valid_records = 0

    with open(annotations, encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            total_annotation_records += 1
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                add_error(
                    errors,
                    line_no,
                    None,
                    "invalid_json",
                    f"Invalid JSON: {exc}",
                )
                continue

            if validate_record(record, line_no, candidates, seen_ids, duplicate_ids, errors):
                valid_records += 1

    candidate_ids = set(candidates)
    missing_ids = sorted(candidate_ids - seen_ids)
    if missing_ids and not allow_missing:
        for missing_id in missing_ids:
            add_error(
                errors,
                None,
                missing_id,
                "missing_id",
                f"Candidate id is missing from annotations: {missing_id}",
            )

    error_counts = Counter(error["error_type"] for error in errors)
    invalid_records = total_annotation_records - valid_records

    summary = {
        "total_input_candidates": len(candidates),
        "total_annotation_records": total_annotation_records,
        "valid_records": valid_records,
        "invalid_records": invalid_records,
        "missing_ids": len(missing_ids),
        "duplicate_ids": len(duplicate_ids),
        "allow_missing": allow_missing,
        "error_counts": dict(sorted(error_counts.items())),
    }

    report = {
        "summary": summary,
        "errors": errors,
    }
    report_out.parent.mkdir(parents=True, exist_ok=True)
    with open(report_out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print("Validation summary")
    print(f"  Total input candidates    : {summary['total_input_candidates']}")
    print(f"  Total annotation records  : {summary['total_annotation_records']}")
    print(f"  Valid records             : {summary['valid_records']}")
    print(f"  Invalid records           : {summary['invalid_records']}")
    print(f"  Missing ids               : {summary['missing_ids']}")
    print(f"  Duplicate ids             : {summary['duplicate_ids']}")
    print(f"  Report                    : {report_out}")
    if error_counts:
        print("  Errors by type:")
        for error_type, count in sorted(error_counts.items()):
            print(f"    {error_type}: {count}")
    else:
        print("  Errors by type            : none")

    return 0 if not errors else 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate AI-assisted complaint span annotation JSONL output."
    )
    parser.add_argument(
        "--input-candidates",
        default="data/processed/annotation_sample_train_20.jsonl",
        help="Input candidates JSONL used for AI annotation",
    )
    parser.add_argument(
        "--annotations",
        default="data/processed/annotation_sample_train_20_ai.jsonl",
        help="AI annotation output JSONL to validate",
    )
    parser.add_argument(
        "--report-out",
        default="data/processed/annotation_sample_train_20_validation_report.json",
        help="Validation report JSON path",
    )
    parser.add_argument(
        "--allow-missing",
        action="store_true",
        help="Allow annotations to contain only a subset of input candidate ids",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    exit_code = validate_annotations(
        input_candidates=Path(args.input_candidates),
        annotations=Path(args.annotations),
        report_out=Path(args.report_out),
        allow_missing=args.allow_missing,
    )
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
