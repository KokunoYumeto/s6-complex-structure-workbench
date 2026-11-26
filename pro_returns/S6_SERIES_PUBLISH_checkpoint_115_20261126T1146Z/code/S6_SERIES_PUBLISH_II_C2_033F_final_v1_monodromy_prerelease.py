"""Fresh prerelease calculation from Viaclovsky arXiv2610.39102v1, (2.1).
No target proof and no earlier program/output is read.
Basis (delta,a,b,d), column-vector convention. T is obtained directly
from log(u)/(2*pi*i) gaining one around the positive u circle.
"""
import sympy as s
from pathlib import Path
import json
A0=s.Matrix([[1,-1,0,2],[0,-1,-1,6],[0,1,0,0],[0,0,0,1]])
A1=s.Matrix([[1,0,1,-3],[0,0,1,0],[0,-1,0,6],[0,0,0,1]])
Ai=s.Matrix([[1,0,0,1],[0,1,1,0],[0,0,1,0],[0,0,0,1]])
I=s.eye(4);E=s.zeros(4);E[0,3]=1;T=I+E
assert A0**3==I and A1**4==I and A0*A1*Ai==I
assert E**2==s.zeros(4)
assert all(A*T==T*A for A in (A0,A1,Ai))
Q=Ai-I
assert Q**2==s.zeros(4) and E*Q==s.zeros(4) and Q*E==s.zeros(4)
p,N=s.symbols('p N',integer=True)
combined=s.expand((I+p*Q)*(I+N*E))
assert combined[1,2]==p and combined[0,3]==p+N
res={'basis':['delta','a','b','d'],'finite_orders':[3,4],'base_product_identity':True,'parameter_monodromy_T':[[int(x) for x in row] for row in T.tolist()],'T_commutes_with_each_base_matrix':True,'cusp_power_times_parameter_power':[[str(x) for x in row] for row in combined.tolist()],'finite_case_argument':'(A_j^p T^N)^e=T^(e N); identity forces N=0 since its (1,4)-entry is e N.','cusp_case_argument':'identity forces p=0 from (2,3), then N=0 from (1,4).','timing':'constructed and run before target-proof release'}
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
