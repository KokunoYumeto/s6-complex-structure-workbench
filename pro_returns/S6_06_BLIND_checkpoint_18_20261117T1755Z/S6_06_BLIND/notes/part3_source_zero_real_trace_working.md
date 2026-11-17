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

The disk-bundle boundary L=S(O(-1) plus O(-2)) has integral cohomology
\(H^2=\mathbb Z,H^4=\mathbb Z/2,H^5=\mathbb Z\). Indeed the
sphere-bundle Gysin Euler map from H0(CP2) to H4(CP2) is multiplication
by two. The adjacent exact terms give the
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

The cyclic source reset is an additional concrete gate. The central
identity B2/(4lambda2)=Id on v=0,T nonzero does not give an extending
identity near every point of the R>0 arm. The exact SZ.32 normal-cone
map, written with 2v=r(1-p) and T=-r(1+p), is w -> p w. Its limit at
nonzero w depends on the approach direction p. Thus the proposed
contraction by v -> s v is not available from that central identity.
The complete withdrawn diagnostic, including the separate old-j/current-n
label mismatch, is preserved in
`records/attempts/source_zero_end_diagnostics/withdrawn_label_and_reset_diagnostics.md`.

## RT.12. Removing the scalar winding by an actual parameter homotopy

This step concerns the punctured family only. It supplies the exact
reason a constant-scalar local attachment can be studied separately;
it does not replace v^(km) by a unit over the origin.

Fix a small source circle |v|=rho and its annular neighbourhood. Choose
the branch of sqrt(1+v) which extends across the source disc and the
same root and Cartier data as RG.1 and RCZ.5--7. On this compact
annulus introduce an independent nonzero root-scalar r. The actual
maps, in the existing full annular marking, are
\[
 B=r^mB_0(v),\qquad A=r^nA_0(v),\qquad
 F=F_0(v)+n\frac{\log r}{2\pi i}s_\infty\delta.
                                                        \tag{RT.17}
\]
The reference F0 here is the actual extending cap-annulus map
constructed in RCZ.5, with its complete integral period, d-delta
cochain and reduced Cartier correction. Its construction is over
the full v-disc on that cap annulus. Source and root equations and
A0 are also holomorphic there, as RG.1 records. The ordinary toric
charts are the same fixed fan over the source annulus; all their
coefficient functions are retained. Compactness of the parameter
annulus permits one sufficiently small scalar annulus on which
these quotients and caps give the proper smooth family.

The positive r deck has the literal ordinary and cap arrows
q1^n and h^n, with h=1-T0(v)q_infinity. They commute with the
retained period maps and finite groupoid arrows. Their coefficients
are single-valued in v on this annulus. Thus (RT.17) is the same
independent-scalar construction used in RG.5, now on the source-zero
annulus; no scalar or source closing is replaced by an unmarked map.

Take r0^m=lambda0 and retain the actual base amplitude \(r_{\rm base}=v_*^k r_0\). The original loop is
\[
 v(t)=v_*e^{2\pi it},\qquad r(t)=r_{\rm base}e^{2\pi ikt}.
\]
On the real phase cover its path (t,kt) has the same endpoints as
the broken path
\[
 (\min(2t,1),\ k\max(2t-1,0)).
\]
Their straight interpolation, with the corner smoothed relative
the endpoints, is an explicit based homotopy in the actual parameter
torus of (RT.17). The first part of the broken path is the source
loop at constant \(r_{\rm base}\); the second is k root-scalar loops at the same
source basepoint. Their complete endpoint arrows compose to
q1^(kn),h^(kn), exactly the original forward arrows. The given root
norm A0^m=B0^n and the full F0 square remain in this homotopy.

Any further comparison to a different fixed scalar reference uses
a separate zero-winding radial path inside the common contracting
range, carrying the actual norm root and F0. No such amplitude change
is hidden in the phase-cover homotopy above.

