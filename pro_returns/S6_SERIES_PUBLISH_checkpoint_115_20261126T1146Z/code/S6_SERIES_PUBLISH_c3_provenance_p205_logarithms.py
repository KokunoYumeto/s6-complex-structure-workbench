#!/usr/bin/env python3
"""Exact limiting-period determinants in the exposed P205 proof."""
import sympy as s

epsilon,y=s.symbols('epsilon y', real=True)
I=s.I
infinity=s.Matrix([[0,0,-1,I],[1,-I,0,0]])
def twistor(z):
    return s.Matrix([[1,I,-z,I*z],[z,-I*z,1,I]])
nilpotents=[]
for row,col,value in [(2,3,-2*epsilon),(3,1,-2*epsilon),(2,1,epsilon**2)]:
    n=s.zeros(4);n[row,col]=value
    nilpotents.append(n)
expected=[4*(1+2*epsilon*y),16*(1+2*epsilon*y),16*(1+epsilon**2*y)]
for frame,n,value in zip([infinity,twistor(I),twistor(-1)],nilpotents,expected):
    periods=frame*(s.eye(4)+I*y*n)
    determinant=s.factor(periods.col_join(s.conjugate(periods)).det())
    assert s.expand(determinant-value)==0
    print(determinant)
print('Three limiting determinants verified exactly; no uniform analytic transversality or compact-occurrence claim follows from arithmetic alone.')
