# Source-zero real trace and actual Cox divisor: working calculation

This note records exact local maps toward the remaining source-zero order-two
attachment. It does not assign either individual source-zero return. We retain
the physical line convention of P3K.68 and the literal maps of the current-run
source-zero completion note.

## RT.1. The horizontal trace immersion

The marked small-resolution coordinates are
\[
 A=Dz,\qquad C=Bz,\qquad v=(B-Dz)/2.
\]
On the normalization of the selected nodal fibre,
\[
 X=s^2-1,\quad Y=s(s^2-1-v),\quad T=v^2-2v,\quad
 z=(s+1)/(s^2+s-v).
\]
Put \(x=s+1,v=xr\). The blowup chart has the exact map
\[
 z=(x-1-r)^{-1},\quad B=x(x-2)(x-1-r),\quad
 D=(B-2xr)/z.
\]
The Jacobian of \((z,B)\) with respect to \((x,r)\) is
\(-2(x-1)/(x-1-r)\), hence is nonzero on the exceptional curve wherever
this chart is finite. At its missing point use
\(w=x-1-r,C=x(x-2)\); the Jacobian is \(2x-2\), again a unit there.
The second blowup chart \(v=y,x=yh\) has
\(z=h/(-1-h+yh^2)\), whose h derivative at y=0 is
\(-1/(-1-h)^2\). These formulas give the actual immersion of the complete
horizontal normalization trace through the exceptional curve.

Let \(F=\operatorname{Bl}_{(-1,0)}(\mathbb P^1_s\times D_v)\) and let E
be its exceptional curve. The Cartier ratio
\((s-\sqrt{1+v})/(s+\sqrt{1+v})\) has divisor
\(D_+-D_--E\). The actual source line restricts as \(O(-aE)\).
Consequently the retained spinor determinant on this trace is
\((1-2a)E\); reversing the two selected branches gives
\(-(1+2a)E\). The local intersection numbers \(E^2=-1,\sigma(F)=-1\)
therefore give the two local physical index expressions
\[
 a(a-1)/2,\qquad a(a+1)/2.
\]
Their difference is a. This is an intersection calculation on the specified
trace. The complete global fixed/cap trace has not yet been identified with F,
so we do not use either expression as a global return.

## RT.2. Exact q factorization on the Cox bridge

Use the actual Cox coordinates
\[
 A'=s_0t_0,\quad B'=s_1t_1,\quad C'=s_0t_1,\quad D'=s_1t_0,
\]
with physical weights \((-1,-1,+1,+1)\) on
\((s_0,s_1,t_0,t_1)\), divided by the retained \(\mu_a\) when appropriate.
The actual base functions, before any quotient completion, are
\[
 v=(s_1t_1-s_0t_0)/2,\qquad
 q=(s_1-s_0)(t_0+t_1)-(s_0t_1-v)^2.
\]
Set \(x=s_0,y=t_1,k=s_1-s_0,l=t_0+t_1\), and choose the analytic unit
\(\sigma=\sqrt{1+xy}\) with value 1 at the origin. Define
\[
 F_+=\frac{(\sigma+1)k-x^2l/(\sigma+1)}2,\qquad
 F_-=\frac{(\sigma+1)l-y^2k/(\sigma+1)}2.
\]
Then
\[
 q=F_+F_-,\qquad
 \det\frac{\partial(F_+,F_-)}{\partial(k,l)}=\sigma.
\]
Thus this is an actual analytic coordinate change over \((x,y)\), with inverse
\[
 k=\frac{(\sigma+1)F_++x^2F_-/(\sigma+1)}{2\sigma},\quad
 l=\frac{y^2F_+/(\sigma+1)+(\sigma+1)F_-}{2\sigma}.
\]
The weights of \(F_+,F_-\) are respectively \(-1,+1\). No physical
character is changed. The source parameter becomes
\[
 v=xy+\frac{yF_+-xF_-}{2\sigma}.
\]
On the chart with invariant coordinates \(u=x/F_+,z=y/F_-\), this reads
\[
 v=q\left(uz+\frac{z-u}{2\sqrt{1+uzq}}\right).
\]
These formulas retain both actual branches of q=0. They show why a proposed
completion has to inspect their quotient strata at v=0 explicitly; the
horizontal trace and the isolated origin link do not by themselves enumerate
all strata of such a completion.

