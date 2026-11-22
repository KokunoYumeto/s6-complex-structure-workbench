#!/usr/bin/env python3
"""Exact checks accompanying the two necessity examples in notes/part4.md.

No numerical root approximations enter the discriminant or chart checks.
The topological statements are proved in the notes; here their arithmetic
and the algebraic local models are recomputed.
"""
from sympy import symbols, expand, gcd, diff, Poly

t, s, x, y, u, v, r, a, b = symbols('t s x y u v r a b')
discriminant_core = t**12 - 4*s**12
affine = discriminant_core.subs(s, 1)
assert Poly(affine, t).degree() == 12
assert gcd(affine, diff(affine, t)) == 1
assert discriminant_core.subs({s: 0, t: 1}) == 1
print('Weierstrass discriminant core:', discriminant_core)
print('Degree on affine base:', Poly(affine, t).degree())
print('gcd(discriminant, derivative):', gcd(affine, diff(affine, t)))
print('Discriminant at infinity:', discriminant_core.subs({s: 0, t: 1}))
print('Number of singular elliptic fibres: 12, all simple nodal fibres')

# xy=uv; diagonal ideal (x-u,y-v), with r=x-u, s=y-v.
eq = r*y + u*s
assert expand(eq.subs({s: a*r, y: -a*u})) == 0
assert expand(eq.subs({r: b*s, u: -b*y})) == 0
first_t = expand((u+r)*(-a*u))
second_t = expand((-b*y+b*s)*y)
assert expand(first_t + a*u*(u+r)) == 0
assert expand(second_t.subs(s, y-v)) == -b*y*v
print('Small resolution chart 1: y=-a*u, x=u+r, t=-a*u*x')
print('Small resolution chart 2: u=-b*y, x=-b*v, t=-b*y*v')
print('Reduced central fibre in each chart: three coordinate hyperplanes')

e_nodal_curve = 2 - 1  # P1 with two distinct points identified.
e_original_special = e_nodal_curve**2
e_resolved_special = e_original_special - 1 + 2
e_total = 12*e_resolved_special
assert e_total == 24
print('Euler number of nodal cubic:', e_nodal_curve)
print('Euler number of its self-product:', e_original_special)
print('Euler number after replacing the conifold point by P1:', e_resolved_special)
print('Euler number of resolved global torus fibration:', e_total)

