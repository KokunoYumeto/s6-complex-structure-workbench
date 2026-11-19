# Fresh prereading derivation: maps:src:F.3.8

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro.
The statement and the known tube/LSAP input were sent by the Paper V
checker. No printed proof of this row has been opened by this checker.

## Statement and supplied known input

D3 is the component of {F in Gr(3,C6): F intersects conjugate(F) trivially}
containing the standard complex structure. At each point it is dominated
by a spanning tube of nine complex lines; the stated source criterion
then gives LSAP and Oka-1. Definition 2.1 of the supplied Oka-1 paper
requires an open connected neighbourhood that is a union of affine
translates of a tree with independent complex-line directions.

## Construction before the printed proof

1. Fix C6=E plus conjugate(E) at a point of D3. Graph coordinates identify
T_E Gr with Hom(E,conjugate(E))=M3(C). A graph Z is transverse to its
conjugate precisely when I-conjugate(Z)Z is invertible: the intersection
equations are x=conjugate(Z)y and y=Zx. This is the actual graph map.

2. For each pair i<j let N_ij=E_ij-E_ji. The curve t -> graph(t N_ij)
extends across infinity in the Grassmannian. At infinity its plane is
the sum of the remaining E coordinate and the two conjugate(E)
coordinates i,j. This plane and its conjugate are complementary.
At finite t, N_ij is real with N_ij^2=-I on its coordinate two-plane
and zero on the remaining coordinate. Hence I-|t|^2 N_ij^2 is invertible.
The whole projective line is contained in D3.

3. A real change of basis preserving E acts on E by A in GL3(C), on
conjugate(E) by conjugate(A), and on graph coordinates by
Z -> conjugate(A) Z A^{-1}. Its real determinant is |det A|^2>0;
it preserves the chosen component. Thus every transformed N_ij again
gives a projective line lying in D3 and through E.

For each of the three pairs take N_ij and 2E_ij-(1/2)E_ji, the latter
coming from the real diagonal A with its i-th entry 2. These six vectors
span the six off-diagonal matrices. Also take A=I+iE_ij. Direct
multiplication gives

    conjugate(A) N_ij A^{-1}
      =2E_ij-E_ji+i(E_ii+E_jj).

Modulo the six off-diagonal vectors, these three vectors give the
three diagonal pair sums. Their coefficient matrix has determinant
-2, up to the order of the rows, so they span the three-dimensional
diagonal space. The nine displayed matrices N_a form a basis of M3(C).

4. Uniform transverse thickness is the additional point. For any fixed
rank-two N_a, the map (t,Y) -> graph(t N_a+Y) extends holomorphically
to P1 times a neighbourhood of Y=0. In Pluecker coordinates its
three-column wedge is a polynomial of degree two in t. The coefficient
of t^2 is the wedge of a basis of im N_a in conjugate(E) with
e_k+Y e_k, where e_k is a nonzero generator of ker N_a (after a
fixed change of column basis). Its E component e_k is nonzero, so
that leading wedge never vanishes. Finite-t graph columns are
independent because projection to E is an isomorphism. Homogenizing
therefore gives a base-point-free holomorphic map on P1 times M3(C).

At Y=0 its image is the compact projective line of steps 2–3, contained
in the open set D3. Compactness gives epsilon_a>0 such that every
graph(t N_a+Y), for all t in C and ||Y||<epsilon_a, lies in D3.
This proves a uniform tube, not merely an individual entire line.

5. Let B:C9 -> M3(C) be the isomorphism z -> sum z_a N_a. Choose
epsilon>0 so that ||B(y)|| is below every epsilon_a whenever ||y||<epsilon.
Let T be the union, over ||y||<epsilon, of y plus the union of the
nine coordinate axes. It is an open connected spanning tube by the
given definition: each translated tree meets the epsilon-ball near
its common vertex, and the union contains that ball. The holomorphic
map z -> graph(B(z)) sends T into D3 by step 4. Its differential at
zero is B, an isomorphism; it dominates D3 at E. Applying an oriented
real change of basis carries this construction to every point.

6. The cited tube-domination criterion supplies LSAP and its cited
LSAP implication supplies Oka-1. Their hypotheses are exactly the
uniform tube and surjective differential just constructed. The precise
source loci are opened before the comparison with the printed proof.

## Computational comparison to be performed

A fresh exact matrix program will construct the nine A/N pairs,
verify the action formula, rank two, the nine-dimensional determinant,
and the complementary infinite-limit planes. It will not use the
other checker's program or the source's producing code.
