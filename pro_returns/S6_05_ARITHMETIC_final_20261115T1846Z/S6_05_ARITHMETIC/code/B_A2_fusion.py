"""Fuse A2-marked flag orbits by exact isometries of marked Niemeier lattices.

Every change of mark is checked to preserve the Leech lattice.  Canonical
Golay code graphs provide isometries, not just matching invariants.
"""
from B_global_lattice import *
import pynauty
from sympy.combinatorics import Permutation
D=json.loads((REC/'B_A2_strata_setup.json').read_text());MODEL=model_A2();Y=np.array(D['Y_basis'],dtype=np.int64);C=np.array(D['C'],dtype=np.int64);cp=D['C_pivots'];_,yp=rr(Y);Yi=inv(Y[:,yp]);rho=np.array(D['rho_N_mod3']);rj=next(i for i,x in enumerate(rho) if x)

def graphcode(C):
 code=[tuple((np.array(a,dtype=np.int64)@C%3).tolist()) for a in product(range(3),repeat=6)]
 adj={i:[i^1] for i in range(24)}
 for c in code:
  if not any(c):continue
  k=len(adj);adj[k]=[2*i+int(x==2) for i,x in enumerate(c) if x]
  for j in adj[k]:adj[j].append(k)
 g=pynauty.Graph(len(adj),adjacency_dict=adj,vertex_coloring=[set(range(24)),set(range(24,len(adj)))])
 return code,pynauty.canon_label(g)
fixedcode,fixedlab=graphcode(C);fixedset=set(fixedcode)
def monoT(p):
 T=fmpq_mat(24,24)
 for i in range(12):
  j=p[2*i]//2;a=[[0,1],[1,0]] if p[2*i]%2 else [[1,0],[0,1]]
  for z in range(2):
   for w in range(2):T[2*i+z,2*j+w]=a[z][w]
 return T

