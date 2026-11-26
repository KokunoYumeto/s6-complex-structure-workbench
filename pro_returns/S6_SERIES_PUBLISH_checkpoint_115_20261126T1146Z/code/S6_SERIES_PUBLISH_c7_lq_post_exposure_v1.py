#!/usr/bin/env python3
"""Whole saved historical LQ arithmetic comparison after individual release.
Uses the frozen new Euclidean routine; no historical helper arithmetic is
used for this independent validation. All saved mathematical cases are read.
"""
from pathlib import Path
from datetime import datetime,timezone
from math import gcd
import json,runpy
import sympy as S
ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_star_logs_receiving'
FRESH=ROOT/'agents/continuation7_iii_star_logs'
P='S6_SERIES_PUBLISH_III_02LQ_'
NEW=runpy.run_path(str(ROOT/'code/S6_SERIES_PUBLISH_c7_lq_fresh_v1.py'),run_name='new_lq_arithmetic')
smith,egcd,wedge=NEW['smith'],NEW['egcd'],NEW['wedge']


def solve(A,b):
    diag,U,V=smith(A); y=U*b; z=S.zeros(A.cols,b.cols)
    for i,d in enumerate(diag):
        for j in range(b.cols):
            assert y[i,j]%d==0
            z[i,j]=y[i,j]/d
    assert all(y[i,j]==0 for i in range(len(diag),A.rows) for j in range(b.cols))
    ans=V*z; assert A*ans==b
    return ans


def mat(A):
    assert all(x.q==1 for x in A)
    return [[int(x) for x in A.row(i)] for i in range(A.rows)]


def kernel(k,R,N,f):
    if f==1: A,B,M=2*N,-R,k
    elif f==2: A,B,M=N,-R//2,k//2
    else: A,B,M=2*N,-R,2*k
    g,p,t=egcd(A,B); assert gcd(g,M)==1
    aa,bb=A//g,B//g
    assert p*aa+t*bb==1
    cols=[]
    for c,d in [(M*p,M*t),(-bb,aa)]:
        numerator=2*N*c-R*d
        assert numerator%k==0
        b=numerator//k
        if f==0: assert b%2==0
        cols.append(S.Matrix([0,b,c,d]))
    return S.Matrix.hstack(*cols)


def norm_identity():
    n,k,j,r,N=S.symbols('n k j r N',integer=True,nonzero=True)
    A=S.Matrix([[-1,0,-1,0],[0,-1,0,0],[0,-n,1,0],[0,0,0,1]])
    t=S.Matrix([0,j/(n*k),r/k,N/(2*k)])
    norm=(k*(S.eye(4)+A)*t).applyfunc(S.simplify)
    inverse=(k*(S.eye(4)+A.inv())*t).applyfunc(S.simplify)
    assert norm==S.Matrix([-r,0,2*r-j,N])
    assert inverse-norm==S.Matrix([j,0,0,0])
    print('SYMBOLIC NORM PASS forward norm and inverse-power norm differ by exactly j alpha',flush=True)


