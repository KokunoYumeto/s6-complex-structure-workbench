"""Finite exact H^3/H^5 test for a normalized eligible (5,4) datum.

The theorem proves this test for every rational (5,4) pair and every
primitive-cusp integral extension passing the stated preliminary tests.
The executed examples below are exactly v=0,1,2 of F.2.16; there is no
finite-height claim about other rational parameters.

Convention dictionary: the imported family(v) matrices A,B are geometric
cohomology pullbacks.  test_pair takes geometric homology M1=A.T,M2=B.T,
and constructs the genuine left cohomology transport T1=A**-1,T2=B**-1.
For comparison with earlier calculations using A,B, simultaneous peripheral
reversal g1->g1**-1, g2->g2**-1 sends g0=(g1*g2)**-1 to
g2*g1=g1**-1*(g1*g2)*g1.  Thus its cusp is conjugate to the inverse
old cusp.  Invariant and coinvariant lattices are unchanged by inversion;
the conjugating peripheral matrix acts trivially on global coinvariants.
All boundary torsion classes used here have order two, so reversal signs
do not alter the six vanishing tests.  The implementation itself uses
actual left transport directly and requires no convention substitution.
"""
import sympy as S
from itertools import combinations
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy.polys.domains import ZZ
from fourfolds_family_survivors import family

def Z(M):return S.Matrix([[int(x) for x in row] for row in M.tolist()])
def snf(M):return tuple(X.to_Matrix() for X in smith_normal_decomp(DomainMatrix.from_Matrix(M).convert_to(ZZ)))
def kernel(M):
    D,U,V=snf(M);K=V[:,M.rank():]
    assert M*K==S.zeros(M.rows,K.cols)
    return K

def factors(M):
    D=smith_normal_form(M,domain=ZZ)
    return [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]

def wedge_map(M,q):
    rows=list(combinations(range(M.rows),q));cols=list(combinations(range(M.cols),q))
    return S.Matrix([[M.extract(i,j).det() for j in cols] for i in rows])

def parabolic_group(A,B):
    n=A.rows;I=S.eye(n)
    equations=S.Matrix.hstack(A-I,A*(B-I),-(A*B-I))
    K=kernel(equations)
    restriction=S.zeros(2*n,3*n)
    restriction[:n,:n]=A-I;restriction[n:,n:2*n]=B-I
    cocycles=hermite_normal_form(Z(restriction*K))
    delta=S.Matrix.vstack(A-I,B-I)
    coordinates=cocycles.gauss_jordan_solve(delta)[0]
    assert all(S.denom(x)==1 for x in coordinates)
    fs=factors(coordinates)
    return {'rank':cocycles.cols-coordinates.rank(),'torsion':[d for d in fs if d>1],
            'all_factors':fs}

def fixed_split(M,ell,m):
    fixed=kernel(M-S.eye(6));row=ell*fixed
    D,U,V=snf(row)
    if abs(D[0,0])!=1:return None
    coeff=V[:,0]*U[0,0]/D[0,0]
    u=fixed*coeff;H=kernel(ell);P=S.Matrix.hstack(u,H)
    assert abs(P.det())==1 and ell*u==S.ones(1,1)
    marked=P.inv()*M*P
    assert marked[0,0]==1 and marked[0,1:]==S.zeros(1,5) and marked[1:,0]==S.zeros(5,1)
    vertical=Z(marked[1:,1:])
    lam=kernel(vertical-S.eye(5))[:,0];phi=kernel(vertical.T-S.eye(5))[:,0].T
    height=abs(int((phi*lam)[0]))
    return {'u':u,'P':P,'D':vertical,'height':height,'expected':m}

