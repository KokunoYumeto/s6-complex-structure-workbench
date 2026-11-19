# Selected-I3: the actual moving-star cap and its reference

This continues MS3 for the specified M6,b=1,m=2,n=1 family,
initial T0 and scalar root s^2 r0. The 36 selected charts and
their 34 ordinary blowups remain those of MS3. No value for the
second Chern number of the completed normal bundle is chosen.
The calculation here supplies the moving-face term with the
full ordinary/root closing, before the outer return comparison.

## MC3.1. The complete selected endpoint and its normal arrows

Write A=(c_q/c0)^2, with c0=(p-1)^4c as in SI3. The forward
ordinary endpoint is q_old^2 and its actual B^-2 representative is

\[
 E:(Z,V_{\rm pt})\longmapsto(P^2Z,P^{-2}A V_{\rm pt}).
 \tag{MC3.1}
\]

P,p, all source-height functions and the full unit A are unchanged
by this arrow. On the ordinary native chart q_old=Z a_N c_N,
V_pt=c_N, the same arrow is exactly

\[
 (Z,a_N,c_N)\longmapsto(P^2Z,A^{-1}a_N,P^{-2}A c_N).
 \tag{MC3.2}
\]

The reciprocal coefficients give its inverse. In particular the
product Z a_N c_N, including its entire source dependence, is
unchanged. The second chart uses Z'=1/Z and a_N'=Za_N,
c_N'=Zc_N; substitution into MC3.2 gives its complete arrow.

In the meromorphic derivative frames of MS3.7, the same map is

\[
 F_-\longmapsto P^6A^{-1}F_-,\qquad
 F_+\longmapsto P^{-6}A F_+.
 \tag{MC3.3}
\]

These factors commute with every original period and with the
physical circle. They are related to MC3.2 by the full coefficient
map a_N=P c_q Z^{-3}F_-, c_N=Z^2F_+ at its two different base
points Z and P^2Z. Thus, for example,

\[
 P c_q(P^2Z)^{-3}(P^6A^{-1}F_-)
       =A^{-1}P c_q Z^{-3}F_-.
 \tag{MC3.4}
\]

The determinant phase of the positive spinor
(conjugate(a_N),c_N) in MC3.2 is
(P/|P|)^(-2)(A/|A|)^2; its winding is -2. The phase in
the MS3.7 frame has winding -12. The coefficient map in MC3.4
has precisely the intervening base-dependent factor: its phase
contains Z^5/|Z|^5, whose value changes by (P/|P|)^10 under
Z to P^2Z. This proves the equality of the two normal arrows
with their windings retained. Neither winding is removed by
calling the normal coefficient an extending unit.

The full point-to-tensor coefficient is the entire Cartier/theta
ratio in MS3.13. Its restriction to this fixed surface is chi6(P),
with chi6(0)=-1. It acts by chi6^-1 on a_N and chi6 on c_N.
This is a unit on the selected parameter disc. Its off-surface
source derivatives remain in the original map, and q_old has
zero first normal derivative on the fixed surface. The stated
restriction is therefore the exact normal derivative.

## MC3.2. A closed selected collar carrying the endpoint

Take a cut positive parameter circle s(theta), 0<=theta<=1,
and a smaller selected q_old-disc on that circle. P(q_old,s)
is nonzero on this compact collar. Choose its continuous
logarithm on the cut, and the analytic logarithm of A. Let
chi(theta) be smooth, zero on an initial collar and one on a
terminal collar. Put

\[
 \alpha_\theta=\exp[-\chi(\theta)\log(P^2)],\qquad
 \beta_\theta=\exp[-\chi(\theta)\log(P^{-2}A)],
\]
\[
 C_\theta:(Z,a_N,c_N)\longmapsto
 (\alpha_\theta Z,
  (\alpha_\theta\beta_\theta)^{-1}a_N,
  \beta_\theta c_N).
 \tag{MC3.5}
\]

All functions are evaluated at the original q_old and s(theta).
The map preserves q_old exactly, so its inverse is obtained by
the reciprocal coefficients at that same q_old. It is a
diffeomorphism on a possibly smaller compact collar. Its
extension to the other Cox chart is obtained by the literal
transition above. On full parameter collars it satisfies

\[
                  C_{\theta+1} E=C_\theta .
 \tag{MC3.6}
\]

