#!/usr/bin/env python3
"""Post-release comparison of all printed KK lattices and historical inputs."""
from contextlib import redirect_stdout
from datetime import datetime,timezone
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from io import StringIO
from itertools import combinations,product
from math import gcd
from pathlib import Path
import urllib.request
import sympy as S

HERE=Path(__file__).resolve().parent
URL=('https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/'
     'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/'
     'pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/'
     'S6_10_PAPERS/code/III/manifolds_yang.py')
OLD=Path('/tmp/S6_SERIES_PUBLISH_c5_02KK_primary/manifolds_yang.py')
if not OLD.exists():
    with urllib.request.urlopen(urllib.request.Request(URL,headers={'User-Agent':'Mozilla/5.0'}),timeout=30) as response:
        OLD.write_bytes(response.read())
assert sha256(OLD.read_bytes()).hexdigest()=='4928a45fc66b89e83f64888007a8aea2dd835367571a5a26b83c89032ee1cf85'
assert len(OLD.read_text().splitlines())==215
print('Historical source:',URL)
print('Historical bytes:',OLD.stat().st_size,'SHA256:',sha256(OLD.read_bytes()).hexdigest())
print('All215 lines read after individual release21:04:11Z; not imported or executed; this is comparison evidence.')
spec=spec_from_file_location('kk_fresh',HERE/'S6_SERIES_PUBLISH_III_02KK_fresh_attachment.py')
f=module_from_spec(spec)
with redirect_stdout(StringIO()):spec.loader.exec_module(f)
print('Frozen fresh maps replayed unchanged; no additional independence credited.')
R,k,l,n1,n2,rr1,rr2=S.symbols('R k l n1 n2 r1 r2',integer=True)
p,q,al,be=S.symbols('p q alpha2 beta2',integer=True)
g,u,w,de=[S.eye(4)[:,j] for j in range(4)]
pair=f.pairs
def biv(x,y):return S.Matrix([x[i]*y[j]-x[j]*y[i] for i,j in pair])
def expand(A):return A.applyfunc(S.expand)
J=S.zeros(6)
for i,j,v in [(0,5,1),(1,4,-1),(2,3,1)]:J[i,j]=J[j,i]=v

def objects(c,d,a):
    m1=d*k;m2=6*l
    A1=S.Matrix([[1,0,0,0],[0,0,1,0],[-c*R,-1,2-c,0],[-R,0,-1,1]])
    A2=S.Matrix([[1,0,0,0],[0,1,-1,0],[0,1,0,0],[0,0,0,1]])
    om1=S.Matrix([-R,R,0,1,0,0]);om2=S.Matrix([1,-1,c,0,0,0])
    P1=S.Matrix.hstack(om1,a*k*om2)
    P2=S.Matrix.hstack(S.eye(6)[:,3],-m2*S.eye(6)[:,2])
    oldD=P1.T.col_join(-P2.T).row_join(S.Matrix([0,-n1,0,n2]))
    Cold=S.Matrix([[R,0,0],[-a*k,m1,-n1],[0,m2,n2]])
    Cnew=S.Matrix([[-R*n1,c*R*n2],[-a*k,-m2]])
    U4=S.Matrix([[1,0,1,0],[0,1,0,0],[0,0,0,1],[1,0,0,0]])
    e=[S.eye(7)[:,i] for i in range(7)]
    V7=S.Matrix.hstack(e[1]-R*e[3],e[2],e[6],e[3],e[0]+e[1],e[4],e[5])
    target=S.zeros(4,7);target[:3,:3]=Cold;target[3,3]=1
    assert U4*oldD*V7==target and abs(U4.det())==abs(V7.det())==1
    F=S.Matrix([[1,0],[0,-n1],[0,0]])
    t=be*n1-al*m1
    G=S.Matrix([[1,q*R,t*q*R],[0,-p,-t*p]])
    L=p*c*n2-q*m2
    Vrel=S.Matrix([[-n1,c*n2],[0,n2],[0,-m2]])
    Wrel=S.Matrix([[-p,be*L,-al*L],[0,be,-al]])
    Hnew=S.Matrix([[0,q],[0,0]])
    Hold=S.Matrix([[0,q,q*t],[0,0,-al],[0,0,-be]])
    subs={p:(1-a*k*q)/n1,al:(1-n2*be)/m2}
    for identity in [F*Cnew-Cold*Vrel,G*Cold-Cnew*Wrel,
                     G*F-S.eye(2)-Cnew*Hnew,F*G-S.eye(3)-Cold*Hold]:
        assert identity.subs(subs).applyfunc(S.cancel)==S.zeros(*identity.shape)
    return dict(A1=A1,A2=A2,P1=P1,P2=P2,om1=om1,om2=om2,
                oldD=oldD,Cold=Cold,Cnew=Cnew,U4=U4,V7=V7,target=target,
                F=F,G=G,Vrel=Vrel,Wrel=Wrel,Hnew=Hnew,Hold=Hold,m1=m1,m2=m2)

