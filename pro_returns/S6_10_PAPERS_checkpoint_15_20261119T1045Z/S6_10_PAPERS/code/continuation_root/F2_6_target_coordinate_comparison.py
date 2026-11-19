"""Fresh post-exposure arithmetic comparing the printed bases and classes.

This does not read any producing program and does not mutate prereading outputs.
"""
from pathlib import Path
from itertools import combinations
import json,re,sys,datetime
BASE=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(BASE/'build/continuation_numeric/python'))
from flint import fmpz_mat,fmpq_mat
def Z(x):return fmpz_mat(x)
def rows(A):return [[int(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]
def sub(A,rs,cs):return Z([[int(A[i,j]) for j in cs] for i in rs])
def eye(n):return Z([[int(i==j) for j in range(n)] for i in range(n)])
def ext(A,k):
 c=list(combinations(range(A.nrows()),k));return Z([[int(sub(A,I,J).det()) for J in c] for I in c])
def exact_image_preimage(A,w):
 H,U=A.transpose().hnf(transform=True);r=A.rank();B=sub(H,range(r),range(H.ncols())).transpose();V=sub(U,range(r),range(U.ncols())).transpose();assert A*V==B
 HB,T=B.hnf(transform=True);v=T*w;assert all(v[i,0]==0 for i in range(r,v.nrows()));W=sub(HB,range(r),range(r));x=fmpq_mat(W).inv()*fmpq_mat(sub(v,range(r),[0]));assert all(x[i,0]==int(x[i,0]) for i in range(r));ans=V*Z(rows(x));assert A*ans==w;return ans
packet=(BASE/'analysis/continuation_V/F2_6_integral_homology_statement_input_packet.md').read_text();d=json.loads(re.search(r'```json\n(.*?)\n```',packet,re.S).group(1))
D=Z([r[1:] for r in d['M2'][1:]])
P=Z([[-1,0,-1,0,1],[-1,2,-1,1,3],[-1,1,-1,2,3],[0,-1,0,-1,-1],[1,-1,2,-1,-3]])
C=Z([[-1,0,-1,0,-1],[0,1,0,0,0],[0,0,0,1,0],[0,-1,0,-1,1],[0,0,1,0,0]])
Q=Z(rows(C.inv().transpose()));T=Z(rows(C.inv()*P));canonical=Z(rows(C.inv()*D*C));assert abs(P.det())==1 and abs(C.det())==1 and abs(T.det())==1;assert P==C*T;assert D*P==P*canonical;assert T*canonical==canonical*T
old={1:[0,0,0,-1,-2],2:[0,0,0,0,0,0,0,1,0,-1],3:[0,0,0,0,0,0,1,0,0,0]}
indices={1:(4,),2:(0,2),3:(0,2,4)}
out={'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'chronology':'Post-target comparison only; prereading program and output files are not altered.','actual_basis_transition_C_inverse_P':rows(T),'inverse_transition':rows(Z(rows(T.inv()))),'basis_identity':'P=C T; T commutes with the common signed permutation','degrees':{}}
for k in range(1,4):
 basis=list(combinations(range(5),k));u=Z([[int(J==indices[k])] for J in basis]);new=ext(Q,k)*u;prior=Z([[x] for x in old[k]]);E=ext(D.transpose(),k)-eye(len(basis));a=exact_image_preimage(E,prior-new);twice=exact_image_preimage(E,2*prior)
 out['degrees'][str(k+1)]={'old_representative':rows(prior),'root_representative':rows(new),'difference_preimage_under_T_minus_I':rows(a),'twice_old_preimage':rows(twice)}
out['status']='passed';Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
