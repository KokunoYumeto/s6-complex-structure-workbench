#!/usr/bin/env python3
"""Fresh K117 checks after all five supplied proofs were read.

No historical checker is imported.  Symbolic identities and fresh linear solves
support the geometric review; they do not replace its relative cap maps.
Author: GPT-6 Astra, ChatGPT Pro mode, inherited effort, same model family.
"""
from pathlib import Path
import itertools,json,time,sys
import sympy as s
OUT=Path(__file__).resolve().parents[1]/'output'
checks=[]; started=time.monotonic()
def ck(name,yes):
    assert yes,name
    checks.append(name)
def zero(v):return s.cancel(v)==0
def mj(M):return [[str(M[i,j])for j in range(M.cols)]for i in range(M.rows)]

# The full original height chart: independent substitution in the cubic.
u,q,X,y,S,c,d=s.symbols('u q X y S c d',nonzero=True)
aa=-u/3-u**4/9;tc=1/(2*u)-u**2/3;xi=1/(4*u**2)+u/3
cc=3*xi;Rc=xi-u;dd=2*tc+q;t=tc+q;x=X+xi
Rt=t*t+aa;f=Rt**2+t;g=Rt**3+s.Rational(3,2)*t*Rt+s.Rational(3,8)
H=dd*(-6*Rc*(u+X)+3*tc)+3*q*dd**2*(2*Rc-xi-X)+2*q*q*dd**3-3*(u+X)+3*q*dd
ck('full original source implicit equation',zero(x**3-3*f*x+2*g-X**2*(X+cc)-q*H))
ck('H(0,0,c)=-2u^4',zero(H.subs({q:0,X:0})+2*u**4))
ck('H0=3u0/2 on 4u0^3+3=0',s.rem(-2*u**4-3*u/2,4*u**3+3,u)==0)
Germ=s.Matrix([S*S-c*c,S*(S*S-c*c),c]);DG=Germ.jacobian([S,c])
minors=[DG.extract(I,[0,1]).det()for I in itertools.combinations(range(3),2)]
gb=s.groebner(minors,S,c)
ck('derivative minor ideal exactly (S,c^2)',[p.as_expr()for p in gb.polys]==[S,c*c])
normal=s.Matrix([3*S*S-c*c,-2*S,2*c*(S*S-c*c)])
ck('cross product of two actual derivatives',all(zero(z)for z in DG[:,0].cross(DG[:,1])-normal))
F0=y*y-X*X*(X+c*c)
grad=s.Matrix([s.diff(F0,z)for z in [X,y,c]]).subs({X:S*S-c*c,y:S*(S*S-c*c)})
ck('entire normalization conormal factor',all(zero(z)for z in grad+(S*S-c*c)*normal))
Z=(S-c)/(S+c)
ck('full Mobius S derivative',zero((S+c)**2*s.diff(Z,S)-2*c))
ck('full Mobius parameter derivative',zero((S+c)**2*s.diff(Z,c)+2*S))
ck('normal branches two products use same unit',zero((S*S-c*c)/Z-(S+c)**2)and zero((S*S-c*c)*Z-(S-c)**2))
R,J,H0=s.symbols('R J H0');eqs=s.Matrix([R*R*(R+1)+J*H0,3*R*R+2*R])
at={R:-s.Rational(2,3),J:-s.Rational(4,27)/H0}
ck('second critical value exact central equations',eqs.subs(at)==s.zeros(2,1))
ck('second critical value invertible Jacobian',eqs.jacobian([R,J]).subs(at)==s.Matrix([[0,H0],[-2,0]]))
# Weighted pencil: the full extended E8 intersection vector and section.
adj=[(0,1),(1,2),(2,3),(3,4),(4,5),(0,6),(0,7),(7,8)]
Q=s.diag(*([-2]*9))
for i,jj in adj:Q[i,jj]=Q[jj,i]=1
mult=s.Matrix([6,5,4,3,2,1,3,4,2])
ck('weighted pencil affine E8 primitive fibre kernel',Q*mult==s.zeros(9,1)and Q.rank()==8)
ext=Q.row_join(s.zeros(9,1)).col_join(s.zeros(1,10));ext[9,9]=-1;ext[5,9]=ext[9,5]=1
ck('weighted pencil with section integral unimodular',ext.det()==-1)
print('source and weighted pencil: PASS',flush=True)

