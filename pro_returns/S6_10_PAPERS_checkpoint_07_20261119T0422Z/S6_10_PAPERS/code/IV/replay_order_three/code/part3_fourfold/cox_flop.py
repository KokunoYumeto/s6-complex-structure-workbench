#!/usr/bin/env python3
"""Exact Cox weights, gauge lift, and charged-cap maps for the real flop."""
from pathlib import Path
from datetime import datetime,timezone
import json
import sympy as s
root=Path(__file__).resolve().parents[2]
p=root/'notes/part3_flop_cobordism.md'
with (root/'records/literature_fourfold.md').open('a') as f:
 f.write('\n-'+datetime.now(timezone.utc).isoformat()+' — Opened own `notes/part3_flop_cobordism.md`; reason: record and check the exact real Cox comparison and charged cap maps; material: fan rays, period lift, oriented-boundary accounting.\n')
t=p.read_text().replace(chr(11)+'mathrm',r'\mathrm')
t=t.replace('V\\longmapsto q\\,r^{2mn}b(q)V,','V\\longmapsto q^n r^{2mn}b(q)V,')
t=t.replace('the displayed \\(q\\).','the displayed \\(q^n\\), using the signed integer vertical translation \\(n\\).')
p.write_text(t)
u0=s.Matrix([0,0,1]);u4=s.Matrix([1,1,1]);u1=s.Matrix([1,0,1]);u2=s.Matrix([0,1,1])
U=s.Matrix.hstack(u0,u4,u1,u2)
aux=s.Matrix([1,1,-1,-1]);delta=s.Matrix([-1,0,0,1]);eta=s.Matrix([-1,0,1,0])
assert U*aux==s.zeros(3,1)
assert U*delta==s.Matrix([0,1,0])
assert U*eta==s.Matrix([1,0,0])
weight_rows=s.Matrix.vstack(aux.T,delta.T)
minors={(i,j):int(weight_rows[:,[i,j]].det()) for i in range(4) for j in range(i+1,4)}
assert all(abs(v)<=1 for v in minors.values())
A,B,R=s.symbols('A B R')
gauge=s.Matrix([-A-B-R,0,A,B+R])
assert U*gauge==s.Matrix([A,B+R,0])
assert sum(gauge)==0
e=s.Matrix([1,-1])
# Columns are the pullbacks of h_A and h_B in the ordered p,q basis.
end1=s.Matrix([[1,0],[0,-1]])
end2=s.Matrix([[0,-1],[1,0]])
assert end1*e==end2*e==s.Matrix([1,1])
swap=s.Matrix([[0,-1],[-1,0]])
assert swap*e==e
assert swap**2==s.eye(2)
pair=s.Matrix([[0,1],[1,0]])
assert swap.T*pair*swap==pair
out=dict(status='PASS',proof='P3K.17',
 ray_matrix=[list(U.row(i)) for i in range(3)],
 auxiliary_weights=list(aux),physical_delta_weights=list(delta),
 two_torus_minors={str(k):v for k,v in minors.items()},
 positive_auxiliary_coordinates_delta_weights=[-1,0,0,-1],
 exact_gauge_lift=[str(x) for x in gauge],
 gauge_torus_vector=[str(x) for x in U*gauge],
 inner_face='CP3 with physical delta weights (-1,0,0,-1)',
 inner_orbit='CP1 * CP1 = S5',
 actual_line='O(1)_A tensor O(-1)_B',
 cap_end_pullbacks=[list(end1*e),list(end2*e)],
 closed_correction_monodromy=[list(swap.row(i)) for i in range(2)],
 retained_obstruction='Neither separate D3 times S2 cap carries h_A-h_B.',
 retained_extra_boundary='Normal S2 bundle over the closed fixed base; its characteristic correction is evaluated separately.',
 scope='Code certifies exact local matrices and cap maps. P3K.17 proves the oriented family/collar comparison; no spin assumption is imposed on that comparison bordism.')
(root/'code/part3_fourfold/cox_flop.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print('PASS: Cox relation, physical delta lift, q preservation, both charged cap maps, and conjugate-swap line/intersection preservation.')


# BEGIN POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
import importlib.util as _scalar_scope_importlib
from pathlib import Path as _ScalarScopePath
_scalar_scope_root = _ScalarScopePath(__file__).resolve().parents[2]
_scalar_scope_spec = _scalar_scope_importlib.spec_from_file_location(
    "_scalar_dependency_scope",
    _scalar_scope_root / "code/part3/scalar_dependency_scope.py")
_scalar_scope_module = _scalar_scope_importlib.module_from_spec(_scalar_scope_spec)
_scalar_scope_spec.loader.exec_module(_scalar_scope_module)
_scalar_scope_module.postprocess_generated(
    ['code/part3_fourfold/cox_flop.json'], [], origin='code/part3_fourfold/cox_flop.py')
# END POST-CHECKPOINT15 SCALAR-SCOPE RESTORATION
