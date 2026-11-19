# Final report coverage review

**Reviewer:** GPT-6 Astra (OpenAI), effort ChatGPT Pro mode. **Date:** 15 November 2026.

**Verdict: PASS. No outstanding report coverage or consistency defect found.** This review did not modify the report, post, or CSV. The reproducible coverage checks are `code/E_check_report_coverage.py` and its output `code/E_check_report_coverage_output.json`.

## Exact final artifacts reviewed

- Post source SHA-256: `e497aaa7011dedbbbaa16ff5b67699a6ffdec6bfb4d2f1f473544939def5dbf9`.
- PDF SHA-256: `d8782e70ae9286badbf36c6ac98247698f7747fa00f1c9733d4a76b1d1c6265a`.
- The complete report has 22,702 words at this check; its exact hash is recorded in the checker output.

## Coverage of every proof statement and step

Every one of the 44 numbered statements has its own individual audit heading in the report. All six full A/B/E audit texts are present verbatim, checked by direct string inclusion against the work files. The 43 proof environments contain 124 numbered steps, distributed as follows:

| Section | Numbered statements | Numbered proof steps | Full audit record |
|---|---:|---:|---|
| 2 | 10 | 20 | B_foundations.md |
| 3 | 7 | 16 | B_foundations.md |
| 4 | 5 | 9 | B_foundations.md |
| 5 | 5 | 13 | B_foundations.md through 5.4; B_hard.md for 5.5 |
| 6 | 5 | 16 | B_hard.md |
| 7 | 3 | 18 | B_hard.md |
| 8 | 5 | 12 | B_hard.md |
| 9 | 4 | 20 | A_accounting.md |
| **Total** | **44** | **124** | |

The short unnumbered proofs of 2.5, 3.5, and 4.1 also have complete independent arguments; Definition 2.9 has its definition audit. Their zero numbered-step counts are intentional and contribute no missing statement.

The layout's step numbers sometimes group the audit paragraphs differently. I checked their logical coverage, especially the required hard points. Lemma 6.2's four published steps are covered by the audit's five paragraphs, separately checking injection counts and initial-pair replacement. Lemma 7.1's eleven published steps are covered by its eight audit paragraphs: reduction and time cases, boundary carry witness, earliest-exception global predecessors, old-key inequality and parent I3, forced successor, first-target propagation, and later-target propagation. Lemma 8.4's two published steps are covered by all three audit paragraphs, including the permitted atomic alphabet. Proposition 9.2's nine published steps have the full formula/state count, tape-length analysis, six detailed subroutine subsections, and dominance/coefficient derivation in Part A. Corollary 9.3's encoding, elementary branches, parameter substitution, and deadline factor are covered in Part A §5 and its explicit statement audit. No published proof step was lost by the assembly.

The 47 CSV rows cover those 44 statements plus Theorems A and B and Cited result 1. The main theorems are established by the fully audited 9.1–9.3 and 8.5, respectively. Their row scope is consistent with the final post, including the explicit m≥3 wording and the corrected cited-source deadline range 1≤T≤n.

## Task and format coverage

All twelve requested task rows are present: A.1–A.3, B.1–B.3, C.1–C.2, D.1, E.1–E.3. The exact cost exponents and effective coefficients agree with the final post. The mathematical source proofs remain self-contained; the external S-check scopes are stated separately.

All ten format-checklist rows are present. Rows 1–9 record completed work and its evidence; row 10 correctly reserves user approval after delivery. The report's complete state is consistent with the permitted unavailable-source treatment: the original FKN full text and the course archive endpoint remain disclosed access limits, with no unresolved mathematical item inferred from them. Historical prompt-byte and model-run provenance qualifications remain explicit. There is no `INCOMPLETE`, `TODO`, `TBD`, or visual-pending marker.

The report includes the complete final visual-inspection record verbatim, the exact final PDF hash, and the before/after build table: baseline 32 pages and zero overflows; initial revision 38 pages and six overflows, four exceeding 2pt; final 38 pages and zero overflows. It records the actual rendering and inspection, including the repaired orphaned Uses line and heading.

## Measured evidence, literature, and exclusions

The finite-check counts and their limitations agree with the recorded outputs. In particular, the report retains the observed maximum injection count of one and zero surviving-first initial-pair replacements, while assigning their arbitrary-history conclusions to the written proofs. The source-access limitations, absence of a fresh Lean build, and the scope-only checks of Jansen/Giraudin are stated consistently. The dated literature summary reports its 50 exact queries and closing repeat without an exhaustive-index claim.

The exclusion table identifies supplied inputs, retrieved source reproductions, generated typesetting runtime state, and duplicate/obsolete render artifacts, with retained replacement evidence. It explicitly preserves every mathematical audit, mandatory ancillary file, and numbered statement, and explains the status of historical recommendations embedded verbatim. Final packaging can apply that stated ledger without losing an undecided result or silently removing a proof statement.

No additional correction is requested by this final coverage review.
