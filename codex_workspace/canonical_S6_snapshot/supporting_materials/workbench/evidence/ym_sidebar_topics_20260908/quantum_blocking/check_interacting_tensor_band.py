"""Exact tensor/Gram checks and a separate complete finite-matrix band diagnostic."""
from pathlib import Path
import json
import sympy as s
import numpy as np
from scipy.linalg import expm
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,condition):
    checks.append(dict(name=name,passed=bool(condition)))
    if not condition:raise AssertionError(name)

# Every original tensor coordinate and raw colour multiplicity remains.
a,sigma,delta,mm=s.symbols('a sigma delta mm',nonzero=True,real=True)
ss=s.symbols('s11 s22 s33 s12 s13 s23',real=True)
S=s.Matrix([[ss[0],ss[3],ss[4]],[ss[3],ss[1],ss[5]],[ss[4],ss[5],ss[2]]])
R=s.Matrix(3,3,lambda i,j:sigma*(delta*(s.trace(S)-S[i,i]) if i==j else mm*S[i,j]))
q=s.Matrix([s.sqrt(6)*R[i,i]/(4*a) for i in range(3)]+[s.sqrt(12)*R[i,j]/(4*a) for i,j in [(0,1),(0,2),(1,2)]])
F=q.jacobian(ss)
cd=s.sqrt(6)*sigma*delta/(4*a);co=s.sqrt(12)*sigma*mm/(4*a)
check('Full six-coordinate determinant with its sign',s.simplify(F.det()-2*cd**3*co**3)==0)
back=s.Matrix(3,3,lambda i,j:(s.trace(R)/2-R[i,i])/(sigma*delta) if i==j else R[i,j]/(sigma*mm))
check('Coordinate inverse in every original tensor entry',s.simplify(back-S)==s.zeros(3))
check('Raw six-state norm equals full symmetric-matrix colour contractions',s.simplify(q.dot(q)-3*s.trace(R.T*R)/(8*a*a))==0)
eta=s.Matrix([s.Rational(1,4),s.Rational(3,8),-s.Rational(9,4)])
star=eta*eta.T
check('Original signed Fabel endpoint tensor retained',star==s.Matrix([[4,6,-36],[6,9,-54],[-36,-54,324]])/64)
starq=q.subs(dict(zip(ss,[star[0,0],star[1,1],star[2,2],star[0,1],star[0,2],star[1,2]])))
check('Endpoint samples all six coordinates nontrivially',all(v!=0 for v in starq))
ns=sigma**2*delta**2*s.trace(S)**2/(2*a*a)
nt=3*sigma**2*delta**2*sum((S[i,i]-s.trace(S)/3)**2 for i in range(3))/(8*a*a)
no=3*sigma**2*mm**2*sum(S[i,j]**2 for i,j in [(0,1),(0,2),(1,2)])/(4*a*a)
check('All three channel masses sum to the full raw norm',s.simplify(ns+nt+no-q.dot(q))==0)
starsub=dict(zip(ss,[star[0,0],star[1,1],star[2,2],star[0,1],star[0,2],star[1,2]]))
check('Exact Fabel scalar channel mass',s.simplify(ns.subs(starsub)-sigma**2/a**2*s.Rational(113569,8192)*delta**2)==0)
check('Exact Fabel diagonal traceless channel mass',s.simplify(nt.subs(starsub)-sigma**2/a**2*s.Rational(100825,16384)*delta**2)==0)
check('Exact Fabel offdiagonal channel mass',s.simplify(no.subs(starsub)-sigma**2/a**2*s.Rational(1593,2048)*mm**2)==0)
dd,oo,cc=s.symbols('dd oo cc',real=True)
KM=s.diag(s.Matrix([[dd,oo,oo],[oo,dd,oo],[oo,oo,dd]]),cc*s.eye(3))
check('Full tensor quadratic form has all three channel coefficients',s.simplify((q.T*KM*q)[0]-(dd+2*oo)*ns-(dd-oo)*nt-cc*no)==0)
J=s.Matrix([[0,0,1],[0,-1,0],[1,0,0]])
QQ=s.Matrix([[ss[0],ss[3],ss[4]],[ss[3],ss[1],ss[5]],[ss[4],ss[5],ss[2]]])
transformed=J*QQ*J.T
SSJ=s.Matrix([transformed[0,0],transformed[1,1],transformed[2,2],transformed[0,1],transformed[0,2],transformed[1,2]]).jacobian(ss)
check('Exact source-to-normal basis signs preserve full correction matrix',SSJ.T*SSJ==s.eye(6) and SSJ.T*KM*SSJ==KM)
si,sj,sk,theta=s.symbols('si sj sk theta',positive=True)
d=s.sqrt(8/(si*sj*sk))*theta
check('Full input cubic raw-norm dictionary',s.simplify(6*d*d-48*theta*theta/(si*sj*sk))==0)
check('Full input inverse-energy dictionary',s.simplify(6*d*d*a/(si+sj+sk)-48*a*theta*theta/(si*sj*sk*(si+sj+sk)))==0)

