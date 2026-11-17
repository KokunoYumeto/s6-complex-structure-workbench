#!/usr/bin/env python3
"""Exact integral MV/specialization calculation for OS49 plus one order-two cap."""
from itertools import combinations
from pathlib import Path
import sympy as s,json
from sympy.matrices.normalforms import smith_normal_form,hermite_normal_form
ROOT=Path(__file__).resolve().parents[2]
checks=[]
def ck(n,v):
 assert bool(v),n;checks.append(n)
def data(a): return [[str(v) if not v.is_Integer else int(v) for v in a.row(i)] for i in range(a.rows)]
def snf(a):
 d=smith_normal_form(a,domain=s.ZZ);return [abs(int(d[i,i])) for i in range(min(d.shape)) if d[i,i]]
def wedge(a,q):
 ix=list(combinations(range(a.rows),q));return s.Matrix([[a.extract(i,j).det() for j in ix] for i in ix])
def contract(v,q):
 src=list(combinations(range(4),q));dst=list(combinations(range(4),q-1));a=s.zeros(len(dst),len(src))
 for j,ix in enumerate(src):
  for k,b in enumerate(ix):a[dst.index(ix[:k]+ix[k+1:]),j]+=(-1)**k*v[b]
 return a
T=[s.Matrix(a) for a in [
[[1,-3,-3,-1],[0,-2,-3,-1],[0,1,1,0],[0,0,0,1]],
[[1,0,0,0],[0,1,1,0],[0,-1,0,0],[0,0,0,1]],
[[1,0,3,1],[0,1,2,1],[0,0,1,0],[0,0,0,1]]]]
H=[a.inv().T for a in T];ell=s.Matrix([1,-1,0,0]);gamma=s.Matrix([1,0,0,0])
ck('actual tuple product',T[0]*T[1]*T[2]==s.eye(4));ck('root order three',H[0]**3==s.eye(4));ck('actual invariant norm',H[0]*ell==ell)
inv={0:s.Matrix([1]),1:s.Matrix([1,0,0,0]),2:s.Matrix([0,0,3,1,0,0]),3:s.Matrix([1,0,0,0]),4:s.Matrix([1])}
coinv={0:s.Matrix([[1]]),1:s.Matrix([[0,0,0,1]]),2:s.Matrix([[0,0,1,3,0,0]]),3:s.Matrix([[0,0,0,1]]),4:s.Matrix([[1]])}
sp={0:1,1:6,2:2,3:2,4:6}
R1=s.diag(2,1,1,1);records={}
for q in range(5):
 W=[wedge(a,q) for a in T];N=W[0].rows;D=[a-s.eye(N) for a in W]
 imgs=[hermite_normal_form(a) for a in D]
 d0=s.Matrix.vstack(*[b.gauss_jordan_solve(a)[0] if b.cols else s.zeros(0,N) for a,b in zip(D,imgs)])
 acc=s.eye(N);blocks=[]
 for a,b in zip(W,imgs):blocks.append(acc*b);acc=acc*a
 d1=s.Matrix.hstack(*blocks);rel=s.Matrix.hstack(*D)
 ck(f'parabolic differential q{q}',d1*d0==s.zeros(N,N))
 ck(f'parabolic ranks q{q}',sum(b.cols for b in imgs)==d0.rank()+d1.rank())
 ck(f'primitive parabolic image q{q}',snf(d0)==[1]*(N-1))
 ck(f'primitive coinvariants q{q}',snf(rel)==[1]*(N-1))
 ck(f'global invariant q{q}',s.Matrix.vstack(*D)*inv[q]==s.zeros(3*N,1))
 ck(f'coinvariant projection q{q}',coinv[q]*rel==s.zeros(1,3*N))
 Rs=wedge(R1,q);ix=list(combinations(range(4),q));bad=[i for i,J in enumerate(ix) if 0 in J]
 Qs=s.zeros(len(bad),N)
 for row,i in enumerate(bad):Qs[row,i]=1
 # Root order-three quotient is Z/3 in degrees 1 and 4, zero otherwise.
 old=1 if q in [1,4] else 0
 Q=s.zeros(old+len(bad),N)
 if old:Q[0,0]=1
 if bad:Q[old:,:]=Qs
 order=s.diag(*(([3] if old else [])+[2]*len(bad))) if old+len(bad) else s.zeros(0,0)
 b=Q*inv[q];P=order.row_join(b)
 expected=[] if q==0 else ([1,1] if q in [1,4] else [1,2,2])
 ck(f'local MV skyscraper Smith q{q}',snf(P)==expected)
 # The displayed primitive global specialization lattice is the full kernel.
 for z0 in range(1,sp[q]):ck(f'minimum global index q{q} candidate{z0}',any(int(z0*b[i])%int(order[i,i]) for i in range(order.rows)))
 ck(f'global index q{q}',all(int(sp[q]*b[i])%int(order[i,i])==0 for i in range(order.rows)))
 r={'wedge_monodromies':[data(a) for a in W],'image_bases':[data(a) for a in imgs],'parabolic_d0':data(d0),'parabolic_d1':data(d1),'parabolic_H1':0,'coinvariant_projection':data(coinv[q]),'global_invariant':data(inv[q]),'smooth_cap_pullback':data(Rs),'smooth_quotient_projection':data(Qs),'combined_quotient_projection':data(Q),'combined_quotient_relations':data(order),'global_to_quotient':data(b),'MV_presentation':data(P),'MV_smith':snf(P),'global_specialization_index':sp[q],'H1_sheaf':'(Z/2)^2' if q in [2,3] else '0'}
 if q:
  ca=contract(ell,q);cs=contract(gamma,q);prism=-s.Rational(1,3)*ca+s.Rational(1,2)*cs
  out=(coinv[q-1]*prism*(sp[q]*inv[q]))[0];ck(f'actual two-cap d2 q{q}',out==1)
  r.update({'star_actual_contraction':data(ca),'smooth_actual_contraction':data(cs),'rational_prism_sum':data(prism),'d2_on_primitive_generator':int(out)})
 records[q]=r