def iso_code(Cnew):
 code,lab=graphcode(Cnew);p=[0]*len(lab)
 for a,b in zip(lab,fixedlab):p[a]=b
 p=p[:24];assert all(p[i^1]==p[i]^1 for i in range(24))
 for c in code:
  d=[0]*12
  for i,x in enumerate(c):d[p[2*i]//2]=x*(1 if p[2*i]%2==0 else -1)%3
  assert tuple(d) in fixedset
 return monoT(p)

# Transports of all codewords to the four fixed representatives.
pg=D['monomial_generators'];trans={}
def actc(c,p):
 a=[0]*12
 for i,x in enumerate(c):a[p[2*i]//2]=x*(1 if p[2*i]%2==0 else -1)%3
 return tuple(a)
for s,sd in enumerate(D['strata']):
 c=tuple(sd['c']);seen={c:list(range(24))};todo=[c]
 for c in todo:
  t=seen[c]
  for p in pg:
   d=actc(c,p)
   if d not in seen:seen[d]=[p[t[i]] for i in range(24)];todo.append(d)
 for c,t in seen.items():
  ti=[0]*24
  for i,j in enumerate(t):ti[j]=i
  # A root-coordinate map becomes an N-coordinate map by R^{-1} T R.
  TN=MODEL.R.inv()*monoT(ti)*MODEL.R;T=np.array(ints(TN),dtype=np.int64)%3
  trans[c]=(s,T)
assert len(trans)==729
maps=[orbit_map(f'B_A2_stratum_{s}.bin') for s in range(4)]
def key_from_Nrow(x):
 a=np.array(ints(x)[0],dtype=np.int64)%3
 c=tuple((a@np.array(D['N_code_map'])%3@C%3).tolist());s,T=trans[c]
 a=a@T%3;a=(a-a[rj]*pow(int(rho[rj]),-1,3)*rho)%3;z=a[yp]@Yi%3
 assert np.array_equal(z@Y%3,a)
 assert z[16:].tolist()==D['strata'][s]['c_coeff']
 num=sum(int(z[i])*3**i for i in range(16));oid=int(maps[s][num]);assert oid>0 and not(s==0 and num==0)
 return (s,oid)

def mark_isometry(ext,source=MODEL):
 B=qmat(ext['basis']);rrs=fmpq_mat(ext['roots']);roots=rrs*B;rg=ints(roots*source.G*roots.transpose());bl=B*source.Li
 col=next(j for j in range(24) if any(F(str(bl[i,j])).denominator!=1 for i in range(24)))
 ell=[int(3*F(str(bl[i,col])))%3 for i in range(24)];re=[sum(ext['roots'][i][j]*ell[j] for j in range(24))%3 for i in range(len(ext['roots']))]
 A=[];seen=set();rv=qrows(roots)
 for i in range(len(rv)):
  if i in seen:continue
  comp={j for j in range(len(rv)) if rg[i][j]};assert len(comp)==6;seen|=comp
  b=next(j for j in sorted(comp) if re[j]==1);g=next(j for j in sorted(comp) if re[j]==1 and rg[b][j]==-1);A +=[rv[b],rv[g]]
 A=qmat(A);AI=A.inv();coords=B*AI;cr=[[int(3*F(str(coords[i,2*j+1])))%3 for j in range(12)] for i in range(24)];Cn,_=rr(cr);assert Cn.shape==(6,12)
 rh=qmat([[sum(row[j] for row in qrows(A)) for j in range(24)]]);lp=[r[0] for r in ints(B*source.G*rh.transpose())];rhs=[(lp[i]-ell[i])%3 for i in range(24)]
 aug,pp=rr(np.column_stack([cr,rhs]));assert len(pp)==6 and 12 not in pp
 z=[0]*12
 for row,j in zip(aug,pp):z[j]=int(row[-1])
 rot=fmpq_mat([[int(i==j) for j in range(24)] for i in range(24)]);r=fmpq_mat([[0,1],[-1,-1]])
 for i,k in enumerate(z):
  a=r**k
  for j in range(2):
   for l in range(2):rot[2*i+j,2*i+l]=a[j,l]
 T=AI*rot*iso_code(Cn)*MODEL.R
 assert T*MODEL.G*T.transpose()==source.G
 assert span(qrows(source.L*T))==span(qrows(MODEL.L))
 assert span(qrows(B*T))==MODEL.N
 return T

if __name__=='__main__':
 flags=json.loads((REC/'B_A2_flags.json').read_text());keys=[(r['stratum'],r['orbit_id']) for r in flags];kset=set(keys);parent={k:k for k in keys};links=[]
 def find(k):
  while parent[k]!=k:parent[k]=parent[parent[k]];k=parent[k]
  return k
 def union(a,b):
  a,b=find(a),find(b)
  if a!=b:parent[max(a,b)]=min(a,b)
 for k in keys:
  dat=json.loads((REC/'B_A2_flags'/f'{k[0]}_{k[1]}.json').read_text());y=qmat([dat['y']]);fused=[]
  for ext in dat['extensions']:
   if ext['L_intersection_index']!=3 or ext['root_system']!='12A2':continue
   T=mark_isometry(ext)
   for x in [MODEL.v,y]:
    xx=x*T
    # Detect a nonzero quotient vector modulo (3N+rho).
    a=np.array(ints(xx)[0],dtype=np.int64)%3;a=(a-a[rj]*pow(int(rho[rj]),-1,3)*rho)%3
    if any(a):break
   else:raise AssertionError('plane collapsed')
   kk=key_from_Nrow(xx);assert kk in kset;fused.append(kk);union(k,kk)
  assert k in fused
  links.append({'flag':k,'change_of_mark':fused});print('flag',k,'marks',fused,flush=True)
 groups={}
 for k in keys:groups.setdefault(find(k),[]).append(k)
 out={'links':links,'plane_orbits':[{'representative':k,'flags':v} for k,v in sorted(groups.items())]}
 (REC/'B_A2_plane_orbits.json').write_text(json.dumps(out));print('A2-marked flags',len(keys),'unmarked plane orbits with A2 neighbour',len(groups),flush=True)
