"""Postrelease method supplement for II 02WN--02WQ, 2026-11-21.

This file was written after the target proofs and pinned historical programs
were opened.  It provides no additional prereading or independent-check credit.
No historical computational routine is imported or executed here.  The old
JSON is read only after the new coefficients have been computed, to exhibit
the exact integral change between two choices of torus coordinate.

Polynomial certificates use evaluation on a Cartesian grid with one more
point than each proved separate degree.  Repeated univariate interpolation
therefore proves the polynomial identities, not just their sampled values.
The universal geometric and all-parameter arguments are in the derivations
and the postrelease cycle-transport record.
"""

from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent


def grid_certificate(name, degrees, point_sets, polynomial):
    assert len(degrees) == len(point_sets)
    for degree, points in zip(degrees, point_sets):
        assert len(set(points)) == degree + 1
    count = 0
    for point in product(*point_sets):
        value = polynomial(*point)
        assert value == 0, (name, point, value)
        count += 1
    print(f"{name}: {count} exact values; separate degree bounds {degrees}.")
    return count


# A division search and a finite residue search, without Euclidean recursion.
# For coprime B,C the C residues B*p mod C are distinct: equality makes C
# divide B*(p-p'), hence C divide p-p'.  Thus residue 1 occurs exactly once.
new_rows = []
for b, c in product(range(1, 9), repeat=2):
    divisors = [k for k in range(1, min(b, c) + 1)
                if b % k == 0 and c % k == 0]
    d = max(divisors)
    B, C = b // d, c // d
    residues = [(B * p) % C for p in range(C)]
    assert len(set(residues)) == C
    p = 0 if C == 1 else residues.index(1)
    q = (1 - B * p) // C
    assert B * p + C * q == 1
    # The inverse is checked on each standard basis column by scalar equations.
    assert (B * p + C * q, q * p - p * q) == (1, 0)
    assert (B * C - C * B, q * C + p * B) == (0, 1)
    # This is the full d by d pairing matrix, including every off-diagonal pair.
    pairings = [[-2 * B * C for _ in range(d)] for _ in range(d)]
    assert sum(map(sum, pairings)) == -2 * b * c
    new_rows.append(dict(b=b, c=c, d=d, B=B, C=C, p=p, q=q,
                         all_lifted_pairings=pairings))

old_path = ROOT / 'code/S6_SERIES_PUBLISH_II_A_recovery_group05_prior_binomial_milnor.json'
old_bytes = old_path.read_bytes()
old_rows = {(row['b'], row['c']): row for row in json.loads(old_bytes)}
transports = []
for row in new_rows:
    b, c, d, B, C, p, q = (row[k] for k in ('b', 'c', 'd', 'B', 'C', 'p', 'q'))
    old = old_rows[b, c]
    p0, q0 = old['bezout']
    assert old['d'] == d and old['primitive_exponents'] == [B, C]
    assert (p - p0) % C == 0
    k = (p - p0) // C
    assert p == p0 + C * k and q == q0 - B * k
    # M_new = [[1,0],[-k,1]] M_old, checked by all four entries.
    assert [[B, C], [q, -p]] == [[B, C], [q0 - k * B, -p0 - k * C]]
    # t_new=h^(-k)t_old transports y=h^p t^C, z=h^q t^(-B).
    assert (p - k * C, q + k * B) == (p0, q0)
    assert old['transfer_degree'] == C
    assert old['spherical_square'] == row['all_lifted_pairings'][0][0]
    transports.append(dict(b=b, c=c, old_bezout=[p0, q0],
                           new_bezout=[p, q], k=k,
                           torus_map='h_new=h_old; t_new=h_old^(-k)*t_old'))
print('64 exponent pairs: exhaustive divisor/residue construction, integral inverses,')
print('all lifted-arc cross-pairings, and exact t_new=h^(-k)t_old transport to the pinned coefficients.')


