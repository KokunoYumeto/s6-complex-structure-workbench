# An actual scalar comparison beyond the vertical-edge fan line

Working proof after checkpoint16, 17 November 2026. This note uses the
physical reference convention of K68–69. It retains the full scalar
closing and finite-cap maps of K62/K64, and never uses the withdrawn
rank-one initial variation of K29. The current target is the explicit
OS45 source and the fan with basis ((2,-1),(-1,1)); no universal fan
classification is claimed.

## NV.1. The actual family, parameter and two products

Fix the constructed OS45 surface
\[
 y^2=x^3-3f(t)x+2g(t),\quad
 f=(t^2+1)^2+t,\quad
 g=(t^2+1)^3+\tfrac32t(t^2+1)+\tfrac38.
\]
Its marked section is \(G=(t^2+1,\sqrt3/2)\), its line is
\(M=\mathcal O(8G-O)\), and the suspension translates by \(-G\).
Retain any one of the four marked simple roots \(\tau\) of
\(48t^4+8t^3+96t^2+72t+57\) as the scalar-zero fibre and retain
K10's actual ordinary multiplicity-one cap at \(t=0\). The parameter
is the primitive \(\lambda=r\), so its scalar winding is one. The
root/cap/source construction, properness and sphere topology are the
ones already proved in K10/K22; the maps below change its cusp fan
and preserve that actual exterior. The forward ordinary closing is
\(t/(t-\tau)\), namely \(q^{-1}\) times the bounded unit \(t\) at
\(q=t-\tau=0\). No cap is added or removed.

We keep symbols \(J,H,\chi\) temporarily to record exactly the
source of each contribution. For this concrete family they are
\(J=1,H=8,\chi=1\). On the degree-two parameter cover the full cusp
periods are
\[
 h:(Z,V)\mapsto(\kappa qZ,\alpha V),\qquad
 B:(Z,V)\mapsto(gZ,q\eta V),\qquad \eta=\lambda\beta.
\tag{NV.1}
\]
All four bounded units other than \(\lambda\) are the original ones.
The forward closing has the form \(q^e u(q)\), with its specified
nonzero unit; in the concrete family \(e=-1,u=t\). Reindex by
\(B^{-e}\), retaining its source factor, and use K64's actual cut
map \(C_\tau=(AZ,DV)\). It satisfies \(C_{\rm end}E=1\) on
whole collars, including all derivatives. On the double cover we
use exactly \(C^{(2)}_{j+\tau}=C_\tau E^{-j}\), \(j=0,1\).
The exterior and cap squares are therefore literal pullbacks of the
single family.

