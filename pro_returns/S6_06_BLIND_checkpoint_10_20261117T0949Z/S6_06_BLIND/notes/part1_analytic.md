# Fourfold analytic calculation: work begun before checkpoint 01

This is a derivation in progress, not a completed numbered assertion. The remaining cohomology-map ranks and endpoint issues are recorded explicitly.

Put L=T² on the orbifold with orders 5,4. Its degree is 1/20. The invariant coarse degree of L^j is

    d(j)=floor(4j/5)+floor(−3j/4).

The corrected lifted Hodge plane is F=O⊕L⊕L². The translation Lie bundle is E=F∨. In the rank-five orthogonal quotient W the kernel of alpha is K=L⊕L², and the quadratic pairing induces W/P=K∨. Consequently G=V/F is an extension of K∨ by Oe. Its extension group H¹(K) vanishes by the displayed floor formula, so G=O⊕L^-1⊕L^-2. At the cusp, the locally constant classes in ker(N) give the coherent H¹ basis on the central fibre. The normalization complex is the cellular cochain complex of the three-torus, with exterior cup product. Its coherent dimensions are (1,3,3,1). Grauert then gives R^q h_*O=∧^qG. The floors at exponents −1 through −5 are all −1, while d(0)=0; hence h^q(O)=(1,1,0,0,0).

The orbifold tangent line is L^9. The logarithmic tangent relation gives det T_M=h^*L^6 and K_M=h^*L^-6. Its tenth inverse power is f^*O(3). An effective horizontal divisor restricts to a nonzero effective divisor on a generic Kähler torus, and hence has nonzero real Chern class there, by pairing with a Kähler form. Since H²(M;Z)=0, no such divisor exists. The pole divisor of a meromorphic function is vertical; the function is constant on a generic compact fibre and descends to P¹. This proves the route to algebraic dimension one.

For the tangent sequence, let D be the singular locus of the cusp. Locally q=x0x1x2x3, its ideal is the four squarefree cubic monomials. It has codimension two and a Hilbert–Burch resolution, so it is Cohen–Macaulay. The conductor square for the toric normalization Y is

    0 -> O_W -> O_Y ⊕ O_D -> O_boundaryY -> 0.

The smooth complete toric threefold Y has no higher coherent structure cohomology. Its full toric boundary has coherent cohomology (1,0,1), from the anticanonical sequence and Serre duality. The boundary top class maps isomorphically to H³(O_W): in the cellular model it is the oriented fundamental three-cell. Thus h(O_D)=(1,3,3), and H^i(O_W)->H^i(O_D) is an isomorphism for i=1,2.

Write J=I_D h^*L^9. From the floor formula and ∧G one obtains h^q(h^*L^9)=(1,2,1,0,0). Evaluation at the cusp followed by the preceding restriction is injective in degrees 0,1,2, with ranks 1,2,1. Thus h^q(J)=(0,0,1,2,0). Likewise h^q(E)=(1,1,0,0,0). The exact tangent sequence gives the candidate, now awaiting integration of these local-map proofs, h^q(T_M)=(1,1,1,2,0). The explicit parameter derivative alpha e modulo F is nonzero. The intrinsic anticanonical map and its three distinguished critical values force any first-order trivialization to preserve the base; the discrete integral torus marking then proves the Kodaira–Spencer class nonzero. A one-dimensional Kuranishi tangent space with this actual nonconstant analytic disk makes the Kuranishi germ smooth by the one-variable analytic local-ring argument.

For automorphisms, the exact parabolic lattice calculation has H¹(B,j_*Lambda)=Z/2 and H¹(E)=0. The fixed half-period (0,1,1,1,1,1)/2 gives an actual order-two translation section. At the cusp it can be represented by a bounded angular half-period because N is primitive. The lattice has no global invariant homology vector, so the connected translation group is C. The common rational centralizer is scalar; integral automorphisms have linear part ±I. At the order-five fibre the −I lift would require ell((I−M1)t)=2/5 modulo Z, while the left side is zero. This excludes it. The remaining expected full group is C×Z/2. This same linear-part computation gives injectivity of the complex parameter once its splitting is fixed.

The Hodge table requires more work. Dualizing the tangent sequence gives

    0 -> h^*L^-9 -> Omega¹_M -> h^*F -> omega_D -> 0.

Here h(omega_D)=(3,3,1), h(h^*F)=(1,3,2,0,0), and h(h^*L^-9)=(0,1,1,0,0). On central cohomology the residue is represented by N(f) wedge g. The exact exported matrix in code/part1/cusp_residue_weight_bases.json gives a possible rank jump of the degree-one map at algebraic parameter z=−3125/384. The agent's actual integral normalization identifies this with c=5/(3pi) in the b1 splitting. Numerical values h(1)<−1 and h(2)<−1 suggest this point is outside the admissible domain; a rigorous exclusion is still needed. No full Hodge table is asserted here.

Real structures and proper limits at the two ends have not yet been determined. The normalization of the splitting in P1.8 and the algebraic b1 splitting in the numerical calculations must be related explicitly before comparing numerical c values.
