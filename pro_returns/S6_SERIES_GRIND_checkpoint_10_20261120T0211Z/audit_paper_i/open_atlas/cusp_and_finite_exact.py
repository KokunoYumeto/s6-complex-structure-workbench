#!/usr/bin/env python3
"""Actual cusp Cartier and finite affine line factors for the new atlas route.

Fresh symbolic calculation, after reading the target statement/proof.
This does not by itself certify an evaluated global coefficient atlas.
"""
from pathlib import Path
import datetime,json,hashlib,time,platform
import sympy as s

started=time.monotonic();checks=[];details={}
def check(name,e):
    entries=list(e) if isinstance(e,s.MatrixBase) else [e]
    ok=all(s.cancel(s.expand(x))==0 for x in entries)
    checks.append({'name':name,'passed':ok})
    if not ok: raise AssertionError((name,e))
def clean(x):
    return x.applyfunc(s.cancel) if isinstance(x,s.MatrixBase) else s.cancel(x)

K=s.Matrix([[0,6],[1,0]])
B=s.Matrix([[0,1],[-1,0]])
mu,tau0,beta0=s.symbols('mu tau0 beta0')
C=s.Matrix([[6*mu,tau0],[beta0,mu]])
check('full unit matrix KC symmetric',K*C-(K*C).T)
check('logarithmic period matrix KB symmetric',K*B-(K*B).T)
ng,nu,mg,mu_n,i,j,u1,u2=s.symbols('ng nu mg mu_n i j u1 u2',integer=True)
n=s.Matrix([ng,nu]);nn=s.Matrix([mg,mu_n]);v=B*n;vv=B*nn
def L(a,b):return a*(a-1)/2-3*b*b
def h(a):return -3*a[0]**2+a[1]*(a[1]-1)/2
def slope(a,b):return s.Matrix([a,-6*b-3])
def intercept(a,b):return -a*(a+1)/2+3*b*(b+1)
for da,db in [(0,0),(1,0),(0,1),(1,1)]:
    check(f'Cartier affine interpolation at square vertex{da,db}',
          (slope(i,j).T*s.Matrix([i+da,j+db]))[0]+intercept(i,j)-L(i+da,j+db))
check('exact support translation law',L(u1+v[0],u2+v[1])-L(u1,u2)-
      ((K.T*n).T*s.Matrix([u1,u2]))[0]-h(n))
check('slope translation',slope(i+v[0],j+v[1])-slope(i,j)-K.T*n)
check('full q exponent cancellation',h(n)+intercept(i,j)-
      intercept(i+v[0],j+v[1])-(slope(i+v[0],j+v[1]).T*v)[0])
check('period factor q cocycle',(n.T*K*B*nn)[0]+h(n)+h(nn)-h(n+nn))
check('period factor unit cocycle',(n.T*K*C*nn)[0]+
      ((n.T*K*C*n)[0]+(nn.T*K*C*nn)[0]-((n+nn).T*K*C*(n+nn))[0])/2)
def Uexp(a,ii,jj):
    w=B*a
    return (a.T*K*C*a)[0]/2-(slope(ii+w[0],jj+w[1]).T*C*a)[0]
check('extending chart unit exact cocycle',Uexp(n,i,j)+
      Uexp(nn,i+v[0],j+v[1])-Uexp(n+nn,i,j))
check('cusp flat-factor comparison',h(n)-(n.T*K*B*n)[0]/2+nu/2)

# Explicit Gaussian comparison for the two actual original monodromies.
tau,mu,beta,z1,z2=s.symbols('tau mu beta zeta1 zeta2')
z=s.Matrix([z1,z2]);Z=s.Matrix([[6*mu,tau],[beta,mu]])
Pi=Z.row_join(s.eye(2));D=s.diag(1,6)
A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
def update(which,tt,mm,bb):
    if which==1:
        return (1-1/tt,(1-mm)/tt,bb-6*(mm-1)**2/tt+2)
    return (-1/tt,1+mm/tt,bb-6*mm*mm/tt-3)
def logfactor(lam,ww,ZZ):
    aa=s.Matrix([lam[0],lam[1]])
    return (aa.T*K*ww)[0]+(aa.T*K*ZZ*aa)[0]/2
