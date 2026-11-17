# P3K.85. The actual reduced-II OS49 page and physical return

Complete mathematical reconstruction after the checkpoint19 restore.
The original RP.1--7 proof passed root and checks, and its nine-page PDF
passed direct all-page review. Historical source/PDF hashes are recorded
in the recovery ledger; no equality of reconstructed bytes is asserted.

Retain the K84 source and all actual root/Cartier/annular maps:
\[
y^2=x^3-3t^3(t-1)x+2t^4(t-1)(t-\tfrac12),\quad
G=(t^2,t^2),\quad\mathcal M=O(G-O),\quad Q=3G.
\tag{RP.1}
\]
The good IV-star cap at t0 has m=3k; the reduced-II cap at t1 has
h=6l+1, k,l>0. Keep full vectors n_A ell_0+d_A delta and
n_B gamma_B+d_B delta, with
\[
hn_A+mn_B=\epsilon=\pm1,\quad M=mh,\quad\chi=k(3l+1).
\tag{RP.2}
\]
Use the actual parameter lambda=r^M and actions
A_(A,r)=r^(hn_A)A_(A,0), A_(B,r)=r^(mn_B)A_(B,0), with their
literal powers B^(n_A),B^(n_B). The endpoint-to-initial ordinary
closing is f(t)=t^(hn_A)(t-1)^(mn_B). On the positive fan T1,
\[
(k_M,\ell_M)=(6kh,24k(3l+1)),\qquad A_M=3kl\pmod{28}.
\tag{RP.3}
\]
The smallest tuple (3,7,1,-2,0,0) has pair(42,96),class3. This
statement concerns the canonical full r-loop. All fixed delta
characters and both determinant signs are retained.

## RP.1. Literal contracting and outward cap phases

Let y_B be the coefficient of the actual contracting B period. On
q_i=z_i^(r_i), with a_i=arg z_i/(2pi), the plus-log ordinary-to-cap
arrow gives y_cap=y_B+n_i a_i. The actual root cut is
(a_i,y_cap)->(a_i+1/r_i,y_cap+n_i/r_i). Thus u_B=r_i y_cap
=r_i y_B+n_i alpha_i. The filled meridian is
r_i alpha_i-n_i gamma_B. Put gamma_out=-y_B and u_out=-u_B;
then u_out=r_i gamma_out-n_i alpha_i and the root cut shifts
u_out by -n_i. This is the exact coordinate arrow to K28's cap.
The positive weighted Hopf angle is therefore
\[
                              \beta=-\epsilon y_B.
\tag{RP.4}
\]
No inward cap formula is imported with the outward gamma unchanged.

Set T=t/(t-1). The two root sites are T0 (order m,n_A) and
T infinity (order h,n_B). Write alpha=arg T/(2pi). The exact
ordinary phases are
phi1=epsilon(m gamma_out-n_A alpha),
phi2=epsilon(h gamma_out+n_B alpha).
The integer phase map has determinant epsilon, and m phi2-h phi1=alpha.
Choose unique positive radii r1²+r2²=1 with r2^m/r1^h=|T|.
Then z_j=r_j exp(2pi i phi_j) gives T=z2^m/z1^h.

At infinity q_infty=z^h let R²+|z|²R^(2m/h)=1. The actual
extending map is
\[
(z,u_\infty)\longmapsto
 (zR^{m/h}e^{2\pi i\epsilon m u_\infty/h},
                         R e^{2\pi i\epsilon u_\infty}).
\tag{RP.5}
\]
At zero q0=z^m use R²+|z|²R^(2h/m)=1 and
\[
(z,u_0)\longmapsto
 (R e^{2\pi i\epsilon u_0},
                  zR^{h/m}e^{2\pi i\epsilon h u_0/m}).
\tag{RP.6}
\]
The root cuts change the phases by the integers
(epsilon n_A,-epsilon n_B) and (-epsilon n_A,epsilon n_B),
respectively, using hn_A+mn_B=epsilon. Both maps descend through
the ACTUAL source/line root quotient. Their inverse first recovers R
from the nonzero coordinate, then an argument lift, and then z;
different lifts differ by precisely the root cut. The radial derivative
is positive. Substitution verifies both ordinary overlaps exactly.
The unit changes from q_i to T or1/T have their specified analytic
roots and are carried by the same actual cap maps.

## RP.2. Exact page, sheet-zero map and actual line

