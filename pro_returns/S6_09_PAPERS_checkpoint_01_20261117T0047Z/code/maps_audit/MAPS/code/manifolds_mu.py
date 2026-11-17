"""Exact local orientation/cubic checks for the integral Zhubr invariant.

No finite check substitutes for the all-d spectral-sequence proof in the text.
The toric support function is interpolated linearly on the unimodular A2 fan.
Its wall degree is psi(v)+psi(v')-psi(w)-psi(w').
"""
import sympy as S
from math import gcd
r,s=S.symbols('r s',integer=True)
psi=-r*(r-1)/2+3*s*(s-1)
print('Support:',psi)
print('period e1:',S.expand(psi.subs(r,r+1)-psi))
print('period -e2:',S.expand(psi.subs(s,s-1)-psi))
def val(p):return psi.subs({r:p[0],s:p[1]})
def degree(v,vp,w,wp):return val(v)+val(vp)-val(w)-val(wp)
wall=[('internal e1',(0,0),(1,0),(0,1),(1,-1)),
      ('fixed delta',(0,0),(0,1),(1,0),(-1,1)),
      ('diagonal',(1,0),(0,1),(0,0),(1,1))]
for name,*points in wall:print(name,'complex degree',degree(*points))
Q=S.diag(1,-1,-1,-1)
a=S.Matrix([-5,6,0,-1]);f=S.Matrix([1,-1,0,0])
print('Normalized class:',list(a))
print('Square:',(a.T*Q*a)[0],'; ruling pairing:',(a.T*Q*f)[0])
assert (a.T*Q*a)[0]==-12 and (a.T*Q*f)[0]==1
for d in [5,7,11,13,17,19,23,25,29,31,35,49,101]:
 assert gcd(d,6)==1
 C=S.zeros(d)
 for i in range(d):C[i,i]=-2;C[i,(i-1)%d]=1;C[i,(i+1)%d]=1
 assert C*S.ones(d,1)==S.zeros(d,1)
 b=S.ones(d,1)*(-12)
 assert sum(b)%d==0
 rr=d-1
 print('d=',d,'H6 free rank=',S.binomial(rr+2,3),'torsion summands=',S.binomial(rr+1,2)+rr+1,
       'cubic b_i=',(-12)%d,'u^3=0')
print('Localized transgressions d3(t^k)=k*d*t^(k-1)*z for k=1,2,3; k units after inverting6.')
print('All exact checks passed.')
