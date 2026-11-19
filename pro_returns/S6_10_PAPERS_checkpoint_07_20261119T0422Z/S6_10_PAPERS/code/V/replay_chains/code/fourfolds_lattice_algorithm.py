"""A finite exact stable-lattice algorithm for one rational rank-five pair.

The trace-dual bound makes order discovery terminate even when the rational
pair preserves no lattice. When an order exists, every primitive-content
stable lattice is contained in a finite interval c*Lambda0 <= Lambda <=
Lambda0. This file prints exact order/conductor certificates for v=0,1,2.
It does not infer conclusions for other parameters from those three runs.
"""
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.domains import ZZ
from math import gcd, lcm, prod
from functools import reduce
from itertools import combinations, product

def vec(M): return S.Matrix(list(M))
def mat(v,n): return S.Matrix(n,n,list(v))
def integral(M): return all(S.denom(x)==1 for x in M)
def hnf(M,det_basis=None):
    d=lcm(*(int(S.denom(x)) for x in M))
    integer=(d*M).applyfunc(int)
    if det_basis is not None:
        # A known contained full-rank sublattice supplies a determinant
        # multiple for the modular HNF algorithm, avoiding coefficient swell.
        determinant=abs(S.Integer(d)**M.rows*det_basis)
        assert S.denom(determinant)==1 and determinant>0
        return hermite_normal_form(integer,D=ZZ(int(determinant)))/d
    return hermite_normal_form(integer)/d

def cyclic_words(A,C,dual=False):
    n=A.rows
    e=(A.T-S.eye(n)).nullspace()[0].T if dual else (A-S.eye(n)).nullspace()[0]
    selected=[S.eye(n)];values=[e];lengths=[0];cursor=0
    while len(values)<n:
        assert cursor<len(selected), 'the pair is not rationally irreducible'
        g=selected[cursor]
        for T in (A,C):
            h=g*T if dual else T*g
            w=e*h if dual else h*e
            rank=S.Matrix.vstack(*values,w).rank() if dual else S.Matrix.hstack(*values,w).rank()
            if rank>len(values):
                selected.append(h);values.append(w);lengths.append(lengths[cursor]+1)
        cursor+=1
    assert max(lengths)<=n-1
    return selected,lengths

def order_and_conductor(A,C,verbose=True):
    n=A.rows
    G,gl=cyclic_words(A,C);H,hl=cyclic_words(A,C,True)
    P=sum((A**j for j in range(5)),S.zeros(n))
    generators=[g*P*h for g in G for h in H]
    B0=S.Matrix.hstack(*(vec(T) for T in generators))
    # The rank-one tensor factorization avoids a slow 25x25 rational
    # determinant and certifies the same determinant by two 5x5 ones.
    e=(A-S.eye(n)).nullspace()[0]
    phi=(A.T-S.eye(n)).nullspace()[0].T
    entry=next((i,j) for i in range(n) for j in range(n) if e[i]*phi[j])
    scalar=P[entry[0],entry[1]]/(e[entry[0]]*phi[entry[1]])
    assert P==scalar*e*phi
    GV=S.Matrix.hstack(*(g*e for g in G))
    HV=S.Matrix.vstack(*(phi*h for h in H))
    det_tensor=scalar**(n*n)*GV.det()**n*HV.det()**n
    assert det_tensor!=0
    trace_product=lambda X,Y:sum(X[i,j]*Y[j,i] for i in range(n) for j in range(n))
    Gram=S.Matrix(n*n,n*n,lambda i,j:trace_product(generators[i],generators[j]))
    if not integral(Gram): return {'stable_lattice':False,'reason':'nonintegral initial trace'}
    assert S.denom(det_tensor**2)==1
    index=abs(int(det_tensor**2))
    assert index>=1
    bound=index.bit_length()-1
    def in_dual(Z):
        return all(S.denom(trace_product(Z,T))==1 for T in generators)
    L=hnf(B0.row_join(vec(S.eye(n))),det_tensor)
    rounds=0
    while True:
        basis=[mat(L[:,j],n) for j in range(n*n)]
        if not all(in_dual(T) for T in basis):
            return {'stable_lattice':False,'reason':'left trace-dual bound','rounds':rounds}
        candidates=basis+[A*T for T in basis]+[C*T for T in basis]
        det_L=prod(L[i,i] for i in range(n*n))
        L2=hnf(S.Matrix.hstack(*(vec(T) for T in candidates)),det_L)
        if L2==L: break
        L=L2;rounds+=1
        assert rounds<=bound+1
    basis=[mat(L[:,j],n) for j in range(n*n)]
    # This stable lattice contains Z^n because the order is unital.
    Lambda=hnf(S.Matrix.hstack(*basis))
    transformed=[Lambda.inv()*T*Lambda for T in basis]
    assert all(integral(T) for T in transformed)
    coordinate_order=S.Matrix.hstack(*(vec(T) for T in transformed))
    Sn=smith_normal_form(coordinate_order,domain=ZZ)
    factors=[abs(int(Sn[i,i])) for i in range(n*n)]
    conductor=factors[-1]
    assert conductor>0
    assert integral(coordinate_order.inv()*conductor*S.eye(n*n))
    result={'stable_lattice':True,'word_length_bounds':(max(gl),max(hl)),
            'trace_dual_index':index,'strict_round_bound':bound,
            'actual_rounds':rounds,'order_smith':factors,'conductor':conductor,
            'lattice_basis':Lambda,'order_basis':L}
    if verbose:
        print({k:v for k,v in result.items() if k not in ('lattice_basis','order_basis')},flush=True)
        print('stable lattice basis',Lambda.tolist(),flush=True)
    return result