## RT.3. The local real chamber map

On the Cox cover define
\(\mu=(\lVert t\rVert^2-\lVert s\rVert^2)/2\). The positive real part of
the physical complex action is
\[
 (s,t)\longmapsto(R^{-1/a}s,R^{1/a}t),\qquad R>0.
\]
Its moment coordinate has strictly positive derivative on every nonzero orbit.
It therefore gives the unique transport between two prescribed moment levels
on an orbit that meets both levels. The negative and positive chambers give the
two displayed small resolutions. In the common Cox coordinates the actual
primitive source translation has identity line coordinate; this is exactly the
map \(U:(p,w)\mapsto(p-G,w/X(p-G))\) in the source divisor frames. Its a-th
power line version is retained on \(\mathbb C^4/\mu_a\).

The additional actual suspension factor is
\(2(-1)^{b+1}\lambda q\). Its positive norm and phase must both be included
when chamber pieces are attached. We have not extended this real map through
every q=0 quotient stratum or the finite logarithmic cap, so no global real
bordism is asserted here.

## RT.4. A primary link-classification input and its exact remaining arrow

Skopenkov, *Suspension theorems for links and link maps*, arXiv
math/0610320v3, Theorem 1.1 and Corollary 3.2, gives the classification of
ordered smooth links \(S^2\sqcup S^2\subset S^5\). Haefliger, *Differentiable
embeddings of spheres*, Corollary 6.6 (printed p.422), gives
\(C_2^3=0\). The other possible summand is
\(\pi_1(SO/SO_2)=0\), by the exact sequence of
\(SO_2\to SO\to SO/SO_2\): the map on \(\pi_1\) is the surjection
\(\mathbb Z\to\mathbb Z/2\). Hence the link group is \(\mathbb Z\).
The integer is the oriented complement degree: Skopenkov's definition of
\(\lambda\) in §3, printed pp.9–10, is the actual retraction of the complement
onto a meridian \(S^2\). Corollary 3.2 provides the explicit right inverse
\(x\mapsto(x/2,\varphi(x))\) in \(D^3\times S^2\), where
\(\deg\varphi\) is that integer.

This is a complete classification of the stated embedded two-sphere link.
For its use here, the actual source vanishing cycle must first be identified
with the circle lift of the second sphere, including its normal framing and
the finite-cap comparison. The local Cox quotient has circle degree a on that
second sphere. That fact supplies its local Euler evaluation; it does not yet
supply the required global embedding/framing arrow.

Primary URLs:
- https://arxiv.org/pdf/math/0610320
- https://webhomes.maths.ed.ac.uk/~v1ranick/tda/haefliger.pdf

Exact algebra: `code/part3/source_zero_real_trace.py`, with JSON and captured
output. Its certificate assigns no global return.

## RT.5. The charged ruling-mapping-torus model

We compute a specified compact model, without identifying it with an end of
the completed family. Put
\[
 K=S^2_h\times S^3_q,\qquad
 \tau(h,q)=(q^{-1}hq,q),
\]
and form its mapping torus using this displayed first-to-second arrow.
It is the projectivization of the rank-two bundle over \(S^3\times S^1\)
whose transition is the same \(SU(2)\) map \(q^{-1}\). This follows on the
unit spinor: \(u\mapsto q^{-1}u\) has projective image exactly \(\tau\).
Thus no abstract bundle substitution is required. Denote the second Chern
number of this explicitly clutched bundle, in the chosen base orientation,
by \(c\). The clutch has degree one up to the displayed inversion, so
\(|c|=1\); reversing the first-to-second arrow changes its sign.

