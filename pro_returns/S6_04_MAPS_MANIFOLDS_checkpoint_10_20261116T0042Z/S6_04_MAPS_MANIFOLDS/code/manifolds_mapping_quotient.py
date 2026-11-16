"""B6.20 marked quotient lattice and exact cup-cube calculation.

The geometric multiplicative comparison and all cap markings are proved in
manifolds_mapping_quotient_proof.tex and independently audited by root/maps.
"""
from pathlib import Path
from itertools import combinations
import json
import sympy as s
from manifolds_rankone_families import decomp,ikernel,wedge,biv
A1=s.Matrix([[1,0,0,0],[6,0,1,-1],[-6,-1,-1,1],[0,0,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,1],[0,0,0,1]])
C1=s.eye(4);C1[2,0]=-1;C1[2,1]=1
C2=s.eye(4);C2[2,0]=1
A=[A1,A2,C1,C2]
v=[s.Matrix([1,2,-4,0]),s.Matrix([-1,-3,3,0])]
assert A1*A2*C1*C2==s.eye(4)
D=s.Matrix.hstack(*[x-s.eye(4) for x in A[:3]])
DD,U,V,r=decomp(D)
E=s.Matrix.hstack(*[wedge(x)-s.eye(6) for x in A])
DE,UE,VE,re=decomp(E)
def j(i,x):
    if i<3:
        z=s.zeros(12,x.cols);z[4*i:4*i+4,:]=x;return z
    return -(A2*C1*x).col_join(C1*x).col_join(x)
fixed=[ikernel(x-s.eye(4)) for x in A]
K=ikernel(D)
DK,UK,VK,rk=decomp(K)
L=VK*s.diag(*[1/DK[i,i] for i in range(rk)])*UK[:rk,:]
assert L*K==s.eye(rk)
B=s.Matrix.hstack(*[L*j(i,fixed[i]) for i in (2,3)])
DB,UB,VB,rb=decomp(B)
record={'basis':['g','u','w','k'], 'monodromies':[x.tolist() for x in A],
        'fibre_H1_coinvariants_smith':[int(DD[i,i]) for i in range(r)],
        'fibre_H1_coinvariants_rank':4-r,
        'fibre_H2_coinvariants_smith':[int(DE[i,i]) for i in range(re)],
        'fibre_H2_coinvariants_rank':6-re,
        'fibre_H2_covectors':ikernel(E.T).T.tolist(),
        'graph_kernel':K.tolist(),'graph_left_inverse':L.tolist(),
        'node_normal_matrix':B.tolist(),'node_normal_rank':rb,
        'node_normal_smith':[int(DB[i,i]) for i in range(rb)],'finite':[]}
for i,m in enumerate((3,4)):
    assert A[i]**m==s.eye(4) and A[i]*v[i]==v[i]
    low=A[i][1:,1:]
    dl,ul,vl,rl=decomp(low-s.eye(3))
    capH1=ul[rl:,:]
    norms=sum([A[i]**k for k in range(m)],s.zeros(4))
    record['finite'].append({'order':m,'power_vector':v[i].tolist(),
      'fixed':fixed[i].tolist(),'norm':norms.tolist(),
      'cap_T3_monodromy':low.tolist(),
      'cap_H1_fibre_smith':[int(dl[j,j]) for j in range(rl)],
      'cap_H1_fibre_projection':capH1.tolist()})
    print('finite',i+1,'fixed',fixed[i].tolist(),'capH1Smith',
          [int(dl[j,j]) for j in range(rl)], 'projection',capH1.tolist())
print('fibre H1',record['fibre_H1_coinvariants_smith'],record['fibre_H1_coinvariants_rank'])
print('fibre H2',record['fibre_H2_coinvariants_smith'],record['fibre_H2_coinvariants_rank'])
print('fibre H2 covectors',record['fibre_H2_covectors'])
print('graph kernel',K.cols,'node normals',rb,record['node_normal_smith'])
omega=s.Matrix([[0,0,1,0,0,0]])
normal=s.zeros(11,0)
for i in (2,3):
    normal=normal.row_join(s.zeros(1,fixed[i].cols).col_join(L*j(i,fixed[i])))
for i,m in enumerate((3,4)):
    norm=sum([A[i]**k for k in range(m)],s.zeros(4))
    k=s.eye(4)[:,3]
    first=s.Matrix([-(omega*biv(k,v[i]))[0]]).col_join(L*j(i,norm*k))
    second=s.zeros(1,1).col_join(L*j(i,v[i]))
    normal=normal.row_join(first).row_join(second)
DN,UN,VN,rn=decomp(normal)
print('full quotient H2 normal Smith', [int(DN[i,i]) for i in range(rn)], 'free rank',11-rn)
projection=UN[rn:,:]
print('H2 quotient projection',projection.tolist(), 'fibre gk value',projection[0,0])
record['full_H2_normals']=normal.tolist()
record['full_H2_smith']=[int(DN[i,i]) for i in range(rn)]
record['H2_projection']=projection.tolist()
Path(__file__).with_suffix('.out.json').write_text(json.dumps(record,indent=2,default=int)+'\n')

# Multiplicative path-form calculation. The companion proof verifies the
# actual finite/nodal cap pullbacks, smooth seams and inverse convention.
eta=(projection[:,1:]*L).T
eta=[eta[4*i:4*i+4,0] for i in range(3)]
g=s.eye(4)[:,0]; kk=s.eye(4)[:,3]
e0=2*biv(g,kk)
def triple1(a,b):
    # coefficient of a wedge (2 gamma wedge kappa) wedge b
    return 2*s.Matrix.hstack(a,g,kk,b).det()
segments=[[eta[0]],[eta[1]],[eta[2]],
          [-C2.T*C1.T*A2.T*eta[0],-C2.T*C1.T*eta[1],-C2.T*eta[2]]]
cube=0; values=[]
for i in range(4):
    capbeta=s.zeros(4,1)
    if i<2:
        aa=v[i]/(3 if i==0 else 4)
        # contraction by aa of 2 gamma wedge kappa
        capbeta=-2*(aa[0]*kk-aa[3]*g)
    parts=segments[i]
    # Split cap's unit-length normal angular circle evenly among segments.
    bs=[p-capbeta/len(parts) for p in parts]
    total=sum(bs,s.zeros(4,1))
    try:
        lam=(A[i].T-s.eye(4)).gauss_jordan_solve(total)[0]
    except ValueError:
        print('NO PATH HOMOTOPY',i,total.tolist());continue
    lam=lam.subs({x:0 for x in lam.free_symbols})
    term=0
    for bpart in bs:
        term+=3*triple1(lam,bpart)
        lam+=bpart
    values.append(term);cube+=term
print('raw oriented cap cup contributions',values,'sum',cube)
print('exterior eta',[x.T.tolist() for x in eta])

record['path_model']={'eta':[list(x) for x in eta], 'raw_cap_contributions':values,
    'raw_sum':cube,'geometric_absolute_cube':abs(cube),
    'status':'B6.20 proved; root and maps independent audits passed; absolute cube1, oriented k=-1 from ell=-4 and spin congruence'}
Path(__file__).with_suffix('.out.json').write_text(json.dumps(record,indent=2,default=lambda x:int(x) if x.q==1 else str(x))+'\n')

assert values==[2,-3,0,0] and cube==-1
