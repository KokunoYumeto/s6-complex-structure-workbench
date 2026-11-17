"""Exact local prism determinants for the rescaled source-zero sectors.

This certifies the displayed period actions and cone determinants. It does
not promote the common-face, quotient-properness, or global cap attachment.
"""
from datetime import datetime, timezone
from pathlib import Path
import json
import sympy as s

root = Path(__file__).resolve().parents[2]
dest = Path(__file__).with_suffix('.json')
N = s.symbols('N', integer=True, positive=True)
n1, n2 = s.symbols('n1 n2', integer=True)
e1, e2 = s.Matrix([1, 0]), s.Matrix([0, 1])
zero = s.zeros(2, 1)
tetrahedra = [(0, 1, 2, 5), (0, 1, 4, 5), (0, 3, 4, 5)]
orientation = [1, -1, 1]
checks = []
sectors = []

def check(name, value):
    assert bool(value), name
    checks.append(name)

def ray(P, vertex, side):
    return (P * vertex).col_join(e1 if side == 0 else e2)

for a, b in [(1, 2), (2, 1)]:
    H = s.Matrix([[2, b], [-a, N - 1]])
    W = s.Matrix([[1, b], [-a, -2]])
    E = s.diag(0, N)
    check(f'ab2_{a}_{b}', a * b == 2)
    for name, P, u, v, expected in [
        ('I', s.eye(2), e1, e2, [[1, N-1, 2*N], [1, 2, 2*N]]),
        ('W', W, e1, e2-b*e1, [[0, N-1, 2*N], [0, 0, 2*N]]),
        ('E', E, e1, e2, [[0, 0, 2*N], [0, 2*N, 2*N]]),
    ]:
        check(f'basis_{a}_{name}', s.Matrix.hstack(u, v).det() == 1)
        B = s.Matrix.hstack(P * s.Matrix([n1,n2]), H * s.Matrix([n1,n2]))
        translation = s.eye(4)
        translation[:2, 2:4] = B
        check(f'period_unimodular_{a}_{name}', translation.det() == 1)
        triangles = [[zero, u, u+v], [zero, v, u+v]]
        determinants = []
        for ti, triangle in enumerate(triangles):
            vertices = [ray(P,z,0) for z in triangle] + [ray(H,z,1) for z in triangle]
            signs = 1 if ti == 0 else -1
            row = []
            for j, tet in enumerate(tetrahedra):
                matrix = s.Matrix.hstack(*(vertices[k] for k in tet))
                det = s.factor(signs * orientation[j] * matrix.det())
                check(f'cone_det_{a}_{name}_{ti}_{j}', s.expand(det-expected[ti][j]) == 0)
                row.append(str(det))
            determinants.append(row)
            for vi, vector in enumerate(vertices):
                side = 0 if vi < 3 else 1
                Pside = P if side == 0 else H
                z = triangle[vi % 3]
                check(f'period_ray_{a}_{name}_{ti}_{vi}',
                      (translation * vector - ray(Pside,z+s.Matrix([n1,n2]),side)).applyfunc(s.expand) == s.zeros(4,1))
        r, t = s.symbols('r t', nonnegative=True)
        determinants_period = {
            'I': r*r + (N+1)*r*t + 2*N*t*t,
            'W': (N-1)*r*t + 2*N*t*t,
            'E': 2*N*r*t + 2*N*t*t,
        }
        period_det = s.factor((r*P+t*H).det())
        check(f'period_det_{a}_{name}', s.expand(period_det-determinants_period[name]) == 0)
        sectors.append({
            'a':a, 'b':b, 'boundary':name,
            'P0':[[str(x) for x in P.row(i)] for i in range(2)],
            'P1':[[str(x) for x in H.row(i)] for i in range(2)],
            'basis':[[str(x) for x in s.Matrix.hstack(u,v).row(i)] for i in range(2)],
            'oriented_prism_determinants':determinants,
            'period_determinant':str(period_det),
        })
    S = s.Matrix([[1,0],[a,1]])
    basis = s.Matrix.hstack(e1,e2-b*e1)
    check(f'W_normal_form_{a}', S*W*basis == s.diag(1,0))
    check(f'H_normal_form_{a}', S*H*basis == s.Matrix([[2,-b],[a,N-1]]))
    shear = s.Matrix([[1,s.Rational(b,1)/(N-1)],[0,1]])
    target = s.Matrix([[2*N/(N-1),0],[a,N-1]])
    check(f'H_triangular_form_{a}', (shear*S*H*basis-target).applyfunc(s.simplify) == s.zeros(2))

record = {
    'utc':datetime.now(timezone.utc).isoformat(),
    'status':'PASS for the exact displayed local determinant and period-action identities',
    'check_count':len(checks), 'checks':checks, 'sectors':sectors,
    'positivity':'For the actual rescaling N=M>1, every displayed determinant is nonnegative, and each nonzero determinant is positive. The interior period determinant is positive.',
    'scope':'No common-face assertion, global periodic fan, quotient properness, finite cap attachment, link count or source return is inferred by this certificate.',
    'correction':'At rank-one boundary sectors the zero-determinant prism tetrahedra collapse even at positive base ratio. The raw piecewise linear map is not claimed injective there.'
}
dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':record['status'],'check_count':len(checks),'sectors':sectors},indent=2))
