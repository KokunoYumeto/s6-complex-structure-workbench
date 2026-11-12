"""Exact vacuum-curve/sector checks. Run: python verify_vacuum_kinetics.py

Requires SymPy; no files, network access or repository paths are used.
Proofs and precise hypotheses are in REPORT.md and vacuum_kinetics_fragment.tex.
"""
import sympy as S

I = S.I
eye = S.eye(3)
checks = 0


def comm(a, b):
    return a*b-b*a


def tf(a):
    return a-S.trace(a)*eye/3


def zero(label, value):
    global checks
    entries = list(value) if isinstance(value, S.MatrixBase) else [value]
    assert all(S.simplify(S.trigsimp(S.expand(e))) == 0 for e in entries), label
    checks += 1


def metric(ph, bv, ps, bw):
    return S.trace(ph*ps)+2*S.re((bv.H*bw)[0])


def current(ph, bv, dp, db):
    return comm(ph,dp)+bv*db.H-db*bv.H


h, k, beta, hd, kd, bd = S.symbols("h k beta hd kd bd", real=True)
m2, Gamma, kap = S.symbols("m2 Gamma kappa", real=True)
chi = S.symbols("chi", positive=True)
theta = S.symbols("theta", real=True)
ph = S.diag(h+k,h-k,-2*h)
b = beta*eye[:,2]
s = 6*h*h+2*k*k+2*beta*beta
a = m2+Gamma*s
V = m2*s/2+Gamma*s*s/4-2*kap*h*(k*k+beta*beta-h*h)
fh = -a*h-kap*h*h+kap*(k*k+beta*beta)/3
fk = -(a-2*kap*h)*k
fb = -(a-2*kap*h)*beta
zero("sector norm", S.trace(ph**2)+2*(b.H*b)[0]-s)
zero("sector cubic", ph.det()-(b.H*ph*b)[0]-2*h*(k*k+beta*beta-h*h))
zero("sector Phi equation",
     -a*ph+kap*tf(ph.adjugate()-b*b.H)-S.diag(fh+fk,fh-fk,-2*fh))
zero("sector b equation", -(a*eye+kap*ph)*b-fb*eye[:,2])
dp = S.diag(hd+kd,hd-kd,-2*hd)
db = bd*eye[:,2]
zero("sector current", current(ph,b,dp,db))
zero("sector kinetic", metric(dp,db,dp,db)/2-(3*hd*hd+kd*kd+bd*bd))
zero("h variational coefficient", S.diff(V,h)+6*fh)
zero("k variational coefficient", S.diff(V,k)+2*fk)
zero("beta variational coefficient", S.diff(V,beta)+2*fb)
zero("sector energy conservation", 6*hd*fh+2*kd*fk+2*bd*fb
     +S.diff(V,h)*hd+S.diff(V,k)*kd+S.diff(V,beta)*bd)

phv = chi*S.diag(3*S.cos(theta)**2-1,3*S.sin(theta)**2-1,-1)
bv = -3*chi*S.cos(theta)*S.sin(theta)*eye[:,2]
tp, tb = phv.diff(theta), bv.diff(theta)
np, nb = tp.diff(theta), tb.diff(theta)
zero("curve tangent norm", metric(tp,tb,tp,tb)-18*chi**2)
zero("curve acceleration norm", metric(np,nb,np,nb)-72*chi**2)
zero("curve orthogonal acceleration", metric(tp,tb,np,nb))
zero("curve current", current(phv,bv,tp,tb))
zero("normal radial projection", metric(np,nb,phv,bv)+18*chi**2)
zero("additional normal component norm",
     metric(np+3*phv,nb+3*bv,np+3*phv,nb+3*bv)-18*chi**2)
sv = S.trace(phv**2)+2*(bv.H*bv)[0]
av = kap*chi-6*Gamma*chi**2+Gamma*sv
gp = av*phv-kap*tf(phv.adjugate()-bv*bv.H)
gb = (av*eye+kap*phv)*bv
zero("entire curve vacuum Phi gradient", gp)
zero("entire curve vacuum b gradient", gb)
zero("Hessian kills tangent Phi", gp.diff(theta))
zero("Hessian kills tangent b", gb.diff(theta))


