# Selected-I3: compact generic fixed curves with full normal clutches

This is the curve contribution in the executed three-end atlas. The
source is SI3 with its corrected local unit c0=(p-1)^4c, the generic
common fan has 4,264 cones, its zero and infinity corners have 4,402
and 4,308 regular four-cones, and I3P supplies the 4,392-cone one
corner. The calculation below retains each final protected-facet
owner, its actual period word, and all source/point-line units.
It does not assign the global completed return.

## I3C.1. Actual fixed curves and their three endpoint charts

Use the common torus (V_reg,Z,R), with physical vector (1,0,0).
For a regular common cone N with columns n_i=(X_i,Y_i,h_i), put
w=N^{-1}(1,0,0). All w_i are integers. The fixed stratum over the
generic exceptional base is a curve precisely for the recorded
cones with all three w_i nonzero: in its actual three normal
coordinates every coordinate must vanish. There are 3,422 such
cones. The same cone has no nontrivial period stabilizer. Indeed
a translation preserving its bounded height-one triangle preserves
its centroid, so the period vector is zero; the exact period matrix
[[7,2],[1,2]] has determinant12, which makes the two period labels
zero.

At p=0 and infinity use the final protected generic-facet records
in e6_selected_i3_generic_corner_index.json. They specify the
untranslated upper rays, the original parent K,J word, the full
native period from that input to its actual corner owner, and all
three columns of the owner face. At p=1 use the corresponding
common-cone reference in the I3P upper star. These are face maps
in the final atlases, after their actual regular subdivisions.
The remaining column has base order exactly1 at each of p=0,
v=p-1=0, and u=p^-1=0. Thus the local curve coordinate is that
actual base parameter with first order, not a finite cover of it.
The full dense overlap carries p identically. Gluing these three
endpoint discs to the common punctured base gives the actual
P1_p curve, with its complex orientation.

## I3C.2. Complete directed normal coefficient maps

Let the zero parent's saved K,J shift be (r,s). From the native
lattice (ord Z,ord V_pt,ord p,ord P), its full common character
matrix is
\[
 F_0=\begin{pmatrix}
 -3&1&-6-r-2s&6+7r+2s\\
 1&0&r+s&r+2s\\
 0&0&1&1
 \end{pmatrix}.
 \tag{I3C.1}
\]
Its unit is ((p-1)^4c)^(2r+s)U_6 in the first common character.
This is the entire point map V_reg=p^-6P^6U_6Z^-3V_pt followed
by the saved period word; in particular its third row is R=pP.

If the stored input-to-owner native h,B word is (a,b), define
\[
 T_0(a,b)=\begin{pmatrix}
 1&0&a&3a-b\\0&1&b&6a+2b\\0&0&1&0\\0&0&0&1
 \end{pmatrix}.
 \tag{I3C.2}
\]
The owner-to-common map is F_0T_0(-a,-b). Its complete unit in
the first character is ((p-1)^4c)^(2r+s-b)U_6. This keeps the
full c0 dictionary before any normal degree is taken.

At p=1 the owner-to-common matrix is the first three rows of
the actual I3P F_(r,s), including its v exponent8r+4s. Its
unit vectors are p^(-6-r-2s,r+s,1) and c^(2r+s,0,0).
At infinity, with owner word (a,b) in K,J, put
\[
 T_\infty(a,b)=\begin{pmatrix}
 1&0&0&7a+2b\\0&1&b&a+2b\\0&0&1&0\\0&0&0&1
 \end{pmatrix}.
 \tag{I3C.3}
\]
In native order (V_reg,Z,u,R) the common map is the projection
to coordinates1,2,4 after T_infinity(-a,-b). Its first-character
unit is f^(-2a-b), where f=(1-u)^4c(P=Ru,R). These maps preserve
the original direct point coefficient, with its full inverse
available on the same torus and localized face charts.

For each end let N_e be the final owner matrix and L_e its
displayed owner-to-common matrix. The full normal-coordinate
arrow is N^{-1}L_eN_e, with the unit vectors multiplied by the
same N^{-1}. Its three protected-face columns are the appropriate
permutation of the three unit coordinate columns. The fourth
column gives integers o_(e,i). Consequently the directed local
coefficient map is
\[
 z_i^{\rm common}=q_e^{o_{e,i}}u_{e,i}\,z_i^{\rm end},
 \qquad(q_0,q_1,q_\infty)=(p,p-1,p^{-1}).
 \tag{I3C.4}
\]
Every u_(e,i) is the full nonvanishing analytic unit just specified;
the certificate stores its individual p,c,U_6 or f powers. On
their common local domains the two directed maps reconstruct the
same torus characters, so they give the actual normal bundle
transition, with all parameter derivatives. The units have zero
order on their stated end discs; none of their nonunit p or v
powers was deleted to obtain this fact.

The normal line degrees in this coefficient direction are
\[
 d_i=-o_{0,i}-o_{1,i}-o_{\infty,i}.
 \tag{I3C.5}
\]
The sign follows from the meromorphic normal section with common
coefficient1: in the end frame its coefficient is q_e^(-o_(e,i))
times the inverse extending unit. This gives exactly the indicated
divisor, including all three ends.

## I3C.3. Original determinant and finite-isotropy residue

The complete R character has degree minus one on these curves:
\[
 \sum_i h_i d_i=-1.
 \tag{I3C.6}
\]
This equality is checked from every actual end matrix. The
original canonical orders on the generic rays are 2h_i-1,
with the original source-volume unit retained in SI3. Thus
\[
 \sum_i(2h_i-1)d_i=-2-\sum_i d_i,
 \tag{I3C.7}
\]
which is the actual adjunction identity for the completed P1.
This also checks the normal-clutch direction against the original
canonical divisor, without choosing a Spin trivialization.

Apply the weighted fixed-normal expression already proved in
SZ.57--59 and IE.4--5 to these actual normal characters. Write
P_w=w_1w_2w_3 and S_d=sum_i d_i/w_i. For the positive generator
U the two characteristic terms are
\[
 k_U=-\frac{S_d}{P_w},\qquad
 \ell_U=\frac{2\sum_i w_id_i-(\sum_iw_i^2)S_d}{P_w}.
 \tag{I3C.8}
\]
They are the coefficient of the base generator in the full
weighted Euler denominator, using integral degree d_i on the
complex P1 and p1(TP1)=0. This is the literal finite-chart
orbifold integration: all weights and their denominators are
retained. The physical line is M=U*, so the inner terms are
(-k_U,-ell_U). Their residue is (4k_M-ell_M)/24. No outer
boundary or Jin parameter orientation is applied in this note.

## I3C.4. Exact scoped sum and reproducibility

The 3,422 compact curves have total physical-M inner pair
\[
 \left(
 \frac{48546878069543671}{5199567557184000},\quad
 \frac{4495914136061841821}{15598702671552000}
 \right)
 \tag{I3C.9}
\]
and inner residue
\[
 -\frac{3913351599227317769}{374368864117248000}.
 \tag{I3C.10}
\]
These are exact rational sums of the stated curve contributions.
The compact surfaces, interior corner points, four lower surfaces,
moving fixed graph and its normal/physical Hopf cap, reference
subtraction and outer transfer are not included in these numbers.

The complete code/part3/e6_selected_i3_fixed_curve_normals.py
exports every common cone, all three actual owner maps, full unit
vectors, normal weights/degrees, original canonical degree and both
individual characteristic terms. Its final run locks the full
inputs and this proof and rechecks that none changed during the
execution. The algebraic residue identity is checked independently
for each row and for the sum. The initial execution before the
complete proof lock is retained under records/attempts.
