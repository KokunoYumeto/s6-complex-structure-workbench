# The actual shear quotient pieces and their Pontryagin pairing

Proved as P3K.63 after full root and independent blind_control audits,
17 November 2026. This
note concerns the selected-cusp positive rho loop and the physical
vertical-edge fans T_n of P3K.56. It retains the complete units, the
actual source and finite caps, and the specified Cox normal products.
The earlier SFIX note and its recorded attempts remain unchanged.

The target of this proof is the individual equality ell(T_n)=0. We do
not recover an integer Haefliger invariant from its residue modulo 28.
All completed mapping tori below first use the physical orientation;
the common parameter reversal at the end gives Jin's convention.

## SQ.1. The two actual quotient pieces

Write the original periods on the protected cusp disc as

\[
 h:(Z,V)\mapsto(\kappa qZ,\alpha V),\qquad
 B:(Z,V)\mapsto(gZ,\eta qV),\qquad Q=\kappa q.
                                                        \tag{SQ.1}
\]

The functions are the full ones in F54 and GF.1. On the positive rho
circle their windings are respectively -6,0,0,0. In particular g,
alpha and eta have their actual periodic logarithms. The new fan is
described by the exact character and period arrows

\[
 Z_n=Z,\quad V_n=Z^{-n}V,\qquad h_n=hB^n,\quad B_n=B.
\]

Their complete multipliers, including the ones with nonzero winding,
are

\[
 Q_n=Qg^n,\quad
 \alpha_n=\alpha\eta^n\kappa^{-n}g^{-n^2},\quad
 g_n=g,\quad\eta_n=\eta g^{-n}.                       \tag{SQ.2}
\]

Here h_n acts by (Q_n Z_n,alpha_n V_n) and B_n by
(g_n Z_n,q eta_n V_n). The coordinate q is unchanged. This is the
literal GF.1--3 arrow, rather than a change of the height character.

In this note gamma_n is the real coefficient of the contracting B.
The increasing F9 moment coordinate has the outward orientation
-gamma_n. We carry this explicit minus on both compared pieces;
we do not reverse the physical Hopf normal orientation.

