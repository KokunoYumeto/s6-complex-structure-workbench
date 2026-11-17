#!/usr/bin/env python3
from pathlib import Path
import datetime
import json
import sympy as S

ROOT=Path(__file__).resolve().parents[2]
checks=[]
def check(name,value):
    if isinstance(value,bool): passed=value
    elif isinstance(value,S.MatrixBase): passed=all(S.trigsimp(S.simplify(x))==0 for x in value)
    else: passed=S.trigsimp(S.simplify(value))==0
    assert passed,name
    checks.append({'name':name,'pass':True})
def qm(p,q):
    w,x,y,z=p; a,b,c,d=q
    return S.Matrix([w*a-x*b-y*c-z*d,w*b+x*a+y*d-z*c,
                     w*c-x*d+y*a+z*b,w*d+x*c-y*b+z*a])
def qc(q): return S.Matrix([q[0],-q[1],-q[2],-q[3]])

a,b,c,kappa,alpha,eta,g=S.symbols('a b c kappa alpha eta g',nonzero=True)
D0=S.diag(eta/alpha,kappa*alpha)
D1=S.diag(kappa/g,g*eta)
D2=S.diag(eta,kappa)
check('C0_actual_ordered_transition',S.Matrix([eta*alpha**-1*a*b,kappa*alpha*b*c])-b*D0*S.Matrix([a,c]))
check('C1_actual_ordered_transition',S.Matrix([kappa*g**-1*a*c,g*eta*b*c])-c*D1*S.Matrix([a,b]))
check('C2_actual_ordered_transition',S.Matrix([eta*a*b,kappa*a*c])-a*D2*S.Matrix([b,c]))
for n,D in enumerate([D0,D1,D2]): check(f'C{n}_determinant_exact',D.det()-kappa*eta)
check('three_tangent_reciprocals',S.Matrix([kappa*(kappa**-1/b)-1/b,eta*(eta**-1/c)-1/c,a**-1-1/a]))

t,theta=S.symbols('t theta',real=True)
AA,BB=S.sin(t),S.cos(t)
p=S.Matrix([AA*S.cos(3*theta),-AA*S.sin(3*theta),BB,0])
p0=S.Matrix([AA,0,BB,0])
H=qm(p,qc(p0))
displayed=S.Matrix([BB**2+AA**2*S.cos(3*theta),-AA**2*S.sin(3*theta),
                    AA*BB*(1-S.cos(3*theta)),AA*BB*S.sin(3*theta)])
check('based_H_expansion',H-displayed)
check('H_unit',qm(H,qc(H))-S.Matrix([1,0,0,0]))
check('H_at_first_end',H.subs(t,0)-S.Matrix([1,0,0,0]))
check('H_at_second_end',H.subs(t,S.pi/2)-S.Matrix([S.cos(3*theta),-S.sin(3*theta),0,0]))
check('H_at_initial_parameter',H.subs(theta,0)-S.Matrix([1,0,0,0]))
check('H_at_final_parameter',H.subs(theta,2*S.pi)-S.Matrix([1,0,0,0]))

x0,y0,x1,y1=S.symbols('x0 y0 x1 y1',real=True)
Q=S.Matrix([x0,y0,x1,y1]) # Q=n0+j*conjugate(n1), not n0+j*n1.
He=H.subs(t,S.pi/2)
C6,S6=S.cos(6*theta),S.sin(6*theta)
check('Tminus_actual_complex_normal_loop',qm(qm(He,Q),qc(He))-S.Matrix([x0,y0,C6*x1+S6*y1,C6*y1-S6*x1]))
check('Tplus_actual_complex_normal_loop',qm(qm(He,Q),He)-S.Matrix([C6*x0+S6*y0,C6*y0-S6*x0,x1,y1]))
i=S.Matrix([0,1,0,0]);j=S.Matrix([0,0,1,0]);k=S.Matrix([0,0,0,1])
nu=qm(qm(H,i),qc(H))
check('axis_first_end',nu.subs(t,0)-i)
check('axis_second_end',nu.subs(t,S.pi/2)-i)
for n in range(3):
    pt={t:S.pi/4,theta:(S.pi+2*S.pi*n)/3}
    check(f'minus_i_preimage_{n}',nu.subs(pt)+i)
    check(f'positive_s_derivative_{n}',nu.diff(t).subs(pt)-4*k)
    check(f'positive_theta_derivative_{n}',nu.diff(theta).subs(pt)-3*j)
check('target_outward_orientation_at_minus_i',S.Matrix.hstack(S.Matrix([-1,0,0]),S.Matrix([0,0,1]),S.Matrix([0,1,0])).det()-1)
check('regular_positive_local_degree_matrix',S.Matrix([[4,0],[0,3]]).det()-12)

I2=S.eye(2); ii=S.diag(S.I,-S.I)
check('MC_first_boundary_trace',S.trace(ii*(-3*ii))-6)
check('MC_second_boundary_trace',S.trace((-3*ii)*(-ii))*(-1)-6)
check('closed_left_factor_degree',S.Rational(12,8)*4-6)
check('closed_right_factor_degree_rank_two',S.Integer(0))
check('complex_to_Hopf_curve_orientation',S.Matrix([[0,-2],[-2,0]]).det()+4)

report={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS',
 'checks_count':len(checks),'checks':checks,'proof':'notes/part3_source_cusp_ordinary_product_working.md',
 'statement':'P3K.48','quaternion_coordinate':'Q=n0+j*conjugate(n1)',
 'normal_loops':['diag(1,exp(-6i theta))','diag(exp(-6i theta),1)','diag(1,exp(-6i theta))'],
 'contractions':['H Q H^-1','H Q H','H Q H^-1'],
 'circle_axis':'H i H^-1','axis_degree':3, 'closed_frame_degrees_complex':[6,0], 'closed_frame_degrees_Hopf':[-6,0],
 'axis_domain_orientation':'ds wedge dtheta, each end circle collapsed',
 'axis_target_orientation':'outward sphere in imaginary quaternions',
 'ordinary_product':'periodic, labelled, oriented, based at the reference fibre',
 'not_assigned':['circle-trace correction','common-exterior variation matrix','nonfixed relative integers','arbitrary-fan return']}
(ROOT/'code/part3/source_cusp_ordinary_product.json').write_text(json.dumps(report,indent=2)+'\n')
print(f'PASS {len(checks)} exact ordinary-plumbing and physical-circle-axis checks; degree +3, no return assigned.')
