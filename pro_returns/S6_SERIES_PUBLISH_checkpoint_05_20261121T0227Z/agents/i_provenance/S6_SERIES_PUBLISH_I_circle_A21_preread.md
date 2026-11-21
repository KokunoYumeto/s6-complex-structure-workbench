# Independent preread derivation: a smooth cusp replacement and its relative homotopy class

Target: mapsI:src:A.2.1. The target statement and its cited input `mapsI:quotient-eq-5` have been read; the target proof has not been opened. A.1.1–A.1.2 were independently derived and frozen before their printed proofs, which have now been compared. The input eq-5 is an unnumbered proved paragraph: the smooth cusp neighbourhood N has pi_1(N)=Lambda/K, and the punctured-cusp inclusion kills K and the base meridian. Its explicit toric argument was visible as an input. This record does not claim preread independence for that input paragraph.

Choose a closed sufficiently small cusp neighbourhood N=f^(-1)(disc), with a connected outer collar A. Its boundary is the connected torus mapping torus over the boundary circle, so A is connected; N is connected as well. Fix the target gluing. In the designated regular solid torus, the target is the product of the cusp disc with S¹. The prescribed map on A has first coordinate f and circle coordinate chi with homomorphism gamma on the period lattice and zero on the base meridian.

By eq-5, gamma kills exactly the relations K and the base meridian used to pass from pi_1(A) to pi_1(N). Thus it defines an integral class alpha in H¹(N;Z) restricting to [chi]. The restriction H¹(N;Z)→H¹(A;Z) is injective, since pi_1(A)→pi_1(N)=Lambda/K is surjective. This is the exact morphism used below.

Represent alpha by a smooth closed real one-form omega with integral periods. On the connected manifold N, the formula

    h0(p)=exp(2pi i integral from p0 to p of omega)

is independent of the chosen path and defines a smooth map to S¹. Its integral H¹ class is alpha. On the collar the quotient h0/chi has zero integral periods, hence has a single-valued smooth real logarithm phi with h0/chi=exp(2pi i phi). Choose a smooth cutoff rho supported in the collar, equal to one near its outer part. The map h=h0 exp(−2pi i rho phi) is smooth on N and equals chi on that outer collar. Therefore (f,h):N→disc×S¹ agrees exactly with the literal quotient near the gluing boundary. Joining it to the literal quotient outside N gives the required smooth map e_q:X→Q over B. Shrinking the cusp disc before this construction gives agreement outside an arbitrarily small cusp neighbourhood.

For uniqueness, let h0,h1 be any two circle coordinates of replacements into this same designated solid torus, with the same prescribed outer collar value. Their ratio h1/h0 is one on A. The induced homomorphism on pi_1(A) is zero, hence its homomorphism on pi_1(N) is zero by the preceding surjectivity. Therefore the ratio has a global smooth real logarithm phi. Since it is identically one on the connected collar, phi is a constant integer there; subtract that integer to make phi zero on A. The explicit homotopy

    h_t=h0 exp(2pi i t phi),  0≤t≤1,

stays in S¹ and is fixed on A. Pairing it with the unchanged map f gives a homotopy through maps to the designated solid torus over B, and extending it by the fixed literal quotient outside N gives the required global homotopy. Equivalently the exact sequence for (N,A), using connectedness and the injective H¹ restriction, gives H¹(N,A;Z)=0, but the explicit logarithm supplies the actual homotopy map.

This argument applies to the existing cusp neighbourhood of every admissible member and requires no sphere identification. For the original member X≃S6 it therefore supplies the stated well-defined class. It makes no global circle-valued extension assertion: the globally glued codomain is the already fixed three-manifold Q, with the designated product solid torus only over the cusp disc.

Expected scope: the full target statement, including the exact over-B condition, arbitrarily small support, fixed gluing, image restriction and relative collar homotopy. One targeted proof check after comparison; no new independent credit for the already read input eq-5, and no separate computational event.
