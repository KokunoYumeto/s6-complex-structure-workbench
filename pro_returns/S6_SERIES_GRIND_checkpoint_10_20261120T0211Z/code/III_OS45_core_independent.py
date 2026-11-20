"""Fresh integral OS45 bar/cap matrix, with every basis map retained.

Written after the printed proof; no historical implementation imported.
The construction uses only D.BC1--15, D.GI2--5 and D.VC9 as stated.
"""
from pathlib import Path
import datetime
import hashlib
import itertools
import json
import time
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parents[1]
started = time.monotonic()
checks = []
def check(name, condition):
    assert bool(condition), name
    checks.append(name)

def integral(A):
    return all(x.q == 1 for x in A)

def smith(A, name):
    dd, uu, vv = smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(s.ZZ))
    S, U, V = (x.to_Matrix() for x in (dd, uu, vv))
    check(name+' exact Smith multiplication', U*A*V == S)
    check(name+' unimodular row map', abs(U.det()) == 1)
    check(name+' unimodular column map', abs(V.det()) == 1)
    rank = sum(S[j,j] != 0 for j in range(min(S.shape)))
    return S, U, V, rank

def integer_kernel(A, name):
    S,U,V,r = smith(A,name)
    K, Kp = V[:,r:], V.inv()[r:,:]
    check(name+' full kernel identity', A*K == s.zeros(A.rows,K.cols))
    check(name+' integral split embedding', integral(Kp) and Kp*K == s.eye(K.cols))
    return K,Kp,(S,U,V)

def saturated_image(A, name):
    S,U,V,r = smith(A,name)
    C = U.inv()[:,:r]
    check(name+' primitive image basis', integral(C))
    check(name+' rational image agreement', C.row_join(A).rank() == r)
    return C

pairs = list(itertools.combinations(range(4),2))
E = s.eye(4)
def wedge(u,v):
    return s.Matrix([u[a]*v[b]-u[b]*v[a] for a,b in pairs])
def ordered_bar(u,v):
    return s.Matrix([u[a]*v[b] for a,b in pairs])
def exterior(A):
    return s.Matrix.hstack(*(wedge(A[:,a],A[:,b]) for a,b in pairs))

B = [s.Matrix(x) for x in (
    [[1,8],[0,1]], [[1,1],[0,1]], [[3,4],[-1,-1]],
    [[3,1],[-4,-1]], [[0,1],[-1,2]])]
g = [s.Matrix(x) for x in ((3,0),(0,0),(2,-1),(1,-2),(0,0))]
weights = [2,0,0,0,0]
A = []
local_data = []
for i,(b,c,w) in enumerate(zip(B,g,weights)):
    p,q = 2*c,8*c
    z,params = (b-s.eye(2)).gauss_jordan_solve(q)
    z = z.subs({x:0 for x in params})
    r = s.Matrix([[p[1],-p[0]]])*b
    aa = s.eye(4); aa[:2,:2]=b; aa[:2,3]=q
    aa[2,:2]=r; aa[2,3]=(r*z)[0]+w
    check(f'site{i} integral monodromy',integral(aa) and aa.det()==1)
    check(f'site{i} rational source lift',(b-s.eye(2))*z==q)
    A.append(aa)
    local_data.append(dict(B=b,g=c,p=p,q=q,z=z,r=r,weight=w,A=aa))
product = s.eye(4)
for aa in A: product = product*aa
check('five singular ordered product identity',product==s.eye(4))
A.append(s.eye(4))
check('actual weighted cusp monodromy',A[0]==s.Matrix([[1,8,0,24],[0,1,0,0],[0,-6,1,-16],[0,0,0,1]]))

ext = [exterior(aa) for aa in A]
def defect(i,u,v):
    return ordered_bar(A[i]*u,A[i]*v)-ext[i]*ordered_bar(u,v)
