"""After-reading radial verification of the target's additional cusp constant."""
from pathlib import Path
import sympy as s
import json,datetime
r=Path(__file__).resolve().parents[1]
radius,A,ell,pi=s.symbols('radius A ell pi',positive=True)
potential=-ell**2/(2*s.log(A/radius))
density=s.simplify(-(s.diff(potential,radius,2)+s.diff(potential,radius)/radius)/(2*pi))
expected=ell**2/(2*pi*radius**2*s.log(A/radius)**3)
assert s.simplify(density-expected)==0
flux=s.simplify(radius*s.diff(potential,radius))
assert s.limit(flux,radius,0,dir='+')==0
o={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
   'timing':'After first printed-proof comparison; no preread credit for this program.',
   'method':'Real radial Laplacian of the inverse-log potential and exact limiting radial flux.',
   'density':str(density),'radial_flux':str(flux),'limit':0,'assertions':2,'outcome':'PASS'}
(r/'records/S6_SERIES_PUBLISH_I_C89_cusp_density.json').write_text(json.dumps(o,indent=2)+'\n')
print(json.dumps(o,indent=2))
