# Selected-cusp source loop: the two nonfixed edge products

Working record after P3K.42. The actual source loop and physical
delta action are retained. The full common-exterior variation and
derivative have not been computed here. The exact chart arrows below
are the inputs to that computation; the restricted diagonal-gauge
calculation is recorded to prevent an unjustified application of
P3K.29's simultaneous-product hypothesis.

## OE.1. The physical-height six-chart atlas

Use the height character given by the original source coordinate
\(q\), with multiplicative source coordinate \(Z\) and line
coordinate \(V\). For \(n=(i,j)\in\mathbb Z^2\), the two
unimodular triangle charts are
\[
 \begin{array}{c|ccc}
 &q&Z&V\\ \hline
 T^+_n&x_0x_1x_2&q^i x_1&q^j x_2\\
 T^-_n&y_0y_1y_2&q^i y_0y_1&q^j y_0y_2.
 \end{array}                                                   \tag{OE.1}
\]
The two actual period generators, in the contracting suspension
convention, are
\[
 h:(Z,V,q)\mapsto(\kappa qZ,\alpha V,q),\qquad
 B:(Z,V,q)\mapsto(gZ,\eta qV,q),\quad \eta=\lambda\beta.
                                                               \tag{OE.2}
\]
Here \(\kappa=q_T/q\) has rho winding \(-6\). The source
Picard multiplier \(\alpha\), the source translation multiplier
\(g\), and the original Hom quotient \(\beta\) are the actual
functions of F54/F56. Their rho winding is zero and their specified
logs extend over the source parameter disc. The scalar \(\lambda\)
is fixed. We do not replace the physical height character by \(q_T\).

A bounded torus multiplier \((Z,V)\mapsto(AZ,BV)\) acts in
these charts by
\[
 T^+:(x_0,x_1,x_2)\mapsto((AB)^{-1}x_0,Ax_1,Bx_2),
\quad
 T^-:(y_0,y_1,y_2)\mapsto(ABy_0,B^{-1}y_1,A^{-1}y_2).
                                                               \tag{OE.3}
\]
Every displayed map is an actual monomial character map multiplied
by the given unit. It preserves the physical height \(q\).

Write \(T^+_0=(a,b,c)\), so \(q=abc,Z=b,V=c\), and write
\(T^-_0=(u,v,w)\). The three adjacent pairs are
\((T^+_0,T^-_{-e_1})\) for the fixed vertical edge,
\((T^+_0,T^-_{-e_2})\) for the horizontal edge, and
\((T^+_0,T^-_0)\) for the diagonal edge. Apply the literal
period in (OE.2) to bring the negative-index chart to the named
representative. The resulting arrows are
\[
 \begin{array}{c|ccc}
 &u&v&w\\ \hline
 C_0\text{ (fixed)}&\kappa\alpha bc&\alpha^{-1}ab&\kappa^{-1}b^{-1}\\
 C_1\text{ (horizontal)}&g\eta bc&\eta^{-1}c^{-1}&g^{-1}ac\\
 C_2\text{ (diagonal)}&a^{-1}&ab&ac.
 \end{array}                                                   \tag{OE.4}
\]
The triple product in every row is exactly \(q\). The tangent
coordinates at the first vertex are respectively \(b,c,a\), and
at the second vertex respectively \(w,v,u\). The physical delta
weights at the two vertices are
\[
             (-1,0,1)\quad\text{and}\quad(1,-1,0).
                                                               \tag{OE.5}
\]
Thus the last two curves have free delta orbits away from their
two endpoints, while the first curve is fixed pointwise.

## OE.2. Each nonfixed star separately has an explicit closed product

For \(C_2\), the last row of (OE.4) already gives the exact
normal transition
\[
                  u=a^{-1},\qquad (v,w)=a(b,c).           \tag{OE.6}
\]
There is no parameter unit in this two-chart star. It is the
specified \(\mathcal O(-1)\oplus\mathcal O(-1)\) product,
with its actual delta weights.

For \(C_1\), make the literal coordinate changes in its second
chart
\[
       \widetilde v=\eta v,\qquad
       \widetilde w=g w,\qquad
       \widetilde u=(g\eta)^{-1}u.                       \tag{OE.7}
\]
They are invertible holomorphic unit maps, are periodic on the
actual rho circle, commute with delta, and preserve \(q\).
They yield
\[
        \widetilde v=c^{-1},\qquad
        (\widetilde w,\widetilde u)=c(a,b).               \tag{OE.8}
\]
The source and Hom logs in F56 give the exact interpolation of
(OE.7) with the original coordinates, retaining their initial
constant values. Thus (OE.8) is a closed actual product for this
single star. Its possible compatibility with the fixed-edge product
at the common vertices is a separate calculation.

## OE.3. A restricted simultaneous diagonal-gauge attempt

This paragraph records an exact limitation of a specific attempted
construction. It does not assert that all smooth equivariant
simultaneous products are obstructed.

