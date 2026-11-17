"""Independent integral checks for the actual prism transgression lemma."""
from itertools import combinations
from pathlib import Path
import json
from sympy import Matrix, eye, zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form

A=Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],
          [0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],
          [0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
D=B.T[1:,1:]
P=Matrix([[-1,0,-1,0,1],[-1,2,-1,1,3],[-1,1,-1,2,3],
          [0,-1,0,-1,-1],[1,-1,2,-1,-3]])
C=Matrix([[0,0,0,1,0],[1,0,0,0,0],[0,1,0,0,0],
          [0,0,1,0,0],[0,0,0,0,-1]])
assert abs(P.det())==1 and D*P==P*C and D**4==eye(5)
assert Matrix([[1,-4],[0,1]]).det()==1
def ext(M,p):
 ii=list(combinations(range(M.rows),p))
 return Matrix([[M.extract(i,j).det() for j in ii] for i in ii])
def factors(M):
 S=smith_normal_form(M,domain=ZZ)
 return [abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]
reps={2:[0,0,0,-1,-2],3:[0,0,0,0,0,0,0,1,0,-1],
      4:[0,0,0,0,0,0,1,0,0,0]}
checks=[]
for q,v in reps.items():
 p=q-1;T=ext(D.T,p);w=Matrix(v);n=T.rows
 norm=sum((T**j for j in range(4)),zeros(n))
 inverse_norm=sum((T**(-j) for j in range(1,5)),zeros(n))
 assert norm==inverse_norm and norm*w==zeros(n,1)
 H=hermite_normal_form(T-eye(n));coordinates=H.gauss_jordan_solve(w)[0]
 assert all((2*x).q==1 for x in coordinates) and any(x.q!=1 for x in coordinates)
 global_inds=list(combinations(range(6),p));vert_inds=list(combinations(range(5),p))
 wf=Matrix([0 if 0 in s else w[vert_inds.index(tuple(i-1 for i in s))] for s in global_inds])
 AA,BB=ext(A,p),ext(B,p)
 R=Matrix.hstack(AA-eye(AA.rows),BB-eye(BB.rows))
 f=factors(R);aug=factors(Matrix.hstack(R,wf))
 assert len(f)==AA.rows and f.count(2)==1 and all(x in (1,2) for x in f)
 assert aug==[1]*AA.rows
 checks.append({'degree':q,'norm_zero':True,'local_order':2,
   'global_factors':f,'augmented_factors':aug,'boundary_theta_component':'w',
   'boundary_fibre_component':'0','global_residue':'nonzero in Z/2'})
out={'status':'PASS','checks':checks,'scope':'Integer matrices and actual four-prism boundary formulas; geometric Leray identification is in the proof supplement.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