Consequently the actual oriented sphere-return classes satisfy
\[
 Z_{\mathcal T}(k)=Z_{\mathcal T}(0)
                      +k A^{\rm scalar}_{\mathcal T}.   \tag{RT.18}
\]
This follows from the constructed family homotopy and the clutch
composition, before using the abelian identification with Z/28.
For the two reference/reflected vertical fans the current physical
scalar values are 0 in the good branch and 3p-1 in the reduced
branch, by K69/K72. Their equality on those two fans is the literal
n=0,1 comparison in that integer scalar proof.

Thus the factor c*lambda in a local constant-scalar study is
constant only after (RT.17)--(RT.18) separate its k actual scalar
turns. In the original family c*v^(km)*lambda0 still has its full
winding and zero. No extending logarithm for that factor is asserted,
and the unknown source-zero class Z_T(0) is not evaluated here.

## RT.13. A compact cut region with its two actual corner arms

We specify the compact region before making any end identification.
In the positive reduced chart put
\[
 H=|S_0|^2+|S_1|^2+|z|^2,\quad
 \rho^2=H|T_1|^2+H^2|V|^2,\quad
 R^2=(|S_0|^2+|S_1|^2)(|T_1|^2+|zV|^2).
                                                        \tag{RT.19}
\]
All three displayed combinations used below are invariant under
the full auxiliary complex action; rho is the actual Fubini--Study
disk-bundle norm on W. Choose r0>0 and epsilon>0 with
0<epsilon2/r0^2<1/4 and take
\[
       \mathcal A_{\varepsilon,r_0}
       =\{\rho\le r_0,\ R\ge\varepsilon\}\subset W.   \tag{RT.20}
\]
This is compact because it is closed in the proper disk bundle over
CP2. It is circle invariant. Its maps q and vtilde are the restrictions
of the actual invariant polynomials; the region makes no change to
those maps or the physical line.

Here is a direct regularity and corner calculation. Set
\[
 A=|z|^2/H,\qquad b=H|T_1|^2,\qquad c=H^2|V|^2.
\]
Then rho2=b+c and R2=(1-A)(b+Ac). On the sphere rho=r0 put
t=b/(b+c). Thus
\[
 \frac{R^2}{r_0^2}=(1-A)\{A+(1-A)t\}=:f(A,t).       \tag{RT.21}
\]
The derivative in the simultaneous fibre radial direction is
2R2, so R=epsilon is regular. On the radial sphere, the only
nonzero critical ratios of R2/r0^2 are 1/4 and 1. Indeed
partial_t f=(1-A)^2, so an interior critical point cannot occur.
On T1=0 the function is A(1-A), whose interior critical value is
1/4. On V=0 it is 1-A, with only endpoint critical values 0,1.
The remaining coordinate endpoints give 0 or 1. Consequently the
two faces in (RT.20) meet transversely. Their corner has the literal
equations rho=r0,R=epsilon, and may be smoothed by an invariant
rounding in these two regular defining functions.

The portion rho=r0,R<=epsilon has exactly two disjoint components.
Writing eta=epsilon2/r0^2 and
\[
 A_\pm=(1\pm\sqrt{1-4\eta})/2,
\]
the inequality f(A,t)<=eta permits only A<=A_- or A>=A_+.
For A>=A_+, increasing A to one decreases f; this component is a
tubular neighbourhood of the core over [0:0:1], with T1,V on their
unit three-sphere. For A<=A_-, decreasing both A and t decreases
f. To check the latter assertion on the allowed sublevel, substitute
t<=(eta-A+A2)/(1-A)^2 in partial_A f; its lower bound is
(1-A-2eta)/(1-A)>0. This component is a tubular neighbourhood of
z=T1=0, with V on the circle bundle O(-2) over P1.

