"""Exact diagnostics for the uninput general analytic completion attempt.

This checks symbolic identities used in E_B_general_completion_attempt.md.
It does not assert an origin completion or nonexistence theorem.
"""
from pathlib import Path
import json
import sympy as S

a1,b1,c1,d1,a2,b2,c2,d2=S.symbols('a1 b1 c1 d1 a2 b2 c2 d2')
mu,tau,C,s,v=S.symbols('mu tau C s v')
A1=6*a1*mu+b1*tau+c1
A2=6*a2*mu+b2*tau+c2
B1=a1*(C-s-12*v)+b1*mu+d1
B2=a2*(C-s-12*v)+b2*mu+d2
det=S.expand(A1*B2-A2*B1)
coeff_v=S.expand(det.coeff(v))
expected_v=12*((a1*b2-a2*b1)*tau+(a1*c2-a2*c1))
assert S.expand(coeff_v-expected_v)==0
remainder=S.expand(det.subs({a1:0,a2:0}))
expected_remainder=(b1*d2-b2*d1)*tau+(c1*b2-c2*b1)*mu+c1*d2-c2*d1
assert S.expand(remainder-expected_remainder)==0

I=S.eye(4)
Nq=S.zeros(4);Nq[2,1]=1;Nq[3,0]=-1
Nr=S.zeros(4);Nr[3,0]=-12
assert Nq**2==S.zeros(4) and Nr**2==S.zeros(4)
assert Nq*Nr==Nr*Nq==S.zeros(4)
assert (I+Nq)*(I+Nr)==(I+Nr)*(I+Nq)

F=S.Matrix([mu*(s+12*v)/2,C*(s+12*v)/12-(s+12*v)**2/24+6*v])
gamma=S.Matrix([6*mu,C-s-12*v]);delta=S.Matrix([0,1])
qdiff=S.simplify(F.subs(s,s+1)-F)
rdiff=S.simplify(F.subs(v,v+1)-F)
assert S.simplify(qdiff-gamma/12+delta/24)==S.zeros(2,1)
assert S.simplify(rdiff-gamma)==S.zeros(2,1)

kappa=S.symbols('kappa')
k=-s+12*kappa
sigma=S.Matrix([6*mu*v,-6*v**2+v*(C-12*kappa)])
G=S.Matrix([mu*s/2,C*s/12-s**2/24])
full_overlap=S.simplify(F-sigma-k*v*delta)
assert S.simplify(full_overlap-G-6*v*delta)==S.zeros(2,1)
assert S.simplify(full_overlap.subs(v,v+1)-full_overlap-6*delta)==S.zeros(2,1)
assert S.simplify(F.subs(s,s+12)-F-gamma+6*delta)==S.zeros(2,1)
n,m=S.symbols('n m',integer=True,positive=True)
assert S.simplify(F.subs(v,v+n)-F-n*gamma+6*n*(n-1)*delta)==S.zeros(2,1)
assert S.simplify(F.subs(s,s+12*m)-F-m*gamma+6*m**2*delta)==S.zeros(2,1)

# Exact face matrices for the sharp log-pairing diag(q,q+12r).
h,j=S.symbols('h j', nonnegative=True)
valuation=S.diag(h,h+12*j)
assert S.factor(valuation.det())==h*(h+12*j)
assert valuation.subs(h,0).nullspace()==[S.Matrix([1,0])]
log_a,log_qA,log_qrD=S.symbols('log_a log_qA log_qrD',real=True)
unit_matrix=S.Matrix([[log_qA,6*log_a],[-log_a,log_qrD]])
assert S.expand(unit_matrix.det())==log_qA*log_qrD+6*log_a**2

result={
 'status':'PASS',
 'v_coefficient':str(S.factor(coeff_v)),
 'zero_gamma_determinant':str(remainder),
 'linear_monodromies_commute':True,
 'Nq_square_zero':True,'Nr_square_zero':True,
 'affine_q_difference':str(qdiff),'affine_r_difference':str(rdiff),
 'actual_full_overlap':str(full_overlap),
 'actual_full_overlap_r_difference':'6 delta; no gamma-period obstruction from this raw overlap',
 'finite_root_r_difference':'n gamma - 6 n(n-1) delta; Y component n gamma',
 'finite_root_q_ghost_matrix':'diag(12m,12m), injective for m positive',
 'sharp_pairing_determinant':str(S.factor(valuation.det())),
 'ordinary_unit_pairing_determinant':str(S.expand(unit_matrix.det())),
 'scope':'Symbolic identities only. No numerical or existence claim for an origin cap.'
}
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result,indent=2)+'\n')
for key,value in result.items():print(f'{key}: {value}')
