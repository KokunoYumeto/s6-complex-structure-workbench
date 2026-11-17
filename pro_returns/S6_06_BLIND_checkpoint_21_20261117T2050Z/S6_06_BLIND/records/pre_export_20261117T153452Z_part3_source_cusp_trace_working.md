# Selected-cusp double source loop: actual trace and line comparison

Proved as P3F.56 after root and independent geometric audits. This file concerns only the
twofold marked closure of P3F.54, with the III-star cap and no logarithmic
disc on either member of the coalescing finite-node pair. The source scalar
is fixed and sufficiently small. Use the standard vertical-edge fan of F41,
whose physical circle has the fixed sphere used below. The value for another
fan is not inferred without its actual framing comparison. This proof does
not replace this source loop by
a scalar loop. The local lifted-link invariant is the separately computed
P3F.55; the purpose here is its actual geometric transfer.

## SC.1. The exact normalization and the ordered critical-value braid

Retain the F54 functions and put
\[
 a(u)=u+u^{-2}=\rho^2,\qquad u(0)=u_*,\quad u_*^3=-1.
\]
The selected fibre is at \(q=t-t_0(u)=0\). In the actual source-parameter
threefold, the coordinates \((X,y,\rho)\) are smooth coordinates and
\[
 q=\frac{y^2-X^2(X+\rho^2)}{X+u(\rho)}.                 \tag{SC.1}
\]
The entire selected rational fibre is normalized by
\[
 f(s,\rho)=\bigl(s^2-\rho^2,
                    s(s^2-\rho^2),\rho\bigr).         \tag{SC.2}
\]
At \(s=\infty\) this is the zero-section point, so its domain is
\(N=\mathbf P^1_s\times D_\rho\). Its two preimages of the node are
the actual sections
\[
 D_+=\{s=\rho\},\qquad D_-=\{s=-\rho\}.              \tag{SC.3}
\]
They meet only at \((s,\rho)=(0,0)\).

