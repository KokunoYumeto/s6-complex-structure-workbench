# Selected-I3: the directed second-Chern clutch of the moving face

This calculates the two actual positive-spinor bundles constructed in
MC3.1--6. It keeps the original M6, translation -G, quadratic cap,
norm one, finite character, complete reference, coupled scalar root
s^2 r0, and positive original s meridian. The source and normal
charts are exactly MS3, and the exterior transfer is exactly ASI3.
The ordered positive spinor is (conjugate(a_N),c_N).

The completed collision bundle and fixed-source reference bundle have

\[
 \int_{F_c}c_2(E_c)=-19,\qquad
 \int_{F_{r,c}}c_2(E_{r,c})=0.                 \tag{IC2.1}
\]

The following maps and intersection computation derive these integers.
They also evaluate the previously retained MC3 quantity kappa as -56.
No return residue is used to determine any of them.

## IC2.1. The exact boundary map after the specified cap product

Write N_theta for MS3.12 followed by the whole point-to-tensor
coefficient and MC3.9. This is the map from the resolved normal bundle
to the ordinary right-complex Cox frame. MC3's actual map to the cut
family is B_theta=C_theta^-1 N_theta. Its actual cap map Chat_theta
restricts to C_theta on the common boundary, and its seam is
Ehat=Chat_1^-1 Chat_0. Therefore, on that entire boundary,

\[
                \widehat C_\theta B_\theta=N_\theta.
                                                        \tag{IC2.2}
\]

The same equality holds for the inverse maps. The base equality is
the corresponding equality of the exact Hermitian-ball maps, and the
normal equality uses the complete matrices of MC3.10--11a. Thus
pullback by the specified cap product leaves precisely the periodic
N_theta as the clutch. It retains every P power of the endpoint and
every unit in C, B and Chat. Applying complex conjugation to their
right-complex coefficient columns gives the actual positive complex
bundle and the same equality IC2.2.

For later use the two positive Cox frames are

\[
 G_0(Z)=\begin{pmatrix}1&-Z\\\overline Z&1\end{pmatrix},\qquad
 G_1(w)=\begin{pmatrix}\overline w&-1\\1&w\end{pmatrix},
\]
\[
 G_1(1/Z)\operatorname{diag}(\overline Z,Z)=G_0(Z).
                                                        \tag{IC2.3}
\]

They are obtained by conjugating the two coefficient expressions of
the same q_H in MC3.9. Both determinants are positive. In this global
rank-two frame the two ordered line subspaces are
C(1,bar Z) and C(-Z,1); their coefficient transitions are bar Z and Z,
so their first Chern classes on the complex Z sphere are +h and -h.
These are the line subbundles used on the reference cap below.

## IC2.2. The complete collision coefficient and its divisor lines

The surface F_star has the 36 charts and 34 chronological blowups of
MS3. Its dense coordinates are the actual Z,P. The original parameter
on this surface is s=-P/u_s(P,0), with nonzero derivative at zero.
This map has positive meridian degree one. Every normal coefficient
below is evaluated at the actual fixed surface p=0; q_old has zero
first normal derivative there, as follows from q_old=Z a_N c_N.
Thus this is the exact normal derivative of the complete source map.

Keep the meromorphic normal functions

\[
 F_+=V_{\rm pt}/Z^2,\quad F_-=pZ^2/V_{\rm pt},\qquad
 a_N=P c_q Z^{-3}F_-,\quad c_N=Z^2F_+ .          \tag{IC2.4}
\]

The last two equalities are MS3.12, directed from the resolved normal
bundle to the original native coefficients. Their inverses divide by
these full coefficients on each common localized chart. The second
sphere chart has a_N'=Za_N and c_N'=Zc_N. The exact positive-spinor
coefficient map before G_0 is consequently

\[
 (\overline{F_-},F_+)\longmapsto
 (\overline P\,\overline{c_q}\,\overline Z^{-3}
          \overline{F_-},\ Z^2F_+).              \tag{IC2.5}
\]

