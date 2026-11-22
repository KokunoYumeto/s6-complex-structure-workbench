import sympy as S
# Check the actual extension of the volume form through xy=t.
x,y,zz=S.symbols('x y z',nonzero=True)
coefficient=S.Matrix([[y,x,0],[1/x,0,0],[0,0,1]]).det()
assert coefficient==-1
assert S.Matrix([[0,1,0],[1,0,0],[0,0,1]]).det()==coefficient
print('PASS exact wedge sign: d(xy) wedge dx/x wedge dz = dy wedge dx wedge dz.')