One defines the next cut by this equation. Near each cut end
MC3.5 is respectively the identity or E^-1, so the equation
holds with all derivatives, not just at theta=0,1.

This is also an actual local isotopy of the physical family.
Its time derivative in the displayed coordinates has components

\[
 (\partial_\theta\log\alpha)Z\partial_Z
 -(\partial_\theta\log(\alpha\beta))a_N\partial_{a_N}
 +(\partial_\theta\log\beta)c_N\partial_{c_N},
 \tag{MC3.7}
\]

together with its real conjugate. Its derivative of q_old is
zero. In the source-family chart include the prescribed
horizontal lift that keeps this actual q_old fixed. This
specifies the complete parameter-dependent field, including
the q_old derivatives of P,A. The two Cox charts give the
same field because they give the same maps MC3.5.

In these chosen q-preserving cut-family coordinates the
cutoff below acts on the vertical correction Cdot C^-1;
the prescribed parameter-horizontal lift remains in
place outside the tube. Choose an invariant cutoff equal to one on this smaller
fixed tube and zero outside a larger selected tube, both
disjoint from the quadratic cap, its annular overlap and
the outer source boundary. Extend the field by zero and
integrate it on the compact fibre over the cut. The flow
is complete for the parameter interval and commutes with
the physical circle. On the smaller tube its solution is
exactly MC3.5, and on the finite cap and side boundary it
is the identity. Thus the full forward endpoint is changed
by the actual interval family to one which is identity on
the selected tube; its finite-cap value remains h^2.
The source/line annular map is transported by this interval
family and is unchanged on the actual cap overlap. Its
directed square remains

\[
            \Phi_{\rho+2}q_{\rm old}^{\,2}=h^2\Phi_\rho,
 \tag{MC3.8}
\]

with every reference integer, finite character and inverse
arrow from SI3.9a--b. This construction does not extend the
P powers in MC3.1 through the central fourfold.

## MC3.3. The full normal clutch and the cap base

Here is a global expression for the normal-sphere coordinate.
In the finite Z chart put

\[
 T_Z=\begin{pmatrix}1&-\overline Z\\Z&1\end{pmatrix},
 \qquad q_H=T_Z(a_N,\overline{c_N})^t.
 \tag{MC3.9}
\]

In the inverse chart use
T'_z=[[z,-1],[1,conjugate(z)]]. The exact identity
T'_(1/Z) diag(Z,conjugate(Z))=T_Z proves that these are
one global quaternion coefficient. The physical circle
acts by its negative right phase. The positive spinor is
(conjugate(a_N),c_N); MC3.9 is the actual anti-linear
coefficient arrow of K68 PL.2.

Consequently the full boundary normal arrow of MC3.5, in
these right-complex coordinates, is

\[
 G_\theta(Z)=T_{\alpha_\theta Z}
 \operatorname{diag}((\alpha_\theta\beta_\theta)^{-1},
                       \overline{\beta_\theta})T_Z^{-1}.
 \tag{MC3.10}
\]

The complete MS3.12 and point/tensor coefficients are
composed before this arrow when starting in a resolved
chart. The inverse is the inverse of this displayed
product. On the unit sphere use Gq_H/||Gq_H|| with the
transported Hermitian metric. Its full positive part can
equivalently be retained by the explicit path
G(G*G)^(-t/2); this preserves the physical character and
never substitutes a multiplicative polar projection.
No SU2 factor or degree of MC3.10 is deleted.

The fixed-sphere base map is Z to alpha_theta Z. Realize
the closed three-ball as the positive semidefinite
Hermitian matrices Y of trace one. For
B_theta=diag(alpha_theta(0),1), its exact extension is

\[
 \Psi_{B_\theta}(Y)=
       B_\theta YB_\theta^*/\operatorname{tr}(B_\theta YB_\theta^*).
 \tag{MC3.11}
\]

The boundary-coordinate convention is explicitly
Y_Z=(1+|Z|^2)^(-1)[[|Z|^2,Z],[conjugate(Z),1]].
Consequently the displayed diagonal matrix sends
Y_Z to Y_(alpha_theta Z). This is the fixed-sphere
base convention; the normal quaternion matrices in
MC3.9 remain the separately typed fibre convention.

