# G2 notes: course CG-S6, lesson 7 (integral homology, sphere recognition) and lesson 11 (almost complex structures), with their companions

Reader G2, Claude Fable 5.2, 12 Nov 2026. Read only; one scratch script at
`work\scratch\G2\check_lattices.py` (sympy; output quoted in G2-1).

Base folder: `K = C:\Users\user\Documents\math\research\s6_recent_results_main\courses\CG-S6`, sources in
`K\src\*.md`, checkers in `K\checks\`. File dates are 8-11 Oct 2026 (the latest, 11 Oct 12:32). The README
gives the authorship: "GPT-6 Astra (OpenAI), Codex, Ultra, 9 October 2026"; the three lesson-11 prerequisite
chapters keep arguments of GPT-6.1 Sol. Every chapter says: author self-check only, no independent review,
no novelty claim. The course is not in the cloned public repository (`repo\`); its chapters link to a
separate private course repository.

A point of vocabulary that governs everything below. In this course "original" and "actual" never mean
"new". They mean "the object as first defined, with no normalization": the original manifold X, the
original map g, the original stable framing, the original handle radii, the original sphere spectrum, the
original integer two. "The original six-dimensional framing invariant" is the classical Kervaire-Arf
invariant written with all its matrices; "the original Adams tower" is the Adams tower of the sphere.
Nothing called "original" in lessons 7 and 11 is a datum computed from the torus fibration f: X -> P^1,
except the integral cohomology computation of lesson 7, sections 1-8.

---

## Direct answers to the four questions of the assignment

**1. Explicit diffeomorphism X = S^6, handle decomposition or Morse function adapted to f?** No. The course
proves existence only, exactly as [AC26] and [E26] do, but with the classical theorems reproved instead of
cited. The chain is: pi_1 = 1 and H_* = H_*(S^6) (lesson 7, sections 1-8, from the fibration) => a degree-one
map g: S^6 -> X chosen by Hurewicz (section 9) => X is stably framed (pi_5 SO(7) = 0) => the framed class
vanishes because H_3(X; F_2) = 0 and Omega_6^fr = pi_6^S = Z/2 is detected by the Arf invariant => a framed
nullbordism W^7 "by the definition of framed bordism" => surgery to indices 3, 4 => regluing along the middle
level by a product of sphere twists => all handles cancel => a flow line map
`d(q) = iota_X^{-1} Fl^Y_T(j(q))` (lesson 7 (10.10); sphere-twist companion (7.1)). The Morse function on the
cobordism is obtained by Sard's theorem on a finite-parameter family
(`relative-morse-functions-and-original-handles.md` (1.5)-(1.7)); W, the surgeries, the twist word and the
gradient-like field are all existence statements. No handle of X is attached along a fibre, a multiple fibre
or the cusp fibre; "bielliptic", "cusp", "multiple fibre", "torus fibration" and "P^1" do not occur in the
nineteen smooth-recognition chapters (grep; the one hit for "cusp" is a link to the file name of lesson 5).
The only use of the complex structure after section 8 is the tangent operator J_X in one framing homotopy
(Pontryagin-Thom companion (8.12)), which the sphere-twist companion, section 7.1, then removes. The whole
argument is stated for an arbitrary oriented homotopy 6-sphere and ends with "Theta_6 = 0 ... no novelty is
asserted".

**2. What is "the original six-dimensional framing invariant"?** It is the Kervaire-Arf invariant
`kappa: Omega_6^fr -> F_2`: for a closed 2-connected stably framed (M^6, tau), the quadratic function
`q_tau: H_3(M; F_2) -> F_2`, `q_tau(x) = epsilon_tau(f) + mu(f)` (framing parity of an immersed representative
f: S^3 -> M, the class of the matrix (2.4) in pi_3 SO mod 2, plus its number of double points mod 2), and
kappa = Arf(q_tau). The course proves the quadratic law, framed bordism invariance, kappa(S^3 x S^3, Lie) = 1
(so the Lie-framed S^3 x S^3 is the nonzero element, i.e. nu^2), and for X: `kappa(X, tau_X) = 0` because
`H_3(X; F_2) = 0`. So yes, the invariant is the class of (X, stable framing) in pi_6^S = Z/2, and its value 0 is
forced for every homotopy 6-sphere (the stable framing is unique up to homotopy since pi_6(SO) = 0). The
framing tau_X is the abstract one from pi_5 SO(7) = 0 pulled back along the homotopy inverse; it is not the
framing induced by the torus fibration. The course never mentions Engel's Remark 8.3, the map S^6 -> S^3, the
Seifert picture, pi_6(S^3), pi_3^S, or a framing of the fibre tori (grep for "Seifert", "pi_6(S^3)",
"Remark 8.3", "torus knot" over all of `src\`: no hit; "Lie framing" occurs once, for S^3 x S^3). It neither
settles nor bears on C1-1, C1-2, C1-3. What it does contain that a checker of C1-2 could reuse: a complete
written Pontryagin-Thom correspondence with tangential framings (companion
`framed-manifolds-and-the-pontryagin-thom-map.md`, sections 1-8, and the explicit homotopy (7.14) of the
sphere-twist companion), and the convention-fixed statement pi_3 SO(3) -> pi_3 SO is multiplication by 2.

**3. Lesson 11: new statements about the almost complex structure underlying X?** None. Lesson 11 is a
self-contained exposition of (a) the octonionic J on S^6 and its Nijenhuis tensor, (b) the smooth
Newlander-Nirenberg theorem, (c) Borel-Serre (only S^2 and S^6 are almost complex). About X it says only:
the charts of lessons 1-5 give an integrable J_X (section 5); no diffeomorphism carries the octonionic J to an
integrable structure (trivial from tensoriality of N); X has no Kaehler metric, and no closed 2-form taming
J_X, because H^2(X; R) = 0 (section 5, (5.3)). Not in the course: that J_X is homotopic through almost complex
structures to the octonionic one (true and classical: pi_6(SO(6)/U(3)) = pi_6(CP^3) = 0; the course proves
only the real statement g^*TX = TS^6, spin-six companion (6.3)); c_1(X) = 0; LeBrun's theorem (no complex
structure orthogonal for the round metric); non-Moishezon, not of class C, balanced or other special metrics.
c_3: the course computes c_3 = -2u for its labelled octonionic field relative to the outward orientation
(the field induces the opposite orientation, lesson 11 after (3.9) and (10.16)); c_3(X) = 2 is used through
the Euler number. Orientation: Theorem 10.2 gives an orientation-preserving d: S^6 -> X.

**4. Self-contained proofs of unusual form or generality.** Listed in G2-3 to G2-7 with a sentence each.
The most unusual are: Theta_6 = 0 by regluing the two halves of a framed nullbordism along a product of
generalized Dehn twists (instead of Kervaire-Milnor's linking-number surgery), and pi_6^S = Z/2 by an Adams
tower in which the dual Steenrod algebra is identified only through degree 8.

---

## 1. Reading notes

### 1.1 `K\README.md` (11.6 KB, 11 Oct), `K\course.json` (69 KB, 11 Oct) — read in full
README: one paragraph per lesson; list of 46 checkers and companions; "no independent whole-course review is
claimed". course.json: 11 units, 84 results, 47 proof providers. Results for my lessons (all with status
`complete_written_proof_with_author_self_check`): CG-S6-07-HOMOLOGY ("Full original integral homology and
marked transgressions"), CG-S6-07-HOMOTOPY ("Original degree-one homotopy equivalence with both inverse
homotopies"), CG-S6-07-SMOOTH ("Orientation-preserving diffeomorphism homotopic to the original map, with
full frame and filling comparisons"); CG-S6-11-TYPES, -OCTONIONS, -NIJENHUIS, -ASSOCIATOR, -TRANSPORT,
-COORDINATES ("the corrected change-of-variable sign"), -GAUGE, -ANALYTIC, -INTEGRABILITY, -SPHERES,
-EXERCISES. Lesson 7 unit status: `authored_with_complete_receiving_proofs_author_self_checked`.

### 1.2 `src\integral-homology-and-sphere-recognition.md` (84.6 KB, 1185 lines, 11 Oct) — read in full
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

### 1.3 `src\sphere-twists-and-the-original-smooth-six-sphere-comparison.md` (65.6 KB, 836 lines, 11 Oct) — read in full
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

### 1.4 `src\almost-complex-structures-and-integrability.md` (79.5 KB, 1250 lines, 11 Oct) — read in full
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

### 1.5 `src\the-original-six-dimensional-framing-invariant.md` (110.6 KB, 1386 lines, 11 Oct) — statements and sections 2, 5.6, 6.4, 8.4, 9 read; the rest by headings
Sections: 1 pi_3 SO(3) -> pi_3 SO(n) and its factor two; 2 the obstruction `k_tau(f,phi) in pi_3 SO(7+s) = Z`
and parity `epsilon_tau(f)` for an embedded S^3 (2.4)-(2.9), "Framing-extension criterion"; 3 values (standard
sphere 0; both factors of S^3 x S^3 with the Lie framing 1; graphs); 4 algebra of F_2-quadratic forms, Arf and
Gauss sum; 5 immersions, generic homotopies, `Q_tau = epsilon_tau + mu` (5.28); 6 quadratic law (6.21)-(6.22),
`Arf(q_tau) = 1` for the Lie-framed S^3 x S^3 (6.24); 7 embedded representatives; 8 framed bordism invariance
(8.12), reduction to indices 3 and 4, `kappa: Omega_6^fr -> F_2` (8.13); 9 `kappa` is an isomorphism (9.3),
`[Sigma, tau_Sigma] = 0` (9.4), criterion (9.5); 10 exercises; 11 sources (Michel-Weber 1409.0704 as context).
"Original" invariant of X computed: kappa(X, tau_X) = 0, from H_3(X;F_2) = 0. Nothing else.

### 1.6 `src\spin-six-and-the-framing-comparison.md` (33 KB, 444 lines, 11 Oct) — statements and sections 4-6 read
Family index for loops; two-step loop periodicity; SU(4) -> SO(6) by Lambda^2; `pi_5 SO(6) = Z` by half the
Euler number (4.7); `pi_5 SO(7) = 0` (5.4); for a homotopy 6-sphere Sigma: `T Sigma + R` trivial (6.2), and an
oriented bundle isomorphism `B: g^* T Sigma -> T S^6` (6.3)-(6.4). General; X enters only as a homotopy sphere.

### 1.7 Topology companions of lesson 7 (opening, headings and statements, closing; a few proofs sampled)
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

### 1.8 Stable-homotopy companions of lesson 7 (opening, statements, closing; key statements read)
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

### 1.9 `src\smooth-duality-and-finite-twist-complexes.md` (35 KB, 10 Oct) — statements; sections 5-6 read
A lesson-10 companion (analysis, not topology): Hodge theory and Serre duality on a compact Hermitian
manifold without Kaehler hypothesis; for the family `d_z = d-bar_V + 2 pi i sum z_j b_j ^` of line-bundle
twists, a finite complex (H, D(z)) of holomorphic matrices by the homological perturbation lemma
(5.4)-(5.9); jump loci are analytic (6.1)-(6.2). Notes a misprint in Crainic math/0403266. General; applied in
lesson 10 to Pic^0(X) = C. Belongs to the reader of lesson 10.

### 1.10 Checkers
`K\checks\*.json`: every file reports all checks passed (for my chapters: INTEGRAL_HOMOLOGY 75, SPHERE_TWIST
442, FRAMED_SIX_OBSTRUCTION 1695, SPIN_SIX 54, ALMOST_COMPLEX 80, PONTRYAGIN_THOM 51, and so on). Each states
its own scope: finite identities (matrices, signs, small ranks); "do not certify the global topological
proof". I did not rerun them.

### 1.11 Baselines consulted
[AC26] `original_clean_transcription.tex` l.2632-2690 (Lemma 7.13, Prop. 7.14), l.3066-3200 (section 7.7),
l.5300-5470 (Appendix B), l.3216-3226 (Theorem 8.1, by Hurewicz, Whitehead, Smale, Kervaire-Milnor).
[E26] `engel_S6.txt` l.627-646 (diffeomorphism by Smale and Kervaire-Milnor), l.940-1140 (section 7).

---

## 2. Candidates

### G2-1. The exact specialization lattices at the two multiple fibres, in every degree, proved by explicit line-bundle descent; sign-definite transgressions
**Type**: refinement of [AC26] (and of [E26] Lemma 7.4); small.

**Where**: lesson 7, Theorem 2.1 with (2.2), (2.9)-(2.11), (2.14a), l.93-279; Theorem 6.1, l.702-782; section 8,
l.831-877; companion `integral-line-bundle-descent-for-the-affine-fillings.md` section 3, (3.1)-(3.7)
(not on my list; section 3 read). 9-11 Oct 2026.

**Statement**. With `h_j = gamma eta_j`, `b = gamma u w`, `c_1 = uw delta - 4 gamma u delta - 2 gamma w delta`,
`c_2 = uw delta - 3 gamma u delta - 3 gamma w delta`:
`pi_1^* H^2(S_1;Z) = Z h_1 + Z q` (the whole invariant lattice);
`pi_2^* H^2(S_2;Z) = {a h_2 + b q : a = b mod 2} = Z(2 h_2) + Z(h_2 + q)`, with form `[[0,1],[1,4]]` on S_2;
`pi_1^* H^3(S_1) = Z b + Z c_1`, `pi_2^* H^3(S_2) = Z(2b) + Z c_2`.
Descent criterion: a class `a h_j + b q` is c_1 of a line bundle on S_j iff the integer row equation
`l N_j = -kappa_j` has a solution, which for j = 2 forces `l_3 = -(a+3b)/2`; explicit lifted actions with
rows `(-22b, 0, 0, a+2b)`, `(9b, 0, 0, -(a+3b)/2)` and constant phases `8b/9`, `27b/32`.
Transgressions: `d_2(12 gamma) = omega`, `d_2(2q) = omega[delta]`, `d_2(2 gamma u w) = omega[gamma delta]`, and in
Engel's basis `d_2(12 psi) = p_E omega_E`, `d_2(2 xi) = -p_E omega_E[k]`, `d_2(2 theta_E) = p_E omega_E[k psi]`,
`p_E = -1`.

**Support**. Written proofs (about 5 pages in the lesson, 6 in the companion); checkers
INTEGRAL_HOMOLOGY (75), AFFINE_LINE_DESCENT (42). Course status: author self-check.

**What it adds**. [AC26] Prop. 7.14 has the index table, the degree-1 lattices, and the generators of the
cokernels ("generated by [q]" in degree 2, by [gamma u w] in degree 3 under 4 | eps_2(v_2)); it uses evenness
of the form of S_2 (Wu, K numerically trivial). [E26] Lemma 7.4 has the same table and argument. Neither
says which index-2 sublattice occurs in degree 2 at p_2: q not in the image leaves both `<h_2, 2q>` and
`<2h_2, h_2 + q>`, and both have even unimodular forms downstairs (`[[0,1],[1,12]]` and `[[0,1],[1,4]]`), so
evenness cannot decide. The course decides it (h_2 is not in the image) and gets evenness as a consequence
instead of an input. [AC26] Prop. 7.27 has the three differentials "with one and the same sign"; the course
fixes the sign by a convention and reconciles with Engel's (p, -p, p). Nothing downstream changes:
H^0(B,R^2) = Z(2q) either way. Literature: not searched (bookkeeping about this one manifold).

**First assessment**. Correct, by an independent check. Script `work\scratch\G2\check_lattices.py`:
A_1^3 = A_2^4 = I, A_j v_j = v_j; Smith form of A_j - I is (1,1,0,0), so the coinvariants are torsion-free;
the saturated rotation sublattice plus the invariant sublattice has index 3 in Lambda for A_1 and 2 for A_2;
Gram matrices of (h_j, q) are `[[0,3],[3,12]]` and `[[0,2],[2,12]]`; `(q - 3h_2)^2 = 0`, `h_2 (q - 3h_2) = 2`.
Hence S_1 is the bielliptic surface with group Z/3 x Z/3 and S_2 the one with group Z/4 x Z/2 (this is the
"product-cover degrees nine and eight" of lesson 1), and F = (E x F')/(Z/2) over S_2. On F the two primitive
isotropic invariant classes are h_2 = the Poincare dual of the rotation-direction subtorus, and
+-(q - 3h_2) = the dual of the translation-direction subtorus. The reduced multiplicity-4 fibre of the
elliptic fibration S_2 -> P^1 pulls back to one translation-direction subtorus, so q - 3h_2 is in the image;
the index is 2; so the image is `<q - 3h_2, 2h_2> = <2h_2, h_2 + q>`, as the course says. (This agrees with
Serrano's bases a/4, b/2 of Num for that type.) I also rechecked the algebra of (6.8)-(6.10): r = s = 1.

**A full check must establish**: the norm matrices N_j and kappa_j of the companion (2.10)-(2.11); the
necessity argument (3.2)-(3.3); (2.14a) through the duality test of `integral-duality-...md` (4.2)-(4.10);
the orientation convention behind omega and the dictionary matrix P of lesson 6.

**Deserves a full check**: no — verified here by a different route, and of bookkeeping interest only.
**Interest**: 2.

### G2-2. Misprints and slips found in the cited literature (grouped)
**Type**: correction of the literature (all at the level of a sign, an index or a swapped symbol).

**Where and what** (each as the course states it; I did not open the cited sources):
1. Hill-Taylor, arXiv:0710.2310v2, eq. 3.14: with their definitions 3.9, 3.12 the linearization at
   (id, 0) is `D_H Psi h = -sum_j d_{z_j} d_{zbar_j} h = -(1/4) Delta h`, not `+`; the right inverse under
   h(0) = 0 is `-4(G f - G f(0))`. Lesson 11, (6.9), l.575-586; Exercise 4 tests it on `H = z + eps z zbar`.
2. Konstantis-Parton, arXiv:1707.03883v1, section 6: the collapse (S^2)^n -> S^{2n} is a cohomology
   isomorphism only in degrees 0 and 2n. Lesson 11, after (10.13), l.1089; Exercise 5.
3. Goerss, arXiv:0802.1006v1: the display at source lines 133-139 reverses the two cohomology modules; the
   vanishing-line display at lines 469-490 ("0 < t-s < 2s + eps") would kill the nonzero class at
   (s,t) = (1,2). `the-adams-tower-and-exact-inverse-limits.md` section 6, l.247-262.
4. Dugger-Isaksen, arXiv:0901.1632v1, lemma at source lines 2362-2374: the Ext target should be
   `Ext_{H_**H}(M_2, H_**(X))` (same file, section 6); and "sign and odd-index discrepancies" in its
   lines 699-900 (`coefficient-rings-...md` sections 2-4 and 8).
5. Isaksen-Wang-Xu, arXiv:2001.04247v1, lines 652-654: the correspondence "tau_i, xi_{i+1} <-> zeta_i,
   zeta_i^2" is off by an index shift and omits powers of tau; exact map `Phi(zeta_i) = tau^{2^{i-1}-1} tau_{i-1}`
   (`coefficient-rings-...md` (1.4)).
6. Strickland, arXiv:2412.09361v1, source line 1256 (X where Y is meant in a mapping spectrum) and line 1264
   ("p-local" where "{p}-local", p inverted, is meant), with counterexamples
   (`the-original-adams-tower-and-arithmetic-completion.md` section 9).
7. Crainic, arXiv:math/0403266v1: printed `A(1 - h delta) = 1` should be `= delta`
   (`smooth-duality-and-finite-twist-complexes.md` after (5.9)).

**Support**. Each with a short derivation or a counterexample in the course.

**What it adds**. Nothing about S^6. Item 1 is in the chain of a proof the course gives in full. Literature:
not searched; whether later arXiv versions or the published versions already fix them is unknown.

**First assessment**. Item 1: I rederived (6.7) from the chain rule and the first variation (6.9); with the
course's reading of the definitions the sign is minus. Item 3: the classical vanishing line is
`0 < t-s < 2s - eps`, so "+" is a plausible misprint; the test point is right (h_1 at (1,2) is nonzero).
Items 2, 5, 6, 7 are plausible as described. None changes a theorem of its source.

**A full check must establish**: each against the cited version and the latest version of the source.

**Deserves a full check**: maybe — ten minutes each against the arXiv sources, if the user wants to send
errata to the authors. **Interest**: 1 (item 1: 2).

### G2-3. A self-contained proof that every homotopy 6-sphere is diffeomorphic to S^6, by regluing a framed nullbordism along sphere twists
**Type**: new proof or restatement of a known result (expository).

**Where**: lesson 7 section 10 (Prop. 10.1, Theorem 10.2), l.954-1083;
`sphere-twists-...md` sections 1-7; `the-original-six-dimensional-framing-invariant.md` sections 7-9;
the sixteen handle, Morse and Whitney companions of 1.7. 9-11 Oct 2026.

**Statement**. (i) For an embedded S^3 in an oriented 6-manifold P there is a diffeomorphism T_f of P,
supported in a tube, with `(T_f)_* x = x + lambda(v,x) v` on H_3(P;Z), v = [f]. (ii) If (H, lambda) is a
unimodular alternating lattice of rank 2r, finite products of transvections T_v act transitively on integral
Lagrangians. (iii) Let W^7 be a framed nullbordism of a homotopy 6-sphere Sigma, a ball removed, made
2-connected with handles of indices 3 and 4 only, `C' = C_- u_P C_+`. Then the belt classes and the attaching
classes span two integral Lagrangians B, L of H_3(P;Z) = Z^{2r}, and for phi a product of twists with phi_* L
complementary to B the reglued cobordism C_phi has unimodular incidence matrix, hence is a product, hence
Sigma = S^6 by an orientation-preserving diffeomorphism. (iv) For X: `d: S^6 -> X` with d ~ g and
d^{-1} ~ h_X. Consequently Theta_6 = 0.

