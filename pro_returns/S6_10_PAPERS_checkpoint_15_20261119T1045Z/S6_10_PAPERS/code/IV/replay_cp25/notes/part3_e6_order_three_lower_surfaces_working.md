# The four lower p=1 fixed surfaces and their complete boundary frames

This calculation describes the native finite-domain fixed surfaces in
E96 and the exact maps to the side-annulus chain E104. It supplies the
source, normal, point-line and determinant arrows needed for the relative
exterior calculation. The characteristic numbers of the closed
collision/reference doubles and the outer Jin completion are not
evaluated here.

## LS.1. Actual source and line charts

Retain the actual functions
\[
 v=p-1=\frac{s u_s}{P},\qquad Q=P^3p,
 \qquad c=\lambda _0qK u_s^{-4}.
 \tag{LS.1}
\]
The finite domain is the original source-base domain
\(|t|\leq\eta\), restricted at \(s=0\); it is carried to the
\(P\)-coordinate by the actual source function. The finite outer
boundary is retained. On the source and line covers use
\[
 x_i=Z/P^i,\quad y_i=P^{i+1}/Z,\qquad
 U_j=\frac{W_C}{(P^3v^4)^j},\quad
 V_j=\frac{(P^3v^4)^{j+1}}{W_C}.
 \tag{LS.2}
\]
Thus \(x_i y_i=P\) and \(U_jV_j=P^3v^4\). For
\(l=0,1,2,3\), the actual lower factor chart is
\[
 v=ab,\qquad U_j=P^3v^l a,\qquad
 V_j=v^{3-l}b,\qquad (x_i,y_i,a,b).
 \tag{LS.3}
\]
The physical action has characters \((0,0,+1,-1)\).
Its fixed set in this chart is precisely \(a=b=0\).
The complete chronological periods are
\[
\begin{split}
 h:(i,j;x,y,a,b)&\longmapsto
 (i+3,j;px,p^{-1}y,p^{-2}a,p^2b),\\
 B:(i,j;Z,a,b)&\longmapsto
 (i-1,j+1;P^{-1}Z,ca,c^{-1}b).
\end{split}
\tag{LS.4}
\]
The adjacent source-chart map is
\((x,y)\mapsto(1/y,xy^2)\), and leaves \(a,b\) unchanged.
Every factor in LS.4 is the original function on the source bidisc.
The inverse maps use the inverse index shifts and reciprocal functions.

The point-line coordinate is the typed coordinate of E96.2:
\[
 W_C=s\Delta ZV_{\rm T},\qquad
 P^3W_C=pU_6 f_{p^{-2}}(Z)v_M.
 \tag{LS.5}
\]
In particular its \(P^3\) factor is retained. At the point/O
coincidence the actual Cartier module generator
\(e=(Z-1)/(Z-b_2)\), \(b_2=p^{-2}\), is carried by
\(f_{b_2}\) to \(b_2^{-1}E_O\). This is the nonzero extending
module map E99.7--8; it provides the actual point-line extension
through that coincidence. It does not remove the factors in LS.5.

## LS.2. The literal source quotient and normal frames

Apply the existing arrow \(B^{-j}\) to a point in the chart
labelled \((i,j)\). Its resulting coordinates are
\[
 I=i+j,\qquad Z_*=P^jZ,\qquad
 a_{\rm ref}=c^{-j}a,\quad b_{\rm ref}=c^j b.
 \tag{LS.6}
\]
These are invariants of LS.4's \(B\) arrow, with its full
source translation retained. The inverse is the actual
\(B^j\) arrow:
\(i=I-j, Z=P^{-j}Z_*,a=c^j a_{\rm ref},b=c^{-j}b_{\rm ref}\).
Hence this is a map of the specified quotient atlas with an
explicit inverse, rather than a change of the source period.

On the fixed surface \(p=1\), the remaining source charts are
\[
 x_I=Z_*/P^I,\qquad y_I=P^{I+1}/Z_*,\qquad
 x_Iy_I=P,
 \tag{LS.7}
\]
with the literal adjacent overlap
\((x_I,y_I)\mapsto(1/y_I,x_Iy_I^2)\), and with
\(h:I\mapsto I+3,\ Z_*\mapsto P^3Z_*\).
These parent charts and their inverses are exactly the three-node
chain presentation of the minimal \(I_3\) source family with
Tate period \(Q=P^3\). Its central fibre consists of the three
cycle components indexed by \(I\bmod3\). Both its generic
elliptic fibres and its finite outer boundary are retained.
There is one such parent for each of the four preserved labels
\(l\); neither period in LS.4 changes \(l\). The executed
558-cone atlas carries an additional, specified refinement of
these parents, described below. Thus LS.7 is an actual
blowdown target for the executed fixed surface.

