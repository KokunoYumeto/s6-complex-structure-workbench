# Exact p-one Cayley cells for the common-fan extension

Local calculation sent to checks before checkpoint24, with the full
common 510-cone extension completed below. The executed refinement has
558 regular four-dimensional cones and retains the complete source,
point-line and period morphisms.

Use the actual p-one characters of E96, with \(v=p-1\),
\(W_C=s_\Delta\cdot ZV_T\), where \(s_\Delta\) is the actual
point-line coefficient retained in E90. Their full periods are
\[
h:(Z,W_C)\mapsto(P^3pZ,p^{-2}W_C),\qquad
B:(Z,W_C)\mapsto(P^{-1}Z,P^3v^4cW_C).
\]
For source cell i and line cell j,
\(x=Z/P^i\), \(y=P^{i+1}/Z\),
\(U=W_C/(P^3v^4)^j\), \(V=(P^3v^4)^{j+1}/W_C\).
Thus \(UV=x^3y^3v^4\). The ordered factors are three x,
three y and four v. The ten actual charts are the ones in
code/part3/e6_p_one_corner.py; h shifts \((i,j)\) to
\((i+3,j)\), and B to \((i-1,j+1)\), with every displayed
unit retained.

In the native lattice
\(N=(\operatorname{ord}Z,\operatorname{ord}W_C,
\operatorname{ord}P,\operatorname{ord}v)\), for j zero put
\[
I_r=(i+1,r,1,0),\quad J_r=(i,r,1,0),\quad E_r=(0,r,0,1).
\]
The ten cones are exactly
\[
\begin{gathered}
(I_{r-1},I_r,J_0,E_0),\quad1\le r\le3,\\
(J_{r-1},J_r,I_3,E_0),\quad1\le r\le3,\\
(E_{r-1},E_r,I_3,J_3),\quad1\le r\le4.
\end{gathered}
\]
Each determinant has absolute value one. Thus the four consecutive
lower intervals join precisely the upper edge \(I_3J_3\) of
their source cell. The first six cones are the E0 stars of the
six generic upper triangles retained by the common fan.

The full point-line relation is
\(P^3W_C=pU_6 f_{p^{-2}}(Z)v_M\). This follows from the
literal theta reindex twice:
\(f_{P^6}(Z)=Z^2/(Q^3p^{-4})\,f_{p^{-2}}(Z)\),
\(Q=P^3p\). The vertical Cartier factor P cubed remains.

For the common-fan implementation, a recorded one-parent translate
\(K^rJ^s\) first has its height translation
\((5r+s,r+2s)\) subtracted from each common ray; then the
inverse of \(A_{\infty1}=\left(\begin{smallmatrix}-1&1\\1&0
\end{smallmatrix}\right)\) gives its native upper ray. The
E0 stars and subdivided top edges then give the native four-cones.
The full map back to common characters must retain
\(b=v^{-4}c^{-1}\). Its lower v ray consequently contributes
\(4(2r+s)\) to the common \(V_{\rm reg}\) valuation, and its
coefficient is
\(p^{-6-3r-3s}c^{2r+s}\); the Z coefficient is \(p^{r+s}\).
These are the actual period/character arrows, including all
vertical powers. Treating b as a bounded unit at v zero would
omit this part of the map.

## PC.1. Pulling the complete common boundary into its native parents

For a common upper ray \((A,B,h)\), let \((r,s)\) be the literal
period translate saved in its `one_parent` record. Put
\[
 A_0=A-(5r+s)h,\qquad B_0=B-(r+2s)h.
\]
The native ray is \((B_0,A_0+B_0,h,0)\). This applies the inverse
of the displayed character map after undoing the saved period word.
It carries every cone to its recorded source cell and one of its six
upper factor parents. In particular its inverse is integral and its
determinant has absolute value one. The 510 resulting upper cones
have disjoint interiors, since the original common fan has this
property and every map on a common parent is the same invertible
linear map. On a shared parent face the two maps agree by the saved
period translation. Their total height-one area is exactly nine.

Join each of these 510 cones to \(E_0\). On the upper edge
\(I_3J_3\) of each of the three source cells the common fan gives
four primitive intervals. Each interval with endpoints
\((z_0,3h_0,h_0)\), \((z_1,3h_1,h_1)\) satisfies
\(\lvert z_0h_1-z_1h_0\rvert=1\). Their rational lengths
sum to one in each source cell. Join these four intervals to each
of the four consecutive lower intervals \(E_kE_{k+1}\),
\(0\le k\le3\). This adds 48 four-cones. It is the literal
subdivision of the last four factor parents, whose upper edge was
already specified by the ordered-factor atlas.

Thus the full list contains 558 four-cones. In the executable list
each is oriented by a recorded permutation to have determinant
\(+1\). If \(N\) is its ordered ray matrix and \(N_0\) its
original factor-parent matrix in the actual free-coordinate order,
then \(N_0^{-1}N\) is a nonnegative integral matrix. The parent
coordinate map is
\[
 x_{0,i}=\prod_{j=1}^4\theta_j^{(N_0^{-1}N)_{ij}}.
\tag{PC.1}
\]
All exponents are saved. This is the chart morphism into the
original ordered-factor resolution, including its source and line
functions, rather than only a containment of ray supports.

