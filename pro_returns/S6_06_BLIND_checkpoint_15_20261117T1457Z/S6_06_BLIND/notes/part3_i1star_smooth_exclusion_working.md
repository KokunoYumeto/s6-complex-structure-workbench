# Extra smooth-site caps on the OS50 additive cores

This proof concerns the actual star core of P3F.36 and the two star/IV cores of the joint calculation, with all other singular source values retained. It allows any finite collection of additional smooth-site caps, with their full elliptic and delta collars. After the exact finite-kernel quotient of P3K.19, every such cap in a sphere member has order one. No inversion is asserted to extend across a marked cap.

## 1. The prime detected by the actual base

The actual source projection of P3K.16 gives the orbit base by filling its positive meridians m_i alpha_i+n_i gamma. Its integral first-homology determinant is

    D_base=b0 product_i m_i+sum_i n_i product_(j!=i) m_j,

where b0 is the retained integral gamma clutch (equivalently it can be represented by an order-one site).

The map from the orbit to this base is onto on fundamental groups: lift a loop away from the finitely many source-singular circles and close the lift in the connected elliptic fibre. The local Hopf meridian makes pi1(X)=pi1(Y), as proved in P3F.36. Thus a sphere forces |D_base|=1. In particular two cap orders cannot have a common prime factor, since that prime would divide every summand.

At a smooth root the finite zero-gamma subgroup has already been removed by the actual quotient map of P3K.19: in invariant source-and-line coordinates it is (e,z)↦(e,z^g), with the line pulled back through that same map. The resulting norm pair is primitive. This is the exact map used here, not a relabelling of a finite isogeny.

Suppose an extra smooth-site order has a prime divisor p. Primitivity gives p not dividing its norm numerator. The existing starred order2 gives p≠2. For the good-IV core the existing order is a multiple of3, so p≠3 as well. Therefore p does not divide the source translation coefficient b: b=2 for the star and reduced-IV cores, and b=6 for the good-IV core.

## 2. The source exterior, before any cap is filled

Let W0 be the actual mapping torus of t_(−bG) on the source complement of the additive fibre neighbourhoods. This is the exterior before all marked caps. Its integral H2 is

    Z⊕Z/2                    for the sole star core,
    Z²⊕Z/2                   for the reduced-IV core,
    Z²⊕Z/6                   for the good-IV core.

The actual source inversion followed by reversal of the suspension,

    I[p,t]=[−p,−t],

is defined on W0. The three executed source/cone calculations give the following H2 matrices, with torsion first:

    [[1,2],[0,−1]],
    [[−1,216,138],[0,−1,0],[0,0,−1]],
    [[−11,120,2],[0,−1,0],[0,0,−1]].

The first is the sole-star model, the second reduced IV, the third good IV. Since p does not divide b, torsion disappears over k=F_p and I acts as−1 on all H2(W0;k).

Remove r regular source-fibre tubes N_i=T3×D2, disjoint from the additive boundaries, and call the exterior W. On a regular tube the actual local translation lift of Q trivializes its mapping torus. In these coordinates I sends the three core circle generators(a_i,b_i,gamma) to their negatives and preserves the positive normal meridian alpha_i. It reverses the orientation of W0 and preserves the orientation of the normal D2.

Every core H2 class is I-even, so its image in H2(W0;k), which is I-odd, is zero. The Thom map H3(W0;k)→⊕H1(T3;k) is dual to intersection with these core two-classes, and is consequently zero. The Thom map H2(W0;k)→⊕H0(T3;k) is also zero: each core fundamental three-class is I-odd, while every two-class is I-odd and I reverses the ambient orientation. Naturality of their intersection pairing gives x·z=−x·z; p is odd, so this intersection vanishes.

The Thom sequence therefore gives the actual short exact sequence

    0→R→H2(W;k)→H2(W0;k)→0,
    R=direct_sum_i span(A_i=a_i alpha_i,
                        B_i=b_i alpha_i,
                        C_i=alpha_i gamma).

All three rim generators are I-odd. Because p is odd, the ±1 eigenspaces of an involution split by(1±I)/2. Both end terms are odd, so all of H2(W;k) is odd. Thus the images in W of every smooth-boundary core class

    a_i b_i, a_i gamma, b_i gamma

are exactly zero over k. This conclusion uses I only on W, not on any marked filling.

## 3. Eliminate the already computed additive blocks

For each of the three cores, the actual additive degree-two Mayer–Vietoris map to H2(W0) plus the additive-cap groups is an integral isomorphism. For the sole star this is P3F.36's arbitrary-kappa matrix. For the joint cores it is the two-kappa matrix in the executed source-boundary certificates; their respective torsion maps are Z/2→Z/2 and Z/2⊕Z/3→Z/6. These statements retain every marked cap coefficient.

Projecting H2(W;k) onto H2(W0;k), the additive boundary map still projects to that isomorphism. Its image therefore has zero intersection with R, and the quotient by the additive image is exactly R. This is an exact elimination of a graph over the quotient space; no extension of the source inversion over the caps is used. Under this identification the smooth-boundary core columns remain zero and the three rim columns remain A_i,B_i,C_i.

## 4. The smooth-cap kernel and its two surviving classes

A primitive smooth cap has the actual marked meridian

    mu_i=m_i alpha_i+n_i gamma+lambda_ai a_i+lambda_bi b_i.

P3K.15's norm shell identifies its orbit with T3×D2, and the actual boundary map on H1 is the quotient by this primitive vector. Its H2 map is the exterior square. Over k, the kernel is therefore precisely mu_i wedge H1(T4;k). Eliminating the cap H2 target identifies the remaining quotient with R modulo the images of these kernel vectors.

The even core columns are zero. In the rim basis(A_i,B_i,C_i), the images of a_i wedge mu_i, b_i wedge mu_i, gamma wedge mu_i, alpha_i wedge mu_i are, up to the displayed orientation signs, the columns

    [[m_i,0,0,−lambda_ai],
     [0,m_i,0,−lambda_bi],
     [0,0,m_i,n_i]].

For the selected prime p dividing m_i, this matrix has rank exactly one: its first three columns vanish, and its final column is nonzero because p does not divide n_i. Hence two independent classes in this actual rim summand survive. Different smooth sites have disjoint rim summands, so their kernel images cannot cancel them. The cokernel of the full degree-two Mayer–Vietoris map injects into H2(Y;k), which is therefore nonzero. This contradicts the orbit homology of a semifree sphere with its standard fixed sphere, already proved in P3F.8 and used in P3K.16.

Every extra smooth-site cap in a sphere member must consequently have reduced order one. This is a necessary exclusion; the proof does not discard the integral order-one annular clutch or its elliptic/delta coordinates, and does not claim a value of a parameter-return invariant.

## Transfer to every allowed cusp fan

P3F.35 gives the actual finite periodic diagonal-flop chain from any allowed one-vertex fan to the vertical fan. Each map is the identity outside the cusp, so all of the present cap markings are retained. The common blowup and its two ruling contractions preserve integral homology and fundamental group. Thus a sphere for the original fan gives a sphere for the vertical fan, where the preceding orbit obstruction applies. This supplies the exact comparison used in the final P3F.39 export.
