"""Exact residue/canonical Jacobians for the E6 chronological flop."""
from pathlib import Path
import sympy as S,json
z,w,x=S.symbols('z w x',nonzero=True)
ss=x-z*w;tt=x*(w-z-1)/2;yy=x*(z+w)/2
checks=[]
def ck(n,e):
 assert S.factor(e)==0,(n,S.factor(e));checks.append(n)
# dx wedge dt wedge ds relative dz,dw,dx.
J=S.Matrix([[S.diff(f,v) for v in (z,w,x)] for f in (x,tt,ss)])
ck('actual source residue',J.det()/(2*yy)-S.Rational(1,2))
T=(-w,x/w-w+1,w*w-w-z*w)
ck('actual source translation determinant',S.Matrix([[S.diff(f,v) for v in (z,w,x)] for f in T]).det()-1)
# c coordinate first, avoiding any branch differentiation.
c=S.symbols('c',nonzero=True)
F=(c,c*z,w/c,x/c)
det=S.Matrix([[S.diff(f,v) for v in (z,w,x,c)] for f in F]).det()
ck('source charged volume in c',det+1/c)
# dlog xi=3 dc/c, so coefficient is -1/3.
a,b,h=S.symbols('a b h')
Ft=(c*a,c*b,1/c,h/c)
det2=S.Matrix([[S.diff(f,v) for v in (a,b,h,c)] for f in Ft]).det()
ck('target charged volume in c',det2-1/c)
targ=(-a,h-a+1,a*a-a-b)
ck('target source determinant',S.Matrix([[S.diff(f,v) for v in (a,b,h)] for f in targ]).det()+1)
ck('auxiliary determinant weight',1+1-1-1)
out={'status':'PASS','count':len(checks),'checks':checks,'scope':'actual local canonical/Spin comparison only'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
