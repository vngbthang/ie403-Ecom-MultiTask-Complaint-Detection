import torch
import torch.nn as nn
from transformers import AutoModel
from torchcrf import CRF


class PhobertCRFMultiTask(nn.Module):
    def __init__(self, num_classes=2, num_ner_tags=9):
        super(PhobertCRFMultiTask, self).__init__()

        self.phobert = AutoModel.from_pretrained("vinai/phobert-base-v2")
        hidden_size = self.phobert.config.hidden_size

        self.classifier = nn.Linear(hidden_size, num_classes)
        self.ner_classifier = nn.Linear(hidden_size, num_ner_tags)
        self.crf = CRF(num_ner_tags, batch_first=True)

    def forward(self, input_ids, attention_mask, class_labels=None, ner_labels=None):
        outputs = self.phobert(input_ids=input_ids, attention_mask=attention_mask)
        sequence_output = outputs.last_hidden_state

        cls_output = sequence_output[:, 0, :]
        classification_logits = self.classifier(cls_output)


        ner_emissions = self.ner_classifier(sequence_output)
        crf_mask = attention_mask.bool()
        ner_predictions = self.crf.decode(ner_emissions, mask=crf_mask)

        return classification_logits, ner_predictions


if __name__ == "__main__":
    print("Dummy Test")

    BATCH_SIZE = 2
    SEQ_LEN = 128
    NUM_CLASSES = 2
    NUM_NER_TAGS = 9
    VOCAB_SIZE = 64000

    model = PhobertCRFMultiTask(num_classes=NUM_CLASSES, num_ner_tags=NUM_NER_TAGS)
    model.eval()

    dummy_input_ids = torch.randint(low=0, high=VOCAB_SIZE, size=(BATCH_SIZE, SEQ_LEN))
    dummy_attention_mask = torch.ones((BATCH_SIZE, SEQ_LEN), dtype=torch.long)
    dummy_class_labels = torch.randint(low=0, high=NUM_CLASSES, size=(BATCH_SIZE,))
    dummy_ner_labels = torch.randint(low=0, high=NUM_NER_TAGS, size=(BATCH_SIZE, SEQ_LEN))

    with torch.no_grad():
        logits, ner_preds = model(
            input_ids=dummy_input_ids,
            attention_mask=dummy_attention_mask,
            class_labels=dummy_class_labels,
            ner_labels=dummy_ner_labels
        )

    print(f"Shape của classification_logits: {list(logits.shape)}")
    print(f"Kích thước Batch NER đầu ra: {len(ner_preds)}")
    print(f"Kích thước chuỗi NER của sequence đầu tiên: {len(ner_preds[0])}")