"""Exact low-degree group-ring model for the regular-fibre complement.

Certificate for Theorem E.2.16, independently audited by root.  The normalized
cusp boundary chain map is proved in sections/maps_complement_module.tex.
All computations are over Z[<a,b,h | h central,a^3=h,b^4=h^-1>].
"""
from __future__ import annotations
from collections import defaultdict
from itertools import combinations, permutations
from pathlib import Path
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT=Path(__file__).resolve().parent

def word_mul(x,y):
    he=x[0]+y[0]; w=list(x[1])
    for typ,power in y[1]:
        if w and w[-1][0]==typ:
            power+=w.pop()[1]
        m,sgn=(3,1) if typ=='a' else (4,-1)
        div,power=divmod(power,m); he+=sgn*div
        if power: w.append((typ,power))
    return he,tuple(w)

def word_inv(x):
    ans=(-x[0],())
    for typ,power in reversed(x[1]): ans=word_mul(ans,(0,((typ,-power),)))
    return ans

ONEWORD=(0,())
class R:
    __slots__=('d',)
    def __init__(self,x=0):
        if isinstance(x,R): self.d=x.d
        elif isinstance(x,int): self.d={ONEWORD:x} if x else {}
        else: self.d={w:int(n) for w,n in x.items() if n}
    def __bool__(self): return bool(self.d)
    def __add__(self,o):
        o=R(o); d=dict(self.d)
        for w,n in o.d.items(): d[w]=d.get(w,0)+n
        return R(d)
    __radd__=__add__
    def __neg__(self): return R({w:-n for w,n in self.d.items()})
    def __sub__(self,o): return self+-R(o)
    def __rsub__(self,o): return R(o)+-self
    def __mul__(self,o):
        o=R(o); d=defaultdict(int)
        for x,n in self.d.items():
            for y,m in o.d.items(): d[word_mul(x,y)]+=n*m
        return R(d)
    __rmul__=__mul__
    def __pow__(self,n):
        if n<0: return self.unit_inverse()**(-n)
        ans=R(1); base=self
        while n:
            if n&1: ans=ans*base
            base=base*base; n//=2
        return ans
    def __eq__(self,o): return self.d==R(o).d
    def unit_inverse(self):
        assert len(self.d)==1
        w,n=next(iter(self.d.items())); assert abs(n)==1
        return R({word_inv(w):n})
    def is_unit(self): return len(self.d)==1 and abs(next(iter(self.d.values())))==1
    def augmentation(self): return sum(self.d.values())
    def mod_h_minus_one(self):
        d=defaultdict(int)
        for (he,w),n in self.d.items():d[(0,w)]+=n
        return R(d)
    def string(self):
        if not self: return '0'
        out=[]
        for (he,w),n in sorted(self.d.items()):
            mon=([f'h^{he}'] if he else [])+[f'{t}^{p}' for t,p in w]
            out.append(str(n)+('*'+'*'.join(mon) if mon else ''))
        return ' + '.join(out)
    def divide_h_minus_one(self):
        grouped=defaultdict(dict)
        for (he,w),n in self.d.items(): grouped[w][he]=n
        result={}
        for w,p in grouped.items():
            assert sum(p.values())==0,(w,p)
            lo,hi=min(p),max(p); prev=0
            for k in range(lo,hi):
                coeff=prev-p.get(k,0)
                if coeff: result[(k,w)]=coeff
                prev=coeff
            assert prev==p.get(hi,0)
        ans=R(result); assert (h-1)*ans==self
        return ans

h=R({(1,()):1}); a=R({(0,(('a',1),)):1}); b=R({(0,(('b',1),)):1})
q=h-1
assert a**3==h and b**4==h**-1 and a*b!=b*a

def bases(n,k): return list(combinations(range(n),k)) if 0<=k<=n else []
def sign_perm(p): return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def zero(n,m): return [[R() for _ in range(m)] for _ in range(n)]
def eye(n): return [[R(int(i==j)) for j in range(n)] for i in range(n)]
def multiply(A,B):
    assert not A or not B or len(A[0])==len(B)
    if not A:return []
    if not B:return zero(len(A),0)
    ans=zero(len(A),len(B[0]))
    for i,row in enumerate(A):
        for k,x in enumerate(row):
            if x:
                for j,y in enumerate(B[k]):
                    if y:ans[i][j]=ans[i][j]+x*y
    return ans
