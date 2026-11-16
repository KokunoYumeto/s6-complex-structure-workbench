"""All translation weights with odd gcd(a,d), retaining the full fibre torsion.

Theorem D.2.40 uses the fibre-inversion splitting.  All original and
Mumford choices in the 495 initial patterns, every free finite-good log,
and arbitrary regular logs/clutch are allowed.  Original star caps only.
"""
from pathlib import Path
from math import gcd
import argparse,json
import sympy as s
import manifolds_weighted_profiles as W
from manifolds_rankone_families import decomp,ikernel,wedge,biv

ROOT=W.ROOT

def fibre_kernel(oldA,d,chern):
    if chern is not None and 'area_covector' in chern:
        annihilator=s.Matrix([chern['area_covector']])
    elif chern is not None and 'fibre_kernel' in chern:
        annihilator=ikernel(s.Matrix(chern['fibre_kernel']).T).T
    else:
        annihilator=ikernel((wedge(oldA)-s.eye(6)).T).T
    Sd=s.diag(1,1,1,d)
    return ikernel(annihilator*wedge(Sd))

def compute(pattern_index,d,finite=None,regular=None,e=0):
    p=W.PATTERNS[pattern_index];kk=W.key(p);row=W.MONO[kk];ini=W.INITIAL[kk]
    g=gcd(p['a'],d)
    if d<1 or g%2==0:raise ValueError('Require d>0 and gcd(a,d) odd.')
    finite={int(i):v for i,v in (finite or {}).items()}
    regular=list(regular or [])+[dict(m=1,v=[0,0,0,-int(e)])]
    offset=len(regular)
    A=[s.eye(4) for _ in regular]+[W.weighted(x['matrix'],d) for x in row['local']]
    D=s.Matrix.hstack(*[B-s.eye(4) for B in A[:-1]])
    K=ikernel(D);Ki=W.integral_left_inverse(K)
    Js=[]
    for i in range(len(A)):
        if i<len(A)-1:
            J=s.zeros(4*(len(A)-1),4);J[4*i:4*i+4,:]=s.eye(4)
        else:
            blocks=[]
            for j in range(len(A)-1):
                B=s.eye(4)
                for C in A[j+1:-1]:B=B*C
                blocks.append(-B)
            J=s.Matrix.vstack(*blocks)
        Js.append(Ki*J)
    relations=s.Matrix.hstack(*[wedge(B)-s.eye(6) for B in A])
    Cgroup=W.group(relations)
    assert Cgroup['free']==1
    assert all(set(s.factorint(x))<=set(s.factorint(g)) for x in Cgroup['torsion'])
    primitive=s.Matrix([[p['a']//g,0,0,0,0,-d*p['b']//g]])
    assert gcd(*map(int,list(primitive)))==1 and primitive*relations==s.zeros(1,relations.cols)
    columns=[relations[:,j].col_join(s.zeros(K.cols,1)) for j in range(relations.cols)]
    seifert=[];capdata=[];beta=L=0
    def normal(i,m,v,order):
        v=s.Matrix(v)
        N=(m//order)*sum((A[i]**j for j in range(order)),s.zeros(4))
        for lam in s.eye(4).columnspace():
            columns.append((-biv(lam,v)).col_join(Js[i]*N*lam))
        columns.append(s.zeros(6,1).col_join(Js[i]*v))
        seifert.append((m,int(v[3])))
    for i,log in enumerate(regular):
        m=int(log['m']);v=s.Matrix(log['v'])
        assert m>0 and gcd(m,*map(int,v))==1
        normal(i,m,v,1)
    additive=dict(p['additive_choices']);multiplicative=dict(p['multiplicative_choices'])
    for j,(loc,geom) in enumerate(zip(row['local'],ini['local'])):
        i=offset+j
        if j in p['finite_indices']:
            h=W.ORDER[loc['type']]
            data=finite.get(j) or W.default_finite(A[i],h)
            m=int(data['m']);v=s.Matrix(data['v'])
            if not W.finite_free(A[i],h,m,v):raise ValueError(f'Nonfree finite action at {j}.')
            normal(i,m,v,h)
            capdata.append(dict(site=j,kind='finite',m=m,v=list(map(int,v))))
            continue
        original=additive.get(j)=='original' or multiplicative.get(j)=='original'
        cc=W.CHERN.get((kk,j)) if original else None
        F=ikernel(A[i]-s.eye(4))
        for q in range(F.cols):columns.append(s.zeros(6,1).col_join(Js[i]*F[:,q]))
        F2=fibre_kernel(s.Matrix(loc['matrix']),d,cc)
        for q in range(F2.cols):columns.append(F2[:,q].col_join(s.zeros(K.cols,1)))
        if j==p['zero_index']:
            capdata.append(dict(site=j,kind='weighted_zero',components=d,fibre_kernel_rank=F2.cols))
            continue
        if cc is not None:
            L+=1;defect=cc.get('free_defect',len(geom['component_multiplicities'])-2);beta+=defect
            capdata.append(dict(site=j,kind='original_chern',defect=defect,fibre_kernel_rank=F2.cols))
        else:
            if loc['type'].startswith('I') and loc['type'][1:].isdigit():
                rho=gcd(d,int(loc['type'][1:])) if geom['P_component']==0 else 1
                SN,_,_,rank=decomp(A[i]-s.eye(4))
                assert rank==1 and abs(SN[0,0])==rho
            else:
                assert original;rho=W.orbit_count(geom['Q_pullback'],d)
            beta+=rho-1
            capdata.append(dict(site=j,kind='zero_degree',components=rho,defect=rho-1,
                                fibre_kernel_rank=F2.cols))
    B=s.Matrix.hstack(*columns);G=W.group(B)
    f=len(seifert);S=s.zeros(f+1)
    for i,(m,n) in enumerate(seifert):S[i,0]=-n;S[i,i+1]=m;S[-1,i+1]=1
    H1=W.group(S);r=H1['free']
    assert r in [0,1] and G['free']==(r if L==0 else 0)
    b2=d-1+beta+L+r+G['free'];b3=2+2*b2-2*r-2*d
    T=G['torsion'];A1=H1['torsion']
    homology=[dict(free=1,torsion=[]),H1,dict(free=b2,torsion=T),dict(free=b3,torsion=T),
              dict(free=b2,torsion=A1),dict(free=r,torsion=[]),dict(free=1,torsion=[])]
    assert b3>=0
    return dict(pattern_index=pattern_index,key=kk,weight=d,common_factor=g,e=e,
                regular_fibre_coinvariant=Cgroup,beta=beta,L=L,local=capdata,
                pi1_presentation='gamma central; c_i^m_i=gamma^n_i; product c_i=1',
                seifert_relations=seifert,H1_matrix=S.tolist(),H2_matrix=B.tolist(),homology=homology)

def elliptic_certificate():
    result=[]
    for row in W.MONO.values():
        B=s.Matrix.hstack(*[s.Matrix(v['matrix'])[:2,:2]-s.eye(2) for v in row['local']])
        assert W.group(B)==dict(free=0,torsion=[])
        result.append(dict(key=W.key(row),elliptic_common_matrix=B.tolist(),smith=[1,1]))
    (ROOT/'records/manifolds_elliptic_coinvariants.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
    return len(result)

def verify():
    ell=elliptic_certificate();checks=shared=comparisons=0;samples=[]
    for i,p in enumerate(W.PATTERNS):
        oddprimes=[int(q) for q in s.factorint(p['a']) if q!=2]
        weights=sorted(set([1]+oddprimes+([2] if p['a']%2 else [])))
        for d in weights:
            result=compute(i,d,e=(i%3)-1);checks+=1
            if gcd(p['a'],d)==1:
                previous=W.compute(i,d,e=(i%3)-1)
                assert result['homology']==previous['homology'];comparisons+=1
            else:
                shared+=1
                if i%13==0 or len(samples)<12:samples.append(result)
    print('Actual elliptic coinvariant unit certificates:',ell)
    print('Full fibre-and-graph Smith presentations:',checks,'shared odd factors:',shared)
    print('Independent agreement with the scalar-functional algorithm:',comparisons)
    (ROOT/'records/manifolds_odd_weighted_profiles.json').write_text(
        json.dumps(dict(scope=__doc__,elliptic_certificates=ell,checks=checks,shared_checks=shared,
                        overlap_comparisons=comparisons,samples=samples),indent=2,default=int)+'\n')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pattern',type=int)
    parser.add_argument('--weight',type=int,default=1)
    parser.add_argument('--e',type=int,default=0)
    parser.add_argument('--finite-json')
    parser.add_argument('--regular-json')
    args=parser.parse_args()
    if args.pattern is None:verify()
    else:
        finite=json.loads(Path(args.finite_json).read_text()) if args.finite_json else None
        regular=json.loads(Path(args.regular_json).read_text()) if args.regular_json else None
        print(json.dumps(compute(args.pattern,args.weight,finite,regular,args.e),indent=2,default=int))
