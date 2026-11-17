# Shear fixed-star characteristic pair: retained maps and remaining cap comparison

This is a working record, not a promoted characteristic-pair result.
P3K.56 proves the actual return class modulo 28 for every shear fan.
The full fixed-star pair has not been inferred from that class.

## SFIX.1. Exact local shear and the corrected relative identities

For the fan T_n, the actual characters and periods are

\[
 Z_n=Z,\quad V_n=Z^{-n}V,\quad h_n=hB^n,\quad B_n=B.
\]

On the common first fixed-star chart, whose physical height monomial is
q=Z c_0 c_1, the normal-factor arrow is exactly

\[
 (Z,c_0,c_1)\longmapsto(Z,Z^n c_0,Z^{-n}c_1).       \tag{SFIX.1}
\]

Its product is unchanged. For x=s-rho, y=s+rho, this arrow retains the
Cartier divisor n(D_+-D_-), with Z=x/y. It is not a gauge by a
nowhere-zero function across either branch section. Its unitary part on
the common punctured chart multiplies the actual right-Hopf quaternion
by the physical circle phase of Z^n. Hence its adjoint normal action is
literally the identity there; the circle-line extension across the two
divisors must still be carried by its Cartier maps.

Let a=V_{00} and b=delta_0 in the actual GF ordinary product. K31.7 and
the proved ordinary/native L^6 comparison give

\[
 n_{\rm native}=(b-a)/2,\qquad
 m_{\rm native}=-(a+b)/2-6,
\]
\[
 k=a+6,\qquad \ell=24+2a+2b,\qquad A=(a-b)/12.       \tag{SFIX.2}
\]

The earlier message using k=6-a had the variation sign reversed; it is
preserved in code/part3/attempts/shear_fixed_pair_sign_attempt.md and
was not used by any proved result.

For completeness, the two nonfixed native pairs are already determined
without a or b:

\[
 (m_1,n_1)=(-6n,6n-6),\qquad
 (m_2,n_2)=(6n-6,-6n).                             \tag{SFIX.3}
\]

Indeed V_{11}=V_{22}=0 gives m_ordinary=-n_native, and removing the
actual pure-left L^6 gives (SFIX.3). This does not determine (SFIX.2).

## SFIX.2. An exact circular-height chart and its full derivative

A possible way to retain an integer branch-height shift is to keep the
inner ambient source circle rather than putting the graph into the
short real arc used in F56. The following coordinate calculation is
exact and does not by itself identify that inner construction with the
actual fan.

On a five-ball |g_1|<R, with h in R/Z, put

\[
 J(g,h)=((R+g_1)\cos(2\pi h),(R+g_1)\sin(2\pi h),
                         g_2,g_3,g_4,g_5).        \tag{SFIX.4}
\]

This embeds the solid torus in R^6. In the ordered domain coordinates
(g_1,h,g_2,g_3,g_4,g_5), its derivative has the two-by-two block

\[
 \begin{pmatrix}
 \cos(2\pi h)&-2\pi(R+g_1)\sin(2\pi h)\\
 \sin(2\pi h)& 2\pi(R+g_1)\cos(2\pi h)
 \end{pmatrix}
\]

and identity on the other four coordinates. Its determinant is
2*pi*(R+g_1)>0. A real height lift h:S^3->R makes this derivative
homotopic to a constant positive matrix by the literal substitution
(g_1,h)->((1-t)g_1,(1-t)h). All matrices remain invertible.

Consequently, for a graph of an immersed projection g:S^3->D^5,
its three tangent columns and its two projection-normal columns plus
height column are transported by DJ without adding a third homotopy
class of GL^+(6). Orthogonalizing uses a positive triangular homotopy.
This calculation concerns the full six-frame, rather than an
unframed immersion class. The projection-normal-plus-height Smale
integer is therefore unchanged by this circular-height coordinate
arrow with its transported frame.

The relevant primary formula has been reopened in Takase,
arXiv:math/0506356: proof of Theorem3.1, printed pp6--7, compresses a
specified third normal field while retaining the framing; the proof
of Theorem3.2 gives 2*omega=3*sigma+e^2 for that frame. The exact
Kummer normalization and omega=-2 for F56's original projection are
already P3F.55/P3K.42. Applying this value to a new fan requires the
actual graph/cap identification described next; no new value is
entered here.

## SFIX.3. Specific remaining arrows in the circular-height route

The actual h_n=hB^n changes the relative branch-height label by the
corresponding integer B-deck count. On the normalization annulus its
ordinary source/line logarithms and the source fractional-translation
map must be used, not replaced by a freely chosen phase. The exact
source reparametrization is F56 SC.10a:

\[
 T_t(s,rho)-s=\frac{h_t(s^2-rho^2)}{2+h_t(rho-s)}.
\]

For a bounded angular height whose derivative is O(1/r), the derivative
of this reparametrization is still I+O(r): its derivative in t has
order r^2. Thus such a height can be retained in the small source
normalization chart. The integer branch label must be retained when
the real height is quotiented by the gamma deck.

