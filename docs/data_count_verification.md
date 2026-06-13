# Data count verification for UIT-ViOCD

## Files checked

- `data/raw/UIT-ViOCD/train.csv`
- `data/raw/UIT-ViOCD/val.csv`
- `data/raw/UIT-ViOCD/test.csv`
- `data/processed/uit_viocd_train.csv`
- `data/processed/uit_viocd_val.csv`
- `data/processed/uit_viocd_test.csv`
- `data/processed/uit_viocd_full_complaint_summary.json`
- `data/processed/uit_viocd_full_complaint_ner_split_summary.json`

## Raw CSV counts

| Split | CSV lines including header | Records excluding header | Complaint | Non-complaint |
|---|---:|---:|---:|---:|
| train | 4,388 | 4,387 | 2,292 | 2,095 |
| val | 549 | 548 | 283 | 265 |
| test | 550 | 549 | 279 | 270 |
| total | 5,487 | 5,484 | 2,854 | 2,630 |

Raw CSV schema observed:

- `Unnamed: 0`
- `review`
- `review_tokenize`
- `label`
- `domain`

## Processed CSV counts

| Split | CSV lines including header | Records excluding header | Complaint candidates | Non-complaint |
|---|---:|---:|---:|---:|
| train | 4,388 | 4,387 | 2,292 | 2,095 |
| val | 549 | 548 | 283 | 265 |
| test | 550 | 549 | 279 | 270 |
| total | 5,487 | 5,484 | 2,854 | 2,630 |

Processed CSV schema observed:

- `id`
- `review`
- `review_tokenize`
- `complaint_label`
- `domain`
- `split`

## Complaint candidate counts

Complaint candidates are records with `complaint_label = 1` in the processed splits.

| Split | Complaint candidates |
|---|---:|
| train | 2,292 |
| val | 283 |
| test | 279 |
| total | 2,854 |

This matches `data/processed/uit_viocd_full_complaint_summary.json`:

- `total_records`: 2,854
- `split_distribution.train`: 2,292
- `split_distribution.val`: 283
- `split_distribution.test`: 279

## Final NER split counts

From `data/processed/uit_viocd_full_complaint_ner_split_summary.json`:

| NER split | Records | Has COMP | No COMP | Tokens | COMP tokens |
|---|---:|---:|---:|---:|---:|
| train | 2,280 | 2,217 | 63 | 87,726 | 65,946 |
| val | 283 | 276 | 7 | 10,569 | 8,015 |
| test | 291 | 280 | 11 | 11,488 | 8,536 |
| total | 2,854 | 2,773 | 81 | 109,783 | 82,497 |

Split overlap ids:

- none (`overlap_ids`: `[]`)

## Conclusion

The total original review records should be reported as **5,484** for the local files used in this repo.

Reason:

- Raw CSV records excluding headers are:
  - train: 4,387
  - val: 548
  - test: 549
- Their sum is `4,387 + 548 + 549 = 5,484`.
- Processed CSV files have the same record counts.
- The complaint candidate total remains correct at **2,854**.

The number **5,485** may correspond to the published UIT-ViOCD paper/dataset description, but the local raw and processed files currently used by this project contain **5,484** records. The report should use 5,484 when describing the actual dataset files used in the experiments.

## Fixes applied

Updated `docs/revised_report_acl_v1.tex`:

- Changed dataset paragraph from `5,485 Vietnamese online reviews` to `5,484 Vietnamese online reviews`.
- Changed the total row in Table `Dataset statistics` from `5,485` to `5,484`.
- Kept complaint candidates as `2,854`.

