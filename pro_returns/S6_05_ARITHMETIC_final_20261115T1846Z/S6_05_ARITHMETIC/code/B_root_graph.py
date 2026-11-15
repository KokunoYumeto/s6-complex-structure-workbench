"""Aut(J) through its intrinsically defined pair of rooted extensions.
The first 144 graph vertices are roots; a colored vertex for each nonzero
inner product encodes its exact value.  A graph automorphism is precisely
an orthogonal permutation of the combined root set, which spans R^24.
Every returned generator is then checked on the original integral J.
"""
import json,sys,time
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from flint import fmpz_mat,fmpq_mat
import pynauty
ROOT=Path(__file__).resolve().parents[1]; REC=ROOT/'records'
sys.path.insert(0,str(ROOT/'code'))
from B_exact_lattices import basis,gram,dot,det,J,qmat

def get_roots(name):
 b=json.loads((REC/f'B_{name}.basis.json').read_text()); rr=[]
 for line in (REC/f'B_{name}.out').read_text().splitlines():
  if line.startswith('vector 2 '):
   a=list(map(int,line.split()[2:]));rr.append(tuple(sum(a[i]*b[i][j] for i in range(24)) for j in range(28)))
 return rr
rr=get_roots('over_2')+get_roots('over_6');assert len(set(rr))==144
assert len(basis(rr))==24
print('root span determinant',det(basis(rr)))
n=len(rr);adj={i:[] for i in range(n)};colors=defaultdict(set);colors[0]=set(range(n))
for i in range(n):
 for j in range(i):
  ip=dot(rr[i],rr[j]);assert (ip*3).denominator==1
  if not ip:continue
  k=len(adj);adj[k]=[i,j];adj[i].append(k);adj[j].append(k);colors[ip].add(k)
print('graph vertices',len(adj),'color classes',[(str(k),len(v)) for k,v in colors.items()],flush=True)
g=pynauty.Graph(len(adj),adjacency_dict=adj,vertex_coloring=list(colors.values()))
t=time.time();gg,mant,exp,orbits,norb=pynauty.autgrp(g)
print('nauty order mantissa/exponent',mant,exp,'generators',len(gg),'seconds',time.time()-t,flush=True)
perms=[p[:n] for p in gg]
# Choose 24 independent root rows.
inds=[];cur=[]
for i,r in enumerate(rr):
 if fmpz_mat(cur+[list(r)]).rank()>len(cur):inds.append(i);cur.append(list(r))
 if len(cur)==24:break
# Orthogonal coordinates relative to this root basis: J = C*cur.
c=qmat(gram(cur)).inv()*fmpq_mat(cur)
Jmat=fmpq_mat([list(x) for x in J]);coords=Jmat*c.transpose()/144
assert coords*fmpq_mat(cur)==Jmat
checks=[];mats=[]
for p in perms:
 images=fmpq_mat([list(rr[p[i]]) for i in inds]);im=coords*images
 vals=[[F(str(im[i,j])) for j in range(28)] for i in range(24)]
 integ=all(x.denominator==1 for row in vals for x in row)
 ok=integ and basis([[int(x) for x in row] for row in vals])==J
 checks.append(ok)
 if ok:
  # Matrix of the isometry in the J basis, exact integer entries.
  jd=qmat(gram(J)).inv()*Jmat
  T=im*jd.transpose()/144
  assert all(F(str(T[i,j])).denominator==1 for i in range(24) for j in range(24))
  mats.append([[int(T[i,j]) for j in range(24)] for i in range(24)])
print('all graph generators preserve J',all(checks),'checks',checks,flush=True)
(REC/'B_root_graph_data.json').write_text(json.dumps({'roots':rr,'permutations':perms,'matrices_on_J':mats,'checks':checks,'nauty_order':[mant,exp]}))
def gapperm(p):
 seen=set();cycles=[]
 for i in range(len(p)):
  if i in seen:continue
  cy=[];j=i
  while j not in seen:seen.add(j);cy.append(j+1);j=p[j]
  if len(cy)>1:cycles.append('('+','.join(map(str,cy))+')')
 return ''.join(cycles) or '()'
gap='G:=Group(['+','.join(map(gapperm,perms))+']);;\nPrint("root_graph_group_order ",Size(G),"\\n");\nPrint("structure ",StructureDescription(G),"\\n");\n'
(ROOT/'code'/'B_root_graph_order.g').write_text(gap)
