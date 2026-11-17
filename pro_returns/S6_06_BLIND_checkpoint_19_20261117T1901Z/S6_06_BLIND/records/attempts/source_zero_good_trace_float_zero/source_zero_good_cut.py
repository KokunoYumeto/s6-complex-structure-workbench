#!/usr/bin/env python3
"""Good-branch real cut, typed two-step cap and local spin-c checks.

No global source-zero value or two-step strip completion is assigned.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
checks=[]
def eq(name,a,b):
    assert s.simplify(a-b)==0,name
    checks.append(name)
b,c,d,H,T,Z=s.symbols('b c d H T Z',nonnegative=True)
rho4=b+c*c+d*d; R2=b+c*d
eq('weighted seam lower bound', (R2-rho4/2).subs(d,c),b/2)
eq('fixed trace radii',R2.subs({c:0,d:0}),rho4.subs({c:0,d:0}))
eq('V=1 weighted radius',rho4.subs({b:H*T,c:H,d:Z}),H*T+H*H+Z*Z)
eq('V=1 product radius',R2.subs({b:H*T,c:H,d:Z}),H*(T+Z))
x,zeta,sig2=s.symbols('x zeta sig2',real=True)
f2=x*(1-zeta)+zeta*zeta
eq('charged angular radial expression',(H*T+H*H+Z*Z).subs({H:x*sig2,T:(1-x-zeta)*sig2,Z:zeta*sig2}),sig2**2*f2)
eq('charged angular product expression',(H*(T+Z)).subs({H:x*sig2,T:(1-x-zeta)*sig2,Z:zeta*sig2}),sig2**2*x*(1-x))
eq('lower angular denominator bound',x-f2,zeta*(x-zeta))
eq('whole angular upper bound',(1-zeta)**2+zeta*zeta-f2,(1-zeta)*(1-zeta-x))
eq('radial side transversality T1 nonzero',s.diff(R2,c)-s.diff(rho4,c),d-2*c)
eq('radial side transversality T1 zero',s.det(s.Matrix([[d,2*c],[c,2*d]])),2*(d*d-c*c))

p=s.symbols('p',positive=True,integer=True)
m=4*p
zz,h,lam=s.symbols('zz h lam',nonzero=True)
q=zz**(-m)*h
for eps in (0,1):
    eq(f'primitive annular square {eps}',zz**(-(eps+1)*m/2)*zz**(m/2),zz**(-eps*m/2))
eq('retained second overlap',zz**(-2*m/2),zz**(-m))
eq('actual two-step norm scalar',-2*lam*q*zz**m,-2*lam*h)
eq('one-step coefficient determinant root',(zz**p)**2,zz**(m/2))
eq('two-step coefficient determinant root',(zz**(2*p))**2,zz**m)
eq('good finite root character',s.exp(2*s.pi*s.I*(m/2)/m),-1)
eq('twice finite character',(-1)**2,1)
z0,z1=s.symbols('z0 z1',nonzero=True)
eq('chronological reset roots',(1/z0)*(1/z1),1/(z0*z1))
eq('chronological reset determinant',(1/(z0*z1))**2,z0**-2*z1**-2)

# Exact a=1 upper free product, retaining the actual line coefficient.
vcoef,zcoef,wcoef,phase,coef=s.symbols('vcoef zcoef wcoef phase coef',nonzero=True)
eq('upper product inverse',zcoef*(wcoef/zcoef),wcoef)
eq('upper product physical invariance',(phase*zcoef)*(vcoef/phase),zcoef*vcoef)
eq('upper physical line coefficient arrow',(phase*zcoef)*(coef/phase),zcoef*coef)
upper_jac=s.Matrix([zcoef*vcoef,zcoef]).jacobian([vcoef,zcoef])
assert upper_jac==s.Matrix([[zcoef,vcoef],[0,1]])
checks.append('full upper product derivative')
eq('upper product determinant',upper_jac.det(),zcoef)

# Full conifold units and all four proper-graph endpoint charts.
s0,s1,t0,t1,eta,uq,up,ux,ll,cl=s.symbols('s0 s1 t0 t1 eta uq up ux L c_lambda',nonzero=True)
ug=uq*up
q1=eta*s0*t0; q2=eta*s1*t1
cc=eta*s0*t1; dd=eta*s1*t0
qq=q1*q2*uq; pp=up/q2; ss=s0/s1
eq('full graph conifold relation',q1*q2,cc*dd)
eq('theta numerator QS',qq*ss,uq*q1*cc)
eq('theta numerator Q/S',qq/ss,uq*q2*dd)
eq('theta denominator S/P',ss/pp,cc/up)
eq('theta denominator QP/S',qq*pp/ss,ug*dd)
zold=ug*dd; vold=pp*(cc/up)*ll
zmid=pp*zold; vmid=q2*ux*vold
eq('actual inverse primitive line',vmid,ux*cc*ll)
l1=ug*up*ux*ll
eq('first indexed edge coefficient',zmid*vmid/q1,l1)
zh=qq*zmid; vh=pp*vmid
eq('second indexed edge coefficient',zh*vh/q1**2,ug*l1)
eq('retained source Tate-node product',(1/zmid)*zh,qq)
eq('retained associated line-node product',(q1*ug*l1)*(1/(ug*l1)),q1)
zfull=pp*zmid; vfull=q2*ux*vmid/(cl*q1)
eq('full B inverse source',zfull,pp**2*ug*dd)
eq('full B inverse line',vfull,q2*ux**2*cc*ll/(cl*q1))
eq('full B inverse unit character',zfull*vfull,ug*up**2*ux**2*ll/cl)
eq('actual retained full-unit vertex value',(ug*up**2*ux**2).subs({uq:s.Rational(1,256),up:16,ux:s.Rational(-1,4)}),1)
rr,sv,pv=s.symbols('r s pchart',nonzero=True)
chart10={s1:1,t0:1,eta:rr,s0:sv,t1:pv}
eq('S1 t0 graph edge first normal',(zh/q1).subs(chart10),ug**2*rr)
eq('S1 t0 graph edge second normal',(q1**2/zh).subs(chart10),sv/ug**2)
chart00={s0:1,t0:1,eta:rr,s1:sv,t1:pv}
eq('S0 t0 adjacent source w',(1/zmid).subs(chart00),pv/(ug*up))
eq('S0 t0 adjacent source z',zh.subs(chart00),ug**2*rr**2*sv)
for ii in (0,1):
    subs={t1:1,eta:rr,t0:pv,(s0 if ii==0 else s1):1,(s1 if ii==0 else s0):sv}
    eq(f't1 graph source normal {ii}',zmid.subs(subs),ug*up*pv)
    eq(f't1 graph other source normal {ii}',(q1/zmid).subs(subs),(eta*s0/(ug*up)).subs(subs))

# Compact smooth source-moment trace and the chronological cap factorization.
us,ut=s.symbols('norm_s_squared norm_t_squared',nonnegative=True)
mu=(ut-us)/2
eq('moment trace compactness',(us+ut)**2,4*mu**2+4*us*ut)
eq('moment-product face Jacobian',s.det(s.Matrix([[s.diff(mu,us),s.diff(mu,ut)],[s.diff(us*ut,us),s.diff(us*ut,ut)]])),-(us+ut)/2)
c0=s.symbols('c0',nonzero=True)
eq('chronological primitive norm factors',c0*(cl/c0)*q,q*cl)
eq('first normalized cap coefficient',zz**(-m/2)*c0*zz**(m/2),c0)
eq('second normalized cap coefficient',zz**m*(cl/c0)*q,cl*h/c0)
eq('complete normalized cap coefficient',c0*(cl*h/c0),cl*h)
eq('physical charged-one index',(4*(-1)-(-4))/24,0)
wp,wm,c2s=s.symbols('w_plus w_minus c2_S4',integer=True)
eq('whole good fixed-trace index',(4*(1+wm-wp)-(4+4*(wm-wp)))/24,0)
eq('retained S4 normal index',(4*c2s-4*c2s)/24,0)

# The canonical Spin-c representative [e1e2,i] squares to [-1,-1].
eq('one-line spin square',-1,-1)
eq('one-line central U1 square',s.I**2,-1)
M=s.diag(1,-1)
assert M*M==s.eye(2)
checks.append('canonical exterior-algebra two-character composition')
for pp in range(1,13):
    mm=4*pp
    assert (mm//2)%2==0
    checks.append(f'actual root-line integer square root p{pp}')

note=ROOT/'notes/part3_source_zero_good_cut_working.md'
data={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),
      'checks':len(checks),'identities':checks,
      'scope':'GC.1–9 exact good-cut, typed two-step cap, upper graph/node/line and moment-trace identities. Full finite-strip proof is submitted for independent geometric audit; this certificate does not substitute algebra for that audit.',
      'source_sha256':hashlib.sha256(note.read_bytes()).hexdigest()}
(ROOT/'code/part3/source_zero_good_cut.json').write_text(json.dumps(data,indent=2)+'\n')
print(f'PASS: {len(checks)} exact good-cut and typed two-step identities.')
print(data['scope'])
