"""
Repair span start/end offsets by re-locating span text in the original record text.

This script does not change span text, labels, reasons, add spans, or remove spans.
It only updates start/end when a deterministic substring match is found.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DEFAULT_INPUT = "data/processed/annotation_sample_train_20_ai.jsonl"
DEFAULT_OUTPUT = "data/processed/annotation_sample_train_20_ai_repaired.jsonl"
DEFAULT_REPORT = "data/processed/annotation_sample_train_20_offset_repair_report.json"


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


def write_jsonl(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def find_all(text: str, needle: str) -> list[int]:
    if not needle:
        return []

    positions: list[int] = []
    start = 0
    while True:
        pos = text.find(needle, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    return positions


def choose_position(positions: list[int], old_start: Any) -> tuple[int, bool]:
    ambiguous = len(positions) > 1
    if not ambiguous:
        return positions[0], False

    if isinstance(old_start, int):
        return min(positions, key=lambda pos: abs(pos - old_start)), True
    return positions[0], True


def is_current_span_valid(text: str, span: dict[str, Any]) -> bool:
    start = span.get("start")
    end = span.get("end")
    span_text = span.get("text")

    if not isinstance(start, int) or not isinstance(end, int):
        return False
    if not isinstance(span_text, str):
        return False
    if not (0 <= start < end <= len(text)):
        return False
    return text[start:end] == span_text


def repair_one_span(record_id: str, text: str, span: dict[str, Any], strict: bool) -> dict[str, Any]:
    old_start = span.get("start")
    old_end = span.get("end")
    span_text = span.get("text")

    detail = {
        "id": record_id,
        "span_text": span_text,
        "old_start": old_start,
        "old_end": old_end,
        "new_start": old_start,
        "new_end": old_end,
        "status": "unresolved",
        "message": "",
    }

    if not isinstance(span, dict):
        detail["message"] = "Span is not an object."
        return detail

    if is_current_span_valid(text, span):
        detail["status"] = "already_valid"
        detail["message"] = "Current offsets are valid."
        return detail

    if not isinstance(span_text, str) or not span_text:
        detail["message"] = "Span text is missing or empty."
        return detail

    positions = find_all(text, span_text)
    used_fallback = False
    matched_text = span_text

    if not positions:
        stripped = span_text.strip()
        if stripped and stripped != span_text:
            positions = find_all(text, stripped)
            used_fallback = bool(positions)
            matched_text = stripped if used_fallback else span_text

    if not positions:
        detail["message"] = "Exact substring not found in record text."
        return detail

    new_start, ambiguous = choose_position(positions, old_start)
    new_end = new_start + len(matched_text)

    span["start"] = new_start
    span["end"] = new_end

    detail["new_start"] = new_start
    detail["new_end"] = new_end
    if ambiguous:
        detail["status"] = "ambiguous_repaired"
        detail["message"] = (
            "Multiple matches found; chose nearest old start."
            if isinstance(old_start, int)
            else "Multiple matches found; chose first match."
        )
    else:
        detail["status"] = "repaired"
        detail["message"] = "Offsets repaired from substring search."

    if used_fallback:
        detail["message"] += " Used stripped span text for search."
        if strict:
            detail["status"] = "unresolved"
            detail["message"] += " Strict mode treats fallback repair as unresolved."

    return detail


def repair_records(records: list[dict[str, Any]], strict: bool) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    details: list[dict[str, Any]] = []
    summary = {
        "records": len(records),
        "spans_total": 0,
        "spans_already_valid": 0,
        "spans_repaired": 0,
        "spans_unresolved": 0,
        "ambiguous_matches": 0,
    }

    for record in records:
        record_id = str(record.get("id", ""))
        text = record.get("text", "")
        spans = record.get("spans", [])

        if not isinstance(text, str) or not isinstance(spans, list):
            continue

        for span in spans:
            summary["spans_total"] += 1
            detail = repair_one_span(record_id, text, span, strict=strict)
            details.append(detail)

            status = detail["status"]
            if status == "already_valid":
                summary["spans_already_valid"] += 1
            elif status == "repaired":
                summary["spans_repaired"] += 1
            elif status == "ambiguous_repaired":
                summary["spans_repaired"] += 1
                summary["ambiguous_matches"] += 1
            else:
                summary["spans_unresolved"] += 1

    return records, {"summary": summary, "details": details}


def write_report(report: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Repair AI annotation span offsets using exact substring search."
    )
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--report-out", default=DEFAULT_REPORT)
    parser.add_argument("--strict", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)
    report_path = Path(args.report_out)

    records = load_jsonl(input_path)
    repaired_records, report = repair_records(records, strict=args.strict)
    write_jsonl(repaired_records, output_path)
    write_report(report, report_path)

    summary = report["summary"]
    print(f"Input path             : {input_path}")
    print(f"Output path            : {output_path}")
    print(f"Report path            : {report_path}")
    print(f"Records                : {summary['records']}")
    print(f"Spans total            : {summary['spans_total']}")
    print(f"Spans already valid    : {summary['spans_already_valid']}")
    print(f"Spans repaired         : {summary['spans_repaired']}")
    print(f"Spans unresolved       : {summary['spans_unresolved']}")
    print(f"Ambiguous matches      : {summary['ambiguous_matches']}")


if __name__ == "__main__":
    main()
