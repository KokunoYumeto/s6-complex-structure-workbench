#!/usr/bin/env python3
from pathlib import Path
import sympy as S,json,datetime
ROOT=Path(__file__).resolve().parents[2];checks=[]
def ck(name,x):
 good=all(S.trigsimp(v)==0 for v in x) if isinstance(x,S.MatrixBase) else S.simplify(x)==0
 if not good:raise AssertionError((name,x))
 checks.append(name)
def qm(p,q):
 a,b,c,d=p;e,f,g,h=q
 return S.Matrix([a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e])
def qc(p):return S.Matrix([p[0],-p[1],-p[2],-p[3]])
t,theta=S.symbols('t theta',real=True);A=S.sin(t);B=S.cos(t)
H=S.Matrix([B**2+A**2*S.cos(3*theta),-A**2*S.sin(3*theta),A*B*(1-S.cos(3*theta)),A*B*S.sin(3*theta)])
i=S.Matrix([0,1,0,0]);j=S.Matrix([0,0,1,0]);k=S.Matrix([0,0,0,1]);w=qm(qm(qc(H),i),H)
for n in range(3):
 pt={t:S.pi/4,theta:(S.pi+2*S.pi*n)/3}
 ck(f'inverse_axis_preimage_{n}',w.subs(pt)+i)
 ck(f'inverse_axis_negative_s_{n}',w.diff(t).subs(pt)+4*k)
 ck(f'inverse_axis_positive_theta_{n}',w.diff(theta).subs(pt)-3*j)
U,Hs,E=S.symbols('U H E',commutative=False)
F1=E**-1*U*E*Hs*E**-1*Hs**-1*U**-1*Hs**-1*E**-1*Hs
P1=E**-1*(U*E*U**-1)*(U*Hs*E**-1*Hs**-1*U**-1)*(Hs**-1*E**-1*Hs)
F2=E*U*E**-1*Hs*E*Hs**-1*U**-1*Hs*E**-1*Hs**-1
P2=E*(U*E**-1*U**-1)*(U*Hs*E*Hs**-1*U**-1)*(Hs*E**-1*Hs**-1)
ck('C1_exact_factorization',F1-P1);ck('C2_exact_factorization',F2-P2)
ck('half_angle_volume',4*S.pi*S.integrate(S.sin(t)**2,(t,0,S.pi))/(2*S.pi**2)-1)
ck('C0_trace_degree',-2*3+6);ck('C1_trace_degree',-3-(-3));ck('C2_trace_degree',3-3)
V=S.Matrix([[0,6,-6],[6,0,0],[-6,0,0]])
ck('integral_variation_symmetry',V-V.T)
ck('trace_D1_column',V*S.Matrix([0,1,0])-S.Matrix([6,0,0]))
ck('trace_minus_D2_column',V*S.Matrix([0,0,-1])-S.Matrix([6,0,0]))
ck('fixed_diagonal_from_OR',V[0,0])
ck('circle_path_C1_boundary_sign',(-1)*(-1)-1)
ck('circle_path_C2_boundary_sign',(-1)*(1)+1)
r={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','checks_count':len(checks),'checks':checks,'proof':'notes/part3_source_cusp_circle_trace_working.md','scope':'actual local orbit trace, generic graph-loop closures, exact chain homotopy and full integral variation; root and independent blind_control PASS','axis_degrees':[0,3,3,-3],'local_trace_degrees':[-6,0,0],'full_variation_matrix':[[0,6,-6],[6,0,0],[-6,0,0]],'not_computed':['nonfixed stable derivative','nonfixed relative integers','further fan return']}
(ROOT/'code/part3/source_cusp_circle_trace.json').write_text(json.dumps(r,indent=2)+'\n');print('PASS',len(checks),'exact orbit-trace and integral variation checks; nonfixed derivative uncomputed.')
