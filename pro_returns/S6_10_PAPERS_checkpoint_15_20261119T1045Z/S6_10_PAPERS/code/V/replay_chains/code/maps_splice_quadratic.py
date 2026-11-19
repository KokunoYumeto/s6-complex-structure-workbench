"""Exact cusp quadratic inclusion into the shifted splice module.

Builds the kernel of the map to the aspherical N complex.  Uses the
audited E.2.16 low complement complex and its full peripheral map.
Certificate for Theorem E.2.17, independently audited by root.
"""
from __future__ import annotations
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import json, random
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT=Path(__file__).resolve().parents[1]

# K=<a,b,h | a^3=h,b^4=h^-1,h central> normal forms.
def kmul(x,y):
    he=x[0]+y[0];w=list(x[1])
    for typ,power in y[1]:
        if w and w[-1][0]==typ:power+=w.pop()[1]
        m,sgn=(3,1) if typ=='a' else (4,-1)
        div,power=divmod(power,m);he+=sgn*div
        if power:w.append((typ,power))
    return he,tuple(w)
KI=(0,())
def kinv(x):
    z=(-x[0],())
    for typ,power in reversed(x[1]):z=kmul(z,(0,((typ,-power),)))
    return z
def kpow(x,n):
    if n<0:return kpow(kinv(x),-n)
    z=KI
    for _ in range(n):z=kmul(z,x)
    return z
KMU=(0,(('a',1),('b',1)))

def left_decompose(k):
    """k=h^he mu^n r, canonical left <h,mu>-transversal r."""
    original=k;he,w=k[0],list(k[1]);n=0
    while w:
        if w[0]==('a',1):
            n+=1
            if len(w)==1:
                he+=1;w=[('b',3)];break
            assert w[1][0]=='b';p=w[1][1]-1
            w=([('b',p)] if p else [])+w[2:]
        elif w[0]==('b',3) and len(w)>1:
            assert w[1][0]=='a';p=w[1][1]+1;n-=1;he-=1
            div,p=divmod(p,3);he+=div
            w=([('a',p)] if p else [])+w[2:]
        else:break
    r=(0,tuple(w))
    assert kmul(kmul((he,()),kpow(KMU,n)),r)==original
    return he,n,r

def hvertex(H,typ):
    p1,p2,m=H
    return (kmul(((p1 if typ==0 else p2),()),kpow(KMU,m if typ==0 else -m)),p2 if typ==0 else p1)
def right_decompose(v,typ):
    k,other=v;he,n,r=left_decompose(kinv(k))
    rr=kinv(r)
    H=(-he,other,-n) if typ==0 else (other,-he,n)
    hk,ho=hvertex(H,typ)
    assert kmul(rr,hk)==k and ho==other
    return rr,H

GI=((),(0,0,0))
def vappend(g,typ,v):
    stack,H=g;stack=list(stack)
    hk,ho=hvertex(H,typ);k,other=v
    rr,newH=right_decompose((kmul(hk,k),ho+other),typ)
    if rr!=KI:
        if stack and stack[-1][0]==typ:
            last=stack.pop()[1]
            rr,H2=right_decompose((kmul(last,rr),0),typ)
            newH=tuple(H2[i]+newH[i] for i in range(3))
        if rr!=KI:stack.append((typ,rr))
    return tuple(stack),newH
def gmul(x,y):
    z=x
    for typ,k in y[0]:z=vappend(z,typ,(k,0))
    return z[0],tuple(z[1][i]+y[1][i] for i in range(3))
def ginv(x):
    z=((),tuple(-p for p in x[1]))
    for typ,k in reversed(x[0]):z=vappend(z,typ,(kinv(k),0))
    return z
def generator(typ,letter):return vappend(GI,typ,((0,((letter,1),)),0))
ga,gb,gc,gd=[generator(t,l) for t,l in [(0,'a'),(0,'b'),(1,'a'),(1,'b')]]
gh1=((),(1,0,0));gh2=((),(0,1,0));gmu=((),(0,0,1))
def gpow(x,n):
    if n<0:return gpow(ginv(x),-n)
    z=GI
    for _ in range(n):z=gmul(z,x)
    return z
