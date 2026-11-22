"""BY comparison by closed-cover Euler strata and explicit normal algebra.

This is separate from the prerelease open-pair program. The local table is
computed from Groebner standard monomials of the Jacobian ideal. The module
multiplication matrices verify the repeated-branch integral algebra.
"""
import json
from fractions import Fraction
import sympy as s

z,r,T=s.symbols('z r T')
Mw=s.Matrix([[0,0,z*r],[1,0,0],[0,z,0]])
Mv=s.Matrix([[0,z*r,0],[0,0,r],[1,0,0]])
I=s.eye(3)
assert Mw*Mv==Mv*Mw==z*r*I
assert Mw**2==z*Mv and Mv**2==r*Mw
assert Mw.charpoly(T).as_expr()==T**3-z**2*r
assert Mv.charpoly(T).as_expr()==T**3-z*r**2
assert Mw**3==z**2*r*I and Mv**3==z*r**2*I

w,x,y=s.symbols('w x y')
local=[]
for k in (1,2,3):
    f=w**3+x**2-y**(2*k)
    gb=s.groebner([s.diff(f,a) for a in (w,x,y)],w,x,y,order='lex')
    leading=[p.LM(order=gb.order).exponents for p in gb.polys]
    standard=[]
    for a in range(3):
        for b in range(2):
            for d in range(2*k):
                exp=(a,b,d)
                if not any(all(u>=v for u,v in zip(exp,lm)) for lm in leading):
                    standard.append(exp)
    assert standard==[(a,0,d) for a in range(2) for d in range(2*k-1)]
    spectrum=[Fraction(a+1,3)+Fraction(b+1,2)+Fraction(d+1,2*k)-1 for a,b,d in standard]
    pg=sum(-1<a<=0 for a in spectrum)
    link=sum(a.denominator==1 for a in spectrum)
    assert (pg,link)==((0,0) if k<3 else (1,2))
    local.append(dict(plane_type='A'+str(2*k-1),jacobian_basis=[list(v) for v in standard],
                      spectrum=[str(v) for v in spectrum],pg=pg,link_b1=link))

# Independent finite-cover stratification, followed by replacing singular
# points by their complete exceptional sets and subtracting class-span rank.
c,g,nu,n,lam,B1=s.symbols('c g nu n lambda B1')
branch_euler=2*c-2*g-nu
closed_euler=3*(4-branch_euler)+branch_euler
resolved_euler=closed_euler+n-lam
pair=s.expand(resolved_euler-2+2*B1-(n+2))
assert pair==2*B1-4*c+4*g-lam+2*nu+8
one=s.expand(pair.subs({c:2,g:0}))
P=s.symbols('P',integer=True,nonnegative=True)
q=s.symbols('q',integer=True,nonnegative=True)
two=s.expand(pair.subs({c:3,g:0,lam:2*P,B1:2*q}))
double=s.expand(pair.subs({c:2,g:0,lam:0,B1:0}))
assert one==2*B1-lam+2*nu
assert two==2*nu-4-2*P+4*q
assert double==2*nu

# Exact factor permutation relating the frozen and printed bidegree frames.
switch=s.Matrix([[0,1],[1,0]])
intersection=s.Matrix([[0,1],[1,0]])
assert switch.T*intersection*switch==intersection
assert switch*s.Matrix([2,3])==s.Matrix([3,2])
assert switch*s.Matrix([1,3])==s.Matrix([3,1])
assert switch*s.Matrix([1,0])==s.Matrix([0,1])
assert switch*s.Matrix([-1,-2])==s.Matrix([-2,-1])

# The exact graph inequality uses k=K-loss and c0<=nG-1, beta<=1.
K,loss,beta,nG=s.symbols('K loss beta nG',integer=True)
components_bound=nG-1
cycles_lower=K-loss-components_bound
assert s.expand(cycles_lower-beta)==K-loss-nG+1-beta
r0,N0=s.symbols('r0 N0',integer=True)
euler_lower=s.expand(2-r0+N0+(r0-N0-loss))
assert euler_lower==2-loss

print(json.dumps(dict(status='PASS',method='Multiplication matrices and Jacobian Groebner bases, then closed-cover Euler strata',
    repeated_algebra_characteristic_polynomials=[str(Mw.charpoly(T).as_expr()),str(Mv.charpoly(T).as_expr())],
    multiplication_relations_verified=True,local_cubic_suspensions=local,
    closed_pair_rank=str(pair),printed_one_simple_rank=str(one),printed_two_simple_rank=str(two),
    printed_double_rank=str(double),factor_permutation_verified=True,
    exact_incidence_bound=str(euler_lower),
    scope='Every printed numerical step agrees; the geometric maps are proved in the derivation and comparison; this adds no second evidence group'),indent=2))
