# Independent global deformation audit — 2026-09-06

Result: no mathematical error or missing implication was found in the scoped
global nontriviality argument. The dual-number section calculation and the
scheme-theoretic critical-value argument suffice to turn the independently
checked nonzero regular-fibre class into a nonzero class in
`H^1(X_{c_*}, T_{X_{c_*}})`.

This audit made no canonical-source edits, ran no builds or Lean processes,
and performed no remote writes. It does not audit or assume sphere recognition,
the global integral-cohomology claim, or the CDP argument.

## Scope and source identity

The complete `period_parameter_deformation.tex` and
`analytic_canonical_ring.tex` were read. Relevant period-equivariance,
admissibility, finite-filling, toric-chart, properness, and global-gluing
proofs in `candidate_geometry.tex` were checked. The determinant-character
and Hodge-line proof in `analytic_picard.tex`, lines 26–254, was also checked
because it supplies the actual transitions used by the canonical-ring proof.
The original period-matrix algebra and the minus sign converting the
plus-graph derivative into the connecting Kodaira–Spencer convention had
already been independently checked by the root's other reviewer; this audit
uses that checked nonzero fibre class and does not claim a second symbolic run.

All source paths below have prefix
`output/s6_consolidated_canonical_2026-08-26/supporting_materials/workbench/research/`.

SHA-256 identities at inspection:

| File | SHA-256 |
| --- | --- |
| `period_parameter_deformation.tex` | `D6CCC5913712497B54895255C6F4483AE3575E8507C2FD423A6A10282FF16162` |
| `analytic_canonical_ring.tex` | `D7B2F50379048ED2705F9BA204DCCECA51BA65FB6357B2C859C0AEF707E24364` |
| `analytic_picard.tex` | `383CFD8101E370F4DA53CEF241120C5447FA342D6E4D01FEBC9383FA77177A57` |
| `candidate_geometry.tex` | `0BFDFEC375CC980A23F61F54BB07D2B81C4547DACB8221E441D7D24C0A43414B` |

## 1. The holomorphic family really retains the same local construction

In `period_parameter_deformation.tex`, lines 76–211, the varying term is the
original additive constant in the lower-left period entry. The original
matrices `R_g` depend on `tau` and `mu`, so they remain unchanged; the
integral deck matrices and both translations `v_j/m_j` also remain unchanged.
Consequently the quotient action and the logarithmic conjugating section
are holomorphic in `(z,c)` and satisfy the same identities with the actual
constant retained. In particular the logarithm ambiguity in (PD8) is an
actual period, not an unverified translation class.

For the cusp, the bound in (PD10) is taken over the compact set formed by the
closed cusp disc and `overline Q`. The inverse bound from (PD12) therefore
holds uniformly. A meeting of two product charts is open and meets the
dense torus; the original bounded-chart-pair estimate bounds the same finite
set of lattice translations uniformly in `c`. This includes meetings at the
boundary, so proper discontinuity there is established rather than inferred
from the punctured family.

The compact representative set in the properness argument is independent
of `c`. At `t_c != 0`, the original exact lattice translation places the
logarithmic position in the radius `sqrt(2)` ball. At `t_c = 0`, for a cell
with vertex `v`, the translation parameter is exactly `B_0 v`; because
`B_0^2 v = -v`, it moves the cell to one containing zero. The full nonzero
multiplier `exp(2 pi i C(0,c) B_0 v)` preserves the toric orbit label. The
six closed bidiscs cover every point of `E_0`, whatever that multiplier's
modulus or argument. This is the same exact justification as
`candidate_geometry.tex`, lines 950–1006. Thus `K_0 x K` supplies all
representatives for each compact parameter set `K`.

Both local quotient maps are local biholomorphisms from charts smooth over
`Q`, so their projections to `Q` are submersions even at critical points of
the separate map to `B`. The gluing uses entire restrictions over the base
cover, so points over the same `(t,c)` lie in one Hausdorff open piece.
Local properness over `B x Q` and compactness of `B` give the asserted
proper holomorphic submersion to `Q`.

## 2. The relative anticanonical identification is justified by transitions

The relevant argument is `period_parameter_deformation.tex`, lines 271–296,
with `analytic_canonical_ring.tex`, lines 48–103, and
`analytic_picard.tex`, lines 83–251.

On a finite covering chart, write the original lift as

`(s,c,zeta) -> (zeta_j s,c,R_g(s) zeta + Pi(g s,c) v_j/m_j)`.

Taking the relative canonical form `ds wedge d zeta_1 wedge d zeta_2`
over `Q`, differentiation of the translation contributes only `ds` and
`dc` terms. The `ds` terms disappear on wedging with `ds`; the `dc`
terms are zero in relative differentials over `Q`. Its transformation
factor is therefore exactly `chi_j = zeta_j det R_g`, independent of `c`.
The same `exp(varphi_j(s))` solves its coefficient equation, and the same
exponents `m_j - 1 - a_j` are respectively `0` and `2`. The divisor of
the relative evaluation section is consequently `2 S_2`, with no
parameter-dependent correction.

At the cusp, differentiating (PD11) changes each `dx_i/x_i` by a multiple
of `dt_c` plus a multiple of `dc`. Relative to `Q`, the latter is zero;
wedging with `dt_c` kills the former. Thus

`(dx_1/x_1) wedge (dx_2/x_2) wedge dt_c`

is the invariant nowhere-zero relative canonical frame, including across
the toric boundary. The unimodular computation establishing its ordinary
chart expression is `candidate_geometry.tex`, lines 849–867. The fixed
modular function `Theta` has the original transition factors and original
orders `2,1,-1`; it identifies the Hodge factor with the pullback of
`O_B(p_0)` throughout the family. The fixed functions
`h = 1/(t-1)` and `eta_B = dt/(t-1)^2` make exactly the divisor changes
used in (CR1). Finally `F^*(p_2 x Q) = 4 S_2` gives (PD16).

