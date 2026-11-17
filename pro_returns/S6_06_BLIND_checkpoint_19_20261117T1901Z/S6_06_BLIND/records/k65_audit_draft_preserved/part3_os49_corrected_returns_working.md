# P3K.65. The two actual OS49 fan returns

Audit draft, 17 November 2026. This proof retains the component line,
both norm signs, every fixed delta character, and the actual shorter
parameter endpoint. Its local maps replace the incomplete outer-line
step of P3K.17; it uses neither that equality nor a universal fan
recurrence. The earlier assertions and their correction notices remain
in the record.

## Statement

Let the source and marked section be
\[
 y^2=x^3-3t^3(t-1)x+2t^4(t-1)(t-\tfrac12),\qquad
 G=(t^2,t^2),\qquad M=\mathcal O(G-O).
\]
Use the actual suspension over \(-3G\), with target-point
linearization divisor the identity component \(C_0\) of the
\(I_2\) fibre at \(q=1/t=0\). At the \(IV^*\) fibre use the
cap of order \(m=3k\), \(k>0\), and invariant vector
\(\ell=n(e_\gamma-e_u)+d\delta\), where \(n=\pm1\) and
\(d\in\mathbb Z\). Retain the original type-II line-complement
quotient. Denote by \(\mathcal T_-\) the negative-diagonal fan
of P3F.26 and by \(\mathcal T_+\) the positive-diagonal fan of
P3F.31. For the actual positive parameter loops the oriented
clutched-sphere classes are
\[
\begin{array}{c|c|c|c}
 \text{parameter}&\text{scalar}&\mathcal T_-&\mathcal T_+\\ \hline
 r&\lambda=r^{3k}&-3k&0\\
 w&\lambda=w^k,\quad w=r^3&-k&0
\end{array}\qquad\text{in }\Theta_7=\mathbb Z/28.       \tag{OR65.1}
\]
The positive fan has Jin characteristic integer zero in both rows.
The actual native C2 free pairs on the negative fan are respectively
\((-3k,3k)\) and \((-k,k)\). In particular the positive scalar
loop \(\lambda=w\), with \(k=1\), on \(\mathcal T_-\) has class
\(27\), a generator. As \(k\) varies, the shorter negative-fan
families realize every residue modulo 28.

The proof assigns the negative fan's sphere class by the actual
relative diffeomorphism and its oriented central generator. It does
not identify an integer characteristic number with a chosen lift of
that residue.

## OR65.1. Source, component line, cap and forward parameter arrow

The source discriminant factor and section substitution are
\[
 [t^3(t-1)]^3-[t^4(t-1)(t-\tfrac12)]^2
       =-\tfrac14t^8(t-1)^2,
\]
so the marked fibres are \(IV^*,II,I_2\) at \(0,1,\infty\).
On the cubic root \(t=z^3,x=z^4X,y=z^6Y\), the good central
curve is \(Y^2=X^3+1\), and \(G\) specializes to \((0,1)\),
of exact order three. At infinity the minimal coordinates of G
are \((1,q)\), meeting component one after resolving the node.
The section is disjoint from O. The line of target-point
linearizations of translation by \(-3G\) has divisor class
\[
 G-O-(-2G)+(-3G)\sim C_0.
\]
Indeed its component degrees at \(I_2\) are \((-2,2)\), those of
\(C_0\); all degrees cancel at \(IV^*\); subtracting \(C_0\)
therefore leaves an integral fibre class, and intersection with O
is zero. We retain that actual section and its scalar multiplier,
not a whole-fibre substitute.

On the nonzero line over the Tate chain the source and suspension
periods have literal valuation vectors \((2,1)\), \((-3,-1)\):
\[
 u=(2s,s)^t+U(q),\qquad
 \gamma=(-3s,-s+mv)^t+C(q),
 \quad s=\frac{\log q}{2\pi i},\quad
 v=\frac{\log r}{2\pi i}.                            \tag{OR65.2}
\]
All components of U and C are the retained bounded holomorphic
units' logarithms. Their units, rather than their logarithms
alone, are the ordinary torus maps. Put
\[
 H=-u-\gamma=(s,-mv)^t-U-C,\qquad
 K=3u+2\gamma=(0,s+2mv)^t+D,\quad D=3U+2C.
\]
The integral change has determinant one. In the physical characters
\((Z,V)\) these primitive periods are
\[
 h:(Z,V,q)\mapsto(\kappa q Z,\alpha V,q),\qquad
 B:(Z,V,q)\mapsto(gZ,\eta qV,q).                     \tag{OR65.3}
\]
For one positive r-loop their full unit windings are
\[
  (\operatorname{wind}\kappa,\operatorname{wind}\alpha,
    \operatorname{wind}g,\operatorname{wind}\eta)
                         =(0,-m,0,2m).              \tag{OR65.4}
\]
Here the physical circle is the positive phase of V.

