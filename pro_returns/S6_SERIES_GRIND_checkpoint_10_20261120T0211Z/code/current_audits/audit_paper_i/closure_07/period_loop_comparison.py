"""Current P1.16 comparison: rational Fuchsian loops versus regular-root series.

Author: GPT-6 Astra, ChatGPT Pro mode, inherited effort, same family.
The loop implementation below is new. It imports no historical implementation.
The second method uses the saved exact inputs and certified normalization of
the current independent P1.18 root calculation. All path vertices and bounds
are retained. Exact intertwiner existence is P1.15, not a residual inference.
"""
from pathlib import Path
from fractions import Fraction as F
import sys, os, json, math, hashlib, time

HERE = Path(__file__).resolve().parent
AUDIT = HERE.parent
sys.path.insert(0, os.environ.get("S6_P116_VENDOR", str(AUDIT / "vendor")))
import flint
from flint import acb, arb, acb_mat, ctx
import sympy as sp
import numpy as np
from scipy.linalg import qr
import scipy

ctx.dps = 140
started = time.monotonic()
receipts = []
def rb(x):
    x=F(x); return arb(x.numerator)/x.denominator
def cb(x):
    x=sp.Rational(x); return acb(int(x.p))/int(x.q)
def mat(x): return acb_mat([[cb(x[i,j]) for j in range(x.cols)] for i in range(x.rows)])
def eye(n=6): return acb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def zer(n=6,m=6): return acb_mat(n,m)
def maxupper(xs):
    r=arb(0)
    for x in xs:
        if x.upper()>r:r=x.upper()
    return r
def norm(x):return maxupper([sum((x[i,j].abs_upper() for j in range(x.ncols())),arb(0)) for i in range(x.nrows())])
def radius(x):return maxupper([x[i,j].real.rad()+x[i,j].imag.rad() for i in range(x.nrows()) for j in range(x.ncols())])
def js(x):return [[str(x[i,j]) for j in range(x.ncols())] for i in range(x.nrows())]
def parse_ball(s):
    if not s.endswith("j"): return acb(arb(s))
    t=s[:-1]
    if " + " in t:
        re,im=t.rsplit(" + ",1);return acb(arb(re),arb(im))
    if " - " in t:
        re,im=t.rsplit(" - ",1);return acb(arb(re),-arb(im))
    return acb(0,arb(t))
def fromjs(x):return acb_mat([[parse_ball(z) for z in row] for row in x])
def point(z):return acb(rb(z[0]),rb(z[1]))
def lower(z):return max(abs(z[0]),abs(z[1]))

l=sp.symbols("l"); a=sp.Rational(256,3125); ar=F(256,3125)
W=sp.Matrix([
[-8*(625*l+48)/l,-8,10*l,sp.Rational(75,2)*l*l,0],
[-sp.Rational(125,2)/l,-4*(625*l+48)/l,8,0,sp.Rational(75,2)*l*l],
[300/l**2,-375/l,0,-48,60*l],
[120/l**3,0,sp.Rational(125,2)/l,4*(625*l+48)/l,-8],
[0,120/l**3,50/l**2,-sp.Rational(125,2)/l,8*(625*l+48)/l]])/(3125*l+256)
G=sp.zeros(6);G[1:6,1:6]=W
G[0,1:6]=sp.Matrix([[-sp.Rational(25,6)/l**2,-sp.Rational(125,48)/l,0,1,0]])/(l+a)
powers=[0,2,1,0,-1,-2]
D=sp.diag(*[l**q for q in powers])
GF=(D.inv()*G*D+D.inv()*D.diff(l)).applyfunc(sp.cancel)
R0=GF.applyfunc(lambda z:sp.limit(l*z,l,0))
Rs=GF.applyfunc(lambda z:sp.limit((l+a)*z,l,-a))
assert (GF-R0/l-Rs/(l+a)).applyfunc(sp.cancel)==sp.zeros(6)
A0,As=mat(R0),mat(Rs); M1=A0+As; M0=A0*cb(a)
n0,ns=norm(A0),norm(As)
print("Derived two Fuchsian residues",str(n0),str(ns),flush=True)

