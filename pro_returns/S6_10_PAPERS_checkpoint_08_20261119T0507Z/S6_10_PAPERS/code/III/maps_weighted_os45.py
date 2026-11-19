"""Research certificate for OS45 (P,Q)=(2G,8G), weight2 at I8.

No smooth classification is asserted by this first extraction.  It retains
the actual period lattice, full H2 presentation, literal critical sum,
and regular-clutch linking data.
"""
from pathlib import Path
import json
import sympy as s
from manifolds_general_initial import compute,integer_solution,graph_data
from manifolds_rankone_families import decomp,bezout,biv,wedge,ikernel
from manifolds_even_critical_cycles import solve_from_smith
from manifolds_weighted_profiles import group

root=Path(__file__).resolve().parent
result=compute(45,'default',2,8,[2,0,0,0,0],e=1)
A=[s.Matrix(v) for v in result['fundamental_group']['conjugation_matrices']]
M=s.Matrix(result['H2_matrix'])
D,U,V,rank=decomp(M);Ui=U.inv()
offset=6*len(A)
power=s.Matrix([0,0,0,-1])
def clutch(c):return c[offset:offset+4,:]+power*c[offset+4]
tors_indices=[j for j in range(rank) if abs(D[j,j])>1]
assert len(tors_indices)==1
j=tors_indices[0];order=abs(int(D[j,j]));z=Ui[:,j]
coeff=V[:,j]*(1 if D[j,j]>0 else -1)
assert M*coeff==order*z
tors_link=clutch(coeff)
M_no_clutch=M[:,list(range(offset))+list(range(offset+5,M.cols))]
cohom_rows=ikernel(M_no_clutch.T).T
assert cohom_rows.rows==4
aux_target=s.Matrix([0,0,-8,0,0])
aux_coeff=integer_solution((cohom_rows*M[:,offset:offset+5]).T,aux_target)
aux_cohomology=aux_coeff.T*cohom_rows
assert aux_cohomology*M_no_clutch==s.zeros(1,M_no_clutch.cols)
alpha_clutch=aux_cohomology*M[:,offset:offset+5]
alpha_torsion=(aux_cohomology*z)[0]
phi=-U[j,:]
assert list(phi[:6])==[1,0,0,0,0,0]
K,Js,correction=graph_data(A)
peripheral=[phi[:,6:]*J for J in Js]

total=s.zeros(6,1);local=[]
for site,Aj in enumerate(A[1:]):
    DD,LU,LV,rr=decomp(Aj[:2,:2]-s.eye(2));assert rr==1
    a=LU.inv()[:,0]
    bc,g=bezout(list(a));assert g==1
    b=s.Matrix([-bc[1],bc[0]])
    T=s.eye(4);T[:2,:2]=s.Matrix.hstack(a,b);assert T.det()==1
    Ac=T.inv()*Aj*T
    L=Ac.extract([0,2],[1,3])
    short=s.Matrix.hstack(s.eye(4)[:,0],s.eye(4)[:,2])
    long=s.Matrix.hstack(s.eye(4)[:,1],s.eye(4)[:,3])
    if L.det():
        index=int(L.det());assert index==16 and site==0
        lb=long*L.inv()
        eta=index*(biv(short[:,0],lb[:,0])+biv(lb[:,0],short[:,1])
                   +biv(short[:,1],lb[:,1]))
        kind='full transferred rank-two critical cycle'
    else:
        DL,UL,VL,rr=decomp(L);assert rr==1
        alpha=UL.inv()[:,0]
        if alpha[0]<0:alpha=-alpha
        bc,g=bezout(list(alpha));assert g==1
        sigma=s.Matrix([-bc[1],bc[0]])
        row=bc.T*L;rho=s.gcd_list(list(row));row=row/rho
        beta,g=bezout(list(row));assert g==1
        ell=s.Matrix([-row[1],row[0]])
        assert L*beta==rho*alpha and L*ell==s.zeros(2,1)
        eta=rho*biv(short*sigma,long*ell)
        index=int(rho);kind='full rank-one critical cycle'
    eta=wedge(T)*eta
    assert all(v.q==1 for v in eta)
    total+=eta
    local.append(dict(site=site,basis=T.tolist(),period=L.tolist(),
                      components=index,kind=kind,critical_lift=list(map(int,eta))))

zz=total.col_join(s.zeros(M.rows-6,1))
coordinates=U*zz
crit_order=1
for i in range(rank):
    if abs(D[i,i])>1:
        crit_order=s.ilcm(crit_order,int(abs(D[i,i]))//s.igcd(int(abs(D[i,i])),int(coordinates[i])))
assert all(v==0 for v in coordinates[rank:])
crit_bound=solve_from_smith(M,D,U,V,rank,int(crit_order)*zz)
crit_link=clutch(crit_bound)

# H1 of the actual complement of the single rank-two cusp.
count=len(A);rows=4+count-1
h1=[(B-s.eye(4))[:,j].col_join(s.zeros(count-1,1))
    for B in A for j in range(4)]
def base(i):
    return s.eye(count-1)[:,i] if i<count-1 else -s.ones(count-1,1)
h1.append((-power).col_join(base(0)))
for cap in result['local'][1:]:
    i=1+cap['site']
    F=s.Matrix(cap['pi1_kernel'])
    h1.extend(v.col_join(s.zeros(count-1,1)) for v in F.columnspace())
    h1.append(s.zeros(4,1).col_join(base(i)))
E_h1=s.Matrix.hstack(*h1)
ED,EU,EV,erank=decomp(E_h1)

out=dict(scope=__doc__,homology=result['homology'],matrix_shape=list(M.shape),
         local=local,torsion_order=order,
         torsion_cycle=list(map(int,z)),torsion_bound=list(map(int,coeff)),
         torsion_regular_link=list(map(int,tors_link)),
         primitive_torsion_character=list(map(int,U[j,:])),
         no_clutch_h2_quotient=group(M_no_clutch),
         auxiliary_cohomology_row=list(map(int,aux_cohomology)),
         auxiliary_clutch_values=list(map(int,alpha_clutch)),
         auxiliary_torsion_generator_value=int(alpha_torsion),
         full_torsion_class_core_row=list(map(int,phi)),
         torsion_class_peripheral_rows=[list(map(int,row)) for row in peripheral],
         torsion_class_cusp_constants=[int(peripheral[1][1]),int(peripheral[1][3])],
         critical_cycle=list(map(int,total)),
         critical_order=int(crit_order),
         critical_bound=list(map(int,crit_bound)),
         critical_regular_link=list(map(int,crit_link)),
         complement_H1=group(E_h1),complement_H1_left_change=EU.tolist(),
         complement_H1_smith=ED.tolist(),
         full=result)
(root/'maps_weighted_os45.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print('Homology:',result['homology'])
for row in local:print('site',row['site'],'L',row['period'],'critical',row['critical_lift'])
print('Torsion order:',order,'regular link:',list(tors_link))
print('Auxiliary line fibre:',list(aux_cohomology[:6]),
      'clutch:',list(alpha_clutch),'torsion generator:',alpha_torsion)
print('Full critical cycle:',list(total),'order:',crit_order,'regular link:',list(crit_link))
print('Actual cusp-complement H1:',group(E_h1))
