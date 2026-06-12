"""
Summarize heuristic annotation warnings into likely_ok vs needs_review.

This script reads BIO annotations and writes review summary artifacts.
It does not modify annotations or BIO labels.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


DEFAULT_BIO = "data/processed/annotation_sample_train_100_bio_v2.jsonl"
DEFAULT_JSON = "data/processed/annotation_sample_train_100_review_summary_v2.json"
DEFAULT_MD = "data/processed/annotation_sample_train_100_review_summary_v2.md"

COMPLAINT_KEYWORDS = [
    "lỗi",
    "không được",
    "tệ",
    "thất vọng",
    "chậm",
    "lag",
    "không đúng",
    "không có",
    "bị",
    "lừa đảo",
]

NON_COMPLAINT_REASON_KEYWORDS = [
    "góp ý",
    "khen",
    "trung tính",
    "không có cụm khiếu nại",
    "không có complaint",
    "không có khiếu nại",
]


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


def span_token_length(span: dict[str, Any]) -> int:
    return len(str(span.get("text", "")).split())


def record_warning_reasons(record: dict[str, Any]) -> list[str]:
    warnings: list[str] = []
    tokens = record.get("tokens", [])
    tags = record.get("ner_tags", [])
    spans = record.get("spans", [])
    meta = record.get("meta", {})
    cls_label = meta.get("cls_label") if isinstance(meta, dict) else None

    token_count = len(tokens)
    comp_count = sum(1 for tag in tags if tag in ("B-COMP", "I-COMP"))
    comp_ratio = comp_count / token_count if token_count else 0.0

    if isinstance(spans, list):
        for idx, span in enumerate(spans):
            if isinstance(span, dict):
                length = span_token_length(span)
                if length >= 15:
                    warnings.append(f"span #{idx} dài >= 15 tokens ({length})")
                if span.get("start") == 0 and length > 8:
                    warnings.append(f"span #{idx} bắt đầu từ đầu text và dài > 8 tokens")
        if len(spans) > 4:
            warnings.append(f"nhiều hơn 4 spans ({len(spans)})")
        if len(spans) == 0 and int(cls_label or 0) == 1:
            warnings.append("spans=[] nhưng cls_label=1")

    if comp_ratio > 0.60:
        warnings.append(f"COMP ratio > 60% ({comp_ratio:.1%})")

    return warnings


def has_strong_complaint_signal(text: str) -> bool:
    lowered = text.lower()
    return any(keyword in lowered for keyword in COMPLAINT_KEYWORDS)


def reason_says_non_complaint(reason: str) -> bool:
    lowered = reason.lower()
    return any(keyword in lowered for keyword in NON_COMPLAINT_REASON_KEYWORDS)


def classify_record(record: dict[str, Any], warning_reasons: list[str]) -> str:
    if not warning_reasons:
        return "no_warning"

    tokens = record.get("tokens", [])
    tags = record.get("ner_tags", [])
    spans = record.get("spans", [])
    text = str(record.get("text", ""))
    reason = str(record.get("reason", ""))

    token_count = len(tokens)
    comp_count = sum(1 for tag in tags if tag in ("B-COMP", "I-COMP"))
    comp_ratio = comp_count / token_count if token_count else 0.0
    span_lengths = [
        span_token_length(span)
        for span in spans
        if isinstance(span, dict)
    ] if isinstance(spans, list) else []
    max_span_len = max(span_lengths, default=0)
    span_count = len(spans) if isinstance(spans, list) else 0
    has_empty_spans = span_count == 0

    if max_span_len >= 15:
        return "needs_review"
    if span_count > 4:
        return "needs_review"
    if has_empty_spans and has_strong_complaint_signal(text):
        return "needs_review"
    if comp_ratio > 0.60 and token_count > 20:
        return "needs_review"
    if any("bắt đầu từ đầu text" in reason_text for reason_text in warning_reasons) and token_count > 20:
        return "needs_review"

    if token_count <= 10 and comp_ratio > 0.60:
        return "likely_ok"
    if has_empty_spans and reason_says_non_complaint(reason):
        return "likely_ok"
    if span_count > 1 and all(length <= 8 for length in span_lengths):
        return "likely_ok"
    if comp_ratio > 0.60 and token_count <= 20:
        return "likely_ok"

    return "likely_ok"


def summarize_record(record: dict[str, Any]) -> dict[str, Any]:
    tokens = record.get("tokens", [])
    tags = record.get("ner_tags", [])
    spans = record.get("spans", [])
    span_lengths = [
        span_token_length(span)
        for span in spans
        if isinstance(span, dict)
    ] if isinstance(spans, list) else []

    token_count = len(tokens)
    comp_token_count = sum(1 for tag in tags if tag in ("B-COMP", "I-COMP"))
    comp_ratio = comp_token_count / token_count if token_count else 0.0
    warning_reasons = record_warning_reasons(record)
    classification = classify_record(record, warning_reasons)

    return {
        "id": record.get("id"),
        "token_count": token_count,
        "comp_token_count": comp_token_count,
        "comp_ratio": comp_ratio,
        "span_count": len(spans) if isinstance(spans, list) else 0,
        "max_span_token_length": max(span_lengths, default=0),
        "has_empty_spans": len(spans) == 0 if isinstance(spans, list) else True,
        "warning_reasons": warning_reasons,
        "classification": classification,
        "text": record.get("text", ""),
        "spans": [
            {
                "start": span.get("start"),
                "end": span.get("end"),
                "text": span.get("text"),
                "label": span.get("label"),
                "token_length": span_token_length(span),
            }
            for span in spans
            if isinstance(span, dict)
        ] if isinstance(spans, list) else [],
    }


def truncate(text: str, limit: int = 160) -> str:
    text = str(text).replace("\n", " ")
    return text[:limit] + ("..." if len(text) > limit else "")


def render_spans(spans: list[dict[str, Any]]) -> str:
    if not spans:
        return "_None_"
    return "<br>".join(
        f"[{span['start']}:{span['end']}] `{span['text']}` ({span['token_length']} tok)"
        for span in spans
    )


def render_table(records: list[dict[str, Any]], include_text: bool = False) -> list[str]:
    if include_text:
        lines = [
            "| id | tokens | comp_ratio | spans | max_span_len | warnings | text | spans detail |",
            "|---|---:|---:|---:|---:|---|---|---|",
        ]
    else:
        lines = [
            "| id | tokens | comp_ratio | spans | max_span_len | warnings |",
            "|---|---:|---:|---:|---:|---|",
        ]

    for record in records:
        warnings = "<br>".join(record["warning_reasons"]) if record["warning_reasons"] else "_None_"
        base = (
            f"| `{record['id']}` | {record['token_count']} | "
            f"{record['comp_ratio']:.1%} | {record['span_count']} | "
            f"{record['max_span_token_length']} | {warnings}"
        )
        if include_text:
            base += f" | {truncate(record['text'])} | {render_spans(record['spans'])} |"
        else:
            base += " |"
        lines.append(base)
    return lines


def render_markdown(summary: dict[str, Any], likely_ok: list[dict[str, Any]], needs_review: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    lines.append("# Annotation Review Summary V2")
    lines.append("")
    lines.append("## Global Summary")
    lines.append("")
    lines.append(f"- Total records: `{summary['total_records']}`")
    lines.append(f"- Warning records: `{summary['warning_records']}`")
    lines.append(f"- Likely OK: `{summary['likely_ok']}`")
    lines.append(f"- Needs review: `{summary['needs_review']}`")
    lines.append("")

    lines.append("## Likely OK Warning Records")
    lines.append("")
    lines.extend(render_table(likely_ok, include_text=False))
    lines.append("")

    lines.append("## Needs Review Records")
    lines.append("")
    lines.extend(render_table(needs_review, include_text=True))
    lines.append("")
    return "\n".join(lines)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Classify annotation warning records into likely_ok vs needs_review."
    )
    parser.add_argument("--bio", default=DEFAULT_BIO)
    parser.add_argument("--json-output", default=DEFAULT_JSON)
    parser.add_argument("--md-output", default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    records = load_jsonl(Path(args.bio))
    summaries = [summarize_record(record) for record in records]
    warning_records = [record for record in summaries if record["warning_reasons"]]
    likely_ok = [record for record in warning_records if record["classification"] == "likely_ok"]
    needs_review = [record for record in warning_records if record["classification"] == "needs_review"]

    summary = {
        "total_records": len(records),
        "warning_records": len(warning_records),
        "likely_ok": len(likely_ok),
        "needs_review": len(needs_review),
        "needs_review_ids": [record["id"] for record in needs_review],
    }
    payload = {
        "summary": summary,
        "likely_ok": likely_ok,
        "needs_review": needs_review,
    }

    json_output = Path(args.json_output)
    md_output = Path(args.md_output)
    write_json(json_output, payload)
    md_output.parent.mkdir(parents=True, exist_ok=True)
    md_output.write_text(render_markdown(summary, likely_ok, needs_review), encoding="utf-8")

    print(f"JSON output     : {json_output}")
    print(f"Markdown output : {md_output}")
    print(f"Warning records : {summary['warning_records']}")
    print(f"Likely OK       : {summary['likely_ok']}")
    print(f"Needs review    : {summary['needs_review']}")
    if needs_review:
        print(f"Needs review ids: {', '.join(summary['needs_review_ids'])}")


if __name__ == "__main__":
    main()
