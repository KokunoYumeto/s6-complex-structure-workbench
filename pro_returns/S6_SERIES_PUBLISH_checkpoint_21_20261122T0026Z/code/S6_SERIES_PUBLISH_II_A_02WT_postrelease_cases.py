#!/usr/bin/env python3
"""Postrelease comparison of the printed minimal-surface and NC counts.

This program was first written after the target release. It receives no
additional independent-prereading credit. Branch incidence is specified in
each case; the actual graph cycle rank is obtained by a spanning-forest walk.
"""
from fractions import Fraction
import json


def incidence(genera, branches):
    c, s = len(genera), len(branches)
    adjacency = [[] for _ in range(c+s)]
    edges = 0
    for j, branch_set in enumerate(branches):
        for i in branch_set:
            adjacency[i].append(c+j)
            adjacency[c+j].append(i)
            edges += 1
    seen, components = set(), 0
    for start in range(c+s):
        if start in seen:
            continue
        components += 1
        stack = [start]
        while stack:
            v = stack.pop()
            if v in seen:
                continue
            seen.add(v)
            stack.extend(adjacency[v])
    cycles = edges-(c+s)+components
    euler = sum(2-2*g for g in genera)-sum(len(b)-1 for b in branches)
    return dict(c=c, singular_points=s, branches=edges, components=components,
                graph_cycles=cycles, normalization_genera=genera, euler=euler)


def main():
    specifications = [
        ('smooth elliptic cubic', [1], [], 'Z2'),
        ('nodal cubic', [0], [[0,0]], 'Z'),
        ('cuspidal cubic', [0], [[0]], 'trivial'),
        ('conic and line transverse', [0,0], [[0,1],[0,1]], 'Z'),
        ('conic and tangent line', [0,0], [[0,1]], 'trivial'),
        ('triangle of lines', [0,0,0], [[0,1],[1,2],[2,0]], 'Z'),
        ('three concurrent lines', [0,0,0], [[0,1,2]], 'trivial'),
        ('double line and another line', [0,0], [[0,1]], 'trivial'),
        ('triple line support', [0], [], 'trivial'),
        ('two sections with two intersection points', [0,0], [[0,1],[0,1]], 'Z'),
        ('two tangent sections', [0,0], [[0,1]], 'trivial'),
        ('two sections and one transverse fibre', [0,0,0], [[0,1],[0,2],[1,2]], 'Z'),
        ('fibre through section intersection', [0,0,0], [[0,1,2]], 'trivial'),
        ('disjoint sections and two fibres', [0,0,0,0], [[0,2],[1,2],[0,3],[1,3]], 'Z'),
        ('disjoint sections and one doubled fibre', [0,0,0], [[0,2],[1,2]], 'trivial'),
        ('bisection and fibre at two points', [0,0], [[0,1],[0,1]], 'Z'),
        ('bisection tangent to fibre', [0,0], [[0,1]], 'trivial'),
    ]
    cases = []
    for name, genera, branches, expected in specifications:
        data = incidence(genera, branches)
        assert data['components'] == 1
        actual = 'Z2' if genera == [1] and data['graph_cycles'] == 0 else (
            'Z' if data['graph_cycles'] == 1 else 'trivial')
        assert actual == expected
        cases.append(dict(name=name, expected=expected, **data))
    # A double section and v distinct vertical fibres: every fibre has one
    # reduced intersection point with the section. The incidence graph is a tree.
    trees = []
    for v in range(9):
        data = incidence([0]*(v+1), [[0,j] for j in range(1,v+1)])
        assert data['graph_cycles'] == 0 and data['euler'] == v+2
        trees.append(dict(vertical_fibres=v, **data))
    # Node blowup replaces one node by an exceptional P1 and two nodes.
    blowups = []
    for k in range(1,9):
        before = incidence([0]*k, [[i,(i+1)%k] for i in range(k)])
        remaining = [[i,(i+1)%k] for i in range(1,k)]
        after = incidence([0]*(k+1), remaining + [[0,k],[k,1%k]])
        assert before['graph_cycles'] == after['graph_cycles'] == 1
        assert after['euler'] == before['euler']+1
        blowups.append(dict(k=k, before=before, after=after))
    # Degree-two conductor map: over a smooth point two preimages; over a
    # triple point three preimages. Count the open stratum and point stratum.
    euler_transport = []
    for t in range(7):
        e_c = t
        open_c = e_c-t
        e_d = 2*open_c+3*t
        e_s = 6-e_d+e_c
        assert e_d == 3*t and e_s == 6-2*t
        euler_transport.append(dict(triple_points=t, eC=e_c, eD=e_d,
                                    eS_from_additivity=e_s,
                                    satisfies_divisor_identity=(e_s==t)))
    solutions = [x for x in euler_transport if x['satisfies_divisor_identity']]
    assert solutions == [dict(triple_points=2, eC=2, eD=6,
                             eS_from_additivity=2, satisfies_divisor_identity=True)]
    # Solve the three linear equalities without a black-box matrix solver:
    # d=3t; d=2c+t => c=t; 6-d+c=t => 6=3t.
    t=Fraction(6,3); c=t; d=3*t; e=6-d+c
    assert (t,c,d,e)==(2,2,6,2)
    print(json.dumps(dict(timing='postrelease', minimal_cases=cases,
                          double_section_trees=trees, node_blowups=blowups,
                          normal_crossing_transport=euler_transport,
                          exact_solution=dict(t=int(t),eC=int(c),eD=int(d),eS=int(e)),
                          conclusion='all exact assertions passed'),indent=2))


if __name__ == '__main__':
    main()
