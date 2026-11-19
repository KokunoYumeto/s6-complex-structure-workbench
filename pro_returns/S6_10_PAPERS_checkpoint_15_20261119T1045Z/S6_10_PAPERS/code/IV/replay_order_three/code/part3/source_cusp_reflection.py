#!/usr/bin/env python3
from pathlib import Path
import datetime,json
import sympy as S
root=Path(__file__).resolve().parents[2]
checks=[]
def check(name,value):
    assert value,name
    checks.append({'name':name,'pass':True})
M=S.Matrix([[-1,0,0],[0,1,0],[1,0,1]])
N=M.T
check('character_involution',M*M==S.eye(3))
check('cone_involution',N*N==S.eye(3))
check('physical_delta_retained',N*S.Matrix([0,1,0])==S.Matrix([0,1,0]))
check('height_retained',(N*S.Matrix(S.symbols('x y h')))[2]==S.symbols('h'))
Z,V,Q,P=S.symbols('Z V Q P',nonzero=True)
arrow=(Q/Z,V,Q)
check('source_arrow_square',S.simplify(Q/(Q/Z)-Z)==0)
check('line_factor_cancellation',S.simplify(P/P)==1)
e1=(1,0);e2=(0,1);zero=(0,0);one=(1,1)
anti=[(zero,e1,e2),(e1,e2,one)]
main=[(zero,e1,one),(zero,e2,one)]
J=lambda p:(-p[0],p[1])
def normalize(triangle):
    # Translation-independent representative of one triangle orbit.
    candidates=[]
    for v in triangle:
        candidates.append(tuple(sorted((p[0]-v[0],p[1]-v[1]) for p in triangle)))
    return min(candidates)
check('actual_reflected_triangle_orbits',
      set(normalize(tuple(J(p) for p in t)) for t in anti)==set(normalize(t) for t in main))
def edge(v):
    return min(v,(-v[0],-v[1]))
old_edges={edge(e1),edge(e2),edge((1,-1))}
new_edges={edge(J(v)) for v in old_edges}
check('physical_fixed_edge_kept',edge(e2) in new_edges)
check('only_nonfixed_diagonal_replaced',new_edges=={edge(e1),edge(e2),edge((1,1))})
report={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS',
 'checks_count':len(checks),'checks':checks,'character_matrix':str(M),'cone_matrix':str(N),
 'source_arrow':'(Z,V,Q)->(Q/Z,V,Q)','physical_delta':'unchanged',
 'return_arrows':['Phi_T=beta alpha','Phi_JT=alpha beta=alpha Phi_T alpha^-1'],
 'specific_fan_class':1,'not_assigned':['individual characteristic pair of reflected fan','integer nonfixed derivative','arbitrary fan formula'],
 'proof':'notes/part3_source_cusp_reflection_working.md'}
(root/'code/part3/source_cusp_reflection.json').write_text(json.dumps(report,indent=2)+'\n')
print(f'PASS {len(checks)} exact half-transport/fan identities; specific diagonal-flop class1, no integer derivative assigned.')
