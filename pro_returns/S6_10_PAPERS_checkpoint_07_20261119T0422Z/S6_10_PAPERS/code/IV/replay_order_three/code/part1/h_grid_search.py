"""Bounded numerical search for the minimum of h; not a certification.

Two finite root disks cover |lambda|<|lambda*| and |lambda|>|lambda*|.
The search uses their normalized radii <=0.98, 25 radial levels and 64
angular levels in a fundamental sector.  The missing annular collar is
explicitly not included in the claimed search bounds.
"""
from pathlib import Path
import json,contextlib,io,csv
with contextlib.redirect_stdout(io.StringIO()):
    exec(Path(__file__).with_name('frobenius_period_check.py').read_text().split('mon=[]')[0])

saved=json.loads(Path(__file__).with_name('frobenius_period_check.json').read_text())
X=acb_mat([[parse(v) for v in row] for row in saved['intertwiner']])
N=650;out=[]
for kind in ['infinity','zero']:
    if kind=='zero':
        lam=u**4;exps=[0,6,3,0,-3,-6];D=3125*u**4+256;m=4
        radius=aq(-cusp)**(acb(1)/4)
    else:
        lam=u**-5;exps=[0,-8,-4,0,4,8];D=3125+256*u**5;m=5
        radius=(1/aq(-cusp))**(acb(1)/5)
    S=s.diag(*[u**v for v in exps])
    GG=(S.inv()*Gamma.subs(l,lam)*S*s.diff(lam,u)+S.inv()*s.diff(S,u)).applyfunc(s.cancel)
    num=(GG*D).applyfunc(s.cancel)
    polynomials=[[s.Poly(num[i,j],u) for j in range(6)] for i in range(6)]
    d0=D.subs(u,0);dj=s.Poly(D,u).coeff_monomial(u**m)
    coeff=[];raw=[];up=radius
    for n in range(N):
        mn=s.Matrix([[polynomials[i][j].coeff_monomial(u**n) for j in range(6)] for i in range(6)])
        gn=cm(mn)/aq(d0)
        if n>=m:gn-=raw[n-m]*aq(dj/d0)
        raw.append(gn);coeff.append(gn*up);up*=radius
    ys=[I]
    for n in range(N):
        v=Z
        for j in range(n+1):v+=ys[n-j]*coeff[j]
        v/=n+1;ys.append(v)
    polys=[np.array([[complex64(v[i,j]) for j in range(6)] for i in range(6)]) for v in ys]
    H=acb_mat([[parse(v) for v in row] for row in saved[kind]['root_limit_frame']])
    HH=X*H;HH=np.array([[complex64(HH[i,j]) for j in range(6)] for i in range(6)])
    def evalh(z):
        V=np.zeros((6,6),complex)
        for coef in polys[::-1]:V=V*z+coef
        V=HH@V
        mat=np.column_stack([V[1:,1].imag,V[1:,1].real,V[1:,2].imag,V[1:,2].real])
        sol=np.linalg.lstsq(mat,V[1:,3].real,rcond=None)[0]
        v=np.array([sol[0]+1j*sol[1],sol[2]+1j*sol[3],-1j])
        return (V[0,1:4]@v).imag/(625*np.pi/96)
    vals=[]
    for rr in np.linspace(0,.98,26):
      for j in range(64 if rr else 1):
        theta=2*np.pi*j/(m*64);z=rr*np.exp(1j*theta)
        h=evalh(z);row=[kind,rr,theta,z.real,z.imag,h];out.append(row);vals.append(row)
    best=min(vals,key=lambda r:r[-1])
    print(kind,'series_order',N,'search_minimum',best,'center_h',saved[kind]['h_b'],flush=True)
with Path(__file__).with_suffix('.csv').open('w') as f:
    w=csv.writer(f);w.writerow(['chart','normalized_radius','angle','z_real','z_imag','h']);w.writerows(out)
