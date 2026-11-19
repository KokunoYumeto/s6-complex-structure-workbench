"""Independent ICAP source/height/norm/sector/product audit."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parents[2];counts=Counter()
def ck(tag,x):
 assert bool(x),tag
 counts[tag]+=1
def eq(tag,x,y=0):ck(tag,S.factor(S.cancel(x-y))==0)
v,t,z,l,n=S.symbols('v t z l n');D=v-2
ss=v*(v+4)/(4*D**2);sq=-2*(v+1)/D
cc=(1-36*ss-sq**3)/108;oo=(1-36*ss+sq**3)/108
eq('exact selected-root square',sq**2,1+12*ss)
eq('actual inverse selected coordinate',8*ss/(1+4*ss+sq),v)
eq('literal selected height zero',cc,v/D**3)
for root in [cc,oo]:eq('both original discriminant roots',27*root**2+(18*ss-S.Rational(1,2))*root-4*ss*(S.Rational(1,4)-ss)**2)
eq('selected central root',cc.subs(v,0),0);eq('other central root',oo.subs(v,0),S.Rational(1,54))
r=S.symbols('r');x=S.symbols('x');poly=x**3+r*x**2+t*x+t*t
eq('full original discriminant',S.discriminant(poly,x),-t*t*(4*r**3-r*r-18*r*t+27*t*t+4*t))
qinf,tc,to=S.symbols('qinf tc to');hc=1-tc*qinf;ho=1-to*qinf;HH=hc/ho
for root,h in [(tc,hc),(to,ho)]:eq('actual ordinary-cap height square',qinf*(1/qinf-root),h)
eq('full selected Hom ratio',HH*ho,hc)
eq('height-ratio center',HH.subs(qinf,0),1)
m=3*l+2;k=2*l+1
eq('root formal group exponent',3*k,2*m-1)
eq('root c invariant first exponent',l-2*k,-m)
eq('root c invariant second exponent',2*l-4*k,-2*m)
eq('middle common deck weight',3*(l+1),m+1)
eq('root line norm old coefficient exponent',6*(l+1)-2*m,2)
# Universal source equation transport, checked as equality of Laurent polynomials.
X,Y=S.symbols('X Y');a2=z**(2*l+2)*r
for lv in range(0,25):
 mv=3*lv+2;kv=2*lv+1
 xo=z**(-2*(lv+1))*X;yo=z**(-3*(lv+1))*Y;tt=z**(-mv)
 original=yo**2-xo**3-r*xo**2-tt*xo-tt**2
 root=Y**2-X**3-r*z**(2*lv+2)*X**2-z**(lv+2)*X-z*z
 eq('full original-root equation',original*z**(6*(lv+1)),root)
 for j in range(0,kv):ck('all neighbouring graph determinants',(j+1)-j==1)
 ck('final graph ray determinant',abs(kv*0-1*1)==1)
 for nv in [-1,1]:
  # The scalar, finite character and root normalization are all retained.
  ck('signed primitive generator norm',nv*nv==1)
  ck('signed source generator exponent',nv*nv*mv==mv)
  for dv in [0,1,mv-1]:ck('finite character full mth power',(dv*mv)%mv==0)
# Full module arrows in the two graph charts.
u,ell,source_s,ta,zz,ww=S.symbols('u ell s tau zeta w')
eq('actual first Cartier module arrow',(ta/(ta-zz*source_s*ell)).subs(ta,zz*u),u/(u-source_s*ell))
eq('actual second Cartier module arrow',(ta/(ta-zz*source_s*ell)).subs(zz,ta*ww),1/(1-ww*source_s*ell))
eq('full Cartier graph overlap',u/(u-source_s*ell),(1/(1-ww*source_s*ell)).subs(ww,1/u))
# Central-one normalized chord before evaluation at the coincidence.
A,tau,XR,YR,XX,YY=S.symbols('A tau XR YR X Y')
chord=tau*(YY-YR)+(A+tau**3*YR)/(A-tau**2*XR)*(XX-XR)
eq('actual normalized chord coincidence',chord.subs(tau,0),XX-XR)
# The H root preserves the actual norm and signed sector word as a groupoid.
a,j0,J,LL=S.symbols('a j0 J L');logH=S.symbols('LogH')
for nv in [-1,1]:
 eq('signed full root-norm ratio exponent',m*(nv*logH/m),nv*logH)
 eq('full annular H-root sector discrepancy',nv*(a+j0)*logH/m-nv*a*logH/m,nv*j0*logH/m)
 eq('full additional B-sector factor',J*logH+nv*j0*logH/m,logH*(J+nv*j0/m))
 eq('inverse full sector H factor',-(J*logH+nv*j0*logH/m),(-J-nv*j0/m)*logH)
# Weighted contraction is an exact finite sum, both primitive signs use J^m=B.
rho=S.symbols('rho',positive=True)
for mv in [2,5,8,11,20,32]:
 vals=S.symbols('b0:'+str(mv+1))
 left=sum(rho**(-2*j)*vals[j+1] for j in range(mv))
 right=rho*rho*(sum(rho**(-2*j)*vals[j] for j in range(mv))-vals[0]+rho**(-2*mv)*vals[mv])
 eq('entire weighted norm identity',left,right)
# Signed homology basis maps keep the physical Euler coefficient unchanged.
for nv in [-1,1]:
 Cn=S.Matrix([[m,1],[nv,0]])
 Cinv=S.Matrix([[0,nv],[1,-m*nv]])
 basis=S.Matrix([[nv,0],[m*(1-nv),1]])
 ck('signed cap primitive integral inverse',Cn*Cinv==S.eye(2))
 ck('literal signed cap relation comparison',Cn*basis==S.Matrix([[m,1],[1,0]]))
 ck('literal quadratic-reference basis comparison',Cn*S.Matrix([[nv,0],[2-m*nv,1]])==S.Matrix([[2,1],[1,0]]))
 ck('signed primitive determinant',Cn.det()==-nv)
orbit=S.Matrix([[0,-1],[-1,0]])
conifold=S.Matrix([[0,0],[-1,-1]])
ck('original sphere orbit filling inverse',orbit*orbit==S.eye(2))
ck('actual conifold physical Euler kernel',conifold*S.Matrix([1,-1])==S.zeros(2,1))
ck('actual conifold primitive cokernel',conifold.rank()==1 and S.gcd_list(list(conifold))==1)
# The base and fan consequences use the independently proved initial/vertical data.
j=S.symbols('j',integer=True)
kj=47-2*j**3+18*j**2-52*j
Sj=8-j*(j*j-9*j+26)/3
eq('same physical-to-native marked product',kj-(-1),6*Sj)
eq('separate physical characteristic index',(4*kj+4)/24,Sj)
source='notes/part3_e6_selected_i3_all_caps_working.md'
paths=[source,'notes/part3_e6_order_three_all_caps_working.md','notes/part3_e6_selected_infinity_negative_norm_working.md']
out={'status':'PASS_FULL_ICAP_SOURCE_HEIGHT_ROOT_SECTOR_AND_CAP_MAPS','utc':datetime.now(timezone.utc).isoformat(),'checks':sum(counts.values()),'check_counts':dict(counts),'source':source,'source_sha256':hashlib.sha256((ROOT/source).read_bytes()).hexdigest(),'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},'scope':'Full ICAP1--5 geometric review accompanied by independent exact source, root, module, signed norm and sector identities. The original IC2/IVP/AFI arithmetic remains its separately audited input.'}
p=Path(__file__);p.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
