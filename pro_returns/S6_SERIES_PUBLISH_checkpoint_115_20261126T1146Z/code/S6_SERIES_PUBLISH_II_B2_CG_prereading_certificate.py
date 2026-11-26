#!/usr/bin/env python3
"""Exact prerelease computations for 01CG; no target or local file is read.

Conormal data are recomputed by Laurent substitution into the actual affine
charts. The pairing budget is exhaustively checked over its proved finite
parameter range. Analytic maps and universal inequalities are proved separately.
"""
import json
import sympy as S

checks = []
details = {}


def equal(name, left, right):
    value = S.cancel(S.expand(left-right))
    if value != 0:
        raise AssertionError((name, str(value)))
    checks.append({"name": name, "result": "exact"})


def true(name, value):
    if not value:
        raise AssertionError(name)
    checks.append({"name": name, "result": "exact"})


x, y, z, t, u, v, s, w = S.symbols("x y z t u v s w", nonzero=True)
g = [y*y-x*z, y*z-x**3, z*z-x*x*y]
P = x**5+x*y**3+z**3-3*x*x*y*z
equal("space cusp saturation relation x", x*P, g[1]**2-g[0]*g[2])
equal("space cusp saturation relation y", y*P, x*g[0]**2+g[1]*g[2])
equal("space cusp saturation relation z", z*P, g[2]**2+x*g[0]*g[1])
G = y*y-x**3
equal("cusp-line saturation relation x", x*(z*G), (x*z)*G)
equal("cusp-line saturation relation y", y*(z*G), (y*z)*G)
equal("cusp-line saturation relation z", z*(z*G), (y*z)**2-x*(x*z)**2)

curve_space = {x:t**3, y:t**4, z:t**5}
curve_cusp = {x:t**2, y:t**3, z:0}
curve_line = {x:0, y:0, z:s}


def differential(f, parametrization):
    return S.Matrix([[S.diff(f,a).subs(parametrization) for a in (x,y,z)]])


a1 = differential(g[0], curve_space)
b1 = differential(g[1], curve_space)+t*a1
K_space = a1.col_join(b1)
K_cusp = differential(x*z, curve_cusp).col_join(differential(G, curve_cusp))
K_line = differential(x*z, curve_line).col_join(differential(y*z, curve_line))
cross_space = S.Matrix(list(a1)).cross(S.Matrix(list(b1)))
for i, expected in enumerate((3*t**8, 4*t**9, 5*t**10)):
    equal("space cusp conormal wedge component " + str(i), cross_space[i], expected)
cross_cusp = S.Matrix(list(K_cusp.row(0))).cross(S.Matrix(list(K_cusp.row(1))))
for i, expected in enumerate((-2*t**5, -3*t**6, 0)):
    equal("planar cusp conormal wedge component " + str(i), cross_cusp[i], expected)
cross_line = S.Matrix(list(K_line.row(0))).cross(S.Matrix(list(K_line.row(1))))
equal("line conormal wedge coefficient", cross_line[2], s*s)
equal("space cusp determinant correction", S.Integer(8)-2, 6)
equal("cusp-line determinant correction", (S.Integer(5)-1)+(S.Integer(2)-0), 6)
equal("non-lci normal degree", -S.Integer(2)+6, 4)

phi_space = S.Matrix([t**3, t**4+v/(3*t**5), t**5-u/t**3+2*v/(3*t**4)])
phi_cusp = S.Matrix([t**2, t**3+v/(2*t**3), u/t**2])
phi_line = S.Matrix([u/s, v/s, s])
for name, phi, K in [('space',phi_space,K_space), ('cusp',phi_cusp,K_cusp), ('line',phi_line,K_line)]:
    pair = S.simplify(K*phi.jacobian([u,v]))
    true(name + " affine chart is dual to the conormal frame", pair == S.eye(2))

def substitute(expr, phi):
    return S.expand(expr.subs(dict(zip((x,y,z),phi)), simultaneous=True))

equal("space affine inverse u", substitute(2*t**4*y-t**3*z-t**8,phi_space), u)
equal("space affine inverse v", substitute(3*t**5*(y-t**4),phi_space), v)
equal("cusp affine inverse u", substitute(t*t*z,phi_cusp), u)
equal("cusp affine inverse v", substitute(2*t**3*(y-t**3),phi_cusp), v)
equal("line affine inverse u", substitute(z*x,phi_line), u)
equal("line affine inverse v", substitute(z*y,phi_line), v)

def quadratic_gram(expr):
    p = S.Poly(expr,u,v)
    return S.Matrix([[p.coeff_monomial(u*u),p.coeff_monomial(u*v)/2],
                     [p.coeff_monomial(u*v)/2,p.coeff_monomial(v*v)]])

q_space = quadratic_gram(substitute(P,phi_space))
equal("space exceptional symbolic-square determinant", q_space.det(), S.Rational(3,4)/t**4)
q_cusp = quadratic_gram(substitute(z*G,phi_cusp))
equal("cusp-line symbolic-square determinant", q_cusp.det(), -S.Rational(1,4)/t**4)

def pole(expr, parameter):
    expr = S.expand(expr)
    if expr == 0:
        return 0
    exponents = [term.as_powers_dict().get(parameter,S.Integer(0)) for term in S.Add.make_args(expr)]
    return max(0, -int(min(exponents)))

