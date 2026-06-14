# Vietnamese Complaint Span Extraction on UIT-ViOCD with AI-assisted Annotation

## Project Overview

This project extends **UIT-ViOCD** from review-level complaint detection to
complaint span extraction for Vietnamese e-commerce reviews.

The original UIT-ViOCD dataset provides binary review-level labels:
`Complaint` and `Non-Complaint`. These labels indicate whether a review contains
a complaint, but they do not identify the exact text region that expresses the
complaint. This repository builds an AI-assisted span annotation pipeline to add
complaint spans, validate character offsets, repair offset mismatches, resolve
overlapping spans, convert spans to BIO labels, and train PhoBERT NER models for
complaint span extraction.

The constructed span labels are **AI-assisted annotations**, not fully
human-verified gold-standard labels. Results should be interpreted as evaluation
on the constructed AI-assisted span dataset, not as an official UIT-ViOCD
benchmark.

## Current Task

Given a Vietnamese review, the current task is to predict token-level BIO tags:

- `O`: token outside a complaint span
- `B-COMP`: first token of a complaint span
- `I-COMP`: continuation token inside a complaint span

The final model extracts one or more complaint spans from review text.

## Key Contributions

- Standardize UIT-ViOCD raw splits into processed CSV files.
- Select complaint reviews from UIT-ViOCD as span annotation candidates.
- Build AI-assisted complaint span annotation requests.
- Validate annotation schema and exact character offsets.
- Repair offset mismatches when span text can be found in the original review.
- Resolve overlapping complaint spans before BIO conversion.
- Convert character-level spans into token-level BIO labels.
- Build pilot and full AI-assisted UIT-ViOCD complaint span datasets.
- Train and evaluate PhoBERT NER models and a rule-based keyword baseline.
- Generate experiment summaries and report figures for the final paper.

## Project Structure

```text
data/
  raw/UIT-ViOCD/                    Raw UIT-ViOCD train/val/test CSV files
  processed/                        Processed CSV, candidates, annotations, BIO, NER JSON

docs/                               LaTeX report and project documentation
figures/                            Figures used in the report
outputs/metrics/                    Current experiment metrics and predictions

src/
  data_processing/                  Data preparation, annotation, validation, repair, merge
  training/                         PhoBERT NER training
  models/                           PhoBERT token classifier and optional sequence model
  evaluation/                       NER metrics, rule baseline, summaries, report figures

scripts/                            Small runner scripts for smoke checks
```

## Main Pipeline

1. Prepare UIT-ViOCD raw splits.
2. Select complaint candidates from UIT-ViOCD.
3. Build AI-assisted span annotation requests.
4. Validate annotation JSONL files.
5. Repair span offset mismatches.
6. Resolve overlapping spans.
7. Convert validated spans to BIO labels.
8. Merge the full UIT-ViOCD complaint NER dataset.
9. Train PhoBERT NER.
10. Evaluate rule-based and PhoBERT NER variants.
11. Build summary metrics and report figures.

## Important Scripts

### Data Processing

- `src/data_processing/prepare_uit_viocd.py`
- `src/data_processing/prepare_uit_annotation.py`
- `src/data_processing/validate_span_annotations.py`
- `src/data_processing/repair_span_offsets.py`
- `src/data_processing/convert_spans_to_bio.py`
- `src/data_processing/process_full_annotation_batches.py`
- `src/data_processing/resolve_full_annotation_overlaps.py`
- `src/data_processing/merge_full_uit_viocd_ner_dataset.py`

### Training

- `src/training/train_phobert_ner.py`

### Evaluation and Reporting

- `src/evaluation/evaluate_rule_based_ner_baseline.py`
- `src/evaluation/build_ner_experiment_summary.py`
- `src/evaluation/create_report_figures.py`

## Main Results

The following results are evaluated on the constructed AI-assisted complaint
span datasets derived from UIT-ViOCD.

| Method | Dataset setting | Entity-F1 | Token-F1 |
|---|---:|---:|---:|
| Rule-based keyword span extractor | Full test split | 0.0032 | 0.1472 |
| PhoBERT NER with CE | Pilot100 | 0.0000 | 0.3002 |
| PhoBERT NER with weighted CE | Pilot100 | 0.1370 | 0.5845 |
| PhoBERT NER with weighted CE | Full complaint dataset | 0.8455 | 0.8620 |
| PhoBERT NER with CE | Full complaint dataset | **0.8561** | **0.8732** |

Key observation: class weighting helped in the low-data Pilot100 setting, but
on the full AI-assisted complaint span dataset, the unweighted PhoBERT NER model
performed best.

## Limitations

- The span labels are AI-assisted and are not fully human gold-standard labels.
- Automatic validation checks schema and offsets, but it cannot guarantee
  semantic correctness of every span boundary.
- Offset repair and overlap resolving improve consistency but do not replace
  complete manual annotation review.
- The reported scores measure performance on the constructed span dataset, not
  official performance on the original UIT-ViOCD review-level task.
- Informal Vietnamese, spelling variants, teencode, implicit complaints, and
  mixed-sentiment reviews remain challenging.

## How to Reproduce

Run commands from the repository root.

Prepare processed UIT-ViOCD files:

```bash
python -m src.data_processing.prepare_uit_viocd
```

Export complaint candidates:

```bash
python -m src.data_processing.prepare_uit_annotation
```

Process full annotation batches after AI outputs are available:

```bash
python -m src.data_processing.process_full_annotation_batches
python -m src.data_processing.resolve_full_annotation_overlaps
python -m src.data_processing.merge_full_uit_viocd_ner_dataset
```

Train PhoBERT NER on the full constructed dataset:

```bash
python -m src.training.train_phobert_ner \
  --train-json data/processed/uit_viocd_full_complaint_ner_train.json \
  --val-json data/processed/uit_viocd_full_complaint_ner_val.json \
  --test-json data/processed/uit_viocd_full_complaint_ner_test.json \
  --output-dir outputs/metrics/uit_viocd_full_complaint_phobert_ner_unweighted_5epoch \
  --epochs 5 \
  --batch-size 8 \
  --learning-rate 2e-5 \
  --model-name vinai/phobert-base-v2 \
  --no-save-checkpoint
```

Evaluate the rule-based baseline:

```bash
python -m src.evaluation.evaluate_rule_based_ner_baseline
```

Build experiment summaries and report figures:

```bash
python -m src.evaluation.build_ner_experiment_summary
python -m src.evaluation.create_report_figures
```

## Notes

- The project currently focuses on complaint span extraction using UIT-ViOCD.
- The full constructed dataset contains only complaint reviews for NER training
  and evaluation.
- Non-complaint reviews are preserved in the processed UIT-ViOCD CSV files for
  dataset traceability but are not used as NER span training samples.
- The optional sequence-labeling model files are retained only for future
  experiments; they are not the main method in the current report.