data={}
for typ,c,d,a in [('B',2,4,2),('C',3,3,1)]:
    ob=objects(c,d,a);data[typ]=(c,d,a,ob)
    A1,A2=ob['A1'],ob['A2'];m1,m2=ob['m1'],ob['m2']
    for AA,PP in [(A1,ob['P1']),(A2,ob['P2'])]:
        assert expand((f.wedge(AA.inv().T)-S.eye(6))*PP)==S.zeros(6,2)
    assert ob['om1'].T*J*ob['om1']==ob['om2'].T*J*ob['om2']==S.zeros(1,1)
    assert ob['om1'].T*J*ob['om2']==S.Matrix([[c]])
    assert ob['P1'].T*J*ob['P1']==S.Matrix([[0,m1],[m1,0]])
    assert ob['P2'].T*J*ob['P2']==S.Matrix([[0,-m2],[-m2,0]])
    v1=n1*(g-R*(u+w))+rr1*de;v2=n2*g+rr2*de
    assert expand(ob['P1'].T*biv(de,v1)/m1)==S.Matrix([0,-n1])
    assert expand(ob['P2'].T*biv(de,v2)/m2)==S.Matrix([0,n2])
    C0=f.wedge(A1*A2)-S.eye(6)
    rows=(1,5) if typ=='B' else (2,5)
    assert C0.extract(rows,(0,3)).det()==-1 and C0.rank()==2
    print(typ,'printed fixed forms, Gram matrices, finite sweep coordinates and cusp rank/minor agree')
    print(typ,'full4x7 -> 3x3+unit maps and mutually inverse3x3/2x2 cokernel maps verified symbolically')
    C=ob['Cold'];minor_values=[S.expand(C.extract(i,j).det()) for i in combinations(range(3),2) for j in combinations(range(3),2)]
    expected=[R*m1,R*n1,R*m2,R*n2,a*k*m2,a*k*n2,m2*n1+m1*n2]
    for value in minor_values:
        assert value==0 or any(S.expand(value-e)==0 or S.expand(value+e)==0 for e in expected)
    for e in expected:
        assert any(S.expand(value-e)==0 or S.expand(value+e)==0 for value in minor_values)
    print(typ,'all seven nonzero2x2 minor formulas match, including their signs up to the stated convention')

# Build the cusp restriction from its mathematical row formulas, and an integer
# preimage for every element of the kernel of the two coordinate sums.
def shift(v,j):return [v[(i+j)%len(v)] for i in range(len(v))]
def add(x,y):return [a+b for a,b in zip(x,y)]
def sub(x,y):return [a-b for a,b in zip(x,y)]
def restrict(v,ee):
    A,b1,b2,b3=v
    X=sub(b1,shift(A,1));X=add(X,shift(add(b2,b3),1))
    Y=sub(sub(sub(A,b1),b2),shift(b3,-ee))
    Z=sub(b2,shift(A,-ee-1));Z=add(Z,shift(add(b1,b3),-ee-1))
    return X+Y+Z
def preimage(X,Y,Z,ee):
    nn=len(X);assert sum(X)+sum(Y)==sum(Y)+sum(Z)==0
    zz=add(Z,shift(Y,-ee-1));h=[0]*nn
    for j in range(1,nn):h[j]=h[j-1]+zz[j]
    b2=h;b3=[-x for x in shift(h,ee)]
    rhs=sub(add(X,shift(Y,1)),shift(sub(b3,shift(b3,-ee)),1))
    b1=[0]*nn
    for j in range(nn-1):b1[j+1]=b1[j]-rhs[j]
    A=add(Y,b1)
    assert restrict((A,b1,b2,b3),ee)==X+Y+Z
    return A,b1,b2,b3
for ee in (1,2):
    for rr in range(1,17):
        for j in range(3*rr):
            v=[0]*(3*rr);v[j]=1
            X,Y,Z=v[:rr],v[rr:2*rr],v[2*rr:]
            b=sum(X)+sum(Y);c0=sum(Y)+sum(Z)
            X[0]-=b;Z[0]-=c0
            preimage(X,Y,Z,ee)
print('All32 historical cusp matrices have explicit integer preimages for the kernel of the split map toZ2; Smith data1^(3R-2),0,0.')

