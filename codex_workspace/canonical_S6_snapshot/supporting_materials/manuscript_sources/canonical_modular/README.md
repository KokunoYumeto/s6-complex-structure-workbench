# Modular canonical reconstruction - source pages 1-108

This directory holds the ten-packet modular reconstruction of the supplied 108-page PDF. It is reconstruction provenance, not the author's original TeX and not the preferred annotated entry point.

## Contents

- `s6_canonical.tex` - modular assembler.
- `parts/packet_01_body.tex` through `packet_10_body.tex` - reconstructed page bodies.
- `scripts/generate_monolithic.py` - regenerates the modular directory's local monolith.
- `scripts/build.sh` and `scripts/verify.sh` - original reproducibility helpers.
- `../reconstruction_audit/` - source-fidelity receipts, page ledger, and release audit.
- `../source_pdfs/` - supplied manuscript authority and reassembled comparison PDF.
- project-root `original_clean_transcription.tex` - curated self-contained clean monolith.

## Direct build

From the public project root:

```powershell
latexmk -cd -pdf -file-line-error -interaction=nonstopmode -halt-on-error supporting_materials/manuscript_sources/canonical_modular/s6_canonical.tex
```

From this directory, ordinary `latexmk -pdf s6_canonical.tex` also works because all ten `\input` paths are directory-relative.

## Scope

The source-fidelity audit establishes correspondence with the supplied
manuscript PDF. It does not prove the mathematical claims. A prior modular
MiKTeX build exposed the page-71 text-placement portability defect recorded by
Reviewer C: a driver newline after the packet-01 `\input` contributed an
unintended space token that was absent from the generated monolith. The driver
now suppresses that newline explicitly, and `scripts/verify.sh` requires the
modular and generated-monolithic PDFs to be byte-identical so the defect cannot
re-enter unnoticed. The project-root monoliths remain the preferred public
reading entry points.
