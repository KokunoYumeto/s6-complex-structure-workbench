# G1a notes: course CG-S6 "Complex threefolds from marked torus families", lessons 1-6, 8, 9

Reader G1a (Claude Fable 5.2), 12 Nov 2026. Read only; nothing in the course folder was changed or run (the checkers write JSON
into the course folder, so I did not run them; my own scratch check is in `work\scratch\G1a\check1.py`).

Course folder: `C:\Users\user\Documents\math\research\s6_recent_results_main\courses\CG-S6\` (below: `CG\`).
Abbreviations: L4 = lesson 4, "L5 (13.9)" = equation (13.9) of lesson 5, "L9 Thm 8.1" = Theorem 8.1 of lesson 9.
Notation of the course: lattice Lambda = Z<gamma^, u^, w^, delta^>, covectors gamma, u, w, delta; period matrix
Pi = [[6 mu, tau, 1, 0], [beta, mu, 0, 1]]; D = Im beta - 6 (Im mu)^2 / Im tau; beta_c = beta^part + c; monodromy A_1 (order 3),
A_2 (order 4), M_0 = (A_1 A_2)^-1; twist vectors v_1 = (1,2,-4,0), v_2 = (-1,-3,3,0); E = delta^ (x) gamma; p_1, p_2, p_0 = t = 0, 1, infinity.

Short answers to the questions of the assignment (details in the candidates):

- **u versus w^2 (reader B's inference): confirmed, it is proved in the course.** L4 Thm 7.1 and L5 Thm 13.1 prove
  phi_per = e^{-2 pi i c} phi_part and, for an independently fixed geometric reference linearization phi_ref with
  phi_part = lambda_0 phi_ref, u_ref = lambda_0 e^{-2 pi i c}. L9 Exercise 9.3 writes it as u_ref = lambda_0 w^2, w = e^{-pi i c},
  range 0 < |u_ref| < |lambda_0| e^{-2 pi M}, and says: the two square roots are parameters differing by 1 mod 2Z and "the two lifted
  threefolds are distinguished by Section 6, although their middle family agrees". The constant lambda_0 is not evaluated (it is a
  convention: the reference linearization is only defined up to scale).
- **The dictionary [AC26] <-> [E26]** is L4 sections 6-8 plus L5 sections 9-13 (candidate G1a-2).
- **M = max D_part**: existence and finiteness only (L4 Thm 5.1). No value, no bound, no location of the maximum.
  L4 Exercise 9.1 uses "M = 7/3" as a hypothetical number.
- **h^1(T_X)**: only >= 1 (L9 (4.9)). h^2(T_X), completeness, unobstructedness: not addressed; L9 says explicitly that no
  assertion is made that the family exhausts the deformations.
- **Limit w -> 0 ([E26] Conjecture 8.2)**: not addressed (L8 Sources: "His conjectural central limit ... is not proved by this lesson").
- **Other discrete choices (a_0, a_1)**: L9 classifies only the retained family (fixed v_1, v_2). L6 Exercise 2 builds the
  threefolds with twist vectors r_1 v_1, -r_2 v_2 and computes pi_1 = Z/|4 r_1 + 3 r_2|; it makes "no homology or smooth-sphere
  claim". This is less than [AC26] Thm 7.22 (H_* for every admissible pair). Nothing on universal covers. See G1a-9 and G1a-13.

---

## 1. Reading notes

### 1.0 Course metadata
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

### 1.1 `CG\src\finite-quotients-and-line-bundles.md` (lesson 1; 23.3 KB, 417 lines; 8 Oct 2026)
Sections: 1 period map (real isomorphism iff Im tau > 0, D != 0); 2 Prop 2.1 (fixed and image lattices of A_1, A_2: Lambda^{A_1} =
Z eps + Z delta^, (A_1 - I)Lambda = Z e_1 + Z f_1, index 3; same at j = 2 with index 2; saturation); 3 Thm 3.1 (isogenies
l_j: E_j x F_j -> T_j with kernels <k_1 = (2/3, rho)>, <k_2 = (1/2, i)>); 4 Thm 4.1 (<k_1,h_1> = C_3 x C_3, <k_2,h_2> = C_2 x C_4 act
freely; covers of degree 9, 8 of S_1, S_2); 5 Thm 5.1 (N_j of exact holomorphic order m_j, smoothly trivial by
H_j(x) = exp(-2 pi i eps_j gamma(x))); 4 exercises (annihilators; sections of N_j^k; H^0(Omega^1_{S_j}) = C d xi; S_j not a torus).
Relation: the course version of `finite_filling_certificates.tex` FF1-FF22, FF42-FF46 (reader A1, candidate A1-5).

### 1.2 `CG\src\normal-boundaries-and-integral-maps.md` (lesson 2; 15.8 KB, 246 lines; 8 Oct)
Thm 2.1 (deck group Gamma_j of the disc bundle and of S_j: t_lambda, G^_j with G^_j^{m_j} = t_{v_j}); Thm 3.1 (punctured bundle:
P_j = Lambda x|_{A_j} Z, positive loop Q_j = t_{v_j} G~_j^{-m_j}); Thm 4.1 (kernel of P_j -> Gamma_j is the central Z generated by
h_j = G~_j^{m_j} t_{-v_j} = Q_j^{-1}); Cor 4.2 (explicit isomorphism P_j = Gamma_j x Z, second component eps_j gamma(lambda));
Thm 5.1 (H_1(S_j) = Z^2; pi_j^* H^1(S_j;Z) = Z(m_j gamma) + Z psi_j, psi_1 = 2u+w+3 delta, psi_2 = u+w+2 delta, index m_j);
3 exercises. Relation: FF30-FF41; [AC26] Lemma A.4 in degree 1.

### 1.3 `CG\src\varying-finite-fillings.md` (lesson 3; 27.5 KB, 479 lines; 9 Oct)
Thm 1.1 (all local period germs: q_j = s^{d_j} F_j(s^{m_j}), tau_j = (a_j - conj(a_j) q_j)/(1 - q_j), mu_1 = (2 - tau_1)/3 +
s^2 H_1(s^3)/(1 - q_1), mu_2 = (1 - tau_2)/2 + s H_2(s^4)/(1 - q_2), beta_j = beta_{j,0} + B_j(s^{m_j}) + b_j(s) with
b_j = (1/m_j) sum_k k phi_j(zeta_j^k s); conversely every germ with the laws has this form uniquely); section 2 (real inverse of the
marking, covariance R_j Pi = Pi(zeta_j s) A_j); Thm 3.1 (N_j = T_j/<G_j> proper over the disc, central fibre m_j S_j, real-analytic
diffeomorphism with the normal disc bundle of lesson 2); Thm 4.1 (T_j is the normalization of the base change, m_j branches
s = zeta_j^{-a} u; full proof of integral closure by idempotents); Thm 5.1 (h_j G_j h_j^{-1} = G_j^0 with h_j = translation by
(log s / 2 pi i) Pi(s) v_j); 3 exercises. Relation: FF23-FF41 and candidate_geometry.tex; A1-6.

### 1.4 `CG\src\global-periods-and-line-bundle-quotients.md` (lesson 4; 34.3 KB, 597 lines; 9 Oct)
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

### 1.5 `CG\src\cusp-and-compact-threefold.md` (lesson 5; 81.8 KB, 1304 lines; 9 Oct)
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

### 1.6 `CG\src\integral-monodromy-and-fundamental-group.md` (lesson 6; 38.4 KB, 715 lines; 9 Oct)
Prop 1.1 (T_j = (A_j^{-1})^t, orders, T_1 T_2 T_0 = I, ker = im (M_0 - I) = Lambda_tor = Z w^ + Z delta^); Thm 2.1, 2.2 (cusp
invariants; common invariants Z gamma, Z q with q = uw + 6 gamma delta, Z gamma u w; coinvariants Z[delta], Z[gamma delta] with
[uw] = 6[gamma delta], Z[u w delta]; complete relation matrices); Lemma 3.1 (van Kampen in the form used); Prop 4.1
(pi_1(J) = Lambda x| F(rho_1, rho_2)); Prop 5.1 (fillings impose rho_1^3 = t_{v_1}, rho_2^4 = t_{v_2}); Lemma 6.1 (Y_eps simply
connected, chart proof), Thm 6.2 (pi_1(N_0) = Lambda/Lambda_tor, kernel H); Thm 7.1 (pi_1(X) = 1 from the presentation
<c, x, y | c central, xy = 1, x^3 = c, y^4 = c^{-1}>); Prop 8.1 (integral dictionary with Engel's marking, matrix P);
4 exercises (G(l_0,l_1,l_2) = Z/|12 l_0 - 4 l_1 - 3 l_2|; additional free affine fillings X_{r_1,r_2}; q^2 = 12 vol; H = Z^3 not central).
Relation: exact_algebra.tex, integral_leray.tex `prop:geometric-pi1`; [AC26] Thm 7.17; [E26] sections 5-6.

### 1.7 `CG\src\canonical-divisor-and-intrinsic-fibration.md` (lesson 8; 29.3 KB, 505 lines; 9 Oct)
Lemma 1.1 (f_* O_X = O_B); Sec 2 (characters chi_j = zeta_j det R_{g_j}, exponents a = (2,1), k_j = m_j - 1 - a_j = (0, 2),
correcting units phi_j); Sec 3 (K = f_* omega_{X/B} = O_B(p_0), generated by Theta^{-1} d zeta_1 ^ d zeta_2); Thm 4.1
(div(ev) = 2 S_2; omega_X = O_X(-2 S_2); omega_X^{-2} = f^* O_B(p_2)); Thm 5.1 (f_* O_X(k S_2) = O_B(floor(k/4) p_2) for all k);
Cor 5.2 (h^0(omega^{-m}) = floor(m/2) + 1; h^0(omega^m) = 0 for m > 0); Thm 6.1 (R(X, -K_X) = C[U,V], degrees 1, 2);
Thm 7.1 (|-2K_X| base-point free, equal to f up to the explicit isomorphism beta(t) = [t-1 : A + B(t-1)]; |-K_X| = {2 S_2});
Cor 7.2 (any biholomorphism between two threefolds of the construction commutes with the fibrations, and the base map is the
identity); 4 exercises (all graded automorphisms; every member of the pencil with multiplicity).
Relation: analytic_canonical_ring.tex (CR1)-(CR5), analytic_picard.tex (9.2)-(9.6); reader B, candidate B-8.

### 1.8 `CG\src\periods-and-nontrivial-deformation.md` (lesson 9; 49.4 KB, 808 lines; 11 Oct)
Thm 1.1 (proper family X_Q -> Q over discs Q in P = {Im c < -M}); Thm 2.1 (marked map w = A_delta zeta + B_delta conj(zeta),
Beltrami matrix nu_delta = delta P/(2iD + delta)); Prop 3.1 (KS_F(d/dc) = -[nu'] != 0); Sec 4 (relative pencil; Lemma 4.1;
critical schemes; (4.9) KS_X != 0, h^1(T_X) >= 1); Lemma 5.1 (centralizer {aI + bE}; middle families: c' - c in Z, linear part
+-I); Sec 6 ((6.2), (6.3): N_j l_j = -(1-a) v_j - n eps_j delta^; (6.4), (6.5): Lambda^{A_1}/N_1 Lambda = Z/3,
Lambda^{A_2}/N_2 Lambda = Z/4 + Z/2); Sec 7 (construction of X_c -> X_{c+n} for even n: (7.1)-(7.16)); Thm 8.1
(X_c = X_{c'} iff c' - c in 2Z); (8.2) parameter disc w = e^{-pi i c}; 4 exercises (9.3: u_ref = lambda_0 w^2 and the KS class in
the u-coordinate; 9.4: critical values over C[eps]).
Relation: the receiving proof of the two files in 1.10; reader B, candidates B-6, B-7.

### 1.9 Companions
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

### 1.10 `CG\sources\period_parameter_deformation.tex` (18.3 KB, 396 lines) and `period_shift_classification.tex` (25.7 KB, 590 lines)
Byte-identical to the workbench files read by reader B (sha256 8baadffb... and 6dff2b4b..., same as
`canonical_S6_snapshot\supporting_materials\workbench\research\period_*.tex`). (PD1)-(PD18) and (PS1)-(PS29), (PS28a).
Lesson 9 follows them step by step: sections 1-4 = PD; sections 5-8 = PS (Lemma 5.1 = pshift:lem:centralizer, (6.3) = (PS10),
(6.4)-(6.5) = (PS11)-(PS12), (7.1) = (PS13), (7.8) = (PS21), (7.12) = (PS24), (7.14) = (PS27), (7.16) = (PS28a), (8.2) = (PS29)).
What the lesson has and the tex files do not: Exercise 9.1 (composition of the marked maps with the changed D), Exercise 9.3
(u_ref = lambda_0 w^2, the KS class in the u-coordinate, (9.9)), Exercise 9.4, and the references to L4/L5 for the meaning of u.
What the tex has and the lesson does not: nothing mathematical that I saw; the tex ends with the same non-claims.

### 1.11 Checkers (`CG\checks\`); none was run by me
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

### 1.12 Read for comparison
[E26] `literature\engel_S6.txt` L100-700 (sections 1.3-5) and L1160-1300 (section 8). [AC26] transcription: L956 (Remark 3.12),
L1651 (Prop 5.6), L1722-1790, L1795-1891 (Construction 6.1, Prop 6.3, Remark 6.4), L2809-2825, L3005-3010 (Thm 7.22),
L5149-5160 (Lemma A.4). `B_notes.md` B-6, B-7, B-8, B-17; `A1_notes.md` A1-2, A1-4, A1-5.

---

## 2. Candidates

### G1a-1
- **Title**: Inside the family, X_c is biholomorphic to X_{c'} exactly when c' - c is an even integer; the isomorphism classes form
  the punctured disc 0 < |w| < e^{-pi M}, w = e^{-pi i c}. **Type**: new result (answers the question left open in [AC26] Remark 6.4).
- **Where**: `CG\src\periods-and-nontrivial-deformation.md`, sections 5-8 (L335-671): Lemma 5.1 (L354-420), section 6 (L422-476),
  section 7 (L478-638), Thm 8.1 (L642-653), (8.2) (L655-666); uses L8 Cor 7.2 (L411-420 of the lesson 8 source). 11 Oct 2026.
  Same mathematics as `period_shift_classification.tex` (6 Sep 2026), candidate B-7.
- **Statement**: (Thm 8.1) For any c, c' in P = {Im c < -M}: X_c = X_{c'} (biholomorphic, nothing else assumed) iff
  c' - c in 2Z. Every such biholomorphism commutes with f and induces the identity on B. For each even n, (7.14) gives an
  isomorphism X_c -> X_{c+n} with complex-linear part I_2 on the fibre coordinates and lattice map I - nE, E = delta^ (x) gamma.
  Ingredients: (Lemma 5.1) the rational centralizer of A_1, A_2 is {aI + bE}; a biholomorphism of middle families over the identity
  of B^o has L Pi_c = Pi_{c'} (aI + bE), a = +-1, hence L = a I_2 and c' - c = -b/a in Z. (Section 6) If such a map extends over
  D_j, its lift to the normalized cyclic cover is translation by B_j with
  B_j(g_j z) - R_{g_j} B_j(z) = Pi_c(g_j z) ( ((1-a) v_j + n eps_j delta^)/m_j + l_j ), l_j in Lambda, whence
  N_j l_j = -(1-a) v_j - n eps_j delta^, N_j = 1 + A_j + ... + A_j^{m_j - 1}. N_1 Lambda = 3Z v_1 + Z delta^,
  N_2 Lambda = 4Z (1,3,-3,0) + 2Z delta^; Lambda^{A_1}/N_1 Lambda = Z/3, Lambda^{A_2}/N_2 Lambda = Z/4 + Z/2. a = -1 is
  impossible (3 does not divide 2); for a = 1 the obstruction is the class of n delta^ in Lambda^{A_2}/N_2 Lambda, of order 2.
  (Section 7) For n even: r_1 = -(n/3)(u^ + w^), l_1 = -n w^, r_2 = (n/4)(u^ + w^), l_2 = (n/2) u^, with
  (I - A_j) r_j = (n eps_j/m_j) delta^ + l_j; cusp value of the cocycle l_0 = (3n/2) w^ - (n/2) delta^; cusp map
  (x, t_c) -> (t_c^{q_n} x, t_c), q_n = (-3n/2, n/2), a fan automorphism; the remaining additive problem is a torsor under the rank-2
  bundle V, 0 -> O_B e -> V -> O_B(-p_0) -> 0, H^1(B, V) = 0, H^0(B, V) = C e. The maps can be chosen with
  F_{2h, c+2k} o F_{2k, c} = F_{2(h+k), c} (7.16), jointly holomorphic in c.
  Parameter statement (8.2): P/2Z -> {0 < |w| < e^{-pi M}}, w = e^{-pi i c}, is a bijection onto the set of isomorphism classes
  "represented by this retained family"; the middle family has parameter w^2, covered 2:1.
- **Support**: written proof of about 340 lines in the lesson (plus the 590-line tex). Checker
  `verify_period_deformation.py` (42 exact identities; lattice arithmetic only). Course status: author self-check, no independent
  review. No claim that the family is complete.
- **What it adds**: over [AC26]: Remark 6.4 (transcription L1890-1891) says "Whether X_{c_0} = X_{c'_0} for admissible
  c_0 != c'_0 is left open"; Prop 6.3 proves independence of the auxiliary choices only. Over [E26]: Remark 8.1 says the manifolds
  deform (uniqueness of the map to P^1, periods vary, E_0 and E_1 vary); no classification. Over the September workbench: the
  same theorem; the course adds the explicit link to Engel's parameter (G1a-2) and Exercise 9.3. Literature: reader B found
  Viaclovsky arXiv:2610.39102 (not locally isotrivial, Kuranishi dimension >= 1) and X. Yang arXiv:2609.29666; my own search
  (12 Nov, WebSearch, "complex structures on S^6 deformation family non-biholomorphic ... Kuranishi") returned nothing newer or
  more specific; I did not fetch those two papers again.
- **First assessment**: I re-derived the necessity part by hand from the definitions (the lift to the normalization commutes with
  the generator G_j exactly; the equivariance equation; iterating m_j times gives N_j kappa = 0) and got (6.2)-(6.3) with the same
  signs. I checked by hand in the sufficiency part: (7.2) for j = 1, 2; (7.4); the cocycle value (7.8) and
  a_0(g_0 z) - a_0(z) = -q_n = Pi l_0; the overlap identity (7.15); that the first coordinate of the difference sheaf has the
  factors -1/tau, 1/tau of L4 (3.3), so that the quotient is O_B(-p_0) and H^1 vanishes. I found no gap. Two cross-checks that
  the course does not make: (i) by L1 Thm 4.1, Alb(S_1) = C/(Z + kappa_1 Z) and Alb(S_2) = C/((1/2)Z + (kappa_2/4)Z), of modulus
  kappa_2/2, with kappa_j(c) = kappa_j^part + c (reader A1 noted this). So the nome of Alb(S_2) is a constant times w and the
  nome of Alb(S_1) a constant times w^2: c -> c+1 changes Alb(S_2) for generic c and c -> c+2 changes neither. This gives the
  "only if" for generic c without the lattice argument and gives w an intrinsic meaning. (ii) [AC26] (L1782-1788) notes that
  N_j depends on v only modulo m_j Lambda^{A_j}; the computation here shows that the finer group Lambda^{A_j}/N_j Lambda
  (Z/3, and Z/4 + Z/2) is what matters for extending a given map of the punctured family, so of Engel's 9 resp. 16 classes
  a_i in (1/m)Lambda^{T_i}/Lambda^{T_i} the delta-direction is redundant at t = 0 and half redundant at t = 1.
  Risks: the proof leans on L8 Cor 7.2 (f is |-2K_X|) and on the statement that the special fibres are distinguished by type; on
  L3 Thm 4.1 (normalization); on the claim that a section with cusp cocycle l_0 in Lambda_tor extends over all strata (it is a fan
  automorphism times a unit; looks right). The theorem is about the fixed (v_1, v_2); see G1a-13 for the other discrete choices.
- **A full check must establish**: (1) L8 Cor 7.2; (2) the lift to J'_j and its exact commutation with G_j; (3) (6.2)-(6.5);
  (4) (7.1)-(7.15), in particular local non-emptiness of the affine sheaf H_n at p_1, p_2, p_0 and exactness of (7.12);
  (5) L4 Lemma 2.1 in the form used; (6) that (7.16) gives a proper family over the w-disc whose fibres are pairwise
  non-biholomorphic (stated only as an identity of maps); (7) the Albanese cross-check; (8) literature after 6 Sep 2026.
- **Deserves a full check**: yes; it settles a question stated as open in [AC26] and gives the exact parameter space of the
  known family. **Interest**: 5.

### G1a-2
- **Title**: Exact dictionary between the period description ([AC26]) and the line-bundle description ([E26]):
  u = lambda_0 e^{-2 pi i c} = lambda_0 w^2; log of the flat norm of the linearization is 2 pi D; exact admissible disc.
  **Type**: refinement of [AC26] and of [E26] (new proof of a relation that both state without proof), with new exact statements.
- **Where**: `CG\src\global-periods-and-line-bundle-quotients.md` sections 6-8 (Thm 6.1 L361-416, Thm 7.1 L433-461, Prop 8.1
  L496-535); `CG\src\cusp-and-compact-threefold.md` sections 9-13 (L466-1205), Thm 13.1 L1169-1199; L9 Exercise 9.3 (L742-774).
  9-11 Oct 2026.
- **Statement**:
  (a) (L4 Thm 6.1) For fixed (tau, mu, beta): dividing C^2 by the last three columns of Pi and exponentiating the second
  coordinate gives L_mu^x = (C x C^*)/((xi, W) ~ (xi+1, W) ~ (xi+tau, e^{2 pi i mu} W)); L_mu = O_{E_tau}(P - O) with
  P = [mu] (section theta(xi - mu)/theta(xi)); the first column acts by A(xi, W) = (xi + 6 mu, e^{2 pi i beta} W), and
  C^2/Pi Lambda -> L_mu^x/<A>, [(xi, eta)] -> [(xi, e^{2 pi i eta})], is a biholomorphism. A^{-1} covers translation by -6P with
  fibre multiplier e^{-2 pi i beta}.
  (b) (L4 Thm 7.1) With the flat norm N(xi, W) = |W| exp(2 pi (Im mu/Im tau) Im xi): N(A^{-1} x) = e^{2 pi D} N(x). So
  D(t) = (1/2 pi) log of the operator norm of the lifted translation on the fibre over t in the flat metric, constant on each
  elliptic fibre. For beta = beta^part + c: u = e^{-2 pi i c}, |u| = e^{2 pi Im c}, and 0 < |u| < e^{-2 pi M} is equivalent to
  non-singularity at every base point.
  (c) (L4 Prop 8.1) x = f^2 wp_tau(xi), y = (1/2) f^3 wp'_tau(xi), f^2 = -(2/3) t (t-1) g_2(tau)/g_3(tau)
  (f^4 = 12 t^3 (t-1)/g_2, f^6 = -8 t^4 (t-1)^2/g_3; f(g_1 z) = -f/tau, f(g_2 z) = f/tau) identifies the elliptic family over
  t != 0, 1, infinity with y^2 = x^3 - 3 t^3 (t-1) x + 2 t^4 (t-1)^2 (Engel's equation).
  (d) (L5 Thm 9.1, 11.2) the section [mu] is a generator P of the Mordell-Weil group Z, P = +-(0, sqrt2 t^2 (t-1)) (G1a-3).
  (e) (L5 Thm 12.2, 13.1) Hom(t_{6P}^* M, M) = pi_S^* O_B(1) for M = O_S(P - O) on the resolved surface; the isomorphism
  I: L_mu -> M, I([xi, W]) = K W s_{P-O}(xi)/F_theta(xi), K = 2 r_theta/f, r_theta = theta(-mu)/theta'(0), sends the frame W = 1
  at O to dx/y; the transported period lift phi_per is a global section with div(phi_per) = F_infinity (orders 0, 0, 1 at
  t = 0, 1, infinity computed in 13.1-13.2; local scalars e^{-2 pi i kappa_1}, e^{-2 pi i kappa_2} at the finite points, (13.8));
  beta = beta_part + c <=> phi_per = e^{-2 pi i c} phi_part; with an independent reference phi_part = lambda_0 phi_ref:
  u_ref = lambda_0 e^{-2 pi i c}, admissible disc 0 < |u_ref| < |lambda_0| e^{-2 pi M_part}.
  (f) (L9 Ex. 9.3) u_ref = lambda_0 w^2; KS_F(d/du_ref) = -(1/(4 pi u_ref D)) d/dzeta_2 (x) (d zeta^-_2 - a d zeta^-_1).
- **Support**: written proofs (L4 about 110 lines for (a)-(c); L5 sections 9-13 about 740 lines). Checkers
  `verify_global_periods.py`, `verify_cusp_geometry.py` (algebra only). Author self-check.
- **What it adds**: [AC26] Remark 3.12 states the elliptic-surface reading in two lines ("not needed later", no proof).
  [E26] section 1.3 says "Roughly, ... tau(z) is the period of the elliptic fibration, mu(z) encodes the third period arising from
  the circle of the principal G_m-bundle, and beta(z) encodes the fourth period"; Prop 2.4 gives "there exists a constant c such
  that |u| < c works" with an arbitrary Hermitian metric. The course gives the exact maps, the sign (-6P, e^{-2 pi i beta}), the
  exact relation u = lambda_0 e^{-2 pi i c}, and the sharp form of Prop 2.4: with the fibrewise flat metric the Z-action is
  properly discontinuous with torus quotients on every fibre iff max_t ||u phi_0||_flat < 1, i.e. |u| < e^{-2 pi M}, and for
  larger |u| some fibre is not a torus (L4 Thm 5.1). It also settles reader B's inference u ~ w^2: correct.
  Not in the course (my reading, to be checked): in Engel's language X_{c+1} is X(u; a_0 + delta/3, a_1 - delta/4) up to sign
  conventions, since Pi_{c+1} v_j = Pi_c (v_j + eps_j delta^). Engel's class e_4 = (0, tau(E_0)) is only defined modulo the
  circle class delta (tau(E_0) is defined mod 1), and the simultaneous change (e_4, f_4) -> (e_4 + delta, f_4 + delta) preserves
  all the data of [E26] Thm 5.1; it is the shift c -> c+1. So for a given u the threefolds X(u, a_0, a_1) with the same
  psi-values fall into exactly two isomorphism classes, exchanged by the monodromy of the marking around u = 0, and "the family
  over the punctured u-disc with locally constant (a_0, a_1)" closes up only over the w-disc. The course states the 2:1 cover but
  not this translation.
- **First assessment**: (a), (b), (c) are short and I checked them ((b): |W| -> e^{2 pi V}|W|, Im xi -> Im xi - 6U gives
  e^{2 pi (V - 6U^2/T)}). Sign conventions agree with [E26] Def. 2.3 (the generator acts by the lift of t_{6P}^{-1} defined by
  u phi_0). For (e) I read the order computation: at the finite points the argument evaluates at a generic point xi = f z of the
  strict component and uses 6 mu = p + r tau + delta with (p, r) = (4, -2), (3, -3) and delta/f holomorphic; at the cusp
  e^{-2 pi i beta} = q e^{-2 pi i b} has order one. I saw no gap, but the descent of I over B^o ("two isomorphisms with the same
  value at O agree") and the use of the base-section property to pass from one generic point to the whole fibre are the places to
  check. lambda_0 is not computed and has no canonical value.
- **A full check must establish**: (6.5)-(6.7) of L4 (theta conventions); Prop 8.1 including the sign laws of f; L5 Thm 12.2
  (multidegree zero, n = 1); L5 13.1-13.2; the equality of conventions with [E26] Def. 2.3-2.5; the translation into (a_0, a_1)
  above.
- **Deserves a full check**: yes; it is the bridge that lets results in one language be quoted in the other, and it carries the
  u = lambda_0 w^2 statement. **Interest**: 4.

### G1a-3
- **Title**: The middle period mu is the elliptic logarithm of a generator of the Mordell-Weil group; wp_tau(mu) = 0;
  e^{2 pi i mu(p_0)} = -5 +- 2 sqrt6. Consequence (mine): mu is the Eichler-Zagier zero of the Weierstrass function.
  **Type**: new proof of a statement that [AC26] makes without proof (Remark 3.12); computation; my added identification is a
  restatement through a known result.
- **Where**: `CG\src\cusp-and-compact-threefold.md` section 9 (Lemma 9.2, Thm 9.1, L481-597), Thm 11.2 (L920-964), (11.14)
  (L966-971), (13.9) (L1135-1144). 9 Oct 2026.
- **Statement**: (Thm 9.1) (x, y) = (f^2 wp_tau(mu), (1/2) f^3 wp'_tau(mu)) is a rational section P of
  y^2 = x^3 - 3 t^3 (t-1) x + 2 t^4 (t-1)^2, and every rational section is nP for a unique n: for a section Q with cusp-regular
  elliptic logarithm nu, nu(g_1 z) = -nu/tau + alpha_1 + beta_1 tau(g_1 z), n := -alpha_1 - 2 beta_1, a := alpha_1 + beta_1, one has
  nu = n mu + a (boxed (9.12)), because the difference is a section of O_B(-p_0). (Lemma 9.2) every rational section avoids the
  node at infinity and has a logarithm holomorphic in 1/t. (Thm 11.2) P = +-P_*, P_* = (0, sqrt2 t^2 (t-1)); P.O = 0;
  h(P) = 2 - 4/3 - 1/2 = 1/6; (6P).O = 2; P.(6P) = 2. (11.14) wp_tau(mu(z)) = 0 on every ordinary fibre. (13.9)
  u_P = e^{2 pi i mu(p_0)} satisfies u_P^2 + 10 u_P + 1 = 0.
- **Support**: written proof (about 200 lines for section 9, 90 for Thm 11.2), using the nodal parametrization
  X = 1 + 12u/(u-1)^2, Y = 12 sqrt3 u(u+1)/(u-1)^3 and the q-expansion (9.3) of wp. Checker entries "generator height",
  "complete nodal parametrization", "section cannot pass node first-order term".
- **What it adds**: [AC26] Remark 3.12 (L956): "its Mordell-Weil group is generated by P = (0, i t^2 (t-1)) [in the model
  y^2 = 4x^3 - 3 t^3 (t-1) x - t^4 (t-1)^2], and -mu is the Abel-Jacobi coordinate of P", recorded as "not needed later", no
  proof. [E26] section 2 takes a generator P from the Oguiso-Shioda table and never relates it to mu. The course proves the
  identification from the transformation laws alone, without the classification of Mordell-Weil lattices, and derives
  wp(mu) = 0 and the cusp value.
  My addition: since P_* is the section x = 0, mu(tau) is, up to sign and periods, the function z_0(tau) of Eichler-Zagier
  (Math. Ann. 258 (1981/82) 399-408): the zeros of wp(., tau) are m + 1/2 + n tau +- [ log(5 + 2 sqrt6)/(2 pi i) +
  144 pi i sqrt6 int_tau^{i infinity} (sigma - tau) Delta(sigma) E_6(sigma)^{-3/2} d sigma ]. The constant term gives
  e^{2 pi i mu(p_0)} = -(5 + 2 sqrt6)^{+-1}, which is (13.9); the special values mu(z_1) = (2 - rho)/3 and mu(z_2) = (1 - i)/2 are
  the zeros of wp at tau = rho (the centroid -(1 + rho)/3 + 1) and tau = i (the double zero (1 + i)/2), as they must be. Duke and
  Imamoglu give a hypergeometric expression for z_0 in terms of 1 - 1728/j = 1 - 1/t. I found no mention of Eichler-Zagier or of
  "zero of wp" in the course sources or in the workbench research folder (grep; the only hits for "Eichler" are unrelated
  quaternion-order files). Searched: WebSearch "Eichler Zagier On the zeros of the Weierstrass p-function formula"; the formula is
  quoted in arXiv:1208.4812 and in Duke-Imamoglu's preprint (math.ucla.edu/~wdduke/preprints/zeros.pdf). I did not search whether
  the S^6 literature already makes this remark.
  Why it matters: it gives mu in closed form, hence Im mu and the gluing units of W numerically (G1a-5), and it is the first step
  towards a number for M (G1a-13 (b)).
- **First assessment**: I checked (9.9)-(9.11) by hand (the constants of mu at g_1 are (1, -1), of an integer a are (2a, -a); at
  g_2 they are (1, 0) and (a, a)); the height value; u_P from X(u) = 0; and that Y = +sqrt2 gives u = -5 + 2 sqrt6. Solid.
  The sign (which of +-P_*, and whether Im mu(p_0) = -log(5 + 2 sqrt6)/(2 pi) = -0.3649) is "fixed by the original period
  values" but not evaluated in the course; reader A1 expected Re mu_0 = 1/2, |Im mu_0| = 0.365.
- **A full check must establish**: Lemma 9.2; the cocycle computation; Thm 11.2; the sign of Im mu(p_0) (numerically from the
  Eichler-Zagier integral: Im mu must pass through -sqrt3/6 at rho and -1/2 at i); the exact form of the Eichler-Zagier formula
  from the original paper.
- **Deserves a full check**: yes (short), mainly for the Eichler-Zagier identification and its numerical use. **Interest**: 4.

### G1a-4
- **Title**: The rational elliptic surface with fibres IV*, III, I_1 done by hand: explicit resolution charts, K_S = -F, the
  height pairing, (nP).O for all n, Hom(t_{6kP}^* M, M) = pi_S^* O_B(k). **Type**: new proof or restatement of known results;
  small computations.
- **Where**: `CG\src\cusp-and-compact-threefold.md` sections 10-12 and Exercises 3, 4 (L601-1031, L1252-1290). 9 Oct 2026.
- **Statement**: (10.17) the fibre at t = 0 is C - E_1 - F_2 - F_1 - E_{2,-}, F_2 - F_3 - E_{2,+} with
  F = C + 2E_1 + 3F_2 + 2F_1 + E_{2,-} + 2F_3 + E_{2,+} (after two blow-ups and the resolution of a c = X^4 by explicit coordinates
  (10.11)-(10.16)); the fibre at t = 1 is two lines tangent to order 2; div(dx ^ dt / y) = -F_infinity. Lemma 11.1: the map
  phi(Q) = Q - O - (Q.O + 1)F + sum Theta_i (C_6^{-1} v_Q)_i + (1/2) d_Q D is additive and
  <Q, R> = 1 + Q.O + R.O - Q.R - v_Q^t C_6^{-1} v_R - (1/2) d_Q d_R. (14.4): for n != 0,
  (nP).O = n^2/12 - 1 + (2/3) eps_3(n) + (1/4) eps_2(n) (eps_m(n) = 0 if m | n, 1 otherwise); values 0, 0, 0, 1, 2, 2 for n = 1..6.
  Lemma 12.1: a base-preserving birational self-map of S is an automorphism (elementary proof). Thm 12.2 = [E26] Lemma 2.1 and
  Cor 2.2 with all steps. Exercise 4: Hom(t_{6kP}^* M, M) = pi_S^* O_B(k) with a section of divisor k F_infinity, corresponding
  to (xi, W) -> (xi - 6k mu, e^{-2 pi i k beta} W).
- **Support**: written proofs; checker `verify_cusp_geometry.py` (122 identities).
- **What it adds**: [E26] cites Shioda's tables and Oguiso-Shioda for all of this; [AC26] does not need it. The formula (14.4)
  and Exercise 4 are easy consequences; Exercise 4 is the algebraic input for the universal covers of the threefolds with
  pi_1 = Z/p (G1a-9), which the course does not mention. Not searched.
- **First assessment**: I checked (14.4) for n = 1..6 and the integrality argument; the resolution was read, not recomputed.
- **A full check must establish**: nothing beyond routine verification. **Deserves a full check**: no. **Interest**: 2.

### G1a-5
- **Title**: The cusp fibre W in explicit terms: two of its three gluing multipliers are units of Z[sqrt6], the third is Engel's u
  up to a constant. **Type**: computation (the combination is mine; the two halves are in the course).
- **Where**: L5 (5.5) (L322-335) and (13.9) (L1135-1144); L5 Exercise 2. Compare A1-4.
- **Statement**: (5.5) the identifications of opposite sides of the hexagon of dP_6 are multiplication by e^{-2 pi i mu_0},
  e^{12 pi i mu_0}, e^{-2 pi i (7 mu_0 + b_0)} in the characters chi^{(0,1)}, chi^{(1,0)}, chi^{(1,1)}. With (13.9),
  e^{2 pi i mu_0} = -(5 + 2 sqrt6)^{+-1}: the first two are -(5 + 2 sqrt6)^{-+1} and (5 + 2 sqrt6)^{+-6} (my substitution).
  Since b_0 = b_0^part + c, the third is -(5 + 2 sqrt6)^{-+7} e^{-2 pi i b_0^part} e^{-2 pi i c}, a constant times u.
  So W_c depends on c only through u = lambda_0 w^2: W_c = W_{c+1}, although X_c and X_{c+1} are not isomorphic.
- **Support**: (5.5) by character evaluation (checker entries "opposite edge exponent 16-18"); (13.9) proved in L5.
- **What it adds**: [AC26] Prop 4.6(ii) and [E26] Prop 2.8 do not give the multipliers. Reader A1 had the value of mu_0 as an
  unverified guess; the course proves it (up to the sign). Not searched.
- **First assessment**: correct as far as the two inputs are; which sign occurs is not decided in the course.
- **A full check must establish**: the sign; whether the triple of multipliers up to the symmetries of the hexagon classifies the
  glued surface, so that u is an invariant of W; which double curve is the fixed curve of Aut^0 = C^*.
- **Deserves a full check**: maybe (short). **Interest**: 3.

### G1a-6
- **Title**: Exact admissible range Im c < -M, and the cusp-free counterexample, in the course version. **Type**: refinement of
  [AC26] (same as A1-2, A1-3).
- **Where**: L4 section 5, Thm 5.1 and the remark after it (L266-346). 9 Oct.
- **Statement**: M = max over B \ {p_0} of D_part exists; Pi is a real isomorphism at every point iff Im c < -M. For
  beta~ = beta + i t the laws hold but D~(R) -> +infinity along t = R -> +infinity (D(R) = -log(1728 R)/(2 pi) + Im b(0) + o(1)).
- **Support**: 15-line proof. **What it adds**: [AC26] Prop 3.15 has the sufficient condition (A1-2). The course adds nothing
  to the workbench statement except the reformulation of G1a-2 (b): 2 pi M = max_t log ||phi_part||_flat. M is not computed.
- **First assessment**: correct. **A full check must establish**: nothing new. **Deserves a full check**: no. **Interest**: 2
  (the open computation is in G1a-13).

### G1a-7
- **Title**: Finite-local package (lessons 1-3): explicit product covers; exact holomorphic order of the normal bundle with an
  explicit smooth trivialization; deck groups and the central attachment kernel with sign; complete parametrization of the local
  period germs; normalization of the base change with all branches. **Type**: refinement of [AC26] / new proofs (grouped).
- **Where**: lessons 1, 2, 3 (files 1.1-1.3). 8-9 Oct.
- **Statement** (items not in [AC26] or [E26] in this form):
  (i) L1 Thm 3.1, 4.1: the covers E_j x F_j -> T_j -> S_j of degrees 3 x 3 and 2 x 4 with moduli kappa_1 = beta_1 + 2 mu_1,
  kappa_2 = beta_2 + 3 mu_2 (A1-5).
  (ii) L1 Thm 5.1: N_j has exact order m_j ([AC26] Main Thm (1) has this) and Theta_j([x, n]) = ([x], n/H_j(x)),
  H_j = exp(-2 pi i eps_j gamma(x)), is an explicit smooth trivialization.
  (iii) L2 Thm 4.1, Cor 4.2: ker(pi_1(punctured bundle) -> pi_1(bundle)) = <G~_j^{m_j} t_{-v_j}>, central, equal to the inverse
  positive loop; P_j = Gamma_j x Z by t_lambda G~_j^k -> (t_lambda G^_j^k, eps_j gamma(lambda)).
  (iv) L3 Thm 1.1: every local period germ at z_j with the laws is given uniquely by three free germs (F_j, H_j, B_j), B_j(0) = 0;
  ord(tau_1 - rho) = 1 and ord(tau_2 - i) = 2 iff F_j(0) != 0.
  (v) L3 Thm 4.1: the torus family over the s-disc is the normalization of N_j x_D Delta, with the branches s = zeta_j^{-a} u, proved
  with explicit idempotents e_a.
- **Support**: complete written proofs; checkers for 1-3. **What it adds**: (i) sharper than [AC26] Thm 5.4(iii), [E26] Cor 3.2;
  (iv) is not in either (it shows what is local and what is global in the period data); (v) is the lemma used in G1a-1 for the
  lift to J'_j, so its proof matters there.
- **First assessment**: routine and careful; I checked several identities ((1.15), (2.4), (5.4) of L3; (4.9) of L1).
- **A full check must establish**: (v) as used in L9 section 6. **Deserves a full check**: no (except (v) inside G1a-1).
  **Interest**: 2.

### G1a-8
- **Title**: Integral dictionary between the [AC26] marking and Engel's bases, with the reversed meridians and the circle term.
  **Type**: new (small) computation / restatement.
- **Where**: L6 section 8, Prop 8.1 and (8.5)-(8.13) (L469-605). 9 Oct.
- **Statement**: With Engel's [T_0]_{B_0} = E, [T_1]_{B_1} = L, C_E, F = C_E L C_E^{-1}, delta_E = -2e_1 - e_2 + 3e_3, psi_E:
  P = [[0,0,0,1],[1,-2,0,2],[1,1,1,-4],[-1,1,0,0]], det P = -1, A_1 P = P E^{-1}, A_2 P = P F^{-1}, M_0 P = P F E,
  P delta_E = delta^, gamma P = psi_E; P e_1 = u^ + w^ - delta^, P e_2 = -2u^ + w^ + delta^, P e_3 = w^, P e_4 = v_1;
  P^{-1} v_1 = e_4, P^{-1} v_2 = -f_4 - delta_E; transported relations x_0^3 = t_{-e_4}, x_1^4 = t_{f_4 + delta_E};
  12 psi_E(-e_4/3 + (f_4 + delta_E)/4) = -1; the cusp images correspond: P E^{-1}(e_1 - e_3) = -w^, P E^{-1}(e_3 - e_2) = delta^ - 2w^.
- **Support**: direct matrix checks; `verify_integral_monodromy.py`. I re-ran the identities in my own script
  (`work\scratch\G1a\check1.py`): all true, including that Engel's matrices as printed in [E26] Thm 5.1 are the ones used.
- **What it adds**: neither paper compares the two markings. The term delta_E in P^{-1} v_2 means: under this P, the [AC26] twist
  vectors correspond to (3a_0, 4a_1) = (e_4, -(f_4 + delta_E)), while Engel's sample choice is (e_4, -f_4). The course keeps the
  term "visible" but does not say what it means. By G1a-1 it is exactly the order-two class; by the remark in G1a-2 it is not a
  discrepancy between the papers, because P is only determined up to the centralizer {+-(I + bE)} and e_4 only modulo delta
  (composing P with the centralizer element e_4 -> e_4 + delta_E of Engel's lattice gives P'^{-1} v_1 = e_4 - delta_E,
  P'^{-1} v_2 = -f_4: the delta-term moves to the first vector, where its class in Lambda^{A_1}/N_1 Lambda is zero).
- **First assessment**: correct. **A full check must establish**: Engel's sign conventions in his Prop 6.1 (I did not read his
  section 6 line by line). **Deserves a full check**: maybe, as part of G1a-2. **Interest**: 3.

### G1a-9
- **Title**: Other free affine fillings: X_{r_1, r_2} with pi_1 = Z/|4 r_1 + 3 r_2|; every p prime to 6 occurs. **Type**:
  expository only (contained in [AC26] section 7), plus an open question that the course leaves.
- **Where**: L6 Exercises 1, 2 (L609-672). 9 Oct.
- **Statement**: G(l_0, l_1, l_2) = <c, x, y | c central, xy = c^{l_0}, x^3 = c^{l_1}, y^4 = c^{l_2}> = Z/p,
  p = 12 l_0 - 4 l_1 - 3 l_2, with x = c^k, k = 4 l_0 - l_1 - l_2. For gcd(r_1, 3) = gcd(r_2, 4) = 1 and twist vectors
  w_1 = r_1 v_1, w_2 = -r_2 v_2 the same construction gives a compact complex threefold with pi_1 = Z/|4 r_1 + 3 r_2|; the
  integer is prime to 6 and every such integer occurs. "It makes no homology or smooth-sphere claim for the additional spaces."
- **Support**: the exercise solution. **What it adds**: nothing over [AC26]: Thm 7.17 and Thm 7.22 treat every admissible pair
  (v_1, v_2) (including delta^-components) and every l_0, with H_*(X;Z) = (Z, Z/p, Z/p, Z/p, Z/p, 0, Z), e(X) = 2; [E26] Prop 6.1
  has the same group. The README sentence "actual additional free affine fillings and their cyclic groups" reads as if this were
  an addition. The course identifies none of these 6-manifolds and says nothing about their universal covers.
- **First assessment**: correct and elementary. My remarks (not in the course): the universal cover X~_p of a member with
  |p| > 1 is a simply connected compact complex threefold fibred over P^1 with general fibre C^2/Pi Lambda',
  Lambda' = {gamma = 0 mod p} (so it is the same construction with the lift of t_{6pP}, L5 Exercise 4), multiple fibres of
  multiplicity 3 and 4, a cusp fibre with |p| components (a cycle of glued dP_6), e = 2|p|, and a free Z/p-action. Its homology
  and diffeomorphism type are not computed anywhere I read; they answer in part the question of [E26] Remark 8.5 ("It is unclear
  what class of 6-manifolds can arise").
- **A full check must establish**: nothing for the exercise. For the question: H_*(X~_p), the cubic form and p_1.
- **Deserves a full check**: no for the exercise; the question is listed in G1a-13 (e). **Interest**: 2.

### G1a-10
- **Title**: Canonical divisor, direct images, anticanonical ring C[U, V], and f = |-2K_X|, with complete proofs.
  **Type**: refinement of [AC26] (same results as B-8, course version).
- **Where**: lesson 8 (file 1.7). 9 Oct.
- **Statement**: omega_X = O_X(-2 S_2) (via ev: f^* f_* omega_{X/B} -> omega_{X/B} with divisor 2 S_2, f_* omega_{X/B} = O_B(p_0),
  omega_B = O_B(-2 p_2), multiplication by 1/(t-1)); f_* O_X(k S_2) = O_B(floor(k/4) p_2) for every integer k;
  h^0(omega_X^{-m}) = floor(m/2) + 1, h^0(omega_X^m) = 0 (m > 0); R(X, -K_X) = C[U, V], deg U = 1, deg V = 2, u^2 = f^* sigma_{p_2};
  |-2K_X| is base-point free and equals beta o f; |-K_X| = {2 S_2}; fixed divisor of |-(2r+1)K_X| is exactly 2 S_2; graded
  automorphisms U -> cU, V -> aV + bU^2; the members of the pencil are 4 S_2, W, 3 S_1 and the smooth fibres. Cor 7.2: every
  biholomorphism between two threefolds of the construction commutes with f and is the identity on the base.
- **Support**: about 400 lines; `verify_canonical_ring.py`. **What it adds**: over B-8, the course writes out f_* O_X = O_B
  (Lemma 1.1), the correcting units phi_j, the proof for all k, and Cor 7.2 as a separate statement. [AC26] Prop 9.11 has K_X;
  [E26] Remark 8.1 gets uniqueness of the map from a(X) = 1.
- **First assessment**: correct at reading; k_j = m_j - 1 - a_j = (0, 2) agrees with [AC26] Lemma 9.10 (per reader B).
  Cor 7.2 holds for "two threefolds of this construction"; for the threefolds with other twist vectors the characters are the
  same (the translation does not enter (2.6)), so the corollary should extend to them; the course does not say so.
- **A full check must establish**: Lemma 1.1 at the cusp; (2.6)-(2.13); Thm 5.1. **Deserves a full check**: maybe (it is the
  input of G1a-1). **Interest**: 3.

### G1a-11
- **Title**: The proper family over c and the non-zero Kodaira-Spencer class, course version. **Type**: new result (same as B-6).
- **Where**: lesson 9 sections 1-4 (L23-332); Exercises 9.1, 9.3, 9.4. 11 Oct.
- **Statement**: as in B-6: for a disc Q with closure in P, F: X_Q -> B x Q and pi: X_Q -> Q are proper, pi a submersion;
  nu_delta = delta P/(2iD + delta), P = [[0,0],[-a,1]], a = Im mu/Im tau; KS_F(d/dc) = -(1/(2iD)) d/dzeta_2 (x)
  (d zeta^-_2 - a d zeta^-_1) != 0; omega_{X_Q/Q}^{-2} = F^* pr_B^* O_B(p_2); H^0(X_A, L_A) = A s_0 + A s_1 over A = C[eps]/(eps^2);
  the critical-value sections are the three constant sections; hence KS_X(d/dc) != 0 and h^1(X, T_X) >= 1.
  Added in the course: the composition law of the marked maps with D replaced by D + Im delta_1 (Ex. 9.1); the class in the
  u-coordinate (Ex. 9.3); the example t = s^m + eps alpha showing why the scheme-theoretic critical value is needed (Ex. 9.4).
- **Support**: about 300 lines; checker (Beltrami identities). **What it adds**: see B-6. Nothing on h^1 beyond >= 1.
- **First assessment**: as B; I read the proof and found it coherent. The uniform cusp estimate (1.7)-(1.9) is the new
  analytic point relative to lesson 5.
- **A full check must establish**: as B-6. **Deserves a full check**: maybe. **Interest**: 3.

### G1a-12
- **Title**: The images pi_j^* H^q(S_j; Z) by explicit line-bundle descent and by a dual-lattice test. **Type**: new proof of a
  known result ([AC26] Lemma A.4).
- **Where**: the two companions (1.9). 11 Oct.
- **Statement**: pi_1^* H^2(S_1) = Z h_1 + Z q; pi_2^* H^2(S_2) = {a h_2 + b q : a = b (2)}; a class a h_2 + b q descends iff the
  integer equation l N_2 = -kappa_2 is solvable iff a + 3b is even; explicit lifted actions (2.6) with constants (3.5);
  downstairs form [[0,1],[1,4]] on S_2. Degree 3: L_1^3 = Z b + Z c_1, L_2^3 = Z(2b) + Z c_2. General test (4.2):
  L^r = {x in V^r : <x u y, [F]> in m Z for all y in L^{n-r}} when the groups are torsion-free.
- **Support**: complete proofs; two checkers. **What it adds**: [AC26] Lemma A.4 has the same lattices and indices. The descent
  proof shows the same mechanism as G1a-1: the obstruction is a norm equation for N_2 and has order two at the order-four point
  only. Not searched.
- **First assessment**: plausible; not recomputed. **A full check must establish**: (2.9) and (3.4). **Deserves a full check**:
  no. **Interest**: 2.

### G1a-13
- **Title**: Open questions that the course leaves or isolates. **Type**: open question isolated.
- **Where / Statement**:
  (a) *All discrete choices.* Classify X(c; w_1, w_2) for all admissible twist vectors w_j in Lambda^{A_j} (and the cusp twist
  l_0 of [AC26]). The course treats only (v_1, v_2). My sketch, by the method of L9 sections 6-7 (not in the course, not
  verified): a map X(c; w) -> X(c'; w') with linear part I needs l_j with N_j l_j = w_j - (I + nE) w'_j and
  l_0 = -M_0(l_1 + A_1 l_2) in Lambda_tor; this is solvable iff p = p' and, writing w_2 = r_2 eps' + k_2 delta^,
  c' - c = k_2 - k'_2 mod 2 (the delta^-part of w_1 is irrelevant). My script confirms the lattice part in examples:
  (r_1, r_2) = (1, -1) -> (-2, 3) solvable for n = 0 and not for n = 1; a change of k_2 by 1 is solvable exactly for odd n; a
  change of k_1 by 5 for n = 0; (1, -1) -> (4, -1) (different p) not solvable. If the analytic part goes through as in L9
  section 7 (same sheaf V), then the isomorphism class depends only on p and w (with the case of linear part -I, which sends
  (w_1, w_2) to (-w_1, -w_2) and p to -p, still to be worked out), and in particular **every S^6 member of the
  whole discrete family of [AC26] and [E26] is biholomorphic to exactly one X_w**: the different admissible (a_0, a_1) give no
  new complex structures. This would be a clean complement to G1a-1. It also needs L8 Cor 7.2 for the other twist vectors
  (see Doubts 7) and the cusp twist l_0 of [AC26], which I did not look at.
  (b) *The number M.* Value of M and the point where D_part is maximal; equivalently the radius of the admissible disc. An
  intrinsic form: the family exists exactly for |q(Alb(S_1))| < R_1 with R_1 = e^{-2 pi (M - D_part(z_1))} <= 1 (and similarly
  for Alb(S_2)); is R_1 = 1? D is superharmonic on the base (Im beta is harmonic and (Im mu)^2/Im tau is plurisubharmonic in
  (mu, tau)), so there is no maximum principle to locate the maximum. With mu from Eichler-Zagier (G1a-3) and beta from
  d beta d tau - 6 d mu^2 = an invariant quadratic differential, or from an explicit theta-function formula for the
  linearization, M is computable. Not done anywhere I read.
  (c) *h^1(T_X), h^2(T_X), completeness.* Only h^1 >= 1. Reader B's remark h^2 = h^1 stands. Is the w-family the Kuranishi
  family (h^1 = 1)?
  (d) *The limit w -> 0* ([E26] Conjecture 8.2) and *the boundary |w| = e^{-pi M}*: not addressed.
  (e) *The threefolds with |p| > 1 and their universal covers* (G1a-9): diffeomorphism types.
  (f) *Aut(X_c).* The necessity argument of L9 (take c' = c) shows that every automorphism is a translation by a section with
  linear part I; the sections are H^0(B, V) = C e modulo periods, plus possibly a discrete part. My sketch: cocycles with
  l_j in (I - A_j) Lambda modulo coboundaries are k (w^ + u^ - delta^) at g_2, with l_0 = -k(u^ - w^), which is not in Lambda_tor
  unless k = 0; so Aut(X_c) = C^* exactly (connected). [AC26] has Aut^0 = C^*. Not stated in the course.
  (g) *lambda_0 and the sign in (13.9)*: which of +-P_* is the period section, and the constant relating a natural geometric
  normalization to beta^part.
- **Deserves a full check**: (a) yes, it is probably a short theorem with the tools already in lesson 9; (b) yes as a
  computation; (f) maybe. **Interest**: (a) 4-5, (b) 3-4, (c) 4, (d) 3, (e) 3-4, (f) 3.

---

## 3. Doubts and errors

1. README (and `course.json` result CG-S6-06-EXTENSIONS: "actual additional free affine fillings") presents L6 Exercise 2 as an
   addition. [AC26] section 5 (after Prop 5.6) and section 7 (Thm 7.17, Thm 7.22) already treat every admissible pair and give
   the homology as well; the lesson's Sources paragraph does not cite them for this exercise. An attribution gap, not an error.
2. L4 Exercise 9.1 computes with "M = 7/3". This is a made-up value for the exercise; M is not known. A reader could take it
   for the value.
3. L4 Exercise 9.1 says that constants with the same u give the same unmarked lattices and "the quotient parameter retains the
   phase modulo this exact integral change of marking". True for the middle family, but lesson 9 shows that the threefolds for
   c and c + 1 are different; lesson 4 gives no forward reference at this point (L4 Thm 7.1 says "the only kernel of c -> u is Z").
4. L5 (13.9) leaves the sign open (u_P = -5 +- 2 sqrt6) although the text says the sign of P "is fixed by the original period
   values"; the value of Im mu(p_0) is not determined in the course. Not an error.
5. L5 Thm 13.1 calls (13.13)-(13.14) "the complete parameter dictionary", but lambda_0 is "obtained by evaluating ... on any
   one ordinary fibre" and never evaluated; there is no canonical phi_ref, so the radius |lambda_0| e^{-2 pi M} has no intrinsic
   meaning without a normalization (the intrinsic forms are in G1a-13 (b)).
6. L9 (8.2) and Figure 1 speak of "the complex parameter space for the isomorphism classes". What is proved is a bijection of
   sets and a holomorphic family over P with the coherent maps (7.16); the descended family over the w-disc is not written down,
   and no universal property is claimed (the lesson says so).
7. L9 Thm 8.1 is stated for "X_c" of the retained family, and L8 Cor 7.2 for "two threefolds of this construction". The proof
   of the corollary uses the characters computed with the retained data; it would apply to other twist vectors too, but that
   is not stated, so the theorem does not yet cover them (G1a-13 (a)).
8. Status wording: every result in `course.json` has `complete_written_proof_with_author_self_check`; the checkers verify the
   displayed algebra only (their JSON says so). For lesson 9 this means that the three analytic steps of the sufficiency proof
   (H^1(B, V) = 0, the extension at the cusp, the lift to the normalization) rest on the written text alone.
9. Notation hazards for a checker: zeta_j is both a root of unity and a fibre coordinate (L8 says so); in L9, "m" is Im mu and
   m_j the orders, "a" is both Im mu/Im tau and the sign +-1 of the linear part and the global section of H_n, "delta" is a
   covector, a parameter difference c - c_*, and delta^ a lattice vector; in L5, u is the Tate coordinate, a chart variable
   (u = t - 1) and (elsewhere) Engel's parameter; M is max D_part, the line bundle O(P - O), and M_C, M_0 are other objects.
10. Not mathematics: the Sources sections of lessons 1-6, 8, 9 link to zenodo.org/records/22678442. If these lessons are
    published, the links fall under the later instruction that bans Zenodo links.

I found no mathematical error in the lessons I read.

---

## 4. Not read

- Lessons 7, 10, 11 and their companions (not in my assignment), except the two companions named in it.
- The `.html` readers, `assets\`, `downloads\`, `rebuild_course.py`, `rebuild_reader.py`, the `draw_*.py` scripts.
- `provenance.json` and `series.json`: structure and the entries for my lessons only.
- Checkers: `verify_global_periods.py` and `verify_period_deformation.py` were read in full; for the other eight I read the
  result JSON (check names, scope, hash) but not the code line by line. No checker was run (they write into the course folder).
- [E26] sections 6-7 (L700-1160 of the text file) were not read line by line; [AC26] only the passages listed in 1.12.
- Literature: Viaclovsky arXiv:2610.39102 and Yang arXiv:2609.29666 were not fetched again (reader B's summaries used); the
  original Eichler-Zagier paper was not opened (the formula is taken from two papers that quote it).
