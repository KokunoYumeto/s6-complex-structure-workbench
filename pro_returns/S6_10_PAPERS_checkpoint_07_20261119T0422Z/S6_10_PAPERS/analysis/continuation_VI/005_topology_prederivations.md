# Unrestricted topology batch: before target proofs

Checker: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation, 19 November 2026.

Statements-only inputs: UN.2, UN.4, UN.14, C2a, C2b, C2c. UN.1 steps 1--2 were exposed in the initial header read; the remaining linear algebra is derived below before opening its printed continuation.

## UN.1, remaining linear algebra

For a mapping torus of T⁴ with A∈SL(4,Z), Wang gives b_j(M)=k_j+k_{j−1}, k_j=dim ker(Λ^jA−I), and k₀=1. Thus b₀+b₁+b₂=2+2k₁+k₂, whose parity is k₂. On Λ²Q⁴ the wedge product is a nondegenerate symmetric form and G=Λ²A is an isometry with det G=(det A)³=1. The identity det G=(−1)^rank(G−I) follows directly as follows. Put W=im(G−I)=ker(G−I)^⊥ and define the nondegenerate bilinear form χ((G−I)x,(G−I)y)=B((G−I)x,y). Independence of the lift y follows from W⊥=ker(G−I). Orthogonality yields χ(v,u)=−χ(G⁻¹u,v). Taking determinants on W gives det(G|W)=(−1)^dimW. G acts trivially on V/W, so det G is the same determinant. Hence rank(G−I) is even and k₂=6−rank(G−I) is even. Combining with the pair-sequence parity gives e(S) even.

## C2a

The critical locus is analytic. Its proper image in the curve is analytic and misses a regular value, hence is finite. Away from this finite set, Ehresmann gives a locally trivial smooth bundle. A finite triangulation subordinate to the base stratification yields χ_c of the regular bundle as χ_c(base)χ(F), including nontrivial monodromy because each simplex trivializes the bundle. Add the compact singular supports by Euler additivity. Nilpotents do not change the underlying space. For two-tori χ(F)=0, and complex orientation identifies the top Chern number with e(Y).

## C2b

Take a smooth genus-two curve C and its Jacobian abelian surface A. The Abel–Jacobi image embeds C as a theta divisor. In A×P¹ blow up C×{0}; the central reduced support is the union of A (blowup along its Cartier divisor is A itself) and P(N_C/A⊕O_C), meeting along C. Thus e=0+2e(C)−e(C)=−2. The full fibre remains reduced because the centre lies in a multiplicity-one component. Blow up one smooth point of the A component away from C; the central support replaces that point by P², adding 3−1=2, and the strict A is its one-point blowup. Its intersection with P² is a line and is disjoint from the ruled component. All local crossings are simple normal crossings, and the new Euler number is zero. Smoothness/projectivity follow from the blowup construction.

## UN.2

Parity restricts all values to 2Z. Point blowups at smooth central points add two and the genus-two curve blowup above subtracts two, giving every even value. For the asserted zero family, iterate the genus-two curve blowup along the outer section of each new ruled component, disjoint from its preceding intersection. In the chart of a blowup corresponding to the base direction, if x is a local defining coordinate of C⊂A and t is the base coordinate, the new coordinates are r=x/t and t. Along r=t=0 the normal transition is N_C/A⊕O; the outer section therefore has the same split normal bundle, so induction constructs k ruled components as a chain without increasing their full-fibre multiplicity. Choose k distinct smooth points on the remaining A component away from the attaching C and blow them up. Each adds a P² leaf and +2; the k curve operations contributed −2k, so the final Euler number is zero, with the stated incidence graph and k-point-blown-up abelian component.

## UN.4

For a blowup of a smooth complex threefold along a compact smooth centre C inside the fibre, the reduced central support becomes its full inverse image. Euler additivity replaces C by P(N_C/Y), so Δe=(codim_C−1)e(C). A point gives +2. A negative-two operation starts with a point blowup; inside its exceptional P² choose a smooth plane quartic C (genus three), and blow up C. The second change is e(C)=−4, yielding net −2. This does not require normal crossings or avoidance of the old support intersection: the formula compares full inverse images of the actual support. Parity of the initial fibre permits reaching any 2k by finitely many signed-two operations. Extra +2 and −2 pairs preserve Euler number while adding irreducible exceptional components, giving arbitrarily large zero-Euler refinements. Strict-transform multiplicities are preserved because the blowup is an isomorphism at their generic points. The integral blowup decomposition adds Z in degrees 2 and 4 for a point; a genus-three curve adds H^{j−2}(C), hence total increments (Δb₂,Δb₃,Δb₄)=(2,6,2).

## UN.14

Use the exact modification π of UN.4. Strict transforms of original surface components are bimeromorphic to them, with unchanged generic full-fibre multiplicity. Every newly created component is P² or a P¹-bundle over the smooth centre curve, and is therefore uniruled by the displayed projection. A bimeromorphism of smooth compact surfaces transports the dominant meromorphic C×P¹ map, so it preserves the indicated uniruled condition. Thus π induces exactly the claimed multiplicity-preserving bijection on non-uniruled normalization-resolution classes. Operations at distinct critical fibres have disjoint centres and may be performed independently; take the finite set of singular fibres for the final global assertion.

## C2c

The toric-stratum decomposition of the reduced central support has only two-dimensional torus strata, one-dimensional torus strata and zero-dimensional triple strata. χ_c((C*)^j)=0 for j>0. A unimodular triangle gives one triple point, so e(S)=F. The quotient triangulation is a cell decomposition of the real two-torus. Thus V−E+F=0 and 3F=2E, whence F=2V. The free translation quotient has V≥1. The standard two-triangle lattice decomposition with one vertex, followed by a translation sublattice of index q, gives V=q and e=2q for every q≥1. For the rank-one construction, P¹-bundles over elliptic curves and all their boundary elliptic curves have Euler number zero; gluing along the indicated curves preserves zero.
