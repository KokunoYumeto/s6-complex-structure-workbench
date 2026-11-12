"""Exact audit of the marked residue C3 action and common integral lattice."""
from fractions import Fraction as F
from itertools import permutations, product
from math import lcm
import json
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

def dot(x,y): return sum(a*b for a,b in zip(x,y))
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def sc(a,x): return tuple(a*b for b in x)
def sub(x,y): return add(x,sc(-1,y))
def norm(x): return dot(x,x)
zero=(F(0),)*28
rhoA=tuple(F(x,2) for x in (5,3,1,-1,-3,-5))
rhoD=tuple(map(F,(3,2,1,0)))
rho=rhoA*4+rhoD
alpha=(F(1),F(-1))+(F(0),)*26
def rA(x): return x[-2:]+x[:-2]
def r(x): return sum((rA(x[6*i:6*i+6]) for i in range(4)),())+x[24:]
rhos=(rho,r(rho),r(r(rho)))
assert r(rhos[2])==rho and pow(289,2,840)==361
assert all(norm(s)==84 and dot(s,alpha)==1 for s in rhos)
vs=tuple(sub(sc(F(1,6),s),alpha) for s in rhos)
q1=sub(vs[1],vs[0]);q2=sub(vs[2],vs[0])

C2=[((a^b^c,a^b,a^c,a),(b,c)) for a,b,c in product(range(2),repeat=3)]
C3=[((a+b)%3,(a+2*b)%3,a,b) for a,b in product(range(3),repeat=2)]
H={(tuple((3*u[i]+2*z[i])%6 for i in range(4)),y):(u,z)
   for u,y in C2 for z in C3}
Dreps={(0,0):(F(0),)*4,(1,0):tuple(map(F,(1,0,0,0))),
       (0,1):(F(1,2),)*4,(1,1):(F(-1,2),)+(F(1,2),)*3}
def aclass(x):
    if sum(x)!=0 or any((a-x[0]).denominator!=1 for a in x):return None
    t=-6*x[0]
    if t.denominator!=1:return None
    return int(t)%6
def dclass(x):
    for y,d in Dreps.items():
        z=sub(x,d)
        if all(a.denominator==1 for a in z) and sum(z)%2==0:return y
    return None
def nclass(x):
    t=tuple(aclass(x[6*i:6*i+6]) for i in range(4));y=dclass(x[24:])
    return (t,y) if (t,y) in H else None
def inN(x):return nclass(x) is not None
def bglue(x):
    cl=nclass(x)
    assert cl is not None
    return H[cl][1][3]
def ell(x,j):return dot(rhos[j],x)%6
def inI(x):return inN(x) and ell(x,0)==0 and bglue(x)==0
def inLambda(x,j):
    k=6*dot(x,alpha)
    if k.denominator!=1:return False
    k=int(k)%6
    y=sub(x,sc(F(k,6),rhos[j]))
    return inN(y) and (dot(rhos[j],y)+k)%6==0
def inJ(x):return inI(x) or inI(sub(x,sc(3,vs[0])))

# Full local A orbit audit: all 720 possible Weyl-vector blocks.
aper=list(permutations(rhoA))
plus={};minus=0
for s in aper:
    t=aclass(sc(F(1,6),sub(rA(s),s)))
    if t is not None:plus[t]=plus.get(t,0)+1
    if aclass(sc(F(1,6),add(rA(s),s))) is not None:minus+=1
assert plus=={4:18,2:18} or plus=={2:18,4:18}
assert minus==0
assert not any((t,(0,0)) in H for t in product((2,4),repeat=4))
assert not inN(q1) and not inN(q2)
assert inN(sc(3,q1)) and inN(sc(3,q2))

def omegaA(t):return tuple(F(j<t)-F(t,6) for j in range(6))
omegaD=dict(Dreps);omegaD[1,1]=(F(1,2),)*3+(F(-1,2),)
def ua(t,y):return sum((omegaA(k) for k in t),())+omegaD[y]
u=ua((2,4,0,2),(0,0))
assert norm(u)==4 and dot(rho,u)==12 and bglue(u)==1

