"""Exact local and topological checks used in Parts A and B."""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

out={}
rays=s.Matrix.hstack(*[s.Matrix(v) for v in [
 (0,0,1,0),(1,0,1,0),(0,1,1,0),(1,1,1,0),(0,0,0,1),(0,1,0,1)]])
chars={'x':s.Matrix([0,1,0,0]),'y':s.Matrix([0,-1,1,1]),
       'z':s.Matrix([1,0,0,0]),'v':s.Matrix([-1,0,1,0]),
       'u':s.Matrix([0,0,0,1]),'q':s.Matrix([0,0,1,0])}
out['character_ray_pairings']={n:list(map(int,(v.T*rays))) for n,v in chars.items()}
assert chars['x']+chars['y']==chars['u']+chars['z']+chars['v']
assert chars['z']+chars['v']==chars['q']
out['monoid_relations']=['x*y=u*z*v','q=z*v']
x,y,z,v,u,a,b,d=s.symbols('x y z v u a b d')
out['hypersurface_gradient']=[str(s.diff(x*y-u*z*v,t)) for t in (x,y,z,v,u)]
out['resolution_charts']=[
 {'coordinates':['u','z','a','y'],'map':{'x':'u*z*a','v':'a*y'},'q':'z*a*y'},
 {'coordinates':['u','a','d','v'],'map':{'x':'u*a','z':'a*d','y':'d*v'},'q':'a*d*v'},
 {'coordinates':['x','b','z','v'],'map':{'u':'x*b','y':'b*z*v'},'q':'z*v'}]
for chart in out['resolution_charts']:
    expr=s.sympify('x*y-u*z*v').subs({s.Symbol(k):s.sympify(val) for k,val in chart['map'].items()},simultaneous=True)
    assert s.expand(expr)==0
out['point_blowup_central_equations']=['u=u (u-chart)','u=z_i*b (z_i-chart, i=1,2,3)']
tt=s.symbols('t')
AA=-3*tt**3*(tt-1); BB=2*tt**4*(tt-1)**2
px=0; py=-s.sqrt(2)*tt**2*(tt-1)
slope=s.cancel(AA/(2*py))
xx=s.cancel(slope**2); yy=s.cancel(-py-slope*xx)
assert s.simplify(yy**2-xx**3-AA*xx-BB)==0
assert xx==s.Rational(9,8)*tt**2
assert s.simplify(yy-s.sqrt(2)*tt**2*(5*tt-32)/32)==0
out['doubling_2P']={'x':str(xx),'y':str(yy),'curve_equation_residual':0}
out['exceptional_cohomology_generization']= [[1,0],[1,1]]
out['generization_determinant']=int(s.Matrix(out['exceptional_cohomology_generization']).det())
d2=s.Matrix([[-1,0,0],[-3,1,0],[-1,0,1]])
d2prime=d2.col_join(s.Matrix([[1,0,0]]))
out['d2_core']=d2.tolist()
out['d2prime_core']=d2prime.tolist()
out['smith_d2']=smith_normal_form(d2,domain=ZZ).tolist()
out['smith_d2prime']=smith_normal_form(d2prime,domain=ZZ).tolist()
out['betti_R']=[1,0,11,0,11,0,1]
out['betti_Rprime']=[1,0,12,0,12,0,1]
out['betti_Q']=[1,1,8,7,10,0,1]
out['betti_Qprime']=[1,1,9,7,11,0,1]
out['euler']={name:sum((-1)**i*b for i,b in enumerate(out[name]))
              for name in ['betti_R','betti_Rprime','betti_Q','betti_Qprime']}
out['deck_shifts']={}
for m,shift in [(3,4),(4,-3)]:
    perms=[[int((j+a*shift)%12) for j in range(12)] for a in range(1,m)]
    assert all(all(row[j]!=j for j in range(12)) for row in perms)
    out['deck_shifts'][str(m)]=perms

# Virtual Chern class: degree bookkeeping uses F^2=F*m=0, m^2=-2[pt].
H,m,F,c2,t=s.symbols('H m F c2 t')
d0=H+m; dinf=H; D=d0+dinf
cTR=(1+F*t+c2*t**2)*(1+D*t)
ratio=((1+(F-d0)*t)*(1+(F-dinf)*t)/(1+F*t)**2)
c3=s.expand(s.series(cTR*ratio,t,0,4).removeO()).coeff(t,3)
# Projective-bundle relation H^2=-mH. Reduce before fibre integration.
reduced=s.rem(s.Poly(c3,H),s.Poly(H**2+m*H,H)).as_expr()
push=s.expand(reduced).coeff(H,1)
push=s.expand(push).subs(F**2,0).subs(F*m,0)
out['virtual_c3_polynomial']=str(c3)
out['virtual_c3_pushforward']=str(s.expand(push))
assert s.expand(push)==0
print(json.dumps(out,indent=2,default=str))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
