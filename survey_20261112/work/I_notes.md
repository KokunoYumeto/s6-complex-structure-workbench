# Reader I — the local workspace outside the canonical snapshot and the course (12 Nov 2026)

Reader I, Claude Fable 5.2. Read only; the only files written are this one and scratch scripts under
`work\scratch\I\` (`uts.py`, `finals.py`, `ledgers.py`, `unfin.py`, `tree*.py`, `claims2.py`, `grepgz.py`,
`members.py`, `relmodels.py`, `check_mono.py`). "LW" = `C:\Users\user\Documents\math\research\s6_recent_results_main\`.
Paths without a drive are relative to LW. The dumps (`*.jsonl.gz`) were streamed by script; none was loaded whole.

Short answer to the assignment:

1. Outside `canonical_S6_snapshot\` and `courses\CG-S6\` the workspace is custody and routing (archives, hashes, ledgers,
   catalogues) plus five "related source" roots. **Almost no mathematics about the threefold X lives only here.**
   What does: (a) the TeX of the correction note [N] with its own assessment file (found; it is the 1 Sep 2026
   draft `s6_arxiv_preprint_draft_2026-09-01\main.tex`); (b) in the two RH sources of 8-9 Sep (GPT-6 Astra), a set
   of small exact facts on the integral monodromy of the (3,4,infinity) local system (all invariant Hermitian
   forms, the commutant, the universal commuting quotient `Z/6 + Z`), an independent coordinate-level re-derivation
   of [AC26] sections 3, 4, 5, 7.4-7.7 and Appendix B, and a contrived degree-196 self-correspondence of the
   torus family. The Geometric Unity, Nolan and mass-gap sources contain no statement about X that is not in
   the canonical snapshot.
2. The paper [R] "The S6 record and the integral monodromy of its (3,4,infinity) period system" (claude-opus-5-5,
   28 Sep 2026) is **not** in the workspace: no copy, no draft, no fragment (searches below).
3. First check: Codex root task `01a03492-...`, started 24 Aug 2026 16:20 UTC, GPT-5.6 Sol at Ultra with
   Sol subagents; GPT-6 Astra appears from 5 Sep. Before it: ChatGPT Pro-mode sessions (transcription in ten
   strips; a packet-06-only review; two full reviews "A" and "B"). Details in 1.9.

---

## 1. Reading notes

### 1.1 Top level of LW

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

### 1.2 `mathematical_consolidation\` (30 Sep 2026; reader H read `MATHEMATICAL_NOTE.md`, `MASTER_MAP.md`,
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

### 1.3 The correction note [N] — found, with companions

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

### 1.4 The paper [R] — not found

No copy or draft of "The S6 record and the integral monodromy of its (3,4,infinity) period system". Searches:
`source_text_blobs\` (6,245 files; `*.tex`, `*.md`, `*.txt`) and `nested_source_blobs\` for "S6 record",
"opus-5-5", "period system", "2609.38442", "Engel": no relevant hit ("S6 record" occurs twice in `source_text_blobs`
md files as part of "S6 record `22666541`"-type Zenodo bookkeeping; "Engel" only Friedrich Engel and unrelated
authors); `ledgers\source_files.jsonl.gz` member names for `opus`, `s6_paper`, `correction_note`. The only local
traces are the citations in `courses\CG-S6\provenance.json` and lesson 10 (as reader H reports). The corpus was
frozen on 28-29 Sep 2026 and [R] is dated 28 Sep, written by another model outside this corpus. Local material
on the integral monodromy that predates [R] is in 1.7 below (candidate I-1) and in the course lesson
`integral-monodromy-and-fundamental-group.md`.

### 1.5 `related_sources\01a06ca0-cc7a-7ec3-ac8c-e21f2e047754\` — Geometric Unity and measured-fibre comparison
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

### 1.6 `related_sources\01a066d4-d59c-7422-aef7-b6b0a100ab86\` — Nolan import and Gaussian fibres
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

### 1.7 `related_sources\01a0814d-7c8a-71c1-b2b8-9c151927593b\` — "RH arithmetic quotient / three-point heat"
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

### 1.8 `related_sources\01a0814d-89f0-7361-8467-84ea74753ec3\` — "RH marked-factor correspondence"
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

### 1.9 `related_sources\01a03c80-d894-7fc2-8acb-5d1b2bd7bac2\` — earlier mass-gap comparison
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

### 1.10 `ledgers\`

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

### 1.11 `custody\` and the first-check provenance

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

### 1.12 `source_dialogues\`, `source_text_blobs\`

`source_dialogues\`: one `.jsonl.gz` per located thread (845 files; the root's is 647 K). Not opened (the
unfinished-routes ledger gave what was needed). `source_text_blobs\`: 6,245 hash-named files (1,783 json, 1,509 md,
960 txt, 925 tex, 920 py, 39 lean, ...); used only for the greps in 1.3-1.4 and to read the note's companions.

---

## 2. Candidates

### I-1
- **Title**: All monodromy-invariant Hermitian forms of the (3,4,infinity) local system, their signature (2,2), the
  restriction to the period plane, and two companion integral facts (commutant; universal commuting quotient
  `Z/6 + Z`). **Type**: computation; refinement of [AC26] §9.1 and of [E26] Remark 8.4.
- **Where**: `related_sources\01a0814d-7c8a-...\source_snapshot\rh_arithmetic_resolvent_20260908\s6_three_points_heat\`
  `negative_monodromy.tex` lines 1-200 (Theorem `thm:all-invariant-forms`, eqs. `Hfull`, `negative-vectors`,
  `period-plane-map`, `period-negative-Gram`, `period-square`, `period-negative-vector`) and `three_point_bridge.tex`
  lines 170-300 (Theorem `thm:integral-quotient`, Proposition `prop:dual-quotient`); commutant:
  `related_sources\01a0814d-89f0-...\source_snapshot\rh_marked_arithmetic_action_20260908\connes_blowup_check\`
  `s6_ns_lattice_dynamics.tex` eq. (S10). 8-9 Sep 2026, GPT-6 Astra.
- **Statement**: On `V = Z gamma + Z u + Z w + Z delta` with
  `T_1 = [[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]]`, `T_2 = [[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]]`
  (`A_j = (T_j^{-1})^T` on the dual lattice `Lambda`):
  (a) the Hermitian matrices with `T_1^* H T_1 = H = T_2^* H T_2` are exactly
  `H(a,b) = [[0,0,0,ia],[0,0,6ia,0],[0,-6ia,0,0],[-ia,0,0,b]]`, `a, b` real; `det H = 36 a^4`; signature (2,2)
  for `a != 0`; for `a = 0` the form is `b|D|^2` (D the `delta`-coordinate), so the positive semidefinite
  invariant forms are `H(0,b)`, `b >= 0`, with radical `<gamma, u, w>`;
  (b) on the period plane `j_P(z_1,z_2) = (6 mu z_1 + beta z_2) gamma + (tau z_1 + mu z_2) u + z_1 w + z_2 delta`:
  `j_P^* H(a,b) j_P = [[12 a Im tau, 12 a Im mu],[12 a Im mu, 2a Im beta + b]]`
  `= 12 a eta |z_1 + (theta/eta) z_2|^2 + (b - 2a d_P/eta)|z_2|^2`, with `eta = Im tau`, `theta = Im mu`,
  `d_P = 6 theta^2 - eta Im beta > 0`; so `H(a,0)` restricts with signature (1,1), negative vector
  `j_P(-theta/eta, 1)` of value `-2 d_P/eta`;
  (c) `{S : S A_1 = A_1 S, S A_2 = A_2 S} = {a I_4 + b E_41}`, `E_41 = delta^ (x) gamma`, and such an S is
  holomorphic on the period torus only for `b = 0`;
  (d) the largest quotient of V on which `g_1, g_2` act by commuting automorphisms is
  `V -> (Z/6) gamma + Z delta`, kernel `<6 gamma, u, w>`, with shears `+2d, -3d, +d` on the first coordinate; for
  `Lambda` it is `gamma: Lambda -> Z`.
- **Support**: written proofs by elimination (about one page each), with exact check scripts in the same folder
  (`negative_exact_checks.py`, 41 checks; not run by me). No workbench status mark: these files are outside the
  canonical ledgers.
- **What it adds**: [AC26] §9.1 and the Leray rows give the invariant class `q = uw + 6 gamma delta` and
  `H^0(B, R^2) = Z(2q)`; the packet-06 review already checked the Gram matrix `G_eta = [[2 Im tau, 2 Im mu],
  [2 Im mu, (1/3) Im beta]]` (the same form up to the factor 6). New here: the list is complete, including the
  rank-one symmetric invariant `|D|^2`, and the (2,2) statement. Over [E26]: Remark 8.4 uses the class of type
  (1,6) and the (1,1) Hodge form and quotes Klingler's question; it does not list all invariant forms. (c) is
  Lemma 5.1 of the later course lesson `courses\CG-S6\src\periods-and-nontrivial-deformation.md` (there with
  the better reading `Pi_{c+n} = Pi_c (I + nE)`); (d) is the algebraic shadow of [E26] Remark 8.3 (the rank-3
  sub-local system `ker gamma`). Literature: not searched.
- **First assessment**: correct. I recomputed with sympy (`work\scratch\I\check_mono.py`): `T_1^3 = T_2^4 = I`,
  `A_j = (T_j^{-1})^T`; the invariant symmetric forms are spanned by `e_44`, the invariant alternating forms by
  `gamma∧delta + 6 u∧w`; the commutant is `aI + bE_41`; the relation lattice has Smith form (1,1,6,0); the Gram
  matrix is as stated. A consequence not stated in the file: `H(a,b)` with `a > 0` is positive definite on the
  period plane at z iff `b > -2a D(z)`, and `-D` is unbounded at the cusp, so no single invariant form polarizes
  all fibres. Elementary, of interest as a clean statement next to Remark 8.4.
- **A full check must establish**: nothing beyond the linear algebra above; that the matrices are those of [AC26]
  in the same basis and transport convention (the files say `A_j` are the transposes of `T_j^{-1}`); whether [R]
  already states (a)-(d).
- **Deserves a full check**: no — it is verified by a ten-line computation; worth keeping as a stated lemma.
  **Interest**: 2.

### I-2
- **Title**: A degree-196 self-correspondence of the torus family from an integral matrix commuting with the cusp
  monodromy only: non-holomorphy, infinite label orbit, and its behaviour at the three fillings. **Type**:
  computation (new, of narrow interest).
- **Where**: `...\01a0814d-89f0-...\connes_blowup_check\s6_ns_lattice_dynamics.tex` (S1)-(S11);
  `s6_cusp_boundary.tex` (B6)-(B15); `s6_logarithmic_boundary.tex` (L1)-(L24); handoffs `HANDOFF_S6_NS_20260909.md`,
  `HANDOFF_CUSP_BOUNDARY_20260909.md`, `HANDOFF_LOGARITHMIC_BOUNDARY_20260909.md`. 9 Sep 2026, GPT-6 Astra.
- **Statement**: With `B_0 = [[0,1],[-1,0]]`, `M_0 = [[I,0],[B_0,I]]`, `J_g = [[3,1],[1,5]]` (a matrix taken from
  the Navier-Stokes manuscript), `C_g = B_0^{-1} J_g B_0 = [[5,-1],[-1,3]]`, `K = diag(C_g, J_g)`: `K M_0 = M_0 K`,
  `det K = 196`, so `[q,v] -> [C_g q, J_g v]` is a 196-sheeted self-covering of `R^4/Z^4` commuting with the cusp
  monodromy, with kernel `{[a/14, 5a/14, b/14, -3b/14]}`. In period coordinates it is
  `zeta -> J_g zeta + (Z C_g - J_g Z) Y_Z^{-1} Im zeta`, holomorphic iff
  `J_g Z - Z C_g = [[beta - 12 mu + tau, 7 mu],[7 mu, beta + 2 mu + tau]] = 0` iff `mu = 0`, `beta = -tau`.
  K does not commute with `A_1, A_2` (defects (S9)); its conjugacy orbit under `<A_1, A_2>` is infinite
  (`M_0^k C_1 M_0^{-k}` has (1,2) entry `1 - k`); a correspondence labelled by the orbit exists over the regular
  base (S11). At the cusp: `K(x,t) = (x_1^3 x_2 U_1, x_1 x_2^5 U_2, t)` with a bounded unit U; along
  `(u,u,u^20)` and `(u^2,u^3,u^20)` the images tend to `P_+` and `P_-`, so there is no continuous extension to
  `P_+`; the closed graph in `N_0 x_Delta N_0` has proper surjective projections and
  `pi_1^{-1}(P_±) = {P_±} x W` (B11). At the multiple fibres the cluster set at `s = 0` of each labelled operation
  is a two-torus `H_L` spanned by `(L-I)v_j, (L-I)d`.
- **Support**: written proofs (16-18 K each) and 33 + 33 + 92 exact checks by script. The files themselves say the
  graph "is not asserted to be a holomorphic graph" and that no global consequence follows.
- **What it adds**: nothing of this is in [AC26], [E26] or the canonical snapshot (grep for the matrices and for
  "196" in `canonical_S6_snapshot\supporting_materials\workbench\research\*.tex`: no hit). It is a statement about
  real-analytic self-maps of the cusp end, not about the complex structure. Literature: not searched.
- **First assessment**: the algebra is right as far as I checked (`K M_0 = M_0 K` by the block identity
  `J_g B_0 = B_0 C_g`; (S6) recomputed by hand). The object exists because of an analogy with another paper; I
  see no use for the geometry of X except the by-products (S10) (see I-1 (c)) and the careful (B1)-(B5).
- **A full check must establish**: (B8)-(B12) (limits along the two families of paths; density of the open orbit in
  W; the fourteen solutions of `a_1^14 = c_1^5/c_2`); (L11)-(L19).
- **Deserves a full check**: no — isolated and not used by anything else. **Interest**: 1.

### I-3
- **Title**: A second, independent coordinate-level re-derivation of [AC26] §3 (periods), §4 (cusp quotient:
  freeness, Hausdorffness, properness), §5 (logarithmic fillings), §7.4-7.7 (van Kampen, Leray) and Appendix B
  (nearby cycles), by a different session and model. **Type**: new proof or restatement of known results
  (replication record).
- **Where**: `...\01a0814d-89f0-...\connes_blowup_check\` `s6_period_existence.tex` (P25)-(P34),
  `s6_cusp_boundary.tex` (B1)-(B5), `s6_logarithmic_boundary.tex` (L1)-(L2), `s6_homology_leray_audit.tex`
  (H1)-(H11), `s6_nearby_cycles_audit.tex` (C1)-(C13), `s6_global_assembly_audit.tex` (GA1)-(GA5),
  `s6_ns_lattice_dynamics.tex` (S12); handoffs of 9 Sep 2026. GPT-6 Astra Ultra.
- **Statement**: the values of [AC26]: `tau, mu, beta` with their transformation laws and `D < 0`;
  `pi_1(X) = <c,x,y | c central, xy = c^{l_0}, x^3 = c^{l_1}, y^4 = c^{l_2}> = Z/|p|`,
  `p = 12 l_0 - 4 l_1 - 3 l_2`, with the explicit inverse isomorphisms `c -> 1, x -> -e, y -> l_0 + e`,
  `e = l_2 - 4 l_0 + l_1` (valid also for `p = 0`); `p = -1` at `(0,1,-1)`, `p = -7` at `(0,1,1)`;
  `d_2(12 gamma) = p omega`, `d_2(2q) = p omega[delta]`, `d_2(2 gamma uw) = p omega[gamma delta]`;
  `H^1 = 0`, `H^2 = H^3 = Z/|p|`; `im sp^q = (wedge^q V)^{T_0}` with the `E_2` table of the nearby-cycle spectral
  sequence; compactness and connectedness of the glued space.
- **Support**: short written proofs (4-7 K per file) and 19 + 18 + 19 + 12 exact checks. Each file lists what it
  takes from the source without proof: the local toric and logarithmic filling theorems, smoothness, the
  cup-product pairings used for `|p'| = |p''|`, the compact-manifold statement.
