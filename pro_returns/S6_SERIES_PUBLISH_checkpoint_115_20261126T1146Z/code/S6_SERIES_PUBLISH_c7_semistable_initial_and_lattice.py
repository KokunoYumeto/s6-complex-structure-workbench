#!/usr/bin/env python3
"""Fresh semistable input enumeration and integral lattice certificates.

Only the four construction-only raw profiles are read. No historical target
program, original L0 proof, or held root candidate calculation is imported.
Component degrees are compared as literal vectors on the cyclic multigraph.
Integer Smith reduction below retains its actual elementary inverse maps.
"""
from __future__ import annotations
from fractions import Fraction
from functools import reduce
from itertools import combinations
from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / 'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'

def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def zeros(m, n):
    return [[0] * n for _ in range(m)]

def transpose(a):
    return [list(c) for c in zip(*a)]

def mul(a, b):
    assert len(a[0]) == len(b)
    out = zeros(len(a), len(b[0]))
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    out[i][j] += x*y
    return out

def add(a, b, sign=1):
    return [[x + sign*y for x,y in zip(ar,br)] for ar,br in zip(a,b)]

def hstack(*args):
    assert len({len(a) for a in args}) == 1
    return [sum((list(a[i]) for a in args),[]) for i in range(len(args[0]))]

def cols(a, ids):
    return [[row[j] for j in ids] for row in a]

def diag_entries(a):
    return [a[i][i] for i in range(min(len(a),len(a[0]))) if a[i][i]]

def egcd(a, b):
    oldr,r,olds,s,oldt,t = a,b,1,0,0,1
    while r:
        q = oldr//r
        oldr,r = r,oldr-q*r
        olds,s = s,olds-q*s
        oldt,t = t,oldt-q*t
    if oldr < 0:
        oldr,olds,oldt = -oldr,-olds,-oldt
    assert olds*a+oldt*b == oldr
    return oldr,olds,oldt

def smith(a):
    """Return D,U,V with D=U A V; each operation is unimodular."""
    original = [row[:] for row in a]
    a = [row[:] for row in a]
    m,n = len(a),len(a[0])
    u,v = eye(m),eye(n)

    def rswap(i,j):
        a[i],a[j] = a[j],a[i]
        u[i],u[j] = u[j],u[i]

    def radd(i,j,q):
        a[i] = [x+q*y for x,y in zip(a[i],a[j])]
        u[i] = [x+q*y for x,y in zip(u[i],u[j])]

    def cswap(i,j):
        for mat in (a,v):
            for row in mat:
                row[i],row[j] = row[j],row[i]

    def cadd(i,j,q):
        for mat in (a,v):
            for row in mat:
                row[i] += q*row[j]

    for k in range(min(m,n)):
        nonzero = [(abs(a[i][j]),i,j) for i in range(k,m)
                   for j in range(k,n) if a[i][j]]
        if not nonzero:
            break
        _,i,j = min(nonzero)
        rswap(k,i); cswap(k,j)
        while True:
            changed = True
            while changed:
                changed = False
                for i in range(k+1,m):
                    if a[i][k]:
                        q = a[i][k]//a[k][k]
                        radd(i,k,-q)
                        if a[i][k]:
                            rswap(i,k)
                        changed = True
                        break
                if changed:
                    continue
                for j in range(k+1,n):
                    if a[k][j]:
                        q = a[k][j]//a[k][k]
                        cadd(j,k,-q)
                        if a[k][j]:
                            cswap(j,k)
                        changed = True
                        break
            bad = next(((i,j) for i in range(k+1,m) for j in range(k+1,n)
                        if a[i][j] % a[k][k]), None)
            if bad is None:
                break
            radd(k,bad[0],1)
        if a[k][k] < 0:
            a[k] = [-x for x in a[k]]
            u[k] = [-x for x in u[k]]
    ds = diag_entries(a)
    assert all(y % x == 0 for x,y in zip(ds,ds[1:]))
    assert all(a[i][j] == 0 for i in range(m) for j in range(n) if i != j)
    assert mul(mul(u,original),v) == a
    return a,u,v

