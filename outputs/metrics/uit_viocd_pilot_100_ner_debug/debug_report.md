# UIT-ViOCD Pilot 100 NER Debug Report

## Summary
- Train COMP token percent: 25.03%
- Test COMP token percent: 18.08%
- Predictions CSV exists: False
- Possible decode misalignment: True
- Class weight detected: False

## Dataset Label Distribution
| split | records | tokens | O | B-COMP | I-COMP | %O | %COMP | with_comp | without_comp | spans | avg_span_len | max_span_len |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| train | 80 | 2661 | 1995 | 136 | 530 | 74.97 | 25.03 | 76 | 4 | 136 | 4.8971 | 14 |
| val | 9 | 301 | 210 | 16 | 75 | 69.77 | 30.23 | 9 | 0 | 16 | 5.6875 | 13 |
| test | 11 | 437 | 358 | 17 | 62 | 81.92 | 18.08 | 10 | 1 | 17 | 4.6471 | 11 |

## Prediction Distribution
| type | O | B-COMP | I-COMP | rows_with_comp |
| --- | --- | --- | --- | --- |
| missing | Predictions CSV not found |  |  |  |

## Train Script Check
- label2id: `{'O': 0, 'B-COMP': 1, 'I-COMP': 2}`
- id2label source: `src.evaluation.evaluate_ner.ID2LABEL`
- loss ignore_index=-100: `True`
- class weight: `False`
- subword alignment: `first_subword_only`
- model num labels default: `3`
- classifier uses num labels: `True`
- evaluate uses model.predict: `True`
- predict filters by attention mask only: `True`

## Examples: Gold COMP But Pred All O
- No examples available.

## Possible Causes
- Train split imbalanced: COMP tokens only 25.03% of labeled tokens; unweighted CE can favor O.
- Evaluation decode is likely misaligned: train labels only first subword, but model.predict returns special tokens and all subwords using attention_mask only.
- No class weights detected in the NER loss; minority B/I-COMP labels are not upweighted.

## Recommended Next Actions
- Sync the Kaggle predictions CSV to the expected path, or rerun this script with --predictions-csv.
- Fix/evaluate prediction decoding so predicted tags are selected at the same positions as non -100 gold labels.
- Run a tiny overfit test on 5-10 records after decode fix to verify the model can learn B-COMP/I-COMP.
- Consider weighted CrossEntropy or focal loss if predictions remain all O after decode is corrected.
- Log train-time per-label prediction counts after each epoch before changing architecture.
