# Local PDF Compile Report

## Build Setup

- Source TeX: `docs/revised_report_acl_v1.tex`
- Build TeX: `report_build/main.tex`
- Bibliography: `report_build/custom.bib`
- ACL style: `report_build/acl.sty`
- Figures folder: `report_build/figures/`

The build folder was created separately so the original report source was not modified for compilation.

## Compiler

- Requested compiler: XeLaTeX
- `latexmk`: not found in PATH
- `xelatex`: not found in PATH
- `bibtex`: not found in PATH
- `pdflatex`: not found in PATH
- `tectonic`: not found in PATH

## Compile Status

- Compile success: no
- Reason: local TeX compiler is not installed or not available in PATH.
- No LaTeX run was completed.

## Build File Checks

`report_build/main.tex` is configured for XeLaTeX:

- Uses `\usepackage{fontspec}`
- Uses `\setmainfont{TeX Gyre Termes}`
- Uses `\setsansfont{TeX Gyre Heros}`
- Uses `\setmonofont{Latin Modern Mono}`
- Does not use `\usepackage{times}`
- Does not use `\usepackage[T1]{fontenc}`
- Does not use `\usepackage[utf8]{inputenc}`
- Does not use `\usepackage{inconsolata}`

Vietnamese text with accents is preserved in the BIO example:

- `áo đẹp nhưng giao hàng chậm quá`
- `giao hàng chậm quá`
- tokens such as `áo`, `đẹp`, `hàng`, `chậm`, `quá`

## Figure Checks

All included figure paths exist under `report_build/figures/`:

- `figures/dataset_span_statistics.png`
- `figures/annotation_pipeline.png`
- `figures/phobert_ner_architecture.png`
- `figures/ner_method_comparison.png`
- `figures/ner_token_f1_comparison.png`
- `figures/full_test_label_distribution.png`

## Output PDF

- Output PDF path: `docs/revised_report_acl_v1.pdf`
- PDF created: no
- Page count: not available
- Main content pages before References: not available

## Warnings / Errors

No LaTeX warnings were produced because compilation could not start. The blocking issue is missing local TeX tooling.

To compile locally on this machine, install TeX Live or MiKTeX with XeLaTeX and BibTeX available in PATH, then run:

```powershell
cd report_build
xelatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

If `latexmk` is installed, use:

```powershell
cd report_build
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```
