import os
import json
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from tqdm import tqdm

from src.models.multitask_model import PhobertCRFMultiTask
from src.data_processing.multitask_dataset import MultiTaskDataset


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

    print(f"Device: {device}")
    print(f"Train samples: {len(train_dataset)}")
    print(f"Epochs: {num_epochs} | Batch size: {batch_size} | LR: {learning_rate} | Alpha: {alpha}")
    print("=" * 60)

    for epoch in range(num_epochs):
        model.train()
        total_cls_loss = 0.0
        total_ner_loss = 0.0
        total_loss = 0.0
        num_batches = 0

        pbar = tqdm(train_loader, desc=f"Epoch {epoch + 1}/{num_epochs}")
        for batch in pbar:
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
            else:
                loss = cls_loss

            # Backward pass
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()

            total_cls_loss += cls_loss.item()
            total_loss += loss.item()
            num_batches += 1

            pbar.set_postfix({
                "cls_loss": f"{cls_loss.item():.4f}",
                "ner_loss": f"{ner_loss.item() if ner_loss else 0.0:.4f}",
                "total": f"{loss.item():.4f}",
            })

        avg_cls_loss = total_cls_loss / num_batches
        avg_ner_loss = total_ner_loss / num_batches
        avg_total_loss = total_loss / num_batches

        print(f"\nEpoch {epoch + 1}/{num_epochs}")
        print(f"  Avg Cls Loss : {avg_cls_loss:.4f}")
        print(f"  Avg Ner Loss : {avg_ner_loss:.4f}")
        print(f"  Avg Total Loss: {avg_total_loss:.4f}")

        # Luu checkpoint moi epoch
        os.makedirs(output_dir, exist_ok=True)
        checkpoint_path = os.path.join(output_dir, f"checkpoint_epoch_{epoch + 1}.pt")
        torch.save(
            {
                "epoch": epoch + 1,
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
                "avg_loss": avg_total_loss,
            },
            checkpoint_path,
        )
        print(f"  Saved: {checkpoint_path}")

    print("\n" + "=" * 60)
    print("Training hoan tat!")

    return model


if __name__ == "__main__":
    print("=" * 60)
    print("Test Custom Multi-task Training Loop")
    print("=" * 60)

    import os
    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    from transformers import AutoTokenizer

    DATA_DIR = "../data/processed"
    CLS_PATH = os.path.join(DATA_DIR, "shopee_mapped.csv")
    NER_PATH = os.path.join(DATA_DIR, "ner_train.json")

    if not os.path.exists(CLS_PATH) or not os.path.exists(NER_PATH):
        print("[WARN] File du lieu chua co. Chi chay 1 epoch nho de test logic.")
        print(f"  cls : {CLS_PATH}")
        print(f"  ner : {NER_PATH}")
    else:
        print(f"classification_data: {CLS_PATH}")
        print(f"ner_data        : {NER_PATH}")

    tokenizer = AutoTokenizer.from_pretrained(
        "vinai/phobert-base-v2",
        use_fast=False
    )

    print("\nBat dau huan luyen 1 epoch nho de kiem tra...")
    train_multitask(
        classification_data_path=CLS_PATH,
        ner_data_path=NER_PATH,
        tokenizer=tokenizer,
        output_dir="./checkpoints",
        num_epochs=1,
        batch_size=2,
        learning_rate=2e-5,
        alpha=1.0,
        weight_decay=0.01,
        max_len=64,
    )

    print("=" * 60)