def markings(old,new):
    bykey={r['name']:r for r in new['rows']}
    transitions=[]
    for row in old['markings']:
        entry,profile,a,b,zero=row['key']
        name=f'OS{entry}/{profile}:zero{zero+1}:({a},{b})'
        current=bykey[name]; C=S.Matrix(row['basis']); H=S.Matrix(current['H'])
        K=C.inv()*H; Ki=H.inv()*C; n=row['n']
        A=S.Matrix(row['canonical_matrix'])
        assert K*Ki==Ki*K==S.eye(4) and K*A==A*K
        mat(K);mat(Ki)
        assert K*S.Matrix([-1,0,2,0])==S.Matrix([-1,0,2,0])
        Q=S.Matrix([[-2,0,0,1,0,0],[0,0,0,0,n,-2]])
        section=S.Matrix.hstack(S.eye(6)[:,3],S.Matrix([0,0,0,0,1,(n-1)//2]))
        induced=Q*wedge(K)*section
        assert induced==S.eye(2)
        transitions.append({'name':name,'new_to_old':mat(K),'old_to_new':mat(Ki)})
        print('MARKING PASS',name,'fibre quotient identity; both integral inverse matrices',flush=True)
    return transitions


def local_cases(cases):
    records=[]
    for c in cases:
        n,k,j,N,r=(c[x] for x in ['n','k','phase_lift','N','r'])
        q=n*k;phase=j%q;h=(j-phase)//q;R=2*r-j
        f=c['fixed_components'];rho=len(c['vertex_orbits'])
        ff,rr,cc,uu,vv=NEW['normalization'](q,phase)
        C=S.Matrix(c['normalization_relations'])
        assert ff==f and rr==rho and C==S.Matrix(cc)
        section=S.Matrix(c['common_section']); J=S.eye(C.rows)
        fixed=[i for i,O in enumerate(c['vertex_orbits']) if len(O)==1]
        for i in range(rho):
            J[:,2*i]=-S.eye(C.rows)[:,2*i]
            if i in fixed: J[:,2*i+1]=section-S.eye(C.rows)[:,2*i+1]
        assert J*J==S.eye(C.rows) and J*section==section
        chain=solve(C,J*C)
        assert chain*chain==S.eye(C.cols)
        oldimage=S.Matrix(c['full_boundary_image']); transformed=J*oldimage
        assert transformed[:,1:]==oldimage[:,1:]
        expected_x=S.zeros(C.rows,1)
        for i in range(rho): expected_x[2*i+1 if i in fixed else 2*i]=1
        edgefix=[i for i,O in enumerate(c['edge_orbits']) if len(O)==1]
        if f==1: expected_x-=S.eye(C.rows)[:,2*rho+edgefix[0]]
        elif f==2: expected_x-=section
        else:
            D0=S.eye(C.rows)[:,2*rho+edgefix[0]]
            D1=S.eye(C.rows)[:,2*rho+edgefix[1]];tau=D1-D0
            expected_x+=tau
            actualY=D0+h*tau
            solve(C,oldimage[:,1]-(-k*actualY+tau))
            solve(C,oldimage[:,2]-2*N*actualY)
            solve(C,oldimage[:,3]+R*actualY)
            # Exact cyclic vertical-cokernel presentation.
            diag,_,_=smith(C.row_join(oldimage[:,0:2]))
            assert [d for d in diag if d>1]==[2*k]
        assert transformed[:,0]==expected_x
        K=kernel(k,R,N,f);hist=S.Matrix(c['full_boundary_kernel'])
        change=K.gauss_jordan_solve(hist)[0];inverse=hist.gauss_jordan_solve(K)[0]
        mat(change);mat(inverse)
        assert change*inverse==inverse*change==S.eye(2)
        assert K*change==hist and hist*inverse==K
        solve(C,oldimage*hist)
        groups=[(1,[]),(2,[]),(rho+1,[2] if f==0 else []),(2*rho,[]),(rho,[])]
        assert c['homology']==[{'free':free,'torsion':torsion} for free,torsion in groups]
        assert c['projected_normal_index']==(k if f==1 else k//2 if f==2 else 2*k)
        assert c['normal_torus_quotient']==2*k//c['projected_normal_index']
        records.append({'n':n,'k':k,'j':j,'J':mat(J),'chain_map':mat(chain),
                        'kernel_new_to_old':mat(change),'kernel_old_to_new':mat(inverse)})
    print('LOCAL PASS',len(cases),'full conductor maps, orientation involutions, phase lifts and both kernel inverses',flush=True)
    return records


def global_cases(cases):
    for c in cases:
        k,j,N,r,e,B=(c['k'],c['phase'],c['N'],c['r'],c['e'],c['b']//4)
        R=2*r-j;s=N-2*k*e;f=1 if k%2 else 2 if j%2==0 else 0
        K=kernel(k,R,N,f);hist=S.Matrix(c['full_kernel'])
        change=K.gauss_jordan_solve(hist)[0];mat(change);assert abs(change.det())==1
        M=S.Matrix.vstack(B*(hist[1,:]-4*e*hist[2,:]),hist[3,:])
        assert M==S.Matrix(c['global_relation_matrix'])
        d,_,_=smith(M);actual=[x for x in d if x>1]
        expected=([2*B*abs(s)] if f==1 else [B*abs(s)] if f==2 else [2,2*B*abs(s)])
        assert actual==c['H2_torsion']==[x for x in expected if x>1]
        assert c['sigma']==s
    print('GLOBAL PASS',len(cases),'saved matrices and exact Smith factors independently verified',flush=True)


if __name__=='__main__':
    print('START',datetime.now(timezone.utc).isoformat(),flush=True)
    old=json.loads((LANE/(P+'historical_manifolds_star_log_caps.json')).read_text())
    new=json.loads((FRESH/(P+'fresh_data_v1.json')).read_text())
    assert set(old)=={'scope','markings','cases','aspherical_marking','one_star'}
    norm_identity();transitions=markings(old,new);local=local_cases(old['cases']);global_cases(old['one_star'])
    dest=LANE/(P+'post_exposure_data_v1.json')
    dest.write_text(json.dumps({'marking_transitions':transitions,'local_chain_maps':local},indent=2)+'\n')
    print('DATA',dest.name,dest.stat().st_size,flush=True)
    print('PASS',datetime.now(timezone.utc).isoformat(),flush=True)
