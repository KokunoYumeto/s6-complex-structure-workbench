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
