"""Exact certificates for the local modules in Part A.
The finite exponent scans accompany, but do not replace, the analytic proofs.
Run: python3 code/A_local_algebra.py
"""
import sympy as s
x,y,z,t,u,v=s.symbols('x y z t u v')

def reduce_vec(vec,f):
    gb=s.groebner([f],x,y,z,order='lex')
    return [s.expand(gb.reduce(s.expand(e))[1]) for e in vec]

def checked(label,expr,f):
    rem=reduce_vec(expr,f)
    assert rem==[0,0,0],(label,rem)
    print(label+': exact remainder '+str(rem))

fc=x*x-y**3
dc=s.Matrix([2*x,-3*y*y,0])
tc=s.Matrix([2*y,-3*x,0])
checked('cusp x*tau = y*dF',x*tc-y*dc,fc)
checked('cusp y^2*tau = x*dF',y*y*tc-x*dc,fc)
assert s.expand((tc[0]*3*t*t+tc[1]*2*t).subs({x:t**3,y:t*t}))==0
print('cusp normalization pullback of tau: 0')
H=lambda n:n==0 or n>=2
inv=[n for n in range(-6,11) if H(n+3) and H(n+4)]
assert inv==list(range(-1,11))
print('cusp inverse-J exponents in [-6,10]:',inv)
print('cusp inverse-J/R exponent basis:',[n for n in inv if not H(n)])

fp=x*x-y*y*z
dp=s.Matrix([2*x,-2*y*z,-y*y])
tp=s.Matrix([2*y*z,-2*x*z,-x*y])
checked('pinch y*tau = x*dF',y*tp-x*dp,fp)
checked('pinch x*tau = yz*dF',x*tp-y*z*dp,fp)
pull=tp.subs({x:u*v,y:u,z:v*v})
assert s.expand(pull[0]*v+pull[1])==0
assert s.expand(pull[0]*u+pull[2]*2*v)==0
print('pinch normalization pullback of tau: (0,0)')
def inR(a,b):return a>=0 and b>=0 and (a>=1 or b%2==0)
allowed=[]
for a in range(-4,7):
    for b in range(-4,9):
        if all(inR(a+i,b+j) for i,j in [(1,1),(1,2),(2,0)]):
            allowed.append((a,b))
expect=[(a,b) for a in range(0,7) for b in range(0,9)]
assert allowed==expect
print('pinch inverse-J monomial scan [-4,6]x[-4,8]: exactly nonnegative exponents')

for r in [1,2,3]:
    coords=[x,y,z][:r]
    F=s.prod(coords)
    grad=s.Matrix([s.diff(F,c) for c in [x,y,z]])
    entries=[s.diff(F,c) for c in coords]
    print(f'normal crossings r={r}: F={F}, branch kernel generators={entries}')
    assert sum((s.Matrix([entries[i] if j==i else 0 for j in range(3)]) for i in range(r)),s.zeros(3,1))==grad
print('ALL EXACT CHECKS PASSED')
