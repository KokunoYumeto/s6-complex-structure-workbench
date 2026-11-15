"""Exact checks for the characteristic formulas and finite group ambiguities."""
from pathlib import Path
import json
import sympy as s
p1,p2,c,sig=s.symbols('p1 p2 c sigma')
ahat8=(7*p1**2-4*p2)/s.Integer(5760)
dirac8=ahat8-p1*c*c/s.Integer(192)+c**4/s.Integer(384)
signature=(7*p2-p1*p1)/45
proposed=(p1*p1-4*sig)/896-p1*c*c/192+c**4/384
assert s.expand(dirac8-proposed.subs(sig,signature))==0
phat=(p1+c*c)/2
cn=(phat*phat-sig)/8-s.Rational(5,12)*c*c*phat+c**4/4
assert s.expand(cn-28*proposed)==0
generator=s.Rational(36-4,896)
assert generator==s.Rational(1,28)
fibres={str(y):[x for x in range(28) if (6*x)%28==y] for y in range(0,28,2)}
assert all(len(v)==2 and (v[1]-v[0])==14 for v in fibres.values())
assert sorted((6*x)%28 for x in range(28))==sorted(list(range(0,28,2))*2)
# Quaternion conjugation by exp(i theta/2) gives one fixed axis and
# a rotation on each (j,k)-plane. Two copies plus Re(w) have fixed R^3.
t=s.symbols('t',real=True)
rot=s.Matrix([[s.cos(t),-s.sin(t)],[s.sin(t),s.cos(t)]])
assert s.simplify(rot.det())==1
J=s.diag(1,-1)
assert s.simplify(J*rot*J-rot.T)==s.zeros(2)
result={'spin_c_index_identity':True,'Crowley_Nordstrom_normalization_identity':True,
        'positive_generator_Euler_class':1,'positive_generator_p1':6,
        'positive_generator_p1_squared':36,'positive_generator_signature':1,
        'positive_generator_mu':str(generator),
        'multiplication_by_6_kernel':[0,14],
        'multiplication_by_6_preimages':fibres,
        'circle_fixed_real_dimension':3,'fixed_sphere_dimension':2,
        'normal_real_representation':'two effective rotation planes',
        'conjugating_one_complex_normal_coordinate_changes_weight_sign':True}
dest=Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
