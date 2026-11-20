# K109 full centralizer derivation

Written after opening EF.1–3 and the nonzero-Abel-class argument in EF.4, stopping at source line 90300 before its printed full-centralizer calculation. This is a new derivation from the displayed full matrix EF.18; it does not claim to precede reading that input matrix or its geometric construction.

Write the ordered lattice as Q gamma ⊕ W ⊕ Q delta and

M_alpha = [[1,0,0],[b v_alpha,A_alpha,0],[c_alpha,a v_alpha^T J A_alpha,1]].

The nonzero rational Abel class [v] and the irreducibility of the elliptic representation imply the common invariant space is exactly Q delta: the gamma coefficient z of an invariant vector would make b z[v]=0, hence z=0; then its W part is invariant and zero. Applying the symplectic dual to the same nonzero extension gives the common fixed covectors Q psi. A commuting linear map therefore has block form L=[[c0,0,0],[u,P,0],[d,w^T,c3]].

The middle block commutes with every A_alpha. The order-three elliptic matrix has quadratic-field centralizer; a nontrivial unipotent has nonzero nilpotent part, so it cannot commute with a non-scalar element of that field. Thus P=c1 I. The (W,gamma) equation is (I−A_alpha)u=b(c0−c1)v_alpha. Nonvanishing of [v] gives c0=c1; irreducibility then gives u=0. The (delta,W) equation is w^T(A_alpha−I)=a(c1−c3)v_alpha^T J A_alpha. Its cohomology class is the symplectic dual of a[v], so c1=c3 and w=0. Every c_alpha cancels in the remaining (delta,gamma) equation. Therefore L=cI+d delta psi.

For an integral lattice automorphism, c=±1 since the determinant is c^4; primitivity of delta and psi makes d integral. If it is complex linear, d delta psi is also complex linear. A nonzero real rank-one map cannot have that property, since the real rank of a complex-linear map is even. Hence d=0 and L=±I. This conclusion uses all central cochains and does not set any c_alpha to zero.

For an isomorphism covering a nontrivial source-base map, the same invariant-line and invariant-covector characterization survives conjugation of the full monodromy group. Thus its lattice map preserves their primitive integral lattices, lifts to the cyclic cover ker(psi), and preserves the complex line through delta. The induced map on ker(psi)/Z delta is unimodular and complex linear, so it is an affine degree-one map of the original elliptic fibres. This supplies the needed bridge from the intrinsic base fibration to the actual j-function used in IV_open_prereading.md, provided that the target source atlas realizes these primitive quotients through the cap charts.
