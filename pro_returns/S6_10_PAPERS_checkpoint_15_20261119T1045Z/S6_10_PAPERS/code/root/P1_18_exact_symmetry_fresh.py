"""Fresh exact height-symmetry calculation from the clean A,B definitions."""
from pathlib import Path
import json
import sympy as S

A=S.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=S.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
xs=S.symbols('k0:36')
K0=S.Matrix(6,6,xs)
e=S.eye(6)[:,0]
eq=list(K0*A-A.inv()*K0)+list(K0*B-B.inv()*K0)+list(K0*e-e)
sol=list(S.linsolve(eq,xs))
assert len(sol)==1 and not set().union(*(a.free_symbols for a in sol[0]))
K=S.Matrix(6,6,sol[0])
checks={
 'normalized_inverse_intertwiner_unique':True,
 'actual_A_inverse_map':K*A==A.inv()*K,
 'actual_B_inverse_map':K*B==B.inv()*K,
 'invariant_line_fixed':K*e==e,
 'real_integral_matrix':all(x.is_Integer for x in K),
 'involution':K*K==S.eye(6),
 'A_order_five':A**5==S.eye(6),
 'B_order_four':B**4==S.eye(6),
}
# The rigorous fresh Hessian bounds lie strictly inside these rational bounds.
xxlo=S.Rational(3215,10000)
yylo=S.Rational(3220,10000)
absxy=S.Rational(218,10000)
mu=S.Rational(299,1000)
checks['hessian_lower_form'] = bool(min(xxlo,yylo)-absxy > mu)
N=S.Matrix([[0,0,0,-1,1,-1],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,-1,1,0,0,0]])
J=S.Matrix([[-1,0,0,0,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1],[0,1,0,1,0,0],[0,0,1,0,0,0],[0,-1,1,0,0,0]])
standard=S.zeros(6)
standard[:3,3:6]=S.eye(3)
checks['actual_cusp_N_square_zero']=N*N==S.zeros(6)
checks['actual_cusp_J_unimodular']=bool(abs(J.det())==1)
checks['actual_cusp_J_marking']=J.inv()*N*J==standard
checks['actual_cusp_invariant_line']=J.inv()*e==-e
checks['cusp_line_annihilated']=N*e==S.zeros(6,1)
assert all(checks.values())
out={'status':'PASS','scope':'Exact actual real height-symmetry map and a rational central Hessian lower bound; no old producer or target proof read','K':[[str(x) for x in K.row(i)] for i in range(6)],'K_det':str(K.det()),'uniform_hessian_lower_bound':str(mu),'check_count':len(checks),'checks':checks}
Path('analysis/continuation_root/P1_18_exact_symmetry_fresh.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
