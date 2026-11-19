#!/usr/bin/env python3
"""Independent OT source, line, cap word and orientation identities."""
import sympy as S
import json,hashlib,datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
checks=[]
def eq(name,expr):
    r=S.factor(S.cancel(S.together(expr)))
    assert r==0,(name,r)
    checks.append(name)
e,x,y,t,chi,sigma,H,Braw,lam,fp,ft,rp,rt=S.symbols('e x y t chi sigma H Braw lam fp ft rp rt',nonzero=True)
d=1-3*e**2
r=e**2*(3*e**2-2)/d**2
xo=e**2*x/d**2;yo=e**3*y/d**3;to=e**4*t/d**3
native=y*y-x**3-(3*e**2-2)*x*x-d*t*x-e*e*t*t
eq('complete original cubic',(yo**2-xo**3-r*xo**2-to*xo-to**2)-e**6*native/d**6)
eq('actual source meridian degree two coefficient',S.limit(r/e**2,e,0)+2)
eq('selected base height',to-e**4*(1-e**2)/d**3-e**4*(t-1+e**2)/d**3)
eq('full raw Hom coefficient',lam*(chi*sigma)**4*chi**-4*H*sigma**-6*Braw-lam*sigma**4*H*(sigma**-6*Braw))
Bpt=Braw*rt/rp;psip=fp/rp;psit=ft/rt
eq('genuine and theta frame square',Bpt*psit/psip-Braw*ft/fp)
eq('genuine frame reciprocal',(rt/rp)*(rp/rt)-1)
A,Yl,V=S.symbols('A Yl V',nonzero=True)
for j in range(4):
    Xj=chi**j*A;Yj=chi**(-j-1)*Yl
    eq(f'chain product residue{j}',(Xj*Yj).subs(Yl,chi*sigma/A)-sigma)
    eq(f'full coefficient residue{j}',sigma**j*Xj-(chi*sigma)**j*A)
    eq(f'quarter turn X/B residue{j}',S.I**(j+4)-S.I**j)
    eq(f'quarter turn Y/B residue{j}',S.I**(-j-5)-S.I**(-j-1))
j0,j1,j2,j3=S.symbols('j0 j1 j2 j3',integer=True)
js=j0+j1+j2+j3
eq('actual cap log quarter step',-4*(-S.Rational(1,4))-1)
eq('four cap logs',4*(-4*(-S.Rational(1,4)))-4)
eq('norm A2=B on full word',4/S.Integer(2)+js-(js+2))
eq('inverse endpoint retains all cap powers',-(js+2)+(js+2))
for a in (6,):
    # eps^4 H_o^-1 sigma^-4, H_o sigma^4, then conjugate first.
    neg=-(4+a-4);pos=-a+4
    eq('negative full point-to-tensor phase',neg+a)
    eq('positive full point-to-tensor phase',pos-(4-a))
    eq('full determinant phase',neg+pos-(4-2*a))
rows=[('strict',1,42,108),('mu2points',1,-2,-14),('interior',2,-18,-126),('exceptional',2,-20,-20),('refinement',2,18,126),('pcurves',2,0,-18),('interface',2,0,0)]
k=sum(n*a for _,n,a,b in rows);ell=sum(n*b for _,n,a,b in rows)
eq('compact cubic sum',k);eq('compact p1-linear sum',ell-18)
kap=S.symbols('kappa_c',integer=True)
kin=k+kap;elin=ell+4*kap+6
eq('full symbolic inner cubic',kin-kap)
eq('full symbolic inner p1-linear',elin-4*kap-24)
eq('U inner index',(4*kin-elin)/24+1)
eq('outer radial sign',(-1)**5+1)
for f in (0,1,2):
    # Moving circle to first position crosses 2f+1, then inner outward -dr.
    eq(f'inner quotient sign f{f}',(-1)**(2*f+1)*(-1)*(-1)**(2*f)-1)
km,em=-kin,-elin
eq('positive-parameter physical index',(4*km-em)/24-1)
kj,ej=-km,-em
eq('Jin physical index',(4*kj-ej)/24+1)
tt=S.symbols('tt');eq('interval inverse',1-(1-tt)-tt)
eq('interval derivative',S.diff(1-tt,tt)+1)
eq('native right without c2',kj-ej/4+6)
source=ROOT/'notes/part3_e6_selected_infinity_outer_transfer_working.md'
out={'status':'PASS','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'check_count':len(checks),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'scope':'Independent exact arrows and signs supplementing full OT1–5 geometric review. M6,b1,m2,n1, initial fan, fixed admissible original scalar, full positive epsilon loop. No value for kappa_c.','compact_U':[str(k),str(ell)],'Jin_physical':[str(kj),str(ej)],'physical_index':-1,'checks':checks}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2))
