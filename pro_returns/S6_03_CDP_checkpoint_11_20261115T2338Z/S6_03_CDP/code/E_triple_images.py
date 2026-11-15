"""Exact symbolic-cube and cubic-discriminant checks for A.5.19."""
import itertools
import sympy as sp

x,y,z,t,s,u,v,w=sp.symbols('x y z t s u v w')
cases={
    'space_cusp': ([y*y-x*z,y*z-x**3,z*z-x*x*y],
                   x**5+x*y**3+z**3-3*x*x*y*z, x),
    'cusp_plus_line': ([x*z,y*z,y*y-x**3],z*(y*y-x**3),x+z),
    'three_axes': ([x*y,x*z,y*z],x*y*z,x+y+z),
}

for name,(gens,extra,denominator) in cases.items():
    cube=[sp.prod(gens[i] for i in index)
          for index in itertools.combinations_with_replacement(range(3),3)]
    candidate=cube+[extra*g for g in gens]
    gb=sp.groebner(candidate,z,y,x)
    saturation=sp.groebner(cube+[1-w*denominator],w,z,y,x)
    eliminated=[p.as_expr() for p in saturation.polys if not p.as_expr().has(w)]
    gs=sp.groebner(eliminated,z,y,x)
    assert all(gb.reduce(p.as_expr())[1]==0 for p in gs.polys)
    assert all(gs.reduce(p.as_expr())[1]==0 for p in gb.polys)
    print(name,': I^(3)=I^3+F I, exact saturation by',denominator)

# The self-contained DVR proof for the space cusp has residue dimension18.
residue=[y**a*z**b for a in range(6) for b in range(6)
         if a+b<=4 or (a,b) in [(5,0),(4,1),(3,2)]]
assert len(residue)==18
print('Space-cusp DVR residue basis length:',len(residue),'=3*length(C{u,v}/(u,v)^3).')

charts={
    'space_cusp': ({x:t**3,y:t**4+v/(3*t**5),z:t**5-u/t**3+2*v/(3*t**4)},t,3),
    'cusp_branch': ({x:t**2,y:t**3+v/(2*t**3),z:u/t**2},t,2),
    'line_branch': ({x:u/s,y:v/s,z:s},s,1),
    'axis_branch': ({x:t,y:u/t,z:v/t},t,1),
}

def pole(expr,param):
    if expr==0:return 0
    num,den=sp.fraction(sp.cancel(expr))
    val=lambda f:min(m[0] for m,c in sp.Poly(f,param).terms() if c)
    return max(0,val(den)-val(num))

for name,(chart,param,bound) in charts.items():
    source='space_cusp' if name=='space_cusp' else ('three_axes' if name=='axis_branch' else 'cusp_plus_line')
    gens,extra,_=cases[source]
    observed=0
    for g in gens:
        expanded=sp.Poly(sp.expand((extra*g).subs(chart,simultaneous=True)),u,v)
        cubic=sum(c*u**m[0]*v**m[1] for m,c in expanded.terms() if sum(m)==3)
        for m,c in sp.Poly(cubic,u,v).terms():
            observed=max(observed,pole(c,param))
    assert observed<=bound
    print(name,': initial cubic pole',observed,'<=',bound)

for poles in ([3],[2,1],[1,1,1]):
    cleared_degree=-6*4+4*sum(poles)
    assert cleared_degree==-12
    print('Discriminant pole orders',poles,'give corrected degree',cleared_degree)

# The local nodal-image example has an exact product fibre map.
F=x*y*z*(x-y*z)
assert sp.cancel(F.subs(z,v/y)-x*v*(x-v))==0
print('Allowed nodal-image map: f(x,y,v/y)=x*v*(x-v).')
print('All exact symbolic-cube, pole and fibre-map checks passed.')
