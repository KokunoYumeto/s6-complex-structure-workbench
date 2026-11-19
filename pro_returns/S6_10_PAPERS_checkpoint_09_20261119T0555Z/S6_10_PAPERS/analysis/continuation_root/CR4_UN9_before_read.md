# CR.4 and UN.9: rank-zero and boundary comparison before reading

19 November 2026. GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro.

Only `CR4_UN9_fresh_statement_input_packet.md` has been opened. No
target proof or target comparison receipt has been read. In particular
smoothness here concerns the reduced support of the full critical
locus; reducedness of the Jacobian ideal is not assumed.

## 1. The reduced equation and the remaining local case

Write the full local map as u*f^m. On a small simply connected ball
choose a holomorphic m-th root of u and replace the local reduced
equation by h=u^(1/m)*f. Its nonzero local levels are actual subsets
of global fibres at values h^m. Its critical germ is still the stated
smooth curve Sigma. Indeed every component of the critical germ of h
through the origin has h constant, hence zero; on h=0 the equations
dh=0 and df=0 agree up to a unit. Shrinking removes components not
through the origin. The Hessian ranks and generic transverse types
are also unchanged, since along Sigma the Hessian is multiplied by
a unit.

Straighten Sigma to x=y=0, with coordinate z along it. Then h belongs
to (x,y)^2. Write its transverse quadratic term as
(x,y) H(z) (x,y)^t, with H a holomorphic symmetric two-by-two matrix.
For a generic node H has rank two off z=0. For a generic cusp it has
rank one off z=0 and its transverse cubic coefficient in the kernel
direction is nonzero there.

The supplied A.5.17 already treats the case of a nonzero Hessian at
the point: the local equation is a constant transverse product. Its
generic type fixes that product as a node or a cusp. It therefore
remains to rule out H(0)=0 under the actual torus-family hypothesis.
The deformation arguments below preserve the critical axis and its
generic type near the chosen boundary; they need not preserve the
interior critical locus.

## 2. A nearby pinch germ in the generic-node case

Perturb the quadratic term by a small constant symmetric matrix C:
h_C=h+(x,y)C(x,y)^t. On the chosen link of Sigma, H is invertible,
and remains so for all sufficiently small C. At the origin det H
vanishes to positive finite order. For sufficiently small C its zeros
inside a small z-disc persist, by the argument principle on a boundary
circle where det H is nonzero.

Choose C so that at least one such zero z_C is simple and H(z_C)+C
has rank one. This choice exists by the following explicit incidence
argument. The rank-one locus det S=0 in the space of symmetric
two-by-two matrices is smooth; the derivative is the nonzero
functional adj(S). The incidence det(H(z)+C)=0 is therefore smooth
off S=0. Its projection to C fails to have a simple z-root exactly
where adj(H(z)+C):H'(z)=0. This is a proper analytic condition on
each neighbourhood with H' not identically zero: rank-one adjugates
span the symmetric matrices. Zeros of H' contribute only isolated
z-slices of dimension two. The rank-zero incidence has codimension
three. Their projected bad parameter sets have empty interior, while
the argument-principle root count persists for every sufficiently
small C. A small C outside those sets has the stated simple root.

At (0,0,z_C) the holomorphic splitting lemma with parameter z gives
h_C=X^2+g(Y,z). The critical axis remains present, so g=Y^2 b(Y,z).
The simple determinant zero says b(0,z_C)=0 and
partial_z b(0,z_C) is nonzero. Set Z=b(Y,z). This is an invertible
coordinate change in (Y,z), and the actual equation becomes

                         h_C=X^2+Y^2 Z.

The supplied local Hirzebruch calculation consequently gives a
compact spherical class of self-intersection -4 in every sufficiently
small regular nonzero local level of this germ.

## 3. A nearby Y^3+X^2Z germ in the generic-cusp case

The rank-one symmetric matrix H over the one-variable holomorphic
local ring can be written H=a(z)v(z)v(z)^t with v primitive. To see
the coordinate change explicitly, saturate its rank-one image line
in O_disc^2, choose its primitive generator v and extend v to a
holomorphic basis. Symmetry makes the quadratic form vanish on its
kernel line and gives a single scalar coefficient a in that basis.
Thus a holomorphic linear transverse coordinate change writes the
quadratic term as a(z)X^2. Since H(0)=0 and its punctured rank is one,
a has a positive finite vanishing order at zero.

Use the two-parameter perturbation

                    h_(epsilon,delta)=h+epsilon X^2+delta Y^3.

Choose epsilon arbitrarily small so that a(z)+epsilon has a simple
zero z_e near zero. This follows by choosing a regular nonzero value
of the one-variable function a, together with its preserved local
zero count. Choose delta small so that the cubic coefficient of Y^3
at z_e is nonzero. On the boundary link a and the original cubic
coefficient are both units, so these properties also persist there
uniformly for small parameters.

Weierstrass preparation in Y at (0,0,z_e) gives a unit times

                    Y^3+A(X,z)Y^2+B(X,z)Y+C(X,z).

