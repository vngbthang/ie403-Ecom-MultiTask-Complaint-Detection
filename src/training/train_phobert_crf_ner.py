"""
Train PhoBERT + CRF cho NER single-task.
Model: PhobertCRFNer (PhoBERT + Linear + CRF)
Dataset: data/processed/ner_train.json, ner_test.json

Output:
    outputs/metrics/phobert_crf_ner_single_task.json
    outputs/metrics/phobert_crf_ner_single_task_entity_report.txt
    outputs/metrics/phobert_crf_ner_single_task_token_report.txt
    outputs/metrics/phobert_crf_ner_single_task_history.json
"""
import os
import sys
import json
import argparse
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer
from tqdm import tqdm

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.models.phobert_crf_ner import PhobertCRFNer
from src.evaluation.evaluate_ner import (
    compute_ner_metrics,
    save_ner_metrics_json,
    save_ner_reports,
    ID2LABEL,
)

# =============================================================================
# Dataset — cùng logic sub-word alignment với train_phobert_ner.py
# =============================================================================

class NERDataset(Dataset):
    """
    Dataset cho PhoBERT + CRF NER single-task.

    Load tu JSON: [{"tokens": [...], "ner_tags": [...]}]

    Sub-word alignment:
        - Tokenizer bat dau bang <s>, ket thuc bang </s>
        - Moi word tokenize thanh 1 hoac nhieu subwords
        - Subword dau tien: giu nhan that
        - Subword con lai: -100
    """

    LABEL2ID = {"O": 0, "B-COMP": 1, "I-COMP": 2}

    def __init__(self, json_path: str, tokenizer, max_len: int = 256):
        with open(json_path, encoding="utf-8-sig") as f:
            self.records = json.load(f)
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx: int):
        item = self.records[idx]
        tokens = item.get("tokens", [])
        tags = item.get("ner_tags", [])

        if not tokens or len(tokens) != len(tags):
            return self.__getitem__((idx + 1) % len(self))

        input_ids = [self.tokenizer.cls_token_id]
        label_ids = [-100]

        for word, tag in zip(tokens, tags):
            word_tokens = self.tokenizer.tokenize(word)
            if not word_tokens:
                continue

            w_ids = self.tokenizer.convert_tokens_to_ids(word_tokens)
            input_ids.extend(w_ids)

            label_id = self.LABEL2ID.get(tag, 0)
            label_ids.append(label_id)
            label_ids.extend([-100] * (len(w_ids) - 1))

        input_ids.append(self.tokenizer.sep_token_id)
        label_ids.append(-100)

        if len(input_ids) > self.max_len:
            input_ids = input_ids[: self.max_len - 1] + [self.tokenizer.sep_token_id]
            label_ids = label_ids[: self.max_len - 1] + [-100]

        attention_mask = [1] * len(input_ids)
        pad_len = self.max_len - len(input_ids)
        if pad_len > 0:
            input_ids.extend([self.tokenizer.pad_token_id] * pad_len)
            attention_mask.extend([0] * pad_len)
            label_ids.extend([-100] * pad_len)

        return {
            "input_ids": torch.tensor(input_ids, dtype=torch.long),
            "attention_mask": torch.tensor(attention_mask, dtype=torch.long),
            "ner_labels": torch.tensor(label_ids, dtype=torch.long),
            "tokens": tokens,
            "tags": tags,
        }


def ner_collate_fn(batch):
    input_ids = torch.stack([item["input_ids"] for item in batch])
    attention_mask = torch.stack([item["attention_mask"] for item in batch])
    ner_labels = torch.stack([item["ner_labels"] for item in batch])
    tokens = [item["tokens"] for item in batch]
    tags = [item["tags"] for item in batch]
    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "ner_labels": ner_labels,
        "tokens": tokens,
        "tags": tags,
    }


# =============================================================================
# Evaluation
# =============================================================================

