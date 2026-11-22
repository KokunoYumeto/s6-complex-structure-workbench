# Exact Hopf-related finite-group block; no other owner routines.
from fractions import Fraction as F
from itertools import permutations, product

# Quadratic field Q(sqrt(5)), represented by pairs (a,b).
zero=(F(0),F(0)); one=(F(1),F(0))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(x,n): return (x[0]*n,x[1]*n)
def sumq(xs):
    out=zero
    for x in xs: out=add(out,x)
    return out
def qm(p,q):
    a,b,c,d=p; e,f,g,h=q
    return (sub(sub(sub(mul(a,e),mul(b,f)),mul(c,g)),mul(d,h)),
            add(add(mul(a,f),mul(b,e)),sub(mul(c,h),mul(d,g))),
            add(add(mul(a,g),mul(c,e)),sub(mul(d,f),mul(b,h))),
            add(add(mul(a,h),mul(d,e)),sub(mul(b,g),mul(c,f))))
def qi(p): return (p[0],neg(p[1]),neg(p[2]),neg(p[3]))
phi=(F(1,2),F(1,2)); invphi=(F(-1,2),F(1,2))
G=set()
for j in range(4):
    for sign in [-1,1]:
        q=[zero]*4; q[j]=scale(one,sign); G.add(tuple(q))
for signs in product([-1,1],repeat=4):
    G.add(tuple(scale(one,F(sign,2)) for sign in signs))
for perm in permutations(range(4)):
    inversions=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
    if inversions%2: continue
    for signs in product([-1,1],repeat=3):
        v=[zero,scale(one,signs[0]),scale(phi,signs[1]),scale(invphi,signs[2])]
        G.add(tuple(scale(v[perm[j]],F(1,2)) for j in range(4)))
assert len(G)==120
assert all(sumq(mul(a,a) for a in p)==one for p in G)
elts=sorted(G); index={q:j for j,q in enumerate(elts)}
table=[]
for p in elts:
    row=[]
    for q in elts:
        v=qm(p,q); assert v in index
        row.append(index[v])
    table.append(row)
identity=index[(one,zero,zero,zero)]
inverse=[index[qi(p)] for p in elts]
comm={table[table[table[i][j]][inverse[i]]][inverse[j]]
      for i in range(120) for j in range(120)}
generated={identity}; frontier=[identity]
while frontier:
    p=frontier.pop()
    for q in comm:
        r=table[p][q]
        if r not in generated:
            generated.add(r); frontier.append(r)
assert len(generated)==120
print('Binary icosahedral exact check: set size', len(elts),
      '; multiplication closure entries',len(elts)**2,
      '; commutator set size',len(comm),'; derived subgroup size',len(generated))
print('Secondary Hopf H1 = Z plus G_ab = Z.')

