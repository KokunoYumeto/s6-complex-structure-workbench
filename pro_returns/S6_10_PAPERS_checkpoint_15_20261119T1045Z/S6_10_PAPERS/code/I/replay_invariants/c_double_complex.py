#!/usr/bin/env python3
"""Exact independent checks for Part C. No geometric input is inferred.

Method 1 computes kernels/images of rational differential matrices.
Method 2 counts sources and sinks of the independently listed arrow summands.
Both methods are exact; there is no floating-point precision claim.
"""
from collections import Counter
import json
from pathlib import Path
import sympy as sp


def arrows(h):
    horizontal = [((0, 1), (1, 1), 1),
                  ((1, 1), (2, 1), h),
                  ((1, 2), (2, 2), h),
                  ((2, 2), (3, 2), 1)]
    vertical = [((a[1], a[0]), (b[1], b[0]), m)
                for a, b, m in horizontal]
    return horizontal + vertical


def matrix_method(h):
    nodes, edges = [], []
    for source, target, multiplicity in arrows(h):
        for _ in range(multiplicity):
            i = len(nodes)
            nodes.extend([source, target])
            edges.append((i, i + 1, source[0] != target[0]))
    nodes.extend([(0, 0), (3, 3)])
    # Add one acyclic square: a -> b, a -> c, b -> d, c -> -d.
    # This verifies, rather than presumes, its vanishing contribution.
    square_start = len(nodes)
    nodes.extend([(0, 0), (1, 0), (0, 1), (1, 1)])
    n = len(nodes)
    p, q = sp.zeros(n), sp.zeros(n)
    for source, target, is_horizontal in edges:
        (p if is_horizontal else q)[target, source] = 1
    a, b, c, d = range(square_start, square_start + 4)
    p[b, a], q[c, a], q[d, b], p[d, c] = 1, 1, 1, -1
    assert p*p == sp.zeros(n) and q*q == sp.zeros(n)
    assert p*q + q*p == sp.zeros(n)
    bc, ae, db = {}, {}, {}
    for x in range(4):
        for y in range(4):
            indices = [i for i, bidegree in enumerate(nodes) if bidegree == (x,y)]
            p_out, q_out = p[:,indices], q[:,indices]
            closed_rank = p_out.col_join(q_out).rank()
            bc[x,y] = len(indices) - closed_rank - (p*q)[indices,:].rank()
            ae[x,y] = len(indices) - (p*q)[:,indices].rank() - p[indices,:].row_join(q[indices,:]).rank()
            db[x,y] = len(indices) - q_out.rank() - q[indices,:].rank()
    return bc, ae, db


def counting_method(h):
    bc, ae = Counter({(0,0):1,(3,3):1}), Counter({(0,0):1,(3,3):1})
    db = Counter({(0,0):1,(3,3):1})
    for source, target, multiplicity in arrows(h):
        bc[target] += multiplicity
        ae[source] += multiplicity
        if source[1] == target[1]:
            db[source] += multiplicity
            db[target] += multiplicity
    return bc, ae, db


def rows(table):
    return [[int(table.get((p,q),0)) for p in range(4)] for q in [3,2,1,0]]


def totals(table):
    return [sum(int(v) for (p,q),v in table.items() if p+q == k) for k in range(7)]


def main():
    results = []
    for h in range(6):
        matrices = matrix_method(h)
        counts = counting_method(h)
        assert all(rows(a) == rows(b) for a,b in zip(matrices,counts))
        bc, ae, db = matrices
        bt, at = totals(bc), totals(ae)
        delta = [bt[k]+at[k]-2*(k in [0,6]) for k in range(7)]
        for p in range(4):
            for q in range(4):
                assert ae[p,q] == bc[3-p,3-q]
        results.append(dict(h=h, two_exact_methods_agree=True,
                            BC_rows_q_descending=rows(bc),
                            A_rows_q_descending=rows(ae),
                            Dolbeault_rows_q_descending=rows(db),
                            BC_totals=bt,A_totals=at,Delta=delta))
    print(json.dumps(results,indent=2))
    print('All calculations are over Q. No numerical approximation was used.')


if __name__ == '__main__':
    main()
