"""Independent exact cusp-height certificate, authored from the clean packet.

This code imports no inherited checker or stored symbolic answer.  The
analytic O(1) estimate is proved in the separate prereading derivation.
"""
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sympy as s

I = s.I
Cf = s.Matrix([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
Cg = s.Matrix([[0,0,0,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
D = Cf*Cg.inv()-s.eye(4)
d = s.Matrix([0,1,1,1])
assert D == d*s.Matrix([[1,0,0,0]])
assert D**2 == s.zeros(4)
pairs = list(combinations(range(4), 2))

def wedge(v, w):
    return s.Matrix([s.expand(v[i]*w[j]-v[j]*w[i]) for i,j in pairs])

std = [s.eye(4)[:,j] for j in range(4)]
E = s.Matrix.hstack(*(wedge(D*std[i],std[j])+wedge(std[i],D*std[j]) for i,j in pairs))
q_inv = s.ones(6,1)
Q = s.eye(6)
Q[:,0] = q_inv
pi = Q.inv()[1:,:]
c = s.Matrix([[1,-1,1,1,-1,1]])
NV = s.Matrix([[0,0,0,-1,1,-1], [0,0,0,0,0,0], [0,0,0,0,0,0],
               [0,1,0,0,0,0], [0,0,1,0,0,0], [0,-1,1,0,0,0]])
NW = NV[1:,1:]
n = NV[0:1,1:]
assert E*q_inv == s.zeros(6,1)
assert E**2 == s.zeros(6)
assert pi*E == NW*pi
assert NW**2 == s.zeros(5)
assert n*NW == s.zeros(1,5)
assert NV**2 == s.zeros(6)
assert (c*q_inv)[0] == 2
assert 2*(q_inv[0]*q_inv[5]-q_inv[1]*q_inv[4]+q_inv[2]*q_inv[3]) == 2
assert Q.det() == 1

ar = s.symbols('ar0:4', real=True)
ai = s.symbols('ai0:4', real=True)
a = s.Matrix([ar[j]+I*ai[j] for j in range(4)])
abar = s.conjugate(a)
alpha = a[0]
norm_alpha = ar[0]**2+ai[0]**2
x,y = s.symbols('x y', real=True)
ss = x+I*y
u = (s.eye(4)+ss*D)*a
eta = I*wedge(u,s.conjugate(u))
r = s.simplify(pi*eta)
r0 = I*pi*wedge(a,abar)
p = pi*wedge(a,d)
A0 = (I*c*wedge(a,abar))[0]
A = (c*eta)[0]
assert s.expand((c*wedge(a,d))[0]-alpha) == 0
assert s.expand((n*p)[0]-alpha) == 0
assert s.simplify(s.conjugate(r)-r) == s.zeros(5,1)
assert s.expand(A-A0-2*y*norm_alpha) == 0
rcan = s.simplify((s.eye(5)-ss*NW)*r)
assert s.simplify(rcan-r0-2*y*s.conjugate(alpha)*p) == s.zeros(5,1)
assert s.simplify(n*rcan-n*r) == s.zeros(1,1)
assert s.expand((n*rcan)[0]-(n*r0)[0]-2*y*norm_alpha) == 0

# An arbitrary bounded functional on P extends locally to W.  Its ten real
# coefficient symbols check the assertion uniformly for all such splittings.
br = s.symbols('br0:5', real=True)
bi = s.symbols('bi0:5', real=True)
b = s.Matrix([[br[j]+I*bi[j] for j in range(5)]])
bc = s.expand((b*rcan)[0])
lift_can = s.Matrix([bc,*rcan])
lift_flat = s.simplify((s.eye(6)+ss*NV)*lift_can)
assert s.simplify(lift_flat[1:,:]-r) == s.zeros(5,1)
imag_top = s.expand((lift_flat[0]-s.conjugate(lift_flat[0]))/(2*I))
imag_bc = s.expand((bc-s.conjugate(bc))/(2*I))
target = imag_bc+y*(n*r0)[0]+2*y**2*norm_alpha
assert s.expand(imag_top-target) == 0
remainder_numerator = s.expand(imag_top-y*A)
assert s.expand(remainder_numerator-imag_bc-y*((n*r0)[0]-A0)) == 0
assert s.Poly(s.expand(A),y).degree() == 1
assert s.Poly(s.expand(imag_top),y).degree() == 2
assert s.Poly(remainder_numerator,y).degree() <= 1
assert s.expand(imag_top).coeff(x) == 0
assert s.expand(A).coeff(y,1) == 2*norm_alpha
assert s.expand(imag_top).coeff(y,2) == 2*norm_alpha

out = {
    'status':'all exact symbolic assertions passed',
    'D_rank':D.rank(), 'NV_rank':NV.rank(),
    'D_squared':0, 'NV_squared':0,
    'actual_quotient_identity':'pi E = NW pi',
    'A_leading_coefficient':'2*(ar0^2+ai0^2)',
    'height_numerator_leading_coefficient':'2*(ar0^2+ai0^2)',
    'height_numerator_degree_in_y':2,
    'height_minus_y_numerator_degree_in_y':s.Poly(remainder_numerator,y).degree(),
    'real_part_x_dependence':False,
    'splitting_scope':'arbitrary bounded canonical functional; all ten real coefficient symbols retained',
    'analytic_scope':'uniform h=y+O(1) follows from the written bounds and a0(0) nonzero, not from numerical sampling',
    'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
outpath = Path(__file__).with_suffix('.output.json')
outpath.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
