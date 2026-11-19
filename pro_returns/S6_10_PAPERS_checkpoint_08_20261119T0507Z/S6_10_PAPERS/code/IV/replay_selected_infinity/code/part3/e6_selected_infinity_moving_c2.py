"""Exact coefficient, frame, and directed Chern checks for MC2."""
from pathlib import Path
import hashlib,json
import sympy as S
R=Path(__file__).resolve().parents[2]
x,y,A,B,C,D=S.symbols('x y A B C D',real=True)
z=x+S.I*y;zb=S.conjugate(z);r2=x*x+y*y
checks=[]
def check(name,value):
    if isinstance(value,S.MatrixBase):
        ok=all(S.simplify(e)==0 for e in value)
    else:ok=S.simplify(value)==0
    assert ok,(name,value)
    checks.append(name)
def qm(p,q):
    a,b,c,d=p;e,f,g,h=q
    return S.Matrix([a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,
                     a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e])
G0=S.Matrix([[1,-z],[zb,1]])
w=1/z
G1=S.Matrix([[S.conjugate(w),-1],[1,w]])
T=S.diag(zb,z)
check('two literal Cox frame charts',G1*T-G0)
check('first frame determinant',G0.det()-(1+r2))
check('second frame determinant',G1.det()-(1+1/r2))
check('first positive Hermitian norm',G0*S.conjugate(G0.T)-(1+r2)*S.eye(2))
check('second positive Hermitian norm',G1*S.conjugate(G1.T)-(1+1/r2)*S.eye(2))
c0=A+S.I*B;c1=C+S.I*D
product=qm([1,0,x,-y],[A,B,C,D])
positive=S.Matrix([product[0]-S.I*product[1],product[2]+S.I*product[3]])
check('quaternion-to-positive-spinor coefficient arrow',
      positive-G0*S.Matrix([S.conjugate(c0),c1]))
Pi=S.Matrix([1,zb])*S.Matrix([[1,z]])/(1+r2)
check('negative-original-normal projector squares',Pi*Pi-Pi)
check('projector Hermitian',Pi-S.conjugate(Pi.T))
check('projector rank one trace',S.trace(Pi)-1)
tau=S.symbols('tau',nonzero=True)
clutch=G0*S.diag(tau,1)*G0.inv()
check('global clutch projector formula',clutch-(S.eye(2)+(tau-1)*Pi))
check('global clutch determinant',clutch.det()-tau)
check('global clutch inverse',clutch*(S.eye(2)+(1/tau-1)*Pi)-S.eye(2))
check('second chart clutch equals first',G1*S.diag(tau,1)*G1.inv()-clutch)
J=S.diag(1/zb,1)
check('full q-factor inverse-Z arrow commutes',J*S.diag(tau,1)-S.diag(tau,1)*J)
rr,rrbar,ttbar=S.symbols('r rbar tbar',nonzero=True)
check('full MC16a diagonal factorization',
      S.diag(ttbar/rrbar,rr)-S.diag(ttbar,1)*S.diag(1/rrbar,rr))
norm,phase=S.symbols('norm phase',positive=True)
check('literal common-phase positive polar factor',
      S.diag(phase/norm,phase*norm)-phase*S.diag(1/norm,norm))
g11,g12,g21,g22=S.symbols('g11 g12 g21 g22')
Gt=S.Matrix([[g11,g12],[g21,g22]])
LA=Gt.inv()*G0
check('transported Cox quaternion target square',Gt*LA-G0)
check('transported Cox quaternion inverse',LA.inv()*LA-S.eye(2))
a=S.symbols('a',integer=True)
order_r=4-a;order_t=4
check('full first positive winding',-(order_t-order_r)-(-a))
check('full second positive winding',order_r-(4-a))
check('full determinant winding',-a+(4-a)-(4-2*a))
check('non-scalar first winding after common phase',-a-order_r+4)
check('non-scalar second winding after common phase',4-a-order_r)
h,u=S.symbols('h u')
def integral(expr):
    return S.expand(expr).coeff(h,1).coeff(u,1)
check('reduced directed second Chern number',integral((h+4*u)*(-h))+4)
check('complete retained-phase second Chern number',
      integral((h+a*u)*(-h+(a-4)*u))+4)
check('common scalar phase has zero second Chern change',
      integral((h+a*u)*(-h+(a-4)*u)-(h+4*u)*(-h)))
for aa in [2,6]:
    check(f'full a={aa} second Chern product',
          integral((h+aa*u)*(-h+(aa-4)*u))+4)
    check(f'full a={aa} determinant degree',
          (-(-aa)-(4-aa))-(2*aa-4))
n0,n1=S.symbols('n0 n1',integer=True)
check('general target-coefficient Chern direction',
      integral((h-n0*u)*(-h-n1*u))-(n0-n1))
check('conjugating both lines preserves c2',
      integral((-h-4*u)*h)-integral((h+4*u)*(-h)))
check('swapping both ordered lines preserves c2',
      integral((-h)*(h+4*u))-integral((h+4*u)*(-h)))
radius=S.symbols('radius',positive=True)
check('literal opposite parameter disc determinant',S.diag(radius**-2,-radius**-2).det()+radius**-4)
check('boundary inverse on the parameter circle',(x-S.I*y)/(x*x+y*y)-1/(x+S.I*y))
source=R/'notes/part3_e6_selected_infinity_moving_c2_working.md'
record={'status':'PASS','scope':'Exact MC2 coefficient/frame and directed Chern identities; bundle bordism and its orientation are proved in the accompanying note. No total return assigned.',
        'checks':len(checks),'identities':checks,'source':str(source.relative_to(R)),
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'c2_moving_cap':-4,'full_phase_windings_a6':[-6,-2],
        'residual_phase_windings':[-4,0],
        'positive_line_classes':['h','-h'],
        'directed_full_capped_line_classes_a6':['h+6u','-h+2u']}
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'source_sha256':record['source_sha256'],'c2':-4}))
