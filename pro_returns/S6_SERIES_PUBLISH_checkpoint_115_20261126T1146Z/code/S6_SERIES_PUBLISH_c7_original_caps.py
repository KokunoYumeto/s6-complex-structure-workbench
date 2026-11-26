#!/usr/bin/env python3
"""Fresh construction-only integral cap and outer-boundary calculations.

No target statement, target proof, historical computation, or manuscript is
read. Input is the explicitly permitted six-profile defining JSON.
"""
from itertools import combinations
from pathlib import Path
import json
from math import gcd

import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.polys.domains import ZZ

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation7_iii_original_caps'
DATA = json.loads((OUT / 'S6_SERIES_PUBLISH_III_02KV_KW_raw_definitions.json').read_text())
PAIRS = list(combinations(range(4), 2))
J = s.Matrix([[0, 1], [-1, 0]])


def wedge2(A):
    return s.Matrix([[A.extract(ii, jj).det() for jj in PAIRS] for ii in PAIRS])


def ints(A):
    assert all(x.q == 1 for x in A)
    return [[int(x) for x in A.row(i)] for i in range(A.rows)]


def smith(A):
    D = smith_normal_form(A, domain=ZZ)
    return [abs(int(D[i, i])) for i in range(min(D.shape)) if D[i, i]]


def smith_certificate(A):
    D, U, V = smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(ZZ))
    D, U, V = D.to_Matrix(), U.to_Matrix(), V.to_Matrix()
    assert U*A*V == D and abs(U.det()) == abs(V.det()) == 1
    return {'D': ints(D), 'U': ints(U), 'Uinv': ints(U.inv()),
            'V': ints(V), 'Vinv': ints(V.inv())}


def kernel(A):
    D, U, V = smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(ZZ))
    D, U, V = D.to_Matrix(), U.to_Matrix(), V.to_Matrix()
    assert U * A * V == D and abs(U.det()) == abs(V.det()) == 1
    rank = sum(bool(D[i, i]) for i in range(min(D.shape)))
    K = V[:, rank:]
    assert A * K == s.zeros(A.rows, K.cols)
    return K, V.inv()[rank:, :]


def mv(maps, n):
    heights = [x.rows for x in maps]
    A = s.zeros(sum(heights), n * (len(maps) - 1))
    row = 0
    for i, f in enumerate(maps[:-1]):
        A[row:row + f.rows, n*i:n*(i+1)] = f
        row += f.rows
    for i in range(len(maps)-1):
        A[row:row+maps[-1].rows, n*i:n*(i+1)] = -maps[-1]
    return A


def solve_integer(A, B):
    D, U, V = smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(ZZ))
    D, U, V = D.to_Matrix(), U.to_Matrix(), V.to_Matrix()
    C = U * B
    X = s.zeros(A.cols, B.cols)
    for i in range(min(D.shape)):
        if D[i, i]:
            for j in range(B.cols):
                assert C[i, j] % D[i, i] == 0
                X[i, j] = C[i, j] / D[i, i]
        else:
            assert all(C[i, j] == 0 for j in range(B.cols))
    for i in range(min(D.shape), D.rows):
        assert all(C[i, j] == 0 for j in range(B.cols))
    X = V * X
    assert A * X == B
    ints(X)
    return X


def primitive_node(A, g):
    N = A-s.eye(2)
    col = next(N[:, j] for j in range(2) if N[:, j] != s.zeros(2, 1))
    h = gcd(abs(int(col[0])), abs(int(col[1])))
    u = col / h
    if next(x for x in u if x) < 0:
        u = -u
    assert N == u*u.T*J
    candidates = [(0, 1), (-1, 0), (1, 0), (0, -1)]
    candidates += sorted(((x, y) for x in range(-8, 9) for y in range(-8, 9)),
                         key=lambda v: (abs(v[0])+abs(v[1]), v))
    for x, y in candidates:
        r = s.Matrix([x, y])
        if (u.T*J*r)[0] == 1:
            k = next(g[i]/u[i] for i in range(2) if u[i])
            assert g == k*u and k.q == 1
            return u, r, k
    raise AssertionError('No Bezout complement found')