For regular tau distinct from0,1,infinity the complex page is
\[
\mathcal C:\ \eta^m-\tau\xi^h=1,\qquad
T=\tau+\xi^{-h}.
\tag{RP.7}
\]
Its weighted radial map is (xi,eta)->(rho^m xi,rho^h eta),
where rho^(2m)|xi|²+rho^(2h)|eta|²=1. It is the positive-argument
page of z2^m-tau z1^h, with the complex orientation. Its map has
degree M. There are h points over T0 of index m, m over infinity
of index h, and one binding point of index M. The last follows
from gcd(m,h)=1 and the expansion xi~c w^-m,eta~d w^-h. Thus
g(Cbar)=(m-1)(h-1)/2. The derivatives of the defining equation cannot
both vanish on its level1.

The sheet-zero map is the actual inverse of RP.5--6 followed by the
specified root source map and Cartier graph. A stabilizer of a lifted
sheet has nk+rh=0, hence (k,h)=(rj,-nj); its action is A^(rj)B^(-nj)=1
by the literal norm. Thus no residual finite quotient remains. The
full finite characters are the prescribed ones, not replaced by an
abstract sectioned base change. At IV-star use the actual corrected
root line of F26/F29; at II use K84's exact graph equality beta*N=pi*M.
The II graph coordinates tau'=z^j u_j carry the ratio
(u_j+z^(l-j))/u_j, and final (u_l+1)/u_l; equal exceptional
coefficients cancel. Consequently the sheet map pulls precisely
N=O(G_page-O), retaining every I2 component degree.

The relative source torsor is trivialized with its exact binding collar.
On a punctured page, the smooth Lie sheaf is fine and the exponential
obstruction is H2(C,partial C;j_*Lambda). The two-sector cancellation
and compact-support duality identify it with monodromy coinvariants.
A lifted II root meridian has elliptic monodromy B_ell^h=B_ell,
and B_ell-I=[[0,1],[-1,-1]] has determinant1. Thus these integral
coinvariants vanish. Component terms are finite skyscraper sheaves
with no H1; they remain in the local diagrams. The actual torsor
translation is chosen relative to the specified binding collar.
Use the rigidified fibrewise Picard/Poincare Hom isomorphism to carry
the line under these translations. Its remaining base line and integral
whole-fibre terms have zero square and zero pairing with N. The
retained local component and finite-character maps fix all other terms.

The elliptic page has M unchanged I2 fibres, m reduced-II fibres,
and h good IV-star roots. Hence its Euler characteristic is
2M+2m=12chi, giving chi=m(h+1)/6=k(3l+1). G and O were disjoint
on the original source and on the good root. At each of the m II
points the exact equality tau'(G')=-z^l gives intersection l.
Thus G_page.O=ml and
\[
N^2=-2\chi-2ml=-2kh,\quad
\sigma(S_{page})=-8\chi,\quad p_1(TS_{page})=-24\chi.
\tag{RP.8}
\]
These are the actual section-line numbers; the nonzero I2 component
degrees have not been replaced by a whole-fibre height.

## RP.3. Full origin square and its actual forward arrow

In the original q=1/t coordinate keep the complete periods
\[
u=(2s,s)^t+U(q),\quad\gamma_B=(-3s,-s+Mv)^t+C(q),
\quad H=-u-\gamma_B,\quad K=3u+2\gamma_B=\mathcal D+(s+2Mv)\delta,
\tag{RP.9}
\]
where Dcal=3U+2C,s=logq/(2pi i),v=logr/(2pi i). The valuation
matrix [[2,-3],[1,-1]] has determinant1. With the actual unit
(1-q)^(mn_B) retained on both ordinary/cusp origins, their basic terms are
\[
o=-\epsilon s\mathcal D/(2M)-\epsilon s^2\delta/(4M)-\epsilon sv\delta,
\qquad\sigma=\epsilon v\mathcal D+\epsilon Mv(v-1)\delta.
\tag{RP.10}
\]
These are PLUS products: xi_ord=zeta+o,xi_cusp=zeta+sigma.
Therefore cusp-to-ordinary is o-sigma. If c=-epsilon s delta is
the ordinary closing log, then o(v+1)-o(v)=c and
sigma(v+1)-sigma(v)=c+epsilon K. The actual bounded forward endpoint
is K^(-epsilon), and its full angular path is
\[
(Z,V)\mapsto(U_K^{-\epsilon\theta}Z,
 (W_K\lambda_0^2)^{-\epsilon\theta}
                      e^{-2\pi i\epsilon M\theta(\theta-1)}V).
\tag{RP.11}
\]
Every unit uses its prescribed logarithm. The whole angular difference
under s->s+2M retains its integral boundary gauge; the auxiliary source
root does not change the positive r parameter. The quadratic physical
factor is carried on the entire source, line and both cap quotients.
The old sigma-o arrow with a forward +epsilon K is the inverse
direction and is preserved only in the historical attempt.

