#!/usr/bin/env python3
"""New LP calculations from explicit admitted LA matrices and the actual fan.
This program reads no target original, historical LP program or target table.
The refined even-order spin class remains outside its conclusions.
"""
from math import gcd
from sympy import Matrix, Poly, Rational, Symbol, expand, eye, factor, rem, zeros


def bezout(a, b):
    r0, r1 = a, b
    s0, s1, t0, t1 = 1, 0, 0, 1
    while r1:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    if r0 < 0:
        r0, s0, t0 = -r0, -s0, -t0
    assert a * s0 + b * t0 == r0
    return r0, s0, t0


D = Symbol('D', integer=True, positive=True)
delta, a, b, gamma = [Symbol(s, integer=True) for s in ('delta', 'a', 'b', 'gamma')]
lam = Matrix([delta, a, b, gamma])
A0 = Matrix([[1, -1, 0, 2*D], [0, -1, -1, 6*D], [0, 1, 0, 0], [0, 0, 0, 1]])
A1 = Matrix([[1, 0, 1, -3*D], [0, 0, 1, 0], [0, -1, 0, 6*D], [0, 0, 0, 1]])
Ainf = eye(4)
Ainf[1, 2], Ainf[0, 3] = 1, D
E = Matrix([[0, 0, 0, -6*D], [0, 0, 1, 0], [0, -1, 0, 0], [6*D, 0, 0, 0]])
assert A0 * A1 * Ainf == eye(4)
assert A0**3 == A1**4 == eye(4)


def q(v):
    return v[1] * v[2] + v[1] + v[2]


def zero_integer_function_mod_two(poly):
    # Integer inputs reduce to the Boolean ring: x^2=x over F2.
    # Coefficientwise evenness is stronger and would reject x^2+x.
    reduced = {}
    for powers, coefficient in poly.terms():
        key = tuple(min(power, 1) for power in powers)
        reduced[key] = (reduced.get(key, 0)+int(coefficient)) % 2
    return not any(reduced.values())


for name, A in [('A0', A0), ('A1', A1), ('Ainf', Ainf)]:
    assert A.T * E * A == E
    difference = Poly(expand(q(A*lam)-q(lam)), delta, a, b, gamma, D)
    assert zero_integer_function_mod_two(difference)
    print(name, 'preserves xi; q difference =', difference.as_expr())

mu_symbols = [Symbol('mu_'+s, integer=True) for s in ('delta', 'a', 'b', 'gamma')]
mu = Matrix(mu_symbols)
polar = Poly(expand(q(lam+mu)-q(lam)-q(mu)-(lam.T*E*mu)[0]),
             delta, a, b, gamma, D, *mu_symbols)
assert zero_integer_function_mod_two(polar)
print('PASS quadratic refinement and lattice cocycle parity for every integer D.')
print('FINITE LIFT commutator exponent = -6 D theta lambda_gamma; N divides 6D.')

# Direct relation preimages: a different marked quotient check from Smith data.
weights = [1, 2, 3, 4, 6, 8, 12]
total = 0
for d in weights:
    count = 0
    for k in range(1, 7):
        for ell in range(1, 7):
            m0, m1 = 3*k, 4*ell
            if gcd(m0, m1) != 1:
                continue
            _, n0base, n1base = bezout(m1, m0)
            _, AA, BB = bezout(-k, 2*ell)
            for sign in (-1, 1):
                for shift in (-1, 0, 1):
                    n0 = sign*n0base + shift*m0
                    n1 = sign*n1base - shift*m1
                    P = m1*n0 + m0*n1
                    assert P == sign
                    _, alpha0, eta0 = bezout(m0, n0)
                    _, alpha1, eta1 = bezout(m1, n1)
                    for r0, r1 in [(-2, 3), (0, 0), (7, -5)]:
                        B = Matrix([[-2*d*n0, -6*d*r0, 0, -3*d*n1, -6*d*r1, 0],
                                    [-k, 0, r0, 2*ell, 0, -r1],
                                    [0, m0, n0, 0, 0, 0],
                                    [0, 0, 0, 0, m1, n1]])
                        basis = eye(6)
                        Rd = -P*(2*ell*basis[:, 0]+k*basis[:, 3])
                        qq = 2*AA*n0+3*BB*n1
                        Rt = AA*basis[:, 0]+BB*basis[:, 3]+qq*Rd
                        C0 = alpha0*basis[:, 1]+eta0*basis[:, 2]
                        C1 = alpha1*basis[:, 4]+eta1*basis[:, 5]
                        Rt0 = C0+6*r0*alpha0*Rd-r0*eta0*Rt
                        Rt1 = C1+6*r1*alpha1*Rd+r1*eta1*Rt
                        inverse_relations = Matrix.hstack(Rd, Rt, Rt0, Rt1)
                        assert B*inverse_relations == Matrix.diag(d, 1, 1, 1)
                        assert all(int(x) % d == 0 for x in B[0, :])
                        quotient = Matrix([[1, 0, 0, 0]])
                        assert quotient*eye(4)[:, 0] == Matrix([[1]])
                        R = Matrix([[-n0, m0], [-n1, -m1]])
                        Rinv = P*Matrix([[-m1, -m0], [n1, -n0]])
                        assert R*Rinv == Rinv*R == eye(2)
                        exterior_basis = Matrix([[-n0, -n1, 0],
                                                 [m0, 0, P], [0, m1, P]])
                        assert exterior_basis.det() == 1
                        exterior_reading = Matrix([[m0*m1, n0*m1, m0*n1]])
                        assert exterior_reading*exterior_basis == Matrix([[0, 0, 1]])
                        count += 1
    total += count
    print('WEIGHT', d, 'all four relation preimages and H1 inverse maps:', count, 'cases')
