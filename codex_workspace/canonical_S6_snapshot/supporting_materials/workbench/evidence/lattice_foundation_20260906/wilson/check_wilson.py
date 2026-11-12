"""Exact Wilson Leech construction in Wilson's fixed octonion basis.
All arithmetic is rational/integer; no lattice-classification oracle is used.
"""
from itertools import product
import json
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form

I=sp.eye(8)
e=[I[:,i] for i in range(8)]
# Indices are infinity,0,1,...,6. Oriented Fano lines (t,t+1,t+3).
table={(0,j):(1,j) for j in range(8)}
table.update({(j,0):(1,j) for j in range(8)})
for j in range(1,8): table[j,j]=(-1,0)
for t in range(7):
    a,b,c=(t+1,(t+1)%7+1,(t+3)%7+1)
    for u,v,w in ((a,b,c),(b,c,a),(c,a,b)):
        assert (u,v) not in table or table[u,v]==(1,w)
        table[u,v]=(1,w);table[v,u]=(-1,w)
assert len(table)==64

def mul(x,y):
    z=sp.zeros(8,1)
    for i in range(8):
        for j in range(8):
            sg,k=table[i,j];z[k]+=sg*x[i]*y[j]
    return z
def conj(x): return sp.diag(1,-1,-1,-1,-1,-1,-1,-1)*x
def right(x):return sp.Matrix.hstack(*(mul(a,x) for a in e))
def norm(x):return (x.T*x)[0]
def tau(x,y,z):return mul(mul(x,y),z)[0]
def qmul(a,b):
    w,x,y,z=a;t,u,v,r=b
    return sp.Matrix([w*t-x*u-y*v-z*r,w*u+x*t+y*r-z*v,
                      w*v-x*r+y*t+z*u,w*r+x*v-y*u+z*t])
def qconj(a):return sp.Matrix([a[0],-a[1],-a[2],-a[3]])
def cdmul(x,y):
    a,b=x[:4,0],x[4:,0];c,d=y[:4,0],y[4:,0]
    return (qmul(a,c)-qmul(qconj(d),b)).col_join(qmul(d,a)+qmul(b,qconj(c)))
J=sp.zeros(8)
for col,row in enumerate([0,1,2,4,3,6,7,5]):J[row,col]=-1 if col==6 else 1
assert J.T*J==I and J.det()==1
for a,b in product(e,e):assert J*mul(a,b)==cdmul(J*a,J*b)
s=sp.Matrix([-1,1,1,1,1,1,1,1])/2
assert J*s==sp.Matrix([-1,1,1,1,1,1,1,-1])/2
for signs in product([-1,1],repeat=8):
    if signs.count(-1)%2:
        image=J*sp.Matrix(signs)
        assert list(image).count(-1)%2==0
B=sp.Matrix.hstack(s,*(e[i]-e[i+1] for i in range(1,7)),e[6]+e[7])
assert abs(B.det())==1
G=B.T*B
S=B.inv()*right(s)*B
T=B.inv()*right(conj(s))*B
assert all(x.q==1 for x in S) and all(x.q==1 for x in T)
assert S+T==-I and S*T==2*I
assert S.T*G*S==2*G and T.T*G*T==2*G
assert abs(S.det())==abs(T.det())==16

def f2_basis_columns(A):
    piv={};inds=[]
    for j in range(A.cols):
        v=sum((int(A[i,j])%2)<<i for i in range(A.rows))
        w=v
        for k in sorted(piv,reverse=True):
            if (w>>k)&1:w^=piv[k]
        if w:
            p=w.bit_length()-1;piv[p]=w;inds.append(j)
    return inds
si=f2_basis_columns(S);ti=f2_basis_columns(T)
assert len(si)==len(ti)==4
assert len(f2_basis_columns(T.row_join(S)))==8
assert sp.Matrix.hstack(T[:,:4],S[:,:4]).det()==-7
gens=[2*sp.eye(24)[:,i] for i in range(24)]
for j in ti:
    m=T[:,j];z=sp.zeros(8,1)
    gens.extend([m.col_join(m).col_join(z),m.col_join(z).col_join(m)])
for j in si:
    n=S[:,j];gens.append(n.col_join(n).col_join(n))
generator_matrix=sp.Matrix([[int(x) for x in row] for row in sp.Matrix.hstack(*gens).tolist()])
H=hermite_normal_form(generator_matrix)
G24=sp.diag(G,G,G)
Gram=(H.T*G24*H)/2
assert abs(H.det())==4096 and Gram.det()==1
assert all(x.q==1 for x in Gram)
assert all(Gram[i,i]%2==0 for i in range(24))
P=sp.zeros(24)
# P implements Wilson's c_W=(y,z,x), inverse to canonical c=(z,x,y).
for i in range(3):
    for j in range(8): P[i*8+j,((i+1)%3)*8+j]=1
