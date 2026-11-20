from pathlib import Path
import sympy as sp
import json,hashlib,time
start=time.monotonic();u=sp.symbols('u1:4',nonzero=True);z=sp.symbols('z1:4',nonzero=True);w=sp.symbols('w',nonzero=True)
# z_i=exp(u_i/2), w=exp(D/2+x); the Dolbeault grading is fixed explicitly.
spinor=w*sp.prod(zz**-1-zz for zz in z)
euler=sp.prod(u)
index_class=sp.prod(uu**2/(zz-zz**-1)**2 for uu,zz in zip(u,z))
from_AS=(-1)**3*spinor/euler*index_class
expected=w*sp.prod(uu/(zz-zz**-1) for uu,zz in zip(u,z))
assert sp.cancel(from_AS-expected)==0
a,d,c2=sp.symbols('a d c2');p1=d*d-2*c2
printed=(3*d*d-p1)/24+(a*a+a*d)/2
rr=(d*d+c2)/12+(a*a+a*d)/2
assert sp.expand(printed-rr)==0
source=Path(__file__);out={'status':'PASS','assertions':2,'seconds':round(time.monotonic()-start,3),'checks':[{'label':'night:P3F.14','name':'ASIII_2_17_Dolbeault_graded_Spin_c_character','residual':'0'},{'label':'night:P3F.14','name':'ASIII_4_3_surface_Riemann_Roch_polynomial','residual':'0'}],'formal_substitution':{'z_i':'exp(u_i/2)','w':'exp(D/2+x)','graded_spinor_character':str(spinor),'Euler':str(euler),'source_index_class':str(index_class),'result':str(sp.factor(expected))},'scope':'Two exact character/polynomial identities for the cited primary source application. Does not independently prove Atiyah–Singer or identify an actual spin-c structure solely by its determinant. The actual inherited spin-c structure, orientation and U line are retained from F14. No earlier code or certificate imports.','code_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
source.with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False))
