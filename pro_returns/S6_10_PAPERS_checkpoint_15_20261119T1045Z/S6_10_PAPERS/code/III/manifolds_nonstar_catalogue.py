"""Complete natural sphere patterns without I_n*, and exact hybrid log homology.
The finite-good formula requires gcd(m,n)=1, a necessary condition for
simple connectivity. Every sphere in these profiles is therefore included.
"""
from pathlib import Path
import json,csv,itertools,sympy as s
from collections import Counter
from math import gcd,prod
from manifolds_rankone_families import decomp,ikernel,wedge,biv,bezout
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'manifolds_sphere_normal_lattices.json').read_text())['rows']
monos=json.loads((ROOT/'manifolds_sphere_monodromies.json').read_text())['rows']
monos={(r['entry'],r['profile'],r['a'],r['b'],r['zero_index']):r for r in monos}
initial=json.loads((ROOT/'manifolds_sphere_initial.json').read_text())['candidates']
initial={(r['entry'],r['profile'],r['a'],r['b'],r['zero_index']):r for r in initial}

def smith_group(M):
    D,U,V,r=decomp(M)
    return M.rows-r,[int(abs(D[i,i])) for i in range(r) if abs(D[i,i])>1]

def hybrid_matrix(a,b,finite,regular,e=0):
    f=len(finite);r=len(regular);size=1+f+4*r
    omega=s.Matrix([[a,0,0,0,0,-b]])
    global_col=s.zeros(size,1);global_col[0]=b*e
    for i in range(f):global_col[1+i]=1
    for j in range(r):global_col[1+f+4*j+2]=1
    columns=[global_col]
    for i,(q,m,n) in enumerate(finite):
        assert m%q==b%q==0 and gcd(m,n)==1
        col=s.zeros(size,1);col[0]=b*n//q;col[1+i]=m//q;columns.append(col)
    for i,(m,v) in enumerate(regular):
        v=s.Matrix(v);assert m>0 and gcd(m,*map(int,v))==1
        for j in range(4):
            u=s.eye(4)[:,j];col=s.zeros(size,1);col[0]=-(omega*biv(u,v))[0]
            col[1+f+4*i+j]=m;columns.append(col)
        col=s.zeros(size,1);col[1+f+4*i:1+f+4*i+4,:]=v;columns.append(col)
    return s.Matrix.hstack(*columns)

def homology(a,b,finite,regular,e=0):
    logs=[(m,n) for q,m,n in finite]+[(m,v[3]) for m,v in regular]
    S=s.zeros(len(logs)+1)
    for i,(m,n) in enumerate(logs):S[i,0]=-n;S[i,i+1]=m
    S[-1,0]=-e
    for i in range(len(logs)):S[-1,i+1]=1
    r,A1=smith_group(S);r2,T=smith_group(hybrid_matrix(a,b,finite,regular,e));assert r==r2
    return dict(H0=[1,[]],H1=[r,A1],H2=[2*r,T],H3=[2*r,T],H4=[2*r,A1],H5=[r,[]],H6=[1,[]])

