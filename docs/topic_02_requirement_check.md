# Topic 02 Requirement Check

This checklist evaluates the current revised report:

- `docs/revised_report_acl_v1.tex`
- `outputs/metrics/summary/ner_experiment_summary.md`
- `data/processed/uit_viocd_pilot_300_summary.json`
- `data/processed/uit_viocd_full_complaint_summary.json`

The current work is UIT-ViOCD-only. All span datasets and experimental settings are derived from UIT-ViOCD complaint reviews. Shopee Reviews and rating-derived labels are not used.

## Checklist

| Requirement | Current evidence in report | Status | Required fix if not PASS |
| --- | --- | --- | --- |
| A. Choose 02-03 datasets on the same task | The report currently presents two data settings: Pilot100 AI-assisted annotations and the full AI-assisted complaint span dataset. The repo also has Pilot300 files and summary, but the report does not yet describe Pilot300. All data settings are derived from UIT-ViOCD and use the same complaint span extraction task. | PARTIAL | Add a short paragraph/table explaining three UIT-ViOCD-derived annotation datasets/settings: Pilot100, Pilot300, and Full. Clarify that due to the UIT-ViOCD-only constraint, these are constructed annotation subsets from the same source dataset for the same task. Pilot300 can be described as a dataset construction and quality-check subset even if it is not a main training result. |
| B. Clear evaluation metrics | Section 4.6 and Section 5.3 state Entity Precision, Entity Recall, Entity-F1, Token-F1 macro, and average loss. The NER results table reports Entity-P, Entity-R, Entity-F1, Token-F1/Loss. | PASS | No required fix. Optionally add one sentence that Entity-F1 is the primary metric because exact span boundaries matter. This is already mostly present. |
| C. Proposed new method/approach | The report describes AI-assisted complaint span annotation, validation, offset repair, overlap resolving, BIO conversion, and PhoBERT NER. The Abstract, Introduction, Methodology, and Conclusion all frame the contribution as an annotation pipeline combined with PhoBERT NER evaluation. | PASS | No required fix. Keep wording clear that the contribution is not weighted loss alone. |
| D. Compare with at least 04 methods, including a modern ML method | Section 6 results table has five methods/settings: Rule-based Keyword Span Extractor, Pilot100 CE PhoBERT, Pilot100 Weighted PhoBERT, Full Weighted PhoBERT, and Full CE PhoBERT. PhoBERT is a modern transformer-based ML method. | PASS | Add one explicit sentence before/after the table: "All methods/settings are evaluated on the same complaint span extraction task." This prevents the comparison from looking like mixed tasks. |
| E. Error analysis on multiple aspects | Section 6 covers rule-based failure, O-bias/label bias, class-weighting effect, data scale effect, prediction distribution, boundary ambiguity, implicit complaints, and informal Vietnamese/teencode/spelling. It mentions domain-wise analysis only as future work, not as current analysis. It does not provide a concrete domain-wise or span-length/boundary quantitative breakdown. | PARTIAL | Add a short paragraph to Error Analysis covering domain-wise risks (app, cosmetic, fashion, mobile) and span-boundary/length issues. If no new experiment is desired, frame it as qualitative analysis from observed errors and annotation characteristics. Optionally add a small table if domain-level metrics are available later. |

## Detailed Notes

### A. Dataset Requirement

The strict wording asks for 02-03 datasets on the same task. The current report is intentionally UIT-ViOCD-only, so it should not introduce Shopee or rating-derived data just to satisfy this item. A defensible framing is:

1. Pilot100 AI-assisted complaint span dataset.
2. Pilot300 AI-assisted complaint span dataset.
3. Full AI-assisted complaint span dataset.

These are not separate original corpora. They are controlled annotation datasets/settings derived from the same UIT-ViOCD source and used for the same complaint span extraction task. This should be stated honestly.

Available Pilot300 evidence in repo:

