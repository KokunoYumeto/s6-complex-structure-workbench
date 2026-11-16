# S6_07_PAPER notation sheet

The paper follows FAM conventions. This sheet distinguishes global symbols, local chart variables, source equation tags, and retained statement labels. A scoped local variable does not change a global parameter. Mathematical signs are unchanged except where the supplied source explicitly converts conventions.

# Root notation and labels

FAM conventions are unchanged: rho=exp(pi i/3); clockwise root deck generators, positive base meridians, Pi_c and w=exp(-pi i c). P_E is renamed P_mark in statements and proofs. Dual covectors u,w appearing in linear combinations and their coefficient comparisons are u_Lambda,w_Lambda; hatted homology vectors retain their names. The shorthand macro for hatted delta is dhat, avoiding the standard T1 command dh. The modular nome is q_tau and the modular discriminant is Delta_mod, agreeing with the periods section; finite discs Delta_j, vector q_n and the auxiliary division-model discriminant keep their distinct meanings.

Scoped renamings avoid collisions with the global parameters u=w^2 and w. In FAM A.1.1 the square root of E_6 is h_6, and the two canonical-ring sections u,v are s_can,t_can (the abstract polynomial generators U,V are unchanged). In FAM A.3.1 the preliminary first-coordinate lift is h_loc. In FAM A.4.2 the moving torus coordinate w is zeta^new and its projector P is P_KS. In FAM B.1.1, B.1.2 and B.1.4 the line-bundle fibre coordinate W is v, exactly as in the first-run conventions; it is distinct from the cusp fibre W. The reciprocal cusp coordinate v=1/t is r_cusp, including the differential in B.1.3. The B.1.3 blow-up parameter u=t-1 is v_t, agreeing with the duplication section. The holomorphic torus-valued unit u(t_c) of B.2.1 is v_unit(t_c). These edits change symbols only, never hypotheses or algebraic identities.

Workbench mathscr V → mathcal V; its homogeneous line mathcal L → mathcal L_per; its local logarithms w_j → ell_j^log; its finite base-change variable u → s_new; its local equivariant first-component function u(z) → h_loc(z). The covector coefficient comparison uses u_Lambda,w_Lambda consistently. Both u replacements are confined to the source paragraphs defining those local variables; the global Engel parameter is unchanged. No sign is changed. Its missing labels ffcert:thm:normalization, prop:period-input-audit and thm:canonical-ring-recovery are mapped respectively to FAM A.1.2, A.3.1 and A.1.1, whose displayed calculations have been matched.

Every retained FAM st:ID label becomes fam:ID. The workbench pshift labels are retained. The companion universal map-factorization statement comes from DGKXv1 thm:all-maps-factor; it is not part of the supplied FAM A.1.1 statement. DGKX a → c and cA → mathcal P. PUSH E.1.1 and E.1.2 are printed as announcements as mandated, with their statement bodies retained.


# Periods and maximum: notation concordance

These are literal notation changes in statements and proofs. No change is made to a parameter range, quantifier, equality, inequality or equality locus. Source equation labels receive the namespace `fam:`, `ari:` or `push:`. The retained source statement numbers remain visible.

| Source notation | Paper notation | Meaning and reason |
| --- | --- | --- |
| FAM `a=5+2√6` | `a_cusp=5+2√6` | Cusp logarithmic constant, distinguished from affine twist variables. |
| FAM C.1 proof `u=e^(2πiμ₀)` | `v_cusp` | Multiplicative cusp value; avoids Engel's global `u=w²`. |
| FAM C.1 proof scalar `f` | `f_sc` | The Weierstrass scaling factor already named `f_sc` in FAM B.1.1; avoids the threefold projection `f`. |
| FAM and ARI modular nome `q=e^(2πiτ)` | `q_τ` | Distinguishes the elliptic modulus from the Albanese nomes. |
| ARI `q₁,q₂` | unchanged | `q₁=-w²/48³`, `q₂=iw/216`; `q₁=(27/64)q₂²`. |
| ARI `η` | `η_D` | Dedekind function; first-run notation, distinguished from the integral cohomology class. |
| ARI `N` | `𝒩` | The Gaussian-normalized theta norm; FAM C.2 uses `𝒩`. |
| ARI `L(t)=log N(P_t)` | `𝓛(t)=log 𝒩(P_t)` | Distinguished from a line bundle. `U_Λ` retains the full torus Green function. |
| ARI elliptic lattice `Λ,Λ′` | `Λ_ell,Λ′_ell` | Distinguished from FAM's marked rank-four period lattice. |
| ARI `Δ₀` | `Δ_mod` | The modular discriminant `q_τ∏(1−q_τⁿ)²⁴`. |
| ARI rational model `E_t`, coordinates `x,y`, point `P` | `E_t^div`, `x_div,y_div`, `P^div` | Auxiliary division-polynomial coordinates, not the FAM cubic coordinates. |
| ARI `Δ(t)=27t⁸(t−1)³` | `Δ_div(t)` | Discriminant of the auxiliary rational model. Generic `Δ_E` and `Δ_Λell` mean the discriminant of their named Weierstrass model/lattice. |
| ARI C.4.3 radicals `W,V` | `W_rad,V_rad` | Products of discriminants and division values, distinguished from the cusp fibre and the integral lattice. |
| ARI C.3.1 `G=g₂(i)` | `G_square` | Square-lattice invariant, distinguished from the local function `G(h,τ)` in the maximum proof. |
| ARI C.3.1 Taylor coefficients `A₂,A₄` | `α₂,α₄` | Avoids the monodromy matrices `A₁,A₂`. |
| ARI C.3.1/C.8.2 scalar `E=π²E₂/3` | `𝓔₂` | Scaled quasimodular scalar, distinguished from the rank-one lattice endomorphism `E`. |
| ARI C.8.2 Fourier sums `A_k` | `𝒮_k` | Scalar theta-series bounds, distinguished from monodromy matrices and duplication polynomials. |
| ARI C.8.4 coefficient bound `M` | `M_coeff` | Bound for five polynomial coefficients, distinguished from the global admissibility maximum `M`. |
| ARI C.8.4 local `u=t−1` | `v_t` | Avoids Engel's multiplicative family parameter. |
| ARI C.8.4 duplication polynomials `A_k` | `𝒜_k` | Avoids the first-run monodromy matrices. |
| ARI C.8.6 integral coordinate `u=1/℘(z)` | `v_℘` | Avoids the Engel parameter and the ladder coordinate. |
| ARI C.8.9 local base coordinate `w` | `z_B` | Avoids the global moduli parameter `w=e^(−πic)`. |
| ARI C.8.11 `W` | `𝒲` | Logarithmic theta derivative; avoids the cusp fibre `W`. |
| ARI C.8.11 `R=μ′−a` | `ℛ_μ` | Derivative defect; distinguished from radii and the theta quotient. |