The actual good-root cap has linear part \(A^3=1\), with
\(A\ell=\ell\), and affine action
\(z\mapsto Az+\ell/m\). Its j-th power has gamma displacement
\(jn/m\). For \(0<j<m\) this is nonintegral, so the action is
free and no physical delta rotation compensates it. On its source
root \(t=s_0^m\) the actual ordinary-to-cap map is
\[
 \Phi_r(z,s_0)=z+\frac{\log s_0}{2\pi i}\Pi_r(s_0)\ell.
                                                               \tag{OR65.5}
\]
Changing the logarithm branch adds an integral period; the root
deck adds exactly the affine displacement. The fixed character
\(\exp(2\pi i d/m)\) is retained. The cap action in the physical
line character is \(A_r=r^nA_0\).

The one-r-turn endpoint-to-initial ordinary closing is multiplication
by \(t^n=q^{-n}\), with the cap comparison dictated by (OR65.5).
The forward parameter arrow is consequently \(q^n\). Reindex by
the actual K-period \(B^{-n}\) to return a chosen toric cell to
its initial representative. The resulting bounded forward arrow is
\[
 E_r(Z,V,q)=(g(q,r)^{-n}Z,\eta(q,r)^{-n}V,q).          \tag{OR65.6}
\]
This equality retains the period and the forward direction for
each sign of n. The type-II and finite-cap maps are untouched
outside the cusp neighbourhood. The independent integral topology
of P3F.26/P3F.29 gives \(\pi_1=0\) and integral sphere homology
for these signs: the four actual transgression maps are
multiplication by n after the specialization indices
\((m,k,k,m)\). Both small resolutions have the same topology,
because their common blowup adds one primitive integral generator
in degrees two and four and preserves the fundamental group.
Thus these are actual smooth six-sphere families.

## OR65.2. The independent positive-fan index

We record why the positive-fan input does not use the claimed
equality in P3K.17. On the source Tate chain the actual line graph
is \(h_j=\lceil j/2\rceil\), with \(h_{j+2}=h_j+1\).
The fibre-coordinate transition gives component degrees
\(-h_{j-1}-h_{j+1}+2h_j=(-1,+1)\). Its alternating edges
\((1,1)\), \((1,0)\) lie in the positive-diagonal unit-square fan.
Projection to the source chain and quotient by u therefore give a
literal toric open embedding of \(M^\times\), through both nodes.
The suspension's height defects are
\[
 h_j-1-h_{j-3}=0\ (j\text{ even}),\quad1\ (j\text{ odd}),
\]
and its N-th positive iterate has defect
\(\lfloor N/2\rfloor\) or \(\lceil N/2\rceil\), respectively.
A point leaving this line-complement open set at a zero cannot
re-enter through a later positive translate.

Choose a smooth Hermitian metric, fibrewise flat on the regular
cusp annulus, and a scalar small enough that the actual lift has
operator norm at most \(c<1\). Choose m shell radii with
\(R_1<\cdots<R_m\) and \(cR_m<R_1\). The preceding iterate
formula and this strict norm inequality prove that the shells
embed disjointly in the completed quotient. Their physical-circle
quotients are embedded copies of the full source \(I_2\)
neighbourhood, carrying the actual line M and missing the fixed
sphere.

On the regular annulus the lift's norm multiplier c(q) is constant
on each elliptic fibre: the logarithm of the ratio of its flat
metrics is harmonic on that compact fibre. The exact lift of a
circle reparametrization \(F_q(t+1)=F_q(t)+1\), with
\(t=\log\|V\|/\log c(q)\), is
\[
                  V\mapsto c(q)^{F_q(t)-t}V.
\]
It preserves the source and base coordinates, commutes with the
contracting lift, and carries the circle line. This glues the m
shells to the m sheets of the actual regular-binding page of the
weighted Hopf base of weights \((1,m)\). At the type-II fibres
use the original line-complement map; at the order-m cap use the
stated good-root map. The fixed d-character supplies only the
explicit scalar transition \(\exp(2\pi i d/m)\) on each sheet;
its product is \(\exp(2\pi i d)=1\). It therefore adds a base
line, whose restriction to the base page is topologically trivial.
This constructs a page V carrying M through all source components.

The source cap of this page has m fibres of type II and m of type
\(I_2\). Its two sections remain disjoint: the degree-3 root
already separates them, and the further degree-k cover branches
only at its smooth good-reduction fibre and the regular binding.
Thus
\[
 \chi(\mathcal O)=k,\quad \sigma=-8k,\quad
 M_{\rm rel}^2=-2k,\quad p_{\rm rel}=-24k.           \tag{OR65.7}
\]