## RP.4. Mixed boundary map and Hopf orientation

Let (x,y_B) be point angles of (u,gamma_B), and (h0,kappa) those of(H,K).
The literal torus maps are
\[
\binom{h_0}{\kappa}=\begin{pmatrix}2&-3\\1&-1\end{pmatrix}
\binom{x}{y_B},\qquad
\binom{x}{y_B}=\begin{pmatrix}-1&3\\-1&2\end{pmatrix}
\binom{h_0}{\kappa}.
\tag{RP.12}
\]
The incoming actual compression graph kappa=g(h0,w) moves under the
positive parameter as kappa=g-epsilon theta, by RP.11. Combining
beta=-epsilon y_B with theta=-epsilon(kappa-g) gives
\[
\binom{h_0}{\theta}=\begin{pmatrix}2&3\epsilon\\-\epsilon&-1\end{pmatrix}
\binom{x}{\beta}+\binom0{\epsilon g},\qquad\det=1.
\tag{RP.13}
\]
The other source cycle w is retained. The source imaginary periods of
u and H have positive leading lengths2 Im s and Im s, so the complex
source orientations agree on the chosen collar. Thus the actual page
boundary maps to E_H x S1_theta with degree+1 for both signs. With
partial W=F-E_H, the glued trace has partial X=F x S1_theta.
In the fixed normal chart the circle-first orientation and the actual
Hopf coordinate below give the positive normal meridian. This is the
line U=M*, not the physical line M; K68's exact dual arrow is retained.

## RP.5. Actual Cox frame, full moduli homotopy and normal square

The positive-fan charts are
\[
(A,B,Z)=(q/V,V/Z,Z),\quad(A',B',Z')=(ZA,ZB,Z^{-1}),\quad q=ZAB.
\]
They have weights(-1,+1,0). Write y=AB,b=(|B|²-|A|²)/2. The
quotient coordinates are (y,b). Positive K decreases log|V|, so its
height chi_K has derivative (chi_K)_b<0. Retain that reflection in
both endpoint references. The global quaternion is
\[
q_H=(1+jZ)(A+j\overline B)=(Z^{-1}+j)(A'+j\overline {B'}).
\tag{RP.14}
\]
Physical delta is right multiplication by exp(-i phi). At Z0 the
Hopf coordinate q_H i bar q_H is
\(-2b i+2\operatorname{Im}(y)j-2\operatorname{Re}(y)k\).
Its determinant relative to(Re y,Im y,b) is-8. The circle-first
quotient determinant at(A,B)=(1,0) is-1. Together these give the
actual positive normal Hopf orientation. The raw initial comparison
in (Re y,Im y,-b) is triangular with last entry -(chi_K)_b>0;
its source shears and positive diagonal contract explicitly.
For the signed beta coordinate apply T_(-epsilon)=diag(1,1,-epsilon)
to BOTH initial references. Its residual comparison is the same
positive triangular matrix; conjugation uses (-epsilon)T_(-epsilon)
in SO3 and adds no free framing term.

For a bounded complex torus multiplier (Z,V)->(aZ,b1 V), retain
the exact q-preserving chart action (Z,A,B)->(aZ,b1^-1 A,(b1/a)B).
The quaternion identity is stated for its UNITARY phases: put
p=b1^-1,q1=b1/a and choose L²=pq1,R²=p/q1,LR=p along the actual
interval. Then q_H->L q_H R and eta->L eta bar L. The full positive
moduli are carried by the literal homotopy
\[
a_t=(a/|a|)|a|^t,\quad b_t=(b_1/|b_1|)|b_1|^t,\qquad
(Z,A,B)\mapsto(a_tZ,b_t^{-1}A,(b_t/a_t)B),\quad0\le t\le1.
\tag{RP.15}
\]
It preserves q and both chart transitions and is used at BOTH normal
references. At t0 the quaternion equality is exact. Higher terms of
the q-units have zero normal linear part because q=ZAB is quadratic
in the normal directions. The closed rotation is constant along F
and extends over its D3, with its actual Spin endpoint retained.

