"""
Process full UIT-ViOCD annotation batches that already have AI outputs.

For each batch in the manifest:
    repair offsets -> validate -> convert spans to BIO/NER

Missing AI output files are skipped and reported. This script does not merge
with pilot100/batch200 and does not modify training code or metrics.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from src.data_processing.convert_spans_to_bio import convert_spans_to_bio
from src.data_processing.repair_span_offsets import (
    load_jsonl as load_annotation_jsonl,
    repair_records,
    write_jsonl,
    write_report,
)
from src.data_processing.validate_span_annotations import validate_annotations


DEFAULT_MANIFEST = "data/processed/full_annotation_batches/full_annotation_batches_manifest.json"
DEFAULT_SUMMARY_JSON = "data/processed/full_annotation_batches/full_annotation_processing_summary.json"
DEFAULT_SUMMARY_MD = "data/processed/full_annotation_batches/full_annotation_processing_summary.md"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return data


def read_json_report(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return load_json(path)


def ai_output_path(input_jsonl: Path) -> Path:
    return input_jsonl.with_name(f"{input_jsonl.stem}_ai.jsonl")


def batch_output_paths(input_jsonl: Path) -> dict[str, Path]:
    stem = input_jsonl.stem
    parent = input_jsonl.parent
    return {
        "ai": parent / f"{stem}_ai.jsonl",
        "repaired": parent / f"{stem}_ai_repaired.jsonl",
        "repair_report": parent / f"{stem}_repair_report.json",
        "validation_report": parent / f"{stem}_validation_report.json",
        "bio": parent / f"{stem}_bio.jsonl",
        "ner": parent / f"{stem}_ner.json",
        "bio_report": parent / f"{stem}_bio_conversion_report.json",
    }


def warning_count(report: dict[str, Any], warning_type: str) -> int:
    return sum(1 for warning in report.get("warnings", []) if warning.get("warning_type") == warning_type)


def process_batch(batch: dict[str, Any]) -> dict[str, Any]:
    batch_id = batch["batch_id"]
    input_jsonl = Path(batch["input_jsonl"])
    paths = batch_output_paths(input_jsonl)

    result: dict[str, Any] = {
        "batch_id": batch_id,
        "input_jsonl": str(input_jsonl),
        "ai_output": str(paths["ai"]),
        "record_count_expected": batch.get("record_count"),
        "status": "pending",
        "validation_pass": False,
        "converted": False,
        "error": None,
        "outputs": {
            "repaired": str(paths["repaired"]),
            "repair_report": str(paths["repair_report"]),
            "validation_report": str(paths["validation_report"]),
            "bio": str(paths["bio"]),
            "ner": str(paths["ner"]),
            "bio_conversion_report": str(paths["bio_report"]),
        },
        "repair_summary": {},
        "validation_summary": {},
        "conversion_summary": {},
        "conversion_warning_counts": {},
    }

    if not paths["ai"].exists():
        result["status"] = "missing_ai_output"
        return result

    try:
        records = load_annotation_jsonl(paths["ai"])
        repaired_records, repair_report = repair_records(records, strict=False)
        write_jsonl(repaired_records, paths["repaired"])
        write_report(repair_report, paths["repair_report"])
        result["repair_summary"] = repair_report.get("summary", {})
    except Exception as exc:
        result["status"] = "repair_failed"
        result["error"] = str(exc)
        return result

    try:
        exit_code = validate_annotations(
            input_candidates=input_jsonl,
            annotations=paths["repaired"],
            report_out=paths["validation_report"],
            allow_missing=False,
        )
        validation_report = read_json_report(paths["validation_report"])
        validation_summary = validation_report.get("summary", {})
        result["validation_summary"] = validation_summary
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
            annotations_path=paths["repaired"],
            candidates_path=input_jsonl,
            bio_output_path=paths["bio"],
            ner_output_path=paths["ner"],
            report_path=paths["bio_report"],
            token_source="whitespace",
        )
        result["conversion_summary"] = conversion_report.get("summary", {})
        result["conversion_warning_counts"] = dict(
            sorted(Counter(warning.get("warning_type", "unknown") for warning in conversion_report.get("warnings", [])).items())
        )
        result["converted"] = True
        result["status"] = "processed"
    except Exception as exc:
        result["status"] = "conversion_failed"
        result["error"] = str(exc)

    return result


def build_summary(manifest: dict[str, Any], batch_results: list[dict[str, Any]]) -> dict[str, Any]:
    missing = [item for item in batch_results if item["status"] == "missing_ai_output"]
    validation_failed = [item for item in batch_results if item["status"] == "validation_failed"]
    validation_passed = [item for item in batch_results if item.get("validation_pass")]
    processed = [item for item in batch_results if item["status"] == "processed"]

    total_records_processed = sum(
        int(item.get("validation_summary", {}).get("total_annotation_records", 0))
        for item in batch_results
        if item["status"] != "missing_ai_output"
    )
    total_valid_records = sum(
        int(item.get("validation_summary", {}).get("valid_records", 0))
        for item in batch_results
    )
    total_invalid_records = sum(
        int(item.get("validation_summary", {}).get("invalid_records", 0))
        for item in batch_results
    )
    total_spans = sum(int(item.get("repair_summary", {}).get("spans_total", 0)) for item in batch_results)
    total_repaired = sum(int(item.get("repair_summary", {}).get("spans_repaired", 0)) for item in batch_results)
    total_unresolved = sum(int(item.get("repair_summary", {}).get("spans_unresolved", 0)) for item in batch_results)
    total_conversion_warnings = sum(
        int(item.get("conversion_summary", {}).get("warnings", 0))
        for item in batch_results
    )
    overlapping_spans = sum(
        int(item.get("conversion_warning_counts", {}).get("overlapping_spans", 0))
        for item in batch_results
    )

    return {
        "manifest": manifest.get("output_dir"),
        "total_batches": len(batch_results),
        "processed_batches": len(processed),
        "missing_ai_output_batches": len(missing),
        "validation_passed_batches": len(validation_passed),
        "validation_failed_batches": len(validation_failed),
        "total_records_processed": total_records_processed,
        "total_valid_records": total_valid_records,
        "total_invalid_records": total_invalid_records,
        "total_spans": total_spans,
        "total_repaired_spans": total_repaired,
        "total_unresolved_spans": total_unresolved,
        "total_conversion_warnings": total_conversion_warnings,
        "overlapping_spans_count": overlapping_spans,
        "missing_ai_output_batch_ids": [item["batch_id"] for item in missing],
        "validation_failed_batch_ids": [item["batch_id"] for item in validation_failed],
        "failed_batches": [
            {
                "batch_id": item["batch_id"],
                "status": item["status"],
                "error": item.get("error"),
                "validation_summary": item.get("validation_summary", {}),
            }
            for item in batch_results
            if item["status"] not in ("processed", "missing_ai_output")
        ],
    }


def render_markdown(summary: dict[str, Any], batch_results: list[dict[str, Any]]) -> str:
    lines = [
        "# Full Annotation Batch Processing Summary",
        "",
        "## Global Summary",
        "",
        f"- Total batches: `{summary['total_batches']}`",
        f"- Processed batches: `{summary['processed_batches']}`",
        f"- Missing AI output batches: `{summary['missing_ai_output_batches']}`",
        f"- Validation passed batches: `{summary['validation_passed_batches']}`",
        f"- Validation failed batches: `{summary['validation_failed_batches']}`",
        f"- Total records processed: `{summary['total_records_processed']}`",
        f"- Total valid records: `{summary['total_valid_records']}`",
        f"- Total invalid records: `{summary['total_invalid_records']}`",
        f"- Total spans: `{summary['total_spans']}`",
        f"- Total repaired spans: `{summary['total_repaired_spans']}`",
        f"- Total unresolved spans: `{summary['total_unresolved_spans']}`",
        f"- Total conversion warnings: `{summary['total_conversion_warnings']}`",
        f"- overlapping_spans count: `{summary['overlapping_spans_count']}`",
        "",
        "## Batch Details",
        "",
        "| batch | status | records | valid | invalid | spans | repaired | unresolved | conversion warnings | overlap warnings |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for item in batch_results:
        validation = item.get("validation_summary", {})
        repair = item.get("repair_summary", {})
        conversion = item.get("conversion_summary", {})
        warning_counts = item.get("conversion_warning_counts", {})
        lines.append(
            f"| {item['batch_id']} | {item['status']} | "
            f"{validation.get('total_annotation_records', 0)} | "
            f"{validation.get('valid_records', 0)} | "
            f"{validation.get('invalid_records', 0)} | "
            f"{repair.get('spans_total', 0)} | "
            f"{repair.get('spans_repaired', 0)} | "
            f"{repair.get('spans_unresolved', 0)} | "
            f"{conversion.get('warnings', 0)} | "
            f"{warning_counts.get('overlapping_spans', 0)} |"
        )

    if summary["failed_batches"]:
        lines.extend(["", "## Failed Batches", ""])
        for item in summary["failed_batches"]:
            lines.append(f"- `{item['batch_id']}`: {item['status']} - {item.get('error') or item.get('validation_summary')}")

    if summary["missing_ai_output_batch_ids"]:
        lines.extend(["", "## Missing AI Outputs", ""])
        lines.append(", ".join(f"`{batch_id}`" for batch_id in summary["missing_ai_output_batch_ids"]))

    lines.append("")
    return "\n".join(lines)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Process full annotation batches with AI outputs.")
    parser.add_argument("--manifest", default=DEFAULT_MANIFEST)
    parser.add_argument("--summary-json", default=DEFAULT_SUMMARY_JSON)
    parser.add_argument("--summary-md", default=DEFAULT_SUMMARY_MD)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    manifest_path = Path(args.manifest)
    manifest = load_json(manifest_path)
    batches = manifest.get("batches", [])
    if not isinstance(batches, list):
        raise ValueError("Manifest field 'batches' must be a list")

    batch_results = []
    for batch in batches:
        batch_id = batch.get("batch_id", "unknown")
        print(f"\n[PROCESS] {batch_id}")
        result = process_batch(batch)
        batch_results.append(result)
        print(f"  status     : {result['status']}")
        if result.get("validation_summary"):
            summary = result["validation_summary"]
            print(
                f"  validation : valid={summary.get('valid_records', 0)} "
                f"invalid={summary.get('invalid_records', 0)}"
            )
        if result.get("conversion_summary"):
            summary = result["conversion_summary"]
            print(f"  conversion : warnings={summary.get('warnings', 0)}")
        if result.get("error"):
            print(f"  error      : {result['error']}")

    summary = build_summary(manifest, batch_results)
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
    print("Full annotation processing summary")
    print("=" * 72)
    print(f"Summary JSON              : {summary_json}")
    print(f"Summary Markdown          : {summary_md}")
    print(f"Total batches             : {summary['total_batches']}")
    print(f"Processed batches         : {summary['processed_batches']}")
    print(f"Missing AI output batches : {summary['missing_ai_output_batches']}")
    print(f"Validation passed batches : {summary['validation_passed_batches']}")
    print(f"Validation failed batches : {summary['validation_failed_batches']}")
    print(f"Total valid records       : {summary['total_valid_records']}")
    print(f"Total invalid records     : {summary['total_invalid_records']}")
    print(f"Total conversion warnings : {summary['total_conversion_warnings']}")
    print(f"Overlapping spans count   : {summary['overlapping_spans_count']}")
    if summary["missing_ai_output_batch_ids"]:
        print(f"Missing AI output ids     : {', '.join(summary['missing_ai_output_batch_ids'])}")
    if summary["validation_failed_batch_ids"]:
        print(f"Validation failed ids     : {', '.join(summary['validation_failed_batch_ids'])}")


if __name__ == "__main__":
    main()
