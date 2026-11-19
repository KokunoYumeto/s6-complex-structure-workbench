#!/usr/bin/env python3
"""Independent first-jet route for the finite collar connection.

Does not import either other atlas checker. It composes actual original
affine maps and line gauges for twelve iterations, transporting every
one-form component by a small exact dual-number implementation.
"""
from pathlib import Path
import datetime,hashlib,json,time,platform
import sympy as s

start=time.monotonic();checks=[];records=[]
def simp(x):return s.cancel(s.expand(x))
def ck(name,x):
    seq=x if isinstance(x,(list,tuple)) else [x]
    ok=all(simp(y)==0 for y in seq)
    checks.append({'name':name,'passed':ok})
    if not ok:raise AssertionError((name,seq))

class J:
    def __init__(self,v,d=(0,0,0)):
        self.v=s.sympify(v);self.d=tuple(s.sympify(x) for x in d)
    def __add__(self,b):
        b=lift(b);return J(self.v+b.v,[x+y for x,y in zip(self.d,b.d)])
    __radd__=__add__
    def __neg__(self):return J(-self.v,[-x for x in self.d])
    def __sub__(self,b):return self+-lift(b)
    def __rsub__(self,b):return lift(b)+-self
    def __mul__(self,b):
        b=lift(b);return J(self.v*b.v,[x*b.v+self.v*y for x,y in zip(self.d,b.d)])
    __rmul__=__mul__
    def __truediv__(self,b):
        b=lift(b);return J(self.v/b.v,[(x*b.v-self.v*y)/(b.v*b.v) for x,y in zip(self.d,b.d)])
    def __rtruediv__(self,b):return lift(b)/self
    def __pow__(self,n):
        assert n>=0
        ans=J(1)
        for k in range(n):ans=ans*self
        return ans
    def reduced(self):return J(simp(self.v),[simp(x) for x in self.d])
def lift(x):return x if isinstance(x,J) else J(x)
def dot(x,y):return sum((a*b for a,b in zip(x,y)),J(0))
def matvec(M,x):return [dot(row,x) for row in M]
def periods(t,m,b):return [[6*m,t,1,0],[b,m,0,1]]
def Tmatrix(t,m,b):return [[t,6*m],[m,b]]
def fperiod(v,z,t,m,b):
    # Original n order (gamma,u), K=[[0,6],[1,0]].
    ng,nu=v[:2]
    return 6*ng*z[1]+nu*z[0]+(6*b*ng*ng+12*m*ng*nu+t*nu*nu)/2
def original_connection(state,v):
    # A/(-12*pi*i), evaluated as a full one-form in the ORIGINAL
    # (ds,dzeta1,dzeta2) directions after all coordinate pullbacks.
    t,m,b,h,z=state
    pv=matvec(periods(t,m,b),v)
    sig=[h*x for x in pv]
    tp,mp,bp=t.d[0],m.d[0],b.d[0]
    det=tp*bp-6*mp*mp
    dsig=[x.d[0] for x in sig]
    a1=2*(bp*dsig[0]-6*mp*dsig[1])/det
    a2=2*(-6*mp*dsig[0]+6*tp*dsig[1])/det
    S=v[1]*pv[0]+6*v[0]*pv[1]
    base=h*h*S
    return [simp(a1*z[0].d[k]+a2*z[1].d[k]+base.d[k]) for k in range(3)]

def one_step(state,which,v,order):
    t,m,b,h,z=state
    if which==1:
        tn,mn,bn=1-1/t,(1-m)/t,b-6*(m-1)**2/t+2
        R=[[-1/t,0],[(1-m)/t,1]]
        phase=s.Rational(32,3)
    else:
        tn,mn,bn=-1/t,1+m/t,b-6*m*m/t-3
        R=[[1/t,0],[-m/t,1]]
        phase=s.Rational(81,8)
    sig=[h*x for x in matvec(periods(t,m,b),v)]
    lin=matvec(R,z)
    vb=[s.Rational(x,order) for x in v]
    affine=matvec(periods(tn,mn,bn),vb)
    zn=[x+y for x,y in zip(lin,affine)]
    F=lambda w:-w[0]*w[0]/(2*t)
    W=F([z[0]+sig[0],z[1]+sig[1]])-F(z)-fperiod(vb,lin,tn,mn,bn)
    line_finite=12*(F(z)+fperiod(vb,lin,tn,mn,bn))+phase
    line_ratio=12*W-phase
    new=tuple(x.reduced() for x in [tn,mn,bn,h-s.Rational(1,order)])+([x.reduced() for x in zn],)
    return new,line_ratio.reduced(),line_finite.reduced()

