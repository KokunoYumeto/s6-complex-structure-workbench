"""Exact low-resource open-box maximal-tree audit; standard library only.

Build d0, d1 and the root path integrals independently from vertices, edges,
faces and the specified first-positive-coordinate parent rule. Matrix products
use integers; rank reduction uses fractions.Fraction. No numerical eigensolver,
symbolic radical eigensolve, Lean, subprocess, network or file writes occur.
The JSON report is printed to stdout for review and durable recording.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial
import json
import time


def zeros(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    out = zeros(len(a), len(b[0]))
    nonzero_b = [[(j, x) for j, x in enumerate(row) if x] for row in b]
    for i, row in enumerate(a):
        for k, value in enumerate(row):
            if value:
                for j, other in nonzero_b[k]:
                    out[i][j] += value * other
    return out


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def is_zero(a):
    return all(value == 0 for row in a for value in row)


def rank(a):
    basis = {}
    for raw_row in a:
        row = {i: Fraction(v) for i, v in enumerate(raw_row) if v}
        while row:
            pivot = min(row)
            if pivot not in basis:
                divisor = row[pivot]
                basis[pivot] = {j: v / divisor for j, v in row.items()}
                break
            scale = row[pivot]
            for j, value in basis[pivot].items():
                new_value = row.get(j, 0) - scale * value
                if new_value:
                    row[j] = new_value
                else:
                    row.pop(j, None)
    return len(basis)


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def moments(a, degree):
    result = [len(a)]
    power = identity(len(a))
    for _ in range(degree):
        power = multiply(power, a)
        result.append(trace(power))
    return result


def scalar_shift(a, value):
    b = [row[:] for row in a]
    for i in range(len(a)):
        b[i][i] -= value
    return b


def step(vertex, coordinate, amount=1):
    return tuple(x + (amount if i == coordinate else 0)
                 for i, x in enumerate(vertex))


def interval_data(m, degree):
    d = zeros(m, m + 1)
    for i in range(m):
        d[i][i], d[i][i + 1] = -1, 1
    a, b = multiply(transpose(d), d), multiply(d, transpose(d))
    return moments(a, degree), moments(b, degree)


def triple_sum_moment(left, middle, right, degree):
    total = 0
    for i in range(degree + 1):
        for j in range(degree - i + 1):
            k = degree - i - j
            coefficient = factorial(degree) // (
                factorial(i) * factorial(j) * factorial(k))
            total += coefficient * left[i] * middle[j] * right[k]
    return total


def one_box(m):
    vertices = list(product(range(m + 1), repeat=3))
    vertex_index = {v: i for i, v in enumerate(vertices)}
    edges = [(v, i) for v in vertices for i in range(3) if v[i] < m]
    edge_index = {e: i for i, e in enumerate(edges)}
    faces = [(v, i, j) for v in vertices for i in range(3)
             for j in range(i + 1, 3) if v[i] < m and v[j] < m]
    d0 = zeros(len(edges), len(vertices))
    for row, (v, i) in enumerate(edges):
        d0[row][vertex_index[v]] = -1
        d0[row][vertex_index[step(v, i)]] = 1
    d1 = zeros(len(faces), len(edges))
    for row, (v, i, j) in enumerate(faces):
        for edge, sign in [((v, i), 1), ((step(v, i), j), 1),
                           ((step(v, j), i), -1), ((v, j), -1)]:
            d1[row][edge_index[edge]] += sign

    root = (0, 0, 0)
    parents = {}
    tree_indices = set()
    for v in vertices:
        if v != root:
            i = next(i for i in range(3) if v[i] > 0)
            parent = step(v, i, -1)
            edge = edge_index[(parent, i)]
            parents[v] = (parent, edge)
            tree_indices.add(edge)
    chord_indices = [i for i in range(len(edges)) if i not in tree_indices]
    path = zeros(len(vertices), len(edges))
    for v in vertices:
        current = v
        while current != root:
            current, edge = parents[current]
            path[vertex_index[v]][edge] += 1

    t = []
    j = zeros(len(edges), len(chord_indices))
    for chord, edge_number in enumerate(chord_indices):
        v, direction = edges[edge_number]
        source = path[vertex_index[v]]
        target = path[vertex_index[step(v, direction)]]
        row = [a - b for a, b in zip(source, target)]
        row[edge_number] += 1
        t.append(row)
        j[edge_number][chord] = 1
    c = multiply(d1, j)
    g = multiply(t, transpose(t))
    curl_laplacian = multiply(transpose(d1), d1)
    quotient_matrix = multiply(multiply(transpose(c), c), g)

    identities = {
        "d1_d0_zero": is_zero(multiply(d1, d0)),
        "T_d0_zero": is_zero(multiply(t, d0)),
        "T_j_identity": multiply(t, j) == identity(len(chord_indices)),
        "d1_equals_C_T": d1 == multiply(c, t),
    }
    ranks = {"d0": rank(d0), "d1": rank(d1), "T": rank(t),
             "C": rank(c), "G": rank(g)}
    r = len(chord_indices)
    identities.update({
        "rank_d0_equals_V_minus_1": ranks["d0"] == len(vertices) - 1,
        "rank_d1_equals_chord_count": ranks["d1"] == r,
        "ker_d1_equals_im_d0_by_containment_and_dimension":
            identities["d1_d0_zero"] and len(edges) - ranks["d1"] == ranks["d0"],
        "ker_T_equals_im_d0_by_containment_and_dimension":
            identities["T_d0_zero"] and len(edges) - ranks["T"] == ranks["d0"],
        "C_injective": ranks["C"] == r,
        "G_positive_definite_via_T_rank": ranks["T"] == ranks["G"] == r,
    })

    degree = 4
    edge_moments = moments(curl_laplacian, degree)[1:]
    tree_moments = moments(quotient_matrix, degree)[1:]
    interval_a, interval_b = interval_data(m, degree)
    tensor_moments = []
    for q in range(1, degree + 1):
        # Tr(Delta_1^q) - Tr(Delta_0^q), with 3 coordinate summands.
        # This derives from actual one-dimensional incidence matrices.
        tensor_moments.append(
            3 * triple_sum_moment(interval_b, interval_a, interval_a, q)
            - triple_sum_moment(interval_a, interval_a, interval_a, q))
    identities["four_exact_trace_moments_match"] = (
        edge_moments == tree_moments == tensor_moments)
    by_k = Counter()
    for indices in product(range(m + 1), repeat=3):
        k = sum(value > 0 for value in indices)
        if k >= 2:
            by_k[k] += k - 1
    identities["tensor_multiplicity_equals_chord_count"] = sum(by_k.values()) == r

    exact_spectrum = None
    if m in (1, 2):
        # The independent interval matrices have exact rational spectra
        # {0,2} and {0,1,3}. Verify every eigenspace dimension, then derive
        # tensor sums. No sine-formula values are copied into this check.
        d = zeros(m, m + 1)
        for i in range(m):
            d[i][i], d[i][i + 1] = -1, 1
        interval_laplacian = multiply(transpose(d), d)
        interval_spectrum = [0, 2] if m == 1 else [0, 1, 3]
        interval_nullities = {
            eigenvalue: len(interval_laplacian)
            - rank(scalar_shift(interval_laplacian, eigenvalue))
            for eigenvalue in interval_spectrum}
        identities["interval_rational_eigenspaces_complete"] = (
            all(value == 1 for value in interval_nullities.values()))
        predicted = Counter()
        for eigenvalues in product(interval_spectrum, repeat=3):
            k = sum(value > 0 for value in eigenvalues)
            if k >= 2:
                predicted[sum(eigenvalues)] += k - 1
        edge_nullities = {
            eigenvalue: len(curl_laplacian)
            - rank(scalar_shift(curl_laplacian, eigenvalue))
            for eigenvalue in sorted(predicted)}
        tree_nullities = {
            eigenvalue: r - rank(scalar_shift(quotient_matrix, eigenvalue))
            for eigenvalue in sorted(predicted)}
        identities["complete_positive_spectrum_by_exact_nullities"] = (
            edge_nullities == tree_nullities == dict(predicted)
            and sum(predicted.values()) == r)
        exact_spectrum = {
            "squared_frequency_multiplicities": dict(sorted(predicted.items())),
            "edge_matrix_eigenspace_dimensions": edge_nullities,
            "tree_matrix_eigenspace_dimensions": tree_nullities,
            "interval_matrix_eigenspace_dimensions": interval_nullities,
        }

    assert all(identities.values()), (m, identities)
    return {
        "m": m,
        "vertices": len(vertices), "edges": len(edges), "faces": len(faces),
        "tree_edges": len(tree_indices), "chords": r,
        "ranks_over_Q": ranks,
        "kernel_dimensions": {"d1": len(edges) - ranks["d1"],
                              "T": len(edges) - ranks["T"],
                              "d0_star": len(edges) - ranks["d0"]},
        "identities": identities,
        "trace_powers_1_to_4": {"original_d1_star_d1": edge_moments,
                                 "tree_C_star_C_G": tree_moments,
                                 "interval_tensor_formula": tensor_moments},
        "tensor_multiplicity_by_positive_coordinate_count": dict(by_k),
        "complete_exact_positive_spectrum": exact_spectrum,
    }


if __name__ == "__main__":
    started = time.monotonic()
    boxes = [one_box(m) for m in (1, 2, 3)]
    report = {
        "status": "PASS",
        "arithmetic": "Exact integers and fractions.Fraction; standard library only",
        "coordinates": "l=n+L, m=2L when m is even; odd m are auxiliary open-box checks",
        "checks_do_not_claim": ["a proof for all m by finite testing",
                                "actual nonlinear spectral eigenvalue computation",
                                "uniform-in-volume convergence or an interacting continuum limit"],
        "boxes": boxes,
        "elapsed_seconds": round(time.monotonic() - started, 6),
    }
    print(json.dumps(report, indent=2, sort_keys=True))
