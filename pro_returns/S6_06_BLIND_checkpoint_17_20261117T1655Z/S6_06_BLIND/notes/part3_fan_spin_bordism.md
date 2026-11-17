# Arbitrary-fan flop: the exact spin cap and the remaining relative pairing

This working note isolates proved local maps from the still uncomputed
global relative Pontryagin pairing. It does not assign a return class
to the arbitrary fan. The two OS49 fans are already settled by P3K.17.

## 1. The actual compact structure group and its loop

Use Cox coordinates \((a_0,a_1,c_0,c_1)\), auxiliary weights
\((1,1,-1,-1)\), and the moment coordinate
\(\mu=|a|^2-|c|^2\). The compact group preserving this data is
\[
 G=(U(2)_a\times U(2)_c)/S^1_{\rm aux}.
\]
The determinant degrees identify
\[
 \pi_1G=\mathbb Z^2/\langle(2,-2)\rangle.
\]
The actual bounded Cox parameter loop has weights
\((-A-B,0,A,B)\), for integral \(A,B\). Its determinant-degree
pair is \((-A-B,A+B)\), hence its class is in the order-two
subgroup and is nonzero there exactly when \(A+B\) is odd.
It is not legitimate to contract every such loop in \(G\).

## 2. An exact twistor extension, including the odd loop

Conjugate the two auxiliary-negative coordinates. The inner boundary
of the real master space becomes ordinary \(\mathbb {CP}^3\),
and the parameter loop has projective weights
\((-A-B,0,-A,-B)\). Multiplication by the common scalar
\(\exp(\pi i(A+B)t)\) gives the determinant-one lift
\[
 \operatorname{diag}\bigl(
 e^{-\pi i(A+B)t},e^{\pi i(A+B)t},
 e^{\pi i(B-A)t},e^{\pi i(A-B)t}\bigr).                 \tag{FSpin.1}
\]
The two consecutive pairs are reciprocal. Thus (FSpin.1) lies in
\(Sp(1)\times Sp(1)\subset Sp(2)\) for the quaternionic
structure pairing the first two and last two coordinates. At
\(t=1\) it is the common central scalar
\((-1)^{A+B}\), so its projectivization is a genuine loop
in \(PSp(2)=SO(5)\). This is an equality of the actual
projective transformations, not only a homotopy of loops.

Let
\[
 Z=D(\Lambda^+TS^4),\qquad
 \partial Z=S(\Lambda^+TS^4)=\mathbb {CP}^3.             \tag{FSpin.2}
\]
The boundary equality is the twistor map sending a unit self-dual
two-form to its orthogonal complex structure on the oriented
tangent four-plane. Equivalently, the quaternionic Hopf projection
\(\mathbb {CP}^3\to\mathbb {HP}^1\) is the displayed sphere
bundle. The \(SO(5)\) action on \(S^4\) acts by its derivative
on \(\Lambda^+TS^4\), and (FSpin.1) is exactly its action on
the boundary. It therefore extends over the disk bundle at every
parameter value, with the same endpoints.

This action preserves an actual spin lift. At a point of the zero
section the isotropy representation is
\[
 SO(4)\longrightarrow SO(7),\qquad
 T Z|_{S^4}=\mathbb R^4\oplus\Lambda^+\mathbb R^4.
\]
Lift a generator of \(\pi_1SO(4)\) to a path in
\(Spin(4)=Sp(1)\times Sp(1)\). Its endpoint is
\((-1,-1)\). The standard four-plane contributes the central
minus one in \(Spin(4)\), while the self-dual three-plane,
through the first \(Sp(1)\), contributes the central minus
one in \(Spin(3)\). Their product in \(Spin(7)\) is plus
one. Hence the isotropy representation itself lifts to a
homomorphism \(SO(4)\to Spin(7)\). The homogeneous construction
\(SO(5)\times_{SO(4)}Spin(7)\), extended over the disk fibres
using an invariant connection, supplies the required
\(SO(5)\)-equivariant spin structure. In particular the odd
loop acts with a closed spin lift.

The orientation can be chosen so that the boundary is the standard
complex-oriented \(\mathbb {CP}^3\). With
\(u\in H^4(S^4;\mathbb Z)\), \(\int u=1\), one has
\[
 e(TS^4)=2u,\quad p_1(TS^4)=0,\quad
 p_1(\Lambda^+TS^4)=4u,\quad p_1(TZ)=4u.
\]
The sphere-bundle pullback is \(\pi^*u=h^2\), matching
\(p_1(T\mathbb {CP}^3)=4h^2\).

## 3. The interface framing transgression is zero