## Cubic normalization and section sign

FAM B.1.1 uses `y_F²=x_F³−3t³(t−1)x_F+2t⁴(t−1)²`. FAM B.1.4 fixes the cusp branch with distinguished section `(0,−√2 t²(t−1))`. ARI C.4 uses `y_div²=x_div³−(3/4)t³(t−1)x_div+(1/4)t⁴(t−1)²` and section `(0,t²(t−1)/2)`. The coordinate substitution `x_F=2x_div`, `y_F=−2√2 y_div` identifies both equations and these distinguished sections. This is a coordinate dictionary, not a new geometric theorem. The norm is independent of the Weierstrass homothety and is even in the point, as in the ARI C.4 setup and C.1.1 proof. Generic sigma/division-polynomial arguments retain their explicitly stated normalization `x=℘`, `y=℘′/2`, `ψ₁=1`, `ψ₂=2y`.

## Special source conventions

`ρ=(1+i√3)/2=e^(πi/3)`, not the other primitive cube root. The finite values are `μ(z₁)=(2−ρ)/3`, `μ(z₂)=(1−i)/2`; the cusp value is `μ₀=1/2−i log(5+2√6)/(2π)`. All phases are continued from that branch. The period half-plane is `Im c<−M` with `M=−(3/π)log6`; the positive-imaginary Albanese representatives are `−κ₁` and `−κ₂/2`. The interval cover uses `0≤Re τ≤1/2`, `|τ|≥1` and not a change of root-deck orientation.

The current convention is exactly the corrected ARI C.8.9 convention: `ddᶜ=(i/π)∂∂̄`, positive Betti measure `db∧da`, total mass `1/12`, probability measure `12m_P`. No sign is changed in the mathematical statements.


# Notation concordance: cohomology

The source statements retain the first-run convention: the coarse base is
`B=\mathbb P^1_t`, its points are `p_1=0`, `p_2=1`, `p_0=\infty`, the
standard finite multiplicities are 3 and 4, the root generators are
clockwise, and `\beta=\beta_{\mathrm{part}}+c`. No additional special-point
swap is required in these fragments. The alternate Engel marking `Q` in
INV is not used; the paper retains the FAM marking `P_{\mathrm{mark}}`.

## Symbol concordance