def step(z,h,R,tag):
    zc,hc=point(z),point(h)
    r=abs(h[0])+abs(h[1]);q=rb(r/R)
    d0=lower(z); ds=lower((z[0]+ar,z[1]))
    assert R<d0 and R<ds and r<R
    bound=n0/rb(d0-R)+ns/rb(ds-R)
    K=(bound*rb(R)).exp(); N=32
    while not K*q**(N+1)/(1-q)<arb("1e-100"):N+=16
    tail=K*q**(N+1)/(1-q)
    Q0=zc*(zc+cb(a));Q1=2*zc+cb(a);P0=M1*zc+M0
    coef=[eye()]
    for n in range(N):
        v=coef[n]*P0-coef[n]*(n*Q1)
        if n:v+=coef[n-1]*M1-coef[n-1]*(n-1)
        coef.append(v/(Q0*(n+1)))
    T=coef[-1]
    for v in reversed(coef[:-1]):T=T*hc+v
    error=acb(arb(0,tail.upper()),arb(0,tail.upper()))
    T=acb_mat([[T[i,j]+error for j in range(6)] for i in range(6)])
    receipts.append({'tag':tag,'z':[str(x)for x in z],'h':[str(x)for x in h],
      'R':str(R),'N':N,'norm_bound':str(bound),'tail':str(tail),'radius':str(radius(T))})
    return T

def segment(z,end,tag):
    U=eye();i=0
    while z!=end:
        dist=min(lower(z),lower((z[0]+ar,z[1])));R=dist/2
        delta=(end[0]-z[0],end[1]-z[1]);length=abs(delta[0])+abs(delta[1])
        fac=min(F(1),R/(4*length));h=(fac*delta[0],fac*delta[1])
        U=U*step(z,h,R,f'{tag}/{i}');z=(z[0]+h[0],z[1]+h[1]);i+=1
    return U

def path(vertices,tag):
    U=eye()
    for j,(z,end) in enumerate(zip(vertices,vertices[1:])):U=U*segment(z,end,f'{tag}/{j}')
    print(tag,len(receipts),'steps so far; radius',radius(U),flush=True)
    return U