**Support**. About 400 KB of written argument across the companions; finite checkers for the algebra. The
course: "author self-checked"; "no new mathematical discovery is claimed".

**What it adds**. [AC26] Theorem 8.1 and [E26] l.637-646 cite Smale and Kervaire-Milnor. The course replaces
the citations by proofs. The odd-dimensional step differs from Kervaire-Milnor section 6 (killing the torsion
of H_3(W) by framed surgery, with linking numbers): here the cobordism is cut at its middle level and
reglued, which is the "formation" picture of the odd-dimensional surgery obstruction (two Lagrangians in a
hyperbolic form; Sp(2r,Z) is realized by diffeomorphisms of the middle level). That picture is known
(Wall, Ranicki, Kreck), and (i) is the Picard-Lefschetz formula for a generalized Dehn twist. The h-cobordism
theorem is proved only for simply connected cobordisms of dimension 6 and 7. Literature: not searched.

**First assessment**. The architecture is sound and each step is a standard one; I read the sphere-twist
companion in full and saw no gap in sections 1-7 at that level (the sign in (2.4), the algorithm of section 3,
s = r, U unimodular, the dimension counts for the Whitney discs in (6,3,3)). Points I did not verify: the
bordism invariance of the Arf invariant (framing chapter section 8), the reduction to indices 3 and 4
(8.2-8.3), and the long coordinate proofs of the Whitney move and the cancellation. Two remarks. The
6-dimensional h-cobordism of Prop. 10.1 (X = D^6 u_phi D^6) is proved but not used by Theorem 10.2, which goes
through the 7-dimensional route alone. And the statement gives no information on d beyond its homotopy
class, which is automatic for a degree-one diffeomorphism.

