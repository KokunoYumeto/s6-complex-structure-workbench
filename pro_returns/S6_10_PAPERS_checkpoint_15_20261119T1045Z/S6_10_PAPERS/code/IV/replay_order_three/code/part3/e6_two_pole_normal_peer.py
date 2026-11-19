"""Independent check of the complete common-ball three-period map."""
from pathlib import Path
import json
import sympy as S

u,v,a,b,d,z=S.symbols('u v a b d z', nonzero=True)
s=u*b-v*a
T=b*(u*u*a-u-v)
E=b+a-u*a*a
F=u*u*a-u-v
K=b*(b+a)-a*a*(2*u*b-v*a)
p=S.Matrix([-d*a/K,-d/E,(s*E*E+a*F*K)/(d*E),F*K*K/(d*E*E)])
checks=[]
def ck(name, expr):
    value=S.factor(expr)
    assert value==0,(name,value)
    checks.append(name)

ck('K identity',K-b*E+s*a*a)
ck('F identity',E*E-E*a-K-a*a*a*F)
ck('source s',p[0]*p[3]-p[1]*p[2]-s)
ck('source t',p[3]*(p[0]*p[0]*p[2]-p[0]-p[1])-T)
for i in range(4):
    ck('circle '+str(i),p[i].subs({u:z*u,v:z*v,a:a/z,b:b/z},simultaneous=True)
       -(z if i<2 else 1/z)*p[i])
ck('charged canonical determinant',p.jacobian([u,v,a,b]).det(method='domain-ge')-1)
out={'status':'PASS','count':len(checks),'checks':checks,
     'scope':'Full normal map and canonical determinant; the d(s,t) derivative is retained by source invariance and the rank-one determinant formula.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
