# Reader H — the public repository (light reading), 12 Nov 2026

Scope: the cloned repository `C:\Users\user\Documents\workbench_review_20261112\repo\` (7,511 files outside `.git`,
578 MB), read lightly for what it adds or changes on S6 relative to the local workspace
`C:\Users\user\Documents\math\research\s6_recent_results_main\` ("LW" below). Paths without a drive are relative to
`repo\`. No git commands were run; all file dates in the clone are the clone time (12 Nov), so dates below come from
file contents. Text files in the clone may have CRLF line endings (the key-advances `.tex` is 14,608 bytes in the clone
and 14,283 bytes with LF, which is the size and SHA-256 `7d0f9f36…` recorded in the package manifest).

Scratch scripts: `work\scratch\H\check_R.py` (numerical/exact checks of R1, R3, R4, R7, R8) and `normdiff.py`
(delimiter-normalised diff of repository and local consolidation files).

Summary of the finding for the survey: the repository contains **no S6 mathematics that is not also in the local
workspace**, with three exceptions: (i) the 5 October status note `s6\STATUS_2026-10-05.md`, which cites two documents
not held locally or in the repository ([R] and [N], Zenodo 10.5281/zenodo.23003415) and states the corrected position
on Campana–Demailly–Peternell; (ii) the Yang–Mills continuation of 30 Sep – 9 Oct, which is built on one S6-topology
theorem of the local higher-rung preprint (the cusp collapse map `H: X -> S^4` represents `eta_4 eta_5`) and otherwise
is Yang–Mills material; (iii) two source files in that continuation that I did not find locally
(`29_s6_cusp_gauge_spectral_chain.tex`, `29a_native_magnetic_upgrade.tex`: flat-torus spectral asymptotics of the
regular fibre at the cusp). The consolidation R1–R8 is the same text as the local `mathematical_consolidation\`.

---

## 1. Reading notes

### 1.1 Repository root

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

### 1.2 `s6\` (53 files, 33 MB; 27 MB of it is the public catalogue database)

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

### 1.3 `s6\consolidation\20260930\` (46 files) — the "S6 recent-results mathematical consolidation", 30 Sep 2026

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

### 1.4 `yang-mills\continuations\20260930-s6-ns-moment-map-bridge\` (145 files, 14 MB; 29 Sep – 9 Oct 2026)

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

### 1.5 Where else S6 enters the repository (grep for S6, S^6, six-sphere, Alp, Niemeier over md/tex/json)

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

### 1.6 The remaining top-level parts (no assessment)

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

## 2. Candidates

Most S6 candidates below are pointers: the mathematics is in the local workspace, which other readers cover. I give
them here so that the repository's statements can be matched to local entries. Interest ratings are mine.

### H-1
- **Title**: The conormal step of CDP20 (p. 692) fails at non-normal fibres: criterion, independent proper test
  family, exact one-dimensional failure at the cusp fibre, and the statement that survives. **Type**: correction of
  the literature; refinement of [AC26] §10.
- **Where**: `repo\s6\STATUS_2026-10-05.md` §3 (5 Oct 2026), which cites [N] Theorem 4.4, Remark 4.5, Theorem 5.2,
  Corollary 5.3 and [R] Propositions 5.3, 5.5 (neither document is in the repository or found locally). Local
  counterparts: `LW\courses\CG-S6\src\non-normal-fibres-and-vanishing.md` (lesson 10: §2 Theorem 2.1, §4 Theorem
  4.1, §5 Theorem 5.1, §6, §9, §11; its source notes name the labels `lem:extending-gluing`, `thm:nodal-test`,
  `thm:corrected-global`, `prop:relative-local` of [N] and `prop:normal`, `prop:kernel`, `prop:sharp`,
  `thm:derived`, `prop:torsion` of [R] §5); `LW\courses\CG-S6\provenance.json` lines 428–466;
  `LW\canonical_S6_snapshot\supporting_materials\workbench\research\ledgers\research_log.tex` lines 140–155 (the
  workbench's own record of constructing the test family).
- **Statement** (as in the status note): (i) for an irreducible reduced fibre `S` of `f` and `A = (L^v (x) K_X)|_S`,
  CDP20 deduce `H^0(S, Omega^1_X|_S (x) A) = 0` from the conormal sequence and
  `H^0(S, tilde Omega^1_S (x) A) = 0`, `tilde Omega^1_S = Omega^1_S/torsion`; this is valid for normal `S` and not
  in general, since the conormal sequence involves `Omega^1_S`, whose torsion is present exactly at the non-normal
  points. (ii) At a reduced normal-crossings fibre the deduction needs the extra hypothesis
  `H^0(tilde S, eta^* A) = 0`, `eta` the normalisation. (iii) Test family: a proper family over a disc with smooth
  total space and central fibre (nodal cubic) x P^1; a non-torsion line bundle on that fibre makes both endpoint
  groups vanish while the ambient twisted cotangent group is nonzero. (iv) At the cusp fibre `W` of X, with
  `eta^* A = O` and `H^0(W, tilde Omega^1_W (x) A) = 0`: `H^0(W, Omega^1_X|_W (x) A) = C` exactly. (v) If one line
  bundle `L_0` has `H^2(X, T_X (x) L_0) = 0`, then the generic vanishing and `c_3(X) <= 0` follow.
- **Support**: in the repository only the summary. Proofs: [N] and [R] (Zenodo, not read); the local course lesson
  10 "independently calculated in this lesson; no priority is claimed", with `checks\verify_conormal_torsion.py`.
- **What it adds**: over [AC26]: Lemma 10.3 and Theorem 10.5 there give the nonzero section
  `d(t_c∘f)|_W (x) theta` and `H^2(W, (T_X (x) L)|_W) != 0` for every `L`, and §10 already locates the p. 692 step
  (transcription line 4432). New relative to AC26: the test family independent of X (iii), the general criterion
  (ii), the exact dimension (iv), and (v). Over [E26]: Engel omits the CDP discussion. Literature: searched the web
  for discussions of an error in CDP20 Theorem 2.2 at non-normal fibres (queries on "Campana Demailly Peternell
  corrigendum … non-normal fibre conormal sequence torsion" and on Engel's paper); found only CDP20 itself
  (arXiv:1904.11179, Demailly's source page), which says the case of singular, in particular non-normal, fibres
  "needs special care"; nothing that identifies the failure. The post-cutoff papers are not indexed by the search.
- **First assessment**: plausible throughout. (i) is standard: for a reduced hypersurface `S` in a smooth threefold,
  `Omega^1_S` has depth >= 1 at isolated singular points, so torsion lives on the one-dimensional singular locus;
  at a normal crossing `xy = 0` the form `x dy` is torsion. Not checked: (iii)–(v).
- **A full check must establish**: the construction of the test family (smooth total space, properness, the
  line bundle and that it extends to the total space — the course's Theorem 5.1 handles the extension); the two
  endpoint vanishings and the non-vanishing; the exact kernel of `Omega^1_X|_W (x) A -> tilde Omega^1_W (x) A` at
  double and triple points; `H^0(dP_6, O) = C` as the source of dimension one; the proof of (v), including the
  base-change and duality steps; that the hypotheses of CDP20 Thm 2.2 are quoted correctly.
- **Deserves a full check**: yes — it is the cleanest self-contained statement of why the published theorem's proof
  breaks, independent of the S6 construction. **Interest**: 4.

### H-2
- **Title**: Every member of the family violates all three conclusions of CDP20 Theorem 2.2. **Type**: expository
  (restatement of [AC26] Corollary 10.6), with the extension "every member of Engel's family".
- **Where**: `repo\s6\STATUS_2026-10-05.md` §2.
- **Statement**: `X` satisfies the hypotheses (`H_1 = H_2 = 0`, `a(X) = 1`, holomorphic algebraic reduction to
  `P^1`); (c) fails since `c_3 = 2`; (b) fails for every `M in Pic(X)` since `c_1(X), c_2(X), c_1(M)` vanish
  rationally and HRR gives `chi(X, T_X (x) M) = c_3/2 = 1`; (a) fails since it would give
  `chi = -h^1 <= 0`. `X` does not contradict CDP20 Thm 2.1 or [LRS].
- **Support**: three-line argument in the note. I recomputed: `ch_3(T_X) = (c_1^3 - 3c_1c_2 + 3c_3)/6 = c_3/2`,
  `td = 1`, so `chi = 1`.
- **What it adds**: over [AC26]: nothing (Cor. 10.6, transcription lines 4631–4633, has the same computation);
  over [E26]: Engel does not discuss which conclusions fail.
- **First assessment**: correct. The note's remark that (a) fails "for any M" needs only `chi = 1`.
- **A full check must establish**: nothing beyond AC26.
- **Deserves a full check**: no. **Interest**: 1.

### H-3
- **Title**: The anticanonical ring of X is `C[U,V]` (degrees 1, 2) and recovers the fibration. **Type**:
  refinement of [AC26].
- **Where**: `repo\s6\27_s6_key_advances_frozen_2026-09-06.tex` §1 (6 Sep). Proof: local
  `…\workbench\research\analytic_canonical_ring.tex` (CR1–CR5; workbench Theorem 53.17); course lesson 8
  (`canonical-divisor-and-intrinsic-fibration.md`).
- **Statement**: `omega_X = O_X(-2S_2)`, `omega_X^{-2} = f^* O_B(p_2)`, `f_* O_X(kS_2) = O_B(floor(k/4) p_2)` for all
  `k in Z`; `(+)_{m>=0} H^0(X, omega_X^{-m}) = C[U,V]` with `div(u) = 2S_2`, `v = f^* l`,
  `l in H^0(B, O(p_2))` nonzero at `p_2`; basis of degree `m`: `u^{m-2j} v^j`, `0 <= j <= floor(m/2)`; the
  degree-two sections give the map `x -> [t(f(x)) - 1 : A + B'(t(f(x)) - 1)]`, i.e. `f`.
- **Support**: statement only in the repository; proof locator given.
- **What it adds**: over [AC26]: Main Theorem (7) has `K_X = f^* O(-1) (x) O(2S_2)`, which equals `O(-2S_2)` since
  `O(4S_2) = f^* O(1)`; the graded ring and the intrinsic recovery of `f` (hence: `f` is canonically attached to
  the complex manifold) are not stated there as far as I saw. Over [E26]: not there. Literature: not searched.
- **First assessment**: consistent: `h^0(omega^{-m}) = h^0(P^1, O(floor(2m/4))) = floor(m/2) + 1`, which is the
  number of monomials `u^{m-2j} v^j`. Depends on `f_* O_X(kS_2)` (multiple-fibre computation).
- **A full check must establish**: the pushforward formula at the multiplicity-4 fibre; the ring structure
  (multiplication), not only dimensions.
- **Deserves a full check**: maybe (short; belongs to the local Theorem 53.17 entry of another reader).
  **Interest**: 3.

### H-4
- **Title**: The period constant `c` in `beta_c = beta^part + c` gives a nonzero Kodaira–Spencer class of the whole
  threefold. **Type**: new result relative to [AC26]; proof of a statement that [E26] Remark 8.1 sketches.
- **Where**: key-advances reader §2; local `period_parameter_deformation.tex` (PD1–PD18; workbench Theorem 53.18);
  course lesson 9 (`periods-and-nontrivial-deformation.md`).
- **Statement**: for `c` in a disc `Q` with closure in `{Im c < -M}`, `M = max_{B \ p_0} D_part`,
  `D_part = Im beta^part - 6 (Im mu)^2/Im tau`, the charts and gluings give a proper holomorphic submersion
  `X_Q -> Q`; on a regular fibre the KS class is
  `-[ (1/(2iD)) d_{zeta_2} (x) (d zeta-bar_2 - (m/T) d zeta-bar_1) ] != 0`; since the degree-two anticanonical
  sections recover `f` over `C[eps]/(eps^2)` and the three critical values are fixed, a first-order trivialisation
  would preserve the fibration, so `KS_{X_{c_*}}(d/dc) != 0 in H^1(X_{c_*}, T)`. Not claimed: pairwise
  non-isomorphism.
- **Support**: statement and proof outline in the reader; full proof local.
- **What it adds**: [AC26] fixes one admissible constant (the parameter is implicit in its Setup); [E26] has the
  family `X(u, a_0, a_1)` and says it really deforms, by a sketch. This is a written first-order proof. The local
  course lesson 9 goes further ("classifies all parameter identifications … exactly the even shifts").
- **First assessment**: the fibre computation is elementary; the weight is on the global step (H-3 over the dual
  numbers, and that the critical values cannot move).
- **A full check must establish**: flatness/freeness of the degree-two sections over the dual numbers; that an
  automorphism of the base fixing three points to first order is trivial; the restriction map from
  `H^1(X, T_X)` to the fibre class; the dictionary `c <-> u` with Engel.
- **Deserves a full check**: yes (through the local sources). **Interest**: 4.

### H-5
- **Title**: Finite fillings: product covers of degrees 9 and 8, the full central attachment kernel, and a smooth
  trivialisation of the torsion normal line. **Type**: refinement of [AC26] (explicit form of the multiple-fibre
  neighbourhoods).
- **Where**: key-advances reader §3; local `finite_filling_certificates.tex` (FF1–FF46; Theorems 53.4, 53.6, 53.7,
  53.9); course lessons 1–3.
- **Statement**: as in §1.2 item 3 above; in particular
  `ker(Lambda x|_{A_j} Z -> Gamma_j) = <G~_j^{m_j} t_{-v_j}> = Z`, central, and
  `H_j(A_j x + v_j/m_j) = zeta_j H_j(x)` for `H_j(x) = exp(-2 pi i eps_j gamma(x))`.
- **Support**: locator only.
- **What it adds**: [AC26] has the multiple fibres with bielliptic reductions and the normal bundle of exact order
  `m_j`; the kernel statement is the group-theoretic input of the `pi_1` computation, made complete ("the entire
  kernel, not merely a relation"). Over [E26]: Engel uses logarithmic transforms.
- **First assessment**: routine but useful bookkeeping; the kernel statement is immediate from the presentation.
- **A full check must establish**: freeness of the actions; degrees; identification with the normalised base change.
- **Deserves a full check**: no (covered by the verification of the `pi_1` computation). **Interest**: 2.

### H-6
- **Title**: Value groups of the cubic `Re((q_1 q_2) q_3)` on a Niemeier lattice, its Leech neighbour and their
  intersection; the common lattice with Wilson's octonionic Leech lattice. **Type**: computation (not S6 geometry).
- **Where**: key-advances reader §§4–5; local `es_niemeier_cubic_arithmetic.tex`,
  `es_niemeier_residue_fixed_neighbor.tex`, `es_niemeier_JM_cubic_extension.tex`, `es_niemeier_wilson_cyclic.tex`,
  `common_d4_image.tex` (also copied in the YM continuation's `sources\`).
- **Statement**: as in §1.2 items 4–5: `V_F(N) subset V_F(J) subset V_F(Lambda_L)` with index 4 then 3 (total
  `Z/12`); `Lambda_cyc ∩ L(N) = Lambda_cyc ∩ L(Lambda_L) = {sqrt2(a,a,a): a in D_4}`, Gram `6 G_{D_4}`, det 5184,
  minimum 12; on it the cubic is `2 sqrt2 P(a)`, `P(a) = a_0(a_0^2 - 3(a_1^2 + a_2^2 + a_3^2))`, generated group
  `4 sqrt2 Z`, value `12 sqrt2` not attained.
- **Support**: locators; checks in the local evidence folder (not read by me).
- **What it adds**: nothing on S6; AC26 and E26 have no such material. Literature: not searched.
- **First assessment**: the last claim checks by hand: `P` is even on `D_4` (if `a_0` is odd then
  `a_1^2 + a_2^2 + a_3^2` is odd), `P(1,1,0,0) = -2`, so the values generate `2Z`; `P ≡ a_0^3 mod 3`, so `3 | P`
  forces `3 | a_0` and then `9 | P`, hence `P = 6` is impossible. `det(6 G_{D_4}) = 6^4·4 = 5184`. The embedding
  `L` and the lattices depend on choices ("fixed real isometry"), so the value groups are invariants of the marked
  embedding, not of the lattices. The "mod 12" coincidence with the S6 exponent `|12 l_0 - 4 l_1 - 3 l_2|` is not
  argued to be more than a coincidence.
- **A full check must establish**: the definition of `L`; the generator certificates; independence or dependence on
  the marking.
- **Deserves a full check**: no for this survey. **Interest**: 2.

### H-7 (R1)
- **Title**: Gaussian mass on `H^3`: `∫ e^{-q^* H q} d^{12}x = pi^6/N(H)^2`, `det L(H) = N(H)^4`,
  `E[q q^*] = 2H^{-1}`. **Type**: new proof or restatement of a known result.
- **Where**: `repo\s6\consolidation\20260930\MATHEMATICAL_NOTE.md` §1; identical in
  `LW\mathematical_consolidation\MATHEMATICAL_NOTE.md`; antecedent `thm:gaussian`. 30 Sep 2026.
- **Statement**: for `H in Herm_3(H)` positive, with `N` the Moore cubic (formula in §1.3 above).
- **Support**: one-page proof (spectral theorem by Rayleigh quotient; Schur complement for the realification
  determinant); exact and numerical checks in `verify_consolidation_v2.py`.
- **What it adds**: nothing over AC26/E26 (unrelated). Literature: not searched; this is the standard
  quaternionic (beta = 4) Gaussian integral `pi^{2n}/det_Moore(H)^2`; the note itself claims no novelty.
- **First assessment**: correct. My check (`work\scratch\H\check_R.py`): for three random positive `H`,
  `det(L(H))^{1/4}` equals the Moore cubic to 14 digits.
- **A full check must establish**: nothing.
- **Deserves a full check**: no. **Interest**: 1.

### H-8 (R2)
- **Title**: Two markings `Psi = X^{-1} H X^{-*}`, `B = X^* H X` of the same `H`, Schur coordinates for the
  observation `y = (q_1 - q_2, q_2 - q_3)`, disintegration with all constants, and three distinct fibres (dimensions
  4, 9, 6). **Type**: computation / correction internal to the workbench (claim ledger MC-001).
- **Where**: MATHEMATICAL_NOTE §2; antecedent `thm:disintegration`, `thm:KLloss`.
- **Statement**: `B = D Psi D`, `D = diag(C^{-1}, 3)`, `det X = det D = 1`; `N(H) = c N_2(S)`;
  `P_* mu_H = (pi^2/c^2) e^{-y^* S y} d^8y`; conditional density `(c^2/pi^2) e^{-c|t + l y|^2}`; surface Jacobian 9
  on `P^{-1}(y)`; equality family for data processing `H + P^* T P`; conditional KL loss formula.
- **Support**: proof in the note; exact checks.
- **What it adds**: unrelated to AC26/E26; standard Gaussian conditioning in quaternionic notation.
- **First assessment**: looks right; `N(H_r) = r` for the witness checked numerically.
- **A full check must establish**: nothing of interest.
- **Deserves a full check**: no. **Interest**: 1.

### H-9 (R3)
- **Title**: Residual-orbit average of the Gaussian mass: `A Z = pi^6 m/(m^2 - beta^2)^{3/2}` for `m > beta`,
  divergence for `-beta < m <= beta`. **Type**: computation / correction internal to the workbench (MC-002).
- **Where**: MATHEMATICAL_NOTE §3; antecedent `rm:cubic-law`, `rm:positive-theorem`.
- **Statement**: on the four circles `S_col -> S_col e^{i theta} q_0`, `N(H_theta) = m - beta cos t`,
  `beta = 2|rho||delta|`; classification as in §1.3.
- **Support**: proof (tangent half-angle substitution); the example `3 pi^6/32` and ratio `27/8`.
- **What it adds**: unrelated to S6.
- **First assessment**: correct; `(1/2pi)∫ (6 - 2 sqrt5 cos t)^{-2} dt = 0.09375 = 3/32` by quadrature.
- **A full check must establish**: nothing.
- **Deserves a full check**: no. **Interest**: 1.

### H-10 (R4)
- **Title**: Affinity `<sqrt p_H, sqrt p_G> = N(H)N(G)/N((H+G)/2)^2` and Fisher metric
  `2 Re tr(H^{-1} K H^{-1} L)`. **Type**: restatement of known results (Bhattacharyya coefficient of centred
  Gaussians; Fisher metric of the precision parameter).
- **Where**: MATHEMATICAL_NOTE §4.
- **Support**: proof; checks. My check on the family `H_r`: `4rs/(r+s)^2`.
- **What it adds**: nothing for S6. **First assessment**: correct.
- **A full check must establish**: nothing. **Deserves a full check**: no. **Interest**: 1.

### H-11 (R5)
- **Title**: A Gaussian random-phase channel on `C^d` built from `p_H` is CPTP; its coherence multiplier factors
  through the Schur coordinates. **Type**: computation (textbook pure dephasing with Gaussian noise).
- **Where**: MATHEMATICAL_NOTE §5.
- **Statement**: multiplier `exp(-i tau(omega_a - omega_b)) exp(-(tau^2/4)(alpha_ab^T L(S)^{-1} alpha_ab +
  |gamma_ab|^2/c))`; identity `L(H)^{-1} = (R - u l) L(S)^{-1} (R - u l)^T + c^{-1} u u^T`.
- **What it adds**: nothing for S6; the model data (pointer basis, couplings) are added by hand, as the note says.
- **First assessment**: correct in form. **Deserves a full check**: no. **Interest**: 1.

### H-12 (R6)
- **Title**: The static `tau^2` dephasing family is a semigroup only when all couplings coincide, but is
  CP-divisible; a Brownian phase variable with covariance `tau_c tau Sigma_H` gives a GKLS semigroup. **Type**:
  computation (known facts about Gaussian dephasing).
- **Where**: MATHEMATICAL_NOTE §6; ledger MC-003; result SZ-20260930-006.
- **What it adds**: nothing for S6. **First assessment**: correct (ratio of multipliers
  `exp(-(tau^2 - s^2) d_ab/4)` is again a Gaussian dephasing multiplier).
- **Deserves a full check**: no. **Interest**: 1.

### H-13 (R7)
- **Title**: Level-minimal "tomography": six points of `H^3` whose 15 pairwise differences give linearly
  independent functionals `A -> v^* A v` on `Herm_3(H)` (`det M_3 = -4096`); four points of `H^2` for `Herm_2(H)`
  (`det M_2 = -16`). **Type**: computation (small explicit design).
- **Where**: MATHEMATICAL_NOTE §7; `TOMOGRAPHY_DESIGN.md`; `checks\TOMOGRAPHY_DESIGN_MATRICES.json`; ledger MC-004;
  result SZ-20260930-007.
- **Statement**: `v_0 = 0`, `v_1 = e_1`, `v_2 = e_2`, `v_3 = e_3`, `v_4 = (0, i + k, 1 + i)`,
  `v_5 = (1 + j, -i, j)`; `w_0 = 0`, `w_1 = e_1`, `w_2 = e_2`, `w_3 = (-i, -j)`; minimality because
  `dim Herm_3(H) = 15 = C(6,2)` and `dim Herm_2(H) = 6 = C(4,2)`.
- **Support**: explicit matrices, Bareiss pivots; script.
- **What it adds**: nothing for S6. The underlying statement (a quadratic form on `H^n` is determined by its values
  on the `C(d,2)` differences of `d` generic points when `C(d,2) = n(2n-1)`) is elementary; the specific integer
  design is new only as an example. Literature: not searched.
- **First assessment**: correct. I rebuilt both matrices from quaternion multiplication: rows 4 and 15 of `M_3`
  and all of `M_2` agree with the appendix; `det M_3 = -4096`, `det M_2 = -16`.
- **A full check must establish**: nothing further.
- **Deserves a full check**: no. **Interest**: 1.

### H-14 (R8)
- **Title**: All negative-power moments of `m - beta cos t` on the circle: thresholds `p < 1` (simple zero),
  `p < 1/2` (tangency) and `J_p = m^{-p} 2F1(p/2, (p+1)/2; 1; beta^2/m^2)` for `m > beta`. **Type**: restatement of a
  known integral (Legendre-function integral).
- **Where**: MATHEMATICAL_NOTE §8; result SZ-20260930-008.
- **Support**: proof by binomial series; checks.
- **What it adds**: nothing for S6. **First assessment**: correct; quadrature agrees with the hypergeometric value
  for `p = 0.7, 2, 3.5` at `m = 6`, `beta = 2 sqrt5` to 15 digits.
- **Deserves a full check**: no. **Interest**: 1.

### H-15
- **Title**: The cusp collapse map `H = p_3 q_2 : X -> S^4` represents `eta_4∘eta_5 != 0 in pi_6(S^4) = Z/2`;
  consequently the pulled-back quaternionic Hopf bundle `P_H -> X` is the nontrivial `Sp(1)`-bundle over `S^6`.
  **Type**: new result (topology of the fibration of [AC26]); the bundle statements are formal consequences.
- **Where**: `repo\yang-mills\continuations\20260930-s6-ns-moment-map-bridge\sources\higher_rung\s6_higher_rung_24d_preprint.tex`
  (title "Retained cusp topology, triality morphisms, and the …"), §"The retained-angle cusp quotient and its
  nonzero top-cell class", lines 4470–5200, Theorem `ret:main` (line 4617); §`rettri:section`, lines 5205–5800,
  Theorems `rettri:bundleclass`, `rettri:subgroup`, Proposition `rettri:forgetting`. The file is byte-identical to
  `LW\canonical_S6_snapshot\s6_higher_rung_24d_preprint.tex` (301,399 bytes). Used in `SP1_BUNDLE_BRIDGE.md` §1.
- **Statement**: with `Z(s) = s B_0 + C(t)`, `t = e^{2 pi i s}`, `B_0 = [[0,1],[-1,0]]`,
  `C(t) = [[6 mu, h_per],[b - h_per, mu]]`, `A(t) = log|t| B_0 - 2 pi Im C(t)`, the native quotient
  `pi-bar_f([x,t]) = [A(t)^{-1} log|x|] in R^2/Z^2`; `q_2(x) = [r, e^{i phi}, pi-bar_f(x)]` for
  `t(f(x)) = r e^{i phi}`, `0 < r < eps`, collapsing `W` and the complement of the cusp neighbourhood;
  `p_3([r,z]) = [r, c_3(z)]` with `c_3: T^3 -> T^3/K^(2) = S^3`. Then `[H] = eta_4∘eta_5 != 0`; "its stabilized
  top-cell postcomposition is `eta^2 in pi_2^S`"; in particular `q_2` is not null-homotopic.
- **Support**: written proof of about 700 lines by the Pontryagin–Thom construction: the regular fibre
  `M = H^{-1}(y_0)` is the torus `w(a,b) = (rho_0 e^{i(phi_0 - a - b)}, rho_1 e^{ia}, rho_2 e^{ib})`,
  `rho_0 = r_0^{1/2}`, `rho_1 = rho_2 = r_0^{1/4}`, inside one toric chart; normal framing
  `(N_l, N_phi, N_1, N_2)` from the four target coordinates; the full frame equals `D(a,b) G_0`,
  `D(a,b) = diag(e^{-i(a+b)}, e^{ia}, e^{ib}) in SU(3)`; an explicit contraction of `D`.
- **What it adds**: over [AC26]: not there. Over [E26]: Remark 8.3 describes a quotient map `S^6 -> S^3` by the
  invariant rank-3 subtorus; this is a related map to `S^4` (the preprint says it "does not use the homotopy class
  of the angle-forgetting map `g: X -> S^3`"). Literature: not searched.
- **First assessment**: the mechanism is sound: since `SU(3)` is 2-connected, `D` is null-homotopic, so the normal
  framing plus the translation-invariant tangent framing is homotopic to a constant frame of `C^3`, and the framed
  bordism class of `M` is that of `T^2` with its Lie framing, which is `eta^2 != 0` in `pi_2^S = Z/2`. Risks: the
  continuity of `H` at the collapsed sets, the unstable-to-stable identification `pi_6(S^4) -> pi_2^S`
  (an isomorphism, `Z/2 -> Z/2`), the choice of framing convention (tangent orientation sign is computed in a
  lemma), and whether `M` is the whole preimage (a lemma proves it). The naming is heavy; the content is one framed
  torus.
- **A full check must establish**: that `q_2` extends continuously over `W` and over the outside; that `y_0` is a
  regular value with `M` the complete preimage; the differential table; the claim full frame `= D G_0`; that the
  class of `(T^2, Lie framing)` is `eta^2`; the identification of `pi_6(S^4)` with the stable group via
  Freudenthal; the relation to Engel's `S^6 -> S^3`.
- **Deserves a full check**: maybe — a genuine small topological fact about the fibration, checkable in an hour;
  it belongs to the reader of the higher-rung preprint. **Interest**: 3.

### H-16
- **Title**: Yang–Mills bridge, linear obstruction and quadratic replacement: `Hom_{Sp(1)}(R^5 + Im H_Ad + H_L^4,
  Im H_Ad) = R pi_Ad`; the maps `mu_e(a) = a e a-bar`; the profile morphism `M_H`; core with magnetic density 48
  and source `D^mu F_{mu j} = -16 T_j`. **Type**: computation (routine); as a contribution to S6: decoration.
- **Where**: `PROOF.md` Prop. 5.1, Lemma 6.1, Theorem 7.1, §§8–9; `RESULTS_20260930.md` SZ-20260930-001…003;
  check `checks\verify_sp1_moment_map_bridge.py`. 30 Sep 2026. Later variant: the quartic map `N = M∘P` in
  `20261011-…\JORDAN_MARKED_SLOTS_AND_PROFILE_MAP.md`.
- **Statement**: as in §1.4.
- **Support**: complete short proofs; SymPy receipts.
- **What it adds**: nothing on the S6 threefold. Prop. 5.1 is Schur's lemma (trivial, spin-1 and spin-1/2
  constituents; no map from spin 1/2 to spin 1). `mu_e` is the Hopf-type map `S^3 -> S^2` extended quadratically.
  The "core" is the constant connection `A_i = e_i` in `su(2)` on a ball, whose curvature is the commutator and
  whose source is the double commutator; the numbers 48 and -16 are normalisation arithmetic. The dependence on
  `X` is only through the bundle in which the constant coefficients live.
- **First assessment**: correct (I recomputed `J_1 = [j, -2k] + [k, 2j] = -8i`, `phi(-8i) = -16 T_1`, density
  `3·16 = 48`). Real as algebra, routine, and not a result about S6 or about Yang–Mills dynamics.
- **A full check must establish**: nothing.
- **Deserves a full check**: no. **Interest**: 1.

### H-17
- **Title**: The 49-dimensional carrier `F_4/rho(Sp(1)) -> F_4/Spin(8)` and the classifying map `r_H`. **Type**:
  expository / decoration.
- **Where**: `HIGHER_CARRIER_AND_EVOLUTION.md` Theorem 2.1, Prop. 3.1, §4; SZ-20260930-005, -006.
- **Statement**: dimensions 52 - 3 = 49, 52 - 28 = 24, fibre 25; `r_H: X -> D` with `r_H^*(F_4 -> D) = P_H`,
  `pi r_H` constant, `r_H` and `f_H: X -> Spin(8)/rho(Sp(1))` not null-homotopic.
- **What it adds**: nothing; any reduction of a trivialised `G`-bundle to `K` is classified by a map to `G/K`.
  Also in the dispositions file: "every continuous homomorphism `Spin(8) -> G` is trivial for `dim G < 28`"
  (true since `Spin(8)` is simple with finite centre, so the kernel is finite or everything).
- **First assessment**: correct, formal. **Deserves a full check**: no. **Interest**: 1.

### H-18
- **Title**: Source-free evolution of the profiles: homogeneous core `f'' + 8 f^3 = 0`; no static compactly
  supported solution with curvature; global Cauchy evolution of the cut-off data by Oh's theorem, with finite
  propagation. **Type**: computation / application of known theorems.
- **Where**: `HIGHER_CARRIER_AND_EVOLUTION.md` Prop. 6.1, Theorem 7.1, Prop. 9.1;
  `COMPACT_SUPPORT_CAUCHY_EVOLUTION.md` Theorem 2.1, Prop. 3.1, Cor. 3.2, Prop. 4.1; SZ-20260930-007…014.
- **Statement**: as in §1.4.
- **What it adds**: nothing for S6. The homogeneous `SU(2)` mechanics is classical (the note compares with
  Tsapalis et al.); `f'' = -8 f^3` follows from `[e_i,[e_i,e_j]] = -4 e_j`, and `f'^2 + 4 f^4` is conserved (I
  checked both). Global existence for smooth compactly supported Yang–Mills data on `R^{1+3}` is classical
  (Eardley–Moncrief; finite energy by Klainerman–Machedon; Oh's papers re-prove the finite-energy theorem by the
  Yang–Mills heat flow — from memory, not looked up); the application is a hypothesis check.
- **First assessment**: routine and plausible. **Deserves a full check**: no. **Interest**: 1.

### H-19
- **Title**: Flat-torus geometry of the regular fibre at the cusp: `D = L q + 6 m^2 = T^2 + (2h_0 - d_0)T +
  (h_0^2 - d_0 h_0 + 6 m_0^2) + O(T e^{-2 pi T})`, systole `>= min(T - C, M)` on the `M`-fold cover,
  `lambda_1 = (4 pi^2/R^2)[1 + min{2(d_0 - h_0), -2h_0}/R + O(R^{-2})]`, low-mode count `(E/4 pi) delta_R + O(R)`.
  **Type**: computation from [AC26] Prop. 3.21.
- **Where**: `HIGHER_DOMAIN_PROGRAM.md` §2; `PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md` PK1–PK20;
  `yang-mills\sources\ym_gap_primary_20260908\retained_cusp_nonlinear_bridge.md` §§1–2 (8 Sep); source
  `sources\s6_cusp\tex\satellites\29_s6_cusp_gauge_spectral_chain.tex` (110 K; not found in LW).
- **Statement**: as displayed; `h_0 = Im h(0)`, `d_0 = Im b(0)`, `m_0 = Im mu(0)` for the functions `h, mu, b`
  holomorphic at the cusp with `tau = sigma + h`, `beta = b - sigma - h`; monodromy `P -> P M_0`, `M_0 = I + N_0`,
  `N_0^2 = 0` of rank 2.
- **Support**: derivations in the files; `checks\verify_period_physical_kernels.py`.
- **What it adds**: over [AC26]: the period normal form at the cusp is AC26's; the volume, systole and Laplace
  eigenvalue asymptotics of the flat fibre metric `P^T P` are not in AC26 or E26 (they are not complex-geometric
  invariants: they depend on the chosen flat metric in the marked real coordinates). Literature: not searched.
- **First assessment**: correct as far as checked: `T = R + h`, `p = d - T` give
  `6m^2 - pT = T^2 - dT + 6m^2 = R^2 + (2h - d)R + h^2 - dh + 6m^2`; the two soft vectors give
  `|.|^2 = (m^2 + T^2)/delta^2 ≈ R^{-2}(1 + 2(d - h)/R)` and `(p^2 + 36 m^2)/delta^2 ≈ R^{-2}(1 - 2h/R)`; the soft
  sublattice has covolume `1/delta`, giving the count `pi (E/4 pi^2) delta`. Elementary.
- **A full check must establish**: nothing beyond the algebra; whether any of it is intrinsic (it is not).
- **Deserves a full check**: no. **Interest**: 2.

### H-20
- **Title**: Open items that the repository isolates (grouped). **Type**: open question isolated.
- **Where / statements**: (a) `s6\consolidation\20260930\UNMINED_QUEUE.md` Q6: classify informational completeness
  for restricted coupling sets beyond the two minimal designs of R7; the channel geometry induced by the affinity
  and Fisher metric; which symmetries act covariantly. (b) `sources\claude\y9_open.tex` Question 7: "Can a sequence
  of the spatial line's kind, in which finite gaps close while spectral weight escapes to high energy, be realised
  along a path whose limit satisfies the reconstruction axioms of the continuum problem?" (Yang–Mills, not S6).
  (c) `SP1_BUNDLE_BRIDGE.md` §7 item 2 and `PROOF.md` §11 item 1: follow the order-two class of `P_H` along "the
  complete soft end" — answered trivially in PK15–PK16 (the bundle is trivial on the cusp end). (d) The status
  note leaves open nothing on S6 itself.
- **What it adds**: nothing on S6 geometry. **Deserves a full check**: no. **Interest**: 1.

---

## 3. Doubts and errors

1. **Uncorrected status wording.** `s6\STATUS_2026-10-05.md` §4 says that `s6/README.md`, `s6/ATTEMPTS.md` and the
   root `README.md` were corrected and that the 6 Sep reader and 9 Sep guide keep their wording as dated records.
   Not corrected and not mentioned there: `WORKBENCH.md`, S6 section ("reconstructing and examining a proposed
   geometric construction … This publication does not independently certify a global complex structure on S6, a
   counterexample to CDP20"); root `ATTEMPTS.md`, S6 section ("the claimed complex-threefold construction");
   `s6\ATTEMPTS.md`, opening paragraphs and the "Limit" lines of routes 1–2 (only the last paragraph was corrected);
   `s6\consolidation\20260930\` (`README.md` Scope, `CLAIM_LEDGER.md` MC-006 "Unresolved", `MASTER_MAP.md` §2.1,
   `AUDIT_LIMITATIONS.md` last section, `UNMINED_QUEUE.md` Q3); `sources\claude\y6_side.tex` ("That statement was
   not checked here"). These are statements about the state of checking at their dates, as the brief says.
2. **The Yang–Mills continuation used `X = S^6` as a fact on 29–30 Sep**, while the S6 pages of the same repository
   then said the identification was not certified: `SP1_BUNDLE_BRIDGE.md` §1 and `PROOF.md` §4 take the "fixed based
   diffeomorphism `d: S^6 -> X`" and classes in `pi_6(S^4)`, `pi_5(Sp(1))` from the higher-rung preprint. With the
   5 Oct position this is consistent; the dependency should be recorded when H-15 is checked.
3. **"Triality bundle" overstates the S6 content.** The rank-24 bundle is `P_H x_rho O^3`; its isomorphism class is
   determined by one bit. The programme text (`HIGHER_DOMAIN_PROGRAM.md` §1) presents the S6 line as "a reusable
   mechanism"; the theorems proved (H-16 to H-18) do not use the S6 threefold beyond that bit, and the period data
   enter only as the number `D` (as `y6_side.tex` says).
4. **Duplicate result identifiers.** `SZ-20260930-005` … `-008` denote the catalogue correction, the semigroup, the
   tomography and the residual moments in `s6\consolidation\20260930\RESULTS_2026-09-30.md`, and the 49-dimensional
   carrier, the connection, the Gauss-preserving correction and the homogeneous evolution in
   `yang-mills\continuations\20260930-s6-ns-moment-map-bridge\RESULTS_20260930.md`.
5. **Two different low-mode counts** under similar names: `HIGHER_DOMAIN_PROGRAM.md` §2.2 has
   `N_R(E) = (E/4 pi) delta_R + O_E(R)` (two soft directions, `E < 4 pi^2`, original fibre); PK19 has
   `N(E) ≈ E^2 M^2 D/(32 pi^2)` (four-dimensional Weyl count on the `M`-fold cover). Not contradictory; easy to
   confuse.
6. **Attribution of the global Cauchy theorem** to Oh alone (`README.md`, `COMPACT_SUPPORT_CAUCHY_EVOLUTION.md` §2).
   For smooth compactly supported data the result is older (my recollection: Eardley–Moncrief 1982,
   Klainerman–Machedon 1995); not looked up.
7. **`spatial_continuum.tex`**: the copy in the continuation's `sources\spatial\` (414,920 bytes) is not the copy in
   the local snapshot's evidence folder (414,872 bytes); line references of `SOURCE_PROVENANCE.md` (Sections 20–21,
   equations 251–256, lines 113–296) refer to the repository copy.
8. **Consolidation R1–R8**: no mathematical error found in the parts I recomputed (R1, R3, R4 on a family, R7,
   R8). The note says "No novelty claim is made", which is accurate: R1, R4, R5, R6, R8 are textbook facts in
   quaternionic notation. The repository's description of the consolidation as "the current object map and complete
   proofs R1–R8" for the S6 programme (`WORKBENCH.md`) can mislead: R1–R8 contain no statement about the S6
   threefold.
9. **STATUS note, minor**: it states `a(X) = 1` and the one-parameter family "of algebraic dimension 1" by citing
   [AC26] and [E26, Remark 8.1] (a remark with a sketch); it calls the two treatments "two independent proofs" of the
   construction, which holds for the S6 identification. For the family the support is thinner: the local
   transcription of [AC26] has no discussion of a deformation family (the words "deform", "one-parameter" occur
   only in "deformation retraction"), so "[AC26] reaches the same family through the period matrix" refers to the
   free constant in `beta`, and the genuine variation rests on Engel's sketch and on H-4. Its references to "[AC26, Main Theorem (2)]" for `W` and "(5)" for the meromorphic
   functions agree with the numbering of the transcription (lines 237–260).
10. Key-advances reader §4: the value groups are groups generated by values of a cubic under a fixed embedding; the
    reader says so, and says no physical conclusion follows. The step from "total quotient `Z/12`" to the S6
    exponent 12 is suggestive only.

---

## 4. Not read

- `yang-mills\continuations\20260930-s6-ns-moment-map-bridge\CLAIM_LEDGER.md` (186 K),
  `RESEARCH_PROGRAM_LEDGER.json`, `checks\*`, `figures\*`, the `.tex`/`.pdf` twins; of
  `PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md` only lines 1–335 and the section list; of `HIGHER_DOMAIN_PROGRAM.md`
  only the opening, §2 and the section list; of `SPECTRAL_PROGRAM.md` only the opening and the section list;
  `RESULTS_20261009.md` headings only (its statements read through `CURRENT_CLAIM_DISPOSITIONS.json`). Reason: the
  assignment asked for introductions and statement lists; the content is lattice Yang–Mills.
- `sources\s6_cusp\tex\satellites\29_s6_cusp_gauge_spectral_chain.tex` beyond its first 60 lines, and
  `29a_native_magnetic_upgrade.tex`: read only through their summary in `HIGHER_DOMAIN_PROGRAM.md` §2. They are
  repository-only S6-cusp files; a later reader may want to look at them (H-19).
- The higher-rung preprint: only lines 4470–4900 and 5195–5300 (for H-15); it is a local file assigned elsewhere.
- `s6\consolidation\20260930\catalogue\*` (27 MB gz database; large dump), `literature\SOURCE_READING_LEDGER.jsonl`,
  `verify_consolidation_v2.py` (not run; I ran my own checks), `CONSOLIDATION.tex` (compared by diff only),
  figures, `UNCLASSIFIED_TRANCHE_2026-09-30.json`; the antecedent `.tex` files beyond abstracts, §§1–2 and statement
  lists.
- `yang-mills\continuations\20261011-central-signs-shrinking-window\`: README opening and the entries on
  `RAW_S6_HESSIAN_RECEIVING.md` and `JORDAN_MARKED_SLOTS_AND_PROFILE_MAP.md` (first pages of each) only.
- All Yang–Mills consolidations, other continuations, readers (PDF), Navier–Stokes material, `workbench.json`,
  `research-attempts.json`, ZIP files: openings or listings only, as assigned.
- The Zenodo documents [R] and [N]: not available locally; not downloaded.
- The search of `C:\Users\user\Documents` for [R] and [N] covered file names to depth 3 (excluding
  `interlanguage\`), and text in `LW\courses\`, `LW\canonical_S6_snapshot\` (md, tex, txt, json),
  `LW\mathematical_consolidation\*.md`, `LW\related_sources\**\*.md`. Compressed ledgers (`*.jsonl.gz`, sqlite) were
  not searched.

---

## Differences between the repository and the local workspace

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