def subspaces_fp(n,p):
    """Every subspace, once, in reduced column-echelon coordinates."""
    for k in range(n+1):
        for pivots in combinations(range(n),k):
            free=[(i,j) for i,q in enumerate(pivots)
                  for j in range(q+1,n) if j not in pivots]
            for values in product(range(p),repeat=len(free)):
                U=S.zeros(n,k)
                for i,q in enumerate(pivots): U[q,i]=1
                for (i,j),value in zip(free,values): U[j,i]=value
                yield pivots,U

def fp_contains(v,pivots,U,p):
    v=[int(z)%p for z in v]
    for i,q in enumerate(pivots):
        a=v[q]
        if a:v=[(x-a*int(U[j,i]))%p for j,x in enumerate(v)]
    return not any(v)

def finite_stable_lattices(A,C,conductor):
    """All content-one stable lattices between c Z^n and Z^n.

    A,C must be integral in the chosen stable basis, and c M_n(Z) must
    belong to their generated order. For each p^a||c, the exhaustive
    search has at most (#subspaces of F_p^n)^a branches before deduplication.
    """
    n=A.rows
    assert integral(A) and integral(C) and conductor>=1
    local_lists=[]
    for pp,aa in S.factorint(conductor).items():
        p,a=int(pp),int(aa)
        spaces=list(subspaces_fp(n,p))
        lower=p**a*S.eye(n)
        current={tuple(S.eye(n)):S.eye(n)}
        for depth in range(a):
            following={}
            for H in current.values():
                AH=H.inv()*A*H;CH=H.inv()*C*H
                assert integral(AH) and integral(CH)
                for pivots,U in spaces:
                    if not all(fp_contains(M*U[:,j],pivots,U,p)
                               for M in (AH,CH) for j in range(U.cols)):
                        continue
                    K=hnf(H*hnf(U.row_join(p*S.eye(n))))
                    if integral(K.inv()*lower): following[tuple(K)]=K
            current=following
        local_lists.append([H for H in current.values()
                            if reduce(gcd,(abs(int(x)) for x in H),0)==1])
    candidates=[S.eye(n)]
    for local in local_lists:
        following=[]
        for H in candidates:
            for K in local:
                dual_sum=hnf(H.inv().T.row_join(K.inv().T))
                following.append(hnf(dual_sum.inv().T))
        candidates=following
    for H in candidates:
        assert integral(H) and integral(H.inv()*conductor*S.eye(n))
        assert integral(H.inv()*A*H) and integral(H.inv()*C*H)
        assert reduce(gcd,(abs(int(x)) for x in H),0)==1
    return candidates

if __name__=='__main__':
    A=S.zeros(5)
    for j in range(5):A[(j+1)%5,j]=1
    for v in (0,1,2):
        q=v*v-v+1
        X=S.eye(5)[:,0].row_join(S.eye(5)[:,2]+v*S.eye(5)[:,4])
        Y=S.Matrix([[0,-q,-v*v,-1,v],[0,1-v*q,-v*q,v*v-v,q]])
        C=(S.eye(5)+X*Y)*A
        print('parameter',v,flush=True)
        result=order_and_conductor(A,C)
        assert result['stable_lattice']
    # A genuine rational finite-order pair with no stable integral lattice.
    J=S.Matrix([[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]])
    A=S.diag(1,J);X=S.Matrix([[0,1],[1,0],[0,1],[0,0],[0,2]])
    ys=S.symbols('y0:10');Y=S.Matrix(2,5,ys);R=(A+S.eye(5)).inv()
    equations=list(Y*X)+list(Y*R*X-S.eye(2))+[
        S.trace(Y*A*X)+1,S.trace(Y*A.inv()*X)-1]
    E,b=S.linear_eq_to_matrix(equations,ys)
    Y=S.Matrix(2,5,list(E.inv()*b));C=(S.eye(5)+X*Y)*A
    assert A**5==S.eye(5) and C**4==S.eye(5)
    assert S.trace(A*A*C*C)==S.Rational(127,43)
    result=order_and_conductor(A,C)
    assert not result['stable_lattice']
    print('nonintegral example [1:0:2], trace A^2C^2=127/43:',result,flush=True)
    print('ALL ORDER AND CONDUCTOR CERTIFICATES PASSED',flush=True)