# Generate original R, then N, then the exact kernel I and common lattice J.
Rgens=[]
for i in range(4):
    for j in range(5):
        e=list(zero);e[6*i+j]=F(1);e[6*i+j+1]=F(-1);Rgens.append(tuple(e))
for d in ((1,-1,0,0),(0,1,-1,0),(0,0,1,-1),(0,0,1,1)):
    Rgens.append((F(0),)*24+tuple(map(F,d)))
gluekeys=(((3,3,3,3),(0,0)),((3,3,0,0),(1,0)),
          ((3,0,3,0),(0,1)),((2,2,2,0),(0,0)),((2,4,0,2),(0,0)))
Ngens=Rgens+[ua(*h) for h in gluekeys]
assert all(inN(g) for g in Ngens)
for g in Ngens:
    assert ell(g,1)==(ell(g,0)+4*bglue(g))%6
    assert ell(g,2)==(ell(g,0)+2*bglue(g))%6
Kgens=[sub(g,sc(ell(g,0),alpha)) for g in Ngens]+[sc(6,alpha)]
Igens=[sub(sub(g,sc(ell(g,0),alpha)),sc(bglue(g),u)) for g in Ngens]+[sc(6,alpha),sc(3,u)]
Jgens=Igens+[sc(3,vs[0])]
Lgens=[Kgens+[vs[0]]]
Lgens.extend([[r(g) for g in Lgens[0]],[r(r(g)) for g in Lgens[0]]])
assert all(inI(g) for g in Igens)
assert all(inI(sc(3,q)) for q in (q1,q2))
assert inI(sub(alpha,r(alpha))) and inI(sub(alpha,r(r(alpha))))
assert inI(sc(6,vs[0])) and not inN(sc(3,vs[0]))
assert all(inJ(g) and inJ(r(g)) for g in Jgens)
assert all(inLambda(g,j) for g in Jgens for j in range(3))
assert all(dot(g,h).denominator==1 for g in Jgens for h in Jgens)
assert all(norm(g)%2==0 for g in Jgens)

def rcoords(x):
    out=[]
    for i in range(4):
        out.extend(sum(x[6*i:6*i+j+1]) for j in range(5))
    a,b,c,d=x[24:]
    return out+[a,a+b,(a+b+c-d)/2,(a+b+c+d)/2]
def rat(a):return sp.Rational(a.numerator,a.denominator)
def basis(gens):
    mat=sp.Matrix.hstack(*(sp.Matrix([rat(a) for a in rcoords(g)]) for g in gens))
    den=lcm(*(int(a.q) for a in mat))
    scaled=mat*den
    assert all(a.q==1 for a in scaled)
    integers=sp.Matrix(scaled.rows,scaled.cols,[int(a) for a in scaled])
    return hermite_normal_form(integers)/den
def determinant(gens):
    mat=basis(gens)
    assert mat.shape==(24,24)
    return sp.factor(mat.det()**2*5184)
dets={"N":determinant(Ngens),"I":determinant(Igens),"J":determinant(Jgens)}
for j in range(3):dets["Lambda"+str(j)]=determinant(Lgens[j])
for i,j in ((0,1),(1,2),(2,0)):
    dets["sum_"+str(i)+str(j)]=determinant(Lgens[i]+Lgens[j])
assert dets["N"]==1 and dets["I"]==324 and dets["J"]==81
assert all(dets["Lambda"+str(j)]==1 for j in range(3))
assert all(dets["sum_"+str(i)+str(j)]==sp.Rational(1,81) for i,j in ((0,1),(1,2),(2,0)))

# Four explicit discriminant generators and the full r matrix modulo three.
discbasis=(u,vs[0],r(u),r(vs[0]))
assert all(inJ(sc(3,g)) for g in discbasis)
assert all(dot(g,h).denominator==1 for g in discbasis for h in Jgens)
G3=[[int(3*dot(a,b))%3 for b in discbasis] for a in discbasis]
gram=[[dot(a,b) for b in discbasis] for a in discbasis]
assert gram==[[F(4),F(2),F(-2),F(-4,3)],
              [F(2),F(4),F(-2,3),F(-2,3)],
              [F(-2),F(-2,3),F(4),F(2)],
              [F(-4,3),F(-2,3),F(2),F(4)]]
