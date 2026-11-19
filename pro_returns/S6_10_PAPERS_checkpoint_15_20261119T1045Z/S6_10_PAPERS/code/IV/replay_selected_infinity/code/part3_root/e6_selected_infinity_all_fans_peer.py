#!/usr/bin/env python3
"""Independent literal-matrix checks of the full IF prism/witness data."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S

R=Path(__file__).resolve().parents[2]
src=R/'notes/part3_e6_selected_infinity_all_fans_working.md'
inp=R/'code/part3_fourfold/e6_selected_infinity_all_fans.json'
jdata=json.loads(inp.read_text());checks=[]
def eq(name,e):
    z=S.factor(S.together(e))
    if z!=0:raise AssertionError((name,z))
    checks.append(name)
def mat(name,M):
    for i in range(M.rows):
        for j in range(M.cols):eq(f'{name}[{i},{j}]',M[i,j])

q0=S.Matrix([[1,-1],[0,1]]);q1=S.Matrix([[1,0],[-1,1]])
W=S.diag(-4,0);t=-4
vs=S.symbols('v00 v01 v02 v11 v12 v22 d0 d1 d2')
Vsym=S.Matrix([[vs[0],vs[1],vs[2]],[vs[1],vs[3],vs[4]],[vs[2],vs[4],vs[5]]])
dsym=S.Matrix(vs[6:9])
eye=S.eye(3)
def local(P):
    B=2*P.inv()*W*P
    ell=[B[1,1]-B[1,0],B[0,0]-B[0,1],B[1,1]]
    x,y=P.inv()[:,1];w=[x,y,-x-y];d=[-x-2*y,-2*x-y,x-y]
    I=[t*w[i]+d[i]*(ell[i]-t) for i in range(3)]
    J=[t*w[i]-d[i]*(ell[i]-t) for i in range(3)]
    return w,I,J
def solve(P,c,e):
    w,I,J=local(P);eqs=[]
    for i in [1,2]:
        v=Vsym*(w[i]*eye[:,i]-w[0]*eye[:,0])-(I[i]*eye[:,i]-I[0]*eye[:,0])
        eqs.extend(list(v));eqs.append(w[i]*dsym[i]-w[0]*dsym[0]-(J[i]-J[0]))
    eqs.extend([Vsym[2,2]-c,dsym[2]-e])
    A,b=S.linear_eq_to_matrix(eqs,vs)
    assert A.rank()==9 and A.row_join(b).rank()==9
    checks.append('fresh rank-nine and compatible prism')
    values=list(S.linsolve((A,b),vs))[0]
    assert all(z.is_Integer for z in values)
    checks.append('fresh complete prism integral')
    sol=dict(zip(vs,values));return Vsym.subs(sol),dsym.subs(sol)

# Each witness is recalculated from its literal word without importing either
# fan implementation or its solved target systems.
witnesses=[]
for entry in jdata['witness_data']['witnesses']:
    jj=entry['vertical_index'];P=S.Matrix([[1,0],[jj,1]])
    V=S.Matrix([[24*jj*(jj-1),8-16*jj,16*jj-8],[8-16*jj,0,0],[16*jj-8,0,0]])
    d=S.Matrix([-24-24*jj*(jj-1),16*jj-16,-16*jj])
    total=S.Integer(-1-2*jj*(jj-1))
    for h,i in enumerate(entry['word']):
        oldc=V[i,i];olde=d[i];step=(olde-oldc)/4
        assert step.is_Integer
        checks.append('actual single-loop right integer')
        P=P*(q0 if i==0 else q1)
        V,d=solve(P,oldc,2*oldc-olde);total+=step
        eq('inverse right degree',(d[2]-V[2,2])/4+step)
        saved=entry['steps'][h]
        mat('all fresh V entries',V-S.Matrix(saved['variation']))
        mat('all fresh stable entries',d-S.Matrix(saved['derivative']))
        eq('each full integer path',total-saved['integer_sum'])
    mat('literal complete basis word',P-S.Matrix(2,2,entry['canonical_basis']))
    eq('final exact path',total-entry['integer_path_sum'])
    eq('final sphere residue',int(total)%28-entry['physical_class_mod28'])
    witnesses.append({'residue':int(total)%28,'basis':list(map(int,P)),
                      'word':entry['word'],'integer':int(total)})
assert sorted(v['residue'] for v in witnesses)==list(range(1,28,2))
checks.append('all fourteen actual odd witnesses')

# Algebraic affine morphism, including the first selected inverse convention.
x,y=S.symbols('x y',nonzero=True);D=-x*y*(x+y);N=x*x+x*y+y*y
for i,(xx,yy) in enumerate([(x+y,y),(x,x+y)]):
    DD=-xx*yy*(xx+yy);NN=xx*xx+xx*yy+yy*yy
    eq('homogeneous target stable constant',DD/(-xx-yy)+D/(x,y)[i])
    eq('full quadratic path difference',NN-N+2*D/(x,y)[i])
for xx,yy in [(0,1),(1,0),(1,1)]:
    eq('primitive mod-two norm',S.Mod(xx*xx+xx*yy+yy*yy,2)-1)
jj=S.symbols('j',integer=True)
mat('symbolic vertical winding',2*S.Matrix([[1,0],[jj,1]]).inv()*W*S.Matrix([[1,0],[jj,1]])-S.Matrix([[-8,0],[8*jj,0]]))
mu=2;nu=-6-12*jj*(jj-1)
eq('native-to-physical cubic',mu+nu-(-4-12*jj*(jj-1)))
eq('native-to-physical linear',4*mu-8)
eq('vertical exact index',(4*(mu+nu)-4*mu)/24-(-1-2*jj*(jj-1)))
eq('vertical full endpoint reflection',(-4-12*jj*(jj-1))-(-4-12*(1-jj)*(-jj)))

# Exact full-coefficient native chart products and normal determinants.
A11,A12,A21,A22,a,b,c,u,v,w=S.symbols('A11 A12 A21 A22 a b c u v w',nonzero=True)
for coords in [(A11*A21*b*c,a*b/A21,1/(A11*b)),
               (A12*A22*b*c,1/(A22*c),a*c/A12),(1/a,a*b,a*c)]:
    eq('literal adjacent source height',S.prod(coords)-a*b*c)
for coords in [(A11*w,A21*v,u/(A11*A21)),
               (A22*v,A12*w,u/(A12*A22)),(u,v,w)]:
    eq('literal second source height',S.prod(coords)-u*v*w)
for Dm in [S.diag(A22/A21,A11*A21),S.diag(A11/A12,A12*A22),S.diag(A22,A11)]:
    eq('complete normal determinant',Dm.det()-A11*A22)

out={'status':'PASS','checks':len(checks),'utc':datetime.now(timezone.utc).isoformat(),
 'source':str(src.relative_to(R)),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'input':str(inp.relative_to(R)),'input_sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),
 'identities':checks,'fresh_witnesses':witnesses,
 'scope':'Independent rational linear solves for every complete nine-variable prism along all14 actual witness paths; exact original-loop right degrees and integer returns, symbolic affine morphism identities, full coefficient products and vertical pair/reflection. Full geometric IF.1--7 root read is separately recorded.'}
dest=R/'code/part3_root/e6_selected_infinity_all_fans_peer.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','checks','source_sha256','input_sha256','fresh_witnesses']},indent=2))
