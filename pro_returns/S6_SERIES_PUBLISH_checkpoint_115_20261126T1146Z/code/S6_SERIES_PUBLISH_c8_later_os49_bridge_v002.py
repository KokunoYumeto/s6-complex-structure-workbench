#!/usr/bin/env python3
"""Literal period and circle-map checks for the written geometric bridge."""
import sympy as s

TA=s.Matrix([[1,-3,-3,-1],[0,-2,-3,-1],[0,1,1,0],[0,0,0,1]])
TB=s.Matrix([[1,0,0,0],[0,1,1,0],[0,-1,0,0],[0,0,0,1]])
A,B=TA.inv().T,TB.inv().T
A1=s.Matrix([[1,0,0,0],[0,0,1,0],[-3,-1,-1,0],[-1,0,-1,1]])
A2=s.Matrix([[1,0,0,0],[0,1,-1,0],[0,1,0,0],[0,0,0,1]])
G=s.Matrix([[-1,0,0,0],[0,-1,0,0],[0,-1,1,0],[0,0,0,1]])
assert G*G==s.eye(4) and A1*G==G*A and A2*G==G*B
n,d,m,k=s.symbols('n d m k',integer=True)
ell=s.Matrix([n,-n,0,d])
assert G*ell==s.Matrix([-n,n,n,d])
print('G_INVERSE=G; EXACT_FINITE_CONJUGACIES; VECTOR=',list(G*ell))
tau,mu,beta=s.symbols('tau mu beta')
Pi=s.Matrix([[3*mu,tau,1,0],[beta,mu,0,1]])
PiP=s.Matrix([[-3*mu,-tau-1,1,0],[-beta,-mu,0,1]])
assert PiP*G==Pi
R1=s.Matrix([[-1/tau,0],[-mu/tau,1]])
R2=s.Matrix([[1/(tau+1),0],[-mu/(tau+1),1]])
laws=[((tau-1)/tau,1-mu/tau,beta+1-3*mu**2/tau),
      (-1/(tau+1),mu/(tau+1),beta-3*mu**2/(tau+1))]
for j,(R,D,law) in enumerate(zip((R1,R2),(A1,A2),laws),1):
    expected=Pi.subs(dict(zip((tau,mu,beta),law)),simultaneous=True)
    difference=(R*Pi*D.inv()-expected).applyfunc(s.simplify)
    assert difference==s.zeros(2,4)
    print('YANG_AFFINE_LAWS',j,law,'ALL_EIGHT_ENTRIES_MATCH')
finite=s.factor(1-(tau+1)/(3*tau)-(tau+1)/3)
assert s.simplify(finite+((tau**2-tau+1)/(3*tau)))==0
print('FINITE_FIXED_VALUE_ERROR=',finite,'VANISHES_AT_tau^2-tau+1=0')
print('PARAMETER_MAP (n_Y,r)=(-n_P,d_P); INVERSE_IDENTICAL')
beta_circle=s.Matrix([-n,-3*d,3*k])
def contraction(i,j):
    result=s.zeros(3,1)
    result[j]=beta_circle[i]
    result[i]=-beta_circle[j]
    return result
u2=contraction(0,1)
p=contraction(2,0)
q=contraction(2,1)/3
assert u2==s.Matrix([3*d,-n,0])
assert p==s.Matrix([3*k,0,n])
assert q==s.Matrix([0,k,d])
print('CLOCKWISE_NORMAL_VALUES=',list(beta_circle))
print('EXACT_TRANSFER_u2_p_q=',list(u2),list(p),list(q))
assert (u2+q).subs({n:1,d:0,k:1})==s.zeros(3,1)
assert (-beta_circle[0]).subs({n:1,d:0,k:1})==1
print('REFERENCE_CAP u2+q HORIZONTAL; -psi HAS NORMAL_VALUE_ONE')
assert u2.cross(p)==n*beta_circle
print('TRANSFER_CROSS_PRODUCT=',list(u2.cross(p)))
print('POSITIVE_NORMAL=-CLOCKWISE_NORMAL; THOM_GENERATOR_MAP=-1; LAST_PAIR_ARROW=-n')
print('GEOMETRIC_ROOF_AND_CHART_PROOF_IS_IN_THE_WRITTEN_COMPARISON; NO_SAMPLED_GEOMETRY_CREDIT')
