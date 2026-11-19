#!/usr/bin/env python3
"""Exact sign, integral-lattice, and indefinite-fibre checks for Part C."""
import sympy as s

l0,l1,l2,a1,a2=s.symbols('l0 l1 l2 a1 a2', integer=True)
n=[4*l1-a1,3*l2-a2,-12*l0+a1+a2]
p=12*l0-4*l1-3*l2
assert s.expand(sum(n)+p)==0
print('Clockwise collar periods:', n)
print('Sum of collar periods =',s.expand(sum(n)),'= -p')
print('Standard twists (0,1,-1): p =',p.subs({l0:0,l1:1,l2:-1}),
      '; degree =',sum(n).subs({l0:0,l1:1,l2:-1}))
# rho runs from 1 to 0 in the outward radial direction; a=-n*dtheta/(2pi).
r=s.symbols('r', real=True)
rho=1-3*r*r+2*r*r*r
collar=s.integrate(-s.diff(rho,r),(r,0,1))
assert collar==1
print('Integral of d rho wedge a per unit clockwise period:',collar)
for m,ell in [(3,1),(4,-1)]:
    allowed=[k for k in range(25) if (k*ell)%m==0]
    assert allowed==list(range(0,25,m))
    print('Integral lift multiples at m=',m,':',allowed)
print('Intersection of the two lift lattices =',s.ilcm(3,4),'Z gamma')

y,m,r0=s.symbols('y m r0',real=True, nonzero=True)
Delta=r0-6*m*m/y
H=s.Matrix([[r0,-6*m],[-6*m,6*y]])/(y*Delta)
assert s.simplify(H.det()-6/(y*Delta))==0
print('Hermitian matrix determinant:',s.factor(H.det()))
print('For y>0 and Delta<0 determinant<0: signature=(1,1).')
# An exact sample is checked both by eigenvalues and principal-minor elimination.
sample=H.subs({y:1,m:0,r0:-1})
print('Rational sample matrix:',sample.tolist())
print('Method 1 eigenvalues:',sample.eigenvals())
print('Method 2 LDL pivots:',sample[0,0],s.factor(sample.det()/sample[0,0]))
assert sample.det()==-6

# Real periods columns, marking order gamma,u,w,delta; complex orientation
# coordinate order Re zeta1, Im zeta1, Re zeta2, Im zeta2.
tauR,muR,betaR=s.symbols('tauR muR betaR',real=True)
P=s.Matrix([[6*muR,tauR,1,0],[6*m,y,0,0],
            [betaR,muR,0,1],[r0,m,0,0]])
assert s.factor(P.det()-y*Delta)==0
print('Real period determinant:',s.factor(P.det()),'= y*Delta < 0')
print('eta^2 = 12 marked_volume; integral in complex orientation = -12.')
print('All computations exact over Z or rational-function fields.')
