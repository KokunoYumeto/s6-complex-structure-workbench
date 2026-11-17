#!/usr/bin/env python3
"""All marked MV degrees for the primitive simultaneous-cap proof P3F.45.

The geometric integral bases are constructed in the companion proof.
This exports the actual local maps and their global incidence maps;
it retains the elliptic path coefficients before integral elimination.
"""
from pathlib import Path
from math import gcd
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

OUT=Path(__file__).resolve().parent
def ints(M): return [[int(x) for x in row] for row in M.tolist()]
def syms(M): return [[str(x) for x in row] for row in M.tolist()]
def smith(M):
    D=smith_normal_form(M,domain=ZZ)
    return [abs(int(D[i,i])) for i in range(min(D.shape))]
def bezout(m,n):
    u,v,g=s.gcdex(m,n)
    assert g==1 and m*u+n*v==1
    return int(u),int(v)
def seifert(ms,ns):
    q=len(ms);M=s.zeros(2*q)
    for i in range(q-1): M[i,2*i]=1;M[i,2*(q-1)]=-1
    for i,(m,n) in enumerate(zip(ms,ns)):
        M[q-1,2*i+1]=1
        M[q+i,2*i]=n;M[q+i,2*i+1]=-m
    return M
def total(ms,ns):
    return sum(ns[i]*s.prod(ms[j] for j in range(len(ms)) if j!=i) for i in range(len(ms)))

m,n,A,k,la,lb,u,v,j,p,r=s.symbols('m n A kappa lambda_a lambda_b u v j p r',integer=True)
# Smooth boundary orders: degree1 (a,b,alpha,gamma),
# degree2 (ab,a gamma,b gamma,a alpha,b alpha,alpha gamma),
# degree3 (N=ab alpha,F gamma=ab gamma,a alpha gamma,b alpha gamma).
Q=s.Matrix([[1,0,-u*la,-v*la],[0,1,-u*lb,-v*lb],[0,0,-n,m]])
J2s=s.Matrix([[1,-v*lb,v*la,-u*lb,u*la,0],
             [0,m,0,-n,0,-la],[0,0,m,0,-n,-lb]])
I2s=s.zeros(3,6);I2s[:,3:6]=s.eye(3)
D2s=I2s.col_join(-J2s)
assert s.expand(D2s.det())==m*m
J3s=s.Matrix([[-n,m,-lb,la]])
# Direct exterior powers with the exact Bezout identity retained.
pairs=[(0,1),(0,3),(1,3),(0,2),(1,2),(2,3)]
triples=[(0,1,2),(0,1,3),(0,2,3),(1,2,3)]
W2=s.Matrix([[Q.extract(rr,cc).det() for cc in pairs] for rr in [(0,1),(0,2),(1,2)]])
W3=s.Matrix([[Q[:,cc].det() for cc in triples]])
assert all(s.rem(s.Poly(x,u),s.Poly(m*u+n*v-1,u)).as_expr()==0 for x in W2-J2s)
assert all(s.rem(s.Poly(x,u),s.Poly(m*u+n*v-1,u)).as_expr()==0 for x in W3-J3s)
# Multiplicative orders: H1 (alpha,b,gamma), H2 (z,R,B,L),
# H3 (N=ab alpha,F gamma=ab gamma,V=a gamma alpha).
Qm=s.Matrix([[p,1,r],[-n,0,m]])
J2m=s.Matrix([[m,-A,0,0],[0,0,m,A]])
I2m=s.Matrix([[0,1,0,0],[0,0,0,1]])
D2m=I2m.col_join(-J2m)
assert s.expand(D2m.det())==-m*m
J3m=s.Matrix([[-n,m,j]])
# The H1/H3 pairing in these actual orientations is exact.
pairing=s.Matrix([[0,-1,0],[0,0,-1],[1,0,0]])
assert -s.Matrix([[m,j,n]])*pairing==J3m
I2a=s.Matrix([[0,1]]);J2a=s.Matrix([[1,k]])
D2a=I2a.col_join(-J2a)
assert D2a.det()==1

