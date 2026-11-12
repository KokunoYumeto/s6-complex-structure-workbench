# G1b notes: CG-S6 lesson 10 "Non-normal fibres and vanishing" and its analytic companions

Reader G1b, Claude Fable 5.2, 12 Nov 2026. Read only; this is the only file written (plus one scratch script,
`work\scratch\G1b\check1.py`). "The lesson" means `courses\CG-S6\src\non-normal-fibres-and-vanishing.md`.
All paths below are under `C:\Users\user\Documents\math\research\s6_recent_results_main\` unless they start
with a drive letter.

Sources of the lesson, as the lesson itself states them (this matters for every novelty judgement below):

- [AC26] section 10 (Lemmas 10.2-10.3, Remark 10.4, Theorem 10.5, Corollary 10.6, Lemma 10.7, Proposition 10.8).
- [N] "The singular-fibre vanishing step: an independent audit and proper test family", dated 1 Sep 2026, drafted
  with "OpenAI Codex gpt-5.6-sol, Ultra" (its own disclosure). A local copy of its TeX is
  `mathematical_consolidation\nested_source_blobs\aca0913df424f72b0efc94546498f1f427786191628503ff56208f4153060abb.tex`
  (39 KB, 948 lines; same blob in `source_text_blobs\`). Numbering there: Lemma 4.2 (gluing bundle), Lemma 4.3
  (extending choice), Theorem 4.4 (failure of the printed endpoint implication), Remark 4.5 (scope), Lemma 5.1
  (generic endpoint vanishing), Theorem 5.2 (derived global CDP criterion), Corollary 5.3 (relative hypothesis),
  Proposition 6.1 (crossing and multiple-fibre modules), Remark 6.2.
- [R] "The S6 record ...", Claude Opus 5.5, v3, 28 Sep 2026, Section 5 (source labels prop:normal, prop:kernel,
  prop:sharp, thm:derived, prop:torsion). NOT present in the local workspace (only cited; provenance.json entry
  `S6-REVIEW-Z23003415-SECTION5` says the lesson author read all of its Section 5). I could not compare [R]'s
  wording; I rely on the lesson's and the status note's descriptions of it.
- The September workbench `canonical_S6_snapshot\supporting_materials\workbench\research\cdp_program.tex`
  (1,665 lines, 29 Sep 2026).

The lesson is explicit that most of its sheaf results are "existing results, independently calculated in this
lesson; no priority is claimed" (line 481, 734, 1256). So the lesson is the latest and most complete WRITE-UP;
the new mathematics over [AC26] was found in [N] (1 Sep), the September workbench and [R] (28 Sep). What the
lesson itself adds is listed per candidate.

## 1. Reading notes

### 1.1 `courses\CG-S6\README.md` (11.6 KB, 11 Oct 2026) and `course.json` (69 KB, 11 Oct)

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

### 1.2 `src\non-normal-fibres-and-vanishing.md` (132 KB, 2,245 lines, file date 11 Oct 2026) - read in full

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

### 1.3 `src\proper-base-change-over-a-curve.md` (28 KB, 442 lines, 11 Oct) - read in full

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

### 1.4 `src\general-proper-flat-surface-base-change.md` (14 KB, 182 lines, 11 Oct) - read in full

Theorem 1.1: f : X -> B proper flat map of complex spaces, B a Riemann surface, every full fibre of pure dimension
two, E a vector bundle: R^q f_*E = 0 (q > 2) and the canonical map (R^2 f_*E)_b (x) k(b) -> H^2(X_b, E_b) is an
isomorphism; no smoothness/compactness of X, no reducedness of fibres. Proof = (finite free complex representing
Rf_*E, from the companions NS, BT, RP, FC) + (coherent cohomology of a compact space of dimension <= n vanishes above
n, from QN, WL, BK, CL, QG) + the algebra of §5. §6 lists the cross-course prerequisites (eleven units of another
course, "complex-analytic-spaces-and-coherent-sheaves" and "elliptic-operators-and-boundary-problems", pinned at
commit da43414 of the programme's course repository; their texts are NOT in this folder). Credits Demailly,
"Complex Analytic and Differential Geometry" (author edition 21 June 2012), Ch. VI-VII and IX; "does not ... claim
novelty for the classical results".

### 1.5 `src\tangent-index-with-torsion-line-bundles.md` (37 KB, 491 lines, 9 Oct) - read in full

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

### 1.6 The nine `src\general-analytic-*.md` companions (all dated 11 Oct 2026, GPT-6 Astra, Ultra)

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

### 1.7 `checks\verify_conormal_torsion.py` (10.6 KB) and `checks\CONORMAL_TORSION_CHECKS.json` (61 checks passed)

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

### 1.8 Comparison files

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

### 1.9 CDP20 (arXiv:1904.11179v2, 20 May 2019) and CDP98 (arXiv:math/9607215v1), fetched and read as PDF pages

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

### 1.10 Answers to the four questions of the assignment (details in the candidates)

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

## 2. Candidates

### G1b-1
- **Title**: Exact kernel of Omega^1_X|_S -> Omega^1_S/torsion on a reduced normal-crossings divisor, and the criterion
  for the CDP20 p. 692 reduction. **Type**: refinement of [AC26] (Lemma 10.3) / correction of the literature.
- **Where**: lesson §§1-3, l. 17-268 (Theorem 2.1, (1.8), (3.2), (3.6)-(3.8)); result id CG-S6-10-TORSION; file date
  11 Oct 2026. Earlier forms: [N] Props "missing filtration", "exact global-section criterion" (1 Sep);
  cdp_program.tex l. 52-111; [R] prop:kernel, prop:sharp (28 Sep, not seen).
- **Statement**: Let S be a reduced effective Cartier divisor with normal crossings (local equation u x, u xy or
  u xyz) in a smooth complex threefold X, eta : S~ -> S its normalization, N^* = I/I^2, T_S = ker(Omega^1_S -> j_* Omega^1_{S_reg}),
  tilde-Omega^1_S = Omega^1_S/T_S, K_S = ker(Omega^1_X|_S -> tilde-Omega^1_S). Then there is a natural isomorphism
  Phi : eta_* eta^* N^* -> K_S under which N^* -> K_S is the inclusion N^* -> eta_* eta^* N^*; hence
  T_S = (eta_* O_{S~}/O_S) (x) N^*, and for every line bundle A on S the sequence 0 -> N^* (x) A -> K_S (x) A -> T_S (x) A -> 0
  is 0 -> N^* (x) A -> eta_* eta^*(N^* (x) A) -> T_S (x) A -> 0. Consequences: (i) H^0(S~, eta^*(N^* (x) A)) injects into
  H^0(S, Omega^1_X|_S (x) A), with equality if H^0(S, tilde-Omega^1_S (x) A) = 0; so, given CDP's statement (11),
  H^0(S, Omega^1_X|_S (x) A) = 0 if and only if H^0(S~, eta^*(N^* (x) A)) = 0. (ii) For a full reduced connected compact
  fibre S = f^{-1}(b) (N^* trivial): if eta^*A is trivial and H^0(S~, Omega^1_{S~}) = 0 then
  dim H^0(S, Omega^1_X|_S (x) A) = r = number of connected components of S~, and if moreover A is nontrivial then
  H^0(S, A) = 0 and dim ker(delta_A) = r.
- **Support**: written proof, about 4 pages: local computation in C{x,y,z}/(xy) and /(xyz) ((2.5)-(2.8)), gluing by
  the unit rule (1.3). Finite-degree kernel/image check in the checker for 2 and 3 branches, degrees 0-6. Status:
  `complete_written_argument_author_self_checked`; the workbench marks its versions \Verified.
- **What it adds**: over [AC26]: Lemma 10.3 constructs one section under eta^*A trivial and shows nonvanishing;
  this gives the whole kernel sheaf, an if-and-only-if criterion, and exact dimensions. Over [E26]: nothing
  comparable (Engel omits CDP). Literature: the local fact that the torsion of Omega^1 of a normal-crossings variety
  is a line bundle on the double locus built from the conormal bundles is classical (R. Friedman, Global smoothings
  of varieties with normal crossings, Ann. of Math. 1983, §1, from memory; my web search did not return the
  passage). Its use as the exact obstruction in CDP20 §7 is, as far as I found, only in [AC26]/[N]/[R]. Searched:
  "Campana Demailly Peternell corrigendum ... non-normal fibre conormal sequence torsion" (only the corrigendum
  itself and Demailly's own copies came back).
- **First assessment**: solid. I redid the double-point computation by hand; the triple-point one is the same
  pattern. The only subtle point is that Phi is defined into restricted ambient forms, not into Omega^1_S (the lesson
  stresses this, l. 211).
- **A full check must establish**: (2.5)-(2.8) including the claim that the kernel of Omega^1_S -> eta_* Omega^1_{S~} is
  exactly T_S; the gluing of Phi; that (3.5) is injective; the statement (i) above with the minimal hypothesis
  (the lesson states (3.6) under the stronger (3.4)); agreement with [R] Prop. 5.5 as published.
- **Deserves a full check**: yes - it is the precise form of the correction to CDP20 and is short.
  **Interest**: 4.

### G1b-2
- **Title**: A proper family over a disc, central fibre (nodal cubic) x P^1, with an infinite-order twist that
  extends to the total space, for which both endpoint groups vanish and the ambient group is exactly C.
  **Type**: correction of the literature (counterexample to the inference at CDP20 p. 692), independent of S6.
- **Where**: lesson §§4-6 and Exercise 1, l. 271-481, 1398-1440; ids CG-S6-10-TEST; [N] Prop. 4.1, Lemmas 4.2-4.3,
  Theorem 4.4, Remark 4.5 (1 Sep 2026); cdp_program.tex l. 276-354.
- **Statement**: C = {([x:y:z],t) in P^2 x Delta_eps : y^2 z = x^2(x+z) + t z^3}, 0 < eps < 4/27, X = C x P^1,
  g = t. Then X is smooth, g proper, S = g^{-1}(0) = C_0 x P^1 is reduced, irreducible, normal crossings (t = U_0 V_0 with
  U_0 = y - x sqrt(1+x), V_0 = y + x sqrt(1+x)), normalization P^1 x P^1 via r -> (r^2 - 1, r(r^2 - 1)), node branches
  r = 1, -1. For lambda in C^* let A_lambda on C_0 be the trivial bundle on the normalization glued by c(p) = lambda c(q).
  For points with parameters a, b the bundle O_{C_0}(P_a - P_b) is A_lambda with lambda = (1+b)(1-a)/((1+a)(1-b)).
  With P(t), Q(t) the sections through r = 0 and r = 1/3, the bundle pr_C^* O_C(P - Q) on X restricts to
  A = pr_1^* A_2 on S, and
  H^0(S, N^*_{S/X} (x) A) = 0, H^0(S, tilde-Omega^1_S (x) A) = 0, H^0(S, Omega^1_X|_S (x) A) = C,
  generated by s_e with torsion image -(2/3) tau (x) s_D, tau = [V_0 dU_0] = -[U_0 dV_0]; H^0(T_S (x) A) = C and
  delta_A = 0. Exercise 1: every A_lambda, lambda in C^*, extends to the total space after shrinking the disc
  (b = (lambda - 1)/(lambda + 1); lambda = -1 via the point at infinity), and dim H^0(S, Omega^1_X|_S (x) pr_1^* A_lambda) = 1
  for every lambda.
- **Support**: complete elementary proofs (about 5 pages); checker items "whole homogeneous normalization" through
  "nonzero torsion coefficient" and "arbitrary gluing scalar recovered". I rechecked (5.5), (5.6), (5.9), (6.7) and
  the smoothness and node computations by hand.
- **What it adds**: over [AC26]: not there ([AC26] shows the failure only at W, which needs the whole
  construction). Over [E26]: not there. Over [N]: exact dimension, the explicit generator, all lambda. Over the
  September workbench: the extension of the twist to the total space (the workbench disclaimed it). Literature:
  nothing found (same search as G1b-1).
- **First assessment**: correct as far as I checked; it is a statement about a sheaf-level implication, not a
  counterexample to a theorem (the lesson says this at l. 479). A reader could object that CDP's L is a general
  member of a family on a compact X; the extension to the total space answers the local form of that objection.
- **A full check must establish**: Theorem 4.1 (smoothness at z = 0, the only singular fibre in the disc);
  the gluing-scalar formula and its direction; H^0(P^1 x P^1, Omega^1) = 0; that the Serre-dual twist of CDP is of
  this form ([N] Remark 4.5); Exercise 1 for lambda = -1.
- **Deserves a full check**: yes - cheap, self-contained, and the natural thing to show a specialist first.
  **Interest**: 4.

### G1b-3
- **Title**: The conditional theorem that survives, in Betti-number form, and nonvanishing of H^2(Y, T_Y (x) L) for
  every L when b_1 = b_2 = b_3 = 0. **Type**: refinement of [AC26] (Theorem 10.5(c), §10.6) / correct restatement of
  the valid core of CDP98-CDP20.
- **Where**: lesson §11.3-11.5 and Exercise 4, l. 1160-1256, 1488-1505; id CG-S6-10-INDEX; [N] Lemma 5.1, Theorem
  5.2, Corollary 5.3; cdp_program.tex `lem:cdp-generic-endpoints`, `thm:corrected-cdp-global`,
  `cor:corrected-cdp-relative` (l. 1368-1500); [R] thm:derived (not seen).
- **Statement**: Let Y be a compact connected complex threefold with b_1(Y) = b_2(Y) = 0 carrying a nonzero effective
  divisor D. Then (i) chi(Y, T_Y (x) L) = 1 - b_3(Y)/2 for every L in Pic(Y), b_3 even; (ii) on each component of
  Pic(Y) (a translate of H^1(Y,O_Y)) there is a dense open set where h^0 = h^3 = 0, hence
  h^2(Y, T_Y (x) L) = h^1(Y, T_Y (x) L) + 1 - b_3/2 there; (iii) if H^2(Y, T_Y (x) L_0) = 0 for one L_0 then b_3 >= 2, i.e.
  c_3(Y) <= 0; (iv) if b_3 = 0 then H^2(Y, T_Y (x) L) != 0 for EVERY L, and R^2 g_*(T_Y (x) L) != 0 for every L and every
  surjective holomorphic g : Y -> C onto a compact curve. For the S6 threefold X: chi(X, T_X (x) L) = 1 and
  H^2(X, T_X (x) L) != 0 for every L in Pic(X).
- **Support**: written proof: (11.8) (a section divisible by every power of the equation of D vanishes), Serre
  duality for h^3, the explicit family (11.10) on Pic^0 = C^q and semicontinuity (from the smooth-duality companion),
  the index value (tangent-index companion or Riemann-Roch), closedness of {h^2 >= 1}. (11.14) by the Leray spectral
  sequence and Serre vanishing on the curve.
- **What it adds**: over [AC26]: Theorem 10.5(c) gives H^2 != 0 only for general M; §10.6 has the generic endpoint
  vanishing but stops at "h^2 >= ... > 0 for general M". Here: every L, a proof that does not use the fibre W at all,
  and a statement for any threefold with b_1 = b_2 = b_3 = 0 and a divisor - for instance any complex structure on S^6
  (or on a rational homology 6-sphere) with a(X) >= 1 or with any divisor has H^2(X, T_X (x) L) != 0 for all L, in
  particular H^2(X, T_X) != 0. Over [E26]: not there. Literature: the mechanism is CDP98's own (introduction, quoted
  in 1.9, and CDP98 Prop. 1.1, Cor. 1.3); the conditional formulation and the "every L" conclusion follow from it
  in a few lines. I did not find it stated, but would not call it new beyond a correct reformulation.
- **First assessment**: correct on reading; I checked the logic (density + closedness) and the index polynomial.
  One hypothesis to keep in view: Pic^0(Y) = H^1(Y,O_Y) uses H^1(Y;Z) = 0, which follows from b_1 = 0.
- **A full check must establish**: (11.8) for non-reduced D; that O(rD) lies in Pic^0 for r the order of c_1(O(D));
  analyticity of the jump loci for the family (11.10) tensored with a fixed L_0; the Leray argument for (11.14).
- **Deserves a full check**: yes - short, and it is the statement to quote as "what remains true".
  **Interest**: 3.

### G1b-4
- **Title**: At the cusp fibre W the Serre-dual group is exactly one-dimensional for every L; the stalk of
  R^2 f_*(T_X (x) L) at p_0 is cyclic; its length is left open. **Type**: refinement of [AC26] (Theorem 10.5(a)) +
  open question isolated.
- **Where**: lesson §9, §10.4, Exercise 3; l. 783-928, 1038-1060, 1472-1486; ids CG-S6-10-CUSP, -DUALITY;
  proper-base-change companion (6.6); [R] Prop. 5.5(b) per the status note.
- **Statement**: For every L in Pic(X), with A = L^v|_W (x) omega_W: eta^* i^* L is trivial on dP_6,
  H^0(W, tilde-Omega^1_W (x) A) = 0, H^0(W, Omega^1_X|_W (x) A) = H^0(dP_6, eta^*(L^v (x) omega_X)|_W) = C (canonical first
  isomorphism), hence dim H^2(W, (T_X (x) L)|_W) = 1 and dim (R^2 f_*(T_X (x) L))_{p_0} (x) C(p_0) = 1. So
  M = (R^2 f_*(T_X (x) L))_{p_0} is isomorphic to A = C{t} or to A/(t^r) for some r >= 1; "neither local freeness nor a
  torsion length can be read from (10.12) alone".
- **Support**: §9 (H^1(dP_6,O) = 0 and H^0(dP_6, Omega^1) = 0 proved from scratch), Theorem 2.1, the duality (10.6), the
  base change (10.10).
- **What it adds**: over [AC26]: "!= 0" becomes "= 1"; duality and base change proved instead of cited ([RR, RRV],
  [BaSt]); the base tangent-line factor in omega_W = omega_X|_W (x) T_{p_0}B kept explicit. Open question (mine, read off
  Exercise 3 and [AC26] §10.6): for general M one has (by [AC26] Step 5 and §10.6) R^2 f_*(T_X (x) M) and
  R^1 f_*(T_X (x) M) of finite support, f_* = 0, so length(R^2 f_*) - length(R^1 f_*) = chi = 1. Is
  (h^0,h^1,h^2,h^3)(X, T_X (x) M) = (0,0,1,0) for general M, i.e. R^1 = 0 and R^2 = C at p_0 (r = 1, nothing at p_1, p_2)?
  And what are the groups at M = O_X (deformations and obstructions of X; lesson 9 shows H^1(X,T_X) != 0)?
- **First assessment**: the dimension statement follows at once from G1b-1 and the two vanishings on dP_6; solid
  given H^2(X;Z) = 0 (or the route G1b-9/10).
- **A full check must establish**: that eta^*(i^*B) trivial is applied to the bundle L^v (x) omega_X (x) O_X(W); the
  identification (9.16); (10.6) and (10.10) (see G1b-7); for the open question, the multiple fibres 3S_1, 4S_2
  need the layers of the non-reduced fibre.
- **Deserves a full check**: maybe - the result is a corollary; the open question is worth one computation.
  **Interest**: 3.

### G1b-5
- **Title**: a(X) = 1 and M(X) = f^* C(t) in a few lines from b_2 = 0: every effective divisor is vertical.
  **Type**: new proof of a result of [AC26] (Main Theorem (3), Prop. 9.7); a general lemma.
- **Where**: lesson §8, l. 736-781; id CG-S6-10-REDUCTION.
- **Statement**: Let f : X -> P^1 be the S6 threefold (used: H^2(X;Z) = 0, smooth fibres are complex tori,
  f_* O_X = O_{P^1}). An effective divisor D with a component dominating the base would restrict to a nonzero
  effective divisor on a torus fibre F with integral of omega_F over D|_F positive, while
  that integral equals <c_1(O_X(D)|_F) u [omega_F], [F]> = 0 because c_1(O_X(D)) lies in H^2(X;Z) = 0. Hence all divisors are
  vertical, the polar divisor of any meromorphic h lies in finitely many fibres, (f^*t)^N h is holomorphic near a
  fibre and equals f^* b_U; so f^* : C(P^1) -> M(X) is an isomorphism. The argument works for any compact complex
  manifold with b_2 = 0 and a surjection with connected fibres onto a curve whose general fibre is Kähler.
- **Support**: complete proof in the lesson (about one page).
- **What it adds**: over [AC26]: Prop. 9.7 uses the period computation of NS(F_b) for very general b (Prop. 9.5,
  a(F_b) = 0) and Lemma 9.6; this proof needs neither. It does not give [AC26] Cor. 9.8 (very general fibre has
  a = 0, NS = Z eta). Over [E26]: the status note says [AC26] and [E26, Remark 8.1] "state" a = 1 for the family; this
  lemma proves a(X) = 1 for every member X(u, a_0, a_1) at once, since each has b_2 = 0 and torus fibres. Literature:
  not searched; the argument is of a standard kind and may be folklore.
- **First assessment**: correct on reading (D|_F is a divisor for F not contained in D; a torsion class restricts
  to a torsion class; the removable-singularity step is spelled out).
- **A full check must establish**: f_* O_X = O (lesson 8) for all members; that the general fibre is a torus for
  Engel's family; the cycle-class identity (8.2).
- **Deserves a full check**: maybe - short; useful as a simplification of the Main Theorem.
  **Interest**: 3.

### G1b-6
- **Title**: The tangent index with torsion twists, proved without the index theorem.
  **Type**: new proof of a known result.
- **Where**: `src\tangent-index-with-torsion-line-bundles.md`, (0.1), §§1-6; 9 Oct 2026; lesson §11.1-11.2.
- **Statement**: Y compact connected complex threefold, c_1(K_Y) and c_1(L) torsion in H^2(Y;Z). Then
  chi(Y, T_Y (x) L) = chi_top(Y)/2 = <c_3(T_Y),[Y]>/2 = 1 - b_1 + b_2 - b_3/2; for the S6 threefold the value is 1 for
  every L and every period parameter. (No hypothesis on c_2 or on H^4.) Companion formula: the full degree-six
  term [ch(T) ch(L) td(T)]_6 = c_3/2 + c_1^3/2 - (19/24) c_1 c_2 + (5/4) l c_1^2 - (3/4) l c_2 + (5/4) l^2 c_1 + l^3/2.
- **Support**: 37 KB written proof (steps in 1.5); 74 finite checks. I verified the polynomial with sympy and the
  identity on a Calabi-Yau threefold.
- **What it adds**: over [AC26]: Cor. 10.6 gets chi = c_3/2 = 1 from Hirzebruch-Riemann-Roch with c_1 = c_2 = 0 integrally;
  here the hypothesis is only torsion c_1(K) and c_1(L), and the proof uses Hodge theory, Serre duality, the
  Frölicher Euler identity and nilpotence of [L] - 1 in K-theory. The same value follows from Riemann-Roch directly
  (every term other than c_3/2 contains c_1 or l), and chi(X,T_X) = c_3/2 is already in CDP98. Nothing new as a
  statement.
- **First assessment**: the chain chi_0 = 0, chi_2 = -chi_1, chi(T) = chi(T (x) K) = chi_2, chi_top = 2 chi_2 is correct. The
  analytic part (Fredholm index as a homomorphism on K^0) is standard.
- **A full check must establish**: (2.3)-(2.5) (nilpotence and torsion of [L] - 1); the signs in (5.1), (5.3).
- **Deserves a full check**: no - known result; a spot check suffices. **Interest**: 2.

### G1b-7
- **Title**: Duality on a Cartier divisor and top-degree base change for all scheme-theoretic fibres, proved by
  Hodge theory on the graph cone and the perturbation lemma. **Type**: new proof of known results.
- **Where**: lesson §10.1-10.3 (l. 930-1036); `src\proper-base-change-over-a-curve.md` (all);
  `src\general-proper-flat-surface-base-change.md` Theorem 1.1; cdp_program.tex `thm:cartier-duality`,
  `prop:analytic-base-change`, `cor:surface-top-base-change`.
- **Statement**: (i) S an effective Cartier divisor (possibly non-normal, reducible, non-reduced) in a compact
  smooth complex threefold Y, E a vector bundle: omega_S = (omega_Y (x) O_Y(S))|_S and natural isomorphisms
  H^q(S, E|_S)^v = H^{2-q}(S, E^v|_S (x) omega_S); H^q(S, E|_S) = 0 for q > 2. (ii) X connected compact complex manifold
  of dimension n, f : X -> C nonconstant to a smooth curve, E a vector bundle: f is flat, every fibre is Cartier;
  near each c there is a bounded complex K of finite free O-modules, in degrees [0, n-1], representing Rf_*E, with
  K (x) C(t) computing H^*(X_t, E|X_t) for the full fibre; 0 -> (R^q f_*E)_t/sigma -> H^q(X_t, E|X_t) ->
  (R^{q+1} f_*E)_t[sigma] -> 0; R^q f_*E = 0 for q > n-1; (R^{n-1} f_*E)_t (x) C(t) = H^{n-1}(X_t, E|X_t) for every t,
  with no local freeness. (iii) the same top-degree statement for proper flat maps of complex spaces with
  two-dimensional fibres over a Riemann surface.
- **Support**: (i) from smooth Serre duality on Y applied to E(-S) -> E; (ii) the construction in 1.3; (iii) the nine
  companions. Finite checks PROPER_CURVE_CHECKS.json (73).
- **What it adds**: over [AC26]: it cites Ramis-Ruget(-Verdier) and Banica-Stanasila for these; here they are
  proved within the course. As statements: classical (Serre-Grothendieck duality on Gorenstein spaces; Grauert;
  base change in top degree). The graph trick (embed f^{-1}(U) in X x U as a Cartier divisor, so that singular and
  multiple fibres are handled by a two-term complex on a fixed compact manifold) with Crainic's perturbation
  formulas is neat; a brief search ("homological perturbation lemma proof of Grauert direct image theorem ...") did
  not find it written down, but I would not claim novelty.
- **First assessment**: plausible; the weak points to read are the uniformity of the Sobolev/smooth estimates in
  the parameter (4.5) and the identification of the parameter-holomorphic relative complex with Rf_*E (§5).
- **A full check must establish**: (2.7), (3.3), (3.6)-(3.7), (4.4)-(4.5), §5, and (6.1)-(6.3).
- **Deserves a full check**: maybe - only if the course is to stand without citing Grauert. **Interest**: 2.

### G1b-8
- **Title**: Torsion of the relative differentials Omega^p_{X/B} for the S6 fibration: global formula and the local
  modules at double, triple and multiple-fibre points. **Type**: computation.
- **Where**: lesson §7 and Exercise 2, l. 483-734, 1442-1470; id CG-S6-10-RELATIVE; [N] Prop. 6.1 (p = 1 local
  modules); [R] prop:torsion (gcd formula, global divisor, p = 2) per the lesson.
- **Statement**: (7.3) for t in R = C{x_1..x_n} nonconstant, Tors(Omega^1_{R/C{t}}) = R[w] = R/(phi), phi = gcd of the
  partials, w = dt/phi. (7.12) for f with fibres locally u x^m: Tors Omega^1_{X/B} = (f^* omega_B (x) O_X(Z))|_Z,
  Z = sum_c (f^*(c) - f^*(c)_red); for X, Z = 2 S_1 + 3 S_2, and Omega^1_{X/P^1} is torsion-free but not locally free along
  the double curve of W. (7.15) for t = xy, Tors Omega^2 = R/(x,y) (dx ^ dy). (7.19)-(7.21) for t = xyz,
  Tors Omega^2 = Q = (R zeta_1 + R zeta_3)/(x zeta_1, y(zeta_1 - zeta_3), z zeta_3) = Ext^2_R(R/J, R), J = (xy,xz,yz) (the
  dualizing module of the three axes), Ann(Q) = J, two generators at the triple point. (7.22) t = s^m.
  (7.23) Omega^3_{R/C{t}} = R/(partials of t).
- **Support**: direct module computations; checker items on the maps, syzygies, wedge relations and the Ext
  presentation.
- **What it adds**: over [AC26]: not in §10; it bears on the "expected values" of Remark 9.21 and on any relative
  Hodge/Frölicher computation (the lesson says none is drawn). The lesson's own additions: (7.23), Exercise 2.
  Literature: standard commutative algebra; not searched.
- **First assessment**: looks right; easy to confirm by computer algebra.
- **A full check must establish**: (7.3) (UFD argument), (7.12) gluing, (7.18)-(7.21) signs.
- **Deserves a full check**: maybe - cheap; needed if someone computes R^q f_* Omega^p_{X/B}. **Interest**: 2.

### G1b-9
- **Title**: c_1(L|_F) = 0 for every L in Pic(X) from the factors of automorphy at the three fillings (norm equations
  2k - 3k/2 + 0 = k/2), without H^2(X;Z) = 0. **Type**: new proof of a step of [AC26] (Theorem 10.5, Step 1) by a
  different route; computation.
- **Where**: lesson §14 and Exercise 6, l. 1510-1885, 2211-2235; id CG-S6-10-BOUNDARY; cdp_program.tex l. 602-1196
  (`lem:picard-crossed-defect`, `lem:picard-finite-norm`, `lem:picard-cusp-defect`, `prop:direct-boundary-picard`).
- **Statement**: With V = Z gamma + Z u + Z w + Z delta, T_1, T_2 as in [AC26] (A.1): (Lambda^2 V)^{<T_1,T_2>} = Z q,
  q = uw + 6 gamma delta; V_G = V/((T_1 - 1)V + (T_2 - 1)V) = Z[delta]. For a holomorphic line bundle L on X write
  c_1(L|_F) = k q. The factors of automorphy of L on the universal cover of the middle family define a crossed
  homomorphism d : <rho_1, rho_2, rho_0> -> V_R, d(gh) = d(g) + T_g d(h), well defined up to (T_g - 1)a, with
  d_1-bar + d_2-bar + d_0-bar = 0 in V_G (x) R. Extension over the finite filling j gives N_{T_j} d_j = iota_{v_j} E,
  N_{T_j} = sum_{r < m_j} T_j^r, (m_1, m_2) = (3,4), v_1 = (1,2,-4,0), v_2 = (-1,-3,3,0); iota_{v_1} q = 2 eta_1, iota_{v_2} q = -3 eta_2,
  [eta_1] = 3[delta], [eta_2] = 2[delta]; so d_1-bar = 2k, d_2-bar = -3k/2. Extension over the cusp gives d_0-bar = 0.
  Hence k/2 = 0 and c_1(L|_F) = 0.
- **Support**: 9-page written argument with the deck groups, lifts and branch choices; checker items for (14.3),
  (14.5), (14.25), the norm identities and 2 - 3/2 = 1/2; my recomputation confirms all the linear algebra.
- **What it adds**: over [AC26]: there, c_1(L) = 0 because H^2(X;Z) = 0 (which rests on the Leray computation of
  §7). This is an independent derivation; it also exhibits how the invariant class q (the type (1,6) class of
  [E26] §8.4, NS(F_b) = Z eta of [AC26] Cor. 9.8) fails to extend: the two multiple fibres contribute 2 and -3/2 and
  the cusp 0. The argument uses only transition functions, so it applies to smooth line bundles too and is in
  substance a boundary computation of the transgression of q. Literature: not searched.
- **First assessment**: the conclusion is robust to the sign conventions (|2k| != |3k/2|, cusp term zero). The parts
  that need care are the identification of the boundary deck group with the filled one ((14.18)-(14.19)) and the
  cusp winding (14.21)-(14.24).
- **A full check must establish**: (14.9)-(14.13); (14.16)-(14.20) including Q_{j,log}^{m_j} = tau_{v_j} from lesson 3
  and the independence of branch; (14.22)-(14.24); the relation rho_1 rho_2 rho_0 = 1 for zero-section lifts.
- **Deserves a full check**: maybe - a useful independent confirmation of H^2-vanishing on fibres; not a new
  statement. **Interest**: 2.

### G1b-10
- **Title**: The degrees of a line bundle on the hexagon of dP_6 determine and are determined by the mixed block
  of its Chern class on the nearby torus: E_M((lambda,0),(0,m)) = -B(B_0 lambda, m). **Type**: computation / new
  formula for the cusp model.
- **Where**: lesson §15 and Exercise 5, l. 1889-2209; id CG-S6-10-CENTRAL; cdp_program.tex `lem:picard-cusp-defect`
  (l. 988 ff.).
- **Statement**: Let M be a holomorphic line bundle on the cusp neighbourhood N_0, pulled back to the toric cover
  Y_eps with deck maps Psi_lambda (15.1), and let (d_1,d_2,d_3,d_1,d_2,d_3) be its degrees on the six boundary curves of
  E_0 = dP_6. With a(x,y) = (d_2+d_3) x(x-1)/2 + d_3 xy + (d_1+d_3) y(y-1)/2, D_a = sum_v a(v) E_v and
  B = [[d_2+d_3, d_3],[d_3, d_1+d_3]], the bundle M (x) O(-D_a) is trivial on every component E_v, and the Chern form of
  M on a nearby fibre C^2/(Z(s)Z^2 + Z^2) has mixed block E_M((lambda,0),(0,m)) = -B(B_0 lambda, m),
  B_0 = [[0,1],[-1,0]]. The map (d_1,d_2,d_3) -> mixed block is an isomorphism Z^3 -> {trace-zero integer 2x2
  matrices} ((16.1)-(16.3)). Consequently E_M = 0 implies eta^*(M|_W) trivial; with G1b-9, eta^* i^* : Pic(X) -> Pic(dP_6)
  is zero without using H^2(X;Z) = 0.
- **Support**: written proof (toric divisor D_a, frames with zero horizontal winding on the charts
  U_v = Delta x (C^*)^2 and S_sigma, factor of automorphy (15.20)); checker items for (15.3)-(15.7), (16.1)-(16.2); I
  rechecked (15.6)-(15.7) by hand.
- **What it adds**: over [AC26]: (10.5) is obtained there from c_1 = 0 and H^1(dP_6,O) = 0; this is an explicit
  specialization formula for the cusp, valid for any line bundle on the cusp neighbourhood. It may be reusable for
  Engel's Mumford filling and for other toric cusps ([E26] §8.5). Literature: this is the kind of statement known
  for Mumford degenerations of abelian varieties (the quadratic function a and its polarization B); not searched.
- **First assessment**: plausible; the delicate step is (15.16)-(15.18) (zero winding of the frame ratios on the
  open torus, where the comparison frame lives on S_sigma).
- **A full check must establish**: Cartier-ness and local finiteness of D_a; (15.8)-(15.10); (15.11) with the
  t_c-power; (15.16)-(15.21) with signs.
- **Deserves a full check**: maybe - if the "analytic route" is to be relied on, or for generalizations.
  **Interest**: 2.

### G1b-11
- **Title**: Which CDP statements X contradicts, and the monodromy correction in the original periods.
  **Type**: correction of the literature (restated from [AC26] §10.5) / expository, with two small additions.
- **Where**: lesson §12, l. 1258-1394; id CG-S6-10-CDP.
- **Statement**: (12.1) for G = K ⋊ Q, G^ab = (K^ab)_Q + Q^ab. For X°: Lambda_{<A_1,A_2>} = Z[gamma-hat] (generators
  (12.3)), H_1(X°;Z) = Z^3 (not rank 6), im(H^1(X°;Z) -> H^1(F;Z)) = Z gamma = H^1(F;Z)^{<T_1,T_2>} (12.5), and its image in
  H^1(F,O_F) is the line spanned by (a_0 d zeta_1-bar - d zeta_2-bar)/(2iD), a_0 = Im mu/Im tau, D = Im beta - 6 (Im mu)^2/Im tau
  (12.6). (12.8): H^2(X, T_X (x) L) != 0, chi(X, T_X (x) L) = 1, c_3 = 2, for every L, so 2.2 a), b), c) all fail,
  "including any generic-twist interpretation" of a). X is not a counterexample to CDP20 Theorem 2.1: every
  meromorphic map X -> P^1 is a rational function of f and hence holomorphic.
- **Support**: short proofs; checker items (12.3) and the period formula.
- **What it adds**: over [AC26]: Lemma 10.7 and the count are there, and [AC26] goes further (failure of the
  conclusions of CDP20 Lemma 4.2, Cor. 5.2, Prop. 5.5; Prop. 10.8), none of which the lesson repeats. New here:
  the explicit formula (12.6), and the explicit remark on Theorem 2.1 (also in the status note).
- **First assessment**: fine. See section 3 for a numbering inconsistency in the CDP98 locators.
- **A full check must establish**: nothing beyond [AC26] §10.5; the locators.
- **Deserves a full check**: no - covered by a check of [AC26] §10. **Interest**: 2.

### G1b-12
- **Title**: Self-contained proofs of the analytic prerequisites (nine companions, 60 arguments, plus the smooth
  duality chapter), with a few repairs of the source text. **Type**: expository only (small corrections of the
  literature inside).
- **Where**: `src\general-analytic-{qn,wl,bk,cl,qg,ns,bt,rp,fc}.md`, `sources\general-analytic-proofs.json`,
  `src\general-proper-flat-surface-base-change.md`, `src\smooth-duality-and-finite-twist-complexes.md`; 10-11 Oct.
- **Statement**: see the table in 1.6; end results QG-6 (H^k(Z,F) = 0 for k > dim Z, Z compact, F coherent), FC-5
  (coherence of R^q f_*G for f proper onto a Riemann surface), FC-7 (top-degree base change for surface fibres).
  Recorded repairs of Demailly's author edition of 21 June 2012: "IX.5.12, with the recorded radius correction"
  (NS-4); "IX.5.34(d)-5.35 with the already recorded shift-sign correction" (BT-5; the cone convention
  C(h)^k = L^k + E^{k-1}, D(l,e) = (d l, h l - d e)); a "placeholder locator" in VI for the normal holomorphic frame,
  replaced by a proof (BK-2); NS-5 globalizes the product-section isomorphism by "refined overlap charts rather
  than an unproved global finite presentation"; QN-0 warns that sums of q-convex functions are q-convex only with a
  common positive subspace (with a 3x3 example).
- **Support**: the written arguments; `review: self_reviewed`; the texts of the eleven prerequisite units are in
  another course and not in this folder.
- **What it adds**: nothing to [AC26]/[E26] mathematically; it replaces citations by proofs. The repairs concern
  an unpublished book draft known to contain misprints; where they were "recorded" is not in this folder.
- **First assessment**: I read QN, WL, BK, CL, QG, FC and saw no gap at reading speed; NS, BT, RP statements match
  Demailly IX.5. Not a place to look for new results.
- **A full check must establish**: (only if wanted as courseware) each of the 60 items against Demailly, and the
  four repairs against the book.
- **Deserves a full check**: no - textbook material. **Interest**: 1.

### G1b-13
- **Title**: What replaces CDP20 Theorem 2.2? The files isolate, but do not answer, this question.
  **Type**: open question isolated (formulation partly mine; marked where).
- **Where**: lesson §11.5, §12; [AC26] §10.6; cdp_program.tex l. 1360-1665 (`thm:corrected-cdp-fibrewise`, the
  "exact monodromy repair" (5.33)); `topology_reduction.tex` l. 1264 ("Additivity therefore gives e(X) = e(W) = 2").
- **Statement**: Known after this work: for X as in CDP20 Theorem 2.2 (H^1 = H^2 = 0 integrally, a = 1, holomorphic
  reduction f : X -> P^1) the conclusions hold if H^2(X, T_X (x) L_0) = 0 for one L_0 (G1b-3), in particular if
  R^2 f_*(T_X (x) L) = 0 for one L, in particular (workbench) if all fibres are reduced and every delta_c is injective;
  for normal-crossings fibres the last condition is H^0(S~, eta^*(N^* (x) A_c)) = 0 (G1b-1). Not known: a statement
  with geometric hypotheses. Three precise sub-questions:
  (Q1, mine) When the general fibre is a torus, additivity of the Euler characteristic gives
  c_3(X) = sum over singular fibres of e(red X_c); CDP's "c_3 <= 0" is then the assertion that this sum is <= 0, and
  the S6 threefold has one fibre with e(W) = 2. Which non-normal surfaces occur as fibres, and is c_3(X) >= 0 for
  all such X, with c_3 = 0 exactly when every fibre has e = 0?
  (Q2, mine, from CDP20 Prop. 4.11) every singular irreducible reduced fibre is non-normal, so the hypothesis
  "all fibres normal" (the case where the p. 692 inference is valid, [AC26] Remark 10.4) reduces to "all fibres
  have smooth reduction", where c_3 = 0 follows from Q1's formula once the reductions have e = 0. Is there any
  case in which the CDP argument, correctly completed, proves something not given by Euler-number additivity?
  (Q3, from [AC26] §10.5 and the workbench) under trivial monodromy on H_1(F;Q), or under the span condition
  (5.33), CDP20 Lemma 4.2, Cor. 5.2, Prop. 5.5, 5.6 stand as printed; do threefolds with b_2 = 0, a = 1, torus
  fibres and trivial monodromy exist at all (r = s - 1 + 4 forces many components), and does c_3 <= 0 hold for them?
- **Support**: none beyond the cited conditional theorems; Q1's formula is elementary topology (I did not find it
  stated in general in the files; the workbench uses it for X).
- **What it adds**: a way to state the corrected problem to specialists.
- **First assessment**: Q1's additivity formula should be checked for the fibre structures allowed (compact
  analytic fibres, locally trivial outside finitely many points); the rest are questions.
- **A full check must establish**: n/a (questions). A literature check on degenerations of complex tori with
  non-Kähler total space would be the first step.
- **Deserves a full check**: maybe - as a research direction, not as a verification. **Interest**: 3.

## 3. Doubts and errors

1. CDP98 locators in the lesson are in mixed numbering. §12.1 (l. 1353) gives "arXiv ... Lemma 5.2(2) ... Theorem
   5.1; the published numbering ... is Lemma 3.2 and Theorem 3.1" (arXiv = published + 2), but §12.3 (l. 1390)
   cites "the earlier 1998 Theorem 4.1" and "1998 Corollary 4.2" without saying which numbering; [AC26] and the
   status note use "CDP98 Cor. 4.2" (following [E26] §1.1), and CDP20 itself calls the main theorem "Theorem 2.1 in
   [CDP98]". In arXiv v1 the main theorem and the corollary are unnumbered in the introduction. A checker should
   fix all CDP98 locators against the Compositio print.
2. The status note quotes Theorem 2.2 a) as "for i != 1 and generic M in Pic^0(X)"; arXiv:1904.11179v2 prints
   "H^i(X, T_X (x) M) = 0 for i != 1" with no quantifier. Harmless (H^2 != 0 for every M), but the quotation should
   match the print (the Compositio version was not checked by me).
3. The lesson states (3.6) under hypothesis (3.4), H^0(S~, Omega^1_{S~} (x) eta^*A) = 0, which is stronger than needed;
   H^0(S, tilde-Omega^1_S (x) A) = 0 suffices (as §1 says). No error; the sharp form is the one in G1b-1.
4. The lesson omits two statements that the public status note attributes to the correction: [R] Prop. 5.3
   ("torsion of Omega^1_S exactly at the non-normal points") and the normal case ([AC26] Remark 10.4). The status
   note's sentence is true for a Cartier divisor in a smooth threefold (a normal hypersurface has isolated
   singularities and torsion-free Omega^1; a reduced surface singular along a curve has torsion there), but I could
   not see [R]'s proof; a checker should read it, since "exactly" is a general claim.
5. README (l. 21): "[Lesson 10] ... includes three complete analytical companion chapters and six solved
   exercises"; §13 is headed "Four worked exercises" and §16 adds two. Consistent, only confusing.
6. The lesson never uses h^{0,1}(X) = 1 and writes Pic(X) = C^q; the course does not reprove [AC26] §9 (Dolbeault
   numbers, R^1 f_* O_X = O + O(-1)). So the course does not cover [AC26] Theorem 10.5(b), Prop. 10.8, or the
   failure of CDP20 Cor. 5.2 / Prop. 5.5. This is a gap of coverage, not an error.
7. `general-analytic-ns.md` l. 165 and `general-analytic-bt.md` l. 147: the "Sources" line has an empty locator
   ("edition of 21 June 2012. . The independently written ..."); the locators exist per item in the JSON
   (`source_locators`). In the JSON, WL-4..6 still have status `conditional_on_BKN-HERMITIAN-TORSION` although BK-5
   discharges the condition.
8. The four "recorded" corrections to Demailly's text (G1b-12) are referred to as already recorded, but the record
   is not in this folder; I could not see what exactly was corrected in IX.5.12 and IX.5.34-5.35.
9. Scope statements are careful throughout (the test family is not called a compact counterexample; "no priority
   is claimed"; "all review here is author self-review"). I found no overclaim in the lesson. The one sentence I
   would tighten is l. 1256: "The source correction note states the more restricted algebraic-reduction version" -
   true of [N] Theorem 5.2, whose proof however never uses a(X) = 1 beyond the existence of a divisor.
10. Authorship as recorded differs by layer: [N] says gpt-5.6-sol (Codex, Ultra), 1 Sep; [R] says Claude Opus 5.5,
    28 Sep; the course says GPT-6 Astra (Codex, Ultra), 9-11 Oct. The brief's "GPT-5.6 Sol" applies to [N] and the
    workbench, not to the course text.

## 4. Not read

- `src\general-analytic-ns.md`, `-bt.md`, `-rp.md`: conventions, all statements and source locators read; proofs
  read only in part (NS-0, NS-1 in full; the rest sampled). Reason: textbook functional analysis following
  Demailly IX.5, no candidate expected.
- `sources\general-analytic-proofs.json`: listed and compared with the .md files by ids, statuses and locators;
  the proof texts were read in the .md files, not again in the JSON.
- `src\smooth-duality-and-finite-twist-complexes.md`: headings and scope only (not in my assignment list, but a
  declared companion of lesson 10).
- [R] (the "S6 record" paper, Section 5): not available locally; not fetched (the Zenodo archive is a zip; the
  brief asks for no downloads beyond the literature check). All statements about [R] are second-hand.
- `cdp_program.tex`: only the statements and l. 17-111, 205-300, 1360-1665 (reader B has it in full).
- The lesson's two figures (`assets\conormal-section-and-torsion.svg`, `assets\hexagon-laurent-cocycle.svg`) and
  `checks\draw_lesson10.py`: not opened.
- CDP20 pages 4 and 12, and CDP98 beyond pages 1-2: not read. The Compositio prints of both were not consulted
  (arXiv versions only).
- I did not run `verify_conormal_torsion.py` (it writes its receipt into the course folder); I recomputed the
  main linear algebra separately in `work\scratch\G1b\check1.py`.
