"""Fresh 02LT calculation: explicit orbit maps versus full integer cones.

No original/historical LT or LU computation is imported.
Finite tests supplement the all-parameter proof.  Every tested case checks
the actual integer equations before a summary is printed.
"""
from datetime import datetime, timezone
from itertools import combinations, product
from math import gcd
from functools import reduce

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


def gcd_all(values):
    return reduce(gcd, (abs(int(x)) for x in values), 0)


def bezout(a, b):
    """Return positive gcd and its signed Bezout coefficients."""
    aa, bb = abs(int(a)), abs(int(b))
    x0, x1, y0, y1 = 1, 0, 0, 1
    while bb:
        q, aa, bb = aa // bb, bb, aa % bb
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return aa, x0 * (-1 if a < 0 else 1), y0 * (-1 if b < 0 else 1)


def row_completion(row):
    """r V=(g,0,...); return V and the independently updated inverse."""
    r = sp.Matrix(1, len(row), list(row))
    n = r.cols
    V, W = sp.eye(n), sp.eye(n)
    for j in range(1, n):
        a, b = int((r * V)[0]), int((r * V)[j])
        if not a and not b:
            continue
        d, s, t = bezout(a, b)
        E, F = sp.eye(n), sp.eye(n)
        E[0, 0], E[0, j], E[j, 0], E[j, j] = s, -b // d, t, a // d
        F[0, 0], F[0, j], F[j, 0], F[j, j] = a // d, b // d, -t, s
        assert E * F == sp.eye(n) == F * E
        V, W = V * E, F * W
    if n and (r * V)[0] < 0:
        E = sp.eye(n)
        E[0, 0] = -1
        V, W = V * E, E * W
    assert V * W == sp.eye(n) == W * V
    g = gcd_all(row)
    assert r * V == sp.Matrix(1, n, [g] + [0] * (n - 1))
    return g, V, W


def kernel_row(row):
    g, V, W = row_completion(row)
    return (V[:, 1:], W[1:, :]) if g else (V, W)


def snf_values(M):
    D = smith_normal_form(M, domain=sp.ZZ)
    values = [abs(int(D[i, i])) for i in range(min(D.shape)) if D[i, i]]
    assert all(b % a == 0 for a, b in zip(values, values[1:]))
    return values


def cycles_of(p):
    unseen, cycles = set(range(len(p))), []
    while unseen:
        start = min(unseen)
        orbit, k = [], start
        while k not in orbit:
            orbit.append(k)
            unseen.remove(k)
            k = p[k]
        assert k == start
        cycles.append(orbit)
    return cycles


def perm_matrix(p):
    P = sp.zeros(len(p))
    for i, j in enumerate(p):
        P[j, i] = 1
    return P


def orbit_matrices(p):
    cycles = cycles_of(p)
    v, rho = len(p), len(cycles)
    R, S, I, K = sp.zeros(rho, v), sp.zeros(v, rho), sp.zeros(v, rho), sp.zeros(v)
    for j, orbit in enumerate(cycles):
        S[orbit[0], j] = 1
        for i in orbit:
            R[j, i], I[i, j] = 1, 1
        for k, i in enumerate(orbit[:-1]):
            for r in orbit[:k + 1]:
                K[i, r] = -1
    A = perm_matrix(p) - sp.eye(v)
    assert R * S == sp.eye(rho)
    assert A * K * (sp.eye(v) - S * R) == sp.eye(v) - S * R
    assert A * I == sp.zeros(v, rho) and R * A == sp.zeros(rho, v)
    return cycles, R, S, I, K


def graph_cartan(v, edges, weights=None):
    C = -2 * sp.eye(v)
    for i, j in edges:
        C[i, j] = C[j, i] = 1
    if weights:
        for (i, j), value in weights.items():
            C[i, j] = C[j, i] = value
    return C


