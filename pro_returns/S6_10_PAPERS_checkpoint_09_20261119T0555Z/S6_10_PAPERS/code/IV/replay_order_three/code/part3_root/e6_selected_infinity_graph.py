"""Exact exponent and finite-deck checks for the selected-infinity root graph."""
from pathlib import Path
import json,math
rows=[]
for kind,begin in [('good',1),('reduced',0)]:
 for ell in range(begin,begin+65):
  m=3*ell if kind=='good' else 3*ell+2
  ax=2*ell if kind=='good' else 2*ell+2
  ay=3*ell if kind=='good' else 3*ell+3
  wx=2*ell if kind=='good' else 2*(ell+2)
  wy=3*ell if kind=='good' else 3*(ell+2)
  dx=0 if kind=='good' else 2
  dy=0 if kind=='good' else 3
  assert 3*ax-2*m==dx and 3*ay-3*m==dy
  assert 2*m-4*ax==-wx and 3*m-4*ay==-wy
  assert (-wx+4*ax)%m==0 and (-wy+4*ay)%m==0
  g=math.gcd(m,4);assert math.gcd(m,math.gcd(4,math.gcd(wx,wy)))==g
  assert math.gcd(m//g,4//g)==1
  rows.append({'branch':kind,'l':ell,'m':m,'root_x_exponent':ax,'root_y_exponent':ay,'eta_x_weight':wx,'eta_y_weight':wy,'d0_numerator_weights':[dx,dy],'primitive_base_ray':[m//g,4//g],'generic_central_inertia':g,'pass':True})
out={'status':'PASS','cases':len(rows),'scope':'Both actual root progressions; explicit selected-infinity graph chart and exact D^-4 finite-deck comparison. No complementary corner, proper native filling or return is asserted.','rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','cases':len(rows)},indent=2))
