#!/usr/bin/env python3
"""Independent exact F2.16 certificate from the clean parameter packet.

The target proof and original producer are unopened. All polynomial
identities below are over Q[v]; integrality is checked in Z[v], and
primitivity has an explicit integer combination of actual minors.
"""
from itertools import combinations
from pathlib import Path
from hashlib import sha256
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

v,z,t=s.symbols('v z t')
checks=[]
def check(name,condition):
    assert condition,name
    checks.append(name)
def zero(M):
    return all(s.cancel(x)==0 for x in M)
def eq(name,M,Q):
    check(name,zero(M-Q))
def strings(M):
    return [[str(s.factor(x)) for x in row] for row in M.tolist()]

q=v*v-v+1
A=s.zeros(5)
for j in range(5):
    A[(j+1)%5,j]=1
X=s.zeros(5,2);X[0,0]=1;X[2,1]=1;X[4,1]=v
Y=s.Matrix([[0,-q,-v*v,-1,v],[0,1-v*q,-v*q,v*v-v,q]])
N=X*Y;C=(s.eye(5)+N)*A;B=A**4*(s.eye(5)-N)
P=s.eye(5);P[:,0]=s.ones(5,1)/q
Ap=s.simplify(P.inv()*A*P);Bp=s.simplify(P.inv()*B*P)
sigma=v*v+v-1;rho=-(v+1)*(v*v-2)/2
beta=s.Matrix([[sigma,sigma-v*rho,v*v*sigma+v*rho,rho,-v*sigma-rho]])
Ah=s.diag(1,Ap);Bh=s.diag(1,Bp);Bh[0,1:6]=beta
L=s.Matrix([[-2,3,-5,-1,5,-3],[0,2,-2,2,-2,2],[0,-4,0,0,4,-4],
            [0,0,0,-4,4,-4],[0,0,4,-4,4,-4],[0,0,0,-4,4,0]])/4
Av=s.simplify(L.inv()*Ah*L);Bv=s.simplify(L.inv()*Bh*L)
K=s.simplify(Bv*Av-s.eye(6));M1=Av.T;M2=Bv.T;M0=s.eye(6)-K.T

eq('YX=0',Y*X,s.zeros(2))
eq('N squared zero',N*N,s.zeros(5))
eq('B is inverse of C',B*C,s.eye(5))
eq('A exact fifth-power relation',A**5,s.eye(5))
eq('C fourth-power relation',C**4,s.eye(5))
check('C characteristic polynomial',s.factor(C.charpoly(t).as_expr())==(t-1)*(t+1)**2*(t*t+1))
eq('Ah fifth-power relation',Ah**5,s.eye(6))
eq('Bh fourth-power relation including beta norm',Bh**4,s.eye(6))
check('P determinant',s.cancel(P.det()-1/q)==0)
check('L determinant',L.det()==-s.Rational(1,4))
eq('actual A lattice morphism',L*Av,Ah*L)
eq('actual B lattice morphism',L*Bv,Bh*L)
for name,M in [('A_v',Av),('B_v',Bv)]:
    for i in range(6):
        for j in range(6):
            check(name+' integer polynomial entry '+str((i,j)),s.Poly(s.cancel(M[i,j]),v).domain==s.ZZ)
    check(name+' determinant one',s.factor(M.det())==1)
eq('K squared zero universally',K*K,s.zeros(6))
eq('actual homology cusp relation',M0*(M1*M2),s.eye(6))
eq('cusp difference exact negative transpose',M0-s.eye(6),-K.T)

# Indices are zero-based, exactly as in the packet.
minor_data=[((0,1,4),(1,2,3),v*(v+1)),
            ((0,1,4),(1,3,4),v*v),
            ((0,3,4),(1,2,3),(v+1)**2)]
for rr,cc,value in minor_data:
    check('actual cusp minor '+str((rr,cc)),s.factor(K.extract(rr,cc).det()-value)==0)
check('integer combination of third minors equals one',s.expand(minor_data[2][2]-2*minor_data[0][2]+minor_data[1][2])==1)
all_third_minors=set()
for rr in combinations(range(6),3):
    for cc in combinations(range(6),3):
        d=s.factor(K.extract(rr,cc).det())
        all_third_minors.add(str(d))
        check('all third minors explicit '+str((rr,cc)),d in (0,v*(v+1),-v*(v+1),v*v,-v*v,(v+1)**2,-(v+1)**2))

# Exact quotient morphism to the original five-dimensional representation.
R=s.simplify(P*L[1:6,:])
eq('quotient intertwines A',R*Av,A*R)
eq('quotient intertwines B',R*Bv,B*R)
check('quotient rank five',R.rank()==5)
eq('quotient kills exactly the displayed common line',R[:,0],s.zeros(5,1))
eq('common line fixed by A',Av[:,0],s.eye(6)[:,0])
eq('common line fixed by B',Bv[:,0],s.eye(6)[:,0])
Nu=N*s.ones(5,1);row=s.ones(1,5)*N
eq('fixed-line obstruction vector',Nu,-2*q*X*s.Matrix([1,v-1]))
check('sum-zero obstruction coordinates',s.factor(row[3]-(v**3-v-1))==0 and s.factor(row[4]-(v**3+v+1))==0)
check('their difference forces v=-1',s.expand(row[4]-row[3])==2*(v+1))
check('the row is nonzero also at v=-1',row[3].subs(v,-1)==-1)

