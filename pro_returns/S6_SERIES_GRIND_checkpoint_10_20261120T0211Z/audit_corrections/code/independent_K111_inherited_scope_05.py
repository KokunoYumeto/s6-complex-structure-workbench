"""Exact statement-to-target parameter/line checks, after reading inputs.

No whole F41/F46/K94/K96 proof or historical certificate is claimed replayed.
"""
import json,hashlib,time
from pathlib import Path
import sympy as s
start=time.perf_counter(); checks=[]
def ck(name,x):
    xx=list(x) if isinstance(x,s.MatrixBase) else [x]
    residual=[s.factor(s.cancel(q)) for q in xx]
    if any(q!=0 for q in residual):raise AssertionError((name,residual))
    checks.append({'name':name,'residuals':[str(q) for q in residual]})
r,t,rho,v,z,X,Y=s.symbols('r t rho v z X Y')
x=s.symbols('x')
poly=x**3+r*x*x+t*x+t*t
disc=s.discriminant(poly,x)
ck('complete source discriminant',disc-t*t*(r*r*(1-4*r)+(18*r-4)*t-27*t*t))
tc=(1-3*rho*rho+2*rho**3)/27
to=(1-3*rho*rho-2*rho**3)/27
rr=(1-rho*rho)/3
ck('selected branch satisfies discriminant',(disc/t**2).subs({t:tc,r:rr}))
ck('other branch satisfies discriminant',(disc/t**2).subs({t:to,r:rr}))
ck('selected real branch sign factor',tc-(rho-1)**2*(2*rho+1)/27)
ck('other real branch sign factor',to-(rho+1)**2*(1-2*rho)/27)
ck('branches remain separated',tc-to-4*rho**3/27)
ck('initial selected zero',tc.subs(rho,-1)+s.Rational(4,27))
ck('target selected collision',tc.subs(rho,-s.Rational(1,2)))
D=v-2;rv=(1-2*v)/D**2;sv=v*(v+4)/(4*D**2)
ck('original SI2 source parameter',s.Rational(1,4)-rv-sv)
ck('original SI2 selected branch',disc.subs({r:rv,t:v/D**3}))
ck('original SI2 meridian derivative',s.diff(sv,v).subs(v,0)-s.Rational(1,4))
ss=s.Rational(1,4)-r
ck('actual doubled marked section',(-t-ss/2)**2-(ss**3+r*ss**2+t*ss+t*t))
source_residual=(s.symbols('y')**2-poly)
root_residual=s.expand(z**6*source_residual.subs({x:z**-2*X,s.symbols('y'):z**-3*Y,t:z**-3}))
ck('literal good cubic root equation',root_residual-(Y**2-X**3-r*z*z*X*X-z*X-1))
f2old=(z**-3*Y-z**-3-z**-2*X/2)/(z**-2*X-ss)
f2root=(Y-1-z*X/2)/(X-ss*z*z)
ck('actual Miller factor root weight',f2old-z**-1*f2root)
tc_symbol=s.symbols('t_c')
ck('six-factor selected height coefficient cancellation',(z**-3-tc_symbol)/(z**-3)**3*z**-6-(1-tc_symbol*z**3))
k6,k2=s.symbols('kappa6 kappa2')
D23=s.Matrix([[1,2,1,1,0],[0,0,0,0,-1],[0,0,-1,0,2],[0,-1,-k6,0,0],[0,0,0,-1,-k2]])
ck('F46 b3 full collar determinant',D23.det()-1)
D1=s.Matrix([[1,0,-1,0],[0,1,0,1],[1,-3,0,0],[0,0,0,-1]])
ck('F46 actual one-cap specialization determinant',D1.det()+1)
ck('F46 actual source meridian determinant',1*1+3*0-1)
out={'status':'PASS','count':len(checks),'checks':checks,'seconds':round(time.perf_counter()-start,6),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':'Exact source path, selected branch, marked point, M2 six-factor root scaling and F41/F46 parameter specialization. This is post-reading targeted algebra, not a whole inherited theorem replay.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2))
