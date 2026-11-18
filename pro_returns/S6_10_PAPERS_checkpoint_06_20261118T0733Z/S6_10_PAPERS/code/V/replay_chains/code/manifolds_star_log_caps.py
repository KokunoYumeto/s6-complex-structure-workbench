"""Unbounded canonical I_n* log-cap normalization, prospective D.2.49.

Scope: n=1 or3, canonical integral block, m=2k and gamma power prime
to m. The affine component action is i -> phase-i on q=n*k components.
Full integral cap groups and fibre-index certificates are computed.
The no-fixed-vertex torsion correction is computed by the actual
aspherical quotient: both primitive fibre lifts have the nonzero Z2
correction. Full fixed-normal columns are retained.
"""
from pathlib import Path
from math import gcd
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form
from manifolds_rankone_families import decomp,ikernel,wedge,biv,bezout
from manifolds_general_initial import integer_solution
from manifolds_weighted_profiles import group
ROOT=Path(__file__).resolve().parents[1]

def orbits(items,action):
    seen=set();out=[]
    for i in items:
        if i in seen:continue
        orbit=[];j=i
        while j not in seen:seen.add(j);orbit.append(j);j=action(j)
        out.append(orbit)
    return out

def canonical(n):
    return s.Matrix([[-1,0,-1,0],[0,-1,0,0],[0,-n,1,0],[0,0,0,1]])

