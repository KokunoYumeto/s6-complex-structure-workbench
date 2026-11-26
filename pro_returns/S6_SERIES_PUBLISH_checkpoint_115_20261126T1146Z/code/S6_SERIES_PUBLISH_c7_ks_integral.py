"""Independent exact calculations for the fresh 02KS continuation.

Reads only the admitted defining fixture, never a target proof or old program.
All integer inverse matrices are retained in the JSON beside the fresh proof.
"""
from pathlib import Path
from itertools import combinations
import json
import sympy as S
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation7_iii_ks'
OUT.mkdir(exist_ok=True)
data = json.loads((ROOT / 'agents/continuation6_iii_carriers/S6_SERIES_PUBLISH_III_02KS_raw_definitions.json').read_text())
row = data['rows'][0]
maps = {}

def save(name, A):
    maps[name] = [[str(x) for x in r] for r in A.tolist()]
    print(name, A.tolist())

def snf(A):
    D, U, V = smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(S.ZZ))
    D, U, V = (x.to_Matrix() for x in (D,U,V))
    assert U*A*V == D and abs(U.det()) == abs(V.det()) == 1
    return D,U,V

def save_smith(name,A):
    D,U,V=snf(A)
    Ui,Vi=U.inv(),V.inv()
    assert U*Ui==Ui*U==S.eye(U.rows)
    assert V*Vi==Vi*V==S.eye(V.rows)
    assert Ui*D*Vi==A
    save(name+'_smith_diagonal',D)
    save(name+'_smith_left',U);save(name+'_smith_right',V)
    save(name+'_smith_left_inverse',Ui);save(name+'_smith_right_inverse',Vi)
    return D,U,V

def wedge(A):
    ij = list(combinations(range(A.rows), 2))
    return S.Matrix([[A.extract(i,j).det() for j in ij] for i in ij])

J=S.Matrix([[0,1],[-1,0]])
Ts=[]
for i,(ar,gr,w) in enumerate(zip(row['elliptic_matrices'],row['generator_section_cocycle'],data['weights'])):
    A,g=S.Matrix(ar),S.Matrix(gr)
    if i==1:
        z=S.Matrix([-S.Rational(4,3),0])
    else:
        z=(A-S.eye(2)).inv()*g
    assert (A-S.eye(2))*z==g
    b=-12*z.T*J
    beta=-12*g.T*J*A
    T=S.eye(4);T[:2,:2]=A;T[:2,3]=g;T[2,:2]=beta;T[2,3]=(beta*z)[0]+w
    C=S.eye(4);C[:2,3]=z;C[2,:2]=b;C[2,3]=(b*z)[0]
    L=S.diag(1,1,1,1);L[:2,:2]=A;L[2,3]=w
    assert C.inv()*L*C==T
    Ts.append(T)
    save(f'T{i}',T);save(f'S{i}',C);save(f'S{i}_inverse',C.inv())
assert Ts[0]*Ts[1]*Ts[2]==S.eye(4)

# These are basis changes on the same KS star, not an identification of
# two distinct elliptic-surface germs.  The geometric construction is
# performed on the KS germ itself in fresh derivation section 3.
star_C=S.Matrix([[1,1],[-1,0]])
star_P=S.diag(star_C,S.eye(2))
assert star_P.inv()*Ts[2]*star_P==S.Matrix([[-1,-1,0,-1],[0,-1,0,1],[-12,-24,1,3],[0,0,0,1]])
save('star_marking_change',star_P);save('star_marking_change_inverse',star_P.inv())
star_l=S.Matrix([[4,0,-3,0,-1,0]])
star_d=S.Matrix([[0,0,-9,0,-3,1]])
star_ld=star_l.col_join(star_d)
star_section=S.zeros(6,2);star_section[4,0]=-1;star_section[5,0]=-3;star_section[5,1]=1
assert star_ld*star_section==S.eye(2)
assert star_ld*(wedge(Ts[2])-S.eye(6))==S.zeros(2,6)
star_D,_,_=save_smith('star_wedge_relation',wedge(Ts[2])-S.eye(6))
assert [abs(star_D[i,i]) for i in range(6)]==[1,1,1,1,0,0]
save('star_H2_boundary_rows',star_ld);save('star_H2_boundary_section',star_section)
star_component=S.zeros(6)
for source,target in enumerate([2,3,1,0,5,4]):star_component[target,source]=1
star_coinv=S.Matrix([[1,1,1,1,0,0],[0,0,0,0,1,1]])
star_orbit_section=S.zeros(6,2);star_orbit_section[0,0]=1;star_orbit_section[4,1]=1
star_inv=star_coinv.T
assert star_coinv*star_orbit_section==S.eye(2)
assert star_coinv*(star_component-S.eye(6))==S.zeros(2,6)
assert (star_component-S.eye(6))*star_inv==S.zeros(6,2)
assert star_coinv*S.Matrix([1,1,1,1,2,2])==S.Matrix([4,4])
save('star_forward_component_permutation',star_component)
save('star_component_coinvariants',star_coinv);save('star_component_section',star_orbit_section)
save('star_component_invariants',star_inv)

