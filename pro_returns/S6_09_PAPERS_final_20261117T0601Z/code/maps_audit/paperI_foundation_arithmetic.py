"""Independent exact checks for three fully read Paper I foundation inputs.

This is an arithmetic certificate, not a substitute for the recorded
geometric, analytic, covering-space, or spectral-sequence proofs.
"""
from itertools import combinations
from pathlib import Path
import json
from sympy import Matrix, eye, zeros, symbols, simplify, expand, ZZ, I, Rational, rem
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form

checks = []
def done(name, scope):
    checks.append({'name': name, 'status': 'PASS', 'scope': scope})
def ext(M, p):
    ii=list(combinations(range(M.rows),p))
    return Matrix([[M.extract(i,j).det() for j in ii] for i in ii])
def smith(M):
    D=smith_normal_form(M,domain=ZZ)
    return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
def same_span(A,B):
    return hermite_normal_form(A)==hermite_normal_form(B)
def zero(M):
    return all(simplify(x)==0 for x in M)

T1=Matrix([[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]])
T2=Matrix([[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]])
T0=(T1*T2).inv(); A1=T1.inv().T; A2=T2.inv().T; M0=T0.inv().T
assert T1**3==eye(4) and T2**4==eye(4)
assert T2**2!=eye(4) and (T0-eye(4))**2==zeros(4)
assert A1*A2*M0==eye(4)
done('monodromy', 'All orders, inverses, contragredients and cusp relation.')

gam=Matrix([1,0,0,0]); eta1=Matrix([0,2,1,3]); eta2=Matrix([0,1,1,2])
q=Matrix([0,0,6,1,0,0]); vol=Matrix([1])
inv0={1:Matrix.hstack(gam,Matrix([0,1,0,0])),
      2:Matrix.hstack(Matrix([1,0,0,0,0,0]),Matrix([0,0,1,0,0,0]),
                     Matrix([0,0,0,1,0,0]),Matrix([0,1,0,0,-1,0])),
      3:Matrix([[1,0],[0,1],[0,0],[0,0]])}
for p,K in inv0.items():
    Q=ext(T0,p)-eye(K.rows)
    assert Q*K==zeros(K.rows,K.cols)
    assert K.cols+Q.rank()==K.rows and smith(K)==[1]*K.cols
done('cusp invariant lattices', 'Primitive full kernels in exterior degrees 1,2,3; ranks 1,2,4,2,1.')

B2=Matrix([[-2,1,1,-6,2,-8,-1,-1,1,-6,6,-3],
[-1,-1,1,-6,2,-6,1,-1,0,0,3,0],
[0,0,0,0,0,-6,0,0,0,0,6,0],
[0,0,0,0,0,1,0,0,0,0,-1,0],
[0,0,0,0,-2,1,0,0,0,0,-1,-1],
[0,0,0,0,-1,-1,0,0,0,0,1,-1]])
B3=Matrix([[0,0,1,2,0,-1,0,-3],[0,-2,1,-6,0,-1,-1,-6],
           [0,-1,-1,-6,0,1,-1,0],[0,0,0,0,0,0,0,0]])
global_invs={1:gam,2:q,3:Matrix([1,0,0,0]),4:vol}
for p,K in global_invs.items():
    U=ext(T1,p);V=ext(T2,p);n=U.rows
    N=Matrix.vstack(U-eye(n),V-eye(n))
    assert N*K==zeros(N.rows,1) and n-N.rank()==1 and smith(K)==[1]
    R=Matrix.hstack(U-eye(n),V-eye(n))
    assert smith(R)==[1]*(n-1)
    if p==2: assert R==B2
    if p==3: assert R==B3
done('global invariant/coinvariant lattices', 'All exterior degrees; printed B2/B3 entrywise; no hidden torsion.')

def wedge_1_1(x,y):
    return Matrix([x[i]*y[j]-x[j]*y[i] for i,j in combinations(range(4),2)])
def wedge_2_2(x,y):
    return x[0]*y[5]-x[1]*y[4]+x[2]*y[3]+x[3]*y[2]-x[4]*y[1]+x[5]*y[0]
def wedge_1_3(x,y):
    return x[0]*y[3]-x[1]*y[2]+x[2]*y[1]-x[3]*y[0]
for T,A,eta,m,v in [(T1,A1,eta1,3,Matrix([1,2,-4,0])),
                     (T2,A2,eta2,4,Matrix([-1,-3,3,0]))]:
    K=Matrix.hstack(gam,eta)
    for j in range(1,m):
        N=T**j-eye(4)
        assert N*K==zeros(4,2) and N.rank()==2 and smith(K)==[1,1]
    assert A*v==v and (eta.T*v)[0]==0 and abs((gam.T*v)[0])==1
    assert smith(A-eye(4))==[1,1]
    x=wedge_1_1(gam,eta);K2=Matrix.hstack(x,q)
    assert (ext(T,2)-eye(6))*K2==zeros(6,2)
    assert (ext(T,2)-eye(6)).rank()==4 and smith(K2)==[1,1]
    assert wedge_2_2(x,x)==0 and wedge_2_2(q,q)==12
    assert wedge_2_2(x,q)==(3 if m==3 else 2)
    z=Matrix([0,-4,-2,1]) if m==3 else Matrix([0,-3,-3,1])
    K3=Matrix.hstack(Matrix([1,0,0,0]),z)
    assert (ext(T,3)-eye(4))*K3==zeros(4,2) and smith(K3)==[1,1]
    pairing=Matrix([[wedge_1_3(a,b) for b in [K3[:,0],K3[:,1]]] for a in [gam,eta]])
    assert pairing==Matrix([[0,1],[-(3 if m==3 else 2),0]])