In each of the three source quadrants, every label \(l\)
has exactly four executed charts. The saved parent matrices
give the source maps, in free tangent coordinates \(r,t\),
\[
 (x,y)=(rt,r^2t),\quad(rt^2,rt),\quad(rt^2,t),
 \quad(t,rt^2).
 \tag{LS.7a}
\]
Their ordered source ray pairs are respectively
\((1,2),(1,1)\), \((1,1),(2,1)\),
\((1,0),(2,1)\), and \((0,1),(1,2)\).
The complete quadrant fan is
\[
 (1,0),\ (2,1),\ (1,1),\ (1,2),\ (0,1).
 \tag{LS.7b}
\]
It is obtained by the three actual ordinary subdivisions
adding first \((1,1)\), then \((2,1)\), then \((1,2)\).
Each new ray is the sum of the two rays of its stated
regular parent cone. The corresponding two-chart maps
are \((r,t)\mapsto(r,rt)\) and
\((r,t)\mapsto(rt,t)\), with their actual reciprocal
overlap. These maps factor LS.7a and are proper blowups
supported at the node and its two specified infinitely
near points. The original source-chart period maps carry
the three quadrants cyclically. Consequently each of the
four executed lower fixed surfaces is the ninefold
blowup of its LS.7 minimal source parent, at three
points over each of its three nodes.

All 48 lower-chart parent matrices retain exactly the
two original normal coordinates \(a,b\), up to their
saved order permutation. There is no tangent monomial
in either normal row. The full source and unit maps of
LS.4 pull back along LS.7a. The proper blowdown is the
identity on the retained outer source boundary.

The normal coefficient frames in LS.6 are globally defined on
each of these finite-domain surfaces. The adjacent source arrow
fixes them. The \(B\) arrow fixes them identically. The \(h\)
arrow multiplies them by \(p^{-2},p^2\), whose restrictions to
the fixed surface are both one. To verify the normal derivative,
use \(p=1+ab\): its first derivatives in the two normal directions
vanish at \(a=b=0\). Thus the full derivative of LS.4 has the
stated normal diagonal with no tangent-to-normal correction.
It gives the equivariant holomorphic bundle isomorphism
\[
 N_F=\mathcal O_{(+1)}\oplus\mathcal O_{(-1)},
 \quad (a,b)\longmapsto(c^{-j}a,c^jb),
 \tag{LS.8}
\]
on the parent finite domain, and its literal pullback on
every one of the executed charts LS.7a. The physical
characters and the inverse coefficient map are part of
this formula.

## LS.3. The actual side-annulus map and its determinant

Put \(k=4j+l\). Solving LS.2--3 gives
\[
 a=\frac{W_C}{P^{3(j+1)}v^k},\qquad
 b=\frac{P^{3(j+1)}v^{k+1}}{W_C}.
 \tag{LS.9}
\]
On the fixed outer source annulus the full boundary map to the
ordinary scalar chain is E104.2:
\[
\begin{split}
 U_k=V_C/s^k
 &=P^{3(j+1)-k}u_s^kZ^{-1}a,\\
 V_k=s^{k+1}/V_C
 &=ZP^{k+1-3(j+1)}u_s^{-k-1}b,
 \qquad V_C=s\Delta V_{\rm T}.
\end{split}
\tag{LS.10}
\]
Every coefficient and its reciprocal is defined on that actual
annulus. Substituting the exact LS.6 quotient map gives
\[
\begin{split}
 U_k&=P^{3-l}u_s^l Z_*^{-1}
       (\lambda _0qK)^j a_{\rm ref},\\
 V_k&=Z_*P^{l-2}u_s^{-l-1}
       (\lambda _0qK)^{-j}b_{\rm ref}.
\end{split}
\tag{LS.11}
\]
Here \(cu_s^4=\lambda _0qK\) is the literal equality LS.1,
not a replacement of the suspension coefficient. The inverse
map divides by the complete displayed coefficients. Their
product is
\[
 \det(\text{normal coefficient map})=P/u_s,
 \qquad U_kV_k=(P/u_s)ab=s.
 \tag{LS.12}
\]
The \(j=0\) representative gives the two coefficients
\(P^{3-l}u_s^l/Z_*\) and
\(Z_*P^{l-2}u_s^{-l-1}\). Before that representative is
chosen, the factors \((\lambda _0qK)^{\pm j}\) remain in
the full atlas map. Applying \(h\) to LS.10 gives precisely
\((U_k,V_k)\mapsto(R^{-3}U_k,R^3V_k)\); applying \(B\)
gives the full opposite factors \(\lambda _0qK\) at the
target labels \(k+4\). These are the actual side-chain
periods and physical line maps.

For use with the individual source components, insert
\(Z_*=P^I x_I\). The two boundary factors in the
\(j=0\) representative become
\[
 P^{3-l-I}u_s^l x_I^{-1},\qquad
 P^{l-2+I}u_s^{-l-1}x_I.
 \tag{LS.13}
\]
Their sum of \(P\)-orders is one. The full quasi-period
under \(I\mapsto I+3\) is \((P^{-3},P^3)\).
These formulas describe the actual annular coefficients;
their domains and the Cartier generator LS.5 remain
part of any continuation across the interior divisor.

