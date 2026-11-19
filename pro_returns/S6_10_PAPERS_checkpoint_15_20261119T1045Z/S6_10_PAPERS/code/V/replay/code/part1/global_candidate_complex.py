"""Diagnostic MV complex with cusp suspension map set to zero.
This is an EXACT computation of a candidate chain model, NOT a proof that
it is the actual gluing: the boundary suspension term needs geometric proof.
"""
from pathlib import Path
from itertools import combinations
import contextlib,io,json,importlib.util
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 exec(Path(__file__).with_name('cusp_marked_collapse.py').read_text().replace("Path(__file__).with_suffix('.json').write_text(json.dumps({str(k):m.tolist() for k,m in maps.items()},indent=2,default=int))",''))
root=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('tupledata',root/'background/data/fourfold_tuple.py');t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)
I=s.eye(6);M=[t.M0,t.M1,t.M2]
# Exterior power matrices with zero-size conventions outside 0..rank.
def ext(m,k):
 if k<0:return s.zeros(0,0)
 return wedge(m,k)
def dim(n,k):return int(s.binomial(n,k)) if 0<=k<=n else 0
W={(i,k):ext(M[i],k) for i in range(3) for k in range(8)}
N=t.M0-I
S=s.Matrix.hstack(N[:,0],N[:,3],N[:,4],I[:,0],I[:,3],I[:,4]);assert abs(S.det())==1 and S.inv()*t.M0*S==Mstd
print('cusp_marking_S',S)
R={};P={};sgn={}
for i,v,m in [(1,t.v1,5),(2,t.v2,4)]:
 sgn[i]=int(v[0]);vp=sgn[i]*v;P[i]=vp.row_join(I[:,1:]);assert abs(P[i].det())==1
 R[i]=(P[i].inv()*M[i]*P[i])[1:,1:]
 print('finite_marking',i,P[i]);print('finite_R',i,R[i])

def main_dim(k):return dim(6,k)+2*dim(6,k-1)
def bdry_dim(k):return dim(6,k)+dim(6,k-1)
def cap_dim(i,k):return dim(5,k)+dim(5,k-1)
def cusp_dim(k):return [1,3,9,9,10,3,1][k] if 0<=k<=6 else 0

def dmain(k):
 a=s.zeros(main_dim(k-1),main_dim(k));n=dim(6,k);l=dim(6,k-1)
 if l:a[:l,n:n+l]=W[1,k-1]-s.eye(l);a[:l,n+l:n+2*l]=W[2,k-1]-s.eye(l)
 return a

def dbdry(i,k):
 a=s.zeros(bdry_dim(k-1),bdry_dim(k));n=dim(6,k);l=dim(6,k-1)
 if l:a[:l,n:]=W[i,k-1]-s.eye(l)
 return a

def dcap(i,k):
 a=s.zeros(cap_dim(i,k-1),cap_dim(i,k));n=dim(5,k);l=dim(5,k-1)
 if l:a[:l,n:]=ext(R[i],k-1)-s.eye(l)
 return a

def fmain(i,k):
 a=s.zeros(main_dim(k),bdry_dim(k));n=dim(6,k);l=dim(6,k-1)
 a[:n,:n]=s.eye(n)
 if l:
  if i:a[n+(i-1)*l:n+i*l,n:]=s.eye(l)
  else:
   a[n:n+l,n:]=-W[2,k-1]*W[0,k-1];a[n+l:n+2*l,n:]=-W[0,k-1]
 return a

def fcap(i,k):
 # In split v,K coordinates, wedge order with v first.
 n=dim(6,k);l=dim(6,k-1);cn=dim(5,k);cl=dim(5,k-1)
 a=s.zeros(cn+cl,n+l);b=s.zeros(cn+cl,n+l)
 inds=list(combinations(range(6),k));low=list(combinations(range(6),k-1)) if k else []
 for j,J in enumerate(inds):
  if 0 not in J:
   row=list(combinations(range(5),k)).index(tuple(x-1 for x in J));b[row,j]=1
  else:
   col=list(combinations(range(5),k-1)).index(tuple(x-1 for x in J[1:]));e=s.eye(cl)[:,col]
   norm=sum((ext(R[i],k-1)**h for h in range([0,5,4][i])),s.zeros(cl))
   b[cn:,j]=sgn[i]*norm*e
 for j,J in enumerate(low):
  if 0 not in J:
   row=list(combinations(range(5),k-1)).index(tuple(x-1 for x in J));b[cn+row,n+j]=1
 change=s.diag(ext(P[i].inv(),k),ext(P[i].inv(),k-1))
 return b*change

def fcusp(k):
 n=dim(6,k);l=dim(6,k-1);a=s.zeros(cusp_dim(k),n+l)
 if n:a[:,:n]=maps[k]*ext(S.inv(),k)
 return a

def space_dim(k):return main_dim(k)+sum(cap_dim(i,k) for i in [1,2])+cusp_dim(k)
def dspace(k):return s.diag(dmain(k),dcap(1,k),dcap(2,k),s.zeros(cusp_dim(k-1),cusp_dim(k)))
def bdry_total(k):return 3*bdry_dim(k)
def dbtotal(k):return s.diag(*[dbdry(i,k) for i in range(3)])
def F(k):
 rows=[main_dim(k),cap_dim(1,k),cap_dim(2,k),cusp_dim(k)];a=s.zeros(sum(rows),bdry_total(k));b=bdry_dim(k)
 for i in range(3):a[:rows[0],i*b:(i+1)*b]=fmain(i,k)
 a[rows[0]:rows[0]+rows[1],b:2*b]=-fcap(1,k)
 a[rows[0]+rows[1]:sum(rows[:3]),2*b:3*b]=-fcap(2,k)
 a[sum(rows[:3]):,:b]=-fcusp(k)
 return a
Diff={}
for k in range(1,10):
 ds=dspace(k);db=dbtotal(k-1);f=F(k-1)
 Diff[k]=ds.row_join(f).col_join(s.zeros(db.rows,ds.cols).row_join(-db))
 assert dspace(k)*F(k)==F(k-1)*dbtotal(k)
 if k>1:assert Diff[k-1]*Diff[k]==s.zeros(Diff[k-1].rows,Diff[k].cols)
 print('D shape',k,Diff[k].shape)
output={'warning':__doc__,'S':S.tolist(),'differentials':{str(k):v.tolist() for k,v in Diff.items()},'homology':{}}
for k in range(9):
 n=space_dim(k)+bdry_total(k-1)
 a=Diff[k] if k else s.zeros(0,n);b=Diff[k+1]
 h=homology(a,b);print('H',k,'free',h['free'],'torsion',h['torsion']);output['homology'][str(k)]=h
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2,default=int))
