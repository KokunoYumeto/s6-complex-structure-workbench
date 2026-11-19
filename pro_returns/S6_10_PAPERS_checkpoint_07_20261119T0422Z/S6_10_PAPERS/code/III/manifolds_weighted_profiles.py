"""Translation iterates of all 172 natural initial rows.

Proved sector: P=aG, Q=d*b*G, gcd(a,d)=1; iterate the actual original
linearization, retain the same smooth periodic fans, allow every original
cap and every free finite-good additive log, and arbitrary regular logs.
Star caps are original in this theorem.  The data input identifies one
of the 495 homology-presentation patterns in original_multiplicative.json.
All matrices and Smith forms are exact; no bounded weight restriction.
"""
from pathlib import Path
from math import gcd
from itertools import product
import argparse
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form,hermite_normal_form
from manifolds_rankone_families import decomp,ikernel,wedge,biv

ROOT=Path(__file__).resolve().parent
key=lambda r:(r['entry'],r['profile'],r['a'],r['b'],r['zero_index'])
MONO={key(r):r for r in json.loads((ROOT/'manifolds_sphere_monodromies.json').read_text())['rows']}
INITIAL={key(r):r for r in json.loads((ROOT/'manifolds_sphere_initial.json').read_text())['candidates']}
PATTERNS=json.loads((ROOT/'manifolds_original_multiplicative.json').read_text())['patterns']
ADD=json.loads((ROOT/'manifolds_original_chern.json').read_text())['local']
MUL=json.loads((ROOT/'manifolds_original_multiplicative.json').read_text())['local']
CHERN={(key(r),r['site']):r for r in ADD+MUL}
ORDER={'II':6,'III':4,'III*':4,'IV':3,'IV*':3}

def group(M):
    D=smith_normal_form(M,domain=s.ZZ)
    v=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
    return dict(free=M.rows-len(v),torsion=[z for z in v if z>1])

def weighted(A,d):
    A=s.Matrix(A);A[:3,3]=d*A[:3,3]
    return A

def integral_left_inverse(K):
    D,U,V,r=decomp(K)
    assert r==K.cols and all(abs(D[i,i])==1 for i in range(r))
    return V*s.diag(*[1/D[i,i] for i in range(r)])*U[:r,:]

def orbit_count(P,d):
    Q=s.Matrix(P)**d;n=Q.rows
    perm=[next(i for i in range(n) if Q[i,j]) for j in range(n)]
    seen=set();count=0
    for i in range(n):
        if i in seen:continue
        count+=1;j=i
        while j not in seen:seen.add(j);j=perm[j]
    return count

def finite_lattice(A,order):
    F=ikernel(A-s.eye(4));assert F.cols==2
    N=sum((A**j for j in range(order)),s.zeros(4))
    Z=integral_left_inverse(F)*N
    assert all(v.q==1 for v in Z)
    H=hermite_normal_form(Z)
    assert H.shape==(2,2)
    return F,N,H

