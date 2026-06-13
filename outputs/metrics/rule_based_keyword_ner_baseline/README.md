# Rule-based keyword NER baseline

Input test file: `data\processed\uit_viocd_full_complaint_ner_test.json`

Method: deterministic Vietnamese complaint keyword and phrase matching over tokenized reviews.

Main metrics:

- Entity Precision: `0.0135`
- Entity Recall: `0.0018`
- Entity F1: `0.0032`
- Token F1 macro: `0.1472`
- Samples: `291`
- Length mismatch count: `0`

This is a simple non-trained baseline for comparison with learned NER models.