# Character morphisms for simultaneous conjugacy and contragredient duality.
tr=s.factor(s.trace(A*C));trinv=s.factor(s.trace(B*A**4))
check('trace via the actual rank-two update',s.factor(tr-s.trace(Y*A**2*X))==0)
check('inverse trace via rank-two update',s.factor(trinv+s.trace(Y*A**3*X))==0)
check('trace of A C',s.factor(tr-(1-v*v*q))==0)
check('trace of inverse A C',s.factor(trinv-(1+v*v*q))==0)
check('nonselfdual trace difference',s.factor(tr-trinv)==-2*v*v*q)
trace6=s.factor(s.trace(Av*Bv**3))
check('six-dimensional conjugacy invariant',s.factor(trace6-(2-v*v*q))==0)
check('strict successive decrease formula',s.expand(trace6.subs(v,v+1)-trace6)==-4*v**3-3*v**2-3*v-1)
trace_table={}
for a in range(1,5):
    for b in range(1,4):
        W=A**a*C**b
        trace_table[str((a,b))]={'trace':str(s.factor(s.trace(W))),
                               'inverse_trace':str(s.factor(s.trace(C**(4-b)*A**(5-a))))}
Q=s.Matrix(5,5,lambda i,j:int((j-i)%5 in (1,4)))
eq('parameter-zero invariant form A',A.T*Q*A,Q)
eq('parameter-zero invariant form B',B.subs(v,0).T*Q*B.subs(v,0),Q)
check('parameter-zero form nondegenerate',Q.det()==2)

a=s.Matrix([1,3,-2,-1,2,0]);e=s.eye(6)[:,0]
w1=s.simplify(sum((M1**j*a for j in range(5)),s.zeros(6,1))/5)
w2=s.simplify(-sum((M2**j*e for j in range(4)),s.zeros(6,1))/4)
eq('first averaged vector fixed',M1*w1,w1)
eq('second averaged vector fixed',M2*w2,w2)
ell=s.Matrix([[1,0,0,0,0,0]])
eq('ell M1 equals ell',ell*M1,ell)
eq('ell M2 equals ell',ell*M2,ell)
check('marked quotient-circle numerators',(ell*w1)[0]==1 and (ell*w2)[0]==-1)
for i in range(6):
    check('w1 integral on the specified subfamily '+str(i),s.Poly(s.cancel(w1[i].subs(v,20*z)),z).domain==s.ZZ)
    check('w2 integral on the specified subfamily '+str(i),s.Poly(s.cancel(w2[i].subs(v,20*z)),z).domain==s.ZZ)
for n,sgn in [(5,1),(4,-1)]:
    for j in range(1,n):
        check('every nontrivial affine power moves the quotient circle '+str((n,j)),s.Rational(sgn*j,n).q!=1)
Z1=s.Matrix([[1,0,0,0,0,0],[0,1,1,2,2,1],[0,-1,0,-1,0,1],
             [1,-1,-1,-1,-1,-1],[-1,1,0,0,0,0],[1,0,0,1,0,0]])
Z2=s.Matrix([[1,0,0,0,0,0],[0,0,0,0,1,0],[0,-1,-1,-1,-1,-1],
             [0,0,0,0,0,1],[0,1,0,0,0,0],[0,0,1,0,0,0]])
eq('parameter-zero marked first matrix',M1.subs(v,0),Z1)
eq('parameter-zero marked second matrix',M2.subs(v,0),Z2)
eq('parameter-zero first affine numerator',w1.subs(v,0),a)
eq('parameter-zero second affine numerator',w2.subs(v,0),-e)
smith_samples={}
for n in (-40,-20,-2,-1,0,1,2,20,40,60):
    H=smith_normal_form(K.subs(v,n),domain=s.ZZ)
    values=[abs(int(H[i,i])) for i in range(6) if H[i,i]]
    check('independent specialized Smith computation '+str(n),values==[1,1,1])
    smith_samples[str(n)]=values

out={'status':'PASS','checks':len(checks),'check_names':checks,
     'method':'new exact symbolic matrix derivation over Q[v], coefficient integrality, an integer Bezout sum of actual third minors, and specialized Smith computations; no original producer import',
     'chronology':'all calculations precede target-proof exposure',
     'A_v':strings(Av),'B_v':strings(Bv),'K':strings(K),'quotient_map':strings(R),
     'third_minor_certificate':[{'rows':rr,'cols':cc,'value':str(val)} for rr,cc,val in minor_data],
     'all_third_minor_values':sorted(all_third_minors),'trace_table':trace_table,
     'w1':strings(w1),'w2':strings(w2),'zero_invariant_form':strings(Q),
     'smith_samples':smith_samples,'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','checks','method','chronology','third_minor_certificate','smith_samples','source_sha256')},indent=2))
