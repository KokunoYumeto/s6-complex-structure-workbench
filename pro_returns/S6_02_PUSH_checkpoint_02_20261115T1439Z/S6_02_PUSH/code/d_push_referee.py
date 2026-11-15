"""Independent exact Chern-class check for A.3.2. No numerics."""
import sympy as s
c, j, v, C = s.symbols("c j v C")
computed = s.expand(C*v-(C+c*v)*v+j*v*(c+v))
expected = c*j*v+(j-c)*v**2
assert s.expand(computed-expected) == 0
print("general degree-three corrected class:", s.factor(computed))
substituted = s.expand(computed.subs(j,c))
assert substituted == c**2*v
print("with j=c=F:",substituted)
print("with F^2=0: 0 (as a cohomology class)")
x,y,z,t = s.symbols("x y z t")
correction = ((1+t*z-t*x)*(1+t*z-t*y)/(1+t*z)**2).series(t,0,4).removeO().expand()
G=s.groebner([z**2,x*y],x,y,z)
reduced=sum(G.reduce(correction.coeff(t,k))[1]*t**k for k in range(4))
target = 1-t*(x+y)+t**2*z*(x+y)
assert s.expand(reduced-target) == 0
print("Chern correction, j^2=d0*dinf=0:",reduced)
print("All exact checks passed.")
