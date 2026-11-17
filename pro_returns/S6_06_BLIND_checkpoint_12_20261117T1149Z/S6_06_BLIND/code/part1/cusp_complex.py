"""Exact orbit-filtration integer complexes for the periodic Kuhn central fibre.
Cells are translation classes of increasing simplices in the Freudenthal
triangulation of Z^3. The output includes every codimension-one incidence,
all lattice quotient projections, every differential, and Smith decompositions.
"""
from itertools import combinations, permutations, product
from pathlib import Path
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.polys.domains import ZZ

zero=(0,0,0);unit=[tuple(int(i==j) for i in range(3)) for j in range(3)]
def normalize(vs):
 vs=tuple(sorted(vs,key=lambda v:(sum(v),v)))
 a=vs[0]
 return tuple(tuple(v[i]-a[i] for i in range(3)) for v in vs)
cells=[set() for _ in range(4)]
for perm in permutations(range(3)):
 v=[0,0,0];tet=[tuple(v)]
 for i in perm:
  v[i]=1;tet.append(tuple(v))
 for k in range(4):
  for vs in combinations(tet,k+1):cells[k].add(normalize(vs))
cells=[sorted(c) for c in cells]
Q={};S={}
for p in range(4):
 for i,c in enumerate(cells[p]):
  tang=s.Matrix.hstack(*[s.Matrix(v) for v in c[1:]]) if p else s.zeros(3,0)
  for js in combinations(range(3),3-p):
   mat=tang.row_join(s.eye(3)[:,list(js)])
   if abs(mat.det())==1:break
  else:raise AssertionError(c)
  Q[p,i]=mat.inv()[p:,:]
  S[p,i]=mat[:,p:]

def wedge(m,q):
 rows=list(combinations(range(m.rows),q));cols=list(combinations(range(m.cols),q))
 return s.Matrix(len(rows),len(cols),lambda i,j:m.extract(rows[i],cols[j]).det())

def snf(m):
 if min(m.shape)==0:return s.zeros(*m.shape),s.eye(m.rows),s.eye(m.cols)
 d,u,v=smith_normal_decomp(DomainMatrix.from_Matrix(m).convert_to(ZZ))
 d,u,v=d.to_Matrix(),u.to_Matrix(),v.to_Matrix()
 assert u*m*v==d and abs(u.det())==abs(v.det())==1
 return d,u,v

def homology(a,b):
 # a is outgoing, b incoming at the same cochain term.
 assert a*b==s.zeros(a.rows,b.cols)
 d,u,v=snf(a);rank=a.rank();n=a.cols
 kb=v.inv()*b
 assert kb[:rank,:]==s.zeros(rank,b.cols)
 rel=kb[rank:,:];diag,_,_=snf(rel)
 tors=[abs(int(diag[i,i])) for i in range(min(diag.shape)) if abs(diag[i,i])>1]
 free=n-rank-rel.rank()
 return {'free':free,'torsion':tors,'kernel_basis':v[:,rank:].tolist(),'incoming_in_kernel_basis':rel.tolist()}

D={};data={'cells':cells,'quotients':{},'incidences':[],'differentials':{},'homology':{}}
for p in range(4):
 for i,c in enumerate(cells[p]):
  data['quotients'][f'{p}.{i}']={'Q':Q[p,i].tolist(),'S':S[p,i].tolist()}
for q in range(4):
 dims={p:len(cells[p])*s.binomial(3-p,q) for p in range(4)}
 for p in range(3):
  a=s.zeros(dims[p+1],dims[p]);dw=int(s.binomial(2-p,q));sw=int(s.binomial(3-p,q))
  for j,coface in enumerate(cells[p+1]):
   for k in range(p+2):
    face=normalize(coface[:k]+coface[k+1:]);i=cells[p].index(face)
    P=Q[p+1,j]*S[p,i];w=wedge(P,q)
    a[j*dw:(j+1)*dw,i*sw:(i+1)*sw]+=(-1)**k*w
    if q==0:data['incidences'].append({'face':f'{p}.{i}','coface':f'{p+1}.{j}','omit':k,'sign':(-1)**k,'projection':P.tolist()})
  D[p,q]=a;data['differentials'][f'd{p}_q{q}']=a.tolist()
 for p in range(4):
  a=D[p,q] if p<3 else s.zeros(0,dims[p]);b=D[p-1,q] if p else s.zeros(dims[p],0)
  data['homology'][f'p{p}_q{q}']=homology(a,b)
print('Cell counts:',[len(x) for x in cells]);print('Codimension-one incidences:',len(data['incidences']))
for k,v in data['quotients'].items():print('quotient',k,v)
for row in data['incidences']:print('incidence',row)
for k,m in D.items():print('D',k,m.shape,m)
betti=[0]*7;torsions=[[] for _ in range(7)]
for p in range(4):
 for q in range(4):
  h=data['homology'][f'p{p}_q{q}'];k=3-p+q
  if k<7:betti[k]+=h['free'];torsions[k]+=h['torsion']
  print('E2',p,q,'degree',k,'free',h['free'],'torsion',h['torsion'])
print('E2 total Betti numbers:',betti)
print('E2 torsion by total degree:',torsions)
print('Euler:',sum((-1)**i*b for i,b in enumerate(betti)))
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2,default=int))
