"""Actual mod8 cusp class and full fundamental-class coordinates for OS45.

The geometric descent comparison is in maps_weighted_os45_mu_proof.tex.
This certificate retains the full Smith/bar row, its affine strip constants,
the exact deck shifts of the D43 annulus map, all16 component restrictions,
and the primitive half-component generator.
"""
from pathlib import Path
from collections import defaultdict
import json
import sympy as s
from manifolds_general_initial import graph_data
from manifolds_rankone_families import decomp
from manifolds_weighted_profiles import integral_left_inverse

root=Path(__file__).resolve().parents[1]
data=json.loads((root/'records/maps_weighted_os45.json').read_text())
M=s.Matrix(data['full']['H2_matrix'])
D,U,V,rank=decomp(M)
j=[i for i in range(rank) if abs(D[i,i])>1][0]
phi=-U[j,:]
assert list(phi[:6])==[1,0,0,0,0,0]
assert all(int(x)%8==0 for x in phi*M)
A=[s.Matrix(v) for v in data['full']['fundamental_group']['conjugation_matrices']]
K,Js,Q=graph_data(A)
Ki=integral_left_inverse(K)
core_d2=s.zeros(4,6+4*(len(A)-1))
core_d2[:,6:]=s.Matrix.hstack(*[B-s.eye(4) for B in A[:-1]])
cycle_inclusion=s.diag(s.eye(6),K)
cycle_retraction=s.diag(s.eye(6),Ki)
core_cochain=phi*cycle_retraction
assert core_d2*cycle_inclusion==s.zeros(4,cycle_inclusion.cols)
assert cycle_retraction*cycle_inclusion==s.eye(cycle_inclusion.cols)
assert core_cochain*cycle_inclusion==phi
core_d3=s.zeros(core_d2.cols,6*(len(A)-1))
from manifolds_rankone_families import wedge
core_d3[:6,:]=s.Matrix.hstack(*[wedge(B)-s.eye(6) for B in A[:-1]])
assert core_d2*core_d3==s.zeros(4,core_d3.cols)
assert all(int(x)%8==0 for x in core_cochain*core_d3)
ell=phi[:,6:]*Js[1]
assert list(ell)==[0,52,0,148]
assert [int(ell[i])%8 for i in (1,3)]==[4,4]