def lincomb(coeff):
    x=zero
    for k,g in zip(coeff,discbasis):x=add(x,sc(k,g))
    return x
reps={coeff:lincomb(coeff) for coeff in product(range(3),repeat=4)}
assert sum(inJ(x) for x in reps.values())==1
cols=[]
for g in discbasis:
    matches=[coeff for coeff,x in reps.items() if inJ(sub(r(g),x))]
    assert len(matches)==1
    cols.append(matches[0])
rmat=sp.Matrix(4,4,lambda i,j:cols[j][i])
gmat=sp.Matrix(G3)
assert all(int(a)%3==0 for a in rmat**3-sp.eye(4))
assert all(int(a)%3==0 for a in rmat.T*gmat*rmat-gmat)
assert int(gmat.det())%3!=0
Lplanes=[]
for j in range(3):
    plane=[coeff for coeff,x in reps.items() if inLambda(x,j)]
    assert len(plane)==9
    assert all(norm(reps[c])%2==0 for c in plane)
    Lplanes.append(plane)
assert all(set(Lplanes[i])&set(Lplanes[j])=={(0,0,0,0)} for i,j in ((0,1),(1,2),(2,0)))

# The parent-requested fourth plane and its explicit Niemeier extension.
p=sub(u,r(u))
q=add(sub(vs[0],r(vs[0])),r(u))
Mgens=Jgens+[p,q]
def inM(x):
    return any(inJ(sub(x,add(sc(a,p),sc(b,q)))) for a,b in product(range(3),repeat=2))
fourth={(a,b,(-a+b)%3,(-b)%3) for a,b in product(range(3),repeat=2)}
assert all(tuple(int(a)%3 for a in rmat*sp.Matrix(c)) in fourth for c in fourth)
assert all(norm(reps[c])%2==0 for c in fourth)
assert all(set(plane)&fourth=={(0,0,0,0)} for plane in Lplanes)
assert all(inM(r(g)) for g in Mgens)
assert all(norm(g)%2==0 for g in Mgens)
assert all(dot(g,h).denominator==1 for g in Mgens for h in Mgens)
assert determinant(Mgens)==1
assert all(determinant(Mgens+Lgens[j])==sp.Rational(1,81) for j in range(3))
Lzero=Igens+[p]
assert determinant(Lzero)==36 and determinant(Ngens+Mgens)==sp.Rational(1,36)
assert ell(p,0)==4 and bglue(p)==0 and inI(sc(3,p))
assert inI(sc(3,q))

roots=[]
for block in range(4):
    for i in range(6):
        for j in range(6):
            if i==j:continue
            x=list(zero);x[6*block+i]=F(1);x[6*block+j]=F(-1)
            if inM(tuple(x)):roots.append(tuple(x))
for i in range(4):
    for j in range(i+1,4):
        for a,b in product((-1,1),repeat=2):
            x=list(zero);x[24+i]=F(a);x[24+j]=F(b)
            if inM(tuple(x)):roots.append(tuple(x))
assert len(roots)==56

def minA_shift(b,t):
    offset=tuple(rhoA[j]/2-b*q1[j]-F(t,6) for j in range(6))
    choices=[[n for n in range(-5,6) if (n+a)**2<=2] for a in offset]
    choices_out=[]
    for ns in product(*choices):
        if sum(ns)!=t:continue
        y=add(ns,offset)
        if norm(y)<=2:choices_out.append((norm(y),y))
    best=min(a for a,x in choices_out)
    return best,[x for a,x in choices_out if a==best]
def minD_half(y):
    offset=add(Dreps[y],sc(F(1,2),rhoD))
    choices=[[n for n in range(-4,5) if (n+a)**2<=2] for a in offset]
    choices_out=[]
    for ns in product(*choices):
        if sum(ns)%2:continue
        vD=add(ns,offset)
        if norm(vD)<=2:choices_out.append((norm(vD),vD))
    best=min(a for a,x in choices_out)
    return best,[x for a,x in choices_out if a==best]