The common truncated conifold interface is
\(K=(S^3\times S^3)/S^1_{\rm aux}\cong S^2\times S^3\).
Choose a stable framing \(\tau\) and include the invariant
radial, moment, and auxiliary directions in its stable tangent
comparison. For a based loop \(g_t\) in the actual compact
group define
\[
 F(x,t)=\tau(g_t x)^{-1}Dg_t\tau(x).
\]
At both endpoints this is the identity. The actual Cox loop has
a closed stable spin lift: before the auxiliary quotient its
four complex weights sum to zero, so its real spin lift is
closed; the three added invariant real directions do not change
that lift. Thus \(F\) is a based map
\(\Sigma K_+\to Spin\). Concatenation of loops concatenates
these maps, and a homotopy of loops gives a homotopy of the
derivative comparisons. Consequently this construction is a
homomorphism on the relevant fundamental-group classes.

The suspension splitting is
\[
 \Sigma(S^2\times S^3)_+
 \simeq S^1\vee S^3\vee S^4\vee S^6.
\]
Stable spin homotopy in those dimensions is respectively
\(0,\mathbb Z,0,0\). Hence the target group is torsion-free.
The actual Cox class has order at most two, so its derivative
comparison is nullhomotopic. This proves that the local
\(S^2\times S^1_{\rm parameter}\) stable-framing transgression
is zero even for the odd loop. The assertion includes the
specific spin lift and the specified boundary marking.

## 4. The actual family bordism and the uncomputed global number

The real master space
\((\mathbb C^4\setminus0)/S^1_{\rm aux}\), truncated as in
P3K.17, has two small-resolution faces, their common outer face,
and the inner \(\mathbb {CP}^3\) face. Its stable tangent
bundle plus the auxiliary real direction is the associated sum
of the four complex weight lines. The sum of their weights is
zero, so it has a compatible spin structure. Glue (FSpin.2) to
the inner face using the exact twistor boundary map. Its unique
boundary spin structure agrees with that of the master space.
All maps carry the actual parameter loop by (FSpin.1), so this
constructs a spin bordism of the actual local families. Attach
the common exterior family times the bordism interval. This
gives a spin eight-dimensional bordism between the two actual
seven-dimensional mapping tori. Its projection to the parameter
circle has seven-dimensional cobordism fibres.

The signature is zero by the mapping-torus intersection
filtration: the classes containing the base-circle factor are
isotropic, and the complementary graded piece pairs with them.
The middle pairing is thus metabolic after quotient by its
radical. This statement retains boundary-relative cohomology;
the two boundary mapping tori have zero rational cohomology in
degrees three and four, so the absolute and relative middle
pairings identify in the required degrees.

The remaining calculation is the relative square of
\(p_1(TW)\). A double parameter cover contracts the local
\(G\)-loop, and Section 3 removes the local stable-framing
transgression. These facts do not by themselves identify the
whole exterior family with a product. Its fibre \(V\) is
homotopy equivalent to \(S^3\), but an exterior return fixed
on the boundary can still have a relative variation
\(H_3(V,\partial V)\to H_3(V)\). The additional boundary
group from \(S^2\times S^1\) must therefore be checked in
the relative gluing, rather than removed by the absolute
identity \(\pi_4SO=0\).

One concrete route is to use the actual torus-fibration tangent
transition matrices outside the critical cusp graph: their
graded factors are pulled back from the marked base and their
parameter dependence is off-diagonal. A common connection or
an explicit relative stable-framing extension through the
remaining toric critical curves would compute the missing
pairing. No vanishing of that global relative square is claimed
here until that extension is written.

## 5. The retained nodal curves: an exact relative stable map

The selected flop curve contains both triangle fixed points. After
removing its tube, each other toric critical curve is a truncated
\(\mathbb C^*\) edge cylinder. In its actual smooth chart
\(q=xy\), \(z\in\mathbb C^*\), use the Cartesian frame
\((\partial_x,\partial_y,z\partial_z)\). On the complement
of the critical curve its adapted vertical/base frame differs by
\[
 U(x,y)=\frac1{\sqrt{|x|^2+|y|^2}}
 \begin{pmatrix}x&\bar y\\-y&\bar x\end{pmatrix}\in SU(2).
\]
For the actual compact torus loop
\[
 R_\theta(x,y,z)=(e^{ia\theta}x,e^{-ia\theta}y,e^{ib\theta}z),
 \qquad D_\theta=\operatorname{diag}(e^{ia\theta},e^{-ia\theta}),
\]
the exact identity is \(U(R_\theta(x,y))=D_\theta U(x,y)\).
In moving chart coordinates the overlap matrix is
\(D_\theta U(x,y)\oplus1\). Applying the bundle-coordinate
gauge \(D_\theta^{-1}\oplus1\) over the entire Cartesian
chart makes this transition \(U(x,y)\oplus1\), independent
of the parameter and equal to the prescribed adapted-frame map
on the punctured overlap. The gauge extends through the node
and has equal identity endpoints and a closed spin lift.
This proves the relative map rather than extending the
nonextendible adapted frame itself.

