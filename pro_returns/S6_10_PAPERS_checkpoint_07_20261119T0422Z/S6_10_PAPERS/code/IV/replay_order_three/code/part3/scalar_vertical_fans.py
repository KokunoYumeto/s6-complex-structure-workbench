#!/usr/bin/env python3
"""Exact actual-period and native-pair arithmetic for scalar vertical fans."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import json

n,J,e=s.symbols("n J e",integer=True)
checks=[]
def ck(name,expr):
    ok=all(s.simplify(x)==0 for x in expr) if isinstance(expr,s.MatrixBase) else s.simplify(expr)==0
    assert ok,(name,expr)
    checks.append({"name":name,"pass":bool(ok)})
P=s.Matrix([[1,0],[n,1]])
B=s.diag(0,J)
ck("actual winding conjugation",P.inv()*B*P-s.Matrix([[0,0],[n*J,J]]))
ck("period basis is unimodular",P.det()-1)
l=s.Matrix([2*J*(1-n),0,2*J])
w=s.Matrix([0,1,-1]);d=s.Matrix([-2,-1,-1]);t=J
I=s.Matrix([t*w[i]+d[i]*(l[i]-t) for i in range(3)])
W=s.Matrix([t*w[i]-d[i]*(l[i]-t) for i in range(3)])
ck("actual circle trace",I-s.Matrix([-2*J+4*n*J,2*J,-2*J]))
ck("actual derivative trace",W-s.Matrix([2*J-4*n*J,0,0]))
pairs={}
for i,weight in ((1,1),(2,-1)):
    V=I[i]/weight
    delta=(W[i]-W[0])/weight
    right=(delta-V)/2
    left=-V-right
    native=s.Matrix([(left+2*J)/2,right/2])
    expected=s.Matrix([J*(1-n),J*(n-1)]) if i==1 else s.Matrix([n*J,-n*J])
    ck(f"C{i} actual single native pair",native-expected)
    pairs[str(i)]=[str(x) for x in native]
A0=s.symbols("A0",integer=True)
A=A0-J*n*(n-1)/2
ck("C2 exact recurrence",A.subs(n,n+1)-A+n*J)
ck("C1 inverse exact recurrence",A.subs(n,n-1)-A-(n-1)*J)
ck("initial value",A.subs(n,0)-A0)
ck("reflected first fan equality",A.subs(n,1)-A0)
u=s.Matrix([1,n]);diag=s.Matrix([1,n-1]);vertical=s.Matrix([0,1])
ck("C2 flip diagonal replacement",u+vertical-s.Matrix([1,n+1]))
ck("C1 flip diagonal replacement",diag-vertical-s.Matrix([1,n-2]))
a0,a1,c0,c1,X,Y=s.symbols("a0 a1 c0 c1 X Y",nonzero=True)
for label,row in (("C1",(a0,Y*a1,c0/(X*Y),X*c1)),("C2",(a0,a1/(X*Y),X*c0,Y*c1))):
    ck(label+" full Cox height",s.prod(row)-a0*a1*c0*c1)
samples=[]
for j in range(-8,9):
 for nn in range(-12,13):
    samples.append({"J":j,"n":nn,"C1":[j*(1-nn),j*(nn-1)],"C2":[nn*j,-nn*j],"relative_class":(-j*nn*(nn-1)//2)%28})
out={"status":"PASS","utc":datetime.now(timezone.utc).isoformat(),"scope":"Working exact vertical-edge scalar-family morphism calculation; no arbitrary-fan formula.","checks":checks,"check_count":len(checks),"native_pairs":pairs,"class":"A0-J*n*(n-1)/2 mod28","samples":samples,"proof":"notes/part3_scalar_vertical_fans_working.md"}
p=Path(__file__).resolve().parent
(p/"scalar_vertical_fans.json").write_text(json.dumps(out,indent=2)+"\n")
print(f"PASS {len(checks)} symbolic identities and {len(samples)} signed instances")
