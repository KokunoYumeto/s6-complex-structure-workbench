"""Exact local charged-chart invariants and finite norms; no global attachment."""
from pathlib import Path
import sympy as S,json
u0,u1,t0,t1,d,z,w,x=S.symbols('u0 u1 t0 t1 d z w x',nonzero=True)
checks=[]
def ck(n,e):
 assert S.factor(e)==0,(n,S.factor(e))
 checks.append(n)
ss=u0*t1-u1*t0
tt=t1*(u0*u0*t0-u1-u0)/2
sub={u0:d*u0,u1:d*u1,t0:t0/d,t1:t1/d}
ck('actual_source_parameter_invariant',ss.xreplace(sub)-ss)
ck('actual_elliptic_base_invariant',tt.xreplace(sub)-tt)
ck('source_chart_s',ss.subs({u0:1,u1:z,t0:w,t1:x})-(x-z*w))
ck('source_chart_t',tt.subs({u0:1,u1:z,t0:w,t1:x})-x*(w-z-1)/2)
h,al,be=S.symbols('h al be')
ck('target_chart_s',ss.subs({u0:al,u1:be,t0:1,t1:h})-(al*h-be))
ck('target_chart_t',tt.subs({u0:al,u1:be,t0:1,t1:h})-h*(al*al-al-be)/2)
R,r,N=S.symbols('R r N',positive=True)
ck('full_norm_ratio',R**3*(N/R**3)-N)
ck('full_finite_end_norm',(R/r**2)**3*(r**3/R**3)-r**(-3))
ck('charge_three_physical_index',S.Rational(4*(-27)-(-12),24)+4)
out={'status':'PASS','checks':len(checks),'identities':checks,'scope':'Local charged chart and full face identities only. No completed return assigned.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
