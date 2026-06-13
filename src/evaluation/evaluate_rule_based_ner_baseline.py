"""
Evaluate a rule-based keyword baseline for UIT-ViOCD complaint span extraction.

This script does not train a model. It reads NER JSON records with tokens and
gold BIO tags, predicts BIO tags from complaint keywords, and writes metrics plus
per-sample predictions.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


LABELS = ["O", "B-COMP", "I-COMP"]

PHRASE_PATTERNS = [
    ["giao", "chậm"],
    ["giao", "lâu"],
    ["bị", "lỗi"],
    ["không", "dùng", "được"],
    ["không", "hoạt", "động"],
    ["không", "nhận", "được"],
    ["chưa", "nhận", "được"],
    ["thiếu", "hàng"],
    ["thiếu", "phụ", "kiện"],
    ["không", "đúng"],
    ["sai", "màu"],
    ["sai", "size"],
    ["hoàn", "tiền"],
    ["đổi", "trả"],
    ["bảo", "hành"],
    ["app", "lỗi"],
]

SINGLE_KEYWORDS = {
    "chậm",
    "lâu",
    "lỗi",
    "hỏng",
    "bể",
    "vỡ",
    "móp",
    "rách",
    "trầy",
    "thiếu",
    "sai",
    "nhầm",
    "kém",
    "tệ",
    "thất vọng",
    "dỏm",
    "giả",
    "fake",
    "lag",
    "đứng",
    "crash",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Evaluate rule-based keyword NER baseline for complaint spans."
    )
    parser.add_argument(
        "--test-json",
        default="data/processed/uit_viocd_full_complaint_ner_test.json",
        help="Path to NER test JSON list.",
    )
    parser.add_argument(
        "--output-dir",
        default="outputs/metrics/rule_based_keyword_ner_baseline",
        help="Output directory for metrics and predictions.",
    )
    return parser.parse_args()


def normalize_token(token: str) -> str:
    return token.strip().lower().strip(".,!?;:\"'()[]{}“”‘’")


def load_records(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"Expected JSON list in {path}")
    for idx, record in enumerate(data):
        if not isinstance(record, dict):
            raise ValueError(f"Record {idx} is not an object")
        if "id" not in record or "tokens" not in record or "ner_tags" not in record:
            raise ValueError(f"Record {idx} missing id/tokens/ner_tags")
        if len(record["tokens"]) != len(record["ner_tags"]):
            raise ValueError(
                f"Length mismatch in {record.get('id', idx)}: "
                f"{len(record['tokens'])} tokens vs {len(record['ner_tags'])} tags"
            )
    return data


def find_matches(tokens: Sequence[str]) -> List[Tuple[int, int]]:
    norm_tokens = [normalize_token(t) for t in tokens]
    matches: List[Tuple[int, int]] = []

    for phrase in PHRASE_PATTERNS:
        phrase_len = len(phrase)
        for start in range(0, len(norm_tokens) - phrase_len + 1):
            if norm_tokens[start : start + phrase_len] == phrase:
                matches.append((start, start + phrase_len))

    for idx, token in enumerate(norm_tokens):
        if token in SINGLE_KEYWORDS:
            matches.append((idx, idx + 1))

    return merge_token_spans(matches)


def merge_token_spans(spans: Iterable[Tuple[int, int]]) -> List[Tuple[int, int]]:
    sorted_spans = sorted(set(spans))
    merged: List[Tuple[int, int]] = []
    for start, end in sorted_spans:
        if start >= end:
            continue
        if not merged or start > merged[-1][1]:
            merged.append((start, end))
        else:
            prev_start, prev_end = merged[-1]
            merged[-1] = (prev_start, max(prev_end, end))
    return merged


def spans_to_bio(length: int, spans: Sequence[Tuple[int, int]]) -> List[str]:
    tags = ["O"] * length
    for start, end in spans:
        if start < 0 or end > length or start >= end:
            continue
        if any(tag != "O" for tag in tags[start:end]):
            continue
        tags[start] = "B-COMP"
        for idx in range(start + 1, end):
            tags[idx] = "I-COMP"
    return tags


def extract_entities(tags: Sequence[str]) -> List[Tuple[int, int, str]]:
    entities: List[Tuple[int, int, str]] = []
    start = None
    label = None
    for idx, tag in enumerate(list(tags) + ["O"]):
        if tag.startswith("B-"):
            if start is not None and label is not None:
                entities.append((start, idx, label))
            start = idx
            label = tag[2:]
        elif tag.startswith("I-"):
            current = tag[2:]
            if start is None or label != current:
                if start is not None and label is not None:
                    entities.append((start, idx, label))
                start = idx
                label = current
        else:
            if start is not None and label is not None:
                entities.append((start, idx, label))
            start = None
            label = None
    return entities


def fallback_metrics(
    gold_sequences: List[List[str]], pred_sequences: List[List[str]]
) -> Dict[str, Any]:
    gold_entities = []
    pred_entities = []
    for sample_idx, (gold, pred) in enumerate(zip(gold_sequences, pred_sequences)):
        gold_entities.extend((sample_idx, *entity) for entity in extract_entities(gold))
        pred_entities.extend((sample_idx, *entity) for entity in extract_entities(pred))

    gold_set = set(gold_entities)
    pred_set = set(pred_entities)
    true_positive = len(gold_set & pred_set)
    precision = true_positive / len(pred_set) if pred_set else 0.0
    recall = true_positive / len(gold_set) if gold_set else 0.0
    entity_f1 = (
        2 * precision * recall / (precision + recall)
        if precision + recall > 0
        else 0.0
    )

    per_label_f1 = []
    for label in LABELS:
        tp = fp = fn = 0
        for gold, pred in zip(gold_sequences, pred_sequences):
            for gold_tag, pred_tag in zip(gold, pred):
                if gold_tag == label and pred_tag == label:
                    tp += 1
                elif gold_tag != label and pred_tag == label:
                    fp += 1
                elif gold_tag == label and pred_tag != label:
                    fn += 1
        p = tp / (tp + fp) if tp + fp else 0.0
        r = tp / (tp + fn) if tp + fn else 0.0
        f1 = 2 * p * r / (p + r) if p + r else 0.0
        per_label_f1.append(f1)

    return {
        "entity_precision": precision,
        "entity_recall": recall,
        "entity_f1": entity_f1,
        "token_f1_macro": sum(per_label_f1) / len(per_label_f1),
    }


def compute_metrics(
    gold_sequences: List[List[str]], pred_sequences: List[List[str]]
) -> Dict[str, Any]:
    try:
        from src.evaluation.evaluate_ner import compute_ner_metrics

        metrics = compute_ner_metrics(gold_sequences, pred_sequences, label_list=LABELS)
        return {
            "entity_precision": metrics["entity_precision"],
            "entity_recall": metrics["entity_recall"],
            "entity_f1": metrics["entity_f1"],
            "token_f1_macro": metrics["token_f1_macro"],
            "token_precision_macro": metrics.get("token_precision_macro"),
            "token_recall_macro": metrics.get("token_recall_macro"),
            "entity_classification_report": metrics.get("entity_classification_report"),
            "token_classification_report": metrics.get("token_classification_report"),
        }
    except Exception as exc:
        metrics = fallback_metrics(gold_sequences, pred_sequences)
        metrics["metric_backend_warning"] = (
            f"Used fallback metrics because src.evaluation.evaluate_ner import failed: {exc}"
        )
        return metrics


def label_distribution(sequences: Sequence[Sequence[str]]) -> Dict[str, int]:
    counter = Counter(tag for seq in sequences for tag in seq)
    return {label: int(counter.get(label, 0)) for label in LABELS}


def write_predictions_csv(
    path: Path,
    rows: Sequence[Dict[str, Any]],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "id",
                "tokens",
                "gold_tags",
                "pred_tags",
                "matched_spans",
                "n_gold_tags",
                "n_pred_tags",
                "has_length_mismatch",
                "gold_has_comp",
                "pred_has_comp",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def write_readme(path: Path, metrics: Dict[str, Any], test_json: Path) -> None:
    content = f"""# Rule-based keyword NER baseline

