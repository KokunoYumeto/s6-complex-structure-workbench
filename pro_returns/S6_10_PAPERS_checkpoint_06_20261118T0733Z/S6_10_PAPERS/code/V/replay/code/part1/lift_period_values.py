"""Period planes and h from the explicit algebraic lift in the input marking.

The normalization is the first extension form of de_rham_connection.py,
Xe0=e0, and alpha=(625*pi*i/128)*alpha_alg.  It differs by an explicitly
allowed scalar splitting translation from other normalizations of sigma.
"""
from pathlib import Path
import contextlib,io,json,re
with contextlib.redirect_stdout(io.StringIO()):
    exec(Path(__file__).with_name('connection_monodromy.py').read_text().split("out={'precision'")[0])
from flint import arb_mat,arb

def parse(v):
    v=v.replace(' ','')
    if 'j' not in v:return acb(v)
    m=re.match(r'^(.+?)([+-])([0-9.]+(?:e[+-]?\d+)?)j$',v)
    if m:return acb(m.group(1),m.group(2)+m.group(3))
    return acb(0,v[:-1])

old=json.loads(Path(__file__).with_name('connection_monodromy.json').read_text())
X=acb_mat([[parse(v) for v in row] for row in old['intertwiner']])

def hvalue(Y):
    # The real intersection vector is normalized by its w0 coefficient -i.
    rows=[];rhs=[]
    for r in range(1,6):
        rows.append([Y[r,1].imag,Y[r,1].real,Y[r,2].imag,Y[r,2].real])
        rhs.append(Y[r,3].real)
    arr=np.array([[float(z) for z in row] for row in rows])
    _,_,piv=qr(arr.T,pivoting=True,mode='economic');chosen=list(piv[:4])
    sol=arb_mat([rows[i] for i in chosen]).solve(arb_mat([[rhs[i]] for i in chosen]))
    v=[acb(sol[0,0],sol[1,0]),acb(sol[2,0],sol[3,0]),acb(0,-1)]
    rv=Y*acb_mat([[0],[v[0]],[v[1]],[v[2]],[0],[0]])
    realerr=max(float(abs(rv[r,0].imag)) for r in range(1,6))
    h=rv[0,0].imag/(arb.pi()*625/96)
    return h,realerr,v

def plane(Y,c):
    F=acb_mat([[Y[r,j] for j in [1,2,3]] for r in range(6)])
    F[0,2]-=acb.pi()*625*c/96
    both=acb_mat([[F[r,j] if j<3 else F[r,j-3].conjugate() for j in range(6)] for r in range(6)])
    return F,both.det()

out={'normalization':__doc__,'points':[]}
for lam in [1,2]:
    Y=X if lam==1 else X*transport([acb(1),acb(lam)],190,.3)[0]
    h,err,v=hvalue(Y)
    values={}
    print('lambda',lam,'h',h.str(80),'real_intersection_error',err,flush=True)
    for c in [0,1,10]:
        F,det=plane(Y,c)
        print('c',c,'det[F,Fbar]',det.str(80),'h+c',(h+c).str(80),flush=True)
        values[str(c)]={'F':stringmatrix(F),'determinant':det.str(90,radius=False)}
    out['points'].append({'lambda':lam,'h':h.str(90,radius=False),
                          'intersection_error':err,'values':values})
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
