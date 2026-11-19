"""Literal critical cycles for the II and c20 extensions of D44.

Original II contributes twice the principal elliptic curve, represented
by delta wedge ell with ell=(-z,0,1), (B-I)z=q. A free finite-good II
log contributes no critical curve (the corrected differential is regular).
This certificate computes linking only; it infers no framing consequence.
"""
from pathlib import Path
from math import gcd,lcm
import json
import sympy as s
import manifolds_all_weighted_profiles as B
from manifolds_rankone_families import decomp,bezout,biv,wedge
from manifolds_even_critical_cycles import solve_from_smith
from manifolds_general_initial import integer_solution,graph_data
ROOT=Path(__file__).resolve().parent

def critical_lift(A,kind,is_finite=False):
    if kind=='II':
        z=integer_solution(A[:2,:2]-s.eye(2),A[:2,3])
        ell=(-z).col_join(s.Matrix([0,1]));delta=s.eye(4)[:,2]
        assert A*ell==ell and s.det(A[:2,:2]-s.eye(2))==1
        reduced=biv(delta,ell)
        return (s.zeros(6,1) if is_finite else 2*reduced),dict(
            type=kind,finite=is_finite,logarithm=list(map(int,z)),
            fixed_long=list(map(int,ell)),reduced_curve_lift=list(map(int,reduced)),
            multiplicity=(0 if is_finite else 2))
    E,UU,VV,rr=decomp(A[:2,:2]-s.eye(2));assert rr==1
    u=UU.inv()[:,0];bc,g=bezout(list(u));assert g==1
    v=s.Matrix([-bc[1],bc[0]])
    C=s.eye(4);C[:2,:2]=s.Matrix.hstack(u,v);assert C.det()==1
    Ac=C.inv()*A*C;L=Ac.extract([0,2],[1,3])
    short=s.Matrix.hstack(s.eye(4)[:,0],s.eye(4)[:,2])
    long=s.Matrix.hstack(s.eye(4)[:,1],s.eye(4)[:,3])
    if L.det():
        assert L.det()==1
        lb=long*L.inv()
        eta=biv(short[:,0],lb[:,0])+biv(lb[:,0],short[:,1])+biv(short[:,1],lb[:,1])
    else:
        DD,LU,LV,rankL=decomp(L);assert rankL==1
        alpha=LU.inv()[:,0]
        if alpha[0]<0:alpha=-alpha
        bc,g=bezout(list(alpha));assert g==1
        sigma=s.Matrix([-bc[1],bc[0]])
        rr=bc.T*L;rho=s.gcd_list(list(rr));rr=rr/rho
        beta,g=bezout(list(rr));assert g==1
        ell=s.Matrix([-rr[1],rr[0]])
        assert s.det(s.Matrix.hstack(alpha,sigma))==s.det(s.Matrix.hstack(beta,ell))==1
        assert L*beta==rho*alpha and L*ell==s.zeros(2,1)
        eta=biv(short*sigma,long*ell)
    eta=wedge(C)*eta
    return eta,dict(type=kind,basis=C.tolist(),period=L.tolist(),curve_lift=list(map(int,eta)))

