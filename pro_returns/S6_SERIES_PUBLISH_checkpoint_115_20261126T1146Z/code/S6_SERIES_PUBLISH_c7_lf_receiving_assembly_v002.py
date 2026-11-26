#!/usr/bin/env python3
"""Assemble the complete LF receiving theorem/proof; canonical source is read-only."""
from pathlib import Path
from hashlib import sha256
import re

BASE = Path('agents/continuation7_iii_three_primary')
LANE = Path('agents/continuation7_iii_three_primary_receiving')
oldstatement = (BASE/'S6_SERIES_PUBLISH_III_02LF_released_statement.tex').read_text()
oldproof = (BASE/'S6_SERIES_PUBLISH_III_02LF_released_proof.tex').read_text()
statement = oldstatement[oldstatement.index(r'\begin{theorem}'):]
statement = '\n'.join(line for line in statement.splitlines()
                      if not line.startswith(r'\StatementRecord')) + '\n'
statement = statement.replace('the full nine-valued invariant in the $c=3$ sector',
                              'The order-nine invariant in the $c=3$ sector')
statement = statement.replace('retain the indicated additive\nchoice and the ordinary clutch',
                              'with the indicated additive\nchoice and ordinary clutch')
statement = statement.replace('In particular the assertion about $\\mu$ determines its order-three\n'
                              'subgroup as well as its ordinary mod-three cubic reduction.\n', '')