The full point-to-tensor factor further multiplies the two entries
by bar chi6^-1 and chi6, with the exact chi6 of MS3.13. The functions
c_q(P,0), chi6(P), and u_s(P,0) are units on the whole small P disc.
For each of them write its actual value as u(0) exp L(P), using the
unique based logarithm. The path u(0) exp(t L(P)), followed by its
constant value, is an explicit homotopy through nonzero coefficients.
Its positive modulus has its real logarithm. These full coefficient
maps and their reciprocal paths extend over the cap: use a radial
cutoff on D3, zero near its centre and one near its boundary, in the
exponential of the corresponding global projector in IC2.3. The
periodic logarithm makes this well-defined on S1. This gives a smooth
map at the centre and an explicit inverse. In particular these units
contribute no parameter degree. The factor bar P in IC2.5 is retained.

The complete derivative characters in the 36 charts have horizontal
orders (3,-2) for dF_- and (-2,3) for dF_+, and zero order on every
vertical tangent ray. Their actual line-module identifications are
therefore

\[
 N_-\simeq\mathcal O(-3D_0+2D_\infty),\qquad
 N_+\simeq\mathcal O(2D_0-3D_\infty).             \tag{IC2.6}
\]

Here the meromorphic dual sections dF_- and dF_+ specify the displayed
divisor-line maps in every chart; the inverse monomial generators
specify their inverses. For a chosen Hermitian metric, the map
bar N_- to N_-^* sending bar v to the functional w mapped to
<w,v> is complex-linear and invertible. Its local metric coefficient
is positive. It carries the first positive summand to the divisor line
O(3D0-2Dinfty). This proves the sign using an explicit bundle map.
The second positive summand is N_+ itself. Their parameter clutch
remains the directed map IC2.5, including all positive metric factors.

## IC2.3. The actual cap replacement and oriented closed surface

After IC2.2 the cap is C0=-D3_Z times S1_P with its trivial rank-two
positive bundle in the conjugated Cox frame. Put C=P1_Z times D2_P.
The actual oriented product gives

\[
 \partial(D^3_Z\times D^2_P)=C+C_0,\qquad
 F_c-(F_{\rm star}-C)=C_0+C.                    \tag{IC2.7}
\]

Round the product corner using its two radial variables. Its rounded
facet is the common boundary times an interval. Attach it to the
boundary collar of F_star times that interval, carrying the same full
coefficient map N constantly along the interval. The rank-two bundle
over D3 times D2 is trivial in the specified Cox frame. This constructs
an explicit five-dimensional bundle bordism between the actual
(F_c,E_c) and a bundle on F_star-C. On the new -C face retain the two
line subbundles of IC2.3, constant in its parameter coordinate. Thus
the replacement bundle splits into two complex lines. The full
boundary arrow IC2.5 preserves precisely these two subspaces.

Let rho0 be the P-disc radius. On the abstract reference disc use
eta=bar xi/rho0^2. This map has negative real determinant and equals
1/P on the common boundary xi=P. Consequently -C has its eta-complex
orientation. The resulting closed surface is the actual 34-fold
blowup of P1_Z times P1_parameter, with all the recorded blowups in
the original P disc. Write U for the pullback of the positive
parameter class, and retain the strict sections D0,Dinfty. The exact
chronological maps give

\[
 D_0^2=-3,\quad D_\infty^2=0,\quad D_0D_\infty=0,
 \quad U^2=0,\quad UD_0=UD_\infty=1.             \tag{IC2.8}
\]

Indeed exactly three of the recorded blowup centres lie on the
successive strict zero section and none lie on the infinity section.
The sections remain disjoint. Each intersects a generic fibre once.
Every other centre and every infinitely near exceptional divisor is
retained in the 34 explicit monomial blowup maps. The independent
certificate reconstructs their order and their intersection matrix.

Compatible connections on this constructed bordism give equality of
the second Chern numbers on its two closed boundary bundles by Stokes.
The same applies to c1 squared. This uses the actual map IC2.2 to the
specified cap, so the bordism carries its complete normal clutch.

## IC2.4. The two collision roots with their parameter coefficients

For a boundary coefficient arrow z_cap=P^n z_F, the section with
coefficient one in the original disc has coefficient eta^-n in the
new cap chart. Its parameter degree is -n. In IC2.5, bar P has phase
P^-1; their ratio is the positive |P|^2. The positive homotopy and
its inverse are explicit and extend over the cap. The two directed
parameter exponents are therefore (-1,0), and their degrees are (1,0).

