"""A1^24 flag stabilizer: M24 orbits of ternary colour partitions."""
from pathlib import Path
from itertools import combinations
import json, numpy as np
from mmgroup import mat24
from sympy.combinatorics import Permutation,PermutationGroup
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'records'
perms=[Permutation(mat24.m24num_to_perm(i)) for i in [123456789,98765432,135791113]]
G=PermutationGroup(perms);assert int(G.order())==244823040
pg=[p.array_form for p in perms]
def table(p):return [[sum(1<<p[8*k+j] for j in range(8) if (x>>j)&1) for x in range(256)] for k in range(3)]
tabs=[table(p) for p in pg]
def act(x,t):return t[0][x&255]|t[1][(x>>8)&255]|t[2][x>>16]
def orbit(a):
 masks=[a];idx={a:0};tp=[list(range(24))];edges=[]
 for x in masks:
  i=idx[x];ee=[]
  for p,t in zip(pg,tabs):
   y=act(x,t)
   if y not in idx:idx[y]=len(masks);masks.append(y);tp.append([p[j] for j in tp[i]])
   ee.append(idx[y])
  edges.append(ee)
 sg=[];sub=PermutationGroup([Permutation(list(range(24)))]);target=244823040//len(masks)
 for i,ee in enumerate(edges):
  for gi,j in enumerate(ee):
   a=tp[i];b=[0]*24
   for k,x in enumerate(tp[j]):b[x]=k
   p=Permutation([b[pg[gi][a[k]]] for k in range(24)])
   if sub.contains(p):continue
   sg.append(p);sub=PermutationGroup(sg)
   if sub.order()==target:break
  if sub.order()==target:break
 assert sub.order()==target
 return masks,tp,sg
strata=[];sixseen=set()
for wt in [0,3,6]:
 for aa in combinations(range(24),wt):
  a=sum(1<<i for i in aa)
  if wt==6 and a in sixseen:continue
  masks,tp,sg=orbit(a)
  if wt==6:sixseen.update(masks)
  n=len(strata);comp=[i for i in range(24) if not(a>>i)&1];ci={j:i for i,j in enumerate(comp)}
  gg=[[ci[p(i)] for i in comp] for p in sg]
  weights={0:[3,6,9,12],3:[3,6,9],6:[6,9]}[wt]
  with (REC/f'B_A1_stratum_{n}.in').open('w') as f:
   f.write(f'{len(comp)} {len(gg)} {len(weights)}\n'+' '.join(map(str,weights))+'\n')
   for p in gg:f.write(' '.join(map(str,p))+'\n')
  np.savez_compressed(REC/f'B_A1_transversal_{n}.npz',masks=np.array(masks,dtype=np.uint32),perms=np.array(tp,dtype=np.uint8))
  strata.append({'A':a,'A_weight':wt,'A_orbit':len(masks),'A_stabilizer':244823040//len(masks),'complement':comp,'generators':gg,'full_coordinate_generators':[p.array_form for p in sg],'weights':weights})
  print('stratum',n,'A',hex(a),'weight',wt,'orbit',len(masks),'stabilizer',244823040//len(masks),'generators',len(gg),flush=True)
  if wt!=6:break
assert len(strata)==4 and len(sixseen)==134596
(REC/'B_A1_setup.json').write_text(json.dumps({'M24_generators':pg,'strata':strata}))
