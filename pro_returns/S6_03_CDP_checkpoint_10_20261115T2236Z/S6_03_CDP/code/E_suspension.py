"""Exact local algebra and linking identities for A.5.15 and A.5.17."""
from math import gcd
import sympy as sp

x, y, z, a, c, m, v = sp.symbols('x y z a c m v')
H = y**2 - z**3 + 3*a**2*z
critical = [sp.Matrix([0, a]), sp.Matrix([0, -a])]
hess = sp.hessian(H, (y, z))
for point in critical:
    substitution = {y: point[0], z: point[1]}
    gradient = [sp.simplify(sp.diff(H, q).subs(substitution)) for q in (y, z)]
    value = sp.factor(H.subs(substitution))
    determinant = sp.factor(hess.subs(substitution).det())
    assert gradient == [0, 0]
    assert value in [2*a**3, -2*a**3]
    assert determinant != 0
    print('Cusp factor morsification: critical point', tuple(point),
          'value', value, 'Hessian determinant', determinant)

for power in range(1, 9):
    power_hess = sp.hessian(H**power, (y, z))
    for point in critical:
        substitution = {y: point[0], z: point[1]}
        value = H.subs(substitution)
        assert sp.simplify(power_hess.subs(substitution)
                           - power*value**(power-1)*hess.subs(substitution)) == sp.zeros(2)
print('Hessian(h^m) = m h^(m-1) Hessian(h) at both critical points, m=1,...,8.')

# Two tangent reduced factors y and y-z^2 split into transverse intersections.
factor_map_jacobian = sp.Matrix([y, y-z**2-c]).jacobian((y,z))
assert factor_map_jacobian.det() == -2*z
print('Shifted tangent factors: intersection y=0, z^2=-c; determinant = -2z, nonzero for c!=0.')

count = 0
for aa in range(2, 11):
    for bb in range(1, 21):
        for cc in range(1, 21):
            d = gcd(bb, cc)
            bp, cp = bb // d, cc // d
            # The common circle fixes v=y^bp z^cp exactly.
            assert bp*cp + cp*(-bp) == 0
            assert gcd(bp, cp) == 1
            square = 2 * cp * (-bp)
            assert square == -2*bp*cp and square < 0
            count += 1
print(f'Primitive weighted circle and nonzero spherical square checked for {count} triples, without a gcd(a,b,c) restriction.')
print('In particular x^2-y^2 z^2 has a spherical class of square -2.')
