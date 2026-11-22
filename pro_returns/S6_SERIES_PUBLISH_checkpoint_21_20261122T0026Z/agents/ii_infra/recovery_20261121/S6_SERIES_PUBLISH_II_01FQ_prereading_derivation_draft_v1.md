# 01FQ / cdp:st:C4g: derivation before target-proof release

The target proof remains closed. This argument concerns the actual smooth constructed families in its statement, with their stated admissible parameters. The common analytic arguments are in S6_SERIES_PUBLISH_II_C4_prereading_common_arguments_v1.md.

## Actual geometry and topology inputs

The original admissible (3,4) affine-twist input E19, supplied as an exact cited-source statement in the immutable supplement, gives nonzero p and rational homology of S6, including every |p|>1. It does not turn their integral torsion groups into zero. The current-I fixed-fan definition supplies the reduced full hexagonal fibre and smooth root torus covers of multiplicities three and four.

For the two-parameter family, the public v1 Two PDF p6 equation(3.1)/Proposition3.1 gives the three reduced irreducible Mumford fibres, with normalization dP6 at the hexagonal value and elliptic ruled normalizations at the other two. Its public pp19-20 Proposition6.4 gives the proper holomorphic submersion over the parameter bidisc, with fixed four-torsion affine quotient at the remaining multiple value. The source Theorem labelled sphere, lines1310-1333, and the actual p20 statement give the integral sphere topology for all these members by the specified family transport. The checker read those source lines and the complete public p19/p20 images.

For the Liu--Rollenske family, the supplied construction and the already released complete E14 cited input give one reduced full hexagonal fibre, one reduced cuspidal fibre, and the smooth fourfold root torus quotient. The primary source S6_arxiv.tex, lines1672-1725, was opened at the integral-homology corollary and the sphere theorem, including the complete first-assertion proof. These constructed manifolds are smooth and have the integral homology of S6. No singular-total-space extrapolation is involved.

## The line on the normalization

In all three actual families, b1=b2=b3=0 rationally. Thus c1(L) is torsion for every ambient line L. Pullback along eta:dP6->Y lands in torsion-free H2(dP6,Z), so c1(eta^*L)=0. Since H1(dP6,O)=0, the exponential sequence supplies eta^*L isomorphic to O. Apply this to K_Y^-1 L. After a trivialization, Serre duality gives
H2(dP6,K_dP6 tensor eta^*(K_Y^-1 L)) = H0(dP6,O)^dual = C.
This proves the specified dimension-one target with an explicit line-bundle identification.

## Euler numbers

The reduced full hexagonal fibre has Euler number two by the specified dP6 hexagon gluing, equivalently current A.4.6. Each rank-one Mumford fibre has ruled elliptic normalization; both its two boundary sections and their identified elliptic image have Euler number zero, and the normalization itself has Euler number zero. Hence the fibre Euler number is zero. The cuspidal support in the LR construction is locally the cuspidal rational curve family over an elliptic curve; its normalization and conductor strata have Euler number zero, so the same normalization/conductor additivity gives zero. The smooth multiple supports are finite free quotients of tori and have Euler number zero. The resulting lists are respectively (2), (2,0,0), and (2,0), with the stated multiplicities (3,4),4,4 at the other critical values. The full nonreduced scheme has the same underlying topology as its reduced support.

## Every smooth multiple passes the ambient test, including |p|>1

Choose a finite-order representative in each Picard component and the real irrational transgression twist. D.1.9 applies because b1=b2=0; it does not require integral H2=0. Pull back to the actual finite free cyclic torus cover near a smooth multiple fibre. The pulled-back full fibre is mT with normal coordinate u. Its every ideal-power layer is the same nontrivial unitary line tensored with Omega_tildeY|T, whose conormal sequence has the three trivial torus summands. All H0 groups vanish. The precise u-adic filtration and faithfully flat descent in the common argument therefore prove ambient H0 zero on the entire mS. Proper semicontinuity and the finite list of multiple values give the simultaneous generic vanishing locus in every Picard component.

This directly proves the test asserted by the reference to A.3.4 for these actual examples. In particular it avoids applying that proposition's integral-CDP hypotheses to the |p|>1 members, whose integral cohomology has torsion.

## Global tangent cohomology

The nonzero normalization target does not by itself specify the rank of the global restriction map. Instead, current C.1.3 applies directly: these smooth compact Y have b1=b2=b3=0 and the nonzero effective Cartier divisor given by a fibre. Its pointwise conclusion is h2(Y,T_Y L)>=1 for every ambient L. This proves the final assertion for all twists, without a surjectivity assertion about their normalization map. The reduced full hexagonal fibre already supplies the displayed normalization obstruction, while every smooth nonreduced critical fibre passes the generic ambient test above.
