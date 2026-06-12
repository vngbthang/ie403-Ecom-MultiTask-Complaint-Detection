"""
Diagnostics for UIT-ViOCD pilot NER smoke training.

This script does not train or modify data. It checks the pilot NER splits,
optional prediction CSV, and relevant training/model source code to explain
common causes of all-O NER predictions.
"""
import argparse
import ast
import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Tuple


VALID_LABELS = {"O", "B-COMP", "I-COMP"}
ORDERED_LABELS = ["O", "B-COMP", "I-COMP"]


def load_json_records(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError(f"{path} must contain a JSON list")
    return data


def get_entities(tags: List[str]) -> List[Tuple[int, int]]:
    entities = []
    start = None
    for idx, tag in enumerate(tags):
        if tag == "B-COMP":
            if start is not None:
                entities.append((start, idx))
            start = idx
        elif tag == "I-COMP":
            if start is None:
                start = idx
        else:
            if start is not None:
                entities.append((start, idx))
                start = None
    if start is not None:
        entities.append((start, len(tags)))
    return entities


def analyze_split(records: List[Dict[str, Any]], split_name: str) -> Dict[str, Any]:
    label_counts = Counter()
    unique_labels = set()
    invalid_records = []
    records_with_comp = 0
    spans_per_record = []
    span_lengths = []

    for idx, record in enumerate(records):
        record_id = record.get("id", f"{split_name}_{idx}")
        tokens = record.get("tokens")
        tags = record.get("ner_tags")

        if not isinstance(tokens, list) or not isinstance(tags, list):
            invalid_records.append(
                {
                    "id": record_id,
                    "error": "tokens/ner_tags must be lists",
                }
            )
            continue

        if len(tokens) != len(tags):
            invalid_records.append(
                {
                    "id": record_id,
                    "error": f"len(tokens)={len(tokens)} != len(ner_tags)={len(tags)}",
                }
            )
            continue

        label_counts.update(tags)
        unique_labels.update(tags)
        has_comp = any(tag in {"B-COMP", "I-COMP"} for tag in tags)
        records_with_comp += int(has_comp)
        entities = get_entities(tags)
        spans_per_record.append(len(entities))
        span_lengths.extend(end - start for start, end in entities)

    total_tokens = sum(label_counts.values())
    comp_tokens = label_counts["B-COMP"] + label_counts["I-COMP"]
    entity_spans = sum(spans_per_record)

    return {
        "records": len(records),
        "total_tokens": total_tokens,
        "count_O": label_counts["O"],
        "count_B-COMP": label_counts["B-COMP"],
        "count_I-COMP": label_counts["I-COMP"],
        "percent_O": round(label_counts["O"] / total_tokens * 100, 4) if total_tokens else 0.0,
        "percent_COMP": round(comp_tokens / total_tokens * 100, 4) if total_tokens else 0.0,
        "records_with_comp": records_with_comp,
        "records_without_comp": len(records) - records_with_comp,
        "entity_spans": entity_spans,
        "avg_span_length": round(sum(span_lengths) / len(span_lengths), 4) if span_lengths else 0.0,
        "max_span_length": max(span_lengths) if span_lengths else 0,
        "unique_labels": sorted(unique_labels),
        "labels_outside_schema": sorted(unique_labels - VALID_LABELS),
        "all_token_tag_lengths_match": len(invalid_records) == 0,
        "invalid_records": invalid_records,
    }


def analyze_predictions(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {
            "path": str(path),
            "exists": False,
            "error": "Predictions CSV not found",
            "pred_label_counts": {label: 0 for label in ORDERED_LABELS},
            "gold_label_counts": {label: 0 for label in ORDERED_LABELS},
            "rows_with_pred_comp": 0,
            "rows_with_gold_comp": 0,
            "examples_gold_comp_pred_all_o": [],
        }

    pred_counts = Counter()
    gold_counts = Counter()
    rows = 0
    rows_with_pred_comp = 0
    rows_with_gold_comp = 0
    examples = []

    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        required = {"gold_tags", "pred_tags"}
        missing = required - set(reader.fieldnames or [])
        if missing:
            return {
                "path": str(path),
                "exists": True,
                "error": f"Missing columns: {sorted(missing)}",
                "columns": reader.fieldnames or [],
            }

        for row in reader:
            rows += 1
            gold_tags = str(row.get("gold_tags", "")).split()
            pred_tags = str(row.get("pred_tags", "")).split()
            gold_counts.update(gold_tags)
            pred_counts.update(pred_tags)

            gold_has_comp = any(tag in {"B-COMP", "I-COMP"} for tag in gold_tags)
            pred_has_comp = any(tag in {"B-COMP", "I-COMP"} for tag in pred_tags)
            rows_with_gold_comp += int(gold_has_comp)
            rows_with_pred_comp += int(pred_has_comp)

            if gold_has_comp and not pred_has_comp and len(examples) < 5:
                examples.append(
                    {
                        "index": row.get("index", rows - 1),
                        "gold_tags": gold_tags,
                        "pred_tags": pred_tags,
                        "correct": row.get("correct", ""),
                    }
                )

    return {
        "path": str(path),
        "exists": True,
        "rows": rows,
        "pred_label_counts": {label: pred_counts[label] for label in ORDERED_LABELS},
        "gold_label_counts": {label: gold_counts[label] for label in ORDERED_LABELS},
        "rows_with_pred_comp": rows_with_pred_comp,
        "rows_with_gold_comp": rows_with_gold_comp,
        "examples_gold_comp_pred_all_o": examples,
    }


def find_assignment_dict(source: str, name: str) -> Dict[str, Any]:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return {}

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    try:
                        value = ast.literal_eval(node.value)
                    except Exception:
                        return {"raw": ast.get_source_segment(source, node.value)}
                    if isinstance(value, dict):
                        return value
    return {}


def inspect_training_code(train_path: Path, model_path: Path) -> Dict[str, Any]:
    train_source = train_path.read_text(encoding="utf-8-sig") if train_path.exists() else ""
    model_source = model_path.read_text(encoding="utf-8-sig") if model_path.exists() else ""

    label2id = find_assignment_dict(train_source, "LABEL2ID")
    id2label_match = re.search(r"ID2LABEL\s*,\s*LABEL_LIST", train_source)

    training_check = {
        "train_path": str(train_path),
        "model_path": str(model_path),
        "label2id": label2id,
        "id2label_source": "src.evaluation.evaluate_ner.ID2LABEL" if id2label_match else "not_detected",
        "loss_ignore_index_minus_100": "ignore_index=-100" in train_source or "ignore_index=-100" in model_source,
        "class_weight_detected": bool(re.search(r"(class_weight|weight\s*=)", train_source)),
        "subword_alignment": "first_subword_only" if "label_ids.extend([-100] * (len(w_ids) - 1))" in train_source else "unknown",
        "model_num_labels_default": 3 if "num_ner_tags: int = 3" in model_source else "unknown",
        "model_classifier_uses_num_labels": "nn.Linear(hidden_size, num_ner_tags)" in model_source,
        "evaluate_uses_model_predict": "predictions = model.predict(input_ids, attention_mask)" in train_source,
        "predict_filters_by_attention_mask_only": "attention_mask[b, pos].item() == 1" in model_source,
        "possible_prediction_decode_misalignment": (
            "predictions = model.predict(input_ids, attention_mask)" in train_source
            and "attention_mask[b, pos].item() == 1" in model_source
        ),
    }
    return training_check


def build_possible_causes(report: Dict[str, Any]) -> List[str]:
    causes = []
    train = report["dataset_label_distribution"].get("train", {})
    pred = report.get("prediction_distribution", {})
    code = report.get("train_script_check", {})

    if train:
        percent_comp = train.get("percent_COMP", 0.0)
        if percent_comp < 30:
            causes.append(
                f"Train split imbalanced: COMP tokens only {percent_comp:.2f}% of labeled tokens; unweighted CE can favor O."
            )

    if pred.get("exists") and pred.get("rows_with_pred_comp", 0) == 0 and pred.get("rows_with_gold_comp", 0) > 0:
        causes.append("Prediction CSV shows zero rows with predicted COMP while gold has COMP entities.")

    if code.get("possible_prediction_decode_misalignment"):
        causes.append(
            "Evaluation decode is likely misaligned: train labels only first subword, but model.predict returns special tokens and all subwords using attention_mask only."
        )

    if not code.get("class_weight_detected"):
        causes.append("No class weights detected in the NER loss; minority B/I-COMP labels are not upweighted.")

    if not causes:
        causes.append("No obvious schema issue detected; inspect predictions and training dynamics manually.")

    return causes


def build_recommended_actions(report: Dict[str, Any]) -> List[str]:
    actions = [
        "Fix/evaluate prediction decoding so predicted tags are selected at the same positions as non -100 gold labels.",
        "Run a tiny overfit test on 5-10 records after decode fix to verify the model can learn B-COMP/I-COMP.",
        "Consider weighted CrossEntropy or focal loss if predictions remain all O after decode is corrected.",
        "Log train-time per-label prediction counts after each epoch before changing architecture.",
    ]
    pred = report.get("prediction_distribution", {})
    if not pred.get("exists"):
        actions.insert(0, "Sync the Kaggle predictions CSV to the expected path, or rerun this script with --predictions-csv.")
    return actions


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def markdown_table(headers: List[str], rows: List[List[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(lines)


def write_markdown(path: Path, report: Dict[str, Any]) -> None:
    dist = report["dataset_label_distribution"]
    pred = report["prediction_distribution"]
    code = report["train_script_check"]

    dataset_rows = []
    for split in ["train", "val", "test"]:
        item = dist[split]
        dataset_rows.append(
            [
                split,
                item["records"],
                item["total_tokens"],
                item["count_O"],
                item["count_B-COMP"],
                item["count_I-COMP"],
                f"{item['percent_O']:.2f}",
                f"{item['percent_COMP']:.2f}",
                item["records_with_comp"],
                item["records_without_comp"],
                item["entity_spans"],
                item["avg_span_length"],
                item["max_span_length"],
            ]
        )

    pred_rows = []
    if pred.get("exists"):
        pred_rows = [
            ["gold", pred["gold_label_counts"].get("O", 0), pred["gold_label_counts"].get("B-COMP", 0), pred["gold_label_counts"].get("I-COMP", 0), pred.get("rows_with_gold_comp", 0)],
            ["pred", pred["pred_label_counts"].get("O", 0), pred["pred_label_counts"].get("B-COMP", 0), pred["pred_label_counts"].get("I-COMP", 0), pred.get("rows_with_pred_comp", 0)],
        ]
    else:
        pred_rows = [["missing", pred.get("error", ""), "", "", ""]]

    lines = [
        "# UIT-ViOCD Pilot 100 NER Debug Report",
        "",
        "## Summary",
        f"- Train COMP token percent: {dist['train']['percent_COMP']:.2f}%",
        f"- Test COMP token percent: {dist['test']['percent_COMP']:.2f}%",
        f"- Predictions CSV exists: {pred.get('exists')}",
        f"- Possible decode misalignment: {code.get('possible_prediction_decode_misalignment')}",
        f"- Class weight detected: {code.get('class_weight_detected')}",
        "",
        "## Dataset Label Distribution",
        markdown_table(
            [
                "split",
                "records",
                "tokens",
                "O",
                "B-COMP",
                "I-COMP",
                "%O",
                "%COMP",
                "with_comp",
                "without_comp",
                "spans",
                "avg_span_len",
                "max_span_len",
            ],
            dataset_rows,
        ),
        "",
        "## Prediction Distribution",
        markdown_table(["type", "O", "B-COMP", "I-COMP", "rows_with_comp"], pred_rows),
        "",
        "## Train Script Check",
        f"- label2id: `{code.get('label2id')}`",
        f"- id2label source: `{code.get('id2label_source')}`",
        f"- loss ignore_index=-100: `{code.get('loss_ignore_index_minus_100')}`",
        f"- class weight: `{code.get('class_weight_detected')}`",
        f"- subword alignment: `{code.get('subword_alignment')}`",
        f"- model num labels default: `{code.get('model_num_labels_default')}`",
        f"- classifier uses num labels: `{code.get('model_classifier_uses_num_labels')}`",
        f"- evaluate uses model.predict: `{code.get('evaluate_uses_model_predict')}`",
        f"- predict filters by attention mask only: `{code.get('predict_filters_by_attention_mask_only')}`",
        "",
        "## Examples: Gold COMP But Pred All O",
    ]

    examples = pred.get("examples_gold_comp_pred_all_o", [])
    if examples:
        for ex in examples:
            lines.extend(
                [
                    f"### index {ex.get('index')}",
                    f"- gold_tags: `{' '.join(ex.get('gold_tags', []))}`",
                    f"- pred_tags: `{' '.join(ex.get('pred_tags', []))}`",
                    "",
                ]
            )
    else:
        lines.append("- No examples available.")

    lines.extend(
        [
            "",
            "## Possible Causes",
            *[f"- {cause}" for cause in report["possible_causes"]],
            "",
            "## Recommended Next Actions",
            *[f"- {action}" for action in report["recommended_next_actions"]],
            "",
        ]
    )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Debug pilot 100 PhoBERT NER training data and predictions")
    parser.add_argument("--train-json", default="data/processed/uit_viocd_pilot_100_ner_train.json")
    parser.add_argument("--val-json", default="data/processed/uit_viocd_pilot_100_ner_val.json")
    parser.add_argument("--test-json", default="data/processed/uit_viocd_pilot_100_ner_test.json")
    parser.add_argument(
        "--predictions-csv",
        default="outputs/metrics/uit_viocd_pilot_100_phobert_ner_3epoch/figures/phobert_ner_single_task_predictions.csv",
    )
    parser.add_argument("--output-dir", default="outputs/metrics/uit_viocd_pilot_100_ner_debug")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    train_path = Path(args.train_json)
    val_path = Path(args.val_json)
    test_path = Path(args.test_json)
    predictions_path = Path(args.predictions_csv)

    split_paths = {
        "train": train_path,
        "val": val_path,
        "test": test_path,
    }

    missing = [str(path) for path in split_paths.values() if not path.exists()]
    if missing:
        print("Missing required dataset files:")
        for path in missing:
            print(f"- {path}")
        return 1

    records_by_split = {split: load_json_records(path) for split, path in split_paths.items()}
    dataset_distribution = {
        split: analyze_split(records, split)
        for split, records in records_by_split.items()
    }

    all_unique_labels = sorted(
        {
            label
            for split_info in dataset_distribution.values()
            for label in split_info["unique_labels"]
        }
    )
    labels_outside_schema = sorted(set(all_unique_labels) - VALID_LABELS)
    all_lengths_match = all(
        split_info["all_token_tag_lengths_match"]
        for split_info in dataset_distribution.values()
    )

    prediction_distribution = analyze_predictions(predictions_path)
    train_script_check = inspect_training_code(
        Path("src/training/train_phobert_ner.py"),
        Path("src/models/phobert_token_classifier.py"),
    )

    report = {
        "inputs": {
            "train_json": str(train_path),
            "val_json": str(val_path),
            "test_json": str(test_path),
            "predictions_csv": str(predictions_path),
        },
        "dataset_label_distribution": dataset_distribution,
        "entity_span_distribution": {
            split: {
                "entity_spans": info["entity_spans"],
                "avg_span_length": info["avg_span_length"],
                "max_span_length": info["max_span_length"],
            }
            for split, info in dataset_distribution.items()
        },
        "label_schema_check": {
            "unique_labels": all_unique_labels,
            "labels_outside_schema": labels_outside_schema,
            "all_token_tag_lengths_match": all_lengths_match,
        },
        "prediction_distribution": prediction_distribution,
        "train_script_check": train_script_check,
    }
    report["possible_causes"] = build_possible_causes(report)
    report["recommended_next_actions"] = build_recommended_actions(report)

    json_path = output_dir / "debug_report.json"
    md_path = output_dir / "debug_report.md"
    write_json(json_path, report)
    write_markdown(md_path, report)

    print("=" * 72)
    print("UIT-ViOCD Pilot 100 NER Debug")
    print("=" * 72)
    for split in ["train", "val", "test"]:
        item = dataset_distribution[split]
        print(
            f"{split}: records={item['records']}, tokens={item['total_tokens']}, "
            f"O={item['count_O']}, B={item['count_B-COMP']}, I={item['count_I-COMP']}, "
            f"COMP%={item['percent_COMP']:.2f}, records_with_comp={item['records_with_comp']}"
        )

    if prediction_distribution.get("exists"):
        print("\nPrediction CSV:")
        print(f"rows={prediction_distribution.get('rows')}")
        print(f"gold={prediction_distribution.get('gold_label_counts')}")
        print(f"pred={prediction_distribution.get('pred_label_counts')}")
        print(f"rows_with_gold_comp={prediction_distribution.get('rows_with_gold_comp')}")
        print(f"rows_with_pred_comp={prediction_distribution.get('rows_with_pred_comp')}")
    else:
        print(f"\nPrediction CSV missing: {predictions_path}")

    print("\nTrain/model check:")
    print(f"label2id={train_script_check.get('label2id')}")
    print(f"ignore_index=-100={train_script_check.get('loss_ignore_index_minus_100')}")
    print(f"class_weight={train_script_check.get('class_weight_detected')}")
    print(f"subword_alignment={train_script_check.get('subword_alignment')}")
    print(f"model_num_labels={train_script_check.get('model_num_labels_default')}")
    print(f"possible_decode_misalignment={train_script_check.get('possible_prediction_decode_misalignment')}")

    print(f"\nSaved JSON report: {json_path}")
    print(f"Saved Markdown report: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