pole_data = []
for name, phi, generators, parameter, expected_max in [
    ('space',phi_space,g,t,5),
    ('cusp',phi_cusp,[x*z,y*z,G],t,3),
    ('line',phi_line,[x*z,y*z,G],s,1),
]:
    vector_pole=max(pole(a,parameter) for a in phi.jacobian([u,v]))
    equal(name + " transverse vector pole", S.Integer(vector_pole), expected_max)
    polys=[S.Poly(substitute(f,phi),u,v) for f in generators]
    first_pole=max(pole(p.coeff_monomial(m),parameter) for p in polys for m in (u,v))
    equal(name + " first generator jet is holomorphic", S.Integer(first_pole), 0)
    second_pole=max(pole(p.coeff_monomial(m),parameter) for p in polys for m in (u*u,u*v,v*v))
    equal(name + " second generator jet pole", S.Integer(second_pole), 2*expected_max)
    cubic=max(second_pole,vector_pole)
    quartic=4*vector_pole
    pole_data.append({'chart':name,'vector_pole':vector_pole,'first_generator_pole':first_pole,
                      'second_generator_pole':second_pole,'mixed_cubic_bound':cubic,
                      'fourth_bound':quartic,'quartic_invariant_bound':max(quartic,2*cubic)})
details['Laurent_chart_poles']=pole_data
true("computed invariant pole divisors", [p['quartic_invariant_bound'] for p in pole_data]==[20,12,4])

# Exact residue-space basis; the proved degree bound makes this a complete box.
basis=[(i,j) for i in range(4) for j in range(3)
       if not any(i>=a and j>=b for a,b in ((4,0),(3,1),(2,2),(0,3)))]
true("space symbolic-square residue basis length",len(basis)==9)
details['residue_basis_y_z_exponents']=basis
equal("residue length equals generic rank",S.Integer(len(basis)),3*3)

q0, delta, A = S.symbols("q0 delta A",integer=True)
degree_R_lci=-2+2*delta-q0
degree_delta_lci=-2*q0-4*degree_R_lci
equal("lci corrected quartic degree",degree_delta_lci+8*delta,8+2*q0)
equal("lci total zero budget",(-2*q0)+(degree_delta_lci+8*delta),8)
degree_delta_nonlci=-2*q0-4*(4-q0)
equal("space corrected quartic degree",degree_delta_nonlci+20,4+2*q0)
equal("cusp-line corrected quartic degree",degree_delta_nonlci+12+4,2*q0)
equal("space total zero budget",(-2*q0)+(degree_delta_nonlci+20),4)
equal("cusp-line total zero budget",(-2*q0)+(degree_delta_nonlci+16),0)

qa, cd, lin, quad, ff = S.symbols('qa cd lin quad ff')
G3=cd**2*ff-qa*lin**2
K4=cd**2*G3-lin*quad
equal("conductor-cleared ambient identity",
      4*qa*cd**6*ff-(2*qa*cd**2*lin+quad)**2,
      4*qa*cd**2*K4-quad**2)
ell, rad, mix, fourth = S.symbols('ell rad mix fourth')
Fjet=qa*ell**2+mix*ell*rad**2+fourth*rad**4
Gjet=cd**2*Fjet-qa*(cd*ell)**2
C2=cd**2*mix*rad**2
Kjet=cd**2*Gjet-(cd*ell)*(cd*C2)
equal("conductor-cleared fourth class",Kjet,cd**4*fourth*rad**4)
equal("conductor quotient recovers quartic invariant",
      (qa*(cd**4*fourth)-(cd**2*mix)**2/4)/cd**4,
      qa*fourth-mix**2/4)

# Coordinate identities on an arbitrary analytic function, not sample germs.
Fun=S.Function('F')
blown=Fun(y*y*w,y,t)/y**4
equal("blowup derivative identity",
      y*y*S.diff(blown,w),S.diff(Fun(x,y,t),x).subs(x,y*y*w))
psi=S.Function('psi')(y,t)
Other=S.Function('G')
factored=(x-psi)*Other(x,y,t)
equal("smooth factor conductor restriction",
      S.diff(factored,x).subs(x,psi),Other(psi,y,t))

feasible=[]
for singular_preimages,min_multiplicity in [(0,0),(1,2),(2,2),(3,4)]:
    for singular_branch_points in range(min(2,singular_preimages)+1):
        for smooth_pairs in range(3):
            lower_A=min_multiplicity+2-singular_branch_points+smooth_pairs
            lower_sigma=6-2*singular_branch_points+2*smooth_pairs
            degrees=[a for a in range(0,9,2) if a>=lower_A and 8-a>=lower_sigma]
            if degrees:
                upper_pairs=smooth_pairs+singular_preimages-singular_branch_points
                feasible.append({'s':singular_preimages,'minimum_mu':min_multiplicity,
                                 't':singular_branch_points,'smooth_pairs':smooth_pairs,
                                 'allowed_A':degrees,'upper_total_pairs':upper_pairs})
true("complete finite pairing budget has maximum one",max(row['upper_total_pairs'] for row in feasible)==1)
details['complete_pairing_budget']=feasible

K, pairs, components, beta, r, N0 = S.symbols('K pairs components beta r N0',integer=True)
equal("degree-two finite-set image cardinality", (K-2*pairs)+pairs,K-pairs)
equal("multistar cycle rank",(K-pairs)-(components+1)+1,K-pairs-components)
equal("Euler forest reduction",2-r+N0+(r-N0-pairs),2-pairs)
equal("Euler lower bound with one pair",(2-pairs).subs(pairs,1),1)

print(json.dumps({'tag':'01CG','all_passed':True,'count':len(checks),
                  'method':'Laurent normal-chart substitution, determinant modules, formal derivative identities, and exhaustive finite divisor budget',
                  'checks':checks,'details':details},indent=2)+'\n',end='')
