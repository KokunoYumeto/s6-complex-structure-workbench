#!/usr/bin/env python3
"""Make the explicit rank-one infinity adaptation; preserve the source program."""
from pathlib import Path
from datetime import datetime, timezone
import json

root=Path(__file__).resolve().parents[2]
source=root/"code/part3/source_zero_regular_fan.py"
dest=root/"code/part3_fourfold/source_infinity_regular_fan.py"
text=source.read_text()
changes=[]
def replace(old,new,count=1):
    global text
    assert text.count(old)==count,(old,text.count(old),count)
    text=text.replace(old,new)
    changes.append({"old":old,"new":new,"count":count})

replace('I = ((1, 0), (0, 1))','I = ((1, 0), (0, 0))')
replace('self.H = ((2,b),(-a,N-1))','self.H = ((2,b),(-a,N-2))')
replace('if S or sector == "I":','if S:')
replace('        elif sector == "W":\n            assert R > 0 and Y == -self.a*X',
'''        elif sector == "I":
            assert R > 0 and Y == 0
            n = (X//R, 0)
        elif sector == "W":
            assert R > 0 and Y == -self.a*X''')
replace('# Its original integral primitive ray is (2,N-1,0,2), not a height-one',
        '# Its original integral primitive ray is (2,N-2,0,2), before primitive reduction of a')
replace('p = primitive((self.b,self.N-1,0,2))','p = primitive((self.b,self.N-2,0,2))')
replace("d = 3 if sector == 'I' else 2","d = 2")
replace("            if boundary=='W':stabilizer=[[-self.b,1]]",
'''            if boundary=='I':stabilizer=[[0,1]]
            elif boundary=='W':stabilizer=[[-self.b,1]]''')
replace("([[-self.b,1]] if sector=='W' else [[1,0]]) if v[3]==0 and sector!='I' else []",
        "([[0,1]] if sector=='I' else [[-self.b,1]] if sector=='W' else [[1,0]]) if v[3]==0 else []")
replace("'proof':'notes/part3_source_zero_equivariant_resolution_audit.md'",
        "'proof':'notes/part3_source_infinity_fourfold_working.md, IF.8; relative regularization algorithm retained from the source-zero proof'")
replace("dest=ROOT/'code/part3'/f'source_zero_regular_fan_{a}_{b}_{N}.json'",
        "dest=ROOT/'code/part3_fourfold'/f'source_infinity_regular_fan_{a}_{b}_{N}.json'")
text=text.replace('"""Execute the proved relative periodic fan resolution, retaining every lattice map.',
'''"""Execute the infinity rank-one fan adaptation, retaining every lattice map.

The legacy sector tags I,W,E now mean the two unselected strict transforms
A,B and the parameter E face. All three are rank one. The selected cusp
lies outside this local atlas. No global analytic quotient or return is assigned.''')
dest.write_text(text)
(root/"code/part3_fourfold/source_infinity_fan_derivation.json").write_text(
    json.dumps({"utc":datetime.now(timezone.utc).isoformat(),
                "source":str(source),"destination":str(dest),"changes":changes},indent=2)+"\n")
print(f"Saved {dest.name}; {len(changes)} exact adaptations")
