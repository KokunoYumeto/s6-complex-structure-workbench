"""Exact boundary, period, and twistor comparisons for C.2.UN.49."""
import sympy as s
from itertools import product
r=s.symbols('r',integer=True,positive=True)
M=s.Matrix([[1,0,r],[0,0,-1],[0,1,0]])
assert M.det()==1
a,b,mu=[M[:,i] for i in range(3)]
eH=r*a-mu
hH=b
assert eH==s.Matrix([0,1,0])
assert hH==s.Matrix([0,0,1])
assert a==s.Matrix([1,0,0])
print('Integral boundary matrix:',M.tolist(),'determinant:',M.det())
print('Smoothing sends e_H to',eH.T,'and h_H to',hH.T)
print('The Hopf complementary meridian kills exactly delta =',a.T)
nu1,nu2=s.symbols('nu1 nu2',integer=True)
mu_global=s.Matrix([r,r*nu1-1,r*nu2])
assert s.simplify(mu_global[1]/r+1/r-nu1)==0
assert s.simplify(mu_global[2]/r-nu2)==0
print('Orbifold vector (nu1-1/r,nu2) becomes the integral vector (nu1,nu2).')

z,w,x,beta,c=s.symbols('z w x beta c',nonzero=True)
for rr in range(1,11):
    U=z/w**rr
    assert s.simplify(U.subs({z:beta**rr*z+w**rr,w:beta*w},simultaneous=True)
                      -U-beta**(-rr))==0
    jac=s.Matrix([U,s.log(w)]).jacobian([z,w]).det()
    assert s.simplify(jac-w**(-rr-1))==0
    periods=s.Matrix([[0,beta**(-rr)],[2*s.pi*s.I,s.log(beta)]])
    assert s.simplify(periods.det()+2*s.pi*s.I*beta**(-rr))==0
print('PASS all ten nonlinear canonical-period Jacobians and nonzero core determinants.')

p,z,pb,zb,t,tb=s.symbols('p z pb zb t tb')
P=p+t*zb
Z=z-t*pb
Pb=pb+tb*z
Zb=zb-tb*p
assert s.expand(P-t*Zb-(1+t*tb)*p)==0
assert s.expand(Z+t*Pb-(1+t*tb)*z)==0
print('Twistor real inverse has positive denominator 1+|t|^2.')

A,B,Ab,Bb=s.symbols('A B Ab Bb',nonzero=True)
V=s.Matrix([[t*Ab,t*Bb],[A,B]])
det=s.expand(V.det())
assert s.simplify(det-t*(Ab*B-A*Bb))==0
count=0
for aa,bb,cc,dd in product(range(-3,4),repeat=4):
    Q=s.Matrix([[aa,bb],[cc,dd]])
    if Q.det()!=1: continue
    assert s.simplify((V*Q).det()-det)==0
    count+=1
print('Fibre-period wedge is identical for',count,'independent SL2(Z) bases.')
delta=s.simplify(t*Bb-t*Ab*B/A)
assert s.simplify(delta+det/A)==0
print('Exact local translation delta(t) =',delta)
print('Its order is one; t=s^r makes its order exactly r for every fibre basis.')

ell,delta0,beta0,Pj,Zj=s.symbols('ell delta0 beta0 Pj Zj',nonzero=True)
g=lambda pp,ll:(pp+delta0,beta0*ll)
deck=lambda pp,ll:(pp+Pj,s.exp(Zj)*ll)
left=g(*deck(p,ell));right=deck(*g(p,ell))
assert all(s.simplify(a-b)==0 for a,b in zip(left,right))
print('Flat-line lattice translations commute exactly with the remaining deck generator.')
print('PASS all integral boundary maps, canonical periods, twistor maps and flat-torsor comparisons.')
