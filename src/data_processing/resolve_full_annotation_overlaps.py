"""
Resolve overlapping COMP spans in processed full annotation batches.

For each batch in the full annotation manifest, this script reads the repaired
annotations, merges overlapping spans per record, validates the no-overlap
annotations, then converts them to BIO/NER artifacts.

It does not merge with pilot100/batch200 and does not modify source files.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from src.data_processing.convert_spans_to_bio import convert_spans_to_bio
from src.data_processing.validate_span_annotations import validate_annotations


DEFAULT_MANIFEST = "data/processed/full_annotation_batches/full_annotation_batches_manifest.json"
DEFAULT_SUMMARY_JSON = "data/processed/full_annotation_batches/full_annotation_overlap_resolve_summary.json"
DEFAULT_SUMMARY_MD = "data/processed/full_annotation_batches/full_annotation_overlap_resolve_summary.md"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return data


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


def write_jsonl(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def batch_paths(input_jsonl: Path) -> dict[str, Path]:
    stem = input_jsonl.stem
    parent = input_jsonl.parent
    return {
        "source": input_jsonl,
        "repaired": parent / f"{stem}_ai_repaired.jsonl",
        "old_conversion_report": parent / f"{stem}_bio_conversion_report.json",
        "no_overlap": parent / f"{stem}_ai_repaired_no_overlap.jsonl",
        "overlap_report": parent / f"{stem}_overlap_resolve_report.json",
        "validation_report": parent / f"{stem}_validation_report_no_overlap.json",
        "bio": parent / f"{stem}_bio_no_overlap.jsonl",
        "ner": parent / f"{stem}_ner_no_overlap.json",
        "bio_report": parent / f"{stem}_bio_conversion_report_no_overlap.json",
    }


def span_is_valid(span: Any) -> bool:
    return (
        isinstance(span, dict)
        and isinstance(span.get("start"), int)
        and isinstance(span.get("end"), int)
        and isinstance(span.get("text"), str)
        and span.get("label") == "COMP"
    )


def whitespace_token_offsets(text: str) -> list[tuple[int, int]]:
    return [(match.start(), match.end()) for match in re.finditer(r"\S+", text)]


def token_indices_for_span(span: dict[str, Any], token_offsets: list[tuple[int, int]]) -> set[int]:
    start = span["start"]
    end = span["end"]
    return {
        idx
        for idx, (token_start, token_end) in enumerate(token_offsets)
        if token_start < end and start < token_end
    }


def merge_spans_for_record(record: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    record_id = str(record.get("id", ""))
    text = record.get("text", "")
    spans = record.get("spans", [])
    if not isinstance(text, str) or not isinstance(spans, list):
        return record, {
            "id": record_id,
            "changed": False,
            "spans_before": 0,
            "spans_after": 0,
            "overlap_groups": [],
        }

    valid_spans = [span for span in spans if span_is_valid(span)]
    invalid_spans = [span for span in spans if not span_is_valid(span)]
    sorted_spans = sorted(valid_spans, key=lambda span: (span["start"], span["end"]))
    token_offsets = whitespace_token_offsets(text)
    merged: list[dict[str, Any]] = []
    groups: list[dict[str, Any]] = []
    current_group: list[dict[str, Any]] = []
    current_group_token_indices: set[int] = set()

    def flush_group(group: list[dict[str, Any]]) -> dict[str, Any]:
        start = min(span["start"] for span in group)
        end = max(span["end"] for span in group)
        return {
            "start": start,
            "end": end,
            "text": text[start:end],
            "label": "COMP",
        }

    for span in sorted_spans:
        span_token_indices = token_indices_for_span(span, token_offsets)
        if not current_group:
            current_group = [span]
            current_group_token_indices = set(span_token_indices)
            continue

        current_end = max(item["end"] for item in current_group)
        if span["start"] < current_end or bool(current_group_token_indices & span_token_indices):
            current_group.append(span)
            current_group_token_indices.update(span_token_indices)
        else:
            merged_span = flush_group(current_group)
            merged.append(merged_span)
            if len(current_group) > 1:
                groups.append(
                    {
                        "source_spans": current_group,
                        "merged_span": merged_span,
                    }
                )
            current_group = [span]
            current_group_token_indices = set(span_token_indices)

    if current_group:
        merged_span = flush_group(current_group)
        merged.append(merged_span)
        if len(current_group) > 1:
            groups.append(
                {
                    "source_spans": current_group,
                    "merged_span": merged_span,
                }
            )

    changed = bool(groups)
    new_record = dict(record)
    if changed:
        # Keep invalid spans untouched if any exist; validation will catch them.
        new_record["spans"] = sorted(merged + invalid_spans, key=lambda span: (span.get("start", 10**12), span.get("end", 10**12)))

    return new_record, {
        "id": record_id,
        "changed": changed,
        "spans_before": len(spans),
        "spans_after": len(new_record.get("spans", spans)),
        "overlap_groups": groups,
    }


def read_conversion_warning_count(path: Path, warning_type: str | None = None) -> int:
    if not path.exists():
        return 0
    report = load_json(path)
    warnings = report.get("warnings", [])
    if not isinstance(warnings, list):
        return 0
    if warning_type is None:
        return len(warnings)
    return sum(1 for warning in warnings if isinstance(warning, dict) and warning.get("warning_type") == warning_type)


def validate_ner_json(path: Path) -> list[str]:
    records = []
    with path.open("r", encoding="utf-8-sig") as f:
        data = json.load(f)
    if not isinstance(data, list):
        return [f"{path}: NER JSON is not a list"]
    errors: list[str] = []
    seen: set[str] = set()
    for idx, record in enumerate(data):
        if not isinstance(record, dict):
            errors.append(f"{path}: record #{idx} is not an object")
            continue
        record_id = str(record.get("id", ""))
        if not record_id:
            errors.append(f"{path}: record #{idx} missing id")
        if record_id in seen:
            errors.append(f"{path}: duplicate id {record_id}")
        seen.add(record_id)
        tokens = record.get("tokens")
        tags = record.get("ner_tags")
        if not isinstance(tokens, list) or not isinstance(tags, list):
            errors.append(f"{path}: {record_id} tokens/ner_tags must be lists")
            continue
        if len(tokens) != len(tags):
            errors.append(f"{path}: {record_id} len(tokens) != len(ner_tags)")
        invalid = sorted(set(tags) - {"O", "B-COMP", "I-COMP"})
        if invalid:
            errors.append(f"{path}: {record_id} invalid labels {invalid}")
    return errors


def process_batch(batch: dict[str, Any]) -> dict[str, Any]:
    batch_id = str(batch["batch_id"])
    input_jsonl = Path(batch["input_jsonl"])
    paths = batch_paths(input_jsonl)
    result: dict[str, Any] = {
        "batch_id": batch_id,
        "status": "pending",
        "input_jsonl": str(paths["source"]),
        "annotations_input": str(paths["repaired"]),
        "annotations_no_overlap": str(paths["no_overlap"]),
        "overlap_report": str(paths["overlap_report"]),
        "validation_report": str(paths["validation_report"]),
        "bio_output": str(paths["bio"]),
        "ner_output": str(paths["ner"]),
        "bio_conversion_report": str(paths["bio_report"]),
        "records": 0,
        "records_with_overlap_before": 0,
        "spans_before": 0,
        "spans_after": 0,
        "merged_overlap_groups": 0,
        "changed_record_ids": [],
        "overlap_warnings_before": read_conversion_warning_count(paths["old_conversion_report"], "overlapping_spans"),
        "overlap_warnings_after": 0,
        "conversion_warnings_after": 0,
        "validation_pass": False,
        "error": None,
    }

    if not paths["repaired"].exists():
        result["status"] = "missing_repaired_annotations"
        result["error"] = f"Missing repaired annotations: {paths['repaired']}"
        return result

    try:
        annotations = load_jsonl(paths["repaired"])
        fixed_records: list[dict[str, Any]] = []
        details: list[dict[str, Any]] = []
        for record in annotations:
            fixed_record, detail = merge_spans_for_record(record)
            fixed_records.append(fixed_record)
            details.append(detail)

        changed_ids = [detail["id"] for detail in details if detail["changed"]]
        report = {
            "batch_id": batch_id,
            "records": len(annotations),
            "records_with_overlap_before": len(changed_ids),
            "spans_before": sum(int(detail["spans_before"]) for detail in details),
            "spans_after": sum(int(detail["spans_after"]) for detail in details),
            "merged_overlap_groups": sum(len(detail["overlap_groups"]) for detail in details),
            "changed_record_ids": changed_ids,
            "details": [detail for detail in details if detail["changed"]],
        }
        write_jsonl(fixed_records, paths["no_overlap"])
        write_json(paths["overlap_report"], report)

        result.update(
            {
                "records": report["records"],
                "records_with_overlap_before": report["records_with_overlap_before"],
                "spans_before": report["spans_before"],
                "spans_after": report["spans_after"],
                "merged_overlap_groups": report["merged_overlap_groups"],
                "changed_record_ids": changed_ids,
            }
        )
    except Exception as exc:
        result["status"] = "overlap_resolve_failed"
        result["error"] = str(exc)
        return result

    try:
        exit_code = validate_annotations(
            input_candidates=paths["source"],
            annotations=paths["no_overlap"],
            report_out=paths["validation_report"],
            allow_missing=False,
        )
        validation_report = load_json(paths["validation_report"])
        result["validation_summary"] = validation_report.get("summary", {})
        if exit_code != 0:
            result["status"] = "validation_failed"
            return result
        result["validation_pass"] = True
    except Exception as exc:
        result["status"] = "validation_failed"
        result["error"] = str(exc)
        return result

    try:
        _, conversion_report = convert_spans_to_bio(
            annotations_path=paths["no_overlap"],
            candidates_path=paths["source"],
            bio_output_path=paths["bio"],
            ner_output_path=paths["ner"],
            report_path=paths["bio_report"],
            token_source="whitespace",
        )
        warnings = conversion_report.get("warnings", [])
        warning_counts = Counter(
            warning.get("warning_type", "unknown")
            for warning in warnings
            if isinstance(warning, dict)
        )
        result["conversion_summary"] = conversion_report.get("summary", {})
        result["conversion_warning_counts"] = dict(sorted(warning_counts.items()))
        result["conversion_warnings_after"] = int(result["conversion_summary"].get("warnings", 0))
        result["overlap_warnings_after"] = int(warning_counts.get("overlapping_spans", 0))

        ner_errors = validate_ner_json(paths["ner"])
        if ner_errors:
            result["status"] = "ner_validation_failed"
            result["error"] = "; ".join(ner_errors[:5])
            return result

        result["status"] = "processed"
    except Exception as exc:
        result["status"] = "conversion_failed"
        result["error"] = str(exc)

    return result


def build_summary(batch_results: list[dict[str, Any]]) -> dict[str, Any]:
    validation_failed = [
        result
        for result in batch_results
        if not result.get("validation_pass")
    ]
    processed = [result for result in batch_results if result["status"] == "processed"]
    total_conversion_warnings_after = sum(int(result.get("conversion_warnings_after", 0)) for result in batch_results)
    total_overlap_warnings_after = sum(int(result.get("overlap_warnings_after", 0)) for result in batch_results)
    return {
        "total_batches": len(batch_results),
        "processed_batches": len(processed),
        "validation_passed_batches": sum(1 for result in batch_results if result.get("validation_pass")),
        "validation_failed_batches": len(validation_failed),
        "total_records": sum(int(result.get("records", 0)) for result in batch_results),
        "total_spans_before": sum(int(result.get("spans_before", 0)) for result in batch_results),
        "total_spans_after": sum(int(result.get("spans_after", 0)) for result in batch_results),
        "total_overlap_warnings_before": sum(int(result.get("overlap_warnings_before", 0)) for result in batch_results),
        "total_overlap_warnings_after": total_overlap_warnings_after,
        "total_conversion_warnings_after": total_conversion_warnings_after,
        "total_changed_records": sum(len(result.get("changed_record_ids", [])) for result in batch_results),
        "changed_record_ids_by_batch": {
            result["batch_id"]: result.get("changed_record_ids", [])
            for result in batch_results
            if result.get("changed_record_ids")
        },
        "validation_pass": len(validation_failed) == 0,
        "conversion_warnings_pass": total_conversion_warnings_after == 0,
        "overlapping_spans_pass": total_overlap_warnings_after == 0,
        "failed_batches": [
            {
                "batch_id": result["batch_id"],
                "status": result["status"],
                "error": result.get("error"),
            }
            for result in batch_results
            if result["status"] != "processed"
        ],
    }


def render_markdown(summary: dict[str, Any], batch_results: list[dict[str, Any]]) -> str:
    lines = [
        "# Full Annotation Overlap Resolve Summary",
        "",
        "## Global Summary",
        "",
        f"- Total batches: `{summary['total_batches']}`",
        f"- Processed batches: `{summary['processed_batches']}`",
        f"- Validation passed batches: `{summary['validation_passed_batches']}`",
        f"- Validation failed batches: `{summary['validation_failed_batches']}`",
        f"- Total records: `{summary['total_records']}`",
        f"- Total spans before: `{summary['total_spans_before']}`",
        f"- Total spans after: `{summary['total_spans_after']}`",
        f"- Overlap warnings before: `{summary['total_overlap_warnings_before']}`",
        f"- Overlap warnings after: `{summary['total_overlap_warnings_after']}`",
        f"- Conversion warnings after: `{summary['total_conversion_warnings_after']}`",
        f"- Changed records: `{summary['total_changed_records']}`",
        f"- Validation pass: `{summary['validation_pass']}`",
        f"- Conversion warnings pass: `{summary['conversion_warnings_pass']}`",
        f"- Overlapping spans pass: `{summary['overlapping_spans_pass']}`",
        "",
        "## Batch Details",
        "",
        "| batch | status | records | changed records | spans before | spans after | overlap before | overlap after | conversion warnings after |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for result in batch_results:
        lines.append(
            f"| {result['batch_id']} | {result['status']} | "
            f"{result.get('records', 0)} | "
            f"{len(result.get('changed_record_ids', []))} | "
            f"{result.get('spans_before', 0)} | "
            f"{result.get('spans_after', 0)} | "
            f"{result.get('overlap_warnings_before', 0)} | "
            f"{result.get('overlap_warnings_after', 0)} | "
            f"{result.get('conversion_warnings_after', 0)} |"
        )

    lines.extend(["", "## Changed Record IDs By Batch", ""])
    if summary["changed_record_ids_by_batch"]:
        for batch_id, ids in summary["changed_record_ids_by_batch"].items():
            lines.append(f"- `{batch_id}`: {', '.join(ids)}")
    else:
        lines.append("_None_")

    if summary["failed_batches"]:
        lines.extend(["", "## Failed Batches", ""])
        for item in summary["failed_batches"]:
            lines.append(f"- `{item['batch_id']}`: {item['status']} - {item.get('error')}")

    lines.append("")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Resolve overlapping spans in full annotation batches.")
    parser.add_argument("--manifest", default=DEFAULT_MANIFEST)
    parser.add_argument("--summary-json", default=DEFAULT_SUMMARY_JSON)
    parser.add_argument("--summary-md", default=DEFAULT_SUMMARY_MD)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    manifest = load_json(Path(args.manifest))
    batches = manifest.get("batches", [])
    if not isinstance(batches, list):
        raise ValueError("Manifest field 'batches' must be a list")

    batch_results: list[dict[str, Any]] = []
    for batch in batches:
        print(f"\n[RESOLVE] {batch['batch_id']}")
        result = process_batch(batch)
        batch_results.append(result)
        print(f"  status                  : {result['status']}")
        print(f"  records                 : {result.get('records', 0)}")
        print(f"  changed records          : {len(result.get('changed_record_ids', []))}")
        print(f"  spans before/after       : {result.get('spans_before', 0)} / {result.get('spans_after', 0)}")
        print(f"  overlap warnings before  : {result.get('overlap_warnings_before', 0)}")
        print(f"  overlap warnings after   : {result.get('overlap_warnings_after', 0)}")
        print(f"  conversion warnings after: {result.get('conversion_warnings_after', 0)}")
        if result.get("error"):
            print(f"  error                   : {result['error']}")

    summary = build_summary(batch_results)
    payload = {
        "summary": summary,
        "batches": batch_results,
    }
    summary_json = Path(args.summary_json)
    summary_md = Path(args.summary_md)
    write_json(summary_json, payload)
    summary_md.parent.mkdir(parents=True, exist_ok=True)
    summary_md.write_text(render_markdown(summary, batch_results), encoding="utf-8")

    print("\n" + "=" * 72)
    print("Full annotation overlap resolve summary")
    print("=" * 72)
    print(f"Summary JSON                     : {summary_json}")
    print(f"Summary Markdown                 : {summary_md}")
    print(f"Total batches                    : {summary['total_batches']}")
    print(f"Processed batches                : {summary['processed_batches']}")
    print(f"Validation passed batches        : {summary['validation_passed_batches']}")
    print(f"Validation failed batches        : {summary['validation_failed_batches']}")
    print(f"Total records                    : {summary['total_records']}")
    print(f"Total spans before               : {summary['total_spans_before']}")
    print(f"Total spans after                : {summary['total_spans_after']}")
    print(f"Total overlap warnings before    : {summary['total_overlap_warnings_before']}")
    print(f"Total overlap warnings after     : {summary['total_overlap_warnings_after']}")
    print(f"Total conversion warnings after  : {summary['total_conversion_warnings_after']}")
    print(f"Total changed records            : {summary['total_changed_records']}")
    print(f"Validation pass                  : {summary['validation_pass']}")
    print(f"Conversion warnings pass         : {summary['conversion_warnings_pass']}")
    print(f"Overlapping spans pass           : {summary['overlapping_spans_pass']}")


if __name__ == "__main__":
    main()
