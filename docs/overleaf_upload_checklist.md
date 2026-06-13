# Overleaf Upload Checklist

This checklist is for uploading the revised UIT-ViOCD complaint span extraction report to Overleaf.

## Required Files to Upload

Upload these files:

- `docs/revised_report_acl_v1.tex`
- `custom.bib`
- `figures/annotation_pipeline.png`
- `figures/phobert_ner_architecture.png`
- `figures/ner_method_comparison.png`
- `figures/ner_token_f1_comparison.png`
- `figures/full_test_label_distribution.png`
- `figures/dataset_span_statistics.png`

ACL style files:

- The LaTeX file uses `\usepackage[preprint]{acl}`.
- No `acl.sty` file was found in this repo.
- No ACL `.bst` file such as `acl_natbib.bst` was found in this repo.
- On Overleaf, use an ACL template that already includes the required ACL style files, or upload the matching `acl.sty` and bibliography style files from the ACL template.

## Figure Include Check

The following `\includegraphics` paths are used in `docs/revised_report_acl_v1.tex`:

| Figure path in TeX | Exists in repo | Upload required |
| --- | --- | --- |
| `figures/dataset_span_statistics.png` | Yes | Yes |
| `figures/annotation_pipeline.png` | Yes | Yes |
| `figures/phobert_ner_architecture.png` | Yes | Yes |
| `figures/ner_method_comparison.png` | Yes | Yes |
| `figures/ner_token_f1_comparison.png` | Yes | Yes |
| `figures/full_test_label_distribution.png` | Yes | Yes |

No included figure file is missing locally.

## Bibliography Check

The report uses:

```latex
\bibliography{custom}
```

`custom.bib` exists in the repo root.

Citation keys used in `docs/revised_report_acl_v1.tex`:

- `viocd2021`
- `phobert2020`

Citation keys available in `custom.bib`:

- `viocd2021`
- `phobert2020`

Missing citation keys: none.

## ACL Style File Check

Search result:

- `acl.sty`: not found in repo
- `acl_natbib.bst`: not found in repo
- other `.bst` files: not found in repo

Recommended handling:

- Option 1: Create the Overleaf project from an ACL template, then replace its main `.tex` content with `docs/revised_report_acl_v1.tex`.
- Option 2: Upload the official ACL style files manually, including `acl.sty` and the required bibliography style file.

## Recommended Overleaf Structure

Suggested Overleaf project structure:

```text
main.tex
custom.bib
figures/
  annotation_pipeline.png
  phobert_ner_architecture.png
  ner_method_comparison.png
  ner_token_f1_comparison.png
  full_test_label_distribution.png
  dataset_span_statistics.png
```

Recommended rename:

- Upload `docs/revised_report_acl_v1.tex` as `main.tex`.
- Keep `custom.bib` at the same level as `main.tex`.
- Keep all PNG files under the `figures/` folder so the existing paths remain valid.

## Final Upload Checklist

- [ ] Upload `main.tex` from `docs/revised_report_acl_v1.tex`.
- [ ] Upload `custom.bib`.
- [ ] Upload the full `figures/` folder with all six PNG files.
- [ ] Ensure ACL template/style files are available in Overleaf.
- [ ] Set compiler to `pdfLaTeX`.
- [ ] Compile twice.
- [ ] Check for missing figure warnings.
- [ ] Check for missing citation or undefined reference warnings.
- [ ] Check page overflow, table width, and figure placement.
- [ ] Verify that no old Shopee/LinearSVM/MTL/CRF figures appear in the compiled PDF.

## Notes

- The current report is UIT-ViOCD-only.
- The included figures are newly generated for the revised report.
- The report should not require old figures related to Shopee, LinearSVM, multi-task learning, or CRF architecture.
