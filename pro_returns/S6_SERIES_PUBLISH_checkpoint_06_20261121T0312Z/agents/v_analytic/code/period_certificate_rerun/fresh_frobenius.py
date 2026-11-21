#!/usr/bin/env python3
"""Fresh finite-root Arb certificate for the printed P1.15--P1.18 data.

Author: GPT-6 Astra, ChatGPT Pro mode, inherited effort, 2026-11-19.
No historical implementation or historical coefficient array is used.
Derive both root connections from the printed rational 6x6 connection.
Transport along the positive real root axis; recover the two finite
monodromies from their exact root characters, then solve the actual
normalized integral intertwiner. Approximate QR selects equations only;
the final inverse, solve, residuals and output are complex-ball operations.

The tail bound is proved in DERIVATION.md. This program certifies only
the domains listed in its output, not the inherited 12911-leaf cover.
"""
from __future__ import annotations
import sys, json, time, math, argparse, os
from pathlib import Path
from fractions import Fraction
HERE=Path(__file__).resolve().parent
for candidate in [os.environ.get('PAPER_V_VENDOR'),str(HERE/'vendor'),str(HERE.parent/'vendor'),str(HERE.parents[1]/'vendor')]:
    if candidate and Path(candidate).exists():sys.path.insert(0,candidate)
import flint
from flint import arb, acb, acb_mat, ctx
import sympy as sp
import numpy as np
from scipy.linalg import qr

parser=argparse.ArgumentParser()
parser.add_argument('--dps',type=int,default=120)
parser.add_argument('--output',default='fresh_frobenius.json')
args=parser.parse_args()
ctx.dps=args.dps
OUT=Path(os.environ.get('PAPER_V_OUTPUT_DIR',str((HERE.parent if HERE.name=='code' else HERE)/'output')));OUT.mkdir(parents=True,exist_ok=True)
started=time.monotonic()
receipts=[]

def log(s): print(s,flush=True)
def ball(q):
    q=sp.Rational(q)
    return acb(int(q.p))/int(q.q)
def rb(q):
    q=Fraction(q)
    return arb(q.numerator)/q.denominator
def ident(n=6): return acb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def zero(r=6,c=6): return acb_mat(r,c)
def toball(M):return acb_mat([[ball(M[i,j]) for j in range(M.cols)] for i in range(M.rows)])
def exact_upper_max(xs):
    result=arb(0)
    for x in xs:
        t=x.upper()
        if t>result:result=t
    return result
WEIGHTS=[rb(x) for x in [1,Fraction(1,128),Fraction(1,128),Fraction(1,32),Fraction(1,64),Fraction(1,32)]]
def norm(M):
    return exact_upper_max([sum((M[i,j].abs_upper()*WEIGHTS[j]/WEIGHTS[i] for j in range(6)),arb(0)) for i in range(6)])
def add_tail(M,t):
    return acb_mat([[M[i,j]+acb(arb(0,(t*WEIGHTS[i]/WEIGHTS[j]).upper()),arb(0,(t*WEIGHTS[i]/WEIGHTS[j]).upper())) for j in range(6)]for i in range(6)])
def maxrad(M):return exact_upper_max([M[i,j].real.rad()+M[i,j].imag.rad() for i in range(M.nrows()) for j in range(M.ncols())])
def matjson(M):return [[str(M[i,j])for j in range(M.ncols())]for i in range(M.nrows())]

lam,u=sp.symbols('lam u')
a=sp.Rational(256,3125)
GW=sp.Matrix([
[-8*(625*lam+48)/lam,-8,10*lam,sp.Rational(75,2)*lam**2,0],
[-sp.Rational(125,2)/lam,-4*(625*lam+48)/lam,8,0,sp.Rational(75,2)*lam**2],
[300/lam**2,-375/lam,0,-48,60*lam],
[120/lam**3,0,sp.Rational(125,2)/lam,4*(625*lam+48)/lam,-8],
[0,120/lam**3,50/lam**2,-sp.Rational(125,2)/lam,8*(625*lam+48)/lam]])/(3125*lam+256)
G=sp.zeros(6)
G[0,1:6]=sp.Matrix([[-sp.Rational(25,6)/lam**2,-sp.Rational(125,48)/lam,0,1,0]])/(lam+a)
G[1:6,1:6]=GW

