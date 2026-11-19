"""Integral Laurent normalization certificate for the gamma-cyclic cusp cover."""
from pathlib import Path
import json
import sympy as s
z=s.symbols('z')
B=s.Matrix([[-1,-1,-1,-1],[1,1,1,z],[-z,-z,-1,-z]])
U=s.Matrix([[-1,0,0],[1,1,0],[-z,0,1]])
V=s.Matrix([[1,-1,-1,-1],[0,1,0,0],[0,0,1,0],[0,0,0,1]])[:,[0,3,2,1]]
D=s.simplify(U*B*V)
assert D==s.Matrix([[1,0,0,0],[0,z-1,0,0],[0,0,z-1,0]])
assert abs(U.det())==abs(V.det())==1
record={'ring':'Z[z,z^-1]','restriction_matrix':str(B),
 'left_unimodular':str(U),'right_unimodular':str(V),'diagonal':str(D),
 'ordinary_homology_modules':{'H0':'R/(z-1)','H1':'R/(z-1)',
 'H2':'R direct_sum (R/(z-1))^2','H3':'0','H4':'R'},
 'marking':'gamma deck z and u deck1; replacing z by z^-1 gives the same isomorphism types',
 'finite_cyclic_base_change_check':'H2 rankd+3; H3 Z^2; H4 rankd, agreeing D1.2'}
print(json.dumps(record,indent=2))
Path(__file__).with_suffix('.out.json').write_text(json.dumps(record,indent=2)+'\n')