- **What it adds**: no new statement. Its value is as a replication by another model that read the original text
  (packets and page renders) on 9 Sep and agrees with [AC26] and with the canonical workbench of 25-29 Aug. Small
  items of presentation: all six signed parabolic carriers kept in (P27); the remark that reversing the meridian
  orientation changes all three `l_i` at once, while changing one sign is a different manifold (`Z/7`); the
  isomorphism (S12) with inverse. Literature: not searched.
- **First assessment**: consistent with the baseline where I compared (the Leibniz argument `p'' = 2p - p'` is
  [AC26], transcription lines 3181-3183; `M_0 = (A_1 A_2)^{-1}` confirmed by sympy). One sign slip in (GA5), see §3.
  It is shallower than the canonical `integral_leray.tex` and `topology_reduction.tex` (it does not derive the
  specialization maps or the based inclusions; it cites them).
- **A full check must establish**: nothing separately; a checker of the canonical topology chain can use these
  files as a cross-reference for signs and bases.
- **Deserves a full check**: no — duplicate of better-developed material. **Interest**: 1 (2 as provenance: it
  answers "was the topology recomputed independently?").

### I-4
- **Title**: The correction note [N] as a document: its full text, its own non-duplication assessment, and the
  three places where it says more than the later summaries. **Type**: correction of the literature; refinement of
  [AC26] §10 (same subject as H-1, G1b-1, -2, -3, -8; this entry only adds the source and what a checker gains
  from it).
