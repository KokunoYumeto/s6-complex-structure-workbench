#!/usr/bin/env python3
"""Fresh post-proof exact checks for K116 and its literal K10 topology input.
This is not prereading evidence. No historical programs are imported.
"""
from pathlib import Path
import json,itertools,math,time
import sympy as s
from sympy.matrices.normalforms import smith_normal_form,hermite_normal_form
from sympy.polys.domains import ZZ
from sympy.combinatorics.fp_groups import free_group,FpGroup,coset_enumeration_r
OUT=Path(__file__).resolve().parents[1]/'output';start=time.monotonic();checks=[]
def ck(name,truth):assert truth,name;checks.append(name)
def sm(M):
 D=smith_normal_form(M,domain=ZZ)
 return [abs(int(D[i,i]))for i in range(min(D.shape))if D[i,i]]
def mat(M):return [[str(M[i,j])for j in range(M.cols)]for i in range(M.rows)]
# Literal rational source and inverse, including the factor sqrt(3).
AA,BB,a,t,b,p,g=s.symbols('AA BB a t b p g',nonzero=True)
v0=3*(AA*BB-a);tt=(BB-AA)/2+b/(2*v0);xx=tt**2+a+v0;YY=v0*(AA+BB)/2
R=t*t+a;ff=R**2+b*t;gg=R**3+s.Rational(3,2)*b*t*R+s.Rational(3,8)*b*b
ck('full rational source substitution',s.cancel(3*YY**2-xx**3+3*ff.subs(t,tt)*xx-2*gg.subs(t,tt))==0)
ck('rational inverse A',s.cancel(YY/v0-tt+b/(2*v0)-AA)==0)
ck('rational inverse B',s.cancel(YY/v0+tt-b/(2*v0)-BB)==0)
# Actual translation slope /sqrt(3) and inverse on this full source chart.
L=s.cancel((YY+b/2)/(xx-(tt*tt+a)));xT=s.cancel(3*L*L-xx-(tt*tt+a));YT=s.cancel(L*(xx-xT)-YY)
Li=s.cancel((YT-b/2)/(xT-(tt*tt+a)))
ck('translation inverse slope',s.cancel(Li+L)==0)
ck('translation inverse x',s.cancel(3*Li*Li-xT-(tt*tt+a)-xx)==0)
ck('translation inverse y',s.cancel(Li*(xT-xx)-YT-YY)==0)
# Chronological cusp tangent quotients (derive, do not insert closed f_m).
x=p**-2;y=p**-3
fprev=s.Integer(1);fm={}
for j in [1,2,4]:
 xj=(j*g)**-2;yj=(j*g)**-3;slope=s.Rational(3,2)/(j*g)
 tangent=y-yj-slope*(x-xj);den=x-(2*j*g)**-2
 fprev=s.cancel(fprev*fprev*tangent/den);fm[2*j]=fprev
 expected=-(2*j)/g**(2*j-1)*(p-g)**(2*j)/((p-2*j*g)*p**(2*j-1))
 ck('chronological cusp f'+str(2*j),s.cancel(fprev-expected)==0)
coef=s.cancel(fm[2]**8*fm[8].subs(p,p-g)/fm[8]);rr=(p-8*g)/p
ck('full cusp point coefficient',s.cancel(coef-256/g**8*(p-g)*(p-8*g)/(p*(p-9*g)))==0)
ck('actual finite point/O frame ratio',s.cancel(coef*rr.subs(p,p-g)/rr-256/g**8)==0)
ck('cusp local-ring coefficient',s.cancel(coef-256/g**8*(1-73*g*g*x+72*g**3*y)/(1-81*g*g*x))==0)
# Three exact original doublings; no nodal approximation in the computation.
f=ff.subs(b,1);Gx=R;GY=s.Rational(1,2)
for k in range(3):
 slope=s.cancel((Gx**2-f)/(2*GY));nx=s.cancel(3*slope*slope-2*Gx);ny=s.cancel(slope*(Gx-nx)-GY);Gx,GY=nx,ny
