"""Exact finite-box incidence, kernel, and second-vacuum-mode diagnostics.

No vacuum sampling, floating point, or continuum approximation is used.
"""

from fractions import Fraction as F
from itertools import combinations, product


def plus(n, i):
    out = list(n)
    out[i] += 1
    return tuple(out)


def boundary(p):
    n, i, j = p
    return frozenset(((n, i), (plus(n, i), j), (plus(n, j), i), (n, j)))


def sign(n):
    return -1 if sum(n) % 2 else 1


def kernel_values(L, f_values, phi_values):
    def potential(i, j, x, y):
        return phi_values.get((i, j, x, y), 0)

    out = {}
    for n in product(range(-L, L + 1), repeat=3):
        for i in range(3):
            if n[i] == L:
                continue
            value = f_values.get((i, n[i]), 0)
            for j in range(i + 1, 3):
                value += potential(i, j, n[i] + 1, n[j]) - potential(i, j, n[i], n[j])
            for j in range(i):
                value -= potential(j, i, n[j], n[i] + 1) - potential(j, i, n[j], n[i])
            out[n, i] = sign(n)*value
    return out


for L in (2, 3, 4):
    vertices = list(product(range(-L, L + 1), repeat=3))
    edges = [(n, i) for n in vertices for i in range(3) if n[i] < L]
    faces = [(n, i, j) for n in vertices for i, j in combinations(range(3), 2)
             if n[i] < L and n[j] < L]
    assert len(edges) == 3*(2*L)*(2*L+1)**2
    assert len(faces) == 3*(2*L)**2*(2*L+1)
    star = {e: [] for e in edges}
    for face in faces:
        for edge in boundary(face):
            star[edge].append(face)
    assert all(2 <= len(p) <= 4 for p in star.values())

    # An adjacent unordered pair has a unique shared edge and outer boundary.
    outer_supports = {}
    adjacent_pairs = []
    for edge, incident in star.items():
        for p, q in combinations(incident, 2):
            assert boundary(p) & boundary(q) == {edge}
            outer = (boundary(p) | boundary(q)) - {edge}
            assert len(outer) == 6
            assert outer not in outer_supports
            outer_supports[outer] = (edge, p, q)
            adjacent_pairs.append((edge, p, q))
    count_one_direction = 48*L**3-4*L
    assert len(adjacent_pairs) == 3*count_one_direction

    alternating = {(n, i): (-1 if (n[1]+n[2]) % 2 else 1) if i == 0 else 0
                   for n, i in edges}
    native = {(n, i): n[1]**2 if i == 0 else 0 for n, i in edges}
    face_sums_alt = {p: sum(alternating[e] for e in boundary(p)) for p in faces}
    assert all(value == 0 for value in face_sums_alt.values())
    weighted_pair_norm = sum(
        len(star[e])*(len(star[e])-1)//2 * alternating[e]**2 for e in edges
    )
    assert weighted_pair_norm == count_one_direction
    native_squared_face_sums = sum(sum(native[e] for e in boundary(p))**2 for p in faces)
    angular_poly = F(L*L*(2*L+1)*(24*L**4+24*L**3+8*L*L-4*L+3), 15)
    assert native_squared_face_sums == 4*angular_poly

    f_parameters = {(i, x): (i+1)*(x+L+1)**2
                    for i in range(3) for x in range(-L, L)}
    phi_parameters = {(i, j, x, y): (x+L)*(y+L)*((i+1)*x+(j+2)*y+x*y)
                      for i, j in combinations(range(3), 2)
                      for x in range(-L+1, L+1) for y in range(-L+1, L+1)}
    weights = kernel_values(L, f_parameters, phi_parameters)
    assert all(sum(weights[e] for e in boundary(p)) == 0 for p in faces)
    for edge, p, q in adjacent_pairs:
        outer = (boundary(p) | boundary(q)) - {edge}
        weighted_outer_sum = sum(weights[f] for f in outer)
        assert weighted_outer_sum == -2*weights[edge]
        assert F(3, 4)*weighted_outer_sum == -F(3, 2)*weights[edge]
        assert F(3, 4)*weighted_outer_sum+2*weights[edge] == F(1, 2)*weights[edge]
    for n, i, j in faces:
        central_sign = lambda x, k: -1 if sum(x[:k]) % 2 else 1
        assert (
            central_sign(n, i)*central_sign(plus(n, i), j)
            *central_sign(plus(n, j), i)*central_sign(n, j)
        ) == -1
    # Reconstruct the independent anchored parameters from the edge field.
    def a_value(n, i):
        return sign(n)*weights[n, i]
    for (i, x), expected in f_parameters.items():
        n = [-L, -L, -L]
        n[i] = x
        assert a_value(tuple(n), i) == expected
    for (i, j, x, y), expected in phi_parameters.items():
        total = 0
        for r in range(-L, x):
            n = [-L, -L, -L]
            n[i], n[j] = r, y
            total += a_value(tuple(n), i)-f_parameters[i, r]
        assert total == expected
    kernel_dimension = len(f_parameters)+len(phi_parameters)
    assert kernel_dimension == 3*(2*L)*(2*L+1)
    assert len(edges)-kernel_dimension == len(faces)

    # Verify every anchored coordinate basis vector in one whole box.
    if L == 2:
        for key in f_parameters:
            basis = kernel_values(L, {key: 1}, {})
            assert all(sum(basis[e] for e in boundary(p)) == 0 for p in faces)
        for key in phi_parameters:
            basis = kernel_values(L, {}, {key: 1})
            assert all(sum(basis[e] for e in boundary(p)) == 0 for p in faces)
    print(f"L={L}: {len(edges)} links, {len(faces)} faces, "
          f"kernel dimension {kernel_dimension}, {len(adjacent_pairs)} distinct pair modes.")

# Vacuum and mode coefficients use the original -2 tr metric.
assert F(1, 3)*F(3, 4) == F(1, 4)
assert F(3, 4)/9 == F(1, 12)
lambda_r, lambda_d = F(9, 2), F(13, 2)
vacuum_r = F(2, 3)*F(1, 2)/lambda_r
vacuum_d = F(2, 3)/lambda_d
assert vacuum_r == F(2, 27)
assert vacuum_d == F(4, 39)
state_r, state_d = vacuum_r*(-F(3, 2)), vacuum_d*F(1, 2)
assert state_r == -F(1, 9)
assert state_d == F(2, 39)
norm_coefficient = state_r**2 + F(3, 4)*state_d**2
energy_coefficient = lambda_r*state_r**2 + lambda_d*F(3, 4)*state_d**2
assert norm_coefficient == F(196, 13689)
assert energy_coefficient == F(8, 117)
assert energy_coefficient/norm_coefficient == F(234, 49)
positive_kernel_difference = energy_coefficient-3*norm_coefficient
assert positive_kernel_difference == F(348, 13689) == F(116, 4563)
print("PASS: full kernel parametrization/reconstruction, all L=2 kernel basis vectors,")
print("distinct pair supports, alternating/native weights, and all exact state coefficients.")