def evaluate(model, dataloader, device="cpu"):
    """
    Danh gia tren toan bo dataloader.
    Tra ve (y_true_str, y_pred_str, metrics_dict)
    """
    model.eval()
    y_true_str = []
    y_pred_str = []

    with torch.no_grad():
        for batch in dataloader:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            ner_labels = batch["ner_labels"].to(device)

            # Decode bằng CRF
            predictions = model.predict(input_ids, attention_mask)

            # Decode ground truth strings, bo qua -100
            batch_size = len(predictions)
            seq_len = ner_labels.size(1)

            for b in range(batch_size):
                gold_seq = []
                pred_seq = []
                pos_in_pred = 0

                for pos in range(seq_len):
                    gold_id = ner_labels[b, pos].item()
                    if gold_id != -100:
                        gold_seq.append(ID2LABEL.get(gold_id, "O"))
                        if pos_in_pred < len(predictions[b]):
                            pred_seq.append(ID2LABEL.get(predictions[b][pos_in_pred], "O"))
                            pos_in_pred += 1

                if gold_seq:
                    y_true_str.append(gold_seq)
                    y_pred_str.append(pred_seq)

    if not y_true_str:
        return [], [], {
            "entity_precision": 0.0,
            "entity_recall": 0.0,
            "entity_f1": 0.0,
            "token_precision_macro": 0.0,
            "token_recall_macro": 0.0,
            "token_f1_macro": 0.0,
        }

    metrics = compute_ner_metrics(y_true_str, y_pred_str)
    return y_true_str, y_pred_str, metrics


# =============================================================================
# Training
# =============================================================================