rays=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
vertices=[(r,t) for r in range(8) for t in range(2)]
def psi(r,t):
    return 4*(r//8)+3*(r%8)*(t//2)
def degree(v,i):
    r,t=v;a=rays[i];b=rays[(i-1)%6];c=rays[(i+1)%6]
    return psi(r,t)+psi(r+a[0],t+a[1])-psi(r+b[0],t+b[1])-psi(r+c[0],t+c[1])
def vertex(v):
    return (v[0]%8)*2+(v[1]%2)

# The identities are formal in quotient and remainder r=8q+r0,t=2p+t0.
# This finite residue check covers every integer by those exact formulas.
for r in range(-16,24):
    for t in range(-8,10):
        assert (psi(r+8,t-6)-psi(r,t)+r-4)%8==0
        assert (psi(r+24,t-16)-psi(r,t)-4)%8==0

eta=[];degrees=[];fixed=[]
intersection=s.diag(1,-1,-1,-1)
curves=[s.Matrix(v) for v in [(0,1,0,0),(1,-1,-1,0),(0,0,1,0),
                             (1,0,-1,-1),(0,0,0,1),(1,-1,0,-1)]]
for v in vertices:
    deg=[degree(v,i) for i in range(6)]
    h=deg[1]+deg[0]+deg[2]
    e=s.Matrix([h,-deg[0],-deg[2],-deg[4]])
    assert all(int((e.T*intersection*C)[0])==dd for C,dd in zip(curves,deg))
    eta.append(e);degrees.append(deg)
    for i,a in enumerate(rays):
        vv=(v[0]+a[0],v[1]+a[1])
        assert (degree(v,i)-degree(vv,(i+3)%6))%8==0
    fixed.append(dict(vertex=list(v),degree=deg[1]%8,
                      character=(psi(v[0],v[1]+1)-psi(*v))%8,
                      y_character=-v[1]))

# Actual D43 inverse Picard columns, with component labels in the
# positive fan convention. The simultaneous inverse deck convention is
# x:translation(-1,0), y:translation(0,1).
generator_curves=[
    [(1,-2,2,1),(0,-1,4,1)],
    [(1,-1,2,-1)],
    [(1,0,0,1),(2,-1,2,1)]]
def norm(n):
    return {i:1 for i in range(n)} if n>=0 else {i:-1 for i in range(n,0)}
def annulus(p,q,a,b):
    pr,qr=-p,q;ar,br=-a,b
    sx={(i,0):v for i,v in norm(pr).items()}
    sy={(pr,j):v for j,v in norm(qr).items()}
    coefficients=[defaultdict(int) for _ in range(3)]
    for ij,v in sx.items():
        coefficients[0][ij]+=ar*v;coefficients[1][ij]+=br*v
    for ij,v in sy.items():
        coefficients[1][ij]+=ar*v;coefficients[2][ij]+=br*v
    value=0
    for h,pol in enumerate(coefficients):
        for (i,j),v in pol.items():
            for r,t,c,w in generator_curves[h]:
                value+=v*w*degree((r-i,t+j),c)
    return value
annuli=[[annulus(p,q,a,b) for p,q in [(8,-6),(24,-16)]]
        for a,b in [(1,0),(0,1)]]
assert [[v%8 for v in row] for row in annuli]==[[1,0],[0,0]]

# Complete mixed terms on the primitive free basis x0,...,x13,y.
C=s.zeros(16)
for i,v in enumerate(vertices):
    for j in range(16):
        if i==j:
            C[i,j]=-sum(degrees[i])
        else:
            C[i,j]=sum(degrees[i][h] for h,a in enumerate(rays)
                       if vertex((v[0]+a[0],v[1]+a[1]))==j)
assert all(int(x)%8==0 for x in C-C.T)
assert all(int(x)%8==0 for x in C*s.ones(16,1))
mixed=s.zeros(15)
mixed[:14,:14]=C[:14,:14]
for i,v in enumerate(vertices[:14]):
    fdegree=int(eta[i][0]+eta[i][1])
    mixed[i,14]=mixed[14,i]=(-1)**v[1]*fdegree
mixed[14,14]=0
square=[int((e.T*intersection*e)[0])%16 for e in eta[:14]]+[0]
assert all((int(mixed[i,i])-square[i])%2==0 for i in range(15))

pure=-3*sum(z['degree']*z['character']**2 for z in fixed)
square_y=-2*sum(z['degree']*z['character']*z['y_character'] for z in fixed)
uy2=-sum(z['degree']*z['y_character']**2 for z in fixed)
assert pure%8==0 and square_y%16==0 and uy2%8==0

# Two half-divisor relations, before any division of finite coefficients.
odd=[i for i,v in enumerate(vertices) if v[1]==1]
for i in range(14):
    assert (sum(C[i,j] for j in odd)-2*mixed[i,14])%8==0
assert sum(int((eta[j].T*intersection*eta[j])[0]) for j in odd)%16==0

result=dict(scope=__doc__,
  torsion_core_row=list(map(int,phi)),cusp_strip_row=list(map(int,ell)),
  literal_core_cochain=list(map(int,core_cochain)),
  graph_cycle_basis=K.tolist(),graph_cycle_left_inverse=Ki.tolist(),
  core_degree_two_boundary=core_d2.tolist(),
  core_degree_three_boundary=core_d3.tolist(),
  support='4*floor(r/8)+3*(r mod8)*floor(s/2) modulo8',
  periods=[[8,-6],[24,-16]],affine_period_gradients=[[-1,0],[0,0]],
  affine_period_constants=[4,4],annulus_evaluations=annuli,
  vertices=[list(v) for v in vertices],
  component_eta=[list(map(int,e)) for e in eta],
  component_wall_degrees=degrees,
  primitive_free_basis=['x'+str(i) for i in range(14)]+['y'],
  mixed_u_x_x=[[int(v)%8 for v in row] for row in mixed.tolist()],
  mixed_P2_u_x=square,pure_u_cube=0,
  fixed_curve_data=fixed,
  exact_fixed_sums=dict(pure_cube= pure,P2_u_y=square_y,u_y_squared=uy2),
  status='All exact cochain, annulus and full-modulus evaluations passed; geometric descent proof separate.')
(root/'records/maps_weighted_os45_mu.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
print('Primitive global torsion row, actual strip constants(4,4): PASS')
print('Full shifted annulus evaluations:',annuli,'mod8 -> [[1,0],[0,0]]')
print('All16 component wall restrictions and opposite gluing checks: PASS')
print('Primitive-basis mixed P2 values mod16:',square)
print('Fixed sums:',result['exact_fixed_sums'])
print(result['status'])
