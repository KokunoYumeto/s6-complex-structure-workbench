#!/usr/bin/env python3
"""Fresh weighted-Engel algebra; target original and old algorithms unopened.

Only the displayed admitted LR marking supplies the three base matrices.
The all-weight argument is written separately; exact finite cases verify
its presentation maps, including noncoprime free finite twists.
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import gcd
from pathlib import Path
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation7_iii_weighted_engel'
PAIRS = list(combinations(range(4), 2))


def wedge(A):
    return S.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k]
                      for k,l in PAIRS] for i,j in PAIRS])


def exterior(x,y):
    return S.Matrix([x[i]*y[j]-x[j]*y[i] for i,j in PAIRS])


def mats(d):
    return (S.Matrix([[1,-1,0,2*d],[0,-1,-1,6*d],[0,1,0,0],[0,0,0,1]]),
            S.Matrix([[1,0,1,-3*d],[0,0,1,0],[0,-1,0,6*d],[0,0,0,1]]),
            S.Matrix([[1,0,0,d],[0,1,1,0],[0,0,1,0],[0,0,0,1]]))


def integer(M):
    assert all(x.q == 1 for x in M)
    return M


def smith(M):
    D,U,V = smith_normal_decomp(M, domain=S.ZZ)
    for i in range(min(D.shape)):
        if D[i,i] < 0:
            D[i,:] = -D[i,:]; U[i,:] = -U[i,:]
    Ui,Vi = integer(U.inv()), integer(V.inv())
    assert U*M*V == D and Ui*D*Vi == M
    assert U*Ui == Ui*U == S.eye(U.rows)
    assert V*Vi == Vi*V == S.eye(V.rows)
    ds = [int(D[i,i]) for i in range(min(D.shape)) if D[i,i]]
    assert all(y % x == 0 for x,y in zip(ds,ds[1:]))
    return ds,D,U,V


def tor(M):
    ds,_,_,_ = smith(M)
    return M.rows-len(ds), [x for x in ds if x > 1]


def free(order,m,r,n,q):
    t = gcd(m,n,q*r)
    return gcd(m,r,n) == 1 and (m//t) % order == 0


def finite(d,k,l,r0,n0,r1,n1):
    m0,m1 = 3*k,4*l
    return (S.Matrix([[-2*d*n0,-6*d*r0,0],[-k,0,r0],
                      [0,m0,n0],[0,0,0]]),
            S.Matrix([[-3*d*n1,-6*d*r1,0],[2*l,0,-r1],
                      [0,0,0],[0,m1,n1]]))


def original(d):
    return (S.Matrix([[2*d,0,0],[0,1,0],[0,0,1],[0,0,0]]),
            S.Matrix([[3*d,0,0],[0,-1,0],[0,0,0],[0,0,1]]))


def det_expansion(M):
    n = M.rows
    ans = 0
    for p in permutations(range(n)):
        sign = (-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term = sign
        for i in range(n): term *= M[i,p[i]]
        ans += term
    return S.expand(ans)


def symbolic():
    d = S.Symbol('d', integer=True, positive=True)
    A0,A1,Ai = mats(d)
    assert A0**3 == A1**4 == A0*A1*Ai == S.eye(4)
    P = S.diag(1,1,1,d)
    for A,B in zip(mats(d),mats(1)):
        assert P*A == B*P
    e = S.eye(4)
    u0 = e[:,3]+2*d*(e[:,1]+e[:,2])
    u1 = e[:,3]+3*d*(e[:,1]+e[:,2])
    xi = S.Matrix([[0,0,-6*d,1,0,0]])
    E0,E1 = wedge(A0)-S.eye(6),wedge(A1)-S.eye(6)
    assert xi*E0 == xi*E1 == S.zeros(1,6)
    s = S.eye(6)
    pre1,pre2 = E0*s[:,3],E1*s[:,3]
    pre5 = -E0*s[:,4]-E1*s[:,5]-d*pre1+4*d*pre2
    pre6 = 2*d*pre1-E0*s[:,5]-pre5
    pre3 = E1*s[:,5]-pre5+pre6-3*d*pre1-6*d*pre2
    assert pre1 == s[:,0] and pre2 == s[:,1]
    assert S.simplify(pre5-s[:,4]) == S.zeros(6,1)
    assert S.simplify(pre6-s[:,5]) == S.zeros(6,1)
    assert S.simplify(pre3-(s[:,2]+6*d*s[:,3])) == S.zeros(6,1)
    q0,q1 = S.Matrix([[-3,1,-1,0],[0,0,0,1]]),S.Matrix([[-2,1,-1,0],[0,0,0,1]])
    assert q0*(A0-S.eye(4)) == q1*(A1-S.eye(4)) == S.zeros(2,4)
    assert (A0-S.eye(4))*(-e[:,1]-e[:,2]) == e[:,0]+3*e[:,1]
    assert (A1-S.eye(4))*(e[:,2]-e[:,1]) == e[:,0]+2*e[:,1]
    assert (A0-S.eye(4))*(-e[:,2]) == (A1-S.eye(4))*(-e[:,1]) == e[:,1]+e[:,2]
    assert A0*u0 == u0 and A1*u1 == u1
    assert sum((A0**j for j in range(3)),S.zeros(4))*e[:,1] == -e[:,0]
    assert sum((A1**j for j in range(4)),S.zeros(4))*e[:,1] == -2*e[:,0]
    assert sum((A0**j for j in range(3)),S.zeros(4))*e[:,3] == 3*u0
    assert sum((A1**j for j in range(4)),S.zeros(4))*e[:,3] == 4*u1
    assert (xi*exterior(e[:,1],u0))[0] == 2*d
    assert (xi*exterior(e[:,1],u1))[0] == 3*d
    assert (xi*exterior(e[:,3],e[:,0]))[0] == 6*d
    assert (xi*exterior(e[:,3],u0))[0] == (xi*exterior(e[:,3],u1))[0] == 0
    x = S.Matrix(S.symbols('x0:4'))
    assert (q0*(A1-S.eye(4))*x)[0] == 3*d*x[3]-x[2]
    n0,n1,k,l = S.symbols('n0 n1 k l', integer=True)
    K = S.Matrix([[-2*d*n0,-3*d*n1],[-k,2*l]])
    assert det_expansion(K) == S.expand(-d*(4*l*n0+3*k*n1))
    # All-weight boundary torsion is retained in the separate relative proof.
    assert wedge(Ai)-S.eye(6) == S.Matrix.hstack(
        S.zeros(6,1),s[:,0],S.zeros(6,1),S.zeros(6,1),
        -d*s[:,0],s[:,4]-d*s[:,1]-d*s[:,0])
    print('SYMBOLIC all d: actual cover conjugacy, finite orders/product, primitive fibre relations, norms, pairings and graph quotient identity PASS')
    print('SYMBOLIC two-log determinant: -d*(4*l*n0+3*k*n1); all signs and coefficients PASS')


def finite_checks():
    counts = Counter()
    examples = []
    for d in (1,2,3,4,6,12):
        A0,A1,Ai = mats(d)
        # Cusp H1 has a genuine d-torsion boundary class.
        assert tor(Ai-S.eye(4)) == (2,[] if d==1 else [d])
        assert tor(wedge(Ai)-S.eye(6)) == (4,[])
        O0,O1 = original(d)
        assert tor(S.Matrix.hstack(O0,O1)) == (0,[] if d==1 else [d])
        counts['both_original'] += 1
        for k in range(1,4):
            for l in range(1,4):
                m0,m1=3*k,4*l
                # Includes zero, signed, and both permitted nonprimitive normal classes.
                for r0,n0,r1,n1 in product((-1,1),(-3,-1,0,2,3),(-1,1),(-3,-1,0,2,3)):
                    f0,f1=free(3,m0,r0,n0,3),free(4,m1,r1,n1,2)
                    if not(f0 or f1): continue
                    B0,B1=finite(d,k,l,r0,n0,r1,n1)
                    if f1 and k == 1 and r0 == -1 and n0 == -3:
                        got=tor(S.Matrix.hstack(O0,B1))
                        want=tor(S.diag(d*gcd(2,n1),gcd(m1,n1)))
                        assert got == want
                        counts['original_IVstar'] += 1
                    if f0 and l == 1 and r1 == -1 and n1 == -3:
                        got=tor(S.Matrix.hstack(B0,O1))
                        want=tor(S.diag(d*gcd(3,n0),gcd(m0,n0)))
                        assert got == want
                        counts['original_III'] += 1
                    if not(f0 and f1): continue
                    P=m1*n0+m0*n1
                    got=tor(S.Matrix.hstack(B0,B1))
                    assert got[0] == int(P==0)
                    counts['all_free_two_log'] += 1
                    if gcd(m0,n0)==gcd(m1,n1)==1:
                        g=gcd(d,k,2*l)
                        want=(1,[g] if g>1 else []) if P==0 else (0,[x for x in (g,d*abs(P)//g) if x>1])
                        assert got==want,(d,k,l,n0,n1,got,want)
                        K=S.Matrix([[-2*d*n0,-3*d*n1],[-k,2*l]])
                        assert tor(K)==got
                        counts['coprime_closed_form'] += 1
                    else:
                        counts['noncoprime_free'] += 1
                    if len(examples)<12 and (gcd(m0,n0)>1 or gcd(m1,n1)>1):
                        examples.append(dict(d=d,k=k,l=l,r0=r0,n0=n0,r1=r1,n1=n1,P=P,result=got))
        print('WEIGHT',d,'all matrix/inverse checks PASS; cumulative',dict(sorted(counts.items())))
    # The zero-Euler coprime branch forces equal multiplicities; include it separately.
    for d,q in product((1,2,3,4,6,12),range(1,5)):
        m=12*q;k=4*q;l=3*q;n=1
        for r0,r1 in product((-1,0,1),repeat=2):
            B0,B1=finite(d,k,l,r0,n,r1,-n)
            g=gcd(d,2*q)
            assert tor(S.Matrix.hstack(B0,B1))==(1,[g] if g>1 else [])
            counts['zero_Euler_coprime']+=1
    print('ZERO EULER exact rank-one factorization checked in',counts['zero_Euler_coprime'],'cases')
    print('EXAMPLES',json.dumps(examples,sort_keys=True))
    print('TOTALS',json.dumps(dict(sorted(counts.items())),sort_keys=True))
    return dict(counts=counts,examples=examples)


if __name__ == '__main__':
    symbolic()
    result=finite_checks()
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'S6_SERIES_PUBLISH_III_02LA_fresh_arithmetic.json').write_text(
        json.dumps(result,indent=2)+'\n')
    print('Scope: fresh all-weight algebra; no historical or target-original input; finite tests support the separate universal proof.')
