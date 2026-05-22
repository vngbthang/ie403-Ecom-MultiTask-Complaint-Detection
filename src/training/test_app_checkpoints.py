import os
import sys
from pathlib import Path

import torch
from transformers import AutoTokenizer

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.models.multitask_model import PhobertCRFMultiTask
from src.utils.utils import clean_vietnamese_text


MODEL_NAME = "vinai/phobert-base-v2"
ID2LABEL = {0: "O", 1: "B-COMP", 2: "I-COMP"}
SAMPLES = [
    "Hàng bình thường, đóng gói ổn",
    "Giao hàng quá chậm, sản phẩm bị móp méo và shop phản hồi rất tệ",
    "Shop giao sai size, nhắn tin không trả lời",
]


def encode_like_training(text, tokenizer, max_len=256):
    words = text.split()
    input_ids = [tokenizer.cls_token_id]
    for word in words:
        word_tokens = tokenizer.tokenize(word)
        if not word_tokens:
            continue
        input_ids.extend(tokenizer.convert_tokens_to_ids(word_tokens))
    input_ids.append(tokenizer.sep_token_id)

    if len(input_ids) > max_len:
        input_ids = input_ids[: max_len - 1] + [tokenizer.sep_token_id]

    attention_mask = [1] * len(input_ids)
    pad_len = max_len - len(input_ids)
    if pad_len > 0:
        input_ids.extend([tokenizer.pad_token_id] * pad_len)
        attention_mask.extend([0] * pad_len)

    return torch.tensor([input_ids]), torch.tensor([attention_mask])


def run_checkpoint(checkpoint_path, tokenizer):
    model = PhobertCRFMultiTask(num_classes=2, num_ner_tags=3)
    checkpoint = torch.load(checkpoint_path, map_location="cpu", weights_only=False)
    model.load_state_dict(checkpoint["model_state_dict"], strict=True)
    model.eval()

    print("=" * 80)
    print(f"CHECKPOINT: {checkpoint_path}")
    print("=" * 80)

    with torch.no_grad():
        for text in SAMPLES:
            input_ids, attention_mask = encode_like_training(text, tokenizer)
            cls_logits, ner_predictions = model(input_ids=input_ids, attention_mask=attention_mask)
            cls_id = int(cls_logits.argmax(-1).item())
            valid_len = int(attention_mask[0].sum().item())
            tokens = tokenizer.convert_ids_to_tokens(input_ids[0][:valid_len].tolist())
            tags = [ID2LABEL.get(x, "O") for x in ner_predictions[0][:valid_len]]

            print(f"TEXT: {text}")
            print(f"CLS : {cls_id} ({'Khiếu nại' if cls_id == 1 else 'Bình thường'})")
            print(f"TOKS: {tokens}")
            print(f"TAGS: {tags}")
            print("-" * 80)


def main():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=False)
    base = Path("checkpoints")
    checkpoints = [base / "checkpoint_epoch_1.pt", base / "checkpoint_epoch_2.pt"]
    for checkpoint_path in checkpoints:
        if checkpoint_path.exists():
            run_checkpoint(str(checkpoint_path), tokenizer)
        else:
            print(f"Missing: {checkpoint_path}")


if __name__ == "__main__":
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    main()
