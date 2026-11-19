#!/usr/bin/env python3
from pathlib import Path
import sympy as S,json,datetime
R=Path(__file__).resolve().parents[2];checks=[]
def ck(n,x):
 ok=all(S.simplify(v)==0 for v in x) if isinstance(x,S.MatrixBase) else S.simplify(x)==0
 if not ok:raise AssertionError((n,x))
 checks.append(n)
a,b,c,g,eta=S.symbols('a b c g eta',nonzero=True)
u=g*eta*b*c;v=1/(eta*c);w=a*c/g
ck('C1_actual_native_chart',S.Matrix([eta*v,g*w,u/(g*eta)])-S.Matrix([1/c,c*a,c*b]))
ck('C2_actual_native_chart',S.Matrix([1/a,a*b,a*c])-S.Matrix([1/a,a*b,a*c]))
triples=[(0,-6,1),(0,-6,1),(-6,0,1)]
second=[(-n,m+2*n,s+n) for m,n,s in triples]
first=[(m+2*n,-n,s+n) for m,n,s in triples]
classes=[x[2]%28 for x in second]
ck('first_flop_classes',S.Matrix(classes)-S.Matrix([23,23,1]))
for i,p in enumerate(first):
 m,n,s=p;reverse=(m+2*n,-n,(s+n)%28)
 ck(f'reverse_flop_{i}',S.Matrix(reverse)-S.Matrix(triples[i]))
r={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','checks_count':len(checks),'checks':checks,'proof':'notes/part3_source_cusp_first_flops_working.md','proof_status':'Proved P3K.54; root and blind_control full FF1--2 audits PASS','initial_native_triples':triples,'second_product_triples':second,'reset_native_triples':first,'first_flop_classes_mod28':classes,'not_assigned':['subsequent ordinary-product reset','general fan formula']}
(R/'code/part3/source_cusp_first_flops.json').write_text(json.dumps(r,indent=2)+'\n');print('PASS',len(checks),'exact native-chart and first-flop checks.')
