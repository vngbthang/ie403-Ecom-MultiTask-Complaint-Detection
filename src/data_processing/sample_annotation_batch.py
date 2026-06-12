"""
Sample a small JSONL batch for AI-assisted annotation testing.

This script does not call any AI API and does not assign labels.
It preserves the input schema exactly.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


DEFAULT_INPUT = "data/processed/uit_viocd_annotation_candidates_train.jsonl"
DEFAULT_OUTPUT = "data/processed/annotation_sample_train_20.jsonl"


def load_jsonl(path: Path) -> list[dict]:
    records = []
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON at {path}:{line_no}: {exc}") from exc
    return records


def write_jsonl(records: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def sample_records(records: list[dict], sample_size: int, seed: int) -> list[dict]:
    if sample_size < 0:
        raise ValueError("--sample-size must be non-negative")
    if sample_size >= len(records):
        return list(records)

    import random

    rng = random.Random(seed)
    indices = sorted(rng.sample(range(len(records)), sample_size))
    return [records[idx] for idx in indices]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a small JSONL sample batch for AI span annotation."
    )
    parser.add_argument("--input", default=DEFAULT_INPUT, help="Input JSONL path")
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="Output JSONL path")
    parser.add_argument("--sample-size", type=int, default=20, help="Number of rows to sample")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    records = load_jsonl(input_path)
    sampled = sample_records(records, sample_size=args.sample_size, seed=args.seed)
    write_jsonl(sampled, output_path)

    print(f"Input path  : {input_path}")
    print(f"Input rows  : {len(records)}")
    print(f"Output path : {output_path}")
    print(f"Output rows : {len(sampled)}")


if __name__ == "__main__":
    main()