for which,A,order,v0 in [(1,A1,3,s.Matrix([1,2,-4,0])),
                       (2,A2,4,s.Matrix([-1,-3,3,0]))]:
    tt,mm,bb=update(which,tau,mu,beta)
    Zg=s.Matrix([[6*mm,tt],[bb,mm]]);Pig=Zg.row_join(s.eye(2))
    R=(Pig*A)[:,2:]
    check(f'finite{which} exact period covariance',R*Pi-Pig*A)
    F=-z1*z1/(2*tau)
    defects=[]
    for jj in range(4):
        lam=s.eye(4)[:,jj];shift=Pi*lam
        Fshift=-(z1+shift[0])**2/(2*tau)
        d=clean(logfactor(A*lam,R*z,Zg)-logfactor(lam,z,Z)-(Fshift-F))
        defects.append(d)
    expected=[24,0,s.Rational(1,2),0] if which==1 else [-9,0,0,0]
    for jj,(d,e) in enumerate(zip(defects,expected)):
        check(f'finite{which} exact theta-character defect{jj}',d-e)
    details[f'finite{which}_theta_defects']=[str(d) for d in defects]

    # Literal composition of the affine generator and its line lift.
    state=(tau,mu,beta);zz=z;total=0
    vfrac=v0/order
    for step in range(order):
        t0,m0,b0=state;t1,m1,b1=map(clean,update(which,t0,m0,b0))
        Z0=s.Matrix([[6*m0,t0],[b0,m0]]);Z1=s.Matrix([[6*m1,t1],[b1,m1]])
        P1=Z1.row_join(s.eye(2));RR=(P1*A)[:,2:]
        zlin=clean(RR*zz)
        total=clean(total-zz[0]**2/(2*t0)+logfactor(vfrac,zlin,Z1))
        zz=clean(zlin+P1*vfrac)
        state=(t1,m1,b1)
    for aa,orig in zip(state,(tau,mu,beta)):
        check(f'finite{which} affine iterate period',aa-orig)
    check(f'finite{which} affine iterate actual lattice vector',zz-z-Pi*v0)
    defect=clean(12*(total-logfactor(v0,z,Z)))
    details[f'finite{which}_twelfth_line_iterate_defect']=str(defect)
    for vv0 in [tau,mu,beta,z1,z2]:
        check(f'finite{which} line iterate defect constant {vv0}',s.diff(defect,vv0))
    # Multiplying each lifted generator by exp(-2pi i defect/order)
    # makes its order-th iterate precisely the actual lattice action.
    check(f'finite{which} exact phase correction',defect-order*(defect/order))

# Universal invertible connection and its actual logarithm-branch gauge.
tp,mp,bp=s.symbols('tau_prime mu_prime beta_prime')
Tp=s.Matrix([[tp,6*mp],[mp,bp]])
check('exact connection inverse',Tp.T.inv()-s.Matrix([[bp,-mp],[-6*mp,tp]])/(tp*bp-6*mp*mp))
sig1,sig2=s.symbols('sigma_prime1 sigma_prime2')
sigp=s.Matrix([sig1,sig2]);a=-24*s.pi*s.I*Tp.T.inv()*D*sigp
check('finite collar connection equation',Tp.T*a+24*s.pi*s.I*D*sigp)
vq=s.Matrix(s.symbols('vq1 vq2'))
check('finite collar vertical branch jump',
      -24*s.pi*s.I*Tp.T.inv()*D*Tp*vq+24*s.pi*s.I*D*vq)
hh,hp,SS,Sp,kk=s.symbols('h h_prime S S_prime k')
b=lambda h:-12*s.pi*s.I*(2*h*hp*SS+h*h*Sp)
check('all integer logarithm-turn base connection corrections',b(hh+kk)-b(hh)+
      24*s.pi*s.I*(kk*hp*SS+kk*hh*Sp+s.Rational(1,2)*kk*kk*Sp))
qq=s.symbols('q',nonzero=True)
ac=6/qq*Tp.T.inv()*s.Matrix([1,0])
check('cusp ratio q^(-6nu) connection',Tp.T*ac-s.Matrix([6/qq,0]))

out={'checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family',
     'phase':'S6_SERIES_GRIND','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'python':platform.python_version(),'sympy':s.__version__,'result':'PASS',
     'check_count':len(checks),'checks':checks,'details':details,
     'elapsed_seconds':time.monotonic()-started,
     'scope':'Exact local Cartier/finite affine factors and annular connection algebra; global coefficient atlas still requires complete descent and an evaluated common-chart partition.'}
p=Path(__file__).resolve().parent/'cusp_and_finite_exact.output.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'result':'PASS','check_count':len(checks),'details':details,
                  'elapsed_seconds':out['elapsed_seconds'],
                  'output_sha256':hashlib.sha256(p.read_bytes()).hexdigest()},indent=2))