quadratics = []
for i in range(6):
    diag=[defect(i,E[:,a],E[:,a]) for a in range(4)]
    cross={ab:defect(i,E[:,ab[0]],E[:,ab[1]]) for ab in pairs}
    for a,b in pairs: check(f'site{i} symmetric defect{a}{b}',cross[a,b]==defect(i,E[:,b],E[:,a]))
    quadratics.append((diag,cross))
def f(i,u):
    diag,cross=quadratics[i]
    out=s.zeros(6,1)
    for a in range(4): out-=diag[a]*(u[a]*(u[a]-1)/2)
    for (a,b),d in cross.items(): out-=d*u[a]*u[b]
    check(f'integral primitive evaluation {i}:{tuple(u)}',integral(out))
    return out

u=s.Matrix(s.symbols('u0:4'));v=s.Matrix(s.symbols('v0:4'))
for i in range(6):
    diag,cross=quadratics[i]
    def symbolic_f(x):
        out=s.zeros(6,1)
        for a in range(4):out-=diag[a]*x[a]*(x[a]-1)/2
        for (a,b),d in cross.items():out-=d*x[a]*x[b]
        return out
    diff=symbolic_f(u)+symbolic_f(v)-symbolic_f(u+v)-defect(i,u,v)
    check(f'site{i} full symbolic BC8 identity',all(s.expand(x)==0 for x in diff))

D = s.Matrix.hstack(*(aa-s.eye(4) for aa in A[:5]))
K,Kplus,Dsmith = integer_kernel(D,'graph differential')
check('graph kernel rank17',K.shape==(20,17))
Jraw=[]
for i in range(5):
    j=s.zeros(20,4);j[4*i:4*i+4,:]=s.eye(4);Jraw.append(j)
last=[]
for j in range(5):
    t=s.eye(4)
    for k in range(j+1,6):t=t*A[k]
    last.append(-t)
Jraw.append(s.Matrix.vstack(*last))
for i in range(6):check(f'peripheral{i} exact boundary',D*Jraw[i]==A[i]-s.eye(4))
def correction(i,u):
    if i<5:return f(i,u)
    out=s.zeros(6,1)
    for j in range(5):out-=f(j,-Jraw[5][4*j:4*j+4,:]*u)
    return out
def graph_coord(i,u):
    raw=Jraw[i]*u
    check(f'peripheral{i} cycle condition {tuple(u)}',D*raw==s.zeros(4,1))
    coords=Kplus*raw
    check(f'peripheral{i} exact integral coordinates {tuple(u)}',K*coords==raw and integral(coords))
    return coords

columns=[];origins=[]
def add(fibre,graph,origin):
    col=s.Matrix.vstack(fibre,graph)
    check('integral relation '+origin,integral(col))
    columns.append(col);origins.append(origin)
zero_graph=s.zeros(17,1)
for i in range(5):
    for j in range(6):add((ext[i]-s.eye(6))[:,j],zero_graph,f'core exterior coinvariant site{i} bivector{j}')
fix=[];vanishing=[]
for i in range(5):
    ff,fp,_=integer_kernel(A[i]-s.eye(4),f'fixed lattice site{i}')
    fix.append(ff)
    if i==0:
        # Preserve the explicitly unsaturated positive-weight kernel.
        for j in range(6):add((ext[i]-s.eye(6))[:,j],zero_graph,f'positive cap imageR bivector{j}')
        for a,b in itertools.combinations(range(ff.cols),2):
            add(wedge(ff[:,a],ff[:,b]),zero_graph,f'positive cap fixed exterior{a},{b}')
        vanishing.append(ff)
    else:
        sat=saturated_image(ext[i]-s.eye(6),f'rank-one cap fibre image site{i}')
        for j in range(sat.cols):add(sat[:,j],zero_graph,f'rank-one saturated fibre site{i} column{j}')
        vanishing.append(saturated_image(A[i]-s.eye(4),f'rank-one cap vanishing site{i}'))
    for j in range(ff.cols):
        vv=ff[:,j];add(correction(i,vv),graph_coord(i,vv),f'fixed normal site{i} vector{j}')
