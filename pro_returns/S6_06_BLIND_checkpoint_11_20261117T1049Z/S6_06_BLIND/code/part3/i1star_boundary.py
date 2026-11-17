#!/usr/bin/env python3
"""Exact source-complement and boundary chain algebra for OS50, I1*+I3.
The geometric line/cap identification remains in the accompanying working note.
"""
from pathlib import Path
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.polys.domains import ZZ
ROOT=Path(__file__).resolve().parent

def dec(M):
    D,L,R=smith_normal_decomp(DomainMatrix.from_Matrix(M).convert_to(ZZ))
    D,L,R=[x.to_Matrix() for x in (D,L,R)]
    assert D==L*M*R
    return D,L,R

def imat(M):
    assert all(x.q==1 for x in M)
    return [[int(x) for x in row] for row in M.tolist()]

def homology(d,up):
    assert d*up==s.zeros(d.rows,up.cols)
    D,L,R=dec(d);rank=d.rank();K=R[:,rank:]
    A=(R.inv()*up)[rank:,:]
    assert K*A==up
    E,V,W=dec(A)
    rankup=A.rank()
    inds=[i for i in range(K.cols) if i>=rankup or abs(E[i,i])!=1]
    orders=[0 if i>=rankup else abs(int(E[i,i])) for i in inds]
    reps=K*V.inv()[:,inds]
    projector=(V*R.inv()[rank:,:])[inds,:]
    assert projector*reps==s.eye(len(inds))
    return dict(orders=orders,reps=reps,projector=projector,boundary=up)

# NS basis O,F,C0,C1,L1,R0,R1,A2_1,A2_2,G.
B=s.zeros(10);B[0,0]=B[9,9]=-1
B[0,1]=B[1,0]=B[1,9]=B[9,1]=1
for i in range(2,9):B[i,i]=-2
for i,j in [(2,3),(2,4),(3,5),(3,6),(7,8),(9,5),(9,7)]:B[i,j]=B[j,i]=1
assert B.det()==-1
inds=[0,9,7,8]
J=B.inv().extract(inds,inds)
T=s.Matrix([[-1,-2,0,0],[2,3,0,0],[1,2,-1,1],[0,1,-1,0]])
U=T.inv().T
F=s.Matrix([1,1,0,0])
assert J*U==T*J
assert U*F==F and J*F==s.zeros(4,1)
# Boundary N has C3=Z,C2=Z4,C1=Z4,C0=Z,d2=J.
# The actual boundary of the mapping torus is its chain cone for t-1.
bd2=s.zeros(5,8);bd2[:4,:4]=J;bd2[:4,4:]=T-s.eye(4)
bd3=s.zeros(8,5);bd3[:4,1:]=U-s.eye(4);bd3[4:,1:]=-J
bd4=s.zeros(5,1)
H2B=homology(bd2,bd3)
H2W=homology(s.zeros(1,4),U-s.eye(4))
j2=s.eye(4).row_join(s.zeros(4))
i2=H2W['projector']*j2*H2B['reps']
H1B=homology(s.zeros(1,5),bd2)
H3B=homology(bd3,bd4)
H3W=homology(U-s.eye(4),s.zeros(4,1))
j3=s.zeros(4,1).row_join(s.eye(4))
i3=H3W['projector']*j3*H3B['reps']
F2B=H2B['projector']*F.col_join(s.zeros(4,1))
F2W=H2W['projector']*F
# The actual positive Hom section gives the contracting source map t_{-2G}.
# The computed +2G model is identified by (p,t)->(p,-t). On chain cones this
# is identity on direct chains and -f^{-1} on suspended chains.
Tm=T.inv();Um=U.inv()
bd2m=s.zeros(5,8);bd2m[:4,:4]=J;bd2m[:4,4:]=Tm-s.eye(4)
bd3m=s.zeros(8,5);bd3m[:4,1:]=Um-s.eye(4);bd3m[4:,1:]=-J
Phi1=s.diag(s.eye(4),-s.ones(1))
Phi2=s.diag(s.eye(4),-Tm)
Phi3=s.diag(s.ones(1),-Um)
assert bd2*Phi2==Phi1*bd2m
assert bd3*Phi3==Phi2*bd3m
actual_reps=Phi2.inv()*H2B['reps']
assert bd2m*actual_reps==s.zeros(5,actual_reps.cols)
assert j2*actual_reps==j2*H2B['reps']
assert (U-s.eye(4))*(-Um)==Um-s.eye(4)
# Oriented actual degree-three generators: source boundary N, then F*gamma.
actual_H3_reps=s.zeros(5,2);actual_H3_reps[0,0]=1;actual_H3_reps[1:,1]=F
actual_H3_target=F
assert bd3m*actual_H3_reps==s.zeros(8,2)
assert (Um-s.eye(4))*actual_H3_target==s.zeros(4,1)
assert j3*actual_H3_reps==actual_H3_target*s.Matrix([[0,1]])
PhiW3=-Um
assert (U-s.eye(4))*PhiW3==Um-s.eye(4)
assert PhiW3*j3==j3*Phi3
actual_to_positive_H3=H3B['projector']*Phi3*actual_H3_reps
actual_to_positive_target_H3=H3W['projector']*PhiW3*actual_H3_target
# Inversion sends G to -G=2O-G-A2_1-A2_2 modulo D5+F.
Tminus=s.Matrix([[1,2,0,0],[0,-1,0,0],[0,-1,0,1],[0,-1,1,0]])
Uminus=Tminus.inv().T
assert Tminus*T*Tminus==T.inv()
assert Uminus*U*Uminus==U.inv()
# The map reversing the mapping-torus parameter is (Uminus,-T^-1*Tminus)
# on C2(N) plus suspended C1(N); the latter is the exact chain-cone factor.
Inv2=s.diag(Uminus,-T.inv()*Tminus)
Inv1=s.diag(Tminus,-s.ones(1))
Inv3=s.diag(s.ones(1),-U.inv()*Uminus)
assert bd2*Inv2==Inv1*bd2
assert bd3*Inv3==Inv2*bd3
IB=H2B['projector']*Inv2*H2B['reps']
IW=H2W['projector']*Uminus*H2W['reps']
result={
 'scope':'Exact one-I1star boundary maps; actual cap collar kappa and graph-path c are retained symbolically',
 'NS_gram':imat(B),'complement_intersection':imat(J),'quotient_translation':imat(T),'complement_translation':imat(U),
 'boundary_d2':imat(bd2),'boundary_d3':imat(bd3),
 'H1_boundary':H1B['orders'],'H2_boundary':H2B['orders'],'H3_boundary':H3B['orders'],
 'H2_exterior':H2W['orders'],'H3_exterior':H3W['orders'],
 'H2_boundary_representatives':imat(H2B['reps']),'H2_exterior_representatives':imat(H2W['reps']),
 'H2_boundary_to_exterior':imat(i2),'H3_boundary_to_exterior':imat(i3),
 'source_fibre_in_boundary':imat(F2B),'source_fibre_in_exterior':imat(F2W),
 'actual_H3_boundary_representatives':imat(actual_H3_reps),'actual_H3_exterior_representative':imat(actual_H3_target),'actual_H3_boundary_to_exterior':[[0,1]],'actual_to_positive_boundary_cone_degree3':imat(Phi3),'actual_to_positive_exterior_cone_degree3':imat(PhiW3),'actual_to_positive_H3_coordinates':imat(actual_to_positive_H3),'actual_to_positive_exterior_H3_coordinates':imat(actual_to_positive_target_H3),'actual_negative_translation':imat(Um),'actual_boundary_d2':imat(bd2m),'actual_boundary_d3':imat(bd3m),'actual_to_positive_cone_degree2':imat(Phi2),'actual_H2_boundary_representatives':imat(actual_reps),'H2_inversion_boundary':imat(IB),'H2_inversion_exterior':imat(IW),'all_pass':True}
