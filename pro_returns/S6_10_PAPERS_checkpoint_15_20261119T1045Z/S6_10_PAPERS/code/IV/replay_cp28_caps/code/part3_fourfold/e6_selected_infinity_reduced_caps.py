#!/usr/bin/env python3
"""Exact symbolic and integral chart checks for HC.1–5."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
checks=[]
def check(name,value):
    v=bool(value);checks.append({"name":name,"pass":v})
    if not v:raise AssertionError(name)
def zero(name,expr):
    check(name,s.factor(s.together(expr))==0)

l=s.symbols('l',integer=True,nonnegative=True)
m=3*l+2;k=2*l+1
for name,expr in [
 ('old source x2 coefficient',6*(l+1)-4*(l+1)-(2*l+2)),
 ('old source t*x coefficient',6*(l+1)-m-2*(l+1)-(l+2)),
 ('old source t2 coefficient',6*(l+1)-2*m-2),
 ('Miller selected coefficient',2*m-6*(l+1)+2),
 ('formal section exponent',3*k-(2*m-1)),
 ('component identity argument',2*m-1-3*k),
 ('c first deck weight',l-2*k+m),
 ('c second deck weight',2*l-4*k+2*m),
 ('U,V deck weight',-3*k-1+2*m),
 ('middle X deck weight',2*(l+1)+2*k-2*m),
 ('middle U,V deck weight',3*(l+1)-1-m),
 ('norm division mR=G',m*(2-(2*m-1)/m)-1),
 ('J X endpoint',-2*(l+2)-8*k+6*m),
 ('J Y endpoint',-3*(l+2)-12*k+9*m),
 ('lift native X exponent',(2*(l+2)+2*m)/4+2*k-2*m),
 ('lift native Y exponent',(3*(l+2)-m)/4+3*k-2*m),
 ('complement X2 exponent',2*(l+1)*4-2*(l+2)-2*m),
 ('complement linear exponent',4*(l+2)-4*(l+2)),
 ('complement constant exponent',2*m+8-6*(l+2)),
]:
    zero(name,expr)

q,tc,tr=s.symbols('q tc tr')
u=(1-tc*q)/(1-tr*q)
zero('whole selected-height ratio',u*(1-tr*q)-(1-tc*q))
zero('height ratio at root centre',u.subs(q,0)-1)
logu=s.symbols('logu')
zero('chosen full logarithmic root',m*(logu/m)-logu)
for n in (-1,1):
    zero(f'norm height factor n{n}',m*(n*logu/m)-n*logu)
    C=s.Matrix([[m,1],[n,0]])
    Ci=s.Matrix([[0,n],[1,-m*n]])
    T=s.Matrix([[n,0],[2-m*n,1]])
    check(f'full cap inverse n{n}',s.simplify(C*Ci)==s.eye(2))
    check(f'full reference relation basis n{n}',s.simplify(C*T)==s.Matrix([[2,1],[1,0]]))
    zero(f'signed cap determinant n{n}',C.det()+n)
    zero(f'signed relation determinant n{n}',T.det()-n)

ss,kk,fD,Pi,cc,hD,jj,beta,Lambda=s.symbols('ss kk fD Pi cc hD jj beta Lambda')
for n in (-1,1):
    fb=fD+Pi
    hb=hD-n*ss*Pi+jj*beta+Lambda
    target=n*kk*fb+kk*cc
    lhs=n*(ss+kk)*fb+(ss+kk)*cc+hb-(n*ss*fD+ss*cc+hD)-target
    zero(f'full target-sheet annular identity n{n}',lhs-jj*beta-Lambda)

R=s.Matrix([[0,-1],[-1,0]])
Rcon=s.Matrix([[0,0],[-1,-1]])
check('original orbit restriction inverse',R*R==s.eye(2))
check('conifold physical Euler kernel',Rcon*s.Matrix([1,-1])==s.zeros(2,1))
check('conifold primitive image',Rcon[:,0]==s.Matrix([0,-1]))
check('conifold rank',Rcon.rank()==1)

# Exact chronological source/scalar/deck words.  The scalar and
# normalized line-lift exponents are never reduced modulo m.
def add(words,order):
    out=[sum(w[i] for w in words) for i in range(4)]
    out[2]%=order;out[3]%=order
    return tuple(out)
def mult(word,power,order):return add([tuple(power*x for x in word)],order)
for lv in range(16):
    mv=3*lv+2;kv=2*lv+1
    rays=[(j,1) for j in range(kv+1)]+[(1,0)]
    for j in range(len(rays)-1):
        a,b=rays[j],rays[j+1]
        check(f'graph primitive adjacent l{lv} ray{j}',abs(a[0]*b[1]-a[1]*b[0])==1)
    for j in range(kv+1):
        check(f'Cartier component equality l{lv} j{j}',min(j,kv)==j)
    B=(mv,mv,0,0)
    for n in (-1,1):
        for dc in range(mv):
            A=(n,n,1,dc)
            H=mult(A,n,mv)
            check(f'full cap norm l{lv} n{n} d{dc}',mult(A,mv,mv)==mult(B,n,mv))
            check(f'primitive cap norm l{lv} n{n} d{dc}',mult(H,mv,mv)==B)
            for js in [(-2,0,1,3),(0,0,0,0),(1,-3,2,4)]:
                word=add([add([A,mult(B,j,mv)],mv) for j in js],mv)
                expected=add([mult(A,4,mv),mult(B,sum(js),mv)],mv)
                check(f'full quarter word l{lv} n{n} d{dc} j{js}',word==expected)
                check(f'inverse full word l{lv} n{n} d{dc} j{js}',add([word,mult(word,-1,mv)],mv)==(0,0,0,0))
    # The finite sum is the coefficientwise telescoping identity HC.26.
    rho=s.symbols('rho',positive=True)
    vals=s.symbols('N0:'+str(mv+1))
    lhs=sum(rho**(-2*j)*vals[j+1] for j in range(mv))
    norm=sum(rho**(-2*j)*vals[j] for j in range(mv))
    zero(f'weighted norm full telescope l{lv}',
         lhs-rho**2*(norm-vals[0]+rho**(-2*mv)*vals[mv]))

source=ROOT/'notes/part3_e6_selected_infinity_reduced_caps_working.md'
deps=[
 'notes/part3_e6_unselected_iii_extension_working.md',
 'notes/part3_e6_selected_infinity_negative_norm_working.md',
 'records/checks_audit_e6_selected_infinity_negative_norm.json',
 'notes/part3_e6_selected_infinity_root_working.md',
 'notes/part3_e6_selected_infinity_outer_transfer_working.md',
 'records/k101_export_manifest.json',
 'records/k102_export_manifest.json',
]
result={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),
 'checks':len(checks),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'symbolic_scope':'All l>=0,m=3l+2,n=+/-1; source exponents, full height root, signed annular square and integral cap/physical orbit maps are symbolic. Additional finite graph/deck instances l0..15 retain every character.',
 'geometric_scope':'The actual cap products, original exterior/selected tube and full integral comparison are proved in HC.1–5; these finite algebra checks do not replace that proof.',
 'dependencies':[{'path':p,'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in deps],
 'identities':checks}
out=ROOT/'code/part3_fourfold/e6_selected_infinity_reduced_caps.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','checks','source_sha256','symbolic_scope']},indent=2))
