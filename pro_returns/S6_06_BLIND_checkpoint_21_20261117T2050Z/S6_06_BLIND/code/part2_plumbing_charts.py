"""Exact local equation checks for the two-component untwisted plumbing."""
import sympy as S
z,w,r,x,y,a,b,k=S.symbols('z w r x y a b k')
f=z*w-r*x*y
assert S.expand(f.subs({r:z*a,w:a*x*y}, simultaneous=True))==0
assert S.expand(f.subs(z,r*b)-r*(b*w-x*y))==0
g=b*w-x*y
assert S.expand(g.subs({b:x*k,y:k*w}, simultaneous=True))==0
assert S.expand(g.subs({x:b*k,w:k*y}, simultaneous=True))==0
print('Original neck:',f)
print('Component blowup chart1: r=z*a, w=a*x*y; smooth affine C4.')
print('Component blowup chart2 strict transform:',g,'with independent r.')
print('Small resolution chart1: b=x*k, y=k*w; smooth affine C4.')
print('Small resolution chart2: x=b*k, w=k*y; smooth affine C4.')
print('Involution: r -> -r, z -> z, w -> -w, x,y fixed.')
assert S.expand(f.subs({r:-r,w:-w}, simultaneous=True)+f)==0
assert S.expand(g.subs({b:-b,w:-w}, simultaneous=True)-g)==0
print('It preserves (z,r) and (b,x); every equation checked exactly.')
print('Global gluing and identification with the prescribed A2 fan are separate proof obligations.')
