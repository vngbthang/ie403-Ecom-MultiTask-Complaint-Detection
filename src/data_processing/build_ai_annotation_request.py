"""
Build a plain-text request file for copying into an AI annotation tool.

This script only combines the annotation prompt with input JSONL records.
It does not call any AI API and does not assign labels.
"""

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_PROMPT = "docs/ai_span_annotation_prompt.md"
DEFAULT_INPUT = "data/processed/annotation_sample_train_20.jsonl"
DEFAULT_OUTPUT = "data/processed/annotation_sample_train_20_request.txt"


def read_text(path: Path) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def read_jsonl_lines(path: Path) -> list[str]:
    with open(path, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f if line.strip()]


def build_request(prompt_file: Path, input_jsonl: Path, output: Path) -> int:
    if not prompt_file.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_file}")
    if not input_jsonl.exists():
        raise FileNotFoundError(f"Input JSONL file not found: {input_jsonl}")

    prompt = read_text(prompt_file).rstrip()
    input_lines = read_jsonl_lines(input_jsonl)

    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, "w", encoding="utf-8") as f:
        f.write(prompt)
        f.write("\n\n")
        f.write("INPUT JSONL TO ANNOTATE:\n")
        for line in input_lines:
            f.write(line)
            f.write("\n")

    return len(input_lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build an AI annotation request text file from prompt and JSONL sample."
    )
    parser.add_argument(
        "--prompt-file",
        default=DEFAULT_PROMPT,
        help="Prompt markdown file",
    )
    parser.add_argument(
        "--input-jsonl",
        default=DEFAULT_INPUT,
        help="Input JSONL records to append to the request",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help="Output request text file",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_path = Path(args.output)
    num_lines = build_request(
        prompt_file=Path(args.prompt_file),
        input_jsonl=Path(args.input_jsonl),
        output=output_path,
    )

    print(f"Output path       : {output_path}")
    print(f"Input JSONL lines : {num_lines}")
    print(
        "Next step         : Copy this request into the AI tool, save the JSONL output to "
        "data/processed/annotation_sample_train_20_ai.jsonl, then run "
        "python -m src.data_processing.validate_span_annotations"
    )


if __name__ == "__main__":
    main()
