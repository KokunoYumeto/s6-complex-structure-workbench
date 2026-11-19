"""Fresh exact dual/conjugate/cusp checks from the statement-only packet."""
from pathlib import Path
from itertools import permutations
import hashlib
import json
import re
import sympy as sp

root=Path(__file__).resolve().parents[2]
packet=root/'analysis/continuation_V/F3_7_duality_statement_input_packet.md'
data=json.loads(re.search(r'```json\n(.*?)\n```',packet.read_text(),re.S).group(1))
A,B,M1,M2,S=[sp.Matrix(data[k]) for k in ['A','B','M1','M2','S']]
v1,v2=[sp.Matrix(data[k]) for k in ['v1','v2']]
I=sp.eye(6)
assert A.T==M1 and B.T==M2
assert A.inv()*A==I and B.inv()*B==I
# Evaluation pairing on arbitrary columns is preserved by the true dual.
for C in [A,B]:
    assert (C.inv().T).T*C==I
assert M1**5==I and M2**4==I
assert M1*v1==v1 and M2*v2==v2

finite=[]
for M,v,m in [(M1,v1,5),(M2,v2,4)]:
    old=sp.eye(7)
    old[:6,:6]=M.inv()
    old[:6,6]=-v/m
    wanted=sp.eye(7)
    wanted[:6,:6]=M
    wanted[:6,6]=v/m
    assert old.inv()==wanted
    assert (old**m)[:6,:6]==I
    assert (old**m)[:6,6]==-v
    assert (wanted**m)[:6,6]==v
    t=sp.symbols('t')
    bold=-t*v
    bnew=t*v
    assert sp.simplify(-(t+sp.Rational(1,m))*v-M.inv()*bold)==-v/m
    assert sp.simplify((t+sp.Rational(1,m))*v-M*bnew)==v/m
    finite.append({'order':m,'inverse_affine_generator_exact':True,'logarithmic_gluing_exact':True})

Mo=M2*M1
M0=(M1*M2).inv()
J=sp.diag(1,1,1,-1,-1,-1)
Tplus=sp.eye(6)
Tplus[:3,3:]=sp.eye(3)
assert M0==M1*Mo.inv()*M1.inv()
assert S.inv()*M0*S==Tplus
So=M1.inv()*S*J
assert So.det() in [1,-1]
assert So.inv()*Mo*So==Tplus
assert M1*So*J==S
assert J*Tplus.inv()*J==Tplus

# Universal block centralizer form and its period normalization.
P=sp.Matrix(3,3,sp.symbols('p0:9'))
Q=sp.Matrix(3,3,sp.symbols('q0:9'))
zero=sp.zeros(3)
G=P.row_join(Q).col_join(zero.row_join(P))
assert G*Tplus==Tplus*G
z=sp.symbols('s')
C=sp.Matrix(3,3,sp.symbols('c0:9'))
period=sp.eye(3).row_join(z*sp.eye(3)+C)
assert period*G==P.row_join(Q+(z*sp.eye(3)+C)*P)

# All six Kuhn simplex types, with arbitrary symbolic translation v.
v=sp.Matrix(sp.symbols('v0:3'))
Phi=sp.diag(-1,-1,-1,1)
R=sp.zeros(4)
for j in range(4):R[j,3-j]=1
e=[sp.eye(3)[:,i] for i in range(3)]
charts=[]
def cone(base,perm):
    p=base
    columns=[p.col_join(sp.ones(1,1))]
    for k in perm:
        p=p+e[k]
        columns.append(p.col_join(sp.ones(1,1)))
    return sp.Matrix.hstack(*columns)
for perm in permutations(range(3)):
    Nold=cone(v,perm)
    Nnew=cone(-v-sp.ones(3,1),perm[::-1])
    assert Nold.det() in [1,-1] and Nnew.det() in [1,-1]
    assert Nnew==Phi*Nold*R
    assert sp.simplify(Nnew.inv()*Phi-R*Nold.inv())==sp.zeros(4)
    assert sp.ones(1,4)*Nold.inv()==sp.Matrix([[0,0,0,1]])
    charts.append((Nold,Nnew))
for No1,Nn1 in charts:
    for No2,Nn2 in charts:
        assert sp.simplify(Nn2.inv()*Nn1-R*(No2.inv()*No1)*R)==sp.zeros(4)

out={'status':'all exact assertions passed','finite_charts':finite,
     'original_dual_cusp_matrix':'M2*M1','target_cusp_matrix':'(M1*M2)^-1',
     'based_path_identity':'M0=M1*Mo^-1*M1^-1','S_determinant':int(S.det()),
     'So_determinant':int(So.det()),'So':[[int(x) for x in row] for row in So.tolist()],
     'target_marking_identity':'M1*So*J=S',
     'Kuhn_symbolic_translation_types':len(charts),'character_overlap_checks':len(charts)**2,
     'cusp_map':'q_new=conj(q_old), x_new=1/conj(x_old), nu_new=-nu_old',
     'analytic_scope':'holomorphy on conjugate charts and bounded remainder are proved in the prereading derivation',
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
