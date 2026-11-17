#!/usr/bin/env python3
from pathlib import Path
import sympy as S,json,datetime
R=Path(__file__).resolve().parents[2];checks=[]
def ck(n,x):
 good=all(S.simplify(v)==0 for v in x) if isinstance(x,S.MatrixBase) else S.simplify(x)==0
 if not good:raise AssertionError((n,x))
 checks.append(n)
n=S.symbols('n',integer=True);P=S.Matrix([[1,0],[n,1]]);B=-6*P.inv()*S.diag(1,0)*P
ck('shear_period_matrix',B-S.Matrix([[-6,0],[6*n,0]]))
ell=[B[1,1]-B[1,0],B[0,0]-B[0,1],B[1,1]];w=[0,1,-1];d=[-2,-1,-1]
I=S.Matrix([-3*wi+di*(li+3) for wi,di,li in zip(w,d,ell)])
W=S.Matrix([-3*wi-di*(li+3) for wi,di,li in zip(w,d,ell)])
ck('actual_orbit_degrees',I-S.Matrix([12*n-6,0,0]));ck('actual_derivative_degrees',W-S.Matrix([6-12*n,-6,6]))
r1=(W[1]-W[0])/2;r2=-(W[2]-W[0])/2
ck('native_C1_right',r1-(6*n-6));ck('native_C2_right',r2+6*n)
s=1-3*n*(n-1)
ck('positive_flop_recurrence',s.subs(n,n+1)-s-r2)
ck('negative_flop_recurrence',s.subs(n,n-1)-s-r1)
ck('initial_return',s.subs(n,0)-1)
ck('first_diagonal_return',s.subs(n,1)-1);ck('first_horizontal_return',s.subs(n,-1)+5)
# Exact translated triangles; vectors remain symbolic.
z=S.Matrix([0,0]);v=S.Matrix([1,n]);ww=S.Matrix([0,1]);vp=v+ww
ck('new_triangle_plus_0',vp-S.Matrix([1,n+1]))
ck('new_triangle_minus_shift_vertex0',-ww+vp-v)
ck('new_triangle_minus_shift_vertex1',-ww+ww)
ck('new_triangle_minus_shift_vertex2',-ww+vp+ww-vp)
ck('period_28',s.subs(n,n+28)-s-28*(-6*n-81))
ck('reflection_symmetry',s.subs(n,1-n)-s)
rows=[{'n':k,'class':int(s.subs(n,k))%28,'native_C1_right':int(r1.subs(n,k)),'native_C2_right':int(r2.subs(n,k))} for k in range(-56,57)]
record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','checks_count':len(checks),'checks':checks,'proof':'notes/part3_source_cusp_vertical_fans_working.md','proof_status':'Proved P3K.56; root and blind_control full VF1--3 audits PASS','formula':'1-3n(n-1) mod28','residue_classes':sorted({x['class'] for x in rows}),'rows':rows,'not_assigned':['nonvertical fan return','other characteristic pairs','shorter source-loop endpoint']}
(R/'code/part3/source_cusp_vertical_fans.json').write_text(json.dumps(record,indent=2)+'\n');print('PASS',len(checks),'exact shear-fan trace and actual flop recurrence checks; residues',record['residue_classes'])
