"""Exact normalized conormal jets for the (3,4,5) space curve.

This certifies the algebra used in the low-delta A2/A3 investigation.
It does not assert a classification of curve germs or a global Euler sign.
"""
from pathlib import Path
import sympy as s

x, y, z, t, u, av, bv = s.symbols('x y z t u av bv')
variables = (x, y, z)
param = {x: t**3, y: t**4, z: t**5}
gs = [y**2-x*z, y*z-x**3, z**2-x**2*y]
special = x**5+x*y**3+z**3-3*x**2*y*z
products = [a*b for i, a in enumerate(gs) for b in gs[i:]]
sat_basis = s.groebner(products+[1-u*x], u, z, y, x, order='lex')
sat = [p.as_expr() for p in sat_basis.polys if not p.as_expr().has(u)]
candidate = s.groebner(products+[special], z, y, x, order='lex')
assert s.expand(x*special-(gs[1]**2-gs[0]*gs[2])) == 0
assert s.expand(y*special-(gs[1]*gs[2]+x*gs[0]**2)) == 0
assert s.expand(z*special-(gs[2]**2+x*gs[0]*gs[1])) == 0
assert all(candidate.reduce(p)[1] == 0 for p in sat)
assert s.groebner(sat, z, y, x, order='lex').reduce(special)[1] == 0

grad = lambda p: s.Matrix([s.diff(p,v).subs(param) for v in variables])
a = grad(gs[0])
b = grad(gs[1])+t*a
assert grad(gs[2]) == -2*t**2*a+t*b
tangent = s.Matrix([3*t**2,4*t**3,5*t**4])
assert a.cross(b) == t**6*tangent
A = s.Matrix([0,0,-t**-3])
B = s.Matrix([0,s.Rational(1,3)*t**-5,s.Rational(2,3)*t**-4])
assert (a.dot(A),a.dot(B),b.dot(A),b.dot(B)) == (1,0,0,1)
H = s.hessian(special,variables).subs(param)/2
q = 3/t*a*a.T-s.Rational(3,2)/t**2*(a*b.T+b*a.T)+t**-3*b*b.T
assert s.simplify(H-q) == s.zeros(3)
assert s.det(s.Matrix([[3/t,-s.Rational(3,2)/t**2],[-s.Rational(3,2)/t**2,t**-3]])) == s.Rational(3,4)/t**4

v = av*A+bv*B
def directional(p, order):
    # Coefficients of v are held fixed while taking ambient derivatives.
    q = p
    for _ in range(order):
        q = sum(v[i]*s.diff(q,variables[i]) for i in range(3))
    return s.expand(q.subs(param))

def pole_order(expr):
    if expr == 0:
        return 0
    terms = s.Add.make_args(s.expand(expr))
    return max(0, -min(int(term.as_powers_dict().get(t,0)) for term in terms))

second_g = [directional(g,2) for g in gs]
cubic_f = directional(special,3)
assert max(map(pole_order,second_g)) == 10
assert pole_order(cubic_f) == 12
assert max(pole_order(directional(p,3)) for p in products) <= 10

# The other non-lci delta-two germ: a cusp plus a transverse line.
cs = [x*z,y*z,y**2-x**3]
cf = z*cs[2]
cp = [a*b for i,a in enumerate(cs) for b in cs[i:]]
cgb = s.groebner(cp+[1-u*(x+z)],u,z,y,x,order='lex')
csat = [p.as_expr() for p in cgb.polys if not p.as_expr().has(u)]
cand = s.groebner(cp+[cf],z,y,x,order='lex')
assert all(cand.reduce(p)[1] == 0 for p in csat)
assert s.groebner(csat,z,y,x,order='lex').reduce(cf)[1] == 0
assert s.expand(x*cf-cs[0]*cs[2]) == 0
assert s.expand(y*cf-cs[1]*cs[2]) == 0
assert s.expand(z*cf-(cs[1]**2-x*cs[0]**2)) == 0
cpole = []
cdefect = []
for pr, aa, bb, der, defect in [
    ({x:t**2,y:t**3,z:0},s.Matrix([0,0,t**-2]),
     s.Matrix([0,s.Rational(1,2)*t**-3,0]),s.Matrix([2*t,3*t**2,0]),4),
    ({x:0,y:0,z:t},s.Matrix([t**-1,0,0]),
     s.Matrix([0,t**-1,0]),s.Matrix([0,0,1]),2),
]:
    cg = [s.Matrix([s.diff(g,k).subs(pr) for k in variables]) for g in cs]
    basis = (cg[0],cg[2]) if pr[z] == 0 else (cg[0],cg[1])
    wedge = basis[0].cross(basis[1])
    assert wedge == (-t**defect*der if pr[z] == 0 else t**defect*der)
    assert (basis[0].dot(aa),basis[0].dot(bb),
            basis[1].dot(aa),basis[1].dot(bb)) == (1,0,0,1)
    vv = av*aa+bv*bb
    hp = [s.expand((vv.T*s.hessian(g,variables).subs(pr)*vv)[0]) for g in cs]
    cpole.append(max(map(pole_order,hp)))
    cdefect.append(defect)