norm=sum((T2**j for j in range(4)),zeros(4))
assert same_span(norm,Matrix.hstack(4*gam,2*eta2))
done('finite invariant and pullback arithmetic', 'All fixed powers, saturated bases, norm lattice, Gram determinants, degree-three perfect-pairing coefficients.')

eps1=Matrix([1,2,-4,0]);eps2=Matrix([1,3,-3,0]);ds=Matrix([0,0,0,1])
e1=Matrix([0,1,-2,0]);f1=Matrix([0,0,-3,1]);e2=Matrix([0,1,-1,0]);f2=Matrix([0,0,-2,1])
for A,eps,e,f,d in [(A1,eps1,e1,f1,-3),(A2,eps2,e2,f2,-2)]:
    K=Matrix.hstack(eps,ds);L=Matrix.hstack(e,f)
    assert (A-eye(4))*K==zeros(4,2) and (A-eye(4)).rank()==2
    assert smith(K)==[1,1] and smith(L)==[1,1] and same_span(A-eye(4),L)
    assert Matrix.hstack(K,L).det()==d
done('fixed/moving product-cover lattices', 'Full images and kernels, primitive summands, and exact indices 3 and 2.')

t,mu,beta=symbols('t mu beta')
F1=Matrix([(t-1)/t,(1-mu)/t,beta+2-6*(1-mu)**2/t])
F2=Matrix([-1/t,1+mu/t,beta-3-6*mu**2/t])
v=Matrix([t,mu,beta])
def comp(F,G): return F.subs(dict(zip([t,mu,beta],G)),simultaneous=True).applyfunc(simplify)
for F,m in [(F1,3),(F2,4)]:
    G=v
    for i in range(m): G=comp(F,G)
    assert zero(G-v)
assert zero(comp(F1,F2)-Matrix([t+1,mu,beta-1]))
Pi=Matrix([[6*mu,t,1,0],[beta,mu,0,1]])
R1=Matrix([[-1/t,0],[(1-mu)/t,1]]); R2=Matrix([[1/t,0],[-mu/t,1]])
for F,R,T in [(F1,R1,T1),(F2,R2,T2)]:
    assert zero(Pi.subs(dict(zip([t,mu,beta],F)),simultaneous=True)-R*Pi*T.T)
pp,rr,kk=symbols('p r k',integer=True)
P=eye(2)+kk*Matrix([[-pp*rr,pp**2],[-rr**2,pp*rr]])
S1=Matrix([[1,-1],[1,0]])
assert simplify((S1.inv()*P.inv()).trace()-(1+kk*(pp**2-pp*rr+rr**2)))==0
done('period cocycles and deck normalization', 'Cyclic affine identities, exact cusp shift, full period covariance, and parabolic trace equation.')

r=symbols('rho'); br=symbols('beta_rho')
for tv,muv,betav,L,R,eps,e,f,kap,d in [
    (r,(2-r)/3,br,Matrix([[0,1],[1,-Rational(1,3)]]),Matrix([[r-1,0],[(2-r)/3,1]]),eps1,e1,f1,br+2*(2-r)/3,3),
    (I,(1-I)/2,br,Matrix([[0,1],[1,-Rational(1,2)]]),Matrix([[-I,0],[(1+I)/2,1]]),eps2,e2,f2,br+3*(1-I)/2,2)]:
    Pc=Pi.subs({t:tv,mu:muv,beta:betav})
    def zz(M): return all(rem(expand(simplify(x).as_numer_denom()[0]),r*r-r+1,r)==0 for x in M)
    assert zz(Pc*eps-Matrix([0,kap])) and zz(Pc*ds-Matrix([0,1]))
    rot=r-1 if d==3 else -I
    assert zz(R*L-L*Matrix.diag(1,rot))
    ker=Matrix([Rational(2,3),r]) if d==3 else Matrix([Rational(1,2),I])
    assert zz(L*ker-Pc*Matrix([0,1,0,0]))
done('central complex product maps', 'Unchanged original periods, moving eigenlines, product linear maps and complete kernel points.')

A=Matrix([[2,1,3,0,0,0],[-4,-2,0,1,0,0],[-2,-2,-4,0,0,0],[3,3,0,-1,0,0]])
Phi=Matrix([[4,2,3,2]])
assert Phi*A==zeros(1,6) and smith(A)==[1,1,1]
assert A.extract([0,1,2],[0,1,3]).det()==2
assert A.extract([0,1,3],[0,1,3]).det()==-3
l0,l1,l2=symbols('l0 l1 l2',integer=True)
assert Matrix([[3,-l1],[4,l2-4*l0]]).det()==-(12*l0-4*l1-3*l2)
done('terminal certificates', 'Primitive degree-two image, displayed minors and terminal group determinant.')

out={'status':'PASS','reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17',
     'checks':checks,'limits':'Exact arithmetic only. Analytic construction, toric properness, finite covering and normalization arguments were independently read and rederived in the separate full-proof ledger.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
