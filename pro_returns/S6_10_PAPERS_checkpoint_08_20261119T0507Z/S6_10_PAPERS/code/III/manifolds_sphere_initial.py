"""Conditional finite sphere initial data including vertical corrections.

Uses the separately proved Euler/two-homology reduction in the companion proof:
the effective linearization
is one reduced component of one I_n fibre, Q acts transitively there, and
<P,Q>=1/n. This program proves the remaining exact integral component
linear algebra for ALL such candidates; the geometric reduction is separate.
"""
from pathlib import Path
from fractions import Fraction
from math import gcd
import sys,json
import sympy as s
from manifolds_rankone_families import decomp,ikernel
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'explorer'))
import os_monodromy as om
profiles=json.loads((ROOT/'manifolds_os_configurations.json').read_text())

def permutation(images):
    n=len(images);P=s.zeros(n)
    for i,j in enumerate(images):P[j,i]=1
    return P

def geometry(kind):
    if kind in ['I1','II']:
        return s.zeros(1),[1],s.eye(1),[0]
    if kind in ['III','IV'] or (kind.startswith('I') and kind[1:].isdigit()):
        n={'III':2,'IV':3}.get(kind,int(kind[1:]) if kind[1:].isdigit() else 0)
        I=-2*s.eye(n)
        for j in range(n):
            I[j,(j+1)%n]+=1;I[(j+1)%n,j]+=1
        return I,[1]*n,permutation([(j+1)%n for j in range(n)]),list(range(n))
    if kind=='IV*':
        I=-2*s.eye(7)
        for j in range(3):I[j,j+3]=I[j+3,j]=1;I[j+3,6]=I[6,j+3]=1
        return I,[1,1,1,2,2,2,3],permutation([1,2,0,4,5,3,6]),[0,1,2]
    if kind=='III*':
        I=-2*s.eye(8)
        for i,j in [(0,2),(2,4),(4,6),(1,3),(3,5),(5,6),(6,7)]:I[i,j]=I[j,i]=1
        return I,[1,1,2,2,3,3,4,2],permutation([1,0,3,2,5,4,6,7]),[0,1]
    if kind.startswith('I') and kind.endswith('*'):
        n=int(kind[1:-1]);assert n%2==1
        I=-2*s.eye(n+5)
        for i,j in [(0,4),(1,4),(2,n+4),(3,n+4)]+[(j,j+1) for j in range(4,n+4)]:I[i,j]=I[j,i]=1
        images=[2,3,1,0]+[n+8-j for j in range(4,n+5)]
        return I,[1]*4+[2]*(n+1),permutation(images),[0,2,1,3]
    raise ValueError(kind)

def solve_integer(M,b):
    D,U,V,r=decomp(M);rhs=U*b;z=s.zeros(M.cols,1)
    for i in range(M.rows):
        if i<r:
            if rhs[i]%D[i,i]:return None
            z[i]=rhs[i]/D[i,i]
        elif rhs[i]:return None
    x=V*z;assert M*x==b
    return x

candidates=[];accepted=[];surface_rank=[]
for profile in profiles:
    en,pr=profile['os_entry'],profile['profile']
    info=om.os_info(en,profile=pr,verbose=False)
    d=Fraction(info['height_matrix'][0][0]).denominator
    kinds=list(info['kodaira_types']);F=sum(not(k.startswith('I') and k[1:].isdigit()) for k in kinds)
    L=len(kinds)-F;assert 2*F+L==5
    # Constant non-split line-extension check; higher P scales the delta row.
    weights=[0]*len(kinds);weights[next(i for i,k in enumerate(kinds) if k.startswith('I') and k[1:].isdigit())]=1
    mats=[s.Matrix(x) for x in om.monodromy_tuple(en,(1,),(d,),tuple(weights),profile=pr,verbose=False)]
    fixedpart=s.Matrix.hstack(*[(x-s.eye(4))[:3,:3] for x in mats])
    assert fixedpart.rank()==3
    surface_rank.append(dict(entry=en,profile=pr,additive=F,multiplicative=L,line_extension_rank=3))
    geoms=[]
    for kind,comp in zip(kinds,info['component_maps']):
        I,m,pi,labels=geometry(kind)
        assert I*s.Matrix(m)==s.zeros(len(m),1)
        assert pi.T*I*pi==I
        assert I.rank()==len(m)-1
        res=int(comp['rows'][0][0]) if comp['rows'] else 0
        mod=int(comp['moduli'][0]) if comp['moduli'] else 1
        assert mod==len(labels)
        geoms.append((I,m,pi,labels,res,mod))
    for site,kind in enumerate(kinds):
        if not(kind.startswith('I') and kind[1:].isdigit()):continue
        n=int(kind[1:])
        if d%n:continue
        product=d//n
        for a in range(1,product+1):
            if product%a:continue
            b=product//a
            if gcd(b*geoms[site][4],n)!=1:continue
            local=[];okay=True
            for j,(I,m,pi,labels,res,mod) in enumerate(geoms):
                p=(a*res)%mod;q=(b*res)%mod
                T=(pi**q).T
                cp=s.eye(I.rows)[:,labels[p]]-s.eye(I.rows)[:,0]
                target=s.eye(I.rows)[:,0] if j==site else s.zeros(I.rows,1)
                E=(s.eye(I.rows)-T)*I
                rhs=I*target-(s.eye(I.rows)-T)*cp
                V=solve_integer(E,rhs)
                # Kernel is exactly the invariant vertical-divisor lattice:
                # if (1-T)IV=0, IV invariant; I is invertible mod its fixed fibre.
                assert E.rank()==(s.eye(I.rows)-T).rank()
                rho=len(s.eye(I.rows).columnspace())- (s.eye(I.rows)-T).rank()
                if V is None:okay=False
                local.append(dict(type=kinds[j],P_component=p,Q_component=q,
                    component_intersection=I.tolist(),component_multiplicities=m,
                    Q_pullback=T.tolist(),P_degree_vector=cp.tolist(),target_divisor=target.tolist(),
                    equation=E.tolist(),rhs=rhs.tolist(),vertical_correction=None if V is None else V.tolist(),
                    invariant_vertical_basis=ikernel(s.eye(I.rows)-T).tolist(),component_orbits=rho))
            rec=dict(entry=en,profile=pr,n=n,a=a,b=b,mixed_height=f'1/{n}',zero_index=site,
                     zero_type=kind,solvable=okay,local=local)
            candidates.append(rec)
            if okay:accepted.append(rec)
