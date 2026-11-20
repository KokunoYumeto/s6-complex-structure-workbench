# Exact duality between the two actual comb cup maps

This is a post-reading calculation from the displayed logarithmic tangent and cotangent extensions in E15 and E2.2. It supplies an exact morphism between their maps. It does not choose an admissible smoothed period section, determine a splitting, or close inv:E2.3.

On the actual root curve put F=E_m^*, G=G_m, D=det G and L=O(-5). The tangent extension has Kodaira–Spencer class beta in E_m tensor G tensor L^*. Its degree-zero connecting map is

    delta_0 : L -> E_m tensor G.

Write N=coker(delta_0) on the root curve. The nonzero cusp matrix proves that delta_0 is injective. Dualizing gives the exact kernel identity

    N^* = ker((E_m tensor G)^* -> L^*).

This identity includes any torsion of N, whose maps to the locally free structure sheaf vanish. It does not assume that the image of delta_0 is saturated.

## The actual wedge and sign maps

Define the everywhere invertible wedge map

    J : G -> G^* tensor D,       J(g)(h)=h wedge g.

With ordered G-basis(g1,g2), determinant frame g1 wedge g2, and dual basis(g1^*,g2^*), its matrix is [[0,1],[-1,0]]. The inverse is its negative. Consequently

    I_F tensor J : F tensor G -> (E_m tensor G)^* tensor D

is an explicit bundle isomorphism.

The sign can be tracked in the extensions. Choose local splittings of the tangent sequence; a change of splitting has block matrix [[I,beta],[0,I]], ordered as(E_m,L). On the dual sequence, ordered as(L^*,F), the block matrix is [[I,-beta^t],[0,I]]. Thus the cotangent extension class is the negative transpose, using the same Cech boundary convention. Cup product followed by the wedge on G is therefore

    kappa_root = -(delta_0^* tensor I_D) (I_F tensor J).

For delta_0(ell)=u1 tensor(a g1+b g2)+u2 tensor(c g1+d g2), its row in the ordered F tensor G basis(f1g1,f1g2,f2g1,f2g2) is(b,-a,d,-c). This verifies the formula entry by entry. Reversing the convention for one connecting map changes its target by the explicit automorphism -I and leaves this kernel unchanged.

It follows, through the displayed isomorphism rather than an identification of E_m with its dual, that

    ker(kappa_root) = (I_F tensor J)^(-1)(N^* tensor D).

Finite stabilizer invariants are exact: the averaging operator(1/r)sum(g) is a projection on each order-r root chart. Thus the actual coarse kernel in(E.6) is identified by rho_*(I_F tensor J) with

    K_m ~= rho_*(N^* tensor D),       D=O(24m-1).

The existing tangent calculation determines the cohomology of rho_*N. It does not provide the individual transition matrices of N needed to split rho_*(N^* tensor D). The preceding equality is an exact relation between the two existing maps; it is not counted as a strictly smaller main gate. The remaining calculation still requires a specified admissible period section and its derivative.
