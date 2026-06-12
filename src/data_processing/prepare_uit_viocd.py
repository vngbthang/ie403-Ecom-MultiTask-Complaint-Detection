"""
Prepare UIT-ViOCD raw splits for the UIT-only complaint analysis pipeline.

Input:
    data/raw/UIT-ViOCD/{train,val,test}.csv

Output:
    data/processed/uit_viocd_{train,val,test}.csv

Output schema:
    id, review, review_tokenize, complaint_label, domain, split
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


SPLITS = ("train", "val", "test")
OUTPUT_COLUMNS = [
    "id",
    "review",
    "review_tokenize",
    "complaint_label",
    "domain",
    "split",
]


def drop_index_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Remove unnamed/index columns produced by CSV exports."""
    index_like_cols = [
        col
        for col in df.columns
        if str(col).startswith("Unnamed:") or str(col).strip() == "H1"
    ]
    if index_like_cols:
        df = df.drop(columns=index_like_cols)
    return df


def validate_columns(df: pd.DataFrame, path: Path) -> None:
    required = {"review", "label"}
    missing = sorted(required - set(df.columns))
    if missing:
        raise ValueError(
            f"{path} is missing required columns: {missing}. "
            f"Found columns: {df.columns.tolist()}"
        )


def normalize_split(raw_path: Path, split: str) -> tuple[pd.DataFrame, int]:
    df = pd.read_csv(raw_path, encoding="utf-8-sig")
    df.columns = [str(col).strip() for col in df.columns]
    df = drop_index_columns(df)
    validate_columns(df, raw_path)

    before = len(df)
    review_text = df["review"].astype("string")
    valid_review_mask = review_text.notna() & review_text.str.strip().ne("")
    dropped = int((~valid_review_mask).sum())
    if dropped:
        print(f"[WARN] {split}: dropped {dropped} rows with empty review")
    df = df.loc[valid_review_mask].copy().reset_index(drop=True)

    complaint_label = pd.to_numeric(df["label"], errors="coerce")
    invalid_label_mask = ~complaint_label.isin([0, 1, 0.0, 1.0])
    invalid_count = int(invalid_label_mask.sum())
    if invalid_count:
        raise ValueError(
            f"{raw_path} has {invalid_count} invalid labels. "
            "Expected binary labels 0/1."
        )

    output = pd.DataFrame(
        {
            "id": [f"{split}_{idx:06d}" for idx in range(1, len(df) + 1)],
            "review": df["review"].astype(str),
            "review_tokenize": (
                df["review_tokenize"].astype(str)
                if "review_tokenize" in df.columns
                else ""
            ),
            "complaint_label": complaint_label.astype(int),
            "domain": df["domain"].astype(str) if "domain" in df.columns else "",
            "split": split,
        }
    )

    return output[OUTPUT_COLUMNS], before


def print_split_stats(split: str, df: pd.DataFrame, raw_rows: int) -> None:
    print(f"\n[{split}]")
    print(f"  Raw rows       : {raw_rows}")
    print(f"  Processed rows : {len(df)}")

    label_dist = df["complaint_label"].value_counts().sort_index()
    print("  Label distribution:")
    for label, count in label_dist.items():
        print(f"    {int(label)}: {int(count)}")

    if "domain" in df.columns and df["domain"].astype(str).str.strip().ne("").any():
        domain_dist = df["domain"].value_counts().sort_index()
        print("  Domain distribution:")
        for domain, count in domain_dist.items():
            print(f"    {domain}: {int(count)}")


def prepare_uit_viocd(raw_dir: Path, out_dir: Path) -> dict[str, pd.DataFrame]:
    out_dir.mkdir(parents=True, exist_ok=True)

    outputs: dict[str, pd.DataFrame] = {}
    for split in SPLITS:
        raw_path = raw_dir / f"{split}.csv"
        if not raw_path.exists():
            raise FileNotFoundError(f"Raw split not found: {raw_path}")

        processed_df, raw_rows = normalize_split(raw_path, split)
        out_path = out_dir / f"uit_viocd_{split}.csv"
        processed_df.to_csv(out_path, index=False, encoding="utf-8-sig")

        print_split_stats(split, processed_df, raw_rows)
        print(f"  Saved          : {out_path}")
        outputs[split] = processed_df

    return outputs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Normalize UIT-ViOCD raw splits into processed CSV files."
    )
    parser.add_argument(
        "--raw-dir",
        default="data/raw/UIT-ViOCD",
        help="Directory containing train.csv, val.csv, test.csv",
    )
    parser.add_argument(
        "--out-dir",
        default="data/processed",
        help="Directory where processed CSV files will be written",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    prepare_uit_viocd(
        raw_dir=Path(args.raw_dir),
        out_dir=Path(args.out_dir),
    )


if __name__ == "__main__":
    main()
