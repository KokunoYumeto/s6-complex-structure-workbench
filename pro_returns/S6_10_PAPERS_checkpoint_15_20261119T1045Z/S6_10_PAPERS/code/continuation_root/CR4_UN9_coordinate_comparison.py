#!/usr/bin/env python3
"""Post-comparison maps between the two explicit normal-form choices."""
from pathlib import Path
from math import gcd
import sympy as s,json
U,V,W,r,a,b,c,u,v,k=s.symbols('U V W r a b c u v k',nonzero=True)
assert s.expand(V**3+(U/r)**2*(r**2*W)-(V**3+U**2*W))==0
R=k*s.Matrix([[u*u,u*v],[u*v,v*v]])
Qp=s.Matrix([[a,b],[b,c]])
assert R.det()==0
der=s.expand(s.trace(R.adjugate()*Qp))
assert s.expand(der-k*(a*v**2-2*b*u*v+c*u**2))==0
assert -2*(2//gcd(2,1))*(1//gcd(2,1))==-4
out={'status':'PASS','chronology':'Written after printed proof comparison; no producing code read',
 'unit_map':'(U,V,W) -> (r^-1 U,V,r^2 W), preserving V^3+U^2 W',
 'incidence_parameter_map':'R=Q(z)+E; inverse E=R-Q(z)',
 'rank_one_determinant_derivative':str(der),'spherical_square':-4,
 'scope':'Exact comparison identities, with their analytic invertibility and transversality arguments in the written proofs.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