assert cpole == [6,2]
assert cdefect == [4,2]

# Independent audit of the symbolic cubes used for ordinary-triple images.
cube_checks=[]
for name, generators, extra, nonzerodivisor in [
    ('345',gs,special,x),
    ('cusp_line',cs,cf,x+z),
    ('three_axes',[x*y,x*z,y*z],x*y*z,x+y+z),
]:
    cube=[generators[i]*generators[j]*generators[k]
          for i in range(3) for j in range(i,3) for k in range(j,3)]
    cg=s.groebner(cube+[1-u*nonzerodivisor],u,z,y,x,order='lex')
    sat3=[p.as_expr() for p in cg.polys if not p.as_expr().has(u)]
    expected=s.groebner(cube+[extra*g for g in generators],z,y,x,order='lex')
    back=s.groebner(sat3,z,y,x,order='lex')
    assert all(expected.reduce(p)[1]==0 for p in sat3)
    assert all(back.reduce(extra*g)[1]==0 for g in generators)
    cube_checks.append(name+': I^(3)=I^3+F I; saturated basis length '+str(len(sat3)))

lines = [
    'EXACT: I^(2)=I^2+(F), via saturation by x.',
    'F = '+str(special),
    'xF=g2^2-g1g3; yF=g2g3+xg1^2; zF=g3^2+xg1g2. Hence mF is contained in I^2.',
    'Saturation Groebner basis: '+str(sat),
    'a = '+str(list(a)),
    'b = '+str(list(b)),
    'dg3 = -2 t^2 a + t b',
    'a cross b = t^6 gamma_prime; determinant defect = 6.',
    'A = '+str(list(A)),
    'B = '+str(list(B)),
    'q_F = (3/t) a^2 -(3/t^2) ab +(1/t^3) b^2',
    'det(q_F) = 3/(4 t^4)',
    'D^3 F(av A+bv B)^3 = '+str(cubic_f),
    'Raw F cubic pole = 12; coefficient in m_D has valuation at least 3.',
    'Hessians of defining generators = '+str(second_g),
    'Maximum generator Hessian pole = 10.',
    'I^2 cubic pole bound = 10, including coefficient derivatives of pole <=5.',
    'For c in m_D, cF cubic pole <=max(12-3,5+3)=9.',
    'Thus every rank-one symbolic-square Hessian is regular and its radical cubic has pole <=10.',
    'GLOBAL USE: det(N) degree = -2+6 = 4 on a rational critical image with this sole singularity.',
    'A2 would force deg R >=4 from q, but 3 deg R <=10 from the nonzero cubic: impossible.',
    'CUSP+LINE: I^(2)=I^2+(z(y^2-x^3)), via saturation by x+z.',
    'Its maximal ideal annihilates the symbolic-square quotient by the three displayed identities.',
    'Normalized determinant defects on cusp/line branches = '+str(cdefect)+'.',
    'Normalized generator Hessian/cubic pole bounds on cusp/line = '+str(cpole)+'.',
    'Their total cubic pole 8 is less than 3*deg R >=12, excluding A2 as well.',
    'Independent exact symbolic-cube audit: '+'; '.join(cube_checks)+'.',
    'No analytic classification or unrestricted Euler assertion is supplied by this script.',
]
output='\n'.join(lines)+'\n'
print(output,end='')
Path(__file__).with_suffix('.out').write_text(output)
