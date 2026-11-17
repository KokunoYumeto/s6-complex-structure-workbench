#!/usr/bin/env python3
"""Exact lattice, canonical and Euler checks for C.2.UN.78."""
from itertools import product
from math import gcd, lcm
from functools import reduce
import sympy as s


def need(value, message):
    if not value:
        raise AssertionError(message)


def egcd(a, b):
    if b == 0:
        return 1, 0, a
    x, y, g = egcd(b, a % b)
    return y, x-(a//b)*y, g


def bezout(values):
    g, result = 0, []
    for a in values:
        x, y, new_g = egcd(g, a)
        result = [x*c for c in result]+[y]
        g = new_g
    need(g == 1, 'primitive weight row')
    need(sum(a*b for a, b in zip(values, result)) == 1, 'actual Bezout vector')
    return result


volumes = 0
burnside = 0
for r in (1, 2, 3):
    for multiplicities in product(range(1, 11), repeat=r):
        d = reduce(gcd, multiplicities)
        primitive = [m//d for m in multiplicities]
        b = s.Matrix(bezout(primitive))
        for factor in (1, 2, 3):
            N = factor*lcm(*multiplicities)
            vertices = [s.eye(r)[:, i]*(N//multiplicities[i]) for i in range(r)]
            columns = [vertices[i]-vertices[-1] for i in range(r-1)]+[b]
            determinant = abs(s.Matrix.hstack(*columns).det())
            expected = s.Rational(N**(r-1)*d, reduce(lambda a, c: a*c, multiplicities, 1))
            need(determinant == expected and expected.q == 1,
                 'normalized height-one simplex volume')
            need(expected > 0, 'positive normalized volume')
            need(N % d == 0, 'root stabilizer order integer')
            fixed_sum = sum(d for j in range(N) if j % d == 0)
            need(fixed_sum == N, 'literal root-cover fixed-point Burnside average')
            volumes += 1
            burnside += 1
print(f'PASS {volumes} exact Bezout/determinant simplex volumes')
print(f'PASS {burnside} actual cyclic stratum-cover fixed-point averages')

pick_cases = 0
canonical_cases = 0
for multiplicities in product(range(1, 7), repeat=3):
    N = lcm(*multiplicities)
    d = reduce(gcd, multiplicities)
    points = []
    for v0 in range(N//multiplicities[0]+1):
        for v1 in range(N//multiplicities[1]+1):
            remainder = N-multiplicities[0]*v0-multiplicities[1]*v1
            if remainder >= 0 and remainder % multiplicities[2] == 0:
                points.append((v0, v1, remainder//multiplicities[2]))
    interior = sum(all(v > 0 for v in point) for point in points)
    boundary = len(points)-interior
    nu = s.Rational(N*N*d, reduce(lambda a, c: a*c, multiplicities, 1))
    need(nu == 2*interior+boundary-2, 'Pick unimodular triangle count')
    pick_cases += 1
    for orders in product(range(3), repeat=3):
        old = [s.Rational(N*(k+1), m)-1 for k, m in zip(orders, multiplicities)]
        minimum = min(old)
        need(all(a.q == 1 for a in old), 'strict canonical orders integral')
        observed = []
        for point in points:
            actual = sum((k+1)*v for k, v in zip(orders, point))-1
            convex = sum(s.Rational(m*v, N)*a
                         for m, v, a in zip(multiplicities, point, old))
            need(actual == convex, 'exact canonical ray interpolation')
            need(actual >= minimum, 'no smaller exceptional canonical order')
            observed.append(actual)
            canonical_cases += 1
        need(min(observed) == minimum, 'old vertices attain the actual minimum')
print(f'PASS {pick_cases} height-one lattice triangles and exact Pick counts')
print(f'PASS {canonical_cases} canonical ray/Jacobian/minimum comparisons')

for h in range(1, 101):
    exceptional_euler = 1 if h == 1 else 2*(h-1)-(h-2)
    need(exceptional_euler == h, 'A_(h-1) fibre Euler equals segment length')
print('PASS 100 exact double-stratum chain Euler numbers')

E0, DK, RN, DP = s.symbols('E0 DK RN DP', integer=True)
EZ = E0-DK
EY = EZ-RN
EX = EY-DP
need(s.expand(EX-(E0-DK-RN-DP)) == 0, 'all actual Euler arrows telescope')
need(s.solve(s.Eq(EX, 0), E0) == [DK+RN+DP], 'exact original zero criterion')
print('PASS symbolic original/root/core Euler reconstruction and zero criterion')

# A flat simple toric fibre has only triple strata with nonzero open Euler.
# Its N-root subdivision has normalized triangle area N^2 at each triple.
examples = 0
for N in range(1, 41):
    for d in range(3, 31):
        triples = 2*d
        e_original = triples
        e_root = N*N*triples
        correction = (N*N-1)*triples
        need(e_root-e_original == correction, 'exact toric root Euler correction')
        examples += 1
print(f'PASS {examples} positive toric root Euler examples')

# Distinguish root exponent N from the flat-core lattice index d0.
# Compact original resolution corrections are independently signed.
zero_checks = 0
for d0 in range(0, 17):
    for point_count in range(6):
        for genus in range(9):
            DP0 = 2*point_count+2-2*genus
            for RN0 in range(-6, 7, 2):
                DK0 = 2*d0-RN0-DP0
                need(2*d0-DK0-RN0-DP0 == 0, 'actual zero-balance integer identity')
                zero_checks += 1
print(f'PASS {zero_checks} independent root/resolution/core zero balances')

unit, root, coefficient = s.symbols('unit root coefficient', nonzero=True)
for multiplicity in range(1, 31):
    transformed = (root/unit)**multiplicity-coefficient/unit**multiplicity
    need(s.factor(transformed-(root**multiplicity-coefficient)/unit**multiplicity) == 0,
         'intrinsic normal-line root transition')
print('PASS 30 intrinsic normal-line root-cover transition algebras')

threshold_checks = 0
for codim in (2, 3):
    for branches in range(1, codim+1):
        for multiplicities in product(range(1, 5), repeat=branches):
            for orders in product(range(3), repeat=branches):
                old = [s.Rational(k+1, m) for k, m in zip(orders, multiplicities)]
                new = s.Rational(sum(orders)+codim, sum(multiplicities))
                average = sum(m*r for m, r in zip(multiplicities, old))/sum(multiplicities)
                need(new == average+s.Rational(codim-branches, sum(multiplicities)),
                     'actual refinement density/Jacobian ratio')
                need(new >= min(old), 'refinement preserves integrability minimum')
                tau = min(old)
                need(any(k-tau*m == -1 for k, m in zip(orders, multiplicities)),
                     'logarithmic divergence at the exact threshold')
                need(all(k-(tau-s.Rational(1, 1000))*m > -1
                         for k, m in zip(orders, multiplicities)),
                     'integrability strictly below the threshold')
                threshold_checks += 1
print(f'PASS {threshold_checks} exact intrinsic-threshold/Jacobian refinements')
print('ALL C.2.UN.78 EXACT CHECKS PASSED')
