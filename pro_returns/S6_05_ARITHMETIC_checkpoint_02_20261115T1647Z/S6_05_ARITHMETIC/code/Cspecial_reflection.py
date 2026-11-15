#!/usr/bin/env python3
import sympy as s
A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
H=s.Matrix([[1,0,0,0],[0,1,0,0],[-6,0,-1,0],[0,-1,0,-1]])
Id=s.eye(4); d=s.Matrix([0,0,0,1]); eps=s.Matrix([1,2,-4,0]); eps2=s.Matrix([1,3,-3,0]); E=d*s.Matrix([[1,0,0,0]])
assert H*H==Id
assert H*A2*H==A2.inv()
assert H*A1*H==A2.inv()*A1.inv()*A2
v1p=-A2*H*eps;v2p=H*eps2
print('v1prime=',list(v1p),'equals -eps+d:',v1p==-eps+d)
print('v2prime=',list(v2p),'equals eps2-3d:',v2p==eps2-3*d)
Hnorm=-Id+E
ells=[s.Matrix([0,0,-2,0]),s.Matrix([0,2,0,0])]
for A,m,v,vp,ell in zip([A1,A2],[3,4],[eps,-eps2],[v1p,v2p],ells):
 N=sum((A**k for k in range(m)),s.zeros(4))
 diff=v-Hnorm*vp
 assert N*ell==-diff
 r=s.linsolve((Id-A,diff/m+ell)); print('m=',m,'diff=',list(diff),'ell=',list(ell),'translation solution=',r)
A0=(A1*A2).inv()
ell0=-A0*(ells[0]+A1*ells[1]);print('ell0=',list(ell0))
print('reflection identities verified exactly')
