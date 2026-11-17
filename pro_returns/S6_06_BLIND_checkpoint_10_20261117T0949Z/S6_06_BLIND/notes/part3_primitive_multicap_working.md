# Simultaneous caps on the primitive sources: exact ordinary comparison

Root derivation begun 17 November 2026, after P3F.40. This is not yet a numbered manuscript statement. The global ordinary comparison and boundary parity below supply a substantially stronger degree-two reduction. The actual reduced/good additive root list and its parameter-return comparisons are being proved separately. No return is assigned here.

## 1. The closed ordinary orbit fixes the full exterior lattice

Use any of the ten sources in P3K.22, with its actual primitive translation G, line M and sole simple whole zero. The unmodified orbit is W0=T_(t_G)S in the physical outward suspension. Its integral Wang groups are H2(W0)=Z[O] and H3(W0)=ZF. Remove a finite collection of disjoint ordinary source-fibre tubes, none at the chosen whole zero. They may be smooth, multiplicative, or one of the reduced additive fibres II, III, IV occurring in these profiles. Let W be the complement of their actual ordinary orbit tubes U_i, and E_i=boundary U_i.

Every ordinary U_i has H2 free. Its central fibre has all component multiplicities one, and G is transitive on its components. The invariant sum of those components is the actual F. Naturality of the integral Wang sequence therefore sends the component-trace generator of H3(U_i) to the primitive generator F of H3(W0). This also holds at a smooth fibre, where the trace is the full T3. Thus the total H3(cap) map is onto H3(W0).

The actual section representative O in a source slice intersects each removed fibre once. Its boundary is sum_i alpha_i in the direct sum of the H1(E_i). Every alpha_i is a primitive infinite-order base meridian. Consequently the boundary map H2(W0)->direct_sum H1(E_i) is injective. These two facts, in the complete ordinary Mayer--Vietoris sequence, give the integral isomorphism

    direct_sum H2(E_i) -> H2(W) direct_sum direct_sum H2(U_i).

In particular H2(W) is free, and the images of the ordinary cap-boundary kernels form an integral basis of H2(W). This uses the actual ordinary caps, not a rational splitting or an assumed absence of rim terms.

## 2. Exact parity on each ordinary boundary kernel

The involution I[p,t]=[-p,-t] is defined on W0 and preserves all the chosen tubes and their complement. It reverses the five-dimensional orientation and preserves the positive normal base-disc orientation.

At a smooth source tube choose a local Lie lift G(q). The map

    (a,b,t) -> [a+b*tau(q)+t*G(q),t]

identifies its actual three-torus mapping torus. In these coordinates I is exactly (a,b,t)->(-a,-b,-t). The positive base meridian alpha is fixed. Thus the three smooth ordinary-cap kernel tori a alpha, b alpha, alpha gamma are I-odd, whereas ab,a gamma,b gamma are I-even.

At a multiplicative source use the same formula on a Tate sector. The source continuation is a->a+Nb+c_G t and hence commutes with -I on (a,b,t). The formula therefore descends to the actual boundary, with c=-c_G in P3F.40's convention. Its integral H2 basis z,R,B,L and intersection form are precisely those of (F40.3)--(F40.4). I is +1 on z,B and -1 on R,L. The ordinary cap kernel is exactly ZR direct_sum ZL; this follows either from the actual cap projection or from its primitive fibre and graph traces and the isotropic-kernel calculation in F40. The source component rotation and the line-unit phases have not been substituted by a different marking.

At a reduced additive ordinary site, the actual affine boundary has free H2 of rank two. The III/IV cases are explicitly certified in code/part3_fourfold/primitive_additive_complements.*; the II case has linear monodromy of order six with D-I unimodular and no component torsion. Write F=r z, where r=1,2,3 is the reduced component count. Its primitive z maps to the primitive cap component orbit C. The boundary is a three-torus mapping torus, hence is parallelizable: a path in GL3+(R) from its oriented monodromy to the identity trivializes the vertical tangent bundle, and the base direction supplies the fourth vector. Its rank-two intersection form is therefore even. Since z^2=0 and z is primitive, choose w with z.w=1, and set s=w-(w^2/2)z. The kernel of the ordinary cap map is isotropic, so its C coefficient on w is w^2/2; hence its kernel is exactly Zs. Inversion fixes F and therefore z. It preserves that kernel and reverses the boundary orientation. The equation Iz.Is=-z.s forces Is=-s, with no possible z correction because the cap map is fixed.

All ordinary boundary-kernel basis vectors are therefore I-odd. Their images are the integral basis of H2(W) from section 1. Thus I acts as -1 on the entire torsion-free H2(W). Every I-even boundary core class maps to zero in W, since its image equals its own negative. This proves the vanishing of all such core columns simultaneously, without extending I over any of the replacement caps.

## 3. The independent replacement blocks

For a primitive smooth cap retain its actual meridian

    mu=m alpha+n gamma+lambda_a a+lambda_b b,

with gcd(m,n)=1. The cap H2 map is the exterior square of the exact primitive quotient by mu. Eliminating that cap target leaves its ordinary rim group modulo the images of mu wedge H1(E). Since the three core columns vanish, a presentation matrix is

    [[m,0,0,-lambda_a],
     [0,m,0,-lambda_b],
     [0,0,m,n]].

Its Smith factors are 1,m,m: gcd(m,n)=1 supplies the first unit, and its primitive-vector quotient gives the two remaining m factors. This is the exact (Z/m)^2 block of P3K.22, with every elliptic coefficient retained.

For a transitive multiplicative cap, P3F.40 gives the complete actual block. With exterior z,B zero and R,L its independent exterior basis, the retained cap target change leaves diag(m,m). Its cokernel is (Z/m)^2.

For an additive cap with free H2=ZC, the ordinary exterior kernel is s and its exterior image is the corresponding independent basis element. The even z column is zero in W. Its replacement block is consequently determined solely by the actual specialization j(z). The reduced III and IV roots currently constructed have j(z)=C because their fibre specializes to rC. The good II root has j(z)=C when its smooth generic fibre transport is degree one. The corresponding blocks are unimodular, with the other integral cap column retained and eliminated by the exterior basis column. Each specialization must be checked in its actual source/line construction; no merely numerical fibre label is used to supply it.

Since the exterior basis and its even zero columns are already simultaneous, these eliminations occur in disjoint direct summands. In this computed scope the full degree-two cokernel is the direct sum of the (Z/m_i)^2 blocks from the smooth and multiplicative sites. Thus every such site of a sphere member has effective order one. The remaining reduced/good additive orders are controlled by their actual norms and the Seifert determinant, not by this degree-two obstruction.

## 4. Remaining integral and parameter comparisons

The program for the simultaneous exact blocks and smooth primitive kernels is exported and executed at code/part3_root/primitive_multicap_blocks.py, with JSON and output. The checks agent independently passed sections 1--3; records/part3_primitive_multicap_working_audit.json records that audit. The scope and residual fundamental-group/parameter comparison are retained here before a numbered manuscript export. The source vanishing cycles retain their original normal closure: multiplicative replacement kills the original vanishing a-cycle, reduced additive replacement kills the source elliptic loops, and smooth replacements leave those original relations elsewhere. This is the route to the exact residual Seifert group; its complete marked presentation will be written, including the surviving order-one clutches.

Every primitive source profile has at most one nonzero-linearization additive site. Once smooth and multiplicative effective orders are one, its first-homology determinant is n_add+m_add*sum(n_other), or sum(n_i) without an additive site. The actual integral gamma gauges and elliptic/delta cochains remain to be traced before this arithmetic is used as an exhaustive family/return table.
