# Exact orbit traces in the ordinary three-curve plumbing

Working calculation following P3K.48 and OR.1--4. We compute the
three actual normal-sphere orbit traces on prescribed source paths.
Proved as P3K.51 after complete root and independent blind_control
audits. Section CT.3 gives the exact boundary-to-common-exterior
variation map. No nonfixed stable derivative or further return is
assigned by this statement.

## CT.1. Three literal trace maps

On each curve use \(z=\tan\chi>0\), \(0\leq\chi\leq\pi/2\),
and set \(U=\cos\chi+j\sin\chi\). Use the actual normal sphere
coordinate \(q_i=UQ\) and the section \(q_i=1\). The based ordinary
normal product is \(T_-=HQH^{-1}\) for \(C_0,C_2\), and
\(T_+=HQH\) for \(C_1\), with \(H\) from OP.6. We first display
the angular maps; the full diagonal units are carried by OP.19 and
its based homotopy. The physical circle angle is \(\phi\), and
\(E=e^{i\phi/2}\).

On \(C_0\) the source point is fixed. On \(C_1,C_2\) it moves
by \(z\mapsto e^{i\phi}z,e^{-i\phi}z\), respectively. The exact
Hopf representatives satisfy
\[
 U(e^{i\phi}z)=E^{-1}UE,\qquad
 U(e^{-i\phi}z)=EUE^{-1}.                         \tag{CT.1}
\]
Substitute \(Q=U^{-1}\), undo \(T_i\), apply the original
physical normal action OP.18, and then redo \(T_i\) and the
source Hopf representative at the moved point. This gives
\[
 \begin{aligned}
 F_0&=H E^{-2}H^{-1},\\
 F_1&=E^{-1}UEH E^{-1}H^{-1}U^{-1}H^{-1}E^{-1}H,\\
 F_2&=EUE^{-1}H E H^{-1}U^{-1}H E^{-1}H^{-1}.
 \end{aligned}                                           \tag{CT.2}
\]
These are actual maps of the parameter/physical-orbit cylinders into
the corresponding normal \(S^3\). Each closes at \(\phi=2\pi\)
and \(\theta=2\pi\). At each radial endpoint it is independent
of \(\theta\). Thus, subtracting its initial-parameter trace gives
a closed relative degree-three cycle with a well-defined integer
normal-sphere degree. We use domain orientation
\(d\chi\wedge d\theta\wedge d\phi\).

## CT.2. The three degrees

Write
\[
 h=UiU^{-1},\qquad a=UHiH^{-1}U^{-1},\qquad
 v=HiH^{-1},\qquad w=H^{-1}iH.
\]
Each is constant in \(\theta\) at both radial ends. As maps from
the cylinder with its ends collapsed, their outward-sphere degrees
are
\[
             \deg h=0,\qquad \deg a=3,
             \deg v=3,\qquad \deg w=-3.             \tag{CT.3}
\]
The first is independent of \(\theta\), and the third is OP.17.
For the second, the exact homotopy
\(U_t=\cos(t\chi)+j\sin(t\chi)\) gives
\(U_tvU_t^{-1}\); it keeps each end independent of \(\theta\),
so it is a homotopy on the collapsed cylinder. For the fourth, the
same three inverse images of \(-i\) as OP.15 have \(H=j\).
Direct differentiation gives
\[
             \partial_s w=-4\vartheta'(s)k,
             \partial_\theta w=3j.
\]
They are all negative regular inverse images in the same orientation
as OP.16. This proves the last integer without assigning a sign by
analogy.

For an axis map \(n\) of degree \(d\), the map
\(\exp(\phi n/2)\) on this cylinder times \([0,2\pi]\) has
normalized third integral \(d\), while its inverse has integral
\(-d\). Indeed the positive quaternion volume is
\(\sin^2 t\,dt\wedge\Omega_{S^2}\); substituting
\(t=\phi/2\) gives
\(4\pi d\int_0^\pi\sin^2t\,dt/(2\pi^2)=d\).
A full-angle inverse \(\exp(-\phi n)\) gives \(-2d\).

The latter formula with axis \(v=HiH^{-1}\) immediately gives the degree of \(F_0\).
For the others, (CT.2) factors literally as
\[
 \begin{aligned}
 F_1&=E^{-1}\exp(\phi h/2)
                  \exp(-\phi a/2)\exp(-\phi w/2),\\
 F_2&=E\exp(-\phi h/2)
                  \exp(\phi a/2)\exp(-\phi v/2).
 \end{aligned}                                           \tag{CT.4}
\]
The Maurer--Cartan product formula OP.21 makes the integrals additive
here. At the radial ends every factor is independent of \(\theta\),
so the boundary two-forms vanish; at \(\phi=0,2\pi\) every factor
is a constant central sign, so they also vanish. The two parameter
faces cancel because the factors are periodic. Consequently
\[
               \deg F_0=-6,\qquad
               \deg F_1=0-3+3=0,\qquad
               \deg F_2=0+3-3=0.                    \tag{CT.5}
\]
The zero-winding unit factors have their carried based homotopy;
through it the full-unit physical action is exactly OP.19. This
computes the degrees of these specified local orbit trace maps.
At this stage of the proof, (CT.5) computes local traces only.
Section CT.3 supplies the actual relative two-chains, their graph-loop
boundaries, and the signed boundary-to-variation map used below.

## CT.3. Closing the graph loops and the full variation map

The following exact chain calculation has passed both independent
audits. We retain its integral signs and the actual vertex paths.

