#!/usr/bin/env python3
"""Exact reduced-II root, Cartier characters, restriction lattices and joint MV."""
from pathlib import Path
from itertools import combinations
from math import gcd
import sympy as s,json,hashlib
from sympy.matrices.normalforms import smith_normal_form,hermite_normal_form
ROOT=Path(__file__).resolve().parents[2];checks=[]
def ck(name,v):
 assert bool(v),name;checks.append(name)
def mat(A):return [[int(v) if v.is_Integer else str(v) for v in A.row(i)] for i in range(A.rows)]
def snf(A):
 D=smith_normal_form(A,domain=s.ZZ);return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
def contraction(v,q):
 si=list(combinations(range(4),q));ti=list(combinations(range(4),q-1));A=s.zeros(len(ti),len(si))
 for j,I in enumerate(si):
  for p,i in enumerate(I):A[ti.index(I[:p]+I[p+1:]),j]+=(-1)**p*v[i]
 return A
T=[s.Matrix(A) for A in [[[1,-3,-3,-1],[0,-2,-3,-1],[0,1,1,0],[0,0,0,1]],[[1,0,0,0],[0,1,1,0],[0,-1,0,0],[0,0,0,1]],[[1,0,3,1],[0,1,2,1],[0,0,1,0],[0,0,0,1]]]]
H=[A.inv().T for A in T]
Bell=T[1].extract([1,2],[1,2]);Hell=Bell.inv().T
ck('rank-two elliptic cohomology determinant',int((Bell-s.eye(2)).det())==1)
ck('rank-two elliptic homology determinant',Hell==s.Matrix([[0,1],[-1,1]]) and int((Hell-s.eye(2)).det())==1)
gen={1:s.Matrix([1,0,0,0]),2:s.Matrix([0,0,3,1,0,0]),3:s.Matrix([1,0,0,0]),4:s.Matrix([1])}
co={0:s.Matrix([[1]]),1:s.Matrix([[0,0,0,1]]),2:s.Matrix([[0,0,1,3,0,0]]),3:s.Matrix([[0,0,0,1]])}
kk,hh,na,nb,da,db=s.symbols('k h nA nB dA dB',integer=True);mm=3*kk
ell0=s.Matrix([1,-1,0,0]);gamma=s.Matrix([1,0,0,0]);delta=s.Matrix([0,0,0,1])
idx={1:mm*hh,2:kk*hh,3:kk*hh,4:mm*hh};symbolic={}
for q in range(1,5):
 prism=contraction(na*ell0+da*delta,q)/mm+contraction(nb*gamma+db*delta,q)/hh
 value=s.simplify((co[q-1]*prism*(idx[q]*gen[q]))[0])
 ck(f'full symbolic prism degree{q}',s.expand(value-hh*na-mm*nb)==0)
 symbolic[q]={'operator':mat(prism),'primitive_index':str(idx[q]),'value':str(value)}
x,y,q,z,X,Y=s.symbols('x y q z X Y')
old=y*y-x**3+3*(1+q)**3*q*x-(1+q)**4*q*(1+2*q)
root_examples=[]
for l in [1,2,3]:
 h=6*l+1
 new=Y*Y-X**3+3*(1+z**h)**3*z**(2*l+1)*X-z*(1+z**h)**4*(1+2*z**h)
 ck(f'exact reduced root equation l{l}',s.expand(old.subs({q:z**h,x:z**(2*l)*X,y:z**(3*l)*Y})/z**(6*l)-new)==0)
 xg=(1+z**h)**2/z**(2*l);yg=(1+z**h)**2/z**(3*l)
 ck(f'actual G equation l{l}',s.factor(new.subs({X:xg,Y:yg}))==0)
 ck(f'exact formal G parameter l{l}',s.cancel(-xg/yg+z**l)==0)
 ck(f'central deck primitive l{l}',gcd(l,h)==1)
 for j in range(1,l+1):
  u=s.symbols('u')
  ck(f'Cartier cancellation l{l} j{j}',s.cancel((z**j*u+z**l)/(z**j*u)-(u+z**(l-j))/u)==0)
 root_examples.append({'l':l,'h':h,'source_equation':str(new),'formal_parameter_G':f'-z^{l}','chain_characters':[l-j for j in range(1,l+1)]})