The critical axis and the displayed rank-one quadratic form imply
A is divisible by X and B,C are divisible by X^2. For example the
restriction at X=0 is Y^3 times a unit, while the X-derivative at
X=0 has no constant or linear Y term. Shift Y by -A/3. The new
linear and constant coefficients are
B-A^2/3 and C-AB/3+2A^3/27; both remain divisible by X^2. The
prepared equation is therefore

                       Y^3+X^2(beta(X,z)Y+gamma(X,z)).

Here gamma(0,z_e)=0 and partial_z gamma(0,z_e) is nonzero, because
the original X^2 coefficient had a simple z-zero. Set
Z=beta(X,z)Y+gamma(X,z). This is an invertible coordinate change.
A remaining unit v is absorbed by X'=v^(1/2)X and Y'=v^(1/3)Y,
whose Jacobian is invertible at the origin. The actual germ is

                             Y'^3+X'^2 Z.

Again the supplied local calculation produces a compact spherical
class with self-intersection -4 in a sufficiently small regular
nonzero local level.

## 4. Uniform boundary transversality for the actual perturbation

Let B_r be the closed ball in the input setup, with rho its boundary
function. On its critical link, rho restricted to Sigma has nonzero
differential. The generic transverse node/cusp is constant there.
For the selected perturbation families, the nonzero transverse
quadratic determinant (node), or the nonzero rank-one quadratic and
kernel cubic coefficients (cusp), remain units on a neighbourhood
of this compact link for all small parameters.

The parameter splitting and root coordinate changes on a finite
cover of that link therefore give actual local forms
X^2+Y^2 or X^2+Y^3, independent of the coordinate Z along Sigma,
throughout those parameter neighbourhoods. Along the link choose a
real vector in the Z-direction on which d(rho) is nonzero. By
continuity it remains nonzero on a smaller product neighbourhood.
This vector is tangent to every local level, because the normal form
is independent of Z. Hence every regular level in that neighbourhood
meets the boundary transversely, uniformly for all small parameters.

On the rest of the boundary near the original zero level, the given
transversality of the smooth hypersurface stratum says
(Re h, Im h, rho) has full real rank three. Compactness and the open
rank condition preserve that rank for every small parameter and
small level value. The remaining compact boundary set has |h|
bounded away from zero, and contains no sufficiently small perturbed
level. Combining these three regions proves a single radius and
parameter/level bounds with uniform transverse boundary. No new
boundary-fibration hypothesis has been assumed.

## 5. A regular path and the actual transport into an original fibre

Write p for the chosen one- or multi-parameter deformation. In the
parameter domain with t nonzero, exclude the pairs (p,t) for which
h_p=t has an interior critical point in B_r. This is a proper
analytic discriminant. To verify the properness used for its analytic
image, note that the boundary neighbourhood just described has no
critical points at nonzero levels. The critical set over any compact
subset of the punctured parameter/level domain is consequently
contained in a fixed compact subset of the interior. Its projection
is proper, and Remmert's proper-image theorem makes its image
analytic. It has empty interior: for each fixed p the holomorphic
function is constant on each component of its critical set, so its
critical values in the compact local problem are discrete. At p=0,
every sufficiently small nonzero t is regular.

The complement of a proper complex analytic subset in this connected
complex parameter domain is path connected. This follows locally by
joining points with generic complex line segments, whose intersections
with the analytic set are discrete, and detouring inside the complex
line; a finite coordinate-ball chain gives the global path. Choose
at the endpoint p=p_* a sufficiently small t_* for the local
Hirzebruch class, also avoiding the finitely many other critical
values. A path in the discriminant complement joins (p_*,t_*) to
(0,t_0), with t_0 nonzero.

Over this path, the compact level manifolds in B_r form a proper
submersion with transverse boundary, by step4 and avoidance of the
interior discriminant. The proper-submersion theorem with boundary
therefore gives orientation-preserving diffeomorphisms of the levels.
The spherical map in the small local level lies in the interior and
is transported into the interior of the original local level h=t_0.
That original level is a subset of the actual global torus fibre at
base value t_0^m, by step1.

The self-intersection is preserved through both maps. Explicitly,
for the compact spherical two-cycle in the oriented local fourfold,
its Poincare dual is a compactly supported degree-two class.
Extension by zero under the open embedding into the torus identifies
its square pairing with the local square pairing. The preceding
diffeomorphism preserves that pairing as well. Thus its image in the
torus has self-intersection -4.

The universal cover of the complex two-torus is C^2. The spherical
map lifts and is null-homotopic, so its homology class in the torus
is zero and its self-intersection is zero. This contradicts -4.
Both rank-zero cases are excluded by the actual comparison maps.

## 6. Conclusion and scope

The Hessian at the original point is nonzero. The supplied A.5.17
now gives a constant transverse product; the generic node/cusp fixes
its exponent. The node coordinates X^2+Y^2 change to the product
(X+iY)(X-iY), and the cusp is X^2+Y^3. The analytic unit in a reduced
equation is absorbed by the corresponding weight-root coordinate
map, and the common full-fibre multiplicity is retained.

This proves both requested reduced-hypersurface conclusions from the
actual hypotheses. The whole derivation, especially the boundary
cover, proper discriminant and fibre transport, is now written before
either target proof is opened. The local negative spherical class and
A.5.17 remain the explicitly supplied cited inputs; their proofs are
not being independently rederived here.
