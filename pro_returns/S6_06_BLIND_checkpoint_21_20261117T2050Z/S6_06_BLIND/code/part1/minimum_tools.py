"""Exact root-chart recurrences and interval helpers for global h minimization."""
from pathlib import Path
import json,contextlib,io,math,re
with contextlib.redirect_stdout(io.StringIO()):
    exec(Path(__file__).with_name('certified_lift_bound.py').read_text().split('mon=[]')[0])
from flint import acb_poly,arb_poly
u=s.symbols('u')

def ballparse(v):
    if 'j' not in v:return acb(arb(v))
    rr,ii=v.rsplit(' + ',1)
    return acb(arb(rr),arb(ii[:-1]))

cert=json.loads(Path(__file__).with_name('certified_lift_bound.json').read_text())
X=acb_mat([[ballparse(v) for v in row] for row in cert['X']])

def root_data(kind):
    if kind=='zero':
        lam=u**4;exps=[0,6,3,0,-3,-6];D=3125*u**4+256;m=4
        radius=aq(-cusp)**(acb(1)/4)
        u0=s.Rational(1,4)
    else:
        lam=u**-5;exps=[0,-8,-4,0,4,8];D=3125+256*u**5;m=5
        radius=(1/aq(-cusp))**(acb(1)/5)
        u0=s.Rational(1,2)
    S=s.diag(*[u**v for v in exps])
    GG=(S.inv()*Gamma.subs(l,lam)*S*s.diff(lam,u)+S.inv()*s.diff(S,u)).applyfunc(s.cancel)
    num=(GG*D).applyfunc(s.cancel)
    polynomials=[[s.Poly(num[i,j],u) for j in range(6)] for i in range(6)]
    deg=max(v.degree() for row in polynomials for v in row if not v.is_zero)
    Bs=[]
    for n in range(deg+1):
        mn=s.Matrix([[polynomials[i][j].coeff_monomial(u**n) for j in range(6)] for i in range(6)])
        Bs.append(cm(mn)*radius**(n+1)/aq(D.subs(u,0)))
    absolute=np.array([[sum(float(abs(B[i,j]).upper()) for B in Bs) for j in range(6)] for i in range(6)])
    # A positive Perron vector supplies a diagonal gauge; dyadic rounding
    # retains exact gauge entries and the row norm below is rounded up.
    eigenval,eigenvec=np.linalg.eig(absolute+np.ones((6,6))*1e-15)
    v=np.abs(eigenvec[:,np.argmax(eigenval.real)].real)
    v/=max(v)
    weights=[arb(2)**round(math.log2(max(float(c),2**-40))) for c in v]
    Bmax=max(sum(sum(abs(B[i,j]) for B in Bs)*weights[j]/weights[i] for j in range(6)) for i in range(6))
    return {'kind':kind,'lam':lam,'S':S,'m':m,'radius':radius,'Bs':Bs,'weights':weights,'Bmax':Bmax,'u0':u0}

def root_coeffs(data,N):
    m=data['m'];Bs=data['Bs'];ys=[I]
    for n in range(1,N+1):
        v=-(n-m)*ys[n-m] if n>=m else Z
        for j in range(min(len(Bs),n)):v+=ys[n-j-1]*Bs[j]
        ys.append(v/n)
    return ys

def root_tail(data,N,r,R=arb('0.999')):
    # Integral bound: 1/(1-t^m) <= 1/(m(1-t))+(m-1)/m.
    m=data['m'];B=data['Bmax']
    growth=(B*((-(1-R).log())/m+(m-1)*R/m)).exp()
    return growth*(r/R)**(N+1)/(1-r/R)

def matrix_series(ys,z):
    out=Z
    for Y in ys[::-1]:out=out*z+Y
    return out

def add_tail(V,tail,weights):
    result=acb_mat(V)
    for i in range(6):
     for j in range(6):
        eps=tail*weights[i]/weights[j]
        result[i,j]+=acb(arb(0,eps),arb(0,eps))
    return result

def root_frame(data,ys):
    z0=aq(data['u0'])/data['radius']
    U=matrix_series(ys,z0)
    U=add_tail(U,root_tail(data,len(ys)-1,abs(z0)),data['weights'])
    lam0=data['lam'].subs(u,data['u0'])
    tr=certified_transport([acb(1),aq(lam0)])
    return X*tr*cm(data['S'].subs(u,data['u0']))*U.inv()

if __name__=='__main__':
    for kind in ['infinity','zero']:
        data=root_data(kind)
        print(kind,'Bmax',data['Bmax'],'weights',data['weights'],'degree',len(data['Bs'])-1,flush=True)
        for N in [1000,2000,4000]: print('N',N,'tail_at_.98',root_tail(data,N,arb('.98')),flush=True)