E=S.eye(4)
delta=E[:,2]; gamma=E[:,3]
lam=S.Matrix([-2,1,-16,0])
ell_ii=S.Matrix([-1,1,0,1]);ell_star=S.Matrix([-1,3,0,4])
H=S.Matrix.hstack(lam,S.Matrix([-1,0,0,0]),delta,gamma)
assert H.det()==1
save('cusp_basis',H);save('cusp_basis_inverse',H.inv());save('cusp_nilpotent',H.inv()*Ts[1]*H-S.eye(4))

D=S.zeros(4,4).row_join(Ts[0]-S.eye(4)).row_join(Ts[1]-S.eye(4))
def j(i,x):
    if i==3:
        return -((Ts[0]*Ts[1]*x).col_join(Ts[1]*x).col_join(x))
    result=S.zeros(12,x.cols);result[4*i:4*i+4,:]=x;return result
assert D*j(3,E)==E-Ts[2].inv()
K=S.Matrix.hstack(j(1,delta),j(1,ell_ii),j(2,lam),j(2,delta),j(3,delta),j(3,ell_star),j(0,E[:,0]),j(0,E[:,1]),j(0,gamma))
C=S.zeros(12,3)
C[5,:]=S.Matrix([[1,2,0]])
C[8,:]=S.Matrix([[-1,19,4]])
C[11,:]=S.Matrix([[0,16,3]])
A=C.row_join(K)
assert D*K==S.zeros(4,9)
assert D*C==S.diag(1,1,3).col_join(S.zeros(1,3))
assert A.det()==-1
Ai=A.inv();L=Ai[3:,:]
assert L*K==S.eye(9)
save('graph_D',D);save('graph_C',C);save('graph_K',K)
save('graph_unimodular_inverse',Ai);save('graph_j0_delta_coordinates',L*j(0,delta))

omega=S.Matrix([[12,0,0,0,0,-1]])
B2=S.zeros(6,6).row_join(wedge(Ts[0])-S.eye(6)).row_join(wedge(Ts[1])-S.eye(6))
F=S.eye(6)[:,:5];F[5,0]=12
s=-S.eye(6)[:,5]
Q=s.row_join(F)
assert abs(Q.det())==1 and omega*Q==S.Matrix([[1,0,0,0,0,0]])
assert omega*B2==S.zeros(1,18)
W=(Q.inv()*B2)[1:,:]
Dw,Uw,Vw=snf(W)
assert [abs(Dw[i,i]) for i in range(5)]==[1]*5
P=Vw[:,:5]*S.diag(*[1/Dw[i,i] for i in range(5)])*Uw
assert B2*P==F
save('wedge_B2',B2);save('wedge_kernel_basis',F);save('wedge_preimages',P)
save('wedge_full_basis_inverse',Q.inv())

# The entire conductor is built from the literal triangular quotient.
rays=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
positive=rays[:3]
def rho(v):return (v[0]-v[1])%3
def add(u,v):return (u[0]+v[0],u[1]+v[1])
def sub(u,v):return (u[0]-v[0],u[1]-v[1])
curves=[S.Matrix(x) for x in [(0,1,0,0),(1,-1,-1,0),(0,0,1,0),(1,0,-1,-1),(0,0,0,1),(1,-1,0,-1)]]
metric=S.diag(1,-1,-1,-1)
inter=S.Matrix([[(a.T*metric*b)[0] for b in curves] for a in curves])
assert all(inter[i,i]==-1 and inter[i,(i+1)%6]==1 for i in range(6))
edges=[(i,d) for i in range(3) for d in positive]
d1=S.zeros(3,9);d2norm=S.zeros(12,9)
for k,(i,d) in enumerate(edges):
    q=rho(add((i,0),d));r=rays.index(d)
    d1[i,k]-=1;d1[q,k]+=1
    d2norm[4*i:4*i+4,k]=-curves[r]
    d2norm[4*q:4*q+4,k]=curves[(r+3)%6]
triangles=[]
for i in range(3):
    v=(i,0)
    triangles.append([v,add(v,(1,0)),add(v,(0,1))])
    triangles.append([add(v,(1,1)),add(v,(0,1)),add(v,(1,0))])
d2=S.zeros(9,6)
for k,tri in enumerate(triangles):
    assert len({rho(v) for v in tri})==3
    for p,q in zip(tri,tri[1:]+tri[:1]):
        direction=sub(q,p)
        if direction in positive:
            edge=(rho(p),direction);sign=1
        else:
            edge=(rho(q),(-direction[0],-direction[1]));sign=-1
        d2[edges.index(edge),k]+=sign
