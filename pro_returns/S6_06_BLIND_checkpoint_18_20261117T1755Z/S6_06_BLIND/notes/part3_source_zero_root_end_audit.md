# Exact defining functions on the reduced source-zero lower arm

17 November 2026. This note audits the actual real cut in RT.13.
It does not assign the unresolved source-zero return.

We retain the reduced branch a=2 and the primary positive auxiliary
quotient with coordinates (S0,S1,T1,z,V), of weights (1,1,-1,1,-2).
Its actual functions are

\[
 H=|S_0|^2+|S_1|^2+|z|^2,\quad
 \rho^2=H|T_1|^2+H^2|V|^2,
\]
\[
 R^2=(|S_0|^2+|S_1|^2)(|T_1|^2+|zV|^2).
\]

Put A=|z|²/H, b=H|T1|², c=H²|V|² and u=b/(b+c) on
the nonzero radial boundary. These are invariant under the positive
real auxiliary gauge. Direct substitution gives

\[
 \rho^2=b+c,\qquad
 R^2=(1-A)(b+Ac),\qquad
 \frac{R^2}{\rho^2}=(1-A)\bigl(A+(1-A)u\bigr).
 \tag{RE.1}
\]

Choose the actual compact cut rho≤rho0 and R≥epsilon with
0<tau=epsilon/rho0<1/2. On its corner rho=rho0, R=epsilon,
the lower arm is parametrized by

\[
 0\le A\le A_-:=\frac{1-\sqrt{1-4\tau^2}}2,
 \qquad
 u=\frac{\tau^2-A+A^2}{(1-A)^2}.
 \tag{RE.2}
\]

The numerator is nonnegative on this interval and vanishes at A_-.
The derivative of u is (A+2tau²-1)/(1-A)³. Since A_-<1/2
and tau²<1/4, it is strictly negative. Thus
0≤u≤tau²<1/4, and c=(1-u)rho0² is positive. In particular
the literal V≠0 chart applies on this whole lower corner arm.
The upper arm lies in A≥A_+=(1+sqrt(1-4tau²))/2; the two
arms have disjoint closures for this fixed choice of tau.

Use the actual primary-negative V=1 chart, with its residual mu2
and its physical weights (-1,-1,+1,+1)/2 in the order
(S0,S1,T1,z). Let x=(S0,S1,z), y=T1, and let
sigma²=||x||²+|y|² be its charged Euclidean radial function.
The positive real auxiliary normalization to H=1 has factor
H_raw^(-1/2), where H_raw=||x||². In that normalization
V becomes H_raw and T1 becomes sqrt(H_raw) y. Consequently

\[
 c=\|x\|^4,\qquad b=\|x\|^2|y|^2,\qquad
 \rho^2=\|x\|^2\sigma^2,
\]
\[
 \sigma^2=\frac{\rho^2}{\sqrt c}
          =\frac{\rho}{\sqrt{1-u}},\qquad
 \rho=\sigma^2\sqrt{1-u}.                           \tag{RE.3}
\]

This is an equality of the actual defining functions in the same
charged chart. On the lower arm the factor sqrt(1-u) lies in
[sqrt(1-tau²),1] and is strictly positive. It therefore preserves
the retained/excised side for the corresponding pulled-back
boundary function. The identity coordinate arrow retains the full
source functions q and v and every line coefficient.

Equation (RE.3) does not identify the level rho=rho0 with a fixed
Euclidean sphere by the identity: its exact image is
sigma²=rho0/sqrt(1-u). The displayed positive angular factor is
part of that transported truncation. The radial map multiplying
all charged coordinates by (1-u)^(1/4) would take it to
sigma²=rho0, but it changes the source functions. We have not
used that radial map as a family arrow preserving q and v.

The lower core has z=T1=0 and fixed rho, so it is the sphere
bundle of O(-2) over CP1, namely the explicit quotient S3/{±1}.
Its two complex normal coordinates have the residual action -1.
Thus its actual normal disk bundle is (S3×D4)/{±1}, with the
diagonal sign action. This is the same residual quotient carried
by EA.22; the auxiliary chamber and boundary side remain those
specified above.

