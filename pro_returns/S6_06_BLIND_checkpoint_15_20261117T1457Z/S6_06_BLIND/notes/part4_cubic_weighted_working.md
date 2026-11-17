# Cubic pole section: the weighted-leading obstruction

## P4.53 candidate — awaiting independent audit

In the remaining positive ruled support, blow up the multiplicity-three image of the contracted horizontal section H, normalize the strict transform S1, and take its minimal resolution T1. The strict transform of H is exceptional over a point of S1. That point is an isolated normal simple elliptic singularity of the entire S1 germ. In particular H cannot dominate a curve in the ambient exceptional plane. No generic transverse type is imposed on the original critical curve.

### A. Exact degree and conductor reduction

Use the maps and notation of P4.52: D1 is the effective total conductor relative to omega(S1), n=ord_H(E)>0, a=coeff_H(D1). The pole identity is 2=n+a, so (n,a) is (2,0) or(1,1).

Suppose H dominates a reduced component L of the projective cubic tangent curve. At its generic point a transverse Weierstrass presentation has degree equal to the multiplicity m of that component in the cubic. Over the discrete valuation field of the transverse exceptional coordinate r, the equality of extension degrees gives

sum_H' ord_H'(r) [C(H'):C(L)]=m.                     (53.1)

This is the usual equality obtained by factoring the monic degree-m Weierstrass polynomial over the completed valuation field: its roots group into branches, each with the displayed ramification index and residue-field degree. Characteristic zero makes the residue extensions separable.

A positive-genus component of a cubic is a smooth elliptic cubic of multiplicity one. Its strict transform is smooth along that curve, with n=1 and a=0, contrary to 2=n+a. Every other reduced component is rational. A finite map from positive-genus H to such a component has degree h>=2. Thus n=2 is impossible in(53.1), since m<=3. We have n=1,a=1.

At a generic point of L the h points of H give h distinct normalization branches of the transverse plane germ, each with conductor exponent one. The exact plane-branch formula c_i=2delta_i+sum_{j≠i}I_ij forces h=2 and exactly two smooth transverse branches meeting once; there are no additional branches. Since each has r-order one, their total Weierstrass degree is two. Hence m=2. The tangent polynomial is y² ell, where y=0 is the double line and ell is a different linear form.

Choose complementary coordinates x,z, so the restriction ell(x,z) is nonzero. Absorb any y term in ell into the higher weighted part. Write r for the blowup's exceptional coordinate in a generic chart along the double line and v for its transverse coordinate. The generic strict-transform equation begins ell v²+r(f4|L)+... . A nonzero f4|L would give ramification order n=2 and residue degree one, which has just been excluded. Therefore f4 is divisible by y. The two transverse branches have intersection one, so after v=r u their two distinct leading slopes are roots of

ell u²+G3 u+G5=0,

where G3 and G5 are the respective degree-three and degree-five forms in x,z coming from yG3 in f4 and G5=f5|y=0. The discriminant Delta=G3²−4ell G5 is nonzero and nonsquare in C(P1), and the residue-field extension of H→L is exactly C(P1)(sqrt(Delta)).

Consequently the weighted leading polynomial of the original equation, for weights (1,2,1) on (x,y,z), is

P5=ell(x,z)y²+G3(x,z)y+G5(x,z).                     (53.2)

Its degree is five. There are no terms of smaller weighted degree. This identifies the normalized projective component of (53.2) birationally with H, rather than merely comparing genera.

### B. The projective curve and all transverse Milnor numbers

Let D be the reduced curve P5=0 in P(1,2,1). The quadratic polynomial is irreducible over C(x/z), since its degree-two residue extension is the connected cover H. Thus P5 has no factors except a possible common vertical factor of ell,G3,G5. Because ell is linear, the only alternatives are irreducible P5, or P5=ell Q4 with Q4 monic quadratic in y. Both are reduced.

In the irreducible case Delta is homogeneous of degree six. If its distinct zeros have multiplicities k_i, the smooth double-cover normalization has genus (#odd k_i−2)/2. Positive genus forces at least four odd multiplicities. Hence

sum_i(k_i−1)=6−#distinct zeros <=2.                 (53.3)

Away from ell=0 and the weighted vertex, completing the quadratic identifies the projective-curve germ exactly with w²−s^(k_i), times a unit. Its transverse Milnor number is k_i−1. At ell=0 there is no extra singularity: if G3 is nonzero then the finite root is simple and the other point lies at the weighted vertex; if G3=0, irreducibility forces G5≠0 and Delta has a simple zero. In the chart y=1, the weighted vertex is the quotient of C² by (x,z)↦(−x,−z); the lifted equation ell+G3+G5 has nonzero differential. The original polynomial also has nonzero derivative in the ell direction on the y-axis. Thus this point supplies no critical ray. We conclude that the total transverse Milnor-number sum M is at most two.

In the reducible case write G3=ell A2, G5=ell A4. Then Q4=y²+A2y+A4. Its discriminant has degree four. A positive-genus connected double cover requires four distinct simple roots, so its normalization is an elliptic curve and Q4 is smooth on the weighted plane. It avoids the weighted vertex. The remaining component ell=0 is rational and meets Q4 in total length two, read directly from the monic quadratic after restricting to that line. There are either two transverse intersections (two A1 points, M=2) or one tangency of order two (one A3 point, M=3). There are no other critical rays. Hence always M<=3.

The weighted plane has Euler number three: the strata x≠0, x=0,z≠0, and x=z=0 are C²,C,and a point. In the irreducible case e(D)<=e(H)<=0. In the reducible case e(D)=0+2−#(Q4∩ell)<=1. Thus

chi(P(1,2,1)\D)>=2.                               (53.4)

### C. The zero-form contradiction and the remaining point

The weighted scalar action with weights(1,2,1) and a primitive fifth root acts freely on F={P5=1}. Its quotient is P(1,2,1)\D: the only possible nontrivial stabilizer for the weighted C* action is at the weighted vertex, and that vertex belongs to D. Hence this is an unramified fivefold cover. A compact invariant core is obtained exactly as in P4.52. The character calculation for the free order-five action gives

rank(T−I)>=4 chi(P(1,2,1)\D)>=8.

The variation identity(4.52a) applies to every one-dimensional hypersurface critical locus, not just ordinary homogeneous ones. Its boundary mapping-torus bound is rank(T−I)<=M<=3 if the form is zero.

The form is zero here by the actual anisotropic scaling comparison: set D_epsilon(x,y,z)=(epsilon x,epsilon²y,epsilon z). Then epsilon^(−5) f(D_epsilon(x,y,z)) converges with all derivatives to P5. The compact-cycle flow of P4.52 embeds its pairings into the actual local Milnor fibre, whose form is zero by P4.51. The contradiction excludes every dominating H.

Thus H is exceptional over the normalized strict transform. Then a>0, so n=a=1. Its adjunction equation is 0=2g(H)−2+(D1−H).H. It gives g(H)=1 and no other positive pole component meeting H. A zero-coefficient exceptional curve cannot meet a positive-coefficient curve, by its own adjunction equation and the nonnegative canonical intersection on a minimal resolution. The connected exceptional fibre is therefore H alone and is disjoint from the strict conductor. The normalization is an isomorphism at its image; another analytic hypersurface branch would intersect this one in a curve and create conductor meeting H. Consequently the entire strict-transform germ at that image is normal and has a single smooth elliptic exceptional curve, namely an isolated simple elliptic singularity.

No assertion is made here that this last simple-elliptic point is excluded; it is the remaining contracted-H case to attack.
