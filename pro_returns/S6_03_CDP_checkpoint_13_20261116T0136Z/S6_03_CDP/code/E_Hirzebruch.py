"""Exact arithmetic for A.5.15; no numerical approximation is used."""
from math import gcd
from fractions import Fraction
import sympy as sp


def data(a, b, c):
    assert a >= 2 and b >= 1 and c >= 1 and gcd(a, gcd(b, c)) == 1
    d = gcd(b, c)
    bp, cp = b // d, c // d
    beta_c = 0 if cp == 1 else (-pow(bp, -1, cp)) % cp
    beta_b = 0 if bp == 1 else (-pow(cp, -1, bp)) % bp
    e0 = Fraction(a) - a * Fraction(beta_c, cp) - a * Fraction(beta_b, bp)
    assert e0 == Fraction(a, bp * cp)
    genus = (a - 1) * (d - 1)
    b1 = genus
    b2 = (a - 1) * d
    boundary_b1 = 2 * genus
    intersection_rank = b1 + b2 - boundary_b1
    assert intersection_rank == a - 1 > 0
    return d, bp, cp, beta_c, beta_b, e0, b1, b2, boundary_b1, intersection_rank


count = 0
for a in range(2, 13):
    for b in range(1, 25):
        for c in range(1, 25):
            if gcd(a, gcd(b, c)) != 1:
                continue
            data(a, b, c)
            count += 1
print(f"Exact Seifert and intersection-rank identities checked for {count} triples.")

print("a b c | d b1(M) b2(M) b1(boundary) rank(I) e0 | torsion determinant")
for a, b, c in [(2, 1, 2), (2, 1, 4), (2, 3, 4), (2, 3, 6),
                 (3, 2, 4), (3, 4, 5), (4, 3, 6), (5, 3, 9)]:
    d, bp, cp, bc, bb, e0, b1, b2, boundary_b1, rank = data(a, b, c)
    # Rational Seifert presentation including harmless order-one fibres.
    presentation = sp.zeros(2 * a + 1)
    for i in range(a):
        presentation[i, i] = cp
        presentation[i, -1] = bc
    for i in range(a, 2 * a):
        presentation[i, i] = bp
        presentation[i, -1] = bb
    for i in range(2 * a):
        presentation[-1, i] = 1
    presentation[-1, -1] = a
    determinant = presentation.det()
    assert determinant == a * (bp * cp) ** (a - 1)
    assert presentation.rank() == 2 * a + 1
    print(a, b, c, "|", d, b1, b2, boundary_b1, rank, e0, "|", determinant)

print("The join CW model has (a-1)(d-1) circle cells and (a-1)d spherical two-cells.")
print("All H2 classes are spherical, while the rational intersection rank is a-1.")
print("For (a,b,c)=(2,1,ell), the integral intersection determinant has absolute value 2 ell.")
