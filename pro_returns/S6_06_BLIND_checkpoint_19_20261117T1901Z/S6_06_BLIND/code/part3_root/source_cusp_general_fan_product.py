"""Exact checks for the full-unit fan product and actual local circle traces.

The proof of the universal assertions is GF.1--4. The bounded enumeration
checks every integral basis with entries in [-8,8]; it assigns no uncomputed
global return or transverse variation/derivative entry.
"""
from pathlib import Path
from datetime import datetime, timezone
from itertools import product
from math import gcd
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
checks = []

def check(name, value):
    assert bool(value), name
    checks.append(name)

def zero(x):
    return S.simplify(x) == 0

def qmul(x, y):
    a,b,c,d = x
    e,f,g,h = y
    return S.Matrix([a*e-b*f-c*g-d*h,
                     a*f+b*e+c*h-d*g,
                     a*g-b*h+c*e+d*f,
                     a*h+b*g-c*f+d*e])

def qbar(x):
    return S.Matrix([x[0], -x[1], -x[2], -x[3]])

p,r,q,s = S.symbols('p r q s')
P = S.Matrix([[p,r],[q,s]])
R = P.inv()
BP = -6 * R * S.Matrix([[1,0],[0,0]]) * P
check('symbolic_character_period_inverse', all(zero(x) for x in R*P-S.eye(2)))
check('symbolic_period_winding_trace', zero(S.trace(BP)+6))
check('symbolic_period_winding_rank_one', zero(BP.det()))
check('symbolic_period_winding_square', all(zero(x) for x in BP*BP+6*BP))

a,b,c = S.symbols('a b c', nonzero=True)
A11,A12,A21,A22 = S.symbols('A11 A12 A21 A22', nonzero=True)
rows = [
    (A11*A21*b*c, A21**-1*a*b, A11**-1*b**-1),
    (A12*A22*b*c, A22**-1*c**-1, A12**-1*a*c),
    (a**-1, a*b, a*c)
]
for i,row in enumerate(rows):
    check(f'actual_height_{i}', zero(S.prod(row)-a*b*c))
u,v,w = rows[0]
check('native_C0_tangent', zero(A11*w-b**-1))
check('native_C0_normal0', zero(A21*v-b*a))
check('native_C0_normal1', zero(u/(A11*A21)-b*c))
u,v,w = rows[1]
check('native_C1_tangent', zero(A22*v-c**-1))
check('native_C1_normal0', zero(A12*w-c*a))
check('native_C1_normal1', zero(u/(A12*A22)-c*b))
u,v,w = rows[2]
check('native_C2_tangent', zero(u-a**-1))
check('native_C2_normal0', zero(v-a*b))
check('native_C2_normal1', zero(w-a*c))
for i,D in enumerate([(A22/A21,A11*A21),(A11/A12,A12*A22),(A22,A11)]):
    check(f'full_normal_determinant_{i}', zero(S.prod(D)-A11*A22))

dd = S.symbols('d', real=True)
unit_i = S.Matrix([0,1,0,0])
unit_j = S.Matrix([0,0,1,0])
unit_k = S.Matrix([0,0,0,1])
H = unit_j
dH_rad = S.Matrix([-2,0,0,0])
dH_ang = S.Matrix([0,-dd/2,0,dd/2])
for name,dH,expect,expect_inverse in [
    ('radial',dH_rad,4*unit_k,-4*unit_k),
    ('angular',dH_ang,-dd*unit_j,-dd*unit_j)
]:
    derivative = qmul(qmul(dH,unit_i),qbar(H))+qmul(qmul(H,unit_i),qbar(dH))
    inverse_derivative = qmul(qmul(qbar(dH),unit_i),H)+qmul(qmul(qbar(H),unit_i),dH)
    check(f'axis_regular_derivative_{name}', derivative == expect)
    check(f'inverse_axis_regular_derivative_{name}', inverse_derivative == expect_inverse)

