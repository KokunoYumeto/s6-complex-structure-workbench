"""K93: symbolic evaluation of the actual K92 groupoid algorithm.

No infinity free coordinate is inferred. Combined arrays are exact algebraic
sums of the two K90 states and twice the K71 state; their only use is to
evaluate the class sum already proved in K92.
"""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import sys,json,math,hashlib
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'code/part3_root'))
import source_all_fans as C
import source_zero_all_fans as Z
checks=[]
def chk(name,v):
 if not bool(v):raise AssertionError(name)
 checks.append(name)
def zer(name,v):
 if isinstance(v,s.MatrixBase): chk(name,all(s.factor(x)==0 for x in v))
 else:chk(name,s.factor(v)==0)
a,j,r,u,low=s.symbols('a j r u low')
b=3-a; z=(1-r*low)/u
P=s.Matrix([[u,-r],[low,z]])
J=s.diag(-1,1);Swap=s.Matrix([[0,1],[1,0]])
K=s.Matrix([[0,1,0],[1,0,0],[0,0,1]])
Q0=s.Matrix([[1,-1],[0,1]]);Q1=s.Matrix([[1,0],[-1,1]])
Pref=J*P*Swap; W=s.Matrix([[1,b],[-a,-2]])

def local(P,kind):
 if kind=='Z': B=2*P.inv()*W*P;t=-1
 else:B=-6*P.inv()*s.diag(1,0)*P;t=-3
 B=B.applyfunc(s.factor)
 l=s.Matrix([B[1,1]-B[1,0],B[0,0]-B[0,1],B[1,1]])
 xy=P.inv()*s.Matrix([0,1]);x,y=xy
 w=s.Matrix([x,y,-x-y]);d=s.Matrix([-x-2*y,-2*x-y,x-y])
 I=s.Matrix([t*w[i]+d[i]*(l[i]-t) for i in range(3)])
 D=s.Matrix([t*w[i]-d[i]*(l[i]-t) for i in range(3)])
 return B,l,w,d,I.applyfunc(s.factor),D.applyfunc(s.factor),t
BZ,lZ,w,d,IZ,JZ,tZ=local(P,'Z')
BR,lR,wR,dR,IR,JR,tR=local(Pref,'Z')
BC,lC,wC,dC,IC,JC,tC=local(P,'C')
zer('full winding sum',BZ+Swap*BR*Swap+2*BC+8*s.eye(2))
zer('reflected physical vector',K*wR-w)
zer('combined full circle prisms',IZ+K*IR+2*IC+8*w)
zer('combined full derivative prisms',JZ+K*JR+2*JC+8*w)
zer('reflected Q0 step',J*(P*Q0)*Swap-Pref*Q1)
zer('reflected Q1 step',J*(P*Q1)*Swap-Pref*Q0)
Pj=s.Matrix([[1,0],[j,1]])
zer('first reflected target',J*(Pj*Q0)*Swap-s.Matrix([[1,0],[1-j,1]])*Q0)
Sfan=s.Matrix([[-1,0],[1,1]])
zer('vertical same fan basis',J*Pj*Sfan-s.Matrix([[1,0],[1-j,1]]))

def poly(j):return b*(j+1)*j*(j-1)/3+(3-b)*(j+1)*j/2

def seedZ(j):
 Pj=s.Matrix([[1,0],[j,1]])
 _,_,w,_,I,D,t=local(Pj,'Z');mu=2-a;nu=6*poly(j)
 V=s.Matrix([[2*t-2*mu-2*nu,-I[0],I[0]],[-I[0],I[1],0],[I[0],0,-I[2]]])
 delta=s.Matrix([2*t-2*mu+2*nu,D[1]-D[0],D[0]-D[2]])
 return Pj,V.applyfunc(s.factor),delta.applyfunc(s.factor),poly(j)

def seedC(j):
 h=18*j*(j-1)
 return Pj,s.Matrix([[h,6-12*j,12*j-6],[6-12*j,0,0],[12*j-6,0,0]]),s.Matrix([-12-h,12*j-12,-12*j]),-1-3*j*(j-1)

Vvars=s.symbols('v00 v01 v02 v11 v12 v22')
Dvars=s.symbols('d0:3');unknown=Vvars+Dvars
Vm=s.Matrix([[Vvars[0],Vvars[1],Vvars[2]],[Vvars[1],Vvars[3],Vvars[4]],[Vvars[2],Vvars[4],Vvars[5]]]);Dm=s.Matrix(Dvars)

