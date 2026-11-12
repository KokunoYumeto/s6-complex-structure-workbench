# Reader E — the "higher rung" continuation of the S6 workbench

Reader: Claude Fable 5.2. Date of reading: 12 Nov 2026. Read only; one scratch folder `work\scratch\E\`
(two small sympy scripts).

Abbreviations: `W\` = `C:\Users\user\Documents\math\research\s6_recent_results_main\canonical_S6_snapshot\supporting_materials\workbench\research\`,
`R\` = `...\canonical_S6_snapshot\`, `EV\` = `...\supporting_materials\workbench\evidence\`.
All files carry the file-system date 29 Sep 2026 00:32 (snapshot copy); internal dates are 3-6 Sep 2026.

Short answer to the assignment, before the details:

- Nothing in these files constructs a new compact complex manifold. The "higher torus wrap" is a local object:
  the Mumford degeneration of a 3-torus over a disc (smooth fourfold `N_3 -> Delta`, cusp fibre `W_3` with
  `chi = 6`), a holomorphic map of cusp families `N_3^C -> N_0` onto the cusp neighbourhood of `X`, and integral
  affine lifts of the order-3 and order-4 monodromies. The workbench records the global gluing as OPEN and
  shows the result could not be `S^8` (`chi = 6`, and `S^8` is not almost complex).
- I believe the open gluing step is closed in a few lines by a fibre product with the rational elliptic
  surface that Engel starts from (candidate E-2); the result is a compact complex fourfold with `chi = 6`,
  simply connected, not sphere-like (`b_2 >= 2`).
- The Euler number 6 that the workbench treats as "the obstruction" is exactly the smallest value allowed by
  Hirzebruch's congruence for an almost complex 8-manifold with `c_1 c_3 = 0`, and there is a 3-connected
  almost complex 8-manifold with `chi = 6`: `3 HP^2 # (-HP^2)` (Mandal, arXiv:2609.27929, Sept 2026). Whether a
  rank-three analogue of the [AC26]/[E26] construction puts a complex structure on it is a well-posed question
  that nobody in these files asks (candidate E-3, written out as a prompt).
- The lattice / Gram-cone / torsor / Lorentz files are correct-looking finite-dimensional linear algebra with no
  map from the threefold `X` other than through the cusp's angular lattice matrix `P`; details in E-7 to E-11.

---

## 1. Reading notes

### 1.1 `W\higher_rung_24d_continuation.tex` (303,964 bytes, 7,376 lines) — "mechanically generated from s6_higher_rung_24d_preprint.tex"
Label prefix `h24:`. Read in full: l.1-1445 (source data, obstructions, toroidal successor, sphere ladder),
l.6134-6200 and the bibliography. All theorem-like statements read (extracted by script) for l.1445-4376,
5112-5750, 6187-7199; proofs there only sampled. l.4376-5112 and 5752-6134 are reader C1's block (C1-3, C1-7),
not reread. l.6184-7199 ("ES-NIEMEIER HOST-ONLY INPUT": Albert orbit quotient, Cartan family, spectral map of
the common lattice) belongs to reader D1's topic; statements listed only.

Sections and main labelled statements:
- l.30-180 source data: monodromies `T_1,T_2` (eq. `h24:eq:original-T`), period matrix, twists
  `(l_0,l_1,l_2) = (0,1,-1)`; matrices `P, R, C, X_P` (`h24:eq:marked-P`); Definition `h24:def:feature-ledger`
  (F1)-(F8) "full higher toroidal wrap" (what a literal analogue would have to supply); the required diagram
  `h24:eq:required-diagram` (0 -> K_Z -> Lambda~ -> Lambda -> 0 over periods).
- l.181-334 "Sphere and Euler obstructions": Thm `h24:thm:s8-obstruction` (no almost complex structure on a
  homotopy `S^8`, signature proof), Thm `h24:thm:all-higher-spheres` (none on homotopy `S^m`, `m > 6`; Bott
  integrality / Borel-Serre), Prop `h24:prop:euler-mismatch` (`chi(W_3) = 6`, so the three-fibre pattern gives
  `chi = 6`), Cor `h24:cor:euler-repair` (an `S^8` carrier needs other fibres with Euler sum `-4`), a remark.
- l.335-774 "The exact toroidal successor over the cusp": Thm `h24:thm:lattice-quotient`
  (`Phi = P (+) Q: Z^6 ->> Z^4`, kernel `Z(k,0) (+) Z(0,k)`, `Phi M_3 = M_F Phi`, `c_F Phi = Q c_3`);
  Thm `h24:thm:elliptic-extension` (`Z_3 = s I_3 + S C_2(t) Q`, `P Z_3 = Z_2 Q`, kernel `E_s = C/(Z + sZ)`);
  Prop `h24:prop:toric-filling-map` (Kuhn fan -> `A_2` fan, quotients `N_3^C -> N_0`, proper discontinuity);
  Lemma `h24:lem:cusp-basis-identification` (`M_3 ~ M_F (+) C_0` over `SL_6(Z)`);
  Prop `h24:prop:finite-lift` (`A~_j = A_j (+) C_j`, free affine lifts); Remark "Exact endpoint" (l.762-773):
  global gluing not constructed.
- l.775-1404 "The forced S^9, S^10 and rank-loss S^8": Thm `h24:thm:orbit-invariants`, Lemma `h24:lem:K3-ball`,
  Thm `h24:thm:sphere-ladder`, Props `h24:prop:U3-ball`, `h24:prop:S9-join`,
  `h24:prop:spectral-floor-observation`, Cor `h24:cor:residual-circle`, Thm `h24:thm:O9-fibres`,
  Prop `h24:prop:Gram-square`, Cor `h24:cor:S9-cusp-limit`, Thm `h24:thm:strongest-gram`. Same mathematics as
  `higher_rung_su3_triple_s8_cone.tex` (1.8).
- l.1406-3576 "The 24-dimensional octonionic flag": Thms `h24:thm:octonionic-triality`,
  `h24:thm:octonionic-cohomology` (both attributed to Mare-Willems 2013), Prop `h24:prop:two-Coxeter-systems`,
  Thm `h24:thm:Kuhn-octonionic-comparison` (bijection of two 6-element `S_3`-sets), Prop
  `h24:prop:complex-flag-embedding`, Thm `h24:thm:octonionic-determinant-S24`, Props `h24:att:prop:peirce`,
  `:norm-inverse`, `:determinant`, Thm `h24:att:thm:stabilizer`, Prop `h24:att:prop:linear-stabilizer`,
  Thm `h24:tri:thm:spectral-graph`, Lemmas `h24:fc:cartan-inverse`, `h24:fc:finite-exponential`,
  Thm `h24:fc:open-cell`, Prop `h24:fc:orientation`, Thm `h24:fc:collapse`, Cors `h24:fc:boundary-composite`,
  `h24:fc:no-reverse-degree`, Prop `h24:prop:three-24d-objects`.
- l.3577-4375 "What the mod-12 and mod-24 arithmetic actually is": Thm `h24:thm:peripheral-moduli`, Props
  `h24:prop:cusp-diagonal-modulus`, `h24:prop:no-modulus-from-cohomology-or-determinant`, Thm
  `h24:thm:stable-12-to-24`, Prop `h24:prop:generator-free-bridge`, Thm `h24:thm:cusp-g-zero` (the one-copy cusp
  map is null; reader C1's C1-4), Cor l.4347.
- l.4376-6137 block `RETAINED_ANGLE_AND_HOPF_BRIDGE_20260905` (C1), inside it l.5112-5750
  `h24:rettri:*`: Thm `h24:rettri:bundleclass`, Thm `h24:rettri:subgroup`, Prop `h24:rettri:forgetting`.
- l.6139-6182 Thm `h24:thm:exact-numerical-boundary` (summary of the numerology tests).
- l.6184-7199 host-only Albert/Cartan/common-lattice block (labels `h24:ocb:*`, `h24:ncs:*`).
- l.7201-7376 bibliography.

Status marks: the file itself has none; `W\status.tex` l.2731-2810 marks the toroidal successor "Verified" and
"the global period-and-overlap gluing over both finite-order discs remains Open"; l.3025 marks the literal
complex `S^8` "Refuted".

### 1.2 `R\s6_higher_rung_24d_preprint.tex` (301,399 bytes, 7,471 lines; dated "6 September 2026")
Title "Retained cusp topology, triality morphisms, and the marked Niemeier-Leech construction"; "Standalone
theorem note for the higher-rung search". Same text as 1.1: equal counts of theorem (25) and proposition (22)
environments, the same section sequence with the preprint's line number = continuation line + 93 (30 -> 123,
4378 -> 4471, 6134 -> 6227); sections are one level higher and labels have no `h24:` prefix. It has in addition
a title and a long abstract (l.36-121) which is mostly about the lattice results (reader D1). Not read twice.

