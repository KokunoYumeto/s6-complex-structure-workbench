# S6 integrated proof-repair and validation update

Date: 25 August 2026

This directory is a dated corrective update to the earlier proof-audit evidence bundle. It integrates the supplied Product/Codex progress record with an independent re-reading of the corresponding arguments in the canonical 108-page source.

## Start here

1. `reports/S6_TWO_PAGE_MATHEMATICAL_STATUS.pdf` — exact two-page mathematician-facing status.
2. `reports/S6_MATHEMATICAL_RESULTS_SO_FAR.pdf` — five-page mathematical entry map.
3. `reports/S6_CORRECTIVE_PEER_REVIEW_ADDENDUM.pdf` — seven-page correction to the earlier verdict.
4. `reports/S6_MATHEMATICAL_PROOF_AUDIT_REVISED.pdf` — nineteen-page integrated edition containing the correction, results map, and original audit preserved as issued.
5. `evidence/annotations/S6_REVISED_AUDIT_ANNOTATED_MANUSCRIPT.pdf` — revised status overlay on all 108 canonical pages.
6. `reports/S6_INTEGRATED_VALIDATION_SUMMARY.json` — machine-readable status summary.

## Central correction

The earlier audit treated the equality of the nearby-cycle specialization map `sp^q` with the explicit collapse pullback `c^*` as indispensable to the topology. The canonical source proves `sp^q` independently in Appendix B and uses it in the Leray route of Section 7.7. The cusp-collapse route remains a separate, still-auditable argument; it does not block the second recognition route.

## Evidence

- `source_record/PRODUCT_PROGRESS_RECORD.md` — the supplied progress record, preserved byte-for-byte; its hash is in `PRODUCT_PROGRESS_RECORD.sha256`.
- `evidence/source_extracts/` — canonical TeX extracts for Section 9.1, Sections 7.5–7.7, Appendix B, and Section 10.
- `evidence/exact_checks/` — 17/17 exact integration checks and machine-readable output.
- `evidence/ledgers/S6_REVISED_PROOF_RISK_LEDGER.csv` — route-specific proof-risk ledger.
- `evidence/ledgers/S6_REVISED_THEOREM_AUDIT_LEDGER.csv` — 95-row revised theorem ledger, including Appendix B entries omitted from the first ledger.
- `evidence/annotations/` — 108-page revised annotated manuscript and matching annotation index.
- `evidence/PDF_RENDER_QA.json` and `evidence/PDF_VISUAL_INSPECTION.md` — report-render checks; the revised annotation and two-page-summary render samples are under `pdf_renders/`.
- `session/INTEGRATION_SESSION_VISIBLE_OUTPUTS.md` and `.pdf` — substantive user-visible writing from this integration pass.

## Reproducibility

From the complete extracted bundle root, run:

```bash
bash integration_update/scripts/run_integration_checks.sh
```

The verifier checks the complete integrated package manifest, reruns and byte-compares the 17 exact checks, validates the PDFs and all 108 annotations, verifies the revised ledgers and source record, runs the frozen baseline verifier, and checks the package manifest again for post-run drift.

## Scope boundary

The supplied progress record named live Overleaf workbench files, but those files were not part of the upload. No claim in this update depends on inaccessible workbench state. The record was used to identify arguments for independent checking in the canonical source.

The update does not certify every cited external theorem. Standard nearby-cycle formalism, Gysin naturality, analytic duality, top-degree base change, and the source-by-source literature comparison remain appropriate external peer-review targets.
