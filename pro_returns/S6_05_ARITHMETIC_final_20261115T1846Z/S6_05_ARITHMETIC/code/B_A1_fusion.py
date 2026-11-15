"""Complete fusion of A1-marked flags, including all A1/A2 overlaps."""
from B_A2_fusion import mark_isometry as markA2,key_from_Nrow,MODEL as TARGET_A2
from B_global_lattice import *
from itertools import permutations
from mmgroup import mat24
import pynauty
md=json.loads((REC/'B_A1_model.json').read_text());MODEL=PlaneModel(md['Gram'],md['root_basis'],rho_factor=F(1,2),correction=2)
D=json.loads((REC/'B_A1_setup.json').read_text());trans=[];maps=[]
for s in range(4):
 z=np.load(REC/f'B_A1_transversal_{s}.npz');pp=z['perms'];mm=z['masks'];trans.append({int(x):pp[i] for i,x in enumerate(mm)});maps.append(orbit_map(f'B_A1_stratum_{s}.bin'))
def canonical(parts):
 keys=[]
 for A,B,C in permutations(parts):
  if A.bit_count()>B.bit_count() or B.bit_count()>C.bit_count():continue
  for s,sd in enumerate(D['strata']):
   if A not in trans[s]:continue
   p=trans[s][A];pi=[0]*24
   for i,j in enumerate(p):pi[int(j)]=i
   bb=sum(1<<pi[i] for i in range(24) if (B>>i)&1);b=sum(((bb>>j)&1)<<i for i,j in enumerate(sd['complement']));oid=int(maps[s][b]);assert oid;keys.append((s,oid))
 return min(keys)

def graph(C):
 code=[]
 for x in range(4096):
  v=np.array([(x>>i)&1 for i in range(12)],dtype=np.int64)@C%2;code.append(tuple(v.tolist()))
 adj={i:[] for i in range(24)}
 for c in code:
  if sum(c)!=8:continue
  k=len(adj);adj[k]=[i for i,x in enumerate(c) if x]
  for i in adj[k]:adj[i].append(k)
 g=pynauty.Graph(len(adj),adjacency_dict=adj,vertex_coloring=[set(range(24)),set(range(24,len(adj)))])
 return code,pynauty.canon_label(g)
Cf=np.array([[int(mat24.gcode_to_vect(1<<j)>>i)&1 for i in range(24)] for j in range(12)],dtype=np.int64);fcode,flab=graph(Cf);fset=set(fcode)
def markA1(ext,source=MODEL):
 B=qmat(ext['basis']);roots=fmpq_mat(ext['roots'])*B;rv=qrows(roots);bl=B*source.Li;col=next(j for j in range(24) if any(F(str(bl[i,j])).denominator!=1 for i in range(24)));ell=[int(3*F(str(bl[i,col])))%3 for i in range(24)];re=[sum(ext['roots'][i][j]*ell[j] for j in range(24))%3 for i in range(len(ext['roots']))]
 A=qmat([v for v,e in zip(rv,re) if e==1]);assert A.nrows()==24;AI=A.inv();coords=B*AI;C,_=rr([[int(2*F(str(coords[i,j])))%2 for j in range(24)] for i in range(24)],2);assert C.shape==(12,24)
 code,lab=graph(C);p=[0]*len(lab)
 for a,b in zip(lab,flab):p[a]=b
 p=p[:24];assert set(p)==set(range(24))
 for c in code:
  d=[0]*24
  for i,x in enumerate(c):d[p[i]]=x
  assert tuple(d) in fset
 P=fmpq_mat([[int(j==p[i]) for j in range(24)] for i in range(24)]);T=AI*P*MODEL.R
 assert T*MODEL.G*T.transpose()==source.G
 assert span(qrows(source.L*T))==span(qrows(MODEL.L))
 return T

def keyA1(x):
 a=qrows(x*MODEL.R.inv())[0];v=[(u.numerator*pow(u.denominator,-1,3))%3 for u in a];parts=tuple(sum(1<<i for i,x in enumerate(v) if x==k) for k in range(3));assert len(set(v))>1
 return canonical(parts)
if __name__=='__main__':
 a2=json.loads((REC/'B_A2_plane_orbits.json').read_text());a2rep={tuple(k):tuple(g['representative']) for g in a2['plane_orbits'] for k in g['flags']};flags=json.loads((REC/'B_A1_flags.json').read_text());keys=[(x['stratum'],x['orbit_id']) for x in flags];parent={k:k for k in keys};links=[];cross={}
 def find(k):
  while parent[k]!=k:parent[k]=parent[parent[k]];k=parent[k]
  return k
 def union(a,b):
  a,b=find(a),find(b)
  if a!=b:parent[max(a,b)]=min(a,b)
 for k in keys:
  dat=json.loads((REC/'B_A1_flags'/f'{k[0]}_{k[1]}.json').read_text());y=qmat([dat['y']]);a2marks=[e for e in dat['extensions'] if e['L_intersection_index']==3 and e['root_system']=='12A2']
  if a2marks:
   ext=a2marks[0];T=markA2(ext,MODEL)
   for x in [MODEL.v,y]:
    xx=x*T
    # zero in target quotient iff proportional to rho modulo3N
    a=np.array(ints(xx)[0],dtype=np.int64)%3;rho=np.array(ints(TARGET_A2.rho)[0])%3;j=next(j for j,x in enumerate(rho) if x);a=(a-a[j]*pow(int(rho[j]),-1,3)*rho)%3
    if any(a):break
   kk=key_from_Nrow(xx);cross[k]=a2rep[kk];print('A1 flag',k,'maps to A2 plane',cross[k],flush=True);continue
  marks=[]
  for ext in dat['extensions']:
   if ext['L_intersection_index']!=3 or ext['root_system']!='24A1':continue
   T=markA1(ext)
   for x in [MODEL.v,y]:
    xx=x*T;aa=qrows(xx*MODEL.R.inv())[0];vv=[(u.numerator*pow(u.denominator,-1,3))%3 for u in aa]
    if len(set(vv))>1:break
   kk=keyA1(xx);marks.append(kk);union(k,kk)
  assert k in marks;links.append({'flag':k,'change_of_mark':marks});print('A1-only flag',k,'marks',marks,flush=True)
 groups={}
 for k in keys:
  if k not in cross:groups.setdefault(find(k),[]).append(k)
 out={'A1_to_A2':[{'flag':k,'A2_plane':v} for k,v in sorted(cross.items())],'A1_only_links':links,'A1_only_plane_orbits':[{'representative':k,'flags':v} for k,v in sorted(groups.items())]}
 (REC/'B_A1_plane_orbits.json').write_text(json.dumps(out));print('A1 flags',len(keys),'with A2 neighbour',len(cross),'new A1-only plane orbits',len(groups),flush=True)
