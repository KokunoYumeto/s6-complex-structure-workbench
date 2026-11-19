"""Certified complex-ball continuation with explicit Cauchy tail bounds.

For each Taylor step choose a disk of radius R avoiding both finite poles.
In a fixed positive diagonal gauge bound ||Gamma||_infty by M on this disk.
Gronwall gives ||U|| <= exp(M R).  Cauchy therefore bounds the omitted
Taylor tail by exp(M R)*(|h|/R)^(N+1)/(1-|h|/R).  The error is added to
every matrix entry with its gauge factor.  No interval radius is discarded.
Finite meridians here use rational polygonal paths, independent of the
circle paths used for the preliminary numerical values.
"""
from pathlib import Path
import json,contextlib,io
with contextlib.redirect_stdout(io.StringIO()):
    exec(Path(__file__).with_name('connection_monodromy.py').read_text().split("out={'precision'")[0])
from flint import arb,arb_mat

terms={}
for i in range(6):
 for j in range(6):
    e=Gamma[i,j]
    if not e:continue
    poly=s.Poly(s.cancel(e*l**3*(l-cusp)),l)
    low=min(m[0] for m,c in poly.terms())
    shift=min(3,low)
    poly=s.Poly(poly.as_expr()/l**shift,l)
    terms[i,j]=(3-shift,[(m[0],abs(c)) for m,c in poly.terms()])

stats=[]
def upperfloat(v):
    # Factor two strictly dominates conversion rounding and enclosure width.
    return 2.0*float(v.abs_upper())

def certified_step(z,h):
    az=abs(z);ad=abs(z-aa)
    dist=min(float(az.lower()),float(ad.lower()))
    # The 0.1% margin dominates IEEE conversion error in this finite range.
    R=arb(str(.449*dist))
    rho=abs(h)/R
    assert rho<arb('0.8')
    exponent=0.75 if float(az)<1 else 0.8
    powers=[0,2,1,0,-1,-2]
    weights=[arb(2)**round(exponent*j*math.log2(float(az))) for j in powers]
    bound=[arb(0) for _ in range(6)]
    for (i,j),(pole,cs) in terms.items():
        num=sum((arb(int(c.p))/int(c.q))*(az+R)**degree for degree,c in cs)
        ent=num/((az-R)**pole*(ad-R))*weights[j]/weights[i]
        bound[i]+=ent
    M=arb(str(max(upperfloat(v) for v in bound)))
    MR=M*R
    N=max(180,math.ceil((float(MR)+160)/(-math.log(float(rho)))))
    tail=(MR.exp()*rho**(N+1)/(1-rho))
    while not tail<arb('1e-65'):
        N+=20;tail=MR.exp()*rho**(N+1)/(1-rho)
    coeff=[];q0=-h/z;qa=-h/(z-aa);p0=acb(1);pa=acb(1)
    for n in range(N):
        C=(parts[-1]*(1/z)+parts[-2]*((n+1)/(z*z))
           +parts[-3]*((n+1)*(n+2)/(2*z*z*z)))*p0
        C+=Ra*(pa/(z-aa))
        if n==0:C+=parts[0]+parts[1]*z
        if n==1:C+=parts[1]*h
        coeff.append(C*h);p0*=q0;pa*=qa
    ys=[I];total=I
    for n in range(N):
        v=Z
        for j in range(n+1):v+=ys[n-j]*coeff[j]
        v/=n+1;ys.append(v);total+=v
    for i in range(6):
     for j in range(6):
        eps=tail*weights[i]/weights[j]
        total[i,j]+=acb(arb(0,eps),arb(0,eps))
    stats.append({'N':N,'MR_upper':str(MR.upper()),'rho_upper':str(rho.upper()),
                  'tail_upper':str(tail.upper())})
    return total

def certified_transport(vertices):
    T=I;z=vertices[0]
    for target in vertices[1:]:
        while float(abs(target-z).upper())>1e-90:
            diff=target-z
            dist=min(float(abs(z).lower()),float(abs(z-aa).lower()))
            n=max(1,math.ceil(float(abs(diff).upper())/(.19*dist)))
            h=diff/n
            U=certified_step(z,h);T=T*U;z=target if n==1 else z+h
    return T

def polygon(radius,sgn):
    r=acb(radius)
    return [r,r+acb(0,sgn)*r,acb(0,sgn)*r,-r+acb(0,sgn)*r,
            -r,-r-acb(0,sgn)*r,-acb(0,sgn)*r,r-acb(0,sgn)*r,r]

mon=[]
for kind,radius,sgn in [('infinity','2',-1),('zero','0.01',1)]:
    vertices=[acb(1),acb(radius)]+polygon(radius,sgn)[1:]+[acb(1)]
    T=certified_transport(vertices);mon.append(T)
    print(kind,'steps',len(stats),'maxN',max(d['N'] for d in stats),flush=True)
    print('entry00',T[0,0].str(80),flush=True)

rows=[];rhs=[]
for target,T in zip([t.A,t.B],mon):
 for r in range(6):
  for j in range(1,6):
    row=[acb(0)]*30
    for pp in range(6):row[pp*5+j-1]+=int(target[r,pp])
    for k in range(1,6):row[r*5+k-1]-=T[k,j]
    rows.append(row);rhs.append(T[0,j] if r==0 else acb(0))
arr=np.array([[complex(float(z.real.mid()),float(z.imag.mid())) for z in row] for row in rows])
_,_,piv=qr(arr.T,pivoting=True,mode='economic');chosen=list(piv[:30])
sol=acb_mat([rows[i] for i in chosen]).solve(acb_mat([[rhs[i]] for i in chosen]))
X=acb_mat(6,6);X[0,0]=1
for r in range(6):
 for j in range(1,6):X[r,j]=sol[r*5+j-1,0]

# The exact existence of the intertwiner and real intersection vector is
# proved in the notes; solving independent subsets encloses those solutions.
rows=[];rhs=[]
for r in range(1,6):
    rows.append([X[r,1].imag,X[r,1].real,X[r,2].imag,X[r,2].real])
    rhs.append(X[r,3].real)
arr=np.array([[float(z.mid()) for z in row] for row in rows])
_,_,piv=qr(arr.T,pivoting=True,mode='economic');chosen=list(piv[:4])
sol=arb_mat([rows[i] for i in chosen]).solve(arb_mat([[rhs[i]] for i in chosen]))
v=[acb(sol[0,0],sol[1,0]),acb(sol[2,0],sol[3,0]),acb(0,-1)]
lift=sum((X[0,j+1]*v[j] for j in range(3)),acb(0))
hh=lift.imag/(arb.pi()*625/96)
print('certified_h_b_at_1',hh.str(100),flush=True)
print('certifies_h_less_than_minus_one',hh<arb(-1),flush=True)
assert hh<arb(-1)
out={'proof_of_tail':__doc__,'precision_digits':ctx.dps,'step_bounds':stats,
     'h_b_at_1':hh.str(100),'certified_h_less_than_minus_one':True,
     'X':[[X[i,j].str(100) for j in range(6)] for i in range(6)]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
