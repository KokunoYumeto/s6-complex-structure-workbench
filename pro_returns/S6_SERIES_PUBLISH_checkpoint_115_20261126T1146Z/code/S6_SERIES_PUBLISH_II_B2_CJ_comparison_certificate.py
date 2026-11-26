#!/usr/bin/env python3
"""CJ printed boundary formula and push/pull relation comparison."""
import json
import sympy as s
checks=[]
def check(name,left,right,evidence):
    difference=s.simplify(left-right)
    assert difference==0,(name,difference)
    checks.append({'name':name,'passed':True,'difference':str(difference),'evidence':evidence})
nu,c,ell,n,b1,eps,h,q,ss=s.symbols('nu c ell n b1 eps h q ss')
eR=4-nu;eU=3*(4-eR);b1D=(nu+h)-(2+h)+c+ell;dD=n+2
check('Cover-complement Euler',eU,3*nu,'Threefold unramified cover of W minus R')
check('Boundary incidence first Betti number',b1D,nu-2+c+ell,'Two strict normalization vertices, h exceptional vertices, nu+h attaching edges, and c components')
eD=c-b1D+dD;eX=eU+eD;b2=eX-2+2*b1;rank=b2-dD+eps
check('Boundary Euler after resolution',eD,n+4-nu-ell,'c-b1(D)+d_D')
check('Resolved compact Euler',eX,n+4+2*nu-ell,'e(U)+e(D)')
check('Printed compact pairing rank',rank,2*nu+2*b1-ell+eps,'b2(X)-d_D+epsilon')
check('Connected-component cancellation',s.diff(rank,c),0,'No connected-boundary assumption enters the rank')
check('Frozen versus printed rank',rank.subs(b1,2*q)-(2*nu-ell+4*q),eps,'The frozen lower bound discards only the nonnegative relation count')
check('Positive-rank lower-gap formula',rank-(2*nu-2),2*b1+(2-ell)+eps,'b1>=0, ell<=2, epsilon>=0')
check('Disjoint-boundary formula',b1D.subs(c,2),nu+ell,'The c=2 case is included')
check('Connected-boundary formula',b1D.subs(c,1),nu-1+ell,'The c=1 case is included')

J=s.Matrix([[2,1],[1,0]])
classes=s.Matrix([[1,2],[ss,-ss]])
G=classes.T*J*classes
check('Two branch classes sum to 3xi',(classes*s.Matrix([1,1]))[0],3,'Horizontal degrees 1 and 2')
check('No fibre part in total branch',(classes*s.Matrix([1,1]))[1],0,'R1+R2=3xi')
check('Base class determinant',classes.det(),-3*ss,'epsilon=1 precisely when ss=0')
check('Base intersection determinant',G.det(),-9*ss**2,'Restriction of the ruled-surface pairing')
check('Dependent-class kernel first entry',(classes.subs(ss,0)*s.Matrix([2,-1]))[0],0,'2R1-R2=0')
check('Dependent-class kernel second entry',(classes.subs(ss,0)*s.Matrix([2,-1]))[1],0,'Same exact relation')
check('Total branch pullback square',3*(s.Matrix([[3,0]])*J*s.Matrix([3,0]))[0],54,'Degree-three pullback')

p0,p1,a00,a01,a10,a11=s.symbols('p0 p1 a00 a01 a10 a11',nonzero=True)
E=s.diag(-p0,-p1);A=s.Matrix([[a00,a01],[a10,a11]])
T=s.eye(4);T[:2,2:]=-A/3;T[2:,2:]=s.eye(2)/3
orth=s.diag(E,3*G);boundary=T.T*orth*T
alpha=s.Matrix([2,-1]);lift=(A*alpha/3).col_join(alpha)
for i,value in enumerate(boundary.subs(ss,0)*lift):check('Lifted branch relation component '+str(i+1),value,0,'Pullback relation maps alpha to ((A alpha)/3,alpha); projection recovers alpha')
check('Boundary determinant with independent branch classes',boundary.det(),-p0*p1*ss**2,'The exceptional correction A cancels from the determinant')
check('Nonzero minor in the dependent case',boundary.extract([0,1,2],[0,1,2]).det().subs(ss,0),s.Rational(2,3)*p0*p1,'Exactly one relation remains when ss=0')

def h0_line(degree):return max(degree+1,0)
def h1_line(degree):return max(-degree-1,0)
check('Relative minus-one line H0',h0_line(-1),0,'Fibre O(-1) has no cohomology')
check('Relative minus-one line H1',h1_line(-1),0,'Fibre O(-1) has no cohomology')
check('Det N has no global sections',h0_line(-2),0,'R1 p_* O(-2)=det N=O(-2), so total H1 is zero')
check('Total minus-two line H2',h1_line(-2),1,'Confirms chi(O_W(-2))=1 used in the frozen proof')

print(json.dumps({'tag':'01CJ','method':'Independent normalization-incidence Euler derivation, symbolic exceptional-correction congruence and exact push/pull kernel, and the printed relative-cohomology dimensions.','checks':checks,'exact_checks':len(checks),'all_passed':True,'scope':'The two-exceptional-variable congruence verifies the symbolic block formula; the proof establishes the same invertible block transformation and relation-map isomorphism for arbitrary n.'},indent=2))
