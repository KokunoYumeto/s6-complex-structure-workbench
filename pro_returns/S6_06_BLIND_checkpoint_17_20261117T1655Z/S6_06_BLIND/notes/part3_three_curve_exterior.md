# The marked common exterior of the three cusp double curves

Working reduction for the remaining finite-isotropy fan branches.
This gives the actual integral groups and inclusion maps of the
common exterior, but does not identify the relative Pontryagin
four-cycle of a second edge.

Let \(C=C_0\cup C_1\cup C_2\subset S^6\) be the three marked
double curves of the index-one cusp. Each \(C_i\) is a complex
projective line, and all three meet at the same two triple
points. The local maps are the three coordinate axes in the
two smooth charts with base monomial \(q=x_0x_1x_2\).
Take small coordinate balls at the two vertices and tubes
along the six intervening complex arcs, with the normal
orientations induced by the complex charts. Their rounded
regular neighbourhood is \(N(C)\); put
\(E_C=S^6\setminus\mathring N(C)\).

Give each sphere two oriented edges \(a_i,b_i\) joining the
two marked vertices and two oriented faces with boundaries
\(a_i-b_i\) and \(b_i-a_i\). This is an actual CW structure on
the union, with differential matrices
\[
 C_2=\mathbb Z^6\xrightarrow{D_2}C_1=\mathbb Z^6
     \xrightarrow{D_1}C_0=\mathbb Z^2,\qquad
 D_1=\begin{pmatrix}-1&-1&-1&-1&-1&-1\\
                     1&1&1&1&1&1\end{pmatrix},
\]
where \(D_2\) consists of three diagonal blocks
\(\left(\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\right)\).
The three sums of the two faces are the oriented classes
\([C_i]\). The two marked one-cycles are
\(a_1-a_0,a_2-a_0\). The program below checks that these
are full primitive bases, not finite-index sublattices.
Thus
\[
       H_2(C)=\mathbb Z^3,\qquad H_1(C)=\mathbb Z^2.
\]

Triangulate the two coordinate-ball models and their tubes
compatibly with this CW subdivision. The ordinary dual-cell
construction in the oriented six-sphere identifies the
reduced complement chains with the shifted cochains of
\(C\): a \(j\)-cell is intersected once by its oriented
normal dual cell. This is the Alexander-duality chain map
in the present marking, with no torsion quotient. It gives
\[
 H_3(E_C)=\mathbb Z^3,\qquad H_4(E_C)=\mathbb Z^2,
\]
and no other positive reduced homology. The three
degree-three generators are the positive normal meridians
of the \(C_i\); they have linking number \(+1\) with the
corresponding complex sphere and zero with the other two.
The degree-four generators are the dual-cell cycles of the
two displayed one-cycles. This also specifies them at the
triple-point charts, where a bare product description of a
rim would be insufficient.

The complement is simply connected by relative general
position: a loop bounds a disc in \(S^6\), and its disc can
be made disjoint from the two-dimensional strata and the
two zero-dimensional strata, with its boundary fixed.
The same argument transports through the regular-neighbourhood
retraction to \(E_C\).

For a chosen curve \(C_i\), let
\(E_i=S^6\setminus\mathring N(C_i)\). The exact inclusion
\(E_C\hookrightarrow E_i\) fills the other two tubular
pieces and the corresponding vertex collars. In the
meridian bases its map on \(H_3\) is the literal coordinate
projection
\[
                  (m_0,m_1,m_2)\longmapsto m_i,
\]
because normal meridians of either filled sphere bound
their normal four-discs. Its \(H_4\) map is zero.
Haefliger's unknottedness result already verified in K23
identifies \(E_i\) with \(D^3\times S^3\), with that marked
normal meridian. The exact relative sequence therefore gives
\[
 H_5(E_i,E_C)=\mathbb Z^2,\qquad
 H_4(E_i,E_C)=\mathbb Z^2,
\]
and no other positive relative group. The first boundary
map is the isomorphism onto \(H_4(E_C)\), and the second
identifies with the kernel spanned by the other two
meridians in \(H_3(E_C)\).

Small meridian representatives for the three distinct
curves are pairwise disjoint. Hence the absolute
three-dimensional intersection map of \(E_C\) vanishes.
Poincare--Lefschetz duality and the boundary sequence give
\[
 H_1(\partial E_C)=\mathbb Z^2,\quad
 H_2(\partial E_C)=\mathbb Z^3,\quad
 H_3(\partial E_C)=\mathbb Z^3,\quad
 H_4(\partial E_C)=\mathbb Z^2.
\]
The maps in degrees three and four to \(E_C\) are
isomorphisms in the above dual-cell bases.

The still required comparison is precise. The selected
edge's relative doubled \(D^3\times S^1_{\rm parameter}\)
four-cycle must be transported through the two displayed
relative groups, with the actual Cox normal frames at both
triple points. The Thom identity of
notes/part3_equivariant_thom_work.md gives its local
Pontryagin change after that pullback; it does not choose
the pullback. Nor does the vanishing of the absolute
Pontryagin class choose it. The integer relative
coordinates \(m=-k+6A\) and \(n=-6A\) are both retained.

The exact cellular certificate is
code/part3_fourfold/three_curve_exterior.py and its JSON.
