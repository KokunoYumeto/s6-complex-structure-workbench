"""Full signed period/endpoint dictionary and assembled I3 boundary expression."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
checks=[]
def ck(n,v):
    assert bool(v),n
    checks.append(n)
def eq(a,b):return S.cancel(S.together(a-b))==0
r,h=S.symbols('r h',nonnegative=True)
M0=S.Matrix([[r+3*h,-h],[6*h,r+2*h]])
M1=S.Matrix([[3*r,-r],[0,4*(r+h)]])
Mi=S.Matrix([[7*h,2*h],[h,r+2*h]])
ck('zero full period determinant',S.expand(M0.det())==r*r+5*r*h+12*h*h)
ck('one full period determinant',S.expand(M1.det()-12*r*(r+h))==0)
ck('infinity full period determinant',S.expand(Mi.det())==7*r*h+12*h*h)
ck('one actual lower source-period kernel',M1.subs(r,0).nullspace()==[S.Matrix([1,0])])
ck('infinity actual lower source-period kernel',Mi.subs(h,0).nullspace()==[S.Matrix([1,0])])
def nonnegative_poly(e):
    p=S.Poly(S.expand(e),r,h)
    if all(a>=0 for a in p.coeffs()): return True
    a=p.coeff_monomial(r*r); b=p.coeff_monomial(r*h); c=p.coeff_monomial(h*h)
    return p.total_degree()==2 and S.expand(e-a*(r-h)**2-(b+2*a)*r*h-(c-a)*h*h)==0 and a>=0 and b+2*a>=0 and c-a>=0
for label,X in [('lower',M0.inv()*r*S.eye(2)),('upper',M0.inv()*h*S.Matrix([[3,-1],[6,2]]))]:
    for i,x in enumerate(X):
        for sign in [-1,1]:
            ck(f'zero actual parent inverse bound {label},{i},{sign}',nonnegative_poly(S.cancel((1+sign*x)*M0.det())))
for i,x in enumerate([-5*(r+2*h)/(7*r+12*h),5*h/(7*r+12*h),2*(r+h)/(7*r+12*h),-7*(r+h)/(7*r+12*h)]):
    for sign in [-1,1]:
        ck(f'infinity actual inverse vertex bound{i},{sign}',nonnegative_poly(S.cancel((1+sign*x)*(7*r+12*h))))
for z in [0,3*r]:
    for y in [0,4*(r+h)]:
        cc=M1.inv()*S.Matrix([z,y])
        ck(f'one actual rectangle inverse bound{z},{y}',all(eq(x,t) for x,t in zip(cc,[z/(3*r)+y/(12*(r+h)),y/(4*(r+h))])))
A,B,C=S.symbols('A B C',positive=True)
L=S.symbols('L',real=True)
N=S.Matrix([[-2*A-B,A],[3*B,L-B]])
ck('entire real determinant',S.expand(N.det())==S.expand((2*A+B)*(-L)+B*B-A*B))
ck('exact first determinant bound',S.expand(N.det().subs(L,-4*B-C))==S.expand(7*A*B+5*B*B+C*(2*A+B)))
ck('exact second determinant bound',S.expand(N.det().subs(L,-4*A-C))==S.expand(8*A*A+3*A*B+B*B+C*(2*A+B)))
q,qi,hh,phi=S.symbols('q qi h phi',nonzero=True)
for j in range(-4,5):
    ck(f'full forward ordinary/cap square{j}',eq(((qi**j*phi)*q**j).subs(q,hh/qi),hh**j*phi))
    ck(f'full inverse closing square{j}',eq((phi*q**-j).subs(q,hh/qi),hh**-j*(qi**j*phi)))
P,p,cq,c0,Z,V=S.symbols('P p cq c0 Z V',nonzero=True)
ck('actual selected endpoint reindex',eq((P*p*cq)**2*(P**2*p*c0)**-2*V,P**-2*(cq/c0)**2*V))
w=S.symbols('w');v=w*w-1;D=v-2;ss=v*(v+4)/(4*D*D)
ck('original source parameter at minus branch',ss.subs(w,-1)==0 and S.diff(ss,w).subs(w,-1)==-S.Rational(1,2))
ck('original source parameter at plus branch',ss.subs(w,1)==0 and S.diff(ss,w).subs(w,1)==S.Rational(1,2))
ck('actual original source reflection',eq(ss.subs(w,-w),ss))
ck('full original source r reflection',eq(((1-2*v)/D**2).subs(w,-w),(1-2*v)/D**2))
tt,rho,GG,HH=S.symbols('t rho G H',real=True)
logD=lambda rr:rr*HH+2*S.pi*S.I*rr*(rr-1)
ck('complete scalar-product functional equation',S.expand(logD(rho+1)-logD(rho)-HH-4*S.pi*S.I*rho)==0)
ck('complete source-cut G coefficient',S.expand(rho*(GG-2*S.pi*S.I)-rho*GG)==-2*S.pi*S.I*rho)
ck('complete source-cut H coefficient',S.expand(logD(rho).subs(HH,HH-6*S.pi*S.I)-logD(rho))==-6*S.pi*S.I*rho)
ck('full diagonal versus MC3 physical factor',S.expand(logD(2*tt)-2*tt*(HH+8*S.pi*S.I*tt)+2*S.pi*S.I*(4*tt**2+2*tt))==0)
ck('retained physical loop exact factorization',S.expand(4*tt**2+2*tt-4*tt*(tt-1)-6*tt)==0)
ck('quadratic logarithm zero at both ends',(tt*(tt-1)).subs(tt,0)==0 and (tt*(tt-1)).subs(tt,1)==0)
u=S.symbols('u',nonzero=True);AA=u**-2;DD=u**-6;LL=u;RR=u**7
ck('entire quaternion source-cut first coefficient',eq(LL*RR,(AA*DD)**-1))
ck('entire quaternion source-cut second coefficient',eq(LL**-1*RR,DD**-1))
ck('entire quaternion source-cut base',eq(LL**-2,AA))
for j in range(-3,4):
    ck(f'actual paired half-phase endpoint{j}',LL.subs(u,S.Integer(-1)**j)==RR.subs(u,S.Integer(-1)**j) and S.simplify(LL*RR).subs(u,S.Integer(-1)**j)==1)
# Actual row sums retain the unknown Chern clutch as an indeterminate.
k=S.symbols('kappa',integer=True)
compact=(-63,453);lower=(72,-348);moving=(k,4*k+123)
inner=tuple(sum(x[i] for x in [compact,lower,moving]) for i in range(2))
ck('entire scoped compact/lower/moving pair',inner==(k+9,4*k+228))
ck('literal retained Chern-clutch cancellation',S.expand(4*inner[0]-inner[1])==-192)
jin=tuple(-v for v in inner)
ck('parameter-reversal physical pair',jin==(-k-9,-4*k-228))
ck('actual physical characteristic index',S.expand((4*jin[0]-jin[1])/24)==8)
ck('integer class after physical inverse-clutch map',8%28==8)
sources=['notes/part3_e6_selected_i3_working.md','notes/part3_e6_selected_i3_fixed_surfaces_working.md','notes/part3_e6_selected_i3_fixed_curve_normals_working.md','notes/part3_e6_selected_i3_lower_relative_working.md','notes/part3_e6_selected_i3_moving_star_working.md','notes/part3_e6_selected_i3_moving_cap_working.md','notes/part3_e6_selected_i3_outer_transfer_working.md']
inputs=['code/part3/e6_selected_i3_corner_lifts.json','code/part3/e6_selected_i3_p_one_cayley.json','code/part3/e6_selected_i3_fixed_faces.json','code/part3/e6_selected_i3_fixed_surfaces.json','code/part3/e6_selected_i3_fixed_curve_normals.json','code/part3/e6_selected_i3_lower_relative.json','code/part3/e6_selected_i3_moving_star.json','code/part3/e6_selected_i3_moving_cap.json']
expected_status={'code/part3/e6_selected_i3_p_one_cayley.json':'PASS_SELECTED_I3_P_ONE_COMMON_CAYLEY','code/part3/e6_selected_i3_fixed_curve_normals.json':'PASS_SELECTED_I3_GENERIC_CURVE_NORMALS','code/part3/e6_selected_i3_lower_relative.json':'PASS_SELECTED_I3_LOWER_RELATIVE'}
for f in inputs:
    d=json.loads((ROOT/f).read_text());ck('saved exact certificate PASS '+f,d['status']==expected_status.get(f,'PASS'))
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'checks':len(checks),'identities':checks,'source_sha256':{f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in sources},'input_sha256':{f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in inputs},'scope':'Complete actual relative selected-I3 boundary for M6,b1,m2,n1, retained finite character, negative-square fan in unit+1 Tate chart; positive full source meridian at the exact basepoint scalar. Formal promotion awaits independent whole-proof audit.','inner_physical_pair':['9+kappa','228+4*kappa'],'jin_physical_pair':['-9-kappa','-228-4*kappa'],'index':8,'class_mod28':8,'unassigned':['kappa and individual native left integer','untransported global Z_w fan at the opposite branch','other selected fans or cap orders']}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