# D.WP ordinary e=1 is m=1 with v=-gamma, placed at the last site.
ordinary_v=-E[:,3]
for j in range(4):
    lam=E[:,j]
    add(correction(5,lam)-wedge(lam,ordinary_v),graph_coord(5,lam),f'ordinary m1 v=-gamma normal{j}')
add(correction(5,ordinary_v),graph_coord(5,ordinary_v),'ordinary affine normal')
M=s.Matrix.hstack(*columns)
S,U,V,rank=smith(M,'complete core matrix')
diag=[int(S[j,j]) for j in range(min(S.shape)) if S[j,j]]
check('complete core rank23 and sole torsion8',rank==23 and [abs(x) for x in diag]==[1]*22+[8])

z=s.Matrix([-16,8,6,16,0,6]+[0]*17)
w=U*z
q=s.zeros(M.cols,1)
for j in range(rank):
    check(f'critical Smith divisibility{j}',w[j]%S[j,j]==0)
    q[j]=w[j]/S[j,j]
for j in range(rank,M.rows):check(f'critical zero Smith row{j}',w[j]==0)
witness=V*q
check('full exact critical null chain',integral(witness) and M*witness==z)

torsion_row=U[22,:]
check('primitive fibre restriction unit',s.gcd(int(torsion_row[0]),8)==1)
mult=int(pow(int(torsion_row[0])%8,-1,8))
phi=s.Matrix([[int(mult*x)%8 for x in torsion_row]])
check('specified fibre restriction mod8',list(phi[:,:6])==[1,0,0,0,0,0])
check('closed full core character',all(int(x)%8==0 for x in phi*M))
extension=phi[:,6:]*Kplus
raw_cusp=extension*Jraw[0]
check('cusp short constants zero mod8',int(raw_cusp[0])%8==0 and int(raw_cusp[2])%8==0)
check('cusp gamma-strip constant4',int(raw_cusp[3])%8==4)
check('cusp e2-strip constant even',int(raw_cusp[1])%2==0)
adjust=next(a for a in range(8) if (int(raw_cusp[1])-6*a)%8==4)
mu=s.Matrix([[0,0,adjust,0]])
marked_extension=extension+mu*D
check('same graph cocycle under literal coboundary',marked_extension*K==phi[:,6:])
cusp=marked_extension*Jraw[0]
check('full marked cusp constants0444',list(s.Matrix([[int(x)%8 for x in cusp]]))==[0,4,0,4])
lift=s.zeros(1,20);lift[1]=6;lift[3]=17
literal_extension=marked_extension+8*lift
literal_phi=phi.copy();literal_phi[:,6:]=literal_extension*K
literal_cusp=literal_extension*Jraw[0]
check('exact printed integer strip lifts',list(literal_cusp)==[0,52,0,148])
check('literal ambient extension of core row',literal_extension*K==literal_phi[:,6:])
check('same mod8 cochain after explicit integral lift',all(int(x)%8==0 for x in literal_extension-marked_extension))
check('literal full core character remains closed',all(int(x)%8==0 for x in literal_phi*M))
negative_smith_generator=-U.inv()[:,22]
check('literal coordinate on negative Smith generator',int((literal_phi*negative_smith_generator)[0])%8==7)

# Complement's remaining vanishing lattice has the literal character
# (gamma, delta mod2), thereby fixing all component meridians (1,s).
outside=s.Matrix.hstack(*vanishing[1:])
SO,UO,VO,ro=smith(outside,'cusp exterior vertical relations')
check('cusp exterior residual cyclic2',ro==3 and [abs(int(SO[j,j])) for j in range(ro)]==[1,1,2])
detector=s.Matrix([[0,0,0,1],[0,0,1,0]])
values=detector*outside
check('actual complement character',all(x==0 for x in values[0,:]) and all(int(x)%2==0 for x in values[1,:]))
for r in range(8):
    for t in range(2):
        meridian=E[:,3]+r*E[:,0]+t*E[:,2]
        val=detector*meridian
        check(f'component meridian {r},{t}',val[0]==1 and int(val[1])%2==t)
