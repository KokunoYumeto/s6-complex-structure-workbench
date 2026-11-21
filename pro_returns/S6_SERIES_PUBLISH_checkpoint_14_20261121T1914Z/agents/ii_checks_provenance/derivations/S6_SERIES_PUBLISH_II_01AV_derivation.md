# Derivation before target proof: 01AV

Owner `cdp:st:A.4.6`; checker `i_provenance`. Exact target and the full supplied
A.4.4/A.4.5 statements are read. The A.4.5 derivation is independently written
before release. No target II proof or old program has been opened. The exact
Schroeer--Siebert Proposition 2.6 was read in the primary author PDF as a
classification input, with its two point blowups and conductor hexagon.

For normalization eta:T->S, let C be its conductor curve and D its image.
The finite map is an isomorphism T\C -> S\D. Additivity of topological Euler
characteristic for the compact complex analytic stratification gives
e(S)=e(T)-e(C)+e(D). This uses the actual normalization map and no equality
of the separate spaces.

In the elliptic ruled case, T is a P1 bundle over an elliptic curve, so e(T)=0.
C consists of two disjoint elliptic curves and D is one elliptic curve;
both Euler numbers are zero. In the Hopf case, a finite cover of T is
S1 times S3, so e(T)=0; its conductor and image are again respectively two
and one elliptic curves, giving zero.

In the rational case Proposition 2.6 gives a Hirzebruch surface with two
point blowups, hence e(T)=4+2=6. The conductor C is a cycle of six P1's with
six distinct ordinary nodes, so e(C)=12-6=6. Pairs of its six components
are identified to give three rational components of D. Each triple point
has three preimages among the six conductor nodes; therefore there are two
triple points. The normalization of D is the three P1's, and at each triple
point three points are replaced by one. Thus e(D)=6-2(3-1)=2 and e(S)=2.

A compact torus fibration has only finitely many critical values. Its smooth
part is a locally trivial differentiable fibration with fibre Euler number
zero. Additivity and multiplicativity for the finite stratification make
e(Y) the sum of the Euler numbers of its special underlying fibres. Scheme
multiplicity leaves the underlying topological fibre unchanged; the smooth
supports allowed in the statement have Euler number zero. Hence e(Y)=2r.
For the smooth compact complex threefold, the complex orientation and
Chern-Gauss-Bonnet identify the Chern number c3(Y) with e(Y). Poincare duality
under b1=b2=0 gives e(Y)=2-b3(Y). Nonnegativity of b3 and r gives r=0 or1
and b3=2-2r, as stated.

All finite Euler calculations are exact incidence counts. The source
classification URL is https://www.math.uni-duesseldorf.de/~schroeer/publications_pdf/kodaira.pdf .