Take the delta quotient of this cusp piece. The proof of F9 applies
in these new vertical characters. Its node charts are the actual
conifold quotient charts (x,y,b),(x,y,b'), with

\[
 2b=r-|y|^2/r,\quad 2b'=|x|^2r-r^{-1},\qquad
 \frac{db'}{db}=\frac{|x|^2+r^{-2}}{1+|y|^2r^{-2}}>0.    \tag{SQ.3}
\]

Its proper increasing outward coordinate -gamma_n is constructed relative to the
specified exterior coordinate, by the section and positive-vector-field
construction in F9. It is therefore a morphism over the actual source
node, with positive upper-triangular stable derivative. The same
construction with the complete positive norms of (SQ.2) is periodic
in rho: logarithms of positive norms are single-valued even when the
complex unit has nonzero phase winding. A phase of alpha_n is a delta
rotation in the line factor, so it is absent from this orbit coordinate.
It remains in the principal-circle line, which we compute below.

The source part of B has the periodic logarithm log g. Its translation
isotopy exp(t log g), together with its positive line-norm isotopy,
untwists the suspension exactly as in F9. Thus the actual orbit piece,
with its marked outer boundary, is

\[
                     W_n=E_n\times S^1_{\gamma_n},       \tag{SQ.4}
\]

where E_n is a compact nodal elliptic neighbourhood with Tate
parameter Q_n. This statement also describes its rho family. We use
the actual radial coordinate supplied by (SQ.3), and transport its
metric; we do not set the line phase alpha_n to one.

We compute the endpoint lift in this prescribed boundary marking.
Put \(L_Q=\log|Q_n|\), \(L_a=\log|\alpha_n|\), \(L_g=\log|g|\) and
\(L_S=\log|q\eta_n|\). On the regular annulus the actual real period
coefficients are obtained by inverting the absolute-value period matrix.
Its gamma coefficient is exactly

\[
 \gamma_n=
 \frac{L_Q\log|V_n|-L_a\log|Z_n|}{L_QL_S-L_aL_g}.
                                                        \tag{SQ.4a}
\]

For a sufficiently small common q disc the denominator is nonzero:
its leading term is \((\log|q|)^2\) and the remaining unit terms are
uniformly bounded on the compact parameter circle. Substitution of
h_n adds (L_Q,L_a) to the two logarithms, hence leaves (SQ.4a)
unchanged. Substitution of B adds (L_g,L_S), hence increases it by
exactly one. This identifies the actual lifts of both deck arrows.
In particular the continuation along the source normalization uses
zero gamma deck index under h_n. The n powers of B present in the
old expression \(hB^n\) have been canceled by the actual character
\(V_n=Z^{-n}V\); they cannot be added again as an endpoint integer.

In the square model whose two period directions are h_n and B,
cut the second nodal orbit circle at a free point. The F9 conifold
above its node is one line piece between the two adjacent free
ends of this cut. Over the source node its exceptional interval has
the exact representatives

\[
 z=\sqrt r,\quad v=0,\quad u=0,\quad w=1/\sqrt r,
                         \qquad0<r<\infty .             \tag{SQ.4b}
\]

Its fixed endpoints are r=0 in the first chart and r=infinity in
the second. They have b=0 and b_prime=0 respectively; the section
of F9 is r=1. On the line-factor nodal model the positive-weight coordinate is
u=Z_n V_n. The actual B multiplies it by q g eta_n, whose
norm is less than one after the chosen shrinking. Hence B runs from
the u branch toward the v branch, opposite to the increasing F9
moment direction. On this interval choose the correctly oriented
contracting-period coordinate

\[
 \gamma_n=\tfrac12-\epsilon\frac{r-1}{r+1},
                       \qquad0<\epsilon<\tfrac14.       \tag{SQ.4c}
\]

Thus its actual endpoint lifts are 1/2+epsilon and 1/2-epsilon.
In the first chart its derivative with respect to b at r=0 is
-4epsilon; in the second its derivative with respect to b_prime at
r=infinity is also -4epsilon. Thus the specified coordinate extends
smoothly with negative derivative at both fixed endpoints; its
outward negative has positive derivative, exactly as in F9.
They lie between the same two successive B translates. To verify
that cell statement, use the literal initial square in the new
characters: its source sides are identified by h_n, whose gamma
lift is zero by (SQ.4a), and its suspension sides by B, whose lift
is one. More explicitly, the two conifold endpoint charts are \(T^+_0\) and
\(T^-_0\). The fixed C_0 sphere uses \(T^+_0\) and
\(T^-_{-e_1}\); the latter is the h_n inverse translate of the
second conifold endpoint. Its gamma lift is unchanged by (SQ.4a).
Thus these are exactly the two endpoint lifts of the same fixed
normalization sphere. The small-resolution interval (SQ.4b) lies in the interior
of that one square and joins its two fixed branches; there is no
further period arrow on this interval. The two infinite half-lines
in the F9 quotient continue to the chosen free cuts in the
F9 increasing outward order. The full nonzero units change their positive
coordinates but not these deck indices or this order. In particular
no integer has been suppressed in (SQ.4c).

Extend (SQ.4c) to a proper decreasing coordinate on those half-lines,
and repeat it by gamma_n to gamma_n+1 on B translates. It agrees
with the prescribed real-period coordinate after a degree-one change in the marked circle orientation
on the overlap. Interpolate the lifted decreasing F9-coordinate
maps by their convex combination, with a partition equal to one
on the protected outside collar. All interpolating derivatives
remain negative in the F9 moment direction, and their lifts respect translation by one.
This is the explicit relative coordinate construction of F9, now
with its interval and its two endpoint indices specified. The
complete positive unit norms are periodic in rho; (SQ.4a) has no
rho reindex, so this relative construction is periodic as well.
On the remaining normalization cylinder choose its graph height
between these two values and match it by the same relative
increasing-coordinate construction. The source normalization is
one-to-one there, so these choices impose no further identification.
The h_n end identification has the zero lift already computed.

Consequently the complete fixed sphere graph has a real lift in the closed short arc
[1/2-epsilon,1/2+epsilon], with the two displayed endpoint values.
For two such graphs, their convex interpolation has endpoint
difference -2epsilon throughout; it never reaches any integer.
This is the endpoint verification needed in SQ.2, rather than an
inference from the existence of a real lift on a sphere alone.

## SQ.2. The actual source map, fixed tube and cap

Put \(L_g=\log g\), with the periodic branch just specified. Consider the
source family with

\[
                      Q_s=Q\exp(snL_g),\qquad0\le s\le1.
                                                        \tag{SQ.5}
\]

For this fixed integer n, shrink the protected q disc uniformly in s
and the compact rho circle so that all Q_s lie in the same Tate
annular range and no second critical value enters the disc.
Its nodal charts are \(xy=Q_s\). They are smooth total source charts,
since q times a unit is Q_s. Near the node the vector field

\[
                 \partial_s+nL_g\,y\partial_y           \tag{SQ.6}
\]

is tangent to this total space and keeps q and rho fixed. In this
formula the y derivative is taken in the displayed complex chart;
the real vector field is its underlying real derivative. It preserves
the node locus and the two branches. On the outside source torus
write a point as \(u+\tau_s v\) with u,v real modulo integers and
\(\tau_s=\log Q_s/(2\pi i)\). Prescribe the actual real marked-period map

\[
              u+\tau_s v\longmapsto u+\tau_0v.           \tag{SQ.7}
\]

It gives a smooth horizontal field on an outside collar. It respects
both monodromies: a q turn sends (u,v) to (u-v,v), and a rho turn
sends it to (u+6v,v); L_g is periodic. On the overlap, both fields
project to the same vector partial_s, keep q and rho fixed and are
tangent to the fibres. Their difference is vertical. A partition of
unity on the total source family, equal to one on a smaller node
neighbourhood and on the protected outside collar respectively,
therefore interpolates them in this affine space of horizontal
fields. No singular fibre is crossed by an untyped vector field.
The source is compact with its boundary, and the field is tangent to
that boundary. Its flow is consequently a diffeomorphism E_n to E_0,
periodic in rho and with boundary exactly (SQ.7). This flow, rather
than the generally nonsmooth real period formula at the node, is the
map used in the interior.

On the central normalization this flow is an orientation-preserving
sphere isotopy which preserves its two marked branch points. Transport
F_n by it. Its height and the height of F_0 are real functions in the
same short arc, and their two node-preimage values have the same strict
order. Their convex interpolation therefore remains an embedding:
the source normalization is injective away from that one pair, and
the two heights at the pair remain different. Extending the velocity
from this compact sphere to its tube and then by a cutoff gives an
ambient isotopy, relative the outside boundary. All data are periodic
in rho, so its vector field and flow are periodic as well.

We retain the normal arrow, not just the isotopy of the sphere. In
the branch notation x=s-rho,y=s+rho,Z=x/y, the shear spinor and its
Cartier morphism are precisely SFIX.5--8:

\[
 E_n^{\rm spin}=E\otimes\mathcal O(n(D_+-D_-)),\qquad
       E_n^{\rm spin}\longrightarrow E,\quad v\longmapsto Z^n v.
                                                        \tag{SQ.8}
\]

The source generators \(x^{-n-1}y^n,x^{-n}y^{n+1}\) go to \(1/x,y\).
Their determinant trivializations also match. The Hom of the two
summands and the adjoint normal bundle are thus carried by the
literal typed bundle isomorphism. The physical q equations
\(q=Zc_0c_1=Z^{-1}c'_0c'_1\) are retained; their differential is the
SP.11b normal arrow. The source flow contributes its actual derivative
and the graph interpolation contributes the positive triangular
graph-normal shear. They are families starting at the identity, so
their normal comparisons extend through the corresponding isotopies.
No phase of kappa is removed from a normal coordinate.

Use these arrows on the normal tube and extend the sphere isotopy to
the three-ball cap by its time-dependent boundary vector field with
a collar cutoff. On the Hopf sphere factor keep the adjoint arrow
of (SQ.8). This is exactly the product-cap construction SP.13 with
the transported base sphere, not a substitution of its tangent
derivative for the Cox frame. It supplies an oriented diffeomorphism
between the completed quotient pieces

\[
 C_n=\bigl(W_n\setminus\operatorname{int}(F_n\times D^3)\bigr)
                      \cup(D^3\times S^2)
                 \longrightarrow C_0 .                 \tag{SQ.9}
\]

It extends over the rho family. The circle line is carried separately
below; (SQ.8) retains its tensor factor rather than identifying two
unmarked circle lines.

## SQ.3. The exact boundary shear and the Euler line

On the boundary use real coefficients (u,v,d,gamma) of the marked
source vanishing period, source period h, physical delta period and
suspension period B. The source point before suspension untwisting is
u+tau v+G gamma, where exp(2pi i G)=g. The same point in the new
basis is

\[
 u+(\tau+nG)v+G(\gamma-nv).
\]

The full integral coefficient arrow, including the line character,
is

\[
 u_n=u,\quad v_n=v,\quad
 \gamma_n=\gamma-nv,\quad d_n=d-nu.                   \tag{SQ.10}
\]

It follows directly by substituting \(Z_n=Z,V_n=Z^{-n}V\) into the
period matrix. It is the boundary gluing between (SQ.9) and the
unchanged exterior. In particular its gamma shear is not asserted to
extend over the old exterior.

Let alpha_q and theta have period one. Retain the full Tate phase

\[
 \alpha_Q=\alpha_q-6\theta+\phi_\kappa,
 \qquad \phi_\kappa=(2\pi)^{-1}\operatorname{Im}f_\kappa,
                                                        \tag{SQ.11}
\]

where f_kappa is the actual periodic logarithm after its winding has
been removed. Then du+alpha_Q dv is a global source one-form on the
boundary. The q monodromy u to u-v and rho monodromy u to u+6v
are both retained by this formula.

First display the integral part of the circle connection. In the
old coefficients it is

\[
 A_0=dd+\alpha_q\,d\gamma.
\]

In the new coefficients the phase winding of alpha_n is 6n and
that of eta_n is zero. Its connection is therefore

\[
 A_n=dd_n+\alpha_q\,d\gamma_n+6n\theta\,dv_n.
                                                        \tag{SQ.12}
\]

Here \(A_n(\partial_d)=1\) is a real principal-circle
connection. The physical complex line \(\mathcal L_\delta\) has
unitary connection \(2\pi iA_n\), so
\(c_1(\mathcal L_\delta)=-dA_n\). Thus the positive real-curvature
class used below is that of its inverse
\(\mathcal U_n=\mathcal L_\delta^{-1}\). P3K.66, EC.1--2,
records the local Hopf and associated-line arrow explicitly.
The vanishing pairing proved here is unchanged by this sign.

For a rho turn d_n changes to d_n-6nv, and for a q turn it changes
to d_n-gamma_n. Thus these are connections on the actual integral
circle bundles, with the displayed transition functions. Substitution
of (SQ.10) gives

\[
 A_n-A_0=-n\{du+(\alpha_q-6\theta)dv\}.             \tag{SQ.13}
\]

The full unit factors have not disappeared. Their connection terms
are obtained from their actual periodic logarithms

\[
 f_{11}=f_\kappa+nf_g,\quad
 f_{21}=f_\alpha+nf_\eta-nf_\kappa-n^2f_g,\quad
 f_{12}=f_g,\quad f_{22}=f_\eta-nf_g.                \tag{SQ.14}
\]

In the actual flat real-period coordinates these are globally defined
one-form corrections, including d(arg g) and d(arg eta). Accordingly
(SQ.13) becomes -n(du+alpha_Q dv) plus that explicitly retained
global one-form correction. Its curvature difference is the exterior
derivative of that expression. We use these full connections below.

Here is the interior class, with no assumption that b is a relative
class. The source E retracts onto its nodal fibre \(S^{2}\) wedge \(S^{1}\).
Let b denote the graph generator of \(H^{1}(E)\), with boundary value the
actual coefficient v. One concrete extension is given by the Lefschetz
handle presentation of E: start with the circle map v on the regular
torus product. The attaching vanishing circle is the a circle, on
which v is constant. Its real lift on the attaching handle collar
extends over the two-handle, with a cutoff agreeing on the collar.
This produces the required source map, with its actual outer value.
The parameter monodromy (u,v) to (u+6v,v) preserves that value and
the same handle extension; the marked branches return literally,
so the construction is periodic. On its normalization cut,
the line with constant factor alpha_n is glued by alpha_n between the
two branches. Formula (SQ.2) makes the parameter winding of that
actual gluing 6n. The line has no vanishing-cycle factor and the
suspension factor eta_n has zero parameter winding. Thus its
inverse-line Chern class differs from the old inverse-line class by

\[
                         6n\,[d\theta]\smile b.         \tag{SQ.15}
\]

One can realize this inverse-line class directly by cutting in theta:
the physical circle coordinate is glued by d to d-6n b at the two ends,
and the dual coefficient has the opposite gluing. For the physical
coefficient, on the graph cut the equivalent gluing is
exp(2pi i 6n theta); the dual graph gluing is its inverse. The equality
of the two physical clutch descriptions is the square with change of coordinate
d to d+6n theta b on its doubly cut rectangle. All zero-winding
terms are the actual logarithms in (SQ.14).

The same calculation holds after fixed-sphere replacement. To see the
extension, the graph map b restricted to the normalization sphere has
a real lift. Its rho winding is zero, since the marked normalization
and branches return literally. Modify that circle-valued map in a
small tube by a compactly supported real homotopy so it is constant
on a smaller fixed tube. It now extends constantly over \(D^{3}\) times \(S^{2}\).
For the line arrow, if b and its modified map b_prime differ by the
supported real function h, change the fibre coordinate on the theta
cut by exp(2pi i 6n theta h). Its two endpoints give precisely the
change of the displayed theta clutch. The modified clutch is constant
on the cap, where this line extends. Its dual therefore supplies an actual
representative of (SQ.15) on C_0, including the cap identification. The
meridian Chern number of the new and old physical circle lines is
the same positive one, by (SQ.8); their difference there is zero.
The retained ordinary b times gamma torus has Chern number zero:
on a regular source fibre the actual total torus is the quotient of
its real period lattice and its physical delta sublattice is primitive,
so the chosen integral period basis gives a section of that torus
bundle. The gamma times theta difference is also zero by eta_n's
zero winding. These maps identify the inverse-circle-line difference with
(SQ.15), equivalently the physical Euler-line difference with its
negative, up to the exact curvature terms already retained in (SQ.14)
and its prescribed outer gauge (SQ.13).

For an integral group check, H_1(W)=Zb plus Zgamma and
H_2(W)=ZF plus Z(b times gamma). The Thom exact sequence for removal
of F adds its normal meridian in degree two: H_3(W) to H_0(F) is
zero, since a regular fibre times gamma is disjoint from F. The
Mayer--Vietoris map for the cap identifies its meridian with that
one and kills the primitive F. Consequently

\[
 H_1(C)=\mathbb Z^2,\qquad
 H_2(C)=\mathbb Z\langle\text{meridian},b\times\gamma\rangle.
                                                        \tag{SQ.16}
\]

Both are torsion free. The parameter monodromy fixes b,gamma and
the oriented meridian. It cannot add a meridian to b times gamma:
the actual global Euler line has evaluation zero on that regular
torus and one on the meridian. This gives the two parameter classes
b times theta and gamma times theta in the Wang sequence and
confirms the preceding class computation without dropping torsion.

## SQ.4. The boundary tangent connection and its exact transgression

Use the invariant boundary coframe

\[
 du+\alpha_Qdv,\quad dv,\quad d\gamma,\quad
 d\alpha_q,\quad d\theta,
                                                        \tag{SQ.17}
\]

together with the outward normal. This is a frame on the actual
nilmanifold times the two retained circles. It retains the rho
monodromy in (SQ.11). Use the corresponding flat tangent connection
on a whole boundary collar; a tangent connection need not be the
Levi--Civita connection to represent p1.

We prescribe these actual real period coordinates on the entire
outside collar before performing the F9 construction. They are smooth
coordinates on the regular real torus quotient, formed from the full
real period matrix of (SQ.1)--(SQ.2). On that collar the marked line coordinate is precisely its
contracting gamma_B coefficient, including the
actual norms of alpha and eta. In the convex combination of proper decreasing F9-coordinate
maps, equivalently proper increasing maps in -gamma_B on both sides,
take the outside partition weight identically
one on this collar. The actual comparison is orientation-preserving between those two
marked coordinates. The resulting orbit product is therefore exactly
this prescribed coordinate there. It is not merely isotopic to it.
The source horizontal field in SQ.2 was likewise prescribed there by
(SQ.7), so it is the identity on the marked real coefficients u,v.
The variables q and rho, including the outward radial variable r,
are fixed.

Order the stable coframes as
\((du+\alpha_Q\,dv,dv,d\gamma,d\alpha_q,d\theta,dr)\), with \(dr\) outward.
Put \(\phi_g=\operatorname{Im}(L_g)/(2\pi)\). The pullback of the target coframe by the
actual gluing arrow is exactly

\[
 \begin{pmatrix}
 1&n\phi_g&0&0&0&0\\
 0&1&0&0&0&0\\
 0&-n&1&0&0&0\\
 0&0&0&1&0&0\\
 0&0&0&0&1&0\\
 0&0&0&0&0&1
 \end{pmatrix}
 \begin{pmatrix}
 du+\alpha_Qdv\\dv\\d\gamma\\d\alpha_q\\d\theta\\dr
 \end{pmatrix}.
                                                        \tag{SQ.18}
\]

Indeed \(\alpha_{Q_n}=\alpha_Q+n\phi_g\), while \(\gamma_n=\gamma-nv\).
The matrix has determinant one. The coordinate matrix on the dual
frames is its inverse transpose; using that matrix instead of the
coframe matrix changes none of the following calculation. There is
no unspecified tangent block. The differentials of arg(alpha) and
arg(eta) belong to the full circle connection (SQ.14); their norms
have already entered the prescribed gamma coordinate. The term
with kappa winding remains in alpha_Q and in (SQ.12). The derivative
d(arg g)/(2pi) is retained explicitly as d(phi_g) below.

Denote the displayed matrix by G. Its Maurer form is literally
\(\omega=G^{-1}dG=n\,d\phi_g\,E_{12}\). The constant gamma shear contributes
no derivative, and its product with E_12 is zero. Thus omega squared
is zero even before restricting to the two boundary base variables.
The dual-frame matrix has the corresponding transposed square-zero
Maurer form. Interpolate the actual flat connections with chi(r) omega
on the gluing collar. Direct multiplication gives

\[
 F=\chi' dr\wedge\omega+(\chi^2-\chi)\omega^2,
 \qquad\operatorname{tr}(F^2)=0.                       \tag{SQ.18a}
\]

This verifies the full collar transgression with the actual matrix.
Flatness at its two ends alone would not suffice. The positive-norm
and graph comparisons are confined to the interior by the prescribed
collar equality, and therefore introduce no additional boundary
matrix. We can compare the two glued tangent connections with p1
identically zero on the entire intervening collar.

## SQ.5. The remaining relative pairing is zero

Choose nested fixed tubes U_0 inside U_1 inside U_2 inside U_3, all away
from the outer boundary. Confine the surgery and every connection change
to U_1. Choose the tangent connection on C_0 to agree outside U_1
with a connection pulled from TE in the actual product E times
\(S^1_\gamma\); add its trivial gamma line. On the outside collar use
the flat connection in (SQ.17). The source connection can be
chosen with precisely its source part there. Extend the connection
arbitrarily across the surgery region using the actual normal and
cap arrows of SQ.2. In the rho family choose it smoothly and
periodically. Its p1 form vanishes near the outer boundary.

We evaluate its relative p1 class on (SQ.15). Fix a parameter theta
and start with a smooth graph map b:E to \(S^{1}\). At a regular value,
its four-dimensional product level in W is \(N^3\) times \(S^1_\gamma\).
The source-pulled p1 four-form restricts to zero there, since its
source component lies in a three-manifold.

The restriction of b to F has a real lift. Extend that lift over a
tube U_3. A cutoff homotopy supported there, fixed on the outside
boundary, changes b to a constant on U_2. Choose a regular value
different from that constant. The new level misses the entire
surgery region and is literally the same submanifold before and
after attaching \(D^{3}\) times \(S^{2}\). It need not be a product; we do not
make that assertion. The regular-value cobordism of the displayed
homotopy, relative the unchanged outer map, identifies its relative
cycle with the original product level. The source-pulled p1 form is
closed and its outer trace is zero. Its integral on the new level
is therefore also zero. The two normal directions to that level
in the rho family are the b direction and the theta direction;
both are globally framed. Consequently this is exactly the
relative pairing, with its actual tangent bundle,

\[
              \big\langle p_1(TC_0),[d\theta]\smile b
                         \big\rangle=0.                 \tag{SQ.19}
\]

Here p1 is relative to the specified flat boundary connection,
whereas b is absolute. There is no assertion that b vanishes on
the outer torus. This distinction is precisely why the retained
boundary connection and its transgression in SQ.4 were required.

## SQ.6. Gluing the actual characteristic calculation

The rest of the completed quotient is the same actual exterior for
every T_n. On the cut piece use the explicit diffeomorphism (SQ.9)
to transport its tangent connection; on the common exterior keep
the original one. SQ.4 joins them over the actual boundary shear
with identically zero p1 form. Thus the difference of the two
p1-times-Euler integrals has only the physical Euler interior term, the negative of (SQ.15),
and the exact curvature terms in (SQ.13)--(SQ.14). The interior term
is zero by (SQ.19). The exact terms contribute a boundary integral
of their actual one-form primitive times p1, which is zero on the
whole collar. This explicitly includes the gauge
-n(du+alpha_Q dv); it is not discarded or assumed to extend.

The two physical completions consequently have the same ell.
The common parameter reversal retains the Euler line, so their
Jin completions have the same ell as well. P3K.42 gives ell(T_0)=0.
The complete comparison therefore proves

\[
                              \ell(T_n)=0.              \tag{SQ.20}
\]

Exact algebraic checks are executed in \path{code/part3/source_cusp_shear_pontryagin.py}, with saved JSON, stdout and stderr. The 29 checks retain the full unit winding, both parameter monodromies, the literal source point, the nodal vector field, the integral Thom/Mayer--Vietoris quotient, the six-by-six derivative and its whole-collar transgression. The geometric proof is assessed separately from this certificate.


## SQ.7. Exact relative consequences

Let A_n denote the actual integer Jin index of this fixed-star
completion, with its specified meridian line. The proved relation of
K7 and the corrected identities SFIX.2 read

\[
 24A_n=4k_n-\ell_n,\qquad
 k_n=V_{00}+6,\quad
 \ell_n=24+2V_{00}+2\delta_0.
\]

Thus the conclusion (SQ.20), together with those exact identifications,
gives

\[
 k_n=6A_n,\quad
 (m_0^{\mathrm{native}},n_0^{\mathrm{native}})=(0,-6A_n),
 \quad V_{00}=6A_n-6,\quad\delta_0=-6A_n-6.           \tag{SQ.21}
\]

P3K.56 separately computes the actual central residue
A_n=1-3n(n-1) modulo 28. Substitution fixes the two displayed
ordinary integers modulo 168, hence also modulo 56:

\[
 V_{00}\equiv-18n(n-1),\qquad
 \delta_0\equiv-12+18n(n-1)\pmod{168}.               \tag{SQ.22}
\]

These consequences do not specify an integer lift of A_n from its
residue. The full integer lift is not inferred from those congruences.