| Source symbol | Printed symbol | Reason and scope |
| --- | --- | --- |
| Dual lattice covectors `u,w` | `u_{\Lambda},w_{\Lambda}` | Distinguishes the period covectors from family parameters; the hatted lattice vectors stay unchanged. Local module generators named `u` are untouched. |
| INV logarithmic relative cotangent `E` or `\mathcal E` | `\mathcal E_{\rm cot}` | Keeps the relative cotangent bundle separate from the tangent bundle and elliptic curves. |
| FAM/PUSH/CDP root vertical tangent `\mathcal E` | `\mathcal E_{\rm tan}` | Distinguishes tangent and cotangent source conventions. |
| INV coarse direct-image bundle `G` | `G_B` | Separates the coarse and root-curve extensions. |
| FAM/PUSH/CDP root direct-image bundle `G` | `G_{\mathfrak B}` | Same distinction. |
| INV root curve `\mathcal B` | `\mathfrak B` | Matches the first-run convention. |
| Root-to-coarse map `\rho` | `\varpi` | Reserves `\rho` for the sixth root `e^{\pi i/3}`. |
| INV cotangent determinant line `N` | `N_{\rm det}` | Separates this line from the Bott--Chern ideal and from a cusp tube. |
| INV square-zero ideal `N` | `N_{BC}` | Only the ideal in inv:C3.3. |
| FAM/PUSH cusp normalization surface `E` | `P_6` | The degree-six del Pezzo surface; not an elliptic curve or a vector bundle. |
| Source B2.2 weighted variables `x` of weight 4, `y` of weight 3 | `x` of weight 3, `y` of weight 4 | Swapped consistently only in the valuation argument imported into inv:B3.3. |
| Source B2.2 auxiliary line `\mathcal L` | `\mathcal L_{\rm root}` | Separates the valuation argument from the integral Picard generator. |
| CDP residue indices `r_1(n),r_2(n)` | `r_3(n),r_4(n)` | The subscripts now record the actual root orders; the residue formulas are unchanged. |

Original statement IDs are retained with `inv:`, `fam:`, `push:`, or `cdp:`
prefixes. Internal equation labels receive the same run prefix. Label and
reference keys are protected before symbol substitutions; no mathematical
replacement is allowed inside an identifier. The source's references to
Part A now point to `sec:cotangent-images`, except the reference to its Hodge
diamond, which points to the more precise `sec:hodge`.

## Environments, packages, and macros

The fragments have no preamble or bibliography. They use `theorem`, `lemma`,
`proposition`, `corollary`, `definition`, `remark`, `announcement`, `cited`,
and `proof`, with the supplied `\uses{...}` macro after each formal
statement. The central preamble provides these environments and `\uses`.
Standard requirements are `amsmath`, `amssymb`, `amsthm`, `mathtools`,
`mathrsfs`, and the central table packages. Existing math operators such as
`\Hom`, `\Ext`, `\rank`, `\coker`, `\im`, `\Spec`, `\Proj`, `\Pic`,
`\End`, `\Sym`, `\Res`, `\ord`, `\tr`, and `\lcm` come from that preamble.
The proof shorthands use the central `\dbar` and `\dhat`; the master
normalizes any legacy `\dh` spelling to `\dhat` to avoid redefining the
standard T1 text command. No standard LaTeX command is redefined here.

## Content-preserving layout edits

Long proofs are divided into numbered steps by placing step labels at
existing source paragraph boundaries. Source formulas are not altered by
that operation. References and notation are normalized before recording
`statement_as_printed`; every stored printed statement is matched against
the generated fragment. Exact original source statements are retained
separately in `source_statement`.

## Final Appendix B cusp-coordinate correction

The final visual check identified a remaining notation collision in the
FAM A.5.2 re-derivation. In that appendix proof, the two occurrences of the
weight-twelve modular discriminant `\Delta(\tau)` become
`\Delta_{\rm mod}(\tau)`. The finite root-disc notation `\Delta_{s_j}` is
unchanged.

The source expressly calls the local equation `q=z_0z_1z_2` the original
cusp family. Only that coordinate and its subsequent occurrences in the
same cusp calculations are renamed to `t_c`: the convergent-series ring,
the toric gluing `u(q)q^{B_0\lambda}`, the relation
`\Delta(\tau)=q\,u(q)`, the field `q\partial_q`, and the differentials
`dq`. The last three now read `\Delta_{\rm mod}(\tau)=t_c\,u(t_c)`,
`t_c\partial_{t_c}`, and `dt_c`. Cohomological indices `q` in higher
direct images, degree conditions and cases are unchanged. No equality
between `t_c` and the modular nome `q_\tau` is introduced.

The exact scope and replacement counts are recorded in
`appendix_notation_changes.json`; `appendix_notation_fix.diff` records the
before/after appendix fragment. The generating script applies the same
finite list of replacements with count assertions, preserving all
statements, hypotheses and proof steps.

The same final scan found exactly one additional modular-discriminant
token in the main INV A1.0 proof. With the assembling editor's explicit
authorization, `\Delta(\tau)^{-1}` there is likewise renamed to
`\Delta_{\rm mod}(\tau)^{-1}`. Its surrounding cusp coordinate was
already `t_c`; no other main-fragment notation is changed. This additional
one-token correction is included in `appendix_notation_changes.json`.


# Geometry and ends: notation and identifier concordance

All mathematical conventions are those of FAM, `returns/S6_02_FAMILY/sections/conventions.tex`. The changes below are notation, reference or layout changes; the source statements, hypotheses and scopes remain separately recorded in `records.json`. Exact statement and proof diffs are in `statement_comparisons.json` and `proof_comparisons.json`.

## Common conventions retained

