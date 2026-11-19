"""Fresh FLINT rational linear algebra for F2.8--11; no producing code imported."""
from pathlib import Path
from itertools import combinations
from math import gcd
from flint import fmpq_mat
import hashlib,json

def eye(n): return fmpq_mat([[int(i==j) for j in range(n)] for i in range(n)])
def zero(r,c): return fmpq_mat(r,c)
def block(*ms):
    out=zero(sum(m.nrows() for m in ms),sum(m.ncols() for m in ms));r=c=0
    for m in ms:
        for i in range(m.nrows()):
            for j in range(m.ncols()):out[r+i,c+j]=m[i,j]
        r+=m.nrows();c+=m.ncols()
    return out
def companion(coeff):
    n=len(coeff)-1; out=zero(n,n)
    for i in range(1,n):out[i,i-1]=1
    for i in range(n):out[i,n-1]=-coeff[i]
    return out
def wedge2(m):
    ij=list(combinations(range(m.nrows()),2))
    return fmpq_mat([[m[i,k]*m[j,l]-m[i,l]*m[j,k] for k,l in ij] for i,j in ij])
def fixed(m):return m.nrows()-(m-eye(m.nrows())).rank()
def bilinear_fixed(m):
    n=m.nrows(); cols=[]
    for i in range(n):
        for j in range(n):
            e=zero(n,n);e[i,j]=1; v=m.transpose()*e*m-e
            cols.append([v[a,b] for a in range(n) for b in range(n)])
    a=fmpq_mat([[cols[j][i] for j in range(n*n)] for i in range(n*n)])
    return n*n-a.rank()
def row_basis(m):
    r,rank=m.rref();return fmpq_mat([[r[i,j] for j in range(m.ncols())] for i in range(rank)])
def pivots(r):return [next(j for j in range(r.ncols()) if r[i,j]) for i in range(r.nrows())]
def kernel(m):
    r,rank=m.rref();pv=[next(j for j in range(m.ncols()) if r[i,j]) for i in range(rank)]
    free=[j for j in range(m.ncols()) if j not in pv];out=zero(m.ncols(),len(free))
    for c,j in enumerate(free):
        out[j,c]=1
        for i,p in enumerate(pv):out[p,c]=-r[i,j]
    return out
def hstack(a,b):return fmpq_mat([[a[i,j] for j in range(a.ncols())]+[b[i,j] for j in range(b.ncols())] for i in range(a.nrows())])
def vstack(a,b):return fmpq_mat(a.tolist()+b.tolist())
def plain(m):return [[str(v) for v in row] for row in m.tolist()]

checks=[]
def check(name,truth):
    assert truth,name
    checks.append(name)

orders=[3,4,5,6,8,10,12]
pairs=[(a,b) for a,b in combinations(orders,2) if gcd(a,b)==1]
check('eight coprime finite-order pairs',pairs==[(3,4),(3,5),(3,8),(3,10),(4,5),(5,6),(5,8),(5,12)])
ranks=[(x,r1,r2) for x in range(1,7) for r1 in (2,4,6) for r2 in (2,4,6) if r1+r2==3+x and r1>=x and r2>=x]
check('only allowed low-degree invariant/fixed-rank pattern',ranks==[(1,2,2)])

cyclos={3:[1,1,1],4:[1,0,1],5:[1,1,1,1,1],6:[1,-1,1],8:[1,0,0,0,1],10:[1,-1,1,-1,1]}
finite=[]
for d in (3,4,6):
    m=block(eye(1),companion(cyclos[d]),companion(cyclos[d]))
    bh=bilinear_fixed(m);we=fixed(wedge2(m))
    check('repeated spectrum '+str(d)+' has Hom9 and wedge4',(bh,we)==(9,4))
    finite.append({'type':'(T-1)Phi'+str(d)+'^2','hom_fixed':bh,'wedge_fixed':we})
for d in (5,8,10):
    m=block(eye(1),companion(cyclos[d]))
    bh=bilinear_fixed(m);we=fixed(wedge2(m))
    check('distinct spectrum '+str(d)+' has Hom5 and wedge2',(bh,we)==(5,2))
    finite.append({'type':'(T-1)Phi'+str(d),'hom_fixed':bh,'wedge_fixed':we})
u=eye(5);u[0,1]=1;u[2,3]=1
check('cusp Hom fixed13',bilinear_fixed(u)==13)
check('cusp exterior fixed6',fixed(wedge2(u))==6)
check('Hom Euler and exterior Euler both2',-25+9+5+13==-10+4+2+6==2)
v=eye(6)
for i in (0,2,4):v[i,i+1]=1
check('rank6 maximal cusp exterior fixed9',fixed(wedge2(v))==9)

cf=companion(cyclos[5]);cg=companion(cyclos[8]);q=eye(6)
for i in range(6):q[i,0]=1
wa=q.inv()*wedge2(cf.inv())*q;wb=q.inv()*wedge2(cg)*q
s1=fmpq_mat([[wa[i,j] for j in range(1,6)] for i in range(1,6)])
s2=fmpq_mat([[wb[i,j] for j in range(1,6)] for i in range(1,6)])
n=s1*s2-eye(5)
check('rank5 model finite fixed ranks',(fixed(s1),fixed(s2))==(1,1))
check('rank5 cusp square zero rank2',n*n==zero(5,5) and n.rank()==2)
rb1=row_basis(s1-eye(5));rb2=row_basis(s2-eye(5))
check('finite row spaces dimension4',rb1.nrows()==rb2.nrows()==4)
cmap=hstack(s2.transpose()*rb1.transpose(),rb2.transpose())
g1=fmpq_mat([[(s1-eye(5))[j,p] for j in range(5)] for p in pivots(rb1)])
g2=fmpq_mat([[(s2-eye(5))[j,p] for j in range(5)] for p in pivots(rb2)])
gauge=vstack(g1,g2)
check('actual gauge-to-cusp identity',cmap*gauge==n.transpose())
check('gauge rank5',gauge.rank()==5)
k=kernel(n);restriction=k.transpose()*cmap
check('restriction quotient rank3',restriction.rank()==3)
check('restriction kernel equals gauge by inclusion and dimensions',restriction*gauge==zero(3,5) and 8-restriction.rank()==gauge.rank())
square=n.transpose()*cmap
check('square-zero extension space dimension6',square.rank()==2)
check('one-dimensional square-zero extension quotient',8-square.rank()-gauge.rank()==1)
# A full rational representative is obtained from a kernel basis, not an old certificate.
admissible=kernel(square);representative=None
for j in range(admissible.ncols()):
    t=fmpq_mat([[admissible[i,j]] for i in range(8)])
    if restriction*t!=zero(3,1):
        representative=cmap*t
        break
check('nonzero maximal extension exists',representative is not None)
check('actual lifted nilpotent has rank3',vstack(representative.transpose(),n).rank()==3)

out={'status':'PASS','library':'python-flint fmpq_mat exact rational arithmetic',
     'checks':checks,'count':len(checks),'order_pairs':pairs,'rank_patterns':ranks,
     'finite_fixed_spaces':finite,'restriction_matrix':plain(restriction),
     'gauge_matrix':plain(gauge),'maximal_cusp_row':plain(representative.transpose()),
     'scope':'Fresh exact finite tables and explicit marked-model maps; universal proofs are prederivations_12.md.',
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks)}))