def models():
    result = []

    def add(name, mu, p, C, B, cocycle, order):
        mu, P, q = sp.Matrix(mu), perm_matrix(p), sp.Matrix(cocycle)
        assert C * mu == sp.zeros(len(mu), 1)
        assert P * mu == mu and P.T * C * P == C
        assert P ** order == sp.eye(len(mu))
        assert all(P ** k != sp.eye(len(mu)) for k in range(1, order))
        result.append((name, mu, p, C, B, q, order))

    B2, B3, B4 = sp.Matrix([[0, -1], [1, 1]]), sp.Matrix([[0, -1], [1, 0]]), sp.Matrix([[0, -1], [1, -1]])
    add("II/q1", [1], [0], sp.zeros(1), B2, [0, 0], 1)
    for order, p in [(1, [0, 1]), (2, [1, 0])]:
        add("III/q" + str(order), [1, 1], p, sp.Matrix([[-2, 2], [2, -2]]), B3, [int(order > 1), 0], order)
    for order, p in [(1, [0, 1, 2]), (3, [1, 2, 0])]:
        add("IV/q" + str(order), [1, 1, 1], p, graph_cartan(3, [(0, 1), (1, 2), (2, 0)]), B4, [int(order > 1), 0], order)
    C6 = graph_cartan(7, [(0, 1), (0, 2), (0, 3), (1, 4), (2, 5), (3, 6)])
    for order, p in [(1, list(range(7))), (3, [0, 2, 3, 1, 5, 6, 4])]:
        add("IVstar/q" + str(order), [3, 2, 2, 2, 1, 1, 1], p, C6, B4.inv(), [int(order > 1), 0], order)
    C7 = graph_cartan(8, [(i, i + 1) for i in range(6)] + [(3, 7)])
    for order, p in [(1, list(range(8))), (2, [6, 5, 4, 3, 2, 1, 0, 7])]:
        add("IIIstar/q" + str(order), [1, 2, 3, 4, 3, 2, 1, 2], p, C7, B3.inv(), [int(order > 1), 0], order)
    for n in (1, 3):
        r = n + 4
        edges = [(0, 2), (1, 2)] + [(i, i + 1) for i in range(2, r - 2)] + [(r - 2, r - 1), (r - 2, r)]
        C = graph_cartan(r + 1, edges)
        mu = [1, 1] + [2] * (r - 3) + [1, 1]
        generator = list(range(r + 1))
        for a, b in zip([0, r - 1, 1, r], [r - 1, 1, r, 0]):
            generator[a] = b
        for i in range(2, r - 1):
            generator[i] = r - i
        p2 = [generator[generator[i]] for i in range(r + 1)]
        B = sp.Matrix([[-1, -n], [0, -1]])
        for order, p, q in [(1, list(range(r + 1)), [0, 0]), (2, p2, [0, 2]), (4, generator, [0, 1])]:
            add("I" + str(n) + "star/q" + str(order), mu, p, C, B, q, order)
    assert len(result) == 15
    return result


def degree_samples(weight):
    """All support<=2 signed kernel parameters, four scalings, two dense signs."""
    H, _ = kernel_row(weight)
    k = H.cols
    coefficients = set()
    for size in (1, 2):
        for support in combinations(range(k), size):
            for signs in product((-1, 1), repeat=size):
                a = [0] * k
                for i, s in zip(support, signs):
                    a[i] = s
                coefficients.add(tuple(a))
    if k:
        for a in (tuple([1] * k), tuple((-1) ** j for j in range(k))):
            coefficients.add(a)
            coefficients.add(tuple(-x for x in a))
    samples = {tuple([0] * len(weight))}
    for a in coefficients:
        for scale in (1, 2, 3, 5):
            samples.add(tuple(int(x) for x in scale * H * sp.Matrix(a)))
    return sorted(samples)


def check_case(mu, p, c_orbit):
    v = len(mu)
    cycles, R, S, I, K = orbit_matrices(p)
    rho, c_j = len(cycles), sp.Matrix(c_orbit)
    c = I * c_j
    A, zero = perm_matrix(p) - sp.eye(v), not any(c)
    assert c.T * A == sp.zeros(1, v) and (c.T * mu)[0] == 0
    g, V, W = row_completion(list(c))
    h = gcd_all([len(orbit) * int(c_j[j]) for j, orbit in enumerate(cycles)])
    assert zero == (g == 0) == (h == 0)
    assert zero or h % g == 0
    X, Xi = (V, W) if zero else (V[:, 1:], W[1:, :])
    assert Xi * X == sp.eye(X.cols)
    boundary = (Xi * A).col_join(c.T)
    diagonal = snf_values(boundary)
    free_h2 = X.cols + 1 - len(diagonal)
    tors_h2 = [a for a in diagonal if a > 1]
    assert free_h2 == rho + 1 if zero else free_h2 == rho - 1
    assert tors_h2 == ([] if h <= 1 else [h])
    assert snf_values(A) == [1] * (v - rho)
    H, Hi = kernel_row(c_orbit)
    cycle_basis = sp.diag(X, sp.ones(1))
    free_part = Hi * R * X
    scalar_part = -c.T * K * (sp.eye(v) - S * R) * X
    Phi = free_part.row_join(sp.zeros(H.cols, 1)).col_join(scalar_part.row_join(sp.ones(1)))
    Section = sp.diag(Xi * S * H, sp.ones(1))
    assert Phi * Section == sp.eye(H.cols + 1)
    QB = Phi * boundary
    assert QB[:-1, :] == sp.zeros(H.cols, v)
    assert gcd_all(QB[-1, :]) == h
    error = cycle_basis * (sp.eye(X.cols + 1) - Section * Phi)
    lift = K * error[:-1, :]
    assert A * lift == error[:-1, :] and c.T * lift == error[-1:, :]
    if h:
        values = [len(orbit) * int(c_j[j]) for j, orbit in enumerate(cycles)]
        hh, HV, _ = row_completion(values)
        eta = I * HV[:, 0]
        assert hh == h and A * eta == sp.zeros(v, 1) and (c.T * eta)[0] == h
        assert boundary * eta == sp.Matrix([0] * X.cols + [h])
        _, GV, _ = row_completion(list(c))
        assert (c.T * GV[:, 0])[0] == g
    q_Q = gcd_all(R * mu)
    w = R * mu / q_Q
    assert all(x.q == 1 for x in w) and gcd_all(w) == 1 and (c_j.T * w)[0] == 0
    wcoords = Hi * w
    assert H * wcoords == w and gcd_all(wcoords) == 1
    one, PV, PW = row_completion(list(wcoords))
    assert one == 1 and PW.T[:, 0] == wcoords
    image_basis, image_inverse = H * PW.T, PV.T * Hi
    assert image_inverse * image_basis == sp.eye(H.cols)
    assert image_basis[:, 0] == w
    complement = image_basis[:, 1:]
    assert complement.cols == (rho - 1 if zero else rho - 2)
    assert image_inverse[1:, :] * complement == sp.eye(complement.cols)
    return g, h, free_h2