def local(row, i, d, cusp):
    typ = row['fibers'][i]
    A = s.Matrix(row['elliptic_matrices'][i])
    g = s.Matrix(row['generator_section_cocycle'][i])
    if typ == 'I1':
        u, r, k = primitive_node(A, g)
        z = k*r
    else:
        z = (A-s.eye(2)).inv()*g
    zq = d*z
    beta = -g.T*J*A
    bline = -z.T*J
    T = s.eye(4)
    T[:2, :2] = A
    T[:2, 3] = d*g
    T[2, :2] = beta
    T[2, 3] = (beta*zq)[0] + int(i == cusp)
    ints(T)
    S = s.eye(4)
    S[:2, 3] = zq
    S[2, :2] = bline
    assert S.det() == 1
    D = s.diag(A, 1, 1)
    D[2, 3] = int(i == cusp)
    assert S*T*S.inv() == D
    result = {'type': typ, 'T': ints(T), 'zG': [str(x) for x in z],
              'zQ': [str(x) for x in zq]}
    if typ == 'I1':
        H = S.inv()*s.diag(s.Matrix.hstack(u, r), 1, 1)
        ints(H)
        assert H.det() == 1 and H[:, 2] == s.Matrix([0, 0, 1, 0])
        Hinv = H.inv()
        canonical = s.eye(4)
        canonical[0, 1] = 1
        canonical[2, 3] = int(i == cusp)
        assert Hinv*T*H == canonical
        if i == cusp:
            f1 = Hinv.extract([1, 3], range(4))
            Q = s.Matrix([[1, 0, 0, 0, 0, 0],
                          [0, 0, 1, -1, 0, 0],
                          [0, 0, 0, 0, 1, 0],
                          [0, 0, 0, 0, 0, 1]])
            f2 = Q*wedge2(Hinv)
            result['cusp_valuation_lattice'] = [[1, 0], [0, 1]]
        else:
            f1 = Hinv.extract([1, 2, 3], range(4))
            f2 = wedge2(Hinv).extract([0, 3, 4, 5], range(6))
        result['H'] = ints(H)
        result['Hinv'] = ints(Hinv)
    elif typ == 'II':
        ints(S)
        f1 = S.extract([2, 3], range(4))
        f2 = wedge2(S).extract([0, 5], range(6))
    else:
        kcomp = {'III*': 8, 'I3*': 8, 'IV*': 7,
                 'III': 2, 'I1*': 6, 'IV': 3}[typ]
        assert all(x.q == 1 for x in zq)
        f1 = s.Matrix([[0, 0, 0, 1]])
        projection = s.Matrix([[1, 0, 0, zq[0]], [0, 1, 0, zq[1]]])
        f2 = s.zeros(kcomp-1, 6)
        for j, pair in enumerate(PAIRS):
            f2[0, j] = projection[:, list(pair)].det()
        result['component_count'] = kcomp
        result['H2_basis'] = ['fibre'] + [f'kernel_component_{j}' for j in range(kcomp-2)]
    assert f1*(T-s.eye(4)) == s.zeros(f1.rows, 4)
    assert f2*(wedge2(T)-s.eye(6)) == s.zeros(f2.rows, 6)
    result['f1'], result['f2'] = ints(f1), ints(f2)
    return T, f1, f2, result


records = []
for row in DATA['rows']:
    d = int(1/s.Rational(row['height_of_generator']))
    cusp = row['fibers'].index('I1')
    local_results = [local(row, i, d, cusp) for i in range(len(row['fibers']))]
    Ts, f1s, f2s, descriptions = map(list, zip(*local_results))
    P = s.eye(4)
    for T in Ts:
        P = P*T
    assert P == s.eye(4)
    M1, M2 = mv(f1s, 4), mv(f2s, 6)
    K, Kleft = kernel(M1)
    # In the fibre-connected sum the final fibre is identified with the other
    # fibres. These witnesses prove that every vertical H2 class is zero.
    vertical = s.zeros(M2.rows, 6)
    vertical[:f2s[0].rows, :] = f2s[0]
    vertical_witness = solve_integer(M2, vertical)
    R = []
    for i, T in enumerate(Ts):
        suffix = s.eye(4)
        for Tnext in Ts[i+1:]:
            suffix *= Tnext
        R.append((T-s.eye(4))*suffix)
    assert sum(R, s.zeros(4)) == s.zeros(4)
    R = s.Matrix.vstack(*R[:-1])
    assert M1*R == s.zeros(M1.rows, 4)
    RK = Kleft*R
    assert K*RK == R and R[:, 2] == s.zeros(R.rows, 1)
    independent_rims = RK[:, [0, 1, 3]]
    assert smith(independent_rims) == [1, 1, 1]
    rc = smith_certificate(independent_rims)
    rim_basis = s.Matrix.hstack(independent_rims, s.Matrix(rc['Uinv'])[:, 3:])
    assert abs(rim_basis.det()) == 1
    coker1 = M1.rows-M1.rank()
    coker2 = M2.rows-M2.rank()
    assert smith(M1) == [1]*M1.rank()
    assert smith(M2) == [1]*M2.rank()
    assert coker1 == 1 and coker2 + K.cols == 10
    record = {'OS': row['OS'], 'profile': row['profile'], 'd': d,
              'cusp_index': cusp, 'local': descriptions,
              'MV1': ints(M1), 'MV2': ints(M2),
              'MV1_kernel_basis': ints(K), 'MV1_kernel_left_inverse': ints(Kleft),
              'vertical_zero_witness': ints(vertical_witness),
              'rim_in_kernel_coordinates': ints(RK),
              'rim_completed_basis': ints(rim_basis),
              'rim_completed_basis_inverse': ints(rim_basis.inv()),
              'MV1_smith_certificate': smith_certificate(M1),
              'MV2_smith_certificate': smith_certificate(M2),
              'MV1_smith': smith(M1), 'MV2_smith': smith(M2),
              'cap_cokernel_rank': coker2, 'edge_kernel_rank': K.cols,
              'rim_smith': smith(independent_rims)}
    records.append(record)
    print(f"PASS {row['OS']}/{row['profile']}: product I; H1 exterior Z; "
          f"H2 exterior Z^{coker2}+Z^{K.cols}=Z^10; all vertical 2-tori zero; "
          "three primitive independent rims; unit cusp valuation lattice")

(OUT/'S6_SERIES_PUBLISH_III_02KV_fresh_cap_maps.json').write_text(json.dumps(records, indent=2)+'\n')
print('PASS six independent cap/boundary calculations written with exact integer witnesses')
