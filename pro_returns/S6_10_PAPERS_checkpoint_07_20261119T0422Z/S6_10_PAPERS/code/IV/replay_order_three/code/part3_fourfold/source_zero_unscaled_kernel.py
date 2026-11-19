#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import json
root=Path(__file__).resolve().parents[2]
w,lam=s.symbols('w lam',nonzero=True)
rows=[]
for a,b,kernel,transverse in [(1,2,(-1,1),(1,2)),(2,1,(-1,2),(1,1))]:
 H=s.Matrix([[2,b],[-a,-1]])
 assert H*s.Matrix(kernel)==s.zeros(2,1)
 assert s.Matrix([transverse])*H==s.zeros(1,2)
 # Exact exceptional-base residual units after separating H powers.
 h=(w,w**(-a))
 g=(w**b,2*(-1)**(b+1)*lam*w**(-2))
 kz=s.simplify(h[0]**kernel[0]*g[0]**kernel[1])
 kv=s.simplify(h[1]**kernel[0]*g[1]**kernel[1])
 ky=s.simplify(kz**transverse[0]*kv**transverse[1])
 assert s.simplify(ky-4*lam**2/w)==0
 rows.append({'a':a,'b':b,'H':[[int(x) for x in row] for row in H.tolist()],
  'kernel':kernel,'transverse_character':transverse,
  'physical_delta_weight':transverse[1],
  'Z_multiplier':str(kz),'V_multiplier':str(kv),'Y_multiplier':str(ky)})
out={'utc':datetime.now(timezone.utc).isoformat(),
 'status':'PASS: actual unscaled H kernel and transverse multiplier',
 'rows':rows,'scope':'The literal kernel multiplier crosses unit modulus; '
 'no compact rank-one quotient or source return is assigned.'}
(root/'code/part3_fourfold/source_zero_unscaled_kernel.json').write_text(
 json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
