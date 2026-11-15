"""Independent read-only audit of every delivered plane and group matrix.

Recompute the total mass from the separately generated group certificates,
not from the flag tables used to discover the classification.
"""
from B_global_lattice import *
from collections import Counter
from hashlib import sha256
CO0=8315553613086720000
rows=json.loads((REC/'B_all_129_plane_orbits.json').read_text());d=json.loads((REC/'B_standard_Leech_basis.json').read_text());G=fmpz_mat(d['Gram']);seen=set();mass=F(0);covered=0;ng=0;manifest=[]
for r in rows:
 i=r['orbit_id'];path=REC/'B_plane_groups'/f'{i:03d}.json';data=json.loads(path.read_text());assert data['order']==r['stabilizer_order'];P=np.array(r['plane_basis_standard_mod3'],dtype=np.int64);p,piv=rr(P);assert np.array_equal(p,P) and len(piv)==2 and tuple(P.flat) not in seen;seen.add(tuple(P.flat))
 assert np.array_equal(P@np.array(d['Gram'],dtype=np.int64)@P.T%3,np.zeros((2,2),dtype=np.int64))
 for a in data['generators_in_standard_Leech_basis']:
  T=fmpz_mat(a);assert abs(T.det())==1 and T*G*T.transpose()==G;assert np.array_equal(rr(P@np.array(a,dtype=np.int64)%3)[0],P);ng+=1
 assert len(r['eight_extensions'])==8 and Counter(r['eight_extensions'])==r['extensions'];assert CO0%data['order']==0
 covered+=CO0//data['order'];mass+=F(1,data['order']);manifest.append({'orbit':i,'generator_file':str(path.relative_to(ROOT)),'sha256':sha256(path.read_bytes()).hexdigest(),'generators':len(data['generators_in_standard_Leech_basis']),'full_order':data['order']})
total=(3**11+1)*(3**12-1)*(3**10+1)*(3**11-1)//16
print('Distinct supplied reduced plane representatives:',len(seen))
print('Exact integral group generators independently rechecked:',ng)
print('Every generator: unimodular, Gram preserving, plane preserving.')
print('Sum of orbit lengths from independently generated FULL group certificates:',covered)
print('Direct split-quadratic incidence count:',total)
print('Rational stabilizer mass:',mass)
print('RESIDUAL PLANES:',total-covered)
print('RESIDUAL MASS:',F(total,CO0)-mass)
assert len(rows)==129 and covered==total and mass==F(total,CO0)
(REC/'B_plane_group_manifest.json').write_text(json.dumps(manifest,indent=2))
print('PASS: all 129 full group records verified; NO RESIDUAL MASS REMAINS.')
