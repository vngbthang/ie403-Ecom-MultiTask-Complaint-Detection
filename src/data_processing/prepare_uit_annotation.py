"""
Export UIT-ViOCD annotation candidates for AI-assisted complaint span labeling.

Input:
    data/processed/uit_viocd_{train,val,test}.csv

Default output:
    data/processed/uit_viocd_annotation_candidates_{train,val,test}.jsonl
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


SPLITS = ("train", "val", "test")
REQUIRED_COLUMNS = {"id", "review", "complaint_label", "split"}


def validate_columns(df: pd.DataFrame, path: Path) -> None:
    missing = sorted(REQUIRED_COLUMNS - set(df.columns))
    if missing:
        raise ValueError(
            f"{path} is missing required columns: {missing}. "
            f"Found columns: {df.columns.tolist()}"
        )


def load_processed_split(processed_dir: Path, split: str) -> pd.DataFrame:
    path = processed_dir / f"uit_viocd_{split}.csv"
    if not path.exists():
        raise FileNotFoundError(f"Processed split not found: {path}")

    df = pd.read_csv(path, encoding="utf-8-sig")
    df.columns = [str(col).strip() for col in df.columns]
    validate_columns(df, path)
    return df


def filter_candidates(
    df: pd.DataFrame,
    include_non_complaint: bool,
    sample_size: int | None,
    seed: int,
) -> pd.DataFrame:
    df = df.copy()
    df["complaint_label"] = pd.to_numeric(df["complaint_label"], errors="coerce")

    invalid_label_mask = ~df["complaint_label"].isin([0, 1, 0.0, 1.0])
    invalid_count = int(invalid_label_mask.sum())
    if invalid_count:
        raise ValueError(
            f"Found {invalid_count} rows with invalid complaint_label. "
            "Expected binary labels 0/1."
        )

    if not include_non_complaint:
        df = df[df["complaint_label"].astype(int) == 1].copy()

    if sample_size is not None and len(df) > sample_size:
        df = df.sample(n=sample_size, random_state=seed).reset_index(drop=True)
    else:
        df = df.reset_index(drop=True)

    return df


def row_to_record(row: pd.Series, split: str) -> dict:
    domain = "" if pd.isna(row.get("domain", "")) else str(row.get("domain", ""))
    cls_label = int(row["complaint_label"])

    return {
        "id": str(row["id"]),
        "text": "" if pd.isna(row["review"]) else str(row["review"]),
        "label": [],
        "meta": {
            "source": "UIT-ViOCD",
            "split": split,
            "domain": domain,
            "cls_label": cls_label,
        },
    }


def write_jsonl(records: list[dict], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def print_split_stats(split: str, input_rows: int, output_df: pd.DataFrame, output_path: Path) -> None:
    print(f"\n[{split}]")
    print(f"  Input rows  : {input_rows}")
    print(f"  Output rows : {len(output_df)}")

    if "domain" in output_df.columns and not output_df.empty:
        domain_dist = output_df["domain"].fillna("").astype(str).value_counts().sort_index()
        print("  Domain distribution:")
        for domain, count in domain_dist.items():
            print(f"    {domain}: {int(count)}")
    else:
        print("  Domain distribution: n/a")

    print(f"  Saved       : {output_path}")


def prepare_annotation_candidates(
    processed_dir: Path,
    out_dir: Path,
    include_non_complaint: bool = False,
    sample_size: int | None = None,
    seed: int = 42,
) -> dict[str, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    output_paths: dict[str, Path] = {}

    for split in SPLITS:
        input_df = load_processed_split(processed_dir, split)
        output_df = filter_candidates(
            input_df,
            include_non_complaint=include_non_complaint,
            sample_size=sample_size,
            seed=seed,
        )

        records = [row_to_record(row, split) for _, row in output_df.iterrows()]
        output_path = out_dir / f"uit_viocd_annotation_candidates_{split}.jsonl"
        write_jsonl(records, output_path)

        print_split_stats(split, len(input_df), output_df, output_path)
        output_paths[split] = output_path

    return output_paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export UIT-ViOCD JSONL candidates for complaint span annotation."
    )
    parser.add_argument(
        "--processed-dir",
        default="data/processed",
        help="Directory containing uit_viocd_{train,val,test}.csv",
    )
    parser.add_argument(
        "--out-dir",
        default="data/processed",
        help="Directory where annotation candidates JSONL files will be written",
    )
    parser.add_argument(
        "--include-non-complaint",
        action="store_true",
        help="Include non-complaint rows with meta.cls_label=0",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=None,
        help="Maximum number of rows to sample per split after filtering",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed used when --sample-size is provided",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    prepare_annotation_candidates(
        processed_dir=Path(args.processed_dir),
        out_dir=Path(args.out_dir),
        include_non_complaint=args.include_non_complaint,
        sample_size=args.sample_size,
        seed=args.seed,
    )


if __name__ == "__main__":
    main()