# Direct Pauli fundamental Casimir, including all four face letters.
pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
TT=[-s.I*m/2 for m in pauli]
check('Original Casimir sum on each fundamental edge',sum((m*m for m in TT),s.zeros(2))==-3*s.eye(2)/4)
check('All four original face edges give eigenvalue three',4*s.Rational(3,4)==3)
gg=s.symbols('g',positive=True)
check('Original cross coefficient has no coupling loss',(2*gg**2/a)*(1/(2*gg**2*a))==1/a**2)
n0,n2,k,Delta=s.symbols('n0 n2 k Delta',nonzero=True)
ratio=(Delta*(n0+gg**2*n2)+gg**2*k)/(n0+gg**2*n2)
check('Second raw-amplitude coefficient cancels only in the quotient',s.series(ratio,gg,0,3).removeO()==Delta+gg**2*k/n0)

# The fluid right inverse is checked in physical coordinates before sampling.
xx=s.Matrix(s.symbols('x y z',real=True));ww=s.Matrix(s.symbols('w1 w2 w3',real=True))
def curl(v):return s.Matrix([s.diff(v[2],xx[1])-s.diff(v[1],xx[2]),s.diff(v[0],xx[2])-s.diff(v[2],xx[0]),s.diff(v[1],xx[0])-s.diff(v[0],xx[1])])
pot=-xx.dot(xx)*ww/4
vel=curl(pot)
check('Vector-potential right inverse has exact one-half velocity factor',vel==ww.cross(xx)/2)
check('Its sampled curl equals all three prescribed components',curl(vel)==ww)
chi=s.Function('chi')(*xx)
cutvel=curl(chi*pot)
check('Compact cutoff preserves exact divergence-free identity',s.simplify(sum(s.diff(cutvel[i],xx[i]) for i in range(3)))==0)
from itertools import product
mid=[]
for vertex in product(range(-2,3),repeat=3):
    for direction in range(3):
        if vertex[direction]<2:
            mid.append(s.Matrix([s.Integer(vertex[i])+s.Rational(int(i==direction),2) for i in range(3)]))
min_dist=min((mid[i]-mid[j]).dot(mid[i]-mid[j]) for i in range(len(mid)) for j in range(i))
check('All original L2 edge midpoints and disjoint physical bump radius',len(mid)==300 and min_dist==s.Rational(1,2) and (2*s.Rational(1,8))**2<min_dist)

# Full ten-dimensional real family, with one vacuum, an exact sixfold
# comparison band and all three other states retained. This independent family
# is a diagnostic for the formula, never a claimed Yang--Mills discretization.
ener=s.Matrix([0,2,2,2,2,2,2,5,7,11]);H0=s.diag(*ener)
H1=s.zeros(10);H2=s.zeros(10)
for i in range(7):
    for j in range(7,10):H1[i,j]=H1[j,i]=s.Rational(((3*i+2*j)%7)-3,5)
for i in range(10):
    for j in range(i,10):
        if (i<7)==(j<7):H2[i,j]=H2[j,i]=s.Rational(((i+2*j)%9)-4,7)
parity=s.diag(*([1]*7+[-1]*3))
check('Independent family exact odd-even conjugation',parity*H1*parity==-H1 and parity*H2*parity==H2)
v0=s.eye(10)[:,0];base=s.eye(10)[:,1:7]
R0=s.diag(*[0 if i==0 else 1/ener[i] for i in range(10)])
Rstar=s.diag(*[1/(ener[i]-2) if i not in range(1,7) else 0 for i in range(10)])
phi1=-R0*H1*v0
e2=(v0.T*(H1*phi1+H2*v0))[0]
phi2=-R0*(H1*phi1+H2*v0)
chi2=phi2-phi1.dot(phi1)*v0/2
eta_mat=-Rstar*H1*base
Kabs=base.T*H2*base-base.T*H1*Rstar*H1*base
K=Kabs-e2*s.eye(6)
zeta_mat=-Rstar*(H1*eta_mat+H2*base-base*Kabs)
G2=eta_mat.T*eta_mat
check('Every first-band quasimode coefficient equation',(H0-2*s.eye(10))*eta_mat+H1*base==s.zeros(10,6) and (H0-2*s.eye(10))*zeta_mat+H1*eta_mat+H2*base-base*Kabs==s.zeros(10,6))
check('Raw frame retains the full nonzero second Gram coefficient',base.T*zeta_mat==s.zeros(6) and G2!=s.zeros(6))

