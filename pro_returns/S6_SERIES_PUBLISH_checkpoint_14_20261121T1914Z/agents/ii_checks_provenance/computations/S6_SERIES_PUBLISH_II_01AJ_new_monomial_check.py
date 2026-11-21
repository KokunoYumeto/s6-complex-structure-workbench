"""Fresh exact parity-bound and differential checks for 01AJ; no reused code."""
import json
import sympy as s
u,v,x,y,z=s.symbols('u v x y z')
F=x*x-y**4*z**3
sub={x:u*u*v**3,y:u,z:v*v}
assert s.expand(F.subs(sub))==0
grad=[s.diff(F,t).subs(sub) for t in (x,y,z)]
tau=[2*y*z,-4*x*z,-3*x*y]
assert all(s.simplify(g/(u*v)-a.subs(sub))==0 for g,a in zip(grad,tau))
dx=[s.diff(sub[x],u),s.diff(sub[x],v)]
dy=[1,0];dz=[0,2*v]
pull=[s.expand(sum(a.subs(sub)*d[k] for a,d in zip(tau,(dx,dy,dz)))) for k in (0,1)]
assert pull==[0,0]

# R monomials: even v-power has a,b >=0; odd has a>=2,b>=3.
# For q=u^a v^b, each shifted membership condition supplies two lower bounds.
# Taking their maxima is an exact decision for every integer a,b of each parity.
def bounds(shifts):
    out={}
    for parity in (0,1):
        ab=[]
        for da,db in shifts:
            target=(parity+db)%2
            amin,bmin=((0,0) if target==0 else (2,3))
            ab.append((amin-da,bmin-db))
        lo_a=max(a for a,b in ab);lo_b=max(b for a,b in ab)
        lo_b += (parity-lo_b)%2
        out[str(parity)]=[lo_a,lo_b]
    return out
conductor=bounds([(0,0),(0,1)])
inverse=bounds([(2,3),(3,6),(4,4)])
assert conductor=={'0':[2,2],'1':[2,3]}
assert inverse=={'0':[0,0],'1':[-1,-1]}
print(json.dumps({'normalization_equation':0,'torsion_generator_pulls_back_to':[str(q) for q in pull],
 'conductor_min_exponents_by_v_parity':conductor,
 'inverse_jacobian_min_exponents_by_v_parity':inverse,
 'universal_scope':'The parity calculation takes exact maxima of every generator constraint; it is not a finite-grid test.',
 'all_assertions_passed':True},indent=2))
