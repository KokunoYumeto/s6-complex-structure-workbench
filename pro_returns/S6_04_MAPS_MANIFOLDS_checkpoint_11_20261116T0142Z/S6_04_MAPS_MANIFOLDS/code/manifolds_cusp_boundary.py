"""Integral gamma-cover cusp divisor and boundary shear audit for E2."""
from pathlib import Path
import itertools,json,sympy as s
from manifolds_rankone_families import decomp,ikernel
h=s.symbols('h');C=s.Matrix([-1,1,0,0])
curves=[s.Matrix(x) for x in [[0,1,0,0],[1,-1,-1,0],[0,0,1,0],
                             [1,0,-1,-1],[0,0,0,1],[1,-1,0,-1]]]
assert curves[1]+curves[2]==curves[4]+curves[5]==-C
assert -sum((curves[j] for j in [1,2,4,5]),s.zeros(4,1))==2*C
B=s.Matrix([[-1,-1,-1,-1],[1,1,1,h],[-h,-h,-1,-h]])
assert B*C==s.zeros(3,1)
assert s.expand(2-h-h**-1+h**-1*(h-1)**2)==0
# Integral Gysin basis for Nil3 times S1: d w=u theta, other degree-one
# generators closed. The Euler coefficient is a unit, so these cohomology
# groups and displayed integral bases follow from the integral Gysin sequence.
bases=[list(itertools.combinations(range(4),k)) for k in range(5)]
def wedge(v):
 if len(set(v))<len(v):return None,0
 return tuple(sorted(v)),(-1)**sum(v[i]>v[j] for i in range(len(v)) for j in range(i+1,len(v)))
d=[]
for k in range(5):
 D=s.zeros(len(bases[k+1]) if k<4 else 0,len(bases[k]))
 if k<4:
  for j,b in enumerate(bases[k]):
   for i,g in enumerate(b):
    if g==1:
     w,sg=wedge(b[:i]+(0,2)+b[i+1:])
     if sg:D[bases[k+1].index(w),j]+=(-1)**i*sg
 d.append(D)
A=s.eye(4);A[2,3]=1
T=[]
for k in range(5):
 T.append(s.Matrix([[A.extract(ii,jj).det() for jj in bases[k]] for ii in bases[k]]))
for k in range(4):assert d[k]*T[k]==T[k+1]*d[k]
coh=[]
for k in range(5):
 Z=ikernel(d[k]);D,U,V,r=decomp(Z);assert all(abs(D[i,i])==1 for i in range(r))
 Zi=(Z.T*Z).inv()*Z.T
 I=s.zeros(Z.cols,0) if k==0 else Zi*d[k-1]
 assert all(x.q==1 for x in I)
 Di,Ui,Vi,ri=decomp(I);assert all(abs(Di[j,j])==1 for j in range(ri))
 G=(Ui*Zi*T[k]*Z*Ui.inv())[ri:,ri:]
 assert all(x.q==1 for x in G)
 N=G-s.eye(G.rows)
 Ds,_,_,rs=decomp(N)
 assert all(abs(Ds[j,j])==1 for j in range(rs))
 assert N*N==s.zeros(G.rows)
 coh.append(dict(degree=k,rank=G.rows,shear_rank=rs,matrix=G.tolist()))
assert [x['rank'] for x in coh]==[1,3,4,3,1]
assert [x['shear_rank'] for x in coh]==[0,1,0,1,0]
record=dict(scope=__doc__,divisor_coefficient='2-h-h^-1 = -h^-1(h-1)^2',
            cohomology_shear=coh,
            homology_modules={'H0':'A/(h-1)','H1':'A/(h-1)^2 + A/(h-1)',
             'H2':'(A/(h-1))^4','H3':'A/(h-1)^2 + A/(h-1)','H4':'A/(h-1)'},
            convention='On forms delta -> delta+theta; on loops theta -> theta+delta.')
print(json.dumps(record,indent=2,default=int));Path(__file__).with_suffix('.out.json').write_text(json.dumps(record,indent=2,default=int)+'\n')
