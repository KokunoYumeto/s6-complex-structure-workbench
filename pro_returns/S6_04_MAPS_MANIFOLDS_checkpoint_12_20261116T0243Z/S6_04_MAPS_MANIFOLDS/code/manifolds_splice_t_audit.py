"""Independent tracking of the two actual complement t cycles through E17."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
source=(ROOT/'code/maps_splice_module.py').read_text().split('def chi_mod12')[0]
source=source.replace('log=[]\ndef cancel', "tracked_t=[]\nfor side in range(2):\n    idx=VB[side][2].index((2,2,()))\n    lab=('V',side,idx)\n    tracked_t.append([R(1) if v==lab else R() for v in labels[2]])\nlog=[]\ndef cancel",1)
needle='    ds[k]=[[M[r][c]-M[r][j]*ui*M[i][c] for c in cols] for r in rows]'
replacement="""    for cycle in tracked_t:
        if k==2:cycle[:]=[v for z,v in enumerate(cycle) if z!=j]
        elif k==3:cycle[:]=[cycle[r]-M[r][j]*ui*cycle[i] for r in rows]
"""+needle
assert needle in source
source=source.replace(needle,replacement,1)
exec(compile(source,'maps_splice_module.py','exec'),globals())
images=[]
for cycle in tracked_t:
    assert not cycle[3] and not cycle[15]
    v=[mod_centers(cycle[i]) for i in trows]
    images.append([(i,x.string()) for i,x in enumerate(v) if x])
assert images==[[(3,'1')],[(11,'1')]],images
print('Actual complement t inclusions in the fourteen-generator block:',images)
print('Hence t(first)=Omega_R, t(second)=Omega_L; their Gamma coinvariants each have exact order6.')
(ROOT/'records/manifolds_splice_t_audit.json').write_text(json.dumps(dict(images=images,coinvariant_order=[6,6]),indent=2)+'\n')
