# The actual source-cusp stable derivative from the circle trace

Proved as P3K.52 after complete root and independent blind_control
audits. We retain
P3K.48's actual ordinary plumbing product, K50's fixed-curve framing,
and K51's integral meridian/dual-cycle convention. The calculation
below assigns the full ambient stable-derivative vector; it does not
borrow the scalar-family initial data of P3K.29/P3K.31.

## ST.1. The exact derivative prism and its sign

Let \(E\) be the actual common exterior, \(P_t:E\to E_t\) the
ordinary-product parallel transport, and \(F=P_1\) its positive
return. On the reference exterior put
\(a_t=P_t^{-1}\delta_tP_t\), with \(t\in[0,1]\). The actions
preserve the common boundary, and there are exact identities
\[
 a_1(\phi)=F^{-1}a_0(\phi)F,\qquad
 \Delta_1=F^{-1}\Delta_0F.                            \tag{ST.1}
\]
Fix an oriented global ambient stable frame of the reference
six-sphere and restrict it to \(E\). Write \(c_F\) for the stable
derivative of \(F\), and \(d_t(\phi,p)\) for the derivative of
\(a_t(\phi)\), both in this frame. Their matrices lie in the stable group
\(GL^+\), not necessarily in its orthogonal subgroup. We lift them
to the universal covering group \(\widetilde{GL^+}\), retaining
its actual group multiplication. The following endpoints are
prescribed. The lift \(c_F\) is one on the
boundary, because \(F\) is the identity on a boundary collar and
\(E\) is simply connected. Lift \(d_t\) starting at one for
\(\phi=0\). Its endpoint at \(\phi=2\pi\) is one: the actual
circle action extends to the vertices, whose three complex weights
are \((-1,0,1)\) or \((1,-1,0)\). Their sum is zero, so the
stable rotation loop has a closed lift there. Continuity on the
connected exterior fixes the same endpoint everywhere and for all
\(t\). No unclosed half-angle lift is used.

The chain rule, with every source and target retained, now gives
the literal identity in the covering group
\[
 d_1(\phi,p)=c_F(a_1(\phi)p)^{-1}
                    d_0(\phi,Fp)c_F(p).              \tag{ST.2}
\]
Both sides have lift value one at \(\phi=0\), so no central sign is
missing. The explicit polar deformation
\[
 A\longmapsto A(A^T A)^{-s/2},\qquad 0\leq s\leq1,
\]
lifts from the identity to a deformation retraction of this covering
group onto Spin. We use this deformation to identify its third
class; we do not apply it to a product identity. Normalize the
integral third class \(\omega\) by degree one on left quaternion
multiplication. In the
stable real vector representation we can use
\[
 \omega(g)=-\frac{\operatorname{tr}_{\mathbb R}
                         (g^{-1}dg)^3}{48\pi^2},
\]
whose restriction to the left quaternion subgroup has integral one.
The Maurer form is closed on the full linear group, and the displayed
deformation proves that it represents the same integral class on
its cover. The local orthogonal blocks below lie in the Spin
subgroup of this cover.
Its Maurer--Cartan product identity has exact boundary form
\(\operatorname{tr}_{\mathbb R}(g^{-1}dg\wedge dhh^{-1})/(16\pi^2)\).
Put \(\Omega=c_F^*\omega\), a relative closed three-form, and
\(\delta(D)=\langle\Omega,D\rangle\).

For a relative two-chain \(x\) with boundary \(\gamma\), integrate
(ST.2) on \(S^1_\phi\times x\). Every product boundary form vanishes:
\(c_F\) is one and its derivative is zero on the collar containing
\(S^1\times\gamma\). The term pulled back from \(c_F(p)\) factors
through a two-chain. The remaining difference involving \(d_0\)
is its integral on \(S^1\times(Fx-x)\). Since \(F\) fixes the
boundary, \(Fx-x\) is an absolute two-cycle; it bounds a three-chain
because \(H_2(E)=0\). The integral of that closed form is therefore
zero. We obtain
\[
 \int_{S^1\times x}(d_1^*\omega-d_0^*\omega)
                   =-\langle\Omega,\Delta_1x\rangle. \tag{ST.3}
\]
The actual action prism \(K\) of CT.8 has
\(\Delta_1x-\Delta_0x=\partial Kx-K\gamma\).
The first term pairs to zero with the closed form \(\Omega\), and
the second lies in the boundary where \(\Omega=0\). Thus the
right side of (ST.3) is \(-\delta(\Delta_0x)\).

Apply Stokes to the derivative map on
\([0,1]_t\times S^1_\phi\times x\), with this displayed product
orientation. Its boundary is top minus bottom plus
\([0,1]\times S^1\times\gamma\). Consequently
\[
 \int_{S^1\times x}(d_1^*\omega-d_0^*\omega)
   =-W(\gamma),\qquad
 W(\gamma)=\int_{[0,1]\times S^1\times\gamma}d_t^*\omega.
                                                               \tag{ST.4}
\]
Combining the two exact signs proves
\[
                       \delta(\Delta_0x)=W(\gamma).    \tag{ST.5}
\]

## ST.2. Actual local frames and the closed Spin blocks