A=s.Matrix([[0,1],[-3,0]]);Q2=s.Matrix([[0,3],[3,0]])
cases=[]
for k in [1,2,3,5]:
 m=3*k
 for l in [1,2,3]:
  h=6*l+1
  if gcd(m,h)!=1:continue
  for eps in [-1,1]:
   nA=eps*pow(h,-1,m);nB=(eps-h*nA)//m
   for dA,dB in [(-1,2),(0,0),(3,-2)]:
    label=f'k{k}h{h}e{eps}d{dA},{dB}'
    ck(label+' exact norm determinant',h*nA+m*nB==eps)
    invm=pow(nA,-1,m);invk=pow(nA,-1,k) if k>1 else 0
    K1=s.Matrix([[m,-3*dA*invm],[0,1]])
    K2=s.diag(k,1);K3=s.Matrix([[k,-dA*invk],[0,1]])
    pair13=K1.T*A*K3/m;pair22=K2.T*Q2*K2/m
    ck(label+' star H1 norm kernel',all(int(v)%m==0 for v in s.Matrix([[nA,3*dA]])*K1))
    ck(label+' star H3 norm kernel',all(int(v)%k==0 for v in s.Matrix([[nA,dA]])*K3))
    ck(label+' star exact dual covering pairing',all(v.q==1 for v in pair13) and abs(pair13.det())==1)
    ck(label+' star exact H2 covering pairing',all(v.q==1 for v in pair22) and abs(pair22.det())==1)
    C1=s.Matrix([[h,-dB*pow(nB,-1,h)],[0,1]])
    ck(label+' II full H1 pullback',C1.det()==h and all(int(v)%h==0 for v in s.Matrix([[nB,dB]])*C1))
    ck(label+' II rotation product character',(pow(nB,-1,h)*nB-1)%h==0)
    P={1:s.Matrix([[m,0,nA],[0,h,nB]]),2:s.Matrix([[k,0,1],[0,h,3]]),3:s.Matrix([[k,0,nA],[0,h,nB]]),4:s.Matrix([[m,0,1],[0,h,1]])}
    for j,M in P.items():ck(label+f' degree{j} exact MV Smith',snf(M)==[1,1])
    Sf=s.Matrix([[-nA,m,0],[-nB,0,h],[0,1,1]])
    ck(label+' exact surviving fundamental determinant',Sf.det()==eps and snf(Sf)==[1,1,1])
    Dpi=s.zeros(6,11);Dpi[:4,:8]=s.Matrix.hstack(H[1]-s.eye(4),H[2]-s.eye(4))
    Dpi[:4,8]=-(nA*ell0+dA*delta);Dpi[4,8]=m
    Dpi[:4,9]=-(nB*gamma+dB*delta);Dpi[5,9]=h
    Dpi[4,10]=1;Dpi[5,10]=1
    ck(label+' full six-generator relation Smith',snf(Dpi)==[1]*6)
    cases.append({'k':k,'l':l,'m':m,'h':h,'nA':nA,'nB':nB,'dA':dA,'dB':dB,'D':eps,'star_H1_pullback':mat(K1),'star_H2_pullback':mat(K2),'star_H3_pullback':mat(K3),'star_normalized_H1_H3_pairing':mat(pair13),'II_H1_H3_pullback':mat(C1),'global_MV':{j:mat(M) for j,M in P.items()},'full_fundamental_matrix':mat(Dpi),'Seifert_matrix':mat(Sf)})
notes=ROOT/'notes/part3_os49_reduced_ii_caps_working.md'
out={'status':'PASS','checks':len(checks),'scope':'Exact named root/Cartier/finite norms and integral specialization/prism/fundamental maps; geometric proof remains submitted for independent audit. No return assigned.','note_sha256':hashlib.sha256(notes.read_bytes()).hexdigest(),'check_names':checks,'symbolic_prism':symbolic,'root_examples':root_examples,'cases':cases,'explicit_smallest_sphere':{'m':3,'h':7,'nA':1,'nB':-2,'dA':0,'dB':0,'D':1},'topology':'D=+-1 gives pi1=0,H0=H6=Z, other homology0 in the displayed two-cap construction.'}
(ROOT/'code/part3/os49_reduced_ii_caps.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(checks),'exact root, Cartier, restriction, duality, MV, prism and fundamental identities;',len(cases),'full signed cases.')