- **Where**: `source_text_blobs\aca0913d....tex` (39 K), `7260e5b4....md`, `7cc1900f....md`, `667494d9....bib`;
  1 Sep 2026; GPT-5.6 Sol Ultra. Statement list in 1.3.
- **Statement**: as in 1.3; the central ones are Proposition 2.3 (`H^0(S, Omega^1_X|_S (x) A) = ker delta_A`
  under the two endpoint vanishings), Theorem 4.4 with Lemma 4.3 (the test family
  `y^2 z = x^2(x+z) + t z^3` times `P^1`, `A = pr_1^* O_C(P - O)|_{C_0}`, gluing multiplier 1/3),
  Theorem 5.2 / Corollary 5.3 (one L with `R^2 f_*(T_X (x) L) = 0` implies `c_3 <= 0`), Proposition 6.1.
- **Support**: complete proofs in the note (I read them; each is half a page to a page). The note's own
  disclosure: a human author "must verify every statement".
- **What it adds**: over [AC26]: [AC26] §10 has the conductor sequence and the conductor-supported section for
  W (Lemmas 10.2-10.3) and the nonvanishing `R^2 f_*(T_X (x) L) != 0` (Theorem 10.5); it does not have the
  connecting map `delta_A`, a test family independent of X, the explicit extending bundle, or Proposition 6.1.
  Over the course lesson 10 (G1b): the lesson re-derives these; the note is the dated first source, and it has
  (i) the explicit sections `P(t) = [3 : sqrt(36+t) : 1]`, `O = [0:1:0]` and `f(r) = r - 2`; (ii) Lemma 5.1 in a
  general form (any compact Y, any bundle B) with the Krull-intersection argument; (iii) `ASSESSMENT.md`, which
  ranks its own four contributions. Over [E26]: Engel omits CDP. Literature: the note's README reports a bounded
  search without a hit; reader H searched again (H-1); I did not.
