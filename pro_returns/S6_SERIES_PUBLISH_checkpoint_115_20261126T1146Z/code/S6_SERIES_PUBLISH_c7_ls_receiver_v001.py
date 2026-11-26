"""Assemble the complete LS receiving theorem and its single proof.

Only the individually released LS spans and frozen fresh evidence are read.
No canonical source, global record, or frozen fresh file is modified.
"""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import re

W=Path(__file__).resolve().parents[1]
LANE=W/'agents/continuation7_iii_vertical_correction_receiving'
fresh=W/'agents/continuation7_iii_vertical_correction/S6_SERIES_PUBLISH_III_02LS_fresh_derivation.md'
assert sha256(fresh.read_bytes()).hexdigest()=='ee6cbed56c156a8f590c0f7926121a9a3baf5ba4fdbccf9302d56a7df126ef7d'
released=(LANE/'S6_SERIES_PUBLISH_III_02LS_released_statement.tex').read_text()
statement=released[released.index(r'\begin{theorem}'):].strip()
statement=statement.replace(r'\label{maps:src:D.2.50}',r'\label{maps:src:D.2.50}\textnormal{\small tag02LS.}',1)
proof=r'''\begin{proof}
\begin{enumerate}
\item \emph{Actual component maps and the integral equation.}
Let $C_0,\ldots,C_{v-1}$ be the components of a reducible fibre,
with $C_0$ meeting $O$, let $\mu$ be its primitive positive
multiplicity column, and put $C=(C_iC_j)$. In particular $\mu_0=1$.
If the actual translation $T_Q$ sends component $i$ to $\sigma(i)$,
write $S$ for pullback on columns: $(Sz)_i=z_{\sigma(i)}$.
Then $CS=SC$, $S\mu=\mu$, and $S^{-1}=S^t$.
The degree column of the section line and its correction are
\[
 m_P=e_p-e_0,\qquad m=m_P+Cd,\qquad \mu^t m=0.
                                                        \tag{D.VC2}\hypertarget{tag-026G}{}\label{maps:eq:D.VC2}
\]
Thus $J_D$ has zero degree on every component precisely when
\[
       (S-I)Cd=-(S-I)(e_p-e_0).
                                                        \tag{D.VC3}\hypertarget{tag-026H}{}\label{maps:eq:D.VC3}
\]
The pushforward convention has matrix $S^{-1}$; its equation is
obtained by the unimodular left multiplication $-S^{-1}$, whose
inverse is $-S$. This proves the exact equivalence of the two
permutation conventions. All lattices in this proof are integral.

If $d,d'$ solve this equation, then
$C(S-I)(d-d')=0$. The integral kernel of $C$ is $\mathbb Z\mu$,
so $(S-I)(d-d')=k\mu$. Pairing with $\mu$ gives
$0=k\mu^t\mu$ and hence $k=0$. Conversely an invariant column
can be added to a solution. The precise ambiguity is therefore
\[
           d+\ker(S-I)\subset\mathbb Z^v.
                                                        \tag{D.VC4}\hypertarget{tag-026I}{}\label{maps:eq:D.VC4}
\]
Its basis consists of the literal sums of the component basis
vectors in each orbit. Reading the common coefficient on a chosen
orbit representative is the inverse coordinate map. Whole fibres
are included, as are the other invariant orbit sums.

\item \emph{A rational function and the exact base line.}
On the generic elliptic curve the divisor
$P-O-(P-Q)+(-Q)$ is principal. For distinct nondegenerate points,
take the line through $P,-Q$, divided by the vertical line through
$P-Q$. If $P=Q$, use $x-x(P)$; if $P=-Q$, use the tangent line
at $P$, divided by the vertical line at $2P$. If $P=0$ or $Q=0$,
the divisor is zero and the function is $1$. These are the actual
group-law functions, with reciprocal inverse maps.

Multiplying by the canonical rational sections of $\mathcal O(D)$
and $\mathcal O(-T_Q^*D)$ gives a rational section of $J_D$ whose
remaining divisor is vertical. If \eqref{maps:eq:D.VC3} holds,
the coefficient column of that divisor at each fibre belongs to
$\ker C=\mathbb Z\mu$. Since $\mu_0=1$, its whole-fibre
coefficient is an integer. Therefore $J_D=f^*\mathcal O(t)$ for
an integer $t$. The isomorphism is multiplication by the displayed
function, the canonical vertical sections, and a degree-zero base
rational function identifying the whole-fibre divisor with $t[\infty]$.
Multiplication by their reciprocals is its inverse. Restriction to
$O$ makes pullback from the base injective. Conversely a base
pullback has zero component degrees, proving necessity of the local
equations at the level of actual line bundles.

To compute $t$, let $f_q$ be the rational column determined by
$Cf_q=e_q-e_0$ and $f_q(0)=0$. The norm of $f_q$ under $S$ has
$C$-image zero, because the orbit sum of $e_q-e_0$ telescopes.
It is thus a rational multiple of $\mu$. Since $m$ is invariant
and $m^t\mu=0$, we obtain $m^tf_q=0$, and hence
\[
             d_q-d_0=-f_q(p)=\operatorname{contr}_v(P,Q).
\]
The mixed height formula on the rational elliptic surface is
\[
 1+P\mathbin{\cdot}O+Q\mathbin{\cdot}O-P\mathbin{\cdot}Q
   =\langle P,Q\rangle+\sum_v\operatorname{contr}_v(P,Q).
\]
Here the local terms are the negative inverse-Cartan pairings;
see \cite[Sections 7, 8 and 11.8, especially pp.32--34 and51--52]{manSS10}.
Intersecting the rational section of $J_D$ with $O$ adds
$\sum_v(d_0-d_q)$ to the left side. The terms cancel literally,
so $t=\langle P,Q\rangle=ab/d_0$. This proves the asserted
identity \eqref{maps:eq:D.VC1}, its necessity, and independence
from every invariant-orbit ambiguity. The argument includes signed
$a,b$ and the zero cases; positivity is not used here.

\item \emph{Integral solutions for every component pair.}
At an $I_n$ fibre use the positive-valuation Tate labels
$\mathbb Z/n$. The actual translation sends $i$ to $i+q$.
The cycle matrix has diagonal $-2$ and one $+1$ for each incident
edge. At $n=2$ both parallel edges are retained, giving off-diagonal
entry $2$. Its image is exactly
\[
 \left\{h\in\mathbb Z^n:\ \sum_i h_i=0,
                  \ \sum_i i h_i=0\pmod n\right\}.
\]
Indeed, for such $h$, put
\[
 r_0=-\frac1n\sum_{i=0}^{n-1}(n-1-i)h_i,
 \quad r_i=r_0+\sum_{j<i}h_j,
 \quad d_0=0,\quad d_i=\sum_{k=1}^{i}r_k.
\]
The moment condition makes $r_0$ integral; augmentation zero
makes the differences cyclic. Then
$(Cd)_i=r_{i+1}-r_i=h_i$, including the two-edge case.
Subtracting the common coefficient $d_0$ is the inverse choice
modulo the whole-fibre constant. At $n=1$ the degree-zero lattice
is zero.

Put $g=\gcd(n,q)$ and $\ell=n/g$. An invariant multidegree is
constant on the $g$ residue classes modulo $g$. Its augmentation
condition cancels the common part of the orbit moments, giving
\[
 \sum_i i m_i=\ell\sum_{j=0}^{g-1}j m_j\pmod n.
\]
For $m=e_p-e_0+Cd$ this moment is $p$, so $\ell\mid p$,
equivalently $n\mid pq$. If $p=0$ or $q=0$, take $d=0$.
Otherwise $g>1$, and the invariant column
\[
 m_i=(p/\ell)
       \bigl({\bf1}_{i=1\bmod g}-{\bf1}_{i=0\bmod g}\bigr)
\]
has the required moment. Apply the displayed inverse to
$h=m-e_p+e_0$. This constructs an integral solution for every
admissible signed residue pair.

For the other types, the component orders and generator
self-pairings from the deleted-zero-component matrix are
\[
\begin{array}{c|rrrrrrr}
 \text{type}&II&III&IV&III^*&IV^*&I_1^*&I_3^*\\\hline
 n&1&2&3&2&3&4&4\\
 \operatorname{contr}(1,1)&0&1/2&2/3&3/2&4/3&5/4&7/4.
\end{array}
\]
The preceding identity $d_q-d_0=\operatorname{contr}(p,q)$
shows that this pairing must be integral. Each numerator is a
unit modulo its component order; therefore the exact condition is
\[
                  \operatorname{ord}(\Phi_v)\mid pq.
                                                        \tag{D.VC6}\hypertarget{tag-026K}{}\label{maps:eq:D.VC6}
\]
For orders2 and3 this makes one section narrow, and $d=0$ works.
For either odd star the only further pair is $(2,2)$. Label the
near leaves $0,1$, their adjacent inner vertex $2$, the inner
chain $2,\ldots,r-2$, and the far leaves $r-1,r$, where $r=5$ or7.
The multiplicities are1 on the four leaves and2 on the chain.
In $D_r=\{x\in\mathbb Z^r:\sum x_i\text{ even}\}$ the near
weight is $e_1$, while a far weight is $(e_1+\cdots+e_r)/2$.
Its square is $r/4$ and twice it equals the near class modulo
$D_r$. This identifies the simple-component labels. Actual
translation by class2 swaps the two near leaves, swaps the two
far leaves and fixes the chain. Taking $d=e_1$ gives
$m=-e_0-e_1+e_2$, invariant under that literal permutation.
Its inverse is the same permutation. This proves sufficiency
without replacing the marked components by an abstract graph.

\item \emph{The twenty-one profiles and all residues.}
The recorded component coordinates of $G$ are units in every
nontrivial cyclic component group. Their nontrivial orders are
pairwise coprime and have the following products:
\[
\begin{array}{c|c|c}
 \mathrm{OS}&\text{nontrivial orders}&d_0\\\hline
 43&(2)&2\\45&(8)&8\\46&(4)&4\\47&(7,2)&14\\
 49&(2,3)&6\\50&(4,3)&12\\55&(5,4)&20\\56&(5,3,2)&30.
\end{array}
\]
Every recorded collision profile retains these marked component
orders. The exact defining matrices and cocycles determine the
orders too: in a Smith decomposition $U(B-I)V=D$, the class of
$g$ has order
\[
 \operatorname{lcm}_{j\leq\operatorname{rank}(B-I)}
       \frac{|D_{jj}|}{\gcd(|D_{jj}|,(Ug)_j)}.
\]
The zero Smith rows of $Ug$ vanish. The recorded82 pairs $(B,g)$
give exactly the stated component orders; the integer preimage
of that order times $g$ is retained. Thus \eqref{maps:eq:D.VC6}
at all fibres is equivalent to $d_0\mid ab$. The constructed
local divisors sum to an integral global $D$.

All signed integers are included by reduction to the component
residues. There are227 distinct local pairs and5696 pairs over
the21 full residue squares. Their exhaustive integral checks
retain the actual affine matrices, all Smith maps and inverses,
all chosen solutions, and the invariant-orbit basis with inverse.
The additional positive height-one initial pairs are
\[
\begin{array}{c|c|c}
 \mathrm{OS}&\text{profiles}&(a,b)\\\hline
45&\mathrm{default},II&(2,4),(4,2)\\
46&\mathrm{default},II&(2,2)\\
50&\mathrm{default},II,IV&(2,6),(6,2)\\
55&\mathrm{default},II&(2,10),(10,2).
\end{array}
\]
This table has sixteen initial rows. The sixteen filled spaces
below have a different explicit parameterization: two pairs,
four zero positions, and two clutch signs on OS45/default.

For example, on $I_4$ with $(p,q)=(2,2)$, $D=-C_0$ changes
$(-1,0,1,0)$ to $(1,-1,1,-1)$. The inverse ambiguity coordinates
are the coefficients of $C_0+C_2$ and $C_1+C_3$.
For general corrections the original-cap multidegrees can be
nonprimitive or permuted. The present argument makes no
identification of those completed caps.

\item \emph{The punctured tensor and period maps.}
Off the singular fibres the canonical section $\sigma_D$ is
nonzero. The actual tensor map and inverse are
\[
 I_D:(p,v)\longmapsto(p,v\sigma_D(p)),\qquad
 I_D^{-1}:(p,v')\longmapsto(p,v'/\sigma_D(p)).
\]
On the arrow line it multiplies by
$\sigma_D(p)/\sigma_D(p+Q)$. An arrow is a map from the line
at $p+Q$ to that at $p$ and thus covers $-Q$. In actual local
frames the conjugated arrow multiplier is
$j_D(p)\sigma_D(p+Q)/\sigma_D(p)$.
The group-law function above identifies it with the uncorrected
Poincare arrow times its actual base section. A ratio constant
on each compact elliptic fibre is a base unit; retain it as
$q^{w_i}u_i(q)$, with $u_i$ nowhere zero.

For a local elliptic matrix $B$, choose $z_G$ with $(B-I)z_G=g$
and put $J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$.
The actual logarithmic comparison and inverse on the transported
period lattice are
\[
 L=\begin{pmatrix}I_2&0&-bz_G\\a z_G^tJ&1&0\\0&0&1\end{pmatrix},
 \qquad
 L^{-1}=\begin{pmatrix}I_2&0&bz_G\\-a z_G^tJ&1&0\\0&0&1\end{pmatrix}.
\]
The cross term is zero because $z_G^tJz_G=0$.
These matrices describe the actual exponential and logarithmic
line-frame maps, with reciprocal multipliers. When denominators
occur they are integral maps on the transported lattices, or on
the corresponding denominator cover; they are not asserted to be
automorphisms of a fixed untransported lattice.

The line row satisfies
$r_G=-g^tJB=z_G^tJ(B-I)$. In the literal marking
$(e_1,e_2,\delta,\gamma)$ the resulting monodromy and inverse are
\[
 T_i=\begin{pmatrix}B_i&0&bg_i\\r_i&1&c_i\\0&0&1\end{pmatrix},
 \quad r_i=-a g_i^tJB_i,\quad c_i=r_i(bz_{G,i})+w_i,
\]
\[
 T_i^{-1}=\begin{pmatrix}
 B_i^{-1}&0&-B_i^{-1}bg_i\\
 -r_iB_i^{-1}&1&r_iB_i^{-1}bg_i-c_i\\0&0&1
 \end{pmatrix}.
\]
The denominator of $z_G$ is the actual component order $h_i$.
It divides $d_0$, so $d_0\mid ab$ makes $c_i$ integral.
At an $I_\nu$ site, write $g=\kappa u$,
$B-I=\nu u(u^tJ)$, and choose $u^tJv=1$; then
$z_G=(\kappa/\nu)v$. This is the transverse period, with
denominator $\nu$ when $\kappa$ is a unit. Changing $z_G$ by
a fixed elliptic vector leaves $r_i z_G$ unchanged.

The ordered raw products, including every defining profile, give
\[
 \prod_i T_i=I+\left(\sum_i w_i-ab/d_0\right)E_{\delta\gamma}.
\]
This is also the exact base-degree cocycle of the constructed
line map. The coefficient matrix $E_{\delta\gamma}$ is fixed
by all blocks and has square zero, so distributing the prescribed
weights among singular or regular sites changes the product by
their sum. The total in the theorem makes this product the identity.

For the original iterated description, choose $h$ such that $hQ$
is narrow everywhere. It fixes every component divisor. Evaluation
of adjacent tensor factors gives the literal identity
\[
 \bigotimes_{j=0}^{h-1}T_Q^{j*}J_D
 =M_D\otimes T_{hQ}^*M_D^{-1}
 =M_0\otimes T_{hQ}^*M_0^{-1}.
                                                        \tag{D.VC5}\hypertarget{tag-026J}{}\label{maps:eq:D.VC5}
\]
All canonical sections of $D$ telescope, with reciprocal inverse
maps. On the logarithmic cover the deck generator is exactly
$\gamma_h=h\gamma$, and its lattice inclusion is
\[
 S_h=\operatorname{diag}(1,1,1,h),\qquad
                 T_iS_h=S_hT_{i,h}.
                                                        \tag{D.VC8}\hypertarget{tag-026M}{}\label{maps:eq:D.VC8}
\]
The inverse on the image divides the last coordinate by $h$.
Here $bg_i$, $bz_G$ and $w_i$ are multiplied by $h$, while $r_i$
is fixed. This proves the actual marked period comparison.
The multiplier units and any constant scalar are retained in the
contracting roof. Its normalized positive density has a strictly
increasing integral, whose inverse gives the chosen circle
parameter. No covering of a completed cap is inferred.

\item \emph{The OS45 data and its two actual corrections.}
The raw defining data, with the raw component convention, are
\[
\begin{gathered}
 (I_8,I_1,I_1,I_1,I_1),\quad d_0=8,
 \quad \overline G_{I_8}=3\pmod8,\\
 g_i=(3,0),(0,0),(2,-1),(1,-2),(0,0),\\
 (B_0,\ldots,B_4)=
 \begin{pmatrix}1&8\\0&1\end{pmatrix},
 \begin{pmatrix}1&1\\0&1\end{pmatrix},
 \begin{pmatrix}3&4\\-1&-1\end{pmatrix},
 \begin{pmatrix}3&1\\-4&-1\end{pmatrix},
 \begin{pmatrix}0&1\\-1&2\end{pmatrix}.
\end{gathered}
                                                        \tag{D.VC9}\hypertarget{tag-026N}{}\label{maps:eq:D.VC9}
\]
Retain the following literal raw-component coefficient choices:
\[
\begin{array}{c|c|c}
 (a,b)&(D_{C_0},\ldots,D_{C_7})&m\\\hline
 (2,4)&(-1,-1,-1,0,0,0,0,0)&(0,0,1,-1,0,0,1,-1)\\
 (4,2)&(-1,0,0,1,1,1,0,0)&(1,-1,1,-1,1,-1,1,-1).
\end{array}
                                                        \tag{D.VC10}\hypertarget{tag-026F}{}\label{maps:eq:D.VC10}
\]
The multidegree column $m$ is invariant under the respective
raw shifts4 and6. No correction is needed at the four irreducible
fibres. Both height pairings are1.

The positive-valuation Tate labels are obtained from the raw
ones by $j\mapsto-j\pmod8$, an involution with matrix $F$ and
$FCF=C$. It conjugates the shift by $q$ to the shift by $-q$.
Thus the physical pairs are $(p,q)=(2,4),(4,2)$.
The explicit Laplacian inverse above gives the physical choices
\[
 d^{\rm new}_{2,4}=(0,0,1,1,1,0,0,0),\qquad
 d^{\rm new}_{4,2}=(0,0,1,1,2,1,1,0).
\]
Subtracting these from the reflected original choices gives
\[
 E_{2,4}=(-1,0,-1,-1,-1,0,-1,-1),\qquad
 E_{4,2}=(-1,0,-1,0,-1,0,-1,0),
\]
invariant under shifts4 and2 respectively. The exact punctured
comparison is $v\mapsto v\sigma_E(p)$, with inverse division.
It conjugates the arrow by
$\sigma_E(p)/\sigma_E(p+Q)$, retaining all units.
Along $O$ its local expression is $q^{-1}u(q)$, with $u$ a
nowhere-zero holomorphic unit. On $q=\epsilon e^{2\pi it}$,
the angular displacement is $-t+\arg u(q)/(2\pi)$; the inverse
subtracts it. The radial multipliers are reciprocal. In particular
the peripheral origin shifts by $-\delta$, with inverse $+\delta$.

For each correction we use the punctured period map just proved
to define the cap origin and the specified affine boundary map.
Comparing corrections transports that origin and gluing by the
displayed tensor map and its inverse, including this shear.
The following filling computation applies directly to the choices
\eqref{maps:eq:D.VC10} with their specified marking. It does not
assert an identification obtained by changing $D$ while fixing an
untransported affine gluing.

\item \emph{Primitive rank-one cap maps without a coprimality shortcut.}
The multiplicative data are
\[
\begin{array}{c|c|c|c|c}
 i&\nu_i&\kappa_i&u_i&v_i\\\hline
0&8&3&(1,0)&(0,1)\\
1&1&0&(1,0)&(0,1)\\
2&1&1&(2,-1)&(1,0)\\
3&1&1&(1,-2)&(1,-1)\\
4&1&0&(1,1)&(-1,0).
\end{array}
\]
Embed $u,v$ in the first two coordinates and put
$\mathcal S=(u,\delta)$, $\mathcal L=(v,\gamma)$.
At a weight-zero site the off-diagonal block between these
two lattices is
\[
 N=\begin{pmatrix}\nu&b\kappa\\
             -a\kappa&-ab\kappa^2/\nu\end{pmatrix}.
\]
Set $d=\gcd(\nu,a\kappa)$, $n=\nu/d$,
$A=a\kappa/d$, $B=b\kappa/n$. For every site in the two
specified pairs these are integers, $\gcd(n,A)=1$ and
$\gcd(d,B)=1$. Choose $n\theta+A\sigma=1$ and $dx+By=1$,
and put
\[
 C_S=\begin{pmatrix}n&\sigma\\-A&\theta\end{pmatrix},
 \quad C_S^{-1}=\begin{pmatrix}\theta&-\sigma\\A&n\end{pmatrix},
 \quad C_L=\begin{pmatrix}x&-B\\y&d\end{pmatrix},
 \quad C_L^{-1}=\begin{pmatrix}d&B\\-y&x\end{pmatrix}.
\]
Then $N=(n,-A)^t(d,B)$ and $NC_L=C_S\operatorname{diag}(1,0)$.
The ordered integral period matrix
\[
 H=(\mathcal S C_Se_1,\mathcal L C_Le_1,
                   \mathcal S C_Se_2,\mathcal L C_Le_2)
\]
has determinant1 and $H^{-1}TH=I+E_{12}$.
At $I_8$ one may use, respectively,
\[
\begin{array}{c|c|c}
(a,b)&C_S&C_L\\\hline
(2,4)&\begin{pmatrix}4&-1\\-3&1\end{pmatrix}
     &\begin{pmatrix}-1&-3\\1&2\end{pmatrix}\\
(4,2)&\begin{pmatrix}2&1\\-3&-1\end{pmatrix}
     &\begin{pmatrix}1&-3\\-1&4\end{pmatrix}.
\end{array}
\]
This calculation uses $\gcd(a,b)=2$ exactly; a natural-row
coprimality formula has not been substituted.

These period changes are realized on the actual torus charts.
Characters transform by $C_S^{-t}$, with inverse $C_S^t$;
the long-period multipliers are the indicated integer products
with exponents $C_L$, whose inverse products have exponents
$C_L^{-1}$. Retain the actual unit multipliers in both directions.
On a one-dimensional fan the node charts are
\[
 X=z/q^j,\qquad Y=q^{j+1}/z,\qquad XY=q;
 \qquad z=Xq^j
\]
on their overlap, with the displayed reciprocal inverse.
The primitive period shift identifies consecutive components.
The resulting normalization is a degree-zero ruled surface over
the torus of the remaining long periods. If its flat multipliers
are $\lambda_1,\lambda_2$, multiplication by
$\exp(-t_1\log\lambda_1-t_2\log\lambda_2)$ on the universal
cover is the smooth trivializing gauge; the positive exponent
is its inverse. A pole-gluing translation $x\mapsto x+a_0$
is removed by $(z,x)\mapsto(z,x-f(z)a_0)$, where $f$ is0
near one pole and1 near the other; the inverse adds that term.
This describes the actual nodal ruled normalization and its
unit maps, yielding a core $(\text{nodal }\mathbb P^1)\times T^2$.

In the $H$-coordinates, write
$z=(z_{12},z_{13},z_{14},z_{23},z_{24},z_{34})$.
Its specialization maps are
\[
 f_1(x)=(x_2,x_3,x_4),\qquad
 f_2(z)=(z_{12},z_{23},z_{24},z_{34}).
\]
Their sections insert zero in the omitted coordinates, and are
transported physically by $H$ and $\Lambda^2H$.
The integral fibre kernel is
$\langle e_{13},e_{14}\rangle$, with exact Wang preimages
$e_{23},e_{24}$. Thus the core has
$\pi_1=\mathbb Z^3$, $H_2=\mathbb Z^4$, $H_3=\mathbb Z^3$,
$H_4=\mathbb Z$, and Euler characteristic0. These identifications
are induced by the displayed normalization and node maps.

\item \emph{The selected triangular cap and all boundary kernels.}
At the selected $I_1$ site, $w=1$, $\nu=1$, and
\[
 C_+=\begin{pmatrix}1&b\kappa\\-a\kappa&1-ab\kappa^2\end{pmatrix},
 \qquad C_+^{-1}=\begin{pmatrix}1-ab\kappa^2&-b\kappa\\a\kappa&1\end{pmatrix}.
\]
Set $H=(\mathcal S C_+e_1,\mathcal Le_1,
\mathcal S C_+e_2,\mathcal Le_2)$. This has determinant1,
and $H^{-1}TH=I+E_{12}+E_{34}$.
The prescribed fan lies in the actual short lattice $\mathcal S C_+$;
its characters transform by $C_+^{-t}$, with inverse $C_+^t$.
The primitive period cell has one vertex, three edges and two
triangles. Its normalization is the toric hexagonal surface,
with the three actual conductor identifications and all period
unit multipliers retained. In each triangle the product-coordinate
chart has $XYZ=q$; the lattice character maps above and their
inverse monomials identify adjacent charts and the period translates.
They construct the specified cap, including its boundary marking.

The normalization/conductor chain maps give
\[
 f_1(x)=(x_2,x_4),\qquad
 f_2(z)=(z_{12},z_{14}-z_{23},z_{24},z_{34}).
\]
Sections are $(s,t)\mapsto(0,s,0,t)$ and
$(r,s,t,u)\mapsto(r,0,s,0,t,u)$.
The kernel of $f_2$ is the primitive lattice
$\langle e_{13},e_{14}+e_{23}\rangle$, with Wang preimages
$e_{23},e_{24}-e_{23}$.
The transverse double tori and the primitive conductor differences
give the four displayed $H_2$ coordinates; the two graph cycles
of the triangulation give $H_3=\mathbb Z^2$.
The universal dual triangulation is a plane, and its toric
components have trivial fundamental group. Thus the only
fundamental-group generators are the two long period deck
translations: $\pi_1=\mathbb Z^2$.
The whole fibre generates $H_4=\mathbb Z$. Open positive-dimensional
torus orbits have Euler characteristic zero; the two triangle
vertices contribute2, so this cap has Euler characteristic2.

For both cap types the actual fixed circles extend over the
toric charts. Sweeping an extending origin disc by such a circle
gives a three-chain whose boundary is the fixed-normal torus,
with sign fixed by the positive base meridian. The kernel of
boundary $H_2$ specialization is consequently generated by the
displayed primitive fibre kernel and these fixed-normal tori.
There are no additional quotient classes: the displayed $f_2$
has an integral section, and the normalization/conductor complex
is exact in the remaining degrees. Boundary $H_1$ specializes
onto core $H_1$ with kernel the positive normal meridian; the
primitive image $(T-I)\Lambda$ is exactly the short vanishing
lattice and the origin disc fixes its affine lift. All maps have
been specified on the actual period coordinates, not only by
their rational ranks.

\item \emph{The full integral exterior and its bar inverse.}
Let $\Lambda=\mathbb Z^4$ and order $\Lambda^2\Lambda$ as
$(12,13,14,23,24,34)$. For the five singular matrices put
\[
 R=(\Lambda^2T_0-I\mid\cdots\mid\Lambda^2T_4-I),\qquad
 D=(T_0-I\mid\cdots\mid T_4-I),\qquad K=\ker D.
\]
The exact Smith factors of $D$ are $1,1,1$, so $K$ is primitive
of rank17. If $U_DDV_D$ is its tracked Smith form, columns4
through20 of $V_D$ form the chosen basis and the corresponding
rows of $V_D^{-1}$ give its inverse on $K$. The nonzero Smith
factors of $R$ are $1,1,1,1,2$. Thus the fibre coinvariant is
$\mathbb Z\oplus\mathbb Z/2$; its torsion is retained.
If $U_RRV_R$ is the Smith form, the quotient map reads the last
coordinate of $U_Rz$ and the fifth modulo2, with inverse induced
by $U_R^{-1}$ on those two coordinate vectors.

Here is the actual bar section and inverse, with the conventions
of \ref{maps:src:D.2.41}. Put
$p(x,y)=\sum_{i<j}x_i y_j e_{ij}$ and use the central group
\[
 (x,z)(y,w)=(x+y,z+w+p(x,y)),\qquad
 (x,z)^{-1}=(-x,-z+p(x,x)).
\]
Lift a signed basis word for $x$ by the ordered images of its
generators under $T$. Its central correction $f_T(x)$ is the
difference from $\Lambda^2T\sum_{i<j}x_ix_je_{ij}$.
Equivalently, with
$A_{ij}=p(Te_i,Te_j)-\Lambda^2T\,p(e_i,e_j)$,
\[
 f_T(x)=-\sum_i\binom{x_i}{2}A_{ii}
        -\sum_{i<j}x_i x_j A_{ij}.
\]
The symmetry $A_{ij}=A_{ji}$ follows from the exterior-square
identity. Signed integer powers use the group inverse just given,
so this formula applies without a positivity restriction.
The lifted map is
$(x,z)\mapsto(Tx,\Lambda^2Tz-f_T(x))$; its inverse sends
$(y,w)$ to
$(T^{-1}y,\Lambda^2T^{-1}(w+f_T(T^{-1}y)))$.

For $k=(u_0,\ldots,u_4)\in K$, let $B_i(u_i)$ be the
normalized prism over the $i$-th graph edge. Close its fibre
boundary by the ordered polygon with sides
$T_0u_0,-u_0,\ldots,T_4u_4,-u_4$, retaining the self terms
$p(u_i,-u_i)$. Its lifted central coordinate is $z(k)$.
The actual integral splitting is
\[
 (c,k)\longmapsto \operatorname{fibre}(c)+Z(k)
                         -\operatorname{fibre}(z(k)),
 \qquad H_2(V)\simeq\operatorname{coker}R\oplus K.
\]
The inverse projects a cycle to its primitive graph coordinate,
subtracts this exact prism/polygon section, and reads the remaining
fibre coinvariant. The normalized bar boundary formula and the
central group law prove both composites are the identity.
In these coordinates a fixed-normal torus at site $i$ is
\[
        (f_{T_i}(u),K^{-1}J_i u),\qquad (T_i-I)u=0,
\]
where $J_i$ inserts $u$ in the $i$-th graph block. There is no
second subtraction of $z(k)$. This specifies the full integral
fixed-normal columns and preserves the order-two fibre class.

\item \emph{The ordinary boundary word and its Thom columns.}
The positive ordinary word is
$\theta_o=(\theta_0\cdots\theta_4)^{-1}$.
Set $P_i=T_{i+1}\cdots T_4$ and
\[
 J_o u=(-P_0u,\ldots,-P_4u),\qquad
 c_o(u)=-\sum_{i=0}^4 f_{T_i}(P_i u)\pmod{\operatorname{im}R}.
\]
Applying the actual inverse lifted maps in their word order gives
the same correction: the difference has its retained integral
preimage under $R$. As the product monodromy is identity, this
map is additive in the fibre coinvariant; the signed word formula
proves the assertion for every integral $u$.

Let $v=-e\gamma$. The ordinary $m=1$ cap has boundary map
\[
 (y,\tau)\longmapsto(x=y-\tau v,e^{2\pi i\tau}),\qquad
 (x,\tau)\longmapsto(y=x+\tau v,\tau)
\]
as its inverse. Its meridian is $\mu_o-v=\mu_o+e\gamma$.
The four fixed-normal Thom columns and the core column in the
above exterior splitting are
\[
 \left(c_o(u)-u\wedge v,K^{-1}J_o u\right)
       \quad(u=e_1,e_2,\delta,\gamma),\qquad
 \left(c_o(v),K^{-1}J_o v\right).
\]
They are induced by the displayed cap map, including the sign
of its meridian, not by a rank substitution.

\item \emph{The exact finite presentation and its inverse coordinates.}
Use six free fibre coordinates and17 graph coordinates. The
full matrix $B$ has23 rows and59 columns, in this exact order:
the30 columns of $R$, the ten cap fibre-kernel columns, the14
singular fixed-normal columns, and the five ordinary columns.
The preceding formulas give every entry from the displayed raw
matrices, the two pairs, the selected site and $e$.
The resulting exact Smith factors are
\[
\begin{array}{c|c|c|c|c}
 (a,b)&\text{selected }I_1&e&\operatorname{rank}B
                           &\text{nonzero Smith factors}\\\hline
 (2,4)&1,2,3,4&-1,+1&23&1^{22},4\\
 (4,2)&1,2,3,4&-1,+1&23&1^{22},2.
\end{array}
\]
Every row of this table denotes its eight separate choices.
The integer computation retains $U,B,V,D_B=UBV$ and
$U^{-1},V^{-1}$, verifies both inverse products and every
divisibility step, and reads all sixteen outputs.
The quotient isomorphism and its inverse are explicitly
\[
 [z]\longmapsto (Uz)_{23}\pmod b,\qquad
 1\pmod b\longmapsto[U^{-1}e_{23}].
\]
The relation $bU^{-1}e_{23}=BV e_{23}$ and the unit Smith
columns prove both composites. Thus this calculation is an
integral presentation proof, including the marking and inverse,
of $\operatorname{coker}B=\mathbb Z/b$.

For clarity concerning the older retained computation, its
23 by70 presentation includes six zero ordinary fibre columns
and five redundant triangular-cap fibre columns. The actual
free-group change from
$(\theta_o,\theta_0,\ldots,\theta_3)$ to
$(\theta_0,\ldots,\theta_4)$ has the inverse words specified
above. On graph coordinates it is
\[
 (u_o,u_0,u_1,u_2,u_3)
     \longmapsto J_o u_o+(u_0,u_1,u_2,u_3,0).
\]
On the23 generators its additional central term is
$C_oE_oK_{\rm old}$, where $C_o$ has columns $c_o(e_j)$
and $E_o$ selects the old ordinary block. Hence the marked
row map is
$M=\left(\begin{smallmatrix}I_6&C_oE_oK_{\rm old}\\0&Q\end{smallmatrix}\right)$,
with inverse
$\left(\begin{smallmatrix}I_6&-C_oE_oK_{\rm old}Q^{-1}\\0&Q^{-1}\end{smallmatrix}\right)$.
Both are integral. The retained comparison supplies exact
relation maps $B C=M B_{\rm old}$ and
$B_{\rm old}D=M^{-1}B$, proving equality of the marked
quotients and explaining the relation count. The chosen proof
of the groups is the59-column computation just given.

\item \emph{The relative map and full fundamental group.}
Each cap $H_2$ specialization is onto, as its explicit section
shows. The only possible additional degree-two contribution
is the kernel of the relative component-disc map to $H_1(V)$.
After the vertical fibre relations, take the positive basis
$(\gamma,\mu_0,\ldots,\mu_4)$ of $H_1(V)$.
The five singular discs map to $\mu_i$, and the ordinary disc
maps to $e\gamma-\sum_i\mu_i$. Thus the full relative map is
\[
 (t_o,t_0,\ldots,t_4)
       \longmapsto(e t_o,-t_o+t_0,\ldots,-t_o+t_4).
\]
For $e=\pm1$ its integral inverse is
$t_o=y_\gamma/e$, $t_i=y_i+y_\gamma/e$.
Changing all five peripheral row and disc signs gives the
printed computational matrix with first column $(e,1,1,1,1,1)$;
that sign change is its own inverse. The relative kernel is zero.
Equivalently, the literal finite-first exterior matrix has
$H_1=\mathbb Z^5$ and there are five whole-fibre component
classes, but the inverse above proves the full integral claim.
Consequently $H_2(X)=\operatorname{coker}B$.

The exterior fundamental group is the actual abelian-fibre
semidirect-product presentation with the five graph words and
the matrices $T_i$. The six primitive toric vanishing vectors
are the first columns of the four rank-one period matrices and
the two short columns of the selected triangular matrix.
Their nongamma coordinates have a retained integer right inverse
onto $\mathbb Z\langle e_1,e_2,\delta\rangle$ in every one
of the eight geometric choices. Thus their unsaturated normal
closure kills that entire abelian normal fibre subgroup.
All singular peripheral words bound the specified origin discs.
The last ordinary relation is then $\gamma^e=1$, with $e=\pm1$.
This proves $\pi_1(X)=1$ in the actual group presentation.

\item \emph{The remaining homology and the computation scope.}
All regular and boundary torus pieces have Euler characteristic0.
The four rank-one caps have Euler characteristic0 and the unique
triangular cap contributes2, so $\chi(X)=2$.
The manifold is closed and oriented. Since $H_1=0$ and $H_2$
is finite, universal coefficients and integral duality give
$H_5=0$, $H_4=H^2=0$ and
$\operatorname{Tor}H_3\simeq\operatorname{Ext}(H_2,\mathbb Z)
\simeq\mathbb Z/b$. More concretely, send the displayed
$H_2$ generator to $1/b$ in $\mathbb Q/\mathbb Z$, take its
Bockstein in $H^3$, and cap with the oriented fundamental class.
The inverse is the perfect torsion linking evaluation against
that generator. The Euler equation now makes the free rank of
$H_3$ zero. Together with $H_0=H_6=\mathbb Z$, these are
exactly all the groups in \eqref{maps:eq:D.VC7}.

The complete fresh calculation is retained in
\path{code/S6_SERIES_PUBLISH_c7_ls_os45_bar_v001.py} and its
actual output, including all period, cap, bar, normal, relative
and inverse matrices. The exhaustive local and historical
auxiliary checks are retained in
\path{code/S6_SERIES_PUBLISH_c7_ls_post_local_v001.py},
\path{code/S6_SERIES_PUBLISH_c7_ls_post_obstructions_v001.py}
and \path{code/S6_SERIES_PUBLISH_c7_ls_post_relations_v001.py}.
They verify all227 local pairs,5696 global residues,82 actual
monodromy/cocycle orders, the sixteen additional initial pairs,
and every field of the sixteen old marked filling outputs.
The lossless readers supply exact inverse expansions to every
output byte, including scalar metadata and the original order.
The historical target programs themselves were read at their
disclosed scope and were not executed in this check. These
finite certificates support the explicit geometric and integral
maps proved above; they do not infer smooth diffeomorphism types
from homology or identify untransported changes of boundary framing.
\end{enumerate}
\end{proof}'''
receiver=statement+'\n\n'+proof+'\n'
old=(LANE/'S6_SERIES_PUBLISH_III_02LS_released_statement.tex').read_text()+(LANE/'S6_SERIES_PUBLISH_III_02LS_released_proof.tex').read_text()
for pattern in (r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}'):
    assert sorted(re.findall(pattern,old))==sorted(re.findall(pattern,receiver))
assert receiver.count(r'\begin{theorem}')==receiver.count(r'\end{theorem}')==1
assert receiver.count(r'\begin{proof}')==receiver.count(r'\end{proof}')==1
out=LANE/'S6_SERIES_PUBLISH_III_02LS_receiving.tex'
out.write_text(receiver)
assert sha256(fresh.read_bytes()).hexdigest()=='ee6cbed56c156a8f590c0f7926121a9a3baf5ba4fdbccf9302d56a7df126ef7d'
print('COMPLETE',datetime.now(timezone.utc).isoformat())
print('RECEIVER',out.relative_to(W),'LINES',len(receiver.splitlines()),'BYTES',len(out.read_bytes()),'SHA256',sha256(out.read_bytes()).hexdigest())
print('PERMANENT_IDENTITIES all label/hypertarget/tag multisets preserved; one theorem and one proof.')
print('SCOPE local receiver only; canonical, globals and frozen fresh unchanged.')
