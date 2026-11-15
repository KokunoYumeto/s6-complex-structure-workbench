"""Every Weyl d-neighbour, d|h, for all23 rooted Niemeier lattices.
All arithmetic, neighbor bases, and root enumeration is exact.  The
catalogue matrix is certified by positivity, evenness, determinant and
the complete root system, not assumed from its filename.
"""
from pathlib import Path
from fractions import Fraction as F
import json,csv,time
from flint import fmpz_mat,fmpq_mat
from B_gram_utils import *
REC=ROOT/'records'/'B_all_neighbours';REC.mkdir(exist_ok=True)
catalog=json.loads((ROOT/'records'/'B_catalogue'/'grams.json').read_text())
table=[]
for name,g in catalog.items():
 n=len(g);G=fmpz_mat(g)
 assert n==24 and G.det()==1 and all(g[i][i]%2==0 for i in range(n))
 roots=[v for norm,v in enumerate_gram(g,2,REC/name) if norm==2]
 h=len(roots)//24;assert 24*h==len(roots)
 typ=root_system(g,roots)
 pos=[v for v in roots if next(x for x in v if x)!=0 and next(x for x in v if x)>0]
 rho=[F(sum(v[i] for v in pos),2) for i in range(n)];assert all(x.denominator==1 for x in rho);rho=list(map(int,rho))
 pair=lambda a,b:sum(a[i]*g[i][j]*b[j] for i in range(n) for j in range(n))
 assert pair(rho,rho)==2*h*(h+1)
 alpha=next(v for v in roots if pair(rho,v)==1)
 heights=[sum(rho[i]*g[i][j] for i in range(n)) for j in range(n)]
 print(name,'root_system',typ,'h',h,flush=True)
 for d in range(1,h+1):
  if h%d:continue
  # d times an ambient lattice basis for the neighbour.
  gens=[[d*d*x for x in alpha]]
  gens += [[d*(int(i==j)-heights[i]*alpha[j]) for j in range(n)] for i in range(n)]
  gens += [[rho[j]-h*alpha[j] for j in range(n)]]
  B=fmpz_mat(hnf(gens));assert B.nrows()==24
  GN=qrows(fmpq_mat(B*G*B.transpose())/(d*d));assert all(x.denominator==1 for row in GN for x in row)
  gn=[[int(x) for x in row] for row in GN]
  assert fmpz_mat(gn).det()==1 and all(gn[i][i]%2==0 for i in range(n))
  rt=[v for norm,v in enumerate_gram(gn,2,REC/f'{name}_d{d}') if norm==2]
  nt=root_system(gn,rt);nh=len(rt)//24 if rt else 1
  okay=nh==h//d
  row={'Niemeier':typ,'h':h,'d':d,'neighbour':nt,'neighbour_h':nh,'prediction_h':h//d,'prediction_correct':okay}
  table.append(row);print(' ',d,nt,'h_convention',nh,'prediction',okay,flush=True)
  (REC/f'{name}_d{d}.json').write_text(json.dumps({'original_gram':g,'rho':rho,'alpha':alpha,'basis_scaled_by_d':matrows(B),'gram':gn,'root_coordinates':rt,'type':nt}))
out=ROOT/'records'/'B_all_neighbours.csv'
with out.open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(table[0]));w.writeheader();w.writerows(table)
print('cases',len(table),'exceptions',sum(not r['prediction_correct'] for r in table),flush=True)
