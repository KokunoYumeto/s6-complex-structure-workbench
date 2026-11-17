"""Exact normal-coordinate and quartic-pole checks in the non-lci part of A.5.18."""
import itertools
import sympy as sp

x,y,z,t,s,u,v=sp.symbols('x y z t s u v')
g=[y**2-x*z,y*z-x**3,z**2-x**2*y]
F=x**5+x*y**3+z**3-3*x**2*y*z
assert sp.expand(x*F-g[1]**2+g[0]*g[2])==0
assert sp.expand(y*F-x*g[0]**2-g[1]*g[2])==0
assert sp.expand(z*F-g[2]**2-x*g[0]*g[1])==0
print('(3,4,5): the three exact maximal-ideal annihilation identities hold.')

param={x:t**3,y:t**4,z:t**5}
dg=[sp.Matrix([sp.diff(h,w).subs(param) for w in (x,y,z)]) for h in g]
a=dg[0]; b=dg[1]+t*dg[0]
assert sp.simplify(dg[2]+2*t**2*a-t*b)==sp.zeros(3,1)
assert a.cross(b)==sp.Matrix([3*t**8,4*t**9,5*t**10])
print('(3,4,5): conormal wedge=t^8(3,4t,5t²), tangent common order2; defect6.')

maps={
    'space_cusp':({x:t**3,y:t**4+v/(3*t**5),z:t**5-u/t**3+2*v/(3*t**4)},t,g,10,20),
    'cusp_branch':({x:t**2,y:t**3+v/(2*t**3),z:u/t**2},t,[x*z,y*z,y**2-x**3],6,12),
    'line_branch':({x:u/s,y:v/s,z:s},s,[x*z,y*z,y**2-x**3],2,4),
}

def pole_order(expr, parameter):
    expr=sp.cancel(expr)
    if expr==0:
        return 0
    numerator,denominator=sp.fraction(expr)
    def val(poly):
        return min(m[0] for m,c in sp.Poly(poly,parameter).terms() if c)
    return max(0,val(denominator)-val(numerator))

for name,(chart,parameter,gens,cubic_bound,quartic_bound) in maps.items():
    pulled=[sp.expand(h.subs(chart,simultaneous=True)) for h in gens]
    print(name,'exact generators:',pulled)
    # First normal derivatives of all generators are holomorphic at the
    # normalization point in the displayed conormal frame.
    for expr in pulled:
        poly=sp.Poly(expr,u,v)
        for monomial,coefficient in poly.terms():
            if sum(monomial)==1:
                assert pole_order(coefficient,parameter)==0
    cubic_actual=quartic_actual=0
    for i,j in itertools.combinations_with_replacement(range(3),2):
        for coefficient in (1,x,y,z,x*x,x*y,x*z,y*y,y*z,z*z):
            expr=sp.expand((coefficient*gens[i]*gens[j]).subs(chart,simultaneous=True))
            for monomial,value in sp.Poly(expr,u,v).terms():
                if sum(monomial)==3:
                    cubic_actual=max(cubic_actual,pole_order(value,parameter))
                if sum(monomial)==4:
                    quartic_actual=max(quartic_actual,pole_order(value,parameter))
    assert cubic_actual<=cubic_bound
    assert quartic_actual<=quartic_bound
    print(name,'cubic/quartic poles:',cubic_actual,quartic_actual,
          'bounds',cubic_bound,quartic_bound)

space_chart=maps['space_cusp'][0]
Fpulled=sp.Poly(sp.expand(F.subs(space_chart,simultaneous=True)),u,v)
qF=sum(coefficient*u**monomial[0]*v**monomial[1]
       for monomial,coefficient in Fpulled.terms() if sum(monomial)==2)
assert sp.expand(qF-(3*u*u/t-3*u*v/t**2+v*v/t**3))==0
qmat=sp.hessian(qF,(u,v))/2
assert sp.factor(qmat.det())==3/(4*t**4)
print('Symbolic generator quadratic:',qF,'determinant',sp.factor(qmat.det()))

G=y*y-x**3
cusp_chart=maps['cusp_branch'][0]
q_extra=sp.Poly(sp.expand((z*G).subs(cusp_chart,simultaneous=True)),u,v)
q_extra=sum(c*u**m[0]*v**m[1] for m,c in q_extra.terms() if sum(m)==2)
assert q_extra==u*v/t**2
assert sp.factor((sp.hessian(q_extra,(u,v))/2).det())==-1/(4*t**4)
print('Cusp-plus-line symbolic generator quadratic:',q_extra)

q=sp.symbols('q',integer=True)
assert sp.expand(-2*q-4*(4-q))==-16+2*q
assert sp.expand((-16+2*q)+20+(-2*q+1))==5
assert sp.expand((-16+2*q)+12+4)==2*q
print('Space-cusp sum of two branch bounds=5; cusp-plus-line cleared degree=2q<=0.')
print('All exact non-lci coordinate, ideal and pole assertions passed.')