Let \(h=c_1(O(1))\) on this projectivization and orient its sphere fibres
complex positively. The actual projective-bundle relation and pushforward are
\[
 h^2+\pi^*c_2(E)=0,\qquad \pi_*h=1.
\]
The vertical tangent Euler class is \(2h\), and the base \(S^3\times S^1\)
is parallelizable. For the specified charge-a line \(O(a)\) we therefore get
\[
 k=-a^3c,\qquad \ell=-4ac,\qquad
 \frac{4k-\ell}{24}=-\frac{a(a^2-1)c}{6}.
\]
The dual line reverses all three numbers. In particular the magnitude of the
charge-two model index is one, whereas the charge-one index is zero.
These equations compute the entire mapping-torus bundle, including its line.
They do not identify its boundary orientation with the remaining source-zero
attachment.

There is an exact finite-cap input for that attachment, proved in
`part3_source_zero_annular_attachment_working.md`, EA.4. In the reduced
sector the Cartier translation is
\[
 U_2^{\rm Cartier}=r_{\rm target}^{-1}U_2^{\rm tensor}r_{\rm source},
 \qquad r=X(p-G),
\]
and on the root \(q_\infty=z^m\),
\[
 U_{\rm cap}=z^{-m}U_2^{\rm Cartier}=B_0/(2h),\qquad
 B=2\lambda h\,U_{\rm cap}.
\]
The actual extending \(B_0\) and deck-invariant h prove that this map extends
and commutes with the full finite cap action. Thus one forward B period
contains exactly the t-ruling to s-ruling arrow, the inverse of \(\tau\) in
the convention above. The inverse B period contains \(\tau\). This verifies
the primitive arrow and excludes an additional ruling interchange at this
cap. It still does not identify the oriented residual boundary with the model.

## RT.6. An embedded trace in the cut source product

The map of RT.1 is the normalization of the selected divisor q=0 in the
marked simultaneous source. Its only identifications are the two disjoint
sections \(D_+\) and \(D_-\) over the selected critical curve. At v=0 the
first lies on the strict component and the second on E; their images are the
same selected z=1 node. The other z=-1 node has a single preimage, the
crossing point of the central components in the smooth surface F.

Choose a smooth function \(\eta:F\to(-\varepsilon,\varepsilon)\) constant
and with distinct values on disjoint tubes of \(D_+\) and \(D_-\). Such a
function is obtained with two disjoint tubular cutoffs. Then
\[
 p\longmapsto(\nu(p),\eta(p))
\]
is a proper embedding of F into the compact cut source times an interval:
its derivative is injective by RT.1, and the only possible distinct points
with the same source image are separated by their height values. This
constructs the trace in that particular source product. Its normal bundle
is the oriented sum of the actual complex normal line of the source
immersion and the interval line. The complex normal line is
\(K_F\otimes\nu^*K_{\rm source}^{-1}\), by the determinant of the displayed
immersion. On the finite source chart the residue trivializes the latter
canonical factor. The divisor identity
\(K_F=O(-D_+-D_-)\) follows from
\(K_{\mathbb P^1\times D}=-2H\), the blowup term E, and
\(D_++D_-=2H-E\).

On the actual outer parameter circle, the two F9 endpoint lifts have the
same zero source-period gamma index and lie in a short interval with
distinct ordered endpoints. The explicit relative interval construction
of SQ.4a–c therefore identifies that boundary graph with this graph after
an isotopy fixed outside its source neighbourhood. This establishes the
boundary graph map. It does not extend the source translation cut through
the central flop: that separate cut is the outstanding gluing map.

## RT.7. The two local charged charts and the remaining boundary gate

In the resolved associated node chart
\[
 U=S_0z,\quad T_0=zV
\]
the variables \((S_0,S_1,T_1,z,V)\) have auxiliary weights
\((1,1,-1,a-1,-a)\) and physical weights \((0,0,0,1,-1)\).
Fixing V=1 gives the effective weights
\((-1,-1,+1,+1)/a\) and residual \(\mu_a\).
For \(a>1\), fixing z=1 gives
\((-1,-1,+1,+1)/(a-1)\) on \((S_0,S_1,T_1,V)\), with residual
\(\mu_{a-1}\). Both are literal gauge calculations. A stability choice
does not automatically include both origins.

Writing \(f(a)=a(a^2-1)/6\), the exact numerical identity is
\[
 f(a)-f(a-1)=a(a-1)/2.
\]
It relates the charged local models to the ordered trace expression, but
does not specify which charged strata occur in a global boundary.

