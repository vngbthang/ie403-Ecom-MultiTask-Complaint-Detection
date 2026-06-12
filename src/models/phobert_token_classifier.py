"""
PhoBERT Token Classifier cho single-task NER.
vinai/phobert-base-v2 + Linear token classifier (khong CRF).
"""
import torch
import torch.nn as nn
from transformers import AutoModel


class PhobertTokenClassifier(nn.Module):
    """
    PhoBERT + Linear token classifier cho NER single-task.

    Su dung sub-word pooling: chi token dau tien cua word
    duoc gan nhan that, cac sub-word con lai duoc gan -100.

    Forward tra ve:
        - Neu co ner_labels: (loss, predictions) — cho training
        - Neu khong: (predictions,) — cho inference

    Predictions tra ve: List[List[int]] (list of tag ID sequences),
    bo qua vi tri -100.
    """

    def __init__(
        self,
        num_ner_tags: int = 3,
        dropout: float = 0.1,
        model_name: str = "vinai/phobert-base-v2",
    ):
        """
        Args:
            num_ner_tags: So luong nhan NER (mac dinh 3: O, B-COMP, I-COMP)
            dropout: Dropout rate truoc token classifier
            model_name: HuggingFace model name/path for the encoder
        """
        super(PhobertTokenClassifier, self).__init__()
        self.phobert = AutoModel.from_pretrained(model_name)
        hidden_size = self.phobert.config.hidden_size

        self.dropout = nn.Dropout(dropout)
        self.ner_classifier = nn.Linear(hidden_size, num_ner_tags)

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        ner_labels: torch.Tensor = None,
        class_weights: torch.Tensor = None,
    ):
        """
        Args:
            input_ids: (batch_size, seq_len)
            attention_mask: (batch_size, seq_len)
            ner_labels: (batch_size, seq_len), gia tri -100 bi bo qua trong loss
            class_weights: Optional tensor (num_tags,) for weighted CrossEntropy

        Returns:
            Neu co ner_labels:
                loss: Scalar tensor (CrossEntropy, bo qua -100)
                predictions: List[List[int]] — list of tag ID sequences
            Neu khong co ner_labels:
                predictions: List[List[int]]
        """
        outputs = self.phobert(input_ids=input_ids, attention_mask=attention_mask)
        sequence_output = outputs.last_hidden_state  # (batch, seq_len, hidden)
        sequence_output = self.dropout(sequence_output)

        emissions = self.ner_classifier(sequence_output)  # (batch, seq_len, num_tags)

        # Decode: lay argmax tren hidden dimension
        predictions = emissions.argmax(dim=-1)  # (batch, seq_len)

        if ner_labels is None:
            return (predictions,)

        # --- Tinh CrossEntropy loss, bo qua -100 ---
        # Chuyen -100 thanh index cuoi cung de tranh loi
        # Nhuoc diem: padding class nhan -100 nhung van tinh loss
        # Giai phap tot hon: mask

        batch_size, seq_len = input_ids.shape
        loss_mask = (ner_labels != -100).float()  # 1.0 neu can tinh loss, 0.0 neu bo qua

        # Di chuyen ner_labels: -100 -> 0 (gia su nhan 0 khong bao gio xuat hien thuc te
        # voi BIO tagging, nhung label 0 = "O" van co the xuat hien)
        # Cai nay co van de. Dung cach khac: ignore_index=-100 trong CrossEntropy

        loss = nn.functional.cross_entropy(
            emissions.view(-1, emissions.size(-1)),
            ner_labels.view(-1),
            weight=class_weights,
            ignore_index=-100,
            reduction="mean",
        )

        # Chuan bi ket qua decode: loai bo -100
        decoded = []
        for b in range(batch_size):
            seq = []
            for pos in range(seq_len):
                if ner_labels[b, pos].item() != -100:
                    seq.append(predictions[b, pos].item())
            decoded.append(seq)

        return (loss, decoded)

    def predict(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
    ) -> list[list[int]]:
        """
        Inference mode: tra ve danh sach tag ID, bo qua -100.

        Args:
            input_ids: (batch_size, seq_len)
            attention_mask: (batch_size, seq_len)

        Returns:
            List of tag ID sequences, moi sequence bo qua cac vi tri padding
        """
        self.eval()
        with torch.no_grad():
            outputs = self.phobert(input_ids=input_ids, attention_mask=attention_mask)
            sequence_output = outputs.last_hidden_state
            emissions = self.ner_classifier(sequence_output)
            predictions = emissions.argmax(dim=-1)  # (batch, seq_len)

        batch_size, seq_len = input_ids.shape
        decoded = []
        for b in range(batch_size):
            seq = []
            for pos in range(seq_len):
                if attention_mask[b, pos].item() == 1:
                    seq.append(predictions[b, pos].item())
            decoded.append(seq)

        return decoded


if __name__ == "__main__":
    print("=" * 60)
    print("Test PhobertTokenClassifier")
    print("=" * 60)

    BATCH_SIZE = 2
    SEQ_LEN = 128
    NUM_NER_TAGS = 3

    model = PhobertTokenClassifier(num_ner_tags=NUM_NER_TAGS)
    model.eval()

    # Dummy input
    dummy_input_ids = torch.randint(low=0, high=64000, size=(BATCH_SIZE, SEQ_LEN))
    dummy_attention_mask = torch.ones((BATCH_SIZE, SEQ_LEN), dtype=torch.long)
    dummy_ner_labels = torch.randint(low=0, high=NUM_NER_TAGS, size=(BATCH_SIZE, SEQ_LEN))

    # Make some positions -100 (sub-word alignment simulation)
    dummy_ner_labels[:, 5] = -100
    dummy_ner_labels[:, 12] = -100
    dummy_ner_labels[:, 20:23] = -100

    # Test inference
    print("--- Inference (no labels) ---")
    result = model(input_ids=dummy_input_ids, attention_mask=dummy_attention_mask)
    predictions = result[0]
    print(f"  predictions type : {type(predictions)}")
    print(f"  batch 0 seq len : {len(predictions[0])}")
    print(f"  batch 0 first 15: {predictions[0][:15]}")
    print(f"  batch 1 first 15: {predictions[1][:15]}")

    # Test training
    print("\n--- Training (with labels) ---")
    loss, decoded = model(
        input_ids=dummy_input_ids,
        attention_mask=dummy_attention_mask,
        ner_labels=dummy_ner_labels,
    )
    print(f"  loss              : {loss.item():.4f}")
    print(f"  decoded type      : {type(decoded)}")
    print(f"  decoded batch 0   : {decoded[0][:10]}")
    print(f"  decoded batch 0 len: {len(decoded[0])}")
    print(f"  (Should be SEQ_LEN - num(-100) positions)")

    # Test predict()
    print("\n--- predict() method ---")
    preds_list = model.predict(dummy_input_ids, dummy_attention_mask)
    print(f"  type  : {type(preds_list)}")
    print(f"  batch 0: {preds_list[0][:10]}")
    print(f"  batch 1: {preds_list[1][:10]}")

    print("=" * 60)
    print("Test hoan tat!")