The two core total spaces and their normal arrows are explicit.
At the first core, fix z=1. The core is S3 in (T1,V), the normal
coordinates are (S0,S1), and the physical weights are respectively
(+1,+1) and (-1,-1). At the second core, use V=1 with its actual
residual mu2. Its core is S3_(S0,S1)/mu2=RP3 and its normal disk
bundle is
\[
 (S^3\times D^4)/\{(S,c)\sim(-S,-c)\}.             \tag{RT.22}
\]
The physical weights in that gauge are -1/2 on the core coordinates
and +1/2 on the two normal coordinates (T1,z). Its principal circle
and physical line therefore retain charge two. No free quotient by
mu2 is removed from this description. The first core retains charge
one. Both corner arms are thus part of the compact comparison;
neither is silently replaced by an ordinary sphere cap.

The fixed trace on the radial sphere has z=V=0 and R=rho. It lies
outside these small-R arms. On (RT.20) it is an annulus in O(-1)
with boundary S3 at R=epsilon and rho=r0, carrying exactly the
normal frame (RT.9) on both ends. Its equivariant tube surgery can
therefore be performed on this annulus relative to both corners.
This produces a compact free-circle bordism between the indicated
pieces, with the two explicit arms still present. Closing those
arms by the full source-period, adjacent-node and finite-cap arrows
is the remaining global task. The identity inclusion of this region
preserves q,vtilde and the Cartier maps throughout.

## RT.14. The full node Cox space keeps the chamber sides visible

For chamber bookkeeping introduce homogeneous node coordinates
alpha,beta and write
\[
 S_0=A\alpha,\quad U=A\beta,\quad
 V=B\alpha,\quad T_0=B\beta.
\]
On (A,B,alpha,beta,S1,T1), the source auxiliary, node auxiliary
and physical weights are respectively
\[
 (1,-a,0,a-1,1,-1),\quad(-1,-1,1,1,0,0),\quad
 (0,-1,0,1,0,0).                                     \tag{RT.23}
\]
Fixing alpha=1 gives RT.8's primary chart. Fixing beta=1 gives
the complementary coordinates (U,w,S1,T1,T0) with source weights
(a,1-a,1,-1,-1) and physical weights (1,-1,0,0,0).
For a2 its positive chamber has the U=1 charge-two origin; its
negative chamber is the O(-1) plus O(-2) bundle over the CP2 of
the three negative coordinates. This is a statement of the actual
coefficient quotients, not an identification of their boundary sides.

In particular one cannot glue the two separately chosen positive
GIT quotients and infer a Hausdorff compact model. The explicit
sequence (S0,S1,T1,z,V)=(epsilon,0,0,1,0) tends to the charge-one
point in the primary positive quotient. In the complementary chart
it is (U,w,S1,T1,T0)=(epsilon,1,0,0,0). Source rescaling by
epsilon^(-1/2) gives (1,sqrt(epsilon),0,0,0), tending to its
charge-two point. Both limits would occur in that proposed gluing.
The actual compact construction must choose its common moment cut
and boundary sides explicitly. RT.20 retains just the stated
primary chamber and does not make this non-Hausdorff gluing.

## RT.15. The actual lower-arm spin structure and the charged overlap

The lower core in RT.22 is not supplied with an unspecified spin
structure. It is the actual boundary of the complex O(-2) surface
z=T1=0 in W. The source-auxiliary quotient (S0,S1,V), with weights
(1,1,-2), has the nowhere-zero canonical two-form obtained by
contracting dS0 wedge dS1 wedge dV with its Euler vector. On V=1
this is -2 dS0 wedge dS1; on S0=1 it is dS1 wedge dV. It extends
over the zero section of O(-2). Thus this crepant surface selects
its canonical complex spin structure and its induced boundary spin
structure on RP3.

Its normal complex two-plane has coefficient coordinates (T1,z)
and determinant frame dT1 wedge dz. The auxiliary weights sum to
zero on this normal determinant. On the double cover S3 its deck
is -I2 on these two coefficients. The determinant-one complex spin
lift acts by +1 on the even spinors Lambda^(0,even) and by -I2
on the odd spinors Lambda^(0,odd). The alternative lift would change
both signs and would not be this determinant-one reduction with its
displayed frame. In a complex-oriented Clifford basis it is
-e5e6e7e8, obtained from the trace-zero rotation angles (pi,-pi).
The base O(-2) surface has the analogous lift -e1e2e3e4. Their
product is
\[
             \omega_8=e_1e_2\cdots e_8.               \tag{RT.24}
\]
Equivalently the full charge-two chart C4/mu2 has deck -I4,
whose canonical complex spin lift is +1 on every even-degree
spinor and -1 on every odd-degree spinor. This is omega8, not its
negative. It has order two. These formulas specify the actual
torsion spin matching, rather than deriving it from rational
characteristic classes.

