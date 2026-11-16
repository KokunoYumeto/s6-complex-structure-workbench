"""Exact charge, fan and dual-complex checks for C.2.UN.68.

The source proves the actual analytic and algebraic morphisms.  This
script checks their integral intersection arithmetic, the explicit
torus action, and finite cellular models; it asserts no smoothability
of abstract proposed toric gluing data.
"""
import random
import sympy as S

v,r,t=S.symbols('v r t', integer=True)
sol=S.solve([v-r+t,2*r-3*t],(r,t))
assert sol=={r:3*v,t:2*v}
e_components=12*(r-t)-3*t
n_components=2*r
assert S.expand((e_components-n_components).subs(sol))==0
assert S.expand((e_components-2*r+t).subs(sol))==2*v
print('PASS exact global counts: r=3v, t=2v, e(S)=2v, sum(e(V_i)-n_i)=0.')

possibilities=[]
for h in (1,2):
    for vertical in range(5):
        if 2*vertical<=2*h:
            possibilities.append((h,vertical,h+vertical))
assert all(n<=4 for h,k,n in possibilities)
assert [(h,k) for h,k,n in possibilities if n==4]==[(2,2)]
partitions=[(3,), (2,1), (1,1,1)]
assert max(map(len,partitions))==3
assert [x for x in partitions if len(x)==3]==[(1,1,1)]
print('PASS minimal-pair bounds: P2 has at most3 boundary primes; F_b at most4, with equality exactly two sections and two fibres.')

z,w,b,lam,mu=S.symbols('z w b lambda mu',nonzero=True)
# The integer exponent is kept exact in a finite full range.
for degree in range(81):
    transformed=(lam*z)**(-degree)*(mu*w)
    second_chart=lam**(-degree)*mu*(z**(-degree)*w)
    assert S.simplify(transformed-second_chart)==0
print('PASS 81 exact ruled-chart torus actions preserve w_infinity=z^(-b)w_zero.')

def det(a,b):
    return a[0]*b[1]-a[1]*b[0]

def squares(fan):
    n=len(fan)
    assert all(det(fan[i],fan[(i+1)%n])==1 for i in range(n))
    return [-det(fan[(i-1)%n],fan[(i+1)%n]) for i in range(n)]

def check(fan):
    self_intersections=squares(fan)
    n=len(fan)
    assert sum(self_intersections)+2*n==12-n
    return self_intersections

seeds=[[(1,0),(0,1),(-1,-1)]]
seeds += [[(1,0),(0,1),(-1,b),(0,-1)] for b in range(81)]
rng=random.Random(6802026)
corner_cases=0
for seed in seeds:
    fan=list(seed)
    old=check(fan)
    for step in range(16):
        i=rng.randrange(len(fan))
        j=(i+1)%len(fan)
        ray=(fan[i][0]+fan[j][0],fan[i][1]+fan[j][1])
        new_fan=fan[:i+1]+[ray]+fan[i+1:]
        new=check(new_fan)
        expected=list(old)
        expected[i]-=1
        expected[j]-=1
        expected=expected[:i+1]+[-1]+expected[i+1:]
        assert new==expected
        assert sum(new)+2*len(new)==sum(old)+2*len(old)-1
        fan,old=new_fan,new
        corner_cases+=1
print('PASS',corner_cases,'exact corner blowups: primitive smooth fan, adjacent squares minus1, new square minus1, K^2 minus1 and charge unchanged.')

charge_cases=0
for minimal_e,minimal_n in ((3,1),(3,2),(3,3),(4,1),(4,2),(4,3),(4,4)):
    for corners in range(31):
        for internals in range(31):
            e=minimal_e+corners+internals
            n=minimal_n+corners
            assert e-n==minimal_e-minimal_n+internals>=0
            assert (e-n==0)==(minimal_e==minimal_n and internals==0)
            charge_cases+=1
print('PASS',charge_cases,'exact blowup charge identities and the equality condition.')

def torus_complex(a,b):
    def vertex(i,j):
        return (i%a)*b+(j%b)
    faces=[]
    for i in range(a):
        for j in range(b):
            faces += [(vertex(i,j),vertex(i+1,j),vertex(i+1,j+1)),
                      (vertex(i,j),vertex(i+1,j+1),vertex(i,j+1))]
    edges=sorted({tuple(sorted((face[k],face[(k+1)%3])))
                  for face in faces for k in range(3)})
    edge_index={edge:i for i,edge in enumerate(edges)}
    d1=S.zeros(len(edges),a*b)
    for i,(x,y) in enumerate(edges):
        d1[i,x]=-1; d1[i,y]=1
    d2=S.zeros(len(faces),len(edges))
    incidences=[0]*len(edges)
    for i,face in enumerate(faces):
        assert len(set(face))==3
        for k in range(3):
            x,y=face[k],face[(k+1)%3]
            j=edge_index[tuple(sorted((x,y)))]
            d2[i,j]=1 if x<y else -1
            incidences[j]+=1
    assert d2*d1==S.zeros(len(faces),a*b)
    assert set(incidences)=={2}
    ranks=(d1.rank(),d2.rank())
    betti=(a*b-ranks[0],len(edges)-sum(ranks),len(faces)-ranks[1])
    assert betti==(1,2,1)
    assert (len(edges),len(faces))==(3*a*b,2*a*b)
    return a*b,len(edges),len(faces),ranks,betti

for a,b in ((3,3),(3,4),(4,4),(5,4)):
    print('PASS exact dual-torus cellular model:',(a,b),torus_complex(a,b))
print('These cellular checks concern the displayed complexes, not existence of an analytic smoothing for arbitrary toric data.')
print('ALL UN68 EXACT CHECKS PASSED')
