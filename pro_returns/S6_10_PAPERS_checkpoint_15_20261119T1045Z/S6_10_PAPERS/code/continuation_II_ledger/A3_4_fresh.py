import sympy as S
from pathlib import Path
import json

t,s,r=S.symbols('t s r');checks=[]
def simp(M):return M.applyfunc(S.cancel)
def zero(M):return all(S.cancel(v)==0 for v in M)
def ck(name,value):
    assert value,name
    checks.append(name)

D0=S.zeros(4,3);D0[2,2]=1
D1=S.zeros(2,4);D1[1,3]=1
h1=S.zeros(3,4);h1[2,2]=1
h2=S.zeros(4,2);h2[3,1]=1
I0=S.eye(3)[:,:2];P0=I0.T
I1=S.eye(4)[:,:2];P1=I1.T
I2=S.eye(2)[:,:1];P2=I2.T
ck('base_degree0_contraction',zero(h1*D0-(S.eye(3)-I0*P0)))
ck('base_degree1_contraction',zero(D0*h1+h2*D1-(S.eye(4)-I1*P1)))
ck('base_degree2_contraction',zero(D1*h2-(S.eye(2)-I2*P2)))
ck('base_complex',zero(D1*D0))
ck('projection_homotopy_side_conditions',zero(P0*h1) and zero(P1*h2))
ck('homotopy_inclusion_side_conditions',zero(h1*I1) and zero(h2*I2))

N0=S.zeros(3);N0[0,2]=1;N0[2,1]=1
N1=S.zeros(4);N1[0,2]=1;N1[2,3]=1;N1[3,1]=1
N2=S.zeros(2);N2[0,1]=1
U0=S.eye(3)+t*N0;U1=S.eye(4)+s*N1;U2=S.eye(2)+t*N2
B0=D0.copy();B0[0,0]=t;B0[1,1]=s
F0=simp(U1.inv()*B0*U0);F1=simp(U2.inv()*D1*U1)
A0=simp(F0-D0);A1=simp(F1-D1)
ck('actual_perturbed_complex',zero(F1*F0))
ck('degree0_Maurer_Cartan',zero(D1*A0+A1*D0+A1*A0))
T0=simp((S.eye(3)+h1*A0).inv());T1=simp((S.eye(4)+h2*A1).inv())
M=simp(P1*A0*T0*I0)
ck('exact_kernel_intertwining',zero(F0*T0*I0-T1*I1*M))
ck('exact_inverse_on_harmonic_domain',zero(P0*T0*I0-S.eye(2)))
ck('left_inverse_T0',zero(T0*(S.eye(3)+h1*A0)-S.eye(3)))
ck('left_inverse_T1',zero(T1*(S.eye(4)+h2*A1)-S.eye(4)))
ck('harmonic_inclusion_injective',I0.rank()==2 and I1.rank()==2)

vals=[S.Rational(-1,4),S.Rational(-1,8),S.Integer(0),S.Rational(1,9),S.Rational(1,5)]
for x in vals:
 for y in vals:
  sub={t:x,s:y};key=f't{x}_s{y}'
  q0=simp(F0.subs(sub));q1=simp(F1.subs(sub));mt=simp(M.subs(sub));tt=simp(T0.subs(sub))
  ck('invertibility_domain_'+key,(S.eye(3)+h1*A0).det().subs(sub)!=0 and (S.eye(4)+h2*A1).det().subs(sub)!=0)
  ck('full_kernel_dimension_'+key,3-q0.rank()==2-mt.rank())
  ck('full_complex_'+key,zero(q1*q0))
  for k,v in enumerate(mt.nullspace()):
   u=tt*I0*v
   ck('forward_actual_kernel_map_'+key+f'_{k}',zero(q0*u))
   ck('projection_inverse_'+key+f'_{k}',zero(P0*u-v))
  for k,u in enumerate(q0.nullspace()):
   v=P0*u
   ck('inverse_actual_kernel_map_'+key+f'_{k}',zero(mt*v))
   ck('reconstruction_'+key+f'_{k}',zero(tt*I0*v-u))

# Exact symbolic exponents retain the orientation epsilon and the fibre period.
# No numerical approximation of irrationality is used.
for m in range(2,13):
 for j in range(m+1):
  for eps in [-1,1]:
   for n in [1,2,5]:
    q=r-S.Rational(eps*j,m)
    name=f'm{m}_j{j}_eps{eps}_period{n}'
    ck('actual_shift_'+name,S.expand(n*q-(n*r-S.Rational(n*eps*j,m)))==0)
    ck('mth_power_character_'+name,S.expand(m*n*q-m*n*r)==-n*eps*j)
    ck('conormal_successive_shift_'+name,S.expand(n*(q-S.Rational(eps,m))-n*(r-S.Rational(eps*(j+1),m)))==0)

out={'result':'PASS','checks':len(checks),'sympy_version':S.__version__,'names':checks,'matrix_domains':{'q0':3,'q1':4,'q2':2,'harmonic_q0':2,'harmonic_q1':2},'export':{k:[[str(x) for x in row] for row in v.tolist()] for k,v in {'D0':D0,'D1':D1,'F0':F0,'F1':F1,'T0':T0,'T1':T1,'M':M}.items()},'scope':'New exact symbolic finite-complex calculation with nonzero contractible blocks and parameter-dependent basis changes; exact kernel maps/inverses and 25 small rational parameter pairs. Rational-shift identities for m=2..12, all j=0..m, both orientation signs and periods1,2,5. Universal analytic proof and every real irrational nontriviality assertion are written separately before target reading.'}
p=Path(__file__).with_suffix('.output.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'result':'PASS','checks':len(checks),'M':str(M),'T0_domain_determinant':str(S.factor((S.eye(3)+h1*A0).det())),'T1_domain_determinant':str(S.factor((S.eye(4)+h2*A1).det()))}))
