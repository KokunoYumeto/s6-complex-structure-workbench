#!/usr/bin/env python3
"""Fresh E13 algebra certificate, written before release of the E13 proof.

This checks the displayed maps in the companion derivation, not the
unopened E_checks.py implementation.  Geometric extension and Cech
arguments are supplied separately in the derivation.
"""
import hashlib
import json
from pathlib import Path
import sympy as s

def mat(M):
    return [[str(x) for x in row] for row in M.tolist()]

z, tau, rho = s.symbols('z tau rho')
J = s.Matrix([[0,0,0,2],[0,0,1,0],[0,-1,0,0],[-2,0,0,0]])
Omega = s.Matrix([[-2*z,1,tau,0],[rho,0,z,1]])
assert Omega * J.inv() * Omega.T == s.zeros(2)
assert J.det() == 4
period_map = {'J':mat(J),'Omega':mat(Omega),
              'Omega_J_inverse_Omega_transpose':mat(Omega*J.inv()*Omega.T),
              'Cstar_vector_lift':mat(s.Matrix([[0,0,0,1]])*J),
              'elliptic_coordinate_vector_lift':mat(s.Matrix([[0,1,0,0]])*J)}

Ts = [s.Matrix(M) for M in [
 [[1,0,-2,-1],[0,0,-1,0],[0,1,0,-1],[0,0,0,1]],
 [[1,0,2,2],[0,1,1,1],[0,0,1,0],[0,0,0,1]],
 [[1,0,0,0],[0,1,0,0],[0,-1,1,0],[0,0,0,1]],
 [[1,0,0,-1],[0,1,1,0],[0,0,1,0],[0,0,0,1]]]]
for T in Ts:
    assert T*J*T.T == J
assert Ts[0]*Ts[1]*Ts[2]*Ts[3] == s.eye(4)
assert Ts[0]**4 == s.eye(4)
for T in Ts[1:]:
    assert (T-s.eye(4))**2 == s.zeros(4)
monodromy = {'cohomological_matrices': [mat(T) for T in Ts],
             'nilpotent_ranks':[int((T-s.eye(4)).rank()) for T in Ts[1:]],
             'preserved_class':'T J T^t = J for every displayed T'}

p1,p2,p3,h1,h2 = s.symbols('p1 p2 p3 h1 h2')
R = s.Matrix([[1,p1,-h1,-h1*p1],[1,p2,-h2,-h2*p2],
              [1,p3,0,0],[0,0,1,p3]])
detR = s.factor(R.det())
assert s.simplify(detR + (h1-h2)*(p1-p3)*(p2-p3)) == 0
e1,e2,mu,b = s.symbols('e1 e2 mu b')
hdiff = s.factor(b/(2*(e1+mu))-b/(2*(e2+mu)))
assert s.simplify(hdiff-b*(e2-e1)/(2*(e1+mu)*(e2+mu))) == 0
t,e = s.symbols('t e')
delta=4*t**3+27*(mu*t+1)**2
assert s.simplify(s.discriminant(delta,t) - 314928*(mu**3-1)) == 0
node_relation=2*e**3+3*mu*e**2-1
assert s.simplify((e**3+(-3*e**2)*e+mu*(-3*e**2)+1)+node_relation)==0
restriction={'normalized_matrix':mat(R),'determinant':str(detR),
             'h1_minus_h2':str(hdiff),'node_relation':str(node_relation),
             'discriminant_of_discriminant':str(s.factor(s.discriminant(delta,t)))}

r,xp,yp = s.symbols('r xp yp',nonzero=True)
x=r**(-2)*xp; y=r**(-3)*yp
h=(y+b)/(2*(x+mu))
hp=(yp+b*r**3)/(2*(xp+mu*r**2))
assert s.simplify(h-r**(-1)*hp)==0
connection={'coefficient':'h=(y+b)/(2(x+mu))',
            'good_reduction_coefficient':'hprime=(yprime+b*r^3)/(2(xprime+mu*r^2))',
            'checked_identity':'h = r^(-1)*hprime; omega = r*omegaprime'}

def h0(k):
    return sum(1 for a in range(max(k,0)+1) for j in range(max(k,0)//4+1) if a+4*j==k)
def h1(k):
    return h0(-k-5)
degrees=list(range(-7,7))
weighted={str(k):[h0(k),h1(k)] for k in degrees}
assert [h0(-1),h1(-1),h0(-2),h1(-2)]==[0,0,0,0]
assert [h0(5),h0(4)]==[2,2]
# Each triple point contributes values(component1-component3,
# component2-component3); the two evaluations agree for constants.
C = s.Matrix([[1,0,-1],[0,1,-1],[1,0,-1],[0,1,-1]])
assert C.rank()==2
assert 3-C.rank()==1 and 4-C.rank()==2

a1,a2,a3=s.symbols('a1 a2 a3', nonzero=True)
M=s.Matrix([[1,a,-s.Rational(9,2)/a] for a in [a1,a2,a3]])
cross=s.factor(M.det())
assert s.simplify(cross-s.Rational(9,2)*(a1-a2)*(a1-a3)*(a2-a3)/(a1*a2*a3))==0

out={'schema':'S6_SERIES_PUBLISH.fresh_prereading_algebra.v1','target':'01GK/cdp:st:E13',
     'target_proof_opened':False,'prior_E_checks_opened':False,
     'period_identification':period_map,'monodromy':monodromy,
     'critical_restriction':restriction,'connection_transport':connection,
     'weighted_line_cohomology':weighted,'critical_theta_constant_map':mat(C),
     'critical_theta_h0_h1':[1,2],'cross_ratio_jacobian_minor':str(cross),
     'derived_cohomology':{'vertical':[1,1,0,0],'base_pullback':[2,4,2,0],
                           'critical_quotient':[3,4,0,0],'image_df':[0,1,2,0],
                           'tangent':[1,2,2,0]},
     'scope':'Algebraic certificate only; exact analytic maps are proved in the accompanying frozen derivation.'}
path=Path(__file__).with_name(Path(__file__).stem+'_output.json')
out['program_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'output':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                  'all_assertions_passed':True,'restriction_determinant':str(detR)}))