The base is `B=P^1_t`, with `p_1=0`, `p_2=1`, `p_0=infinity`; the retained multiplicities are `(3,4)`. Homology columns have order `(hat-gamma,hat-u,hat-w,hat-delta)`. The deck generators are clockwise root transformations, `g_1g_2g_0=1`; positive geometric parameter loops are counterclockwise. The period matrix is `Pi_c=((6mu,tau,1,0),(beta_part+c,mu,0,1))`, with `(beta_part+tau)(p_0)=0`, and `w=exp(-pi*i*c)`. The Albanese nome is `q_2=iw/216`. The fibre vector is `e=(0,1)^t=Pi_c hat-delta`; the lattice vector is `d=hat-delta`.

## Symbol mappings

| Source and scope | Source notation | Printed notation | Reason / sign convention |
|---|---|---|---|
| FAM F, lattice | `e=hat-delta` | `d=hat-delta` | Distinguishes the primitive lattice vector from the fibre vector `e` already used in FAM AB. Every concatenated occurrence `Je`, `C e`, `R e`, `Z e`, stabilizer subscript and `q_e` is changed consistently. |
| FAM F | `E=e tensor gamma`, `q_e`, `P_{e,Z/R/Q}` | `E=d tensor gamma`, `q_d`, `P_{d,Z/R/Q}` | Same operator, invariant function and stabilizer. |
| FAM F, auxiliary scalars | matrix entry/denominator `d` | `d_aux` | Prevents the local scalar from colliding with the renamed lattice vector. Matrix formulas and denominator-clearing integers are otherwise unchanged. |
| FAM F.3.3 | cusp `q=exp(2pi*i*s)` | `t_c=exp(2pi*i*s)` | Keeps the cusp coordinate distinct from the Albanese nome. Exponentials `e^(pi*i/3)` and `e^(2pi*i*s)` remain exponentials. |
| FAM F and D, dual coframe | `u,w` in wedge forms | `u_Lambda,w_Lambda` | Matches the root paper's dual-coframe notation; hatted homology vectors and parameter `w` are unchanged. |
| FAM D | `beta` | `beta=beta_part+c` | Retains the actual period, not the particular solution alone. |
| FAM D.1.4 | `T,U,D` in `G` | `T=Im tau`, `U=Im mu`, `D=Im beta-6U^2/T` stated explicitly | `T` is defined in FAM C; `U` is not locally defined in CD.tex. This notational ambiguity is recorded in the discrepancy report. No entry of `G`, determinant or intersection sign is changed. |
| FAM D.1.4/D.1.6 | Hermitian form | `H_E(v,w)=Etilde(v,Jw)-i Etilde(v,w)` | The source convention, linear in its first entry, is retained. Its Chern form is `-Im H_E`; no sign is silently imported from AC26. |
| MAPS A.3 | homology `g` | `hat-gamma` in the translation formula | The short alias is removed. |
| MAPS A.3 representative formula | `S(t)d` in a fibre-coordinate translation, although `d=hat-delta` | `S(t)e`, with `e=Pi_c d=(0,1)^t` explicitly stated | Exposes the source's lattice/fibre-vector shorthand. All coefficients, branches and real representatives are unchanged. |
| MAPS A.3 | circle action `rho` | `rho_circ(b)` is translation by `b e`, `b in R/Z` | Explicitly identifies the source circle action with FAM B.4.1 and reserves the unadorned `rho=exp(pi*i/3)` for the period constant. Every `rho(1/2)` is renamed consistently. |
| MAPS A.3 | `D_1,D_2,D_12` | unchanged | Directions `e_1,e_2,e_1-e_2`; `D_2` is the circle-fixed curve. These are not interchanged. |
| PUSH A | Engel line bundle `L` | `M_S=O_S(P-O)` | Matches FAM conventions. The cotangent complex `mathbb L_D` in A.2.5 remains `mathbb L_D`; it is not the line bundle. |
| PUSH A | linearization line `J` | `J_lin` | Avoids confusing the line bundle with a real complex structure or the monodromy integer. Its Chern class is still the lower-case `j`. |
| PUSH A fan | cusp `q`, height `h_q` | `t_c`, `h_{t_c}` | Same cusp base coordinate and same primitive ray heights. The degeneration parameter `u` is unchanged. |
| E26 Conjecture 8.2 quotation | `M` | `M` inside the verbatim quotation, identified with `M_S` immediately afterward | Preserves the exact conjecture wording; outside that quotation `M` remains the period maximum. |
| PUSH E.2.7/E.2.21 | fixed-pair parameter `z=exp(-pi*i*c/(kl))` | `w_{k,l}` | Separates the parameter from the first-run uniformizing coordinate `z`. |
| MAPS B.6.24 | positive generator `2kl` of the parameter-period lattice | unchanged | The source positive closing-translation convention is retained. The positive geometric `w` loop in the retained family lifts to `c -> c-2`; no nonzero sign-sensitive mapping class is inferred. |
| FAM/PUSH bibliography | `DGKX26v1`, `DuGuoKusakabeXie2026v1` | `DGKXv1` | Common bibliography key. The full-automorphism locator is the theorem labelled `p2:thm:full-automorphisms`, not an unqualified period-classification citation. |
| FAM period cross-reference | `eq:cd-beta` | `fam:eq:cd-beta` | Matches the period agent's sole equation label; no second label is inserted into its equation. |

