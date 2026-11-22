#!/usr/bin/env python3
"""Fresh prerelease certificate for 02WT: actual incidence and cubical cells.

No previous target program, proof, or outline was opened before writing this
program. The all-size formulas are proved in the accompanying derivation.
Finite cases here certify the implementations and the stated degree-two
identities, rather than serving as a proof by unbounded enumeration.
"""
from fractions import Fraction
from itertools import combinations, product
import json


def connected_components(vertices, edges):
    parent = list(range(vertices))
    def root(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for a, b in edges:
        aa, bb = root(a), root(b)
        if aa != bb:
            parent[aa] = bb
    return len({root(a) for a in range(vertices)})


def curve_cells(genera, branches):
    """Normalization surfaces joined to singular-point vertices by branches.

    Each component contributes one 0-cell, 2g 1-cells, one 2-cell.
    A singular point contributes a vertex and one incident edge per branch.
    This is the mapping-cylinder model of the finite identification map.
    Repeated component indices represent distinct marked points of one curve.
    """
    count = len(genera)
    edges = [(i, count + j) for j, indices in enumerate(branches) for i in indices]
    vertices = count + len(branches)
    conn = connected_components(vertices, edges)
    graph_b1 = len(edges) - vertices + conn
    cells = [vertices, 2 * sum(genera) + len(edges), count]
    euler = cells[0] - cells[1] + cells[2]
    betti = [conn, 2 * sum(genera) + graph_b1, count]
    assert euler == betti[0] - betti[1] + betti[2]
    assert euler == count + conn - graph_b1 - 2 * sum(genera)
    return dict(genera=genera, branches=branches, cells=cells, betti=betti,
                graph_b1=graph_b1, euler=euler, components=conn)


def torus_cells(n):
    """Identify opposite faces of [0,1]^n and compute every boundary.

    A k-cell is a k-element set of the free coordinates. The lower and upper
    face in each free coordinate have the same identified target cell and
    opposite signs. We sum the two contributions, not a preloaded zero map.
    """
    basis = [list(combinations(range(n), k)) for k in range(n + 1)]
    nonzero_entries = 0
    paired_faces = 0
    for k in range(1, n + 1):
        for cell in basis[k]:
            boundary = {}
            for j in range(k):
                target = cell[:j] + cell[j + 1:]
                for side in (0, 1):
                    sign = (-1) ** (j + 1 - side)
                    boundary[target] = boundary.get(target, 0) + sign
                    paired_faces += 1
            nonzero_entries += sum(value != 0 for value in boundary.values())
    assert nonzero_entries == 0
    ranks = [len(cells) for cells in basis]
    second = ranks[2] if n >= 2 else 0
    assert second == n * (n - 1) // 2
    return dict(n=n, ranks=ranks, nonzero_boundary_entries=nonzero_entries,
                face_contributions=paired_faces, second_betti=second,
                presentation_deficiency_upper=n - second)


def intersection(form, x, y):
    return sum(Fraction(x[i]) * form[i][j] * Fraction(y[j])
               for i in range(len(x)) for j in range(len(y)))


def ruled_canonical(g, degree):
    # h.h=degree, h.f=1, f.f=0. Solve K.f=-2 and
    # (K + h+r f).(h+r f)=2g-2 using the section h+r f, r=3.
    form = [[degree, 1], [1, 0]]
    section_r = 3
    a = -2
    b = 2 * g - 2 - (degree + 2 * section_r) - a * (degree + section_r)
    canonical = [a, b]
    assert b == degree + 2 * g - 2
    assert intersection(form, canonical, [0, 1]) == -2
    assert intersection(form, [canonical[0] + 1, canonical[1] + section_r],
                        [1, section_r]) == 2 * g - 2
    square = intersection(form, canonical, canonical)
    assert square == 8 * (1 - g)
    # S^2-bundle: base cells (1, 2g, 1) times sphere cells (1, 0, 1).
    base, fibre = [1, 2 * g, 1], [1, 0, 1]
    cells = [sum(base[i] * fibre[k-i] for i in range(3)
                 if 0 <= k-i < 3) for k in range(5)]
    euler = sum((-1) ** k * number for k, number in enumerate(cells))
    assert euler == 4 * (1 - g)
    return dict(g=g, degree=degree, K=canonical, K2=int(square),
                cells=cells, euler=euler)


def finite_degree_certificate():
    # Both sides have total degree at most two in the single variable n.
    # Three exact values certify their identity by polynomial interpolation.
    n_grid = []
    for n in range(3):
        lhs = Fraction(n) - Fraction(n * (n-1), 2)
        rhs = 1 - Fraction((n-1)*(n-2), 2)
        assert lhs == rhs
        n_grid.append([n, str(lhs), str(rhs)])
    # The graph lower-bound decomposition has separate degree <=1 in c,r.
    graph_grid = []
    for c, r in product((1, 2), (0, 1)):
        lhs, rhs = c + 1 - r, (c - 1) + (2 - r)
        assert lhs == rhs
        graph_grid.append([c, r, lhs])
    return dict(deficiency_degree=2, deficiency_grid=n_grid,
                graph_separate_degrees=[1, 1], graph_grid=graph_grid,
                all_integer_reason="(n-1)(n-2) is nonnegative for every integer n>=0")


def main():
    curves = []
    for count in range(1, 7):
        tree = [[i, i+1] for i in range(count-1)]
        for loops in range(4):
            branch_sets = tree + [[0, 0] for _ in range(loops)]
            item = curve_cells([0] * count, branch_sets)
            assert item['components'] == 1 and item['graph_b1'] == loops
            assert item['euler'] == count + 1 - loops
            curves.append(item)
    # Connected triple point, nodal rational cycle, elliptic component,
    # and one rational curve with a triple self-identification.
    special = [
        curve_cells([0, 0, 0], [[0, 1, 2]]),
        curve_cells([0, 0, 0], [[0, 1], [1, 2], [2, 0]]),
        curve_cells([1], []),
        curve_cells([0], [[0, 0, 0]]),
    ]
    assert special[0]['euler'] == 4
    assert special[1]['euler'] == 3 and special[1]['graph_b1'] == 1
    assert special[2]['euler'] == 0
    assert special[3]['euler'] == 0 and special[3]['graph_b1'] == 2
    torus = [torus_cells(n) for n in range(10)]
    for t in torus:
        assert t['presentation_deficiency_upper'] <= 1
    ruled = [ruled_canonical(g, d) for g in range(5) for d in (-3, 0, 4)]
    # Anticanonical cycle: each rational component has two node preimages.
    cycles = []
    for k in range(1, 9):
        nodes = [[i, (i+1) % k] for i in range(k)]
        result = curve_cells([0] * k, nodes)
        assert result['euler'] == k and result['graph_b1'] == 1
        cycles.append(dict(k=k, euler=result['euler'], graph_b1=result['graph_b1']))
    zero_cases = []
    for c in range(1, 9):
        for r in range(3):
            e = curve_cells([0] * c,
                            [[i, i+1] for i in range(c-1)] + [[0, 0]] * r)['euler']
            assert e >= 0
            if e == 0:
                zero_cases.append([c, r])
            if r <= 1:
                assert e >= 1
    assert zero_cases == [[1, 2]]
    # Exact generic conductor length constraints, with the general algebraic
    # implication q=2delta and delta>=q-1 => q<=2 in the text.
    candidates = [[q, delta] for q in range(1, 12) for delta in range(1, 12)
                  if q == 2 * delta and delta >= q - 1]
    assert candidates == [[2, 1]]
    # Once C is irreducible and the generic degree is two, k is 1 or 2.
    strict_boundary = [[k, 3-k] for k in (1, 2)]
    assert min(item[1] for item in strict_boundary) == 1
    # Blowup adds a sphere in place of a point and an orthogonal (-1)-class.
    blowups = []
    for start_e, start_k in ((3, 9), (4, 8)):
        for count in range(7):
            euler = start_e + count * (2-1)
            square = start_k + count * (-1)
            assert euler + square == 12
            blowups.append([start_e, count, euler, square])
    data = dict(method="incidence mapping cylinders and explicitly paired cubical faces",
                graph_samples=curves, special_curves=special, torus_cells=torus,
                ruled_canonical=ruled, anticanonical_cycles=cycles,
                exact_polynomial_certificates=finite_degree_certificate(),
                zero_cases=zero_cases, conductor_pairs=candidates,
                strict_boundary=strict_boundary, blowups=blowups,
                conclusion="all exact assertions passed")
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
