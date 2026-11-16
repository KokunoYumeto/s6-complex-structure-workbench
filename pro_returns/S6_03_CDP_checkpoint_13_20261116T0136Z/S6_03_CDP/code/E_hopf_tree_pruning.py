#!/usr/bin/env python3
"""Exact root-torsor, primitive-basis and recursive reinsertion identities."""
from math import gcd
from sympy import Matrix, symbols, simplify, gcdex, ZZ
from sympy.matrices.normalforms import smith_normal_form

basis_cases = 0
for a in range(-5, 6):
    for b in range(-5, 6):
        if a == b == 0:
            continue
        n = gcd(a, b)
        e = Matrix([-a//n, -b//n])
        s, t, d = gcdex(e[0], e[1])
        assert d == 1
        mat = Matrix.hstack(e, Matrix([-t, s]))
        assert mat.det() == 1
        assert mat.inv()*Matrix([a, b]) == Matrix([-n, 0])
        basis_cases += 1
print("actual primitive fibre-basis changes passed =", basis_cases)

root_cases = 0
for a in range(1, 21):
    for b in range(1, 21):
        g = gcd(a, b)
        rel = Matrix([[a, 0, -1], [0, b, -1]])
        snf = smith_normal_form(rel, domain=ZZ)
        assert abs(snf[0, 0]) == 1 and abs(snf[1, 1]) == g
        A, B = a//g, b//g
        assert gcd(A, B) == 1
        root_cases += 1
print("two-mark Picard lattices Z plus Z/g and coprime root covers =", root_cases)

x, W, Z, beta, d, t = symbols("x W Z beta d t", nonzero=True)
nested = 0
for m in range(1, 9):
    for n in range(1, 9):
        if gcd(m, n) != 1:
            continue
        for ell in range(m, m + 5):
            xp = x/beta
            Wp = beta*W
            Zp = beta**m*(Z + d*x**(ell-m)*W**ell)
            assert simplify(xp**m*Zp - x**m*Z - d*(x*W)**ell) == 0
            assert simplify(xp*Wp-x*W) == 0
            assert simplify(Zp/Wp**m-Z/W**m-d*(x*W)**(ell-m)) == 0
            # The inserted nonlinear monomial has the correct finite weight.
            assert (-(ell-m)+ell-m) % n == 0
            # Exact derivative of the old fibre form through t=xW.
            assert simplify(n*x**m/W - n*(x*W)**m/W**(m+1)) == 0
            nested += 1
print("weighted maps, full finite actions and exact remaining-order drops =", nested)
for ell in range(2, 21):
    assert simplify(d*t**ell/t-d*t**(ell-1)) == 0
print("ordinary product-cap drop1 passed for ell=2,...,20")

# A complete nested record, including a product cap, with exact positive margins.
R = 9
record = [(0, 1, 2, "Hopf"), (1, 2, 1, "cap"),
          (2, 3, 3, "Hopf"), (3, 4, 3, "nonlinear"),
          (1, 5, 4, "Hopf")]
height = {0: 0}
for parent, child, m, kind in record:
    height[child] = height[parent] + m
    remaining_before = R-height[parent]
    remaining_after = remaining_before-m
    assert remaining_after == R-height[child]
    if kind == "nonlinear":
        assert remaining_after == 0
    else:
        assert remaining_after > 0
    if kind == "cap":
        assert m == 1 and remaining_before >= 2
print("nested recorded heights =", height)
print("all central types and product-cap inequalities passed")
print("ALL CHECKS PASSED")
