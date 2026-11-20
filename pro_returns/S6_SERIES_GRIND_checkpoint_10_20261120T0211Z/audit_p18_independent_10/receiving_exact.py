"""Post-freeze target-comparison assertions; not represented as pre-reading work."""
import sympy as s
from itertools import combinations
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
A=s.Matrix([[1,0,0,1,-1,1],[0,1,-1,-1,1,0],[0,1,0,-1,0,0],[0,2,-1,-1,0,1],[0,2,0,-1,0,0],[0,1,1,-1,0,0]])
B=s.Matrix([[1,0,0,0,0,0],[0,0,-1,0,1,0],[0,0,-1,0,0,1],[0,0,-1,0,0,0],[0,1,-1,0,0,0],[0,0,-1,1,0,0]])
Cf=s.Matrix([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
Cg=s.Matrix([[0,0,0,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
Q=s.eye(6);Q[:,0]=s.ones(6,1);pi=Q.inv()[1:,:]
k=s.Matrix([[1,-1,1,1,-1,1]])
pairs=list(combinations(range(4),2))
def wedge(a,b):return s.Matrix([a[i]*b[j]-a[j]*b[i] for i,j in pairs])
D=Cf*Cg.inv()-s.eye(4);N=(B*A).inv()-s.eye(6);NW=N[1:,1:]
a=s.Matrix(s.symbols('a0:4'));b=s.Matrix(s.symbols('b0:4'))
w=wedge(a,D*b);p=pi*w;lift=s.Matrix.vstack(s.zeros(1,1),p)
checks={}
def check(name,condition):
 assert condition,name
 checks[name]=True
check('target scalar identity',s.expand((N*lift)[0]-a[0]*b[0])==0)
check('target contraction identity',s.expand((k*w)[0]-a[0]*b[0])==0)
check('target quotient kernel identity',(NW*p).applyfunc(s.expand)==s.zeros(5,1))
U=s.Matrix.hstack(*[pi*wedge(a,s.eye(4)[:,j]) for j in range(4)])
check('rank two quotient image minor',s.factor((NW*U).extract([2,3],[2,3]).det())==a[0]**2)
check('rank two quotient image bound',NW.rank()==2)
pa=pi*wedge(a,D*a)
check('kernel generator nonzero contraction',s.expand((k*wedge(a,D*a))[0]-a[0]**2)==0)
check('kernel generator central lift image',(N*s.Matrix.vstack(s.zeros(1,1),pa)-s.Matrix([a[0]**2,0,0,0,0,0])).applyfunc(s.expand)==s.zeros(6,1))
# Verify that the pre-reading artifacts have not changed.
root=Path(__file__).parent
freeze=json.loads((root/'freeze_manifest.json').read_text())
for name,digest in freeze['sha256'].items():check('frozen unchanged: '+name,hashlib.sha256((root/name).read_bytes()).hexdigest()==digest)
target=Path('audit_root/P18_fresh_inputs_09/target_P18_receiving_10.tex')
check('received target hash',hashlib.sha256(target.read_bytes()).hexdigest()=='0a397ce2ac20d36abfdf2117ff6b78d914f5fe65cda20ac7b337aba467c882c4')
result={'utc':datetime.now(timezone.utc).isoformat(),'scope':'Post-freeze target comparison only; full proof and its original code were frozen before reading target.','checks':checks,'status':'PASS','target_sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
(root/'receiving_exact_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