For orientation control, on the ordinary Cox cover conjugate its two
negative physical-weight coordinates. This preserves the real
eight-dimensional orientation. With radius increasing outward, the
circle-first orbit orientation is
\(-dr\wedge\Omega_{\mathbb{CP}^3}\). A deleted origin thus has
positive complex \(\mathbb{CP}^3\) boundary. The physical nonzero-vector
line on that boundary is \(O(-a)\); the \(O(a)\) line is its dual U.
Consequently the physical model index on that oriented boundary is
\(-f(a)\). This is a local orientation calculation only.

The proposed real cut uses the compact marked source, cuts its suspension
outside the short graph, and inserts the Cox moment cobordism in place of
the birational U cut. The associated node \(UV=q\) is required on the
overlap, with its actual line character and the actual polynomial q.
Fourfold's finite-cap arrow in RT.5 supplies the cap side of this cut.
The following two maps are still absent:

1. The finite, Hausdorff real overlap of that moment cut with the full
   q=0 associated-node chart, including its actual stable subsets.
2. The labelled boundary map from the chosen node resolution (the
   j=-1 vertical fan of SZ.15) to the requested source-zero fan and the
   resulting orientation of every residual boundary.

The nonproper infinite central quotient of SZ.29 is not used as a replacement
for either map. We retain the local orientations and the cap arrow above
while leaving both individual source-zero returns undecided.

## RT.8. A regular reduced moment cut with its actual fixed strata

For the reduced case a=2, write the auxiliary and physical weight vectors as
\[
 A=(1,1,-1,1,-2),\qquad D=(0,0,0,1,-1).
\]
Let \(\mu_A,\mu_D\) be their ordinary quadratic moments on the five displayed
coordinates. Fix \(K>0,c>0\) and take the invariant hypersurface
\[
 \mu_A+K\mu_D=c.
\]
Along the positive real auxiliary action its derivative is a positive
multiple of the sum with coefficients
\[
 A_i(A_i+KD_i)=(1,1,1,1+K,4+2K).
\]
It is therefore strictly positive off the origin. Every auxiliary complex
orbit whose positive-weight coordinates \((S_0,S_1,z)\) do not all vanish
meets this hypersurface exactly once: as the real auxiliary parameter tends
to positive infinity the left side tends to positive infinity, and at the
other end it is nonpositive or tends to negative infinity. Quotienting this
section by the compact auxiliary circle is thus the actual positive-stable
complex quotient, with q and v unchanged. The hypersurface is regular and
the compact truncations of this quotient are Hausdorff.

Its physical fixed strata follow by comparing the two weight vectors on
the nonzero coordinates. The physical-weight-zero locus \(z=V=0\) gives
the horizontal quotient with weights \((1,1,-1)\), the blowup surface.
The z-only ray meets the hypersurface once and has auxiliary weight one,
so its local charged model is the charge-one chart of RT.7. The V-only
ray cannot meet a positive level because its coefficient is \(-2-K\).
There are no other proportional-weight supports. This proves the stated
fixed-stratum list for this particular local cut.

The physical positive real action, followed by the unique auxiliary
projection back to the level, is also monotone in \(\mu_D\) away from its
fixed strata. Put
\[
 A_2=\sum A_i^2|z_i|^2,\quad
 AD=\sum A_iD_i|z_i|^2,\quad D_2=\sum D_i^2|z_i|^2.
\]
Its derivative, up to one common positive convention factor, is
\[
 \frac{A_2D_2-(AD)^2}{A_2+KAD}.
\]
The denominator is the positive sum above. The numerator is nonnegative by
the Gram determinant and vanishes precisely when the two circle directions
are proportional on the nonzero coordinate support, the fixed strata
already listed. Thus this is an explicit monotone real chamber transport,
not an inferred deformation of complex quotients.

