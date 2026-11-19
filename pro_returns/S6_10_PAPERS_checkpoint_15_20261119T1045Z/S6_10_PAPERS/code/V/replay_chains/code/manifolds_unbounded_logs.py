"""Exact arbitrary-multiplicity computation for the IV*, III, I1 family.

The geometric and integral comparison proof is Theorem D.2.5.  This program
does not call the bounded Threefold Explorer service.  Its Smith matrices
come from the marked van Kampen presentation and normal-circle tori.

Usage: python manifolds_unbounded_logs.py [k l n0 n1 [r0 r1]]
The unrestricted algorithm accepts m0=3*k, m1=4*l, gcd(ni,mi)=1.
Without arguments it executes the exact validation bounds stated below.
"""
from pathlib import Path
from math import gcd
import json
import sys
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

ROOT = Path(__file__).resolve().parents[1]


def smith(matrix):
    D = smith_normal_form(matrix, domain=s.ZZ)
    nonzero = [abs(int(D[i, i])) for i in range(min(D.shape)) if D[i, i]]
    return dict(rank=matrix.rows-len(nonzero),
                torsion=[v for v in nonzero if v > 1], diagonal=nonzero)


def bezout(m, n):
    alpha, beta, common = map(int, s.gcdex(m, n))
    assert common == 1 and m*alpha+n*beta == 1
    return alpha, beta


def compute(k, ell, n0, n1, r0=0, r1=0):
    m0, m1 = 3*k, 4*ell
    if k < 1 or ell < 1 or gcd(n0, m0) != 1 or gcd(n1, m1) != 1:
        raise ValueError('Require positive k,l and gcd(ni,mi)=1.')
    a0, b0 = bezout(m0, n0)
    a1, b1 = bezout(m1, n1)
    presentation = s.Matrix([[-n0, m0], [-n1, -m1]])
    B = s.Matrix([[-2*n0, -6*r0*a0, -3*n1, -6*r1*a1],
                  [-k, r0*b0, 2*ell, -r1*b1],
                  [0, 1, 0, 0], [0, 0, 0, 1]])
    P = m1*n0+m0*n1
    assert presentation.det() == B.det() == P
    group = smith(presentation.T)
    coker = smith(B)
    assert group['torsion'] == coker['torsion'] == ([] if abs(P) <= 1 else [abs(P)])
    assert group['rank'] == coker['rank'] == int(P == 0)
    if P:
        H = [{'rank': int(j in (0, 6)),
              'torsion': [abs(P)] if j in (1, 2, 3, 4) and abs(P) > 1 else []}
             for j in range(7)]
    else:
        H = [{'rank': rank, 'torsion': []} for rank in (1, 1, 2, 2, 2, 1, 1)]
    return dict(k=k, ell=ell, m0=m0, m1=m1, n0=n0, n1=n1,
                r0=r0, r1=r1, P=P, pi1=group, H=H,
                normal_torus_matrix=[list(map(int, row)) for row in B.tolist()],
                sphere=abs(P) == 1)


def validation():
    k, ell, n0, n1, r0, r1, a0, a1, b0, b1 = s.symbols(
        'k ell n0 n1 r0 r1 a0 a1 b0 b1', integer=True)
    B = s.Matrix([[-2*n0, -6*r0*a0, -3*n1, -6*r1*a1],
                  [-k, r0*b0, 2*ell, -r1*b1],
                  [0, 1, 0, 0], [0, 0, 0, 1]])
    assert s.expand(B.det()) == 4*ell*n0+3*k*n1
    print('Symbolic determinant:', s.expand(B.det()))
    A0 = s.Matrix([[1, -1, 0, 2], [0, -1, -1, 6],
                   [0, 1, 0, 0], [0, 0, 0, 1]])
    A1 = s.Matrix([[1, 0, 1, -3], [0, 0, 1, 0],
                   [0, -1, 0, 6], [0, 0, 0, 1]])
    Ainf = s.Matrix([[1, 0, 0, 1], [0, 1, 1, 0],
                     [0, 0, 1, 0], [0, 0, 0, 1]])
    delta, a, b, d = [s.eye(4)[:, j] for j in range(4)]
    u0, u1 = d+2*a+2*b, d+3*a+3*b
    assert A0*A1*Ainf == s.eye(4) and A0**3 == A1**4 == s.eye(4)
    N0 = sum((A0**j for j in range(3)), s.zeros(4))
    N1 = sum((A1**j for j in range(4)), s.zeros(4))
    assert N0*a == -delta and N1*a == -2*delta
    assert N0*d == 3*u0 and N1*d == 4*u1
    print('Monodromy, invariant vectors, and minimal norm matrices checked.')
    checked = 0
    for kk in range(1, 9):
        for ll in range(1, 9):
            for nn0 in (-1, 1, 3*kk-1):
                for nn1 in (-1, 1, 4*ll-1):
                    for rr0, rr1 in ((0, 0), (2, -3)):
                        compute(kk, ll, nn0, nn1, rr0, rr1)
                        checked += 1
    print('Actual integer Smith computations:', checked,
          '; 1<=k,l<=8; n0 in {-1,1,3k-1}; n1 in {-1,1,4l-1};'
          ' (r0,r1)=(0,0),(2,-3).')
    arithmetic_checks = 0
    for kk in range(1, 31):
        for ll in range(1, 31):
            for nn0 in range(-3*kk, 3*kk+1):
                if gcd(nn0, 3*kk) != 1:
                    continue
                for nn1 in (-1, 1, 4*ll-1):
                    assert gcd(gcd(2*nn0, 3*nn1), gcd(kk, 2*ll)) == 1
                    assert gcd(gcd(nn0, nn1), gcd(3*kk, 4*ll)) == 1
                    arithmetic_checks += 1
    print('Exact gcd checks:', arithmetic_checks,
          '; 1<=k,l<=30; |n0|<=3k with gcd(n0,3k)=1; n1=-1,1,4l-1.')
    examples = [compute(1, 1, 1, -1), compute(3, 1, -2, 1),
                compute(3, 1, 1, 1), compute(2, 1, 1, 1),
                compute(4, 3, 1, -1), compute(8, 6, 1, -1)]
    target = ROOT/'records/manifolds_unbounded_logs.json'
    target.write_text(json.dumps(dict(symbolic_determinant=str(s.expand(B.det())),
                                    smith_checks=checked, gcd_checks=arithmetic_checks,
                                    examples=examples), indent=2)+'\n')
    for e in examples:
        print('m=', (e['m0'], e['m1']), 'n=', (e['n0'], e['n1']),
              'P=', e['P'], 'pi1=', e['pi1'], 'H=', e['H'])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(json.dumps(compute(*map(int, sys.argv[1:])), indent=2))
    else:
        validation()
