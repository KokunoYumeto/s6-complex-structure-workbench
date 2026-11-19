#!/usr/bin/env python3
"""Independent P1.18 analytic recurrences, bounds and map certificates.
Reads the clean statement data only. It never imports an earlier producer.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import sys,json,re,math,time
sys.path.insert(0,str(Path('build/continuation_numeric/python').resolve()))
import sympy as sp
from flint import arb,acb,acb_mat,fmpq,ctx
ctx.prec=256
START=time.time(); checks=[]
def check(name,ok):
    if not ok: raise AssertionError(name)
    checks.append(name)
def qa(x):
    x=F(x);return arb(fmpq(x.numerator,x.denominator))
def frac(x):return F(int(sp.numer(x)),int(sp.denom(x)))
def ident(n=6):return acb_mat(n,n,[int(i==j) for i in range(n) for j in range(n)])
def azero(n=6):return acb_mat(n,n)
def smat(M):return acb_mat(M.rows,M.cols,[qa(frac(v)) for v in M])
def amax(xs):
    it=iter(xs);v=next(it)
    for x in it:v=v.max(x)
    return v

def norm(M,w):
    return amax([sum((abs(M[i,j])*qa(w[j]/w[i]) for j in range(6)),arb(0)) for i in range(6)])
def abs_matrix(M):return acb_mat(6,6,[M[i,j].abs_upper() for i in range(6) for j in range(6)])
def matrix_contains(M,N):
    return all(M[i,j].contains(N[i,j]) for i in range(M.nrows()) for j in range(M.ncols()))
def matrix_overlaps(M,N):
    return all(M[i,j].overlaps(N[i,j]) for i in range(M.nrows()) for j in range(M.ncols()))
def poly_eval(coeff,z):
    y=azero()
    for c in reversed(coeff):y=y*z+c
    return y

def inflate(M,tau,w):
    return acb_mat(6,6,[M[i,j]+acb(arb(0,tau*qa(w[i]/w[j])),arb(0,tau*qa(w[i]/w[j]))) for i in range(6) for j in range(6)])
def mat_strings(M):return [[str(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def root_bracket(c,m,digits=32):
    D=10**digits;lo=0;hi=2*D
    while F(hi,D)**m<c:hi*=2
    while hi-lo>1:
        mid=(lo+hi)//2
        if F(mid,D)**m<=c:lo=mid
        else:hi=mid
    check('exact rational root bracket '+str((c,m)),F(lo,D)**m<=c<=F(hi,D)**m)
    return F(lo,D),F(hi,D)

packet=Path('analysis/continuation_V/P1_18_analytic_certificate_statement_packet.md')
data=json.loads(re.search(r'```json\n(.*?)\n```',packet.read_text(),re.S).group(1))
w=list(map(F,[1,F(1,128),F(1,128),F(1,32),F(1,64),F(1,32)]))
outputs={};root_data={};NROOT=3000
for key,m,c in [('zero',4,F(256,3125)),('infinity',5,F(3125,256))]:
    x=sp.Symbol('t' if key=='zero' else 'u')
    source=sp.Matrix([[sp.sympify(v,locals={str(x):x}) for v in row] for row in data['root_connection_matrices'][key]])
    cc=sp.Rational(c.numerator,c.denominator)
    numerator=source.applyfunc(lambda e:sp.cancel(e*(1+x**m/cc)))
    C=[numerator.applyfunc(lambda e:sp.Poly(e,x).nth(k)) for k in range(m)]
    check(key+' exact original-root polynomial connection',source==((sum((C[k]*x**k for k in range(m)),sp.zeros(6)))/(1+x**m/cc)).applyfunc(sp.cancel))
    check(key+' numerator degree',all(sp.degree(e,x)<=m-1 for e in numerator if e!=0))
    alow,aup=root_bracket(c,m);alpha=qa(c).root(m)
    B=[smat(C[k])*acb(alpha**(k+1)) for k in range(m)]
    b=max(sum((abs(frac(C[k][i,j]))*aup**(k+1)*w[j]/w[i] for k in range(m) for j in range(6)),F(0)) for i in range(6))
    R=qa(F(999,1000));r=qa(F(98,100));K=(qa(b)*(-(1-R).log()/m+qa(F(m-1,m))*R)).exp()
    coeff=[ident()]
    for n in range(NROOT):
        rhs=azero()
        for k in range(min(m-1,n)+1):rhs+=coeff[n-k]*B[k]
        if n>=m:rhs-=coeff[n-m+1]*(n-m+1)
        coeff.append(rhs/(n+1))
    check(key+' all3001 coefficient matrices finite',all(z.is_finite() for M in coeff for z in M.entries()))
    # Separate exact rational original-coordinate power series, using the
    # full geometric expansion of the connection rather than the finite
    # denominator recurrence above.
    V=[sp.eye(6)]
    for n in range(12):
        rhs=sp.zeros(6)
        for j in range(n+1):
            k=n-j;Gk=C[k%m]*(-1/cc)**(k//m)
            rhs+=V[j]*Gk
        V.append(rhs/(n+1))
    for n in range(13):
        exact=smat(V[n])*acb(alpha**n)
        check(key+' independently expanded coefficient '+str(n),matrix_overlaps(coeff[n],exact))
    tau=K*(r/R)**(NROOT+1)/(1-r/R)
    check(key+' finite positive root tail',tau.is_finite() and tau>0)
    # Explicit actual convex rectangle, with true maximum corner radius.
    z0=acb(qa(F(2,5)),qa(F(1,5)))
    hx=qa(F(1,100));hy=qa(F(3,200));rho=(hx*hx+hy*hy).sqrt()
    rrect=((qa(F(2,5))+hx)**2+(qa(F(1,5))+hy)**2).sqrt()
    check(key+' rectangle in Cauchy disc',rrect<R)
    trect=K*(rrect/R)**(NROOT+1)/(1-rrect/R)
    centre=inflate(poly_eval(coeff,z0),K*(abs(z0)/R)**(NROOT+1)/(1-abs(z0)/R),w)
    A=acb_mat(6,6,[sum((B[k][i,j].abs_upper()*rrect**k for k in range(m)),arb(0))/(1-rrect**m) for i in range(6) for j in range(6)])
    err=abs_matrix(centre)*((A*acb(rho)).exp()-ident())
    check(key+' rectangle exponential error finite',all(z.is_finite() for z in err.entries()))
    # Explicit midpoint coefficient radii and derivative error for every
    # entry, retaining each complex ball's real and imaginary radii.
    mid=[acb_mat(6,6,[q.mid() for q in M.entries()]) for M in coeff]
    midvalue=poly_eval(mid,z0)
    errors=[]
    for i in range(6):
        for j in range(6):
            coefferr=arb(0);deriv=arb(0);p0=arb(1);pr=arb(1)
            for n,M in enumerate(coeff):
                q=M[i,j];epsilon=q.real.rad()+q.imag.rad()
                coefferr+=epsilon*p0;p0*=abs(z0)
                if n:deriv+=n*q.abs_upper()*pr;pr*=rrect
            errors.append(coefferr+rho*deriv+trect*qa(w[i]/w[j]))
    check(key+' midpoint rectangle errors finite',all(e.is_finite() and e>=0 for e in errors))
    # The universal elementary integral inequality is additionally tested
    # as an exact polynomial with nonnegative coefficients on [0,1].
    ss=sp.Symbol('s');difference=sum(ss**j-ss**m for j in range(1,m))/m
    check(key+' exact Gronwall majorant numerator',sp.expand((m-(m-1)*ss)*sum(ss**j for j in range(m))/m-1-difference)==0)
    fingerprint=sha256('\n'.join(str(v) for M in coeff for v in M.entries()).encode()).hexdigest()
    outputs[key]={'m':m,'alpha_bracket':[str(alow),str(aup)],'b_upper_exact':str(b),'K_at_999_1000':str(K),'N':NROOT,'tail_at_98_100':str(tau),'coefficients_sha256':fingerprint,'rectangle':{'centre':str(z0),'halfwidths':[str(hx),str(hy)],'actual_max_radius':str(rrect),'rho':str(rho),'max_ODE_entry_error':str(amax([v.abs_upper() for v in err.entries()])),'max_midpoint_entry_error':str(amax(errors))}}
    root_data[key]=(B,coeff,K,R)
    print(key+' root recurrence3000 and rectangle bounds complete',flush=True)

# Cusp: exact commutator operator and both recurrences.
Rrat=sp.Matrix([[sp.Rational(v) for v in row] for row in data['Rcusp']]);Arat=sp.Matrix([[sp.Rational(v) for v in row] for row in data['R0']])
check('actual cusp R squared zero',Rrat*Rrat==sp.zeros(6))
adop=sp.kronecker_product(Rrat.T,sp.eye(6))-sp.kronecker_product(sp.eye(6),Rrat)
check('actual column-vec ad cubed zero',adop**3==sp.zeros(36))
check('actual ad square nonzero',adop**2!=sp.zeros(36))
for n in [1,2,7]:check('finite inverse operator n='+str(n),(n*sp.eye(36)-adop)*(sp.eye(36)+adop/n+adop**2/n**2)/n==sp.eye(36))
wc=[F(100),F(1),F(1),F(1),F(1),F(1)]
r0=max(sum(abs(frac(Rrat[i,j]))*wc[j]/wc[i] for j in range(6)) for i in range(6));a0=max(sum(abs(frac(Arat[i,j]))*wc[j]/wc[i] for j in range(6)) for i in range(6));C0=1+2*r0+4*r0*r0;gamma=C0*a0
Rb,Ab=smat(Rrat),smat(Arat)
def ad(Q):return Q*Rb-Rb*Q
P=[ident()];S=azero();cn=arb(1)
for n in range(1,601):
    S=P[-1]*Ab-S
    P.append((S+ad(S)/n+ad(ad(S))/(n*n))/n)
    cn*=qa((gamma+n-1)/n)
    check('cusp finite majorant coefficient '+str(n),norm(P[-1],wc)<cn)
# Independently use one-step exact rational C2 for initial coefficients.
Pr=[sp.eye(6)]
for n in range(1,11):
    Q=Pr[-1]*Rrat-Rrat*Pr[-1]+Pr[-1]*Arat-(n-1)*Pr[-1]
    adQ=Q*Rrat-Rrat*Q;ad2=adQ*Rrat-Rrat*adQ
    Pr.append((Q+adQ/n+ad2/n**2)/n)
    check('cusp alternative exact recurrence '+str(n),matrix_overlaps(P[n],smat(Pr[n])))
sc=qa(F(2,5));rc=qa(F(1,4));Kc=(-(1-sc).log()*qa(gamma)).exp();tc=Kc*(rc/sc)**601/(1-rc/sc);inner=qa(F(1,100));ti=Kc*(inner/sc)**601/(1-inner/sc)
innerabs=[]
for i in range(6):
    for j in range(6):innerabs.append(sum((P[n][i,j].abs_upper()*inner**n for n in range(1,601)),arb(0))+ti*qa(wc[i]/wc[j]))
check('cusp inner-disc full absolute sums finite',all(x.is_finite() for x in innerabs))
outputs['cusp']={'r0_exact':str(r0),'a0_exact':str(a0),'C0_exact':str(C0),'gamma_exact':str(gamma),'N':600,'K_at_2_5':str(Kc),'tail_at_1_4':str(tc),'tail_at_1_100':str(ti),'inner_abs_error_entries':[[str(innerabs[i*6+j]) for j in range(6)] for i in range(6)],'coefficients_sha256':sha256('\n'.join(str(v) for M in P for v in M.entries()).encode()).hexdigest()}
print('cusp recurrence600, exact commutator and majorants complete',flush=True)

# Actual local collar Taylor steps, continuing the freshly computed
# infinity solution through z=1 on the positive real ray.
B,U,K,R=root_data['infinity'];zeta=[acb(0,arb.pi()*(2*j+1)/5).exp() for j in range(5)]
def transition(z0,delta,tag):
    distances=[abs(acb(z0)-z) for z in zeta];rloc=distances[0]
    for d in distances[1:]:rloc=rloc.min(d)
    rloc/=2;dlow=arb(1)
    for d in distances:dlow*=d-rloc
    check(tag+' denominator lower positive',dlow>0)
    ratio=abs(acb(delta))/rloc;check(tag+' radius ratio below0.3',ratio<qa(F(3,10)))
    q=[math.comb(5,j)*acb(z0)**(5-j)+(1 if j==0 else 0) for j in range(6)]
    Bt=[]
    for j in range(5):
        Q=azero()
        for k in range(j,5):Q+=B[k]*(math.comb(k,j)*acb(z0)**(k-j))
        Bt.append(Q)
    bmax=amax([sum((Bt[k][i,j].abs_upper()*qa(w[j]/w[i])*rloc**k for k in range(5) for j in range(6)),arb(0)) for i in range(6)])
    M=bmax/dlow;bound=(M*rloc).exp();T=[ident()]
    for n in range(160):
        rhs=azero()
        for j in range(min(4,n)+1):rhs+=T[n-j]*Bt[j]
        for j in range(1,min(5,n)+1):rhs-=T[n-j+1]*(q[j]*(n-j+1))
        T.append(rhs/(q[0]*(n+1)))
    tail=bound*ratio**161/(1-ratio);value=inflate(poly_eval(T,acb(delta)),tail,w)
    check(tag+' transition finite',all(v.is_finite() for v in value.entries()))
    return value,{'centre':str(z0),'delta':str(delta),'Rloc':str(rloc),'Dlower':str(dlow),'M':str(M),'ratio':str(ratio),'N':160,'tail':str(tail)}
# A local step entirely inside the original disc is checked against the
# separately summed degree3000 solution, verifying multiplication order.
z=qa(F(4,5));delta=qa(F(1,20));T,record=transition(z,delta,'overlap')
Ystart=inflate(poly_eval(U,acb(z)),K*(z/R)**3001/(1-z/R),w)
Yend=inflate(poly_eval(U,acb(z+delta)),K*((z+delta)/R)**3001/(1-(z+delta)/R),w)
check('local transition overlaps independently summed global series',matrix_overlaps(Ystart*T,Yend))
z=qa(F(19,20));Y=inflate(poly_eval(U,acb(z)),K*(z/R)**3001/(1-z/R),w);collar=[];product=ident()
for n in range(5):
    T,record=transition(z,delta,'collar'+str(n));Y=Y*T;product=product*T;collar.append(record);z+=delta
for n in range(4,-1,-1):
    T,record=transition(z,-delta,'reverse'+str(n));product=product*T;z-=delta
check('five actual right transitions and reverse contain identity',matrix_contains(product,ident()))
outputs['collar']={'steps':collar,'final_point':'6/5','final_solution':mat_strings(Y),'roundtrip_contains_identity':True}
print('collar160-term transitions and actual right-product comparison complete',flush=True)

# Exact independent test of real coordinate projections, implicit first
# and second derivatives, using an explicitly solved holomorphic ODE.
x,y=sp.symbols('x y',real=True);zz=x+sp.I*y;Nm=sp.zeros(6);Nm[4,1]=1;Nm[1,2]=1;Nm[2,3]=1
H=sp.Matrix([[1,1+2*sp.I,3+4*sp.I,5+6*sp.I,0,0],[0,sp.I,0,2,0,0],[0,1,0,3,1,0],[0,0,sp.I,5,0,0],[0,0,1,7,0,1],[0,0,0,1,0,0]])
check('exact derivative test fundamental initial matrix',H.det()!=0)
YY=H*(sp.eye(6)+zz*Nm+zz**2*Nm**2+sp.Rational(2,3)*zz**3*Nm**3);GG=Nm+zz*Nm**2;Q=GG**2+Nm**2
check('actual holomorphic first derivative identity',sp.simplify(YY.diff(x)-YY*GG)==sp.zeros(6))
check('actual holomorphic yy sign',sp.simplify(YY.diff(y,2)+YY*Q)==sp.zeros(6))
check('actual holomorphic mixed i factor',sp.simplify(YY.diff(x,y)-sp.I*YY*Q)==sp.zeros(6))
def realrow(row):return [sp.im(row[1]).expand(),sp.re(row[1]).expand(),sp.im(row[2]).expand(),sp.re(row[2]).expand()]
MM=sp.Matrix([realrow(list(YY.row(i))) for i in range(1,5)]);bb=sp.Matrix([sp.re(YY[i,3]).expand() for i in range(1,5)]);cv=sp.Matrix([realrow(list(YY.row(0)))]);dd=sp.re(YY[0,3]).expand();vv=MM.inv()*bb;hh=(cv*vv)[0]-dd
check('actual real selected minor determinant',sp.simplify(MM.det())!=0)
va={}
for a in (x,y):
    va[a]=MM.inv()*(bb.diff(a)-MM.diff(a)*vv)
    check('implicit first derivative '+str(a),sp.simplify(va[a]-vv.diff(a))==sp.zeros(4,1))
    check('height first derivative '+str(a),sp.simplify((cv.diff(a)*vv+cv*va[a])[0]-dd.diff(a)-hh.diff(a))==0)
for a,b in [(x,x),(x,y),(y,y)]:
    vab=MM.inv()*(bb.diff(a,b)-MM.diff(a,b)*vv-MM.diff(a)*va[b]-MM.diff(b)*va[a])
    check('implicit Hessian '+str((a,b)),sp.simplify(vab-vv.diff(a,b))==sp.zeros(4,1))
    hab=(cv.diff(a,b)*vv+cv.diff(a)*va[b]+cv.diff(b)*va[a]+cv*vab)[0]-dd.diff(a,b)
    check('height Hessian '+str((a,b)),sp.simplify(hab-hh.diff(a,b))==0)
outputs['implicit_exact_test']={'M_determinant':str(sp.simplify(MM.det())),'h_over_k':str(sp.simplify(hh)),'Hessian_over_k':[str(sp.simplify(hh.diff(a,b))) for a,b in [(x,x),(x,y),(y,y)]],'note':'This exact analytic test validates the signs and coordinate maps; the actual full-square determinant and leaf margins remain owner numerical data.'}
check('implicit test has nonconstant selected determinant',sp.simplify(MM.det()).has(x) or sp.simplify(MM.det()).has(y))
check('implicit test has nonzero Hessian',any(sp.simplify(hh.diff(a,b))!=0 for a,b in [(x,x),(x,y),(y,y)]))
result={'status':'PASS','checks':len(checks),'check_names':checks,'working_precision_bits':ctx.prec,'root_degrees':[3000,3000],'cusp_degree':600,'collar_degree':160,'outputs':outputs,'elapsed_seconds':time.time()-START,'packet_sha256':sha256(packet.read_bytes()).hexdigest(),'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'target_opened':False,'old_producer_imported':False,'scope':'All A-E and midpoint analytic algorithms; fresh exact/ball computations on supplied root/cusp data and actual representative collar/rectangle domains. Complete old global leaf subdivision is not supplied and is not claimed here.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','checks','working_precision_bits','root_degrees','cusp_degree','collar_degree','elapsed_seconds','source_sha256']},indent=2))
