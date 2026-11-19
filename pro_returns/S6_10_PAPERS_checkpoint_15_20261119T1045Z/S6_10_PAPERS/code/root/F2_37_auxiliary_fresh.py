from pathlib import Path
from functools import reduce
from math import gcd
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form

checks=[]
def ck(name,value):
    ok=bool(value);checks.append({'name':name,'pass':ok});assert ok,name
def cycle(n):
    M=S.zeros(n)
    for j in range(n):M[(j+1)%n,j]=1
    return M
def primitive(v):
    den=S.ilcm(*[x.q for x in v]);a=[int(x*den) for x in v];g=reduce(gcd,[abs(x) for x in a]);return S.Matrix([x//g for x in a])
examples=[]
for d in range(2,7):
    M=S.diag(cycle(d),S.eye(6-d)) if d<6 else cycle(d)
    examples.append((f'cycle{d}',M,d))
examples.extend([('three_swaps',S.diag(cycle(2),cycle(2),cycle(2)),2),('cubic_plus_identity',S.diag(S.Matrix([[0,-1],[1,-1]]),S.eye(4)),3),('quartic_plus_identity',S.diag(S.Matrix([[0,-1],[1,0]]),S.eye(4)),4)])
for label,M,d in examples:
    u=primitive((M-S.eye(6)).nullspace()[0]);SM=sum((M**j for j in range(d)),S.zeros(6))
    ck(label+' fixed primitive',M*u==u and reduce(gcd,[abs(int(x)) for x in u])==1)
    ck(label+' exact order',M**d==S.eye(6) and all(M**j!=S.eye(6) for j in range(1,d)))
    ck(label+' integer averaging',SM*u==d*u and all(x.is_Integer for x in SM))
    for j in range(1,d*d):
        ck(label+f' power{j} averaging',SM*(M**j-S.eye(6))==S.zeros(6))
        obstruction=j*u/d if j%d else j*u/(d*d)
        ck(label+f' power{j} nonintegral obstruction',any(not x.is_Integer for x in obstruction))
        if not j%d:ck(label+f' power{j} actual translation',M**j==S.eye(6))
    ck(label+' endpoint identity',M**(d*d)==S.eye(6) and all(x.is_Integer for x in u))
u=S.Matrix([1,2,3,4,5,6]);ck('identity half-vector order2',any(not x.is_Integer for x in u/2) and all(x.is_Integer for x in u))
for label,M in [('minus_identity',-S.eye(6)),('three_cubic_blocks',S.diag(*([S.Matrix([[0,-1],[1,-1]])]*3)))]:
    a=S.Matrix([S.Rational(1,j+2) for j in range(6)]);x=(S.eye(6)-M).inv()*a
    ck(label+' exact fixed-point map',M*x+a==x)
A=S.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=S.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
C=(A*B).inv();N=C-S.eye(6)
ck('actual base square-zero rank3',N*N==S.zeros(6) and N.rank()==3)
SN=smith_normal_form(N,domain=S.ZZ)
ck('actual base primitive image',[abs(SN[i,i]) for i in range(6) if SN[i,i]]==[1,1,1])
def key(tup):
    flat=tuple(int(x) for m in tup for x in m);return (max(map(abs,flat)),flat)
def insert(tup,i):return tup[:i]+(S.eye(6),)+tup[i:]
tuples=[]
for i in range(6):
    j=(i+1)%6
    for k in [-2,-1,1,2]:
        P=S.eye(6);P[i,j]=k
        if k<0:P[:,0]=-P[:,0]
        ck(f'witness{i},{k} unimodular',abs(P.det())==1)
        tup=tuple(P*m*P.inv() for m in (A,B,C));tuples.append(tup)
        for slot in range(3):
            full=insert(tup,slot);base=insert((A,B,C),slot)
            ck(f'witness{i},{k} slot{slot} same map',all(P*base[j]*P.inv()==full[j] for j in range(4)))
            ck(f'witness{i},{k} slot{slot} height',key(full)[0]==key(tup)[0])
            ck(f'witness{i},{k} slot{slot} product',full[0]*full[1]*full[2]*full[3]==S.eye(6))
for i in range(len(tuples)):
    for j in range(i+1,len(tuples)):
        for slot in range(3):
            ck(f'lex{i},{j},slot{slot}',(key(tuples[i])<key(tuples[j]))==(key(insert(tuples[i],slot))<key(insert(tuples[j],slot))))
out={'status':'PASS','check_count':len(checks),'scope':'Exact specified affine lift, invariant integer averaging, actual fixed-point obstruction, and marked identity deletion/reinsertion maps only','checks':checks}
Path('analysis/continuation_root/F2_37_auxiliary_fresh.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','check_count':len(checks)}))
