"""Exact charts and cohomology arithmetic for C.2.UN.13."""
from math import comb
import sympy as s

r, u, v, R = s.symbols('r u v R')
a, b, z = r, r*u, r*v
quadrics = [a*a, a*b, a*z, b*b, b*z, z*z]
assert [s.expand(q).subs(r*r, R) for q in quadrics] == [R,R*u,R*v,R*u*u,R*u*v,R*v*v]
assert s.expand(z*z).subs(r*r,R) == R*v*v
assert s.det(s.Matrix([[s.diff(a,r),s.diff(a,u)],
                      [s.diff(b,r),s.diff(b,u)]])) == r
print('Quotient blowup chart: (a,b,s)=(r,ru,rv), R=r²; invariant quadrics and t=R v² verified.')
print('Surface canonical comparison: da wedge db = r dr wedge du = (1/2) dR wedge du.')

# -1 on A acts by (-1)^j on H^j(A); the P1 action is cohomologically trivial.
b_A = [comb(4,j) for j in range(5)]
b_X = [sum(b_A[j] for j in range(5)
           if j % 2 == 0 and k-j in (0,2)) for k in range(7)]
assert b_X == [1,0,7,0,7,0,1]
b_W = b_X.copy()
for k in (2,4):
    b_W[k] += 32
assert b_W == [1,0,39,0,39,0,1]

e = lambda ranks: sum((-1)**k*n for k,n in enumerate(ranks))
assert e(b_X) == 16 and e(b_W) == 80
e_Aquot = sum(b_A[j] for j in range(0,5,2))
e_K3 = e_Aquot + 16*(2-1)
e_special = e_K3 + 16*3 - 16*2
assert e_K3 == 24 and e_special == 40
assert 2*e_special == e(b_W)

blocks_per_fibre = 20
blocks = 2*blocks_per_fibre
b_Y = b_W.copy()
for k,inc in [(2,2),(3,6),(4,2)]:
    b_Y[k] += blocks*inc
assert b_Y == [1,0,119,240,119,0,1]
assert e(b_Y) == 0
assert e_special-2*blocks_per_fibre == 0
assert 17+2*blocks_per_fibre == 57
hO = [1,0,1,0]
b_support_W = [1,0,22,0,17]
b_support_Y = b_support_W.copy()
for k,inc in [(2,2),(3,6),(4,2)]:
    b_support_Y[k] += blocks_per_fibre*inc
assert b_support_Y == [1,0,62,120,57]
assert e(b_support_W) == 40 and e(b_support_Y) == 0
print('Quotient invariant rational Betti ranks:',b_X)
print('Resolved compact model rational Betti ranks:',b_W,'; Euler',e(b_W))
print('Kummer surface Euler:',e_K3,'; each original special support Euler:',e_special)
print('Each special support: 2*K3 + sixteen P2; intersections are sixteen P1.')
print('A-Campo signature before balancing: a1=16, a2=24-16*2=-8; weighted sum zero.')
assert 16 + 2*(-8) == 0
print('Balanced compact model rational Betti ranks:',b_Y,'; Euler',e(b_Y))
print('Negative-two operations:',blocks,'; twenty on each of the two special fibres.')
print('Each balanced support: Euler 0, 57 components, original K3 unchanged.')
print('Original support rational cohomology ranks:',b_support_W)
print('Balanced support rational cohomology ranks:',b_support_Y)
print('Coherent support dimensions in both models:',[1,0,1])
print('Coherent cohomology dimensions for both smooth models:',hO)
print('All exact checks passed.')
