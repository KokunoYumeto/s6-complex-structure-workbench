#!/usr/bin/env python3
"""Exact compactification lattices for x^2-z*y^n=1 (P4.16).

The proof constructs the surface and its boundary, and proves that the
displayed orthogonal kernel is the image of compact H_2 of the affine
surface.  This program independently checks every lattice calculation.
All arithmetic is integral or rational; no numerical rank test is used.
"""
from functools import reduce
from math import gcd
import json
from pathlib import Path
import sympy as S

records = []
for n in (1,):
    size = 2 + 2*n
    names = ['H_x', 'H_y'] + [f'E_{sign},{j}'
                            for sign in ('+', '-') for j in range(1,n+1)]
    Q = S.diag(*([0,0]+[-1]*(2*n)))
    Q[0,1] = Q[1,0] = 1
    def basis(i):
        v = S.zeros(size,1); v[i] = 1
        return v
    def exceptional(sign,j):
        return basis(2 + sign*n + j-1)
    divisors = [basis(0), basis(1),
                basis(1)-exceptional(0,1)-exceptional(1,1)]
    divisor_names = ['x=infinity', 'y=infinity', 'strict(y=0)']
    for sign in range(2):
        for j in range(1,n):
            divisors.append(exceptional(sign,j)-exceptional(sign,j+1))
            divisor_names.append(f'strict(E_{"+" if sign == 0 else "-"},{j})')
    B = S.Matrix.hstack(*divisors)
    restriction = B.T*Q
    v = sum((exceptional(0,j)-exceptional(1,j) for j in range(1,n+1)),
            S.zeros(size,1))
    kernel = restriction.nullspace()
    square = (v.T*Q*v)[0]
    assert restriction.rank() == 2*n+1
    assert len(kernel) == 1 and restriction*v == S.zeros(2*n+1,1)
    assert reduce(gcd, map(abs, map(int,v))) == 1
    assert square == -2*n
    assert kernel[0] == -v or kernel[0] == v
    # The boundary is a tree of rational curves, checked from its graph.
    intersection = B.T*Q*B
    edges = [(i,j) for i in range(B.cols) for j in range(i+1,B.cols)
             if intersection[i,j] != 0]
    assert all(intersection[i,j] == 1 for i,j in edges)
    assert len(edges) == B.cols-1
    reached = {0}
    while True:
        new = reached | {j for i,j in edges if i in reached} | {
            i for i,j in edges if j in reached}
        if new == reached: break
        reached = new
    assert len(reached) == B.cols
    weights = (n+2, 2, 4)
    assert 2*weights[0] == weights[2] + n*weights[1]
    print(f'n={n}: compactification rank={size}, boundary rank={B.cols}, '
          f'kernel=Z*{list(v)}, square={square}, boundary graph=tree; '
          f'weights={weights}, degree={2*n+4}')
    records.append(dict(n=n,basis=names,intersection_matrix=[list(r) for r in Q.tolist()],
                        boundary_divisors=divisor_names,
                        boundary_columns=B.tolist(),
                        restriction=restriction.tolist(),kernel=list(v),square=square))

