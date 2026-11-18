"""Record the exact kernel calculation added to the audited native-square proof."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json

root=Path(__file__).resolve().parents[2]
source=root/'notes/part3_source_zero_double_loop_product_working.md'
kernel=[r for r in range(28) if (2*r)%28==0]
assert kernel==[0,14]
cases=[]
for a,scalar in [(1,0),(2,-2)]:
    solutions=[(z,j) for z in range(28) for j in range(28)
               if (z+j+a-2*scalar)%28==0 and (j-z-a)%28==0]
    formula=sorted([((-a+scalar+14*e)%28,(scalar+14*e)%28) for e in [0,1]])
    assert solutions==formula
    cases.append({'a':a,'k':1,'scalar_index':scalar,'pairs':solutions})
record={'utc':datetime.now(timezone.utc).isoformat(),'reviewer':'root','status':'PASS',
 'audited_sections':['DZ.5','DZ.6'],'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'kernel_of_doubling':kernel,'smallest_cases':cases,
 'reason':'The proved sum and actual single-loop difference give 2(Z_JT-k A_scalar)=0. Its full inverse image in Z/28 is the common translate by the kernel {0,14}. Subtraction of the actual difference gives the ordered pair in DZ.28.',
 'scope':'No e is selected and no assertion of constancy across family data is made. The complete DZ.1-4 map audit is recorded separately.'}
p=root/'records/root_audit_source_zero_pair_corollary.json'
assert not p.exists()
p.write_text(json.dumps(record,indent=2)+'\n')
print('PASS: exact kernel and two-element ordered-pair corollary.')