# Use a fully populated nonsingular tensor coordinate matrix in this family.
FF=F.subs({a:2,sigma:s.Rational(3,2),delta:-2,mm:3})
Ds=[]
for col in range(6):
    D0=s.zeros(10);D1=s.zeros(10);D2=s.zeros(10)
    for i in range(6):D0[i+1,0]=D0[0,i+1]=FF[i,col]
    for i in range(10):
        D0[i,i]=s.Rational((i+col)%5,4)
        D2[i,i]=s.Rational((i+2*col)%4,3)
    for i in range(7):
        for j in range(7,10):D1[i,j]=D1[j,i]=s.Rational((i+j+col)%5-2,6)
    Ds.append((D0,D1,D2))
def coeffs(D0,D1,D2):
    m0=(v0.T*D0*v0)[0]
    m2=(v0.T*D2*v0)[0]+2*(phi1.T*D1*v0)[0]+2*(chi2.T*D0*v0)[0]+(phi1.T*D0*phi1)[0]
    xi0=(D0-m0*s.eye(10))*v0
    xi1=D1*v0+(D0-m0*s.eye(10))*phi1
    xi2=(D2-m2*s.eye(10))*v0+D1*phi1+(D0-m0*s.eye(10))*chi2
    return xi0,xi1,xi2
BS=s.zeros(6)
for col,Dscol in enumerate(Ds):
    xi0,xi1,xi2=coeffs(*Dscol)
    check(f'No first coordinate response for profile{col}',base.T*xi1+eta_mat.T*xi0==s.zeros(6,1))
    BS[:,col]=base.T*xi2+eta_mat.T*xi1+zeta_mat.T*xi0-G2*FF[:,col]
def arr(M):return np.array(M.evalf(),dtype=float)
h0,h1,h2=map(arr,[H0,H1,H2]);fmat,kmat,g2,bsmat=map(arr,[FF,K,G2,BS])
base_a,eta_a,zeta_a=map(arr,[base,eta_mat,zeta_mat])
darr=[tuple(map(arr,D)) for D in Ds]
def compute(g):
    hh=h0+g*h1+g*g*h2
    ee,uu=np.linalg.eigh(hh)
    psi=uu[:,0]
    if psi[0]<0:psi=-psi
    band=uu[:,1:7];P=band@band.T
    R=P@(base_a+g*eta_a+g*g*zeta_a)
    Gram=R.T@R
    states=[]
    for da,db,dc in darr:
        dd=da+g*db+g*g*dc
        xi=(dd-(psi@dd@psi)*np.eye(10))@psi
        states.append(P@xi)
    T=np.array(states).T
    Q=np.linalg.solve(Gram,R.T@T)
    Avec=np.linalg.solve(Gram,R.T@(hh-ee[0]*np.eye(10))@R)
    predicted=Q.T@Gram@expm(-0.4*(Avec-2*np.eye(6))/(g*g))@Q
    exact=T.T@band@np.diag(np.exp(-0.4*(ee[1:7]-ee[0]-2)/(g*g)))@band.T@T
    return dict(Q=Q,Gram=Gram,Avec=Avec,T=T,P=P,exact=exact,predicted=predicted)
out=[]
for g in [0.02,0.01,0.005]:
    v=compute(g)
    check(f'Exact projected tensor inverse and onto range,g={g}',np.linalg.norm(v['T']@np.linalg.solve(v['T'].T@v['T'],v['T'].T)-v['P'])<2e-12)
    check(f'Raw-frame long-time identity with exact projector,g={g}',np.linalg.norm(v['exact']-v['predicted'])<2e-8)
    errQ=np.linalg.norm((v['Q']-fmat)/(g*g)-bsmat)
    errG=np.linalg.norm((v['Gram']-np.eye(6))/(g*g)-g2)
    errK=np.linalg.norm((v['Avec']-2*np.eye(6))/(g*g)-kmat)
    errLong=np.linalg.norm(v['exact']-fmat.T@expm(-0.4*kmat)@fmat)
    out.append(dict(g=g,q_second_error=errQ,raw_Gram_second_error=errG,interaction_matrix_error=errK,long_time_error=errLong))
for key in ['q_second_error','raw_Gram_second_error','interaction_matrix_error','long_time_error']:
    check('Independent band convergence for '+key,all(out[i+1][key]<out[i][key]*0.4 for i in range(2)))
check('Independent second-coordinate coefficient accuracy',out[-1]['q_second_error']<0.001)
check('Independent raw Gram coefficient accuracy',out[-1]['raw_Gram_second_error']<0.001)
result=dict(passed=all(c['passed'] for c in checks),groups=len(checks),checks=checks,independent_matrix_diagnostics=out,
            scope='Exact coordinate and raw-coefficient algebra, plus a complete separate ten-dimensional matrix family. This tests the band formulas; it does not numerically evaluate the full YM interaction matrix or certify a continuum limit.')
(ROOT/'INTERACTING_TENSOR_BAND_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(passed=result['passed'],groups=len(checks),diagnostics=out),indent=2))