- **First assessment**: sound on reading. Checks I did: `P(t)` lies on the curve (`y^2 = 9·4 + t`); `P(0)`
  corresponds to `r = y/x = 2`, the node branches to `r = ±1`, so the multiplier is `(1-2)/(-1-2) = 1/3`;
  in Theorem 5.2, `Pic(X) = H^1(X,O)` from `H^1(X;Z) = H^2(X;Z) = 0`, and Hirzebruch-Riemann-Roch gives
  `chi(T_X (x) M) = c_3/2` because `c_1, c_2` and `c_1(M)` vanish rationally. Corollary 5.3 with `c_3 = 2` gives
  `R^2 f_*(T_X (x) L) != 0` for every L on X from topology and `a(X) = 1` alone (G1b-3 has this). Weak points to
  look at: in Lemma 5.1 the parameter space must be irreducible and carry a Poincaré family (supplied in Theorem
  5.2 by an explicit Čech construction); Theorem 5.2 assumes the algebraic reduction is a morphism.
- **A full check must establish**: as listed under H-1 and G1b-1/2/3; in addition that Proposition 4.1's local
  model `uv = t` and the vanishing `H^0(S, N^* (x) A) = H^0(C_0, A_lambda) = 0` are right (they are immediate).
- **Deserves a full check**: yes, but once, together with H-1/G1b — use this TeX as the object to check.
  **Interest**: 4 (the same as H-1; not a separate finding).