Its inverse is Psi_(B_theta^-1). The denominator is
positive on the closed ball. On its rank-one boundary
it is exactly the stated Möbius map. Composition respects
matrix multiplication and hence the full cut identity
MC3.6, using diag(P(0)^2,1) on the forward seam. Thus
the ball mapping torus with this actual seam is identified
by MC3.11 with D3 times S1. The normal Hopf factor is
the q_H of MC3.9, with its entire boundary clutch MC3.10.
It is a separate factor from this fixed-sphere base map.

The cut normal maps themselves have the following explicit
ball extension, which also specifies the endpoint typing.
Choose a radial cutoff tau on this ball, zero near its
centre and one near its boundary. In MC3.10 replace
alpha_theta,beta_theta by
exp(tau log alpha_theta),exp(tau log beta_theta), and
evaluate Z at the direction of the radial vector. Near
the centre the matrix is the identity and is independent
of that direction, so this formula is smooth there.
Call the resulting invertible matrix Ghat_theta(Y).
Together with MC3.11 it defines

\[
 \widehat C_\theta(Y,q_H)=
 (\Psi_{B_\theta}(Y),
     \widehat G_\theta(Y)q_H/\|\widehat G_\theta(Y)q_H\|).
 \tag{MC3.11a}
\]

The inverse first applies Psi_(B_theta^-1) and then the
inverse matrix at that recovered Y. The complete path
of matrices, including the continuous logarithms already
specified on the cut, is retained in this formula.
Define the forward cap seam by
Ehat=Chat_1^-1 Chat_0. Its boundary is exactly the full
E of MC3.1--2, not only its base map. Chat_theta then
identifies this ball/sphere mapping torus with its
literal product. This construction fixes the entire
U2 endpoint map without assigning a degree to it.

For clarity, let N_theta be the full MS3.12 followed by
MC3.9 and the point/tensor map, directed from the resolved
normal to the ordinary native frame. It is periodic in
the raw boundary coordinates. The map to the actual cut
family is B_theta=C_theta^-1 N_theta. Its endpoints obey
B_1=E B_0. On the cap use the seam Ehat just constructed.
The full boundary clutch therefore glues, and after the
product identification Chat_theta it is precisely the
periodic N_theta. These are both directions of the
same bundle map; the P powers and all phases have stayed
in N, C and Chat. No SU2 degree of N is removed.
The q_H coordinate is right-complex and has the negative
physical character. For the positive complex cap bundle
use its conjugate coordinate. Thus the anti-linear
right-complex N_theta is a complex-linear clutch to
that conjugate bundle. This is exactly the coefficient
typing of K68 PL.2, with conjugation applied also to
Ghat and its inverse; it supplies the positive E_c
used in the Chern calculation.

Attach this K68 reference product cap C0=D3 times S1,
oriented oppositely to that product. The resulting
rank-two positive bundle is E_c over F_c, with that
complete clutch. The explicit Chat map is its
identification with the actual product surgery cap.
On the cap the Hermitian dual map of K68 PL.2a and its
inverse carry the physical tautological line M and
the positive hyperplane line U=M*.

## MC3.4. Integral determinant and tangent pairings

The chronological blowdown of MS3 is identity on the
whole outer parameter boundary. Thus F_star has H1=0,
and its H2 is generated by the generic sphere and the
34 actual total-transform exceptional classes. On the
boundary S2 times S1, restriction of H2 has degree one
on that sphere and zero on every exceptional class.
The cap contributes H1=Z with restriction isomorphism
to the boundary H1, and H2=0. The actual integral
Mayer--Vietoris sequence therefore gives

\[
 H^2(F_c;\mathbb Z)\hookrightarrow H^2(F_{\rm star};\mathbb Z),
 \qquad \operatorname{image}=
          \mathbb Z\langle e_1,\ldots,e_{34}\rangle.
 \tag{MC3.12}
\]

In particular the entire determinant phase, including
the winding in MC3.1--4, contributes no extra connecting
class. As a map this can be seen directly: divide a
boundary C* function by its actual e^(i n theta), lift
the zero-period ratio to a logarithm and extend that
logarithm from a collar into D3 times S1 with a cutoff.
The factor e^(i n theta) itself extends on that cap.
This retains n and does not extend it over a parameter
disc.

MS3 gives c1(E)=5(D0-Dinfty), with the explicit compact
representative -5 sum aC_(a,h). It has degree zero on
the boundary sphere. By MC3.12 its unique closed
extension is c1(E_c), and its pairing is the actual
integral intersection already computed in MS3:

\[
                     \int_{F_c}c_1(E_c)^2=-75.
 \tag{MC3.13}
\]

Before the 34 blowups, the base is the union S2 times
D2 with D3 times S1. The boundary Möbius/cut map
extends by MC3.11, so this is the oriented boundary
of D3 times D2, with product collars rounded. Its
stable tangent Pontryagin number is zero. Each
chronological map in MS3.4 has Jacobian a or d and
exceptional square -1; its relative changes are
delta c1^2=-1 and delta c2=1. Hence delta p1=-3.
These maps are identity on the outer boundary and
give, with the complex orientation,

\[
                        \int_{F_c}p_1(TF_c)=-102.
 \tag{MC3.14}
\]

## MC3.5. The actual scalar reference moving face

For the fixed reference source retain its Tate charts
x_i y_i=q_T, q_T=kappa(q_old)q_old, with the full
nonzero kappa. Its actual period maps are
h=(q_T Z,alpha(q_old)V) and
B=(g(q_old)Z,s^4q_T Gamma(q_old)V).
Here alpha=P_sel^6, g=P_sel^-1 and
Gamma=lambda0 kappa^-1 K P_sel^-3, the same entire
point-frame suspension coefficient as I3R.3 at the
fixed source. All these functions are retained.

Use the line chain U_j V_j=s^4q_T. The exact h/B maps
carry its source index and line index, with the complete
alpha and Gamma factors. On a source chart the ordered
factors are (s,s,s,s,y_i,x_i). For its r-th chart put
f_r=u_r v_r, U=u_r product_(h<r)f_h and
V=v_r product_(h>r)f_h. These are smooth charts, with
their direct inverse localizations. The four s-factor
charts give the four source-chain surfaces used in
I3R. The two final charts, through the actual h source
overlap, give the selected P1 times D_s; this is the
same negative-square native Cox transition
(Z,a_N,c_N) to (Z^-1,Za_N,Zc_N).

In its y-factor chart the complete ordinary normal map
is

\[
             c_N=s^4 u_r,\qquad
             a_N=\kappa^{-1}s^{-4}v_r,
             q_{\rm old}=Z a_Nc_N.
 \tag{MC3.15}
\]

The x-factor chart is its stated source-period image,
including alpha,Gamma and their inverses. Thus both
reference normal lines have degree -1 on the generic
sphere. Their additional s powers are the displayed
opposite principal divisor maps. The reference spinor
determinant is zero in H2 of this product surface.
It has no interior point blowups. Its original scalar
closing and Hopf cap are the same construction
MC3.5--11 with the fixed-source functions, retaining
all s powers. The Mayer--Vietoris maps give
c1(E_ref,c)=0 and p1(F_ref,c)=0. Its second Chern
number remains the one of its actual full clutch.

## MC3.6. The scoped completed normal expression

On the positive spinor projectivization put
c_i=c_i(E_c), x=c1(O(1)). Its exact projective relation
is x^2+c1 x+c2=0, with fibre integral x=1. Conjugating
the negative physical normal line reverses the real
normal orientation; the actual inner normal quotient
therefore has the opposite orientation to this complex
projective bundle. Its U numbers are

\[
 k_U=-\int(c_1^2-c_2),\qquad
 \ell_U=-\int\{p_1(TF_c)+c_1^2-4c_2\}.
 \tag{MC3.16}
\]

These are the K68 actual normal/Hopf orientation maps,
applied to the same full bundle clutch above. The
physical line M is the Hermitian dual, so its odd
pair is their negative. With the actual but unassigned
integer c2(E_c), MC3.13--14 give

\[
 (k_M,\ell_M)_{\rm moving}
      =(-75-c_2(E_c),-177-4c_2(E_c)).
 \tag{MC3.17}
\]

The reference has the same formula with its own c2
and with the two numbers MC3.13--14 replaced by zero.
Writing kappa for the resulting actual difference of
the first physical numbers, the moving/reference
contribution is exactly

\[
 (k_M,\ell_M)_{\rm moving-ref}=(\kappa,4\kappa+123),
 \qquad (4k_M-\ell_M)/24=-41/8.
 \tag{MC3.18}
\]

The coefficient of each actual second Chern number
has cancelled in this last expression. No choice or
division of an uncomputed integer is used. This is
the selected moving-face/reference term only; the
compact components, four lower doubles and outer
Jin parameter/physical-clutch arrow are still separate.