**A full check must establish**: the Kervaire invariant chapter (well-definedness on immersions, quadratic
law, bordism invariance); the handle trading to indices 3, 4 in dimension 7; the Whitney and cancellation
chapters; that each cited "included" prerequisite is used within its stated hypotheses.

**Deserves a full check**: no for the purpose of finding results about S^6 (it is the classical theorem);
maybe if the course is to be published as a checked text. **Interest**: 2 (as exposition).

### G2-4. A self-contained computation pi_6^S = Z/2 with the dual Steenrod algebra identified only through degree 8
**Type**: new proof or restatement of a known result (expository).

**Where**: the ten companions of 1.8; the conclusion in
`the-original-integral-stable-group-and-its-completion-maps.md` (7.1)-(7.4). 10-11 Oct 2026.

**Statement**. `pi_6(S^_2) = F_2`, in Adams filtration 2, represented by `[xi_1^4 | xi_1^4]` (h_2^2);
`pi_6(S^_p) = 0` for p odd; pi_6(S) is finitely generated; hence `pi_6(S) = Z/2` and the 2-completion unit is
an isomorphism. Inputs proved on the way: Ext^{s,s+6} of the mod 2 dual Steenrod algebra for all s
(Theorem 1.1 of the cobar chapter), vanishing in stem 5 for all s, convergence of the Adams tower as a tower
of finite groups, comparison of the Adams completion with the p-completion for bounded-below spectra with
the transition bound `2m(n-b+1)`, and bijectivity of `F_2[xi_1, xi_2, ...] -> pi_*(H ^ H)` in degrees 0..8.