def train(
    train_json: str,
    test_json: str,
    output_dir: str = "outputs",
    num_epochs: int = 5,
    batch_size: int = 8,
    learning_rate: float = 2e-5,
    weight_decay: float = 0.01,
    max_len: int = 256,
    device: str = None,
    resume_checkpoint: str = None,
    disable_tqdm: bool = False,
    max_steps_per_epoch: int = None,
    eval_every: int = 1,
):
    """
    Huấn luyện PhoBERT + CRF cho NER single-task.

    Args:
        train_json: Đường dẫn ner_train.json
        test_json: Đường dẫn ner_test.json
        output_dir: Thư mục lưu kết quả
        num_epochs: Số epoch
        batch_size: Kích thước batch
        learning_rate: Tốc độ học
        weight_decay: Hệ số giảm tốc độ học
        max_len: Độ dài tối đa chuỗi
        device: 'cuda' hoặc 'cpu'
        resume_checkpoint: Đường dẫn checkpoint để resume
        disable_tqdm: Tắt tqdm
        max_steps_per_epoch: Giới hạn số step mỗi epoch (debug)
        eval_every: Đánh giá sau mỗi eval_every epochs
    """
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"

    print(f"Device: {device}")

    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        "vinai/phobert-base-v2",
        use_fast=False,
    )

    # Datasets
    print(f"\n[LOAD] Training data: {train_json}")
    train_dataset = NERDataset(train_json, tokenizer, max_len=max_len)
    print(f"[LOAD] Test data: {test_json}")
    test_dataset = NERDataset(test_json, tokenizer, max_len=max_len)
    print(f"  Train samples: {len(train_dataset)}")
    print(f"  Test samples : {len(test_dataset)}")

    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=0,
        collate_fn=ner_collate_fn,
    )
    test_loader = DataLoader(
        test_dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=0,
        collate_fn=ner_collate_fn,
    )

    # Model
    model = PhobertCRFNer(num_ner_tags=3)
    model.to(device)

    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=learning_rate,
        weight_decay=weight_decay,
    )

    start_epoch = 0
    best_f1 = 0.0
    if resume_checkpoint:
        print(f"Resuming from: {resume_checkpoint}")
        ckpt = torch.load(resume_checkpoint, map_location=device)
        model.load_state_dict(ckpt["model_state_dict"])
        optimizer.load_state_dict(ckpt["optimizer_state_dict"])
        start_epoch = int(ckpt.get("epoch", 0))
        best_f1 = float(ckpt.get("best_entity_f1", 0.0))

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    metrics_dir = output_dir / "metrics"
    figures_dir = output_dir / "figures"
    metrics_dir.mkdir(exist_ok=True)
    figures_dir.mkdir(exist_ok=True)

    print(f"\nEpochs: {num_epochs} | Batch size: {batch_size} | LR: {learning_rate}")
    print(f"Resume from epoch: {start_epoch} | Best F1: {best_f1:.4f}")
    print("=" * 60)

    all_epoch_metrics = []

    for epoch in range(start_epoch, start_epoch + num_epochs):
        model.train()
        total_loss = 0.0
        num_batches = 0

        pbar = train_loader if disable_tqdm else tqdm(
            train_loader,
            desc=f"Epoch {epoch + 1}/{start_epoch + num_epochs}"
        )

        for step_idx, batch in enumerate(pbar):
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            ner_labels = batch["ner_labels"].to(device)

            optimizer.zero_grad()
            loss = model(input_ids, attention_mask, ner_labels)[0]
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()

            total_loss += loss.item()
            num_batches += 1

            if not disable_tqdm:
                pbar.set_postfix({"loss": f"{loss.item():.4f}"})

            if max_steps_per_epoch is not None and step_idx >= max_steps_per_epoch:
                break

        avg_loss = total_loss / max(num_batches, 1)
        print(f"\nEpoch {epoch + 1}/{start_epoch + num_epochs} | Avg Loss: {avg_loss:.4f}")

        # Đánh giá
        if (epoch + 1) % eval_every == 0 or epoch == start_epoch + num_epochs - 1:
            y_true, y_pred, test_metrics = evaluate(model, test_loader, device)

            print(f"  Test - Entity P: {test_metrics['entity_precision']:.4f}  "
                  f"R: {test_metrics['entity_recall']:.4f}  "
                  f"F1: {test_metrics['entity_f1']:.4f}")
            print(f"  Test - Token F1 (macro): {test_metrics['token_f1_macro']:.4f}")

            test_metrics["epoch"] = epoch + 1
            test_metrics["avg_loss"] = avg_loss
            all_epoch_metrics.append(test_metrics)

            # Lưu metrics JSON cho epoch này
            epoch_metrics_dir = metrics_dir / f"crf_epoch_{epoch + 1}"
            epoch_metrics_dir.mkdir(exist_ok=True)
            save_ner_metrics_json(test_metrics, str(epoch_metrics_dir))
            save_ner_reports(test_metrics, str(epoch_metrics_dir))

            # Cập nhật best model
            if test_metrics["entity_f1"] >= best_f1:
                best_f1 = test_metrics["entity_f1"]
                print(f"  [BEST] New best Entity F1: {best_f1:.4f}")

                # Ghi đè file chính
                final_metrics = {
                    "epoch": epoch + 1,
                    "entity_precision": test_metrics["entity_precision"],
                    "entity_recall": test_metrics["entity_recall"],
                    "entity_f1": test_metrics["entity_f1"],
                    "token_precision_macro": test_metrics["token_precision_macro"],
                    "token_recall_macro": test_metrics["token_recall_macro"],
                    "token_f1_macro": test_metrics["token_f1_macro"],
                    "avg_loss": avg_loss,
                }
                final_path = metrics_dir / "phobert_crf_ner_single_task.json"
                with open(final_path, "w", encoding="utf-8") as f:
                    json.dump(final_metrics, f, ensure_ascii=False, indent=2)
                print(f"  [SAVE] Best metrics: {final_path}")

                # Entity report
                entity_path = metrics_dir / "phobert_crf_ner_single_task_entity_report.txt"
                with open(entity_path, "w", encoding="utf-8") as f:
                    f.write(test_metrics["entity_classification_report"])

                # Token report
                token_path = metrics_dir / "phobert_crf_ner_single_task_token_report.txt"
                with open(token_path, "w", encoding="utf-8") as f:
                    f.write(test_metrics["token_classification_report"])

                # Predictions CSV
                import pandas as pd
                pred_path = figures_dir / "phobert_crf_ner_single_task_predictions.csv"
                records = []
                for i in range(min(len(y_true), len(y_pred))):
                    records.append({
                        "index": i,
                        "gold_tags": " ".join(y_true[i]),
                        "pred_tags": " ".join(y_pred[i]),
                        "correct": (y_true[i] == y_pred[i]),
                    })
                pd.DataFrame(records).to_csv(pred_path, index=False, encoding="utf-8-sig")
                print(f"  [SAVE] Predictions: {pred_path}")

            # Ve entity breakdown chart
            from src.evaluation.evaluate_ner import plot_ner_entity_breakdown
            import matplotlib.pyplot as plt

            fig = plot_ner_entity_breakdown(
                test_metrics.get("per_label", {}),
                model_name="PhoBERT-CRF-NER-SingleTask",
                dataset_name="NER Test",
            )
            fig.savefig(
                figures_dir / f"phobert_crf_ner_single_task_breakdown_epoch{epoch+1}.png",
                dpi=150,
                bbox_inches="tight",
            )
            plt.close(fig)

        # Luu checkpoint
        ckpt_path = output_dir / "checkpoints" / f"crf_ner_single_task_epoch_{epoch+1}.pt"
        ckpt_path.parent.mkdir(parents=True, exist_ok=True)
        torch.save({
            "epoch": epoch + 1,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "best_entity_f1": best_f1,
        }, ckpt_path)

    # Lưu training history
    history_path = metrics_dir / "phobert_crf_ner_single_task_history.json"
    with open(history_path, "w", encoding="utf-8") as f:
        json.dump(all_epoch_metrics, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 60)
    print("Training hoàn tất!")
    print(f"Best Entity F1: {best_f1:.4f}")
    print(f"Final metrics: {metrics_dir / 'phobert_crf_ner_single_task.json'}")
    print("=" * 60)

    return model