K=hermite_normal_form(s.Matrix.hstack(H[1]-s.eye(4),H[2]-s.eye(4)))
ck('nonfinite relation lattice primitive',snf(K)==[1,1,1]);qA=K.gauss_jordan_solve(H[0]-s.eye(4))[0];ck('finite linear relations already retained',all(x.q==1 for x in qA))
Dpi=s.zeros(6,11);Dpi[:4,:8]=s.Matrix.hstack(H[1]-s.eye(4),H[2]-s.eye(4));Dpi[:4,8]=ell;Dpi[4,8]=3;Dpi[:4,9]=-gamma;Dpi[5,9]=2;Dpi[4,10]=1;Dpi[5,10]=1
ck('full van Kampen abelian relation Smith',snf(Dpi)==[1]*6)
S=s.Matrix([[1,3,0],[-1,0,2],[0,1,1]])
ck('surviving Seifert determinant',S.det()==1)
general=[]
for r,v in [(2,[1,0,0,0]),(3,[0,2,3,5]),(4,[2,3,0,2]),
            (6,[2,3,5,0]),(8,[0,3,2,6]),(9,[2,2,2,2]),
            (10,[5,2,4,6]),(15,[3,5,2,0])]:
 v=s.Matrix(v);G=hermite_normal_form((r*s.eye(4)).row_join(v))
 pull=r*G.inv().T;pull2=wedge(pull,2)
 ck(f'full root lattice pullback integral r{r}',all(z.q==1 for z in pull))
 ck(f'exact effective root degree r{r}',G.det()==r**3 and pull.det()==r)
 ck(f'first root restriction Smith r{r}',snf(pull)==[1,1,1,r])
 ck(f'second root restriction Smith r{r}',snf(pull2)==[1,1,1,r,r,r])
 P=pull2.row_join(inv[2]);sd=snf(P);dims={}
 for p in s.factorint(r):
  dims[str(p)]=sum(d%p==0 for d in sd)
  ck(f'one global invariant leaves two generators r{r} p{p}',dims[str(p)]>=2)
 general.append({'order':r,'norm_vector':data(v),'enlarged_lattice_numerator':data(G),
  'full_H1_pullback':data(pull),'full_H2_pullback':data(pull2),
  'H2_Smith':snf(pull2),'global_MV_presentation':data(P),'global_MV_Smith':sd,
  'remaining_mod_p_dimensions':dims})