### I-5
- **Title**: Open items about X that the workspace outside the snapshot records, including one question it
  isolates and leaves: elliptic quotients, subtori and Néron-Severi classes of the fibres. **Type**: open question
  isolated (grouped).
- **Where**: `mathematical_consolidation\UNMINED_QUEUE.md` Q3, Q4; `ledgers\unfinished_and_nonclaim_routes.jsonl.gz`
  (root thread raw lines given below); `source_text_blobs\aca0913d....tex` §5, Remark 6.2; the related-source
  ledgers; for (c) the canonical remark `cusp-spec-elliptic-descent-scope`
  (`canonical_S6_snapshot\supporting_materials\workbench\research\cusp_spectral_geometry.tex` lines 1165-1175).
- **Statement** (the list):
  (a) External replication only: the canonical ledger rows `U-HODGE-REPLICATION` ("Can an independent specialist
  reproduce the singular-fibre cotangent and scalar calculation?") and `U-EXTERNAL-ADJUDICATION`; root dialogue
  [61018, 62358, 65619]: no internal theorem open as of 31 Aug - 1 Sep.
  (b) Deformations: the reported nonzero Kodaira-Spencer class along the period constant "does not classify all
  deformations" [126720]; pairwise non-isomorphism of the members and an exhaustive classification are expressly
  not claimed (child thread `01a08749-50bc`, lines 36, 52). Open: the Kuranishi space of X; whether the family in
  `c` (and Engel's `u`) is the whole of it; when two members are biholomorphic.
  (c) Fibres: the locus `6 mu = a tau + b` where the first coordinate gives a map `F_z -> E_tau` with kernel
  `E_{tau_f}`, `tau_f = a mu - beta`, is classified; the workbench says this "does not prove that `A_z` has no
  other elliptic quotient or elliptic subtorus, that its Néron-Severi group vanishes, or that it carries no smooth
  integral magnetic line bundle". Open: all non-simple fibres; the jump loci of `NS(F_z)`; relation to
  Klingler's question in [E26] 8.4.
  (d) The cusp collapse map: its class after "forgetting the angle" is computed (`a = 0`); "it does not settle what
  survives before forgetting the angle" [108265].
  (e) The local elliptic bridge (a rank-three to rank-two lattice map intertwining monodromy, fans, periods and the
  cusp filling, with elliptic kernel): "extend this elliptic quotient across all three global fillings and audit
  the resulting topology" [90237].
  (f) From [N]: torsion of `wedge^2`, `wedge^3` of the relative differentials and of ramified quotient charts
  (Remark 6.2; later treated in the course, G1b-8); "whether the global hypotheses force a different argument to
  make `delta_A` injective" (§5; answered in the negative by X itself once X is accepted).
  (g) UNMINED_QUEUE Q3/Q4: a single standalone proof chain for the current candidate selected by hash; exact
  operator realizations for the cusp spectral statements. These are consolidation tasks, not known gaps.
  (h) From the RH sources: a map from the complex atlas, tangent bundle or Dolbeault complex of X to the arithmetic
  quotient was not found (`S6_BRIDGE_STATUS.md`); not a question about X.
- **Support**: quotations as given. For (c) I add a sketch of my own (not in the files): a class in
  `H^2(F_z;Z)` is of type (1,1) iff it is orthogonal to the periods of `d zeta_1 ∧ d zeta_2`, which in the basis
  `(gamma, u, w, delta)` are `(6 mu^2 - tau beta, -beta, 6 mu, -mu, tau, 1)`. The only linear relation that holds
  identically is the one between `6 mu` and `-mu`, which gives `eta = u∧w + 6 gamma∧delta`: near the cusp
  `tau = s + h`, `beta = -s + (b - h)`, `mu`, `h`, `b` single-valued, `s = log t_c/(2 pi i)`, so a relation
  `c_0 + c_1 tau + c_2 mu + c_3 beta + c_4 det Z = 0` forces `c_4 = 0`, `c_1 = c_3`, then (applying `g_1`, which
  brings in `beta tau`) `c_1 = 0`, `c_0 = 0`, `c_2 = 0`. Hence `NS(F_z) = Z eta` for z outside a countable union of
  proper analytic subsets, and since the Hodge form of `eta` is indefinite such fibres are not algebraic,
  in agreement with [E26] 8.4. This needs a proper check; it would settle the "very general" part of (c) and
  leave the jump loci.
- **What it adds**: (b) and (c) are questions that [AC26] does not pose; [E26] poses (b) in Remark 8.1 /
  Conjecture 8.2 and touches (c) in 8.4. Literature: not searched.
- **First assessment**: (b), (c) are well posed and reachable; (d), (e) belong to the higher-rung and sphere
  lanes (other readers). The wording "its Néron-Severi group vanishes" in the canonical remark cannot be meant
  literally, since `eta` is an integral (1,1) class on every fibre.
- **A full check must establish**: for (c): the period vector and the independence argument; the list of loci
  where further integral classes become (1,1); for (b): `H^1(X, T_X)` and the obstruction space, which the
  canonical `period_parameter_deformation.tex` and the course lesson on periods address in part.
- **Deserves a full check**: maybe — as a short task: prove `NS(F_z) = Z eta` for very general z and describe
  the exceptional loci. **Interest**: 3.

### I-6 (grouped; not about X)
- **Title**: Mathematics in the related sources with no map to X. **Type**: computation / expository (grouped).
- **Where / Statement** (one line each):
  - GU bridge, `handoff\S6_INTRINSIC_MATH.md` §1: normalizer of `R(Herm_3(H))` in `u(6)` is `R(sp(3)) + iR I_6`;
    Lie closure of `iR(J)` is `u(6)`. §2: support rank of any Jordan representation of `Herm_3(H)` is divisible
    by 6. (Standard facts reproved; "No novelty claim".)
  - GU bridge, `S6_COMPLETE_MATH.md` §2: no full-unit representation of the rank-three algebra on a (64,64)
    carrier; maximum support 120. §4: a rank-14 submersion from the 15-dimensional algebra to a chamber of
    Lorentz metrics with four-circle fibres; the Moore cubic does not descend. §5: a contraction
    `Omega^2 -> Omega^13` giving the Einstein tensor on Levi-Civita spin curvature, with a counterexample to the
    contracted Bianchi identity for general connections.
  - Nolan bridge: arcsine law of the Moore cubic on the residual circle (`E[N] = m`, `Var = beta^2/2`); these
    feed R3 and R8 (H-9, H-14).
  - Three-point packet: irreducibility of the hypergeometric system `(h, h+1; 1/2)` for `0 < h < 1/100` and
    absence of intertwiners with the rank-four S6 system; `B: v -> (1/4) e^{u/2} v(e^u)` as an algebra isomorphism
    with `F_4 B T = Xi`; `zeta(-1/2 + it) != 0` for real t (stated in a final answer of the 89f0 source; trivial
    from the functional equation and nonvanishing on `Re s = 3/2`).
  - Jacobian counterexample: `det DF = -2` by coefficient tables and three points with one image
    (`jacobian_negative.tex`); a replication of a known 2026 result.
- **Support**: written proofs and scripts in the snapshots; not checked by me.
- **What it adds**: nothing to S6 geometry. **First assessment**: not assessed (per the assignment for the zeta and
  Navier-Stokes material); the Jordan/normalizer items look routine.
- **A full check must establish**: n/a here.
- **Deserves a full check**: no — outside the scope of this survey. **Interest**: 1.

---

## 3. Doubts and errors

1. `s6_global_assembly_audit.tex` (GA5) writes `det R = 12 l_0 - 4 l_1 - 3 l_2 = -p`. With
   `R = [[3, -l_1],[4, l_2 - 4 l_0]]`, `det R = -12 l_0 + 4 l_1 + 3 l_2`, which is `-p` for
   `p = 12 l_0 - 4 l_1 - 3 l_2` as in (H2), (H4). The middle expression has the wrong sign; only `|p|` is used.
2. `s6_nearby_cycles_audit.tex` (C6): the source has `,qquad` for `\qquad` (a TeX slip; the 47-page PDF was
   reported as visually inspected).
3. `CUSTODY_INDEX.md` and `mathematical_consolidation\README.md`, `AUDIT_LIMITATIONS.md` ("has not accepted a
   global S6 identification, sphere recognition, global analytic atlas"), `UNMINED_QUEUE.md` Q3: wording of
   29-30 Sep. `actual_source_readings.jsonl` shows why: that consolidation read only lines 1-170 of
   `main.tex`, `workbench.tex` and the overview. It is not a finding against the workbench proofs, and it
   contradicts neither the canonical ledgers (no internal theorem open on 1 Sep) nor the 5 Oct status note.
4. The canonical remark `cusp-spec-elliptic-descent-scope` says the result "does not prove ... that its
   Néron-Severi group vanishes". `eta = u∧w + 6 gamma∧delta` is an integral (1,1) class on every fibre ([AC26]
   §9.1, [E26] 8.4; I rechecked the orthogonality to the (2,0) periods), so the group never vanishes; the intended
   statement is presumably about classes other than multiples of `eta`.
5. The root row of `custody\source_task_tree.json` carries `model: gpt-6-astra`. Read alone it suggests the audit
   was done on Astra. The subagent rows show Sol for 24 Aug - 4 Sep. Any provenance line should say "GPT-5.6 Sol
   (Ultra) for the first check and the proofs of 24 Aug - 4 Sep; GPT-6 Astra (Ultra) from about 5 Sep and for the
   two RH sources of 8-9 Sep".
6. Custody gap with a consequence for provenance: the original histories of all 2,039 subagent threads of
   24-31 Aug are missing. Statements such as "two independent adversarial audits" in that week cannot be checked
   against the subagents' own transcripts, only against projections (385 MB, not opened) and output files.
7. `ROOT_REQUESTS_AND_FINALS.md` of the 89f0 source: the final at raw line 1876 lists "`zeta(-1/2 + it) != 0`
   for every real t, without assuming RH" among results; this is classical and should not be counted as a finding.
8. `ASSESSMENT.md` of [N] (1 Sep) says the Hodge and Bott-Chern tables "still depend on unstated global frame,
   saturation, base-change, or cup-map bridges", while the root dialogue of 31 Aug - 1 Sep says the ledger has
   "no unresolved internal premise" and marks the Hodge arguments VERIFIED. Two statements of the same days by
   the same system; the readers of `hodge_frolicher.tex` should treat the Hodge numbers as needing the full check
   that the ledger row `U-HODGE-REPLICATION` also asks for.
9. The related-source files contain long stretches of verbatim private dialogue. They are custody records; nothing
   in them is a mathematical source, and they should not be quoted in any public summary.

---

## 4. Not read

- `mathematical_consolidation\MATHEMATICAL_NOTE.md`, `MASTER_MAP.md`, `CLAIM_LEDGER.md`, `REVIEW_2026-09-30.md`,
  `TOMOGRAPHY_DESIGN.md`, `CONSOLIDATION.tex`: by instruction (reader H). Both sqlite catalogues, the coverage
  dumps, receipts, scripts, figures: not opened.
- `ledgers\projected_thread_items.jsonl.gz` (385 MB), `projected_thread_turns`, `projected_thread_history_*`: not
  opened. `unfinished_and_nonclaim_routes`: all 1,596 records streamed; read in text: the 99 root-thread assistant
  records that match geometry and unfinished-work words (first 500-600 characters each) and about 10 child-thread
  records; the user records (733) not read. `source_claim_locators`: schema and counts only.
- `custody\FINAL_CUSTODY_AUDIT.json`, `archive_verification.json`, `source_history_coverage.json`: not opened.
- `ROOT_REQUESTS_AND_FINALS.md`: read in full only for `01a06ca0` (11 K). For `01a066d4` (20 K): the finals and
  the first goal block. For `01a03c80` (108 K), `01a0814d-7c8a` (282 K), `01a0814d-89f0` (218 K): every assistant
  final answer (at 1,500-5,000 characters each) and the user requests that carry
  mathematics; the repeated machine goal blocks (about 10 K each, dozens of copies) skipped.
- `UNIQUE_TEXT_SOURCES.json`: summarized by script (member roots and counts), not read row by row.
- Related-source snapshots: read in full: the handoffs named in 1.5-1.8, `S6_BRIDGE_STATUS.md`, the seven
  `s6_*.tex` files of the 89f0 source except `s6_logarithmic_boundary.tex` (first 80 lines + handoff),
  `negative_monodromy.tex` lines 1-215, `three_point_bridge.tex` lines 60-300. Not read: the GU and Nolan chapter
  proofs, `marked_arithmetic_action.tex` (75 K), the other 16 inputs of the three-point packet, everything under
  `connes_quotient_heat_transport_2026-09-08\` and `dbn_ns_rh_20260908\`, all check scripts (none run).
- `source_dialogues\`: not opened. `source_text_blobs\`, `nested_source_blobs\`: grep and the six files named in 1.3.
- No web search was made (no candidate of interest 4-5 originates here; I-4 is covered by reader H's search).
