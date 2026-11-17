# The exact torsion boundary map for the three complementary good-root caps

Independent calculation for OS47 minus III with \(Q=2G\), OS56
minus III with \(Q=2G\), and OS56 minus IV with \(Q=3G\).
The corresponding lines are \(7G-O,15G-O,10G-O\).
The cap maps and their return calculations belong to the
blind-control construction. This note supplies the complete
integral source-boundary map needed by that construction.

Let \(S\) be the marked rational elliptic source, \(N\) a small
neighbourhood of the selected reduced III or IV fibre, and
\(V=S\setminus\mathring N\). Put \(p=2\) or \(3\), respectively.
Write \(G\) for the full unimodular NS Gram matrix in the saved
basis, and \(T=(T_{-G})^p\) for the actual suspension translation.
Let \(J:\mathbb Z^p\to\mathbb Z^{10}\) have the actual central
component classes as columns, with the identity component first.
Then
\[
                         TJ=J,\qquad Q=J^tGJ.
\]
The central reduced curve is a wedge of \(p\) two-spheres:
III has its two components meeting at one point, and IV has
its three components meeting at one point. Thus \(N\) has
the stated \(0\)- and \(2\)-cell chain model. Its boundary
is not replaced by a cycle-of-spheres plumbing with extra
first homology.

The rational source has a cell chain model with one cell in
degrees zero and four, and the marked ten generators in
degree two. The inclusion of the central components is the
integer map \(J\). These maps are the actual pair maps:
cellular approximation for the pair preserves the inclusion,
and the actual holomorphic translation preserves \(N\) and
the component classes. Its degree-two map is \(T\); the
degree-zero, degree-four, and \(N\)-degree-two maps are
identities. There are no odd cellular differentials in
these source and neighbourhood models.

Poincare--Lefschetz duality for the complement, with the
complex orientation and the NS intersection identification,
gives the uncancelled chain complex
\[
 C_2(V)=\mathbb Z^{10}
       \xrightarrow{\,J^tG\,}C_1(V)=\mathbb Z^p,\qquad
 C_0(V)=\mathbb Z.
                                                        \tag{WAB.1}
\]
Here the additional degree-four to degree-three identity
pair from the source fundamental cell and neighbourhood
zero-cell has already been cancelled. The translation is
the identity on both of those cells, so that cancellation
is equivariant and creates no mapping-torus correction.
The differential to \(C_0\) is zero. Its translation is
\(T\) on \(C_2\), and the identity on \(C_1,C_0\).
The source boundary has
\[
 C_3(\partial V)=\mathbb Z,\quad
 C_2(\partial V)=\mathbb Z^p
       \xrightarrow{\,Q\,}C_1(\partial V)=\mathbb Z^p,\quad
 C_0(\partial V)=\mathbb Z.
                                                        \tag{WAB.2}
\]
The inclusion into (WAB.1) is \(J\) in degree two and the
identity in degrees one and zero, with zero degree-three
map. It is a chain map because \(J^tGJ=Q\). The chosen
local good-root Abel lift of \(pG\), which specializes to
zero, gives the actual translation isotopy on the source
neighbourhood and hence the identity boundary chain map.
Equivalently this boundary map is obtained directly by the
pair-duality construction above; no relative rim coefficient
is omitted.

Here is the explicit cancellation retaining that relative
coefficient. Let \(I_{\rm del}\) select \(F\) and the nonidentity
components of the removed fibre. Write
\[
 J=I_{\rm del}U,\qquad
 U=\begin{pmatrix}
 1&0&\cdots&0\\
 -1&1&&0\\
 \vdots&&\ddots&\\
 -1&0&&1
 \end{pmatrix}.
\]
Let \(K=G^{-1}[:,{\rm retained}]\),
\(P=G[{\rm retained},:]\), and
\(L=G^{-1}[:,{\rm deleted}]\), as in the executed source
calculation. Then
\[
 PK=I,\quad PL=0,\quad
 KP+L\,G[{\rm deleted},:]=I.
\]
Thus the actual degree-two chain group in (WAB.1) splits as
\[
                 K\mathbb Z^{10-p}\oplus LU^{-t}\mathbb Z^p,
\]
and its differential is projection onto the second summand.
In this splitting the translation is
\[
                  \begin{pmatrix}T_V&-H\\0&I\end{pmatrix},
 \quad T_V=PTK,\quad H=-PTLU^{-t}.
                                                        \tag{WAB.3}
\]
Put \(A=PJ\), \(D=T_V-I\). Direct multiplication gives
\[
                              DA=HQ.
                                                        \tag{WAB.4}
\]
The off-diagonal block in (WAB.3) is precisely the data that
would be lost by first cancelling the acyclic pair and
retaining only the absolute homology action.

Apply the actual mapping-torus cone convention
\(d(a,b)=(da+(T-I)b,-db)\). After the cancellation, the
degree-two boundary inclusion on a source component chain
\(a\) and a gamma-crossed source one-chain \(b\) is
\[
                         (a,b)\longmapsto Aa-Hb.
                                                        \tag{WAB.5}
\]
In degree three the gamma-crossed component chain maps by
\(A\). Equation (WAB.4) verifies its differential exactly.
In degree one the gamma generator maps to the common gamma
generator and every source boundary generator maps to zero.

Let \(\alpha=e_0\), and let \(\eta=e_1-e_0\).
In \({\rm coker}\,Q\), the first is a free generator and the
second has exact order \(p\). Formula (WAB.5) gives the
actual two columns
\[
           \alpha\gamma\longmapsto-H\alpha,\qquad
           \eta\gamma\longmapsto-H\eta.
                                                        \tag{WAB.6}
\]
The first agrees with the corrected punctured-section
relative-Wang cycle \(TO-O\), modulo the displayed integral
column \(D(PO)\). No fractional fibre class is used.

All matrices and identities are exported in
code/part3_fourfold/weighted_additive_complements.json.
For the two III cases,
\({\rm SNF}(D)=(1,1,1,1,1,1,2,0)\); for IV it is
\((1,1,1,1,1,3,0)\). In every case, adjoining
\(-H\alpha\) kills the free factor and leaves \(\mathbb Z/p\);
adjoining the actual torsion column \(-H\eta\) gives only
unit Smith factors. Thus the latter maps primitively onto
the exterior torsion. The fibre column \(F\) also generates
that torsion, as independently checked by adjoining it.

The resulting exterior groups are
\[
 H_1=\mathbb Z,\qquad H_2=\mathbb Z\oplus\mathbb Z/p,
 \qquad H_3=\mathbb Z F.
\]
The line \(M\) is recorded as the integral cohomology
functional \(K^tGM\) on the source complement. Its removed
component degrees are nonzero, so its divisor class was
not silently used as a compact homology generator.

Blind-control independently obtained the same torsion
surjectivity from its full uncancelled cone in
code/part3/ordinary_additive_boundary.py. The two calculations
retain their respective integer bases and exact matrices.