def run(i,e=1,finite=None):
    p=B.W.PATTERNS[i];row=B.W.MONO[B.W.key(p)];residual=p['b']
    result=B.compute(i,1,e=e,finite=finite)
    assert result['homology'][1]==dict(free=0,torsion=[])
    assert result['homology'][2]==result['homology'][3]==dict(free=0,torsion=[residual])
    M=s.Matrix(result['H2_matrix']);D,U,V,rank=decomp(M);Ui=U.inv()
    offset=6*(len(row['local'])+1);power=s.Matrix([0,0,0,-e])
    def clutch(c):return c[offset:offset+4,:]+power*c[offset+4]
    indices=[j for j in range(rank) if abs(D[j,j])>1];assert len(indices)==1
    j=indices[0];order=abs(int(D[j,j]));cycle=Ui[:,j]
    coeff=V[:,j]*(1 if D[j,j]>0 else -1)
    assert M*coeff==order*cycle
    linking=clutch(coeff)
    regular_torus_order=order//gcd(int(linking[2]),order)
    regular_H3_image_order=order//gcd(order,*map(int,linking))
    assert all(clutch(V[:,q])[2]==0 for q in range(rank,M.cols))
    total=s.zeros(6,1);local=[]
    for site,loc in enumerate(row['local']):
        eta,record=critical_lift(s.Matrix(loc['matrix']),loc['type'],site in p['finite_indices'])
        total+=eta;record['site']=site;local.append(record)
    z=total.col_join(s.zeros(M.rows-6,1))
    rhs=U*z
    assert not any(rhs[j] for j in range(rank,M.rows))
    multiplier=lcm(*(abs(int(D[j,j]))//gcd(abs(int(D[j,j])),int(rhs[j])) for j in range(rank)))
    if residual in [4,8]:assert multiplier==1
    critical_coeff=solve_from_smith(M,D,U,V,rank,multiplier*z)
    critical_clutch=clutch(critical_coeff)
    core_record=None
    if p['finite_indices']:
        assert len(p['finite_indices'])==1
        site=p['finite_indices'][0];A=s.Matrix(row['local'][site]['matrix'])
        zlog=integer_solution(A[:2,:2]-s.eye(2),A[:2,3])
        t=A[2,:2]*(A[:2,:2]-s.eye(2)).inv()
        psi=s.Matrix([[-t[0],-t[1],1,-(t*zlog)[0]]])
        data=finite[site];m=int(data['m']);vv=s.Matrix(data['v'])
        r=int((psi*vv)[0]);n=int(vv[3]);d=gcd(r,n)
        sigma=n-m*e;assert sigma in [-1,1]
        char=psi-sigma*r*s.Matrix([[0,0,0,1]])
        root_character=-sigma*r*e
        assert all(x.q==1 for x in char) and (char*vv)[0]==m*root_character
        assert gcd(m,d)==1 and abs(n-m*e)==1
        cursor=offset+5;cap_offset=None
        for locdata in result['local']:
            j0=locdata['site']
            if j0==site:cap_offset=cursor
            if locdata['kind']=='finite':cursor+=5
            else:
                cursor+=B.ikernel(s.Matrix(row['local'][j0]['matrix'])-s.eye(4)).cols+locdata['fibre_kernel_rank']
        assert cursor==M.cols and cap_offset is not None
        def core_pair(c):return int((char*c[cap_offset:cap_offset+4,:])[0]+root_character*c[cap_offset+4])
        core_link=core_pair(coeff)
        assert gcd(core_link,order)==1
        assert all(core_pair(V[:,q])==0 for q in range(rank,M.cols))
        omega=s.Matrix([[p['a'],0,0,0,0,-p['b']]])
        critical_scalar=int((omega*total)[0])
        qcrit=multiplier*critical_scalar//residual
        assert qcrit*residual==multiplier*critical_scalar
        assert core_pair(critical_coeff)==sigma*qcrit
        unit,gcdab=bezout([p['a'],-p['b']]);assert gcdab==1
        standard_cycle=s.zeros(M.rows,1);standard_cycle[0]=unit[0];standard_cycle[5]=unit[1]
        standard_coeff=solve_from_smith(M,D,U,V,rank,residual*standard_cycle)
        standard_link=core_pair(standard_coeff)
        assert standard_link==sigma
        core_record=dict(delta_projection=psi.tolist()[0],character=char.tolist()[0],
                         root_character=root_character,r=r,n=n,m=m,d=d,column_offset=cap_offset,
                         torsion_linking=core_link,image_order=order//gcd(core_link,order),
                         two_primary_generator=True,standard_generator_linking=standard_link,
                         critical_scalar=critical_scalar,critical_multiple_scalar=qcrit,
                         critical_linking=core_pair(critical_coeff))
    return dict(pattern=i,key=B.W.key(p),e=e,c=residual,finite=finite or {},
                regular_three_torus='e1 wedge e2 wedge gamma',
                torsion_cycle=cycle.T.tolist()[0],
                torsion_bounding_coefficients=coeff.T.tolist()[0],
                torsion_linking_loop=list(map(int,linking)),
                regular_three_torus_order=regular_torus_order,
                regular_H3_image_order=regular_H3_image_order,
                local_critical_lifts=local,critical_cycle=list(map(int,total)),
                critical_cycle_order=multiplier,
                critical_bounding_coefficients=critical_coeff.T.tolist()[0],
                critical_linking_loop=list(map(int,critical_clutch)),
                critical_linking=int(critical_clutch[2]),finite_core=core_record)

def symbolic_certificates(records):
    """Fixed integral chain lifts proving the formulas for every parameter."""
    certificates=[];seen=set()
    for rec in records:
        i=rec['pattern']
        if i in seen:continue
        seen.add(i);p=B.W.PATTERNS[i];row=B.W.MONO[B.W.key(p)]
        A=[s.eye(4)]+[s.Matrix(x['matrix']) for x in row['local']]
        delta=s.eye(4)[:,2];gamma=s.eye(4)[:,3]
        Kgraph,Js,correction=graph_data(A)
        assert all(M*delta==delta for M in A)
        assert all(correction(j,delta)==s.zeros(6,1) for j in range(len(A)))
        assert sum((J*delta for J in Js),s.zeros(Kgraph.cols,1))==s.zeros(Kgraph.cols,1)
        R=s.Matrix.hstack(*[wedge(M)-s.eye(6) for M in A])
        DD,UU,VV,rank=decomp(R)
        assert rank==5 and all(abs(DD[j,j])==1 for j in range(rank))
        a,b=p['a'],p['b'];omega=s.Matrix([[a,0,0,0,0,-b]])
        assert omega*R==s.zeros(1,R.cols)
        bc,g=bezout([a,-b]);assert g==1
        zs=s.zeros(6,1);zs[0]=bc[0];zs[5]=bc[1]
        assert (omega*zs)[0]==1
        critical=s.Matrix(rec['critical_cycle']);C=int((omega*critical)[0])
        crit_difference=integer_solution(R,critical-C*zs)
        ordinary=integer_solution(R,biv(delta,gamma)+b*zs)
        cert=dict(pattern=i,key=B.W.key(p),finite=bool(p['finite_indices']),
                  fibre_relation_matrix=R.tolist(),standard_fibre_generator=list(map(int,zs)),
                  critical_scalar=C,critical_order=b//gcd(b,C),
                  critical_difference_coefficients=list(map(int,crit_difference)),
                  ordinary_difference_coefficients=list(map(int,ordinary)),
                  delta_bar_corrections_zero=True,peripheral_delta_sweeps_sum_zero=True)
        if p['finite_indices']:
            site=p['finite_indices'][0];M=A[site+1]
            zlog=integer_solution(M[:2,:2]-s.eye(2),M[:2,3])
            ell=(-zlog).col_join(s.Matrix([0,1]))
            finite_difference=integer_solution(R,-biv(delta,ell)-b*zs)
            m,n,e,r=s.symbols('m n e r',integer=True)
            v=r*delta+n*ell
            actual=-biv(delta,v)+m*e*biv(delta,gamma)
            polynomial=n*finite_difference+m*e*ordinary
            assert R*polynomial==actual-b*(n-m*e)*zs
            cert.update(fixed_long=list(map(int,ell)),
                        finite_difference_coefficients=list(map(int,finite_difference)),
                        all_parameter_identity='R*(n*c_fin+m*e*c_ord) = -delta wedge v + m*e*delta wedge gamma - b*(n-m*e)*s',
                        all_parameter_core_link='(n-m*e)*(D*Omega(Crit)/b), when n-m*e=+/-1',
                        core_standard_generator_link='n-m*e')
        else:
            cert['all_parameter_regular_link']='-e*D*Omega(Crit)/b, e=+/-1'
        certificates.append(cert)
    assert len(certificates)==11
    (ROOT/'manifolds_extended_critical_symbolic.json').write_text(
        json.dumps(dict(scope='Unbounded integral delta-chain identities, retaining monodromy preimages',
                        rows=certificates),indent=2,default=int)+'\n')
    print('All-parameter delta-chain certificates',len(certificates),flush=True)
    return certificates

if __name__=='__main__':
    keys={(45,'II',1,8,2),(45,'II',1,8,3),(55,'II',5,4,3),(55,'II',1,20,3)}
    keys|={(55,'default',1,20,i) for i in [2,3,4]}
    records=[]
    for i,p in enumerate(B.W.PATTERNS):
        if B.W.key(p) not in keys:continue
        if any(v=='original' for _,v in p['multiplicative_choices']):continue
        if not p['finite_indices']:
            for e in [-1,1]:records.append(run(i,e=e))
        else:
            assert len(p['finite_indices'])==1
            site=p['finite_indices'][0]
            A=s.Matrix(B.W.MONO[B.W.key(p)]['local'][site]['matrix'])
            assert B.W.MONO[B.W.key(p)]['local'][site]['type']=='II'
            z=integer_solution(A[:2,:2]-s.eye(2),A[:2,3])
            ell=(-z).col_join(s.Matrix([0,1]));delta=s.eye(4)[:,2]
            for k in [1,2,3]:
                m=6*k
                for r in [0,1]:
                    for e in [-1,0,1]:
                        for sign in [-1,1]:
                            n=m*e+sign;v=r*delta+n*ell
                            data={site:dict(m=m,v=list(map(int,v)))}
                            rec=run(i,e=e,finite=data);rec['canonical_parameters']=[k,r,e,sign]
                            records.append(rec)
        recent=[r for r in records if r['pattern']==i]
        print(B.W.key(p),'pattern',i,'finite',bool(p['finite_indices']),
              'cases',len(recent),'critical orders',sorted({r['critical_cycle_order'] for r in recent}),
              'regular T3 orders',sorted({r['regular_three_torus_order'] for r in recent}),
              'regular H3 image orders',sorted({r['regular_H3_image_order'] for r in recent}),
              'critical values',sorted({r['critical_linking'] for r in recent}),
              'parities',sorted({r['critical_linking']%2 for r in recent}),
              'core critical values',sorted({r['finite_core']['critical_linking'] for r in recent if r['finite_core']}),
              'core parities',sorted({r['finite_core']['critical_linking']%2 for r in recent if r['finite_core']}),flush=True)
    assert len(records)==158
    (ROOT/'manifolds_extended_critical_cycles.json').write_text(
        json.dumps(dict(scope=__doc__,rows=records),indent=2,default=int)+'\n')
    symbolic_certificates(records)