The candidate inner ambient region is B^6 times the gamma circle.
Its boundary is S^5 times S^1. A gamma circle over a source point
outside the projected knot has a product tubular neighborhood
D^5 times S^1. Attaching the corresponding seven-dimensional
2-handle replaces this neighborhood by S^4 times D^2, giving the
standard S^6 decomposition (D^5 times S^1) union (S^4 times D^2).
The actual source-line trivialization along that attaching circle
must be extended using its fixed scalar and the source/line logs
that extend over the rho disc. This would retain the Thom line
through the handle; its winding must not be chosen afterward.

There are two remaining checks before this is a characteristic
calculation for T_n:

1. Construct the quotient-body/graph arrow for the whole actual
   shear fan, including both branch neighborhoods and the source
   period hB^n, as an embedding in this source-circle product. The
   integer branch label cannot be removed by compressing its real
   height into a short arc.
2. Match the actual principal Cartier twist in (SFIX.1) on the
   inner and outer surgery collars. The adjoint normal action is
   already identity on the common open star, but the extension of
   the circle line and its cap framing at D_+ and D_- must be
   written explicitly. Only after that comparison can K42's
   sphere-bundle pair be retained or corrected.

No equality ell=0, full integer A, or full pair (k,ell) is recorded
from this working route. The exact proved shear-fan result remains
P3K.56.

## SFIX.4. Typed Cartier spinor comparison under the actual shear

The scalar open-star gauge must not be regarded as an automorphism of
an unchanged framed spinor. In the delta-centralizer U(2), its determinant
has winding +2n around D_+ and -2n around D_-. It therefore does not
extend as that unchanged centralizer gauge over either branch disc.

The actual new coefficient arrow instead determines a tensor line. In
SP.7's fixed order, both right-complex spinor coefficients acquire the
unitary factor phase(Z)^n. The actual spinor is consequently

\[
 M_n=\mathcal O(n(D_+-D_-)),\qquad
 E_n=E\otimes M_n
 =\mathcal O((n+1)D_+-nD_-)\oplus
   \mathcal O(nD_+-(n+1)D_-).                         \tag{SFIX.5}
\]

Here the passage from the conjugate of the negative physical weight
line to M_n uses its Hermitian dual; the positive modulus is retained
by the corresponding positive normal rescaling. The product normal
line Hom(first,second) remains exactly O(-D_+-D_-).

In the finite (x,y) chart the actual Cartier generators are

\[
 e_{1,n}=x^{-n-1}y^n,\qquad e_{2,n}=x^{-n}y^{n+1}.
                                                               \tag{SFIX.6}
\]

Their wedge is Z^(-2n-1); the determinant trivialization is multiplication
by Z^(2n+1). The scalar meromorphic expression Z^n defines the typed
morphism

\[
 E_n\longrightarrow E,\qquad v\longmapsto Z^n v,     \tag{SFIX.7}
\]

because its source is the tensor line in (SFIX.5). This is a holomorphic
Cartier-line isomorphism also at x=0, y=0 and their intersection: it
sends the generators in (SFIX.6) exactly to (1/x,y). Its inverse is
multiplication by Z^(-n) with the opposite source/target types. These
are nonvanishing bundle morphisms even though their expressions as
meromorphic functions have zeros and poles.

On y!=0 the coefficient arrow to SP.8's standard dual-tautological and
tautological frames, after (SFIX.7), is therefore literally

\[
                         \operatorname{diag}(1/y,y).
                                                               \tag{SFIX.8}
\]

The x-chart gives the identical overlap. Its Hermitian normalization
and the fixed summand swap give the same matrix g(x,y) in SP.9.
This is a concrete cancellation of the principal Cartier tensor line;
it is not an extension of the nonextending scalar function gauge.
The corresponding new normal Hopf line is the old tautological line
tensored by the pullback of M_n. Its global Cartier generator Z^(-n)
must be used when matching that line on both surgery collars.

This establishes the typed local spinor calculation. To retain SP.20
for the actual completed fan, the new outer Cox collar must be matched
using precisely this tensor trivialization and the actual B^n source/
line reindex in the second chart. No additional rho-dependent circle
phase may be discarded. The full ambient graph/annular comparison in
SFIX.3 remains a separate required step.

For comparison, an ordinary SU(2) contraction of the diagonal phase on
a branch disc carries a nonconstant physical circle axis. With H_d of
GF.9, the actual new-to-old arrow uses H_n^(-1) near D_+ and H_n near
D_- (constant torus factors from the other nonzero coordinate retained).
The two transported axes have degrees +n and -n in the GF cylinder
orientation. Their boundary eigenline generators are Z^(-n) in the
positive line and Z^n in the negative line, precisely the Cartier
transition in (SFIX.5). A claim that these axes remain constant would
lose those divisors. The tensor-line calculation (SFIX.5)--(SFIX.8)
keeps them without making that claim.