ell = S.symbols('ell', integer=True)
check('normal_first_exponent', -3+(ell+3) == ell)
check('normal_second_exponent', -3-(ell+3) == -6-ell)
aa,bb,cc,ss = S.symbols('aa bb cc ss')
axis = S.Matrix([0,aa,0,-bb])
Hplus = S.Matrix([bb**2+aa**2*cc,aa**2*ss,aa*bb*(1-cc),-aa*bb*ss])
Hminus = Hplus.subs(ss,-ss)
relative_identity = qmul(qmul(axis,qbar(Hplus)),qbar(axis))-Hminus
unit_relation = S.groebner([aa**2+bb**2-1],aa,bb,cc,ss)
check('explicit_initial_product_right_homotopy', all(unit_relation.reduce(S.expand(x))[1] == 0 for x in relative_identity))
z = S.symbols('z', real=True)
integer_angle = S.symbols('integer_angle', integer=True)
check('all_integer_angle_integrals', zero(S.integrate(S.sin(z)**2,(z,0,S.pi*integer_angle))-S.pi*integer_angle/2))

bound = 8
data = []
for p,r,q,s in product(range(-bound,bound+1), repeat=4):
    det = p*s-q*r
    if abs(det) != 1:
        continue
    bp = [[-6*s*p//det,-6*s*r//det],[6*q*p//det,6*q*r//det]]
    assert bp[0][0]+bp[1][1] == -6
    ls = [bp[1][1]-bp[1][0],bp[0][0]-bp[0][1],bp[1][1]]
    xi,upsilon = -r//det,p//det
    ws = [xi,upsilon,-xi-upsilon]
    ds = [-xi-2*upsilon,-2*xi-upsilon,xi-upsilon]
    Is = [-3*wi+di*(li+3) for wi,di,li in zip(ws,ds,ls)]
    Ws = [-3*wi-di*(li+3) for wi,di,li in zip(ws,ds,ls)]
    assert gcd(xi,upsilon) == 1
    assert all((di-wi)%2 == 0 for wi,di in zip(ws,ds))
    assert all(ii+ww == -6*wi for ii,ww,wi in zip(Is,Ws,ws))
    assert all(ii-ww == 2*di*(li+3) for ii,ww,di,li in zip(Is,Ws,ds,ls))
    assert all((-1)**abs(wi) * (-1)**abs(wi) == 1 for wi in ws)
    data.append({'P':[[p,r],[q,s]],'det':det,'period_windings':bp,
                 'normal_first_windings':ls,'tangent_weights':ws,
                 'normal_weight_differences':ds,'orbit_degrees':Is,
                 'derivative_degrees':Ws})

initial = next(row for row in data if row['P'] == [[1,0],[0,1]])
check('initial_orbit_degrees', initial['orbit_degrees'] == [-6,0,0])
check('initial_derivative_degrees', initial['derivative_degrees'] == [6,-6,6])
V = S.Matrix([[0,6,-6],[6,0,0],[-6,0,0]])
delta = S.Matrix([-12,-12,0])
ws,Is,Ws = (initial[k] for k in ['tangent_weights','orbit_degrees','derivative_degrees'])
for j in (1,2):
    e0,ej = S.eye(3)[:,0],S.eye(3)[:,j]
    check(f'initial_integral_variation_relation_{j}', V*(ws[j]*ej-ws[0]*e0) == Is[j]*ej-Is[0]*e0)
    check(f'initial_integral_derivative_relation_{j}', ws[j]*delta[j]-ws[0]*delta[0] == Ws[j]-Ws[0])

record = {'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
          'proof':'notes/part3_source_cusp_general_fan_product_working.md',
          'symbolic_and_initial_checks':len(checks),'checks':checks,
          'integer_basis_entry_bound':bound,'integer_bases_checked':len(data),
          'rows':data,
          'scope':'Full actual unit/character arrows and local trace formulas; bounded enumeration is supplemental to the written general proof. No new global return or transverse variation/derivative entry is assigned.'}
dest = ROOT/'code/part3_root/source_cusp_general_fan_product.json'
dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k != 'rows'},indent=2))
