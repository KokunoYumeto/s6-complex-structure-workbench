"""Exact algebra in the period coordinates of the prompt. No float arithmetic."""
import sympy as S
from pathlib import Path

s,v,m,n,mu,C,l0,l1,l2=S.symbols('s v m n mu C l0 l1 l2')
p=12*l0-4*l1-3*l2
a=-p
gamma=S.Matrix([6*mu,C-s-12*v])
delta=S.Matrix([0,1])
F=S.Matrix([mu*(s+12*v)/2,C*(s+12*v)/12-(s+12*v)**2/24+6*v])
print('F =',F.T)
print('F(s+12m,v)-F =',S.simplify(F.subs(s,s+12*m)-F).T)
print('F(s,v+n)-F =',S.simplify(F.subs(v,v+n)-F).T)
assert S.simplify(F.subs(s,s+12*m)-F-m*gamma+6*m*m*delta)==S.zeros(2,1)
assert S.simplify(F.subs(v,v+n)-F-n*gamma+6*n*(n-1)*delta)==S.zeros(2,1)
print('Q-loop exact: m*gamma - 6*m^2*delta')
print('r-loop exact: n*gamma - 6*n*(n-1)*delta')
print('p(default 0,1,-1) =',p.subs({l0:0,l1:1,l2:-1}))
print('The supplied F has +n gamma modulo delta; p*n has -n gamma for the supplied default.')

zg=S.Matrix([6*s*mu,-s*(s+1)/2+s*(C-12*v)])
assert S.simplify(zg.subs(s,s+1)-zg-gamma.subs(s,s+1))==S.zeros(2,1)
assert S.simplify(zg.subs(v,v+1)-zg+12*s*delta)==S.zeros(2,1)
print('collar generator z_gamma =',zg.T)
print('collar radial difference =',S.simplify(zg.subs(v,v+1)-zg).T)
print('total coefficient from finite logarithmic gluings and collar =',a)
print('member (0,2,-1): p,a =',p.subs({l0:0,l1:2,l2:-1}),a.subs({l0:0,l1:2,l2:-1}))

A1=S.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
print('Ai invariants modulo delta:',(A1[:3,:3]-S.eye(3)).col_join(A2[:3,:3]-S.eye(3)).nullspace())
E=S.zeros(4);E[3,0]=1
R=S.eye(4)-12*E
Kq=S.Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
for A in [A1,A2,Kq]: assert R*A==A*R
print('positive r period-column change =',R.tolist())
print('positive q period-column change =',Kq.tolist())
print('All printed polynomial identities verified exactly.')
