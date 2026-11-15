"""Independent rational construction of A5^4 D4, its neighbours and J.

Coordinates in four copies of the sum-zero subspace of Q^6 and in Q^4.
All stored ambient coordinates are multiplied by 12.  HNF, Gram matrices,
duals, intersections and discriminant calculations are exact.
The auxiliary enumerator uses integer fraction-free Gram--Schmidt.
"""
from fractions import Fraction as F
from itertools import product, combinations
from pathlib import Path
import json, subprocess, time
from flint import fmpz_mat, fmpq_mat

ROOT = Path(__file__).resolve().parents[1]
REC = ROOT / "records"
S = 12

def add(*vv): return tuple(sum(x) for x in zip(*vv))
def mul(a,v): return tuple(a*x for x in v)
def dot(a,b): return F(sum(x*y for x,y in zip(a,b)),S*S)
def basis(vv):
    h=fmpz_mat([list(v) for v in vv]).hnf()
    return [tuple(int(h[i,j]) for j in range(h.ncols())) for i in range(h.nrows()) if any(h[i,j] for j in range(h.ncols()))]
def gram(bb): return [[dot(a,b) for b in bb] for a in bb]
def qmat(a): return fmpq_mat([[str(x) for x in row] for row in a])
def det(bb): return F(str(qmat(gram(bb)).det()))
def integral_even(bb):
    g=gram(bb)
    return all(x.denominator==1 for row in g for x in row) and all(g[i][i].numerator%2==0 for i in range(len(g)))
def dual(bb):
    g=qmat(gram(bb)); b=fmpq_mat([list(v) for v in bb]); d=g.inv()*b
    rr=[[F(str(d[i,j])) for j in range(d.ncols())] for i in range(d.nrows())]
    assert all(x.denominator==1 for row in rr for x in row)
    return basis([[int(x) for x in row] for row in rr])
def lattice_sum(*bb): return basis([v for b in bb for v in b])
def intersect(a,b): return dual(lattice_sum(dual(a),dual(b)))
def rmap(v):
    return tuple(v[6*k+(i-2)%6] for k in range(4) for i in range(6))+v[24:]
def vector(blocks,d=(0,0,0,0)):
    vals=[F(x)*S for b in blocks for x in b]+[F(x)*S for x in d]
    assert all(x.denominator==1 for x in vals)
    return tuple(map(int,vals))
ZERO=(0,)*6
roots=[]
for k in range(4):
    for i in range(5):
        a=[0]*6;a[i]=1;a[i+1]=-1
        blocks=[ZERO]*4;blocks[k]=a
        roots.append(vector(blocks))
for a in [(1,-1,0,0),(0,1,-1,0),(0,0,1,-1),(0,0,1,1)]:
    roots.append(vector([ZERO]*4,a))
lam=tuple(F(x,6) for x in [5,-1,-1,-1,-1,-1])
glue=[]
for a,d in [([3,3,3,3],(0,0,0,0)),([3,3,0,0],(1,0,0,0)),([3,0,3,0],(F(1,2),)*4),([2,2,2,0],(0,0,0,0)),([2,4,0,2],(0,0,0,0))]:
    glue.append(vector([mul(k,lam) for k in a],d))
generators=roots+glue
N=basis(generators)
rho=vector([tuple(F(x,2) for x in [5,3,1,-1,-3,-5])]*4,(3,2,1,0))
alpha=roots[0]
assert dot(rho,alpha)==1 and dot(rho,rho)==84

def neighbour(d):
    h=6
    ker=basis([mul(d,alpha)]+[add(g,mul(-int(dot(rho,g)),alpha)) for g in generators])
    v=add(mul(F(1,d),rho),mul(-F(h,d),alpha))
    assert all(F(x).denominator==1 for x in v)
    return basis(ker+[tuple(map(int,v))])