Choose the actual invariant coordinate balls and Hermitian normal
tubes first, with equivariant rounding. Restrict the ordinary product
to their boundaries and use positive radial normalization on each
normal sphere; the transported metric is retained as in OP.19. Thus
the physical action preserves every actual boundary before applying
the ordinary coordinates. Choose the two graph generators of P3K.29 as
\(\gamma_j=a_j-a_0\), each \(a_i\) running from the first vertex
to the second. Lift their curve-interior paths to the plumbing
boundary by a constant generic normal-sphere section \(q_i=q_*\).
Generic means that at both ends both actual normal coordinates are
nonzero, avoiding the other two curve axes. Such constants form an
open dense set. Join the endpoints by fixed paths in the reference
vertex link, the five-sphere with the three axis-circle tubes
removed. The connecting paths can be explicit. Arrange the two
endpoints in the open set with all three coordinates nonzero, and
write their coordinates as \(r_ke^{it_k}\), \(r'_ke^{it'_k}\), with
\(\sum r_k^2=\sum(r'_k)^2=1\). Choose one real argument for each
endpoint coordinate and use
\[
 z_k(s)=\sqrt{(1-s)r_k^2+s(r'_k)^2}\,
                 e^{i((1-s)t_k+st'_k)}.
\]
All coordinates remain nonzero. The three axis-tube inequalities
are linear inequalities in the squared moduli, so these paths stay
outside the same sufficiently small axis tubes. The physical
circle changes only phases, hence its traces avoid them as well.
The connecting paths are fixed in the reference vertex and do not
depend on the parameter.

The ordinary vertex maps OP.1 commute with the physical circle, so
the transported action on these vertex connectors is independent
of the parameter. The edge-end traces have the same property. The
local calculation (CT.5) remains unchanged for a constant generic
\(q_*\): varying the constant normal point gives a homotopy of
normal-sphere trace maps with parameter-independent radial ends.
The integers are therefore the ones computed at \(q_*=1\).

Here is the exact meridian projection, including the endpoints.
Each edge block is an annulus times its actual normal three-sphere.
The trace at either end is independent of the parameter circle.
Fill its two-torus by \(D^2_\theta\times S^1_\phi\), with the map
constant in \(D^2_\theta\). This closes the local three-chain
inside the edge block by chains of rank at most one. Its third
homology is the normal \(\mathbb Z\), measured by (CT.5), and its
inclusion in the common exterior takes that generator to the
positive complex normal meridian \(m_i\). The same endpoint
fillings on the vertex connectors leave cycles factoring through
a two-dimensional space, since the entire vertex trace is
parameter-independent. Their third homology classes vanish.
Thus the closed graph-loop trace, in the orientation
parameter--circle--path, is exactly
\[
 [K\gamma_j]=[F_j]-[F_0]=6m_0,\qquad j=1,2.       \tag{CT.6}
\]
The cyclic permutation from path--parameter--circle in CT.2 to this
orientation has positive sign. No meridian contribution from a
vertex link has been omitted: the displayed fillings and the
parameter-independent factorization remove it explicitly.

Choose relative two-chains \(x_j\) with \(\partial x_j=\gamma_j\).
They exist because \(H_1(E_C)=0\). For the positive physical circle
trace \(\Delta c=a_*([S^1_\phi]\times c)\), the boundary identity
is \(\partial\Delta=-\Delta\partial\). The map from the plumbing
boundary to its regular-neighbourhood retract identifies its second
homology with \(H_2(C)\), with the positive complex sphere basis.
Indeed the relative groups in degrees two and three of the
neighbourhood and its boundary vanish by duality and
\(H^4(C)=H^3(C)=0\). On \(C_1\), the source rotation is
\(z\mapsto e^{i\phi}z\); circle--path orientation is opposite to
its complex orientation. On \(C_2\) the rotation has the opposite
sign and gives its positive complex sphere. The trace of the
\(C_0\) path projects to a one-dimensional path. Hence
\[
             \Delta x_1=D_1,\qquad
             \Delta x_2=-D_2.                         \tag{CT.7}
\]
These equalities are integral: P3K.29 identifies the relative
three-group by the boundary sphere basis, with no torsion.

Let \(P_t\) be ordinary-product parallel transport on the common
exterior, and set \(a_t=P_t^{-1}\delta_tP_t\). If \(F=P_1\) is
the actual return, then \(a_1=F^{-1}a_0F\). Define the prism
\(Kc=a_*([I_t]\times[S^1_\phi]\times c)\). The literal boundary
formula is
\[
 \partial Kc=(\Delta_1-\Delta_0)c+K\partial c,
          \qquad F\Delta_1=\Delta_0F.                 \tag{CT.8}
\]
Consequently
\[
 (F-1)\Delta_0x
 =-F\partial Kx+F K\partial x+\Delta_0(Fx-x).
\]
Here \(F\) is the identity on the common boundary. It acts trivially
on absolute third homology because the boundary meridians generate
that group integrally. Moreover,
\(H_2(E_C)=0\) makes the last term a boundary. Thus
\[
             \operatorname{Var}_3(\Delta_0x)
                           =[K\partial x].            \tag{CT.9}
\]
Combining (CT.6)--(CT.9) gives
\(\operatorname{Var}(D_1)=6m_0\) and
\(\operatorname{Var}(D_2)=-6m_0\). The integral symmetry proof
of P3K.29 applies to this ordinary relative return without any
circle-equivariance hypothesis. OR.3 gives \(V_{00}=0\).
The resulting exact matrix is therefore
\[
 V=\begin{pmatrix}0&6&-6\\6&0&0\\-6&0&0\end{pmatrix}. \tag{CT.10}
\]
No stable derivative on the two nonfixed cycles, and no further fan
return, is determined by this chain calculation alone.