def wedge(A,k):
    n=len(A); bs=bases(n,k); ans=zero(len(bs),len(bs))
    for i,rows in enumerate(bs):
        for j,cols in enumerate(bs):
            for p in permutations(range(k)):
                term=R(sign_perm(p))
                for r in range(k):term=term*A[rows[r]][cols[p[r]]]
                ans[i][j]=ans[i][j]+term
    return ans
def add_block(M,A,row,col,sgn=1):
    for i,rr in enumerate(A):
        for j,x in enumerate(rr):M[row+i][col+j]=M[row+i][col+j]+sgn*x
def mat_pow(A,n):
    assert n>=0; ans=eye(len(A))
    for _ in range(n):ans=multiply(ans,A)
    return ans
def scalar_matrix(x,A):return [[x*y for y in row] for row in A]

A1=sp.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=sp.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
M0=(A1*A2).inv()

def lifted(A):
    return [[R(int(A[i,j]))*(h if j==0 and i>0 else 1) for j in range(4)] for i in range(4)]

Fdim=[len(bases(4,k)) for k in range(5)]
def d_f(k):
    src=bases(4,k); dst=bases(4,k-1); ans=zero(len(dst),len(src))
    for j,v in enumerate(src):
        if v and v[0]==0:ans[dst.index(v[1:])][j]=q
    return ans

def boundary(A,x):
    dims=[len(bases(4,k))+len(bases(4,k-1)) for k in range(6)]
    d={}; FA=lifted(A)
    for k in range(1,4):
        ans=zero(dims[k-1],dims[k]); add_block(ans,d_f(k),0,0)
        B=wedge(FA,k-1)
        for i in range(len(B)):
            for j in range(len(B)):B[i][j]=(x if i==j else R())-B[i][j]
        add_block(ans,B,0,len(bases(4,k)))
        add_block(ans,d_f(k-1),len(bases(4,k-1)),len(bases(4,k)),-1)
        d[k]=ans
    return dims,d

def finite_cap(A,x,m,n,v):
    D=sp.Matrix(A[1:,1:]); assert D**m==sp.eye(3)
    capdims=[len(bases(3,k))+len(bases(3,k-1)) for k in range(5)]
    d={}; imap={}
    for k in range(1,4):
        ans=zero(capdims[k-1],capdims[k]); Dk=wedge([[R(int(z)) for z in row] for row in D.tolist()],k-1)
        B=[[((x if i==j else R())-Dk[i][j]) for j in range(len(Dk))] for i in range(len(Dk))]
        add_block(ans,B,0,len(bases(3,k)));d[k]=ans
    # The adapted first fibre vector is n*v and has gamma coordinate one.
    P=sp.eye(4); P[:,0]=n*sp.Matrix(v); assert P.det()==1
    assert P.inv()*A*P==sp.diag(1,D)
    invP=lifted(P.inv())
    for k in range(3):
        fbs=bases(4,k); ebs=bases(4,k-1)
        out=zero(capdims[k],len(fbs)+len(ebs))
        # Standard boundary-to-cap map in adapted coordinates.
        std=zero(capdims[k],len(fbs)+len(ebs))
        for col,vv in enumerate(fbs):
            if 0 not in vv:
                ww=tuple(t-1 for t in vv);std[bases(3,k).index(ww)][col]=R(1)
            else:
                ww=tuple(t-1 for t in vv[1:]); level=k-1; Dk=wedge([[R(int(z)) for z in row] for row in D.tolist()],level)
                N=zero(len(Dk),len(Dk))
                if n==1:
                    for j in range(m):add_block(N,scalar_matrix(x**j,mat_pow(Dk,m-1-j)),0,0)
                else:
                    # (x-D) * [-x^-m sum_(j=0)^(m-1) x^j D^(m-1-j)] = x^-m-1.
                    for j in range(m):add_block(N,scalar_matrix(-(x**(j-m)),mat_pow(Dk,m-1-j)),0,0)
                jj=bases(3,level).index(ww)
                for row in range(len(Dk)):std[len(bases(3,k))+row][col]=N[row][jj]
        for j,vv in enumerate(ebs):
            if 0 not in vv:
                ww=tuple(t-1 for t in vv);std[len(bases(3,k))+bases(3,k-1).index(ww)][len(fbs)+j]=R(1)
        change=zero(len(fbs)+len(ebs),len(fbs)+len(ebs))
        add_block(change,wedge(invP,k),0,0)
        add_block(change,wedge(invP,k-1),len(fbs),len(fbs)) if k else None
        imap[k]=multiply(std,change)
    return capdims,d,imap

