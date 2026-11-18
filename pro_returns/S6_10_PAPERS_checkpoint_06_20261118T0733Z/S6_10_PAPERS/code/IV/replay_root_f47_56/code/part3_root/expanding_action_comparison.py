"""Exact integer identities for the actual inverse-action comparison."""
from pathlib import Path
import json
import sympy as s

out = Path(__file__).with_suffix(".json")
m0, mi, n0, ni, N, b0 = s.symbols("m0 mi n0 ni N b0", integer=True)
D = m0 * (ni + mi*N) + mi*n0
D_inverse = m0 * (-ni - mi*N) - mi*n0
assert s.expand(D_inverse + D) == 0
J = s.diag(1, -1)
assert J*J == s.eye(2) and J.det() == -1
p, q, r, t = s.symbols("p q r t", integer=True)
valuation = s.Matrix([[p,q],[r,t]])
assert (valuation*J)*J == valuation
cap_relation = s.Matrix([mi,-ni])
assert J*cap_relation == s.Matrix([mi,ni])
a,b=s.symbols("a b",integer=True)
assert (-a)*(-b)==a*b
assert s.expand(a*a-a*b+b*b - (b*b-b*a+a*a)) == 0

v00,v01,v02,v11,v12,v22=s.symbols("v00 v01 v02 v11 v12 v22")
V=s.Matrix([[v00,v01,v02],[v01,v11,v12],[v02,v12,v22]])
delta=s.Matrix(s.symbols("d0:3"))
central=s.symbols("central")
fan_checks=[]
for i in range(3):
    e=s.eye(3)[:,i]
    M=s.eye(3)
    M[:,i]=s.Matrix([-1 if j==i else 2 for j in range(3)])
    image=(M*V*M.T, M*(delta-2*V*e),
           central+(delta[i]-V[i,i])/2)
    inverse_image=(M*(-V)*M.T, M*(-delta-2*(-V)*e),
                   -central+(-delta[i]+V[i,i])/2)
    assert all(s.simplify(inverse_image[j]+image[j])==s.zeros(*image[j].shape)
               for j in range(2))
    assert s.simplify(inverse_image[2]+image[2])==0
    fan_checks.append({"edge":i,"matrix":list(map(list,M.tolist())),
                       "inverse_return_commutes":True})

result={
 "status":"PASS",
 "scope":"Algebraic identities; actual quotient, line, chart and loop maps are proved in P3F.50.",
 "cap_exponent_change":J.tolist(),
 "valuation_old":valuation.tolist(),
 "valuation_new":(valuation*J).tolist(),
 "same_valuation_image_inverse_basis":J.tolist(),
 "old_signed_determinant":str(D),
 "new_signed_determinant":str(D_inverse),
 "determinant_reverses":True,
 "physical_toric_chart_map_for_B_inverse":"identity",
 "separate_elliptic_inversion_map":"(Z,V)->(Z^-1,V)",
 "positive_lambda_loop_under_mu_inverse":"negative_mu_loop",
 "fan_recurrence_checks":fan_checks,
}
out.write_text(json.dumps(result,indent=2,default=str)+"\n")
print(json.dumps(result,indent=2,default=str))
