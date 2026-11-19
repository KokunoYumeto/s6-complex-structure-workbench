"""Fresh exact nonsingularity enclosures for the central real-intersection system."""
from pathlib import Path
import json
import minimum_root_regions as rr
from flint import arb,acb_mat
chart=rr.Chart('infinity')
out={'scope':'The actual preconditioned 4 by 4 real-intersection system on the full central square, its centre, and 16 subsquares.','results':[]}
boxes=[('centre',['0','0','0','0']),('full_square',['-.1','.1','-.1','.1'])]
for i in range(4):
 for j in range(4):
  boxes.append((f'subsquare_{i}_{j}',[str(-arb('.1')+arb(i)/20),str(-arb('.1')+arb(i+1)/20),str(-arb('.1')+arb(j)/20),str(-arb('.1')+arb(j+1)/20)]))
for name,box in boxes:
 M,b,c,d=rr.equations(chart.box(box)); det=M.det().real; inv=M.inv();assert not det.contains(0)
 out['results'].append({'name':name,'box':box,'determinant_lower':str(det.lower()),'determinant_upper':str(det.upper()),'determinant_excludes_zero':True,'inverse_finite':all(inv[i,j].is_finite() for i in range(4) for j in range(4))})
 assert out['results'][-1]['inverse_finite']
out['status']='PASS'
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