def cusp_cap():
    dims=[1,2,4,2,1]
    d={1:[[q,R()]],2:[[R()]*4,[q,R(),R(),R()]],3:zero(4,2)}
    d[3][2][0]=q;d[3][3][1]=q
    i={0:[[R(1)]],1:zero(2,5),2:zero(4,10)}
    i[1][0][0]=R(1);i[1][1][1]=R(1)
    # Rows: gu, E, U, D. Columns: gu,gw,gd,uw,ud,wd,g theta,u theta,w theta,d theta.
    i[2][0][0]=R(1);i[2][1][2]=R(1);i[2][2][3]=R(1)
    i[2][3][1]=-h;i[2][3][4]=R(1)
    return dims,d,i

boundaries=[boundary(A1,a),boundary(A2,b),boundary(M0,R(1))]
caps=[finite_cap(A1,a,3,1,[1,2,-4,0]),finite_cap(A2,b,4,-1,[-1,-3,3,0]),cusp_cap()]
for j in range(3):
    for k in (1,2):
        assert multiply(caps[j][1][k],caps[j][2][k])==multiply(caps[j][2][k-1],boundaries[j][1][k]),('cap chain map',j,k)

udims=[len(bases(4,k))+3*len(bases(4,k-1)) for k in range(6)]
ud={}
for k in range(1,4):
    out=zero(udims[k-1],udims[k]);add_block(out,d_f(k),0,0)
    for j,(A,x) in enumerate([(A1,a),(A2,b),(M0,R(1))]):
        Bj=boundaries[j][1][k]; fprev=len(bases(4,k-1));fcur=len(bases(4,k))
        add_block(out,[row[fcur:] for row in Bj[:fprev]],0,fcur+j*fprev)
        add_block(out,[row[fcur:] for row in Bj[fprev:]],fprev+j*len(bases(4,k-2)),fcur+j*fprev)
    ud[k]=out

def inclusion(j,k):
    ans=zero(udims[k],boundaries[j][0][k]);nf=len(bases(4,k));np=len(bases(4,k-1))
    add_block(ans,eye(nf),0,0);add_block(ans,eye(np),nf+j*np,nf)
    return ans

dims=[]; labels=[]
for k in range(4):
    labels.append([f'U{k}:{i}' for i in range(udims[k])])
    for j in range(3):labels[-1]+=[f'C{j}.{k}:{i}' for i in range(caps[j][0][k])]
    if k:
        for j in range(3):labels[-1]+=[f'B{j}.{k-1}:{i}' for i in range(boundaries[j][0][k-1])]
    dims.append(len(labels[-1]))
ds={}
for k in range(1,4):
    out=zero(dims[k-1],dims[k]);add_block(out,ud[k],0,0)
    row=udims[k-1];col=udims[k]
    for j in range(3):
        add_block(out,caps[j][1][k],row,col);row+=caps[j][0][k-1];col+=caps[j][0][k]
    shiftrow=row
    for j in range(3):
        add_block(out,inclusion(j,k-1),0,col)
        caprow=udims[k-1]+sum(caps[t][0][k-1] for t in range(j))
        add_block(out,caps[j][2][k-1],caprow,col,-1)
        if k>1:
            add_block(out,boundaries[j][1][k-1],shiftrow,col,-1)
            shiftrow+=boundaries[j][0][k-2]
        col+=boundaries[j][0][k-1]
    ds[k]=out

def check_chain():
    for k in (2,3):
        prod=multiply(ds[k-1],ds[k]); assert not any(x for row in prod for x in row),('chain',k)