For completeness the meridian-line comparison uses the actual
regular bands. The fixed-edge charts have normals
\((A,B)=(q/V,V/Z)\), with second chart
\((A',B')=(ZA,ZB)\); their weights are \((-1,+1)\).
The real compression of P3K.6 lies over \(q\in[0,\epsilon]\).
The page misses its fixed end, so all remaining intersections
project to a compact regular interval. The normal pushoff of its
unchanged binding collar is
\[
 q-\epsilon=(\rho+i\eta_0)e^{i\alpha(\gamma)},\quad
 \rho\ge0,\quad \eta_0>0.
\]
Its intersection with the real compression requires
\(\rho=-\eta_0\cot\alpha\) and
\(q-\epsilon=-\eta_0/\sin\alpha\), hence occurs only on m
proper boundary arcs. Enlarge their regular lifts to disjoint
half-disc bands. Each pair is
\((T^2\times D_i,T^2\times A_i)\), where the inner semicircle
\(A_i\hookrightarrow D_i\) is a homotopy equivalence. Its
relative \(H^2\) is zero. Outside these bands the exact radial
graph homotopy reaches the original page pushoff without meeting
the trace. Excision and restriction injectivity therefore identify
the graph-normal meridian line with M on the entire page.

The incoming cycle map is exactly
\[
 (u,\gamma)=(2H+K,-3H-K),\qquad
 \det\begin{pmatrix}2&-3\\1&-1\end{pmatrix}=1.
\]
The compression cap kills the primitive vanishing cycle \(w_0\);
the regular elliptic cap kills gamma. Their closed difference is
\(S^1_u\times S^3\), with zero signature. The cap's line class
is zero because its restriction to the boundary is zero and the
restriction map on \(H^2\) is injective. A boundary gauge changes
the glued class by \(d\chi\wedge\alpha_0\); its square and its
product with M vanish. The actual sphere-bundle bordism of P3K.7
therefore has \(b^2=-8k\), \(p_1(T\bar X)=-24k\), and
\[
              A_+=\frac{3(-8k)-(-24k)}{24}=0.        \tag{OR65.8}
\]
Both norm signs use their actual positive parameter arrow. The
extending origins on \(q=Q^{2m}\) are
\[
 \sigma=nvD+nmv(v-1)\delta,\qquad
 o=-\frac{nsD}{2m}-\frac{ns^2}{4m}\delta-nsv\delta.
\]
Their difference changes by
\(n\theta K+nm\theta(\theta-1)\delta\); the second term has
zero endpoint values. The signed page/cycle map retains the two
norm signs, and the computed integer is zero in either orientation.
P3F.22's actual Hopf-lift transfer gives positive-fan sphere class
zero. No negative-fan assertion enters this computation.

## OR65.3. The actual closed native C2 product

On a cut r-circle use holomorphic-in-q, smooth-in-parameter
logarithms of g and eta. Let \(\chi\) be zero and one on the
initial and terminal collars. Put
\[
 C_\tau(Z,V,q)=(A_\tau Z,D_\tau V,q),\qquad
 A_\tau=e^{n\chi\log g},\quad D_\tau=e^{n\chi\log\eta}.
                                                               \tag{OR65.9}
\]
It has the inverse obtained by negating the exponents, commutes
with both periods and delta, and satisfies
\(C_{\rm end}E_r=C_{\rm start}=1\) on whole collars, with all
derivatives. It acts on the two vertices as
\[
 (a,b,c)\mapsto((AD)^{-1}a,Ab,Dc),\qquad
 (u_0,v_0,w_0)\mapsto(ADu_0,D^{-1}v_0,A^{-1}w_0).
\]
The complete six-chart transitions are
\[
\begin{array}{c|ccc}
 &u_0&v_0&w_0\\ \hline
 C_0&\kappa\alpha bc&\alpha^{-1}ab&\kappa^{-1}b^{-1}\\
 C_1&g\eta bc&\eta^{-1}c^{-1}&g^{-1}ac\\
 C_2&a^{-1}&ab&ac.
\end{array}                                                   \tag{OR65.10}
\]
Substitution gives the same three factors on every row. Thus all
full unit coefficients, their windings (OR65.4), the physical
weights and the finite-cap closing remain the actual ones. In
particular C2 is a literal closed native star
\(z'=z^{-1},\ c'_i=zc_i\), with first coordinates \((a,b,c)\).
This asserts a product on that single star, not a simultaneous
delta-equivariant product of the three-curve plumbing.

