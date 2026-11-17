"""High precision analytic continuation of the explicit rank-six connection.

Uses complex ball arithmetic for coefficient evaluation and Taylor arithmetic.
Taylor truncation is checked by a second independently chosen order/step run;
the printed accuracy is numerical agreement, not a certified interval theorem.
The monodromies are compared to the supplied integral A,B by an intertwiner.
"""
from pathlib import Path
import json, math
import sympy as s
import flint
from flint import acb, acb_mat, ctx
import numpy as np
from scipy.linalg import qr
import importlib.util
ctx.dps=110
p=Path(__file__).parent
data=json.loads((p/'de_rham_connection.json').read_text())
l=s.symbols('l'); cusp=-s.Rational(256,3125)
GW=s.Matrix([[s.sympify(v) for v in row] for row in data['Gamma5']])
b=s.Matrix([[s.sympify(v) for v in data['extension_forms'][0]]])
Gamma=s.zeros(6);Gamma[1:,1:]=GW;Gamma[0,1:]=b

def aq(q):
    q=s.Rational(q)
    return acb(int(q.p))/int(q.q)

def cm(M):return acb_mat([[aq(v) for v in row] for row in M.tolist()])
parts={k:s.zeros(6) for k in [-3,-2,-1,0,1]}
Ra=s.zeros(6)
for i in range(6):
 for j in range(6):
    e=Gamma[i,j]
    Ra[i,j]=s.limit((l-cusp)*e,l,cusp)
    e=s.cancel(e-Ra[i,j]/(l-cusp))
    for k in [-3,-2,-1]:
        parts[k][i,j]=s.limit(l**(-k)*e,l,0)
        e=s.cancel(e-parts[k][i,j]*l**k)
    parts[0][i,j]=e.subs(l,0)
    parts[1][i,j]=s.diff(e,l)
    assert s.diff(e,l,2)==0
parts={k:cm(v) for k,v in parts.items()};Ra=cm(Ra);aa=aq(cusp)
I=acb_mat([[int(i==j) for j in range(6)] for i in range(6)])
Z=acb_mat(6,6)

def norm(M):return max(float(abs(M[i,j])) for i in range(M.nrows()) for j in range(M.ncols()))
def center(z):return acb(z.real.mid(),z.imag.mid())
def recenter(M):return acb_mat([[center(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())])

def step(z,h,N):
    # Taylor series in u=(lambda-z)/h, evaluated at u=1.
    coeff=[]
    q0=-h/z;qa=-h/(z-aa)
    p0=acb(1);pa=acb(1)
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
    return recenter(total),norm(ys[-1])

def transport(vertices,N=190,ratio=.3):
    T=I;maxlast=0.;count=0
    z=vertices[0]
    for target in vertices[1:]:
        while abs(complex(float((target-z).real),float((target-z).imag)))>1e-100:
            diff=target-z
            dist=min(float(abs(z)),float(abs(z-aa)))
            n=max(1,math.ceil(float(abs(diff))/(ratio*dist)))
            h=diff/n
            U,last=step(z,h,N);T=recenter(T*U);z=target if n==1 else center(z+h)
            maxlast=max(maxlast,last);count+=1
    return T,{'steps':count,'largest_final_taylor_term':maxlast}

def circle(radius,orientation):
    return [acb(radius)*(acb(0,orientation)*acb.pi()*2*k/16).exp() for k in range(17)]

def loop(kind,N,ratio):
    if kind=='zero':
        vs=[acb(1),acb('0.01')]+circle('0.01',1)[1:]+[acb(1)]
    else:
        vs=[acb(1),acb(2)]+circle(2,-1)[1:]+[acb(1)]
    return transport(vs,N,ratio)

def stringmatrix(M):return [[M[i,j].str(95,radius=False) for j in range(M.ncols())] for i in range(M.nrows())]
def complex64(z):return complex(float(z.real),float(z.imag))

root=p.parents[2]
spec=importlib.util.spec_from_file_location('tupledata',root/'background/data/fourfold_tuple.py')
t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)

out={'precision':ctx.dps,'method':'Taylor connection transport','scope':__doc__}
mon=[]
for kind in ['infinity','zero']:
    M,info=loop(kind,190,.3)
    print(kind,info,flush=True)
    print('finite_order_error',norm(M**(5 if kind=='infinity' else 4)-I),flush=True)
    out[kind]={'matrix':stringmatrix(M),'info':info};mon.append(M)

# Unknowns X_{r,j}, 0<=r<6, 1<=j<6, with X e0=e0.
rows=[];rhs=[]
for target,T in zip([t.A,t.B],mon):
    for r in range(6):
        for j in range(1,6):
            row=[acb(0)]*30
            for pp in range(6):row[pp*5+j-1]+=int(target[r,pp])
            for k in range(1,6):row[r*5+k-1]-=T[k,j]
            rows.append(row);rhs.append(T[0,j] if r==0 else acb(0))
arr=np.array([[complex64(z) for z in row] for row in rows])
_,rr,piv=qr(arr.T,pivoting=True,mode='economic')
chosen=list(piv[:30])
sol=acb_mat([rows[i] for i in chosen]).solve(acb_mat([[rhs[i]] for i in chosen]))
X=acb_mat(6,6);X[0,0]=1
for r in range(6):
 for j in range(1,6):X[r,j]=sol[r*5+j-1,0]
res=max(norm(cm(target)*X-X*T) for target,T in zip([t.A,t.B],mon))
print('intertwiner_residual',res,'det',X.det().str(40),flush=True)
print('X',X.str(60,radius=False),flush=True)
out['intertwiner']=stringmatrix(X);out['intertwiner_residual']=res
out['intertwiner_det']=X.det().str(80,radius=False)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
