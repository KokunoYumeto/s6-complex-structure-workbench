"""Exact normal-jet and inverse-Jacobian computations for Statement C2d."""
import sympy as s

a,b,c,u = s.symbols('a b c u')
delta = a*c-b*b/4
changed = a*(c+b*u+a*u*u)-(b+2*a*u)**2/4
assert s.expand(changed-delta)==0
print('Tacnode numerator ac-b^2/4 invariant under x -> x+u*y^2: exact.')

x,A,B,C,D,lam,mu = s.symbols('x A B C D lam mu')
disc = s.discriminant(A*x**3+B*x**2+C*x+D,x)
scaled = disc.subs({A:A*lam**3,B:B*lam**2*mu,C:C*lam*mu**2,D:D*mu**3}, simultaneous=True)
assert s.expand(scaled-lam**6*mu**6*disc)==0
print('Binary cubic discriminant diagonal weight (det)^6: exact.')
print('Binary cubic discriminant:',disc)

a1,a2,a3 = s.symbols('a1 a2 a3')
tacnode = s.linsolve([a1+a2,a1-a2],(a1,a2))
triple = s.linsolve([-a1,a3,a2,-a3],(a1,a2,a3))
assert tacnode == s.FiniteSet((0,0))
assert triple == s.FiniteSet((0,0,0))
print('Tacnode putative double-pole coefficients:',tacnode)
print('Ordinary triple putative double-pole coefficients:',triple)

def cusp_ring(n):
    return n>=0 and n!=1
inverse_values=[n for n in range(-6,9) if cusp_ring(n+3) and cusp_ring(n+4)]
assert inverse_values==list(range(-1,9))
print('Cusp inverse-Jacobian valuations in [-6,8]:',inverse_values)
print('All exact checks passed.')
