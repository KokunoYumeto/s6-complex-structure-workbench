"""Exact certificates for F=x^2-y^4*z^3 and its vertical residue pole."""
import sympy as s

x, y, z, u, v = s.symbols('x y z u v')
F = x**2-y**4*z**3
sub = {x:u**2*v**3, y:u, z:v**2}
grad = [s.diff(F,t) for t in (x,y,z)]
vertical = [2*y**2*z, -4*x*y*z, -3*x*y**2]
generator = [2*y*z, -4*x*z, -3*x*y]
print('normalization equation:', s.expand(F.subs(sub)))
print('fraction field identity x/(y^2*z)=v:', s.cancel((x/(y**2*z)).subs(sub)))
for name, coeffs, multiplier in [('vertical pole',vertical,1/v),
                                 ('torsion generator',generator,1/(u*v))]:
    identities=[s.cancel(c.subs(sub)-multiplier*g.subs(sub))
                for c,g in zip(coeffs,grad)]
    du=s.expand(sum(c.subs(sub)*s.diff(sub[t],u)
                    for c,t in zip(coeffs,(x,y,z))))
    dv=s.expand(sum(c.subs(sub)*s.diff(sub[t],v)
                    for c,t in zip(coeffs,(x,y,z))))
    print(name,'gradient identities:',identities)
    print(name,'normalization pullback du,dv:',du,dv)
    assert identities==[0,0,0] and du==dv==0
print('x/(u*v)=',s.cancel(sub[x]/(u*v)))
print('y^3*z^2/(u*v)=',s.cancel((y**3*z**2).subs(sub)/(u*v)))

def in_R(a,b):
    return a>=0 and b>=0 and (b%2==0 or (a>=2 and b>=3))

checked=0
for a in range(-4,12):
    for b in range(-6,16):
        actual=all(in_R(a+c,b+d) for c,d in [(2,3),(3,6),(4,4)])
        predicted=((a>=0 and b>=0 and b%2==0)
                   or (a>=-1 and b>=-1 and b%2==1))
        assert actual==predicted,(a,b,actual,predicted)
        checked+=1
print('exact monomial certificate points:',checked)
print('J_inverse=A0 direct_sum (u*v)^(-1)*A0, A0=C{u,v^2}')
print('J_inverse/B=A0/(u*v^2) times (u*v)^(-1)')
print('torsion=R/(x,y^3*z^2), generator 2*y*z*dx-4*x*z*dy-3*x*y*dz')
print('Finite scan is a check; the paper proves the complete analytic module.')