# =============================================================================
# CLI
# =============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train PhoBERT + CRF NER Single-Task")
    parser.add_argument(
        "--train-json",
        default="data/processed/ner_train.json",
        help="Đường dẫn ner_train.json",
    )
    parser.add_argument(
        "--test-json",
        default="data/processed/ner_test.json",
        help="Đường dẫn ner_test.json",
    )
    parser.add_argument(
        "--output-dir",
        default="outputs",
        help="Thư mục gốc lưu kết quả (mặc định: outputs)",
    )
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--lr", type=float, default=2e-5)
    parser.add_argument("--weight-decay", type=float, default=0.01)
    parser.add_argument("--max-len", type=int, default=256)
    parser.add_argument("--resume-checkpoint", default=None)
    parser.add_argument("--disable-tqdm", action="store_true")
    parser.add_argument("--max-steps-per-epoch", type=int, default=None)
    parser.add_argument("--eval-every", type=int, default=1)
    args = parser.parse_args()

    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    print("=" * 60)
    print("PhoBERT + CRF NER Single-Task Training")
    print("=" * 60)
    print(f"Train JSON : {args.train_json}")
    print(f"Test JSON  : {args.test_json}")
    print(f"Output Dir : {args.output_dir}")

    device = "cuda" if torch.cuda.is_available() else "cpu"
    train(
        train_json=args.train_json,
        test_json=args.test_json,
        output_dir=args.output_dir,
        num_epochs=args.epochs,
        batch_size=args.batch_size,
        learning_rate=args.lr,
        weight_decay=args.weight_decay,
        max_len=args.max_len,
        device=device,
        resume_checkpoint=args.resume_checkpoint,
        disable_tqdm=args.disable_tqdm,
        max_steps_per_epoch=args.max_steps_per_epoch,
        eval_every=args.eval_every,
    )
