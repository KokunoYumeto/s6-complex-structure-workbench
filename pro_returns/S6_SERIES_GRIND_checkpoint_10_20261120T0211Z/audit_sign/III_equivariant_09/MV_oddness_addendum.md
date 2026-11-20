# Exact mod-two Mayer–Vietoris detector

This is the post-freeze clarification requested by root after reading the receiving proof. The frozen corrections text's bare nonzero order-two-image sentence requires this extra argument. My receiving report used the exponent-two boundary torsion recorded in D.GC3; the direct argument below supplies the actual map and avoids relying only on that group-size statement. Both original freezes remain byte-for-byte unchanged.

Let M be the actual cusp boundary, A0 the exact D.PC5 matrix, R=Lambda^2 A0-I, and alpha=e1 wedge delta. Use the ordered basis(e1e2,e1delta,e1gamma,e2delta,e2gamma,deltagamma). The integral Wang sequence is

    0 -> C=coker R -> H2(M;Z) -> K=ker(A0-I on Z4) -> 0.

K is a subgroup of Z4 and hence free. Tensoring with F2 therefore preserves the injection C tensor F2 -> H2(M;Z) tensor F2. Since A0=I mod2, R is zero mod2. Thus C tensor F2 is the actual six-dimensional quotient Z6/(RZ6+2Z6)=F2^6, and alpha maps to its nonzero second basis vector. Universal coefficients inject H2(M;Z) tensor F2 into H2(M;F2). These are the exact maps carrying alpha to a nonzero mod-two class.

The physical compact SU2 sphere crosses M in the degree-one short torus, so its integral Mayer–Vietoris connecting image is +/-alpha. Coefficient reduction commutes with that connecting map, being induced by the same singular-chain restriction/difference maps. Therefore the mod-two class represented by N has nonzero boundary alpha mod2. If the integral class of N were in 2H3(X;Z), its coefficient reduction would be zero, contradicting this boundary. Since H3(X;Z)=Z/8, the class of N is odd.

There is also a complete explicit integral splitting behind D.GC3. Put

    v=(-12,8,4,-8,0,-3).

Directly, R has image 2<alpha,v>: its nonzero columns are -6alpha,-16alpha,8alpha,2v,-24alpha, and 2alpha=R(e1e2+e2delta). The two functionals

    f_alpha(z)=z_1-8(z_2+z_5),
    f_v(z)=z_2+z_5

(with zero-based indices) give a left inverse to the ordered inclusion(alpha,v). Thus <alpha,v> is a primitive direct summand of Z6, C=Z4 plus(Z/2)^2, and the actual H2(M)=Z6 plus(Z/2)^2. This proves the claimed exponent-two image bound by an explicit splitting, not by an abstract order argument. Its alpha-coordinate mod2 is a detector extending across the free Wang quotient; any such extension takes alpha to one.

The direct mod-two argument is sufficient for the published proof. It changes none of the collar, Borel, reference-frame or critical-link computations; it supplies the precise missing step in the frozen receiving text.