Take the exact regular binding coordinate
q_b=(T-tau)(T/tau)^(-epsilon h n_A), derivative1 at tau. Its full
phase, from the actual polynomial page, is alpha_b=phi-M beta.
RP.13 gives beta=2theta+epsilon(h0-2g), so
\[
\alpha_b=\phi-2M\theta-\epsilon M(h_0-2g).
\tag{RP.16}
\]
The source term is circle-valued and retained. The actual quotient
normal map from the collar tangent(cos alpha,sin alpha,rho,0),rho>0,
sends (v_q,v_r,v_eta) to(v_q-v_r(cos alpha,sin alpha)/rho,v_eta).
Projecting the two Cartesian parameter vectors gives
\[
G(\alpha,\theta)=\begin{pmatrix}
-\sin\alpha&\cos\theta\cos\alpha&\sin\theta\cos\alpha\\
\cos\alpha&\cos\theta\sin\alpha&\sin\theta\sin\alpha\\
0&\sin\theta&-\cos\theta
\end{pmatrix}\in SO(3).
\tag{RP.17}
\]
The same signed/reflected frames are used at both ends. An actual
frame on the compression transported by the K flow differs from the
Cox frame by R(p), independent of theta; its S2 boundary map extends
over D3. The compression is a solid torus minus a ball, and its normal
three-bundle has zero w2 in the stably parallelizable actual orbit S5,
so such a frame exists. The full clutch factors exactly as
\[
[R(p)^{-1}R_z(-\epsilon M(h_0-2g))]
       [R_z(\phi-2M\theta)G(0,\theta)].\tag{RP.18}
\]
The first factor comes from the actual source T2, the second from
the parameter circle. Expanding the Maurer--Cartan cubic of their
product gives the sum of factor cubics plus an exact form. Each
factor cubic vanishes by dimension. With the carried collar connection,
the actual normal Pontryagin pairing is therefore0. No lower-degree
normal data are discarded.

## RP.6. The full component line, regular bands and both cap markings

The actual line subfan has rays (j,ceil(j/2),1), with source component
degrees(-1,+1). The strict contraction supplies M ordered norm shells.
After the first zero, the exact positive-iterate height defects prevent
reentry, so these shells embed. The radial annular comparison is
v->c(q)^(F(s)-s)v with F(s+1)=F(s)+1. Its positive multiplier is
periodic, so it commutes with the original contracting lift and delta,
and fixes the source/base coordinates. Thus it carries the actual
circle line, including the root characters, into the compact page.

The graph-normal pushoff is chosen in those same base-fixed annular
and binding charts. Outside the projected regular bands its radial
homotopy avoids the entire compression. In each band the exact boundary
equation is rho=-eta0 cot alpha with sin alpha>0, cos alpha<=0. The
three boundary arcs are slightly larger than the finite-collar
intersections, with disjoint gaps. The inner semicircle includes into
its half-disc by a homotopy equivalence. After the source-circle product,
the relative H2 of each band vanishes; restriction is injective. Hence
the normal meridian line equals the carried page line on the entire
comparison, with every nonzero I2 degree retained.

The fixed d_A,d_B terms are actual source-trivial finite characters.
Their full sheet products are one. Their compact extensions differ
only by an integral fibre/base class, whose square and pairing with
N vanish. This proves the same relative square N² in RP.8 for every
retained character, rather than deleting its boundary gauge.

The incoming marked basis is (u,gamma_B)=(2H+K,-3H-K), determinant1.
The compression cap is (D2_w x S1_H) x S1_K; its H2 injects into
H2(T3), and the actual boundary line is flat, so its line class is0.
The regular cap T2_(u,w) x D2_gamma has zero line class and signature.
They kill different primitive cycles; no identification of the caps
is asserted. Novikov additivity and the actual line restrictions give
the same tangent Pontryagin pairing and b²=4N² despite all odd gauges.

## RP.7. Exact physical/Jin arrow and final numbers

With U=M* the positive Hopf meridian has fibre integral+1 and the
actual page restriction b_U=-2c1(N). Thus b_U²=-8kh, while
p1(TXbar)=-24chi and p1(normal)=0. The sphere-bundle pushforward is
\[
(k_U,\ell_U)=((p_1(\nu)+3b_U^2)/4, p_1(T\bar X)+p_1(\nu))
                  =(-6kh,-24\chi).
\tag{RP.19}
\]
K68's actual Hermitian dual/spinor map Q(a,b)=(bar b,-bar a) sends
U to the physical line M and reverses both characteristic integrals.
Its piecewise gluing gives lambda_M(F)=-Sigma(F^-1)=Sigma(F), with F
the actual forward map RP.11. Hence the physical pair is
\[
(k_M,\ell_M)=(6kh,24\chi),\qquad
A_M=(4k_M-\ell_M)/24=kh-\chi=3kl.
\tag{RP.20}
\]
Both arrow reversals RP.4 and RP.11 were needed; changing just one
would falsely give determinant-1. For the old one-cap h1,l0 case the
same maps give the retained physical pair(2m,8m), not its negative.
This supports K76/K77 through the corrected actual local maps.
