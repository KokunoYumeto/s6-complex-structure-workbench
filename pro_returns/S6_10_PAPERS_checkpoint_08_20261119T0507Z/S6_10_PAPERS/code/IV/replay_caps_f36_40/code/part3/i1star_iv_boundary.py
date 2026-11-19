#!/usr/bin/env python3
"""Actual NS-derived source/exterior chain maps for OS50, (a,b)=(2,6).
No cap topology conclusion is encoded before its actual boundary maps are supplied.
"""
from pathlib import Path
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.polys.domains import ZZ
ROOT=Path(__file__).resolve().parent

def dec(M):
 D,L,R=smith_normal_decomp(DomainMatrix.from_Matrix(M).convert_to(ZZ));D,L,R=[x.to_Matrix() for x in(D,L,R)];assert D==L*M*R;return D,L,R

def hom(d,up):
 assert d*up==s.zeros(d.rows,up.cols)
 D,L,R=dec(d);rank=d.rank();K=R[:,rank:];A=(R.inv()*up)[rank:,:];assert K*A==up
 E,V,W=dec(A);r=A.rank();inds=[i for i in range(K.cols) if i>=r or abs(E[i,i])!=1]
 orders=[0 if i>=r else abs(int(E[i,i])) for i in inds]
 reps=K*V.inv()[:,inds];proj=(V*R.inv()[rank:,:])[inds,:]
 assert proj*reps==s.eye(len(inds))
 return orders,reps,proj

def imat(M):
 assert all(x.q==1 for x in M)
 return [[int(x) for x in row] for row in M.tolist()]

def cone(d,f,dims):
 wdims={k:dims.get(k,0)+dims.get(k-1,0) for k in range(7)}
 w={}
 for k in range(1,7):
  top=d.get(k,s.zeros(dims.get(k-1,0),dims.get(k,0))).row_join(f.get(k-1,s.zeros(0))-s.eye(dims.get(k-1,0)))
  bot=s.zeros(dims.get(k-2,0),dims.get(k,0)).row_join(-d.get(k-1,s.zeros(dims.get(k-2,0),dims.get(k-1,0))))
  w[k]=top.col_join(bot)
  assert w[k].shape==(wdims[k-1],wdims[k])
 for k in range(2,7):assert w[k-1]*w[k]==s.zeros(wdims[k-2],wdims[k])
 return w,wdims

B=s.zeros(10);B[0,0]=B[9,9]=-1;B[0,1]=B[1,0]=B[1,9]=B[9,1]=1
for i in range(2,9):B[i,i]=-2
for i,j in [(2,3),(2,4),(3,5),(3,6),(7,8),(9,5),(9,7)]:B[i,j]=B[j,i]=1
assert B.det()==-1
vec=lambda i:s.eye(10)[:,i]
F=vec(1);L0=F-2*vec(2)-2*vec(3)-vec(4)-vec(5)-vec(6)
Lstar=s.Matrix.hstack(L0,vec(4),vec(5),vec(6),vec(2),vec(3))
Liv=s.Matrix.hstack(F-vec(7)-vec(8),vec(7),vec(8));L=Lstar.row_join(Liv)
# Section vectors from their actual component intersections and height pairing.
D5=-B.extract(range(2,7),range(2,7));A2=-B.extract([7,8],[7,8]);invD=D5.inv();invA=A2.inv()
Dindex={0:None,1:3,2:2,3:4}
def section(k):
 di=Dindex[k%4];ai=None if k%3==0 else k%3-1
 cd=0 if di is None else invD[di,di];ca=0 if ai is None else invA[ai,ai]
 op=(s.Rational(k*k,12)-2+cd+ca)/2
 gp=1+op-s.Rational(k,12)-(0 if di is None else invD[3,di])-(0 if ai is None else invA[0,ai])
 q=s.zeros(10,1);q[0]=op;q[1]=1;q[9]=gp
 if di is not None:q[di+2]=1
 if ai is not None:q[ai+7]=1
 v=B.inv()*q;assert all(x.q==1 for x in v);assert (v.T*B*v)[0]==-1;return v
