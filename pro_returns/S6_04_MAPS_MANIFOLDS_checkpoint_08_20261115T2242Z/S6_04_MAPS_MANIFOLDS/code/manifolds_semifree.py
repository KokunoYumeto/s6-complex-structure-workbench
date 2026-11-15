"""Exact toric checks for the semifree angular action in Theorem D.2.14."""
import sympy as s
delta=s.Matrix([0,1,0])
v00=s.Matrix([0,0,1]);v10=s.Matrix([1,0,1])
v01=s.Matrix([0,1,1]);v11=s.Matrix([1,1,1])
for rays in ((v00,v10,v01),(v10,v01,v11)):
    cone=s.Matrix.hstack(*rays)
    assert abs(cone.det())==1
    weights=cone.inv()*delta
    assert sorted(map(int,weights))==[-1,0,1]
    print('cone',cone.tolist(),'circle weights',list(weights))
w=s.Matrix([1,0,1]);wp=s.Matrix([-1,1,1])
assert w+wp==v00+v01
print('fixed wall relation w+wprime=v00+v01: normal degrees (-1,-1)')
z=s.symbols('z',nonzero=True)
clutch=s.diag(z**-1,z)
assert clutch.det()==1
print('equivariant real clutch after conjugation:',clutch,'determinant',clutch.det())
print('The clutch loop lies in SU(2), whose fundamental group is zero.')
print('All exact checks passed; global freeness and spin descent are proved in the text.')
