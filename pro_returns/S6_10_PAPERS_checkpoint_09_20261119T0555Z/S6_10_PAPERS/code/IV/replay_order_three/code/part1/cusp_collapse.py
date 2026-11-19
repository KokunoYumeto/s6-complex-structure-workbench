"""Integral graded collapse maps from T^3 x T^3 to the Kuhn orbit model."""
from pathlib import Path
import contextlib,io,json
with contextlib.redirect_stdout(io.StringIO()):
 exec(Path(__file__).with_name('cusp_complex.py').read_text().replace("Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2,default=int))",''))

def presentation(a,b):
 d,u,v=snf(a);r=a.rank();K=v[:,r:];R=(v.inv()*b)[r:,:]
 rd,ru,rv=snf(R);rr=R.rank()
 assert all(abs(rd[i,i])==1 for i in range(rr))
 # Coords in homology are ru*(Kcoords) after quotienting first rr rows.
 # basis cycles lift free standard coordinates through ru^-1 and K.
 Z=K*ru.inv()[:,rr:]
 Pi=ru[rr:,:]*v.inv()[r:,:]
 assert Pi*Z==s.eye(Z.cols)
 return Z,Pi

result=[]
for q in range(4):
 srcD={p:s.kronecker_product(D[p,0],s.eye(s.binomial(3,q))) for p in range(3)}
 P={}
 for p in range(4):
  blocks=[wedge(Q[p,i],q) for i in range(len(cells[p]))]
  P[p]=s.diag(*blocks)
 for p in range(3):assert D[p,q]*P[p]==P[p+1]*srcD[p]
 for p in range(4):
  ns=len(cells[p])*s.binomial(3,q);nt=len(cells[p])*s.binomial(3-p,q)
  sa=srcD[p] if p<3 else s.zeros(0,ns);sb=srcD[p-1] if p else s.zeros(ns,0)
  ta=D[p,q] if p<3 else s.zeros(0,nt);tb=D[p-1,q] if p else s.zeros(nt,0)
  sz,spi=presentation(sa,sb);tz,tpi=presentation(ta,tb)
  H=tpi*P[p]*sz;hd,hu,hv=snf(H)
  cok=[abs(int(hd[i,i])) for i in range(min(hd.shape)) if abs(hd[i,i])>1]
  row={'p':p,'q':q,'degree':3-p+q,'source_rank':sz.cols,'target_rank':tz.cols,'map':H.tolist(),'rank':H.rank(),'cokernel_free':H.rows-H.rank(),'cokernel_torsion':cok}
  result.append(row);print(row)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2,default=int))
