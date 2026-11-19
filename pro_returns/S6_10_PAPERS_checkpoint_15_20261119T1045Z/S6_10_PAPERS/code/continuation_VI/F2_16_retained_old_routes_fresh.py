#!/usr/bin/env python3
"""New post-target computations for every extra old F2.16 producer route.

Imports only our independently authored clean-packet construction. The
old producer is never imported or called. No prereading proof credit is
claimed for this supplementary calculation.
"""
from F2_16_symbolic_work import A,B,C,X,Y,N,P,Ap,Bp,Ah,Bh,Av,Bv,L,beta,v,q,s
from pathlib import Path
from hashlib import sha256
from itertools import combinations
from math import prod
from sympy.matrices.normalforms import smith_normal_form
import json

x,h,k=s.symbols('x h k')
checks=[]
def check(name,b):
    assert b,name
    checks.append(name)
def equal(name,a,b):
    check(name,all(s.cancel(z)==0 for z in a-b))
def integral_poly(M,var):
    return all(s.Poly(s.cancel(z),var).domain==s.ZZ for z in M)
def minors_mod(M,rank,p):
    return [int(M.extract(rr,cc).det())%p for rr in combinations(range(M.rows),rank) for cc in combinations(range(M.cols),rank)]
def torsion(M):
    D=smith_normal_form(M,domain=s.ZZ)
    return prod(abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i])

right_inverse=(A+s.eye(5)).inv()*X
equal('actual rational right inverse for Y',Y*right_inverse,s.eye(2))
check('twice right inverse integer polynomial',integral_poly(2*right_inverse,v))
check('primitive original X has a unit row minor',X.extract((0,2),(0,1)).det()==1)
parities={}
for epsilon in (0,1):
    yy=Y.subs(v,epsilon)
    yy_min=minors_mod(yy,2,2)
    check('rank two Y mod2 '+str(epsilon),1 in yy_min)
    total=Av*Bv-s.eye(6)
    nn=total.subs(v,epsilon)
    nn_min=minors_mod(nn,3,2)
    check('rank three final cusp mod2 '+str(epsilon),1 in nn_min)
    parities[str(epsilon)]={'Y_nonzero_second_minors_mod2':sum(yy_min),'cusp_nonzero_third_minors_mod2':sum(nn_min)}
equal('five-dimensional ordered product',A*B,s.eye(5)-N)
equal('actual restricted operator H in the X basis',N*A*X,X*(Y*A*X))
equal('actual restricted operator Hprime in the X basis',N*A**4*X,X*(Y*A**4*X))
d=s.factor((Y*A*X).det());dp=s.factor((Y*A**4*X).det())
check('det H',s.expand(d-(1-v*v*q))==0)
check('det Hprime',s.expand(dp-(1+v*v*q))==0)
check('additional trace invariant',s.factor(s.trace(A**2*C**2))==v**5-v**4+3)
pencil=s.Poly(s.det(x*s.eye(5)-(s.eye(5)+h*N)*A),h)
check('pencil degree at most2',pencil.degree()==2)
check('quadratic pencil coefficient',s.factor(pencil.nth(2)-x*x*(d*x-dp))==0)
check('pencil endpoint at0',s.expand(pencil.as_expr().subs(h,0)-A.charpoly(x).as_expr())==0)
check('pencil endpoint at1',s.expand(pencil.as_expr().subs(h,1)-C.charpoly(x).as_expr())==0)
check('anti-reciprocity coefficient obstruction',s.cancel(pencil.nth(2)+x**5*pencil.nth(2).subs(x,1/x)-x*x*(x+1)*(d-dp))==0)

check('A prime polynomial integral',integral_poly(Ap,v))
check('B prime polynomial integral',integral_poly(Bp,v))
equal('specified overlattice generator transformation',Y*s.ones(5,1),2*q*s.Matrix([-1,1-v]))
rho=-(v+1)*(v*v-2)/2;sigma=v*v+v-1
for epsilon in (0,1):
    check('r integer-valued parity '+str(epsilon),s.Poly(s.expand(rho.subs(v,2*k+epsilon)),k).domain==s.ZZ)
