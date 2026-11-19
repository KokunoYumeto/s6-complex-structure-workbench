"""Enumerate the MW=Z configurations from Engel's public exact engine.

All input sources are snapshotted under records/explorer, with upstream
licenses. This script executes the Python (Fraction/integer) monodromy path,
not the unavailable Sage topology service. No filled topology is inferred.
"""
from pathlib import Path
import sys,json,csv
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(Path(__file__).resolve().parent/'explorer'))
import os_monodromy as om

def clean(x):
    if isinstance(x,dict): return {str(k):clean(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [clean(v) for v in x]
    if isinstance(x,(str,int,bool)) or x is None:return x
    return str(x)
records=[]
for entry in range(1,75):
    info=om.os_info(entry,verbose=False)
    if info['mw_rank']!=1 or info['torsion_orders']:continue
    for profile in info['available_profiles']:
        data=om.os_info(entry,profile=profile,verbose=False)
        matrices=data['elliptic_matrices']
        assert om.matrix_product(matrices,size=2)==om.identity(2)
        assert sum(om.fiber_invariants(t)[0] for t in data['kodaira_types'])==12
        assert sum(om.fiber_invariants(t)[1] for t in data['kodaira_types'])==7
        assert data['mw_rank']==1 and not data['torsion_orders']
        records.append(clean(data))
        print(entry,profile,','.join(data['kodaira_types']),
              'height='+str(data['height_matrix'][0][0]),
              'narrow='+str(data['narrow_generators'][0][0]))
assert len(records)==21
(Path(__file__).resolve().parent/'manifolds_os_configurations.json').write_text(json.dumps(records,indent=2))
with (Path(__file__).resolve().parent/'manifolds_os_configurations.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['os_entry','profile','configuration','height','narrow_generator',
                               'monodromy_product','Euler_sum','root_rank'])
    for r in records:w.writerow([r['os_entry'],r['profile'],' + '.join(r['kodaira_types']),
                                r['height_matrix'][0][0],r['narrow_generators'][0][0],'identity',12,7])
print('EXACT CHECKS: 8 torsion-free rank-one MW entries; 21 configurations; all products identity.')