L=neighbour(6)
L1=basis([rmap(v) for v in L]);L2=basis([rmap(rmap(v)) for v in L])
J=intersect(L,L1)
assert intersect(L1,L2)==J and intersect(L2,L)==J
assert basis([rmap(v) for v in J])==J
v=add(mul(F(1,6),rho),mul(-1,alpha));v=tuple(map(int,v))
def omega(k): return tuple(F(int(i<k))-F(k,6) for i in range(6))
u=vector([omega(2),omega(4),ZERO,omega(2)])
e=[u,v,rmap(u),rmap(v)]
assert all(dot(a,b).denominator==1 for a in e for b in J)
assert all(basis(J+[mul(3,a)])==J for a in e)
assert lattice_sum(J,basis(e))==dual(J)
def lift(c): return tuple(sum(c[k]*e[k][j] for k in range(4)) for j in range(28))
def q(c): return (dot(lift(c),lift(c))/2)%1
elements=list(product(range(3),repeat=4))
isotropic=[c for c in elements if q(c)==0]
planes=set()
for a,b in combinations(isotropic[1:],2):
    ss=frozenset(tuple((i*x+j*y)%3 for x,y in zip(a,b)) for i,j in product(range(3),repeat=2))
    if len(ss)==9 and all(q(c)==0 for c in ss): planes.add(ss)
planes=sorted(planes,key=lambda ss:sorted(ss))
over=[]
for ss in planes:
    nz=sorted(c for c in ss if any(c));a=nz[0]
    b=next(c for c in nz if c!=a and c!=tuple(2*x%3 for x in a))
    bb=basis(J+[lift(a),lift(b)])
    assert det(bb)==1 and integral_even(bb)
    over.append((a,b,bb))

def enumerator_input(bb,bound,path,store=False):
    # LLL only chooses a faster basis.  All subsequent enumeration is exact.
    zz=fmpz_mat([list(v) for v in bb]);ll,tt=zz.lll(transform=True)
    assert tt.det() in (-1,1) and tt*zz==ll
    rr=[[int(ll[i,j]) for j in range(ll.ncols())] for i in range(ll.nrows())]
    g=gram(rr);assert all(x.denominator==1 for row in g for x in row)
    n=len(g);gs=[[F(x) for x in row] for row in g]
    minors=[1];d=[];U=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    for i in range(n):
        di=gs[i][i]-sum(d[k]*U[k][i]**2 for k in range(i));d.append(di)
        m=F(minors[-1])*di;assert m.denominator==1 and m>0;minors.append(int(m))
        for j in range(i+1,n):
            U[i][j]=(gs[i][j]-sum(d[k]*U[k][i]*U[k][j] for k in range(i)))/di
    mm=[]
    for i in range(n):
        row=[]
        for j in range(n):
            a=U[i][j]*minors[i+1];assert a.denominator==1;row.append(int(a))
        mm.append(row)
    text=f'{n} {bound} {int(store)}\n'+' '.join(map(str,minors))+'\n'
    text+='\n'.join(' '.join(map(str,row)) for row in mm)+'\n'
    path.write_text(text)
    path.with_suffix('.basis.json').write_text(json.dumps(rr))
    return {"minors_max":max(minors),"bound":bound,"rank":n}

if __name__=='__main__':
    started=time.time();REC.mkdir(exist_ok=True)
    print('Exact independent construction; coordinates scaled by12')
    for name,b in [('R',basis(roots)),('N',N),('L0',L),('L1',L1),('L2',L2),('J',J),('N2',neighbour(2)),('N3',neighbour(3))]:
        print(name,'rank',len(b),'det',det(b),'even_integral',integral_even(b))
        (REC/f'B_{name}_basis.json').write_text(json.dumps(b))
    print('J pairwise intersection and r-stable: True')
    print('Discriminant Gram:',[[str(x) for x in row] for row in gram(e)])
    print('isotropic vectors including zero',len(isotropic),'planes',len(planes))
    data={}
    for name,b,bound,store in [('N',N,2,True),('J',J,6,False),('N2',neighbour(2),2,True),('N3',neighbour(3),2,True)]+[(f'over_{i}',b,2,True) for i,(a,c,b) in enumerate(over)]:
        print('enumeration input',name,enumerator_input(b,bound,REC/f'B_{name}.enum',store))
        data[name]={'basis':b,'bound':bound}
    for i,(a,b,bb) in enumerate(over):
        rf=basis([rmap(v) for v in bb]);rimage=next(j for j,(_,_,cc) in enumerate(over) if cc==rf)
        print('overlattice',i,'plane',a,b,'rimage',rimage,'equals',[name for name,cc in [('L0',L),('L1',L1),('L2',L2),('N2',neighbour(2))] if bb==cc])
    print('elapsed_seconds',time.time()-started)