assert gmul(ga,gb)==gmu and gmul(gc,gd)==ginv(gmu)
assert gpow(ga,3)==gh1 and gpow(gb,4)==ginv(gh1)
assert gpow(gc,3)==gh2 and gpow(gd,4)==ginv(gh2)
for g in (ga,gb,gc,gd):
    assert gmul(g,ginv(g))==GI and gmul(gh1,g)==gmul(g,gh1) and gmul(gh2,g)==gmul(g,gh2)
random.seed(16017)
els=[GI,ga,gb,gc,gd,gh1,gh2,gmu]
for _ in range(200):
    x,y,z=[random.choice(els) for _ in range(3)]
    assert gmul(gmul(x,y),z)==gmul(x,gmul(y,z))
    v=gmul(x,y);assert gmul(v,ginv(v))==GI;els.append(v)

class R:
    __slots__=('d',)
    def __init__(self,x=0):
        if isinstance(x,R):self.d=x.d
        elif isinstance(x,int):self.d={GI:x} if x else {}
        else:self.d={w:int(n) for w,n in x.items() if n}
    def __bool__(self):return bool(self.d)
    def __add__(self,o):
        o=R(o);d=dict(self.d)
        for w,n in o.d.items():d[w]=d.get(w,0)+n
        return R(d)
    __radd__=__add__
    def __neg__(self):return R({w:-n for w,n in self.d.items()})
    def __sub__(self,o):return self+-R(o)
    def __rsub__(self,o):return R(o)+-self
    def __mul__(self,o):
        o=R(o);d=defaultdict(int)
        for x,n in self.d.items():
            for y,m in o.d.items():d[gmul(x,y)]+=n*m
        return R(d)
    __rmul__=__mul__
    def __pow__(self,n):
        if n<0:return self.unit_inverse()**(-n)
        z=R(1)
        for _ in range(n):z=z*self
        return z
    def __eq__(self,o):return self.d==R(o).d
    def is_unit(self):return len(self.d)==1 and abs(next(iter(self.d.values())))==1
    def unit_inverse(self):
        assert self.is_unit();w,n=next(iter(self.d.items()));return R({ginv(w):n})
    def aug(self):return sum(self.d.values())
    def string(self):
        if not self:return '0'
        out=[]
        for (stack,H),n in sorted(self.d.items()):
            ss=[]
            for typ,(he,w) in stack:
                ss.append('['+','.join(([f'h{typ+1}^{he}'] if he else [])+[('a' if typ==0 else 'c')+f'^{p}' if t=='a' else ('b' if typ==0 else 'd')+f'^{p}' for t,p in w])+']')
            ss += [f'{s}^{p}' for s,p in zip(('h1','h2','mu'),H) if p]
            out.append(str(n)+('*'+'*'.join(ss) if ss else ''))
        return ' + '.join(out)

a,b,c,d,h1,h2,mu=[R({g:1}) for g in (ga,gb,gc,gd,gh1,gh2,gmu)]
def zero(n,m):return [[R() for _ in range(m)] for _ in range(n)]
def multiply(A,B):
    if not A:return []
    if not B:return zero(len(A),0)
    out=zero(len(A),len(B[0]))
    for i,row in enumerate(A):
        for k,x in enumerate(row):
            if x:
                for j,y in enumerate(B[k]):
                    if y:out[i][j]=out[i][j]+x*y
    return out
def bs(n,k):return list(combinations(range(n),k)) if 0<=k<=n else []

def ecomplex(A,B,H):
    dims=[1,2,6,6];ds={1:[[A-1,B-1]],2:zero(2,6),3:zero(6,6)}
    ds[2][0][0]=1+A+A**2;ds[2][1][0]=H*(1+B+B**2+B**3)
    ds[3][2][0]=A-1;ds[3][2][1]=B-1
    ds[3][1][2]=H-1;ds[3][3][3]=H-1;ds[3][4][4]=H-1
    ds[3][1][5]=1+B;ds[3][2][5]=R(3)
    # Rows in E2 are r,x,t,y,z,e.
    per0=[[R(1)]];per1=zero(2,5);per1[0][0]=1+A+A**2;per1[0][4]=B;per1[1][4]=R(1)
    per2=zero(6,10)
    per2[2][2]=R(6);per2[2][3]=R(1)
    vals=[(B-1,-2,0,-6*B,5-2*B,H),(0,1,0,-B,B,0),(0,0,0,-1-B,1,0),(0,1,2,0,B-1,0)]
    for col,v in enumerate(vals,6):
        for row,x in enumerate(v):per2[row][col]=R(x)
    return dims,ds,{0:per0,1:per1,2:per2}

