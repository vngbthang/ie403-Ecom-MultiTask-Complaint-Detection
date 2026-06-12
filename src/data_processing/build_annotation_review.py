"""
Build a Markdown review file for manual quality checking of BIO annotations.

This script only reads annotations and writes a review document.
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


DEFAULT_INPUT = "data/processed/annotation_sample_train_20_bio.jsonl"
DEFAULT_OUTPUT = "data/processed/annotation_sample_train_20_review.md"


def load_jsonl(path: Path, max_records: int | None = None) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            if max_records is not None and len(records) >= max_records:
                break
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


def escape_md_cell(value: Any) -> str:
    text = str(value)
    return text.replace("|", "\\|").replace("\n", " ")


def count_span_tokens(span_text: str) -> int:
    return len(str(span_text).split())


def heuristic_warnings(record: dict[str, Any]) -> list[str]:
    warnings: list[str] = []
    spans = record.get("spans", [])
    tokens = record.get("tokens", [])
    tags = record.get("ner_tags", [])
    meta = record.get("meta", {})
    cls_label = meta.get("cls_label") if isinstance(meta, dict) else None

    if isinstance(spans, list):
        for idx, span in enumerate(spans):
            if not isinstance(span, dict):
                continue
            span_text = str(span.get("text", ""))
            span_token_len = count_span_tokens(span_text)
            if span_token_len >= 15:
                warnings.append(
                    f"span #{idx} quá dài ({span_token_len} tokens >= 15)"
                )

            start = span.get("start")
            if start == 0 and span_token_len > 8:
                warnings.append(
                    f"span #{idx} bắt đầu từ token đầu/text đầu và dài hơn 8 tokens"
                )

        if len(spans) > 4:
            warnings.append(f"record có nhiều hơn 4 spans ({len(spans)} spans)")

        if len(spans) == 0 and int(cls_label or 0) == 1:
            warnings.append("spans=[] nhưng cls_label=1")

    if tokens and tags and len(tokens) == len(tags):
        comp_count = sum(1 for tag in tags if tag in ("B-COMP", "I-COMP"))
        comp_ratio = comp_count / len(tokens) if tokens else 0.0
        if comp_ratio > 0.60:
            warnings.append(f"tỉ lệ COMP token > 60% ({comp_ratio:.1%})")

    return warnings


def render_record(record: dict[str, Any], index: int) -> tuple[str, list[str]]:
    record_id = record.get("id", "")
    meta = record.get("meta", {})
    if not isinstance(meta, dict):
        meta = {}
    domain = meta.get("domain", "")
    split = meta.get("split", "")
    text = record.get("text", "")
    spans = record.get("spans", [])
    reason = record.get("reason", "")
    tokens = record.get("tokens", [])
    tags = record.get("ner_tags", [])
    warnings = heuristic_warnings(record)

    lines: list[str] = []
    lines.append(f"## {index}. `{record_id}`")
    lines.append("")
    lines.append(f"- Domain: `{domain}`")
    lines.append(f"- Split: `{split}`")
    lines.append("")
    lines.append("**Text gốc:**")
    lines.append("")
    lines.append(f"> {text}")
    lines.append("")
    lines.append("**Spans:**")
    lines.append("")

    if isinstance(spans, list) and spans:
        for span_idx, span in enumerate(spans):
            if not isinstance(span, dict):
                lines.append(f"- Span #{span_idx}: invalid span object")
                continue
            lines.append(
                "- "
                f"#{span_idx} "
                f"[{span.get('start')}:{span.get('end')}] "
                f"`{span.get('text', '')}` "
                f"label=`{span.get('label', '')}`"
            )
    else:
        lines.append("- None")

    lines.append("")
    lines.append(f"**Reason:** {reason}")
    lines.append("")
    lines.append("**Token/BIO:**")
    lines.append("")
    lines.append("| idx | token | tag |")
    lines.append("|---:|---|---|")
    for idx, (token, tag) in enumerate(zip(tokens, tags)):
        lines.append(f"| {idx} | {escape_md_cell(token)} | `{escape_md_cell(tag)}` |")

    lines.append("")
    lines.append("**Heuristic warnings:**")
    lines.append("")
    if warnings:
        for warning in warnings:
            lines.append(f"- {warning}")
    else:
        lines.append("- None")

    lines.append("")
    lines.append("**Human review:** OK / NEED_FIX / DROP")
    lines.append("")
    lines.append("**Notes:**")
    lines.append("")
    lines.append("---")
    lines.append("")

    return "\n".join(lines), warnings


def build_review(records: list[dict[str, Any]]) -> tuple[str, list[str]]:
    warning_ids: list[str] = []
    sections: list[str] = [
        "# Annotation Review - Sample Train 20",
        "",
        "Manual checklist for reviewing AI-assisted complaint span annotations.",
        "",
    ]

    for idx, record in enumerate(records, start=1):
        section, warnings = render_record(record, idx)
        if warnings:
            warning_ids.append(str(record.get("id", "")))
        sections.append(section)

    return "\n".join(sections), warning_ids


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a Markdown manual review file for BIO annotations."
    )
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--max-records", type=int, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)
    records = load_jsonl(input_path, max_records=args.max_records)
    content, warning_ids = build_review(records)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")

    print(f"Output path                    : {output_path}")
    print(f"Records                        : {len(records)}")
    print(f"Records with heuristic warnings: {len(warning_ids)}")
    if warning_ids:
        print(f"Warning ids                    : {', '.join(warning_ids)}")


if __name__ == "__main__":
    main()