def solve_first(kind,seed):
 P0,V0,D0,cls=seed;T=P0*Q0
 _,_,w,_,I,D,_=local(T,kind)
 eq=[]
 for i in (1,2):
  vec=s.zeros(3,1);vec[i]=w[i];vec[0]=-w[0]
  rhs=s.zeros(3,1);rhs[i]=I[i];rhs[0]=-I[0]
  eq+=list(Vm*vec-rhs)
  eq.append(w[i]*Dm[i]-w[0]*Dm[0]-D[i]+D[0])
 eq +=[Vm[2,2]-V0[0,0],Dm[2]-(2*V0[0,0]-D0[0])]
 A,rhs=s.linear_eq_to_matrix(eq,unknown)
 chk('complete first target rank '+kind+str(seed[0][1,0]),A.rank()==9)
 sol=s.linsolve((A,rhs),unknown);chk('unique full first target '+kind+str(seed[0][1,0]),len(sol)==1)
 row=next(iter(sol));mp=dict(zip(unknown,row));V=Vm.subs(mp).applyfunc(s.factor);delta=Dm.subs(mp).applyfunc(s.factor)
 chk('no free target unknowns '+kind+str(seed[0][1,0]),not set(unknown).intersection(set().union(*(x.free_symbols for x in list(V)+list(delta)))))
 for e in eq:zer('full first prism row '+str(len(checks)),e.subs(mp))
 divisor=4 if kind=='Z' else 2
 return T,V,delta,s.factor(cls+(D0[0]-V0[0,0])/divisor)

_,V0,D0,S0=solve_first('Z',seedZ(j))
_,VR,DR,SR=solve_first('Z',seedZ(1-j))
_,VC,DC,SC=solve_first('C',seedC(j))
Vsum=(V0+K*VR*K+2*VC).applyfunc(s.factor)
Dsum=(D0+K*DR+2*DC).applyfunc(s.factor)
w0=s.Matrix([1,1,-2]);S0norm=3;D0prod=2
C0=-4*(2*a+1)*D0prod**2
E0=4*D0prod*((2*a+1)*S0norm+2*a-8)
Vexpected=s.Matrix(3,3,lambda i,k:(-8 if i==k else 0)+s.Rational(1,1)*C0/(w0[i]*w0[k]))
Dexpected=s.Matrix([-8+E0/w0[i] for i in range(3)])
zer('complete combined first variation seed',Vsum-Vexpected)
zer('complete combined first derivative seed',Dsum-Dexpected)
zer('vertical class seed',-poly(j)-poly(1-j)-(-1-3*j*(j-1))-(1-a))
zer('actual first class sum',-S0-SR-SC-7*(1-a))

Sval=r*r+r*u+u*u;Dval=r*u*(r+u)
Cval=-4*(2*a+1)*Dval**2;Eval=4*Dval*((2*a+1)*Sval+2*a-8)
w=s.Matrix([r,u,-r-u])
Vbar=s.Matrix(3,3,lambda i,k:(-8 if i==k else 0)+Cval/(w[i]*w[k]))
dbar=s.Matrix([-8+Eval/w[i] for i in range(3)])
for idx in (0,1):
 rp,up=(r+u,u) if idx==0 else (r,u+r)
 Sp=rp**2+rp*up+up**2;Dp=rp*up*(rp+up);wp=s.Matrix([rp,up,-rp-up])
 Cp=-4*(2*a+1)*Dp**2;Ep=4*Dp*((2*a+1)*Sp+2*a-8)
 Vp=s.Matrix(3,3,lambda i,k:(-8 if i==k else 0)+Cp/(wp[i]*wp[k]))
 dp=s.Matrix([-8+Ep/wp[i] for i in range(3)])
 zer('norm generator identity '+str(idx),Sp-Sval-2*Dval/w[idx])
 zer('product generator identity '+str(idx),Dp/wp[2]+Dval/w[idx])
 zer('selected target variation '+str(idx),Vp[2,2]-Vbar[idx,idx])
 zer('selected target derivative '+str(idx),dp[2]-(2*Vbar[idx,idx]-dbar[idx]))
 for h in (1,2):
  vec=s.zeros(3,1);vec[h]=wp[h];vec[0]=-wp[0]
  zer('target full combined prism '+str((idx,h)),Vp*vec+8*vec)
  zer('target derivative combined prism '+str((idx,h)),wp[h]*dp[h]-wp[0]*dp[0]+8*wp[h]-8*wp[0])

def f(a,S):return 1-a-3*(a-1)*(S-1)-(2*a+1)*(S-1)*(S-3)/4
for idx in (0,1):
 rp,up=(r+u,u) if idx==0 else (r,u+r)
 Sp=rp**2+rp*up+up**2
 zer('actual class generator increment '+str(idx),-(dbar[idx]-Vbar[idx,idx])/4-(f(a,Sp)-f(a,Sval)))