Define its doubled product as its actual pullback. On the second
sheet use
\[
 C^{(2)}_{j+\tau}=C_\tau E_{r(\tau)}^{-j},\qquad j=0,1.
                                                               \tag{OR65.11}
\]
At the middle seam both maps equal \(E^{-1}\); at the final seam
the map cancels the doubled forward arrow after \(B^{-2n}\).
The complete cap overlap (OR65.5) is pulled back at the same time.
A connection on the actual compact family with this prescribed
native boundary product is obtained by extending its velocity
from a collar with a cutoff and joining it to an arbitrary global
connection in the affine space of connections. On the double
cover use the literal pullback connection. Its relative return
is the square of the single native return.

## OR65.4. An ordinary doubled product and its actual trace degrees

For the doubled closed charts set
\[
       t_0=2m,\qquad (l_0,l_1,l_2)=(6m,0,4m).       \tag{OR65.12}
\]
At the second vertex use \((u_0,\eta v_0,\kappa w_0)\), with
the same initial constants in the reference chart. The three
normal matrices become
\[
 D_0=\operatorname{diag}(\eta/\alpha,\kappa\alpha),\quad
 D_1=\operatorname{diag}(\kappa/g,g\eta),\quad
 D_2=\operatorname{diag}(\eta,\kappa).
\]
Their determinant winding is \(2t_0\); their first diagonal
windings are the \(l_i\) in (OR65.12). For each full based diagonal
entry subtract its displayed angular winding. The remaining
unit has a based periodic logarithm, retained below.

The explicit based quaternion contraction is
\[
 H_d(s_0,\theta)=
 (\sin\vartheta(s_0)e^{id\theta}+j\cos\vartheta(s_0))
 (\sin\vartheta(s_0)+j\cos\vartheta(s_0))^{-1},
\]
where \(\vartheta\) is constant at 0 and \(\pi/2\) near its
ends. It is periodic and based in theta. For
\(Q=n_0+j\bar n_1\), use
\[
                    Q\mapsto H_{t_0}QH_{l_i-t_0}.   \tag{OR65.13}
\]
At the second radial end its two complex factors have windings
\((l_i,2t_0-l_i)\), exactly those of \(D_{i,*}^{-1}D_i\).
Multiply by the exponential of each retained zero-winding unit
logarithm, with radial cutoff zero and one at the two ends.
The resulting map \(\mathcal K_i\) satisfies
\[
 \mathcal K_i(0,\theta)=1,\qquad
 zD_{i,*}\mathcal K_i(1,\theta)=zD_i.
\]
The three curve interiors are disjoint, so these actual tube maps
glue to the two vertex products. For nonlinear germs conjugate by
\((z,n)\mapsto(z,\tau n)\), which extends at \(\tau=0\)
to its invertible normal derivative, and integrate the cutoff
velocity to restore the full germ. Carry the rounded boundary by
the same isotopy. This constructs a based periodic ordinary
plumbing product, with all unit maps and its boundary specified.
It is not required to intertwine the physical circle.

In that product the tangent weights and normal differences are
\[
                    w=(0,1,-1),\qquad d=(-2,-1,-1).
\]
The actual circle action on the normal quaternion is
\[
 Q\mapsto(H_{t_0}e^{-iw_i\phi/2}H_{t_0}^{-1})Q
       (H_{l_i-t_0}^{-1}e^{id_i\phi/2}H_{l_i-t_0}).
                                                               \tag{OR65.14}
\]
The retained unit exponentials conjugate this formula and give a
based homotopy to it, with the metric transported. Let
\(U=\cos\chi+j\sin\chi\), \(E_i=e^{iw_i\phi/2}\). At the
normal section \(q_H=1\) the circle trace is literally
\[
 E_i^{-1}UE_i H_{t_0}E_i^{-1}H_{t_0}^{-1}U^{-1}
              H_{l_i-t_0}^{-1}e^{id_i\phi/2}H_{l_i-t_0}.
                                                               \tag{OR65.15}
\]
Direct differentiation at the inverse images of \(-i\) gives
\(\deg(H_diH_d^{-1})=-d\),
\(\deg(H_d^{-1}iH_d)=d\), in the path-parameter orientation.
The quaternion volume gives degree ce for an axis of degree e
and angle \(c\phi/2\). The Maurer product boundary terms vanish
on the radial ends and constant central-sign angle ends; the
parameter faces cancel. Therefore the normal-meridian and closed
stable-derivative degrees are
\[
 I_i=t_0w_i+d_i(l_i-t_0),\qquad
 W_i=t_0w_i-d_i(l_i-t_0).                              \tag{OR65.16}
\]
For the latter formula a left quaternion factor contributes its
degree and a right factor its negative. The base rotation has
only the phi variable; its Spin endpoint and the normal endpoint
are both \((-1)^{w_i}\), so their product is one. The vertex
caps are actual parameter-independent paths in the vertex links,
interpolating squared moduli and phases; their traces factor
through dimension two. They contribute no additional meridian
or third derivative class.