check_chain()
aug=[sp.Matrix([[x.augmentation() for x in row] for row in ds[k]]) for k in (1,2,3)]
aug_ranks=[x.rank() for x in aug]
print('Initial cell dimensions:',dims)
print('Augmentation ranks d1,d2,d3:',aug_ranks)
print('Augmentation Betti0,1,2:',[dims[0]-aug_ranks[0],dims[1]-sum(aug_ranks[:2]),dims[2]-sum(aug_ranks[1:])])
assert [dims[0]-aug_ranks[0],dims[1]-sum(aug_ranks[:2]),dims[2]-sum(aug_ranks[1:])]==[1,1,4]

cancel_log=[]
boundary_cycles=[]
for vv in [(1,2),(1,3),(2,3)]:
    vec=[R() for _ in range(dims[2])]
    vec[bases(4,2).index(vv)]=R(1)
    boundary_cycles.append(vec)
# Extra geometric cycles from the normalized cusp.  This instrumentation
# uses the identical cancellation sequence of maps_complement_module.py.
cusp_cycles=[]
for cusp_label in ('C2.2:1','C2.2:2','C2.2:3'):
    vec=[R() for _ in range(dims[2])]
    vec[labels[2].index(cusp_label)]=R(1)
    cusp_cycles.append(vec)
peripheral_columns=[]
peripheral_one_columns=[]
for jj in range(4):
    vec=[R() for _ in range(dims[1])];vec[jj]=R(1);peripheral_one_columns.append(vec)
vec=[R() for _ in range(dims[1])]
vec[4]=b;vec[5]=R(1);vec[6]=R(1);peripheral_one_columns.append(vec)
for jj in range(6):
    vec=[R() for _ in range(dims[2])];vec[jj]=R(1);peripheral_columns.append(vec)
edge_blocks=[scalar_matrix(b,eye(4)),lifted(A1),multiply(lifted(A1),lifted(A2))]
for jj in range(4):
    vec=[R() for _ in range(dims[2])]
    for edge,B in enumerate(edge_blocks):
        for ii in range(4):vec[6+4*edge+ii]=B[ii][jj]
    peripheral_columns.append(vec)
def cancel(k,i,j):
    M=ds[k];u=M[i][j];ui=u.unit_inverse()
    rows=[r for r in range(len(M)) if r!=i];cols=[c for c in range(len(M[0])) if c!=j]
    ds[k]=[[M[r][c]-M[r][j]*ui*M[i][c] for c in cols] for r in rows]
    if k>1:ds[k-1]=[[x for t,x in enumerate(row) if t!=i] for row in ds[k-1]]
    if k<3:ds[k+1]=[row for t,row in enumerate(ds[k+1]) if t!=j]
    if k==2:
        for v in boundary_cycles+cusp_cycles:v.pop(j)
        for v in peripheral_columns:v.pop(j)
        for v in peripheral_one_columns:
            vi=v[i];v[:]=[v[r]-M[r][j]*ui*vi for r in rows]
    if k==1:
        for v in peripheral_one_columns:v.pop(j)
    cancel_log.append((k,labels[k-1][i],labels[k][j],u.string()))
    labels[k-1].pop(i);labels[k].pop(j);dims[k-1]-=1;dims[k]-=1

while True:
    found=None
    for k in (1,2):
        for i,row in enumerate(ds[k]):
            for j,x in enumerate(row):
                if x.is_unit():found=(k,i,j);break
            if found:break
        if found:break
    if not found:break
    cancel(*found)
check_chain()
print('After degree0/1 cancellations:',dims)
print('Remaining degree1 labels:',labels[1])
print('d1:',[[x.string() for x in row] for row in ds[1]])
print('Nonzero d2 columns:',[(j,[ds[2][i][j].string() for i in range(dims[1])]) for j in range(dims[2]) if any(ds[2][i][j] for i in range(dims[1]))])

