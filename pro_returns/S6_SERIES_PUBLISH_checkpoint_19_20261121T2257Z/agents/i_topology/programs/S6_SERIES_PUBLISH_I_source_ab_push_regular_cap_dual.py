#!/usr/bin/env python3
"""Exact incidence and elementary-collapse certificate for B.4.16.

The analytic identification of the vertices and triangles is proved in the
text.  This script certifies the resulting finite integral chain complex.
"""
import itertools
import json
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def parity_triangle_complex(n):
    assert n >= 4 and n % 2 == 0
    # H_i=i; V_i=n+i.  The diagonal always joins V_even to H_odd.
    triangles = []
    top_pairs = []
    lower_pairs = []
    for i in range(n):
        j = (i + 1) % n
        even, odd = (i, j) if i % 2 == 0 else (j, i)
        top = tuple(sorted((n + even, n + odd, odd)))
        lower = tuple(sorted((n + even, even, odd)))
        triangles.extend((top, lower))
        top_pairs.append((top, tuple(sorted((n + i, n + j)))))
        lower_pairs.append((lower, tuple(sorted((n + even, odd)))))
    edges = sorted({e for t in triangles for e in itertools.combinations(t, 2)})
    vertices = [(i,) for i in range(2 * n)]
    d1 = sp.zeros(2 * n, len(edges))
    for k, (a, b) in enumerate(edges):
        d1[a, k], d1[b, k] = -1, 1
    d2 = sp.zeros(len(edges), len(triangles))
    edge_index = {e: k for k, e in enumerate(edges)}
    for k, t in enumerate(triangles):
        for ell in range(3):
            e = t[:ell] + t[ell + 1:]
            d2[edge_index[e], k] = (-1) ** ell
    assert d1 * d2 == sp.zeros(2 * n, len(triangles))

    # Retraction to the old horizontal cycle, at the level of chains.
    old_edges = sorted({tuple(sorted((i, (i + 1) % n))) for i in range(n)})
    old_index = {e: k for k, e in enumerate(old_edges)}
    old_d1 = sp.zeros(n, n)
    for k, (a, b) in enumerate(old_edges):
        old_d1[a, k], old_d1[b, k] = -1, 1
    retract0 = sp.zeros(n, 2 * n)
    for v in range(2 * n):
        retract0[v % n, v] = 1
    retract1 = sp.zeros(n, len(edges))
    for k, (a, b) in enumerate(edges):
        ia, ib = a % n, b % n
        if ia == ib:
            continue
        e = tuple(sorted((ia, ib)))
        retract1[old_index[e], k] = 1 if ia < ib else -1
    assert old_d1 * retract1 == retract0 * d1
    assert retract1 * d2 == sp.zeros(n, 2 * n)

    # A literal elementary-collapse sequence, not just a Betti calculation.
    simplices = set(vertices) | set(edges) | set(triangles)
    collapses = []
    for maximal, free_face in top_pairs + lower_pairs:
        assert maximal in simplices and free_face in simplices
        containing = [s for s in simplices if len(s) > len(free_face)
                      and set(free_face).issubset(s)]
        assert containing == [maximal]
        simplices.remove(maximal)
        simplices.remove(free_face)
        collapses.append([list(maximal), list(free_face)])
    for i in range(n):
        edge, vertex = tuple(sorted((i, n + i))), (n + i,)
        assert edge in simplices and vertex in simplices
        containing = [s for s in simplices if len(s) > 1 and n + i in s]
        assert containing == [edge]
        simplices.remove(edge)
        simplices.remove(vertex)
        collapses.append([list(edge), list(vertex)])
    assert simplices == {(i,) for i in range(n)} | set(old_edges)

    # The old cycle has winding one under an integral cocycle.
    cycle = sp.zeros(n, 1)
    for i in range(n):
        j = (i + 1) % n
        cycle[old_index[tuple(sorted((i, j)))], 0] = 1 if i < j else -1
    assert old_d1 * cycle == sp.zeros(n, 1)
    cut = sp.zeros(1, n)
    cut[0, old_index[(0, n - 1)]] = -1
    alpha = cut * retract1
    assert alpha * d2 == sp.zeros(1, 2 * n)
    assert (cut * cycle)[0] == 1

    sf1 = smith_normal_form(d1, domain=ZZ)
    sf2 = smith_normal_form(d2, domain=ZZ)
    snf1 = [abs(int(sf1[i, i])) for i in range(min(sf1.shape)) if sf1[i, i]]
    snf2 = [abs(int(sf2[i, i])) for i in range(min(sf2.shape)) if sf2[i, i]]
    assert snf1 == [1] * (2 * n - 1)
    assert snf2 == [1] * (2 * n)
    return {
        'n': n, 'f_vector': [2 * n, 4 * n, 2 * n],
        'integral_homology': ['Z', 'Z', '0'],
        'd1_nonzero_smith': snf1, 'd2_nonzero_smith': snf2,
        'collapse_count': len(collapses), 'collapses': collapses,
        'retraction_is_chain_map': True, 'angular_cocycle_winding': 1,
        'triangles': [list(t) for t in triangles],
    }


out = {'status': 'PASS', 'scope': 'B.4.15 local insertions and the specified generated operations only',
       'certificates': [parity_triangle_complex(n) for n in (4, 6, 12, 24)]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
