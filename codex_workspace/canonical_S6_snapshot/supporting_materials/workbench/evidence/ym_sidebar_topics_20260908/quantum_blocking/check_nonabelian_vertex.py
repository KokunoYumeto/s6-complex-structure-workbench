"""Exact polynomial checks for the original nonabelian vertex derivation."""
from pathlib import Path
from itertools import permutations
import json,subprocess,sys
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,ok):
    checks.append(dict(name=name,passed=bool(ok)))
    if not ok:raise AssertionError(name)

# Full twelve-variable ordered four-link word, through degree four.
z=[s.Matrix(s.symbols(f'z{i}_0:3')) for i in range(4)]
zero=s.zeros(3,1)
def mul(a,b):
    aa,av=a;bb,bv=b
    return s.expand(aa*bb-av.dot(bv)/4),(aa*bv+bb*av+av.cross(bv)/2).applyfunc(s.expand)
word=[(s.Integer(1),zero)]+[(s.Integer(0),zero) for _ in range(4)]
for v in z:
    r=v.dot(v)
    coeff=[(1,zero),(0,v),(-r/8,zero),(0,-r*v/24),(r*r/384,zero)]
    out=[]
    for k in range(5):
        parts=[mul(word[j],coeff[k-j]) for j in range(k+1)]
        out.append((s.expand(sum(p[0] for p in parts)),sum((p[1] for p in parts),zero).applyfunc(s.expand)))
    word=out
A=zero;B=zero;C=zero
for v in z:
    A,B,C=A+v,B+A.cross(v)/2,C+B.cross(v)/2+(A.cross(A.cross(v))+v.cross(v.cross(A)))/12
check('Original constant2 cancels traceI only at zero',2-2*word[0][0]==0)
check('Full four-link linear trace coefficient vanishes',word[1][0]==0)
check('Full twelve-coordinate quadratic face polynomial',s.expand(-2*word[2][0]-A.dot(A)/4)==0)
check('Full twelve-coordinate cubic face polynomial and order signs',s.expand(-2*word[3][0]-A.dot(B)/2)==0)
check('Full twelve-coordinate fourth face polynomial with nested terms',s.expand(-2*word[4][0]-B.dot(B)/4-A.dot(C)/2+A.dot(A)**2/192)==0)
subs={z[0][i]:int(i==0) for i in range(3)}
subs.update({z[1][i]:int(i==1) for i in range(3)})
subs.update({z[2][i]:-int(i==2) for i in range(3)})
subs.update({z[3][i]:0 for i in range(3)})
check('Original specified face magnetic H1 coefficient',s.expand(-word[3][0]).subs(subs)==-s.Rational(1,8))

# Bernoulli and exact Haar-density coefficients.
t=s.symbols('t')
check('Left logarithmic field through fourth order',s.series(t/(s.exp(t)-1),t,0,5).removeO()==1-t/2+t*t/12-t**4/720)
check('Right logarithmic field through fourth order',s.series(t*s.exp(t)/(s.exp(t)-1),t,0,5).removeO()==1+t/2+t*t/12-t**4/720)
check('Retained logarithmic Haar density through fourth order',s.series(2*s.log(s.sin(t/2)/(t/2)),t,0,6).removeO()==-t*t/12-t**4/1440)
x=s.Matrix(s.symbols('x0:3'));basis=[s.eye(3)[:,i] for i in range(3)]
for alpha in range(3):
    cross=x.cross(basis[alpha]);double=x.cross(cross)
    check(f'First field has zero flat divergence, colour{alpha}',sum(s.diff(cross[i],x[i]) for i in range(3))==0)
    check(f'Second field divergence fixes density multiplication, colour{alpha}',s.expand(sum(s.diff(double[i],x[i]) for i in range(3))-2*x[alpha])==0)
    check(f'Radial density contraction retains only additive field, colour{alpha}',s.expand(x.dot(cross))==0 and s.expand(x.dot(double))==0)

# General three-chord Gaussian derivatives with symmetric six-parameter K.
xx=[s.Matrix(s.symbols(f'x{c}_0:3')) for c in range(3)]
ks=s.symbols('k00 k01 k02 k11 k12 k22')
K=s.Matrix([[ks[0],ks[1],ks[2]],[ks[1],ks[3],ks[4]],[ks[2],ks[4],ks[5]]])
pp=[sum((K[c,d]*xx[d] for d in range(3)),zero) for c in range(3)]
tt=s.symbols('t0:3');bb=s.symbols('b0:3')
vv=sum((tt[c]*pp[c] for c in range(3)),zero)
theta=sum((bb[c]*xx[c].cross(pp[c]) for c in range(3)),zero)
def D0(poly,alpha):return s.expand(sum(tt[c]*s.diff(poly,xx[c][alpha]) for c in range(3)))
def D1(poly,alpha):
    return s.expand(sum(bb[c]*xx[c].cross(basis[alpha])[beta]*s.diff(poly,xx[c][beta])/2 for c in range(3) for beta in range(3)))