allvan=s.Matrix.hstack(*vanishing,E[:,3])
SV,UV,VV,rv=smith(allvan,'complete primitive vanishing lattice')
check('all four fibre generators normally killed',rv==4 and all(abs(SV[j,j])==1 for j in range(4)))
ordinary_h1=s.Matrix.vstack(-ordinary_v,-s.ones(5,1))
E_h1=s.Matrix.vstack(D,s.zeros(5,D.cols)).row_join(ordinary_h1)
SE,UE,VE,re=smith(E_h1,'regular piece with ordinary cap H1')
b1E=9-re
check('finite-filled exterior first Betti number5',b1E==5)
relative_rank=8*2+4-b1E
check('relative component free rank15',relative_rank==15)
euler=2*8*2
check('absolute Betti ranks and Euler number',23-rank+relative_rank==15 and 2+2*15-euler==0)

def encode(x):
    if isinstance(x,s.MatrixBase):return [[int(y) if y.q==1 else str(y) for y in row] for row in x.tolist()]
    if isinstance(x,s.Basic):return int(x) if x.q==1 else str(x)
    raise TypeError(type(x).__name__)
out=dict(
    utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    author='GPT-6 Astra (OpenAI), ChatGPT Pro mode; no separate numeric effort setting exposed; same model family',
    exposure='After reading the printed statements/formulas and outputs; no historical program imported; frozen construction plan retained',
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    sympy_version=s.__version__,passed=len(checks),seconds=round(time.monotonic()-started,3),checks=checks,
    local_data=local_data,monodromies=A,bar_quadratics=quadratics,
    graph_differential=D,kernel=K,kernel_left_inverse=Kplus,graph_smith=Dsmith,
    peripheral_raw_maps=Jraw,fixed_lattices=fix,vanishing_lattices=vanishing,
    matrix=M,column_origins=origins,smith=S,row_map=U,column_map=V,smith_diagonal=diag,
    critical_cycle=z,critical_witness=witness,
    primitive_character=phi,raw_graph_extension=extension,raw_cusp_constants=raw_cusp,
    graph_coboundary=mu,marked_graph_extension=marked_extension,marked_cusp_constants=cusp,
    integral_lift_row=lift,literal_graph_extension=literal_extension,literal_core_character=literal_phi,
    literal_cusp_constants=literal_cusp,negative_smith_generator=negative_smith_generator,
    complement_detector=detector,complement_vanishing=outside,
    finite_filled_exterior_H1_matrix=E_h1,finite_filled_exterior_b1=b1E,
    relative_component_rank=relative_rank,absolute_b2=15,absolute_b3_free=0,Euler_characteristic=euler,
    qualification='This proves the displayed integral core quotient, null chain, literal mod8 cocycle/coboundary and component meridian marking. A distinct basis and column list from the unavailable historical program is explicitly embedded in the same bar lattice. The full geometric cap theorem is used at its printed scope. Odd torsion-cycle framing and the refined0/4 choice are not computed here.')
# Tuple-keyed bilinear data is expanded to explicit labeled records.
out['bar_quadratics']=[{'diagonal':d,'cross':[{ 'indices':list(ab),'coefficient':v} for ab,v in c.items()]} for d,c in quadratics]
target=ROOT/'code/outputs/III_OS45_core_independent.json'
target.write_text(json.dumps(out,indent=2,default=encode)+'\n')
print(json.dumps({'passed':len(checks),'matrix_shape':M.shape,'smith_diagonal':diag,'critical_witness_nonzero':[(j,int(witness[j])) for j in range(witness.rows) if witness[j]],'raw_cusp':list(raw_cusp),'coboundary':list(mu),'marked_cusp':list(cusp),'seconds':out['seconds']},default=encode))
