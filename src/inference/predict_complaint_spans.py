"""Inference utilities for UIT-ViOCD complaint span extraction.

The model is a PhoBERT token classifier trained with BIO labels:
O, B-COMP, I-COMP. Inference mirrors the training-time alignment by assigning
one prediction to the first subword of each whitespace token.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import torch
from transformers import AutoTokenizer

from src.models.phobert_token_classifier import PhobertTokenClassifier


DEFAULT_MODEL_NAME = "vinai/phobert-base-v2"
DEFAULT_CHECKPOINT_PATH = (
    "outputs/metrics/demo_full_unweighted_phobert_ner_5epoch/checkpoints/"
    "ner_single_task_epoch_5.pt"
)
DEFAULT_LABEL2ID = {"O": 0, "B-COMP": 1, "I-COMP": 2}
DEFAULT_ID2LABEL = {0: "O", 1: "B-COMP", 2: "I-COMP"}


def load_model(
    checkpoint_path: str | Path,
    model_name: str = DEFAULT_MODEL_NAME,
    device: str | torch.device | None = None,
) -> tuple[PhobertTokenClassifier, Any, dict[int, str], torch.device]:
    """Load tokenizer and PhoBERT NER checkpoint for inference."""
    checkpoint_path = Path(checkpoint_path)
    if not checkpoint_path.exists():
        raise FileNotFoundError(f"Checkpoint not found: {checkpoint_path}")

    resolved_device = torch.device(
        device if device is not None else ("cuda" if torch.cuda.is_available() else "cpu")
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
    model = PhobertTokenClassifier(num_ner_tags=3, model_name=model_name)

    checkpoint = torch.load(checkpoint_path, map_location=resolved_device)
    if not isinstance(checkpoint, dict) or "model_state_dict" not in checkpoint:
        raise ValueError(
            "Invalid checkpoint format. Expected a dict with key 'model_state_dict'."
        )

    model.load_state_dict(checkpoint["model_state_dict"])
    model.to(resolved_device)
    model.eval()
    return model, tokenizer, DEFAULT_ID2LABEL.copy(), resolved_device


def tokenize_words(text: str) -> list[str]:
    """Whitespace tokenization for display and word-level BIO output."""
    if not text or not text.strip():
        return []
    return text.strip().split()


def _build_model_inputs(
    tokens: list[str],
    tokenizer: Any,
    max_len: int,
) -> tuple[torch.Tensor, torch.Tensor, list[int]]:
    """Create model inputs and remember first-subword positions per token."""
    cls_id = tokenizer.cls_token_id
    sep_id = tokenizer.sep_token_id
    pad_id = tokenizer.pad_token_id

    if cls_id is None or sep_id is None or pad_id is None:
        raise ValueError("Tokenizer must define cls_token_id, sep_token_id, and pad_token_id.")

    input_ids = [cls_id]
    first_subword_positions: list[int] = []

    for word in tokens:
        word_tokens = tokenizer.tokenize(word)
        if not word_tokens:
            continue
        word_ids = tokenizer.convert_tokens_to_ids(word_tokens)
        if not word_ids:
            continue

        # Reserve one slot for final SEP.
        if len(input_ids) + len(word_ids) + 1 > max_len:
            break

        first_subword_positions.append(len(input_ids))
        input_ids.extend(word_ids)

    input_ids.append(sep_id)
    attention_mask = [1] * len(input_ids)

    if len(input_ids) < max_len:
        pad_len = max_len - len(input_ids)
        input_ids.extend([pad_id] * pad_len)
        attention_mask.extend([0] * pad_len)

    return (
        torch.tensor([input_ids], dtype=torch.long),
        torch.tensor([attention_mask], dtype=torch.long),
        first_subword_positions,
    )


def predict_token_labels(
    text: str,
    model: PhobertTokenClassifier,
    tokenizer: Any,
    id2label: dict[int, str],
    device: torch.device | str,
    max_len: int = 256,
) -> tuple[list[str], list[str]]:
    """Predict one BIO label for each whitespace token in text."""
    tokens = tokenize_words(text)
    if not tokens:
        return [], []

    if max_len < 4:
        raise ValueError("max_len must be at least 4.")

    input_ids, attention_mask, first_positions = _build_model_inputs(tokens, tokenizer, max_len)
    input_ids = input_ids.to(device)
    attention_mask = attention_mask.to(device)

    with torch.no_grad():
        outputs = model.phobert(input_ids=input_ids, attention_mask=attention_mask)
        sequence_output = model.dropout(outputs.last_hidden_state)
        logits = model.ner_classifier(sequence_output)
        pred_ids = logits.argmax(dim=-1)[0].detach().cpu().tolist()

    kept_tokens = tokens[: len(first_positions)]
    labels = [id2label.get(pred_ids[pos], "O") for pos in first_positions]
    return kept_tokens, labels


def bio_to_spans(tokens: list[str], labels: list[str]) -> list[dict[str, int | str]]:
    """Convert BIO token labels into complaint spans."""
    spans: list[dict[str, int | str]] = []
    current_start: int | None = None

    def close_span(end_idx: int) -> None:
        nonlocal current_start
        if current_start is not None and current_start < end_idx:
            spans.append(
                {
                    "text": " ".join(tokens[current_start:end_idx]),
                    "start_token": current_start,
                    "end_token": end_idx,
                }
            )
        current_start = None

    for idx, label in enumerate(labels):
        if label == "B-COMP":
            close_span(idx)
            current_start = idx
        elif label == "I-COMP":
            if current_start is None:
                current_start = idx
        else:
            close_span(idx)

    close_span(len(labels))
    return spans


def predict_spans(
    text: str,
    checkpoint_path: str | Path,
    model_name: str = DEFAULT_MODEL_NAME,
    max_len: int = 256,
) -> dict[str, Any]:
    """Load model, predict BIO labels, and return complaint spans."""
    model, tokenizer, id2label, device = load_model(checkpoint_path, model_name=model_name)
    tokens, labels = predict_token_labels(
        text=text,
        model=model,
        tokenizer=tokenizer,
        id2label=id2label,
        device=device,
        max_len=max_len,
    )
    return {
        "text": text,
        "tokens": tokens,
        "labels": labels,
        "spans": bio_to_spans(tokens, labels),
    }


def _print_prediction(result: dict[str, Any]) -> None:
    print("Input review:")
    print(result["text"])
    print()
    print("Complaint spans:")
    if result["spans"]:
        for span in result["spans"]:
            print(f"- {span['text']} [{span['start_token']}:{span['end_token']}]")
    else:
        print("- No complaint span detected.")
    print()
    print("Token/BIO labels:")
    for idx, (token, label) in enumerate(zip(result["tokens"], result["labels"])):
        print(f"{idx:>3}  {token:<30}  {label}")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Predict UIT-ViOCD complaint spans.")
    parser.add_argument(
        "--checkpoint",
        default=DEFAULT_CHECKPOINT_PATH,
        help="Path to PhoBERT NER checkpoint.",
    )
    parser.add_argument(
        "--text",
        required=True,
        help="Vietnamese review text.",
    )
    parser.add_argument("--model-name", default=DEFAULT_MODEL_NAME)
    parser.add_argument("--max-len", type=int, default=256)
    args = parser.parse_args()

    try:
        result = predict_spans(
            text=args.text,
            checkpoint_path=args.checkpoint,
            model_name=args.model_name,
            max_len=args.max_len,
        )
    except Exception as exc:
        raise SystemExit(f"Prediction failed: {exc}") from exc

    _print_prediction(result)


if __name__ == "__main__":
    main()
