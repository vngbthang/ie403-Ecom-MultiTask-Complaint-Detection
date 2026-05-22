import os
import argparse
import json
import sys
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, WeightedRandomSampler, Subset
from tqdm import tqdm
from seqeval.metrics import precision_score, recall_score, f1_score, classification_report
from transformers import AutoTokenizer

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.models.multitask_model import PhobertCRFMultiTask
from src.data_processing.multitask_dataset import MultiTaskDataset


ID2LABEL = {0: "O", 1: "B-COMP", 2: "I-COMP"}


def build_weighted_sampler(dataset: MultiTaskDataset):
    weights = []
    for idx in range(len(dataset)):
        item = dataset[idx]
        has_ner = int(item["ner_has_labels"].item())
        has_comp = int(item["ner_has_complaint"].item())

        if has_comp:
            weight = 4.0
        elif has_ner:
            weight = 2.0
        else:
            weight = 1.0
        weights.append(weight)

    return WeightedRandomSampler(
        weights=torch.DoubleTensor(weights),
        num_samples=len(weights),
        replacement=True,
    )


def evaluate_ner(model, ner_data_path, tokenizer, max_len=256, device="cpu"):
    with open(ner_data_path, encoding="utf-8-sig") as f:
        eval_records = json.load(f)

    y_true = []
    y_pred = []
    model.eval()

    with torch.no_grad():
        for item in eval_records:
            tokens = item.get("tokens", [])
            tags = item.get("ner_tags", [])
            if not tokens or len(tokens) != len(tags):
                continue

            input_ids = [tokenizer.cls_token_id]
            label_ids = [-100]

            for word, tag in zip(tokens, tags):
                word_tokens = tokenizer.tokenize(word)
                if not word_tokens:
                    continue

                w_ids = tokenizer.convert_tokens_to_ids(word_tokens)
                input_ids.extend(w_ids)
                mapped = {"O": 0, "B-COMP": 1, "I-COMP": 2}.get(tag, 0)
                label_ids.append(mapped)
                label_ids.extend([-100] * (len(w_ids) - 1))

            input_ids.append(tokenizer.sep_token_id)
            label_ids.append(-100)

            if len(input_ids) > max_len:
                input_ids = input_ids[: max_len - 1] + [tokenizer.sep_token_id]
                label_ids = label_ids[: max_len - 1] + [-100]

            attention_mask = [1] * len(input_ids)
            pad_len = max_len - len(input_ids)
            if pad_len > 0:
                input_ids.extend([tokenizer.pad_token_id] * pad_len)
                attention_mask.extend([0] * pad_len)
                label_ids.extend([-100] * pad_len)

            input_ids_t = torch.tensor([input_ids], dtype=torch.long, device=device)
            attention_mask_t = torch.tensor([attention_mask], dtype=torch.long, device=device)

            _, ner_predictions = model(input_ids=input_ids_t, attention_mask=attention_mask_t)
            pred_ids = ner_predictions[0]

            true_seq = []
            pred_seq = []
            seq_len = min(len(pred_ids), len(label_ids))
            for pos in range(seq_len):
                gold = int(label_ids[pos])
                if gold == -100:
                    continue
                pred = int(pred_ids[pos])
                true_seq.append(ID2LABEL.get(gold, "O"))
                pred_seq.append(ID2LABEL.get(pred, "O"))

            if true_seq:
                y_true.append(true_seq)
                y_pred.append(pred_seq)

    if not y_true:
        return {
            "precision": 0.0,
            "recall": 0.0,
            "f1": 0.0,
            "report": "No valid NER labels found for evaluation.",
        }

    return {
        "precision": precision_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "f1": f1_score(y_true, y_pred),
        "report": classification_report(y_true, y_pred, digits=4),
    }


