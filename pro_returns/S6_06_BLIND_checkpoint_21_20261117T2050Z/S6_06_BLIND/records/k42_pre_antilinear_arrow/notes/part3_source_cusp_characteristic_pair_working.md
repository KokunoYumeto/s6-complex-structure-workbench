# The actual characteristic pair of the selected-cusp source loop

Proved as P3K.42 after the full root audit and the independent
SP.2--4 frame/sign audit. We retain the exact positive rho
loop, initial physical-delta-edge fan, source, line and cap maps of
P3F.54, P3F.56 and P3K.40. The scalar is fixed and the coalescing finite
pair carries no logarithmic modification. The computation below uses
the actual normal framings on both caps of the F56 bordism. It does not
assign a value to another fan.

The resulting characteristic numbers in Jin's convention are
\[
                         (k,\ell)=(6,0).                 \tag{SP.1}
\]
Thus its first-resolution relative coordinates are
\((m,n)=(0,-6)\), with central coordinate one. The first fixed-edge
flop remains the value \(-5=23\) already proved in P3K.40.

## SP.1. The framed local surgery and its actual four-cycle

Let \(e:S^3\hookrightarrow S^6\) be the actual lifted link of P3F.55.
Its projection is the immersion of complex Smale length two, and its
third normal field is the actual increasing height direction. Fix the
first normal field in the oriented complex normal plane of the
projection, and complete the frame \((\nu _1,\nu _2,\nu _3)\) with
that height field. Normalizing and applying Gram--Schmidt uses a
positive triangular homotopy. It therefore retains the actual
projection-normal plus height framing, rather than adding an element
of \(\pi _3(SO(3))\).

Takase, Corollary 2.15, supplies a Seifert embedding
\(V\hookrightarrow S^6\) whose outward boundary normal is this
specified \(\nu _1\). The proof of his Theorem 3.2 gives, for this
projection and this boundary normal,
\[
              2\omega=3\sigma(V)+e(\nu V)^2.             \tag{SP.2}
\]
The invariant and generator comparison in P3F.55, equations
(CL.16)--(CL.19), fixes the convention in (SP.2): the punctured
Kummer test has signature \(-16\) and Smale invariant \(-24\)
in both conventions. Hence the actual local projection has
\(\omega=-2\). The same comparison gives
\[
             8H(e)=e(\nu V)^2-\sigma(V),\qquad H(e)=1.
                                                               \tag{SP.3}
\]
Solving these two displayed equalities gives
\[
                    e(\nu V)^2=5,\qquad \sigma(V)=-3.    \tag{SP.4}
\]

We now identify these numbers with the characteristic numbers of the
*framed* surgery manifold, including its meridian line. Let
\[
 N_e=(S^6\setminus\operatorname{int}(S^3\times D^3))
                  \cup(D^4\times S^2)
\]
use precisely the preceding normal frame. Along the Seifert collar,
the vector from its boundary into \(V\) is \(-\nu _1\).
Consequently the truncated Seifert surface has boundary
\(S^3\times\{-\nu _1\}\), and caps by the literal constant section
\(D^4\times\{-\nu _1\}\). Denote this closed four-manifold by
\(\widehat V\).

Here are the orientations of this cap. Write the ambient orientation
near the knot as
\(\Omega_{S^3}\wedge dn_1\wedge dn_2\wedge dn_3\).
The Seifert orientation is
\(dn_1\wedge\Omega_{S^3}\), so its oriented normal two-plane is
\(-dn_2\wedge dn_3\). At \(-\nu _1\), the outward-first
orientation of the normal meridian sphere is also
\(-dn_2\wedge dn_3\). The boundary of the knot complement is
\(+\Omega_{S^3}\wedge\Omega_{S^2}\); the surgery cap therefore
has orientation \(-\Omega_{D^4}\wedge\Omega_{S^2}\).
The cap of \(\widehat V\) has orientation \(-\Omega_{D^4}\).
Thus its oriented normal plane is exactly the positive meridian
plane, with no sign change in its Euler class.

