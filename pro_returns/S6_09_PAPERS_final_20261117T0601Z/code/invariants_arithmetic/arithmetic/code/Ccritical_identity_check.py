"""Independent high-precision check of the derived Cayley identity, not a proof."""
from pathlib import Path
import json
import mpmath as m
m.mp.dps=110
root=Path(__file__).resolve().parents[1];dd=json.loads((root/'records/Ccritical_certificate.json').read_text())
def rat(s):
 ss=s.split('/');return m.mpf(ss[0])/(m.mpf(ss[1]) if len(ss)>1 else 1)
B=[rat(v) for v in dd['B']];J=[rat(v) for v in dd['J']];H=[rat(v) for v in dd['H']]
poly=lambda V,z:sum(v*z**n for n,v in enumerate(V))
A=1+240*sum(n**3*m.exp(-2*m.pi*n)/(1-m.exp(-2*m.pi*n)) for n in range(1,100));k=m.pi**2*A
for tau in [m.mpc(0,'1.1'),m.mpc('.2','1'),m.mpc('.5','1.4'),m.mpc('.49','.88')]:
 q=m.exp(2j*m.pi*tau);C=[q**n/(1-q**n) for n in range(1,121)];E2=1-24*sum(n*C[n-1] for n in range(1,121));E4=1+240*sum(n**3*C[n-1] for n in range(1,121));E6=1-504*sum(n**5*C[n-1] for n in range(1,121))
 def wp(u):return m.pi**2/m.sin(m.pi*u)**2-m.pi**2*E2/3-8*m.pi**2*sum(n*C[n-1]*m.cos(2*m.pi*n*u) for n in range(1,121))
 def wpp(u):return -2*m.pi**3*m.cos(m.pi*u)/m.sin(m.pi*u)**3+16*m.pi**3*sum(n*n*C[n-1]*m.sin(2*m.pi*n*u) for n in range(1,121))
 u=m.findroot(wp,(m.mpc('.5','-.3'),m.mpc('.5','-.4')),tol=m.mpf('1e-105'),maxsteps=100)
 W=m.pi/m.tan(m.pi*u)+4*m.pi*sum(C[n-1]*m.sin(2*m.pi*n*u) for n in range(1,121))+2j*m.pi*u.imag/tau.imag
 p=wpp(u);g2=4*m.pi**4*E4/3;X=3*W*p/g2
 w=(tau-1j)/(tau+1j);z=k*w*w;r=abs(w)
 hh=poly(H,z);hp=poly([n*H[n] for n in range(1,len(H))],z)
 FC=m.sqrt(poly(J,z))/poly(B,z)*(hh+4*z*hp+2*r/(1-r*r)*(r*hh-m.conj(hh)))
 t=E4**3/(E4**3-E6**2);tp=-2j*m.pi*t*E6/E4;lt=1j*W*(3*W*p-2*g2)/(24*m.pi*p)/tp
 print('tau',m.nstr(tau,25));print('X',m.nstr(X,80));print('F-Cayley residual',m.nstr(abs(1-X-FC),12));print('radial identity residual',m.nstr(abs((t-1)*lt-X*(X-2)/24),12));print('wp residual',m.nstr(abs(wp(u)),12))