The original point-line frame is carried by the full
coefficient arrow E106.1,
\[
 V_{\rm pt}=H V_C,\qquad H=P^{-6}U_6^{-1}Z^3.
 \tag{LS.13a}
\]
It and its inverse are defined on the actual outer
annulus, and the point/O module map LS.5 is retained
at its interior continuation. Composing this arrow
with LS.11 gives
\[
 U_k^{\rm pt}
 =P^{-3-l}u_s^lU_6^{-1}Z_*^2
   (\lambda_0qK P^{-3})^j a_{\rm ref}.
 \tag{LS.13b}
\]
The negative coefficient is
\(P^{l+4}u_s^{-l-1}U_6 Z_*^{-2}
(\lambda_0qK P^{-3})^{-j}b_{\rm ref}\).
Their product coefficient remains \(P/u_s\).
Indeed the actual source multiplier of \(V_C\) is
\(R^{-3}\), so \(Q^3R^{-3}=P^6\) intertwines
it with the point-line source multiplier. Likewise
the source translation \(Z\mapsto P^{-1}Z\) in
\(B\) gives exactly the factor \(P^{-3}\) in
the point-frame suspension. Thus LS.13a carries
both entire period arrows, including their inverses.
The quadratic-cap comparison is consequently
\(F_{\rm pt}\circ H\), with inverse
\(H^{-1}\circ F_{\rm pt}^{-1}\); the physical
\(q^2/h^2\) closing scalars commute with \(H\).
This retains the actual reference line through the
boundary calculation.

## LS.4. The retained marked volume and reference obligation

The original marked volume from E96.10 is
\[
 \mathcal V_{\rm orig}
 =(2J_{ts}/a_{\rm T})P\,
 dx\wedge dy\wedge dv\wedge dU_j/U_j.
 \tag{LS.14}
\]
From \(v=ab\) and \(U_j=P^3(ab)^l a\), wedge multiplication
gives the exact identity
\[
 dx\wedge dy\wedge dv\wedge dU_j/U_j
 =-dx\wedge dy\wedge da\wedge db.
 \tag{LS.15}
\]
Thus the full coefficient in the lower chart is
\(-(2J_{ts}/a_{\rm T})P\). The change to LS.6 does
not alter this four-form: its extra term is a multiple
of \(dv\wedge d\log c(P,v)\), which vanishes after
wedging with \(dx\wedge dy\), since \(P=xy\).
The original \(P\) determinant divisor and the full unit
therefore remain in these invariant normal frames.

The source blowdowns LS.7a also give a definite relative
tangent comparison with their minimal parents. For one
ordinary blowup the two displayed Jacobians give
\(K_{\widetilde F}=f^*K_F+E\), with \(E^2=-1\)
and \(f^*K_F\cdot E=0\). Replacing the point by its
actual exceptional projective line raises the Euler
number by one. Thus the relative change of
\(p_1=c_1^2-2c_2\), with the identity boundary map,
is \(-1-2=-3\). Applying the nine specified blowups
gives
\[
 \Delta\!\int p_1(TF)=-27
 \tag{LS.16}
\]
for each lower surface. This is a relative tangent
calculation for the actual blowdown, with all centres
inside the finite domain. Its original-volume
Jacobian factors are also explicit: in the four
source maps LS.7a the determinant is respectively
\(-r^2t, -rt^2, t^2,-t^2\), in the displayed
coordinate orders. These factors remain in LS.14.

The integral exceptional intersection calculation is
also explicit. At each source node the three strict
exceptional rays in order \((2,1),(1,1),(1,2)\)
have intersection matrix
\[
 I_E=\begin{pmatrix}-1&1&0\\1&-3&1\\0&1&-1\end{pmatrix}.
 \tag{LS.17}
\]
The primitive total-transform basis has columns
\((1,1,1),(1,0,0),(0,0,1)\). Its integral matrix
\(T\) has determinant \(-1\) and
\(T^tI_ET=-I_3\). The relative canonical divisor,
read from the same Jacobians, has strict-basis
coefficient vector \((2,1,2)\) and square \(-3\).
The three exceptional replacements raise the Euler
number by three. Hence the relative tangent
Pontryagin change is \(-3-2\cdot3=-9\) at
each node, agreeing with LS.16 for all three nodes.
This is an integral basis comparison, with every
exceptional component and its multiplicity retained.

The complete boundary cochain LS.11, the point-line
module map LS.5 and this determinant arrow are the input
to the collision/reference doubling. LS.8 is a native
bundle isomorphism on a surface with its finite boundary;
it does not calculate the relative Chern squares in the
boundary frame LS.11. No characteristic number of the
four doubles or total source return is assigned here.

The executable record is
`code/part3/e6_order_three_lower_surfaces.py` with its
JSON and stdout. It checks the index quotient and inverse,
all four labels and full boundary characters, both
period squares, the determinant and parameter equations,
the free integral exceptional basis and canonical
divisor, and the exact marked-volume wedge. It retains
all 48 executed parent matrices and their source/normal
rows as input records. Their independent chart audit
is `code/part3/e6_lower_surface_blowups_peer.*`, with
412 checks, so the identical chart tests are not
repeated. The underlying
four-orbit identification is read from the executed
558-cone atlas and its saved physical fixed-face output.
