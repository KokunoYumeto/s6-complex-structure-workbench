#!/usr/bin/env python3
"""Division-free form determinant and exact torus coinvariant count."""
from pathlib import Path
import hashlib,json
import sympy as S
r=Path(__file__).resolve().parents[1];x,y,s=S.symbols('x y s',real=True);tau=(1+S.sqrt(3)*S.I)/2
a=S.Matrix([[1,tau,0,0]]);b=S.Matrix([[(y-1)/2,-(x+1)/2,1,S.I]])
M=a.col_join(b).col_join(S.conjugate(a)).col_join(S.conjugate(b))
det=S.expand(M.det(method='berkowitz'));assert S.simplify(det-2*S.sqrt(3))==0
monodromy=S.eye(4);coinvariant_dimension=4-(monodromy-S.eye(4)).rank();assert coinvariant_dimension==4
count=S.expand(2*0+s-1+coinvariant_dimension-0);assert count==s+3
out={'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'form_determinant_division_free':str(det),'form_determinant_equals':str(2*S.sqrt(3)),'form_basis_nonzero_for_every_real_x_y':True,'identity_monodromy_coinvariant_dimension':coinvariant_dimension,'component_count':str(count),'events_added':0}
p=r/'agents/ii_infra/checks/S6_SERIES_PUBLISH_II_form_and_count_exact_output.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