(ROOT/'i1star_boundary.json').write_text(json.dumps(result,indent=2)+'\n')
for k,v in result.items():print(k,'=',v)
print('PASS: unimodular NS lattice, functorial intersection chain cone, integral boundary maps and inversion.')
# The marked cap need not preserve the exterior-boundary inversion.
# Retain its actual integral collar coefficient kappa; the fibre degree fixes r.
kappa=s.symbols('kappa',integer=True)
cap2=s.Matrix([[0,-1,kappa]])
assert cap2*H2B['projector']*F.col_join(s.zeros(4,1))==s.Matrix([[2]])
D2=i2.col_join(-cap2)
assert D2.det()==-1
# Exact adapted basis: s_new=s+kappa*r, with all source/exterior markings retained.
BC=s.Matrix([[1,0,0],[0,1,kappa],[0,0,1]])
assert BC.det()==1 and cap2*BC==s.Matrix([[0,-1,0]])
assert i2*BC==i2
reps_adapted=H2B['reps']*BC
smat=lambda M:[[str(x) for x in row] for row in M.tolist()]
result['H2_boundary_to_cap_symbolic']=smat(cap2)
result['H2_MV_symbolic']=smat(D2)
result['H2_MV_determinant']=int(D2.det())
result['H2_adapted_basis_change']=smat(BC)
result['H2_adapted_boundary_representatives']=smat(reps_adapted)
result['actual_H2_adapted_boundary_representatives']=smat(actual_reps*BC)
result['H2_adapted_MV']=imat(D2*BC)
result['correction']='The exterior-boundary inversion does not fix the marked cap; its actual coefficient kappa is retained. The prior zero-cap specialization is preserved under attempts/.'
(ROOT/'i1star_boundary.json').write_text(json.dumps(result,indent=2)+'\n')
print('H2 cap map =',cap2.tolist(),'full MV =',D2.tolist(),'det =',D2.det())
print('Exact adapted boundary basis =',BC.tolist(),'adapted MV =',(D2*BC).tolist())
print('PASS: full H2 map is an integral isomorphism for the actual retained collar coefficient.')
# Positive outward gamma and positive base alpha: alpha maps to -n*h;
# the retained gamma graph correction is -b/2=-1.
# Retain the actual unspecified graph-path integer c in degree one.
n,c=s.symbols('n c',integer=True)
D1=s.Matrix([[1,c,-1],[0,-n,2],[0,0,1]])
D3=s.Matrix([[0,1],[n,-2]])
assert D1.det()==-n and D3.det()==-n
result['H1_MV_symbolic']=[[str(x) for x in row] for row in D1.tolist()]
result['H3_MV_symbolic']=[[str(x) for x in row] for row in D3.tolist()]
result['one_cap_group_order']='abs(n), for odd n; retained graph-path integer c arbitrary'
(ROOT/'i1star_boundary.json').write_text(json.dumps(result,indent=2)+'\n')
print('H1 MV =',D1.tolist(),'det =',D1.det())
print('H3 MV =',D3.tolist(),'det =',D3.det())
print('PASS: retained graph-path coefficient, exact one-cap degree-one/three determinants.')
