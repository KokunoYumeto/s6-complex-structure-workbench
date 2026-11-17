"""Exact universal characteristic and finite-group checks, P3R.1--2."""
from pathlib import Path
import json
import sympy as s

c1,c2,sigma=s.symbols('c1 c2 sigma')
p1=c1**2-2*c2
spin_c=28*((p1**2-4*sigma)/896-c1**2*p1/192+c1**4/384)
answer=(-c1**4+4*c1**2*c2+3*c2**2-3*sigma)/24
assert s.expand(spin_c-answer)==0
rows=[]
for b in range(28):
    actual=[a for a in range(28) if (6*a-b)%28==0]
    expected=[] if b%2 else sorted({(5*(b//2))%28,(5*(b//2)+14)%28})
    assert actual==expected
    rows.append({'sixfold_class':b,'original_classes':actual})
result={'status':'PASS','characteristic_polynomial':str(s.expand(answer)),
        'sixfold_residue_table':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
