# Primitive source complements for the reduced III and IV caps

Exact source calculation for the cap construction, 17 November 2026.
The full matrices are in
code/part3_fourfold/primitive_additive_complements.json.
The actual reduced-root cap maps are supplied separately by the
source-classification proof.

Use the integral NS basis and the actual negative-translation
matrix \(T=T_{-G}\) of P3K.22. The three cases are OS47 with its
III fibre removed, OS56 with its III fibre removed, and OS56 with
its IV fibre removed. Write \(p=2,2,3\), respectively.

Let \(B\) denote the unimodular NS Gram matrix. Let \(J\) be the
indices consisting of \(F\) and the \(p-1\) nonidentity components
of the selected additive fibre, and let \(J^c\) be the other
indices. The actual intersection map to the removed components
is
\[
                  D=B_{J,*}.
\]
The full integral source-complement lattice is
\[
 K=B^{-1}_{*,J^c},\qquad P=B_{J^c,*},\qquad
 DK=0,\quad PK=I .
\]
Here \(K\) denotes the matrix of basis columns. Since \(B^{-1}\)
is an integral unimodular basis of the entire NS lattice, these
columns give the entire integral kernel. They do not merely span
a rational kernel or a finite-index sublattice. The actual
translation on it is
\[
                       T_V=PTK,\qquad KT_V=TK .
\]

To identify this lattice with the homology of the actual source
complement \(V\), take a small regular neighbourhood of the
selected reduced III or IV fibre. Its underlying curve is
connected, has \(H_1=0\), and has \(H_2=\mathbb Z^p\). The
excision and Poincare--Lefschetz sequence therefore gives
\(H_2(V)=\ker D\), \(H_3(V)=0\), and \(H_1(V)=\operatorname{coker}D\).
The selected rows of the unimodular matrix \(B\) are surjective,
so this cokernel is zero. The source fibration over the punctured
base has a section. Filling the remaining singular fibres kills
the base loops through that section; the fundamental group of
\(V\) is consequently a quotient of the abelian fundamental
group of a regular elliptic fibre. Its vanishing abelianization
proves \(\pi_1(V)=0\).

The executed Smith forms of \(T_V-I\) are
\[
 \begin{array}{c|c|c}
 \text{source and removed fibre}&\text{Smith form}
          &\operatorname{coker}(T_V-I)\\ \hline
 \text{OS47, III}&(1,1,1,1,1,1,1,0)&\mathbb Z\\
 \text{OS56, III}&(1,1,1,1,1,1,1,0)&\mathbb Z\\
 \text{OS56, IV}&(1,1,1,1,1,1,0)&\mathbb Z .
 \end{array}
\]
The integral kernel is \(\mathbb ZF\). Thus the actual mapping
torus exterior has \(H_1=\mathbb Z\), \(H_2=\mathbb Z\),
\(H_3=\mathbb ZF\), and no higher absolute homology. Its
fundamental group is the suspension \(\mathbb Z\).

The primitive boundary column is computed by the relative-Wang
chain map in notes/part3_reduced_additive_wang.md. Start with
\[
                         Z_0=p(TO-O).
\]
Add the unique rational combination of the removed root
components that makes its intersection with every one of them
zero. The component class of \(G\) generates the order-\(p\)
discriminant group, so this correction is integral after the
displayed factor \(p\); the program also verifies each coefficient
directly. The resulting integral cycle \(Z\) lies in \(\ker D\).
It is exactly the image of the boundary cone cycle over the
invariant meridian \(pq\).

Normalize the primitive cokernel functional by its first nonzero
coordinate being positive, as in the exported matrix. Then the
three actual boundary values are all
\[
                              [Z]=-1.
\]
In contrast, the original line divisor \(M=P_{dG}-O\) has
cokernel values
\[
             7,\qquad15,\qquad10
\]
in these three cases. The line is therefore not the primitive
boundary generator. The exact identity
\((T_V-I)[M]=-[F]\) is retained in every matrix.

Finally the source intersection of \(F\) with \(Z\) is zero.
The compact \(H_2\times H_3\) pairing of the mapping-torus
exterior therefore vanishes. Poincare--Lefschetz duality makes
both middle absolute-to-relative maps zero, and the boundary
map onto its free \(H_2\) is surjective with primitive kernel.
This supplies the integral source side of the reduced-cap
Mayer--Vietoris comparison, with no unknown multiplier in its
second column.