def main():
    print("START", datetime.now(timezone.utc).isoformat())
    total, zero_count, nonzero_count, h_large, h_over_g, log_checks = 0, 0, 0, 0, 0, 0
    for name, mu, p, C, B, q, order in models():
        cycles, R, _, _, _ = orbit_matrices(p)
        assert gcd_all(R * mu) == order
        actual_h, count = set(), 0
        for c in degree_samples(list(R * mu)):
            g, h, _ = check_case(mu, p, c)
            count += 1
            total += 1
            zero_count += (g == 0)
            nonzero_count += (g > 0)
            h_large += (h > 1)
            h_over_g += (h > g > 0)
            actual_h.add(h)
        for sign in (-1, 1):
            for shift in ([0, 0], [1, 0], [0, 1], [-2, 3]):
                qq = sign * q + (B - sp.eye(2)) * sp.Matrix(shift)
                z = (B - sp.eye(2)).inv() * qq
                denominator = sp.ilcm(*(x.q for x in z))
                assert denominator == order
                row = [order, int(order * z[1]), int(-order * z[0])]
                assert gcd_all(row) == 1
                _, V, _ = row_completion(row)
                assert (sp.Matrix(1, 3, row) * V[:, 0])[0] == 1
                log_checks += 1
        print("PASS", name, "v", len(mu), "rho", len(cycles), "q", order,
              "cones", count, "h", ",".join(map(str, sorted(actual_h))))
    for n in (1, 3):
        r = n + 4
        edges = [(0, 2), (1, 2)] + [(i, i + 1) for i in range(2, r - 2)] + [(r - 2, r - 1), (r - 2, r)]
        C = graph_cartan(r + 1, edges)
        e0, e1 = sp.eye(r + 1)[:, 0], sp.eye(r + 1)[:, 1]
        degree = e1 - e0 + C * (-e0)
        p = [0, 1, r - 1, r] + list(range(2, r - 1))
        inverse = [p.index(i) for i in range(r + 1)]
        literal = [int(degree[i]) for i in p]
        assert literal == [1, 1, 0, 0, -1] + [0] * (r - 4)
        assert [p[inverse[i]] for i in range(r + 1)] == list(range(r + 1))
        perm = [1, 0, 3, 2] + list(range(4, r + 1))
        mu = sp.Matrix([1, 1, 1, 1] + [2] * (r - 3))
        orbits = cycles_of(perm)
        c_orbit = [literal[o[0]] for o in orbits]
        assert check_case(mu, perm, c_orbit)[:2] == (1, 1)
        print("PASS IC8", "I" + str(n) + "star", "new_to_old", p,
              "old_to_new", inverse, "degrees", literal, "g=h=1")
    print("PASS ALL", "cones", total, "zero", zero_count, "nonzero", nonzero_count,
          "h>1", h_large, "h>g", h_over_g, "logarithm_markings", log_checks)
    print("SCOPE full integer equations checked in every declared finite case;"
          " no manual reading of unprinted matrices is claimed.")
    print("END", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
