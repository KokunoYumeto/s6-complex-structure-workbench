#!/usr/bin/env python3
"""Post-release exact comparison of KN's original and fresh presentations.

The original script is read only. Its pinned output is downloaded to /tmp
and retained outside every checkpoint. This program constructs the actual
unimodular morphisms and inverses between the two graph/Thom presentations.
"""
from datetime import datetime,timezone
from hashlib import sha256
from itertools import combinations
from math import gcd
from pathlib import Path
from urllib.request import urlopen
import json
import sympy as S

HERE=Path(__file__).resolve().parent
INPUT_ROOT = Path(__file__).resolve().parents[1] / 'agents/continuation6_iii_d2'
BASE=INPUT_ROOT.parent/'continuation5_iii_d2'
COMMIT='a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7'
REPO='https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/'
DIR='pro_returns/S6_04_MAPS_MANIFOLDS_checkpoint_12_20261116T0243Z/S6_04_MAPS_MANIFOLDS/'
RAW=[('code/manifolds_semistable.py','38356600a9684198c42dd71a6f69065def04e429635ccc43cf509b840f1b03c1'),
     ('records/manifolds_semistable.json','44c95103bbae48ec694d70a706e955d2dbab11d059dd1267e287873f50a2463b')]


def primary_bytes(rel,digest):
    kind='py' if rel.endswith('.py') else 'json'
    p=Path('/tmp/S6_SERIES_PUBLISH_KN_historical.'+kind)
    if not p.exists():p.write_bytes(urlopen(REPO+COMMIT+'/'+DIR+rel,timeout=40).read())
    data=p.read_bytes()
    assert sha256(data).hexdigest()==digest
    print('Pinned original',rel,'bytes',len(data),'SHA256',digest)
    return data


def serial(obj):
    if isinstance(obj,S.MatrixBase):return [[int(v) for v in r] for r in obj.tolist()]
    if isinstance(obj,dict):return {k:serial(v) for k,v in obj.items()}
    if isinstance(obj,list):return [serial(v) for v in obj]
    return obj