We recall the integral groups which make this a computation of
the actual return. The union of the three spheres has two vertices,
six edges and six faces, with
\[
 D_1=\begin{pmatrix}-1&-1&-1&-1&-1&-1\\1&1&1&1&1&1\end{pmatrix},
 \qquad D_2=\bigoplus_{i=0}^2
             \begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]
Its primitive bases are the three sums of paired faces in degree
two and \(a_1-a_0,a_2-a_0\) in degree one. The oriented dual-cell
map in S6 gives the common exterior \(H_3=\mathbb Z^3\),
\(H_4=\mathbb Z^2\), \(H_2=0\). The H3 generators are the
positive complex normal meridians. Their pairwise intersection is
zero. Poincare--Lefschetz duality gives the corresponding relative
cycles \(D_i\). Filling the other two curve tubes projects the H3
basis to the selected meridian. These are independent cellular
and dual-cell maps, not consequences of an equivariant product.

Write \(\mathcal V\) for the ordinary-product variation and
\(\delta_i\) for the actual ambient stable-derivative pairings.
For \(a_j-a_0=\partial x_j\), the positive-circle identity
\(\partial\Delta=-\Delta\partial\) gives
\(\Delta x_j=w_jD_j-w_0D_0\). Its action prism and the chain-rule
prism yield
\[
 \mathcal V(w_je_j-w_0e_0)=I_je_j-I_0e_0,\qquad
 w_j\delta_j-w_0\delta_0=W_j-W_0.                    \tag{OR65.17}
\]
Here the actual return fixes the common boundary by the ordinary
product just constructed. The ambient-frame change extends
through each annulus times its normal four-disc, whose H3 is zero;
its pairing on the capped trace vanishes. Thus no omitted change
of ambient stable frame occurs in (OR65.17).

Substitution in (OR65.16) gives
\[
                    I=(-8m,4m,-4m),\qquad W=(8m,0,0).
\]
Since \(w_0=0,w_2=-1\), equation (OR65.17) gives
\[
                    \mathcal V_{22}=4m,\qquad \delta_2=8m.
\]
The actual ambient-to-first-resolution product comparison has
third class \(+1\) on its complex meridian: write the Cox normal
trivialization \(q_H=u(c_0+j\bar c_1)\), so that
\(c=u^{-1}q_H\). Its derivative is triangular; contract its
off-diagonal block to zero. The only nonconstant stable block
is left multiplication by \(q_H\), of degree +1. The positive
complex meridian and the relative D3 product orientation give
the frame correction \(-\mathcal V_{22}\). In the product frame
the relative generators L and R have stable derivatives 0 and
\(-2\), respectively. Hence the ordinary relative pair is
\[
 2\nu_2=\delta_2-\mathcal V_{22},\qquad
 \mu_2=-\mathcal V_{22}-\nu_2,
 \qquad (\mu_2,\nu_2)=(-6m,2m).                    \tag{OR65.18}
\]

The native-to-ordinary C2 boundary arrow is
\[
 q_H\mapsto (U H_{t_0}U^{-1})q_H H_{l_2-t_0}.        \tag{OR65.19}
\]
Its left factor has degree \(2t_0=4m\) on the Hopf-oriented
sphere times parameter; this is the Maurer boundary integral
of the displayed based H contraction. Its right factor depends
only on radial coordinate and parameter, so has third degree
zero. Extend the inverse factors over \(D^3\times I\) by the
literal cylinder retraction. The endpoint has free degrees
\((-2t_0,0)\), and these coefficient maps extend over
\(D^3\times D^4\). Thus there is no disc-supported correction.
The ordinary return is the native return followed by this
pure-left map. Its native doubled free pair is consequently
\[
                         (-2m,2m).                  \tag{OR65.20}
\]
By (OR65.11) this is the actual square of the single native return.
The relative group has torsion-free free quotient \(\mathbb Z^2\)
and central disc group \(\Theta_7\). Therefore its single native
free pair is \((-m,m)\). This step divides only two known free
integers of an actual square.

## OR65.5. The oriented native flop and the r-loop class

