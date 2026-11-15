"""Exact small identities and edge cases used in Part A; no numerical cutoff proof."""
import sympy as s
from math import isqrt
D=s.diag(1,-3,-18)
M=s.Matrix([[17,0,72],[0,1,0],[4,0,17]])
assert M.det()==1 and M.T*D*M==D
assert M.inv()==s.Matrix([[17,0,-72],[0,1,0],[-4,0,17]])
assert {((a*a-3*b*b)%3) for a in range(3) for b in range(3)}=={0,1}
print('integral isometry, inverse, and norm-mod-3 obstruction PASS')
a,b,n=s.symbols('a b n',integer=True)
x,y,z=s.symbols('x y z',integer=True)
assert s.expand((x+y+4*z)**2-3*(y-x)**2-18*z*z-2*(4*(x*y+x*z+y*z)-x*x-y*y-z*z))==0
print('original quadratic-form identity PASS')
for v in [(4,0,1),(17,1,4)]:
 S,T,Z=v;assert S*S-3*T*T-18*Z*Z==-2 and T>=0 and 0<S and 4*S<=17*Z and S-4*Z<=T
print('two strict-wall exceptions PASS')
# The reduced norm-minus-two Pell seed in Q(sqrt(2)) is (0,1).
# alpha in [sqrt(2), (3+2sqrt(2))*sqrt(2)) forces 0<=a<4.
seeds=[]
for a in range(4):
 for b in range(1,4):
  if a*a-2*b*b==-2:seeds.append((a,b))
assert seeds==[(0,1)]
print('t=0 endpoint Pell reduction seed',seeds,'PASS')
# Upper arc endpoint would give 144*k^2=9*z^2-1; compare mod 9.
assert all((144*k*k-9*z*z+1)%9!=0 for k in range(9) for z in range(9))
print('upper arc endpoint impossible modulo 9 PASS')