def eij(i,j):
    out=S.zeros(3)
    out[i,j]=1
    return out


basis=[]
for i in range(3):
    for j in range(i+1,3):
        basis += [eij(i,j)-eij(j,i),I*(eij(i,j)+eij(j,i))]
basis += [I*S.diag(1,-1,0),I*S.diag(0,1,-1)]
for n,z in enumerate(basis):
    zero("SU3 horizontal tangent "+str(n),metric(tp,tb,comm(z,phv),z*bv))
for angle,rank_expected in [(0,4),(S.pi/6,7),(S.pi/4,5)]:
    p0=phv.subs({theta:angle,chi:1})
    b0=bv.subs({theta:angle,chi:1})
    cols=[]
    for z in basis:
        values=list(comm(z,p0))+list(z*b0)
        cols.append(S.Matrix([S.re(e) for e in values]+[S.im(e) for e in values]))
    assert S.Matrix.hstack(*cols).rank()==rank_expected
    checks += 1

P=S.Matrix([[1,-1,0],[0,1,-1]])
G=P*(phv+chi*eye)*P.T
zero("retained observed matrix",
     G-3*chi*S.Matrix([[1,-S.sin(theta)**2],[-S.sin(theta)**2,S.sin(theta)**2]]))
rho=sum(bv)
invariant=(bv.H*bv)[0]
zero("observed saturation",G.det()-rho**2)
zero("invariant derivative",S.diff(invariant,theta)-(9*chi**2/2)*S.sin(4*theta))
M=9*chi**2/4
zero("invariant coordinate metric",S.diff(invariant,theta)**2-16*invariant*(M-invariant))

# Exact nonlinear null profiles, not homogeneous moduli geodesics.
t,z=S.symbols("t z",real=True)
f=S.Function("f",real=True)
profile=f(t-z)
pw=phv.subs(theta,profile)
bw=bv.subs(theta,profile)
zero("nonlinear null-wave Phi dAlembertian",pw.diff(t,2)-pw.diff(z,2))
zero("nonlinear null-wave b dAlembertian",bw.diff(t,2)-bw.diff(z,2))
# A real profile has a real first jet.  Use that independent real jet rather
# than asking SymPy to infer conjugation of an unevaluated f' automatically.
profile_speed=S.symbols("profile_speed",real=True)
zero("nonlinear null-wave current",current(phv,bv,tp*profile_speed,tb*profile_speed))

# Exact homogeneous gauge-horizontal periodic sector.
hh=S.symbols("hh",positive=True)
den=1-6*Gamma*hh/kap
aa=(m2+12*Gamma*hh**2)/den
rr=3*aa*hh/kap+3*hh**2
ww=(m2-2*kap*hh+24*Gamma*hh**2)/den
zero("periodic norm self-consistency",aa-m2-Gamma*(6*hh**2+2*rr))
zero("periodic h equation",-aa*hh-kap*hh**2+kap*rr/3)
zero("periodic frequency",ww-aa+2*kap*hh)
energy=rr*ww+m2*(3*hh**2+rr)+Gamma*(3*hh**2+rr)**2-2*kap*hh*(rr-hh**2)
h0=S.symbols("h0",positive=True)
mrelation=2*kap*h0-24*Gamma*h0**2
vacenergy=12*mrelation*h0**2+144*Gamma*h0**4-16*kap*h0**3
er=energy.subs(m2,mrelation)
zero("periodic limiting radius",rr.subs({m2:mrelation,hh:h0})-9*h0**2)
zero("periodic limiting frequency",ww.subs({m2:mrelation,hh:h0}))
zero("periodic limiting energy",er.subs(hh,h0)-vacenergy)
leading=18*h0**2*(24*Gamma*h0-kap)/(1-6*Gamma*h0/kap)
zero("periodic energy excess slope",S.diff(er,hh).subs(hh,h0)-leading)
zero("periodic frequency squared slope",
     S.diff(ww.subs(m2,mrelation),hh).subs(hh,h0)
     -2*(24*Gamma*h0-kap)/(1-6*Gamma*h0/kap))
print("PASS:",checks,"exact checks.")