## Statement and equation labels

Every retained numbered source statement has the label `run:original-ID`: `fam:B.4.1`, `fam:B.4.2`, `ari:C.2.2`, `maps:A.3.1`–`maps:A.3.3`, `fam:F.1.1`–`fam:F.3.3`, `fam:D.1.1`–`fam:D.2.3`, the retained `push:A.*`, `push:D.1.*`, and all specified `push:B.4.33`, `push:C.3.24`, `push:C.3.27`, `maps:B.6.21`, `maps:B.6.24`, `push:E.2.21`–`push:E.2.24`.

The exact E26 target is labelled `e26:Conjecture8.2`. The final replacement sentence of PUSH A.3.2 is labelled `push:A.3.2.replacement` and separately typed A; its source ID remains A.3.2. The rest of that source statement is the T-item `push:A.3.2`.

FAM displayed labels acquire the `fam:` prefix, including `fam:eq:F-g`, `fam:eq:F-Gamma`, `fam:eq:F-law`, `fam:eq:F-SLpresentation`, `fam:eq:F-H`, `fam:eq:F-qD`, `fam:eq:F-tauaction`, `fam:eq:F-j`, `fam:eq:cd-NS` and `fam:eq:cd-theta-sections`. Contextual definitions use labels ending `.setup`, `.scope`, `.representatives`, `.fan`, `.rays`, `.periods`, `.Hermitian` or `.orientation`; their metadata identifies the original unnumbered context or proof extract explicitly, rather than inventing an original theorem number.

## Scoped reuse retained from the sources

The symbols `B` (base / local 2-by-2 block), `T` (modular generator / imaginary period / translation `t_{6P}`), and `E` (rank-one marking operator / alternating class) have explicitly separated local scopes, as in the first run. The local `S(t)` in the real representative table is a scalar translation function, whereas `S` in the filling section is Engel's rational elliptic surface. The record does not identify these objects.


## Complete retained-label concordance

| Run | Source ID | Paper label | Status |

|---|---|---|---|

| FAM | conventions | def:conventions | text |

| FAM | A.1.1 | fam:A.1.1 | K |

| DGKXv1 | Theorem 7.2; thm:all-maps-factor | dgkx:all-maps-factor | K |

| FAM | B.1.1 | fam:B.1.1 | T |

| FAM | B.1.2 | fam:B.1.2 | T |

| FAM | B.1.3 | fam:B.1.3 | T |

| FAM | B.1.4 | fam:B.1.4 | T |

| FAM | B.2.3 | fam:B.2.3 | T |

| FAM | A.5.1 | fam:A.5.1 | K |

| FAM | B.2.1 | fam:B.2.1 | T |

| FAM | B.2.2 | fam:B.2.2 | T |

| FAM | B.3.1 | fam:B.3.1 | T |

| PUSH | E.1.1 | push:E.1.1 | A |

| PUSH | E.1.2 | push:E.1.2 | A |

| FAM | A.1.2 | fam:A.1.2 | T |

| FAM | A.2.1 | fam:A.2.1 | K |

| FAM | A.3.1 | fam:A.3.1 | K |

| FAM | A.4.1 | fam:A.4.1 | T |

| FAM | A.4.2 | fam:A.4.2 | K |

| WORKBENCH | pshift:lem:centralizer | pshift:lem:centralizer | K |

| WORKBENCH | pshift:thm:classification | pshift:thm:classification | K |

| FAM | C.1.1 | fam:C.1.1 | T |

| FAM | C.1.2 | fam:C.1.2 | T |

| ARI | C.1.1 | ari:C.1.1 | T |

| ARI | C.1.2 | ari:C.1.2 | T |

| ARI | C.2.1 | ari:C.2.1 | T |

| ARI | C.4.2 | ari:C.4.2 | T |

| ARI | C.4.3 | ari:C.4.3 | T |

| ARI | C.4.4 | ari:C.4.4 | T |

| ARI | C.8.6 | ari:C.8.6 | T |

| ARI | C.8.7 | ari:C.8.7 | T |

| ARI | C.8.8 | ari:C.8.8 | A |

| ARI | C.8.9 | ari:C.8.9 | A |

| ARI | C.8.10 | ari:C.8.10 | A |

| ARI | C.8.11 | ari:C.8.11 | A |

| FAM | C.2.3 | fam:C.2.3 | T |

| PUSH | E.4.1 | push:E.4.1 | T |

| ARI | C.3.1 | ari:C.3.1 | T |

| ARI | C.8.1 | ari:C.8.1 | T |

| ARI | C.8.2 | ari:C.8.2 | T |

| ARI | C.8.3 | ari:C.8.3 | T |

| ARI | C.8.4 | ari:C.8.4 | T |

| ARI | C.8.5 | ari:C.8.5 | T |

| ARI | C.8.15 | ari:C.8.15 | A |

| FAM | C.1 setup | periods:theta-definitions | text |

