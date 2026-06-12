"""
Compare two BIO annotation versions to quantify span shortening.

Default comparison:
    v1: data/processed/annotation_sample_train_20_bio.jsonl
    v2: data/processed/annotation_sample_train_20_bio_v2.jsonl
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


DEFAULT_V1 = "data/processed/annotation_sample_train_20_bio.jsonl"
DEFAULT_V2 = "data/processed/annotation_sample_train_20_bio_v2.jsonl"
DEFAULT_JSON = "data/processed/annotation_sample_train_20_v1_v2_comparison.json"
DEFAULT_MD = "data/processed/annotation_sample_train_20_v1_v2_comparison.md"


def load_jsonl_by_id(path: Path) -> dict[str, dict[str, Any]]:
    records: dict[str, dict[str, Any]] = {}
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON at {path}:{line_no}: {exc}") from exc
            record_id = str(record.get("id", ""))
            if not record_id:
                raise ValueError(f"Missing id at {path}:{line_no}")
            records[record_id] = record
    return records


def count_comp_tokens(record: dict[str, Any]) -> int:
    return sum(1 for tag in record.get("ner_tags", []) if tag in ("B-COMP", "I-COMP"))


def span_token_lengths(record: dict[str, Any]) -> list[int]:
    spans = record.get("spans", [])
    if not isinstance(spans, list):
        return []
    lengths = []
    for span in spans:
        if isinstance(span, dict):
            lengths.append(len(str(span.get("text", "")).split()))
    return lengths


def avg(values: list[float | int]) -> float:
    return float(sum(values) / len(values)) if values else 0.0


def compact_spans(record: dict[str, Any]) -> list[dict[str, Any]]:
    spans = record.get("spans", [])
    if not isinstance(spans, list):
        return []
    compact = []
    for span in spans:
        if not isinstance(span, dict):
            continue
        compact.append(
            {
                "start": span.get("start"),
                "end": span.get("end"),
                "text": span.get("text"),
                "label": span.get("label"),
                "token_length": len(str(span.get("text", "")).split()),
            }
        )
    return compact


def compare_records(v1: dict[str, dict[str, Any]], v2: dict[str, dict[str, Any]]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    ids_v1 = set(v1)
    ids_v2 = set(v2)
    if ids_v1 != ids_v2:
        missing_v2 = sorted(ids_v1 - ids_v2)
        missing_v1 = sorted(ids_v2 - ids_v1)
        raise ValueError(f"ID sets differ. missing in v2={missing_v2}, missing in v1={missing_v1}")

    rows: list[dict[str, Any]] = []
    for record_id in sorted(ids_v1):
        r1 = v1[record_id]
        r2 = v2[record_id]
        tokens_v1 = r1.get("tokens", [])
        tokens_v2 = r2.get("tokens", [])
        if tokens_v1 != tokens_v2:
            raise ValueError(f"Token sequence differs for id={record_id}")

        comp_v1 = count_comp_tokens(r1)
        comp_v2 = count_comp_tokens(r2)
        spans_v1 = compact_spans(r1)
        spans_v2 = compact_spans(r2)
        span_lengths_v1 = [span["token_length"] for span in spans_v1]
        span_lengths_v2 = [span["token_length"] for span in spans_v2]

        rows.append(
            {
                "id": record_id,
                "tokens": len(tokens_v1),
                "comp_tokens_v1": comp_v1,
                "comp_tokens_v2": comp_v2,
                "delta_comp_tokens": comp_v2 - comp_v1,
                "spans_v1_count": len(spans_v1),
                "spans_v2_count": len(spans_v2),
                "avg_span_token_length_v1": avg(span_lengths_v1),
                "avg_span_token_length_v2": avg(span_lengths_v2),
                "text": r1.get("text", ""),
                "spans_v1": spans_v1,
                "spans_v2": spans_v2,
            }
        )

    total_records = len(rows)
    total_tokens = sum(row["tokens"] for row in rows)
    total_comp_v1 = sum(row["comp_tokens_v1"] for row in rows)
    total_comp_v2 = sum(row["comp_tokens_v2"] for row in rows)
    absolute_reduction = total_comp_v1 - total_comp_v2
    percent_reduction = (absolute_reduction / total_comp_v1 * 100) if total_comp_v1 else 0.0

    all_span_lengths_v1 = [
        span["token_length"]
        for row in rows
        for span in row["spans_v1"]
    ]
    all_span_lengths_v2 = [
        span["token_length"]
        for row in rows
        for span in row["spans_v2"]
    ]

    summary = {
        "total_records": total_records,
        "total_tokens": total_tokens,
        "total_comp_tokens_v1": total_comp_v1,
        "total_comp_tokens_v2": total_comp_v2,
        "absolute_reduction": absolute_reduction,
        "percent_reduction": percent_reduction,
        "records_with_reduced_comp_tokens": sum(1 for row in rows if row["delta_comp_tokens"] < 0),
        "records_unchanged": sum(1 for row in rows if row["delta_comp_tokens"] == 0),
        "records_increased": sum(1 for row in rows if row["delta_comp_tokens"] > 0),
        "avg_span_token_length_v1": avg(all_span_lengths_v1),
        "avg_span_token_length_v2": avg(all_span_lengths_v2),
    }
    return summary, rows


def render_spans(spans: list[dict[str, Any]]) -> str:
    if not spans:
        return "_None_"
    return "<br>".join(
        f"[{span['start']}:{span['end']}] `{span['text']}` ({span['token_length']} tok)"
        for span in spans
    )


def render_markdown(summary: dict[str, Any], rows: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    lines.append("# Annotation V1 vs V2 Comparison")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total records: `{summary['total_records']}`")
    lines.append(f"- Total tokens: `{summary['total_tokens']}`")
    lines.append(f"- COMP tokens V1: `{summary['total_comp_tokens_v1']}`")
    lines.append(f"- COMP tokens V2: `{summary['total_comp_tokens_v2']}`")
    lines.append(f"- Absolute reduction: `{summary['absolute_reduction']}`")
    lines.append(f"- Percent reduction: `{summary['percent_reduction']:.2f}%`")
    lines.append(f"- Records reduced: `{summary['records_with_reduced_comp_tokens']}`")
    lines.append(f"- Records unchanged: `{summary['records_unchanged']}`")
    lines.append(f"- Records increased: `{summary['records_increased']}`")
    lines.append(f"- Avg span token length V1: `{summary['avg_span_token_length_v1']:.2f}`")
    lines.append(f"- Avg span token length V2: `{summary['avg_span_token_length_v2']:.2f}`")
    lines.append("")

    lines.append("## Per-record Table")
    lines.append("")
    lines.append("| id | comp_v1 | comp_v2 | delta | spans_v1 | spans_v2 |")
    lines.append("|---|---:|---:|---:|---:|---:|")
    for row in rows:
        lines.append(
            f"| `{row['id']}` | {row['comp_tokens_v1']} | {row['comp_tokens_v2']} | "
            f"{row['delta_comp_tokens']} | {row['spans_v1_count']} | {row['spans_v2_count']} |"
        )
    lines.append("")

    lines.append("## Largest Reductions")
    lines.append("")
    reduced_rows = sorted(rows, key=lambda row: row["delta_comp_tokens"])[:5]
    for row in reduced_rows:
        lines.append(f"### `{row['id']}`")
        lines.append("")
        lines.append(f"- Delta COMP tokens: `{row['delta_comp_tokens']}`")
        lines.append(f"- Text: {row['text']}")
        lines.append(f"- V1 spans: {render_spans(row['spans_v1'])}")
        lines.append(f"- V2 spans: {render_spans(row['spans_v2'])}")
        lines.append("")

    return "\n".join(lines)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare sample annotation BIO versions.")
    parser.add_argument("--v1", default=DEFAULT_V1)
    parser.add_argument("--v2", default=DEFAULT_V2)
    parser.add_argument("--json-output", default=DEFAULT_JSON)
    parser.add_argument("--md-output", default=DEFAULT_MD)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    v1 = load_jsonl_by_id(Path(args.v1))
    v2 = load_jsonl_by_id(Path(args.v2))
    summary, rows = compare_records(v1, v2)

    payload = {
        "summary": summary,
        "records": rows,
    }
    json_output = Path(args.json_output)
    md_output = Path(args.md_output)
    write_json(json_output, payload)
    md_output.parent.mkdir(parents=True, exist_ok=True)
    md_output.write_text(render_markdown(summary, rows), encoding="utf-8")

    print(f"JSON output       : {json_output}")
    print(f"Markdown output   : {md_output}")
    print(f"Total records     : {summary['total_records']}")
    print(f"COMP tokens V1    : {summary['total_comp_tokens_v1']}")
    print(f"COMP tokens V2    : {summary['total_comp_tokens_v2']}")
    print(f"Reduction         : {summary['absolute_reduction']} ({summary['percent_reduction']:.2f}%)")
    print(f"Records reduced   : {summary['records_with_reduced_comp_tokens']}")
    print(f"Records unchanged : {summary['records_unchanged']}")
    print(f"Records increased : {summary['records_increased']}")
    print("Top 5 reductions:")
    for row in sorted(rows, key=lambda item: item["delta_comp_tokens"])[:5]:
        print(
            f"  {row['id']}: {row['comp_tokens_v1']} -> {row['comp_tokens_v2']} "
            f"(delta {row['delta_comp_tokens']})"
        )


if __name__ == "__main__":
    main()
