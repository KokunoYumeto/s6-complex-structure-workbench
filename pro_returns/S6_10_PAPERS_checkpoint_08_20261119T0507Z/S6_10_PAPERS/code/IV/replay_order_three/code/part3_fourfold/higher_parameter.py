#!/usr/bin/env python3
"""Higher-root orbifold lattice complex and the exact parameter period."""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

K,L=s.symbols('K L',integer=True,positive=True)
T1=s.Matrix([[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]])
T2=s.Matrix([[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]])
A1=T1.inv().T;A2=T2.inv().T;A0=(A1*A2).inv();I=s.eye(4)
N1=I+A1+A1**2;N2=I+A2+A2**2+A2**3
delta=s.Matrix([0,0,0,1])
eps1=s.Matrix([1,2,-4,0]);eps2=s.Matrix([1,3,-3,0])
B1=s.Matrix.hstack(delta,eps1);B2=s.Matrix.hstack(delta,eps2)
assert (A1-I)*B1==s.zeros(4,2) and (A2-I)*B2==s.zeros(4,2)
norm1=B1.gauss_jordan_solve(N1)[0]
norm2=B2.gauss_jordan_solve(N2)[0]
assert all(z.is_integer for z in norm1) and all(z.is_integer for z in norm2)
K0=s.Matrix([[0,0],[0,0],[1,0],[0,1]])
d0=s.zeros(28,14)
d0[0:4,0:4]=A1-I;d0[4:8,0:4]=A2-I
d0[8:12,4:8]=A1-I;d0[12:16,8:12]=A2-I
for i in range(3):d0[16+4*i:20+4*i,0:4]=I
d0[16:20,4:8]=-I;d0[20:24,8:12]=-I;d0[24:28,12:14]=-K0
d1=s.zeros(20,28)
d1[0:4,8:12]=K*N1;d1[4:8,12:16]=L*N2
d1[8:12,0:4]=I;d1[8:12,8:12]=-I
d1[12:16,4:8]=I;d1[12:16,12:16]=-I
d1[16:20,0:4]=-A0;d1[16:20,4:8]=-A0*A1
for i,A in enumerate([A1,A2,A0]):d1[8+4*i:12+4*i,16+4*i:20+4*i]=-(A-I)
d2=s.zeros(8,20);d2[0:4,0:4]=A1-I;d2[4:8,4:8]=A2-I
assert d1*d0==s.zeros(20,14) and d2*d1==s.zeros(8,28)
kernel=s.diag(B1,B2,s.eye(12))
assert d2*kernel==s.zeros(8,16)
R=kernel.gauss_jordan_solve(d1)[0]
assert all(s.Poly(z,K,L).domain==s.ZZ for z in R)

# All elimination operations are elementary and polynomial in K,L.
# The certificate retains every transformation, not only specialized Smith forms.
D=R.copy();U=s.eye(D.rows);V=s.eye(D.cols);rank=0
while True:
    pivot=next(((i,j) for i in range(rank,D.rows) for j in range(rank,D.cols)
                if D[i,j] in (s.Integer(1),s.Integer(-1))),None)
    if pivot is None:break
    i,j=pivot
    D.row_swap(rank,i);U.row_swap(rank,i)
    D.col_swap(rank,j);V.col_swap(rank,j)
    if D[rank,rank]==-1:
        D.row_op(rank,lambda val,col:-val);U.row_op(rank,lambda val,col:-val)
    for i in range(D.rows):
        if i==rank:continue
        coeff=D[i,rank]
        if coeff:
            D.row_op(i,lambda val,col,coeff=coeff: s.expand(val-coeff*D[rank,col]))
            U.row_op(i,lambda val,col,coeff=coeff: s.expand(val-coeff*U[rank,col]))
    for j in range(D.cols):
        if j==rank:continue
        coeff=D[rank,j]
        if coeff:
            D.col_op(j,lambda val,row,coeff=coeff:s.expand(val-coeff*D[row,rank]))
            V.col_op(j,lambda val,row,coeff=coeff:s.expand(val-coeff*V[row,rank]))
    rank+=1
assert U*R*V==D
assert s.expand(U.det()) in (-1,1) and s.expand(V.det()) in (-1,1)
tail=D[rank:,rank:]
reduced=s.Matrix([[K,0,0],[0,0,-3*K],[0,2*L,0],[0,0,4*L]])
coeff=s.Matrix.vstack(tail[0,:]/K,tail[2,:]/(2*L),tail[3,:]/(4*L))
assert all(z.is_integer for z in coeff)
right_inverse=s.zeros(tail.cols,3)
right_inverse[9,0]=1
right_inverse[2,1]=1;right_inverse[9,1]=1
right_inverse[0,2]=1
assert tail==reduced*coeff
assert coeff*right_inverse==s.eye(3) and tail*right_inverse==reduced
canonical=s.Matrix([[K,0,0,0,0],[0,0,2*L,0,0],
                    [0,3*K,0,0,-1],[0,0,0,4*L,-1]])

def group(prev,nxt):
    dm,um,vm=smith_normal_decomp(DomainMatrix.from_Matrix(nxt).convert_to(s.ZZ))
    dm,um,vm=[z.to_Matrix() for z in (dm,um,vm)]
    rr=nxt.rank();C=(vm.inv()*prev)[rr:,:]
    assert (vm.inv()*prev)[:rr,:]==s.zeros(rr,prev.cols)
    sm=smith_normal_form(C,domain=s.ZZ)
    tors=[abs(int(sm[i,i])) for i in range(min(sm.shape)) if abs(sm[i,i])>1]
    return {'free':int(nxt.cols-rr-C.rank()),'torsion':tors,
            'relation_smith':[[int(v) for v in sm.row(i)] for i in range(sm.rows)]}
