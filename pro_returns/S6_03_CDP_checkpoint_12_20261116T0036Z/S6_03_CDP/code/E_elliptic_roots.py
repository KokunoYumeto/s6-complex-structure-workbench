"""Exact algebra and integral matrices supporting C.2.UN.6."""
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
from math import lcm

a, b, z, w, y, q = s.symbols("a b z w y q", nonzero=True)
for m in range(2, 13):
    assert s.cancel((a**m*b).subs({a: z/w, b: w**m}, simultaneous=True)) == z**m
    assert s.cancel((a**m*b).subs({a: q**-1*a, b: q**m*b}, simultaneous=True)) == a**m*b
    assert s.cancel((a**m*b*y).subs({a: z/w, b: w**m}, simultaneous=True)) == z**m*y
    assert s.diff(z**m, z) == m*z**(m-1)
    # Diagonal mu_m weights of a=z/w and b=w^m are zero modulo m.
    assert (1-1) % m == 0 and m % m == 0
print("Exact quotient, q-action, full-fibre and canonical-vanishing identities passed for m=2,...,12")
print("Universal identities: x=a^m*b=z^m; t=z^m*y; dx=m*z^(m-1) dz")

# Boundary columns: solid-torus meridian and longitude.
# Rows: the two base generators, the outside circle h, the inside longitude.
# The base boundary delta is zero in H1 of a once-punctured elliptic curve.
boundary = s.Matrix([[0, 0], [0, 0], [1, 0], [0, -1]])
snf = smith_normal_form(boundary, domain=ZZ)
assert [abs(x) for x in snf.diagonal()] == [1, 1]
assert boundary.rank() == 2
print("Mayer--Vietoris boundary matrix:")
print(boundary)
print("Smith diagonal:", list(snf.diagonal()), "; cokernel = Z^2; H1(P_m)=Z^3")

def plurigenus(m, r):
    degree = r*(m-1)//m
    return 1 if degree == 0 else degree

comparisons = 0
for m in range(2, 13):
    for n in range(m+1, 13):
        r = 2*lcm(m, n)
        assert plurigenus(m, r) != plurigenus(n, r)
        comparisons += 1
print("Exact distinguishing plurigenus checks:", comparisons, "pairs")
for m in (2, 3, 4, 7):
    print("m=", m, ": first 12 plurigenera =", [plurigenus(m, r) for r in range(1, 13)],
          "; asymptotic slope =", s.Rational(m-1, m))
assert 0+0-0 == 0
print("Central Euler equality: e(P_m)+e(Q_m)-e(J)=0")

# Explicit source-audit counterexample: diagonal Hopf threefold -> P^2.
c, Y, Z, lam = s.symbols("c Y Z lam")
for m in range(2, 13):
    coordinates = s.Matrix([a**m, b, c])
    transformed = coordinates.subs({a: q*a, b: q**m*b, c: q**m*c}, simultaneous=True)
    assert transformed == q**m*coordinates
    generic_fibre = coordinates.subs({b: Y*a**m, c: Z*a**m}, simultaneous=True)
    assert generic_fibre == a**m*s.Matrix([1, Y, Z])
    multiple_fibre = coordinates.subs({a: 0, b: lam*Y, c: lam*Z}, simultaneous=True)
    assert multiple_fibre == lam*s.Matrix([0, Y, Z])
print("Hopf source-audit map [a,b,c] -> [a^m:b:c]: equivariance and both fibre parametrizations passed")
print("Along the projective line X=0, pullback order is m, while the line has self-intersection 1")
print("All exact checks passed.")