def train_multitask(
    classification_data_path: str,
    ner_data_path: str,
    tokenizer,
    output_dir: str = "./checkpoints",
    num_epochs: int = 5,
    batch_size: int = 8,
    learning_rate: float = 2e-5,
    alpha: float = 1.0,
    weight_decay: float = 0.01,
    max_len: int = 256,
    device: str = None,
    ner_eval_path: str = None,
    resume_checkpoint: str = None,
    use_weighted_sampler: bool = True,
    only_ner_matched: bool = False,
    disable_tqdm: bool = False,
    max_steps_per_epoch: int = None,
):
    """
    Vong lap huan luyen thuan tuy PyTorch cho mo hinh da nhiem vu.

    Ham tong suy hao:
        Total_Loss = CrossEntropy(classification_logits, class_labels)
                    + alpha * NER_Loss(CRF)

    Args:
        classification_data_path: Duong dan file phan loai (CSV/JSONL)
        ner_data_path: Duong dan file NER (JSON)
        tokenizer: PhoBERT tokenizer
        output_dir: Thu muc luu checkpoint (khong luu vao Git)
        num_epochs: So epoch huan luyen
        batch_size: Kich thuoc batch
        learning_rate: Toc do hoc
        alpha: He so nhan cho NER loss
        weight_decay: He so giam toc do hoc
        max_len: Do dai toi da chuoi dau vao
        device: 'cuda' hoac 'cpu'
    """
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"

    # Khoi tao dataset va dataloader
    train_dataset = MultiTaskDataset(
        classification_data_path=classification_data_path,
        ner_data_path=ner_data_path,
        tokenizer=tokenizer,
        max_len=max_len,
    )

    alignment_report = train_dataset.get_alignment_report()

    if only_ner_matched:
        matched_indices = []
        for i in range(len(train_dataset)):
            if int(train_dataset[i]["ner_has_labels"].item()) == 1:
                matched_indices.append(i)
        train_dataset = Subset(train_dataset, matched_indices)
        print(f"Using only matched NER samples: {len(matched_indices)}")

    if use_weighted_sampler:
        if isinstance(train_dataset, Subset):
            subset_weights = []
            for subset_idx in train_dataset.indices:
                item = train_dataset.dataset[subset_idx]
                has_ner = int(item["ner_has_labels"].item())
                has_comp = int(item["ner_has_complaint"].item())
                if has_comp:
                    weight = 4.0
                elif has_ner:
                    weight = 2.0
                else:
                    weight = 1.0
                subset_weights.append(weight)
            train_sampler = WeightedRandomSampler(
                weights=torch.DoubleTensor(subset_weights),
                num_samples=len(subset_weights),
                replacement=True,
            )
        else:
            train_sampler = build_weighted_sampler(train_dataset)
        train_loader = DataLoader(
            train_dataset,
            batch_size=batch_size,
            sampler=train_sampler,
            num_workers=0,
        )
    else:
        train_loader = DataLoader(
            train_dataset,
            batch_size=batch_size,
            shuffle=True,
            num_workers=0,
        )

    # Khoi tao model
    model = PhobertCRFMultiTask(num_classes=2, num_ner_tags=3)
    model.to(device)

    # Khoi tao toi uu hoa
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=learning_rate,
        weight_decay=weight_decay,
    )

    # Loss function cho classification
    cls_criterion = nn.CrossEntropyLoss()

    start_epoch = 0
    if resume_checkpoint:
        print(f"Loading checkpoint to resume: {resume_checkpoint}")
        ckpt = torch.load(resume_checkpoint, map_location=device)
        model.load_state_dict(ckpt["model_state_dict"])
        if "optimizer_state_dict" in ckpt:
            optimizer.load_state_dict(ckpt["optimizer_state_dict"])
        start_epoch = int(ckpt.get("epoch", 0))

    print(f"Device: {device}")
    print(f"Train samples: {len(train_dataset)}")
    print(f"Epochs: {num_epochs} | Batch size: {batch_size} | LR: {learning_rate} | Alpha: {alpha}")
    print(
        "Alignment | matched: "
        f"{alignment_report['matched_samples']}/{alignment_report['total_classification_samples']} "
        f"({alignment_report['matched_ratio'] * 100:.2f}%), "
        f"matched_with_complaint: {alignment_report['matched_with_complaint']}"
    )
    print(f"Resume from epoch: {start_epoch}")
    print("=" * 60)

    for epoch in range(start_epoch, start_epoch + num_epochs):
        model.train()
        total_cls_loss = 0.0
        total_ner_loss = 0.0
        total_loss = 0.0
        num_batches = 0
        ner_active_batches = 0

        pbar = train_loader if disable_tqdm else tqdm(train_loader, desc=f"Epoch {epoch + 1}/{start_epoch + num_epochs}")
        for step_idx, batch in enumerate(pbar, start=1):
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            class_labels = batch["class_labels"].to(device)
            ner_labels = batch["ner_labels"].to(device)

            optimizer.zero_grad()

            # Forward pass
            classification_logits, ner_predictions, ner_loss = model(
                input_ids=input_ids,
                attention_mask=attention_mask,
                class_labels=class_labels,
                ner_labels=ner_labels,
            )

            # Tinh classification loss
            cls_loss = cls_criterion(classification_logits, class_labels)

            # Ham tong suy hao: Total_Loss = cls_loss + alpha * ner_loss
            if ner_loss is not None:
                loss = cls_loss + alpha * ner_loss
                total_ner_loss += ner_loss.item()
                ner_active_batches += 1
            else:
                loss = cls_loss

            # Backward pass
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()

            total_cls_loss += cls_loss.item()
            total_loss += loss.item()
            num_batches += 1

            if not disable_tqdm:
                pbar.set_postfix({
                    "cls_loss": f"{cls_loss.item():.4f}",
                    "ner_loss": f"{ner_loss.item() if ner_loss else 0.0:.4f}",
                    "total": f"{loss.item():.4f}",
                })

            if max_steps_per_epoch is not None and step_idx >= max_steps_per_epoch:
                print(f"  Reached max_steps_per_epoch={max_steps_per_epoch}, stop this epoch early.")
                break

        avg_cls_loss = total_cls_loss / num_batches
        avg_ner_loss = total_ner_loss / max(ner_active_batches, 1)
        avg_total_loss = total_loss / num_batches

        print(f"\nEpoch {epoch + 1}/{start_epoch + num_epochs}")
        print(f"  Avg Cls Loss : {avg_cls_loss:.4f}")
        print(f"  Avg Ner Loss : {avg_ner_loss:.4f}")
        print(f"  Avg Total Loss: {avg_total_loss:.4f}")
        print(f"  NER active batches: {ner_active_batches}/{num_batches}")

        ner_metrics = None
        if ner_eval_path:
            ner_metrics = evaluate_ner(
                model=model,
                ner_data_path=ner_eval_path,
                tokenizer=tokenizer,
                max_len=max_len,
                device=device,
            )
            print("  NER Eval:")
            print(f"    Precision: {ner_metrics['precision']:.4f}")
            print(f"    Recall   : {ner_metrics['recall']:.4f}")
            print(f"    F1       : {ner_metrics['f1']:.4f}")
            print("  NER Report:")
            print(ner_metrics["report"])

        # Luu checkpoint moi epoch
        os.makedirs(output_dir, exist_ok=True)
        checkpoint_path = os.path.join(output_dir, f"checkpoint_epoch_{epoch + 1}.pt")
        torch.save(
            {
                "epoch": epoch + 1,
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
                "avg_loss": avg_total_loss,
                "ner_metrics": ner_metrics,
                "alignment_report": alignment_report,
            },
            checkpoint_path,
        )
        print(f"  Saved: {checkpoint_path}")

    print("\n" + "=" * 60)
    print("Training hoan tat!")

    return model


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train PhoBERT + CRF multi-task model")
    parser.add_argument("--cls-path", default="data/processed/shopee_mapped.csv")
    parser.add_argument("--ner-train-path", default="data/processed/ner_train.json")
    parser.add_argument("--ner-test-path", default="data/processed/ner_test.json")
    parser.add_argument("--output-dir", default="checkpoints")
    parser.add_argument("--resume-checkpoint", default=None)
    parser.add_argument("--epochs", type=int, default=2)
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--lr", type=float, default=2e-5)
    parser.add_argument("--alpha", type=float, default=1.0)
    parser.add_argument("--weight-decay", type=float, default=0.01)
    parser.add_argument("--max-len", type=int, default=256)
    parser.add_argument("--no-weighted-sampler", action="store_true")
    parser.add_argument("--only-ner-matched", action="store_true")
    parser.add_argument("--disable-tqdm", action="store_true")
    parser.add_argument("--max-steps-per-epoch", type=int, default=None)
    args = parser.parse_args()

    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    print("=" * 60)
    print("Train Custom Multi-task Loop")
    print("=" * 60)

    print(f"classification_data: {args.cls_path}")
    print(f"ner_train_data    : {args.ner_train_path}")
    print(f"ner_test_data     : {args.ner_test_path}")
    print(f"resume_checkpoint : {args.resume_checkpoint}")

    tokenizer = AutoTokenizer.from_pretrained(
        "vinai/phobert-base-v2",
        use_fast=False
    )

    print("\nBat dau huan luyen...")
    train_multitask(
        classification_data_path=args.cls_path,
        ner_data_path=args.ner_train_path,
        tokenizer=tokenizer,
        output_dir=args.output_dir,
        num_epochs=args.epochs,
        batch_size=args.batch_size,
        learning_rate=args.lr,
        alpha=args.alpha,
        weight_decay=args.weight_decay,
        max_len=args.max_len,
        ner_eval_path=args.ner_test_path,
        resume_checkpoint=args.resume_checkpoint,
        use_weighted_sampler=not args.no_weighted_sampler,
        only_ner_matched=args.only_ner_matched,
        disable_tqdm=args.disable_tqdm,
        max_steps_per_epoch=args.max_steps_per_epoch,
    )

    print("=" * 60)