num,den=map(lambda z:s.Poly(z,t),s.fraction(Gx));xlim=s.cancel(num.LC()/den.LC());ck('x8 leading degree2',num.degree()-den.degree()==2)
numy,deny=map(lambda z:s.Poly(z,t),s.fraction(GY));ylim=s.cancel(numy.LC()/deny.LC());ck('y8 leading degree3',numy.degree()-deny.degree()==3)
ck('full doubling infinity x8',s.cancel(xlim-(81*a**6-90*a**3+1)/(9*a**3+1)**2)==0)
ck('full doubling infinity y8',s.cancel(ylim-108*a**3*(9*a**3-1)/(9*a**3+1)**3)==0)
num1,den1=s.fraction(s.cancel(Gx.subs(a,1)));expected=(6*t+1)**2*(360*t*t+282*t+199)**2
ck('K10 denominator up to constant',s.cancel(den1/expected).is_number)
ck('K10 denominator squarefree after removing squares',s.degree(s.sqf_part(den1),t)==3)
D=48*(t*t+1)**2+8*t**3+72*t+9
ck('K10 section intersections ordinary',s.gcd(den1,D)==1 and s.gcd(num1,den1)==1)
# Actual surface Gram and directed Hom.
C=s.diag(*([2]*7))
for i in range(6):C[i,i+1]=C[i+1,i]=-1
ck('A7 determinant8',C.det()==8);ck('component3 correction15/8',C.inv()[2,2]==s.Rational(15,8))
Gram=s.zeros(10);Gram[0,0]=Gram[9,9]=-1;Gram[0,1]=Gram[1,0]=Gram[9,1]=Gram[1,9]=1
Gram[2:9,2:9]=-C;Gram[9,4]=Gram[4,9]=1
ck('actual ten-class source Gram unimodular',Gram.det()==-1)
inter={}
for n in [1,7,8,9]:
 k=3*n%8;inter[n]=s.cancel((s.Rational(n*n,8)-2+s.Rational(k*(8-k),8))/2)
ck('section intersections 0,3,3,5',[inter[n]for n in [1,7,8,9]]==[0,3,3,5])
ck('both directed Hom degrees1',inter[9]-inter[1]-inter[8]-1==1 and inter[8]+1-inter[7]+inter[1]==1)
cycle=s.diag(*([-2]*8))
for i in range(8):cycle[i,(i+1)%8]=cycle[(i+1)%8,i]=1
ck('whole I8 kernel primitive',cycle.rank()==7 and cycle*s.ones(8,1)==s.zeros(8,1))
word=s.Matrix([[-1,3],[-3,8]]);ck('primitive period determinant',word.det()==1);ck('primitive valuations',s.Matrix([[8,-3]])*word==s.Matrix([[1,0]]));ck('period inverse',word.inv()==s.Matrix([[8,-3],[3,-1]]))
# The literal K10 Jacobi cocycle is determined algebraically, not by a search.
r,j,h=s.symbols('r j h');Es=[s.Matrix([[1,8],[0,1]]),s.Matrix([[1,1],[0,1]]),s.Matrix([[4,9],[-1,-2]]),s.Matrix([[1,0],[-1,1]]),s.Matrix([[-2,9],[-1,4]])]
def jac(E,k,z):
 a,b,c,d=list(E);jj,hh=k
 return s.Matrix([[1,c*jj-a*hh,d*jj-b*hh,z],[0,a,b,8*jj],[0,c,d,8*hh],[0,0,0,1]])
Ts=[jac(Es[0],[3,0],9),jac(Es[1],[r,0],8*r*r),jac(Es[2],[-3*j,j],8*j*j),jac(Es[3],[0,h],8*h*h),jac(Es[4],[0,0],-1)]
prod=s.eye(4)
for T in Ts:prod*=T
ck('global lift linear equations',s.simplify(prod[0,1]-(2*h-j))==0 and s.simplify(prod[0,2]-(-9*h+6*j+r+3))==0)
ck('unique integral central root',s.expand(prod[0,3].subs({j:2*h,r:-3*h-3})-16*(h+1)*(4*h+5))==0)
Ts=[T.subs({h:-1,j:-2,r:0})for T in Ts];prod=s.eye(4)
for T in Ts:prod*=T
ck('literal five matrices productI',prod==s.eye(4))
# Twelve-coset PSL2 covering from a full Todd-Coxeter run.
FG,ss,rr=free_group('s,r');PSL=FpGroup(FG,[ss**2,rr**3]);tw=ss*rr
sub=[tw**9,tw**-3*ss*tw*ss*tw**3,ss*tw*ss,tw**3*ss*tw*ss*tw**-3]
ct=coset_enumeration_r(PSL,sub,max_cosets=1000);ct.compress();ct.standardize();ck('modular index12',ct.n==12)
def perm(word):
 out=[]
 for k in range(ct.n):
  for gen,exp in word.array_form:
   col=0 if str(gen)=='s' else 2
   if exp<0:col+=1
   for _ in range(abs(exp)):k=ct.table[k][col]
  out.append(k)
 return out
def cycle_lengths(p):
 unseen=set(range(len(p)));lens=[]
 while unseen:
  a=next(iter(unseen));k=a;n=0
  while k in unseen:unseen.remove(k);n+=1;k=p[k]
  lens.append(n)
 return sorted(lens)
ck('modular source branch profiles',cycle_lengths(perm(ss))==[2]*6 and cycle_lengths(perm(rr))==[3]*4 and cycle_lengths(perm(tw))==[1,1,1,9])
# Reconstruct all parabolic chain matrices, integral kernels and coinvariants.
def wedge(T,q):
 inds=list(itertools.combinations(range(4),q))
 return s.Matrix([[T.extract(I,J).det()for J in inds]for I in inds])
