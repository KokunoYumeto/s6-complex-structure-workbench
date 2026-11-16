"""Exact local checks for the moving-zero conifold family."""
import sympy as s
x,y,z,v,u,a,b,ss=s.symbols('x y z v u a b s')
F=x*y-u*(z*v-ss)
print('Family equation:',F)
print('Relative gradient:',[s.diff(F,t) for t in [x,y,z,v]])
print('Total derivative in smoothing parameter:',s.diff(F,ss))
print('Relative critical point equation:',F.subs({x:0,y:0,z:0,v:0}))
H=s.hessian(F,[x,y,z,v]); print('Hessian determinant:',s.factor(H.det()))
assert s.factor(H.det())==u**2
print('First small-resolution chart equation:',s.expand(F.subs({x:a*z,v:a*y/u,ss:0})))
print('Second small-resolution chart equation:',s.expand(F.subs({z:b*x,y:b*u*v,ss:0})))
assert s.expand(F.subs({x:a*z,v:a*y/u,ss:0}))==0
assert s.expand(F.subs({z:b*x,y:b*u*v,ss:0}))==0
print('Resolution normal transition: (x,u v)=a*(z,y), b=1/a.')
print('Surgery homology ranks:',[1,0,0,2,0,0,1])
print('Euler characteristic:',sum((-1)**i*n for i,n in enumerate([1,0,0,2,0,0,1])))
print('All assertions passed.')
