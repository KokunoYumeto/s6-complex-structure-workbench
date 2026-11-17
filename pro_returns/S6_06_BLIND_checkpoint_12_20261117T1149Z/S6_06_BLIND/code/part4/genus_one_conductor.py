#!/usr/bin/env python3
"""Exact conductor jets for the omitted genus-one planar curve models.

The geometric proof is in P4.14.  At every jet order used, columns are
restrictions of all ambient monomials relevant modulo the parameter power.
Ranks are exact over Q, including the codimension defining delta.
"""
from itertools import product
import sympy as S

t = S.symbols('t')

def jet_column(branches, a, b, n):
    col = []
    for x, y in branches:
        p = S.Poly(S.expand(x**a * y**b), t)
        col.extend(p.nth(k) for k in range(n))
    return S.Matrix(col)

models = {
    'III_tacnode_y(y-x^2)': [(t,0),(t,t**2)],
    'IV_triple_xy(x-y)': [(t,0),(0,t),(t,t)],
}
for name, branches in models.items():
    print(name)
    for n in (2,3,4,6,8):
        cols = [jet_column(branches,a,b,n)
                for a,b in product(range(n),repeat=2) if a+b < n]
        A = S.Matrix.hstack(*cols)
        rank = A.rank()
        delta = len(branches)*n-rank
        assert delta == (2 if len(branches)==2 else 3)
        for j in range(len(branches)):
            for k in range(2,n):
                v = S.zeros(len(branches)*n,1); v[j*n+k]=1
                assert A.row_join(v).rank() == rank
            v = S.zeros(len(branches)*n,1); v[j*n+1]=1
            assert A.row_join(v).rank() > rank
        print(' jet order',n,'normalization dimension',len(branches)*n,
              'image rank',rank,'delta',delta,'conductor exponent 2 on every branch')
    normal_chi = len(branches)
    print(' chi(O_normalization)=',normal_chi,
          '; chi(O_curve)=',normal_chi-delta,
          '; arithmetic genus=',1-normal_chi+delta)
    print(' conductor length on normalization=',2*len(branches),
          '; conductor quotient length=',2*len(branches)-delta)
print('Both reduced planar cubics have arithmetic genus 1 and dualizing O(3-3)=O.')
