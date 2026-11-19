"""Exact finite-coefficient support/localization data for the marked OS45 case.

The support must first be identified with the actual global cyclic class;
that geometric boundary comparison is owned by the maps proof. This
program does not infer it from matching only the regular-fibre form.
Once that comparison is proved, the three localization values below
follow for all equivariant character choices by integer polynomial
identities, with target moduli8,16,8 retained exactly.
"""
from pathlib import Path
from itertools import product
import json
import sympy as S
ROOT=Path(__file__).resolve().parent
RAYS=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
def psi(r,s):return 4*(r//8)+3*(r%8)*(s//2)
def val(v):return psi(*v)
def plus(v,w):return v[0]+w[0],v[1]+w[1]
# Actual quasiperiod differences, verified symbolically by residue reduction.
# Every integer point is (8a+r,2b+s), with residues0<=r<8,0<=s<2.
a,b=S.symbols('a b',integer=True)
period_checks=[]
for r,s in product(range(8),range(2)):
    f=4*a+3*r*b
    fh=4*(a+1)+3*r*(b-3)
    fF=4*(a+3)+3*r*(b-8)
    assert S.expand(fh-f-(-(8*a+r)+4))%8==0
    assert S.expand(fF-f-4)%8==0
    period_checks.append(dict(residue=[r,s],h_difference=str(S.expand(fh-f)),F_difference=str(S.expand(fF-f))))
Q=S.diag(1,-1,-1,-1)
curves=[S.Matrix(v) for v in [(0,1,0,0),(1,-1,-1,0),(0,0,1,0),
                            (1,0,-1,-1),(0,0,0,1),(1,-1,0,-1)]]
f=S.Matrix([1,-1,0,0]);rows=[]
for r,s in product(range(8),range(2)):
    v=(r,s)
    degrees=[val(v)+val(plus(v,RAYS[j]))-val(plus(v,RAYS[(j-1)%6]))-val(plus(v,RAYS[(j+1)%6])) for j in range(6)]
    eta=S.Matrix([degrees[0]+degrees[1]+degrees[2],-degrees[0],-degrees[2],-degrees[4]])
    assert [(eta.T*Q*c)[0] for c in curves]==degrees
    fixed_degree=degrees[1]%8
    lam=psi(r,s+1)-psi(r,s)
    assert lam==(0 if s==0 else 3*r)
    mu=-s
    rows.append(dict(vertex=[r,s],wall_degrees=degrees,
                     eta=list(map(int,eta)),eta_square=int((eta.T*Q*eta)[0]),
                     eta_dot_ruling=int((eta.T*Q*f)[0]),
                     u_xi_y=int((-1)**s*(eta.T*Q*f)[0])%8,
                     P2u_xi=int((eta.T*Q*eta)[0])%16,
                     fixed_u_degree=fixed_degree,lambda_weight=lam,y_weight=mu))
assert sum(r['fixed_u_degree'] for r in rows)==40
assert sum(r['fixed_u_degree']*r['lambda_weight'] for r in rows)==336
assert sum(r['fixed_u_degree']*r['lambda_weight']**2 for r in rows)==5544
L,V=S.symbols('L V',integer=True)
identities=[]
for eps in [-1,1]:
    cube=S.expand(-3*sum(r['fixed_u_degree']*(L+eps*r['lambda_weight'])**2 for r in rows))
    square_y=S.expand(-2*sum(r['fixed_u_degree']*(L+eps*r['lambda_weight'])*(V+r['y_weight']) for r in rows))
    u_y2=S.expand(-sum(r['fixed_u_degree']*(V+r['y_weight'])**2 for r in rows))
    assert all(c%8==0 for c in S.Poly(cube,L,V).coeffs())
    assert all(c%16==0 for c in S.Poly(square_y,L,V).coeffs())
    assert all(c%8==0 for c in S.Poly(u_y2,L,V).coeffs())
    identities.append(dict(sign=eps,u_cube=str(cube),P2u_y=str(square_y),u_y2=str(u_y2)))
    print('SIGN',eps,'u^3:',cube,'; P2(u)y:',square_y,'; uy^2:',u_y2)
out=dict(scope=__doc__,period_checks=period_checks,components=rows,
         fixed_degree_sum=40,fixed_degree_weight_sum=336,
         fixed_degree_squared_weight_sum=5544,
         universal_character_identities=identities,
         conditional_results=dict(u_cube_mod8=0,P2u_y_mod16=0,u_y2_mod8=0),
         status='Algebra PASS; geometric support comparison is a separately proved required input.')
(ROOT/'fourfolds_OS45_localization.json').write_text(json.dumps(out,indent=2)+'\n')
print('All16 support-wall restrictions and six all-character divisibility identities PASS')