Tp=s.eye(10);Tp[:,0]=section(6);Tp[:,9]=section(7);Tp[:,4]=L0;Tp[:,5]=vec(6);Tp[:,6]=vec(5)
assert Tp.T*B*Tp==B
Pstar=s.zeros(6)
for i,j in enumerate([1,0,3,2,4,5]):Pstar[j,i]=1
Pc=s.diag(Pstar,s.eye(3));assert Tp*L==L*Pc
# Actual contracting map covers -6G.
T=Tp.inv();Pr=Pc.inv().T;G=L.T*B
assert G*T==Pr*G
pdims={0:1,1:9,2:10,3:2,4:1}
pd={1:s.zeros(1,9),2:G,3:s.zeros(10,2),4:s.ones(2,1),5:s.zeros(1,0)}
pf={0:s.eye(1),1:Pr,2:T,3:s.eye(2),4:s.eye(1)}
w,wdims=cone(pd,pf,pdims)
WH={k:hom(w[k],w[k+1]) for k in range(1,5)}
# Source inversion and reversal of the actual suspension, before any cap is filled.
Jsrc=s.eye(10);Jsrc[:,9]=section(-1);Jsrc[:,5]=vec(6);Jsrc[:,6]=vec(5);Jsrc[:,7]=vec(8);Jsrc[:,8]=vec(7)
Js=s.eye(6);Js[:,2]=s.eye(6)[:,3];Js[:,3]=s.eye(6)[:,2]
Jv=s.eye(3);Jv[:,1]=s.eye(3)[:,2];Jv[:,2]=s.eye(3)[:,1]
Jcomp=s.diag(Js,Jv)
assert Jsrc*T*Jsrc==T.inv() and Jsrc*L==L*Jcomp
JI2=s.diag(Jsrc,-Pr.inv()*Jcomp)
JI1=s.diag(Jcomp,-s.eye(1))
JI3=s.diag(s.eye(2),-T.inv()*Jsrc)
assert w[2]*JI2==JI1*w[2] and w[3]*JI3==JI2*w[3]
IH2=WH[2][2]*JI2*WH[2][1]
assert IH2[1:,1:]==-s.eye(2)
result={'NS_gram':imat(B),'component_inclusion':imat(L),'translation_plus6':imat(Tp),'translation_actual_minus6':imat(T),'exterior_homology':{str(k):WH[k][0] for k in WH},'boundaries':{},'H2_exterior_inversion':imat(IH2),'all_pass':True}
for name,Li,Pi,idx in [('star',Lstar,Pstar,0),('iv',Liv,s.eye(3),1)]:
 k=Li.cols;Bi=Li.T*B*Li
 ndims={0:1,1:k,2:k,3:1};nd={1:s.zeros(1,k),2:Bi,3:s.zeros(k,1),4:s.zeros(1,0)}
 nf={0:s.eye(1),1:Pi.inv().T,2:Pi,3:s.eye(1)}
 nw,nwdims=cone(nd,nf,ndims)
 e=s.eye(2)[:,idx];emb=s.zeros(9,k);start=0 if idx==0 else 6;emb[start:start+k,:]=s.eye(k)
 js={0:s.eye(1),1:emb,2:Li,3:e,4:s.zeros(1,0)}
 jws={j:s.diag(js.get(j,s.zeros(pdims.get(j,0),ndims.get(j,0))),js.get(j-1,s.zeros(pdims.get(j-1,0),ndims.get(j-1,0)))) for j in range(1,5)}
 for j in range(2,5):assert w[j]*jws[j]==jws[j-1]*nw[j]
 H={j:hom(nw[j],nw[j+1]) for j in range(1,5)}
 maps={j:WH[j][2]*jws[j]*H[j][1] for j in range(1,5)}
 mult=s.Matrix([1,1,1,1,2,2]) if idx==0 else s.ones(3,1)
 fib=mult.col_join(s.zeros(k,1))
 fcoords=H[2][2]*fib
 alpha=s.zeros(k+1,1);alpha[0]=1
 gamma=s.zeros(k+1,1);gamma[k]=1
 N3=s.zeros(k+1,1);N3[0]=1
 trace=s.zeros(k+1,1);trace[1:,0]=mult
 marks={'alpha_H1':imat(H[1][2]*alpha),'gamma_H1':imat(H[1][2]*gamma),'N3_H3':imat(H[3][2]*N3),'fibre_gamma_H3':imat(H[3][2]*trace),'alpha_exterior':imat(maps[1]*H[1][2]*alpha),'gamma_exterior':imat(maps[1]*H[1][2]*gamma),'N3_exterior':imat(maps[3]*H[3][2]*N3),'fibre_gamma_exterior':imat(maps[3]*H[3][2]*trace)}
 result['boundaries'][name]={'markings':marks,'intersection':imat(Bi),'homology':{str(j):H[j][0] for j in H},'maps':{str(j):imat(maps[j]) for j in maps},'H2_reps':imat(H[2][1]),'fibre_H2':imat(fcoords),'fibre_exterior':imat(maps[2]*fcoords)}
