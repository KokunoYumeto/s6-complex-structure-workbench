"""Exact checks for the circle quotient and its framing obstruction.

No numerical approximation is used.  The finite tests modulo 2 exhaust F_2^4.
The lens-space arithmetic is symbolic, not a bounded search.
"""
import itertools
import json
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

I=s.eye(4)
T1=s.Matrix([[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]])
T2=s.Matrix([[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]])
A1=T1.inv().T; A2=T2.inv().T; M0=(A1*A2).inv()
v1=s.Matrix([1,2,-4,0]); v2=s.Matrix([-1,-3,3,0])
e=[I[:,i] for i in range(4)]

def mat(A): return [[str(x) for x in row] for row in A.tolist()]
def kernel(A): return [list(map(str,v)) for v in A.nullspace()]
def fixed_mod2(matrices):
    return [list(c) for c in itertools.product(range(2),repeat=4)
            if all(all(int(a)%2==0 for a in s.Matrix([c])*(A-I)) for A in matrices)]

out={"A1":mat(A1),"A2":mat(A2),"M0":mat(M0),
     "orders_and_product":[A1**3==I,A2**4==I,A1*A2*M0==I],
     "fixed_twists":[A1*v1==v1,A2*v2==v2],
     "twist_characters":[int(v1[0]),int(v2[0])],
     "fixed_vectors":kernel((A1-I).col_join(A2-I)),
     "fixed_covectors":kernel((A1.T-I).col_join(A2.T-I)),
     "fixed_covectors_mod2":fixed_mod2([A1,A2]),
     "coinvariants_smith":mat(smith_normal_form((A1-I).row_join(A2-I),domain=s.ZZ)),
     "invariant_H3_evaluation_on_L":str(s.Matrix.hstack(e[3],e[1],e[2],e[3]).det())}
B=s.Matrix([[0,1],[-1,0]])
out["toric_triple_paths"]=[{"a":list(map(str,a)),"Ba":list(map(str,B*a)),
                            "character":str(a[0]%1)}
                           for a in (s.Matrix([-s.Rational(1,4),s.Rational(1,4)]),
                                     s.Matrix([-s.Rational(1,2),s.Rational(1,4)]))]
out["edge_character_slopes"]=[str((B.inv()*w)[0]) for w in
                               (s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([1,-1]))]
l0,l1,l2,a,b=s.symbols('l0 l1 l2 a b',integer=True)
mu1=s.Matrix([3,-l1]); mu2=s.Matrix([-4,4*l0-l2]); lam1=s.Matrix([a,b])
p=12*l0-4*l1-3*l2
q=4*b+a*(4*l0-l2)
out["lens_arithmetic"]={"det_meridians":str(s.det(s.Matrix.hstack(mu1,mu2))),
                         "det_mu1_lambda1":str(s.det(s.Matrix.hstack(mu1,lam1))),
                         "q":str(q),"3q_minus_ap":str(s.expand(3*q-a*p)),
                         "meridian_reconstruction":mat(s.simplify(-q*mu1+p*lam1-mu2))}
# These exact matrices are K11, checked in the supplied checkpoint section E.5.2.
HV=[s.Matrix(x) for x in [
 [[1,0,0,0],[-2,0,-1,0],[0,1,0,0],[1,1,0,1]],
 [[1,0,0,0],[0,1,0,0],[-2,-1,1,0],[-2,-1,0,1]],
 [[1,0,0,0],[0,1,1,0],[0,0,1,0],[0,0,0,1]],
 [[1,0,0,0],[0,1,0,0],[0,-1,1,0],[1,0,0,1]]]]
out["viaclovsky_two_parameter"]={
    "fixed_vectors":kernel(s.Matrix.vstack(*[A-I for A in HV])),
    "fixed_covectors":kernel(s.Matrix.vstack(*[A.T-I for A in HV])),
    "fixed_covectors_mod2":fixed_mod2(HV),
    "unipotent_ranks":[(A-I).rank() for A in HV[1:]],
    "unipotent_squares_zero":[(A-I)**2==s.zeros(4) for A in HV[1:]]}
HLR=[s.Matrix(x) for x in [
 [[-1,-1,-1,0],[2,1,1,0],[0,0,1,0],[0,0,0,1]],
 [[1,1,0,1],[-2,0,-1,-1],[0,-1,1,-1],[0,0,0,1]]]]
out["liu_rollenske"]={
    "fixed_vectors":kernel(s.Matrix.vstack(*[A-I for A in HLR])),
    "fixed_covectors":kernel(s.Matrix.vstack(*[A.T-I for A in HLR])),
    "fixed_covectors_mod2":fixed_mod2(HLR),
    "finite_orders":[HLR[0]**4==I,HLR[1]**6==I],
    "cusp_square_zero":((HLR[1]*HLR[0]).inv()-I)**2==s.zeros(4)}
PE=s.Matrix([[0,-2,-1,-2],[2,-1,0,-1],[0,2,1,3],[-1,0,0,0]])
out["engel_dictionary"]={"P_E":mat(PE),"det":str(PE.det()),
                          "psi_P_E":mat(s.Matrix([[0,0,0,1]])*PE),
                          "T0":mat(PE*A1*PE.inv()),"T1":mat(PE*A2*PE.inv()),
                          "P_E_v1":mat(PE*v1),"P_E_minus_v2":mat(-PE*v2)}
PV=s.Matrix([[-2,1,0,1],[-6,0,-1,0],[0,-1,0,0],[-1,0,0,0]])
V0=s.Matrix([[1,-1,0,2],[0,-1,-1,6],[0,1,0,0],[0,0,0,1]])
V1=s.Matrix([[1,0,1,-3],[0,0,1,0],[0,-1,0,6],[0,0,0,1]])
out["K1_dictionary"]={"det":str(PV.det()),
                      "monodromy_intertwining":[V0*PV==PV*A1,V1*PV==PV*A2],
                      "P_V_v1":mat(PV*v1),"P_V_minus_v2":mat(-PV*v2),
                      "P_V_delta":mat(PV*e[3])}
k1,k2,k3,lam=s.symbols('k1 k2 k3 lam',real=True)
pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
D=k1*pauli[0]+k2*pauli[1]+k3*pauli[2]
out["dirac_fourier_symbol"]={"trace":str(s.trace(D)),
    "characteristic_polynomial":str(s.expand((lam*s.eye(2)-D).det())),
    "square":mat(s.simplify(D**2)),"zero_mode_dimension":2,
    "real_e_invariant":str(s.Rational(1,2)*s.Rational(2,2))}
target=Path(__file__).with_suffix('.out.json')
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
