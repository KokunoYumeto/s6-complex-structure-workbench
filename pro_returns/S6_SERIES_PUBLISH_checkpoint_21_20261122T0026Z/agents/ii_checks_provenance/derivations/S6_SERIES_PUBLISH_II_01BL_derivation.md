# Derivation before target proof: 01BL

Owner: `cdp:st:B2`. Checker: `i_provenance`.
The exact target and cited B1 statements and empty supplement have been read.
No target proof, prior target check, or old target program has been opened.

Write a(t)=t^4+1 and b(t)=t^6. The Weierstrass discriminant, up to its
nonzero scalar unit, is 4a^3+27b^2=D(t). The displayed changes of x,y extend
the equation to the projective bundle with fundamental line O(1), hence
define a projective surface. At infinity its coefficients are 1+s^4 and 1,
and its discriminant at s=0 is 31, so that fibre is smooth.

Put u=t^4 and P(u)=31u^3+12u^2+12u+4. The exact identity
3P-uP'=12(u+1)^2, together with P'(-1)=81, excludes common roots of P,P'.
Also P(0)=4. Thus D has twelve distinct, finite, nonzero roots. P(-1)=-27
shows a(t) is nonzero at each root; b(t) is nonzero there as well. The singular
cubic therefore has one double and one simple root, and is irreducible nodal.
For a node at (x,y)=(r,0), one has a=-3r^2,b=2r^3 with r nonzero. Its plane
Hessian is diag(-6r,2), so its two branches are transverse. Differentiating
the discriminant at such a point gives
D'=108r^3(r a'+b'). Since D' is nonzero, the t-partial of the total equation
is nonzero. Thus the total space is smooth at every node. At the zero section
[0:1:0], the z-partial of the homogeneous equation equals one, and all other
points are smooth on a smooth fibre. This proves smoothness of E everywhere.

The section P is disjoint from O. On a nodal fibre it is smooth because its
y-coordinate t^3 is nonzero, whereas the node has y=0. Consequently M=O(P-O)
is a nontrivial degree-zero line on every smooth or nodal genus-one fibre.
Here the Abel map from the smooth locus with origin O to Pic^0 of the integral
genus-one curve sends P precisely to this line. Its nontriviality can also be
seen explicitly at a node: the normalization parameter v=y/(x-r) satisfies
x=v^2-2r, and the two node preimages are +/-sqrt(3r). At P, v^2=2r. The gluing
parameter is (q-1)/(q+1), or its inverse, with q^2=2/3. Thus it satisfies
lambda^2+10lambda+1=0. Its roots are real and different from +/-1, so the
nodal restrictions are in fact non-torsion. The newly written coefficient
program verifies the discriminant identities and this elimination exactly.

Every degree-zero nontrivial line on an integral smooth or nodal genus-one
curve has h^0=h^1=0: a nonzero section would have effective divisor of degree
zero and trivialize the line, while Serre duality uses the trivial dualizing
line. Proper base change then gives Rh_*M=Rh_*M^(-1)=0.

The invariant differential dx/(2y) transforms by s^(-1) at infinity. As a
relative dualizing generator it extends over the nodes and the zero section;
therefore omega_(E/P1)=h^*O(1) and K_E=h^*O(-1). Let Z be the reduced set of
the twelve nodes in the smooth total surface. The relative cotangent quotient
fits in the exact sequence

0 -> h^*Omega^1_P1 -> Omega^1_E -> I_Z tensor omega_(E/P1) -> 0.

At a node choose total-space coordinates p,q with t-t_i=pq times a unit,
absorbed in p. The map from relative differentials to the dualizing line
sends dp to p eta and dq to -q eta. Its image is (p,q) eta and its kernel is
the relation q dp+p dq; these are the exact local maps giving the sequence.
Away from Z it is the usual smooth cotangent sequence.

Tensor by M^(-1). Both Rh_*(h^*Omega_P1 tensor M^(-1)) and
Rh_*(omega_(E/P1) tensor M^(-1)) vanish by the preceding fibre calculation.
The sequence 0->I_Z N->N->N|Z->0, N=omega_(E/P1) tensor M^(-1), then gives

Rh_*(Omega^1_E tensor M^(-1)) = (direct sum_i C_(t_i))[-1].

Each length is one because O_(E,Z)/(p,q)=C at the simple node. The possible
choice of scalar trivialization of N at each point explains the noncanonical
one-dimensional identifications; support and length are canonical.

Now use the actual product Y=E times P1. Contraction with the canonical
two-form gives T_E tensor K_E=Omega^1_E. Hence the stated sheaf Ecal splits as

(Omega^1_E tensor M^(-1)) external O_P1(-2)
direct-sum (K_E tensor M^(-1)) external O_P1.

The second summand has zero derived h-pushforward. The first has the extra
cohomological shift from H^1(P1,O(-2))=C. Thus Rg_*Ecal is the direct sum of
twelve residue fields placed in degree two, exactly as claimed, and no other
direct image occurs.

For a nodal fibre S=C times P1, the conormal is O_S because it is the full
reduced fibre. The line A in the statement equals M|C external O. Thus its
first endpoint vanishes. The torsion-free cotangent sheaf of the nodal curve
is nu_*Omega^1_P1, as follows at the node from the two branch differential
maps; its normalization pullback of M is trivial. Both summands of the
torsion-free cotangent on C times P1 therefore have no global sections after
this twist: the first uses H^0(P1,O(-2))=0, and the second uses the same
P1 differential and H^0(C,M)=0. This proves the second endpoint vanishing.

Derived base change for the vector bundle Omega_E tensor M^(-1) gives its
cohomology on C from C_(t_i)[-1] tensor^L C_(t_i). The two-term resolution
O --(t-t_i)--> O becomes the zero differential after tensoring, producing
one-dimensional H^0 and H^1 on C. Kunneth with O_P1(-2) shifts these to
H^1,H^2 on S, while the second product summand vanishes. Therefore the
restriction tuple is (0,1,1). Finally Leray for the degree-two skyscraper
direct image yields global dimensions (0,0,12,0).

This proof keeps the actual restriction maps and the length-one local
modules; fibre dimensions alone were not used to infer the direct-image
lengths. All computational inputs are newly checked. Target-proof comparison
and comparison with the old computational method remain pending.
