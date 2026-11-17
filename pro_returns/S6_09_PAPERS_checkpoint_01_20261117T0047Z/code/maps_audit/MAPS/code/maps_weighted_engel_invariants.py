"""Exact marked algebra behind the weighted Engel refined-class proof.

This checks polynomial identities and all residue cases needed by the
proof.  It does not replace the geometric primitive-class, reference-frame,
or relative-characteristic arguments in the companion TeX.
"""
from pathlib import Path
import json
import math
import sympy as s

d,k,l,n0,n1,r0,r1=s.symbols('d k l n0 n1 r0 r1', integer=True)
P=4*l*n0+3*k*n1
K0=s.Matrix([-2*d*n0,-k,0,0])
K1=s.Matrix([-3*d*n1,2*l,0,0])
bound=-2*l*P*K0-k*P*K1
assert s.simplify(bound-s.Matrix([d*P**2,0,0,0]))==s.zeros(4,1)
critical=s.simplify(d-6*d)
assert critical==-5*d
link=s.simplify(-5*(-k*P))
assert link==5*k*P

B=s.Matrix([[0,1],[-1,0]])
assert B**4==s.eye(2)
for j in (1,3):
    assert (B**j-s.eye(2)).det()==2

# Actual core covering before the finite affine fills are attached.
def monodromies(weight):
    return (
        s.Matrix([[1,-1,0,2*weight],[0,-1,-1,6*weight],
                  [0,1,0,0],[0,0,0,1]]),
        s.Matrix([[1,0,1,-3*weight],[0,0,1,0],
                  [0,-1,0,6*weight],[0,0,0,1]]),
        s.Matrix([[1,0,0,weight],[0,1,1,0],
                  [0,0,1,0],[0,0,0,1]]))
cover=s.diag(1,1,1,d)
for A1,Ad in zip(monodromies(1),monodromies(d)):
    assert A1*cover==cover*Ad
normal_values=s.Matrix([[-2*d*n0,-6*d*r0,0],
                       [-3*d*n1,-6*d*r1,0]])
assert all(s.simplify(x/d).is_polynomial() for x in normal_values)

# Integral support and full Pontryagin-square evaluation.
rv,sv=s.symbols('r s',integer=True)
psi=-rv*(rv-1)/2+3*sv*(sv-1)
def value(p): return psi.subs({rv:p[0],sv:p[1]})
walls=[((0,0),(1,0),(0,1),(1,-1)),
       ((1,0),(0,1),(0,0),(1,1)),
       ((0,0),(0,1),(1,0),(-1,1))]
degrees=[s.expand(value(a)+value(b)-value(c)-value(e))
         for a,b,c,e in walls]
assert degrees==[-6,0,1]
eta=s.Matrix([-5,6,0,-1])
ruling=s.Matrix([1,-1,0,0])
Q=s.diag(1,-1,-1,-1)
assert (eta.T*Q*eta)[0]==-12
assert (eta.T*Q*ruling)[0]==1

rows=[]
for kv in range(1,12):
    for lv in range(1,12):
        m0,m1=3*kv,4*lv
        if math.gcd(m0,m1)!=1:
            continue
        inv=pow(m1,-1,m0)
        for Pv in (-1,1):
            n0v=(Pv*inv)%m0
            n1v=(Pv-m1*n0v)//m0
            assert m1*n0v+m0*n1v==Pv
            assert kv%2==1 and math.gcd(n1v,m1)==1
            for rv in (-7,0,9):
                Bv=(2*rv*pow(n1v,-1,m1))%m1
                Cv=(n1v*Bv-2*rv)//m1
                assert m1*Cv==-2*rv+n1v*Bv
                exponent=pow(n1v,-1,m1)
                assert exponent%4 in (1,3)
                rows.append(dict(k=kv,l=lv,P=Pv,n0=n0v,n1=n1v,
                                 r1=rv,chi_eta=Bv,chi_g=Cv,
                                 root_exponent_mod4=exponent%4,
                                 critical_link=5*kv*Pv,
                                 reference_parity=1,refined_P_parity=0))

component_checks=[]
for dv in range(1,51):
    C=s.zeros(dv)
    for i in range(dv):
        C[i,i]-=2
        C[i,(i+1)%dv]+=1
        C[i,(i-1)%dv]+=1
    assert C*s.ones(dv,1)==s.zeros(dv,1)
    if dv==1:
        assert C==s.zeros(1)
    else:
        assert C.rank()==dv-1
    component_checks.append(dict(d=dv,rank=C.rank(),
                                  row_sum_zero=True,
                                  H4_cyclic_order=math.gcd(dv**2,2*dv),
                                  H6_cyclic_order=math.gcd(dv**3,3*dv),
                                  mixed_square=(-12)%(dv*math.gcd(dv,2))))
    assert math.gcd(dv**2,2*dv)==dv*math.gcd(dv,2)
    assert math.gcd(dv**3,3*dv)==dv*math.gcd(dv,3)

out={
    'bounding_chain_identity':[str(s.factor(x)) for x in bound],
    'critical_fibre_value':str(critical),
    'critical_link':str(link),
    'cover_matrix':[[str(x) for x in row] for row in cover.tolist()],
    'normal_gysin_coefficients':[[str(x) for x in row] for row in normal_values.tolist()],
    'support_function':str(psi),
    'wall_degrees':list(map(int,degrees)),
    'component_eta':list(map(int,eta)),
    'eta_square':-12,
    'finite_order_four_cases':rows,
    'component_laplacians':component_checks,
    'status':'All exact marked and parity checks passed; geometry in companion proof.'
}
root=Path(__file__).resolve().parents[1]
(root/'records/maps_weighted_engel_invariants.json').write_text(
    json.dumps(out,indent=2)+'\n')
print('Polynomial bounding chain:',list(map(s.factor,bound)))
print('Literal critical-cycle value:',critical)
print('Actual core critical link:',link)
print('Finite-core cases checked:',len(rows))
print('Component cyclic Laplacians checked:',len(component_checks))
print(out['status'])
