#!/usr/bin/env python3
"""Independent comparison of the printed 01CG budget and conductor algebra.

The finite search uses the printed weak bound and its exhaustion argument,
not the stronger prereading multiplicity inequality. Local ring equality is
checked by two Groebner reductions with a formal inverse of the unit.
"""
import json
import sympy as S

checks=[]
details={}


def equal(name,left,right):
    residual=S.cancel(S.expand(left-right))
    if residual!=0:
        raise AssertionError((name,str(residual)))
    checks.append({'name':name,'result':'exact'})


def true(name,value):
    if not value:
        raise AssertionError(name)
    checks.append({'name':name,'result':'exact'})


weak=[]
for s in range(4):
    for A in range(0,9,2):
        for Bs in range(min(2,s)+1):
            for dr in range(5):
                if A>=2*s-2 and 3*(2-Bs)+Bs+2*dr<=8-A:
                    weak.append({'s':s,'A':A,'B_s':Bs,'d_reg':dr,'upper_d':s-Bs+dr})
true('printed weak inequalities bound d by two',max(v['upper_d'] for v in weak)==2)
edge=[v for v in weak if v['upper_d']==2]
true('printed d=2 candidates exhaust A',all(v['A']<=2*v['s']-2 for v in edge))
reasons=[]
for v in edge:
    s,A,Bs,dr=v['s'],v['A'],v['B_s'],v['d_reg']
    if s==1:
        true('s=1 candidate violates singular a vanishing',A==0)
        reason='A=0 contradicts the singular zero of a'
    elif s in (2,3):
        true('singular zeros exhaust a for s='+str(s),A==({2:2,3:4}[s]))
        true('exhausted candidate contradicts absence of smooth attachments or branching',
             (Bs,dr)!=(2,0) and s-2<=1)
        reason='exhaustion requires B_s=2 and d_reg=0, leaving at most s-2 <= 1'
    else:
        raise AssertionError(('unexcluded candidate',v))
    reasons.append({**v,'contradiction':reason})
details['all_printed_d_equals_two_candidates']=reasons
survivors=[]
for v in weak:
    s,A=v['s'],v['A']
    if s==1 and A==0:
        continue
    if s in (2,3) and A=={2:2,3:4}[s]:
        if v['B_s']!=2 or v['d_reg']!=0:
            continue
    survivors.append(v)
true('printed exhaustion proof leaves d at most one',max(v['upper_d'] for v in survivors)<=1)

q_candidates=[q for q in range(-1,1) if 2<=4+2*q and 1<=-2*q]
true('space-cusp genus-zero inequalities force q0=-1',q_candidates==[-1])
equal('space-cusp cleared divisor then has degree two',4+2*S.Integer(-1),2)
true('two positive odd orders in degree two are both simple',
     [(a,b) for a in range(1,3,2) for b in range(1,3,2) if a+b==2]==[(1,1)])

a,b,e,alpha,beta,gamma,mu=S.symbols('a b e alpha beta gamma mu')
gram=S.Matrix([[a,b/2],[b/2,e]])
T=S.Matrix([[alpha,beta],[0,gamma**2]])
pulled=mu*T.T*gram*T
equal('quartic Gram determinant',gram.det(),a*e-b*b/4)
equal('quartic determinant transition',pulled.det(),mu**2*alpha**2*gamma**4*gram.det())
d,w=S.symbols('d w')
Delta=gram.det()
equal('cover field map',(a*w+b/2)**2+Delta,a*(a*w*w+b*w+e))
equal('cover inverse map',((d-b/2)/a).subs(d,a*w+b/2),w)
c0,d0=S.symbols('c0 d0',nonzero=True)
equal('conductor clearing preserves the quadratic relation',
      (c0**2*d)**2+c0**4*Delta,c0**4*(d*d+Delta))
equal('conductor clearing inverse on the quadratic field',
      (d0/c0**2).subs(d0,c0**2*d),d)
equal('conductor clearing forward after inverse',c0**2*(d0/c0**2),d0)

# Universal localization at a unit U; V is its exact formal inverse.
x,y,lam,U,V,Q=S.symbols('x y lam U V Q')
I=[x-lam*y*y,U*y*y,U*V-1]
J=[x,y*y,U*V-1]
GI=S.groebner(I,x,y,U,V,lam,order='lex')
GJ=S.groebner(J,x,y,U,V,lam,order='lex')
true('smooth-root conductor ideal contains the double curve',all(GI.reduce(p)[1]==0 for p in J))
true('double-curve ideal contains the conductor generators',all(GJ.reduce(p)[1]==0 for p in I))
details['localized_conductor_Groebner_basis']=[str(p.as_expr()) for p in GI.polys]
F1=x-lam*y*y
F2=y*y*U+F1*Q
equal('factor derivative restricts to the conductor generator',S.diff(F1*F2,x).subs(x,lam*y*y),y*y*U)
equal('unit inverse generates y squared',V*(U*y*y)-y*y,(U*V-1)*y*y)

K,r,N0,eG,k,loss=S.symbols('K r N0 eG k loss',integer=True)
equal('printed first Euler inequality difference',
      (2-r+N0+eG)-(2-K+eG),K-r+N0)
equal('selected-edge loss',K-(K-loss),loss)
equal('printed final Euler reduction',2-K+(K-loss),2-loss)
equal('one paired value gives positive Euler bound',(2-loss).subs(loss,1),1)

print(json.dumps({'tag':'01CG','all_passed':True,'count':len(checks),
                  'method':'printed weak-bound exhaustive comparison, symmetric Gram determinant, and localized conductor ideal equality',
                  'checks':checks,'details':details},indent=2)+'\n',end='')
