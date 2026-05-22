"""
PhoBERT + CRF cho single-task NER.
Tận dụng pytorch-crf.CRF, loại bỏ classification head.
"""
import torch
import torch.nn as nn
from transformers import AutoModel
from torchcrf import CRF


class PhobertCRFNer(nn.Module):
    """
    PhoBERT + Linear + CRF cho single-task NER.

    Khác với PhobertTokenClassifier:
    - Dùng CRF layer để encode ràng buộc BIO (I-COMP phải đi sau B-COMP)
    - Không có classification head

    Args:
        num_ner_tags: Số lượng nhãn NER (mặc định 3: O, B-COMP, I-COMP)
        dropout: Dropout rate trước emission layer
    """

    def __init__(self, num_ner_tags: int = 3, dropout: float = 0.1):
        super(PhobertCRFNer, self).__init__()
        self.phobert = AutoModel.from_pretrained("vinai/phobert-base-v2")
        hidden_size = self.phobert.config.hidden_size

        self.dropout = nn.Dropout(dropout)
        self.ner_classifier = nn.Linear(hidden_size, num_ner_tags)
        self.crf = CRF(num_ner_tags, batch_first=True)

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        ner_labels: torch.Tensor = None,
    ):
        """
        Args:
            input_ids: (batch_size, seq_len)
            attention_mask: (batch_size, seq_len)
            ner_labels: (batch_size, seq_len), -100 cho subwords

        Returns:
            Inference (không labels):
                predictions: List[List[int]] — decoded tag ID sequences
            Training (có labels):
                (loss, predictions)
        """
        outputs = self.phobert(input_ids=input_ids, attention_mask=attention_mask)
        sequence_output = outputs.last_hidden_state  # (batch, seq_len, hidden)
        sequence_output = self.dropout(sequence_output)

        emissions = self.ner_classifier(sequence_output)  # (batch, seq_len, num_tags)

        # Decode bằng CRF
        predictions = self.crf.decode(emissions, mask=attention_mask.bool())

        if ner_labels is None:
            return (predictions,)

        # CRF loss: chỉ tính trên các vị trí hợp lệ (không -100)
        # Logic giữ nguyên từ PhobertCRFMultiTask để đảm bảo consistency
        has_valid_ner = (ner_labels != -100).any(dim=1)

        if not has_valid_ner.any():
            # Tất cả samples không có nhãn NER hợp lệ
            loss = emissions.sum() * 0.0  # zero loss, gradient vẫn chảy
            return (loss, predictions)

        sub_emissions = emissions[has_valid_ner]
        sub_labels = ner_labels[has_valid_ner]
        sub_attn = attention_mask[has_valid_ner]

        # CRF mask: True tại vị trí cần decode
        crf_mask = (sub_labels != -100) & sub_attn.bool()
        crf_mask[:, 0] = True  # luôn decode vị trí đầu tiên

        # Thay -100 bằng 0 để CRF không bị lỗi (0=O, nhưng vị trí -100 bị mask nên không ảnh hưởng)
        safe_labels = torch.where(
            sub_labels == -100,
            torch.tensor(0, device=sub_labels.device),
            sub_labels,
        )

        loss = -self.crf(sub_emissions, safe_labels, mask=crf_mask, reduction="mean")

        return (loss, predictions)

    def predict(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
    ) -> list[list[int]]:
        """
        Inference: trả về list of tag ID sequences.

        Args:
            input_ids: (batch_size, seq_len)
            attention_mask: (batch_size, seq_len)

        Returns:
            List of tag ID sequences, bỏ qua padding positions
        """
        self.eval()
        with torch.no_grad():
            outputs = self.phobert(input_ids=input_ids, attention_mask=attention_mask)
            sequence_output = outputs.last_hidden_state
            emissions = self.ner_classifier(sequence_output)
            predictions = self.crf.decode(emissions, mask=attention_mask.bool())

        return predictions


if __name__ == "__main__":
    print("=" * 60)
    print("Test PhobertCRFNer")
    print("=" * 60)

    BATCH_SIZE = 2
    SEQ_LEN = 128
    NUM_NER_TAGS = 3

    model = PhobertCRFNer(num_ner_tags=NUM_NER_TAGS)
    model.eval()

    # Dummy input
    dummy_input_ids = torch.randint(low=0, high=64000, size=(BATCH_SIZE, SEQ_LEN))
    dummy_attention_mask = torch.ones((BATCH_SIZE, SEQ_LEN), dtype=torch.long)
    dummy_ner_labels = torch.randint(low=0, high=NUM_NER_TAGS, size=(BATCH_SIZE, SEQ_LEN))

    # Gán -100 cho một số vị trí (sub-word simulation)
    dummy_ner_labels[:, 5] = -100
    dummy_ner_labels[:, 12] = -100
    dummy_ner_labels[:, 20:23] = -100

    # --- Inference (no labels) ---
    print("--- Inference (no labels) ---")
    (predictions,) = model(
        input_ids=dummy_input_ids,
        attention_mask=dummy_attention_mask,
    )
    print(f"  type      : {type(predictions)}")
    print(f"  batch count: {len(predictions)}")
    print(f"  seq[0] len: {len(predictions[0])}")
    print(f"  seq[0][:10]: {predictions[0][:10]}")

    # --- Training (with labels) ---
    print("\n--- Training (with labels) ---")
    loss, decoded = model(
        input_ids=dummy_input_ids,
        attention_mask=dummy_attention_mask,
        ner_labels=dummy_ner_labels,
    )
    print(f"  loss      : {loss.item():.4f}")
    print(f"  decoded len[0]: {len(decoded[0])}")
    print(f"  decoded[0][:10]: {decoded[0][:10]}")

    # --- predict() method ---
    print("\n--- predict() method ---")
    preds_list = model.predict(dummy_input_ids, dummy_attention_mask)
    print(f"  type      : {type(preds_list)}")
    print(f"  seq[0][:10]: {preds_list[0][:10]}")
    print(f"  seq[1][:10]: {preds_list[1][:10]}")

    print("=" * 60)
    print("Test hoàn tất!")
