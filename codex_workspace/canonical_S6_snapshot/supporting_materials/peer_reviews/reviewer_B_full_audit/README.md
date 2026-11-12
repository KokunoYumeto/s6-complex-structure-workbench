# Reviewer B final evidence — curated Overleaf subset

This directory is a deliberately compact public subset of the unchanged 72.7 MB final evidence ZIP. It is **not** the complete original bundle, and the full-bundle `run_all_checks.sh` workflow does not apply here because the canonical release, comparison images, and other bulky duplicate inputs were intentionally omitted from the Overleaf compile tree.

The complete original ZIP has SHA-256 `d2fb49e35e5885b531ffd296f4309deb1632e3e4a966c106702fef627badab98`. Its 169 internal checksum rows were independently verified. The primary report here is byte-identical to the previously recovered Markdown, so the final evidence bundle does not alter the integrated mathematical verdict. See `RECONCILIATION.md` for that comparison.

## Disposition

**MAJOR REVISION — MAIN THEOREM NOT CERTIFIED.**

The separate source-fidelity audit passes all 108 pages. The mathematical audit reaches a different conclusion: 38 finite exact-algebra checks pass, while the claimed identification of the constructed threefold with the standard smooth six-sphere still depends on geometric maps not independently certified at chain level. The principal unresolved items R1–R4 are the cusp-collapse model, integral specialization, based van Kampen maps/signs, and the geometric identification of the printed Mayer–Vietoris/Leray matrices. R5 is a conditional recognition step rather than an additional geometric defect.

## Start here

1. Read `reports/S6_MATHEMATICAL_PROOF_AUDIT.pdf` or the matching Markdown.
2. Read `reports/S6_MATHEMATICAL_PROOF_AUDIT_SUMMARY.json` for the machine-readable synopsis.
3. Open `evidence/annotations/S6_AUDIT_ANNOTATED_MANUSCRIPT.pdf` for Reviewer B's page-level notes.
4. Open `evidence/critical_pages/S6_CRITICAL_EVIDENCE_PAGES.pdf` for its 37 selected load-bearing pages.
5. Inspect the theorem and risk ledgers under `evidence/ledgers/`.
6. Run `python scripts/reproduce_core_checks.py` to reproduce the genuinely standalone 38-check exact-algebra harness. The archived `core_checks.json` and `core_checks.txt` are the reference outputs.

## What is included

- the primary report in Markdown and PDF plus its JSON summary;
- Reviewer B's 108-page popup-annotated PDF and annotation index;
- the 37-page critical-evidence PDF and its index;
- the 92-row theorem ledger and R1–R5 risk ledger;
- exact-check script and archived JSON/TXT results;
- the source/text extracts needed to inspect the critical ranges;
- build-environment and verification receipts; and
- selected generating scripts retained as provenance artifacts.

`scripts/build_annotated_manuscript.py`, `scripts/build_critical_evidence.py`, and `scripts/generate_theorem_ledger.py` are preserved for provenance but require inputs available only in the complete archive. They are not represented as runnable against this subset. `MANIFEST.txt` inventories this curated directory, not the full original bundle.

## Deliberate omissions

The full canonical release, authority duplicates, contact sheets, detailed image pairs, duplicate manuscript sources/PDFs, session-export prose containing dead temporary download links, and the full-bundle shell verifier were omitted to keep the Overleaf import below service limits. The complete unchanged ZIP is intended as a separate archival/Zenodo attachment rather than a nested Overleaf file.

This is a literal model-peer proof audit, not a journal's anonymous peer-review record. A source-fidelity PASS means that the transcription reproduces the supplied source; it does not certify the mathematical theorem.