Xn=s.simplify(P.inv()*X);Yn=s.simplify(Y*P)
Z=s.Matrix([-v**3+v-1,0,0,2,2*(1-v*v)])
equal('Y prime X prime zero',Yn*Xn,s.zeros(2))
check('X prime primitive unit minor',s.factor(Xn.extract((1,2),(0,1)).det())==-1)
T=Yn[:,(0,3,4)]
expected=s.Matrix([[-2,-1,v],[2*(1-v),v*v-v,q]])
equal('actual quotient coordinate map',T,expected)
signed_minors=s.Matrix([T[:,(1,2)].det(),-T[:,(0,2)].det(),T[:,(0,1)].det()])
equal('three signed minors give specified generator',signed_minors,Z[(0,3,4),:])
equal('actual kernel generator',Yn*Z,s.zeros(2,1))
check('beta of actual kernel lift equals1',s.expand((beta*Z)[0])==1)
check('explicit scalar Bezout identity',s.expand(sigma*(v**3-v-1)+2*v*v*rho)==1)
for epsilon in (0,1):
    check('kernel first coordinate odd '+str(epsilon),s.Poly(s.expand((Z[0].subs(v,2*k+epsilon)-1)/2),k).domain==s.ZZ)
hatN=Ah*Bh-s.eye(6)
equal('hat cusp squared zero',hatN*hatN,s.zeros(6))
equal('actual beta vanishing on quotient nilpotent',beta*(Ap*Bp-s.eye(5)),s.zeros(1,5))
equal('beta kills actual quotient image',beta*Xn,s.zeros(1,2))
check('L inverse is integral',all(z.q==1 for z in L.inv()))

# Reconstruct the additional integral coinvariant arithmetic independently.
row=s.Matrix([[5,q,q,q,q]])
equal('A coinvariant row morphism',row*Ap,row)
kappa=s.simplify(row*(Bp-s.eye(5))/q)
check('q is prime to5 on every residue',[int(q.subs(v,j))%5 for j in range(5)]==[1,1,3,2,3])
check('kappa difference gives2v',s.expand(kappa[2]-kappa[1])==2*v)
check('kappa fourth entry gives cubic',s.expand(kappa[3])==-(v**3-v-1))
check('integral Euclidean identity for v and cubic',s.expand(v*(v*v-1)-(v**3-v-1))==1)
for epsilon in (0,1):
    check('cubic is odd '+str(epsilon),s.Poly(s.expand(((v**3-v-1).subs(v,2*k+epsilon)-1)/2),k).domain==s.ZZ)

diagnostics=[]
for value in range(-6,11):
    D=smith_normal_form(hatN.subs(v,value),domain=s.ZZ)
    nonzero=[abs(int(D[i,i])) for i in range(6) if D[i,i]]
    check('old diagnostic cusp range '+str(value),nonzero==[1,1,1])
    b=beta.subs(v,value);finite_matrix=Bp.subs(v,value).T-s.eye(5)
    before=torsion(finite_matrix);after=torsion(finite_matrix.row_join(b.T))
    check('finite extension index division '+str(value),before%after==0)
    diag={'v':value,'cusp_smith':nonzero,'finite_B_extension_order':before//after}
    # The producer's additional odd-coinvariant assertion is checked on
    # its entire diagnostic range, with the symbolic row proof above.
    raw=(Ap-s.eye(5)).row_join(Bp-s.eye(5)).subs(v,value)
    check('raw quotient coinvariant order '+str(value),torsion(raw)==int(q.subs(v,value)))
    diagnostics.append(diag)

out={'status':'PASS','checks':len(checks),'check_names':checks,
     'chronology':'new independent computation after target/old producer exposure; no prereading proof credit',
     'method':'new exact quotient maps, polynomial pencil coefficients, parity substitutions, integer minors and Smith indices; old producer not imported',
     'development_correction':'An initial structural-expression equality for anti-reciprocity failed although the polynomial difference is zero; it was corrected to exact cancellation. No mathematical formula changed.',
     'parity_data':parities,'detH':str(d),'detHprime':str(dp),
     'pencil_quadratic':str(s.factor(pencil.nth(2))),
     'kappa':[str(s.factor(z)) for z in kappa],
     'bounded_diagnostics':diagnostics,
     'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','checks','chronology','parity_data','bounded_diagnostics','source_sha256')},indent=2))
