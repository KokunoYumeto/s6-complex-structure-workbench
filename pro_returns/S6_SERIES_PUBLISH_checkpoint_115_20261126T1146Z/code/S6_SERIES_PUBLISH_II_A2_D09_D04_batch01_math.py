#!/usr/bin/env python3
"""Exact preservation calculations for the bounded R10/R14/R15 edit.

Written after full proof and historical-code reading. First-jet Taylor
pullbacks, a two-branch cubic parametrization, and explicit quotient-ring
inverses supply the comparisons. This is no independent whole-proof check.
"""
import json
import sympy as s

t,x,y,z,a,c,l,u,v,w=s.symbols('t x y z a c l u v w')
H=y*y-x**3
F=(a*z+c*H)**2+H**4
pull=s.expand(F.subs({x:t*t+l*u,y:t**3+l*v,z:l*w},simultaneous=True))
first_form=-3*c*t**4*u+2*c*t**3*v+a*w
assert s.expand(pull.coeff(l,2)-first_form**2)==0
ell=s.Matrix([-3*c*t**4,2*c*t**3,a])
cusp_hessian=2*ell*ell.T
F1=z*x*x+x*y*y
f1pull=s.expand(F1.subs({x:l*u,y:l*v,z:z+l*w},simultaneous=True))
assert f1pull.coeff(l,2)==z*u*u

# The inequalities in the retained proof hold for every permissible
# integer, by the two exact decompositions below, rather than a sample.
A,B,D,M,C=s.symbols('A B D M C',integer=True,nonnegative=True)
assert s.expand((D+2*B-2*M)-((D-A)+(A+B-2*M)+B))==0
# Planar: C<=A gives b=C; C>=A gives b=A and D+2b-2A=D.
assert s.expand(D+2*A-2*A)==D

# The printed polar example is reduced to two values of alpha=x/z.
P=z*(x-z)*(x-2*z)
Pz=s.diff(P,z);Px=s.diff(P,x);G=2*P+x*Px
J=s.Matrix([G-2,Pz]).jacobian([x,z]).det()
q=25*z**6+50*z**3-2
xbar=(5*z**4+14*z)/3
assert s.rem(Pz.subs(x,xbar),q,z)==0
assert s.rem((G-2).subs(x,xbar),q,z)==0
assert s.gcd(q,s.diff(q,z))==1
unit_inverses={}
for name,poly in [('x',x),('H_x',Px),('J',J)]:
    val=s.rem(poly.subs(x,xbar),q,z)
    inv=s.invert(val,q,z)
    assert s.rem(val*inv,q,z)==1
    unit_inverses[name]=str(inv)
branches=[]
for sign in [-1,1]:
    alpha=3+sign*s.sqrt(3)
    coefficient=s.simplify(4*alpha**2-9*alpha+4)
    assert coefficient==25+sign*15*s.sqrt(3)
    assert s.simplify(alpha**2-6*alpha+6)==0
    assert coefficient!=0 and alpha!=0 and 2*alpha-3!=0
    jac=s.simplify((J.subs(x,alpha*z)/z**3)*(2/coefficient))
    assert s.simplify(jac+sign*12*s.sqrt(3))==0
    branches.append({'alpha':str(alpha),'x':'alpha*z',
                     'z_cubed':str(s.simplify(2/coefficient)),
                     'Jacobian':str(jac),'simple_roots':3})
assert sum(r['simple_roots'] for r in branches)==6
rho=s.symbols('rho')
assert s.expand(Pz.subs({x:rho*x,z:rho*z},simultaneous=True)-rho**2*Pz)==0
assert s.expand(G.subs({x:rho*x,z:rho*z},simultaneous=True)-rho**3*G)==0

# The degree-two Taylor term of h^m at dh=0 is
# m*v0^(m-1) times the degree-two term of h. The higher
# terms in the binomial expansion have order at least four.
m=s.symbols('m',integer=True,positive=True)
v0,qa,qb,qc,epsilon=s.symbols('v0 qa qb qc epsilon',nonzero=True)
Q=s.Matrix([[qa,qb],[qb,qc]])
quadratic=u*u+m*v0**(m-1)*(qa*v*v+2*qb*v*w+qc*w*w)/2
matrix=s.hessian(quadratic,(u,v,w))
expected=s.diag(2,m*v0**(m-1),m*v0**(m-1))
expected[1:3,1:3]=m*v0**(m-1)*Q
assert matrix==expected
assert s.simplify(matrix.det()-2*m*m*v0**(2*m-2)*(qa*qc-qb*qb))==0
moving=s.simplify(matrix.subs({v0:-epsilon,qa:0,qb:1,qc:0}))
assert s.simplify(moving.det()+2*m*m*epsilon**(2*m-2))==0

out={'scope':'Post-reading exact preservation checks; no canonical events.',
 'R10_cusp_equation':'(a*z+c*(y^2-x^3))^2+(y^2-x^3)^4',
 'R10_first_jet_vector':[str(k) for k in ell],
 'R10_rank_one_condition':'a!=0, so the last entry of ell is nonzero',
 'R10_hessian':[[str(k) for k in row] for row in cusp_hessian.tolist()],
 'R10_simple_zero_hessian':'diag(2*z,0,0)',
 'unbounded_lattice_inequalities':{
   'nonplanar':'D+2B-2M=(D-A)+(A+B-2M)+B >=0',
   'planar_C_le_A':'b=C and the premise D+2C>=2A gives D+2b>=2A',
   'planar_C_ge_A':'b=A and D+2b-2A=D>=0'},
 'R14_printed_basis':['3*x-5*z^4-14*z',str(q)],
 'R14_exact_branches':branches,
 'R14_quotient_inverses':unit_inverses,
 'R14_scaling':'(x,z)->rho*(x,z), epsilon=rho^3',
 'R15_Taylor_hessian':[[str(k) for k in row] for row in matrix.tolist()],
 'R15_general_determinant':'2*m^2*v0^(2*m-2)*det(Q)',
 'R15_moving_node_value':'(-epsilon)^m',
 'R15_moving_node_determinant':'-2*m^2*epsilon^(2*m-2)',
 'all_assertions_passed':True,
 'not_checked_here':['Analytic boundary transport','Conductor-sheaf and curve-group theorems','Any independent whole-statement derivation']}
print(json.dumps(out,indent=2))
