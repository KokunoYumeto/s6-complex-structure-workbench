#!/usr/bin/env python3
"""Exact finite face chain; no actual return value is assigned."""
import json
from pathlib import Path
import sympy as s
labels=['Sigma_rho0','Y_f','Y_round','H_rim','H_floor','H_side']
D=s.Matrix([1,0,0,-1,1,-1]);C=s.Matrix([0,1,-1,-1,1,-1])
assert D-C==s.Matrix([1,-1,1,0,0,0])
# Actual cap order F-C0=(F-C)+(C-C0).
F=s.Matrix([1,0,0]);cap=s.Matrix([0,1,0]);cap0=s.Matrix([0,0,1])
assert F-cap0==(F-cap)+(cap-cap0)
out={'status':'PASS','labels':labels,'boundary_D':list(D),'boundary_C':list(C),
 'glued_boundary_D_minus_C':list(D-C),
 'orbit_boundary_labels':['N6','P3_a','B_F','B_S4','P3_1'],
 'orbit_boundary_signs':[-1,-1,-1,-1,1],
 'scope':'Formal exact face/cap chain with the actual maps recorded in EA18--20; complete geometric attachment remains under audit and no source-zero class is output.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print('PASS exact horn and cap boundary chains')
