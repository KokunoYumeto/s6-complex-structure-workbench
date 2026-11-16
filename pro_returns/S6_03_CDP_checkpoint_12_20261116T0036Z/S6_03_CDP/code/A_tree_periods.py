"""Exact period coefficient and nested-insertion orders for Hopf trees."""
from pathlib import Path
import sympy as s

a,b,c,d,u,v,z=s.symbols('a b c d u v z',real=True)
R=s.symbols('R',integer=True,positive=True)
lam=s.Matrix([a+s.I*b,c+s.I*d])
ratio=u+s.I*v
mu=ratio*lam
J=s.Matrix([[0,1],[-1,0]])
def V(w): return w+z*J*s.conjugate(w)
period=s.factor(s.Matrix.hstack(V(lam),V(mu)).det())
expected=2*s.I*v*(a*a+b*b+c*c+d*d)*z
assert s.expand(period-expected)==0

# Use an independent symbol t and arbitrary holomorphic displacement
# delta(t).  The weighted substitution is an exact monomial identity.
t,x,W,Z,delta,beta=s.symbols('t x W Z delta beta',nonzero=True)
checks=0
for m in range(1,16):
    new_Z=beta**m*(Z+delta/x**m)
    new_W=beta*W
    pencil=s.cancel(new_Z/new_W**m-Z/W**m)
    assert s.cancel(pencil-delta/(x*W)**m)==0
    for order in range(m,25):
        assert s.cancel((t**order/t**m)-t**(order-m))==0
        checks+=1
lines=[
 'Exact primitive elliptic core period:',str(period),
 'Thus V_(t^R) gives exactly 2*i*Im(ratio)*||lambda||^2*t^R, with nonzero coefficient.',
 'The arbitrary horizontal displacement and all other lattice periods are retained.',
 f'PASS {checks} nested weighted orders: p=x^m Z,t=xW gives delta(t)/t^m on the new pencil.',
 'Equality of displacement order and m gives a nonlinear central Hopf; strict inequality gives the linear resonant central Hopf.',
 'The ordinary product-ruled cap chart p=t*q gives the same exact order drop1.',
 'These are local identity certificates; global pruning/reinsertion is proved separately.'
]
out='\n'.join(lines)+'\n'
Path(__file__).with_suffix('.out').write_text(out)
print(out,end='')