zer('first closed value',f(a,3)-7*(1-a))
zer('vertical closed value',f(a,1)-(1-a))
x,y,tau=s.symbols('x y tau',integer=True)
Norm=lambda x,y:x*x+x*y+y*y
zer('norm under swap',Norm(y,x)-Norm(x,y))
zer('norm under rotation',Norm(y,-x-y)-Norm(x,y))
zer('norm under central sign',Norm(-x,-y)-Norm(x,y))
zer('good half-variable polynomial',f(1,2*tau+1)+3*tau*(tau-1))
zer('reduced half-variable polynomial',f(2,2*tau+1)+5*tau**2+tau+1)
zer('good residue period',f(1,2*(tau+28)+1)-f(1,2*tau+1)+28*(6*tau+81))
zer('reduced residue period',f(2,2*(tau+28)+1)-f(2,2*tau+1)+28*(10*tau+141))

def fi(a,S):
 num=4*(1-a)-12*(a-1)*(S-1)-(2*a+1)*(S-1)*(S-3)
 assert num%4==0
 return num//4
images={aa:sorted({fi(aa,2*t+1)%28 for t in range(28)}) for aa in (1,2)}
chk('good complete odd-norm upper image',images[1]==[0,6,8,10,14,20,22,24])
chk('reduced complete odd-norm upper image',images[2]==[5,7,9,13,19,21,23,27])
for xx,yy in ((1,0),(0,1),(1,1)):
 chk('primitive parity class '+str((xx,yy)),Norm(xx,yy)%2==1)

def egcd(a,b):
 if b==0:return (a,1,0)
 g,x,y=egcd(b,a%b);return(g,y,x-(a//b)*y)

witnesses=[]
for aa in (1,2):
 best={}
 for rr in range(25):
  for uu in range(1,25):
   if math.gcd(rr,uu)!=1:continue
   SS=rr*rr+rr*uu+uu*uu;val=fi(aa,SS)%28
   score=(max(rr,uu),rr+uu,SS,rr,uu)
   if val not in best or score<best[val][0]:best[val]=(score,rr,uu,SS)
 chk('all image values have primitive witnesses '+str(aa),sorted(best)==images[aa])
 for val in images[aa]:
  _,rr,uu,SS=best[val];gcd,zz,ss=egcd(uu,rr);P=(uu,-rr,ss,zz)
  chk('witness determinant '+str((aa,val)),C.det(P)==1)
  actualZ=Z.calculate(P,aa,1,0,True);actualR=Z.calculate(C.mul((-1,0,0,1),P),aa,1,0,True);actualC=C.calculate(P,True)
  total=-actualZ['integer_path_sum']-actualR['integer_path_sum']-actualC['integer_path_sum']
  chk('full actual witness algorithms '+str((aa,val)),total==fi(aa,SS) and total%28==val)
  witnesses.append({'a':aa,'residue':val,'physical_pair':[rr,uu],'S':SS,'basis':P,'source_zero':actualZ,'reflected_source_zero':actualR,'selected_cusp':actualC,'integer_groupoid_sum':total})
# A compact independent range exercises both generators and nonzero vertical
# indices after the symbolic complete proof above.
inputs=list(Z.bounded_inputs(8));replays=0
for P in inputs:
 xy=C.inv(P)[1],C.inv(P)[3];SS=Norm(*xy)
 for aa in (1,2):
  total=-Z.calculate(P,aa,1,0)['integer_path_sum']-Z.calculate(C.mul((-1,0,0,1),P),aa,1,0)['integer_path_sum']-C.calculate(P)['integer_path_sum']
  chk('exact full algorithm replay '+str((aa,P)),total==fi(aa,SS));replays+=1
result={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'scope':'Complete symbolic first-step/full-prism/reflected-generator induction evaluating K92; no infinity free-pair identification. Complete image follows the proved residue period and explicit primitive fan witnesses.','checks':len(checks),'symbolic_seed_and_generator_checks':len(checks)-replays,'full_algorithm_replays':replays,'formula':'1-a-3(a-1)(S-1)-(2a+1)(S-1)(S-3)/4','S':'x^2+xy+y^2, (x,y)=P^-1 e2','exact_images':{str(k):v for k,v in images.items()},'witnesses':witnesses,'combined_first_variation':str(Vsum),'combined_first_derivative':str(Dsum),'source_hashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['code/part3_root/source_zero_all_fans.py','code/part3_root/source_all_fans.py','notes/part3_source_infinity_groupoid_all_fans_working.md','notes/part3_source_infinity_closed_formula_working.md','code/part3_fourfold/source_infinity_closed_formula.py']}}
(ROOT/'code/part3_fourfold/source_infinity_closed_formula.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['witnesses','source_hashes']},indent=2))
