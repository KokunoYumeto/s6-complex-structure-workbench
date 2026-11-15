"""Exact arithmetic for the integral orthogonal group and its norm -2 orbits."""
from fractions import Fraction as F
from itertools import product
from math import gcd
import sympy as S
G=S.diag(1,-3,-18)
roots=[S.Matrix(x) for x in [(0,-1,0),(0,0,-1),(1,1,0),(9,3,2),(4,0,1)]]
refs=[S.eye(3)-2*r*(r.T*G)/(r.T*G*r)[0] for r in roots]
for r,A in zip(roots,refs):
 assert A.T*G*A==G and A.det()==-1 and all(x.q==1 for x in A)
 print('root',tuple(r),'norm',(r.T*G*r)[0],'reflection',A.tolist())
print('Coxeter Gram:',S.Matrix(5,5,lambda a,b:(roots[a].T*G*roots[b])[0]))
verts=[(F(0),F(0)),(F(1,3),F(0)),(F(1,3),F(1,6)),(F(1,9),F(2,9)),(F(0),F(2,9))]
print('Klein/projective polygon vertices:',verts)
print('vertex a^2:',[1/(1-3*u*u-18*v*v) for u,v in verts])
can=[]
for a,q,n in product(range(-5,6),range(-3,4),range(-1,2)):
 if a*a-3*q*q-18*n*n!=-2:continue
 values=[a-3*q*u-18*n*v for u,v in verts]
 if min(values)<=0<=max(values):can.append((a,q,n))
print('norm -2 normals whose geodesic meets polygon:',can)
adj={v:[] for v in can}
for v in can:
 for j,A in enumerate(refs):
  w=tuple(A*S.Matrix(v))
  if w in adj:adj[v].append((j,w))
seen=set();components=[]
for v in can:
 if v in seen:continue
 stack=[v];c=[];seen.add(v)
 while stack:
  w=stack.pop();c.append(w)
  for _,u in adj[w]:
   if u not in seen:seen.add(u);stack.append(u)
 components.append(sorted(c))
for c in components:
 div={gcd(gcd(abs(a),3*abs(q)),18*abs(n)) for a,q,n in c}
 print('component size',len(c),'divisibilities',div,'vertices',c)
assert len(components)==2
assert sorted({gcd(gcd(abs(c[0][0]),3*abs(c[0][1])),18*abs(c[0][2])) for c in components})==[1,2]
print('two orbits, representatives (1,1,0) and (4,0,1) PASS')
# Complete norm-one integer search inside the polygon, bounded by max vertex a²=27/2.
normone=[]
for a,q,n in product(range(1,4),range(4),range(2)):
 if a*a-3*q*q-18*n*n==1 and a>=3*q and a>=q+4*n and 2*a>=9*n:normone.append((a,q,n))
assert normone==[(1,0,0)];print('norm-one reduction endpoint',normone)
# Primitive translations of the three geodesics; their traces in SO(1,2)
# determine cosh(length)=(trace-1)/2.
for name,left,right in [('source g0',0,2),('norm -2 divisibility 1',1,3),('norm -2 divisibility 2',3,0)]:
 A=refs[left]*refs[right];print(name,'translation',A.tolist(),'cosh_length',S.factor((S.trace(A)-1)/2))
