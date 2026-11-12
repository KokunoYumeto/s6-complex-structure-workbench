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

---

### Reader A0: The first check of the original manuscript (audits, peer reviews, status, ledgers)

Full notes: `work\A0_notes.md`.


#### 1.1 Audit annotation sources (`supporting_materials\audit_annotation_sources\`)

- `audit_annotations_appendix.tex` (42 KB, "Prepared 24 August 2026"). The printed appendix of the annotated
  edition: status legend (E exact / N reviewed / C conditional / U critical unresolved / X repairable error /
  P provenance), page-by-page integrated annotations for the 108 pages with the three reviewer streams
  separated, then Reviewer A's 17-row ledger (A-F-01, A-E-01/02, A-R-01..09, A-V-01..05), Reviewer B's ledger
  (B-EX-00..06, B-RV-01..04, B-CR-01..04, B-CO-01/02, B-VERDICT), the Codex ledger (C-REV-001..004, C-CDP-005,
  C-ERR-006..008, C-TEX-009/010, C-QA-011, C-PRES-012), a reconciliation and a "minimum revision package".
  Verdict at that date: "major revision; the central theorem is not presently certifiable", "not disproved".
  This is the state on 24 Aug, before any WB proof. It is frozen as a historical record.
- `audit_annotation_layer.tex` (3.9 KB): only the badge overlay (one status per page: 1-7 C, 8-12 E, 13-23 N,
  24-29 U, 30 X, 31-35 N, 36-37 C, 38-62 U, 63 X, 64-70 C, 71 X, 72-73 C, 74-77 U, 78-83 C, 84-95 U, 96-97 E,
  98 X, 99 E, 100 X, 101-105 U, 106-108 P). No mathematics.
- `reader_guide.tex` (6.8 KB): one-page synopsis of the two Pro audits of 24 Aug (A: CDP obstruction and
  section 10; B: exact algebra versus geometric topology; four obligations).
- `corrective_results_addendum.tex` (39 KB): the current front matter of `main.tex` (it is `\input` at
  main.tex line 167; the reader guide follows at lines 173-298; the transcription starts at line 299). Six
  pages: p.1 Reviewer B's revised disposition (25 Aug) and its 26 Aug analytic follow-up; p.2 Reviewer A's
  corrective audit (25 Aug); p.3 "Subsequent Codex validate/repair/disprove results", each "VERIFIED ... as of
  30 August 2026" (construction, specialization and Leray d_2, van Kampen, algebraic reduction, Prop. 10.8,
  Hodge numbers, Bott-Chern, the three all-Pic routes); p.4 "Exact sign, Hodge and Bott-Chern certificates";
  p.5 "Typed affine-defect and toric restriction certificates" (the finite norm identity (5.17-A15), the toric
  inclusions, the matrix B); p.6 "3 September 2026: native cusp, sphere carriers, spectral scope" (later
  extension work, outside the first check). `ANNOTATION_INDEX.csv` (3.3 KB) not opened (index only).

#### 1.2 Peer reviews (`supporting_materials\peer_reviews\`)

All "reviewers" are AI sessions: A and B are two separate ChatGPT Pro-mode sessions (GPT in Pro mode;
`tool_disclosure.tex`), C is Codex. `README.md` (3.5 KB) maps the streams; `REVIEW_SOURCES.json` gives hashes.

- `superseded_packet_06\` (README 3 KB; report 45 KB, skimmed; receipt dated 2026-08-24T14:13 UTC). A review
  of pages 56-66 only (the other packets were missing). Recommendation "reject" on the ground that CDP20
  Thm 2.2 / Cor 2.3 contradict the claims; 22 exact checks pass; finds the Remark 7.28 quantifier defect;
  audits Lemma 7.16 (sign propagation) and calls it "conditionally sound"; minor notes (Z/p with p < 0;
  "c_3(X)=2" should be a Chern number; Hurewicz induction wording in Lemma 8.2; sign conventions in
  Lemma 7.25 / Prop. 7.27). Superseded the same day by the full-source reviews.
- `reviewer_A_full_audit\report\full_mathematical_peer_review.md` (50 KB, 24 Aug) and
  `audit\issue_ledger.json` (17 rows). Section-by-section review of the whole manuscript. "Major revision and
  resubmission after independent specialist replication"; "did not identify a fatal mathematical contradiction".
  28 exact checks. Two "confirmed errors": E-01 Remark 7.28, E-02 Prop. 4.7(iv). Withdraws the packet rejection:
  section 10's conductor section and the coinvariant correction are "coherent on close inspection".
- `reviewer_A_corrective_2026-08-25\`: `report\corrective_addendum_and_results_map.md` (12 KB),
  `report\revised_full_mathematical_peer_review.md` (72 KB; the first report plus the addendum, a "conditional
  recognition theorem and obligation split", an expanded Appendix B section and "four distinct propositions"
  for section 10), `notes\minimal_recognition_obligations.md` (obligations G, V1, B1, F1, L1 for the Leray
  route; C1-C3, MV1 for the collapse route), `notes\literature_comparison_CDP98_CDP20.md`,
  `notes\codex_findings_crosswalk.json` (C-01..C-12: what A adopted from a Codex progress log). New in this
  round: the direct proof of a(X)=1 is "complete conditional only on the period family"; the Leray route is
  logically sufficient without Prop. 7.2; Lemma A.3 variance error confirmed (third local defect). Stays at
  "major revision".
- `reviewer_B_full_audit\reports\S6_MATHEMATICAL_PROOF_AUDIT.md` (13.6 KB, 24 Aug). "MAJOR REVISION - MAIN
  THEOREM NOT CERTIFIED". No arithmetic or local analytic error found; four unresolved obligations: R1 cusp
  collapse, R2 integral specialization, R3 van Kampen inclusions, R4 identification of the MV/Leray matrices.
  38 exact checks; 92-row theorem ledger (not in this subset).
- `reviewer_B_corrective_2026-08-25\report\S6_CORRECTIVE_PEER_REVIEW_ADDENDUM.md` (15 KB) and
  `S6_MATHEMATICAL_RESULTS_SO_FAR.md` (10 KB). "RECONSIDERED - PROVISIONALLY FAVORABLE WITH FOCUSED
  VERIFICATION REQUESTS." The correction is the distinction between sp^q (nearby cycles, Appendix B) and c^*
  (collapse, section 7.2): section 7.7 uses only sp^q, so R2 and R4 do not block the Leray route; R3 retired
  after re-reading section 7.5. Revised risk ledger C1, C2, B1, V1, L1, MV1, G1, A1, D1.
  `S6_MATHEMATICAL_PROOF_AUDIT_REVISED.md` (39 KB) not read in full (same content at length).
- `reviewer_B_candidate_validation_2026-08-26\reports\S6_CANDIDATE_SPECIFIC_VALIDATION_UPDATE.md` (15 KB,
  26 Aug). Proves, from named inputs CAND-X (compact smooth X, nonconstant f), CAND-W (reduced Cartier nc fibre
  with normalization dP6), TOP-H2 (H^2(X;Z)=0): flatness; R^q f_*E = 0 for q>2 and the degree-two base-change
  isomorphism at every scheme-theoretic fibre by the finite-complex universal-coefficient sequence; Cartier
  duality; the conductor section; hence R^2 f_*(T_X (x) L) != 0 for all L. 8 exact checks.
- `reviewer_C_codex\report\integrated_peer_review_report.tex` (23 KB, 24 Aug), `mathematical_audit.md`,
  `tex_audit.md`. "Not presently independently certifiable"; three confirmed manuscript errors (Remark 7.28,
  Remark A.6, Lemma A.3); p.71 TeX portability defect (build only); the CDP gap is "credible".

#### 1.3 Workbench status files (`supporting_materials\workbench\research\`)

- `status.tex` (129 KB, 3,304 lines; dated "As of 6 September 2026"). Lines 1-423 are a preamble of later
  work (6 Sep spectral/umbral maps, Niemeier/Leech, canonical ring, deformation over Im c < -M, quaternionic
  model, quantum mechanics): not the first check. The S6 status list is the enumerate at lines 424-1354:
  (1) construction with the simultaneous orientation normalization and deck certificate
  phi(g_1)=S_1, phi(g_2)=S, phi(g_0)=P; (2) integral algebra; (3) sp^q and Leray d_2: d_2(12 gamma)=omega,
  d_2(2q)=omega[delta], d_2(2 gamma uw)=omega[gamma delta]; (4) collapse C1-C3 with c^* = sp^q; (5) pi_1 and
  S^6; (6) NS(F_b)=Z eta, a(X)=1; (7) REFUTED: CDP20 p.692 inference; (8) conductor/duality/base change, Pic^0
  route; (9) r = nu^* i^* and the three all-Pic certificates; (10) the local cusp Picard map is nonzero
  (D_Q); (11) third all-Pic certificate in full; (12) REFUTED: CDP98 split-extension formula; (13) corrected
  replacement theorem; (14) counterexample to CDP20 Thm 2.2; (15) Prop. 10.8; (16) alternate MV route;
  (17) Hodge diamond, E_2 = E_infty; (18) REFUTED: Remark 1.3 torsion claim; (19) Bott-Chern/Aeppli numbers;
  (20) Bott-Chern algebra. Lines 1355-3290: cusp spectral geometry, Kummer covers, S^12/S^24 carriers,
  gauge operators and so on (3 Sep and later). Lines 3272-3304: external validation note, Reviewer B
  checkpoint, status language.
- `local_repairs.tex` (2.6 KB): seven "confirmed local repairs": 1 Prop. 4.7(iv); 2 Remark 7.28 (REFUTED);
  3 Lemma A.3; 4 Remark A.6; 5 p.71 build defect; 6 Omega^1_{X/B} torsion claim (REFUTED); 7 the finite-filling
  Hodge-line frame wording.
- `validation_protocol.tex` (2.8 KB): the four statuses (VERIFIED / CONDITIONAL / OPEN / REFUTED), "repair is
  an operation, not a fifth status", exact computations as certificates, literature policy.
- `tool_disclosure.tex` (1.9 KB): the source was reconstructed from the PDF in ten strips (8 x 11 pages,
  2 x 10) in ChatGPT Pro sessions; two Pro sessions made the first audits; the workbench was made "with Codex
  using ChatGPT 5.6 Sol in Ultra mode". The candidate and its theorem claims "remain attributed to the
  reported Claude/Fabel source".
- `literature_log.tex` (43 KB, 783 lines; lines 1-658 on the S6 literature, read at the start and skimmed; from
  line 659 later topics). Records which source carries which step: CDP20 Thm 2.2, Cor 2.3, section 7 p.692;
  CDP98 Lemma 3.2; Ramis-Ruget; Banica-Stanasila III.3 Thm 3.4, Cor 3.10 and III.4 Thm 4.12; Dimca 4.2.1,
  4.2.2, 4.2.11, 2.3.26; Kashiwara-Schapira 8.6; SGA 7 (algebraic scope only); Stacks tags; Smale 1961/1962,
  Kervaire-Milnor; McHugh 2019; Angella; Schweitzer; Cartan, Deligne, Katz-Oda.
- `ledgers\claim_ledger.txt` (128 KB, 152 lines; index in the work folder). REFUTED: S6-CDP-P692,
  S6-CDP98-MONO, S6-LOCAL-728, S6-HODGE-CUSP-TORSION, and two later ones outside the first check
  (S6-CUSP-DECOMPACTIFICATION-QUOTIENT, S6-CUSP-LITERAL-COMPACT-EXTENSION). OPEN: S6-OPEN-HODGE-REPLICATION,
  S6-OPEN-EXTERNAL-ADJUDICATION, and later ones (KOIDE-SQRT-DISCREPANCY, YM-PHYSICAL-BRIDGE). Three ids keep
  "OPEN" in their name but have status VERIFIED (S6-OPEN-R-ANALYTIC, S6-OPEN-HODGE-REPRESENTATIVES,
  S6-OPEN-CDP-REPAIR).
- `ledgers\uncertainties.txt` (37 KB, 45 JSON lines). First-check entries: U-CUSP-ACTION, U-SPECIALIZATION-INDEX,
  U-COLLAPSE-COMPARISON, U-MERIDIAN-SIGN, U-CDP-HYPOTHESES, U-PROP-10.8, U-CDP-R-DIRECT, U-CDP-R-ANALYTIC,
  U-HODGE-H12, U-HODGE-BCA, U-HODGE-REPRESENTATIVES, U-CDP-REPAIR (all VERIFIED); U-CDP-P692-INFERENCE,
  U-CDP98-COINVARIANTS, U-HODGE-CUSP-TORSION (REFUTED); still OPEN: U-HODGE-REPLICATION,
  U-EXTERNAL-ADJUDICATION, U-FABLE-PROVENANCE (provenance of the Jacobian-conjecture map, not mathematics).
- `ledgers\next_lemmas.tex` (55 KB, 1,511 lines). "Resolved bridge records": G0 (signs), K1, C4-C10, S1-S2,
  G1-G2 (all later work, lines 18-910); the first-check records are at lines 912-1445: C1, C2, C3, V1, MV1, L1,
  P10.8, R1, R2, R3, D1, H1, H2 (OPEN: human replication), H3.
- `ledgers\research_log.tex` (138 KB, 2,768 lines): the dated record. Rounds 0-5 undated (24-25 Aug),
  Round 6 = 25 Aug, Rounds 7-11 = 26 Aug, 12-17 = 27 Aug, 18-21 = 28 Aug, 22-23 = 29 Aug, 24-26 = 30 Aug,
  27 = 1 Sep, 28-36 = 3 Sep, 37-38 and following = 4-5 Sep. I read Rounds 0-27 in full and the 5 Sep entry
  "direct-image and logarithmic real-marking corrections" (lines 2670-2690); the rest only by headings.
- `comparative_context\prior_fable_context.tex` (5 KB) and its README: a replay of the degree-seven map F on
  C^3 with det DF = -2 and three points with one image (the Jacobian-conjecture counterexample attributed to
  Fable); used only as a model of "small certificate" method. No S6 mathematics.

#### 1.4 Pro-mode feedback files (`supporting_materials\workbench\`)

- `WEB_PRO_MODE_FEEDBACK.md` (98 KB, 2,827 lines; "Last updated 2026-09-06"). This is the note *from* the
  workbench *to* the ChatGPT Pro web session, 3-4 Sep. It is not a review of [AC26]: it audits Pro-mode's
  extension packets (rank-three toroidal successor, S^12/SU(3)/(3,1)-cone, Koide arithmetic, Jordan-toric
  Euler packet, native full-flux magnetic packet). I read lines 1-750 in full and the rest by section
  (corrections, notation, "corrections to avoid"). Objections and dispositions that it records:
  (a) Pro's finite-cover R^4 construction is valid but for an altered cusp family (WB: "ancillary");
  (b) Pro dismissed an S^12 interpretation because X x X is not S^12: WB answers that the right source is the
  smash X ^ X (the map q_2 is constant on the fat wedge);
  (c) the naive Kummer power map does not descend; the source action needs C_N(v) = C(v^N)/N (WB repair K1);
  (d) both sphere-valued carriers are null-homotopic (pi_12(S^8) = 0; st([g ^ g]) = 4a^2 nu^2 = 0);
  (e) a literal three-special-fibre pattern with the rank-three cusp has Euler characteristic 6, so cannot be
  S^8 (and a homotopy S^8 has no almost complex structure);
  (f) the Gram-cone "S^6" is a different object from the complex S^6; no identification follows from the
  number 6 or an SU(3) action; (g) the coefficient 1/2 in Pro's Q_4 is a choice (kappa = 2), not forced;
  (h) three operator theorems of the magnetic packet "not yet proved at the precision asserted";
  (i) classical or auxiliary spectral statements give no Yang-Mills mass-gap statement (OPEN).
  It also contains one S6 computation that belongs to the first-check material: the "cyclic-six defect
  quotient" kappa_F = (12,0,4,0,-3,0) on H^4(U;Z) of the regular locus, with Phi_1(l_0 c - g_1 - g_2) = p
  (lines 383-487).
- `WEB_PRO_MODE_PRE_FEEDBACK_RESPONSE_2026-09-03.md` (19 KB): the verbatim Pro-mode answer ("three exact
  constructions": universal cover, finite covers, doubling) that the note above responds to. Read the head only.
- `WEB_PRO_TRIALITY_LEECH_FEEDBACK_20260906.md` (7.9 KB): handoff on the Niemeier-Leech-triality work. No S6
  first-check content.

#### 1.5 Root files and history

- `workbench.tex` (76 KB, dated 6 Sep 2026; title "The Claimed Complex Structure on S^6: Validate, Repair, or
  Disprove"). Its abstract runs from line 67 to line 1595; the S6 part is lines 274-480 (same content as
  status.tex items 1-20). Inputs at lines 1599-1644. Line 274: "consolidated successor to the former 56-page
  workbench ... the subsequent 18-page repair branch and the later Reviewer B/Codex validation work".
- `main.tex` (621 KB): front matter = the corrective addendum and the reader guide (above), then the
  transcription with badges, then the annotation appendix (from line 5932).
- `supporting_materials\workbench_history\`: `README.md`, `PROJECT_MERGE_MAP.md` (26 Aug consolidation: the
  123-page public edition, the 108-page clean source, the then 60-page workbench; the 56-page former
  workbench; the 18-page conservative branch whose Pic^0 argument was integrated; the first repair notebook of
  25 Aug; the 121-page public checkpoint of 24 Aug). READMEs of the four checkpoints read; old copies not
  opened. `workflow_record_2026-08-24\LOGBOOK.md` skimmed for dates (24 Aug assembly and Overleaf import,
  25 Aug 121-page edition frozen).
- `supporting_materials\workbench\evidence\s6_cdp_direct_image_reaudit_20260905\` (README and AUDIT.md lines
  1-140) and `...\s6_global_smooth_reaudit_20260905\` (README, head of CUSP_AUDIT.md). Not in my list, opened
  because the research log points to them: two bounded re-audits of first-check proofs on 5 Sep (see 1.6).
- Proof files opened only to confirm dispositions: `candidate_geometry.tex` (lines 30-115, 325-345),
  `topology_reduction.tex` (1-106, 277-300, 915-930, 1124-1240), `cdp_program.tex` (40-123, 205-300, 553-660,
  1196-1300, 1304-1325, 1368-1600 in part), `algebraic_dimension.tex` (285-300), `analytic_picard.tex`
  (690-702), `integral_leray.tex` (950-965).
- Engel's paper (`literature\engel_S6.txt`): introduction and section 8 read; the rest by search.

#### 1.6 What the 5 September re-audits say (they bear on how far to trust "VERIFIED")

- CDP direct-image re-audit: confirms the chain conductor section => H^2(W,(T_X (x) L)|_W) != 0 =>
  (R^2 f_*(T_X (x) L))_{p_0} != 0 and the nodal-cubic test; finds **two errors in the WB's own written proofs**,
  both corrected: (1) `thm:cartier-duality` had "constructed" the duality isomorphism by matching the outer
  terms of two five-term sequences; (2) the logarithmic gluing translation was written as a complex scalar
  alpha = log s/(2 pi i) times v_j in a real marking; the right vector is
  a_j(s) = Re(alpha) v_j + Im(alpha) J_s v_j, J_s = Pi(s)^{-1} i Pi(s). Signs and coefficients of the results
  unchanged. It also notes a "fixed-twist issue" in CDP20's explanatory prose (the fibrewise dual H^0 is
  displayed without the canonical factor omega_X) and that the WB's all-twist nonvanishing includes the
  trivial twist.
- Global-construction re-audit (period, cusp, finite fillings): "No false assertion was found among the cusp
  theorem's geometric conclusions"; three abbreviations in the WB text to restore; "The earlier source [the
  original, packet 03] already includes all three details." New there: the exact admissible constants
  (Im c_0 < -M) and the opposite-edge multipliers.

---

---

### Reader A1: Core construction and topology (workbench)

Full notes: `work\A1_notes.md`.


#### 1.1 candidate_geometry.tex (61 KB, 1581 lines; written 24–26 Aug, refined 5 Sep 2026)
Section "The analytic threefold constructed in the candidate" (label sec:candidate-geometry). Order: period family, cusp filling,
finite fillings, gluing. Every main statement carries \Verified.
- lem:triangle-generator-orientations (l.32–111): g_1'(z_1)=e^{-2 pi i/3}, g_2'(z_2)=-i can be chosen simultaneously with g_0=(g_1g_2)^{-1} parabolic;
  free-product word argument that the two mixed orientation choices are not parabolic. [AC26] Prop. 2.11(ii) (l.587–595) states the same; the
  word argument is an added detail.
- prop:period-input-audit (l.113–561): existence of tau, mu, beta with the affine laws (2.1), D<0, Pi(gz)=R_g(z)Pi(z)M_g. Proof: lift of
  J_B=1728 t through j; deck homomorphism phi: Delta -> PSL_2(Z); parabolicity of phi(g_0) by a winding argument; phi(g_0)(w)=w-1 forced by
  tr(S_1^{-1}P^{-1}) = 1 + k(p^2-pr+r^2) = 0; line sheaf L of automorphy factor j~ identified with O_B(-p_0) by Theta = E_4^2 h/Delta_mod,
  h^2 = E_6∘tau; H^0=H^1=0 gives the unique mu, with mu(z_1)=(2-rho)/3, mu(z_2)=(1-i)/2; beta is a section of an O_B-torsor (sum identities
  (2.1c), local solutions (2.1d)), unique up to a constant; (2.3a)–(2.3d) equivariance; D -> -infinity at the cusp.
  This is [AC26] Thm 3.4 with §§3.1–3.5 (l.750–1090), same torsor structure ("mu: a torsor under a line bundle of degree -1", l.876; E_6^{1/2} at l.909).
- prop:period-exact-admissible-constants (l.563–596) and the remark "the cusp extension is essential" (l.598–617): see candidates A1-2, A1-3.
  Ledger ids S6-PERIOD-EXACT-ADMISSIBLE-CONSTANTS, S6-PERIOD-CUSP-FREE-SHIFT-COUNTEREXAMPLE (both VERIFIED), morphism M-S6-PERIOD-ADMISSIBLE-AFFINE-LINE.
- (2.5a),(2.5b) (l.620–650): Z = s B_0 + C(t_c), B_0=[[0,1],[-1,0]], C=[[6mu,h],[b-h,mu]], b=beta+tau, h=(2 pi i)^{-1} log u_1.
- lem:toric-chart-control (l.709–761), thm:candidate-cusp-geometry (l.763–1065): the infinite A_2 fan, Psi_lambda(x,t)=(c_lambda(t) t^{B_0 lambda} x, t)
  acts freely and properly discontinuously on Y_eps; N_0 = Y_eps/Lambda-bar smooth, f_0 proper; W reduced, irreducible, nonnormal, nc not snc,
  normalization dP_6; omega_{N_0} trivial via Omega = dx_1 dx_2 dt/(x_1x_2). The proof spells out Hausdorffness of the countable-fan toric variety
  (semigroup separation), the closed-unit-polydisc cover of E_0 by six bidiscs, properness with an explicit compact K_0. = [AC26] Lemmas 4.2–4.4,
  Thm 4.5, Prop. 4.6 (l.1227–1467). New relative to [AC26]: the explicit opposite-edge maps (l.1029–1064, eq:cusp-exact-opposite-edge), candidate A1-4;
  ledger S6-CUSP-EXACT-EDGE-IDENTIFICATIONS, morphism M-S6-CUSP-OPPOSITE-EDGE.
- prop:candidate-cusp-overlap (l.1067–1226): exponentiation E(z,zeta)=(e^{2 pi i zeta_1},e^{2 pi i zeta_2},e^{2 pi i s(z)}) identifies J|_{D_0^*} with N_0\W;
  written with the group G_0 = Lambda ⋊_{M_0} <g_0~>, normal subgroup H = Lambda_tor x <g_0~>, quotient Lambda-bar. = [AC26] Prop. 4.7 (l.1481–1510).
- lem:middle-period-proper (l.1271–1311); prop:candidate-finite-fillings (l.1339–1469): free Z/m_j action (z,x) -> (g_j z, A_j x + v_j/m_j),
  f_j^*(p_j)=m_jS_j, conjugation by the logarithmic section (2.9d),(2.9e). = [AC26] Thm 5.4, Lemma 5.5, Prop. 5.6 (l.1594–1672).
- lem:finite-filling-stalk-map (l.1471–1516): radial retraction N_j -> S_j, specialization = pi_j^*. = [AC26] Lemma 7.3(i).
- thm:candidate-global-geometry (l.1518–1570): gluing; Hausdorff, second countable, proper, compact, connected; omega_X|_{N_0} trivial. = [AC26] Thm 6.2.
- Only the tautological cusp gluing (l_0=0) and the twists v_1=eps, v_2=-eps' are constructed here. The l_0-regluing of [AC26] Prop. 6.7 and the
  general admissible v of [AC26] Thm 5.4 / Rem. 5.8 are not re-derived in this file.
Evidence: `..\evidence\s6_global_smooth_reaudit_20260905\` (PERIOD_AUDIT.md, CUSP_AUDIT.md, FINITE_FILLINGS_AUDIT.md, FINITE_INDEPENDENT_REVIEW.md,
INTEGRATED_GEOMETRY_REVIEW.md = a post-integration check "PASS", CANDIDATE_GEOMETRY.diff, before/after snapshots, check_finite_fillings.py with 25
exact matrix assertions). I read README.md, INTEGRATED_GEOMETRY_REVIEW.md, the start of FINITE_FILLINGS_AUDIT.md and FINITE_EXACT_RESULTS.json.
The reviews are by other agent sessions of the same workbench ("/root/s6_period_existence_reaudit"), not external.

#### 1.2 exact_algebra.tex (19 KB, 587 lines; 24–25 Aug)
"Exact integral algebra of the printed monodromy data". All \Verified. Hand-checkable certificates:
prop:monodromy-certificate (T_1^3=T_2^4=I, T_0, A_1, A_2, M_0, A_1A_2M_0=I); thm:cusp-lattices (ker(M_0-I)=im(M_0-I)=<w^,delta^>; T_0-invariants
of wedge^q V of ranks (1,2,4,2,1), all saturated); thm:coinvariants (V^G=Z gamma, (wedge^2V)^G=Z q, q=uw+6 gamma delta, (wedge^3V)^G=Z gamma uw;
V_G=Z[delta], (wedge^2 V)_G=Z[gamma delta], [uw]=6[gamma delta], (wedge^3V)_G=Z[uw delta]); prop:finite-indices (pi_j^* indices (1,3,1,1,3),
(1,4,2,2,4); pi_2^*H^2(S_2)={a gamma eta_2 + b q : a ≡ b mod 2}, by LHS spectral sequence + evenness of the form); prop:terminal-group
(G(l_0,l_1,l_2) = Z/|p|); prop:terminal-degree-two (im A = ker(4,2,3,2)); prop:terminal-all-degree (formal: H_* = (Z, Z/p, Z/p, Z/p, Z/p, 0, Z)
from stated algebraic outputs). These are [AC26] §2 (Lemmas 2.2–2.8), Lemma 7.13, Prop. 7.14, Thm 7.17, Lemma 7.19, Thm 7.22 and Appendix A.1.
Ledger: S6-ALG-P, S6-ALG-A2, S6-ALG-HOM (each with the nonclaim "does not identify the printed presentation/matrix with the geometric one").
CTX-FABLE-CERT in the ledger is unrelated to S6 ("degree-seven map has det DF=-2"; nonclaim: "No S6 lemma follows").

#### 1.3 integral_leray.tex (36 KB, 967 lines; Round 7, 26 Aug)
"Integral topology without the cusp-collapse argument".
- thm:p0-integral-specialization (l.23–399): sp^r: H^r(W;Z) -> H^r(F;Z) injective with image the T_0-invariants, 0<=r<=4. Nearby cycles psi
  (Dimca 4.2.1, 4.2.2, 4.2.11), H^b psi from the three local models, normalization resolution (5.5), E_2 ranks (1,2,4,2,1),(2,1,3),(2), degree 3 by
  a supported Thom–Gysin class along a compact T_f-orbit, saturation. This is [AC26] Appendix B (Thm B.1, §§B.2–B.7, l.5283–5590) step for step.
- prop:leray-e2 (l.412–591): H^0(B,R^1)=Z(12 gamma), H^0(R^2)=Z(2q), H^0(R^3)=Z(2 gamma uw); H^1(B,R^1)=H^1(B,R^2)=0 via the parabolic-cohomology
  quotient (5.17); H^2(B,R^r)=coinvariants. = [AC26] Lemma 7.25, Prop. 7.26. Stated only for the actual twist v_2=-eps' (the hypothesis
  4 | eta_2(v_2) of [AC26] Prop. 7.14).
- lem:first-transgression (l.595–688): d_2(12 gamma)=omega; new justification: the Cech discrepancy cocycle is identified with Leray d_2 through
  the canonical truncation triangle (Stacks 08J5, 0FLJ, 0F16). lem:higher-transgressions: d_2(2q)=omega[delta], d_2(2 gamma uw)=omega[gamma delta]
  by the derivation rule (r=s from signed products, s=2-r). thm:h2-vanishing. = [AC26] Prop. 7.27 (l.3143–3195), = [E26] Lemmas 7.5–7.6.
- prop:geometric-pi1 (l.772–934): based van Kampen with zero-section whiskers; real-marking computation a_j(g_j s)=A_j a_j(s) - v_j/m_j giving
  rho_j^{m_j}=t_{v_j}; pi_1(Y_eps)=1 from the toric formula on finite subfans, pi_1(N_0)=Lambda-bar; cusp meridian bounds the disc t -> (t,1,1).
  = [AC26] Lemma 7.4, Lemma 7.16 (sign lemma), Thm 7.17, Cor. 4.8. Only (l_0,l_1,l_2)=(0,1,-1).
- cor:candidate-sphere: X diffeomorphic to S^6, c_3=2.
Ledger: S6-NEARBY, S6-TOP-V1, S6-TOP-LERAY-D2, S6-TOP-END. Morphisms M-SP-P0, M-LERAY-D2, M-VK-*.

#### 1.4 topology_reduction.tex (46 KB, 1279 lines; Rounds 3, 12, 13: 25–27 Aug)
"The alternate collapse and Mayer–Vietoris route".
- prop:topological-spine (l.41–79): abstract lemma (contractible pair (A,A_0), free proper Gamma-action, compact quotient Q, collared boundary
  quotient H, same deck group => H is a strong deformation retract of Q, retraction lifts Gamma-equivariantly). This is exactly the argument inside
  [AC26] Lemma 7.8 + the "Existence" part of Lemma 7.9 (l.2267–2295), stated abstractly.
- lem:collapse-straightening, lem:positive-collapse, lem:phase-spread-collapse, prop:verified-cellular-collapse (l.106–371) = [AC26] Lemmas 7.5,
  7.6–7.8, 7.9, 7.10, with the same formulas ((C.3),(C.4) = L_t and G; (C.7) stabilizers; (C.13)–(C.15) tent-function modification).
- prop:verified-collapse-homology (l.388–519): 0 -> im(wedge^q M_0 - I) -> wedge^q Lambda -> H_q(W;Z) -> 0 exact, free; explicit [c_*]_2 (C.20),
  (C.19) c_*(beta ⊗ v) = sum_k nu_k(B_0 beta) nu_k(v)[C-bar_k], (C.21) in degree 3, (C.25) the image lattices. Statement = [AC26] Prop. 7.12 (l.2563) with
  Prop. 7.11; the matrix (C.20) and the table (C.25) are written out here.
- thm:collapse-equals-specialization (l.523–598): sp^q = i_F^* r^* = c^* for all q, integrally. [AC26] says this in one sentence (Remark B.2,
  l.5310: "With it (Proposition 7.2), sp^q is also the restriction map H^q(N_0') -> H^q(F)") and Remark B.4 says it is "not re-proved here".
- prop:actual-finite-band-maps (l.640–781): alpha_r = (pi_1*, -pi_2*) with matrices (MV.3), (MV.6), (MV.9), kernel nu_0 = -u^ - w^ + delta^, left
  kernel Phi=(4,2,3,2). prop:cusp-mv-blocks (l.785–918): K_1 = Z[a~_0], K_2 = <xi_w, xi_delta>, D_1 (MV.11) with det -p, j_* xi_delta = -p e.
  Remark (l.920–961): one-shot 9x9 collar matrix Delta_1 with det = 1 - 12 l_0. = [AC26] Lemmas 7.18, 7.19, 7.21 (sweeping), Thm 7.22.
- thm:mv-leray-comparison (l.965–1111): commuting squares (L.5), (L.7): Leray d_2 = dual of the MV cusp maps, all three coefficients -p.
- lem:cohomological-closure, thm:sphere-recognition (Hurewicz, Whitehead, Smale 1961/1962, Kervaire–Milnor), cor:abstract-s6,
  cor:candidate-mv-sphere (l.1124–1275) = [AC26] §8.
Ledger: S6-TOP-C1-SPINE, S6-TOP-C1, C2, C3, MV1, L1, END-MV, RECOGNITION, ABSTRACT (all VERIFIED). Morphisms M-COLLAPSE-Q, M-COLLAPSE-SP, M-MV-Q, M-MV-CUSP.

#### 1.5 finite_filling_certificates.tex (32 KB, 760 lines; 6 Sep 2026)
"Exact product covers, normalization branches, and peripheral kernels of the finite fillings" (labels ffcert:*; equations FF1–FF46).
No \Verified marks in the file; ledger id FINITE-FILLING-FULL-CERTIFICATES-20260906 (VERIFIED), morphism M-FINITE-PRODUCT-NORMALIZATION-20260906.
Evidence: `..\evidence\period_lattice_continuation_20260906\finite_fillings\` (check_exact_finite_products.py, EXACT_RESULTS.json: degrees 3·3=9, 2·4=8,
moving rotation matrices [[-2,-3],[1,1]], [[1,2],[-1,-1]], all assertions passed).
Contents: ffcert:prop:integral-summands (fixed and moving lattices, annihilators, det -3, -2); ffcert:thm:product-covers (candidate A1-5);
ffcert:prop:quotient-charts; ffcert:thm:normalization, ffcert:thm:peripheral-kernel, ffcert:cor:covering-h1 (candidate A1-6); the gluing
interface (repeats thm:candidate-global-geometry); ffcert:thm:normal-trivialization (candidate A1-7).

#### 1.6 algebraic_dimension.tex (11 KB, 299 lines; 26 Aug)
lem:torus-algebraic-reduction-audit; prop:very-general-torus-audit (NS(F_b)=Z eta outside a countable set, via P_E (3.1) and linear independence
of 1, tau, mu, beta, 6mu^2 - tau beta; G_eta = [[2 Im tau, 2 Im mu],[2 Im mu, (1/3) Im beta]], det = (2/3) Im tau · D < 0); lem:meromorphic-descent-audit;
thm:algebraic-dimension-audit (M(X)=f^*C(t), a(X)=1). "Provenance: the candidate's Lemmas 9.2–9.6 and Proposition 9.7, reconstructed with an
explicit Appell–Humbert matrix bridge, a proof that the smooth locus remains connected, and the omitted root estimate". Ledger S6-ALG-DIM.

#### 1.7 cusp_toric_cover_completion.tex (16 KB, 442 lines; Round 31, 3 Sep)
One theorem, cusp-cover-extension-theorem (\Verified), and two remarks. Candidate A1-8. Ledger S6-CUSP-KUMMER-COMPLETION,
S6-CUSP-FINITE-COVER-R4-AUXILIARY; morphisms M-CUSP-KUMMER-DIRECT, M-CUSP-KUMMER-RELATIVE. Related (not mine): cusp_spectral_geometry.tex
(S6-CUSP-SPEC-COVERS: the cover over the punctured disc and the metric R^4 limits).

#### 1.8 cusp_globalization_replacement.tex (28 KB, 738 lines; Round 29, 3 Sep)
One theorem, cusp-spec-globalization-obstruction (\Verified), parts (i)–(vi), with proof. It is an \input fragment that replaces a theorem inside
cusp_spectral_geometry.tex (it cites cusp-spec-native-quotient, cusp-spec-full-inverse-transpose, cusp-spec-radial-notation there and
cusp-cone-S12-route etc. in cusp_cone_sphere_routes.tex; those are reader C1's files). Candidates A1-1 and A1-9.
Ledger: S6-CUSP-FOUR-COPY-R4 (VERIFIED), S6-CUSP-LITERAL-COMPACT-EXTENSION (REFUTED = the nonextension is proved);
morphisms M-CUSP-GLOBAL-FOUR-CIRCLE, M-CUSP-GLOBAL-FOUR-CIRCLE-EXTENSION (REFUTED), M-CUSP-CONE-Q1.

#### 1.9 local_repairs.tex (3 KB, 53 lines)
Seven items; candidate A1-18.

#### 1.10 mathematical_summary.tex (145 KB) — parts read
l.1–56 (6 Sep: includes the statement X_c ≅ X_{c'} <=> c'-c in 2Z, see A1-X1), l.116–192 (canonical ring; period deformation; 5 Sep corrections;
exact period constants and cusp edge maps), l.395–540 (construction, cusp fibre, algebraic reduction, Leray route, van Kampen), l.1060–1128
(collapse, MV), l.1630–1948 (four-copy quotient, Kummer model, cone carriers q_2, q_{1,cusp}, q_1), l.3652–3782 (certificates, review checkpoint,
"current evidence boundary"). The summary adds nothing mathematical to the files above; it is the status view.
"Independent review checkpoint" (l.3671–3686): a "Reviewer B" reviewed the reconstruction up to a cutoff and "found no load-bearing defect in the
non-collapse nearby-cycle/Leray and based van Kampen route".

#### 1.11 Ledgers
claim_ledger.txt: JSON lines; my ids extracted to `work\scratch\A1\ledger_extract.txt`. morphism_ledger.txt: 124 lines, entries listed in 1.3–1.8.
uncertainties.txt: U-CUSP-ACTION, U-SPECIALIZATION-INDEX, U-COLLAPSE-COMPARISON, U-MERIDIAN-SIGN all VERIFIED; U-EXTERNAL-ADJUDICATION OPEN.

#### 1.12 Comparison with [E26]: what each side has
What Engel's route gives with little work and the workbench (like [AC26]) proves at length:
- Existence of the period data. Engel: elliptic surface y^2 = x^3 - 3t^3(t-1)x + 2t^4(t-1)^2, M = O(P-O), Lemma 2.1 (Shioda heights give
  Hom(t_{6P}^*M, M) = O(1)), Cor. 2.2. Workbench: l.113–561 of candidate_geometry.tex (lifting through j, two torsor problems, cusp regularity).
- Proper discontinuity / nondegeneracy of the lattice. Engel: Prop. 2.4, a contraction argument for |u| < c. Workbench: D < 0 after a constant shift.
- The cusp filling. Engel: Prop. 2.7–2.8, citing the Mumford construction. Workbench: l.652–1065, a self-contained proof for the infinite fan.
- The section over the cusp. Engel Prop. 2.9; workbench: the disc t -> (t,1,1).
- Bagnera–de Franchis types of the multiple fibres. Engel: Cor. 3.2, Cor. 3.9, immediate from the good-reduction picture.
  Workbench: classification table in [AC26]; explicit product covers in finite_filling_certificates.tex.
- The integral monodromy. Engel derives it (Thm 5.1) from the overlattices and primitivity of im N; the workbench certifies printed matrices.
What the workbench (with [AC26]) has that Engel does not:
- A complete proof that sp^k at the cusp is an isomorphism onto the invariants in all degrees, integrally (Engel Lemma 7.4, last paragraph: "A
  computation of the Mayer–Vietoris spectral sequence for the toric stratification ... shows"); and a second, independent homology computation
  (collapse + Mayer–Vietoris) with the comparison sp = c^* and the MV/Leray commuting squares.
- pi_1 = Z/|p| and H_* = (Z, Z/p, Z/p, Z/p, Z/p, 0, Z) for all (l_0,l_1,l_2) — but this is [AC26] Thm 7.17/7.22; the workbench re-proves the algebra
  and the cusp blocks for general p, the geometry only for (0,1,-1) (see section 3, item 5). Engel treats |p| = 1 only.
- a(X)=1 with f the algebraic reduction, by a direct NS computation (Engel quotes [AC26] §9.1 in Remark 8.4).
- The exact parameter half-plane Im c_0 < -M (A1-2); explicit gluing multipliers of W (A1-4); explicit moduli of the bielliptic fibres (A1-5);
  the Kummer cover (A1-8); the rigorous Seifert quotient away from the cusp and the nonextension at the cusp (A1-1), which bears on [E26] Rem. 8.3;
  in neighbouring files (not mine): the classification X_c ≅ X_{c'} <=> c'-c in 2Z and the nonzero Kodaira–Spencer class (A1-X1), which bear on
  [E26] Rem. 8.1; pointed R^4 limits of covers and quotients (A1-9).
What Engel has that these files do not: the geometric origin (rational elliptic surface, Mordell–Weil generator P, line bundle, linearization);
the conceptual derivation of the integral monodromy; the invariant class of type (1,6) as a first Chern class; Conjecture 8.2 (flat limit at u=0);
the conifold-transition remark 8.5. The workbench never uses the elliptic-surface description (no occurrence of Mordell–Weil or Weierstrass in the
S6 files); see the remark on mu(p_0) in A1-4.

#### 1.13 Quotient maps of the kind of [E26] Remark 8.3 in my files
Only cusp_globalization_replacement.tex computes with them: chi_gamma = (f, theta_gamma): J -> B° x R/Z is exactly the quotient by the rank-3
subtorus family ker(gamma) = ker(phi); part (iv) gives the Seifert solid tori C_j at p_1, p_2; part (v) proves that the literal map does not extend
continuously over W. The file does not form the closed Seifert manifold Q = S^3 of Engel; the neighbouring cusp_cone_sphere_routes.tex cones the
boundary torus instead (map q_1: X -> C = M ∪ Cone(∂M), M = (P x S^1) ∪ C_1 ∪ C_2; mathematical_summary.tex l.1873–1924). [AC26] itself has the
Seifert reading only as a heuristic on its first summary page (Orlik's formula |a_1a_2e_0 + a_2b_1 + a_1b_2|, "glue so that the coinvariant circle
of the fibres traces out the (3,4) Seifert fibration of the three-sphere"). Details in A1-1.

---------------------------------------------------------------------------------------------------------------------------

---

### Reader B: Complex-analytic part: CDP, Picard, Hodge, Bott-Chern, canonical ring, deformation, classification (workbench)

Full notes: `work\B_notes.md`.


#### 1.1 `WB\cdp_program.tex` (63.6 KB, 1665 lines; content 26-30 Aug 2026, corrected 5 Sep 2026)
Section "The non-normal fibre and the CDP obstruction". Every statement carries a mark \Verified or \Refuted.
- L17-110. The p. 692 inference of CDP20. `prop:missing-cotangent-filtration` (L52): for a reduced effective Cartier divisor S in a
  smooth threefold, 0 -> N^* -> K_S -> T_S -> 0 and 0 -> K_S -> Omega_X|_S -> Omega~_S -> 0, K_S = kernel of Omega_X|_S -> Omega_S/torsion.
  `prop:missing-global-section-criterion` (L81): the "exact global-section criterion" (connecting map delta_A).
- L112-274. Local algebra of a reduced normal-crossings fibre. `lem:conormal-injective` (L124), `lem:conductor-square` (L153, the
  sequence 0 -> O_S -> eta_* O_S~ + O_D -> eta_* O_D~ -> 0), `prop:conductor` (L209, "conductor-supported ambient differential").
  These three are [AC26] (10.1), Lemma 10.2, Lemma 10.3 almost verbatim.
- L276-353. `prop:nodal-counterexample` (\Refuted mark on the CDP inference): the test family (nodal cubic pencil) x P^1.
- L355-486. `thm:cartier-duality` (L357), `prop:cartier-duality-absolute` (L427): Serre-Grothendieck duality on a compact Cartier
  divisor / full fibre without normality (Ramis-Ruget). Rewritten on 5 Sep (the pairing is now built from the analytic trace).
- L488-600. `lem:curve-flatness`, `prop:analytic-base-change`, `cor:surface-top-base-change` ((5.17-V), (5.17-T): R^q f_* E = 0 for
  q > 2 and top-degree base change at every fibre, also non-reduced ones).
- L602-1196. "A topology-independent Pic^0 route and three all-Pic routes": `prop:pic0-pullback`, `prop:all-pic-restriction`
  (r = eta^* i^*: Pic(X) -> Pic(dP_6)), `prop:leray-edge-restriction` (certificate 1), `lem:picard-crossed-defect`,
  `lem:picard-finite-norm` (N_{T_j} d_j = iota_{v_j} E), `lem:picard-cusp-defect`, `prop:direct-boundary-picard` (certificate 2:
  c_1(L|_F) = 0 from 4n - 3n = n = 0); L1143 inputs `analytic_picard_completion.tex` (certificate 3); `cor:candidate-pic0-route`.
- L1198-1300. `thm:candidate-conductor` (hypotheses H1-H4) and `cor:candidate-conductor-actual`: R^2 f_*(T_X (x) L) != 0 for all L.
  This is [AC26] Theorem 10.5(a).
- L1302-1358. `lem:semidirect-abelianization` (= [AC26] Lemma 10.7); minimal counterexample Z x|_{-1} Z; formula (5.22).
- L1360-1606. "The corrected theorem that survives both defects": `lem:cdp-generic-endpoints`, `thm:corrected-cdp-global`,
  `cor:corrected-cdp-relative`, `thm:corrected-cdp-fibrewise`, remark on scope, "exact monodromy repair" (5.33).
- L1608-1665. "Exact present disposition" (six items) and `test:cdp-comparison`.
Relation to other files: inputs `analytic_picard_completion.tex`; depends on `candidate_geometry.tex`, `integral_leray.tex`,
`exact_algebra.tex` (not my files). Evidence packet: `..\evidence\s6_cdp_direct_image_reaudit_20260905\`.

#### 1.2 `WB\analytic_picard.tex` (26.3 KB, 709 lines; 26 Aug 2026)
"Structure-sheaf direct images and uniform non-torsion". A re-derivation of [AC26] Lemma 9.10, Prop. 9.11, Lemma 9.12, Prop. 9.13,
Theorem 10.5(b), Prop. 10.8, all marked \Verified:
`lem:hodge-line-audit` (f_* omega_{X/B} = O(1); det R_{g_j}(z_j) = zeta_j^{a_j}, (a_1,a_2) = (2,1); canonical section with divisor
k_j S_j, k_j = m_j - 1 - a_j = (0, 2), kept apart from the generator s_j^{-a_j} e of the direct image);
`lem:finite-normal-order-audit` (O(S_j)|_{S_j} has exact order m_j); `lem:cusp-structure-sheaf-audit` (h^q(O_W) = (1,2,1));
`thm:structure-direct-images-audit` (f_*O = O, R^1 = O + O(-1), R^2 = O(-1), base change at all fibres);
`cor:picard-line-audit` (Pic(X) = Pic^0(X) = C; restriction to every scheme fibre injective);
`thm:uniform-nontorsion-audit` (= Prop. 10.8); `rem` "provenance of the repair".
The file then inputs `finite_filling_certificates.tex` (not mine), `analytic_picard_local_obstruction.tex`,
`analytic_canonical_ring.tex`, `period_parameter_deformation.tex`, `period_shift_classification.tex`.

#### 1.3 `WB\analytic_picard_completion.tex` (35.0 KB, 1042 lines; 30 Aug 2026)
"An analytic completion of the all-Picard certificate". `prop:analytic-ah-boundary` (crossed homomorphism d: pi_1(P) -> V_R of
a line bundle, built from logarithms of O^* factors; N_{T_j} d_j = iota_{v_j} E; <d_0, delta^> = 0 by the argument principle on a
Stein chart); `lem:analytic-support-specialization` (L629: the degrees of nu^*(M|_W) on the hexagon determine the mixed
Appell-Humbert block of M|_{F_t}); `thm:analytic-all-picard` (L986: r = 0, "third certificate"). Checker
`supporting_materials\reproducibility\verify_analytic_picard_completion.py` (25 checks, not read).

#### 1.4 `WB\analytic_picard_local_obstruction.tex` (14.2 KB, 484 lines; 29 Aug 2026)
`prop:local-cusp-picard-obstruction`: the explicit line bundle L_Q on the cusp neighbourhood N_0; remark with Bingener 1980.

#### 1.5 `WB\hodge_frolicher.tex` (48.4 KB, 1329 lines; 27 Aug 2026, three internal audits that day)
"Hodge numbers, cotangent direct images, and the Frölicher page".
`prop:workbench-holomorphic-form-vanishing` (L17, = [AC26] Prop. 9.20, shortened);
`thm:parametric-hodge-diamond` (L100); `thm:frolicher-e2-candidate` (L166);
`prop:period-derivative-determinant` (L218: K = det(dZ/dz) = 6 mu'^2 - tau' beta' is not identically 0 and K(z_1) = 0);
`prop:log-relative-direct-images` (L319: E = Omega_X(log D)/f^* Omega_B(log Sigma), R^q f_* E, invariant bases (11.4));
`prop:log-ks-divisor` (L525: div det kappa_0 = p_1 + p_2; kappa_1 surjective; ord_{z_1} K = 2, ord_{z_2} K = 0);
`prop:absolute-cotangent-direct-images` (L707: R^q f_* Omega^1_X); remark "the cusp is not the torsion locus" (L811-1008:
Omega^1_{X/B} is torsion-free near W, torsion exactly at the multiple fibres; "The reconstructed manuscript's assertion that
torsion occurs at all three singular fibres is false");
`thm:h12-scalar` (L1012); `cor:exact-hodge-diamond` (L1129); `thm:exact-bott-chern-aeppli` (L1189);
L1312 inputs `bott_chern_algebra.tex`; `record:h12-direct-images` (L1314, \Open: independent human replication outstanding).

#### 1.6 `WB\bott_chern_algebra.tex` (30.4 KB, 809 lines; integrated 30 Aug - 4 Sep 2026)
"Period-coordinate Dolbeault classes and the Bott-Chern algebra". Fibre representatives Gamma, U, Q_F ((bcpr-gamma-form) etc.);
`lem:bcpr-degree-one-input`, `lem:bcpr-eta-extension`; the factor 12 (exp(12 g) = f^*O(1)) and c_{1,BC}(exp(z g)) = zA + z^- B
(L371-486); `prop:bcpr-generators-are-bases` (L513); `thm:bcpr-square-zero-algebra` (L626); two remarks saying that no literal
global coefficient formula for the forms G, Q is given.

#### 1.7 `WB\analytic_canonical_ring.tex` (7.5 KB, 169 lines; 6 Sep 2026)
`thm:canonical-ring-recovery` (CR1)-(CR5), no status mark in the file; ledger S6-CANONICAL-RING-20260906 says VERIFIED.

#### 1.8 `WB\period_parameter_deformation.tex` (18.3 KB, 396 lines; 6 Sep 2026)
`thm:retained-period-deformation` (PD1)-(PD18). Ledger S6-RETAINED-PERIOD-DEFORMATION-20260906: VERIFIED ("independent
GLOBAL_AUDIT.md; checker 15 identities" - those two files were not located by me).

#### 1.9 `WB\period_shift_classification.tex` (25.7 KB, 590 lines; 6 Sep 2026; header "New proof fragment")
`pshift:thm:classification` (PS1)-(PS29), `pshift:lem:centralizer`. No own ledger id; recorded in the dated note at the end of
`ledgers\claim_ledger.txt` (L144-152, "original analytic-family classification c modulo 2Z") and in
`mathematical_summary.tex` L45-54.

#### 1.10 Ledgers and summary
- `WB\ledgers\claim_ledger.txt` (152 lines of JSON): entries read: S6-CDP-CONDUCTOR, -CONDUCTOR-W, -P692 (REFUTED), -DUAL, -BC,
  -R2-IF, -HYPOTHESES, -CONFLICT, -10.8, S6-CDP98-MONO (REFUTED), -DUAL-ABS, -PIC0, -RESTRICTION, -R-LERAY, -R-BOUNDARY,
  S6-HODGE-PARAM, -KS, -H1, -BCA, S6-CDP-CONDUCTOR-ABSTRACT, S6-CDP-R-LOCAL-OBSTRUCTION, S6-OPEN-R-ANALYTIC (VERIFIED despite the
  name), S6-OPEN-HODGE-REPLICATION (OPEN), S6-OPEN-HODGE-REPRESENTATIVES (VERIFIED), S6-OPEN-CDP-REPAIR (VERIFIED),
  S6-OPEN-EXTERNAL-ADJUDICATION (OPEN), S6-HODGE-CUSP-TORSION (REFUTED, names "Remark 1.3" of the original),
  S6-CANONICAL-RING-20260906, S6-RETAINED-PERIOD-DEFORMATION-20260906, and the 6 Sep note.
- `WB\ledgers\uncertainties.txt`: U-CDP-HYPOTHESES, U-CDP-P692-INFERENCE, U-CDP98-COINVARIANTS, U-PROP-10.8, U-CDP-R-DIRECT,
  U-CDP-R-ANALYTIC, U-HODGE-H12, U-HODGE-BCA, U-HODGE-REPLICATION (OPEN), U-HODGE-REPRESENTATIVES, U-CDP-REPAIR,
  U-HODGE-CUSP-TORSION. They repeat the claim ledger.
- `WB\ledgers\topic_literature_route_analytic_picard.json`: sources used for the third certificate (Birkenhake-Lange ch. 1 §2,
  Schnell's lecture notes, Fulton, Cox-Little-Schenck, Cartan 1957); says "unresolved_dependencies: []".
- `WB\mathematical_summary.tex`: read L1-200 (6 and 5 Sep items: classification, canonical ring, deformation, exact period
  constants, cusp edge multipliers), L440-640, L980-1135, L1295-1330; the rest of the S6 items (L1130-1510) repeats
  hodge_frolicher.tex and bott_chern_algebra.tex and was only skimmed.
- `WB\candidate_geometry.tex` L555-617 (`prop:period-exact-admissible-constants`): read because the deformation files rest on it.

#### 1.11 Evidence and checker
- `...\workbench\evidence\s6_cdp_direct_image_reaudit_20260905\`: README.md, AUDIT.md (28 KB; read §§1-3, 7, 8), INPUT_HASHES.md,
  replacement_passages.tex, before\ and after\ copies of cdp_program.tex and integral_leray.tex, full.diff,
  integration_receipt.md, manifests. The audit (5 Sep) found two faulty passages (an unconstructed "unique middle duality
  isomorphism"; the logarithmic translation alpha(s) Pi(s) v_j treated as a real multiple of v_j) and replaced them; the finite norm
  sign and the endpoint relation did not change. It also records: Pic^0(W) = (C^*)^2; a twist-bookkeeping slip in CDP20's prose
  (the factor omega_X missing in the fibrewise dual H^0 for a fixed L); the correspondence of theorem numbers between the arXiv
  and journal versions of CDP98.
- `supporting_materials\reproducibility\verify_direct_boundary_picard.py` (5.6 KB): 14 integer checks: T_1^3 = T_2^4 = I; the
  relations (T_j - I)V have rank 3 with gcd of 3x3 minors 1 (so V_G = Z, primitive); delta-coordinates of eta_1, eta_2 are 3, 2;
  iota_{v_1}(2q) = 4 eta_1, iota_{v_2}(2q) = -6 eta_2; 12/3 = 4, -12/4 = -3, 4 - 3 = 1. Two of the checks are tautologies
  (a list of even numbers; 4 + (-3) = 1). It verifies the lattice arithmetic only, as its docstring says.

#### 1.12 [AC26] sections read for comparison
L3239-3260 (Theorem 9.1), L3566-3600 (Remark 9.9), L3603-3682 (Lemma 9.10, Prop. 9.11), L3858-3942 (Prop. 9.13, §9.4),
L4223-4400 (Lemmas 9.17-9.19, Prop. 9.20, Remark 9.21, Cor. 9.22, Props. 9.23-9.24, Remarks 9.25-9.27), L4404-4881 (all of §10).
[E26] read in full.

---

---

### Reader C1: Cusp sphere-carrier and homotopy files (workbench)

Full notes: `work\C1_notes.md`.


#### 1.1 `W\research\cusp_cone_sphere_routes.tex` (38.7 KB, 950 lines) — read in full
Subsection "Cone-compactified sphere carriers for the native cusp quotient" (label `cusp-cone-section`).
- Lemma `cusp-cone-native-descent` (l.33-94): the quotient `pibar: N_0 \ W -> D_0^* x Tbar^2`,
  `Tbar^2 = (Lambda/K) (x) R / (Lambda/K)`, well defined because `M_0 = id mod K`; on `F_T` it is
  `pi_T: F_T -> Q_T = R^2/Y_T Z^2`, `sys(Q_T) >= T - C`.
- Theorem `cusp-cone-S12-route` (l.118-271): `q_2: (X,x_0) -> (A,v_0)`, `A = Susp(S^1 x Tbar^2) = Susp(T^3)`
  (unreduced), `q_2(x) = [r, e^{i phi}, pibar_f(x)]` for `t = r e^{i phi}`, `q_2(W) = v_0`,
  `q_2(X \ int N_0) = v_1`; smash square `X^X = S^12 -> A^A`; restriction to `F_T^2` is `pi_T x pi_T`;
  `(Q_T^2, 0) -> (R^4, 0)` pointed GH; reduced homology of `A` (Z^3, Z^3, Z in degrees 2,3,4) and of `A^A`.
- Proposition `cusp-cone-S24-local-route` (l.287-358): `q_{1,cusp}: X -> B = Susp(T^2)`,
  `x -> [r, e^{i phi}, theta_gamma(x)]`; fourth smash power, source `S^24`.
- Theorem `cusp-cone-S24-route` (l.394-561): `M = (P x S^1) u C_1 u C_2` (pair of pants times circle, glued
  to the two Seifert solid tori), `partial M = partial D_0 x S^1`, `C = M u Cone(partial M)`;
  `q_1: X -> C` equal to `(f, theta_gamma)` over `P`, the Seifert-target maps over `D_1, D_2`,
  `[r,(e^{i phi}, theta_gamma)]` on `N_0 \ W`, `W -> c_0`. `H_1(M) = Z<g>` with
  `rho_0 = -g, rho_1 = 4g, rho_2 = -3g, eta = 12g` (meridian relations `3 rho_1 - eta = 0`,
  `4 rho_2 + eta = 0`); `H~_k(C) = Z` for `k = 2,3`.
- Definition `cusp-cone-target-slice-embeddings`, Proposition `cusp-cone-metric-scope` (l.563-638):
  ambient diameters of the slices tend to 0 in any fixed compatible metric, intrinsic diameters to infinity.
- Proposition `cusp-cone-S12-almost-complex-obstruction` (l.640-782): three proofs that no homotopy `S^12`
  is almost complex (Borel-Serre `P^1_5(c_2) = 6 c_6` mod lower classes; Bott integrality `120 | c_6`;
  `p_3 = -2 c_6` on the standard sphere).
- Theorem `cusp-cone-obstructions` (l.784-917): rank bound `rank(Lambda^{(+)r}/N) <= r` for full-base
  quotients with diverging systole; no finite base cover preserves `K`
  (`(A_2A_1)^n w^ = w^ + n(u^ - delta^)`); no fixed `T^4` or `S^4` target; products and joins are not
  `S^12`, `S^24`.
All statements carry the workbench status VERIFIED via ledger entries S6-CUSP-CONE-SPHERE-ROUTES and
S6-CUSP-CONE-OBSTRUCTIONS.

#### 1.2 `W\research\cusp_sphere_route_strengthening.tex` (46.8 KB, 1186 lines) — read in full
- Theorem `cusp-cone-optimal-exponents` (l.29-139): two copies necessary and sufficient cusp-locally
  (rank <= 2r), four over the full base (rank <= r), "within native connected torus quotients with the
  unscaled metric".
- Theorem `cusp-cone-angle-forgotten-sphere-carriers` (l.141-472): the sphere-valued maps
  `q^_3 = p^_2 o q_2: X -> S^3`, `p^_2([r, e^{i phi}, u]) = [r, c(u)]`, `c: Tbar^2 -> Tbar^2/K^(1) = S^2`
  the collapse of the coordinate 1-skeleton, target `Sigma_r(S^2) = S^3`; and
  `q^_gamma = p^_1 o q_{1,cusp}: X -> S^2`, `p^_1([r, e^{i phi}, theta]) = [r, theta] in Sigma_r(S^1)`.
  Moving 4-spheres `S_T^2 ^ S_T^2 c S^6`, `C_T^{^4} c S^8` with exact Euclidean balls of radius `R` once
  `T - C > 4R` (resp. `l_T > 4R`).
- Corollaries `cusp-cone-S12-sphere-map-null`, `cusp-cone-S24-sphere-map-null` (l.474-563): both smash
  maps null; the general statements (see C1-6).
- Corollary `cusp-cone-literal-R4-open-cells`, Remarks `cusp-cone-moving-S4-null-homotopy`,
  `cusp-cone-sphere-map-homotopy-status` (l.565-676). The last one states the status:
  "`[q^_3] in pi_6(S^3)` is now zero by Theorem `cusp-null:thm`; `[q^_gamma] in pi_6(S^2)` remains open."
- Proposition `cusp-cone-explicit-carriers` (cones on `T^4`, local homology at the vertex), Theorem
  `cusp-cone-target-homotopy-types` (l.788-886): `A^A ~ V^9 S^4 v V^18 S^5 v V^15 S^6 v V^6 S^7 v S^8`,
  `pi_1(M) = <x,y,h | [x,h],[y,h], x^3 = h, y^4 = h^{-1}>`, `pi_1(C) = 1`, `C ~ S^2 v S^3`,
  `C^{^4} ~ S^8 v V^4 S^9 v V^6 S^10 v V^4 S^11 v S^12`.
- Theorem `cusp-cone-exact-decompactification-space` (l.888-1136): 5-manifolds `E_nu` with boundary `R^4`,
  comparison maps `beta_nu: E_nu -> D_nu` continuous, surjective, not proper, not quotient maps
  (ledger: S6-CUSP-DECOMPACTIFICATION-QUOTIENT REFUTED). Corollary `cusp-cone-sharp-global-R4-scope`.
Ledger: S6-CUSP-SPHERE-MOVING-S4, S6-CUSP-SPHERE-LITERAL-R4-OPEN-CELLS (VERIFIED).

#### 1.3 `W\research\cusp_sphere_fixed_metric.tex` (35.8 KB, 917 lines) — read in full
Label prefix `sphere-metric-`. Theorem `sphere-metric-uniform-collapse` (any fixed compatible metric:
slices Hausdorff-converge to the smash base point); Theorem `sphere-metric-fixed-realization` (explicit
metric `g_A = dr^2 + r^2 du^2 + (r/T(r))^2 h_{T(r)}`, `g_B = g_C = dr^2 + r^2(du^2 + d theta^2)` near the
cone; slice blow-ups by `T/r_T` resp. `l_T/r_T` converge to `R^4`, ambient blow-ups to `R^8`, `R^12`);
Theorem `sphere-metric-scaling-trichotomy` (limit is a point, a square flat `T^4`, or `R^4` as
`lambda_T r_T -> 0, L, infinity`); Corollary `sphere-metric-unit-volume`; Proposition
`sphere-metric-tangent-scope` (links `T^3*T^3`, `(T^2)^{*4}`, `partial(M^4)`; local homology of
`C^{^4}` at the base point). Ledger: S6-CUSP-SPHERE-FIXED-METRIC (VERIFIED).

#### 1.4 `W\research\cusp_s12_carrier_homotopy.tex` (25.3 KB, 609 lines) — read in full
- Theorem `cusp-s12-full-carrier-null` (l.40-110): `[x ^ y] = 0 in pi_12(S^6)` for all `x, y: S^6 -> S^3`.
- Corollary `cusp-s12-all-higher-smashes-null`; Remark `cusp-s12-one-copy-invariant` (the regular fibre of
  `q^_3` is a `T^3` = mapping torus of the kernel 2-torus over the circle `|t| = r_0`).
- Subsection "The original cusp coefficient: an explicit framed nullbordism": Theorem `cusp-null:thm`
  (l.242-565), `g = q^_3` is based null-homotopic; Corollary (`a = 0 mod 12`, `E^6 g = 0`). The same
  theorem appears as `h24:thm:cusp-g-zero` in `higher_rung_24d_continuation.tex`.
Ledger: S6-CUSP-ONE-COPY-FRAMED-NULL (VERIFIED), M-CUSP-ONE-COPY-FRAMED-NULL.

#### 1.5 `W\research\higher_rung_24d_continuation.tex` (304 KB) — only l.4375-5112 and l.5750-6110 read
(the block `RETAINED_ANGLE_AND_HOPF_BRIDGE_20260905`; it is where the ledger entries
S6-CUSP-RETAINED-ANGLE-ARF and S6-CUSP-HOPF-NONZERO-MOD24 point).
- Theorem `h24:ret:main` (l.4524-4536; proof to l.5051): `H = p_3 q_2: X -> S^4`,
  `p_3([r,z]) = [r, c_3(z)]`, `c_3: T^3 -> T^3/K^(2) = S^3` (collapse of the coordinate 2-skeleton of
  `S^1_phi x Tbar^2`), target `Sigma_r S^3 = S^4`; `[H] = eta_4 o eta_5 != 0 in pi_6(S^4) = Z/2`.
- Corollary `h24:ret:q2-detected-quotient` (l.5070): `q_2` is not null; odd multiples of `[q_2]` nonzero.
- l.5112-5750 (`h24:rettri:*`, "three-dimensional bundle inside the triality carrier"): not read (outside topic).
- Theorem `h24:hbridge:mu-theorem` (l.5817): `mu_eta: pi_6(S^4) -> pi_9(S^6)`, `[x] -> [eta_2 ^ x]`,
  injective, `[eta_2 ^ H] = 12 nu_6`. Theorem `h24:hbridge:peripheral-theorem` (l.5970):
  `Psi_H = mu_eta o Theta_H o chi: SL_2(Z) -> pi_9(S^6)`, values `(12 nu_6, 0, 12 nu_6)` on `(C_0, C_1, C_2')`.

#### 1.6 `W\research\cusp_globalization_replacement.tex` (28.5 KB, 739 lines) — read in full
Not on my list, but it holds the statements the cone files depend on and the ledger entries
S6-CUSP-FOUR-COPY-R4 and S6-CUSP-LITERAL-COMPACT-EXTENSION. One theorem,
`cusp-spec-globalization-obstruction` (marked \Verified), parts (i)-(vi):
(i) `chi_gamma = (f, theta_gamma): f^{-1}(B^o) -> B^o x R/Z`, fibrewise group epimorphism with kernel the
`T^3`-family of `L`; `Hom(Lambda,Z)^Delta = Z eps_gamma` (l.319-326);
(ii) circumference `l_T = D_T / sqrt(L_T^2 + m_T^2) = T + H - B + O(1/T)`;
(iii) four copies, minimality;
(iv) finite fillings: `Phi_j(s,x) = (e^{-2 pi i/m_j} s, A_j x + v_j/m_j)`,
`(m_1, v_1, kappa_1) = (3, gamma^+2u^-4w^, 1)`, `(m_2, v_2, kappa_2) = (4, -gamma^-3u^+3w^, -1)`,
`kappa_j = eps_gamma(v_j)`; Seifert targets `C_j = Delta_j x R/Z / ((s,theta) ~ (e^{-2 pi i/m_j}s, theta + kappa_j/m_j))`,
solid-torus chart `w = s u^{r_j}`, `U = u^{m_j}`, `t_j = w^{m_j} U^{-r_j}`; `N_j -> C_j` is a smooth proper
`T^3`-bundle; overlap identity `chi_gamma o h_j = h_j^{S^1} o chibar_j` (l.474-502);
(v) cusp nonextension (proof l.551-657): two radial paths with `B_0 a = (1/4,1/4)`, `B_0 a' = (1/4,1/2)`
converge to the same triple point of `W` and carry `theta_gamma = 3/4` and `1/2`; the class of
`theta_gamma` in `H^1` does extend over `N_0` (`pi_1(N_0) = Lambda/K`), "hence a map to `S^1` whose
restriction is homotopic to `chi_gamma`" (l.645-657);
(vi) products/smashes, Borel-Serre.

#### 1.7 `R\s6_cone_sphere_routes_preprint.tex` (224.7 KB, 5561 lines; dated "5 September 2026")
Title "Real S^12 and S^24 Routes from Alpoge's Candidate (3,4,infinity) Two-Torus Fibration". Read:
abstract and status paragraph (l.43-160), all section and theorem headings, l.1485-2130, l.3418-3470,
l.3590-3640, l.3712-3946; the rest compared by heading with the research files.
It is an assembly, with its own labels, of: the input data and `cusp_globalization_replacement`
(sections 1; "Why the literal circle map cannot cross the cusp" l.553-595), `cusp_cone_sphere_routes`
(sections 2-3, 7), `cusp_sphere_route_strengthening` (section 4), `cusp_sphere_fixed_metric` (section 5),
`cusp_s12_carrier_homotopy` (l.1491-1617 and l.3947-4357), and the retained-angle and Hopf blocks of
`higher_rung_24d_continuation` (l.4358-5460). It contains five items that are not in the four research
files I was given:
- Theorem `thm:one-copy-framing-reduction` (l.1619-1772): stable framings of a closed oriented 3-manifold
  form a torsor with stages `H^1(N;Z/2)` (spin) and `H^3(N;Z)`; an honest rank-3 twist changes the
  Pontryagin-Thom class by `2 nu`; `[T^3, Lie] = eta^3 = 12 nu`. Standard (Kirby-Melvin, Levine, Adams
  are cited); it is the general frame for C1-2 below.
- Corollary `cor:smash-join-product-separation` (l.1833): joins are null; `h^{x r}` is null iff `h` is.
- Theorem `thm:SU3-clutching-scope` (l.1986-2125): `SU(3)`-bundles `P_k` on the moving `S^4`; they do not
  extend over the ambient sphere; pullbacks along the null sphere maps are trivial;
  `pi_7(SU(3)) = 0`, `pi_11(SU(3)) = Z/4`. Routine.
- Section "The nine-dimensional Gram carrier" (l.3418-3711): `Mat_3(C)/U(3) = Herm_3^+`, one-point
  compactification `B^9`, boundary `S^8`; "no structure-preserving bridge is constructed". Not about `S^6`.
- Section "An ancillary finite-cover route" (l.3712-3827): `S_N = diag(1,1,N,N)`,
  `S_N^{-1} M_0^N S_N = M_0` (ledger S6-CUSP-FINITE-COVER-R4-AUXILIARY).
Lemma l.949 "The cone attachment as a collapsed-boundary quotient" records `C = M/partial M`.

#### 1.8 Ledgers (`W\research\ledgers\`)
`claim_ledger.txt` lines 3-6, 60-62, 74-75, 113-115 read in full; `morphism_ledger.txt` lines 2-8, 48-52,
85-87 read (M-CUSP-SPHERE-Q3, -QGAMMA, -Q3-SMASH, -QGAMMA-SMASH, -U12/U24-OPEN-CELL,
M-CUSP-DECOMPACTIFICATION-BETA-QUOTIENT (REFUTED), M-CUSP-CONE-Q2, -Q2-SMASH, -Q1-LOCAL, -Q1, -Q1-SMASH,
M-CUSP-ONE-COPY-FRAMED-NULL, M-CUSP-RETAINED-ANGLE, M-CUSP-HOPF-PERIPHERAL). The ledger statements agree
with the tex. Two points: (a) S6-CUSP-SPHERE-MOVING-S4 proves `g ^ g = 0` by "Toda Prop. 5.11:
`st: pi_12(S^6) -> pi_6^S` is an isomorphism, `st(g^g) = (2a nu)^2 = 4a^2 nu^2 = 0`", while
`cusp_s12_carrier_homotopy.tex` uses the exponent argument (C1-6); `mathematical_summary.tex` l.2000-2035
has the Toda version. Both are correct. (b) entries 113-115 (5 Sep) use a shorter schema without
`depends_on`. `next_lemmas.tex` l.430-452 and `uncertainties.txt` (U-CUSP-SPHERE-*, U-CUSP-CONE-SPHERE-ROUTES,
U-CUSP-GLOBAL-R4-GENERALIZATION) repeat the same status.

#### 1.9 Evidence folders
- `W\evidence\cusp_framing_20260905\`: `MATHEMATICAL_AUDIT.md` (result, the repaired smoothing-neighbourhood
  mismatch), `verify_framing_jacobian.py` + `FRAMING_JACOBIAN_CHECK.json` (five sympy identities:
  `B_0 u_0 = (1/4,1/4)`, `det J = det(l B_0 + lambda R)`, `det J_0 = l^2`), `PROOF_INTEGRATION_RECEIPT.json`,
  build and visual-QA receipts (workbench then 624 pages, cone/sphere preprint 51 pages). All read.
- `W\evidence\retained_angle_20260905\`: `MATHEMATICAL_AUDIT.md` (18.6 KB, ten sections; a careful
  second-agent audit of `h24:ret:main`, with the full frame `D(a,b) G_0`,
  `D(a,b) = diag(e^{-i(a+b)}, e^{ia}, e^{ib}) in SU(3)`, the explicit contraction, the spin quadratic form
  `q(xe+yf) = x + xy + y`, the smoothing-order repair, and the remark that sphere recognition is used
  exactly to pass from the chart framing to `pi_6(S^4)`), `verify_retained_angle_frame.py` +
  `RETAINED_ANGLE_EXACT_CHECKS.json` (12 sympy checks), receipts. All read.

#### 1.10 `W\research\mathematical_summary.tex` — grep and read l.268-292, 1672-1700, 1760-1780, 1940-2050, 2256-2282, 3700-3732
Summarises the above with the same statuses; nothing additional. `literature_log.tex` l.480-520 repeats
the two smash-null arguments.

#### 1.11 Baselines consulted
- [E26] Remark 8.3 (`literature\engel_S6.txt` l.1208-1247).
- [AC26] `original_clean_transcription.tex` l.111 (summary page): the formula
  `pi_1 = Z/|12 l_0 - 4 l_1 - 3 l_2|` "admits a reading, which the body does not use": it is Orlik's
  formula for `H_1` of the Seifert space over `S^2(3,4)`, and "heuristically the twist condition says: glue
  so that the coinvariant circle of the fibres traces out the (3,4) Seifert fibration of the three-sphere
  over the base". So the map `S^6 -> S^3` of Engel's Remark 8.3 is already foreshadowed in [AC26] as a
  heuristic; neither source constructs it with proof.

---

---

### Reader F: Cusp spectral geometry, gauge and quaternionic lanes, root-level drafts (workbench)

Full notes: `work\F_notes.md`.


#### 1.1 Cusp spectral and gauge files

**`W\cusp_spectral_geometry.tex`** (50 KB, 1390 lines; section "Flat spectral geometry on the positive radial
cusp", label `cusp-spec-section`). Read in full except lines 947–957, which `\input` five other modules
(`cusp_globalization_replacement`, `cusp_toric_cover_completion`, `cusp_cone_sphere_routes`,
`cusp_sphere_route_strengthening`, `cusp_s12_carrier_homotopy`, `cusp_sphere_fixed_metric`) that are not in
this assignment.
- Setup (1–86): period matrix Π = [Z | I_2], Z = [[6μ, τ],[β, μ]]; cusp identity Z = s·[[0,1],[−1,0]] +
  [[6μ, h],[b−h, μ]], b = β+τ, s = τ−h, e^{2πis} = t_c; radial ray t_c = e^{−2πT}, s = iT. Real quantities
  L_T = T+H_T = Im τ, q_T = L_T − B_T = −Im β, m_T = Im μ, D_T = L_T q_T + 6 m_T²; limits H = Im h(0),
  B = Im b(0), m = Im μ(0). Line 83–86: "The metric in this section is, by definition, the quotient of
  dx_1²+dy_1²+dx_2²+dy_2² ... the complex period construction itself neither requires nor singles out this
  Euclidean metric."
- Prop. `cusp-spec-exact-dual-lattice` (88): P_T (4×4), det P_T = −D_T, covolume D_T = −L_T·D_can, full
  P_T^{−T}, dual lattice, spectrum λ_T(k) = 4π²(n_1²+n_2² + [(m R + q S)² + (−L R + 6m S)²]/D²).
  Ledger S6-CUSP-SPEC-DUAL, VERIFIED.
- Thm `cusp-spec-shortest-modes` (254): shortest dual vectors are ±ℓ_γ, ±ℓ_u with |ℓ_γ|² = (L²+m²)/D²,
  |ℓ_u|² = (q²+36m²)/D²; λ_1 = (4π²/T²)(1 + (−2H + 2 min{B,0})/T + O(T^{−2})). Ledger S6-CUSP-SPEC-GAPS.
- Cor. `cusp-spec-unit-volume` (410): Vol = D_T = T² + (2H−B)T + H(H−B) + 6m² + O(T e^{−2πT}); unit-volume
  metric has λ_1 = (4π²/T)(1 + (−H − B/2 + 2 min{B,0})/T + …).
- Prop. `cusp-spec-counting` (476): N_T(E) = π D_T Σ_{n∈Z²}(E/4π² − |n|²)_+ + O_E(T+1); first band
  N_T(E) = E D_T/(4π) + O_E(T); unit-volume count E D_T^{1/2}/(4π) + O(D_T^{1/4}); count at the collapsing
  scale = #{(r,s): r²+s² ≤ E}. Ledger S6-CUSP-FIXED-ENERGY-COUNT.
- Thm `cusp-spec-pointed-limits` (645): (F_T, o) → T² × R² (pointed, balls eventually isometric); sys = 1,
  inj = 1/2; covers by Λ_{T,M} = ⟨v_γ, v_u, M e_1, M e_3⟩ of degree M² → R⁴ iff M → ∞ (unit-volume pullback:
  iff M/√T → ∞). Ledger S6-CUSP-SPEC-COVERS, S6-CUSP-FINITE-COVER-R4-AUXILIARY.
- Prop. `cusp-spec-native-quotient` (866): 0 → T²_re → F_T → Q_T = R²/Y_T Z² → 0, det Y_T = D_T,
  sys(Q_T) ≥ T − C.
- Subsection "The exceptional first-coordinate elliptic quotient" (959–1176): Prop.
  `cusp-spec-first-coordinate-descent` (988), Thm `cusp-spec-elliptic-descent-finiteness` (1073), Remark
  `cusp-spec-elliptic-descent-scope` (1165). Ledger S6-CUSP-FIRST-ELLIPTIC-QUOTIENT. See F-2, F-3.
- Thm `cusp-spec-cover-momentum-theorem` (1178): M_0 = I + R, R² = 0, ker R = im R = ⟨ŵ, δ̂⟩;
  S_M^{−1} M_0^M S_M = M_0; cover spectrum and momentum-mesh bound C(1/T + 1/M).
- "Scope and residual data" (1350–1390): metric is declared; B is a free additive constant of the construction
  (see Doubts 3.2); covers are local at the cusp.

**`W\cusp_spectral_interpretation.tex`** (13 KB, 332 lines). Read in full. Thm
`cusp-interpretation-direct-integral-gapless` (63): the multiplication operator ⊕_k λ_k(T) on
L²([T_0,∞); L²_0(T⁴)) is self-adjoint, injective, 0 ∈ σ_ess (Weyl sequence 1_{[n,n+1]} e_{k_0}); ledger
S6-CUSP-AUX-THRESHOLD. Prop. `cusp-interpretation-fixed-complex-counterexample` (145): on (C/Z[i])² the flat
Kähler metrics R²|dz_1|² + R^{−2}|dz_2|² have volume one and λ_1 = 4π²/R² → 0, so complex data do not select
a gap. Prop. `cusp-interpretation-typed-physical-transfer` (211): an abstract Rayleigh-quotient transfer lemma.
Audit record (315): auxiliary gaplessness VERIFIED, conclusion about the 4d quantum Yang–Mills Hamiltonian
OPEN (= ledger S6-OPEN-YM-PHYSICAL-BRIDGE).

**`W\cusp_spectral_preprint_radial_bridge.tex`** (5 KB). Notation bridge for the standalone preprint (there
R = logarithmic height, T = Im τ). One proposition restating the dual lattice. Nothing new.

**`W\cusp_gauge_operators.tex`** (35 KB, 954 lines). Statements read, proofs not. Hessian of YM at the product
connection on F_T is g^{−2} d*d; Coulomb-reduced first eigenvalue γ_T = (4π²/g²) min{|ℓ_γ|², |ℓ_u|²}
(Thm `cusp-gauge-continuum-gap`, 706), multiplicity 6 d_G #I_T; finite cubical cochain model with gap
ρ_N/(g² T²)(1+…), ρ_N = 4N² sin²(π/N), uniformly in the mesh N ≥ 2 (Thm `cusp-gauge-finite-gap-limits`, 407).
Subsection "The physical boundary and the exact no-gap bridge" (756–954) lists five reasons why this is not a
quantum statement. Ledger S6-CUSP-GAUGE-CLASSICAL.

**`W\cusp_su2_magnetic.tex`** (36 KB, 1066 lines; twin `cusp_su2_magnetic_preprint.tex`). Statements read.
Integral coframe θ^j = du_j, θ¹∧θ² = D_T^{−1} dy_1∧dy_2 (Prop. 31); unit-flux line bundle L_T with
c_1 = [γ∧u]; E_T = L_T ⊕ L_T^{−1} smoothly SU(2)-trivial (Prop. `cusp-magnetic-su2-triviality`, 143);
Thm `cusp-magnetic-ym-critical-point` (273); Thm `cusp-magnetic-oscillator-theorem` (425): for every
nondegenerate integral alternating form E the magnetic Laplacian has spectrum {(2n_1+1)b_1+(2n_2+1)b_2};
Cor. `cusp-magnetic-frequency-product` (541): b_1 b_2 = 4π² |Pf E|/D_T, gap ≤ 4π √(|Pf E|/D_T);
Thm `cusp-magnetic-negative-mode` (787). Ledger S6-CUSP-MAGNETIC-SPECTRUM, S6-CUSP-FULL-TORUS-MAGNETIC-GAP,
S6-CUSP-SU2-UNSTABLE. See F-5.

**`W\cusp_native_full_flux_magnetic.tex`** (39 KB, 1047 lines; twin `_preprint`). Lines 1–300, 425–660,
846–1047 read. The invariant class η = u∧w + 6γ∧δ (checked against T_1, T_2 at lines 74–92), E_η with
SNF diag(1,1,6,6), Pf = 6; explicit cocycle and connection; ½η² = +6 in the marking orientation and −6 in the
complex orientation; frequencies B_± = π(Ξ_T ± S_T)/D_T, S_T = 6L_T − q_T, Ξ_T = √((6L_T+q_T)² + 144 m_T²),
B_+B_− = 24π²/D_T; Thm `cusp-native-full-flux-landau-theorem` (433); Cor.
`cusp-native-full-flux-heat-count` (522); split SU(2) connection (576–646); Thm
`cusp-native-full-flux-Morse-theorem` (926). See F-4.

**`W\cusp_native_full_flux_radial.tex`** (21 KB; twin `_preprint`). Thm `native-di-main-theorem` (394): the
direct integral over T of the full-flux magnetic Laplacians has purely continuous spectrum [0,∞), no
eigenvalues. Remark (615): "No radial derivative and no interacting Yang–Mills claim".

**`W\cusp_native_full_flux_suN.tex`** (28 KB; twin `_preprint`). Split-Cartan SU(r) version: action
(π² s_2(m)/g²)(37 + 35B/T + …), negative bands q_ij((2n+1)B_min − B_max), multiplicities 12 q_ij², nullities,
stability boundary S_T = 0; closing remark (lines 660–686): a bundle with c_2 ≠ 0 on a fibre cannot extend
over a space with H⁴ = 0.

**`W\cusp_compact_link_gaussian.tex`** (32 KB; twin `_preprint`; standalone
`R\s6_compact_link_gaussian_preprint.tex`, 98 KB, is the same material with the cover-spectrum, magnetic
saddle and coercive-bridge sections of the other modules added). Cubulation of the degree-M² cover torus,
holonomy map to SU(2)^E, an explicit periodic link configuration with plaquette exp(2π H/N²), finite Hessian
spectrum λ(k) = g^{−2}|P_T^{−T} S_M^{−1} d_N(k)|², Gaussian oscillator with gap √λ_min, diagonal sequence
T_j = j², M_j = j, N_j = j³ on which the gap → 0 (Thm `cusp-link-gaussian-theorem`, 624); Prop.
`cusp-link-exponential-local-only` (754). Ledger S6-CUSP-COMPACT-LINK-FLUX, S6-CUSP-FINITE-GAUSSIAN.

**Preprint twins.** `cusp_compact_link_gaussian_preprint.tex`, `cusp_native_full_flux_magnetic_preprint.tex`,
`cusp_native_full_flux_radial_preprint.tex`, `cusp_native_full_flux_suN_preprint.tex`,
`cusp_su2_magnetic_preprint.tex`: confirmed by size and by `diff` (header says "Standalone-preprint adaptation
of …; the canonical radial-height symbol T was renamed R consistently", with the SHA-256 of the source).
Skipped.

**`R\s6_spectral_degeneration_preprint.tex`** (118 KB, 2645 lines; title "Cusp Spectral Degeneration and Local
Toric Kummer Extension. Conditional results from the reconstructed candidate S⁶ complex-torus fibration",
"Revised conditional specialist-verification draft, 4 September 2026"). Abstract, statement list, §5 opening
(1016–1075), 2255–2300 read. It is the standalone view of the cusp modules above plus two modules outside this
assignment: Thm `thm:global-real-quotient` (1030; the unique primitive monodromy-invariant character ε_γ,
real circle quotient of the regular family with circumference −T D/√(T²+m²); ledger S6-CUSP-FOUR-COPY-R4; this
is the object of [E26] Remark 8.3) and the local toric Kummer morphism (§6; ledger S6-CUSP-KUMMER-COMPLETION).
In this preprint T = Im τ, so H does not appear. Prop. `prop:total-space` (2279) records that the compact
total space with any smooth metric has a positive gap and that the Euclidean fibre metrics are not shown to be
restrictions of a metric on X. Remark at 2263 "Correction of an ambient-family argument" withdraws an earlier
argument that used the path (τ,μ,β) = (i/T, 0, −iT), which is not on the period image.

#### 1.2 Quaternionic block

**`W\quaternionic_4441_reconciliation.tex`** (251 KB, 5840 lines; section "The common marked slice and its
dynamics", label `sec:q444-reconciliation`; wrapper `R\s6_quaternionic_4441_reconciliation.tex`, 7.6 KB, is
title + abstract + `\input`). Lines 1–400, 521–665, 1105–1200, 1364–1545, 1626–1700, 1801–1830, 1926–1975,
2113–2400, 2489–2510, 3972–4070, 4448–4472, 5742–5840 read; elsewhere statements only (58 statements).
Source of the model (lines 4–13, 5744–5752): two GPT "Pro-mode packets" dated 4 Sep 2026, "Triality 4-4-4-1
Dynamic Completion" and "Quaternionic 4441 Continuation". The workbench audits and extends them. Contents:
- 35–341: conventions; Moore determinant; Lemma `q444:pair-cubic` N(Θ(A,b)) = det A − b*Ab; marking
  P = [[1,−1,0],[0,1,−1]], u = (1,1,1)^t, C = PP* (the A_2 Cartan matrix), X = (R u); Thm
  `q444:identification` (144); Prop. `q444:cubics`; Prop. `q444:positive`; Prop. `q444:pair-topology`
  ((S¹², S⁸)); Thm `q444:jordan` (308).
- 343–520: group action convention; positive observation O(H) = π_C(PHP*) (ledger S6-Q444-POSITIVE-OBSERVATION).
- 521–1625: the period bridge: Prop. `q444:period-gram` (541), Thm `q444:metric-fibre` (627), rank-loss
  propositions (823, 901), Thm `q444:hermitian-cometric` (1162), Thm (1252) lattice cometric = character
  spectrum, Thm `q444:metric-submersion` (1364), Prop. `q444:native-period-spectrum` (1491).
- 1626–2110: scalar mechanics L = ½ tr Φ̇² + ḃ*ḃ − V, V = m² s/2 + Γ s²/4 − κ(det Φ − b*Φb): Thm `q444:force`
  (1644), Prop. `q444:constrained`, Lemma `q444:global`, Thm `q444:invariant-W` (1801), Prop.
  `q444:fourth-jet` (1879), Thm `q444:moving-family` (1932), Prop. `q444:charge`.
- 2113–2324: Lemma `q444:sharp` (54 n² ≤ s³), Thm `q444:vacua` (2175), Thm `q444:vacuum-hessian` (2234).
- 2325–3970: gauge lift with SU(3): sign of the gauge kinetic term corrected; all homogeneous field equations;
  Thm `q444:temporal-no-lift` (2489); Gauss inertia; no real-connection lift (2795); a real radial family of
  full solutions (2988); vacuum kinetics; exact periodic continuation (3485); null waves (3585); all eight
  gauge-inertia eigenvalues (3754); invariant current.
- 3972–5740: the "rotating ansatz" finite system in su(3)³ (five equations, displayed at 3993–4004): block
  exclusion (4148), Gauss inverse and residual zero set (4539), signature constraint (4744), stress matrix,
  finite coupling fibre (5396; a degree-28 polynomial p_Z), generic exclusion via a 24×24 Sylvester determinant
  (5606).
- 5742–5840: sources and checkers (evidence folders `quaternionic_4441_audit_20260904`,
  `finite_coupling_20260905`, `scalar_gauss_domain_20260905`).
- Scope sentence at 2358–2364: "No result here identifies these cone-boundary spheres with the claimed
  integrable complex structure on S⁶, assigns new spinor periods and toroidal fillings, or proves a continuum
  interacting Yang–Mills spectral gap."

**`W\two_cross_exceptional_shared.tex`** (33 KB). Thm `q444:twocross:thm:exclusion` (64): the five-equation
system has no solution with Z_1, Z_2 ∈ p (the 4-real-dimensional "cross" part of su(3) relative to the matter
line), for any t = g² > 0 and ω ≠ 0. Prop. (475): the class lies in the exceptional set of the generic
exclusion theorem. Prop. (590): a polynomial residual certificate with a strict lower bound. Ledger
Q444-TWO-CROSS-EXCLUSION, -RESIDUAL-CERTIFICATE.

**`W\scalar_gauss_domain_shared.tex`** (36 KB). Thm `sgd:parametrization` (208): the solutions of the two
scalar equations and Gauss (no spatial equation) in the classified frame are in bijection with
D × {±1}² × U(1)², D = {(u,v_0,y): u>0, d = u v_0 − δ² − y² > 0, c = 4v_0 − 5u > 0}, δ = √(2/3), t = 72 d/c.
Thm `sgd:literal-addon:quotient` (647): the literal set S_sg = (D × {±1}² × U(1)² × U(1))/⟨ι⟩. Cor.
`sgd:every-coupling` (862): nonempty for every t. Ledger Q444-TWO-CROSS-SCALAR-GAUSS-*.

**`W\scalar_gauss_smooth_shared.tex`** (25 KB). Thm `sgd:smooth-addon:literal-diffeomorphism` (250), Thm
`sgd:smooth-addon:coupling` (415), Cor. `sgd:smooth-addon:levels` (535): S_sg is an embedded 6-manifold
≅ {±1}² × (0,∞) × R² × T³ with t the (0,∞) coordinate. Ledger Q444-SCALAR-GAUSS-SMOOTH-LITERAL-PRODUCT.

#### 1.3 Other workbench modules

**`W\worldline_presymplectic_reduction.tex`** (35 KB, 991 lines; wrapper
`R\s6_worldline_presymplectic_reduction_preprint.tex`). Lines 1–190, 321–350, 720–760 read. Model:
x ∈ Herm_2(C) (Minkowski space with ⟨A,A⟩_L = det A), Z ∈ Mat_{3×2}(C), p = α Z*Z, action
∫⟨p, ẋ⟩ − (e/2)(det p − m_0²c²), left SU(3) "colour". Thm `wpr:thm:quotient` (143), Thm `wpr:thm:massive`
(321), Lemma `wpr:lem:irregular` (488), Thm `wpr:thm:massless` (519), Thm `wpr:thm:zero` (645), Thm
`wpr:thm:verdict` (720), Thm `wpr:thm:packet-action` (893). Ledger S6-WPR-*. Cites Dirac 1950,
Gotay–Nester–Hinds 1978, Marsden–Weinstein 1974 for the framework.

**`W\hermitian_normal_slice_physics.tex`** (54 KB, 1299 lines). Lines 1–60, 132–160, 528–612, 1124–1146,
1220–1299 read, other statements by head. Thm `hnsp-lorentz-theorem` (132): ½ D²(det)_{uu*} on the normal
slice {X ∈ Herm_3(C): Xu = 0} ≅ Herm_2(C) is the Minkowski form; spin action (234); a gauge–scalar model on
the slice (421); Prop. `hnsp-candidate-spacelike` (538): G_{η,T} = [[2L_T, 2m_T],[2m_T, −q_T/3]] has
det = −(2/3) D_T < 0; free-field and regulator spectra (759, 861); obstruction propositions (1126, 1147);
Thm `hnsp-coercive-transfer` (1220); "Exact conclusion" (1270).

**`W\homogeneous_quantum_confinement.tex`** (80 KB, 1841 lines; wrapper
`R\s6_homogeneous_quantum_confinement.tex`). Lines 1–84, 847–870, 946–965, 1072–1125, 1232–1257 read. The
38-coordinate SU(3) matrix quantum mechanics (three gauge matrices, adjoint scalar, triplet): Thm
`qh:full-compact` (847), Thm `qh:hq-positive` (946), Cor. `qh:hq-ground` (1072), Prop. `qh:hq-embedding`
(1099); second section (1232–1841): Born–Oppenheimer comparison for a two-Fourier-coordinate truncation. Line
17–22 attributes the discreteness mechanism to the literature. Ledger S6-Q444-HOMOGENEOUS-QUANTUM-*,
S6-Q444-MOVING-FOURIER-QUANTUM-COMPARISON.

**`W\ym_bulk_plaquette_extension.tex`** (39 KB, 1093 lines; "Mechanically generated from the complete audited
BULK_PLAQUETTE_EXTENSION.md", 8 Sep 2026). Lines 1–75, 990–1093 read. SU(2) Kogut–Susskind Hamiltonian
H = −κ Σ Δ_e + b Σ(2 − W_p) on the open box {−L..L}³; second-order strong-coupling (ξ = b/κ) improvement of a
Rayleigh quotient: R_ret − R_corr = (1951/81675) b²/κ + O_L(b³/κ²). No S6 input at all.

**`W\z6_defect_center_bridge.tex`** (22 KB, 657 lines). Read in full except the proofs of the two group
theorems. Thm `zdc:thm:fibre-degree` (178), Prop. `zdc:prop:finite-reductions` (356), Thm
`zdc:thm:tensor-centres` (461), Thm `zdc:thm:common-centre` (535), boundary (642). See F-7.

#### 1.4 Root-level drafts (title, opening, statement heads only)

All are the Yang–Mills programme; they later moved to the public repository (the clone has
`repo\yang-mills\…` and files such as `spatial_continuum_127p.tex`). The common object is the SU(2)
Kogut–Susskind Hamiltonian H = κ Σ_e E_e + b Σ_p (2 − W_p), κ = 2g²/a, b = 1/(2g²a), ξ = b/κ = 1/(4g⁴), on
the open cubic box {−L,…,L}³ with all links and plaquettes. The only datum taken from X is one number, the
plaquette angle θ = 2π a²/D with D = L_T q_T + 6 m_T² (stated in
`s6_volume_uniform_local_vacuum_draft.tex` §1), that is, the unit-flux cusp bundle of
`cusp_su2_magnetic.tex` put on a lattice.

- `s6_adjacent_plaquette_quantum_draft.tex` (21 KB, 8 Sep): two plaquettes sharing a link, seven links; a
  nonzero second-order elimination correction; it `\input`s `ym_bulk_plaquette_extension.tex`. "not a
  four-dimensional continuum mass-gap result".
- `s6_wilson_temporal_transfer_draft.tex` (29 KB, 8 Sep): exact single-link character multiplier of the SU(2)
  Wilson transfer operator; strong limit to the Hamiltonian on a finite spatial lattice (Thm
  `thm:multiplier`, `thm:stronglimit`). A known type of statement, made explicit.
- `s6_interacting_wilson_variation_draft.tex` (39 KB, 8 Sep): Fierz identities, ground-state transform, centre
  symmetry selection rules, all-coupling finite-volume bounds for vacuum-weighted Wilson loops (8 statements).
- `s6_spatial_vacuum_elimination_draft.tex` (35 KB, 8 Sep): conditional projection in the true lattice vacuum,
  Schur-complement form, temporal memory kernel, improved trial vectors (5 statements). Attributes the
  Feshbach–Schur method to the literature.
- `s6_retained_cusp_nonlinear_draft.tex` (33 KB, 8 Sep): the full 6×6 two-form metric of the cover torus
  (G^{−1} from P_M) and the nonlinear Wilson action in it. "does not claim a quantum mass-gap counterexample".
- `s6_extensive_quantum_blocking_draft.tex` (91 KB, 8 Sep): blocking of the full box in the true vacuum,
  Schur memory, associativity of repeated blocking, a "gap transfer" theorem (14 statements). Opens with a
  correction notice listing superseded "Fabel" notes.
- `s6_magnetic_translation_quantum_draft.tex` (318 KB, 8 Sep, 11 parts): the cusp magnetic background as a
  translation operator on the Wilson Hilbert space; first excitation band of the open box; centre-disorder
  endpoint; spectral leakage polynomials.
- `s6_weak_coupling_physical_draft.tex` (344 KB, 8 Sep, 18 parts): fixed-box weak-coupling limit of physical
  eigenvalues (maximal-tree gauge), a "radial carrier" representation, first two coupling coefficients; Part 18
  "Non-Abelian fluid encoding". Reader scope says the Gamma representation "does not reconstruct local
  interacting Yang–Mills theory".
- `s6_spatial_continuum_draft.tex` (415 KB, 8 Sep, 28 sections, 88 statements): simultaneous cusp/refinement
  sequences; §9 a volume-uniform gap at strong coupling, (H − E)|_{ψ^⊥} ≥ (3κ/4)(1 − 512 ξ/3) for
  0 < ξ ≤ 1/49152, by the method of Yarotsky (arXiv:math-ph/0411042) with explicit constants; §27 a
  "regulator-level obstruction" to a perturbative route; §28 conclusion: "proves neither a continuum mass gap
  nor its absence".
- `s6_volume_uniform_local_vacuum_draft.tex` (312 KB, 9 Sep, 26+ sections): volume-independent local estimates
  in the full vacuum (local electric moments, cluster coordinates, decay of electric covariance).
- `s6_xi4_heat_transport_draft.tex` (18 KB wrapper, 8 Sep; `\input`s 12 files from
  `supporting_materials\workbench\evidence\ym_sidebar_topics_20260908\xi4_heat_transport\tex\`). Title "The
  heat generator on the retained inverse-fibre cover". The abstract combines the de Bruijn–Newman heat flow,
  a Connes quotient, a polynomial map of Tao, a Navier–Stokes source and a fourth-order lattice coefficient;
  it includes `s6_three_point_quotient.tex` (a real three-torus quotient built from the three special points;
  it records μ(z_1) = (2−ρ)/3, μ(z_2) = (1−i)/2, ρ = e^{πi/3}) and `s6_three_point_forcing.tex` (a "forced
  fluid" built from it). See Doubts 3.6.

---

---

### Reader D1: Niemeier, Leech, triality, Erdos-Straus bridge (workbench)

Full notes: `work\D1_notes.md`.


All files carry filesystem date 2026-09-29 00:32 (copy date). Internal dates: 5–6 Sep 2026. Status marks are the
workbench's own.

#### R\es_niemeier_shared.tex (79,366 bytes, 1,878 lines; "Shared mathematical module", 5–6 Sep 2026)
Root of the lane; inputs the next six files and then `common_d4_image.tex`, `niemeier_umbral_shadow.tex`
(l. 1870–1878). Labels have prefix `esn:`. An older copy (77,230 bytes, differs from l. 10 on: older intro) is in
`E\es_niemeier_20260905\`; the receipts there hash the older copy.
- l. 7–43 intro (summary of all results of the lane).
- esn:thm:cyclic-fibre (l. 65–106): β = (Legendre mod 5, mod 7): V_840 → F_2^2 onto, fibres of 6,
  S_840 = <289>, κ: S_840 ≅ Z/6.
- esn:thm:root-discriminant (l. 154–235): R_ES = A_5^4 ⊥ D_4, det = 6^4·4 = 5184, discriminant form
  (5/6)Σx_i^2 + 1_{y≠0} mod 2.
- esn:thm:niemeier (l. 264–380): glue H = {(3u+2z; y)}, C_2 = <(1111;00),(1100;10),(1010;01)>,
  C_3 = <(1,1,1,0),(1,2,0,1)> (the tetracode); |H| = 72, N even unimodular, 46 nonzero classes of minimum 4 and 25
  of minimum 6 (table l. 351–364), roots exactly A_5^4 D_4 (144). Transporter to the earlier glue l. 388–416.
- esn:thm:d4-f4-triality (l. 440–533): W(F_4) = W(D_4) ⋊ S_3 with section <R_D, H_D> (reflections in ε_1 and in
  c = (−1,1,1,1)/2); v,s,c ↔ weights of V_8, S^+, S^−. Mare–Willems paragraph l. 535–607.
- esn:thm:glue-gl2 (l. 682–736): stabilizer G of H among (signs, S_4, GL_2(F_2)) is ≅ GL_2(F_3) via
  ℓ_i A = ε_i ℓ_{p(i)}, ℓ = ((1,1),(1,2),(1,0),(0,1)). esn:thm:triality-q8 (l. 756–845): split sequence
  1 → Q_8 → GL_2(F_3) → GL_2(F_2) → 1. esn:thm:gl2-full-lattice-lift (l. 855–921): faithful action L_g on N.
- ES part: esn:thm:shell-bijection (l. 976–1035), esn:thm:raw-channels (l. 1054–1132, with the correction of the
  source's wording, l. 1128–1132), esn:thm:non-descent (l. 1137–1222), esn:thm:residue-cocycle (l. 1237–1278),
  esn:thm:sample-fourier (l. 1298–1366).
- Full automorphism group: esn:fa:thm:a5-automorphisms (l. 1402–1515), esn:fa:thm:d4-automorphisms
  (l. 1517–1614), esn:fa:thm:full-quotient (l. 1616–1813): O(N) = W(R_ES) ⋊ L(G), |O(N)| = 48·(6!)^4·192;
  esn:fa:thm:residue-weyl (l. 1815–1868): ρ(S_840) ⊂ W, commutes with L(G), C_6 × GL_2(F_3) of order 288.
Ledger: ESN-RESIDUE-NIEMEIER-LATTICE, ESN-FULL-WEYL-QUOTIENT, ESN-EXACT-SHELL-COUNT-PUSHFORWARD (all VERIFIED;
claim_ledger.txt l. 127–129), morphism ledger M-ESN-RESIDUE-WEYL-COCYCLE, M-ESN-SHELL-AND-SAMPLE.

#### R\es_niemeier_leech.tex (19,469 bytes, 532 lines; 6 Sep 2026; prefix `esnl:`, tags NL1–NL20)
- NL1–NL3 (l. 28–90): ρ = ρ_A^{⊕4} ⊥ ρ_D, ρ_A = (5,3,1,−1,−3,−5)/2, ρ_D = (3,2,1,0), ρ^2 = 84, glue class
  (3,3,3,3;00); K = ker((ρ,·) mod 6), v = ρ/6 − α, Λ = K + Zv.
- esnl:thm:leech-neighbor (l. 94–245): Λ even unimodular, minimum 4; hand proof of rootlessness by a table of
  shifted coset minima (NL4) and a congruence on (ρ,x).
- NL8–NL11 (l. 247–328): identification with the Conway–Sloane holy construction (credited; Borcherds 1985).
- esnl:thm:cyclic-twelve (l. 348–381): Λ/R_0 ≅ Z/12 ⊕ (Z/6)^2, R_0 = R ∩ K, class of v of order 12.
- NL15–16 (l. 383–405): N + Λ = K^∨, K^∨/K ≅ (Z/6)^2 with form q = ab/3.
- NL17–18 (l. 407–450): Lorentzian picture, w = (ρ, 6, 7) in N ⊥ U.
- esnl:thm:f4-coxeter-twelve (l. 468–525): explicit F_4 Coxeter element C of order 12 on the D_4 space,
  1 → <C^3> ≅ Z/4 → <C> → Z/3 → 1.
Ledger: NIEMEIER-LEECH-EXACT-NEIGHBOR-20260906 (VERIFIED; l. 134).

#### R\es_niemeier_triality_bridge.tex (18,369 bytes, 426 lines; prefix `n24:`; header "Staged only")
- n24:thm:full-isometry (l. 50–119): the isometry 𝓛: V_N → O^3 (even/odd triplets of each A_5 block to the three
  sectors; mean differences and D_4 coordinates to the diagonal), 𝓛 r = c 𝓛 for r = ρ(361), c the cyclic shift.
- l. 121–153 glue test in octonion coordinates; l. 155–222 Albert determinant
  det(λI + E(𝓛X)) = λ^3 − λ(X,X) + 2 t_N(X), tr(E∘E) = 2(X,X).
- l. 224–241 "Dependence": the map depends on the origins f_i, on 289, on the even/odd order, on the order of b
  and on the octonion basis; "no claim of independence".
- l. 243–321 the Leech neighbour transported to O^3; l. 323–426 glue symmetry, character computation showing
  the triality section <R̂, Ĥ> (7·1 ⊕ 5·sgn ⊕ 6·Std) is not conjugate to the frame S_3 on O^3
  (1 ⊕ 7·sgn ⊕ 8·Std); connected Spin(8) cannot preserve the lattice.

#### R\es_niemeier_cubic_arithmetic.tex (23,513 bytes, 588 lines; prefix `nca:`)
- nca:thm:polynomial (l. 114–184): F = P_0 + √2 P_2 + √3 P_3, no √6 term.
- generators g_1..g_29 of N, h_1..h_30 of Λ (l. 186–238).
- nca:thm:finite-values (l. 251–298): the additive group generated by all values of a cubic on a finitely
  generated lattice is generated by F(b_i), F(b_i ± b_j) − ..., and the triple polarizations (4495 / 4960 items).
- Cayley–Dickson frame fixed (l. 300–320). nca:thm:value-modules (l. 322–437):
  V_F(N) = (1/27)Z ⊕ (√2/54)Z ⊕ (√3/18)Z, V_F(Λ) = (1/27)Z ⊕ (√2/216)Z ⊕ (√3/54)Z, quotient Z/4 ⊕ Z/3.
- l. 439–490 frame dependence, with an explicit orthonormal frame change that produces the value −√15/3.
- l. 492–588 which lattice symmetries preserve F (only the order-3 subgroup of the residue group; R̂, Ĥ and a
  root reflection do not), F(ρ) = 15√2 + 16√3, F(v) = 14/27 − 7√2/24 − √3/27.

#### R\es_niemeier_residue_fixed_neighbor.tex (26,840 bytes, 782 lines; prefix `esrf:`, tags RF1–RF45)
- esrf:thm:equality (l. 49–97): Λ_σ = Λ_τ iff K_σ = K_τ iff τ ≡ ±σ mod 6N, for σ, τ in the orbit Ω = O(N)ρ.
- esrf:thm:no-fixed-neighbor (l. 113–178): r = ρ(361) fixes no Λ_σ (obstruction: no tetracode word of weight 4).
- RF9–RF19 (l. 185–311): q_1, q_2, β: N → F_3, I = ker(ℓ_0, β) of index 18, J = I + Z·3v, det J = 81.
- esrf:thm:common-J (l. 313–346): Λ_0∩Λ_1 = Λ_1∩Λ_2 = Λ_2∩Λ_0 = J, [Λ_j : J] = 9.
- esrf:thm:discriminant-correspondence (l. 363–529): J^∨/J ≅ F_3^4, q_J = (2/3)(2ad + bc + bd), the three
  Leech lattices are the planes P_0, P_1, P_2; matrix of r.
- esrf:thm:fourth-extension (l. 546–782): the r-fixed plane P_∞ gives M, even unimodular, 72 roots, A_2^12,
  [M : R_M] = 3^6; M ∩ N = L_0 of index 6 in both.

#### R\es_niemeier_JM_cubic_extension.tex (13,819 bytes, 328 lines; prefix `jmv:`)
jmv:thm:IJM-generators (l. 69–104), jmv:thm:JM-values (l. 108–202): V_F(J) = V_F(M) =
(1/27)Z ⊕ (√2/216)Z ⊕ (√3/18)Z; jmv:thm:chain (l. 215–271): V_F(N) ⊂ V_F(J) = V_F(M) ⊂ V_F(Λ) with quotients
Z/4, Z/3. Ledger JM-CUBIC-VALUE-GROUPS-20260906 (VERIFIED). Evidence in
`E\period_lattice_continuation_20260906\jm_cubic\` (not opened; outside my list).

#### R\es_niemeier_wilson_cyclic.tex (35,241 bytes, 883 lines; prefix `wcl:`)
Wilson's octonionic Leech lattice (L = E_8 = D_8 + Zs, pair sums in L s̄, total in L s, norm (1/2)ΣN) rebuilt
with explicit matrices: wcl:lem:e8 (l. 93–135), wcl:lem:complementary (l. 169–192), wcl:thm:Leech (l. 246–286),
wcl:thm:fixed-coinvariant (l. 319–374: fixed lattice Gram 3G_{E8}, coinvariant ≅ A_2 ⊗ E_8), glue sequence and
explicit anti-isometry (l. 376–432), a subgroup A_4 × (C_7 ⋊ C_3) of order 252 preserving lattice and cubic
(l. 434–489), the maps r_t do not preserve the cubic (l. 491–548), wcl:lem:quaternion-intersection
(l. 618–640), wcl:thm:literal-intersection (l. 688–783): Λ_cyc ∩ 𝓛(N) = Λ_cyc ∩ 𝓛(Λ) = {√2(a,a,a): a ∈ D_4},
Gram 6G_{D4}; cubic on it (l. 815–856). Ledger WILSON-CYCLIC-INTERSECTION-20260906 (VERIFIED).

#### R\common_d4_image.tex (15,562 bytes, 443 lines; prefix `d4i:`, tags D4I1–D4I35)
d4i:thm:complete-image (l. 123–172): P(a) = a_0(a_0^2 − 3(a_1^2+a_2^2+a_3^2)) on D_4 has image
18Z ∪ (6Z+2) ∪ (6Z−2), with an explicit section by three affine lines; d4i:thm:local-images (l. 247–320);
factorization on the sum-zero slice P = 2(3w+u+v)(u^2 − uv + v^2) (l. 322–443).

#### R\niemeier_umbral_shadow.tex (28,148 bytes, 706 lines; prefix `nus:`)
Specialization of Cheng–Duncan–Harvey to X = A_5^4 D_4: Ω^X = 5 I_12 + J (l. 93–123), M^X (l. 134–149), theta
transformation and intertwiner (l. 151–229), quadratic similitude Z/12 → Z/6 with multiplier 10 (l. 231–259),
determinant character (l. 261–367), residue Fourier map and twisted shadows from the class functions
(a_g, b_g, s_g, c_g) on GL_2(F_3) (l. 369–553), T_6 = η(τ)^5 η(3τ)/(η(2τ) η(6τ)^5), f^X = −q d/dq log T_6 =
5λ_6 + λ_2 − λ_3, T_6(W_6 τ) = 72/T_6, f^X|W_6 = −f^X, J_6 = T_6 + 5 + 72/T_6 (l. 555–684). Scope statement
l. 686–697: "They do not construct a new graded moonshine module or a new moonshine theorem."

#### R\p1201_selector_jordan_bridge.tex (11,685 bytes, 322 lines) = E\p1201_selector_jordan_bridge_20260905\fifteen_selector_jordan_bridge.tex (identical up to a final blank line)
The 15 marked ES selector states at p = 1201 (table l. 50–73) mapped to rank-one points of Sym_2(R) ⊂ Herm_3(H);
thm:fifteen-span (l. 194–219): span and Jordan closure have dimension 3, not 15; counts 15, 54, 36, 29 at
p = 1201, 4561, 8761, 9601 (l. 224–231). `REPORT.md` (16,745 bytes) is the long form of the same; `LOGBOOK.md`
not read in full.

#### R\erdos_straus_selector_crosswalk.tex (10,829 bytes, 322 lines; marks \Verified)
prop:es-first-half-denominator (l. 13–52), prop:es-two-channel-selector (l. 67–148),
thm:es-s6-selector-terminal-bijection (l. 191–241). Ledger S6-ES-SELECTOR-CROSSWALK (VERIFIED, l. 72).
Superseded in content by the next file, which repeats and extends it.

#### R\erdos_straus_koide_s6_bridge.tex (37,172 bytes, 1,031 lines)
Longer version: lem:esksb-first-half, prop:esksb-shell-bijection, prop:esksb-two-channel,
prop:esksb-reconstruct, thm:esksb-bridge (l. 394–466), corollary (3.8)–(3.11), (3.12)–(3.14) affine coordinates,
lem:esksb-factors and prop:esksb-factor-congruence (l. 599–655), counterexample criterion (4.5) (l. 657–684),
examples on forgetting labels, thm:esksb-affine-gate (l. 814–875), descendant maps (7.1)–(7.7) (l. 882–985),
"Sharp verdict" (l. 987–1031). Despite the name there is no Koide content in this file beyond the title.

#### R\ES_NIEMEIER_PROVENANCE.md (15,668 bytes; identical copy in E\es_niemeier_20260905\)
Sources: CDH Table 3; Mare–Willems; the April 2026 residual note; the "Foundation transport theorem"
(thm:exact-support-glue-Fricke-transport; the origin of T_6 and of "the original scalar 72"); excerpt of the
source's two-channel theorem whose wording is corrected; SHA-256 of snapshots.

#### R\es_niemeier_bibliography.tex (3,028 bytes)
CDH 2014; Mare–Willems 2013; the two ES corpus items; Conway–Sloane 1982 "Twenty-three constructions";
Borcherds 1985; Wilson 2009.

#### ..\WEB_PRO_TRIALITY_LEECH_FEEDBACK_20260906.md (7,856 bytes)
A handoff text to GPT (Pro mode), not feedback received: restates the lattice results and sets "a bounded next
calculation" (the image set of the cubic on the common D_4 slice), which `common_d4_image.tex` then answers.

#### Evidence folders (reports and outputs only)
- `E\es_niemeier_20260905\`: EXACT_CHECKS.json (PASS; glue minima 46/25, order-48 stabilizer, shell counts
  2521/3361), receipts, four checker scripts.
- `E\triality_leech_20260906\`: README (lists two corrections made during review: only the GL_2(F_3) complement
  centralizes the residue action; C v_D = c_D + (1,−1,0,0)), checker outputs.
- `E\lattice_foundation_20260906\`: `cubic\`, `neighbours\`, `wilson\`, `canonical_ring\` each with
  EXACT_CHECKS.json. `neighbours\EXACT_CHECKS.json` records det J = 81, det(Λ_i+Λ_j) = 1/81, and lists only the
  three Leech planes plus the fourth plane.
- `E\spectral_umbral_period_20260906\`: README, five checkers with logs (common D_4 image, shadow, shift
  matrices, orbit scalar identities, common-lattice spectral map).
- `E\p1201_selector_jordan_bridge_20260905\`: REPORT.md, verification_output.txt.

#### My own exact checks (results)
- `lat.py`: det R_ES = 5184, index 72, N even unimodular with roots A_5^4 D_4 (144); glue minima {4: 46, 6: 25};
  det K = 36; Λ even unimodular with no vector of norm 2 (so Λ is the Leech lattice); Λ_0, Λ_1, Λ_2 pairwise
  distinct, det(Λ_i + Λ_j) = 1/81; det I = 324, det J = 81, J ⊂ all three, rJ = J; M even unimodular, rM = M,
  72 roots, A_2^12; isotropy of classes in J^∨/J agrees with formula (RF24).
  **New in my check:** J^∨/J has exactly 8 totally isotropic planes; the 8 even unimodular overlattices of J are
  **six Leech lattices and two Niemeier lattices A_2^12**. The workbench has one ruling (Λ_0, Λ_1, Λ_2, M); the
  other ruling consists of three more rootless lattices (permuted by r) and a second r-stable A_2^12, namely
  M' = J + Zu_* + Z r u_* = the 2-neighbour of N along ρ/2.
- `nb.py`: the d-neighbours of N along the Weyl vector for d | 6: d = 2 gives A_2^12, d = 3 gives A_1^24,
  d = 6 gives Leech.
- `snf.py`: Λ/R_0 has invariants (6, 6, 12); the class of v has order 12; det(N+Λ) = 1/36.
- `cubic.py`: independent implementation of 𝓛, the Cayley–Dickson product and F; F(α), F(v), F(p), F(q) agree
  with the files; V_F(N), V_F(Λ), V_F(J) = V_F(M) and the quotients Z/4, Z/3, Z/12 are reproduced exactly.
  Choice test: see D1-5.
- `es.py`: A_3(2521) = 0, A_3(3361) = 6, both primes ≡ 1 mod 840, the unit-fraction identity for 3361; census
  (#E, #M, #unordered) = (7,8,11), (26,28,40), (16,20,26), (17,12,23) at p = 1201, 4561, 8761, 9601; 2521 has
  12 selector states on other shells; affine-gate theorem (6.6) has no violation for m < 400; P(D_4) residues
  mod 18 are {0,2,4,8,10,14,16}; P = 6 is not attained; T_6(τ)T_6(−1/(6τ)) = 72 numerically.

---

### Reader D2: Koide arithmetic (workbench)

Full notes: `work\D2_notes.md`.


All files dated 29 Sep 2026 00:32 on disk (snapshot copy time); internal dates 3–4 Sep 2026.

#### 1.1 `W\research\koide_period_discriminant.tex` (6.7 KB, 201 lines)
Subsection "The Koide cone and the canonical period discriminant", label `koide-s6-subsection-ambient-discriminant`.
Input by `SNAP\workbench.tex` line 1629.
- Defines Q_K (eq. koide-s6-eq-koide-form), orthogonal matrix 𝓕 with rows (1,1,1)/√3, (1,0,−1)/√2, (1,−2,1)/√6,
  the period convention Z = (6μ τ; β μ), the 4×4 real matrix P(τ,μ,β), and S(t,m,ϱ) = (t √6m; √6m ϱ).
- **Theorem koide-s6-thm-ambient-discriminant** ("Ambient coefficient-space discriminant isomorphism"):
  Q_K = h² − x² − y²; 𝒦(h,x,y) = (h+y, x/√6, h−y); det P = det S = tϱ − 6m²; det P(𝒦𝓕 r) = Q_K(r); on the nonnegative
  Koide cone S is positive semidefinite of rank one. Proof: 20 lines of linear algebra. Correct.
- **Cor. koide-s6-cor-ambient-only**: the identification is ambient only; on the Koide cone det P = 0, no torus.
- **Cor. koide-s6-cor-actual-cusp**: det P_T = −D_T < 0, D_T = T² + (2H−B)T + O(1), citing `cusp-spec-determinant`,
  `cusp-spec-D-expansion` (in `cusp_spectral_geometry.tex`, another reader's file).
- Ledger: S6-KOIDE-AMBIENT-DISCRIMINANT, VERIFIED; uncertainties.txt U-KOIDE-CUSP-RELATION, VERIFIED.

#### 1.2 `W\research\koide_counting_repair.tex` (41 KB, 1159 lines)
Section "Exact arithmetic of the Koide defect-one shell", label `koide-count-sec-main`. Input by `workbench.tex`
line 1631 and by the root preprint. Its last four lines input the parametrization, census, quaternion and
literature files. "Repair": the source packet compared counts with X/(9π) (field `max_z_over_9pi` in the stored
JSON); the workbench replaced that by a proved constant. First sentence: the section "does not use the existence of
the proposed complex structure on S^6, any period-map assertion, or any Yang–Mills interpretation".
- §Vieta (`koide-count-subsec-vieta`): Δ = 3Q_K (eq. defect-qk); Gram matrix A_K = (−1 2 2; 2 −1 2; 2 2 −1),
  signature (1,2); **Prop. vieta-reflections** (s_i are the reflections in e_i, B_K(e_i,e_i) = −1);
  **Prop. vieta-reduction** (0<x≤y≤z, Δ=−1: if z < 4(x+y) then 0 < z' < y, z' = 4(x+y) − z);
  reduced set 𝓡 = {0<x≤y≤z, Δ=−1, z ≥ 4(x+y)}, R(X) = #{𝓡, z ≤ X} (eq. rx-definition);
  **Prop. vieta-forest** (positive solutions form a rooted forest; roots = 𝓡);
  **Thm coordinate-bijection** (Φ: 𝓡 → 𝓣 = {a>0, q≥0, n≥0, a+4n>q, a²−3q²−18n² = −2}, inverse
  ((a+4n−q)/2, (a+4n+q)/2, 4a+17n); 2Δ = a²−3q²−18n²);
  **Prop. pell-faces** (n=0 face: a_k+q_k√3 = (1+√3)(2+√3)^k, k ≥ 1; q=0 face: A_k+N_k√18 = (4+√18)(17+4√18)^k,
  k ≥ 0; each O(log X) points).
- §local (`koide-count-subsec-local`): F = a²−3q²−18n², 𝒳 = {F = −2}; **Thm local-densities**: σ_2 = 3/2, σ_3 = 2,
  σ_p = (1−p^{-2})/(1−(3/p)p^{-1}) for p ≥ 5; 𝔖 = (9/2)·L(1,χ_12)/ζ(2) = (9/2)·log(2+√3)/(√3 ζ(2)).
- §archimedean: gauge form ω_∞ = dq∧dn/(2a); **Thm archimedean-factor**: m_∞{𝒳(R)∩𝒞, 4a+17n ≤ X} ~ I_∞ X,
  I_∞ = (1/(2√3))·log(3/(2√2)).
- §gos: **Lemma genuine-norm** (‖(a,q,n)‖_* = max{|4a+17n|,|q|,|a|} equals the height on the chamber);
  **Lemma gos-hypotheses** (Spin(F), x_0 = (1,1,0), stabilizer = norm-one torus of Q(√3), no Q-characters; the cone
  is admissible and generic for Gorodnik–Oh–Shah 2009 Thm 1.6).
- §borovoi: **Prop. finite-sign-balance**: Borovoi's coefficient c_𝒳 = 1, by the explicit g = r_v r_e ∈ SO(F, Z_2)
  (v = (1,0,1), e = (1,0,0)), spinor norm −17, (−17,3)_2 = −1.
- §calibration: **Thm linear-asymptotic**: R(X) ~ C_0 X, C_0 = 𝔖·I_∞ = (9/(2π²))·log(2+√3)·log(3/(2√2))
  = 0.035362047799731853…
- §computation: first roots (1,4,20), (4,4,33), (4,8,49), (4,15,76), (8,24,129); table X = 10^4 … 2·10^5;
  **Open problem `koide-count-open-square-root-discrepancy`** (R(X) − C_0X = O(X^{1/2+ε})?), marked OPEN.
- Status in ledger: S6-KOIDE-DEFECT-COUNTING, VERIFIED (one entry covering this file and the parametrization file).

#### 1.3 `W\research\koide_exact_parametrization.tex` (45 KB, 1186 lines)
"Integrated 4 September 2026"; labels `koide-param-*`. Sections: arithmetic of Z[√3]; HNF parameters; complete
integral parametrization; divisor and sharp-height formulas; phase term as Hecke-character data; unconditional
effective exponent; exact obstruction to the square-root claim; boundary ledger.
- Lemma ring-units (h = 1, units ±ε^j, ε = 2+√3, no unit of norm −1); Lemma ideal-number (#ideals of norm m =
  ρ(m) = Σ_{d|m} χ_12(d)); **Prop. HNF-ideals** ((C,D,E) with C²D = m, 0 ≤ E < D, E² ≡ 3 (D) ↦ C(DZ + (E+√3)Z) is a
  bijection onto ideals of norm m); m_n = 18n² − 2; Lemma positive-norm-generator; **Lemma integral-seed-descent**
  (seed condition a > 2q ≥ 0; descent (a,q) ↦ (2a−3q, 2q−a)); **Thm integral-parametrization** ((n, 𝔭, k) ↦
  α_{n,𝔭} ε^k is a bijection onto solutions with a>0, q≥0, n≥1; multiplicity one); Prop. n-zero;
  **Prop. orbit-divisor** (number of unit orbits at fixed n is ρ(m_n) = ρ(3n−1)ρ(3n+1));
  **Thm exact-floor** (R(X) = R_0(X) + Σ_{n∈𝒩(X)} Σ_𝔭 (⌊L_n(X) − τ_{n,𝔭}⌋ + 1));
  eq. exact-discrepancy-splitting (R − C_0X = R_0 + [Σ ρ(m_n)L_n(X) − C_0X] + Σ Δ_n(λ_n(X)));
  Hecke characters ξ_ℓ, S_ℓ(m) = Σ_{N𝔞=m} ξ_ℓ(𝔞), S_ℓ(18n²−2) = (−1)^ℓ S_ℓ(3n−1)S_ℓ(3n+1) (eq.
  shifted-Hecke-factorization), Fejér identity (eq. Fejer-exact, exact-shifted-Hecke-correlation).
- **Lemma volume** (m_∞(B_X) = I_∞X + O(1); B_X is effectively well-rounded in the sense of Benoist–Oh Def. 13.1);
  **Thm power-saving**: R(X) = C_0X + O(X^{1−η}) for some unspecified η > 0 (Benoist–Oh 2012 Thm 13.2 applied to
  each of the finitely many integral orbits).
- "Exact obstruction": two descriptions; says explicitly that 2/3 is not claimed for R(X).
- Replay script `W\evidence\koide_exact_checkpoint_20260904\parametrization\verify_parametrization.py`
  (1 ≤ n ≤ 200, exact integers).

#### 1.4 `W\research\koide_exact_census.tex` (7.8 KB, 203 lines)
Section `koide-count-sec-census-1e8`. **R(10^8) = 3,536,002**; n_max = 2,943,725; 2,327,513 unit orbits;
checkpoint table 2·10^5 … 10^8; max E = +721.79 at X = 77,078,404; min E = −812.83 at X = 32,461,294;
max |E|/√X on [10^4,10^8] = 0.171400 at X = 867,240 (root (a,q,n) = (199997,115061,3956));
12,916 sign changes; 2,472,015 occupied heights; max multiplicity 35 at z = 92,923,120; largest gap 564.
Ledger S6-KOIDE-CENSUS-1E8, VERIFIED. Evidence: `W\evidence\koide_exact_checkpoint_20260904\census\`
(`koide_fast_enum.py` 40 KB: SPF sieve, HNF triples, Lagrange–Mollin–Matthews continued fraction for a generator,
seed descent, unit orbit; `METHOD_AND_RESULTS.md` 21 KB; `FINAL_RECEIPT.json`; `validate_fast_enum.py`;
`audit_coordinate_file.py`; `final_100000000\` with the 76 MB coordinate file, not opened).

#### 1.5 `W\research\koide_quaternion_bridge.tex` (29 KB, 822 lines)
Section `koide-quat-exact-quaternion-bridge-order-shell-and-hyperbolic-conjugacy-classes`; converted from a
Markdown report (headings `koide-quat-*`; no theorem environments, boxed formulas).
- B = (18,−6)_Q, K = IJ, K² = 108; order 𝒪 = Z ⊕ Z(I+J)/2 ⊕ Z(I−J)/2 ⊕ Z K/2 with multiplication table
  (eq. multiplication-table); nrd(r+sE+tF_0+uG) = r² − 3s² − 12st − 3t² − 27u²; reduced discriminant 108, index 18
  in a maximal order, not Eichler; Ram(B) = {2,3}, disc 6.
- Shell bijection (eq. shell-bijection): (a,q,n) with F = −2 ↔ γ = 2 + (qI + aJ + nK)/2, trd γ = 4, nrd γ = 1;
  γ² − 4γ + 1 = 0; 𝒪 ∩ Q(γ) = Z[γ−2] ≅ Z[√3]; C_Γ(γ) = {±γ^k}; every γ primitive hyperbolic of length
  2 log(2+√3); finitely many Γ-classes (h not computed); class decomposition of R(X) (eq. koide-class-count);
  "radial Huber parameter" X_i(γ)² = 1 + (7a + 15√2 n)²/48 for the base point i of one chosen splitting.
- Conclusion: places the problem "beside" the conjugacy-class lattice-point problem (Huber; Good Thm 4;
  Chatzakos–Petridis 2016, O(X^{2/3}), Conj. 5.7 O(X^{1/2+ε})) and lists nine missing items.
- Ledger S6-KOIDE-QUATERNION-BRIDGE, VERIFIED. Replay `…\quaternion\verify_quaternion_bridge.py` (48 shell points in
  a box, Hilbert symbols; log PASS).

#### 1.6 `W\research\koide_effective_literature_audit.tex` (57 KB, 844 lines)
Section `koide-lit-…`, dated 4 Sep 2026. Determination (`koide-lit-determination`): no listed theorem gives the
square-root bound; strongest exact-domain result is the Benoist–Oh power saving. Result matrix (18 rows: DRS 1993,
Eskin–McMullen 1993, GOS 2009/2010, Benoist–Oh 2012, Gorodnik–Nevo 2012, Liu–Sarnak 2010, Good 1983 /
Chatzakos–Petridis 2016, Bourgain–Kontorovich–Sarnak 2010, Browning–Gorodnik 2017, Cao–Huang 2022,
Cao–Huang–Zhang arXiv:2509.23320, Oh–Shah 2014, Xu–Zhang 2023, Huang arXiv:2412.03350 and 2412.05903, Zhang
arXiv:2603.21080, Li–Liu arXiv:2501.15033, Voskou arXiv:2407.03134, Lekkas–Petridis arXiv:2509.12902). Detailed
subsections: Benoist–Oh applicability (hypotheses, Def. 13.1 check, finite-orbit passage, why η is unspecified:
η = δκ/(p+κ)); Good/Chatzakos–Petridis; "current sharp refinements remain at 2/3"; BKS; Liu–Sarnak (smooth radial
O(T^{1/2+θ+ε}), θ = 7/64 gives 39/64; claims Prop. 3.2 applies class by class to Γ = 𝒪^1 because Γ is congruence:
Kim–Sarnak + Jacquet–Langlands, Chu–Li λ_1 ≥ 975/4096); Gorodnik–Nevo explicit exponents 19/20 and 39/40;
taxonomy table; citation-ready conclusion; 28 references with locators; limitations (Good's book not consulted
directly; no local copies of sources).

#### 1.7 `W\research\koide_es_v3_audit.tex` (15 KB, 351 lines)
Section `sec:esv3-audit`, 4 Sep 2026: audit of a Pro-mode packet "Divisor Channels, Prime Saturation, and Bézout
Openings, v3" (Erdős–Straus / Koide). Input by `workbench.tex` line 1606. Mostly Erdős–Straus, only its last two
subsections touch the Koide surface.
- Prop. esv3-channel: bijection (δ,u,v) ↔ ordered solutions of 4/n = 1/a + 1/y + 1/z for n ≡ 1 (4), R ≡ 3 (4),
  a = (n+R)/4, with δ | n², uv = a², R | 4u+δ; corrects an orientation reversal in the packet.
- Integral presentation R_δ = (3 −ℓ_1; 4 −T), 12ℓ_0 − 4ℓ_1 − 3ℓ_2 = δ, SNF diag(1,δ); "gluing admissibility
  3 ∤ ℓ_1 fails exactly when 3 | δ".
- Prop. esv3-diagonal, esv3-density: for primes p ≡ 1 (4) the "diagonal" solutions 4/p = 1/x + 1/(xk) + 1/(pxk),
  x = (p+R)/4, k = (p+1)/R, R | (p+1)/2, R ≡ 3 (4); count ν(p) = ½(τ(m) − Σ_{d|m}χ_4(d)), m = (p+1)/2; density one
  (classical; cites Elsholtz–Tao 2013).
- Bézout opening: A = δvv^T − ww^T, det A = −δ; **REFUTED** packet claim "A_11 > 0 for every real δ > 0"
  (counterexample (r,t,δ) = (2,1,1/8)); a torus with det P_A = −δ is constructed but "does not determine a point on
  the global period curve".
- "Original map's rational nonintersection": the orthogonal map 𝔎_δ sends no rational A to a rational triple.
- Lemma esv3-anisotropic (Δ anisotropic over Q); **Thm esv3-rational-bridge**: stereographic projection from
  (1,0,0) gives an isomorphism of open subsets of {ac − b² = −δ} and {Δ = −1} over Q, with denominator formula.
- Evidence `W\evidence\koide_es_v3_audit_20260904\` (AUDIT_AND_PRO_FEEDBACK.md, CLAIMS.json with ESV3-* ids,
  verify_independent.py, source\ packet with a 58 KB TeX, not read).

#### 1.8 `SNAP\koide_arithmetic_preprint.tex` (18 KB, 411 lines) and its PDF (877 KB)
"The Koide Quadratic Cone as a Lorentzian Determinant — Vieta dynamics and a ternary defect-one counting problem",
"Specialist-verification draft, 4 September 2026", no author. A root file: §1 restates the Koide form
(Thm orthogonal-model; Cor. exact-phase-sector: r_i = (h/√3)(1 + √2 cos(θ − θ_i)), nonnegativity arcs
[π/12, π/4] ∪ [3π/4, 11π/12] ∪ [17π/12, 19π/12], endpoint ratio 2±√3; Prop. S6-dictionary = the ambient
discriminant theorem; Cor. rank-one-square; Cor. ambient-only; Remark on the radial cusp), then
`\input{…koide_counting_repair}` (which pulls in everything else), then "Interpretation and limits". It is a view of
the same sources; the only content not in 1.1–1.6 is the phase-sector corollary and the angle π/4 remark (both
elementary and known: Koide's relation as a 45° angle with (1,1,1) is in the Koide literature; cites Kocik 2012).
Abstract still says "a recent proposed complex-torus construction on S^6" (the caution of early September).

#### 1.9 Ledger entries (`W\research\ledgers\claim_ledger.txt`)
Line 9 S6-OPEN-KOIDE-SQRT-DISCREPANCY (OPEN); line 67 S6-KOIDE-AMBIENT-DISCRIMINANT; line 68
S6-KOIDE-DEFECT-COUNTING; line 69 S6-KOIDE-CENSUS-1E8; line 70 S6-KOIDE-QUATERNION-BRIDGE (all VERIFIED, each with a
"nonclaim" field saying the arithmetic is independent of S6). `uncertainties.txt` lines 34–35: U-KOIDE-CUSP-RELATION
(VERIFIED), U-KOIDE-SQRT-DISCREPANCY (OPEN). `research_log.tex`: Round 28 (audit of "T1 Koide arithmetic",
normalization still open), Round 29 (3 Sep, normalization closed), Round 37 (4 Sep: parametrization, quaternion
bridge, exponent, census).

#### 1.10 `W\reproduction\t1_koide_exact\`
README.md (provenance: copied byte-for-byte from the Pro packet zip, SHA given), `verify_koide_narain_root_density.py`
(13 KB; (n,a) scan with numpy square detection and exact recheck), `koide_verification_200000.json` (R(200000) =
7109; contains the packet's comparison with max_z/(9π)).

#### 1.11 Related files not in my assignment (seen, not read)
`SNAP\s6_erdos_straus_koide_bridge_preprint.tex`, `SNAP\s6_koide_es_divisor_extension_audit.tex`,
`W\research\erdos_straus_koide_s6_bridge.tex`, `erdos_straus_selector_crosswalk.tex` (the Erdős–Straus lane).

---

---

### Reader E: Higher-rung continuation (workbench)

Full notes: `work\E_notes.md`.


#### 1.1 `W\higher_rung_24d_continuation.tex` (303,964 bytes, 7,376 lines) — "mechanically generated from s6_higher_rung_24d_preprint.tex"
Label prefix `h24:`. Read in full: l.1-1445 (source data, obstructions, toroidal successor, sphere ladder),
l.6134-6200 and the bibliography. All theorem-like statements read (extracted by script) for l.1445-4376,
5112-5750, 6187-7199; proofs there only sampled. l.4376-5112 and 5752-6134 are reader C1's block (C1-3, C1-7),
not reread. l.6184-7199 ("ES-NIEMEIER HOST-ONLY INPUT": Albert orbit quotient, Cartan family, spectral map of
the common lattice) belongs to reader D1's topic; statements listed only.

Sections and main labelled statements:
- l.30-180 source data: monodromies `T_1,T_2` (eq. `h24:eq:original-T`), period matrix, twists
  `(l_0,l_1,l_2) = (0,1,-1)`; matrices `P, R, C, X_P` (`h24:eq:marked-P`); Definition `h24:def:feature-ledger`
  (F1)-(F8) "full higher toroidal wrap" (what a literal analogue would have to supply); the required diagram
  `h24:eq:required-diagram` (0 -> K_Z -> Lambda~ -> Lambda -> 0 over periods).
- l.181-334 "Sphere and Euler obstructions": Thm `h24:thm:s8-obstruction` (no almost complex structure on a
  homotopy `S^8`, signature proof), Thm `h24:thm:all-higher-spheres` (none on homotopy `S^m`, `m > 6`; Bott
  integrality / Borel-Serre), Prop `h24:prop:euler-mismatch` (`chi(W_3) = 6`, so the three-fibre pattern gives
  `chi = 6`), Cor `h24:cor:euler-repair` (an `S^8` carrier needs other fibres with Euler sum `-4`), a remark.
- l.335-774 "The exact toroidal successor over the cusp": Thm `h24:thm:lattice-quotient`
  (`Phi = P (+) Q: Z^6 ->> Z^4`, kernel `Z(k,0) (+) Z(0,k)`, `Phi M_3 = M_F Phi`, `c_F Phi = Q c_3`);
  Thm `h24:thm:elliptic-extension` (`Z_3 = s I_3 + S C_2(t) Q`, `P Z_3 = Z_2 Q`, kernel `E_s = C/(Z + sZ)`);
  Prop `h24:prop:toric-filling-map` (Kuhn fan -> `A_2` fan, quotients `N_3^C -> N_0`, proper discontinuity);
  Lemma `h24:lem:cusp-basis-identification` (`M_3 ~ M_F (+) C_0` over `SL_6(Z)`);
  Prop `h24:prop:finite-lift` (`A~_j = A_j (+) C_j`, free affine lifts); Remark "Exact endpoint" (l.762-773):
  global gluing not constructed.
- l.775-1404 "The forced S^9, S^10 and rank-loss S^8": Thm `h24:thm:orbit-invariants`, Lemma `h24:lem:K3-ball`,
  Thm `h24:thm:sphere-ladder`, Props `h24:prop:U3-ball`, `h24:prop:S9-join`,
  `h24:prop:spectral-floor-observation`, Cor `h24:cor:residual-circle`, Thm `h24:thm:O9-fibres`,
  Prop `h24:prop:Gram-square`, Cor `h24:cor:S9-cusp-limit`, Thm `h24:thm:strongest-gram`. Same mathematics as
  `higher_rung_su3_triple_s8_cone.tex` (1.8).
- l.1406-3576 "The 24-dimensional octonionic flag": Thms `h24:thm:octonionic-triality`,
  `h24:thm:octonionic-cohomology` (both attributed to Mare-Willems 2013), Prop `h24:prop:two-Coxeter-systems`,
  Thm `h24:thm:Kuhn-octonionic-comparison` (bijection of two 6-element `S_3`-sets), Prop
  `h24:prop:complex-flag-embedding`, Thm `h24:thm:octonionic-determinant-S24`, Props `h24:att:prop:peirce`,
  `:norm-inverse`, `:determinant`, Thm `h24:att:thm:stabilizer`, Prop `h24:att:prop:linear-stabilizer`,
  Thm `h24:tri:thm:spectral-graph`, Lemmas `h24:fc:cartan-inverse`, `h24:fc:finite-exponential`,
  Thm `h24:fc:open-cell`, Prop `h24:fc:orientation`, Thm `h24:fc:collapse`, Cors `h24:fc:boundary-composite`,
  `h24:fc:no-reverse-degree`, Prop `h24:prop:three-24d-objects`.
- l.3577-4375 "What the mod-12 and mod-24 arithmetic actually is": Thm `h24:thm:peripheral-moduli`, Props
  `h24:prop:cusp-diagonal-modulus`, `h24:prop:no-modulus-from-cohomology-or-determinant`, Thm
  `h24:thm:stable-12-to-24`, Prop `h24:prop:generator-free-bridge`, Thm `h24:thm:cusp-g-zero` (the one-copy cusp
  map is null; reader C1's C1-4), Cor l.4347.
- l.4376-6137 block `RETAINED_ANGLE_AND_HOPF_BRIDGE_20260905` (C1), inside it l.5112-5750
  `h24:rettri:*`: Thm `h24:rettri:bundleclass`, Thm `h24:rettri:subgroup`, Prop `h24:rettri:forgetting`.
- l.6139-6182 Thm `h24:thm:exact-numerical-boundary` (summary of the numerology tests).
- l.6184-7199 host-only Albert/Cartan/common-lattice block (labels `h24:ocb:*`, `h24:ncs:*`).
- l.7201-7376 bibliography.

Status marks: the file itself has none; `W\status.tex` l.2731-2810 marks the toroidal successor "Verified" and
"the global period-and-overlap gluing over both finite-order discs remains Open"; l.3025 marks the literal
complex `S^8` "Refuted".

#### 1.2 `R\s6_higher_rung_24d_preprint.tex` (301,399 bytes, 7,471 lines; dated "6 September 2026")
Title "Retained cusp topology, triality morphisms, and the marked Niemeier-Leech construction"; "Standalone
theorem note for the higher-rung search". Same text as 1.1: equal counts of theorem (25) and proposition (22)
environments, the same section sequence with the preprint's line number = continuation line + 93 (30 -> 123,
4378 -> 4471, 6134 -> 6227); sections are one level higher and labels have no `h24:` prefix. It has in addition
a title and a long abstract (l.36-121) which is mostly about the lattice results (reader D1). Not read twice.

#### 1.3 `W\higher_rung_fourfold_toric_degeneration.tex` (38,239 bytes, 1,063 lines) — read in full
Label prefix `hrftd:`. Sections: baseline of the threefold cusp; rank-three periodic fan (Lemma
`hrftd:lemma:unimodular`, Prop `hrftd:prop:four-branch`: `t = z_0 z_1 z_2 z_3`); analytic quotient (Thm
`hrftd:thm:toroidal-cusp`); monodromy (Prop `hrftd:prop:cusp-monodromy`: `pi_1(N_3) = Z^3`); central fibre
(Thm `hrftd:thm:strata`, Thm `hrftd:thm:normalization`, Remark, Cor `hrftd:cor:euler-shear-determinant`);
obstructions (Thm `hrftd:thm:euler-obstruction`, Thm `hrftd:thm:no-almost-complex-s8`); a diagonal monodromy
candidate and Prop `hrftd:prop:finite-fixed-points`; "replication requirements" (Prop `hrftd:prop:van-kampen`,
Thm `hrftd:thm:mv-criterion`, Wang sequence); Hermitian boundary (Prop `hrftd:prop:hermitian-compactification`,
Thm `hrftd:thm:hermitian-not-snc`); conclusion.

#### 1.4 `W\higher_rung_toroidal_elliptic_bridge.tex` (36,927 bytes, 1,105 lines) — read in full
Labels `teb-*`, equations (TEB.1)-(TEB.55). Prop `prop:teb-fan-morphism`, Thm `thm:teb-local-lattice-bridge`,
Thm `thm:teb-holomorphic-cusp-bridge`, Prop `prop:teb-explicit-conjugacy`, Prop
`prop:teb-finite-monodromy-lift`, Prop `prop:teb-weyl-chambers`, Thm
`thm:teb-hermitian-determinant-splitting`, Prop `prop:teb-theta-order-lift`, an audit record (3 Sep 2026),
Thm `thm:teb-no-gram-identification`, and "The remaining global problem" (l.1057-1105). This is the earlier,
fuller source of 1.1 l.335-774 (same matrices, same proofs).

#### 1.5 `W\higher_rung_s8_constraints.tex` (29,222 bytes, 715 lines; header date 2026-09-03) — read in full
Label prefix `hrs8:`. No theorem environments; boxed statements. Subsections: no almost complex structure on a
homotopy `S^8` (three arguments); requirements for a real `T^6`-fibration `S^8 -> S^2`; Euler constraint;
`pi_1` and monodromy; Mayer-Vietoris / Wang / Serre tests; torus-rank bound and `S^8/T^4 = B^4`; Gram quotient
with boundary `S^8`; `SU(3)` bundles on the regular locus `U = X \ (W u S_1 u S_2)`; consequences; sources.

#### 1.6 `W\higher_rung_rank_six_lattice.tex` (14,630 bytes, 355 lines) — read in full
Prefix `rsl:`. Thm `rsl:thm:s3-sequence`, Thm `rsl:thm:three-sixes`, Prop `rsl:prop:gram-scope`, audit record.

#### 1.7 `W\higher_rung_rank_nine_matrix_torsor.tex` (15,420 bytes, 409 lines) — read in full
Prefix `rnmt:`. Thm `rnmt:thm:regular-torsor`, Thm `rnmt:thm:pair-kuhn-weyl`, Prop
`rnmt:prop:marking-boundary`, Prop `rnmt:prop:representation-bridge`, audit record.

#### 1.8 `W\higher_rung_su3_gram_cone.tex` (25,251 bytes, 708 lines) and `W\higher_rung_su3_triple_s8_cone.tex` (24,855 bytes, 885 lines)
Statements read in full, proofs sampled. Gram cone (2 columns): Thm `thm:hrgc-gram-quotient`, Prop
`prop:hrgc-stabilizers`, Thm `thm:hrgc-free-trivialization`, Prop `prop:hrgc-pluecker`, Thm
`thm:hrgc-s12-ball-quotient`, Thm `thm:hrgc-no-native-s4-sector`. Triple cone (3 columns): Thm
`thm:hr3c-u3-gram-classification`, Lemma `lem:hr3c-density-ball`, Cor `cor:hr3c-u3-unit-quotient`, Thm
`thm:hr3c-u3-compactification`, Thm `thm:hr3c-su3-invariants`, Thm `thm:hr3c-su-unit-sphere`, Thm
`thm:hr3c-su-full-cone`, Prop `prop:hr3c-rank-strata`, Thm `thm:hr3c-rank-loss-pair`, Cor
`cor:hr3c-residual-circle`, Thm `thm:hr3c-two-ladders`. The first file states at its head that it "isolates
the part ... that is independent of the candidate complex threefold".

#### 1.9 `W\higher_rung_lorentz_observation_bridge.tex` (31,339 bytes, 927 lines)
Prefix `hlob:`. Statements read in full; l.674-927 read in full. Lemma `hlob:lem:splitting-identities`, Thm
`hlob:thm:split-observation`, Thm `hlob:thm:block-coordinates`, Thm `hlob:thm:lorentz-action`, Thm
`hlob:thm:cone-section`, Cor `hlob:cor:Y3-block-form`, subsection "holomorphic toric seed", Thm
`hlob:thm:colour-momentum`, a worldline action.

#### 1.10 Evidence folders (reports only)
- `EV\higher_rung_24d_20260905\`: `MATHEMATICAL_LEDGER.md` (table of what is proved; ends "A completed global
  higher torus wrap remains open"), `AUDIT_OCTONIONIC_LOG.md` (an independent audit of the flag block; found two
  defects of statement, since repaired: the tangent space needs `d Xi_lambda`; restricted roots are
  `gamma_i/2`), `LITERATURE_LOCATOR_CORRECTION.md`, `WORKLOG.md` (contains the user's request: an analogue of
  the S6 object "on S8 or S9", and the "24-dimensional mod 24 or mod 12" idea), build receipts.
- `EV\exact_lorentz_observation_bridge_audit_20260904\`: `README.md`, `AUDIT_REPORT.md`, `CLAIM_LEDGER.md`
  (C01-C32). Verdict: C01-C22, C24-C26, C31 proved; C23 (the displayed first-order action as dynamics) and C32
  (global completion) REFUTED; C27 (a pointwise map from the toroidal total space to the phase-retaining
  carrier), C28 (the global analytic elliptic overlap cocycle through the finite fillings), C29, part of C30
  OPEN. "No packet theorem is novel relative to the current canonical tree."

#### 1.11 Other places consulted
`W\status.tex` l.2655-3064 (the result map for this block; statuses quoted above); `claim_ledger_index.txt`
(the higher-rung toroidal statements have no ledger ids of their own; the Gram/Lorentz side appears as
S6-WPR-*, S6-Q444-*); Engel's text (section 1.2, 2, Remark 8.5); `C1_notes.md` (C1-3, C1-7).
No file in `W\` contains the word "conifold"; Engel's Remark 8.5 is not taken up anywhere in this block.

---

---

### Reader G1a: Course CG-S6, lessons 1-6, 8, 9

Full notes: `work\G1a_notes.md`.


#### 1.0 Course metadata
- `CG\README.md` (11.6 KB, 11 Oct 2026). Describes the 11 lessons and 47 companions; "Current authoring provenance: GPT-6 Astra
  (OpenAI), Codex, Ultra, 9 October 2026. Independent review is not claimed." Says 46 lesson solutions, 68 companion solutions.
- `CG\course.json` (69 KB, 11 Oct): schema open-mathematics-course/v1; status `complete_written_series_author_self_checked`;
  `independent_whole_course_review: false`; 11 units; 84 result ids. Result ids for my lessons: CG-S6-01-{PERIOD, LATTICE, COVER,
  SURFACE, LINE, FORMS}; -02-{DECK, KERNEL, INTEGRAL}; -03-{PERIODS, COVARIANCE, FILLING, BRANCHES, CONJUGACY}; -04-{TAU, MU, BETA,
  RANGE, QUOTIENT, CONTRACTION, CUBIC}; -05-{CHARTS, ACTION, PROPER, FIBRE, CANONICAL, OVERLAP, GLOBAL, SECTION, RESOLUTION, HEIGHT,
  TRANSLATION, LIFT, ITERATES}; -06-{MATRICES, EXTERIOR, GLUING, MIDDLE, FINITE, CUSP, GROUP, DICTIONARY, EXTENSIONS};
  -08-{FUNCTIONS, CHARACTERS, HODGE, CANONICAL, DIRECT, RING, FIBRATION, EXERCISES}; -09-{FAMILY, BELTRAMI, FIBRE-KS, GLOBAL-KS,
  CENTRALIZER, FINITE, GLOBAL-MAPS, CLASSIFICATION, EXERCISES}. Every one has status
  `complete_written_proof_with_author_self_check`. Unit status: `writing_ai_self_checked`, `independent_review: false`.
- `CG\series.json` (26 KB): lesson list with proof scopes and antecedents (e.g. lesson 1: FF1-FF22, FF42-FF46, Engel section 3);
  note "boundary_repair_20261009": the line-bundle and cubic comparison is in lesson 4, the resolved fibres and lift extension in
  lesson 5. Skimmed.
- `CG\provenance.json` (80 KB): source identities and hashes; skimmed only (structure).
- `CG\CG-S6-0N.html` and the other `.html`: rendered readers of `src\*.md`; not read (same content).

#### 1.1 `CG\src\finite-quotients-and-line-bundles.md` (lesson 1; 23.3 KB, 417 lines; 8 Oct 2026)
Sections: 1 period map (real isomorphism iff Im tau > 0, D != 0); 2 Prop 2.1 (fixed and image lattices of A_1, A_2: Lambda^{A_1} =
Z eps + Z delta^, (A_1 - I)Lambda = Z e_1 + Z f_1, index 3; same at j = 2 with index 2; saturation); 3 Thm 3.1 (isogenies
l_j: E_j x F_j -> T_j with kernels <k_1 = (2/3, rho)>, <k_2 = (1/2, i)>); 4 Thm 4.1 (<k_1,h_1> = C_3 x C_3, <k_2,h_2> = C_2 x C_4 act
freely; covers of degree 9, 8 of S_1, S_2); 5 Thm 5.1 (N_j of exact holomorphic order m_j, smoothly trivial by
H_j(x) = exp(-2 pi i eps_j gamma(x))); 4 exercises (annihilators; sections of N_j^k; H^0(Omega^1_{S_j}) = C d xi; S_j not a torus).
Relation: the course version of `finite_filling_certificates.tex` FF1-FF22, FF42-FF46 (reader A1, candidate A1-5).

#### 1.2 `CG\src\normal-boundaries-and-integral-maps.md` (lesson 2; 15.8 KB, 246 lines; 8 Oct)
Thm 2.1 (deck group Gamma_j of the disc bundle and of S_j: t_lambda, G^_j with G^_j^{m_j} = t_{v_j}); Thm 3.1 (punctured bundle:
P_j = Lambda x|_{A_j} Z, positive loop Q_j = t_{v_j} G~_j^{-m_j}); Thm 4.1 (kernel of P_j -> Gamma_j is the central Z generated by
h_j = G~_j^{m_j} t_{-v_j} = Q_j^{-1}); Cor 4.2 (explicit isomorphism P_j = Gamma_j x Z, second component eps_j gamma(lambda));
Thm 5.1 (H_1(S_j) = Z^2; pi_j^* H^1(S_j;Z) = Z(m_j gamma) + Z psi_j, psi_1 = 2u+w+3 delta, psi_2 = u+w+2 delta, index m_j);
3 exercises. Relation: FF30-FF41; [AC26] Lemma A.4 in degree 1.

#### 1.3 `CG\src\varying-finite-fillings.md` (lesson 3; 27.5 KB, 479 lines; 9 Oct)
Thm 1.1 (all local period germs: q_j = s^{d_j} F_j(s^{m_j}), tau_j = (a_j - conj(a_j) q_j)/(1 - q_j), mu_1 = (2 - tau_1)/3 +
s^2 H_1(s^3)/(1 - q_1), mu_2 = (1 - tau_2)/2 + s H_2(s^4)/(1 - q_2), beta_j = beta_{j,0} + B_j(s^{m_j}) + b_j(s) with
b_j = (1/m_j) sum_k k phi_j(zeta_j^k s); conversely every germ with the laws has this form uniquely); section 2 (real inverse of the
marking, covariance R_j Pi = Pi(zeta_j s) A_j); Thm 3.1 (N_j = T_j/<G_j> proper over the disc, central fibre m_j S_j, real-analytic
diffeomorphism with the normal disc bundle of lesson 2); Thm 4.1 (T_j is the normalization of the base change, m_j branches
s = zeta_j^{-a} u; full proof of integral closure by idempotents); Thm 5.1 (h_j G_j h_j^{-1} = G_j^0 with h_j = translation by
(log s / 2 pi i) Pi(s) v_j); 3 exercises. Relation: FF23-FF41 and candidate_geometry.tex; A1-6.

#### 1.4 `CG\src\global-periods-and-line-bundle-quotients.md` (lesson 4; 34.3 KB, 597 lines; 9 Oct)
Sec 1 Thm 1.1 (tau with j(tau) = 1728 t, laws, orders 1, 2 at z_1, z_2, e^{2 pi i tau} = w/1728 + O(w^2), w = 1/t; the cusp width
and sign are derived from a trace computation (1.8)-(1.9)); Sec 2 Lemma 2.1 (additive cocycles with values in O_B, O_B(-p_0) split;
by Cauchy transform and Laurent splitting); Sec 3 Thm 3.1 (unique cusp-regular mu; the homogeneous sheaf is O_B(-p_0) via
Theta = (E_4 o tau)^2 sqrt(E_6 o tau)/(Delta o tau), orders 2, 1, -1 at z_1, z_2, p_0); Sec 4 Thm 4.1 (beta^part + c, all
solutions); Sec 5 Thm 5.1 (exact range Im c < -M, boxed (5.5); remark with the cusp-free solution beta + i t); Sec 6 Thm 6.1
(L_mu = O_{E_tau}(P - O), P = [mu]; A(xi, W) = (xi + 6 mu, e^{2 pi i beta} W); C^2/Pi Lambda = L_mu^x/<A>); Sec 7 Thm 7.1
(N(A^{-1} x) = e^{2 pi D} N(x) for the flat norm N; u = e^{-2 pi i c}, 0 < |u| < e^{-2 pi M}); Sec 8 Prop 8.1 (x = f^2 wp_tau(xi),
y = f^3 wp'_tau(xi)/2 with f^2 = -(2/3) t (t-1) g_2/g_3 identifies the family with y^2 = x^3 - 3 t^3 (t-1) x + 2 t^4 (t-1)^2;
rational parametrization (8.11); c_4, c_6, Delta_cub = 1728 t^8 (t-1)^3; node at infinity); 4 exercises.
Relation: candidate_geometry.tex `prop:period-input-audit`, `prop:period-exact-admissible-constants` (A1-2, A1-3); [E26] sections 1.3, 2.

#### 1.5 `CG\src\cusp-and-compact-threefold.md` (lesson 5; 81.8 KB, 1304 lines; 9 Oct)
Sec 1 (Z = s B_0 + C(t_c), units c_lambda = exp(2 pi i C lambda)); Sec 2 Lemma 2.1 (infinite toric threefold Y is Hausdorff,
second countable); Sec 3 Thm 3.1 (action Psi free and properly discontinuous on Y_eps, |log eps| > 2 M_C); Sec 4 Thm 4.1
(properness); Sec 5 Thm 5.1 (W reduced, irreducible, non-normal, normalization dP_6, gluing multipliers (5.5):
e^{-2 pi i mu_0}, e^{12 pi i mu_0}, e^{-2 pi i (7 mu_0 + b_0)}); Sec 6 Prop 6.1 (omega_{N_0} trivial); Sec 7 Thm 7.1 (cusp overlap);
Sec 8 Thm 8.1 (X compact Hausdorff, f proper with connected fibres); Sec 9 Thm 9.1 and Lemma 9.2 (the period section P = [mu]
generates the Mordell-Weil group, which is Z); Sec 10 (explicit resolution of the III and IV* fibres, (10.17), K_S = -F, Q^2 = -1);
Sec 11 Lemma 11.1, Thm 11.2 (height pairing; P = +-P_*, P_* = (0, sqrt2 t^2 (t-1)); P.O = 0, h(P) = 1/6, (6P).O = 2, P.(6P) = 2;
(11.14) wp_tau(mu) = 0); Sec 12 Lemma 12.1 (base-preserving birational self-maps of S are automorphisms), Thm 12.2
(Hom(t_{6P}^* M, M) = pi_S^* O_B(1), unique section with divisor F_infinity); Sec 13 Thm 13.1 (div(phi_per) = F_infinity;
beta = beta_part + c <=> phi_per = e^{-2 pi i c} phi_part; u_ref = lambda_0 e^{-2 pi i c}); (13.9) e^{2 pi i mu(p_0)} = -5 +- 2 sqrt6;
13.3 (which threefold the comparison constructs); 4 exercises ((14.4) (nP).O for all n; Hom line for 6kP is pi_S^* O(k)).
Relation: candidate_geometry.tex (A1-4 etc.) for sections 1-8; sections 9-13 have no workbench antecedent that I know of
(the Sources paragraph says they are "independently proved" here; primary source [E26] sections 2-4, and Schuett-Shioda's survey).

#### 1.6 `CG\src\integral-monodromy-and-fundamental-group.md` (lesson 6; 38.4 KB, 715 lines; 9 Oct)
Prop 1.1 (T_j = (A_j^{-1})^t, orders, T_1 T_2 T_0 = I, ker = im (M_0 - I) = Lambda_tor = Z w^ + Z delta^); Thm 2.1, 2.2 (cusp
invariants; common invariants Z gamma, Z q with q = uw + 6 gamma delta, Z gamma u w; coinvariants Z[delta], Z[gamma delta] with
[uw] = 6[gamma delta], Z[u w delta]; complete relation matrices); Lemma 3.1 (van Kampen in the form used); Prop 4.1
(pi_1(J) = Lambda x| F(rho_1, rho_2)); Prop 5.1 (fillings impose rho_1^3 = t_{v_1}, rho_2^4 = t_{v_2}); Lemma 6.1 (Y_eps simply
connected, chart proof), Thm 6.2 (pi_1(N_0) = Lambda/Lambda_tor, kernel H); Thm 7.1 (pi_1(X) = 1 from the presentation
<c, x, y | c central, xy = 1, x^3 = c, y^4 = c^{-1}>); Prop 8.1 (integral dictionary with Engel's marking, matrix P);
4 exercises (G(l_0,l_1,l_2) = Z/|12 l_0 - 4 l_1 - 3 l_2|; additional free affine fillings X_{r_1,r_2}; q^2 = 12 vol; H = Z^3 not central).
Relation: exact_algebra.tex, integral_leray.tex `prop:geometric-pi1`; [AC26] Thm 7.17; [E26] sections 5-6.

#### 1.7 `CG\src\canonical-divisor-and-intrinsic-fibration.md` (lesson 8; 29.3 KB, 505 lines; 9 Oct)
Lemma 1.1 (f_* O_X = O_B); Sec 2 (characters chi_j = zeta_j det R_{g_j}, exponents a = (2,1), k_j = m_j - 1 - a_j = (0, 2),
correcting units phi_j); Sec 3 (K = f_* omega_{X/B} = O_B(p_0), generated by Theta^{-1} d zeta_1 ^ d zeta_2); Thm 4.1
(div(ev) = 2 S_2; omega_X = O_X(-2 S_2); omega_X^{-2} = f^* O_B(p_2)); Thm 5.1 (f_* O_X(k S_2) = O_B(floor(k/4) p_2) for all k);
Cor 5.2 (h^0(omega^{-m}) = floor(m/2) + 1; h^0(omega^m) = 0 for m > 0); Thm 6.1 (R(X, -K_X) = C[U,V], degrees 1, 2);
Thm 7.1 (|-2K_X| base-point free, equal to f up to the explicit isomorphism beta(t) = [t-1 : A + B(t-1)]; |-K_X| = {2 S_2});
Cor 7.2 (any biholomorphism between two threefolds of the construction commutes with the fibrations, and the base map is the
identity); 4 exercises (all graded automorphisms; every member of the pencil with multiplicity).
Relation: analytic_canonical_ring.tex (CR1)-(CR5), analytic_picard.tex (9.2)-(9.6); reader B, candidate B-8.

#### 1.8 `CG\src\periods-and-nontrivial-deformation.md` (lesson 9; 49.4 KB, 808 lines; 11 Oct)
Thm 1.1 (proper family X_Q -> Q over discs Q in P = {Im c < -M}); Thm 2.1 (marked map w = A_delta zeta + B_delta conj(zeta),
Beltrami matrix nu_delta = delta P/(2iD + delta)); Prop 3.1 (KS_F(d/dc) = -[nu'] != 0); Sec 4 (relative pencil; Lemma 4.1;
critical schemes; (4.9) KS_X != 0, h^1(T_X) >= 1); Lemma 5.1 (centralizer {aI + bE}; middle families: c' - c in Z, linear part
+-I); Sec 6 ((6.2), (6.3): N_j l_j = -(1-a) v_j - n eps_j delta^; (6.4), (6.5): Lambda^{A_1}/N_1 Lambda = Z/3,
Lambda^{A_2}/N_2 Lambda = Z/4 + Z/2); Sec 7 (construction of X_c -> X_{c+n} for even n: (7.1)-(7.16)); Thm 8.1
(X_c = X_{c'} iff c' - c in 2Z); (8.2) parameter disc w = e^{-pi i c}; 4 exercises (9.3: u_ref = lambda_0 w^2 and the KS class in
the u-coordinate; 9.4: critical values over C[eps]).
Relation: the receiving proof of the two files in 1.10; reader B, candidates B-6, B-7.

#### 1.9 Companions
- `CG\src\integral-line-bundle-descent-for-the-affine-fillings.md` (19.8 KB, 283 lines; 11 Oct). Explicit smooth line bundles
  L_C on R^4/Z^4 with c_1 = a h_j + b q (h_j = gamma eta_j), explicit lifts G_{j,l,beta} of the affine generator with quadratic
  phases, power defect (2.9)-(2.11), criterion l N_j = -kappa_j. Result (3.7): pi_1^* H^2(S_1;Z) = Z h_1 + Z q (all invariants),
  pi_2^* H^2(S_2;Z) = {a h_2 + b q : a = b mod 2} = Z(2 h_2) + Z(h_2 + q); intersection form of S_2 in that basis [[0,1],[1,4]].
  Constant phases 8b/9, 27b/32. Two exercises. Receiving lesson: 7.
- `CG\src\integral-duality-and-the-specialization-lattices.md` (25.1 KB, 350 lines; 11 Oct). Integral Poincare duality with
  compact supports proved from singular chains (Lemma 1.1, Lemma 2.1, Thm 3.1, Cor 3.2); (4.2) dual-lattice test for the image of
  pi^* under a finite regular cover; (4.9) L_1^3 = Z b + Z c_1, L_2^3 = Z(2b) + Z c_2 with b = gamma u w,
  c_1 = u w delta - 4 gamma u delta - 2 gamma w delta, c_2 = u w delta - 3 gamma u delta - 3 gamma w delta. Two exercises.
  Both companions reprove [AC26] Lemma A.4 (indices (1,3,1,1,3) and (1,4,2,2,4), and the same lattice
  {a gamma^eta_2 + b q : a = b (2)}) by other means; (4.9) names the generators in degree 3.

#### 1.10 `CG\sources\period_parameter_deformation.tex` (18.3 KB, 396 lines) and `period_shift_classification.tex` (25.7 KB, 590 lines)
Byte-identical to the workbench files read by reader B (sha256 8baadffb... and 6dff2b4b..., same as
`canonical_S6_snapshot\supporting_materials\workbench\research\period_*.tex`). (PD1)-(PD18) and (PS1)-(PS29), (PS28a).
Lesson 9 follows them step by step: sections 1-4 = PD; sections 5-8 = PS (Lemma 5.1 = pshift:lem:centralizer, (6.3) = (PS10),
(6.4)-(6.5) = (PS11)-(PS12), (7.1) = (PS13), (7.8) = (PS21), (7.12) = (PS24), (7.14) = (PS27), (7.16) = (PS28a), (8.2) = (PS29)).
What the lesson has and the tex files do not: Exercise 9.1 (composition of the marked maps with the changed D), Exercise 9.3
(u_ref = lambda_0 w^2, the KS class in the u-coordinate, (9.9)), Exercise 9.4, and the references to L4/L5 for the meaning of u.
What the tex has and the lesson does not: nothing mathematical that I saw; the tex ends with the same non-claims.

#### 1.11 Checkers (`CG\checks\`); none was run by me
All result files record the sha256 of the lesson source; all ten hashes match the current sources (I recomputed them).
- `verify_finite_quotients.py` -> `EXACT_CHECKS.json` (45 passed): orders of A_j, fixed and image lattices, determinants -3, -2,
  period covariance R_j Pi_j = Pi_j A_j, the kernel points k_j, intertwining L_j h_j = R_j L_j + Pi_j v_j/m_j, freeness test
  (only the identity has a period translation), characters, one-form eigenvalues.
- `verify_normal_boundaries.py` -> `NORMAL_BOUNDARY_CHECKS.json` (45): power relation, centrality data, coordinates of the kernel
  generator (-eps_j, 0, m_j), the product isomorphism and its inverse on each residue class.
- `verify_varying_fillings.py` -> `VARYING_FILLING_CHECKS.json` (72): symbolic covariance (2.4), the cyclic sums (1.12), (1.14),
  (1.15), the Cayley inverse, branch idempotents (4.6), the conjugacy (5.4).
- `verify_global_periods.py` -> `GLOBAL_PERIOD_CHECKS.json` (45) [read in full]: orders 3, 4 of the laws; g_1 g_2 = inverse cusp
  translation (tau+1, mu, beta-1); covariance; real determinant T V - 6 U^2; the parabolic trace identity (1.9); the identity
  2 pi V - 12 pi U^2/T = 2 pi D; discriminant, j, c_4, c_6 of the cubic; the section (0, sqrt2 t^2 (t-1)); the model at infinity;
  the rational parametrization; (8.9); g_2^3 - 27 g_3^2 = (2 pi)^12 Delta. Algebra only; nothing about M or the range.
- `verify_cusp_geometry.py` -> `CUSP_GEOMETRY_CHECKS.json` (122): chart substitutions, the three edge exponents, the resolution
  charts (10.3)-(10.16), E_6 Cartan matrix and inverse, corrections 4/3 and 1/2, height 1/6, nodal parametrization (9.4)-(9.5),
  the first-order term excluding the node, comparison exponents.
- `verify_integral_monodromy.py` -> `MONODROMY_GROUP_CHECKS.json` (72): all matrices of L6 sections 1-2 (exterior powers from
  minors, invariants, torsion-free coinvariants), the dictionary P (both inverses, intertwining, cusp comparison, images of v_1,
  v_2, "source signed sphere parameter"), the cyclic terminal group.
- `verify_canonical_ring.py` -> `CANONICAL_RING_CHECKS.json` (38): determinant characters, exponents k_j, floors, bases of the
  graded pieces up to degree 24, Hilbert series, graded automorphisms, pencil members.
- `verify_period_deformation.py` -> `PERIOD_DEFORMATION_CHECKS.json` (42) [read in full]: A_j E = E A_j = E; the centralizer by
  solving the linear system (two parameters); N_1, N_2 and their Hermite forms (N_1 Lambda = <3 v_1, delta^>,
  N_2 Lambda = <4 v_2, 2 delta^>); (7.2), N_1 l_1 = -n delta^, N_2 l_2 = n delta^; (7.8); the Beltrami identities (2.2)-(2.8);
  Pi_{c+n} = Pi_c (I + nE); "n delta^ in N_2 Lambda iff n even" for -15 <= n <= 15; (9.3), (9.9). It does not check the analytic
  parts (H^1(B,V) = 0, extension over the cusp strata, the normalization lift).
- `verify_affine_line_descent.py` -> `AFFINE_LINE_DESCENT_CHECKS.json` (42); `verify_integral_duality.py` ->
  `INTEGRAL_DUALITY_CHECKS.json` (67; mostly the cap-boundary sign identity for simplices up to dimension 8, plus (4.8)).
Every result file states that it checks algebra only and is "author self-check, not independent proof certification".

#### 1.12 Read for comparison
[E26] `literature\engel_S6.txt` L100-700 (sections 1.3-5) and L1160-1300 (section 8). [AC26] transcription: L956 (Remark 3.12),
L1651 (Prop 5.6), L1722-1790, L1795-1891 (Construction 6.1, Prop 6.3, Remark 6.4), L2809-2825, L3005-3010 (Thm 7.22),
L5149-5160 (Lemma A.4). `B_notes.md` B-6, B-7, B-8, B-17; `A1_notes.md` A1-2, A1-4, A1-5.

---

---

### Reader G1b: Course CG-S6, lesson 10 and analytic companions

Full notes: `work\G1b_notes.md`.


#### 1.1 `courses\CG-S6\README.md` (11.6 KB, 11 Oct 2026) and `course.json` (69 KB, 11 Oct)

Course "Complex threefolds from marked torus families", 11 lessons, author record GPT-6 Astra (OpenAI), Codex,
Ultra, 9 Oct 2026; status `complete_written_series_author_self_checked`; "no independent whole-course review is
claimed". Lesson 10 unit: `CG-S6-10`, title "Non-normal fibres, the missing torsion map, and a proper test
family", requires lessons 1, 5, 6, 7 (Sections 1-8), 8; six solved exercises; ten result ids, all with status
`complete_written_argument_author_self_checked`:
CG-S6-10-TORSION (#normalization-isomorphism), -TEST (#exact-counterexample), -RELATIVE (#relative-differentials),
-REDUCTION (#algebraic-reduction), -CUSP (#cusp-section-space), -DUALITY (#duality-and-base-change), -INDEX
(#global-index), -CDP (#cdp-comparison), -BOUNDARY (#analytic-boundary-cocycle), -CENTRAL
(#analytic-central-restriction). Proof providers attached to lesson 10: smooth-duality-and-finite-twist-complexes,
proper-base-change-over-a-curve, tangent-index-with-torsion-line-bundles; plus the ten "general analytic" entries
(dated 11 Oct). The course does not reprove the Dolbeault numbers of [AC26] section 9; lesson 10 writes
Pic(X) = H^1(X,O_X) = C^q with q left unspecified (line 1176).

#### 1.2 `src\non-normal-fibres-and-vanishing.md` (132 KB, 2,245 lines, file date 11 Oct 2026) - read in full

Sections, with the labelled statements (the lesson numbers equations (s.n); only Theorems 2.1, 4.1, 5.1 carry
theorem numbers):

- §1 (l. 17-82) cotangent filtration. S reduced effective Cartier divisor in a smooth threefold X. Conormal
  sequence 0 -> N^* -> Omega^1_X|_S -> Omega^1_S -> 0 exact on the left (proof by reducedness). T_S = ker(Omega^1_S ->
  j_* Omega^1_{S_reg}), tilde-Omega = Omega^1_S/T_S, K_S = ker(Omega^1_X|_S -> tilde-Omega). (1.5): 0 -> N^* -> K_S -> T_S -> 0 and
  0 -> K_S -> Omega^1_X|_S -> tilde-Omega -> 0. (1.8): if H^0(tilde-Omega (x) A) = 0 and H^0(N^* (x) A) = 0 then
  H^0(S, Omega^1_X|_S (x) A) = ker(delta_A : H^0(T_S (x) A) -> H^1(N^* (x) A)).
- §2 (l. 84-199) Theorem 2.1 (normal crossings): natural isomorphism Phi : eta_* eta^* N^* -> K_S compatible with the
  conormal inclusion; T_S = (eta_* O_{S~}/O_S) (x) N^*; delta_A is the normalization connecting map. Local proofs at
  double and triple points; (2.9)-(2.12) the exact sequence R -> R~ -> (three curve rings) -> C at a triple point.
- §3 (l. 201-268) full fibre S = f^{-1}(b): N^* trivialized by [f^*t]; (3.2) H^0(K_S (x) A) = H^0(S~, eta^*A); (3.6)
  under H^0(S~, Omega^1_{S~} (x) eta^*A) = 0: H^0(S, Omega^1_X|_S (x) A) = H^0(S~, eta^*A); (3.7) S connected, eta^*A trivial:
  A trivial or H^0(S,A) = 0; (3.8) dim ker delta_A = r (number of components of S~).
- §4 (l. 271-337) Theorem 4.1: the family C = {y^2 z = x^2(x+z) + t z^3} over |t| < eps < 4/27, X = C x P^1, is smooth
  and proper, central fibre (nodal cubic) x P^1 reduced irreducible normal crossings, normalization (4.3).
- §5 (l. 339-413) A_lambda (gluing scalar lambda at the node); Theorem 5.1: A = pr_1^* A_2 is the restriction of
  O_C(P - Q) for explicit sections P, Q; (5.8) lambda = (1+b)(1-a)/((1+a)(1-b)); comparison with [N] Lemma 4.3
  (multiplier 1/3).
- §6 (l. 415-481) (6.1)-(6.4): H^0(S, N^* (x) A) = 0, H^0(S, tilde-Omega (x) A) = 0, H^0(S, Omega^1_X|_S (x) A) = C; (6.5)-(6.8)
  explicit generator, its torsion image -(2/3) tau (x) s_D, H^0(T_S (x) A) = C, delta_A = 0. Scope paragraph: this is a
  disc family, not a compact counterexample.
- §7 (l. 483-734) relative differentials. (7.3) Tors(Omega^1_{R/C{t}}) = R[w] = R/(phi), phi = gcd of partials of t;
  (7.7)-(7.9) t = xy, xyz: torsion-free, not locally free; (7.10) t = s^m: torsion R/(m s^{m-1}) ds; (7.12)
  Tors Omega^1_{X/B} = (f^* omega_B (x) O_X(Z))|_Z with Z = sum_c (f^*(c) - f^*(c)_red), (7.13) Z = 2 S_1 + 3 S_2 for X;
  (7.15) Omega^2 for t = xy has torsion R/(x,y); (7.19)-(7.21) for t = xyz the torsion Q of Omega^2 is Ext^2(R/J, R),
  J = (xy,xz,yz), needs two generators at the triple point; (7.22); (7.23) Omega^3 = R/(Jacobian ideal).
- §8 (l. 736-781) (8.1), (8.5): M(X) = f^* C(t), a(X) = 1; proof by "every effective divisor is vertical".
- §9 (l. 783-928) the cusp fibre W, eta : E_0 = dP_6 -> W. (9.2): for every line bundle B on X, eta^* i^* B trivial,
  H^0(W, tilde-Omega_W (x) i^*B) = 0, dim H^0(W, Omega^1_X|_W (x) i^*B) = 1. Proofs of H^1(dP_6, O) = 0 (Laurent/Čech,
  (9.3)-(9.7)) and H^0(dP_6, Omega^1) = 0 (9.8). (9.14)-(9.17) adjunction with the base tangent line kept.
- §10 (l. 930-1060) (10.6) duality on a Cartier divisor of a compact smooth threefold; (10.7)-(10.10) finite complex,
  the sequence 0 -> M^q/t -> H^q(X_c) -> M^{q+1}[t] -> 0, R^q f_* E = 0 (q>2), top-degree isomorphism; boxed (10.12):
  dim H^2(W, (T_X (x) L)|_W) = 1 = dim (R^2 f_*(T_X (x) L))_{p_0} (x) C(p_0) for every L in Pic(X).
- §11 (l. 1062-1256) (11.1): chi(X, T_X (x) L) = 1 and H^2(X, T_X (x) L) != 0 for every L; (11.6) the full degree-6
  polynomial; (11.8) H^0(V(-mD)) = 0 for m >> 0; (11.12)-(11.13); (11.14) R^2 g_*(T_X (x) L) != 0 for every map g onto
  a curve; §11.5 generalization to b_1 = b_2 = b_3 = 0 and (11.16) chi = 1 - b_3/2.
- §12 (l. 1258-1394) comparison with CDP98/CDP20: (12.1) abelianization of K ⋊ Q; (12.4) H_1(X°;Z) of rank 3;
  (12.5)-(12.6) image of H^1(X°;Z) -> H^1(F,O_F) is one line, in the original periods; §12.2 the p. 692 inference;
  §12.3 which conclusions X contradicts ((12.8)), and that X is no counterexample to CDP20 Theorem 2.1.
- §13 (l. 1396-1505) Exercises 1-4 with solutions: every A_lambda extends ((13.1)-(13.4)); Ann(Q) = (xy,xz,yz);
  the stalk M = (R^2 f_*)_{p_0} is A or A/(t^r) ((13.7)); (13.8) h^2 = h^1 + 1 - b_3/2.
- §14 (l. 1510-1885) "Line-bundle factors and the three boundary equations": (14.4) invariant integral 2-forms
  = Z q, q = uw + 6 gamma delta; (14.6) V_G = Z[delta]; crossed homomorphism d : pi_1(base) -> V_R from factors of
  automorphy ((14.12)-(14.15)); (14.20) norm equations N_{T_j} d_j = iota_{v_j} E at the two finite fillings; (14.24)
  cusp: d_0-bar = 0; (14.26)-(14.27): k/2 = 0, so c_1(L|_F) = 0 for every L in Pic(X).
- §15 (l. 1889-2173) "Recovering the central restriction from the original toric family": degrees (d_1,d_2,d_3) of a
  line bundle M on the cusp neighbourhood on the three pairs of hexagon sides; divisor D_a (15.3)-(15.9); boxed
  (15.21) E_M((lambda,0),(0,m)) = -B(B_0 lambda, m); (15.22)-(15.23): eta^* i^* : Pic(X) -> Pic(dP_6) is zero, without
  H^2(X;Z) = 0.
- §16 (l. 2175-2235) Exercises 5-6. Sources paragraph (l. 2239-2245).

Relation to other files: §§1-6, 10-12 are the "course" form of `cdp_program.tex` (props
`prop:missing-cotangent-filtration`, `prop:missing-global-section-criterion`, `prop:conductor`,
`prop:nodal-counterexample`, `thm:cartier-duality`, `cor:surface-top-base-change`, `lem:semidirect-abelianization`,
`thm:corrected-cdp-global`, `cor:corrected-cdp-relative`); §§14-15 are the course form of its "topology-independent
route" (lemmas `lem:picard-crossed-defect`, `lem:picard-finite-norm`, `lem:picard-cusp-defect`,
`prop:direct-boundary-picard`). `CG-S6-10.html` (181 KB) is the rendered reader of the same source.

Differences between the lesson and the September workbench that I saw:
(i) the workbench (cdp_program.tex l. 1611-1615) says of the test family "no extension of that bundle to the
displayed total space is claimed"; [N] Lemma 4.3 and the lesson (Theorem 5.1, Exercise 1) prove the extension;
(ii) the workbench proves existence of one section (as [AC26] Lemma 10.3); the lesson proves the exact kernel
(Theorem 2.1) and exact dimensions; (iii) the workbench has `thm:corrected-cdp-fibrewise` (if all fibres are reduced
and delta_c is injective for every c, then R^2 f_* = 0 and the CDP conclusions hold); the lesson has no such
theorem but its §3 gives the sharper normal-crossings form; (iv) the lesson states the global theorem under
Betti-number hypotheses (b_1 = b_2 = 0), the workbench and [N] under H^1(X;Z) = H^2(X;Z) = 0, a(X) = 1 and holomorphic
algebraic reduction.

#### 1.3 `src\proper-base-change-over-a-curve.md` (28 KB, 442 lines, 11 Oct) - read in full

"Proper base change from the actual graph resolution." Setting: X connected compact complex manifold of dimension
n, f : X -> C nonconstant to a smooth curve, E a holomorphic vector bundle. §1 graph Gamma in X x U is a Cartier
divisor, (1.3)-(1.4) two-term resolution of j_*(E|f^{-1}(U)) and of each full fibre (equations s^3 - tau, s^4 - tau,
xy - tau, xyz - tau kept); f is flat. §2 smooth identification of the bundles M_t with M_0, holomorphic in t. §3 the
elliptic cone complex (3.1)-(3.2) on A^{0,k}(E) + A^{0,k+1}(F), Hodge contraction (3.7). §4 homological perturbation
(Crainic's formulas) gives a finite free holomorphic complex K (4.6). §5 K represents Rf_*E, evaluation gives the
full fibre ((5.3)-(5.4)). §6: K^q = 0 outside [0, n-1], R^q f_*E = 0 for q > n-1 ((6.3), by Serre duality on X),
coherence over C{sigma}, (6.4) 0 -> R^q/sigma -> H^q(X_t, E) -> R^{q+1}[sigma] -> 0, boxed (6.5)
(R^{n-1} f_*E)_t (x) C(t) = H^{n-1}(X_t, E|X_t); (6.6) stalk A or A/(sigma^r) when the fibre group is one-dimensional.
Two exercises. Status: author self-check; "does not claim the general coherence theorem for every proper map".

#### 1.4 `src\general-proper-flat-surface-base-change.md` (14 KB, 182 lines, 11 Oct) - read in full

Theorem 1.1: f : X -> B proper flat map of complex spaces, B a Riemann surface, every full fibre of pure dimension
two, E a vector bundle: R^q f_*E = 0 (q > 2) and the canonical map (R^2 f_*E)_b (x) k(b) -> H^2(X_b, E_b) is an
isomorphism; no smoothness/compactness of X, no reducedness of fibres. Proof = (finite free complex representing
Rf_*E, from the companions NS, BT, RP, FC) + (coherent cohomology of a compact space of dimension <= n vanishes above
n, from QN, WL, BK, CL, QG) + the algebra of §5. §6 lists the cross-course prerequisites (eleven units of another
course, "complex-analytic-spaces-and-coherent-sheaves" and "elliptic-operators-and-boundary-problems", pinned at
commit da43414 of the programme's course repository; their texts are NOT in this folder). Credits Demailly,
"Complex Analytic and Differential Geometry" (author edition 21 June 2012), Ch. VI-VII and IX; "does not ... claim
novelty for the classical results".

#### 1.5 `src\tangent-index-with-torsion-line-bundles.md` (37 KB, 491 lines, 9 Oct) - read in full

Theorem (0.1): Y compact connected complex threefold, c_1(K_Y) and c_1(L) torsion in H^2(Y;Z). Then
chi(Y, T_Y (x) L) = chi_top(Y)/2 = <c_3(T_Y),[Y]>/2 = 1 - b_1 + b_2 - b_3/2.
"A receiving proof of a known index equality, with no novelty claim." Proof without the index theorem:
§1 the Fredholm index of sqrt2(dbar + dbar^*) is a homomorphism I_Y : K^0(Y) -> Z equal to chi(Y,V) on holomorphic V;
§2 a line bundle with torsion c_1 has [L] - 1 nilpotent and torsion in K^0(Y) ((2.3)-(2.5)), so I_Y(W (x) L) = I_Y(W);
§3 transfer of d = dbar + del to the harmonic spaces (finite perturbation series (3.4)-(3.7), no E_1-degeneration
assumed) gives chi_top = sum_p (-1)^p chi(Omega^p) (3.8); §4 de Rham/singular comparison, Poincaré duality, b_3 even;
§5 chi(O) = chi(K) = -chi(O) so chi_0 = chi_3 = 0, chi_2 = -chi_1, T (x) K = Omega^2, hence chi_top = 2 chi(T_Y) (5.6), (5.7);
§6 e(TY) = c_3 via the diagonal (6.4), and the full Riemann-Roch polynomial (6.6) for comparison. Two exercises.
Checker: `checks\TANGENT_INDEX_CHECKS.json` (74 finite checks).

#### 1.6 The nine `src\general-analytic-*.md` companions (all dated 11 Oct 2026, GPT-6 Astra, Ultra)

Each is a list of "Statement / Proof" items following Demailly's book; machine-readable copy in
`sources\general-analytic-proofs.json` (229 KB, 9 chapters, 60 proofs). I read QN, WL, BK, CL, QG and FC in full
and the statements plus sampled proofs of NS, BT, RP (see section 4). What each proves:

| file | items | content | textbook source (as cited) |
|---|---|---|---|
| general-analytic-qn.md (22 KB) | QN-0..5 | strongly q-convex functions; an analytic subset Y with a strongly q-convex exhaustion has a fundamental system of strongly q-complete neighbourhoods (QN-5) | Demailly IX.2.1-2.6, 2.11-2.13 (Demailly's 1990 theorem) |
| general-analytic-wl.md (26 KB) | WL-0..6 | L^2 dbar with weights on a strongly q-complete manifold, non-Kähler metric: H^k(M, O(E)) = 0 for k >= q (WL-5); approximation in degree q-1 (WL-6) | Demailly VI.2.3, VII.1-2, VIII.4, IX.3.1, IX.4.1 (Andreotti-Grauert) |
| general-analytic-bk.md (17 KB) | BK-0..5 | Bochner-Kodaira-Nakano identity for a Hermitian (non-Kähler) metric: Delta'' = Delta'_tau + [i Theta, Lambda] + T_omega | Demailly VI.6.1-6.14, VII.1-2 |
| general-analytic-cl.md (22 KB) | CL-0..5 | passage to coherent sheaves on a local model (finite free ambient resolution); topology on cohomology; local q-Runge approximation | Demailly IX.4.C, Lemma IX.4.9 |
| general-analytic-qg.md (31 KB) | QG-0..6 | Mayer-Vietoris with Fréchet topologies, bumps, finiteness; QG-5: H^k(X,F) = 0 for k >= q on a strongly q-complete space, F coherent; QG-6: compact space of dimension <= n has H^k(Z,F) = 0 for k > n | Demailly IX.4, Lemma 4.12, Prop. 4.13 (Andreotti-Grauert) |
| general-analytic-ns.md (37 KB) | NS-0..6 | completed tensor products, nuclear maps and spaces; Gamma(X,F) is nuclear; Gamma(X,F) ^(x) Gamma(Y,G) = Gamma(X x Y, F box G); restrictions are nuclear | Demailly IX.5.2-5.20, 5.36-5.37 |
| general-analytic-bt.md (29 KB) | BT-0..6 | balanced completed tensor over a nuclear algebra, bar-Tor, transversality, subnuclear maps | Demailly IX.5.25-5.37 |
| general-analytic-rp.md (25 KB) | RP-0..5 | "fully nuclear" algebras with a radius system; perturbation of a surjection by a subnuclear map has finitely generated cokernel after shrinking (RP-5, Schwartz-type) | Demailly IX.5.38-5.44(a) |
| general-analytic-fc.md (32 KB) | FC-0..7 | finite free complex quasi-isomorphic to the relative Čech complex; FC-5: R^q f_*G coherent for f proper to a Riemann surface; FC-6 bounded complex; FC-7 = Theorem 1.1 of §1.4 | Demailly IX.5.44 and proof of IX.5.1 (Grauert's theorem, Kiehl-Verdier / Forster-Knorr method) |

All nine are textbook theorems reproved (Andreotti-Grauert vanishing and finiteness; Demailly's q-complete
neighbourhood theorem; the Hermitian Bochner-Kodaira-Nakano identity; Grauert's direct image theorem; cohomology
and base change in top degree). I saw no statement in a generality or form unknown to me. Two restrictions
relative to the textbook: the direct image theorem is proved only over a one-dimensional base (FC-4..7), and FC-7
is for vector-bundle coefficients. The vocabulary "fully nuclear", "transverse", "A-subnuclear" is Demailly's. The
only non-textbook content is a handful of repairs of the source text (see candidate G1b-12).

`sources\general-analytic-dependencies.json` (14.5 KB): the 60 result ids, and 11 external prerequisite units with
hashes and result locators; `review: self_reviewed true, independently_reviewed false, formally_verified false`.
WL-4..6 carry status `conditional_on_BKN-HERMITIAN-TORSION` in the JSON; BK-5 discharges it.

Not in my list but a declared companion of lesson 10: `src\smooth-duality-and-finite-twist-complexes.md` (35 KB,
10 Oct): Hodge theory for a Hermitian metric, smooth Serre duality with signs, finite complexes for the family
(11.10) of line-bundle twists, analytic jump loci. Headings read only.

#### 1.7 `checks\verify_conormal_torsion.py` (10.6 KB) and `checks\CONORMAL_TORSION_CHECKS.json` (61 checks passed)

Exact sympy checks: the cubic, its normalization, the points P, Q and (5.6); the node coordinates (4.5)-(4.6); the
gluing scalar (5.8)-(5.9) and the -2/3 in (6.7); the triple-point lift (2.12); for 2 and 3 branches and polynomial
degrees 0..6, that the image of Phi equals the kernel of restriction to the branches (a finite-degree test of
Theorem 2.1); the maps (7.8), the syzygy (7.17), the wedge relations (7.18), the Ext presentation; the polynomial
(11.6); Exercise 1; the coinvariant relations (12.3) and the saturation; the period formula for gamma (12.6);
the hexagon connectivity used in (9.5) for the 80 weights in [-4,4]^2; the twelve equations (14.3), rank 5 and
kernel q; (14.5); (14.25), A_j v_j = v_j, T_j eta_j = eta_j; N_{T_j}(T_j - 1) = 0; 2 - 3/2 = 1/2; (15.3)-(15.7); (16.1)-(16.2).
The receipt is bound to the lesson's sha256. These are finite algebra checks of formulas; they do not test the
sheaf or analytic arguments (the scope line says so).

My own recomputation (scratch script, sympy): T_1^3 = T_2^4 = 1 for the matrices (A.1) of [AC26]; A_j = (T_j^{-1})^t
as in the lesson; invariants of Lambda^2 V = Z(uw + 6 gamma delta); V^G = Z gamma; Smith forms of the coinvariant relations
are (1,1,1,0) on both V and Lambda (so V_G = Z, Lambda_G = Z, no torsion); A_j v_j = v_j; iota_{v_1} q = (0,4,2,6),
iota_{v_2} q = (0,-3,-3,-6); d_1-bar + d_2-bar = 2k - 3k/2 = k/2; the polynomial (11.6); the multiplier 1/3 of [N]. All
agree with the lesson. Hand checks: (15.6)-(15.7), (5.5)-(5.6), (6.7), the double-point computation (2.5)-(2.6), and
the tangent-index identity on a Calabi-Yau threefold (chi(T) = h^{1,1} - h^{2,1} = chi_top/2).

#### 1.8 Comparison files

- `canonical_S6_snapshot\original_clean_transcription.tex`, l. 4455-4881 ([AC26] §10.1-10.6): read in full.
  Already there: Lemma 10.3 (one nonzero section s with eta^* s = eta^*(dg) (x) e, torsion image, not from the conormal
  term), Remark 10.4 (the reduction is valid for normal S), Theorem 10.5 (a) H^2(W,(T_X (x) L)|_W) != 0 and
  R^2 f_*(T_X (x) L) != 0 for every L, (b) injectivity of H^1(X,O) -> H^1(f^*(c),O) and countability, (c)
  H^2(X, T_X (x) M) != 0 for general M; Corollary 10.6 with chi(T_X (x) M) = c_3/2 = 1 for every M; §10.5 Lemma 10.7,
  the corrected count r = s - 1 + t' + 2g - b_1, failure of the CONCLUSIONS of CDP20 Lemma 4.2, Corollary 5.2,
  Proposition 5.5 for X (R^1 f_* O_X = O + O(-1)); Proposition 10.8 (a line bundle non-torsion on every fibre);
  §10.6 (what a proof would have had to control). Also l. 3515-3560 (Lemma 9.6, Proposition 9.7: proof of a(X) = 1).
- `cdp_program.tex`: statements listed in 1.2; read l. 17-111, 205-300, 1360-1665.
- `C:\Users\user\Documents\workbench_review_20261112\repo\s6\STATUS_2026-10-05.md` (10.6 KB): read in full.
  Its citations and the lesson:
  - [N] Theorem 4.4, Remark 4.5 (test family): in the lesson, §§4-6, sharpened (dimension exactly 1; every lambda).
  - [N] Theorem 5.2, Corollary 5.3 (what survives): in the lesson, §11.3-11.5 and Exercise 4, in the stronger form
    of [R]; the relative form (Corollary 5.3) appears as its contrapositive (11.14).
  - [R] Proposition 5.5 (extra hypothesis H^0(S~, eta^*A) = 0; dimension one at W): in the lesson, (3.2), (3.6), (9.2).
  - [R] Proposition 5.3 ("the torsion of Omega^1_S is present exactly at the non-normal points of S"): NOT in the
    lesson. The lesson treats only normal crossings and never states the normal case ([AC26] Remark 10.4 is also
    absent).
  - The status note says conclusion (a) of Theorem 2.2 is "for generic M"; arXiv:1904.11179v2 prints (a) without
    a quantifier on M (see 1.9). No mathematical consequence, since H^2 != 0 for every M.
  - The status note's "related statements that fail for X" (CDP20 Lemma 4.2, Cor. 5.2, Prop. 5.5) are from [AC26]
    §10.5; the lesson only treats the abelianization inference of Lemma 4.2 (§12.1) and does not discuss Cor. 5.2,
    Prop. 5.5, Prop. 5.6 or [AC26] Prop. 10.8.

#### 1.9 CDP20 (arXiv:1904.11179v2, 20 May 2019) and CDP98 (arXiv:math/9607215v1), fetched and read as PDF pages

CDP20 pages 1-3, 5-11, 13-18 read. Exact wording that matters:
- Theorem 2.2: X compact complex 3-fold, H^1(X,Z) = H^2(X,Z) = 0, a(X) = 1, algebraic reduction f : X -> C holomorphic.
  Then a) H^i(X, T_X (x) M) = 0 for i != 1; b) chi(X, T_X (x) M) <= 0; c) c_3(X) <= 0.
- Proposition 2.4: if R^2 f_*(T_X (x) L) = 0 for some (or general) L then the assertions of 2.2 hold; "Equation (1)
  is equivalent to the vanishing H^2(X_c, T_X (x) L|X_c) = 0 for all complex-analytic fibers X_c (with the natural
  fiber structure), equivalently H^0(X_c, Omega^1_X (x) L^*|X_c) = 0"; "here the case when X_c is singular, in particular
  non-normal, needs special care".
- §7 opening (arXiv p. 14 = Compositio p. 692): "We first consider irreducible fibers. Let S = red X_c. Using the
  (co-)tangent sheaf sequence 0 -> N^*_S -> Omega^1_X|S -> Omega^1_S -> 0 it is immediate that it suffices to show -
  provided L|S is non-torsion - the following statement (11) H^0(S, tilde-Omega^1_S (x) L|S) = 0, where
  tilde-Omega^1_S = Omega^1_S/torsion."
- Proposition 7.3 ("Equation (11) holds for singular reduced fibers"): its proof starts "By Lemma 4.6 and
  Proposition 4.11, kappa(S_0) = -infinity, the surface S is non-normal", and inside Step 1 (proof of the Claim,
  argued by contradiction) it derives "Thus all line bundles eta^*(L_t) are trivial".
- Proposition 4.11: "Let X_c = lambda S with S singular, irreducible. Then S is non-normal."
- Lemma 4.2: r = s - 1 + b_1(X_c); proof: "As seen in the proof of [CDP98, Lemma 3.2], H_1(X',Z) = H_1(C \ f(A),Z) +
  H_1(X_c,Z)". Corollary 5.2 (H^1(X,O_X) -> H^1(F,O_F) surjective), Proposition 5.5 (R^1 f_*O_X = O(b_1) + O(b_2),
  b_j >= 0), Proposition 5.6 (general L non-torsion on every fibre) as quoted in [AC26].

So the lesson (§12.2) and [AC26] read the printed proof correctly. In my own words: with A the twist and
H^0(N^*_S (x) A) = 0 (true when A is non-torsion on a connected S with torsion conormal bundle), the conormal sequence
only gives an injection H^0(Omega^1_X|_S (x) A) -> H^0(Omega^1_S (x) A). To conclude one needs the vanishing of
H^0(Omega^1_S (x) A), but (11) is the vanishing of H^0 of the quotient Omega^1_S/torsion. A section of Omega^1_X|_S (x) A
whose image in Omega^1_S (x) A is a nonzero torsion section is invisible to (11). For normal S there is no such
section (a fibre is a hypersurface, so a normal S has isolated singularities, Omega^1_S is torsion-free there and
the section extends as a conormal section: [AC26] Remark 10.4). For non-normal S the torsion sheaf T_S is supported
on the double locus and for normal crossings the sections that map to torsion are exactly H^0(S~, eta^*(N^* (x) A)).
This is nonzero whenever eta^*(N^* (x) A) has a section, in particular when eta^*A is trivial although A is non-torsion
(A lies in the kernel of Pic(S) -> Pic(S~), a group of gluing data that contains non-torsion elements). The failure
is exactly as the lesson says. Two remarks of mine that the files do not make: (1) by CDP20's own Proposition
4.11 every singular irreducible reduced fibre is non-normal, so the non-normal case, where the inference fails,
is the only case Proposition 7.3 is about; and in one sub-case of their own proof of 7.3 (the proof of the Claim
in Step 1, where H^1(S~, O) = 0) they use that "all line bundles eta^*(L_t) are trivial", which is exactly the
hypothesis under which the missed section exists; (2) Remark 7.2 and 7.4 (multiple fibres) pass from S = red X_c to the
non-reduced fibre in one sentence; neither [AC26] nor the lesson examines that step (the workbench says a
non-reduced fibre "requires additional nilpotent-thickening layers and is not covered").

CDP98 v1 introduction (p. 1-2): "The proof of the Theorem consists in showing that for generic L in Pic^0(X), we
have h^0(X, B (x) L) = h^2(X, B (x) L) = 0 for B either the tangent bundle T_X or the cotangent bundle. This forces
c_3(X)/2 = chi(X, T_X) to be 0", and Proposition 1.1 is the lemma H^0(Y, F (x) O(-kD)) = 0 for k >= k_0. So the
"surviving conditional theorem" and the identity chi(T_X (x) L) = c_3/2 are the valid core of CDP's own method.

#### 1.10 Answers to the four questions of the assignment (details in the candidates)

1. (a) G1b-1; (b) G1b-2; (c) G1b-3; (d) G1b-7. None of (a)-(d) is first proved in the lesson; (a), (b) were found
   in [N]/[R] after [AC26] Lemma 10.3; (c) is the valid core of CDP98; (d) is classical. As corrections of the
   literature on compact complex threefolds with b_2 = 0, (a)+(b) are, as far as my search shows, unpublished
   elsewhere (a search for an erratum or discussion of CDP20 p. 692 returned only the 2019/2020 corrigendum itself).
2. No. The lesson and the workbench give only conditional statements: G1b-3 (one vanishing H^2 implies c_3 <= 0 /
   b_3 >= 2), the fibre criterion G1b-1, the workbench's `thm:corrected-cdp-fibrewise`, and the corrected
   abelianization formula. There is no corrected bound and no classification under "normal fibres" or "trivial
   monodromy". [AC26] §10.5 notes that the printed Lemma 4.2 stands when the monodromy acts trivially on H_1(F;Q);
   the workbench (l. 1592-1606) gives the exact condition (5.33) under which the rank argument works. See G1b-13
   for the question this leaves. Which CDP statements fail for X: Theorem 2.2 a), b), c) (lesson (12.8)); CDP98
   main theorem and the S^6 corollaries (with lesson 7 for the sphere); the direct-sum inference in CDP98 Lemma
   3.2(2) = CDP20 Lemma 4.2 (lesson §12.1); and, in [AC26] only, the conclusions of Lemma 4.2 (r = 3, not 6),
   Corollary 5.2 and Proposition 5.5 (and the printed route to Proposition 5.6, whose conclusion holds for X by
   [AC26] Prop. 10.8). Survives: CDP20 Theorem 2.1 and [LRS] (X has no non-holomorphic meromorphic map to P^1;
   lesson l. 1392); Proposition 2.4 as a conditional statement; Proposition 7.3 as a statement about tilde-Omega
   ((11) does hold at W); Proposition 4.11 is consistent with X (W is non-normal).
3. G1b-3 (global) and G1b-4 (at W).
4. G1b-6.

---

### Reader G2: Course CG-S6, lessons 7 and 11 and topology companions

Full notes: `work\G2_notes.md`.


#### 1.1 `K\README.md` (11.6 KB, 11 Oct), `K\course.json` (69 KB, 11 Oct) — read in full
README: one paragraph per lesson; list of 46 checkers and companions; "no independent whole-course review is
claimed". course.json: 11 units, 84 results, 47 proof providers. Results for my lessons (all with status
`complete_written_proof_with_author_self_check`): CG-S6-07-HOMOLOGY ("Full original integral homology and
marked transgressions"), CG-S6-07-HOMOTOPY ("Original degree-one homotopy equivalence with both inverse
homotopies"), CG-S6-07-SMOOTH ("Orientation-preserving diffeomorphism homotopic to the original map, with
full frame and filling comparisons"); CG-S6-11-TYPES, -OCTONIONS, -NIJENHUIS, -ASSOCIATOR, -TRANSPORT,
-COORDINATES ("the corrected change-of-variable sign"), -GAUGE, -ANALYTIC, -INTEGRABILITY, -SPHERES,
-EXERCISES. Lesson 7 unit status: `authored_with_complete_receiving_proofs_author_self_checked`.

#### 1.2 `src\integral-homology-and-sphere-recognition.md` (84.6 KB, 1185 lines, 11 Oct) — read in full
Lesson 7. Notation: V = H^1(F;Z) = Z<gamma,u,w,delta>, q = uw + 6 gamma delta, vol = gamma u w delta;
p_0 = infinity (cusp), p_1 = 0 (m_1 = 3), p_2 = 1 (m_2 = 4); eta_1 = 2u+w+3 delta, eta_2 = u+w+2 delta.
- Section 1, Prop. 1.1: H_*(S_j; Z) torsion-free, Betti numbers (1,2,2,2,1).
- Section 2, Theorem 2.1: indices of `L_j^r = pi_j^* H^r(S_j)` in the invariant lattices: (1,3,1,1,3) and
  (1,4,2,2,4); full images `L_1^1 = <3 gamma, eta_1>`, `L_2^1 = <4 gamma, eta_2>`,
  `L_1^2 = <gamma eta_1, q>`, `L_2^2 = {a gamma eta_2 + b q : a = b mod 2}` (2.2);
  `L_1^3 = Z b + Z c_1`, `L_2^3 = Z(2b) + Z c_2`, b = gamma u w (2.14a). Proof of L_2^2: index 2 by
  determinants; gamma eta_2 not in the image by the d_2 of the group extension, `d_2(gamma eta_2) = -[eta_2]`
  in `H^2(C_4; V) = <gamma, eta_2>/<4 gamma, 2 eta_2>` (2.9); parity from the line-bundle descent companion
  (2.10a).
- Section 3: H^*(W; Z) = (Z, Z^2, Z^4, Z^2, Z) from the normalization resolution (3.1).
- Section 4, Theorem 4.1: sp^r: H^r(W) -> H^r(F)^{T_0} is an isomorphism for all r. Nearby-cycle spectral
  sequence (4.6)-(4.7); rank count leaves beta + d + e = 1 (4.9); resolved by the Gysin image of a
  transported T_f-orbit (4.10)-(4.16).
- Section 5, Prop. 5.1: H^0(B,R^1) = Z(12 gamma), H^0(B,R^2) = Z(2q), H^0(B,R^3) = Z(2 gamma u w),
  H^1(B,R^1) = H^1(B,R^2) = 0, H^2(B,R^r) = coinvariants; Q^1 = Z/3 + Z/4, Q^2 = Q^3 = Z/2 at p_2.
- Section 6, Theorem 6.1: d_2(12 gamma) = omega, d_2(2q) = omega[delta], d_2(2 gamma u w) = omega[gamma delta],
  all with coefficient +1 once omega is fixed by the clockwise annular sum.
- Section 7, Theorem 7.1: H^k(X;Z) = H_k(X;Z) = Z for k = 0, 6 and 0 otherwise.
- Section 8: dictionary with Engel's classes psi, k, xi, theta_E, nu via the matrix P of lesson 6;
  Engel's three signed transgressions recovered (8.3).
- Section 9, Theorem 9.1: a degree-one homotopy equivalence g: S^6 -> X with homotopy inverse h_X.
- Section 10: Prop. 10.1 (X minus two discs is a simply connected h-cobordism between 5-spheres);
  Theorem 10.2 (orientation-preserving diffeomorphism d: S^6 -> X with d ~ g, d^{-1} ~ h_X). Long paragraphs
  of links to the companions. "Status of the classical prerequisite" paragraph.
- Section 11: four exercises.
Relation to the baseline: sections 1-7 follow [AC26] section 7.7 and Appendix B step by step (Lemma 7.13,
Prop. 7.14, Lemma 7.25, Prop. 7.26, 7.27, Theorem B.1 with the same strategy (i)-(v), including the Gysin
argument along one T_f-orbit) and [E26] section 7 (Lemmas 7.4-7.6). What differs is in G2-1.

#### 1.3 `src\sphere-twists-and-the-original-smooth-six-sphere-comparison.md` (65.6 KB, 836 lines, 11 Oct) — read in full
- Section 1: the model twist `F_theta(q,z) = (cos theta(r) q + sin theta(r) z/r, -r sin theta(r) q + cos theta(r) z)`
  on the tube `N_R = {(q,z) in H + H : |q| = 1, <q,z> = 0, |z| <= R}` of an embedded S^3 in a 6-manifold P,
  theta = pi near the core and 0 near the boundary; comparison with Seidel's Dehn twist (math/0105186).
- Section 2: `(F_f)_*(x) = x - lambda(v,x) v`, `(T_f)_* (x) = x + lambda(v,x) v` on H_3(P;Z), via the variation
  map, with the integer sign (2.1)-(2.6).
- Section 3: a terminating algorithm: products of transvections carry any integral Lagrangian of a unimodular
  alternating lattice to any other (3.5)-(3.11).
- Section 4: the framed nullbordism W of the homotopy sphere Sigma, a ball removed, surgered to a 2-connected
  cobordism C' = C_- u_P C_+ with r handles of index 3 and s of index 4; `0 -> Z^r -> H_3(P) -> Z^r -> 0`;
  belts b_i and attaching classes a_j span two integral Lagrangians, s = r;
  `D^old_{ij} = sigma_i lambda(b_i, a_j)`, `H_4(C',S^6) = ker D^old`, `H_3(C',S^6) = coker D^old` (4.10).
- Section 5: regluing `C_phi = (C_- u C_+)/(i_+(p) ~ i_-(phi(p)))`; the frame comparison
  `A_phi(p) = tau_{-,phi(p)} (D phi_p + 1 + I_h) tau_{+,p}^{-1}` (5.6) ("the frame defect"; it is recorded, not
  computed and not used).
- Section 6: new incidence matrix U unimodular; slides, Whitney moves in the triple (6,3,3), cancellation;
  product map (6.8).
- Section 7: d (7.1), d ~ g (7.4), h ~ d^{-1} (7.5), tangent comparison `E_q = B_q P_H^{-1} Dd_q` (7.6);
  "Theta_6 = 0 ... the classical smooth recognition result ... no novelty is asserted" (7.8); 7.1: explicit
  homotopy between the tangential and the normal stable framing for any stably framed 6-manifold (7.14).
- Section 8: two matrix exercises (old torsion Z/3 and Z/2 kept, new gluing word). Section 9: sources.
"Both fillings" of the README = the old filling C' and the new filling C_phi.

#### 1.4 `src\almost-complex-structures-and-integrability.md` (79.5 KB, 1250 lines, 11 Oct) — read in full
(sections 7-8 on estimates at reading speed)
- 1: charts -> J, N_J (1.5) (sign opposite to Hill-Taylor), (1.8) `N_J(Z,W) = -4 pi^{1,0}[Z,W]`, (1.10).
- 2: two Cayley-Dickson products and the isomorphism Phi(a,b) = (a, b-bar) between them; cross product.
- 3: `J_p U = p x U`; `N_J(U,V) = -4 p x (U x V)` (3.6); `|N_J(U,V)|^2 = 16(|U|^2|V|^2 - <U,V>^2 - <JU,V>^2)` (3.7);
  `d omega = 3 phi` (3.8); the labelled field induces the orientation opposite to the outward one.
- 4: `N_J(U,V) = 2[p,U,V]_O` (4.3); kernel of N_U = span(U, JU), image W_U, inverse (4.8); the complex map
  `Lambda^2 T^{0,1} -> T^{1,0}` is an isomorphism with determinant 64i in adapted bases (4.12).
- 5: transport (5.2); J_X integrable; no closed taming form on X (5.3).
- 6: coordinate equation `d-bar F = A dF` (6.3), integrability (6.5), change of variables (6.7), gauge (6.8);
  "Source sign correction" for Hill-Taylor eq. 3.14 (6.9).
- 7: periodic gauge on a torus, `L = -Delta/4`, inverse Fourier multiplier (7.9), contraction.
- 8: ellipticity identity (8.2)-(8.3), smoothness, interior estimate (8.8), factorial bound (8.11).
- 9: complexified commuting flows; Theorem 9.1 (smooth Newlander-Nirenberg); the chart (9.5).
- 10: clutching, Fejer approximation, linearization (10.3), Riesz idempotent (10.5): K^0(S^2 x Y) is generated
  by K^0(Y) and b K^0(Y) (10.6); ch on (S^2)^n integral (10.11); `c_n(E)[S^{2n}]/(n-1)!` integral (10.15);
  (10.16)-(10.18): only S^2, S^6. A remark corrects wording in Konstantis-Parton section 6.
- 11: six exercises (Ex. 3: every local J-holomorphic function for the octonionic J is constant).
Companions of lesson 11 (read: opening, statements, closing): `thom-euler-for-lesson11.md` (36 KB; singular
chains, excision, universal coefficients, Thom isomorphism Theorem 7.1, Euler class, zeros on spheres);
`projective-splitting-for-lesson11.md` (13.6 KB; Gysin, H^*(CP^n;Z), projective bundle theorem, flag
bundles, tensor rule for lines); `integral-chern-classes-for-lesson11.md` (8.2 KB; Chern classes by the
projective relation, Whitney sum, conjugation, Chern character). Textbook, general, nothing about X.

#### 1.5 `src\the-original-six-dimensional-framing-invariant.md` (110.6 KB, 1386 lines, 11 Oct) — statements and sections 2, 5.6, 6.4, 8.4, 9 read; the rest by headings
Sections: 1 pi_3 SO(3) -> pi_3 SO(n) and its factor two; 2 the obstruction `k_tau(f,phi) in pi_3 SO(7+s) = Z`
and parity `epsilon_tau(f)` for an embedded S^3 (2.4)-(2.9), "Framing-extension criterion"; 3 values (standard
sphere 0; both factors of S^3 x S^3 with the Lie framing 1; graphs); 4 algebra of F_2-quadratic forms, Arf and
Gauss sum; 5 immersions, generic homotopies, `Q_tau = epsilon_tau + mu` (5.28); 6 quadratic law (6.21)-(6.22),
`Arf(q_tau) = 1` for the Lie-framed S^3 x S^3 (6.24); 7 embedded representatives; 8 framed bordism invariance
(8.12), reduction to indices 3 and 4, `kappa: Omega_6^fr -> F_2` (8.13); 9 `kappa` is an isomorphism (9.3),
`[Sigma, tau_Sigma] = 0` (9.4), criterion (9.5); 10 exercises; 11 sources (Michel-Weber 1409.0704 as context).
"Original" invariant of X computed: kappa(X, tau_X) = 0, from H_3(X;F_2) = 0. Nothing else.

#### 1.6 `src\spin-six-and-the-framing-comparison.md` (33 KB, 444 lines, 11 Oct) — statements and sections 4-6 read
Family index for loops; two-step loop periodicity; SU(4) -> SO(6) by Lambda^2; `pi_5 SO(6) = Z` by half the
Euler number (4.7); `pi_5 SO(7) = 0` (5.4); for a homotopy 6-sphere Sigma: `T Sigma + R` trivial (6.2), and an
oriented bundle isomorphism `B: g^* T Sigma -> T S^6` (6.3)-(6.4). General; X enters only as a homotopy sphere.

#### 1.7 Topology companions of lesson 7 (opening, headings and statements, closing; a few proofs sampled)
All dated 9-11 Oct 2026, all general (stated for "the original cobordism" but using nothing about X).
| file (KB) | what it proves |
|---|---|
| `cw-models-and-the-first-hurewicz-map.md` (21) | CW model of an open subset of R^N by a telescope of cube complexes; compact manifolds and the punctured cobordism as retracts; first Hurewicz theorem (Theorem 4.1) by "coherent simplex contractions". |
| `path-fibres-and-integral-homotopy-equivalences.md` (40) | path fibration, Serre homology spectral sequence by filtered chains, two edge maps; Theorem 5.1: an integral homology equivalence of simply connected spaces with CW comparisons is a homotopy equivalence, inverse constructed. |
| `relative-morse-functions-and-original-handles.md` (46) | existence of a Morse function on a cobordism constant on the ends (Sard on the family (1.5)); Morse lemma with Hessian coefficients; handle attachment with corners; finite handle decomposition. |
| `rearranging-the-original-framed-handles.md` (43) | reordering handles by index. |
| `morse-trajectories-and-critical-value-lowering.md` (33) | self-indexing ("ordered") Morse function; lowering a critical value with compact support. |
| `morse-cancellation-with-controlled-support.md` (33) | Theorem 2.1: cancellation of two critical points joined by one transverse trajectory, after Laudenbach (1307.2545); product map. |
| `removing-the-original-zero-and-top-handles.md` (24) | removal of index 0 and n. |
| `creating-an-original-cancelling-handle-pair.md` (28) | birth of a cancelling pair of indices k, k+1 in a regular band. |
| `framed-handle-slides-and-index-one-removal.md` (87) | pi_1 from the handle presentation; 2-handle slides; removal of index 1 and n-1 for n >= 6; section 8.1: the same under the weaker hypothesis that pi_1(M_-) -> pi_1(C) is onto. |
| `integral-handle-chains-and-signed-incidences.md` (34) | handle chain complex = singular homology; incidence = signed intersection of attaching and belt spheres; integral reduction; the dimension 6 and 7 cases. |
| `higher-index-framed-slides-and-chain-maps.md` (30) | handle slides in index 2 <= k <= n-2 and their effect on both neighbouring boundary matrices. |
| `belt-sphere-complements-and-the-whitney-disk.md` (89) | complement of belt spheres diffeomorphic to complement of attaching cores; embedded Whitney disc with framed collar in the triple (5,2,3); the pi_1 SO(3)-type frame obstruction. |
| `whitney-move-with-controlled-support.md` (41) | the Whitney move as a compactly supported flow; transport of the handle framings. |
| `whitney-moves-in-the-receiving-dimensions.md` (44) | the same for (d,p,q) = (5,2,3), (6,2,4), (6,3,3); rank-four frame obstruction. |
| `realizing-framed-handles-and-middle-cancellation.md` (53) | Morse function realizing a modified handle presentation; intersections = trajectories; simply connected h-cobordism theorem in dimensions 6 and 7 only (section 6). Sources: Benedetti 1907.10297, Durst-Geiges-Kegel 1811.09055. |
| `framed-manifolds-and-the-pontryagin-thom-map.md` (62) | Pontryagin-Thom in both directions with explicit tubes; suspension; (8.8) stable class zero iff bounds after stabilization; (8.11)-(8.13) tangential vs normal framing for X using J_X. |

#### 1.8 Stable-homotopy companions of lesson 7 (opening, statements, closing; key statements read)
| file (KB) | what it proves |
|---|---|
| `the-degree-six-milnor-cobar-calculation.md` (35) | Theorem 1.1: in the cobar complex of F_2[zeta_1, zeta_2, ...], `H^{s,s+6} = F_2{[zeta_1^4 | zeta_1^4]}` for s = 2 and 0 otherwise, for all s; Theorem 6.1: `H^{s,s+6} = 0` at every odd prime. |
| `coefficient-rings-and-the-original-degree-six-class.md` (52) | the presentation of the motivic dual Steenrod algebra over F_2[tau] from Isaksen-Wang-Xu (2001.04247), exact maps to the classical one after inverting tau (`Phi(zeta_i) = tau^{2^{i-1}-1} tau_{i-1}`), and: the cobar group in bidegree (2,8) over F_2[tau] is free of rank one (no tau-torsion), with a matrix certificate (`checks\ORIGINAL_COEFFICIENT_H28_CERTIFICATE.json`, 226 KB). A detour; the later chapters do not need the motivic coefficient ring. |
| `the-adams-tower-and-exact-inverse-limits.md` (57) | the Adams tower of the sphere at p, lim and lim^1 for towers of finite groups, convergence; all-length vanishing in stem 5; section 6 "source corrections" (Dugger-Isaksen, Goerss); sections 8-11: H F_p built from finite cocycles, finiteness of its stable homology. |
| `the-original-adams-tower-and-arithmetic-completion.md` (48) | for every bounded-below spectrum the Adams-tower limit equals the p-completion (Moore tower), with a pro-isomorphism bound `2m(n-b+1)`; `pi_0 C_s = Z/p^{s+1}`; section 9 corrects two slips in Strickland 2412.09361. |
| `the-actual-mod-two-adams-resolution-and-cooperation-maps.md` (40) | Gamma = pi_*(H ^ H) as a coalgebra; the Adams resolution equals the cobar complex of Gamma (both chain maps and homotopies); stem 6 needs Gamma only through degree 8. |
| `the-exact-characteristic-two-coordinate-calculation.md` (15) | over F_2-algebras: symmetric additive 2-cocycles, a formal group law with 2-series zero is additive, strict automorphisms of the additive law (toward Luecke 2109.00048). |
| `the-original-projective-coordinate-and-actual-cooperations.md` (27) | the Hopf algebra map `F_2[xi_1, xi_2, ...] -> Gamma` from RP^infinity; xi_1 is the class of the integer two. |
| `the-actual-mod-two-cooperation-comparison-through-degree-eight.md` (47) | that map is bijective in degrees 0..8 (bar constructions on K(Z/2,n), suspension); `pi_6(S^_2) = F_2`. |
| `the-original-odd-prime-cooperations-and-degree-six-adams-calculation.md` (44) | odd-prime analogue in the needed degrees; `pi_6(S^_p) = 0` for p odd. |
| `the-original-integral-stable-group-and-its-completion-maps.md` (51) | finite generation of homotopy groups of spheres; Freudenthal range; `pi_6(S) = Z/2`, detected by `[xi_1^4 | xi_1^4]` (7.4). |

#### 1.9 `src\smooth-duality-and-finite-twist-complexes.md` (35 KB, 10 Oct) — statements; sections 5-6 read
A lesson-10 companion (analysis, not topology): Hodge theory and Serre duality on a compact Hermitian
manifold without Kaehler hypothesis; for the family `d_z = d-bar_V + 2 pi i sum z_j b_j ^` of line-bundle
twists, a finite complex (H, D(z)) of holomorphic matrices by the homological perturbation lemma
(5.4)-(5.9); jump loci are analytic (6.1)-(6.2). Notes a misprint in Crainic math/0403266. General; applied in
lesson 10 to Pic^0(X) = C. Belongs to the reader of lesson 10.

#### 1.10 Checkers
`K\checks\*.json`: every file reports all checks passed (for my chapters: INTEGRAL_HOMOLOGY 75, SPHERE_TWIST
442, FRAMED_SIX_OBSTRUCTION 1695, SPIN_SIX 54, ALMOST_COMPLEX 80, PONTRYAGIN_THOM 51, and so on). Each states
its own scope: finite identities (matrices, signs, small ranks); "do not certify the global topological
proof". I did not rerun them.

#### 1.11 Baselines consulted
[AC26] `original_clean_transcription.tex` l.2632-2690 (Lemma 7.13, Prop. 7.14), l.3066-3200 (section 7.7),
l.5300-5470 (Appendix B), l.3216-3226 (Theorem 8.1, by Hurewicz, Whitehead, Smale, Kervaire-Milnor).
[E26] `engel_S6.txt` l.627-646 (diffeomorphism by Smale and Kervaire-Milnor), l.940-1140 (section 7).

---

---

### Reader I: Local workspace outside the snapshot and the course: consolidation, related sources, ledgers, custody

Full notes: `work\I_notes.md`.


#### 1.1 Top level of LW

- `README.md` (635 B, 29 Sep 2026): "S6 and recent-results continuing corpus"; six source roots archived; "Transfer
  and routing do not establish new independent proof acceptance"; no remote publication.
- `CUSTODY_INDEX.md` (12.7 K, header "Updated 2026-09-28T23:59:59Z", file date 29 Sep 19:43). Continuing main
  `01a0ea06-5fdc-7a60-97f3-4f4347467d95` (Ultra). Table of the six sources in processing order:
  1. `01a03492-84a8-7d20-b7bf-667a02b24479` "S6 Proof Audit, Reconstruction & Overleaf Release": 2,884 tree
     records, 845 with original JSONL history, 2,039 without ("explicit custody gap");
  2. `01a06ca0-...` (Geometric Unity / measured-fibre comparison; 62 records);
  3. `01a03c80-...` (earlier mass-gap comparison; 3 records; already archived by the Yang-Mills main);
  4. `01a066d4-...` (Nolan import; 42 records);
  5. `01a0814d-7c8a-...` (RH arithmetic quotient; 2 records);
  6. `01a0814d-89f0-...` (RH marked-factor correspondence; 1 record).
  Nine verified ZIPs in `C:\Users\user\Documents\interlanguage\old stuff\` with sizes and SHA-256 (the S6 audit
  ZIP is 17.9 GB, 62,477 members). First transfer: 35,461 text versions, 5,318 unique text blobs, 56,146
  statement/proof blocks, 1,440 canonical snapshot files, 9,957 dialogue messages, 1,596 unfinished/nonclaim routes.
  Status sentences are those of 29 Sep: "global S6 recognition and the original-zeta reconstruction remain open";
  "The first S6 main is a derivative reconstruction of a supplied PDF, not recovered original-author TeX".
  Stale against later files: says R1-R7 (the note has R1-R8) and 7,636 text versions (V2.1: 7,637).
- `RELATED_SOURCE_DISPOSITIONS.md` (5.6 K): sixteen other roots considered and left with their own mains
  (Yang-Mills volume-uniform and coarse-graining; three Navier-Stokes roots; GCT exact arithmetic; course operator;
  website discussion; Connes spectral quotient; Split-Zero/GCT; RH counterfactual; two withdrawn "identity-absorber
  square" explorations; two unrelated). One line each on why. "A routing match is a locator, not evidence that its
  proofs have been read."
- `FIRST_SOURCE_TRANSFER_RECEIPT.json` (1 K): the counts above.

#### 1.2 `mathematical_consolidation\` (30 Sep 2026; reader H read `MATHEMATICAL_NOTE.md`, `MASTER_MAP.md`,
`CLAIM_LEDGER.md`, `REVIEW_2026-09-30.md` in the public copy; see `H_notes.md` 1.3 and "Differences (a)")

- `README.md` (8.2 K, 30 Sep 10:10): reading order; five status words (proved here / bounded source reading /
  routed source claim / unmined / missing original history); corpus receipt V2.1 (71,426 direct entries; 214
  nested-package placements; 56 package versions; 12,822 file definitions; 29,324 logical occurrences; 7,637 text
  versions of which 1,282 TeX; 55,659 spans; 87,272 references); "New mathematics" = R1-R8 (quaternionic Gaussian
  material; nothing about X); scope boundary ("does not certify the historical global S6 candidate, an S6 sphere
  recognition ..."); publication at commit `5f358fb5...`.
- `WORKFLOW.md` (7.9 K): the request behind the consolidation (inventory every member of the nine ZIPs; structural
  TeX extraction; a coherent reader over eight lanes; concrete mathematics on the two marking conventions and the
  Gaussian/decoherence integration; claim ledger; figures) and the completion state of 30 Sep.
- `UNMINED_QUEUE.md` (9.3 K): Q1-Q10, each with "current evidence / next work / completion condition". The ones
  about X: **Q3 "close the analytic-candidate dependency chain"** (select the current candidate by source hash;
  reconstruct cover and chart domains, transition maps and cocycle identities, singular/exceptional/boundary loci,
  global topology and action, the maps from Leray and nearby-cycle data to the global invariants, the recognition
  theorem or its exact obstruction) and **Q4** (cusp operators: metric, domains, self-adjointness, then the
  receiving maps into the global candidate). Q1 (4,228 unrouted versions), Q2 (845 located histories; 2,039
  missing), Q5 (selector-to-Jordan-to-lattice maps), Q6 (extensions of R1-R8), Q7 (zeta/heat from the original zeta
  function), Q8 (finite-quantum cross-references), Q9 (opaque members), Q10 (synthesis) are not about X.
  Q3 is a statement about what this consolidation had re-read, not a gap in the canonical workbench.
- `AUDIT_LIMITATIONS.md` (8.7 K): what registration means; structural index (30,269 displays; 6,021 statement
  environments; 5,042 proof environments; 282 + 217 manual heading locators); "occurrences, versions and works
  differ"; lane counts (315 analytic-candidate, 371 cusp/spectral, 1,243 arithmetic-selector, 354 lattice/Jordan,
  538 quaternionic/gauge, 190 measured-fibre, 409 finite-quantum, 1,022 zeta/heat, 7 GCT, 23 primary S6, 8 YM, 2 NS;
  4,228 unclassified); actual reading coverage (four passages); "Claims expressly outside current acceptance"
  (global S6 identification, sphere recognition, global analytic atlas, ...).
- `CATALOGUE_GUIDE.md` (6.2 K): schema of `CORPUS_CATALOGUE_V2.sqlite` (191 MB; tables `versions`, `archives`,
  `archive_members`, `direct_text_occurrences`, `package_*`, `spans`, `references_found`, `topics`,
  `classification_*`) and seven read-only queries. Useful for a later checker: `spans` gives every theorem/proof
  environment of every TeX version by hash.
- `UNCLASSIFIED_TRANCHE_2026-09-30.md` (17.5 K) and `.json` (58 K): the 40 largest unrouted TeX versions, one cue
  line each: 23 "primary S6" (versions of the cumulative workbench/annotated edition, 568-662 K, cue "The period
  family over the thrice-punctured sphere"), 8 Yang-Mills spectral (`s6_spatial_continuum_draft.tex`), 6 "GCT /
  nonstandard RH bridge", 1 GCT IV source, 2 Navier-Stokes. Shows that the corpus holds about two dozen dated
  versions of the main S6 TeX (24 Aug - 9 Sep) under `nested_source_blobs\<sha>.tex`.
- `literature\CANONICAL_LITERATURE_ROUTING.json` (5.9 K): nine rows routed from the zeta literature index
  ("routing only; PDF routes not read"); `SOURCE_ACQUISITION.json`: the two arXiv sources read for R5-R6
  (Chruściński-Pascazio 1710.05993v2, Hornberger quant-ph/0612118v3). Nothing on complex geometry.
- `GITHUB_PUBLICATION_2026-09-30.json` (2.1 K): published and verified 30 Sep 08:07 UTC, commit `5f358fb5...`,
  46 remote files, byte checks of six files; `compiled_pdf_claimed: false`.
- Not opened: both sqlite catalogues, `ARCHIVE_MEMBER_COVERAGE*.jsonl.gz`, receipts, scripts, figures.
- `nested_source_blobs\` (3,296 files: 840 md, 805 tex, 753 json, 439 py, 301 txt, ...) and `v2_source_blobs\`
  (one 52.9 MB manifest): text blobs named by SHA-256, extracted from nested ZIPs. Grep results (on `*.tex`,
  `*.md`): "S6 record": none; "Engel": none; "Rollenske": 37 TeX (the workbench versions and preprints cite
  him); "integral monodromy": 14 TeX (higher-rung preprints, research logs, toroidal bridge) and 13 md;
  "proper test family": 8 research-log versions + `7260e5b4...md`; "Singular-Fibre Vanishing" (case-sensitive
  title): only `aca0913d...tex`.

#### 1.3 The correction note [N] — found, with companions

All five files of the original folder `C:\Users\user\Documents\math\output\s6_arxiv_preprint_draft_2026-09-01\`
are in `source_text_blobs\` (member paths from `ledgers\source_files.jsonl.gz`):

| file | bytes | blob |
|---|---:|---|
| `main.tex` | 39,045 (948 lines) | `source_text_blobs\aca0913df424f72b0efc94546498f1f427786191628503ff56208f4153060abb.tex`; identical copy at `mathematical_consolidation\nested_source_blobs\aca0913d....tex` |
| `ASSESSMENT.md` | 3,555 | `source_text_blobs\7260e5b435690dacee0e8f0d0e73be73998b8624d8eb690fa813a8567d6d1b56.md` |
| `README.md` | 4,592 | `source_text_blobs\7cc1900f2d19b927f021d1c3140d7b6c3453eb59949c313cdd7c44c64a566faf.md` |
| `references.bib` | 3,115 | `source_text_blobs\667494d934a6c681708d0d5e97e31a445e22b79ac20e1f93f8510f00485c1619.bib` |
| `00_s6_independent_correction_note_SHA256SUMS.txt` | 537 | `source_text_blobs\6d24be1c7f47....txt` (lists `main.tex` = `ACA0913D...`, the source zip `0BC908E2...`, the PDF `50B9AFE3...`) |

The `main.tex` hash is the one recorded for [N] in `courses\CG-S6\provenance.json`, so this is the cited text.
`\title{The Singular-Fibre Vanishing Step: An Independent Audit and Proper Test Family}`, `\author{Human author to
be supplied}`, `\date{1 September 2026}`, amsart; disclosure: "The local drafting and audit assistance used OpenAI
Codex gpt-5.6-sol, Ultra; no AI system is an author." I read all of it. Statements (numbering as compiled:
one counter per section):

- §1 Purpose and scope. **Lemma 1.1** (`lem:torsion-identification`): for a reduced effective Cartier divisor S in
  a smooth complex manifold, `ker(Omega^1_S -> j_* Omega^1_{S_reg}) = Tor(Omega^1_S)`.
- §2 The exact cotangent filtration. **Lemma 2.1** (`lem:conormal`): `0 -> N^*_{S/X} -> Omega^1_X|_S -> Omega^1_S -> 0`
  is exact on the left for S reduced (dvr argument at each minimal prime). **Proposition 2.2** (`prop:filtration`):
  with `K_S = ker(Omega^1_X|_S -> tilde Omega^1_S)`: `0 -> N^* -> K_S -> T_S -> 0` (2.4) and
  `0 -> K_S -> Omega^1_X|_S -> tilde Omega^1_S -> 0` (2.5). **Proposition 2.3** (`prop:criterion`): if
  `H^0(S, tilde Omega^1_S (x) A) = 0` and `H^0(S, N^* (x) A) = 0` then
  `H^0(S, Omega^1_X|_S (x) A) = ker( delta_A : H^0(S, T_S (x) A) -> H^1(S, N^* (x) A) )`. Remark 2.4 (Cech form).
- §3 A conductor-supported section (stated as a restatement of [AC26] Lemma 10.3, no priority claimed).
  **Lemma 3.1** (`lem:conductor`): `0 -> O_S -> eta_* O_{S~} + O_D -> eta_* O_{eta^{-1}D} -> 0` for a
  self-crossing surface. **Proposition 3.2** (`prop:conductor-differential`): if `eta^* A` is trivial and
  `eta^* theta_g` vanishes on `eta^{-1}(D)`, there is a unique nonzero `s in H^0(S, Omega^1_X|_S (x) A)` with image
  `(eta^* theta_g (x) e, 0)`; its image in `Omega^1_S (x) A` is torsion. **Corollary 3.3**: then `delta_A` is not
  injective.
- §4 The proper nodal-cubic test family: `C = { y^2 z = x^2 (x+z) + t z^3 } in P^2 x Delta`, `X = C x P^1`,
  `S = C_0 x P^1`. **Proposition 4.1** (`prop:family-geometry`): g proper, X smooth, S reduced irreducible
  self-crossing with normalization `P^1 x P^1`, `D = {[0:0:1]} x P^1`, local model `uv = t` with
  `u = y - x sqrt(1+x)`, `v = y + x sqrt(1+x)`; the other discriminant value is `t = -4/27`. **Lemma 4.2**
  (`lem:gluing-bundle`): `A_lambda` (gluing scalar lambda not a root of unity) has `nu^* A = O`, `H^0 = 0`, no
  torsion power. **Lemma 4.3** (`lem:extending-gluing`): with `O(t) = [0:1:0]`, `P(t) = [3 : sqrt(36+t) : 1]`,
  `B = O_C(P - O)` restricts on `C_0` to `A_lambda` with `lambda = 1/3` (from `f(r) = r - 2`, `f(1)/f(-1) = 1/3`).
  **Theorem 4.4** (`thm:nodal-test`): for `A = pr_1^* A_lambda`: `H^0(S, N^* (x) A) = 0`,
  `H^0(S, tilde Omega^1_S (x) A) = 0`, `H^0(S, Omega^1_X|_S (x) A) != 0`. **Remark 4.5** (`rem:scope`): A is
  non-torsion and extends; with `L~ = omega_X (x) A~^{-1}` it is the Serre-dual twist of the CDP argument; the
  family lacks the global hypotheses of CDP20 Thm 2.2.
- §5 The corrected reading of the CDP step; 5.1 derived criterion. **Lemma 5.1** (`lem:generic-endpoints`): Y
  compact connected of dimension n, D nonzero effective Cartier with `O(D) in Pic^0`, B a vector bundle, P an
  irreducible parameter space in `Pic^0` with a Poincaré bundle, stable under dualization and containing suitable
  `O(-mD)`, `O(-lD)`: then on a dense open subset `H^0(Y, B (x) P') = H^n(Y, B (x) P') = 0` (Krull intersection
  + Grauert semicontinuity + Serre duality). **Theorem 5.2** (`thm:corrected-global`): X compact connected
  threefold, `H^1(X;Z) = H^2(X;Z) = 0`, `a(X) = 1`, algebraic reduction a holomorphic map to a curve; if one `L_0`
  has `H^2(X, T_X (x) L_0) = 0`, then on a dense open `U` of `Pic(X) = H^1(X,O)`: `H^i(X, T_X (x) M) = 0` for
  `i = 0,2,3` and `c_3(X) <= 0` (via `chi(T_X (x) M) = c_3/2`). **Corollary 5.3** (`cor:relative`): it is enough
  that `R^2 f_*(T_X (x) L) = 0` for one L.
- §6 **Proposition 6.1** (`prop:relative-local`): `Omega^1_{R/C{t}}` for `t = xy` and `t = xyz` is torsion-free and
  not locally free at the origin (explicit embeddings in free modules, images `R dz + (x,y)e` and
  `R x e_1 + R y e_2 + R z(e_1+e_2)`); for `t = s^m`: `R dy_1 + R dy_2 + R/(s^{m-1}) ds`, the last summand the
  torsion. **Remark 6.2**: scope (total-space modules, `p = 1` only; ramified quotient charts need a separate
  invariant-module calculation).
- §7 Relation to the S6 reconstruction (records the candidate values `H^1 = H^2 = H^3 = 0`, `a = 1`, `c_3 = 2`;
  "not an adjudication of the candidate's existence").

`ASSESSMENT.md` ("Non-duplication assessment") is the note's own judgment: the conductor mechanism and the
coinvariant lemma are [AC26]'s; independent content = (1) the connecting map `delta_A`, (2) the proper test family
with `O(P-O)`, multiplier 1/3, (3) the local module correction, (4) the one-twist criterion; "The proper test
family is the only component that plausibly carries enough independent mathematical content to anchor a short
correction note." It also says the candidate values `h^{1,2} = 1` and the Hodge/Bott-Chern tables "still depend on
unstated global frame, saturation, base-change, or cup-map bridges" as of 1 Sep (later workbench entries mark them
VERIFIED). `README.md`: the bounded literature audit "found no occurrence of this specific equation together with
this proper-family endpoint test"; the Zenodo record named there is 10.5281/zenodo.22235524.

Relation to other readers: this is the document behind H-1 and G1b-1, -2, -3, -8; reader H did not find it
locally, reader G1b did. The research logs (`nested_source_blobs\4f522fe6...`, `6f72cf4a...`, `86a940ef...`,
`9f0b8a1c...`, `972b1a12...` and others) carry the line "Constructed an independent proper test family from a
smoothing of a ..." already in Round 0-1, i.e. the family predates the 1 Sep note (root dialogue line 9451,
about 25-26 Aug: "the explicit nodal-fibre counterexample").

#### 1.4 The paper [R] — not found

No copy or draft of "The S6 record and the integral monodromy of its (3,4,infinity) period system". Searches:
`source_text_blobs\` (6,245 files; `*.tex`, `*.md`, `*.txt`) and `nested_source_blobs\` for "S6 record",
"opus-5-5", "period system", "2609.38442", "Engel": no relevant hit ("S6 record" occurs twice in `source_text_blobs`
md files as part of "S6 record `22666541`"-type Zenodo bookkeeping; "Engel" only Friedrich Engel and unrelated
authors); `ledgers\source_files.jsonl.gz` member names for `opus`, `s6_paper`, `correction_note`. The only local
traces are the citations in `courses\CG-S6\provenance.json` and lesson 10 (as reader H reports). The corpus was
frozen on 28-29 Sep 2026 and [R] is dated 28 Sep, written by another model outside this corpus. Local material
on the integral monodromy that predates [R] is in 1.7 below (candidate I-1) and in the course lesson
`integral-monodromy-and-fundamental-group.md`.

#### 1.5 `related_sources\01a06ca0-cc7a-7ec3-ac8c-e21f2e047754\` — Geometric Unity and measured-fibre comparison
(Codex, GPT-5.6 Sol Ultra, 4 Sep 2026 13:34 - 5 Sep 00:14 UTC; 62 threads)

- `CONTINUING_SOURCE_LEDGER.md` (6.3 K), `ROOT_REQUESTS_AND_FINALS.md` (11 K, read in full: the requests and
  four final answers), `UNIQUE_TEXT_SOURCES.json` (1,358 versions, of which about 1,150 are copies of the S6
  canonical tree of 26 Aug and the rest the two comparison repositories), dumps (`exact_source_files`,
  `exact_statement_proof_blocks` 2,602 blocks, dialogues, database rows).
- `source_snapshot\geometric_unity_15d_bridge_20260904\` (53-page report; `chapters\`: `gu_core.tex` 22.6 K,
  `jordan_clifford.tex` 28.8 K, `cone_geometry.tex` 8.4 K, `model.tex` 21.9 K, `model_split.tex` 19.8 K,
  `nonlinear_observer.tex` 31.6 K, `curvature_contraction.tex` 19.1 K, `flat_gauge.tex` 27.2 K, `results.tex`,
  `scope.tex`; `handoff\`, `provenance\`, `sources\`, `verification\`).
- `source_snapshot\nolan_quaternionic_bridge_20260904\` (89-page report; `chapters\gaussian_fibres.tex` 14.9 K,
  `residual_measure.tex` 32.5 K (identical in both sources and to the repository antecedent), `kernel_projection.tex`
  36 K, `chirality.tex` 30 K, `operator_limits.tex` 9.5 K; `foundations\` = the GU chapters; `handoff\`).
- What it is: a comparison of the 15-dimensional algebra `J = Herm_3(H)` of the workbench's "quaternionic
  determining algebra" lane (not of X) with (i) Weinstein's 2021 draft and (ii) Nolan's "measured fibre" notes.
- `handoff\S6_INTRINSIC_MATH.md` (7.5 K, read in full). **"Intrinsic" means intrinsic to `Herm_3(H)` and its Moore
  cubic, i.e. independent of the Weinstein draft; it does not mean intrinsic to the threefold.** Five items:
  (1) `u(6) = R(sp(3)) + i R(J)`, `su(6) = R(sp(3)) + i R(J_0)`, `span[iR(J_0), iR(J_0)] = R(sp(3))`, and the
  infinitesimal normalizer of `R(J)` in `u(6)` is `R(sp(3)) + iR I_6` (proof given in the file);
  (2) every ordinary Jordan representation of J on a complex space has support rank divisible by 6, with
  signature `(6 l_+, 6 l_-)` in the self-adjoint case; (3) on the positive cone the Hessian of `-log N` is
  `g_H(K,L) = Re tr(H^{-1} K H^{-1} L)`, the level `N = 1` is a smooth 14-manifold; (4) an explicit flat-space
  `Sp(3)` scalar-gauge model with a null wave and a quaternionic instanton of action `2 pi^2/g^2` in its trace
  convention; (5) the "omitted-coordinate force" `rho_ddot(0) = -2 kappa` in the scalar mechanics.
- `handoff\S6_COMPLETE_MATH.md` (11.6 K, read in full): six source-attributed additions: the 14 = 4 + 10 bundle
  of Lorentzian metrics with vertical forms of signatures (3,7), (4,6) and a (7,7) split bundle, sectional
  curvature +1/2 on a vertical 2-plane over flat base; the Jordan map `H -> diag(-(i/2)R(H), 0_58, 0_64)` into
  `u(64,64)`, maximal support 120, no full-unit rank-three representation in dimension 128; the form
  `Q14 = det G + 2 Re(z^T eps w) + |rho|^2` of signature (7,7) and rank-5 equivariant maps; a rank-14
  submersion `H -> (G, -h)` with four-circle fibres, residual group `(U(1) x Q_8)/{±1}`, and non-descent of the
  cubic ("changes by 8 log 3"); a repaired curvature contraction `Omega^2(u(64,64)) -> Omega^13` reproducing the
  Einstein tensor on Levi-Civita spin curvature; ambient gauge lifts and the criterion `D_mu F_{rho sigma} = 0`.
- `handoff\CORRECTION_SENT_TO_S6.md` (3.6 K): withdraws the earlier instruction to leave out source-inspired
  results; `SENT_TO_S6.md` records delivery, not integration.
- Connection to X: none by a map. The link is the workbench lane that attaches `Herm_3(H)` to the S6 project by
  analogy and dimension counts. No candidate about X.

#### 1.6 `related_sources\01a066d4-d59c-7422-aef7-b6b0a100ab86\` — Nolan import and Gaussian fibres
(Codex, GPT-5.6 Sol Ultra, 3 Sep 10:33 - 5 Sep 16:50 UTC; 42 threads)

- `CONTINUING_SOURCE_LEDGER.md` (5.9 K), `ROOT_REQUESTS_AND_FINALS.md` (20 K; two finals: the import of nine
  public repositories of `mikalnolan`; a 10-page note "Quaternionic Gaussian fibres and exact information loss";
  then the unfinished request "Download the literature on decoherence and integrate it with this"),
  `HISTORICAL_GOAL_ROWS.jsonl`, `UNIQUE_TEXT_SOURCES.json` (168 versions).
- `source_snapshot\nolan_gaussian_fibres_20260904\main.tex` (34.4 K; the antecedent of R1, R2, R4-R7; statement
  list in `H_notes.md` 1.3) with worklogs, `literature\decoherence\` (18 PDFs, 552 pages by its manifest),
  `verification\`; `source_snapshot\nolan_quaternionic_bridge_20260904\` (copy; `handoff\S6_MATHEMATICAL_HANDOFF.md`
  8.4 K, read in full: Gaussian mass `Z(H) = pi^6/N(H)^2`, `E[qq^*] = 2 H^{-1}`, arcsine law of the cubic on the
  residual fibre with `E[N] = m`, `Var(N) = beta^2/2`, positive-cone image `a > 0, Delta > 0, m + beta > 0`,
  kernel/helicity counterexamples to statements in the imported notes, a commuting-sector Yang-Mills wave packet).
- Connection to X: none. This is the source of the consolidation's R1-R8 (reader H, H-7 to H-14).
  Unfinished by its own ledger: the decoherence integration, a stationarity/chirality paper, the upstream proposal.

#### 1.7 `related_sources\01a0814d-7c8a-71c1-b2b8-9c151927593b\` — "RH arithmetic quotient / three-point heat"
(Codex, GPT-6 Astra Ultra, 8 Sep 13:55 - 9 Sep 01:19 UTC; 2 threads; 52 M tokens)

- `CONTINUING_SOURCE_LEDGER.md` (3.4 K); `ROOT_REQUESTS_AND_FINALS.md` (282 K, mostly repeated machine goal
  text; I read the 24 final answers and the user requests that carry mathematics); `UNIQUE_TEXT_SOURCES.json`
  (1,793 versions; about 1,130 are again the S6 canonical tree); `ADDITIONAL_SOURCE_SNAPSHOT_MANIFEST.json`.
- `source_snapshot\`: `rh_arithmetic_resolvent_20260908\` (with `s6_three_points_heat\`, 158 files, the 90-page
  packet `three_point_bridge.tex` 51.9 K + 18 inputs), `connes_quotient_heat_transport_2026-09-08\`,
  `dbn_ns_rh_20260908\` (`tex\s6_three_point_quotient.tex`, `s6_three_point_forcing.tex`, `xi4_*.tex`, ...).
- What it claims (one sentence): typed maps from the three marked points and the monodromy of the S6 period system
  through a quadratic Fourier pullback and the September Navier-Stokes blow-up construction to an "arithmetic heat
  observable" whose Mellin transform is `xi`; it states repeatedly that no RH disproof, no zero-preserving map
  and no certification of the external Navier-Stokes proof is obtained.
- `S6_BRIDGE_STATUS.md` (8.1 K, two identical copies; read in full): "The current RH driver does not include a
  map from the S6 complex atlas, its holomorphic tangent bundle, its Dolbeault complex, or its global gluing data
  to the arithmetic trace quotient"; what is proved is `h_ar = 4 h_heat`, `T = 4S`, the isomorphism
  `(Bv)(u) = (1/4) e^{u/2} v(e^u)` of function spaces with `F_4 B T = Xi`, and a coordinate dictionary with
  `kappa = sqrt(1977)/54`. "Other bridges": an Erdős-Straus satellite gives a section of
  `lambda(l) = 12 l_0 - 4 l_1 - 3 l_2` with its rank-two kernel. Nothing here is about the complex geometry of X.
- Parts that are about the monodromy of X (read: `three_point_bridge.tex` lines 170-300 and
  `negative_monodromy.tex` lines 1-215):
  - `three_point_bridge.tex` §"The complete marked integral representation": `V = Z gamma + Z u + Z w + Z delta`,
    `T_1`, `T_2` (eq. T), `T_0 = (T_1 T_2)^{-1} = I + N`, `N^2 = 0`; **Theorem `thm:integral-quotient`** (the
    largest quotient of the `Delta`-module V on which `g_1, g_2` commute is `M = (Z/6) gamma + Z delta`, kernel
    `<6 gamma, u, w>`, shears `S_1(a,d) = (a+2d, d)`, `S_2 = (a-3d, d)`, `S_0 = (a+d, d)`); **Proposition
    `prop:dual-quotient`** (for the dual lattice `Lambda` the universal commuting quotient is the coordinate
    `gamma: Lambda -> Z` with kernel `<u^, w^, delta^>`, trivial action, twist vectors `v_1, v_2 -> 1, -1`);
    **Theorem `thm:alpha`** (`Delta^ab = Z/12` realised as `(Z/13)^x` by `(g_1,g_2,g_0) -> (3,5,7)`).
  - `negative_monodromy.tex` (12.5 K): **Theorem `thm:all-invariant-forms`** (all Hermitian forms invariant under
    `T_1, T_2` are `H(a,b)`; signature (2,2) for `a != 0`); eq. `period-negative-Gram`, `period-square` (the
    restriction to the period plane); a general remark that any nondegenerate Hermitian form making N self-adjoint
    on a 4-space has signature (2,2). See candidate I-1.
  - `global_marked_continuation.tex` (18 K): the Navier-Stokes source's rank-two Gauss hypergeometric local system
    (parameters `(h, h+1; 1/2)`, `0 < h < 1/100`) is irreducible and has no nonzero flat intertwiner with the
    rank-four S6 system in either direction; a covering-space transport is kept. Not about X itself.
  - `jacobian_negative.tex`: an independent coefficient check of `det DF = -2` and of the three points
    `P_0, P_+, P_-` with the same image for the July 2026 Jacobian counterexample ("Fable" in these files means
    that polynomial map; the "Fable fibre over (-1/4,0,0)" is its fibre).

#### 1.8 `related_sources\01a0814d-89f0-7361-8467-84ea74753ec3\` — "RH marked-factor correspondence"
(Codex, GPT-6 Astra Ultra, 8 Sep 13:55 - 9 Sep 01:18 UTC; 1 thread; 56 M tokens)

- `CONTINUING_SOURCE_LEDGER.md` (3.2 K); `ROOT_REQUESTS_AND_FINALS.md` (218 K; I read all 21 final answers);
  `UNIQUE_TEXT_SOURCES.json` (239 versions).
- `source_snapshot\rh_marked_arithmetic_action_20260908\`: `marked_arithmetic_action.tex` (75 K; "marked-factor
  correspondence on the arithmetic quotient"; not read) and `connes_blowup_check\` (190 files): the cumulative
  49-page `antiunitary_fable_s6_bridge.tex` (20 K + inputs) with seven S6 inputs, eight handoffs, work logs, check
  scripts (`check_homology_leray.py` 19 checks, `check_nearby_cycles.py` 18, `check_period_existence.py` 19,
  `check_logarithmic_boundary.py` 92, `check_cusp_boundary.py` 33, `check_s6_ns_lattice.py` 33,
  `check_s6_global_assembly.py` 12), `s6_source\` (the reconstructed packets and "authority" page renders).
- What it claims (one sentence): an "antiunitary / blow-up" comparison between the Jacobian-counterexample fibre,
  the S6 cusp, the Connes quotient and the forced Navier-Stokes construction; its finals say that no RH
  falsification, no zeta-preserving morphism and no independently certified Navier-Stokes counterexample is
  established.
- The seven S6 files (all 9 Sep 2026; they work from the reconstructed packets and page renders of the original
  PDF, each marks the local toric/logarithmic filling results as "source inputs"):
  - `s6_period_existence.tex` (6.9 K, read in full), (P25)-(P34): re-derivation of [AC26] §3: lift
    `j∘tau = F`, orders 3 and 4, the parabolic class P with **all six signed carriers**
    `(p,r) = (±1,0),(0,±1),(±1,±1)` before the marking `P = T^{-1}`; `tau g_0 = tau - 1`,
    `tau g_1 = (tau-1)/tau`, `tau g_2 = -1/tau`; affine law `mu g_1 = (1-mu)/tau`, `mu g_2 = 1 + mu/tau` with both
    orbit tables; difference sheaf `O(-1)`; `mu(z_1) = (2-rho)/3`, `mu(z_2) = (1-i)/2`;
    `phi_1 = 2 - 6(1-mu)^2/tau`, `phi_2 = -3 - 6 mu^2/tau`, cocycle sums zero, `beta = beta^part + c_0`;
    `det_R Pi = (Im tau) D`, D invariant, `D -> -infinity` at the cusp; `R_{g_1}, R_{g_2}`, cocycle law.
  - `s6_cusp_boundary.tex` (15.9 K, read in full), (B1)-(B15): (B1)-(B5) freeness, proper discontinuity,
    Hausdorffness of `N_0 = Y_eps/{Psi_lambda}` and properness of `f_0` with explicit constants (`B_t = B_0 +
    R(t)/log|t|`, `|B_t - B_0| < 1/2`), two distinct triple points `P_+`, `P_-`; (B6)-(B12) the degree-196 map
    (candidate I-2); (B13)-(B15) a Rees blow-up of `(z_0, z_1^2, z_2^4)`.
  - `s6_logarithmic_boundary.tex` (17.7 K; lines 1-80 and the handoff read), (L1)-(L24): `alpha_j(s,x) =
    (zeta_j s, A_j x + v_j/m_j)`, freeness from `gamma(v_j) = ±1`, smoothness/properness of `N_j`; the period
    complex structure `I_s` in block form and the logarithmic translation `D_j(s) = u_s v_j + r_s I_s v_j`; cluster
    tori of the labelled correspondence at `s = 0`.
  - `s6_ns_lattice_dynamics.tex` (16.6 K, read in full), (S1)-(S15): see I-2; contains the commutant (S10) and the
    explicit isomorphism `G_l = Z/pZ` (S12).
  - `s6_homology_leray_audit.tex` (6.4 K, read in full), (H1)-(H11): audit of [AC26] §7.4-7.7: `A_1, A_2, M_0`;
    van Kampen presentation (H3); `R = [[3, -l_1],[4, l_2 - 4 l_0]]`, `det R = -p` (H4); coinvariants
    `V_{G_0} = Z[delta]`, `(wedge^2 V)_{G_0} = Z[gamma delta]` with `[uw] = 6[gamma delta]`, degree three
    `Z[uw delta]`; `d_2(12 gamma) = p omega` from the three annular discrepancies (H8); `p'' = 2p - p'`,
    `|p'| = |p''|`, hence `p' = p'' = p` (H9); `H^1 = 0`, `H^2 = H^3 = Z/|p|` (H10). The Leibniz step is already
    [AC26] (transcription line 3181-3183).
  - `s6_nearby_cycles_audit.tex` (5.8 K, read in full), (C1)-(C13): audit of Appendix B: local models
    `f_0 = z_0, z_0 z_1, z_0 z_1 z_2`; nearby-cycle sheaves `H^0 psi = Z_W`, `H^1 psi = V` on D (ranks 1, 2),
    `H^2 psi = Z_P + Z_Q`; endpoint map `(n_1,n_2,n_3) -> (s,s)`, `s = n_1 - n_2 + n_3`; `H^q(W;Z) =
    (Z, Z^2, Z^4, Z^2, Z)`; `d(L) = (r,-r,r)`, `r = b_1+b_2+b_3-a` on `Pic(dP_6)`; `E_2` rank table (C12);
    only `d_2^{0,2}` has rank one, forced by the Gysin map of a free `T_f`-orbit; `im sp^q = (wedge^q V)^{T_0}`.
  - `s6_global_assembly_audit.tex` (4.5 K, read in full), (GA1)-(GA5): the quotient of `J + N_0 + N_1 + N_2` by
    the overlap maps is a compact connected complex manifold with proper f (given the source's local properness);
    `pi_1(X) = Z/|p|`; "Reversing the single global meridian orientation changes all three `l_i` simultaneously and
    leaves |p|; changing only one sign would be a different gluing datum, not a convention."
- So this source does contain an independent recomputation of the homology/Leray and nearby-cycle data, done by
  GPT-6 Astra on 9 Sep from the original text, separate from the canonical workbench (which was GPT-5.6 Sol,
  25-29 Aug). It reaches the same values and adds no statement beyond [AC26] and the canonical workbench in
  those parts (candidate I-3).

#### 1.9 `related_sources\01a03c80-d894-7fc2-8acb-5d1b2bd7bac2\` — earlier mass-gap comparison
(Codex, GPT-5.6 Sol Ultra, 27 Aug 17:46 - 28 Aug 14:24 UTC by the thread table; its two rollouts are dated 26 and
27 Aug; 3 threads)

- `CONTINUING_SOURCE_LEDGER.md` (3 K), `EXISTING_ARCHIVE_SCOPE.json`, `ROOT_REQUESTS_AND_FINALS.md` (108 K; I read
  the opening requests, the finals at raw lines 745, 2862, 4742 and the later exchange; the rest is repeated goal
  text and resource-limit messages), `UNIQUE_TEXT_SOURCES.json` (1,199 versions, all of them copies of S6 trees
  of 24-26 Aug: the source's own output folder `Papors\Chatnotes\Yang-Mills-Mass-Gap-Foundation\` belongs to the
  Yang-Mills main and is not in this transfer).
- What it is: the request to analyse `Im tau (Im beta - 6 (Im mu)^2 / Im tau) != 0` "as a mass gap condition".
  Final at raw line 2862: "In its native S6 setting it gives period/lattice nondegeneracy and an indefinite
  signature-(1,1) form—not positivity or a Millennium mass gap. On the additional locus `6 mu = a tau + b`, an
  explicit S6-to-elliptic quotient, kernel, integral basis change, and conditional base-fibre identity are
  proved." A later message (raw 5618) adds: kernel curve of modulus `tau_f = a mu - beta`, the condition equals
  `-Im tau · Im tau_f`, the class `eta = u∧w + 6 gamma∧delta` restricts to degree 6 on that fibre, Landau level
  spacing `12 pi / Im tau_f`. It claims no mass gap.
- Connection to X: a real statement about the regular fibres, but it is **already in the canonical snapshot**:
  `canonical_S6_snapshot\s6_spectral_degeneration_preprint.tex` Proposition `prop:descent` ("Exact descent
  criterion", lines 2157-2186) and `supporting_materials\workbench\research\cusp_spectral_geometry.tex` §"The
  exceptional first-coordinate elliptic quotient" (line 959 ff.; `status.tex` lines 1916-1941, VERIFIED, with the
  label action `g_0: (a,b) -> (a, a+b)`, `g_2: (a,b) -> (-b, 6+a)`). This source is where it first appeared
  (27-28 Aug). The readers of the canonical snapshot own it.

#### 1.10 `ledgers\`

- `actual_source_readings.jsonl` (57 K, 57 rows; keys `canonical_source_id, source_task_id, archive_sha256, member,
  read_lines, coverage, receiving_work, status, snapshot, source_file_sha256, recorded_date`): 40 one-line cue
  readings of the tranche; 8 full-file scope readings of the related sources; 3 "preamble and opening reader
  material only" readings of `main.tex`, `workbench.tex`, `workbench_and_manuscript_overview.tex`; 6 readings for
  R1-R8. So the consolidation of 29-30 Sep itself re-read none of the S6 proofs; its statements about S6 status
  are routing statements.
- `source_reading_use_ledger.json` (262 K): `coverage` for the 845 located histories (raw record and dialogue
  counts per thread), `raw_history_gaps` (2,039 thread ids), "transfer and routing only; actual proof reading to be
  recorded by passage".
- `unfinished_and_nonclaim_routes.jsonl.gz` (1.8 M): **1,596 records**, schema `source_task_id, archive_sha256,
  raw_member, raw_line, role, exact_text, status`; 790 assistant, 733 user, 73 developer messages from 629
  threads (530 from the root thread, raw lines 9 to 126,817); 11.0 M characters. These are whole dialogue
  messages selected by wording, not a list of open problems; status on every row "historical source text
  retained verbatim". I filtered assistant messages for geometry and unfinished-work words (292 records; 99 in
  the root thread, all read at 500-600 characters; the child threads sampled by keyword). The chronicle they give
  and the open items are in 1.11 and 2 (I-5).
- `source_claim_locators.jsonl.gz` (25.8 M): **56,146 records**, schema `archive_sha256, member, line,
  environment, exact_source_block, corpus_file, status, locator_method`; environments: 26,538 proof, 11,056
  theorem, 8,983 proposition, 3,996 lemma, 3,053 corollary, 1,994 remark, 217 definition, ...; only **4,374
  distinct blocks** (951 theorems, 582 propositions, 357 corollaries, 202 lemmas, 1,945 proofs): the rest are the
  same blocks in dozens of staged copies of the Overleaf tree. Largest files by block count: `cdp_program.tex`
  4,512, `s6_higher_rung_24d_preprint.tex` 2,503, `s6_cone_sphere_routes_preprint.tex` 2,284,
  `quaternionic_4441_reconciliation.tex` 2,042, `topology_reduction.tex` 1,440, `integral_leray.tex` 1,204,
  `candidate_geometry.tex` 1,016, `hodge_frolicher.tex` 798, `analytic_picard.tex` 780, `algebraic_dimension.tex`
  464, `bott_chern_algebra.tex` 360. The 7 distinct `conjecture` blocks: none about X (a Koide counting
  remainder `R(X) - C_0 X = O(X^{1/2+eps})`, a "four-Time" physics conjecture, five from GCT literature).
- Not opened: `projected_thread_items.jsonl.gz` (385 MB), `projected_thread_turns`, `source_files.jsonl.gz` was
  streamed only to resolve member names (35,461 rows; keys `archive_sha256, member, original_source_path, bytes,
  sha256, corpus_file, source_status, reading_coverage`).

#### 1.11 `custody\` and the first-check provenance

- `source_task_tree.json` (6.2 M): `source_id`, `threads` (2,884 rows, 42 fields each), `edges` (5,766).
  Root row: id `01a03492-84a8-7d20-b7bf-667a02b24479`, name "S6 Proof Audit, Reconstruction & Overleaf Release",
  rollout `rollout-2026-08-24T18-20-12-...jsonl`, created 2026-08-24 16:20 UTC, last update 2026-09-09 19:04 UTC,
  source `vscode` (Codex), cli `0.149.0-alpha.4.1`, 59.3 M tokens, model field `gpt-6-astra`, effort `ultra`.
  All other 2,883 rows are subagents of it. Models of the rows: 2,809 `gpt-5.6-sol`, 62 `gpt-6-astra`,
  8 `gpt-5.6-luna`, 3 `gpt-5.6-terra`; effort `ultra` on 2,835. By creation day (threads / tokens):
  24 Aug 21 / 126 M; 25 Aug 29 / 116 M; 26 Aug 19 / 80 M; 27 Aug 23 / 104 M; 28 Aug 37 / 347 M; 29 Aug 32 /
  214 M; **30 Aug 1,845 / 1,259 M**; 31 Aug 34 / 57 M; 1 Sep 51 / 398 M; 2 Sep 74 / 260 M; **3 Sep 340 /
  1,841 M**; 4 Sep 285 / 881 M; 5 Sep 47 / 218 M; 6 Sep 19 / 124 M; 8 Sep 20 / 90 M; 9 Sep 8 / 46 M. Total
  6.16 G tokens, of which 5.57 G on Sol/ultra and 0.40 G on Astra/ultra. Every subagent created 24 Aug - 4 Sep is
  Sol (a few Luna/Terra); the first Astra subagents are of 5 Sep (22 that day), and from 8 Sep all but one are
  Astra. The root row shows the model at capture time, so the root was moved from Sol to Astra around 5 Sep
  (inference from the subagent rows; the tree has no per-turn model record).
- The 2,039 missing original histories are exactly the subagent threads created 24-31 Aug (20 + 29 + 19 + 23 +
  37 + 32 + 1,845 + 34). For the first eight days — the first check, the topology, Picard and Hodge work — only
  the root thread's history is original; the subagents survive as projected rows and as their output files.
- `inherited_goal_state.jsonl` (4.2 K): one goal row for the root, created 8 Sep, status `paused`: "Primary research
  target, redirected by the user on 8 September 2026: construct and prove a counterexample to the four-dimensional
  quantum Yang-Mills mass-gap assertion ... This is a target, not an assumed conclusion", plus a request to test
  whether the "Alpöge/Fable counterexample mechanisms propagate through the Jacobian, claimed S6/CDP20 and recent
  Euler/Navier-Stokes work". So the root's S6 work ends in effect on 6-8 Sep.
- `FINAL_CUSTODY_AUDIT.json`, `archive_verification.json`, `source_history_coverage.json`: not opened.
- What did the first check, by the records:
  1. Before Codex (dates not in these files; `REVIEW_SOURCES.json` has `release_date 2026-08-24`): the PDF was
     transcribed in ten strips "in ChatGPT Professional Pro-mode sessions"; a first review saw only packet 06
     (source pages 56-66), ran 22 exact checks, recommended rejection because of the clash with CDP and found
     the error in Remark 7.28 (`(l_0,l_1,l_2) = (100,1,-1)` gives `p = 1199`); "Two independent ChatGPT
     Professional Pro-mode sessions performed full mathematical reviews" (Reviewer A, Reviewer B, 28 and 38
     checks; corrective reviews 25 Aug; Reviewer B follow-up 26 Aug). Source:
     `canonical_S6_snapshot\supporting_materials\project_documentation\PROJECT_README.md` lines 474-483 and
     `peer_reviews\README.md`, `REVIEW_SOURCES.json`. The Pro-mode model is not named in these files.
  2. The Codex root (first message of 24 Aug: the transcription ZIP `s6_canonical_108_pages_audited.zip`, the
     packet review ZIP, and the request to integrate and check them): "Codex then consolidated the sources and
     reviews, performed a third mathematical and TeX audit ... The Codex work used ChatGPT 5.6 Sol in Ultra mode."
     First subagents 24 Aug 16:24 UTC (nicknames Halley, Russell, Archimedes; then Goodall, Helmholtz, ...), all
     Sol/ultra. This agrees with the workbench disclosure. The public README's "GPT-5.6 Sol and GPT-6 Astra" is
     right for the whole period to 9 Sep and for the related RH sources; the first check and the proofs of
     26-29 Aug are Sol.
- Chronicle from the root dialogue (raw line numbers in brackets; dates as the messages state them):
  [3763-3975] first verdict: finite algebra consistent; cusp collapse, integral specialization, based van Kampen
  maps, identification of the Mayer-Vietoris/Leray matrices "remain unproved"; local errors in Proposition
  4.7(iv), Remark 7.28, Lemma A.3, `Lambda/Lambda-bar`, page 71. [7661] the conductor lemma is sound and "the CDP20
  page-692 sentence really does discard precisely the torsion-supported ambient differential". [9451] "the
  explicit nodal-fibre counterexample". [11602, 11725] cusp overlap closed by an explicit exponential quotient;
  construction VERIFIED. [13112] 26 Aug, 50-page workbench: construction, Leray route, S6 recognition, `a(X) = 1`,
  "theorem-level CDP counterexample" verified; Proposition 10.8 then proved [13294]. [25498] the Mayer-Vietoris
  route closed ("primitive and unimodular at p = -1"). [25895] Hodge diamond determined by `m = h^{1,2}`,
  Frölicher degenerates at `E_2`; [28287] `h^{1,2}_BC = 1` "against McHugh's published threefold formula",
  Bott-Chern and Aeppli diamonds. [51323] 29 Aug, 108-page workbench. [53818-55093] an analytic global proof of
  the Picard restriction (third route), after an adversarial audit "found two genuine local gaps" (linear versus
  logarithmic lifts; the wrong loop named as bounding a disc). [61018-65619] "no unresolved internal theorem: the
  remaining OPEN entries are provenance and external replication". [69863, 73623] 1 Sep: the correction note.
  [76329-90278] 2-4 Sep: cusp quotients and sphere carriers, higher-rung analogues (a rank-three toric lift with
  central fibre of Euler characteristic 6), the elliptic bridge. [102800-108265] 4-6 Sep: quaternionic model;
  `F_4/Spin(8)`; the class of the cusp map (`a = 0`). [117424] 8 Sep: Yang-Mills target.

#### 1.12 `source_dialogues\`, `source_text_blobs\`

`source_dialogues\`: one `.jsonl.gz` per located thread (845 files; the root's is 647 K). Not opened (the
unfinished-routes ledger gave what was needed). `source_text_blobs\`: 6,245 hash-named files (1,783 json, 1,509 md,
960 txt, 925 tex, 920 py, 39 lean, ...); used only for the greps in 1.3-1.4 and to read the note's companions.

---

---

### Reader H: The public repository (light reading) and its differences from the local workspace

Full notes: `work\H_notes.md`.


#### 1.1 Repository root

| File | Size | Date (content) | What it is |
|---|---:|---|---|
| `README.md` | 6.1 K | "last updated 16 October 2026" | Title "Yang–Mills, S6 and Navier–Stokes: an AI-produced mathematical research workbench". Three programmes; made by GPT-5.6 Sol and GPT-6 Astra ("PolyClank"); status paragraph; for S6 it points to `s6/STATUS_2026-10-05.md`. Credits: Alpöge (Jacobian counterexample of 20 July 2026; S6 manuscript), Tao's exposition, Engel arXiv:2609.38442, Sung-Jin Oh, OpenAI's Navier–Stokes paper. No licence file. |
| `WORKBENCH.md` | 13.8 K | 9 Sep, extended to 9 Oct | What each programme investigates. Its S6 section still has the pre-5-October wording ("does not independently certify a global complex structure on S6, a counterexample to CDP20") and no pointer to the status note (see §3, item 1). Summarises the 30 Sep S6 consolidation (R1–R8) and the YM continuation ("every equivariant linear colour map has one adjoint channel … magnetic density 48 … source `D^mu F_{mu j} = -16 T_j`"). |
| `ATTEMPTS.md` | 31 K | 9 Sep, with later additions | "What we tried, why, and where it was left": Navier–Stokes (reconstruction of OpenAI's "Finite Time Blowup for Navier–Stokes", fluid audits, coupled Boussinesq stages), Yang–Mills (incl. the entry `ym-s6-ns-moment-map`), Erdős–Straus routes (external repository), **S6 section** (five routes = the five sections of the key-advances reader: intrinsic fibration, period deformation, finite fillings, Niemeier–Leech cubic transport, literal common lattice), zeta routes (external repository). Machine-readable twin: `research-attempts.json` (90 K). |
| `RESEARCH_LOG.md` | 8.4 K | 9, 14, 16, 30 Sep | Publication history. 30 Sep entry: the S6 consolidation ("complete proofs R1–R8 … twenty exact groups and five numerical groups"; no PDF build). 14 Sep entry: the spectral-reconstruction continuation, "informed by the explicit mutually inverse S6 smooth normal-line trivialization". |
| `ATTRIBUTION.md` | 6.0 K | 21 Sep | Two inputs from Alpöge: (a) the Jacobian counterexample `F=(F_1,F_2,F_3)`, `det DF=-2`, three points with the same image — used in the "material-tensor branch"; (b) the S6 regular-fibre period matrix `Pi(z) = [[6mu, tau, 1, 0],[beta, mu, 0, 1]]` — used in the "period-dependent magnetic branch" (`yang-mills/sources/ym_gap_primary_20260908/retained_cusp_nonlinear_bridge.md` §1, `magnetic_translation_true_vacuum.md` §1 eqs (1.2)–(1.4), `ym_volume_uniform_astra_20260908/VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.md` §19). States that these uses "do not require an independent proof here of the completed threefold's identification with the six-sphere". |
| `ARCHIVE.md` | 1.6 K | — | Lists the preserved earlier root files (below). |
| `CONTRIBUTING.md`, `REVIEW_GUIDE.md` | 3.3 K, 4.0 K | 9 Sep | How to contribute / record a check. |
| `workbench.json` | 3.4 M | — | Machine catalogue of tracked files. |
| Preserved earlier root files | — | 8–9 Sep | `05_current_authored_ym_lanes_2026-09-09.zip` (5.4 M), `06_…README.md`, `07_…MANIFEST.json`; readers `quantum_coarse_graining_75p.pdf`, `quantum_interacting_tensor_band_71p.pdf`, `quantum_nonabelian_vertex_63p.pdf`, `volume_uniform_vacuum_77p.pdf`, `spatial_continuum_121p.pdf`, `spatial_continuum_127p.{md,tex,pdf}`, `spatial_continuum_129p.{md,tex,pdf}`; `navier_stokes_workbench_208p.pdf` (2.0 M), `navier_stokes_workbench.tex` (854 K), `navier_stokes_source_bundle.zip`, `navier_stokes_primary_manifest.json`, `navier_stokes_checks.json`; `check_fixed_coupling_analytic_disk_obstruction.py`, `scaled_angle_prescribed_kernel_rates.md`. No S6 content except that the spatial-continuum manuscripts use the S6 period block (below). |

#### 1.2 `s6\` (53 files, 33 MB; 27 MB of it is the public catalogue database)

- `s6\README.md` (3.1 K). **Status, 5 October 2026**: "The construction gives complex structures on S6 … a one-parameter
  family … each of algebraic dimension 1 … counterexample to the Campana–Demailly–Peternell theorem". Says the
  earlier caution "was misplaced". Points to the Zenodo archive of the frozen 6 Sep project (1,079 files, 174 MB ZIP,
  DOI 10.5281/zenodo.22678442; family 10.5281/zenodo.22235523; v1.2 10.5281/zenodo.22346462). The repository itself
  holds only the 5-page reader.
- `s6\STATUS_2026-10-05.md` (10.6 K). The corrected status note. Sections: Summary; 1 The family (E26 Thm 4.1,
  Engel's five construction steps, the fibration, invariants); 2 The false statements (CDP98 Cor. 4.2; CDP20 Thm 2.2
  with conclusions (a),(b),(c), Cor. 2.3; the Hirzebruch–Riemann–Roch argument `chi(X, T_X (x) M) = c_3/2 = 1` for every
  `M`; related failing statements CDP20 Lemma 4.2, Cor. 5.2, Prop. 5.5; what X does not contradict: CDP20 Thm 2.1 and
  [LRS]); 3 The inference that does not follow (CDP20 p. 692: conormal sequence used with `tilde Omega^1_S =
  Omega^1_S/torsion`; valid for normal `S`; at a reduced normal-crossings fibre one needs the extra hypothesis
  `H^0(tilde S, eta^* A) = 0`; two examples: a test family with central fibre (nodal cubic) x P^1, and the cusp fibre
  `W`, where `H^0(W, Omega^1_X|_W (x) A) = C` exactly; "what survives": if one `L_0` has `H^2(X, T_X (x) L_0) = 0` then
  generic vanishing and `c_3 <= 0` follow); 4 Earlier wording in this repository; References, including
  **[N]** "The singular-fibre vanishing step: an independent audit and proper test family", v1.0, file
  `00_s6_independent_correction_note_v1.0.pdf`, and **[R]** Claude (model claude-opus-5-5), "The S6 record and the
  integral monodromy of its (3, 4, infinity) period system", version 3, 28 Sep 2026, file
  `00-claude-opus-5-5-s6-paper.pdf`, both in Zenodo record 10.5281/zenodo.23003415. Neither document is in the
  repository. See candidates H-1, H-2 and the section "Differences" (c).
- `s6\ATTEMPTS.md` (10.6 K, 9 Sep, sixth section 30 Sep, last paragraph corrected 5 Oct). Cold-start account of six
  routes: 1 finite-fibre attachment maps (product covers of degree 9 and 8; full attachment kernel
  `<G~_j^{m_j} t_{-v_j}> = Z`; workbench Theorems 53.4, 53.6, 53.7, 53.9, `finite_filling_certificates.tex` FF1–FF46);
  2 intrinsic fibration (`omega_X = O_X(-2S_2)`, anticanonical ring `C[U,V]`, degrees 1, 2; Thm 53.17,
  `analytic_canonical_ring.tex` CR1–CR5); 3 deformation (`beta_c = beta^part + c`, `KS(d/dc) != 0`; Thm 53.18,
  `period_parameter_deformation.tex` PD1–PD18); 4 Niemeier–Leech cubic transport (value-group inclusions
  `diag(1,4,1)`, `diag(1,1,3)`, quotient `Z/12`); 5 Wilson's Leech lattice versus the retained embeddings
  (`Lambda_cyc ∩ L(N) = Lambda_cyc ∩ L(Lambda_L) = {sqrt2 (a,a,a): a in D_4}`, Gram `6 G_{D_4}`, det 5184, min 12);
  6 the 30 Sep consolidation. The opening paragraphs keep the old wording ("claimed to be the six-sphere"; "These
  local certificates do not, by themselves, establish the complete global identification with S6").
- `s6\S6_FROZEN_PROJECT_GUIDE_2026-09-09.md` (4.3 K) and `S6_FROZEN_PROJECT_PACKAGE_MANIFEST_2026-09-09.json`
  (2.7 K): guide and hashes of the 9 Sep packaging of the 6 Sep checkpoint (782-page cumulative workbench, 138-page
  higher-rung paper, 1,079 files, 221,140,515 bytes). Old wording kept as a dated record.
- `s6\27_s6_key_advances_frozen_2026-09-06.tex` (14.3 K) and `26_….pdf` (302 K, 5 pages), "Exact maps and analytic
  certificates: key advances", 6 Sep 2026. Five sections, each a statement with a proof locator into the frozen
  workbench (no proofs here):
  1. *The anticanonical ring recovers the fibration*: `f^*(p_1)=3S_1`, `f^*(p_2)=4S_2`; the evaluation
     `f^* f_* omega_{X/B} -> omega_{X/B}` has zero divisor exactly `2S_2`; `omega_X = O_X(-2S_2)`,
     `omega_X^{-2} = f^* O_B(p_2)`, `f_* O_X(kS_2) = O_B(floor(k/4) p_2)`;
     `(+)_{m>=0} H^0(X, omega_X^{-m}) = C[U,V]`, `deg U = 1`, `deg V = 2`; degree-two map
     `x -> [t(f(x))-1 : A + B'(t(f(x))-1)]`. Locator: workbench Thm 53.17, pp. 699–700; `analytic_canonical_ring.tex`.
  2. *The original period constant gives a nonzero deformation*: family `X_c`, `c` in discs inside
     `{Im c < -M}`, `M = max D_part`; exact marked map between period lattices, Beltrami matrix
     `nu_delta = delta/(2iD+delta) P`, KS class `-[ (1/(2iD)) d_{zeta_2} (x) (d zeta-bar_2 - (m/T) d zeta-bar_1) ] != 0`;
     global step via the intrinsic degree-two sections and the three fixed critical values; conclusion
     `KS_{X_{c_*}}(d/dc) != 0 in H^1(X_{c_*}, T)`. Locator: Thm 53.18, pp. 701–705; `period_parameter_deformation.tex`.
  3. *Finite fillings*: `kappa_1 = beta_1 + 2 mu_1`, `kappa_2 = beta_2 + 3 mu_2`, `E_j x F_j` product covers of
     degrees 9 and 8, deck-group presentation `Gamma_j = <Lambda, G_j | G_j t_lambda G_j^{-1} = t_{A_j lambda},
     G_j^{m_j} = t_{v_j}>`, kernel of `Lambda x|_{A_j} Z -> Gamma_j` equal to `<G~_j^{m_j} t_{-v_j}> = Z`, central;
     smooth trivialisation of the normal line `H_j(x) = exp(-2 pi i eps_j gamma(x))`. Locator: Thms 53.4, 53.6, 53.7,
     53.9, pp. 684–690; `finite_filling_certificates.tex`.
  4. *Niemeier–Leech transport retains the cubic arithmetic*: `R = A_5^4 ⊥ D_4`, Niemeier overlattice `N`,
     `[N:R]=72`, neighbour `Lambda_L = K + Z(rho_N/6 - alpha)`, value groups of `F = tau∘L`, `tau(q) = Re((q_1q_2)q_3)`:
     `V_F(N) = (1/27)Z + (sqrt2/54)Z + (sqrt3/18)Z`, `V_F(J)=V_F(M) = (1/27)Z + (sqrt2/216)Z + (sqrt3/18)Z`,
     `V_F(Lambda_L) = (1/27)Z + (sqrt2/216)Z + (sqrt3/54)Z`; Albert determinant
     `det Q_O(lambda; Ly) = lambda^3 - lambda(y,y) + 2F(y)`. Locator: higher-rung paper §§9–11, pp. 106–125.
  5. *A literal common lattice*: as in ATTEMPTS item 5; `tau(sqrt2(a,a,a)) = 2 sqrt2 a_0(a_0^2 - 3(a_1^2+a_2^2+a_3^2))`;
     generated group `4 sqrt2 Z`, value `12 sqrt2` not attained. Locator: higher-rung paper §12, pp. 125–135.
  Relation to LW: the five source files named (`analytic_canonical_ring.tex`, `period_parameter_deformation.tex`,
  `finite_filling_certificates.tex`, `es_niemeier_*.tex`) are all in
  `LW\canonical_S6_snapshot\supporting_materials\workbench\research\`; the 5-page reader itself is not in the local
  snapshot (no file contains its title). The reader is a pointer document; other readers of this survey cover the
  sources.

#### 1.3 `s6\consolidation\20260930\` (46 files) — the "S6 recent-results mathematical consolidation", 30 Sep 2026

Public derivative of `LW\mathematical_consolidation\` (see "Differences" (a)). Files:

- `README.md` (5.5 K): reading order; list of what is proved; corrected corpus model (56 package versions, 214 direct
  placements, 12,822 file definitions, 29,324 logical occurrences, 24,564 text occurrences; 41,695 direct text
  assignments checked); first routing tranche; scope ("does not certify the historical global S6 candidate …").
- `MATHEMATICAL_NOTE.md` (38.9 K), "Exact marking, measured fibres and Gaussian phase dynamics". "No novelty claim
  is made." Antecedents: the two files under `source\antecedents\`; cited sources Nolan (2025, GitHub), Hornberger
  quant-ph/0612118v3, Chruściński–Pascazio arXiv:1710.05993v2. Sections and statements (all marked "proved here"):
  - §1 **Proposition R1**: on `P = {H in Herm_3(H): H > 0}`, with the Moore cubic
    `N = a b lambda - lambda|v|^2 - b|q_1|^2 - a|q_2|^2 + 2 Re(q-bar_1 v q_2)`: `Z(H) = ∫ e^{-q^* H q} d^{12}x =
    pi^6 / N(H)^2`; real covariance `Sigma_H = (1/2) L(H)^{-1}`; `E_H[q q^*] = 2 H^{-1}`; `det L(H) = N(H)^4`.
  - §2 **Proposition R2**: with `P = [[1,-1,0],[0,1,-1]]`, `u=(1,1,1)^T`, `C = PP^*`, `R = P^* C^{-1}`, `X = (R u)`,
    `D = X^* X = diag(C^{-1}, 3)`: the two markings `Psi = X^{-1} H X^{-*}` and `B = X^* H X` satisfy `B = D Psi D`;
    unit Jacobians; Schur coordinates `c = u^* H u`, `l = c^{-1} b^*`, `S = A - c l^* l`, `N(H) = c N_2(S)`;
    pushforward `P_* mu_H = (pi^2/c^2) e^{-y^* S y} d^8 y`; conditional density; three fibres of dimensions 4, 9, 6;
    conditional KL loss `2[c_G/c_H - 1 - log(c_G/c_H)] + 2 c_G (l_G - l_H) S_H^{-1} (l_G - l_H)^*`.
  - §3 **Proposition R3**: on the residual circle orbits `N(H_theta) = m - beta cos t`, `beta = 2|rho||delta|`;
    positive point exists iff `m + beta > 0`; whole orbit positive iff `m > beta`; conditional mass average finite iff
    `m > beta`, and then `A Z = pi^6 m / (m^2 - beta^2)^{3/2} > pi^6/m^2`. Example `G = 4I`, `S_col = diag(2,1)`,
    `rho = 1/2 + i`: at `lambda = 104/59`, `m = 6`, `A Z = 3 pi^6/32`, ratio `27/8` to the mean-cubic value.
  - §4 **Proposition R4**: `psi_H = sqrt(p_H)` in `L^2(R^12)`; affinity `<psi_H, psi_G> = N(H)N(G)/N((H+G)/2)^2`;
    Fisher metric `I_H(K,L) = 2 Re tr(H^{-1} K H^{-1} L)`.
  - §5 **Proposition R5**: random-unitary phase channel `E^H_tau(rho) = ∫ U_tau(x) rho U_tau(x)^* dp_H(x)` on `C^d` is
    CPTP with multiplier `exp(-i tau(omega_a - omega_b)) exp(-(tau^2/4) b_ab^T L(H)^{-1} b_ab)`; factorisation through
    the Schur coordinates; observation-only couplings see only `S_H`.
  - §6 **Proposition R6**: the static family is a homogeneous semigroup iff all `b_a` coincide; it is CP-divisible
    (clock `sqrt(tau^2 - s^2)`); a separate Brownian family with covariance `tau_c tau Sigma_H` is a GKLS semigroup;
    noiseless blocks = classes `b_a = b_b`; units.
  - §7 **Proposition R7**: six points `v_0..v_5` in `H^3` give a 15x15 integer matrix `M_3` with `det M_3 = -4096`;
    four points `w_0..w_3` in `H^2` give `M_2` with `det M_2 = -16`; hence one six-level channel recovers `H`
    (15 parameters) and one four-level channel recovers `S_H` (6 parameters); minimality by a kernel perturbation
    and by `d(d-1)/2 >= 15`, resp. `>= 6`; witness family `H_r = I + ((r-1)/3) u u^*`, `N(H_r) = r`.
  - §8 **Proposition R8**: `J_p(m,beta) = (1/2pi) ∫_{f>0} (m - beta cos t)^{-p} dt`: zero for `m <= -beta`; finite
    iff `p < 1` for `-beta < m < beta`; finite iff `p < 1/2` at `m = beta`; for `m > beta`,
    `J_p = m^{-p} 2F1(p/2, (p+1)/2; 1; beta^2/m^2)`, and for integer `p`,
    `J_p = ((-1)^{p-1}/(p-1)!) d_m^{p-1} (m^2 - beta^2)^{-1/2}`.
  - §9 scope: none of this certifies the S6 atlas, a Yang–Mills gap or a zeta statement.
- `CONSOLIDATION.tex` (47 K): the same mathematics as standalone LaTeX (pandoc-generated; no PDF build claimed,
  `BUILD_STATUS.md`).
- `TOMOGRAPHY_DESIGN.md` (3.4 K) and `checks\TOMOGRAPHY_DESIGN_MATRICES.json`: the matrices `M_3`, `M_2`, Bareiss
  pivots, row swaps.
- `MASTER_MAP.md` (12.7 K): four evidence layers; "object chain" of lanes: 2.1 analytic and topological candidate
  (the workbench files `candidate_geometry.tex`, `topology_reduction.tex`, `integral_leray.tex`,
  `algebraic_dimension.tex`, `analytic_picard.tex`, `hodge_frolicher.tex`; "the final recognition arrow is unresolved
  in this consolidation"); 2.2 cusp and spectral lane (371 versions); 2.3 arithmetic selector and Jordan/lattice lane
  (Erdős–Straus, Koide, `p1201` bridge, Niemeier, Leech; 1,243 + 354 versions; Yokota's *Exceptional Lie groups* TeX
  recovered); 2.4 quaternionic carrier; 2.5 residual action; 2.6 finite quantum dynamics; 2.7 zeta/heat (1,022
  versions); 2.8 protected programme boundaries; table of R1–R8.
- `CLAIM_LEDGER.md` (11.5 K): MC-001 … MC-009. MC-001–005 are the corrections behind R2, R3/R8, R6, R7, R1/R4;
  **MC-006 "global S6 recognition remains a source claim … Status. Unresolved; no theorem accepted or rejected"**
  (30 Sep wording, superseded by the 5 Oct note but not edited); MC-007 original-zeta reconstruction pending; MC-008
  counts are not acceptance; MC-009 the catalogue defect.
- `RESULTS_2026-09-30.md` (4.2 K): result IDs SZ-20260930-005 (catalogue), -006 (integrated-phase semigroup, R6),
  -007 (tomography, R7), -008 (residual moments, R8). The same IDs are used for different results in the Yang–Mills
  continuation (§3, item 4).
- `REVIEW_2026-09-30.md` (5.4 K): the review of the 29 Sep draft; nine defects (nested-package model; verification
  scope; R7's 78 two-level experiments -> 13-level repair rejected -> six-level design; R6 lacked the separately
  defined `Y_tau`; terminology; malformed LaTeX; stale receipts; a hash collision; R8 endpoint).
- `AUDIT_LIMITATIONS.md` (8.7 K), `UNMINED_QUEUE.md` (9.3 K, Q1–Q10; Q3 "close the analytic-candidate dependency
  chain", Q4 cusp operators, Q5 selector-to-Jordan-to-lattice maps, Q6 extensions of R1–R8, Q7 zeta/heat),
  `CATALOGUE_GUIDE.md`, `SOURCE_RECORDS.md` (hashes and read line ranges of the two antecedents and the two arXiv
  sources), `BUILD_STATUS.md`, `PUBLICATION_MANIFEST.json`, `PUBLIC_VALIDATION.json` (replay: 20 exact groups, 5
  numerical, `M3_determinant -4096`, `M2_determinant -16`), `verify_consolidation_v2.py` (24 K),
  `verify_publication.py`.
- `checks\`: `MATHEMATICAL_CHECKS_V2.json` (names of the 20 exact and 5 numerical check groups),
  `UNCLASSIFIED_TRANCHE_2026-09-30.{md,json}` (the 40 largest unclassified TeX versions routed by one cue line each:
  2 Navier–Stokes, 6 "GCT / nonstandard RH bridge", 1 GCT IV primary source, 23 "primary S6 construction" (versions
  of the cumulative workbench TeX, 568–662 K each, cue "The period family over the thrice-punctured sphere"), 8
  "Yang–Mills cusp and spectral work" = versions of `spatial_continuum.tex`, pdftitle "The retained cusp, spatial
  refinement, and the spectral measure of the actual magnetic vacuum translation"), `DIRECT_TEXT_MAPPING_AUDIT.json`,
  `ENCODING_RECOVERY_RECEIPT.json`.
- `catalogue\`: `CORPUS_CATALOGUE_V2_PUBLIC.sqlite.gz` (27 M), `ARCHIVE_MEMBER_COVERAGE_V2_PUBLIC.jsonl.gz` (4.2 M),
  receipt, unpack script. Not opened (brief: no large dumps).
- `figures\`: four figures in pdf/png/svg (exact maps, mass and time laws, residual integrability map, tomography
  designs). `literature\`: `SOURCE_ACQUISITION.json`, `SOURCE_READING_LEDGER.jsonl` (55 K).
- `source\antecedents\quaternionic_gaussian_fibres_2026-09-04.tex` (34.4 K): "Quaternionic Gaussian fibres and exact
  information loss", "Local mathematical contribution; prepared with OpenAI Codex; not a Nolan-authored manuscript",
  4 Sep 2026. Abstract: "These are classical Gaussian mechanisms worked out as a source-inspired, reproducible
  example; no historical novelty or physical field-equation claim is made." Labelled statements: `lem:spectral`,
  `lem:differential`, `thm:gaussian` (exact mass and precision geometry), `prop:tilt`, `thm:disintegration`,
  `prop:conditionalmom`, `prop:KL`, `thm:KLloss`, `thm:Fisherloss` (six observed and nine conditional directions),
  `prop:gauge`; also `eq:paircubic`: `N(Theta(A,b)) = det_C A - b^* A b`. Byte-identical (SHA-256 `107932c0…`) to
  `LW\related_sources\01a066d4-…\source_snapshot\nolan_gaussian_fibres_20260904\main.tex`.
- `source\antecedents\residual_measure_2026-09-04.tex` (32.5 K): "A measured residual fibre for the marked
  quaternionic cubic"; `rm:fibre` (four circle components), `rm:hilbert-projection`, `rm:cubic-law`,
  `rm:positive-theorem`. Byte-identical (`c3c53021…`) to
  `LW\related_sources\01a06ca0-…\source_snapshot\nolan_quaternionic_bridge_20260904\chapters\residual_measure.tex`.

What R1–R8 have to do with S6: nothing geometric. The link is the "quaternionic determining-algebra" lane of the
workbench (the marked `Herm_3(H)` carrier and its Moore cubic, tied in the corpus to the Koide/selector/Jordan
material) and Nolan's "measured fibre" source; the note itself says that it "does not identify the existing S6
gauge action with a decoherence model".

#### 1.4 `yang-mills\continuations\20260930-s6-ns-moment-map-bridge\` (145 files, 14 MB; 29 Sep – 9 Oct 2026)

Title: "S6-reduced triality-to-profile bridge for the Yang–Mills gapless-state programme". Programme goal, stated as
a goal and not a result: construct a globally smooth interacting gapless state within the four-dimensional
Yang–Mills axioms and contradict the mass-gap statement.

- `README.md` (23 K, dated 8 Oct, with 9 Oct additions): summary of everything below and reading order.
- `SP1_BUNDLE_BRIDGE.md` (22 K, 29 Sep, corrected 30 Sep). Inputs taken from the higher-rung preprint: the based map
  `H = p_3 q_2 : X -> S^4` "from the original cusp coordinates", `[H d] = eta_4 eta_5 != 0 in pi_6(S^4) = Z/2`;
  the pulled-back quaternionic Hopf bundle `P_H = (chi H)^* S^7 -> X` with clutching class
  `c(P_H) = d[chi H d] != 0 in pi_5(Sp(1)) = Z/2` (source theorem `rettri:bundleclass`); adjoint bundle
  `A_H = P_H x_Ad Im H` with no nowhere-zero section; injection `rho: Sp(1) -> Spin(8)`,
  `rho(u) = (B_u, A_u, D_u)`, `B_u(a,b) = (u a u-bar, b)`, `A_u(a,b) = (ua, b u-bar)`, `D_u(a,b) = (a u-bar, b u-bar)`
  on `O = H + H l` (source theorem `rettri:subgroup`); `Q_H = P_H x_rho Spin(8)` trivial while the reduction is not
  (`rettri:forgetting`). New here: Prop. 2.1 (`phi(i,j,k) = 2(T_1,T_2,T_3)` is a Lie isomorphism scaling the metric
  by 4), Prop. 3.1 (no global colour frame), §4 (bundle-valued divergence-free profile space `U_H`; partial
  connection along `R^3`), Prop. 5.1 (a chart-supported non-Abelian profile; later demoted to "receiving space is
  non-empty"), Cor. 6.1.
- `PROOF.md` (28.6 K, 30 Sep): "Redo of the Sol 6 S^6, triality, and Yang–Mills bridge". Audit table of the 29 Sep
  claims; §4 the rank-24 bundle `W_H = V_r + V_q + V_p`, fibrewise `R^5_triv + Im H_Ad + H_L^4`;
  **Prop. 5.1** `Hom_{Sp(1)}(W, Im H_Ad) = R pi_Ad`, hence every equivariant linear map to adjoint-valued profiles
  is `a -> pi_Ad(a) (x) w` and `[A_i, A_j] = 0`; **Lemma 6.1** `mu_e(a) = a e a-bar` equivariant, `|mu_e(a)| = |a|^2`,
  differential of rank 3 off zero (`D mu D mu^T = 4|a|^2 I_3`); **Theorem 7.1** the map
  `M_H(zeta; alpha, beta; gamma, delta) = mu_i(alpha) (x) w^(1) + mu_j(beta) (x) w^(2) + mu_k(gamma) (x) w^(3)`,
  `w^(1) = curl(0,0,chi x_2)`, `w^(2) = curl(0,0,-chi x_1)`, `w^(3) = curl(0,chi x_1,0)`, is a global smooth
  fibrewise quadratic bundle morphism, zero set the rank-12 subbundle `V_r + L_{p,2}`, vertical ranks 0, 3, 6, 9;
  §8 core `(v_1,v_2,v_3) = (i,j,k)`: `F_12 = 2k` etc., `F_12 = 4T_3` etc., magnetic density
  `-2 sum_{i<j} tr(F_ij^2) = 48`; §9 source `J_j = sum_i [v_i, F_ij] = -8 e_j`, `D^mu F_{mu j} = -16 T_j`;
  Cor. 10.1; §11 list of what is and is not established. Later appended summaries of the next files.
- `HIGHER_CARRIER_AND_EVOLUTION.md` (30 K; `.tex` twin): **Thm 2.1** `D = F_4/rho(Sp(1))` (dim 49) fibres over
  `M = F_4/Spin(8)` (dim 24) with fibre `Spin(8)/rho(Sp(1))` (dim 25); a map `r_H: X -> D` with
  `r_H^*(F_4 -> D) = P_H`, `pi r_H` constant; Prop. 3.1 extension of the profile map; §4 a full connection
  (Maurer–Cartan projection); **Prop. 6.1** `A = C + s^2 S/2` preserves Gauss's law with residual
  `s^2 L/2 + s^4 Q/4 + s^6 N/8`; **Thm 7.1** homogeneous core ODE `V''_j = sum_i [V_i,[V_i,V_j]]` has global smooth
  solutions; equal-colour case `f'' + 8 f^3 = 0`, `f'^2 + 4 f^4 = 4`, energy density `24/g^2`; **Prop. 9.1** a
  smooth compactly supported static source-free connection with `A_0 = 0` has zero spatial curvature. Comparison
  source: Tsapalis–Politis–Maintas–Diakonos arXiv:1603.01858.
- `COMPACT_SUPPORT_CAUCHY_EVOLUTION.md` (36.5 K; `.tex` twin): **Thm 2.1** applies Sung-Jin Oh's global theorem
  (arXiv:1210.1557v2; local theory 1210.1558v2) to the compactly supported data `(C, 0)`; Prop. 3.1 support in
  `|x| <= R + |s|`; Cor. 3.2 agreement with the homogeneous solution on `|x| + |s| < r`; CE17 curvature-commutator
  witness `>= 128`; Prop. 4.1 energy zero set = the rank-12 subbundle; §§5–6 parameter dependence and bundle
  descent; §7 dilation; §8 link holonomies (CE42–CE45).
- `PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md` (241 K; `.tex`; `.pdf` 73 pages, 3.3 M): equations PK1–PK227. Read:
  header and §§1–3 (lines 1–335) and the section list. §2 **cusp period data**: `t_c = e^{-2 pi T + i phi}`,
  real period matrix `P = [[6a,u,1,0],[6m,L,0,0],[c_0,a,0,1],[-q,m,0,0]]`, `D = Lq + 6m^2 > 0`; monodromy
  `P(T, phi + 2 pi) = P M_0`, `M_0 = I + N_0`, `N_0^2 = 0` (PK3–PK4); `M`-fold covered torus, `det(P S_M) = -M^2 D`
  (PK8), inverse metric (PK9), singular-value and systole bounds `sys >= min(T - C_B, M)` (PK10–PK11),
  `D = T^2 + (2h_0 - d_0)T + (h_0^2 - d_0 h_0 + 6 m_0^2) + O(T e^{-2 pi T})` (PK12). §3: pullback of `P_H` to the
  covered cusp end; the restriction of `P_H` to the end `r_c < eps/2` is trivial (PK15–PK16); dual spectrum (PK18),
  lattice-point count (PK19), `4 pi^2/(T + C_B + M + ||A_per||)^2 <= Lambda_1 <= 4 pi^2/(T - C_B)^2` (PK20).
  §§4–9.35: lattice Yang–Mills (heat-kernel packets, Gram and Hamiltonian kernels on a finite open cubic lattice,
  electric layers, moments, "spectral escape"); statements list read only through `CURRENT_CLAIM_DISPOSITIONS.json`.
- `RESULTS_20260930.md` (11.4 K): SZ-20260930-001 … -014 (001 linear adjoint channel; 002 quadratic map; 003 core
  curvature and source; 004 scope of the reduction; 005 49-dimensional carrier; 006 connection; 007 Gauss-preserving
  correction; 008 homogeneous evolution; 009 static obstruction; 010–014 Cauchy evolution, support, energy,
  parameters, dilation/holonomy). `RESULTS_20261008.md` (3.5 K): SZ-20261008-001 … -005 (period matrix monodromy
  and covered bundle; physical heat packets and a reflection-odd vector orthogonal to the finite-lattice vacuum;
  corrected joint path, classical energy coefficient `400/(kappa_* j)`; first electric eigenspace at eigenvalue 3,
  next at 9/2; magnetic face sum and resolvent return). `RESULTS_20261009.md` (20.8 K): SZ-20261009-001 … -027,
  all lattice Yang–Mills (headings read; contents via the dispositions file).
- `CURRENT_CLAIM_DISPOSITIONS.json` (39 K): 49 records. The first eleven (`YM-S6NS-20260929-*`,
  `YM-S6NS-20260930-*`) are the corrections of the 29 Sep text, among them
  `YM-S6NS-20260929-SPIN8-LOW-DIMENSION` ("every continuous homomorphism Spin(8) -> G is trivial when G is a
  finite-dimensional Lie group of dimension below 28"); the rest are the SZ results with "proved_at_stated_scope".
- `HIGHER_DOMAIN_PROGRAM.md` (169 K; read: opening, §2, section list). §2 "What the S6 prototype actually supplies":
  real period matrix `P_R`, `delta_R = 6 m_R^2 - p_R T_R = R^2 + (2h_0 - d_0)R + (h_0^2 - d_0 h_0 + 6 m_0^2)
  + O(R e^{-2 pi R})`; marked fibre `F_R = R^4/P_R Z^4`, `Vol = delta_R`; N-torsion bijection and holonomy law;
  soft dual vectors `P_R^{-T}(r,s,0,0) = (0, (m_R r - p_R s)/delta_R, 0, (-T_R r + 6 m_R s)/delta_R)`;
  `lambda_1(F_R) = (4 pi^2/R^2)[1 + min{2(d_0 - h_0), -2 h_0}/R + O(R^{-2})]`; `N_R(E) = (E/4 pi) delta_R + O_E(R)`
  for `0 < E < 4 pi^2`; the decomposable operator `H_v` on `L^2([R_0, inf), dR; L^2_0(T^4))` has
  `0 in Spec_c ∩ Spec_ess`, `ker = 0`; Gaussian "quadratic" Hamiltonian with gap `s_N/R [...]`,
  `s_N = 2N sin(pi/N)`. Source of all this: `sources\s6_cusp\tex\satellites\29_s6_cusp_gauge_spectral_chain.tex`.
- `SPECTRAL_PROGRAM.md` (139 K; read: opening, section list): "Locally gapped, globally gapless Yang–Mills limits";
  two abstract spectral propositions and a toy model; cites the question in Claude's `y9_open.tex` line 12.
- `SOURCE_PROVENANCE.md` (23.8 K): hashes and read ranges; external sources Yokota arXiv:0902.0431 (Thms 1.16.2,
  2.7.1), Tsapalis et al. arXiv:1603.01858, Oh arXiv:1210.1557v2 and 1210.1558v2, Hall arXiv:1707.02355v1,
  Bahr–Thiemann arXiv:0709.4636v1, Dusson–Sigal–Stamm arXiv:2105.02058v1; the Clay problem page.
- Not read: `CLAIM_LEDGER.md` (186 K), `RESEARCH_PROGRAM_LEDGER.json` (42 K), `checks\*` (14 scripts and receipts),
  `figures\*`, `PUBLIC_MANIFEST.json`.
- `sources\` (20 files), copies of inputs. Comparison with LW by size and SHA-256 (first 16 hex digits):

  | Repository file under `sources\` | Bytes | Local copy | Same? |
  |---|---:|---|---|
  | `higher_rung\s6_higher_rung_24d_preprint.tex` | 301,399 (`8c526746de9b56a4`) | `canonical_S6_snapshot\s6_higher_rung_24d_preprint.tex` | identical |
  | `higher_rung\supporting_materials\workbench\research\higher_rung_24d_continuation.tex` | 303,964 | `canonical_S6_snapshot\supporting_materials\workbench\research\` same name | identical |
  | same folder: `common_d4_image.tex` 15,562; `es_niemeier_JM_cubic_extension.tex` 13,819; `es_niemeier_bibliography.tex` 3,028; `es_niemeier_cubic_arithmetic.tex` 23,513; `es_niemeier_leech.tex` 19,469; `es_niemeier_residue_fixed_neighbor.tex` 26,840; `es_niemeier_shared.tex` 79,366; `es_niemeier_triality_bridge.tex` 18,369; `es_niemeier_wilson_cyclic.tex` 35,241; `niemeier_umbral_shadow.tex` 28,148 | | `…\workbench\research\` same names | all identical (older variants of `es_niemeier_shared.tex` and `es_niemeier_bibliography.tex` also exist under `…\workbench\evidence\es_niemeier_20260905\`) |
  | `navier_stokes\GAUGE_AND_NAVIER_STOKES_BRIDGE.md` | 11,579 | `…\workbench\evidence\ym_sidebar_topics_20260908\quantum_blocking\` same name | identical |
  | `spatial\spatial_continuum.tex` | 414,920 (`e035407b…`) | `…\evidence\ym_sidebar_topics_20260908\spatial_continuum\spatial_continuum.tex`, 414,872 (`a879df6e…`) | **differs** (48 bytes; both hashes appear as ranks 31 and 32 of the unclassified tranche) |
  | `s6_cusp\tex\satellites\29_s6_cusp_gauge_spectral_chain.tex` | 110,505 | none found (file name and section label searched in `canonical_S6_snapshot\`, `related_sources\`, `courses\`) | repository only |
  | `s6_cusp\tex\satellites\29a_native_magnetic_upgrade.tex` | 26,358 | none found | repository only |
  | `claude\y6_side.tex`, `y9_open.tex`, `y9a_directions.tex` | 5,927; 3,160; 5,876 | none found | repository only |

  The three `claude\` files are sections of a Claude-written Yang–Mills paper ("The side branches: the Jacobian map,
  Navier–Stokes and S6"; "Questions, and what was not checked"). `y6_side.tex` says that the Yang–Mills lines need
  from the S6 data only the number `D = L_T q_T + 6 m_T^2` through `theta = 2 pi a^2/D`, and refers to "the companion
  S6 paper [SixSpherePaper], which also determines the monodromy group of the same period system" — that is [R].

**What is S6 mathematics here and what is Yang–Mills on top.**
S6 mathematics (all of it taken from, or restating, local files): (1) theorem `ret:main` of the higher-rung preprint
(lines 4470–5200): the map `H = p_3 q_2` — collapse of the cusp neighbourhood `0 < |t| < eps` onto
`Sigma(S^3)` using the coordinates `(r, phi, u_1, u_2)`, where `(u_1,u_2) = A(t)^{-1} log|x|` is the native quotient
to `T^2` and `phi = arg t` the "retained angle" — has class `eta_4∘eta_5 != 0`; its regular fibre is the 2-torus
`w(a,b) = (rho_0 e^{i(phi_0 - a - b)}, rho_1 e^{ia}, rho_2 e^{ib})` in one toric chart `C^3` of the cusp filling,
and the full frame is `D(a,b) G_0` with `D(a,b) = diag(e^{-i(a+b)}, e^{ia}, e^{ib}) in SU(3)` (candidate H-15);
(2) the consequences `rettri:*` (lines 5205–5800): the nontrivial `Sp(1)`-bundle `P_H`, the rank-three bundle
`A_H` without nowhere-zero section, the rank-24 "triality" bundle `W_H = P_H x_rho (O^3)` and its splitting — these
are formal once (1) is known, because principal `Sp(1)`-bundles over `S^6` are classified by `pi_5(S^3) = Z/2`;
(3) the cusp period data PK1–PK12 and `delta_R`, `lambda_1`, `N_R(E)`: elementary consequences of AC26
Prop. 3.21 (`Z = s B_0 + C(t_c)` with `h, mu, b` holomorphic at the cusp) (candidate H-19).
Yang–Mills on top: everything else. The "rank-24 triality bundle" is an associated vector bundle over `X = S^6`
whose only non-trivial datum is the class in `Z/2`; the Yang–Mills fields are functions on `R^3` with values in a
fibre of `A_H`, the base point of `X` being a parameter. Nothing in PROOF.md, HIGHER_CARRIER or COMPACT_SUPPORT
uses the complex structure of `X`, its fibration, or even that the base is `X` rather than any space with a
nontrivial `Sp(1)`-bundle. The period data enter only in PERIOD_COUPLING §§2–3 and in the older sources.

#### 1.5 Where else S6 enters the repository (grep for S6, S^6, six-sphere, Alp, Niemeier over md/tex/json)

Counts of matching files per folder: `yang-mills/consolidation/20260921-fifth-reference` 46,
`yang-mills/consolidation/20260921` 45, `navier-stokes/continuations/20260930-coupled-viscous-control` 44,
`yang-mills/continuations/20261011-central-signs-shrinking-window` 39,
`yang-mills/continuations/20260930-s6-ns-moment-map-bridge` 30, `s6/consolidation` 10,
`yang-mills/consolidation/20260916` 7, `yang-mills/sources/ym_spatial_continuum_astra_20260908` 5, others 1–3.

- `yang-mills\continuations\20261011-central-signs-shrinking-window\` (1,066 files, 79 MB: 1,022 at top level plus
  `fourth_return\`, `sources\temporal_transfer.tex`, `union_label_global\`; 349 json, 247 py, 163 png, 160 svg,
  145 md, 2 tex incl. `RESEARCH_CONTINUATION.tex` 4.3 M; README 133 K with 113 sections; results files
  `RESULTS_20261011…20261015.md`; 11–15 Oct 2026). "Yang–Mills phase moments and central link symmetry … It belongs
  to the S6 and Navier–Stokes inspired Yang–Mills programme." Content: SU(2) lattice Hamiltonian on open cubic
  boxes along the path `L_j = j^4`, `a_j = 1/(100j)`, `g_j^2 = kappa_*/(200j)`; phase observables in the actual
  vacuum, a central-sign involution, Schur returns, Hessian and covariance bounds; the positive low-energy weight is
  stated as not established. S6 enters in name only ("the full raw S6 phase", `RAW_S6_HESSIAN_RECEIVING.md`,
  43 K, RH1–RH51: "S6" labels the observable inherited from the programme) and through
  `JORDAN_MARKED_SLOTS_AND_PROFILE_MAP.md` (18.8 K, JMO1–JMO12): the three octonion slots of `h_3(O)`, products
  `mu_ij(a,b) = conj(ab)`, and the quartic profile map `N = M∘P`, `P(r,q,p) = (p-bar q, p r, q r-bar)`, built on
  lines 2104–2804 and 5400–5614 of the higher-rung preprint. No statement about the S6 threefold.
- `yang-mills\sources\ym_gap_primary_20260908\retained_cusp_nonlinear_bridge.md` (30 K, 8 Sep; `.tex` twin):
  §1 the covered period matrix `Q = R P_M = [[A, M I_2],[B, 0]]`, `B = [[6m, L],[-q, m]]`, `D = Lq + 6m^2`,
  inverse metric, two-form metric, Yang–Mills action on the fibre torus
  `S = (M^2 D/(2 g^2)) ∫ sum K_{I,J} c(F_I, F_J)`, flux value `2 pi^2 M^2/(g^2 D)`; §2 `sys >= min(T - C, M)` and
  transport of compactly supported connections into the fibre torus.
- `yang-mills\sources\ym_gap_primary_20260908\magnetic_translation_true_vacuum.md` (27 K, 8 Sep): "Only the explicit
  regular-fibre period and magnetic-bundle data are used; the claimed identification of a completed complex
  threefold with S6 is not an input"; eq. (1.4): magnetic links `h_1(n) = exp(-theta n_2 H_c)`,
  `theta = 2 pi a^2/D`, `D = L_T q_T + 6 m_T^2`. Copies in `ym_spatial_continuum_astra_20260908\sources\`.
  `weak_coupling_electric_graph_limit.md` mentions the same input.
- `yang-mills\sources\ym_spatial_continuum_astra_20260908\spatial_continuum.{md,tex}` and
  `sources\scaled_angle_native_limit.md`; `ym_volume_uniform_astra_20260908\VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.{md,tex}`
  §19: retain the magnetic construction; S6 = source of `D`.
  `ym_quantum_coarse_graining_astra_20260908\references\WEAK_COUPLING_ELECTRIC_GRAPH_INPUT.md`: one mention. The
  "Fabel/Jacobi" files there concern the Jacobian counterexample, not S6.
- `yang-mills\continuations\20260914-spectral-reconstruction\RESEARCH_NOTE.md` §7 "Smooth frames and the S6
  continuation mechanism" and `20260914-vacuum-refinement-infrared\RESEARCH_NOTE.md` §2.1 "The inspected S6 map":
  use the smooth normal-line trivialisation `H_j(x)` of key-advances §3 as a model for smooth frames with exact
  inverse. An analogy; no S6 statement.
- `yang-mills\consolidation\20260916`, `20260917`, `20260919`, `20260921`, `20260921-fifth-reference`: the hits are
  packaged copies of the files above (`package\history\…`, `CUMULATIVE_RESEARCH.md`) and attribution sentences.
  (`S6` also occurs as an equation tag in `20260915-gauge-native-band\SPATIAL_RETURN.md` and as the symmetric group
  in `20260917-quartic-cube\SIXTH_ENERGY.md`.)
- `navier-stokes\`: `README.md` (link to `../s6/`), `RESEARCH_STATE.md` ("initially investigated transfers from
  algebraic, S6-related and heat-flow constructions into fluids"),
  `continuations\20260919-vacuum-hydrodynamics\` ("No S6 edge was identified"),
  `continuations\20260930-coupled-viscous-control\` (hits in packaged sources and in
  `audits\claude-sources\contrib\claude-ab\rewrite\…`, a Claude-written audit of the Navier–Stokes material; no S6
  mathematics).
- `docs\polyclank\REPOSITORY_NOTES.md`: one navigation sentence. `releases\2026-09-09\README.md`: DOI table
  (S6: 10.5281/zenodo.22678442).
- No file in the repository contains "CG-S6", "integral monodromy", "23003415" other than `s6\STATUS_2026-10-05.md`.

#### 1.6 The remaining top-level parts (no assessment)

- `yang-mills\README.md` (122 K) and `AI_READING_INDEX.md` (135 K): opening and section lists read. Reading guide to
  "interacting SU(2) lattice gauge theory: the vacuum and its response to local couplings, ground energies, physical
  excitation spectra, and maps relating states and operators at different scales". Sections: full proofs and editable
  LaTeX; start reading; 14–16 Sep continuation; 9 Sep foundation edition; then about 60 dated sections (9–15 Oct)
  repeating the continuation summaries. Also `DEPENDENCIES.json`, `OMISSIONS.json`, `PUBLICATION_EDITS.json`,
  `READER_PROVENANCE.json`, `SOURCE_MANIFEST.json`, `yang_mills_current_sources_2026-09-09.zip` (6.2 M). Claims: explicit
  finite-lattice results (for example a lower bound for the full physical gap on open boxes at strong coupling,
  `g^2 >= 15`, later `g^2 >= 4.1156…` and `g^2 >= 3.68…`, uniform in the box). Does not claim the continuum mass
  gap or its negation.
- `yang-mills\consolidation\` (4,992 files, 286 MB): `20260916` (90 files; 14–16 Sep "web-session" consolidation,
  reader PDF/TeX, eleven preserved responses), `20260917` (51; fourth-order vacuum, sixth-order energy reader),
  `20260919` (18; sixth source, eighth energy, plaquette response), `20260921` (2,040 files, 128 MB; heat
  correlations and full physical complement; reader, archives, packaged history), `20260921-fifth-reference`
  (2,793 files, 134 MB; fifth-order reference, heat circle `|xi| < 1/55`).
- `yang-mills\continuations\` (1,443 files): twelve dated folders, 14 Sep – 15 Oct: `20260914-coupled-response` (8),
  `20260914-spectral-reconstruction` (2), `20260914-vacuum-refinement-infrared` (5), `20260915-actual-loop-moments`
  (8), `20260915-gauge-native-band` (15), `20260915-uniform-gap-zero-shift` (14),
  `20260915-zero-shift-local-fibres-review` (2), `20260916-cubic-linearized` (15), `20260917-quartic-cube` (29),
  `20260917-quartic-independent` (134), `20260930-s6-ns-moment-map-bridge` (145), and
  `20261011-central-signs-shrinking-window` (1,066).
- `yang-mills\readers\` (5 PDFs, 4.6 M): quantum coarse-graining (79 pp.), interacting tensor band (71), non-Abelian
  vertex (63), volume-uniform vacuum (81), spatial continuum (129). `yang-mills\research-control\` (8 files).
- `yang-mills\sources\` (234 files, 6.5 M; 8–9 Sep): `ym_gap_primary_20260908` (49 files; the "primary" lane: 25
  manuscripts in md, checks), `ym_quantum_coarse_graining_astra_20260908` (120), `ym_spatial_continuum_astra_20260908`
  (61), `ym_volume_uniform_astra_20260908` (4).
- `navier-stokes\` (722 files, 90 MB): `README.md`, `RESEARCH_STATE.md`, the 208-page "corrected reader" and its TeX,
  source bundle; `sources\openai-source-faithful-20260920\` (132 files; LaTeX reconstruction of OpenAI's 166-page
  "Finite Time Blowup for Navier–Stokes", with erratum D1 of 28 Sep); `continuations\20260919-vacuum-hydrodynamics\`
  (21 files); `continuations\20260930-coupled-viscous-control\` (559 files, 52 MB; coupled Boussinesq control
  calculations and a Claude audit). Claims a reconstruction with corrections and continuations; does not claim an
  independent certification of the blowup construction (the "infinite modified trajectory" is unfinished).
- `docs\polyclank\` (6 files, 60 K, 9 Sep): design notes for a network of self-describing workbenches (README,
  NETWORKING, PROBLEM_CATALOGUE, PUBLISHING, REPOSITORY_NOTES, RESEARCH_STATE); "proposed community protocol, not a
  deployed network".
- `tools\` (4 Python scripts, 60 K): build the continuation reader, package/verify a consolidation, update
  `workbench.json`.
- `releases\2026-09-09\` (4 files, 3.3 M): tree manifest, hashes, DOI correspondence table (Yang–Mills
  10.5281/zenodo.22678364; S6 10.5281/zenodo.22678442; Navier–Stokes 10.5281/zenodo.22678406), earlier descriptor.

---

#### Differences between the repository and the local workspace (reader H)


**(a) `s6\consolidation\20260930\` versus `LW\mathematical_consolidation\`.** They are the same edition. The local
folder is the working original: first version 29 Sep (files dated 29 Sep: `CATALOGUE_RECEIPT.json`,
`CONSOLIDATION_RECEIPT.json`, `MATHEMATICAL_CHECKS.json`, `CORPUS_CATALOGUE.sqlite` 79 MB,
`ARCHIVE_MEMBER_COVERAGE.jsonl.gz`, `build_catalogue.py`, `verify_and_illustrate.py`), corrected "V2" 30 Sep
05:15–06:01 (the reader files and V2 receipts), and published the same morning:
`LW\mathematical_consolidation\GITHUB_PUBLICATION_2026-09-30.json` records commit `5f358fb5…`, 46 remote files, and
the byte sizes and hashes of the published `README.md` (5,479), `MATHEMATICAL_NOTE.md` (38,864,
`8f037908…`), `CONSOLIDATION.tex` (47,268) — exactly the files in the clone. The local `MATHEMATICAL_NOTE.md`
(40,166 bytes, 30 Sep 05:59) already contains R1–R8; there is no separate local file with only R1–R7 (the 29 Sep
state survives only in the V1 receipts and in `REVIEW_2026-09-30.md`). Neither side is newer in mathematics. After
replacing `\( \) \[ \]` by `$`/`$$`, the differences are: `MATHEMATICAL_NOTE.md` 5 changed lines (antecedent paths:
local `../related_sources/…/main.tex` and `…/chapters/residual_measure.tex`, repository `source/antecedents/…`; four
figure links `.pdf` locally, `.png` in the repository); `TOMOGRAPHY_DESIGN.md` none; `CONSOLIDATION.tex` 2 lines
(the same paths); `MASTER_MAP.md`, `CLAIM_LEDGER.md`, `AUDIT_LIMITATIONS.md`, `UNMINED_QUEUE.md`,
`CATALOGUE_GUIDE.md`, `REVIEW_2026-09-30.md` only file-name references (public catalogue names, `checks/` prefix,
`PUBLICATION_MANIFEST.json` for `CONSOLIDATION_RECEIPT_V2.json`); `BUILD_STATUS.md`, `MATHEMATICAL_CHECKS_V2.json`,
`TOMOGRAPHY_DESIGN_MATRICES.json`, `DIRECT_TEXT_MAPPING_AUDIT.json` and all figures identical;
`UNCLASSIFIED_TRANCHE_2026-09-30.{md,json}` and `ENCODING_RECOVERY_RECEIPT.json` differ by the removal of
account-specific paths; `README.md` rewritten for the public (5.5 K against 8.2 K locally);
`verify_consolidation_v2.py` 3 lines. Repository only: `RESULTS_2026-09-30.md`, `SOURCE_RECORDS.md`,
`PUBLICATION_MANIFEST.json`, `PUBLIC_VALIDATION.json`, `verify_publication.py`, `catalogue\*_PUBLIC*`,
`source\antecedents\*` (copies of local `related_sources` files, byte-identical), `literature\SOURCE_READING_LEDGER.jsonl`
(local: `LW\ledgers\actual_source_readings.jsonl`). Local only: the V1 files, the private databases
(`CORPUS_CATALOGUE_V2.sqlite` 191 MB), `WORKFLOW.md`, the build/repair/classify scripts, `literature\` with the two
arXiv source archives, `nested_source_blobs\`, `v2_source_blobs\`.

**(b) The S6 project itself.** The repository holds only the 5-page key-advances reader (PDF and TeX), the guide and
the manifest of the 6 Sep checkpoint, and links to Zenodo for the 1,079-file archive. The local workspace holds the
project (`canonical_S6_snapshot\`: `workbench.tex` and its inputs, ledgers, the original transcription, the
preprints). The 5-page reader is not among the local files; the four source files it cites are. In the other
direction, the continuation's `sources\higher_rung\` copies thirteen local files byte for byte (table in §1.4), and
the local snapshot's `s6_higher_rung_24d_preprint.tex` already contains the "retained cusp" sections (H-15), so the
local snapshot is at least as late as the version used on 29 Sep.

**(c) The documents [R] and [N].** No copy found locally: no file name in `LW` or in `C:\Users\user\Documents`
(depth 3) matches `opus-5-5`, `s6-paper`, `S6 record`, `correction_note`, `23003415` (the two `opus-5-5` hits are an
unrelated transcription pilot). Text hits: `LW\courses\CG-S6\provenance.json` lines 428–466 (records
`S6-CORRECTION-NOTE-Z23003415`, title "The singular-fibre vanishing step: an independent audit and proper test
family", SHA-256 `aca0913d…`, URL `https://zenodo.org/records/23003415/files/00_s6_independent_correction_note_source_v1.0.zip`,
labels `lem:extending-gluing`, `thm:nodal-test`, `thm:corrected-global`, `prop:relative-local`; and
`S6-REVIEW-Z23003415-SECTION5`, "The S6 record, Section 5: correction note and relative differentials", SHA-256
`4c1a863d…`, URL `…/00-claude-opus-5-5-s6-paper-source.zip`, member `s6/paper/s6/s5_correction.tex`, labels
`prop:normal`, `prop:kernel`, `prop:sharp`, `thm:derived`, `prop:torsion`; "kind: retained programme derivation; not
original-human-author literature"); `LW\courses\CG-S6\src\non-normal-fibres-and-vanishing.md` lines 413 and 481
(the lesson re-derives the content); `CG-S6-10.html`. So the mathematics of [N] and of [R] §5 is present locally
in lesson 10, and the test family's origin is recorded in the local `research_log.tex` (lines 149–154); the other
part of [R] — "the integral monodromy of its (3,4,infinity) period system" — has a local counterpart in
`LW\courses\CG-S6\src\integral-monodromy-and-fundamental-group.md` and `checks\verify_integral_monodromy.py`,
`MONODROMY_GROUP_CHECKS.json`, but I found no local statement that is identified as [R]'s monodromy theorem. A
later checker who wants [R] and [N] themselves must fetch the Zenodo record.

**(d) The course `LW\courses\CG-S6\`** (files dated 8–11 Oct; eleven lessons plus about 45 companion chapters in
`src\`) is not in the repository: no path or text (md, json, tex) in the clone contains "CG-S6", the course title
"Complex threefolds from marked torus families", or the lesson-10 title or file name. Confirmed.

**(e) Wording on the status of the S6 result.**
- Repository, corrected 5 Oct: `s6\README.md` ("The construction gives complex structures on S6 … That caution was
  misplaced"), `s6\STATUS_2026-10-05.md`, last paragraph of `s6\ATTEMPTS.md`, root `README.md` ("For the S6
  construction, see the 5 October status note").
- Repository, still cautious (older dates): the places listed in §3 item 1.
- Local workspace: `LW\README.md` (29 Sep) is neutral ("Transfer and routing do not establish new independent proof
  acceptance"); `LW\mathematical_consolidation\` has the 30 Sep wording identical to the repository's consolidation
  (MC-006 "Unresolved; no theorem accepted or rejected"; "does not certify the historical global S6 candidate");
  the canonical snapshot's ledgers are of early–mid Sep. The local course (8–11 Oct) is written as a development
  of an established construction ("lesson 7 now includes the full integral homology, original homotopy equivalence
  and smooth recognition"; lesson 10 "exact comparison with the 1998 and 2020 statements") while stating "no
  independent whole-course review is claimed". The explicit sentence "CDP20 Theorem 2.2 and Corollary 2.3 are
  false" with the list of failing conclusions appears, among the places I read, only in the repository's status
  note (and in AC26 itself).
- One more difference of content: the repository's status note attributes the sharpened statements to [R] and [N];
  the local course presents the same statements as "existing results, independently calculated in this lesson".