checked=zero_cases=0
for typ in ('B','C'):
    c,d,a,ob=data[typ]
    for rr,kk,ll,nn1,nn2 in product((1,2,3,4,6,12),range(1,5),range(1,4),(-5,-2,-1,1,2,5),(-5,-1,1,5)):
        mm1=d*kk;mm2=6*ll
        if gcd(nn1,mm1)!=1 or gcd(nn2,mm2)!=1:continue
        hh0,pp,qq=f.egcd(nn1,a*kk);assert hh0==1
        hh2,aa,bb=f.egcd(mm2,nn2);assert hh2==1
        ss={R:rr,k:kk,l:ll,n1:nn1,n2:nn2,p:pp,q:qq,al:aa,be:bb}
        Cd=ob['oldD'].subs(ss);Co=ob['Cold'].subs(ss);Cn=ob['Cnew'].subs(ss)
        assert ob['U4']*Cd*ob['V7'].subs(ss)==ob['target'].subs(ss)
        FF=ob['F'].subs(ss);GG=ob['G'].subs(ss)
        assert FF*Cn==Co*ob['Vrel'].subs(ss) and GG*Co==Cn*ob['Wrel'].subs(ss)
        assert GG*FF-S.eye(2)==Cn*ob['Hnew'].subs(ss)
        assert FF*GG-S.eye(3)==Co*ob['Hold'].subs(ss)
        d1,d2,_,_=f.diagonal_maps(Cn.tolist())
        PP=mm2*nn1+mm1*nn2;hh=gcd(gcd(rr,a*kk),PP)
        assert (d1,d2)==(hh,rr*abs(PP)//hh if PP else 0)
        d0=gcd(mm1,mm2)
        phi=[mm1*mm2//d0,mm2*nn1//d0,mm1*nn2//d0]
        assert gcd(gcd(phi[0],phi[1]),phi[2])==1
        assert -nn1*phi[0]+mm1*phi[1]==-nn2*phi[0]+mm2*phi[2]==0
        assert phi[1]+phi[2]==PP//d0
        checked+=1;zero_cases+=PP==0
assert (checked,zero_cases)==(2592,72)
print('All2592 historical full4x7 presentations verified by exact maps;72 haveP=0. Relative free-meridian values and kernel ranks agree.')

finite=0
for typ in ('B','C'):
    c,d,a,ob=data[typ]
    for rr,(kk,ll),(nn1,nn2),(rra,rrb) in product((1,2,6),((1,1),(3,2),(4,3)),((1,-1),(-1,1),(5,5)),((0,0),(7,-4),(-13,18))):
        mm1=d*kk;mm2=6*ll
        if gcd(nn1,mm1)!=1 or gcd(nn2,mm2)!=1:continue
        ss={R:rr,k:kk,l:ll,n1:nn1,n2:nn2,rr1:rra,rr2:rrb}
        for j in (1,2):
            AA=ob['A'+str(j)].subs(ss);PP=ob['P'+str(j)].subs(ss)
            mm=mm1 if j==1 else mm2;nn=nn1 if j==1 else nn2;rrt=rra if j==1 else rrb
            vv=nn*(g-rr*(u+w))+rrt*de if j==1 else nn*g+rrt*de
            assert AA*vv==vv
            assert (f.wedge(AA.inv().T)-S.eye(6))*PP==S.zeros(6,2)
            target=S.Matrix([[0,mm],[mm,0]])*(1 if j==1 else -1)
            assert PP.T*J*PP==target
            assert PP.T*biv(de,vv)/mm==S.Matrix([0,-nn if j==1 else nn])
            gg,aa,bb=f.egcd(mm,nn);assert gg==1
            # Primitive linear coinvariants followed by the explicit Bezout
            # section give exactly three primitive relations in Z5.
            qlin=S.Matrix([[1,0,0,0],[0,-1,1,-c]]) if j==1 else S.Matrix([[1,0,0,0],[0,0,0,1]])
            rv=qlin*vv
            H=S.Matrix([[0,1,0],[aa,0,bb]])
            # Verify the relation maps to zero and the two free coordinates
            # recover the basis (retained period,z).
            JJ=S.Matrix([[c*rrt*bb,1,-c*rrt*aa],[mm,0,nn]]) if j==1 else S.Matrix([[-rrt*bb,1,rrt*aa],[mm,0,nn]])
            sec=S.Matrix([[0,aa],[1,0],[0,bb]])
            assert JJ*sec==S.eye(2) and JJ*S.Matrix([-int(rv[0]),-int(rv[1]),mm])==S.zeros(2,1)
        finite+=1
assert finite==162
print('All162 historical finite quotient, integral pullback and delta-sweep inputs agree via primitive sections and the displayed pairings.')
for args in [('B',1,1,1,1,-1),('B',2,1,1,1,-1),('C',2,1,1,1,-1),('B',6,3,2,1,-1),('C',6,2,1,1,-1),('C',3,1,2,2,1),('B',101,7,11,3,-5)]:
    typ,rr,kk,ll,nn1,nn2=args;c,d,a,_=data[typ]
    PP=6*ll*nn1+d*kk*nn2;hh=gcd(gcd(rr,a*kk),PP)
    print('Historical example',args,'P',PP,'h',hh,'middle invariants',[hh,rr*abs(PP)//hh] if PP else [hh,0])
print('ALL POST-RELEASE KK COMPARISONS PASS; no additional independent-check credit.')
print('Completed UTC:',datetime.now(timezone.utc).isoformat())
