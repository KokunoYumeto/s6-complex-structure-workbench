# The fixed-curve relative return in the actual ordinary plumbing product

Proved as P3K.50 after complete root, fourfold and blind_control
audits. We compute only the restriction of the
ordinary-product return to the exterior of the original fixed curve
C0. The two other relative entries and the full three-curve variation
matrix remain uncomputed. No additional fan return is assigned.

## OR.1. The exact direction of the two boundary products

Let \(E_\theta\) be the exterior of the actual fixed curve, with the
parameter running positively from \(0\) to \(2\pi\). Write
\(b^H_\theta:\partial E_\theta\to\partial E_0\) for the actual
Hopf/Cox product of P3K.40/P3K.42 and
\(b^O_\theta:\partial E_\theta\to\partial E_0\) for the restriction
of P3K.48's ordinary plumbing product. These are actual-to-reference
coordinate arrows, both based at the identity.

We verify their local coordinates before taking a homotopy. In the
first fixed-edge chart of OE.4,
\[
 Z=b,\qquad(c_0,c_1)=(a,c),\qquad q=bac,\qquad
 q_H=U(b)(a+j\overline c),\quad
 U(b)=\frac{1+jb}{\sqrt{1+|b|^2}}.                 \tag{OR.1}
\]
Here \(q\) is the original source-height coordinate. The retained
period multiplier \(\kappa=q_T/q\) is not substituted for this
height. The second standard Hopf chart has coordinates
\[
 (Z',c'_0,c'_1)=(\kappa w,\alpha v,(\kappa\alpha)^{-1}u).
                                                               \tag{OR.2}
\]
Substitution of OE.4 gives exactly
\(Z'=b^{-1}\), \(c'_0=ba\), \(c'_1=bc\).
The ordinary product instead uses the second vertex coordinates
\((u,\eta v,\kappa w)\), with the same transformation at the
initial reference parameter. Its first-chart normal arrow is the
literal \(\mathcal K_0=\mathcal D_0 T_-\) of OP.9. Thus, after the
specified based homotopy of the actual zero-winding unit factors,
\[
 \Gamma_\theta=b^O_\theta(b^H_\theta)^{-1},\qquad
 \Gamma_\theta(h,q_H)=
       (h,L(h,\theta)q_H R(h,\theta)),
 \quad L=UHU^{-1},\quad R=H^{-1}.                     \tag{OR.3}
\]
This is the direction of OP.20, rather than its inverse. The full
\(\mathcal D_0\) is retained before that based homotopy. Its
positive normal metric and its based periodic logarithms extend the
homotopy on the protected collars, so it changes neither endpoint
relative class. The higher normal terms are carried by the same
normal-rescaling collar isotopy as OP.3. No additional source
inversion, Tate-height substitution or line gauge is made.

P3K.48 OP.5 computed the degrees of the two closed maps in (OR.3):
\[
 (\deg L,\deg R)=(-6,0)
 \quad\text{on }S^2_h\times S^1_\theta.                \tag{OR.4}
\]
The complex-curve orientation has the opposite sign; (OR.4) uses
exactly the \(h\)-sphere boundary orientation of P3K.23.

## OR.2. Extension of the inverse gauge and its endpoint degree

Use the actual oriented exterior product
\(E_0=D^3_y\times S^3_{q_H}\) of P3K.23. Each of the based
homotopies \(L^{-1},R^{-1}:S^2\times[0,2\pi]\to SU(2)\)
extends to \(D^3\times[0,2\pi]\), with value one at the initial
end. To see this as an exact extension problem, the restriction
\[
 D^3\times\{0\}\cup S^2\times[0,2\pi]
                    \longrightarrow D^3\times[0,2\pi]
\]
is a cofibration with an explicit retraction. Rescale time to
\(t\in[0,1]\), set
\[
 \lambda=\min\{2/(2-t),1/|y|\},\qquad
 r(y,t)=(\lambda y,\,2+\lambda(t-2)),
\]
with \(1/0=\infty\). The image is on the bottom or side, and the
map fixes that subspace. Straight interpolation between the identity
and this map is a deformation through the cylinder. Composing the
prescribed bottom-and-side map with \(r\) gives a continuous
extension. Relative smoothing in \(\mathbb R^4\), followed by
radial normalization to its unit sphere, gives smooth extensions
while retaining the protected side and bottom collars, denoted
\(A(y,\theta)\), \(B(y,\theta)\), without changing their prescribed
boundary maps. Set
\[
 \psi_\theta(y,q_H)=
       (y,A(y,\theta)q_HB(y,\theta)).                \tag{OR.5}
\]
This is a smooth orientation-preserving diffeomorphism for every
parameter, with inverse obtained by replacing the two multipliers
by their inverses. On the boundary it is precisely
\(\Gamma_\theta^{-1}\). Its endpoint is relative to the boundary.

We fix the connecting sign by integration. Orient
\(D^3\times[0,2\pi]\) by \(\Omega_{D^3}\wedge d\theta\).
Its side has orientation \(\Omega_{S^2}\wedge d\theta\), while
its top has orientation \(-\Omega_{D^3}\). For the normalized
closed degree-three form \(\omega\) of OP.21, Stokes gives
\[
 0=\int_{S^2\times[0,2\pi]}A^*\omega
                    -\int_{D^3}A(\cdot,2\pi)^*\omega.
\]
The bottom integral is zero. Inverting an \(SU(2)\) map reverses
its third class, so (OR.4) yields
\[
 \deg A(\cdot,2\pi)=6,\qquad
 \deg B(\cdot,2\pi)=0.                               \tag{OR.6}
\]
These are degrees of maps \((D^3,S^2)\to(S^3,1)\), with exactly
P3K.23's orientation.

The endpoint map (OR.5) is a product of the actual left and right
multiplications of K23.5. Homotopies of the two coefficient maps
relative to their boundary identify its relative class as
\[
                         [\psi_{2\pi}]=L^6.           \tag{OR.7}
\]
There is no disc-supported central factor: the same formula extends
over \(D^3\times D^4\), and its coefficient maps are classified by
the two degrees in (OR.6). Changing either extension changes neither
of these degrees nor the endpoint relative class represented by
these fibrewise multiplications.

## OR.3. The actual physical return and its three coordinates

Let \(P^H_\theta:E_0\to E_\theta\) be parallel transport chosen
so that \(b^H_\theta P^H_\theta\) is the identity on the boundary.
Equation (OR.3) gives the ordinary-product transport
\[
                       P^O_\theta=P^H_\theta\psi_\theta,
 \qquad b^O_\theta P^O_\theta=\operatorname{Id}
                       \text{ on }\partial E_0.      \tag{OR.8}
\]
Its endpoint is therefore
\[
                         \Phi_O=\Phi_H\psi_{2\pi}.   \tag{OR.9}
\]
These are the actual forward returns of the positive parameter loop;
we do not identify their physical mapping tori with Jin's oppositely
parameterized completion. That sign was already retained when
P3K.42 computed \([\Phi_H]=L^0R^{-6}\mathcal C\).
Connections compatible with the same fixed boundary product form
an affine space; an interpolation with fixed boundary gives a
relative isotopy of their endpoints. Thus (OR.9) also computes the
return from the connection fixed on all three components of the
ordinary plumbing in OP.3.

The generators \(L,R\) commute literally, and \(\mathcal C\) is
central. Substituting (OR.7) consequently proves
\[
       [\Phi_O]=L^6R^{-6}\mathcal C,
       \qquad (m,n,s)=(6,-6,1).                      \tag{OR.10}
\]
The fixed-curve variation is \(m+n=0\). In the Cartesian/left-
quaternion stable frame of P3K.23 its relative stable derivative is
\(-2n=12\) on the product-oriented relative cycle \([D^3_h]\).
In the ambient-relative-dual convention used for the common exterior,
\(D_0=-[D^3_h]\), so the same derivative evaluates \(-12\) on
\(D_0\). The identification with the ambient stable frame also retains the
actual frame-change map of P3K.31: its third class is
\([g_0]=e_0\), and its derivative correction on this cycle is
\(-V_{00}=0\), because the fixed-curve variation was just
computed to vanish. Hence the ambient value is exactly
\(\delta_0=-12\). These statements concern this one exterior restriction
in the explicitly constructed ordinary product. The two nonfixed
edge restrictions, their mutual variations, and any further fan
return require additional actual maps and are not assigned here.

## OR.4. The two exact nonfixed single-star frame comparisons

The same calculation identifies, without evaluating their native
returns, the two remaining changes of boundary product. For \(C_1\),
the native equivariant star of OE.7--8 has first coordinates
\((z,n_0,n_1)=(c,a,b)\) and second coordinates
\[
 (z',n'_0,n'_1)=(\eta v,g w,(g\eta)^{-1}u).
\]
The transition is exactly \(z'=z^{-1}\), \(n'=zn\).
For \(C_2\), the native star has first coordinates
\((z,n_0,n_1)=(a,b,c)\) and second \((u,v,w)\), with the
same standard transition. Thus both native products use
\(q_i=U(z)(n_0+j\overline{n_1})\), in the identical source/normal
orientation convention. The complete parameter units in the first
star have their original extending logarithms, while the second
star is already parameter-free in these charts.

The ordinary product of OP.1--3 consequently gives the actual
native-to-ordinary boundary arrows, after their carried based unit
homotopies,
\[
 \begin{array}{ll}
 C_1:&q_1\longmapsto (UHU^{-1})q_1 H,\\
 C_2:&q_2\longmapsto (UHU^{-1})q_2 H^{-1}.
 \end{array}                                             \tag{OR.11}
\]
The left factor is the identical closed map of OP.20 on the
corresponding source sphere. Each right factor depends on only the
radial coordinate and parameter. Therefore each arrow has factor
degrees \((-6,0)\) in its own \(h\)-sphere orientation. The full
extension and direction proof of OR.2--3 applies to these displayed
arrows: the ordinary relative return is the native single-star
relative return composed with the explicit pure-left endpoint of
degree six. In particular this boundary change leaves the native
right relative integer unchanged. This computes the comparison
map, not the native nonfixed return. Those two actual returns and
their mutual common-exterior entries are still required.
