"""Fresh marked-cycle composition, authored after target comparison.
Uses only the independently generated current collapse row matrices, and
recomputes each AW source column directly from the defining Kuhn faces.
No old producing code or its exported matrices are read.
"""
from pathlib import Path
from itertools import combinations
import json,hashlib
from flint import fmpz_mat
P=Path(__file__).resolve().parents[2]
x=json.loads((P/'code/continuation_V/P1_11_collapse_fresh.output.json').read_text())
rows={(z['p'],z['q']):z for z in x['full_exact_maps']}
rank={(z['p'],z['q']):z['target_rank'] for z in x['graded_homology_maps']}
faces=x['faces'];checks=[]
def mat(a,n=0):return fmpz_mat(a) if a else fmpz_mat(0,n)
def sign(seq):return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1
def wedge(M,k):
 idx=list(combinations(range(M.nrows()),k))
 return fmpz_mat([[int(fmpz_mat([[M[a,b] for b in J]for a in I]).det()) if k else 1 for J in idx]for I in idx])
def check(ok,name):
 if not ok:raise AssertionError(name)
 checks.append(name)
M=fmpz_mat([[int(i==j)+int(i<3 and j==i+3) for j in range(6)]for i in range(6)])
answer=[]
for k in range(7):
 basis=list(combinations(range(6),k));out=[];grade_ranges=[]
 for q in range(4):
  p=k-q
  if not 0<=p<=3:continue
  z=rows[p,q];n=rank[p,q];Q=mat(z['collapse_chain_map']);T=mat(z['target_projection'],Q.nrows());D=mat(z['source_differential'],len(faces[3-p])*len(list(combinations(range(3),q))))
  ai=list(combinations(range(3),q));cols=[]
  for K in basis:
   I=tuple(i for i in K if i<3);J=tuple(i-3 for i in K if i>=3);v=[0]*(len(faces[3-p])*len(ai))
   if len(I)==q and len(J)==p:
    comp=tuple(i for i in range(3) if i not in J);eps=sign(J+comp)*((-1)**(p*q))
    for fidx,F in enumerate(faces[3-p]):
     c=eps
     for t,j in enumerate(comp):c*=F[t+1][j]-F[t][j]
     v[fidx*len(ai)+ai.index(I)]=c
   col=fmpz_mat([[a]for a in v]);check(D*col==fmpz_mat(D.nrows(),1),f'k{k} p{p} q{q} source cycle {K}')
   value=T*Q*col if n else fmpz_mat(0,1);cols.append([int(value[i,0])for i in range(n)])
  block=[[cols[j][i]for j in range(len(basis))]for i in range(n)];out+=block;grade_ranges.append({'p':p,'q':q,'rows':n})
 C=mat(out,len(basis));W=wedge(M,k);I=fmpz_mat(W.nrows(),W.ncols())
 for i in range(W.nrows()):I[i,i]=1
 check(C*(W-I)==fmpz_mat(C.nrows(),W.ncols()),f'k{k} exact marked monodromy annihilation')
 snf=C.snf();diag=[abs(int(snf[i,i]))for i in range(min(snf.nrows(),snf.ncols())) if snf[i,i]]
 check(all(t==1 for t in diag),f'k{k} marked image primitive')
 check(len(diag)==x['graded_collapse_ranks'][k],f'k{k} marked rank')
 answer.append({'k':k,'source_basis':[list(z)for z in basis],'target_grading':grade_ranges,'marked_collapse_matrix':out,'smith':diag,'kernel_rank':len(basis)-len(diag)})
result={'status':'PASS','checks':len(checks),'check_names':checks,'scope':'Post-comparison fresh composition of marked integral AW source cycles with preread current quotient row maps. All full matrices, exact annihilation of exterior M0-I and primitive Smith factors retained. Does not read the original producers.','matrices':answer,'input_sha256':hashlib.sha256((P/'code/continuation_V/P1_11_collapse_fresh.output.json').read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'status':'PASS','checks':len(checks),'ranks':[len(z['smith'])for z in answer]}))
