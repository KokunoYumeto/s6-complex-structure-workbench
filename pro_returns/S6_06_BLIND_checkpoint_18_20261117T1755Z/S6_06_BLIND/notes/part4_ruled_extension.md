# Smooth ruled normalizations: completion of the numerical sign

## P4.21 (Proved). Smooth rational normalization has positive Euler number

In the setting of Part 4.2, an irreducible singular support S with smooth rational normalization T has e(S)>0.

**Proof.** Let D be the conductor divisor and C=Sing(S)_red. We have K_T+D numerically trivial by P4.12. Contract T to a minimal rational surface T0 and push D forward to D0. At every reversed blowup, the exceptional coefficient is μ−1, where μ is the multiplicity of the current conductor at the centre. In particular every centre lies on the conductor.

We record the precise alternatives for D0. On P2 it is a plane cubic. An irreducible cubic is either a smooth elliptic curve, a rational nodal cubic, or a rational cuspidal cubic. A reducible cubic is a smooth conic and a line, three lines, a double line and another line, or a triple line. A conic and line meet in two distinct points or are tangent; three distinct lines form a triangle or are concurrent. Thus either D0 is reduced with only ordinary nodes and its reduced support has fundamental group Z or Z2, or its reduced support is simply connected and all its normalized components are rational. Here Z2 means Z^2, not Z/2.

On a Hirzebruch surface, let F denote a ruling fibre. Since D0.F=2, its horizontal part is a double section, two distinct reduced sections, or a reduced irreducible bisection. A double section with vertical fibres is a rational tree and is simply connected. Write the other two possibilities as

    D0=H1+H2+Σ a_j F_j,  or  D0=H+Σ a_j F_j.

In the first case adjunction on either section gives

    H1.H2+Σ a_j=2.

The two sections and the vertical fibres therefore form a rational tree or a single rational cycle. A cycle occurs only when all coefficients equal one and all its intersections are ordinary double points. In the second case adjunction gives

    p_a(H)=1−Σ a_j.

Hence either there is no vertical fibre and H has arithmetic genus one, or there is one vertical fibre of coefficient one and H is a smooth rational bisection. In the first alternative H is smooth elliptic, rational nodal, or rational cuspidal. In the second it meets the vertical fibre in two distinct points or in one tangency point. Once again the only nontrivial fundamental groups are Z and Z^2, and those alternatives have a reduced nodal divisor. These computations include the possibility that the two section-intersection points coincide, or that a vertical fibre passes through their intersection: those configurations give trees, not additional cycles.

We now follow the blowups. At a conductor point of multiplicity at least two, the exceptional P1 belongs to the new conductor and its contraction has connected simply connected fibre. Replacing the local branch-identification point by this P1 induces an isomorphism on fundamental groups, as follows directly from van Kampen on small neighbourhoods. At a point of conductor multiplicity one, the conductor is smooth and reduced and its strict transform is isomorphic to it. Thus the fundamental group of D_red is unchanged throughout. If the initial alternative has nontrivial fundamental group, its divisor is reduced nodal; a smooth-point blowup adds no conductor component and a node blowup inserts an exceptional component of coefficient one between the two branches. It stays reduced nodal at every step.

In this latter alternative every generic transverse conductor exponent is one. A reduced plane-curve germ having conductor exponent one on a branch has two smooth branches meeting transversely: a singular branch has intrinsic conductor exponent at least two, and intersections with other branches add to that exponent. Thus S has ordinary double curves away from finitely many points. P4.20 applies to the smooth normalization and proves that S is normal crossing everywhere. P4.6–P4.8 give e(S)=2 for its rational normalization.

In the remaining alternative, D_red is connected and simply connected, and every component of its normalization is rational. The topological conductor pushout, proved in P4R.3, gives

    π1(S)=π1(T)*_{π1(D_red)}π1(C)=π1(C).

Each component of C has rational normalization, because it is the finite nonconstant image of some rational component of D_red. P4R.1 makes π1(C) virtually abelian. For a connected curve with rational normalized components this group is a free group of rank b, where b is the first Betti number of its point-identification graph. A free group is virtually abelian only for b≤1. If c≥1 is the number of components, therefore

    e(C)=c+1−b≥c≥1.

Finally P4.13 gives e(S_reg)≥0, and additivity gives e(S)=e(S_reg)+e(C)>0. This proves the assertion in both alternatives. ∎

## P4.22 (Proved). Smooth elliptic-ruled normalization

In the setting of Part 4.2, an irreducible singular support S whose smooth normalization T is birationally ruled over an elliptic curve has e(S)≥0. Equality holds exactly when T is minimal.

**Proof.** Again K_T+D is numerically trivial. Push the effective conductor to the minimal ruled surface T0 over the elliptic curve B. If a horizontal component H has coefficient one, adjunction gives p_a(H)≤1, whereas its nonconstant map to B gives geometric genus at least one. Thus H is smooth elliptic and (D0−H).H=0. There is no vertical component, and the horizontal part is either one elliptic bisection or two disjoint elliptic sections, all with coefficient one. All subsequent blowups are at smooth coefficient-one conductor points; their exceptional curves are absent from the conductor. The conductor remains a disjoint union of smooth elliptic curves with coefficient one. The normalization differential has no divisorial rank drop. P4.15 then makes T minimal, makes the differential immersive everywhere, and gives e(S)=0.

The other possibility is

    D0=2H+Σ a_j F_j,

with H a smooth elliptic section. The same blowup calculation as P4R.3 shows that D_red is H with rational trees attached and that π1(D_red)→π1(T) is an isomorphism. The conductor pushout and P4R.1 therefore make π1(C) virtually abelian. The reduced-curve calculation in P4R.3 gives e(C)≥0. Together with P4.13 this proves e(S)≥0.

Suppose e(S)=0. Then e(C)=0, so C has just one component, its smooth normalization has genus one, and it has no branch-identification cycles. Every conductor component maps finitely and nonconstantly to C. Riemann–Hurwitz excludes rational conductor components. Thus D_red=H and no blowup occurred: the first blowup on 2H would create an exceptional conductor component of coefficient one. Therefore T is minimal.

Conversely suppose T is minimal. In the displayed double-section alternative, if v distinct vertical fibres occur then

    e(S_reg)=e(T\D_red)=−v,

because e(T)=e(H)=0 and each vertical P1 meets H once. P4.13 forces v=0, so D=2H. At a general point of its image curve, each normalization branch has conductor exponent two. For a reduced plane curve, the exponent on one branch is its intrinsic conductor exponent plus the sum of its intersection multiplicities with the other branches. A singular branch has intrinsic exponent at least two. Consequently either there is a single ordinary cusp branch, or all branches are smooth and there are two branches tangent to order two, or three branches meeting pairwise transversely. This is an exhaustive list: a singular branch together with another branch would have exponent greater than two, and four smooth branches would have exponent at least three.

In the cusp alternative the finite map H→C has generic degree one, so the smooth normalization of C is H itself. Since π1(C) is virtually abelian and H is elliptic, the curve has no additional point-identification graph cycles. Hence e(C)=0 and e(S)=e(T)−e(H)+e(C)=0. In the other two alternatives the normalization differential is immersive along the generic point of H. There is no other conductor component, so its failure-of-immersion set is finite. P4.15 applies and gives e(S)=0. We have proved both directions of the equality statement. ∎

Together with P4R.3, these statements establish the numerical sign for every smooth ruled normalization. They do not yet supply the full asserted irreducible-fibre classification, the class-VII case, or arbitrary singular normalizations.
