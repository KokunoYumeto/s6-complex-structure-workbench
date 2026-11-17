#!/usr/bin/env python3
"""Exact starred component marking and all 21 generic source-factor filters."""
from pathlib import Path
import math,json
import sympy as s
root=Path(__file__).resolve().parents[2]
profiles=[
 (43,2,'III*+3I1',[],0,3),(43,2,'III*+II+I1',[],0,1),
 (45,8,'I8+4I1',[8],0,4),(45,8,'I8+II+2I1',[8],0,2),
 (46,4,'I3*+3I1',[],3,3),(46,4,'I3*+II+I1',[],3,1),
 (47,14,'I7+I2+3I1',[7,2],0,3),(47,14,'I7+I2+II+I1',[7,2],0,1),
 (47,14,'I7+III+2I1',[7],0,2),
 (49,6,'IV*+I2+2I1',[2],0,2),(49,6,'IV*+I2+II',[2],0,0),
 (49,6,'IV*+III+I1',[],0,1),
 (50,12,'I1*+I3+2I1',[3],1,2),(50,12,'I1*+I3+II',[3],1,0),
 (50,12,'I1*+IV+I1',[],1,1),
 (55,20,'I5+I4+3I1',[5,4],0,3),(55,20,'I5+I4+II+I1',[5,4],0,1),
 (56,30,'I5+I3+I2+2I1',[5,3,2],0,2),
 (56,30,'I5+I3+I2+II',[5,3,2],0,0),
 (56,30,'I5+I3+III+I1',[5,3],0,1),
 (56,30,'I5+IV+I2+I1',[5,2],0,1)]
records=[]
for os,d,name,mult,star,i1 in profiles:
 pairs=[]
 for a in range(1,d+1):
  if d%a:continue
  b=d//a
  if not i1:continue
  if any(a%N or math.gcd(N,b)!=1 for N in mult):continue
  if star and (star!=1 or a%2 or b%4!=2):continue
  pairs.append([a,b])
 records.append(dict(os=os,height_denominator=d,profile=name,
                     multiplicative_indices=mult,star_index=star,I1_count=i1,
                     remaining_pairs=pairs))
assert len(profiles)==21
assert sum(bool(r['remaining_pairs']) for r in records)==16
assert sum(len(r['remaining_pairs']) for r in records)==26
graphs=[]
for star in (1,3):
 labels=[f'C{j}' for j in range(star+1)]+['L0','L1','R0','R1']
 ix={v:i for i,v in enumerate(labels)};B=-2*s.eye(len(labels))
 edges=[(f'C{j}',f'C{j+1}') for j in range(star)]
 edges += [('C0','L0'),('C0','L1'),(f'C{star}','R0'),(f'C{star}','R1')]
 for v,w in edges:B[ix[v],ix[w]]=B[ix[w],ix[v]]=1
 multiplicities=s.Matrix([2]*(star+1)+[1]*4)
 assert B*multiplicities==s.zeros(len(labels),1)
 keep=[j for j in range(len(labels)) if j!=ix['L0']]
 Cartan=-B.extract(keep,keep);inverse=Cartan.inv()
 assert inverse[keep.index(ix['L1']),keep.index(ix['L1'])]==1
 for leaf in ('R0','R1'):
  assert inverse[keep.index(ix[leaf]),keep.index(ix[leaf])]==s.Rational(star+4,4)
 entry=dict(star_index=star,labels=labels,
            intersection_matrix=[list(B.row(i)) for i in range(len(labels))],
            multiplicities=list(multiplicities),
            inverse_cartan=[list(inverse.row(i)) for i in range(len(keep))],
            quadratic_generator_component=star)
 if star==1:
  e=lambda label:s.eye(len(labels))[:,ix[label]]
  corrected=e('L1')-e('L0')-B*e('L0')
  assert corrected==e('L0')+e('L1')-e('C0')
  perm=list(range(len(labels)))
  for v,w in [('L0','L1'),('R0','R1')]:perm[ix[v]],perm[ix[w]]=ix[w],ix[v]
  P=s.zeros(len(labels))
  for j,k in enumerate(perm):P[k,j]=1
  assert P*corrected==corrected
  entry.update(translation_order_two_matrix=[list(P.row(i)) for i in range(len(labels))],
               vertical_divisor=list(-e('L0')),corrected_degree_vector=list(corrected))
 graphs.append(entry)
out=dict(status='PASS',proof='P3K.21',source_profiles=records,
         retained_profile_count=16,retained_generic_pair_count=26,
         starred_graph_certificates=graphs,
         scope='Exact necessary source-factor reduction and literal corrected Hom data; remaining cap tuples are not declared sphere tuples by this code.')
(root/'code/part3_fourfold/source_reduction.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print('PASS: 21 profiles -> 16 retained profiles / 26 generic pairs; affine D5,D7 inverse matrices and the row50 vertical correction verified.')