cases=[
    ((1+2*s.I,s.Rational(1,5)+s.I/7,2-3*s.I),
     (2+s.I,-1+2*s.I,3-s.I),s.Rational(1,7)+s.I/5,1/(2*s.pi*s.I)),
    ((-1+3*s.I,-s.Rational(2,7)+s.I/4,-2-4*s.I),
     (1-2*s.I,2+s.I,-3+2*s.I),-s.Rational(2,9)+s.I/6,2/(3*s.pi*s.I)),
]
for caseid,(vals,dots,h0,hp) in enumerate(cases,1):
    for which,order,v in [(1,3,[1,2,-4,0]),(2,4,[-1,-3,3,0])]:
        z0=[J(s.Rational(2,3)+s.I/5,(0,1,0)),J(-s.Rational(1,4)+s.I/7,(0,0,1))]
        state=tuple(J(x,(d,0,0)) for x,d in zip(vals,dots))+(J(h0,(hp,0,0)),z0)
        initial=state;Ainit=original_connection(initial,v)
        accumulated=[0,0,0];finite_log=J(0);ratio_log=J(0)
        orbit_forms=[]
        for it in range(1,13):
            state,lr,lf=one_step(state,which,v,order)
            finite_log=(finite_log+lf).reduced();ratio_log=(ratio_log+lr).reduced()
            accumulated=[simp(x-y/6) for x,y in zip(accumulated,lr.d)]
            pulled=original_connection(state,v)
            transported=[simp(x+y) for x,y in zip(pulled,accumulated)]
            # Difference of two descended holomorphic connections is a
            # base one-form. These are the two full vertical components.
            ck(f'case{caseid} finite{which} iterate{it} vertical connection descent',
               [transported[1]-Ainit[1],transported[2]-Ainit[2]])
            if it%order==0:
                ck(f'case{caseid} finite{which} iterate{it} FULL connection cycle',
                   [x-y for x,y in zip(transported,Ainit)])
                turns=s.Rational(it,order)
                pshift=matvec(periods(*initial[:3]),[turns*x for x in v])
                for j in range(2):
                    ck(f'case{caseid} finite{which} iterate{it} actual affine coordinate{j}',
                       state[4][j].v-initial[4][j].v-pshift[j].v)
                # Compare the full corrected line lift with its original
                # lattice factor; the exact residual must be an integer.
                target=12*fperiod([turns*x for x in v],initial[4],*initial[:3])
                residual=simp(finite_log.v-target.v)
                assert residual.is_Integer,('nonintegral line residual',residual)
                ck(f'case{caseid} finite{which} iterate{it} line gauge derivative',
                   [x-y for x,y in zip(finite_log.d,target.d)])
                records.append({'case':caseid,'finite':which,'iterations':it,
                                'lattice_multiple':str(turns),'exact_line_log_residual':str(residual)})

# Independent concrete one-dimensional sign: tau=i, z=p+i q.
# The compatible metric log is 2*pi*q^2. Its curvature coefficient is
# -pi dz wedge dbar z and c1=iF/(2pi)=-i/2 dz wedge dbar z=-dp wedge dq.
p,q,z,bz=s.symbols('p q z bz',real=True)
phi=2*s.pi*((z-bz)/(2*s.I))**2
mixed=s.diff(phi,z,bz)
ck('literal curvature mixed Hessian sign',mixed-s.pi)
chern=-s.I*mixed/(2*s.pi)
complex_wedge=-2*s.I # (dp+i dq) wedge (dp-i dq)
ck('Chern iF/2pi equals dq wedge dp',chern*complex_wedge+1)

out={'checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; same model family',
     'phase':'S6_SERIES_GRIND','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'method':'Independent exact first-jet arithmetic; no prior atlas checker imported.',
     'python':platform.python_version(),'sympy':s.__version__,'result':'PASS',
     'check_count':len(checks),'checks':checks,'cycle_records':records,
     'elapsed_seconds':time.monotonic()-start,
     'scope':'Two generic rational complex period/first-jet inputs, both original affine actions, every iterate1..12, all three one-form directions at every full cycle; universal proof remains in the written draft.'}
dest=Path(__file__).resolve().parent/'finite_collar_jet_verifier.output.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'result':'PASS','check_count':len(checks),'elapsed_seconds':out['elapsed_seconds'],
                  'cycle_records':records,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()},indent=2))
