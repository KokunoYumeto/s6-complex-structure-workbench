# Paper V: derivations recorded before the corresponding printed proofs were read

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation, 19 November 2026.

Only the statement environments and their displayed input definitions have been extracted. The standalone proofs and the prior checking programs have not been read for the rows below at the time this file is first written. This is an evidence record; completion of a derivation is assessed only after comparison and any needed computation.

## maps:src:F.1.1

Stratify the base into the exceptional points and their complement. Additivity of compactly supported Euler characteristic for the proper triangulable map gives the sum of base-stratum Euler characteristic times fibre Euler characteristic. A positive-dimensional real torus has Euler characteristic zero; the same holds for its free finite quotients since the covering degree multiplies Euler characteristic. In the toric central fibre, every positive-dimensional torus orbit likewise has Euler characteristic zero. Its zero-dimensional strata correspond to maximal simplices of the periodic rank-three Kuhn triangulation. A unit cube contains the six simplices indexed by permutations of its three coordinate directions; a period fundamental domain consists of d cubes. Thus there are exactly 6d zero-dimensional strata and the Euler characteristic is 6d. This derives the asserted value once the term 'Kuhn toroidal fibre' has precisely this periodic stratum incidence.

## maps:src:F.1.4

Choose a real representative b of the torus translation. Since det(I-A) is nonzero, x=(I-A)^{-1}b satisfies Ax+b=x already in R^n, and hence defines a fixed point in R^n/Z^n. This exact inverse solves the fixed point equation for every b. It supplies the asserted obstruction for each matrix with no eigenvalue 1.

## maps:src:F.2.1

Put N=U-I. The index-one hypothesis must mean N^2=0, rank N=3 and im N=ker N as integral sublattices. Let a_1,a_2,a_3 be a basis of the saturated kernel and choose b_i with Nb_i=a_i. The six vectors form a lattice basis: their images b_i in the quotient map isomorphically under N onto the kernel. The basis (a_1,a_2,a_3,b_1,b_2,b_3) gives the stated matrix. For a general block matrix [[P,Q],[R,S]], equating XN and NX gives R=0 and S=P. Its determinant is det(P)^2, so integral invertibility is equivalent to P in GL_3(Z), while Q is arbitrary integral. The converse commutation follows by the same multiplication.

## maps:src:F.2.2

A finite-order integral matrix is semisimple in characteristic zero. Its rational characteristic polynomial is a product of cyclotomic polynomials with total degree 6. The preceding affine obstruction forces a Phi_1 factor. Enumeration can be performed by solving sum m_d phi(d)=6 with m_1>=1. All eligible d have phi(d)<=6, and the m_1 constraint excludes degree-six factors. The order is lcm of d with m_d>0. A commuting real complex structure is equivalent to even multiplicity of each real eigenvalue: m_1 and m_2 are even. Each irreducible pair of nonreal conjugate eigenspaces already admits multiplication by i. A new enumeration will test the printed counts 38 and 19 without reading the original enumeration program.

## maps:src:F.2.3

Keep a fixed boundary torus bundle and its monodromy, affine translations and boundary collar. Inside a filling choose an embedded 8-ball and form its interior connected sum with S^4 x S^4. This leaves the entire collar and peripheral gluing map unchanged. Excision and the Mayer-Vietoris sequence for the connected sum give H_4(new filling)=H_4(old filling) direct sum Z^2, and the same extra summand persists after the fixed exterior is attached. Thus the peripheral data by themselves admit fillings whose glued homology differs by Z^2 in degree four. The statement concerns unrestricted fillings; the specified Kuhn filling removes this freedom.

## maps:src:F.3.1 and maps:src:F.3.2

Write V=R^1g_*Q, with generic rank 6, finite-point invariant ranks r_i and cusp rank 3. For these local models, the finite stalk is the invariant cohomology of the torus; for the index-one cusp its H^1 is the invariant rank-three part. Put a=dim H^0(V) and b=dim H^0(V^*). On the base sphere the sheaf Euler characteristic is 12-(6-3)-sum_i(6-r_i)=9-6k+sum_i r_i. Duality for the invariant extension gives H^2(V) dimension b. In Leray, the only differential from H^0(V) is d_2 to H^2(B,Q). Since b_1(M)=b_2(M)=0, this is an isomorphism, so a=1. The group H^1(V) survives and must vanish. Consequently the Euler characteristic is a+b=1+b and sum_i r_i=6k-8+b. A common invariant covector restricts to the cusp invariant space, so 0<=b<=3. Each finite holomorphic quotient has even r_i, from its invariant real complex structure. Hence b is even, so b is 0 or 2. For k=2 or 3, enumerating the even ranks 2,4,6 in the displayed sum gives exactly the stated pairs/triples (assuming free finite action forces r_i>=2). Self-duality yields b=a=1, which makes the right hand side odd while the left hand side is even, a contradiction. This derives the parity obstruction with the exact sheaf maps requiring verification in the printed proof.

## night:P1.4

For f=x^5+lambda^3 x+lambda^4, a repeated finite root satisfies 5x^4+lambda^3=0 and f=0. Eliminating x using lambda != 0 gives x=-5lambda/4, and then lambda=-256/3125. The second derivative 20x^3 is nonzero there, giving an ordinary double root; the other three roots remain simple. At lambda=0 substitute lambda=t^8, x=t^6 X, y=t^15 Y: Y^2=X^5+X+t^2. At infinity substitute lambda=s^{-5}, x=s^{-4}X, y=s^{-10}Y: Y^2=X^5+sX+1. The limiting curves are smooth. The first holomorphic form scales as dx/y=t^{-9}dX/Y near zero and as s^6 dX/Y at infinity. The second form x dx/y scales as t^{-3} X dX/Y and s^2 X dX/Y. Their corresponding fractional divisors are 3((2/5)[infinity]-(3/8)[0]) and ((2/5)[infinity]-(3/8)[0]), giving degree 3/40 and 1/40. The finite eigenvalue characters at these charts must be checked for minimality of root orders 8 and 5; the coordinate actions have those orders and the primitive characters of the holomorphic forms force them. The node formula and all scaling exponents will be recalculated by new symbolic code.

## night:P1.5

At a point choose a generator v of ell_0. The map w |-> v wedge w has kernel span(v). Restricted to the rank-two Hodge space containing v, its rank is 2-1=1. On the full rank-four de Rham space its rank is 4-1=3. Projection to the primitive exterior-square quotient must remain injective on this rank-three space. For the symplectic primitive quotient, the polarization line is generated by a bivector of rank four, while v wedge w has wedge square zero and rank at most two; the two subspaces meet only in zero. Thus the corrected image has rank three. This linear algebra supplies the exact correction, subject to matching the projection convention in the source.
