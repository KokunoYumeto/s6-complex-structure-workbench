# S6 runs in progress: preliminary intake of the newest checkpoints

By the S6 intake agent, Claude Fable 5.2 at effort high, 15 November 2026. Everything here is PRELIMINARY: the four
runs (GPT-6 Astra, ChatGPT Pro mode) are still working, and these are hourly checkpoints. The reading was cursory:
for each run the head of its report (outcome table), its results CSV (status of every row, the text of the rows that
are not "Proved"), and the list of new files. No proof was read, no program rerun, no PDF opened. "Proved" below
always means "the run labels it proved". Statuses are the runs' own.

Checkpoints read (folder `s6_pro_prompts_20261112_work\returns\`):
`S6_02_PUSH_checkpoint_04_20261115T1638Z_unzipped`, `S6_03_CDP_checkpoint_04_20261115T1635Z_unzipped`,
`S6_04_MAPS_MANIFOLDS_checkpoint_02_20261115T1648Z_unzipped`, `S6_05_ARITHMETIC_checkpoint_02_20261115T1647Z_unzipped`.

## 1. S6_02_PUSH (checkpoint 04, after the fourth hour)

**State by its own table.** First line of the report: INCOMPLETE. 100 rows: 81 proved, 8 known, 6 refuted, 5 open.
A 96-page paper existed at checkpoint 03.

**Main claims so far.**
- **Part A (Engel's Conjecture 8.2), mostly closed.**
  - A.1: the nodal plumbing is a proper flat family with central fibre exactly Q (proved).
  - A.3 (proved): no proper flat filling of Engel's family with smooth general fibre has centre Q, even without a map
    to B. The tool is A.3.1: in a proper flat lci smoothing the Euler number of the general fibre is the virtual top
    Chern number of the reduced central fibre; for Q it is 0, and chi(X(u)) = 2. This is the outcome my Lead 1 and
    Lead 3 expected, by a cleaner argument; my pointwise count is corrected (smooth zero contributes 1, the integral
    over the smooth locus 0).
  - A.2: two minimal invariant refinements exist (as in my Lead 2), but **my description "every central normalization is
    a blow-up of P_S(O + M)" is refuted (A.2.3)**: some invariant smooth refinements have a P^3 component in a star.
    A.2.5 (new) gives all proper invariant smooth refinements by finite certificates and a blow-up/blow-down algorithm.
  - A.3.3: uniqueness of the two semistable fillings is refuted (also part of my Lead 3).
  - A.4: topology proved for every fan: Q has Betti numbers (1,1,8,7,10,0,1), chi = 12; the two minimal central fibres
    (1,1,9,7,11,0,1), chi = 14 (my expected value), pi_1 = Z. Classical Clemens-Schmid hypotheses fail (not Kahler).
- **Part B (the limit of the S^6 family): open.**
  - B.1.1 refuted: my Lead 4 (product of the smooth elliptic family with the Tate 12-gon) is false; replaced by a
    non-product semiabelian filling (B.1.2, proved locally).
  - B.3.1 refuted: my Lead 5. The finite-place models and the plain cusp model cannot be glued: the component
    rotations (+-4 at t = 0, +-3 at t = 1) never sum to 0 mod 12, against the peripheral relation.
  - B.4.1, B.5.1 open: no global filling of the S^6 family exists yet; so no central fibre, no topology.
  - Constraints proved for any semistable filling (B.4.2-B.4.6): the centre is simply connected, has h^1(O) >= 1,
    H^1(D; C) = 0, cannot be a proper algebraic variety, and (simple normal crossings) some closed stratum fails the
    dd-bar lemma. An assembly with hyperbolic toric Kato caps is excluded (B.4.6, new).
- **Part C (the class in Theta_7 = Z/28): open.** C.5.1: the residue of Phi is undetermined. Proved on the way: the
  mapping-torus comparison and the Eells-Kuiper formulas (spin and spin^c; my Lead 6's formula is labelled proved);
  the generator convention; Phi reduced to an annular orbit translation; a spin 6-manifold cap constructed; "affine
  frame defect -24", cap Pontryagin pairing of absolute value 24; the cubic is 3 times a relative circle-bundle square
  s_delta, not evaluated (C.3.15 open, C.3.20 new).
- **Part D (the boundary |w| = 216): closed by its table.**
  - D.1: no proper flat extension across any boundary point, even fibrewise-isomorphic ones; j(Alb S2) = J(iw/216)
    (my Lead 8 and R7, labelled proved).
  - D.2.2: **my Lead 9 is refuted as a characterization**: the non-separated directions are not only C(2,-1); the
    lattice vectors n^2(gamma + 3u - 3w) - 6n w + 3n delta at h = 1/n tend to (0,-3i). D.2.1 confirms the local
    expansion: tau = i - (3 pi i/2) h^2, D = -3|h|^2, which is my constant 2i/(3 pi) (finding F9).
  - D.3 (all Chabauty limits), D.4 (every supercritical level a nested Jordan curve; regular crossing at t = 0) proved.
- **Part E.** E.1 (Viaclovsky's coordinates, 2kl in his notation) proved. E.2.1: for all coprime (3k,4l),
  h^q(T) = (1,1,1,0) and a smooth miniversal Kuranishi line (answers Viaclovsky's Question 2); E.2.4 open (deformation
  classes across arbitrary chains: his Question 1). E.3: foundations from standard theorems; the five proofs of
  arXiv:2610.00250v1 audited; v1 has nothing on Parts A-D. E.4: all 19,701 boxes re-certified with Arb. E.5.1:
  **the prompt misdescribed the two-parameter family** (the source has III* and ranks 1, 1, 2, not III and three
  rank-one fibres: my error in the prompt); classification proved on the corrected data.

**New since checkpoint 03.** New rows A.2.5, A.4.8, A.4.9, B.4.6, C.3.16-C.3.20. Status changes: A.2.3 open -> refuted,
A.4.5 open -> proved, B.2.2 open -> proved. So the fourth hour finished Part A and B.2 and moved Part C by structure,
not by a number. Its three-hour assessment says it continues on the main open questions.

**Looks wrong or needs a look (at a glance).**
- A.4.1 says "without torsion" for the homology of Q and the minimal fibres; the first run had H_*(Q) =
  (Z, Z, Z^8, Z^7, Z^10, 0, Z), consistent.
- B.3.1 rests on one congruence (+-4 +- 3 not 0 mod 12). It kills my gluing; whether it kills every gluing of local
  semistable models, or only the plain cusp fan, decides whether Part B can close. The report says "corrected
  construction open".
- Part C has many intermediate integers (12, -24, 24, 3 s_delta) and an unresolved orientation sign; no value should
  be quoted from it.
- E.5.1: check the source (arXiv:2609.33785) for III versus III*; the first run's A.5 scope paragraph also wrote
  "y^2 = x^3 + tx + 1".

**Bears on.** F13 (boundary) is settled by D.1-D.4 if they hold. F14 (Conjecture 8.2) is settled by Part A in the
corrected form. F15 (S^6 limit, Theta_7) stays open, with my Leads 4 and 5 refuted. F9 confirmed. S6_04 B.6 asks the
same Theta_7 element by topology: neither run has it.

## 2. S6_03_CDP (checkpoint 04, after the fourth hour)

**State by its own table.** First line: INCOMPLETE. 127 rows: 111 proved, 10 refuted, 3 known, 3 with other labels
("exact check", "explicit second examples", "a second count counterexample"). The one main item still moving is C.2
(the sign of the Euler number of every fibre under b2 = 0): the conductor cases with rational normalization remain.

**Main claims so far.**
- **Part A (the conormal step in general).** The ambient cotangent kernel is the conormal line tensored with the
  inverse Jacobian ideal (A.1, A.2: pinch, cusp, ordinary cases computed). A.3: a complete lifting criterion for
  multiple fibres; "vanishing on the support does not imply vanishing on the multiple fibre" (A.3.2, a compact
  counterexample); CDP20 Remark 7.2 proved for smooth multiples. A.4: CDP20 Proposition 7.3 is labelled proved in
  full generality by a different argument, and one implication of its printed proof refuted (A.4.2).
- **Part B.** The nodal test family confirmed for every gluing scalar; a compact example with twelve nodal fibres has
  tangent-twist cohomology (0,0,12,0) (it fails the global CDP hypotheses, so it refutes the local inference only).
  B.3: under all CDP hypotheses, c3 > 0 forces a fixed non-normal support.
- **Part C.** C.3: the very general smooth fibre of the reduction is a 2-torus or a primary or secondary Hopf surface
  of algebraic dimension 0; bielliptic, Kodaira, Inoue and elliptic Hopf are excluded; every surviving type is
  realized. C.4 (the corrected theorem): generic tangent vanishing holds exactly when every irreducible non-normal
  support has non-zero ambient Picard pullback on its normalization; one zero pullback forces H^2 != 0 for every
  twist. C.5: all twists and all cohomology groups for X computed; the all-twist surjection has explicit exceptions
  at integral twists (C5b). C.2: unrestricted non-negativity of fibre Euler numbers refuted (a blow-up along a
  genus-two curve gives -2); under b2 = 0 proved for normal-crossings supports, class VII normalizations, all
  reducible fibres; rational-normalization cases in progress.
- **Part D (monodromy).** Corrected count by coinvariants proved; Wang's rational homology sphere is a second
  counterexample to the printed count and to the printed surjectivity. D.2: under trivial rational H1-monodromy,
  c3 <= 0 and b3 >= 2 hold without restriction (D.2.5), and an explicit compact example attains equality with
  integral H1 = H2 = 0, a = 1 (D.2.7; fibres join a primary Kodaira and a primary Hopf surface along an elliptic curve).
- **Part E.** a = 1 by vertical divisors for all named families; CDP20 Theorem 2.1 (non-holomorphic reduction) proved
  by a graph method, with an overgeneral auxiliary statement and CDP98 Lemma 1.5 and Proposition 1.1 corrected
  (E12, E17). Tangent cohomology and Kuranishi germs for all named families: original family (1,1,1,0) (cited from
  arXiv:2610.00250v1 with derivation, E9); coprime (3k,4l) and all affine twists (1,1,1,0) (E11); positive combs
  (2m+1, 8m+1, 6m+1, 0) with smooth miniversal germ of dimension 8m+1 (E15). E19: all affine twists have
  pi_1 = Z/|p|, H_1..H_4 = Z/|p|, H_5 = 0. Refuted: a fixed positive-genus-target stability claim (E10) and a
  "universal square theta identity" (E18), both Leads of the prompt as sent.

**New since checkpoint 03** (from its four-hour review): the sign and the zero-Euler geometry for every reducible
support; the class VII equality criterion; all horizontal tacnode images on irrational ruled normalizations
(A.5.18, without the lci hypothesis); two rational boundary classes. New section files of this hour are the
`part_A6_*`, `part_A7_*`, `part_C2_*` pieces.

**Looks wrong or needs a look (at a glance).**
- The breadth: 111 "proved" rows in four hours, many "with arbitrary singularities and multiplicities". The CSV
  statements are titles, not statements; the full intake has to read the theorems themselves (part_A 112 KB,
  part_C1_C3 53 KB, part_D 53 KB, part_E 71 KB).
- A.4: "Proposition 7.3 proved in its full stated generality" next to my reading that its Step 1 is where Lead 1
  gives a non-zero ambient section: the two have to be reconciled on W (the report says W is treated).
- D.2.7: a new compact threefold with H1 = H2 = 0, a = 1, trivial monodromy, c3 = 0, b3 = 2: every invariant needs
  recomputation; it is the first example of its kind in our material.
- C.3.2, C.3.3 are labelled "refuted surface assertion, with explicit ..." (secondary Kodaira and Hopf surfaces with
  H_1 = Z and H^2 = 0): unclear from the title what was refuted.
- A consistency check that passes: the comb tuple (2m+1, 8m+1, 6m+1, 0) has alternating sum 1 (cross-run list, X5).

**Bears on.** My S6_03 Lead 8 (H^2 through the normalization) is confirmed in a sharper form (C4: exact criterion;
C5b: exceptions at integral twists). E11 agrees with S6_02_PUSH E.2.1 on (3k,4l). E19 agrees with [AC26] Theorem 7.22.

## 3. S6_04_MAPS_MANIFOLDS (checkpoint 02, after about two hours)

**State by its own table.** First line: INCOMPLETE. 81 rows: 65 proved, 6 known, 5 refuted, 5 open. Undecided items:
B.6 (the Theta_7 class), D.2 (the table of all configurations), E.2 (higher integral homology of the shifted fibre
product), F.2 and F.3 in universal scope.

**Main claims so far.**
- **A (circle quotient, Engel's map).** The literal character fails at both triple points and two double curves; it
  extends along the double curve D1, which is **not** the curve fixed by Aut^0 (that is D2): a correction of the
  workbench statement quoted in the prompt (A.1.2). A smooth replacement map exists; its class is canonical only if its
  image near the cusp is confined to the cusp solid torus, otherwise all twelve classes of pi_6(S^3) occur (A.2.2).
- **A.3 (real forms, my Lead 9), proved by its table.** Exactly two conjugacy classes of antiholomorphic involutions;
  every non-empty fixed locus is S^3. For w on the negative imaginary axis both classes have non-empty fixed locus;
  on the positive imaginary axis exactly one. The circle action on the real S^3 is semifree in the first case, the
  free Hopf action in the second. The ambient knot type of the real S^3 in S^6 (Haefliger) is not asserted.
- **B (homotopy classes).** [e] = 6 nu' = eta^3, the element of order two of pi_6(S^3) (Lead 2 confirmed, with an
  independent e-invariant computation); f is null-homotopic; H = eta_4 eta_5; all named sphere families have the same
  quotient class, so [e] distinguishes none of them (B.4.1). B.5: a topological CW structure adapted to f; smooth
  framed handles are still missing.
- **B.6 (Theta_7): undecided.** No value of [Phi] or of 6[Phi]. Proved: 6[Phi] would leave two residues for [Phi];
  the even-shift maps extend to the conifold smoothing, whose monodromy is in the Torelli group with vanishing
  normal-framing invariant, hence in the central Theta_7 (B.6.3, B.6.4, new). My Lead 8 (Phi as a twist) is not
  enough: "an equivariant representative alone cannot determine the class".
- **C (Kummer covers).** Local covers proved; no smooth compact global source for N > 1.
- **D.** D.1: my Lead 5 refuted: the universal cover X~_d has Euler number 2d and H_2 = Z^(d-1) + Z/d, H_3 = Z/d,
  H_4 = Z^(d-1); it is not a connected sum of S^3 x S^3; it is identified as a specific spin 6-manifold M_d by its
  Zhubr invariants, with a canonical free cyclic action. D.2: the Mordell-Weil-rank-one list is 8 Oguiso-Shioda
  entries, 21 configurations; three treated for all multiplicities (Wang's type gives conic surgery on CP^3); the rest
  pending. D.3: the conifold family is constructed (proper, flat, contracts one (-1,-1)-curve, smooths
  xy = u(zv - s)); the smoothing is S^3 x S^3 with a = 1 (a = 1 structures on S^3 x S^3 were known).
- **E (fibre-product fourfold).** The literal normalization of Lead 6 is refuted; a corrected compact smooth fourfold
  has torsion-free homology with Betti numbers (1,0,2,1,2,1,2,0,1), K_Z = Pi^* L^(-5).
- **F (dimension eight). F.4.1, new in this checkpoint: "a compact complex fourfold, three-connected, chi = 6,
  oriented diffeomorphic to 3HP^2 # (-HP^2)"**, from an explicit monodromy tuple of orders (5,4) with a rank-three
  cusp and the genus-two pencil y^2 = x^5 + lambda^3 x + lambda^4 as period source (F.2.5, F.3.5-F.3.7).

**New since checkpoint 01.** F.3.5-F.3.7 and F.4.1 (the fourfold claim; at checkpoint 01 F.4 was undecided);
B.6.3-B.6.4; D.1 completed (cubic form, Zhubr invariant, cyclic action); D.2.7-D.2.8 (Wang type for every 3k);
E.1 integral homology proved torsion-free.

**Looks wrong or needs a look (at a glance).**
- **F.4.1 is an extraordinary claim** (a complex structure on a 3-connected 8-manifold, the analogue of the S^6 result
  one dimension up) produced and "audited" inside one hour. Every link needs an independent check: the monodromy
  tuple and its free affine lifts, the cusp filling, the holomorphic period family with non-degenerate imaginary
  part and bounded correction, the homology H_2 = H_3 = 0 integrally, and the diffeomorphism classification (it cites
  "Nagy 2026 Thm 1.4" and Nikulin). Until then it is a lead, not a result.
- A.1.2 contradicts a sentence of the prompt (the extendible curve is the fixed curve of Aut^0). S6_02 C.4.1 has the
  fixed curve as the one of direction e_2; which double curve the character extends along should be recomputed once.
- A.3.2: the asymmetry between the two halves of the imaginary w-axis depends on the sign conventions of R3
  (conjugate of X_c is X_(1 - c-bar)); to be rechecked with the Albanese nomes (q(Alb S2) = i w/216 is real on both
  halves, positive on one and negative on the other, which fits two different real types).

**Bears on.** S6_02_PUSH Part C: both runs are stuck on the same number; S6_04 adds that the class is central and
that 6[Phi] leaves two candidates. F10 of the survey (class of Engel's map) confirmed. The conifold family (D.3)
uses the moving zero of the linearization, the same two-parameter picture as S6_02_PUSH Part A.

## 4. S6_05_ARITHMETIC (checkpoint 02, after about two hours)

**State by its own table.** First line: INCOMPLETE. 79 rows: 69 proved, 6 known, 2 refuted, 1 open, 1 "computed with
explicit error bounds". The prompt as sent has more than my version: Leads 13-16 and Parts C.6-C.8 (heights over
number fields, the transcendence question at CM points, integral and measure identities), added on 13 and 15 November.
Undecided: A.5.4 (the Omega-results), six numerical factor identifications in C.6, and C.7(c) (the real norm at the
eleven rational CM points).

**Main claims so far.**
- **A (the count).** Bijections and census to 10^9; the group identified, no exceptional eigenvalues; the unrestricted
  count with error O(X^(2/3)) (derived from Lekkas-Petridis); **the sharp-arc bound R(X) = C0 X + O(X^(2/3+eps)) is
  labelled proved (A.4.4)**; the mean-square bound O(X^(2+eps)) proved; the Omega-results open.
- **B (the lattice).** Lead 6 proved; theta series and automorphism group of J; **all 129 Co0-orbits of totally
  isotropic planes of Lambda/3Lambda classified** with their eight overlattices and stabilizers (B.9); the "Weyl h/d
  rule" refuted with exactly 11 exceptions among 96 cases (B.6); the stabilizer of the cubic has order 252 (B.7).
- **C (the periods of X).**
  - C.1-C.3: my Leads 7-9 and 12 labelled proved: the values at z1, the Albanese nomes and the relation (27/64), the
    expansions at i and at rho; at t = 0, D_part has neither a local maximum nor a local minimum.
  - C.4: N as a Siegel function and local height (known, with derivation); on the torsion locus
    **N^12 = |Delta| / |psi_m(P)|^(12/(m^2-1)) for m = +-1 mod n**, with fields, and all 13 smooth roots up to order 8
    checked to 108 digits. Hand check (mine, three points): with Delta = 27 t^8 (t-1)^3 and
    psi_3(P) = -(9/16) t^6 (t-1)^2 this gives N^12 = 64/|t| for n = 2, 4, so 64 at t = 1 and 10 at t = 32/5; with
    psi_2(P) = t^2 (t-1) it gives 27/|t-1| for n = 3, so 27 at t = 0. All three agree with my numerical values (Lead 10).
  - C.5: CM and torsion together only at t = 0, 1, from Bourdon-Clark-Stankewicz Theorem 4.15(a) (Lead 11 confirmed;
    the reference I gave from memory was located as a three-author paper).
  - C.8: **the inequality N <= sqrt2 (R4) is labelled proved by explicit analytic estimates and three duplication
    steps, without the interval certificate (C.8.5)**; L = log N decreases strictly on every ray from t = 1, t = 1 is
    the unique maximum, every lower level set is one star-shaped Jordan curve, and a saddle proposed in a Lead does not
    exist (C.8.15); a measure identity of a Lead is corrected in sign and normalization (C.8.9: total mass 1/12).
  - C.6: heights of the specialized sections at the eleven rational CM fibres: ranks, section indices, three exact
    rational factors; six identifications numerical only.
  - C.7: algebraicity of N at CM points where P is not torsion: (a) proved, (b) proved under a period conjecture,
    (c) unresolved.

**New since checkpoint 01** (its own words): A.4, the mean-square part of A.5, the full classification in B.2, exact
factors in C.6, and the global geometry in C.8.

**Looks wrong or needs a look (at a glance).**
- A.4.4 is a strong claim in analytic number theory (a sharp-arc sectorial count with exponent 2/3 + eps, uniform in
  the angular frequency) reached in the second hour. The uniformity step is where such proofs fail; the full intake
  must read `sections/A.tex` (91 KB) at that step.
- B.9 (129 orbits) rests on computation; the mass-formula check it cites is the thing to rerun.
- C.8.5 would replace the 19,701-box certificate. It has to be compared line by line with S6_02_PUSH D.4.7-D.4.8,
  which reach the same level-set statement with "a complete interval and analytic certificate".
- C.3.2 (t = 0 neither maximum nor minimum; expansion with |t|^(4/3)) and S6_02_PUSH D.4 ("exact regular crossing at
  t = 0") describe the same point and must agree.

**Bears on.** F3 and F8 of my findings (M, the closed forms): confirmed and extended. Routes 2 and 3 of ROUTES.md
(algebraicity at CM points; a proof of N <= sqrt2 without intervals by the duplication ladder): Route 3.1 is what
C.8.4-C.8.5 claim to have carried out; Route 2 is C.7, still open in its unconditional part.

## 5. Cross-run list

- **X1. The Theta_7 class is the one number nobody has.** S6_02_PUSH Part C and S6_04 B.6 both stop before a value.
  Assembled so far: the class is central; 6[Phi] would leave two residues (S6_04 B.6.1); S6_02_PUSH has a cap with
  Pontryagin pairing of absolute value 24 and an unevaluated relative square s_delta and orientation sign. A value
  that appears in either final return has to be checked against the other run's partial data.
- **X2. No global limit of the S^6 family at w = 0 exists yet** (S6_02_PUSH B.4.1). My gluing (Leads 4, 5) is refuted
  by a congruence of component rotations. The proved constraints (centre simply connected, not algebraic, a stratum
  failing dd-bar) say the limit, if it exists, is far from a Kahler normal-crossings variety. Without it, the
  filling route to Theta_7 (my Lead 6) has no 8-manifold to compute on.
- **X3. Conjecture 8.2 is decided in corrected form** (S6_02_PUSH Part A): Q is the limit of the nodal models, not of
  X(u); semistable fillings exist, are not unique, and their normalizations are not all blow-ups of P_S(O + M).
  S6_04 D.3 (the conifold family) lives in the same two-parameter picture and should be read together with it.
- **X4. The boundary is treated twice**: S6_02_PUSH D.1-D.4 and S6_05 C.8 (level sets of D_part, the maximum, the
  behaviour at t = 0). They overlap on the level-set geometry and on the proof of the maximum; compare them.
- **X5. Tangent cohomology agrees across runs**: (1,1,1,0) for the original family, all affine twists and all coprime
  (3k,4l) in S6_02_PUSH E.2.1 and S6_03 E9, E11; combs (2m+1, 8m+1, 6m+1, 0) in S6_03 E15, whose alternating sum is 1,
  as Riemann-Roch requires on S^6.
- **X6. Corrections to my own leads and prompt text** found by the runs: Lead 9 of the push prompt (non-separated
  directions) false; Leads 4 and 5 false; "the normalization is a blow-up of P_S(O + M)" false in general; S6_04
  Lead 5 (connected sums of S^3 x S^3) false; the two-parameter family misdescribed in push item E.5 (III* and ranks
  1, 1, 2); the sentence that the character extends along the Aut^0-fixed curve false (S6_04 A.1.2).
- **X7. New claims that would be results on their own if they hold**, in order of how much checking they need:
  the compact complex structure on 3HP^2 # (-HP^2) (S6_04 F.4.1); the compact threefold with H1 = H2 = 0, a = 1,
  trivial monodromy and c3 = 0 (S6_03 D.2.7); the classification of the general fibre of the reduction (S6_03 C.3.1);
  the corrected CDP theorem (S6_03 C4); the sharp-arc exponent (S6_05 A.4.4); the 129 orbits (S6_05 B.9);
  N^12 on the torsion locus (S6_05 C.4.2, hand-checked at three points).
- **X8. arXiv:2610.00250v1.** S6_02_PUSH E.3 audited its five proofs and reports nothing in v1 on Parts A-D; S6_03 E9
  cites v1 for the original family. No run reports an error in v1.

## 6. Notes for the full intake (when the four final returns are in)

- Read first: S6_02_PUSH `sections/AB_push.tex` at A.3.1 (virtual Euler number), B.3.1, B.4.3-B.4.6; `D_push.tex` at
  D.1 and D.2.2; the `C_*.tex` files only if a value of [Phi] is claimed. S6_03 `part_C4.tex`, `part_C5.tex`,
  `part_D.tex` (D.2.5, D.2.7), `part_C1_C3.tex`. S6_04 `sections/fourfolds*.tex` (F.2.5, F.3.5-F.3.7, F.4.1),
  `real_forms.tex`, `maps_B.tex` (B.6). S6_05 `C_special.tex`, `C_critical.tex`, `C_torsion_heights.tex`, `A.tex` at A.4.4.
- Rerun: the Arb certificate (S6_02_PUSH E.4), the period and classification code behind S6_04 F.4.1, the mass check
  of S6_05 B.9, the 108-digit torsion check of S6_05 C.4.5.
- Not read in this pass: any proof; ROUTES.md beyond its headings; the prompts as sent (the Leads numbered 13-16 in
  S6_05 and the K-items cited by the runs are known to me only through the runs' tables).
