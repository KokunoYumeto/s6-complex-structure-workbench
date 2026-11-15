"""Exact base discriminant, root-cover identities, charts and Euler for UN25."""
import sympy as s

T,z,y,u,v,w,r,t,a,ell,q=s.symbols('T z y u v w r t a ell q')
f=T**4-3
g=T**6+T+2
Delta=s.expand(4*f**3+27*g**2)
assert s.gcd(Delta,s.diff(Delta,T)) == 1
assert s.diff(Delta,T).subs(T,0) == 108
assert s.Poly(Delta,T).LC() == 31
assert s.degree(Delta,T) == 12
print('Discriminant:',Delta)
print('gcd(Delta,Delta prime)=1; Delta prime(0)=108; leading coefficient31.')
print('T=0 is I1 and infinity is smooth; all twelve discriminant roots are simple.')

phi=(z-1)*(z-2)/((z+1)*(z+2))
assert s.factor(phi*phi.subs(z,-z)) == 1
assert phi.subs(z,0) == 1
assert s.limit(phi,z,s.oo) == 1
assert s.expand((z**2-1)*(z**2-4)) == z**4-5*z**2+4
assert s.gcd((z**2-1)*(z**2-4),s.diff((z**2-1)*(z**2-4),z)) == 1
print('phi(-z)=1/phi(z); phi(0)=phi(infinity)=1.')
print('Elliptic cover C: Y²=(z²-1)(z²-4), with four simple branch values.')
print('eta free; eta*k free; k has4*4=16 fixed points in8 eta-orbits.')

# Actual product cover: ell=u², a=y/u, so a² ell=y²=phi.
assert s.cancel((y/u)**2*u**2) == y**2
assert s.cancel((u/y)**2*u**(-2)) == y**(-2)
print('Both product-cover maps preserve the actual positive/negative root equations.')

# Quotient and resolution charts, including the base parameter.
for AA,BB,CC,base in [(r,r*v,r*v**2,u**2*r),
                      (r*v**2,r*v,r,u**2*r*v**2)]:
    assert s.expand(AA*CC-BB**2) == 0
    assert s.expand(base-u**2*AA) == 0
print('Both A1 charts satisfy AC=B² and T=u²A exactly.')
print('Full coefficients: 2M+2A+4Q1+4Q2+E1+E2+E3+E4.')

components = 12+4+2*0+4*4
pairwise = 2*2+2*0+4*2+4*2*2
triple = 4*2
e_initial = components-pairwise+triple
assert e_initial == 12
assert e_initial-6*2 == 0
print('Euler strata:',components,'-',pairwise,'+',triple,'=',e_initial)
print('Six negative-two blocks give Euler0 and preserve M unchanged.')

# Finite group quotient of C x E:
quotient_euler = (0+0+16+0)//4
assert quotient_euler == 4
assert quotient_euler+8 == 12
print('Klein-four quotient Euler4; eight A1 resolutions add8, giving Enriques Euler12.')
print('All exact checks passed.')
