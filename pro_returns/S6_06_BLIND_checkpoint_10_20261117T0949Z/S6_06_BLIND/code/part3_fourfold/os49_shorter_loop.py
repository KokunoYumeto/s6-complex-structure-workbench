#!/usr/bin/env python3
"""Exact endpoint cochains, component norms and origins for OS49 shortening.

The geometric proof and its closing-arrow convention are retained separately
in notes/part3_os49_shorter_loop_working.md; this is its algebraic certificate.
"""
from pathlib import Path
from datetime import datetime, timezone
import sympy as S
import json

ROOT=Path(__file__).resolve().parents[2]
I=S.eye(4)
TA=S.Matrix([[1,-3,-3,-1],[0,-2,-3,-1],[0,1,1,0],[0,0,0,1]])
TB=S.Matrix([[1,0,0,0],[0,1,1,0],[0,-1,0,0],[0,0,0,1]])
TC=S.Matrix([[1,0,3,1],[0,1,2,1],[0,0,1,0],[0,0,0,1]])
A,B,C=[T.inv().T for T in (TA,TB,TC)]
assert TA*TB*TC==I and A*B*C==I
gamma,u_hom,w,delta=[I[:,i] for i in range(4)]
# F26's displayed cohomology u has dual period -u in the positive Tate marking.
# This is checked, rather than dropped: C sends gamma by -3w-delta and
# the physical u=-u_hom by +2w+delta, exactly OC.3.
u=-u_hom
assert (C-I)*gamma==-3*w-delta
assert (C-I)*u==2*w+delta
K=3*u+2*gamma
H=-u-gamma
assert (C-I)*K==delta
n,k,v,D1,D2=S.symbols('n k v D1 D2',integer=True)
m=3*k
sigma=n*v*S.Matrix([D1,D2])+S.Matrix([0,n*m*v*(v-1)])
step=S.Rational(1,3)
tau=n*S.Matrix([D1,D2+2*m*v])/3
alpha=-2*n*m/9
assert S.simplify(sigma.subs(v,v+step)-sigma-tau-S.Matrix([0,alpha]))==S.zeros(2,1)
norm=sum((tau.subs(v,v+j*step)+S.Matrix([0,alpha]) for j in range(3)),S.zeros(2,1))
assert S.simplify(norm-n*S.Matrix([D1,D2+2*m*v]))==S.zeros(2,1)
u1,u2,gamma1,gamma2,Rlog,slog=S.symbols('u1 u2 gamma1 gamma2 Rlog slog')
u_log=S.Matrix([u1,u2]); gamma_log=S.Matrix([gamma1,gamma2]); delta_log=S.Matrix([0,1])
lift_log=(-gamma_log+m*v*delta_log-Rlog*delta_log)/3
g0_log=(-n*slog-2*n*Rlog)/3
bounded_log=n*u_log-2*n*lift_log+(2*n*k*v+g0_log)*delta_log
assert S.simplify(bounded_log-n*(3*u_log+2*gamma_log-slog*delta_log)/3)==S.zeros(2,1)
p=(-n*delta-n*(A-I)*K)/3
q=-n*(B-I)*K/3
assert p==n*w and q==-n*(u_hom+w)
assert p+A*q==S.zeros(4,1)
assert q==(B-I)*(n*u_hom)
assert k*(I+A+A**2)*p==-n*k*delta
assert -n*delta-3*p==n*(A-I)*K
assert -3*q==n*(B-I)*K
# Literal component graph defects, with j=0,1 as parity representatives.
ceilhalf=lambda j:(j+1)//2
component=[]
for j in [0,1]:
 forward=ceilhalf(j)-ceilhalf(j+1)
 triple=ceilhalf(j)-ceilhalf(j+3)
 inverse_B=ceilhalf(j)+1-ceilhalf(j+3)
 assert inverse_B-triple==1
 component.append(dict(parity=j,U=forward,U_cubed=triple,B_inverse=inverse_B,rho=1))
assert [a['U'] for a in component]==[-1,0]
assert [a['U_cubed'] for a in component]==[-2,-1]
e,j=S.symbols('e j',integer=True)
rho_cusp=1-3*e
g_cusp=S.expand((-n-2*n*rho_cusp)/3)
assert S.expand(g_cusp-2*n*e)==-n
root_e=m*(S.Rational(1,3)+j)
rho_cap=S.cancel(-3*root_e/m)
assert S.expand(rho_cap)==-1-3*j
root_g=S.expand(m*(n-2*n*rho_cap)/3)
assert S.expand(root_g-2*n*root_e)==m*n/3
assert S.expand((n+2*n)/3)==n
assert 3*alpha==-2*n*k
# All parameter phases in the third iterate are literal integer periods.
norm_phase=2*n*k*sum([S.Rational(0),S.Rational(1,3),S.Rational(2,3)])+3*alpha
assert S.simplify(norm_phase)==0
Sfan=S.symbols('S',integer=True)
short_k,short_ell=-2*k,-8*k
assert 3*short_k==-6*k and 3*short_ell==-24*k
short_A=S.simplify((4*short_k-short_ell)/24)
assert short_A==0
fan=S.factor(short_ell*(Sfan-1)/8-short_k*(Sfan**2-1)/8)
assert fan==k*(Sfan-3)*(Sfan-1)/4
odd_integer_form=S.factor(fan.subs(Sfan,2*j+1))
assert odd_integer_form==j*k*(j-1)
def mat(M):return [[str(S.simplify(x)) for x in M.row(i)] for i in range(M.rows)]
data=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS: exact algebraic certificate; geometric note awaiting root audit',
          A=mat(A),B=mat(B),C=mat(C),K=mat(K),H=mat(H),
          K_jumps={name:mat((D-I)*K) for name,D in [('A',A),('B',B),('C',C)]},
          integral_primitive={'finite':mat(p),'ordinary_II':mat(q),'finite_norm':mat(-n*k*delta)},
          component_defects=component,rho_cusp=str(rho_cusp),rho_cap=str(rho_cap),
          root_cap_residual_power=str(S.factor(root_g-2*n*root_e)),
          sigma=mat(sigma),tau=mat(tau),alpha=str(alpha),norm=mat(norm),
          retained_unit_logarithmic_cancellation=mat(bounded_log),
          closing_arrow='X_(zeta3 r) -> X_r; the forward deck is its inverse',
          norm_parameter_phase=str(norm_phase),
          short_pair=[str(short_k),str(short_ell)],short_index=str(short_A),
          fan_class=str(fan),integer_odd_S_form=str(odd_integer_form),
          k1_fan_residues=sorted({int(fan.subs({k:1,Sfan:s}))%28 for s in range(1,113,2)}))
(ROOT/'code/part3_fourfold/os49_shorter_loop.json').write_text(json.dumps(data,indent=2)+'\n')
with (ROOT/'records/literature_fourfold.md').open('a') as f:
 f.write('\n- '+data['utc']+' — Executed own OS49 shorter-loop certificate. Material: exact homology matrices, integral finite/ordinary endpoint primitive, component graph norms, rational divisor congruences, retained root power, typed closing arrow, third iterate and identical Cox origin; characteristic covering equations are integer identities. Geometric proof remains subject to root audit.\n')
print(json.dumps(data,indent=2))
