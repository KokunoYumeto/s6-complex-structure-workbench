"""All positive translation weights, with complete integral bar-chain corrections.

Theorem D.2.41 removes the common-factor restriction in D.2.37/40.
All original and Mumford choices in the 495 natural initial patterns,
every free finite-good log and arbitrary regular logs/clutch are allowed.
Star caps remain original.  Full integral fibre torsion is retained.
"""
from pathlib import Path
from math import gcd
import argparse,json
import sympy as s
import manifolds_weighted_profiles as W
import manifolds_odd_weighted_profiles as O
from manifolds_rankone_families import decomp,ikernel,wedge,biv,PAIRS
ROOT=W.ROOT
fibre_kernel=O.fibre_kernel

def p2(u,v):
    u=s.Matrix(u);v=s.Matrix(v)
    return s.Matrix([u[i]*v[j] for i,j in PAIRS])

class QuadraticCorrection:
    def __init__(self,A):
        self.A=s.Matrix(A);WA=wedge(self.A);self.WA=WA;E=s.eye(4)
        self.D=[[p2(self.A*E[:,i],self.A*E[:,j])-WA*p2(E[:,i],E[:,j])
                 for j in range(4)] for i in range(4)]
        assert all(self.D[i][j]==self.D[j][i] for i in range(4) for j in range(4))
    def __call__(self,u):
        u=s.Matrix(u)
        result=-sum((self.D[i][i]*(u[i]*(u[i]-1)/2) for i in range(4)),s.zeros(6,1))
        result-=sum((self.D[i][j]*u[i]*u[j] for i in range(4) for j in range(i+1,4)),s.zeros(6,1))
        assert all(x.q==1 for x in result)
        return result
    def coefficients(self):
        return dict(diagonal=[self.D[i][i].T.tolist()[0] for i in range(4)],
                    mixed=[self.D[i][j].T.tolist()[0] for i in range(4) for j in range(i+1,4)])
    def check(self,u,v):
        u=s.Matrix(u);v=s.Matrix(v)
        assert self(u)+self(v)-self(u+v)==p2(self.A*u,self.A*v)-self.WA*p2(u,v)

def compute(pattern_index,d,finite=None,regular=None,e=0):
    p=W.PATTERNS[pattern_index];kk=W.key(p);row=W.MONO[kk];ini=W.INITIAL[kk]
    g=gcd(p['a'],d)
    if d<1:raise ValueError('Require d>0.')
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
    # Strict bar-chain peripheral comparison, including the reversed last word.
    cocycles=[QuadraticCorrection(B) for B in A[:-1]]
    suffix=[]
    for j in range(len(A)-1):
        B=s.eye(4)
        for C in A[j+1:-1]:B=B*C
        suffix.append(B)
    def sweep(i,v):
        v=s.Matrix(v)
        if i<len(A)-1:return cocycles[i](v)
        # A[last]v is required for a general local one-chain; for fixed
        # vectors it equals v. Keep it here to transport full norm chains.
        return -sum((cocycles[j](suffix[j]*A[i]*v) for j in range(len(A)-1)),s.zeros(6,1))
    seifert=[];capdata=[];beta=L=0
    def normal(i,m,v,order):
        v=s.Matrix(v)
        N=(m//order)*sum((A[i]**j for j in range(order)),s.zeros(4))
        for lam in s.eye(4).columnspace():
            correction=(m//order)*sum((sweep(i,A[i]**j*lam) for j in range(order)),s.zeros(6,1))
            columns.append((correction-biv(lam,v)).col_join(Js[i]*N*lam))
        columns.append(sweep(i,v).col_join(Js[i]*v))
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
        for q in range(F.cols):columns.append(sweep(i,F[:,q]).col_join(Js[i]*F[:,q]))
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
                bar_corrections=[Q.coefficients() for Q in cocycles],
                pi1_presentation='gamma central; c_i^m_i=gamma^n_i; product c_i=1',
                seifert_relations=seifert,H1_matrix=S.tolist(),H2_matrix=B.tolist(),homology=homology)

def verify():
    checks=overlap=even=0;samples=[];chainchecks=0
    vectors=[s.Matrix(v) for v in [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],
                                  [1,-2,3,-1],[-2,1,-1,2],[2,2,-3,-2]]]
    for row in W.MONO.values():
        for loc in row['local']:
            for d in [1,2,6]:
                Q=QuadraticCorrection(W.weighted(loc['matrix'],d))
                for u,v in [(vectors[0],vectors[1]),(vectors[4],vectors[5]),(vectors[5],vectors[6])]:
                    Q.check(u,v);chainchecks+=1
    # Literal bar chains, not merely their abelianized vectors.
    from collections import Counter
    wordchecks=0
    for row in W.MONO.values():
        for d in [1,2,6]:
            matrices=[W.weighted(loc['matrix'],d) for loc in row['local']]
            for u in vectors[4:]:
                residual=Counter()
                for j,A in enumerate(matrices[:-1]):
                    B=s.eye(4)
                    for C in matrices[j+1:-1]:B=B*C
                    v=B*matrices[-1]*u
                    residual[tuple(A*v)]-=1;residual[tuple(v)]+=1
                residual[tuple(matrices[-1]*u)]-=1;residual[tuple(u)]+=1
                assert all(x==0 for x in residual.values())
                wordchecks+=1
    print('Integral quadratic identities:',chainchecks,'literal reversed-word identities:',wordchecks,flush=True)
    for i,p in enumerate(W.PATTERNS):
        weights=sorted(set([1,2,3,p['a'],2*p['a']]))
        for d in weights:
            result=compute(i,d,e=(i%3)-1);checks+=1
            if gcd(p['a'],d)%2:
                previous=O.compute(i,d,e=(i%3)-1)
                assert result['homology']==previous['homology'],(i,d,result['homology'],previous['homology'])
                overlap+=1
            else:
                even+=1
                if len(samples)<24 or i%37==0:samples.append(result)
    print('Integral quadratic bar-chain identities:',chainchecks)
    print('Full corrected presentations:',checks,'shared even-factor cases:',even)
    print('Independent comparisons with proved odd-factor method:',overlap)
    (ROOT/'records/manifolds_all_weighted_profiles.json').write_text(
        json.dumps(dict(scope=__doc__,chainchecks=chainchecks,wordchecks=wordchecks,checks=checks,even_checks=even,
                        overlap_comparisons=overlap,samples=samples),indent=2,default=int)+'\n')

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