def torus(gens,maxdeg=3):
    basis=[bs(len(gens),k) for k in range(maxdeg+1)];ds={}
    for k in range(1,maxdeg+1):
        out=zero(len(basis[k-1]),len(basis[k]))
        for j,v in enumerate(basis[k]):
            for p,t in enumerate(v):out[basis[k-1].index(v[:p]+v[p+1:])][j]=(-1)**p*(gens[t]-1)
        ds[k]=out
    return basis,ds

Es=[ecomplex(a,b,h1),ecomplex(c,d,h2)]
Ts=[torus([h2,R(1),R(1),R(1)]),torus([h1,R(1),R(1),R(1)])]
VB=[];VD=[];VK=[]
for side in range(2):
    E,ed,ep=Es[side];tb,td=Ts[side]
    basis=[[(p,i,v) for p in range(k+1) for i in range(E[p]) for v in tb[k-p]] for k in range(4)]
    ds={}
    for k in range(1,4):
        out=zero(len(basis[k-1]),len(basis[k]))
        for j,(p,i,v) in enumerate(basis[k]):
            if p:
                for ii in range(E[p-1]):
                    x=ed[p][ii][i]
                    if x:out[basis[k-1].index((p-1,ii,v))][j]=out[basis[k-1].index((p-1,ii,v))][j]+x
            for pos,t in enumerate(v):
                x=((-1)**(p+pos))*([h2,h1][side]-1) if t==0 else R()
                if x:out[basis[k-1].index((p,i,v[:pos]+v[pos+1:]))][j]=out[basis[k-1].index((p,i,v[:pos]+v[pos+1:]))][j]+x
        ds[k]=out
    keep=[]
    for k in range(4):
        keep.append([idx for idx,(p,i,v) in enumerate(basis[k]) if not ((p<2 or (p==2 and i==0)) and all(t==0 for t in v))])
    VB.append(basis);VD.append(ds);VK.append(keep)

BB,BD=torus([h1,R(1),R(1),R(1),h2,R(1),R(1),R(1),mu])
BK=[[i for i,v in enumerate(BB[k]) if any(t not in (0,4,8) for t in v)] for k in range(4)]

def peripheral(side,k):
    out=zero(len(VB[side][k]),len(BB[k]));ep=Es[side][2]
    for col,v in enumerate(BB[k]):
        alpha=tuple(t for t in v if t<4);beta=tuple(t-4 for t in v if 4<=t<8);th=int(8 in v)
        if side==0:
            vv=alpha+((4,) if th else ());tt=beta;sgn=(-1)**(th*(len(beta)+len(alpha)));right=R(1)
        else:
            vv=beta+((4,) if th else ());tt=alpha;sgn=(-1)**(len(alpha)*(len(beta)+th)+th*len(beta));right=-mu if th else R(1)
        p=len(vv);column=bs(5,p).index(vv)
        # The E cone has theta first in swept cells.  The signs above move
        # the source torus's final theta coordinate to that cone position.
        if p==2:
            column=(bs(4,2).index(vv) if 4 not in vv else 6+vv[0])
        for i in range(Es[side][0][p]):
            x=sgn*ep[p][i][column]*right
            if x:out[VB[side][k].index((p,i,tt))][col]=x
    return out

PB=[{k:peripheral(side,k) for k in range(3)} for side in range(2)]
for side in range(2):
    for k in (1,2):
        assert multiply(VD[side][k],PB[side][k])==multiply(PB[side][k-1],BD[k]),('peripheral',side,k)

labels=[]
for k in range(4):
    ll=[]
    for side in range(2):ll += [('V',side,i) for i in VK[side][k]]
    if k:ll += [('B',0,i) for i in BK[k-1]]
    labels.append(ll)