print('all proposed sphere section/component candidates',len(candidates),'integer-solvable',len(accepted))
for pr in surface_rank:
    rows=[x for x in accepted if x['entry']==pr['entry'] and x['profile']==pr['profile']]
    print(pr['entry'],pr['profile'],[(x['zero_type'],x['a'],x['b']) for x in rows])
record=dict(scope=__doc__,rank_certificates=surface_rank,
    number_candidates=len(candidates),number_integrally_solvable=len(accepted),candidates=candidates)
(ROOT/'manifolds_sphere_initial.json').write_text(json.dumps(record,indent=2,default=int)+'\n')

# Natural section-line sector: require V=0 and retain every marked component.
natural=[]
for c in candidates:
    okay=True;zero_components=[]
    for j,v in enumerate(c['local']):
        I=s.Matrix(v['component_intersection']);T=s.Matrix(v['Q_pullback'])
        cp=s.Matrix(v['P_degree_vector']);rhs=(s.eye(I.rows)-T)*cp
        if j==c['zero_index']:
            zero_components=[i for i in range(I.rows) if rhs==I[:,i]]
            if not zero_components:okay=False
        elif rhs!=s.zeros(I.rows,1):okay=False
    if okay:
        rec={k:c[k] for k in ['entry','profile','n','a','b','zero_index','zero_type']}
        rec['zero_components']=zero_components
        if c['n']>1:
            z=c['local'][c['zero_index']]
            assert zero_components==[0]
            assert z['P_component']==z['Q_component']
            assert z['P_component'] in [1,c['n']-1]
        natural.append(rec)
assert len(candidates)==226 and len(accepted)==226 and len(natural)==172
print('Natural uncorrected section-line candidates:',len(natural))
for pr in surface_rank:
    nc=sum(x['entry']==pr['entry'] and x['profile']==pr['profile'] for x in natural)
    bc=sum(x['entry']==pr['entry'] and x['profile']==pr['profile'] for x in candidates)
    print('profile count',pr['entry'],pr['profile'],'natural',nc,'corrected',bc)
(ROOT/'manifolds_sphere_natural.json').write_text(json.dumps(
    dict(scope='Exact natural M=O(P-O) component criterion; geometric reduction is in the companion proof, not inferred from these finite calculations.',
         count=len(natural),candidates=natural),indent=2)+'\n')

# Universal alternating-form identity; central extension is unrestricted.
aa,bb,cc,x,y=s.symbols('a b c x y')
p11,p12,p21,p22=s.symbols('p11 p12 p21 p22')
B=s.Matrix([[p11,p12],[p21,p22]]);J=s.Matrix([[0,1],[-1,0]]);z=s.Matrix([x,y])
A=s.eye(4);A[:2,:2]=B;A[:2,3]=bb*z;A[2,:2]=-aa*z.T*J*B;A[2,3]=cc
Omega=s.diag(aa*J,s.Matrix([[0,-bb],[bb,0]]))
D=A.T*Omega*A-Omega
ideal=s.groebner([p11*p22-p12*p21-1],p11,p12,p21,p22,x,y,aa,bb,cc)
for item in D:
    assert ideal.reduce(s.expand(item))[1]==0
print('Universal alternating form identity verified modulo det(B)=1')
