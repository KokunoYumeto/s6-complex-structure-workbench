"""Small exact integral-lattice utilities for fresh K111 endpoint atlases."""
from fractions import Fraction as F
from functools import reduce
from itertools import combinations
from math import gcd

def det3(a,b,c):
 return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def matrix(c):return tuple(tuple(v[i] for v in c) for i in range(4))
def adj(c):
 B=matrix(c)
 return tuple(tuple((-1)**(i+j)*det3(*(tuple(B[r][k] for k in range(4) if k!=i) for r in range(4) if r!=j)) for j in range(4)) for i in range(4))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def det(c):return dot(adj(c)[0],c[0])
def orient(c):
 c=tuple(tuple(v) for v in c)
 return c if det(c)>0 else (c[1],c[0],*c[2:])
def bary(c,v):
 d=det(c);return tuple(F(dot(r,v),d) for r in adj(c))
def inverse(c):
 d=det(c);return tuple(tuple(F(x,d) for x in row) for row in adj(c))
def mv(A,v):return tuple(dot(r,v) for r in A)
def mm(A,B):return tuple(tuple(dot(r,c) for c in zip(*B)) for r in A)
def prim(v):
 d=reduce(gcd,map(abs,v));return tuple(x//d for x in v)
def volume(c):return F(abs(det(c)),6*reduce(lambda a,b:a*b,(v[2]+v[3] for v in c),1))
def facets(c):return [tuple(sorted(x)) for x in combinations(c,3)]
def serial(x):
 if isinstance(x,F):return int(x) if x.denominator==1 else str(x)
 if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [serial(v) for v in x]
 return x
