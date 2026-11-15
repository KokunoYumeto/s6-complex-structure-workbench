"""Construct every A2^12-marked isotropic-plane orbit and all extensions."""
from B_global_lattice import *
from collections import Counter
D=json.loads((REC/'B_A2_strata_setup.json').read_text());Y=np.array(D['Y_basis'],dtype=np.int64);M=model_A2();out=[];mass=0
folder=REC/'B_A2_flags';folder.mkdir(exist_ok=True)
for s,sd in enumerate(D['strata']):
 for line in (REC/f'B_A2_stratum_{s}.out').read_text().splitlines():
  z=line.split()
  if not z or z[0]!='orbit':continue
  oid,num,size=int(z[1]),int(z[3]),int(z[7])
  if s==0 and num==0:continue
  vec=[];n=num
  for _ in range(16):vec.append(n%3);n//=3
  vec+=sd['c_coeff'];y=(np.array(vec)@Y%3).tolist()
  path=folder/f'{s}_{oid}.json'
  if path.exists():r=json.loads(path.read_text())
  else:r=M.plane(y,folder/f'{s}_{oid}');path.write_text(json.dumps(r))
  orbit=size*sd['code_orbit']//2;assert size*sd['code_orbit']%2==0;mass+=orbit
  rsum=Counter(x['root_system'] for x in r['extensions']);flags=[x['root_system'] for x in r['extensions'] if x['L_intersection_index']==3]
  out.append({'stratum':s,'orbit_id':oid,'representative':num,'flag_orbit_size':orbit,'flag_stabilizer':277136640//orbit,'extensions':dict(rsum),'opposite':flags})
  assert 277136640%orbit==0
  print('flag',s,oid,'orbit',orbit,'stabilizer',277136640//orbit,'extensions',dict(rsum),'opposite',flags,flush=True)
assert mass==5230235650
(REC/'B_A2_flags.json').write_text(json.dumps(out));print('complete A2 flag orbits',len(out),'total isotropic quotient lines',mass,flush=True)