# The standard aspherical one-relator presentation has Fox column
# (1+a+a^2, h(1+b+b^2+b^3))^t.  Every column factors through it.
assert dims[0]==1 and dims[1]==2 and ds[1]==[[a-1,b-1]]
fox=[R(1)+a+a**2,h*(R(1)+b+b**2+b**3)]
factors=[]
for j in range(dims[2]):
    factor=((a-1)*ds[2][0][j]).divide_h_minus_one() if ds[2][0][j] else R()
    assert all(ds[2][i][j]==fox[i]*factor for i in range(2))
    factors.append(factor)
p=next(j for j,x in enumerate(factors) if x==1)
for col in range(dims[3]):
    assert sum((factors[j]*ds[3][j][col] for j in range(dims[2])),R())==0
pres=[row for j,row in enumerate(ds[3]) if j!=p]
peripheral_fox_columns=[sum((factors[j]*v[j] for j in range(len(v))),R()) for v in peripheral_columns]
for v in boundary_cycles+cusp_cycles:
    assert sum((factors[j]*v[j] for j in range(len(v))),R())==0
    v.pop(p)
for v in peripheral_columns:v.pop(p)
genlabels=[s for j,s in enumerate(labels[2]) if j!=p]
rellabels=labels[3][:]
pcancel=[]
while True:
    piv=None
    for i,row in enumerate(pres):
        for j,x in enumerate(row):
            if x.is_unit():piv=(i,j);break
        if piv:break
    if not piv:break
    i,j=piv; ui=pres[i][j].unit_inverse()
    rows=[r for r in range(len(pres)) if r!=i]
    cols=[c for c in range(len(pres[0])) if c!=j]
    new=[[pres[r][c]-pres[r][j]*ui*pres[i][c] for c in cols] for r in rows]
    for v in boundary_cycles+cusp_cycles:
        vi=v[i]
        nv=[v[r]-pres[r][j]*ui*vi for r in rows]
        v[:]=nv
    for v in peripheral_columns:
        vi=v[i]
        v[:]=[v[r]-pres[r][j]*ui*vi for r in rows]
    pcancel.append((genlabels.pop(i),rellabels.pop(j),pres[i][j].string()))
    pres=new
# Delete identically zero relations; these are degree-three homology inputs,
# not relations of pi2.
nonzero=[j for j in range(len(pres[0])) if any(row[j] for row in pres)]
pres=[[row[j] for j in nonzero] for row in pres]
rellabels=[rellabels[j] for j in nonzero]
print('Presentation size after unit reductions:',len(pres),'generators,',len(pres[0]),'relations')
print('Generator labels:',genlabels)
print('Peripheral H2 images (uw,ud,wd):',[[x.string() for x in v] for v in boundary_cycles])
print('Cusp E,U,D images:', [[x.string() for x in v] for v in cusp_cycles])
print('Peripheral degree2 coefficients in the free cusp generator:',[v[4].string() for v in peripheral_columns])
print('Peripheral degree1 columns:',[[x.string() for x in v] for v in peripheral_one_columns])
print('Peripheral degree2 Fox coefficients:',[x.string() for x in peripheral_fox_columns])
expected_peripheral=[
 [R(),R(),R(),R(),R()], [R(),R(),R(),R(),R()],
 [R(),R(6),R(),R(),R()], [R(),R(1),R(),R(),R()],
 [R(),R(),R(),R(),R()], [R(),R(),R(),R(),R()],
 [R(-2),R(),-6*b,5-2*b,h],
 [R(1),R(),-b,b,R()], [R(),R(),-1-b,R(1),R()],
 [R(1),R(2),R(),b-1,R()]]
for got,want in zip(peripheral_columns,expected_peripheral):
    norm=[got[0].mod_h_minus_one(),R(got[1].augmentation()),got[2].mod_h_minus_one(),got[3].mod_h_minus_one(),got[4]]
    assert norm==want
for j in range(len(pres[0])):
    print('relation',j,[(i,pres[i][j].string()) for i in range(len(pres)) if pres[i][j]])