checks=[]
for k,l in [(1,1),(1,2),(1,5),(3,1),(5,1),(5,2),(7,5),(13,7)]:
    if s.gcd(3*k,4*l)!=1:continue
    d1v=d1.subs({K:k,L:l})
    h1=group(d0,d1v);h2=group(d1v,d2)
    assert h1['free']==0 and h1['torsion']==[]
    assert h2['free']==1 and h2['torsion']==[2*k*l]
    sm=smith_normal_form(canonical.subs({K:k,L:l}),domain=s.ZZ)
    tors=[abs(int(sm[i,i])) for i in range(min(sm.shape)) if abs(sm[i,i])>1]
    assert tors==[2*k*l]
    checks.append({'K':k,'L':l,'H1':h1,'H2':h2,
                   'canonical_smith':[[int(v) for v in sm.row(i)] for i in range(sm.rows)]})

def serial(matrix):return [[str(v) for v in matrix.row(i)] for i in range(matrix.rows)]
a,d,ss,vv,theta,Gamma,Cc,Uc=s.symbols('a d s v theta Gamma C U')
g=s.Matrix([Gamma,Cc-ss-d*vv]);del2=s.Matrix([0,1])
ordinary=s.Matrix([-a*Gamma*ss/d,a*ss**2/(2*d)-a*Cc*ss/d+vv*(a*ss+Uc)])
cusp=s.Matrix([a*Gamma*vv,vv*Uc+a*Cc*vv-a*d*vv**2/2+a*d*vv/2])
F=(cusp-ordinary).applyfunc(s.expand)
expectedF=a*s.Matrix([Gamma*(ss+d*vv)/d,Cc*(ss+d*vv)/d-(ss+d*vv)**2/(2*d)+d*vv/2])
assert (F-expectedF).applyfunc(s.simplify)==s.zeros(2,1)
assert (ordinary.subs(vv,vv+1)-ordinary-(a*ss+Uc)*del2).applyfunc(s.simplify)==s.zeros(2,1)
assert (cusp.subs(vv,vv+1)-cusp-(a*ss+Uc)*del2-a*g).applyfunc(s.simplify)==s.zeros(2,1)
angular=(F.subs(vv,vv+theta)-F).applyfunc(s.simplify)
assert (angular-a*theta*g-a*d*theta*(1-theta)*del2/2).applyfunc(s.simplify)==s.zeros(2,1)
assert (F.subs(ss,ss+d)-F-a*g+a*d*del2/2).applyfunc(s.simplify)==s.zeros(2,1)
assert (angular.subs(ss,ss+d)-angular+a*d*theta*del2).applyfunc(s.simplify)==s.zeros(2,1)
data={'proof':'notes/part3_higher_parameter.md P3K.11',
 'cochain_ranks':[14,28,20,8],
 'homology_monodromies':[serial(A) for A in (A1,A2,A0)],
 'finite_invariant_bases':[serial(B1),serial(B2)],
 'ordinary_norm_coordinates':[serial(norm1),serial(norm2)],
 'higher_norms':'K*N1 and L*N2, since the extra root stabilizers act trivially on the lattice',
 'd0':serial(d0),'d1':serial(d1),'d2':serial(d2),
 'kernel_d2_basis':serial(kernel),'relation_matrix':serial(R),
 'polynomial_unit_elimination':{'unit_pivots':rank,'left':serial(U),'right':serial(V),'result':serial(D),'remaining':serial(tail),
  'three_relation_matrix':serial(reduced),'coefficient_matrix':serial(coeff),
  'coefficient_right_inverse':serial(right_inverse)},
 'canonical_H2_generators':['delta1','epsilon1','delta2','epsilon2','hc'],
 'canonical_H2_relations':serial(canonical),
 'full_complex_specializations':checks,
 'H2_for_coprime_3K_4L':'Z plus Z/K plus Z/(2L), hence Z plus Z/(2KL)',
 'shear_change':'b*(n0*delta1+n1*delta2)',
 'period_in_c':'2*K*L*Z',
 'closed_parameter':'w_h=exp(-pi*i*c/(K*L)); u=kappa*w_h^(2*K*L)',
 'one_gamma_cover':'w_h=r^6; u=kappa*r^(12*K*L)',
 'sphere_condition':'a=4*L*n0+3*K*n1 in {+1,-1}, with zero cusp collar',
 'signed_origins':{'ordinary':serial(ordinary),'cusp':serial(cusp),'difference':serial(F),
   'angular_difference':serial(angular),'quotient_loop':'a*gamma',
   'deck_gauge_winding':'-a*d'},
 'rotating_one_gamma_pair':['-6*K*L','-24*K*L'],
 'descended_pair_on_w_h':['-K*L','-4*K*L'],
 'pair_scope':'a=+1 positive-gamma sphere marking; index0 is proved for both a signs'}
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(data,indent=2)+'\n')
print('Norm coordinates:',norm1,norm2)
print('Polynomial unit pivots:',rank,'remaining relation matrix:',tail)
print('Full symbolic d1*d0=d2*d1=0; polynomial unimodular elimination verified.')
for row in checks:print('K,L',row['K'],row['L'],'H1',row['H1']['free'],row['H1']['torsion'],'H2',row['H2']['free'],row['H2']['torsion'])
print('Closed higher parameter and characteristic pair:',data['closed_parameter'],data['descended_pair_on_w_h'])
print('Signed extending origins and angular identity verified symbolically; pair scope:',data['pair_scope'])