The same lift is visible directly in the total Cox volume. In the
primary order (S0,S1,T1,z,V), contraction of the five-variable volume
by the auxiliary Euler vector descends because its total weight is
zero. On V=1 it is
\[
       -2\,dS_0\wedge dS_1\wedge dT_1\wedge dz.       \tag{RT.25}
\]
The complementary U=1 chart has the contracted volume
2 dw wedge dS1 wedge dT1 wedge dT0. The literal adjacent-node map is
\[
 (U,w,S_1,T_1,T_0)\longmapsto
 (S_0',S_1',T_1',z',V')=(Uw,S_1,T_1,UT_0,U^{-1}).    \tag{RT.26}
\]
Its inverse is U=(V')^-1,w=S0'V',T0=z'V'. The five-dimensional
Jacobian is -1, and the auxiliary Euler vector is preserved.
The full q=UwT0 and vtilde=q-S1T1 are unchanged. This carries the
complementary-positive U-stable part to the primary-negative
V-stable part, retaining that boundary side.

After the actual U=1 and V'=1 gauges, (RT.26) is the identity on
the four charged coordinates (w,S1,T1,T0). The two contracted
volumes differ by the constant -1; its determinant root may be
taken as the fixed constant i. It has no loop-dependent choice on
RP3. The map commutes with the actual diagonal mu2 deck, so its
canonical complex spin-c map commutes with the deck action on
all even and odd spinors in (RT.24). This proves that this charged
overlap carries the specified spin structure. The global parameter
spin lift still requires composing the retained endpoint maps;
no independent sign is inserted at this overlap.

For the retained physical rescaling d(q,v), put eta=Wc in the
charged coordinates, with W=diag(-1,-1,+1,+1), allowing the actual
half-weights on the mu2 cover. Its derivative is its diagonal
linear part times I+eta tensor dlog d. The functions q,v are
invariant, so dlog d(eta)=0. This rank-one factor has determinant
one, its square deviation is zero, and I+s eta tensor dlog d is
an explicit invertible contraction. The linear factor has complex
determinant one because the four weights sum to zero.

For a full physical 2pi turn the four complex angles on the cover
are (-pi,-pi,+pi,+pi). Its Spin8 endpoint is exactly omega8,
the canonical mu2 deck already used in (RT.24). It therefore closes
on the actual quotient spin bundle. The two choices of the scalar
square root differ by that same deck, rather than by a freely
chosen other spin structure. Source/line units with extending
logarithms use their actual continuous lifts from the chosen
reference. A nonzero parameter winding of c*lambda is retained
until the actual scalar separation RT.12 is applied.

To compare with the physical positive-weight Hopf model, conjugate
the two negative complex coordinates S0,S1. This is the real
orientation-preserving constant map with Spin8 representative
e2e4. It commutes with omega8. Consequently the positive-Hopf
description preserves the same total spin lift and the physical
charge-two line. The individual base and normal physical spin
paths need not each close: each differs from its canonical deck
by a sign after the 2pi turn, and those two signs cancel in the
total lift (RT.24). They must not be discarded separately.

Finally the fixed S3 tube uses exactly (RT.9), hence the smooth
complex lines O(-(a-1)E),O(-aE) in (RT.11). The cap spin structure
there is the one transported by this actual coefficient frame;
S3 has no alternative H1 spin choice. The preceding Cox volume
extends over the fixed-tube complement, carrying the base and
normal determinant frames together. This verifies the local
fixed-tube/charged-overlap spin dictionary. It does not replace
the outstanding cyclic source reset or assign the global
order-two return from the local spin calculation.

## RT.16. The whole fixed trace, its actual cap clutches, and the index

We keep the whole surface F=Bl(P1_s times D_v), including its
exceptional disk. No copy of the local fixed-S3 handle of RT.9 is
inserted in this calculation. Let Y=boundary F=S2 times S1, with
its complex boundary orientation. Put c(v)=sqrt(1+v), on the actual
branch equal to one at zero. The marked coordinate

\[
 Z=(s-c(v))/(s+c(v))
\]

is induced by the full matrix ((1,-c),(1,c)); its determinant 2c
is nonzero on the whole parameter disk. Thus this is an extending
Mobius map on the unblown P1 family, not a replacement of its
parameter loop by a constant matrix. It takes D+ to zero and D-
to infinity. The blowup centre lies on D- and not on D+.

Cap by a second P1 times disk using this actual boundary coordinate.
Write C for this cap with orientation chosen so that its boundary
is Y. Equivalently, -C has the complex orientation of the second
parameter chart w=constant/v. The closed oriented surface F-C is
the complex blowup of P1 times P1. Let H and B be respectively the
two factor classes, and retain E for the exceptional class. Then

\[
 H^2=B^2=0,\quad H B=1,\quad E^2=-1,\quad
 H E=B E=0,\qquad \sigma(F-C)=-1.                 \tag{RT.27}
\]

In the first parameter disk the actual divisors have classes
D+=H and D-=H-E. The positive spinor of the physical normal
model is the same tensor sum carried in RT.1 and RT.9:

\[
 O(D_+)\otimes O(-aE)\ \oplus\
 O(-D_-)\otimes O(-aE).                           \tag{RT.28}
\]

The tensor factor is the actual source line. At a=2 this statement
includes the source and target Cartier r maps, not just the tensor
line's divisor class. The full F0 cap maps act on its nonzero
coefficients. The negative normal coefficient is conjugated by the
same physical positive-weight arrow as in K68; no line dual is
silently substituted.

Here is how all parameter and cap clutches are retained on the
second disk. Give its two summands the reference divisor frames
of O(H) and O(-H), in the displayed Z coordinate. On Y compare
them with (RT.28), transported by the actual source/Cartier/F0
maps and the actual Cox normal frame. Denote the resulting two
nonzero coefficient ratios by g+ and g-. They are functions on
Y because the common O(1) and O(-1) point transitions cancel.
In a finite s chart these are the ratios of the reference frames
1/(s-c) and s+c to the actual frames of (RT.28), including their
full source-line coefficient and normal units. At their divisor
points the same ratios are taken in the alternate Cartier chart;
the ratios agree, so no zero or pole is introduced at D+ or D-.
The finite character of the cap is part of these ratios. Its
constant value is not replaced by one.

Use the frame convention e_cap=g e_F. Define the two actual
integers by

\[
 w_\pm={1\over2\pi i}\int_{\{p_*\}\times S^1}
                              g_\pm^{-1}dg_\pm .   \tag{RT.29}
\]

Here p* is a regular point in the marked sphere, away from the
Cartier charts' divisor points. The integer is independent of p*
because g is a nonzero function on the connected product Y.
The direction of (RT.29) is fixed as follows: e_cap=v e_F is
the actual transition of O(1) on the doubled parameter sphere,
so a winding w contributes +w B. This also fixes the sign of
the base classes below.

There is an exact smooth line map reducing this clutch to its
displayed integer without losing the rest of the map. The ratio
g exp(-i w theta) has zero class in H1(S2 times S1;Z), and
therefore has a single-valued smooth logarithm h. Extend h over
S2 times the cap disk by the parameter-disk Poisson extension,
with a collar interpolation preserving its boundary value. Changing
the cap frame by exp(-h) gives precisely exp(i w theta) on Y.
This is a nonvanishing frame change on that specified cap. It
does not change the original F0, source or normal map on the first
piece. In particular it does not declare either w to be zero.

It follows that the actual capped spinor is isomorphic, with these
boundary arrows retained, to the sum of lines with Chern classes

\[
 l_+=H-aE+w_+B,\qquad
 l_-=-H+(1-a)E+w_-B.                               \tag{RT.30}
\]

Consequently, for b=c1(E_spin) and c2=c2(E_spin),

\[
 b=(1-2a)E+(w_++w_-)B,\qquad b^2=-(1-2a)^2,
\]
\[
 c_2=-a(a-1)+(w_--w_+).                            \tag{RT.31}
\]

Thus even the unequal normal-clutch windings have been retained;
their cross term occurs in c2. The determinant has no H term,
which is the precise reason there is no B cross term in b squared.
The local canonical complex spin-c arrows, their determinant
lifts on the charged collars, and the physical line are those
of RT.15 and EA.13. The cap construction carries those actual
bundle maps. It makes no additional choice of a spin character
on the lower RP3 arm.

For completeness the characteristic cancellation is obtained from
the physical line itself. On P(E_spin) put h=c1(O(1)); the actual
physical nonzero-vector line is M=O(-1), hence x=-h. The same
Hopf coefficient map on both caps gives this line arrow. The
projective relation and fibre integrals are

\[
 h^2+b h+c_2=0,\quad \pi_*h=1,\quad
 \pi_*h^2=-b,\quad\pi_*h^3=b^2-c_2.
\]

The vertical complex tangent has Chern class 2h+b, so its first
Pontryagin class is b squared minus 4c2, pulled back from the base.
Thus the two physical characteristic numbers, with the stated
base and complex fibre orientations, are

\[
 k=c_2-b^2,\qquad
 \ell=-\langle p_1(F-C),[F-C]\rangle-b^2+4c_2,
\]
\[
 {4k-\ell\over24}
 ={\langle p_1(F-C),[F-C]\rangle-3b^2\over24}
 ={\sigma(F-C)-b^2\over8}={a(a-1)\over2}.           \tag{RT.32}
\]

Neither the normal c2 nor either actual clutch integer was set to
zero in this computation. The full source and finite-cap maps
enter (RT.29); their possible cross terms cancel by (RT.32).

## RT.17. The two actual caps and the fixed-boundary correction

The outside Jin completion uses its actual product cap
C0=D3 times S1, with boundary Y and the retained Cox/Hopf normal
coefficient frame. Its normal bundle and its physical line are
the ones specified by that frame. They are not replaced by the
reference divisor frame used to calculate (RT.30).

The actual boundary arrow defining this cap is the following.
Use the full TL.1--3 node/Cartier map to the selected fixed-edge
charts of current Tate T0. In the boundary parameter annulus their
native coordinate is the displayed Z, and their two linear normal
coordinates have overlap c_i'=Z c_i and physical weights (-1,+1).
The units in TL.11 and the degree-two r arrow are included in
these coefficient maps. This is the literal two-cone fixed-star
chart, not a statement obtained from its normal degrees alone.
An actual nonzero chart unit on this annulus has the exact form
v^d exp(h); its integer d and its full coefficient are retained.
On each of the two physical weight lines, the linear normal
automorphism over the compact fixed P1 is a scalar function of
the parameter, because H0(P1,O)=C. The higher normal terms are
carried to their linear maps by equivariant normal rescaling on
a common smaller tube. The rescaling is the identity on the zero
section and is followed by its collar isotopy, so it carries the
original line and annular maps rather than discarding them.

In homogeneous unit Cox factors put

\[
 u=a_0+j a_1,\qquad v_N=c_0+j\overline{c_1},\qquad
 h=u i u^{-1},\qquad q_H=u v_N.                    \tag{RT.33a}
\]

The auxiliary circle cancels in q_H. Choosing a Hopf representative
of h and putting v_N=u^{-1}q_H is its explicit inverse. On the
finite Z chart it is the normalized expression
(1+jZ)(c0+j conjugate(c1)). These are exactly the first-resolution
products of K23, equations SF.5--6 of
part3_source_cusp_fixed_edge_working.md, applied here to the actual
TL fixed-star coefficient maps. Their formulas are independent of
which source supplied those maps. At nonunit normal radius the
same expression is real linear in the normal vector and sends
zero to zero. Thus it identifies the entire small normal tube,
not just its link. The physical action is
q_H -> q_H exp(-i phi), with its actual character.

All parameter powers act through their actual Cox coefficients
in (RT.33a). They are single-valued integer powers on this annulus.
This yields a periodic normal product over the parameter circle;
it does not claim that its comparison to a different product
extends over the cap. That comparison is the normal clutch on
the S4 in (RT.33), and is retained below. The underlying sphere
coordinate change has the literal extension

\[
 P\longmapsto A_{c(v)}P A_{c(v)}^*/
                    \operatorname{tr}(A_{c(v)}P A_{c(v)}^*),
 \qquad A_c=\begin{pmatrix}1&-c\\1&c\end{pmatrix},  \tag{RT.33b}
\]

on the trace-one positive-Hermitian three-ball. Its denominator
is positive, its inverse uses A_c inverse, and its boundary map
is exactly Z. Holding the actual q_H coordinate fixed gives the
product cap arrow (P,q_H,v)->(B_c(P),q_H,v). It is the explicit
K42 SP.13/K68 physical-circle cap arrow, now with the extending
c(v) and the actual TL/Cox coefficient product. It preserves
the physical line and normal orientation. No tangent derivative
is substituted for this product arrow.

The two cap choices have the exact closed base

\[
 S_4=C-C_0
     =(S^2\times D^2)\cup_{S^2\times S^1}
                        -(D^3\times S^1)\cong S^4, \tag{RT.33}
\]

with the orientations chosen above. The last map is the rounded
boundary of D3 times D2; its two product faces are precisely the
two written caps, with their opposite boundary orientations.
Their actual normal coefficient maps along Y define the normal
bundle on this S4 by gluing, including every difference of the
Cartier and Cox frames. The induced physical Hopf line is the
tautological O(-1) on its projectivization. There is no unrecorded
circle gauge: the coefficient ratios on Y are the same g functions
as above, and a circle gauge's S1 degree extends on C0 because
H1(C0;Z) maps isomorphically to H1(Y;Z).

There is an explicit bordism implementing this cap replacement.
Take the products of F,C,C0 with intervals and join their boundary
collars by Y times a triangle, one interval product on each edge.
Use the three boundary identifications furnished by the actual
normal frames; the third is the inverse composite of the first
two. They therefore extend over this collar triangle. Rounding
its product corners gives a compact oriented five-dimensional
base bordism with the three closed four-dimensional faces
F-C0, F-C and C-C0. The normal bundles glue on the same products,
and projectivizing gives the required sphere-bundle bordism with
the physical line. This proves the literal cycle identity

\[
 [B_{F-C_0}]=[B_{F-C}]+[B_{S_4}]                 \tag{RT.34}
\]

with the retained normal maps, rather than only an equality of
intersection forms. A nonzero third-class normal clutch may be
present on S4. Its c2 is carried by this construction. Applying
the same formula (RT.32) gives index zero, because H2(S4)=0
and its signature is zero. The c2 term cancels explicitly.

Deleting the entire fixed tube in the global orbit construction
therefore supplies -B_(F-C)-B_(S4). The exceptional E remains
in the first base. This is the fixed-cap part of the boundary
ledger; it must be combined with the finite-period face chain
and the actual outside/Jin arrow before a global return is assigned.

The additional exact certificates are
code/part3/source_zero_cut_spin.py (67 local cut, charged-overlap,
Clifford and spinor identities) and
code/part3/source_zero_fixed_cap.py (462 whole-cap identities,
including arbitrary retained w+ and w-). Their JSON and captured
outputs retain these local scopes. The fixed-cap program's first
JSON serialization error is preserved under
records/attempts/source_zero_fixed_cap_json_types; all its
mathematical assertions had completed, and the repair converts
only SymPy output integers to native JSON integers.
