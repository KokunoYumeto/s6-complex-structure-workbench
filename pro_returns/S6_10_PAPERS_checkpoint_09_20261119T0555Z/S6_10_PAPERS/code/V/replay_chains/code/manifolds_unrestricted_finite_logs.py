"""Unrestricted free finite logs at all primitive-gamma finite cap positions.
Exact all-order arithmetic criterion and three-column Thom normal kernels.
Finite runs validate the symbolic proofs; no multiplicity bound is used in them.
"""
from pathlib import Path
import json,sympy as s
from math import gcd
from collections import Counter
from manifolds_rankone_families import decomp,ikernel,biv,bezout,wedge
ROOT=Path(__file__).resolve().parents[1]
normal=json.loads((ROOT/'records/manifolds_sphere_normal_lattices.json').read_text())['rows']
monos=json.loads((ROOT/'records/manifolds_sphere_monodromies.json').read_text())['rows']
key=lambda r:(r['entry'],r['profile'],r['a'],r['b'],r['zero_index'])
mono={key(r):r for r in monos};norm={key(r):r for r in normal}
patterns=json.loads((ROOT/'records/manifolds_nonstar_sphere_patterns.json').read_text())['all_patterns']

def group(M):
    D,U,V,r=decomp(M)
    return M.rows-r,[int(abs(D[j,j])) for j in range(r) if abs(D[j,j])>1]