Input test file: `{test_json}`

Method: deterministic Vietnamese complaint keyword and phrase matching over tokenized reviews.

Main metrics:

- Entity Precision: `{metrics['entity_precision']:.4f}`
- Entity Recall: `{metrics['entity_recall']:.4f}`
- Entity F1: `{metrics['entity_f1']:.4f}`
- Token F1 macro: `{metrics['token_f1_macro']:.4f}`
- Samples: `{metrics['samples']}`
- Length mismatch count: `{metrics['length_mismatch_count']}`

This is a simple non-trained baseline for comparison with learned NER models.
"""
    path.write_text(content, encoding="utf-8")


def main() -> None:
    args = parse_args()
    test_json = Path(args.test_json)
    output_dir = Path(args.output_dir)
    metrics_dir = output_dir / "metrics"
    figures_dir = output_dir / "figures"
    metrics_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    records = load_records(test_json)

    gold_sequences: List[List[str]] = []
    pred_sequences: List[List[str]] = []
    prediction_rows: List[Dict[str, Any]] = []
    length_mismatch_count = 0

    for record in records:
        tokens = record["tokens"]
        gold_tags = record["ner_tags"]
        matched_spans = find_matches(tokens)
        pred_tags = spans_to_bio(len(tokens), matched_spans)

        has_mismatch = len(gold_tags) != len(pred_tags)
        if has_mismatch:
            length_mismatch_count += 1

        gold_sequences.append(gold_tags)
        pred_sequences.append(pred_tags)

        prediction_rows.append(
            {
                "id": record["id"],
                "tokens": " ".join(tokens),
                "gold_tags": " ".join(gold_tags),
                "pred_tags": " ".join(pred_tags),
                "matched_spans": json.dumps(matched_spans, ensure_ascii=False),
                "n_gold_tags": len(gold_tags),
                "n_pred_tags": len(pred_tags),
                "has_length_mismatch": has_mismatch,
                "gold_has_comp": any(tag != "O" for tag in gold_tags),
                "pred_has_comp": any(tag != "O" for tag in pred_tags),
            }
        )

    metric_values = compute_metrics(gold_sequences, pred_sequences)
    metrics = {
        "method": "Rule-based keyword span extractor",
        "entity_precision": metric_values["entity_precision"],
        "entity_recall": metric_values["entity_recall"],
        "entity_f1": metric_values["entity_f1"],
        "token_f1_macro": metric_values["token_f1_macro"],
        "gold_label_distribution": label_distribution(gold_sequences),
        "pred_label_distribution": label_distribution(pred_sequences),
        "samples": len(records),
        "length_mismatch_count": length_mismatch_count,
        "test_json": str(test_json),
        "keywords": sorted(SINGLE_KEYWORDS),
        "phrase_patterns": PHRASE_PATTERNS,
    }
    for key in (
        "token_precision_macro",
        "token_recall_macro",
        "metric_backend_warning",
    ):
        if key in metric_values:
            metrics[key] = metric_values[key]

    metrics_path = metrics_dir / "rule_based_ner_metrics.json"
    metrics_path.write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    reports_path = metrics_dir / "rule_based_reports.txt"
    reports = []
    if metric_values.get("entity_classification_report"):
        reports.append("=== ENTITY REPORT ===\n")
        reports.append(metric_values["entity_classification_report"])
    if metric_values.get("token_classification_report"):
        reports.append("\n\n=== TOKEN REPORT ===\n")
        reports.append(metric_values["token_classification_report"])
    if reports:
        reports_path.write_text("".join(reports), encoding="utf-8")

    predictions_path = figures_dir / "rule_based_predictions.csv"
    write_predictions_csv(predictions_path, prediction_rows)

    readme_path = output_dir / "README.md"
    write_readme(readme_path, metrics, test_json)

    print("Rule-based keyword NER baseline completed.")
    print(f"Samples: {metrics['samples']}")
    print(f"Entity Precision: {metrics['entity_precision']:.4f}")
    print(f"Entity Recall: {metrics['entity_recall']:.4f}")
    print(f"Entity F1: {metrics['entity_f1']:.4f}")
    print(f"Token F1 macro: {metrics['token_f1_macro']:.4f}")
    print(f"Gold distribution: {metrics['gold_label_distribution']}")
    print(f"Pred distribution: {metrics['pred_label_distribution']}")
    print(f"Length mismatch count: {length_mismatch_count}")
    print(f"Metrics: {metrics_path}")
    print(f"Predictions: {predictions_path}")
    print(f"README: {readme_path}")


if __name__ == "__main__":
    main()

