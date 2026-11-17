# Boundary-preserving exclusions for generic ordinary-double critical curves

Working proof, 2026-11-17. This is separate from the frozen TeX and is not
yet included in the proved statement map. Independent root audit requested.

## A. A singular planar critical curve is impossible

Let the reduced critical curve at a point have ideal `(z,h(x,y))`, with h
reduced and singular at the origin. Suppose every generic transverse germ
along its branches is an ordinary double point. Then the reduced equation f
belongs to the symbolic square of this ideal; because `(z,h)` is a regular
sequence, its symbolic and ordinary squares agree. Thus

\[
 f=A z^2+Bzh+Ch^2.
\]

Add a sufficiently small constant multiple of z². This retains the critical
curve and retains its transverse A1 germs near a fixed compact boundary,
where their rank-two Hessians were already nondegenerate. Choose the
constant so that the coefficient of z² at the origin is nonzero. The Morse
lemma in z, with parameters x,y, writes the new equation as

\[
 Z^2+h(x,y)^2u(x,y).
\]

Indeed the removed critical z-coordinate vanishes on h=0 and is divisible
by h. Add a small constant to u if necessary, and pass to a smaller ball
where this new u is a unit. Its square root absorbs into h. We have reduced,
through boundary-A1 deformations, to `Z²+H(x,y)²`, where H has the same
singular reduced zero curve as h. A reduced plane curve has an isolated
critical point at such a singular point. A generic small morsification H_s
has Morse critical points, and adding a small constant makes their critical
values nonzero. At each of them, `Z²+H_s²` has an isolated nondegenerate
critical point: the plane Hessian is `2 H_s Hess(H_s)` and the Z Hessian is
2. Its vanishing sphere has square −2.

Every deformation retains ordinary-double transverse type near its own
fixed boundary. For the deformation of H, the moving critical curve H_s=0
is transverse to that boundary and the normal quadratic form remains
nondegenerate. The boundary submersion and finite-critical-value argument
of P4.20 transports the compact sphere, first into the preceding smaller
ball and then into the original nearby fibre. This contradicts its
inclusion in a four-torus. Thus no such planar singular critical curve
occurs. This argument allows singular normalization.

## B. A transverse union of a cusp and a smooth branch is impossible

Consider the nonplanar reduced curve consisting of the cusp
`z=0, h=y²−x³=0` and the transverse line `x=y=0`. Its ideal is

\[
 P=(xz,yz,h).
\]

The symbolic square is computed directly from its two component ideals:

\[
 P^{(2)}=(z,h)^2\cap(x,y)^2
 =(x^2z^2,xyz^2,y^2z^2,zh,h^2).
\]

To check the intersection identity, write an element of `(z,h)²` as
`a z²+b z h+c h²`. The last two terms already belong to `(x,y)²`.
Since z is a nonzero divisor modulo `(x,y)²`, the first does so exactly when
`a∈(x,y)²`. Consequently every hypersurface with this critical curve and
generic transverse A1 germs has the form

\[
 f=Azh+z^2(Bx^2+Cxy+Dy^2)+Gh^2.
\]

Small constant changes in A and B preserve the critical curve and its
nondegenerate transverse Hessians near a fixed boundary. We make A(0),B(0)
nonzero, then use a smaller neighbourhood. Replace h by

\[
 h_s=y^2-x^3-sx^2
\]

in this exact expression. The new critical curve contains `z=0,h_s=0`
and `x=y=0`, and the boundary ordinary-double germs persist. On the latter
axis, the transverse quadratic form in x,y has matrix coefficients

\[
 a=-sAz+Bz^2,\qquad b=Cz^2,\qquad c=Az+Dz^2,
\]

where A,B,C,D are restricted to that axis. Its determinant divided by z² is

\[
 F(s,z)=(-sA+Bz)(A+Dz)-C^2z^2/4.
\]

At (0,0), its z derivative is A(0)B(0), and its s derivative is
`−A(0)²`. The implicit-function theorem therefore gives a simple root
`z(s)=s A(0)/B(0)+O(s²)`, nonzero for small nonzero s. At this root the
y² coefficient is nonzero, the Hessian rank is one, and its determinant
has a simple zero in the axis direction. The parametrized Morse lemma
gives `Y²+x²H(x,z)` with `H_z≠0`. The exact coordinate change
`Z=H(x,z)` produces the pinch germ `Y²+x²Z`.

P4.16 supplies its compact spherical class of square −4. The same nested
boundary-A1 transport used in A carries it into an actual nearby torus
fibre, a contradiction. Thus this critical-curve germ cannot occur either.

## Why these are relevant

For a reduced image conductor with two rational normalized components,
one graph cycle, and arithmetic genus two, the total excess of analytic
delta over the graph contribution is one. Planar excess-one germs are
excluded by A. The minimal nonplanar two-branch excess-one germ is a cusp
plus a transverse smooth branch, excluded by B. A complete use of this
observation still requires an exact classification of all excess-one curve
germs and verification that the conductor image is reduced in the sector
at issue. Those further steps are not claimed here.
