"""Exact, denominator-retained two-cross residual identity; no file writes."""
import sympy as s

e, t, om, u, z, b, dm, ar, ai, nr, ni, n22 = s.symbols(
    'e t om u z b dm ar ai nr ni n22', real=True)
mb = ar-s.I*ai
N21 = nr-s.I*ni
B2 = 4*b-4*om*e
D2 = t/4-om**2-4*e**2
A21 = D2*mb+B2*N21
A22 = D2*z+dm+B2*n22
G21 = -6*e*mb-4*om*N21
G22 = -5*e*t/6-8*e*z-4*om*n22
g0 = e*t/6+4*e*(u+2*z)+8*om*b
lhs = 4*om**2*(mb*A22-z*A21)+om*B2*(mb*G22-z*G21)
lhs += e*(z+5*t/12)*mb*g0
rhs = 4*mb*(om**2*dm+e**2*(u+2*z+t/24+2*om**2)*(z+5*t/12))
if s.expand(lhs-rhs) != 0:
    raise RuntimeError('Full residual polynomial identity failed')
print('PASS: full denominator-free residual certificate on independent entries')

# Exact expansion behind the positive lower bound, before assuming signs.
positive = (u+2*z+t/24+2*om**2)*(z+5*t/12)
extra = z*(u+2*z+t/24+2*om**2)+(5*t/12)*(u+2*z+t/24)
if s.expand(positive-5*t*om**2/6-extra) != 0:
    raise RuntimeError('Retained positive remainder expansion failed')
print('PASS: strict lower-bound remainder with every coupling coefficient')
print('ALL 2 ROOT CERTIFICATE CHECKS PASSED')