For completeness, intersect each parent with the positive hyperplane
\(\operatorname{ord}P+\operatorname{ord}v=1\). The exact volume
of the simplex of a cone with primitive columns \(n_i\) is
\[
 \frac{\lvert\det(n_1,n_2,n_3,n_4)\rvert}
 {6\prod_i(n_{i,P}+n_{i,v})}.
\tag{PC.2}
\]
The new volumes sum to the old one separately in all 30 original
parents. The upper subdivisions and the lower interval joins have
disjoint interiors as just described. Their common faces are the
inherited common subdivisions. This proves full support and gives
the proper toric modification of these original affine charts.
It also preserves all source and parameter multiplicities.

## PC.2. Full corner characters and the shared period facets

The full map from native valuation variables \((z,w,h,t)\) to a
common chart with period translate \((r,s)\) is the integral matrix
\[
 F_{r,s}=
 \begin{pmatrix}
 -1&1&5r+s&4(2r+s)\\
 1&0&r+2s&0\\
 0&0&1&0\\
 0&0&0&1
 \end{pmatrix}.
\tag{PC.3}
\]
Its coefficient vectors are
\[
 p^{(-6-3r-3s,\ r+s,\ 0,\ 0)},\qquad
 c^{(2r+s,\ 0,\ 0,\ 0)}.
\tag{PC.4}
\]
Equations PC.3--4 substitute the actual \(b=v^{-4}c^{-1}\)
before extending the chart. Thus its lower ray has the required
\(4(2r+s)\) first component. For every new cone the saved
common-character exponent matrix is exactly \(F_{r,s}N\),
with PC.4 as its coefficient. A separate check recomputes each
persisted matrix from that cone's own rays. The map retains the
vertical divisor and every original unit, including their parameter
dependence.

The actual native period matrices on the full four-lattice are
\[
 H=\begin{pmatrix}1&0&3&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix},
 \qquad
 B=\begin{pmatrix}1&0&-1&0\\0&1&3&4\\0&0&1&0\\0&0&0&1\end{pmatrix}.
\tag{PC.5}
\]
They commute. The coefficient of \(H^rB^s\) is
\(p^{(r,-2r,0,0)}c^{(0,s,0,0)}\), since both maps fix
the full base functions \(P,v,p,c\). The incidence list has 510
generic boundary facets and 38 further boundary facets. Every one
of the latter is paired by an explicitly saved word \(H^rB^s\),
with \(r,s\in\{-1,0,1\}\). All internal three-facets occur
exactly twice.

For a paired face from cone \(N_s\) to cone \(N_t\), its full
chart map is
\[
 \theta'_i=p^{(N_t^{-1}(r,-2r,0,0)^t)_i}
 c^{(N_t^{-1}(0,s,0,0)^t)_i}
 \prod_j\theta_j^{(N_t^{-1}H^rB^sN_s)_{ij}}.
\tag{PC.6}
\]
All exponents are integral. The columns along the shared face
are nonnegative; only the recorded coordinate away from that
face is inverted. Therefore PC.6 is an actual morphism on the
localized face chart, with inverse given by the inverse period
word and the inverse character matrix. Its coefficients retain
the same holomorphic functions \(p\) and \(c\). These maps
commute with the source and point-line expressions because they
are precisely the original \(h,B\) maps on the dense torus and
both sides extend by the stated monomials. The holomorphic
identities consequently hold on the whole overlap.

## PC.3. Source, physical line, and inherited determinant

On every new cone the source coordinates
\[
 Z_0=Z,\qquad W_0=pP^3/Z,\qquad Z_0W_0=pP^3=Q
\tag{PC.7}
\]
are holomorphic. Their exponent rows are respectively
\((1,0,0,0)N\) and \((-1,0,3,0)N\), both nonnegative;
the latter has the full coefficient \(p\). This covers the
complete source cell used here, including its node. The point
and O coincidence graph still uses its actual generators and
the original theta/Cartier map. In particular the line arrow is
still \(P^3W_C=pU_6f_{p^{-2}}(Z)v_M\): PC.1 and PC.6
carry the factor \(P^3\) literally, without replacing it by a
unit at the new boundary.

The physical cocharacter is \(\delta=(0,1,0,0)\).
In every chart its full weight vector is \(N^{-1}\delta\),
saved as four integers. The inherited original four-form from
E83/E94, after \(R=pP\) and \(v=p-1\), is a nowhere-zero
unit times
\[
 P\,dP\wedge dv\wedge d\log Z\wedge d\log W_C.
\tag{PC.8}
\]
Its order on a primitive ray \((z,w,h,t)\) is therefore
\(2h+t-1\). These complete orders and the actual base heights
are recorded for every ray. The coefficient in PC.8 is the
original \(2J_{ts}/a_{\rm T}\), with all frame derivatives
retained; source-dependent line logarithms wedge to zero with
the source three-form by E83.2. No determinant or Spin lift is
selected by deleting this divisor.

The complete executable construction is
`code/part3_fourfold/e6_p_one_common_cayley.py`, with its JSON and
stdout. It records every primitive ray, oriented cone, native
parent map, full common-character map, period face and localized
unit map. The original export before the per-cone reference-copy
repair is retained under
`records/attempts/e6_p_one_common_cayley_reference_alias/`.
The complete point/O graph, compact global end attachment, its
Spin extension and the characteristic return remain separate
unfinished constructions; this proof assigns no such value.
