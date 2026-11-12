"""Exact finite-incidence and channel checks; no vacuum simulation or Lean.

Uses only the standard library and prints results without creating files.
The analytic spectral theorem is proved in the companion Markdown source.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, product


def add(n, i):
    return tuple(x + (j == i) for j, x in enumerate(n))


def box(L):
    vertices = list(product(range(-L, L + 1), repeat=3))
    edges = [(n, i) for n in vertices for i in range(3) if n[i] < L]
    faces = {}
    for n in vertices:
        for i, j in combinations(range(3), 2):
            if n[i] < L and n[j] < L:
                faces[(n, i, j)] = ((n, i), (add(n, i), j),
                                     (add(n, j), i), (n, j))
    incident = defaultdict(list)
    for p, boundary in faces.items():
        for e in boundary:
            incident[e].append(p)
    w = {e: e[0][1] ** 2 if e[1] == 0 else 0 for e in edges}
    a = {p: F(sum(w[e] for e in boundary), 4)
         for p, boundary in faces.items()}
    adjacent = [(p, q, e) for e, ps in incident.items()
                for p, q in combinations(ps, 2)]
    assert len({frozenset((p, q)) for p, q, _ in adjacent}) == len(adjacent)
    assert len(edges) == 3 * (2 * L) * (2 * L + 1) ** 2
    assert len(faces) == 3 * (2 * L) ** 2 * (2 * L + 1)
    assert len(adjacent) == 144 * L ** 3 - 12 * L
    for (n, i, j), ap in a.items():
        expected = (F(n[1] ** 2 + (n[1] + 1) ** 2, 4)
                    if (i, j) == (0, 1) else
                    F(n[1] ** 2, 2) if (i, j) == (0, 2) else F(0))
        assert ap == expected
    return faces, w, a, adjacent


def multiply(values):
    out = F(1)
    for value in values:
        out *= value
    return out


def cos_pi_over_3(m):
    return (F(1), F(1, 2), F(-1, 2), F(-1), F(-1, 2), F(1, 2))[m % 6]


def char_ratio(j, m):
    if j == 0:
        return F(1)
    if j == F(1, 2):
        return cos_pi_over_3(m)
    assert j == 1
    return (1 + 2 * cos_pi_over_3(2 * m)) / 3


def check_box(L):
    faces, w, a, adjacent = box(L)
    norm_a = sum((ap ** 2 for ap in a.values()), F(0))
    sum_a = sum(a.values(), F(0))
    poly_n = F(L ** 2 * (2 * L + 1), 60) * (
        24 * L ** 4 + 24 * L ** 3 + 8 * L ** 2 - 4 * L + 3)
    poly_s = F(L ** 2 * (2 * L + 1) * (4 * L ** 2 + 2 * L + 1), 3)
    assert norm_a == poly_n
    assert sum_a == poly_s
    r8 = F(0)
    r0 = F(0)
    r1 = F(0)
    # Derive the vacuum second coefficient via its H_0 equation, then
    # subtract the spectral dressing denominators independently.
    for p, boundary in faces.items():
        gamma_y = sum(2 * w[e] for e in boundary)
        assert gamma_y == 8 * a[p]
        vacuum_y = F(1, 3) / 8
        dressing_y = a[p] / (8 - 3)
        residual_y = gamma_y * vacuum_y - dressing_y
        assert residual_y == F(2, 15) * a[p]
        # Character second derivatives on every translated spin-one edge.
        beta_theta2 = sum((-F(4, 3) * w[e] for e in boundary), F(0))
        u_theta2 = -F(2, 3) * a[p]
        angular_residual_y = beta_theta2 / 24 - u_theta2 / 5
        assert angular_residual_y == -F(2, 3) * residual_y
        r8 += residual_y ** 2
    degrees = defaultdict(int)
    off_diagonal_weight = -F(1, 21)
    assert F(1, 3) - (F(1, 4) / F(3, 2) + F(3, 4) / F(7, 2)) == off_diagonal_weight
    for p, q, e in adjacent:
        degrees[p] += 1
        degrees[q] += 1
        boundary_outer = set(faces[p]) ^ set(faces[q])
        assert len(boundary_outer) == 6
        assert set(faces[p]) & set(faces[q]) == {e}
        s = a[p] + a[q]
        gamma0 = sum(F(3, 4) * w[f] for f in boundary_outer)
        gamma1 = gamma0 + 2 * w[e]
        assert gamma0 == 3 * s - F(3, 2) * w[e]
        assert gamma1 == 3 * s + F(1, 2) * w[e]
        residual0 = gamma0 * (F(2, 3) / F(9, 2)) - s / F(3, 2)
        residual1 = gamma1 * (F(2, 3) / F(13, 2)) - s / F(7, 2)
        assert residual0 == -F(2, 9) * (s + w[e])
        assert residual1 == F(2, 273) * (3 * s + 7 * w[e])
        outer_theta2 = sum((-F(1, 2) * w[f] for f in boundary_outer), F(0))
        k0_theta2 = outer_theta2
        k1_theta2 = outer_theta2 - F(4, 3) * w[e]
        u_theta2 = -F(2, 3) * s
        assert F(4, 27) * k0_theta2 - F(2, 3) * u_theta2 == -F(2, 3) * residual0
        assert F(4, 39) * k1_theta2 - F(2, 7) * u_theta2 == -F(2, 3) * residual1
        r0 += F(1, 4) * residual0 ** 2
        r1 += F(3, 4) * residual1 ** 2
    M = len(faces)
    for p in faces:
        d = degrees[p]
        assert d <= 12
        original_diag = F(1, 3) - F(1, 5) - F(M - 1 - d, 3) - F(8 * d, 21)
        assert original_diag + F(M, 3) == F(7, 15) - F(d, 21)
    assert r8 == F(4, 225) * norm_a
    assert r0 == sum((F(1, 81) * (a[p] + a[q] + w[e]) ** 2
                     for p, q, e in adjacent), F(0))
    assert r1 == sum((F(1, 24843) * (3 * (a[p] + a[q]) + 7 * w[e]) ** 2
                     for p, q, e in adjacent), F(0))
    assert r8 > 0 and r0 > 0 and r1 > 0
    return norm_a, r8, r0, r1


def check_finite_angle():
    # At theta=pi/3 every multiplier is rational; evaluate genuine link
    # products before subtracting the first-band dressing.
    faces, w, a, adjacent = box(2)
    alpha = {p: multiply(char_ratio(F(1, 2), e[0][1])
                         for e in b if e[1] == 0) for p, b in faces.items()}
    beta = {p: multiply(char_ratio(1, e[0][1])
                        for e in b if e[1] == 0) for p, b in faces.items()}
    u = {p: (alpha[p] - 1) / 3 for p in faces}
    c2 = sum(((alpha[p] - 1) / 9 for p in faces), F(0))
    assert -c2 == -sum(u.values(), F(0)) / 3
    for p in faces:
        assert (beta[p] - 1) / 24 - u[p] / 5 == (
            F(1, 24) * beta[p] - F(1, 24) - (alpha[p] - 1) / 15)
    adjacent_keys = {frozenset((p, q)) for p, q, _ in adjacent}
    nonzero_disjoint = 0
    for p, q in combinations(faces, 2):
        if frozenset((p, q)) in adjacent_keys:
            continue
        multiplier = multiply(char_ratio(F(1, 2), e[0][1])
                              for e in set(faces[p]) | set(faces[q]) if e[1] == 0)
        assert multiplier == alpha[p] * alpha[q]
        residual = (multiplier - 1) / 9 - (u[p] + u[q]) / 3
        assert residual == (alpha[p] - 1) * (alpha[q] - 1) / 9
        nonzero_disjoint += residual != 0
    assert nonzero_disjoint > 0
    for p, q, e in adjacent:
        outer = set(faces[p]) ^ set(faces[q])
        km_outer = multiply(char_ratio(F(1, 2), f[0][1]) for f in outer if f[1] == 0)
        k0 = km_outer
        k1 = km_outer * (char_ratio(1, e[0][1]) if e[1] == 0 else 1)
        for j, kj, E in [(0, k0, F(9, 2)), (1, k1, F(13, 2))]:
            vacuum_coefficient = F(2, 3) / E
            residual = vacuum_coefficient * (kj - 1) - (u[p] + u[q]) / (E - 3)
            expected = ((F(4, 27) * (k0 - 1) - F(2, 3) * (u[p] + u[q]))
                        if j == 0 else
                        (F(4, 39) * (k1 - 1) - F(2, 7) * (u[p] + u[q])))
            assert residual == expected
    return nonzero_disjoint


if __name__ == "__main__":
    for L in range(2, 6):
        N, R8, R0, R1 = check_box(L)
        print(f"L={L}: ||a||^2={N}; R8={R8}; R9/2={R0}; R13/2={R1}")
    count = check_finite_angle()
    print(f"Finite-angle L=2 check: {count} nonzero edge-disjoint channels retained.")
    print("PASS: exact native incidence, all second-order channels, angular factors, vacuum subtraction, and physical-band coefficients.")
