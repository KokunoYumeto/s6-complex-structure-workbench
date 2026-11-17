#!/usr/bin/env python3
"""Actual E6+A1 source lattice and the complement of the IV* fibre."""
from pathlib import Path
import json
import sympy as S
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.polys.domains import ZZ

root=Path(__file__).resolve().parent
def dec(M):
    D,U,V=smith_normal_decomp(DomainMatrix.from_Matrix(M).convert_to(ZZ))
    D,U,V=[x.to_Matrix() for x in (D,U,V)]
    assert D==U*M*V
    return D,U,V
def ints(M):
    assert all(x.q==1 for x in M)
    return [[int(x) for x in row] for row in M.tolist()]

def hom(d, up):
    assert d*up==S.zeros(d.rows,up.cols)
    D,U,V=dec(d); r=d.rank(); K=V[:,r:]
    relation=(V.inv()*up)[r:,:]
    assert K*relation==up
    E,L,R=dec(relation); rr=relation.rank()
    indices=[i for i in range(K.cols) if i>=rr or abs(E[i,i])!=1]
    orders=[0 if i>=rr else abs(int(E[i,i])) for i in indices]
    reps=K*L.inv()[:,indices]
    project=(L*V.inv()[r:,:])[indices,:]
    assert project*reps==S.eye(len(indices))
    return orders,reps,project

def cone(ds,fs,dimensions):
    dims={j:dimensions.get(j,0)+dimensions.get(j-1,0) for j in range(7)}
    out={}
    for j in range(1,7):
        top=ds.get(j,S.zeros(dimensions.get(j-1,0),dimensions.get(j,0))).row_join(
            fs.get(j-1,S.zeros(0))-S.eye(dimensions.get(j-1,0)))
        bottom=S.zeros(dimensions.get(j-2,0),dimensions.get(j,0)).row_join(
            -ds.get(j-1,S.zeros(dimensions.get(j-2,0),dimensions.get(j-1,0))))
        out[j]=top.col_join(bottom)
        assert out[j].shape==(dims[j-1],dims[j])
    for j in range(2,7): assert out[j-1]*out[j]==S.zeros(dims[j-2],dims[j])
    return out,dims

A=2*S.eye(6)
for i,j in [(0,1),(1,2),(2,3),(3,4),(2,5)]:
    A[i,j]=A[j,i]=-1
marks=S.Matrix([1,2,3,2,1,2])
assert A.det()==3 and A*marks==S.Matrix([0,0,0,0,0,1])
B=S.zeros(10)
B[0,0]=B[9,9]=-1
B[0,1]=B[1,0]=B[9,1]=B[1,9]=1
B[2:8,2:8]=-A
B[8,8]=-2
B[9,2]=B[2,9]=B[9,8]=B[8,9]=1
assert B.det()==-1
eye=S.eye(10)
O,F,G=eye[:,0],eye[:,1],eye[:,9]
roots=eye[:,2:8]
aff=F-roots*marks
def correction(n):
    ans=S.zeros(10,1)
    c=S.Rational(0)
    r=n%3
    if r:
        col=0 if r==1 else 4
        ans[2:8,0]=A.inv()[:,col]
        c+=S.Rational(4,3)
    if n%2:
        ans[8]=S.Rational(1,2)
        c+=S.Rational(1,2)
    return ans,c
r1,_=correction(1)
phi=G-O-F+r1
assert (phi.T*B*phi)[0]==-S.Rational(1,6)
def section(n):
    rn,cn=correction(n)
    po=(S.Rational(n*n,6)-2+cn)/2
    P=O+(po+1)*F+n*phi-rn
    ints(P)
    assert (P.T*B*P)[0]==-1
    assert (P.T*B*O)[0]==po
    return P
Tp=S.eye(10)
Tp[:,0]=G
Tp[:,9]=section(2)
# The actual order-three translation permutation of the affine E6 arms.
for i,j in [(0,4),(1,3),(2,2),(3,5),(5,1)]:
    Tp[:,2+i]=eye[:,2+j]
Tp[:,6]=aff  # outer C4 -> identity component
Tp[:,8]=F-eye[:,8]
assert Tp.T*B*Tp==B and Tp.det() in (1,-1)

constraints=B[[1,2,3,4,5,6,7],:]
free=[0,8,9]
K=B.inv()[:,free]
left=B[free,:]
assert constraints*K==S.zeros(7,3) and left*K==S.eye(3)
assert all(x.q==1 for x in K)
results=[]
Lcomp=S.Matrix.hstack(aff,roots)
Pcomp=S.zeros(7)
# Labels are identity,C0,C1,C2,C3,C4,C5.
for i,j in enumerate([1,5,4,3,6,0,2]):
    Pcomp[j,i]=1