C=H.inv()*P*H
Pcanonical=P.T
Ccanonical=H.inv()*Pcanonical*H
assert Pcanonical==P**2 and Pcanonical*P==sp.eye(24)
assert Ccanonical==C**2 and Ccanonical*C==sp.eye(24)
assert all(x.q==1 for x in C) and C**3==sp.eye(24)
assert C.T*Gram*C==Gram
assert (C-sp.eye(24)).rank()==16
assert (Ccanonical-sp.eye(24)).rank()==16
Fix=S.col_join(S).col_join(S)
assert all(x.q==1 for x in H.inv()*Fix)
assert (Fix.T*G24*Fix)/2==3*G
Coin=sp.Matrix.vstack(sp.Matrix.hstack(T,sp.zeros(8)),
                     sp.Matrix.hstack(sp.zeros(8),T),
                     sp.Matrix.hstack(-T,-T))
CoinGram=sp.Matrix.vstack(sp.Matrix.hstack(2*G,G),sp.Matrix.hstack(G,2*G))
assert (Coin.T*G24*Coin)/2==CoinGram
assert CoinGram.det()==3**8
assert all(x.q==1 for x in H.inv()*Coin)
assert abs((H.inv()*Fix.row_join(Coin)).det())==3**8
Lift=S.col_join(I).col_join(-I)
Fp=Fix/3
Cp=Lift-Fp
assert all(x.q==1 for x in H.inv()*Lift)
assert Fp.T*G24*Cp==sp.zeros(8)
assert Fp.T*G24*Fp/2==G/3
assert Cp.T*G24*Cp/2==5*G/3
assert all(x.q==1 for x in Cp.T*G24*Coin/2)

# Right-unit maps preserve L and satisfy the two congruences sufficient
# for (x,y,z)->(x,y i_t,z i_t) to preserve Wilson's defining conditions.
right_unit_checks=[]
for j in range(1,8):
    U=B.inv()*right(e[j])*B
    assert all(x.q==1 for x in U) and U.det()==1
    assert all(x.q==1 for x in T.inv()*(U-I))
    assert all(x.q==1 for x in ((U-I)*T)/2)
    R=sp.diag(I,U,U)
    RH=H.inv()*R*H
    assert all(x.q==1 for x in RH) and abs(RH.det())==1
    a=2*(e[0]+e[j])
    before=tau(a,a,a);after=tau(a,mul(a,e[j]),mul(a,e[j]))
    assert (before,after)==(-16,16)
    right_unit_checks.append([j-1,int(before),int(after)])

# Sector transposition counterexample uses a vector in (2L)^3.
a=2*(e[0]+e[1]);b=2*(e[0]+e[2]);c=2*(e[3]+e[4])
# e[3]=i_2 and e[4]=i_3, so the k component controls the scalar.
assert (tau(a,b,c),tau(b,a,c))==(-8,8)
# Translation and doubling simultaneously applied to all sectors.
fano_checks=[]
for name,f in [('shift',lambda t:(t+1)%7),('double',lambda t:2*t%7)]:
    A=sp.zeros(8);A[0,0]=1
    for t in range(7):A[f(t)+1,t+1]=1
    assert A*s==s
    for x,y in product(e,e):assert A*mul(x,y)==mul(A*x,A*y)
    AL=B.inv()*A*B
    AH=H.inv()*sp.diag(AL,AL,AL)*H
    assert all(x.q==1 for x in AH) and abs(AH.det())==1
    fano_checks.append(name)

# Literal rank-four intersection with the two retained Niemeier embeddings.
U0=sp.eye(8)[:,:4]
NinvU=S.inv()*B.inv()*J.T*U0
expected_NinvU=sp.Matrix([
 [2,-2,-2,-2],[-2,0,0,2],[-4,2,0,2],[-6,4,2,2],
 [-8,4,4,2],[-10,6,4,4],[-5,3,3,3],[-7,3,3,3]])/4
assert NinvU==expected_NinvU
# All congruence classes suffice: the matrix has denominator four.
for k in product(range(4),repeat=4):
    actual=all(v.q==1 for v in NinvU*sp.Matrix(k))
    predicted=all(v%2==0 for v in k) and sum(k)%4==0
    assert actual==predicted
D4=sp.Matrix([[1,0,0,0],[-1,1,0,0],[0,-1,1,1],[0,0,-1,1]])
G4=D4.T*D4
assert abs(D4.det())==2 and (6*G4).det()==5184
common_Wilson=2*B.inv()*J.T*U0*D4
common_L3=common_Wilson.col_join(common_Wilson).col_join(common_Wilson)
assert all(v.q==1 for v in H.inv()*common_L3)
assert common_L3.T*G24*common_L3/2==6*G4
ones=sp.ones(4,1)
P4=sp.Matrix.hstack(2*sp.eye(4)[:,0],2*sp.eye(4)[:,1],2*sp.eye(4)[:,2],ones)
P04=hermite_normal_form((2*D4).row_join(ones))
assert abs(P4.det())==8 and abs(P04.det())==16
assert abs((P4.inv()*2*D4).det())==4
assert abs((P04.inv()*2*D4).det())==2
glue=set()
for u in product(range(2),repeat=4):
    if sum(u)%2:continue
    for a,b in product(range(3),repeat=2):
        ternary=(a+b,a+2*b,a,b)
        glue.add(tuple((3*u[i]+2*ternary[i])%6 for i in range(4))+
                 ((u[1]+u[3])%2,(u[2]+u[3])%2))
