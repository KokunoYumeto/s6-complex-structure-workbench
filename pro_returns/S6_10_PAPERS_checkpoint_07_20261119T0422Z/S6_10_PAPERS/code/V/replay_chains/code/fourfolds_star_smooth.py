"""Exact marked certificates for the f=2, b0=4 simply connected star-log family.

The proof is uniform in h>=1, e,r in Z, even phase j, and sign s=+/-1.
This file checks all six actual default initial rows, the symbolic meridian
identity, and all even component phases for n in {1,3}, 1<=h<=12.
Restriction Smith forms and all divisor cubic coefficients are checked at
phase zero, which is integrally conjugate by component rotation to each
even phase. No smooth classification is inferred from these checks alone;
the geometric proof is sections/fourfolds_D2_star_smooth.tex.
"""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form
from manifolds_rankone_families import decomp
from manifolds_star_log_caps import actual_markings, orbits

ROOT=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'records/manifolds_sphere_monodromies.json').read_text())['rows']
marks=actual_markings()
actual=[]
for row in rows:
    if row['entry'] not in [46,50] or row['profile']!='default' or row['b']!=4:
        continue
    key=[row[v] for v in ['entry','profile','a','b','zero_index']]
    mark=next(x for x in marks if x['key']==key)
    cols=[]
    for item in row['local']:
        if 'toric_vanishing_basis' in item:
            cols.extend(s.Matrix(item['toric_vanishing_basis']).columnspace())
    V=s.Matrix.hstack(*cols)
    assert V[3,:]==s.zeros(1,V.cols)
    H=hermite_normal_form(V[:3,:])
    assert H==s.eye(3)
    D,U,W,rank=decomp(V[:3,:])
    assert rank==3 and all(abs(D[i,i])==1 for i in range(3))
    actual.append(dict(key=key,n=mark['n'],canonical_basis=mark['basis'],
                       literal_vanishing_columns=V.tolist(),vertical_HNF=H.tolist()))
assert len(actual)==6

h,e,r,phase,sign=s.symbols('h e r phase sign',integer=True)
m=4*h;N=m*e+sign
assert s.expand(m*e-N)==-sign
# Every component meridian is m*g-v; the other fibre directions vanish
# in the actual exterior. This identity is independent of r and phase.
symbolic=dict(m=str(m),N=str(N),component_meridian_gamma=str(s.expand(m*e-N)),
              allowed_signs=[-1,1],phase='any even integer',transverse_r='any integer')

checks=[];phase_checks=0
for n in [1,3]:
    for hh in range(1,13):
        t=n*hh;q=2*t;rho=t+1
        for jj in range(0,q,2):
            vertices=orbits(range(q),lambda i:(jj-i)%q)
            edges=orbits(range(q),lambda i:(jj-i-1)%q)
            assert len(vertices)==rho and len(edges)==t
            assert sum(len(v)==1 for v in vertices)==2
            assert all(len(v)==2 for v in edges)
            vi={v:i for i,O in enumerate(vertices) for v in O}
            adjacency=set()
            for a,b in [(i,(i+1)%q) for i in range(q)]:
                assert vi[a]!=vi[b]
                adjacency.add(tuple(sorted((vi[a],vi[b]))))
            assert len(adjacency)==t
            deg=[sum(v in edge for edge in adjacency) for v in range(rho)]
            assert sorted(deg)==[1,1]+[2]*(rho-2)
            # Rotation by jj/2 identifies the exact reflection with phase zero.
            shift=jj//2
            assert all(((jj-i)-shift)%q==(-(i-shift))%q for i in range(q))
            phase_checks+=1

        # Actual Picard coordinates on endpoints: (sigma,F), sigma^2=1.
        # Interiors: (sigma,F), sigma^2=0.  Both have sigma.F=1, F^2=0.
        R=s.zeros(2*rho,rho);forms=[];canon=[]
        for i in range(rho):
            fixed=i in [0,t]
            Q=s.Matrix([[1 if fixed else 0,1],[1,0]])
            C=s.Matrix([2,-1]) if fixed else s.Matrix([1,0])
            K=-C if fixed else -2*C
            assert (K.T*Q*K)[0]==0 and (K.T*Q*C)[0]==0
            assert (C.T*Q*C)[0]==0
            forms.append(Q);canon.append(K)
            near=[j for j in [i-1,i+1] if 0<=j<rho]
            for j in near:R[2*i:2*i+2,j]=C
            R[2*i:2*i+2,i]=-len(near)*C
            assert R[2*i:2*i+2,i]==K
        assert R*s.ones(rho,1)==s.zeros(2*rho,1)
        for deleted in range(rho):
            cols=[j for j in range(rho) if j!=deleted]
            # Select F at endpoints and sigma at interior vertices, then omit
            # the same graph row. This gives a unit path-Laplacian cofactor.
            select=[2*i+(1 if i in [0,t] else 0) for i in range(rho) if i!=deleted]
            minor=R.extract(select,cols)
            assert abs(minor.det())==1
        D,U,W,rank=decomp(R[:,:t])
        assert rank==t and all(abs(D[i,i])==1 for i in range(t))
        # The complete component cubic is computed geometrically by restricting
        # two factors to the first component; all triples must vanish.
        triple_count=0
        for i in range(rho):
            block=R[2*i:2*i+2,:]
            cubic_slice=block.T*forms[i]*block
            assert cubic_slice==s.zeros(rho)
            triple_count+=rho*rho
        checks.append(dict(n=n,h=hh,q=q,rho=rho,free_rank=t,
                           primitive_smith=[1]*t,checked_component_triples=triple_count,
                           restriction_matrix=R.tolist(),component_canonical=[list(v) for v in canon]))

out=dict(scope=__doc__,actual_default_rows=actual,symbolic_meridians=symbolic,
         phase_checks=phase_checks,path_cases=checks,
         primary_classification='Zhubr 1975, Theorem 1 and section 1.5; primary PDF reopened',
         status='PASS: actual markings, all-parameter meridian identity, primitive lattice, cubic and characteristic restrictions')
(ROOT/'records/fourfolds_star_smooth.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print('Actual default rows / primitive vertical lattices:',len(actual))
print('All even phase-orbit comparisons:',phase_checks)
print('Path restriction / primitive Smith / full cubic cases:',len(checks))
print('Symbolic all-parameter component meridian:',symbolic)
print(out['status'])
