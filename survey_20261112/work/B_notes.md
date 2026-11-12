# Reader B notes: the complex-analytic part of the S6 workbench

Reader: B (Claude Fable 5.2). Date of reading: 12 Nov 2026. Read only; nothing changed in the workspace.
Scratch script: `C:\Users\user\Documents\workbench_review_20261112\work\scratch\B\check_ps.py`.

Abbreviations. WB = `C:\Users\user\Documents\math\research\s6_recent_results_main\canonical_S6_snapshot\supporting_materials\workbench\research\`.
[AC26] = `...\canonical_S6_snapshot\original_clean_transcription.tex` (line numbers of that file). [E26] = Engel, arXiv:2609.38442.
All WB files carry the file date 29 Sep 2026 00:32 (a copy date); the content dates below come from the ledgers.
Notation of the workbench: f: X -> B = P^1, cusp p_0 (fibre W, normalization dP_6), finite points p_1, p_2 with f^*(p_j) = m_j S_j,
(m_1, m_2) = (3, 4); lattice Lambda = Z<gamma^, u^, w^, delta^>, V = Hom(Lambda, Z) = Z<gamma, u, w, delta>;
period matrix Pi = [Z | I_2], Z = [[6 mu, tau],[beta, mu]]; q = eta = u^w + 6 gamma^delta (the invariant (1,1) class, type (1,6));
T_j the monodromies on V, A_j = (T_j^{-1})^t on Lambda; v_1 = (1,2,-4,0), v_2 = (-1,-3,3,0) the logarithmic translation vectors.

---

## 1. Reading notes

### 1.1 `WB\cdp_program.tex` (63.6 KB, 1665 lines; content 26-30 Aug 2026, corrected 5 Sep 2026)
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

### 1.2 `WB\analytic_picard.tex` (26.3 KB, 709 lines; 26 Aug 2026)
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

### 1.3 `WB\analytic_picard_completion.tex` (35.0 KB, 1042 lines; 30 Aug 2026)
"An analytic completion of the all-Picard certificate". `prop:analytic-ah-boundary` (crossed homomorphism d: pi_1(P) -> V_R of
a line bundle, built from logarithms of O^* factors; N_{T_j} d_j = iota_{v_j} E; <d_0, delta^> = 0 by the argument principle on a
Stein chart); `lem:analytic-support-specialization` (L629: the degrees of nu^*(M|_W) on the hexagon determine the mixed
Appell-Humbert block of M|_{F_t}); `thm:analytic-all-picard` (L986: r = 0, "third certificate"). Checker
`supporting_materials\reproducibility\verify_analytic_picard_completion.py` (25 checks, not read).

### 1.4 `WB\analytic_picard_local_obstruction.tex` (14.2 KB, 484 lines; 29 Aug 2026)
`prop:local-cusp-picard-obstruction`: the explicit line bundle L_Q on the cusp neighbourhood N_0; remark with Bingener 1980.

### 1.5 `WB\hodge_frolicher.tex` (48.4 KB, 1329 lines; 27 Aug 2026, three internal audits that day)
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

### 1.6 `WB\bott_chern_algebra.tex` (30.4 KB, 809 lines; integrated 30 Aug - 4 Sep 2026)
"Period-coordinate Dolbeault classes and the Bott-Chern algebra". Fibre representatives Gamma, U, Q_F ((bcpr-gamma-form) etc.);
`lem:bcpr-degree-one-input`, `lem:bcpr-eta-extension`; the factor 12 (exp(12 g) = f^*O(1)) and c_{1,BC}(exp(z g)) = zA + z^- B
(L371-486); `prop:bcpr-generators-are-bases` (L513); `thm:bcpr-square-zero-algebra` (L626); two remarks saying that no literal
global coefficient formula for the forms G, Q is given.

### 1.7 `WB\analytic_canonical_ring.tex` (7.5 KB, 169 lines; 6 Sep 2026)
`thm:canonical-ring-recovery` (CR1)-(CR5), no status mark in the file; ledger S6-CANONICAL-RING-20260906 says VERIFIED.

### 1.8 `WB\period_parameter_deformation.tex` (18.3 KB, 396 lines; 6 Sep 2026)
`thm:retained-period-deformation` (PD1)-(PD18). Ledger S6-RETAINED-PERIOD-DEFORMATION-20260906: VERIFIED ("independent
GLOBAL_AUDIT.md; checker 15 identities" - those two files were not located by me).

### 1.9 `WB\period_shift_classification.tex` (25.7 KB, 590 lines; 6 Sep 2026; header "New proof fragment")
`pshift:thm:classification` (PS1)-(PS29), `pshift:lem:centralizer`. No own ledger id; recorded in the dated note at the end of
`ledgers\claim_ledger.txt` (L144-152, "original analytic-family classification c modulo 2Z") and in
`mathematical_summary.tex` L45-54.

### 1.10 Ledgers and summary
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

### 1.11 Evidence and checker
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

### 1.12 [AC26] sections read for comparison
L3239-3260 (Theorem 9.1), L3566-3600 (Remark 9.9), L3603-3682 (Lemma 9.10, Prop. 9.11), L3858-3942 (Prop. 9.13, §9.4),
L4223-4400 (Lemmas 9.17-9.19, Prop. 9.20, Remark 9.21, Cor. 9.22, Props. 9.23-9.24, Remarks 9.25-9.27), L4404-4881 (all of §10).
[E26] read in full.

---

## 2. Candidates

### B-1
- **Title**: The complete Hodge diamond of X: h^{1,2} = h^{2,1} = 1, h^{1,1} = h^{2,2} = 2, with the direct images R^q f_* Omega^1_X.
  **Type**: new result (computation); proves the "expected values" of [AC26].
- **Where**: `hodge_frolicher.tex`, `prop:log-relative-direct-images` (L319), `prop:log-ks-divisor` (L525),
  `prop:absolute-cotangent-direct-images` (L707), `thm:h12-scalar` (L1012), `cor:exact-hodge-diamond` (L1129). 27 Aug 2026.
- **Statement**: With E = Omega^1_X(log D)/f^*Omega^1_B(log Sigma), D = W + S_1 + S_2, L = Omega^1_B(log Sigma) = O(1):
  f_*E = O + O(-1), R^1 f_*E = O^2 + O(-1)^2, R^2 f_*E = O + O(-1), locally free with base change. The connecting maps
  kappa_0: f_*E -> L (x) R^1 f_*O_X and kappa_1: R^1 f_*E -> L (x) R^2 f_*O_X = O satisfy div(det kappa_0) = p_1 + p_2, kappa_1
  surjective, and H^0(kappa_1): C^2 -> C has rank one. Then
  f_*Omega^1_X = O(-2), R^1 f_*Omega^1_X = ker kappa_1 = O + O(-1)^2, R^2 f_*Omega^1_X = O + O(-1), and
  h^{p,q} (rows q = 3..0, columns p = 0..3): (0,0,0,1), (0,1,2,1), (1,2,1,0), (1,0,0,0).
- **Support**: a written proof of about 700 lines. Inputs: R^q f_*O_X = O, O + O(-1), O(-1) and f_*omega_{X/B} = O(1) ([AC26]
  Props. 9.11, 9.13, re-derived in analytic_picard.tex); the cyclic invariant bases (11.4) at p_j
  (e_0, s^{m-a} e_1 | e_0 b_0, s^a e_0 b_1, s^{m-a} e_1 b_0, e_1 b_1 | s^a e_0 b_0^b_1, e_1 b_0^b_1 with (m,a) = (3,2), (4,1));
  the cusp frame (d log x_1, d log x_2); a degree count (det kappa_0 is a section of O(2) with forced zeros at p_1 and p_2);
  the residue sequence 0 -> Omega^1_X -> Omega^1_X(log D) -> nu_* O_{D~} -> 0; the scalar
  kappa_1(h (x) gamma)(p_2) = -(1/4) mu'(z_2) != 0, where h is the unique section of f_*E with <h, xi> = 1.
  Workbench status: VERIFIED (S6-HODGE-H1, U-HODGE-H12), "three internal read-only audits 2026-08-27", a "further
  context-isolated AI derivation" reproduced it; human replication OPEN (S6-OPEN-HODGE-REPLICATION).
- **What it adds**: [AC26] proves h^{0,q} = (1,1,0,0), h^{p,0} = 0 (p > 0), Serre duals, and h^{1,1} = h^{2,2} = h^{1,2} + 1
  (Theorem 9.1(vi), Remark 9.21, L4307-4330), and says of h^{1,2}: "which we do not compute; the expected value is h^{1,2} = 1".
  The workbench value agrees with the expectation. [E26] omits Dolbeault cohomology. Literature: searched (WebSearch, 12 Nov 2026)
  "Hodge numbers Dolbeault complex structure S^6 2026", read Angella arXiv:1705.10518, McHugh arXiv:1708.03251 (abstract and
  tables through ar5iv), Viaclovsky arXiv:2609.33785 and 2610.39102, Liu-Rollenske arXiv:2609.33826 (pp. 1-3). Found: Gray 1997
  (h^{0,1} = h^{0,2} + 1 >= 1, h^{3,0} = 0), Ugarte 2000 and Angella's notes (h^{2,0} + h^{1,1} = h^{1,0} + h^{1,2} + 1; E_3 = E_infinity;
  h_2^{0,1} = h^{1,2} - h^{1,1} + 1), all for a hypothetical structure; Viaclovsky states h^{0,q} for his own family and writes
  "We do not compute the remaining Hodge numbers". I found no computation of h^{1,1}, h^{1,2} for any complex structure on S^6.
  The literature is moving fast (Liu-Rollenske cite six more 2026 preprints, GFL26, Yan26, Wan26, LLZ26, Che26, Eng26b, which
  I did not open), so a full check must repeat the search.
- **First assessment**: looks solid. Sanity checks done by hand: (i) chi(Omega^1) = 0 - 2 + 1 - 0 = -1, chi(Omega^2) = 0 - 1 + 2 - 0 = 1,
  chi(O) = 0, chi(Omega^3) = 0, sum (-1)^p chi(Omega^p) = 2 = c_3 (agrees with [AC26] §9.4); (ii) Serre duality holds in the table;
  (iii) the direct images reproduce chi(Omega^1) = -1 without topology: chi(E) = (2-1) - (4-2) + (2-1) = 0, chi(f^*L) = 2 - 3 + 1 = 0,
  chi(nu_*O_{D~}) = 1 + 0 + 0, so chi(Omega^1) = -1, and h^{1,0} = h^0(O(-2)) = 0, h^{1,3} = h^1(O + O(-1)) = 0 agree with [AC26]
  Prop. 9.20; (iv) the only place where m = h^{1,2} is decided is the rank of H^0(kappa_1): rank 1 gives ker kappa_1 = O + O(-1)^2
  (m = 1), rank 0 would give O^2 + O(-2) (m = 2, h^{1,1} = 3); m = 0 is impossible once the direct images are right;
  (v) I re-derived the reduction: h^{1,2} = 1 iff a tau' + mu' is not identically 0, where h = a d zeta_1 + d zeta_2; the function
  a_0 = -d mu/d tau satisfies the same automorphy law a(g_2 z) = tau a + mu as a, so the statement is that a_0 is not holomorphic,
  which holds as soon as mu'(z_2) != 0 at the order-4 point (there tau' = 0 in the coordinate s); mu'(z_2) != 0 is obtained from
  the degree count deg(det kappa_0) = 2 with one forced zero at each p_j. Weak points: the formula
  det kappa_0 = unit * m^{-2} s^{m+2-2a} K(s) and the identification of the frames at p_j; deg f_*E = -1 (elementary divisors
  (1,t) of f_*E -> (f_*T_{X/B})^dual at p_1, p_2); the claim that the composite T = coker kappa_0 -> H^1(S_j, O) is an isomorphism;
  the cusp frames. mu'(z_2) != 0 is not forced by the local symmetry (I checked: the law mu o g_2 = 1 + mu/tau puts no condition
  on the linear coefficient), so it rests entirely on the global degree argument; a numerical evaluation of mu near z_2 from
  its definition in [AC26] §3.2 would be an independent test.
- **A full check must establish**: (1) Omega^1_X(log D) and E are locally free at all three fibres, and E|_{N_0} is free on
  d log x_1, d log x_2; (2) the invariant bases (11.4) and base change at the non-reduced fibres; (3) degrees of f_*E, R^1 f_*E,
  R^2 f_*E; (4) formula (11.9)-(11.11) for kappa_0, kappa_1 in the invariant frames, K(z_1) = 0, unit at the cusp;
  (5) the residue computation (11.14)-(11.17) and R^1 f_*Omega^1_X = ker kappa_1; (6) the scalar (11.19a)-(11.20a);
  (7) an independent numerical or symbolic evaluation of mu'(z_2) or of ord_{z_2} K; (8) Leray on P^1.
- **Deserves a full check**: yes; it is the first complete Dolbeault computation for a complex structure on S^6 and the proof
  has a single decisive scalar. **Interest**: 5.

### B-2
- **Title**: Frölicher sequence degenerates exactly at E_2; complete Bott-Chern and Aeppli diamonds. **Type**: new result
  (computation); refinement of [AC26] Cor. 9.22.
- **Where**: `hodge_frolicher.tex`, `thm:frolicher-e2-candidate` (L166), `thm:exact-bott-chern-aeppli` (L1189). 27-30 Aug 2026.
- **Statement**: E_1 != E_2 = E_infinity; the two middle d_1 rows are exact complexes 0 -> C -> C^2 -> C -> 0
  (H^{0,1} -> H^{1,1} -> H^{2,1} and H^{1,2} -> H^{2,2} -> H^{3,2}); dim E_1 = 10, dim E_2 = 2.
  h_BC (rows q = 3..0, columns p = 0..3): (0,0,1,1), (0,1,2,1), (0,2,1,0), (1,0,0,0);
  h_A: (0,0,0,1), (0,1,2,0), (1,2,1,0), (1,1,0,0); by total degree h_BC^k = (1,0,2,2,2,2,1), h_A^k = (1,2,2,2,2,0,1),
  Delta^k = h_BC^k + h_A^k - 2 b_k = (0,2,4,4,4,2,0).
- **Support**: E_2 = E_infinity: ten lines, from the Hodge table and b_k = 0 (1 <= k <= 5); it holds for every value of
  m = h^{1,2}. Bott-Chern: substitution in McHugh's formulas for compact threefolds (Theorem 6.3, Prop. 6.4, eq. (7), §7.1) with
  k^{p,q} <= b_{p+q} (proved in the text), E_2^{3,1} = 0; Aeppli by Schweitzer's duality. Workbench: VERIFIED (S6-HODGE-PARAM,
  S6-HODGE-BCA).
- **What it adds**: [AC26] Cor. 9.22 has only "no degeneration at E_1" and injectivity of d: H^{0,1} -> H^{1,1}; Bott-Chern and
  Aeppli are not in [AC26] or [E26]. Literature: McHugh's table for a hypothetical S^6 (read through ar5iv) gives
  h_BC^{1,1} = 2 + 2h^{0,2}, h_BC^{1,2} = h_BC^{2,1} = h^{1,2} + h_2^{0,2}, h_BC^{2,2} = 2h^{1,2} + 2h_2^{0,2} - 2h^{0,2},
  h_BC^{2,3} = h_BC^{3,2} = 1 + h^{0,2} + h^{2,0}; with h^{0,2} = h^{2,0} = h_2^{0,2} = 0, h^{1,2} = 1 this is exactly the
  workbench's table. So B-2 is B-1 plus known general formulas.
- **First assessment**: correct given B-1. Checks: McHugh's S^6 table reproduces (11.21); Angella's relation
  h_BC^{2,2} = 2 h_BC^{2,1} - 2h^{0,1} + 2 = 2 holds; I re-proved h_BC^{1,1} = 2h^{0,1} directly (b_1 = b_2 = 0). The summary of
  McHugh's paper returned by the fetch tool flagged a possible inconsistency inside that paper (k^{3,1} against k^{2,0} in
  h_BC^{3,2}); it does not matter here because all k^{p,q} vanish in middle degrees.
- **A full check must establish**: B-1; McHugh's formulas as printed (read the source, arXiv:1708.03251v3); the inequality
  k^{p,q} <= b_{p+q}.
- **Deserves a full check**: maybe; it is short once B-1 holds. **Interest**: 4.

### B-3
- **Title**: The Bott-Chern algebra of X: nine generators, H_BC = C1 + N with N^2 = 0; c_{1,BC}(exp(z g)) = zA + z^- B;
  exp(12 g) = f^*O(1). **Type**: new result.
- **Where**: `bott_chern_algebra.tex`, `lem:bcpr-eta-extension` (L220), L371-486, `prop:bcpr-generators-are-bases` (L513),
  `thm:bcpr-square-zero-algebra` (L626). 30 Aug - 4 Sep 2026.
- **Statement**: Let g in H^{0,1}(X) be the class of gamma^{0,1}, q in H^{1,1}(X) a class restricting on smooth fibres to the
  class of eta (fibre representative Q_F = (2 i y Delta)^{-1}(r dz_1 dz^-_1 - 6m dz_1 dz^-_2 - 6m dz_2 dz^-_1 + 6y dz_2 dz^-_2),
  y = Im tau, m = Im mu, r = Im beta, Delta = r - 6m^2/y), with d-bar-closed representatives G, Q. Then
  A = [dG], B = [d-bar G^-] span H^{1,1}_BC; C = [dQ] (2,1), C^- (1,2); D = [d(G^Q)], D^- span H^{2,2}_BC; E = [d(Q^2)] (3,2), E^- (2,3);
  T (3,3) (here d means the (1,0) part "partial"). Every product of two positive-degree classes is zero.
  The map Pic(X) = C -> H^{1,1}_BC is z -> zA + z^- B, and exp(12 g) = f^*O_B(1) (up to the orientation sign).
- **Support**: written proof, about 400 lines; uses B-1 (dimensions, exact rows), R^1 f_*Omega^1_X = ker kappa_1, H^0(B, R^1 f_*Z) =
  Z(12 gamma) and d_2(12 gamma) = generator (from integral_leray.tex), Serre duality, Stokes. Workbench: VERIFIED
  (S6-OPEN-HODGE-REPRESENTATIVES); it states that no literal global formula for G, Q is given.
- **What it adds**: nothing of this is in [AC26] or [E26]. [AC26] Prop. 10.8 normalises L_12 = f^*O(1) by rescaling; the workbench
  shows the canonical coordinate from the primitive class gamma gives exactly 12. Literature: not searched beyond B-2's sources.
- **First assessment**: the product theorem is a formal consequence of the dimension table plus three small arguments, which I
  read and found sound: A^2 + B^2 = 0 from the square of a form pulled back from the curve, then A^2 = 0 through injectivity of
  d_1 on H^{1,2}; AC = 0 through the Serre pairing with [G]; top-degree products by d-exactness. One thing to check: the proof
  that [Q_F] != 0 and [Gamma ^ Q_F] != 0 uses integrals with signs depending on the orientation convention (y Delta < 0).
- **A full check must establish**: B-1; extension of the class eta over the three special fibres as a section of ker kappa_1;
  the list of products is exhaustive; the factor 12 and its sign (depends on d_2(12 gamma) in integral_leray.tex).
- **Deserves a full check**: maybe; a clean statement for a paper on the invariants, but dependent on B-1. **Interest**: 3.

### B-4
- **Title**: Omega^1_{X/B} is torsion-free but not locally free along W; its torsion sits exactly on the multiple fibres.
  **Type**: correction of [AC26].
- **Where**: `hodge_frolicher.tex` L811-1008 (remark, (11.17a)-(11.17f)); ledger S6-HODGE-CUSP-TORSION (REFUTED). 27 Aug 2026.
- **Statement**: [AC26] Remark 1.3 (L270: "the sheaves Omega^p_{X/B} along the three singular fibres, where they have torsion")
  and Remark 9.21 (L4330: "Omega^1_{X/B} has torsion along W u S_1 u S_2") are wrong at W. At t = xy and t = xyz,
  Omega^1_{X/B} injects into the free module E with image R dz + (x,y)R e, resp. <x e_1, y e_2, z(e_1+e_2)>; at a multiple fibre
  t = s^m the pullback to the cover is R dy_1 + R dy_2 + (R/(s^{m-1})) ds. Also 0 -> Omega^1_{N_0/Delta} -> E|_{N_0} -> i_*Q -> 0
  with Q = nu_*O_{dP_6}/O_W, h^.(Q) = (2,1,0).
- **Support**: local module computations in the text. **What it adds**: corrects two remarks of [AC26] (not a theorem there).
  [E26]: not discussed. Literature: standard local algebra; not searched.
- **First assessment**: correct. I checked the case t = xy by hand: g*omega in R(y dx + x dy) forces omega in R(y dx + x dy)
  because gcd(x, y) = 1.
- **A full check must establish**: nothing beyond the three local models.
- **Deserves a full check**: no (verified here at the level needed). **Interest**: 2.

### B-5
- **Title**: The logarithmic Kodaira-Spencer divisor: div(det kappa_0) = p_1 + p_2; K = det(dZ/dz) vanishes to order 2 at the
  order-3 point, is non-zero at the order-4 point and on B^o; f_*E -> (f_*T_{X/B})^dual has elementary divisors (1, t) at p_1, p_2.
  **Type**: new result (part of the proof of B-1, of independent use).
- **Where**: `hodge_frolicher.tex`, `prop:period-derivative-determinant` (L218), `prop:log-ks-divisor` (L525), (11.4)-(11.11).
- **Statement**: as in the title; in particular the period map of the torus family is an immersion in the sense det(dZ) != 0
  everywhere on the smooth base, "maximal variation" fails exactly to first order at z_1 (dmu/dz = -(1/3) dtau/dz,
  dbeta/dz = (2/3) dtau/dz there), and direct image does not commute with duals at the multiple fibres.
- **Support**: proof in the text (degree count on O(2), equivariance ord_s K = 2a - 2 mod m). Ledger S6-HODGE-KS: VERIFIED.
- **What it adds**: not in [AC26] (Lemma 9.14(iii) has only dtau/dz != 0 on the smooth locus) or [E26]. Not searched.
- **First assessment**: consistent: ord_s K = 2 mod 3 at z_1 is forced by equivariance alone, and the degree count then leaves
  exactly one more simple zero, at p_2, which comes from the prefactor s^4 = t. Same weak points as B-1.
- **A full check must establish**: as B-1 items (2)-(4).
- **Deserves a full check**: yes, together with B-1. **Interest**: 3.

### B-6
- **Title**: The family X_c (beta_c = beta^part + c, Im c < -M) is a proper holomorphic submersion and its Kodaira-Spencer class
  is non-zero; h^1(X, T_X) >= 1. **Type**: new result (complete proof of what [E26] Remark 8.1 sketches).
- **Where**: `period_parameter_deformation.tex`, `thm:retained-period-deformation`, (PD1)-(PD18); domain from
  `candidate_geometry.tex` `prop:period-exact-admissible-constants` (L563). 5-6 Sep 2026.
- **Statement**: For every disc Q with closure in P = {Im c < -M}, M = max over B \ {p_0} of
  D_part = Im beta^part - 6(Im mu)^2/Im tau (finite, attained; the period map is a real isomorphism everywhere exactly for
  Im c < -M), there is a proper holomorphic submersion pi: X_Q -> Q with a map F: X_Q -> B x Q restricting to f_c on each fibre.
  On a regular fibre, with T = Im tau, m = Im mu, D = Im beta_{c_*} - 6m^2/T, a = m/T, P = [[0,0],[-a,1]], delta = c - c_*:
  w = A_delta z + B_delta z^-, A_delta = I + (delta/2iD) P, B_delta = -(delta/2iD) P; Beltrami matrix nu_delta = delta P/(2iD + delta);
  d nu/d delta at 0 = (1/2iD) d/dz_2 (x) (dz^-_2 - a dz^-_1), whose class in H^{0,1}(F, T^{1,0}) is non-zero; KS(d/dc) = -[that].
  The relative anticanonical pencil omega^{-2}_{X_Q/Q} = F^* pr_B^* O_B(p_2) recovers f over C[eps]/(eps^2); the three critical
  values are fixed to first order; hence the first-order deformation of the whole X_c is non-trivial.
- **Support**: written proof, about 320 lines, self-contained except for the charts of candidate_geometry.tex and B-9. Workbench:
  VERIFIED; its own non-claim: "No sphere-topology, CDP disproof, global injectivity of parameter-to-isomorphism classes, or
  versality is inferred."
- **What it adds**: [AC26]: the constant c_0 appears as a choice (§3.4); I did not find a statement there that the complex structure
  varies with it (reader of §§3-6 should confirm). [E26] Remark 8.1 argues in three lines (uniqueness of the map to P^1, periods
  vary, the curves E_0, E_1 vary). Literature: Viaclovsky, arXiv:2610.39102 (29 Oct 2026), Prop. 4.7, proves that the u-family is
  not locally isotrivial and deduces Kuranishi dimension >= 1 (per the fetched summary); his Question (2), whether u gives all
  small deformations, is open. So the non-triviality has since appeared in print by another route; the workbench's proof is
  seven weeks earlier and gives the explicit class.
- **First assessment**: sound at reading. The fibre computation is elementary ((PD4) is Pi(z,c) Pi(z,c_*)^{-1}). The step from the
  fibre to X uses that a first-order trivialisation must commute with f, which is where B-9 enters; the argument that the
  three critical values cannot move infinitesimally is done with critical ideals and looks right.
  Not computed in the workbench: h^1(T_X) and h^2(T_X) themselves, unobstructedness, completeness. My own remark: from
  chi(T_X) = 1, h^0(T_X) = 1 ([AC26] Thm 9.1(iv),(v)) and h^3(T_X) = h^0(Omega^1 (x) K_X) = h^0(Omega^1_X(-2S_2)) = 0 one gets
  h^2(T_X) = h^1(T_X) >= 1, so the obstruction space is not zero and unobstructedness is a real question.
- **A full check must establish**: joint holomorphy and properness of the three kinds of charts in (z, c); (PD4)-(PD5);
  (PD16)-(PD18); the critical-scheme argument; the sign conventions are immaterial for non-vanishing.
- **Deserves a full check**: maybe; the statement is now also in the literature, but this proof is explicit and feeds B-7.
  **Interest**: 3-4.

### B-7
- **Title**: Exact classification inside the family: X_c is biholomorphic to X_{c'} if and only if c' - c is an even integer; the
  parameter space is the punctured disc 0 < |w| < e^{-pi M}, w = e^{-pi i c}. **Type**: new result.
- **Where**: `period_shift_classification.tex`, `pshift:thm:classification`, `pshift:lem:centralizer`, (PS1)-(PS29). 6 Sep 2026.
- **Statement**: It is the strong statement: for c, c' in P the threefolds X_c, X_{c'} are biholomorphic (as abstract complex
  manifolds, no marking and no compatibility with f assumed) iff c' - c in 2Z. Every biholomorphism commutes with the maps to B.
  For even n there is an explicit isomorphism X_c -> X_{c+n} with linear part I_2 on the fibre coordinates and lattice map
  I - nE, E = delta^ (x) gamma. For every integer n the middle families over B^o coincide (Pi_{c+n} = Pi_c (I + nE),
  Pi_{c+n} Lambda = Pi_c Lambda), and so do the cusp actions; the obstruction for odd n is the class of n delta^ in
  Lambda^{A_2}/N_2 Lambda = Z/4 + Z/2 (N_j = 1 + A_j + ... + A_j^{m_j-1}), where delta^ generates the Z/2; at the order-3 fibre
  Lambda^{A_1}/N_1 Lambda = Z/3 and delta^ = N_1 w^ is zero. The rational centraliser of the monodromy is {aI + bE}.
- **Support**: written proof, 590 lines. Necessity: |-2K_X| is f (B-9), the three special fibres have different types, so the
  induced automorphism of P^1 is the identity; fibrewise the map is affine with integral lattice map H commuting with A_1, A_2,
  so H = aI + bE, a = +-1, and the period equation L Pi_c = Pi_{c'} H gives L = aI, c' - c = -b/a; lifting to the normalised
  cyclic covers at p_j gives N_j l_j = -(1-a) v_j - n eps_j delta^ (eps_j = gamma(v_j) = +-1), which excludes a = -1 (3 does not
  divide 2) and odd n (at j = 2). Sufficiency: explicit translations b_j = Pi_c r_j (r_1 = -(n/3)(u^ + w^), r_2 = (n/4)(u^ + w^)),
  the toric map (x, t) -> (t^{q_n} x, t), q_n = (-3n/2, n/2), and a global correction obtained from H^1(B, V) = 0 for the rank-2
  bundle V (extension of O(-1) by O; it is f_*T_{X/B}). Status in the workbench: recorded as integrated on 6 Sep; no separate
  ledger id; no checker named.
- **What it adds**: not in [AC26]. [E26] Remark 8.1 only says the manifolds deform. Viaclovsky 2610.39102 distinguishes different
  multiplicities and, per the fetched summary, "does not prove that different u give non-biholomorphic manifolds".
  X. Yang, arXiv:2609.29666 (13 Sep 2026) proves "uncountably many pairwise non-biholomorphic complex structures" for related
  families of rational homology spheres (abstract only read); a full check should compare methods. I found no statement of the
  2Z phenomenon anywhere.
  Translation to [E26] (my inference, not in the workbench, to be checked): gamma^ is the lattice generator coming from the
  Z-action and delta^ the circle of the G_m-bundle (Pi delta^ = e_2 generates Aut^0 = C^*), so scaling the linearisation by u
  adds log(u)/(2 pi i) to beta up to sign: u = const * e^{-2 pi i c} = const * w^2, and |u| -> 0 is Im c -> -infinity.
  Then the result says: going once around u = 0 the multiplicity class a_1 changes by the 2-torsion class of delta^ in
  Lambda^{T_1}/N Lambda, so Engel's family Y(u, a_0, a_1) -> Delta^* with locally constant (a_0, a_1) closes up only on the
  double cover w^2 = u; for a fixed u the two fillings are not biholomorphic. Also the exact domain: the construction exists
  exactly for |w| < e^{-pi M} (Engel has "u sufficiently small").
- **First assessment**: I re-derived the necessity part in full (period equation, equation (PS10), the norm obstruction) and it
  is correct. My script confirms with exact arithmetic: A_j = (T_j^{-1})^t for the matrices of [AC26] (A.1); A_1^3 = A_2^4 = I;
  A_j v_j = v_j; A_j E = E A_j = E; N_1, N_2 as printed; centraliser = {aI + bE}; identity (PS14); Lambda^{A_1}/N_1 Lambda = Z/3
  with delta^ = 0, Lambda^{A_2}/N_2 Lambda = Z/4 + Z/2 with delta^ of order 2; cocycle value (PS21). The sufficiency part
  (gluing with the logarithmic terms, extension over all cusp strata) I read without finding a gap but did not recompute.
  Risk: the identification "J'_j is the normalisation of the base change" (cited from finite_filling_certificates.tex) and the
  use of the retained fillings: the theorem is about this family with its fixed (l_0, l_1, l_2); other discrete choices are
  outside it.
- **A full check must establish**: (1) intrinsicness of f (B-9 or the algebraic reduction); (2) the lifting of a biholomorphism of
  N_j to J'_j commuting with the generator; (3) (PS10)-(PS12); (4) the even-shift maps (PS13)-(PS28) including the overlap
  identities with the original gluings; (5) L = O(-p_0) and H^1(B, V) = 0; (6) the dictionary u <-> c with [E26] and the
  resulting statement about multiplicity classes; (7) literature after 6 Sep 2026.
- **Deserves a full check**: yes; a precise new theorem with a visible mechanism (an order-two filling invariant), and it corrects
  the naive picture of the parameter. **Interest**: 5.

### B-8
- **Title**: Anticanonical ring: omega_X = O_X(-2S_2), f_*O_X(kS_2) = O_B(floor(k/4) p_2),
  sum_m H^0(X, omega_X^{-m}) = C[U,V] with degrees 1, 2; |-2K_X| is f. **Type**: refinement of [AC26] (new restatement and
  consequence of Prop. 9.11).
- **Where**: `analytic_canonical_ring.tex`, `thm:canonical-ring-recovery` (CR1)-(CR5), and L161-169. 6 Sep 2026.
- **Statement**: the evaluation f^*f_*omega_{X/B} -> omega_{X/B} has zero divisor exactly 2S_2; omega_X = O_X(-2S_2),
  omega_X^{-2} = f^*O_B(p_2); h^0(omega_X^{-m}) = floor(m/2) + 1, h^0(omega_X^m) = 0 (m > 0); the degree-1 system is the single
  divisor 2S_2, the degree-2 system is base-point free with map f. In the Picard coordinate with L_12 = f^*O(1):
  O(S_1) = L_4, O(S_2) = L_3, omega_X = L_{-6}.
- **Support**: proof of 110 lines from `lem:hodge-line-audit`. Ledger: VERIFIED.
- **What it adds**: [AC26] has K_X = f^*O(-1) (x) O(2S_2) (Prop. 9.11) and K_X not torsion; it does not remark that -K_X = 2S_2 is
  effective, nor the ring, nor that f is the bi-anticanonical map. [E26]: nothing. Viaclovsky 2609.33785 (26 Sep 2026)
  Remark 6.3 quotes h^0(-K) = 1 for the Alpöge-Claude threefold and uses the anticanonical pencil for his own family (fetched
  summary), so the idea is now in print in a neighbouring case.
- **First assessment**: correct; f^*O(-1) = O(-4S_2) gives (CR1) at once; (CR2) checked for k < 0 and k >= 0. Consequences not
  stated in the workbench (mine): the anti-Kodaira dimension is 1; since a very general fibre has NS = Z eta with eta indefinite
  it carries no curves, so every divisor of X is vertical and the classes of divisors form the subgroup Z = <L_1>,
  L_1 = O(S_1 - S_2), of Pic(X) = C.
- **A full check must establish**: the exponents k_j = m_j - 1 - a_j = (0, 2) (already [AC26] Lemma 9.10) and (CR2).
- **Deserves a full check**: maybe (short). **Interest**: 3.

### B-9
- **Title**: General criterion replacing the CDP20 p. 692 step: with K_S the kernel of Omega_X|_S -> Omega_S/torsion, the two printed
  vanishings give H^0(S, Omega_X|_S (x) A) = ker(delta_A: H^0(T_S (x) A) -> H^1(N^* (x) A)). **Type**: correction of the literature
  (sharpening of [AC26] §10.2-10.4); a statement about arbitrary reduced Cartier divisors, independent of S^6.
- **Where**: `cdp_program.tex`, `prop:missing-cotangent-filtration` (L52), `prop:missing-global-section-criterion` (L81),
  `prop:conductor` (L209). 26-29 Aug 2026.
- **Statement**: S a reduced effective Cartier divisor in a smooth complex threefold X, T_S = ker(Omega_S -> j_*Omega_{S_reg}),
  A a line bundle on S. There are exact sequences 0 -> N^*_{S/X} -> K_S -> T_S -> 0 and 0 -> K_S -> Omega_X|_S -> Omega~_S -> 0.
  If H^0(S, Omega~_S (x) A) = 0 then H^0(Omega_X|_S (x) A) = H^0(K_S (x) A); if also H^0(N^* (x) A) = 0 this is ker delta_A. "Hence
  the two vanishings printed in the p. 692 reduction imply the desired ambient vanishing if and only if delta_A is injective."
  Conductor theorem: for a proper g: X -> Delta with reduced normal-crossings fibre S (local forms g = ux, uxy, uxyz),
  normalisation eta, and A with eta^*A trivial, there is a unique non-zero s in H^0(S, Omega_X|_S (x) A) with
  eta^*s = eta^*(dg) (x) e and s|_D = 0; its image in Omega_S (x) A is torsion; if S is connected and A non-trivial, H^0(S, A) = 0.
- **Support**: short complete proofs. Ledger: S6-CDP-CONDUCTOR VERIFIED, S6-CDP-P692 REFUTED.
- **What it adds**: the conductor theorem is [AC26] Lemma 10.3 with Remark 10.4 (normal case). New here: the filtration and the
  "if and only if delta_A injective" form, valid for any reduced Cartier divisor (not only normal crossings). [E26] omits CDP.
  Literature: searched for an erratum or a 2026 paper on the CDP gap: none found; Liu-Rollenske (footnote 1) say the gap
  "was known only to a few experts".
- **First assessment**: correct (elementary homological algebra; I re-derived both sequences).
- **A full check must establish**: that the CDP20 text on p. 692 is as quoted in [AC26] L4473-4479 (primary source:
  arXiv:1904.11179v2 or the journal).
- **Deserves a full check**: maybe; small but exactly the right general statement for an erratum. **Interest**: 3.

### B-10
- **Title**: A proper test family for the p. 692 inference: (pencil of plane cubics with a nodal member) x P^1 with a
  non-torsion gluing bundle. **Type**: correction of the literature (counterexample to a printed inference), independent of S^6.
- **Where**: `cdp_program.tex`, `prop:nodal-counterexample` (L278-353). 26 Aug 2026.
- **Statement**: C = {y^2 z = x^2(x+z) + t z^3} in P^2 x Delta (smooth total space, C_0 nodal), X = C x P^1, S = C_0 x P^1,
  A = pr_1^* A_lambda with A_lambda in Pic^0(C_0) the bundle glued by lambda not a root of unity. Then
  H^0(S, N^* (x) A) = H^0(S, A) = 0 and H^0(S, Omega~_S (x) A) = 0 (it injects into H^0(P^1 x P^1, Omega^1) = 0), yet
  H^0(S, Omega_X|_S (x) A) != 0. The file states the limits: A is not claimed to extend to X, and the family does not satisfy
  the hypotheses of CDP Theorem 2.2.
- **Support**: one page. **What it adds**: [AC26] shows the failure only at W itself; this is a two-line example with no
  dependence on the construction. Not in [E26]. Literature: not found elsewhere (same search as B-9).
- **First assessment**: correct. Hand check: Omega_X|_S = (Omega_C|_{C_0} box O) + (O box Omega_{P^1}); on C_0,
  0 -> A_lambda -> Omega_C|_{C_0} (x) A_lambda -> Omega_{C_0} (x) A_lambda -> 0 with H^0(A_lambda) = H^1(A_lambda) = 0, and
  Omega_{C_0} has a one-dimensional torsion at the node, so h^0 >= 1; delta_A cannot be injective because its target
  H^1(S, A) is 0.
- **A full check must establish**: nothing further; decide how to phrase it (it refutes a formal implication for a bundle on the
  fibre, not for a bundle on the total space).
- **Deserves a full check**: no (checked here). **Interest**: 3.

### B-11
- **Title**: "Corrected CDP theorem": if H^2(X, T_X (x) L_0) = 0 for one L_0 then c_3(X) <= 0; sufficient relative and fibrewise
  conditions; contrapositive for X. **Type**: correction of the literature (conditional replacement); claim S6-OPEN-CDP-REPAIR.
- **Where**: `cdp_program.tex`, `lem:cdp-generic-endpoints` (L1368), `thm:corrected-cdp-global` (L1408),
  `cor:corrected-cdp-relative` (L1471), `thm:corrected-cdp-fibrewise` (L1502), remark L1562, (5.33). 30 Aug 2026.
- **Statement**: (a) X a compact connected complex threefold with H^1(X;Z) = H^2(X;Z) = 0, a(X) = 1, holomorphic algebraic
  reduction f: X -> C. If there is L_0 in Pic(X) with H^2(X, T_X (x) L_0) = 0, then for M in a dense open subset of Pic(X):
  H^i(X, T_X (x) M) = 0 (i != 1), chi(X, T_X (x) M) <= 0 and <c_3(T_X), [X]> <= 0. (b) It suffices that R^2 f_*(T_X (x) L) = 0 for
  one L (this is CDP20 Prop. 2.4). (c) If every full fibre W_c is reduced and, for A_c = (omega_X (x) L^dual)|_{W_c},
  H^0(W_c, Omega~_{W_c} (x) A_c) = 0, H^0(W_c, N^* (x) A_c) = 0 and delta_c is injective for every c, then (b) and (a) hold.
  Non-reduced fibres are not covered by (c). For the constructed X (c_3 = 2): H^2(X, T_X (x) L_0) != 0 and
  R^2 f_*(T_X (x) L) != 0 for every L. Monodromy: the CDP98 rank argument is valid exactly when the invariant lattice
  H^1(F;Z)^{pi_1} spans H^1(F, O_F) over C (5.33).
- **Support**: proofs of about 200 lines; standard tools (semicontinuity on Pic(X) = H^1(X,O), Serre duality, HRR with
  c_1 = c_2 = 0 rationally, Leray, Serre vanishing on the base, B-9, duality and base change). Ledger: VERIFIED.
- **What it adds**: [AC26] §10.6 says what an argument "would have had to control" and Cor. 10.6 lists which conclusions fail;
  the workbench turns this into theorems. Is it a real repair of CDP20 Theorem 2.2? In my reading, no: it is the intact part of
  the CDP strategy with the failing step moved into the hypotheses. Statement (a) needs only an effective divisor, not
  a(X) = 1; (b) is CDP's own proposition; (c) restates B-9 fibre by fibre. No geometric condition on X (for example "all
  fibres of the reduction are normal") is shown to imply the hypotheses, and the supply of a line bundle non-torsion on every
  fibre (CDP20 §5) is not repaired in general. The ledger's wording "the strongest intact replacement" is not proved in any
  sense. What is useful and correct: the clean contrapositive (any compact complex threefold with b_1 = b_2 = 0 (integrally),
  an effective divisor and c_3 > 0 has H^2(X, T_X (x) L) != 0 for all L; if it fibres over a curve, some fibre has
  H^0(X_c, Omega_X|_{X_c} (x) A_c) != 0 for every L), and the list of exactly which CDP statements survive.
- **First assessment**: the proofs are correct as far as I read; HRR: chi(T_X (x) M) = c_3/2 checked. The open problem it isolates
  is better than the theorem: find geometric hypotheses under which c_3 <= 0 does hold (for instance: must a threefold with
  b_1 = b_2 = 0, a = 1 and c_3 > 0 have a non-normal fibre or a fibre where delta_c fails to be injective?).
- **A full check must establish**: the family of line bundles over Pic(X) used for semicontinuity; the reading of CDP20
  Prop. 2.4, §5 and §7 against the primary source; an honest formulation of what is and is not repaired.
- **Deserves a full check**: maybe; needed if an erratum-type note on CDP is written, but it is conditional. **Interest**: 3.

### B-12
- **Title**: CDP98 Lemma 3.2 / CDP20 Lemma 4.2: abelianisation of a split extension needs coinvariants. **Type**: correction of
  the literature, already in [AC26]; the workbench adds a minimal counterexample and the exact repair condition.
- **Where**: `cdp_program.tex` L1302-1358, L1592-1606. Ledger S6-CDP98-MONO (REFUTED).
- **Statement**: (K x| Q)^ab = Q^ab + (K^ab)_Q; G = Z x|_{-1} Z has G^ab = Z + Z/2; b_1(X^o) = s - 1 + dim H_1(F;Q)_{pi_1}.
- **What it adds**: [AC26] Lemma 10.7 and §10.5 have the lemma, the corrected count r = s - 1 + t' and a bielliptic example;
  new are the two-line example and (5.33). **First assessment**: correct, trivial.
- **Deserves a full check**: no. **Interest**: 2.

### B-13
- **Title**: Pic(X) -> Pic(dP_6) is zero, proved three ways; in particular a proof by O^* cocycles that c_1(L|_F) = 0 for every
  line bundle, with the primitive obstruction 4 - 3 = 1 (resp. 2 - 3/2 = 1/2). **Type**: new proof of a known result
  (the statement follows from H^2(X;Z) = 0).
- **Where**: `cdp_program.tex` L602-1141 (`prop:leray-edge-restriction`, `prop:direct-boundary-picard`),
  `analytic_picard_completion.tex` (`prop:analytic-ah-boundary`, `thm:analytic-all-picard`). 28-30 Aug, corrected 5 Sep 2026.
- **Statement**: for L in Pic(X) with c_1(L|_F) = kq there is a crossed homomorphism d: pi_1(pair of pants) -> V_R, unique up to
  principal ones, with d_1 + T_1 d_2 + T_1 T_2 d_0 = 0, N_{T_j} d_j = iota_{v_j}(kq) (so d^-_1 = 2k[delta], d^-_2 = -(3/2)k[delta] in
  V_G (x) R = R[delta], using iota_{v_1} q = 2 eta_1, iota_{v_2} q = -3 eta_2, [eta_1] = 3[delta], [eta_2] = 2[delta]) and
  d^-_0 = 0 at the cusp; hence k = 0.
- **Support**: long proofs (about 900 lines in total) with careful conventions; checkers with 14 and 25 integer checks; the
  5 Sep audit corrected one formula without changing the result. Ledger: VERIFIED (S6-CDP-R-LERAY, -R-BOUNDARY,
  S6-OPEN-R-ANALYTIC).
- **What it adds**: [AC26] Theorem 10.5 Step 1 gets (10.5) from H^2(X;Z) = 0 in one line. The workbench removes the dependence
  on the topology theorem ("three proofs with different dependency sets"); for L in Pic^0 no topology at all is needed
  (`cor:candidate-pic0-route`). Mathematically this is redundancy, valuable as an independent confirmation of the count
  12 l_0 - 4 l_1 - 3 l_2 = +-1 seen holomorphically. Not in [E26]. Not searched.
- **First assessment**: arithmetic confirmed by my script (iota_{v_1} q = (0,4,2,6) = 2 eta_1, iota_{v_2} q = (0,-3,-3,-6) =
  -3 eta_2). The geometric lemmas were read, not recomputed.
- **A full check must establish**: only needed if one wants a topology-free proof of Theorem 10.5; then the sign conventions
  of (5.17-A14)-(5.17-A20).
- **Deserves a full check**: no (redundant with the topology theorem). **Interest**: 2.

### B-14
- **Title**: A cusp-local line bundle with non-zero normalised restriction, and the formula linking the degrees on the hexagon
  of dP_6 to the Appell-Humbert form of nearby fibres. **Type**: new result (local; statement about the Mumford degeneration).
- **Where**: `analytic_picard_local_obstruction.tex`, `prop:local-cusp-picard-obstruction`;
  `analytic_picard_completion.tex`, `lem:analytic-support-specialization` (L629). 29-30 Aug 2026.
- **Statement**: on the toric cover Y_eps of the cusp neighbourhood N_0, D_Q = sum_{v in Z^2} (v_1^2 - 6 v_2^2) E_v is a locally
  finite Cartier divisor; O(D_Q) has an explicit equivariant structure for the Z^2-action Psi (factors
  f_lambda = exp(pi i lambda^t A(t) lambda) chi^{m_lambda}, A = 2PC symmetric) and descends to L_Q in Pic(N_0) with
  c_1(L_Q|_{F_t}) = -2q and degrees (-12, 2, 0, -12, 2, 0) on the six curves of the hexagon. In general, for M in Pic(N_0) with
  degrees (d_1, d_2, d_3, d_1, d_2, d_3) on the hexagon, E_M((lambda,0),(0,m)) = -B(B_0 lambda, m) with
  B = [[d_2 + d_3, d_3],[d_3, d_1 + d_3]]; so E_M = 0 forces nu^*(M|_W) trivial, and Pic(N_0) -> Pic(dP_6) is not zero.
- **Support**: complete computations; two sign audits (29 Aug); ledger VERIFIED (S6-CDP-R-LOCAL-OBSTRUCTION).
- **What it adds**: not in [AC26] or [E26] ([E26] Remark 8.4 notes that the invariant class of type (1,6) is a Chern class on
  each fibre). It shows that the class 2q (and presumably q, with a(v) = v_1(v_1-1)/2 - 3v_2^2; my remark, unchecked) extends
  as a line bundle over the cusp neighbourhood but not over X. Literature: this is the usual dictionary between Z^2-quasi-
  periodic piecewise-linear functions and polarisations in Mumford's construction (Mumford 1972, Alexeev-Nakamura); not
  searched for the exact statement. Probably known in substance.
- **First assessment**: the numbers are consistent: Q(a_i) = (1,-6,-5,1,-6,-5), degrees -Q(a_i) + Q(a_{i-1}) + Q(a_{i+1}) give
  (-12,2,0,...); B = 2H = diag(2,-12) matches the general formula.
- **A full check must establish**: the cocycle identity (5.17al) and the sign of the Chern class.
- **Deserves a full check**: no, unless the local Picard group of the degeneration is wanted. **Interest**: 2-3.

### B-15
- **Title**: Re-derivation of R^q f_*O_X, Pic(X) = C and Prop. 10.8, with three changes of proof. **Type**: new proof /
  expository.
- **Where**: `analytic_picard.tex` (whole file). 26 Aug 2026.
- **Statement**: as [AC26] Props. 9.11, 9.13, Thm 10.5(b), Prop. 10.8. Changes: the extension of gamma^{0,1}, u^{0,1} over the
  cusp uses the nearby-cycle isomorphism instead of the cellular collapse; the canonical section (divisor k_j S_j) is kept
  apart from the generator of f_*omega_{X/B}; the restriction line iota_q(C) is identified with the gamma^{0,1}-summand, which
  removes [AC26]'s continuity argument for the integral lift lambda_0(q); the order of O(S_j)|_{S_j} is proved by characters.
- **What it adds**: no new statement. **First assessment**: fine. **Deserves a full check**: no. **Interest**: 1-2.

### B-16
- **Title**: General tools stated with full hypotheses: duality on a compact Cartier divisor without normality; top-degree
  base change for surface fibres including non-reduced ones; flatness over a curve. **Type**: expository only (known results).
- **Where**: `cdp_program.tex` L355-600. **Statement**: H^q(W, F)^dual = H^{2-q}(W, F^dual (x) omega_W), omega_W = (omega_X (x) O(W))|_W
  (Ramis-Ruget); R^q f_*E = 0 (q > 2) and (R^2 f_*E)_b (x) C(b) = H^2(X_b, E|_{X_b}) for all b (Banica-Stanasila III.3).
- **What it adds**: [AC26] Theorem 10.5 Steps 2-3 cite the same theorems. **Deserves a full check**: no. **Interest**: 1.

### B-17
- **Title**: Open questions that the files isolate or leave. **Type**: open question isolated.
- **Where / Statement**:
  (a) h^1(X, T_X) = h^2(X, T_X) (equality is my remark, see B-6): its value; is the w-family complete / versal; is X
      unobstructed? Not computed in the workbench (`period_parameter_deformation.tex` L386-391 says so). The machinery of B-1
      (invariant bases, kappa_0, residues) applied to T_X(-log D) should decide it. Viaclovsky's Question (2) asks the same.
  (b) The limit w -> 0 (Im c -> -infinity), i.e. [E26] Conjecture 8.2: nothing in my files.
  (c) The boundary |w| = e^{-pi M}: where D_part attains its maximum a fibre degenerates; what happens there is not studied.
  (d) Which geometric hypotheses make the CDP conclusion c_3 <= 0 true (B-11).
  (e) Human replication of B-1 (the workbench's own OPEN item).
  (f) Whether a literal global formula for the forms G, Q exists (bott_chern_algebra.tex, two remarks).
  (g) Relation of X_c to the other 2026 families (Viaclovsky's two-parameter family has h^0(-K) = 2 against 1 here).
- **Deserves a full check**: (a) yes as a new computation. **Interest**: 4 for (a), 3 for (b)-(d).

---

## 3. Doubts and errors

1. `claim_ledger.txt` S6-OPEN-CDP-REPAIR and `mathematical_summary.tex` L1001: "the strongest intact replacement for CDP20
   Theorem 2.2" / "the strongest corrected CDP conclusion". No maximality is proved; the theorem is conditional on exactly the
   vanishing whose proof failed. In `thm:corrected-cdp-global` the hypotheses "a(X) = 1, holomorphic algebraic reduction" are
   used only to have a non-zero effective divisor.
2. `cdp_program.tex` L138-141 (proof of `lem:conormal-injective`): the letter f is used for the local equation that is called
   g in the statement ("the term f du vanishes after restriction to f = 0", "it suffices to use f = x, xy, xyz"). Slip of notation.
3. The identifiers S6-OPEN-R-ANALYTIC, S6-OPEN-HODGE-REPRESENTATIVES, S6-OPEN-CDP-REPAIR have status VERIFIED; the word OPEN in
   the id is historical (the ledger says so for the first). `claim_ledger_index.txt` users should not read them as open.
4. `claim_ledger.txt` S6-HODGE-CUSP-TORSION cites only "Remark 1.3" of the original; the same wrong sentence is also in
   Remark 9.21 ([AC26] L4330).
5. The classification theorem (`period_shift_classification.tex`) has no ledger id of its own and no named checker, although
   it is the strongest statement among the 6 Sep additions; the deformation entry (S6-RETAINED-PERIOD-DEFORMATION-20260906)
   still carries the non-claim "no global injectivity of parameter-to-isomorphism classes", which the same day's classification
   supersedes. The "independent GLOBAL_AUDIT.md" and "checker 15 identities" cited there were not found in the folders I read.
6. `verify_direct_boundary_picard.py`: checks "order-four pure-q parity" and "primitive boundary obstruction" compare
   constants with constants; the count "14/14" overstates what is tested (the docstring is honest about scope).
7. `hodge_frolicher.tex`: heavy reuse of letters (B: base and a matrix entry in (11.10a); A: a ring, the sheaf script-A and a
   matrix entry; D: divisor and D_0; T: a torsion sheaf and Im tau elsewhere). No error found, but a checker must watch it.
   L1049: R_{g_2} is written [[1/tau, 0], [-mu/tau, 1]]; `analytic_picard.tex` L72 writes it with tau(g_2 z), mu(g_2 z); the two
   agree (checked).
8. `hodge_frolicher.tex` `thm:h12-scalar`: the value a(z_2) = 1/2 is computed but then multiplies tau'(z_2) = 0, so it plays no
   role; the theorem rests on mu'(z_2) != 0, which is derived from the degree count and not from an evaluation. Not an error,
   but the proof would be more convincing with a direct evaluation.
9. `analytic_picard.tex` L79: "tau(z_1) = rho = e^{pi i/3}" and second eigenvalue rho - 1 = e^{2 pi i/3}; consistent with
   [AC26] Lemma 9.10. No issue; noted because [E26] uses omega = e^{2 pi i/3} for the same point up to translation.
10. `cdp_program.tex` disposition item 6 and `test:cdp-comparison` say the repair "bypasses both refuted dependencies"; it
    bypasses them by assuming their conclusion. See item 1.
11. Wording dated before 5 Oct ("candidate", "does not certify the global construction") occurs throughout, including in files
    of 6 Sep that say "without using the claimed identification of its total space with S^6". This is caution of the time, as
    the brief says; it also means that B-6, B-7, B-8 were deliberately made independent of the topology.
12. My translation u = const * w^2 between Engel's parameter and c (B-7) is an inference from the roles of gamma^ and delta^; I did not
    find it in the workbench and did not prove it.

---

## 4. Not read

- `mathematical_summary.tex`: only the parts listed in 1.10; L200-440 and L640-980 and L1135-3782 not read except by keyword
  search (most of it is outside S6 or repeats the files above).
- `ledgers\claim_ledger.txt`, `uncertainties.txt`: only the matching entries; `morphism_ledger.txt`, `dependency_ledger.txt`,
  `next_lemmas.tex`, `research_log.tex`, `status.tex` not read.
- Evidence folder: AUDIT.md §§4-6, `replacement_passages.tex`, `full.diff`, `integration_receipt.md`, the before/after copies:
  not read (they document the two corrections of 5 Sep).
- `verify_analytic_picard_completion.py` and the result JSON files: not read.
- [AC26]: Lemma 9.12 (cohomology of W), Lemmas 9.14-9.16 (L3965-4222) only glanced at; §§1-8 not read (other readers).
  `main.tex` (annotated edition) not consulted.
- `finite_filling_certificates.tex` (input of analytic_picard.tex; cited by B-7 for the normalisation statement): not read,
  it belongs to another reader's topic.
- The course `courses\CG-S6\` and the public repository clone: not consulted (not in my assignment).
- Literature: CDP20 and CDP98 were not read in the primary source (I relied on the verbatim quotations in [AC26] §10 and on
  the 5 Sep audit, which did read arXiv:1904.11179 and math/9607215). Of the 2026 follow-up papers I read only abstracts or
  machine summaries (Viaclovsky 2609.33785, 2610.10451, 2610.39102; Yang 2609.29666) and pp. 1-3 of Liu-Rollenske 2609.33826;
  GFL26, Yan26, Wan26, LLZ26, Che26, Eng26b (cited there) not identified.