This proves a relative line-bundle identification by actual transitions.
No inference from separately chosen fibrewise line-bundle isomorphisms is
needed.

## 3. Dual-number section base change is exact

The relevant argument is `period_parameter_deformation.tex`, lines 298–328.
Keep `A = C[epsilon]/(epsilon^2)`, `L_A = omega_{X_A/A}^{-2}`, and
`L_* = omega_{X_{c_*}}^{-2}`. Since the total deformation is smooth over
the disc, its base change is flat over `A`; local freeness of `L_A` gives
the exact sheaf sequence (PD17) on the common underlying topological
space. Its first arrow sends a local section represented by a lift `v`
to `epsilon v` and is independent of the chosen lift.

The actual two sections pulled back from `O_B(p_2)` lift a basis of
`H^0(X_{c_*},L_*)` by the degree-two instance of (CR2)–(CR4). Consequently
reduction of any global section `s` has the unique form
`alpha_0 bar(s_0) + alpha_1 bar(s_1)`. The difference

`s - alpha_0 s_0 - alpha_1 s_1`

belongs to the kernel of the global reduction map. Left exactness of
global sections in (PD17) identifies that kernel with the injected copy
of `H^0(X_{c_*},L_*)`; therefore it equals
`epsilon beta_0 s_0 + epsilon beta_1 s_1`. This proves generation over
`A`. If an `A`-linear relation vanishes, its reduction kills its two
constant coefficients, and injectivity of the first arrow of (PD17)
kills its two epsilon coefficients. Thus (PD18) follows in both directions.

No vanishing of `H^1(L_*)` is required, and no invalid interchange of
pointwise dimension with base change occurs. The two generators have no
common zero because they are pullbacks of the basepoint-free system on
`B`; their map is exactly the retained coordinate expression
`[t-1 : A_0 + B_0'(t-1)]`.

## 4. The critical schemes detect infinitesimal motion of all three values

The relevant argument is `period_parameter_deformation.tex`, lines 330–367.
The critical ideal of a map from a smooth relative threefold to a smooth
relative curve is the ideal of the three coefficients of its relative
differential. It is preserved by isomorphisms of the source and by a base
coordinate change whose differential is a unit.

For each finite chart, retain the exact equation `t_j = s_j^{m_j}` with
`m_1 = 3`, `m_2 = 4`. Since these integers are units in `A`, the critical
ring in local torus coordinates is

`A{s_j,zeta_1,zeta_2}/(s_j^{m_j-1})`.

The pullback of `t_j` is zero in this ring. Evaluation at the zero section
and `s_j=0` gives a retraction onto `A`, so the structure map from `A`
is injective. The kernel of the map from the local base ring `A{t_j}`
to this critical ring is therefore exactly `(t_j)`: evaluation of a
base series gives its constant coefficient, and that coefficient can
vanish in the critical ring only if it is zero in `A`.

At a cusp triple chart the critical ring is

`A{z_0,z_1,z_2}/(z_1 z_2,z_0 z_2,z_0 z_1)`.

Here `t_c = z_0 z_1 z_2` is zero. Evaluation at the origin retracts
onto `A`, so the same kernel is exactly `(t_c)`. At a double chart,
`t_c = z_0 z_1` and the critical ideal is `(z_0,z_1)`, again giving
the identical base kernel. Smooth cusp charts have empty critical locus.
The covering maps are local biholomorphisms, so these local critical
ideals are the actual ideals downstairs. Outside the three distinguished
values the map is a submersion.

These computations show that the scheme-theoretic image of the critical
locus is exactly the union of the three constant `A`-sections. In
particular, it is not merely a statement about the three points of the
reduced central base. A displacement `epsilon d` of a given critical value
would pull back to the same element of the injected `A` on its critical
chart, and would vanish there only if `d=0`.

An identity-reducing first-order trivialization identifies the complete
relative anticanonical systems, so it induces a projective linear
automorphism of `P^1_A` reducing to the identity. The coordinate change
between the chosen anticanonical coordinates and the original `t`
coordinate is fixed, hence this is the claimed `a_A` in the original
coordinate. Preservation of the critical images fixes `0`, `1`, and
infinity as `A`-sections: their distinct closed points prevent any
permutation. Write

`a_A(t) = t + epsilon (b_0 + b_1 t + b_2 t^2)`.

Fixing zero gives `b_0=0`, and fixing one gives `b_0+b_1+b_2=0`.
In the retained coordinate `u=1/t`, the expression becomes

`u -> u - epsilon (b_0 u^2 + b_1 u + b_2)`.

Fixing infinity therefore gives `b_2=0`, and consequently also `b_1=0`.
The induced base automorphism is the identity.

## 5. The final global implication is valid

The resulting putative trivialization preserves `f_A` over the original
base. Base change by any retained regular value then restricts it to an
identity-reducing trivialization of the corresponding two-dimensional
torus deformation. That contradicts the independently checked nonzero
fibre Kodaira–Spencer class, with its explicit connecting-convention sign.
Thus no identity-reducing first-order trivialization of `X_A` exists.

The closing Cech argument at `period_parameter_deformation.tex`, lines
370–383, proves the needed implication from vanishing global
Kodaira–Spencer class to such a trivialization: differentiating product
chart transitions gives the tangent-valued 1-cocycle, and a coboundary is
removed by the corresponding local coordinate changes multiplied by
`epsilon`. Products of two correction terms vanish because `epsilon^2=0`.
The chosen sign affects the representative but not this vanishing
criterion. Therefore the global class is nonzero, as asserted.

No correction is requested from this audit.
