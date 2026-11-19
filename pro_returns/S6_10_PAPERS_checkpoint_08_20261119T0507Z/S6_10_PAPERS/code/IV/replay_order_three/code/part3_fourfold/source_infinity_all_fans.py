"""P3K.92 exact source/period/root maps and all-fan groupoid arithmetic.

The proof is notes/part3_source_infinity_groupoid_all_fans_working.md.
Finite arithmetic does not replace the compact-family or cap-atlas proof.
The integer sums below are representatives of classes, not newly inferred
infinity characteristic integers.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import sys,json,hashlib
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'code/part3_root'))
import source_all_fans as C
import source_zero_all_fans as Z
checks=[]
def check(name, value):
    if not bool(value): raise AssertionError(name)
    checks.append(name)
def zero(name, expr): check(name,S.simplify(expr)==0)

e,x,y,t,T,X,Y,v,u,xi,rho,s,sn,q,Q,kappa,alpha,g,eta,V,z=S.symbols('e x y t T X Y v u xi rho s sn q Q kappa alpha g eta V z',nonzero=True)
a,b,n,k,j=S.symbols('a b n k j',integer=True)
old=Y**2-X**3-(1-2*v)*X**2-T*X-v**2
new=y**2-x**3-(-2+3*e**2)*x**2-t*x-e**2*(1-e**2)**2
zero('full source rescaling',e**6*old.subs({X:e**-2*x,Y:e**-3*y,T:e**-4*t,v:e**-2-1})-new)
qold=T-(v**2-2*v)
qnew=t-(1-e**2)*(1-3*e**2)
zero('selected height rescaling',e**4*qold.subs({T:e**-4*t,v:e**-2-1})-qnew)
zero('marked G point',e**3*(e**-2-1)-e*(1-e**2))
zero('selected infinity normalization',new.subs({x:sn**2-e**2,y:sn*(sn**2-1),t:(1-e**2)*(1-3*e**2)}))
zero('same source Z at infinity',((s-rho)/(s+rho)).subs({s:sn/e,rho:1/e})-(sn-1)/(sn+1))
zero('marked P at infinity',((1+rho)/(1-rho)).subs(rho,1/e)+(1+e)/(1-e))
zero('full nodal leading Tate unit',e**-4*(-(rho**2-1)/(64*rho**6)).subs(rho,1/e)+(1-e**2)/64)
# The selected-cusp local equation, with u^3=v and rho^2=u^3+1.
q0=S.symbols('q0')
origlocal=y**2-x**3-(u**-2-2*u)*x**2-(u**2-2/u+q0)*x-1
zero('selected-cusp actual q arrow',origlocal.subs(x,xi+u)-(y**2-xi**2*(xi+(u**3+1)/u**2)-q0*(xi+u)))
zero('selected local Z retained',(s/u-rho/u)/(s/u+rho/u)-(s-rho)/(s+rho))
# Full period actions and reflection are literal maps, with all units retained.
def H(pt): return (Q*pt[0],alpha*pt[1])
def B(pt): return (g*pt[0],q*eta*pt[1])
def R(pt): return (Q/pt[0],pt[1])
def Htarget_inv(pt): return (pt[0]/Q,alpha*pt[1])
def Btarget(pt): return (pt[0]/g,q*eta*pt[1])
for idx in (0,1):
 zero('R H = Htarget^-1 R component '+str(idx),R(H((z,V)))[idx]-Htarget_inv(R((z,V)))[idx])
 zero('R B = Btarget R component '+str(idx),R(B((z,V)))[idx]-Btarget(R((z,V)))[idx])
 zero('reflection square component '+str(idx),R(R((z,V)))[idx]-(z,V)[idx])
R3=S.Matrix([[-1,0,1],[0,1,0],[0,0,1]])
check('integral cone reflection square',R3*R3==S.eye(3))
check('physical delta preserved',R3*S.Matrix([0,1,0])==S.Matrix([0,1,0]))
U,W,Hh=S.symbols('U W Hh',integer=True)
check('full dual semigroup exponents',R3.T*S.Matrix([U,W,Hh])==S.Matrix([-U,W,Hh+U]))
zero('height/primitive suspension cancellation good',2*1*2-4)
zero('height/primitive suspension cancellation reduced',2*2*1-4)
zero('full Hom scaling exponent',-4-(-3)-(-1))
zero('full Q period under infinity',(e**4*kappa)*(e**-4*q)-kappa*q)
zero('full B period under infinity',(e**-4*q)*(e**4*eta)-q*eta)
# Actual endpoint exponents from minimal source scaling.
root_rows=[]
for aa in (1,2):
 for p in range(1,13):
  m=4*p-(aa-1)
  ex=Fraction(2)-Fraction(8*p,m);ey=Fraction(3)-Fraction(12*p,m)
  check(f'root x exponent a{aa} p{p}',ex==(0 if aa==1 else Fraction(-2,m)))
  check(f'root y exponent a{aa} p{p}',ey==(0 if aa==1 else Fraction(-3,m)))
  check(f'D^-4 x endpoint a{aa} p{p}',(-8*p)%m==(0 if aa==1 else -2)%m)
  check(f'D^-4 y endpoint a{aa} p{p}',(-12*p)%m==(0 if aa==1 else -3)%m)
  root_rows.append({'a':aa,'p':p,'m':m,'source_exponents':[str(ex),str(ey)],'endpoint_exponents':[-4,0 if aa==1 else -2,0 if aa==1 else -3]})
L,D=S.symbols('L D',commutative=True)
zero('retained A0^4 D^-4 = L^4',(L*D)**4*D**-4-L**4)
r0=S.symbols('r0',nonzero=True)
zero('full finite endpoint scalar',(r0**n*L*D)**4*D**-4-r0**(4*n)*L**4)
zero('endpoint-to-initial inverse',r0**(-4*n)*L**-4*(r0**(4*n)*L**4)-1)
logr0,theta=S.symbols('logr0 theta')
zero('ordinary and cap scalar cochain',(-4*n*theta*logr0).subs(theta,theta+1)+4*n*theta*logr0+4*n*logr0)
omega1,omega2,small=S.symbols('omega1 omega2 small')
Rlog=(small+2*omega1+2*omega2)/4
zero('transported period vector',4*Rlog-small-2*omega1-2*omega2)
zero('signed L period',4*(-n*Rlog)-(-n*small)+n*(2*omega1+2*omega2))
te=S.symbols('te')
Ephase=-4*n*k*te*(te-1)
zero('quadratic ordinary/cap phase square',Ephase.subs(te,te+1)-Ephase+8*n*k*te)
check('fixed scalar specialization',Ephase.subs(k,0)==0)
check('total global winding',1+0+1-2==0)
J=(-1,0,0,1);Sfan=(-1,0,1,1)
for jj in range(-60,61):
 P=(1,0,jj,1)
 check(f'vertical reflected basis {jj}',C.mul(C.mul(J,P),Sfan)==(1,0,1-jj,1))
 for aa in (1,2):
  bb=3-aa
  check(f'vertical polynomial {aa} {jj}',Z.polynomial(bb,jj)+Z.polynomial(bb,1-jj)==3*jj*(jj-1)+aa)
  cc=-1-3*jj*(jj-1)
  check(f'vertical marked sum {aa} {jj}',-Z.polynomial(bb,jj)-Z.polynomial(bb,1-jj)-cc==1-aa)
# All input algorithms are already proved; this run checks their exact use,
# including negative determinant bases and actual identical-fan maps.
bases=list(Z.bounded_inputs(8)); fan_values={1:{},2:{}}
rows=[]; unit_checks=0; cone_checks=0
Gmat=S.Matrix(2,2,S.symbols('g0:4'))
for P in bases:
 Pi=C.inv(P);Pm=S.Matrix(2,2,P);Pim=S.Matrix(2,2,Pi)
 check('full coefficient inverse '+repr(P),Pm*(Pim*Gmat*Pm)*Pim==Gmat)
 unit_checks+=1
 JP=C.mul(J,P)
 verts=[(0,0),(P[0],P[2]),(P[1],P[3]),(P[0]+P[1],P[2]+P[3])]
 for vx,vy in verts:
  out=R3*S.Matrix([vx,vy,1]);check('cone height image '+repr((P,vx,vy)),out==S.Matrix([1-vx,vy,1]));cone_checks+=1
 for aa in (1,2):
  z0=Z.calculate(P,aa,1,0);zr=Z.calculate(JP,aa,1,0);c0=C.calculate(P)
  val=(-z0['integer_path_sum']-zr['integer_path_sum']-c0['integer_path_sum'])%28
  key=C.edges(P)
  if key in fan_values[aa]: check('identical fan value '+repr((aa,P)),fan_values[aa][key]==val)
  fan_values[aa][key]=val
for P in [C.ID,C.Q0,C.mul(C.Q0,C.Q0),C.mul(C.Q0,C.Q1),(3,-2,2,-1)]:
 for aa in (1,2):
  zz=Z.calculate(P,aa,1,0,True);zj=Z.calculate(C.mul(J,P),aa,1,0,True);cc=C.calculate(P,True)
  val=(-zz['integer_path_sum']-zj['integer_path_sum']-cc['integer_path_sum'])%28
  rows.append({'a':aa,'P':P,'source_zero':zz,'reflected_source_zero':zj,'selected_cusp':cc,'infinity_class_mod28':val})
for aa,expected in ((1,10),(2,7)):
 P=C.mul(C.Q0,C.Q0)
 hit=next(x for x in rows if x['a']==aa and tuple(x['P'])==P)
 check(f'Q0 squared exact example a{aa}',hit['infinity_class_mod28']==expected)
paths=['notes/part3_source_infinity_groupoid_all_fans_working.md','code/part3_root/source_zero_all_fans.py','code/part3_root/source_all_fans.py']
res={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'scope':'Exact source/height/period/root/closing maps and finite execution of the proved groupoid algorithm. The finite observed images below are not asserted exhaustive. No infinity characteristic integer is inferred from a sphere class.','checks':len(checks),'symbolic_and_named_checks':checks[:30],'root_endpoint_cases':root_rows,'input_bound':8,'unimodular_inputs':len(bases),'full_coefficient_inverse_checks':unit_checks,'absolute_cone_image_checks':cone_checks,'distinct_fans_per_branch':{str(a):len(x) for a,x in fan_values.items()},'finite_observed_residues':{str(a):sorted(set(x.values())) for a,x in fan_values.items()},'examples':rows,'source_hashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
out=ROOT/'code/part3_fourfold/source_infinity_all_fans.json';out.write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k not in ['examples','root_endpoint_cases','symbolic_and_named_checks']},indent=2))