Let \(x\) be the meridian class with integral one on this sphere.
The Mayer--Vietoris map in degree two identifies the boundary
\(H_2(S^3\times S^2)=\mathbb Z\) with the meridian summands in
both pieces; it gives \(H^2(N_e)=\mathbb Zx\). In degree four,
the connecting map identifies \([\widehat V]\) with the oriented
boundary \([S^3]\). The normal-plane calculation above therefore
gives the actual duality identity
\[
       \operatorname{PD}_{N_e}(x)=[\widehat V],\qquad
       x|_{\widehat V}=e(\nu\widehat V).                 \tag{SP.5}
\]
The cap frame is constant. Its Euler square is the relative square
in (SP.4), and capping by a four-ball leaves the signature unchanged.
Restriction of the ambient tangent bundle to this embedded cycle is
\(T\widehat V\oplus\nu\widehat V\). It follows directly that
\[
 \begin{aligned}
 k(N_e)&=\int_{N_e}x^3=\int_{\widehat V}e(\nu\widehat V)^2=5,\\
 \ell(N_e)&=\int_{N_e}p_1(TN_e)x
       =3\sigma(\widehat V)+e(\nu\widehat V)^2=-4.
 \end{aligned}                                             \tag{SP.6}
\]
This constructs the four-cycle and its Euler-line restriction; it
does not recover the pair from the Haefliger number alone.

## SP.2. The actual Cartier-to-Cox coordinate map

Use the normalization and branch notation of F56:
\[
 N=\mathbf P^1_s\times D_\rho,\quad
 x=s-\rho,\quad y=s+\rho,\quad Z=x/y,\quad
 D_+=(x=0),\quad D_-=(y=0).
\]
Remove the inner four-ball to obtain \(W\). The actual determinant
normal isomorphism of F56 is
\[
 L=\mathcal O(-D_+-D_-),\qquad
 E=\mathcal O(D_+)\oplus\mathcal O(-D_-),\qquad
 \operatorname{ad}E=\mathbb R_\gamma\oplus L_{\mathbb R}.
                                                               \tag{SP.7}
\]
The determinant trivialization is multiplication by \(x/y\).
In the finite \((s,\rho)\) ball, the Cartier frames of \(E\) are
\((1/x,y)\); their determinant is \(y/x\), so the stated
trivialization sends their wedge to one. These are nonvanishing
frames of the indicated line bundles even on the corresponding
divisors.

The morphism \(r=[x:y]:W\to\mathbf P^1\) identifies \(E\)
with \(r^*(\mathcal O(1)\oplus\mathcal O(-1))\). On the chart
\(y\ne0\), the coefficient arrow from the Cartier frames to the
standard dual-tautological and tautological frames is exactly
\[
                         \operatorname{diag}(1/y,y).      \tag{SP.8}
\]
Indeed the first pulled-back divisor frame is \(y/x\), and the
second divisor is absent from this chart. Equation (SP.8) follows by
expressing \(1/x\) and \(y\) in those frames. The corresponding
equation on \(x\ne0\) agrees on the overlap.

The actual Cox quaternion is
\((1+jZ)(c_0+j\overline{c_1})\). Its summand order is
\((c_0,\overline{c_1})=(\text{second},\text{first})\) in
(SP.7). After the positive Hermitian normalization of (SP.8), a
Cartier vector \((a,b)\) therefore becomes
\((\operatorname{phase}(y)b,\overline{\operatorname{phase}(y)}a)\)
in Cox order. Multiplication by the normalized first quaternion gives
\[
 g(x,y)=\frac1{\sqrt{|x|^2+|y|^2}}
       \begin{pmatrix}y&-\overline x\\x&\overline y\end{pmatrix}
                                                               \tag{SP.9}
\]
times the fixed summand swap. In particular (SP.9) is the
**Cartier-coordinate to Cox-coordinate** arrow. It is not its
inverse. A constant unitary adjustment of the swap makes it
determinant one and does not change its homotopy class.

The same fixed swap must also be kept on real normal coordinates.
Its adjoint action is
\[
                  (\gamma,\ell)\longmapsto
                           (-\gamma,\overline\ell).       \tag{SP.10}
\]
Both the real line and the complex plane reverse orientation;
their rank-three product preserves orientation. This is precisely
F56's constant positive-Hopf normal identification, retained at both
caps.

The inner projection-normal frame is the Cartier frame used here,
up to an extending gauge. To verify that assertion rather than
postulate it, use F56's explicit nonzero normal covector
\[
       (3s^2-\rho^2)\,dX-2s\,dy
                          +2\rho(s^2-\rho^2)\,d\rho .     \tag{SP.11}
\]
The determinant exact sequence identifies its normal quotient with
the canonical line of the normalization. The ratio of this line
identification and the Cartier identification is a holomorphic unit
on the punctured finite ball. Hartogs extension extends it to the
ball, and a holomorphic function in two variables cannot have its
only zero at the origin. Its extension is therefore a unit. The
resulting real two-plane frame comparison extends over the inner
four-ball. Adding the height line and the explicit triangular
graph-normal shear gives the actual frame of SP.1, with no free
\(SO(3)\) clutch.

