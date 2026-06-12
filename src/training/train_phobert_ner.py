"""
Train PhoBERT Token Classifier cho NER single-task.
Khong su dung CRF.

Dataset: data/processed/ner_train.json, data/processed/ner_test.json
Format: {"tokens": [...], "ner_tags": [...]}

Sub-word alignment:
    - Token dau tien cua word -> gan nhan that
    - Cac sub-word con lai -> gan -100

Output:
    outputs/metrics/phobert_ner_single_task.json
    outputs/figures/phobert_ner_single_task_confusion_matrix.png
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

from src.models.phobert_token_classifier import PhobertTokenClassifier
from src.evaluation.evaluate_ner import (
    compute_ner_metrics,
    save_ner_metrics_json,
    save_ner_reports,
    save_all_ner_results,
    ID2LABEL,
    LABEL_LIST,
)

# =============================================================================
# Dataset
# =============================================================================

class NERDataset(Dataset):
    """
    Dataset cho PhoBERT NER single-task.

    Load tu JSON: [{"tokens": [...], "ner_tags": [...]}]

    Sub-word alignment:
        - Tokenizer bat dau bang <s>, ket thuc bang </s>
        - Moi word tokenize thanh 1 hoac nhieu subwords
        - Subword dau tien: giu nguyen nhan
        - Subword con lai: -100
    """

    LABEL2ID = {"O": 0, "B-COMP": 1, "I-COMP": 2}

    def __init__(
        self,
        json_path: str,
        tokenizer,
        max_len: int = 256,
    ):
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

        # Encode: [CLS] + word1_sub1 word1_sub2 [SEP] + padding
        input_ids = [self.tokenizer.cls_token_id]
        label_ids = [-100]

        for word, tag in zip(tokens, tags):
            word_tokens = self.tokenizer.tokenize(word)
            if not word_tokens:
                continue

            w_ids = self.tokenizer.convert_tokens_to_ids(word_tokens)
            input_ids.extend(w_ids)

            # Sub-word alignment: dau tien giu nhan, con lai -100
            label_id = self.LABEL2ID.get(tag, 0)
            label_ids.append(label_id)
            label_ids.extend([-100] * (len(w_ids) - 1))

        input_ids.append(self.tokenizer.sep_token_id)
        label_ids.append(-100)

        # Truncate if too long
        if len(input_ids) > self.max_len:
            input_ids = input_ids[: self.max_len - 1] + [self.tokenizer.sep_token_id]
            label_ids = label_ids[: self.max_len - 1] + [-100]

        # Padding
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


# =============================================================================
# Collate
# =============================================================================

def ner_collate_fn(batch):
    """Ghep batch, chi giu tokens va tags cua mau dau tien moi sequence."""
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
    total_loss = 0.0
    num_batches = 0

    with torch.no_grad():
        for batch in dataloader:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            ner_labels = batch["ner_labels"].to(device)

            # Inference aligned with training labels.
            # Do not use attention_mask for final tag decoding because it also
            # includes special tokens and non-first subwords. The correct mask
            # for metric positions is exactly the labels mask used by the loss.
            outputs = model.phobert(input_ids=input_ids, attention_mask=attention_mask)
            sequence_output = model.dropout(outputs.last_hidden_state)
            logits = model.ner_classifier(sequence_output)
            pred_ids = logits.argmax(dim=-1)

            for b in range(input_ids.size(0)):
                gold_seq = []
                pred_seq = []

                for pos in range(ner_labels.size(1)):
                    gold_id = ner_labels[b, pos].item()
                    if gold_id != -100:
                        gold_seq.append(ID2LABEL.get(gold_id, "O"))
                        pred_seq.append(ID2LABEL.get(pred_ids[b, pos].item(), "O"))

                if len(gold_seq) != len(pred_seq):
                    raise ValueError(
                        "NER decode length mismatch in evaluate(): "
                        f"gold={len(gold_seq)} pred={len(pred_seq)}"
                    )

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


def decode_predictions_from_logits(logits, ner_labels):
    """
    Decode predictions va ground truth tu logits bang mask labels != -100.

    logits: Tensor (batch_size, seq_len, num_labels)
    ner_labels: Tensor (batch_size, seq_len)
    Tra ve (y_true_str, y_pred_str)
    """
    y_true_str = []
    y_pred_str = []
    pred_ids = logits.argmax(dim=-1)
    batch_size = ner_labels.size(0)

    for b in range(batch_size):
        gold_seq = []
        pred_seq = []
        seq_len = ner_labels.size(1)

        for pos in range(seq_len):
            gold_id = ner_labels[b, pos].item()
            if gold_id != -100:
                gold_seq.append(ID2LABEL.get(gold_id, "O"))
                pred_seq.append(ID2LABEL.get(pred_ids[b, pos].item(), "O"))

        if len(gold_seq) != len(pred_seq):
            raise ValueError(
                "NER decode length mismatch in decode_predictions_from_logits(): "
                f"gold={len(gold_seq)} pred={len(pred_seq)}"
            )

        if gold_seq:
            y_true_str.append(gold_seq)
            y_pred_str.append(pred_seq)

    return y_true_str, y_pred_str


def count_label_distribution(sequences):
    """Dem label va so sequence co COMP trong list tag sequences."""
    counts = {label: 0 for label in LABEL_LIST}
    samples_with_comp = 0
    for seq in sequences:
        has_comp = False
        for tag in seq:
            counts[tag] = counts.get(tag, 0) + 1
            if tag in {"B-COMP", "I-COMP"}:
                has_comp = True
        samples_with_comp += int(has_comp)
    return {
        "counts": counts,
        "samples_with_comp": samples_with_comp,
        "samples_total": len(sequences),
    }


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
    model_name: str = "vinai/phobert-base-v2",
):
    """
    Huan luyen PhoBERT Token Classifier cho NER single-task.

    Args:
        train_json: Duong dan ner_train.json
        test_json: Duong dan ner_test.json
        output_dir: Thu muc luu ket qua
        num_epochs: So epoch
        batch_size: Kich thuoc batch
        learning_rate: Toc do hoc
        weight_decay: He so giam toc do hoc
        max_len: Do dai toi da chuoi
        device: 'cuda' hoac 'cpu'
        resume_checkpoint: Duong dan checkpoint de resume
        disable_tqdm: Tat tqdm
        max_steps_per_epoch: Gioi han so step moi epoch (debug)
        eval_every: Danh gia sau moi eval_every epochs (mac dinh 1)
    """
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"

    print(f"Device: {device}")

    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
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
    model = PhobertTokenClassifier(num_ner_tags=3, model_name=model_name)
    model.to(device)

    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=learning_rate,
        weight_decay=weight_decay,
    )

    criterion = nn.CrossEntropyLoss(ignore_index=-100)

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
    print(f"Resume from epoch: {start_epoch} | Best F1 so far: {best_f1:.4f}")
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

        # Danh gia
        if (epoch + 1) % eval_every == 0 or epoch == start_epoch + num_epochs - 1:
            y_true, y_pred, test_metrics = evaluate(model, test_loader, device)

            print(f"  Test - Entity P: {test_metrics['entity_precision']:.4f}  "
                  f"R: {test_metrics['entity_recall']:.4f}  "
                  f"F1: {test_metrics['entity_f1']:.4f}")
            print(f"  Test - Token F1 (macro): {test_metrics['token_f1_macro']:.4f}")

            gold_dist = count_label_distribution(y_true)
            pred_dist = count_label_distribution(y_pred)
            print("  Test - Gold label distribution:")
            print(
                "    "
                + " | ".join(f"{label}: {gold_dist['counts'].get(label, 0)}" for label in LABEL_LIST)
                + f" | samples_with_COMP: {gold_dist['samples_with_comp']}/{gold_dist['samples_total']}"
            )
            print("  Test - Pred label distribution:")
            print(
                "    "
                + " | ".join(f"{label}: {pred_dist['counts'].get(label, 0)}" for label in LABEL_LIST)
                + f" | samples_with_COMP: {pred_dist['samples_with_comp']}/{pred_dist['samples_total']}"
            )

            test_metrics["epoch"] = epoch + 1
            test_metrics["avg_loss"] = avg_loss
            test_metrics["gold_label_distribution"] = gold_dist
            test_metrics["pred_label_distribution"] = pred_dist
            all_epoch_metrics.append(test_metrics)

            # Luu metrics JSON cho epoch nay
            epoch_metrics_dir = metrics_dir / f"epoch_{epoch + 1}"
            epoch_metrics_dir.mkdir(exist_ok=True)

            save_ner_metrics_json(test_metrics, str(epoch_metrics_dir))
            save_ner_reports(test_metrics, str(epoch_metrics_dir))

            # Lưu final metrics
            if test_metrics["entity_f1"] >= best_f1:
                best_f1 = test_metrics["entity_f1"]
                print(f"  [BEST] New best Entity F1: {best_f1:.4f}")

                # Ghi de file single-task chinh
                final_metrics_path = metrics_dir / "phobert_ner_single_task.json"
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
                with open(final_metrics_path, "w", encoding="utf-8") as f:
                    json.dump(final_metrics, f, ensure_ascii=False, indent=2)
                print(f"  [SAVE] Best metrics: {final_metrics_path}")

                # Save entity report
                entity_report_path = metrics_dir / "phobert_ner_single_task_entity_report.txt"
                with open(entity_report_path, "w", encoding="utf-8") as f:
                    f.write(test_metrics["entity_classification_report"])

                # Save token report
                token_report_path = metrics_dir / "phobert_ner_single_task_token_report.txt"
                with open(token_report_path, "w", encoding="utf-8") as f:
                    f.write(test_metrics["token_classification_report"])

                # Save predictions CSV
                predictions_path = figures_dir / "phobert_ner_single_task_predictions.csv"
                import pandas as pd
                records = []
                for i in range(min(len(y_true), len(y_pred))):
                    n_gold_tags = len(y_true[i])
                    n_pred_tags = len(y_pred[i])
                    has_length_mismatch = n_gold_tags != n_pred_tags
                    if has_length_mismatch:
                        raise ValueError(
                            "Cannot save NER predictions with length mismatch: "
                            f"index={i}, gold={n_gold_tags}, pred={n_pred_tags}"
                        )
                    records.append({
                        "index": i,
                        "gold_tags": " ".join(y_true[i]),
                        "pred_tags": " ".join(y_pred[i]),
                        "n_gold_tags": n_gold_tags,
                        "n_pred_tags": n_pred_tags,
                        "has_length_mismatch": has_length_mismatch,
                        "correct": (y_true[i] == y_pred[i]),
                    })
                pd.DataFrame(records).to_csv(predictions_path, index=False, encoding="utf-8-sig")
                print(f"  [SAVE] Predictions: {predictions_path}")

            # Ve confusion matrix cho entity breakdown
            from src.evaluation.evaluate_ner import plot_ner_entity_breakdown
            fig = plot_ner_entity_breakdown(
                test_metrics.get("per_label", {}),
                model_name="PhoBERT-NER-SingleTask",
                dataset_name="NER Test",
            )
            fig.savefig(
                figures_dir / f"phobert_ner_single_task_breakdown_epoch{epoch+1}.png",
                dpi=150,
                bbox_inches="tight",
            )
            import matplotlib.pyplot as plt
            plt.close(fig)

        # Luu checkpoint
        ckpt_path = output_dir / "checkpoints" / f"ner_single_task_epoch_{epoch+1}.pt"
        ckpt_path.parent.mkdir(parents=True, exist_ok=True)
        torch.save({
            "epoch": epoch + 1,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "best_entity_f1": best_f1,
        }, ckpt_path)

    # Luu history
    history_path = metrics_dir / "phobert_ner_single_task_history.json"
    with open(history_path, "w", encoding="utf-8") as f:
        json.dump(all_epoch_metrics, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 60)
    print("Training hoan tat!")
    print(f"Best Entity F1: {best_f1:.4f}")
    print(f"Final metrics: {metrics_dir / 'phobert_ner_single_task.json'}")
    print("=" * 60)

    return model


# =============================================================================
# CLI
# =============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train PhoBERT NER Single-Task")
    parser.add_argument(
        "--train-json",
        default="data/processed/ner_train.json",
        help="Duong dan ner_train.json",
    )
    parser.add_argument(
        "--test-json",
        default="data/processed/ner_test.json",
        help="Duong dan ner_test.json",
    )
    parser.add_argument(
        "--val-json",
        default=None,
        help="Optional validation JSON path. Accepted for runner compatibility; current training evaluates on --test-json.",
    )
    parser.add_argument(
        "--output-dir",
        default="outputs",
        help="Thu muc goc luu ket qua (mac dinh: outputs)",
    )
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--lr", "--learning-rate", dest="lr", type=float, default=2e-5)
    parser.add_argument("--weight-decay", type=float, default=0.01)
    parser.add_argument("--max-len", type=int, default=256)
    parser.add_argument("--resume-checkpoint", default=None)
    parser.add_argument("--disable-tqdm", action="store_true")
    parser.add_argument("--max-steps-per-epoch", type=int, default=None)
    parser.add_argument("--eval-every", type=int, default=1)
    parser.add_argument("--model-name", default="vinai/phobert-base-v2")
    args = parser.parse_args()

    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    print("=" * 60)
    print("PhoBERT NER Single-Task Training")
    print("=" * 60)
    print(f"Train JSON : {args.train_json}")
    print(f"Val JSON   : {args.val_json}")
    print(f"Test JSON  : {args.test_json}")
    print(f"Output Dir : {args.output_dir}")
    print(f"Model Name : {args.model_name}")

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
        model_name=args.model_name,
    )
