"""Diagnostic: test the zero-suspension cusp map against Poincare--Lefschetz duality."""
from pathlib import Path
import contextlib,io,json
with contextlib.redirect_stdout(io.StringIO()):
 exec(Path(__file__).with_name('global_candidate_complex.py').read_text().split('Diff={}')[0])
Ds={}
for k in range(1,9):
 n=cusp_dim(k);prev=cusp_dim(k-1)
 d=s.zeros(prev,n).row_join(fcusp(k-1)).col_join(s.zeros(bdry_dim(k-2),n).row_join(-dbdry(0,k-1)))
 Ds[k]=d
out={}
for k in range(9):
 n=cusp_dim(k)+bdry_dim(k-1)
 a=Ds[k] if k else s.zeros(0,n)
 b=Ds[k+1] if k<8 else s.zeros(n,0)
 h=homology(a,b);out[k]=h;print(k,h,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=int))
print('psi collapse',s.Matrix([[1,-1,1,1,-1,-1,1]])*maps[4][3:,:],flush=True)