For the real rank-four normal action -I4, the two lifts to Spin(4)
are ±e1e2e3e4, and each has square1. Their quotient is the
nontrivial sign character on the actual deck group Z/2. The
complex normal determinant is trivial, and that determinant
alone does not choose between those two lifts. The global
attachment must carry the lift determined by the actual complex
spin-c structure, physical line, and Cox/Cartier derivative.
The positive boundary factor in (RE.3) supplies its orientation
comparison but does not supply this remaining lift by itself.

## A full charged truncation with the exact prescribed lower arm

The preceding defining-function equality yields an actual compact
comparison, without applying the radial map to the source functions.
On the charged unit sphere modulo mu2, let u=|y|²/sigma². The
closed lower corner arm has u≤tau²<1/4. Choose a smooth invariant
function chi(u) equal to1 on a neighbourhood of [0,tau²] and
equal to0 for u≥1/2. Define

\[
 f=1-\chi(u)\bigl(1-\sqrt{1-u}\bigr),\qquad
 Y_f=\{\sigma^2 f=\rho_0\}/\mu_2.
 \tag{RE.4}
\]

The product involving the square root is set to zero on u≥1/2;
it is smooth there because chi vanishes on a neighbourhood of
that closed set. The resulting function is smooth on the whole
charged sphere, invariant under the physical circle, and lies
between 1/sqrt2 and1. Its homogeneous extension off the origin
defines Y_f as a smooth closed star-shaped hypersurface.
On a neighbourhood of the entire lower arm its equation is
exactly rho=rho0 by (RE.3).

The charged-coordinate identity EA.22 pulls back this full
defining function to the complementary U=1 chart. The source
functions q and v are identical under that arrow. The pullback
therefore matches the actual lower face, its line, and its
retained/excised side exactly. It carries the specified residual
mu2 and the canonical complex spin-c lift, whose explicit
volume comparison is retained in EA/RT's spin calculation.

Here is the complete characteristic comparison to the round link.
Take the actual compact region in this same charged chart

\[
 \mathcal A_f=
 \{\rho_0/2\le\sigma^2\le\rho_0/f\}/\mu_2.
 \tag{RE.5}
\]

The inner boundary has the strictly smaller squared radius rho0/2.
Since f≤1, the outer squared radius is at least rho0, and the
interval has positive width everywhere. Thus (RE.5) is an honest
smooth radial interval bundle over the whole charged angular
sphere quotient. The choice of the smaller inner round link changes
neither the actual outer cut nor any gluing arrow. It also avoids
coincident faces on the angular set where f=1. The first version of
this paragraph used the coincident inner radius and is preserved in
`records/attempts/source_zero_root_shape_annulus/pre_strict_inner_radius.md`;
the strictly smaller inner radius is the construction used here.

The origin does not occur. The mu2 action is free on the punctured
charged chart, and the effective physical circle has weights
(-1,-1,+1,+1)/2 with that mu2 identification. It is free on this
region: a stabilizing circle phase lifts to the common scalar
sign on all nonzero coordinates and is exactly the already
quotiented mu2 element. Thus A_f/S1 is a compact oriented
seven-dimensional bordism from the round quotient to Y_f/S1.
Its physical line and stable tangent bundle are the ones induced
by these actual free actions, and restrict to those on both ends.
Stokes applied to their closed characteristic forms gives

\[
 \int_{Y_f/S^1}x^3=\int_{Y_{\rm round}/S^1}x^3,
 \qquad
 \int_{Y_f/S^1}p_1x=\int_{Y_{\rm round}/S^1}p_1x.
 \tag{RE.6}
\]

The outward orientation on the inner round boundary is reversed
in this bordism, which supplies the displayed equality. Both
source functions q,v are retained by ambient inclusion on A_f.
For sufficiently small rho0 the entire compact annulus is inside
the original charged chart. No assertion that a radial
normalization preserves q or v is used here.