The derivative minors of (SC.2) are
\[
 2s,\qquad 3s^2-\rho^2,\qquad
                      2\rho(s^2-\rho^2).
\]
Their ideal is \((s,\rho^2)\). Thus \(f\) is a complex immersion off
the origin. Its only distinct double pairs there are
\((\rho,\rho)\) and \((-\rho,\rho)\): equality of the last and first
coordinates first gives the same \(\rho\) and \(s'=\pm s\), and equality
of the second then gives \(s(s^2-\rho^2)=0\).

The two nearby critical values of (SC.1) can also be read without a
change of the base coordinate. Besides \(X=0,y=0\), the second critical
point is \(X=aR(a),y=0\), where
\[
 2aR^2+(a+3u)R+2u=0,\qquad R(0)=-2/3.
\]
The implicit derivative in \(R\) is \(3u_*\ne0\). Its actual critical
value is
\[
 q_1(\rho)
   =-\rho^6\frac{R(\rho^2)^2(R(\rho^2)+1)}
                    {\rho^2R(\rho^2)+u(\rho)},\qquad
 \frac{q_1(\rho)}{\rho^6}\longrightarrow-\frac4{27u_*}.
                                                               \tag{SC.4}
\]
The remaining critical point stays outside this small source chart.
For one positive \(\rho\)-loop the ordered pair \((0,q_1)\) therefore
has six positive full turns of its difference. In the convention that
the positive generator \(\sigma\) of the two-point braid group is a
positive half turn, this is exactly \(\sigma^{12}\).

Here is the retained Hurwitz convention. For an ordered pair of positive
Picard--Lefschetz twists \((g,h)\), the right Hurwitz action is
\[
 (g,h)\cdot\sigma=(h,h^{-1}gh).
\]
Writing \(C=gh\), direct multiplication gives
\[
 (g,h)\cdot\sigma^{2j}
       =(C^{-j}gC^j,C^{-j}hC^j).                    \tag{SC.5}
\]
The two vanishing arcs are adjacent arcs between the three roots of the
cubic in (SC.1). Their lifts to its double cover meet once. The local
regular fibre is the double cover of a disc branched at these three
points, hence a once-punctured torus. The positive twists are the lifts
of the two positive adjacent half twists. The braid
\((\sigma_1\sigma_2)^3\) is one full turn of the three branch points.
Its lift rotates the inner boundary coordinate by half a turn, because
the boundary covering has degree two. Squaring it gives the actual
boundary twist:
\[
                        (gh)^6=T_{\partial}.        \tag{SC.6}
\]
For example, on a boundary collar with covering angle
\(\vartheta=2\widetilde\vartheta\), the base twist
\(\vartheta\mapsto\vartheta+2\pi\chi(r)\) lifts to
\(\widetilde\vartheta\mapsto\widetilde\vartheta+\pi\chi(r)\);
its square is the positive boundary twist of the lifted collar.
This is the boundary map, not merely the order-six homology matrix.
Thus (SC.5) retains conjugation by \(T_{\partial}^{-1}\) after the
positive \(\rho\)-loop. The ordered vanishing curves return because the
boundary twist is central, while the boundary twist itself is retained.
The weighted chart rotates the three cubic roots twice and has the
opposite, inner-to-outer boundary arrow \(T_{\partial}\). These two
arrows are the same gluing relation read in opposite directions.

## SC.2. The explicit compact pencil and its plumbing

The substitution
\[
 X=\rho^2\widetilde X,\qquad
 y=\rho^3\widetilde Y,\qquad q=\rho^6Q
\]
is the \(\rho\)-chart of the weighted blowup of the smooth coordinates
\((X,y,\rho)\) with weights \((2,3,1)\). The complete equation is
\[
 \widetilde Y^2=\widetilde X^2(\widetilde X+1)
                    +Q\bigl(u(\rho)+\rho^2\widetilde X\bigr).
                                                               \tag{SC.7}
\]
On the exceptional weighted plane \(\mathbf P(2,3,1)\), with coordinates
\([X:Y:R]\), the actual pencil is
\[
 Q=[Y^2-X^2(X+R^2):u_*R^6].                          \tag{SC.8}
\]
The constant base unit \(u_*\) is retained.

Its only base point is the smooth point \([1:1:0]\). In local coordinates
\(R,z=Y^2-X^2(X+R^2)\), the ideal is \((z,R^6)\). The six successive
blowups with charts \(z=R^jz_j\), \(j=1,\ldots,6\), resolve the
pencil. The first five exceptional curves are in the infinite fibre,
with multiplicities \(5,4,3,2,1\); the sixth is its section. The proper
curve \(R=0\) has multiplicity six. The quotient point of order two on
this curve has the scalar \((1,1)\) chart; its resolution contributes a
single curve with multiplicity three. The order-three quotient has
weights \((2,1)\); the two regular rays have \(R\)-valuations
\(2/3,1/3\), and contribute multiplicities four and two, in that order
away from the central curve.

Every vertical curve has self-intersection \(-2\). For the central
curve this can also be checked before the point blowups: its weighted
self-intersection \(1/6\), minus the two resolution corrections
\(1/2\) and \(2/3\), is \(-1\); the first ordinary base-point blowup
makes it \(-2\). Each of the first five ordinary exceptional curves
is blown up once more, while the last section remains a \((-1)\)-curve.
Thus the infinite fibre is the literal affine \(E_8\) plumbing with
central multiplicity six and three arms
\[
 (5,4,3,2,1),\qquad(3),\qquad(4,2).                  \tag{SC.9}
\]
The finite discriminant of (SC.7) at \(\rho=0\) is
\(-u_*Q(4+27u_*Q)\), giving the two displayed nodal fibres. The compact
source pencil therefore has \(II^*+I_1+I_1\). Its integral intersection
matrix, including the last section, is unimodular of signature \(-8\);
the executed certificate supplies the integral basis consisting of the
fibre, section and the eight finite \(E_8\) roots.

The pullback of the original source Cartier line to this blowup and all
six further blowups is trivial near the exceptional pencil: both original
divisor sections avoid the source cusp point. This assertion is about
that literal pullback. It is not a substitution of the compact pencil
for the actual principal-circle line. The latter comparison is supplied
by the real trace below.

## SC.3. The actual ambient orbit product and the embedded trace

Choose a small base disc containing just the two coalescing finite
critical values, and a small source-parameter disc. On its boundary the
elliptic map is a submersion for every parameter. The source total family
is smooth, including the cuspidal member, and is proper with this boundary.
A horizontal field tangent to the boundary therefore gives a smooth
source trivialization over the parameter disc. The III-star cap and the
ordinary complement extend there by the actual full-coefficient maps of
F51/F54. These choices retain their original annular boundary marking.

The suspension translation also has a logarithm on this small base and
parameter polydisc. At the central cuspidal fibre its smooth group is
additive. Divide its central section value by a sufficiently large
integer, continue that division section by the inverse function theorem,
and take the small-group logarithm of this section. Multiplication by the
same integer gives a logarithm of the actual section. Exponentiating
\(t\) times it, \(0\leq t\leq1\), supplies an actual extending
translation isotopy. The invertible line lift obtained after dividing
the chosen Hom section by its base factor \(q\) has the same construction
in the line-extension group: its scalar unit has an analytic logarithm
on the polydisc. Thus this isotopy retains the source-line lift as well
as the source section.

Use this isotopy to untwist the source suspension. At the selected node
use the exact relative orbit product of P3F.9. Its local formulas
\[
 2b=r-|y_0|^2/r,\qquad
 2b'=|x_0|^2r-r^{-1},\qquad db'/db>0
\]
give a proper increasing gamma coordinate, fixed on the prescribed
outside collar. They identify the actual orbit body with the source
neighbourhood times its marked gamma circle. They are periodic on the
\(\rho\)-cover, since the ordered node coordinates return literally
by F54. The target source product exists also at \(\rho=0\). Gluing it
to the already extending exterior gives a smooth ambient orbit-body
family over the disc. We use its trivialization as \(Y\times D_\rho\).
No extension of the complex threefold at \(\rho=0\) is made here.

There is a global real gamma lift of the fixed-sphere graph on the whole
closed parameter annulus. The ordinary gamma coordinate is formed from
real logarithmic norms, divided by the positive logarithmic norm of the
contracting suspension. The source and invertible-line logarithms just
constructed extend across the full parameter disc. At the node the F9
coordinate is a proper real coordinate with positive derivative, fixed
relative to that ordinary coordinate. Its two endpoint values therefore
have a real lift, not only a circle-valued difference. The full \(\rho\)
closing has no gamma reindex: by F54 the two literal node transitions
\((Z,V)\mapsto(q_T/Z,V)\) compose to \((Z,V)\mapsto(Z,V)\).
A nonzero suspension deck power would change \(|V|\) by a nontrivial
power of its strictly contracting norm; hence it is not present in this
identity. The chosen gamma cell and its real coordinate return to
themselves. An increasing real change of the F9 coordinate, fixed on the
outer collar, puts the entire compact fixed graph in one common short
arc. This proves its zero parameter winding and supplies the real lift
used in the convex interpolation below. A scalar Cox-line gauge is a
different map and is retained in SC.4--SC.5.

The source projection of the fixed sphere is the actual normalization
(SC.2). Fractional source translations used in the suspension product
do not change this local normalization germ. Here is their exact
normalization map. If \(Z=(s-\rho)/(s+\rho)\) and a translation has
Tate multiplier \(g(\rho)\), with \(g(0)=1\) and
\((1-g)/\rho\) analytic, then
\[
 s\longmapsto
 \frac{(1+g)s+(1-g)\rho}
      {((1-g)/\rho)s+(1+g)}.                        \tag{SC.10}
\]
It is analytic at the origin, fixes \(s=\pm\rho\), and has invertible
derivative there. The same formula for the fractional multiplier
\(\exp(t\log g)\) provides the actual isotopy. The positive product
coordinate may be chosen in an arbitrarily short gamma arc. For an exact
quantitative check, write \(g_t=\exp(t\rho A(\rho))=1+\rho h_t\).
Formula (SC.10) gives
\[
 T_t(s,\rho)-s
       =\frac{h_t(s^2-\rho^2)}{2+h_t(\rho-s)}.       \tag{SC.10a}
\]
For bounded \(t\) with bounded first derivative, \(h_t\) and its
first derivative are bounded. Uniformly for \(0\leq\alpha\leq1\),
substitution of \(\alpha t\) gives
\[
 T_{\alpha t}=s+O((|s|+|\rho|)^2),\qquad
 D(T_{\alpha t},\rho)=I+O(|s|+|\rho|).
\]
On one sufficiently small common ball the error in the derivative has
norm less than one half. The maps are therefore injective diffeomorphism
germs, with positive real determinant, and the displayed isotopy fixes
both branches exactly. The height (SC.11) has bounded first derivative
off the origin. Inside the removed inner ball it can be cut off to the
smooth polynomial \(\operatorname{Re}(s\overline\rho)\), without
changing \(W\) or its inner boundary and with a bounded first derivative.
Thus the same estimate gives a smooth isotopy of actual germs.

To avoid circular use of this estimate, first lift the fixed graph to the
universal real gamma cover furnished above. In that cover its source
projection is the normalization itself. Perform the height interpolation
there, in the common arc of length less than one. Quotienting cannot
create a new identification by a nonzero gamma deck, since two heights
in that arc do not differ by a nonzero integer. Now untwist the
suspension by the fractional translation. Equation (SC.10a) is the
actual resulting normalization reparametrization and removes that
source shear by the explicit isotopy. This proves the use of (SC.2)
as the projected germ, with its marking retained.

The order of the two gamma heights is fixed by the charts, rather than
chosen afterward. The source branch \(y_0=0\) is \(s=-\rho\) and
occurs at the lower endpoint \(b=0\). The branch \(x_0=0\) is
\(s=+\rho\) and occurs at the upper endpoint \(b'=0\). The increasing
overlap identifies them in precisely this order.

On the local normalization put
\[
 H(s,\rho)=\frac{\operatorname{Re}(s\overline\rho)}
                  {\sqrt{|s|^2+|\rho|^2}}.          \tag{SC.11}
\]
It has the same strict ordering on the two branches. Multiplying by a
fixed small positive constant puts it in the chosen gamma arc. Extend
it with a cutoff over the rest of \(\mathbf P^1\). On a collar of the
outer parameter circle retain the actual gamma graph. Interpolate by
a convex combination on the intervening annulus. The difference of
the heights on every double pair remains positive. Away from those
pairs the source map is already injective. Hence this is an isotopy
through embedded graphs, with the actual outer trace unchanged.

Remove the small complex-oriented star-shaped four-ball specified below from \(N\), and call
the result \(W\). The map \((f,H)\), with the just specified outer
interpolation, is an actual smooth embedding of \(W\) in
\(Y\times D_\rho\), and its outer boundary is the actual fixed-sphere
trace with orientation \(F\times S^1_\rho\). Its inner boundary is the
lifted link of (SC.2).

Here is the literal inner boundary used in F55. Choose a small positive
\(\epsilon\), and remove from the normalization the star-shaped four-ball
\(B_f=f^{-1}(B^6_\epsilon)\). Its boundary is exactly
\(L_\epsilon=f^{-1}(S^5_\epsilon)\). The norm square of \(f\) is
strictly increasing on every positive domain ray, so this is a smooth
three-sphere with its stated complex boundary orientation. A smooth
radial interpolation, fixed near a smaller Euclidean ball, identifies
\(B_f\) with a four-ball without changing its boundary orientation.

Choose the ambient inner seven-ball to be the rounded product
\(B^6_\epsilon\times[-2\eta\epsilon,2\eta\epsilon]\), with
\(\eta H\) as height. Indeed \(|H|\leq|\rho|\leq\epsilon\) whenever
\(\|f\|\leq\epsilon\); thus the embedded graph misses the two flat
caps and every rounded corner. Its intersection with the boundary is
literally
\[
 (f,\eta H):L_\epsilon\longrightarrow
                 S^5_\epsilon\times(-2\eta\epsilon,2\eta\epsilon).
                                                               \tag{SC.11a}
\]
This boundary is the smooth six-sphere obtained by rounding the product
of a six-ball and an interval. In its cylindrical chart, use precisely
the orientation-preserving stereographic map \(\psi\) of F55. Equation
(SC.11a) is then exactly \((\psi f,\eta H)\), with its prescribed
ordering. The chart is an actual open chart of this six-sphere; shrinking
a compact subchart by its radial coordinate gives the usual chart
comparison, through embeddings. No comparison of two different radial
projections is required. The weighted radial construction of the first
draft is retained in the attempts record; the present product-ball map
supplies the missing literal boundary identification.

## SC.4. The extending normal spinor and actual Hopf circle line

The finite-base source has a nowhere-zero holomorphic two-form. In the
coordinates (SC.1), its residue expression is a nonzero holomorphic
unit times \(dX\wedge dy\). Together with \(d\rho\) it trivializes the
ambient complex determinant along the normalization. The complex normal
line of the immersion (SC.2) on \(W\) is consequently
\[
 L=N_f\cong\mathcal O(-D_+-D_-).                     \tag{SC.12}
\]
This is a determinant isomorphism, not merely a degree equality. In the
finite coordinate chart its normal covector is the explicit cross product
\[
 (3s^2-\rho^2)\,dX-2s\,dy
                    +2\rho(s^2-\rho^2)\,d\rho.     \tag{SC.13}
\]
It is nonzero everywhere on \(W\) in this chart. Changing to the
infinite normalization coordinate gives the \(\mathcal O(-2)\)
normal transition. The divisor identity
\(\operatorname{div}(s^2-\rho^2)=D_++D_--2\{s=\infty\}\)
gives the displayed actual isomorphism (SC.12).

The normal bundle of the real graph is isomorphic to
\(L_{\mathbb R}\oplus\mathbb R_\gamma\): quotient by its tangent
graph gives the identity on the source normal two-plane and the gamma
coordinate, with only a triangular shear. Its linear contraction is
the precise graph-normal comparison. Retain the same constant orientation
change as in the positive-Hopf convention of K7.

Define the rank-two complex spinor bundle
\[
 E=(\mathcal O\oplus L)\otimes\mathcal O(D_+)
       =\mathcal O(D_+)\oplus\mathcal O(-D_-).        \tag{SC.14}
\]
Its determinant is \(\mathcal O(D_+-D_-)\), trivialized by the literal
Cartier ratio \((s-\rho)/(s+\rho)\). Thus \(E\) is an actual
\(SU(2)\) bundle, and
\[
 \operatorname{ad}E\cong
              \mathbb R\oplus L_{\mathbb R}.        \tag{SC.15}
\]
The off-diagonal summand is exactly
\(\operatorname{Hom}(\mathcal O(D_+),\mathcal O(-D_-))=L\).
Its Hopf sphere bundle carries the meridian-one Thom line U with
determinant class b=0. The physical nonzero-vector line M is its dual:
in the literal normal chart (v,z), the positive spinor is (bar v,z),
whose physical circle is the unit circle of the tautological line.
The actual outward normal meridian has its projective complex orientation,
so that physical line has degree -1. The Hermitian dual map supplies
the degree-one Thom line and inverts its circle character. P3K.68
gives this complete coordinate and orientation computation.

This identifies the actual outer physical circle line and its meridian-one dual; their characters are retained separately. In the normalization coordinate
\(Z=(s-\rho)/(s+\rho)\), the two Cox normal coordinates have transition
\(c_i'=Zc_i\) and physical weights \((-1,+1)\). Conjugating the
negative-weight coordinate gives the unitary transition
\[
       \operatorname{diag}(\overline Z/|Z|,Z/|Z|),
\]
which is precisely that of (SC.14), after the explicit Hermitian
identification of the conjugate tautological line with its dual. It
intertwines the physical circle actions. The quaternion formula
\[
 q_{\rm H}=(1+jZ)(c_0+j\overline{c_1})
\]
is the same formula as K30; its second-chart expression gives the
identical vector. The ratio \([s-\rho:s+\rho]\) is a genuine map from
\(W\) to \(\mathbf P^1\), since its only common zero was removed.
Consequently this Cox/Hopf identification extends over all of \(W\),
including the inner link, with the original ordered branch marking.

The pullback of the source Picard line to
\(\mathbf P^1\times D_\rho\) has degree zero on every normalization
fibre and hence is a line from the parameter disc. Rigidifying it along
the zero section gives a literal trivialization. The source-line unit
in the suspension isotopy above is retained in this trivialization.
It contributes the same extending scalar gauge on both sides of
(SC.14). No degree-zero line or scalar winding is discarded.

The circle line also extends on the whole excision complement; this
does not follow just from constructing its restriction to the normal
sphere bundle. Put \(Z'= (Y\times D_\rho)\setminus\operatorname{int}B^7\).
It has \(H^2(Z';\mathbb Z)=H^3(Z';\mathbb Z)=0\). The codimension-three
Thom sequence of the properly embedded connected \(W\) therefore gives
\[
 H^2(Z'\setminus W;\mathbb Z)\xrightarrow{\ \cong\ }
             H^0(W;\mathbb Z)=\mathbb Z.             \tag{SC.15a}
\]
The isomorphism is evaluation on the oriented normal meridian. Choose
the line with meridian value one. On the outer complement the actual
meridian-one dual U has this value, and \(H^2\) of that complement is also
\(\mathbb Z\): each fibre is the complement of the unknotted \(S^2\)
in \(S^5\), with \(H^1=0,H^2=\mathbb Z\), and the oriented return
preserves its generator. The Wang sequence has no other degree-two
term. The ratio of the two lines is therefore topologically trivial;
multiplication by a chosen nonzero section of that ratio is the actual
boundary bundle isomorphism. It retains the stated dual circle character.

Furthermore restriction
\(H^2(S(\nu W))\to H^2(S(\nu W)|_{F\times S^1})\) is an isomorphism:
it is an isomorphism both on the base \(H^2\) and on the meridian
summand of the sphere-bundle sequence. Thus the restriction of the line
in (SC.15a) is exactly the line (SC.14), whose outer identification was
just given in Cox coordinates. In particular its determinant class on
\(W\) is zero. On the inner link it is the same oriented meridian line.
Possible boundary isomorphisms differ by circle-valued gauges; their
outer parameter winding is extended over the specified
\(D^3\times S^1\) cap below. This retains that winding rather than
assuming it vanishes in the excision complement.

## SC.5. Excision, its zero-index correction, and the transfer sign

Take a small seven-ball around the local lifted germ inside
\(Z=Y\times D_\rho\); its boundary contains the inner embedded
three-sphere \(e\). Remove the normal disc bundle of \(W\) from the
remaining ambient cobordism. Attach the product surgery collar
\((D^3\times S^1)\times S^2\) on the outer side, as in K7, and the
\(D^4\times S^2\) collar on the inner side. The outer closed boundary
is the actual physical mapping torus \(P_f\) after fixed-sphere
replacement. The inner closed boundary is the surgery manifold
\(N_e\) of the actual embedded link, with the same meridian line.
The further boundary is the normal sphere bundle over
\[
 \overline W=W\cup(D^3\times S^1)\cup D^4
       =(S^2\times D^2)\cup(D^3\times S^1)
       =\partial(D^3\times D^2)\cong S^4.            \tag{SC.16}
\]
These are the literal boundary identifications from the construction;
the two caps are not exchanged by an unspecified change of marking.

The varying outer normalization coordinate also has an explicit cap
extension. On the outer parameter circle put
\[
 A_\rho=\begin{pmatrix}1&-\rho\\1&\rho\end{pmatrix},
 \qquad Z=A_\rho\cdot s=\frac{s-\rho}{s+\rho}.
\]
Represent the closed three-ball by positive semidefinite Hermitian
two-by-two matrices \(P\) of trace one. Its boundary consists of the
rank-one matrices and is \(\mathbf P^1\). The exact ball map is
\[
 \mathcal B_\rho(P)
       =\frac{A_\rho P A_\rho^*}
                    {\operatorname{tr}(A_\rho P A_\rho^*)}.
                                                               \tag{SC.16a}
\]
Its inverse uses \(A_\rho^{-1}\). The denominator is positive on the
closed ball, so both maps are smooth there. On its boundary it is
exactly the displayed Mobius map. The matrix \(A_\rho\) is periodic
on the actual parameter circle, so this ball map closes literally even
when the associated projective loop has nontrivial fundamental-group
class. The source reparametrization isotopies of (SC.10a) extend as
well: extend their time-dependent sphere vector fields over a boundary
collar of the ball using a radial cutoff, and integrate them. These
extensions are periodic in the parameter. Composing them with
(SC.16a) identifies the actual outer cap marking with the product cap
in (SC.16). Its normal clutch is carried along, not set to zero.

The meridian-one dual U extends over both collars; the physical M extends by the inverse character. On the outer boundary
its class is the positive meridian class, by (SC.14); every possible
boundary gauge extends over \(D^3\times S^1\), since restriction is
an isomorphism on \(H^1\). On the inner \(S^3\) there is no
\(H^1\) gauge obstruction. Both normal bundles extend after choosing
their actual boundary framings; any resulting normal Pontryagin class
is retained. The extra sphere-bundle boundary has index zero, since its
base is (SC.16), \(H^2(S^4)=0\), and \(\sigma(S^4)=0\). The sphere-
bundle formula cancels the normal Pontryagin class and gives this zero
without a normal-framing assumption.

The orientations are the same two reversals as K7. The complex
orientation on \(W\) has outer boundary \(F\times S^1_\rho\) and
inner boundary the negative of the complex-domain link. The outer
boundary of \(Y\times D_\rho\) is \(-P_f\), and the excised inner
seven-ball supplies \(-N_e\). The remaining normal-sphere boundary
has zero index. Hence
\[
                         A(P_f)=-A(N_e).
\]
The actual positive family is Jin's mapping torus for \(f^{-1}\), so
\[
                         A_{U,\rm Jin}(f)=A_U(N_e).      \tag{SC.17}
\]

For an actual Seifert embedding of the lifted link in its six-sphere,
repeat the identical normal-tube excision, cap its boundary by \(D^4\),
and use the complex normal two-plane plus the radial real line. The
meridian line on the surgery boundary is the one in (SC.14); on the
three-sphere a line or its gauge has no additional class. The sphere-
bundle formula gives
\[
 A_U(N_e)=\frac{e(\nu V)^2-\sigma(V)}8
                      =H(e),                        \tag{SC.18}
\]
where the last equality is Takase's corrected Haefliger formula,
recorded in P3F.5. The normalization comparison with the invariant
computed directly in P3F.55 is its equations (CL.16)--(CL.19): an
actual punctured Kummer surface embedded in the oriented five-sphere
has signature \(-16\), trivial normal Euler class and value two
for both invariants. The exact Whitehead-to-Stiefel morphism and the
sign-refined immersed Seifert formula give that equality on this
nonzero element. The two group isomorphisms to \(\mathbb Z\)
therefore agree on every embedding. This supplies the sign bridge
used here.

The displayed local Seifert computation uses the meridian-one U
line. Its raw complex-plus-height orientation and the physical orbit
orientation are opposite; the outward-meridian-one line reverses at
the same time, so its U index is the displayed H(e)=1. The actual
nonzero-vector physical line M is U inverse. Therefore its odd
characteristic index in the same oriented Jin manifold is the negative.
The exact spinor arrow is anti-linear, not the previously written
linear swap: Cartier coefficients (a,b) map to g(x,y) overline(a,b)
in the right-complex Cox spinor. The globally defined quaternionic
anti-linear map commutes with all SU2 clutches and extends over both
cap products; its normal antipodal map and the dual circle character
are retained. P3K.68 gives every unit and both cap extensions.

The physical Hopf transfer has positive-line base -S2_z and y'=-y,
so its first and second pieces are -R,-L in the K23 plumbing order.
Its first-to-second clutch r maps to F(r); rewriting with L first
gives minus Sigma_(F inverse). The removed ball has the original
complex six-sphere as its outward boundary, and its free-face map is
the actual physical return, with the identity on the fixed tube.
Thus this is the actual clutched sphere. The meridian-one U transfer
instead has pieces +R,+L and is its orientation reverse. There is
no extra inverse after this explicit piece exchange.

Consequently the direct local calculation H(e)=1 gives
\[
 A_{U,\rm Jin}(f)=1,\qquad A_{M,\rm Jin}(f)=-1,
 \qquad[\Phi]=-1\in\Theta_7\cong\mathbb Z/28.          \tag{SC.19}
\]
The last equality is the physical-line oriented Hopf transfer of P3F.22, with the exact dual and piece maps of P3K.68. For the
forward physical return \(\Phi\), P3F.24 gives the literal cut-and-paste
identification
\[
 M_\Phi\cong(S^1\times S^6)\mathbin{\#}\Sigma_{-1}.
                                                               \tag{SC.20}
\]
Both spin structures have Eells--Kuiper invariant \(-1/28\), whereas
both spin structures of the product have value zero. Orientation
reversal changes the sign and still does not give zero. Consequently
this mapping torus is not diffeomorphic to the product, even without
an orientation requirement.

The loop in (SC.19) is one positive \(\rho\)-loop. Since
\(a'(u_*)=1-2u_*^{-3}=3\), the equation \(a(u)=\rho^2\) makes it
exactly two positive turns of the original marked source coordinate
\(u-u_*\). The scalar and all finite-cap choices stay fixed.

There is also an obstruction to smooth descent of this entire closed
family. Let
\[
 p:D_\rho^*\longrightarrow D_a^*,\qquad a=\rho^2,
                                                               \tag{SC.21}
\]
with \(u\) the analytic inverse of \(a(u)\) near \(u_*\). An oriented
smooth sphere bundle on \(D_a^*\) is obtained by cutting an annulus
along a radial interval and gluing its ends by an orientation-preserving
diffeomorphism \(\Phi_a\). Pulling this exact clutch construction back
along (SC.21) concatenates two copies of the interval; its closing map
is \(\Phi_a^2\). A change of fibre marking conjugates this map.
In \(\pi_0\operatorname{Diff}^+(S^6)\cong\Theta_7\) conjugation is
trivial because the group is abelian. Therefore an oriented smooth
bundle isomorphism from the actual \(\rho\)-family to such a pullback
would imply
\[
                -1=[\Phi]=2[\Phi_a]\quad\hbox{in }\mathbb Z/28.
                                                               \tag{SC.22}
\]
Reduction modulo two contradicts (SC.22). Thus this particular full
\(\rho\)-family does not descend as an oriented smooth bundle through
(SC.21). This does not exclude all conceivable one-turn endpoint maps:
it excludes exactly those that would give a descent of this specified
closed family.

No value for a different toric fan or another source-moduli puncture
is assigned by this proof.

Exact symbolic identities and the integral plumbing certificate are
saved separately in `code/part3/source_cusp_trace.py` and its outputs.

## Audit and preservation record

Root's full independent geometric audit passed the actual ambient
extension, normalization shear, circle line and spinor, both cap maps,
and the complete excision sign. The independent SC.3--SC.5 audits by
fourfold and checks passed the same maps. The final source-loop value uses the
separately audited P3F.55 Kummer normalization comparison. The complete
pre-promotion note and the earlier radial-link comparison are retained
in records and in the attempts file; no failed passage was discarded.


Physical-line correction, 2026-11-17T15:34:51.130110+00:00: original source/line proof preserved verbatim; P3K.68 replaces only the anti-linear coefficient and physical-transfer convention. The local link and all source/cap geometry remain.
