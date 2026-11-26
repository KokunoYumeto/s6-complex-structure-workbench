#!/usr/bin/env python3
"""Exact post-exposure 02LV support/character coordinate checks.

The oriented clutch and canonical fibre maps are proved in the receiver.
This script verifies their actual finite arrays and the all-integer
polynomial identities after writing r=8a+r0, s=2b+s0.
"""
from datetime import datetime, timezone
import sympy as S

print('START', datetime.now(timezone.utc).isoformat())
a, b, r0, s0 = S.symbols('a b r0 s0', integer=True)
r = 8*a+r0
psi = 4*a+3*r0*b
psi_l1 = 4*(a+1)+3*r0*(b-3)
psi_l2 = 4*(a+3)+3*r0*(b-8)
m = (r-4, S.Integer(-4))
k = (r0-a, 3*r0-1)
assert S.expand(-(psi_l1-psi)-m[0]-8*k[0]) == 0
assert S.expand(-(psi_l2-psi)-m[1]-8*k[1]) == 0
assert S.expand(m[0].subs(a,a+3)-m[0]) == 24
assert S.expand(k[0].subs(a,a+3)-k[0]) == -3
assert S.expand(m[1].subs(a,a+1)-m[1]) == 0
assert S.expand(k[1].subs(a,a+1)-k[1]) == 0
print('ALL_INTEGER_PERIOD_IDENTITIES', 'h=-Psi; m1=r-4,k1=r0-a; m2=-4,k2=3r0-1; cross discrepancy24+8*(-3)=0')

rays = ((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
def add(v,w): return (v[0]+w[0],v[1]+w[1])
def potential(v): return 4*(v[0]//8)+3*(v[0]%8)*(v[1]//2)
def wall(v,j):
    return (potential(v)+potential(add(v,rays[j]))
            -potential(add(v,rays[(j-1)%6]))
            -potential(add(v,rays[(j+1)%6])))
def lam(v): return -3*(v[0]%8)*(v[1]%2)
transport=[]
old_failures=[]
for rr in range(8):
    for ss in range(2):
        v=(rr,ss)
        for j,endpoint in ((0,(rr+1,ss-1)),(2,(rr-1,ss))):
            d=wall(v,j)
            difference=lam(v)-lam(endpoint)
            assert (difference-d)%8 == 0
            transport.append((v,endpoint,j,d%8,difference%8))
            if (-difference-d)%8:
                old_failures.append((v,endpoint,j,d%8,(-difference)%8))
assert len(transport)==32
assert old_failures
print('ALL32_ORBIT_TRANSITIONS', transport)
print('ORIGINAL_POSITIVE_CHARACTER_FAILURES', len(old_failures), old_failures)
assert wall((1,0),0)==6
assert lam((1,0))-lam((2,-1))==6

# Solve the literal three-ray character equations in the cone
# (v,v+e1,v+e2). Canonical positive divisor fibre weight is +m(delta).
raymat=S.Matrix([[1,1,0],[1,2,0],[1,1,1]])
lower=raymat.inv()*S.Matrix([1,0,0])
upper=raymat.inv()*S.Matrix([0,0,1])
assert lower[2]==-1 and upper[2]==1
print('POSITIVE_THOM_NORMAL_WEIGHTS', int(lower[2]), int(upper[2]), 'canonical fibre weight=+m(delta)')

L,V=S.symbols('L V',integer=True)
old_representatives=[]
fresh_representatives=[]
for rr in range(8):
    eps=4 if rr==0 else -4 if rr==7 else 0
    for ss in range(2):
        d=(eps if ss==0 else eps+3)
        old_representatives.append((d%8,lam((rr,ss)), -ss))
        fresh_representatives.append((d,lam((rr,ss)), 1-ss))
def values(rows):
    return [S.expand(-3*sum(d*(l+L)**2 for d,l,w in rows)),
            S.expand(-2*sum(d*(l+L)*(w+V) for d,l,w in rows)),
            S.expand(-sum(d*(w+V)**2 for d,l,w in rows))]
old=values(old_representatives)
fresh=values(fresh_representatives)
for val,mod in zip(old,(8,16,8)):
    assert all(c%mod==0 for c in S.Poly(val,L,V).coeffs())
for val,mod in zip(fresh,(8,16,8)):
    assert all(c%mod==0 for c in S.Poly(val,L,V).coeffs())
print('CORRECTED_OLD_DEGREE_REPRESENTATIVES',old)
print('FRESH_DEGREE_AND_Y_CHARACTER_REPRESENTATIVES',fresh)
print('Y_CHARACTER_MAP', '(0,-1)+(1,1)=(1,0); inverse subtracts the one common character')

C=S.Matrix([[8,24],[-6,-16]])
T=S.Matrix([[1,3],[-3,-8]])
Ti=S.Matrix([[-8,-3],[3,1]])
assert T*Ti==Ti*T==S.eye(2)
assert C==S.diag(8,2)*T
print('PERIOD_LATTICE_MAP',T.tolist(),'INVERSE',Ti.tolist(),'C=diag(8,2)T')
print('END',datetime.now(timezone.utc).isoformat())