AMS={(b,t):minA_shift(b,t) for b in range(3) for t in range(6)}
DMS={y:minD_half(y) for y in Dreps}
half_candidates={}
for b in range(3):
    found=[]
    for t,y in H:
        minimum=sum(AMS[b,k][0] for k in t)+DMS[y][0]
        assert minimum>=2
        if minimum!=2:continue
        for blocks in product(*(AMS[b,k][1] for k in t),DMS[y][1]):
            x=sum(blocks,())
            assert norm(x)==2 and inM(x)
            found.append(x)
    half_candidates[b]=len(found)
    roots.extend(found)
assert half_candidates=={0:16,1:0,2:0}
assert len(set(roots))==72 and all(inM(x) and norm(x)==2 for x in roots)
zetas=[]
for i in range(4):
    x=list(zero);x[6*i:6*i+6]=tuple(F(a,4) for a in (1,-1,1,-1,1,-1))
    zetas.append(tuple(x))
rows=((1,1,1,1),(-1,-1,1,1),(-1,1,-1,1),(1,-1,-1,1))
deltas=((1,0,1,0),(1,0,-1,0),(0,1,0,1),(0,1,0,-1))
newroots=set()
for row,dd in zip(rows,deltas):
    zz=zero
    for a,z in zip(row,zetas):zz=add(zz,sc(a,z))
    delta=(F(0),)*24+tuple(map(F,dd))
    for a,b in product((-1,1),repeat=2):
        newroots.add(add(sc(a,zz),sc(F(b,2),delta)))
assert len(newroots)==16
assert newroots=={x for x in roots if not inN(x)}

unseen=set(roots);components=[]
while unseen:
    component={next(iter(unseen))}
    todo=list(component)
    while todo:
        x=todo.pop()
        neighbors={y for y in unseen-component if dot(x,y)!=0}
        component|=neighbors
        todo.extend(neighbors)
    unseen-=component
    components.append(component)
assert len(components)==12 and all(len(c)==6 for c in components)
for comp in components:
    found=False
    for a in comp:
        for b in comp:
            if dot(a,b)==-1:
                assert comp=={a,b,add(a,b),sc(-1,a),sc(-1,b),sc(-1,add(a,b))}
                found=True
                break
        if found:break
    assert found
assert determinant(list(roots))==3**12
assert all(r(x) in roots for x in roots)
fixed_components=sum(all(r(x)==x for x in comp) for comp in components)
assert fixed_components==4

result={"status":"PASS","residue_element":361,"action":"C^2 in four A5 blocks; identity on D4",
        "A_Weyl_blocks_exhausted":len(aper),"admissible_plus_A_classes":plus,
        "admissible_minus_A_blocks":minus,"fixed_neighbors_in_specified_family":0,
        "original_glue_order":len(H),"q1_squared":str(norm(q1)),"q2_squared":str(norm(q2)),
        "q1_q2_pairing":str(dot(q1,q2)),"rho_q1_pairing":str(dot(rho,q1)),
        "u_squared":str(norm(u)),"rho_u_pairing":str(dot(rho,u)),
        "determinants":{k:str(v) for k,v in dets.items()},
        "discriminant_basis":["u","v0","r(u)","r(v0)"],
        "full_Euclidean_Gram_of_discriminant_representatives":[[str(a) for a in row] for row in gram],
        "three_times_discriminant_Gram_mod3":G3,
        "r_matrix_columns_in_discriminant_basis_mod3":[list(c) for c in cols],
        "r_matrix_rows_mod3":[list(map(int,rmat.row(i))) for i in range(4)],
        "isotropic_planes":[[list(c) for c in plane] for plane in Lplanes],
        "all_pairwise_intersections_equal_J":True,
        "fourth_plane_fixed":True,"fourth_extension_generators":["u-r(u)","v+r(u)-r(v)"],
        "fourth_extension_determinant":str(determinant(Mgens)),
        "fourth_extension_intersection_N_determinant":str(determinant(Lzero)),
        "fourth_extension_root_count":len(roots),"fourth_extension_root_system":"A2^12",
        "fourth_extension_half_shift_candidates":half_candidates,
        "fourth_extension_root_lattice_determinant":str(determinant(list(roots))),
        "fourth_extension_root_lattice_index":3**6,
        "fourth_extension_fixed_A2_components":fixed_components,
        "fourth_extension_rotated_A2_components":12-fixed_components}
print(json.dumps(result,indent=2))