For bounded base units, the exact maps
\((x,y,z)\mapsto(u(q)x,u(q)^{-1}y,v(q)z)\) have the exact
reciprocal-unit inverse. Their normalized nonvanishing ratios
have unique logarithms vanishing at the central fibre; scaling
those logarithms contracts the bounded terms through actual
coordinate maps. An annular overlap
\((x,y,z)\mapsto(z^k x,z^{-k}y,z)\) remains an actual
parameter-independent monomial map and changes \(a\) to
\(a+kb\); it preserves the displayed equivariance. These
identities are written and independently checked in
`notes/part3_nodal_frames.md` and
`code/part3_fourfold/nodal_frames.py`.

There is also a stable obstruction check with the same relative
scope. For a normal disk bundle \(D^4\) over an edge annulus
\(A\), extend the parameter homotopy relative to its initial
and final values, its punctured normal boundary, and its two
end collars. The relative cells have dimensions five through
seven. The obstruction groups are therefore
\(\pi_4Spin,\pi_5Spin,\pi_6Spin\), all zero. This verifies
the existence of the relative stable extension independently
of the explicit chart formula. It does not invoke a vanishing
of \(\pi_3Spin\), and introduces no new arbitrary boundary
framing at the nodal cylinder.

## 6. The finite logarithmic collars in the orbit comparison

Varying the real logarithm parameter changes the scalar suspension
by a phase, which disappears in its physical delta quotient.
One extra term must be retained in a finite logarithmic collar:
the transition \(t^c=\exp(c\log t)\) has modulus
\(\exp(c\log|t|)\). The actual real radial translation
\(-c\log|t|\) on the ordinary side removes it in the orbit
comparison. To match all parameter endpoints at once, use the
actual global ordinary closing multiplier \(h(t)\): its positive
real gauge \(|h(t)|^{-\theta}\) is single-valued. Near a finite
point, \(\log|h|=n\log|t-p|+\log|u(t)|\), with the bounded
unit extending into the fixed root chart. Thus its collar map
is exactly the displayed radial correction, and its endpoint
is the inverse of the actual ordinary closing modulus. Local
cutoffs may be introduced only with this endpoint matching
retained. The centre is kept in the fixed root-chart quotient.
The residual cusp comparison, after its specified integral
period is subtracted, is the
bounded torus loop of Sections 1--3, with its full integral
period reindexing retained.

Thus a claim that the finite-collar orbit gluing is literally
independent of the parameter before this radial gauge would
omit a real transition. The displayed gauge supplies the
required collar map. Its compatibility with the chosen
relative Pontryagin primitives on all pieces is still the
last global pairing check of Section 4.

## 7. An explicit Cox normal trivialization

The normal bundle on the \(a\)-resolution is
\(\mathcal O(-1)\otimes\mathbb C^2\). Choose a unit
representative \(a=(a_0,a_1)\in S^3\) of the base point and
write quaternions with complex coefficients on the right:
\[
 u=a_0+j a_1,\qquad c=c_0+j\overline{c_1},\qquad q=u c.
\]
The auxiliary relation is
\((u,c)\sim(u e^{i\phi},e^{-i\phi}c)\). Thus \(q\)
is invariant and is an actual real trivialization of the
normal four-plane bundle. It reverses the complex normal
orientation once; composing with quaternionic conjugation
gives an oriented real trivialization if required.

Put \(s=A+B\). Under the actual Cox loop one has exactly
\[
 u'=e^{-is\theta/2}u e^{-is\theta/2},\qquad
 c'=e^{is\theta/2}c e^{i(A-B)\theta/2},
\]
and consequently
\[
 q'=e^{-is\theta/2}q e^{i(A-B)\theta/2}.               \tag{FSpin.3}
\]
This normal rotation is independent of the base point.
At \(\theta=2\pi\), both quaternionic multipliers are
the same central sign, so (FSpin.3) is a closed \(SO(4)\)
loop with parity \(s\). In the oriented conjugate
trivialization it is
\(\bar q'=e^{-i(A-B)\theta/2}\bar q e^{is\theta/2}\),
again independent of the base.

Therefore the normal-section map of this Cox loop depends
only on the parameter circle and has degree zero on
\(\mathbb P^1\times S^1\). This supplies the exact Cox-side
normal marking. It does not identify that marking with the
rotating compression marking of P3K.9; their global comparison
still contains the exterior variation recorded in
`notes/part3_exterior_variation.md`.
