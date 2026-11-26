#!/usr/bin/env python3
"""Full anti-invariant extension-unit check for fresh LQ.
The earlier retained toric check set eta1=0. This source keeps it.
No target original or historical target program is read.
"""
from datetime import datetime, timezone
import sympy as S

print('START',datetime.now(timezone.utc).isoformat())
n,k,j,r,N,tau,l,w,z,B,eps,eta,F=S.symbols('n k j r N tau l w z B eps eta F')
m=2*k; q=n*k; R=2*r-j; t=(R+N*tau)/m
linear=S.Matrix([[-1,-1],[0,1]])
periods=[S.Matrix([1,0]),S.Matrix([-q*l-eps/2+B,-n/2+eps]),
         S.Matrix([0,1]),S.Matrix([-tau/2+eta,tau])]
shift={l:l+1/m,eps:-eps,eta:-eta}
shifted=[v.subs(shift,simultaneous=True) for v in periods]
wanted=[-shifted[0],-shifted[1]-n*shifted[2],shifted[2]-shifted[0],shifted[3]]
for name,a,b in zip(('alpha','beta','lambda','ell'),periods,wanted):
    assert (linear*a-b).applyfunc(S.simplify)==S.zeros(2,1)
    print('PERIOD PASS',name,'with both anti-invariant extension functions')
first=-z-w-j*l+F-N*eta/m
second=S.expand(-first-(w+t)-j*(l+1/m)+F+N*eta/m)
assert S.simplify(second-(z-t-j/m+2*N*eta/m))==0
assert S.simplify(k*(-t-j/m+2*N*eta/m)-(-r-N*tau/2+N*eta))==0
recovered=-first-w-j*l+F-N*eta/m
assert S.simplify(recovered-z)==0
print('POWER PASS exact two-step and m-step translations with eta1 retained')
print('INVERSE PASS exact holomorphic affine inverse')
# Exact finite-group homotopy: (T-I)sum j T^j=m I-Norm.
for order in range(2,25,2):
    v=S.Matrix(list(range(order)))
    shifted=S.Matrix([v[(i-1)%order] for i in range(order)])
    assert shifted-v==S.Matrix([order-1]+[-1]*(order-1))
print('GAUGE PASS finite cyclic coefficient identity for orders 2 through 24')
print('PASS',datetime.now(timezone.utc).isoformat())
