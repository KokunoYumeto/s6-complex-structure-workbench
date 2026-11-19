"""Compute both possible effects of all derived cusp-map corrections after global gluing.
Only H3(boundary) has torsion, Z/2. Thus a homologically invisible map
into the free cusp homology is an Ext class in H4(cusp)/2. Its image in
the global degree-four cokernel has rank one modulo two (cusp_ext_ambiguity).
The two cases below therefore exhaust its effect on integral homology.
"""
from pathlib import Path
import contextlib,io,json
with contextlib.redirect_stdout(io.StringIO()):
 exec(Path(__file__).with_name('complement_check.py').read_text().split('out={}')[0])
# A cohomology generator of the torsion subgroup H^4(B;Z).
a=dbdry(0,5).T;b=dbdry(0,4).T
z,p,rels=hpresentation(a,b)
d,u,v=snf(rels)
idx=[i for i in range(rels.rank()) if abs(d[i,i])>1]
assert len(idx)==1 and abs(d[idx[0],idx[0]])==2
r=(z*u.inv()[:,idx[0]]).T
assert r*dbdry(0,5)==s.zeros(1,dbdry(0,5).cols)
# Any integral H4(B) cycle pairs trivially with this torsion cohomology class.
bz,bp,br=hpresentation(dbdry(0,4),dbdry(0,5));assert r*bz==s.zeros(1,bz.cols)
# e_3 is the first base-degree-two cusp coordinate; psi(e_3)=1.
vect=s.zeros(cusp_dim(4),1);vect[3,0]=1
E=vect*r
out={'torsion_cocycle':r.tolist(),'correction':E.tolist(),'cases':{}}
for bit in [0,1]:
 Diff={}
 for k in range(1,10):
  ds=dspace(k);db=dbtotal(k-1);f=F(k-1)
  if k==5 and bit:
   start=main_dim(4)+cap_dim(1,4)+cap_dim(2,4)
   f[start:start+cusp_dim(4),:bdry_dim(4)]-=E
  Diff[k]=ds.row_join(f).col_join(s.zeros(db.rows,ds.cols).row_join(-db))
  if k>1:assert Diff[k-1]*Diff[k]==s.zeros(Diff[k-1].rows,Diff[k].cols)
 hh={}
 for k in range(9):
  n=space_dim(k)+bdry_total(k-1)
  h=homology(Diff[k] if k else s.zeros(0,n),Diff[k+1])
  hh[k]={'free':h['free'],'torsion':h['torsion']}
  print('Ext case',bit,'H',k,hh[k],flush=True)
 out['cases'][bit]={'homology':hh,'differentials':{str(k):v.tolist() for k,v in Diff.items()}}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=int))