def root_data(name,sub,powers,Q):
    D=sp.diag(*[u**d for d in powers])
    Gr=(D.inv()*(sp.diff(sub,u)*G.subs(lam,sub))*D+D.inv()*D.diff(u)).applyfunc(sp.cancel)
    P=(Gr*Q).applyfunc(sp.cancel)
    assert all(sp.denom(x)==1 or sp.denom(x).is_Integer for x in P)
    degree=max(sp.degree(x,u)for x in P if x)
    coeff=[P.applyfunc(lambda x:sp.expand(x).coeff(u,j)) for j in range(degree+1)]
    assert P==sum((x*u**j for j,x in enumerate(coeff)),sp.zeros(6))
    q=[sp.expand(Q).coeff(u,j)for j in range(sp.degree(Q,u)+1)]
    data={'name':name,'lambda':str(sub),'gauge_exponents':powers,
          'denominator_coefficients':[str(x)for x in q],
          'numerator_coefficients':[[[str(x[i,j])for j in range(6)]for i in range(6)]for x in coeff]}
    return [toball(x)for x in coeff],[ball(x)for x in q],data

log('Deriving exact root connections from printed rational Gamma6')
P0,Q0,data0=root_data('zero',u**4,[0,6,3,0,-3,-6],3125*u**4+256)
PI,QI,dataI=root_data('infinity',u**-5,[0,-8,-4,0,4,8],3125+256*u**5)
(OUT/'fresh_root_connections.json').write_text(json.dumps({'zero':data0,'infinity':dataI},indent=2)+'\n')

def shift_poly(P,Q,c):
    c=acb(rb(c))
    pp=[sum((P[k]*(math.comb(k,j)*c**(k-j))for k in range(j,len(P))),zero())for j in range(len(P))]
    qq=[sum((Q[k]*(math.comb(k,j)*c**(k-j))for k in range(j,len(Q))),acb(0))for j in range(len(Q))]
    return pp,qq

def bounded_transition(P,Q,h,R,tag,goal=70):
    """T'=T P(t)/Q(t), T(0)=I; integrate at rational h in |t|<R."""
    hA=acb(rb(h)); r=rb(abs(h)); RA=rb(R)
    dl=Q[0].abs_lower()-sum((Q[j].abs_upper()*RA**j for j in range(1,len(Q))),arb(0))
    assert dl>0,(tag,str(dl))
    upper=sum((norm(P[j])*RA**j for j in range(len(P))),arb(0))/dl
    K=(upper*RA).exp()
    ratio=r/RA
    assert ratio<1
    N=32
    while not K*ratio**(N+1)/(1-ratio)<arb(10)**(-goal):N+=16
    tail=K*ratio**(N+1)/(1-ratio)
    coeff=[ident()]
    for n in range(N):
        rhs=sum((coeff[n-j]*P[j]for j in range(min(len(P)-1,n)+1)),zero())
        rhs-=sum((coeff[n-j+1]*(Q[j]*(n-j+1))for j in range(1,min(len(Q)-1,n)+1)),zero())
        coeff.append(rhs/(Q[0]*(n+1)))
    value=coeff[-1]
    for C in reversed(coeff[:-1]):value=value*hA+C
    value=add_tail(value,tail)
    receipts.append({'tag':tag,'h':str(h),'R':str(R),'N':N,'denominator_lower':str(dl),'norm_bound':str(upper),'tail':str(tail),'result_max_radius':str(maxrad(value))})
    log(f'{tag}: N={N}, tail={tail}, radius={maxrad(value)}')
    return value

# Distinct path from the inherited closed-loop implementation: regular root
# series at zero, then positive real root axis; infinity is a single root series.
U0=bounded_transition(P0,Q0,Fraction(1,4),Fraction(2,5),'zero-root',goal=85)
c=Fraction(1,4)
while c<1:
    delta=min(c/Fraction(32),1-c)
    pp,qq=shift_poly(P0,Q0,c)
    trans=bounded_transition(pp,qq,delta,c/Fraction(8),f'zero-axis-{len(receipts)}',goal=85)
    U0=U0*trans
    c+=delta
UI=bounded_transition(PI,QI,Fraction(1),Fraction(5,4),'infinity-root',goal=85)

