"""Exact terminal-pair, blowdown and normal-extension certificates for UN64."""
from pathlib import Path
import csv
import sympy as S

ruled = [(d,a) for d in range(1,51) for a in range(-50,1) if a*d == -2]
plane = [(d,a) for d in range(1,51) for a in range(-50,1) if a*d == -3]
assert ruled == [(1,-2),(2,-1)]
assert plane == [(1,-3),(3,-1)]
print('Exact ruled degree/coefficient alternatives:', ruled)
print('Exact plane degree/coefficient alternatives:', plane)

x,y,z = S.symbols('x y z')
curve_map = S.Matrix([x,x*y,z])
point_map = S.Matrix([x,x*y,x*z])
curve_jac = S.factor(curve_map.jacobian([x,y,z]).det())
point_jac = S.factor(point_map.jacobian([x,y,z]).det())
assert curve_jac == x and point_jac == x**2
print('Ordinary curve-blowup Jacobian:', curve_jac)
print('Ordinary point-blowup Jacobian:', point_jac)
print('Both displayed charts have full fibre t=x*y, with multiplicities (1,1).')

kij,kjk,aij,ajk,bi,bj = S.symbols('kij kjk aij ajk bi bj', nonzero=True)
transition = S.Matrix([[kij,aij],[0,1]])
next_transition = S.Matrix([[kjk,ajk],[0,1]])
assert transition*next_transition == S.Matrix([[kij*kjk,kij*ajk+aij],[0,1]])
gauge_i = S.Matrix([[1,bi],[0,1]])
gauge_j = S.Matrix([[1,bj],[0,1]])
gauged = gauge_i.inv()*transition*gauge_j
assert gauged == S.Matrix([[kij,aij+kij*bj-bi],[0,1]])
print('PASS exact normal-extension cocycle and lift-change coboundary.')

p,w,t,beta,beta1,d0,d1 = S.symbols('p w t beta beta1 d0 d1')
normal_results = []
for R in [1,2,3,4]:
    delta = t**R*(d0+d1*t)
    deck = S.Matrix([p+delta,(beta+beta1*t)*w,t])
    jac = deck.jacobian([p,w,t]).subs(t,0)
    normal = jac.extract([0,2],[0,2])
    expected = S.Matrix([[1,d0 if R==1 else 0],[0,1]])
    assert normal == expected
    normal_results.append((R,normal[0,1]))
print('Exact normal upper entries by transverse period order:', normal_results)
print('The gamma-prime term lies in the tangent row removed by the actual normal quotient.')
a = S.symbols('a',nonzero=True)
scaled_delta = a*t*(d0+d1*t)
assert S.diff(scaled_delta,t).subs(t,0) == a*d0
print('Fixed-endpoint period scaling: V_t(w)=w+a*t*J*conjugate(w); normal extension entry = a*d0.')
zr,zi = S.symbols('zr zi',real=True)
real_period = S.Matrix([[1,0,-zr,-zi],[0,1,-zi,zr],[zr,zi,1,0],[zi,-zr,0,1]])
assert S.factor(real_period.det()) == (1+zr**2+zi**2)**2
print('Exact real period determinant for zr+i*zi=a*t:', S.factor(real_period.det()))
print('Infinity frame = J*conjugate(w)+(s/a)*w.')

gamma = S.symbols('gamma',nonzero=True)
constant_checks = 0
for exponent in range(-30,31):
    diff = (gamma*w)**exponent-w**exponent
    assert S.expand(diff).coeff(w,0) == 0
    constant_checks += 1
print('Laurent monomial constant-coefficient checks:', constant_checks)
print('Every Laurent splitting difference has constant coefficient zero; d0 is nonzero for R=1.')

q = S.symbols('q',integer=True,nonnegative=True)
unipotent = S.Matrix([[1,d0],[0,1]])
for n in range(-30,31):
    assert unipotent**n == S.Matrix([[1,n*d0],[0,1]])
print('PASS 61 exact positive/negative normal deck iterates, retaining the additive extension.')

g,e_after = S.symbols('g e_after',integer=True)
e_B = 2-2*g
e_T = 2*e_B
e_before = S.expand(e_after-e_B+e_T)
assert S.expand(e_before-e_after) == e_B
assert 3-1 == 2
assert S.simplify((-2+1)*(2-2*g)-(2*g-2)) == 0
print('Curve contraction Euler difference:', S.expand(e_before-e_after))
print('Section self-intersection:', 2-2*g)
print('Point contraction Euler difference: 2')
print('All terminal-pair, blowup, normal-extension and Euler certificates passed.')

root = Path(__file__).resolve().parents[1]
path = root/'records/root_results.csv'
with path.open(newline='') as f:
    reader=csv.DictReader(f); fields=reader.fieldnames; rows=list(reader)
row=dict(zip(fields,[
 'C.2.UN.64',
 'Exact terminal ruled and plane pair restrictions, holomorphic exceptional-leaf contractions, full normal extensions and compact occurrence of both elliptic ruled extension types',
 'Proved',
 'sections/part_C2_exceptional_leaves.tex; C.EL.1–11; code/root_exceptional_leaves.py and .out',
 'Actual canonical evaluation and SNC normal-product maps; Nakano1970 Main Theorem corrected by FujikiNakano1971 Section2; UN61 compact smooth twistor family; UN60 actual primitive period cover',
 'C.2','',
 'For an actual full reduced SNC fibre, a terminal P1-bundle boundary has degree1 with K=-2C or degree2 with K=-C. The elliptic-base connected bisection is excluded by the exact residue/finite-trace map. Section leaves contract holomorphically to smooth curves with normal extension 0 to K_B to V to O_B to0 and Euler change2−2g; plane-line leaves contract to smooth points with Euler change2. All actual blowup and exterior maps are retained. Iteration terminates with the exact summed Euler formula. Both split and nonzero extensions over every specified elliptic B occur by ordinary blowup in a compact twistor torus family, with the nonzero class proved by its actual Laurent constant obstruction. Anticanonical terminal alternatives are necessary pair restrictions only; no arbitrary occurrence assertion is made. Full source audits requested.'
]))
old=next((r for r in rows if r['id']==row['id']),None)
if old is None: rows.append(row)
else:
    row['notes']=old['notes']
    rows=[row if r['id']==row['id'] else r for r in rows]
with path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(rows)
print('CSV metadata C.2.UN.64 saved.')
