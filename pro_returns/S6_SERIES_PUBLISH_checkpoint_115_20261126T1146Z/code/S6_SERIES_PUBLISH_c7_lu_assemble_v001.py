#!/usr/bin/env python3
"""Assemble one LU theorem/proof from the frozen derivation and settled auxiliaries."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import re

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/'agents/continuation7_iii_corrected_initial_receiving'
FRESH = ROOT/'agents/continuation7_iii_corrected_initial/S6_SERIES_PUBLISH_III_02LU_fresh_derivation.md'
assert sha256(FRESH.read_bytes()).hexdigest() == 'c9439d8819da0dbf1ba285687e37a5ddce780e2afafeafb1a9f61297f71b29e1'
target = LANE/'S6_SERIES_PUBLISH_III_02LU_receiving.tex'
assert not target.exists()
receiver = r'''\begin{theorem}[all height-integral initial pairs with corrected original additive caps]\hypertarget{tag-02LU}{}\label{maps:src:D.2.52}
\textup{\scriptsize[02LU]}

Fix any of the twenty-one marked Mordell--Weil rank-one
profiles, write $\langle G,G\rangle=1/d_0$, and take
$P=aG,Q=bG$ with $a,b>0$ and $d_0\mid ab$.
Choose nonnegative integral whole-fibre weights of total
$ab/d_0$, supported at multiplicative or additional regular
fibres, and use the corrected line of \ref{maps:src:D.2.50}.
There is a finite exact integral algorithm for the fundamental
group and every integral homology group with the following fillings:
\begin{enumerate}[label=(\roman*)]
\item marked rank-one or triangular Mumford caps, with their
prescribed periodic fan, at multiplicative or regular sites;
\item free finite-good additive logarithmic caps, with their
affine powers and all five integral Thom columns;
\item original additive caps whose corrected multidegree has
$h=1$ in \eqref{maps:eq:D.IC2}, and unchanged zero-degree
original additive caps with their extending frames;
\item original multiplicative caps with the uncorrected line,
degree vector and relative frame of \ref{maps:src:D.2.46};
\item any finite number of regular logarithms at additional
weight-zero sites, and any ordinary integral clutch.
\end{enumerate}
Positive weights use the prescribed Mumford filling. Odd-star
fibres use their original caps. A supplied integral component
divisor must satisfy \eqref{maps:eq:D.VC3}; its component
permutation, degree vector and extending frames enter the
algorithm. For an original additive cap the test is the
literal orbit condition $h=1$, or the unchanged zero-degree
case with its specified relative marking.

The canonical corrections of \ref{maps:src:D.2.50} supply these
fillings for every positive pair of integral height. The only
newly non-narrow additive positions have component pair
$(2,2)$ at an odd star, with degree vector
\eqref{maps:eq:D.IC8}; newly non-narrow multiplicative positions
may use the marked Mumford filling. Thus the initial pair
need not satisfy the narrowness-OR condition of
\ref{maps:src:D.2.46}. Across all twenty-one profiles there
are exactly $45$ additional residue pairs modulo $d_0$.

The algorithm applies to every finite list and all permitted
section multiples, weights, logarithmic orders and affine
numerators. Its original-cap choices specify the line and
relative frame: a whole-fibre change carries the meridian
shear proved below. A corrected original multiplicative cap
with a different supplied relative marking, or an additive
cap with $h>1$, requires its own complete local boundary map
before it is an input to this algorithm.
\end{theorem}

\begin{proof}
\smallskip\noindent\emph{Corrected lines and marked periods.}
Let $C$ be the component intersection matrix, $\mu$ its
multiplicity vector, and $S$ the pullback permutation induced
by $Q$. A component divisor $d$ changes the degree vector to
\[
 c=e_p-e_0+Cd.
\]
The integral equation and its equivalent invariance condition are
\[
 C(I-S)d=-(I-S)(e_p-e_0),\qquad (I-S)c=0.
\]
Here $CS=SC$ in the component marking. If two solutions differ
by $z$, then $(I-S)z=k\mu$, since $\ker C=\mathbb Z\mu$.
Taking the scalar product with $\mu$ gives $k=0$.
Consequently the ambiguity is precisely the integral lattice
of orbit-constant vectors. Its inverse coordinate map reads
one coefficient on each orbit.

The existence and global degree computation in
\ref{maps:src:D.2.50} apply to these literal divisors.
The relevant line maps can be specified explicitly. Set
$M_0=\mathcal O(P-O)$ and $M_D=M_0\otimes\mathcal O(D)$.
On the complement of the singular fibres the canonical
section $\sigma_D$ is nonzero, and
\[
 I_{D,p}(v)=v\otimes\sigma_D(p),\qquad
 I_{D,p}^{-1}(v\otimes\sigma_D(p))=v.
\]
For the difference lines $J_0,J_D$ the corresponding map is
\[
 I_{J,p}(j)=j\otimes\frac{\sigma_D(p)}{\sigma_D(p+Q)}.
\]
Its inverse uses the reciprocal ratio. A section of $J_D$
defines the forward line arrow $A_{D,p}:M_{D,p+Q}\to M_{D,p}$.
Thus it covers $-Q$, and its conjugate is exactly
\[
 I_{D,p}^{-1}A_{D,p}I_{D,p+Q}
   =j_D(p)\frac{\sigma_D(p+Q)}{\sigma_D(p)}.
\]
The inverse is the inverse arrow composed with the inverse
tensor maps in the reverse order.

The group-law function for
$P-O-(P-Q)+(-Q)$, the vertical component sections, and a
degree-zero base function give the isomorphism of $J_D$
with the base line of degree $ab/d_0$. Multiplication by
these functions and division by them are the forward and
inverse maps. In an extending base frame a zero of weight
$w$ has coefficient $q^w u(q)$, where $u$ is the nonzero
holomorphic unit of that frame. On a compact smooth elliptic
fibre the ratio with the transported Poincar\'e frame is a
nonzero holomorphic function and hence constant. It is a
base unit, which remains in the arrow and its reciprocal
inverse. This identifies the punctured families with their
specified zero orders and units.

Let $B$ be the elliptic monodromy, $g$ the cocycle of $G$,
and choose $z_G$ with $(B-I)z_G=g$. At an additive site
$z_G=(B-I)^{-1}g$. At a multiplicative site write
\[
 B-I=\nu u u^{\mathsf t}J,\quad g=\kappa u,
 \quad u^{\mathsf t}Jv=1,\quad z_G=(\kappa/\nu)v,
 \qquad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
The period $v$ is transverse to the vanishing period $u$.
In the coordinates $(x,\delta,\gamma)$ the Poincar\'e
translation and line frame give
\[
 L=\begin{pmatrix}I_2&0&-bz_G\\
             az_G^{\mathsf t}J&1&0\\0&0&1\end{pmatrix},
 \qquad
 L^{-1}=\begin{pmatrix}I_2&0&bz_G\\
             -az_G^{\mathsf t}J&1&0\\0&0&1\end{pmatrix}.
\]
Their cross term is $abz_G^{\mathsf t}Jz_G=0$.
They map the transported period lattices to one another.
On the denominator cover, the translation is integral;
the exponential line factor and its reciprocal give the
frame maps. The section logarithm reads the inverse modulo
the transported lattice. These maps therefore retain the
Poincar\'e units as well as their valuations.

Since $B^{\mathsf t}JB=J$,
\[
 r_G=-g^{\mathsf t}JB=z_G^{\mathsf t}J(B-I).
\]
Multiplying $L\operatorname{diag}(B,1,1)L^{-1}$ and adding
the zero-order shear gives, with $r=ar_G$ and $z=bz_G$,
\[
 T=\begin{pmatrix}B&0&bg\\ r&1&rz+w\\0&0&1\end{pmatrix},
 \qquad
 T^{-1}=\begin{pmatrix}
 B^{-1}&0&-B^{-1}bg\\
 -rB^{-1}&1&rB^{-1}bg-rz-w\\0&0&1
 \end{pmatrix}.
\]
Both composites are the identity. The elementary shear fixes
$\delta$ and the $\gamma$ covector and hence commutes with
the displayed comparison.

The denominator of $z_G$ is the order of the generator's
component class, by the component/logarithm map of
\ref{maps:src:D.2.20}. The nontrivial orders are
\[
\begin{array}{c|c|c}
 \mathrm{OS}&\text{component orders}&d_0\\ \hline
 43&2&2\\45&8&8\\46&4&4\\47&7,2&14\\
 49&2,3&6\\50&4,3&12\\55&5,4&20\\56&5,3,2&30
\end{array}
\]
and each order divides $d_0$. At a multiplicative component
$\kappa$ is a unit modulo $\nu$, so its denominator is
exactly $\nu$. It follows that $abz_G$ is integral and hence
$rz=ab r_Gz_G$ is integral. All entries of $T$ and $T^{-1}$
are therefore integral for every permitted $a,b$.
In the ordered defining periods, the height calculation gives
\[
 \prod_i T_i=I+\left(\sum_iw_i-\frac{ab}{d_0}\right)
                         \delta\gamma^*=I.
\]
This is the ordered peripheral product; its inverse is the
reversed product of the displayed inverses.

An invariant orbit divisor $E$ has canonical pullback
trivialization $\sigma_E/T_Q^*\sigma_E$. Tensoring by
$\sigma_E$ on the punctured family and dividing by it are
inverse maps. In the arrow the ratio
$\sigma_E(p+Q)/\sigma_E(p)$ cancels through that same
difference-line trivialization. The period blocks and the
specified base weights thus agree under this map, with no
extension across the zeros or poles of $\sigma_E$ being used.

\smallskip\noindent\emph{The original additive cap as a mapping cone.}
Let $K$ be the reduced additive central curve and let $c_i$
be the corrected component degrees. Its normalization is
rational. The cusp of type II is topologically a sphere,
and the common points in III and IV give wedges of two and
three spheres. The other additive diagrams are trees.
Contract connecting arcs to a vertex. The inverse sends
each oriented sphere cell to its normalized component
with those arcs, and the arc contractions give both homotopies.

In a Hermitian norm the forward line arrow has a positive
roof after multiplication by a sufficiently small nonzero
scalar on the compact collar. Integrate a positive density
of total one, with matching endpoint value, along that roof.
This is an increasing coordinate; its increasing inverse
recovers the original norm and roof. Normalize the arrow
to the unit circle in each fibre. These maps identify the
cap with the mapping torus of its unit-circle-bundle map,
retaining the arrow's norm factor and units.

Retract the original Kodaira neighbourhood to $K$ and lift
the paths through a fixed line connection. Reverse parallel
transport gives the inverse along each path. If $r_u$ runs
from the identity to inclusion followed by the retraction
$r$, then $H_u=rQr_u$ joins $rQ$ to $Q_Kr$. The induced
mapping-torus map traverses $[r(x),2t]$ in the first half
of the roof and $H_{2-2t}(x)$ at roof zero in the second
half. Its endpoint is $r(Qx)$. Inclusion, reverse transport
and this cylinder homotopy give the inverse up to homotopy.

The component automorphisms can be removed with their lifts.
With two fixed nodes the map is $z\mapsto\alpha z$ and the
path is $z\mapsto\exp(t\log\alpha)z$. With one fixed node
at infinity it is $z\mapsto\alpha z+\beta$, with path
$z\mapsto\exp(t\log\alpha)z+t\beta$. With three fixed
nodes it is the identity. Subtracting the translation and
dividing by the nonzero scalar gives the path inverses.
Identify permuted components by their marked normalizations,
and solve the line gauges from the root of the rational
tree; reciprocal gauges are their inverses. The resulting
permutation $\sigma$ is that of the forward arrow, hence
the inverse of the positive $Q$ component permutation.

The circle bundle over the component wedge has one cell in
degrees zero and one and one cell per component in degrees
two and three. Its degree-two differential is $c^{\mathsf t}$,
the winding of the component clutch. Positive mapping-torus
prisms give the integral complex
\[
\begin{split}
 C_0&=\mathbb Z,& C_1&=\mathbb Z\delta\oplus\mathbb Z\gamma,\\
 C_2&=\mathbb Z^v\oplus\mathbb Zt,&
 C_3&=\mathbb Z^v\oplus\mathbb Z^v,&C_4&=\mathbb Z^v,\\
 d_2(x,t)&=(c^{\mathsf t}x,0),&
 d_3(u,y)&=((\sigma-I)y,c^{\mathsf t}y),&
 d_4(z)&=((I-\sigma)z,0).
\end{split}
\]
Here $t=\delta\wedge\gamma$. Reading the component cells
and oriented prisms is the inverse cellular coordinate map.
The identities $c^{\mathsf t}\sigma=c^{\mathsf t}$ give
$d_2d_3=d_3d_4=0$. Any line-frame change contributes its
integer prism coordinate to this complex.

Write the orbits as $O_j$, their lengths as $\ell_j$, and
their common degrees as $c_j$. Suppose
$h=\gcd(\ell_jc_j)=1$. Choose $a_j$ with
$\sum_j a_j\ell_jc_j=1$ and set $\eta=a_j$ on $O_j$.
Then
\[
 (\sigma-I)\eta=0,\qquad c^{\mathsf t}\eta=1,
 \qquad d_3(0,\eta)=(0,1).
\]
This is an integral bounding chain for $t$.
Let $R:\mathbb Z^v\to\mathbb Z^\rho$ read orbit sums.
The map and section for degree two are
\[
 H_2(U)\longrightarrow\ker(c_1,\ldots,c_\rho),\quad
 [(x,t)]\longmapsto Rx,
\]
with section placing each coordinate on a chosen orbit
representative and setting $t=0$. If $z$ has zero orbit
sums, enumerate an orbit by $\sigma e_i=e_{i+1}$ and put
$y_i=-\sum_{r=0}^i z_r$, with $y_{\ell-1}=0$.
Then $(\sigma-I)y=z$. For a cycle $(x,t)$ subtract the
section of $Rx$. The difference is exactly
\[
 d_3\bigl(0,y+(t-c^{\mathsf t}y)\eta\bigr).
\]
Thus both quotient composites have displayed integral
bounding chains.

The fundamental group has presentation
\[
 \langle\delta,\gamma\mid[\delta,\gamma]=1,
                         \ \delta^{c_i}=1\ (1\leq i\leq v)\rangle.
\]
Since $\gcd(c_i)=1$, a Bezout combination kills $\delta$.
The remaining primitive generator is the positive roof loop
$\gamma$. The elliptic loops map to the simply connected
rational configuration and die after $\delta$ is killed.
The map from the fibre therefore reads its $\gamma$
coordinate; the roof loop supplies its inverse section.

In degree three, read the orbit sums of $u$ and the
orbit-constant coefficients of $y$. This gives
\[
 H_3(U)\simeq\mathbb Z^\rho\oplus
             \ker(\ell_jc_j:\mathbb Z^\rho\to\mathbb Z).
\]
Insert representatives in $u$ and constant orbit coefficients
in $y$ for the inverse, using the same partial sums for
the zero-sum differences. In degree four the orbit-constant
vectors have inverse reading of one coordinate per orbit.
Consequently
\[
 H_0(U)=\mathbb Z,\quad H_1(U)=\mathbb Z,\quad
 H_2(U)=\mathbb Z^{\rho-1},\quad
 H_3(U)=\mathbb Z^{2\rho-1},\quad H_4(U)=\mathbb Z^\rho.
\]
All are free and $\chi(U)=0$.

\smallskip\noindent\emph{The integral fibre map and both normal maps.}
Put $z=bz_G$ and let $q$ be its least denominator, equivalently
the order of the component class of $Q$. The component-orbit
vector of the elliptic fibre is
$R\mu=(\ell_j\mu_j)_j$. Its gcd is $q$.
Indeed a multiplicity-one orbit has length $q$, and every
other $\ell_j\mu_j$ is divisible by $q$: in III and IV
this is the two- or three-cycle; in IV$^*$ the three arms
meet a multiplicity-three centre; in III$^*$ the reflection
of the chain $1,2,3,4,3,2,1$ fixes only even multiplicities,
including its multiplicity-two branch. At an odd $D$ star
an order-four component generator cycles the four outer
leaves and pairs the inner multiplicity-two vertices; its
square pairs the leaves and fixes the inner vertices.
The identity action gives $q=1$.

The class $W$ with orbit coordinates $R\mu/q$ is primitive,
and lies in $\ker(c_j)$ since $c^{\mathsf t}\mu=0$.
The orbit section above constructs it as an integral
two-cycle. The actual elliptic fibre represents $qW$.
Pass to the $q$-fold long-circle cover. The return $Q^q$
has integral logarithm $qz$ and is narrow. Translating by
that logarithm along the roof, with negative translation
as inverse, removes the return on $K$. The line lift is
the preceding node/frame path; endpoint changes are scalar.
On elliptic coordinates the map is $x\mapsto x+zx_\gamma$,
with inverse subtraction. The mixed classes on the cover
are $qz_2$ times the elliptic area and $-qz_1$ times that
area. Scalar crosses vanish by the Bezout cone chains.
Transfer followed by projection multiplies by $q$.
The target is free, so cancellation of that integer proves
the full integral fibre map
\[
 \bigwedge\nolimits^2\Lambda\longrightarrow H_2(U),\qquad
 y\longmapsto q(y_{12}+z_2y_{14}-z_1y_{24})W,
 \quad \Lambda=\mathbb Z\langle e_1,e_2,\delta,\gamma\rangle.
\]
Its row is integral and primitive because
$\gcd(q,qz_1,qz_2)=1$. A Bezout vector in these three
entries is a section; the kernel is exactly the integral
kernel of this row.

The fixed lattice at this zero-weight additive site is
\[
 F=\mathbb Z\delta\oplus\mathbb Z\ell,
 \qquad \ell=(-qz_1,-qz_2,0,q).
\]
The $\delta$ normal sweep bounds the scalar bundle over
the normal section disc in its extending frame. For the
$\ell$ sweep use the same $q$-fold cover. After the integral
logarithm comparison it is the long circle times a normal
section disc, together with the line-frame prisms. Its
component two-cell projection is zero. Transfer therefore
gives $q$ times its orbit vector equal to zero; the orbit
target is free, so that vector is zero on the original cap.
Cellularize this literal torus as $(x,t)$, retaining every
frame jump. Then $Rx=0$, and the partial-sum vector $y$
gives its complete bounding chain
\[
 (0,y+(t-c^{\mathsf t}y)\eta).
\]
This supplies both normal maps, including the scalar-long
correction. In the Wang boundary sequence, subtract these
two bounding normal tori and apply the displayed fibre
row. Its kernel together with these two normal columns
is the full boundary kernel, with the stated section and
bounding chains as inverse maps.

\smallskip\noindent\emph{The literal odd-star correction and the count.}
For the affine $D_r$ diagrams, $r=5,7$, let leaves $0,1$
meet vertex $2$, let the inner chain end at $r-2$, and
let the far leaves be $r-1,r$. The zero component is $0$.
At $(\overline P,\overline Q)=(2,2)$, $P$ meets leaf $1$
and $Q$ swaps $(0,1)$ and $(r-1,r)$ while fixing the chain.
The intersection matrix has diagonal $-2$ and entry one
on these edges. For the divisor $d_{\rm can}=-e_0$,
\[
 e_p-e_0=e_1-e_0,\qquad Cd_{\rm can}=2e_0-e_2,
 \qquad c=e_0+e_1-e_2.
\]
Define new coordinate $i$ to be old coordinate $p_i$, where
\[
\begin{array}{c|c|c}
 r&p&p^{-1}\\ \hline
 5&(0,1,4,5,2,3)&(0,1,4,5,2,3)\\
 7&(0,1,6,7,2,3,4,5)&(0,1,4,5,6,7,2,3).
\end{array}
\]
The maps are $x'_i=x_{p_i}$ and $x_j=x'_{p^{-1}_j}$.
Conjugating $C$ and the permutation by these inverse maps
gives $\mu=(1,1,1,1,2,\ldots,2)$, $\sigma=(01)(23)$ and
\[
 c=(1,1,0,0,-1,0,\ldots,0).
\]
This is \eqref{maps:eq:D.IC8}. Its orbit degree products
include $2$ and $-1$, so $h=1$; $\eta=-e_4$ is the
explicit invariant vector with $c^{\mathsf t}\eta=1$.
The alternative divisor $e_1$ differs from $d_{\rm can}$
by $e_0+e_1$. Multiplication by the canonical section of
$\mathcal O(-C_0-C_1)$ and its reciprocal give the
punctured comparison, conjugating the arrow with its
section ratio. Each original cap is handled by its own
cone and frame. In the displayed order-two action the
forward-arrow permutation equals its inverse; for other
orders the partial sums above follow the forward arrow.

The component orders in the table are pairwise coprime
and their product is $d_0$. The CRT coordinate map is
$a\mapsto(a\bmod h_i)_i$. If $M_i=d_0/h_i$ and
$M_it_i\equiv1\pmod{h_i}$, its inverse is
$\sum_i M_it_i a_i\bmod d_0$. Both composites are the
identity on every residue coordinate. Applying it to
$a$ and $b$ makes $d_0\mid ab$ equivalent to
$h_i\mid a_i b_i$. There are
\[
 H(h)=\sum_{a\bmod h}\gcd(h,a)
 \quad\hbox{such local pairs, and}\quad N(h)=2h-1
\]
pairs with $a_i=0$ or $b_i=0$. The number of additional
pairs per profile is $\prod_iH(h_i)-\prod_iN(h_i)$.
For a prime $h$ these counts agree. At $h=4$ the only
additional pair is $(2,2)$; at $h=8$ the pairs are
$(2,4),(4,2),(4,4),(4,6),(6,4)$.
The CRT inverses give the complete nonzero contributions:
\[
\begin{array}{c|l|r}
 \text{profiles}&\text{additional pairs in each profile}&\text{total}\\ \hline
 45/\mathrm{default},\mathrm{II}
   &(2,4),(4,2),(4,4),(4,6),(6,4)&10\\
 46/\mathrm{default},\mathrm{II}&(2,2)&2\\
 50/\mathrm{default},\mathrm{II},\mathrm{IV}
   &(2,6),(6,2),(6,6),(6,10),(10,6)&15\\
 55/\mathrm{default},\mathrm{II}
   &(2,10),(6,10),(10,2),(10,6),(10,10),&18\\
   &\quad(10,14),(10,18),(14,10),(18,10)&
\end{array}
\]
The other profiles contribute zero, so the sum is $45$.
At an additive prime-order position height integrality
forces one section to be narrow. The only remaining
additive case is the displayed odd-star pair $(2,2)$.
It has the required literal correction with $h=1$.
This proves the full initial-pair scope; a multiplicative
newly non-narrow position takes its prescribed Mumford cap.

\smallskip\noindent\emph{Global relation maps and the fundamental group.}
Apply the integral ordered bar model of
\ref{maps:src:D.2.41} to the tuple $T_i$ just constructed.
It keeps the six fibre bivectors, their return columns,
and the integral graph kernel with its Smith coordinate
inverse. The binomial quadratic cochains and the suffixes
of the ordered last-boundary word give every normal column.
These maps apply to all integral determinant-one matrices
with the displayed product, so they apply to this tuple.

At the new original additive caps insert the full kernel,
both literal normals and their bounding chains proved above.
At every other permitted cap use the full marked maps of
\ref{maps:src:D.2.46} and \ref{maps:src:D.2.43}:
the prescribed-fan period and logarithm inverse, all component
normal discs, the nonsaturated fibre kernel and boundary
torsion, or the finite sheet/norm maps and all five Thom
columns. These local maps are functions of the displayed
periods, fan, extending frames and affine power; each input
is retained here. At an uncorrected multiplicative site,
invariance of $e_p-e_0$ forces $p=0$ or $q=0$: for $p\ne0$
the coefficient $-1$ occurs uniquely at zero, which must
be fixed by the component translation. Thus this cap has
exactly the unchanged geometry and frame covered by
\ref{maps:src:D.2.46}.

The fundamental-group presentation retains the four
commuting fibre generators, each peripheral generator,
conjugation by $T_i$, the ordered peripheral product,
every affine power relation, and every nonlogarithmic cap
quotient. At an $h=1$ additive cap it kills
$e_1,e_2,\delta$ and the origin meridian and retains
the positive $\gamma$ loop. The forward maps are these
paths; the inverses read the roof, finite sheet or short/long
period coordinates and then the cut-base graph coordinates.
They agree on every boundary generator and their two
composites fix every generator. Van Kampen therefore gives
the asserted finite presentation, including its nonabelian
relations. Abelianization computes $H_1(X)$.

For completeness its vertical normal closure is a terminating
integer procedure with explicit subgroup maps. Let
$V=\mathbb Z\langle e_1,e_2,\delta\rangle$, let
$M_i=T_i|_V\in\mathrm{SL}(3,\mathbb Z)$, and let $L_0$
be the integer span of the killed vertical vectors. Set
\[
 L_{r+1}=L_r+\sum_iM_iL_r.
\]
The union is a subgroup of $\mathbb Z^3$, hence finitely
generated. Each of its finitely many generators occurs
at some stage; their maximal stage contains the union.
This proves termination. Hermite column operations retain
the exact subgroup and the integer word for each basis
vector, together with the inverse coordinate reading.
If the characteristic polynomial of $M_i$ is
$x^3-t_ix^2+s_ix-1$, Cayley--Hamilton gives
\[
 M_i^{-1}=M_i^2-t_iM_i+s_iI.
\]
Positive stability thus gives inverse stability, so the
stable lattice contains all positive and negative conjugates.

Before the cap and power relators, the exterior group is
the semidirect product of the abelian fibre with the
cut-base free group. Send $M_wv$ to
$t_wx_vt_w^{-1}$ for each initially killed vector $v$.
Products of conjugates add their fibre exponent vectors.
Reading that exponent is the inverse map, so the stable
lattice is precisely this normal subgroup. Taking its
quotient first or adding its generators as relators gives
inverse homomorphisms on every fibre and peripheral
generator. All remaining power and product relations are
then retained. This establishes the unsaturated closure
procedure without assuming that the final group is abelian
or that the intermediate vertical quotient injects into it.

\smallskip\noindent\emph{The integral splitting and all homology groups.}
Let $\mathcal B$ be the complete fibre-and-graph relation
matrix. Keep the Smith transformations
$U\mathcal B V=\Delta$. The quotient generators are
$U^{-1}e_j$, and the relations satisfy
\[
 \mathcal B V e_j=\Delta_{jj}U^{-1}e_j.
\]
The inverse map reads $U$ times a represented cycle,
modulo the corresponding diagonal factor. This retains
every torsion factor of a nonsaturated local kernel.

At least one weight is positive, since $ab/d_0>0$.
Its prescribed Mumford cap is nonlogarithmic. Attach the
finite and regular logarithmic caps first and call the
result $E$. Their root-disc boundaries are
$m_i\tau_i-v_i$. A relation among them in peripheral
coordinates is a multiple of the single sum relation.
Its coefficient at the remaining nonlogarithmic site is
zero, so that multiple is zero; each coefficient of a
root boundary is then zero. Reading a peripheral
coordinate and dividing by its $m_i$ gives the inverse
on the image. Thus this first stage is exactly the
quotient by the five Thom columns at each logarithmic cap.

For each remaining cap $U_i$, take its component or orbit
normal discs in the extending Cartier frames. Their
boundaries follow the stems, period logarithms and integer
frame jumps already used in the bar model. They define
\[
 \Gamma:\mathbb Z^{\sum_i h_i}\longrightarrow H_1(E),
 \qquad h_i=b_4(U_i).
\]
At a new $h=1$ cap, $h_i=\rho_i$, and its free $H_3$
shows directly that $H^4(U_i)$ is the free component-orbit
target. The other allowed caps have the component-disc
targets of \ref{maps:src:D.2.46} and
\ref{maps:src:D.2.43}. Exponentiating the period coordinate
and reversing the chart transitions invert each boundary
construction, with its meridian coefficient.

The pair sequence is therefore
\[
 0\longrightarrow\operatorname{coker}\mathcal B
  \longrightarrow H_2(X)
  \longrightarrow\ker\Gamma\longrightarrow0.
\]
Here is an integral section and its inverse. Choose an
injective basis matrix $P$ for the relation image in a
free presentation of $H_1(E)$ and retain its preimages
in the original relation columns. Lift $\Gamma$ to a
matrix $M$ and solve $Mz=Pz'$ by integer Smith operations.
Projection to $z$ has inverse recovering the unique $z'$
because $P$ is injective. For a resulting kernel basis
vector, join the component discs to the retained relation
chains, exterior cylinders and ordered torus polygons.
This is a closed integral two-cycle. Reading the disc
coordinates and subtracting these cycles is the inverse
splitting. In particular the full integral kernel,
including its index in its rational span, is retained.

The local degree-one quotient maps are onto, so
$\operatorname{coker}\Gamma=H_1(X)$. The relative free
rank is consequently
\[
 \sum_i b_4(U_i)-b_1(E)+b_1(X).
                         \tag{D.CI1}\hypertarget{tag-01YN}{}\label{maps:eq:D.CI1}
\]
Write $\operatorname{coker}\mathcal B=\mathbb Z^g\oplus T$
and $H_1(X)=\mathbb Z^r\oplus A_1$, with $T,A_1$ finite.
If $q_{\rm rel}$ is \eqref{maps:eq:D.CI1}, then
\[
 b_2=g+q_{\rm rel},\qquad
 \chi(X)=2\sum_{\text{positive multiplicative }i}\nu_iw_i,
 \qquad b_3=2+2b_2-2r-\chi(X).
\]
The new additive caps have Euler number zero by the cone
calculation. The other cap indices give the displayed
Euler sum, and the exterior and boundaries are mapping
tori with zero Euler number. The complex orientation and
the determinant-one ordinary clutch orient the closed
six-manifold. Integral duality and universal coefficients
give
\[
\begin{array}{c|c}
 j&H_j(X;\mathbb Z)\\ \hline
 0,6&\mathbb Z\\
 1&\mathbb Z^r\oplus A_1\\
 2&\mathbb Z^{b_2}\oplus T\\
 3&\mathbb Z^{b_3}\oplus T\\
 4&\mathbb Z^{b_2}\oplus A_1\\
 5&\mathbb Z^r.
\end{array}
\]
For a torsion factor the resolution
$\mathbb Z\xrightarrow{d}\mathbb Z$, its dual unit
cochain and oriented cap product give the torsion map;
reading the residue modulo $d$ is its inverse. This also
computes the Euler-zero cases.

\smallskip\noindent\emph{Relative frames for supplied corrections.}
The algorithm forms $C(I-S)d$ and compares it integrally
with $-(I-S)(e_p-e_0)$. It reads the literal degree $c$,
its orbits and $h=\gcd(\ell_jc_j)$; the preceding maps
apply to $h=1$. At an unchanged zero-degree original
cap it uses its given extending frame and the original
maps of \ref{maps:src:D.2.46}.

To specify the whole-fibre change, write $F=\operatorname{div}(q)$
and $D=kF$. The punctured tensor map is
$I_D(v)=v\sigma_D$, with reciprocal inverse. The extending
isomorphism is $E_D(v)=vq^{-k}\sigma_D$, since
$q^{-k}\sigma_D$ is its nonzero extending frame. Translation
preserves $q$, and the line arrows conjugate by these exact
multipliers. Hence
\[
 I_D^{-1}E_D(v)=q^{-k}v,\qquad E_D^{-1}I_D(v)=q^kv.
\]
On the boundary the first sends
$\tau\mapsto\tau-k\delta$ and the inverse sends
$\tau\mapsto\tau+k\delta$; both fix $\delta$.
At $h=1$ the resulting scalar-long addition bounds by
the displayed $\eta$ chain. The zero-degree cap retains
this meridian shear as part of its relative marking.
Thus the specified original-cap inputs, all supplied
integral corrections in their proved local scope, and
all finite affine parameters enter one finite exact
presentation and homology construction.
\end{proof}
'''
old = ''.join((LANE/f'S6_SERIES_PUBLISH_III_02LU_released_{x}.tex').read_text()
              for x in ('statement','proof','following_auxiliary'))
for command in ('label','hypertarget','tag'):
    pattern = r'\\'+command+r'\{([^{}]+)\}'
    assert sorted(re.findall(pattern, old)) == sorted(re.findall(pattern, receiver)), command
assert receiver.count(r'\begin{proof}') == receiver.count(r'\end{proof}') == 1
assert r'\StatementRecord' not in receiver and r'\path{' not in receiver
print('START', datetime.now(timezone.utc).isoformat())
target.write_text(receiver)
print('RECEIVER', target.relative_to(ROOT), 'LINES', len(receiver.splitlines()))
print('SHA256', sha256(target.read_bytes()).hexdigest())
print('IDENTITIES', {k: re.findall(r'\\'+k+r'\{([^{}]+)\}', receiver) for k in ('label','hypertarget','tag')})
print('END', datetime.now(timezone.utc).isoformat())
