"""Exact lattice audit for B.4.31; geometric finite-orbit proof is in TeX."""
import json
from pathlib import Path
import sympy as s

A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
delta=s.Matrix([0,0,0,1])
gamma=s.Matrix([[1,0,0,0]])
E=delta*gamma
M1=A1[1:3,1:3]
M2=A2[1:3,1:3]
U=M1*M2
V=M2*U*M2.inv()
k,l=s.symbols('k l', integer=True, positive=True)
Uk=s.eye(2)+k*(U-s.eye(2))
Vl=s.eye(2)+l*(V-s.eye(2))
stack=(Uk-s.eye(2)).col_join(Vl-s.eye(2))
minor=stack.extract([1,2],[0,1]).det()

checks={
  'A1_order_three':A1**3==s.eye(4),
  'A2_order_four':A2**4==s.eye(4),
  'delta_primitive_and_fixed':list(delta)==[0,0,0,1] and A1*delta==delta and A2*delta==delta,
  'gamma_fixed':gamma*A1==gamma and gamma*A2==gamma,
  'commute_with_rank_one_nilpotent':A1*E==E*A1 and A2*E==E*A2 and E**2==s.zeros(4),
  'elliptic_quotients':M1==s.Matrix([[0,1],[-1,-1]]) and M2==s.Matrix([[0,-1],[1,0]]),
  'lower_unipotent':U==s.Matrix([[1,0],[-1,1]]),
  'upper_unipotent':V==s.Matrix([[1,1],[0,1]]),
  'no_common_nonzero_fixed_vector':s.factor(minor)==k*l,
}
assert all(checks.values()),checks
data={
  'checks':checks,
  'matrices':{name:[list(row) for row in mat.tolist()] for name,mat in [('A1',A1),('A2',A2),('M1',M1),('M2',M2),('U',U),('V',V)]},
  'positive_power_fixed_space_minor':str(s.factor(minor)),
  'scope':'Finite orbit implies fixation by positive powers of U and V; their common fixed space is zero. The compact-stratum meridian transport and the treatment of multiplicities are proved geometrically in B.4.31.'
}
for name,value in checks.items():
    print(f'{name}: {"PASS" if value else "FAIL"}')
print(f'fixed-space minor for arbitrary positive powers: {s.factor(minor)}')
print(data['scope'])
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2,default=str)+'\n')
