
A=s.Matrix([[0,-1],[1,1]])
assert A**6==s.eye(2) and (A-s.eye(2)).det()==1
print('Secondary Kodaira A:', A.tolist())
print('Secondary Kodaira coinvariant Smith diagonal:',
      list(smith_normal_form(A-s.eye(2),domain=ZZ).diagonal()))
x,y,z=s.symbols('x y z')
sigma=s.Matrix([-y,x+y,z-y/2])
q=s.Matrix([x,y,z])
for k in range(6):
    q=sigma.subs({x:q[0],y:q[1],z:q[2]}, simultaneous=True).applyfunc(s.expand)
assert q==s.Matrix([x,y,z])
print('Secondary Kodaira sigma^6:', list(q))
print('Lattice preservation difference:', s.expand((z-y/2)-(-y)*(x+y)/2-(z-x*y/2)))
print('This equals xy+y(y-1)/2, an integer at integer x,y.')
