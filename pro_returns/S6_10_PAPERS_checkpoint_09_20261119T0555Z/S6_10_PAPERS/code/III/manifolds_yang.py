"""Exact integral certificates for D.2.10, both Yang logarithmic families.

The default run checks the geometric monodromies, finite quotient lattices,
cusp restriction matrices, relative boundary groups, and full 4x7 Smith forms.
The proof is unrestricted; finite execution bounds are reported explicitly.
For one arbitrary admissible input:
    python code/manifolds_yang.py B 2 3 2 1 -1 7 -4
Arguments: type, cusp index R, k, l, n1, n2, r1, r2.
"""
from pathlib import Path
from itertools import combinations
from math import gcd
import json
import sys
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

ROOT = Path(__file__).resolve().parents[1]
PAIRS = list(combinations(range(4), 2))
gamma, u, w, delta = [s.eye(4)[:, i] for i in range(4)]
J = s.zeros(6)
for i, j, value in ((0, 5, 1), (1, 4, -1), (2, 3, 1)):
    J[i, j] = J[j, i] = value


def wedge(A):
    return s.Matrix([[A.extract(i, j).det() for j in PAIRS] for i in PAIRS])


def bivector(x, y):
    return s.Matrix([x[i]*y[j]-x[j]*y[i] for i, j in PAIRS])


def smith(A):
    D = smith_normal_form(A, domain=s.ZZ)
    return [abs(int(D[i, i])) for i in range(min(D.shape))]


def monodromies(kind, R):
    c, d, a = (2, 4, 2) if kind == 'B' else (3, 3, 1)
    A1 = s.Matrix([[1, 0, 0, 0], [0, 0, 1, 0],
                   [-c*R, -1, 2-c, 0], [-R, 0, -1, 1]])
    A2 = s.Matrix([[1, 0, 0, 0], [0, 1, -1, 0],
                   [0, 1, 0, 0], [0, 0, 0, 1]])
    return A1, A2, c, d, a


def cusp_restriction(R, ell):
    """Actual 3R x 4R normalization restriction-difference matrix."""
    M = s.zeros(3*R, 4*R)
    def add(row, vertex, coord, value):
        M[row, 4*(vertex % R)+coord] += value
    for j in range(R):
        add(j, j, 1, 1)
        for coord, value in ((0, -1), (2, 1), (3, 1)):
            add(j, j+1, coord, value)
        for coord, value in ((0, 1), (1, -1), (2, -1)):
            add(R+j, j, coord, value)
        add(R+j, j-ell, 3, -1)
        add(2*R+j, j, 2, 1)
        for coord, value in ((0, -1), (1, 1), (3, 1)):
            add(2*R+j, j-ell-1, coord, value)
    return M


def finite_presentation(A, v, m):
    B = (A-s.eye(4)).col_join(s.zeros(1, 4))
    return B.row_join((-v).col_join(s.Matrix([m])))


