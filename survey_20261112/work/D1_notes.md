# D1 notes: the lattice side lane (Niemeier A_5^4 D_4, Leech neighbours, triality, cubic value groups, Wilson, umbral shadow, Erdős–Straus bridges)

Reader D1, 12 Nov 2026. Model: Claude Fable 5.2. Survey reading (medium-deep), not a verification.
Base folder (abbreviated `R\` below):
`C:\Users\user\Documents\math\research\s6_recent_results_main\canonical_S6_snapshot\supporting_materials\workbench\research\`
Evidence folder (abbreviated `E\`): `...\supporting_materials\workbench\evidence\`
My scratch scripts (all exact arithmetic, python-flint / Fractions):
`C:\Users\user\Documents\workbench_review_20261112\work\scratch\D1\lat.py`, `cubic.py`, `es.py`, `nb.py`, `snf.py`.

## 0. The first question: how does this lane connect to the S6 threefold?

Short answer: **there is no mathematical map from the threefold X (or from its fibre lattice Λ = Z^4, its
monodromy, its (1,6) form, or the hexagon / dP6 fibre) to any of these lattices.** The lane is attached to the
S6 work by one elementary integer identity, one chosen marking, and shared small integers. In detail:

1. **Where the lattice N comes from.** N is not built from X. It is built from the Erdős–Straus residue datum
   modulo 840 = 24·5·7, taken over from an earlier (April 2026) note of the user's ES corpus ("Residual divisor
   shells ... the A_5^4 D_4 Niemeier refinement of the modulo-840 Erdős–Straus datum", cited as
   `esn:Residual2026`; see `R\ES_NIEMEIER_PROVENANCE.md`). The 24 free coordinates are indexed by
   V_840 = {r in (Z/840)^× : r ≡ 1 mod 24} (24 elements). The Legendre symbols mod 5 and mod 7 split V_840 into
   four fibres of six; the kernel S_840 = {1,121,169,289,361,529} = <289> is exactly Mordell's set of residue
   classes mod 840 not covered by the classical identities. Each fibre gives an A_5 (sum-zero vectors in Z^6); a
   D_4 is added by hand, with its discriminant group F_2^2 identified with the quotient V_840/S_840; the glue
   code (index 72) is the one that makes A_5^4 D_4 unimodular. So N is the Niemeier lattice A_5^4 D_4 with a
   labelling of its coordinates by residues. None of the lattice files mentions S^6, the threefold, the hexagon,
   or the (1,6) form (I grepped the ten lattice files: no occurrence).
2. **The one exact bridge to X: the linear form 12 l_0 − 4 l_1 − 3 l_2.** `erdos_straus_selector_crosswalk.tex`
   and `erdos_straus_koide_s6_bridge.tex` take the relation matrix R(l) = [[3, −l_1],[4, l_2 − 4 l_0]] of the
   abstract group <c,x,y | c central, xy = c^{l_0}, x^3 = c^{l_1}, y^4 = c^{l_2}> (the presentation that gives
   π_1(X) = Z/|12 l_0 − 4 l_1 − 3 l_2| in [AC26]) and observe that the Erdős–Straus divisor congruence
   R_j T − 4u = p^ε, R_j = 4j+3, written as the matrix [[R_j, −u],[4, −T]], is carried to R(l_0, l_1, 1) by the
   row shear [[1, −j],[0, 1]]. This is the identity (4j+3)T − 4u = 3T − 4(u − jT). It is a correct statement about
   2×2 integer matrices. It is not a map of spaces; the files say so themselves ("not a geometric morphism from
   the reciprocal cubic to the complex threefold", bridge l. 42–45, 1005–1009; crosswalk l. 316–322). The
   threefold has λ = −1 at (l_0,l_1,l_2) = (0,1,−1); the ES channels have λ = +1 and +p with l_2 = 1; "no audited
   map identifies" them (bridge l. 583–591).
3. **The number 12 and the character SL_2(Z) → Z/12.** The S6 family lives over the (3,4,∞) orbifold line, and
   its monodromy (elements of orders 3 and 4 with unipotent product) is modular: the higher-rung file records,
   from the "elliptic-kernel peripheral matrices", a surjective character χ: SL_2(Z) → Z/12 (I read only its
   summary statement, h24:thm:exact-numerical-boundary (ii)); Z/12 is the abelianization of SL_2(Z). `niemeier_umbral_shadow.tex` (l. 264–350) shows that the
   determinant of the 12-dimensional theta (Weil) representation for index m = h = 6 is e(−χ/12). Both are
   instances of Hom(SL_2(Z), C^×) ≅ Z/12: any character of SL_2(Z) is a power of the η^2 multiplier. The file then
   composes χ with Z/12 → Z/6 → S_840, j ↦ 289^j (l. 543–553). That last arrow is a chosen marking (a generator
   of Z/6 is matched with 289); nothing derives it from X.
4. **Triality and 24.** The workbench's "higher rung" (file `higher_rung_24d_continuation.tex`, not in my
   assignment) studies the octonionic flag manifold F_4/Spin(8) of dimension 24 with tangent module
   V_8 ⊕ S_8^+ ⊕ S_8^−. The lattice lane connects to it by (a) the textbook fact that the three nonzero
   discriminant classes of D_4 are the weights of V_8, S^+, S^− (esn:thm:d4-f4-triality), and (b) a chosen real
   isometry 𝓛: N⊗R → O^3 (n24:thm:full-isometry). (b) is a choice among a large family; see candidate D1-5.
   The higher-rung file itself states (h24:thm:exact-numerical-boundary, l. 6139–6168 there): "No arrow between
   these four lines is defined merely by equality of their integers."
5. **The numbers.** 3, 4 (orders of the two special fibres; entries of R(l)); 6 = |S_840| = Coxeter number of
   A_5 and D_4; 12 = lcm(3,4) = |SL_2(Z)^ab| = 2h = number of theta indices = Coxeter number of F_4;
   24 = rank = |V_840| = dim O^3; 72 = glue index = Fricke constant of the eta quotient T_6 = root count of
   A_2^12. Of these coincidences only "glue index = Fricke constant" is a theorem (see D1-9); the rest are
   equalities of integers.

So the lane is a self-contained piece of lattice arithmetic (mostly re-derivations of classical facts in
explicit coordinates, plus a few explicit computations) hung on the ES corpus; its tie to the S6 threefold is
the shear identity in item 2 and analogy otherwise. This is my reading; the files are careful and state the same
limits in their "nonclaim" fields.

## 1. Reading notes

All files carry filesystem date 2026-09-29 00:32 (copy date). Internal dates: 5–6 Sep 2026. Status marks are the
workbench's own.

### R\es_niemeier_shared.tex (79,366 bytes, 1,878 lines; "Shared mathematical module", 5–6 Sep 2026)
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

### R\es_niemeier_leech.tex (19,469 bytes, 532 lines; 6 Sep 2026; prefix `esnl:`, tags NL1–NL20)
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

### R\es_niemeier_triality_bridge.tex (18,369 bytes, 426 lines; prefix `n24:`; header "Staged only")
- n24:thm:full-isometry (l. 50–119): the isometry 𝓛: V_N → O^3 (even/odd triplets of each A_5 block to the three
  sectors; mean differences and D_4 coordinates to the diagonal), 𝓛 r = c 𝓛 for r = ρ(361), c the cyclic shift.
- l. 121–153 glue test in octonion coordinates; l. 155–222 Albert determinant
  det(λI + E(𝓛X)) = λ^3 − λ(X,X) + 2 t_N(X), tr(E∘E) = 2(X,X).
- l. 224–241 "Dependence": the map depends on the origins f_i, on 289, on the even/odd order, on the order of b
  and on the octonion basis; "no claim of independence".
- l. 243–321 the Leech neighbour transported to O^3; l. 323–426 glue symmetry, character computation showing
  the triality section <R̂, Ĥ> (7·1 ⊕ 5·sgn ⊕ 6·Std) is not conjugate to the frame S_3 on O^3
  (1 ⊕ 7·sgn ⊕ 8·Std); connected Spin(8) cannot preserve the lattice.

### R\es_niemeier_cubic_arithmetic.tex (23,513 bytes, 588 lines; prefix `nca:`)
- nca:thm:polynomial (l. 114–184): F = P_0 + √2 P_2 + √3 P_3, no √6 term.
- generators g_1..g_29 of N, h_1..h_30 of Λ (l. 186–238).
- nca:thm:finite-values (l. 251–298): the additive group generated by all values of a cubic on a finitely
  generated lattice is generated by F(b_i), F(b_i ± b_j) − ..., and the triple polarizations (4495 / 4960 items).
- Cayley–Dickson frame fixed (l. 300–320). nca:thm:value-modules (l. 322–437):
  V_F(N) = (1/27)Z ⊕ (√2/54)Z ⊕ (√3/18)Z, V_F(Λ) = (1/27)Z ⊕ (√2/216)Z ⊕ (√3/54)Z, quotient Z/4 ⊕ Z/3.
- l. 439–490 frame dependence, with an explicit orthonormal frame change that produces the value −√15/3.
- l. 492–588 which lattice symmetries preserve F (only the order-3 subgroup of the residue group; R̂, Ĥ and a
  root reflection do not), F(ρ) = 15√2 + 16√3, F(v) = 14/27 − 7√2/24 − √3/27.

### R\es_niemeier_residue_fixed_neighbor.tex (26,840 bytes, 782 lines; prefix `esrf:`, tags RF1–RF45)
- esrf:thm:equality (l. 49–97): Λ_σ = Λ_τ iff K_σ = K_τ iff τ ≡ ±σ mod 6N, for σ, τ in the orbit Ω = O(N)ρ.
- esrf:thm:no-fixed-neighbor (l. 113–178): r = ρ(361) fixes no Λ_σ (obstruction: no tetracode word of weight 4).
- RF9–RF19 (l. 185–311): q_1, q_2, β: N → F_3, I = ker(ℓ_0, β) of index 18, J = I + Z·3v, det J = 81.
- esrf:thm:common-J (l. 313–346): Λ_0∩Λ_1 = Λ_1∩Λ_2 = Λ_2∩Λ_0 = J, [Λ_j : J] = 9.
- esrf:thm:discriminant-correspondence (l. 363–529): J^∨/J ≅ F_3^4, q_J = (2/3)(2ad + bc + bd), the three
  Leech lattices are the planes P_0, P_1, P_2; matrix of r.
- esrf:thm:fourth-extension (l. 546–782): the r-fixed plane P_∞ gives M, even unimodular, 72 roots, A_2^12,
  [M : R_M] = 3^6; M ∩ N = L_0 of index 6 in both.

### R\es_niemeier_JM_cubic_extension.tex (13,819 bytes, 328 lines; prefix `jmv:`)
jmv:thm:IJM-generators (l. 69–104), jmv:thm:JM-values (l. 108–202): V_F(J) = V_F(M) =
(1/27)Z ⊕ (√2/216)Z ⊕ (√3/18)Z; jmv:thm:chain (l. 215–271): V_F(N) ⊂ V_F(J) = V_F(M) ⊂ V_F(Λ) with quotients
Z/4, Z/3. Ledger JM-CUBIC-VALUE-GROUPS-20260906 (VERIFIED). Evidence in
`E\period_lattice_continuation_20260906\jm_cubic\` (not opened; outside my list).

### R\es_niemeier_wilson_cyclic.tex (35,241 bytes, 883 lines; prefix `wcl:`)
Wilson's octonionic Leech lattice (L = E_8 = D_8 + Zs, pair sums in L s̄, total in L s, norm (1/2)ΣN) rebuilt
with explicit matrices: wcl:lem:e8 (l. 93–135), wcl:lem:complementary (l. 169–192), wcl:thm:Leech (l. 246–286),
wcl:thm:fixed-coinvariant (l. 319–374: fixed lattice Gram 3G_{E8}, coinvariant ≅ A_2 ⊗ E_8), glue sequence and
explicit anti-isometry (l. 376–432), a subgroup A_4 × (C_7 ⋊ C_3) of order 252 preserving lattice and cubic
(l. 434–489), the maps r_t do not preserve the cubic (l. 491–548), wcl:lem:quaternion-intersection
(l. 618–640), wcl:thm:literal-intersection (l. 688–783): Λ_cyc ∩ 𝓛(N) = Λ_cyc ∩ 𝓛(Λ) = {√2(a,a,a): a ∈ D_4},
Gram 6G_{D4}; cubic on it (l. 815–856). Ledger WILSON-CYCLIC-INTERSECTION-20260906 (VERIFIED).

### R\common_d4_image.tex (15,562 bytes, 443 lines; prefix `d4i:`, tags D4I1–D4I35)
d4i:thm:complete-image (l. 123–172): P(a) = a_0(a_0^2 − 3(a_1^2+a_2^2+a_3^2)) on D_4 has image
18Z ∪ (6Z+2) ∪ (6Z−2), with an explicit section by three affine lines; d4i:thm:local-images (l. 247–320);
factorization on the sum-zero slice P = 2(3w+u+v)(u^2 − uv + v^2) (l. 322–443).

### R\niemeier_umbral_shadow.tex (28,148 bytes, 706 lines; prefix `nus:`)
Specialization of Cheng–Duncan–Harvey to X = A_5^4 D_4: Ω^X = 5 I_12 + J (l. 93–123), M^X (l. 134–149), theta
transformation and intertwiner (l. 151–229), quadratic similitude Z/12 → Z/6 with multiplier 10 (l. 231–259),
determinant character (l. 261–367), residue Fourier map and twisted shadows from the class functions
(a_g, b_g, s_g, c_g) on GL_2(F_3) (l. 369–553), T_6 = η(τ)^5 η(3τ)/(η(2τ) η(6τ)^5), f^X = −q d/dq log T_6 =
5λ_6 + λ_2 − λ_3, T_6(W_6 τ) = 72/T_6, f^X|W_6 = −f^X, J_6 = T_6 + 5 + 72/T_6 (l. 555–684). Scope statement
l. 686–697: "They do not construct a new graded moonshine module or a new moonshine theorem."

### R\p1201_selector_jordan_bridge.tex (11,685 bytes, 322 lines) = E\p1201_selector_jordan_bridge_20260905\fifteen_selector_jordan_bridge.tex (identical up to a final blank line)
The 15 marked ES selector states at p = 1201 (table l. 50–73) mapped to rank-one points of Sym_2(R) ⊂ Herm_3(H);
thm:fifteen-span (l. 194–219): span and Jordan closure have dimension 3, not 15; counts 15, 54, 36, 29 at
p = 1201, 4561, 8761, 9601 (l. 224–231). `REPORT.md` (16,745 bytes) is the long form of the same; `LOGBOOK.md`
not read in full.

### R\erdos_straus_selector_crosswalk.tex (10,829 bytes, 322 lines; marks \Verified)
prop:es-first-half-denominator (l. 13–52), prop:es-two-channel-selector (l. 67–148),
thm:es-s6-selector-terminal-bijection (l. 191–241). Ledger S6-ES-SELECTOR-CROSSWALK (VERIFIED, l. 72).
Superseded in content by the next file, which repeats and extends it.

### R\erdos_straus_koide_s6_bridge.tex (37,172 bytes, 1,031 lines)
Longer version: lem:esksb-first-half, prop:esksb-shell-bijection, prop:esksb-two-channel,
prop:esksb-reconstruct, thm:esksb-bridge (l. 394–466), corollary (3.8)–(3.11), (3.12)–(3.14) affine coordinates,
lem:esksb-factors and prop:esksb-factor-congruence (l. 599–655), counterexample criterion (4.5) (l. 657–684),
examples on forgetting labels, thm:esksb-affine-gate (l. 814–875), descendant maps (7.1)–(7.7) (l. 882–985),
"Sharp verdict" (l. 987–1031). Despite the name there is no Koide content in this file beyond the title.

### R\ES_NIEMEIER_PROVENANCE.md (15,668 bytes; identical copy in E\es_niemeier_20260905\)
Sources: CDH Table 3; Mare–Willems; the April 2026 residual note; the "Foundation transport theorem"
(thm:exact-support-glue-Fricke-transport; the origin of T_6 and of "the original scalar 72"); excerpt of the
source's two-channel theorem whose wording is corrected; SHA-256 of snapshots.

### R\es_niemeier_bibliography.tex (3,028 bytes)
CDH 2014; Mare–Willems 2013; the two ES corpus items; Conway–Sloane 1982 "Twenty-three constructions";
Borcherds 1985; Wilson 2009.

### ..\WEB_PRO_TRIALITY_LEECH_FEEDBACK_20260906.md (7,856 bytes)
A handoff text to GPT (Pro mode), not feedback received: restates the lattice results and sets "a bounded next
calculation" (the image set of the cubic on the common D_4 slice), which `common_d4_image.tex` then answers.

### Evidence folders (reports and outputs only)
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

### My own exact checks (results)
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

## 2. Candidates

### D1-1
- **Title**: Three Leech neighbours of N(A_5^4 D_4) permuted by an order-3 Weyl element, their common sublattice J (det 81), and the unimodular overlattices of J. **Type**: computation / possibly new explicit configuration (novelty not established).
- **Where**: `R\es_niemeier_residue_fixed_neighbor.tex`, esrf:thm:common-J (l. 313–346), esrf:thm:discriminant-correspondence (l. 363–529), esrf:thm:fourth-extension (l. 546–782); 6 Sep 2026.
- **Statement**: Let r = C^2 on each A_5 block (coordinate shift by 2), identity on D_4; r ∈ W(N), r^3 = 1. Let σ_j = r^j ρ, Λ_j = {x + kσ_j/6 : x ∈ N, (σ_j,x) + k ≡ 0 mod 6}. Then Λ_0, Λ_1, Λ_2 are three distinct Leech lattices, Λ_0∩Λ_1 = Λ_1∩Λ_2 = Λ_2∩Λ_0 = J := I + Z·3v, I = {x ∈ N : (ρ,x) ≡ 0 mod 6, β(x) = 0} (β = fourth tetracode coordinate of the glue class), det J = 81, [Λ_j : J] = 9, J^∨ = Λ_i + Λ_j, J^∨/J ≅ F_3^4 with q_J(a,b,c,d) = (2/3)(2ad + bc + bd) mod 2Z in the basis (u_*, v, r u_*, r v), u_* = (ω_2, ω_4, 0, ω_2; 0). Λ_j/J are the planes P_0 = (a,b,0,0), P_1 = (0,0,c,d), P_2 = (a,b,a−b,b). The plane P_∞ = (a,b,−a+b,−b) is isotropic and r-fixed; its inverse image M = J + Zp + Zq (p = u_* − r u_*, q = v + r u_* − r v) is even unimodular with exactly 72 roots, root system A_2^12, [M : R_M] = 3^6, M ∩ Λ_j = J, M ∩ N = {x ∈ N : β(x) = 0, (ρ,x) even} of index 6 in both; r fixes four A_2 components pointwise and acts as a 3-cycle on the other eight.
- **Support**: written proofs (about 470 lines in total; inputs: the glue code, the equality criterion RF3, coset minima from the neighbour proof), checker `E\lattice_foundation_20260906\neighbours\check_fixed_neighbor.py` (PASS). Workbench status VERIFIED (ledger NIEMEIER-LEECH-EXACT-NEIGHBOR-20260906).
- **What it adds**: nothing over [AC26] or [E26] (unrelated to them). Over the literature: the neighbour construction along a Weyl vector is classical (Conway–Sloane 1982; Borcherds 1985; Chenevier–Lannes, arXiv:1409.7616, Thm 4.2.10 and Prop. 4.2.11, which I fetched and read at that place). I searched for "intersection of three Leech lattices index 9 / F_3^4 / A_2^12" and found no source for this specific configuration; I did not look in Chenevier–Lannes' tables of 3-neighbours. The statement is an instance of the general theory of neighbours, so "new" would mean only "this explicit instance".
- **First assessment**: solid. My script confirms every determinant, index, the pairwise intersections, the root system of M, and the isotropy formula. My script also completes the picture, which the files leave half done: the form q_J is hyperbolic, so there are 8 isotropic planes in two rulings of 4; all 8 overlattices are even unimodular; they are 6 Leech lattices and 2 copies of A_2^12 (M and M' = J + Zu_* + Z r u_*, the 2-neighbour of N along ρ/2). r fixes M and M' and permutes each triple of Leech lattices cyclically.
- **A full check must establish**: (1) the equality criterion RF3 and the no-fixed-member theorem for the whole orbit Ω (I checked only σ = ρ numerically); (2) the proof that the 72 roots of M are exhaustive (my enumeration confirms the count); (3) the 8-plane statement with a written proof; (4) whether J is known: is J characterized as an index-9 sublattice of Leech attached to a totally isotropic plane of Λ/3Λ, and which Co_0-orbit of such planes it is (this decides novelty and interest); (5) a search in Chenevier–Lannes (tables of p-neighbours of Niemeier lattices for p = 3) and in Borcherds' thesis for the pair (Leech, A_2^12, A_5^4 D_4).
- **Deserves a full check**: maybe; it is the one place in the lane with lattice content beyond re-derivation, but its interest depends on item (4). **Interest**: 2–3.

### D1-2
- **Title**: No member of the family {Λ_σ : σ ∈ O(N)ρ} is fixed by r; equality criterion for Weyl-vector neighbours. **Type**: new result (small) / restatement.
- **Where**: `R\es_niemeier_residue_fixed_neighbor.tex`, esrf:thm:equality (l. 49–97), esrf:thm:no-fixed-neighbor (l. 113–178).
- **Statement**: For σ, τ ∈ Ω = O(N)ρ: Λ_σ = Λ_τ ⇔ K_σ = K_τ ⇔ τ ≡ ±σ mod 6N. The element r fixes no Λ_σ; every r-orbit on the family has three members. Reason: a fixed member would need (rσ − σ)/6 ∈ N, whose glue class would be (t_1,..,t_4; 00) with all t_i ∈ {2,4}, i.e. a tetracode word of weight 4, and the tetracode has only weights 0 and 3.
- **Support**: written proof (about 110 lines), checker (720 A-block permutations exhausted). VERIFIED.
- **What it adds**: the first equivalence is the standard parametrization of d-neighbours by points of the quadric mod d (Chenevier–Lannes §4.2); the second statement is a small exact fact about this lattice. Not searched further.
- **First assessment**: the argument reads correctly (the block of σ is a permutation of ±1/2, ±3/2, ±5/2; Δ_j ≡ c mod 6 with 3c ≡ 0; c = 0 impossible). Minor.
- **A full check must establish**: the claim that each A-block of every σ ∈ Ω is a signed coordinate permutation of ρ_A (uses esn:fa:thm:full-quotient), and the class computation t_i = −c.
- **Deserves a full check**: no (small; would be covered by a check of D1-1). **Interest**: 2.

### D1-3
- **Title**: O(N) for N = N(A_5^4 D_4) as an explicit split extension W(A_5^4 D_4) ⋊ L(GL_2(F_3)), with the code isomorphism Θ and the D_4-triality quotient Q_8 → GL_2(F_3) → S_3. **Type**: new proof or restatement of a known result.
- **Where**: `R\es_niemeier_shared.tex`, esn:thm:glue-gl2 (l. 682–736), esn:thm:triality-q8 (l. 756–845), esn:thm:gl2-full-lattice-lift (l. 855–921), esn:fa:thm:full-quotient (l. 1616–1813), esn:fa:thm:residue-weyl (l. 1815–1868); 5 Sep 2026.
- **Statement**: Every T ∈ O(N) is uniquely w L_g with w ∈ W(R_ES) = S_6^4 × W(D_4) and g ∈ G, where G is the stabilizer of the glue H in {(ε, p, B)} = {±1}^4 ⋊ S_4 × GL_2(F_2) and Θ: G → GL_2(F_3) is defined by M_g j = j Θ(g), j(a,b) = (a+b, a+2b, a, b); L_g(X_1..X_4; d) = (ε_i X_{p(i)}; δ(B)d) with δ(B_R) = diag(−1,1,1,1), δ(B_H) = I − 2cc^T. |O(N)| = 48·(6!)^4·192. The projection G → GL_2(F_2) (action on the D_4 discriminant) is onto with kernel Q_8 = <[[0,1],[2,0]], [[1,1],[1,2]]> and section <diag(1,2), [[1,2],[0,2]]>. The residue group ρ(S_840) ≅ C_6 lies in W, commutes with L(G), and ρ(r)L_g gives C_6 × GL_2(F_3) ⊂ O(N) of order 288.
- **Support**: complete written proofs (about 600 lines; elementary: root graph components, maximal cliques of roots for O(A_5), glue stabilizer), checkers in `E\es_niemeier_20260905\`. VERIFIED.
- **What it adds**: the abstract quotient GL_2(3) with image PGL_2(3) on components is CDH Table 3 (and |G_1| = 2, |G_2| = 24 in Conway–Sloane ch. 16); the files credit this. The splitting itself is standard for every Niemeier lattice: O(N) = W ⋊ H with H the stabilizer of a Weyl chamber (equivalently of ρ), isomorphic to the glue-code automorphism group (search result: e.g. arXiv:1609.04154 states O(N) ≅ W ⋊ H for A_4^6). What is specific here: a different complement (it uses −1 on A_5 blocks and reflections in short roots of F_4 on D_4, so it does not fix ρ), the explicit matrices over F_3, and the placement of the residue six-cycle. The file says the complement is not claimed to be the simple-root-preserving one (l. 1383–1385) and compares the two sections in `niemeier_umbral_shadow.tex` l. 437–460.
- **First assessment**: correct as far as I read (I read the full-quotient proof in full). No new mathematics; a clean coordinate presentation.
- **A full check must establish**: nothing beyond a routine reading; optionally whether the two complements (this one and the chamber stabilizer) are conjugate in O(N).
- **Deserves a full check**: no (known result, explicit version). **Interest**: 2.

### D1-4
- **Title**: The Leech lattice as the 6-neighbour K + Z(ρ/6 − α) of N in the retained coordinates, with a hand proof of rootlessness and the quotient Λ/R_0 ≅ Z/12 ⊕ (Z/6)^2. **Type**: new proof or restatement of a known result.
- **Where**: `R\es_niemeier_leech.tex`, esnl:thm:leech-neighbor (l. 94–245), NL8–NL11 (l. 247–328), esnl:thm:cyclic-twelve (l. 348–381), NL15–NL18 (l. 383–450), esnl:thm:f4-coxeter-twelve (l. 468–525).
- **Statement**: as in the reading notes. In addition: N + Λ = K^∨, K^∨/K = <[α],[v]> ≅ (Z/6)^2 with q_K(a[α] + b[v]) = ab/3 mod 2; in N ⊥ U (U with Gram [[0,−1],[−1,0]]), w = (ρ,6,7) is primitive isotropic and w^⊥/Zw ≅ Λ by [(x,m,n)] ↦ x − mρ/6.
- **Support**: written proofs; checker `E\triality_leech_20260906\check_leech_neighbor.py` (PASS). VERIFIED.
- **What it adds**: nothing beyond the holy construction. Is anything beyond Conway–Sloane ch. 24 claimed? No: the file says "It is the holy-construction Leech lattice" and credits Conway–Sloane and Borcherds; the Lorentzian vector (ρ, h, h+1) is Conway's/Borcherds' standard one; Chenevier–Lannes Thm 4.2.10 states vois_h(L;ρ) ≅ vois_{h+1}(L;ρ) ≅ Leech in general. The only items stated that I have not seen stated elsewhere are bookkeeping: Λ/R_0 ≅ Z/12 ⊕ (Z/6)^2 and the order-12 class of v ("12" from Coxeter denominator 6 and the order-2 glue class of ρ).
- **First assessment**: correct; my script confirms det Λ = 1, evenness, no vectors of norm 2, the invariants (6,6,12), order 12 of [v], det(N+Λ) = 1/36. A side observation from my check (not in the files): along the same Weyl vector, the 2-neighbour of N is A_2^12 and the 3-neighbour is A_1^24, i.e. vois_d(N;ρ) has Coxeter number h/d for d | h = 6 in this case. I did not find this pattern in a quick search (not searched thoroughly; it may be in Borcherds' thesis or folklore).
- **A full check must establish**: nothing needed for the files' claims. For the side observation: whether "vois_d(N;ρ) has Coxeter number h/d for d | h" holds for all 23 Niemeier lattices and is in the literature.
- **Deserves a full check**: no (classical). **Interest**: 1–2 (the side observation 2–3 if it is not known).

### D1-5
- **Title**: Cubic value groups V_F(N) ⊂ V_F(J) = V_F(M) ⊂ V_F(Λ) with quotients Z/4, Z/3 (total Z/12) for F = Re((q_1 q_2) q_3) ∘ 𝓛. **Type**: computation.
- **Where**: `R\es_niemeier_triality_bridge.tex` n24:thm:full-isometry (l. 50–119); `R\es_niemeier_cubic_arithmetic.tex` nca:thm:polynomial (l. 114–184), nca:thm:finite-values (l. 251–298), nca:thm:value-modules (l. 322–437); `R\es_niemeier_JM_cubic_extension.tex` jmv:thm:JM-values (l. 108–202), jmv:thm:chain (l. 215–271); 6 Sep 2026.
- **Statement**: With 𝓛X = (A+M, B+M, −A−B+M), where A, B are the residuals of the even/odd coordinate triplets of the four A_5 blocks placed on the octonion units u_{2(i−1)+p}, and M = (√2/6)Σ_{a≤3} s_{a+1} u_a + (√3/3)Σ_k d_k u_{k+3}, s_i = Σ_j (−1)^j x_{i,j}; Cayley–Dickson product (a,b)(c,d) = (ac − d̄b, da + b c̄); V_F(L) := additive group generated by {F(x) : x ∈ L}: V_F(N) = (1/27)Z ⊕ (√2/54)Z ⊕ (√3/18)Z; V_F(J) = V_F(M) = (1/27)Z ⊕ (√2/216)Z ⊕ (√3/18)Z; V_F(Λ) = (1/27)Z ⊕ (√2/216)Z ⊕ (√3/54)Z. Albert determinant: det(λI + E(𝓛X)) = λ^3 − λ(X,X) + 2F(X).
- **Support**: polynomial identity proof; finite generation lemma for value groups of a cubic (correct and reusable: 2 pair terms because n_i n_j (n_i ± n_j)/2 are integers); exact enumeration (20,399 polarization entries) with Bezout certificates. VERIFIED.
- **What it adds**: nothing to [AC26]/[E26]. Literature: not searched; the object is defined by a choice, so there is nothing to compare with.
- **First assessment**: the numbers are right: my independent implementation reproduces all four groups and the quotients. **How canonical is the isometry? It is a choice, and the value groups are invariants of the choice.** The file says this (triality bridge l. 224–229; cubic arithmetic l. 439–490 gives a frame change producing the value −√15/3). 𝓛 is pinned by "isometry with 𝓛r = c𝓛" only up to the centralizer of c in O(24), which is O(8) × U(8) (dimension 92), while the stabilizer of the cubic commuting with c is much smaller; the assignment of the eight "t-channels" and of the eight coordinates (α_1..α_4, d_1..d_4) to octonion units is an arbitrary bijection. My test (`cubic.py`): among 10 other assignments of the same signed-permutation type, 7 give the same groups, but "α's to units 4–7, d's to units 0–3" gives V(N) = (1/27, √2/18, √3/18), V(Λ) = (1/27, √2/108, √3/54), quotient Z/3 ⊕ Z/6, and a random pair of permutations gives quotient Z/3 ⊕ Z/54. So the headline "Z/12" is not an invariant of (N, Λ) and not even of the discrete family of coordinate assignments; in my small sample it held when the real unit u_0 received an A_5 mean coordinate and failed when it received a D_4 coordinate (pattern from 11 cases only). Relabelings that transport all objects together (other origins f_i, octonion automorphisms) change nothing, trivially.
- **A full check must establish**: nothing more about correctness. If someone wants meaning: find a characterization of 𝓛 (for example by a property of the image 𝓛(N) ⊂ O^3 relative to the Albert cubic) that singles it out up to the stabilizer of the cubic; without that the result is a computation about one embedding.
- **Deserves a full check**: no (already reproduced; the open issue is meaning, not correctness). **Interest**: 1–2.

### D1-6
- **Title**: The cyclic isometry 𝓛: N⊗R → O^3 and the non-conjugacy of the two S_3 actions. **Type**: computation / expository.
- **Where**: `R\es_niemeier_triality_bridge.tex` l. 50–119, 323–426.
- **Statement**: 𝓛 r = c 𝓛, r N = N; the triality section <R̂, Ĥ> ⊂ O(N) acts on V_N as 7·1 ⊕ 5·sgn ⊕ 6·Std while the Albert frame S_3 acts on O^3 as 1 ⊕ 7·sgn ⊕ 8·Std, so no linear map conjugates them; the subgroup of Spin(8) preserving 𝓛(N) is finite; the element r has trivial discriminant action on N but cycles the three sectors.
- **Support**: short proofs (traces 2, 6 versus −6, 0). VERIFIED (ledger TRIALITY-EXACT-CARRIER-MAPS / morphism NIEMEIER-LEECH-TRIALITY-MORPHISMS-20260906).
- **What it adds**: a negative result inside the lane: the D_4-triality of the glue (quotient GL_2(F_3) → S_3) is not the triality of the three octonion sectors under this embedding. Not searched.
- **First assessment**: correct (trace count checked by hand: R̂ has trace 0 + 5 − 5 + 2 = 2). It documents that the "triality bridge" identifies two different S_3's only by name.
- **A full check must establish**: nothing.
- **Deserves a full check**: no. **Interest**: 1.

### D1-7
- **Title**: Wilson's octonionic Leech lattice in explicit matrices; cyclic fixed lattice √3E_8, coinvariant A_2 ⊗ E_8, glue F_3^8; "literal intersection" with 𝓛(N) and 𝓛(Λ). **Type**: new proof or restatement of a known result / computation.
- **Where**: `R\es_niemeier_wilson_cyclic.tex`, wcl:thm:Leech (l. 246–286), wcl:thm:fixed-coinvariant (l. 319–374), l. 376–432, l. 434–548, wcl:thm:literal-intersection (l. 688–783), l. 815–856.
- **Statement**: (a) Λ_W = {(x,y,z) ∈ L^3 : x+y, x+z, y+z ∈ L s̄, x+y+z ∈ L s} with norm (1/2)ΣN is even unimodular of minimum 4 (Wilson 2009; reproved). (b) For the cyclic shift: fixed lattice {(n,n,n) : n ∈ L s} with Gram 3G_{E8}; orthogonal complement {(m_1,m_2,−m_1−m_2) : m_i ∈ L s̄} ≅ A_2 ⊗ E_8; Λ_W/(F ⊕ C) ≅ L s/3L s ≅ F_3^8 with explicit glue map f(a) ↦ γ(a). (c) A_4 × (C_7 ⋊ C_3) (order 252) preserves the lattice and the cubic τ; the transposition of two sectors and Wilson's r_t do not preserve τ (explicit lattice vectors, τ = ∓8, ∓16). (d) In the fixed frame, Λ_cyc ∩ 𝓛(N) = Λ_cyc ∩ 𝓛(Λ) = {√2(a,a,a) : a ∈ D_4 ⊂ span(1,i,j,k)}, rank 4, Gram 6G_{D4}, det 5184, minimum 12; τ on it equals 2√2·P(a).
- **Support**: written proofs; checker `E\lattice_foundation_20260906\wilson\check_wilson.py` (PASS). VERIFIED.
- **What it adds**: (a) is Wilson; (b) is the known decomposition of the Leech lattice under an order-3 element with 8-dimensional fixed space (not searched specifically; the lattices √3E_8 and A_2 ⊗ E_8 inside Leech are standard, e.g. in the Griess–Lam papers that my search returned); (c) not searched; (d) has no canonical meaning: the intersection of two rank-24 lattices placed by two unrelated choices. It has rank 4 because 𝓛(N) has coordinates in Q + Q√2 or Q + Q√3 and Λ_cyc has coordinates in Q√2; the argument is linear independence of 1, √2, √3. The coincidence det = 5184 = det R_ES is 6^4·det D_4 against 6^4·4, an accident of the scale 6.
- **First assessment**: proofs read correctly; I did not recompute the Wilson side. "Not commensurable in the retained embedding" is a statement about the embedding.
- **A full check must establish**: only if (c) is wanted: the full stabilizer of the cubic in Aut(Λ_W) (the file gives a subgroup of order 252 and does not claim it is everything).
- **Deserves a full check**: no. **Interest**: 1–2 (the question in (c), the stabilizer in Co_0 of Wilson's trilinear form, is a well-posed side question; interest 2).

### D1-8
- **Title**: The exact image of P(a) = a_0(a_0^2 − 3(a_1^2 + a_2^2 + a_3^2)) = Re(a^3) on the D_4 lattice of quaternions, with integral and local sections. **Type**: new result (elementary) / computation.
- **Where**: `R\common_d4_image.tex`, d4i:thm:complete-image (l. 123–172), d4i:thm:local-images (l. 247–320), l. 322–443; preceded by `es_niemeier_wilson_cyclic.tex` l. 849–856 ("12√2 is generated but not attained").
- **Statement**: P(D_4) = 18Z ∪ (6Z+2) ∪ (6Z−2) = {n even : 3 ∤ n or 9 | n}; a section is n = 18h ↦ (−3h, h+1, h−1, h), n = 2(3r+ε) ↦ (−3r−ε, r, r, r+ε). Locally P(D_4 ⊗ Z_2) = 2Z_2, P(D_4 ⊗ Z_3) = Z_3^× ∪ 9Z_3, P = Z_p for p ≥ 5, so an integer is represented iff it is represented everywhere locally. On the slice Σa_i = 0: P(−3w−u−v, w+u, w+v, w) = 2(3w+u+v)(u^2 − uv + v^2). The additive group generated by the values is 2Z, so 6 lies in the generated group and is not a value.
- **Support**: complete elementary proof (read in full, no gap seen); checker. VERIFIED in summary. My brute force agrees (residues mod 18; P = 6 not attained).
- **What it adds**: a complete small result. It is the image of Re(a^3) on a rank-4 lattice; the proof is three explicit lines on which the quadratic factor is constant (−2 or −6). Literature: not searched.
- **First assessment**: correct. Its relevance to the rest depends on the "literal intersection" of D1-7, which is choice-dependent; as a standalone exercise it is fine.
- **A full check must establish**: nothing (the proof is ten lines of algebra).
- **Deserves a full check**: no. **Interest**: 1–2.

### D1-9
- **Title**: The Cheng–Duncan–Harvey shadow of A_5^4 D_4 in the marked coordinates: Ω^X = 5I_12 + J, twisted matrices from the glue group, determinant character of the theta representation, and the map to T_6 with T_6(W_6τ) = 72/T_6. **Type**: new proof or restatement of a known result / computation.
- **Where**: `R\niemeier_umbral_shadow.tex` (whole file), 6 Sep 2026.
- **Statement**: Ω^X = 4Ω_6(1) + (Ω_6(1) + Ω_6(3)) = 5I_12 + J, J_{rs} = 1_{s ≡ 5r (12)}; on the odd part M^X = [[5,0,0,0,1],[0,4,0,0,0],[0,0,6,0,0],[0,0,0,4,0],[1,0,0,0,5]]; twisted M_g^X with entries a_g+1, b_g, a_g+c_g, b_g, a_g+1 and corners s_g; det F_+ = −i, det U(T) = e(1/12), det U(S) = e(−3/12), det U(γ) = e(−χ(γ)/12) with χ(T) = −1, χ(S) = 3 (the multiplier of η^2); reduction Z/12 → Z/6 is a quadratic similitude of multiplier 10 onto the A_5 discriminant form; S_840 → O(N) → O(N)/W is trivial; with π_X = −5[1] + [2] − [3] + 5[6], T_6 = η(τ)^5 η(3τ)/(η(2τ)η(6τ)^5): f^X := 1 + Σ α_{n mod 6} n q^n/(1−q^n) (α = (0,5,4,6,4,5)) = −q d/dq log T_6 = 5λ_6 + λ_2 − λ_3; T_6(−1/(6τ)) = 72/T_6(τ); f^X|_2 W_6 = −f^X; J_6 = T_6 + 5 + 72/T_6, Y_6^2 = (J_6−5)^2 − 288.
- **Support**: direct proofs for each identity; checker `E\spectral_umbral_period_20260906\check_shadow.py` (exact arithmetic in Q(ζ_24)). VERIFIED in the summary; the file states that no new moonshine statement is made.
- **What it adds**: a specialization of CDH (arXiv:1307.5793, §§3–5), credited. Classical: T_6 is a Hauptmodul of Γ_0(6) and T + 5 + 72/T one for Γ_0(6)+6. I did not search for the determinant-character computation; it is the statement that the determinant of the 12-dimensional Weil representation of Z/12 is the η^2 character.
- **First assessment**: correct in the places I checked (det U(T): Σ r^2 = 506, 506/24 ≡ 1/12; the α identity; T_6·T_6∘W_6 = 72 numerically). A general remark the file does not make and that explains "the original scalar 72": for a Coxeter frame shape π = Σ a_d [d] of a root system R one has Π d^{a_d} = det(1 − Coxeter element) = det(R), a_{h/d} = −a_d and Σ a_d = 0, so the eta quotient T^X = Π η(dτ)^{−a_d} satisfies T^X(W_h τ)·T^X(τ) = Π d^{a_d/2} = sqrt(det R_X) = [N : R_X]. So **for every Niemeier root system the Fricke constant of the CDH eta quotient equals the order of the glue code** (2^12 for A_1^24, 3^6 for A_2^12, 72 here, ...; table computed in `es.py`). This is a two-line proof; I expect it is implicit in CDH and known, not searched.
- **A full check must establish**: comparison of the twisted formulas (l. 478–499) with CDH §5.1 in the exceptional m = 6, D_4 case (I did not open CDH to compare); the section comparison l. 437–476.
- **Deserves a full check**: no (known machinery). **Interest**: 2.

### D1-10
- **Title**: Erdős–Straus two-channel divisor selector, its shear to the S6 terminal relation matrix, the factor-form criterion, and the "affine gate" theorem. **Type**: new proof or restatement of a known result, with one small new lemma; the S6 link is formal.
- **Where**: `R\erdos_straus_koide_s6_bridge.tex` (thm:esksb-bridge l. 394–466; (4.1)–(4.6) l. 599–684; thm:esksb-affine-gate l. 814–875; descendant maps l. 882–985); shorter version `R\erdos_straus_selector_crosswalk.tex`; ledger S6-ES-SELECTOR-CROSSWALK.
- **Statement**: p ≡ 1 mod 12 prime, R_j = 4j+3, a_j = (p+R_j)/4, 0 ≤ j < (p−1)/4. (i) In a sorted solution of 4/p = 1/x+1/y+1/z, p/4 < x ≤ p/2, so x = a_j for a unique j. (ii) W_ε(p,j) = {u > 0 : u | a_j^2, R_j | 4u + p^ε} (ε = 0: E-channel; ε = 1: M-channel); ES(p) ⇔ some W_ε(p,j) ≠ ∅; solution (a_j, pK, p^ε a_j K/u), T = (4u+p^ε)/R_j, K = (p^{1−ε}T+1)/4. (iii) Θ(j,u) = (j, (T+1)/4, u − jT) is a bijection onto {(j,l_0,l_1) : 12l_0 − 4l_1 − 3 = p^ε, 4l_0−1 > 0, u := l_1 + j(4l_0−1) > 0, u | a_j^2}, and [[1,−j],[0,1]]·[[R_j,−u],[4,−T]] = [[3,−l_1],[4,1−4l_0]]. (iv) With u = r^2 s, a_j = rst, gcd(r,t) = 1: u ∈ W_0 ⇔ R_j | pr + t; u ∈ W_1 ⇔ R_j | r + t; p is a counterexample iff R_j ∤ pr+t and R_j ∤ r+t for all j and all such factorizations. (v) Affine gate: for p = 12m − 11, the point (l_0,l_1,l_2) = (m,2,1), u_j = 2 + j(4m−1): u_j | a_j^2 ⇔ (j = 0 and 2 | m) or (j = 2 and 8 | m); so this point yields a solution exactly when p ≡ 13 mod 24, namely 4/p = 1/(3m−2) + 1/(pm) + 1/(pm(3m−2)/2). (vi) Descendant maps along p_b = bp + (b−1)R.
- **Support**: complete elementary proofs; marks \Verified. My script: censuses agree with the table in the p = 1201 file; (v) has no violation for m < 400.
- **What it adds**: about the Erdős–Straus conjecture nothing is proved; the file says so (l. 1019–1023). (i)–(ii) and (iv) are the classical parametrization of solutions for prime denominators: the E/M channels are the solutions with exactly one, respectively two, denominators divisible by p (Type I / Type II in Elsholtz–Tao, arXiv:1107.1010; I confirmed the paper but not the exact numbering of their parametrization; Mordell's book has the same divisor formulation). (iii) is the row-shear identity of section 0. (v) is a small exact lemma I have not seen stated; its content is that this one terminal point, sheared through all shells, yields a solution exactly for p ≡ 13 mod 24; that class is not ≡ 1 mod 24 and is covered by the classical identities, as the file itself says (l. 40–42), so it adds no new residue class.
- **First assessment**: correct, elementary, honest about scope. The phrase "stronger than a shared determinant" (l. 1019) is true but small: any matrix [[R,−u],[4,−T]] with R ≡ 3 mod 4 has the same row lattice as one with first column (3,4).
- **A full check must establish**: nothing mathematical; for attribution, the exact correspondence with Elsholtz–Tao's Type I/II parametrization and with Mordell.
- **Deserves a full check**: no. **Interest**: 1–2.

### D1-11
- **Title**: Fixed-shell divisor counts: reduced-shell bijection, raw versus unordered counts (correction of the ES source note), non-descent modulo 840 (A_3(2521) = 0, A_3(3361) = 6), and the lattice-valued count vector. **Type**: correction of the (internal ES) literature / computation.
- **Where**: `R\es_niemeier_shared.tex`, esn:thm:shell-bijection (l. 976–1035), esn:thm:raw-channels (l. 1054–1132), esn:thm:non-descent (l. 1137–1222), esn:thm:residue-cocycle (l. 1237–1278), esn:thm:sample-fourier (l. 1298–1366); provenance file section "two-channel wording".
- **Statement**: For p ≡ 1 mod 24 prime, R ≡ 3 mod 4, a = (p+R)/4, g = gcd(R, pa), R_0 = R/g, N_0 = pa/g: {d > 0 : d | N_0^2, d ≡ −N_0 mod R_0} ↔ ordered (b,c) with 4/p = 1/a + 1/b + 1/c, d ↦ ((N_0+d)/R_0, (N_0+N_0^2/d)/R_0). Unordered count U_R(p) = (A_R(p) + δ)/2, δ = 1 iff R_0 | 2. If gcd(R,pa) = 1, p ∤ a: A_R(p) = c_R(a;−1) + 2c_R(a;−p^{−1}) (this is the raw count; the source note called it the count after identifying complementary divisors). 2521 ≡ 3361 ≡ 1 mod 840, A_3(2521) = 0 (a = 631 prime, ≡ 1 mod 3), A_3(3361) = 6 (a = 841 = 29^2, 29 ≡ −1 mod 3), 4/3361 = 1/841 + 1/974690 + 1/28266010. b(r) = e_r − e_1 is a 1-cocycle S_840 → N for the residue action; Q_{R,P} = 6W − Mu ∈ A(S_840) ⊂ N for a finite prime sample P.
- **Support**: complete elementary proofs; checker; my script confirms the counts and the identity.
- **What it adds**: **what is proved is bookkeeping, not a statement about the Erdős–Straus conjecture.** A_3(2521) = 0 says only that 4/2521 has no decomposition with first denominator 631; 2521 has 12 selector states on other shells (my census: 6 E, 6 M, 9 unordered solutions). The point of the theorem is internal to the user's ES corpus: the number of solutions on a fixed shell R is not a function of p mod 840, so any "function on the 24 residues" (hence any lattice vector in N built from residues alone) cannot record shell counts; the count vector Q_{R,P} needs the actual primes. The correction of the two-channel wording is a correction of that corpus's April 2026 note (not of published literature).
- **First assessment**: correct and trivial in the good sense. The cocycle b(r) = e_r − e_1 = ρ(r)e_1 − e_1 is the coboundary of the vector e_1 of the ambient permutation module Z[V_840] (e_1 itself is not in N); it has no content beyond notation.
- **A full check must establish**: nothing.
- **Deserves a full check**: no. **Interest**: 1.

### D1-12
- **Title**: The fifteen ES selector states at p = 1201 span a 3-dimensional corner of Herm_3(H), and the count 15 is not stable. **Type**: computation (negative result).
- **Where**: `R\p1201_selector_jordan_bridge.tex` (thm:fifteen-span l. 194–219; table l. 224–231); `E\p1201_selector_jordan_bridge_20260905\REPORT.md`.
- **Statement**: The 15 marked states s = (χ,R,h,r,t) at p_0 = 1201 map to rank-one matrices h(r,t)^T(r,t) in Sym_2(R) ⊂ Herm_3(H); their span and Jordan closure are Sym_2(R), of dimension 3. #(E ⊔ M) = 15, 54, 36, 29 for p = 1201, 4561, 8761, 9601 (all ≡ 361 mod 840). The 15 states lie on a conic, so no three are collinear, which excludes an incidence identification with PG(3,2).
- **Support**: direct computation; verification script; my census agrees with all four columns (including the unordered counts 11, 40, 26, 23).
- **What it adds**: it disposes of a numerological suggestion (15 = dim Herm_3(H)) by exact computation. No mathematics beyond that.
- **First assessment**: correct. Worth recording only as an example of the workbench testing and rejecting a coincidence.
- **A full check must establish**: nothing.
- **Deserves a full check**: no. **Interest**: 1.

### D1-13
- **Title**: Open questions isolated by these files that are well posed for an outside mathematician. **Type**: open question isolated.
- **Where**: as indicated per item.
- **Statement**:
  1. (From D1-1; my formulation.) Identify the lattice J (rank 24, det 3^4, minimum 4, J^∨/J hyperbolic over F_3, eight unimodular overlattices = six Leech + two A_2^12): its automorphism group, its kissing number, and the Co_0-orbit of the corresponding totally isotropic plane of Λ/3Λ. How many Co_0-orbits of such planes are there, and which Niemeier lattices occur among the overlattices in each?
  2. (From D1-4; my side observation.) For a Niemeier lattice N with Coxeter number h and Weyl vector ρ and a divisor d of h, is vois_d(N; ρ) always the Niemeier lattice whose root system has Coxeter number h/d (here d = 2: A_2^12, d = 3: A_1^24, d = 6: Leech)? Presumably known or easy from the height filtration of roots; needs a reference or a proof for all 23.
  3. (cubic arithmetic l. 439–490; wilson l. 485–489.) The stabilizer of Wilson's trilinear form Re((xy)z) in Aut(Λ_W) ≅ Co_0: the file exhibits A_4 × (C_7 ⋊ C_3) of order 252 and shows the r_t are outside; the full stabilizer is not determined.
  4. (triality bridge l. 224–229; D1-5.) Is there an isometric embedding of N(A_5^4 D_4) (or of any Niemeier lattice) into O^3 distinguished by its relation to the Albert cubic, for example one on which 2F is integer valued, or one maximizing the stabilizer of the cubic in O(N)? The files compute value groups for one embedding and do not pose this; without such a characterization the value groups of D1-5 have no intrinsic meaning.
  5. (p1201 file l. 310–322.) The "decisive higher-rung test" (a marking-to-conjugation map into a quaternionic structure group) is described and not defined; as posed it is not yet a mathematical question.
  6. (bridge (4.5).) The factor-incidence form of the Erdős–Straus conjecture for p ≡ 1 mod 24: for some j and some factorization a_j = rst with gcd(r,t) = 1, R_j | pr + t or R_j | r + t. This is the conjecture itself in classical dress, not a new question.
- **Support**: n/a.
- **What it adds**: items 1–4 are lattice-theoretic questions independent of S6.
- **First assessment**: item 1 is the most concrete; items 2 and 3 are quick literature or computer-algebra tasks (Magma/GAP).
- **A full check must establish**: n/a.
- **Deserves a full check**: maybe (items 1–2 are cheap to settle with a computer algebra system and a look at Chenevier–Lannes and Borcherds' thesis). **Interest**: 2–3.

## 3. Doubts and errors

1. **No error found in the lattice statements.** Everything I recomputed agrees (section 1, "My own exact checks").
2. **Presentation risk: the number 12.** The summary texts (`es_niemeier_shared.tex` l. 19–21; `mathematical_summary.tex` l. 57–74; ledger NIEMEIER-LEECH-EXACT-NEIGHBOR) put the value-group quotient Z/12 next to the other twelves. The quotient is specific to one coordinate assignment (D1-5: other assignments of the same kind give Z/3 ⊕ Z/6 and Z/3 ⊕ Z/54). The detailed file says "frame-dependent"; the summaries say "in this fixed frame" but a reader will take Z/12 as structural. Similarly Λ/R_0 ≅ Z/12 ⊕ (Z/6)^2 is true and is bookkeeping (12 = 2·6 because 6v ∈ K has order-2 glue).
3. **"Literal intersection" with Wilson's lattice** (wcl:thm:literal-intersection) is presented with Gram matrix, determinant 5184 and a complete cubic image, which gives weight to an object that exists only because of the two chosen placements. The equality det = 5184 = det R_ES is not explained and is a scale accident (6^4·4 in both cases for different reasons).
4. **The S6 link is overstated by the titles only.** "The exact marked Erdős–Straus–S^6 bridge" and "...Koide S6 bridge" suggest geometry; the bodies deny it correctly. The file name `erdos_straus_koide_s6_bridge.tex` promises Koide content that is not in the file.
5. **Symbol collisions** (hazard for a checker, not errors): M is the A_2^12 lattice (esrf, jmv), N + Λ = K^∨ (esnl NL15), and the mean octonion (nca); J is the common lattice, the matrix Ω_6(3) (nus), a Jordan algebra (esn l. 537, p1201), and J_p an index set (bridge); ρ is the Weyl vector (esnl, nca) and the residue representation (esn, esrf, where the Weyl vector is ϱ); β is the Legendre map (esn l. 55), the ternary coordinate (esrf RF12) and exponent vectors (esn l. 1042); τ is the binary map (esn l. 632), the cubic (wcl) and the modular variable (nus); R is a root lattice, the shell modulus, a reflection matrix; L is a lattice, L = (p−1)/4, L_s, and 𝓛.
6. `es_niemeier_shared.tex` l. 1368–1371: the comment says the `esn:fa:` fragment is to be input "after esn:thm:gl2-full-lattice-lift and before the shell subsection"; it sits after the Fourier theorem. Harmless (it restates ρ).
7. The evidence copy `E\es_niemeier_20260905\es_niemeier_shared.tex` (77,230 bytes) is older than the research copy (79,366 bytes); FINAL_SOURCE_RECEIPT hashes there refer to the older text. The later modules (leech, cubic, fixed neighbour, JM, Wilson, d4 image, shadow) have their own evidence folders dated 6 Sep.
8. `WEB_PRO_TRIALITY_LEECH_FEEDBACK_20260906.md` is named "feedback" but is an outgoing handoff; there is no record in my assigned files of an answer from the Pro model on the lattice claims, so "VERIFIED" here means: written proof plus the workbench's own exact scripts (and now my recomputation for the items listed).
9. esn:thm:residue-cocycle: the "actual residue cocycle" b(r) = e_r − e_1 is the coboundary of e_1 (not in N, but in the ambient permutation module), so it carries no cohomological information; the text does not claim otherwise but the heading suggests more.
10. nus l. 543–553 (SL_2(Z) → Z/12 → Z/6 → S_840): correct as a composite of defined maps; the middle identification is a marking. The text calls these "explicit different outgoing morphisms from the same marking", which is accurate.
11. Attribution: the neighbour construction is credited to Conway–Sloane and Borcherds; Chenevier–Lannes (Thm 4.2.10, Prop. 4.2.11: HC(L;ρ) = vois_h(L;ρ)) is the modern reference and is not cited. The standard splitting O(N) = W ⋊ Stab(chamber) is not mentioned where esn:fa:thm:full-quotient is presented as "the exact full automorphism quotient".

## 4. Not read

- `R\higher_rung_24d_continuation.tex` (304 KB): not in my list; I read its introduction (l. 1–90), the summary theorem h24:thm:exact-numerical-boundary (l. 6139–6180) and grepped it for references to the lattice lane, to answer the first question. Ledger entries TRIALITY-EXACT-CARRIER-MAPS-20260906 and RETAINED-THREEPLANE-TRIALITY-20260906 point into that file; I read the entries, not their proofs (h24:rettri:*, h24:fc:collapse).
- `E\period_lattice_continuation_20260906\jm_cubic\` (cited by the JM file): not in my list; I recomputed the J/M value groups myself instead.
- `E\p1201_selector_jordan_bridge_20260905\LOGBOOK.md`, `natural_span_results.json`, `verification_output.txt`: only the REPORT head was read; the TeX file there is identical to the research copy.
- Checker scripts (`*.py`) in the evidence folders: outputs and JSON read, source code not read line by line.
- JSON receipts (build, layout, visual QA) in the evidence folders: passed over as build records.
- The Wilson-side matrices (S, T, U_t, the membership matrix (wcl:eq:quaternion-membership-matrix)) were read but not recomputed.
- Literature not opened: CDH §5.1 (twisted shadow formulas), Borcherds' thesis, Conway–Sloane ch. 16/24 (cited from memory), Elsholtz–Tao full text (Type I/II correspondence stated from memory; the search confirmed only the paper).