### 1.3 `W\higher_rung_fourfold_toric_degeneration.tex` (38,239 bytes, 1,063 lines) — read in full
Label prefix `hrftd:`. Sections: baseline of the threefold cusp; rank-three periodic fan (Lemma
`hrftd:lemma:unimodular`, Prop `hrftd:prop:four-branch`: `t = z_0 z_1 z_2 z_3`); analytic quotient (Thm
`hrftd:thm:toroidal-cusp`); monodromy (Prop `hrftd:prop:cusp-monodromy`: `pi_1(N_3) = Z^3`); central fibre
(Thm `hrftd:thm:strata`, Thm `hrftd:thm:normalization`, Remark, Cor `hrftd:cor:euler-shear-determinant`);
obstructions (Thm `hrftd:thm:euler-obstruction`, Thm `hrftd:thm:no-almost-complex-s8`); a diagonal monodromy
candidate and Prop `hrftd:prop:finite-fixed-points`; "replication requirements" (Prop `hrftd:prop:van-kampen`,
Thm `hrftd:thm:mv-criterion`, Wang sequence); Hermitian boundary (Prop `hrftd:prop:hermitian-compactification`,
Thm `hrftd:thm:hermitian-not-snc`); conclusion.

### 1.4 `W\higher_rung_toroidal_elliptic_bridge.tex` (36,927 bytes, 1,105 lines) — read in full
Labels `teb-*`, equations (TEB.1)-(TEB.55). Prop `prop:teb-fan-morphism`, Thm `thm:teb-local-lattice-bridge`,
Thm `thm:teb-holomorphic-cusp-bridge`, Prop `prop:teb-explicit-conjugacy`, Prop
`prop:teb-finite-monodromy-lift`, Prop `prop:teb-weyl-chambers`, Thm
`thm:teb-hermitian-determinant-splitting`, Prop `prop:teb-theta-order-lift`, an audit record (3 Sep 2026),
Thm `thm:teb-no-gram-identification`, and "The remaining global problem" (l.1057-1105). This is the earlier,
fuller source of 1.1 l.335-774 (same matrices, same proofs).

### 1.5 `W\higher_rung_s8_constraints.tex` (29,222 bytes, 715 lines; header date 2026-09-03) — read in full
Label prefix `hrs8:`. No theorem environments; boxed statements. Subsections: no almost complex structure on a
homotopy `S^8` (three arguments); requirements for a real `T^6`-fibration `S^8 -> S^2`; Euler constraint;
`pi_1` and monodromy; Mayer-Vietoris / Wang / Serre tests; torus-rank bound and `S^8/T^4 = B^4`; Gram quotient
with boundary `S^8`; `SU(3)` bundles on the regular locus `U = X \ (W u S_1 u S_2)`; consequences; sources.

### 1.6 `W\higher_rung_rank_six_lattice.tex` (14,630 bytes, 355 lines) — read in full
Prefix `rsl:`. Thm `rsl:thm:s3-sequence`, Thm `rsl:thm:three-sixes`, Prop `rsl:prop:gram-scope`, audit record.

### 1.7 `W\higher_rung_rank_nine_matrix_torsor.tex` (15,420 bytes, 409 lines) — read in full
Prefix `rnmt:`. Thm `rnmt:thm:regular-torsor`, Thm `rnmt:thm:pair-kuhn-weyl`, Prop
`rnmt:prop:marking-boundary`, Prop `rnmt:prop:representation-bridge`, audit record.

### 1.8 `W\higher_rung_su3_gram_cone.tex` (25,251 bytes, 708 lines) and `W\higher_rung_su3_triple_s8_cone.tex` (24,855 bytes, 885 lines)
Statements read in full, proofs sampled. Gram cone (2 columns): Thm `thm:hrgc-gram-quotient`, Prop
`prop:hrgc-stabilizers`, Thm `thm:hrgc-free-trivialization`, Prop `prop:hrgc-pluecker`, Thm
`thm:hrgc-s12-ball-quotient`, Thm `thm:hrgc-no-native-s4-sector`. Triple cone (3 columns): Thm
`thm:hr3c-u3-gram-classification`, Lemma `lem:hr3c-density-ball`, Cor `cor:hr3c-u3-unit-quotient`, Thm
`thm:hr3c-u3-compactification`, Thm `thm:hr3c-su3-invariants`, Thm `thm:hr3c-su-unit-sphere`, Thm
`thm:hr3c-su-full-cone`, Prop `prop:hr3c-rank-strata`, Thm `thm:hr3c-rank-loss-pair`, Cor
`cor:hr3c-residual-circle`, Thm `thm:hr3c-two-ladders`. The first file states at its head that it "isolates
the part ... that is independent of the candidate complex threefold".

### 1.9 `W\higher_rung_lorentz_observation_bridge.tex` (31,339 bytes, 927 lines)
Prefix `hlob:`. Statements read in full; l.674-927 read in full. Lemma `hlob:lem:splitting-identities`, Thm
`hlob:thm:split-observation`, Thm `hlob:thm:block-coordinates`, Thm `hlob:thm:lorentz-action`, Thm
`hlob:thm:cone-section`, Cor `hlob:cor:Y3-block-form`, subsection "holomorphic toric seed", Thm
`hlob:thm:colour-momentum`, a worldline action.