# Exact finite averaging retains the constant lattice/finite-character term.
for r in [2,3,4,6]:
 ff=list(s.symbols('f0:'+str(r)))
 gg=sum(j*ff[j] for j in range(r))/r
 gd=sum(j*ff[(j+1)%r] for j in range(r))/r
 ck(f'full cyclic averaging identity r{r}',s.expand(gd-gg-ff[0]+sum(ff)/r)==0)
q,z0,X,Y,x,y=s.symbols('q z0 X Y x y')
old=y*y-x**3+3*(1+q)**3*q*x-(1+q)**4*q*(1+2*q)
new=Y*Y-X**3+3*(1+z0**6)**3*z0**2*X-(1+z0**6)**4*(1+2*z0**6)
ck('actual good-II root equation',s.expand(old.subs({q:z0**6,x:z0**2*X,y:z0**3*Y})/z0**6-new)==0)
xg=(1+z0**6)**2/z0**2;yg=(1+z0**6)**2/z0**3
ck('actual marked G on good-II root',s.factor(new.subs({X:xg,Y:yg}))==0)
ck('exact formal parameter of G',s.cancel(-xg/yg+z0)==0)
ii=s.Matrix([[1,1],[-1,0]])
ck('central II deck exact order six',ii**6==s.eye(2) and ii**3==-s.eye(2))
ck('II deck fixed lattice determinant',int((ii-s.eye(2)).det())==1)
kk,ll,nn,ns=s.symbols('kk ll nn ns',integer=True)
seif=s.Matrix([[3*kk,0,-ns],[0,6*ll,-nn],[1,1,0]])
mod3=s.Matrix([[1,-1,0]])
ck('literal shared-three fundamental quotient',all(s.expand(v).subs({kk:0,ll:0})==0 for v in mod3*seif.T))
out={'status':'PASS','checks':len(checks),'names':checks,'data':{'star':[3,-1,0],'smooth_order':2,'smooth_norm_vector':data(gamma)},'degrees':records,'full_fundamental_relation_matrix':data(Dpi),'full_fundamental_smith':snf(Dpi),'finite_relation_preimage':data(qA),'Seifert_relation_matrix':data(S),'Seifert_determinant':int(S.det()),'integral_cohomology':{'H0':'Z','H1':'0','H2':'0','H3':'(Z/2)^2','H4':'(Z/2)^2','H5':'0','H6':'Z'},'integral_homology':{'H0':'Z','H1':'0','H2':'(Z/2)^2','H3':'(Z/2)^2','H4':'0','H5':'0','H6':'Z'},'scope':'Actual torus specialization and Cech/Mayer-Vietoris maps; the geometric local-cap and prism comparisons are written in the accompanying working proof.'}
out['general_effective_smooth_caps']=general
out['good_II_root']={'root_order':'6l','formal_parameter_G':'-z^l',
 'central_elliptic_deck':data(ii),'psi_norm':'n',
 'shared_three_relations':data(seif),'explicit_Z3_character':data(mod3)}
(ROOT/'code/part3/os49_order_two_cap.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',len(checks),'exact integral specialization, MV, primitive-index, prism and van Kampen checks.')
print('pi1=0; H2=H3=(Z/2)^2; other reduced homology vanishes except H6=Z.')
