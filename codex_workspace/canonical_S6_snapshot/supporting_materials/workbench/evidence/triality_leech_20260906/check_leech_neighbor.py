"""Exact arithmetic audit; all coordinates keep the canonical Euclidean metric."""
from fractions import Fraction as F
from itertools import product
import json

def dot(x,y): return sum(a*b for a,b in zip(x,y))
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def scale(a,x): return tuple(a*b for b in x)
def norm(x): return dot(x,x)

rhoA=tuple(F(x,2) for x in (5,3,1,-1,-3,-5))
rhoD=tuple(map(F,(3,2,1,0)))
rho=rhoA*4+rhoD
alpha=(F(1),F(-1))+tuple(F(0) for _ in range(26))
assert norm(rho)==84 and dot(rho,alpha)==1
v=add(scale(F(1,6),rho),scale(-1,alpha))
assert norm(v)==4 and dot(rho,scale(6,v))==78

C2=[]
for a,b,c in product(range(2),repeat=3):
    C2.append(((a^b^c,a^b,a^c,a),(b,c)))
C3=[((a+b)%3,(a+2*b)%3,a,b) for a,b in product(range(3),repeat=2)]
H=[(tuple((3*u[i]+2*z[i])%6 for i in range(4)),y,u,z)
   for u,y in C2 for z in C3]
assert len({(t,y) for t,y,u,z in H})==72
assert any(t==(3,3,3,3) and y==(0,0) for t,y,u,z in H)
for t,y,u,z in H:
    assert (sum(F(5*x*x,6) for x in t)+(y!=(0,0)))%2==0

def omegaA(t): return tuple(F(j<t)-F(t,6) for j in range(6))
omegaD={(0,0):(F(0),)*4,(1,0):tuple(map(F,(1,0,0,0))),
        (0,1):(F(1,2),)*4,(1,1):(F(1,2),)*3+(F(-1,2),)}
for t,y,u,z in H:
    ua=sum((omegaA(k) for k in t),())+omegaD[y]
    assert norm(ua)%2==0
    assert dot(rho,ua)==3*norm(ua) and dot(rho,ua)%6==0
    assert norm(add(ua,scale(F(-1,6),rho)))==F(7,3)

def amin(m,t):
    offset=tuple(F(m,6)*r-F(t,6) for r in rhoA)
    choices=[[n for n in range(-4,5) if (n+a)**2<=2] for a in offset]
    out=[]
    for ns in product(*choices):
        if sum(ns)!=t: continue
        y=add(ns,offset)
        if norm(y)<=2: out.append((norm(y),add(ns,(-F(t,6),)*6)))
    best=min(q for q,x in out)
    return best,[x for q,x in out if q==best]

Dreps={(0,0):(F(0),)*4,(1,0):tuple(map(F,(1,0,0,0))),
       (0,1):(F(1,2),)*4,(1,1):(F(-1,2),)+(F(1,2),)*3}
def dmin(m,mark):
    rep=Dreps[mark]
    offset=add(rep,scale(F(m,6),rhoD))
    choices=[[n for n in range(-4,5) if (n+a)**2<=2] for a in offset]
    out=[]
    for ns in product(*choices):
        if sum(ns)%2: continue
        y=add(ns,offset)
        if norm(y)<=2: out.append((norm(y),add(ns,rep)))
    best=min(q for q,x in out)
    return best,[x for q,x in out if q==best]

AM={(m,t):amin(m,t) for m in range(4) for t in range(6)}
DM={(m,y):dmin(m,y) for m in range(4) for y in Dreps}
assert all(AM[1,t][0]==F(35,72) for t in range(6))
assert all(DM[1,y][0]==F(7,18) for y in Dreps)
assert all(AM[2,t][0]==(F(11,18) if t%2==0 else F(4,9)) for t in range(6))
assert DM[2,(0,0)][0]==F(2,9)
assert all(AM[3,t][0]==(F(3,8) if t%3==0 else F(17,24)) for t in range(6))
assert all(DM[3,y][0]==F(1,2) for y in Dreps)

equality={}
for m in (1,2,3):
    candidates=[]
    for t,y,u,z in H:
        minimum=sum(AM[m,k][0] for k in t)+DM[m,y][0]
        assert minimum>=2
        if minimum!=2: continue
        for blocks in product(*(AM[m,k][1] for k in t),DM[m,y][1]):
            x=sum(blocks,())
            w=add(x,scale(F(m,6),rho))
            assert norm(w)==2
            pairing=dot(rho,x)
            assert norm(x)%2==0 and pairing.denominator==1
            assert (pairing+m)%6!=0
            candidates.append((int(norm(x)),int(pairing)%6))
    equality[m]={"candidate_count":len(candidates),
                 "norm_pairing_residue_pairs":sorted(set(candidates))}

def eye(n): return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
def mm(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))
                         for j in range(len(b[0]))) for i in range(len(a)))
def mpow(a,n):
    out=eye(len(a))
    for _ in range(n): out=mm(out,a)
    return out
def reflect(a):
    return tuple(tuple(F(i==j)-2*a[i]*a[j]/norm(a) for j in range(4)) for i in range(4))
froots=[tuple(map(F,x)) for x in ((0,1,-1,0),(0,0,1,-1),(0,0,0,1))]
froots.append((F(1,2),F(-1,2),F(-1,2),F(-1,2)))
cf=eye(4)
for a in froots: cf=mm(cf,reflect(a))
cf2=mpow(cf,2); cf3=mpow(cf,3)
assert mpow(cf,6)==tuple(tuple(-a for a in row) for row in eye(4))
assert mpow(cf,12)==eye(4)
assert all(mpow(cf,k)!=eye(4) for k in (1,2,3,4,6))
assert all(mpow(cf,4)[i][j]-cf2[i][j]+eye(4)[i][j]==0 for i in range(4) for j in range(4))
assert all(sum(abs(a) for a in row)==1 for row in cf3)
assert sum(a<0 for row in cf3 for a in row)%2==0

def matvec(a,x): return tuple(dot(row,x) for row in a)
def dclass(x):
    for y,rep in Dreps.items():
        d=add(x,scale(-1,rep))
        if all(a.denominator==1 for a in d) and sum(d)%2==0: return y
    raise AssertionError(x)
triality={str(y):dclass(matvec(cf,rep)) for y,rep in Dreps.items()}
assert matvec(cf,Dreps[1,0])==add(Dreps[1,1],tuple(map(F,(1,-1,0,0))))
assert matvec(cf,Dreps[0,1])==Dreps[1,0]
assert matvec(cf,Dreps[1,1])==add(Dreps[0,1],tuple(map(F,(0,0,-1,-1))))
assert len({triality[str(y)] for y in Dreps})==4
assert all(triality[str(y)]!=y for y in Dreps if y!=(0,0))

result={"status":"PASS","rho_squared":str(norm(rho)),"v_squared":str(norm(v)),
        "glue_order":len(H),"neighbor_index_each_side":6,
        "holy_representatives_all_72_checked":True,
        "A_shift_minima":{str(m):[str(AM[m,t][0]) for t in range(6)] for m in range(4)},
        "D_shift_minima":{str(m):{str(y):str(DM[m,y][0]) for y in Dreps} for m in range(4)},
        "norm_two_equality_candidates_all_excluded":equality,
        "F4_coxeter_matrix":[[str(a) for a in row] for row in cf],
        "F4_coxeter_cube":[[str(a) for a in row] for row in cf3],
        "F4_coxeter_triality":triality}
print(json.dumps(result,indent=2))
