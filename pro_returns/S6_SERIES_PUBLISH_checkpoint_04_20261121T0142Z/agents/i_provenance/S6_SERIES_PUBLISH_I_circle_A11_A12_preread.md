# Independent preread derivation: the integral circle quotient and its pointwise cusp limits

Targets: mapsI:src:A.1.1 and mapsI:src:A.1.2. Target statements only were opened; their proofs have not been read. Previously exposed inputs are the common marked period matrix, the explicit finite root deck convention, the standard unit-square cusp fan, and the primary basis comparison. The separate target night:P5.7 was inadvertently exposed by an extractor that omitted `remark`; no independence is claimed for that target.

## A.1.1: integral kernels, quotient, finite fillings

Use the displayed ordered basis (g,u,w,d). Solving (A1−I)v=(A2−I)v=0 gives v in Qd; since d is a primitive basis vector, the integral kernel is Zd. Solving the transposed systems gives Q gamma, hence integral invariant covectors Z gamma. This is also checked by a fresh exact symbolic calculation using only the displayed matrices.

The cusp vanishing lattice is im(M0−I)=Z d+Z w: M0g−g=−d and M0u−u=w. Any invariant subgroup containing it contains A1w=u−w, hence u. Therefore its invariant integral closure contains L=Z<u,w,d>. Conversely gamma A_j=gamma and gamma M0=gamma, so L=ker gamma is invariant. It is primitive because the surjective homomorphism gamma:Lambda→Z has that kernel. Thus it is the smallest invariant primitive subgroup required by the statement. The fresh Smith calculation of the six closure generators has three unit diagonal entries, independently certifying saturation.

On a regular fibre, Pi(z):Lambda_R→C² is an invertible real map. Its inverse identifies that fibre with Lambda_R/Lambda. The map x↦gamma(x) mod Z is a group epimorphism; every point r mod Z is the image of rg. Its fibre over zero is L_R/L because a representative with gamma(x) integral can be translated by that integer times g. This proves connected kernel and rank three. The period/deck covariance and gamma A_j=gamma make the formula independent of the marked lift of the base. The coefficients of Pi and its real inverse are real analytic, so this is a real-analytic map of the regular family.

On the j-th finite cover, the action is (s,x)↦(exp(−2pi i/m_j)s,A_jx+v_j/m_j), with (m_1,m_2)=(3,4). Its projection to the quotient base is exactly

    (s,r)↦(exp(−2pi i/m_j)s,r+epsilon_j/m_j),
    (epsilon_1,epsilon_2)=(1,−1).

The fresh exact computation gives A_j v_j=v_j and A_j^m_j=I, so the m_j-th iterate translates x by v_j in Lambda and is the identity on the torus. Every intermediate iterate shifts r by k epsilon_j/m_j, which is nonintegral for 0<k<m_j. Thus the cyclic action on the base disc times S¹ is free, including its core. Its quotient is the Seifert solid torus with the specified clockwise root convention, multiplicity m_j and translation residue epsilon_j. The map from the covered family to disc×S¹ is a smooth proper submersion with fibre L_R/L. The free finite quotient on the base has local sections; pulling the quotient map back by a section recovers this covered submersion. Hence the descended map is a smooth proper T³-bundle. All signs come from gamma(v_j), not an inferred unoriented Seifert invariant.

## A.1.2: the exact asymptotic character and all strata

Write the cusp period block as Z=s B0+C(q), where B0=[[0,1],[-1,0]], q=exp(2pi i s), and C(q) is holomorphic at zero. In the toric coordinates x_i=exp(2pi i zeta_i), put T=Im s=−log|q|/(2pi)>0 and y_i=Im zeta_i=−log|x_i|/(2pi). Real parts of the coefficients along the last two lattice columns have zero imaginary contribution. Therefore the coefficient gamma(x) of the first integral generator is the first entry of (Im Z)^(-1)y.

Since C is bounded, (Im Z)^(-1)=T^(-1)B0^(-1)+O(T^(-2)). The first row of B0^(-1) is (0,−1), so

    gamma(x)=−y_2/T+O((|y_1|+|y_2|)/T²).

In the chart q=z0 z1 z2, x1=z1,x2=z2, put b_i=−log|z_i|. On any relatively compact chart each b_i is bounded below, sum b_i=2pi T→+infinity, and |b_i|≤sum b_i+O(1). Thus the error is uniformly O(1/T), and the actual circle character has the same limiting behaviour as

    −b2/(b0+b1+b2) mod Z.

At a smooth point of W exactly one z_i vanishes. The ratio tends to 0 when i=0 or1 and to1 when i=2. Every case gives circle limit0. At the double curve z0=z1=0 with z2 nonzero, b2 stays bounded and the ratio tends to0. At z0=z2=0 with z1 nonzero, paths z0=r^a,z2=r^b, a,b>0, give −b/(a+b) mod Z, which varies with (a,b). At z1=z2=0 with z0 nonzero the same computation applies. At the triple point, paths z_i=r^{a_i}, a_i>0, give −a2/(a0+a1+a2), again with different limits.

The other triangle in the standard unit-square triangulation has vertices e1,e2,e1+e2. Its chart has q=z0 z1 z2, x1=z0 z2, x2=z1 z2. The same computation yields −(b1+b2)/(b0+b1+b2) mod Z. This varies on positive weighted paths into its triple point. Along the equal-height horizontal edge the limit is the integer −1; along its other edges it varies. The integer lattice translations identifying the triangles add an integer to the affine height, so the two horizontal edges define the one extendible double curve in the quotient, and the other two double curves are nonextendible. This identifies both triple points and all three double curves through the actual toric character, with the bounded C(q) term controlled uniformly.

Finally the direction d=e2 acts by (x1,x2)↦(x1,lambda x2) with q fixed. In the first triple chart it is

    (z0,z1,z2)↦(lambda^(-1)z0,z1,lambda z2).

Its fixed double curve is exactly z0=z2=0,z1 nonzero. The extendible curve z0=z1=0,z2 nonzero moves by z2↦lambda z2. These explicit maps prove the stated distinction and identify which curve fails pointwise extension; no categorical distinction is asserted without the maps.

## Scope and expected credit

A.1.1: full derivation and a supporting fresh exact kernel/Smith/finite-iterate computation, frozen together before reading its proof. A.1.2: full local asymptotic proof including the second cusp triangle and the fixed-action weights, frozen before reading its proof. The natural evidence unit is one targeted proof check per statement; the supporting A.1.1 computation is not counted again here. Neither result has yet been compared with its printed proof. No conclusion about the existence or homotopy class of a modified cusp map (A.2.1) is included.