**What it adds**. Nothing new mathematically (pi_6^S is classical); the form is unusual: no Steenrod
operations, no Serre classes, no cellular Adams resolution tables; the Steenrod algebra enters only as the
coalgebra pi_*(H ^ H) in a finite range, computed by iterated bar constructions. One side product is off the
path: the cobar group in bidegree (2,8) of the motivic presentation over F_2[tau] has no tau-torsion
(coefficient-rings chapter, section 6, with a matrix certificate); known from the motivic Adams charts
(h_2^2 is tau-free). Literature: not searched.

**First assessment**. Not checked beyond statements. The risk is in the topological comparisons (the
identification of the E_2-term with the cobar complex of pi_*(H ^ H), convergence), which the finite checkers
do not touch, as they say themselves.

**A full check must establish**: Theorem 1.1 for all s (the filtration argument over F_2[x]); the degree-8
bijectivity; convergence and the completion comparison; finite generation of pi_6(S).

**Deserves a full check**: no — classical result; no bearing on S^6 beyond G2-3. **Interest**: 1.

### G2-5. The Kervaire-Arf invariant of framed 6-manifolds in explicit quaternionic form, and the homotopy between tangential and normal framings
**Type**: new proof or restatement of a known result (expository) / computation.

**Where**: `the-original-six-dimensional-framing-invariant.md` sections 1-9;
`framed-manifolds-and-the-pontryagin-thom-map.md` (8.9)-(8.13); `sphere-twists-...md` (7.9)-(7.19).

