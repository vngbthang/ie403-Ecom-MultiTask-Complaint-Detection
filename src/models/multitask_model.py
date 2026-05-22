import torch
import torch.nn as nn
from transformers import AutoModel
from torchcrf import CRF


class PhobertCRFMultiTask(nn.Module):
    """
    Mo hinh da nhiem vu PhoBERT + CRF cho NER.

    - Nhanh 1 (Classification): <s> token -> Linear -> nhan dinh khieu nai (0/1)
    - Nhanh 2 (NER): toan bo sequence -> Linear -> CRF -> chuoi nhan BIO
    """

    def __init__(self, num_classes: int = 2, num_ner_tags: int = 3):
        super(PhobertCRFMultiTask, self).__init__()

        self.phobert = AutoModel.from_pretrained("vinai/phobert-base-v2")
        hidden_size = self.phobert.config.hidden_size

        # Nhanh 1: Phan loai cau
        self.classifier = nn.Linear(hidden_size, num_classes)

        # Nhanh 2: Sequence labeling
        self.ner_classifier = nn.Linear(hidden_size, num_ner_tags)
        self.crf = CRF(num_ner_tags, batch_first=True)

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        class_labels: torch.Tensor = None,
        ner_labels: torch.Tensor = None,
    ):
        """
        Args:
            input_ids: (batch_size, seq_len)
            attention_mask: (batch_size, seq_len)
            class_labels: (batch_size,) - optional, chi can cho training
            ner_labels: (batch_size, seq_len) - optional, chi can cho training

        Returns:
            Neu chi infer (khong co labels):
                classification_logits: (batch_size, num_classes)
                ner_predictions: List[List[int]] - gia tri nhan cua moi token
            Neu co labels:
                classification_logits, ner_predictions, total_loss
        """
        outputs = self.phobert(input_ids=input_ids, attention_mask=attention_mask)
        sequence_output = outputs.last_hidden_state  # (batch, seq_len, hidden)

        # --- Nhanh 1: Classification ---
        cls_output = sequence_output[:, 0, :]  # <s> token
        classification_logits = self.classifier(cls_output)  # (batch, num_classes)

        # --- Nhanh 2: NER ---
        ner_emissions = self.ner_classifier(sequence_output)  # (batch, seq_len, num_tags)
        crf_mask = attention_mask.bool()
        ner_predictions = self.crf.decode(ner_emissions, mask=crf_mask)

        # Neu khong co nhan, tra ve ket qua infer
        if ner_labels is None and class_labels is None:
            return classification_logits, ner_predictions

        # Tinh loss khi co nhan
        ner_loss = None
        if ner_labels is not None:
            # 1. Tạo mặt nạ: Bắt CRF BỎ QUA các vị trí đệm và các vị trí bị gán -100
            crf_mask = (ner_labels != -100) & attention_mask.bool()

            # 2. Làm giả nhãn: Đổi -100 thành 0 để CRF không văng lỗi Index Out Of Bounds
            safe_ner_labels = torch.where(
                ner_labels == -100,
                torch.tensor(0, device=ner_labels.device),
                ner_labels
            )

            # 3. Tính Loss an toàn
            ner_loss = -self.crf(ner_emissions, safe_ner_labels, mask=crf_mask, reduction="mean")

        return classification_logits, ner_predictions, ner_loss


if __name__ == "__main__":
    print("=" * 60)
    print("Test cua PhobertCRFMultiTask")
    print("=" * 60)

    BATCH_SIZE = 2
    SEQ_LEN = 128
    NUM_CLASSES = 2
    NUM_NER_TAGS = 3

    model = PhobertCRFMultiTask(num_classes=NUM_CLASSES, num_ner_tags=NUM_NER_TAGS)
    model.eval()

    # Tao dummy input
    dummy_input_ids = torch.randint(low=0, high=64000, size=(BATCH_SIZE, SEQ_LEN))
    dummy_attention_mask = torch.ones((BATCH_SIZE, SEQ_LEN), dtype=torch.long)
    dummy_class_labels = torch.randint(low=0, high=NUM_CLASSES, size=(BATCH_SIZE,))
    dummy_ner_labels = torch.randint(low=0, high=NUM_NER_TAGS, size=(BATCH_SIZE, SEQ_LEN))

    # Test inference
    with torch.no_grad():
        logits, ner_preds, ner_loss = model(
            input_ids=dummy_input_ids,
            attention_mask=dummy_attention_mask,
            class_labels=dummy_class_labels,
            ner_labels=dummy_ner_labels,
        )

    print(f"classification_logits shape : {list(logits.shape)}")
    print(f"  -> Kieu du lieu        : {logits.dtype}")
    print(f"  -> Gia tri cua vi tri [0,0]: {logits[0, 0].item():.4f}")
    print(f"  -> Gia tri cua vi tri [1,1]: {logits[1, 1].item():.4f}")
    print(f"")
    print(f"ner_predictions (so phan tu batch): {len(ner_preds)}")
    print(f"  -> Do dai chuoi NER[0]  : {len(ner_preds[0])}")
    print(f"  -> Do dai chuoi NER[1]  : {len(ner_preds[1])}")
    print(f"  -> Nhan NER[0][:10]      : {ner_preds[0][:10]}")
    print(f"  -> Nhan NER[1][:10]      : {ner_preds[1][:10]}")
    print(f"")
    print(f"ner_loss (scalar tensor)     : {ner_loss.item():.4f}")
    print("=" * 60)
    print("Test inference (khong co labels):")
    with torch.no_grad():
        logits2, ner_preds2 = model(
            input_ids=dummy_input_ids,
            attention_mask=dummy_attention_mask,
        )
    print(f"  -> classification_logits shape: {list(logits2.shape)}")
    print(f"  -> ner_predictions type       : {type(ner_preds2)} (List[List[int]])")
    print("=" * 60)