z4=acb(0,1)
z5=(acb(0,2)*arb.pi()/5).exp()
T0=acb_mat([[z4**(-[0,6,3,0,-3,-6][i])if i==j else 0 for j in range(6)]for i in range(6)])
TI=acb_mat([[z5**(-[0,-8,-4,0,4,8][i])if i==j else 0 for j in range(6)]for i in range(6)])
H0=U0.inv()*T0*U0
HI=UI.inv()*TI*UI
A=acb_mat([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=acb_mat([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])

log('Selecting and certifying normalized intertwiner equations')
def solve_intertwiner(H0,HI,A,B):
    rows=[];rhs=[]
    for H,T in [(H0,B),(HI,A)]:
        for i in range(6):
            for j in range(1,6):
                row=[acb(0)for _ in range(30)]
                for k in range(1,6):row[i*5+k-1]+=H[k,j]
                for k in range(6):row[k*5+j-1]-=T[i,k]
                rows.append(row);rhs.append(-H[0,j]if i==0 else acb(0))
    approx=np.array([[complex(float(z.real.mid()),float(z.imag.mid()))for z in row]for row in rows])
    _,_,piv=qr(approx.T,pivoting=True,mode='economic')
    selected=[int(i)for i in piv[:30]]
    mat=acb_mat([rows[i]for i in selected]);vec=acb_mat([[rhs[i]]for i in selected])
    sol=mat.solve(vec)
    X=acb_mat([[int(i==0)]+[sol[i*5+j,0]for j in range(5)]for i in range(6)])
    res0=X*H0-B*X;resI=X*HI-A*X
    consistent=all(res0[i,j].contains(0)and resI[i,j].contains(0)for i in range(6)for j in range(6))
    log(f'Intertwiner residual balls contain zero: {consistent}; radius {maxrad(X)}')
    assert consistent,'Exact monodromy constraints not certified: check peripheral directions/paths.'
    return X,selected,res0,resI
X,selected,res0,resI=solve_intertwiner(H0,HI,A,B)
c0=96/(625*arb.pi())
F0=X*U0.inv();FI=X*UI.inv()
hinf=-c0*FI[0,3].real
hzero=-c0*F0[0,3].real

def height(Y):
    rows=[];rhs=[]
    for i in range(1,6):
        rows.append([Y[i,1].imag,Y[i,1].real,Y[i,2].imag,Y[i,2].real]);rhs.append(Y[i,3].real)
    approx=np.array([[float(z.mid())for z in row]for row in rows])
    _,_,piv=qr(approx.T,pivoting=True,mode='economic');sel=[int(i)for i in piv[:4]]
    mat=acb_mat([[acb(z)for z in rows[i]]for i in sel]);vec=acb_mat([[acb(rhs[i])]for i in sel]);v=mat.solve(vec)
    h=c0*(sum(([Y[0,1].imag,Y[0,1].real,Y[0,2].imag,Y[0,2].real][j]*v[j,0].real for j in range(4)),arb(0))-Y[0,3].real)
    residual=[sum((rows[i][j]*v[j,0].real for j in range(4)),arb(0))-rhs[i]for i in range(5)]
    assert all(x.contains(0)for x in residual)
    return h,sel
h1,realrows=height(X)
log(f'h_b(infinity)={hinf}\nh_b(0)={hzero}\nh_b(1)={h1}')
reported={'infinity':'-1.094540250311402780116268263054945703725533',
          'zero':'-0.931793376356523505430795105796011114990828',
          'one':'-1.03427662241632179949424884537834605259496477790218821132'}
results={'infinity':hinf,'zero':hzero,'one':h1}
matches={k:results[k].overlaps(arb(v,arb(10)**(-len(v.split('.')[1]))))for k,v in reported.items()}
payload={'checker':'GPT-6 Astra, ChatGPT Pro mode, inherited effort; same model family',
 'library':{'python_flint':flint.__version__,'precision_digits':ctx.dps},
 'method':'new exact root-connection derivation, rigorous Arb Taylor tails, finite deck characters, certified normalized intertwiner solve',
 'scope':'three point enclosures; no global minimum or global leaf-partition certificate claimed',
 'h_b':{k:str(v)for k,v in results.items()},'matches_printed_prefix_enclosures':matches,
 'intertwiner_selected_equations':selected,'height_selected_rows':realrows,
 'X':matjson(X),'zero_root_to_base':matjson(U0),'infinity_root_to_base':matjson(UI),
 'zero_constant_frame':matjson(F0),'infinity_constant_frame':matjson(FI),
 'normalized_intertwiner_residuals_contain_zero':True,'transition_receipts':receipts,
 'elapsed_seconds':time.monotonic()-started}
(OUT/args.output).write_text(json.dumps(payload,indent=2)+'\n')
assert all(matches.values()),matches
log(f'PASS; output {OUT/args.output}')
