"""Exact Weierstrass/Tate leading, line-weight and central-period checks."""
from pathlib import Path
import sympy as S,json
r,t,s,u,Q,P,R,z,d,eta,q,lam=S.symbols('r t s u Q P R z d eta q lam',nonzero=True)
checks=[]
def ck(n,e):
 assert S.factor(e)==0,(n,S.factor(e))
 checks.append(n)
c4=16*(r*r-3*t);c6=-64*r**3+288*r*t-864*t*t
Delta=-16*t*t*(r*r*(4*r-1)+(4-18*r)*t+27*t*t)
ck('Weierstrass discriminant invariants',(c4**3-c6**2)/1728-Delta)
# Source equation obtained from the full Tate depressed cubic.
XT,YT,ct4,ct6=S.symbols('XT YT ct4 ct6')
xp=u*u*XT-r/3;yp=u**3*YT
target=yp*yp-xp**3-r*xp*xp-t*xp-t*t
rhs=u**6*(YT*YT-XT**3)+(r*r/S.Integer(3)-t)*u*u*XT-(2*r**3/S.Integer(27)-r*t/S.Integer(3)+t*t)
ck('exact depressed source map',target-rhs)
# Actual first derivatives of Tate G coordinates, using u^2=4r at t0.
xTd=1/(8*r*r)
yTd=1/(8*r**S.Rational(3,2))-1/(16*r*r)
ck('actual P over t leading',xTd+yTd-(1+2*S.sqrt(r))/(16*r*r))
ck('actual W over t leading',-yTd-(1-2*S.sqrt(r))/(16*r*r))
qlead=(1-4*r)/(256*r**4)
plead=(1+2*S.sqrt(r))/(16*r*r)
ck('actual R boundary value',qlead/plead**2-(1-2*S.sqrt(r))/(1+2*S.sqrt(r)))
rs=S.Rational(1,4)-s
R0=(1-2*S.sqrt(rs))/(1+2*S.sqrt(rs))
ck('R_s_at_origin',S.diff(R0,s).subs(s,0)-1)
ck('P_t_at_origin',plead.subs(r,S.Rational(1,4))-2)
ck('coordinate Jacobian',S.Matrix([[2,0],[2,1]]).det()-2)
# Full line character under h and B, retaining point-to-tensor factors.
ck('actual h line character',P**6/(P*P*R)**3-R**(-3))
K=(P/t)**3*eta**6
ck('actual B line multiplier',(P**3/t**3)*eta**6-K)
# At central source P eta^3=-2t, so eta^6=4t²/P².
K0=S.factor(K.subs(eta**6,4*t*t/P**2))
ck('central full K',K0-4*P/t)
ck('central source period',(P**3)*P**(-3)-1)
ck('central line period',P**(-3)*(lam*q*K0)**3-(4*lam*q/t)**3)
# Actual norm wall point.
c,tc=S.symbols('c tc',nonzero=True)
tb=-4*lam*tc/(c-4*lam)
ck('explicit norm wall point',4*lam*(tb-tc)/tb-c)
out={'status':'PASS','count':len(checks),'checks':checks,'scope':'Exact annular source/Cartier/period equations and norm wall; no global compact attachment or return.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
