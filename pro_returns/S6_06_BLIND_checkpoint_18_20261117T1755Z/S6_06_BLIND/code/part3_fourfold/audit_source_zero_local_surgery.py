from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
root=Path(__file__).resolve().parents[2]
a=s.symbols('a',integer=True)
b2=-(1-2*a)**2
c2=-a*(a-1)
assert s.expand(b2-4*c2)==-1
k=s.expand(-(b2-c2))
ell=s.expand(3-b2+4*c2)
assert k==3*a*a-3*a+1 and ell==4
outer_k=-k.subs(a,2)-1
outer_ell=-ell-4
assert (outer_k,outer_ell)==(-8,-8)
assert (4*outer_k-outer_ell)/24==-1
record={'utc':datetime.now(timezone.utc).isoformat(),'reviewer':'fourfold',
 'scope':'RT.9–10, specified reduced local fixed-S3 surgery only','status':'PASS',
 'frame':'The inside coefficient of O(-E) maps to T1 times that coefficient in the outside trivial line. Thus the displayed frame gives O(-(a-1)E) plus O(-aE), retaining the positive real factor for the conjugated second coordinate.',
 'bundle':'c1=(1-2a)E, c2=-a(a-1), p1(ad)=-1; base is oriented reversed CP2, E^2=-1.',
 'physical_fixed_boundary_pair':['3a^2-3a+1',4],
 'orientations':'The orbit-bordism outer boundary is minus the circle-first physical quotient; the fixed-surface deleted tube is -BF after one negative normal conjugation; the isolated point gives +CP3 after two conjugations.',
 'isotropy':'Away from the fixed surface and isolated point, a nonzero S or T coordinate forces auxiliary phase1 and then physical phase1; if only z,V are nonzero, the two weight equations again force both phases1.',
 'local_free_boundary_pair':[-8,-8],'local_physical_index':-1,
 'limitation':'No identification with the global residual end, no requested-fan comparison, and no individual source-zero return is inferred.'}
(root/'records/fourfold_audit_source_zero_local_surgery.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','local_pair':[-8,-8],'local_index':-1}))
