# E6: the two finite poles of the chronological outside map

Working local continuation by fourfold. This supplies the two finite
pole charts requested for the E80 core seam. It retains the original
source parameters, the full \(M_6\) line, and the actual scalar
\(d(s,t)=8\lambda q_{\rm sel}(s,t)\). It does not close the full
period strip or assign a return. In particular the central cyclic
norm and the nonclosed-orbit wall of E78 remain unchanged.

## EP.1. The full two-step map before taking the central core

Use the first opposite-ruling chart \((h,\alpha,\beta)\) of E74.2.
Write
\[
 e=h-\alpha+1,\qquad f=\alpha^2-\alpha-\beta,\qquad
 k=e(e-1)-f=h^2+h-2h\alpha+\beta .
 \tag{EP.1}
\]
The first target is the actual resolved source chart
\[
 (z_1,w_1,x_1)=(-\alpha,e,f),\qquad
 s=h\alpha-\beta=he-k,\qquad 2t_{\rm base}=hf .
 \tag{EP.2}
\]
The full line coefficient \(\xi_1\) is the one in E75:
it includes the actual \(s\Delta r_6\) and the local
\(M_1^{\otimes6}\otimes\mathcal O(3C_{\rm old})\) frame.
Each following suspension is translation by \(-G\), and keeps
both \(s\) and \(t_{\rm base}\). Therefore its factor
\(d=8\lambda q_{\rm sel}(s,t_{\rm base})\) is the same function
at both source points.

On the common open set the next two source and line maps are
\[
 \begin{split}
 (z_2,w_2,x_2)&=(-e,-k/e,he),&
 \xi_2&=d\,e^{-3}\xi_1,\\
 (z_3,w_3,x_3)&=
 \left(k/e,-se/k-f/e,-fk/e^2\right),&
 \xi_3&=-d^2 k^{-3}\xi_1 .
 \end{split}
 \tag{EP.3}
\]
These follow by substituting the literal \(-G\) formula
\[
 (z,w,x)\longmapsto
 \left(-w,\ s/w+z-w+1,\ 2t_{\rm base}w/x\right)
\]
with its line coefficient \(dw^{-3}\). The apparent final
division by \(x\) cancels in (EP.3), using (EP.2).
Direct substitution gives
\[
 x_i-z_iw_i=s,\qquad
 x_i(w_i-z_i-1)=2t_{\rm base}\quad(i=1,2,3).
 \tag{EP.4}
\]
At \(\alpha=\beta=0\), \(e=h+1\), \(k=h(h+1)\), so the
last line coefficient is precisely E80's
\(-d^2/[h^3(h+1)^3]\). Its two poles have thus been retained
inside the full threefold map.

## EP.2. The \(h=0\) endpoint

Near \((h,\alpha,\beta)=(0,0,0)\), \(e\) is a unit. The first
map in (EP.3) is a holomorphic coordinate map with determinant
\(-1\). Its literal inverse, with target coordinates \((z,w,x)\),
is
\[
 e=-z,\qquad h=-x/z,\qquad
 \alpha=-x/z+z+1,\qquad
 \beta=h\alpha-(x-zw).
 \tag{EP.5}
\]
All denominators are units on this neighbourhood. The line inverse
is \(\xi_1=e^3d^{-1}\xi_2\). Its full complex differential is
block triangular, with source determinant \(-1\), line diagonal
factor \(de^{-3}\), and the retained off-diagonal derivative
\[
 d\log d-3\,d\log e .
 \tag{EP.6}
\]
Thus this preliminary arrow preserves the complex eight-dimensional
orientation and the actual physical line; its parameter/source
unit derivative has not been suppressed.

The remaining map is exactly the third primitive graph, centred
at \(w_2=x_2=0\), near \(z_2=-1\). Its full common Cox chart is
\[
 u^{(3)}=(1,-e),\qquad
 t^{(3)}=(-k/e,he),\qquad \Xi^{(3)}=\xi_2 .
 \tag{EP.7}
\]
The auxiliary weights are \((1,1,-1,-1,-3)\) on
\((u_0,u_1,t_0,t_1,\Xi)\). The common source functions are
\[
 s=u_0t_1-u_1t_0,\qquad
 2t_{\rm base}=t_1(u_0^2t_0-u_1-u_0).
 \tag{EP.8}
\]
In the opposite chart \(t_0=1\), put
\[
 h_3=x_2/w_2,\qquad A_3=w_2,\qquad B_3=z_2w_2.
 \tag{EP.9}
\]
The target resolved source map is literally
\[
 (z_3,w_3,x_3)=(-A_3,h_3-A_3+1,A_3^2-A_3-B_3),
 \qquad \xi_3=dA_3^{-3}\xi_2 .
 \tag{EP.10}
\]
The common-Cox line has weight minus three; the factor \(d\)
is applied after its chart change. Equations (EP.7)--(EP.10),
rather than the rational expression with denominator \(k\),
give the continuation at this pole.

## EP.3. The \(h=-1\) endpoint and its linked next centre

