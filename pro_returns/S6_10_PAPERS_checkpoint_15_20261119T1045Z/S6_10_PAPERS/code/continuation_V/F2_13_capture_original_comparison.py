"""Capture old producer output and its chosen coordinate bases for comparison only.
No output of this script is a new independent mathematical certificate.
"""
from pathlib import Path
import contextlib,io,runpy,json,hashlib,datetime
base=Path('/workspace/scratch/ae06852560d6/materials/S6_08_PAPERS_2_returns_code/returns/S6_04_MAPS_MANIFOLDS/code')
outdir=Path(__file__).resolve().parents[2]/'analysis/continuation_V'
result={'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Original producer rerun solely as comparison-coordinate data, no independent-check credit.','cases':{}}
for case,name in [('A','fourfolds_56a_newlattice.py'),('B','fourfolds_56b_newlattice.py')]:
 p=base/name;f=io.StringIO()
 with contextlib.redirect_stdout(f):ns=runpy.run_path(str(p))
 (outdir/f'F2_13_old_{case}_producer.stdout.txt').write_text(f.getvalue())
 def vals(m):return [[str(x) for x in row] for row in m.tolist()]
 A,B=ns['A'],ns['B'];finite=[]
 for M,m,u,C in zip([ns['M1'],ns['M2']],[5,6],ns['twists'],[A,B]):
  D=M[1:,1:];lam=ns['Matrix']([0]+list(ns['kernel'](D-ns['eye'](5))[:,0]));K2=ns['kernel'](ns['ext'](C,2)-ns['eye'](15));K3=ns['kernel'](ns['ext'](C,3)-ns['eye'](20))
  finite.append({'order':m,'u':vals(u),'lambda':vals(lam),'K2_old_basis':vals(K2),'K3_old_basis':vals(K3)})
 result['cases'][case]={'producer':str(p),'producer_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'A_transformed':vals(A),'B_transformed':vals(B),'Qnew':vals(ns['Qnew']),'finite_basis_comparison_data':finite}
p=outdir/'F2_13_old_coordinate_definitions.json';p.write_text(json.dumps(result,indent=2)+'\n');print(p)
