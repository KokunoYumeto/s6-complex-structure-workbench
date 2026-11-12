# C1 notes: cusp sphere-carriers and homotopy (S6 workbench)

Reader C1, Claude Fable 5.2, 12 Nov 2026. Read only; one scratch script at
`work\scratch\C1\check_invariants.py` (sympy; output quoted in C1-2).

Base folder below: `R = C:\Users\user\Documents\math\research\s6_recent_results_main\canonical_S6_snapshot`,
`W = R\supporting_materials\workbench`. All files carry the copy time 29 Sep 2026 00:32; the content
dates are 3-5 Sep 2026 (research_log Rounds 29-36 are dated 3 Sep; the framing/Arf/Hopf pieces 5 Sep).
That is before Engel's paper (13 Sep 2026), so nothing here refers to [E26].

Notation of the workbench (fixed once): `Lambda = Z<gamma^,u^,w^,delta^>` is the marked fibre lattice;
cusp monodromy `M_0`, `im(M_0-I) = ker(M_0-I) = K = Z<w^,delta^>` (the vanishing 2-torus); elliptic
monodromies `A_1` (order 3), `A_2` (order 4); `eps_gamma` = the gamma^-coordinate = the unique
monodromy-invariant covector; `L = ker eps_gamma = Z<u^,w^,delta^>` (Engel's invariant rank-3 sublattice);
cusp at `t = 0` (`p_0`), `N_0 = f^{-1}(|t| <= eps)`, `W = f^{-1}(0)`; `F_T` the fibre over `t = e^{-2 pi T}`.

---

## 1. Reading notes

### 1.1 `W\research\cusp_cone_sphere_routes.tex` (38.7 KB, 950 lines) — read in full
Subsection "Cone-compactified sphere carriers for the native cusp quotient" (label `cusp-cone-section`).
- Lemma `cusp-cone-native-descent` (l.33-94): the quotient `pibar: N_0 \ W -> D_0^* x Tbar^2`,
  `Tbar^2 = (Lambda/K) (x) R / (Lambda/K)`, well defined because `M_0 = id mod K`; on `F_T` it is
  `pi_T: F_T -> Q_T = R^2/Y_T Z^2`, `sys(Q_T) >= T - C`.
- Theorem `cusp-cone-S12-route` (l.118-271): `q_2: (X,x_0) -> (A,v_0)`, `A = Susp(S^1 x Tbar^2) = Susp(T^3)`
  (unreduced), `q_2(x) = [r, e^{i phi}, pibar_f(x)]` for `t = r e^{i phi}`, `q_2(W) = v_0`,
  `q_2(X \ int N_0) = v_1`; smash square `X^X = S^12 -> A^A`; restriction to `F_T^2` is `pi_T x pi_T`;
  `(Q_T^2, 0) -> (R^4, 0)` pointed GH; reduced homology of `A` (Z^3, Z^3, Z in degrees 2,3,4) and of `A^A`.
- Proposition `cusp-cone-S24-local-route` (l.287-358): `q_{1,cusp}: X -> B = Susp(T^2)`,
  `x -> [r, e^{i phi}, theta_gamma(x)]`; fourth smash power, source `S^24`.
- Theorem `cusp-cone-S24-route` (l.394-561): `M = (P x S^1) u C_1 u C_2` (pair of pants times circle, glued
  to the two Seifert solid tori), `partial M = partial D_0 x S^1`, `C = M u Cone(partial M)`;
  `q_1: X -> C` equal to `(f, theta_gamma)` over `P`, the Seifert-target maps over `D_1, D_2`,
  `[r,(e^{i phi}, theta_gamma)]` on `N_0 \ W`, `W -> c_0`. `H_1(M) = Z<g>` with
  `rho_0 = -g, rho_1 = 4g, rho_2 = -3g, eta = 12g` (meridian relations `3 rho_1 - eta = 0`,
  `4 rho_2 + eta = 0`); `H~_k(C) = Z` for `k = 2,3`.
- Definition `cusp-cone-target-slice-embeddings`, Proposition `cusp-cone-metric-scope` (l.563-638):
  ambient diameters of the slices tend to 0 in any fixed compatible metric, intrinsic diameters to infinity.
- Proposition `cusp-cone-S12-almost-complex-obstruction` (l.640-782): three proofs that no homotopy `S^12`
  is almost complex (Borel-Serre `P^1_5(c_2) = 6 c_6` mod lower classes; Bott integrality `120 | c_6`;
  `p_3 = -2 c_6` on the standard sphere).
- Theorem `cusp-cone-obstructions` (l.784-917): rank bound `rank(Lambda^{(+)r}/N) <= r` for full-base
  quotients with diverging systole; no finite base cover preserves `K`
  (`(A_2A_1)^n w^ = w^ + n(u^ - delta^)`); no fixed `T^4` or `S^4` target; products and joins are not
  `S^12`, `S^24`.
All statements carry the workbench status VERIFIED via ledger entries S6-CUSP-CONE-SPHERE-ROUTES and
S6-CUSP-CONE-OBSTRUCTIONS.

### 1.2 `W\research\cusp_sphere_route_strengthening.tex` (46.8 KB, 1186 lines) — read in full
- Theorem `cusp-cone-optimal-exponents` (l.29-139): two copies necessary and sufficient cusp-locally
  (rank <= 2r), four over the full base (rank <= r), "within native connected torus quotients with the
  unscaled metric".
- Theorem `cusp-cone-angle-forgotten-sphere-carriers` (l.141-472): the sphere-valued maps
  `q^_3 = p^_2 o q_2: X -> S^3`, `p^_2([r, e^{i phi}, u]) = [r, c(u)]`, `c: Tbar^2 -> Tbar^2/K^(1) = S^2`
  the collapse of the coordinate 1-skeleton, target `Sigma_r(S^2) = S^3`; and
  `q^_gamma = p^_1 o q_{1,cusp}: X -> S^2`, `p^_1([r, e^{i phi}, theta]) = [r, theta] in Sigma_r(S^1)`.
  Moving 4-spheres `S_T^2 ^ S_T^2 c S^6`, `C_T^{^4} c S^8` with exact Euclidean balls of radius `R` once
  `T - C > 4R` (resp. `l_T > 4R`).
- Corollaries `cusp-cone-S12-sphere-map-null`, `cusp-cone-S24-sphere-map-null` (l.474-563): both smash
  maps null; the general statements (see C1-6).
- Corollary `cusp-cone-literal-R4-open-cells`, Remarks `cusp-cone-moving-S4-null-homotopy`,
  `cusp-cone-sphere-map-homotopy-status` (l.565-676). The last one states the status:
  "`[q^_3] in pi_6(S^3)` is now zero by Theorem `cusp-null:thm`; `[q^_gamma] in pi_6(S^2)` remains open."
- Proposition `cusp-cone-explicit-carriers` (cones on `T^4`, local homology at the vertex), Theorem
  `cusp-cone-target-homotopy-types` (l.788-886): `A^A ~ V^9 S^4 v V^18 S^5 v V^15 S^6 v V^6 S^7 v S^8`,
  `pi_1(M) = <x,y,h | [x,h],[y,h], x^3 = h, y^4 = h^{-1}>`, `pi_1(C) = 1`, `C ~ S^2 v S^3`,
  `C^{^4} ~ S^8 v V^4 S^9 v V^6 S^10 v V^4 S^11 v S^12`.
- Theorem `cusp-cone-exact-decompactification-space` (l.888-1136): 5-manifolds `E_nu` with boundary `R^4`,
  comparison maps `beta_nu: E_nu -> D_nu` continuous, surjective, not proper, not quotient maps
  (ledger: S6-CUSP-DECOMPACTIFICATION-QUOTIENT REFUTED). Corollary `cusp-cone-sharp-global-R4-scope`.
Ledger: S6-CUSP-SPHERE-MOVING-S4, S6-CUSP-SPHERE-LITERAL-R4-OPEN-CELLS (VERIFIED).

### 1.3 `W\research\cusp_sphere_fixed_metric.tex` (35.8 KB, 917 lines) — read in full
Label prefix `sphere-metric-`. Theorem `sphere-metric-uniform-collapse` (any fixed compatible metric:
slices Hausdorff-converge to the smash base point); Theorem `sphere-metric-fixed-realization` (explicit
metric `g_A = dr^2 + r^2 du^2 + (r/T(r))^2 h_{T(r)}`, `g_B = g_C = dr^2 + r^2(du^2 + d theta^2)` near the
cone; slice blow-ups by `T/r_T` resp. `l_T/r_T` converge to `R^4`, ambient blow-ups to `R^8`, `R^12`);
Theorem `sphere-metric-scaling-trichotomy` (limit is a point, a square flat `T^4`, or `R^4` as
`lambda_T r_T -> 0, L, infinity`); Corollary `sphere-metric-unit-volume`; Proposition
`sphere-metric-tangent-scope` (links `T^3*T^3`, `(T^2)^{*4}`, `partial(M^4)`; local homology of
`C^{^4}` at the base point). Ledger: S6-CUSP-SPHERE-FIXED-METRIC (VERIFIED).

### 1.4 `W\research\cusp_s12_carrier_homotopy.tex` (25.3 KB, 609 lines) — read in full
- Theorem `cusp-s12-full-carrier-null` (l.40-110): `[x ^ y] = 0 in pi_12(S^6)` for all `x, y: S^6 -> S^3`.
- Corollary `cusp-s12-all-higher-smashes-null`; Remark `cusp-s12-one-copy-invariant` (the regular fibre of
  `q^_3` is a `T^3` = mapping torus of the kernel 2-torus over the circle `|t| = r_0`).
- Subsection "The original cusp coefficient: an explicit framed nullbordism": Theorem `cusp-null:thm`
  (l.242-565), `g = q^_3` is based null-homotopic; Corollary (`a = 0 mod 12`, `E^6 g = 0`). The same
  theorem appears as `h24:thm:cusp-g-zero` in `higher_rung_24d_continuation.tex`.
Ledger: S6-CUSP-ONE-COPY-FRAMED-NULL (VERIFIED), M-CUSP-ONE-COPY-FRAMED-NULL.

### 1.5 `W\research\higher_rung_24d_continuation.tex` (304 KB) — only l.4375-5112 and l.5750-6110 read
(the block `RETAINED_ANGLE_AND_HOPF_BRIDGE_20260905`; it is where the ledger entries
S6-CUSP-RETAINED-ANGLE-ARF and S6-CUSP-HOPF-NONZERO-MOD24 point).
- Theorem `h24:ret:main` (l.4524-4536; proof to l.5051): `H = p_3 q_2: X -> S^4`,
  `p_3([r,z]) = [r, c_3(z)]`, `c_3: T^3 -> T^3/K^(2) = S^3` (collapse of the coordinate 2-skeleton of
  `S^1_phi x Tbar^2`), target `Sigma_r S^3 = S^4`; `[H] = eta_4 o eta_5 != 0 in pi_6(S^4) = Z/2`.
- Corollary `h24:ret:q2-detected-quotient` (l.5070): `q_2` is not null; odd multiples of `[q_2]` nonzero.
- l.5112-5750 (`h24:rettri:*`, "three-dimensional bundle inside the triality carrier"): not read (outside topic).
- Theorem `h24:hbridge:mu-theorem` (l.5817): `mu_eta: pi_6(S^4) -> pi_9(S^6)`, `[x] -> [eta_2 ^ x]`,
  injective, `[eta_2 ^ H] = 12 nu_6`. Theorem `h24:hbridge:peripheral-theorem` (l.5970):
  `Psi_H = mu_eta o Theta_H o chi: SL_2(Z) -> pi_9(S^6)`, values `(12 nu_6, 0, 12 nu_6)` on `(C_0, C_1, C_2')`.

### 1.6 `W\research\cusp_globalization_replacement.tex` (28.5 KB, 739 lines) — read in full
Not on my list, but it holds the statements the cone files depend on and the ledger entries
S6-CUSP-FOUR-COPY-R4 and S6-CUSP-LITERAL-COMPACT-EXTENSION. One theorem,
`cusp-spec-globalization-obstruction` (marked \Verified), parts (i)-(vi):
(i) `chi_gamma = (f, theta_gamma): f^{-1}(B^o) -> B^o x R/Z`, fibrewise group epimorphism with kernel the
`T^3`-family of `L`; `Hom(Lambda,Z)^Delta = Z eps_gamma` (l.319-326);
(ii) circumference `l_T = D_T / sqrt(L_T^2 + m_T^2) = T + H - B + O(1/T)`;
(iii) four copies, minimality;
(iv) finite fillings: `Phi_j(s,x) = (e^{-2 pi i/m_j} s, A_j x + v_j/m_j)`,
`(m_1, v_1, kappa_1) = (3, gamma^+2u^-4w^, 1)`, `(m_2, v_2, kappa_2) = (4, -gamma^-3u^+3w^, -1)`,
`kappa_j = eps_gamma(v_j)`; Seifert targets `C_j = Delta_j x R/Z / ((s,theta) ~ (e^{-2 pi i/m_j}s, theta + kappa_j/m_j))`,
solid-torus chart `w = s u^{r_j}`, `U = u^{m_j}`, `t_j = w^{m_j} U^{-r_j}`; `N_j -> C_j` is a smooth proper
`T^3`-bundle; overlap identity `chi_gamma o h_j = h_j^{S^1} o chibar_j` (l.474-502);
(v) cusp nonextension (proof l.551-657): two radial paths with `B_0 a = (1/4,1/4)`, `B_0 a' = (1/4,1/2)`
converge to the same triple point of `W` and carry `theta_gamma = 3/4` and `1/2`; the class of
`theta_gamma` in `H^1` does extend over `N_0` (`pi_1(N_0) = Lambda/K`), "hence a map to `S^1` whose
restriction is homotopic to `chi_gamma`" (l.645-657);
(vi) products/smashes, Borel-Serre.

### 1.7 `R\s6_cone_sphere_routes_preprint.tex` (224.7 KB, 5561 lines; dated "5 September 2026")
Title "Real S^12 and S^24 Routes from Alpoge's Candidate (3,4,infinity) Two-Torus Fibration". Read:
abstract and status paragraph (l.43-160), all section and theorem headings, l.1485-2130, l.3418-3470,
l.3590-3640, l.3712-3946; the rest compared by heading with the research files.
It is an assembly, with its own labels, of: the input data and `cusp_globalization_replacement`
(sections 1; "Why the literal circle map cannot cross the cusp" l.553-595), `cusp_cone_sphere_routes`
(sections 2-3, 7), `cusp_sphere_route_strengthening` (section 4), `cusp_sphere_fixed_metric` (section 5),
`cusp_s12_carrier_homotopy` (l.1491-1617 and l.3947-4357), and the retained-angle and Hopf blocks of
`higher_rung_24d_continuation` (l.4358-5460). It contains five items that are not in the four research
files I was given:
- Theorem `thm:one-copy-framing-reduction` (l.1619-1772): stable framings of a closed oriented 3-manifold
  form a torsor with stages `H^1(N;Z/2)` (spin) and `H^3(N;Z)`; an honest rank-3 twist changes the
  Pontryagin-Thom class by `2 nu`; `[T^3, Lie] = eta^3 = 12 nu`. Standard (Kirby-Melvin, Levine, Adams
  are cited); it is the general frame for C1-2 below.
- Corollary `cor:smash-join-product-separation` (l.1833): joins are null; `h^{x r}` is null iff `h` is.
- Theorem `thm:SU3-clutching-scope` (l.1986-2125): `SU(3)`-bundles `P_k` on the moving `S^4`; they do not
  extend over the ambient sphere; pullbacks along the null sphere maps are trivial;
  `pi_7(SU(3)) = 0`, `pi_11(SU(3)) = Z/4`. Routine.
- Section "The nine-dimensional Gram carrier" (l.3418-3711): `Mat_3(C)/U(3) = Herm_3^+`, one-point
  compactification `B^9`, boundary `S^8`; "no structure-preserving bridge is constructed". Not about `S^6`.
- Section "An ancillary finite-cover route" (l.3712-3827): `S_N = diag(1,1,N,N)`,
  `S_N^{-1} M_0^N S_N = M_0` (ledger S6-CUSP-FINITE-COVER-R4-AUXILIARY).
Lemma l.949 "The cone attachment as a collapsed-boundary quotient" records `C = M/partial M`.

### 1.8 Ledgers (`W\research\ledgers\`)
`claim_ledger.txt` lines 3-6, 60-62, 74-75, 113-115 read in full; `morphism_ledger.txt` lines 2-8, 48-52,
85-87 read (M-CUSP-SPHERE-Q3, -QGAMMA, -Q3-SMASH, -QGAMMA-SMASH, -U12/U24-OPEN-CELL,
M-CUSP-DECOMPACTIFICATION-BETA-QUOTIENT (REFUTED), M-CUSP-CONE-Q2, -Q2-SMASH, -Q1-LOCAL, -Q1, -Q1-SMASH,
M-CUSP-ONE-COPY-FRAMED-NULL, M-CUSP-RETAINED-ANGLE, M-CUSP-HOPF-PERIPHERAL). The ledger statements agree
with the tex. Two points: (a) S6-CUSP-SPHERE-MOVING-S4 proves `g ^ g = 0` by "Toda Prop. 5.11:
`st: pi_12(S^6) -> pi_6^S` is an isomorphism, `st(g^g) = (2a nu)^2 = 4a^2 nu^2 = 0`", while
`cusp_s12_carrier_homotopy.tex` uses the exponent argument (C1-6); `mathematical_summary.tex` l.2000-2035
has the Toda version. Both are correct. (b) entries 113-115 (5 Sep) use a shorter schema without
`depends_on`. `next_lemmas.tex` l.430-452 and `uncertainties.txt` (U-CUSP-SPHERE-*, U-CUSP-CONE-SPHERE-ROUTES,
U-CUSP-GLOBAL-R4-GENERALIZATION) repeat the same status.

### 1.9 Evidence folders
- `W\evidence\cusp_framing_20260905\`: `MATHEMATICAL_AUDIT.md` (result, the repaired smoothing-neighbourhood
  mismatch), `verify_framing_jacobian.py` + `FRAMING_JACOBIAN_CHECK.json` (five sympy identities:
  `B_0 u_0 = (1/4,1/4)`, `det J = det(l B_0 + lambda R)`, `det J_0 = l^2`), `PROOF_INTEGRATION_RECEIPT.json`,
  build and visual-QA receipts (workbench then 624 pages, cone/sphere preprint 51 pages). All read.
- `W\evidence\retained_angle_20260905\`: `MATHEMATICAL_AUDIT.md` (18.6 KB, ten sections; a careful
  second-agent audit of `h24:ret:main`, with the full frame `D(a,b) G_0`,
  `D(a,b) = diag(e^{-i(a+b)}, e^{ia}, e^{ib}) in SU(3)`, the explicit contraction, the spin quadratic form
  `q(xe+yf) = x + xy + y`, the smoothing-order repair, and the remark that sphere recognition is used
  exactly to pass from the chart framing to `pi_6(S^4)`), `verify_retained_angle_frame.py` +
  `RETAINED_ANGLE_EXACT_CHECKS.json` (12 sympy checks), receipts. All read.

### 1.10 `W\research\mathematical_summary.tex` — grep and read l.268-292, 1672-1700, 1760-1780, 1940-2050, 2256-2282, 3700-3732
Summarises the above with the same statuses; nothing additional. `literature_log.tex` l.480-520 repeats
the two smash-null arguments.

### 1.11 Baselines consulted
- [E26] Remark 8.3 (`literature\engel_S6.txt` l.1208-1247).
- [AC26] `original_clean_transcription.tex` l.111 (summary page): the formula
  `pi_1 = Z/|12 l_0 - 4 l_1 - 3 l_2|` "admits a reading, which the body does not use": it is Orlik's
  formula for `H_1` of the Seifert space over `S^2(3,4)`, and "heuristically the twist condition says: glue
  so that the coinvariant circle of the fibres traces out the (3,4) Seifert fibration of the three-sphere
  over the base". So the map `S^6 -> S^3` of Engel's Remark 8.3 is already foreshadowed in [AC26] as a
  heuristic; neither source constructs it with proof.

---

## 2. Candidates

### C1-1. The fibrewise circle quotient (Engel's S^6 -> S^3): exact Seifert targets at the two multiple fibres, and proof that the literal quotient does not extend continuously across the cusp fibre
**Type**: refinement of [AC26] (makes its heuristic "reading" precise) / correction of the literature
([E26] Remark 8.3, wording of the extension at infinity).

**Where**: `cusp_globalization_replacement.tex`, Theorem `cusp-spec-globalization-obstruction` (i), (iv),
(v), proof l.293-349, 443-502, 551-657; ledger S6-CUSP-FOUR-COPY-R4 (VERIFIED) and
S6-CUSP-LITERAL-COMPACT-EXTENSION (REFUTED = "the literal extension is refuted"); used in
`cusp_cone_sphere_routes.tex` Theorem `cusp-cone-S24-route`. Research log Round 29, 3 Sep 2026.

**Statement**. (a) `Hom(Lambda,Z)^Delta = Z eps_gamma`, and
`chi_gamma([z, Pi(z)x]) = ([z], eps_gamma(x) mod Z)` is a real-analytic fibrewise group epimorphism
`f^{-1}(B^o) -> B^o x R/Z` with connected kernel the `T^3`-family of `L = Z<u^,w^,delta^>`.
(b) At `p_j` (`j = 1,2`, `m_j = 3,4`) the filling generator `Phi_j(s,x) = (e^{-2 pi i/m_j}s, A_j x + v_j/m_j)`
shifts the character by `kappa_j/m_j`, `kappa_1 = 1`, `kappa_2 = -1`, so `chi_gamma` descends to
`N_j -> C_j = Delta_j x (R/Z) / ((s,theta) ~ (e^{-2 pi i/m_j}s, theta + kappa_j/m_j))`, a smooth proper
`T^3`-bundle over a solid torus whose projection to `D_j` has a central circle of multiplicity `m_j`;
the gluing with the regular part is `h_j^{S^1}(z,theta) = (z, theta + beta_j(z))`,
`beta_j(g_j z) = beta_j(z) - kappa_j/m_j`. (c) The glued 3-manifold `M` (over `B` minus the cusp disc) has
`H_1(M) = Z`, `rho_0 = -g, rho_1 = 4g, rho_2 = -3g, eta = 12g`. (d) `theta_gamma` has no continuous
extension to `W`: for `x_T(a) = exp(2 pi i Z_T a)` the logarithmic position is
`B_0 a + Im C(t) a / T` and `theta_gamma(x_T(a)) = a_1`; `a = (-1/4, 1/4)` and `a' = (-1/2, 1/4)` both
converge to the triple point of the chart `(z_0,z_1,z_2) = (t/(x_1x_2), x_1, x_2)` with values `3/4` and
`1/2`. (e) The class of `theta_gamma` in `H^1` extends over `N_0`.

**Support**. Written proofs (about 6 pages); the matrices are those of `exact_algebra.tex`
Prop. `monodromy-certificate`. The workbench marks all of it VERIFIED.

**What it adds**. Over [AC26]: the original has only the heuristic sentence at l.111. Over [E26]: Remark 8.3
describes the same quotient and says that over the cusp "this quotient map of the first paragraph extends
continuously to the composition of the moment mapping with a further quotient to a circle". Statement (d)
shows that the literal fibrewise group quotient does not extend: near a triple point the character is
`theta ~ -log|z_2| / log|t|`, which takes every value on approach to the double curves `z_0 = z_2 = 0` and
`z_1 = z_2 = 0` (it does extend along the third double curve, which matches Engel's "distinguished edge").
What exists is a map homotopic to it near the cusp (Engel's Clemens collapse followed by the moment map;
or any representative of the extended `H^1`-class). So Engel's remark is right up to homotopy and wrong as
literally worded; the workbench has the exact statement and the proof, eleven days earlier.
Literature: WebSearch for the S^6 -> S^3 quotient/Seifert map and its class in pi_6(S^3) found only the
construction papers (AC26, Engel, and Z. Wang arXiv:2609.11541 on a rational homology 6-sphere); no
treatment of this map.

**First assessment**. Solid. I rederived (d) independently from `log|x| = A(t)u`, `A(t) = l B_0 + R(t)`:
the set-valued limit of `pibar` at a double curve is the corresponding closed edge of the `A_2`
triangulation of `Tbar^2`, and `eps_gamma` is non-constant on two of the three edge classes
(`B_0^{-1}e_1 = (0,1)`, `B_0^{-1}e_2 = (-1,0)`, `B_0^{-1}(e_1-e_2) = (1,1)`). I checked (c) by hand.
Not noticed by the workbench: `M` is the exterior of the torus knot `T(3,4)` in `Q = S^3` (its
presentation of `pi_1(M)` is the torus-knot group `<x,y | x^3 = y^{-4}>`), filling `M` along `rho_0` gives
Engel's `Q = S^3` (the only slope with trivial `H_1`), and `C = Q/(fibre over p_0) ~ S^2 v S^3`, which is
what the workbench computes for `C`. So `q_1 ~ kappa o e`, where `e: X -> Q` is Engel's map (made
continuous near `W`) and `kappa: S^3 -> S^3 v S^2` is the inclusion of the first summand up to homotopy.

**A full check must establish**: the monodromy matrices and `v_j` against [AC26] sections 3 and 6; the
equivariance and freeness in (b); the overlap identity; the two limits in (d) in the actual toric chart
of [AC26] section 4; that Engel's `epsilon` (Lemma 3.8) is `eps_gamma`.

**Deserves a full check**: yes — it is the only place where Engel's Remark 8.3 map is actually constructed
with proofs, and it corrects the remark's wording. **Interest**: 4.

### C1-2. The homotopy class of Engel's map `e: S^6 -> S^3` in `pi_6(S^3) = Z/12`: left open by the workbench; a short argument from workbench data gives the element of order 2
**Type**: open question isolated (with a proposed answer by this reader, not in the workbench, not verified).

**Where**: the workbench records as OPEN "the based homotopy class of `q_1^{^4}`" and never mentions the
class of `q_1` or of a map to `S^3 = Q` (`cusp_sphere_route_strengthening.tex` l.661-676, ledger
S6-CUSP-CONE-SPHERE-ROUTES nonclaim). By C1-1, `[q_1] in pi_6(S^2 v S^3)` and `[e] in pi_6(S^3)` determine
each other. The workbench's `[q^_3] = 0 in pi_6(S^3)` is about a different map (C1-4) and says nothing
about `e`.

**Statement (proposed)**. Let `e: X -> Q = S^3` be the fibrewise quotient by the invariant 3-torus, made
continuous near `W`. Then `E^infty[e] = eta^3 = 12 nu in pi_3^S = Z/24`, so `[e]` is the unique element
of order 2 of `pi_6(S^3)` (`= eta_3 o eta_4 o eta_5`). In particular `e` is essential. Independently of
this value, `f: X -> P^1` is null-homotopic as a map `S^6 -> S^2`.

**Support (reader's argument, about one page; to be checked)**.
1. Pontryagin-Thom: a regular fibre of `e` is one coset of the `L`-torus `T^3` in a regular fibre
   `F = F_t`; its normal framing is (lift of a base frame, the direction dual to `d theta_gamma`).
2. Let `tau_1` be the framing of `TX|_F` by translation-invariant fields plus a lifted base frame, `tau_0`
   the stable framing of `S^6`, and `d = tau_1 - tau_0 in [F, SO] = KO^{-1}(T^4)`. The framed-bordism class
   of the fibre is `[T^3, Lie framing twisted by d|_L]`. `d` is invariant under the monodromy group
   `Delta` (transport `F` around a loop; the Lie framing changes by a constant matrix in `GL_4^+(R)`).
3. `KO~^{-1}(T^4)` has the natural filtration with quotients `H^1(F;Z/2)` and `H^3(F;Z)`. The image
   `sigma` of `d` lies in `H^1(F;Z/2)^Delta = {0, eps_gamma mod 2}` (script), so `sigma|_L = 0`. This
   agrees with the workbench's independent local computation that the vanishing 2-torus carries the Lie
   spin structure (C1-3).
4. `2d` lies in `H^3(F;Z)^Delta = Lambda^Delta = Z delta^` (Poincare duality; script), and the class dual
   to `delta^` evaluates on `[L]` to the intersection number `delta^ . L = 0`. So `2(d|_L) = 0`; since
   `sigma|_L = 0`, `d|_L` lies in `H^3(L;Z) = Z`, hence `d|_L = 0`.
5. So the fibre is the Lie-framed `T^3`, class `eta^3 = 12 nu != 0`; stabilisation
   `pi_6(S^3) -> pi_3^S` is injective onto the even classes, which gives the statement.
6. `f = h o e` with `h: S^3 -> S^2(3,4)`, `h(z_1,z_2) = [z_1^4 : z_2^3]` = Hopf o (degree 12 map);
   a degree-`k` self-map of `S^3` acts on `pi_6(S^3)` by `k`, and `12 pi_6(S^3) = 0`; so `[f] = 0`.
   (Without `e`: `f = [s_1^3 : s_2^4]` for sections `s_j` of the topologically trivial bundles `O(S_j)`.)
Script `work\scratch\C1\check_invariants.py`: `A_1^3 = A_2^4 = I`, `A_1A_2M_0 = I`,
`Lambda^Delta = Z(0,0,0,1)`, invariant covectors `Z(1,0,0,0)`, mod-2 invariant covectors
`{0, (1,0,0,0)}`, `kappa_{delta^}(L) = 0`.

**What it adds**. [AC26]: nothing on this. [E26]: Remark 8.3 gives the map and no homotopy class. Literature:
searched (see C1-1), nothing found. If correct: the natural map `S^6 -> S^3` of the construction is
`eta^3`, and the holomorphic fibration `S^6 -> P^1` is null-homotopic.

**First assessment**. The argument is short and each step is standard, but it is mine, written during a
survey; the risks are in step 2 (identification of the Pontryagin-Thom framing with `tau_1`, and
`Delta`-invariance of `d`), in the naturality used in steps 3-4, and in the existence of a continuous `e`
that is the literal quotient away from `W` (C1-1(e) gives it). Signs do not matter for a class of order 2.
Consistency checks passed: the value is even (in the image of `pi_6(S^3)`); `q^_gamma ~ lambda o e` with
`lambda: S^3 -> S^2` of Hopf invariant 0 is null (C1-5); `sigma|_K = 0` matches Arf = 1 in C1-3.

**A full check must establish**: steps 1-6 in full, in particular the framing comparison of step 2 with
explicit conventions; an independent computation (for example the e-invariant of the framed `T^3`, or the
bordism through the Seifert solid tori) would be worth having.

**Deserves a full check**: yes — a concrete, new-looking invariant of the construction, answering a
question Engel's remark leaves open. **Interest**: 4.

### C1-3. The retained-angle map `H = p_3 q_2: X -> S^4` is `eta_4 o eta_5 != 0`; the vanishing 2-torus of the cusp is Lie-framed (Arf invariant 1)
**Type**: computation / new result (small).

**Where**: `higher_rung_24d_continuation.tex` l.4378-5107, Theorem `h24:ret:main`, Corollary
`h24:ret:q2-detected-quotient`; preprint l.4358-5088; evidence `retained_angle_20260905\`; ledger
S6-CUSP-RETAINED-ANGLE-ARF (VERIFIED). 5 Sep 2026.

**Statement**. `H(x) = [r, c_3(e^{i phi}, pibar_f(x))] in Sigma_r(T^3/K^(2)) = S^4`. For the regular value
`r_0 e^{i pi}`, `u_0 = (-1/4,1/4)`, the whole fibre is the torus
`w(a,b) = (rho_0 e^{i(pi-a-b)}, rho_1 e^{ia}, rho_2 e^{ib})`, `(rho_0,rho_1,rho_2) = (r_0^{1/2}, r_0^{1/4}, r_0^{1/4})`,
in the chart `w = F(z)`, `F(z) = (z_0/(h_1h_2), h_1z_1, h_2z_2)`, `h_j = exp(-2 pi i (C(t)u_0)_j)`,
`t = w_0w_1w_2`. Its derivative framing differs from a constant by
`D(a,b) = diag(e^{-i(a+b)}, e^{ia}, e^{ib}) in SU(3)`, which is null-homotopic, so the stable framing is the
Lie framing; the spin quadratic form is `q(xe+yf) = x+xy+y`, Arf = 1; hence `E^infty[H] = eta^2` and
`[H] = eta_4 eta_5 in pi_6(S^4) = Z/2`. Consequently `q_2: X -> Susp(T^3)` is not null-homotopic.

**Support**. Proof of about 12 pages with explicit differential table; a separate adversarial audit (ten
sections, one ordering defect found and repaired); 12 exact sympy checks. Sphere recognition is used once,
to compare the chart framing with the framing of `S^6` on a contractible ball.

**What it adds**. Not in [AC26] or [E26]. The geometric content: in the local model `t = w_0w_1w_2` the fibre
2-torus `{|w_j| = rho_j, arg t fixed}` with its fibration framing represents `eta^2 in pi_2^S`. This is a
statement about the normal-crossings triple point (the same holds for any such degeneration in a ball); it
is not specific to `S^6`. Literature not searched; I would expect it to be folklore (it is the statement
that vanishing cycles carry the Lie framing relative to the fibre framing, as for Lefschetz thimbles).

**First assessment**. Correct as far as I can see. Two independent sanity checks: (1) the spin structure of
the product-bounding framing on `T^3 = {|w_j| = rho_j}` is `(1,1,1) in H^1(T^3;Z/2)` relative to Lie;
restricted to the subtorus spanned by `(1,-1,0)`, `(0,1,-1)` it is `0`, i.e. Lie, Arf = 1; (2) monodromy
invariance forces `sigma|_L = 0` globally (C1-2 step 3).

**A full check must establish**: the fibre identification in the chart, the differential table, the
`SU(3)` contraction, the Arf computation, the use of Pontryagin-Thom for a map that is only continuous
away from the fibre.

**Deserves a full check**: maybe — correct-looking and cheap to confirm, modest interest; it is an input
for C1-2. **Interest**: 3.

### C1-4. The one-copy map `q^_3: X -> S^3` is null-homotopic (explicit framed nullbordism)
**Type**: computation.

**Where**: `cusp_s12_carrier_homotopy.tex` l.188-594, Theorem `cusp-null:thm`; preprint l.3947-4357;
evidence `cusp_framing_20260905\`; ledger S6-CUSP-ONE-COPY-FRAMED-NULL (VERIFIED). 5 Sep 2026.

**Statement**. `g(x) = [|t|, c(pibar_f(x))]` on `0 < |t| < eps`, `g(W) = g(X \ int N_0) = *`. The fibre over
`[r_0, c(3/4,1/4)]` is `T_{r_0} = {|w_0| = r_0^{1/2}, |w_1| = |w_2| = r_0^{1/4}}`; its framing is
`N J(t) H^{-1}` with `det J = det(l B_0 + R(t))`, homotopic to the constant-matrix radial framing, which
extends over the bordism `{|w_0|^2 + q(v) = rho_0^2, |w_1| = rho_1, |w_2| = rho_2} = D^2 x T^2` in
chart x `[0,1]` (the workbench's `\mathcal W`; `q(v)` a smooth cut-off profile). Hence
`[g] = 0 in pi_6(S^3)`, `a = 0`, `E^6 g = 0`.

**Support**. Six-page proof, sympy check of the Jacobian identities, audit note.

**What it adds**. Not in [AC26]/[E26]. But `q^_3` is not Engel's map: its target is
`Sigma(Tbar^2/1-skeleton)`, a suspension of a collapse of the rank-2 cusp quotient, supported in the cusp
neighbourhood. The result is local.

**First assessment**. Correct. It also has a five-line proof that the workbench missed: the two classes of
`pibar_f` in `H^1(N_0 \ W)` extend over `N_0` (the workbench says so for `eps_gamma`,
`cusp_globalization_replacement.tex` l.645-657; the `u^`-coordinate is also `M_0`-invariant and kills
`K`); replace `pibar_f` by a continuous `pi': N_0 -> Tbar^2` in the same class; the straight-line homotopy
is continuous into `Sigma_r(S^2)` because the end `r = 0` is collapsed; and `[r, c(pi'(x))]` factors
through `([0,eps] x Tbar^2)/({eps} x Tbar^2) = Cone(T^2)`, which is contractible. The same argument does
not apply to `H` of C1-3 (keeping `e^{i phi}` one lands in `(D_0 x Tbar^2)/(partial D_0 x Tbar^2)`, which
is not contractible), so it is consistent with C1-3.

**A full check must establish**: nothing beyond the short argument, or the framing computation as written.

**Deserves a full check**: no — true for a soft reason, and about a self-posed map. **Interest**: 2.

### C1-5. The class `[q^_gamma] in pi_6(S^2)`, recorded as OPEN, is zero
**Type**: open question isolated (resolved by a short argument of this reader; not in the workbench).

**Where**: stated open in `cusp_sphere_route_strengthening.tex` l.672-675, `mathematical_summary.tex`
l.2044 and l.3717-3719, ledger S6-CUSP-SPHERE-MOVING-S4 (nonclaim), M-CUSP-SPHERE-QGAMMA, `next_lemmas.tex`
l.448.

**Statement**. `q^_gamma(x) = [r, theta_gamma(x)] in Sigma_r(S^1) = S^2` on `N_0 \ W`, constant elsewhere,
is null-homotopic.

**Support**. The argument of C1-4 with `theta'`: `N_0 -> S^1` continuous in the class of `eps_gamma`
(exists, same reference): `q^_gamma ~ [r, theta'(x)]`, which factors through
`([0,eps] x S^1)/({eps} x S^1)`, a disc. Equivalently `q^_gamma ~ lambda o e` with `lambda: S^3 -> S^2`
of Hopf invariant 0 (the fibres of `lambda` are meridian circles of the solid torus over `D_0`, unlinked).

**What it adds**. Closes an item the workbench lists as open; shows that the angle-forgetting sphere maps
carry no information.

**First assessment**. I see no gap; the one point to check is the continuity of the homotopy at `W`
(uniform because every neighbourhood of the suspension point contains `{r < delta}`), and that the classes
of `theta_gamma` and `theta'` agree in `H^1(N_0 \ W)` (both vanish on the zero-section loop, which bounds
the toric zero-section disc, ledger S6-TOP-V1).

**A full check must establish**: those two points.

**Deserves a full check**: maybe — ten minutes; it changes a status line. **Interest**: 2.

### C1-6. General homotopy statements: `x ^ y = 0` for `x,y in pi_6(S^3)`; `f^{^r} = 0` for `f in pi_6(S^2)`, `r >= 2`
**Type**: new proof or restatement of a known result (elementary consequences of the tables).

**Where**: `cusp_s12_carrier_homotopy.tex` Theorem `cusp-s12-full-carrier-null`, Corollary
`cusp-s12-all-higher-smashes-null`; `cusp_sphere_route_strengthening.tex` Corollary
`cusp-cone-S24-sphere-map-null`; ledger S6-CUSP-SPHERE-MOVING-S4. Round 36, 3 Sep 2026.

**Statement and proofs**. (a) `x ^ y = (E^3 x) o (E^6 y)` (Toda, Prop. 3.1, sign `+`); `12 y = 0` so
`E^6 y in pi_12(S^9) = Z/24` is even, `= 2 gamma`; postcomposition is additive, `pi_12(S^6) = Z/2`; so
`x ^ y = 2 (E^3x)_* gamma = 0`. Ledger variant: `st: pi_12(S^6) -> pi_6^S = Z/2<nu^2>` is an isomorphism
(Toda Prop. 5.11) and `st(g ^ g) = (2a nu)^2 = 4a^2 nu^2 = 0`. (b) `f ^ f = (id ^ f) o (f ^ id_{S^6})`,
`f ^ id = Sigma^6 f in pi_12(S^8) = pi_4^S = 0` (stable since `12 <= 2*8 - 2`). (c) higher powers by
smashing the null-homotopy.

**Arithmetic checked**: `pi_6(S^3) = pi_6(S^2) = Z/12`; `pi_3^S = pi_12(S^9) = Z/24`; `pi_6^S = Z/2<nu^2>`;
`pi_12(S^6) = Z/2<nu_6 nu_9>` and it stabilises isomorphically; `pi_12(S^8) = pi_4^S = 0`; `E^infty` on
`pi_6(S^3)` is injective with image the even classes. All correct. Left distributivity
`alpha o (beta_1 + beta_2) = alpha o beta_1 + alpha o beta_2` is the one used, and it always holds.

**What it adds**. Nothing to [AC26]/[E26]. Standard; a homotopy theorist would call (a) and (b) exercises.
"Optimality of the two-copy and four-copy routes" is a separate statement (C1-9), unrelated to these.

**Deserves a full check**: no — correct and standard. **Interest**: 1.

### C1-7. "Hopf nonzero mod 24": `[eta_2 ^ H] = 12 nu_6 in pi_9(S^6) = Z/24`, and the "peripheral homotopy morphism" `Psi_H`
**Type**: computation (formal).

**Where**: `higher_rung_24d_continuation.tex` l.5752-6110, Theorems `h24:hbridge:mu-theorem`,
`h24:hbridge:peripheral-theorem`; preprint l.5089-5460; ledger S6-CUSP-HOPF-NONZERO-MOD24, M-CUSP-HOPF-PERIPHERAL.

**Statement**. What is nonzero: the class of `eta_2 ^ (H o d): S^3 ^ S^6 = S^9 -> S^2 ^ S^4 = S^6`, equal to
`eta^3 = 12 nu` in `pi_9(S^6) = pi_3^S = Z/24` (order 2); after three suspensions, `12 nu_9 in pi_12(S^9)`.
`Psi_H = mu_eta o Theta_H o chi: SL_2(Z) -> pi_9(S^6)`, with `chi: SL_2(Z) -> Z/12` the abelianisation
(`chi(C_0,C_1,C_2') = (-1,4,-3)`) and `Theta_H([n]) = n[H]`; values `(12 nu_6, 0, 12 nu_6)`, kernel
`chi^{-1}(2Z/12)`.

**First assessment**. The first part is `eta . eta^2 = eta^3 = 12 nu` applied to C1-3; correct and
contentless beyond C1-3. `Psi_H` is the composite of the abelianisation of `SL_2(Z)` with the homomorphism
`n -> n[H]`, which is not induced by any geometric construction; it is "reduction mod 2 of chi" written
in `pi_9(S^6)`. No mathematics about `S^6`. (Remark: by C1-2, `eta^3 = 12 nu` is, if my argument holds, the
stable class of Engel's map itself; the workbench reaches the same element by a formal smash with `eta_2`.)

**Deserves a full check**: no. **Interest**: 1.

### C1-8. Topology of the targets: `C ~ S^2 v S^3`, `pi_1(M)`, homology and homotopy types of the smash targets, local homology at the cone points
**Type**: computation.

**Where**: `cusp_cone_sphere_routes.tex` (homology in the three route theorems);
`cusp_sphere_route_strengthening.tex` Proposition `cusp-cone-explicit-carriers`, Theorem
`cusp-cone-target-homotopy-types`; `cusp_sphere_fixed_metric.tex` Proposition `sphere-metric-tangent-scope`
(eq. `sphere-metric-C-smash-local-homology`).

**Statement**: as listed in 1.1-1.3 (for example `H~_k(A^A) = Z^9, Z^18, Z^15, Z^6, Z` in degrees 4..8;
`H_i(C^{^4}, C^{^4} \ *) = Z^{binom(4,i-1)}` for `2 <= i <= 5`, `Z^{binom(4,i-8)}` for `8 <= i <= 12`).

**First assessment**. Routine and, where I checked (the `H_1(M)` presentation, `C ~ S^2 v S^3`, the
Kuenneth ranks), correct. The one item with outside meaning is `M` and `C`, see C1-1.

**Deserves a full check**: no. **Interest**: 1.

### C1-9. Optimality of two copies (cusp-local) and four copies (full base); no finite base cover preserves `K`
**Type**: new result (elementary), for a self-posed question.

**Where**: `cusp_sphere_route_strengthening.tex` Theorem `cusp-cone-optimal-exponents`;
`cusp_cone_sphere_routes.tex` Theorem `cusp-cone-obstructions` (1)-(2);
`cusp_globalization_replacement.tex` (iii) and proof l.400-441; ledger S6-CUSP-CONE-OBSTRUCTIONS.

**Statement**. If `N c Lambda^{(+)r}` is primitive and the quotient systole (unscaled Euclidean metric on
the radial cusp fibres) tends to infinity, then `K^{(+)r} c N`, so rank `<= 2r`; if `N` is invariant under
the full monodromy, or under a finite-index subgroup, then `L^{(+)r} c N`, rank `<= r`, because
`A_1 w^ = u^ - w^` and `(A_2A_1)^n w^ = w^ + n(u^ - delta^)`.

**First assessment**. Correct (I recomputed `A_2A_1` in the script). The content with outside meaning is
only: `K` is not preserved by any finite-index subgroup of the monodromy group, and `L` is the smallest
invariant lattice containing `K`. "Optimal" is relative to a class of constructions chosen by the author.

**Deserves a full check**: no. **Interest**: 1.

### C1-10. Metric statements (grouped)
**Type**: computation / expository, for a self-posed question.

**Where**: `cusp_cone_sphere_routes.tex` (limits, Proposition `cusp-cone-metric-scope`);
`cusp_sphere_route_strengthening.tex` (moving 4-spheres, open cells, `E_nu`); `cusp_sphere_fixed_metric.tex`
(all); ledgers S6-CUSP-SPHERE-FIXED-METRIC, S6-CUSP-SPHERE-LITERAL-R4-OPEN-CELLS,
S6-CUSP-DECOMPACTIFICATION-QUOTIENT (REFUTED).

**Statements**. (1) `(Q_T^2, 0)` and `(C_T^4, 0) -> (R^4, 0)` pointed GH, with exact Euclidean `R`-balls
once the systole exceeds `4R`; the same for the quotient length metrics on the moving 4-spheres at the
midpoint base points. (2) In any fixed metric compatible with the compact target, the slices converge to
the smash base point. (3) For the explicit cone metrics, the slice blown up by `lambda_T` has limit a
point, `(R/LZ)^4` or `R^4` according as `lambda_T r_T -> 0, L, infinity`, the vertex is at rescaled
distance exactly `lambda_T r_T`, and the full ambient bubbles are `R^8` and `R^12`; unit-volume
normalisation gives the square flat torus. (4) `E_nu = ([0,s_0] x R^4)/~` is a 5-manifold with boundary
fibre `R^4`. (5) REFUTED: that `beta_nu: E_nu -> D_nu = Cone(T^4)` is a quotient map (so that the cone
would be `E_nu` with the boundary `R^4` collapsed): the set `{[s_j, A_{1/s_j} a]}`, `a` not in `Z^4`, is
closed and saturated but its image accumulates at the vertex.

**First assessment**. All of it is elementary flat-torus geometry and point-set topology and looks correct.
The only inputs from the complex structure are `sys(Q_T) >= T - C` and
`l_T = T + H - B + O(1/T)`, which belong to the cusp spectral files (another reader). The two REFUTED
entries are refutations of the workbench's own earlier over-readings: (5), and the literal extension of
C1-1(d), which is the one with outside meaning.

**Deserves a full check**: no. **Interest**: 1.

### C1-11. Three proofs that no homotopy `S^12` is almost complex; list of obstructions
**Type**: expository only (known: Borel-Serre 1953).

**Where**: `cusp_cone_sphere_routes.tex` Proposition `cusp-cone-S12-almost-complex-obstruction`, Theorem
`cusp-cone-obstructions` (3)-(6).

**First assessment**. The exact identity `P^1_5(c_2) = s_5 s_1 - s_6 = 6 c_6 + (terms in c_1..c_5)` is right
(`s_6 = -6 c_6` modulo lower classes). No novelty.

**Deserves a full check**: no. **Interest**: 1.

### C1-12. Items found only in the preprint view
**Type**: expository / routine. Listed in 1.7: the framing-torsor theorem (standard; useful as the frame
for C1-2), smash/join/Cartesian corollary, `SU(3)` clutching, the Gram carrier `B^9/S^8`, the finite-cover
unspooling. None concerns the complex structure on `S^6` beyond the lattice identity
`S_N^{-1} M_0^N S_N = M_0`.

**Deserves a full check**: no. **Interest**: 1.

### Direct answers to the four questions of the assignment
1. Maps and classes. `q_2: X -> Susp(T^3)`: not null (C1-3), full class unknown.
   `q^_3 = p^_2 q_2: X -> S^3`: zero in `pi_6(S^3)` (C1-4). `H = p_3 q_2: X -> S^4`: `eta_4 eta_5`, the
   nonzero element of `pi_6(S^4) = Z/2`; "retained-angle Arf" is the Arf invariant 1 of its fibre torus.
   "Hopf nonzero mod 24": `[eta_2 ^ H] = 12 nu_6 in pi_9(S^6) = Z/24` (C1-7).
   `q_{1,cusp}: X -> Susp(T^2)`, `q_1: X -> C`: classes open in the workbench.
   `q^_gamma: X -> S^2`: open in the workbench; zero by C1-5.
   None of `q^_3`, `q^_gamma`, `H` is Engel's map. Engel's map is `q_1` before the cone: `q_1 ~ kappa o e`
   (C1-1). The workbench does not compute a class in `pi_6(S^3)` of a natural map coming from the fibration;
   its `pi_6(S^3)` result concerns the cusp-local `q^_3`, by a complete but unnecessary framed-bordism
   argument (the framed manifold is `T^3 = {|w_j| = rho_j}` in a polydisc chart with the product radial
   framing, bounding `D^2 x T^2`). For Engel's map itself, C1-2 proposes `eta_3 eta_4 eta_5`.
2. General statements: correct and standard (C1-6); arithmetic checked.
3. Metric statements: C1-10; what is REFUTED and why: C1-10(5) and C1-1(d).
4. Judgement. Real mathematics about the complex structure / the fibration: C1-1 (the circle quotient, its
   Seifert targets, the non-extension at the cusp), and the monodromy facts inside C1-9
   (`K = im(M_0 - I)`, `L` minimal invariant, unique invariant character). Real but local mathematics about
   the normal-crossings cusp: C1-3 (the vanishing 2-torus is `eta^2`). Everything else (the `S^12`/`S^24`
   smash sources, cone and suspension targets, moving 4-spheres, `R^4` limits, trichotomy, `E_nu`,
   optimality "within the class", `SU(3)` clutching, Gram carrier, the peripheral character `Psi_H`) answers
   a self-posed question; it is correct as far as I checked and of little outside interest. The smash
   powers have no geometric role: all the sphere-valued smash maps are null for reasons that hold for every
   map between those spheres. The most valuable thing in this material is what it leaves undone: the class
   of the natural map `S^6 -> S^3` (C1-2).

---

## 3. Doubts and errors

1. **[E26] Remark 8.3 versus the workbench** (C1-1): the remark says the fibrewise quotient "extends
   continuously" over the cusp fibre; the workbench proves the literal quotient does not
   (`cusp_globalization_replacement.tex` l.551-613). Not a workbench error; a point to state precisely in
   any write-up that cites Engel's map.
2. **"`[q^_gamma] in pi_6(S^2)` remains open"** (many places, see C1-5): it is zero by an argument whose
   key fact the workbench states itself (`cusp_globalization_replacement.tex` l.645-657). Underclaim.
3. **`cusp-null:thm`** (C1-4): six pages for a statement with a five-line proof; the workbench's remark
   `cusp-s12-one-copy-invariant` and the preprint's `thm:one-copy-framing-reduction` present the class
   `a in Z/12` as a delicate framing datum. For this map it is not.
4. **`Psi_H`** ("an exact nonzero peripheral homotopy morphism", C1-7): a formal composite with no
   geometric source; the wording "the particular original cusp map supplies ..." overstates it.
5. **Workbench does not identify `M`, `C`, `Q`**: `M` = exterior of `T(3,4)`, `C = S^3/T(3,4)`; so "the
   class of `q_1` is open" hides that it is the class of the natural map to `S^3`.
6. **Preprint abstract** (l.72-90) is accretive: it first says "Neither conclusion computes either one-copy
   sphere-map class" and then "For the specified `S^6 -> S^3` map we now compute that datum". Same pattern
   in Remark `cusp-s12-one-copy-invariant` ("does not need to determine ... It is now zero").
7. **Two different proofs of `g ^ g = 0`** in ledger and tex (1.8(a)); both correct; the ledger's evidence
   pointer names the tex theorem whose proof is the other one.
8. **`sphere-metric-tangent-scope`**: "Take `V_i = Cone(L_i)` and `A_i = L_i`, its outer boundary" — with the
   smash based at `v_0` (the image of `W`), the cone must be taken from the other end (`v_1` as cone
   vertex, the `r = 0` end as `A_i`). The conclusions are unaffected by the symmetry `r -> eps - r`.
9. Outside my topic, for the coordinator: the web search surfaced literature statements of the type "every
   holomorphic map from a complex `S^6` to a lower-dimensional complex space is constant" (arXiv:1912.09719
   and related), which depend on `a(X) = 0` and fall with CDP.
10. I found no mathematical error in the files of this assignment.

---

## 4. Not read

- `higher_rung_24d_continuation.tex` outside l.4375-5112 and l.5750-6110 (not my topic); within the
  retained-angle proof, l.4604-4840 (fibre lemma, differential table, orientation sign, frame contraction)
  I read through the audit `retained_angle_20260905\MATHEMATICAL_AUDIT.md` and the statement labels, not
  line by line.
- `s6_cone_sphere_routes_preprint.tex`: the parts that duplicate the research files (l.161-1484,
  l.2127-3417, l.3947-5460) were compared by headings and spot reading, not reread in full; the Gram
  carrier section l.3470-3590, l.3640-3711 and the proof of the finite-cover proposition were skimmed.
- `AI_BUNDLE_RECEIPT.json`, `FINAL_SOURCE_RECEIPT.json`, `INTEGRATION_RECEIPT.json`, `VISUAL_QA.json` in the
  evidence folders: opened or listed only (build and hash records).
- `morphism_ledger.txt` lines 4-7, 48-50, 52: read in the truncated listing only (they restate the maps).
- The public repository clone and the CG-S6 course: not consulted for this topic.
- `cusp_spectral_geometry.tex` (source of `sys(Q_T) >= T - C`, `l_T`) and `candidate_geometry.tex`
  (`prop:candidate-finite-fillings`, `prop:geometric-pi1`): not read; statements imported from them are
  taken as the workbench gives them.
