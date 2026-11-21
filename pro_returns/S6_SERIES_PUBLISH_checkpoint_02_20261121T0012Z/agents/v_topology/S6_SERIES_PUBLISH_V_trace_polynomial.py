#!/usr/bin/env python3
"""Exact degree-bounded interpolation check of F.CN3, with integer arrays."""
import json
import sympy as sp
from datetime import datetime,timezone

def mul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def trace(A):return sum(A[i][i] for i in range(len(A)))
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def add(A,B):return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]

A=[[int(i==(j+1)%5) for j in range(5)] for i in range(5)]
values=[]
for v in range(5):
    q=v*v-v+1
    X=[[int(i==0),int(i==2)+v*int(i==4)] for i in range(5)]
    Y=[[0,-q,-v*v,-1,v],[0,1-v*q,-v*q,v*v-v,q]]
    N=mul(X,Y)
    C=mul(add(eye(5),N),A)
    # The six-dimensional upper-triangular extension contributes one
    # additional eigenvalue one to the trace of A_v B_v^{-1}.
    values.append((v,1+trace(mul(A,C))))

v=sp.Symbol('v')
polynomial=sp.expand(sp.interpolate(values,v))
claimed=-v**4+v**3-v**2+2
assert polynomial==claimed
difference=sp.expand(polynomial.subs(v,v+1)-polynomial)
assert difference==-4*v**3-3*v**2-3*v-1
print(json.dumps({'computed_utc':datetime.now(timezone.utc).isoformat(),
 'method':'Exact interpolation from five integer-array trace evaluations. Every entry of X has degree at most one and every entry of Y degree at most three, so 1+trace(A(I+XY)A) has degree at most four; five distinct values certify equality.',
 'sample_values':values,'trace_polynomial':str(polynomial),'successive_difference':str(difference),
 'marked_homology_word':'trace(M1*M2^3)=trace(A_v*B_v^{-1})=1+trace(A*C)',
 'trace_transport':'M1=A_v^t, M2=B_v^t, B_v^4=I; transpose and cyclic trace identity give the equality. The rank-five quotient and one-dimensional diagonal block give the final equality.',
 'strictly_decreasing_for_nonnegative_integer_parameter':True},indent=2))