def main():
    print('Post-release comparison started',datetime.now(timezone.utc).isoformat())
    original_source=primary_bytes(*RAW[0]).decode()
    historical=json.loads(primary_bytes(*RAW[1]))
    fresh=json.loads((BASE/'S6_SERIES_PUBLISH_III_02KN_fresh_linear_maps.json').read_text())
    inputs=json.loads((INPUT_ROOT.parent/'continuation5_iii_infra'/'S6_SERIES_PUBLISH_III_02KN_marked_inputs.json').read_text())['rows']
    assert len(historical)==len(fresh['rows'])==4
    records=[];total=zero=0
    m,n,a,b,c=S.symbols('m n a b c',integer=True)
    M=lambda v:S.Matrix(v)
    for old,new,raw in zip(historical,fresh['rows'],inputs):
        p=new['P']
        assert old['entry']==new['OS'] and old['P']==p
        assert old['types']==raw['fibers']
        assert old['A']==new['matrices']
        assert old['omega']==new['omega']
        for aa,gg,pc,qc in zip(raw['elliptic_matrices'],raw['generator_section_cocycle'],
                               old['P_components'],old['Q_components']):
            N=M(aa)-S.eye(2)
            order=gcd(*(int(v) for v in N))
            col=next(N[:,i] for i in range(2) if N[:,i]!=S.zeros(2,1))
            primitive=col/gcd(*(int(v) for v in col))
            first=next(i for i in range(2) if primitive[i])
            if primitive[first]<0:primitive=-primitive
            coeff=S.Rational(gg[first],primitive[first])
            assert coeff.q==1 and M(gg)==coeff*primitive
            assert pc==([int(p*coeff)%order] if order>1 else [])
            assert qc==([int(coeff)%order] if order>1 else [])
            assert all(v==0 for v in pc)
        T=[M(x) for x in new['matrices']]
        D=S.Matrix.hstack(*(x-S.eye(4) for x in T[:5]))
        j5=-S.Matrix.vstack(T[1]*T[2]*T[3]*T[4],T[2]*T[3]*T[4],
                           T[3]*T[4],T[4],S.eye(4))
        assert D*j5==S.eye(4)-T[5].inv()
        Ko,Lo,Bo=(M(old[k]) for k in ['primitive_fixed_sweeps','left_inverse','unchanged_normals'])
        W=M(old['graph_kernel'])
        assert D*W==S.zeros(4,17) and W.rank()==17
        Kn=M(new['graph_K'])
        Ln=M(new['graph_complete_inverse'])[3:,:]
        assert abs((Ln*W).det())==1
        assert Lo*Ko==Ln*Kn==S.eye(17)
        assert D*Ko==D*Kn==S.zeros(4,17)
        # Fresh graph order is (three smooth, fourteen reduced) whereas the
        # original order is (fourteen reduced, three smooth).
        Q=Lo[:14,:]*Kn[:,3:]
        Qi=Q.inv()
        assert abs(Q.det())==1 and all(v.q==1 for v in Qi)
        assert Bo*Q==Kn[:,3:]
        A=Ln*Ko;Ai=Lo*Kn
        assert A*Ai==Ai*A==S.eye(17)
        assert Kn*A==Ko and Ko*Ai==Kn
        j0=S.zeros(20,4);j0[:4,:]=S.eye(4)
        J=S.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1]])
        assert M(old['J'])==J and M(old['projection'])*j0==J
        assert M(old['projection'])*Ko==S.zeros(3,14).row_join(S.eye(3))
        assert (Lo*j0)[14:,:]==J and (Ln*j0)[:3,:]==J
        assert A*Lo*j0==Ln*j0
        form=S.zeros(4);form[0,1]=p;form[1,0]=-p
        form[2,3]=-1;form[3,2]=1
        v=S.Matrix([a,b,c,n])
        fibre=-(form*v).T
        smooth_old=S.zeros(18,5);smooth_old[0,:4]=fibre
        smooth_old[1:,:4]=m*Lo*j0;smooth_old[1:,4]=Lo*j0*v
        normals_old=S.zeros(18,14);normals_old[1:15,:]=S.eye(14)
        F_old=normals_old.row_join(smooth_old)
        smooth_new=S.zeros(18,5);smooth_new[0,:4]=fibre
        smooth_new[1:,:4]=m*Ln*j0;smooth_new[1:,4]=Ln*j0*v
        normals_new=S.zeros(18,14);normals_new[4:,:]=S.eye(14)
        F_new=smooth_new.row_join(normals_new)
        target=S.diag(1,A);target_inverse=S.diag(1,Ai)
        source=S.zeros(19);source[:14,5:]=Q;source[14:,:5]=S.eye(5)
        source_inverse=source.inv()
        assert target*target_inverse==S.eye(18)
        assert source*source_inverse==source_inverse*source==S.eye(19)
        assert target*F_old*source==F_new
        R=S.Matrix([[-p*b,p*a,n,-c,0],[m,0,0,0,a],[0,m,0,0,b],[0,0,0,m,n]])
        assert old['C']==str(R) and smooth_new[:4,:]==R
        minors=[str(S.factor(R[:,ii].det())) for ii in combinations(range(5),4)]
        assert old['maximal_minors']==minors
        count=nzero=0
        for mm in range(1,13):
            for nn in (-7,-2,-1,0,1,2,7):
                for aa,bb,cc in [(0,0,0),(1,0,0),(0,1,0),(0,0,1),(2,3,5),
                                 (3,6,2),(-2,4,3),(2,4,1),(1,1,4)]:
                    if gcd(mm,aa,bb,cc,nn)!=1:continue
                    count+=1;nzero+=int(nn==0)
        assert count==old['full_smith_cases'] and nzero==old['zero_cases']
        total+=count;zero+=nzero
        # The receiving local bases keep delta literally as their third column.
        for loc in new['local'].values():assert M(loc['H'])[:,2]==S.eye(4)[:,2]
        sec=new['section'];rel=M(sec['section_relation']);cob=M(sec['coboundary'])
        K,L=M(sec['relation_kernel']),M(sec['relation_kernel_inverse'])
        quotient,section=M(sec['quotient_map']),M(sec['quotient_section_local'])
        assert rel*K==S.zeros(2,3) and L*K==S.eye(3) and K*L*cob==cob
        assert quotient*cob==S.zeros(1,2) and quotient*section==S.ones(1,1)
        # Every relation/coboundary inclusion is primitive in the displayed bases.
        U,V=M(sec['coboundary_target_change']),M(sec['coboundary_source_change'])
        diag=U*L*cob*V
        assert diag==S.Matrix([[1,0],[0,1],[0,0]])
        assert abs(U.det())==abs(V.det())==1
        print('OS',old['entry'],': every historical field compared; exact 17-dimensional graph'
              ' isomorphism and 18x19 target/source maps hold symbolically for all m,n,a,b,c.')
        print('  Original local component residues',old['Q_components'],'; original sample counts',count,nzero)
        print('  Full peripheral identity D j5 = I - T5^-1 checked, including non-fixed columns.')
        records.append(dict(OS=old['entry'],reduced_source_map=Q,reduced_source_inverse=Qi,
                            graph_coordinate_map=A,graph_coordinate_inverse=Ai,
                            full_target=target,full_target_inverse=target_inverse,
                            full_source=source,full_source_inverse=source_inverse))
    assert (total,zero)==(2924,388)
    print('All',total,'historical parameter choices accounted for, including',zero,'with n=0.')
    print('The original script was read, not executed; no new independent credit is assigned to its samples.')
    (HERE/'S6_SERIES_PUBLISH_III_02KN_comparison_maps.json').write_text(json.dumps(serial(records),indent=2)+'\n',newline='\n')
    print('Every new coordinate map and its inverse saved; all symbolic comparisons passed.')
    print('Post-release comparison completed',datetime.now(timezone.utc).isoformat())


if __name__=='__main__':main()
