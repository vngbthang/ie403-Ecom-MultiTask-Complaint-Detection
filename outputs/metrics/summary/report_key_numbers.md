# Report Key Numbers - UIT-ViOCD NER

## Dataset Statistics

- Pilot 100 records: `100`
- Full complaint records: `2854`
- Full records with spans: `2773`
- Full records without spans: `81`
- Full total tokens: `109783`
- Full COMP token count: `82497`
- Full COMP token ratio: `0.7515`

Domain distribution:
- app: `1510`
- cosmetic: `475`
- fashion: `732`
- mobile: `137`

Split for model training:
- train: `2280` records, `87726` tokens, `65946` COMP tokens
- val: `283` records, `10569` tokens, `8015` COMP tokens
- test: `291` records, `11488` tokens, `8536` COMP tokens

## Annotation Pipeline Statistics

- Dataset source: `UIT-ViOCD` only.
- Pilot 100 was used to validate the AI-assisted span annotation workflow.
- Batch 200 was added and manually fixed for overlap cases before pilot300.
- Remaining 2554 complaint reviews were processed in 13 AI annotation batches.
- Automatic validation, offset repair, and overlap resolving were applied before merging.
- Final total spans: `10195`
- Average spans per record: `3.5722`

## Experiment Results

| experiment_name | dataset | train_records | test_records | loss_type | epochs | entity_precision | entity_recall | entity_f1 | token_f1_macro | avg_loss | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pilot100 Unweighted PhoBERT NER | UIT-ViOCD pilot 100 | 100 |  | CrossEntropy | 3 | 0.0000 | 0.0000 | 0.0000 | 0.3002 | 0.6437 | model biased to O on small pilot data |
| Pilot100 Weighted PhoBERT NER | UIT-ViOCD pilot 100 | 100 |  | Weighted CrossEntropy | 7 | 0.0893 | 0.2941 | 0.1370 | 0.5845 | 0.3660 | class weights helped the model predict COMP labels but data size remained small |
| Full Complaint Weighted PhoBERT NER | UIT-ViOCD full AI-assisted complaint span dataset | 2280 | 291 | Weighted CrossEntropy | 5 | 0.7937 | 0.9045 | 0.8455 | 0.8620 | 0.2486 | best result after expanding annotation to all complaint reviews |

Loaded metrics files:
- `outputs\metrics\uit_viocd_pilot_100_phobert_ner_3epoch_clean\metrics\phobert_ner_single_task.json`
- `outputs\metrics\uit_viocd_pilot_100_phobert_ner_weighted_10epoch\metrics\phobert_ner_single_task.json`
- `outputs\metrics\uit_viocd_full_complaint_phobert_ner_weighted_5epoch\metrics\phobert_ner_single_task.json`

## Key Findings

- Best available Entity F1: `0.8455` from `Full Complaint Weighted PhoBERT NER`.
- Expanding from pilot annotations to the full complaint span dataset substantially improved NER performance.
- Weighted CrossEntropy was used to reduce bias toward the O label.

## Limitations To Mention In Report

- Full span labels are AI-assisted annotations, not fully human gold-standard labels.
- Automatic validation, offset repair, overlap resolving and partial manual review were used to improve consistency.
- Results should be interpreted as evaluation on the constructed AI-assisted span dataset.
- Some pilot metrics may be absent locally if Kaggle outputs were not copied back.
