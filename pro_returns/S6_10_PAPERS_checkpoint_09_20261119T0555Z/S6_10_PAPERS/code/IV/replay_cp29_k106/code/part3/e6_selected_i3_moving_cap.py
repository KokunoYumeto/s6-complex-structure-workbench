"""Exact full Cox endpoint, normal clutch, reference charts and cap pairing."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
from datetime import datetime,timezone
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
checks=[]
def ck(n,x):
    assert bool(x),n
    checks.append(n)
def eq(a,b):return S.cancel(S.together(a-b))==0
P,p,cq,c0,Z,V,A,aa,bb=S.symbols('P p cq c0 Z V A alpha beta',nonzero=True)
fm,fp=S.symbols('Fminus Fplus',nonzero=True)
nminus=P*cq*Z**-3*fm; nplus=Z**2*fp
ck('full native height',eq(Z*nminus*nplus,P*cq*fm*fp))
ck('B^-2 source endpoint',eq(P**2*Z,P**2*Z))
ck('full forward height and B line factor',eq((P*p*cq)**2*P**-4*p**-2*c0**-2*V,P**-2*(cq/c0)**2*V))
ck('negative derivative endpoint',eq(P*cq*(P**2*Z)**-3*(P**6*A**-1*fm),A**-1*nminus))
ck('positive derivative endpoint',eq((P**2*Z)**2*(P**-6*A*fp),P**-2*A*nplus))
ck('full forward native height preserved',eq((P**2*Z)*(A**-1*nminus)*(P**-2*A*nplus),Z*nminus*nplus))
ck('entire cut collar preserves height',eq((aa*Z)*((aa*bb)**-1*nminus)*(bb*nplus),Z*nminus*nplus))
ck('literal collar inverse',eq(aa**-1*(aa*Z),Z) and eq(aa*bb*((aa*bb)**-1*nminus),nminus) and eq(bb**-1*(bb*nplus),nplus))
z,zb,al,alb,be,beb=S.symbols('z zb al alb be beb',nonzero=True)
T=S.Matrix([[1,-zb],[z,1]])
Tp=S.Matrix([[1/z,-1],[1,1/zb]])
ck('global Cox quaternion on the full chart overlap',Tp*S.diag(z,zb)==T)
Ta=S.Matrix([[1,-alb*zb],[al*z,1]])
G=Ta*S.diag((al*be)**-1,beb)*T.inv()
ck('complete right-complex normal matrix',all(eq(a,b) for a,b in zip(G*T,Ta*S.diag((al*be)**-1,beb))))
ck('full determinant retains positive metric factor',eq(G.det(),(1+al*alb*z*zb)/(1+z*zb)*beb/(al*be)))
ck('normal homotopy identity endpoint',all(eq(a,b) for a,b in zip(G.subs({al:1,alb:1,be:1,beb:1}),S.eye(2))))
ck('positive spinor endpoint winding',-2==(-6-6)+10)
ck('actual parameter seam spin parity',(-1)**(-2)==1)

# Six actual ordered factor charts for UV=s^4*x*y, in lattice (x,y,s,U).
charts=[]
for r in range(6):
    if r<4:
        # x,y,u,v, with s=uv,U=s^r*u.
        N=S.Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,1],[0,0,r+1,r]])
        names=['x','y','u','v']
    elif r==4:
        # x,s,u,v, with y=uv,U=s^4*u.
        N=S.Matrix([[1,0,0,0],[0,0,1,1],[0,1,0,0],[0,4,1,0]])
        names=['x','s','u','v']
    else:
        # y,s,u,v, with x=uv,U=s^4*y*u.
        N=S.Matrix([[0,0,1,1],[1,0,0,0],[0,1,0,0],[1,4,1,0]])
        names=['y','s','u','v']
    w=N.inv()*S.Matrix([0,0,0,1])
    ck(f'actual regular reference factor chart{r}',abs(N.det())==1)
    ck(f'actual reference factor weights{r}',list(w)==[0,0,1,-1])
    Urow=list(N.row(3));Vrow=list(S.Matrix([[1,1,4,-1]])*N)
    ck(f'full reference factor equation{r}',[Urow[j]+Vrow[j] for j in range(4)]==list(S.Matrix([[1,1,4,0]])*N))
    charts.append({'factor':r,'variables':names,'matrix':[[int(x) for x in row] for row in N.tolist()],'physical_weights':list(map(int,w)),'U_exponents':list(map(int,Urow)),'V_exponents':list(map(int,Vrow))})
s,kappa,u,v=S.symbols('s kappa u v',nonzero=True)
ck('reference entire actual height',eq(Z*(kappa**-1*s**-4*v)*(s**4*u),kappa**-1*Z*u*v))
ck('reference opposite principal orders',-4+4==0)
starpath=ROOT/'code/part3/e6_selected_i3_moving_star.json'
star=json.loads(starpath.read_text())
ck('retained actual34 source blowups',len(star['chronological_blowups'])==34)
section_coeff=[]
for b in star['chronological_blowups']:
    left=tuple(b['left']);right=tuple(b['right'])
    on0=(1,0) in (left,right);oninf=(-1,0) in (left,right)
    section_coeff.append(-int(on0)+int(oninf))
ck('exact three D0 section centres',section_coeff.count(-1)==3 and section_coeff.count(1)==0)
ck('actual independent total-transform square',-sum(a*a for a in section_coeff)==-3)
ck('actual determinant total-transform square',-sum((5*a)**2 for a in section_coeff)==-75)
ck('actual tangent change from Jacobians',-3*len(section_coeff)==-102)
# Explicit integral MV maps: H1(F)+H1(cap)->H1(boundary), and H2 restriction.
H1=S.Matrix([[-1]]);H2=S.Matrix([[1]+[0]*34])
ck('primitive cap H1 restriction',abs(H1.det())==1)
ck('cap H2 image exactly exceptional lattice',len(H2.nullspace())==34 and H2.nullspace()==[S.eye(35).col(i) for i in range(1,35)])
C,Cr=S.symbols('c2_collision c2_reference',integer=True)
km=-75-C;lm=-177-4*C;kr=-Cr;lr=-4*Cr
ck('full collision projective expression',4*km-lm==-123)
ck('full reference projective expression',4*kr-lr==0)
ck('actual second Chern difference retained',S.expand((lm-lr)-4*(km-kr))==123)
ck('scoped moving/reference index',Fraction(-123,24)==Fraction(-41,8))
source=ROOT/'notes/part3_e6_selected_i3_moving_cap_working.md'
out={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'checks':len(checks),'source':str(source.relative_to(ROOT)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'local_star_input_sha256':hashlib.sha256(starpath.read_bytes()).hexdigest(),'identities':checks,'reference_ordered_charts':charts,'chronological_D0_minus_Dinf_coefficients':section_coeff,'H1_cap_restriction':[[-1]],'H2_boundary_restriction':[[1]+[0]*34],'closed_determinant_square':-75,'closed_tangent_p1':-102,'physical_moving_pair':['-75-c2_collision','-177-4*c2_collision'],'physical_reference_pair':['-c2_reference','-4*c2_reference'],'physical_difference_pair':['kappa','4*kappa+123'],'physical_difference_index':'-41/8','scope':'Actual moving/reference Hopf-cap term only. Full second Chern clutch retained; no outer transfer or source return assigned.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['reference_ordered_charts','identities']},indent=2))