def finite_free(A,order,m,v):
    v=s.Matrix(v)
    if m<=0 or m%order or A*v!=v or gcd(m,*map(int,v))!=1:return False
    F,N,H=finite_lattice(A,order)
    z=integral_left_inverse(F)*v
    w=order*H.inv()*z
    assert all(x.q==1 for x in w)
    t=gcd(m,*map(int,w))
    return (m//t)%order==0

def default_finite(A,order,m=None):
    m=m or order;F,_,_=finite_lattice(A,order)
    for x,y in product(range(-3,4),repeat=2):
        v=F*s.Matrix([x,y])
        if finite_free(A,order,m,v):return dict(m=m,v=list(map(int,v)))
    raise AssertionError("No free power found in the small validation choices.")

def compute(pattern_index,d,finite=None,regular=None,e=0):
    p=PATTERNS[pattern_index];kk=key(p);row=MONO[kk];ini=INITIAL[kk]
    if d<1 or gcd(p['a'],d)!=1:
        raise ValueError("This theorem requires d>0 and gcd(a,d)=1.")
    finite={int(i):v for i,v in (finite or {}).items()}
    # An ordinary order-one clutch realizes the integer e with the D23 sign.
    regular=list(regular or [])+[dict(m=1,v=[0,0,0,-int(e)])]
    offset=len(regular)
    A=[s.eye(4) for _ in regular]+[weighted(x['matrix'],d) for x in row['local']]
    product_A=s.eye(4)
    for B in A:product_A=product_A*B
    assert product_A==s.eye(4)
    D=s.Matrix.hstack(*[B-s.eye(4) for B in A[:-1]])
    K=ikernel(D);Ki=integral_left_inverse(K)
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
    omega=s.Matrix([[p['a'],0,0,0,0,-d*p['b']]])
    assert gcd(*map(int,list(omega)))==1
    columns=[];seifert=[];capdata=[]
    beta=L=0
    def add_normal(i,m,v,order):
        v=s.Matrix(v)
        N=(m//order)*sum((A[i]**j for j in range(order)),s.zeros(4))
        for lam in s.eye(4).columnspace():
            cut=N*lam;assert A[i]*cut==cut
            columns.append(s.Matrix([-(omega*biv(lam,v))[0]]).col_join(Js[i]*cut))
        columns.append(s.Matrix([0]).col_join(Js[i]*v))
        seifert.append((m,int(v[3])))
    for i,log in enumerate(regular):
        m=int(log['m']);v=s.Matrix(log['v'])
        assert m>0 and gcd(m,*map(int,v))==1
        add_normal(i,m,v,1)
    additive=dict(p['additive_choices']);multiplicative=dict(p['multiplicative_choices'])
    for j,(loc,geom) in enumerate(zip(row['local'],ini['local'])):
        i=offset+j
        if j in p['finite_indices']:
            order=ORDER[loc['type']]
            data=finite.get(j) or default_finite(A[i],order)
            m=int(data['m']);v=s.Matrix(data['v'])
            if not finite_free(A[i],order,m,v):
                raise ValueError(f"Nonfree finite action at site {j}.")
            add_normal(i,m,v,order)
            capdata.append(dict(site=j,type=loc['type'],kind='finite',m=m,v=list(map(int,v))))
            continue
        F=ikernel(A[i]-s.eye(4))
        for q in range(F.cols):columns.append(s.Matrix([0]).col_join(Js[i]*F[:,q]))
        if j==p['zero_index']:
            capdata.append(dict(site=j,type=loc['type'],kind='weighted_zero',components=d))
            continue
        original=additive.get(j)=='original' or multiplicative.get(j)=='original'
        cc=CHERN.get((kk,j)) if original else None
        if cc is not None:
            h=d*cc['fibre_relation'];v=s.zeros(1+K.cols,1);v[0]=h;columns.append(v)
            L+=1
            defect=cc.get('free_defect',len(geom['component_multiplicities'])-2)
            beta+=defect
            capdata.append(dict(site=j,type=loc['type'],kind='original_chern',
                                components=len(geom['component_multiplicities']),defect=defect,fibre_relation=h))
        else:
            if loc['type'].startswith('I') and loc['type'][1:].isdigit():
                rho=gcd(d,int(loc['type'][1:])) if geom['P_component']==0 else 1
                kind='rank_one'
            else:
                assert original
                rho=orbit_count(geom['Q_pullback'],d);kind='original_zero_degree'
            beta+=rho-1
            capdata.append(dict(site=j,type=loc['type'],kind=kind,components=rho,defect=rho-1))
    B=s.Matrix.hstack(*columns);G=group(B)
    f=len(seifert);S=s.zeros(f+1)
    for i,(m,n) in enumerate(seifert):S[i,0]=-n;S[i,i+1]=m;S[-1,i+1]=1
    H1=group(S);r=H1['free']
    assert r in [0,1] and G['free']==(r if L==0 else 0)
    b2=d-1+beta+L+r+G['free'];b3=2+2*b2-2*r-2*d
    T=G['torsion'];A1=H1['torsion']
    H=[dict(free=1,torsion=[]),H1,dict(free=b2,torsion=T),dict(free=b3,torsion=T),
       dict(free=b2,torsion=A1),dict(free=r,torsion=[]),dict(free=1,torsion=[])]
    assert b3>=0 and sum((-1)**i*x['free'] for i,x in enumerate(H))==2*d
    return dict(pattern_index=pattern_index,key=kk,weight=d,e=e,initial_pair=[p['a'],d*p['b']],
                beta=beta,L=L,local=capdata,seifert_relations=seifert,
                pi1_presentation='gamma central; c_i^m_i=gamma^n_i; product c_i=1',
                H1_matrix=S.tolist(),H2_matrix=B.tolist(),homology=H)

def zero_certificates():
    records=[];rank_one_records=[]
    for row in MONO.values():
        A=[weighted(v['matrix'],0) for v in row['local']]
        gs=[]
        for q in [1,2]:
            R=s.Matrix.hstack(*[(B-s.eye(4)) if q==1 else (wedge(B)-s.eye(6)) for B in A])
            D=smith_normal_form(R,domain=s.ZZ)
            diag=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
            assert len(diag)==(3 if q==1 else 5)
            assert all(set(s.factorint(v))<=set(s.factorint(row['a'])) for v in diag)
            gs.append(diag)
        records.append(dict(key=key(row),smith_at_zero=gs))
        geom=INITIAL[key(row)]
        for j,loc in enumerate(row['local']):
            if j==row['zero_index'] or not (loc['type'].startswith('I') and loc['type'][1:].isdigit()):continue
            N=s.Matrix(loc['matrix'])-s.eye(4);DD,UU,VV,rr=decomp(N)
            assert rr==1 and abs(DD[0,0])==1
            alpha=UU.inv()[:,0];bb=DD[0,0]*VV.inv()[0,:]
            assert N==alpha*bb and gcd(*map(int,alpha))==gcd(*map(int,bb))==1
            q=gcd(*map(int,list(bb[:3])));c=int(bb[3])
            assert q>0 and gcd(q,c)==1
            pnarrow=geom['local'][j]['P_component']==0
            if pnarrow:assert q==int(loc['type'][1:])
            else:assert set(s.factorint(q))<=set(s.factorint(row['a']))
            rank_one_records.append(dict(key=key(row),site=j,type=loc['type'],P_narrow=pnarrow,
                                         alpha=list(map(int,alpha)),beta=list(map(int,bb)),
                                         vertical_content=q,gamma_coefficient=c))
    (ROOT/'manifolds_weighted_zero_certificates.json').write_text(json.dumps(records,indent=2)+'\n')
    (ROOT/'manifolds_weighted_rankone_certificates.json').write_text(
        json.dumps(rank_one_records,indent=2)+'\n')
    print('Actual rank-one factors:',len(rank_one_records),
          'non-narrow vertical contents:',sorted({r['vertical_content'] for r in rank_one_records if not r['P_narrow']}))
    return len(records)

def verify():
    n=zero_certificates();checks=positive=0;sample=[]
    for i,p in enumerate(PATTERNS):
        for d in [1,2,3,5]:
            if gcd(p['a'],d)>1:continue
            result=compute(i,d,e=(i%3)-1)
            checks+=1;positive+=d>1
            if d>1 and i%37==0:sample.append(result)
    print('All-row weight-zero prime-support certificates:',n)
    print('Weighted full graph presentations:',checks,'positive weights beyond one:',positive)
    (ROOT/'manifolds_weighted_profiles.json').write_text(
        json.dumps(dict(scope=__doc__,zero_certificates=n,checks=checks,positive_weight_checks=positive,
                        samples=sample),indent=2,default=int)+'\n')

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
