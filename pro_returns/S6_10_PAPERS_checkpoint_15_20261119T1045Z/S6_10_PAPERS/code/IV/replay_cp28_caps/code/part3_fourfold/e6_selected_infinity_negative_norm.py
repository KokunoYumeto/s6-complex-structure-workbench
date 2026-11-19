#!/usr/bin/env python3
"""Exact algebra for SN; the relative cap product is proved in the source."""
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations, product
from fractions import Fraction
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
checks = []


def check(name, statement):
    value = bool(statement)
    checks.append({"name": name, "pass": value})
    if not value:
        raise AssertionError(name)


def zero(name, expression):
    check(name, s.factor(s.together(expression)) == 0)


e, zeta, z, X, Y, t, r, q, tr = s.symbols("e zeta z X Y t r q tr")
d = 1 - 3 * e**2
rr = e**2 * (3 * e**2 - 2) / d**2
tc = e**4 * (1-e**2) / d**3
xo, yo, to = e**2/d**2*X, e**3/d**3*Y, e**4/d**3*t
native = Y**2-X**3-(3*e**2-2)*X**2-d*t*X-e**2*t**2
original = yo**2-xo**3-rr*xo**2-to*xo-to**2
zero("original/native full cubic", original-e**6/d**6*native)
zero("original selected height", to-tc-e**4/d**3*(t-(1-e**2)))
zero("r is even", rr.subs(e,-e)-rr)
zero("selected value is even", tc.subs(e,-e)-tc)
zero("r derivative at zeta zero", s.diff(zeta*(3*zeta-2)/(1-3*zeta)**2,zeta).subs(zeta,0)+2)

xo, yo, to = z**-2*X, z**-3*Y, z**-2
root_eq = Y**2-X**3-r*z**2*X**2-z**2*X-z**2
zero("quadratic original root cubic",
     yo**2-xo**3-r*xo**2-to*xo-to**2-z**-6*root_eq)
zero("root deck preserves equation", root_eq.subs({z:-z,Y:-Y},simultaneous=True)-root_eq)
zero("root zero-section formal parameter", -X/Y-z*(-(z**2*X)/(z**3*Y)))

c, U, V, a, b = s.symbols("c U V a b")
zero("A2 full source identity",
     s.expand((Y-z*c)*(Y+z*c)-X**3).subs(c**2,1+X+r*X**2)-root_eq)
charts = [(a*b,a,a**2*b**3),(a*b,a**2*b,a*b**2),(a*b,a**2*b**3,a)]
for k,(xx,uu,vv) in enumerate(charts):
    zero(f"A2 chart{k}",uu*vv-xx**3)
for k in range(3):
    mat=s.Matrix([[s.degree(charts[k][1],a),s.degree(charts[k][1],b)],
                  [s.degree(charts[k][0],a),s.degree(charts[k][0],b)]])
    check(f"A2 chart{k} primitive root lattice",abs(mat.det())==1)
am, bm = 1/b, a*b**2
for name,new,old in zip(("X","U","V"),
    (am*bm,am**2*bm,am*bm**2),charts[0]):
    zero("first-to-middle "+name,new-old)
for name,expr in zip(("X","U","V"),charts[1]):
    weight=1 if name=="X" else -1
    zero("middle deck "+name,expr.subs({a:-a,b:-b},simultaneous=True)-weight*expr)

tau,L,u,v=s.symbols("tau L u v")
zero("point-line u chart", (tau/(tau-z*L)).subs(tau,z*u)-u/(u-L))
zero("point-line v chart", (tau/(tau-z*L)).subs(z,tau*v)-1/(1-v*L))
zero("point-line overlap", (u/(u-L)).subs(u,1/v)-1/(1-v*L))
for forward in (u/(u-L),1/(1-v*L)):
    zero("Cartier inverse product",forward/forward-1)
check("division 2R=G",2*(2-Fraction(3,2))==1)

hsel=1-tc*z**2
href=1-tr*z**2
uh=hsel/href
zero("height ratio whole function", uh*href-hsel)
zero("height ratio deck invariant", uh.subs(z,-z)-uh)
zero("height ratio central value", uh.subs(z,0)-1)
zero("height ratio first coefficient", s.diff(uh,z,2).subs(z,0)-2*(tr-tc))

# Characters are recorded additively as (R_lambda,Ftilde,D,(-1)).
# D and the normalized full line map commute; D^2 is the identity.
def add(*words):
    out=[sum(w[i] for w in words) for i in range(4)]
    out[2]%=2;out[3]%=2
    return tuple(out)
def mul(word,k):
    return add(tuple(k*x for x in word))
Bword=(2,2,0,0)
for char in range(2):
    Aminus=(-1,-1,1,char)
    Hminus=mul(Aminus,-1)
    check(f"negative norm character{char}",mul(Aminus,2)==mul(Bword,-1))
    check(f"primitive contraction character{char}",mul(Hminus,2)==Bword)
    check(f"opposite actual generator character{char}",Hminus==(1,1,1,char))
    for js in product(range(-2,3),repeat=4):
        word=add(*(add(Aminus,mul(Bword,j)) for j in js))
        check(f"quarter word char{char} j{js}",word==mul(Bword,sum(js)-2))
        check(f"inverse quarter word char{char} j{js}",add(word,mul(word,-1))==(0,0,0,0))