Let diagonal parameter gauges at the two vertex charts have factors
\((A,B,C)\) and \((U,V,W)\), and retain the ordered three
axes. A product of the three pointed curves gives the tangent
relations
\[
                  AU=1,\qquad CV=\eta,\qquad BW=\kappa.
                                                               \tag{OE.9}
\]
In a fixed-edge product, the two weight normal lines cannot be
mixed. Put \(Q=ABC\). Their transition factors after (OE.9)
are, respectively,
\[
                       \frac{\eta}{\alpha Q},\qquad
                       \frac{\kappa\alpha}{Q}.           \tag{OE.10}
\]
To interpolate each of these diagonal factors to a parameter-
independent transition while keeping the chosen vertex products,
its rho winding must vanish. Hence the two necessary winding
equalities for this restricted construction are
\[
 \operatorname{wind}Q=\operatorname{wind}\eta-\operatorname{wind}\alpha,
 \qquad
 \operatorname{wind}Q=\operatorname{wind}\kappa+\operatorname{wind}\alpha.
                                                               \tag{OE.11}
\]
They give zero and \(-6\) in the actual source loop. Thus the
diagonal vertex-gauge attempt does not produce the required
simultaneous product. In particular, the separate products (OE.6)
and (OE.8) cannot simply be declared identical to K42's fixed-edge
product at both vertices.

The next calculation must either construct a more general actual
common-exterior product with all its frame maps, or compute the
relative entries in the separate products and their exact transition.
No rank-one variation or zero nonfixed derivative is inferred from
the numerical pair \((6,0)\).

## OE.4. Exact even-winding factorization of the residual seam

After the extending zero-winding unit gauges, write the residual
source phase as \(\kappa=e^{-6i\theta}\). In the second vertex
chart, one direction of the retained seam has weights
\((-6,0,6)\) on \((u,v,w)\); its inverse has the opposite
weights. The fixed curve is the \(w\)-axis and the normal delta
weights are \((1,-1)\) on \((u,v)\).

Take the actual base \(SU(2)\) loop on the homogeneous coordinate
of the fixed curve
\[
                 A_\theta=\operatorname{diag}
                            (e^{3i\theta},e^{-3i\theta}).
                                                               \tag{OE.12}
\]
At this pole, its action on the tautological normal bundle and the
base tangent is \((-3,-3,6)\). The physical delta loop
\(e^{-3i\theta}\) adds \((-3,3,0)\), so their actual product
has precisely \((-6,0,6)\). At the other pole the same global
bundle map has weights \((6,-6,0)\) on \((a,b,c)\).
Thus this is an explicit transfer of the seam between the two
vertices, not a simultaneous cancellation at both.

In the retained fixed-edge product its literal map is
\[
 (h,q_H)\longmapsto
       (A_\theta hA_\theta^{-1},
                           A_\theta q_H e^{-3i\theta}).  \tag{OE.13}
\]
It is periodic, commutes with the physical right circle, and extends
over \(D^3\times S^3\) by the same formula. Consequently it is
compatible with the product cap of P3K.42. The right scalar is
retained, even though it disappears on the adjoint orbit normal.

The \(SU(2)\) loop in (OE.12) does have a concrete disc filling.
In right-complex matrix coordinates one may use the unit vector
\[
       \bigl(r^3e^{3i\theta},\sqrt{1-r^6}\bigr),
       \quad 0\le r\le1,
                                                               \tag{OE.14}
\]
as its first column and the determinant-one orthogonal second
column. This is smooth at the centre. A radial reparametrization
that is flat at the boundary makes a smooth collar without
changing the boundary loop. Its central matrix is the constant
quarter-turn; a constant path joins that matrix to the identity.

This contraction carries nontrivial marked-point information. The
first column's projective map sends the boundary to \([1:0]\)
and the centre to \([0:1]\). A generic finite nonzero value has
exactly three preimages, each with positive local orientation,
as is seen from the coordinate
\(r^3e^{3i\theta}/\sqrt{1-r^6}\). Its degree is therefore
\(+3\). The orthogonal marked point has degree \(-3\).
Thus a claim that the contraction also fixes both attachments or
has zero relative derivative would discard an actual degree.
The extension through the two nonfixed tubes, with these two
marked-point maps and their line lifts, remains to be computed.

The exact monomial and unit identities are executed in
code/part3/source_cusp_other_edges.py.

## OE.5. The full labelled equivariant product obstruction

P3K.47, proved in notes/part3_source_cusp_product_obstruction_working.md,
extends the precise endpoint calculation to arbitrary smooth equivariant
normal maps, including full GL(2,C) mixing along the fixed curve. Its
determinant square has the actual obstruction
\(\operatorname{wind}\kappa+2\operatorname{wind}\alpha-
\operatorname{wind}\eta=-6\). Hence the simultaneous labelled,
complex-orientation-preserving equivariant plumbing product does not
exist for this family. This does not invalidate the separate products
above or the reflected fixed-edge cap comparison of P3K.46. The remaining
all-fan work must retain this nontrivial boundary clutch, or supply a
different explicit global representative and its comparison with the
actual curves. No nonfixed relative integer is assigned here.