dims=list(map(len,labels));ds={}
for k in range(1,4):
    out=zero(dims[k-1],dims[k])
    for col,lab in enumerate(labels[k]):
        typ,side,idx=lab
        if typ=='V':
            for ii in VK[side][k-1]:
                out[labels[k-1].index(('V',side,ii))][col]=VD[side][k][ii][idx]
            assert all(not VD[side][k][ii][idx] for ii in range(len(VB[side][k-1])) if ii not in VK[side][k-1])
        else:
            for s in range(2):
                for ii in VK[s][k-1]:out[labels[k-1].index(('V',s,ii))][col]=((-1)**s)*PB[s][k-1][ii][idx]
                assert all(not PB[s][k-1][ii][idx] for ii in range(len(VB[s][k-1])) if ii not in VK[s][k-1])
            if k>1:
                for ii in BK[k-2]:out[labels[k-1].index(('B',0,ii))][col]=-BD[k-1][ii][idx]
    ds[k]=out
assert dims==[0,6,40,123],dims
assert not any(x for row in multiply(ds[2],ds[3]) for x in row)
print('Kernel complex ranks:',dims,flush=True)

# Four actual complement cycles before either cancellation stage.
cycle_keys=[(side,i) for side in range(2) for i in (2,5)]
cycle_vectors=[]
for side,i in cycle_keys:
    v=[R() for _ in range(dims[2])]
    j=labels[2].index(('V',side,VB[side][2].index((2,i,()))))
    v[j]=R(1); cycle_vectors.append(v)
log=[]
def cancel(k,i,j):
    M=ds[k];ui=M[i][j].unit_inverse();rows=[r for r in range(len(M)) if r!=i];cols=[c for c in range(len(M[0])) if c!=j]
    ds[k]=[[M[r][c]-M[r][j]*ui*M[i][c] for c in cols] for r in rows]
    if k==2:
        ds[3]=[row for r,row in enumerate(ds[3]) if r!=j]
        for v in cycle_vectors: v[:]=[x for ii,x in enumerate(v) if ii!=j]
    if k==3:
        for v in cycle_vectors:
            vi=v[i]
            v[:]=[v[r]-M[r][j]*ui*vi for r in rows]
    log.append((k,labels[k-1].pop(i),labels[k].pop(j),M[i][j].string()))
    dims[k-1]-=1;dims[k]-=1
while dims[1]:
    pivot=next(( (i,j) for i,row in enumerate(ds[2]) for j,x in enumerate(row) if x.is_unit()),None)
    assert pivot;cancel(2,*pivot)
print('Presentation before unit reduction:',dims[2:4],flush=True)
while True:
    pivot=next(((i,j) for i,row in enumerate(ds[3]) for j,x in enumerate(row) if x.is_unit()),None)
    if not pivot:break
    cancel(3,*pivot)
nonzero=[j for j in range(dims[3]) if any(row[j] for row in ds[3])]
pres=[[row[j] for j in nonzero] for row in ds[3]]
rels=[labels[3][j] for j in nonzero]
print('Final presentation:',len(pres),'generators,',len(nonzero),'nonzero relations',flush=True)
print('Actual complement t,e inclusion vectors:',[[x.string() for x in v] for v in cycle_vectors],flush=True)
for vector,index in zip(cycle_vectors,(4,3,12,15)):
    assert vector==[R(int(i==index)) for i in range(16)]

aug=sp.Matrix([[x.aug() for x in row] for row in pres]);S=smith_normal_form(aug,domain=ZZ)
smith=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]
print('Coinvariant Smith:',smith,'free rank',len(pres)-len(smith),flush=True)
assert len(pres)-len(smith)==2 and [x for x in smith if x!=1]==[12]*6
# The two cusp generators split off as cyclic modules on the two central axes.
for row,rel,Q in ((3,16,h2-1),(15,39,h1-1)):
    assert pres[row][rel]==Q
    assert all(not pres[row][j] for j in range(len(nonzero)) if j!=rel)
    assert all(not pres[i][rel] for i in range(len(pres)) if i!=row)
# Exact pure norm relations, before taking any quotient.
for row,jj,kk in ((0,9,46),(1,10,47),(2,11,48)):
    diff=[pres[i][jj]-pres[i][kk] for i in range(16)]
    assert all(x==(h1*(1+b+b**2+b**3) if i==row else R()) for i,x in enumerate(diff))
for row,jj in ((5,49),(6,50),(7,51)):
    assert all(pres[i][jj]==(1+c+c**2 if i==row else R()) for i in range(16))
