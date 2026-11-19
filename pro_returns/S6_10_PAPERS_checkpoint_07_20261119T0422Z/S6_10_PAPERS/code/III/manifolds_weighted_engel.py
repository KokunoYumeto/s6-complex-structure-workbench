"""All positive initial weights and all free finite logs on Engel's profile.

P=G, Q=6*d*G, the linearization has zero d at I1.  The cusp is
the d-period smooth hexagonal tube.  This is an exact integer algorithm,
including nonprimitive finite numerators and zero Seifert Euler number.
The all-parameter proof is Theorem D.2.34.
"""
from pathlib import Path
from itertools import combinations, product
from math import gcd
import argparse
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from manifolds_rankone_families import wedge, biv

ROOT = Path(__file__).resolve().parent

def group(M):
    D = smith_normal_form(M, domain=s.ZZ)
    ds = [abs(int(D[j,j])) for j in range(min(D.shape)) if D[j,j]]
    return dict(free=M.rows-len(ds), torsion=[z for z in ds if z>1])

def admissible(m,n,r,order,q):
    t=gcd(m,n,q*r)
    return gcd(m,n,r)==1 and (m//t)%order==0

def matrices(d):
    A=s.Matrix([[1,-1,0,2*d],[0,-1,-1,6*d],[0,1,0,0],[0,0,0,1]])
    B=s.Matrix([[1,0,1,-3*d],[0,0,1,0],[0,-1,0,6*d],[0,0,0,1]])
    C=s.Matrix([[1,0,0,d],[0,1,1,0],[0,0,1,0],[0,0,0,1]])
    return A,B,C

def normal_matrix(d,k,l,n0,n1,r0,r1,original0=False,original1=False):
    M=s.Matrix([
        [-2*d*n0,-6*d*r0,0,-3*d*n1,-6*d*r1,0],
        [-k,0,r0,2*l,0,-r1],
        [0,3*k,n0,0,0,0],
        [0,0,0,0,4*l,n1]])
    if original0:M[:,:3]=s.Matrix([[2*d,0,0],[0,1,0],[0,0,1],[0,0,0]])
    if original1:M[:,3:]=s.Matrix([[3*d,0,0],[0,-1,0],[0,0,0],[0,0,1]])
    return M

def compute(d,k,l,n0,n1,r0=0,r1=0,original0=False,original1=False):
    if min(d,k,l)<1:
        raise ValueError("d,k,l must be positive.")
    m0,m1=3*k,4*l
    if (not original0 and not admissible(m0,n0,r0,3,3)) or (not original1 and not admissible(m1,n1,r1,4,2)):
        raise ValueError("The finite affine action is not free.")
    mm0,nn0=(1,0) if original0 else (m0,n0)
    mm1,nn1=(1,0) if original1 else (m1,n1)
    P=mm1*nn0+mm0*nn1
    H1=group(s.Matrix([[-nn0,mm0],[-nn1,-mm1]]))
    G=group(normal_matrix(d,k,l,n0,n1,r0,r1,original0,original1))
    rr=H1['free']
    L=int(original0)+int(original1);beta=5*int(original0)
    assert rr==int(P==0) and G['free']==(rr if not L else 0)
    T=G['torsion']; A1=H1['torsion']
    b2=d-1+2*rr if not L else d-1+beta+L+rr
    b3=2*rr if not L else 2*beta+2*L
    homology=[
        dict(free=1,torsion=[]),
        H1,
        dict(free=b2,torsion=T),
        dict(free=b3,torsion=T),
        dict(free=b2,torsion=A1),
        dict(free=rr,torsion=[]),
        dict(free=1,torsion=[])]
    assert sum((-1)**j*h['free'] for j,h in enumerate(homology))==2*d
    return dict(d=d,k=k,l=l,n0=n0,n1=n1,r0=r0,r1=r1,P=P,
                original=[original0,original1],component_defect=beta,extra_bridge=L,
                cap_torsion=[0 if original0 else gcd(m0,n0,3*r0),0 if original1 else gcd(m1,n1,2*r1)],
                pi1_abelian=H1,normal_matrix=normal_matrix(d,k,l,n0,n1,r0,r1,original0,original1).tolist(),
                homology=homology)

def symbolic_certificates():
    d=s.symbols('d',integer=True,positive=True)
    A,B,C=matrices(d);I=s.eye(4)
    assert A*B*C==I and A**3==I and B**4==I
    delta,a,b,gamma=(I[:,j] for j in range(4))
    u0=gamma+2*d*(a+b);u1=gamma+3*d*(a+b)
    assert A*u0==u0 and B*u1==u1
    omega=s.Matrix([[0,0,-6*d,1,0,0]])
    assert omega*wedge(A)==omega and omega*wedge(B)==omega
    R=s.Matrix.hstack(wedge(A)-s.eye(6),wedge(B)-s.eye(6))
    K=s.Matrix.hstack(biv(delta,a),biv(delta,b),
                      biv(delta,gamma)+6*d*biv(a,b),biv(a,gamma),biv(b,gamma))
    kr=[0,1,2,4,5]
    coeff=R[kr,:]
    assert K*coeff==R
    unit_columns=None
    for cols in combinations(range(R.cols),5):
        M=coeff[:,list(cols)]
        if abs(M.subs(d,1).det())==1 and M.det() in [1,-1]:
            unit_columns=cols;break
    assert unit_columns is not None
    # A primitive integral basis of the entire five-dimensional graph kernel.
    cd=(-delta).col_join(-delta);ca=b.col_join(-a)
    K1=s.Matrix.hstack(cd,ca,delta.col_join(s.zeros(4,1)),
                       u0.col_join(s.zeros(4,1)),s.zeros(4,1).col_join(u1))
    DD=s.Matrix.hstack(A-I,B-I)
    assert DD*K1==s.zeros(4,5)
    kr1=[0,2,3,4,7]
    assert abs(K1[kr1,:].det())==1
    assert sum((A**i for i in range(3)),s.zeros(4))*a==-delta
    assert sum((B**i for i in range(4)),s.zeros(4))*a==-2*delta
    assert sum((A**i for i in range(3)),s.zeros(4))*gamma==3*u0
    assert sum((B**i for i in range(4)),s.zeros(4))*gamma==4*u1
    return dict(symbolic_matrices=[M.tolist() for M in (A,B,C)],
                omega=list(omega),fibre_kernel_basis=K.tolist(),
                unit_fibre_relation_columns=list(unit_columns),
                graph_kernel_basis=K1.tolist(),unit_graph_rows=kr1)

def full_graph_matrix(d,k,l,n0,n1,r0,r1,original0=False,original1=False):
    A,B,C=matrices(d);I=s.eye(4)
    delta,a,b,gamma=(I[:,j] for j in range(4))
    u0=gamma+2*d*(a+b);u1=gamma+3*d*(a+b)
    cd=(-delta).col_join(-delta);ca=b.col_join(-a)
    K=s.Matrix.hstack(cd,ca,delta.col_join(s.zeros(4,1)),
                     u0.col_join(s.zeros(4,1)),s.zeros(4,1).col_join(u1))
    kr=[0,2,3,4,7];Ki=K[kr,:].inv()
    omega=s.Matrix([[0,0,-6*d,1,0,0]])
    out=[s.Matrix([0]).col_join(s.eye(5)[:,j]) for j in range(2)]
    for site,(AA,m,n,r,uu,order) in enumerate([
            (A,3*k,n0,r0,u0,3),(B,4*l,n1,r1,u1,4)]):
        if (original0,original1)[site]:
            z=2*d if site==0 else 3*d
            for fibre in [biv(delta,a),biv(delta,b),biv(delta,gamma),
                          biv(a,gamma)+z*biv(a,b),biv(b,gamma)-z*biv(a,b)]:
                out.append(s.Matrix([(omega*fibre)[0]]).col_join(s.zeros(5,1)))
            for cut in [delta,uu]:
                graph=cut.col_join(s.zeros(4,1)) if site==0 else s.zeros(4,1).col_join(cut)
                coord=Ki*graph[kr,:]
                assert K*coord==graph
                out.append(s.Matrix([0]).col_join(coord))
            continue
        v=n*uu+r*delta
        Nm=(m//order)*sum((AA**j for j in range(order)),s.zeros(4))
        for loop in [a,gamma,None]:
            cut=Nm*loop if loop is not None else v
            graph=cut.col_join(s.zeros(4,1)) if site==0 else s.zeros(4,1).col_join(cut)
            coord=Ki*graph[kr,:]
            assert K*coord==graph and all(z.q==1 for z in coord)
            f=-(omega*biv(loop,v))[0] if loop is not None else 0
            out.append(s.Matrix([f]).col_join(coord))
    return s.Matrix.hstack(*out)

def verify():
    cert=symbolic_certificates()
    full_checks=primitive_checks=nonprimitive_checks=zero_checks=original_checks=0
    samples=[]
    for d,k,l in product([1,2,3,4,6,9,12],[1,2,3,4],[1,2,3,4]):
        m0,m1=3*k,4*l
        choices0=[(1,0),(-1,2),(m0-1,-1),(0,1),(3,1),(2,1)]
        choices1=[(1,0),(-1,3),(m1-1,-1),(0,1),(2,1),(4,1)]
        # The six paired choices include primitive, torsion-cap and zero-Euler data.
        for (n0,r0),(n1,r1) in zip(choices0,choices1):
            if not admissible(m0,n0,r0,3,3) or not admissible(m1,n1,r1,4,2):continue
            result=compute(d,k,l,n0,n1,r0,r1)
            full=full_graph_matrix(d,k,l,n0,n1,r0,r1)
            assert group(full)==group(normal_matrix(d,k,l,n0,n1,r0,r1))
            full_checks+=1
            if gcd(m0,n0)==gcd(m1,n1)==1:
                g=gcd(d,k,2*l);P=result['P']
                expected=dict(free=int(P==0),torsion=[])
                factors=[g,d*abs(P)//g] if P else [g]
                expected['torsion']=[v for v in factors if v>1]
                assert group(normal_matrix(d,k,l,n0,n1,r0,r1))==expected
                primitive_checks+=1
            else:nonprimitive_checks+=1
            zero_checks+=result['P']==0
            if d in [2,3,6] and k==l==2:samples.append(result)
            for o0,o1 in [(True,False),(False,True),(True,True)]:
                result=compute(d,k,l,n0,n1,r0,r1,o0,o1)
                full=full_graph_matrix(d,k,l,n0,n1,r0,r1,o0,o1)
                assert group(full)==group(normal_matrix(d,k,l,n0,n1,r0,r1,o0,o1))
                if o0 and o1:
                    target=s.diag(d)
                    assert result['homology'][2]['free']==d+7 and result['homology'][3]['free']==14
                elif o0:target=s.diag(d*gcd(2,n1),gcd(m1,n1))
                else:target=s.diag(d*gcd(3,n0),gcd(m0,n0))
                assert result['homology'][2]['torsion']==group(target)['torsion']
                full_checks+=1;original_checks+=1;zero_checks+=result['P']==0
    # Primitive zero-Euler data necessarily have 3k=4l.
    for d,j in product(range(1,19),range(1,5)):
        result=compute(d,4*j,3*j,1,-1,2,-3)
        assert result['homology'][2]==dict(free=d+1,torsion=[gcd(d,2*j)] if gcd(d,2*j)>1 else [])
        assert result['homology'][3]['free']==2
        full=full_graph_matrix(d,4*j,3*j,1,-1,2,-3)
        assert group(full)==group(normal_matrix(d,4*j,3*j,1,-1,2,-3))
        full_checks+=1;primitive_checks+=1;zero_checks+=1
    print('Symbolic polynomial monodromy, primitive fibre and graph certificates passed.')
    print('Full unreduced graph Smith comparisons:',full_checks)
    print('Primitive closed formulas:',primitive_checks,
          'nonprimitive free twists:',nonprimitive_checks,'Euler-zero:',zero_checks)
    print('Original/log closed-form comparisons:',original_checks)
    data=dict(scope=__doc__,symbolic=cert,full_Smith_checks=full_checks,
              primitive_formula_checks=primitive_checks,nonprimitive_checks=nonprimitive_checks,
              euler_zero_checks=zero_checks,original_checks=original_checks,samples=samples)
    (ROOT/'manifolds_weighted_engel.json').write_text(json.dumps(data,indent=2,default=str)+'\n')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data',nargs=7,type=int,metavar=('d','k','l','n0','n1','r0','r1'))
    parser.add_argument('--original0',action='store_true')
    parser.add_argument('--original1',action='store_true')
    args=parser.parse_args()
    if args.data:
        print(json.dumps(compute(*args.data,args.original0,args.original1),indent=2,default=int))
    else:verify()
