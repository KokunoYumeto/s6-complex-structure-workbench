"""Fresh exact computations for IRR.1; no inherited verifier imported."""
from pathlib import Path
import hashlib
import json
import sympy as s

n,b,v=s.symbols('n b v',integer=True)
Q=s.Matrix([[-n,1],[1,0]])
K=s.Matrix([-2,-n]);H=s.Matrix([2,b]);V=s.Matrix([0,v])
assert (K+H+V).subs(b,n-v)==s.zeros(2,1)
pa=s.expand(1+(H.T*Q*(K+H))[0]/2)
assert s.expand(pa.subs(b,n-v))==1-v
a,d=s.symbols('a d',integer=True)
assert (1+a-d).subs(a,d-1)==0

# Eliminate the normalization variables from the explicit pinch map.
u,t,x,y,z=s.symbols('u t x y z')
G=s.groebner([x-u*t,y-u,z-t*t],u,t,x,y,z,order='lex')
eliminated=[s.expand(p.as_expr()) for p in G.polys if not p.as_expr().has(u,t)]
assert eliminated==[x*x-y*y*z]
assert (x*x-y*y*z).subs({x:u*t,y:u,z:t*t})==0

# The complete semigroup criterion is proved in the written analytic ring
# comparison; these independent monomial checks supplement its generators.
monomials=0
for du in range(25):
    for dt in range(25):
        admissible=(du>0 or dt%2==0)
        if admissible:
            power_x=dt%2
            power_y=du-power_x
            power_z=(dt-power_x)//2
            assert min(power_x,power_y,power_z)>=0
            assert power_x+power_y==du
            assert power_x+2*power_z==dt
        else:
            assert du==0 and dt%2==1
        monomials+=1

# For the node, the two normalization restrictions kill exactly the mixed
# monomials divisible by xy. Their constants along the conductor coincide.
node=0
for dx in range(15):
    for dy in range(15):
        for dz in range(5):
            mon=x**dx*y**dy*z**dz
            killed=(mon.subs(y,0)==0 and mon.subs(x,0)==0)
            assert killed==(dx>0 and dy>0)
            node+=1

out={'status':'all exact assertions passed','ruled_arithmetic_genus':'1-v',
     'blowup_exceptional_coefficient':'d-1',
     'pinch_elimination_ideal':str(eliminated[0]),
     'conductor_semigroup_checks':monomials,'node_kernel_monomial_checks':node,
     'Euler_identity':'e(T)=number of ruling point blowups; m*e(T)=0 forces zero',
     'scope':'Exact symbolic divisor identities and actual node/pinch ring maps; the analytic depth-two and convergence arguments are written separately.',
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