| FAM | C.1.2 artifact-availability record | periods:special-computation-availability | text |

| ARI | C.1 setup; C.8 critical setup | periods:norm-definition | text |

| FAM | C.2.1 proof, eq:cd-norm | fam:eq:cd-norm | text |

| ARI | C.4 setup and local-height notation in C.4.1 | periods:division-model | text |

| ARI | C.8 measure conventions | periods:measure-conventions | text |

| FAM;PUSH | FAM C.2.3; PUSH E.4.1–3; REVIEW_S6_02_FAMILY §2 | periods:certificate-record | text |

| ARI | C.3 setup | periods:local-expansion-constants | text |

| ARI | C.8 analytic setup | periods:ladder-modular-conventions | text |

| INV | notation-cotangent | inv:notation-cotangent | text |

| INV | A1.0 | inv:A1.0 | T |

| INV | A1.1 | inv:A1.1 | T |

| INV | A1.2 | inv:A1.2 | T |

| INV | notation-period-branch | inv:notation-period-branch | text |

| INV | A2.1 | inv:A2.1 | T |

| INV | A2.2 | inv:A2.2 | T |

| INV | A2.4 | inv:A2.4 | T |

| INV | A1.3 | inv:A1.3 | T |

| INV | A3.1 | inv:A3.1 | T |

| INV | notation-hodge-input | inv:notation-hodge-input | text |

| INV | C1.1 | inv:C1.1 | T |

| INV | C2.1 | inv:C2.1 | T |

| INV | C3.3 | inv:C3.3 | A |

| INV | B1.1 | inv:B1.1 | T |

| INV | B2.1 | inv:B2.1-canonical | T |

| INV | B1.2 | inv:B1.2 | A |

| INV | B2.1 | inv:B2.1-hodge | A |

| INV | B3.1 | inv:B3.1 | T |

| INV | B3.2 | inv:B3.2 | T |

| INV | B3.3 | inv:B3.3 | T |

| INV | C3.5 | inv:C3.5 | A |

| INV | C3.7 | inv:C3.7 | A |

| INV | A4.1 | inv:A4.1 | T |

| INV | A4.2 | inv:A4.2 | T |

| FAM | A.5.2 | fam:A.5.2 | K |

| CDP | notation-integral-twists | cdp:notation-integral-twists | text |

| CDP | C5b | cdp:C5b | T |

| PUSH | E.2.1 | push:E.2.1 | T |

| FAM | F4 consequence of A.5.2; binding row 6d | fam:A.5.2-corollary | T |

| FAM | B.4.1 | fam:B.4.1 | K |

| FAM | B.4.2 | fam:B.4.2 | T |

| ARI | C.2.2 | ari:C.2.2 | T |

| MAPS | A.3 (opening conventions) | maps:A.3.setup | text |

| MAPS | A.3.1 | maps:A.3.1 | A |

| MAPS | A.3, equations (A.3.1)–(A.3.2) | maps:A.3.representatives | text |

| MAPS | A.3.2 | maps:A.3.2 | A |

| MAPS | A.3.3 | maps:A.3.3 | A |

| FAM | F (opening conventions) | fam:F.setup | text |

| FAM | F.1.1 | fam:F.1.1 | T |

| FAM | F.1.2 | fam:F.1.2 | T |

| FAM | F.2 (definition preceding F.2.1) | fam:F.2.setup | text |

| FAM | F.2.1 | fam:F.2.1 | T |

| FAM | F.2.2 | fam:F.2.2 | T |

| FAM | F.2.3 | fam:F.2.3 | T |

| FAM | F.3.1 | fam:F.3.1 | T |

| FAM | F.3.2 | fam:F.3.2 | T |

| FAM | F.3.3 | fam:F.3.3 | T |

| FAM | D.1.1 | fam:D.1.1 | T |

| FAM | D.1.2 | fam:D.1.2 | T |

| FAM | D.1.3 | fam:D.1.3 | T |

| FAM | D.1.6 (proof, Hermitian-form convention) | fam:D.1.Hermitian | text |

| FAM | D.1.4 | fam:D.1.4 | T |

| FAM | D.1.5 | fam:D.1.5 | T |

| FAM | D.1.6 | fam:D.1.6 | T |

| FAM | D.1.7 | fam:D.1.7 | T |

| FAM | D.2.1 | fam:D.2.1 | T |

| FAM | D.2.2 | fam:D.2.2 | T |

| FAM | D.2.3 | fam:D.2.3 | T |

| PUSH | D (opening definitions) | push:D.1.setup | text |

| PUSH | D.1.1 | push:D.1.1 | T |

| PUSH | D.1.2 | push:D.1.2 | T |

| PUSH | D.1.3 | push:D.1.3 | T |

| PUSH | A.1 (opening definitions) | push:A.1.setup | text |

| E26 | Conjecture 8.2 | e26:Conjecture8.2 | false as worded |

| PUSH | A.3.1 | push:A.3.1 | T |

| PUSH | A.3.2 | push:A.3.2 | T |

| PUSH | A.3.2 | push:A.3.2.replacement | A |