def normal_kernel(k,phase,N,r,fixed_count):
    assert gcd(N,2*k)==1
    Rpower=2*r-phase
    if fixed_count==1:
        K=ikernel(s.Matrix([[1,0,0,0],[0,-k,2*N,-Rpower]]))
    elif fixed_count==2:
        assert k%2==0 and Rpower%2==0
        K=ikernel(s.Matrix([[1,0,0,0],[0,-k//2,N,-Rpower//2]]))
    else:
        assert k%2==0 and Rpower%2==1
        lift=s.Matrix([[0,0,0],[2,0,0],[0,1,0],[0,0,1]])
        K=lift*ikernel(s.Matrix([[-2*k,2*N,-Rpower]]))
    return hermite_normal_form(K)

def cap(n,k,phase,N=1,r=0):
    assert n in [1,3] and k>0
    assert gcd(N,2*k)==1
    q=n*k;phase_lift=phase;phase%=q;peripheral_shift=(phase_lift-phase)//q
    Rpower=2*r-phase_lift
    vertices=orbits(range(q),lambda i:(phase-i)%q)
    edges=orbits(range(q),lambda i:(phase-i-1)%q)
    flags=orbits([(i,d) for i in range(q) for d in [-1,1]],
                 lambda x:((phase-x[0])%q,-x[1]))
    vi={v:i for i,O in enumerate(vertices) for v in O}
    ei={v:i for i,O in enumerate(edges) for v in O}
    rho=len(vertices);epsilon=len(edges)
    fixed=[i for i,O in enumerate(vertices) if len(O)==1]
    fixed_edges=[i for i,O in enumerate(edges) if len(O)==1]
    assert len(fixed)+len(fixed_edges)==2
    assert rho+epsilon==q+1 and len(flags)==q
    # Each normalization gives f,sigma; each double curve gives D.
    R=s.zeros(2*rho+epsilon,q);flag_data=[]
    for j,O in enumerate(flags):
        v,d=O[0];V=vi[v];E=ei[(v if d==1 else v-1)%q]
        if V in fixed:R[2*V,j]=-1;R[2*V+1,j]=2
        else:R[2*V+1,j]=1
        degree=2 if E in fixed_edges else 1
        R[2*rho+E,j]=-degree
        flag_data.append(dict(vertex=V,edge=E,conductor_degree=degree))
    H2=group(R)
    expected=dict(free=rho+1,torsion=([2] if not fixed else []))
    assert H2==expected and R.rank()==q
    # The universal common conductor section class S.
    V=flag_data[0]['vertex'];S=s.zeros(R.rows,1)
    if V in fixed:S[2*V]=-1;S[2*V+1]=2
    else:S[2*V+1]=1
    for V in range(rho):
        local=s.zeros(R.rows,1)
        if V in fixed:local[2*V]=-1;local[2*V+1]=2
        else:local[2*V+1]=1
        integer_solution(R,local-S)
    total=s.zeros(R.rows,1);T=s.zeros(R.rows,1)
    for V,O in enumerate(vertices):
        total[2*V]=len(O)
        T[2*V+1 if V in fixed else 2*V]=1
    def edgeclass(i):return s.eye(R.rows)[:,2*rho+i]
    if len(fixed)==1:
        assert k%2==1
        D=edgeclass(fixed_edges[0]);x=-T+D;w=-k*D
        normal_delta=2*N*D;normal_long=-Rpower*D;kappa=k
    elif len(fixed)==2:
        assert k%2==0
        x=-T+S;w=-(k//2)*S
        normal_delta=N*S;normal_long=-(Rpower//2)*S;kappa=k//2
    else:
        assert k%2==0 and phase%2==1
        D0,D1=[edgeclass(i) for i in fixed_edges];tau=D1-D0
        integer_solution(R,2*tau)
        x=-T+tau;w=-k*D0+tau
        normal_delta=2*N*D0;normal_long=-Rpower*D0+peripheral_shift*tau
        kappa=2*k
    integer_solution(R,2*x+total)
    integer_solution(R,2*w+k*S)
    integer_solution(R,2*k*normal_delta+4*N*w)
    integer_solution(R,2*k*normal_long-2*Rpower*w)
    G=group(R.row_join(x).row_join(w))
    assert G['free']==rho-1
    order=1
    for d in G['torsion']:order*=d
    assert order==kappa
    image=s.Matrix.hstack(x,w,normal_delta,normal_long)
    K=normal_kernel(k,phase_lift,N,r,len(fixed))
    exact=ikernel(R.row_join(image))[R.cols:,:]
    assert hermite_normal_form(exact)==K
    assert group(R.row_join(image))==dict(free=rho-1,torsion=[])
    assert group(K[2:,:])==dict(free=0,torsion=([kappa] if kappa>1 else []))
    A=canonical(n);assert A*A-s.eye(4)==n*s.eye(4)[:,0]*s.eye(4)[1,:]
    assert group(A-s.eye(4))==dict(free=2,torsion=[])
    assert group(wedge(A)-s.eye(6))==dict(free=2,torsion=[])
    # Independent mapping-torus chain calculation. Its lifted area t is
    # specialized beta wedge lambda; naturality gives t -> -t-sum f_i.
    P=s.zeros(q)
    for i in range(q):P[(phase-i)%q,i]=1
    H1action=s.Matrix([[-1,0],[-n,1]])
    H2action=s.zeros(q+1);H2action[:q,:q]=P
    H2action[:q,q]=-s.ones(q,1);H2action[q,q]=-1
    assert H2action*H2action==s.eye(q+1)
    C2=group(H2action-s.eye(q+1));C2['free']+=1
    assert C2==H2
    assert group(H1action-s.eye(2))==dict(free=1,torsion=[])
    return dict(n=n,k=k,m=2*k,phase=phase,phase_lift=phase_lift,
                peripheral_shift=peripheral_shift,N=N,r=r,R=Rpower,component_count=q,
                vertex_orbits=vertices,edge_orbits=edges,fixed_components=len(fixed),
                normalization_relations=R.tolist(),common_section=list(map(int,S)),
                homology=[dict(free=1,torsion=[]),dict(free=2,torsion=[]),H2,
                          dict(free=2*rho,torsion=[]),dict(free=rho,torsion=[])],
                fibre_image=dict(x=list(map(int,x)),w=list(map(int,w)),cokernel=G),
                full_boundary_image=image.tolist(),full_boundary_kernel=K.tolist(),
                projected_normal_index=kappa,
                normal_torus_quotient=2*k//kappa)

def one_star_formula(k,phase,N,r,e,B):
    f=1 if k%2 else (2 if phase%2==0 else 0)
    K=normal_kernel(k,phase,N,r,f);sigma=N-2*k*e
    assert sigma and gcd(sigma,2*k)==1
    M=s.Matrix.vstack(B*(K[1,:]-4*e*K[2,:]),K[3,:])
    out=group(M)
    expected=([2*B*abs(sigma)] if f==1 else
              [B*abs(sigma)] if f==2 else [2,2*B*abs(sigma)])
    expected=[x for x in expected if x>1]
    assert out==dict(free=0,torsion=expected)
    return dict(k=k,phase=phase,N=N,r=r,e=e,b=4*B,sigma=sigma,
                full_kernel=K.tolist(),global_relation_matrix=M.tolist(),H2_torsion=expected)

def actual_markings():
    records=[]
    rows=json.loads((ROOT/'records/manifolds_sphere_monodromies.json').read_text())['rows']
    for row in rows:
        for j,loc in enumerate(row['local']):
            if loc['type'] not in ['I1*','I3*'] or row['a']%2==0:continue
            A=s.Matrix(loc['matrix']);DD,U,V,rank=decomp(A*A-s.eye(4))
            assert rank==1;n=int(DD[0,0]);alpha=U.inv()[:,0]
            lam=(s.eye(4)[:,2]+alpha)/2;assert all(x.q==1 for x in lam)
            beta=integer_solution((A+s.eye(4)).col_join(s.eye(4)[3,:]),
                                  (-n*lam).col_join(s.zeros(1,1)))
            F=ikernel(A-s.eye(4));ell=F*bezout(list(F[3,:]))[0]
            C=s.Matrix.hstack(alpha,beta,lam,ell)
            assert C.det()==1 and C.inv()*A*C==canonical(n)
            omega=s.Matrix([[row['a'],0,0,0,0,-row['b']]])
            x=biv(beta,lam)
            # n is odd; w=(beta ell +(n-1)/2 lambda ell) has the primitive
            # class with beta ell=n w, lambda ell=-2 w.
            w=biv(beta,ell)+((n-1)//2)*biv(lam,ell)
            assert (omega*x)[0]==-row['a'] and (omega*w)[0]==s.Rational(row['b'],4)
            records.append(dict(key=[row[k] for k in ['entry','profile','a','b','zero_index']],
                                site=j,type=loc['type'],basis=C.tolist(),n=n,
                                canonical_matrix=canonical(n).tolist()))
    assert len(records)==12
    return records

if __name__=='__main__':
    markings=actual_markings();cases=[]
    for n in [1,3]:
        for k in range(1,13):
            for phase in sorted(set([0,1,n*k,n*k+1])):
                cases.append(cap(n,k,phase))
    # The actual group-homology correction in the no-fixed-component case.
    nn,kk,aa,RR=s.symbols('n k a R',integer=True)
    # In the Z2 fibre coinvariant, n,a,R are odd and k is even:
    # beta ell -> -kn z -(kn+aR)t, lambda ell -> 2k z.
    assert s.expand(-kk*nn+((nn-1)/2)*(2*kk))==-kk
    aspherical=dict(H2='Z[z] + Z2[t]',D0='z',D1='z-t',
                    x='t',w='-k*z+t for k even and R odd',
                    normal_delta='2*N*z',normal_long='-R*z')
    global_cases=[]
    for k in range(1,13):
        for phase in range(min(2,k)):
            for N in sorted(set([1,-1,2*k+1,2*k-1])):
                for r in [-1,0,1]:
                    for e in [-1,0,1]:
                        for B in [1,3]:global_cases.append(one_star_formula(k,phase,N,r,e,B))
    print('Actual canonical marked star positions',len(markings),flush=True)
    print('Exact normalization/mapping-torus comparisons',len(cases),flush=True)
    print('All projected-normal indices: k (one fixed), k/2 (two fixed), 2k (none).',flush=True)
    print('No-fixed-component torsion marking resolved by actual group homology.',flush=True)
    print('All-order one-star closed Smith comparisons',len(global_cases),flush=True)
    (ROOT/'records/manifolds_star_log_caps.json').write_text(
        json.dumps(dict(scope=__doc__,markings=markings,cases=cases,
                        aspherical_marking=aspherical,one_star=global_cases),indent=2,default=int)+'\n')
