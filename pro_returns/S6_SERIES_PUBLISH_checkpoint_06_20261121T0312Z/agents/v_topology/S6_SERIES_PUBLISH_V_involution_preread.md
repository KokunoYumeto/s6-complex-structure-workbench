# Pre-read derivation: F.2.37–39 and the 56 involution classes

Recorded 20 November 2026, before reading the proof bodies of F.2.37, F.2.38 and F.2.39. Inputs read: their statements, the statements of F.2.31–36, and the displayed normal-form formulas IV1–IV4 and CN1–CN3. The derivation below checks the asserted normal-form morphisms and count independently of the proof text.

## Canonical representatives (F.2.37)

Order all integral (k+1)-tuples first by maximum absolute entry and then lexicographically. For an input T of height H, its own orbit has at least one representative in the finite box of height H, namely T itself. Enumerate the whole box, reject tuples failing the exact admissibility equations, and use the simultaneous integral-conjugacy decision algorithm of F.2.36 on the remaining candidates in that order. The first conjugate is the least element of the entire orbit: any smaller height or lexicographically earlier representative would have been encountered. Record the conjugator returned by F.2.36. Another input in the same orbit gives the same least representative even if its height is larger; a different orbit cannot give the same representative. There are at most (2H+1)^(36(k+1)) box candidates. This is finite for each input, not a common bound for all orbits.

The family with trace(M1 M2^3)=-v^4+v^3-v^2+2 has infinitely many trace values as integral v grows. Simultaneous conjugacy preserves that trace. A fixed finite-height box contains finitely many tuples, so it cannot contain representatives of all those classes. This proves the absence of a fixed global height bound through an explicit invariant.

## Involution algebra and the cusp normalizer (F.2.38)

Normalize the primitive square-zero cusp N to [[0,I3],[0,0]] by choosing an integral image/kernel basis and integral preimages. Since M1 M2=(I+N)^-1=I-N and M1^2=M2^2=I, we obtain M1 N M1=-N. Writing M1 in 3-by-3 blocks then forces M1=[[A,B],[0,-A]], with A^2=I and AB=BA; M2=[[A,B-A],[0,-A]]. Conversely these equations give precisely the required two involutions and primitive maximal cusp.

A simultaneous conjugator between two normalized triples must commute with N. Its explicit form is [[P,Q],[0,P]], where P is unimodular and Q integral. It conjugates A by P and changes B by the corresponding anticommutator AD+DA. Thus the integral classification is the classification of integral involutions A on Z^3, followed by B modulo that explicit map and the action of A's integral centralizer.

An integral involution on L is classified by the primitive eigensublattices L+ and L-. The quotient L/(L+ plus L-) is killed by two. Its embedding into (L+/2L+) plus (L-/2L-) projects injectively to each summand: a glue class supported on only one eigenspace would violate the saturation of that eigensublattice. Hence it is the graph of an isomorphism between two equal-dimensional F2 subspaces. Integral basis changes of L+ and L- lift the mod-two basis changes and reduce this graph to the coordinate graph. Each glued pair is a swap module. We obtain A=I_p plus (-I_q) plus J^r, p+q+2r=3, and the triple (p,q,r) is recovered from the eigenspace ranks and glue rank. There are six possibilities.

For the B quotient define the intrinsic groups
K+=ker(A-I)/(I+A)L and K-=ker(A+I)/(I-A)L.
Their dimensions over F2 are p and q. A commuting B acts on them. This gives the explicit map
End_{Z[A]}(L) -> End_F2(K+) plus End_F2(K-).
Its kernel is the image of D -> AD+DA. In the displayed module blocks, on pure plus and pure minus blocks this image is twice every matrix. A commuting block from a pure sign s to a swap is (a,sa), and every such block equals sD+DJ for a suitable integral row D. The reverse block is treated by its transpose. A commuting swap block is [[a,b],[b,a]], and every such block equals JD+DJ because the two off-diagonal sums of D are arbitrary integers. Opposite-sign commuting blocks vanish. These calculations prove the claimed quotient exactly.

Every integral centralizer unit acts separately on K+ and K-, so the residual B's are classified by a pair of F2 similarity classes. Conversely the block groups GL_p(Z) and GL_q(Z) surject onto GL_p(F2) and GL_q(F2), yielding every required pair of similarities. The remaining difference in B has zero residue and is removed by an integral solution of AD+DA, found by Smith reduction. These maps furnish a canonical representative and the actual simultaneous unimodular conjugator.

The numbers c_n of similarity classes of n-by-n binary matrices for n=0,1,2,3 are 1,2,6,14. A fresh exhaustive orbit program will verify them and construct representatives. The six involution types contribute, in order,
c0*c3 + c1*c2 + c2*c1 + c3*c0 + c1*c0 + c0*c1
=14+12+12+14+2+2=56.

Every resulting six-dimensional involution has a rank-three fixed lattice, so choose a primitive fixed vector u. The affine map x -> Mx+u/4 has order four. Its square is translation by u/2, with no fixed point. A fixed point for an odd power would give (I-M)x=j u/4 modulo the lattice; multiplying by I+M forces j u/2 to be integral, contradicting primitivity. Thus all nonidentity powers act freely. Every free affine lift of a linear involution has even affine order, and the two-point orbifold quotient is C_gcd(m1,m2), with even nontrivial order. No filling in this sector is simply connected.

## Complete algorithmic scope (F.2.39)

The canonical-linear classification is exactly F.2.37 with the finite involution sub-classification above. The fundamental-group presentation and extension kernel are the explicit output of F.2.31 for the supplied affine data. The homology computation is the finite integral gluing complex of F.2.35. The retained three-connected data are characterized by the exhaustive inputwise lattice enumeration and the necessary-and-sufficient tests of F.2.30, already independently checked compositionally in this task. All these statements use the same ordered peripheral and primitive cusp markings. Canonical linear tuples identify simultaneous integral conjugacy; the theorem does not assert that arbitrary distinct affine gluings are diffeomorphic merely from equality of homology. The final theorem's scope matches those precise component outputs.
