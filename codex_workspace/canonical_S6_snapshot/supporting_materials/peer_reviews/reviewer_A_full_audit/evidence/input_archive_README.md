# S6 Canonical LaTeX Reconstruction — Pages 1–108

This directory contains a consolidated, independently reconstructed LaTeX source for the complete 108-page authority PDF supplied in ten audited packets. It is not the author's original TeX source.

## Primary deliverables

- `s6_canonical_full.tex` — single-file, self-contained canonical LaTeX source.
- `s6_canonical.tex` plus `parts/` — modular form of the same source.
- `pdf/s6_canonical.pdf` in the release ZIP — audited compiled PDF, 108 letter-size pages.
- `authority/s6_authority_reassembled.pdf` — clean reassembly of the ten supplied authority slices.
- `audit/AUDIT_REPORT.md` — audit method, findings, metrics, and scope.
- `audit/PAGE_AUDIT.csv` — one audit row for every physical page.

The modular and monolithic sources compile to byte-identical PDFs in the audited environment.

## Build

Required: a reasonably complete TeX Live installation with `latexmk`, `pdftex`, and the packages named in the preamble.

```bash
./scripts/build.sh
```

The script regenerates the monolithic source from the modular tree, builds both forms, scans both logs, and verifies that both PDFs are byte-identical. Outputs are written to `build/` and `build_monolithic/`.

Direct single-file build:

```bash
export SOURCE_DATE_EPOCH=1704067200
export FORCE_SOURCE_DATE=1
export TZ=UTC
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -file-line-error -outdir=build_full s6_canonical_full.tex
```

## Verification

```bash
./scripts/verify.sh
```

The verification first validates `SHA256SUMS.txt`, then checks page count and size, page markers and anchors, placeholder absence, log cleanliness, font embedding, and equality of the modular and monolithic outputs.

## Audit disposition

All 108 pages have complete upstream page receipts and were independently rechecked as 200-dpi authority/canonical pairs. No unresolved source-fidelity discrepancy was found. Packets 6 and 9 contain stale internal checksum metadata; those defects are documented rather than hidden, and the consolidated release has a newly generated valid checksum ledger.

The audit establishes fidelity to the supplied authority PDF. It does not independently prove the mathematical results or validate the external bibliography.
