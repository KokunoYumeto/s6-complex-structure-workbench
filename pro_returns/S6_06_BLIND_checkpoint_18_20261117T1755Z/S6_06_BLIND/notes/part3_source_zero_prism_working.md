# Actual prism cones for the rescaled source-zero period sectors

This is an unpromoted working construction for P3K.39. We retain the
actual pairs \((a,b)=(1,2),(2,1)\), and use the literal scalar
rescaling \(\lambda=v^N\lambda_0\), where \(N=kM\ge6\)
and \(k\) is a positive integer. The one-gamma root parameter is
\(r=v^k r_0\). The fan identities below hold for every integer
\(N>1\); the displayed larger choice also satisfies the actual
residual-contraction estimate in the assembled quotient.
Divisibility by the shorter
fixed-source scalar period alone has not supplied a mixed source/cap
family, so we do not replace this marked parameter by a shorter root.

The period matrices on the three strict-transform sectors and the
exceptional direction are
\[
 I=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad
 W=\begin{pmatrix}1&b\\-a&-2\end{pmatrix},\quad
 E=\begin{pmatrix}0&0\\0&N\end{pmatrix},\quad
 H=I+W+E=\begin{pmatrix}2&b\\-a&N-1\end{pmatrix}.
\]
We use the actual blown-up base sectors \((I,H),(W,H),(E,H)\).
Their base lattice coordinates below are their own two primitive rays.
Their transition to the original base is still carried by the actual
blowup charts in the source-zero working note.

## 1. The exact cones and period maps

For each pair \((P_0,P_1)\) above and \(n\in\mathbb Z^2\), set
\[
 R_0(n)=(P_0n,1,0),\qquad R_1(n)=(P_1n,0,1)
              \quad\hbox{in }\mathbb Z^2\oplus\mathbb Z^2.
\]
The actual integral period action associated with \(m\in\mathbb Z^2\)
is the linear lattice automorphism
\[
 T_m(x,r,s)=(x+rP_0m+sP_1m,r,s).
\]
It has determinant one and sends \(R_i(n)\) to \(R_i(n+m)\).
These are the exponent maps of the actual torus deck transformations;
their remaining holomorphic units act through the same torus and must
still be retained in the analytic quotient.

For \((I,H)\) and \((E,H)\), take \(u=e_1,v=e_2\). For
\((W,H)\), take \(u=e_1,v=e_2-be_1\). This last change has
determinant one and satisfies \(Wv=0\). Triangulate every lattice
square by the triangles
\((n,n+u,n+u+v)\) and \((n,n+v,n+u+v)\). If its ordered
vertices are \(n_0,n_1,n_2\), the three staircase prism cones are
generated respectively by
\[
\begin{split}
 &(R_0(n_0),R_0(n_1),R_0(n_2),R_1(n_2)),\\
 &(R_0(n_0),R_0(n_1),R_1(n_1),R_1(n_2)),\\
 &(R_0(n_0),R_1(n_0),R_1(n_1),R_1(n_2)).
\end{split}
\]
The middle determinant has the opposite column-order sign. After
orienting each triangle by \((u,v)\), their signed determinant rows are

| Sector | First triangle | Second triangle |
| --- | --- | --- |
| \((I,H)\) | \(1,N-1,2N\) | \(1,2,2N\) |
| \((W,H)\) | \(0,N-1,2N\) | \(0,0,2N\) |
| \((E,H)\) | \(0,0,2N\) | \(0,2N,2N\) |

All nonzero entries are positive for the actual integer \(N>1\).
The independent exact certificate is
`code/part3_root/source_zero_prism_fan.py`, with its JSON and standard
output. It checks both actual \((a,b)\) pairs symbolically in \(N\),
every displayed determinant, and every period arrow on the prism rays.

## 2. What the degree calculation establishes

