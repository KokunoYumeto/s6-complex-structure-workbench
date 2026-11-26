"""Fresh KX enumeration from raw marked matrices and component potentials.

No target original, earlier enumeration, or held root calculation is read.
Integer vertical solutions are constructed by rational component potentials
and exact orbit integration; no Smith-normal-form library is used.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
from functools import reduce
from itertools import product
import json
import re
import hashlib

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'agents/continuation7_iii_initial'
OUT.mkdir(parents=True,exist_ok=True)
RAW=ROOT/'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
inputs=json.loads(RAW.read_text())

def add(A,B): return [[a+b for a,b in zip(r,s)] for r,s in zip(A,B)]
def mul(A,B): return [[sum(a*b for a,b in zip(r,c)) for c in zip(*B)] for r in A]
def mv(A,v): return [sum(a*b for a,b in zip(r,v)) for r in A]
def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def sub(A,B): return [[a-b for a,b in zip(r,s)] for r,s in zip(A,B)]
def trans(A): return list(map(list,zip(*A)))
def det2(A): return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def egcd(a,b):
    if not b: return abs(a), (1 if a>=0 else -1), 0
    g,x,y=egcd(b,a%b)
    return g,y,x-(a//b)*y
def solve(A,b):
    """Exact Gauss-Jordan map; retained inverse is applied to b."""
    n=len(A)
    if not n:return []
    R=[list(map(F,A[i]))+list(map(F,eye(n)[i])) for i in range(n)]
    for j in range(n):
        p=next(k for k in range(j,n) if R[k][j])
        R[j],R[p]=R[p],R[j]
        v=R[j][j];R[j]=[x/v for x in R[j]]
        for k in range(n):
            if k!=j:
                v=R[k][j];R[k]=[x-v*y for x,y in zip(R[k],R[j])]
    inv=[r[n:] for r in R]
    assert mul(A,inv)==eye(n)==mul(inv,A)
    return mv(inv,b)
def fraction_json(x):
    if isinstance(x,F): return str(x)
    raise TypeError(type(x))

def cycle(n):
    C=[[0]*n for _ in range(n)]
    if n>1:
        for j in range(n):
            C[j][j]=-2
            C[j][(j-1)%n]+=1;C[j][(j+1)%n]+=1
    return dict(C=C,multiplicities=[1]*n,
                labels=[f'Theta_{j}' for j in range(n)],
                outer=list(range(n)),generator=[(j+1)%n for j in range(n)])

def tree(labels,edges,outer,generator):
    n=len(labels);C=[[-2*int(i==j) for j in range(n)] for i in range(n)]
    for i,j in edges:C[i][j]=C[j][i]=1
    # Normalize the unique affine null vector by the identity component.
    ms=[F(1)]+solve([r[1:] for r in C[1:]],[-r[0] for r in C[1:]])
    assert all(x.denominator==1 and x>0 for x in ms)
    ms=list(map(int,ms));assert mv(C,ms)==[0]*n
    return dict(C=C,multiplicities=ms,labels=labels,
                outer=outer,generator=generator)

def graph(kind):
    match=re.fullmatch(r'I(\d+)',kind)
    if match:return cycle(int(match[1]))
    if kind=='II':return cycle(1)
    if kind=='III':return cycle(2)
    if kind=='IV':return cycle(3)
    if kind=='IV*':
        # Three length-two arms; outer components in group order 0,1,2.
        labels=['O0','O1','O2','B0','B1','B2','C']
        edges=[(j,j+3) for j in range(3)]+[(j+3,6) for j in range(3)]
        return tree(labels,edges,[0,1,2],[1,2,0,4,5,3,6])
    if kind=='III*':
        # Long arms of length three and one short arm.
        labels=['O0','O1','A0','A1','B0','B1','C','S']
        edges=[(0,2),(2,4),(4,6),(1,3),(3,5),(5,6),(6,7)]
        return tree(labels,edges,[0,1],[1,0,3,2,5,4,6,7])
    match=re.fullmatch(r'I(\d+)\*',kind)
    if match:
        k=int(match[1]);assert k in (1,3)
        labels=['L0','R0','L1','R1']+[f'B{j}' for j in range(k+1)]
        edges=[(0,4),(2,4),(1,4+k),(3,4+k)]+[(4+j,5+j) for j in range(k)]
        gen=[1,2,3,0]+[4+k-j for j in range(k+1)]
        return tree(labels,edges,[0,1,2,3],gen)
    raise ValueError(kind)

def permutation_power(p,k):
    ans=list(range(len(p)))
    for _ in range(k):ans=[p[j] for j in ans]
    return ans
def pull(v,p):return [v[p[j]] for j in range(len(v))]
def diff(v,p):return [x-y for x,y in zip(v,pull(v,p))]
def orbits(p):
    seen=set();ans=[]
    for j in range(len(p)):
        if j in seen:continue
        orb=[];k=j
        while k not in seen:seen.add(k);orb.append(k);k=p[k]
        assert k==j;ans.append(orb)
    return ans
def potential(G,p):
    C=G['C'];outer=G['outer'];n=len(C)
    rhs=[int(j==outer[p])-int(j==0) for j in range(n)]
    z=[F(0)]+solve([r[1:] for r in C[1:]],rhs[1:])
    assert mv(C,z)==rhs
    return z,rhs

profiles=[]
for row in inputs['rows']:
    fibers=[];Ap=eye(2);gp=[0,0]
    d=F(row['height_of_generator']).denominator
    assert F(row['height_of_generator'])==F(1,d)
    for kind,A,g,mark in zip(row['fibers'],row['elliptic_matrices'],row['generator_section_cocycle'],row['component_coordinates']):
        assert det2(A)==1
        gp=[x+y for x,y in zip(gp,mv(Ap,g))];Ap=mul(Ap,A)
        G=graph(kind);C=G['C'];s=len(G['outer']);B=sub(A,eye(2))
        local=dict(kind=kind,A=A,g=g,**G)
        assert all(C[i][j]==C[G['generator'][i]][G['generator'][j]] for i in range(len(C)) for j in range(len(C)))
        assert pull(G['multiplicities'],G['generator'])==G['multiplicities']
        if re.fullmatch(r'I\d+',kind):
            n=int(kind[1:]);col=next(c for c in zip(*B) if any(c))
            gg=reduce(gcd,map(abs,col));u=[x//gg for x in col]
            if next(x for x in u if x)<0:u=[-x for x in u]
            _,x,y=egcd(*u);r=[-y,x]
            assert det2([[u[0],r[0]],[u[1],r[1]]])==1
            J=[[0,1],[-1,0]]
            assert B==[[n*x*y for y in mv(trans(J),u)] for x in u]
            j=next(i for i in range(2) if u[i]);kappa=F(g[j],u[j])
            assert kappa.denominator==1
            kappa=int(kappa);assert [kappa*x for x in u]==g
            cr=[r[1],-r[0]]
            assert sum(x*y for x,y in zip(cr,u))==1
            assert all(x%n==0 for x in mv(trans(B),cr))
            local.update(component_order=n,kappa=kappa,u=u,r=r,component_row=cr,component_inverse=u)
            if mark['moduli']:
                assert mark['moduli']==[n] and (kappa-mark['rows'][0][0])%n==0
        else:
            assert abs(det2(B))==s
            kappa=mark['rows'][0][0] if mark['moduli'] else 0
            assert s==1 or mark['moduli']==[s]
            rows=[list(h) for h in product(range(s),repeat=2)
                  if all(x%s==0 for x in mv(trans(B),h))
                  and sum(x*y for x,y in zip(h,g))%s==kappa%s
                  and gcd(s,*h)==1]
            if s==1: rows=[[0,0]]
            assert rows
            cr=rows[0]
            rv=next((list(v) for v in product(range(s),repeat=2)
                     if sum(x*y for x,y in zip(cr,v))%s==1%s),[0,0])
            local.update(component_order=s,kappa=kappa,component_row=cr,component_inverse=rv)
            inv_g=solve(B,g)
            order=1
            for x in inv_g:order=order*x.denominator//gcd(order,x.denominator)
            assert order==s
        # Full exact potentials and all graph-coordinate maps, before enumeration.
        local['potentials']=[potential(G,p)[0] for p in range(s)]
        fibers.append(local)
    assert Ap==eye(2) and gp==[0,0]
    profiles.append(dict(OS=row['OS'],profile=row['profile'],d=d,fibers=fibers))

enlarged=[];natural=[];counts=[]
for prof in profiles:
    total=nat=0;site_counts=[]
    for j,fib in enumerate(prof['fibers']):
        if not re.fullmatch(r'I\d+',fib['kind']):continue
        n=fib['component_order'];d=prof['d']
        assert d%n==0
        h=d//n
        assert gcd(n,h)==1 and (h*fib['kappa']**2-1)%n==0
        site_total=site_nat=0
        for a in range(1,h+1):
            if h%a:continue
            b=h//a;local_solutions=[];all_zero=True
            for i,f in enumerate(prof['fibers']):
                s=f['component_order'];p=(a*f['kappa'])%s;q=(b*f['kappa'])%s
                perm=permutation_power(f['generator'],q)
                z,m=potential(f,p)
                C=f['C'];N=len(C)
                dj=diff(m,perm)
                selected=i==j
                if selected:
                    assert gcd(q,s)==1 and (p*q-1)%s==0
                    W=[F(0)]*s
                    for k in range(1,s):W[(k*q)%s]=F(k,s)-1
                    V=[w-zz for w,zz in zip(W,z)]
                    target=[int(t==0) for t in range(N)]
                    assert diff(W,perm)==[F(t)-F(1,s) for t in target]
                else:
                    V=[F(0)]*N
                    for orb in orbits(perm):
                        for t in orb:V[t]=z[orb[0]]-z[t]
                    target=[0]*N
                    assert diff([x+y for x,y in zip(z,V)],perm)==[0]*N
                assert all(x.denominator==1 for x in V),(prof['OS'],prof['profile'],a,b,j,i,V)
                V=list(map(int,V))
                # Literal component equation and its inverse construction.
                assert [x+y for x,y in zip(dj,mv(C,diff(V,perm)))]==mv(C,target)
                # Every integral invariant is read off on one representative per orbit.
                obs=orbits(perm)
                basis=[[int(t in orb) for t in range(N)] for orb in obs]
                assert all(diff(v,perm)==[0]*N for v in basis)
                assert len(set(t for orb in obs for t in orb))==N
                all_zero=all_zero and not any(V)
                inverse_perm=permutation_power(f['generator'],(-q)%s)
                assert [perm[t] for t in inverse_perm]==list(range(N))
                local_solutions.append(dict(fiber_index=i+1,kind=f['kind'],p=p,q=q,
                  translation_Q_component_permutation=perm,
                  forward_linearization_component_permutation=inverse_perm,
                  degree_of_J=dj,potential=z,vertical_solution=V,
                  corrected_zero=target,invariant_basis=basis,
                  inverse_invariant_coordinates=[orb[0] for orb in obs]))
            # Separate direct natural-degree test, including every component h.
            natural_positions=[]
            for zero_component in range(n):
                ok=True
                for i,ls in enumerate(local_solutions):
                    C=prof['fibers'][i]['C'];target=[0]*len(C)
                    if i==j:target[zero_component]=1
                    ok=ok and ls['degree_of_J']==mv(C,target)
                if ok:natural_positions.append(zero_component)
            assert natural_positions in ([],[0]) and bool(natural_positions)==all_zero
            rec=dict(OS=prof['OS'],profile=prof['profile'],a=a,b=b,
              zero_fiber_index=j+1,zero_kind=fib['kind'],zero_component=0,
              local_solutions=local_solutions,natural=all_zero)
            enlarged.append(rec);total+=1;site_total+=1
            if all_zero:natural.append(rec);nat+=1;site_nat+=1
    # Every repeated I1 marker remains in the index.
        site_counts.append(dict(index=j+1,kind=fib['kind'],enlarged=site_total,natural=site_nat))
    counts.append(dict(OS=prof['OS'],profile=prof['profile'],natural=nat,enlarged=total,sites=site_counts))

keys=[(r['OS'],r['profile'],r['a'],r['b'],r['zero_fiber_index']) for r in enlarged]
assert len(set(keys))==len(keys)
assert (len(natural),len(enlarged))==(172,226)
data=dict(scope='Fresh derivation; only raw marked construction data read; no target original or held enumeration',
          input_sha256=hashlib.sha256(RAW.read_bytes()).hexdigest(),
          component_models=profiles,counts=counts,natural=natural,enlarged=enlarged)
(OUT/'S6_SERIES_PUBLISH_III_02KX_fresh_vertical_data.json').write_text(
    json.dumps(data,default=fraction_json,ensure_ascii=False,indent=2)+'\n')
print('INPUT_SHA256',data['input_sha256'])
print('METHOD exact rational component potentials; orbit integration; direct integer equation verification')
print('PROFILES',len(profiles))
for c in counts:
    print('COUNT',c['OS'],c['profile'],'natural',c['natural'],'enlarged',c['enlarged'],
          'sites',[(s['index'],s['kind'],s['natural'],s['enlarged']) for s in c['sites']])
print('TOTAL',len(natural),len(enlarged))
for num,r in enumerate(enlarged,1):
    print('ROW',num,r['OS'],r['profile'],f"({r['a']},{r['b']})",f"zero={r['zero_fiber_index']}:{r['zero_kind']}",
          'NATURAL' if r['natural'] else 'VERTICAL',
          'V='+repr([ls['vertical_solution'] for ls in r['local_solutions']]),
          'freedom='+repr([len(ls['invariant_basis']) for ls in r['local_solutions']]))
models={f['kind']:f for p in profiles for f in p['fibers']}
for kind,f in sorted(models.items()):
    print('MODEL',kind,'labels',f['labels'],'multiplicities',f['multiplicities'],
          'component_generator',f['generator'])
    for p,z in enumerate(f['potentials']):
        if p: print('POTENTIAL',kind,p,[str(x) for x in z])
nonzero={}
for r in enlarged:
    for ls in r['local_solutions']:
        if any(ls['vertical_solution']):
            k=(ls['kind'],ls['p'],ls['q'],bool(any(ls['corrected_zero'])))
            v=ls['vertical_solution']
            assert k not in nonzero or nonzero[k]==v
            nonzero[k]=v
for k,v in sorted(nonzero.items()):print('NONZERO_LOCAL',k,v)
natural_pairs={}
for r in natural:
    natural_pairs.setdefault((r['OS'],r['zero_kind']),set()).add((r['a'],r['b']))
for k,v in sorted(natural_pairs.items()):print('NATURAL_PAIRS',k,sorted(v))
print('PASS: all 226 integral vertical solutions, all 172 natural markers, every literal component equation and all orbit-coordinate inverse maps.')