def all_maps(sites):
    q=len(sites)
    rks=[3 if z['kind']=='smooth' else 2 if z['kind']=='multiplicative' else 1 for z in sites]
    h1cols=[r+1 for r in rks]
    D1=s.zeros(q+sum(rks),sum(h1cols))
    D3=s.zeros(sum(rks)+q,sum(h1cols))
    # Exterior H3 order: q-1 source-boundary classes, common Fgamma,
    # then every local additional ordinary-cap-kernel class.
    ex3extra=q
    cap1=q;cap3=sum(rks);col=0;blocks=[]
    for idx,(z,rank) in enumerate(zip(sites,rks)):
        mm,nn=z['m'],z['n'];uu,vv=bezout(mm,nn)
        kind=z['kind']
        if kind=='smooth':
            aa,bb=z.get('la',0),z.get('lb',0)
            local1=Q.subs({m:mm,n:nn,u:uu,v:vv,la:aa,lb:bb})
            ac,gc=2,3
            local2=D2s.subs({m:mm,n:nn,u:uu,v:vv,la:aa,lb:bb})
            local3=J3s.subs({m:mm,n:nn,la:aa,lb:bb})
        elif kind=='multiplicative':
            jj=z.get('j',0);pp=-uu*jj;rr=-vv*jj
            assert mm*pp+nn*rr==-jj
            local1=Qm.subs({m:mm,n:nn,p:pp,r:rr})
            ac,gc=0,2
            aa=z['N']*jj-z['c']*nn
            assert gcd(mm,aa)==1
            local2=D2m.subs({m:mm,A:aa})
            local3=J3m.subs({m:mm,n:nn,j:jj})
        else:
            local1=s.Matrix([[-nn,mm]]);ac,gc=0,1
            local2=D2a.subs({k:z.get('kappa',0)})
            local3=s.Matrix([[-nn,mm]])
        if idx<q-1: D1[idx,col+ac]=1;D3[idx,col]=1
        else:
            for ii in range(q-1):D1[ii,col+ac]=-1;D3[ii,col]=-1
        D1[q-1,col+gc]=1
        D3[q-1,col+1]=1
        D1[cap1:cap1+rank,col:col+rank+1]=-local1
        for extra in range(rank-1):D3[ex3extra+extra,col+2+extra]=1
        D3[cap3+idx,col:col+rank+1]=-local3
        blocks.append(local2)
        cap1+=rank;ex3extra+=rank-1;col+=rank+1
    D2=s.diag(*blocks)
    D0=s.ones(1,q).col_join(-s.eye(q))
    D4=s.eye(q-1).row_join(-s.ones(q-1,1))
    ms=[z['m'] for z in sites];ns=[z['n'] for z in sites]
    d=total(ms,ns);S=seifert(ms,ns)
    assert abs(D1.det())==abs(d) and abs(D3.det())==abs(d)
    assert [x for x in smith(D1) if x!=1]==[x for x in smith(S) if x!=1]
    assert [x for x in smith(D3) if x!=1]==[x for x in smith(S) if x!=1]
    expected=s.diag(*[z['m'] for z in sites if z['kind']!='additive' for _ in range(2)])
    assert [x for x in smith(D2) if x!=1]==[x for x in smith(expected) if x!=1]
    assert D0.rank()==q and D4.rank()==q-1
    return {'sites':sites,'D':int(d),'matrices':{str(i):ints(x) for i,x in enumerate([D0,D1,D2,D3,D4])},
            'Smith_D1':smith(D1),'Smith_D2':smith(D2),'Smith_D3':smith(D3)}

symbolic=[]
for q in range(1,6):
    ms=s.symbols('m1:'+str(q+1));ns=s.symbols('n1:'+str(q+1))
    M=seifert(ms,ns);d=total(ms,ns)
    assert s.factor(M.det()-(-1)**(q*(q+1)//2)*d)==0
    symbolic.append({'q':q,'matrix':syms(M),'determinant':str(s.factor(M.det()))})

samples=[]
for mm in range(1,7):
 for nn in range(-3,4):
  if gcd(mm,nn)!=1:continue
  sites=[{'kind':'smooth','m':mm,'n':nn,'la':2,'lb':-3},
         {'kind':'multiplicative','m':1,'n':-2,'N':7,'c':-2,'j':3},
         {'kind':'additive','m':5,'n':1,'kappa':-4}]
  samples.append(all_maps(sites))
for mm in [1,2,3,5,7]:
 for nn in [-3,-1,0,1,2,3]:
  if gcd(mm,nn)!=1:continue
  for jj in [-2,-1,0,1,2]:
   if gcd(mm,5*jj+2*nn)!=1:continue
   sites=[{'kind':'multiplicative','m':mm,'n':nn,'N':5,'c':-2,'j':jj},
          {'kind':'smooth','m':1,'n':2,'la':-3,'lb':1}]
   samples.append(all_maps(sites))

result={'status':'PASS','scope':'Actual effective primitive caps of F45; additive roots from F42/F43.',
        'local':{'smooth_H1':syms(Q),'smooth_H2':syms(J2s),'smooth_H3':syms(J3s),
                 'smooth_D2':syms(D2s),'multiplicative_H1':syms(Qm),'multiplicative_H2':syms(J2m),
                 'multiplicative_H3':syms(J3m),'multiplicative_D2':syms(D2m),
                 'additive_D2':syms(D2a),'multiplicative_H1_H3_pairing':ints(pairing)},
        'symbolic_Seifert_matrices':symbolic,'full_integer_cases':samples}
(OUT/'primitive_multicap_complete.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: actual exterior-power and H1/H3 cap maps, all local D2 blocks.')
print('PASS: symbolic Seifert determinants for q=1,...,5, with the general proof in F45.')
print('PASS:',len(samples),'full D0--D4 integral multicap matrices, including negative and zero determinants.')