inv={0:s.Matrix([1]),1:s.Matrix([1,0,0,0]),2:s.Matrix([0,0,1,8,0,0]),3:s.Matrix([1,0,0,0]),4:s.Matrix([1])}
coinv={0:s.Matrix([[1]]),1:s.Matrix([[0,0,0,1]]),2:s.Matrix([[0,0,8,1,0,0]]),3:s.Matrix([[0,0,0,1]]),4:s.Matrix([[1]])}
chains={}
for chosen in range(1,5):
 mats=[m.copy()for m in Ts]
 if chosen!=4:mats[4][0,3]+=1;mats[chosen][0,3]-=1
 pp=s.eye(4)
 for m in mats:pp*=m
 ck('all four zero choices product '+str(chosen),pp==s.eye(4))
 rel=s.Matrix.hstack(*[m.inv().T-s.eye(4)for m in mats]);ck('primitive van Kampen quotient '+str(chosen),sm(rel)==[1,1,1]and rel[0,:]==s.zeros(1,rel.cols))
 ck('actual positive-norm-one cap kills pi1 '+str(chosen),sm(rel.row_join(s.Matrix([1,0,0,0])))==[1,1,1,1])
 for q in range(5):
  Ws=[wedge(m,q)for m in mats];n=Ws[0].rows;Ls=[hermite_normal_form(W-s.eye(n))for W in Ws]
  blocks=[]
  for W,LL in zip(Ws,Ls):
   co=LL.gauss_jordan_solve(W-s.eye(n))[0]if LL.cols else s.zeros(0,n)
   ck('integer HNF coordinates '+str((chosen,q,len(blocks))),all(v.q==1 for v in co));blocks.append(co)
  d0=s.Matrix.vstack(*blocks);pre=s.eye(n);db=[]
  for W,LL in zip(Ws,Ls):db.append(pre*LL);pre=pre*W
  d1=s.Matrix.hstack(*db)
  ck('parabolic chain zero '+str((chosen,q)),d1*d0==s.zeros(n))
  ranks=[d0.rank(),d1.rank()];m=sum(L.cols for L in Ls)
  ck('zero middle and rank-one ends '+str((chosen,q)),sum(ranks)==m and n-ranks[0]==1 and n-ranks[1]==1)
  ck('primitive parabolic differentials '+str((chosen,q)),sm(d0)==[1]*ranks[0]and sm(d1)==[1]*ranks[1])
  ck('specified invariant generator '+str((chosen,q)),d0*inv[q]==s.zeros(m,1))
  ck('specified coinvariant functional '+str((chosen,q)),coinv[q]*d1==s.zeros(1,m) and math.gcd(*[int(z)for z in coinv[q]])==1)
  chains[str((chosen,q))]={'d0':mat(d0),'d1':mat(d1),'ranks':ranks,'smith_d0':sm(d0),'smith_d1':sm(d1),'local_lattice_ranks':[L.cols for L in Ls]}
# Full contraction with an arbitrary cap vector, retaining all source coordinates.
gamma=s.symbols('g0:4')
for q in range(1,5):
 oldinds=list(itertools.combinations(range(4),q));newinds=list(itertools.combinations(range(4),q-1));ans=s.zeros(len(newinds),1)
 for k,inds in enumerate(oldinds):
  for i,jj in enumerate(inds):ans[newinds.index(inds[:i]+inds[i+1:])]+=(-1)**i*gamma[jj]*inv[q][k]
 ck('all original cap coordinates retained in d2 '+str(q),s.expand((coinv[q-1]*ans)[0]-gamma[0])==0)
payload={'checker':'GPT-6 Astra, ChatGPT Pro mode, inherited effort; same model family','phase':'fresh computation after complete K116 supporting proof and K10 topology proof reading','check_count':len(checks),'checks':checks,'modular_coset_table':ct.table,'modular_profiles':{'order2':cycle_lengths(perm(ss)),'order3':cycle_lengths(perm(rr)),'cusp':cycle_lengths(perm(tw))},'source_Gram':mat(Gram),'monodromy_T':list(map(mat,Ts)),'all_four_zero_choices_parabolic_chains':chains,'scope':'exact rational source/translation inverses, chronological cusp Miller maps, both Cartier charts, actual infinity doubling, Hom degree, primitive periods, modular cover and literal K10 integral topology matrices. Analytic compactness, local invariant specialization, full fan geometry and cap endpoint maps are assessed in the written proof review.','elapsed_seconds':time.monotonic()-start}
(OUT/'k116_afterreading_exact.json').write_text(json.dumps(payload,indent=2)+'\n');print(json.dumps({k:v for k,v in payload.items()if k not in ['all_four_zero_choices_parabolic_chains','source_Gram','monodromy_T']},indent=2))