The physical pair of the round charged link can also be read from
an explicit bundle morphism. Conjugate the two negative-weight
complex coordinates, which preserves the real eight-dimensional
orientation. The link becomes S7/mu2 with the physical action
u↦exp(it/2)u, and its quotient is CP3. The actual associated
physical line has the map

\[
 [u,z]\longmapsto z\,u^{\otimes2}\in O_{\mathbb P^3}(-2).
 \tag{RE.7}
\]

The mu2 action leaves u⊗2 unchanged, and the physical circle
multiplies u⊗2 by exp(it), exactly canceled by the associated
coefficient exp(-it). This proves the displayed line morphism.
With H the positive hyperplane class, its first Chern class is
x=-2H. The complex Euler sequence gives
p1(TCP3)=c1²-2c2=(16-12)H²=4H², and the complex orientation
gives integral H³=1. Hence both the round link and Y_f have

\[
 (k_M,\ell_M)=(-8,-8),\qquad
 (4k_M-\ell_M)/24=-1.                              \tag{RE.8}
\]

This is the characteristic pair of this specified internal charged
boundary. Its sign in the eventual complete boundary equation is
still determined by whether that boundary is retained or excised
in the actual period-strip attachment.

This constructs a full charged boundary with the required local
face and proves its characteristic pair by an actual bordism.
Its remaining period-strip faces and the global ownership of
the fixed cap are the separate EA/RT attachment obligation.

## The full quaternion overlap on the charged boundary

We give its complement map, retaining the actual Hopf lift. After
the two negative-coordinate conjugations put

\[
 p=\overline{S_0}+j\overline{S_1},\qquad q=T_1+jz.
\]

The effective physical circle is right multiplication by exp(it/2)
on both quaternions, with the common sign already quotiented.
On q≠0 define

\[
 w=pq^{-1},\qquad u=q/|q|,\qquad h=u i u^{-1}.
\]

On p≠0 define w'=qp^{-1}, u'=p/|p| and h'=u'i(u')^-1.
On their full overlap the exact identities are

\[
 w'=w^{-1},\qquad u'=g u,\qquad
 h'=g h g^{-1},\qquad g=w/|w|.                     \tag{RE.9}
\]

The Hopf lift u'=gu commutes with the right physical circle and
with its residual sign. On the common unit boundary |w|=1 the
fibre clutch is exactly (h,w)↦(w h w^-1,w), the inverse of
the recorded ruling map tau(h,w)=(w^-1 h w,w). The base-coordinate
change w'=w^-1 is retained as well; it is not discarded when
assigning an orientation to the two four-dimensional hemispheres.

These formulas apply to the transported hypersurface Y_f itself.
Write r=|q| and r'=|p|. Its two reconstructions are

\[
 (p,q)=(rwu,ru)=(r'u',r'w'u'),\qquad r'=|w|r.
 \tag{RE.10}
\]

For Y_f, r is the positive solution of
r²(1+|w|²)f([wu,u])=rho0. The angular function is independent
of the right physical phase, so this equation determines r on
the actual circle quotient. Formula (RE.10) proves that the two
charts are descriptions of precisely the same charged point.
Every source function q_source,v and every carried line function
therefore has identical values on the overlap. In particular the
actual primary source product q_source=S0 z is retained.

The lower core is q=0, p≠0; its tubular orbit chart is a disk
bundle over its Hopf S2. The complementary core is p=0, q≠0
and has the other such chart. The two core neighbourhoods are
the explicit |p|≥|q| and |q|≥|p| portions, with their common
unit-quaternion clutch (RE.9). Their underlying real disk bundles
have the actual Hopf descriptions above; no trivialization is
used to erase the line or the clutch. Identifying this map with
a finite period-strip face still requires matching its g to that
face's specified native quaternion q_H and retaining the base
and normal orientations. The present calculation supplies the
complete charged-boundary side of that comparison.

The exact symbolic identities in this note are executed in
`code/part3_root/source_zero_end_defining_functions.py`, with
the output retained. The analytic region and the two-arm
attachment are RT.13–14 and EA.9–12. No local characteristic
number is substituted for the global return in this audit.
