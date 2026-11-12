# Reader F — physics-flavoured side lanes of the S6 workbench

Reader: Claude Fable 5.2. Date of reading: 12 Nov 2026. Depth: light to medium, as assigned (every statement
of the cusp files, the introductions and scope paragraphs of everything, proofs only where noted).

Folders (read only):
- `W` = `C:\Users\user\Documents\math\research\s6_recent_results_main\canonical_S6_snapshot\supporting_materials\workbench\research\`
- `R` = `C:\Users\user\Documents\math\research\s6_recent_results_main\canonical_S6_snapshot\`
- scratch scripts of this reader: `C:\Users\user\Documents\workbench_review_20261112\work\scratch\F\`

All files carry the snapshot time stamp 29 Sep 2026 00:32; their internal dates are 3–9 Sep 2026.

Short answer to the question of the assignment. Of these lanes, three things are mathematics about X:
(a) the first-coordinate elliptic quotient locus (F-2, sharpened by this reader in F-3: exactly two regular
fibres, and a dense countable set of abelian fibres); (b) the fibre-degree row (12,0,4,0,−3,0) on
H^4(X minus the three special fibres) (F-7); (c) the bookkeeping of the invariant class
η = u∧w + 6γ∧δ on the fibre (type (1,6), Pfaffian 6, η² = ∓12, indefinite Hermitian form), which repeats
[AC26] §9.1 and [E26] Remark 8.4. Everything else is a computation on an auxiliary object chosen by the
workbench (a flat metric in period coordinates, a lattice Hamiltonian, a matrix model supplied by a GPT Pro
packet). The files say so themselves, repeatedly and correctly; no file claims a statement about the quantum
Yang–Mills mass gap.

---

## 1. Reading notes

### 1.1 Cusp spectral and gauge files

**`W\cusp_spectral_geometry.tex`** (50 KB, 1390 lines; section "Flat spectral geometry on the positive radial
cusp", label `cusp-spec-section`). Read in full except lines 947–957, which `\input` five other modules
(`cusp_globalization_replacement`, `cusp_toric_cover_completion`, `cusp_cone_sphere_routes`,
`cusp_sphere_route_strengthening`, `cusp_s12_carrier_homotopy`, `cusp_sphere_fixed_metric`) that are not in
this assignment.
- Setup (1–86): period matrix Π = [Z | I_2], Z = [[6μ, τ],[β, μ]]; cusp identity Z = s·[[0,1],[−1,0]] +
  [[6μ, h],[b−h, μ]], b = β+τ, s = τ−h, e^{2πis} = t_c; radial ray t_c = e^{−2πT}, s = iT. Real quantities
  L_T = T+H_T = Im τ, q_T = L_T − B_T = −Im β, m_T = Im μ, D_T = L_T q_T + 6 m_T²; limits H = Im h(0),
  B = Im b(0), m = Im μ(0). Line 83–86: "The metric in this section is, by definition, the quotient of
  dx_1²+dy_1²+dx_2²+dy_2² ... the complex period construction itself neither requires nor singles out this
  Euclidean metric."
- Prop. `cusp-spec-exact-dual-lattice` (88): P_T (4×4), det P_T = −D_T, covolume D_T = −L_T·D_can, full
  P_T^{−T}, dual lattice, spectrum λ_T(k) = 4π²(n_1²+n_2² + [(m R + q S)² + (−L R + 6m S)²]/D²).
  Ledger S6-CUSP-SPEC-DUAL, VERIFIED.
- Thm `cusp-spec-shortest-modes` (254): shortest dual vectors are ±ℓ_γ, ±ℓ_u with |ℓ_γ|² = (L²+m²)/D²,
  |ℓ_u|² = (q²+36m²)/D²; λ_1 = (4π²/T²)(1 + (−2H + 2 min{B,0})/T + O(T^{−2})). Ledger S6-CUSP-SPEC-GAPS.
- Cor. `cusp-spec-unit-volume` (410): Vol = D_T = T² + (2H−B)T + H(H−B) + 6m² + O(T e^{−2πT}); unit-volume
  metric has λ_1 = (4π²/T)(1 + (−H − B/2 + 2 min{B,0})/T + …).
- Prop. `cusp-spec-counting` (476): N_T(E) = π D_T Σ_{n∈Z²}(E/4π² − |n|²)_+ + O_E(T+1); first band
  N_T(E) = E D_T/(4π) + O_E(T); unit-volume count E D_T^{1/2}/(4π) + O(D_T^{1/4}); count at the collapsing
  scale = #{(r,s): r²+s² ≤ E}. Ledger S6-CUSP-FIXED-ENERGY-COUNT.
- Thm `cusp-spec-pointed-limits` (645): (F_T, o) → T² × R² (pointed, balls eventually isometric); sys = 1,
  inj = 1/2; covers by Λ_{T,M} = ⟨v_γ, v_u, M e_1, M e_3⟩ of degree M² → R⁴ iff M → ∞ (unit-volume pullback:
  iff M/√T → ∞). Ledger S6-CUSP-SPEC-COVERS, S6-CUSP-FINITE-COVER-R4-AUXILIARY.
- Prop. `cusp-spec-native-quotient` (866): 0 → T²_re → F_T → Q_T = R²/Y_T Z² → 0, det Y_T = D_T,
  sys(Q_T) ≥ T − C.
- Subsection "The exceptional first-coordinate elliptic quotient" (959–1176): Prop.
  `cusp-spec-first-coordinate-descent` (988), Thm `cusp-spec-elliptic-descent-finiteness` (1073), Remark
  `cusp-spec-elliptic-descent-scope` (1165). Ledger S6-CUSP-FIRST-ELLIPTIC-QUOTIENT. See F-2, F-3.
- Thm `cusp-spec-cover-momentum-theorem` (1178): M_0 = I + R, R² = 0, ker R = im R = ⟨ŵ, δ̂⟩;
  S_M^{−1} M_0^M S_M = M_0; cover spectrum and momentum-mesh bound C(1/T + 1/M).
- "Scope and residual data" (1350–1390): metric is declared; B is a free additive constant of the construction
  (see Doubts 3.2); covers are local at the cusp.

**`W\cusp_spectral_interpretation.tex`** (13 KB, 332 lines). Read in full. Thm
`cusp-interpretation-direct-integral-gapless` (63): the multiplication operator ⊕_k λ_k(T) on
L²([T_0,∞); L²_0(T⁴)) is self-adjoint, injective, 0 ∈ σ_ess (Weyl sequence 1_{[n,n+1]} e_{k_0}); ledger
S6-CUSP-AUX-THRESHOLD. Prop. `cusp-interpretation-fixed-complex-counterexample` (145): on (C/Z[i])² the flat
Kähler metrics R²|dz_1|² + R^{−2}|dz_2|² have volume one and λ_1 = 4π²/R² → 0, so complex data do not select
a gap. Prop. `cusp-interpretation-typed-physical-transfer` (211): an abstract Rayleigh-quotient transfer lemma.
Audit record (315): auxiliary gaplessness VERIFIED, conclusion about the 4d quantum Yang–Mills Hamiltonian
OPEN (= ledger S6-OPEN-YM-PHYSICAL-BRIDGE).

**`W\cusp_spectral_preprint_radial_bridge.tex`** (5 KB). Notation bridge for the standalone preprint (there
R = logarithmic height, T = Im τ). One proposition restating the dual lattice. Nothing new.

**`W\cusp_gauge_operators.tex`** (35 KB, 954 lines). Statements read, proofs not. Hessian of YM at the product
connection on F_T is g^{−2} d*d; Coulomb-reduced first eigenvalue γ_T = (4π²/g²) min{|ℓ_γ|², |ℓ_u|²}
(Thm `cusp-gauge-continuum-gap`, 706), multiplicity 6 d_G #I_T; finite cubical cochain model with gap
ρ_N/(g² T²)(1+…), ρ_N = 4N² sin²(π/N), uniformly in the mesh N ≥ 2 (Thm `cusp-gauge-finite-gap-limits`, 407).
Subsection "The physical boundary and the exact no-gap bridge" (756–954) lists five reasons why this is not a
quantum statement. Ledger S6-CUSP-GAUGE-CLASSICAL.

**`W\cusp_su2_magnetic.tex`** (36 KB, 1066 lines; twin `cusp_su2_magnetic_preprint.tex`). Statements read.
Integral coframe θ^j = du_j, θ¹∧θ² = D_T^{−1} dy_1∧dy_2 (Prop. 31); unit-flux line bundle L_T with
c_1 = [γ∧u]; E_T = L_T ⊕ L_T^{−1} smoothly SU(2)-trivial (Prop. `cusp-magnetic-su2-triviality`, 143);
Thm `cusp-magnetic-ym-critical-point` (273); Thm `cusp-magnetic-oscillator-theorem` (425): for every
nondegenerate integral alternating form E the magnetic Laplacian has spectrum {(2n_1+1)b_1+(2n_2+1)b_2};
Cor. `cusp-magnetic-frequency-product` (541): b_1 b_2 = 4π² |Pf E|/D_T, gap ≤ 4π √(|Pf E|/D_T);
Thm `cusp-magnetic-negative-mode` (787). Ledger S6-CUSP-MAGNETIC-SPECTRUM, S6-CUSP-FULL-TORUS-MAGNETIC-GAP,
S6-CUSP-SU2-UNSTABLE. See F-5.

**`W\cusp_native_full_flux_magnetic.tex`** (39 KB, 1047 lines; twin `_preprint`). Lines 1–300, 425–660,
846–1047 read. The invariant class η = u∧w + 6γ∧δ (checked against T_1, T_2 at lines 74–92), E_η with
SNF diag(1,1,6,6), Pf = 6; explicit cocycle and connection; ½η² = +6 in the marking orientation and −6 in the
complex orientation; frequencies B_± = π(Ξ_T ± S_T)/D_T, S_T = 6L_T − q_T, Ξ_T = √((6L_T+q_T)² + 144 m_T²),
B_+B_− = 24π²/D_T; Thm `cusp-native-full-flux-landau-theorem` (433); Cor.
`cusp-native-full-flux-heat-count` (522); split SU(2) connection (576–646); Thm
`cusp-native-full-flux-Morse-theorem` (926). See F-4.

**`W\cusp_native_full_flux_radial.tex`** (21 KB; twin `_preprint`). Thm `native-di-main-theorem` (394): the
direct integral over T of the full-flux magnetic Laplacians has purely continuous spectrum [0,∞), no
eigenvalues. Remark (615): "No radial derivative and no interacting Yang–Mills claim".

**`W\cusp_native_full_flux_suN.tex`** (28 KB; twin `_preprint`). Split-Cartan SU(r) version: action
(π² s_2(m)/g²)(37 + 35B/T + …), negative bands q_ij((2n+1)B_min − B_max), multiplicities 12 q_ij², nullities,
stability boundary S_T = 0; closing remark (lines 660–686): a bundle with c_2 ≠ 0 on a fibre cannot extend
over a space with H⁴ = 0.

**`W\cusp_compact_link_gaussian.tex`** (32 KB; twin `_preprint`; standalone
`R\s6_compact_link_gaussian_preprint.tex`, 98 KB, is the same material with the cover-spectrum, magnetic
saddle and coercive-bridge sections of the other modules added). Cubulation of the degree-M² cover torus,
holonomy map to SU(2)^E, an explicit periodic link configuration with plaquette exp(2π H/N²), finite Hessian
spectrum λ(k) = g^{−2}|P_T^{−T} S_M^{−1} d_N(k)|², Gaussian oscillator with gap √λ_min, diagonal sequence
T_j = j², M_j = j, N_j = j³ on which the gap → 0 (Thm `cusp-link-gaussian-theorem`, 624); Prop.
`cusp-link-exponential-local-only` (754). Ledger S6-CUSP-COMPACT-LINK-FLUX, S6-CUSP-FINITE-GAUSSIAN.

**Preprint twins.** `cusp_compact_link_gaussian_preprint.tex`, `cusp_native_full_flux_magnetic_preprint.tex`,
`cusp_native_full_flux_radial_preprint.tex`, `cusp_native_full_flux_suN_preprint.tex`,
`cusp_su2_magnetic_preprint.tex`: confirmed by size and by `diff` (header says "Standalone-preprint adaptation
of …; the canonical radial-height symbol T was renamed R consistently", with the SHA-256 of the source).
Skipped.

**`R\s6_spectral_degeneration_preprint.tex`** (118 KB, 2645 lines; title "Cusp Spectral Degeneration and Local
Toric Kummer Extension. Conditional results from the reconstructed candidate S⁶ complex-torus fibration",
"Revised conditional specialist-verification draft, 4 September 2026"). Abstract, statement list, §5 opening
(1016–1075), 2255–2300 read. It is the standalone view of the cusp modules above plus two modules outside this
assignment: Thm `thm:global-real-quotient` (1030; the unique primitive monodromy-invariant character ε_γ,
real circle quotient of the regular family with circumference −T D/√(T²+m²); ledger S6-CUSP-FOUR-COPY-R4; this
is the object of [E26] Remark 8.3) and the local toric Kummer morphism (§6; ledger S6-CUSP-KUMMER-COMPLETION).
In this preprint T = Im τ, so H does not appear. Prop. `prop:total-space` (2279) records that the compact
total space with any smooth metric has a positive gap and that the Euclidean fibre metrics are not shown to be
restrictions of a metric on X. Remark at 2263 "Correction of an ambient-family argument" withdraws an earlier
argument that used the path (τ,μ,β) = (i/T, 0, −iT), which is not on the period image.

### 1.2 Quaternionic block

**`W\quaternionic_4441_reconciliation.tex`** (251 KB, 5840 lines; section "The common marked slice and its
dynamics", label `sec:q444-reconciliation`; wrapper `R\s6_quaternionic_4441_reconciliation.tex`, 7.6 KB, is
title + abstract + `\input`). Lines 1–400, 521–665, 1105–1200, 1364–1545, 1626–1700, 1801–1830, 1926–1975,
2113–2400, 2489–2510, 3972–4070, 4448–4472, 5742–5840 read; elsewhere statements only (58 statements).
Source of the model (lines 4–13, 5744–5752): two GPT "Pro-mode packets" dated 4 Sep 2026, "Triality 4-4-4-1
Dynamic Completion" and "Quaternionic 4441 Continuation". The workbench audits and extends them. Contents:
- 35–341: conventions; Moore determinant; Lemma `q444:pair-cubic` N(Θ(A,b)) = det A − b*Ab; marking
  P = [[1,−1,0],[0,1,−1]], u = (1,1,1)^t, C = PP* (the A_2 Cartan matrix), X = (R u); Thm
  `q444:identification` (144); Prop. `q444:cubics`; Prop. `q444:positive`; Prop. `q444:pair-topology`
  ((S¹², S⁸)); Thm `q444:jordan` (308).
- 343–520: group action convention; positive observation O(H) = π_C(PHP*) (ledger S6-Q444-POSITIVE-OBSERVATION).
- 521–1625: the period bridge: Prop. `q444:period-gram` (541), Thm `q444:metric-fibre` (627), rank-loss
  propositions (823, 901), Thm `q444:hermitian-cometric` (1162), Thm (1252) lattice cometric = character
  spectrum, Thm `q444:metric-submersion` (1364), Prop. `q444:native-period-spectrum` (1491).
- 1626–2110: scalar mechanics L = ½ tr Φ̇² + ḃ*ḃ − V, V = m² s/2 + Γ s²/4 − κ(det Φ − b*Φb): Thm `q444:force`
  (1644), Prop. `q444:constrained`, Lemma `q444:global`, Thm `q444:invariant-W` (1801), Prop.
  `q444:fourth-jet` (1879), Thm `q444:moving-family` (1932), Prop. `q444:charge`.
- 2113–2324: Lemma `q444:sharp` (54 n² ≤ s³), Thm `q444:vacua` (2175), Thm `q444:vacuum-hessian` (2234).
- 2325–3970: gauge lift with SU(3): sign of the gauge kinetic term corrected; all homogeneous field equations;
  Thm `q444:temporal-no-lift` (2489); Gauss inertia; no real-connection lift (2795); a real radial family of
  full solutions (2988); vacuum kinetics; exact periodic continuation (3485); null waves (3585); all eight
  gauge-inertia eigenvalues (3754); invariant current.
- 3972–5740: the "rotating ansatz" finite system in su(3)³ (five equations, displayed at 3993–4004): block
  exclusion (4148), Gauss inverse and residual zero set (4539), signature constraint (4744), stress matrix,
  finite coupling fibre (5396; a degree-28 polynomial p_Z), generic exclusion via a 24×24 Sylvester determinant
  (5606).
- 5742–5840: sources and checkers (evidence folders `quaternionic_4441_audit_20260904`,
  `finite_coupling_20260905`, `scalar_gauss_domain_20260905`).
- Scope sentence at 2358–2364: "No result here identifies these cone-boundary spheres with the claimed
  integrable complex structure on S⁶, assigns new spinor periods and toroidal fillings, or proves a continuum
  interacting Yang–Mills spectral gap."

**`W\two_cross_exceptional_shared.tex`** (33 KB). Thm `q444:twocross:thm:exclusion` (64): the five-equation
system has no solution with Z_1, Z_2 ∈ p (the 4-real-dimensional "cross" part of su(3) relative to the matter
line), for any t = g² > 0 and ω ≠ 0. Prop. (475): the class lies in the exceptional set of the generic
exclusion theorem. Prop. (590): a polynomial residual certificate with a strict lower bound. Ledger
Q444-TWO-CROSS-EXCLUSION, -RESIDUAL-CERTIFICATE.

**`W\scalar_gauss_domain_shared.tex`** (36 KB). Thm `sgd:parametrization` (208): the solutions of the two
scalar equations and Gauss (no spatial equation) in the classified frame are in bijection with
D × {±1}² × U(1)², D = {(u,v_0,y): u>0, d = u v_0 − δ² − y² > 0, c = 4v_0 − 5u > 0}, δ = √(2/3), t = 72 d/c.
Thm `sgd:literal-addon:quotient` (647): the literal set S_sg = (D × {±1}² × U(1)² × U(1))/⟨ι⟩. Cor.
`sgd:every-coupling` (862): nonempty for every t. Ledger Q444-TWO-CROSS-SCALAR-GAUSS-*.

**`W\scalar_gauss_smooth_shared.tex`** (25 KB). Thm `sgd:smooth-addon:literal-diffeomorphism` (250), Thm
`sgd:smooth-addon:coupling` (415), Cor. `sgd:smooth-addon:levels` (535): S_sg is an embedded 6-manifold
≅ {±1}² × (0,∞) × R² × T³ with t the (0,∞) coordinate. Ledger Q444-SCALAR-GAUSS-SMOOTH-LITERAL-PRODUCT.

### 1.3 Other workbench modules

**`W\worldline_presymplectic_reduction.tex`** (35 KB, 991 lines; wrapper
`R\s6_worldline_presymplectic_reduction_preprint.tex`). Lines 1–190, 321–350, 720–760 read. Model:
x ∈ Herm_2(C) (Minkowski space with ⟨A,A⟩_L = det A), Z ∈ Mat_{3×2}(C), p = α Z*Z, action
∫⟨p, ẋ⟩ − (e/2)(det p − m_0²c²), left SU(3) "colour". Thm `wpr:thm:quotient` (143), Thm `wpr:thm:massive`
(321), Lemma `wpr:lem:irregular` (488), Thm `wpr:thm:massless` (519), Thm `wpr:thm:zero` (645), Thm
`wpr:thm:verdict` (720), Thm `wpr:thm:packet-action` (893). Ledger S6-WPR-*. Cites Dirac 1950,
Gotay–Nester–Hinds 1978, Marsden–Weinstein 1974 for the framework.

**`W\hermitian_normal_slice_physics.tex`** (54 KB, 1299 lines). Lines 1–60, 132–160, 528–612, 1124–1146,
1220–1299 read, other statements by head. Thm `hnsp-lorentz-theorem` (132): ½ D²(det)_{uu*} on the normal
slice {X ∈ Herm_3(C): Xu = 0} ≅ Herm_2(C) is the Minkowski form; spin action (234); a gauge–scalar model on
the slice (421); Prop. `hnsp-candidate-spacelike` (538): G_{η,T} = [[2L_T, 2m_T],[2m_T, −q_T/3]] has
det = −(2/3) D_T < 0; free-field and regulator spectra (759, 861); obstruction propositions (1126, 1147);
Thm `hnsp-coercive-transfer` (1220); "Exact conclusion" (1270).

**`W\homogeneous_quantum_confinement.tex`** (80 KB, 1841 lines; wrapper
`R\s6_homogeneous_quantum_confinement.tex`). Lines 1–84, 847–870, 946–965, 1072–1125, 1232–1257 read. The
38-coordinate SU(3) matrix quantum mechanics (three gauge matrices, adjoint scalar, triplet): Thm
`qh:full-compact` (847), Thm `qh:hq-positive` (946), Cor. `qh:hq-ground` (1072), Prop. `qh:hq-embedding`
(1099); second section (1232–1841): Born–Oppenheimer comparison for a two-Fourier-coordinate truncation. Line
17–22 attributes the discreteness mechanism to the literature. Ledger S6-Q444-HOMOGENEOUS-QUANTUM-*,
S6-Q444-MOVING-FOURIER-QUANTUM-COMPARISON.

**`W\ym_bulk_plaquette_extension.tex`** (39 KB, 1093 lines; "Mechanically generated from the complete audited
BULK_PLAQUETTE_EXTENSION.md", 8 Sep 2026). Lines 1–75, 990–1093 read. SU(2) Kogut–Susskind Hamiltonian
H = −κ Σ Δ_e + b Σ(2 − W_p) on the open box {−L..L}³; second-order strong-coupling (ξ = b/κ) improvement of a
Rayleigh quotient: R_ret − R_corr = (1951/81675) b²/κ + O_L(b³/κ²). No S6 input at all.

**`W\z6_defect_center_bridge.tex`** (22 KB, 657 lines). Read in full except the proofs of the two group
theorems. Thm `zdc:thm:fibre-degree` (178), Prop. `zdc:prop:finite-reductions` (356), Thm
`zdc:thm:tensor-centres` (461), Thm `zdc:thm:common-centre` (535), boundary (642). See F-7.

### 1.4 Root-level drafts (title, opening, statement heads only)

All are the Yang–Mills programme; they later moved to the public repository (the clone has
`repo\yang-mills\…` and files such as `spatial_continuum_127p.tex`). The common object is the SU(2)
Kogut–Susskind Hamiltonian H = κ Σ_e E_e + b Σ_p (2 − W_p), κ = 2g²/a, b = 1/(2g²a), ξ = b/κ = 1/(4g⁴), on
the open cubic box {−L,…,L}³ with all links and plaquettes. The only datum taken from X is one number, the
plaquette angle θ = 2π a²/D with D = L_T q_T + 6 m_T² (stated in
`s6_volume_uniform_local_vacuum_draft.tex` §1), that is, the unit-flux cusp bundle of
`cusp_su2_magnetic.tex` put on a lattice.

- `s6_adjacent_plaquette_quantum_draft.tex` (21 KB, 8 Sep): two plaquettes sharing a link, seven links; a
  nonzero second-order elimination correction; it `\input`s `ym_bulk_plaquette_extension.tex`. "not a
  four-dimensional continuum mass-gap result".
- `s6_wilson_temporal_transfer_draft.tex` (29 KB, 8 Sep): exact single-link character multiplier of the SU(2)
  Wilson transfer operator; strong limit to the Hamiltonian on a finite spatial lattice (Thm
  `thm:multiplier`, `thm:stronglimit`). A known type of statement, made explicit.
- `s6_interacting_wilson_variation_draft.tex` (39 KB, 8 Sep): Fierz identities, ground-state transform, centre
  symmetry selection rules, all-coupling finite-volume bounds for vacuum-weighted Wilson loops (8 statements).
- `s6_spatial_vacuum_elimination_draft.tex` (35 KB, 8 Sep): conditional projection in the true lattice vacuum,
  Schur-complement form, temporal memory kernel, improved trial vectors (5 statements). Attributes the
  Feshbach–Schur method to the literature.
- `s6_retained_cusp_nonlinear_draft.tex` (33 KB, 8 Sep): the full 6×6 two-form metric of the cover torus
  (G^{−1} from P_M) and the nonlinear Wilson action in it. "does not claim a quantum mass-gap counterexample".
- `s6_extensive_quantum_blocking_draft.tex` (91 KB, 8 Sep): blocking of the full box in the true vacuum,
  Schur memory, associativity of repeated blocking, a "gap transfer" theorem (14 statements). Opens with a
  correction notice listing superseded "Fabel" notes.
- `s6_magnetic_translation_quantum_draft.tex` (318 KB, 8 Sep, 11 parts): the cusp magnetic background as a
  translation operator on the Wilson Hilbert space; first excitation band of the open box; centre-disorder
  endpoint; spectral leakage polynomials.
- `s6_weak_coupling_physical_draft.tex` (344 KB, 8 Sep, 18 parts): fixed-box weak-coupling limit of physical
  eigenvalues (maximal-tree gauge), a "radial carrier" representation, first two coupling coefficients; Part 18
  "Non-Abelian fluid encoding". Reader scope says the Gamma representation "does not reconstruct local
  interacting Yang–Mills theory".
- `s6_spatial_continuum_draft.tex` (415 KB, 8 Sep, 28 sections, 88 statements): simultaneous cusp/refinement
  sequences; §9 a volume-uniform gap at strong coupling, (H − E)|_{ψ^⊥} ≥ (3κ/4)(1 − 512 ξ/3) for
  0 < ξ ≤ 1/49152, by the method of Yarotsky (arXiv:math-ph/0411042) with explicit constants; §27 a
  "regulator-level obstruction" to a perturbative route; §28 conclusion: "proves neither a continuum mass gap
  nor its absence".
- `s6_volume_uniform_local_vacuum_draft.tex` (312 KB, 9 Sep, 26+ sections): volume-independent local estimates
  in the full vacuum (local electric moments, cluster coordinates, decay of electric covariance).
- `s6_xi4_heat_transport_draft.tex` (18 KB wrapper, 8 Sep; `\input`s 12 files from
  `supporting_materials\workbench\evidence\ym_sidebar_topics_20260908\xi4_heat_transport\tex\`). Title "The
  heat generator on the retained inverse-fibre cover". The abstract combines the de Bruijn–Newman heat flow,
  a Connes quotient, a polynomial map of Tao, a Navier–Stokes source and a fourth-order lattice coefficient;
  it includes `s6_three_point_quotient.tex` (a real three-torus quotient built from the three special points;
  it records μ(z_1) = (2−ρ)/3, μ(z_2) = (1−i)/2, ρ = e^{πi/3}) and `s6_three_point_forcing.tex` (a "forced
  fluid" built from it). See Doubts 3.6.

---

## 2. Candidates

### F-1
- **Title**: Flat spectral geometry of the regular fibres along the cusp (exact spectrum, first eigenvalue,
  volume, fixed-energy counting law, pointed limits, gapless direct integral). **Type**: computation.
- **Where**: `W\cusp_spectral_geometry.tex` 1–945, 1178–1390; `W\cusp_spectral_interpretation.tex`; standalone
  `R\s6_spectral_degeneration_preprint.tex` §§2–4, 7. Early Sep 2026 (preprint dated 4 Sep).
- **Statement**: With the Euclidean metric of the coordinates in which the period matrix is [Z | I_2]:
  Spec(Δ_{F_T}) = {4π²|P_T^{−T}k|²}; Vol(F_T) = D_T = |det P_T| = L_T q_T + 6m_T² =
  T² + (2H−B)T + H(H−B) + 6m² + O(T e^{−2πT}); sys = 1; λ_1 = 4π² min{(L²+m²)/D², (q²+36m²)/D²} =
  (4π²/T²)(1 + (−2H + 2min{B,0})/T + O(T^{−2})); N_T(E) = π D_T Σ_{n∈Z²}(E/4π² − |n|²)_+ + O_E(T+1); pointed
  limit T² × R² with balls eventually isometric; the direct integral over T ∈ [T_0,∞) of the mean-zero fibre
  Laplacians is self-adjoint, injective, with 0 in its essential spectrum.
- **Support**: complete written proofs (about 15 pages), all elementary (2×2 block inversion, lattice-point
  count in ellipses with the area–perimeter bound, displacement bounds). Ledger: S6-CUSP-SPEC-DUAL, -GAPS,
  -COVERS, S6-CUSP-FIXED-ENERGY-COUNT, S6-CUSP-AUX-THRESHOLD, all VERIFIED.
- **What it adds**: not in [AC26] or [E26] (neither puts a metric on the fibres). Over the literature: these
  are standard facts for a family of flat tori Z = sB_0 + (bounded); not searched.
- **First assessment**: correct as far as read. I rechecked the two first-order expansions of λ(ℓ_γ), λ(ℓ_u)
  and the leading term of the counting law by hand. On what the statements depend:
  (i) The metric is the flat Kähler metric that makes the Z-basis ŵ, δ̂ of the vanishing lattice
  K = ker(M_0 − I) = im(M_0 − I) unitary. It is invariant under the cusp monodromy M_0, so it is a well-defined
  family over the punctured cusp disc, canonical up to the choice of a positive quadratic form on the rank-two
  lattice K. It is not invariant under the full monodromy (the preprint says so at 1068–1070) and it is not
  the restriction of any metric on X: in a metric of X the fibres have bounded diameter and converge to W, and
  the cycles ŵ, δ̂ are the ones that shrink on the toric boundary, whereas here they keep length 1 and the
  other two periods grow like T.
  (ii) Intrinsic to the degeneration: D_T = |det Im Z| is the covolume of Λ measured in units of K ⊕ iK, and
  the rate D_T ~ T² = (log|t_c|/2π)² says that the unipotent monodromy has N² = 0 with rank N = 2. This is
  the usual nilpotent-orbit growth, not a new invariant.
  (iii) The constants: B = Im(β+τ)(0) is a free additive constant of the construction (file, 1365–1369); it
  is, up to normalization, −(1/2π) log|u| of Engel's family X(u, a_0, a_1). H depends on the base coordinate;
  with t_c = 1/t and j = 1728 t one gets e^{2πi h(0)} = 1/1728, H = log(1728)/(2π) ≈ 1.186 (my computation
  from j = 1/q + 744 + …). m = Im μ(0) is the logarithm of the G_m-coordinate of the Mordell–Weil generator P
  on the nodal fibre; from the Weierstrass model of F-3 that coordinate is −(5 − 2√6)^{±1}, so
  Re μ(0) ≡ 1/2 and |m| = log(5+2√6)/(2π) ≈ 0.3649 (my computation; consistent with Re μ = 1/2 at both
  elliptic points). The workbench keeps H, B, m symbolic.
  (iv) No statement here is an invariant of the complex structure of X alone; the file proves this itself
  (Prop. `cusp-interpretation-fixed-complex-counterexample`).
- **A full check must establish**: the sign conventions of P_T against [AC26] §3; the O(T) remainder in the
  counting law (uniformity in the finitely many n); the claim "balls eventually isometric"; whether the values
  of H and m in (iii) agree with the workbench conventions for h and μ.
- **Deserves a full check**: no — routine and already correct on reading; worth one paragraph in a write-up
  only if the metric is introduced as "the M_0-invariant flat Kähler metric normalized on the vanishing
  lattice". **Interest**: 2.

### F-2
- **Title**: The first-coordinate elliptic quotient of a fibre exists exactly on a finite set of the base,
  away from the cusp. **Type**: new result (small) / refinement of [AC26] Cor. 9.8.
- **Where**: `W\cusp_spectral_geometry.tex` 959–1176 (Prop. `cusp-spec-first-coordinate-descent`, Thm
  `cusp-spec-elliptic-descent-finiteness`, Remark `cusp-spec-elliptic-descent-scope`); preprint
  `R\s6_spectral_degeneration_preprint.tex` 2146–2275 (`prop:descent`, `thm:descent-finite`,
  `cor:no-landau-cusp`). Early Sep 2026.
- **Statement**: For A_z = C²/⟨(6μ,β),(τ,μ),(1,0),(0,1)⟩, pr_1 descends to a surjective holomorphic
  homomorphism A_z → E_τ = C/(Zτ+Z) iff 6μ(z) = aτ(z) + b for a (unique) (a,b) ∈ Z². Then the kernel is
  connected, equal to C/(Z + Zτ_f) with τ_f = aμ − β, Im τ_f = −D_can > 0. The labels transform by
  g_0(a,b) = (a, a+b), g_2(a,b) = (−b, 6+a); the union D of the loci is invariant under the triangle group,
  its image in the completed base is finite, and it misses a punctured neighbourhood of the cusp.
- **Support**: written proof, about 2 pages: imaginary parts force a = 6 Im μ/Im τ → 0 at the cusp; identity
  theorem; no identity 6μ = aτ + b can hold on the whole half-plane (apply g_0, then g_2); compactness of a
  truncated fundamental polygon. Ledger S6-CUSP-FIRST-ELLIPTIC-QUOTIENT, VERIFIED.
- **What it adds**: [AC26] Cor. 9.8 only says that NS(F_b) = Zη and a(F_b) = 0 outside a countable set and
  gives the criterion "E ∈ NS(F_z) iff a linear form in 1, τ, μ, β, 6μ² − τβ vanishes" (transcription line
  312; §9.1). The workbench isolates one explicit jump locus and proves it finite. [E26] does not discuss it,
  but its Lemma 2.1 computes (6P)·O = 2, which is the count of this locus (see F-3). Literature: not searched.
- **First assessment**: the proof is sound as read. I checked the two label laws and that both elliptic points
  lie in D: at z_2 (τ = i, μ = (1−i)/2) 6μ = −3τ + 3; at z_1 (τ = ρ = e^{πi/3}, μ = (2−ρ)/3) 6μ = −2τ + 4.
  These are the fixed labels of g_2 and of g_1 = g_0^{−1}g_2^{−1}. The theorem is weaker than what is true
  (F-3), and the remark at 1165 is right to say that other elliptic quotients are not excluded: they exist in
  abundance (F-3 (c)).
- **A full check must establish**: nothing beyond F-3, which contains it.
- **Deserves a full check**: yes, together with F-3 (cheap). **Interest**: 3.

### F-3
- **Title**: (Reader's sharpening of F-2; not in the workbench.) Exactly two regular fibres of X admit the
  first-coordinate elliptic quotient, over t = 64(47 ± 27√3)/11; and the fibres over the dense countable set
  where the Mordell–Weil generator is torsion are abelian surfaces isogenous to a product of elliptic curves.
  **Type**: new result (to be checked) / refinement of [AC26] Cor. 9.8 and of [E26] Remark 8.4.
- **Where**: this reader's computation; script
  `C:\Users\user\Documents\workbench_review_20261112\work\scratch\F\six_P_meets_O.py` (sympy, exact; runs in
  seconds). Inputs: F-2; [E26] §2 (the rational elliptic surface with fibres IV*, III, I_1, the section P,
  (6P)·O = 2, and "P intersects a 3-torsion point of E_ρ and a 2-torsion point of E_i").
- **Statement**: (a) In Engel's description the fibre over t is the quotient of the C*-bundle of O(P − O) over
  E_t by a lift of translation by 6P, so μ is the coordinate of P and the condition 6μ ∈ Zτ + Z of F-2 says
  6P(t) = O(t). (b) The surface is Y² = X³ − (3/4) t³(t−1) X + (1/4) t⁴(t−1)² (j = 1728 t; IV* at t = 0, III at
  t = 1, I_1 at t = ∞), with P = (0, t²(t−1)/2) of height 1/6. Then
  x(6P) = (89t² + 4736t − 4096)(881t⁴ + 4745344t³ − 12079104t² + 24641536t − 16777216) / (1296 (11t² − 6016t + 8192)²),
  and 6P is not O at t = ∞. Hence 6P = O exactly at the two simple roots t_± = 64(47 ± 27√3)/11 ≈ 1.3651 and
  545.54 (j = 1728 t_±), in agreement with (6P)·O = 2. So the image of D in the base is {0, 1, t_+, t_−}, and
  exactly two regular fibres F_{t_±} carry a holomorphic surjection onto E_t with elliptic kernel. (c) On such
  a fibre the kernel curve has lattice ⟨γ̂ − aû − bŵ, δ̂⟩ and η = u∧w + 6γ∧δ takes the value 6 on it; with
  η² = −12 and f² = 0 for the fibre class f, the class xη + yf has positive square for suitable x, y, so the
  fibre has an ample class: F_{t_±} are abelian surfaces, isogenous to E_τ × E_{τ_f}. The same argument works
  whenever 6P(t) is a torsion point of order k (then pr_1 maps onto C/(Zτ + Z + Z·6μ)), and the set of such t
  is countable and dense in the base; the number of t with 6kP = O is (6kP)·O = 3k² − 1 counted with
  multiplicity. So X has a dense countable set of abelian fibres, although the very general fibre has
  algebraic dimension 0.
- **Support**: (b) is an exact computation with the group law over Q(t); the script also verifies the fibre
  types and j = 1728 t. The local analysis at the special points: with φ = 6μ − aτ − b one has
  φ∘g_2 = φ/τ at z_2 and φ∘g_1 = −φ/τ at z_1, so ord φ ≡ 1 mod 4 and ≡ 2 mod 3 in the uniformizing
  coordinates, as it must be for a section through the identity component of III and IV*; the vanishing there
  does not count as an intersection with O on the surface. (a) and (c) are short arguments written above, not
  checked by anyone else.
- **What it adds**: over [AC26]: explicit members of the countable exceptional set of Cor. 9.8, with their
  algebraic dimension (2, not 0), and the exact count for the simplest jump locus. Over [E26]: Remark 8.4 says
  only that a very general fibre is not an abelian variety; the two special values of t and the density
  statement are not there (though the density of torsion values of a section is standard and would be evident
  to the author). Over the workbench: Thm `cusp-spec-elliptic-descent-finiteness` gave "finite". Literature:
  not searched beyond [AC26] and [E26].
- **First assessment**: the computation is exact and agrees with Engel's intersection number, with the
  workbench's values of μ at the elliptic points, and with the local orders. The identification of the
  manuscript's μ with the coordinate of the Mordell–Weil generator (up to sign and lattice translation) rests
  on the transformation laws μ∘g_0 = μ, μ∘g_2 = 1 + μ/τ and on the torsion values at z_1, z_2; a checker should
  confirm it against [AC26] §2–3. Part (c) uses that a class of positive square in NS of a 2-torus has a
  definite Hermitian form.
- **A full check must establish**: (1) the dictionary between the period functions (τ, μ, β) of [AC26] and
  (E_t, P, linearization) of [E26]; (2) the Weierstrass model and that P generates the Mordell–Weil group;
  (3) x(6P) (re-run the script, or use division polynomials); (4) the behaviour at t = 0, 1, ∞ on the Néron
  model; (5) the value η(kernel lattice) = ±6 and the ampleness argument; (6) the count 3k² − 1 and the
  density claim; (7) whether F_{t_±} sit in X in any special way (for instance curves in X: an abelian fibre
  contains curves, so X contains compact curves inside regular fibres; compare with what [AC26] says about
  curves and divisors on X).
- **Deserves a full check**: yes — cheap, concrete, and it is a statement about the complex geometry of X that
  neither paper has. **Interest**: 3.

### F-4
- **Title**: The magnetic Laplacian and the split SU(2)/SU(r) Yang–Mills connection of the invariant class
  η = u∧w + 6γ∧δ on a cusp fibre. **Type**: computation.
- **Where**: `W\cusp_native_full_flux_magnetic.tex` (Thms `cusp-native-full-flux-landau-theorem` 433,
  `cusp-native-full-flux-Morse-theorem` 926; Cor. 522); `W\cusp_native_full_flux_suN.tex`;
  `W\cusp_native_full_flux_radial.tex`. Canonical integration dated 3 Sep 2026.
- **Statement**: For the Hermitian line bundle L_η with c_1 = η and the constant-curvature connection, in the
  Euclidean period metric: Spec(Δ_η) = {(2n_+ +1)B_+ + (2n_− +1)B_−}, each joint level of complex dimension
  6 = Pf(E_η); B_± = π(Ξ_T ± S_T)/D_T, S_T = 6L_T − q_T, Ξ_T² − S_T² = 24 D_T, B_+B_− = 24π²/D_T;
  B_− = 2π/T − 2πH/T² + …, B_+ = 12π/T + …, ratio → 6; Tr e^{−tΔ} = 3/(2 sinh(tB_+) sinh(tB_−));
  N_η(E) = E² D_T/(32π²) + O_E(T). For A = ∇_η ⊕ ∇_η^{−1} on L_η ⊕ L_η^{−1}: c_2 = −η², Chern number −12
  (marking orientation), +12 (complex orientation); YM(A) = 24π²/g² + 2π² S_T²/(g² D_T) = 74π²/g² +
  70π²B/(g²T) + …; negative Jacobi eigenvalues ν_n = (4π/D_T)[nΞ_T − (n+1)|S_T|] for 2n+1 < ρ* = B_max/B_min,
  each of real multiplicity 48; real Morse index 48⌈(ρ*−1)/2⌉ = 144 deep in the cusp. SU(r): the same with
  root charges q_ij, bands of real dimension 12 q_ij².
- **Support**: written proofs (ladder operators, polar complex structure J_η, Weitzenböck/polarization table,
  Coulomb reduction by resolvent intertwining). Multiplicity cross-checked in the file against
  Gordon–Kirwin–Schueth–Webb, Prop. 4.5 (cited with link). Ledger: the SU(2)/SU(r) items are in the result
  map; S6-CUSP-FULL-TORUS-MAGNETIC-GAP VERIFIED.
- **What it adds**: [AC26] §9.1 and [E26] 8.4 have the class, its type (1,6) and the signature (1,1); the
  spectral and Yang–Mills computations are additions, but about a chosen metric. Literature: instability of
  non-self-dual constant-curvature connections on flat four-tori is classical (constant field strength
  solutions of 't Hooft and van Baal); not searched.
- **First assessment**: internally consistent; I rechecked the expansion of B_−, the count n = 0,1,2 for
  ρ* → 6, and 24+24 = 48. Two remarks that change how it should be presented. (1) S_T/D_T is the ω-degree of
  η for the Euclidean Kähler form ω (η∧ω ∝ S_T), and the action excess 2π²S_T²/(g²D_T) is the usual
  (degree)²/volume term. Because the Hermitian form of η has signature (1,1), there are flat Kähler metrics on
  the same fibre with η∧ω = 0; for those the connection is anti-self-dual, the action is the topological value
  24π²/g², and there is no negative mode. So "Morse index 144" is a property of the metric normalized on the
  vanishing lattice, not of the fibre. The file treats S_T = 0 as a "wall" but does not say that it can be
  reached by changing the metric. (2) Intrinsic content: Pf = 6, c_2 = ±12, the (1,1) type, and the fact that
  L_η cannot be the restriction of a line bundle on X (H²(X;Z) = 0) although η is monodromy invariant.
- **A full check must establish**: the polarization table (846–925) and the claim that all negative modes are
  Coulomb; the orientation statements; remark (1).
- **Deserves a full check**: no — a correct model computation whose headline number is metric dependent.
  **Interest**: 2.

### F-5
- **Title**: The unit-flux reducible SU(2) Yang–Mills connection on a cusp fibre is unstable
  (S6-CUSP-SU2-UNSTABLE), and the oscillator spectrum for an arbitrary integral alternating form.
  **Type**: computation.
- **Where**: `W\cusp_su2_magnetic.tex` (Thm `cusp-magnetic-ym-critical-point` 273; Thm
  `cusp-magnetic-oscillator-theorem` 425; Cor. 541; Thm `cusp-magnetic-negative-mode` 787).
- **Statement**: Bundle: E_T = L_T ⊕ L_T^{−1} over the flat torus F_T, where L_T has c_1 = θ¹∧θ² = [γ∧u]
  (the first two members of the integral coframe; θ¹∧θ² = D_T^{−1} dy_1∧dy_2). c_1(E) = 0, c_2(E) = −c_1(L)² = 0,
  and the SU(2)-bundle is smoothly trivial (explicit nullhomotopy of the transition functions). Connection:
  ∇^T = d + 2π u_1 du_2 H_mag, H_mag = diag(i, −i); curvature (2π/D_T) H_mag dy_1∧dy_2, parallel, hence
  d_∇^* F = 0; non-flat. Action with YM = (1/2g²)∫|F|²: 2π²/(g² D_T). Proved: on the full background-gauge
  slice the Jacobi operator −Σ∇_μ∇_μ a_ν − 2Σ[F_νμ, a_μ] has a smooth real eigenform a with d_∇^* a = 0 and
  eigenvalue −4π/D_T (the lowest Landau level of the charge-two root line in the favourable polarization), so
  YM''(a,a) = −4π/(g² D_T) < 0 for every T; the negative eigenvalue → 0 as T → ∞. For any nondegenerate
  integral E: Spec = {(2n_1+1)b_1 + (2n_2+1)b_2}, b_1b_2 = 4π²|Pf E|/D_T, gap ≤ 4π√(|Pf E|/D_T).
- **Support**: written proofs; ledger S6-CUSP-SU2-UNSTABLE, S6-CUSP-MAGNETIC-SPECTRUM VERIFIED.
- **What it adds**: nothing about X. The class γ∧u is invariant under the cusp monodromy only, and
  dy_1∧dy_2 is not of type (1,1), so L_T is not a holomorphic line bundle on the fibre. The instability is
  the Nielsen–Olesen mechanism for a constant abelian field in one plane; it holds on every flat torus with
  such a flux. Not searched.
- **First assessment**: correct in kind; no complete Morse index is claimed here (one negative direction is
  exhibited). The words "classical Yang–Mills critical point" in the ledger are accurate.
- **A full check must establish**: nothing needed for the S6 survey.
- **Deserves a full check**: no. **Interest**: 1.

### F-6
- **Title**: Classical gauge Hessian at the product connection, cubical cochain model, compact-link flux,
  finite Gaussian oscillator, radial direct integrals (grouped). **Type**: computation.
- **Where**: `W\cusp_gauge_operators.tex`; `W\cusp_compact_link_gaussian.tex`;
  `W\cusp_native_full_flux_radial.tex`; `R\s6_compact_link_gaussian_preprint.tex`.
- **Statement**: (i) Coulomb-reduced Hessian g^{−2}d*d on F_T has first eigenvalue (4π²/g²) min{|ℓ_γ|²,|ℓ_u|²},
  multiplicity 6 d_G #I_T; (ii) the cubical cochain version has first eigenvalue
  (ρ_N/g²T²)(1 + (−2H + 2min{B,0})/T + …), ρ_N = 4N² sin²(π/N), uniformly in N ≥ 2; (iii) an explicit periodic
  SU(2) link field with constant plaquette exp(2πH/N²) and its action; (iv) the Gaussian oscillator on the
  finite Coulomb space has gap √λ_min ≤ (2N sin(π/N)/g)·√(L²+m²)/D, and the gap → 0 along T = j², M = j,
  N = j³; (v) the direct integral over T of the full-flux magnetic Laplacians has purely continuous spectrum
  [0,∞).
- **Support**: written proofs; ledger S6-CUSP-GAUGE-CLASSICAL, S6-CUSP-COMPACT-LINK-FLUX,
  S6-CUSP-FINITE-GAUSSIAN VERIFIED.
- **What it adds**: nothing about X; these are F-1 rewritten for one-forms and for a lattice. Each file states
  that these are linear classical or finite Gaussian operators and not a quantum Hamiltonian.
- **First assessment**: routine; (i) is F-1 tensored with the transverse polarizations.
- **A full check must establish**: nothing for the S6 survey.
- **Deserves a full check**: no. **Interest**: 1.

### F-7
- **Title**: The fibre-degree row on H⁴(X minus the three special fibres): (12, 0, 4, 0, −3, 0).
  **Type**: computation / small new result on the topology of X.
- **Where**: `W\z6_defect_center_bridge.tex`, Thm `zdc:thm:fibre-degree` (178–300), Prop.
  `zdc:prop:finite-reductions` (356), §"Coefficient reduction" (409–456). Not in the claim-ledger index under
  a Z6 name.
- **Statement**: Let D = W ⊔ S_1 ⊔ S_2, U = X ∖ D. Alexander duality in X ≅ S⁶ gives
  L = H⁴(U;Z) ≅ H_1(D;Z) = Z⟨a_0,b_0; a_1,b_1; a_2,b_2⟩ (a_0 = [γ̂], b_0 = [û] on W; a_j the class of the
  affine deck generator on S_j, b_j the invariant coordinate; π_{1*}[γ̂] = 3a_1, π_{2*}[γ̂] = −4a_2). For a
  smooth fibre F the restriction H⁴(U;Z) → H⁴(F;Z) = Z is
  deg_F(n_0a_0 + r_0b_0 + n_1a_1 + r_1b_1 + n_2a_2 + r_2b_2) = 12 n_0 + 4 n_1 − 3 n_2 (for the twists
  (ℓ_0,ℓ_1,ℓ_2) = (0,1,−1)); it is primitive, with saturated kernel ⟨b_0,b_1,b_2, a_0 − 3a_1, 3a_1 + 4a_2⟩; it
  factors through H_1(X°;Z) ≅ Z by Φ_1(c) = 12, Φ_1(ḡ_1) = 4ℓ_1, Φ_1(ḡ_2) = 3ℓ_2; the normal-line holonomy
  characters of S_1, S_2 combine to χ_12 = e^{−2πi deg_F/12}; H⁴(U;Z/6) ≅ (Z/6)⁶. In other words, a generic
  fibre has linking numbers 12, 4, −3 with the loops γ̂ ⊂ W, ĝ_1 ⊂ S_1, ĝ_2 ⊂ S_2, and the terminal meridian
  pairs to p = 12ℓ_0 − 4ℓ_1 − 3ℓ_2 = −1.
- **Support**: a written proof: a 9×9 Mayer–Vietoris collar matrix Δ_1 with det 1 and the transposed system
  Δ_1^T y = −ã_0^∨, solved by hand (y = (12,4,−3; 12,0; 4,0; −3,0)). It uses the "verified local homology
  computations" H_1(W) = Z², H_1(S_j) = Z² and the presentation of H_1(X°) from other modules.
- **What it adds**: [AC26] has π_1(X) = Z/|12ℓ_0 − 4ℓ_1 − 3ℓ_2| and H_*(X) = H_*(S⁶); the cohomology of the
  complement of the special fibres and the linking numbers of a fibre with the 1-cycles of the special fibres
  are a refinement in the same spirit. [E26]: the numbers 12, 4, 3 appear in the condition |12(a_0+a_1)| = 1
  and in the Seifert picture of Remark 8.3; the row itself is not stated. Literature: not searched.
- **First assessment**: plausible and consistent with the Main Theorem. I checked one input: the coinvariants
  Λ/(T_1 − 1)Λ are torsion-free of rank 2 (image of T_1 − 1 is spanned by (2,−1,0,0), (2,1,1,0), a primitive
  sublattice), so H_1(S_1;Z) ≅ Z² is consistent provided the class of ĝ_1³ is not divisible by 3 in the
  coinvariants. The second half of the file (SU(2)×SU(3) → SU(6) by tensor product; the quotient
  (U(1)×SU(2)×SU(3))/μ_6 ↪ U(6)) is textbook group theory; the file states that the map
  H⁴(U;Z) → μ_6 is "one particular surjection" and that no gauge bundle follows.
- **A full check must establish**: the collar matrix Δ_1 (orientations, the entries −3 and +4), H_1(S_j;Z)
  including possible torsion, and the dependence on (ℓ_0,ℓ_1,ℓ_2). This overlaps with the reader who covers
  the integral Leray / finite-band modules.
- **Deserves a full check**: maybe — only as part of the check of the homology computation it depends on.
  **Interest**: 2.

### F-8
- **Title**: The quaternionic "4+4+4+1" slice of Herm_3(H): algebra and scalar mechanics (grouped).
  **Type**: computation on a supplied model (audit of two GPT Pro packets); expository only as far as X is
  concerned.
- **Where**: `W\quaternionic_4441_reconciliation.tex` 35–520, 1626–2370; 4–5 Sep 2026.
- **What the object is**: the 13-dimensional real subspace J_P = {H ∈ Herm_3(H): PHP* ∈ Herm_2(C)} =
  L_u = {Θ(A,b) = A + B(b)j : A ∈ Herm_3(C), b ∈ C³, u*b = 0}, with coordinates G ∈ Herm_2(C) (4), z ∈ C²
  (4), w ∈ C² (4), λ ∈ R (1) through H = X [[G, z + wj],[(z+wj)*, λ]] X*. Its relation to X is only the
  marking: P = [[1,−1,0],[0,1,−1]] and u = (1,1,1)^t are the lattice maps of the toric cusp chart
  (t = z_0z_1z_2), and C = PP* is the A_2 form of the dP_6 hexagon. The potential, the kinetic term, the gauge
  group SU(3) and the Lorentzian reading of Herm_2(C) come from the packets, not from X (file, 2358–2364).
- **Statement / judgement, item by item**:
  1. N(Θ(A,b)) = det A − b*Ab (Lemma `q444:pair-cubic`); restricted cubic
     N_13 = λ det G − z* adj(G) z − w* adj(G) w. Correct; it is the classical decomposition
     Herm_3(H) = Herm_3(C) ⊕ C³.
  2. J_P = L_u with w = −ε χ̄ (Thm `q444:identification`). Correct, two lines of linear algebra.
  3. Positive fibres: PSD iff G ≥ 0, z, w ∈ Ran G, λ − z*G^†z − w*G^†w ≥ 0 (Schur complement). Routine.
  4. Boundary pair (S¹², S⁸) of the positive cones. Routine (a cone over a 12-sphere).
  5. The Jordan closure of the slice is all of Herm_3(H); in marked coordinates the product is
     (MDN + NDM)/2 with D = diag(C^{−1}, 3); the packet's coefficient 1/2 becomes 3/2. A correction of the
     packet, of no outside interest.
  6. Thm `q444:force`: the constraint ρ = u*b = 0 is not preserved by the scalar mechanics;
     ρ̈ = −(m² + Γs)ρ − κ u*Φb, example with ρ̈(0) = −2κ. A correction of the packet.
  7. Thm `q444:invariant-W`: invariant sectors of configuration dimension 6 and 8 (b ∈ W, Φ preserving W).
     Elementary.
  8. Prop. `q444:fourth-jet`: tangency to order 3 with ρ'''' = −12κ. A cautionary example.
  9. Thm `q444:moving-family`: periodic solutions b(t) = O(t)b_0, Φ(t) = O(t)Φ_0O(t)* with O(t) a rotation
     about u of frequency √a; at (m², Γ, κ) = (1,1,6): s = 1, energy 7/4. A relative equilibrium of an
     SO(3)-invariant mechanical system; elementary.
  10. Lemma `q444:sharp`: 54 n² ≤ s³ for trace-free Q, equality iff Q = x(3P − I) (this is the discriminant).
      Thm `q444:vacua`: global minima of V = m²s/2 + Γs²/4 − κn: Q = 0 for m² > κ²/(27Γ); coexistence at
      equality; Q = x_*(3P − I), x_* = (κ + sgn(κ)√(κ² − 24Γm²))/(12Γ), P a rank-one quaternionic projector,
      for m² below; each nonzero component ≅ HP². Thm `q444:vacuum-hessian`: eigenvalues x(12Γx − κ), 0, 3κx
      with multiplicities 1, 8, 5; kernel = tangent space of HP². I rechecked the factorization
      f(r) = (Γ/4) r²(r − r_c)² + ((m² − m_c²)/2) r² and the multiplicities (1+8+5 = 14). Correct; a standard
      Landau potential with a cubic invariant on the 14-dimensional representation of Sp(3). The file says
      that it "does not assert a new discovery of that phase diagram".
  11. Sign of the gauge kinetic term with anti-Hermitian generators and (+−−−) corrected; group action
      gZk^{−1} instead of gZk. Corrections of the packets.
- **Support**: written proofs and exact checker scripts (named at 5742–5840). Ledger S6-Q444-EMBEDDED-
  RECONCILIATION, -OMITTED-COORDINATE-FORCE, -ACTION-CONVENTIONS, -INVARIANT-SECTORS, -FOURTH-JET,
  -MOVING-KERNEL, -SCALAR-VACUA, -POSITIVE-OBSERVATION: VERIFIED.
- **What it adds**: nothing over [AC26] or [E26]. Over the literature: nothing new that I can see; not searched.
- **First assessment**: correct where I checked; self-posed model computation.
- **A full check must establish**: nothing for the S6 survey.
- **Deserves a full check**: no. **Interest**: 1.

### F-9
- **Title**: The rotating-ansatz gauge lift of the periodic scalar orbit: exclusions, the scalar–Gauss domain
  S_sg ≅ {±1}² × (0,∞) × R² × T³, and the open existence question. **Type**: computation; open question
  isolated (on the supplied model).
- **Where**: `W\quaternionic_4441_reconciliation.tex` 2371–5740; `W\two_cross_exceptional_shared.tex`;
  `W\scalar_gauss_domain_shared.tex`; `W\scalar_gauss_smooth_shared.tex`; 4–5 Sep 2026.
- **Statement**: For the fixed data H, q, A (displayed at 3974–3980; m² = Γ = 1, κ = 6) find
  (t = g² > 0, ω ≠ 0, C, Z_1, Z_2 ∈ su(3)) with
  [C,[C,H]] − Σ[Z_j,[Z_j,H]] = F; (C² − Z_1² − Z_2²)q = −2q; (tI + 2K)C = 4ω[Z_1,Z_2];
  −ω²Z_1 − 2ω[C,Z_2] + [C,[C,Z_1]] + KZ_1 + (t/2)IZ_1 = 0; and the same with (1,2) exchanged and the sign of
  2ω reversed. Proved: no solution with A_0 = 0 (temporal gauge) for the literal orbit; no solution with all
  connections real skew; no solution with Z_1, Z_2 in the cross space p (two-cross exclusion); for a fixed
  spatial pair the admissible couplings are the positive roots of a polynomial of degree 28 (at most 14
  couplings); solutions project into the zero set of a nonzero polynomial R (a 24×24 Sylvester determinant),
  hence a closed nowhere dense set; the solution set of the scalar and Gauss equations alone in the two-cross
  class is an embedded 6-manifold with four components ≅ D × T³, globally {±1}² × (0,∞) × R² × T³ with t the
  positive coordinate, nonempty at every t. Open: whether the full system has any solution on the remaining
  exceptional set.
- **Support**: written proofs plus exact symbolic and finite-field checkers (evidence folders named in the
  file). Ledger S6-Q444-FULL-GAUGE-LIFT-EXCLUSIONS, -COMPLEX-ROTATING-CONTINUATION, Q444-EXACT-FINITE-COUPLING-
  FIBRE, Q444-GENERIC-SPATIAL-EXCLUSION, Q444-TWO-CROSS-*, Q444-SCALAR-GAUSS-SMOOTH-LITERAL-PRODUCT: VERIFIED.
- **What it adds**: nothing about X. It is a real-algebraic elimination problem about one family of
  homogeneous solutions of an SU(3) gauge–scalar system with a particular potential.
- **First assessment**: I read the statements and the scope sections only. The open question is well posed (a
  finite polynomial system) but self-posed; its answer would not bear on X or on Yang–Mills theory in
  general. The product decomposition of S_sg is a parametrization of a solution set that has no invariant
  meaning beyond this ansatz.
- **A full check must establish**: nothing for the S6 survey.
- **Deserves a full check**: no. **Interest**: 1.

### F-10
- **Title**: Flat-metric dictionary for the rank-three toroidal extension of the cusp (period Gram matrices,
  metric fibres, the quotient T_3 → T_2 as a Riemannian submersion). **Type**: computation / expository.
- **Where**: `W\quaternionic_4441_reconciliation.tex` 521–1625 (Prop. `q444:period-gram`, Thm
  `q444:metric-fibre`, Thm `q444:hermitian-cometric`, Thm `q444:metric-submersion`, Prop.
  `q444:native-period-spectrum`).
- **Statement**: With Z_2 = sB_0 + C_2(t) (the cusp periods), S = [[1,1],[0,1],[0,0]], Q_latt = B_0^{−1}P,
  C_3 = S C_2 Q_latt, Z_3 = sI_3 + C_3: P Z_3 = Z_2 Q_latt, so [z] ↦ [Pz] is a surjective holomorphic
  homomorphism T_3 = C³/(Z³ + Z_3Z³) → T_2 with connected kernel Cu/(Zu + sZu). For a positive real lattice
  cometric W: H_3 = Ω_3 W Ω_3* and P H_3 P* = Ω_2 (Φ W Φ^t) Ω_2*; no constant W is periodic under s ↦ s+1;
  W(s) = M(−Re s) W_* M(−Re s)^t descends, with det(P H_3 P*) = y⁴ det(PKP*) + O(y³). All positive W over a
  given H form an open convex 12-dimensional set; the unique Hermitian-compatible one has h_3 = 2H^{−1}. The
  submersion metric on T_2 is h_2 = 2(PH_3P*)^{−1}; target characters pull back to the source characters
  constant on fibres. For h_3 = I: λ_1(T_3) ~ 4π²/y², λ_1(T_2) ~ 8π²/y², Vol(T_3) = det Y ~ y³.
- **Support**: written proofs; checker `exact_period_metric_checker.py`,
  `exact_hermitian_metric_spectrum_checker.py`. Ledger S6-Q444-PERIOD-GRAM, S6-Q444-HERMITIAN-PERIOD-SPECTRUM,
  q444:metric-fibre: VERIFIED.
- **What it adds**: the family T_3 is the torus of the toric cusp chart modulo the lifted action, an object of
  the workbench's "higher-rung toroidal elliptic bridge" (not in this assignment). The statements are linear
  algebra over the cusp periods. The one point of substance is the observation that a period-derived Gram
  matrix needs a monodromy-compatible varying lattice metric (same phenomenon as F-1 (i)).
- **First assessment**: routine and, as far as read, correct.
- **A full check must establish**: nothing for the S6 survey beyond the check of the module it depends on.
- **Deserves a full check**: no. **Interest**: 1.

### F-11
- **Title**: Presymplectic reduction of the SU(3)-Gram worldline model. **Type**: computation on a supplied
  model; self-contained.
- **Where**: `W\worldline_presymplectic_reduction.tex`; wrapper
  `R\s6_worldline_presymplectic_reduction_preprint.tex`.
- **Statement**: For S = ∫(⟨αZ*Z, ẋ⟩_L − (e/2)(det(αZ*Z) − m_0²c²)) dτ on Herm_2(C) × Mat_{3×2}(C) × R with
  left SU(3): Mat_{3×2}(C)/SU(3) ≅ PSD_2 by the Gram map, orbit types SU(3), S⁵, point. m_0 > 0: constraint
  surface smooth, action free, presymplectic kernel = 8 colour directions ⊕ R(p,0) ⊕ R∂_e, equations ṗ = 0,
  ẋ = e p, reduced space T*H⁺_{m_0,c}: the free relativistic particle. m_0 = 0, rank one: intrinsic reduction
  T*N_+^×, but det(αZ*Z) = α² Σ_{a<b}|Δ_ab(Z)|² has zero differential on rank ≤ 1, so the written multiplier
  action gives ẋ = λp with λ unrelated to e, four extra null directions, and arbitrary x(τ) at Z = 0.
  Hard-threshold packet variant: ẋ = 0 above threshold.
- **Support**: written proofs and `verify_worldline_reduction.py`. Ledger S6-WPR-MASSIVE-REDUCTION,
  -MASSLESS-PUNCTURED, -ZERO-APEX, -HARD-THRESHOLD-DYNAMICS: VERIFIED.
- **What it adds**: nothing about X (the model lives on the "Lorentzian" Herm_2(C) of F-12). As mathematics it
  is a clean worked example of a singular constraint (a quadratic composite momentum whose mass-shell function
  is not regular on the null cone); the phenomenon is standard in constrained dynamics. Not searched.
- **First assessment**: looks correct; the massless irregularity is the only point of interest.
- **A full check must establish**: nothing for the S6 survey.
- **Deserves a full check**: no. **Interest**: 1.

### F-12
- **Title**: The Hessian of det at a rank-one point of Herm_3(C) is the Minkowski form on Herm_2(C); the
  "candidate cusp matrix" is spacelike. **Type**: expository only (restatement of known facts, with one remark
  that restates [E26] 8.4).
- **Where**: `W\hermitian_normal_slice_physics.tex` (Thm `hnsp-lorentz-theorem` 132; Prop.
  `hnsp-candidate-spacelike` 538; Prop. 1126; Thm `hnsp-coercive-transfer` 1220).
- **Statement**: ½ D²(det)_{uu*}[X,Y] = η_2(G,K) for X = R_P G R_P*, i.e. det on Herm_2(C), signature (1,3);
  SL_2(C) acts through the spin cover. For G_{η,T} = [[2L_T, 2m_T],[2m_T, −q_T/3]]:
  det G_{η,T} = −(2/3) D_T < 0, coordinates (t,x,y,z) = (L − q/6, 2m, L + q/6, 0), direction → (5/6, 0, 7/6, 0).
  No positive-definite quadratic form on the slice is Lorentz invariant. The rest of the file builds a free
  Klein–Gordon field, lattice regulators and a gauge–scalar model on this "host".
- **Support**: written proofs.
- **What it adds**: G_{η,T} is (1/3 of) the Hermitian form of the invariant class η; det < 0 is the statement
  that its signature is (1,1), which is [AC26] §9.1 and [E26] Remark 8.4. Read this way, the radial cusp
  traces a curve in the space of indefinite Hermitian forms, i.e. in the period domain Sp_4(R)/U(1,1) of
  [E26] 8.4. The file does not take this step and does not address Klingler's question (proper discontinuity
  of the monodromy group on that domain); none of the files of this assignment does.
- **First assessment**: correct and elementary; the physics built on it is a choice, as the file's "Exact
  conclusion" says.
- **A full check must establish**: nothing.
- **Deserves a full check**: no. **Interest**: 1 (the open question it brushes against, Klingler's, is of
  interest 4 but is not treated here).

### F-13
- **Title**: Compact resolvent, unique ground state and positive gap for the 38-coordinate homogeneous SU(3)
  gauge–adjoint–triplet quantum mechanics; Born–Oppenheimer comparison for a two-mode truncation.
  **Type**: computation on a supplied model.
- **Where**: `W\homogeneous_quantum_confinement.tex`; wrapper `R\s6_homogeneous_quantum_confinement.tex`.
- **Statement**: H_hom ≥ (ηħ²g²/4V_3) T_A + (ħ²/2V_3) T_E + ħ√(6(1−η)) Σ_i‖A_i‖ + (V_3Γ/8)s² − V_3 C_κ for
  0 < η < 1 (Thm `qh:full-compact`); e^{−τH} positivity improving; unique SU(3)-invariant positive ground
  state; E_1^phys − E_0 > 0 at fixed ħ, g², V_3, Γ. The homogeneous classical solutions embed in the torus
  field theory; a quartic coupling 3ΓV_3 q²y²/4 prevents a product reducing subspace. Second part: effective
  Hamiltonian with Born–Huang term ħ²‖Ω'_q‖²/(2V_3), error O(V_3^{−1/2}).
- **Support**: written proofs. Ledger S6-Q444-HOMOGENEOUS-QUANTUM-GAP, -SUBSECTOR-OBSTRUCTION,
  S6-Q444-MOVING-FOURIER-QUANTUM-COMPARISON: VERIFIED.
- **What it adds**: nothing about X ("does not require the construction of a compact complex structure on
  S⁶", line 37). The discreteness of bosonic matrix models with commutator potentials is classical (the file
  says so at 17–22); the explicit constant √6 from the su(3) root sum is a small detail. Not searched.
- **First assessment**: plausible; the gap is that of a finite-dimensional quantum mechanics at fixed volume
  and the file says so in the corollary and after it.
- **A full check must establish**: nothing for the S6 survey.
- **Deserves a full check**: no. **Interest**: 1.

### F-14
- **Title**: The Yang–Mills drafts stored with the S6 project (grouped): strong-coupling and finite-box
  results for the SU(2) Kogut–Susskind Hamiltonian. **Type**: computation (lattice gauge theory); outside S6.
- **Where**: `W\ym_bulk_plaquette_extension.tex`; the eleven `R\s6_*_draft.tex` files of §1.4; 8–9 Sep 2026.
- **Statement** (the ones I saw stated precisely): (i) on the open box, for small ξ = b/κ,
  R_ret − R_corr = (1951/81675) b²/κ + O_L(b³/κ²) (= (1951/653400)/(g⁶a) in the original parameters), a strict
  improvement of an upper bound for the physical gap, which tends to 3κ as ξ → 0; (ii)
  (H − E)|_{ψ^⊥} ≥ (3κ/4)(1 − 512ξ/3) for 0 < ξ ≤ 1/49152, uniformly in the box size L
  (`s6_spatial_continuum_draft.tex` §9, eq. (62)), by Yarotsky's creation-coordinate method with all constants;
  (iii) the Wilson transfer operator converges strongly to e^{−tH} on a finite spatial lattice with an exact
  character multiplier; (iv) the perturbative analyticity disc |ξ| < 3/(16 M_L) shrinks with the volume (FC8).
- **Support**: long written derivations (converted from Markdown), exact rational checkers
  (`check_bulk_plaquette_incidence.py` and others). I did not read proofs.
- **What it adds**: nothing on S6. The only input from X is θ = 2πa²/D. For lattice gauge theory: a uniform
  gap at strong coupling is the expected and essentially known statement (Euclidean strong-coupling
  expansions; here in Hamiltonian form through Yarotsky's theorem); explicit constants may be of some use.
  Not searched.
- **First assessment**: the drafts are consistently worded as finite-regulator results; each says it does not
  prove or refute a mass gap. The sentence at the end of the spatial-continuum draft keeps "the proposed
  four-dimensional mass-gap counterexample" as an unresolved target (see Doubts 3.5).
- **A full check must establish**: belongs to a review of the Yang–Mills repository, not of S6.
- **Deserves a full check**: no (for this survey). **Interest**: 1 for S6; 2 for the lattice statements (ii)
  and (i) if someone reviews the Yang–Mills programme.

---

## 3. Doubts and errors

3.1 **The metric is a choice, and the vocabulary sometimes hides it.** The cusp files call the Euclidean
period metric "native", "physical", "actual". The files do declare the choice (cusp_spectral_geometry 83–86,
1350–1354; preprint 2291) and prove that complex data do not fix a gap. But nowhere do they say what the
choice is in invariant terms (the flat Kähler metric that is unitary on a basis of the vanishing lattice
ker(M_0 − I)), nor that it is opposite in character to any metric coming from X: in X the cycles ŵ, δ̂ shrink.
A reader of the preprint abstract ("on the actual manuscript cusp … sharp asymptotics") could take λ_1 ~ 4π²/T²
for a property of X.

3.2 **The constants H, B, m.** B = Im(β+τ)(0) is a free parameter of the construction (the modulus of the
family), H depends on the normalization of the base coordinate, and m is a fixed number of the elliptic
surface. The files treat all three as "limiting cusp constants" of "the actual cusp" on the same footing
(the scope paragraph mentions only the freedom in β). Not an error, but the boxed formula for λ_1 mixes a
modulus, a coordinate convention and an invariant. My values H = log 1728/(2π), |m| = log(5+2√6)/(2π) need
confirmation against the workbench conventions.

3.3 **"Morse index 144" and "unstable for every finite T" are metric statements.** See F-4 (1): on the same
fibre there are flat Kähler metrics for which L_η ⊕ L_η^{−1} is anti-self-dual and stable. The file's
"stability boundary" proposition presents S_T = 0 as a parameter wall in T, which never occurs deep in the
cusp for the Euclidean metric; it does not mention that the wall is crossed by changing the metric at fixed T.

3.4 **Finiteness theorem is weaker than the truth, and its remark could mislead.** Thm
`cusp-spec-elliptic-descent-finiteness` proves "finite"; the locus is {0, 1, t_+, t_−} (F-3). The remark at
1165 lists as open "that A_z has no other elliptic quotient or elliptic subtorus": in fact fibres with other
elliptic quotients form a dense countable set (F-3 (c)), so the corollary "the first-coordinate Landau sector
does not run into the cusp" (preprint `cor:no-landau-cusp`) is true only for the literal map to C/(Zτ+Z);
quotients onto C/(Zτ + Z + Z·6μ) with 6μ torsion do accumulate at the cusp.

3.5 **Framing of the Yang–Mills drafts.** No file presents a finite-dimensional or classical model as a
statement about the quantum mass gap; I found no such overclaim in the assigned files. What can mislead is
(a) the file names `s6_*` and titles such as "The retained cusp, spatial refinement, and the spectral measure
of the actual magnetic vacuum translation", which suggest that the S6 geometry does work in these papers,
while its whole contribution is the number D in θ = 2πa²/D; (b) the standing phrase "the proposed
four-dimensional mass-gap counterexample" (`s6_spatial_continuum_draft.tex`, last section) and "gap-closing
sequence" in the cusp files: the gap that closes is that of a Laplacian on a torus whose size goes to
infinity, and the cusp files themselves list (cusp_gauge_operators 756–790) why this says nothing about a
mass; (c) abstract "transfer" propositions (`cusp-interpretation-typed-physical-transfer`,
`cusp-gauge-no-gap-bridge`, `hnsp-coercive-transfer`, the "full-domain coercive gap transfer" of the
compact-link preprint) are correct one-line functional analysis with hypotheses that nothing in the project
verifies; the files say so, and the ledger entry S6-OPEN-YM-PHYSICAL-BRIDGE is OPEN.

3.6 **`s6_xi4_heat_transport_draft.tex`.** Its abstract joins the de Bruijn–Newman flow, a quotient of
Connes, a polynomial of Tao, a "corrected Navier–Stokes source", and the three special points of the S6 base,
with sentences such as "the inverse-fibre construction alone does not exhibit a counterexample to the Riemann
hypothesis or to the classical Euclidean Navier–Stokes problem". I read only the abstract and the list of
inputs. Nothing in it is needed for S6; I would not spend checking time on it, and I would not cite it. The
included `s6_three_point_quotient.tex` may contain a correct description of a real quotient torus (cf. [E26]
8.3), but that belongs to the reader of the globalization modules.

3.7 **Status vocabulary.** The preprint `R\s6_spectral_degeneration_preprint.tex` is titled "Conditional
results from the reconstructed candidate S⁶" (4 Sep): this is the caution of that date, as the brief says.

3.8 **A small point in `cusp-interpretation-typed-physical-transfer`.** The proof concludes "zero is not an
eigenvalue, hence a continuous spectral point, hence in the essential spectrum"; correct (a non-eigenvalue
point of the spectrum of a self-adjoint operator is not isolated), but the proposition is a restatement of the
variational principle and should not be counted as a result.

3.9 **Quaternionic block: provenance of the model.** The Lagrangian and the 4+4+4+1 slice are taken from two
GPT Pro packets; the workbench corrects three of their conventions or claims (F-8 items 5, 6, 11) and says
that it "does not certify every theorem in either supplied packet". Ledger entries with the prefix S6-Q444
therefore do not concern S6.

---

## 4. Not read

- Proofs in `cusp_gauge_operators.tex`, `cusp_su2_magnetic.tex` (except statements), `cusp_native_full_flux_suN.tex`,
  `cusp_native_full_flux_radial.tex`, `cusp_compact_link_gaussian.tex`: statements and scope paragraphs only,
  since none is a candidate of interest 3 or more.
- `quaternionic_4441_reconciliation.tex`: of 5840 lines about 1900 read (listed in §1.2); for 2400–5740 only the
  statements and the scope sections. `scalar_gauss_*`, `two_cross_exceptional_shared.tex`: main statements only.
- `hermitian_normal_slice_physics.tex` 160–528 and 612–1120; `homogeneous_quantum_confinement.tex` proofs and the
  second section; `worldline_presymplectic_reduction.tex` 350–720 and 760–991; `ym_bulk_plaquette_extension.tex`
  75–990: not read (model computations, assignment says light).
- The five `*_preprint.tex` twins in `W`: confirmed as views and skipped.
- Root-level drafts: only title, opening paragraphs, statement heads and (for the spatial-continuum draft) §9
  opening and the last section, as assigned. `R\s6_compact_link_gaussian_preprint.tex`: statement heads only.
- Modules `\input` by `cusp_spectral_geometry.tex` but not assigned (`cusp_globalization_replacement`,
  `cusp_toric_cover_completion`, `cusp_cone_sphere_routes`, `cusp_sphere_route_strengthening`,
  `cusp_s12_carrier_homotopy`, `cusp_sphere_fixed_metric`): not read.
- Evidence folders, checker scripts and the files under
  `evidence\ym_sidebar_topics_20260908\xi4_heat_transport\tex\` (except the first 80 lines of
  `s6_three_point_quotient.tex`): not read.
- The public repository: only a directory listing of `repo\` and `repo\yang-mills\` to confirm that the drafts
  moved there.
- Literature searches on the web: none made; no candidate reached interest 4. Comparisons were made against
  the transcription of [AC26] (§9.1, Cor. 9.8, lines 312, 3274–3556) and the text of [E26] (§2, Remarks
  8.3–8.4).
