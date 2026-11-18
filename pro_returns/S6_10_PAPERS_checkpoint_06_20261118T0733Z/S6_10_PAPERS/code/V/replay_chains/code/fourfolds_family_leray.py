"""Bounded exact low-degree coefficient diagnostics, v=-2,...,4.

These Smith groups are inputs to the integral Leray calculation, not
by themselves the total manifold homology. No transgression is inferred.
"""
from itertools import combinations
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
from fourfolds_family_survivors import family


def exterior(M,q):
    indices=list(combinations(range(M.rows),q))
    return s.Matrix([[M.extract(a,b).det() for b in indices] for a in indices])


def factors(M):
    D=smith_normal_form(M,domain=ZZ)
    return [abs(int(e)) for e in D.diagonal() if e]


for v in range(-2,5):
    A,B=family(v); A=A.applyfunc(int);B=B.applyfunc(int)
    print('PARAMETER',v,flush=True)
    for degree in (1,2,3,4):
        a,b=exterior(A,degree),exterior(B,degree)
        I=s.eye(a.rows)
        delta=s.Matrix.vstack(a-I,b-I)
        coin=s.Matrix.hstack(a-I,b-I)
        ds,cs=factors(delta),factors(coin)
        local=[a.rows-(T-I).rank() for T in (a,b,a*b)]
        h0=a.rows-len(ds); h2=a.rows-len(cs)
        h1=h0+h2+a.rows-sum(local)
        print('degree',degree,'global ranks h0,h1,h2',(h0,h1,h2),
              'delta torsion',[z for z in ds if z>1],
              'coinvariant torsion',[z for z in cs if z>1],flush=True)
print('All seven bounded parameters completed exactly.')