Near \((-1,0,0)\), use (EP.2) as source coordinates. This map
has determinant \(-1\) everywhere, and its inverse is
\[
 \alpha=-z_1,\qquad h=w_1-z_1-1,\qquad
 \beta=z_1^2+z_1-x_1 .
 \tag{EP.11}
\]
The second primitive graph therefore has the exact common Cox
presentation
\[
 u^{(2)}=(1,z_1),\qquad t^{(2)}=(e,f),\qquad
 \Xi^{(2)}=\xi_1 .
 \tag{EP.12}
\]
In its opposite chart set \(h_2=f/e\), \(A_2=e\),
\(B_2=z_1e\). Its source/line image is
\[
 (z_2,w_2,x_2)
   =(-A_2,h_2-A_2+1,A_2^2-A_2-B_2),\qquad
 \xi_2=dA_2^{-3}\xi_1 .
 \tag{EP.13}
\]
Along its new core \(A_2=B_2=0\), the next centre
\(w_2=x_2=0\) is exactly \(h_2=-1\). In the full chart
its equations are
\[
 h_2-A_2+1=0,\qquad A_2^2-A_2-B_2=0 .
 \tag{EP.14}
\]
The actual source map (EP.13) is invertible, with
\[
 A_2=-z_2,\qquad h_2=w_2-z_2-1,\qquad
 B_2=A_2^2-A_2-x_2 .
 \tag{EP.15}
\]
Hence the next graph is again the literal third graph with
common Cox coordinates \((1,z_2),(w_2,x_2)\) and coefficient
\(\xi_2\). On the overlap \(e\ne0\), (EP.12)--(EP.15) coincide
with (EP.7). The \(h_2=-1\) centre is the chronological
continuation of the same \(k/e=0\) equation. The two finite
poles are not two unrelated constant core identifications.

## EP.4. The second projective chart and its actual line frame

For either primitive graph write the opposite finite coordinates
as \((h_i,A_i,B_i)\). The complementary projective chart has
\[
 k_i=h_i^{-1},\qquad A=h_iA_i,\qquad B=h_iB_i,\qquad
 D_i=1+k_i-k_i^2A .
 \tag{EP.16}
\]
The actual target \(S_1=1\) chart, including its inverse, is
\[
 \begin{aligned}
 a&=k_i/D_i,& b&=D_i(-B-A+k_iA^2),& c&=-D_iA,\\
 E_i&=1-a-a^2c,&
 k_i&=a/E_i,& A&=-cE_i,& B&=(c+ac^2-b)E_i .
 \end{aligned}
 \tag{EP.17}
\]
Here \(D_iE_i=1\), and the maps preserve (EP.8).
They are the full E74.3 coordinate arrows, applied at the
specified chronological step.

The actual \(M_6\) endpoint frame is
\(a^{-6}b^{-3}\), while the target finite rational frame is
\((ab)^{-3}\). Consequently the *coefficient* arrow is
\[
 \xi_{\rm end}=a^3\xi_{\rm finite}
              =D_i^{-3}k_i^3\xi_{\rm finite}.
 \tag{EP.18}
\]
On the common Cox \(t_1=1\) chart its coefficient is
\(\xi_{t_1}=k_i^3\xi_{\rm finite}\). Thus the full actual
line map there is \(D_i^{-3}\xi_{t_1}\); the unit \(D_i^{-3}\)
cannot be removed from the Cartier arrow. The suspension
factor \(d\) is present in both projective charts. Equations
(EP.16)--(EP.18) supply the missing projective endpoint of
each finite graph, with the prescribed \(M_1\) divisor at \(G\).

## EP.5. Physical circle and finite faces

Since \(q_{\rm sel}\) is a unit on this unselected collision
neighbourhood and \(\lambda\ne0\) is fixed, the full \(d\)
has an analytic logarithm on the chosen bidisc after its
constant value is fixed. The associated equation
\(\Xi\Xi^\vee=q_{\rm sel}\) is carried by the reciprocal
line factor, including every \(d\), \(e\), and \(D_i\)
appearing above.

In the \(\Xi=1\) gauge, a primitive graph is
\(\mathbb C^4/\mu_3\), with
\[
 (u,t)\sim(\zeta_3u,\zeta_3^{-1}t),\qquad
 \delta_\phi(u,t)=(e^{i\phi/3}u,e^{-i\phi/3}t).
 \tag{EP.19}
\]
The actual line multiplication by \(d\) is
\((u,t)\mapsto(d^{1/3}u,d^{-1/3}t)\) modulo the displayed
group. Both original source functions (EP.8) remain fixed.
The branch change of \(d^{1/3}\) is exactly that finite
group action.

For each specified primitive chart, the finite norm faces are
the exact E76 products
\((S^3_u\times D^4_t)/\mu_3\) and
\((D^4_u\times S^3_t)/\mu_3\), with common
\((S^3_u\times S^3_t)/\mu_3\). Their physical line is
the charge-three line carried by (EP.18)--(EP.19).
The maps above identify the continuation of these faces
through the two finite poles. They retain both chronological
graph factors and their common centre. The number and
orientation of their unpaired full boundary components in
a compact period strip still requires the global strip
attachment; no such count is extracted from this chart list.