The initial two vertex charts are \((a,b,c)\), \((u,v,w)\), with
\(q=abc=uvw\). The native fixed star \(C_0\) has charts
\[
 (z,n_0,n_1)=(b,a,c),\qquad
 (z',n'_0,n'_1)=(\kappa w,\alpha v,(\kappa\alpha)^{-1}u).
\tag{NV.2}
\]
Substitution of the full period row gives
\(z'=z^{-1}\), \(n'_i=zn_i\), with every unit retained.
Its Cox quaternion is
\[
 q_H=(1+jz)(n_0+j\overline{n_1}).
\tag{NV.3}
\]
This is literally K30.11 in the same order: \(n_0\) has physical
weight \(-1\), \(n_1\) weight \(+1\), and physical delta is right
multiplication by \(e^{-i\phi}\). Thus the native C0 normal and base
markings are the ones used for K69's retained relative pair.

There is one endpoint comparison to retain here. K30 writes its
extending origin as a reference-to-current map. Its inverse gives
closed coordinates. With linear parameter cutoff and \(g=U^{-1}\),
\(\eta=\lambda W^{-1}\), K64's current-to-reference cut map differs
from that inverse by the global physical-circle factor
\[
 \exp\bigl(\pi i eJ(\theta^2+\theta)\bigr)
\tag{NV.4}
\]
on a single \(J\)-winding interval. Both endpoints are one. This is
an actual based circle action on the whole family, commuting with all
periods and finite caps, so carrying the connection by it preserves
the relative return. Replacing the linear cutoff by the protected
cutoff changes the bounded source and line factors through their
explicit interval logarithms with zero endpoint values. Multiplying
these logarithms by a real homotopy parameter gives an actual based
homotopy of the star products. The q-dependent normal jets are carried
by the normal-rescaling flow of K64. No parameter winding is discarded.

## NV.2. The fixed-star native-to-ordinary map

For the doubled loop, put \(t=J\) and use exactly K64's common
ordinary plumbing product
\[
 T_i(Q)=H_JQH_{l_i-J},\qquad(l_0,l_1,l_2)=(2J,0,2J).
\tag{NV.5}
\]
At the fixed star, the normal pair in (NV.2) is \((a,c)\), so its
literal map to the common product is
\[
 q_H\longmapsto (U(z)H_JU(z)^{-1})q_HH_J,
 \qquad U(z)=\frac{1+jz}{\sqrt{1+|z|^2}}.
\tag{NV.6}
\]
This is obtained by substituting \(Q=n_0+j\overline{n_1}\) into
(NV.3), with no interchange or inversion of the normal pair.
At the opposite vertex the factors are precisely the full unit
factors \(\eta/\alpha\) and \(\kappa\alpha\) from K64. The
normal homotopy therefore matches both protected collars of (NV.2).

The left factor in (NV.6) has degree \(2J\) on the oriented native
Hopf base times parameter, by the same direct quaternion integral as
SV.11; the right factor depends only on radius and parameter and has
zero third degree. The inverse-cylinder extension has endpoint
\(L^{-2J}\). It follows that the ordinary relative pair is the
native pair minus \((2J,0)\). This is the identical arrow to the
already proved nonfixed C1/C2 comparison, now verified in the actual
fixed-star coordinates (NV.2)–(NV.3).

The retained K69 native pair on the single family is
\((6\chi,3H-6\chi)\). Its literal double pullback is
\((12\chi,6H-12\chi)\), hence the common-product C0 pair is
\[
 (m_0^{\rm ord},n_0^{\rm ord})
       =(12\chi-2J,6H-12\chi).
\tag{NV.7}
\]
The actual product-frame derivative map K31.7, retained independently
of its false initial-data claim, therefore gives
\[
 V_{00}=2J-6H,\qquad \delta_0=2J+6H-24\chi.
\tag{NV.8}
\]
The physical double return is \(2(H/2-\chi)\), by the actual
parameter pullback and K68, not by a division of a sphere class.

## NV.3. Complete initial ordinary data from the actual prisms

The full-unit trace maps of K64 have degrees
\[
 I=(-2J,2J,-2J),\qquad W=(2J,0,0).
\tag{NV.9}
\]
Use the literal generic endpoint paths and rank-one endpoint caps of
K51/K52. Their vertex maps are (SV.5), commute with the physical
circle and are parameter independent after transport. Thus the same
oriented chains give
\[
 \operatorname{Var}(D_1)=2J(m_0+m_1),\qquad
 \operatorname{Var}(D_2)=2J(-m_0+m_2),\qquad
 \delta_1=-2J,\quad\delta_2=2J.
\tag{NV.10}
\]
Here \(\Delta x_1=D_1\), \(\Delta x_2=-D_2\), and the boundary
identity is \(\operatorname{Var}(\Delta x)=[K\partial x]\).
Together with symmetry and (NV.8), the actual data are
\[
 V_0=\begin{pmatrix}
 2J-6H&2J&-2J\\2J&2J&0\\-2J&0&2J
 \end{pmatrix},\qquad
 \delta_0^{\rm vec}=
 \begin{pmatrix}2J+6H-24\chi\\-2J\\2J\end{pmatrix}.
\tag{NV.11}
\]
These replace the withdrawn scalar rank-one seed. Their derivation
uses the actual separate native products and the ordinary double
product; it makes no simultaneous equivariance assertion.

## NV.4. Two literal Cox changes and target products

The first flip is C0, with exact new basis and characters
\[
 P_1=\begin{pmatrix}1&-1\\0&1\end{pmatrix},\qquad
 (Z',V')=(ZV,V).
\tag{NV.12}
\]
The native other-ruling map is
\((z,n_0,n_1)\mapsto(n_0/n_1,zn_1,n_1)\); the rank-one matrix
\(\bigl(\begin{smallmatrix}n_0&n_1\\zn_0&zn_1\end{smallmatrix}\bigr)\)
gives both charts. It preserves \(q=zn_0n_1\) exactly. The whole
unit matrix transforms by the actual monomial map
\(A'_{rs}=\prod A_{hj}^{(P_1^{-1})_{rh}(P_1)_{js}}\).
The cut map C transforms by the same characters and has the full Cox
lift. Thus the outside source, finite cap and closing remain the
ones of NV.1.

Construct the new ordinary product from these full transformed units,
using the same based logarithms and H maps. On this fan its doubled
winding matrix, tangent/normal weights and first normal exponents are
\[
 B_1=\begin{pmatrix}0&2J\\0&2J\end{pmatrix},\quad
 w=(1,1,-2),\quad d=(-3,-3,0),\quad l=(2J,-2J,2J).
\tag{NV.13}
\]
The trace maps, including their full unit homotopies, have
\[
 I=(-2J,10J,-2J),\qquad W=(4J,-8J,-2J).
\tag{NV.14}
\]
The selected new star is C2. The unrestricted four-weight Cox
common-link and the constant complex reset are precisely K54/CF.5.
On each side the native-to-ordinary map adds the same pure-left
\(-2J\) to the native return. It cancels in the selected-coordinate
comparison. Consequently, if a,b are the old selected ordinary
\(V_{00},\delta_0\), the new selected entries are
\(V'_{22}=a\), \(\delta'_2=2a-b\), and the physical central
increment is the old native right integer. This is a direct comparison
of the two constructed products on the selected star; no common
exterior matrix-reset premise is used.

All target weights are nonzero. Its actual prism equations and
symmetry then determine the target uniquely from those two selected
entries: with \(r_i=1/w_i\),
\[
 V'=\operatorname{diag}(I_i/w_i)+c\,rr^t,\quad
 \delta'_i=(W_i+e_*)/w_i,\quad
 c=w_2^2a-w_2I_2,\quad e_*=w_2(2a-b)-W_2.
\tag{NV.15}
\]
This is linear algebra on actual integral cycle identities. Substitution
gives
\[
 V'=\begin{pmatrix}
 2J-24H&4J-24H&-2J+12H\\
 4J-24H&14J-24H&-2J+12H\\
 -2J+12H&-2J+12H&2J-6H
 \end{pmatrix},\quad
 \delta'=\begin{pmatrix}
 2J+36H-48\chi\\-10J+36H-48\chi\\2J-18H+24\chi
 \end{pmatrix}.
\tag{NV.16}
\]
The new C1 ordinary and native right integer is therefore
\[
 n_1^{(2)}=30H-24\chi-12J.
\tag{NV.17}
\]
Its native product is the explicit periodic holomorphic star product
with all transformed units. Its double product is chosen as the
literal pullback of that single product, exactly as in K64. The
ordinary-product comparison just made uses those boundary products.
Thus (NV.17) is the right coordinate of the actual relative square;
injectivity of multiplication by two in the free relative group gives
\[
 n_1=15H-12\chi-6J.
\tag{NV.18}
\]
No division occurs in \(\Theta_7\).

The second actual flip has basis
\[
 P_1Q_1=\begin{pmatrix}2&-1\\-1&1\end{pmatrix},\qquad
 Q_1=\begin{pmatrix}1&0\\-1&1\end{pmatrix}.
\tag{NV.19}
\]
Its characters are \((Z'',V'')=(Z',Z'V')\). The same full unit
formula and the two Cox charts give the actual family. The constant
normal interchange is carried by CF.6a's explicit U(2) path. The
unrestricted common-link map, followed by its fixed complex-normal
reset, adds (NV.18) to the physical central class.

For the specified OS45 data, the actual initial physical value is3.
The first fixed-edge flip adds18 and gives21. Formula(NV.18) is102,
so the second specified flip gives
\[
               3+18+102=123\equiv11\pmod{28}.
\tag{NV.20}
\]
This is a concrete nonvertical fan comparison. Promotion awaits the
independent audit of NV.2's C0 product/closing match and NV.4's full
selected target-product comparison. The formulas above are retained
as a complete working derivation, not yet an active theorem.

## NV.5. The complete closing check and exact finite consistency record

For the concrete OS45 cap the ordinary forward map has line multiplier
\(q^{-1}t\). Its reindexing by the actual \(B\) gives
\[
 E:(Z,V)\longmapsto(gZ,t\eta V),\qquad
 C_{\rm end}:(Z,V)\longmapsto(g^{-1}Z,(t\eta)^{-1}V).
\tag{NV.21}
\]
Their composition is the identity on the whole cusp annulus. These
are full nonzero germs in q, so equality retains every derivative.
On the two successive laps the actual products are \(C_\tau\) and
\(C_\tau E^{-1}\). Their adjoining collar values are both
\(E^{-1}\), and their final value is \(E^{-2}\). The finite-cap
map is the original order-one map carried by the same ordinary
closing, hence this change of coordinates preserves its full overlap
square. On either mutated fan the character changes of NV.4 send
(NV.21) to their literal monomial images. All maps fix q, so these
images still give exactly the original source, line and cap family
on the common exterior.

For every vertex multiplier \((A,D)\), the three full rows satisfy
\[
 F_i((AD)^{-1}a,Ab,Dc)
      =(AD\,u_i,D^{-1}v_i,A^{-1}w_i),
\tag{NV.22}
\]
where \((u_i,v_i,w_i)\) are the respective period rows. Thus the
bounded source factor, line factor and higher q jets are carried
through every selected star. The Cox lift is precisely the one
obtained by this substitution in the rank-one matrix of NV.4.
It extends to both rulings before taking the free period quotient.
This verifies the actual closing/product square, rather than only
the final winding matrix.

The executed certificate is `code/part3/scalar_nonvertical.py`, with
its JSON and captured output. It passes 66 exact identities. These
include the OS45 equation, section, simple-cusp polynomial and regular
cap; the full unit rows and quaternion overlap; the based physical
delta comparison; all initial and target trace equations; the actual
native-square integers; and both other-ruling charts.

A separate finite consistency calculation in that same file uses the
concrete seed only. Through words of length four it obtains 21 basis
states and 16 literal periodic triangulations. All ten repeated-basis
or repeated-fan checks agree. For a repeated fan the program does
not identify it from a numerical invariant: it compares its actual
two triangle orbits, writes each new triangle as an old triangle plus
an integral vector, and exports the vertex permutation. The vector
\((r,s)\) is the actual period \(h^rB^s\), with its full units; the
induced map on the quotient is therefore the identity of the same
family. For example the reverse of the second flop has basis
\(\bigl(\begin{smallmatrix}2&1\\-1&0\end{smallmatrix}\bigr)\).
Its two triangles are the earlier \(P_1\) triangles translated by
\((1,-1)\) and \((2,-1)\), with exported permutations, and its
physical class returns to 21.

The two encountered targets whose zero-weight curve is not the
selected flopped curve are left unevaluated. No fixed-star left
integer is inferred there from a central class. The finite search
is an exact consistency certificate for the written maps, not a
claim to have computed every fan or every word.
