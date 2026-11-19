#!/usr/bin/env python3
"""Exact E7 complement and boundary maps for primitive and twice-primitive Q."""
from pathlib import Path
import json
import sympy as S
from integer_chain import dec, ints, hom, cone

root=Path(__file__).resolve().parent
A=2*S.eye(7)
for i,j in [(0,1),(1,2),(2,3),(3,4),(4,5),(2,6)]:
    A[i,j]=A[j,i]=-1
marks=S.Matrix([2,3,4,3,2,1,2])
assert A.det()==2 and A*marks==S.Matrix([1,0,0,0,0,0,0])
B=S.zeros(10)
B[0,0]=B[9,9]=-1
B[0,1]=B[1,0]=B[9,1]=B[1,9]=1
B[2:9,2:9]=-A
B[9,7]=B[7,9]=1
assert B.det()==-1
eye=S.eye(10);O,F,G=eye[:,0],eye[:,1],eye[:,9]
rr=S.zeros(10,1);rr[2:9,0]=A.inv()[:,5]
phi=G-O-F+rr
assert (phi.T*B*phi)[0]==-S.Rational(1,2)
def section(n):
    corr=rr if n%2 else S.zeros(10,1)
    local=S.Rational(3,2) if n%2 else 0
    po=(S.Rational(n*n,2)-2+local)/2
    P=O+(po+1)*F+n*phi-corr
    ints(P); assert (P.T*B*P)[0]==-1
    return P
aff=F-eye[:,2:9]*marks
Tp=S.eye(10);Tp[:,0]=G;Tp[:,9]=section(2)
for i,j in [(0,4),(1,3),(2,2),(3,1),(4,0),(6,6)]:
    Tp[:,2+i]=eye[:,2+j]
Tp[:,7]=aff
assert Tp.T*B*Tp==B
L=S.Matrix.hstack(aff,eye[:,2:9])
P=S.zeros(8)
for i,j in enumerate([6,5,4,3,2,1,0,7]):P[j,i]=1
assert Tp*L==L*P
cases=[]
for a,b in [(2,1),(1,2)]:
    T=Tp**(-b);Pc=P**(-b)
    pdims={0:1,1:8,2:10,3:1,4:1}
    pd={1:S.zeros(1,8),2:L.T*B,3:S.zeros(10,1),4:S.ones(1,1),5:S.zeros(1,0)}
    pf={0:S.eye(1),1:Pc.inv().T,2:T,3:S.eye(1),4:S.eye(1)}
    wd,wdims=cone(pd,pf,pdims)
    WH={j:hom(wd[j],wd[j+1]) for j in range(1,5)}
    ndims={0:1,1:8,2:8,3:1}
    nd={1:S.zeros(1,8),2:L.T*B*L,3:S.zeros(8,1),4:S.zeros(1,0)}
    nf={0:S.eye(1),1:Pc.inv().T,2:Pc,3:S.eye(1)}
    ed,edims=cone(nd,nf,ndims)
    EH={j:hom(ed[j],ed[j+1]) for j in range(1,5)}
    inc={0:S.eye(1),1:S.eye(8),2:L,3:S.eye(1),4:S.zeros(1,0)}
    iw={j:S.diag(inc.get(j,S.zeros(pdims.get(j,0),ndims.get(j,0))),
                     inc.get(j-1,S.zeros(pdims.get(j-1,0),ndims.get(j-1,0))))
        for j in range(1,5)}
    for j in range(2,5): assert wd[j]*iw[j]==iw[j-1]*ed[j]
    maps={j:WH[j][2]*iw[j]*EH[j][1] for j in range(1,5)}
    multiplicity=S.Matrix([1,*list(marks)])
    fcoord=EH[2][2]*multiplicity.col_join(S.zeros(8,1))
    cases.append(dict(a=a,b=b,translation=ints(T),
        exterior_homology={str(j):WH[j][0] for j in WH},
        boundary_homology={str(j):EH[j][0] for j in EH},
        boundary_maps={str(j):ints(maps[j]) for j in maps},
        fibre_boundary_H2=ints(fcoord),fibre_exterior_H2=ints(maps[2]*fcoord)))
result=dict(status='PASS: exact E7 source and boundary chain maps',
    scope='Cap norm and specialization maps are supplied geometrically in the companion proof.',
    cartan=ints(A),source_gram=ints(B),translation_plus_G=ints(Tp),
    component_inclusion=ints(L),cases=cases)
(root/'iii_star_good_complement.json').write_text(json.dumps(result,indent=2)+'\n')
for c in cases:
    print('a,b=',c['a'],c['b'],'exterior',c['exterior_homology'],'boundary',c['boundary_homology'])
    print('H2 inclusion',c['boundary_maps']['2'],'F',c['fibre_boundary_H2'],'->',c['fibre_exterior_H2'])
print('PASS: all integral E7 boundary maps and marked fibre classes.')
