#!/usr/bin/env python3
"""Independent exact root, exceptional-divisor, norm and gluing checks."""
from pathlib import Path
from math import gcd
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

root=Path(__file__).resolve().parent
l=S.symbols('l',integer=True,nonnegative=True)
def scalar_zero(v):assert S.expand(v)==0
def ints(A):return [[int(x) for x in row] for row in A.tolist()]
def sn(A):
 D=smith_normal_form(A,domain=ZZ)
 return [abs(int(D[j,j])) for j in range(min(D.shape)) if D[j,j]]

# (ord f,ord g) after q=z^m,x=z^(2k)X,y=z^(3k)Y.
roots=[]
for typ,m,k,f,g,ef,eg in [
 ('IIIstar reduced',4*l+3,3*l+2,3,6,1,6*l+6),
 ('IIIstar good',4*(l+1),3*(l+1),3,6,0,6*l+6),
 ('IVstar A reduced',3*l+2,2*l+1,4,4,4*l+4,2),
 ('IVstar B reduced',3*l+2,2*l+1,3,4,l+2,2),
 ('IVstar good',3*(l+1),2*(l+1),4,4,4*l+4,0),
 ('III reduced',4*l+1,l,1,2,1,2*l+2),
 ('III good',4*(l+1),l+1,1,2,0,2*l+2),
 ('IV reduced',3*l+1,l,2,2,2*l+2,2),
 ('IV good',3*(l+1),l+1,2,2,2*l+2,0),
 ('II reduced',6*l+1,l,1,1,2*l+1,1),
 ('II good',6*(l+1),l+1,1,1,2*l+2,0)]:
 scalar_zero(f*m-4*k-ef);scalar_zero(g*m-6*k-eg)
 roots.append({'type':typ,'m':str(m),'k':str(k),'new_f':str(ef),'new_g':str(eg)})

# The common smooth refinements and exact Cartier correction at starred roots.
toric=[]
for r,rays in [(3,[(1,0),(2,1),(1,1),(1,2),(0,1)]),
               (4,[(1,0),(3,1),(2,1),(1,1),(1,2),(1,3),(0,1)])]:
 assert all(S.Matrix.hstack(S.Matrix(u),S.Matrix(v)).det()==1 for u,v in zip(rays,rays[1:]))
 minimal=[S.Matrix([S.Rational(r-j,r),S.Rational(j,r)]) for j in range(r+1)]
 assert all(S.Matrix.hstack(u,v).det()==S.Rational(1,r) for u,v in zip(minimal,minimal[1:]))
 character=S.Matrix([1,-(r-1)])
 assert ((r-1)*character[0]+character[1])%r==0
 coeff=[min(w,(r-1)*z) for w,z in rays[1:-1]]
 assert coeff==([2,1,1] if r==3 else [3,2,1,1,1])
 for w,z in rays:
  assert w-max(w-(r-1)*z,0)==min(w,(r-1)*z)
 toric.append({'r':r,'rays':rays,'exceptional_coefficients':coeff})

def contract(Q,i):
 assert Q[i,i]==-1
 ix=[j for j in range(Q.rows) if j!=i]
 return Q.extract(ix,ix)+Q.extract(ix,[i])*Q.extract([i],ix)
diagrams=[]
for name,weights,mults,seq in [
 ('good II',[-1,-6,-3,-2],[6,1,2,3],[0,2,1]),
 ('good III',[-1,-4,-4,-2],[4,1,1,2],[0,2]),
 ('good IV',[-1,-3,-3,-3],[3,1,1,1],[0])]:
 Q=S.diag(*weights)
 for j in range(1,4):Q[0,j]=Q[j,0]=1
 assert Q*S.Matrix(mults)==S.zeros(4,1)
 stages=[ints(Q)]
 for i in seq:
  Q=contract(Q,i);stages.append(ints(Q))
 expected={'good II':S.zeros(1),'good III':S.Matrix([[-2,2],[2,-2]]),
           'good IV':S.Matrix([[-2,1,1],[1,-2,1],[1,1,-2]])}[name]
 assert Q==expected
 diagrams.append({'type':name,'stages':stages,'multiplicities_before_contraction':mults})

norms=[]
for r,D in [(3,S.Matrix([[0,-1],[1,-1]])),
            (4,S.Matrix([[0,-1],[1,0]])),
            (6,S.Matrix([[1,-1],[1,0]]))]:
 assert D**r==S.eye(2)
 assert sum((D**j for j in range(r)),S.zeros(2))==S.zeros(2)
 for u in range(1,r):
  if gcd(u,r)!=1:continue
  U=(D**u-S.eye(2))*(D-S.eye(2)).inv()
  assert all(x.q==1 for x in U) and abs(U.det())==1
 norms.append({'order':r,'matrix':ints(D),'norm':[[0,0],[0,0]],
               'central_coinvariant_Smith':sn(D-S.eye(2))})

# The actual good-root mixed finite/free maps: columns eta,r,s.
mixed=[]
for label,p,A,cap in [
 ('E7 good',2,[[-7,-1,3],[0,0,1]],[0,-1,0]),
 ('E6 good',3,[[-2,2,-2],[0,0,-1]],[0,1,0]),
 ('OS47 III good',2,[[-1,-7,-1],[0,0,1]],[0,1,0]),
 ('OS56 III good',2,[[-1,-15,-1],[0,0,1]],[0,1,0]),
 ('OS56 IV good',3,[[-2,-10,-2],[0,0,1]],[0,1,0])]:
 for kap in range(-3,4):
  cr=S.Matrix([cap]);cr[0,2]=kap
  D=S.Matrix(A).col_join(-cr)
  relations=D.row_join(S.Matrix([p,0,0]))
  assert sn(relations)==[1,1,1]
 mixed.append({'type':label,'torsion_order':p,'source_map':A,
               'cap_fibre_sign':cap[1],'all_kappa_samples_pass':True})

m,n,kap=S.symbols('m n kappa',integer=True)
D1=S.Matrix([[0,1],[n,-m]])
D2=S.Matrix([[0,1],[-1,-kap]])
assert D1.det()==-n and D2.det()==1
out={'status':'PASS','root_exponents':roots,'starred_toric_maps':toric,
     'good_root_contractions':diagrams,'exact_norm_endomorphisms':norms,
     'mixed_torsion_maps':mixed,'free_MV_D1_D3':[[str(x) for x in row] for row in D1.tolist()],
     'free_MV_D2':[[str(x) for x in row] for row in D2.tolist()],
     'scope':'Independent algebraic audit of the actual constructions/topology in SC,OA,II notes; the geometric divisor and frame maps are read and audited separately.'}
(root/'additive_cap_root_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: eleven exact root substitutions, both starred toric Cartier corrections.')
print('PASS: all actual good II/III/IV contraction matrices and fibre multiplicities.')
print('PASS: exact central norm maps, primitive torsion transport and all retained-kappa mixed maps.')
