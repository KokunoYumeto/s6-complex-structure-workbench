# D2 notes — the "Koide" arithmetic side lane of the S6 workbench

Reader D2, 12 Nov 2026 (Claude Fable 5.2). Read only; scratch scripts and data in
`C:\Users\user\Documents\workbench_review_20261112\work\scratch\D2\` (`recount.c`, `recount2.c`,
`analyze.py`, `checks.py`, `cnt_1e7.bin`).

Base folder below: `C:\Users\user\Documents\math\research\s6_recent_results_main\canonical_S6_snapshot\`
(abbreviated `SNAP\`); `W\` = `SNAP\supporting_materials\workbench\`.

## 0. Answers to the four questions, in short

**Q1. Where the quadric comes from; is the S6 link mathematical or nominal?** Nominal.

- "Koide" is the Koide charged-lepton relation m1+m2+m3 = (2/3)(√m1+√m2+√m3)². In r_i = √m_i it is the null cone
  of Q_K(r) = (2/3)(r1+r2+r3)² − (r1²+r2²+r3²), a real quadratic form of signature (1,2).
- The integer form is Δ(x,y,z) = 4(xy+xz+yz) − (x²+y²+z²) = 3·Q_K(x,y,z). The lane counts integer points on the
  level Δ = −1 (one step off the Koide cone; "defect one"; in the source packet "Koide–Narain root shell": the
  vectors of norm −1 in the Lorentzian lattice (Z³, Δ), whose reflections are the Vieta moves x ↦ 4(y+z) − x).
- The quadric a² − 3q² − 18n² = −2 is the same surface after the integral substitution n = z − 4(x+y), q = y − x,
  a = x + y − 4n (then 2Δ = a² − 3q² − 18n² and z = 4a + 17n). It is not derived from the threefold: not from a
  Néron–Severi lattice, not from the period lattice of a fibre, not from the invariant (1,6) class.
- The only bridge to S6 is `koide_period_discriminant.tex`: with the period convention Z = (6μ τ; β μ), Π = [Z | I],
  the 4×4 realified period matrix has det P = Imτ·Imβ − 6(Imμ)² = −det Im Z, a real form of signature (1,2) on the
  three imaginary parts, and the real-linear map (h,x,y) ↦ (Imτ, Imμ, Imβ) = (h+y, x/√6, h−y) carries Q_K to it.
  Any two real ternary forms of signature (1,2) are isomorphic, so this says nothing. The workbench itself says so
  (Cor. koide-s6-cor-ambient-only: the Koide cone is the locus det P = 0, where the columns do not span a lattice;
  Cor. koide-s6-cor-actual-cusp: on the actual cusp det P_T = −D_T ~ −T² ≠ 0; ledger "nonclaim").
- It is weaker than the workbench says: over Q the two forms are not even equivalent or similar. tρ − 6m² is
  isotropic over Q (t = m = 0), while Δ = 3Q_K is anisotropic over Q (mod-3 descent, Lemma esv3-anisotropic; I found
  no zero in the box |x|,|y|,|z| ≤ 30). The √6 in the map is the witness. So there is no rational or integral
  dictionary between Koide triples and periods, only a real one. (The 6 in the form is the 6 of Engel's (1,6)
  class, [E26] §8.4, where Im Z has signature (1,1); that is the whole connection.)
- Origin by provenance: a ChatGPT Pro-mode packet `S6_Koide_MassGap_Research_Packet (1).zip` ("T1", early Sep 2026)
  that tried to tie Koide, the S6 periods and a Yang–Mills mass gap together. The Codex workbench audited it, kept the
  arithmetic as a separate preprint line, and recorded that it is independent of S6 (research_log Round 28–29, 37).

**Q2. The arithmetic statements.** All are correct as far as I checked (statement by statement in §2). All are
applications of known theory to one explicit quadric: Vieta descent (elementary), Siegel/Borovoi local densities,
Gorodnik–Oh–Shah / Duke–Rudnick–Sarnak / Eskin–McMullen for the main term, Benoist–Oh for an unspecified power
saving, ideal theory of Z[√3], the standard quadric ↔ quaternion order dictionary. Nothing beyond known theory is
proved. The explicit constant C_0, the exact parametrization and the census are computations. My recount (different
coordinates, C, 75 s) reproduces R(X) at every checkpoint up to 10^7 and the location and value of the extremum
max |E|/√X = 0.171400 at X = 867,240.

**Q3. The open item.** It is a hyperbolic lattice-point problem with a sharp cutoff; square-root cancellation is the
standard conjecture for such problems, the census agrees with it (|E(X)| ≤ 0.172·√X on [10^4, 10^8], no growth of
E/√X), and a proof is out of reach of present methods: the best exponent known for every problem of this type is 2/3
(Selberg, Good 1983; unchanged in 2025). What the workbench missed: the height 4a+17n is not exotic. In the
original coordinates it is the coordinate z, and z = (1/3)·cosh(distance from the geodesic of the point to one fixed
closed geodesic). So R(X) is the count of common perpendiculars between closed geodesics (Good's
hyperbolic–hyperbolic case; Martin–McKee–Wambach 2011; Voskou 2024; Lekkas–Petridis 2025) restricted to those
whose foot lies in a fixed arc, of proportion λ_0 = log(3/(2√2))/log(2+√3) = 0.04472 of the closed geodesic.
Equivalently R(X) = Σ_{z≤X} #{ideals of Z[√3] of norm 18z²−2 with Hecke angle in [0, λ_0]} + O(log X). This gives a
much cleaner problem statement (candidate D2-8, D2-9) and realistic sub-targets (explicit exponent, mean square).

**Q4. Wrong or overclaimed.** No false theorem found. Overclaims of relevance and two misjudgments in the literature
positioning: see §3.

---

## 1. Reading notes

All files dated 29 Sep 2026 00:32 on disk (snapshot copy time); internal dates 3–4 Sep 2026.

### 1.1 `W\research\koide_period_discriminant.tex` (6.7 KB, 201 lines)
Subsection "The Koide cone and the canonical period discriminant", label `koide-s6-subsection-ambient-discriminant`.
Input by `SNAP\workbench.tex` line 1629.
- Defines Q_K (eq. koide-s6-eq-koide-form), orthogonal matrix 𝓕 with rows (1,1,1)/√3, (1,0,−1)/√2, (1,−2,1)/√6,
  the period convention Z = (6μ τ; β μ), the 4×4 real matrix P(τ,μ,β), and S(t,m,ϱ) = (t √6m; √6m ϱ).
- **Theorem koide-s6-thm-ambient-discriminant** ("Ambient coefficient-space discriminant isomorphism"):
  Q_K = h² − x² − y²; 𝒦(h,x,y) = (h+y, x/√6, h−y); det P = det S = tϱ − 6m²; det P(𝒦𝓕 r) = Q_K(r); on the nonnegative
  Koide cone S is positive semidefinite of rank one. Proof: 20 lines of linear algebra. Correct.
- **Cor. koide-s6-cor-ambient-only**: the identification is ambient only; on the Koide cone det P = 0, no torus.
- **Cor. koide-s6-cor-actual-cusp**: det P_T = −D_T < 0, D_T = T² + (2H−B)T + O(1), citing `cusp-spec-determinant`,
  `cusp-spec-D-expansion` (in `cusp_spectral_geometry.tex`, another reader's file).
- Ledger: S6-KOIDE-AMBIENT-DISCRIMINANT, VERIFIED; uncertainties.txt U-KOIDE-CUSP-RELATION, VERIFIED.

### 1.2 `W\research\koide_counting_repair.tex` (41 KB, 1159 lines)
Section "Exact arithmetic of the Koide defect-one shell", label `koide-count-sec-main`. Input by `workbench.tex`
line 1631 and by the root preprint. Its last four lines input the parametrization, census, quaternion and
literature files. "Repair": the source packet compared counts with X/(9π) (field `max_z_over_9pi` in the stored
JSON); the workbench replaced that by a proved constant. First sentence: the section "does not use the existence of
the proposed complex structure on S^6, any period-map assertion, or any Yang–Mills interpretation".
- §Vieta (`koide-count-subsec-vieta`): Δ = 3Q_K (eq. defect-qk); Gram matrix A_K = (−1 2 2; 2 −1 2; 2 2 −1),
  signature (1,2); **Prop. vieta-reflections** (s_i are the reflections in e_i, B_K(e_i,e_i) = −1);
  **Prop. vieta-reduction** (0<x≤y≤z, Δ=−1: if z < 4(x+y) then 0 < z' < y, z' = 4(x+y) − z);
  reduced set 𝓡 = {0<x≤y≤z, Δ=−1, z ≥ 4(x+y)}, R(X) = #{𝓡, z ≤ X} (eq. rx-definition);
  **Prop. vieta-forest** (positive solutions form a rooted forest; roots = 𝓡);
  **Thm coordinate-bijection** (Φ: 𝓡 → 𝓣 = {a>0, q≥0, n≥0, a+4n>q, a²−3q²−18n² = −2}, inverse
  ((a+4n−q)/2, (a+4n+q)/2, 4a+17n); 2Δ = a²−3q²−18n²);
  **Prop. pell-faces** (n=0 face: a_k+q_k√3 = (1+√3)(2+√3)^k, k ≥ 1; q=0 face: A_k+N_k√18 = (4+√18)(17+4√18)^k,
  k ≥ 0; each O(log X) points).
- §local (`koide-count-subsec-local`): F = a²−3q²−18n², 𝒳 = {F = −2}; **Thm local-densities**: σ_2 = 3/2, σ_3 = 2,
  σ_p = (1−p^{-2})/(1−(3/p)p^{-1}) for p ≥ 5; 𝔖 = (9/2)·L(1,χ_12)/ζ(2) = (9/2)·log(2+√3)/(√3 ζ(2)).
- §archimedean: gauge form ω_∞ = dq∧dn/(2a); **Thm archimedean-factor**: m_∞{𝒳(R)∩𝒞, 4a+17n ≤ X} ~ I_∞ X,
  I_∞ = (1/(2√3))·log(3/(2√2)).
- §gos: **Lemma genuine-norm** (‖(a,q,n)‖_* = max{|4a+17n|,|q|,|a|} equals the height on the chamber);
  **Lemma gos-hypotheses** (Spin(F), x_0 = (1,1,0), stabilizer = norm-one torus of Q(√3), no Q-characters; the cone
  is admissible and generic for Gorodnik–Oh–Shah 2009 Thm 1.6).
- §borovoi: **Prop. finite-sign-balance**: Borovoi's coefficient c_𝒳 = 1, by the explicit g = r_v r_e ∈ SO(F, Z_2)
  (v = (1,0,1), e = (1,0,0)), spinor norm −17, (−17,3)_2 = −1.
- §calibration: **Thm linear-asymptotic**: R(X) ~ C_0 X, C_0 = 𝔖·I_∞ = (9/(2π²))·log(2+√3)·log(3/(2√2))
  = 0.035362047799731853…
- §computation: first roots (1,4,20), (4,4,33), (4,8,49), (4,15,76), (8,24,129); table X = 10^4 … 2·10^5;
  **Open problem `koide-count-open-square-root-discrepancy`** (R(X) − C_0X = O(X^{1/2+ε})?), marked OPEN.
- Status in ledger: S6-KOIDE-DEFECT-COUNTING, VERIFIED (one entry covering this file and the parametrization file).

### 1.3 `W\research\koide_exact_parametrization.tex` (45 KB, 1186 lines)
"Integrated 4 September 2026"; labels `koide-param-*`. Sections: arithmetic of Z[√3]; HNF parameters; complete
integral parametrization; divisor and sharp-height formulas; phase term as Hecke-character data; unconditional
effective exponent; exact obstruction to the square-root claim; boundary ledger.
- Lemma ring-units (h = 1, units ±ε^j, ε = 2+√3, no unit of norm −1); Lemma ideal-number (#ideals of norm m =
  ρ(m) = Σ_{d|m} χ_12(d)); **Prop. HNF-ideals** ((C,D,E) with C²D = m, 0 ≤ E < D, E² ≡ 3 (D) ↦ C(DZ + (E+√3)Z) is a
  bijection onto ideals of norm m); m_n = 18n² − 2; Lemma positive-norm-generator; **Lemma integral-seed-descent**
  (seed condition a > 2q ≥ 0; descent (a,q) ↦ (2a−3q, 2q−a)); **Thm integral-parametrization** ((n, 𝔭, k) ↦
  α_{n,𝔭} ε^k is a bijection onto solutions with a>0, q≥0, n≥1; multiplicity one); Prop. n-zero;
  **Prop. orbit-divisor** (number of unit orbits at fixed n is ρ(m_n) = ρ(3n−1)ρ(3n+1));
  **Thm exact-floor** (R(X) = R_0(X) + Σ_{n∈𝒩(X)} Σ_𝔭 (⌊L_n(X) − τ_{n,𝔭}⌋ + 1));
  eq. exact-discrepancy-splitting (R − C_0X = R_0 + [Σ ρ(m_n)L_n(X) − C_0X] + Σ Δ_n(λ_n(X)));
  Hecke characters ξ_ℓ, S_ℓ(m) = Σ_{N𝔞=m} ξ_ℓ(𝔞), S_ℓ(18n²−2) = (−1)^ℓ S_ℓ(3n−1)S_ℓ(3n+1) (eq.
  shifted-Hecke-factorization), Fejér identity (eq. Fejer-exact, exact-shifted-Hecke-correlation).
- **Lemma volume** (m_∞(B_X) = I_∞X + O(1); B_X is effectively well-rounded in the sense of Benoist–Oh Def. 13.1);
  **Thm power-saving**: R(X) = C_0X + O(X^{1−η}) for some unspecified η > 0 (Benoist–Oh 2012 Thm 13.2 applied to
  each of the finitely many integral orbits).
- "Exact obstruction": two descriptions; says explicitly that 2/3 is not claimed for R(X).
- Replay script `W\evidence\koide_exact_checkpoint_20260904\parametrization\verify_parametrization.py`
  (1 ≤ n ≤ 200, exact integers).

### 1.4 `W\research\koide_exact_census.tex` (7.8 KB, 203 lines)
Section `koide-count-sec-census-1e8`. **R(10^8) = 3,536,002**; n_max = 2,943,725; 2,327,513 unit orbits;
checkpoint table 2·10^5 … 10^8; max E = +721.79 at X = 77,078,404; min E = −812.83 at X = 32,461,294;
max |E|/√X on [10^4,10^8] = 0.171400 at X = 867,240 (root (a,q,n) = (199997,115061,3956));
12,916 sign changes; 2,472,015 occupied heights; max multiplicity 35 at z = 92,923,120; largest gap 564.
Ledger S6-KOIDE-CENSUS-1E8, VERIFIED. Evidence: `W\evidence\koide_exact_checkpoint_20260904\census\`
(`koide_fast_enum.py` 40 KB: SPF sieve, HNF triples, Lagrange–Mollin–Matthews continued fraction for a generator,
seed descent, unit orbit; `METHOD_AND_RESULTS.md` 21 KB; `FINAL_RECEIPT.json`; `validate_fast_enum.py`;
`audit_coordinate_file.py`; `final_100000000\` with the 76 MB coordinate file, not opened).

### 1.5 `W\research\koide_quaternion_bridge.tex` (29 KB, 822 lines)
Section `koide-quat-exact-quaternion-bridge-order-shell-and-hyperbolic-conjugacy-classes`; converted from a
Markdown report (headings `koide-quat-*`; no theorem environments, boxed formulas).
- B = (18,−6)_Q, K = IJ, K² = 108; order 𝒪 = Z ⊕ Z(I+J)/2 ⊕ Z(I−J)/2 ⊕ Z K/2 with multiplication table
  (eq. multiplication-table); nrd(r+sE+tF_0+uG) = r² − 3s² − 12st − 3t² − 27u²; reduced discriminant 108, index 18
  in a maximal order, not Eichler; Ram(B) = {2,3}, disc 6.
- Shell bijection (eq. shell-bijection): (a,q,n) with F = −2 ↔ γ = 2 + (qI + aJ + nK)/2, trd γ = 4, nrd γ = 1;
  γ² − 4γ + 1 = 0; 𝒪 ∩ Q(γ) = Z[γ−2] ≅ Z[√3]; C_Γ(γ) = {±γ^k}; every γ primitive hyperbolic of length
  2 log(2+√3); finitely many Γ-classes (h not computed); class decomposition of R(X) (eq. koide-class-count);
  "radial Huber parameter" X_i(γ)² = 1 + (7a + 15√2 n)²/48 for the base point i of one chosen splitting.
- Conclusion: places the problem "beside" the conjugacy-class lattice-point problem (Huber; Good Thm 4;
  Chatzakos–Petridis 2016, O(X^{2/3}), Conj. 5.7 O(X^{1/2+ε})) and lists nine missing items.
- Ledger S6-KOIDE-QUATERNION-BRIDGE, VERIFIED. Replay `…\quaternion\verify_quaternion_bridge.py` (48 shell points in
  a box, Hilbert symbols; log PASS).

### 1.6 `W\research\koide_effective_literature_audit.tex` (57 KB, 844 lines)
Section `koide-lit-…`, dated 4 Sep 2026. Determination (`koide-lit-determination`): no listed theorem gives the
square-root bound; strongest exact-domain result is the Benoist–Oh power saving. Result matrix (18 rows: DRS 1993,
Eskin–McMullen 1993, GOS 2009/2010, Benoist–Oh 2012, Gorodnik–Nevo 2012, Liu–Sarnak 2010, Good 1983 /
Chatzakos–Petridis 2016, Bourgain–Kontorovich–Sarnak 2010, Browning–Gorodnik 2017, Cao–Huang 2022,
Cao–Huang–Zhang arXiv:2509.23320, Oh–Shah 2014, Xu–Zhang 2023, Huang arXiv:2412.03350 and 2412.05903, Zhang
arXiv:2603.21080, Li–Liu arXiv:2501.15033, Voskou arXiv:2407.03134, Lekkas–Petridis arXiv:2509.12902). Detailed
subsections: Benoist–Oh applicability (hypotheses, Def. 13.1 check, finite-orbit passage, why η is unspecified:
η = δκ/(p+κ)); Good/Chatzakos–Petridis; "current sharp refinements remain at 2/3"; BKS; Liu–Sarnak (smooth radial
O(T^{1/2+θ+ε}), θ = 7/64 gives 39/64; claims Prop. 3.2 applies class by class to Γ = 𝒪^1 because Γ is congruence:
Kim–Sarnak + Jacquet–Langlands, Chu–Li λ_1 ≥ 975/4096); Gorodnik–Nevo explicit exponents 19/20 and 39/40;
taxonomy table; citation-ready conclusion; 28 references with locators; limitations (Good's book not consulted
directly; no local copies of sources).

### 1.7 `W\research\koide_es_v3_audit.tex` (15 KB, 351 lines)
Section `sec:esv3-audit`, 4 Sep 2026: audit of a Pro-mode packet "Divisor Channels, Prime Saturation, and Bézout
Openings, v3" (Erdős–Straus / Koide). Input by `workbench.tex` line 1606. Mostly Erdős–Straus, only its last two
subsections touch the Koide surface.
- Prop. esv3-channel: bijection (δ,u,v) ↔ ordered solutions of 4/n = 1/a + 1/y + 1/z for n ≡ 1 (4), R ≡ 3 (4),
  a = (n+R)/4, with δ | n², uv = a², R | 4u+δ; corrects an orientation reversal in the packet.
- Integral presentation R_δ = (3 −ℓ_1; 4 −T), 12ℓ_0 − 4ℓ_1 − 3ℓ_2 = δ, SNF diag(1,δ); "gluing admissibility
  3 ∤ ℓ_1 fails exactly when 3 | δ".
- Prop. esv3-diagonal, esv3-density: for primes p ≡ 1 (4) the "diagonal" solutions 4/p = 1/x + 1/(xk) + 1/(pxk),
  x = (p+R)/4, k = (p+1)/R, R | (p+1)/2, R ≡ 3 (4); count ν(p) = ½(τ(m) − Σ_{d|m}χ_4(d)), m = (p+1)/2; density one
  (classical; cites Elsholtz–Tao 2013).
- Bézout opening: A = δvv^T − ww^T, det A = −δ; **REFUTED** packet claim "A_11 > 0 for every real δ > 0"
  (counterexample (r,t,δ) = (2,1,1/8)); a torus with det P_A = −δ is constructed but "does not determine a point on
  the global period curve".
- "Original map's rational nonintersection": the orthogonal map 𝔎_δ sends no rational A to a rational triple.
- Lemma esv3-anisotropic (Δ anisotropic over Q); **Thm esv3-rational-bridge**: stereographic projection from
  (1,0,0) gives an isomorphism of open subsets of {ac − b² = −δ} and {Δ = −1} over Q, with denominator formula.
- Evidence `W\evidence\koide_es_v3_audit_20260904\` (AUDIT_AND_PRO_FEEDBACK.md, CLAIMS.json with ESV3-* ids,
  verify_independent.py, source\ packet with a 58 KB TeX, not read).

### 1.8 `SNAP\koide_arithmetic_preprint.tex` (18 KB, 411 lines) and its PDF (877 KB)
"The Koide Quadratic Cone as a Lorentzian Determinant — Vieta dynamics and a ternary defect-one counting problem",
"Specialist-verification draft, 4 September 2026", no author. A root file: §1 restates the Koide form
(Thm orthogonal-model; Cor. exact-phase-sector: r_i = (h/√3)(1 + √2 cos(θ − θ_i)), nonnegativity arcs
[π/12, π/4] ∪ [3π/4, 11π/12] ∪ [17π/12, 19π/12], endpoint ratio 2±√3; Prop. S6-dictionary = the ambient
discriminant theorem; Cor. rank-one-square; Cor. ambient-only; Remark on the radial cusp), then
`\input{…koide_counting_repair}` (which pulls in everything else), then "Interpretation and limits". It is a view of
the same sources; the only content not in 1.1–1.6 is the phase-sector corollary and the angle π/4 remark (both
elementary and known: Koide's relation as a 45° angle with (1,1,1) is in the Koide literature; cites Kocik 2012).
Abstract still says "a recent proposed complex-torus construction on S^6" (the caution of early September).

### 1.9 Ledger entries (`W\research\ledgers\claim_ledger.txt`)
Line 9 S6-OPEN-KOIDE-SQRT-DISCREPANCY (OPEN); line 67 S6-KOIDE-AMBIENT-DISCRIMINANT; line 68
S6-KOIDE-DEFECT-COUNTING; line 69 S6-KOIDE-CENSUS-1E8; line 70 S6-KOIDE-QUATERNION-BRIDGE (all VERIFIED, each with a
"nonclaim" field saying the arithmetic is independent of S6). `uncertainties.txt` lines 34–35: U-KOIDE-CUSP-RELATION
(VERIFIED), U-KOIDE-SQRT-DISCREPANCY (OPEN). `research_log.tex`: Round 28 (audit of "T1 Koide arithmetic",
normalization still open), Round 29 (3 Sep, normalization closed), Round 37 (4 Sep: parametrization, quaternion
bridge, exponent, census).

### 1.10 `W\reproduction\t1_koide_exact\`
README.md (provenance: copied byte-for-byte from the Pro packet zip, SHA given), `verify_koide_narain_root_density.py`
(13 KB; (n,a) scan with numpy square detection and exact recheck), `koide_verification_200000.json` (R(200000) =
7109; contains the packet's comparison with max_z/(9π)).

### 1.11 Related files not in my assignment (seen, not read)
`SNAP\s6_erdos_straus_koide_bridge_preprint.tex`, `SNAP\s6_koide_es_divisor_extension_audit.tex`,
`W\research\erdos_straus_koide_s6_bridge.tex`, `erdos_straus_selector_crosswalk.tex` (the Erdős–Straus lane).

---

## 2. Candidates

### D2-1
- **Title**: Main term for the reduced "defect-one" roots: R(X) ~ C_0 X with C_0 = (9/(2π²))·log(2+√3)·log(3/(2√2)).
  **Type**: computation (application of known counting theorems to one explicit quadric).
- **Where**: `koide_counting_repair.tex`, Thm `koide-count-thm-local-densities` (l. 421–572), Thm
  `koide-count-thm-archimedean-factor` (l. 611–687), Lemmas genuine-norm, gos-hypotheses (l. 692–832), Prop.
  `koide-count-prop-finite-sign-balance` (l. 854–987), Thm `koide-count-thm-linear-asymptotic` (l. 992–1071);
  3 Sep 2026.
- **Statement**: Let R(X) = #{(x,y,z) ∈ Z³: 0 < x ≤ y ≤ z ≤ X, 4(xy+xz+yz) − (x²+y²+z²) = −1, z ≥ 4(x+y)}
  = #{(a,q,n) ∈ Z³: a²−3q²−18n² = −2, a>0, q≥0, n≥0, a+4n>q, 4a+17n ≤ X}. Then R(X) ~ C_0X with
  C_0 = 𝔖·I_∞, 𝔖 = σ_2σ_3Π_{p≥5}σ_p = (3/2)·2·Π_{p≥5}(1−p^{-2})/(1−(3/p)/p) = (9/2)·log(2+√3)/(√3·ζ(2)) = 2.0800572…,
  I_∞ = (1/(6√6))∫_0^{π/2} dθ/(4 + (17/(3√2)) sin θ) = (1/(2√3)) log(3/(2√2)) = 0.0170005…, C_0 = 0.0353620478…,
  and Borovoi's adelic coefficient equals 1.
- **Support**: written proofs, about 650 lines; uses Borovoi 2001 (Thm 1.4.1, Prop. 1.5.1), Gorodnik–Oh–Shah 2009
  Thm 1.6, Voight's book for Hilbert symbols. Workbench: VERIFIED (S6-KOIDE-DEFECT-COUNTING).
- **What it adds**: nothing over [AC26] or [E26] (unrelated to them). Over the literature: an explicit worked case
  of the Borovoi–Rudnick / DRS / Eskin–McMullen theory; not searched for this particular form; no novelty in method.
- **First assessment**: solid. My checks: brute-force N_{2,k} = 384, 1536, 6144 (k = 4,5,6) = 3·2^{2k−1};
  N_{3,k} = 18, 162, 1458 = 2·3^{2k}; N_{p,1} = p² + (3/p)p for p = 5,7,11,13; g^TAg = A, det g = 1; numerical
  quadrature of I_∞ agrees to 13 digits; (−17,3)_2 = −1. Census: R(10^8)/10^8 = 0.03536002 against C_0 = 0.0353620478,
  difference −202.78 (relative −5.7·10^{-5}, 0.02·√X). This confirms the structure (c = 1, not 0 or 2; the Euler
  product; the sector). It does not separate C_0 from the packet's earlier guess 1/(9π) = 0.0353677651 (relative
  difference 1.6·10^{-4}: at 10^8 that guess gives a residual −775, inside the observed range of fluctuations
  [−813, +722]); so the fine value of the constant rests on the proof, as the workbench says. An independent
  consistency check of mine: C_0 = λ_0·c with λ_0 = log(3/(2√2))/log(2+√3) and c = (9/(2π²))·log²(2+√3) = 0.790782,
  where c should be the mean value of ρ(18z²−2) (see D2-9); observed mean for z ≤ 10^7: 0.7907565.
- **A full check must establish**: Borovoi's normalization (convergence factors, the sign ν and the density 1+ν)
  as used; that the spinor-norm argument at 2 is the right orbit invariant (stabilizer torus of Q_2(√3)); the GOS
  cone hypotheses for a one-sheeted hyperboloid; conditional convergence order of the Euler product.
- **Deserves a full check**: no — routine, numerically consistent, and of no S6 relevance. **Interest**: 2.

### D2-2
- **Title**: Vieta reduction: the positive solutions of Δ = −1 form a rooted forest; exact integral coordinates; Pell
  faces. **Type**: new proof or restatement of a known kind of result (elementary; computation).
- **Where**: `koide_counting_repair.tex` l. 35–394 (Props vieta-reflections, vieta-reduction, vieta-forest, Thm
  coordinate-bijection, Prop. pell-faces).
- **Statement**: s_i(u) = u − 2B_K(u,e_i)/B_K(e_i,e_i)·e_i are integral reflections of (Z³, Δ), e.g.
  s_3(x,y,z) = (x,y,4x+4y−z). For 0<x≤y≤z with Δ = −1: z < 4(x+y) ⟹ 0 < z' < y; z ≥ 4(x+y) ⟹ z' ≤ 0. Every positive
  solution has a unique reduced representative (z ≥ 4(x+y)); the graph of positive Vieta moves is a forest with one
  root per component. (x,y,z) ↦ (a,q,n) = (x+y−4n, y−x, z−4(x+y)) is a bijection of reduced roots onto the chamber
  𝓣, with 2Δ = a²−3q²−18n², z = 4a+17n. Face n = 0: (a_k,q_k) from (1+√3)(2+√3)^k, k ≥ 1, first root (1,4,20);
  face q = 0: (A_k,N_k) from (4+√18)(17+4√18)^k, first root (4,4,33).
- **Support**: complete short proofs. Workbench VERIFIED.
- **What it adds**: unrelated to [AC26], [E26]. Literature: the pattern is that of root quadruples of Apollonian
  packings (Graham–Lagarias–Mallows–Wilks–Yan) and of Markoff-type descents, here for a ternary form, where the
  "Vieta group" ⟨s_1,s_2,s_3⟩ is a reflection group with three pairwise ultraparallel mirrors at distance
  arccosh 2 = log(2+√3) (infinite covolume), so there are infinitely many trees and R(X) counts roots. Not searched
  for this specific form.
- **First assessment**: correct (I reproduced the first roots (1,4,20), (4,4,33), (4,8,49), (4,15,76), (8,24,129),
  (16,17,136) by brute force and the polynomial identities on random integers). A simpler coordinate system exists:
  s = x+y+4z, t = y−x gives 2Δ = s² − 3t² − 18z², the same form with the height as a coordinate (see D2-9); the
  workbench's (a,q,n) is this composed with the automorph (a,n) ↦ (17a+72n, 4a+17n) of a² − 18n².
- **A full check must establish**: nothing beyond reading the proofs.
- **Deserves a full check**: no. **Interest**: 1–2.

### D2-3
- **Title**: Exact parametrization of the counted points by ideals of Z[√3] and unit powers; sharp floor formula;
  Hecke-phase splitting of the discrepancy. **Type**: computation / restatement (standard ideal theory).
- **Where**: `koide_exact_parametrization.tex` l. 165–842 (Prop. HNF-ideals, Lemma integral-seed-descent, Thm
  integral-parametrization, Prop. orbit-divisor, Thm exact-floor, eqs. exact-discrepancy-splitting, Fejer-exact,
  shifted-Hecke-factorization, exact-shifted-Hecke-correlation); 4 Sep 2026.
- **Statement**: for n ≥ 1, m_n = 18n²−2: solutions (a,q) of a²−3q² = m_n with a>0, q≥0 are α_{n,𝔭}ε^k, k ≥ 0,
  𝔭 = (C,D,E) running over C²D = m_n, 0≤E<D, E² ≡ 3 (D), α the generator with seed condition a > 2q ≥ 0; each point
  once; number of orbits ρ(m_n) = ρ(3n−1)ρ(3n+1), ρ = 1*χ_12. With τ = log(α/√m_n)/log ε, Y_n = (X−17n)/4,
  L_n(X) = log((Y_n + √(Y_n²−m_n))/√m_n)/log ε: R(X) = R_0(X) + Σ_{n: Y_n ≥ √m_n} Σ_𝔭 (⌊L_n(X) − τ⌋ + 1), and
  R(X) − C_0X = R_0(X) + [Σ_n ρ(m_n)L_n(X) − C_0X] + Σ_n Δ_n(λ_n(X)), with the phase discrepancy expanded in
  S_ℓ(18n²−2) = (−1)^ℓ S_ℓ(3n−1)S_ℓ(3n+1), S_ℓ(m) = Σ_{N𝔞=m} ξ_ℓ(𝔞), ξ_ℓ((γ)) = exp(πiℓ·log|γ/γ'|/log ε).
- **Support**: complete proofs; finite replay n ≤ 200; used by the census (2,943,725 values of n, each checked
  against ρ(3n−1)ρ(3n+1)). Workbench VERIFIED.
- **What it adds**: nothing for S6. Literature: textbook (ideals of a real quadratic field with h = 1, Hecke
  Grössencharaktere, Maass's theta series); not searched.
- **First assessment**: correct on reading (I checked the floor identity, the splitting, ξ_ℓ at the primes over 2
  and 3, the Fejér coefficients). It is more complicated than necessary: it slices by n, so the angular window
  λ_n(X) moves with n and X. Slicing by the height z (D2-9) gives a fixed window [0, λ_0] and a plain sharp cutoff
  z ≤ X: R(X) = R_0(X) − 1 + Σ_{z≤X} #{𝔞: N𝔞 = 18z²−2, τ(𝔞) ∈ [0,λ_0]}.
- **A full check must establish**: nothing beyond reading.
- **Deserves a full check**: no. **Interest**: 2.

### D2-4
- **Title**: Power saving R(X) = C_0X + O(X^{1−η}), η > 0 unspecified. **Type**: application of a known theorem.
- **Where**: `koide_exact_parametrization.tex`, Lemma `koide-param-lem:volume` (l. 899–1022), Thm
  `koide-param-thm:power-saving` (l. 1024–1094); duplicated in `koide_effective_literature_audit.tex` l. 349–474.
- **Statement**: m_∞(B_X) = I_∞X + O(1); the family B_X (five linear walls and 4a+17n ≤ X on F = −2) is effectively
  well-rounded (Benoist–Oh 2012, Def. 13.1, boundary exponent κ = 1); F is Q-anisotropic (mod-3 descent); hence by
  Benoist–Oh Thm 13.2 applied to each of the finitely many G_Z-orbits, R(X) = C_0X + O(X^{1−η}).
- **Support**: a 120-line verification of Def. 13.1(2),(3) and the standing hypotheses. Workbench VERIFIED.
- **What it adds**: nothing for S6; for the literature it is a routine instance. The same qualitative saving also
  follows from Parkkonen–Paulin's counting of common perpendiculars with error term (arXiv, ETDS 2017) once D2-9 is
  accepted. Not searched further.
- **First assessment**: plausible; I did not open Benoist–Oh to compare Def. 13.1 word for word. The verification
  argument (linear functionals move by O(δ‖x‖) under a δ-ball of G; measure da·dθ/(6√6)) is sound.
- **A full check must establish**: the exact wording of Benoist–Oh Def. 13.1 and Thm 13.2 (group-action
  thickenings B^±; the integrability condition); that their Thm 13.2 covers S = {∞} and a non-maximal lattice.
- **Deserves a full check**: no — superseded in interest by an explicit exponent (D2-9). **Interest**: 2.

### D2-5
- **Title**: Quaternionic form of the shell: trace-4, norm-1 elements of an order of reduced discriminant 108 in the
  quaternion algebra of discriminant 6. **Type**: new proof or restatement of a known result (standard dictionary),
  with one misleading comparison.
- **Where**: `koide_quaternion_bridge.tex` (all), 4 Sep 2026.
- **Statement**: B = (18,−6)_Q is the indefinite division algebra ramified at {2,3}; 𝒪 = Z⟨1, (I+J)/2, (I−J)/2,
  K/2⟩ is an order with discrd 108 (trace-form determinant −108²), index 18 in a maximal order, not Eichler;
  (a,q,n) ↦ γ = 2 + (qI+aJ+nK)/2 is a bijection {F = −2} → {γ ∈ 𝒪: trd γ = 4, nrd γ = 1}; γ² − 4γ + 1 = 0;
  𝒪 ∩ Q(γ) = Z[γ−2] ≅ Z[√3] (optimal embeddings of Z[√3]); C_{𝒪^1}(γ) = {±γ^k}; primitive hyperbolic, length
  2 log(2+√3); finitely many 𝒪^1-conjugacy classes; 𝒪^1 ⊇ 𝓜^1(18𝓜) is a congruence cocompact Fuchsian group;
  ‖ρ(γ)‖_F² = 14 + (7a + 15√2 n)²/4 in the chosen real splitting.
- **Support**: displayed algebra; finite replay; Voight's book. Workbench VERIFIED.
- **What it adds**: nothing for S6. For the counting problem it supplies the lattice Γ = 𝒪^1 and the fact that it
  is a congruence group (so Kim–Sarnak applies). Literature: standard (ternary form ↔ quaternion order).
- **First assessment**: the algebra is right (my check: det ρ(γ) = 1 and the Frobenius identity at shell points
  (5,3,0), (4,0,1), (1,1,0); trd is always even on 𝒪, so 𝒪^1/±1 is torsion-free). The comparison drawn from it is
  off target: the "radial Huber height 7a+15√2 n" is the distance to the base point i of an arbitrarily chosen
  splitting (another splitting or base point gives another linear form with a timelike dual vector), and it is then
  observed that it differs from 4a+17n. The height 4a+17n is dual to a spacelike rational vector
  (w' = (72,0,−17), F(w') = −18, 4a+17n = ⟨v,w'⟩/18), so the right companion problem is geodesic-to-geodesic
  (double cosets by two hyperbolic subgroups), not geodesic-to-point (conjugacy classes). See D2-9 and §3.
- **A full check must establish**: the multiplication table; the local structure of 𝒪 at 2 and 3; h and class
  representatives (not computed in the workbench).
- **Deserves a full check**: maybe — only as input to D2-9. **Interest**: 2.

### D2-6
- **Title**: Exact census R(10^8) = 3,536,002 with certified extrema of E(X) = R(X) − C_0X. **Type**: computation.
- **Where**: `koide_exact_census.tex`; evidence `W\evidence\koide_exact_checkpoint_20260904\census\`; 4 Sep 2026.
- **Statement**: R(10^8) = 3,536,002; checkpoints R(2·10^5) = 7,109, R(10^6) = 35,381, R(2·10^6) = 70,637,
  R(5·10^6) = 176,943, R(10^7) = 353,598, R(2·10^7) = 707,458, R(5·10^7) = 1,768,230; max E = +721.79 at
  77,078,404; min E = −812.83 at 32,461,294; max |E|/√X = 0.17140 on [10^4,10^8] at 867,240; |E| ≤ 0.172√X there;
  12,916 sign changes.
- **Support**: exact-integer enumeration via ideals, independent replay of all rows, literal scan to 2·10^4.
  Workbench VERIFIED (S6-KOIDE-CENSUS-1E8).
- **What it adds**: data for the open problem; no S6 content.
- **First assessment**: confirmed up to 10^7 by my own program (`scratch\D2\recount.c`: for each z ≤ X loop over
  s ∈ (√(18z²−2), 17z/4], test (s² − 18z² + 2)/3 = t², x = (s−4z−t)/2 > 0, recheck Δ = −1): R = 353 (10^4),
  715 (2·10^4), 3,535 (10^5), 7,109 (2·10^5), 17,695 (5·10^5), 35,381 (10^6), 70,637 (2·10^6), 176,943 (5·10^6),
  353,598 (10^7); max |E|/√X on [10^4,10^7] = 0.1714002 at X = 867,240 with R = 30,827. All equal to the workbench
  values. Further statistics from my data: rms of E over [5·10^6,10^7] is 140 = 0.051·√X; over [10^5,2·10^5] it is
  0.062·√X; so E/√X shows no growth over three decades. Splitting E into the "full-period" part
  λ_0·(Σ_{z≤X}ρ(18z²−2) − cX) and the angular part R(X) − λ_0Σρ: at the top dyadic block the angular part has rms
  0.059·√X and the full-period part λ_0·0.29·√X = 0.013·√X; the angular (arc) part dominates.
- **A full check must establish**: nothing more is needed below 10^7; 10^7–10^8 rests on the workbench's two passes.
- **Deserves a full check**: no. **Interest**: 2.

### D2-7
- **Title**: Literature audit for effective counting on the fixed sector (which theorems apply, with exponents).
  **Type**: expository only.
- **Where**: `koide_effective_literature_audit.tex`; 4 Sep 2026.
- **Statement**: (i) GOS 2009 Thm 1.6 gives C_0X + o(X); (ii) Benoist–Oh Thm 13.2 gives O(X^{1−η}); (iii) Good /
  Chatzakos–Petridis: sharp radial conjugacy-class count O(X^{2/3}) after subtracting the X^{s_j} terms; (iv)
  Liu–Sarnak Prop. 3.2: smooth radial O(X^{1/2+θ+ε}), θ = 7/64, applicable class by class to 𝒪^1; (v) Gorodnik–Nevo:
  19/20 (tempered) or 39/40; (vi) split-stabilizer papers (Oh–Shah, Xu–Zhang, Huang, Zhang) are a different regime
  because 108 is not a square; (vii) mean-square and Ω results (Chatzakos, Voskou, Lekkas–Petridis) are not pointwise.
- **Support**: locators into each source; admits Good's book was not consulted.
- **What it adds**: a usable map of the literature. Not mathematics.
- **First assessment**: careful and mostly right, but it files the closest theorem in the wrong row: Voskou's and
  Lekkas–Petridis's closed-geodesic double-coset counts are listed as "current sharp comparator, not the target",
  and the two "independent missing inputs" are said to be a sharp nonradial height and control of exceptional
  spectrum. With D2-9 the height is exactly their height; what is missing is only the restriction to an arc.
  The exceptional-spectrum worry is void at the 2/3 level (Kim–Sarnak: s_j ≤ 39/64 < 2/3) and probably void
  altogether (Booker–Lee–Strömbergsson 2020, arXiv:1803.06016: Selberg's conjecture holds for Γ_1(N), N ≤ 880, and
  Γ(N), N ≤ 226; the Jacquet–Langlands transfers for an order of reduced discriminant 108 = 2²·3³ should have
  twist-minimal conductor dividing 108 — to be checked locally at 2 and 3). I could not verify "Lekkas–Petridis,
  version dated 24 August 2026"; arXiv shows v1 of 16 Sep 2025 with the same theorem numbers (Thm 1.2, Thm 1.5,
  Conj. 1.6), which I confirmed by fetching the HTML.
- **A full check must establish**: n/a.
- **Deserves a full check**: no. **Interest**: 2.

### D2-8
- **Title**: Open problem S6-OPEN-KOIDE-SQRT-DISCREPANCY, restated as a clean self-contained problem.
  **Type**: open question isolated.
- **Where**: `koide_counting_repair.tex`, `koide-count-open-square-root-discrepancy` (l. 1133–1153); ledger line 9;
  `uncertainties.txt` U-KOIDE-SQRT-DISCREPANCY; discussion in `koide_exact_parametrization.tex` l. 1096–1149,
  `koide_quaternion_bridge.tex` l. 677–742, `koide_effective_literature_audit.tex`.
- **Statement** (workbench): R(X) − C_0X = O_ε(X^{1/2+ε}) for every ε > 0?
  **Statement** (self-contained, equivalent; the form I recommend for a prompt):

  > Let ε_0 = 2+√3 and let χ be the primitive real character mod 12 (χ(±1) = 1, χ(±5) = −1), ρ(m) = Σ_{d|m} χ(d)
  > = number of ideals of norm m in Z[√3] (class number one, all units ±ε_0^k of norm +1).
  > For z ≥ 1 put m_z = 18z² − 2 = 2(3z−1)(3z+1). Define
  > R(X) = #{(s,t,z) ∈ Z³ : s² − 3t² = 18z² − 2, 1 ≤ z ≤ X, t ≥ 0, t + 4z < s ≤ 17z/4}.
  > (Equivalently, with x = (s−4z−t)/2, y = (s−4z+t)/2: R(X) = #{(x,y,z) ∈ Z³: 4(xy+xz+yz) − x² − y² − z² = −1,
  > 0 < x ≤ y, 4(x+y) ≤ z ≤ X}. Equivalently, with a = 17s − 72z, q = t, n = 17z − 4s: the count of
  > a² − 3q² − 18n² = −2, a > 0, q ≥ 0, n ≥ 0, a + 4n > q, 4a + 17n ≤ X.)
  > Each ideal 𝔞 of norm m > 0 with m ≡ 1 mod 3 has a unique generator α = s + t√3 with √m ≤ α < ε_0√m; put
  > θ(𝔞) = log(α/√m)/log ε_0 ∈ [0,1). Then, with λ_0 = log(3/(2√2))/log(2+√3) = 0.0447178…,
  > R(X) = Σ_{1≤z≤X} #{𝔞 ⊂ Z[√3] : N𝔞 = 18z² − 2, 0 ≤ θ(𝔞) ≤ λ_0} + R_0(X) − 1   (X ≥ 1),
  > where R_0(X) = #{k ≥ 1 : 4a_k ≤ X}, a_k + q_k√3 = (1+√3)(2+√3)^k, is O(log X), and the −1 removes the ideal (4)
  > of norm 16 at z = 1 (the point (s,t,z) = (4,0,1), i.e. (x,y,z) = (0,0,1), which fails t + 4z < s).
  > Known: R(X) = C_0X + O(X^{1−η}) for some η > 0, C_0 = (9/(2π²))·log(2+√3)·log(3/(2√2)) = 0.03536204780…;
  > Σ_{z≤X} ρ(18z²−2) has mean value c = (9/(2π²))·log²(2+√3) = 0.790782…, and C_0 = λ_0·c.
  > Exact data: R(10^6) = 35,381; R(10^7) = 353,598; R(10^8) = 3,536,002; |R(X) − C_0X| ≤ 0.172·√X for
  > 10^4 ≤ X ≤ 10^8, with extreme values −812.83 at X = 32,461,294 and +721.79 at X = 77,078,404.
  > Problem: is R(X) − C_0X = O_ε(X^{1/2+ε})?
  > Geometric form: Γ = SO(F,Z)-lattice of F = s² − 3t² − 18z² (cocompact, arithmetic, from the quaternion algebra of
  > discriminant 6); integer points v with F(v) = −2 are the Γ-translates of finitely many closed geodesics of
  > Γ\H; z(v) = (1/3)·cosh d(g_v, g_0), g_0 the closed geodesic dual to e_z = (0,0,1) (F(e_z) = −18; its stabilizer
  > contains T: (s,t) ↦ (2s+3t, s+2t)); θ is the position of the foot of the common perpendicular on g_0. So R(X)
  > counts common perpendiculars of length ≤ arccosh(3X) from g_0 to the translates, with foot in a fixed arc of
  > proportion λ_0 of g_0.
  > Fourier form: with S_ℓ(m) = Σ_{N𝔞=m} e^{2πiℓθ(𝔞)} (coefficients of Maass's theta series of level 12 and
  > spectral parameter πℓ/log ε_0), S_ℓ(18z²−2) = (−1)^ℓ S_ℓ(3z−1)S_ℓ(3z+1), so
  > R(X) − R_0(X) + 1 = λ_0 Σ_{z≤X} ρ(3z−1)ρ(3z+1) + Σ_{ℓ≠0} c_ℓ (−1)^ℓ Σ_{z≤X} S_ℓ(3z−1)S_ℓ(3z+1) + (endpoint terms at θ = 0),
  > c_ℓ = (1 − e^{−2πiℓλ_0})/(2πiℓ) (Fejér-summed): a family of sharp-cutoff shifted convolution sums.

- **Support**: the workbench has the n-sliced version (D2-3). The z-sliced statement above is mine; it follows from
  2Δ = (x+y+4z)² − 3(y−x)² − 18z² and D2-3's ideal bijection (derivation and boundary cases in D2-9). Numerically
  checked: the count in the (s,t,z) form is what my program computes, and it equals the workbench's R(X) up to 10^7;
  the mean of ρ(18z²−2) for z ≤ 10^7 is 0.7907565 against c = 0.7907816.
- **What it adds**: over [AC26], [E26]: nothing (unrelated). Over the literature: it is an instance of two classical
  open problems with the same barrier. (a) Hyperbolic lattice-point problems: for all nine double-coset types
  (point/geodesic/cusp) the best pointwise error is O(X^{2/3}) (Selberg; Good 1983 Thm 4; re-proved for
  geodesic–geodesic by Voskou arXiv:2407.03134 and Lekkas–Petridis arXiv:2509.12902 Thm 1.2, who state that 2/3
  "has not been improved" in any case); square root is conjectured (Chatzakos–Petridis Conj. 5.7; Voskou Conj. 1;
  Lekkas–Petridis Conj. 1.6) and proved only in mean square (Lekkas–Petridis Thm 1.5:
  (1/X)∫_X^{2X}|E|² ≪ X log²X). (b) The ℓ = 0 term is the Q(√3) analogue of the binary additive divisor problem
  Σ d(n)d(n+h), where the best exponent is also 2/3 (Deshouillers–Iwaniec, Motohashi) and 1/2 is conjectured.
  Searched: arXiv listings for Lekkas–Petridis, Voskou, Good; Templier, Templier–Tsimerman (sums of GL(2)
  coefficients over quadratic polynomials); Hooley/Bykovskii-type divisor sums over quadratic polynomials. Found no
  treatment of an arc-restricted (sectorial) geodesic–geodesic count with an explicit exponent.
- **First assessment**: square-root cancellation is plausible (standard conjecture; census: E/√X bounded by 0.172,
  rms about 0.05–0.06, sign changes frequent). A proof would need what nobody has: cancellation in
  Σ_j X^{it_j}·(period of u_j on g_0, twisted by e^{2πiℓ·})·(period of u_j on g_v)·t_j^{-1/2} beyond the local Weyl
  law, uniformly in ℓ; i.e. breaking the 2/3 barrier. The item should not go to a stronger model as "prove the
  square-root bound". Realistic targets, in order: (T1) an explicit exponent: R(X) = C_0X + O(X^{θ}) with θ < 1
  explicit, aiming at 2/3 + ε (Good's method or the Lekkas–Petridis relative trace formula with twisted periods;
  needs uniformity in the angular mode ℓ, or direct two-variable smoothing of the arc and the radius; exceptional
  spectrum is harmless below 2/3 by Kim–Sarnak); (T2) the full-period corollary
  Σ_{z≤X} ρ(3z−1)ρ(3z+1) = (9/(2π²))·log²(2+√3)·X + O(X^{2/3}) as a direct consequence of Good / Lekkas–Petridis
  (needs only orbit bookkeeping); (T3) a mean-square bound ∫_X^{2X}|R(x) − C_0x|²dx ≪ X^{2+ε} (via the
  Lekkas–Voskou large sieve for periods); (T4) an Ω-result R(X) − C_0X = Ω(X^{1/2}); (T5) absence of exceptional
  eigenvalues for this lattice via Booker–Lee–Strömbergsson.
- **A full check must establish**: the equivalence of the three coordinate forms and the fixed-arc formula
  (boundary cases: the point (s,t,z) = (17,1,4), the Pell families); the identification of z with cosh d; that the
  literature statements are quoted correctly (Good's Thm 4 from the book itself).
- **Deserves a full check**: yes — only the restatement (cheap) before it is used in a prompt; the conjecture itself
  is not checkable. **Interest**: 3 (as an open problem it is a special case of a known conjecture, not a new one).

### D2-9
- **Title**: (Found during this survey, not in the workbench.) The Koide height is a geodesic-to-geodesic distance:
  R(X) is an arc-restricted count of common perpendiculars between closed geodesics, and
  R(X) = R_0(X) − 1 + Σ_{z≤X} #{𝔞: N𝔞 = 18z²−2, θ(𝔞) ∈ [0,λ_0]}. **Type**: new way of stating a known result /
  refinement of the workbench's reduction; a correction of the workbench's positioning of the problem.
- **Where**: not in the files. Contradicts the emphasis of `koide_quaternion_bridge.tex` l. 625–675, 705, 739
  ("the radial Huber height 7a+15√2 n … is a different linear height … their symmetric difference can have
  main-order size"; item 9 "missing … transfer between the two exact heights") and of
  `koide_effective_literature_audit.tex` l. 90, 506–517, 345–346.
- **Statement**: (1) 2Δ(x,y,z) = s² − 3t² − 18z² with s = x+y+4z, t = y−x (one line: 2Δ = p² − 3t² + 8pz − 2z²,
  p = x+y). In the workbench's coordinates s = 17a+72n, t = q, z = 4a+17n: the composite with the automorph
  17+4√18 of a² − 18n². (2) The reduced-root conditions 0 < x ≤ y, z ≥ 4(x+y) become t ≥ 0, s − 4z > t,
  s ≤ 17z/4. The only solutions with t ≥ 0, 0 < s ≤ 17z/4 violating s − 4z > t are (s,t,z) = (4,0,1) and
  (17,1,4), i.e. (x,y,z) = (0,0,1) and (0,1,4) (brute force for z ≤ 30,000; for z ≥ 10 a violation is impossible
  because it forces t ≥ (2−√3)z − 1 while s ≤ 17z/4 forces 48t² ≤ z² + 32). (3) For fixed z, the solutions (s,t), s>0, of
  s² − 3t² = m_z modulo ε_0 are the ρ(m_z) ideals; s ≤ 17z/4 ⟺ θ(𝔞) ≤ λ_z with cosh(λ_z log ε_0) = 17z/(4√m_z);
  λ_z ↓ λ_0, cosh(λ_0 log ε_0) = 17/(12√2), λ_0 log ε_0 = log(3/(2√2)); the points with λ_0 < θ ≤ λ_z are exactly
  those with 4s = 17z (the n = 0 Pell face, which contains (17,1,4)); no ideal has θ = λ_0 exactly (it would need
  9z² − 1 to be a square). Hence R(X) = R_0(X) − 1 + Σ_{z≤X} A_z with A_z = #{𝔞: N𝔞 = 18z²−2, θ(𝔞) ≤ λ_0}; checked
  height by height for z ≤ 30,000 (`scratch\D2\arccheck.py`, exact integers: θ ≤ λ_0 ⟺ 288s² ≤ 289(18z²−2)).
  (4) The linear form z is dual to the spacelike vector e_z (F(e_z) = −18; in (a,q,n) coordinates w' = (72,0,−17));
  its stabilizer in SO(F,Z) contains the integral hyperbolic element T(a,q,n) = (290a+51q+1224n, 17a+2q+72n,
  −68a−12q−287n), so the dual geodesic g_0 is closed on Γ\H, and for F(v) = −2: |⟨v,e_z⟩|/√(F(v)F(e_z)) = 18z/6 = 3z
  = cosh d(g_v, g_0) (when ≥ 1). (5) Hence C_0 = λ_0·c, c = (9/(2π²))·log²(2+√3) = mean value of ρ(18z²−2), and the
  unrestricted count Σ_{z≤X} ρ(18z²−2) is literally the Good / Lekkas–Petridis double-coset count H_0\Γ/H_v
  (summed over the finitely many classes of v), so it has error O(X^{2/3}) by their theorem; the main term
  log²(2+√3)/π² has the shape ℓ(g_0)·ℓ(g_v)/vol of the classical common-perpendicular asymptotic.
- **Support**: my derivation (above; each step is two lines). Scripts: `checks.py` verifies the identities on random
  integers, F(72,0,−17) = −18, and that T is an integral isometry fixing w' and the height; `analyze.py`: mean of
  ρ(3z−1)ρ(3z+1) over z ≤ 10^7 is 0.7907565 (prediction 0.7907816; the difference −251 is 0.08·√X);
  cnt[z] ≤ ρ(m_z) for every z ≤ 10^7; the recount in these coordinates equals the workbench's R(X).
- **What it adds**: over the workbench: removes "nonradial height" from the list of obstructions, replaces the
  n-sliced floor formula by a fixed-window formula, identifies the right theorem in the literature (so 2/3 is within
  reach where the workbench has only an unspecified η), and gives the corollary on Σρ(3z−1)ρ(3z+1). Over the
  literature: nothing new in principle (it is the standard dictionary); the arc-restricted version with an explicit
  exponent I did not find (searched as in D2-8). Lekkas–Petridis (HTML v1) count the aggregate only and say that
  Good split the problem by signs; Parkkonen–Paulin give equidistribution of the feet with an unspecified error
  term.
- **First assessment**: steps (1)–(4) are solid (checked by script). Step (5) needs bookkeeping I did not do: which
  lattice (SO(F,Z) against Ad(𝒪^1): T has adjoint eigenvalue ε_0, the elements γ of 𝒪^1 have ε_0², so T itself is
  not in Ad(𝒪^1)), the number h of classes, orientation and sign cases (Good's four subcases), whether Lekkas–
  Petridis's standing assumptions (cocompact, torsion-free, "no elements with zeros on the diagonal") hold or can be
  arranged, and a cross-check of c against their main term (2/π)·ℓ_1ℓ_2/vol·X. The claim "O(X^{2/3}) for the
  arc-restricted R(X)" is not proved by anyone; it is a target (T1 of D2-8).
- **A full check must establish**: (1)–(4) by hand; the orbit and orientation bookkeeping in (5) and the equality
  of main terms; the local type of 𝒪 at 2, 3 and the conductor bound for the Booker–Lee–Strömbergsson argument.
- **Deserves a full check**: yes — it is cheap and it changes what should be asked of a stronger model.
  **Interest**: 3.

### D2-10
- **Title**: Koide cone ≅ zero locus of the real period determinant; phase-sector description of the Koide cone.
  **Type**: expository only.
- **Where**: `koide_period_discriminant.tex` (Thm koide-s6-thm-ambient-discriminant, two corollaries);
  `koide_arithmetic_preprint.tex` §1 (Thm orthogonal-model, Cor. exact-phase-sector, Prop. S6-dictionary,
  Cor. rank-one-square, Remark on the radial cusp).
- **Statement**: Q_K = h² − x² − y² = det(h+y x; x h−y); under (t,m,ϱ) = (h+y, x/√6, h−y): det P = tϱ − 6m² = Q_K;
  nonnegative Koide triples ↔ θ in three arcs of length π/6, endpoint ratios 2±√3; on the actual cusp
  det P_T = −D_T, D_T = T² + (2H−B)T + H(H−B) + 6m² + O(Te^{−2πT}).
- **Support**: elementary proofs. Workbench VERIFIED, with the explicit non-claim.
- **What it adds**: nothing; a real-linear coincidence of signatures. Over [AC26]: the formula det P = −det Im Z and
  the cusp asymptotic D_T belong to the cusp files (other readers). Literature: Koide's relation as an angle of 45°
  with (1,1,1) is well known (Foot 1994); not searched further.
- **First assessment**: correct and empty of consequences; see §3 (the forms are not even Q-equivalent).
- **A full check must establish**: nothing.
- **Deserves a full check**: no. **Interest**: 1.

### D2-11
- **Title**: Audit of the "Erdős–Straus / Koide v3" packet: channel bijection for 4/n = 1/a + 1/y + 1/z, density-one
  diagonal family, one refuted positivity claim, a rational map between {ac − b² = −δ} and {Δ = −1}.
  **Type**: grouped small items — restatements of known results, one correction of the Pro packet (not of [AC26] or
  the literature).
- **Where**: `koide_es_v3_audit.tex`; `W\evidence\koide_es_v3_audit_20260904\`; 4 Sep 2026.
- **Statement**: (a) Prop. esv3-channel: for n ≡ 1 (4), R ≡ 3 (4), 0 < R < n, gcd(n,R) = 1, a = (n+R)/4, N = na:
  (δ,u,v) with δ | n², uv = a², R | 4u+δ ↦ (y,z) = ((N + (n²/δ)u)/R, (N + δv)/R) is a bijection onto ordered positive
  solutions; inverse δ = n²/gcd(Ry−N, n²). (b) R_δ = (3 −ℓ_1; 4 −T) with 12ℓ_0 − 4ℓ_1 − 3ℓ_2 = δ and cokernel Z/δ;
  ℓ_1 ≡ −δ (3). (c) Prop. esv3-diagonal/density: for prime p ≡ 1 (4), the solutions with R | (p+1)/2, R ≡ 3 (4)
  number ½(τ(m) − Σ_{d|m}χ_4(d)), m = (p+1)/2; they cover a set of primes of relative density one in each class;
  p = 73 is missed. (d) REFUTED: "A_11 > 0 for every real δ > 0" (counterexample (2,1,1/8)); true for integer δ ≥ 1.
  (e) the orthogonal map 𝔎_δ has no rational image point. (f) Thm esv3-rational-bridge: 𝓑_δ(a,b,c) = (1 + 2K/D,
  2Ka/D, 2Kb/D), D = −1−a²−b²+4a+4b+4ab, K = 1−2a−2b, inverse a = q_2/(q_1−1), b = q_3/(q_1−1), c = (b²−δ)/a;
  denominator |D|/gcd(|D|,|2K|).
- **Support**: short proofs; independent verifier (1430 states through n = 161; 819 certificates for 329 primes
  below 5000; 820 denominator cases). CLAIMS.json: four VERIFIED, one REFUTED.
- **What it adds**: the link to S6 is the expression 12ℓ_0 − 4ℓ_1 − 3ℓ_2 (= the order of π_1 in [AC26] Main Theorem
  (2)): Erdős–Straus data are fed into that linear form. That belongs to the Erdős–Straus reader. (c) is classical
  (the file says so, citing Elsholtz–Tao 2013); (f) is stereographic projection of a quadric.
- **First assessment**: correct as far as read; no result of interest by itself. The remark "gluing admissibility
  3 ∤ ℓ_1 fails exactly when 3 | δ" is the only point of contact with the construction and should be seen by whoever
  reads the Erdős–Straus bridge.
- **A full check must establish**: nothing here; see the Erdős–Straus lane.
- **Deserves a full check**: no. **Interest**: 1.

---

## 3. Doubts and errors

1. **The name and the placement overstate the link.** The lane sits in the S6 claim ledger under ids S6-KOIDE-*, and
   the preprint title speaks of "the Koide quadratic cone as a Lorentzian determinant". Mathematically the lane has
   nothing to do with the threefold: `koide_period_discriminant.tex` is an identification of two real quadratic
   forms of the same signature through a map with a √6 in it. The workbench says this itself (corollaries,
   "nonclaim" fields, research_log Round 28: "no morphism from a regular abelian-surface fibre … is supplied").
   Stronger than what it says: tρ − 6m² is Q-isotropic and Δ is Q-anisotropic, so no rational identification exists
   at all. Nothing in the lane explains the Koide relation either (the preprint says so in its last section).

2. **Misclassified neighbour problem** (`koide_quaternion_bridge.tex` l. 625–742; `koide_effective_literature_audit.tex`
   l. 90, 345–346, 506–517, 605; `koide_exact_parametrization.tex` l. 1129–1149). The files compare R(X) with the
   conjugacy-class (geodesic-to-point, Huber) problem and conclude that the height is "nonradial" and a "transfer
   between the two exact heights" is missing. The base point i is an artefact of the chosen splitting; no base
   point can give 4a+17n because that form is dual to a spacelike vector. The right neighbour is the
   geodesic-to-geodesic problem (Good's hyperbolic–hyperbolic case), for which the height is exactly the Koide
   height (D2-9). Consequently the statement in the ledger entry S6-OPEN-KOIDE-SQRT-DISCREPANCY, field
   `evidence_needed` ("a pointwise sharp-boundary … estimate for the exact five-wall polyhedron and height 4a+17n,
   together with control or elimination of every complementary-spectrum secondary term") describes the difficulty
   wrongly: the height is standard, four of the five walls are either compact, automatic or Pell faces, and what
   remains is one arc restriction. Not an error in a theorem; an error in the diagnosis.

3. **Exceptional spectrum is presented as a live obstruction** (parametrization file l. 1118–1134, quaternion file
   item 6, audit l. 517). For this congruence lattice s_j ≤ 39/64 < 2/3 by Kim–Sarnak (the audit itself establishes
   that Kim–Sarnak applies), so such terms cannot affect any result at the 2/3 level, and they would be absent if
   Selberg's conjecture holds for the relevant small level, which is likely a theorem (Booker–Lee–Strömbergsson,
   N ≤ 880). The files never draw either conclusion.

4. **"VERIFIED" for S6-KOIDE-DEFECT-COUNTING covers heterogeneous things** in one entry: elementary bijections, a
   Tamagawa-measure computation resting on Borovoi's conventions, and two applications of deep theorems (GOS,
   Benoist–Oh) whose hypotheses were checked against page-cited definitions without local copies of the sources
   (the audit's own limitation section says so). The numerics support the main term only to about 10^{-4} relative
   (they do not distinguish C_0 from 1/(9π), which the source packet used). I found no mistake.

5. **The coordinates (a,q,n) and the n-slicing are a detour.** The form a²−3q²−18n² with height 4a+17n is the form
   s²−3t²−18z² with height z after an automorph. The floor formula, the "Hecke-phase discrepancy splitting" with
   moving windows λ_n(X) and weights L_n(X), and the remark that "L_n has a square-root singularity at the
   endpoint" are artefacts of slicing transversally to the height. Not wrong, but the "exact obstruction" section
   reads as harder than the problem is.

6. **Source not consulted**: Good's 1983 book (the central reference) was only seen through Chatzakos–Petridis; the
   audit says so. Whether Good's Theorem 4 already contains the Fourier modes along the geodesics (I believe his
   general theorem does) decides how much of target T1 is already in print. To be checked from the book.

7. **Version claim I could not confirm**: "Lekkas–Petridis arXiv:2509.12902, version dated 24 August 2026". I saw v1
   (16 Sep 2025) only; theorem numbers agree.

8. **Minor**: the quaternion file is a converted Markdown report (no theorem environments), and opens with "The
   proposed quaternionic realization is correct" — it is an audit of a proposal from the Pro session, kept in that
   voice. The preprint's abstract and status paragraph still treat the S6 construction as "proposed"; that wording
   is dated (pre-[E26]).

9. Nothing in the lane corrects or refines [AC26] or [E26].

---

## 4. Not read

- `W\evidence\koide_exact_checkpoint_20260904\census\final_100000000\koide_roots_through_100000000.csv.gz` (76 MB)
  and `koide_discrepancy_100000000.json` (3.6 MB): not opened, as instructed.
- `koide_fast_enum.py` (40 KB), `validate_fast_enum.py`, `audit_coordinate_file.py`,
  `supplemental_candidate_analysis.py`: only the function list and the method record (first 300 lines of
  METHOD_AND_RESULTS.md) were read; I replaced a code review by an independent recount to 10^7.
- `verify_quaternion_bridge.py`, `verify_independent.py`, `record_intake.py`, the JSON receipts: only logs/heads.
- `W\evidence\koide_es_v3_audit_20260904\source\` (the Pro packet: `koide_es_extension_v3.tex`, 58 KB, PDF,
  background\, source_extract\): not read; outside the arithmetic lane proper.
- `W\WEB_PRO_MODE_FEEDBACK.md`: only the Koide passages (l. 2040–2220).
- Benoist–Oh 2012, Gorodnik–Oh–Shah 2009, Borovoi 2001, Good 1983: not opened; Lekkas–Petridis read through a
  fetched summary of the arXiv HTML (first 100,000 characters).
- The Erdős–Straus bridge files listed in 1.11.
