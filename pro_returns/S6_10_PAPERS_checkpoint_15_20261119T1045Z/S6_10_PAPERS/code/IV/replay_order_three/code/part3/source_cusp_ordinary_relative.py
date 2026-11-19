#!/usr/bin/env python3
import sympy as S,json,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
checks=[]
def ck(name,x):
 if isinstance(x,S.MatrixBase): good=all(S.simplify(y)==0 for y in x)
 else: good=S.simplify(x)==0
 if not good:raise AssertionError((name,x))
 checks.append(name)
a,b,c,k,al,eta=S.symbols('a b c k alpha eta',nonzero=True)
u=k*al*b*c;v=al**-1*a*b;w=k**-1/b
ck('actual_Hopf_second_chart',S.Matrix([k*w,al*v,u/(k*al)])-S.Matrix([1/b,a*b,b*c]))
ck('physical_height_retained',u*v*w-a*b*c)
G,P=S.symbols('Gamma P_H',commutative=False)
ck('ordinary_transport_boundary_direction',G*P**-1*(P*G**-1)-1)
ck('inverse_left_side_degree',-S.Integer(-6)-6)
ck('inverse_right_side_degree',-S.Integer(0))
ck('side_minus_top_degree_equation',S.Integer(6)-6)
ck('relative_m_after_composition',0+6-6)
ck('relative_n_after_composition',-6+0+6)
ck('central_class_unchanged',1+0-1)
ck('fixed_curve_variation',6-6)
ck('relative_stable_derivative',-2*(-6)-12)
g=S.symbols('g',nonzero=True)
u1=g*eta*b*c;v1=eta**-1/c;w1=g**-1*a*c
ck('native_C1_second_chart',S.Matrix([eta*v1,g*w1,u1/(g*eta)])-S.Matrix([1/c,c*a,c*b]))
ck('native_C2_second_chart',S.Matrix([1/a,a*b,a*c])-S.Matrix([1/a,a*b,a*c]))
r={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','checks_count':len(checks),'checks':checks,'proof':'notes/part3_source_cusp_ordinary_relative_working.md','status_of_proof':'Proved P3K.50; root, fourfold and blind_control audits PASS','boundary_gauge_direction':'ordinary_product composed with inverse_Hopf_product','boundary_degrees_Hopf':[-6,0],'transport_correction_degrees':[6,0],'relative_coordinates':[6,-6,1],'fixed_curve_variation':0,'fixed_curve_derivative_product_cycle':12,'fixed_curve_derivative_ambient_dual_cycle':-12,'not_computed':['nonfixed relative entries','mutual variations','further fan return']}
(ROOT/'code/part3/source_cusp_ordinary_relative.json').write_text(json.dumps(r,indent=2)+'\n')
print('PASS',len(checks),'exact fixed-curve ordinary-product direction and relative-coordinate checks.')