**Statement**. (a) `kappa: Omega_6^fr -> F_2`, `kappa = Arf(q_tau)`, is an isomorphism;
`[S^3 x S^3, Lie]` is the nonzero element; for 2-connected framed M^6: framed null-bordant iff Arf(q_M) = 0
iff H_3(M;F_2) has a q-zero Lagrangian (9.5). (b) kappa(X, tau_X) = 0. (c) For a stable tangent framing tau of
M^n embedded in R^N with derivative J, Gram matrix H = J^T J, Q = H^{-1}J^T, the normal framing E it induces
gives back the tangential framing `tau_E = tau_st S`, `S(v,a,b) = (Qa, P_nu a + Jv, b)`, and
`S_t(v,a,b) = (cos t' v + sin t' Qa, P_nu a + J w_t, b_t)`, `(w_t, b_t) = D_t(-sin t' v + cos t' Qa, b)`,
`D_t = R_t C_t`, is a homotopy from the identity to S through bundle automorphisms (n = 6, rank made even).

**What it adds**. (a) is Kervaire's invariant in dimension 6 (nu^2 has Kervaire invariant one). (b) is the
answer to question 2 above: zero, for the trivial reason. (c) is the standard equivalence of tangential and
normal framings with an explicit formula; I checked it: C_1 = -1 on E = TM + R^k, R_1 = 1 + (-1), so
D_1 = (-1_{TM}) + 1_k, and the rotation of (v, Qa) then gives S_1 = S. Correct.

