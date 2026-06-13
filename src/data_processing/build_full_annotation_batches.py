"""
Build AI annotation request batches for all remaining UIT-ViOCD complaint reviews.

The script excludes ids already annotated in pilot100 and batch200 fixed, then
creates deterministic JSONL/request batches for manual or AI-assisted annotation.
It does not modify existing annotation/BIO/training artifacts.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


DEFAULT_CANDIDATES = [
    "data/processed/uit_viocd_annotation_candidates_train.jsonl",
    "data/processed/uit_viocd_annotation_candidates_val.jsonl",
    "data/processed/uit_viocd_annotation_candidates_test.jsonl",
]
DEFAULT_EXISTING = [
    "data/processed/uit_viocd_pilot_100_annotations.jsonl",
    "data/processed/annotation_batch_200_new_for_pilot300_ai_repaired_fixed.jsonl",
]
DEFAULT_PROMPT = "docs/ai_span_annotation_prompt.md"
DEFAULT_OUT_DIR = "data/processed/full_annotation_batches"
DEFAULT_BATCH_SIZE = 200
DEFAULT_SEED = 42

SPLIT_ORDER = {"train": 0, "val": 1, "test": 2}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8-sig") as f:
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


def get_id(record: dict[str, Any]) -> str:
    record_id = record.get("id")
    if record_id is None or str(record_id) == "":
        raise ValueError(f"Record missing id: {record}")
    return str(record_id)


def get_meta(record: dict[str, Any]) -> dict[str, Any]:
    meta = record.get("meta", {})
    return meta if isinstance(meta, dict) else {}


def get_split(record: dict[str, Any]) -> str:
    return str(get_meta(record).get("split", ""))


def get_domain(record: dict[str, Any]) -> str:
    domain = get_meta(record).get("domain", "")
    return "" if domain is None else str(domain)


def normalize_candidate(record: dict[str, Any]) -> dict[str, Any]:
    record_id = get_id(record)
    text = record.get("text", "")
    if not isinstance(text, str):
        text = "" if text is None else str(text)

    meta = dict(get_meta(record))
    meta.setdefault("source", "UIT-ViOCD")
    meta.setdefault("split", "")
    meta.setdefault("domain", "")
    meta.setdefault("cls_label", 1)

    return {
        "id": record_id,
        "text": text,
        "label": record.get("label", []) if isinstance(record.get("label", []), list) else [],
        "meta": meta,
    }


def load_candidates(paths: list[Path]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in paths:
        if not path.exists():
            raise FileNotFoundError(f"Candidate file not found: {path}")
        records.extend(normalize_candidate(record) for record in load_jsonl(path))
    return records


def load_existing_ids(paths: list[Path]) -> set[str]:
    ids: set[str] = set()
    for path in paths:
        if not path.exists():
            raise FileNotFoundError(f"Existing annotation file not found: {path}")
        for record in load_jsonl(path):
            ids.add(get_id(record))
    return ids


def count_duplicate_ids(records: list[dict[str, Any]]) -> int:
    ids = [get_id(record) for record in records]
    return len(ids) - len(set(ids))


def deterministic_sort(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        records,
        key=lambda record: (
            SPLIT_ORDER.get(get_split(record), 99),
            get_domain(record),
            get_id(record),
        ),
    )


def chunk_records(records: list[dict[str, Any]], batch_size: int) -> list[list[dict[str, Any]]]:
    return [records[idx : idx + batch_size] for idx in range(0, len(records), batch_size)]


def write_jsonl(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def write_request(prompt: str, records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write(prompt.rstrip())
        f.write("\n\n")
        f.write("INPUT JSONL TO ANNOTATE:\n")
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False))
            f.write("\n")


def distribution(records: list[dict[str, Any]], field: str) -> dict[str, int]:
    if field == "split":
        counts = Counter(get_split(record) for record in records)
    elif field == "domain":
        counts = Counter(get_domain(record) for record in records)
    else:
        raise ValueError(f"Unsupported distribution field: {field}")
    return dict(sorted(counts.items()))


def build_markdown(manifest: dict[str, Any]) -> str:
    lines = [
        "# Full UIT-ViOCD Complaint Annotation Batches",
        "",
        "## Summary",
        "",
        f"- Total complaint candidates: `{manifest['total_candidates']}`",
        f"- Already annotated: `{manifest['existing_annotated_count']}`",
        f"- Remaining: `{manifest['remaining_count']}`",
        f"- Batch size: `{manifest['batch_size']}`",
        f"- Num batches: `{manifest['num_batches']}`",
        f"- Duplicate ids count: `{manifest['duplicate_ids_count']}`",
        "",
        "## Batches",
        "",
        "| batch | records | split distribution | domain distribution | first 5 ids |",
        "|---|---:|---|---|---|",
    ]
    for batch in manifest["batches"]:
        split_dist = ", ".join(f"{k}: {v}" for k, v in batch["split_distribution"].items())
        domain_dist = ", ".join(f"{k}: {v}" for k, v in batch["domain_distribution"].items())
        first_ids = ", ".join(batch["first_5_ids"])
        lines.append(
            f"| {batch['batch_id']} | {batch['record_count']} | "
            f"{split_dist} | {domain_dist} | {first_ids} |"
        )
    lines.append("")
    return "\n".join(lines)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build full UIT-ViOCD annotation batches.")
    parser.add_argument("--candidates", nargs="+", default=DEFAULT_CANDIDATES)
    parser.add_argument("--existing-annotations", nargs="+", default=DEFAULT_EXISTING)
    parser.add_argument("--prompt-file", default=DEFAULT_PROMPT)
    parser.add_argument("--out-dir", default=DEFAULT_OUT_DIR)
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    candidate_paths = [Path(path) for path in args.candidates]
    existing_paths = [Path(path) for path in args.existing_annotations]
    prompt_path = Path(args.prompt_file)
    out_dir = Path(args.out_dir)

    if args.batch_size <= 0:
        raise ValueError("--batch-size must be positive")
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")

    candidates = load_candidates(candidate_paths)
    duplicate_candidate_ids = count_duplicate_ids(candidates)
    if duplicate_candidate_ids:
        raise ValueError(f"Duplicate candidate ids found: {duplicate_candidate_ids}")

    existing_ids = load_existing_ids(existing_paths)
    remaining = [
        record
        for record in candidates
        if get_id(record) not in existing_ids
    ]
    remaining = deterministic_sort(remaining)
    duplicate_remaining_ids = count_duplicate_ids(remaining)
    if duplicate_remaining_ids:
        raise ValueError(f"Duplicate remaining ids found: {duplicate_remaining_ids}")

    prompt = prompt_path.read_text(encoding="utf-8")
    out_dir.mkdir(parents=True, exist_ok=True)
    batches = chunk_records(remaining, args.batch_size)

    batch_manifest: list[dict[str, Any]] = []
    for index, batch_records in enumerate(batches, start=1):
        batch_id = f"full_annotation_batch_{index:03d}"
        jsonl_path = out_dir / f"{batch_id}.jsonl"
        request_path = out_dir / f"{batch_id}_request.txt"
        write_jsonl(batch_records, jsonl_path)
        write_request(prompt, batch_records, request_path)

        batch_manifest.append(
            {
                "batch_id": batch_id,
                "input_jsonl": str(jsonl_path),
                "request_txt": str(request_path),
                "record_count": len(batch_records),
                "split_distribution": distribution(batch_records, "split"),
                "domain_distribution": distribution(batch_records, "domain"),
                "first_5_ids": [get_id(record) for record in batch_records[:5]],
            }
        )

    manifest = {
        "candidate_files": [str(path) for path in candidate_paths],
        "existing_annotation_files": [str(path) for path in existing_paths],
        "prompt_file": str(prompt_path),
        "output_dir": str(out_dir),
        "seed": args.seed,
        "total_candidates": len(candidates),
        "existing_annotated_count": len(existing_ids),
        "remaining_count": len(remaining),
        "batch_size": args.batch_size,
        "num_batches": len(batches),
        "duplicate_ids_count": duplicate_candidate_ids + duplicate_remaining_ids,
        "remaining_split_distribution": distribution(remaining, "split"),
        "remaining_domain_distribution": distribution(remaining, "domain"),
        "batches": batch_manifest,
    }

    manifest_path = out_dir / "full_annotation_batches_manifest.json"
    summary_path = out_dir / "full_annotation_batches_summary.md"
    write_json(manifest_path, manifest)
    summary_path.write_text(build_markdown(manifest), encoding="utf-8")

    print(f"Output dir              : {out_dir}")
    print(f"Manifest                : {manifest_path}")
    print(f"Summary Markdown        : {summary_path}")
    print(f"Total candidates        : {manifest['total_candidates']}")
    print(f"Existing annotated count: {manifest['existing_annotated_count']}")
    print(f"Remaining count         : {manifest['remaining_count']}")
    print(f"Batch size              : {manifest['batch_size']}")
    print(f"Num batches             : {manifest['num_batches']}")
    print(f"Duplicate ids count     : {manifest['duplicate_ids_count']}")
    if batch_manifest:
        first = batch_manifest[0]
        print(f"First batch JSONL       : {first['input_jsonl']}")
        print(f"First batch request     : {first['request_txt']}")


if __name__ == "__main__":
    main()