For a=1 the z-only auxiliary weight is zero. The same formula does not
give a locally free auxiliary quotient there, and RT.8 makes no assertion
about that different stratum. Also, a contracting factor containing q can
send a fixed-coordinate level to an infinite or collapsed end as q tends
to zero. The actual adjacent node-chart reindex is still required before
the two finite ends of this cut can be glued by B. That reindex and its
labelled outer-fan map remain the two gates in RT.7.

## RT.9. The reduced link and its framed fixed three-sphere

The actual positive quotient of RT.8 is
\[
 W=\operatorname{Tot}\bigl(O(-1)\oplus O(-2)\longrightarrow
 \mathbb P^2_{[S_0:S_1:z]}\bigr),
\]
with fibre coordinates T1,V: on the three nonzero homogeneous-coordinate
charts, the auxiliary coefficient transition functions are their first
and second inverse powers. The physical action is z of weight one and V
of weight minus one. Its fixed surface is F=D(O(-1) over P1), and its
other fixed point is [0:0:1] with zero fibre coordinates.

The disk-bundle boundary L=S(O(-1) plus O(-2)) has integral groups
H2=Z,H4=Z/2,H5=Z. Indeed the sphere-bundle Gysin Euler map from H0(CP2)
to H4(CP2) is multiplication by two. The adjacent exact terms give the
other groups. Thus this link is not substituted for a homotopy sphere.
The disk bundle is spin, since c1=3h-h-2h=0; its middle form is [2]
and p1=3h2+(h2+4h2)=8h2.

On F set R=||S|| |T1|. At R=epsilon, take the unique positive auxiliary
gauge ||S||=1 and write T1=epsilon exp(i phi). Then
\[
                  p=e^{i\varphi}(S_0,S_1)\in S^3
\]
is invariant under the remaining auxiliary circle and is the actual
fixed-set boundary map. The positive-weight normal coefficients have
the exact arrow
\[
 (z,\overline V)\longmapsto
 (e^{i(a-1)\varphi}z,e^{ia\varphi}\overline V).       \tag{RT.9}
\]
Before the positive gauge, the second coordinate also carries the
positive factor ||S||^(2a); it is retained in the real quotient map.
The physical action is scalar on both displayed coefficients. Its
original complex normal orientation is the negative of this spinor
orientation, because precisely V was conjugated.

The finite free-end map is also explicit. In the common Cox line xi
of auxiliary weight a, put Nt=|xi| ||t||^a, Ns=|xi|/||s||^a and
R=||s|| ||t||. Since Nt=R^a Ns, the map Nt=1 to Ns=1 is
\[
 (\xi,\xi_{\rm dual})\longmapsto
 (R^a\xi,R^{-a}\xi_{\rm dual}),\qquad\xi\xi_{\rm dual}=q.
                                                        \tag{RT.10}
\]
It is smooth and bounded on R>=epsilon, preserves q, and extends both
q=0 branches. Auxiliary normalization is performed afterward. The q
factor in B is first absorbed in the actual adjacent node charts
\[
 U_j=\frac{w}{(2\lambda)^jq^j},\quad
 V_j=\frac{(2\lambda)^jq^{j+1}}w,\quad
 B:(j,U_j,V_j)\mapsto(j+1,\rho U_j,\rho^{-1}V_j).
\]
The Cartier coefficient rho is the identity in the common Cox line.
This is an arrow between node charts, not a limit of q-scaling on one
chart. The fixed S3 in (RT.9) remains on the inner end. That end is
therefore not identified with the bare ruling mapping torus of RT.5.

## RT.10. A specified local fixed-sphere surgery and its physical line

Attach D4 times D4 to the reduced disk bundle W along its fixed
S3 times D4 tube using (RT.9). The circle is trivial on the first
factor and has the original normal weights (+1,-1) on the second.
This is an explicit equivariant handle attachment. Its boundary Y
has free circle action. The capped fixed surface is CP2 with reversed
orientation, with exceptional generator E squared equal to minus one;
the separate charge-one point is unchanged.