**Deserves a full check**: no. **Interest**: 1.

### G2-6. Lesson 11: complete proofs of the octonionic obstruction, the smooth Newlander-Nirenberg theorem, and Borel-Serre
**Type**: expository only (with the correction G2-2, item 1).

**Where**: `almost-complex-structures-and-integrability.md`, sections 2-10; 9-11 Oct 2026.

**Statements with outside content**. `N_J(U,V) = 2[p,U,V]_O = -4 p x (U x V)`;
`|N_J(U,V)|^2 = 16(|U|^2|V|^2 - <U,V>^2 - <JU,V>^2)`; the complex Nijenhuis map
`Lambda^2 T^{0,1} -> T^{1,0}` of the octonionic structure is an isomorphism at every point, so a local
J-holomorphic function is constant (Ex. 3, and for any J whose Nijenhuis image spans T^{1,0}). Theorem 9.1
(Newlander-Nirenberg, smooth case) by Malgrange's method: gauge `sum_j d_{zeta_j} B_j = 0` obtained on a torus
with `L = -Delta/4` inverted as a Fourier multiplier; analyticity of B from the first-order elliptic system
(8.4) by a nested-ball factorial induction (8.11); coordinates from commuting complexified flows (9.2),
no analytic Frobenius theorem. Section 10: `c_n(E)[S^{2n}]/(n-1)!` is an integer, using only that
K^0((S^2)^n) is generated by products of Bott classes (the surjectivity half of periodicity, by Fejer
approximation, linearization and a Riesz idempotent).