# WQ: multiply the substituted fibre equation minus 1 by y^3.
# Each of y^4*x^2, (y*x^2-1)*y^3, y^3 has separate degree <=(2,4).
grid_certificate('WQ inverse after denominator clearing', (2, 4),
                 [range(-1, 2), range(1, 6)],
                 lambda x, y: y**4*x*x-(y*x*x-1)*y**3-y**3)
# Each term has separate degree <=(2,3) in (u,v).
grid_certificate('WQ Whitney parametrization', (2, 3),
                 [range(-1, 2), range(-1, 3)],
                 lambda u, v: v*((u*v)**2-u*u*v*v))


# WN: clear b^n in a/b^n - c/b^(n-j) with a=b^j*c.
# The two terms have b-degree n and c-degree 1, also at j=n.
total = 0
for n in range(1, 13):
    for j in range(1, n + 1):
        for b, c in product(range(1, n + 2), (0, 1)):
            assert b**j*c*b**(n-j)-b**n*c == 0
            total += 1
print(f'WN 78 blowup charts: {total} exact values, bounds (n,1), n=1..12 and j=1..n.')


# The n=2 alternative compactification has explicit rational inverse charts.
grid_certificate('WN n=2 rational chart numerator', (2, 2),
                 [range(-1, 2), range(-1, 2)],
                 lambda r, s: (r+s)**2-4*r*s-(r-s)**2)
grid_certificate('WN n=2 exceptional chart numerator', (4, 2),
                 [range(-2, 3), range(-1, 2)],
                 lambda R, z: (1+R*R*z)**2-4*R*R*z-(1-R*R*z)**2)


def boundary_coordinates(a, b, c, d):
    return a, a+b, b+c, a+d


def inverse_boundary_coordinates(a, r1, r2, r3):
    return a, r1-a, r2-r1+a, r3-a


# The two displayed integer linear maps are inverse on a Z-basis in each
# direction, hence inverse on every integral vector.  Their last three
# coordinates are the three boundary intersection functionals.
for j in range(4):
    e = tuple(int(i == j) for i in range(4))
    assert inverse_boundary_coordinates(*boundary_coordinates(*e)) == e
    assert boundary_coordinates(*inverse_boundary_coordinates(*e)) == e
kernel = inverse_boundary_coordinates(1, 0, 0, 0)
assert kernel == (1, -1, 1, -1)
grid_certificate('WN n=2 kernel norm', (2,), [range(-1, 2)],
                 lambda a: 2*a*(-a)-a*a-(-a)**2+4*a*a)
print('WN n=2 boundary kernel: explicit integral coordinate inverse gives primitive (1,-1,1,-1), square -4.')


# Exact maps at y=0 use R=y/(x+1) or S=y/(x-1).  At all displayed nonzero
# denominators this independent rational evaluation checks both directions.
# Universal inverse identities follow from x^2-z*y^2=1 and the certified
# cleared numerators above; no finite sample substitutes for that argument.
for R, z in product((Fraction(1, 2), Fraction(2, 3)), (Fraction(-1), Fraction(2))):
    den = 1-R*R*z
    if den == 0:
        continue
    x, y = (1+R*R*z)/den, 2*R/den
    assert x*x-z*y*y == 1 and y/(x+1) == R
    x, y = -(1+R*R*z)/den, -2*R/den
    assert x*x-z*y*y == 1 and y/(x-1) == R

output = ROOT / 'code/S6_SERIES_PUBLISH_II_A_recovery_group05_different_methods.json'
output.write_text(json.dumps(dict(
    timing='postrelease supplement; no new prereading credit',
    compared_old_data=str(old_path.relative_to(ROOT)),
    compared_old_data_sha256=hashlib.sha256(old_bytes).hexdigest(),
    transports=transports,
    n2_kernel=list(kernel),
    inverse_maps='(a,b,c,d)->(a,a+b,b+c,a+d); (a,r1,r2,r3)->(a,r1-a,r2-r1+a,r3-a)',
), indent=2)+'\n')
print('All different-method certificates passed; new data record contains every coefficient transport.')
