# Cleanup check for `docs/revised_report_acl_v1.tex`

## Old-story keyword check

Checked the full LaTeX file for the following old-story keywords:

- `Shopee`
- `rating`
- `rating-derived`
- `LinearSVM`
- `Logistic Regression`
- `Naive Bayes`
- `Macro-F1`
- `Complaint-F1`
- `7,817`
- `1,564`
- `400 training`
- `100 test`
- `189`
- `only-ner-matched`
- `alpha`
- `L_cls`
- `L_ner`
- `classification head`
- `multi-task`
- `CRF`

Result:

- No old Shopee/rating/classification-result keywords remain.
- No old MTL objective keywords remain.
- No old subset-size keywords remain.
- `CRF` and `multi-task` remain only in Future Work context.

## Allowed remaining keywords and context

Allowed remaining mentions:

- `CRF`: appears only in Future Work as a possible future sequence labeling baseline, specifically `PhoBERT+CRF` or `transformer-CRF`.
- `multi-task`: appears only in Future Work as a future extension for jointly modeling review-level complaint classification and span extraction.

These are not presented as the current main method or current main results.

## Citation check

Detected citation keys in `docs/revised_report_acl_v1.tex`:

- `viocd2021`
- `phobert2020`

Detected keys in `custom.bib`:

- `viocd2021`
- `phobert2020`

Missing citation keys:

- None.

Applied fix:

- Created `custom.bib` with entries for `viocd2021` and `phobert2020`, matching the citation keys used in the LaTeX file.

## Label/ref check

Detected labels:

- `tab:dataset-statistics`
- `tab:span-dataset-statistics`
- `fig:phobert-ner-architecture`
- `tab:experimental-setup`
- `tab:ner-results-new`
- `tab:test-label-distribution`

Duplicate labels:

- None.

Refs without matching labels:

- None.

Unused labels:

- `fig:phobert-ner-architecture`

This is not a compile blocker. It only means the figure is labeled but not referenced in text yet.

## LaTeX risk check

Checked for:

- Unescaped `%` in text.
- Suspicious unescaped underscores in normal text.
- Obvious table column count mismatches.
- Missing labels for existing refs.

Result:

- No unescaped `%` found.
- No unescaped underscore issue found.
- No obvious table column mismatch found.
- No missing ref target found.

## Recommended fixes applied

- Added `custom.bib` because the LaTeX file uses `\bibliography{custom}` and cites `viocd2021` and `phobert2020`.
- No direct content edits were needed in `docs/revised_report_acl_v1.tex` during this cleanup pass.

## Remaining issues

- `fig:phobert-ner-architecture` is currently not referenced in text. This is safe for compilation, but the paper can be improved later by adding a sentence such as `Figure~\ref{fig:phobert-ner-architecture} illustrates the model architecture.`
- Dataset count verification was later completed in `docs/data_count_verification.md`. The local raw and processed files contain `5,484` records, so `docs/revised_report_acl_v1.tex` now reports `5,484` original reviews.

## Compile readiness

The file is ready for a first LaTeX compile attempt from the repository root, assuming the ACL style package is available in the LaTeX environment.
