#!/usr/bin/env python3
"""Exact symbolic checks for C.7.11; no numerical sampling or grid."""
import sympy as s

z,w,om,omb,k,u,D,a,ac,al,alb,X,Xc,s2,s2c=s.symbols('z w omega omega_bar k u D a a_bar alpha alpha_bar X X_bar s2 s2_bar')
automorphy=k*(omb*(z+om/2)+om*(w+omb/2)-((z+om)*(w+omb)-z*w))
assert s.expand(automorphy)==0
print('Paired-lattice automorphy residual:',s.expand(automorphy))
gradient=s.Matrix([alb*D+a-k*alb*u, al*D+ac-k*al*u])
V=s.Matrix([al,-alb])
first=s.expand((V.T*gradient)[0])
assert first==al*a-alb*ac
print('Cancelling first logarithmic jet:',first)
hessian=s.Matrix([[-X-s2,-k],[-k,-Xc-s2c]])
second=s.expand((V.T*hessian*V)[0])
expected=-al**2*(X+s2)-alb**2*(Xc+s2c)+2*al*alb*k
assert s.expand(second-expected)==0
print('Second logarithmic jet:',second)
ratio=s.expand(4*first**2+2*second)
atQ=s.simplify(ratio.subs({al:1,alb:1,a:0,ac:0,X:4,Xc:4,s2:-2,s2c:-2}))
assert atQ==4*k-8
print('V^2 H/H at Q:',atQ)
lam=s.symbols('lambda',nonnegative=True)
left=(3-1)*4
right=3*2+2*3*(2-1)*(lam+1)
print('Waldschmidt Theorem 1: left=',left,'right=',s.expand(right))
print('Strict-inequality margin:',s.expand(left-right))
print('Packing lower exponent:',s.Rational(4,2)-1)
print('All symbolic identities passed.')