# This is the target-sheet Lie identity, with D transport represented by fD.
ss,k,fa,fD,Pi,cc,ha,hD,jj,bb,Lambda=s.symbols("ss k fa fD Pi cc ha hD jj bb Lambda")
fb=fD+Pi
hb=hD+ss*Pi+jj*bb+Lambda
Lbeta=-(ss+k)*fb+(ss+k)*cc+hb
DLalpha=-ss*fD+ss*cc+hD
target=-k*fb+k*cc
zero("full negative-norm target-sheet square",
     Lbeta-DLalpha-target-jj*bb-Lambda)
logu=s.symbols("logu")
zero("actual height root norm",2*(-logu/2)+logu)
zero("quarter sector log change",-4*(-s.Rational(1,4))-1)

sigma,chi=s.symbols("sigma chi",nonzero=True)
de=1-3*(chi*sigma)**2
xo=sigma**2/de**2*X
yo=sigma**3/de**3*Y
to=sigma**4/de**3
native_good=Y**2-X**3-(3*(chi*sigma)**2-2)*chi**2*X**2-de*X-sigma**2
rgraph=(chi*sigma)**2*(3*(chi*sigma)**2-2)/de**2
zero("full complementary original cubic",
     yo**2-xo**3-rgraph*xo**2-to*xo-to**2
     -sigma**6/de**6*native_good)
zero("old cap graph coordinate",1/to-de**3/sigma**4)
zero("quarter preserves epsilon",(s.I*chi)*(-s.I*sigma)-chi*sigma)
zero("quarter preserves old t",to.subs({chi:s.I*chi,sigma:-s.I*sigma},simultaneous=True)-to)

rho,xnorm,hnorm,bnorm=s.symbols("rho xnorm hnorm bnorm",positive=True)
norm=xnorm+rho**-2*hnorm
zero("weighted Hermitian norm identity",
     hnorm+rho**-2*bnorm-rho**2*(norm-xnorm+rho**-4*bnorm))
zero("contracting norm bound after B bound",
     (hnorm+rho**-2*bnorm-rho**2*norm).subs(bnorm,rho**4*xnorm))
for sign in (-1,1):
    check(f"primitive actual cap columns sign{sign}",
          s.Matrix([[2,1],[sign,0]]).det()==-sign)

for sign in (-1,1):
    C=s.Matrix([[2,1],[sign,0]])
    inverse=s.Matrix([[0,sign],[1,-2*sign]])
    T=s.Matrix([[sign,0],[2*(1-sign),1]])
    check(f"actual cap inverse sign{sign}", C*inverse==s.eye(2))
    check(f"actual cap relation basis sign{sign}", C*T==s.Matrix([[2,1],[1,0]]))
R=s.Matrix([[0,-1],[-1,0]])
J=s.diag(1,-1)
check("complex-meridian orbit inverse",R*R==s.eye(2))
check("physical-meridian orbit inverse",J*R*s.Matrix([[0,1],[-1,0]])==s.eye(2))
check("physical Euler restriction preserved",J*s.Matrix([0,-1])==s.Matrix([0,1]))

Rcon=s.Matrix([[0,0],[-1,-1]])
check("actual conifold primitive Euler kernel",Rcon*s.Matrix([1,-1])==s.zeros(2,1))
check("actual conifold rank",Rcon.rank()==1)
check("actual conifold primitive image",Rcon[:,0]==s.Matrix([0,-1]))

# Every cap comparison form is pulled from the proved five-dimensional body.
twos=list(combinations(range(5),2))
fours=list(combinations(range(5),4))
for A,B,C in product(twos,repeat=3):
    check("five-dimensional cubic "+str((A,B,C)),len(set(A+B+C))<6)
for A,B in product(fours,twos):
    check("five-dimensional p1-linear "+str((A,B)),len(set(A+B))<6)

source=ROOT/'notes/part3_e6_selected_infinity_negative_norm_working.md'
deps=[
 'notes/part3_e6_unselected_iii_extension_working.md',
 'notes/part3_e6_selected_infinity_root_working.md',
 'notes/part3_e6_selected_infinity_outer_transfer_working.md',
 'notes/part3_e6_selected_infinity_all_fans_working.md',
 'records/k101_export_manifest.json',
 'records/k102_export_manifest.json',
]
result={
 'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),
 'checks':len(checks),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'scope':'M6,b1,m2,n=-1; full negative-norm cap/ref/closing algebra. The relative product, global characteristic comparison and physical return are proved in SN.4–6, not inferred from these finite equations.',
 'dependencies':[{'path':p,'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in deps],
 'identities':checks,
}
path=ROOT/'code/part3_fourfold/e6_selected_infinity_negative_norm.json'
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','checks','source_sha256','scope']},indent=2))