def test_pair(M1,M2,verbose=True):
    M1,M2=Z(M1),Z(M2);I=S.eye(6)
    assert M1**5==I and M2**4==I
    x=S.Symbol('x')
    assert M1.charpoly(x).as_expr().expand()==S.expand((x-1)**2*S.cyclotomic_poly(5,x))
    assert M2.charpoly(x).as_expr().expand()==S.expand((x-1)**2*(x+1)**2*(x*x+1))
    N=(M1*M2).inv()-I
    assert N*N==S.zeros(6) and factors(N)==[1,1,1]
    global_hom=factors(S.Matrix.hstack(M1-I,M2-I))
    if global_hom!=[1]*5:return {'passes':False,'reason':'global homology coinvariants not free Z','smith':global_hom}
    ell=kernel(S.Matrix.vstack(M1.T-I,M2.T-I))[:,0].T
    splits=[fixed_split(M,ell,m) for M,m in ((M1,5),(M2,4))]
    if any(s is None or s['height']!=s['expected'] for s in splits):
        return {'passes':False,'reason':'finite fixed direction or suspension index','heights':[None if s is None else s['height'] for s in splits]}
    # Actual left cohomology transport, fixing the peripheral product convention.
    T1=Z(M1.inv().T);T2=Z(M2.inv().T);T0=Z((T1*T2).inv())
    G={};relations={};wedge={}
    for q in range(1,5):
        A=wedge_map(T1,q);B=wedge_map(T2,q);n=A.rows
        R=S.Matrix.hstack(A-S.eye(n),B-S.eye(n))
        DD,UU,VV=snf(R)
        assert R.rank()==n
        G[q]={'factors':[abs(int(DD[i,i])) for i in range(n)],'D':DD,'U':UU}
        relations[q]=R;wedge[q]=(A,B)
    def nonzero(q,v):
        a=G[q]['U']*v
        return any(int(a[i])%G[q]['factors'][i] for i in range(a.rows))
    def generates(q,columns):
        f=factors(S.Matrix.hstack(relations[q],*columns))
        return f==[1]*relations[q].rows
    cap={};vertical=splits[1]['D'];inclusion=splits[1]['P'].inv().T[:,1:]
    for q in range(2,6):
        E=wedge_map(vertical.T,q-1);DD,UU,VV=snf(E-S.eye(E.rows))
        tors=[i for i in range(E.rows) if abs(DD[i,i])>1]
        assert len(tors)==1 and abs(DD[tors[0],tors[0]])==2
        w=UU.inv()[:,tors[0]]
        assert sum((E**j*w for j in range(4)),S.zeros(E.rows,1))==S.zeros(E.rows,1)
        cap[q]=wedge_map(inclusion,q-1)*w
        assert not nonzero(q-1,2*cap[q])
    E=wedge_map(T0,3);DD,UU,VV=snf(E-S.eye(20))
    tors=[i for i in range(20) if abs(DD[i,i])>1]
    assert len(tors)==1 and abs(DD[tors[0],tors[0]])==2
    cusp=UU.inv()[:,tors[0]]
    assert not nonzero(3,2*cusp)
    P2=parabolic_group(*wedge[2]);P4=parabolic_group(*wedge[4])
    tests={'H3_21':generates(1,[cap[2]]),
           'H3_12':P2['rank']==0 and not P2['torsion'],
           'H3_03':bool(nonzero(2,cap[3])),
           'H5_23':generates(3,[cap[4],cusp]),
           'H5_14':P4['rank']==0 and not P4['torsion'],
           'H5_05':bool(nonzero(4,cap[5]))}
    result={'passes':all(tests.values()),'tests':tests,
            'global_coinvariants':{q:[d for d in G[q]['factors'] if d>1] for q in G},
            'parabolic2':P2,'parabolic4':P4,
            'cusp_image_nonzero':bool(nonzero(3,cusp)),
            'cap_images_nonzero':{q:bool(nonzero(q-1,cap[q])) for q in cap}}
    if verbose:print(result,flush=True)
    return result

if __name__=='__main__':
    for v in (0,1,2):
        A,B=family(v)
        print('PARAMETER',v,flush=True)
        # A,B are pullbacks; the function accepts homology, not pullback.
        result=test_pair(A.T,B.T)
        assert result['passes']==(v in (0,1))
    print('ALL FINITE ARITHMETIC TEST CERTIFICATES PASSED',flush=True)