def data_for(kind, R, k, l, n1, n2, r1=0, r2=0, finite_checks=True):
    if kind not in ('B', 'C') or min(R, k, l) < 1:
        raise ValueError('Need kind B/C and positive R,k,l.')
    A1, A2, c, d, a = monodromies(kind, R)
    m1, m2 = d*k, 6*l
    if gcd(n1, m1) != 1 or gcd(n2, m2) != 1:
        raise ValueError('Need gcd(n1,m1)=gcd(n2,m2)=1.')
    ell = gamma-R*(u+w)
    v1, v2 = n1*ell+r1*delta, n2*gamma+r2*delta
    P = m2*n1+m1*n2
    h = gcd(gcd(R, a*k), abs(P))
    omega1 = s.Matrix([-R, R, 0, 1, 0, 0])
    omega2 = s.Matrix([1, -1, c, 0, 0, 0])
    P1 = s.Matrix.hstack(omega1, (m1//c)*omega2)
    P2 = s.Matrix([[0, 0], [0, 0], [0, -m2], [1, 0], [0, 0], [0, 0]])
    alpha2 = P1.T.col_join(-P2.T)
    b = s.Matrix([0, -n1, 0, n2])
    D = alpha2.row_join(b)
    C = s.Matrix([[R, 0, 0], [-a*k, m1, -n1], [0, m2, n2]])
    expected = [1, 1, h, R*abs(P)//h] if P else [1, 1, h, 0]
    assert smith(D) == expected, (kind, R, k, l, n1, n2, smith(D), expected)
    assert smith(C) == expected[1:]
    assert C.det() == R*P
    circ = s.Matrix([[-n1, m1, 0], [-n2, 0, m2]])
    d0 = gcd(m1, m2)
    assert smith(circ) == [1, d0]
    completed = circ.col_join(s.Matrix([[0, 1, 1]]))
    assert smith(completed) == [1, 1, abs(P)]
    phi = s.Matrix([m1*m2//d0, m2*n1//d0, m1*n2//d0])
    assert circ*phi == s.zeros(2, 1)
    assert gcd(gcd(*[abs(int(x)) for x in phi[:2]]), abs(int(phi[2]))) == 1
    assert int(phi[1]+phi[2]) == P//d0
    if P == 0:
        assert m1 == m2 and n2 == -n1
    if finite_checks:
        assert A1*v1 == v1 and A2*v2 == v2
        assert smith(finite_presentation(A1, v1, m1)) == [1, 1, 1, 0, 0]
        assert smith(finite_presentation(A2, v2, m2)) == [1, 1, 1, 0, 0]
        assert (wedge(A1.inv().T)-s.eye(6))*P1 == s.zeros(6, 2)
        assert (wedge(A2.inv().T)-s.eye(6))*P2 == s.zeros(6, 2)
        assert P1.T*J*P1 == s.Matrix([[0, m1], [m1, 0]])
        assert P2.T*J*P2 == s.Matrix([[0, -m2], [-m2, 0]])
        assert P1.T*bivector(delta, v1)/m1 == s.Matrix([0, -n1])
        assert P2.T*bivector(delta, v2)/m2 == s.Matrix([0, n2])
    torsion = [x for x in ([h, R*abs(P)//h] if P else [h]) if x > 1]
    ranks = [1, 0, R-1, 0, R-1, 0, 1] if P else [1, 1, R+1, 2, R+1, 1, 1]
    assert sum((-1)**i*b for i, b in enumerate(ranks)) == 2*R
    return dict(kind=kind, R=R, k=k, l=l, m1=m1, m2=m2, n1=n1, n2=n2,
                r1=r1, r2=r2, P=P, h=h, pi1=('Z' if P == 0 else f'Z/{abs(P)}'),
                betti=ranks, H2_H3_torsion=torsion, full_smith=expected,
                alpha2=alpha2.tolist(), cusp_column=b.tolist(), reduced=C.tolist(),
                free_meridian_value=-P//d0,
                relative_kernel_rank=R if P == 0 else R-1)


def json_default(x):
    return int(x) if isinstance(x, s.Integer) else x


def run():
    R = s.symbols('R', integer=True, positive=True)
    symbolic = {}
    for kind in ('B', 'C'):
        A1, A2, c, d, a = monodromies(kind, R)
        assert A1**d == A2**6 == s.eye(4)
        assert A1*(gamma-R*(u+w)) == gamma-R*(u+w)
        P0 = A1*A2
        C0 = wedge(P0)-s.eye(6)
        rows = (1, 5) if kind == 'B' else (2, 5)
        assert C0.extract(rows, (0, 3)).det() == -1
        assert C0.rank() == 2
        assert A1.inv()*w == -u and A2.inv()*(-u) == w
        joint = s.Matrix.hstack(A1-s.eye(4), A2-s.eye(4))
        unit_cols = next(cols for cols in combinations(range(8), 3)
                         if joint.extract((1, 2, 3), cols).det() in (-1, 1))
        assert joint.rank() == 3
        symbolic[kind] = dict(A1=A1.tolist(), A2=A2.tolist(),
                              cusp_exterior=C0.tolist(),
                              cusp_unit_rows=[i+1 for i in rows],
                              joint_unit_columns=[i+1 for i in unit_cols])
        print(kind, 'symbolic finite orders, fixed vectors, clockwise cusp rank2/unit minor,')
        print('  joint monodromy unit columns:', symbolic[kind]['joint_unit_columns'])

    cusp_checks = 0
    for ell in (1, 2):
        for R in range(1, 17):
            vals = smith(cusp_restriction(R, ell))
            assert vals == [1]*(3*R-2)+[0, 0]
            cusp_checks += 1
    print('Cusp normalization full Smith forms:', cusp_checks, '; ell=1,2; 1<=R<=16.')

    checked, degenerate, finite_checked = 0, 0, 0
    for kind in ('B', 'C'):
        d = 4 if kind == 'B' else 3
        for R in (1, 2, 3, 4, 6, 12):
            for k in range(1, 5):
                for l in range(1, 4):
                    for n1 in (-5, -2, -1, 1, 2, 5):
                        if gcd(n1, d*k) != 1:
                            continue
                        for n2 in (-5, -1, 1, 5):
                            if gcd(n2, 6*l) != 1:
                                continue
                            record = data_for(kind, R, k, l, n1, n2,
                                              7, -4, finite_checks=False)
                            checked += 1
                            degenerate += int(record['P'] == 0)
        for R in (1, 2, 6):
            for k, l in ((1, 1), (3, 2), (4, 3)):
                for n1, n2 in ((1, -1), (-1, 1), (5, 5)):
                    if gcd(n1, d*k) != 1 or gcd(n2, 6*l) != 1:
                        continue
                    for r1, r2 in ((0, 0), (7, -4), (-13, 18)):
                        data_for(kind, R, k, l, n1, n2, r1, r2)
                        finite_checked += 1
    print('Full augmented 4x7 Smith forms:', checked, '; P=0 cases:', degenerate)
    print('Bounds: R in {1,2,3,4,6,12}; 1<=k<=4; 1<=l<=3;')
    print('  n1 in {-5,-2,-1,1,2,5}, n2 in {-5,-1,1,5}; admissibility enforced.')
    print('Additional full finite quotient pullback, sweep, and 5x5 abelianization checks:',
          finite_checked)
    examples = []
    for args in (('B', 1, 1, 1, 1, -1), ('B', 2, 1, 1, 1, -1),
                 ('C', 2, 1, 1, 1, -1), ('B', 6, 3, 2, 1, -1),
                 ('C', 6, 2, 1, 1, -1), ('C', 3, 1, 2, 2, 1),
                 ('B', 101, 7, 11, 3, -5)):
        ex = data_for(*args, r1=7, r2=-4)
        examples.append(ex)
        print({k: ex[k] for k in ('kind', 'R', 'm1', 'm2', 'n1', 'n2',
                                  'P', 'h', 'pi1', 'betti', 'H2_H3_torsion')})
    payload = dict(theorem='D.2.10', checks=checked, zero_P_checks=degenerate,
                   finite_quotient_checks=finite_checked,
                   cusp_checks=cusp_checks, symbolic=symbolic, examples=examples)
    (Path(__file__).resolve().parent/'manifolds_yang.json').write_text(
        json.dumps(payload, indent=2, default=lambda x:
                   int(x) if isinstance(x, s.Integer) else str(x))+'\n')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if len(sys.argv) != 9:
            raise SystemExit('Usage: manifolds_yang.py TYPE R k l n1 n2 r1 r2')
        output = data_for(sys.argv[1], *map(int, sys.argv[2:]))
        print(json.dumps(output, indent=2, default=json_default))
    else:
        run()
