# Exact nonlinear and finite interacting Yang-Mills calculations

This evidence accompanies the five standalone root papers added on 8 September 2026:

| Root paper | PDF pages | Result |
| --- | ---: | --- |
| `s6_retained_cusp_nonlinear_draft.tex` | 9 | Original period metric, complete nonlinear pullback, arbitrary finite-link realization, exact six-staple integration, extensive patch integration, and retained anisotropic time-step coefficient. |
| `s6_interacting_wilson_variation_draft.tex` | 12 | Exact interacting-vacuum transform, Wilson-loop Dirichlet and covariance formulas, center selection, repeated-edge contractions, and finite-regulator bounds. |
| `s6_wilson_temporal_transfer_draft.tex` | 10 | Exact temporal character multipliers, scalar shift, gauge projection, operator domains, and strong time-continuum and resolvent limits on a fixed spatial lattice. |
| `s6_spatial_vacuum_elimination_draft.tex` | source only | Actual vacuum marginal, conditional-score coupling, exact form-domain resolvent, memory, and improved excitation estimates. |
| `s6_adjacent_plaquette_quantum_draft.tex` | source only | Explicit absolute two-face excitation quotients and unchanged energy origin, followed by the complete fixed-full-box extension of the nonzero eliminated coupling and Rayleigh improvement. |

The complete mathematical arguments are the root TeX sources. Their matching PDFs are independently compiled reading artifacts. The retained-cusp Markdown in this directory supplies its source calculation, including Section 5.2 and the coefficient `3 g_YM^2 epsilon/(4a)` appearing in the TeX and PDF.

## Exact replay

Run the following from this evidence directory with Python and SymPy installed:

```
python check_retained_cusp_bridge.py
python check_wilson_exact.py
python check_temporal_coefficients.py
python check_spatial_elimination.py
python check_adjacent_plaquette.py
python check_bulk_plaquette_incidence.py
```

The copies included in this project were replayed on 8 September 2026. All exited successfully. The preserved first-batch `EXACT_REPLAY_RECEIPT.json` records 51 retained-cusp check groups, 1,012 Wilson scalar assertions with further exact matrix entries, 237 temporal scalar assertions with further exact matrix entries, 12 spatial-elimination scalar/block assertions with further exact matrix entries, and the then-current 20 adjacent-plaquette groups. The final source-only update's `FINAL_DELTA_REPLAY_RECEIPT.json` records the current 25 adjacent-plaquette groups and complete open-box incidence checks for `L=2,3,4,5`. The current `ADJACENT_PLAQUETTE_CHECKS.json` identifies the updated proof bytes. The scripts check finite algebra, coefficients, orientations, and product identities; the analytic theorems are proved in the papers and are not inferred from finite tests. The actual interacting vacuum, a spatial continuum limit, and a continuum spectral gap were not numerically computed.

## Source and PDF identity

`DRAFT_ARTIFACT_RECEIPT.json` identifies the first-batch TeX/PDF artifacts by their exact SHA-256 hashes and byte counts. `FINAL_DELTA_ARTIFACT_RECEIPT.json` identifies the subsequent source-only update, including the original adjacent source, its composed host, and the complete mechanically converted bulk appendix. The first-batch adjacent source hash is historical; it is not the current composed host hash. The Wilson and temporal PDFs have a complete 22-page visual-check receipt in `SUPPORTING_PDF_QA_RECEIPT.json`, with the readable account in `SUPPORTING_PDF_VISUAL_QA.md`. The nine retained-cusp pages were visually checked in the main mathematical workflow; this installation verifies the same artifact bytes and the presence of its anisotropic section. All three published PDFs remain byte-identical. The final combined source is checked with two pdfLaTeX draft-mode passes, which create no PDF; `FINAL_DELTA_COMPILE_RECEIPT.json` records that source check.

The retained proof and checker audit preceded installation. The cumulative workbench PDF remains its previous dated compilation checkpoint; these additive standalone papers and the current source bundle do not imply that a new cumulative compilation occurred.

The source basenames used in companion cross-references map to root papers as follows: `wilson_finite_lattice.tex` is `s6_interacting_wilson_variation_draft.tex`; `temporal_transfer.tex` is `s6_wilson_temporal_transfer_draft.tex`; `spatial_vacuum_elimination.tex` is `s6_spatial_vacuum_elimination_draft.tex`. The adjacent-plaquette Markdown is included here and its exact hash is recorded by `ADJACENT_PLAQUETTE_CHECKS.json`.

## Complete audited final extension

`adjacent_plaquette_quantum_correction.md/.tex` are the complete current two-face sources before appendix composition. `BULK_PLAQUETTE_EXTENSION.md` contains the entire full-box proof; its generated fragment is `supporting_materials/workbench/research/ym_bulk_plaquette_extension.tex`, included once by the existing adjacent root. Conversion preserves all mathematical content; only generated label identifiers are prefixed to avoid collisions. The exact source and fragment hashes are in `FINAL_DELTA_ARTIFACT_RECEIPT.json`.

The two-face excitation trial quotients are `3 kappa + (5/9)b^2/kappa + O(b^3/kappa^2)` and `3 kappa + (43424/81675)b^2/kappa + O(b^3/kappa^2)`. The unchanged energy origin and the complete moment calculation are in Section 5.1. The difference `(1951/81675)b^2/kappa + O_L(b^3/kappa^2)` and coupling norm squared `b^2/12 + O_L(b^3/kappa)` extend to every fixed open full three-dimensional box with all plaquettes included. The absolute two-face coefficients are not asserted to extend. The full-box projection disk `|b/kappa| < 3/(16M)` shrinks with the face count; no volume-uniform or continuum mass-gap disproof is claimed.

`ADJACENT_PLAQUETTE_INDEPENDENT_AUDIT.md`, `SPATIAL_ELIMINATION_INDEPENDENT_AUDIT.md`, and `BULK_PLAQUETTE_INDEPENDENT_AUDIT.md` provide completed independent proof audits with exact conventions and scope. The bulk audit explicitly covers its final 746-line source, including the opposite-basis dictionary. The adjacent audit preserves its initial review and the later Section 5.1 addendum.

`YM_CURRENT_EXACT_CALCULATIONS_FOR_PRO_20260908.md` is the complete dedicated mathematical packet; `PRO_PACKET_RECEIPT.json` records its 13 original sources. Each embedded source was checked byte-for-byte exactly once against its current original. The packet's relative source locators describe its original organization; standalone copies in this evidence directory use the basenames listed above. `FINAL_DELTA_BUNDLE_VERIFICATION_RECEIPT.json` identifies the final canonical source bundle; the earlier `BUNDLE_VERIFICATION_RECEIPT.json` is preserved as the prior batch checkpoint.

Only mathematical sources, exact checking programs, and sanitized verification records are included here. The update preserves the existing project and main-document selection.
