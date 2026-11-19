"""Exact integral p=infinity period fan and 23-cone regular refinement."""
from pathlib import Path
from itertools import combinations
import sympy as S,json
r,z=S.symbols('r z',nonnegative=True)
R,u,f,v,w=S.symbols('R u f v w',nonzero=True)
checks=[]
def ck(n,e):
    e=S.factor(e)
    assert e==0,(n,e)
    checks.append(n)
MR=S.Matrix([[5,1],[1,2]]);MU=S.Matrix([[0,0],[0,1]])
for entry in MR-(4*S.Matrix([[1,0],[0,0]])+S.Matrix([[0,0],[0,1]])+S.ones(2)):
    ck('principal cone entry',entry)
ck('period determinant',(r*MR+z*MU).det()-(9*r*r+5*r*z))
K=(R**5*f**2,R);J=(R*f,R**2*u)
ck('h line',J[0]**2/K[0]-R**-3)
ck('h source',J[1]**2/K[1]-R**3*u**2)
ck('B line',K[0]/J[0]-R**4*f)
ck('B source',K[1]/J[1]-R**-1*u**-1)
poly=[(0,0),(-4*r,0),(-5*r,-r),(-5*r,-2*r-z),(-r,-2*r-z),(0,-r-z)]
area=sum(poly[i][0]*poly[(i+1)%6][1]-poly[(i+1)%6][0]*poly[i][1] for i in range(6))/2
ck('full hexagon area',area-(9*r*r+5*r*z))
inside=lambda x,y:-5<=x<=0 and -2<=y<=0 and -4<=x-y<=1
tri=[]
for x in range(-5,0):
    for y in range(-2,0):
        for t in [((x,y),(x+1,y),(x+1,y+1)),((x,y),(x,y+1),(x+1,y+1))]:
            if all(inside(*a) for a in t):tri.append(t)
assert len(tri)==18;checks.append('eighteen upper unit triangles')
A=(0,0,0,1);B=(0,-1,0,1)
cones=[(A,)+tuple((x,y,1,0) for x,y in t) for t in tri]
cones += [(A,B,(x,-2,1,0),(x+1,-2,1,0)) for x in range(-5,-1)]
cones += [(A,B,(-1,-2,1,0),(0,-1,1,0))]
assert len(cones)==23;checks.append('twenty-three full cones')
data=[]
for i,rs in enumerate(cones):
    V=S.Matrix.hstack(*map(S.Matrix,rs));det=V.det()
    assert abs(det)==1,(i,det);checks.append('unimodular cone '+str(i))
    ws=tuple(V.inv()*S.Matrix([1,0,0,0]))
    ck('physical weight sum '+str(i),sum(ws))
    for q in rs:
        ck('canonical height '+str((i,q)),q[2]+q[3]-1)
        assert q[1]+3*q[2]+2*q[3]>=0
        assert -q[1]>=0
    checks.append('actual source node monomials '+str(i))
    data.append({'rays':rs,'det':int(det),'physical_weights':list(map(int,ws)),
                 'dual_characters':[[int(a) for a in row] for row in V.inv().tolist()]})
def facets(row):
    out=set()
    for C in cones:
        for F in combinations(C,3):
            if all(sum(a*b for a,b in zip(row,v))==0 for v in F):
                if S.Matrix.hstack(*map(S.Matrix,F)).rank()==3:
                    out.add(tuple(sorted(F)))
    return out
TK=S.Matrix([[1,0,5,0],[0,1,1,0],[0,0,1,0],[0,0,0,1]])
TJ=S.Matrix([[1,0,1,0],[0,1,2,1],[0,0,1,0],[0,0,0,1]])
def transform(fs,T):
    return {tuple(sorted(tuple(map(int,T*S.Matrix(v))) for v in F)) for F in fs}
tests=[
 ('K', (1,0,0,0),(1,0,5,0),TK),
 ('J', (0,1,0,0),(0,1,2,1),TJ),
 ('KJinv',(1,-1,-1,-1),(1,-1,4,0),TK*TJ.inv())]
for n,target,source,T in tests:
    lhs=facets(target);rhs=transform(facets(source),T)
    assert lhs==rhs,(n,lhs,rhs)
    checks.append('full shared-facet triangulation '+n)
    ck('period fan determinant '+n,T.det()-1)
# Exact convexity increments for the integral quadratic refinement.
i,j=S.symbols('i j',integer=True)
phi=lambda i,j:5*r*i*(i-1)/2+(2*r+z)*j*(j-1)/2+r*i*j
ck('diagonal convexity',phi(i,j)+phi(i+1,j+1)-phi(i+1,j)-phi(i,j+1)-r)
ck('horizontal remaining convexity',5*r-r-4*r)
ck('vertical remaining convexity',2*r+z-r-(r+z))
for l,m in [(1,0),(0,1),(1,-1),(-2,3)]:
    shift=(r*MR+z*MU)*S.Matrix([l,m])
    ck('integer quadratic period identity '+str((l,m)),
       phi(i+l,j+m)-phi(i,j)-phi(l,m)-i*shift[0]-j*shift[1])
out={'status':'PASS','count':len(checks),'checks':checks,
     'upper_triangles':tri,'cones':data,
     'scope':'Exact actual-period toric fan, integral regular chart semigroups, source-node height and full shared-facet arrows. Point-line graph gluing, compact global boundary, inherited spin attachment and return remain unassigned.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