The normal-coordinate unit can also be checked directly in both
actual fixed-edge charts. We use the physical source coordinate
\(q\) of F56, not its Tate multiple. With \(X=xy\), restriction
of the differential of that displayed source equation to the
normalization gives
\[
 dq=-\frac{xy}{xy+u(\rho)}\,n,
 \qquad n\text{ is the covector in (SP.11)}.              \tag{SP.11a}
\]
The first Cox chart has \(q=Zc_0c_1\), and the second has
\(q=Z^{-1}c'_0c'_1\), with \(c'_i=Zc_i\). Their quotient
complex normal coordinates consequently satisfy, on the fixed curve,
\[
 \begin{aligned}
 d(c_0c_1)&=-\frac{y^2}{xy+u(\rho)}\,n,\\
 d(c'_0c'_1)&=-\frac{x^2}{xy+u(\rho)}\,n.
 \end{aligned}                                             \tag{SP.11b}
\]
These are exactly the two Hom arrows of (SP.8), multiplied by the
same explicit unit \(-1/(xy+u(\rho))\). Since \(u(0)=u_*\ne0\),
it has an analytic logarithm and square root on the finite inner
ball. Its spinor adjustment therefore extends over that ball. This
verifies the actual normal-unit comparison, as well as its line
transition. It supplies no additional relative Chern number.

There is also an exact check on the separate normal factors. Once
their product has been matched by (SP.11b), any remaining
weight-preserving linear normal gauge has the form
\((c_0,c_1)\mapsto(g c_0,g^{-1}c_1)\). Remove its positive
modulus by the actual equivariant positive rescaling. For its unitary
phase, both right-complex spinor coordinates are multiplied by
\(g/|g|\); hence
\[
                  q_H\longmapsto q_H\,g/|g|.             \tag{SP.11c}
\]
This is the physical circle action, and its adjoint Hopf normal
coordinate is exactly unchanged. It contributes no additional
\(SO(3)\) clutch. A possible parameter winding of this circle-line
gauge is retained and extends over \(D^3\times S^1\), whose
restriction map on \(H^1\) is an isomorphism. We therefore do not
assume that each separate normal gauge has a logarithm across the
parameter origin.

## SP.3. The outer cap: the actual product arrow

The outer coordinate change is the literal map of F56
\[
 A_\rho=\begin{pmatrix}1&-\rho\\1&\rho\end{pmatrix},
 \qquad
 \mathcal B_\rho(P)=
       \frac{A_\rho P A_\rho^*}{\operatorname{tr}(A_\rho P A_\rho^*)}.
                                                               \tag{SP.12}
\]
Here the closed three-ball is the positive semidefinite Hermitian
matrices of trace one. Its boundary consists of rank-one matrices.
This is a periodic diffeomorphism of the ball, including its centre,
and its boundary map is exactly \(r\). We use its actual product
extension on the surgery collar, rather than replacing the normal
frame by its derivative.

The collar in P3K.40 and F56 is the literal first-resolution product
\((h,q_H)\), where \(h\) is the base sphere coordinate and
\(q_H=(1+jZ)(c_0+j\overline{c_1})\) is the normalized actual
Cox quaternion. The physical circle acts by
\(q_H\mapsto q_H e^{-i\theta}\). Thus on the normal sphere
cover the exact outer cap map is
\[
 (P,q_H,\rho)\longmapsto
                  (\mathcal B_\rho(P),q_H,\rho)
 \quad\text{on }D^3\times S^3\times S^1.                 \tag{SP.13}
\]
It is a periodic diffeomorphism, is equivariant for that same circle,
and restricts to the actual base-coordinate change on the boundary.
Its quotient is
\((\mathcal B_\rho,\operatorname{Id}_{S^2})\). It therefore
extends both the actual Cox normal frame and the meridian circle
line over the product cap. This is precisely the product surgery
collar used in F56: its second factor is the actual Hopf normal
sphere, and (SP.13) holds that factor, with its orientation, fixed.

In particular (SP.13) keeps the full determinant winding. For
clarity the exact determinant discrepancy can be written down.
The Hom arrow induced by (SP.8) takes the Cartier frame \(xy\)
of \(L\) to \(y^2\) times the standard \(\mathcal O(-2)\)
frame. Under the standard canonical identification this is
\[
                  y^2\,dZ=2\rho\,ds.                    \tag{SP.14}
\]
Thus the actual Cox arrow has the factor
\(\det A_\rho=2\rho\) relative to the cotangent inverse.
Its winding is one. We neither remove it nor identify (SP.13) with
the tangent derivative of \(\mathcal B_\rho\). It remains in
the Cartier-to-Cox coordinate matrix (SP.9) and hence in the clutch
computed below. The earlier attempted derivative comparison that
omitted this factor is preserved as a superseded unpromoted attempt.

All coordinates in (SP.13) are the actual coordinates already
matched in F56 and P3K.40. In particular we make no additional
replacement of \(q_H\) by a Tate-scaled quaternion. The winding
\(-6\) of \(q_T/q\) is retained by those matched charts.
Equations (SP.11a)--(SP.11b) use the physical \(q\) in those
charts; the nonzero factor \(q_T/q\) remains in the period
identification of the adjacent cell. Replacing that period by one
with factor one would change the marking and is not done here.
The original source and line unit gauges used in F56 extend over
the full source disc. Their displayed logarithms give extending
isotopies on the same normal collar. The induced isotopies of its
boundary extend over the product cap by extending their invariant
vector fields with a collar cutoff; averaging preserves the
physical circle action. This carries these actual gauges in
(SP.13), rather than changing the cap framing.

## SP.4. The relative second Chern number and the normal sphere bundle

Cap \(W\) by the inner four-ball in its projection-normal frame
and the outer \(D^3\times S^1\) in its actual Cox frame. The
resulting base and spinor bundle will be denoted by
\(\overline W\) and \(\overline E\). The base orientation is
\[
 \overline W=(S^2\times D^2)\cup(D^3\times S^1)
                      =\partial(D^3\times D^2).
                                                               \tag{SP.15}
\]
The first piece has its complex orientation, and the second has
minus its displayed product orientation. Thus the boundary of the
outer cap is the negative of
\(K=\mathbf P^1\times S^1\), with \(K\) oriented as the
boundary of \(N\).

The bundle \(E\) extends across the inner ball and is a trivial
\(SU(2)\) bundle over \(N\simeq S^2\). Choose a global frame
agreeing there with the Cartier frame. Such agreement can be made
on the ball because the difference of two extending frames is
itself an extending gauge. Compare this frame with the Cox frame on
\(W\). On the inner boundary its coordinate matrix is (SP.9).
Since this comparison extends over \(W\), its degree on the outer
boundary \(K\) is the same as its degree on the inner sphere in
its positive complex-domain orientation.

We calculate that degree with its precise trace convention. The
first column of (SP.9) is \((y,x)\); the map
\((s,\rho)\mapsto(y,x)\) is complex linear with nonzero
determinant \(-2\). Hence its normalized boundary map has degree
one for the complex first-column orientation. At the identity the
positive tangent matrices in that orientation are
\[
 I=\begin{pmatrix}i&0\\0&-i\end{pmatrix},\quad
 J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
 K_0=\begin{pmatrix}0&i\\i&0\end{pmatrix}.
                                                               \tag{SP.16}
\]
They satisfy \(IJ=-K_0\) and \(\operatorname{tr}(IJK_0)=2\).
Consequently the right Maurer--Cartan form has
\[
           \int_K\operatorname{tr}(dg\,g^{-1})^3=24\pi^2.
                                                               \tag{SP.17}
\]
This explicitly fixes the sign; the quaternion convention with the
opposite group orientation cannot be substituted in (SP.17).

Equation (SP.9) is a coordinate arrow from the frame on \(N\) to
the cap frame. A connection that is zero in the first frame is
therefore \(-dg\,g^{-1}\) in the latter frame near their boundary.
Writing \(\omega=dg\,g^{-1}\), we have
\(d\omega=\omega^2\) and
\[
 \operatorname{tr}\bigl((-\omega)d(-\omega)
                    +\tfrac23(-\omega)^3\bigr)
                    =\tfrac13\operatorname{tr}(\omega^3).
\]
Extend this connection into the cap with a collar cutoff. Stokes'
formula and its negative boundary orientation give the actual
clutch number
\[
 \begin{aligned}
 c_2(\overline E)[\overline W]
    &=\frac1{8\pi^2}\int_{\text{cap}}\operatorname{tr}(F^2)\\
    &=-\frac1{24\pi^2}
                       \int_K\operatorname{tr}(dg\,g^{-1})^3=-1.
 \end{aligned}                                             \tag{SP.18}
\]
For the actual adjoint bundle,
\(p_1(\operatorname{ad}\overline E)=-4c_2(\overline E)\).
This identity follows directly on the diagonal circle: the spinor
has Chern roots \(a,-a\), and the nontrivial real adjoint plane has
Euler class \(2a\). Therefore
\[
             p_1(\operatorname{ad}\overline E)[S^4]=4.    \tag{SP.19}
\]

Let \(B=S(\operatorname{ad}\overline E)\to S^4\), with the
actual positive Hopf meridian class \(x\) from F56. Its determinant
class is zero, so the oriented vertical tangent Euler class is
\(e_v=2x\). The exact splitting
\(T_vB\oplus\mathbb R\cong\pi^*(\operatorname{ad}\overline E)\)
gives \(4x^2=\pi^*p_1(\operatorname{ad}\overline E)\).
Since \(\pi_*x=1\) and \(p_1(TS^4)=0\), we obtain
\[
                         (k(B),\ell(B))=(1,4).             \tag{SP.20}
\]
Its index is zero, as already used in F56. The present calculation
retains the individual numbers of this actual normal bundle.

## SP.5. The full oriented boundary sum

Use exactly F56's normal-tube excision and its two product surgery
collars. The complex orientation of \(W\), followed by the
positive-Hopf normal orientation, is the ambient orientation.
Explicitly, F56 gives
\(\Omega_{\rm ambient}=-\Omega_{\rm source}\wedge d\gamma\)
and
\(\Omega_{\nu H}=-d\gamma\wedge\Omega_L\); hence
\(\Omega_{\rm ambient}=\Omega_W\wedge\Omega_{\nu H}\).
The fixed swap (SP.10) has determinant one and preserves this
orientation; it does not supply the initial minus. The inner
boundary of the removed normal disc bundle consequently has
orientation
\(-\Omega_W\wedge\Omega_{S^2}\). Both product collars preserve
that sign, so this additional closed boundary is \(-B\).

The outer boundary of \(Y\times D_\rho\) is \(-P_f\), because
\(\dim Y=5\). The excised inner seven-ball gives \(-N_e\).
Thus the complete oriented boundary, retaining all three pieces, is
\[
                         -P_f\ \sqcup\ -N_e\ \sqcup\ -B.
                                                               \tag{SP.21}
\]
The Thom meridian line constructed in F56 extends through this
cobordism and both collars. Its restriction on each displayed piece
is the class used above. Stokes' theorem applied to its cube and
to its product with the stable tangent Pontryagin class gives
\[
                  (k,\ell)(P_f)=-(k,\ell)(N_e)-(k,\ell)(B).
                                                               \tag{SP.22}
\]
The local raw complex-plus-height orientation reverses both the
six-manifold orientation and the meridian class relative to the
physical positive-Hopf convention. The products \(x^3\) and
\(p_1x\) are unchanged by these simultaneous reversals. Thus the
local values (SP.6) enter (SP.22) with exactly the signs written.

Finally the physical positive return has
\(P_f=M_{f^{-1}}\) in Jin's endpoint convention. Reversing the
parameter reverses both characteristic numbers while carrying the
same meridian line. Equations (SP.6), (SP.20) and (SP.22) therefore
give
\[
                 (k,\ell)_{\rm Jin}(f)
                       =(5,-4)+(1,4)=(6,0).
                                                               \tag{SP.23}
\]
The exact relative-coordinate identities of P3K.23 now give
\(m=6A-k=0\), \(n=-6A=-6\), with \(A=1\). This uses the
actual first-resolution product established in P3K.40. No product
on the other cusp curves, and no later fan value, is inferred here.

## Audit and computation status

The local Seifert formula is read directly from Takase's Corollary
2.15 and the proof of Theorem3.2. The convention is fixed by the
nonzero Kummer comparison in F55. The earlier derivative matrix was
independently multiplied by root, but its proposed identification
with the actual Cox arrow omitted the determinant factor (SP.14)
and has been withdrawn. The actual product-collar map (SP.13)
retains that factor. Root passed the complete revised proof,
including the Seifert cap cycle and full oriented boundary sum.
The independent SP.2--4 audit passed the actual physical-q normal
units, residual physical-circle gauge, product collar, Cartier-to-Cox
arrow and relative Chern sign.

The certificate is code/part3/source_cusp_characteristic_pair.py.
It records the derivative matrix only as a diagnostic, and checks
the actual Cartier/Cox product, determinant factor,
the fixed real-line sign, the Maurer--Cartan trace, the two Seifert
equations, and the sphere-bundle and bordism arithmetic. It does not
substitute arithmetic for the bundle and cobordism proofs above.