On the slice \(r+s=1\), linearly extend the vertex map from the
staircase triangulation of \(\mathbb R^2\times[0,1]\). Write it
\((x,t)\mapsto(F_t(x),t)\). Its exact periodicity is
\[
 F_t(x+m)=F_t(x)+P(t)m,
 \qquad P(t)=(1-t)P_0+tP_1.
\]
For \(0<t<1\), the matrix \(P(t)\) is invertible: its determinant
is the corresponding positive polynomial
\[
 r^2+(N+1)rs+2Ns^2,\quad
 (N-1)rs+2Ns^2,\quad
 2Nrs+2Ns^2.
\]
Thus \(F_t\) descends to a continuous map from
\(\mathbb R^2/\mathbb Z^2\) to
\(\mathbb R^2/P(t)\mathbb Z^2\). The straight homotopy
between \(F_t(x)\) and \(P(t)x\) is periodic, so this map has
degree one with the displayed orientations. At a value outside the
finite polygonal images of all lower-dimensional pieces, the signed
preimage count equals one. Every nondegenerate piece has positive
Jacobian by the determinant table. It follows that its regular value
has exactly one preimage. Consequently the interiors of the
nondegenerate image cones are disjoint, and their closures cover the
whole fibre plane over every strictly positive base ratio.

This argument does not establish that every intersection is a common
face. It also does not establish injectivity of the raw piecewise
linear map in the rank-one sectors. A zero-determinant tetrahedron
collapses even on an interior slice. The earlier suggestion of raw
injectivity was withdrawn immediately, and this is the corrected
claim. The common-face calculation, or a compatible refinement, is
the next exact step.

## 3. The rank-one sector in explicit coordinates

For the \((W,H)\) sector, the codomain map
\(S=\left(\begin{smallmatrix}1&0\\a&1\end{smallmatrix}\right)\)
and the domain basis \((u,v)\) give
\[
 SW(u,v)=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
 SH(u,v)=\begin{pmatrix}2&-b\\a&N-1\end{pmatrix}.
\]
The additional rational codomain shear
\(\left(\begin{smallmatrix}1&b/(N-1)\\0&1\end{smallmatrix}\right)\)
carries the latter to
\(\left(\begin{smallmatrix}2N/(N-1)&0\\a&N-1\end{smallmatrix}\right)\)
and leaves the first matrix fixed. This rational map is used only to
inspect cone geometry; the actual toric lattice and its primitive
rays remain the integral ones above.

The image on the rank-one base face is the image line of \(P_0\).
The transverse torus coordinate survives. The kernel period must
therefore be quotiented using its actual nonzero contraction unit,
as computed from the source translation and line reset. We have not
replaced this action by a trivial lattice stabilizer or filled its
omitted origin.

## 4. Outstanding analytic and gluing steps

The \(H\) boundary has different chosen square triangulations in
the \(W\) sector and the other two sectors. The independent audit
in `notes/part3_source_zero_prism_audit.md` now supplies the missing
common-face proof and the exact periodic overlay, including its
extension through all three sectors. Thus the open common-face
step recorded in Section 2 has been resolved by that explicit strip
calculation, rather than by determinant positivity alone.

Sections 19--22 of `notes/part3_source_zero_completion_working.md`
give the actual period units, residual contraction bounds, signed
finite-cap chain maps and normal analytic quotient; their intermediate
scope has passed the recorded root and peer audits. The equivariant
regular subdivision is being audited separately. The oriented
fixed-stratum boundary incidence, characteristic number and source
return remain uncomputed. Neither a lattice index nor a local origin
value is used as their replacement.

The subsequent default negative-fan construction, including the
primitive scalar-chain boundary, is proved in
`notes/part3_source_zero_prism_audit.md`. The initial positive-fan
choice and its full audit remain in
`notes/part3_source_zero_prism_positive_audit.md`; no source-loop
identification between these marked boundaries is inserted here.

For comparison, one common symmetric form for all of \(I,W,E\)
would satisfy \(Q_{12}=0\) and
\(Q_{22}=-(b/a)Q_{11}\). Every nonzero such form is indefinite.
This exact linear calculation rules out that proposed common-positive-
form construction. It does not rule out the explicit sector fans
being constructed here.
