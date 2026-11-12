# S6 Mathematical Proof-Audit Evidence Bundle

## Disposition

**MAJOR REVISION - MAIN THEOREM NOT CERTIFIED.**

The separate source-fidelity audit passes all 108 pages: the canonical LaTeX and PDF reproduce the supplied authority. The mathematical audit reaches a different conclusion. Thirty-eight finite exact-algebra checks pass, but the manuscript's identification of the constructed threefold with the standard smooth six-sphere still depends on integral geometric maps that this audit did not independently certify at chain level.

The unresolved load-bearing items are indexed as R1-R4 in `evidence/ledgers/S6_PROOF_RISK_LEDGER.csv`:

- the global equivariant cusp-collapse model;
- the integral geometric specialization map;
- the based van Kampen inclusion maps, drifts, primitivity, and signs;
- the identification of the printed Mayer-Vietoris and Leray matrices with the actual geometric boundary maps.

## Start here

1. Read `reports/S6_MATHEMATICAL_PROOF_AUDIT.pdf` or the matching Markdown file.
2. Read `reports/S6_MATHEMATICAL_PROOF_AUDIT_SUMMARY.json` for a machine-readable synopsis.
3. Open `evidence/annotations/S6_AUDIT_ANNOTATED_MANUSCRIPT.pdf` for page-level status notes.
4. Open `evidence/critical_pages/S6_CRITICAL_EVIDENCE_PAGES.pdf` for the 37 load-bearing pages.
5. Inspect `evidence/ledgers/S6_THEOREM_AUDIT_LEDGER.csv` and `evidence/ledgers/S6_PROOF_RISK_LEDGER.csv`.
6. Run `scripts/run_all_checks.sh` from the bundle root.

## Included material

### Reports

- `reports/S6_MATHEMATICAL_PROOF_AUDIT.md`
- `reports/S6_MATHEMATICAL_PROOF_AUDIT.pdf`
- `reports/S6_MATHEMATICAL_PROOF_AUDIT_SUMMARY.json`
- `reports/S6_CANONICAL_AUDIT_REPORT.md`
- `reports/S6_CANONICAL_AUDIT_SUMMARY.json`

### User-visible session writing

- `session/ASSISTANT_VISIBLE_OUTPUTS.md`
- `session/ASSISTANT_VISIBLE_OUTPUTS.pdf`

This is the assistant prose shown to the user in the session. It excludes private reasoning and transient tool diagnostics.

### Canonical manuscript

- `source/s6_canonical_full_108_pages.tex`
- `source/s6_canonical_modular_main_108_pages.tex`
- `source/s6_canonical_108_pages.pdf`

The entire earlier source-fidelity release is also unpacked under `canonical_release/`, including its authority PDF, parts, contact sheets, page ledger, source-verification data, build logs, and build/verification scripts.

### Exact algebra evidence

- `scripts/reproduce_core_checks.py`
- `evidence/core_checks/core_checks.json`
- `evidence/core_checks/core_checks.txt`

The script performs exact integer/rational calculations. It checks the printed monodromy matrices, orders, determinants, nilpotent logarithm, contragredient relation, Smith forms, coinvariants, invariant lattices, invariant alternating form, induced form, wedge-power ranks and saturation, selected exterior-power coinvariants, twist arithmetic, and numerical Riemann-Roch consistency.

These checks do not create the missing geometric morphisms. The exact scope limitation is written into both result files.

### Critical source evidence

- `evidence/source_extracts/source_pages_040_062.tex`
- `evidence/source_extracts/source_pages_095_108.tex`
- `evidence/source_extracts/pdf_text_pages_040_062.txt`
- `evidence/source_extracts/pdf_text_pages_095_108.txt`
- `evidence/critical_pages/manuscript_pages_040_062.pdf`
- `evidence/critical_pages/manuscript_pages_095_108.pdf`
- `evidence/critical_pages/S6_CRITICAL_EVIDENCE_PAGES.pdf`
- `evidence/critical_pages/CRITICAL_PAGE_INDEX.csv`

### Page-level and theorem-level classifications

- `evidence/annotations/S6_AUDIT_ANNOTATED_MANUSCRIPT.pdf`
- `evidence/annotations/ANNOTATION_INDEX.csv`
- `evidence/ledgers/S6_THEOREM_AUDIT_LEDGER.csv`
- `evidence/ledgers/S6_PROOF_RISK_LEDGER.csv`

The annotated PDF preserves the original page content. Each page has a narrow right-margin status and a popup note. The classification does not change the manuscript text.

## Verification

From the extracted bundle root:

```bash
bash scripts/run_all_checks.sh
```

The verifier:

- checks every static file against `manifests/SHA256SUMS.txt`;
- reruns the 38 exact core checks in a temporary directory and byte-compares the results;
- verifies the canonical and annotated PDFs have 108 pages;
- verifies the annotated PDF has 108 audit annotations;
- verifies the critical-evidence PDF has 37 pages;
- verifies the theorem ledger contains 92 rows with the recorded status totals;
- verifies the canonical TeX has exactly 108 source-page start and end markers.

## Audit boundary

This bundle documents an independent proof audit. It is not a journal's anonymous peer-review record. The PASS status in the canonical release means that the LaTeX/PDF accurately reproduces the supplied source pages. It does not mean that the main mathematical theorem is proved.
