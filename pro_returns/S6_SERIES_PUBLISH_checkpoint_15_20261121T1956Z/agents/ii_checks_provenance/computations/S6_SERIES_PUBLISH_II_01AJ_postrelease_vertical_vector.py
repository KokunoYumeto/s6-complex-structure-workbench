"""Fresh exact check of the additional vector displayed in released 01AJ."""
import sympy as s
import json
x,y,z,u,v=s.symbols('x y z u v')
F=x*x-y**4*z**3;sub={x:u*u*v**3,y:u,z:v*v}
display=[2*y*y*z,-4*x*y*z,-3*x*y*y]
for q,w in zip([s.diff(F,q) for q in (x,y,z)],display):
 assert s.simplify(q.subs(sub)/v-w.subs(sub))==0
pull=[s.expand(sum(w.subs(sub)*s.diff(sub[q],a) for w,q in zip(display,(x,y,z)))) for a in (u,v)]
assert pull==[0,0]
print(json.dumps({'gradient_multiplier':'1/v','pullback':[str(q) for q in pull],
 'all_assertions_passed':True,'timing_scope':'Additional displayed vector checked after target release; original module derivation was already frozen.'},indent=2))