The normal line direction follows from the actual ideal inclusion:
O(-E) has inside frame T1, so an inside coefficient c becomes T1*c
in the outside trivial line. Hence (RT.9) extends the positive spinor as
\[
 \mathcal E=O(-(a-1)E)\oplus O(-aE),\quad
 c_1(\mathcal E)=(1-2a)E,\quad c_2(\mathcal E)=-a(a-1),
 \quad p_1(\operatorname{ad}\mathcal E)=-1.             \tag{RT.11}
\]
Here a=2 in the reduced disk bundle. The same polynomial records the
displayed framed-surface calculation for other integer charges.

Here O(kE) denotes the smooth complex line with its displayed clutch;
no complex structure on the capped reversed CP2 is asserted.
Orient BF=P(Ecal) by the orientation inherited from complex F and
extended across its cap, followed by the complex projective fibre,
and set h=c1(O(1)).
The projective coefficient sequence gives
h2+c1(Ecal)h+c2(Ecal)=0 and pi_*h=1. The physical line is M=O(-1).
Its two separate characteristic integrals are therefore
\[
 (k_{B_F},\ell_{B_F})=(3a^2-3a+1,4).                 \tag{RT.12}
\]
Indeed pi_*h3=c1(Ecal)^2-c2(Ecal)=-3a2+3a-1. The vertical tangent
class is 2h+c1(Ecal), whose squared pushforward is
c1(Ecal)^2-4c2(Ecal)=-1; the base p1 integral is -3. Dualizing h
gives exactly the physical signs in (RT.12).

We retain the three actual boundary orientations. The positive-spinor
polar orientation is dr wedge ddelta wedge Omega_CP1. Conjugating V
reverses that normal real4 orientation. The circle-first orbit
orientation near the fixed surface is consequently
Omega_F wedge dr wedge Omega_CP1. Its deleted tube contributes -BF.
At the other fixed point the weights are (-1,-1,+1,+1); conjugating
two coordinates preserves real8 orientation, and its deleted ball
contributes positive complex CP3, with physical line O(-1). At the
outside, moving the circle past the outward normal contributes
minus the physical quotient Y/S1. Thus the free quotient bordism has
\[
          \partial Q=-Y/S^1\;\sqcup\;-B_F\;\sqcup\;\mathbb P^3.
                                                        \tag{RT.13}
\]
On CP3 the physical integrals are (-1,-4). The associated physical
line extends over Q. The stable tangent bundle of its free total
space is the orbit tangent plus the trivial circle direction, so p1
also extends. Stokes, using product connections on every collar,
gives, for the reduced a=2 model,
\[
 (k_{Y/S^1},\ell_{Y/S^1})=(-8,-8),\qquad
                 (4k-\ell)/24=-1.                    \tag{RT.14}
\]
This computes the specified framed local surgery boundary Y. It does
not identify Y, its orientation, or its line/cap marking with the
unassembled residual end of the global source-zero family. That
labelled attachment, including the j=-1 versus requested node fan,
remains open. No individual source-zero return is assigned here.

## RT.11. The precise remaining radial-boundary mismatch

The previous local surgery uses a disk-bundle radial boundary in W.
The actual finite-source cut does not yet have that boundary map.
Indeed in the associated chart
\[
 s=(S_0,S_1),\quad t=(zV,T_1),\qquad
 R^2=(|S_0|^2+|S_1|^2)(|zV|^2+|T_1|^2).
                                                        \tag{RT.15}
\]
On the whole fibre over [0:0:1], R is zero, including points with
nonzero T1 or V. A disk-bundle radial norm is positive at those points.
For example the representative (S0,S1,z,T1,V)=(0,0,1,1,0) has R=0
and is off the zero section. Thus the hypersurface R=epsilon has not
been carried to S(O(-1) plus O(-2)) by the auxiliary normalization or
by (RT.10). The latter preserves the actual source coordinates and
therefore cannot fix this mismatch.

The exact local parameter map also remains part of the attachment:
after the actual disc change vtilde=v*u_v(v), u_v(0) nonzero,
\[
             \widetilde v=S_0zV-S_1T_1.                \tag{RT.16}
\]
Its two quadratic critical charts are [1:0:0] and [0:0:1]. A future
compact replacement of the R-cut must specify its overlaps with both
charts, retain the physical line and the finite cap arrow, and account
for every additional boundary. No radial renaming or unproved
compactification is used in RT.9--10.