- `data/processed/uit_viocd_pilot_300_summary.json`
- Total records: 300
- Records with spans: 262
- Records without spans: 38
- Total tokens: 10,128
- COMP tokens: 3,754
- COMP token ratio: 37.07%
- Domain distribution: app 99, cosmetic 62, fashion 84, mobile 55
- Validation pass: true

The report currently does not include these Pilot300 numbers.

### B. Metrics Requirement

The current metrics are sufficient:

- Entity Precision
- Entity Recall
- Entity-F1
- Token-F1 macro
- Average loss

Entity-F1 is correctly treated as the primary metric for exact complaint span extraction.

### C. Proposed Method Requirement

The proposed approach is sufficiently clear:

- Use UIT-ViOCD review-level labels to select complaint candidates.
- Apply AI-assisted complaint span annotation.
- Validate schema and exact offsets.
- Repair offset mismatch where safe.
- Resolve overlap before BIO conversion.
- Train/evaluate PhoBERT NER models.

The report should keep emphasizing this as the main contribution. Weighted loss is a training variant, not the main proposed method.

### D. Method Comparison Requirement

The current five-row comparison satisfies the "at least 04 methods" requirement:

1. Rule-based Keyword Span Extractor.
2. Pilot100 Unweighted PhoBERT NER.
3. Pilot100 Weighted PhoBERT NER.
4. Full Complaint Weighted PhoBERT NER.
5. Full Complaint Unweighted PhoBERT NER.

The modern machine learning method is PhoBERT, a transformer-based Vietnamese language model.

One possible weakness is that some rows are better described as dataset/training settings rather than entirely different model families. A minimal fix is to explicitly call them "methods/settings" and state that they are compared on the same task: complaint span extraction.

### E. Error Analysis Requirement

Current coverage is good but not complete enough for "many aspects" if the evaluator expects concrete categories.

Already covered:

- Rule-based baseline fails due to low exact-span recall.
- Pilot100 unweighted collapses toward O predictions.
- Weighted loss helps in low-data setting.
- Full data improves span extraction substantially.
- Prediction distribution shows tendency to predict more complaint tokens.
- Boundary ambiguity affects Entity-F1 more than Token-F1.
- Informal Vietnamese, spelling errors, teencode, mixed sentiment, and implicit complaints remain challenging.

Recommended additions:

- Domain-wise discussion: app reviews often contain software behavior complaints such as lag/crash/error; fashion/cosmetic reviews often contain product quality, mismatch, packaging, and delivery complaints; mobile reviews may involve device/spec/service issues.
- Span-boundary discussion: long complaint explanations and repeated complaints can cause overly broad spans; short implicit complaints can be missed.
- Annotation-quality discussion: AI-assisted labels improve coverage but can still contain semantically broad boundaries despite passing offset validation.

## Recommended Minimal Fixes Before Final Submission

1. Add one paragraph in Section 5.2 Dataset Splits explaining three UIT-ViOCD-derived dataset settings:
   - Pilot100
   - Pilot300
   - Full AI-assisted complaint span dataset

2. Add one sentence before the NER result table:
   - "All five methods/settings are evaluated on the same complaint span extraction task."

3. Add one short error analysis paragraph covering:
   - domain-wise differences across app, cosmetic, fashion, and mobile;
   - span-boundary/length issues;
   - implicit complaint and informal Vietnamese failure cases.

4. Keep the existing limitation wording:
   - Full span labels are AI-assisted, not fully human gold-standard labels.
   - Entity-F1 is evaluation on the constructed span dataset, not an official UIT-ViOCD benchmark.

5. Do not add Shopee or rating-derived labels back into the report.

## Does This Require More Training?

No. The report already has enough methods/settings for the comparison requirement:

- Rule-based baseline
- Pilot100 unweighted PhoBERT
- Pilot100 weighted PhoBERT
- Full weighted PhoBERT
- Full unweighted PhoBERT

No additional training is strictly required. The only recommended changes are small reporting fixes to make the rubric alignment explicit.
