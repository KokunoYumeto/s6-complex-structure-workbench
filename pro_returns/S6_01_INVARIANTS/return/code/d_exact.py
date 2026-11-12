"""Exact checks for Parts D and E; no floating-point inference is used.

Run from the deliverable directory with: python code/d_exact.py.
The source archive is not needed for these algebraic checks.
"""
from pathlib import Path
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

def coarse_degree(n):
    r1 = n % 3
    r2 = (3*n) % 4
    return (n-4*r1-3*r2)//12

def monomials(n):
    if n < 0:
        return []
    return [(a,b) for a in range(n//3+1) for b in range(n//4+1)
            if 3*a+4*b == n]

def cohom_stack(n):
    # Method 1: invariant descent to P^1.
    d = coarse_degree(n)
    first = (max(d+1,0),max(-d-1,0))
    # Method 2: weighted Cech monomials and the dual negative monomials.
    second = (len(monomials(n)),len(monomials(-n-7)))
    assert first == second, (n,first,second)
    return first

def tangent_integral(n):
    u = lambda k: cohom_stack(k)[0]
    v = lambda k: cohom_stack(k)[1]
    ep = int(n % 3 != 0)
    h = [u(n)+u(n-1),
         v(n)+v(n-1)+u(n)+u(n-1)+u(n+2),
         v(n)+v(n-1)+v(n+2)+u(n+6)+ep,
         v(n+6)]
    assert h[0]-h[1]+h[2]-h[3] == 1, (n,h)
    return h

x,y,t=s.symbols('x y t')
ks=s.Matrix([[0,y],[y,x]])
delta0=s.Matrix([0,y,y,x])
delta1=s.Matrix([[-y,0],[-x,y]])
assert delta1.det() == -y*y
# Exact cokernel relation: the two nontrivial entries (y,x) have syzygy (x,-y).
assert (s.Matrix([[x,-y]])*s.Matrix([y,x]))[0] == 0

# Cusp local system on a two-torus, evaluated at two exact nontrivial characters.
cusp=[]
for q in [s.Rational(2),s.I]:
    d0=s.Matrix([q-1,0])
    d1=s.Matrix([[0,q-1]])
    assert d1*d0 == s.zeros(1)
    h=[1-d0.rank(),2-d0.rank()-d1.rank(),1-d1.rank()]
    assert h==[0,0,0]
    cusp.append({'character':str(q),'cohomology':h})

# Tangent normal quotient and critical syzygies in the actual smooth local ring.
z=s.symbols('z')
local={
 'xy': {'df':s.Matrix([[y,x,0]]),
        'vertical':s.Matrix([[x,0],[-y,0],[0,1]])},
 'xyz':{'df':s.Matrix([[y*z,x*z,x*y]]),
        'vertical':s.Matrix([[x,x],[-y,0],[0,-z]])},
 's3':{'df':s.Matrix([[3*x*x,0,0]]),
       'vertical':s.Matrix([[0,0],[1,0],[0,1]])},
 's4':{'df':s.Matrix([[4*x**3,0,0]]),
       'vertical':s.Matrix([[0,0],[1,0],[0,1]])}}
for value in local.values():
    assert value['df']*value['vertical'] == s.zeros(1,2)

# Exact elliptic duplication, both substitution and chord-tangent computation.
A=-3*t**3*(t-1)
B=2*t**4*(t-1)**2
xp=s.Integer(0)
yp=s.sqrt(2)*t**2*(t-1)
assert s.simplify(yp**2-(xp**3+A*xp+B)) == 0
slope=s.simplify((3*xp**2+A)/(2*yp))
x2=s.simplify(slope**2-2*xp)
y2=s.simplify(slope*(xp-x2)-yp)
assert s.simplify(x2-s.Rational(9,8)*t**2)==0
assert s.simplify(y2-t**2*(32-5*t)/(16*s.sqrt(2)))==0
ts=s.Rational(32,5)
disc=s.factor(-16*(4*A**3+27*B**2))
assert disc.subs(t,ts)!=0 and yp.subs(t,ts)!=0 and y2.subs(t,ts)==0
assert s.simplify(x2.subs(t,ts)**3+A.subs(t,ts)*x2.subs(t,ts)+B.subs(t,ts))==0

report={
 'weighted_cohomology_two_methods_checked':[-240,240],
 'small_weight_cohomology':{str(n):cohom_stack(n) for n in range(-8,14)},
 'KS_matrix':str(ks), 'KS_determinant':str(ks.det()),
 'delta0':str(delta0),'delta1':str(delta1),
 'integral_twist_cohomology':{str(n):tangent_integral(n) for n in range(-24,25)},
 'local_syzygies':{k:{a:str(b) for a,b in v.items()} for k,v in local.items()},
 'cusp_character_checks':cusp,
 'order_four_section_check':{
    't':str(ts),'P_x':str(xp),'P_y':str(yp.subs(t,ts)),
    'double_x':str(x2),'double_y':str(y2),
    'discriminant':str(disc),'discriminant_at_t':str(disc.subs(t,ts)),
    'exact_order':4},
 'comb_values':{str(m):{'deg_R1O':2*m-1,'h01':2*m+1,'h02':2*m,
                           'dim_Def_lower_bound':8*m-8}
                for m in [12,13,20,100]}}
for n in range(-240,241): cohom_stack(n)
for n in range(-240,241): tangent_integral(n)
(OUT/'d_exact.json').write_text(json.dumps(report,indent=2)+'\n')
print('Exact weighted cohomology: two independent methods agree for -240 <= n <= 240.')
print('All 481 integral tangent-twist Euler characteristics equal 1.')
print('Untwisted tangent cohomology:',tangent_integral(0))
print('KS determinant:',ks.det())
print('Cusp local-system checks:',cusp)
print('The section P has exact order four at t=32/5; discriminant =',disc.subs(t,ts))
print('Wrote outputs/d_exact.json.')