Retain K17's original Cox order \((z_0,z_4,z_1,z_2)\), auxiliary
weights \((1,1,-1,-1)\), and physical weights \((-1,0,0,1)\).
The positive auxiliary moment has \((z_0,z_4)\ne0\), with common
fan edge \(u_1u_2\), so it is \(\mathcal T_-\). In the chart
\(z_4=1\) take \((a,b,c)=(z_0,z_1,z_2)\); the chart \(z_0=1\)
is exactly \((a^{-1},ab,ac)\). This identifies the first ruling
with the native C2 product used above. The negative auxiliary
moment has \((z_1,z_2)\ne0\), common edge \(u_0u_4\), and is
\(\mathcal T_+\). The actual lifted seam is
\[
 (z_0,z_4,z_1,z_2)\mapsto
       ((AD)^{-1}z_0,z_4,Az_1,Dz_2).                 \tag{OR65.21}
\]
It preserves q, commutes with auxiliary and physical circles,
and extends to both quotient rulings. Its inverse uses the
reciprocal units at the same q. Transport the Hermitian metric
by this map before radial normalization; thus its nonunit moduli
are retained on the common link. Full q-dependent germs are
carried by the same normal-rescaling isotopies on both rulings.
Every period representative has trivial stabilizer, and extension
by the original periods gives the map on the whole orbit of curves.
The cap and ordinary exterior are unchanged.

On the common link use the actual quaternion products
\[
 u=a_0+ja_1,\quad v=c_0+j\bar c_1,\quad
 h=uiu^{-1},\quad k=v^{-1}iv,\quad q_H=uv.
\]
The old and new boundary coordinates are \((h,q_H)\) and
\((k,q_H)\). Hence their exact arrow and oriented exterior
extension are
\[
 \tau(h,q_H)=(q_H^{-1}h q_H,q_H),\qquad
 T(y,q_H)=(q_H^{-1}yq_H,q_H).                         \tag{OR65.22}
\]
The inverse uses \(q_Hyq_H^{-1}\). It is smooth at y=0 and
orientation preserving. The same four-coordinate multipliers
(OR65.21) intertwine this map with the actual parameter action,
including any odd loop; thus no additional parameter transition
is inserted between the two native products. In particular the
direction is \(\mathcal T_-\) to \(\mathcal T_+\).

Use the oriented relative generators of P3K.23,
\[
 L(y,q_H)=(y,\zeta(y)q_H),\qquad
 R(y,q_H)=(y,q_H\zeta(y)),
\]
where \(\zeta:(D^3,S^2)\to(S^3,1)\) has degree one. They
commute and extend over \(D^3\times D^4\), so their closed
sphere classes are zero. The central disc generator \(\mathcal C\)
has the positive oriented class 1; its sign is fixed by the signed
plumbing proof in P3K.23, with the same complex exterior orientation.
The exact relative conjugation is
\[
 T(L^\mu R^\nu\mathcal C^s)T^{-1}
       =L^{-\nu}R^{\mu+2\nu}\mathcal C^{s+\nu}.     \tag{OR65.23}
\]
This group identity imposes no circle-quotient restriction on the
selected curve. The actual native pair \((-m,m)\) therefore
gives
\([\Sigma_+]=[\Sigma_-]+m\). By the independent computation
(OR65.8), \([\Sigma_+]=0\). Thus
\([\Sigma_-]=-m=-3k\), proving the first row of (OR65.1).

The exact outer obstruction which the old charged-cap argument
omitted is visible in the same charts. On the fixed branch at
the second vertex, the C0 native coordinates have base
\(\kappa w_0\), negative normal \(\alpha v_0\), and positive
normal \((\kappa\alpha)^{-1}u_0\). The C2 native coordinates
have base \(w_0\) and normals \((v_0,u_0)\). Their map has
base multiplier \(\kappa^{-1}\), normal matrix
\(\operatorname{diag}(\alpha^{-1},\kappa\alpha)\), and
positive-weight determinant
\[
                  \kappa\alpha/\bar\alpha,
                  \qquad\operatorname{wind}=-2m.    \tag{OR65.24}
\]
The other outer branch is the identity. A nonvanishing determinant
homotopy between them would have equal winding at both ends.
Thus equal inner charged-cap gauges do not make the full outer
determinant parameter-independent. Equation (OR65.23) computes
the sphere correction without discarding that outer map.

## OR65.6. The actual shorter source/line/cap endpoint

We reproduce the endpoint map needed for the second row, retaining
the component divisor. Let B0 be the actual unscaled contracting
lift over \(-3G\), with zero on source C1, so its inverse over
\(+3G\) has pole on source C0. An actual rational lift U over
\(+G\) is supplied in the section frame by the divisor identity
\[
 \operatorname{div}\frac1{x-x(G)}=2O-G-(-G)
                 =t_G^*(G-O)-(G-O),
\]
taking the inverse of the resulting line isomorphism. Translation
extends on the relatively minimal regular source; its graph
preserves the canonical two-form, and cannot have an exceptional
curve over a smooth centre. In the actual line graph its forward
source shift is j to j+1. Normalize by an integral base monomial
so its line valuation is zero. Its two defects are
\(h_j-h_{j+1}=-1,0\). Thus its vertical pole is C0, through both
node charts. The third translated norm has divisor
\(-2C_0-C_1\), and
\[
                \rho=B_0^{-1}/U^3,\qquad
                \operatorname{ord}_{q=0}\rho=1.     \tag{OR65.25}
\]
The ratio is an actual rational base function because its maps
cover the same source translation and their ratio is constant
on every compact generic elliptic fibre.