for k,v in result.items():print(k,'=',v)
(ROOT/'i1star_iv_boundary.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: actual negative-translation source and both boundary chain maps, all degrees.')
# Actual cap maps retain every unspecified free collar coefficient.
ks,kv,ns,nv,m=s.symbols('kappa_star kappa_IV n_star n_IV m',integer=True)
i2=s.Matrix(result['boundaries']['star']['maps']['2']).row_join(s.Matrix(result['boundaries']['iv']['maps']['2']))
capstar=s.Matrix([[0,1,ks,0,0,0]])
capiv=s.Matrix([[0,0,0,0,1,kv]])
D2raw=i2.col_join(-capstar).col_join(-capiv)
# Z/6 -> Z/2+Z/3, 1 -> (1,-1), is the exact CRT identification.
CRT=s.zeros(6,5);CRT[0,0]=1;CRT[3,0]=-1
for c,r in enumerate([1,2,4,5],1):CRT[r,c]=1
D2=D2raw*CRT
for c in range(D2.cols):D2[0,c]=int(D2[0,c])%6
assert D2.det() in [s.Integer(1),s.Integer(-1)]
D1=s.Matrix([[1,0,-1,0],[0,1,0,1],[ns,-2,0,0],[0,0,nv,-m]])
D3=s.Matrix([[0,1,0,1],[-1,0,1,0],[ns,-2,0,0],[0,0,nv,-m]])
D=m*ns+2*nv
assert s.expand(D1.det()**2-D**2)==0 and s.expand(D3.det()**2-D**2)==0
smat=lambda M:[[str(x) for x in row] for row in M.tolist()]
result.update(H2_raw_MV=smat(D2raw),H2_CRT=imat(CRT),H2_MV=smat(D2),H2_MV_determinant=int(D2.det()),H1_free_MV=smat(D1),H3_MV=smat(D3),seifert_determinant=str(D),H4_MV=[[1,-1]],H0_MV=[[1,1],[-1,0],[0,-1]])
(ROOT/'i1star_iv_boundary.json').write_text(json.dumps(result,indent=2)+'\n')
print('H2 MV after exact CRT=',D2.tolist(),'det=',D2.det())
print('H1 free MV=',D1.tolist(),'det=',s.factor(D1.det()))
print('H3 MV=',D3.tolist(),'det=',s.factor(D3.det()))
print('PASS: all cap-collar coefficients retained; H2 isomorphism and exact determinant m*n_star+2*n_IV.')
# Complete degree-one map before eliminating either actual torsion collar.
cs,ds,cv,dv=s.symbols('c_star d_star c_IV d_IV',integer=True)
D1full=s.Matrix([[0,1,0,0,-1,0],[0,0,1,0,0,1],[-1,-cs,-ds,0,0,0],[0,ns,-2,0,0,0],[0,0,0,-1,-cv,-dv],[0,0,0,0,nv,-m]])
result['H1_full_domain_orders']=[2,0,0,3,0,0]
result['H1_full_target_orders']=[0,0,2,0,3,0]
result['H1_full_MV_symbolic']=smat(D1full)
assert s.expand(D1full.det()**2-D**2)==0
(ROOT/'i1star_iv_boundary.json').write_text(json.dumps(result,indent=2)+'\n')
print('Complete H1 map, all torsion path coefficients retained=',D1full.tolist())
