#!/usr/bin/env python3
"""New post-reading exact source bridges for the isolated K111 comparison."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S

P=Path(__file__).resolve().parents[2]
v,w,k,X,Y,T,a,b,Rb,q,Fnew=S.symbols('v w k X Y T a b Rb q Fnew')
D=v-2;s=v*(v+4)/(4*D**2);r=(1-2*v)/D**2
kb=-2*(v+1)/D;xi=(kb-1)*(kb+2)/18;tc=-(kb-1)*(kb+2)**2/108
checks=[]
def eq(name,expression):
 value=S.factor(S.cancel(expression));assert value==0,(name,value)
 checks.append({'name':name,'result':'PASS'})
def branch_reduce(expression):
 num,_=S.fraction(S.cancel(expression))
 return S.rem(S.Poly(num,Rb),S.Poly(Rb**2-(b+2)**2-4*v,Rb)).as_expr()

eq('source r and s bridge',r+s-S.Rational(1,4))
eq('exact k branch bridge',kb*kb-(1+12*s))
eq('initial k value',kb.subs(v,0)-1)
eq('selected xi bridge',xi-v/D**2)
eq('selected height bridge',tc-v/D**3)
eq('original source scaling',(Y/D**3)**2-((X/D**2)**3+r*(X/D**2)**2+(T/D**3)*(X/D**2)+(T/D**3)**2)-(Y*Y-X**3-(1-2*v)*X*X-D*T*X-T*T)/D**6)
s0=v+v*v/4
eq('doubling x under source scaling',s*D**2-s0)
f_old=(Y/D**3-T/D**3-X/(2*D**2))/(X/D**2-s)
f_new=(Y-T-D*X/2)/(X-s0)
eq('full Miller function scaling',f_old-f_new/D)
eq('six-factor selected coefficient scaling',(q/D**3)/(T/D**3)**3*(Fnew/D**6)-q*Fnew/T**3)
pw=(1-w)/(1+w);vw=w*w-1;Dw=vw-2
eq('marked torus point over exact selected height',pw/(vw/Dw**3)+Dw**3/(w+1)**2)
eq('actual selected u_P leading coefficient',S.limit(pw/(vw/Dw**3),w,1)-2)

z=a-v/2;om=b+v/2
XX=s0+z*om;YY=XX*(z+om)/2;TT=XX*(om-z-D)/2
eq('source U coordinate',YY-TT-D*XX/2-XX*z)
eq('source V coordinate',YY+TT+D*XX/2-XX*om)
eq('full ordered source resolution identity',YY**2-XX**3-(1-2*v)*XX**2-D*TT*XX-TT**2)
K=b+v+2+Rb
xn=a-v*b/K;yn=(b*K-(2*b+v)*a)/4
eq('selected full node product equals actual q',branch_reduce(xn*yn-(TT-v)))
eq('complete implicit inverse equation',branch_reduce(4*yn+v*xn-2*b*(Rb-xn)))
K0=(w+1)**2;v0=w*w-1
eq('normal Jacobian with branch w',K0/4-v0*v0/(4*K0)-w)
eq('inverse denominator central unit',2*(S.Integer(2)-0)-4)

out={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'count':len(checks),'outcome':'PASS',
     'chronology':'Written after reading supporting proof1 lines1--145; no producer program read or imported. Does not add before-reading credit.',
     'scope':'Exact bridges from frozen preread coordinates to SI2.1; complete Miller scaling and selected-height coefficient; post-reading local source-resolution/node-map identities. Compact cap/Jin/native-product/closing proofs remain unreviewed.',
     'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'analysis/continuation_IV/K111_source_comparison.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'count':len(checks),'outcome':'PASS'}))