def primitive_direction(mat):
    for col in transpose(mat):
        d = reduce(gcd,col,0)
        if d:
            out = [x//d for x in col]
            if next(x for x in out if x) < 0:
                out = [-x for x in out]
            return out
    raise AssertionError('zero matrix')

def factor_local(row, i):
    nu = int(row['fibers'][i][1:])
    a = row['elliptic_matrices'][i]
    g = row['generator_section_cocycle'][i]
    u = primitive_direction(add(a,eye(2),-1))
    ju = [-u[1],u[0]]
    assert add(a,eye(2),-1) == [[nu*x*y for y in ju] for x in u]
    index = next(j for j,x in enumerate(u) if x)
    assert g[index] % u[index] == 0
    kappa = g[index]//u[index]
    assert g == [kappa*x for x in u]
    d,s,t = egcd(u[0],u[1])
    assert d == 1
    r = [-t,s]
    assert u[0]*r[1]-u[1]*r[0] == 1
    return nu,u,kappa,r

def component_degrees(n,p,q):
    out = [0]*n
    for j,c in ((p,1),(0,-1),(p-q,-1),(-q,1)):
        out[j%n] += c
    return out

def component_column(n,h):
    out = [0]*n
    for j,c in ((h,-2),(h-1,1),(h+1,1)):
        out[j%n] += c
    return out

PAIRS = tuple(combinations(range(4),2))
def wedge2(t):
    return [[t[i][k]*t[j][l]-t[i][l]*t[j][k]
             for k,l in PAIRS] for i,j in PAIRS]

def periods(row, a, b, zero):
    out = []
    for i,A in enumerate(row['elliptic_matrices']):
        nu,u,kappa,r = factor_local(row,i)
        t = eye(4)
        for p in range(2):
            for q in range(2):
                t[p][q] = A[p][q]
            t[p][3] = b*kappa*u[p]
        t[2][0],t[2][1] = a*kappa*u[1],-a*kappa*u[0]
        central = Fraction(int(i==zero)-a*b*kappa*kappa,nu)
        assert central.denominator == 1
        t[2][3] = central.numerator
        out.append(t)
    product = eye(4)
    for t in out:
        product = mul(product,t)
    assert product == eye(4)
    omega = [[0,a,0,0],[-a,0,0,0],[0,0,0,-b],[0,0,b,0]]
    assert all(mul(mul(transpose(t),omega),t)==omega for t in out)
    return out

def insertion(i, x):
    out = zeros(20,len(x[0]))
    for j in range(4):
        out[4*i+j] = x[j][:]
    return out

def certificate(row,a,b,zero,ts):
    ns = [add(t,eye(4),-1) for t in ts]
    fixed = []
    for i,N in enumerate(ns):
        d,u,v = smith(N)
        ds = diag_entries(d)
        assert ds == [1]*(2 if i==zero else 1)
        fixed.append(cols(v,range(len(ds),4)))
    D = hstack(zeros(4,4),*ns[:4])
    D0 = D[:3]
    diag,ud,vd = smith(D0)
    assert diag_entries(diag)==[1,1,1]
    C0 = mul(cols(vd,range(3)),ud)
    assert mul(D0,C0)==eye(3)
    jlast = []
    for i in range(5):
        tail=eye(4)
        for t in ts[i:4]:
            tail=mul(tail,t)
        jlast.extend([[-x for x in r] for r in tail])
    blocks=[insertion(i+1,fixed[i]) for i in range(4)]
    blocks.append(mul(jlast,fixed[4]))
    B=hstack(*blocks)
    j0free=insertion(0,cols(eye(4),(0,1,3)))
    K=hstack(B,j0free)
    assert len(K[0])==17 and mul(D,K)==zeros(4,17)
    diag,uk,vk=smith(K)
    assert diag_entries(diag)==[1]*17
    L=mul(vk,uk[:17])
    assert mul(L,K)==eye(17)
    projector=add(eye(20),mul(C0,D0),-1)
    assert mul(mul(K,L),projector)==projector
    j0delta=insertion(0,cols(eye(4),(2,)))
    assert [r[0] for r in mul(L,j0delta)[14:]]==[0,0,0]

    # Complete fibre degree-two coinvariants, including an integral inverse.
    B2=hstack(zeros(6,6),*[add(wedge2(t),eye(6),-1) for t in ts[:4]])
    w=[[a,0,0,0,0,-b]]
    assert mul(w,B2)==zeros(1,30)
    d,x,y=egcd(a,b)
    assert d==1
    s=[[x],[0],[0],[0],[0],[-y]]
    F=[[b,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],
       [0,0,0,1,0],[0,0,0,0,1],[a,0,0,0,0]]
    assert mul(w,s)==[[1]] and mul(w,F)==zeros(1,5)
    diag,u2,v2=smith(B2)
    assert diag_entries(diag)==[1]*5
    transformed=mul(u2,F)
    assert transformed[5]==[0]*5
    Z=mul(cols(v2,range(5)),transformed[:5])
    assert mul(B2,Z)==F

    # The single cusp's transported discs already span all of ker(chi).
    nu,u,kappa,r=factor_local(row,zero)
    c=(1-a*b*kappa*kappa)//nu
    H=transpose([[u[0],u[1],0,0],
                 [c*r[0],c*r[1],0,a*kappa],
                 [0,0,1,0],[-b*kappa*r[0],-b*kappa*r[1],0,nu]])
    standard=eye(4);standard[0][1]=1;standard[2][3]=1
    assert mul(ts[zero],H)==mul(H,standard)
    dh,uh,vh=smith(H)
    assert diag_entries(dh)==[1]*4
    short=cols(H,(0,2))
    transported=hstack(short,*[mul(t,short) for t in ts])
    assert transported[3]==[0]*len(transported[0])
    dc,uc,vc=smith(transported[:3])
    assert diag_entries(dc)==[1]*3
    cusp_inverse=mul(cols(vc,range(3)),uc)
    assert mul(transported[:3],cusp_inverse)==eye(3)
    data = {'periods':ts,'fixed_bases':fixed,'D':D,'D0_right_inverse':C0,
            'K':K,'K_left_inverse':L,'fibre_boundary':B2,
            'fibre_kernel_basis':F,'fibre_boundary_preimages':Z,
            'fibre_generator':s,'physical_cusp_basis':H,
            'transported_cusp_discs':transported,
            'cusp_disc_right_inverse':cusp_inverse}
    return tuple(tuple(x) for x in H),len(B[0]),data

def fan_slopes(c):
    p=(c[0][0],c[1][0]);q=(c[0][1],c[1][1])
    def unoriented(v):
        assert reduce(gcd,v,0)==1
        return v if next(x for x in v if x)>0 else tuple(-x for x in v)
    return {unoriented(p),unoriented(q),unoriented((q[0]-p[0],q[1]-p[1]))}

def farey_word(initial):
    """Actual periodic fans, not a relabelling: every edge move is checked."""
    c=[row[:] for row in initial]
    word=[]
    def step(op,new,flip=True):
        nonlocal c
        assert c[0][0]*c[1][1]-c[0][1]*c[1][0]==1
        assert new[0][0]*new[1][1]-new[0][1]*new[1][0]==1
        old_edges,new_edges=fan_slopes(c),fan_slopes(new)
        if flip:
            assert len(old_edges&new_edges)==2
            assert len(old_edges-new_edges)==len(new_edges-old_edges)==1
        else:
            assert old_edges==new_edges
        word.append({'operation':op,'before':c,'after':new,'flip':flip,
                     'removed':sorted(old_edges-new_edges),
                     'inserted':sorted(new_edges-old_edges)})
        c=new
    while c[0][1]:
        quotient=c[0][0]//c[0][1]
        for _ in range(abs(quotient)):
            sign=-1 if quotient>0 else 1
            step(f'p += {sign} q',[[row[0]+sign*row[1],row[1]] for row in c])
        old_second=abs(c[0][1])
        step('(p,q) -> (q,-p)',[[row[1],-row[0]] for row in c])
        assert abs(c[0][1])<old_second
    assert abs(c[0][0])==1
    if c[0][0]<0:
        step('(p,q) -> (-p,-q)',[[-x for x in row] for row in c],False)
    assert c[0][0]==c[1][1]==1 and c[0][1]==0
    lower=c[1][0]
    for _ in range(abs(lower)):
        sign=-1 if lower>0 else 1
        step(f'p += {sign} q',[[row[0]+sign*row[1],row[1]] for row in c])
    assert c==eye(2)
    return word

profiles=json.loads(RAW.read_text())['rows']
profiles=[r for r in profiles if r['OS'] in (45,47,55,56)
          and r['profile']=='default']
assert [r['OS'] for r in profiles]==[45,47,55,56]
rows=[]
certificates=[]
print('Fresh direct cyclic-component enumeration and full integral lattice certificates')
print('Input: four construction-only profiles; no historical target algorithm imported.')
for profile in profiles:
    d=Fraction(profile['height_of_generator']).denominator
    assert Fraction(profile['height_of_generator'])==Fraction(1,d)
    factors=[factor_local(profile,i) for i in range(5)]
    before=len(rows)
    for zero,(nu,_,_,_) in enumerate(factors):
        if d%nu:
            continue
        height_product=d//nu
        for a in range(1,height_product+1):
            if height_product%a:
                continue
            b=height_product//a
            degrees=[component_degrees(n,a*k,b*k) for n,u,k,r in factors]
            if any(any(degrees[i]) for i in range(5) if i!=zero):
                continue
            kappa=factors[zero][2]
            if gcd(nu,b*kappa)!=1:
                continue
            hits=[h for h in range(nu) if degrees[zero]==component_column(nu,h)]
            for h in hits:
                assert h==0 and gcd(a,b)==1
                ts=periods(profile,a,b,zero)
                H,normal_count,data=certificate(profile,a,b,zero,ts)
                assert normal_count==14
                nu,u,kappa,r=factors[zero]
                C=[[nu,b*kappa],[-a*kappa,(1-a*b*kappa*kappa)//nu]]
                word=farey_word(C)
                data.update({'OS':profile['OS'],'zero_position':zero+1,
                             'a':a,'b':b,'source_short_matrix':C,
                             'actual_fan_word':word})
                certificates.append(data)
                rows.append((profile['OS'],zero+1,nu,a,b))
                print(f'OS{profile["OS"]} zero={zero+1}:I{nu} a={a} b={b}; '
                      'component/period/inverse/graph/fibre/cusp-span PASS; '
                      f'actual fan flips={sum(x["flip"] for x in word)}')
    print(f'OS{profile["OS"]} natural rows = {len(rows)-before}')
assert len(rows)==62
assert len(set(rows))==62
b_one=[r for r in rows if r[-1]==1]
assert len(b_one)==17
print('TOTAL NATURAL ROWS:',len(rows),'DISTINCT:',len(set(rows)))
print('B=1 ROWS:',b_one)
print('For every row: gcd(a,b)=1; all periods integral, product identity and preserved omega.')
print('Local N Smith ranks: four primitive rank-one nodes and one primitive rank-two cusp.')
print('D0 right inverse, K/L graph inverse, B2/Z fibre inverse and cusp-disc spanning inverse: PASS.')
print('These are marked algebraic certificates; geometric attachment and fan transport are proved separately.')

def omega_pair(a,b,u,v):
    return a*(u[0]*v[1]-u[1]*v[0])+b*(u[3]*v[2]-u[2]*v[3])

def presentation(a,b,sites,e):
    s=len(sites)
    rel=zeros(1+4*s,5*s+1)
    for i,(m,v) in enumerate(sites):
        assert m>0 and reduce(gcd,[m,*v],0)==1
        for j in range(4):
            u=eye(4)[j]
            rel[0][5*i+j]=-omega_pair(a,b,u,v)
            rel[1+4*i+j][5*i+j]=m
            rel[1+4*i+j][5*i+4]=v[j]
        rel[1+4*i+2][-1]=1
    rel[0][-1]=b*e
    return rel

def seifert(sites,e):
    s=len(sites)
    out=zeros(s+1,s+1)
    for i,(m,v) in enumerate(sites):
        out[0][i]=-v[3]
        out[i+1][i]=m
        out[i+1][-1]=1
    out[0][-1]=-e
    return out

def simply_connected(sites,e):
    remaining=[]
    for m,v in sites:
        if m==1:
            e-=v[3]
        else:
            remaining.append((m,v[3]))
    if not remaining:
        return abs(e)==1
    if len(remaining)==1:
        m,n=remaining[0]
        return abs(m*e-n)==1
    if len(remaining)==2:
        (m,n),(q,k)=remaining
        return abs(q*n+m*k-e*m*q)==1
    return False

def belongs(rel, red, vectors):
    d,u,v=red
    diag=diag_entries(d)
    z=mul(u,vectors)
    coordinates=zeros(len(rel[0]),len(vectors[0]))
    for i in range(len(z)):
        for j in range(len(z[0])):
            if i<len(diag):
                assert z[i][j]%diag[i]==0
                coordinates[i][j]=z[i][j]//diag[i]
            else:
                assert z[i][j]==0
    inverse=mul(v,coordinates)
    assert mul(rel,inverse)==vectors

def check_core_maps(a,b,sites,e,rel,red):
    M=1
    for m,v in sites:
        M*=m
    X=sum((M//m)*v[0] for m,v in sites)
    Y=sum((M//m)*v[1] for m,v in sites)
    Delta=sum((M//m)*v[3] for m,v in sites)-e*M
    assert abs(Delta)==1
    assert all(gcd(m,q)==1 for i,(m,_) in enumerate(sites)
               for q,_ in sites[i+1:])
    assert all(gcd(m,v[3])==1 for m,v in sites)
    core=[[b,-Y,X],[0,M,0],[0,0,M]]
    rc=smith(core)
    g=reduce(gcd,(b,M,X,Y),0)
    assert diag_entries(rc[0])==[g,M,b*M//g]
    assert [x for x in diag_entries(red[0]) if x>1] == [x for x in (g,M,b*M//g) if x>1]

    # F sends (sigma,U,V) to (a*s,sum_i t_i(e1),sum_i t_i(e2)).
    F=zeros(len(rel),3);F[0][0]=a
    for i in range(len(sites)):
        F[1+4*i][1]=1;F[2+4*i][2]=1
    one,ainv,_=egcd(a,b)
    assert one==1
    G=zeros(3,len(rel));G[0][0]=ainv
    for i,(m,vec) in enumerate(sites):
        one,qinv,_=egcd(M//m,m)
        assert one==1
        r=(M//m)*qinv
        Ay=sum(((r-int(i==j))//q)*v[1] for j,(q,v) in enumerate(sites))
        Ax=sum(((r-int(i==j))//q)*v[0] for j,(q,v) in enumerate(sites))
        assert all((r-int(i==j))%q==0 for j,(q,v) in enumerate(sites))
        t1=[-Ay,r,0];t2=[Ax,0,r]
        one,alpha,_=egcd(vec[3],m)
        assert one==1
        tg=[-alpha*(vec[0]*t1[k]+vec[1]*t2[k]) for k in range(3)]
        for k in range(3):
            G[k][1+4*i]=t1[k]
            G[k][2+4*i]=t2[k]
            G[k][3+4*i]=0
            G[k][4+4*i]=tg[k]
    belongs(rel,red,mul(F,core))
    belongs(core,rc,mul(G,rel))
    belongs(rel,red,add(mul(F,G),eye(len(rel)),-1))
    belongs(core,rc,add(mul(G,F),eye(3),-1))

cases=[
    ('no-sites-zero',[],0),('no-sites-plus',[],1),('no-sites-minus',[],-1),
    ('unit-zero',[(1,[7,-4,9,0])],0),
    ('unit-plus',[(1,[-7,4,-9,1])],0),
    ('unit-minus',[(1,[7,-4,9,-1])],0),
    ('zero-slope',[(12,[5,6,7,0])],0),
    ('nonprimitive-n',[(12,[1,6,7,8])],0),
    ('even-coprime',[(2,[7,-3,8,1]),(3,[-5,8,7,-1])],0),
    ('odd-coprime',[(3,[9,4,-7,-1]),(5,[2,-11,6,2])],0),
    ('large-even',[(4,[-7,3,14,1]),(9,[6,-5,13,-2])],0),
    ('lifted-unit-slope',[(7,[100,-71,9,8])],1),
    ('noncoprime',[(2,[1,0,0,1]),(4,[0,1,0,-1])],0),
    ('triangle',[(2,[1,2,3,1]),(3,[4,5,6,1]),(5,[7,8,9,1])],0),
    ('triangle-rank-one',[(2,[1,2,3,1]),(3,[4,5,6,1]),(6,[7,8,9,-5])],0),
    ('many-unit-sites',[(1,[j,-2*j,j*j,n]) for j,n in enumerate((2,-3,0,7,-5,0,0))],0),
    ('mixed-five-sites',[(1,[7,-3,8,2]),(2,[7,-3,8,1]),
                         (3,[-5,8,7,-1]),(1,[3,6,4,-2]),(1,[9,8,7,0])],0),
]
_,n1,n2=egcd(991,997)
cases.append(('large-primes',[(997,[10**12+3,-10**11,9,n1]),
                             (991,[-10**13+7,10**10,12,n2])],0))
print('\nALL-ORDER PRESENTATION AND EXPLICIT MAP CHECKS')
for name,sites,e in cases:
    print(name, 'm=',[m for m,v in sites], 'n=',[v[3] for m,v in sites],
          'e=',e,'simple=',simply_connected(sites,e))
total=simple_total=lift_total=0
for a,b in sorted({(r[3],r[4]) for r in rows}):
    pair_simple=0
    for name,sites,e in cases:
        rel=presentation(a,b,sites,e)
        red=smith(rel)
        rank=len(rel)-len(diag_entries(red[0]))
        expected_rank=int(Fraction(e)==sum((Fraction(v[3],m) for m,v in sites),Fraction()))
        assert rank==expected_rank
        ss=smith(seifert(sites,e))
        assert len(sites)+1-len(diag_entries(ss[0]))==rank
        if simply_connected(sites,e):
            assert diag_entries(ss[0])==[1]*(len(sites)+1)
            check_core_maps(a,b,sites,e,rel,red)
            pair_simple+=1;simple_total+=1
        # Literal integral lift changes and their inverse preserve the full presentation.
        lambdas=[[i+2,-i-1,2*i+3,1-2*i] for i in range(len(sites))]
        new_sites=[(m,[v[j]+m*lam[j] for j in range(4)])
                   for (m,v),lam in zip(sites,lambdas)]
        new_e=e+sum(v[3] for v in lambdas)
        new_rel=presentation(a,b,new_sites,new_e)
        new_red=smith(new_rel)
        F=eye(len(rel));G=eye(len(rel))
        for i,lam in enumerate(lambdas):
            for j in range(4):
                k=omega_pair(a,b,eye(4)[j],lam)
                F[0][1+4*i+j]=k;G[0][1+4*i+j]=-k
        assert mul(F,G)==eye(len(rel))==mul(G,F)
        belongs(rel,red,mul(F,new_rel))
        belongs(new_rel,new_red,mul(G,rel))
        assert rank==len(new_rel)-len(diag_entries(new_red[0]))
        assert diag_entries(red[0])==diag_entries(new_red[0])
        total+=1;lift_total+=1
    print(f'a={a}, b={b}: {len(cases)} unrestricted presentation cases, '
          f'{pair_simple} exact CRT/three-generator inverse pairs, '
          f'{len(cases)} full-vector lift inverse pairs: PASS')
print('TOTAL presentation cases:',total,'CRT inverse comparisons:',simple_total,
      'full-vector lift inverse comparisons:',lift_total)
print('All sample Smith forms have the proved rational rank; all simply connected '
      'cases have factors gcd(b,M,X0,Y0), M, bM/g.')
print('The unbounded proof uses the displayed integer maps; finite cases are consistency checks.')
outdir=ROOT/'agents/continuation7_iii_semistable'
outdir.mkdir(parents=True,exist_ok=True)
certificate_path=outdir/'S6_SERIES_PUBLISH_III_02L0_fresh_lattice_certificates.json'
certificate_path.write_text(json.dumps({'scope':'fresh 62 natural semistable rows',
                                      'rows':certificates},indent=2)+'\n')
print('Saved all 62 actual integral inverse maps and finite fan words in the fresh certificate JSON.')
