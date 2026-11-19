"""All zero-multidegree original additive caps on the natural candidate rows.
Exact component-orbit defects, full boundary lattices, and scalar-circle checks.
"""
from pathlib import Path
import json,itertools,sympy as s
from math import gcd,lcm
from collections import Counter
from manifolds_rankone_families import decomp,ikernel,wedge
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'manifolds_all_finite_logs.json').read_text())['rows']
monos=json.loads((ROOT/'manifolds_sphere_monodromies.json').read_text())['rows']
initial=json.loads((ROOT/'manifolds_sphere_initial.json').read_text())['candidates']
key=lambda r:(r['entry'],r['profile'],r['a'],r['b'],r['zero_index'])
M={key(r):r for r in monos};I={key(r):r for r in initial}
def group(A):
 D,U,V,r=decomp(A);return A.rows-r,[int(abs(D[j,j])) for j in range(r) if abs(D[j,j])>1]
def ismult(k):return k.startswith('I') and k[1:].isdigit()
locals=[];patterns=[];scalar=0
for row in rows:
 K=key(row);old=I[K];mm=M[K];choices=[];sites=[];rho={}
 for j,(loc,geom) in enumerate(zip(row['local'],old['local'])):
  typ=loc['type'];P0=geom['P_component']==0
  if j==row['zero_index']:continue
  if P0:
   A=s.Matrix(mm['local'][j]['matrix']);assert group(A-s.eye(4))[1]==[] and group(wedge(A)-s.eye(6))[1]==[]
   T=s.Matrix(geom['Q_pullback']);E=s.Matrix(geom['component_intersection']);n=T.rows
   perm=[next(i for i in range(n) if T[i,j]) for j in range(n)]
   seen=set();orbits=[]
   for v in range(n):
    if v in seen:continue
    o=[];w=v
    while w not in seen:seen.add(w);o.append(w);w=perm[w]
    orbits.append(o)
   rr=len(orbits);assert rr==geom['component_orbits'];rho[j]=rr
   O=s.zeros(n,rr);R=s.zeros(n,rr)
   for h,o in enumerate(orbits):
    for t in o:O[t,h]=1
    R[o[0],h]=1
   folded=O.T*E*R
   assert folded.rank()==rr-1
   F=ikernel(A-s.eye(4));g=gcd(*map(int,list(F[3,:])))
   order=lcm(*[len(o) for o in orbits])
   if not ismult(typ):assert g==order
   else:assert rr==1
   locals.append(dict(entry=row['entry'],profile=row['profile'],a=row['a'],b=row['b'],zero_index=row['zero_index'],
       site=j,type=typ,orbits=orbits,rho=rr,component_order=order,fixed_gamma_index=g,
       folded_intersection=folded.tolist(),defect=rr-1))
  if not ismult(typ):
   opts=[]
   if 'q' in loc:opts.append('log')
   if P0:opts.append('original')
   sites.append(j);choices.append(opts)
 for cc in itertools.product(*choices):
  orig=[j for j,c in zip(sites,cc) if c=='original'];fi=[j for j,c in zip(sites,cc) if c=='log']
  D=sum(rho[j]-1 for j in orig)
  rec={k:row[k] for k in ['entry','profile','a','b','zero_type','zero_index']}
  rec.update(additive_choices=list(zip(sites,cc)),original_indices=orig,finite_indices=fi,
             defect=D,finite_gamma_indices=[row['local'][j]['gamma_index'] for j in fi])
  patterns.append(rec)
  if row['b']==1 and all(row['local'][j]['gamma_index']==1 for j in fi):
   for j,loc in enumerate(row['local']):
    if j==row['zero_index'] or not ismult(loc['type']):continue
    assert old['local'][j]['P_component']==0 and old['local'][j]['component_orbits']==1
    A=s.Matrix(mm['local'][j]['matrix']);D0,U,V,r=decomp(A-s.eye(4));assert r==1
    van=U.inv()[:,:1];DD,_,_,rr=decomp(van.row_join(s.eye(4)[:,2]));assert rr==2 and abs(DD[0,0])==abs(DD[1,1])==1
    scalar+=1
print('Zero-degree original local certificates:',len(locals),flush=True)
print('Nonminimal types and orbit counts:',dict(Counter((v['type'],v['rho']) for v in locals if v['defect'])),flush=True)
print('All additive patterns:',len(patterns),'initial rows:',len(set(key(p) for p in patterns)),flush=True)
print('Patterns with a positive original component defect:',sum(p['defect']>0 for p in patterns),flush=True)
print('Scalar-circle checks in b1 potentially simply-connected patterns:',scalar,flush=True)
print('b1 free defects:',sorted(set(p['defect'] for p in patterns if p['b']==1 and all(g==1 for g in p['finite_gamma_indices']))),flush=True)
(ROOT/'manifolds_original_zero_degree.json').write_text(json.dumps(dict(scope=__doc__,local=locals,patterns=patterns,scalar_checks=scalar),indent=2,default=int)+'\n')