proof = r'''\begin{proof}
\paragraph{The integral marking and the cap maps.}
Write
\[
 \Lambda=\mathbb Z\langle e_1,e_2,\delta,\gamma\rangle,
 \qquad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
 \qquad\omega=a e_1^*\wedge e_2^*-b\delta^*\wedge\gamma^*,
 \qquad\chi=\gamma^*.
\]
The positive scalar circle is translation by $t\delta$, $t\in\mathbb R/\mathbb Z$.
The arrow $\gamma$ is the forward contracting arrow covering $-bG$.
All curves have their complex orientations. The local data at the selected
place in the seven marked rows underlying \eqref{maps:eq:D.T31} are
\[
\begin{array}{c|r|r|r|r|r}
\text{profile}&a&b&\text{zero}&\nu&\kappa\\\hline
II&5&3&0&2&-1\\
III&1&6&0&5&-4\\
III&5&6&3&1&-1\\
III&10&3&3&1&-1\\
\text{default}&5&3&2&2&-1\\
\text{default}&10&3&3&1&0\\
\text{default}&10&3&4&1&-1
\end{array}
\]
The first row has the two additive choices in the statement. In particular
$b\in\{3,6\}$, $a\nu=30/b$, and $3\nmid a\nu$.
In the defining elliptic marking, a multiplicative monodromy and section
cocycle are
\[
 A_i-I=\nu_i u_i u_i^tJ,\qquad g_i=\kappa_i u_i,
 \qquad\det(u_i,v_i)=1,
\]
where the first nonzero entry of $u_i$ is positive. At a finite elliptic
matrix set $z_i=(A_i-I)^{-1}g_i$; at a multiplicative place set
$z_i=(\kappa_i/\nu_i)v_i$. The four-period monodromies are
\[
 \beta_i=-a g_i^tJA_i,\qquad c_i=\beta_i b z_i+w_i,
 \qquad
 T_i=\begin{pmatrix}A_i&0&bg_i\\\beta_i&1&c_i\\0&0&1\end{pmatrix},
 \qquad
 w_i=\begin{cases}1/\nu_i&i\text{ selected},\\0&\text{otherwise}.
 \end{cases}
\]
Their inverse maps are
\[
 T_i^{-1}=\begin{pmatrix}
 A_i^{-1}&0&-bA_i^{-1}g_i\\
 -\beta_iA_i^{-1}&1&b\beta_iA_i^{-1}g_i-c_i\\0&0&1
 \end{pmatrix}.
\]
Substitution gives integral matrices, $T_i^*\omega=\omega$,
$T_i\delta=\delta$, $\chi T_i=\chi$, and the ordered product $\prod_iT_i=I$.
On a cut base the period map is
$x\bmod\Lambda\mapsto\Pi(q)x\bmod\Pi(q)\Lambda$, with inverse the group
logarithm modulo that lattice. Here $\Pi$ consists of the elliptic and line
period functions, including their holomorphic units. For an integral basis
$H$, replacing $\Pi$ by $\Pi H$ replaces coordinates by $H^{-1}x$.
The inverse basis change reverses this map, preserving the base coordinate,
zero section, and line frames.

Let $\mathcal E$ be the regular torus bundle after all cap discs have been
removed. We use the integral period-graph and cap maps of
\ref{maps:src:D.2.26}, in the following coordinates. In wedge order
$12,13,14,23,24,34$, put
\[
 B_2=[\wedge^2T_1-I\ \cdots\ \wedge^2T_N-I],\qquad
 \omega=(a,0,0,0,0,-b).
\]
Choose $ax+by=1$ and $s_0=xe_{12}-ye_{34}$. Integer row and column
reduction gives five unit nonzero Smith factors and an integer matrix
$R_2$ with
\[
 B_2R_2=I-s_0\omega,\qquad\omega B_2=0,\qquad\omega(s_0)=1.
\]
Thus the fibre quotient and its inverse are
\[
 [v]\longmapsto\omega(v),\qquad n\longmapsto[ns_0].
\]
The chain bounding $v-\omega(v)s_0$ is the sum of the monodromy cylinders
with coefficients $R_2v$. Write $s=[s_0]$.

Include the removed ordinary disc as the final site, with monodromy $I$.
For $M$ sites set $D=[T_1-I\ \cdots\ T_{M-1}-I]$. The first boundary
maps are block inclusions, and the last is
\[
 j_M(x)=-(T_2\cdots T_{M-1}x,\ldots,T_{M-1}x,x),
 \qquad Dj_M(x)=(I-T_M^{-1})x.
\]
Choose each fixed basis to begin with $\delta$. These bases are
$(\delta,u)$ at the cusp, $(\delta,u,w_0)$ at a rank-one place,
$(\delta,\ell)$ at a finite additive cap, $(\delta,\ell_0)$ at an
original additive cap, and $(\delta,e_1,e_2,\gamma)$ at the ordinary disc.
The vectors $w_0,\ell,\ell_0$ are given below. If
$B=[j_1F_1\ \cdots\ j_MF_M]$, then $\operatorname{im}B=\ker D$
integrally, and
\[
 \ker B=\mathbb Z\sum_i e_{\delta,i}.
\]
An explicit inverse on $\ker D$ is obtained by reducing
$U_DDV_D=\operatorname{diag}(I_3,0)$, denoting the final columns of $V_D$
by $V_0$, and solving $BS=V_0$ by integer operations. It is
$R_{\rm graph}=S(V_D^{-1})_{\text{rows}>3}$, with
$BR_{\rm graph}y=y$ for $Dy=0$. The reduction of $B$ has only unit
nonzero factors and one relation. The fixed loops sweep the boundary
circles; their addition and subtraction are the period triangles
with vertices $0,u,u+v$. Projection to the graph, this inverse, and
the fibre quotient give
\[
 H_2(\mathcal E;\mathbb Z)=\mathbb Zs\oplus
 \left(\bigoplus_i\operatorname{Fix}(T_i)\right)
             /\mathbb Z\sum_i\delta_i.
\]
The last relation is the scalar circle over the cut base. The ordinary
clutch $\prod c_i=\gamma^e$ adds
$-\omega(\delta,e\gamma)=be$ to it.

At an original additive cap put $z=(A-I)^{-1}g$, $h=az\in\mathbb Z^2$,
$z_Q=bz$, and $\lambda=-h^tJ$. Its line-frame maps are
\[
 S_P(x,d,g_0)=(x,d+\lambda x,g_0),\qquad
 S_P^{-1}(x,d',g_0)=(x,d'-\lambda x,g_0).
\]
The identity $\lambda(A-I)+\beta=0$ removes the line shear. Zero
multidegree trivializes the smooth complex line bundle on that elliptic neighbourhood.
The contracting quotient is a mapping torus with a positive roof $r(y)$.
Choose $k\max r<1$ and a nonnegative smooth function $b_y$ supported away from the
ends of $[0,r(y)]$ with integral one. The increasing function
\[
 f_y(t)=\int_0^t\{k+(1-kr(y))b_y(v)\}\,dv
\]
and its inverse identify that roof with a unit interval, with matching
end derivatives. Translation by the identity-component N\'eron logarithm
times the interval parameter, with a cutoff at its ends, removes that
part of the return; the negative translation is the inverse. The
remaining finite translation has one orbit on the rational components.
Reciprocal line gauges preserve their node constants.
For type $II$ put $q=1$, and for type $III$ put $q=2$. The cap has
$H_2=\mathbb Z[C]\oplus\mathbb Z[\delta\gamma]$, with elliptic fibre
$q[C]$. In the $S_P$ coordinates its fibre map is
\[
 f_2(y)=\bigl(q(y_{12}+z_{Q,2}y_{14}-z_{Q,1}y_{24}),y_{34}\bigr).
\]
The first coordinate is obtained by $x\mapsto x+z_Qx_\gamma$;
subtraction is the inverse. Choose
$qA+qz_{Q,2}B-qz_{Q,1}C=1$. A section sends $[C]$ to
$\wedge^2S_P^{-1}(Ae_{12}+Be_{14}+Ce_{24})$ and
$[\delta\gamma]$ to $e_{34}$. Component transitivity gives these integers.
The fixed lattice has basis
\[
 \delta,\qquad\ell_0=(-qz_{Q,1},-qz_{Q,2},0,q).
\]
The two sweeps bound the origin disc and the $q$-fold forward orbit tube,
closed using the same logarithm and line frame. At original $III$ the
second vector is $(-3,9,0,2)$.

At a primitive rank-one cap, in the ordered basis $(l,h,p_0,w_0)$ below,
the fibre maps and their sections are
\[
 f_1(x)=(x_2,x_3,x_4),\qquad
 f_2(y)=(y_{12},y_{23},y_{24},y_{34}),
\]
with sections inserting zeros in the omitted positions and then applying
the period basis. The normalization is one ruled component, with its
zero and infinity sections identified along the elliptic core. Its
normalization/conductor sequence gives these generators; fixed sweeps
bound the normal toric chains. At the cusp, use
$H=(SCe_1,Le_1,SCe_2,Le_2)$, with $S,L,C$ defined below. The maps are
\[
 f_1(x)=(x_2,x_4),\qquad
 f_2(y)=(y_{12},y_{14}-y_{23},y_{24},y_{34}).
\]
The section of $f_2$ inserts $(u,0,v,0,w,z)$ and applies $\wedge^2H$.
Its primitive kernel is generated by $e_{13},e_{14}+e_{23}$, the local
Wang image. The cusp charts below give the corresponding normal chains.

\paragraph{Finite caps and arbitrary affine parameters.}
For finite $II$ and $III$, respectively, write $(d,q)=(6,1)$ and $(4,2)$.
The vector $\ell=(-bz_1,-bz_2,0,1)$ is integral. The power and
multiplicity of a simply connected finite filling have the form
\[
 v=n\ell+r\delta,\qquad m=dk,\quad k\in\mathbb Z_{>0},\quad r\in\mathbb Z,
 \qquad me-n=\varepsilon\in\{1,-1\}.
\]
In particular $\gcd(m,n)=1$. The return is $x\mapsto Tx+v/m$.
For a lift $Tx+t$ with $N_mt=v$, where $N_m=\sum_{j=0}^{m-1}T^j$,
put $\pi=N_m/m$. On $\ker\pi$, the operator $I-T$ is invertible;
solving $(I-T)h=t-v/m$ gives the conjugacy $x\mapsto x+h$, with inverse
$x\mapsto x-h$. It commutes with scalar translation.
For base-dependent holomorphic lifts on the good root disc, let
$\sigma(u)=\zeta u$ and let $A(u):E_u\to E_{\sigma u}$ be the linear
deck map on its Lie bundle. Put
\[
 (\mathcal Rf)(u)=A(\sigma^{-1}u)f(\sigma^{-1}u),\qquad
 \mathcal N=\sum_{j=0}^{m-1}\mathcal R^j,\qquad\mathcal R^m=I.
\]
Two lifts with the same integral power have terms $b_0,b_1$ with
$\mathcal N(b_1-b_0)=0$. The holomorphic section
\[
 h=-\frac1m\sum_{j=0}^{m-1}j\mathcal R^j(b_1-b_0)
\]
satisfies $(I-\mathcal R)h=b_1-b_0$. Translation by $h$, inverted by
translation by $-h$, gives the conjugacy on the disc and collar.
Changing a period representative changes the power by $N_m\lambda$;
aligning those representatives gives the same comparison.

Choose a vertical coinvariant $\beta_0$ and a period $y$ with
\[
 q\beta_0+(T-I)y=\delta,\qquad
 N_d\beta_0=(d/q)\delta,\qquad N_d\ell=d\ell,
 \qquad-\omega(\beta_0,\ell)=b/q.
\]
For $II$, take $\beta_0=\delta$, $\ell=\gamma$. For $III$ with
$a=1$ or $5$ and $b=6$, take
\[
 \ell=(-3,9,0,1),\quad
 \beta_0=(0,-1,(1-a)/2,0),\quad y=(-5,11,0,0).
\]
The inverse coinvariant coordinates are $(-3a,-a,2,0)$ and $(0,0,0,1)$.
They give a primitive section of the quotient by $(T-I)\Lambda$.
An integer right inverse of $[T-I\mid\beta_0\mid\ell]$ expresses any
change of these representatives as an explicit $(T-I)$-boundary;
negating the boundary reverses the change.

Writing $D=t(\delta)$ and $L=t(\ell)$ for fixed sweeps, the meridian
$m\mu-v$ gives the Thom columns in coordinates $(s,D,L)$:
\[
 C_1=(bn/q,m/q,0),\qquad C_2=(-br,0,m),\qquad C_3=(0,r,n).
\]
The boundary map and its inverse are
\[
 [y,\tau]\longmapsto[y+(\tau/m)v,e^{2\pi i\tau/m}],\qquad
 [x,z]\longmapsto[x-(\tau/m)v,\tau].
\]
A change of root argument is exactly the mapping-torus relation on both
sides. The normal circle is $(y,\tau)\mapsto(y-tv,\tau+mt)$.
The central surface satisfies
\[
 H_1(F)=\langle\beta_0,\ell,c\mid mc=n\ell+rq\beta_0\rangle.
\]
For $A_0m+B_0n=1$, a basis and inverse are
\[
 \beta_0,\ z=A_0\ell+B_0c;\qquad
 \ell=mz-B_0rq\beta_0,\quad c=nz+A_0rq\beta_0.
\]
Thus $H_1(F)$ is free of rank two. Its finite torus cover and transfer
give rational Betti numbers $(1,2,2,2,1)$; integral duality then makes
$H_2(F)$ and $H_3(F)$ free. The flat normal line has torsion Chern class
in the free group $H^2(F;\mathbb Z)$, so this class is zero.
Transfer of a loop $\lambda$ is the torus
$[s\lambda,\exp(2\pi it)]$. Cutting into $m$ sectors gives fibre area
$-\lambda\wedge v$ and sweep $N_m\lambda$; rejoining gives the inverse
chain map. The torus for $c$ has area zero and sweep $v$.
Thom exactness on the displayed basis gives the complete integral kernel
$\langle C_1,A_0C_2+B_0C_3\rangle$.

There is at most one finite cap. Its Seifert presentation is
\[
 \langle\gamma,c\mid[\gamma,c]=1,
                  \ c^m=\gamma^n,\ c=\gamma^e\rangle,
\]
which is trivial exactly when $me-n=\varepsilon=\pm1$.
In the other rows the group is trivial exactly when $e=\pm1$.
Take $A_0=\varepsilon e$, $B_0=-\varepsilon$. Then
\[
 \begin{aligned}
 K_0&=A_0C_2+B_0C_3=(-A_0br,B_0r,1),\\
 C_2-mK_0&=-B_0qrC_1,\qquad
 C_3-nK_0=A_0qrC_1.
 \end{aligned}
\]
These identities give both directions of the generator change.
The ordinary polygon relation $D=-be\,s$ gives
\[
 L=br(A_0+B_0e)s=0,\qquad
 (b/q)(n-me)s=-3\varepsilon s=0.
\]
Without a finite cap the remaining relation is $be\,s=0$, with
$b=3$ and $e=\pm1$. A peripheral change $c\mapsto c\lambda$ changes
the power by $N_m\lambda$ and changes a fixed sweep by
$t(u)\mapsto t(u)+\omega(u,\lambda)s$; the opposite shear and inverse
period change reverse the map. This proves the same quotient for all
the affine representatives and all integers $k,e,r$ above.
Mayer--Vietoris with the fibre sections and graph inverse therefore gives
\[
 H_2(X;\mathbb Z)=\mathbb Z/3\langle s\rangle.
\]
The two zero-dimensional toric strata at the cusp contribute Euler
number two. All other torus strata and caps have Euler number zero.
Simple connectivity, duality, and the universal coefficient sequence give
\[
 H_0=H_6=\mathbb Z,\qquad H_1=H_4=H_5=0,\qquad
 H_2=H_3=\mathbb Z/3,\qquad b_3=0.
\]
Consequently $H^2(X;\mathbb Z)=H^2(X;\mathbb F_2)=0$; the complex first
Chern class vanishes and the spin structure is unique. Let
$\alpha\in H^2(X;\mathbb F_3)$ satisfy $\alpha(s)=1$.

\paragraph{The primitive period charts and circle isotropy.}
At an unselected multiplicative place set
\[
 d_0=\gcd(\nu,a\kappa),\quad n_0=\nu/d_0,
 \quad A'=a\kappa/d_0,\quad B'=b\kappa/n_0.
\]
Here $B'$ is integral and $\gcd(d_0,B')=1$. Choose
$n_0\theta+A'\sigma=1$ and $d_0x+B'y=1$. With
$S=(u,\delta)$ and $L=(v,\gamma)$ put
\[
 C_S=\begin{pmatrix}n_0&\sigma\\-A'&\theta\end{pmatrix},\qquad
 C_L=\begin{pmatrix}x&-B'\\y&d_0\end{pmatrix},
\]
\[
 C_S^{-1}=\begin{pmatrix}\theta&-\sigma\\A'&n_0\end{pmatrix},\qquad
 C_L^{-1}=\begin{pmatrix}d_0&B'\\-y&x\end{pmatrix}.
\]
Define $(l,p_0)=SC_S$, $(h,w_0)=LC_L$. The ordered basis
$(l,h,p_0,w_0)$ has determinant one and return $h\mapsto h+l$.
Its pairing and scalar vector are
\[
 K_N=(SC_S)^t\omega(LC_L)=\begin{pmatrix}N&0\\M&R\end{pmatrix},
 \quad N=a\nu/d_0^2,\quad R=-bd_0^2/\nu,\quad
 \delta=-\sigma l+n_0p_0.
\]
The identity on the period cover, followed by these basis changes and
exponentiation of $l$, gives adjacent Tate charts
\[
 X=z/q^j,\quad Y=q^{j+1}/z,\quad XY=q;\qquad
 z=Xq^j,\quad q=XY.
\]
The primitive long period identifies successive charts, with its period
units. The inverse uses the inverse basis matrices and these inverse
chart formulas. The elliptic conductor has primitive periods $p_0,w_0$.
The scalar circle translates it by $n_0t\,p_0$.
In every row there is exactly one site with $3\mid n_0$: the $I_3$
site, where $d_0=1$, $n_0=3$, $N=3a$, and $R=-b/3$.
Call its elliptic conductor $E$. Its stabilizer is $C_3$ and its two
normal characters are $-\sigma,\sigma$, both units modulo three.
Away from the node a nonzero normal coordinate is rotated by that
character. Every other rank-one site has $n_0=1$, so the translation
by $n_0/3$ on its conductor is nontrivial.

At the selected cusp put
\[
 \rho=(1-ab\kappa^2)/\nu,\qquad
 C=\begin{pmatrix}\nu&b\kappa\\-a\kappa&\rho\end{pmatrix},\qquad
 C^{-1}=\begin{pmatrix}\rho&-b\kappa\\a\kappa&\nu\end{pmatrix}.
\]
This integral matrix has determinant one, and $(T-I)L=SC$.
Thus the short basis of the prescribed Jordan fan is $SC$, and the
scalar circle has short coordinates
\[
 d_\delta=C^{-1}(0,1)^t=(-b\kappa,\nu)^t.
\]
Write $k=b\kappa$. Then $3\mid k$ and $3\nmid\nu$. The vertical edge
of the prescribed unit triangulation is the unique edge direction
parallel to $d_\delta$ modulo three. Its curve $C_0$ has charts
\[
 (x,y,w)=(q/(X_1X_2),X_2,X_1),\qquad
 (X_1,X_2,q)=(w,y,xyw),
\]
\[
 (x',y',w')=(q/X_2,X_1X_2,X_1^{-1}),\qquad
 (X_1,X_2,q)=(1/w',y'w',x'y'w').
\]
Their transition and inverse are
\[
 (x',y',w')=(wx,wy,w^{-1}),\qquad
 (x,y,w)=(w'x',w'y',(w')^{-1}).
\]
Hence $C_0\cong\mathbb P^1$ with normal bundle
$\mathcal O(-1)\oplus\mathcal O(-1)$. The circle weights in these charts are
\[
 (k-\nu,\nu,-k),\qquad(-\nu,\nu-k,k).
\]
It fixes $C_0$ pointwise for $k=0$ and rotates it with tangent weight
$-k$ for $k\ne0$. In either case $C_3$ fixes $C_0$, and its two normal
characters are nonzero. Every triangle contains a vertical edge; its
two vertex orbits are the two endpoints of this curve. A translation
fixing a bounded edge fixes both endpoints and is zero, so the edge
quotient is embedded.

On an original additive cap, a norm strictly decreasing under the
positive contracting arrow excludes equality of a nonzero vector with
a nonzero iterate times a unit scalar. The zero iterate fixes that
vector only for the identity scalar. Thus its scalar action is free.
At a finite cap, an equality between scalar translation and the $j$th
deck iterate implies $jn/m\in\mathbb Z$ after applying $\chi$.
Since $\gcd(m,n)=1$, this forces $m\mid j$; primitivity of $\delta$
then makes the scalar trivial. Off the core the base rotation gives
the same divisibility. The ordinary cap is free for the same primitive
torus-translation reason. We have proved
\[
                         X^{C_3}=C_0\sqcup E.
\]
Every nontrivial subgroup of $C_9$ contains $C_3$. Consequently $C_9$
is free on the complement and on the two normal sphere bundles.

\paragraph{One equivariant line on the partial completion.}
Let $Y$ denote the completion at all multiplicative places, with the
ordinary disc and the additive discs still removed. On its real period
cover define
\[
 J_\lambda(x,z)=(x+\lambda,e^{2\pi i\omega(\lambda,x)}z).
\]
The cocycle quotient is $e^{2\pi i\omega(\lambda,\mu)}=1$ and the
inverse is $J_{-\lambda}$. The connection
$d-2\pi i\omega(x,dx)$ has first Chern class $2\omega$ in the positive
line convention. Monodromy lifts by $(x,z)\mapsto(T_ix,z)$, with
inverse $(x,z)\mapsto(T_i^{-1}x,z)$.
The scalar generator of $C_3$ lifts as
\[
 \mathcal T(x,z)=
 (x+\delta/3,e^{2\pi i\omega(\delta/3,x)}z).
\]
Its commutator with each period is one because
$\omega(\delta/3,\Lambda)=-(b/3)\mathbb Z$, and its third power is
$J_\delta$. These formulas define a $C_3$-equivariant line $\mathcal D$.

For its holomorphic comparison put $D_0=\operatorname{diag}(a,-b)$
and $Z=U+\Omega_{\rm ph}W$. The entries of $\Omega_{\rm ph}$ are
$\tau,-b\zeta_G;a\zeta_G,\rho_L$, so $D_0\Omega_{\rm ph}$ is symmetric.
The gauge
\[
 G_0=\exp\{-2\pi i(U^tD_0W+W^tD_0\Omega_{\rm ph}W)\}
\]
and its reciprocal give short factors one and long factors
$h_1^{-a}z^{-2a}$ and $R^bv^{2b}$. Multiplication of the vector
coordinate by $z^a$, with inverse $z^{-a}$, gives
\[
 \begin{aligned}
 h(z,v,\zeta)&=(h_1z,h_G^av,z^{-2a}\zeta),\\
 F(z,v,\zeta)&=(h_G^{-b}z,Rv,h_G^{-ab}R^bv^{2b}\zeta),\\
 J(z,v,\zeta)&=(z^{-1},v^{-1},z^{-2a}\zeta).
 \end{aligned}
\]
For $h,F$ the inverse auxiliary factors, in target coordinates, are
$h_1^{-2a}z^{2a}$ and $h_G^{ab}R^bv^{-2b}$; $J$ is its own inverse.
Substitution gives $hF=Fh$, $JhJ=h^{-1}$, and $JFJ=F^{-1}$.
The functions $h_1,h_G,R$ include their units. Overlaps are $G_0$,
the integral period change, and the reciprocal gauge of the next
chart. Their triple compositions cancel. The origin section and a
nonzero line frame on the punctured base fix the origin frames.
On a fixed-loop sweep the connection integral and monodromy multiplier
are zero; hence $\mathcal D$ has degree two on $s$ and zero on every
section sweep.

In the rank-one basis set $\Omega=C_S^{-1}\Omega_{\rm ph}C_L$.
Its return adds $E_{11}$ and $K_N^t\Omega$ is symmetric. The gauge
\[
 G_N=\exp\{-2\pi i(U^tK_NW+W^tK_N^t\Omega W)\}
\]
and its reciprocal have long factors
$\exp(-4\pi i h^tK_N^tZ-2\pi i h^tK_N^t\Omega h)$.
The integral support $Nj^2$ has difference $2Nhj+Nh^2$, giving
the normal monomial factors in the Tate charts. The other factors
are the units of $\Omega$. Replacing $\Omega$ by $\Omega+E_{11}$
and replacing $U$ by $U+E_{11}W$ both add $NW_1^2$ to the exponent
before multiplication by $-2\pi i$, proving compatibility around the base.
In physical coordinates let $r=\operatorname{ord}h_G=-\kappa$,
$\rho=\operatorname{ord}R=-ab\kappa^2/\nu$, and write the two
valuation periods as $\alpha_0u_0,\beta_0u_0$, where
$\alpha_0=d_0$, $u_0=(n_0,-A')$, and $\beta_0=B'$.
Then $a\beta_0u_{0,1}+b\alpha_0u_{0,2}=0$ and the physical support is
\[
 \psi_1(j)=-\frac{a u_{0,1}}{\alpha_0}j(j-\alpha_0)
          =-Nj^2+N\alpha_0j.
\]
Its period differences are $-2au_{0,1}j$ and
$2bu_{0,2}j+b\rho-ab r$. The residual of the second equality factors as
$(a\beta_0u_{0,1}+b\alpha_0u_{0,2})(\alpha_0-\beta_0-2j)/\alpha_0$.
The linear term is the gauge $z^a$, and the quadratic sign is the
change from frame to vector coordinates. At the $I_3$ core,
$\delta/3=-\sigma l/3+p_0$; its integral short shift adds no character.
The local character is $-\sigma N(2j+1)$, divisible by three.
The complex-oriented torus $(p_0,w_0)$ specializes with coefficient one
to $E$, giving
\[
                  \deg\mathcal D|_E=-2b/3.
\]

At the cusp,
\[
 K=C^tD_0=
 \begin{pmatrix}a\nu&ab\kappa\\ab\kappa&b(ab\kappa^2-1)/\nu\end{pmatrix},
 \qquad Kd_\delta=(0,-b)^t.
\]
Both $K$ and $K\Omega$ are symmetric. The gauge
\[
 G_C=\exp\{-2\pi i(U^tKW+W^tK\Omega W)\}
\]
and its reciprocal give long factors
$q^{-h^tKh}X^{-2Kh}\exp(-2\pi i h^tKB(q)h)$.
The integral support $\psi(t)=t^tKt$ on the prescribed unit triangles
has difference $2h^tKt+h^tKh$. On a triangle of slope $m$, the regular
frame and vector coordinate are $e_m=\chi^{-m}e$ and $z_m=\chi^mz$;
the opposite exponents give their inverses. Around the base,
$G_C(U,W,\Omega+I)=G_C(U+W,W,\Omega)$.
The physical support, with $r=-\kappa$, has the exact pullback
\[
 \begin{aligned}
 \psi_{\rm ph}(x,y)&=-a\rho x^2-2ab rxy+b\nu y^2+ax,\\
 \psi_{\rm ph}(Ct)&=-t^tKt+a(\nu t_1-brt_2).
 \end{aligned}
\]
Its two period differences are $-2ax$ and $2by+b\rho-ab r$.
The affine term is the same $z^a$ gauge. The slopes adjacent to
$[0,e_2]$ are $(K_{11},K_{22})$ and $(2K_{12}-K_{11},K_{22})$.
The first character is $b\{a\kappa(b\kappa-\nu)-1\}$ and their
character difference is $2(K_{11}-K_{12})(d_\delta)_1$, both divisible
by three. The transition in $X_1$ and $X_1^{-1}$ gives
\[
 \deg\mathcal D|_{C_0}=2(K_{11}-K_{12})=2a(\nu-b\kappa).
\]
Nonzero base units have local logarithms, are scalar invariant, and
have degree zero on these curves; their factors remain in the gauges.
This constructs one line on $Y$ with zero $C_3$ characters on both
components and the stated degrees.

\paragraph{The global Borel class and its finite characters.}
The cusp kills the two short columns $SC$, equivalently $u,\delta$.
Every other multiplicative cap kills its primitive $l$.
Their columns in the first three period coordinates form a matrix
$K_1$ with an integer right inverse $K_1R_1=I_3$ in each row.
Thus $e_1,e_2,\delta$ vanish in the fundamental group, by the cap
discs and the corresponding integer combinations. The remaining
matrix relations make $\gamma$ commute with each unfilled base meridian.
There are zero or one unfilled additive meridians, and
\[
                \pi_1(Y)=\mathbb Z_\gamma\times F_t,
                  \qquad t=0\text{ or }1.
\]
The inverse group map kills the first three periods, retains $\gamma$
and the additive meridian, and replaces the ordinary meridian by the
inverse product. This proves torsion freeness.
The graph and cap maps above send every section sweep to zero in
$H_2(X;\mathbb F_3)$: for a finite cap $L=0$ and $D=-be\,s=0$,
and for an original cap both sweeps bound. Since $H_1(Y)$ is free,
the cycle values determine the ordinary degree-two class, giving
\[
                  \tfrac12\rho_3c_1(\mathcal D)=\alpha|_Y.
\]
Here $1/2=2$ in $\mathbb F_3$.
The connected circle acts trivially on ordinary cohomology. The only
possible outgoing differentials on $\alpha$ in the Borel sequence have
targets $H^2(BS^1;H^1(X;\mathbb F_3))$ and $H^3(BS^1;\mathbb F_3)$,
both zero. Hence a class $U\in H^2_{S^1}(X;\mathbb F_3)$ restricts to
$\alpha$.

Use a toric endpoint of $C_0$ as basepoint. The circle fixes it, so
its isotopy to any group element is based and
$\pi_1(Y_{C_3})=\pi_1(Y)\times C_3$. Every finite isotropy section
has generator $(1,\zeta_3)$, since its first component lies in a
torsion-free group. In degree two the kernel of restriction to $Y$
is spanned by the base class $t$ and
$\rho_3(\lambda_j)\eta$, where the integral $\lambda_j$ form a basis
of $H^1(Y)$ and vanish on the finite factor, and
$\eta\in H^1(BC_3;\mathbb F_3)$. These realize the two positive-base
terms $(2,0)$ and $(1,1)$ in total degree two. Equivalently, the
universal-cover five-term sequence gives those same group-cohomology
terms for $\pi_1(Y)\times C_3$; its ordinary group-cohomology summand
injects into $H^2(Y)$.
Thus
$U|_{Y_{C_3}}-\tfrac12\rho_3c_1^{C_3}(\mathcal D)$
has one common base coefficient $h$ on both components. The mixed
products vanish on each finite isotropy section. Replace $U$ by
$U-hT$, with inverse addition of $hT$, where $T$ is the positive
circle character. Both finite point characters now vanish.

Put $A=a(\nu-k)$ and let $z=c_1^{S^1}(\mathcal O(1))$ on $C_0$,
with value zero at the first endpoint and $kT$ at the second.
The chart weights give $z(z-kT)=0$ and $\int_{C_0}z=1$. The restriction is
\[
             U|_{(C_0)_{S^1}}=\rho_3(Az),\qquad z(z-kT)=0.
             \tag{D.T34}\hypertarget{tag-025F}{}\label{maps:eq:D.T34}
\]
The generator satisfying $u([C_0])=1$ is
$u=A^{-1}\alpha$ in $\mathbb F_3$; its inverse change is $\alpha=Au$.

\paragraph{The coefficient-one detector and spin bordism.}
Cartan's divided-power computation gives
\[
 H_5(K(\mathbb Z/3,2);\mathbb Z)=0,\qquad
 H_6(K(\mathbb Z/3,2);\mathbb Z)=
       \mathbb Z/9\langle\gamma_3(e)\rangle,
\]
where positive reduction $\mathbb {CP}^{\infty}\to K(\mathbb Z/3,2)$
sends $[\mathbb {CP}^3]$ to $\gamma_3(e)$
\cite[Expos\'e~11, Theorems~1 and~4, pp.~11-09--11-14]{manCartan1955EML}.
Universal coefficients identify universal degree-six cohomology with
$\operatorname{Hom}(\mathbb Z/9,\mathbb Z/9)$. The detector is therefore
fixed by positive $\mathbb {CP}^3$ evaluation one:
\[
 Q_3:H^2(-;\mathbb F_3)\longrightarrow H^6(-;\mathbb Z/9),\qquad
 Q_3(\rho_3x)=\rho_9(x^3).
\]
Its coefficient map is $\gamma_3(e)\mapsto1$, with inverse
$j\mapsto j\gamma_3(e)$.
For this normalization, Thomas's cochain formula is
\[
 P_3(v)=(v^3,0)+(\Sigma^*v^2\delta v,1)
\]
\cite[(3.3)--(3.6), p.~268]{ffThomas56}.
For an integral cocycle the second term vanishes. The degree-zero
part of the diagonal carrier may be the iterated Alexander--Whitney
diagonal with augmentation one, and the carried homotopy identifies
any other such choice with it. Its product is consequently the
ordinary cube with coefficient one. This identifies Thomas's operation
with $Q_3$, including its coefficient map.
His odd-index suspension theorem gives
\[
                      Q_3(\sigma v)=0,\qquad
                      v\in H^1(K;\mathbb F_3)
\]
\cite[Theorem~I(ii), pp.~897--898; (3.1), p.~900; \S5, pp.~904--905]{ffThomas1959Suspension}.
Here suspension is the left cross product by the positive generator
of $H^1(I,\partial I;\mathbb Z)$; slant product by the interval is
its inverse. The odd-prime proof uses the relative external-product
identity and the vanishing on the dimension-one factor.
For $e\mapsto ve$ with $v\in(\mathbb Z/3)^\times$, the coefficient
map is multiplication by $v^3$ modulo nine. It is independent of the
integer lift, and its inverse is multiplication by $w^3$ when
$vw=1\pmod3$.

We also identify the refined invariant in this marking.
Zhubr's free-lift epimorphism and injective pair $(P,h)$ imply that
$\Omega^{\mathrm{Spin}}_6(K(\mathbb Z/3,2))$ is generated by the images
of $\epsilon,\zeta$, with $(P,h)(\epsilon)=(6,0)$ and
$\zeta=[\mathbb {CP}^3,x]$
\cite[\S\S3.11--3.14 and Theorem~5]{manZhubr75}.
Reduction kills $\epsilon$ because both invariants vanish.
The class $\zeta$ has $h=\gamma_3(e)$ and $P=1\pmod3$:
$c(T\mathbb {CP}^3)=(1+x)^4$ gives $p_1=4x^2$.
Thus $9\zeta$ has both invariants zero and vanishes by injectivity,
while its $h$-image has exact order nine. We obtain the exact maps
\[
 \Omega^{\mathrm{Spin}}_6(K(\mathbb Z/3,2))
   =\mathbb Z/9\langle\zeta\rangle,\qquad
 h(j\zeta)=j\gamma_3(e),\qquad P(j\zeta)=j\pmod3.
\]
In particular the kernel of the fundamental-class map is zero.

\paragraph{The C9 localization and the two component contributions.}
Let $U_9$ be the restriction of $U$ to $X_{C_9}$ and put
$R=\mathbb Z/9$. The periodic cyclic resolution gives
$H^*(BC_9;R)=R[T_9]\otimes\Lambda(\eta_9)$.
Its coefficient constants inject after $T_9$ is inverted.
Choose disjoint invariant tubular discs around $C_0$ and $E$,
and denote their union by $N$. The complement and their sphere bundles are free C9 spaces, whose
Borel spaces have the cohomology of finite-dimensional quotients.
After inverting $T_9$ these groups vanish. Relative excision and
the Thom sequences consequently give
\[
 H^*_{C_9}(X,N;R)[T_9^{-1}]=0,\qquad
 H^*_{C_9}(\partial N;R)[T_9^{-1}]=0.
 \tag{D.T37}\hypertarget{tag-025I}{}\label{maps:eq:D.T37}
\]
The normal Euler classes become invertible, and restriction has
the explicit inverse
\[
 H^*_{C_9}(X;R)[T_9^{-1}]
    \xrightarrow{\ \cong\ }
 H^*_{C_9}(C_0\sqcup E;R)[T_9^{-1}],\qquad
 (v_C,v_E)\longmapsto
       i_{C*}(v_C/e_C)+i_{E*}(v_E/e_E).
 \tag{D.T38}\hypertarget{tag-025J}{}\label{maps:eq:D.T38}
\]
These maps use the invariant tubular components with their induced
actions. Equivariant integration of $Q_3(U_9)$ lies in $H^0(BC_9;R)$
and equals the ordinary evaluation $\langle Q_3(\alpha),[X]\rangle$.

The normal roots on $C_0$ are $(k-\nu)T-z$ and $\nu T-z$.
Using \eqref{maps:eq:D.T34}, their product is
\[
 e_C=\nu(k-\nu)T^2,\qquad
 Q_3(U)|_{(C_0)_{S^1}}=\rho_9(A^3z^3)
                         =\rho_9(A^3k^2T^2z).
\]
The contribution after restriction to C9 and integration is
\[
                     \frac{A^3k^2}{\nu(k-\nu)}=0\pmod9.
\]
The denominator factors are units modulo nine and $3\mid k$.

The action on the elliptic component, in its primitive periods, is
$t\cdot(z,w)=(t^3z,w)$. The map
$[e,z]\mapsto[er]\in ES^1/C_3$, where $r^3=z$, has inverse
$[e]\mapsto[e,1]$. Changing the root multiplies by C3 and leaves
the map unchanged; the associated relation
$[et,z]=[e,t^3z]$ verifies it on the Borel quotient. With the second
circle this gives
\[
 E_{S^1}\simeq BC_3\times S^1,\qquad
 U|_{E_{S^1}}=d_E\,\eta\,\rho_3(\xi),\qquad d_E=-b/3.
 \tag{D.T35}\hypertarget{tag-025G}{}\label{maps:eq:D.T35}
\]
Here the positive first-period loop maps to the specified C3 generator,
and $\xi$ is the integral generator on the second circle.
The degree-two base coefficient vanishes by the common-character
calculation. The mixed coefficient is $d_E$, by the ordinary degree
of $\tfrac12c_1(\mathcal D)$.
Flip the factors and collapse the wedge to obtain
$c:BC_3\times S^1\to S^1\wedge BC_3$.
The left suspension pulls back as
$c^*\sigma(\eta)=\rho_3(\xi)\eta=-\eta\rho_3(\xi)$.
Thus \eqref{maps:eq:D.T35} is $c^*\sigma(-d_E\eta)$ and
\[
 Q_3(U)|_{E_{S^1}}=c^*Q_3(\sigma(-d_E\eta))=0
                  \quad\text{in }H^6(E_{S^1};\mathbb Z/9).
 \tag{D.T36}\hypertarget{tag-025H}{}\label{maps:eq:D.T36}
\]
Its C9 restriction also vanishes. Formula \eqref{maps:eq:D.T38} and
injectivity of constants now give
\[
                  \langle Q_3(\alpha),[X]\rangle=0
                                   \quad\text{in }\mathbb Z/9.
 \tag{D.T39}\hypertarget{tag-025K}{}\label{maps:eq:D.T39}
\]
The coefficient-one identification proves $\mu(X)=0$. The spin-bordism
coefficient map then gives $\mathfrak p(X)=0$ and the zero marked
spin-bordism class.

\paragraph{The oriented surgery model.}
Let $f:S^2\to S^2$ have degree three and let
$\iota:S^2\hookrightarrow S^4$ be an equatorial embedding. The map
$x\mapsto(f(x),\iota(x))$ is an embedding representing three times
the positive first-factor generator. Its oriented rank-four normal
bundle has $w_2=0$, since $S^2\times S^4$ is spin and
$w_2(TS^2)=0$. Oriented rank-four bundles on $S^2$ are classified by
this class, so the normal bundle is trivial. Its framing is unique
up to homotopy because $\pi_2SO(4)=0$.
The framed index-three surgery trace is a spin cobordism. The attaching
map on $H_2$ is multiplication by three, giving
$H_2(W)=\mathbb Z/3$, $H_3(W)=0$, and $H_4(W)=\mathbb Z$.
From the other end its dual handle has index four; intersection of
the first-factor sphere with the second-factor sphere gives
$H_4(W)\to H_4(W,M_{3,0})$ equal to multiplication by three.
The two exact sequences therefore give
$H_2(M_{3,0})=H_3(M_{3,0})=\mathbb Z/3$ and $b_3=0$.
General position in real codimension four and van Kampen preserve
simple connectivity. The spin structure extends across the framed handle.
The mod-three class of the first factor extends over the trace since
the attaching sphere evaluates to zero; the relative extension is
unique because $\pi_3K(\mathbb Z/3,2)=0$.
The initial marked pair bounds $S^2\times D^5$ over $K(\mathbb Z/3,2)$.
Consequently $M_{3,0}$ has zero marked spin-bordism class.

Zhubr's marked recognition theorem for zero free third homology,
with the construction and uniqueness in \S4.1, now applies to $X$
and $M_{3,0}$
\cite[Theorem~3, p.~795; Theorem~5 and \S4.1, pp.~807,809--810]{manZhubr75}.
Both classifying maps induce the given isomorphism on $H_2$, both
have $b_3=0$, and their spin-bordism classes coincide. The resulting
oriented diffeomorphism carries the positive surgery generator to $s$.
This proves \eqref{maps:eq:D.T32} and \eqref{maps:eq:D.T33}.
\end{proof}
'''

