# What each part contains: the local S6 workspace and the public repository

Assembled 12 November 2026 by Claude Fable 5.2 (effort high) from the reading notes of thirteen readers, so that a
later checker can find things. The ranked findings are in `FINDINGS.md`; the readers' full notes, with the six-point
entry of every candidate, are in `work\<reader>_notes.md`; their check scripts are in `work\scratch\<reader>\`.

## Map

**Local Codex workspace** `C:\Users\user\Documents\math\research\s6_recent_results_main\` (2.1 GB; primary and most
up to date on S6):

| Part | What it is | Reader |
|---|---|---|
| `canonical_S6_snapshot\original_clean_transcription.tex`, `main.tex`, `supporting_materials\manuscript_sources\source_pdfs\original_ai_manuscript.pdf` | The original 108-page manuscript [AC26]: PDF, AI transcription, annotated edition | A0 |
| `canonical_S6_snapshot\supporting_materials\peer_reviews\`, `audit_annotation_sources\`, `workbench\research\status.tex`, `local_repairs.tex`, `ledgers\` | The first check of the original (24 August to early September 2026): reviews A, B, C, corrective rounds, claim ledger (125 entries: 115 VERIFIED, 6 REFUTED, 4 OPEN) | A0 |
| `…\workbench\research\candidate_geometry.tex`, `exact_algebra.tex`, `integral_leray.tex`, `topology_reduction.tex`, `finite_filling_certificates.tex`, `algebraic_dimension.tex`, `cusp_toric_cover_completion.tex`, `cusp_globalization_replacement.tex` | Construction and topology re-proved; exact admissible range; finite fillings; Kummer cover; the circle quotient | A1 |
| `…\cdp_program.tex`, `analytic_picard*.tex`, `hodge_frolicher.tex`, `bott_chern_algebra.tex`, `analytic_canonical_ring.tex`, `period_parameter_deformation.tex`, `period_shift_classification.tex` | CDP, Picard group, Hodge and Bott-Chern, anticanonical ring, the family and its classification | B |
| `…\cusp_cone_sphere_routes.tex`, `cusp_sphere_route_strengthening.tex`, `cusp_sphere_fixed_metric.tex`, `cusp_s12_carrier_homotopy.tex`; root `s6_cone_sphere_routes_preprint.tex` | Maps from X and its smash powers to spheres; homotopy classes | C1 |
| `…\cusp_spectral_*.tex`, `cusp_gauge_operators.tex`, `cusp_su2_magnetic.tex`, `cusp_native_full_flux_*.tex`, `cusp_compact_link_gaussian.tex`, `quaternionic_4441_reconciliation.tex`, `scalar_gauss_*.tex`, `two_cross_exceptional_shared.tex`, `worldline_presymplectic_reduction.tex`, `hermitian_normal_slice_physics.tex`, `homogeneous_quantum_confinement.tex`, `ym_bulk_plaquette_extension.tex`, `z6_defect_center_bridge.tex`; root `s6_*_draft.tex` | Physics-flavoured lanes; the Yang-Mills drafts that later moved to the repository | F |
| `…\es_niemeier_*.tex`, `common_d4_image.tex`, `niemeier_umbral_shadow.tex`, `p1201_selector_jordan_bridge.tex`, `erdos_straus_*.tex` | Lattice lane | D1 |
| `…\koide_*.tex`; root `koide_arithmetic_preprint.tex` | Counting lane | D2 |
| `…\higher_rung_*.tex`; root `s6_higher_rung_24d_preprint.tex` | Higher-dimensional attempts; the retained-angle theorem | E, C1 |
| `…\mathematical_summary.tex` | The workbench's own result map (145 KB) | A1, B, C1 (parts) |
| `…\workbench\evidence\` (23 folders) | Audit reports and checkers of 4-8 September | by topic |
| `courses\CG-S6\` (src\*.md, checks\, sources\) | The course, written to 11 October 2026: eleven lessons and about fifty companions; the latest treatment | G1a, G1b, G2 |
| `mathematical_consolidation\` | Consolidation of 29-30 September (R1-R8, catalogue); `nested_source_blobs\` | I, H |
| `related_sources\` (five roots) | Geometric Unity bridge, Nolan Gaussian fibres, two RH sources, earlier mass-gap comparison | I |
| `source_text_blobs\aca0913d….tex` | The correction note [N] of 1 September 2026 on the CDP step | I, G1b |
| `ledgers\`, `custody\`, `source_dialogues\`, `source_text_blobs\` | Custody and routing; not read beyond what readers I and A0 record | I |

**Public repository** (clone in `repo\`; read lightly): `s6\` (status note of 5 October, five-page key-advances reader,
consolidation of 30 September), `yang-mills\` (the lattice Yang-Mills programme; its continuation
`20260930-s6-ns-moment-map-bridge` uses the threefold through one homotopy class and one number), `navier-stokes\`,
`docs\`, `tools\`, `releases\`. Reader H.

**Literature fetched** (`C:\Users\user\Documents\s6_pro_prompts_20261112_work\literature\`; Engel's first version also in
`literature\engel\`): Engel arXiv:2609.38442; CDP20 arXiv:1904.11179v2; CDP98 arXiv:math/9607215; Lehn-Rollenske-Schinko
arXiv:1912.09719; Viaclovsky arXiv:2609.33785, 2610.10451, 2610.39102; Liu-Rollenske arXiv:2609.33826; Yang
arXiv:2609.29666; Wang arXiv:2609.11541; Mandal arXiv:2609.27929; McHugh arXiv:1708.03251; Angella arXiv:1705.10518;
Duke-Imamoglu (zeros of ℘); Lekkas-Petridis arXiv:2509.12902; Voskou arXiv:2407.03134; Chenevier-Lannes arXiv:1409.7616.

**Not read by anyone in this survey:** the sqlite catalogues and the large `.jsonl.gz` dumps beyond streamed samples;
`source_dialogues\`; most of `source_text_blobs\`; the proofs of the general-analytic and handle-theory companions
of the course (statements only); the repository's Yang-Mills and Navier-Stokes mathematics; the paper [R] cited by
the status note (in neither place). Each reader's own "Not read" list is in section 4 of its notes.

## Reading notes by reader
