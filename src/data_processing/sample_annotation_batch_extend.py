"""
Sample new UIT-ViOCD complaint annotation records to extend pilot 100 to pilot 300.

This script keeps existing pilot annotations untouched. It samples only new
records from the UIT-ViOCD train complaint candidates, builds an AI annotation
request, and writes a summary for reproducibility.
"""

from __future__ import annotations

import argparse
import json
import random
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


DEFAULT_CANDIDATES = "data/processed/uit_viocd_annotation_candidates_train.jsonl"
DEFAULT_EXISTING = "data/processed/uit_viocd_pilot_100_annotations.jsonl"
DEFAULT_PROMPT = "docs/ai_span_annotation_prompt.md"
DEFAULT_OUTPUT = "data/processed/annotation_batch_200_new_for_pilot300.jsonl"
DEFAULT_REQUEST = "data/processed/annotation_batch_200_new_for_pilot300_request.txt"
DEFAULT_SUMMARY = "data/processed/annotation_batch_200_new_for_pilot300_summary.json"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
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


def get_record_id(record: dict[str, Any]) -> str:
    record_id = record.get("id")
    if record_id is None:
        raise ValueError(f"Record missing id: {record}")
    return str(record_id)


def get_domain(record: dict[str, Any]) -> str:
    meta = record.get("meta", {})
    if isinstance(meta, dict):
        domain = meta.get("domain", "")
    else:
        domain = ""
    return "" if domain is None else str(domain)


def validate_candidates(records: list[dict[str, Any]]) -> None:
    seen: set[str] = set()
    for record in records:
        record_id = get_record_id(record)
        if record_id in seen:
            raise ValueError(f"Duplicate candidate id: {record_id}")
        seen.add(record_id)
        if "text" not in record:
            raise ValueError(f"Candidate {record_id} missing text")
        meta = record.get("meta", {})
        if isinstance(meta, dict) and meta.get("cls_label") not in (1, "1", None):
            raise ValueError(f"Candidate {record_id} is not a complaint candidate: {meta.get('cls_label')}")


def balanced_sample_by_domain(
    records: list[dict[str, Any]],
    sample_size: int,
    seed: int,
) -> list[dict[str, Any]]:
    rng = random.Random(seed)
    by_domain: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_domain[get_domain(record)].append(record)

    for domain_records in by_domain.values():
        rng.shuffle(domain_records)

    domains = sorted(by_domain)
    if sample_size > len(records):
        raise ValueError(f"Requested {sample_size} records but only {len(records)} are available")

    base_quota = sample_size // len(domains)
    remainder = sample_size % len(domains)
    quotas = {domain: base_quota for domain in domains}

    # Give remainder slots to domains with larger available pools for stability.
    ranked_domains = sorted(domains, key=lambda d: (-len(by_domain[d]), d))
    for domain in ranked_domains[:remainder]:
        quotas[domain] += 1

    selected: list[dict[str, Any]] = []
    leftovers: list[dict[str, Any]] = []
    for domain in domains:
        domain_records = by_domain[domain]
        take = min(quotas[domain], len(domain_records))
        selected.extend(domain_records[:take])
        leftovers.extend(domain_records[take:])

    if len(selected) < sample_size:
        rng.shuffle(leftovers)
        selected.extend(leftovers[: sample_size - len(selected)])

    rng.shuffle(selected)
    return selected[:sample_size]


def write_jsonl(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def build_request(prompt_path: Path, input_records: list[dict[str, Any]], output_path: Path) -> None:
    prompt = prompt_path.read_text(encoding="utf-8").rstrip()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        f.write(prompt)
        f.write("\n\n")
        f.write("INPUT JSONL TO ANNOTATE:\n")
        for record in input_records:
            f.write(json.dumps(record, ensure_ascii=False))
            f.write("\n")


def write_summary(summary: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sample 200 new UIT-ViOCD annotation records for pilot 300.")
    parser.add_argument("--candidates", default=DEFAULT_CANDIDATES)
    parser.add_argument("--existing-annotations", default=DEFAULT_EXISTING)
    parser.add_argument("--prompt-file", default=DEFAULT_PROMPT)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--request-output", default=DEFAULT_REQUEST)
    parser.add_argument("--summary-output", default=DEFAULT_SUMMARY)
    parser.add_argument("--sample-size", type=int, default=200)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    candidates_path = Path(args.candidates)
    existing_path = Path(args.existing_annotations)
    prompt_path = Path(args.prompt_file)

    if not candidates_path.exists():
        raise FileNotFoundError(f"Candidates file not found: {candidates_path}")
    if not existing_path.exists():
        raise FileNotFoundError(f"Existing annotations file not found: {existing_path}")
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")

    candidates = read_jsonl(candidates_path)
    existing_annotations = read_jsonl(existing_path)
    validate_candidates(candidates)

    existing_ids = {get_record_id(record) for record in existing_annotations}
    candidate_ids = [get_record_id(record) for record in candidates]
    duplicate_candidate_ids = len(candidate_ids) - len(set(candidate_ids))

    available = [record for record in candidates if get_record_id(record) not in existing_ids]
    selected = balanced_sample_by_domain(available, sample_size=args.sample_size, seed=args.seed)
    selected_ids = [get_record_id(record) for record in selected]

    duplicate_selected_ids = len(selected_ids) - len(set(selected_ids))
    overlap_with_existing = sorted(set(selected_ids) & existing_ids)
    if duplicate_selected_ids:
        raise ValueError(f"Selected duplicate ids: {duplicate_selected_ids}")
    if overlap_with_existing:
        raise ValueError(f"Selected ids overlap existing pilot ids: {overlap_with_existing[:10]}")

    output_path = Path(args.output)
    request_path = Path(args.request_output)
    summary_path = Path(args.summary_output)

    write_jsonl(selected, output_path)
    build_request(prompt_path, selected, request_path)

    domain_distribution = dict(sorted(Counter(get_domain(record) for record in selected).items()))
    summary = {
        "candidates_path": str(candidates_path),
        "existing_annotations_path": str(existing_path),
        "prompt_path": str(prompt_path),
        "seed": args.seed,
        "existing_pilot_count": len(existing_ids),
        "new_batch_count": len(selected),
        "total_after_merge_expected": len(existing_ids) + len(selected),
        "duplicate_ids_count": duplicate_candidate_ids + duplicate_selected_ids,
        "overlap_with_existing_count": len(overlap_with_existing),
        "domain_distribution": domain_distribution,
        "first_10_selected_ids": selected_ids[:10],
        "output": str(output_path),
        "request_output": str(request_path),
    }
    write_summary(summary, summary_path)

    print(f"Output JSONL : {output_path}")
    print(f"Request file : {request_path}")
    print(f"Summary file : {summary_path}")
    print(f"Existing pilot count       : {len(existing_ids)}")
    print(f"New batch count            : {len(selected)}")
    print(f"Total after merge expected : {len(existing_ids) + len(selected)}")
    print(f"Duplicate ids count        : {summary['duplicate_ids_count']}")
    print(f"Overlap with pilot count   : {len(overlap_with_existing)}")
    print("Domain distribution:")
    for domain, count in domain_distribution.items():
        print(f"  {domain}: {count}")
    print(f"First 10 selected ids      : {selected_ids[:10]}")


if __name__ == "__main__":
    main()
