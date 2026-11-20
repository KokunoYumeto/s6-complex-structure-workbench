# Targeted receiving check of the comb dual-cup morphism

PASS at the exact stated scope. This is a post-reading comparison with E15 and E2.2, not a new unexposed derivation, period-section construction, splitting computation or strict movement of inv:E2.3.

## Actual source maps and types

E15 Step1 identifies F as the Hodge subbundle, V=F* as the vertical logarithmic tangent bundle, G=R1 fbar_*O, and cup product R2 fbar_*O=exterior²G. This comparison is explicitly retained on finite-root charts and at the hexagonal fibre through its normalization complex. E15 Step6 gives the logarithmic tangent extension with horizontal line L=O(-5). E2.2 Step2 uses E_m=V and fixes D=detG=O(24m-1); Step6 identifies the root cokernel N=coker(delta0) with R1 of the logarithmic tangent bundle, and Step8 defines the actual cotangent kernel through kappa1.

Dualizing that very extension gives the logarithmic cotangent extension with subline L* and quotient F. For the displayed tangent change-of-splitting block, inverse transpose followed by the literal permutation from(F,L*) to(L*,F) gives the block with off-diagonal entry minus beta-transpose. Here beta denotes the relative Kodaira–Spencer section represented by the family Cech cocycle; no independent extension class is substituted.

## Wedge and sign calculation

With ordered frame(g1,g2) and determinant frame omega=g1 wedge g2, define J(g)(h)=h wedge g. Then

    J(g1)=-g2* tensor omega,    J(g2)=g1* tensor omega,
    J=[[0,1],[-1,0]],         J inverse=-J.

This is a natural bundle isomorphism G->G* tensor D: evaluation after a change of G-frame is the original wedge pairing with the actual determinant-frame change. It is therefore equivariant on the root charts and requires no identification of E_m with its dual.

Write beta(ell)=u1 tensor(a g1+b g2)+u2 tensor(c g1+d g2), in a local L-frame ell and dual F-frame(f1,f2). The cotangent cup boundary on fi tensor g is minus beta_i wedge g, using the stated Cech boundary convention and the ordinary cup/exterior order already fixed by E15. Its four entries are exactly

    (b,-a,d,-c).

On the other hand delta0* has row(a,b,c,d), and right multiplication by I_F tensor J gives(-b,a,-d,c). The additional dual-extension minus sign gives the same row. Thus the formula

    kappa_root = -(delta0* tensor I_D)(I_F tensor J)

is correct with the note's conventions. A global opposite convention for one connecting morphism is transported by the explicit target automorphism minus identity, so it has exactly the same kernel.

## Nonsaturation and coarse descent

For the actual exact sequence L->E_m tensor G->N->0, left exactness of Hom(-,O) gives N*=ker(delta0*). It does not require N to be torsion-free or delta0 to have saturated image. On a smooth root-curve chart, maps from its torsion to the free rank-one structure sheaf vanish. Tensoring with the line D is exact. Consequently the actual inverse image under I_F tensor J is the cotangent kernel on the root curve.

Finally rho_* is computed by finite stabilizer invariants in characteristic zero. The averaging projection is exact and the wedge map is equivariant. Applying it to the kernel sequence gives the asserted isomorphism

    rho_*(I_F tensor J): K_m -> rho_*(N* tensor D).

Keeping the dualization and D-twist before rho_* is essential to this exact formula; no coarse tensor-product or coarse-dual replacement is used.

## Remaining scope

The note correctly leaves the admissible period section, its transition maps/derivative and the splitting of the resulting bundle uncomputed. The tangent calculation gives cohomology of rho_*N, while the displayed wedge isomorphism specifies the exact additional dual-and-twist construction needed for K_m. Replacing the older phrase about a different cup map by this precise relation is justified. This comparison closes only the proposed local/global map identification and its sign; it supplies no new value of h0(K_m), no claim that two admissible sections have distinct Hodge numbers and no conditional theorem.
