"""
Run a smoke PhoBERT NER training job on the UIT-ViOCD pilot 100 dataset.

Usage from repo root:
    python scripts/run_pilot_100_phobert_ner_smoke.py --dry-run
    python scripts/run_pilot_100_phobert_ner_smoke.py
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

TRAIN_JSON = Path("data/processed/uit_viocd_pilot_100_ner_train.json")
VAL_JSON = Path("data/processed/uit_viocd_pilot_100_ner_val.json")
TEST_JSON = Path("data/processed/uit_viocd_pilot_100_ner_test.json")
OUTPUT_DIR = Path("outputs/metrics/uit_viocd_pilot_100_phobert_ner_smoke")

EPOCHS = 1
BATCH_SIZE = 8
LEARNING_RATE = 2e-5
MODEL_NAME = "vinai/phobert-base-v2"


def load_json_list(path: Path) -> list[dict[str, Any]]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"{path} must contain a JSON list")
    return data


def validate_ner_records(split_name: str, records: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    for idx, record in enumerate(records):
        if not isinstance(record, dict):
            errors.append(f"{split_name}[{idx}] is not an object")
            continue
        record_id = str(record.get("id", f"<missing-id-{idx}>"))
        if record_id in seen_ids:
            errors.append(f"{split_name}: duplicate id {record_id}")
        seen_ids.add(record_id)
        for field in ("id", "tokens", "ner_tags"):
            if field not in record:
                errors.append(f"{split_name}:{record_id} missing field {field}")
        tokens = record.get("tokens")
        tags = record.get("ner_tags")
        if not isinstance(tokens, list) or not isinstance(tags, list):
            errors.append(f"{split_name}:{record_id} tokens/ner_tags must be lists")
            continue
        if len(tokens) != len(tags):
            errors.append(
                f"{split_name}:{record_id} length mismatch "
                f"tokens={len(tokens)} ner_tags={len(tags)}"
            )
    return errors


def print_torch_info() -> None:
    try:
        import torch
    except ImportError:
        print("[WARN] torch is not installed.")
        return

    print(f"torch version             : {torch.__version__}")
    cuda_available = torch.cuda.is_available()
    print(f"torch.cuda.is_available() : {cuda_available}")
    if cuda_available:
        print(f"GPU name                  : {torch.cuda.get_device_name(0)}")


def build_train_command() -> list[str]:
    return [
        sys.executable,
        "-m",
        "src.training.train_phobert_ner",
        "--train-json",
        str(TRAIN_JSON),
        "--val-json",
        str(VAL_JSON),
        "--test-json",
        str(TEST_JSON),
        "--output-dir",
        str(OUTPUT_DIR),
        "--epochs",
        str(EPOCHS),
        "--batch-size",
        str(BATCH_SIZE),
        "--learning-rate",
        str(LEARNING_RATE),
        "--model-name",
        MODEL_NAME,
        "--disable-tqdm",
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Smoke-run PhoBERT NER training on UIT-ViOCD pilot 100."
    )
    parser.add_argument("--dry-run", action="store_true", help="Validate and print command only")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    os.chdir(PROJECT_ROOT)
    print(f"Project root: {PROJECT_ROOT}")

    missing = [path for path in (TRAIN_JSON, VAL_JSON, TEST_JSON) if not path.exists()]
    if missing:
        print("[ERROR] Missing required data files:")
        for path in missing:
            print(f"  - {path}")
        return 1

    try:
        train_records = load_json_list(TRAIN_JSON)
        val_records = load_json_list(VAL_JSON)
        test_records = load_json_list(TEST_JSON)
    except Exception as exc:
        print(f"[ERROR] Failed to load JSON data: {exc}")
        return 1

    print(f"train records: {len(train_records)}")
    print(f"val records  : {len(val_records)}")
    print(f"test records : {len(test_records)}")

    schema_errors = []
    schema_errors.extend(validate_ner_records("train", train_records))
    schema_errors.extend(validate_ner_records("val", val_records))
    schema_errors.extend(validate_ner_records("test", test_records))
    if schema_errors:
        print("[ERROR] NER schema validation failed:")
        for error in schema_errors[:50]:
            print(f"  - {error}")
        if len(schema_errors) > 50:
            print(f"  ... {len(schema_errors) - 50} more errors")
        return 1

    print_torch_info()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    command = build_train_command()
    print("Train command:")
    print(" ".join(command))

    if args.dry_run:
        print("Dry run: no training was executed.")
        return 0

    completed = subprocess.run(command, cwd=PROJECT_ROOT)
    if completed.returncode != 0:
        print(f"[ERROR] Training subprocess failed with return code {completed.returncode}")
        return completed.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