| PUSH | A.1.1 (proof, cone definition) | push:A.1.fan | text |

| PUSH | A.1.1 | push:A.1.1 | A |

| PUSH | A.1.2 | push:A.1.2 | A |

| PUSH | A.2.1 (proof, six rays and bottom diagonal) | push:A.2.rays | text |

| PUSH | A.2.1 | push:A.2.1 | A |

| PUSH | A.2.2 | push:A.2.2 | A |

| PUSH | A.2.3 | push:A.2.3 | A |

| PUSH | A.2.4 (proof, base-changed period shears) | push:A.2.periods | text |

| PUSH | A.2.4 | push:A.2.4 | A |

| PUSH | A.2.5 | push:A.2.5 | A |

| PUSH | Conventions; B.4.33 (scope) | push:B.4.33.scope | text |

| PUSH | B.4.33 | push:B.4.33 | A |

| PUSH | Conventions (mapping-torus orientation) | push:C.orientation | text |

| PUSH | C.4.1 (scope) | push:C.4.1.scope | text |

| PUSH | C.3.24 | push:C.3.24 | A |

| PUSH | C.3.27 | push:C.3.27 | A |

| MAPS | B.6.21 | maps:B.6.21 | A |

| PUSH | E.1.1 (sphere data); FAM B.3.1 (parameter lattice) | push:E.1.1.scope | text |

| MAPS | B.6.24 | maps:B.6.24 | A |

| PUSH | E.2.5 (hypotheses); E.2.7 (parameter) | push:E.2.5.scope | text |

| PUSH | E.2.21 | push:E.2.21 | A |

| PUSH | E.2.22 | push:E.2.22 | A |

| PUSH | E.2.23 | push:E.2.23 | A |

| PUSH | E.2.24 | push:E.2.24 | A |

## Source equation and ancillary labels

The following labels are used in the assembled fragments. Prefixes identify the source run; the unchanged source ID or descriptive tail is retained.

