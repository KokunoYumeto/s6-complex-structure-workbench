"""Exhaustive bounded search for integral rank-one bending families.

Use u,v in {-1,0,1}^5, both nonzero, with v.u=0, so I+t*u*v
is unimodular for every integer t. Conjugate the order-four B by
that shear, keep A fixed, and test maximal square-zero cusp.
The entries of (A B(t)-I)^2 have degree <=4 in t, so tests at
five distinct integer values certify the identity for all t.
All arithmetic below is exact int64, with a conservative entry
bound stated and checked before multiplication.
"""
from itertools import product
import numpy as np
from sympy import Matrix, symbols, eye, factor

A=np.array([[1,-1,-1,1,0],[1,0,-1,0,0],
            [2,-1,-1,0,1],[2,0,-1,0,0],[1,1,-1,0,0]],dtype=np.int64)
B=np.array([[0,-1,0,1,0],[0,-1,0,0,1],
            [0,-1,0,0,0],[1,-1,0,0,0],[0,-1,1,0,0]],dtype=np.int64)
I=np.eye(5,dtype=np.int64)
assert np.array_equal(np.linalg.matrix_power(A,5),I)
assert np.array_equal(np.linalg.matrix_power(B,4),I)
assert not np.any((A@B-I)@(A@B-I))
vectors=[np.array(u,dtype=np.int64) for u in product([-1,0,1],repeat=5) if any(u)]
count=valid=nonconstant=0;examples=[]
def invariants(T):
    return (int(np.trace(A@A@T@T)),int(np.trace(A@A@A@T@T)),
            int(np.trace(A@T@A@T@T)),int(np.trace(A@A@T@A@T@T)))
for u in vectors:
 for v in vectors:
  if int(v@u):continue
  count+=1;H=np.outer(u,v);seen=[];good=True
  for t in [1,-1,2,-2,0]:
   T=(I+t*H)@B@(I-t*H);N=A@T-I
   # Bounds here are far below 2^63: each N entry <=400, and
   # every tested square entry <=5*400^2. Trace words use at
   # most six matrices with entries <=100, still <2^63.
   assert np.max(np.abs(N))<=400 and np.max(np.abs(T))<=100
   if np.any(N@N):good=False;break
   seen.append(invariants(T))
  if not good:continue
  valid+=1
  if len(set(seen))>1:
   nonconstant+=1
   if len(examples)<4:examples.append((u.tolist(),v.tolist(),seen))
print('nonzero vectors in cube',len(vectors),'orthogonal ordered pairs tested',count)
print('certified square-zero polynomial families',valid,'with varying trace certificates',nonconstant)
for u,v,traces in examples:
 t=symbols('t');AA=Matrix(A.tolist());BB=Matrix(B.tolist());H=Matrix(u)*Matrix([v])
 T=(eye(5)+t*H)*BB*(eye(5)-t*H)
 assert (AA*T-eye(5))**2==Matrix.zeros(5)
 print('u',u,'v',v,'traces at 1,-1,2,-2,0',traces)
 print('trace A2 B(t)2',factor((AA**2*T**2).trace()))
 print('trace A3 B(t)2',factor((AA**3*T**2).trace()))
 print('trace A B(t) A B(t)2',factor((AA*T*AA*T**2).trace()))
 print('trace A2 B(t) A B(t)2',factor((AA**2*T*AA*T**2).trace()))
 print('symbolic finite and cusp identities checked exactly')
print('No conclusion beyond this complete cube search is asserted if no varying trace is found.')