augpres=sp.Matrix([[x.augmentation() for x in row] for row in pres])
S=smith_normal_form(augpres,domain=ZZ)
smith=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]
assert all(x==1 for x in smith) and len(pres)-len(smith)==4
assert genlabels==['C1.2:5','C2.2:2','B1.1:2','B1.1:3','B2.1:3']
assert all(not row[4] for row in zip(*pres))
# Exact triangular reduction to the six displayed relations.
assert [pres[1][j] for j in (0,12,8)]==[q,1-a**-1,b-a**-1]
assert (pres[1][12]*a)==a-1 and pres[1][8]-pres[1][12]==b-1
active={5,6,7,17,18,19}
for j in range(len(pres[0])):
    if j not in active:
        assert all(not pres[i][j] for i in (0,2,3,4))
        assert pres[1][j].augmentation()==0
assert [pres[1][j].augmentation() for j in (5,6,7,17,18,19)]==[0,0,0,3,3,6]
assert pres[2][5]==q and pres[3][6]==q and pres[0][7]==-q
assert pres[2][6]==-q*b and pres[3][7]==-q*(b-1)
assert [pres[0][j] for j in (17,18,19)]==[h*(1+b),h*(b+b**2),h*(1+b+b**2+b**3)]
assert pres[2][18]==-q and pres[3][19]==-q

# Retain the geometric normalization cycles, rather than infer their
# images from the peripheral map after taking ordinary coinvariants.
expected_cusp = [
    [R(), R(6), R(), R(), 1-h],
    [R(), R(1), R(), R(), R()],
    [R(), R(), R(), R(), R()],
]
for got, want in zip(cusp_cycles, expected_cusp):
    norm = [got[0].mod_h_minus_one(), R(got[1].augmentation()),
            got[2].mod_h_minus_one(), got[3].mod_h_minus_one(), got[4]]
    assert norm == want

# Whitehead's universal quadratic group on a free abelian basis is the
# degree-two polynomial group, with q(v) represented by v**2 and the
# cross effect represented by 2*v*w.  Checking the free universal case
# verifies the identity before passage to any module relations.
qsE, qsU, qsD, qse, qst, qsh = sp.symbols('E U D e t h')
qH, qE1, qE2, qE3 = -qsE+qsU-qsD, -qsE-qsD, qsD, qsU-qsD
qpicard = sp.expand(qH**2-qE1**2-qE2**2-qE3**2)
assert qpicard == -2*qsE*qsU-2*qsD**2
qglobal = sp.expand(qpicard.subs({qsE:(1-qsh)*qse+6*qst,
                                  qsU:qst, qsD:0}))
assert sp.expand(qglobal-2*qse*qst*(qsh-1)+12*qst**2) == 0
print('Quadratic identity:', qglobal)

result={'status':'Exact arithmetic replay passed; full geometric proof review is recorded separately in records/III_events.tsv',
        'cusp_E_U_D_normal_form':[[x.string() for x in v] for v in expected_cusp],
        'quadratic_identity':str(qglobal),
        'cusp_E_U_D_images':[[x.string() for x in v] for v in cusp_cycles], 'initial_dimensions':[4,20,49,62], 'augmentation_betti012':[1,1,4],
        'reduced_dimensions':dims,'labels':labels,
        'd1':[[x.string() for x in row] for row in ds[1]],
        'd2':[[x.string() for x in row] for row in ds[2]],
        'd3':[[x.string() for x in row] for row in ds[3]],
        'cancellations':cancel_log,
        'fox_factors':[x.string() for x in factors],
        'presentation_generators':genlabels,'presentation_relations':rellabels,
        'presentation':[[x.string() for x in row] for row in pres],
        'presentation_cancellations':pcancel,
        'peripheral_H2_images':[[x.string() for x in v] for v in boundary_cycles],
        'peripheral_degree2_columns':[[x.string() for x in v] for v in peripheral_columns],
        'peripheral_degree2_normal_form':[[x.string() for x in v] for v in expected_peripheral],
        'peripheral_degree1_columns':[[x.string() for x in v] for v in peripheral_one_columns],
        'peripheral_degree2_fox_coefficients':[x.string() for x in peripheral_fox_columns],
        'normal_form':'R + (Z[C3*C4])^2 + <x,t | t(a-1),t(b-1),x(1+b)+3t>',
        'augmentation_smith':smith}
(ROOT/'maps_cusp_quadratic.out.json').write_text(json.dumps(result,indent=2)+'\n')
