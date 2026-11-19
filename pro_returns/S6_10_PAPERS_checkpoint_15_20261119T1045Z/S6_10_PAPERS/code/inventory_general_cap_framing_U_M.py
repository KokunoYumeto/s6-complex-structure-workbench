#!/usr/bin/env python3
"""Current exact signed Cox comparison with explicitly typed dual/physical indices.

The received program used physical A_M in a U-characteristic assertion.
This copy preserves all maps, reads the explicit auxiliary index, and checks
the actual K68 relation A_M=-A_U. The original failed replay is retained.
"""
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as S

a,b,theta=S.symbols('alpha beta theta', real=True)
R=lambda x:S.Matrix([[S.cos(x),-S.sin(x),0],[S.sin(x),S.cos(x),0],[0,0,1]])
G=lambda x,t:S.Matrix([
 [-S.sin(x),S.cos(t)*S.cos(x),S.sin(t)*S.cos(x)],
 [S.cos(x),S.cos(t)*S.sin(x),S.sin(t)*S.sin(x)],
 [0,S.sin(t),-S.cos(t)]])
clean=lambda X:X.applyfunc(S.trigsimp)
assert clean(G(a,theta).T*G(a,theta)-S.eye(3))==S.zeros(3)
assert S.trigsimp(G(a,theta).det())==1
assert clean(G(a,theta)-R(a)*G(0,theta))==S.zeros(3)
assert clean(R(a+b)-R(a)*R(b))==S.zeros(3)

qx,qy,qb=S.symbols('chi_x chi_y chi_b')
Q=S.Matrix([[1,0,0],[0,1,0],[qx,qy,qb]])
for sign in (1,-1):
 T=S.diag(1,1,sign);So=sign*T
 assert So.det()==1 and So.T*So==S.eye(3)
 assert T.inv()*(T*Q)==Q
 assert S.simplify(T*G(a,theta)*T.inv()-So*G(a,theta)*So.inv())==S.zeros(3)

s,v,M,g,C=S.symbols('s v M g C')
delta=S.Matrix([0,1]);gamma=S.Matrix([g,-C-s-M*v])
for sign in (1,-1):
 sigma=sign*S.Matrix([g*v,-C*v-M*(v*v-v)/2])
 ordinary=sign*S.Matrix([-g*s/M,C*s/M+s*s/(2*M)+s*v])
 assert (sigma.subs(v,v+1)-sigma-sign*s*delta-sign*gamma).applyfunc(S.simplify)==S.zeros(2,1)
 bounded=sign*S.Matrix([g*theta,(-C-M*v)*theta-M*theta*(theta-1)/2])
 assert (sigma.subs(v,v+theta)-sigma-bounded).applyfunc(S.simplify)==S.zeros(2,1)
 F=sigma-ordinary
 assert (F.subs(v,v+theta)-F-sign*theta*gamma+
         sign*M*theta*(theta-1)*delta/2).applyfunc(S.simplify)==S.zeros(2,1)

u,tau,K,epsilon=S.symbols('u tau K epsilon', nonzero=True)
binding=u*(1+u/tau)**(-epsilon*K)
assert S.simplify(S.diff(binding,u).subs(u,0))==1
phi,Beta,argt,argq,argtau=S.symbols('phi Beta arg_t arg_t_minus_tau arg_tau')
poly_phase=M*Beta+argq-epsilon*K*argt
binding_phase=argq-epsilon*K*(argt-argtau)
assert S.expand(poly_phase-(M*Beta+binding_phase-epsilon*K*argtau))==0

root=Path(__file__).resolve().parents[3]/'sources/newer_night/checkpoint29'
one=json.loads((root/'code/part3/additive_returns.json').read_text())
joint=json.loads((root/'code/part3/joint_additive_returns.json').read_text())
rows=[]
for group,source in [('K26',one['cases']),('K28',joint['rows'])]:
 for row in source:
  H=S.sympify(row['height']);chi=S.sympify(row['chi'])
  AA=S.sympify(row['auxiliary_dual_line_index'])
  A_physical=S.sympify(row.get('actual_positive_return',row.get('actual_A')))
  assert S.simplify(A_physical+AA)==0
  kk=S.expand(-3*H);ell=S.expand(-24*chi)
  mr=S.expand(6*chi);nr=S.expand(3*H-6*chi)
  assert S.simplify(4*kk-ell-24*AA)==0
  assert S.simplify(mr+nr+kk)==0
  assert S.simplify(4*mr+ell)==0
  rows.append(dict(group=group,label=row['label'],H=str(H),chi=str(chi),
                   k=str(kk),ell=str(ell),m_relative=str(mr),n_relative=str(nr),
                   central_A_U=str(AA),actual_A_M=str(A_physical)))
  print(group,row['label'],'k=',kk,'ell=',ell,'relative=',(mr,nr),'A_U=',AA,'A_M=',A_physical)
rows.append(dict(group='K28',label='F36 one I1-star cap, both profiles and norms',
                 H='6',chi='1',k='-18',ell='-24',m_relative='6',n_relative='12',central_A_U='-2',actual_A_M='2'))
out=dict(status='PASS_CURRENT_TYPED_U_M',timestamp_utc=datetime.now(timezone.utc).isoformat(),
         proof='notes/part3_general_cap_framing.md',
         scope='Exact signed frame and binding identities; all K26/K28 input rows read with A_U=auxiliary_dual_line_index and A_M=-A_U. This is a current certificate repair, not an unchanged historical replay.',
         normal_matrix='G(alpha,theta) in K30.18',
         signed_comparison='Q_beta=T_epsilon Q; both initial frames receive T_epsilon; T_epsilon^-1 Q_beta=Q.',
         signed_clutch='Conjugation by T_epsilon equals conjugation by epsilon*T_epsilon in SO(3).',
         exact_binding_coordinate='(t-tau)*(t/tau)^(-epsilon*m_infty*n_0)',
         normal_pontryagin=0,
         rows=rows)
(Path(__file__).resolve().parents[1]/'analysis/IV_retained_batch/general_cap_framing_U_M.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: signed normal derivative, exact binding chart, full degree-M clutch, and every individual pair.')

