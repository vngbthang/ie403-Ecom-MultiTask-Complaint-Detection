"""
Build a priority review file for the new batch-200 annotations before pilot300 merge.

The script reads repaired annotations plus existing conversion/review reports and
creates Markdown/JSON artifacts grouped by review priority. It does not modify
annotations or BIO labels.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any


DEFAULT_ANNOTATIONS = "data/processed/annotation_batch_200_new_for_pilot300_ai_repaired.jsonl"
DEFAULT_CANDIDATES = "data/processed/annotation_batch_200_new_for_pilot300.jsonl"
DEFAULT_CONVERSION_REPORT = "data/processed/annotation_batch_200_new_for_pilot300_bio_conversion_report.json"
DEFAULT_REVIEW_SUMMARY = "data/processed/annotation_batch_200_new_for_pilot300_review_summary.json"
DEFAULT_REVIEW_MD = "data/processed/annotation_batch_200_new_for_pilot300_review.md"
DEFAULT_JSON_OUTPUT = "data/processed/annotation_batch_200_new_for_pilot300_priority_review.json"
DEFAULT_MD_OUTPUT = "data/processed/annotation_batch_200_new_for_pilot300_priority_review.md"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return data


def load_jsonl_by_id(path: Path) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    with path.open("r", encoding="utf-8-sig") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            if not isinstance(record, dict):
                raise ValueError(f"Expected JSON object at {path}:{line_no}")
            record_id = str(record.get("id", ""))
            if not record_id:
                raise ValueError(f"Missing id at {path}:{line_no}")
            records[record_id] = record
    return records


def span_token_length(span: dict[str, Any]) -> int:
    return len(str(span.get("text", "")).split())


def spans_overlap(a: dict[str, Any], b: dict[str, Any]) -> bool:
    return (
        isinstance(a.get("start"), int)
        and isinstance(a.get("end"), int)
        and isinstance(b.get("start"), int)
        and isinstance(b.get("end"), int)
        and a["start"] < b["end"]
        and b["start"] < a["end"]
    )


def find_overlap_pairs(spans: list[dict[str, Any]]) -> list[dict[str, Any]]:
    pairs: list[dict[str, Any]] = []
    for left_idx in range(len(spans)):
        for right_idx in range(left_idx + 1, len(spans)):
            left = spans[left_idx]
            right = spans[right_idx]
            if not isinstance(left, dict) or not isinstance(right, dict):
                continue
            if spans_overlap(left, right):
                overlap_start = max(left["start"], right["start"])
                overlap_end = min(left["end"], right["end"])
                pairs.append(
                    {
                        "span_a_index": left_idx,
                        "span_b_index": right_idx,
                        "overlap_start": overlap_start,
                        "overlap_end": overlap_end,
                        "span_a_text": left.get("text", ""),
                        "span_b_text": right.get("text", ""),
                    }
                )
    return pairs


def compact_span(span: dict[str, Any], index: int) -> dict[str, Any]:
    return {
        "index": index,
        "start": span.get("start"),
        "end": span.get("end"),
        "label": span.get("label"),
        "text": span.get("text"),
        "token_length": span_token_length(span),
    }


def has_many_sentences_or_commas(span: dict[str, Any]) -> bool:
    text = str(span.get("text", ""))
    sentence_marks = len(re.findall(r"[.!?。]+", text))
    comma_like = len(re.findall(r"[,，;:]+", text))
    return sentence_marks >= 2 or comma_like >= 3


def is_high_priority(review_item: dict[str, Any], record: dict[str, Any]) -> bool:
    warning_reasons = review_item.get("warning_reasons", [])
    text = str(record.get("text", ""))
    spans = record.get("spans", [])
    token_count = int(review_item.get("token_count") or len(text.split()))
    span_count = len(spans) if isinstance(spans, list) else 0

    if any("dài >= 15 tokens" in reason for reason in warning_reasons):
        return True
    if span_count > 4:
        return True
    if span_count > 0 and token_count <= 10:
        return True
    if review_item.get("has_empty_spans") and any(
        keyword in text.lower()
        for keyword in ["lỗi", "không được", "tệ", "thất vọng", "chậm", "lag", "không đúng", "không có", "bị", "lừa đảo"]
    ):
        return True
    if isinstance(spans, list) and any(isinstance(span, dict) and has_many_sentences_or_commas(span) for span in spans):
        return True
    if any("bắt đầu từ đầu text" in reason for reason in warning_reasons) and token_count > 20:
        return True
    if float(review_item.get("comp_ratio") or 0.0) > 0.60 and token_count > 20:
        return True
    return False


def build_overlap_group(
    conversion_report: dict[str, Any],
    annotations_by_id: dict[str, dict[str, Any]],
    candidates_by_id: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    warnings_by_id: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for warning in conversion_report.get("warnings", []):
        if warning.get("warning_type") == "overlapping_spans":
            warnings_by_id[str(warning.get("id", ""))].append(warning)

    group = []
    for record_id in sorted(warnings_by_id):
        record = annotations_by_id.get(record_id, {})
        candidate = candidates_by_id.get(record_id, {})
        spans = record.get("spans", [])
        if not isinstance(spans, list):
            spans = []
        group.append(
            {
                "id": record_id,
                "text": record.get("text") or candidate.get("text", ""),
                "spans": [
                    compact_span(span, index)
                    for index, span in enumerate(spans)
                    if isinstance(span, dict)
                ],
                "overlap_pairs": find_overlap_pairs([span for span in spans if isinstance(span, dict)]),
                "conversion_warnings": warnings_by_id[record_id],
                "suggested_action": "keep longer / keep shorter / split / drop duplicate",
            }
        )
    return group


def build_review_groups(
    review_summary: dict[str, Any],
    annotations_by_id: dict[str, dict[str, Any]],
    candidates_by_id: dict[str, dict[str, Any]],
    must_fix_ids: set[str],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], int]:
    likely_ok_count = int(review_summary.get("summary", {}).get("likely_ok", 0))
    needs_review_items = review_summary.get("needs_review", [])
    high: list[dict[str, Any]] = []
    low: list[dict[str, Any]] = []

    for item in needs_review_items:
        record_id = str(item.get("id", ""))
        if record_id in must_fix_ids:
            continue
        record = annotations_by_id.get(record_id, {})
        candidate = candidates_by_id.get(record_id, {})
        spans = record.get("spans", [])
        if not isinstance(spans, list):
            spans = []

        review_record = {
            "id": record_id,
            "text": record.get("text") or candidate.get("text", ""),
            "spans": [
                compact_span(span, index)
                for index, span in enumerate(spans)
                if isinstance(span, dict)
            ],
            "warning_reasons": item.get("warning_reasons", []),
            "token_count": item.get("token_count"),
            "comp_ratio": item.get("comp_ratio"),
            "span_count": len(spans),
        }
        if is_high_priority(item, record):
            high.append(review_record)
        else:
            low.append(
                {
                    "id": record_id,
                    "warning_reasons": item.get("warning_reasons", []),
                }
            )

    return high, low, likely_ok_count


def truncate(text: str, limit: int = 320) -> str:
    text = str(text).replace("\n", " ")
    return text[:limit] + ("..." if len(text) > limit else "")


def render_span_list(spans: list[dict[str, Any]]) -> list[str]:
    if not spans:
        return ["- _No spans_"]
    lines = []
    for span in spans:
        lines.append(
            f"- #{span['index']} [{span['start']}:{span['end']}] "
            f"{span['label']} ({span['token_length']} tok): `{span['text']}`"
        )
    return lines


def render_markdown(payload: dict[str, Any]) -> str:
    summary = payload["summary"]
    lines: list[str] = [
        "# Priority Annotation Review - Batch 200 for Pilot300",
        "",
        "## Summary",
        "",
        f"- Total records: `{summary['total_records']}`",
        f"- MUST_FIX_OVERLAP records: `{summary['must_fix_overlap_count']}`",
        f"- NEEDS_REVIEW_HIGH records: `{summary['needs_review_high_count']}`",
        f"- NEEDS_REVIEW_LOW records: `{summary['needs_review_low_count']}`",
        f"- LIKELY_OK records: `{summary['likely_ok_count']}`",
        f"- Recommended action: {summary['recommended_action']}",
        "",
        "## A. MUST_FIX_OVERLAP",
        "",
    ]

    if not payload["must_fix_overlap"]:
        lines.append("_None_")
    for record in payload["must_fix_overlap"]:
        lines.extend(
            [
                f"### {record['id']}",
                "",
                f"Text: {truncate(record['text'])}",
                "",
                "Current spans:",
                *render_span_list(record["spans"]),
                "",
                "Overlap pairs:",
            ]
        )
        if record["overlap_pairs"]:
            for pair in record["overlap_pairs"]:
                lines.append(
                    f"- span #{pair['span_a_index']} overlaps span #{pair['span_b_index']} "
                    f"at [{pair['overlap_start']}:{pair['overlap_end']}]"
                )
        else:
            for warning in record["conversion_warnings"]:
                lines.append(
                    f"- warning span_index={warning.get('span_index')}: "
                    f"{warning.get('message')}"
                )
        lines.extend(
            [
                "",
                f"Suggested action: `{record['suggested_action']}`",
                "",
                "Human action: KEEP_LONGER / KEEP_SHORTER / SPLIT / DROP_DUPLICATE / OTHER",
                "Notes:",
                "",
            ]
        )

    lines.extend(["", "## B. NEEDS_REVIEW_HIGH", ""])
    if not payload["needs_review_high"]:
        lines.append("_None_")
    for record in payload["needs_review_high"]:
        lines.extend(
            [
                f"### {record['id']}",
                "",
                f"Text: {truncate(record['text'])}",
                "",
                "Warning reasons:",
                *[f"- {reason}" for reason in record["warning_reasons"]],
                "",
                "Current spans:",
                *render_span_list(record["spans"]),
                "",
                "Human action: KEEP / FIX / DROP",
                "Suggested fixed spans:",
                "Notes:",
                "",
            ]
        )

    lines.extend(["", "## C. NEEDS_REVIEW_LOW", ""])
    if payload["needs_review_low"]:
        lines.extend(["| id | warning reasons |", "|---|---|"])
        for record in payload["needs_review_low"]:
            reasons = "<br>".join(record.get("warning_reasons", []))
            lines.append(f"| `{record['id']}` | {reasons} |")
    else:
        lines.append("_None_")

    lines.extend(
        [
            "",
            "## D. LIKELY_OK",
            "",
            f"- Count: `{summary['likely_ok_count']}`",
            "- Details omitted by design.",
            "",
        ]
    )
    return "\n".join(lines)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build prioritized annotation review for batch 200.")
    parser.add_argument("--annotations", default=DEFAULT_ANNOTATIONS)
    parser.add_argument("--candidates", default=DEFAULT_CANDIDATES)
    parser.add_argument("--conversion-report", default=DEFAULT_CONVERSION_REPORT)
    parser.add_argument("--review-summary", default=DEFAULT_REVIEW_SUMMARY)
    parser.add_argument("--review-md", default=DEFAULT_REVIEW_MD)
    parser.add_argument("--json-output", default=DEFAULT_JSON_OUTPUT)
    parser.add_argument("--md-output", default=DEFAULT_MD_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    annotations_by_id = load_jsonl_by_id(Path(args.annotations))
    candidates_by_id = load_jsonl_by_id(Path(args.candidates))
    conversion_report = load_json(Path(args.conversion_report))
    review_summary = load_json(Path(args.review_summary))

    must_fix = build_overlap_group(conversion_report, annotations_by_id, candidates_by_id)
    must_fix_ids = {record["id"] for record in must_fix}
    high, low, likely_ok_count = build_review_groups(
        review_summary,
        annotations_by_id,
        candidates_by_id,
        must_fix_ids=must_fix_ids,
    )

    total_records = int(review_summary.get("summary", {}).get("total_records", len(annotations_by_id)))
    summary = {
        "total_records": total_records,
        "must_fix_overlap_count": len(must_fix),
        "needs_review_high_count": len(high),
        "needs_review_low_count": len(low),
        "likely_ok_count": likely_ok_count,
        "recommended_action": (
            "Fix MUST_FIX_OVERLAP first, then review NEEDS_REVIEW_HIGH. "
            "NEEDS_REVIEW_LOW can be spot-checked before merge."
        ),
        "must_fix_overlap_ids": [record["id"] for record in must_fix],
        "needs_review_high_ids": [record["id"] for record in high],
        "needs_review_low_ids": [record["id"] for record in low],
    }
    payload = {
        "inputs": {
            "annotations": args.annotations,
            "candidates": args.candidates,
            "conversion_report": args.conversion_report,
            "review_summary": args.review_summary,
            "review_md": args.review_md,
        },
        "summary": summary,
        "must_fix_overlap": must_fix,
        "needs_review_high": high,
        "needs_review_low": low,
        "likely_ok": {"count": likely_ok_count},
    }

    json_output = Path(args.json_output)
    md_output = Path(args.md_output)
    write_json(json_output, payload)
    md_output.parent.mkdir(parents=True, exist_ok=True)
    md_output.write_text(render_markdown(payload), encoding="utf-8")

    print(f"Priority JSON    : {json_output}")
    print(f"Priority Markdown: {md_output}")
    print(f"Total records    : {summary['total_records']}")
    print(f"MUST_FIX_OVERLAP : {summary['must_fix_overlap_count']}")
    print(f"NEEDS_REVIEW_HIGH: {summary['needs_review_high_count']}")
    print(f"NEEDS_REVIEW_LOW : {summary['needs_review_low_count']}")
    print(f"LIKELY_OK        : {summary['likely_ok_count']}")
    print(f"MUST_FIX ids     : {', '.join(summary['must_fix_overlap_ids'])}")
    print(f"HIGH ids         : {', '.join(summary['needs_review_high_ids'])}")


if __name__ == "__main__":
    main()