**What it adds**. All known (Froelicher, Ehresmann-Libermann, Borel-Serre, Newlander-Nirenberg, Malgrange,
Atiyah-Bott). The periodic-gauge variant and the truncated Bott argument are economical routes. No statement
about X beyond those listed in the answer to question 3. Literature: not searched.

**First assessment**. I followed sections 1-6, 9, 10 and the induction (8.10)-(8.13) (the bound (8.12)
holds: both partial sums are at most 2/(k+3)). No gap seen at reading depth; the Sobolev bookkeeping of
sections 7-8 not checked line by line.

**Deserves a full check**: no. **Interest**: 1 (2 as teaching material).

### G2-7. General homotopy-theory and handle chapters (grouped)
**Type**: expository only.

**Where**: the files of 1.7 and `cw-models...`, `path-fibres...`, `spin-six...`.

**Items of slightly unusual form**: first Hurewicz theorem by coherent simplex contractions on singular
chains, with both inverse maps (no CW approximation); "homology equivalence of simply connected spaces is a
homotopy equivalence" by the path fibration and two edge maps of the Serre spectral sequence;
CW models of manifolds by cube telescopes (no triangulation); `pi_5 SO(6) = Z` (half the Euler number) through
SU(4) -> SO(6) and the evenness of c_3 on S^6, then `pi_5 SO(7) = 0` from the frame fibration; removal of
index-one handles when pi_1(M_-) -> pi_1(C) is onto (slides chapter, 8.1; the known 1-connected-pair form);
Whitney move and Morse cancellation written as compactly supported flows with explicit cutoffs (after
Laudenbach). Nothing in them is specific to X.

**Deserves a full check**: no. **Interest**: 1.

### G2-8. Not in the course, one line from what it proves: J_X and the octonionic structure are homotopic as almost complex structures
**Type**: refinement (an underclaim noted by this reader; classical).

**Where**: would sit after spin-six (6.3) or in lesson 11 section 5. The course proves the oriented real
isomorphism `B: g^*TX -> TS^6` and stops.