- `app:credits`
- `app:dependencies`
- `app:known-periods`
- `app:notation`
- `app:source-status`
- `app:tangent-rederivation`
- `app:verification`
- `ari:C.1.1`
- `ari:C.1.2`
- `ari:C.2.1`
- `ari:C.2.2`
- `ari:C.3.1`
- `ari:C.4.2`
- `ari:C.4.3`
- `ari:C.4.4`
- `ari:C.8.1`
- `ari:C.8.10`
- `ari:C.8.11`
- `ari:C.8.15`
- `ari:C.8.2`
- `ari:C.8.3`
- `ari:C.8.4`
- `ari:C.8.5`
- `ari:C.8.6`
- `ari:C.8.7`
- `ari:C.8.8`
- `ari:C.8.9`
- `ari:eq:ca-GHbounds`
- `ari:eq:ca-H`
- `ari:eq:ca-current`
- `ari:eq:ca-delta-h`
- `ari:eq:ca-density0`
- `ari:eq:ca-density1`
- `ari:eq:ca-derivatives`
- `ari:eq:ca-exp`
- `ari:eq:ca-ladder`
- `ari:eq:ca-mahler`
- `ari:eq:ca-nu`
- `ari:eq:ca-sup`
- `ari:eq:ca-wpmean`
- `ari:eq:cs-Li`
- `ari:eq:cs-division`
- `ari:eq:cs-isogeny`
- `ari:eq:cs-torsionvalue`
- `cdp:C5b`
- `cdp:notation-integral-twists`
- `def:conventions`
- `dgkx:all-maps-factor`
- `e26:Conjecture8.2`
- `fam:A.1.1`
- `fam:A.1.2`
- `fam:A.2.1`
- `fam:A.3.1`
- `fam:A.4.1`
- `fam:A.4.2`
- `fam:A.5.1`
- `fam:A.5.2`
- `fam:A.5.2-corollary`
- `fam:B.1.1`
- `fam:B.1.2`
- `fam:B.1.3`
- `fam:B.1.4`
- `fam:B.2.1`
- `fam:B.2.2`
- `fam:B.2.3`
- `fam:B.3.1`
- `fam:B.4.1`
- `fam:B.4.2`
- `fam:C.1.1`
- `fam:C.1.2`
- `fam:C.2.3`
- `fam:D.1.1`
- `fam:D.1.2`
- `fam:D.1.3`
- `fam:D.1.4`
- `fam:D.1.5`
- `fam:D.1.6`
- `fam:D.1.7`
- `fam:D.1.Hermitian`
- `fam:D.2.1`
- `fam:D.2.2`
- `fam:D.2.3`
- `fam:F.1.1`
- `fam:F.1.2`
- `fam:F.2.1`
- `fam:F.2.2`
- `fam:F.2.3`
- `fam:F.2.setup`
- `fam:F.3.1`
- `fam:F.3.2`
- `fam:F.3.3`
- `fam:F.setup`
- `fam:eq:F-Gamma`
- `fam:eq:F-H`
- `fam:eq:F-SLpresentation`
- `fam:eq:F-g`
- `fam:eq:F-j`
- `fam:eq:F-law`
- `fam:eq:F-qD`
- `fam:eq:F-tauaction`
- `fam:eq:ab-cusp-resolution`
- `fam:eq:ab-direct-images`
- `fam:eq:ab-log-tangent`
- `fam:eq:ab-normal-quotient`
- `fam:eq:ab-relative-dualizing`
- `fam:eq:ab-root-degree`
- `fam:eq:cd-NS`
- `fam:eq:cd-beta`
- `fam:eq:cd-norm`
- `fam:eq:cd-theta-sections`
- `fam:eq:cd-wp`
- `inv:A1.0`
- `inv:A1.1`
- `inv:A1.2`
- `inv:A1.3`
- `inv:A2.1`
- `inv:A2.2`
- `inv:A2.4`
- `inv:A3.1`
- `inv:A4.1`
- `inv:A4.2`
- `inv:B1.1`
- `inv:B1.2`
- `inv:B2.1-canonical`
- `inv:B2.1-hodge`
- `inv:B3.1`
- `inv:B3.2`
- `inv:B3.3`
- `inv:C1.1`
- `inv:C2.1`
- `inv:C3.3`
- `inv:C3.5`
- `inv:C3.7`
- `inv:eq:A-E-line`
- `inv:eq:A-H-images`
- `inv:eq:A-N-images`
- `inv:eq:A-absolute-table`
- `inv:eq:A-modular-K`
- `inv:eq:A-mu-value`
- `inv:eq:A-s-branch`
- `inv:eq:C-BC-A`
- `inv:eq:C-arrows`
- `inv:eq:C-hodge-input`
- `inv:notation-cotangent`
- `inv:notation-hodge-input`
- `inv:notation-period-branch`
- `maps:A.3.1`
- `maps:A.3.2`
- `maps:A.3.3`
- `maps:A.3.representatives`
- `maps:A.3.setup`
- `maps:B.6.21`
- `maps:B.6.24`
- `maps:eq:A.3.3`
- `pshift:eq:actual-overlap-difference`
- `pshift:eq:affine-bundle-action`
- `pshift:eq:centralizer`
- `pshift:eq:classification`
- `pshift:eq:cocycle-law`
- `pshift:eq:coherent-shift-action`
- `pshift:eq:covariance`
- `pshift:eq:cusp-actions-identical`
- `pshift:eq:cusp-cocycle`
- `pshift:eq:cusp-periods`
- `pshift:eq:cusp-translation`
- `pshift:eq:finite-class`
- `pshift:eq:finite-data`
- `pshift:eq:finite-equation`
- `pshift:eq:finite-middle-sections`
- `pshift:eq:finite-norm-obstruction`
- `pshift:eq:finite-overlap-identity`
- `pshift:eq:full-isomorphism`
- `pshift:eq:global-correction`
- `pshift:eq:integer-shear`
- `pshift:eq:local-affine-cocycle`
- `pshift:eq:local-corrections`
- `pshift:eq:local-matrix-identity`
- `pshift:eq:no-analytic-obstruction`
- `pshift:eq:norms`
- `pshift:eq:parameter-disc`
- `pshift:eq:period-morphism`
- `pshift:eq:periods`
- `pshift:eq:rank-one-map`
- `pshift:eq:vector-sheaf`
- `pshift:lem:centralizer`
- `pshift:sec:classification`
- `pshift:thm:classification`
- `push:A.1.1`
- `push:A.1.2`
- `push:A.1.fan`
- `push:A.1.setup`
- `push:A.2.1`
- `push:A.2.2`
- `push:A.2.3`
- `push:A.2.4`
- `push:A.2.5`
- `push:A.2.periods`
- `push:A.2.rays`
- `push:A.3.1`
- `push:A.3.2`
- `push:A.3.2.replacement`
- `push:B.4.33`
- `push:B.4.33.scope`
- `push:C.3.24`
- `push:C.3.27`
- `push:C.4.1.scope`
- `push:C.orientation`
- `push:D.1.1`
- `push:D.1.2`
- `push:D.1.3`
- `push:D.1.setup`
- `push:E.1.1`
- `push:E.1.1.scope`
- `push:E.1.2`
- `push:E.2.1`
- `push:E.2.21`
- `push:E.2.22`
- `push:E.2.23`
- `push:E.2.24`
- `push:E.2.5.scope`
- `push:E.4.1`
- `sec:algebraic-dimension-nearby`
- `sec:announcements`
- `sec:bc-aeppli`
- `sec:cohomology`
- `sec:cotangent-images`
- `sec:discrete`
- `sec:ends`
- `sec:family`
- `sec:fibres`
- `sec:frolicher`
- `sec:hodge`
- `sec:maximum`
- `sec:metric-announcements`
- `sec:monodromy`
- `sec:multiplicities-covers`
- `sec:periods`
- `sec:real`
- `sec:relative-correction`
- `sec:tangent`
- `sec:tangent-higher`
- `sec:tangent-known`
- `sec:tangent-twists`