The horizontal factors bar Z^-3 and Z^2 are also retained. On the
second sphere chart they become bar Z^-2 and Z^3. Their local section
indices give the horizontal classes (3D0-2Dinfty) and
(2D0-3Dinfty), respectively, in agreement with the divisor maps
IC2.6. The two complete roots on the replacement closed surface are

\[
 x_1=3D_0-2D_\infty+U,\qquad
 x_2=2D_0-3D_\infty.                            \tag{IC2.9}
\]

All vertical exceptional corrections are included in these strict
divisor classes; their original tangent monomial orders are zero.
Using IC2.8 gives directly

\[
 \int x_1x_2=6(-3)+(2-3)=-19,\qquad
 \int(x_1+x_2)^2=25(-3)=-75.                    \tag{IC2.10}
\]

The latter reproduces MC3's independently determined determinant
pairing. IC2.7 transfers the first equality to the actual E_c and
proves the first number in IC2.1.

## IC2.5. The entire fixed-source reference clutch

Keep the six-factor reference of MC3.5, including its actual h and B
source/line periods. Its moving face is P1 times D_s, with no point
blowups. In its y-factor chart its full normal map is

\[
 a_N=\kappa_{\rm sel}^{-1}s^{-4}v_r,\qquad
 c_N=s^4u_r .                                    \tag{IC2.11}
\]

The x-factor chart is the actual source-period image, with the full
alpha,Gamma factors and their inverses. These two charts give the
same ordered native line subbundles of IC2.3. The source coefficient
kappa_sel is a unit of the fixed source; its logarithm and inverse
extend in the same explicit way as above. In the positive spinor,
the two parameter phases in IC2.11 are both s^4. The first follows
by conjugating s^-4; the ratio to s^4 is the positive |s|^-8.
Thus both directed parameter degrees are -4.

Apply the identical IC2.2 cap product and IC2.7 bordism, using the
fixed-source functions in MC3. There are no exceptional classes.
The two complete reference roots on P1 times P1 are

\[
                 h-4U,\qquad -h-4U,
 \quad h^2=U^2=0,\quad\int hU=1.                 \tag{IC2.12}
\]

Their product is zero. The common phase s^4 also extends directly
over the actual C0 as a scalar map constant on the ball. Both
calculations retain its winding four and give the second number in
IC2.1. The reference tangent number and determinant square are zero,
as already supplied by MC3's full source/reference construction.

## IC2.6. The completed integer pair and its physical coordinate map

MC3.17 evaluates the collision contribution as
(-75-c2(E_c),-177-4c2(E_c)). Substituting the two directed Chern
numbers IC2.1 gives

\[
 (k_M,\ell_M)_{\rm moving-reference}=(-56,-101),
 \qquad\kappa=-56.                               \tag{IC2.13}
\]

The four lower doubles and all compact components retain their
already audited pairs (72,-348) and (-63,453). Their sum with
IC2.13 is (-47,4). The actual ASI3 Stokes arrow and parameter
reversal therefore give the complete fixed-scalar Jin pair

\[
              (k_M,\ell_M)=(47,-4).                \tag{IC2.14}
\]

Its index is 8. This index agrees with ASI3's earlier cancellation
of the unassigned kappa, now through the independently calculated
bundle clutch. The actual K68 map k_M=mu+nu, ell_M=4mu gives

\[
                 (\mu_{C0},\nu_{C0})=(-1,48).      \tag{IC2.15}
\]

This is the fixed-C0 product of MC3 and ASI3. The separately computed
C2 native pair of IF3 retains its own cycle/frame map and equals
(8,-6). All original parameter, physical-line and commutator
orientations remain those displayed in those proofs.

The companion exact certificate reconstructs all 36 derivative
charts, all 34 blowups, the complete intersection matrix, both Cox
frames, both directed coefficient exponents and Chern products, and
the complete physical sums. The cap-bundle morphism and bordism are
the explicit constructions IC2.2--7, rather than a numerical choice
of a second-Chern lift.
