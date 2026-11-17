"""Exact two-variable normalization and marked boundary for a general cusp.

Theorem D.2.43: a same-fan triangular cusp with period lattice L has
H2 = Z^(det L+3) + Z_s, where s is the first Smith factor of L.
The fibre kernel is im(wedge(A)-I) plus the primitive angular area;
it is not saturated when s>1.
"""
from pathlib import Path
from math import gcd
import json
import sympy as S
from manifolds_rankone_families import wedge
from manifolds_weighted_profiles import group

ROOT=Path(__file__).resolve().parents[1]
x,y=S.symbols('x y')
C=[S.Matrix(v) for v in [(0,1,0,0),(1,-1,-1,0),(0,0,1,0),
                         (1,0,-1,-1),(0,0,0,1),(1,-1,0,-1)]]
J=S.diag(1,-1,-1,-1)
B=S.Matrix.vstack(*[((C[i]-[1/x,y,x*y][i]*C[i+3]).T*J) for i in range(3)])
U=S.eye(3);V=S.eye(4);R=B.copy()
def row_add(i,j,c):
    global R,U
    R[i,:]+=c*R[j,:];U[i,:]+=c*U[j,:]
R[0,:]*=-x;U[0,:]*=-x
for i in [1,2]:row_add(i,0,-R[i,0])
for j in [1,2,3]:
    q=R[0,j];R[:,j]-=q*R[:,0];V[:,j]-=q*V[:,0]
row_add(2,1,x*y)
assert S.simplify(U*B*V-R)==S.zeros(3,4)
F=R[1:,1:].T
expected=S.Matrix([[1-x,0],[0,x*y-1],[y-1,x*y*(y-1)]])
assert S.simplify(F-expected)==S.zeros(3,2)
T=S.Matrix([[0,0,-1/x],[-1/(x*y*y),1/(x*y),-1/(x*x*y)],[-1/y,0,0]])
standard=S.Matrix([[-(y-1),0],[x-1,-(y-1)],[0,x-1]])
source=S.Matrix([[y,x*y*y],[x,0]])
assert S.simplify(T.inv()*F-standard*source)==S.zeros(3,2)
assert S.factor(T.det())==-1/(x*x*y*y)
assert S.factor(source.det())==-x*x*y*y
generators=S.Matrix([[-(x*y-1)*(y-1),-x*y*(1-x)*(y-1),(1-x)*(x*y-1)]])
assert S.simplify(generators*T-S.Matrix([[(x-1)**2,(x-1)*(y-1),(y-1)**2]]))==S.zeros(1,3)
symbolic=dict(ring='Z[x^+-1,y^+-1]',opposite_weights=['x^-1','y','xy'],
             restriction=str(B),left=str(U),right=str(V),cancelled=str(R),
             target_change=str(T),source_change=str(source),
             hilbert_burch=str(standard),ideal='(x-1,y-1)^2')

def finite_case(a,b,c):
    """Columns (a,0),(b,c), with 0<=b<a; cosets (i,j)."""
    assert a>0 and c>0 and 0<=b<a
    D=a*c;s=gcd(a,b,c);t=D//s
    X=S.zeros(D);Y=S.zeros(D)
    for i in range(a):
        for j in range(c):
            X[((i+1)%a)*c+j,i*c+j]=1
            if j+1<c:Y[i*c+j+1,i*c+j]=1
            else:Y[((i-b)%a)*c,i*c+j]=1
    assert X*Y==Y*X and X**a==S.eye(D) and X**b*Y**c==S.eye(D)
    N=S.zeros(3*D,4*D)
    for i,W in enumerate([X.inv(),Y,X*Y]):
        for j in range(4):
            N[i*D:(i+1)*D,j*D:(j+1)*D]=J[j,j]*(C[i][j]*S.eye(D)-C[i+3][j]*W)
    normalized=group(N.T)
    assert normalized==dict(free=D+2,torsion=([s] if s>1 else []))
    L=S.Matrix([[a,b],[0,c]])
    A=S.eye(4);A[:2,2:]=L
    exterior=wedge(A)-S.eye(6)
    local=group(exterior)
    assert local==dict(free=4,torsion=([s,s] if s>1 else []))
    angular=S.eye(6)[:,0]
    image=group(exterior.row_join(angular))
    assert image==dict(free=4,torsion=([s] if s>1 else []))
    # The component-ray meridians in angular coinvariants plus the base.
    meridians=S.Matrix([[i for i in range(a) for j in range(c)],
                        [j for i in range(a) for j in range(c)],
                        [1 for i in range(a) for j in range(c)]])
    rel=L.col_join(S.zeros(1,2))
    assert group(rel.row_join(meridians))==dict(free=0,torsion=[])
    return dict(lattice=L.tolist(),index=D,smith=[s,t],
                normalization_H2=normalized,
                cap_H2=dict(free=D+3,torsion=([s] if s>1 else [])),
                boundary_H2=dict(free=6,torsion=([s,s] if s>1 else [])),
                regular_fibre_image=image,monodromy=A.tolist(),
                full_fibre_kernel_generators=exterior.row_join(angular).tolist(),
                component_meridians=meridians.tolist())

if __name__=='__main__':
    cases=[]
    for a in range(1,6):
        for c in range(1,6):
            for b in range(a):cases.append(finite_case(a,b,c))
    print('Symbolic Laurent unimodular reduction to the squared augmentation ideal: PASS')
    print('Finite HNF period-lattice normalizations and exact marked fibre kernels:',len(cases))
    print('Noncyclic torsion cases:',sum(v['smith'][0]>1 for v in cases))
    (ROOT/'records/manifolds_general_cusp.json').write_text(
        json.dumps(dict(symbolic=symbolic,cases=cases),indent=2,default=int)+'\n')
