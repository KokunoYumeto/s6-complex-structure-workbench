#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
from itertools import combinations
import sympy as s,json
checks=[]
def ck(n,b):assert b,n;checks.append(n)
X=s.Matrix(3,3,s.symbols('x0:9',real=True));Y=s.Matrix(3,3,s.symbols('y0:9',real=True));Z=X+s.I*Y;I=s.eye(3);O=s.zeros(3)
K=(-Z).row_join(-s.conjugate(Z)).col_join(I.row_join(I));T=I.row_join(Z).col_join(O.row_join(I));J=O.row_join(I).col_join(I.row_join(O))
ck('actual complex graph row-operation map',s.simplify(J*T*K-I.row_join(I).col_join(O.row_join(2*s.I*Y)))==s.zeros(6))
ck('actual row-block exchange sign',J.det()==-1)
ck('three-dimensional imaginary determinant factor',s.expand(-(2*s.I*Y).det()-8*s.I*Y.det())==0)
realmap=I.row_join(X).col_join(O.row_join(Y))
ck('actual real quotient determinant',s.simplify(realmap.det()-Y.det())==0)
ck('actual graph kernel',[I.row_join(Z)*(-Z).col_join(I)]==[s.zeros(3)])
B=s.Matrix([[1,s.I,1],[0,1,2*s.I],[2,0,1]]);ck('example complex frame invertible',B.det()!=0)
Q=B*s.Matrix([[1,s.I,0,0,0,0],[0,0,1,s.I,0,0],[0,0,0,0,1,s.I]])
indices=next(t for t in combinations(range(6),3) if Q[:,t].det()!=0);rest=tuple(i for i in range(6) if i not in indices);perm=indices+rest;P=s.eye(6)[:,perm];BB=(Q*P)[:,:3];CC=(Q*P)[:,3:];ZZ=BB.inv()*CC
ck('actual selected indices',(indices,rest)==((0,2,4),(1,3,5)))
ck('integer marked permutation',abs(P.det())==1 and P.T*P==s.eye(6))
ck('actual B inverse normalized period map',BB.inv()*Q*P==I.row_join(ZZ))
ck('actual original-marking kernel map',Q*P*(-ZZ).col_join(I)==s.zeros(3))
ck('normalized imaginary determinant',s.im(ZZ).det()==1)
D=s.eye(2).row_join(s.zeros(2,9));R=s.eye(2).col_join(s.zeros(9,2))
ck('actual Grassmann projection differential right inverse',D*R==s.eye(2))
r={'status':'PASS','checks':len(checks),'check_names':checks,'actual_selected_indices':indices,'actual_complementary_indices':rest,'actual_permutation_determinant':int(P.det()),'normalized_Z':str(ZZ),'graph_determinant_factor':'8i det(Im Z)','source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'target_opened':False}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