assert Tp*Lcomp==Lcomp*Pcomp
for b,a in [(1,6),(3,2)]:
    T=Tp**(-b)
    R=left*T*K
    assert T*K==K*R
    D,U,V=dec(R-S.eye(3))
    M=section(a)-O
    assert T*M-M==-F
    compact_line_cycle=constraints*M==S.zeros(7,1)
    rminus,_=correction(-b)
    e6corr=S.zeros(10,1);e6corr[2:8,0]=rminus[2:8,0]
    cycle=3*(section(-b)-O)+3*e6corr
    assert constraints*cycle==S.zeros(7,1)
    vals=U*left*cycle
    Pc=Pcomp**(-b)
    assert T*Lcomp==Lcomp*Pc
    pdims={0:1,1:7,2:10,3:1,4:1}
    pd={1:S.zeros(1,7),2:Lcomp.T*B,3:S.zeros(10,1),4:S.ones(1,1),5:S.zeros(1,0)}
    pf={0:S.eye(1),1:Pc.inv().T,2:T,3:S.eye(1),4:S.eye(1)}
    wd,wdims=cone(pd,pf,pdims)
    WH={j:hom(wd[j],wd[j+1]) for j in range(1,5)}
    ndims={0:1,1:7,2:7,3:1}
    nd={1:S.zeros(1,7),2:Lcomp.T*B*Lcomp,3:S.zeros(7,1),4:S.zeros(1,0)}
    nf={0:S.eye(1),1:Pc.inv().T,2:Pc,3:S.eye(1)}
    ed,edims=cone(nd,nf,ndims)
    EH={j:hom(ed[j],ed[j+1]) for j in range(1,5)}
    inc={0:S.eye(1),1:S.eye(7),2:Lcomp,3:S.eye(1),4:S.zeros(1,0)}
    iw={j:S.diag(inc.get(j,S.zeros(pdims.get(j,0),ndims.get(j,0))),
                     inc.get(j-1,S.zeros(pdims.get(j-1,0),ndims.get(j-1,0))))
        for j in range(1,5)}
    for j in range(2,5):assert wd[j]*iw[j]==iw[j-1]*ed[j]
    maps={j:WH[j][2]*iw[j]*EH[j][1] for j in range(1,5)}
    multiplicity=S.Matrix([1,*list(marks)])
    fibre_boundary=EH[2][2]*multiplicity.col_join(S.zeros(7,1))
    results.append(dict(a=a,b=b,translation=ints(T),restriction=ints(R),
                        smith=ints(D),smith_left=ints(U),smith_right=ints(V),
                        fibre=ints(left*F),line_is_compact_cycle=compact_line_cycle,
                        line_cycle=ints(left*M) if compact_line_cycle else None,
                        line_cohomology_restriction=ints(K.T*B*M),
                        line_in_cokernel=ints(U*left*M) if compact_line_cycle else None,
                        corrected_relative_wang_cycle=ints(cycle),
                        relative_wang_in_cokernel=ints(vals),
                        exterior_homology={str(j):WH[j][0] for j in WH},
                        boundary_homology={str(j):EH[j][0] for j in EH},
                        boundary_maps={str(j):ints(maps[j]) for j in maps},
                        boundary_fibre_H2=ints(fibre_boundary),
                        exterior_fibre_H2=ints(maps[2]*fibre_boundary)))
record=dict(status='PASS: exact source and complement matrices',
            scope='Source lattice certificate; cap boundary maps and topology proved separately.',
            E6_cartan=ints(A),E6_marks=ints(marks),source_gram=ints(B),
            translation_plus_G=ints(Tp),constraints=ints(constraints),
            integral_kernel_basis=ints(K),kernel_left_inverse=ints(left),cases=results)
(root/'iv_star_complement.json').write_text(json.dumps(record,indent=2)+'\n')
for case in results:
    print('a,b=',case['a'],case['b'],'Smith=',[case['smith'][i][i] for i in range(3)],
          'M coker=',case['line_in_cokernel'],'relative Wang=',case['relative_wang_in_cokernel'])
    print('Exterior',case['exterior_homology'],'boundary',case['boundary_homology'])
    print('H2 inclusion',case['boundary_maps']['2'],'boundary F',case['boundary_fibre_H2'],
          'exterior F',case['exterior_fibre_H2'])
print('PASS: unimodular E6+A1 source, actual translation, integral complement and relative-Wang cycles.')
