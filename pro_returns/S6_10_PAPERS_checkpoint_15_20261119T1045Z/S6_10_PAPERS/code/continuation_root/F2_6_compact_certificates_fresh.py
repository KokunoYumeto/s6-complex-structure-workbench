"""Compact integral certificates from the same newly authored local models."""
from pathlib import Path
import contextlib,io,json,random,math
with contextlib.redirect_stdout(io.StringIO()):
 import F2_6_integral_sheaf_fresh as f
Z,eye,zero,sub,rows,ext,hc,vc=f.Z,f.eye,f.zero,f.sub,f.rows,f.ext,f.hc,f.vc
comb=f.combinations
def basisvec(k,terms):
 ii=list(comb(range(6),k));return Z([[sum(c for J,c in terms if tuple(J)==I)] for I in ii])
def normal_cusp(k):
 if k==1:return hc(*[basisvec(1,[((i,),1)]) for i in (3,4,5)])
 if k==2:
  vv=[basisvec(2,[(J,1)]) for J in comb((3,4,5),2)]
  vv += [basisvec(2,[((i,i+3),1)]) for i in range(3)]
  vv += [basisvec(2,[((i,j+3),1),((j,i+3),1)]) for i,j in comb(range(3),2)]
  return hc(*vv)
 if k==3:
  vv=[basisvec(3,[((3,4,5),1)])]
  vv += [basisvec(3,[((i,j+3,k+3),1)]) for j,k in comb(range(3),2) for i in (j,k)]
  vv += [basisvec(3,[((0,4,5),1),((1,3,5),1)]),basisvec(3,[((0,4,5),1),((2,3,4),-1)])]
  return hc(*vv)
 J=Z([[int(i<3 and j==i+3)-int(i>=3 and j==i-3) for j in range(6)] for i in range(6)])
 H=zero(15,15);two=list(comb(range(6),2));four=list(comb(range(6),4))
 for a,I in enumerate(two):
  Ic=tuple(j for j in range(6) if j not in I);per=I+Ic;sgn=(-1)**sum(per[i]>per[j] for i in range(6) for j in range(i+1,6));H[four.index(Ic),a]=sgn
 return H*ext(J,2)*normal_cusp(2)
def orbit_basis(T,m,norm=False):
 unused=set(range(T.nrows()));vv=[]
 while unused:
  j=min(unused);i=j;sgn=1;v=zero(T.nrows(),1);L=0
  while True:
   unused.discard(i);v[i,0]=sgn;L+=1
   loc=[r for r in range(T.nrows()) if T[r,i]];assert len(loc)==1
   sgn*=int(T[loc[0],i]);i=loc[0]
   if i==j:break
  if sgn==1:vv.append((m//L)*v if norm else v)
 return hc(*vv) if vv else zero(T.nrows(),0)
def left_mod2(C):
 # Nullspace of transpose by independent binary elimination.
 a=[[int(C[j,i])%2 for j in range(C.nrows())] for i in range(C.ncols())];r=0;piv=[]
 for c in range(C.nrows()):
  z=next((i for i in range(r,len(a)) if a[i][c]),None)
  if z is None:continue
  a[r],a[z]=a[z],a[r]
  for i in range(len(a)):
   if i!=r and a[i][c]:a[i]=[x^y for x,y in zip(a[i],a[r])]
  piv.append(c);r+=1
 free=[i for i in range(C.nrows()) if i not in piv];assert len(free)==1
 x=[0]*C.nrows();x[free[0]]=1
 for i,c in reversed(list(enumerate(piv))):x[c]=sum(a[i][j]*x[j] for j in free)%2
 assert all(sum(x[i]*int(C[i,j]) for i in range(C.nrows()))%2==0 for j in range(C.ncols()))
 return x
out={'scope':'All matrices and calculations precede target proof exposure. Indices are zero based.','degrees':{}}
for q in range(1,5):
 A,B=ext(f.A1,q),ext(f.A2,q);n=A.nrows();I=eye(n);Delta=hc(A-I,B-I)
 J=[]
 for g in f.finite:
  invq=orbit_basis(ext(g['D'].transpose(),q),g['m'])
  normprev=orbit_basis(ext(g['D'].transpose(),q-1),g['m'],True)
  Ji=ext(g['Q'],q)*hc(f.embed_vertical(q)*invq,f.embed_horizontal(q)*normprev)
  assert (A if g['i']==1 else B)*Ji==Ji;J.append(Ji)
 J0=ext(f.inv(f.S).transpose(),q)*normal_cusp(q)
 assert (ext(f.M0.transpose(),q)-I)*J0==zero(n,J0.ncols())
 assert f.snf(J0)['torsion']==[]
 assert J0.ncols()==f.kernel(ext(f.M0.transpose(),q)-I)[0].ncols()
 d0=vc(hc(J[0],zero(n,J[1].ncols()),-J0),hc(zero(n,J[0].ncols()),J[1],-A*J0))
 assert Delta*d0==zero(n,d0.ncols())
 chosen=None
 for attempt in range(1000):
  order=list(range(2*n));random.Random(attempt).shuffle(order);P=[]
  for j in order:
   if sub(Delta,range(n),P+[j]).rank()>len(P):P.append(j)
   if len(P)==n:break
  P.sort();C=sub(Delta,range(n),P)
  if abs(C.det())==2:chosen=(P,C);break
 assert chosen is not None
 P,C=chosen;F=[i for i in range(2*n) if i not in P]
 CP=C.inv()*sub(Delta,range(n),F);assert all(CP[i,j]==int(CP[i,j]) for i in range(n) for j in range(n))
 R=sub(d0,F,range(d0.ncols()));rank=R.rank();mins=[];gcd=0
 if q==1:
  for js in comb(range(R.ncols()),rank):
   det=int(sub(R,range(rank),js).det())
   if det:
    mins.append({'rows':list(range(rank)),'columns':list(js),'determinant':det});gcd=math.gcd(gcd,det)
   if gcd==1:break
 else:
  # Here all columns are independent; q3 needs a primitive row minor.
  assert rank==R.ncols()
  for rs in comb(range(R.nrows()),rank):
   det=int(sub(R,rs,range(rank)).det())
   if det:
    mins.append({'rows':list(rs),'columns':list(range(rank)),'determinant':det});gcd=math.gcd(gcd,det)
   if gcd==1:break
 assert gcd==1
 rho=left_mod2(C)
 d={'dimension':n,'Delta_pivot_columns':P,'Delta_pivot_determinant':int(C.det()),'kernel_free_rows':F,'d0_columns':[j.ncols() for j in J]+[J0.ncols()],'H1_relation_rank':rank,'H1_torsionfree_minor_certificates':mins,'H1_free':n-rank,'global_mod2_covector':rho,'J1':rows(J[0]),'J2':rows(J[1]),'J0':rows(J0),'R':rows(R)}
 if q<=3:
  w=Z(f.out['transgression'][str(q+1)]['w_original_basis']);x=C.inv()*(2*w)
  assert all(x[i,0]==int(x[i,0]) for i in range(n));assert C*Z(rows(x))==2*w
  assert sum(rho[i]*int(w[i,0]) for i in range(n))%2==1
  d['torsion_w']=rows(w);d['twice_w_pivot_coordinates']=rows(x);d['rho_w_mod2']=1
 out['degrees'][str(q)]=d
out['status']='passed'
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'passed','degrees':{q:{k:d[k] for k in ['Delta_pivot_columns','Delta_pivot_determinant','H1_relation_rank','H1_torsionfree_minor_certificates','H1_free','global_mod2_covector']} for q,d in out['degrees'].items()}},indent=2))