On the central core the retained E80 seam gives the exact
invariant norm relation
\[
 \|u\|\|t\|=
 |\kappa_d|\,\frac{1+|h|^2}{|h(h+1)|},
 \qquad \kappa_d^3=-d^2 .
 \tag{EP.20}
\]
Thus neither finite pole can be filled by extending a
constant-radius core identification. Their continuation
is the source/line graph atlas (EP.7)--(EP.18).

## EP.6. Both full faces in one common charged gauge

Equation (EP.20) compares the independently normalized actual
target and source gauges of E80. For the two faces of a *single*
common Cox ball, the first primitive suspension must also be
included. In its gauge \(\Xi=1\), the source coefficient is
\(u_0^3\), whereas the actual first target coefficient is
\(d\,t_0^{-3}\). Consequently the full outside map in that
same common gauge uses
\[
 \kappa_{\rm full}^3=-d^3,\qquad
 \kappa_{\rm full}=-d .
 \tag{EP.21}
\]
This is the specified root itself, with no additional branch
choice. The other two representatives are the already displayed
\(\mu_3\) action. Equivalently the actual first target charged
coordinates are \((d^{1/3}u,d^{-1/3}t)\); substitution in
(EP.20) gives exactly (EP.21).

The map also has a full normal formula. On this common charged
chart set
\[
 \begin{split}
 E&=t_1+t_0-u_0t_0^2,\\
 F&=u_0^2t_0-u_0-u_1,\\
 K&=t_1(t_1+t_0)-t_0^2(2u_0t_1-u_1t_0).
 \end{split}
 \tag{EP.22}
\]
These are the literal functions \(et_0,f/t_0,kt_0^2\).
In particular
\[
 K=t_1E-st_0^2,\qquad
 E^2-Et_0-K=t_0^3F,\qquad 2t_{\rm base}=t_1F .
 \tag{EP.23}
\]
The entire three-period source and line map, expressed in the
initial charged coordinates, is
\[
 \begin{split}
 u'_0&=-dt_0/K,&u'_1&=-d/E,\\
 t'_0&=(sE^2+t_0FK)/(dE),&
 t'_1&=FK^2/(dE^2).
 \end{split}
 \tag{EP.24}
\]
Its two original source functions (EP.8) are unchanged.
It is equivariant for the actual physical circle and the
existing finite quotient. Substituting \(u=0\) yields the
complete common-ball core arrow
\[
 u'=-d\,\frac{(t_0,t_1)}{t_1(t_0+t_1)},\qquad t'=0 .
 \tag{EP.25}
\]
At \(t_0=0\) with \(t_1\ne0\), \(E=t_1\), \(K=t_1^2\).
The map is regular there in the original source's
complementary projective chart. Its coefficient is
\(-d^3 E^{-3}\), including the first-period \(d\) and the
full \(D_i=E/t_1\) of (EP.18).
The divisors \(E=0\) and \(K=0\) are continued by the two
chronological graph atlases (EP.7)--(EP.18), not by omitting
their line poles.

The common charged canonical four-form is the one computed
from the actual source residue in E83. Each source translation
and logarithmic line map preserves that form. The derivative
of \(d(s,t_{\rm base})\) is retained: it is a source one-form
and wedges to zero with the complete source three-form.
Thus (EP.24) carries the same canonical determinant and
physical-line lift as its three actual constituent maps.

Here is a full-face separation estimate with that typed map.
Fix a closed sufficiently small source bidisc on which
\(d\) is a unit, and write \(d_{\min}=\inf|d|>0\).
Choose \(r_0>0\) with
\[
 r_0^2(\sqrt2+r_0^2)<d_{\min}.
 \tag{EP.26}
\]
On the target face \(\|t\|=r_0,\ \|u\|\le r_0\),
\[
 |E|\le r_0(\sqrt2+r_0^2),\qquad
 \|u'\|\ge |u'_1|
       \ge\frac{d_{\min}}{r_0(\sqrt2+r_0^2)}>r_0 .
 \tag{EP.27}
\]
The inequality is on the full common open set of (EP.24),
including all normal variables. On the central core the
sharper minimum is
\(2|d|/(1+\sqrt2)\) for \(\|u'\|\|t\|\).

This small-ball separation does not remove the ordinary
cyclic norm wall. Indeed on the whole product ball
\(\|u\|,\|t\|\le r_0\), (EP.8) gives
\[
 |2t_{\rm base}|\le \sqrt2\,r_0^2+r_0^4<|d|.
 \tag{EP.28}
\]
On the central wall E78 the actual equality is
\(|2t_{\rm base}|=|d|\), so that wall lies outside this
product ball. The compact finite-strip construction must
therefore carry the ordinary period region of E81--82
as well as these paired local faces. Equations
(EP.21)--(EP.28) supply their full gauge, normal map and
separation; they assign no additional unpaired boundary.