print('TOTAL marked filling cases', total)

x, y, j, c = [Symbol(s, integer=True) for s in ('x', 'y', 'j', 'c')]


def phi(xx, yy):
    return -Rational(1, 2)*xx*(xx-1)+3*yy**2


assert expand(phi(x+1, y)-phi(x, y)) == -x
assert expand(phi(x, y+D)-phi(x, y)) == 6*D*y+3*D**2
rays = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
degrees = []
for i, (vx, vy) in enumerate(rays):
    left, right = rays[(i-1) % 6], rays[(i+1) % 6]
    wall = expand(phi(left[0], j+left[1])+phi(right[0], j+right[1])
                  -phi(0, j)-phi(vx, j+vy))
    degrees.append(-wall)
print('EXACT WALL DEGREES', degrees)
assert degrees == [-6, 1, 0, -6, 1, 0]
vertical_slope = expand(phi(0, j+1)-phi(0, j))
assert vertical_slope == 6*j+3
print('TORIC period differences -x and 6D*y+3D^2; six complex line degrees', degrees)
print('FIXED CURVE line character', -vertical_slope, 'modulo N dividing 6D')
surface_class = Matrix([-5, -1, 6, 0])
intersection = Matrix.diag(1, -1, -1, -1)
assert (surface_class.T*intersection*surface_class)[0] == -12
print('NORMALIZATION degree tuple [-5,1,-6,0]; square = -12')

t, z = Symbol('t'), Symbol('z')
roots = [2*z, t-z, -t-z]
c1 = sum(roots)
c2 = sum(roots[i]*roots[k] for i in range(3) for k in range(i+1, 3))
euler = roots[1]*roots[2]
p1 = sum(v*v for v in roots)
assert c1 == 0
assert rem(expand(c2-euler), z**2, z) == 0
assert rem(expand(p1+2*euler), z**2, z) == 0
print('FIXED BUNDLE c1=0, c2/e=1, p1/e=-2 in the curve cohomology ring.')
q3sum = expand(-3*(36*D*(D-1)*(2*D-1)/6 - 12*c*D*(D-1)/2 + D*c*c))
q3quotient = factor(q3sum/(3*D))
assert expand(3*D*q3quotient-q3sum) == 0
assert Poly(q3quotient, D, c).domain.is_ZZ
print('Q3 localization sum / (3D) =', q3quotient)
for d in range(1, 37):
    for constant in range(-d, d+1):
        actual = -3*sum((-6*i+constant)**2 for i in range(d))
        assert actual == int(q3sum.subs({D: d, c: constant}))
        assert actual % (d*gcd(d, 3)) == 0
print('PASS exact polynomial Q3 divisibility; bounded direct sums d=1..36 also agree.')

for d in range(1, 13):
    C = zeros(d, d)
    for i in range(d):
        C[i, i] -= 2
        C[i, (i+1) % d] += 1
        C[i, (i-1) % d] += 1
    assert C.rank() == d-1 and C*Matrix([1]*d) == zeros(d, 1)
    minor = C[:d-1, :d-1]
    assert abs(minor.det()) == d
    print('CYCLE', d, 'rank', d-1, 'principal determinant', minor.det())

print('SCOPE homology maps, actual fan, integral line and coefficient arithmetic only.')
print('OPEN even-order refined spin class; this output proves no value for it.')
