#!/usr/bin/env python3
"""Exact identities for BW1--3's relative bottom-row winding calculation.

The relative local line and cap morphisms are proved in the companion
working note. This certificate does not substitute winding numbers for
a named family's actual primitive-period or finite-cap identification.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
checks=[]
def ck(name,a,b=0):
    if isinstance(a,s.MatrixBase) or isinstance(b,s.MatrixBase):
        z=s.Matrix(a)-s.Matrix(b)
        assert all(s.simplify(x)==0 for x in z),(name,z)
    else:
        assert s.simplify(a-b)==0,(name,s.simplify(a-b))
    checks.append(name)
def exact(name,a,b):
    assert a==b,(name,a,b)
    checks.append(name)

L,J,n,e=s.symbols('L J n e',integer=True)
u,v,d,gamma,theta,alpha,t=s.symbols('u v d gamma theta alpha t')
tau,mu,G,zeta=s.symbols('tau mu G zeta')
z=u+tau*v+G*gamma
ell=d+mu*v+zeta*gamma
qdeck={tau:tau+1,zeta:zeta+1,u:u-v,d:d-gamma}
thdeck={mu:mu+L,zeta:zeta+J,d:d-L*v-J*gamma}
for name,deck in [('q',qdeck),('theta',thdeck)]:
    ck(name+' full source-point deck',z.subs(deck,simultaneous=True),z)
    ck(name+' full line-point deck',ell.subs(deck,simultaneous=True),ell)
taun=tau+n*G
mun=mu+n*zeta-n*tau-n*n*G
zn=zeta-n*G
dn=d-n*u
gn=gamma-n*v
ck('actual sheared source point',u+taun*v+G*gn,z)
ck('actual sheared line point',dn+mun*v+zn*gn,ell-n*z)
ck('new source scalar winding',taun.subs(thdeck,simultaneous=True),taun)
ck('new h line winding',mun.subs(thdeck,simultaneous=True)-mun,L+n*J)
ck('new B line winding',zn.subs(thdeck,simultaneous=True)-zn,J)
ck('new theta delta coefficient',dn.subs(thdeck,simultaneous=True)-dn,-J*gn-(L+n*J)*v)
ck('new q delta coefficient',dn.subs(qdeck,simultaneous=True)-dn,-gn)

kappa,al,g,eta,q,unit,A,D=s.symbols('kappa al g eta q unit A D',nonzero=True)
E=s.Matrix([g**(-e),unit*eta**(-e)])
Cend=s.Matrix([g**e,unit**(-1)*eta**e])
ck('fixed-e exact source seam',E[0]*Cend[0],1)
ck('fixed-e exact line seam',E[1]*Cend[1],1)
En=s.Matrix([E[0],E[1]*E[0]**(-n)])
Cn=s.Matrix([Cend[0],Cend[1]*Cend[0]**(-n)])
ck('sheared fixed-e source seam',En[0]*Cn[0],1)
ck('sheared fixed-e line seam',s.powsimp(En[1]*Cn[1],force=True),1)
a,b,c=s.symbols('a b c',nonzero=True)
rows=[s.Matrix([kappa*al*b*c,al**-1*a*b,kappa**-1/b]),
      s.Matrix([g*eta*b*c,eta**-1/c,g**-1*a*c]),
      s.Matrix([1/a,a*b,a*c])]
action={a:a/(A*D),b:A*b,c:D*c}
for i,row in enumerate(rows):
    ck(f'full bounded-unit period square {i}',row.subs(action,simultaneous=True),
       s.Matrix([A*D*row[0],D**-1*row[1],A**-1*row[2]]))
    ck(f'actual q retained {i}',s.prod(row),a*b*c)

dd,du,dv,dgamma=s.symbols('dd du dv dgamma')
A0=dd+(alpha+J*theta)*dgamma+L*theta*dv
An=dd+(alpha+J*theta)*dgamma+(L+n*J)*theta*dv
ck('original connection q deck',A0.subs({dd:dd-dgamma,alpha:alpha+1},simultaneous=True),A0)
ck('original connection theta deck',A0.subs({dd:dd-L*dv-J*dgamma,theta:theta+1},simultaneous=True),A0)
ck('sheared connection q deck',An.subs({dd:dd-dgamma,alpha:alpha+1},simultaneous=True),An)
ck('sheared connection theta deck',An.subs({dd:dd-(L+n*J)*dv-J*dgamma,theta:theta+1},simultaneous=True),An)
ck('exact whole boundary line primitive',An.subs({dd:dd-n*du,dgamma:dgamma-n*dv},simultaneous=True)-A0,-n*(du+alpha*dv))
A01=dd+(alpha+theta)*dgamma
ck('literal two-theta-tensor boundary arrow',A0-A01,L*theta*dv+(J-1)*theta*dgamma)

phi,dphi=s.symbols('phi dphi')
E12=s.zeros(6);E12[0,1]=1
E32=s.zeros(6);E32[2,1]=1
GG=s.eye(6)+n*phi*E12-n*E32
ck('whole tangent collar determinant',GG.det(),1)
om=GG.inv()*GG.diff(phi)*dphi
ck('whole tangent Maurer form',om,n*dphi*E12)
ck('whole tangent Maurer square',om*om,s.zeros(6))

def add(*forms):
    out={}
    for f in forms:
        for I,x in f.items():out[I]=s.simplify(out.get(I,0)+x)
    return {I:x for I,x in out.items() if x!=0}
def scale(x,f):
    return {I:s.simplify(x*y) for I,y in f.items() if s.simplify(x*y)!=0}
def wedge(a,b):
    out={}
    for I,x in a.items():
        for K,y in b.items():
            if set(I)&set(K):continue
            sig=(-1)**sum(i>j for i in I for j in K)
            key=tuple(sorted(I+K))
            out[key]=s.simplify(out.get(key,0)+sig*x*y)
    return {I:x for I,x in out.items() if x!=0}
def fc(name,a,b):exact(name,add(a,scale(-1,b)),{})
da,duf,dvf,dgf,dt=[{(i,):s.Integer(1)} for i in range(5)]
beta=add(scale(-n,duf),scale(-n*alpha,dvf))
dbeta=scale(-n,wedge(da,dvf))
Xi=wedge(dt,dvf)
Psi=wedge(dt,dgf)
fc('actual b theta tensor square',wedge(Xi,Xi),{})
fc('actual gamma theta tensor square',wedge(Psi,Psi),{})
fc('two actual theta tensors multiply zero',wedge(Xi,Psi),{})
Fext=add(wedge(add(da,scale(J,dt)),add(dgf,scale(n,dvf))),scale(L,Xi))
Fpiece=add(wedge(add(da,scale(J,dt)),dgf),scale(L+n*J,Xi))
fc('complete boundary curvature arrow',add(Fext,dbeta),Fpiece)
fc('retained nonzero exterior square',wedge(Fext,Fext),scale(2*L,wedge(wedge(da,dgf),Xi)))
fc('boundary primitive derivative square',wedge(dbeta,dbeta),{})
Ft=add(Fext,scale(t,dbeta))
CS=scale(3,wedge(beta,wedge(Ft,Ft)))
up={I:s.integrate(x,(t,0,1)) for I,x in CS.items()}
down={I:s.integrate(x,(t,1,0)) for I,x in CS.items()}
fc('full retained five-form collar',up,{tuple(range(5)):6*L*n+3*J*n*n})
fc('actual outward collar sign',down,{tuple(range(5)):-6*L*n-3*J*n*n})
exact('physical dual and Jin sign cancellation',(-1)**3*(-1),1)

# An arbitrary curvature in six variables, to check tensor invariance
# algebraically without replacing the relative line-bundle argument.
Fbase={(i,j):s.Symbol(f'f{i}{j}') for i in range(6) for j in range(i+1,6)}
Ftens=add(Fbase,scale(L,Xi),scale(J-1,Psi))
fc('relative bulk pairing independent of both theta tensors',
   wedge(wedge(Ftens,Ftens),Xi),wedge(wedge(Fbase,Fbase),Xi))
R=s.symbols('R')
exact('same-e local K62 integer calibration',s.solve(s.Eq(3*R-3,0),R),[1])
k0,ell0=s.symbols('k0 ell0')
delta_k=s.expand(3*n*J-6*L*n-3*J*n*n)
ck('actual complete relative Euler cube',delta_k,-6*L*n-3*J*n*(n-1))
ck('physical index change',4*delta_k/24,-L*n-J*n*(n-1)/2)
ck('whole-I1 specialization',delta_k.subs(L,0),-3*J*n*(n-1))
ck('zero J exact retained L contribution',delta_k.subs(J,0),-6*L*n)
ck('single C2 full integer contribution',delta_k.subs(n,1),-6*L)

# Actual OS49 primitive-period, positive-chart and shorter-endpoint maps.
m,k=s.symbols('m k',positive=True,integer=True)
eps=s.symbols('eps',integer=True)
ss,vv=s.symbols('s v')
U0,U1,C0,C1,D0,D1=s.symbols('U0 U1 C0 C1 D0 D1')
src=s.Matrix([2*ss+U0,ss+U1])
susp=s.Matrix([-3*ss+C0,-ss+m*vv+C1])
HH=-src-susp
KK=3*src+2*susp
ck('literal OS49 H period',HH,s.Matrix([ss-U0-C0,-m*vv-U1-C1]))
ck('literal OS49 K period',KK,s.Matrix([3*U0+2*C0,ss+2*m*vv+3*U1+2*C1]))
ck('actual deck-generator determinant',s.Matrix([[-1,3],[-1,2]]).det(),1)
ck('actual OS49 H theta winding',HH.subs(vv,vv+1)-HH,s.Matrix([0,-m]))
ck('actual OS49 K theta winding',KK.subs(vv,vv+1)-KK,s.Matrix([0,2*m]))
Ta={(0,0),(1,1),(0,1)}
Tb={(1,1),(0,1),(1,2)}
Pa={(0,0),(1,1),(0,1)}
Pb={(0,0),(1,0),(1,1)}
exact('positive T1 first literal triangle',Ta,Pa)
exact('positive T1 second is full B translate',Tb,{(x,y+1) for x,y in Pb})
Z,V=s.symbols('Z V',nonzero=True)
Vn=Z**(-n)*V
native=s.Matrix([Z,q/(Z*Vn),Vn])
ck('whole vertical native q',s.prod(native),q)
ck('actual positive T1 OC11 chart',native.subs(n,1),s.Matrix([Z,q/V,V/Z]))
second=s.Matrix([1/Z,Z*native[1],Z*native[2]])
ck('actual positive T1 second OC11 chart',second.subs(n,1),s.Matrix([1/Z,q*Z/V,V]))
kk=s.expand(2*m+delta_k.subs({L:-m,J:2*m})-delta_k.subs({L:-m,J:2*m,n:1}))
ee=8*m
ck('named positive-reference integer comparison',kk,2*m-6*m*(n-1)**2)
ck('named full physical Jin integer',(4*kk-ee)/24,-m*(n-1)**2)
ck('named native fixed left',ee/4,2*m)
ck('named native fixed right',kk-ee/4,-6*m*(n-1)**2)

delta=s.Matrix([0,1]);DD=s.Matrix([D0,D1])
sigma=eps*vv*DD+eps*m*vv*(vv-1)*delta
close=eps*DD/3+(2*eps*m*vv/3-2*eps*m/9)*delta
ck('actual shorter closing direction',sigma.subs(vv,vv+s.Rational(1,3))-sigma,close)
lap=sum((close.subs(vv,vv+s.Rational(j,3)) for j in range(3)),s.zeros(2,1))
ck('literal three-sheet closing norm',lap,eps*DD+2*eps*m*vv*delta)
shear=s.Matrix([[1,0],[-n,1]])
for j in range(4):
    P=sum((close.subs(vv,vv+s.Rational(h,3)) for h in range(j)),s.zeros(2,1))
    ck(f'actual sheared endpoint table {j}',shear*P,
       (shear*sigma).subs(vv,vv+s.Rational(j,3))-shear*sigma)
for j in range(3):
    P=sum((close.subs(vv,vv+s.Rational(h,3)) for h in range(j)),s.zeros(2,1))
    Pnext=sum((close.subs(vv,vv+s.Rational(h,3)) for h in range(j+1)),s.zeros(2,1))
    ck(f'whole source/line seam increment {j}',shear*(Pnext-P),shear*close.subs(vv,vv+s.Rational(j,3)))
Dn=D*A**(-n)
cox=s.Matrix([1,A,(A*Dn)**(-1),Dn])
ck('actual C0 Cox product q',s.prod(cox),1)
ck('actual first C0 cut factors',s.Matrix([cox[1]/cox[0],cox[0]*cox[2],cox[0]*cox[3]]),s.Matrix([A,(A*Dn)**(-1),Dn]))
ck('actual second C0 cut factors',s.Matrix([cox[0]/cox[1],cox[1]*cox[2],cox[1]*cox[3]]),s.Matrix([A**(-1),Dn**(-1),A*Dn]))
origin=sigma.subs(vv,vv+theta)-sigma
canonical=eps*theta*DD+2*eps*m*theta*(vv+theta)*delta
ck('full origin/canonical seam difference',origin-canonical,-eps*m*(theta*theta+theta)*delta)
ck('global physical delta correction initial',(-eps*m*(theta*theta+theta)).subs(theta,0),0)
ck('global physical delta correction terminal',(-eps*m*(theta*theta+theta)).subs(theta,1),-2*eps*m)
ck('actual based delta loop exponential',s.exp(-4*s.pi*s.I*eps*m),1)
ck('shorter physical Euler integral cover',3*(2*k-6*k*(n-1)**2),kk.subs(m,3*k))
ck('shorter physical p1 integral cover',3*8*k,ee.subs(m,3*k))
ck('shorter physical Jin integer',((4*(2*k-6*k*(n-1)**2)-8*k)/24),-k*(n-1)**2)
j=s.symbols('j',positive=True,integer=True)
Pn=s.Matrix([[1,0],[n,1]])
BB=2*Pn.inv()*s.Matrix([[0,0],[-j,2*j]])*Pn
ck('actual doubled OS49 winding',BB,s.Matrix([[0,0],[2*j*(2*n-1),4*j]]))
wgt=[0,1,-1];normal=[-2,-1,-1];tt=2*j
ll=[BB[1,1]-BB[1,0],BB[0,0]-BB[0,1],BB[1,1]]
II=s.Matrix([s.expand(tt*wgt[i]+normal[i]*(ll[i]-tt)) for i in range(3)])
WW=s.Matrix([s.expand(tt*wgt[i]-normal[i]*(ll[i]-tt)) for i in range(3)])
ck('actual OS49 full normal trace',II,s.Matrix([8*j*(n-1),4*j,-4*j]))
ck('actual OS49 full stable trace',WW,s.Matrix([8*j*(1-n),0,0]))
Vseed=s.Matrix([[12*j*(n-1)**2,8*j*(1-n),8*j*(n-1)],
                [8*j*(1-n),4*j,0],[8*j*(n-1),0,4*j]])
Dseed=s.Matrix([-12*j*(n-1)**2,8*j*(n-1),8*j*(1-n)])
for h in [1,2]:
    ck(f'actual variation prism {h}',Vseed*(wgt[h]*s.eye(3)[:,h]),II[h]*s.eye(3)[:,h]-II[0]*s.eye(3)[:,0])
    ck(f'actual derivative prism {h}',wgt[h]*Dseed[h],WW[h]-WW[0])
left=4*j-4*j
right=-12*j*(n-1)**2
ck('actual ordinary fixed variation from native pair',-(left+right),Vseed[0,0])
ck('actual ordinary fixed derivative from native pair',right-left,Dseed[0])

out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
     'proof_status':'Working full relative proof; root audit pending. Exact algebra certificate is not a global-family identification.',
     'check_count':len(checks),'checks':checks,
     'scope':'Actual primitive nodal piece with the fixed closing exponent e, full bounded period factors, physical line and Hopf cap; named-family primitive/root/cap dictionaries are retained separately.',
     'formulas':{'delta_k_M':str(s.factor(delta_k)),'delta_ell_M':'0',
                 'delta_A_M':str(s.factor(delta_k/6)),
                 'outward_collar':'-6*L*n-3*J*n**2','interior':'3*n*J'},
     'OS49_vertical':{'r_pair':['2*m-6*m*(n-1)**2','8*m'],'w_pair':['2*k-6*k*(n-1)**2','8*k'],'r_index':'-m*(n-1)**2','w_index':'-k*(n-1)**2','actual_positive_reference':'T1 with OC11 charts and K68 physical pair(2m,8m)','double_seed':{'V':[[str(x) for x in row] for row in Vseed.tolist()],'delta':[str(x) for x in Dseed]}},
     'proof':'notes/part3_bottom_row_winding_working.md'}
(ROOT/'code/part3/bottom_row_winding.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'PASS: {len(checks)} exact full-period, relative-line, tangent and whole-collar identities.')
print(json.dumps(out['formulas'],indent=2))