patterns=[];sphere=[];scalar_checks=0;smith_checks=0
for row in rows:
    if any(v['type'].startswith('I') and v['type'].endswith('*') and v['type'][1:-1].isdigit() for v in row['local']):continue
    key=(row['entry'],row['profile'],row['a'],row['b'],row['zero_index'])
    additive=[i for i,v in enumerate(row['local']) if not(v['type'].startswith('I') and v['type'][1:].isdigit())]
    choices=[]
    for i in additive:
        v=row['local'][i];opts=[]
        if v['original_minimal']:opts.append('original')
        if 'delta_index' in v:opts.append('log')
        choices.append(opts)
    for cc in itertools.product(*choices):
        fi=[i for i,c in zip(additive,cc) if c=='log']
        qs=[row['local'][i]['delta_index'] for i in fi];ds=[row['local'][i]['log_order'] for i in fi]
        Q=prod(qs);assert row['b']%Q==0
        obstruction=len(ds)>2 or (len(ds)==2 and gcd(*ds)!=1)
        rec={k:row[k] for k in ['entry','profile','a','b','zero_type','zero_index']}
        rec.update(additive_choices=list(zip(additive,cc)),finite_indices=fi,
                   finite_types=[row['local'][i]['type'] for i in fi],minimal_orders=ds,
                   component_product=Q,residual_c=row['b']//Q,orbifold_obstruction=obstruction)
        patterns.append(rec)
        if not obstruction and row['b']==Q:
            sphere.append(rec)
            # Actual scalar circle, at each zero-free multiplicative site.
            for j,(v,c) in enumerate(zip(monos[key]['local'],initial[key]['local'])):
                if j==row['zero_index'] or not(v['type'].startswith('I') and v['type'][1:].isdigit()):continue
                assert c['P_component']==0 and c['component_orbits']==1
                A=s.Matrix(v['matrix']);D,U,V,r=decomp(A-s.eye(4));assert r==1
                van=U.inv()[:,:1];D,_,_,r=decomp(van.row_join(s.eye(4)[:,2]))
                assert r==2 and abs(D[0,0])==abs(D[1,1])==1
                scalar_checks+=1
        if obstruction:continue
        # Exact all-primary formula checked on one/two-log data, including
        # regular sites whenever the orbifold criterion permits them.
        for k in (1,2,5):
            finite=[];regular=[]
            if len(fi)==2:
                m1,m2=ds[0]*k,ds[1]
                if gcd(m1,m2)!=1:continue
                n1,n2,gg=map(int,s.gcdex(m2,m1));assert gg==1
                finite=[(qs[0],m1,n1),(qs[1],m2,n2)]
            elif len(fi)==1:
                mf=ds[0]*k
                mr=next(z for z in (2,3,5,7,11) if gcd(z,mf)==1)
                nf,nr,gg=map(int,s.gcdex(mr,mf));assert gg==1
                finite=[(qs[0],mf,nf)];regular=[(mr,[2,3,5,nr])]
            else:
                m1,m2=k+1,k+2;n1,n2,gg=map(int,s.gcdex(m2,m1));assert gg==1
                regular=[(m1,[1,2,3,n1]),(m2,[2,3,5,n2])]
            H=homology(row['a'],row['b'],finite,regular)
            R=prod(m for m,v in regular);c=row['b']//Q
            X=sum((R//m)*v[0] for m,v in regular);Y=sum((R//m)*v[1] for m,v in regular)
            g=gcd(c,R,X,Y);want=[t for t in (g,R,c*R//g) if t>1]
            assert H['H1']==[0,[]] and H['H2']==[0,want],(rec,H,want)
            smith_checks+=1
        # Non-simply-connected and rational-Euler-zero inputs are retained.
        if len(fi)==1:
            q,d=qs[0],ds[0]
            for n in (1,5,7):
                if gcd(n,d)!=1:continue
                homology(row['a'],row['b'],[(q,d,n)],[]);smith_checks+=1

assert len(patterns)==164 and len(sphere)==59
print('All minimal-cap patterns:',len(patterns))
print('Compatible with possible simple connectivity:',sum(not x['orbifold_obstruction'] for x in patterns))
print('Sphere patterns:',len(sphere),'distinct initial rows',len(set((x['entry'],x['profile'],x['a'],x['b'],x['zero_index']) for x in sphere)))
print('Profile sphere counts:',dict(Counter((x['entry'],x['profile']) for x in sphere)))
print('Actual scalar-circle checks:',scalar_checks,'hybrid Smith checks:',smith_checks)
record=dict(scope=__doc__,all_patterns=patterns,sphere_patterns=sphere,scalar_checks=scalar_checks,smith_checks=smith_checks)
(ROOT/'manifolds_nonstar_sphere_patterns.json').write_text(json.dumps(record,indent=2,default=int)+'\n')
with (ROOT/'manifolds_nonstar_sphere_patterns.csv').open('w',newline='') as f:
    fields=['entry','profile','a','b','zero_type','zero_index','finite_types','minimal_orders','component_product','residual_c','additive_choices']
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for row in sphere:w.writerow({k:row[k] for k in fields})
