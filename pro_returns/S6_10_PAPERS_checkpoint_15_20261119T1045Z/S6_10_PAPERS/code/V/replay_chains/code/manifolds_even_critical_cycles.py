"""Actual regular-three-torus and complex critical-cycle linking for seven rows.

Only the seven default semistable c=4,8 rows are asserted here.
All cap curves are lifted using their actual unimodular Tate markings.
No framing consequence is inferred by this algebraic certificate alone.
"""
from pathlib import Path
import json
import sympy as s
import manifolds_all_weighted_profiles as B
from manifolds_rankone_families import decomp,bezout,biv,wedge
ROOT=Path(__file__).resolve().parents[1]

def solve_from_smith(M,D,U,V,rank,z):
    rhs=U*z;temp=s.zeros(M.cols,1)
    for j in range(rank):
        assert rhs[j]%D[j,j]==0
        temp[j]=rhs[j]/D[j,j]
    assert all(v==0 for v in rhs[rank:])
    coeff=V*temp;assert M*coeff==z
    return coeff

def run(i,e=1):
    p=B.W.PATTERNS[i];row=B.W.MONO[B.W.key(p)];residual=p['b']
    assert e in [-1,1]
    result=B.compute(i,1,e=e)
    assert result['homology'][2]==result['homology'][3]==dict(free=0,torsion=[residual])
    M=s.Matrix(result['H2_matrix']);D,U,V,rank=decomp(M);Ui=U.inv()
    offset=6*(len(row['local'])+1);power=s.Matrix([0,0,0,-e])
    def clutch(c):return c[offset:offset+4,:]+power*c[offset+4]
    indices=[j for j in range(rank) if abs(D[j,j])>1];assert len(indices)==1
    j=indices[0];order=abs(int(D[j,j]));cycle=Ui[:,j]
    coeff=V[:,j]*(1 if D[j,j]>0 else -1)
    assert M*coeff==order*cycle
    linking=clutch(coeff)
    assert s.gcd(int(linking[2]),order)==1
    # A closed three-chain has zero integral intersection with the torsion T3.
    assert all(clutch(V[:,q])[2]==0 for q in range(rank,M.cols))
    total=s.zeros(6,1);local=[]
    for site,loc in enumerate(row['local']):
        A=s.Matrix(loc['matrix'])
        E,UU,VV,rr=decomp(A[:2,:2]-s.eye(2));assert rr==1
        u=UU.inv()[:,0];bc,g=bezout(list(u));assert g==1
        v=s.Matrix([-bc[1],bc[0]])
        C=s.eye(4);C[:2,:2]=s.Matrix.hstack(u,v);assert C.det()==1
        Ac=C.inv()*A*C;L=Ac.extract([0,2],[1,3])
        short=s.Matrix.hstack(s.eye(4)[:,0],s.eye(4)[:,2])
        long=s.Matrix.hstack(s.eye(4)[:,1],s.eye(4)[:,3])
        if L.det():
            assert L.det()==1 and site==p['zero_index']
            lb=long*L.inv()
            eta=biv(short[:,0],lb[:,0])+biv(lb[:,0],short[:,1])+biv(short[:,1],lb[:,1])
            # Alternative lift of the mixed support-function degree.
            alternate=biv(short[:,0],lb[:,0])+biv(lb[:,1],short[:,0])+biv(short[:,1],lb[:,1])
            kind='sum of three cusp double curves'
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
            alternate=biv(short*(sigma+alpha),long*ell)
            kind='nodal transverse elliptic curve'
        eta=wedge(C)*eta;alternate=wedge(C)*alternate;total+=eta
        diff=(alternate-eta).col_join(s.zeros(M.rows-6,1))
        altcoeff=solve_from_smith(M,D,U,V,rank,diff)
        assert clutch(altcoeff)[2]==0
        local.append(dict(site=site,type=loc['type'],kind=kind,basis=C.tolist(),
                          period=L.tolist(),curve_lift=list(map(int,eta)),
                          alternate_lift=list(map(int,alternate))))
    z=total.col_join(s.zeros(M.rows-6,1))
    critical_coeff=solve_from_smith(M,D,U,V,rank,z)
    critical_clutch=clutch(critical_coeff)
    record=dict(pattern=i,key=B.W.key(p),e=e,c=residual,
                regular_three_torus='e1 wedge e2 wedge gamma',
                torsion_cycle=cycle.T.tolist()[0],
                torsion_bounding_coefficients=coeff.T.tolist()[0],
                torsion_linking_loop=list(map(int,linking)),
                local_critical_lifts=local,critical_cycle=list(map(int,total)),
                critical_bounding_coefficients=critical_coeff.T.tolist()[0],
                critical_linking_loop=list(map(int,critical_clutch)),
                critical_linking=int(critical_clutch[2]))
    return record

if __name__=='__main__':
    candidates=json.loads((ROOT/'records/manifolds_nonstar_sphere_patterns.json').read_text())['all_patterns']
    keys={B.W.key(p) for p in candidates if p['residual_c'] in [4,8]
          and not p['orbifold_obstruction'] and p['profile']=='default'}
    records=[]
    for i,p in enumerate(B.W.PATTERNS):
        if B.W.key(p) not in keys:continue
        if any(v=='original' for _,v in p['multiplicative_choices']):continue
        for e in [1,-1]:
            r=run(i,e=e);records.append(r)
            print(r['key'],'e',e,'c',r['c'],'regular linking',r['torsion_linking_loop'],
                  'critical linking',r['critical_linking'],flush=True)
    assert len(records)==14
    for i in range(0,14,2):assert records[i]['critical_linking']==-records[i+1]['critical_linking']
    (ROOT/'records/manifolds_even_critical_cycles.json').write_text(
        json.dumps(dict(scope=__doc__,rows=records),indent=2,default=int)+'\n')
