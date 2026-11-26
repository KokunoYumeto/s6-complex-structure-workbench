"""Exact independent algebra for the LP circle-quotient characteristic bordism.

Input: the actual normal line degrees (-1,-1), characters (+1,-1),
and r_j=h-6j-3 already derived without the target original.
All geometric quotient and boundary maps are proved in the companion note.
"""
from itertools import combinations
import sympy as s

x, t, r, h, j = s.symbols('x t r h j', integer=True)
d = s.symbols('d', integer=True, positive=True)


def reduce_ring(expression):
    poly = s.Poly(s.expand(expression), x, t)
    return s.expand(sum(coefficient*x**a*t**b
                        for (a, b), coefficient in poly.terms()
                        if a < 2 and b < 3))


roots = (2*x, t, t-x, t+x)
c1 = reduce_ring(sum(roots))
c2 = reduce_ring(sum(a*b for a, b in combinations(roots, 2)))
p1 = reduce_ring(c1**2-2*c2)
assert c1 == 2*x+3*t
assert c2 == 3*t**2+6*x*t
assert p1 == 3*t**2
omega = (2*r+1)*t+2*x
numerator = reduce_ring(p1*omega-omega**3)
number = s.expand(numerator).coeff(x, 1).coeff(t, 2)
gamma = s.factor(number/s.Integer(8))
assert gamma == -3*r*(r+1)
assert s.expand(gamma.subs(r, r+2*d)-gamma).coeff(r, 1) % d == 0
print('RING x^2=0, t^3=0, integral(x*t^2)=1')
print('c1=', c1, 'c2=', c2, 'p1=', p1)
print('endpoint numerator=', s.factor(number), 'Gamma=', gamma)

endpoint_sum = s.summation(gamma.subs(r, h-6*j-3), (j, 0, d-1))
outer_gamma = s.factor(-endpoint_sum)
expected = 3*d*((h-3)*(h-2)-3*(2*h-5)*(d-1)
                +6*(d-1)*(2*d-1))
assert s.expand(outer_gamma-expected) == 0
quotient = s.Poly(s.cancel(outer_gamma/d), d, h, domain=s.ZZ)
print('outer Gamma integral polynomial=', outer_gamma)
print('outer Gamma/d integral polynomial=', quotient.as_expr())

cases = 0
for degree in range(2, 33):
    c = 2
    used = []
    while c <= degree:
        if degree % c == 0:
            for common in range(c):
                direct = 3*sum((common-6*k-3)*(common-6*k-2)
                               for k in range(degree))
                symbolic = int(outer_gamma.subs({d: degree, h: common}))
                assert direct == symbolic
                assert direct % c == 0
                for k in range(degree):
                    rr = common-6*k-3
                    old = -3*rr*(rr+1)
                    new = -3*(rr+c)*(rr+c+1)
                    assert (new-old) % c == 0
                cases += 1
            used.append(c)
        c *= 2
    if used:
        print(f'd={degree}: two-primary moduli={used}; '
              'all common characters and integral-lift changes checked; residue=0')

print(f'PASS: all symbolic identities and {cases} complete coefficient cases.')
print('The characteristic quotient, orientations and coefficient maps are proved in the note.')
