"""Actual separating torus twist in the circle fibre of E.2.13.

All matrices are exact rational boundary restriction maps.  The two
pieces are E_12 x T^3 and T^3 x E_12.  Deck-invariant cohomology of
E_12 is the pullback of H*(E); noninvariant classes restrict to zero.
This program does not identify the full smooth type of E_12 or Y.
"""
from pathlib import Path
from itertools import combinations
from functools import reduce
from math import gcd
import json

import sympy as sp
from manifolds_shifted_mv import F, E, phi, wedge_sign

BASE = {k: list(combinations(range(8), k)) for k in range(9)}
NAMES = ['g1', 'u1', 'w1', 'd1', 'g2', 'u2', 'w2', 'd2']


def wedge(a, b, coefficient=1):
    sign = wedge_sign(a, b)
    return (tuple(sorted(a+b)), coefficient*sign) if sign else (None, 0)


def restriction(k, alpha, side):
    if k == 0:
        return {(): sp.Integer(1)}
    offset = 4*side
    # xi|boundary=theta+12 gamma fixes epsilon=+1. Ring closure then
    # forces eta=-1, as checked by multiplying r1(1) by r2(delta).
    ph = phi(k, 1, -1)
    result = {}
    for index, beta in enumerate(F[k]):
        coefficient = ph[index, F[k-1].index(alpha)]
        if coefficient:
            result[tuple(x+offset for x in beta)] = coefficient
    # theta on E becomes 12(g_other-g_own) on the level Y.
    for a, coefficient in ((4 if side == 0 else 0, 12),
                           (0 if side == 0 else 4, -12)):
        beta, n = wedge((a,), tuple(x+offset for x in alpha), coefficient)
        if n:
            result[beta] = result.get(beta, 0)+n
    return result


def boundary_matrix(k, side):
    cols = []
    labels = []
    torus = range(5, 8) if side == 0 else range(1, 4)
    for p in range(5):
        for alpha in E.get(p, []):
            for beta in combinations(torus, k-p) if 0 <= k-p <= 3 else []:
                vec = sp.zeros(len(BASE[k]), 1)
                for a, coefficient in restriction(p, alpha, side).items():
                    b, n = wedge(a, beta, coefficient)
                    if n:
                        vec[BASE[k].index(b), 0] += n
                cols.append(vec)
                labels.append((p, alpha, beta))
    matrix = sp.Matrix.hstack(*cols) if cols else sp.zeros(len(BASE[k]), 0)
    return matrix, labels


def contraction(k):
    """Contraction by the primitive diagonal g1+g2."""
    C = sp.zeros(len(BASE[k-1]), len(BASE[k]))
    for col, monomial in enumerate(BASE[k]):
        for i, variable in enumerate(monomial):
            if variable in (0, 4):
                C[BASE[k-1].index(monomial[:i]+monomial[i+1:]), col] += (-1)**i
    return C


def primitive(v):
    denominator = sp.ilcm(*[a.q for a in v]) if len(v) > 1 else v[0].q
    integers = [int(denominator*a) for a in v]
    divisor = reduce(gcd, integers, 0)
    return sp.Matrix([a//abs(divisor) for a in integers]) if divisor else v


def describe(v, k):
    return [{'coefficient': int(c),
             'monomial': [NAMES[i] for i in BASE[k][j]]}
            for j, c in enumerate(v) if c]


def run():
    matrices = {}
    rows = []
    rank = {}
    dim = {}
    for k in range(9):
        A, _ = boundary_matrix(k, 0)
        B, _ = boundary_matrix(k, 1)
        matrices[k] = (A, B)
        D = A.row_join(B)
        rank[k] = D.rank()
        dim[k] = D.cols
    invariant_betti = [
        (dim[k]-rank[k] if k < 9 else 0)
        +(len(BASE[k-1])-rank[k-1] if k > 0 else 0)
        for k in range(10)
    ]
    assert invariant_betti == [1, 0, 1, 19, 45, 45, 19, 1, 0, 1]

    for k in range(1, 9):
        A, B = matrices[k]
        relation = A.row_join(-B)
        kernel = relation.nullspace()
        common_columns = [A*v[:A.cols, :] for v in kernel]
        common = (sp.Matrix.hstack(*common_columns) if common_columns
                  else sp.zeros(len(BASE[k]), 0))
        old = matrices[k-1][0].row_join(matrices[k-1][1])
        image = contraction(k)*common
        variation_rank = old.row_join(image).rank()-old.rank()
        row = {'degree': k, 'variation_rank': variation_rank,
               'common_boundary_rank': common.rank()}
        if variation_rank:
            assert variation_rank == 1 and k in (4, 5)
            for col in range(common.cols):
                if old.row_join(image[:, col]).rank() > old.rank():
                    witness = primitive(common[:, col])
                    row['boundary_witness'] = describe(witness, k)
                    row['contracted_witness'] = describe(contraction(k)*witness, k-1)
                    break
            else:
                raise AssertionError('Missing rank-one witness')
        rows.append(row)
    assert [r['variation_rank'] for r in rows] == [0, 0, 0, 1, 1, 0, 0, 0]

    # Wang for the actual P, whose rational Betti numbers are E.2.7.
    p_betti = [1, 1, 1, 20, 63, 88, 63, 20, 1, 1, 1]
    blocks = []
    preceding = 0
    for degree, value in enumerate(p_betti[:-1]):
        preceding = value-preceding
        blocks.append(preceding)
    sizes_two = [invariant_betti[k]-blocks[k] for k in range(10)]
    assert sizes_two == [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    sizes_one = [blocks[k]-sizes_two[k] for k in range(10)]
    assert all(n >= 0 for n in sizes_one)
    output = {
        'scope': 'E.2.14: actual torus-twist variation, not a smooth classification.',
        'invariant_boundary_map_ranks': [rank[k] for k in range(9)],
        'invariant_piece_dimensions': [dim[k] for k in range(9)],
        'generalized_eigenvalue_one_betti': invariant_betti,
        'eigenvalue_one_Jordan_blocks_size_one': sizes_one,
        'eigenvalue_one_Jordan_blocks_size_two': sizes_two,
        'variation': rows,
    }
    Path(__file__).with_suffix('.out.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2))


if __name__ == '__main__':
    run()
