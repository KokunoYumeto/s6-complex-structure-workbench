# Sanity check: why B.4.33 does not exclude the untwisted Engel filling

**Date:** 15 November 2026. **Status:** exact comparison of the already constructed Part A family with the proposed B.4.33 obstruction. Requested by root during the final referee. No new independent theorem number is assigned.

## The linear local system does not distinguish the two cases

Over the ordinary base, the untwisted Engel two-tori have the same period matrix `Pi_c` and linear peripheral matrices `A1,A2` as the actual sphere family. The quotient `V=Lambda_Q/Q delta` consequently has the same zero common fixed space. In particular it would be wrong to explain Part A's proper filling by inventing a nonzero invariant vector in V.

The identities `Pi_(c-12)=Pi_c(I-12E)` and `[A_j,E]=0` hold for both families. The finite-order matrices are the Jacobian monodromy, which is unaffected by an affine logarithmic transform. They do not by themselves determine the family of affine torsors or its parameter-closing maps.

## The untwisted finite collars permit identity closing

For the untwisted family the finite logarithmic-transform vectors are zero. The period-family finite actions are linear, and the root-to-ordinary affine collars have `sigma_(j,c)=0` in these group presentations. More generally any base line-bundle frame factors are independent of c and hence of the degeneration logarithm. Therefore the identity Lie-coordinate map under `c -> c-12` is compatible with the finite root charts as well as the ordinary torus quotient. The actual Part A family is defined directly with the single-valued multiplier `u`, so this is also clear from its construction.

After `u=r^12`, the r-central twelve-cycle labels have no finite-place translation shifts. Their local transport around the two finite places and the cusp is `(0,0,0)`, unlike the sphere family's `(4,-3,-1)`. The ordinary scalar closing can be chosen as `K_untwisted=1`.

There can still be base-dependent changes of line-bundle frame: `O_S(P-O)` need not be globally rigidified along the zero section. Such changes are holomorphic units in the base and independent of r. They have zero radial-loop class and do not create a gamma contribution. Thus this comparison does not assume that the compact global C*-bundle itself has a globally chosen nonvanishing vector over its zero section.

## Why the same closing fails for the sphere twists

The sphere collars are instead

`sigma_(j,c) = w_j Pi_c v_j`, with `gamma(v_1)=1` and `gamma(v_2)=-1`.

If one attempted the identity ordinary closing under `c -> c-12`, its induced root-chart translation would be

`sigma_(j,c)-sigma_(j,c-12) = 12 epsilon_j w_j delta`.

In the coordinate `W=exp(-2 pi i zeta_2)`, this is multiplication by `s_j^(-12 epsilon_j)`: a pole at one root centre and a zero at the other. It is not an invertible extension of the finite-place family. The actual coherent sphere closing supplies the scalar `K(t)=t^4/(t-1)^3`; its root representatives `K s1^-12` and `K s2^12` are units. Their divisor orders on the marked base are `(4,-3,-1)`. The cusp order -1 is exactly the retained affine logarithmic-transform imbalance `p=-1` in the prescribed conventions.

This distinction is not removable by reusing the sphere closing in Part A: that closing, without the sphere collar corrections, has zeros or poles at the untwisted finite places and is not an automorphism of the untwisted completed family.

## The untwisted cusp has a common extending zero

The untwisted two-parameter cusp is the standard model built in A.1--A.2 with period multipliers `(q c1,c2)` and `(c3,u q c4)`. The ordinary toric zero `(Z,W)=(1,1)` extends simultaneously on both axes. In the unsubdivided node chart

`xy=u z v`, `q=zv`,

its section is explicitly `x=1`, `z=1`, `v=q`, `y=u q`. This lies away from the singular locus, so it lifts unchanged through the chosen smooth subdivisions and through normalized coordinate-root base changes. Any harmless period-unit or line-frame adjustment gives the corresponding unit section.

Choose this same origin on the two axial restrictions. Then `sigma_untwisted=o_untwisted` and the axial clutching section is `F_untwisted=0`. Its radial gamma label is zero. More generally an r-independent change of the two local frames gives an r-independent clutching section, again with zero radial gamma label.

For the sphere family the actual coherent parameter descent instead gives the sigma of B.4.9 and the corrected rotating origin of B.4.18. Their difference is the nonzero F of B.4.24, with radial period jump gamma. This exact F is part of the sphere affine data; it is not a formula for the untwisted family.

## Result of the stress test

The global-meridian and loop-invariance mechanisms are compatible with Part A: its extending local sections have normalized loop defect zero. The last B.4.33 contradiction does not arise because the untwisted clutching gamma class is zero, so the corresponding equality is `0=0`, not `0=Dn`.

The actual separation is therefore:

| Datum | Untwisted Engel family | Actual sphere family |
|---|---|---|
| Ordinary linear matrices | A1, A2 | A1, A2 |
| Common fixed space in V | zero | zero |
| Finite affine twist vectors | zero, zero | epsilon, minus epsilon-prime |
| Compatible radial scalar closing | 1 | K=t^4/(t-1)^3 |
| Cusp scalar order | 0 | -1 |
| Axial clutching radial gamma label | 0 | 1; n after r=R^n |
| Consequence | Proper toroidal fillings in A are consistent | Positive trace degree retains the B.4.33 obstruction |

The exact period, collar, divisor-order, and common-zero identities are checked in `code/ab_push_untwisted_sanity.py`, with saved output and JSON. This note uses the explicitly constructed Part A family and the fully audited C.3.5/B.4.19 formulas; it does not infer an affine filling merely from common linear monodromy.