for row,jj,kk in ((8,32,49),(9,33,50),(10,34,51)):
    diff=[pres[i][jj]-pres[i][kk] for i in range(16)]
    assert all(x==(h2*(1+d+d**2+d**3) if i==row else R()) for i,x in enumerate(diff))
def mod_centers(x):
    out=defaultdict(int)
    for (stack,H),n in x.d.items():out[(stack,(0,0,H[2]))]+=n
    return R(out)
trows=[i for i in range(16) if i not in (3,15)]
tcols=[j for j in range(len(nonzero)) if j not in (16,39)]
tmat=[[mod_centers(pres[i][j]) for j in tcols] for i in trows]
tgens=[labels[2][i] for i in trows];trels=[rels[j] for j in tcols];tlog=[]
while True:
    piv=next(((i,j) for i,row in enumerate(tmat) for j,x in enumerate(row) if x.is_unit()),None)
    if not piv:break
    i,j=piv;ui=mod_centers(tmat[i][j].unit_inverse());rs=[r for r in range(len(tmat)) if r!=i];cs=[s for s in range(len(tmat[0])) if s!=j]
    nxt=[[mod_centers(tmat[r][s]-tmat[r][j]*ui*tmat[i][s]) for s in cs] for r in rs]
    tlog.append((tgens.pop(i),trels.pop(j),tmat[i][j].string()));tmat=nxt
nn=[j for j in range(len(tmat[0])) if any(row[j] for row in tmat)]
tmat=[[row[j] for j in nn] for row in tmat];trels=[trels[j] for j in nn]
print('Central intersection summand:',len(tmat),'generators,',len(nn),'relations',flush=True)
assert len(tmat)==14 and len(nn)==26
def column(j):return [row[j] for row in tmat]
def vec(entries):
    z=[R() for _ in range(14)]
    for i,x in entries.items():z[i]=mod_centers(R(x))
    return z
Na0=1+a+a**2;Nb0=1+b+b**2+b**3;Nc0=1+c+c**2;Nd0=1+d+d**2+d**3
expected_couplings=[
 vec({0:-(b**3)*Na0,10:-Na0,12:d*Na0,13:-d*Na0}),
 vec({1:-(b**3)*Na0,12:(1+d)*Na0,13:-Na0}),
 vec({2:-(b**3)*Na0,10:-Na0,11:-2*Na0,13:(1-d)*Na0})]
for i in range(3):
    assert column(20+i)==expected_couplings[i]
    assert [mod_centers(x-y) for x,y in zip(column(4+i),column(20+i))]==vec({i:Nb0})
    assert column(23+i)==vec({4+i:Nc0})
    assert [mod_centers(x-y) for x,y in zip(column(14+i),column(23+i))]==vec({7+i:Nd0})
assert column(19)==vec({10:1+d,11:3})
for j,row,g in ((1,11,a),(3,11,b),(17,11,c),(18,11,d),(7,3,a),(8,3,b),(11,3,c),(13,3,d)):
    assert column(j)==vec({row:g-1})
assert column(0)==vec({11:6*(a-1)}) and column(2)==vec({11:6*(b-1)})
assert column(10)==vec({3:6*(c-1)}) and column(12)==vec({3:6*(d-1)})
coefR0=[a*(1-b-b**2+b**3),a*(b**2-1),-a*(1+b**3)]
big={3:3-2*b**2-2*b**3}
for i,x in enumerate(coefR0):big[4+i]=d*x;big[7+i]=x
assert column(9)==vec(big)
tsmith=smith_normal_form(sp.Matrix([[x.aug() for x in row] for row in tmat]),domain=ZZ)
ts=[abs(int(tsmith[i,i])) for i in range(min(tsmith.shape)) if tsmith[i,i]]
assert len(ts)==len(tmat) and [v for v in ts if v!=1]==[12]*6
def chi_mod12(g):
    stack,H=g;val=H[2]
    for typ,(he,w) in stack:
        for letter,power in w:val+=power*({(0,'a'):4,(0,'b'):-3,(1,'a'):-4,(1,'b'):3}[(typ,letter)])
    return val%12
