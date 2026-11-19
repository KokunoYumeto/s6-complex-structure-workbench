#!/usr/bin/env python3
"""New exact determinant implementation of printed B.6.20 arithmetic.

Written from the displayed matrices and forms on 19 November 2026.
No source program was opened or reused.  Exterior products are evaluated
as ordinary determinants in SymPy, including the transported last boundary.
The program verifies these algebraic data; it supplies no geometric premise.
"""
import json
from pathlib import Path
import sympy as S

I=S.eye(4);g,u,w,k=[I[:,j] for j in range(4)]
A1=S.Matrix([[1,0,0,0],[6,0,1,-1],[-6,-1,-1,1],[0,0,0,1]])
A2=S.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,1],[0,0,0,1]])
C1=I+w*(u-g).T;C2=I+w*g.T
eta=[-4*g-w,-3*g+u+k,S.zeros(4,1)]
alpha=[-2*g+u+k,3*g+w-k]
orders=[3,4];power=[S.Matrix([1,2,-4,0]),S.Matrix([-1,-3,3,0])]
beta=[-2*S.Rational(v[0],m)*k+2*S.Rational(v[3],m)*g for v,m in zip(power,orders)]
b=[eta[j]-beta[j] for j in range(2)]
lam=[(-u+w)/3,(-u+w)/2]

def cube_collar(v,q):
    # 3 * [v (2 G wedge K) q]_{G,U,W,K}
    return 6*S.Matrix.hstack(v,g,k,q).det()

checks={}
checks['global_monodromy_product']=(A1*A2*C1*C2==I)
checks['finite_cap_forms']=[list(v) for v in beta]
checks['lifted_euler_coboundaries']=[eta[j]==-alpha[j]+(A.T-I)*(-u) for j,A in enumerate([A1,A2])]
checks['boundary_primitives']=[(A.T-I)*lam[j]==b[j] for j,A in enumerate([A1,A2])]
checks['finite_collar_integrals']=[cube_collar(lam[j],b[j]) for j in range(2)]
segments=[-C2.T*C1.T*A2.T*eta[0],-C2.T*C1.T*eta[1],-C2.T*eta[2]]
checks['last_boundary_segments']=[list(x) for x in segments]
checks['last_boundary_sum_is_G']=(sum(segments,S.zeros(4,1))==g)
checks['last_boundary_primitive_closes']=((C2.T-I)*w==g)
primitive=w.copy();last=[]
for segment in segments:
    last.append(cube_collar(primitive,segment))
    primitive+=segment
checks['last_boundary_collar_integrals']=last
checks['raw_algebraic_cube']=sum(checks['finite_collar_integrals'])+sum(last)
checks['inverse_boundary_primitive']=[-A.inv().T*b[j]==(A.inv().T-I)*lam[j] for j,A in enumerate([A1,A2])]
checks['inverse_collar_integrals']=[cube_collar(lam[j],-A.inv().T*b[j]) for j,A in enumerate([A1,A2])]
checks['spin_congruence_solutions']=[j for j in [-1,1] if (-4-4*j)%24==0]
ks,ls=S.symbols('k_U ell_U')
checks['dual_index_polynomial']=S.expand((4*(-ks)-(-ls))/24+(4*ks-ls)/24)
checks['reference_pairs']={'meridian':[-1,-4],'physical':[1,4],'both_indices': [0,0]}

assert checks['global_monodromy_product']
assert all(checks['lifted_euler_coboundaries']) and all(checks['boundary_primitives'])
assert checks['finite_collar_integrals']==[2,-3]
assert checks['last_boundary_sum_is_G'] and checks['last_boundary_primitive_closes']
assert sum(last)==0 and checks['raw_algebraic_cube']==-1
assert all(checks['inverse_boundary_primitive'])
assert checks['inverse_collar_integrals']==[-2,3]
assert checks['spin_congruence_solutions']==[-1]
assert checks['dual_index_polynomial']==0

payload={'method':'Exact rational matrix operations and determinants, SymPy '+S.__version__,
         'source':'Printed maps:src:B.6.20 steps 1, 3–8; line convention from night:P3K.68',
         'scope':'Algebraic identities only; no full geometric proof claim',
         'checks':checks,'outcome':'PASS'}
text=json.dumps(payload,default=str,indent=2)
target=Path(__file__).with_suffix('.output.json');target.write_text(text+'\n')
print(text)
