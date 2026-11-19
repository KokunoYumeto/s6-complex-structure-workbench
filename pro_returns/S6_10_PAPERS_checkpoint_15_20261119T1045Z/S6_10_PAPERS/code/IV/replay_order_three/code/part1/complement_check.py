from pathlib import Path
import contextlib,io,json
with contextlib.redirect_stdout(io.StringIO()):
 exec(Path(__file__).with_name('global_candidate_complex.py').read_text().split('Diff={}')[0])

def yspace_dim(k):return main_dim(k)+cap_dim(1,k)+cap_dim(2,k)
def ys_d(k):return s.diag(dmain(k),dcap(1,k),dcap(2,k))
def yF(k):
 ns=yspace_dim(k);nb=bdry_dim(k);a=s.zeros(ns,2*nb)
 a[:main_dim(k),:nb]=fmain(1,k);a[:main_dim(k),nb:]=fmain(2,k)
 a[main_dim(k):main_dim(k)+cap_dim(1,k),:nb]=-fcap(1,k)
 a[main_dim(k)+cap_dim(1,k):,nb:]=-fcap(2,k)
 return a

def ydim(k):return yspace_dim(k)+2*bdry_dim(k-1)
def yd(k):
 a=ys_d(k);b=s.diag(dbdry(1,k-1),dbdry(2,k-1));f=yF(k-1)
 return a.row_join(f).col_join(s.zeros(b.rows,a.cols).row_join(-b))
def yj(k):
 a=s.zeros(ydim(k),bdry_dim(k));a[:main_dim(k),:]=fmain(0,k);return a

def hpresentation(a,b):
 d,u,v=snf(a);r=a.rank();K=v[:,r:];R=(v.inv()*b)[r:,:]
 rd,ru,rv=snf(R);rr=R.rank()
 # Retain all torsion rows together with free rows.
 keep=[i for i in range(R.rows) if i>=rr or abs(rd[i,i])>1]
 Z=K*ru.inv()[:,keep];Pi=ru[keep,:]*v.inv()[r:,:]
 rel=s.zeros(len(keep),len(keep))
 for j,i in enumerate(keep):
  if i<rr:rel[j,j]=rd[i,i]
 return Z,Pi,rel
out={}
for k in range(5):
 ya=yd(k) if k else s.zeros(0,ydim(k));yb=yd(k+1)
 ba=dbdry(0,k) if k else s.zeros(0,bdry_dim(k));bb=dbdry(0,k+1)
 yz,yp,yr=hpresentation(ya,yb);bz,bp,br=hpresentation(ba,bb)
 j=yp*yj(k)*bz
 print('degree',k,'Yrel',yr,'Brel',br,'BtoY',j,flush=True)
 coker=snf(j.row_join(yr))[0];print('coker_BtoY',coker,flush=True)
 # preimage of Y boundaries in boundary cycles: j*x=yr*y.
 mat=j.row_join(-yr);dd,uu,vv=snf(mat);ker=vv[:,mat.rank():]
 x=ker[:j.cols,:]
 susp=bz[dim(6,k):,:]*x
 print('suspension_in_kernel_BtoY',susp,flush=True)
 out[str(k)]={'Yrel':yr.tolist(),'Brel':br.tolist(),'BtoY':j.tolist(),'kernel_suspension':susp.tolist()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=int))