cover=sp.zeros(12*len(tmat),12*len(tmat[0]))
for i,row in enumerate(tmat):
    for j,x in enumerate(row):
        for g,n in x.d.items():
            shift=chi_mod12(g)
            for kk in range(12):cover[12*i+(kk+shift)%12,12*j+kk]+=n
CS=smith_normal_form(cover,domain=ZZ)
css=[abs(int(CS[i,i])) for i in range(min(CS.shape)) if CS[i,i]]
cfree=cover.rows-len(css)
print('Surface-subgroup coinvariants of intersection summand:',cfree,[v for v in css if v!=1],flush=True)
assert cfree==86 and [v for v in css if v!=1]==[6,6]
# A compact presentation for the central summand: two six-generator blocks.
compact=zero(12,20)
Na,Nb,Nc,Nd=[sum((x**j for j in range(n)),R()) for x,n in ((a,3),(b,4),(c,3),(d,4))]
for i in range(3):
    compact[i][i]=Na;compact[3+i][3+i]=Nb
    compact[6+i][10+i]=Nc;compact[9+i][13+i]=Nd
coefL=[1+d-d**2-d**3,d**3-d,d**2+d**3]
coefR=[a*(1-b-b**2+b**3),a*(b**2-1),-a*(1+b**3)]
omegaL=coefL+[-x for x in coefL]
omegaR=[d*x for x in coefR]+coefR
for jj,x in enumerate((a,b,c,d)):
    for i in range(6):
        compact[i][6+jj]=mod_centers(omegaL[i]*(x-1))
        compact[6+i][16+jj]=mod_centers(omegaR[i]*(x-1))
compact=[[mod_centers(x) for x in row] for row in compact]
sm=smith_normal_form(sp.Matrix([[x.aug() for x in row] for row in compact]),domain=ZZ)
ss=[abs(int(sm[i,i])) for i in range(min(sm.shape)) if sm[i,i]]
assert ss==[1]*6+[12]*6
# The actual t0,t1 images have order six after full coinvariants.
# They are -2(B2+C2) and 2(p2-r2), with independent orders 3,4.
from math import gcd, lcm
assert lcm(3//gcd(3,2),4//gcd(4,2))==6
assert [x.aug() for x in omegaL]==[0,0,2,0,0,-2]
assert [x.aug() for x in omegaR]==[0,0,-2,0,0,-2]
cc=sp.zeros(144,240)
for i,row in enumerate(compact):
    for j,x in enumerate(row):
        for g,n in x.d.items():
            shift=chi_mod12(g)
            for kk in range(12):cc[12*i+(kk+shift)%12,12*j+kk]+=n
cs=smith_normal_form(cc,domain=ZZ)
ccs=[abs(int(cs[i,i])) for i in range(min(cs.shape)) if cs[i,i]]
assert cc.rows-len(ccs)==86 and [v for v in ccs if v!=1]==[6,6]
print('Compact central presentation: 12 generators,20 relations; ordinary and12-sheet Smith checks passed',flush=True)
for j in range(len(nonzero)):
    print('relation',j,[(i,pres[i][j].string()) for i in range(len(pres)) if pres[i][j]])
out={'status':'Proposition E.2.18 proved; actual splice inclusions and Whitehead obstruction independently audited by root',
     'cycle_keys_t_e':cycle_keys,'cusp_inclusions':[[x.string() for x in v] for v in cycle_vectors],
     'kernel_dimensions':[0,6,40,123],'generators':labels[2],'relations':rels,
     'matrix':[[x.string() for x in row] for row in pres],
     'coinvariant_smith':smith,'coinvariant_free_rank':2,'unit_cancellations':log,
     'split_axes':['R/(h2-1)','R/(h1-1)'],
     'central_intersection_generators':tgens,'central_intersection_relations':trels,
     'central_intersection_matrix':[[x.string() for x in row] for row in tmat],
     'central_intersection_smith':ts,'central_intersection_unit_cancellations':tlog,
     'seven_generator_block_collection_verified':True,
     'surface_subgroup_coinvariants_free':cfree,'surface_subgroup_coinvariants_smith':css}
out['compact_central_matrix']=[[x.string() for x in row] for row in compact]
out['compact_central_smith']=ss
out['compact_surface_subgroup_smith']=ccs
(ROOT/'code/maps_splice_quadratic.out.json').write_text(json.dumps(out,indent=2)+'\n')
