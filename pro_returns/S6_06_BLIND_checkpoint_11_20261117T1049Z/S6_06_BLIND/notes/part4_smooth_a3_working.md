# Smooth critical curves of generic type A3 in an actual torus degeneration

Current-run proof P4R.14, independently audited in full by checks and root.
Exact symbolic and six-point polar certificates in smooth_a3_polar.* pass.

At a point where the entire reduced critical locus is a smooth curve and
the generic transverse type is A3, the actual local equation of a reduced
support in Part4.2 has one of the two product/degeneration forms

    X^2+Y^4,                  X(Y^2+XZ).

The first normalization has two smooth branches; the second consists of a smooth plane
and a rational double point A1. In particular no exceptional curve of
positive genus occurs over such a point. All changes below are changes of
actual local holomorphic coordinates or boundary-preserving deformations.

## The weighted discriminant has no zero

Choose a parameter z along the critical curve and normal variables x,y.
The quadratic transverse Hessian has generic rank one. Diagonalizing the
symmetric matrix over C{z}, as in P4.28, makes the quadratic term h(z)x^2.
The null cubic coefficient is zero identically because the generic type is
A3. With weight2 for x and weight1 for y, the terms of weight4 are

    h(z)x^2 + a(z)xy^2 + b(z)y^4.

All remaining terms have larger weight. The discriminant
`Delta(z)=4h(z)b(z)-a(z)^2` is nonzero generically.

Suppose Delta has a zero at the point. Perturb the three coefficients by
small constants. Its zeros in a fixed sufficiently small parameter disc
are conserved by the one-variable argument principle. Generic such
perturbations make these zeros simple and disjoint from h=0: at a common
zero of h and Delta one would also have a=0, a codimension-two condition
which the independent constant changes avoid. At a zero with h nonzero,
the derivative of Delta with respect to the b-parameter is 4h, proving
the required transversality. The original critical curve and the generic
A3 germs near the fixed boundary are preserved throughout.

At a resulting simple zero, the parametrized Morse lemma removes x and
gives exactly `X^2+y^4 U(y,z)`, with `U(0,z)` having a simple zero. Thus
`Z=U(y,z)` is a holomorphic coordinate and the germ is `X^2+y^4 Z`.
P4.16 gives its compact spherical class of nonzero square. The explicit
boundary transport of P4.28 applies also to A3: near a boundary point the
parametrized Morse lemma and a fourth root of a unit give X^2+Y^4, whose
nonzero levels are submersive after the tangential boundary coordinate is
solved. It transports that sphere to the actual nearby torus, a
contradiction. Consequently Delta is a unit at the original point.

## The exact factorization at a Hessian zero

When h is a unit, Morse splitting and the unit discriminant give the
product tacnode. Otherwise h(0)=0 and Delta(0) nonzero force a(0) nonzero.
The actual analytic function

    f(y^2 v,y,z)/y^4

has value `h(z)v^2+a(z)v+b(z)` at y=0. At the point it has the finite
simple root v=-b(0)/a(0). The implicit-function theorem gives a
holomorphic root v=v(y,z). Thus the smooth graph `x=y^2v(y,z)` is an
actual factor of f. Set `X=x-y^2v(y,z)`; division by its monic equation
writes f=Xg. The coefficient of y^2 in g at the point is a unit.
The Morse lemma in y, with parameters X,z, gives

    f=X(Y^2+X H(X,z)).

The residual term is divisible by X because g restricted to X=0 has its
critical value zero along y=0. The coordinate Y vanishes on X=y=0.
The function H(0,z) is not identically zero, since the generic Hessian
rank is one. Its value at the point is zero.

## The polar curve forces the remaining singularity to be A1

Write `G=2H+X H_X`. The full derivatives of f show that, off X=0,
its critical equations are `Y=0, H_z=0, G=0`. The actual critical locus
has only the axis X=Y=0. If H_z(0,0)=0, then H_z is a nonzero plane
germ, not divisible by X, because H(0,z) has finite positive order.
No component of the polar curve H_z=0 can have G identically zero:
that would give an additional critical-curve branch off X=0. Hence
(H_z,G) is an isolated complete intersection at the origin, of positive
intersection multiplicity.

Use the explicit deformation `H -> H-eta*z-epsilon`, so the two plane
critical equations become

    H_z-eta=0,       G-2 eta z-2 epsilon=0.

Their local positive intersection number is conserved for sufficiently
small parameters; equivalently, the holomorphic map on the boundary of
a small four-ball has the same nonzero local degree. The universal map
to these two equations is submersive in (eta,epsilon), with determinant
2. Generic parameters therefore give a nonempty finite set of transverse
solutions. They avoid X=0: the parameter values admitting such a
solution are the images of that complex curve under the explicit map
`(X,z) -> (H_z,(G-2zH_z)/2)`. They also avoid H_X=0, whose
parameter values are images under the same map. On a small compact
representative, each curve has countably many smooth real two-dimensional
strata; their smooth images have four-dimensional Lebesgue measure zero.
Their union therefore cannot exhaust the open parameter ball on which
the positive local degree is retained. This argument does not require
the image of a nonproper analytic map to be analytic. H_X is not
identically zero, since H_X=0
identically would make H depend only on z and make H_z=G=0 contain
the whole line z=0, contrary to the isolated intersection just proved.

At such a solution the critical value is exactly

    f_(eta,epsilon)=-X^3 H_X/2,

which is nonzero. The Y-Hessian entry is 2X. The determinant of the
remaining two-by-two Hessian is X^3 times the Jacobian determinant
`J=det d(G-2 eta z-2 epsilon,H_z-eta)/d(X,z)`, with the order
specified here. Thus every transverse solution is
an isolated holomorphic Morse point. The deformation retains the smooth
critical axis and its A3 type near the fixed boundary, so the same
boundary comparison transports its (-2)-sphere to the nearby torus.
This is impossible. We conclude that H_z(0,0) is a unit.

The exact coordinate Z=H(X,z), keeping X and Y, now gives

    f=X(Y^2+XZ).

Its two normalization branches are the plane X=0 and the normal A1
quadric Y^2+XZ=0; its minimal resolution has one rational (-2)-curve.
This completes the local classification in the stated smooth-curve
scope. It makes no claim at an intersection with another critical curve.

## A retained local test

The polynomial

    f=x[y^2+x z(x-z)(x-2z)]

has only the smooth A3 critical axis x=y=0. Its second normalization
branch is a simple elliptic double plane; the exceptional elliptic curve
has pole coefficient2. Thus pole coefficient2 by itself does not exclude
positive genus outside the uniform-D4 argument. The explicit deformation
H -> H-epsilon above produces six off-axis Morse points with nonzero
critical values. This exact calculation is recorded in
code/part4/smooth_a3_polar.py and explains why this local polynomial is
excluded in an actual torus degeneration. It is not a proposed global
counterexample to Part4.2.