assert len(glue)==72
for k in product(range(4),repeat=4):
    label=tuple(3*v%6 for v in k)+(0,0)
    assert (label in glue)==(len({v%2 for v in k})==1)
    if label in glue:
        rho_pair=sp.Rational(3,2)*sum(k)
        assert (rho_pair%6==0)==(sum(k)%4==0)
# d_n=-m rho_D/6, fourth coordinate zero, is in D* iff 6 divides m.
for m in range(6):
    dn=-sp.Rational(m,6)*sp.Matrix([3,2,1,0])
    ddual=all(v.q==1 for v in dn) or all((v-sp.Rational(1,2)).q==1 for v in dn)
    assert ddual==(m==0)
# Apply the original map, including its nontrivial means placement.
def original_L(x,d):
    sig=[sum((-1)**j*x[i][j] for j in range(6)) for i in range(4)]
    means=[sp.sqrt(2)*v/6 for v in sig]+[sp.sqrt(3)*v/3 for v in d]
    out=sp.zeros(24,1)
    for i,p,j in product(range(4),range(2),range(3)):
        a=2*i+p
        t=x[i][p+2*j]-sum(x[i][p+2*h] for h in range(3))/3
        out[8*j+a]=sp.simplify(t+means[a])
    return out
rhoA=sp.Matrix([5,3,1,-1,-3,-5])/2
for col in range(4):
    a=D4[:,col]
    x=[[(-1)**j*a[i] for j in range(6)] for i in range(4)]
    image=original_L(x,[0]*4)
    target=sp.sqrt(2)*(U0*a).col_join(U0*a).col_join(U0*a)
    assert image==target
    assert sum((rhoA.T*sp.Matrix(block))[0] for block in x)%6==0
a0,a1,a2,a3=sp.symbols('a0 a1 a2 a3')
av=sp.Matrix([a0,a1,a2,a3,0,0,0,0])
Ppoly=4*a0**3-3*a0*(a0*a0+a1*a1+a2*a2+a3*a3)
assert sp.expand(cdmul(cdmul(av,av),av)[0]-Ppoly)==0
assert Ppoly.subs({a0:1,a1:1,a2:0,a3:0})==-2
for aa in product(range(3),repeat=4):
    pp=int(Ppoly.subs(dict(zip((a0,a1,a2,a3),aa))))
    if pp%3==0:assert pp%9==0

def rows(M):return [[str(x) for x in row] for row in M.tolist()]
report={'status':'PASS','Wilson_to_current_CD_basis_map':rows(J),
 'Wilson_to_current_basis_products_checked':64,'s_in_current_CD_basis':rows(J*s),
 'Wilson_odd_half_roots_map_to_current_even_half_roots':True,
 'cyclic_operator_conventions':{'Wilson':'(y,z,x)','canonical':'(z,x,y)',
                              'Wilson_is_canonical_inverse':True},
 'basis_B':rows(B),'gram_E8':rows(G),
 'right_s_matrix_S':rows(S),'right_sbar_matrix_T':rows(T),
 'S_mod2_basis_columns_1based':[i+1 for i in si],
 'T_mod2_basis_columns_1based':[i+1 for i in ti],
 'lambda_hnf_in_L3':rows(H),'lambda_gram_original_metric':rows(Gram),
 'lambda_index_in_L3':int(abs(H.det())),'unimodular_gram_det':int(Gram.det()),
 'cyclic_fixed_rank':8,'fixed_gram':rows(3*G),
 'coinvariant_gram':rows(CoinGram),'fixed_plus_coinvariant_index':3**8,
 'glue_projection_gram_fixed':rows(G/3),
 'glue_projection_gram_coinvariant':rows(5*G/3),
 'right_unit_cubic_tests_tau':right_unit_checks,
 'transposition_tau_values':[-8,8],
 'fano_cubic_preserving_generators':fano_checks,
 'N_W_intersection_U_membership_matrix':rows(NinvU),
 'literal_common_D4_basis':rows(D4),'literal_common_Gram':rows(6*G4),
 'literal_common_rank':4,'literal_common_determinant':5184,
 'literal_common_minimum_proved':12,'literal_slice_indices':[4,2],
 'literal_common_cubic_generated_group':'4 sqrt(2) Z',
 'literal_common_Albert_cubic_generated_group':'8 sqrt(2) Z',
 'cubic_generator_witness_a':[1,1,0,0],
 'cubic_generator_witness_F':'-4 sqrt(2)',
 'unattained_cubic_group_element':'12 sqrt(2)'}
print(json.dumps(report,indent=2))