assert d1*d2==S.zeros(3,6)
for name,M,rank in [('dual_d1',d1,2),('dual_d2',d2,5),('normalization_H2_incidence',d2norm,7)]:
    DD,UU,VV=save_smith(name,M)
    assert M.rank()==rank and all(abs(DD[i,i])==1 for i in range(rank))
    save(name,M)

# Local divisor restrictions and the full cubic.
d=S.symbols('d0:3')
polynomial=0
pairings=[]
for i in range(3):
    coeff=S.Matrix([d[rho(add((i,0),r))]-d[i] for r in rays])
    polynomial+=d[i]*(coeff.T*inter*coeff)[0]
    # e2 edge, one fixed curve in this component representative.
    col=[]
    for k in range(3):
        c=S.Matrix([(1 if rho(add((i,0),r))==k else 0)-(1 if i==k else 0) for r in rays])
        col.append((c.T*inter[:,1])[0])
    pairings.append(col)
polynomial=S.factor(polynomial)
assert S.expand(polynomial-3*(2*d[0]-d[1]-d[2])*(2*d[1]-d[0]-d[2])*(2*d[2]-d[0]-d[1]))==0
save('boundary_intersection',inter)
FP=S.Matrix.hstack(*[S.Matrix(x) for x in pairings]);save('fixed_curve_divisor_pairing',FP)
assert FP[:,:2]==S.Matrix([[-1,-1],[2,-1],[-1,2]])
print('component_cubic',polynomial)
maps['component_cubic']=str(polynomial)

# The normal-lattice map and its inverse on its kernel.
V=FP[:,:2]
Linverse=S.Matrix([[-S.Rational(1,3),S.Rational(1,3),0],[-S.Rational(1,3),0,S.Rational(1,3)]])
assert Linverse*V==S.eye(2)
assert S.Matrix([[1,1,1]])*V==S.zeros(1,2)
assert all(x%3==0 for x in S.Matrix([[0,1,2]])*V)
save('cusp_relative_kernel_basis',V);save('cusp_relative_kernel_inverse',Linverse)

# Solve the cubic on the primitive dual basis of the fixed spheres.
a,b=S.symbols('a b');c30,c21,c12,c03=S.symbols('c30 c21 c12 c03')
Pab=c30*a**3+3*c21*a*a*b+3*c12*a*b*b+c03*b**3
sub_a=-d[0]+2*d[1]-d[2];sub_b=-d[0]-d[1]+2*d[2]
eq=S.Poly(S.expand(Pab.subs({a:sub_a,b:sub_b})-polynomial),d).coeffs()
solution=S.solve(eq,[c30,c21,c12,c03])
assert solution=={c30:0,c21:-1,c12:-1,c03:0}
print('primitive_cubic',S.factor(Pab.subs(solution)))
maps['primitive_cubic']=str(S.factor(Pab.subs(solution)))

# The log relations are derived from the collar wedge and graph maps.
m,n,aa,bb,cc=S.symbols('m n a_log b_log c_log',integer=True)
R=S.Matrix([[-12*bb,12*aa,n,-cc,0],[m,0,0,0,aa],[0,m,0,0,bb],[0,0,0,m,n]])
q=S.Matrix([-aa,-bb,-cc,-n,m])
assert R*q==S.zeros(4,1)
minors=S.Matrix([(-1)**j*R[:,[k for k in range(5) if k!=j]].det() for j in range(5)])
assert minors==m*m*n*q
G4=S.Matrix([[-n,0,0,0],[m,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
assert G4.det()==n
G4zero=G4.subs(n,0)
normal_kernel=S.Matrix([1,m,m,m])
assert G4zero*normal_kernel==S.zeros(4,1)
assert G4zero.rank()==3 and G4zero.nullspace()[0]*m==normal_kernel
save('normal_G4',G4);save('normal_G4_n0_primitive_kernel',normal_kernel)
save('log_R',R);save('log_maximal_minors',minors)

checks=0
for M in range(1,9):
    for N in range(-4,5):
        for AA,BB,CC in [(0,0,0),(1,0,0),(0,1,0),(0,0,1),(2,3,5),(3,-1,4)]:
            if S.gcd_list([M,N,AA,BB,CC])!=1:continue
            RR=R.subs({m:M,n:N,aa:AA,bb:BB,cc:CC})
            DD,UU,VV=snf(RR)
            t=S.gcd_list([M,N,AA,BB])*S.gcd_list([M,N,12,CC])
            expect=[1,t,M,M*abs(N)//t if N else 0]
            got=[abs(DD[i,i]) for i in range(4)]
            assert got==expect,(M,N,AA,BB,CC,got,expect)
            checks+=1
print('independent_small_log_smith_checks',checks)
print('SUCCESS: exact period, integral graph, wedge, conductor, cubic and log identities verified.')
(OUT/'S6_SERIES_PUBLISH_III_02KS_c7_maps.json').write_text(json.dumps(maps,indent=2)+'\n')