receiver = statement.rstrip() + '\n\n' + proof
def identities(text):
    return {kind: re.findall(pattern, text) for kind, pattern in {
        'labels': r'\\label\{([^}]+)\}',
        'hypertargets': r'\\hypertarget\{([^}]+)\}',
        'tags': r'\\tag\{([^}]+)\}',
    }.items()}
oldids, newids = identities(oldstatement + oldproof), identities(receiver)
for kind in oldids:
    assert sorted(oldids[kind]) == sorted(newids[kind]), (kind, oldids[kind], newids[kind])
    assert len(newids[kind]) == len(set(newids[kind])), kind
assert receiver.count(r'\begin{proof}') == receiver.count(r'\end{proof}') == 1
assert r'\StatementRecord' not in receiver
target = LANE/'S6_SERIES_PUBLISH_III_02LF_receiving.tex'
assert sha256(target.read_bytes()).hexdigest() == '8720aef25b96b7a00e275be16f6c74718ae047e4bc1c39146d22f544f9f292e3'
with target.open('w') as stream:
    stream.write(receiver)
print('RECEIVER', target, 'LINES', len(receiver.splitlines()),
      'SHA256', sha256(receiver.encode()).hexdigest())
print('IDENTITIES', newids)
print('CANONICAL_SOURCE_UNCHANGED; EXACTLY_ONE_RECEIVING_PROOF; NO_HISTORICAL_RUN')
