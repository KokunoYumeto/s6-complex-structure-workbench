# A1 notes — core construction and topology of the S6 threefold in the Codex workbench

Reader A1, 12 Nov 2026. Model: Claude Fable 5.2. Survey reading (medium-deep), not a verification.
Folder read: `C:\Users\user\Documents\math\research\s6_recent_results_main\canonical_S6_snapshot\supporting_materials\workbench\research\`
(all file dates on disk are 29 Sep 2026, a copy date; content dates are taken from `ledgers\research_log.tex`).
Baselines: [AC26] = `canonical_S6_snapshot\original_clean_transcription.tex` (line numbers below are lines of that file);
[E26] = `workbench_review_20261112\literature\engel_S6.txt`.
Scratch: `work\scratch\A1\check_a1.py` (exact sympy checks, all pass) and `work\scratch\A1\ledger_extract.txt`.

Notation used throughout (that of [AC26] and the workbench): V = Z<gamma,u,w,delta>, Lambda = V^* = Z<gamma^,u^,w^,delta^>;
T_1,T_2 of orders 3,4 on V, T_0=(T_1T_2)^{-1}; A_j=(T_j^{-1})^t, M_0=(T_0^{-1})^t on Lambda; Lambda_tor = K_Lambda = <w^,delta^>;
period matrix Pi = [Z | I], Z = [[6mu, tau],[beta, mu]]; D = Im beta - 6(Im mu)^2/Im tau; p = 12 l_0 - 4 l_1 - 3 l_2;
p_1,p_2,p_0 = t=0,1,infinity; S_j the reduced multiple fibres; W the cusp fibre; N_0, N_1, N_2 the three fillings; J the family over B°.
Dictionary to [E26]: Engel's 0,1,infinity = p_1,p_2,p_0; his phi = gamma; his lambda_0 (circle class of M^x) = delta^; his W_{-2} = Lambda_tor;
his u corresponds to exp(±2 pi i c_0) (beta -> beta + c_0 rescales the linearization), his E_0,E_1 are the curves E_1,E_2 of A1-5 below.

---------------------------------------------------------------------------------------------------------------------------

## 1. Reading notes

### 1.1 candidate_geometry.tex (61 KB, 1581 lines; written 24–26 Aug, refined 5 Sep 2026)
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

### 1.2 exact_algebra.tex (19 KB, 587 lines; 24–25 Aug)
"Exact integral algebra of the printed monodromy data". All \Verified. Hand-checkable certificates:
prop:monodromy-certificate (T_1^3=T_2^4=I, T_0, A_1, A_2, M_0, A_1A_2M_0=I); thm:cusp-lattices (ker(M_0-I)=im(M_0-I)=<w^,delta^>; T_0-invariants
of wedge^q V of ranks (1,2,4,2,1), all saturated); thm:coinvariants (V^G=Z gamma, (wedge^2V)^G=Z q, q=uw+6 gamma delta, (wedge^3V)^G=Z gamma uw;
V_G=Z[delta], (wedge^2 V)_G=Z[gamma delta], [uw]=6[gamma delta], (wedge^3V)_G=Z[uw delta]); prop:finite-indices (pi_j^* indices (1,3,1,1,3),
(1,4,2,2,4); pi_2^*H^2(S_2)={a gamma eta_2 + b q : a ≡ b mod 2}, by LHS spectral sequence + evenness of the form); prop:terminal-group
(G(l_0,l_1,l_2) = Z/|p|); prop:terminal-degree-two (im A = ker(4,2,3,2)); prop:terminal-all-degree (formal: H_* = (Z, Z/p, Z/p, Z/p, Z/p, 0, Z)
from stated algebraic outputs). These are [AC26] §2 (Lemmas 2.2–2.8), Lemma 7.13, Prop. 7.14, Thm 7.17, Lemma 7.19, Thm 7.22 and Appendix A.1.
Ledger: S6-ALG-P, S6-ALG-A2, S6-ALG-HOM (each with the nonclaim "does not identify the printed presentation/matrix with the geometric one").
CTX-FABLE-CERT in the ledger is unrelated to S6 ("degree-seven map has det DF=-2"; nonclaim: "No S6 lemma follows").

### 1.3 integral_leray.tex (36 KB, 967 lines; Round 7, 26 Aug)
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

### 1.4 topology_reduction.tex (46 KB, 1279 lines; Rounds 3, 12, 13: 25–27 Aug)
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

### 1.5 finite_filling_certificates.tex (32 KB, 760 lines; 6 Sep 2026)
"Exact product covers, normalization branches, and peripheral kernels of the finite fillings" (labels ffcert:*; equations FF1–FF46).
No \Verified marks in the file; ledger id FINITE-FILLING-FULL-CERTIFICATES-20260906 (VERIFIED), morphism M-FINITE-PRODUCT-NORMALIZATION-20260906.
Evidence: `..\evidence\period_lattice_continuation_20260906\finite_fillings\` (check_exact_finite_products.py, EXACT_RESULTS.json: degrees 3·3=9, 2·4=8,
moving rotation matrices [[-2,-3],[1,1]], [[1,2],[-1,-1]], all assertions passed).
Contents: ffcert:prop:integral-summands (fixed and moving lattices, annihilators, det -3, -2); ffcert:thm:product-covers (candidate A1-5);
ffcert:prop:quotient-charts; ffcert:thm:normalization, ffcert:thm:peripheral-kernel, ffcert:cor:covering-h1 (candidate A1-6); the gluing
interface (repeats thm:candidate-global-geometry); ffcert:thm:normal-trivialization (candidate A1-7).

### 1.6 algebraic_dimension.tex (11 KB, 299 lines; 26 Aug)
lem:torus-algebraic-reduction-audit; prop:very-general-torus-audit (NS(F_b)=Z eta outside a countable set, via P_E (3.1) and linear independence
of 1, tau, mu, beta, 6mu^2 - tau beta; G_eta = [[2 Im tau, 2 Im mu],[2 Im mu, (1/3) Im beta]], det = (2/3) Im tau · D < 0); lem:meromorphic-descent-audit;
thm:algebraic-dimension-audit (M(X)=f^*C(t), a(X)=1). "Provenance: the candidate's Lemmas 9.2–9.6 and Proposition 9.7, reconstructed with an
explicit Appell–Humbert matrix bridge, a proof that the smooth locus remains connected, and the omitted root estimate". Ledger S6-ALG-DIM.

### 1.7 cusp_toric_cover_completion.tex (16 KB, 442 lines; Round 31, 3 Sep)
One theorem, cusp-cover-extension-theorem (\Verified), and two remarks. Candidate A1-8. Ledger S6-CUSP-KUMMER-COMPLETION,
S6-CUSP-FINITE-COVER-R4-AUXILIARY; morphisms M-CUSP-KUMMER-DIRECT, M-CUSP-KUMMER-RELATIVE. Related (not mine): cusp_spectral_geometry.tex
(S6-CUSP-SPEC-COVERS: the cover over the punctured disc and the metric R^4 limits).

### 1.8 cusp_globalization_replacement.tex (28 KB, 738 lines; Round 29, 3 Sep)
One theorem, cusp-spec-globalization-obstruction (\Verified), parts (i)–(vi), with proof. It is an \input fragment that replaces a theorem inside
cusp_spectral_geometry.tex (it cites cusp-spec-native-quotient, cusp-spec-full-inverse-transpose, cusp-spec-radial-notation there and
cusp-cone-S12-route etc. in cusp_cone_sphere_routes.tex; those are reader C1's files). Candidates A1-1 and A1-9.
Ledger: S6-CUSP-FOUR-COPY-R4 (VERIFIED), S6-CUSP-LITERAL-COMPACT-EXTENSION (REFUTED = the nonextension is proved);
morphisms M-CUSP-GLOBAL-FOUR-CIRCLE, M-CUSP-GLOBAL-FOUR-CIRCLE-EXTENSION (REFUTED), M-CUSP-CONE-Q1.

### 1.9 local_repairs.tex (3 KB, 53 lines)
Seven items; candidate A1-18.

### 1.10 mathematical_summary.tex (145 KB) — parts read
l.1–56 (6 Sep: includes the statement X_c ≅ X_{c'} <=> c'-c in 2Z, see A1-X1), l.116–192 (canonical ring; period deformation; 5 Sep corrections;
exact period constants and cusp edge maps), l.395–540 (construction, cusp fibre, algebraic reduction, Leray route, van Kampen), l.1060–1128
(collapse, MV), l.1630–1948 (four-copy quotient, Kummer model, cone carriers q_2, q_{1,cusp}, q_1), l.3652–3782 (certificates, review checkpoint,
"current evidence boundary"). The summary adds nothing mathematical to the files above; it is the status view.
"Independent review checkpoint" (l.3671–3686): a "Reviewer B" reviewed the reconstruction up to a cutoff and "found no load-bearing defect in the
non-collapse nearby-cycle/Leray and based van Kampen route".

### 1.11 Ledgers
claim_ledger.txt: JSON lines; my ids extracted to `work\scratch\A1\ledger_extract.txt`. morphism_ledger.txt: 124 lines, entries listed in 1.3–1.8.
uncertainties.txt: U-CUSP-ACTION, U-SPECIALIZATION-INDEX, U-COLLAPSE-COMPARISON, U-MERIDIAN-SIGN all VERIFIED; U-EXTERNAL-ADJUDICATION OPEN.

### 1.12 Comparison with [E26]: what each side has
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

### 1.13 Quotient maps of the kind of [E26] Remark 8.3 in my files
Only cusp_globalization_replacement.tex computes with them: chi_gamma = (f, theta_gamma): J -> B° x R/Z is exactly the quotient by the rank-3
subtorus family ker(gamma) = ker(phi); part (iv) gives the Seifert solid tori C_j at p_1, p_2; part (v) proves that the literal map does not extend
continuously over W. The file does not form the closed Seifert manifold Q = S^3 of Engel; the neighbouring cusp_cone_sphere_routes.tex cones the
boundary torus instead (map q_1: X -> C = M ∪ Cone(∂M), M = (P x S^1) ∪ C_1 ∪ C_2; mathematical_summary.tex l.1873–1924). [AC26] itself has the
Seifert reading only as a heuristic on its first summary page (Orlik's formula |a_1a_2e_0 + a_2b_1 + a_1b_2|, "glue so that the coinvariant circle
of the fibres traces out the (3,4) Seifert fibration of the three-sphere"). Details in A1-1.

---------------------------------------------------------------------------------------------------------------------------

## 2. Candidates

### A1-1
- **Title**: The invariant-circle (rank-3 subtorus) quotient: rigorous Seifert structure over B\{p_0}, and proof that the literal quotient map does
  not extend continuously over the cusp fibre W. **Type**: new result / correction of the literature ([E26] Remark 8.3).
- **Where**: cusp_globalization_replacement.tex, Theorem cusp-spec-globalization-obstruction parts (i), (iv), (v); statement l.22–59, 144–230;
  proofs l.293–349 (group law, invariant character), l.443–549 (finite fillings), l.551–657 (cusp). Round 29, 3 Sep 2026 (ten days before [E26]).
- **Statement**: (i) Hom(Lambda,Z)^Delta = Z eps_gamma, eps_gamma(a gamma^ + b u^ + c w^ + d delta^) = a; L_Lambda = ker eps_gamma = <u^,w^,delta^> is the
  smallest monodromy-invariant lattice containing K_Lambda = <w^,delta^>. chi_gamma([z, Pi(z)x]) = ([z], eps_gamma(x) mod Z) is a global real-analytic
  fibrewise group epimorphism J -> B° x (R/Z) whose kernel is the T^3-family H = (h_z° x (L_Lambda ⊗ R)/L_Lambda)/Delta.
  (iv) At p_j, with kappa_j = eps_gamma(v_j) = ±1: eps_gamma(A_j x + v_j/m_j) = eps_gamma(x) + kappa_j/m_j; the map descends to N_j -> C_j,
  C_j = (Delta_j x R/Z)/((s,theta) ~ (e^{-2 pi i/m_j}s, theta + kappa_j/m_j)), a smooth solid torus (invariant coordinates w = s u^{r_j}, U = u^{m_j},
  r_j kappa_j ≡ 1 mod m_j, t_j = w^{m_j} U^{-r_j}) whose central circle has multiplicity m_j, and N_j -> C_j is a smooth proper T^3-bundle. The
  logarithmic gluing h_j induces h_j^{S^1}(z,theta) = (z, theta + beta_j(z)) with beta_j(g_j z) = beta_j(z) - kappa_j/m_j, and
  chi_gamma ∘ h_j = h_j^{S^1} ∘ chi-bar_j. No homomorphism to Z restricting to n eps_gamma exists on pi_1(X) for n ≠ 0 (3a = n, 4b = -n, a+b = 0).
  (v) On the radial ray, the point x_T(a) = exp(2 pi i Z_T a), a in R^2, has logarithmic position y_T(a) = B_0 a + Im C(t_c) a / T and
  chi_gamma = a_1 mod Z. If B_0 a lies in the open triangle conv(0,e_1,e_2), then x_T(a) converges to the torus-fixed point of that chart, i.e. to
  one triple point of W. For a = (-1/4,1/4) and a' = (-1/2,1/4) the limits coincide and the character values are 3/4 and 1/2. Hence chi_gamma has no
  continuous extension to N_0. Likewise the fibrewise translation by u^/2 (in H) does not extend: it sends two paths with the same limit to paths
  converging to the two different triple points. The class of eps_gamma in H^1 does extend over N_0 (pi_1(N_0) = Lambda/K_Lambda).
- **Support**: written proof, about 250 lines, elementary (the formulas of candidate_geometry.tex and the toric chart z_0 = t/(x_1x_2), z_1 = x_1,
  z_2 = x_2). Ledger S6-CUSP-FOUR-COPY-R4 VERIFIED and S6-CUSP-LITERAL-COMPACT-EXTENSION REFUTED (i.e. nonextension proved). No script.
- **What it adds**: over [AC26]: the Seifert picture is there only as a heuristic on summary page 1 (l.111); nothing in the body. Over [E26]:
  Remark 8.3 asserts that at infinity "this quotient map of the first paragraph extends continuously to the composition of the moment mapping with a
  further quotient to a circle", and concludes "the quotient map is a map S^6 -> S^3". Part (v) shows that the literal fibrewise quotient does not
  extend continuously (in the limit theta_gamma = -y_2 depends on the direction of approach to a triple point, is constant 0 on the open orbit of W,
  and is undetermined along two of the three double curves). What exists is a continuous map on N_0 in the same homotopy class (Clemens collapse
  followed by the moment map), which agrees with the quotient only after a homotopy near W; and the T^3-family action itself does not extend.
  Parts (i), (iv) give the proof of Engel's description at 0 and 1, with the explicit rotation data theta -> theta + kappa_j/m_j = theta + 1/3,
  theta - 1/4 (in the convention of [AC26] p.1: Seifert invariants (3,-l_1), (4,-l_2)) and the T^3-bundle statement.
  Literature: searched the web for follow-ups to [E26] on the Seifert quotient S^6 -> S^3 (two queries, 12 Nov 2026): nothing beyond [AC26]/[E26].
- **First assessment**: solid. I re-derived the key formula: Im Z_T = T B_0 + Im C, so log|x|/log|t_c| = B_0 a + Im C a/T, and for y in the open
  triangle all three chart coordinates have absolute values |t|^{1-y_1-y_2}, |t|^{y_1}, |t|^{y_2} -> 0. The nonextension is real and robust. The
  workbench does not state the positive replacement (a continuous map X -> S^3) nor Q ≅ S^3; that part is in [AC26] p.1 and [E26] only as a claim.
  Engel's remark is informal, so "correction" means: the sentence is false as written, and the true statement needs a collapse map.
- **A full check must establish**: (1) the invariance and primitivity statements in (i); (2) smoothness of C_j and the T^3-bundle claim; (3) the
  overlap identity chi_gamma ∘ h_j = h_j^{S^1} ∘ chi-bar_j with signs; (4) the two-path argument and convergence in the quotient N_0 (not only in Y);
  (5) the precise corrected form of [E26] Rem. 8.3: a continuous map X -> Q, Q = M ∪ (D^2 x S^1) ≅ S^3 iff |p| = 1, equal to the quotient map
  outside a neighbourhood of W; whether it can be chosen T_f-invariant; and its class in pi_6(S^3) = Z/12 (reader C1's files compute related but
  different maps: ledger S6-CUSP-ONE-COPY-FRAMED-NULL says an "angle-forgetting cusp map g: X -> S^3" is null-homotopic).
- **Deserves a full check**: yes — it corrects a statement in the only published companion paper and the proof is short. **Interest**: 4.

### A1-2
- **Title**: Exact admissible set of the period constant: Im c_0 < -M. **Type**: refinement of [AC26].
- **Where**: candidate_geometry.tex, prop:period-exact-admissible-constants, l.563–596; 5 Sep 2026. Summary l.164–177.
- **Statement**: with tau, mu, beta^part the cusp-regular solutions, D_part = Im beta^part - 6(Im mu)^2/Im tau descends to B\{p_0}, tends to -infinity
  at p_0 and attains a finite maximum M. beta = beta^part + c_0 makes Pi(z) a real isomorphism Lambda ⊗ R -> C^2 for every z exactly for
  {c_0 : Im c_0 < -M}; for Im c_0 >= -M the determinant Im tau · (D_part + Im c_0) vanishes somewhere.
- **Support**: 15-line proof (continuity, attained maximum, intermediate value theorem on a path to the cusp). Ledger VERIFIED; a post-integration
  review in evidence\s6_global_smooth_reaudit_20260905\INTEGRATED_GEOMETRY_REVIEW.md.
- **What it adds**: [AC26] Prop. 3.15 (l.1036) gives the sufficient condition Im c_0 < -max(M,0) and Remark 6.4 leaves the dependence on c_0 open.
  [E26] Prop. 2.4 gives "there exists c such that |u| < c works". The workbench statement is the exact domain of the period construction:
  in Engel's parameter the punctured disc |u| < e^{-2 pi M} (suitable normalization). Not searched in the literature (specific to this family).
- **First assessment**: correct and easy. M depends on the normalization of beta^part (sections of the torsor differ by constants); the set is
  intrinsic. The number M is not computed anywhere. Whether Engel's quotient M^x/Z is still a manifold with torus fibres for |u| beyond this radius
  is the same question (the lattice degenerates at a point where D = 0), so the radius is sharp for his construction too — that should be said in a check.
- **A full check must establish**: continuity of D at the elliptic points; the limit at the cusp; that D = 0 at one point really destroys the
  family (yes: Pi(z)Lambda is not a lattice); a numerical value of M for the normalization b(0) = 0 and the location of the maximum (open computation).
- **Deserves a full check**: maybe — the proof needs no check, the value of M and the comparison with Engel's disc would be the content. **Interest**: 3.

### A1-3
- **Title**: The "cusp-free" solution beta + i·t∘pi satisfies all affine laws but admits no admissible constant. **Type**: new (small) counterexample / refinement of [AC26].
- **Where**: candidate_geometry.tex, remark after prop:period-exact-admissible-constants, l.598–617; 5 Sep. Ledger S6-PERIOD-CUSP-FREE-SHIFT-COUNTEREXAMPLE.
- **Statement**: beta~ = beta + i t∘pi is holomorphic on h_z and obeys the laws (beta1); D~ = D + Re t; along t = R -> +infinity,
  D(R) = -log(1728R)/(2 pi) + Im b(0) + o(1), so D~(R) -> +infinity; no constant shift makes D~ < 0 everywhere. beta~ + tau = b + i t has a pole at the cusp.
- **Support**: 10 lines. **What it adds**: shows that condition (beta2) of [AC26] Def. 3.1 (cusp regularity) is needed for (beta3), not only for the
  filling. Not in [AC26] or [E26]. Not searched.
- **First assessment**: correct (t∘pi is Delta-invariant; q ≈ 1/(1728 t)).
- **A full check must establish**: the asymptotic of Im tau along the ray; nothing else.
- **Deserves a full check**: no — a remark. **Interest**: 2.

### A1-4
- **Title**: Exact gluing data of the cusp fibre W: the three opposite-side identifications of the hexagon of dP_6 are multiplications by
  e^{-2 pi i mu_0}, e^{12 pi i mu_0}, e^{-2 pi i (7 mu_0 + b_0)}. **Type**: refinement of [AC26] / computation.
- **Where**: candidate_geometry.tex l.1029–1064 (inside the proof of thm:candidate-cusp-geometry), eq:cusp-exact-opposite-edge; 5 Sep.
  Ledger S6-CUSP-EXACT-EDGE-IDENTIFICATIONS; summary l.178–189.
- **Statement**: for v in {±e_1, ±e_2, ±(e_1-e_2)}, C_v = E_0 ∩ E_v, iota_v = Psi_{B_0 v}|_{C_v}: C_v -> C_{-v}. For a primitive row a with a·v = 0 and
  the character w = chi^{(a,0)} on both curves, iota_v^* w_{-v} = exp(2 pi i a C(0) B_0 v) w_v. With mu_0 = mu(p_0), b_0 = (beta+tau)(p_0):
  (v,a) = (e_1,(0,1)): e^{-2 pi i mu_0}; (e_2,(1,0)): e^{12 pi i mu_0}; (e_1-e_2,(1,1)): e^{-2 pi i (7 mu_0 + b_0)} (h(0) cancels).
- **Support**: direct character computation; my sympy check reproduces the three exponents -mu_0, 6 mu_0, -7 mu_0 - b_0.
- **What it adds**: [AC26] Prop. 4.6(ii) (l.1457) only says C_v is identified with C_{-v} by Psi_lambda; [E26] Prop. 2.8 only names the glued dP_6.
  The multipliers are invariant under the torus of dP_6, so they are moduli of W: two are independent of c_0, the third moves with c_0 (b_0 -> b_0 + c_0)
  and is invariant under c_0 -> c_0 + 1. Not searched.
- **First assessment**: correct. An addition the workbench does not make (my own unverified sanity computation, with Engel's model): the generator
  of the Mordell–Weil group is P = (0, sqrt2 t^2(t-1)) (it lies on the surface, is integral and meets the non-identity components at t=0,1); at
  t = infinity the fibre is Y^2 = (X-1)^2(X+2) and P = (0, sqrt2) has multiplicative coordinate (sqrt2+sqrt3)/(sqrt2-sqrt3) = -(5+2 sqrt6). If mu is
  the Abel–Jacobi coordinate of P (consistent with mu(z_1) = (2-rho)/3 a 3-torsion point, mu(z_2) = (1-i)/2 a 2-torsion point, and [E26] Prop. 3.1),
  then e^{2 pi i mu_0} = -(5+2 sqrt6)^{±1}, i.e. Re mu_0 = 1/2, |Im mu_0| = log(5+2 sqrt6)/(2 pi) ≈ 0.365, and two of the three gluing multipliers
  are explicit units of Z[sqrt6]: -(5 ∓ 2 sqrt6) and (5 ± 2 sqrt6)^6.
- **A full check must establish**: the sign and character conventions; that the triple (m_1,m_2,m_3) up to the dihedral symmetry of the hexagon
  classifies such glued surfaces; the value of mu_0 (via Engel's surface or numerically from the torsor); which double curve is the fixed curve of
  Aut^0 = C^* (the one for v = ±e_2, with multiplier e^{12 pi i mu_0}).
- **Deserves a full check**: maybe — small, but it makes W explicit and connects the period picture to Engel's. **Interest**: 3.

### A1-5
- **Title**: Explicit elliptic-product covers of the central tori and of the bielliptic fibres: S_1 = (E_1 x F_1)/(C_3 x C_3), S_2 = (E_2 x F_2)/(C_2 x C_4),
  degrees 9 and 8, with moduli kappa_1 = beta(z_1) + 2 mu(z_1), kappa_2 = beta(z_2) + 3 mu(z_2). **Type**: refinement of [AC26] (sharper, explicit).
- **Where**: finite_filling_certificates.tex, FF4–FF22, ffcert:prop:integral-summands (l.87–136), ffcert:thm:product-covers (l.175–304); 6 Sep 2026.
- **Statement**: Lambda^{A_1} = Z eps ⊕ Z delta^, (A_1-I)Lambda = Z e_1 ⊕ Z f_1 with e_1 = (0,1,-2,0), f_1 = (0,0,-3,1), index 3 in Lambda; Lambda^{A_2} =
  Z eps' ⊕ Z delta^, (A_2-I)Lambda = Z e_2 ⊕ Z f_2, e_2 = (0,1,-1,0), f_2 = (0,0,-2,1), index 2. Pi(z_1)eps = (0,kappa_1), Pi(z_j)delta^ = (0,1),
  Pi(z_1)e_1 = (rho-2, -(rho-2)/3), Pi(z_1)f_1 = (-3,1), Pi(z_2)e_2 = (i-1, -(i-1)/2), Pi(z_2)f_2 = (-2,1); Im kappa_j = D(z_j) < 0.
  E_j = C/(Z + kappa_j Z), F_1 = C/(Z(rho-2) + 3Z), F_2 = C/(Z(i-1) + 2Z). L_1(xi,eta) = (eta, xi - eta/3), L_2(xi,eta) = (eta, xi - eta/2) induce
  isogenies E_j x F_j -> A_0^{(j)} with kernels <k_1 = (2/3, rho)> of order 3 and <k_2 = (1/2, i)> of order 2. Lifts of the affine generators:
  g_1^prod(xi,eta) = (xi + kappa_1/3, (rho-1) eta), g_2^prod(xi,eta) = (xi - kappa_2/4, -i eta). <k_1,g_1^prod> ≅ C_3 x C_3 and <k_2,g_2^prod> ≅ C_2 x C_4
  act freely, and S_j is the quotient.
- **Support**: written proof (130 lines) + exact checker (evidence\period_lattice_continuation_20260906\finite_fillings). My check: the two
  determinants are -3, -2 and the first coordinates of Pi(z_j)eps, Pi(z_j)eps' vanish.
- **What it adds**: [AC26] Thm 5.4(iii), Lemma 5.7 (l.1691): "isogenous to a product", type read off the Bagnera–de Franchis list from ord(K) and
  torsion-free H_1. [E26] Cor. 3.2, 3.9: (E~ x E_0)/mu_3, (E~ x E_1)/mu_2, without moduli. Here: explicit curves and groups; F_1, F_2 are Engel's
  E~_triangle, E~_square (index 3 in Z[rho], index 2 in Z[i]); E_1, E_2 are his E_0, E_1 with modulus kappa_j, which moves with c_0 (kappa_j -> kappa_j + c_0).
  Consequence not drawn in this file: Alb(S_1) ≅ C/(Z + kappa_1 Z) and Alb(S_2) ≅ C/(Z·(1/2) + Z·kappa_2/4), so the isomorphism class of X_{c_0}
  determines kappa_1 + c_0 and (kappa_2 + c_0)/2 modulo SL_2(Z); in particular c_0 -> c_0 + 1 changes Alb(S_2) in general. This is the
  mechanism behind the 2Z-classification of A1-X1 and makes [E26] Remark 8.1 ("E_0 and E_1 vary") quantitative. Not searched.
- **First assessment**: looks right; all arithmetic is exact and I spot-checked several identities. Risk: orientation conventions (Im kappa_j < 0 is kept on purpose).
- **A full check must establish**: FF7–FF22; that the kernel is exactly Lambda/(Lambda^{A_j} + (A_j-I)Lambda); freeness of the joint groups; the
  identification with Engel's Cor. 3.2; the Albanese statement above.
- **Deserves a full check**: maybe — routine but it carries the explicit invariants used elsewhere. **Interest**: 3.

### A1-6
- **Title**: Finite fillings: the varying torus family is the normalization of the base change; complete deck-group presentation; the attachment
  kernel is exactly the central Z generated by G~_j^{m_j} t_{-v_j}; exact H^1 covering image. **Type**: refinement of [AC26] (sharper statements) / new proof.
- **Where**: finite_filling_certificates.tex: ffcert:prop:quotient-charts (l.339–382), ffcert:thm:normalization (l.395–455),
  ffcert:thm:peripheral-kernel (l.459–548), overlap section (l.550–605), ffcert:cor:covering-h1 (l.607–640); 6 Sep.
- **Statement**: nu_j: J'_j -> P_j = N_j x_{D_j} Delta^base (t_j = u^{m_j}), y -> (q_j(y), s_j(y)), is the normalization; local equation
  s^{m_j} - u^{m_j} = prod_a (s - e^{2 pi i a/m_j}u), m_j smooth branches, nu_j(G_j y) = (q_j(y), zeta_j s_j(y)). Universal cover Delta_j x C^2 -> N_j with
  deck group Gamma_j = <Lambda, G^_j | Lambda abelian, G^_j t_lambda G^_j^{-1} = t_{A_j lambda}, G^_j^{m_j} = t_{v_j}> (also pi_1(S_j)); pi_1(N_j \ S_j) =
  Lambda ⋊_{A_j} Z; ker(pi_1(N_j\S_j) -> pi_1(N_j)) = <G~_j^{m_j} t_{-v_j}> ≅ Z, central. pi_j^* H^1(S_j;Z) = Z(m_j gamma) ⊕ Z psi_j.
  Real-marking overlap: a_j(z) = Re alpha · v_j + Im alpha · J_z v_j, J_{g_j z}A_j = A_j J_z, a_j(g_j z) = A_j a_j(z) - v_j/m_j.
- **Support**: written proofs (normal forms t_lambda G^k; local ring argument for the normalization). Ledger VERIFIED.
- **What it adds**: [AC26] Lemma 7.4 / Lemma 7.16 state the relation rho_j^{m_j} = t_{v_j} imposed by N_j; here the kernel is identified exactly and
  shown central; the normalization statement is the standard picture of a logarithmic transform ([E26] Construction 3.5 runs it in the other
  direction) but is not written in [AC26]. The real-marking formula corrects a shortcut (multiplying a real vector by the complex scalar alpha),
  summary l.146–162 "5 September: exact corrections to two S6 proof steps". Not searched; standard material.
- **First assessment**: correct as far as read; the kernel generator is the meridian of S_j, so the statement is the expected one.
- **A full check must establish**: uniqueness of normal forms; the centrality; the local normalization argument.
- **Deserves a full check**: no — standard, low risk. **Interest**: 2.

### A1-7
- **Title**: The normal bundle of S_j has holomorphic order exactly m_j but an explicit smooth trivialization H_j(x) = exp(-2 pi i eps_j gamma(x)). **Type**: refinement of [AC26].
- **Where**: finite_filling_certificates.tex, ffcert:thm:normal-trivialization, l.678–760; 6 Sep.
- **Statement**: N_{S_j/N_j} = (A_0^{(j)} x C)/((x,n) ~ (A_j x + v_j/m_j, zeta_j n)); H_j(A_j x + v_j/m_j) = zeta_j H_j(x) with eps_j = gamma(v_j) = ±1;
  Theta_j([x,n]) = ([x], n/H_j(x)) is a smooth trivialization; so c_1 = 0 in H^2(S_j;Z) while the holomorphic order is m_j.
- **Support**: 80 lines, direct. **What it adds**: [AC26] Thm 5.4(iii) has the order m_j; c_1 = 0 follows there from torsion-freeness of H^2(S_j);
  the explicit section is new and uses only gamma. For general admissible v one needs eps with eps·gamma(v) ≡ 1 mod m_j (not stated). Not searched.
- **First assessment**: correct (one-line verification). **A full check must establish**: the character sign convention.
- **Deserves a full check**: no. **Interest**: 2.

### A1-8
- **Title**: Completed Kummer cover of the cusp: a finite flat degree-N^3 map N_0^{<N>} -> N_0 and a degree-N^2 quasi-étale, non-flat map to the
  normal base change N_0[N], with exact non-flat locus. **Type**: new result (local; standard toric techniques).
- **Where**: cusp_toric_cover_completion.tex, cusp-cover-extension-theorem (l.57–406), remarks l.408–442; Round 31, 3 Sep 2026. Ledger S6-CUSP-KUMMER-COMPLETION.
- **Statement**: for N >= 1 put C_N(v) = C(v^N)/N and Psi^{(N)}_lambda(xi,v) = (exp(2 pi i C_N(v) lambda) v^{B_0 lambda} xi, v) on a copy Y^{(N)} of the same toric
  threefold. (1) The action is free and properly discontinuous; N_0^{<N>} = Y^{(N)}/Lambda-bar -> Delta_v is proper from a smooth threefold, central
  fibre W_N reduced, irreducible, nonnormal, normalization dP_6. (2) P_N(xi_1,xi_2,v) = (xi_1^N,xi_2^N,v^N) is finite flat of degree N^3, equivariant, and
  descends to kappa_N: N_0^{<N>} -> N_0 with f_0∘kappa_N = (v -> v^N)∘f_N. (3) kappa_N is étale over v ≠ 0, kappa_N^*W = N W_N, Ram = (N-1)W_N.
  (4) N_0[N] = N_0 x_{Delta_t} Delta_v is normal (local ring C{z,v}/(z_0z_1z_2 - v^N) = C{w_0,w_1,w_2}^{G_N}, G_N = {eps in mu_N^3 : prod = 1});
  Q_N: N_0^{<N>} -> N_0[N] has degree N^2, is étale in codimension one, not flat exactly over the double and triple strata (fibre lengths 2N-1 > N
  and 3N^2-3N+1 > N^2). (5) On normalizations of the central fibres it is [N]: dP_6 -> dP_6. (6) Over v ≠ 0, Q_N is the cover for the sublattice
  Z<gamma^,u^,N w^,N delta^>, deck group (Z/N)^2, and S_N^{-1}M_0^N S_N = M_0, S_N = diag(1,1,N,N). Remark: without the factor 1/N in C_N the power map
  does not descend; the sublattice is not preserved by A_1, so nothing global over B follows.
- **Support**: written proof (250 lines). My check: the fibre-length counts N^3-(N-1)^3 and 2N-1 for N = 2,3,4; stabilizer description of G_N.
- **What it adds**: nothing like it in [AC26] or [E26]. In the literature the general statements are standard (a base change of a Mumford/Kulikov
  degeneration; z_0z_1z_2 = v^N is a toric quotient singularity; fibrewise it is the isogeny C^2/(N Z^2 + Z Z^2) -> C^2/(Z^2 + Z Z^2)); what is specific
  is the explicit model for this family, including the corrected twist C(v^N)/N. Not searched beyond that judgement.
- **First assessment**: looks correct; low risk. Its purpose in the workbench was auxiliary (pointed R^4 limits, "S12/S24 carriers"); as mathematics it
  is a clean statement about the cusp that could serve a study of finite covers or of base changes of the family at infinity.
- **A full check must establish**: proper discontinuity of the modified action after shrinking; flatness after the quotient; normality of N_0[N] on
  all strata; the claim "not a normalization" (N_0[N] is already normal, Q_N is a different finite cover).
- **Deserves a full check**: maybe — new and self-contained, modest interest. **Interest**: 3.

### A1-9
- **Title**: Four-copy T^4 quotient with pointed R^4 limit, minimality of four copies, no finite base cover preserves K_Lambda, products/smash/joins
  bookkeeping. **Type**: new result (metric/topological side statements); partly expository.
- **Where**: cusp_globalization_replacement.tex parts (ii), (iii), (vi); l.61–142, 232–290; proofs l.351–441, 659–737; 3 Sep.
- **Statement**: (ii) for the Euclidean fibre metric on the radial cusp the quotient circle has circumference l_T = D_T/sqrt(L_T^2 + m_T^2) =
  T + H - B + O(1/T). (iii) chi_gamma^{[4]}: J^{[4]} -> B° x (R/Z)^4 has kernel fibres T^12 and radial quotient (R/l_T Z)^4 -> R^4 (pointed, exactly
  Euclidean on balls of radius R once l_T > 4R); a primitive invariant kernel N in Lambda^{⊕r} with diverging quotient systole contains L_Lambda^{⊕r}, so
  the quotient rank is <= r; H_* = A_2A_1 = I + N_*, N_*^2 = 0, H_*^n w^ = w^ + n(u^ - delta^), so no finite-index subgroup of pi_1(B°) preserves K_Lambda.
  (iv, second half) the simultaneous-root model N~_j^{[4]} is the normalization of the fourfold fibre product of N_j, of degree m_j^3 = 27, 64 on the
  reduced central fibre. (vi) X^2, X^4 are not spheres; X∧X ≅ S^12, X^{∧4} ≅ S^24 but the quotient maps do not factor; Borel–Serre excludes almost
  complex structures on S^12, S^24; a target-smash map F_T^4 -> S^4 does not extend to X^4 since H^4(X^4) = 0.
- **Support**: written proofs; my check: A_2A_1 = [[1,0,0,0],[6,1,1,0],[0,0,1,0],[-5,0,-1,1]], nilpotent part squares to zero.
- **What it adds**: not in [AC26]/[E26]. The monodromy statement (L_Lambda is the invariant hull of the vanishing lattice; unipotent A_2A_1) is a clean
  fact about the local system (Engel's filtration (3.1)–(3.2)). The metric statements depend on a chosen flat fibre metric (the file says so) and
  on a programme (R^4 limits, sphere "carriers") whose mathematical interest is unclear to me. Not searched.
- **First assessment**: correct as far as read; mostly elementary. **A full check must establish**: the expansions of D_T, L_T, m_T (they live in
  cusp_spectral_geometry.tex); the normalization claim for the fourfold fibre product.
- **Deserves a full check**: no — low mathematical weight; keep the monodromy facts. **Interest**: 2.

### A1-10
- **Title**: The collapse pullback equals nearby-cycle specialization: sp^q = i_F^* r^* = c^* integrally, all q. **Type**: new proof of a statement asserted in [AC26].
- **Where**: topology_reduction.tex, thm:collapse-equals-specialization, l.523–598; Round 12, 27 Aug. Ledger S6-TOP-C3.
- **Statement**: with the radial marking of the punctured cusp family, for 0 <= q <= 4, sp^q = i_F^* r^* = c^*: H^q(W;Z) -> H^q(F;Z); hence im c^* =
  (wedge^q V)^{T_0} saturated, and the degree-3 orientation of the cellular computation is that of intrinsic specialization.
- **Support**: one-page proof: closed tubes N_rho are cofinal; i_{W,rho}^* is an isomorphism with inverse j_rho^* r^*; restrictions of one class to
  fibres along a ray form a flat section; independence of the lift by (C.24).
- **What it adds**: [AC26] defines sp^q := c^* in Prop. 7.12, uses the sheaf-theoretic sp in App. B, and says the identification "continues to rest
  on §7.2" (Remark B.4, l.5595), with one sentence in Remark B.2. [E26] does not have a collapse map. Not searched (standard fact about retractions).
- **First assessment**: correct; a gap-filling detail, not a new result.
- **A full check must establish**: the direct-limit description of sp for the analytic nearby cycle functor (Dimca 4.2.11).
- **Deserves a full check**: no. **Interest**: 2.

### A1-11
- **Title**: Integral collapse sequence 0 -> im(wedge^q M_0 - I) -> wedge^q Lambda -> H_q(W;Z) -> 0 with explicit matrices. **Type**: re-proof of [AC26] Prop. 7.12 with explicit data.
- **Where**: topology_reduction.tex, prop:verified-collapse-homology, l.388–519, (C.16)–(C.25); 27 Aug. Ledger S6-TOP-C2.
- **Statement**: c_* surjective in all degrees with kernel im(wedge^q M_0 - I); n_1 = w^, n_2 = delta^ - w^, n_3 = -delta^, nu_k(v) = det(n_k,v);
  c_*(gamma^u^) = [T_B], c_*(w^delta^) = 0, c_*(beta ⊗ v) = sum_k nu_k(B_0 beta) nu_k(v) [C-bar_k]; matrix (C.20)
  [[1,0,0,0,0,0],[0,0,-1,0,0,0],[0,-1,-1,1,1,0],[0,0,0,1,0,0]]; kernels (C.25): <w^,delta^>, <w^delta^, gamma^w^ + u^delta^>, <gamma^w^delta^, u^w^delta^>.
- **Support**: cellular proof; H_*(W) via (W,D) and Lefschetz duality. My check: (C.20)·(wedge^2 M_0 - I) = 0, rank of the image 2, (C.20) has Smith form (1,1,1,1).
- **What it adds**: statement identical to [AC26] Prop. 7.12 (l.2563) and 7.11; the matrix and the kernel table are explicit. [E26]: the degree-1
  case only (im N = ker N). Not searched.
- **First assessment**: consistent. **A full check must establish**: orientation conventions in (C.19); nothing structural.
- **Deserves a full check**: no — duplicate of [AC26] with explicit matrices. **Interest**: 2.

### A1-12
- **Title**: Abstract "equivariant topological spine" lemma and the equivariant strong deformation retraction of the cusp. **Type**: new proof or restatement of a known result ([AC26] §7.2).
- **Where**: topology_reduction.tex, prop:topological-spine l.41–79; lemmas l.106–371; Rounds 3 and 12. Ledger S6-TOP-C1-SPINE, S6-TOP-C1.
- **Statement**: as in 1.4. The retraction Y_{<=eta} -> Y_0 is Gamma- and T_f-equivariant and descends to r: N'_0 -> W whose restriction to a fibre is the
  honeycomb collapse.
- **Support**: Whitehead + homotopy extension + unique path lifting; then the candidate-specific hypotheses.
- **What it adds**: nothing over [AC26] Lemmas 7.5–7.10 except the abstract packaging (the research log, Round 3, says "Proved independently the
  formal topological spine of Lemmas 7.8–7.9"). [E26] does not need it (Leray route only). Not searched.
- **First assessment**: same proof as the original; fine. **A full check must establish**: nothing new.
- **Deserves a full check**: no. **Interest**: 1.

### A1-13
- **Title**: Mayer–Vietoris/Leray comparison as commuting squares; explicit finite-band matrices; one-shot collar matrix with det = 1 - 12 l_0. **Type**: new proof / computation.
- **Where**: topology_reduction.tex, prop:actual-finite-band-maps (l.640–781), prop:cusp-mv-blocks (l.785–918), remark (l.920–961),
  thm:mv-leray-comparison (l.965–1111); Round 13, 27 Aug. Ledger S6-TOP-MV1, S6-TOP-L1.
- **Statement**: [alpha_1] = [[3,0,0,0],[0,2,1,3],[4,0,0,0],[0,-1,-1,-2]] (Smith (1,1,1,0), kernel Z(-u^-w^+delta^)); [alpha_2] (MV.6) with left kernel
  Phi = (4,2,3,2) and 2q = 4 pi_1^*a_1 + 2 pi_1^*b_1 = 3 pi_2^*a_2 + 2 pi_2^*b_2; [alpha_4] = (3,-4)^t; D_1 = [[1,0,0],[0,1,0],[-12,0,-p]];
  j_* xi_delta = -p e; 9x9 matrix Delta_1 (MV.17), det = 1 - 12 l_0 = -p for (l_1,l_2) = (1,-1); squares (L.5), (L.7): d_2(12 gamma) = -p omega_MV,
  d_2(2q) = -p omega_MV[delta], d_2(2 gamma uw) = -p omega_MV[gamma delta].
- **Support**: written; my sympy check confirms Smith forms, Phi·[alpha_2] = 0, det Delta_1 = 1 - 12 l_0.
- **What it adds**: [AC26] computes both routes and observes agreement (Prop. 7.27 "in agreement with Theorems 7.17 and 7.22"); the commuting
  squares and the one-shot matrix are additions. [E26]: Leray only. Not searched.
- **First assessment**: consistent with [AC26] Lemmas 7.18–7.19 (same K_1, K_2, nu_0, Phi). **A full check must establish**: bases and signs in (MV.5)–(MV.13).
- **Deserves a full check**: no — a cross-check of known numbers. **Interest**: 2.

### A1-14
- **Title**: Nearby-cycle/Leray proof of H^1 = H^2 = H^3 = 0, with d_2 identified through the canonical truncation triangle. **Type**: new proof or restatement of a known result ([AC26] §7.7 + App. B; [E26] §7).
- **Where**: integral_leray.tex, all; Round 7, 26 Aug. Ledger S6-NEARBY, S6-TOP-LERAY-D2, S6-TOP-END.
- **Statement**: as in 1.3.
- **Support**: full proofs; the rank count (alpha = 0, gamma' = 0, beta + delta' + eps = 1) checks against Betti numbers (1,4,6,4,1) (I redid it).
- **What it adds**: over [AC26]: (a) the identification of the Cech discrepancy with Leray d_2 (truncation triangle, Stacks tags) where [AC26] says
  "is the obstruction to lifting"; (b) the sign of the higher transgressions from r = s and s = 2 - r directly, where [AC26] argues |p'| = |p''| and
  excludes p'' = -p' by p ≠ 0. Over [E26]: a complete proof of the sentence in Lemma 7.4 that specialization at infinity is an isomorphism onto the
  invariants for k = 2, 3 (Engel gives no details), and the parabolic-cohomology formula (5.17) for H^1(B, j_*L). Not searched.
- **First assessment**: sound as far as read; same skeleton as the original.
- **A full check must establish**: the degree-3 Gysin argument (the only non-formal step); Dimca's integral coefficients hypotheses.
- **Deserves a full check**: no — the theorem is established twice elsewhere; useful as the written-out reference for Engel's Lemma 7.4. **Interest**: 2.

### A1-15
- **Title**: Period family existence with all normalizations (orientation lemma, cusp image by a trace argument, two torsor problems). **Type**: new proof or restatement of a known result ([AC26] Thm 3.4).
- **Where**: candidate_geometry.tex l.32–561; 24–26 Aug, refined 5 Sep.
- **Statement**: as in 1.1.
- **Support**: full proof. **What it adds**: over [AC26]: the argument that the mixed orientation choices are not parabolic (cyclically reduced
  words y^3x, yx^2 vs y^3x^2); the determination phi(g_0)(w) = w - 1 from k(p^2 - pr + r^2) = -1; explicit statement that g_2'(z_2) = -i is not
  determined by the quadratic ramification. Over [E26]: Engel gets the same functions from the elliptic surface with no analysis. Not searched.
- **First assessment**: correct as far as read (I re-derived the trace identity). **A full check must establish**: the cusp-regular stalk of L (order -1
  at the cusp, orders 2 and 1 of Theta at z_1, z_2 against stabilizer orders 3 and 4), which gives L ≅ O(-1).
- **Deserves a full check**: no. **Interest**: 2.

### A1-16
- **Title**: Toric cusp filling: Hausdorffness of the countable-fan toric variety, closed-polydisc cover, properness, trivial canonical bundle. **Type**: new proof or restatement of a known result ([AC26] §4).
- **Where**: candidate_geometry.tex l.652–1226. **Statement**: as in 1.1.
- **Support**: full proofs. **What it adds**: details that [AC26] takes from toric generalities (separatedness for an infinite fan by the semigroup
  identity S_kappa + S_kappa' = S_upsilon; explicit table of the six closed bidiscs covering E_0; restricted charts U_sigma(S,eps)). [E26] cites [Mum72], [EGFS25].
- **First assessment**: careful and plausible. **A full check must establish**: nothing beyond [AC26] Thm 4.5.
- **Deserves a full check**: no. **Interest**: 1.

### A1-17
- **Title**: Direct proof of a(X) = 1 with repaired meromorphic descent and an explicit Appell–Humbert bridge. **Type**: new proof or restatement of a known result ([AC26] §9.1), with small repairs.
- **Where**: algebraic_dimension.tex, all (299 lines); 26 Aug. Ledger S6-ALG-DIM.
- **Statement**: NS(F_b) = Z eta for b outside a countable set, H_eta indefinite, eta^2 = 12 vol, a(F_b) = 0; a meromorphic function constant on
  uncountably many fibres is f^*phi with phi meromorphic (root estimate |phi(t)| <= C|t-t_0|^{-M/k} at the special points); M(X) = f^*C(t).
- **Support**: full proofs. **What it adds**: over [AC26] Lemmas 9.2–9.6, Prop. 9.7: the bridge G_E = 2 conj(H_E)^{-1} between the computed matrix and
  the Appell–Humbert form; connectedness of f^{-1}(B°) minus the polar set; the growth estimate that makes phi meromorphic at 0, 1, infinity.
  [E26] only quotes [AC26] §9.1. Not searched.
- **First assessment**: fine. The linear-independence argument for 1, tau, mu, beta, 6mu^2 - tau beta uses only the transformation laws.
- **A full check must establish**: the expansion (3.3) of E ∧ sigma_1 ∧ sigma_2 = P_E vol and the matrix G_eta.
- **Deserves a full check**: no. **Interest**: 2.

### A1-18
- **Title**: Local repairs of [AC26] (grouped). **Type**: correction of [AC26].
- **Where**: local_repairs.tex l.1–53; also summary l.146–162 and research_log Round 17.
- **Statement**: (1) Prop. 4.7(iv): the closed-image conclusion holds because s(B) is the equalizer of id and s∘f in a Hausdorff space; the printed
  justification is not needed. (2) Remark 7.28 ("|p| = 1 iff (l_1 mod 3, l_2 mod 4) in {(1,3),(2,1)}") is false for a fixed triple, e.g. (100,1,-1) has
  p = 1199; it must be read existentially in l_0. (3) Lemma A.3 prints cohomological arrows labelled as homology. (4) Remark A.6 must read
  pi_1(N_0) = Lambda-bar = pi_1(W), not Lambda (transcription l.5262 indeed has "pi_1(N_0) = Lambda = pi_1(W)"). (5) a build defect, not mathematics.
  (6) The assertion that Omega^1_{X/B} has torsion along all three singular fibres ([AC26] Remark 1.3 and l.4330) is false at the cusp: at t = xy
  and t = xyz the module is torsion-free and not locally free; torsion occurs only along S_1, S_2. (7) In the finite-filling Hodge-line computation
  the invariant canonical section s_j^{m_j-1-a_j} e^{phi} ds_j ∧ e has divisor (m_j-1-a_j)S_j, so it is not a frame for j = 2; the direct image is
  O_{D_j}·s_j^{m_j-1-a_j} theta'_j.
- **Support**: short arguments. I checked (6): O^2/O(y,x) ≅ the ideal (x,y), and O^3/O(yz,xz,xy) is torsion-free because gcd(yz,xz,xy) = 1; at
  t = s^m the quotient has the torsion O/(s^{m-1}).
- **What it adds**: errata to [AC26]; (6) and (7) matter for the Hodge computations (other readers). [E26] does not discuss these. Not searched.
- **First assessment**: (1),(3),(4),(6) are right; (2) is a matter of reading (the remark is evidently about the residue classes; "Refuted" is strong);
  (7) not checked (depends on analytic_picard.tex).
- **A full check must establish**: (7) against the Hodge files; whether (4) is an error of the source PDF or of the transcription.
- **Deserves a full check**: maybe — only (6) and (7), together with the Hodge reader. **Interest**: 3.

### A1-19
- **Title**: Integral algebra certificates and the general-p package (pi_1 = Z/|p|, H_* = (Z, Z/p, Z/p, Z/p, Z/p, 0, Z)); sphere recognition written out. **Type**: new proof or restatement of a known result ([AC26] §2, §7, §8).
- **Where**: exact_algebra.tex, all; topology_reduction.tex l.1124–1275; integral_leray.tex l.936–954. 24–27 Aug.
- **Statement**: as in 1.2 and 1.4. **Support**: hand-checkable matrices; "exact audit harness" (28 + 38 checks, summary l.3652–3669).
- **What it adds**: nothing over [AC26] Thm 7.17, 7.22, 8.1 in content; it is the independent recomputation. Relative to [E26]: general p (Engel
  proves only |p| = 1), and the invariant class q = uw + 6 gamma delta (Engel's omega of type (1,6); my check: q is T_1- and T_2-invariant).
  The geometric realization for general (l_0,l_1,l_2) is not re-proved here (see 3, item 5).
- **First assessment**: fine. **A full check must establish**: nothing new.
- **Deserves a full check**: no. **Interest**: 1.

### A1-X1 (outside my assignment; lightly read; recorded so that it is not lost)
- **Title**: Classification of the family in the period constant: X_c ≅ X_{c'} iff c' - c in 2Z; parameter disc w = e^{-pi i c}, 0 < |w| < e^{-pi M};
  nonzero Kodaira–Spencer class of the family. **Type**: new result; answers the open question of [AC26] Remark 6.4; refines/corrects [E26] Remark 8.1.
- **Where**: period_shift_classification.tex (26 KB; pshift:thm:classification, l.53–72; conclusion l.560–600) and period_parameter_deformation.tex
  (18 KB; thm:retained-period-deformation) with analytic_canonical_ring.tex; 6 Sep 2026. Summary l.44–54 and l.125–142. Evidence:
  evidence\period_lattice_continuation_20260906\period_deformation\INDEPENDENT_GLOBAL_AUDIT.md (read in full: "no mathematical error or missing
  implication was found"; an internal agent audit).
- **Statement**: for c, c' with Im < -M the threefolds X_c, X_{c'} are biholomorphic iff c' - c in 2Z; every biholomorphism preserves f; for even n an
  explicit isomorphism X_c -> X_{c+n} with lattice part I - nE, E = delta^ ⊗ gamma. The middle families agree for all integer shifts; "the
  multiplicity-four filling retains an order-two obstruction to odd shifts". Over a parameter disc the X_c form a proper holomorphic submersion;
  the Kodaira–Spencer class at each c_* is nonzero (Beltrami matrix nu_delta = delta/(2iD + delta)·[[0,0],[-m/T,1]]; the anticanonical pencil
  |-2K_X| recovers f over the dual numbers and its three critical values rigidify the base).
- **Support**: written proofs (not read by me beyond the statements and the audit). Ledger lines 143–151 of claim_ledger.txt are free text, not a JSON entry.
- **What it adds**: [AC26] Remark 6.4 (l.1890): "Whether X_{c_0} ≅ X_{c'_0} for admissible c_0 ≠ c'_0 is left open." [E26] Remark 8.1 sketches that the
  family "is indeed deforming" and speaks of a submersion over the u-disc with fibre X(u,a_0,a_1). The workbench says (l.584–588) that "the
  integer-period quotient seen by the middle family has coordinate w^2" and is covered two-to-one by the w-disc, the two lifts being non-isomorphic.
  My reading in Engel's terms (not in the workbench, to be checked): w^2 = u^{±1}; going once around u = 0 replaces the torsion data (a_0,a_1) by
  (a_0 ± lambda_0/3, a_1 ± lambda_0/4) because Engel's e_4 is a multivalued period, and this gives a non-isomorphic threefold; so the family with
  fibre X(u,a_0,a_1) lives over the double cover of the u-disc, not over the u-disc.
  A quick consistency check of mine: by A1-5, Alb(S_2) has modulus (kappa_2 + c)/2, which changes under c -> c + 1 and not under c -> c + 2.
  Literature: one web search for deformation/moduli results on this family (12 Nov 2026): nothing found.
- **First assessment**: plausible and, if right, the most significant item near my topic. Not assessed in depth.
- **A full check must establish**: the centralizer lemma (pshift:lem:centralizer); the order-two invariant (PS10)–(PS12); the even-shift isomorphism
  through the cusp (PS18)–(PS28); the dictionary c <-> Engel's u and the monodromy of (a_0,a_1) around u = 0; the Kodaira–Spencer computation.
- **Deserves a full check**: yes — it settles a question left open in [AC26] and sharpens a remark of [E26]. **Interest**: 5.

---------------------------------------------------------------------------------------------------------------------------

## 3. Doubts and errors

1. [E26] Remark 8.3 against cusp_globalization_replacement.tex (v): Engel says the fibrewise quotient by the rank-3 subtorus "extends continuously"
   over infinity; the workbench proves it does not (two paths to the same triple point with character values 3/4 and 1/2). I re-derived the
   computation and agree with the workbench. Engel's map exists only after replacing the quotient near W by a collapse-type map (homotopic on the
   boundary). See A1-1.
2. claim_ledger.txt, entry S6-CUSP-ACTION: "exponentiation identifies its punctured part with the abelian-surface family". The fibres are complex
   2-tori, very generally non-algebraic; mathematical_summary.tex l.409–410 has the right wording ("not with an abelian-surface family"). Stale ledger text.
3. local_repairs.tex item 2 marks [AC26] Remark 7.28 "Refuted". The remark is a statement about residue classes with l_0 free ("l_0 is the free
   gluing parameter"); reading it for a fixed triple is uncharitable. An erratum of wording, not a false claim.
4. exact_algebra.tex prop:terminal-all-degree is a formal implication ("assume only the following algebraic outputs"); it is not a geometric
   computation of H_*(X) for general p. The ledger says so (S6-ALG-HOM nonclaim).
5. General (l_0,l_1,l_2): the workbench constructs only the tautological cusp gluing and the twists (eps, -eps') (candidate_geometry.tex);
   prop:leray-e2 is stated for the actual twist; prop:geometric-pi1 for (0,1,-1); cor:candidate-mv-sphere for p = -1. thm:mv-leray-comparison and
   prop:cusp-mv-blocks carry a general p and refer to "the general affine cusp regluing" t_mu with l_0 = gamma(mu) (l.1005–1014) without constructing
   it. So "pi_1 and H_* for every admissible triple" remains a theorem of [AC26] (Thm 7.17, 7.22, Prop. 6.7), re-checked here only algebraically.
   Not an error; a limit of what was re-proved.
6. candidate_geometry.tex prop:period-exact-admissible-constants: M is defined through "the" particular solution beta^part, which is unique only up
   to an additive constant; the statement is correct for any fixed choice, but M is not an invariant until a normalization (e.g. b(0) = 0) is fixed.
   mathematical_summary.tex and period_shift_classification.tex use M in e^{-pi M} without fixing it.
7. cusp_toric_cover_completion.tex (4): normality of N_0[N] along the double and smooth strata is asserted by "the corresponding face-chart
   calculations" without display. True (toric), but not written.
8. cusp_globalization_replacement.tex (iii): the minimality statement ("four copies are minimal") is relative to the unscaled Euclidean fibre
   metric and to quotients with primitive invariant kernels; the file says this, the ledger summary line is shorter and reads more absolute.
9. All "independent" reviews cited in the evidence folders (INTEGRATED_GEOMETRY_REVIEW.md, INDEPENDENT_GLOBAL_AUDIT.md, FINITE_INDEPENDENT_REVIEW.md)
   are other agent sessions of the same workbench; "Reviewer B" (summary l.3671) is not identified in the files I read.
10. Nothing in the nine assigned files looked mathematically wrong to me at survey depth. The exact checks I ran (orders, A_jv_j = v_j, determinants
    -3 and -2, Smith forms of alpha_1, alpha_2, Phi, det Delta_1, (C.20) against wedge^2 M_0 - I, invariance of q, A_2A_1, the three edge exponents,
    Kummer fibre lengths) all agree with the text.

## 4. Not read

- mathematical_summary.tex: read only the parts listed in 1.10 (about 900 of 3782 lines); the rest concerns other topics (Hodge, CDP, Koide,
  Niemeier, quaternionic and Yang–Mills material).
- ledgers\claim_ledger.txt and morphism_ledger.txt: only the entries for my ids and their neighbours; research_log.tex only Rounds 2, 3, 17, 29 and
  the round headings; next_lemmas.tex, dependency_ledger.txt, literature_sources.md not read.
- evidence\s6_global_smooth_reaudit_20260905: PERIOD_AUDIT.md, CUSP_AUDIT.md, FINITE_INDEPENDENT_REVIEW.md, SMOOTH_INDEPENDENT_REVIEW.md (scalar–Gauss,
  not S6), the JSON receipts and the .tex snapshots not read (the snapshots duplicate candidate_geometry.tex); FINITE_FILLINGS_AUDIT.md only its first 60 lines.
- evidence\period_lattice_continuation_20260906: jm_cubic\ not opened (not S6 geometry); period_deformation\INDEPENDENT_GLOBAL_AUDIT.md read in full.
- period_shift_classification.tex and period_parameter_deformation.tex are not in my assignment; I read only the theorem statements and the closing
  paragraph of the first (see A1-X1). cusp_spectral_geometry.tex and cusp_cone_sphere_routes.tex (cited by cusp_globalization_replacement.tex) not read.
- [AC26]: sections 2–8 and Appendices A, B were consulted at the statements and at the proofs of Lemmas 7.5–7.10, Prop. 7.27, Thm 3.4/Prop. 3.15,
  Thm 5.4/Lemma 5.7, Prop. 4.6, Prop. 6.7, Remarks B.2/B.4; not read line by line. main.tex (annotated edition) not opened.
- Literature: two web searches (Seifert quotient / follow-ups to [E26]; deformation and moduli of the family), no relevant hits; no search for the
  minor items. SCOREBOARD.md has no S6 entry.