check('Complete cubic contraction derivative D0theta vanishes',s.expand(sum(D0(theta[alpha],alpha) for alpha in range(3)))==0)
check('Complete cubic contraction derivative D1v vanishes',s.expand(sum(D1(vv[alpha],alpha) for alpha in range(3)))==0)
kin=s.expand(-2*sum(D0(theta[alpha]/8,alpha)-theta[alpha]*vv[alpha]/32-D1(vv[alpha]/4,alpha)-vv[alpha]*theta[alpha]/32 for alpha in range(3)))
check('Both kinetic derivative orders give +v dot theta/8',s.expand(kin-vv.dot(theta)/8)==0)

# Six colour assignments and the full cross-covariance determinant.
perms=list(permutations(range(3)))
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
q=s.Matrix(3,3,s.symbols('q0:9'))
wick=0
for aa in perms:
    for b in perms:
        wick+=sign(aa)*sign(b)*s.prod(q[i,b.index(aa[i])] for i in range(3))
check('All36 colour determinant contractions equal6det covariance',s.expand(wick-6*q.det())==0)
check('Original vertex raw norm lower-bound arithmetic',2*s.Rational(242,1000)**2==s.Rational(14641,125000))
check('Inverse three-excitation raw norm lower-bound arithmetic',s.Rational(14641,125000)/108==s.Rational(14641,13500000))

# The field-coordinate derivative includes the exact density-bearing connection.
g=s.symbols('g',positive=True);dim=s.symbols('d');rr=s.symbols('r',positive=True)
J=s.Function('J');F=s.Function('F')
chart=g**(dim/2)*s.sqrt(J(g*rr))*F(g*rr)
check('Exact radial version of chart coupling connection',s.simplify(s.diff(chart,g)-(rr*s.diff(chart,rr)+dim*chart/2)/g)==0)

# Fourth field coefficient, including its density-bearing skew identity.
for alpha in range(3):
    ad4=x.cross(x.cross(x.cross(x.cross(basis[alpha]))))
    div4=sum(s.diff(-ad4[i]/720,x[i]) for i in range(3))
    check(f'Fourth field density is half its full divergence, colour{alpha}',s.expand(div4/2-x.dot(x)*x[alpha]/720)==0)
    check(f'Fourth density radial contraction vanishes, colour{alpha}',s.expand(x.dot(ad4))==0)

# Independent direct simplex integration, retaining repeated energies and zero.
tau,u,v=s.symbols('tau u v',positive=True)
def It(a,b):return tau*s.exp(-tau*a) if a==b else (s.exp(-tau*a)-s.exp(-tau*b))/(b-a)
def Jt(a,b,c):
    vals=[s.sympify(a),s.sympify(b),s.sympify(c)]
    if len(set(vals))==3:
        return sum(s.exp(-tau*z)/s.prod(w-z for w in vals if w!=z) for z in vals)
    if len(set(vals))==1:return tau*tau*s.exp(-tau*a)/2
    repeated=next(z for z in vals if vals.count(z)==2)
    other=next(z for z in vals if z!=repeated)
    delta=other-repeated
    return ((tau*delta-1)*s.exp(-tau*repeated)+s.exp(-tau*other))/(delta*delta)
for energies in [(0,2,3),(2,0,3),(3,2,0),(0,0,3),(3,0,0),(0,3,0),(2,2,2)]:
    a,b,c=energies
    direct=s.integrate(s.integrate(s.exp(-(tau-u)*a-(u-v)*b-v*c),(v,0,u)),(u,0,tau))
    check(f'Independent ordered simplex integral {energies}',s.simplify(direct-Jt(*energies))==0)
for a,b in [(0,2),(2,0),(2,2)]:
    direct=s.integrate(s.exp(-(tau-u)*a-u*b),(u,0,tau))
    check(f'Independent single insertion integral {(a,b)}',s.simplify(direct-It(a,b))==0)