r=F(1,32); one=(F(1),F(0))
v0=[one,(r,F(0)),(r,r),(-r,r),(-r,-r),(r,-r),(r,F(0)),one]
vi=[one,(F(1),F(-1)),(F(-1),F(-1)),(F(-1),F(1)),(F(1),F(1)),one]
H0=path(v0,'positive-zero-meridian')
HI=path(vi,'positive-infinity-meridian')
A=acb_mat([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=acb_mat([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
rows=[];rhs=[]
for H,T in [(H0,B),(HI,A)]:
    for i in range(6):
        for j in range(1,6):
            row=[acb(0)for _ in range(30)]
            for k in range(1,6):row[i*5+k-1]+=H[k,j]
            for k in range(6):row[k*5+j-1]-=T[i,k]
            rows.append(row);rhs.append(-H[0,j]if i==0 else acb(0))
approx=np.array([[complex(float(z.real.mid()),float(z.imag.mid()))for z in row]for row in rows])
_,_,piv=qr(approx.T,pivoting=True,mode='economic');selected=[int(x)for x in piv[:30]]
Xv=acb_mat([rows[k]for k in selected]).solve(acb_mat([[rhs[k]]for k in selected]))
X=acb_mat([[int(i==0)]+[Xv[i*5+j,0]for j in range(5)]for i in range(6)])
res=[X*H0-B*X,X*HI-A*X]
assert all(m[i,j].contains(0)for m in res for i in range(6)for j in range(6))

rootdir=Path(os.environ.get('S6_P116_ROOT_INPUTS', str(AUDIT/'paper_v_review/output')))
root=json.loads((rootdir/'fresh_frobenius.json').read_text())
Xroot=fromjs(root['X']);FI=fromjs(root['infinity_constant_frame'])
T12=path([one,(F(2),F(0))],'positive-one-to-two')
D2inv=acb_mat([[acb(2)**(-powers[i]) if i==j else 0 for j in range(6)]for i in range(6)])
Y2=X*T12*D2inv

# Second method at lambda=2: one regular infinity-root series, no loop.
root_inputs=json.loads((rootdir/'fresh_root_connections.json').read_text())['infinity']
Pc=[acb_mat([[cb(sp.Rational(z))for z in row]for row in m])for m in root_inputs['numerator_coefficients']]
Qc=[cb(sp.Rational(z))for z in root_inputs['denominator_coefficients']]
u=acb(arb(2).root(5))**-1;R=arb(5)/4
dl=Qc[0].abs_lower()-sum((Qc[j].abs_upper()*R**j for j in range(1,len(Qc))),arb(0))
assert dl>0
M=sum((norm(Pc[j])*R**j for j in range(len(Pc))),arb(0))/dl
K=(M*R).exp();q=u.abs_upper()/R;N=32
while not K*q**(N+1)/(1-q)<arb('1e-100'):N+=16
tail=K*q**(N+1)/(1-q);cs=[eye()]
for n in range(N):
    v=sum((cs[n-j]*Pc[j]for j in range(min(n,len(Pc)-1)+1)),zer())
    v-=sum((cs[n-j+1]*(Qc[j]*(n-j+1))for j in range(1,min(n,len(Qc)-1)+1)),zer())
    cs.append(v/(Qc[0]*(n+1)))
Ui=cs[-1]
for m in reversed(cs[:-1]):Ui=Ui*u+m
err=acb(arb(0,tail.upper()),arb(0,tail.upper()))
Ui=acb_mat([[Ui[i,j]+err for j in range(6)]for i in range(6)])
expinf=[0,-8,-4,0,4,8]
DIinv=acb_mat([[u**(-expinf[i])if i==j else 0 for j in range(6)]for i in range(6)])
Y2root=FI*Ui*DIinv
diff1=maxupper([(X-Xroot)[i,j].abs_upper()for i in range(6)for j in range(6)])
diff2=maxupper([(Y2-Y2root)[i,j].abs_upper()for i in range(6)for j in range(6)])
assert diff1<arb('1e-30') and diff2<arb('1e-30'),(diff1,diff2)

def height(Y):
    rows=[[Y[i,1].imag,Y[i,1].real,Y[i,2].imag,Y[i,2].real]for i in range(1,6)]
    rhs=[Y[i,3].real for i in range(1,6)]
    _,_,piv=qr(np.array([[float(x.mid())for x in row]for row in rows]).T,pivoting=True,mode='economic')
    sel=[int(x)for x in piv[:4]]
    v=acb_mat([[acb(x)for x in rows[i]]for i in sel]).solve(acb_mat([[acb(rhs[i])]for i in sel]))
    assert all((sum((rows[i][j]*v[j,0].real for j in range(4)),arb(0))-rhs[i]).contains(0)for i in range(5))
    coeff=[Y[0,1].imag,Y[0,1].real,Y[0,2].imag,Y[0,2].real]
    return 96/(625*arb.pi())*(sum((coeff[j]*v[j,0].real for j in range(4)),arb(0))-Y[0,3].real)

def determinant(Y):
    Z=acb_mat([[Y[i,j+1]-(625*arb.pi()/96)*10*int(i==0 and j==2)for j in range(3)]for i in range(6)])
    return acb_mat([[Z[i,j]if j<3 else Z[i,j-3].conjugate()for j in range(6)]for i in range(6)]).det()
h1=height(X)
assert h1>arb('-1.0342766224163217994942488453783461')
assert h1<arb('-1.0342766224163217994942488453783460')
dets=[determinant(X),determinant(Y2)]
assert all(x.real.contains(0)and x.imag>0 for x in dets),dets
payload={'author':'GPT-6 Astra, ChatGPT Pro mode, inherited effort; same family','phase':'S6_SERIES_GRIND',
 'method':'New exact two-residue Fuchsian gauge, rational closed polygon meridians, Taylor-ball Cauchy/Gronwall bounds; compared with independent current regular-root method.',
 'python_flint':flint.__version__,'working_decimal_digits':ctx.dps,
 'dependency_versions':{'sympy':sp.__version__,'numpy':np.__version__,'scipy':scipy.__version__},
 'gauge_exponents':powers,'residue_zero':[[str(z)for z in row]for row in R0.tolist()],
 'residue_star':[[str(z)for z in row]for row in Rs.tolist()],
 'vertices_zero':[[str(x)for x in z]for z in v0],'vertices_infinity':[[str(x)for x in z]for z in vi],
 'intertwiner_equations':selected,'all_intertwiner_residuals_contain_zero':True,
 'X_loop':js(X),'Y2_loop':js(Y2),'Y2_root':js(Y2root),
 'matrix_difference_one_upper':str(diff1),'matrix_difference_two_upper':str(diff2),
 'h_b_one':str(h1),'c10_determinants':[str(x)for x in dets],
 'loop_and_open_path_steps':len(receipts),'maximum_loop_Taylor_order':max(x['N']for x in receipts),
 'step_receipts':receipts,'root_at_two':{'N':N,'R':'5/4','norm_bound':str(M),'denominator_lower':str(dl),'tail':str(tail)},
 'input_files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in [rootdir/'fresh_frobenius.json',rootdir/'fresh_root_connections.json']},
 'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'elapsed_seconds':time.monotonic()-started,'result':'PASS'}
out=HERE/'period_loop_comparison.output.json';out.write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps({'result':'PASS','steps':len(receipts),'max_order':payload['maximum_loop_Taylor_order'],'diff_one':str(diff1),'diff_two':str(diff2),'h1':str(h1),'determinants':[str(x)for x in dets],'output':str(out)}),flush=True)
