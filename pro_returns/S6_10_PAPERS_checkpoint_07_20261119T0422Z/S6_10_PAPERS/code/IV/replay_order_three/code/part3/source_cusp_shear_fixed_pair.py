#!/usr/bin/env python3
from pathlib import Path
import sympy as S,json,datetime
R=Path(__file__).resolve().parents[2];checks=[]
def ck(k,x):
 if S.simplify(x)!=0:raise AssertionError((k,x))
 checks.append(k)
a,b,n,g1,RR,h=S.symbols('a b n g1 R h',real=True)
nr=(b-a)/2;mr=-(a+b)/2-6
ck('native_pair_to_k',-(mr+nr)-(a+6))
ck('native_pair_to_ell',-4*mr-(24+2*a+2*b))
ck('native_pair_to_A',-nr/6-(a-b)/12)
ck('nonfixed_C1_pair_sum',-6*n+(6*n-6)+6)
ck('nonfixed_C2_pair_sum',(6*n-6)-6*n+6)
M=S.Matrix([[S.cos(2*S.pi*h),-2*S.pi*(RR+g1)*S.sin(2*S.pi*h)],[S.sin(2*S.pi*h),2*S.pi*(RR+g1)*S.cos(2*S.pi*h)]])
ck('circular_chart_positive_jacobian',M.det()-2*S.pi*(RR+g1))
t=S.symbols('t',real=True)
ck('contracted_jacobian',M.subs({g1:(1-t)*g1,h:(1-t)*h}).det()-2*S.pi*(RR+(1-t)*g1))
x,y=S.symbols('x y',nonzero=True)
for j in range(-5,6):
 ck('Cartier_first_%d'%j,(x/y)**j*x**(-j-1)*y**j-1/x)
 ck('Cartier_second_%d'%j,(x/y)**j*x**(-j)*y**(j+1)-y)
 ck('Cartier_det_%d'%j,(x/y)**(2*j+1)*x**(-2*j-1)*y**(2*j+1)-1)
record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','checks_count':len(checks),'checks':checks,'proof':'notes/part3_source_cusp_shear_fixed_pair_working.md','scope':'Only exact local shear/relative identities, circular-height derivative and typed Cartier spinor maps. Actual full graph/cap comparison remains open.','not_assigned':['ell','k','integer Haefliger value']}
(R/'code/part3/source_cusp_shear_fixed_pair.json').write_text(json.dumps(record,indent=2)+'\n');print('PASS',len(checks),'local identities; no characteristic pair assigned')
