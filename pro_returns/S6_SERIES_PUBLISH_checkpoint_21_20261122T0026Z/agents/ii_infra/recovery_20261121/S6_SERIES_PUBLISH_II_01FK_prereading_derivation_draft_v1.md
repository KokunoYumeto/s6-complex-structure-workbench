# 01FK / cdp:st:C4a: derivation before target-proof release

Status: complete derivation on the smooth total-space domain of the cited conormal/index inputs; the original compact-complex-threefold wording has an unresolved scope question, kept separate. The target proof remains closed. The common analytic arguments are in S6_SERIES_PUBLISH_II_C4_prereading_common_arguments_v1.md and are part of this derivation's bound input set.

The supplied statement assumes connected f:Y->P1, b1=b2=0, smooth general two-torus, and the specified full-fibre class. It additionally requires the integral transgression generator to remain nonzero rationally on the normalization of every singular reduced full fibre.

1. The low-degree integral Leray sequence gives
0 -> H0(P1,R1f_*Z) --d2--> H2(P1,Z)=Z -> H2(Y,Z).
Here H1(Y,Z)=0 and R0f_*Z=Z, and the last group is finite. Therefore d2 is injective with a nonzero finite-index image dZ, and H0(R1f_*Z) is infinite cyclic. The cited D.1.9 construction sends its generator gamma to a coherent class beta in H1(Y,O), whose restriction to each full fibre is the coefficient image of gamma_c. Its fibrewise nonvanishing is part of that verified input.

2. Fix an arbitrary target Picard component P. In the component K_Y P^-1, construct a finite-order line T as in the common argument, and put A_r=T exp(2 pi i r beta), for real irrational r. Set L_r=K_Y A_r^-1; then L_r lies in P. The restriction of A_r to each full fibre is unitary flat.

3. Let S be a singular reduced irreducible normal-crossings full fibre. The required nonzero pullback eta^*gamma_S supplies a cycle with a nonzero integral period on its normalization. Hence eta^*A_r is a nontrivial unitary line for every irrational r. A unitary flat line on a connected compact complex manifold has a nonzero holomorphic section only when its character is trivial: the flat norm of such a section attains a maximum, and the local maximum principle forces a nonzero parallel section. Thus H0(tildeS,eta^*A_r)=0. The exact ambient-to-normalization isomorphism in current A.4.5 gives H0(S,Omega_Y^1|S tensor A_r)=0. In particular the use of the normalization map is explicit and is stronger than merely knowing A_r is nontrivial on S.

4. Every full smooth multiple fibre has the stated finite free cyclic torus cover. The full u-adic calculation in the common argument proves H0(mS,Omega_Y^1|mS tensor A_r)=0 through all m layers. For a regular torus fibre, gamma is nonzero and A_r is nontrivial unitary; the ordinary conormal sequence gives the same H0 vanishing. Therefore every full-fibre dual H2 group for T_Y tensor L_r is zero. The base-change, positive base twist and Picard semicontinuity argument gives generic H2(Y,T_Y tensor L)=0 in P.

5. No singular normalization can be rational: a rational smooth surface has H1(Q)=0, contradicting the specified nonzero eta^*gamma. Thus A.4.6 gives Euler number zero for every singular normal-crossings support. A smooth multiple support is a finite etale quotient of a torus, so has Euler number zero as well; the multiplicity does not change the underlying topological space. Euler characteristic of the proper fibration, decomposed into the regular base and finitely many critical points, is consequently zero. Chern--Gauss--Bonnet on the smooth total space gives c3(Y)=e(Y)=0.

6. The common primary generic-vanishing argument gives H0 and H3 zero on a dense open subset of P. Intersect with the H2 vanishing locus. The index is c3/2=0, hence 0=chi=-h1 there. All four cohomology groups vanish. P was arbitrary. No tangent-cohomology vanishing assumption was inserted into the fibre hypotheses.

Every exact morphism used above is specified: the coefficient image gamma->beta, normalization pullback, finite etale pullback with u-adic layers, full-fibre residue/duality, projection formula, and the Picard-component preserving base twist. No claim about a singular total space has been established or refuted by this draft.
