"""New exact exploration of the supplied marked matrices; targets unread."""
from pathlib import Path
from itertools import combinations,product
import json,re,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'build/continuation_numeric/python'))
from flint import fmpz_mat

BASE=Path(__file__).resolve().parents[2]
text=(BASE/'analysis/continuation_V/F2_6_integral_homology_statement_input_packet.md').read_text()
data=json.loads(re.search(r'```json\n(.*?)\n```',text,re.S).group(1))
def mat(x):return fmpz_mat(x)
def eye(n):return mat([[int(i==j) for j in range(n)] for i in range(n)])
def cols(v):return mat([[int(x[i]) for x in v] for i in range(len(v[0]))])
def seq(A):return [[int(A[i,j]) for j in range(A.ncols())] for i in range(A.nrows())]
def wedge(A,k):
 c=list(combinations(range(A.nrows()),k))
 return mat([[int(mat([[int(A[i,j]) for j in J] for i in I]).det()) for J in c] for I in c]) if k else mat([[1]])
def snf(A):
 S=A.snf();r=A.rank();return {'rank':r,'free':A.nrows()-r,'torsion':[int(S[i,i]) for i in range(r) if abs(S[i,i])>1]}
def inv(A):return mat(seq(A.inv()))
M1,M2=mat(data['M1']),mat(data['M2'])
D1=mat([r[1:] for r in data['M1'][1:]])
D2=mat([r[1:] for r in data['M2'][1:]])
out={'finite':{},'global':{}}
for name,D in [('D1',D1),('D2',D2)]:
 out['finite'][name]={str(q):snf(wedge(D.transpose(),q)-eye(len(list(combinations(range(5),q))))) for q in range(1,5)}
for q in range(1,5):
 A=wedge(M1.transpose(),q);B=wedge(M2.transpose(),q);I=eye(A.nrows());R=mat([seq(A-I)[i]+seq(B-I)[i] for i in range(A.nrows())]);out['global'][str(q)]=snf(R)
small=sorted(product(range(-1,2),repeat=5),key=lambda x:sum(abs(y) for y in x))
for v in small:
 if not any(v):continue
 V=mat([[x] for x in v]);orbit=[V]
 for k in range(4):orbit.append(D1*orbit[-1])
 C=cols([[int(o[i,0]) for i in range(5)] for o in orbit])
 if abs(C.det())==1:
  out['D1_conjugacy']={'basis':seq(C),'new_D':seq(inv(C)*D1*C)};break
minus=[v for v in small if any(v) and D2*mat([[x] for x in v])==-mat([[x] for x in v])]
for v in small:
 if not any(v):continue
 V=mat([[x] for x in v]);orbit=[V]
 for k in range(3):orbit.append(D2*orbit[-1])
 for w in minus:
  C=cols([[int(o[i,0]) for i in range(5)] for o in orbit]+[w])
  if abs(C.det())==1:
   out['D2_conjugacy']={'basis':seq(C),'new_D':seq(inv(C)*D2*C)};break
 if 'D2_conjugacy' in out:break
out['invariant_translations']={name:seq(M*mat([[x] for x in data[v]]))==[[x] for x in data[v]] for name,M,v in [('M1',M1,'v1'),('M2',M2,'v2')]}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
