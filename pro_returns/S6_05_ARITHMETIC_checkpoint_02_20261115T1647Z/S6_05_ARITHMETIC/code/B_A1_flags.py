"""Complete M24 orbit classification of A1^24-marked isotropic planes."""
from B_global_lattice import *
from itertools import permutations
from collections import Counter
from mmgroup import mat24
D=json.loads((REC/'B_A1_setup.json').read_text());trans=[];maps=[]
for s,sd in enumerate(D['strata']):
 z=np.load(REC/f'B_A1_transversal_{s}.npz');m=z['masks'];pp=z['perms'];trans.append({int(x):pp[i] for i,x in enumerate(m)});maps.append(orbit_map(f'B_A1_stratum_{s}.bin'))

def canonical(parts):
 keys=[]
 for A,B,C in permutations(parts):
  if A.bit_count()>B.bit_count() or B.bit_count()>C.bit_count():continue
  for s,sd in enumerate(D['strata']):
   if A not in trans[s]:continue
   p=trans[s][A];pi=[0]*24
   for i,j in enumerate(p):pi[int(j)]=i
   bb=sum(1<<pi[i] for i in range(24) if (B>>i)&1);b=sum(((bb>>j)&1)<<i for i,j in enumerate(sd['complement']));oid=int(maps[s][b]);assert oid
   keys.append((s,oid))
 return min(keys)
rows=[];groups={};FULL=(1<<24)-1
for s,sd in enumerate(D['strata']):
 for line in (REC/f'B_A1_stratum_{s}.out').read_text().splitlines():
  z=line.split()
  if not z or z[0]!='orbit':continue
  oid,b,size=int(z[1]),int(z[3]),int(z[5]);B=sum(((b>>i)&1)<<j for i,j in enumerate(sd['complement']));parts=(sd['A'],B,FULL^sd['A']^B);key=canonical(parts)
  colors=[0]*24
  for i in range(24):colors[i]=1 if (B>>i)&1 else 2 if (parts[2]>>i)&1 else 0
  sizes=sorted([p.bit_count() for p in parts]);mult=2 if sizes[0]==sizes[1] or sizes[1]==sizes[2] else 1
  r={'stratum':s,'orbit_id':oid,'parts':parts,'colors':colors,'ordered_orbit':sd['A_orbit']*size,'multiplicity':mult}
  rows.append(r);groups.setdefault(key,[]).append(r)
out=[];total=0
for key,rs in sorted(groups.items()):
 r=next(r for r in rs if (r['stratum'],r['orbit_id'])==key);orbit=sum(x['ordered_orbit'] for x in rs)//r['multiplicity'];assert sum(x['ordered_orbit'] for x in rs)%r['multiplicity']==0
 assert 244823040%orbit==0;total+=orbit;r['flag_orbit_size']=orbit;r['flag_stabilizer']=2*244823040//orbit;out.append(r)
 print('flag',key,'size_pattern',sorted(x.bit_count() for x in r['parts']),'orbit',orbit,'stabilizer',r['flag_stabilizer'],flush=True)
assert total==5230235650
(REC/'B_A1_partition_flags.json').write_text(json.dumps(out));print('complete A1 flag orbits',len(out),'total quotient lines',total,flush=True)

# Exact A1^24 Niemeier lattice in root coordinates, with the matching Golay code.
code=[[int(mat24.gcode_to_vect(1<<j)>>i)&1 for i in range(24)] for j in range(12)];Nb=span([[F(int(i==j)) for j in range(24)] for i in range(24)]+[[F(x,2) for x in row] for row in code]);G=ints(2*Nb*Nb.transpose());R=Nb.inv();M=PlaneModel(G,qrows(R),rho_factor=F(1,2),correction=2)
folder=REC/'B_A1_flags';folder.mkdir(exist_ok=True);records=[]
for r in out:
 s,oid=r['stratum'],r['orbit_id'];path=folder/f'{s}_{oid}.json';y=ints(fmpq_mat([r['colors']])*R)[0]
 if path.exists():data=json.loads(path.read_text())
 else:data=M.plane(y,folder/f'{s}_{oid}');path.write_text(json.dumps(data))
 r['extensions']=dict(Counter(x['root_system'] for x in data['extensions']));r['opposite']=[x['root_system'] for x in data['extensions'] if x['L_intersection_index']==3];records.append(r)
 print('extension flag',s,oid,r['extensions'],'opposite',r['opposite'],flush=True)
(REC/'B_A1_flags.json').write_text(json.dumps(records));(REC/'B_A1_model.json').write_text(json.dumps({'Gram':G,'root_basis':qjson(R),'N_in_root_basis':qjson(Nb)}))