**Statement**. Almost complex structures on S^6 inducing a fixed orientation are sections of a bundle with
fibre SO(6)/U(3) = CP^3, and `pi_k(CP^3) = pi_k(S^7) = 0` for 3 <= k <= 6, so any two are homotopic. Hence
`d^* J_X` is homotopic to the octonionic structure inducing the outward orientation (in the course's
labelling that is -J, by lesson 11 Ex. 6), and (TX, J_X) = (TS^6, octonionic) as complex bundles
(`pi_5 U(3) = Z` by c_3/2, and c_3 = e = 2 on both).

**What it adds**. Nothing new; it is the standard remark (for instance in the surveys on the Hopf problem)
and is not in [AC26] or [E26] either, as far as I saw. It answers the natural question "which almost complex
structure is it" by "the only one".

**Deserves a full check**: no. **Interest**: 1.

---

## 3. Doubts and errors

1. **Naming**. Titles such as "the original six-dimensional framing invariant", "the original smooth
   six-sphere comparison", "retains both fillings, every signed incidence, the full frame defect" read as if
   data of X were computed. They are not (see the vocabulary note at the top). The "frame defect" A_phi (5.6)
   and the "tangent comparison" E_q (7.6) are written down and never evaluated or used; the course says so
   ("no claim that E is the identity or nullhomotopic is needed or made").
2. **Redundancy in lesson 7 section 10**. Prop. 10.1 and the 6-dimensional product theorem give
   X = D^6 u_phi D^6; Theorem 10.2 does not use this, it applies the 7-dimensional argument to X directly.
   The paragraphs between (10.4) and Theorem 10.2 repeat the same link sentences five times (accretive
   editing); the logical order of the proof has to be reconstructed from the companions.
3. **"Explicit" and "actual"**. "The actual framed nullbordism W", "an actual diffeomorphism phi", "the
   actual function" denote objects whose existence is proved; none is constructed from X. In
   `the-original-six-dimensional-framing-invariant.md` section 9: W exists "by the definition of framed
   bordism".
4. **Detour**. `coefficient-rings-and-the-original-degree-six-class.md` works over the motivic coefficient
   ring F_2[tau] because the source consulted (Isaksen-Wang-Xu) presents the motivic algebra; the chapter says
   itself that the identification with motivic operations "is not proved by this chapter", and the later
   chapters use the classical pi_*(H ^ H). It is not part of the proof of Theorem 10.2.
5. **Lesson 7 versus the baseline**. Sections 1-7 present as the course's own computation what is, step for
   step, [AC26] section 7.7 with Appendix B and [E26] section 7. The lesson names Engel in section 8 only; the
   Gysin argument of 4.3 is [AC26] B.6. No error; attribution inside the lesson is thinner than in the README.
6. **Underclaim**: G2-8.
7. **Exact lattice at p_2**: the lesson's sentence "The nonzero degree-three cokernel at p_2 is generated by
   the image of gamma u w" and (2.2) are right; [E26] says the degree-2 cokernel is "generated by xi" (= q),
   the lesson says gamma eta_2 is not in the image. Both hold (the image is {a = b mod 2}); no contradiction.
8. I found no mathematical error in the parts read in full (lesson 7, the sphere-twist companion, lesson 11).

---

## 4. Not read

- Read only by opening, headings, statements and closing (as the assignment prescribes), with the samples
  named in section 1: all files of 1.7 and 1.8, `thom-euler-for-lesson11.md`,
  `projective-splitting-for-lesson11.md`, `integral-chern-classes-for-lesson11.md`,
  `smooth-duality-and-finite-twist-complexes.md` (sections 5-6 read), `spin-six-...md` (sections 4-6 read).
- `the-original-six-dimensional-framing-invariant.md`: sections 3, 4, 5.1-5.5, 6.1-6.3, 7, 8.1-8.3, 10 by
  headings only. The bordism invariance (8.12) is the main unread proof behind G2-3.
- Lesson 11 sections 7 and 8.1-8.2: read at speed, estimates not verified.
- Not on my list, but lesson 7 depends on them: `integral-line-bundle-descent-for-the-affine-fillings.md`
  (section 3 read for G2-1; it is specific to X), `integral-duality-and-the-specialization-lattices.md`
  (headings only; its section 4 gives the dual-lattice test behind (2.14a)),
  `tangent-index-with-torsion-line-bundles.md` (headings only; lesson 10). The coordinator may want to make
  sure the first two are covered by the reader of lesson 6 or of lesson 10.
- `K\checks\*.py`: not run; JSON summaries read. HTML readers, `provenance.json`, `series.json`, `assets\`,
  `downloads\`: not opened.
- The cited arXiv sources of G2-2: not opened; the corrections are reported as the course states them.
- No web search was made: no candidate reached interest 4.
