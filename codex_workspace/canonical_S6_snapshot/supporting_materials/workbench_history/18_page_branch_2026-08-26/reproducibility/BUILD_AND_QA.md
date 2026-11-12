# Build and QA receipt

Date: 26 August 2026  
Root document: `main.tex`  
Engine: pdfLaTeX via MiKTeX 26.5 / `latexmk` 4.88  

## Commands

The live notebook was compiled outside the source tree with:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir=<external-build-directory> -cd main.tex
```

The frozen baselines were compiled independently with the same command,
using `audit_baseline/annotated_audit.tex` and
`audit_baseline/clean_transcription.tex` as roots.

## Results

| Artifact | Pages | Result |
|---|---:|---|
| `main.tex` | 16 | pass; final log has no fatal, LaTeX, package, reference, citation, or box warnings |
| `audit_baseline/annotated_audit.tex` | 121 | pass; frozen source preserved |
| `audit_baseline/clean_transcription.tex` | 108 | pass; frozen source preserved |

All 16 pages of the live notebook were rasterized and inspected as a contact
sheet, with the title/contents page, status ledger, exact-algebra page,
duality proof, base-change proof, candidate-status page, and final references
also inspected at full rendered resolution.  There is no clipping, overlap,
split status token, blank page, or unreadable equation.  Generated `.aux`,
`.log`, `.out`, `.toc`, `.fls`, and `.fdb_latexmk` files remain outside this
source tree.

## Remote Overleaf verification

The synchronized owner project is
`https://www.overleaf.com/project/6a8e36c973b98042c96f85ce`, titled
“S6 Proof Repair and Disproof Workbench — Private”.  It is distinct from the
public audit project.  Root `main.tex` was compiled with pdfLaTeX to 16 pages;
the Overleaf diagnostics panel reported `All logs 0`, `Errors 0`,
`Warnings 0`, and `Info 0`.  Sharing controls were neither opened nor changed.

## Evidence boundary

The exact algebra is certified for the printed matrices.  The topology and
Section~10 conclusions remain typed `CONDITIONAL` or `OPEN` until the named
geometric and analytic bridge lemmas are independently discharged.  This
receipt records compilation, not theorem validity.

## Package round trip

The upload archive is
`s6_proof_repair_disproof_workbench_private_2026-08-26.zip`.

```text
ZIP entries: 27
Round-trip files: 27
Unsafe ZIP paths: 0
Tree differences after extraction: 0
SHA-256 mismatches after extraction: 0
```

The complete per-file manifest is `SHA256SUMS.txt`.  The archive's SHA-256 is
kept in the adjacent sidecar file
`s6_proof_repair_disproof_workbench_private_2026-08-26.zip.sha256`, so the
manifest remains non-self-referential.