def admissible(d,q,m,n,r):
    assert m%d==0
    t=gcd(m,n,q*r)
    return gcd(m,n,r)==1 and (m//t)%d==0

def hybrid(a,b,finite,regular=(),e=0):
    f=len(finite);R=len(regular);size=1+2*f+4*R
    cols=[];g=s.zeros(size,1);g[0]=b*e
    for i in range(f):g[1+2*i]=1
    for i in range(R):g[1+2*f+4*i+2]=1
    cols.append(g)
    for i,(d,q,m,n,r) in enumerate(finite):
        assert admissible(d,q,m,n,r)
        for c0,cd,cl in [(b*n//q,m//q,0),(-b*r,0,m),(0,r,n)]:
            c=s.zeros(size,1);c[0]=c0;c[1+2*i]=cd;c[2+2*i]=cl;cols.append(c)
    omega=s.Matrix([[a,0,0,0,0,-b]])
    for i,(m,v) in enumerate(regular):
        assert gcd(m,*v)==1;v=s.Matrix(v);start=1+2*f+4*i
        for j in range(4):
            u=s.eye(4)[:,j];c=s.zeros(size,1);c[0]=-(omega*biv(u,v))[0];c[start+j]=m;cols.append(c)
        c=s.zeros(size,1);c[start:start+4,0]=v;cols.append(c)
    return s.Matrix.hstack(*cols)

power_checks=0;cap_cases=[]
for row in normal:
    mats=[s.Matrix(x['matrix']) for x in mono[key(row)]['local']]
    for i,loc in enumerate(row['local']):
        if 'delta_index' not in loc:continue
        A=mats[i];d=loc['log_order'];q=loc['delta_index'];ell=s.Matrix(loc['ell']);delta=s.eye(4)[:,2]
        assert group(A-s.eye(4))==(2,[]) and group(wedge(A)-s.eye(6))==(2,[])
        tests=[]
        for j in range(d):
            L=ikernel((A**j-s.eye(4)).T).T
            tests.append([(int((L*ell)[h]),int((L*delta)[h])) for h in range(L.rows)])
        for k in range(1,7):
            m=d*k
            for n in range(m):
                for r in range(m):
                    free=True
                    for j in range(1,m):
                        if all((j*(ln*n+lr*r))%m==0 for ln,lr in tests[j%d]):
                            free=False;break
                    assert free==admissible(d,q,m,n,r),(key(row),i,m,n,r,free)
                    power_checks+=1
        cap_cases.append(dict(entry=row['entry'],profile=row['profile'],a=row['a'],b=row['b'],
                              zero_index=row['zero_index'],site=i,type=loc['type'],d=d,q=q))
print('Full affine fixed-point power checks:',power_checks,'at',len(cap_cases),'marked finite positions',flush=True)

cache={};full_checks=0;new_torsion_cases=0;rank_checks=0
for pat in patterns:
    K=key(pat);row=norm[K];mr=mono[K];A=[s.Matrix(x['matrix']) for x in mr['local']];N=len(A)
    if K not in cache:
        D=s.Matrix.hstack(*[x-s.eye(4) for x in A[:-1]])
        Sd,Ud,Vd,rd=decomp(D);Wi=Vd.inv()[rd:,:]
        def ji(i,x):
            if i<N-1:
                y=s.zeros(4*(N-1),x.cols);y[4*i:4*i+4,:]=x;return y
            oo=[]
            for h in range(N-1):
                p=s.eye(4)
                for z in A[h+1:N-1]:p=p*z
                oo.append(-p*x)
            return s.Matrix.vstack(*oo)
        Js=[]
        for i in range(N):Js.append(Wi*ji(i,s.eye(4)))
        cache[K]=(Wi.rows,Js)
    h,Js=cache[K];fi=pat['finite_indices']
    if not fi:continue
    samples=[]
    for target in range(len(fi)):
        for case in range(5):
            params=[]
            for j,i in enumerate(fi):
                v=row['local'][i];d=v['log_order'];q=v['delta_index']
                m,n,r=d,1,0
                if j==target:
                    m,n,r=[(d,1,0),(d*q,0,1),(d*q,q,1),(2*d,2,1),(3*d,3,1)][case]
                assert admissible(d,q,m,n,r)
                params.append((d,q,m,n,r))
            samples.append(params)
    for params in samples:
        cs=[];slot={i:p for i,p in zip(fi,params)}
        for i,loc in enumerate(row['local']):
            if i not in slot:
                fixed=s.Matrix(loc['fixed']);M=Js[i]*fixed
                for j in range(M.cols):cs.append(s.Matrix([0]).col_join(M[:,j]))
            else:
                d,q,m,n,r=slot[i];ell=s.Matrix(loc['ell']);beta=s.Matrix(loc['beta']);delta=s.eye(4)[:,2]
                Nm=sum((A[i]**j for j in range(m)),s.zeros(4))
                assert Nm*beta==(m//q)*delta
                for c0,u in [(row['b']*n//q,Nm*beta),(-row['b']*r,m*ell),(0,r*delta+n*ell)]:
                    cs.append(s.Matrix([c0]).col_join(Js[i]*u))
                P=s.Matrix([[m//q,0,r],[0,m,n]])
                gp=group(P);t=gcd(m,n,q*r)
                assert gp[0]==0
                order=1
                for z in gp[1]:order*=z
                assert order==(m//q)*t
                new_torsion_cases+=t>1
        full=s.Matrix.hstack(*cs);small=hybrid(row['a'],row['b'],params)
        assert group(full)==group(small),(K,params,group(full),group(small))
        # Rational ranks and all-primary duality table retain euler-zero cases.
        S=s.zeros(len(params)+1)
        for j,(_,_,m,n,r) in enumerate(params):S[j,0]=-n;S[j,j+1]=m;S[-1,j+1]=1
        r1,H1=group(S);r2,H2=group(small);assert r1==r2
        full_checks+=1;rank_checks+=r1==1
print('Full unreduced graph/normal Smith comparisons:',full_checks,flush=True)
print('Cap-torsion instances retained:',new_torsion_cases,'Euler-zero instances:',rank_checks,flush=True)
# Concrete new countercheck to extrapolating the primitive-gamma formula.
assert group(hybrid(1,3,[(3,3,9,3,1)]))==(0,[3,3])
assert group(hybrid(1,2,[(4,2,8,0,1)]))==(1,[2])
print('Examples: (q,m,n,r)=(3,9,3,1) has H2=H3=(Z3)^2; (2,8,0,1) has H2=H3=Z²+Z2.',flush=True)
(ROOT/'records/manifolds_unrestricted_finite_logs.json').write_text(json.dumps(dict(scope=__doc__,
    finite_positions=cap_cases,power_checks=power_checks,full_Smith_checks=full_checks,
    retained_cap_torsion_instances=new_torsion_cases,euler_zero_instances=rank_checks),indent=2)+'\n')
