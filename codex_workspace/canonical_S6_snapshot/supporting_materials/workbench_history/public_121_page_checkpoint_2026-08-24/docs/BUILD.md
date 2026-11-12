# Build and verification

## Overleaf

- Main document: `main.tex`
- Compiler: pdfLaTeX
- TeX Live: latest available
- Expected annotated result: 121 US-letter pages
- Composition: one reader guide, 108 unchanged manuscript pages, and 12 annotation pages
- Expected clean result: 108 US-letter pages

The local reference PDFs use MiKTeX pdfTeX 1.40.29. Overleaf uses TeX Live, so cross-distribution byte identity is not expected. Page count, page-one layout, badge links, and source page 71 (physical annotated PDF page 72) must be checked after import.

## Local builds from the project root

```powershell
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error main.tex
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error clean_transcription.tex
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error manuscript/s6_canonical_annotated_standalone.tex
latexmk -pdf -file-line-error -interaction=nonstopmode -halt-on-error manuscript/annotated_maintainable.tex
latexmk -cd -pdf -file-line-error -interaction=nonstopmode -halt-on-error manuscript/canonical_modular/s6_canonical.tex
```

`main.tex` is the canonical maintainable edition. `manuscript/annotated_maintainable.tex` is a small compatibility wrapper around it. The archival one-file edition is regenerated with:

```powershell
python reproducibility/annotated_qa/build_standalone.py
```

The modular source is retained for reconstruction provenance. Its inputs are directory-relative, so its own scripts work; direct root builds use `latexmk -cd`. The monolithic sources remain preferred because a prior modular MiKTeX build exposed the documented page-71 portability defect.

## Structural QA

```powershell
python -m pip install -r reproducibility/annotated_qa/requirements.txt
python reproducibility/annotated_qa/verify_pdf.py `
  clean_transcription.pdf main.pdf `
  --standalone manuscript/s6_canonical_annotated_standalone.pdf `
  --output reproducibility/annotated_qa/verification.json
```

The verifier checks the one-page physical offset, all page sizes and counts, absence of a guide-page badge, all 108 badge links and destinations, unchanged manuscript text and coordinates outside badge regions, and equivalence of the preferred annotated source forms. See `docs/QA_RECEIPT.md` for the recorded release result.