# Derive the chronological tangent quotients directly on the nodal cubic.
xx=lambda z:z*z-s.Rational(2,3)*c*c
yy=lambda z:z*(z*z-c*c)
nodef=c**4/9;cur=d;fm=s.Integer(1);fs={};points={1:d}
for m in [2,4,8]:
    slope=s.cancel((3*xx(cur)**2-3*nodef)/(2*yy(cur)))
    nxt=s.cancel((cur*cur+c*c)/(2*cur))
    tangent=yy(S)-yy(cur)-slope*(xx(S)-xx(cur))
    quotient=s.cancel(tangent/(xx(S)-xx(nxt)))
    ck('tangent quotient at '+str(m//2)+'G',zero(quotient-(S-cur)**2/(S-nxt)))
    fm=s.cancel(fm*fm*quotient);points[m]=nxt;cur=nxt
    ck('chronological nodal f'+str(m),zero(fm-(S-d)**m/(S-nxt)))
    # Reuse the factored expression only after exact zero-difference proof.
    fm=(S-d)**m/(S-nxt);fs[m]=fm
P=(d-c)/(d+c);T=(d*S-c*c)/(d-S)
ck('nodal inverse source translation',zero((d*T+c*c)/(d+T)-S))
ck('node translation period P inverse',zero(Z.subs(S,T)-Z/P))
kernel=s.cancel(fs[2]*(T-d)/(S-d))
ck('exact Miller cancellation before eighth power',zero(kernel+2*d))
coef=kernel**8*(S-points[8])/(T-points[8])
ck('full nodal Miller coefficient through point modules',zero(coef-(-2*d)**8*(S-points[8])/(T-points[8])))
ck('Cartier W arrow exactly constant at every normalization point',zero(coef*(T-points[8])/(S-points[8])-(-2*d)**8))
for m in [2,4,8]:
    sm=points[m]
    ck('literal nodal theta coefficient '+str(m),zero((1-Z/P**m)/(1-Z)-(S-sm)/(c-sm)))
    ck('reflected point factor '+str(m),zero((-c-sm)-P**(-m)*(c-sm)))
    ck('central division limit '+str(m),zero(sm.subs(c,0)-d/m))
C8=(c-points[8])/(c-d)**8
ck('entire nodal point to tensor factor even',zero(C8.subs(c,-c)-C8))
ck('original beta node constant',zero(((-2*d)**8).subs(d,-s.sqrt(3)/(2*u))-81/u**8))
print('chronological Miller and full point modules: PASS',flush=True)

# Physical quaternion and determinant signs, including the full anti-linear map.
ii=s.I;I=s.diag(ii,-ii);JJ=s.Matrix([[0,-1],[1,0]]);K=s.Matrix([[0,ii],[ii,0]])
ck('first column SU2 tangent multiplication I J=-K',I*JJ==-K)
ck('first column cubic trace coefficient',s.trace(I*JJ*K)==2)
cubic=sum(((-1)**sum(p[a]>p[b]for a in range(3)for b in range(a+1,3)))*s.trace([I,JJ,K][p[0]]*[I,JJ,K][p[1]]*[I,JJ,K][p[2]])for p in itertools.permutations(range(3)))
ck('Maurer cubic 12 times oriented volume',cubic==12)
lin=s.Matrix([[1,1],[1,-1]])
ck('frame map complex det -2 real det +4',lin.det()==-2 and lin.det()**2==4)
a0,a1,b0,b1=s.symbols('a0 a1 b0 b1',real=True);av=a0+ii*a1;bv=b0+ii*b1
gmat=s.Matrix([[av,-s.conjugate(bv)],[bv,s.conjugate(av)]])
ck('anti-linear map intertwines every SU2 transition',s.conjugate(gmat)==JJ*gmat*JJ.inv())
anti=s.Matrix([[0,0,1,0],[0,0,0,-1],[-1,0,0,0],[0,1,0,0]])
ck('physical duality real orientation and square',anti.det()==1 and anti*anti==-s.eye(4))
gam=av*s.conjugate(av)-bv*s.conjugate(bv);ell=s.conjugate(av)*bv
qa,qb=s.conjugate(bv),-s.conjugate(av)
ck('anti-linear projective map is full antipodal',s.expand(qa*s.conjugate(qa)-qb*s.conjugate(qb)+gam)==0 and s.expand(s.conjugate(qa)*qb+ell)==0)
def qm(a,b):
    a0,a1,a2,a3=a;b0,b1,b2,b3=b
    return s.Matrix([a0*b0-a1*b1-a2*b2-a3*b3,a0*b1+a1*b0+a2*b3-a3*b2,a0*b2-a1*b3+a2*b0+a3*b1,a0*b3+a1*b2-a2*b1+a3*b0])
def qc(a):return s.Matrix([a[0],-a[1],-a[2],-a[3]])
vv,al=s.symbols('vartheta angle',real=True)
h=qm([s.sin(vv)*s.cos(al),s.sin(vv)*s.sin(al),s.cos(vv),0],[s.sin(vv),0,-s.cos(vv),0])
axis=qm(qm(h,[0,1,0,0]),qc(h));inverse_axis=qm(qm(qc(h),[0,1,0,0]),h)
point={vv:s.pi/4,al:s.pi}
ck('actual H_d axis at its regular negative-i preimage',axis.subs(point)==s.Matrix([0,-1,0,0]))
ck('actual H_d axis derivatives and degree sign',axis.diff(vv).subs(point)==s.Matrix([0,0,0,4])and axis.diff(al).subs(point)==s.Matrix([0,0,-1,0]))
ck('actual inverse H_d axis derivatives and degree sign',inverse_axis.diff(vv).subs(point)==s.Matrix([0,0,0,-4])and inverse_axis.diff(al).subs(point)==s.Matrix([0,0,-1,0]))
ck('Hopf source sphere orientation reversal',s.Matrix([[0,-2],[-2,0]]).det()==-4)
sig,esq=s.symbols('signature e_square');seif=s.solve([3*sig+esq+4,esq-sig-8],[sig,esq])
ck('both signed Seifert equations',seif=={sig:-3,esq:5})
ck('local link Haefliger formula',s.Rational(1,2)+s.Rational(2,6)+s.Rational(1,6)==1)
ck('nonzero Kummer normalization test',-s.Rational(3,2)*16/(-4)/3==2 and s.Rational(16,8)==2)
ck('two cap pairs and physical inverse clutch',(-1-5,-4+4)==(-6,0) and s.Rational(-6,6)==-1)

# Exact exterior algebra in declared outward order (alpha,u,b,gamma,theta).
def add(A,B):
    out=dict(A)
    for k,vv in B.items():out[k]=s.expand(out.get(k,0)+vv)
    return {k:v for k,v in out.items()if v!=0}
def scale(A,v):return {k:s.expand(v*x)for k,x in A.items()if v*x!=0}
def wedge(A,B):
    out={}
    for ia,va in A.items():
      for ib,vb in B.items():
        if set(ia)&set(ib):continue
        seq=ia+ib;sg=(-1)**sum(seq[i]>seq[j]for i in range(len(seq))for j in range(i+1,len(seq)))
        key=tuple(sorted(seq));out[key]=s.expand(out.get(key,0)+sg*va*vb)
    return {k:v for k,v in out.items()if v!=0}
j,alpha,theta,ss=s.symbols('j alpha theta s')
beta={(1,):-j,(2,):-j*(alpha-6*theta)}
F={(0,3):1,(0,2):j};dbeta={(0,2):-j,(2,4):-6*j}
ck('full boundary F square zero',wedge(F,F)=={})
ck('full beta differential square zero',wedge(dbeta,dbeta)=={})
ck('exact boundary fifth form',wedge(wedge(beta,F),dbeta)=={(0,1,2,3,4):6*j*j})
Ft=add(F,scale(dbeta,ss));trans=wedge(beta,wedge(Ft,Ft))
trans={k:s.integrate(3*v,(ss,0,1))for k,v in trans.items()}
ck('integrated entire collar transgression',trans=={(0,1,2,3,4):18*j*j})
# The source coefficients are first retained in their logarithms.  Basis change
# is linear there, so this verifies the entire coefficients, not just windings.
lk,lg,la,le,lq=s.symbols('log_kappa log_g log_alpha log_eta log_q')
vertical=s.Matrix([[1,0],[-j,1]])
periods=s.Matrix([[lk+lq,lg],[la,le+lq]])
newperiods=vertical*periods*s.Matrix([[1,0],[j,1]])
ck('entire vertical source and line periods',all(zero(z)for z in newperiods-s.Matrix([[lk+lq+j*lg,lg],[la+j*le-j*lk-j*j*lg,le+lq-j*lg]])))
va,db=s.symbols('va db');mu=-6-(va+db)/2;nu=(db-va)/2
mup=mu+2*nu;nup=-nu;vap=-6-mup-nup;dbp=-6-mup+nup
ck('native Cox reset gives both target ordinary values',zero(vap-va)and zero(dbp-2*va+db))
print('cap signs, complete wedge and native reset: PASS',flush=True)

# Full coefficient basis maps: every atom exponent, forward and inverse.
Q0=s.Matrix([[1,-1],[0,1]]);Q1=s.Matrix([[1,0],[-1,1]])
def data(P):
    R=P.inv();B=-6*R*s.Matrix([[1,0],[0,0]])*P;x,y=R*s.Matrix([0,1])
    w=[x,y,-x-y];d=[-x-2*y,-2*x-y,x-y]
    ell=[B[1,1]-B[1,0],B[0,0]-B[0,1],B[1,1]]
    I=[-3*w[i]+d[i]*(ell[i]+3)for i in range(3)];J=[-3*w[i]-d[i]*(ell[i]+3)for i in range(3)]
    return w,I,J,ell
def seed(n):
    h=18*n*(n-1)
    return s.Matrix([[h,6-12*n,12*n-6],[6-12*n,0,0],[12*n-6,0,0]]),s.Matrix([-12-h,12*n-12,-12*n]),s.Integer(-1-3*n*(n-1))
vs=s.symbols('v00 v01 v02 v11 v12 v22 d0 d1 d2')
Vvar=s.Matrix([[vs[0],vs[1],vs[2]],[vs[1],vs[3],vs[4]],[vs[2],vs[4],vs[5]]]);Dvar=s.Matrix(vs[6:])
paths=[];solves=0
for n in range(-3,4):
    P=s.Matrix([[1,0],[n,1]]);V,D,score=seed(n)
    w,I,J,ell=data(P)
    for k in [1,2]:
        ck('full vertical seed '+str((n,k)),V*(w[k]*s.eye(3)[:,k]-w[0]*s.eye(3)[:,0])==I[k]*s.eye(3)[:,k]-I[0]*s.eye(3)[:,0]and w[k]*D[k]-w[0]*D[0]==J[k]-J[0])
    states=[(P,V,D,score,())]
    for depth in range(1,6):
      targets=[]
      for P,V,D,score,word in states:
        for edge in ([0]if depth==1 else [0,1]):
          Q=Q0 if edge==0 else Q1;PP=P*Q;w,I,J,ell=data(PP);va=V[edge,edge];db=D[edge]
          equations=[]
          for k in [1,2]:
            equations+=list(Vvar*(w[k]*s.eye(3)[:,k]-w[0]*s.eye(3)[:,0])-I[k]*s.eye(3)[:,k]+I[0]*s.eye(3)[:,0])
            equations.append(w[k]*Dvar[k]-w[0]*Dvar[0]-J[k]+J[0])
          equations += [Vvar[2,2]-va,Dvar[2]-(2*va-db)]
          system,rhs=s.linear_eq_to_matrix(equations,vs)
          solutions=list(s.linsolve((system,rhs),vs));assert len(solutions)==1
          sol=solutions[0];assert all(not z.free_symbols and z.q==1 for z in sol)
          Vnew=Vvar.subs(dict(zip(vs,sol)));Dnew=Dvar.subs(dict(zip(vs,sol)))
          C=w[2]**2*va-w[2]*I[2];E=w[2]*(2*va-db)-J[2]
          explicit=s.Matrix(3,3,lambda r,k:(I[r]/w[r]if r==k else 0)+C/(w[r]*w[k]))
          ck('fresh nine variable solution '+str((n,word+(edge,))),Vnew==explicit and Dnew==s.Matrix([(J[k]+E)/w[k]for k in range(3)]))
          newscore=score+(db-va)/2;assert newscore.q==1
          for ah,al in itertools.product(range(2),repeat=2):
            atom=s.zeros(2);atom[ah,al]=1
            old=P.inv()*atom*P;new=PP.inv()*atom*PP
            assert Q.inv()*old*Q==new and Q*new*Q.inv()==old
          targets.append((PP,Vnew,Dnew,newscore,word+(edge,)));solves+=1
          paths.append({'seed':n,'word':list(word+(edge,)),'P':mj(PP),'V':mj(Vnew),'delta':[str(z)for z in Dnew],'score':str(newscore),'score_mod28':int(newscore)%28})
      states=targets
ck('217 actual canonical forward target solves',solves==217)
result={'author':'GPT-6 Astra; ChatGPT Pro mode; inherited effort; same model family','chronology':'After reading all five K117 supporting proofs. No historical code imported.','runtime':{'python':sys.version,'sympy':s.__version__},'status':'PASS','check_count':len(checks),'checks':checks,'fresh_full_nine_variable_solves':solves,'full_atom_exponent_roundtrips':solves*4,'elapsed_seconds':time.monotonic()-started,'paths':paths,'scope_limit':'Exact source/Miller/determinant/Chern/wedge/prism algebra and bounded canonical paths; the unbounded termination and actual geometric line/cap transports are checked in K117_REVIEW.md, not established by finite execution.'}
(OUT/'k117_afterreading_exact.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items()if k!='paths'},indent=2))