### 1.10 Evidence folders (reports only)
- `EV\higher_rung_24d_20260905\`: `MATHEMATICAL_LEDGER.md` (table of what is proved; ends "A completed global
  higher torus wrap remains open"), `AUDIT_OCTONIONIC_LOG.md` (an independent audit of the flag block; found two
  defects of statement, since repaired: the tangent space needs `d Xi_lambda`; restricted roots are
  `gamma_i/2`), `LITERATURE_LOCATOR_CORRECTION.md`, `WORKLOG.md` (contains the user's request: an analogue of
  the S6 object "on S8 or S9", and the "24-dimensional mod 24 or mod 12" idea), build receipts.
- `EV\exact_lorentz_observation_bridge_audit_20260904\`: `README.md`, `AUDIT_REPORT.md`, `CLAIM_LEDGER.md`
  (C01-C32). Verdict: C01-C22, C24-C26, C31 proved; C23 (the displayed first-order action as dynamics) and C32
  (global completion) REFUTED; C27 (a pointwise map from the toroidal total space to the phase-retaining
  carrier), C28 (the global analytic elliptic overlap cocycle through the finite fillings), C29, part of C30
  OPEN. "No packet theorem is novel relative to the current canonical tree."

### 1.11 Other places consulted
`W\status.tex` l.2655-3064 (the result map for this block; statuses quoted above); `claim_ledger_index.txt`
(the higher-rung toroidal statements have no ledger ids of their own; the Gram/Lorentz side appears as
S6-WPR-*, S6-Q444-*); Engel's text (section 1.2, 2, Remark 8.5); `C1_notes.md` (C1-3, C1-7).
No file in `W\` contains the word "conifold"; Engel's Remark 8.5 is not taken up anywhere in this block.

---

## 2. Candidates

### E-1. The rank-three toroidal cusp and its holomorphic quotient onto the cusp of `X` (local)
**Type**: computation / restatement of a known construction (Mumford 1972), with one new comparison map.

**Where**: `W\higher_rung_fourfold_toric_degeneration.tex` l.49-555 (`hrftd:thm:toroidal-cusp`,
`hrftd:prop:cusp-monodromy`, `hrftd:thm:strata`, `hrftd:thm:normalization`,
`hrftd:cor:euler-shear-determinant`); `W\higher_rung_toroidal_elliptic_bridge.tex` l.119-615
(`prop:teb-fan-morphism`, `thm:teb-local-lattice-bridge`, `thm:teb-holomorphic-cusp-bridge`,
`prop:teb-explicit-conjugacy`, `prop:teb-finite-monodromy-lift`); repeated in
`W\higher_rung_24d_continuation.tex` l.335-774. 3-5 Sep 2026.

**Statement**.
(a) Let `T_3` be the `Z^3`-periodic Kuhn triangulation of `R^3` (tetrahedra
`conv{m, m+e_{pi_1}, m+e_{pi_1}+e_{pi_2}, m+(1,1,1)}`, `pi in S_3`), `Y_3` the toric fourfold of the fan of
cones over `T_3 x {1}`, `t` the height character. `Y_3` is smooth, `t = z_0 z_1 z_2 z_3` in each chart,
`div(t)` is reduced. `Z^3` acts by `(x,t) -> (t^lambda x, t)`; on `Y_{3,eps} = {|t| < eps}` the action is free
and properly discontinuous, `N_3 = Y_{3,eps}/Z^3` is a smooth complex fourfold, `pi_3: N_3 -> Delta_eps` is
proper, the fibre over `q = e^{2 pi i tau} != 0` is `E_tau^3`. `pi_1(N_3) = Z^3`; monodromy
`M_3 = [[I,I],[0,I]]` on `(a_i; b_i)`; the fibre inclusion kills `a_i` and sends `b_i -> e_i`.
(b) The central fibre `W_3` is irreducible, with open strata indexed by cells of `T_3/Z^3`:
`(f_0,f_1,f_2,f_3) = (1,7,12,6)`, `chi(W_3) = 6`. Its normalization is the smooth permutohedral toric
threefold (14 boundary surfaces, 36 curves, 24 fixed points), glued 2:1, 3:1, 4:1 onto 7 double surfaces, 12
triple curves, 6 quadruple points. For a finite-index shear `B_0: Z^3 -> Z^3`:
`chi(W_{3,B_0}) = 3! |det B_0|`.
(c) With `P = [[1,-1,0],[0,1,-1]]`, `B_0 = [[0,1],[-1,0]]`, `Q = B_0^{-1} P = [[0,-1,1],[1,-1,0]]`,
`S = [[1,1],[0,1],[0,0]]`, `k = (1,1,1)`, and the cusp period `Z_2 = s B_0 + C_2(t)` of [AC26]
(`t = e^{2 pi i s}`, `C_2` bounded holomorphic): put `C_3 = S C_2 Q`, `Z_3 = s I_3 + C_3`. Then
`P Z_3 = Z_2 Q`, `Phi = P (+) Q: Z^3 (+) Z^3 ->> A_F (+) B_F` satisfies `Phi M_3 = M_F Phi` and
`c_F Phi = Q c_3`; `P` maps every Kuhn tetrahedron onto an `A_2` triangle, so it induces a toric morphism
`Y_3 -> Y_2` over `t`, equivariant for the twisted actions
`Psi^{(3)}_lambda(x,t) = (exp(2 pi i C_3 lambda) t^lambda x, t)`, `Psi^{(2)}_mu(y,t) = (exp(2 pi i C_2 mu) t^{B_0 mu} y, t)`
via `lambda -> Q lambda`; it descends to a holomorphic map `N_3^C -> N_0` over the cusp disc whose fibres over
`t != 0` are extensions `0 -> C/(Z + sZ) -> C^3/(Z^3 + Z_3 Z^3) -> F_t -> 0`.
(d) There is `U_6 in SL_6(Z)` with `U_6 M_3 U_6^{-1} = M_F (+) C_0`, `C_0 = [[1,1],[0,1]]`. With
`C_1 = [[-1,-1],[1,0]]`, `C_2' = [[0,1],[-1,0]]`: `C_1^3 = C_2'^4 = 1`, `C_1 C_2' = C_0^{-1}`; the matrices
`A~_j = A_j (+) C_j` satisfy `A~_1^3 = A~_2^4 = 1`, `A~_1 A~_2 M~_0 = 1`, and
`g~_j(x,y) = (A_j x + v_j/m_j, C_j y)` on `T^4 x T^2` is free of order `m_j` (`(m_1,m_2) = (3,4)`).
(e) The diagonal candidate `M_1 = I_3 (x) S`, `M_2 = I_3 (x) Q`, `M_0 = I_3 (x) T` (orders 4, 6, unipotent)
admits no free affine lift (`det(1-S) = 2`, `det(1-Q) = 1`), `hrftd:prop:finite-fixed-points`.

**Support**. Written proofs, each under two pages; the proper discontinuity is proved by a tropical-coordinate
estimate (`A(t) = I + Im C_3/y`, norms between 1/2 and 3/2). `W\status.tex` l.2731: Verified; "the global
period-and-overlap gluing over both finite-order discs remains Open".

**What it adds**. Over [AC26]: the cusp of `X` is the rank-two case; nothing of rank three there. Over [E26]:
nothing there. Over the literature: (a), (b) are the standard maximal degeneration of `E^3` with the Kuhn
(= `A_3` alcove/"staircase") decomposition; the counts `(1,7,12,6)`, the permutohedral normalization and
`chi = n!` are standard (not searched; I regard them as textbook Mumford/Alexeev-Nakamura). New, as far as the
files go, is only (c)-(d): a holomorphic fibration of a rank-three cusp over the actual cusp of `X` with
elliptic kernel, and the observation (d) that it splits integrally as (cusp of `X`) (+) (Tate curve). Not
searched; it is specific to `X`.

**First assessment**. Correct as far as I read (I checked the matrix identities by hand and the monodromy
relations by script). (d) shows that the construction is a small resolution of a fibre product (see E-2); the
workbench does not say this.

**A full check must establish**: unimodularity and the fan map (short); proper discontinuity at the toric
boundary for the twisted action (the argument "the cell label is translated by lambda" is brief); the
homology map of the filling.

**Deserves a full check**: no, on its own — routine; it matters only as input to E-2 and E-3. **Interest**: 2.

### E-2. The open "global higher torus wrap" is closed by a fibre product with Engel's rational elliptic surface; it gives a simply connected compact complex fourfold with `chi = 6` (reader's observation, not in the workbench)
**Type**: open question of the workbench answered (new small result, derived by this reader from workbench
data; unverified) / underclaim.

**Where**: the open problem is stated at `W\higher_rung_toroidal_elliptic_bridge.tex` l.1057-1105 ("The
remaining global problem", (TEB.54)), l.610-614; `W\higher_rung_24d_continuation.tex` l.762-773 (Remark "Exact
endpoint"); `W\status.tex` l.2805-2806 ("remains Open"); `EV\exact_lorentz_...\README.md` (C28 OPEN);
`EV\higher_rung_24d_20260905\MATHEMATICAL_LEDGER.md` last paragraph.

**Statement of the open problem (workbench)**. Construct a proper holomorphic `f~: X~^8 -> P^1` and a map
`Pi: X~ -> X` over `P^1` such that (1) on regular fibres `Pi` is the elliptic extension (TEB.31) with integral
map `Phi`; (2) over the cusp disc `Pi` is `N_3^C -> N_0`; (3) over the two finite-order discs the affine
monodromy and translation are `g~_j` of E-1(d) "and its punctured overlap agrees with the regular period
family"; (4) `pi_1` and `H_*` are computed from the actual inclusions. "Equations (TEB.24)-(TEB.45) ... do not
supply the global period and overlap construction in item 3."

**Statement (reader)**. The matrices `C_1 = [[-1,-1],[1,0]]`, `C_2' = [[0,1],[-1,0]]`, `C_0 = [[1,1],[0,1]]`
are Kodaira's normal forms of the local monodromy of fibres of type `IV*`, `III`, `I_1`. A relatively minimal
elliptic surface over `P^1` with a section and exactly these three singular fibres over `p_1, p_2, p_0` exists
and is unique: its `J`-map has degree 1, and it is the rational elliptic surface `S -> P^1` of [E26] section 2
(`IV*`, `III`, `I_1`; Mordell-Weil group infinite cyclic). Near `p_j` (`j = 1,2`) write `X|_Delta = F/mu_{m_j}` with `F -> Delta~` a smooth family of 2-tori
over the `m_j`-fold cover and `mu_{m_j}` acting freely (this is what a multiple fibre with smooth reduction
is), and `S|_Delta` = minimal resolution of `E/mu_{m_j}` with `E -> Delta~` a smooth elliptic family
(`IV*`: `m = 3`, central fibre `j = 0`; `III`: `m = 4`, central fibre `j = 1728`). Define

- over `B° = P^1 \ {p_0,p_1,p_2}`: `Z° = X° x_{B°} S°` (monodromy `rho_X (+) rho_S`, i.e. `A~_1, A~_2, M~_0`);
- over a disc at `p_j`, `j = 1,2`: `(F x_{Delta~} E)/mu_{m_j}` (diagonal action, free because it is free on
  `F`) — a smooth fourfold, proper over `Delta`, equal to `X x_Delta S` over `Delta^*`, with multiple fibre
  `m_j . (F_0 x E_0)/mu_{m_j}`; this is the workbench's `g~_j`;
- over the cusp disc: the workbench's `N_3^C` (with `C_3` changed by a bounded holomorphic multiple of the
  rank-one matrix `k r`, `r = (0,0,1)`, so that the kernel curve has Tate parameter `q_S(t) = t . unit`
  instead of `t`; this does not affect `P C_3 = C_2 Q` or the estimates). By E-1(d) and the splitting below it
  is a small toric resolution of the fibre product `N_0 x_Delta S|_Delta`, which has the toric singularities
  `w_0 w_1 w_2 = x y`.