On the actual order-m good root, the central Cartier line has
deck weights \(\varrho,\varrho^{-1},1\) on the cyclic orbit
of G', O and the third order-three point, with
\(\varrho=\zeta_3^2\). An invertible lift L of translation
\(+G'\) has successive weight ratios \(\varrho^{-1}=\zeta_3\).
Finite cyclic averaging removes the nonconstant commutator unit;
an invariant cube root fixes its exact norm. Hence
\[
                    DLD^{-1}=\zeta_3 L,\qquad
                    L^3=B_0^{-1}.
\]
Write the pulled-back U as \(z^e a(z)L\). The target-scalar
conjugation rule \(D m_fD^{-1}=m_{f(\zeta_m^{-1}z)}\) gives
\[
 \zeta_m^e=\zeta_3,\quad a(\zeta_mz)=a(z),\quad
 \operatorname{ord}_{t=0}\rho=-3e/m\equiv-1\pmod3.  \tag{OR65.26}
\]
At the type-II and other ordinary fibres, the vertical divisor
is a whole-fibre divisor, so the order of rho is divisible by
three. These statements retain the original d-character, which
is scalar and commutes with L.

Put \(h_0=t^n=q^{-n}\). The rational divisor of
\(h_0\rho^{-2n}\) is divisible by three at every fibre: its
cusp order is \(-3n\) modulo three, its IV* order is \(3n\)
modulo three, and the remaining orders are zero modulo three.
Choose the actual rational root
\[
                     g_0^3=h_0\rho^{-2n}.
\]
The endpoint-to-initial ordinary map is
\[
 C_r=r^{2nk}g_0(t)U^{-2n}:X_{\zeta_3r}\longrightarrow X_r.
                                                               \tag{OR65.27}
\]
Its whole-fibre powers cancel at every ordinary fibre. On the
IV* root insertion of (OR65.26) leaves precisely the base power
\(z^{mn/3}\), an invariant unit and \(L^{-2n}\).
The ordinary-to-cap map (OR65.5) changes under
\(r\mapsto\zeta_3r\) by the logarithm of that positive base
power. Consequently its exact square is
\[
 \Phi_r C_r=C_{\rm cap}\Phi_{\zeta_3r},\qquad
 C_{\rm cap}=(\text{invariant unit})L^{-2n}.
\]
The bounded map extends, and
\[
 C_{\rm cap}A_{\zeta_3r}C_{\rm cap}^{-1}
       =\zeta_3^n\zeta_3^{2n}A_r=A_r.               \tag{OR65.28}
\]
This proves the cap descent for both signs, with its original
character and the specified closing direction.

The cusp vector of (OR65.27) is \((-2n,-n)\). Write
\(h_{\rm src}\) for the actual source deck with logarithmic period u;
it is distinct from the primitive H-deck h in (OR65.3).
Reindex by \(h_{\rm src}^n\), of vector \((2n,n)\), to make it
bounded on every toric chart. Retain all logarithms by putting
\(R=\log\rho/(2\pi i)\), \(L_U=\log U/(2\pi i)\),
\(g_*=\log g_0/(2\pi i)\), coherently with the norm. Their
literal identities are
\[
 3L_U=-\gamma+mv\delta-R\delta,\qquad
 3g_*=-ns-2nR.
\]
The bounded logarithm of the reindexed closing is therefore
\[
 nu-2nL_U+(2nkv+g_*)\delta
       =\frac{nK}{3}-\frac{ns}{3}\delta
       =\tau(v),\qquad
 \tau(v)=\frac n3(D+2mv\delta).                    \tag{OR65.29}
\]
This is an equality of the full units, including their constants.
Change the constant cube root by
\(\exp(-4\pi i nk/3)\), an actual cube root of unity, and write
\(a_*=-2nk/3\). The closing becomes the bounded translation
\(\tau(v)+a_*\delta\). The same extending origin as above obeys
\[
 \sigma(v+1/3)-\sigma(v)=\tau(v)+a_*\delta,\qquad
 \sum_{j=0}^2\{\tau(v+j/3)+a_*\delta\}=nD+2nmv\delta.
                                                               \tag{OR65.30}
\]
On the ordinary chart the three closing maps compose exactly to
\(h_0B_\lambda^{2n}\). The second factor is a literal period;
the first is the prescribed one-r-turn closing. Work first over
the universal v-plane, quotient by that one-turn gluing, then
by the resulting order-three parameter deck. Its action is free
because r is nonzero. This constructs the proper holomorphic
family over \(w=r^3\), with \(\lambda=w^k\), and retains both
fans, all source and cap maps, and both vertices at once.

## OR65.7. The three native seams and the shorter sphere class

Use the literal plus translation \(\xi=z+\sigma(v)\) in the
additive torus coordinates of (OR65.30); in characters it is
multiplication by \(\exp(2\pi i\sigma(v))\). The closing sends
\(z_{\rm end}\) to \(z_{\rm end}+c_{\rm add}(v)\), where
\(c_{\rm add}(v)=\tau(v)+a_*\delta\). Since
\(\sigma(v+1/3)-\sigma(v)=c_{\rm add}(v)\), it gives exactly
\(\xi_{\rm initial}=\xi_{\rm end}\). The forward map is the
inverse of this closing. The C2 row of
(OR65.10) remains \((a^{-1},ab,ac)\), so these coordinates give
an actual closed native C2 product. They do not supply the
quarantined whole-plumbing equivariant product.

Here are all three intermediate seams of its pullback. Write
\(c(v)=\exp(2\pi i\{\tau(v)+a_*\delta\})\) for the bounded
closing, and \(e(v)=c(v)^{-1}\) for its forward map, after the
actual source-period reindexing. On the j-th cut interval of the
triple pullback use the same single product and the transition
\[
            P_j(v)=\prod_{h=0}^{j-1}e(v+h/3)^{-1},
            \qquad j=0,1,2,3.                       \tag{OR65.31}
\]
The factors commute because they are actual base-dependent torus
translations. At the seam from j to j+1 the outgoing product
gains exactly \(e(v+j/3)^{-1}\); hence its outgoing chart is
the incoming chart multiplied by the prescribed closing. This
is the literal pullback identification, with every collar
derivative retained. Equation (OR65.30) gives
the complete endpoint list
\[
\begin{array}{c|c}
 j&\log P_j/(2\pi i)\\ \hline
 0&0\\
 1&nD/3+(2nkv-2nk/3)\delta\\
 2&2nD/3+(4nkv-2nk/3)\delta\\
 3&nD+6nkv\delta .
\end{array}
\]
In particular
\[
 P_3(v)=\exp(2\pi i(nD+2nmv\delta)),
\]
which is precisely the bounded one-r-turn closing after the
actual period reindexing. The ordinary identity
\(h_0B_\lambda^{2n}\) and the cap square (OR65.28) identify the
full family, not just these bounded charts.

Define the covered r native product to be this triple pullback.
Each coordinate change commutes with H, K and delta and leaves
the complete transition coefficients in (OR65.10) unchanged.
Thus its doubled ordinary construction (OR65.12)--(OR65.20)
computes the same covered free pair \((-3k,3k)\) directly in
these charts. No identification with a presumed whole-plumbing
product is used. A connection with the single w native product,
pulled back to the cover, has relative return \(f_w^3\).
The free quotient of the relative group is \(\mathbb Z^2\),
so its exact free coordinates satisfy
\[
                     3(\mu_w,\nu_w)=(-3k,3k),
                     \qquad(\mu_w,\nu_w)=(-k,k).    \tag{OR65.32}
\]

For the positive fan choose the actual closed fixed-curve native
product; the vertex maps and their standard fixed-curve unit
normalization close by the same endpoint (OR65.30). Its pullback
gives the covered physical circle Euler line and tangent bundle.
The degree-three covering of the completed conifold mapping tori
therefore gives \(3A_{+,w}=A_{+,r}=0\) as an equality of integer
characteristic integrals. Thus \(A_{+,w}=0\) and its actual
Hopf lift has sphere class zero. This is integer naturality on
constructed mapping tori, not division of an element of Theta7.

The same Cox arrow (OR65.21), now with the shorter endpoint,
carries the native flop and both cap maps. Applying the oriented
identity (OR65.23) to (OR65.32) gives
\([\Sigma_{+,w}]=[\Sigma_{-,w}]+k\). Hence
\([\Sigma_{-,w}]=-k\), completing (OR65.1). For k=1 this is
the actual positive loop of the scalar itself, with class 27.
The integers k=1 through 28 supply every residue; each is an
actual admitted cap order and completed family.

The symbolic certificate records the source identity, period
change, all three full-unit seam rows, both norm-sign cap squares,
the doubled trace degrees, actual free-coordinate equations and
three-step norm. Its computations supplement the explicit maps
above. No claim for a third fan or an arbitrary fan is made here.
