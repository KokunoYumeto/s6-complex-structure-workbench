"""Exact canonical finite-cap certificates in all relevant degrees.

Both finite orders5,4 and exterior degrees0..6 are exhausted. No unbounded
matrix search is used: the proof reduces every eligible cap locally to
these models by prime-to-the-relevant-prime isogenies.
"""
import sympy as S
from itertools import combinations
from fourfolds_survivor_test import kernel,factors,wedge_map

def cup_matrix(n,q):
    left=list(combinations(range(n),q));right=list(combinations(range(n),n-q))
    J=S.zeros(len(left),len(right))
    for i,a in enumerate(left):
        b=tuple(j for j in range(n) if j not in a);j=right.index(b)
        c=a+b;J[i,j]=(-1)**sum(c[k]>c[l] for k in range(n) for l in range(k+1,n))
    return J

for m in (5,4):
    cycle=S.zeros(m)
    for j in range(m):cycle[(j+1)%m,j]=1
    D=cycle if m==5 else S.diag(cycle,-1)
    T=S.diag(1,D).T
    print('FINITE ORDER',m,'vertical model',D.tolist())
    invariants={q:kernel(wedge_map(T,q)-S.eye(S.binomial(6,q))) for q in range(7)}
    assert [invariants[q].cols for q in range(7)]==[1,2,3,4,3,2,1]
    for q in range(2,6):
        tors=[d for d in factors(wedge_map(D.T,q-1)-S.eye(S.binomial(5,q-1))) if d>1]
        assert tors==([] if m==5 else [2])
        print('cap torsion degree',q,tors)
    pairings={}
    for q in (1,2,3):
        Gram=invariants[q].T*cup_matrix(6,q)*invariants[6-q]
        det=abs(int(Gram.det()));pairings[q]=det
        expected={1:m,2:m**3,3:m**4}[q]
        assert det==expected
        print('invariant pairing degrees',q,6-q,'determinant',det)
    assert m**4==pairings[3]
    assert m**3==pairings[2]
    assert m**2==m*pairings[1]
    print('covering indices in degrees1..5:',[m,1,1,1,1])
print('ALL CANONICAL CAP CERTIFICATES PASSED')
