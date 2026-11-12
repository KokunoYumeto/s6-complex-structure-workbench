# A0 notes: the first check of the original S6 manuscript [AC26]

Reader A0, 12 Nov 2026 (Claude Fable 5.2). Base folder for all relative paths:
`C:\Users\user\Documents\math\research\s6_recent_results_main\canonical_S6_snapshot\` (all files there are
dated 29 Sep 2026 on disk; internal dates are given below). "Original" means
`original_clean_transcription.tex` (567,706 bytes; line numbers below refer to it). "WB" = the workbench
(GPT-5.6 Sol in Codex). "VERIFIED" in quotation of the WB means only that the WB gives it that label.

Short answer to the assignment. The first check found **no error that touches a theorem of [AC26]**. It found
four or five local slips (one false side remark, one variance slip in an appendix proof, one typo, one loose
quantifier, one sentence the audits call wrong but which I read as correct), and several places where the
original leaves a step unproved or resting on another route. All main conclusions of [AC26] survive in the WB.
The mathematics the first check *added* is in the CDP part (an exact criterion and an independent test
family for the failing step, a statement of what survives of CDP20), in the comparison of the two topology
routes (maps identified, signs made absolute), in three topology-free proofs of the line-bundle input to
Theorem 10.5, and in the Hodge computation that [AC26] left open (h^{1,2} = 1). Engel's paper closes the
"external adjudication" item for the existence and the topology only.

---

## 1. Reading notes

### 1.1 Audit annotation sources (`supporting_materials\audit_annotation_sources\`)

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

### 1.2 Peer reviews (`supporting_materials\peer_reviews\`)

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

### 1.3 Workbench status files (`supporting_materials\workbench\research\`)

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

### 1.4 Pro-mode feedback files (`supporting_materials\workbench\`)

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

### 1.5 Root files and history

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

### 1.6 What the 5 September re-audits say (they bear on how far to trust "VERIFIED")

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

## 2. Table: every error, gap or imprecision the audits found in the original [AC26]

Severity: A = affects a stated theorem; B = false statement not used later, or a real slip in a proof whose
conclusion stands; C = wording, typo, compressed step; D = exposition or citation request. "Survives" = does
the original's conclusion survive, according to the WB.

| # | Place in [AC26] (line in transcription) | What the audits say is wrong or missing | Sev. | Found by / date | Disposition and locator in the WB | Survives? |
|---|---|---|---|---|---|---|
| 1 | Remark 7.28, p.63 (l. 3197): "thus \|p\|=1 iff (l_1 mod 3, l_2 mod 4) in {(1,3),(2,1)}" | False as a biconditional for a fixed triple: (100,1,-1) has residues (1,3) but p = 1199. Must be: for fixed admissible (l_1,l_2) there is an l_0 (unique) with \|p\|=1 iff the residue pair is listed. | C | packet-06 review, A (E-01), C (ERR-006); 24 Aug | REFUTED S6-LOCAL-728; `local_repairs.tex` item 2; ledger line 35 | Yes. The sentence before it in the original says "l_0 is the free gluing parameter", so the existential reading is the natural one; the example (0,1,-1) vs (0,1,1) is right. I checked: p = -(4 l_1 + 3 l_2) mod 12, and = -1 iff (l_1,l_2) = (1,3) mod (3,4), = +1 iff (2,1). |
| 2 | Prop. 4.7(iv), p.30 (l. 1508): "the image is closed in N_0 because sigma is proper over Delta_eps (f_0 being proper, sigma(closed disc) is compact for every eps_1 < eps)" | "Proper over the open disc" is "not the appropriate reason"; use the closed-graph / equalizer argument. | C | A (E-02; A places it on pp.32-33, C corrects to p.30); 24 Aug | "VERIFIED" repair `local_repairs.tex` item 1: s(B) = {x : s(f(x)) = x} is closed in a Hausdorff space. Research log Round 10 keeps this repair against the 18-page branch. | Yes. **My reading: the original argument is correct as printed.** The parenthesis says sigma(closed disc of radius eps_1) is compact for all eps_1 < eps; a subset of N_0 whose intersection with each f_0^{-1}(closed disc) is compact is closed, since the open sets f_0^{-1}(open disc) cover N_0. The words "f_0 being proper" are superfluous, not wrong. The audit finding is an over-reading. |
| 3 | Lemma A.3, p.98 (l. 5116-5127): Mayer-Vietoris "H_k(W) -> H_k(W~) (+) H_k(D) -> H_k(D~) -> H_{k+1}(W)" | The arrows and the maps computed (intersection numbers D.C_k) are cohomological; the label H_k is wrong. Replace by H^k and finish by universal coefficients. | B | C (ERR-008, "major, repairable"); confirmed by A on 25 Aug (C-08: corrected 6x7 matrix has rank 4, Smith diag (1,1,1,1)) | "VERIFIED" repair `local_repairs.tex` item 3; Appendix B of the original already uses the right direction. | Yes: H_*(W) = (Z, Z^2, Z^4, Z^2, Z). I checked the original text: the sequence is printed exactly as the audit says. The same proof has a display that ends "cong {}" with nothing after it (l. 5127), not mentioned by any audit; either a transcription loss or an unfinished display in the PDF. |
| 4 | Remark A.6, p.100 (l. 5262): "pi_1(N_0) = Lambda = pi_1(W)" | Must be Lambda-bar = Lambda/Lambda_tor (rank 2), as in Cor. 4.8 (l. 1511) and l. 2043. | C | C (ERR-007); 24 Aug | "VERIFIED" repair `local_repairs.tex` item 4. A (25 Aug) "did not locate" it in the passages it inspected. | Yes (typo). Checked in the original: printed as the audit says. |
| 5 | Remark 1.3 (l. 270) and Remark 9.21 (l. 4330): "the sheaves Omega^p_{X/B} along the three singular fibres, where they have torsion"; "Omega^1_{X/B} has torsion along W u S_1 u S_2" | False at the cusp fibre W: for t = xy and t = xyz the module Omega^1_{X/B} injects into the free logarithmic relative module; it is torsion-free but not locally free there. Torsion only at the two multiple fibres: after t = s^m it is (R/(s^{m-1})) ds. | B | WB, Rounds 15, 17, 20 (27-28 Aug) | REFUTED S6-HODGE-CUSP-TORSION (ledger line 56); `status.tex` l. 1179-1200; `hodge_frolicher.tex` (11.17a-f); `local_repairs.tex` item 6 | The remark is not used in any proof of [AC26] (it describes a computation "not done here"). The WB's statement is right: O^n/(a) is torsion-free iff gcd of the entries of a is 1, and (y,x), (yz,xz,xy) have gcd 1 while m s^{m-1} does not. |
| 6 | Lemma 9.10(ii) / section 9.2 (l. 3626-3661), finite fibres | `local_repairs.tex` item 7: the invariant canonical section sigma_j = s_j^{m_j-1-a_j} e^{phi} ds_j ^ e has divisor (m_j-1-a_j) S_j after descent, so for j=2 it is not a nowhere-vanishing frame; the right statement is f_{j*} omega_{N_j/D_j} = O . s_j^{k_j} theta'_j. | C | WB (26 Aug or later) | `analytic_picard.tex`, `lem:hodge-line-audit`; `status.tex` l. 951-979 | Yes: f_* omega_{X/B} = O(1), K_X, direct images unchanged. **I could not find the defective sentence in the original**: l. 3636 says correctly "the invariant form descends, and its divisor is k_j S_j". This may be a repair of the WB's own earlier wording. |
| 7 | Lemma 9.6 (l. 3510-3530), descent of meromorphic functions | Omega := f^{-1}(B^o) minus the polar set is called "connected" without proof; the last step (extension of phi over the finitely many omitted points) lacks a "root estimate". | C | WB Round 5 (25 Aug) | `algebraic_dimension.tex`, `lem:meromorphic-descent-audit`; "Disposition" l. 292-299 | Yes: M(X) = f^*C(t), a(X) = 1. |
| 8 | Prop. 9.5 / Prop. 9.7: a 2-torus with NS = Z eta, eta of signature (1,1), eta^2 = 12, has a = 0 | The classification fact used (a = 2 needs a positive class, a = 1 needs a nonzero isotropic semipositive class) is "compressed"; cite or prove. | D | A (R-05) | WB proves it with an explicit Appell-Humbert matrix bridge: `prop:very-general-torus-audit` | Yes. |
| 9 | Remark B.4 (l. 5595): sp^q = c^*, the generators of H_2(W), the normalisations sp^2(T_B^v) = gamma ^ u etc. "are not re-proved here and continue to rest on 7.2 and Proposition 7.12" | Not an error: a dependence. B's first report treated the identification sp = c^* as an unproved premise of both routes (wrong: only of route 1). | - | B (R2), corrected by B on 25 Aug | WB proves c^* = i_F^* r^* = sp^q integrally: `thm:collapse-equals-specialization` (S6-TOP-C3, 27 Aug) | Yes; strengthened (see A0-7). |
| 10 | Prop. 7.2, Lemmas 7.5-7.10 (cusp collapse), pp.40-50 | "Could not independently certify" continuity across strata, equivariance, descent, integral effect; A and B ask for a finite CW model. | - | A (R-02), B (R1), C | WB Round 3: the request for a CW model "was too strong"; the original's proof is audited and closed: S6-TOP-C1, C2 (27 Aug). One change: the end map is "modified equivariantly so that its restriction to a marked smooth fibre is the explicit honeycomb collapse" (Round 12). | Yes. |
| 11 | Theorem 4.5 (toric cusp filling), Cor. 4.8 | No error found; A wants one consolidated lemma (local finiteness, second countability, proper action); C calls it "critical, open" until reconstructed. C-PRES-012: forward/backward dependence between Thm 4.5(d) and Prop. 4.6 on reducedness. | D | A (R-06), C (REV-001, PRES-012) | "VERIFIED" S6-CUSP-ACTION (`thm:candidate-cusp-geometry`, 26 Aug); re-audited 5 Sep: "No false assertion ... The earlier source already includes all three details". | Yes. |
| 12 | Lemma 7.16 (sign lemma), Thm 7.17, sections 6-7.5 (meridians, drifts -v_j, l_0) | No error found; A and B want an orientation table and a derivation of the inclusions from the coordinate gluings ("a sign error interchanges the p = -1 and p = -7 examples"). | D | A (R-08), B (R3), C (REV-002) | "VERIFIED" S6-TOP-V1 (`prop:geometric-pi1`): zero-section whiskers, rho_j^{m_j} = t_{v_j}, cusp meridian bounds the toric disc, no drift. | Yes. |
| 13 | Prop. 7.27 (Leray transgressions "up to a common sign") and section 7.6 (MV) | No error; B says the matrices are not shown to be the geometric maps and the two routes share inputs. | D | B (R4), C (REV-003/004) | WB: d_2 identified through the truncation triangle (S6-TOP-LERAY-D2, 26 Aug); MV maps identified and compared with Leray (S6-TOP-MV1, S6-TOP-L1, 27 Aug); signs absolute. | Yes; strengthened (A0-8, A0-9). |
| 14 | Prop. 9.13 and Thm 10.5: base change, duality at nonnormal and nonreduced fibres | "Plausible; citations insufficiently precise" (flatness, Grauert, top-degree base change, Gorenstein duality on W, multiple fibres). | D | A (R-03), C | WB: `thm:cartier-duality` (corrected 5 Sep), `prop:cartier-duality-absolute`, `lem:curve-flatness`, `prop:analytic-base-change`, `cor:surface-top-base-change` (B's 26 Aug argument), `thm:structure-direct-images-audit`. The flatness argument is already in the original (section 9, "Step 0", l. 4075). | Yes. |
| 15 | Prop. 10.8 (a line bundle non-torsion on every fibre) | No error; the WB kept it "CONDITIONAL" until the direct images, Pic(X) = C and the orders of O_X(S_j)\|S_j were reproved. The original's cusp extension used the collapse route and a "separate continuity argument for a moving integral lift". | - | WB Round 7-8 (26 Aug) | "VERIFIED" S6-CDP-10.8: `thm:uniform-nontorsion-audit`; remark "provenance of the repair" (`analytic_picard.tex` l. 694-702) | Yes; proof made independent of section 7.2 (A0-12). |
| 16 | Theorem 10.5 (R^2 f_*(T_X (x) L) != 0 for every L) | No error; depends on H^2(X;Z) = 0 (to make every L trivial on dP6), i.e. on the topology. | - | A, B (26 Aug), WB | WB adds a Pic^0 route without topology and three proofs that r = nu^* i^* = 0 (A0-6). | Yes; strengthened. |
| 17 | Section 10.2-10.5 against CDP98/CDP20 | A: "no local algebra error", wants exact quotations and a separately refereed note; B: a conflict with the literature is no evidence for the construction; C: "a proof gap is not yet a proof that the published theorem is false". | D | A (R-04), B, C (CDP-005) | WB: the two printed inferences are REFUTED (S6-CDP-P692 with an independent test family; S6-CDP98-MONO); the theorem-level counterexample S6-CDP-CONFLICT is "VERIFIED" from the whole construction; corrected theorem S6-OPEN-CDP-REPAIR. | Yes; sharpened (A0-3, A0-4, A0-5). |
| 18 | Remark 1.3 / 9.21: h^{1,2} "not computed; expected value 1" | Not an error: an open computation with a stated plan (direct images of E = Omega^1_X(log D)/f^*Omega^1_B(log Sigma)). | - | WB Rounds 14-15 (27 Aug) | "VERIFIED" S6-HODGE-H1: h^{1,2} = 1, h^{1,1} = 2 (A0-10). | Expected value confirmed. |
| 19 | Section 8 (recognition), Lemma 8.2 | Hurewicz "applied inductively" needs one more sentence; cite the exact smooth statement. | D | packet-06 review, A (V-05) | `thm:sphere-recognition`; Round 19 fixes the citation chain (Smale 1961 Thm A gives homeomorphism; Smale 1962 Cor 1.2 or Kervaire-Milnor give diffeomorphism). | Yes. |
| 20 | Notation: "Z/p" with p < 0; "c_3(X) = 2" for the Chern number | Write Z/\|p\|Z and <c_3(T_X),[X]> = 2. | D | packet-06 review | Adopted throughout the WB. | Yes. |
| 21 | p.71, modular TeX build | A phrase is set 15,000 pt off the page under MiKTeX in the modular build of the *reconstruction*. | - | C (TEX-009) | Build defect of the reconstruction, not of [AC26]. | n/a |

Items the WB front matter presents as its own results but which are **already in [AC26]** (so they are not
corrections of it):

- "The period signs are simultaneous": g_1'(z_1) = e^{-2 pi i/3}, g_2'(z_2) = -i, g_0 parabolic; "quadratic
  ramification alone gives only (g_2'(z_2))^2 = -1"; the mixed words y^3 x and y x^2 are not parabolic. The
  original has g_j'(z_j) = e^{-2 pi i/m_j} in the Setup (l. 144) and in Prop. 2.11(ii) (l. 592), zeta_2 = -i
  (l. 851), and the whole reduced-word argument in Lemma 7.16 (l. 2754-2769: "That 'simultaneously' is
  forced"). The WB's `lem:triangle-generator-orientations` (candidate_geometry.tex l. 33-112) is the same
  argument moved to the front. Round 26 ("exact-normalization supersession", 30 Aug) corrected the WB's own
  earlier text, not the original.
- The spine argument of S6-TOP-C1-SPINE is the proof of Lemma 7.8 of the original (l. 2267-2279: K(Z^2,1)'s,
  Whitehead, collar [Bro62], cofibration, Hatcher 0.19/0.20), stated abstractly.
- The simple connectivity of Y_eps by finite subfans and scaling in t is the original's proof of Cor. 4.8
  (l. 1516-1524). The "circular exhaustion argument" replaced in Round 6 was the WB's own.
- Flatness of f over a curve (torsion-free over a DVR) is in the original (l. 4075); Reviewer B "independently
  proved" it on 26 Aug.

Two reported "corrections" that are not errors of [AC26] either: the "modular factor e = F^{-1} e on page 71"
and the "simplification in the Neron-Severi independence proof" (A's crosswalk C-04, C-05). Reviewer B's
addendum calls them "two corrected transcription defects in the new proof layer", i.e. defects of the Codex
progress layer; A found the audited source correct at both places.

---

## 3. Candidates

### A0-1. The step on CDP20 p.692: exact cotangent filtration, an if-and-only-if criterion, and a test family that does not use X
- **Type**: correction of the literature; refinement of [AC26] (Lemma 10.3, Remark 10.4).
- **Where**: `cdp_program.tex` l. 40-123 (`prop:missing-cotangent-filtration`,
  `prop:missing-global-section-criterion`), l. 205-275 (`prop:conductor`), l. 278-352
  (`prop:nodal-counterexample`); ledger S6-CDP-P692, S6-CDP-CONDUCTOR; Round 4 (25 Aug), Round 5; re-audited
  5 Sep (`evidence\s6_cdp_direct_image_reaudit_20260905\AUDIT.md`, section 3).
- **Statement**: Let S be a reduced effective Cartier divisor in a smooth complex threefold X,
  T_S = ker(Omega^1_S -> j_* Omega^1_{S_reg}), Omega~^1_S = Omega^1_S/T_S,
  K_S = ker(Omega^1_X|_S -> Omega~^1_S). Then
  0 -> N^*_{S/X} -> K_S -> T_S -> 0 and 0 -> K_S -> Omega^1_X|_S -> Omega~^1_S -> 0 are exact. For a line bundle
  A on S: if H^0(S, Omega~^1_S (x) A) = 0 and H^0(S, N^*_{S/X} (x) A) = 0, then
  H^0(S, Omega^1_X|_S (x) A) = ker[ delta_A : H^0(S, T_S (x) A) -> H^1(S, N^*_{S/X} (x) A) ]. "Hence the two
  vanishings printed in the p.692 reduction imply the desired ambient vanishing if and only if delta_A is
  injective." Test family: C = {([x:y:z],t) in P^2 x Delta : y^2 z = x^2(x+z) + t z^3}, X' = C x P^1,
  S = C_0 x P^1 (C_0 the nodal cubic), A = pullback of the line bundle on C_0 glued at the node with
  multiplier lambda = 2. Both printed vanishings hold and H^0(S, Omega^1_{X'}|_S (x) A) != 0.
- **Support**: written proofs (about 4 pages); exact local checks of the conductor ideals for xy and xyz;
  re-audited once by a separate bounded audit (5 Sep) which reproduces the argument. WB: REFUTED (the
  inference), "VERIFIED" (the conductor theorem). The ledger adds the nonclaim: "This is not a counterexample
  to CDP Theorem 2.2, whose global hypotheses the test family does not satisfy."
- **What it adds**: over [AC26]: the conductor section s (Lemma 10.3) and the remark that the normal case is
  fine (Remark 10.4) are in the original; new are the exact sequences with K_S, the iff criterion, and a
  proper test family with smooth total space that shows the failure without any of the S6 construction.
  Over [E26]: Engel omits the CDP discussion. Literature: one web search (terms: Campana Demailly Peternell,
  algebraic dimension, vanishing second Betti number, non-normal fibre, torsion, conductor, 2026) returned
  only CDP98, the 2019/2020 corrigendum and Demailly's diff files; no published correction of the p.692 step
  found. Not an exhaustive search.
- **First assessment**: solid. My check of the test family: Omega~_{C_0} = nu_* Omega_{P^1} = nu_* O(-2), so
  H^0(S, Omega~_S (x) A) = 0 (both summands); H^0(S,A) = 0 because A_0 is a nontrivial degree-0 bundle on the
  nodal cubic; T_S is O on {node} x P^1, so H^0(T_S (x) A) = C; H^1(S, N^* (x) A) = H^1(C_0, A_0) = 0 by
  chi(A_0) = 0. So delta_A : C -> 0 and the ambient H^0 is C != 0. Agrees with the WB.
- **A full check must establish**: exactness on the left of the conormal sequence for reduced Cartier S; the
  identification of the kernel with ker delta_A as a canonical isomorphism; smoothness of C; that the
  quotation of CDP20 p.692 (arXiv:1904.11179 source, lines 980-986 in the WB's copy) says what is refuted;
  that CDP20 uses the step for a possibly nonnormal S.
- **Deserves a full check**: yes; it is the cleanest self-contained statement about the published proof.
  **Interest**: 4.

### A0-2. What survives of CDP20 Theorem 2.2 ("corrected CDP theorem") and the consequence H^2(X, T_X (x) L) != 0 for every L
- **Type**: correction of the literature (restatement of the valid part); new consequence for X.
- **Where**: `cdp_program.tex` l. 1368-1600 (`lem:cdp-generic-endpoints`, `thm:corrected-cdp-global`,
  `cor:corrected-cdp-relative`, `thm:corrected-cdp-fibrewise`, remark "scope and sharpness", paragraph "The
  exact monodromy repair"); ledger S6-OPEN-CDP-REPAIR (status VERIFIED); Round 24 (30 Aug); `next_lemmas.tex`
  record D1.
- **Statement**: Let X be a compact connected complex threefold with H^1(X;Z) = H^2(X;Z) = 0, a(X) = 1 and
  holomorphic algebraic reduction f : X -> C. If there is L_0 in Pic(X) with H^2(X, T_X (x) L_0) = 0, then for
  M in a dense open subset of Pic(X): H^i(X, T_X (x) M) = 0 (i != 1), chi(X, T_X (x) M) = (1/2) c_3(X) <= 0.
  It is enough that R^2 f_*(T_X (x) L) = 0 for one L ("the valid content of ... CDP20 Proposition 2.4"). If
  all full fibres W_c are reduced, with A_c = (omega_X (x) L^v)|_{W_c}: if for every c
  H^0(W_c, Omega~^1 (x) A_c) = 0, H^0(W_c, N^* (x) A_c) = 0 and
  delta_c : H^0(W_c, T_c (x) A_c) -> H^1(W_c, N^*_{W_c/X} (x) A_c) is injective, then R^2 f_*(T_X (x) L) = 0.
  For the constructed X: since c_3 = 2, H^2(X, T_X (x) L_0) != 0 for every L_0 (contrapositive).
- **Support**: written proofs (generic vanishing of H^0 and H^3 for general P in Pic^0 when a nonzero
  effective divisor is in Pic^0; semicontinuity; HRR with c_1 = c_2 = 0; projection formula and Leray). WB:
  "VERIFIED"; the ledger lists ten checked points.
- **What it adds**: over [AC26]: the original (l. 5093) only remarks that an argument excluding X "would have
  had to produce a lower bound for the torsion of R^1 f_*(T_X (x) M)"; it does not state a corrected theorem
  nor H^2(X, T_X (x) L) != 0 for all L. Over [E26]: nothing there. Literature: this is close to the logic of
  CDP20 Prop. 2.4 itself; novelty is small (a careful statement of what is still true). Not searched further.
- **First assessment**: plausible and mostly formal. The fibrewise criterion is by construction equivalent to
  the wanted vanishing, so it carries no new information beyond A0-1. The statement
  "H^2(X, T_X (x) L) != 0 for all L in Pic(X) = C" is a real property of X.
- **A full check must establish**: the generic endpoint lemma (H^0 and H^3 for general twist) in the analytic
  category; that "dense open" is right when Pic(X) = Pic^0(X) = C; the semicontinuity step; chi = c_3/2.
- **Deserves a full check**: maybe; short and it fixes what one may still quote from CDP20. **Interest**: 3.

### A0-3. CDP98 Lemma 3.2 (split extension): coinvariants, and the exact condition under which the surjectivity argument works
- **Type**: correction of the literature; refinement of [AC26] section 10.5 (Lemma 10.7).
- **Where**: `cdp_program.tex` l. 1304-1366 (`lem:semidirect-abelianization`) and l. 1586-1600; ledger
  S6-CDP98-MONO; Rounds 5, 6, 24.
- **Statement**: for a split extension 1 -> K -> G -> Q -> 1, G^ab = Q^ab (+) (K^ab)_Q (example
  Z x|_{-1} Z has abelianization Z (+) Z/2). The CDP98 restriction argument "can reach only the invariant
  integral lattice H^1(F;Z)^{pi_1(C^o)}"; its last step is valid precisely when the image of that lattice
  spans H^1(F, O_F) over C. For X the coinvariant rank is 1, not 4 (original: r = 3 instead of 6).
- **Support**: elementary proof; WB REFUTED (the printed formula) and "VERIFIED" (the lemma).
- **What it adds**: over [AC26]: the correction and its consequences (failure of CDP20 Cor 5.2, Prop 5.5 for
  X; R^1 f_* O_X = O (+) O(-1)) are in the original, l. 4652-4655, 4962, 5059. New: only the "exact span
  condition". Over [E26]: not treated.
- **First assessment**: correct; the content is the original's.
- **A full check must establish**: that CDP98 Lemma 3.2 (published numbering; "Lemma 5.2" in the arXiv
  version, as the 5 Sep audit warns) really uses the direct-sum formula without a monodromy hypothesis.
- **Deserves a full check**: maybe, only the quotation check. **Interest**: 3 (as part of a note on CDP).

### A0-4. Theorem 10.5 without the topology: the Pic^0 route, the obstruction r = nu^* i^*, three proofs that r = 0, and the nonzero local map
- **Type**: refinement of [AC26] (Theorem 10.5); new computation (the line bundle L_Q on the cusp tube).
- **Where**: `cdp_program.tex` l. 607-1195 (`prop:pic0-pullback`, `prop:all-pic-restriction`,
  `prop:leray-edge-restriction`, `lem:picard-crossed-defect`, `lem:picard-finite-norm`,
  `lem:picard-cusp-defect`, `prop:direct-boundary-picard`, `cor:candidate-pic0-route`);
  `analytic_picard_local_obstruction.tex` (14 KB); `analytic_picard_completion.tex` (35 KB;
  `prop:analytic-ah-boundary`, `lem:analytic-support-specialization`, `thm:analytic-all-picard`); ledger
  S6-CDP-PIC0, S6-CDP-RESTRICTION, S6-CDP-R-LERAY, S6-CDP-R-BOUNDARY, S6-CDP-R-LOCAL-OBSTRUCTION,
  S6-OPEN-R-ANALYTIC; Rounds 10 (26 Aug), 18, 19 (28 Aug), 23 (29 Aug), 25 (30 Aug); corrected 5 Sep.
- **Statement**: (a) omega_X is trivial near W (the form dx_1 ^ dx_2 ^ dt/(x_1 x_2)); hence for L in Pic^0(X),
  nu^*((L^v (x) omega_X)|_W) = O_{dP6} and R^2 f_*(T_X (x) L) != 0, "without using global topology". (b) For
  arbitrary L the conductor argument applies iff r(L) = 0, r = nu^* i^* : Pic(X) -> Pic(dP6). (c) r = 0, three
  proofs: (i) Leray edge: e(c_1(L)) lies in E_infty^{0,2} inside ker d_2^{0,2} = 0 because
  d_2^{0,2}(2q) = omega[delta]; (ii) boundary: c_1(L|_F) = 2nq and the crossed-homomorphism defects on the
  pair of pants are d-bar_1 = 4n[delta], d-bar_2 = -3n[delta], d-bar_0 = 0 with sum 0, so n = 0; (iii) purely
  analytic: for c_1(M|_{F_t}) = kq, (d-bar_1, d-bar_2, d-bar_0) = (2k, -3k/2, 0)[delta], so k = 0; then with
  the six central degrees (d_1,d_2,d_3,d_1,d_2,d_3), B = [[d_2+d_3, d_3],[d_3, d_1+d_3]] and
  E_M((lambda,0),(0,m)) = -B(B_0 lambda, m), unimodularity of B_0 forces d_i = 0. (d) The local map
  Pic(N_0) -> Pic(dP6) is not zero: D_Q = sum_{v in Z^2} (v_1^2 - 6 v_2^2) E_v descends to L_Q with
  c_1(L_Q|_{F_t}) = -2q and normalized central degrees (-12, 2, 0, -12, 2, 0).
- **Support**: long written proofs; exact verifiers (14/14 and 25/25 checks); "two independent read-only
  audits" (same model); three defects found and repaired during the "adversarial audit" of (iii) on 30 Aug;
  the finite norm identity was corrected again on 5 Sep (real marking). WB: all "VERIFIED".
- **What it adds**: over [AC26]: Theorem 10.5 deduces triviality on dP6 from H^2(X;Z) = 0 and injectivity of
  c_1 on Pic(dP6) (so it needs section 7). The Pic^0 statement, the map r, the proofs (ii), (iii) and the
  example L_Q are not in the original. Since Pic(X) = Pic^0(X) = C once H^2(X;Z) = 0 is known, (i)-(iii) do
  not give a new fact about X; they make the CDP contradiction partly independent of the integral topology.
  Over [E26]: nothing there. Literature: not searched.
- **First assessment**: (a), (b), (d) look solid. I checked (d) by hand: the neighbours of 0 in the fan are
  +-e_1, +-e_2, +-(e_1 - e_2), in cyclic order e_1, e_2, e_2 - e_1, -e_1, -e_2, e_1 - e_2, with Q-values
  1, -6, -5, 1, -6, -5; with C_k^2 = -1 the degrees a_{k-1} + a_{k+1} - a_k are -12, 2, 0, -12, 2, 0, as
  claimed; and then B = [[2,0],[0,-12]] = 2 diag(1,-6), consistent with the formula for B and with
  c_1 = -2q. (ii) and (iii) are delicate (branches of logarithms, three levels of covers, signs); they were
  corrected several times, which is a reason to check them, not to trust them.
- **A full check must establish**: the crossed-homomorphism formalism and its independence of choices; the
  finite norm identity N_{T_j} d_j = iota_{v_j} E with its sign; the cusp value d-bar_0 = 0 (argument principle
  in a Stein chart); the relation between toric support functions and the Appell-Humbert form; that (iii)
  really avoids Leray and nearby cycles (it still uses the coinvariant computation c_1(L|_F) = kq).
- **Deserves a full check**: yes for (a), (b), (d) (short); maybe for (ii), (iii) (long, redundant with the
  topology). **Interest**: 3.

### A0-5. The general "conductor mechanism" theorem and uniform top-degree base change
- **Type**: refinement of [AC26] (abstract form of Theorem 10.5); new proof of a known result (base change).
- **Where**: `cdp_program.tex` l. 357-606 (`thm:cartier-duality`, `prop:cartier-duality-absolute`,
  `lem:curve-flatness`, `prop:analytic-base-change`, `cor:surface-top-base-change`), l. 1200-1300
  (`thm:candidate-conductor`, hypotheses H1-H4); ledger S6-CDP-CONDUCTOR-ABSTRACT, S6-CDP-DUAL,
  S6-CDP-DUAL-ABS, S6-CDP-BC; Reviewer B's report of 26 Aug.
- **Statement**: (H1) X connected compact smooth threefold, f : X -> B nonconstant to a compact curve; (H2)
  W = f^{-1}(p_0) the full fibre, reduced, with local models x, xy, xyz; (H3) normalization dP6; (H4)
  H^2(X;Z) = 0. Then for every L in Pic(X): H^2(W, (T_X (x) L)|_W) != 0 and R^2 f_*(T_X (x) L) != 0. Base
  change: for f proper flat to a Riemann surface with fibres of pure dimension 2 and E a vector bundle,
  R^q f_* E = 0 for q > 2 and (R^2 f_* E)_b (x) C(b) -> H^2(X_b, E|_{X_b}) is an isomorphism at every b,
  including nonreduced fibres. Duality: for a compact full Cartier fibre W in a smooth threefold,
  H^2(W, E|_W)^v = H^0(W, E^v|_W (x) omega_X|_W), "compactness of ambient X and normality of W are
  unnecessary".
- **Support**: written proofs; B's independent derivation (26 Aug); 8 exact checks; the duality proof was
  rewritten on 5 Sep after the re-audit found the first construction of the pairing invalid.
- **What it adds**: over [AC26]: same mechanism as Theorem 10.5 and its proof (duality on the Gorenstein
  surface W, top-degree base change, flatness are all used there); the WB isolates the hypotheses and gives
  references (Banica-Stanasila III.3; Ramis-Ruget). The hypothesis list H1-H4 is tied to dP6 and H^2 = 0, so
  it is not really more general than the original; the natural general hypothesis is "eta^*A_L trivial" as in
  `prop:conductor`. Over [E26]: not there. Literature: standard tools.
- **First assessment**: sound as far as read; expository value.
- **A full check must establish**: the corrected duality proof; that the finite-complex theorem is quoted with
  the right hypotheses in the analytic category.
- **Deserves a full check**: no (standard), except the corrected duality paragraph together with A0-1.
  **Interest**: 2.

### A0-6. Integral equality sp^q = c^* and the completed collapse route (C1-C3)
- **Type**: refinement of [AC26] (closes the dependence stated in Remark B.4); new proof.
- **Where**: `topology_reduction.tex` l. 41-610 (`prop:topological-spine`, `lem:collapse-straightening`,
  `lem:positive-collapse`, `lem:phase-spread-collapse`, `prop:verified-cellular-collapse`,
  `prop:verified-collapse-homology`, `thm:collapse-equals-specialization`); ledger S6-TOP-C1, C1-SPINE, C2, C3;
  Round 3 (25 Aug), Round 12 (27 Aug). Reader A1 has the proofs.
- **Statement**: there is a Gamma- and T_f-equivariant strong deformation retraction Y_{<=eta} -> Y_0,
  continuous across every toric stratum, descending to r : N'_0 -> W; for c = r|_F,
  0 -> im(wedge^q M_0 - I) -> wedge^q Lambda -> H_q(W;Z) -> 0 is exact for every q; and for every q
  sp^q = i_F^* (i_W^*)^{-1} = i_F^* r^* = c^* : H^q(W;Z) -> H^q(F;Z), an integral equality (no sign or
  finite-index ambiguity), with image (wedge^q V)^{T_0}.
- **Support**: written proofs; WB "VERIFIED"; references Brown (collars), Dimca (proper specialization).
- **What it adds**: over [AC26]: Prop. 7.2 and Prop. 7.12 claim the collapse and its homology; Remark B.4
  says the identification sp = c^* and the degree-two normalisations are "not re-proved" in Appendix B and
  rest on section 7.2. The WB proves the comparison by functoriality of nearby cycles under the retraction.
  One modification of the original's end map (Round 12). Over [E26]: Engel uses a Leray computation and
  mentions the Clemens collapse only in Remark 8.3. Literature: for semistable degenerations the Clemens map
  realizes specialization (Clemens 1977); here W is not simple normal crossings and the degeneration is not
  polarized, so the statement is specific. Not searched further.
- **First assessment**: the comparison statement is natural and probably right; the weight is in the
  candidate-specific continuity and equivariance, which the reviews could not certify and which the WB
  reports as closed on 27 Aug.
- **A full check must establish**: (A1's job) continuity of straightening at the toric boundary, the phase
  spreading at stabilizers, the modified end map, the degree-three orientation.
- **Deserves a full check**: yes (through A1). **Interest**: 3.

### A0-7. The two topology routes compared as maps: Mayer-Vietoris blocks, absolute signs of the Leray transgressions
- **Type**: refinement of [AC26] (Props 7.26-7.27, Thm 7.22: signs "up to a common sign" made absolute; the
  two routes shown to agree by commuting squares); new proof of d_2 by the truncation triangle.
- **Where**: `integral_leray.tex` (`thm:p0-integral-specialization`, `prop:leray-e2`,
  `lem:first-transgression`, `lem:higher-transgressions`, `thm:h2-vanishing`, `prop:geometric-pi1`,
  `cor:candidate-sphere`); `topology_reduction.tex` l. 640-1123 (`prop:actual-finite-band-maps`,
  `prop:cusp-mv-blocks`, remark "one-shot H_1 check", `thm:mv-leray-comparison`), l. 1241
  (`cor:candidate-mv-sphere`); ledger S6-TOP-LERAY-D2, S6-TOP-MV1, S6-TOP-L1, S6-TOP-END, S6-TOP-END-MV;
  Rounds 7 (26 Aug), 13 (27 Aug), 21 (28 Aug).
- **Statement**: for K = Rf_*Z_X, the triangle R^0 f_*Z -> tau_{<=1}K -> R^1 f_*Z[-1] -> R^0 f_*Z[1]
  identifies the Cech lift-discrepancy cocycle with Leray d_2. On the clockwise disc/pair-of-pants cover the
  local discrepancy of 12 gamma is (4 l_1 - b_1, 3 l_2 - b_2, -(12 l_0 - b_1 - b_2)), with signed sum -p.
  With omega = c_1(O_B(1)): d_2(12 gamma) = -p omega, d_2(2q) = -p omega[delta],
  d_2(2 gamma uw) = -p omega[gamma delta] (so omega, omega[delta], omega[gamma delta] for p = -1). MV side:
  alpha_q = (pi_{1*}, -pi_{2*}) for X^o = X_1 u X_2 in named primitive bases, degree-one and degree-two
  matrices of Smith form diag(1,1,1,0), degree-two left kernel (4,2,3,2), top map (3,-4);
  K_1 = Z[a~_0], K_2 = Z<xi_w, xi_delta>; the cusp attachment has degree-one determinant -p and reduced
  degree-two block diag(-p, 1); a one-shot 9x9 collar matrix has determinant 1 - 12 l_0 = -p for
  (l_1,l_2) = (1,-1). The dual obstruction squares commute with the three transgressions.
- **Support**: written proofs; exact integer checks; "two independent read-only audits"; WB "VERIFIED".
- **What it adds**: over [AC26]: the original computes H_*(X) twice and says "neither computation uses the
  other" (l. 2197); it gives d_2 = +-p with a common sign and does not compare the two computations map by
  map. The WB (i) corrects an early conflation of its own (alpha_q belong to the finite-band stage, not a
  one-shot cover), (ii) proves the comparison, (iii) fixes the signs. Over [E26]: Engel's sections 6-7 redo
  van Kampen and Leray in his setting; no MV route, no comparison. Literature: not searched.
- **First assessment**: looks like careful bookkeeping; the result (H^k(X;Z) = Z/|p| for k = 2,3) is the
  original's. Arithmetic I checked: 1 - 12 l_0 = -(12 l_0 - 4 + 3).
- **A full check must establish**: (A1) the truncation-triangle identification; the orientation conventions
  that give -p rather than +p; primitivity of the bases; commutativity of the comparison squares.
- **Deserves a full check**: maybe (through A1); it is the part that turns "two computations agree" into a
  theorem. **Interest**: 3.

### A0-8. The Hodge numbers left open in [AC26]: h^{1,2} = 1, h^{1,1} = 2 (pointer; reader B has the proof)
- **Type**: new result (computation announced as "expected" in [AC26]).
- **Where**: `hodge_frolicher.tex` (48 KB); `status.tex` l. 991-1177; `next_lemmas.tex` records H1, H2;
  ledger S6-HODGE-PARAM, S6-HODGE-KS, S6-HODGE-H1; Rounds 14-15 (27 Aug), 17, 20 (28 Aug), 27 (1 Sep).
- **Statement**: with D = W + S_1 + S_2, L = Omega^1_B(log Sigma) = O(1), E = Omega^1_X(log D)/f^*L:
  f_*E = O (+) O(-1), R^1 f_*E = O^2 (+) O(-1)^2, R^2 f_*E = O (+) O(-1); div(det kappa_0) = p_1 + p_2;
  R^0 f_* Omega^1_X = O(-2), R^1 f_* Omega^1_X = O (+) O(-1)^2, R^2 f_* Omega^1_X = O (+) O(-1);
  h^{1,2} = h^{2,1} = 1, h^{1,1} = h^{2,2} = 2; dim E_1 = 10, dim E_2 = 2, E_2 = E_infty. The decisive scalar:
  kappa_1(h (x) gamma)(p_2) = -(1/4) mu-dot(z_2) != 0, using tau-dot(z_2) = 0 and K(z_2) = 6 mu-dot(z_2)^2 != 0.
- **Support**: written proof; exact invariant-lattice checks; "three independent audits converged on the
  scalar after one proposed h^{1,2} = 2 shortcut was falsified" (it divided by tau-dot at the order-four
  point); a context-isolated AI re-derivation on 1 Sep (Round 27). WB "VERIFIED"; human replication OPEN
  (S6-OPEN-HODGE-REPLICATION).
- **What it adds**: over [AC26]: Remark 1.3 and Remark 9.21 leave h^{1,2} open, "expected" 1, and name the
  sheaf E and the method. The WB carries the plan out. Over [E26]: Engel omits Dolbeault computations.
  Literature (web search, one query): Gray (h^{0,1} > 0), Ugarte 2000 (Frolicher constraints), Angella,
  arXiv:1705.10518 (Hodge numbers of a hypothetical complex structure on S^6), McHugh, arXiv:1708.03251
  (Bott-Chern and Aeppli numbers in terms of Hodge and Frolicher numbers). These treat a hypothetical
  structure; no computed diamond for an actual one was found, which is as expected before 2026.
- **First assessment**: the table is consistent: sum (-1)^{p+q} h^{p,q} = 2, chi(Omega^1) = -1, Serre
  symmetry, dim E_1 = 10 (my check). The value 1 depends on one scalar at the order-four point; that is where
  an error would sit.
- **A full check must establish**: (B) the invariant bases at the two multiple fibres, the residue
  cancellation, the cusp row (0,1,-1,0), the uniqueness of the lift h, and mu-dot(z_2) != 0.
- **Deserves a full check**: yes. **Interest**: 5.

### A0-9. Bott-Chern and Aeppli numbers and the Bott-Chern algebra (pointer; reader B)
- **Type**: new result (computation).
- **Where**: `hodge_frolicher.tex`, `bott_chern_algebra.tex` (30 KB); `status.tex` l. 1202-1353; ledger
  S6-HODGE-BCA, S6-OPEN-HODGE-REPRESENTATIVES; Rounds 16-17 (27 Aug), 23 (29 Aug).
- **Statement**: Bott-Chern rows q = 3,2,1,0: (0,0,1,1), (0,1,2,1), (0,2,1,0), (1,0,0,0); Aeppli rows:
  (0,0,0,1), (0,1,2,0), (1,2,1,0), (1,1,0,0); h^k_BC = (1,0,2,2,2,2,1), h^k_A = (1,2,2,2,2,0,1);
  H_BC^{*,*}(X) = C 1 (+) N with N^2 = 0, N spanned by A = [dG], B = [d-bar G-bar], C, C-bar, D, D-bar, E,
  E-bar, T; exp(12 g) = f^*O_B(1), c_{1,BC}(f^*O_B(1)) = 12(A + B).
- **Support**: McHugh's threefold formula h^{1,2}_BC = h^{1,2} + dim E_2^{3,1} - k^{2,0} with k^{2,0} <= b_2 = 0;
  the mechanism for k^{p,q} <= b_{p+q} was first argued wrongly (an injection into de Rham cohomology) and
  corrected in Round 17 to a surjection from the de Rham image of d- and d-bar-closed forms. WB "VERIFIED".
- **What it adds**: not in [AC26], not in [E26]. Literature: McHugh and Angella give the formulas for a
  hypothetical structure; numbers for an actual one need A0-8.
- **First assessment**: my check: the rows give h^k_BC = (1,0,2,2,2,2,1) and are symmetric under conjugation;
  nine generators match the row sums. Depends entirely on A0-8.
- **A full check must establish**: (B) McHugh's formula as quoted; the product computations; A C = 0 (the WB
  says it needs Dolbeault-Serre duality and an injection H^{3,2}_BC -> H^{3,2}_dbar).
- **Deserves a full check**: yes, after A0-8. **Interest**: 4.

### A0-10. Proposition 10.8 reproved without the collapse route; exact restriction condition
- **Type**: refinement of [AC26] (new proof of Prop. 10.8 and of Prop. 9.13 at the cusp).
- **Where**: `analytic_picard.tex` (`lem:hodge-line-audit`, `thm:structure-direct-images-audit`,
  `thm:uniform-nontorsion-audit`, remark at l. 694-702); ledger S6-CDP-10.8; Round 8 (26 Aug).
- **Statement**: f_*O_X = O_B, R^1 f_*O_X = O (+) O(-1), R^2 f_*O_X = O(-1), Pic(X) = C, degree-one base
  change at every scheme-theoretic fibre, ord(O_X(S_j)|_{S_j}) = m_j; for lambda = a gamma + bu + cw + d delta
  the restriction of the Picard line to a smooth fibre meets lambda exactly when c tau + d mu - b = 0; by the
  independence of 1, tau, mu every parameter outside R and a countable set gives an L non-torsion on every
  full fibre and on S_1, S_2.
- **Support**: written proof; WB "VERIFIED".
- **What it adds**: over [AC26]: same statements (Prop. 9.13, Prop. 10.8) and the same period/countability
  idea; the WB replaces the collapse-dependent cusp step by nearby cycles, identifies the restriction line
  with the gamma^{0,1} summand (removing a continuity argument), and proves the orders m_j by a finite-cover
  character argument. Over [E26]: not there.
- **First assessment**: a cleaner dependency graph; no new statement.
- **A full check must establish**: (B / G readers) the degree-one base change at the multiple fibres.
- **Deserves a full check**: maybe. **Interest**: 2.

### A0-11. Corrections of [AC26] proper (grouped): items 1-7 of the table
- **Type**: correction of [AC26].
- **Where**: `local_repairs.tex`; ledger S6-LOCAL-728, S6-HODGE-CUSP-TORSION; table in section 2 above.
- **Statement**: (i) Remark 7.28 must be existential in l_0; (ii) Lemma A.3: replace H_k by H^k and add
  universal coefficients; (iii) Remark A.6: pi_1(N_0) = Lambda-bar; (iv) Remarks 1.3 and 9.21:
  Omega^1_{X/B} is torsion-free and not locally free along W, with torsion (R/(s^{m-1})) ds only at the two
  multiple fibres; (v) Lemma 9.6: add the proof that Omega is connected and the estimate at the omitted
  points; (vi) Prop. 4.7(iv): the audits replace the argument, but the printed one is valid.
- **Support**: checked by me against the original for (i), (ii), (iii), (iv), (vi) (line numbers in the
  table); (iv) by the gcd criterion.
- **What it adds**: an errata list for [AC26]. Engel does not list errata.
- **First assessment**: all are harmless to the theorems. The only mathematical content is (iv).
- **A full check must establish**: comparison with the PDF at alpo.ge (the audits worked from a GPT
  reconstruction; (iii) and the truncated display in Lemma A.3 could be transcription artefacts).
- **Deserves a full check**: no (ten minutes with the PDF). **Interest**: 2.

### A0-12. Period family: the exact set of admissible constants, and why the cusp condition is needed
- **Type**: refinement of [AC26] (section 3: "the final imaginary constant is chosen so that ... D < 0").
- **Where**: `candidate_geometry.tex` (`prop:period-exact-admissible-constants`, `lem:toric-chart-control`,
  eq. `eq:cusp-exact-opposite-edge`); `status.tex` l. 169-184; ledger S6-PERIOD-EXACT-ADMISSIBLE-CONSTANTS,
  S6-PERIOD-CUSP-FREE-SHIFT-COUNTEREXAMPLE, S6-CUSP-EXACT-EDGE-IDENTIFICATIONS; 5-6 Sep (from the re-audit of
  the first check; other readers may have it under the deformation family).
- **Statement**: for the cusp-regular beta = beta^part + c_0, D_part = Im beta^part - 6 (Im mu)^2/Im tau
  descends to B minus p_0, tends to -infinity at p_0 and has a finite maximum M; the marked real period map is
  an isomorphism everywhere exactly when Im c_0 < -M. Without the cusp-regularity condition,
  beta~ = beta + i t o pi obeys the same affine laws but D~ = D + Re t is unbounded above. The opposite-edge
  identifications of W carry the multipliers e^{-2 pi i mu_0}, e^{12 pi i mu_0}, e^{-2 pi i (7 mu_0 + b_0)}.
- **Support**: written proofs; re-audit packet of 5 Sep with exact checks. WB "VERIFIED".
- **What it adds**: over [AC26]: the original proves existence of admissible constants (large negative
  imaginary part), not the exact half-plane; the edge multipliers are not written there as far as I saw.
  Over [E26]: Engel's parameter u in a small punctured disc plays the role of c; he does not give the exact
  range. Relevant to Engel's Remark 8.1.
- **First assessment**: plausible; M is defined as a maximum over a noncompact quotient, so its attainment
  uses the behaviour at the cusp, which is stated.
- **A full check must establish**: continuity and the limit of D_part at p_0, p_1, p_2; the "exactly when".
- **Deserves a full check**: maybe (short; fixes the parameter space of the family). **Interest**: 3.

### A0-13. Abstract restatements (grouped)
- **Type**: expository only / restatement of known results.
- **Where**: ledger S6-TOP-C1-SPINE (`prop:topological-spine`), S6-TOP-RECOGNITION
  (`thm:sphere-recognition`, with `lem:cohomological-closure`), S6-TOP-ABSTRACT (`cor:abstract-s6`),
  S6-ALG-P, S6-ALG-A2, S6-ALG-HOM (`exact_algebra.tex`); Rounds 3, 10, 22.
- **Statement**: spine: for a free properly discontinuous action of Gamma on a contractible manifold pair
  (A, A_0) with compact quotient Q, collared boundary quotient H and the same deck group, H is a strong
  deformation retract of Q and the retraction lifts equivariantly. Recognition: a closed smooth simply
  connected 6-manifold with the integral homology of S^6 is diffeomorphic to S^6 (Hurewicz, Whitehead, Smale
  1962 Cor. 1.2 or |Theta_6| = 1). Abstract application: V1 + MV1/L1 with H^2 = H^3 = Z/|p| and |p| = 1 give
  S^6. Algebra: the relation matrix has Smith form diag(1,|p|); the degree-two matrix has rank 3, saturated
  image, primitive left kernel (4,2,3,2); terminal homology (Z, Z/|p|, Z/|p|, Z/|p|, Z/|p|, 0, Z).
- **Support**: short proofs; exact checks. Reclassified from CONDITIONAL to VERIFIED on 29 Aug (Round 22)
  because "their displayed hypotheses are theorem antecedents".
- **What it adds**: nothing over [AC26]: the spine is the proof of Lemma 7.8, recognition is section 8, the
  algebra is Theorem 7.17, Lemma 7.18, Remark 7.20. Useful only as a dependency map.
- **First assessment**: correct and standard.
- **A full check must establish**: nothing beyond a reading.
- **Deserves a full check**: no. **Interest**: 1.

### A0-14. Open questions that the first check isolates
- **Type**: open question isolated.
- **Where**: `research_log.tex` l. 78-98 ("Current next calculations"); ledger S6-OPEN-HODGE-REPLICATION,
  S6-OPEN-EXTERNAL-ADJUDICATION; original l. 5093.
- **Statement**: (a) "whether the positive Euler characteristic admits a quantitative localization in the
  torsion length of R^2 f_*(T_X (x) L) and the conductor connecting kernels" (for X: chi(T_X (x) M) = 1 > 0
  although the generic rank considerations of CDP suggest <= 0; compute the lengths of the torsion of
  R^1 and R^2 f_*(T_X (x) M) at W, S_1, S_2). The original raises the same point in words (l. 5093).
  (b) An independent human derivation of the singular-fibre cotangent computation (h^{1,2} = 1).
  (c) For general proper families with a reduced nonnormal nc fibre: when is delta_A injective (A0-1)?
  that is, for which fibres does the CDP20 step hold.
- **Support**: none (questions).
- **What it adds**: (a) is a concrete computation on X not done in [AC26], [E26] or the WB as far as I read.
- **First assessment**: (a) is well posed and bounded once the direct images of T_X (x) L are computed in
  the style of A0-8.
- **A full check must establish**: n/a.
- **Deserves a full check**: n/a; (a) is worth a prompt of its own. **Interest**: 3.

Pointer outside my topic, for the coordinator: Engel's Remark 8.3 (quotient S^6 -> S^3 by the rank-3
subtorus, Seifert picture) meets later WB material that I saw only in the ledger and in status.tex
l. 1529-1806: S6-CUSP-CONE-SPHERE-ROUTES (maps q_1 : X -> C with Seifert targets, q-hat_3 : X ->> S^3),
S6-CUSP-LITERAL-COMPACT-EXTENSION (REFUTED: the literal circle quotient does not extend through the cusp;
"reduced-central-fibre degrees 27 and 64"), S6-CUSP-ONE-COPY-FRAMED-NULL ("the original based
angle-forgetting cusp map g : X -> S^3 is based null-homotopic", 5 Sep) and S6-CUSP-RETAINED-ANGLE-ARF
([H] = eta_4 eta_5 != 0 in pi_6(S^4)). Whether one of these maps is Engel's map, and what its class in
pi_6(S^3) = Z/12 is, would be a candidate for the reader of that part.

---

## 4. What remains open in the first check, and whether [E26] closes it

| Open item (WB id) | What is missing | Does Engel's paper close it? |
|---|---|---|
| S6-OPEN-EXTERNAL-ADJUDICATION / U-EXTERNAL-ADJUDICATION | "Independent specialist and community adjudication of the complete construction and counterexample" | **In part.** [E26] is an independent, human-verified, self-contained proof that the family consists of complex structures on S^6 (construction, van Kampen, Leray, recognition). It closes the item for existence and topology. It does not treat: the CDP analysis (omitted; the introduction only says the construction contradicts [CDP98, Cor. 4.2] and refers to [AC26, section 10]); a(X) = 1 (asserted in Remark 8.1, with [AC26, 9.1] cited in Remark 8.4 for the invariant Hodge class); direct images, K_X, Pic(X), Aut^0 (he states Aut^0 = C^* in Remark 8.3 without proof). Engel proves the theorem for his construction X(u, a_0, a_1); the identification with the period-theoretic X of [AC26] is described ("roughly") in his section 1.3, not proved in detail. |
| S6-OPEN-HODGE-REPLICATION / U-HODGE-REPLICATION / record H2 | A separately authored reconstruction of the cyclic invariant lattices, the determinant divisor p_1 + p_2, the residue cancellation and the order-four scalar. One context-isolated AI re-derivation exists (1 Sep). | **No.** Engel omits "computations of Dolbeault cohomology groups". h^{1,2} = 1 has no human check. |
| CDP side (not a WB open id; the WB calls S6-CDP-CONFLICT "VERIFIED") | Review by people who know the CDP papers of: the p.692 step, Lemma 3.2 of CDP98, and the counterexample to Thm 2.2 / Cor 2.3 | **No** for the analysis of the proofs; **yes** for the bare fact that Cor. 4.2 of CDP98 is false, once a(X) = 1 is accepted. |
| U-FABLE-PROVENANCE | Original session source of the Jacobian-conjecture map | Not mathematics; not relevant. |
| Question (a) of A0-14 | Torsion lengths of R^1, R^2 f_*(T_X (x) M) | No. |

Everything else that the three reviews of 24 Aug left "critical unresolved" (R1-R4; G, V1, B1, F1, L1; C1-C3,
MV1) is "VERIFIED" in the WB by 27 Aug; none of it is listed open in `uncertainties.txt`.

---

## 5. Timeline of the first check

| Date (2026) | Who / what | What was checked and with what result |
|---|---|---|
| Jul-Aug | Alpöge / Claude (Fable 5) | 108-page manuscript [AC26] circulated (PDF). |
| by 24 Aug | ChatGPT Pro sessions | PDF re-transcribed to LaTeX in ten strips (8 x 11 pp, 2 x 10 pp), consolidated as `s6_canonical_full.tex` (SHA-256 c20f12fd...); page-by-page fidelity audit "passes all 108 pages". No author TeX. |
| 24 Aug, 14:13 UTC | Pro session, "packet 06" review (pp. 56-66 only) | Reject, because of CDP20 Thm 2.2 / Cor 2.3. 22 exact checks pass. Finds Remark 7.28. Superseded the same day. |
| 24 Aug | Reviewer A (Pro), full manuscript, 17 pp | Major revision; no fatal contradiction; 28 checks; errors Remark 7.28, Prop. 4.7(iv); section 10 "coherent"; withdraws the packet rejection. |
| 24 Aug | Reviewer B (Pro), full manuscript, 6 pp + 92-row ledger | Major revision, main theorem not certified; 38 checks; four obligations R1-R4 in the integral topology. |
| 24 Aug | Reviewer C (Codex), integrated review + TeX audit | Not certifiable, not shown false; errors Remark 7.28, Remark A.6, Lemma A.3; p.71 build defect; CDP gap "credible". Annotated edition (120/121 pp) assembled; Overleaf import. |
| 25 Aug | Codex workbench starts (Rounds 0-5; "validate, repair, or disprove") | Obligations C1-C3, V1, MV1, L1 named; spine of Lemmas 7.8-7.9 reproved; CDP20/CDP98/Ramis-Ruget/Banica-Stanasila read; nodal-cubic test family; duality and top-degree base change; first reconstruction of the whole proof (statuses then reset to OPEN/CONDITIONAL). |
| 25 Aug | Round 6 | "Fail-closed recalibration": 28/28 and 38/38 reruns; p.692 inference and CDP98 formula REFUTED; supported-specialization diagram restored. |
| 25 Aug | Reviewer A corrective (from a Codex progress log, rechecked in the manuscript) | Adopts: a(X) = 1 proof complete; Leray route sufficient without Prop. 7.2; Lemma A.3 confirmed. Still major revision. 14 more checks. |
| 25 Aug | Reviewer B corrective | "Provisionally favorable": sp^q versus c^*; no load-bearing defect in the Leray + van Kampen route; 17 checks. |
| 26 Aug | Round 7 | Construction, cusp nearby cycles, Leray page and d_2, van Kampen, sphere, a(X) = 1, counterexample to CDP20: "VERIFIED". Collapse route and Prop. 10.8 still open. |
| 26 Aug | Rounds 8-11 | Prop. 10.8 and the structure-sheaf direct images; 56-page workbench, 123-page public edition; merge with the 18-page branch (Pic^0 route, obstruction r); Reviewer B's analytic follow-up (base change, duality, conductor from CAND-X, CAND-W, TOP-H2). |
| 27 Aug | Rounds 12-13 | Collapse C1-C3 (sp = c^*); MV1 and L1 (comparison with Leray, absolute signs). All six reviewer obligations closed. |
| 27 Aug | Rounds 14-17 | Hodge: reduction to m = h^{1,2}; K = det(Z-dot) vanishes at the order-three point (a shortcut refuted); h^{1,2} = 1 after a false h^{1,2} = 2 shortcut; Bott-Chern/Aeppli numbers; correction of the k^{p,q} <= b argument; cusp cotangent certificate. |
| 28 Aug | Rounds 18-21 | Leray-edge proof of r = 0; boundary-Picard proof; Hodge-map audit (three wording defects of the WB repaired; S6-HODGE-CUSP-TORSION entered); sign d_2(12 gamma) = -p omega fixed. |
| 29 Aug | Rounds 22-23 | Status semantics (three implication theorems to VERIFIED); L_Q (local Picard map nonzero); Bott-Chern algebra. |
| 30 Aug | Rounds 24-26 | Corrected CDP theorem (arXiv sources of CDP20 and CDP98 read); purely analytic proof of r = 0 (three defects repaired on the way); "exact-normalization supersession". Front matter of main.tex: "VERIFIED ... as of 30 August 2026". |
| 1 Sep | Round 27 | Context-isolated AI re-derivation of the Hodge computation; primary sources for HRR, Serre duality. |
| 3-4 Sep | Rounds 28-38 and Pro web session | Extension tracks (cusp spectral geometry, S^12/S^24 carriers, Kummer covers, Koide arithmetic, gauge operators). Not the first check. |
| 5 Sep | Bounded re-audits | CDP direct-image chain (two errors in the WB's proofs corrected); global construction: period, cusp, finite fillings (no false assertion; exact admissible constants). |
| 6 Sep | Workbench dated; 782 pp | Canonical ring, period-shift classification, deformation family (other readers). |
| 13 Sep (v1), 29 Sep | Engel, arXiv:2609.38442 | Independent geometric proof. |
| 29 Sep | Snapshot | File dates of `canonical_S6_snapshot`. |

---

## 6. Doubts and errors

1. **Prop. 4.7(iv)** (table item 2): the three audits and `local_repairs.tex` call the printed justification
   incorrect. As printed (l. 1508) it is a valid proof of closedness. The "repair" is harmless but the finding
   should not be listed as an error of [AC26].
2. **Remark 7.28** (item 1): REFUTED only under a reading that the sentence before it excludes. Fair to call it
   loose wording.
3. **Local repair 7** (item 6): I could not find a false sentence in the original; l. 3636 states the divisor
   k_j S_j correctly. Probably a repair of WB text presented among the manuscript repairs.
4. **Attribution in the front matter of main.tex** (corrective addendum, pp. 3-4): "The period signs are
   simultaneous", the spine, flatness, the Leray route and the nearby-cycle theorem are presented under "Codex
   validate/repair/disprove results". The statements and the arguments are in [AC26] (Lemma 7.16, Lemma 7.8,
   section 9 Step 0, section 7.7, Appendix B). The WB's contribution there is an independent re-derivation
   with more detail, not a repair. A reader of the front matter alone would overestimate what was wrong with
   the original.
5. **"VERIFIED" is not error-free.** Within the first check the WB's own proofs were corrected after being
   labelled complete: Round 15 (false h^{1,2} = 2 shortcut), Round 17 (wrong mechanism for k^{p,q} <= b),
   Round 20 (three wording defects in the Hodge proof), Round 25 (three defects in the analytic all-Pic
   proof), Round 26 ("supersession" of interim normalizations), 5 Sep (the duality pairing was not
   constructed; a complex scalar used in a real marking). None changed a final statement, but it shows that
   the long sign-sensitive proofs (A0-4 (ii), (iii); A0-7; A0-8) need a real check.
6. **Independence of the audits.** "Reviewer A", "Reviewer B", "two independent read-only audits", "three
   independent audits", "context-isolated derivation" are all sessions or sub-agents of GPT models, and A's
   and B's corrective rounds were prompted by a Codex progress log. The WB says so (`tool_disclosure.tex`,
   Round 27), and the harness counts (22, 28, 38, 14, 17, 8, 14, 25) overlap and certify only displayed algebra.
7. **Text base.** Every audit worked on a GPT reconstruction of the PDF. Table items 3 (the display ending
   "cong {}") and 4 could be transcription artefacts; a comparison with https://alpo.ge/s6.pdf is cheap and
   was not possible for me here.
8. `status.tex` item 13 calls the corrected statement "the strongest corrected conclusion that survives";
   "strongest" is not proved (no statement that weaker hypotheses fail), and the relative criterion is
   CDP20's own Prop. 2.4.
9. `thm:candidate-conductor` is announced as an "abstract" theorem but its hypotheses (dP6, H^2(X;Z) = 0)
   are those of the candidate; the abstract statement is `prop:conductor` plus duality and base change.
10. Dates: the research log gives no dates for Rounds 0-5; I place them on 24-25 Aug from the checkpoint
    names ("early_workbench_2026-08-25") and from Round 6 being dated 25 Aug.

---

## 7. Not read

- `reviewer_B_corrective_2026-08-25\report\S6_MATHEMATICAL_PROOF_AUDIT_REVISED.md` (39 KB): not read; its
  addendum and results file, which I read, state its content. `source_record\` of the same folder (copies of
  the canonical release, manifests): not opened.
- `reviewer_A_corrective...\report\revised_full_mathematical_peer_review.md`: read the addendum (lines 34-230)
  and lines 757-1075 (Appendix B, section 10, errors, requirements); the section-by-section part is the first
  report, which I read in full.
- `superseded_packet_06\report\peer_review_report.md`: skimmed (headings, sign audit, "additional issues").
- `WEB_PRO_MODE_FEEDBACK.md`: lines 750-2827 read by section heads and selected passages only (later
  extension work); `WEB_PRO_MODE_PRE_FEEDBACK_RESPONSE_2026-09-03.md`: head only.
- `research_log.tex` from Round 28 (3 Sep) on: headings only, except the 5 Sep direct-image entry.
- `literature_log.tex`: lines 60-658 skimmed, not read line by line.
- `claim_ledger.txt`: full JSON read only for the REFUTED/OPEN entries and the five named abstract entries;
  the rest through the index.
- `mathematical_summary.tex`, `dependency_ledger.txt`, `morphism_ledger.txt`, `literature_sources.md`: not in
  my list, not opened.
- Old copies under `workbench_history\` (transcriptions, former workbench sources): not opened, as instructed.
- Engel's paper: sections 2-7 not read line by line (searched for the overlap topics only).
