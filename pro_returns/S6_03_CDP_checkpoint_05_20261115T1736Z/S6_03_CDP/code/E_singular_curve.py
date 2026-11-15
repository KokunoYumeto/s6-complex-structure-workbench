"""Exact conductor-cleared cubic/quartic and discriminant identities in A.5.5."""
import sympy as s
x,z,w,t=s.symbols('x z w t')
h=z**2-x**3
f=x*w**2+2*z*w*h+x**2*h**2+h**3
square=x*(w+z*h/x)**2+(1-1/x)*h**3
assert s.cancel(f-square)==0
cleared=x**2*f-x*(x*w+z*h)**2
assert s.expand(cleared-x*(x-1)*h**3)==0
q=s.Matrix([[x,z],[z,x**2]])
assert s.factor(q.det())==-h
qn=q.subs({x:t**2,z:t**3})
assert qn==t**2*s.Matrix([1,t])*s.Matrix([[1,t]])
print('A.5.5 Hessian determinant:',s.factor(q.det()))
print('A.5.5 normalized Hessian:',qn)
print('A.5.5 conductor-cleared quotient:',s.factor(cleared/h**3))
print('A.5.5 radical cubic on normalization:',1-t**-2)
print('A.5.5 conductor exponent 2; actual cubic pole order 2; proved upper bound 4')

# The two successive conductor clearings and exact square completion.
a,d,P,H,K,F=s.symbols('a d P H K F')
G=d**2*F-a*P**2
K_def=d**2*G-P*H
identity=4*a*d**6*F-(2*a*d**2*P+H)**2-(4*a*d**2*K_def-H**2)
assert s.expand(identity)==0
C2,KR=s.symbols('C2 KR')
radial=s.cancel(a*KR/d**4-(d*C2)**2/(4*d**6))
assert s.cancel(radial-(a*KR-C2**2/4)/d**4)==0
b,e,u=s.symbols('b e u')
assert s.expand(a*(e+b*u+a*u**2)-(b+2*a*u)**2/4-(a*e-b**2/4))==0
g,c,q=s.symbols('g c q')
assert s.expand(-2*q-4*(2*g-2+c-q)+4*c)==-8*g+8+2*q
print('A.5.5 conductor-cleared fourth-order square identity: exact')
print('A.5.5 quartic invariant:',radial)
print('A.5.5 quartic normal-shift invariance: exact')
print('A.5.5 corrected quartic degree:',-8*g+8+2*q)

# The invariant transformation is checked directly for a binary cubic.
A,B,C,D,u,v,aa,bb,cc,dd=s.symbols('A B C D u v aa bb cc dd')
poly=A*u**3+B*u**2*v+C*u*v**2+D*v**3
disc=s.discriminant(poly.subs(v,1),u)
assert s.expand(disc-(B**2*C**2-4*A*C**3-4*B**3*D-27*A**2*D**2+18*A*B*C*D))==0
# Diagonal, elementary shear, and interchange generate GL2.
for U,V,det in [(aa*u,dd*v,aa*dd),(u+bb*v,v,1),(v,u,-1)]:
    pp=s.Poly(s.expand(poly.subs({u:U,v:V},simultaneous=True)),u,v)
    coeff=[pp.coeff_monomial(u**3),pp.coeff_monomial(u**2*v),
           pp.coeff_monomial(u*v**2),pp.coeff_monomial(v**3)]
    changed=disc.subs(dict(zip((A,B,C,D),coeff)),simultaneous=True)
    assert s.expand(changed-det**6*disc)==0
print('A.5.5 binary cubic discriminant determinant weight six: exact generator checks passed')

# A.5.7 uses the indicated action of the reduced conductor ring, rather
# than the componentwise action on the split ribbon.
ss=s.symbols('ss')
af,bf,cf,uf=[s.Function(n)(ss) for n in ('af','bf','cf','uf')]
phi_product=af*cf+uf*s.diff(af,ss)*bf-uf*s.diff(af*bf,ss)
phi_linear=af*(cf-uf*s.diff(bf,ss))
assert s.expand(phi_product-phi_linear)==0
assert s.expand((z**3)**2-(z**2)**3)==0
print('A.5.7 derivation-graph quotient A-linearity: exact product-rule check passed')
print('A.5.7 cusp normalization generators z^2 and z^3 satisfy y^2=x^3 exactly')