# A separate finite matrix family tests the complete covariance coefficient
# against direct high-precision diagonalization, rather than a second copy of
# the formal expansion. It is a diagnostic of the formula, not a YM truncation.
import mpmath as mp
mp.mp.dps=65
HH0=s.diag(0,2,3,7)
HH1=s.Matrix([[0,1,0,2],[1,0,-3,0],[0,-3,0,4],[2,0,4,0]])
HH2=s.Matrix([[2,0,1,0],[0,3,0,-2],[1,0,5,0],[0,-2,0,6]])
DD0=s.Matrix([[1,0,2,0],[0,-1,0,3],[2,0,4,0],[0,3,0,2]])
DD1=s.Matrix([[0,2,0,-1],[2,0,1,0],[0,1,0,3],[-1,0,3,0]])
DD2=s.Matrix([[3,0,-2,0],[0,2,0,1],[-2,0,1,0],[0,1,0,4]])
vv0=s.eye(4)[:,0];inv0=s.diag(0,s.Rational(1,2),s.Rational(1,3),s.Rational(1,7))
pp1=-inv0*HH1*vv0
ee2=(vv0.T*(HH1*pp1+HH2*vv0))[0]
pp2=-inv0*(HH1*pp1+HH2*vv0)
cc2=pp2-(pp1.dot(pp1)/2)*vv0
def state_coefficients(Da,Db,Dc):
    ma=(vv0.T*Da*vv0)[0]
    mc=(vv0.T*Dc*vv0)[0]+2*(pp1.T*Db*vv0)[0]+2*(cc2.T*Da*vv0)[0]+(pp1.T*Da*pp1)[0]
    return (Da-ma*s.eye(4))*vv0,Db*vv0+(Da-ma*s.eye(4))*pp1,(Dc-mc*s.eye(4))*vv0+Db*pp1+(Da-ma*s.eye(4))*cc2,mc
zz0,zz1,zz2,mm2=state_coefficients(DD0,DD1,DD2)
constant=state_coefficients(HH0,HH1,HH2)
check('All three total-energy centered coefficients vanish exactly',all(z==s.zeros(4,1) for z in constant[:3]) and constant[3]==ee2)
PP=s.diag(1,-1,1,-1)
check('Independent covariance example has every required parity',all(PP*H*PP==sign*H for H,sign in [(HH0,1),(HH1,-1),(HH2,1),(DD0,1),(DD1,-1),(DD2,1)]) and PP*zz0==zz0 and PP*zz1==-zz1 and PP*zz2==zz2)
SS0=s.diag(*(s.exp(-tau*HH0[i,i]) for i in range(4)))
SS1=s.Matrix(4,4,lambda i,j:-HH1[i,j]*It(HH0[i,i],HH0[j,j]))
AA2=HH2-ee2*s.eye(4)
SS2=s.Matrix(4,4,lambda i,j:-AA2[i,j]*It(HH0[i,i],HH0[j,j])+sum(HH1[i,k]*HH1[k,j]*Jt(HH0[i,i],HH0[k,k],HH0[j,j]) for k in range(4)))
pred0=(zz0.T*SS0*zz0)[0]
pred2=2*(zz2.T*SS0*zz0)[0]+(zz1.T*SS0*zz1)[0]+2*(zz1.T*SS1*zz0)[0]+(zz0.T*SS2*zz0)[0]
check('Covariance quadratic diagnostic includes a nonzero coefficient',abs(float(pred2.subs(tau,s.Rational(7,10))))>1)
def mp_matrix(M):return mp.matrix([[mp.mpf(str(v)) for v in row] for row in M.tolist()])
h0,h1,h2,d0,d1,d2=map(mp_matrix,[HH0,HH1,HH2,DD0,DD1,DD2])
def actual_cov(gg,tt):
    hh=h0+gg*h1+gg*gg*h2
    eig,vec=mp.eigsy(hh)
    psi=vec[:,0]
    dd=d0+gg*d1+gg*gg*d2
    mm=(psi.T*dd*psi)[0]
    xx=(dd-mm*mp.eye(4))*psi
    spectral=vec.T*xx
    return sum(spectral[i]**2*mp.exp(-tt*(eig[i]-eig[0])) for i in range(4))
for time_string in ['0','0.7','2.3']:
    tt=mp.mpf(time_string);gg=mp.mpf('0.0000001')
    p0=mp.mpf(str(s.N(pred0.subs(tau,s.Rational(time_string)),60)))
    p2=mp.mpf(str(s.N(pred2.subs(tau,s.Rational(time_string)),60)))
    observed=(actual_cov(gg,tt)+actual_cov(-gg,tt)-2*p0)/(2*gg*gg)
    check(f'Full C2 versus independent 65-digit eigensolve, time={time_string}',abs(observed-p2)<mp.mpf('1e-9')*max(1,abs(p2)))

subprocess.run([sys.executable,str(ROOT/'certify_nonabelian_vertex.py')],check=True,stdout=subprocess.DEVNULL)
certificate=json.loads((ROOT/'NONABELIAN_VERTEX_CERTIFICATE.json').read_text(encoding='utf-8'))
check('Independent integer-only full176-mode vertex enclosure',certificate['proved'] and certificate['strict_conclusion']=='-243/1000 < a*cubic_coefficient < -242/1000')
out=dict(passed=all(c['passed'] for c in checks),groups=len(checks),checks=checks,
         scope='Exact symbolic polynomial checks plus the separate rigorous finite radical interval certificate. No interacting continuum assertion is numerically certified.')
(ROOT/'NONABELIAN_VERTEX_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=out['passed'],groups=len(checks))))
