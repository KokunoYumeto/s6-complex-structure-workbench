"""Independent lifted-period computation by regular finite-root Frobenius frames.

Finite monodromy is obtained algebraically from deck eigencharacters at u=0,
conjugated by Frobenius connection matrices.  No loop integration is used.
The result is compared with the previous closed-loop analytic continuation.
"""
from pathlib import Path
import json,contextlib,io,re
with contextlib.redirect_stdout(io.StringIO()):
    exec(Path(__file__).with_name('connection_monodromy.py').read_text().split("out={'precision'")[0])
from flint import arb
u=s.symbols('u')

def parse(v):
    v=v.replace(' ','')
    if 'j' not in v:return acb(v)
    m=re.match(r'^(.+?)([+-])([0-9.]+(?:e[+-]?\d+)?)j$',v)
    if m:return acb(m.group(1),m.group(2)+m.group(3))
    return acb(0,v[:-1])

def frobenius(kind):
    if kind=='zero':
        lam=u**4;exps=[0,6,3,0,-3,-6];D=3125*u**4+256;u0=s.Rational(1,4);N=360;m=4
    else:
        lam=u**-5;exps=[0,-8,-4,0,4,8];D=3125+256*u**5;u0=s.Rational(1,2);N=250;m=5
    S=s.diag(*[u**v for v in exps])
    GG=(S.inv()*Gamma.subs(l,lam)*S*s.diff(lam,u)+S.inv()*s.diff(S,u)).applyfunc(s.cancel)
    numerator=(GG*D).applyfunc(s.cancel)
    polynomials=[[s.Poly(numerator[i,j],u) for j in range(6)] for i in range(6)]
    d0=D.subs(u,0);dj=s.Poly(D,u).coeff_monomial(u**m)
    coeff=[];raw=[];uc=aq(u0);up=uc
    for n in range(N):
        mn=s.Matrix([[polynomials[i][j].coeff_monomial(u**n) for j in range(6)] for i in range(6)])
        gn=cm(mn)/aq(d0)
        if n>=m:gn-=raw[n-m]*aq(dj/d0)
        raw.append(gn);coeff.append(gn*up);up*=uc
    ys=[I];total=I
    for n in range(N):
        v=Z
        for j in range(n+1):v+=ys[n-j]*coeff[j]
        v/=n+1;ys.append(v);total+=v
    lambda0=lam.subs(u,u0)
    transport0,info=transport([acb(1),aq(lambda0)],190,.3)
    H=recenter(transport0*cm(S.subs(u,u0))*total.inv())
    zeta=(acb(0,1)*acb.pi()*2/m).exp()
    deck=acb_mat([[zeta**(-exps[i]) if i==j else 0 for j in range(6)] for i in range(6)])
    mon=recenter(H*deck*H.inv())
    return mon,H,{'root_order':m,'u0':str(u0),'lambda0':str(lambda0),
                 'series_order':N,'last_series_term':norm(ys[-1]),'path':info}

mon=[];Hs=[];out={'method':__doc__,'precision_digits':ctx.dps}
old=json.loads(Path(__file__).with_name('connection_monodromy.json').read_text())
for kind in ['infinity','zero']:
    T,H,info=frobenius(kind);mon.append(T);Hs.append(H)
    oldM=acb_mat([[parse(v) for v in row] for row in old[kind]['matrix']])
    err=norm(T-oldM)
    print(kind,info,'comparison_error',err,flush=True)
    assert err<1e-70
    out[kind]={'matrix':stringmatrix(T),'root_limit_frame':stringmatrix(H),
               'info':info,'loop_comparison_error':err}

rows=[];rhs=[]
for target,T in zip([t.A,t.B],mon):
 for r in range(6):
  for j in range(1,6):
    row=[acb(0)]*30
    for pp in range(6):row[pp*5+j-1]+=int(target[r,pp])
    for k in range(1,6):row[r*5+k-1]-=T[k,j]
    rows.append(row);rhs.append(T[0,j] if r==0 else acb(0))
arr=np.array([[complex64(z) for z in row] for row in rows])
_,_,piv=qr(arr.T,pivoting=True,mode='economic');chosen=list(piv[:30])
sol=acb_mat([rows[i] for i in chosen]).solve(acb_mat([[rhs[i]] for i in chosen]))
X=acb_mat(6,6);X[0,0]=1
for r in range(6):
 for j in range(1,6):X[r,j]=sol[r*5+j-1,0]
oldX=acb_mat([[parse(v) for v in row] for row in old['intertwiner']])
err=norm(X-oldX);print('period_intertwiner_comparison_error',err,flush=True);assert err<1e-70
out['intertwiner']=stringmatrix(X);out['period_comparison_error']=err
for kind,H in zip(['infinity','zero'],Hs):
    V=X*H
    h=-V[0,3].real/(arb.pi()*625/96)
    err=max(float(abs(V[r,3].real)) for r in range(1,6))
    print('finite_h',kind,h.str(90),'real_line_error',err,flush=True)
    out[kind]['h_b']=h.str(95,radius=False)
    out[kind]['real_line_error']=err
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
