# Scalar C1 consistency: exact failure and dependency notice

Working audit dated 17 November 2026, after checkpoint14.
The historical promoted texts and their earlier audits are retained.
This notice does not overwrite any master statement or report.

## Exact newly identified map

SCN.15--SCN.21 in
notes/part3_scalar_c1_native_arrow_working.md compare the
actual native C0 and C1 outer fixed-normal charts.
Their first endpoint arrow is the identity. Their second
endpoint arrow is
\[
 \text{base }g/\kappa,\qquad
 \operatorname{diag}(\eta/\alpha,\kappa\alpha/(g\eta)).
\]
After reference division and conjugation of the negative
physical-weight line, the positive Hopf spinor map is
\(e^{-i\theta}I_2\). Its determinant winds \(-2\), while
the first endpoint winding is zero.
The resulting two-overlap scalar line has Cech class
\(-1\) in SCN.20's explicitly prescribed two-torus
orientation; its determinant has class \(-2\).
No global characteristic sign is selected from an expected
flop value.

This identifies the absent outer comparison in K25.
Its inner equal-gauge calculation does not identify the
outer endpoint maps. Its claim that the additional fixed
base's line is pulled back from a three-dimensional factor,
and hence has \(b^2=0\), is not established by that proof.

Independently, K47's exact arbitrary-GL2 determinant square
specializes to \(-1=0\) for this scalar loop. Thus the
simultaneous labelled delta-equivariant plumbing product
invoked in K29 Section 3 does not exist. This conclusion
retains all actual unit coordinates and labelled vertices;
it is not a restriction to diagonal normal derivatives.

## Granular dependency table

| Item | Exact dependence or retained proof | Required treatment |
|---|---|---|
| K25 whole-I1 nonfixed shears | Its extra normal-sphere boundary is assigned zero using the unmatched outer line | Withdraw that zero-boundary step and its C1/shear conclusion pending correction; preserve the earlier text |
| K29 Sections 1--2 | Integral common-exterior cells, meridians, dual bases and blowdown transfer | Retained; these do not use the scalar product |
| K29 Section 3 and initial variation claims | Entire three-curve labelled delta-equivariant product is invoked | The stated product is obstructed; initial rank-one variation and zero nonfixed derivatives require a new actual product/computation |
| K31 Sections 2--4 local frame arrows | First-resolution product-frame class, literal boundary flop, ambient frame change and normal reset | Retained as local maps in their stated actual product markings |
| K31 initial data and universal scalar-fan formula | Uses K29's rank-one variation and zero nonfixed derivative entries | Open/correction notice; the local algebra alone does not establish these initial data |
| F53 canonical scalar catalogue | Source pairs, root orders, cap topology and initial page values have independent proofs | Retain those fields; all_fan expressions and ranges inherit the K31 dependency |
| K35 weighted shorter scalar loops | Actual root/line/period descent and cyclic norm are explicit | Retain those maps and initial fixed-fan consequence; its all-fan application of K31 needs correction |
| K37 OS49 shorter loop | Actual threefold endpoint/cap/cusp map is explicit | Retain actual descent; its all-fan application inherits the separate OS49 product issue |
| K34 OS49 Section 6 | Claims a simultaneous delta-equivariant product and then the K29/K31 initial data | Audit its actual mixed-period determinant and outer marks separately; the whole-I1 calculation does not itself assign an OS49 correction |
| K17 OS49 flop | Uses a structurally similar extra-boundary pullback-line assertion | Audit its own outer fixed-normal arrows; do not infer its value merely from this whole-I1 example |
| K27 and K30 initial fixed-star pair | Actual page/trace and one fixed-star Cox normal map | Retain that scoped computation; it does not imply a simultaneous product of the three stars |
| K58 RG.1--6 geometric groupoid/dictionary | Actual source/root/Cartier/closing maps and loop relation | Retained independently of K25 |
| K58 RG.5/RG.7 initial/reflected scalar equality | Previously cited K25/K26 | Repaired directly by SCN.8's literal C2 native product, square and actual Cox map; SCN.9 supplies the narrow integer comparison |
| K58 RG.25 paired numerical values | Uses the preceding two-fan scalar equality and K57 local infinity values | Retain after the narrow SCN.8--9 comparison is audited; no universal fan formula is needed |
| K60 DZ.1--5 native C2 source-zero comparison | Uses K29's integral topology and K31's local single-star frame arrow, with its own explicit ordinary product | Retained; it does not invoke the obstructed scalar simultaneous product |
| K60 paired-sum corollary | Imports K58's numerical sum | Its dependence is repaired by the same narrow C2 result; no individual source-zero class is selected |
| K47--K55 source-loop ordinary products and trace formulas | Their non-equivariant products, actual chain prisms and local frame comparisons are constructed separately | The scalar obstruction does not invalidate those explicit constructions; do not replace their data by K29's scalar initial data |
| K53 unselected source-disc extension | Actual source/line/finite-cap extension across its disc | Unaffected; this is distinct from the catalogue F53 |

## Narrow two-fan repair

SCN.22--SCN.27 retain the exact C2 native product
\((a,b,c),(u,v,w)\), its closing seam, both small
resolutions and the full Cox map. For two turns with
scalar winding \(J\), the ordinary pair is \((-2J,0)\)
and the native pair is \((0,0)\). The doubled product
is literally pulled back from the single native product,
so its actual single right integer is zero in the free
relative group. The single Cox map therefore gives
equal initial/reflected sphere classes without division
in \(\Theta_7\).

The second outer C2 normal map is
\(\operatorname{diag}(\alpha^{-1},\kappa\alpha)\), with
base factor \(\kappa^{-1}\), and is independent of the
scalar parameter; the first is the identity. These
maps remove the omitted outer-marking problem for
this one comparison. They do not remove the C1 map
\(\operatorname{diag}(\eta/\alpha,\kappa\alpha/(g\eta))\).

The exact certificate is
code/part3/scalar_c1_outer_marking.py.