We compute (ST.4) using the same generic normal sections and
vertex-link paths as CT.3. This is an actual frame comparison.
For a fixed change of stable frame \(g\), the derivative action
changes by
\[
 d_t'(\phi,p)=g(a_t(\phi)p)^{-1}d_t(\phi,p)g(p).
                                                               \tag{ST.6}
\]
On the closed graph trace, the last term factors through its path,
and the exact Maurer boundary terms cancel. Hence its third
integral changes by minus the pairing of \(g^*\omega\) with the
actual orbit trace \(K\gamma\).

On each edge choose the reference complex coordinate frame on the
annulus times its normal four-disc, retaining its stable orientation.
Its comparison with the global ambient frame extends through that
four-disc. This domain has zero third cohomology. Close the edge
trace with the rank-one \(D^2_t\times S^1_\phi\) endpoint caps of
CT.3; the preceding pairing with \(g^*\omega\) is then zero.
Thus this frame change contributes zero to its integer. The vertex
coordinate frames extend over their actual balls. The vertex traces
and the same caps are independent of \(t\), hence their third
integrals vanish as well. If a determinant adjustment is used to
choose a Spin-compatible complex frame, its scalar factor has no
third class and is retained in (ST.6). This verifies the passage to
local frames on closed cycles, rather than identifying two frames
by their names.

The full physical action in these coordinates is OP.19. Its
zero-winding unit factors have the actual based logarithm homotopy
already displayed there. The higher normal terms are removed by
the literal normal rescaling of OP.3. To compute the derivative
trace, move its normal evaluation point to the zero section through
that four-disc, where the coordinate frame and action both extend.
At the zero section the derivative is block triangular, with base
rotation and normal block. Its off-diagonal block vanishes there;
the rescaling is a homotopy through invertible derivatives. All end
faces remain parameter-independent. Thus these operations preserve
the closed third integrals and retain the actual full-unit action.

In the actual quaternion coordinate
\(Q=n_0+j\overline{n_1}\), the three normal blocks are exactly
\[
 \begin{array}{c|c|c|c}
 &\text{base rotation}& A& B\quad (Q\mapsto AQB)\\ \hline
 C_0&1&1&H e^{-i\phi}H^{-1}\\
 C_1&e^{i\phi}&H e^{-i\phi/2}H^{-1}&H^{-1}e^{-i\phi/2}H\\
 C_2&e^{-i\phi}&H e^{i\phi/2}H^{-1}&H e^{-i\phi/2}H^{-1}.
 \end{array}                                             \tag{ST.7}
\]
For the stable class, a left factor has degree \(+1\) and a right
factor has degree \(-1\). This is the same normalization as
P3K.31: \(\operatorname{Ad}_q=L_qR_{q^{-1}}\) has stable degree
two. Equivalently the real quaternion trace restricts to the
positive normalized form on the left factor and its negative on
the right factor. The degree of (ST.7)'s normal block is therefore
\(\deg A-\deg B\).

At the two nonfixed curves, the normal half-angle pair ends at
\((-1,-1)\), representing the central minus sign in the normal
Spin lift. The source \(SO(2)\) rotation has Spin endpoint minus
one. Their images in Spin of the full six-dimensional tangent
space multiply to plus one. The full lift therefore closes exactly.
The source factor depends only on \(\phi\), so its own third
form is zero. Product-form boundary terms vanish on the same
parameter-independent end faces and constant central-sign angle
faces used in CT.2. Thus the half-angle block calculation evaluates
the closed full stable lift, not an artificially closed normal loop.

## ST.3. The full derivative vector and the three relative pairs

CT.3's axis calculations, with the orientation
path--parameter--circle, give
\[
 \begin{array}{c|rr|r}
 &\deg A&\deg B&W_i=\deg A-\deg B\\ \hline
 C_0&0&-6&6\\
 C_1&-3&3&-6\\
 C_2&3&-3&6.
 \end{array}                                             \tag{ST.8}
\]
The vertex connectors contribute zero by ST.2. The graph loops are
\(\gamma_j=a_j-a_0\); hence
\[
                  W(\gamma_1)=-12,\qquad W(\gamma_2)=0.
\]
CT.7 supplies the exact integral signs
\(\Delta x_1=D_1\), \(\Delta x_2=-D_2\). Equation (ST.5)
therefore gives \(\delta_1=-12\) and \(\delta_2=0\).
K50 computed the remaining entry in the same ambient frame and
relative-dual orientation. Thus
\[
                       \delta=(-12,-12,0)^T.           \tag{ST.9}
\]

For clarity the frame relation to each single-curve exterior is also
retained. K31's actual product-frame comparison has third class
\(e_i\). Its derivative correction is \(-V_{ii}\); all three
diagonal entries in K51 are zero. K31.7 consequently gives
\[
 2n_i=\delta_i-V_{ii},\qquad m_i=-V_{ii}-n_i.
\]
The actual ordinary relative pairs are therefore
\[
 (m_0,n_0)=(6,-6),\qquad
 (m_1,n_1)=(6,-6),\qquad
 (m_2,n_2)=(0,0).                                     \tag{ST.10}
\]
Each exterior's central coordinate is the same oriented closed
return, namely one from F56. The native nonfixed products differ by
the explicit pure-left correction in OR.4: subtracting that \(L^6\)
gives native pairs \((0,-6)\) at \(C_1\) and \((-6,0)\) at
\(C_2\), with the central coordinate unchanged. No additional fan
return is assigned by this calculation; the actual flop maps and
subsequent basis/frame transports must still be applied.
