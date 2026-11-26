from pathlib import Path
import sympy as sp

t, z, w = sp.symbols('t z w', real=False)
c = (1-t*t)/(1+t*t)
s = 2*t/(1+t*t)

def simp(a):
    return a.applyfunc(sp.cancel) if isinstance(a, sp.MatrixBase) else sp.cancel(a)

def adj(a, var):
    return a.T.subs(var, 1/var)

def K(var):
    return sp.Matrix([[c*c/var+s*s, c*s*(1/var-1)],
                      [c*s*(1-var), s*s+c*c*var]])

def embed(a, second):
    out = sp.eye(3)
    ix = (0, second)
    for i in range(2):
        for j in range(2):
            out[ix[i],ix[j]] = a[i,j]
    return out

checks = []
def check(name, actual, expected):
    assert simp(actual-expected) == (sp.zeros(*actual.shape)
                                    if isinstance(actual, sp.MatrixBase) else 0), name
    checks.append(name)

check('rational circle identity', c*c+s*s, 1)
for var in (z,w):
    q=sp.Matrix([[c/var,-s],[s,c*var]])
    k=K(var)
    check(f'Q inverse ({var})',q*adj(q,var),sp.eye(2))
    check(f'K product formula ({var})',q*adj(q.subs(var,1),var),k)
    check(f'K inverse left ({var})',k*adj(k,var),sp.eye(2))
    check(f'K inverse right ({var})',adj(k,var)*k,sp.eye(2))
    check(f'K determinant ({var})',k.det(),1)
    check(f'K first endpoint ({var})',k.subs(t,0),sp.diag(1/var,var))
    check(f'K last endpoint ({var})',k.subs(t,1),sp.eye(2))
    check(f'K based seam ({var})',k.subs(var,1),sp.eye(2))
a,b=embed(K(z),1),embed(K(w),2)
C=a*b
Cinv=embed(adj(K(w),w),2)*embed(adj(K(z),z),1)
check('embedded inverse left',C*Cinv,sp.eye(3))
check('embedded inverse right',Cinv*C,sp.eye(3))
check('full first endpoint',C.subs(t,0),sp.diag(1/(z*w),z,w))
check('full last endpoint',C.subs(t,1),sp.eye(3))
check('full based seam',C.subs({z:1,w:1}),sp.eye(3))
out='Exact rational/Laurent contraction verification\n'+'\n'.join('PASS '+x for x in checks)+'\n'
Path(__file__).with_suffix('.out').write_text(out,newline='\n')
print(out,end='')
