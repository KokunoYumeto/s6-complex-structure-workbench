"""Read and summarize the complete interval proof, preserving sharp endpoints."""
from certified_minimum_root import *
from pathlib import Path
import hashlib
p=Path(__file__).parent
roots=json.loads((p/'certified_minimum_root.json').read_text())
cusp=json.loads((p/'certified_minimum_cusp.json').read_text())
ann=json.loads((p/'certified_minimum_cusp_annulus.json').read_text())
collar=json.loads((p/'certified_minimum_collar.json').read_text())
shift=json.loads((p/'normalization_shift.json').read_text())
def ends(v):return {'lower':v.lower().str(80),'upper':v.upper().str(80)}
ev=RootEvaluator('infinity',400)
hess=ev.evaluate(acb(arb(0,'.1'),arb(0,'.1')),True)
assert hess['xx']>0 and hess['yy']>0 and hess['xx']*hess['yy']-hess['xy']*hess['xy']>0
hessout={k:ends(hess[k]) for k in ['xx','xy','yy']}
hessout['determinant']=ends(hess['xx']*hess['yy']-hess['xy']*hess['xy'])
hmin=arb(roots['charts']['infinity']['center_h']);a_split=ballparse(shift['a_split']);original=hmin-a_split.imag
out={'theorem':'h_b has its unique global minimum at infinity.','h_min':ends(hmin),'threshold_b':ends(-hmin),
     'h_original_min':ends(original),'threshold_original':ends(-original),'local_hessian_square_radius':'.1','hessian':hessout,
     'counts':{'infinity_root':len(roots['charts']['infinity']['accepted_boxes']),'zero_root':len(roots['charts']['zero']['accepted_boxes']),
               'cusp_annulus':len(ann['accepted_boxes']),'collar':len(collar['accepted_boxes']),'collar_steps':len(collar['continuation_bounds'])},
     'cusp_inner_disk':cusp['certified_disk_radius'],'cusp_outer_disk':ann['outer_radius']}
files=['minimum_tools.py','certified_minimum_root.py','certified_minimum_root.json','certified_minimum_cusp.py','certified_minimum_cusp.json',
       'certified_minimum_cusp_annulus.py','certified_minimum_cusp_annulus.json','certified_minimum_collar.py','certified_minimum_collar.json']
out['sha256']={name:hashlib.sha256((p/name).read_bytes()).hexdigest() for name in files}
print(json.dumps(out,indent=2),flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
