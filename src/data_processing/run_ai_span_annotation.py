"""
Run AI-assisted complaint span annotation for a small JSONL sample.

Safety defaults:
    - reads only data/processed/annotation_sample_train_20.jsonl
    - annotates at most 20 records by default
    - requires OPENAI_API_KEY from the environment
    - supports --dry-run without importing or calling the OpenAI SDK
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


DEFAULT_INPUT = "data/processed/annotation_sample_train_20.jsonl"
DEFAULT_PROMPT = "docs/ai_span_annotation_prompt.md"
DEFAULT_OUTPUT = "data/processed/annotation_sample_train_20_ai.jsonl"
DEFAULT_REPORT = "data/processed/annotation_sample_train_20_ai_run_report.json"
DEFAULT_REQUEST = "data/processed/annotation_sample_train_20_request.txt"
DEFAULT_VALIDATION_REPORT = "data/processed/annotation_sample_train_20_validation_report.json"


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
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON at {path}:{line_no}: {exc}") from exc
    return records


def read_text(path: Path) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def chunks(records: list[dict[str, Any]], batch_size: int) -> list[list[dict[str, Any]]]:
    return [records[i : i + batch_size] for i in range(0, len(records), batch_size)]


def build_batch_prompt(guideline: str, batch: list[dict[str, Any]]) -> str:
    batch_jsonl = "\n".join(json.dumps(record, ensure_ascii=False) for record in batch)
    return (
        f"{guideline.rstrip()}\n\n"
        "INPUT JSONL TO ANNOTATE:\n"
        f"{batch_jsonl}\n"
    )


def parse_jsonl_response(content: str, batch_index: int) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    stripped = content.strip()
    if stripped.startswith("```"):
        raise ValueError(
            f"Batch {batch_index}: model returned markdown fences; expected raw JSONL."
        )

    for line_no, line in enumerate(stripped.splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Batch {batch_index}, response line {line_no}: invalid JSON: {exc}"
            ) from exc
        if not isinstance(record, dict):
            raise ValueError(
                f"Batch {batch_index}, response line {line_no}: expected JSON object."
            )
        records.append(record)
    return records


def write_report(report_path: Path, report: dict[str, Any]) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)


def ensure_openai_ready() -> bool:
    if not os.getenv("OPENAI_API_KEY"):
        print(
            "OPENAI_API_KEY not found. Please set it as an environment variable "
            "or use manual annotation request file."
        )
        print(f"Manual request file: {DEFAULT_REQUEST}")
        return False

    try:
        import openai  # noqa: F401
    except ImportError:
        print(
            "OpenAI SDK is not installed in this environment. "
            "Install it with: pip install openai"
        )
        print("No API call was made.")
        return False

    return True


def call_openai(model: str, prompt: str) -> str:
    from openai import OpenAI

    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a strict JSONL annotation engine. "
                    "Return only raw JSONL, no markdown, no extra text."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )
    return response.choices[0].message.content or ""


def run_validator(input_candidates: Path, annotations: Path, validation_report: Path) -> int:
    cmd = [
        sys.executable,
        "-m",
        "src.data_processing.validate_span_annotations",
        "--input-candidates",
        str(input_candidates),
        "--annotations",
        str(annotations),
        "--report-out",
        str(validation_report),
    ]
    completed = subprocess.run(cmd, text=True)
    return completed.returncode


def run_annotation(args: argparse.Namespace) -> int:
    input_path = Path(args.input)
    prompt_path = Path(args.prompt_file)
    output_path = Path(args.output)
    report_path = Path(args.report_out)
    validation_report = Path(args.validation_report)

    if not input_path.exists():
        print(f"Input file not found: {input_path}")
        return 2
    if not prompt_path.exists():
        print(f"Prompt file not found: {prompt_path}")
        return 2
    if args.batch_size <= 0:
        print("--batch-size must be positive.")
        return 2
    if args.max_records <= 0:
        print("--max-records must be positive.")
        return 2

    records = load_jsonl(input_path, max_records=args.max_records)
    guideline = read_text(prompt_path)
    has_key = bool(os.getenv("OPENAI_API_KEY"))

    print(f"Input path       : {input_path}")
    print(f"Prompt file      : {prompt_path}")
    print(f"Output path      : {output_path}")
    print(f"Model            : {args.model}")
    print(f"Batch size       : {args.batch_size}")
    print(f"Max records      : {args.max_records}")
    print(f"Records selected : {len(records)}")
    print(f"OPENAI_API_KEY   : {'found' if has_key else 'not found'}")

    if args.dry_run:
        preview_prompt = build_batch_prompt(guideline, records[: min(args.batch_size, len(records))])
        print("\nDry run only. No API call was made.")
        print("Prompt preview:")
        print(preview_prompt[:2000])
        if len(preview_prompt) > 2000:
            print("... [preview truncated]")
        return 0

    if not ensure_openai_ready():
        return 2

    report: dict[str, Any] = {
        "input_path": str(input_path),
        "output_path": str(output_path),
        "model": args.model,
        "total_input": len(records),
        "total_annotated": 0,
        "failed_batches": 0,
        "errors": [],
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    batches = chunks(records, args.batch_size)

    with open(output_path, "w", encoding="utf-8") as out_f:
        for batch_index, batch in enumerate(batches, start=1):
            prompt = build_batch_prompt(guideline, batch)
            try:
                content = call_openai(args.model, prompt)
                annotated = parse_jsonl_response(content, batch_index)
                if len(annotated) != len(batch):
                    raise ValueError(
                        f"Batch {batch_index}: expected {len(batch)} records, got {len(annotated)}."
                    )

                for record in annotated:
                    out_f.write(json.dumps(record, ensure_ascii=False) + "\n")
                out_f.flush()
                report["total_annotated"] += len(annotated)
                print(f"[OK] Batch {batch_index}/{len(batches)}: {len(annotated)} records")
            except Exception as exc:
                report["failed_batches"] += 1
                report["errors"].append(
                    {
                        "batch": batch_index,
                        "message": str(exc),
                        "ids": [record.get("id") for record in batch],
                    }
                )
                print(f"[ERROR] Batch {batch_index}/{len(batches)} failed: {exc}")
                if args.stop_on_error:
                    break
            time.sleep(args.sleep_seconds)

    write_report(report_path, report)
    print(f"Run report: {report_path}")

    if report["total_annotated"] > 0:
        print("\nRunning validator...")
        validator_code = run_validator(input_path, output_path, validation_report)
        if validator_code != 0:
            print(
                "Validator failed. No automatic guessing/fixing was performed. "
                f"Check validation report: {validation_report}"
            )
            return validator_code
        print("Validator passed.")

    return 0 if report["failed_batches"] == 0 else 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run AI-assisted complaint span annotation on the 20-row sample batch."
    )
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--prompt-file", default=DEFAULT_PROMPT)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--model", default="gpt-4o-mini")
    parser.add_argument("--batch-size", type=int, default=5)
    parser.add_argument("--max-records", type=int, default=20)
    parser.add_argument("--sleep-seconds", type=float, default=1.0)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--stop-on-error", action="store_true")
    parser.add_argument("--report-out", default=DEFAULT_REPORT)
    parser.add_argument("--validation-report", default=DEFAULT_VALIDATION_REPORT)
    return parser.parse_args()


def main() -> None:
    raise SystemExit(run_annotation(parse_args()))


if __name__ == "__main__":
    main()