These glue (they are all the same space over the punctured discs) to a compact complex fourfold `Z` with
holomorphic maps `f~: Z -> P^1` (general fibre `F_z x E_z`) and `Pi: Z -> X` (an elliptic fibration, smooth
over `X \ W`, with a section coming from the zero section of `S`). This satisfies (1)-(3) of (TEB.54).
Consequences (reader's quick arguments):
- `chi(Z) = 6` (only the cusp fibre contributes; (TEB.55));
- `pi_1(Z) = 1`: `pi_1(E_z) -> pi_1(Z) -> pi_1(X) = 1` is exact (section, no multiple fibres of `Pi`), loops in
  the section are null-homotopic, so the image of `pi_1(E_z) = Z^2` is a quotient of the coinvariants of
  `<C_1, C_2'> = SL_2(Z)`, which vanish (`det(C_1 - 1) = 3`, `det(C_2' - 1) = 2`);
- `b_2(Z) >= 2` (the section divisors over the two generators `O`, `P` of the Mordell-Weil group of `S`; the
  class of a fibre of `f~` dies because `H^2(X) = 0`), so `Z` is not 3-connected;
- heuristic Betti numbers `(1,0,2,1,2,1,2,0,1)`: Leray for `f~` with `R^q = j_* Lambda^q` plus one extra class
  in `H^4` of the Kuhn fibre (the invariants of `Lambda^*` under `M~_0` have dimensions `1,3,9,9,9,3,1`, sum
  with signs 5, against `chi(W_3) = 6`). The script `work\scratch\E\leray_betti.py` prints the `E_2` terms
  (`X`: rows `(1,0,1)` for `q = 0..4`; `Z`: `(1,0,1),(1,1,1),(2,0,2),(3,1,3),(3,0,2),(1,1,1),(1,0,1)`); the
  `d_2` bookkeeping was done by hand, modelled on `X`, where `d_2` must be an isomorphism
  `E_2^{0,q} -> E_2^{2,q-1}` for `q = 1..4` to give `S^6` (it is cup product with the class that makes
  `pi_1(X) = Z/|12 l_0 - 4 l_1 - 3 l_2|`). The result satisfies Poincaré duality and `chi = 6`; `b_3 = 1` is odd.
- `X` embeds in `Z` as a holomorphic retract, so `Z` is not Kähler and not of class C (a closed submanifold
  of a class C manifold is of class C, and `X` has `b_1 = 0`, `h^{0,1} = 1`); `a(Z) = 2` (`Z` dominates the
  rational surface `S`, and `a(Z) <= a(X) + 1`).
More generally, for any compact complex manifold `Y` with a holomorphic map to `P^1` that is a submersion over
`p_0, p_1, p_2`, the fibre product `X x_{P^1} Y` is a compact complex manifold (a fibre product with a
submersion is smooth); `Y = P^1 x M` gives `X x M`, e.g. complex structures on `S^6 x S^2` and `S^6 x S^6`.

**Support**. None in the workbench (it records the step as open). My argument above; the monodromy identities
`A_1^3 = A_2^4 = 1`, `A_1 A_2 M_F = 1`, `C_1 C_2' C_0 = 1` and the splitting checked by script. The
identification of the workbench's rank-three cusp family with a product: the sublattice
`{(a,b): a_3 = b_3 = 0}` is a complement of the kernel lattice and `Omega_3` maps it into the complex plane
`C e_1 + C e_2` (the third row of `S` is zero), so `C^3/(Z^3 + Z_3 Z^3) = F_t x E_s` holomorphically.

**What it adds**. Over [AC26], [E26]: new compact complex manifolds, but obtained by a formal operation; Engel's
Remark 8.5 has a different generalization in mind (other elliptic surfaces in place of `S` inside the
construction). Literature: searched (WebSearch, 12 Nov 2026) for follow-ups to [E26] on fibre products or
higher-dimensional analogues; found none (only a press remark that Engel expects "a little bit of a zoo" of
generalizations).

**First assessment**. I am fairly confident of existence and of `chi`, `pi_1`. The Betti numbers are a
heuristic count. Interest is modest: specialists would regard `X x_{P^1} S` as an immediate corollary of the
existence of `X`. It does settle what the workbench left open and shows that "the higher torus wrap" in the
workbench's sense is not a new idea but a fibre product.

**A full check must establish**: (i) the local structure of the multiple fibres of `X` as free `mu_m`
quotients of smooth families (it is in [AC26] section on logarithmic transforms and in [E26] section 3, "smooth reduction of IV* and III Kodaira fibers after a" base change);
(ii) that the monodromy of `S` in the bases used is `(C_1, C_2', C_0)` with the same orientation conventions
as `A_j` (if not, replace `S` by its "conjugate"; existence is unaffected, since any elliptic surface whose
local monodromy at `p_1`, `p_2` has order dividing 3, 4 works); (iii) the small resolution at the cusp is
globally consistent (the workbench's `N_3^C` does this); (iv) `H_*(Z; Z)` by Mayer-Vietoris as in [AC26]
section 6 (integral, with torsion), and the signature.

**Deserves a full check**: maybe — cheap to confirm; closes an item the workbench lists as open; low
specialist interest by itself. **Interest**: 3.

### E-3. Open question isolated: a 3-connected rank-three analogue. `chi = 6` is not an obstruction but the first admissible Euler number; is `3 HP^2 # (-HP^2)` a complex manifold?
**Type**: open question isolated (the question is the reader's synthesis of workbench results with the
literature; the workbench stops at "not `S^8`").

**Where**: workbench inputs: `chi(W_{3,B}) = 3! |det B|` (`hrftd:cor:euler-shear-determinant`), the Euler
count `chi(X~) = 6` ((TEB.55), `h24:prop:euler-mismatch`, `h24:cor:euler-repair`), the "replication
requirements" (`hrftd:prop:van-kampen`, `hrftd:thm:mv-criterion`, `hrs8:` l.198-352), the failure of the
diagonal monodromy (`hrftd:prop:finite-fixed-points`), the success of the split one (E-1(d)).

**Statement**. Facts:
1. (Workbench) A proper map `g: M^8 -> S^2` that is a `T^6`-bundle off finitely many points, with one Kuhn-type
   cusp fibre of index `d` and all other special fibres free finite quotients of `T^6`, has `chi(M) = 6d`.
2. (Standard; reader's calculation.) If `M^8` is closed, almost complex, with `H^2(M;Q) = H^6(M;Q) = 0` (so
   `c_1 = c_3 = 0` rationally), then Hirzebruch's congruence `c_1 c_3 + 2 c_4 = 0 mod 12` gives
   `chi(M) = 0 mod 6`; the signature and Todd formulas give `3 c_2^2 = 45 sigma - 14 chi` and
   `Td(M) = (3 sigma - chi)/48 in Z`. For `chi = 6`: `sigma = 2 mod 16`. If `M` is 3-connected then
   `b_4 = chi - 2 = 6d - 2`; for `d = 1`: `b_4 = 4`, `sigma = 2`, form `3<1> (+) <-1>`, `c_2^2 = 2`, `Td = 0`.
3. (Literature, post-cutoff.) S. Mandal, arXiv:2609.27929 (8 Sep 2026): `M_{l,m} = l HP^2 # m (-HP^2)` is
   almost complex iff `l = 2m+1` with `m` odd (correcting Sato-Suzuki 1974). The smallest case is
   `M_{3,1}`: `chi = 6`, `sigma = 2`; in general `chi = 3(m+1) = 6d`, `sigma = 2d` with `d = (m+1)/2` — the
   numbers of fact 1 and 2. (I rederived the criterion from fact 2 with `p_1(HP^2) = 2u`: `chi = 3 sigma` and
   `6 | chi`.)
4. For `S^6`: rank 2, cusp `chi = 2! = 2 = chi(S^6)`, `Td = 0 = chi(O_X)`. For rank 3: cusp `chi = 3! = 6`.
   For rank 4 the pattern stops: a 4-connected 10-manifold has `chi <= 2`, the cusp gives `24`.

Question. Is there a compact complex fourfold `Z` with a proper holomorphic map `Z -> P^1` whose regular
fibres are complex 3-tori, with one maximally unipotent cusp fibre of Kuhn type (`(M_0 - 1)^2 = 0`,
`rank(M_0 - 1) = 3`, index 1, `chi = 6`) and finitely many smooth multiple fibres, such that `Z` is simply
connected with `H_2(Z;Z) = H_3(Z;Z) = 0`? Such a `Z` is a 3-connected closed 8-manifold with `b_4 = 4`,
`sigma = 2`; is it (or can it be chosen) diffeomorphic to `3 HP^2 # (-HP^2)`? Either a construction or a proof
that no monodromy/twist datum has `H_2 = H_3 = 0` would be a result.

**Self-contained prompt for a stronger model** (all data needed):

> Background (take as given). There is a compact complex threefold `X` diffeomorphic to `S^6` with a
> holomorphic map `f: X -> P^1`, regular fibres complex 2-tori, special fibres over `p_0, p_1, p_2`
> (Claude-Alpöge 2026, alpo.ge/s6.pdf; P. Engel, arXiv:2609.38442). On `H_1(fibre) = Z^4` (basis
> `gamma^, u^, w^, delta^`) the monodromies are
> `A_1 = [[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]` (order 3, at `p_1`),
> `A_2 = [[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]]` (order 4, at `p_2`),
> `M_F = [[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]]` (at `p_0`, `(M_F - 1)^2 = 0`, rank 2), `A_1 A_2 M_F = 1`.
> Over `p_0` the fibre is a Mumford toric degeneration (`A_2`-triangulated `R^2/Z^2`, one component, the
> degree-6 del Pezzo surface with opposite sides glued, `chi = 2`); over `p_j` the fibre is `m_j` times a
> smooth free quotient `T^4/<x -> A_j x + v_j/m_j>`, `(m_1,m_2) = (3,4)`,
> `v_1 = gamma^ + 2u^ - 4w^`, `v_2 = -gamma^ - 3u^ + 3w^`; `pi_1(X) = Z/|12 l_0 - 4 l_1 - 3 l_2| = 1` for the
> twists `(l_0,l_1,l_2) = (0,1,-1)`. Engel's construction: `S -> P^1` the rational elliptic surface with
> fibres `IV*, III, I_1` and Mordell-Weil generator `P`; `M = O(P - O)`; `X(u)` is the quotient of the
> `C^*`-bundle `M^x` (over the complement of the `I_1` fibre) by a lift, scaled by small `u`, of translation
> by `6P`, filled at infinity by a Mumford construction and log-transformed with multiplicities 3, 4.
>
> Known in rank three. (i) The fibre product `Z_0` of `X` with `S` over `P^1` (normalized at `p_1, p_2`,
> resolved by the Kuhn triangulation at `p_0`) is a compact complex fourfold fibred in 3-tori `F_z x E_z` with
> monodromy `A_j (+) C_j`, `C_1 = [[-1,-1],[1,0]]`, `C_2 = [[0,1],[-1,0]]`, `C_0 = [[1,1],[0,1]]`; it is
> simply connected with `chi = 6` but `b_2 >= 2`. (ii) The monodromy `I_3 (x) (S, Q, T)` of `E_tau^3` has no
> free affine lifts. (iii) A closed almost complex 8-manifold with `c_1 c_3 = 0` has `6 | chi`; a 3-connected
> one with `chi = 6` has `b_4 = 4`, `sigma = 2`, `c_2^2 = 2`, Todd genus 0; `3 HP^2 # (-HP^2)` is almost
> complex (Mandal, arXiv:2609.27929).
>
> Tasks. (1) Verify (i) and compute `H_*(Z_0; Z)` and the signature. (2) Classify, up to conjugacy, triples
> `(M_1, M_2, M_0)` in `GL_6(Z)` with `M_1 M_2 M_0 = 1`, `M_1, M_2` of finite order, `(M_0-1)^2 = 0`,
> `rank(M_0 - 1) = 3` and `M_0 - 1` inducing an isomorphism from the quotient lattice onto the image lattice
> (index 1), such that `M_1, M_2` have free affine lifts `x -> M_j x + v_j/m_j`; allow also more than two
> finite points. For each, with each choice of twists, compute `pi_1` and `H_*(.;Z)` of the glued 8-manifold
> by van Kampen and Mayer-Vietoris (as in section 6 of the Claude-Alpöge paper) and list the data with
> `pi_1 = 1`, `H_2 = H_3 = 0`. (3) For each surviving datum decide whether a holomorphic period family with
> that monodromy exists over the thrice-punctured sphere with `Im` of the period nondegenerate and bounded
> correction at the cusp; the natural source is Engel's method with `S` replaced by a fibration of abelian
> surfaces `A -> P^1` (for example the Jacobian fibration of a pencil of genus-2 curves with three singular
> fibres, one of toric rank 2 and two with finite monodromy), a fibrewise degree-0 line bundle `M` on `A` and
> a section of infinite order; the quotient of `M^x` by a scaled lift of the translation has fibres
> 3-tori and a cusp with `rank(M_0 - 1) = 2 + 1`. (4) If a 3-connected example exists, identify it in Wall's
> classification (intersection form `3<1> (+) <-1>`, `p_1 = -2 c_2`) and compare with `3 HP^2 # (-HP^2)`.
> Done means: either an explicit datum with a proof of compactness, smoothness and the homology computation,
> or a proof that no datum of type (2) has `H_2 = H_3 = 0`. A list of numerical coincidences is not a result.

**Support**. Fact 1: workbench proofs (short, correct). Fact 2: my calculation from the standard formulas
`sigma = (7 p_2 - p_1^2)/45`, `Td_4 = (-c_4 + c_1 c_3 + 3 c_2^2 + 4 c_1^2 c_2 - c_1^4)/720`,
`p_1 = c_1^2 - 2c_2`, `p_2 = c_2^2 - 2 c_1 c_3 + 2 c_4`. Fact 3: abstract of arXiv:2609.27929 read via
WebFetch on 12 Nov 2026 (paper not read).

**What it adds**. Not in [AC26]; [E26] Remark 8.5 asks in general "what class of 6-manifolds can arise";
this is the dimension-8 version with a definite target. Literature searched: H. Yang, arXiv:1110.1798 (almost
complex structures on (n-1)-connected 2n-manifolds), Yang arXiv:1808.07343, Mandal arXiv:2609.27929; no paper
found that asks for an integrable structure on `3 HP^2 # (-HP^2)` or relates it to torus fibrations.

**First assessment**. It is a question, and it may well have a negative answer (for instance if every
admissible monodromy has an invariant class forcing `b_2 > 0` or `b_3 > 0`); but the numerical fit
(`chi = 3!`, `Td = 0`, existence of the almost complex structure exactly at `chi = 6d`, `sigma = 2d`) is
better than the workbench's own numerology, and part (2) of the prompt is a finite computation.

**A full check must establish**: n/a (research prompt). The first step, the classification of integral
representations of `Z/m_1 * Z/m_2` on `Z^6` with a rank-three unipotent product, is mechanical.

**Deserves a full check**: yes, as a prompt to a stronger model rather than a check — it is the one place
where this block points to a possibly new compact complex manifold. **Interest**: 4.

### E-4. Exclusions for spheres: no almost complex structure on a homotopy `S^8` (three proofs) or on homotopy `S^m`, `m > 6`; Euler and bundle constraints for a `T^6`-fibration of `S^8`
**Type**: expository only (known results with full proofs) plus bookkeeping criteria.

**Where**: `W\higher_rung_s8_constraints.tex` l.25-408; `hrftd:thm:no-almost-complex-s8`,
`hrftd:thm:euler-obstruction`, `hrftd:prop:van-kampen`, `hrftd:thm:mv-criterion`; `h24:thm:s8-obstruction`,
`h24:thm:all-higher-spheres`. 3-5 Sep 2026.

**Statement**. (i) A closed smooth manifold homotopy equivalent to `S^8` has no almost complex structure:
`c_4 = 2u`, `p_2 = 2 c_4 = 4u`, but `sign = 0 = 7 p_2/45`. Also Borel-Serre's `P^1(c_2) = ... + 4 c_4` mod 3,
and Bott's `(n-1)! | c_n` on `S^{2n}`. No homotopy `S^m`, `m > 6`, is almost complex. (ii) No fibre bundle
`T^6 -> S^8 -> S^2` (`Z -> Z^6` not onto; `chi`). (iii) For a singular `T^6`-fibration of `S^8` over `S^2`:
`sum chi(F_i) = 2`; `pi_1 = pi_1(E)/<<ker(pi_1(A_i) -> pi_1(N_i))>>`; the homology-sphere criterion in terms
of the Mayer-Vietoris maps `alpha_q`; Wang and Serre sequences with the correct edge maps
(`0 -> (Lambda^q)_rho -> H_q(E) -> H_1(B°; Lambda^{q-1}) -> 0`). (iv) An effective torus action on `S^8` has
rank `<= 4`; `S^8/T^4 = Susp(Delta^3) = B^4`.

**Support**. Complete short proofs. `W\status.tex` l.3025: "Refuted" for the literal complex `S^8`.

**What it adds**. Nothing new: (i) is Borel-Serre 1953 (cited); (iv) is standard. The answer to the
assignment's question 2: the S^8 file proves only known exclusions and necessary conditions; it contains no
construction and no new constraint on quotient or collapse maps.

**First assessment**. Correct. One criticism in section 3 (the role of `chi = 6`).

**A full check must establish**: nothing beyond reading the three short arguments in (i).

**Deserves a full check**: no — known results. **Interest**: 1.

### E-5. `SU(3)` bundles on the regular locus `U = X \ (W u S_1 u S_2)`: classified by `H^4(U;Z) = Z^6`
**Type**: computation (small, self-posed).

**Where**: `W\higher_rung_s8_constraints.tex` l.482-669 (`hrs8:eq:h4-regular-locus`,
`hrs8:eq:su3-classification`, `hrs8:eq:extension-criterion`, `hrs8:eq:c3-clutching`, `hrs8:eq:h6-relative`);
also `rsl:eq:defect-lattice`. 3 Sep 2026.

**Statement**. With `X = S^6`: `H^4(U;Z) = H_1(W) (+) H_1(S_1) (+) H_1(S_2) = (Z^2)^3` by Alexander duality;
`0 -> H^1(B°; V^3) -> H^4(U) -> H^0(B°; V^4) = Z -> 0`; `U` has the homotopy type of a 5-complex, so
`c_2: {SU(3)-bundles on U}/iso -> H^4(U;Z) = Z^6` is a bijection; a bundle on `U` extends over `X` iff
`c_2 = 0`; `SU(3)`-bundles on `S^6` are classified by `pi_5(SU(3)) = Z` with `c_3 = +-2k u`, and all restrict
trivially to `U`; `H^5(U) = Z^2`, `H^6(X,U) = Z^3` with augmentation `(n_0,n_1,n_2) -> n_0+n_1+n_2`.

**Support**. Written argument. Sanity check by this reader: `H_1(S_j;Z)` computed from the presentation
(`Z^4` with `(A_j - 1)`, and `m_j g = v_j`) by Smith normal form — both are `Z^2` with no torsion
(`work\scratch\E\h1_bielliptic.py`), as the file asserts. `c_2: BSU(3) -> K(Z,4)` is 6-connected, so the
classification is right.

**What it adds**. Not in [AC26]/[E26]. The by-product `H^4(X \ D; Z) = Z^6`, and the torsion-freeness of
`H_1(S_j)`, are facts about `X`; the rest is obstruction theory. Not searched.

**First assessment**. Correct, of no evident outside interest (the gauge-theoretic reading is disclaimed in
the file itself).

**A full check must establish**: `H_1(W;Z) = Z^2` (from the reconstruction of [AC26]); triangulability of `D`
for Alexander duality; the CW dimension of `U`.

**Deserves a full check**: no — short and already sanity-checked. **Interest**: 2.

### E-6. Gram quotients of matrix spaces: `Mat_{3x2}(C)/SU(3) = Herm_2^{>=0}`, `Mat_3(C)/SU(3) = {(H,z): |z|^2 = det H} = R^10`, `S^17/SU(3) = S^9`, the pair `(S^10, S^8)`
**Type**: expository only (classical invariant theory with explicit homeomorphisms).

**Where**: `W\higher_rung_su3_gram_cone.tex`, `W\higher_rung_su3_triple_s8_cone.tex`,
`W\higher_rung_24d_continuation.tex` l.775-1404, `hrs8:` l.410-480, `hrftd:` l.888-1030.

**Statement** (grouped). `Gamma(A) = A^* A` separates `U(3)`-orbits on `Mat_{3xk}(C)`; for `k = 2` also
`SU(3)`-orbits, quotient the closed future light cone `{t >= |x|}` in `Herm_2 = R^{1,3}`,
`det Gamma(A) = |a ^ b|^2`; the free locus is `SU(3) x Herm_2^{>0}`; `(Mat_{3x2})^+/SU(3) = B^4`. For `k = 3`:
`Mat_3/U(3) = Herm_3^{>=0} = R^8 x R_{>=0}` by `H -> (H - tr H/3, lambda_min(H))`; `S^17/U(3) = B^8`;
`Mat_3^+/U(3) = B^9` with boundary the rank-loss `S^8`; `(A^*A, det A)` separates `SU(3)`-orbits;
`S^17/SU(3) = S^9 = S^7 * S^1`; `Mat_3^+/SU(3) = S^10` containing the rank-loss locus as a linear `S^8`, with
complement `R^8 x C^*`; `U(3)/SU(3)` rotates `z`. The compression `O_9(H,z) = P H P^*` on `S^9` has fibres
`S^5`, disc, point (`h24:thm:O9-fibres`). The rank-one germ of `{det = 0}` is the cone `uv = x^2 + y^2`, not
normal crossings (`hrftd:thm:hermitian-not-snc`). No `SU(3)` bundle with `c_2 != 0` on `S^4` arises
(`thm:hrgc-no-native-s4-sector`).

**Support**. Complete elementary proofs.

**What it adds**. Nothing about `X`. The only link to `X` is `h24:prop:Gram-square`: for a real `6x6` Gram
matrix `G_6`, `P (Omega_3 G_6 Omega_3^*) P^* = Omega_2 (Phi G_6 Phi^T) Omega_2^*`, a restatement of
`P Omega_3 = Omega_2 Phi` (E-1(c)), and the limit `h_3 -> I_3/3` at the cusp for `G_6 = I`. Literature not
searched (first fundamental theorem for `U(n)`, `SU(n)`; the sphere statements are folklore).

**First assessment**. Correct; self-posed; my judgement: decoration around the word "S^8". The S^8 here is the
boundary of an orbit space and has no relation to a fibration or a complex structure, as the files say
themselves.

**A full check must establish**: continuity of the explicit homeomorphisms at rank loss and at the cone point
(the only non-formal steps).

**Deserves a full check**: no — classical, unrelated to `X`. **Interest**: 1.

### E-7. "Lorentz observation": `Herm_3(C) = Herm_2(C) (+) C^2 (+) R` under `SL_2(C)`, the cubic `det H = lambda det G - psi^* adj(G) psi`, and related identities
**Type**: expository only / computation (standard linear algebra in physical vocabulary).

**Where**: `W\higher_rung_lorentz_observation_bridge.tex` (all); `thm:teb-hermitian-determinant-splitting`,
`prop:teb-theta-order-lift` in `W\higher_rung_toroidal_elliptic_bridge.tex` l.705-923;
`EV\exact_lorentz_observation_bridge_audit_20260904\`. 3-4 Sep 2026.

**Statement** (grouped). With `X_P = (R u)`, `R = P^* (P P^*)^{-1}`, `u = (1,1,1)`: every `H in Herm_3` is
`X_P [[G, psi],[psi^*, lambda]] X_P^*` with `G = P H P^*`, `psi = P H u/3`, `lambda = u^* H u/9`;
`det H = lambda det G - psi^* adj(G) psi`; `H >= 0` iff `G >= 0`, `psi in im G`, `lambda >= psi^* G^+ psi`;
`T_P(g) = R g P + u u^*/3` embeds `GL_2(C)` in `GL_3(C)` and acts by `(G, psi, lambda) -> (g G g^*, g psi,
lambda)`; `e_2(R G R^*) = det G/3`; `det(u u^* + eps R G R^*) = eps^2 det G`;
`det(S + i [a]_x) = det S - a^T S a` for real symmetric `S`;
`det_3 Theta(H_2) = (tr H_2/2) det_2 H_2` for `Theta: Herm_2 -> R I_3 (+) i so(3)`; `p_alpha(Z) = alpha Z^* Z`
on `Mat_{3x2}(C)` with "mass" `det p/c^2`; a first-order worldline action.

**Support**. Proofs in the file; an independent audit with 30/30 and 33/33 exact checks; the audit REFUTES the
dynamical reading of the action (C23: on the hard `(lambda_0, omega_0)` constraint it forces `x' = 0`) and
the global-completion claim (C32), and leaves C27-C30 OPEN.

**What it adds**. Nothing about `X`: the matrix `P` is the cusp's angular quotient `Z^3 -> Z^2`, and that is
the only input from the threefold. The decomposition is the Peirce decomposition of the Jordan algebra
`Herm_3(C)` relative to a rank-one idempotent (`u u^*/3`), with the structure group of the `Herm_2` corner
acting as the Lorentz group — standard (Jordan-von Neumann-Wigner; not searched). The "holomorphic toric seed"
(l.674-747) is the factorization `z_0 z_1 z_2 z_3 = det diag(z_0 z_3, z_1 z_2)`.

**First assessment**. Correct identities; my judgement: decoration. No statement links to `X` by a map of
spaces; the files say so ("not a holomorphic toric map, a map of integral period lattices, or a
singular-fibre filling map").

**A full check must establish**: nothing further; the identities were replayed twice by exact scripts.

**Deserves a full check**: no — standard linear algebra, already audited. **Interest**: 1.

### E-8. Rank-six lattice and rank-nine "chamber torsor"
**Type**: computation (bookkeeping of the numbers 6 and 9).

**Where**: `W\higher_rung_rank_six_lattice.tex`, `W\higher_rung_rank_nine_matrix_torsor.tex`. Sept 2026.

**Statement** (grouped). `0 -> K -> Z^3 (+) Z^3 -Phi-> A_F (+) B_F -> 0` is a sequence of `Z[S_3]`-modules,
split over `Z` with monodromy but not over `Z[S_3]` (an equivariant retraction would have entries divisible by
3); `Z^3/Zk` is the `A_2` weight lattice; "three sixes": `rk H_1(T^6) = 6`, 6 Kuhn cells, `chi = 3! |det B|`,
and the 6 basis vectors are not equivariantly the 6 cells (characters `(6,2,0)` vs `(6,0,0)`);
`Hom(L-bar_3, L_3) = Z[S_3/S_2] (+) Z[S_3]`, the cells correspond to the off-diagonal matrix units
`c_pi -> E_{pi_1 pi_3}`, which are the `E_3`-isotropic mixed pairs; `D = [P | -P]` restricted to
`Z(e_i,0) + Z(0,e-bar_j)` is an isomorphism onto `A_F` mapping the positive quadrant to a Weyl chamber; no `T`
with `D M_3 = T D`; the standard alternating form `E_3` is not pulled back along `Phi`
(`E_3((k,0),(0,k)) = 3`); `Mat_3(R) = Herm_3(C)` as `S_3`-representations with integral index 8.

**Support**. Short complete proofs.

**What it adds**. Nothing outside the workbench's own question ("is the 6 of the cells the 6 of the lattice
rank?"). One remark with content for E-2/E-3: the product family carries no polarization compatible with
`Phi` (expected: the tori are not algebraic).

**First assessment**. Correct; decoration.

**A full check must establish**: nothing further (finite matrix identities).

**Deserves a full check**: no — bookkeeping. **Interest**: 1.

### E-9. Octonionic flag `F_4/Spin(8)`: explicit open cell, degree-one collapse onto `S^24`, and the determinant-boundary sphere
**Type**: expository (Mare-Willems) with explicit formulas that may be new as formulas.

**Where**: `W\higher_rung_24d_continuation.tex` l.1406-3576. 5 Sep 2026.

**Statement** (the parts beyond citation). (i) `partial C(O)`, the boundary of the positive cone in the
equal-diagonal slice `{Q_O(lambda; q)}` of `h_3(O)`, is the graph `q -> Q_O(a(q); q)` over `O^3`, so
`(partial C(O))^+ = S^24`, `Spin(8)`-equivariantly; `d(X) = xi_1 xi_2 xi_3 - sum xi_i N(q_i) + 2 Re((q_1 q_2) q_3)`.
(ii) With `nu_i(u) = (L_u + [L_{h_*}, L_u]/rho_i(h_*))/2`, `Z(q) = sum nu_i(E_i(q_i))`: `Z(q)^5 = 0`,
`[nu_1(r), nu_2(s)] = nu_3(-(rs)-bar/2)`, group law
`(q) * (q') = (q_1+q_1', q_2+q_2', q_3+q_3' - (q_1 q_2')-bar/4 + (q_1' q_2)-bar/4)`; the map
`Psi(q) = (exp(Z) d_2/tr, exp(-Z^*) d_1/tr)` is a `Spin(8)`-equivariant diffeomorphism of `O^3` onto the open
cell `{a_22 > 0, b_11 > 0}` with inverse `q_1 = 2 a_23/a_22`, `q_2 = -2 b_31/b_11`,
`q_3 = 2 a_12/a_22 - (q_1 q_2)-bar/4`. (iii) The collapse `c: Fl(O) -> (O^3)^+ = S^24` is equivariant of degree
`+1`, zero on `H_8`, `H_16`; every map `S^24 -> Fl(O)` has degree 0. (iv) The six `Spin(8)`-fixed flags
correspond `S_3`-equivariantly to the six zero-strata of `W_3`; `h(F_4) = 12`, `W(F_4)/W(D_4) = S_3`;
`H^*(Fl(O); Z/N)` and the tests of `h24:thm:exact-numerical-boundary`: "No arrow between these four lines is
defined merely by equality of their integers."

**Support**. Proofs in the file (statements read, proofs sampled); an independent audit of the flag claims
against Mare-Willems (`AUDIT_OCTONIONIC_LOG.md`).

**What it adds**. Nothing about `X`: the only relations are a bijection of 6-element sets and the statement
that `X^{^4}` is an `S^24` after a chosen homeomorphism `X = S^6`. The explicit Bruhat-cell chart (ii) is the
kind of formula found in the literature on `F_4` (not searched).

**First assessment**. Looks correct; the block's own conclusion is negative (no map, no mod-24 mechanism). My
judgement: decoration with respect to S6; possibly a usable explicit chart for someone working on
`F_4/Spin(8)`.

**A full check must establish**: (ii) (the coefficient 1/4 and the inverse formula) by a computer algebra
check with octonions.

**Deserves a full check**: no. **Interest**: 1.

### E-10. The peripheral character `chi: SL_2(Z) -> Z/12` and the numerology tests
**Type**: computation (bookkeeping); overlaps C1-4, C1-6, C1-7.

**Where**: `W\higher_rung_24d_continuation.tex` l.3577-3770 (`h24:thm:peripheral-moduli`,
`h24:prop:cusp-diagonal-modulus`, `h24:prop:no-modulus-from-cohomology-or-determinant`).

**Statement**. `chi(C_1, C_2', C_0) = (4, -3, -1) mod 12`; every homomorphism `SL_2(Z) -> Z/24` has even
image, and `chi` has no lift along reduction `Z/24 -> Z/12`; the diagonal-sum character
`Z^3 -> Z/N` factors through `P` or `Q` iff `N | 3`; `e_N = 6u mod N` has order `N/gcd(N,6)`.

**Support**. Short proofs from the presentation `SL_2(Z) = Z/4 *_{Z/2} Z/6`; summarized in
`h24:thm:exact-numerical-boundary`.

**What it adds**. Elementary. In the light of E-2, `chi` is the abelianized monodromy of Engel's elliptic
surface `S`; the values 4 and -3 are those of the `IV*` and `III` fibres. No use is made of this.

**First assessment**. Correct. The block's conclusion is negative: none of the tested mechanisms singles out
12 or 24.

**A full check must establish**: nothing further.

**Deserves a full check**: no — bookkeeping. **Interest**: 1.

### E-11. A nontrivial real 3-plane bundle on `X = S^6` from the retained-angle map
**Type**: computation (formal consequence of C1-3).

**Where**: `W\higher_rung_24d_continuation.tex` l.5112-5750 (`h24:rettri:bundleclass`, `h24:rettri:subgroup`,
`h24:rettri:forgetting`).

**Statement**. For `H: X -> S^4 = HP^1` with `[H] = eta_4 eta_5`, the pulled-back Hopf bundle `P_H` has
clutching class `partial[H] != 0 in pi_5(Sp(1)) = Z/2`; the adjoint bundle `A_H = P_H x_Ad Im H` is the
nontrivial oriented `R^3`-bundle over `S^6` (`pi_5(SO(3)) = Z/2`), with no nowhere-zero section;
`rho(u) = (B_u, A_u, D_u): Sp(1) -> Spin(8)` is an injective homomorphism into the triality group; the
induced `Spin(8)`-bundle is trivial and gives a non-null map `X -> Spin(8)/rho(Sp(1))`.

**Support**. Written proofs (statements read; proofs not read); depends on Theorem `h24:ret:main` (C1-3).

**What it adds**. Given C1-3 this is the standard chain `pi_6(S^4) -> pi_5(S^3) -> pi_5(SO(3))` of
isomorphisms. It says: the unique nontrivial `R^3`-bundle on `S^6` is the pull-back of the adjoint Hopf bundle
by a map defined from the cusp coordinates. Minor.

**First assessment**. Formally correct if C1-3 is; no independent content.

**A full check must establish**: C1-3 only; then the three isomorphisms `pi_6(S^4) = pi_5(Sp(1)) = pi_5(SO(3))`.

**Deserves a full check**: no — depends only on C1-3. **Interest**: 1.

---

## 3. Doubts and errors

1. **Underclaim (main point).** `W\higher_rung_toroidal_elliptic_bridge.tex` l.610-614 and l.1083-1085,
   `W\higher_rung_24d_continuation.tex` l.762-773, `W\status.tex` l.2805: the global gluing of the rank-three
   family is recorded as open. With the monodromy `A_j (+) C_j` that the workbench itself chose, the family is
   the fibre product of `X` with an elliptic surface, and the gluing is automatic (E-2). The workbench proved
   the integral splitting (`prop:teb-explicit-conjugacy`) but did not draw the conclusion, and did not
   recognise `C_1, C_2', C_0` as the Kodaira matrices of `IV*, III, I_1`, i.e. of Engel's surface. (The
   workbench predates Engel's paper by about a week, which explains the second omission.)
2. **Framing of `chi = 6`.** `hrftd:` l.556-642, (TEB.55), `h24:cor:euler-repair`, `hrs8:` l.169-196 treat
   `chi = 6` only as the reason why the total space is not `S^8`, and go on to ask for extra singular fibres
   with Euler sum `-4` in a "real" `S^8`. The natural question — which closed 8-manifolds with `chi = 6` could
   carry the structure — is not asked. `chi = 0 mod 6` is forced for almost complex 8-manifolds with
   `c_1 c_3 = 0` (E-3). Also l.1046 of `hrftd:` "A compact complex globalization must have different
   topology" is true and has an immediate example nobody mentions: the resolved triple fibre product of an
   elliptic modular surface (a projective fourfold) for the untwisted cusp.
3. **Wording that claims more than the mathematics.** `h24:thm:strongest-gram` ("Which Gram carrier is
   strongest") is not a theorem about a defined notion; `hrs8:` l.684-686 calls the `U(3)` Gram boundary "the
   strongest precise realisation presently obtained for the 'one rung higher' intuition" although it has no
   relation to `X`; `h24:prop:three-24d-objects` (ii) uses an arbitrary homeomorphism `X^{^4} = S^24`. The
   files do add disclaimers each time.
4. **`h24:def:feature-ledger` (F6)** asks for "the claimed smooth sphere topology" of a higher wrap, which
   `h24:thm:all-higher-spheres` (ten lines later) shows is impossible; the definition should have asked for
   the topology to be computed (it says so in its first sentence, inconsistently with (F6)).
5. **Proper discontinuity at the toric boundary** (`h24:prop:toric-filling-map` proof, l.620-634): the twisted
   action's behaviour on boundary strata is argued in two sentences ("the bounded cell label is translated by
   lambda"). The fuller version is in `thm:teb-holomorphic-cusp-bridge`. I see no error; a checker of E-2
   should read the fuller version.
6. **Lorentz block**: the audit in `EV\exact_lorentz_...` refutes the dynamical and global-completion claims of
   the imported packet (C23, C32). The workbench file `higher_rung_lorentz_observation_bridge.tex` l.748-927
   keeps the action and says "complete constrained kinematic dynamics"; its Euler-Lagrange equations are
   derived for the soft constraint `det p = m_0^2 c^2` only, so there is no contradiction, but the physical
   vocabulary ("mass", "colour", "Weyl spinor") names linear-algebra objects and should not be read as a
   result about `X`.
7. No mathematical error found in the statements I read. Checks done: monodromy relations and invariance of
   `v_j` (script); `H_1(S_j;Z) = Z^2` (script); `det(I + i[a]_x) = 1 - |a|^2`; `S Q = T^{-1}`,
   `det(1 - Q) = 1`; the count `(1,7,12,6)` and the 14 neighbours of a Kuhn vertex.

---

## 4. Not read

- `W\higher_rung_24d_continuation.tex`: proofs in l.1445-3576 (octonionic block) and l.3577-4375 only
  sampled; l.4376-5112 and 5752-6134 left to C1's notes; l.6184-7199 (Albert orbit / Cartan family / common
  lattice) statements only — reader D1's topic.
- `R\s6_higher_rung_24d_preprint.tex`: only the head (l.1-123) and a structural comparison with the
  continuation; same text.
- `W\higher_rung_su3_gram_cone.tex` l.401-466 and l.645-708 (four-coefficient form; log-Euclidean metric and
  Yang-Mills as extra choices): headings only. `W\higher_rung_su3_triple_s8_cone.tex` l.844-885: heading only.
- Evidence folders: `WORKLOG.md` first 5 KB only; `CLAIM_LEDGER.md`, `DEFINITIONS_AND_MAPS.md` of the Lorentz
  audit not opened (the README and the audit report sections 5-8 were read); JSON receipts, checker scripts
  and build/visual-QA files not opened.
- arXiv:2609.27929 (Mandal): abstract only. arXiv:1110.1798 (Yang): not opened.
- Not computed: `H_*(Z;Z)` of the fibre product in E-2 beyond the heuristic count; the classification of
  monodromy triples asked for in E-3.
