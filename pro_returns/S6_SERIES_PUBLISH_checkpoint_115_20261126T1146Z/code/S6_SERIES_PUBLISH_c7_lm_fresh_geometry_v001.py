#!/usr/bin/env python3
"""Fresh LM geometry, integral chains and full coefficient calculation.

Reads defining periods only. The new calculation uses integral Cartier
gradient jumps, a retained column-Euclid relation section, and symbolic
all-parameter Thom identities. It reads no LM original or historical work.
"""
from hashlib import sha256
from itertools import combinations
from math import gcd
from pathlib import Path
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/'agents/continuation7_iii_residual_twenty_root'
RAW = ROOT/'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
EXPECTED = '6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522'
assert sha256(RAW.read_bytes()).hexdigest() == EXPECTED
raw = json.loads(RAW.read_text())
E, J = S.eye(4), S.Matrix([[0,1],[-1,0]])
delta, gamma = E[:,2], E[:,3]
PAIRS = list(combinations(range(4),2))


def integers(M):
    assert all(x.is_Integer for x in M)
    return [[int(x) for x in row] for row in M.tolist()]


def vec(M):
    assert all(x.is_Integer for x in M)
    return [int(x) for x in M]


def egcd(a,b):
    a,b = int(a),int(b)
    aa,bb,u,v,uu,vv = abs(a),abs(b),1,0,0,1
    while bb:
        q = aa//bb
        aa,bb,u,v,uu,vv = bb,aa-q*bb,uu,vv,u-q*uu,v-q*vv
    u *= 1 if a >= 0 else -1
    v *= 1 if b >= 0 else -1
    assert u*a+v*b == aa
    return aa,u,v


def wedge(u,v):
    return S.Matrix([u[i]*v[j]-u[j]*v[i] for i,j in PAIRS])


def exterior(T):
    return S.Matrix.hstack(*(wedge(T[:,i],T[:,j]) for i,j in PAIRS))


def relation_section(A):
    """Track integral row/column Euclid to U A V=[I,0]."""
    M,U,V = A.copy(),S.eye(A.rows),S.eye(A.cols)
    for i in range(A.rows):
        j = next(j for j in range(i,A.cols) if M[i,j])
        M.col_swap(i,j);V.col_swap(i,j)
        for j in range(i+1,A.cols):
            if not M[i,j]:
                continue
            p,q = int(M[i,i]),int(M[i,j])
            g,u,v = egcd(p,q)
            c,d = M[:,i].copy(),M[:,j].copy()
            vc,vd = V[:,i].copy(),V[:,j].copy()
            M[:,i],M[:,j] = u*c+v*d,(-q//g)*c+(p//g)*d
            V[:,i],V[:,j] = u*vc+v*vd,(-q//g)*vc+(p//g)*vd
        if M[i,i] == -1:
            M[:,i] = -M[:,i];V[:,i] = -V[:,i]
        assert M[i,i] == 1, ('nonunit relation image',i,M[i,i])
        for j in range(i+1,A.rows):
            q = M[j,i]
            M[j,:] = M[j,:]-q*M[i,:]
            U[j,:] = U[j,:]-q*U[i,:]
    assert M == S.eye(A.rows).row_join(S.zeros(A.rows,A.cols-A.rows))
    assert U*A*V == M and abs(U.det()) == abs(V.det()) == 1
    R = V[:,:A.rows]*U
    assert A*R == S.eye(A.rows)
    assert U.inv()*U == S.eye(A.rows) and V.inv()*V == S.eye(A.cols)
    return R,U,V


def rank_period(B,G):
    D = B-S.eye(2)
    w = next(D[:,j] for j in range(2) if D[:,j] != S.zeros(2,1))
    u = w/gcd(int(w[0]),int(w[1]))
    if next(x for x in u if x) < 0:
        u = -u
    outer = u*u.T*J
    nu = next(D[i,j]/outer[i,j] for i in range(2) for j in range(2) if outer[i,j])
    kappa = next(G[i]/u[i] for i in range(2) if u[i])
    assert nu.is_Integer and kappa.is_Integer and nu > 0
    assert D == nu*outer and G == kappa*u
    one,p,q = egcd(u[0],u[1]);assert one == 1
    r = S.Matrix([-q,p])
    assert S.Matrix.hstack(u,r).det() == 1
    return u,r,int(nu),int(kappa)


def gradient(K,triangle):
    T = S.Matrix([[x,y,1] for x,y in triangle])
    values = S.Matrix([(K[0,0]*x*x+2*K[0,1]*x*y+K[1,1]*y*y-x)/2
                       for x,y in triangle])
    assert abs(T.det()) == 1
    return (T.inv()*values)[:2,0]


def wall_degrees(K):
    a = gradient(K,[(0,0),(0,1),(1,0)])-gradient(K,[(0,0),(0,1),(-1,1)])
    b = gradient(K,[(0,0),(1,0),(0,1)])-gradient(K,[(0,0),(1,0),(1,-1)])
    c = gradient(K,[(1,0),(0,1),(1,1)])-gradient(K,[(1,0),(0,1),(0,0)])
    assert a[1] == b[0] == 0 and c[0] == c[1]
    return [a[0],b[1],c[0]]


print('RAW_SHA256',EXPECTED)
records = []
cases = [(45,'II',1,8,[2,3]),(55,'II',5,4,[3]),
         (55,'default',1,20,[2,3,4]),(55,'II',1,20,[3])]
for os,name,a,b,zeros in cases:
    profile = next(r for r in raw['rows'] if r['OS'] == os and r['profile'] == name)
    for zero in zeros:
        Omega = S.Matrix([[a,0,0,0,0,-b]])
        alt = S.Matrix([[0,a,0,0],[-a,0,0,0],[0,0,0,-b],[0,0,b,0]])
        local,returns,crit,original_extra = [],[],[],S.zeros(6,1)
        for i,(kind,bb,gg) in enumerate(zip(profile['fibers'],profile['elliptic_matrices'],profile['generator_section_cocycle'])):
            B,G = S.Matrix(bb),S.Matrix(gg)
            beta = -G.T*J*B
            T = S.eye(4);T[:2,:2] = B;T[:2,3] = b*G;T[2,:2] = a*beta
            if kind == 'II':
                z = (B-S.eye(2)).inv()*G
                T[2,3] = a*b*(beta*z)[0]
                ell = S.Matrix([-b*z[0],-b*z[1],0,1])
                xi = a*beta*(B-S.eye(2)).inv()
                H = S.Matrix.hstack(E[:,0]+xi[0]*delta,E[:,1]+xi[1]*delta,delta,ell)
                expected = S.eye(4);expected[:2,:2] = B
                assert H.det() == 1 and H.inv()*T*H == expected
                assert (B-S.eye(2)).det() == 1 and (B.inv()-S.eye(2)).det() == 1
                original_extra = 2*wedge(delta,ell)
                assert (Omega*original_extra)[0] == -2*b
                crit.append(S.zeros(6,1))
                local.append(dict(index=i,kind=kind,H=integers(H),H_inverse=integers(H.inv()),
                                  original_critical=vec(original_extra),degree_original=-2*b,
                                  moving_return=integers(B),moving_minus_identity_inverse=integers((B-S.eye(2)).inv())))
            else:
                u0,r0,nu,kappa = rank_period(B,G)
                u,r = S.Matrix([*u0,0,0]),S.Matrix([*r0,0,0])
                T[2,3] = S.Rational(int(i == zero)-a*b*kappa*kappa,nu)
                if i == zero:
                    assert nu == 1
                    C = S.Matrix([[1,b*kappa],[-a*kappa,1-a*b*kappa*kappa]])
                    short = S.Matrix.hstack(u,delta)*C
                    H = S.Matrix.hstack(short[:,0],r,short[:,1],gamma)
                    expected = S.eye(4);expected[0,1] = expected[2,3] = 1
                    K = C.T*S.diag(a,-b)
                    values = wall_degrees(K)
                    v = wedge(H[:,0],H[:,1])+wedge(H[:,1],H[:,2])+wedge(H[:,2],H[:,3])
                    assert sum(values) == (Omega*v)[0] == a-a*b*kappa-b+a*b*b*kappa*kappa
                    cusp = dict(index=i,kappa=kappa,C=integers(C),C_inverse=integers(C.inv()),
                                K=integers(K),wall_degrees=[int(x) for x in values],
                                character=int(S.Rational(b,2)*(a*kappa*(b*kappa-1)-1)),
                                degree=a*(1-b*kappa))
                    extra = cusp
                else:
                    d0 = gcd(nu,a*kappa)
                    l = S.Rational(nu,d0)*u-S.Rational(a*kappa,d0)*delta
                    one,p,q = egcd(nu//d0,-a*kappa//d0);assert one == 1
                    residual = -q*u+p*delta
                    f2 = S.Rational(b*kappa*d0,nu);assert f2.is_Integer
                    one,p,q = egcd(d0,f2);assert one == 1
                    long1,long2 = p*r+q*gamma,-f2*r+d0*gamma
                    H = S.Matrix.hstack(l,long1,residual,long2)
                    expected = S.eye(4);expected[0,1] = 1
                    v = wedge(residual,long2)
                    assert (Omega*v)[0] == -S.Rational(b*d0*d0,nu)
                    extra = dict(nu=nu,kappa=kappa,d0=d0,isotropy=nu//d0)
                assert H.det() == 1 and H.inv()*T*H == expected
                crit.append(v)
                local.append(dict(index=i,kind=kind,H=integers(H),H_inverse=integers(H.inv()),
                                  critical=vec(v),degree=int((Omega*v)[0]),**extra))
            assert all(x.is_Integer for x in T) and T.T*alt*T == alt and T*delta == delta
            returns.append(T)
        product = S.eye(4)
        for T in returns:
            product *= T
        assert product == S.eye(4)
        one,aa,bb = egcd(a,-b);assert one == 1
        F = S.zeros(6);F[0,0],F[5,0],F[0,1],F[5,1] = aa,bb,b,a
        for j,i in enumerate([1,2,3,4],2):
            F[i,j] = 1
        assert abs(F.det()) == 1 and F.inv()[0,:] == Omega
        R = S.Matrix.hstack(*(exterior(T)-S.eye(6) for T in returns))
        M = F.inv()*R;assert M[0,:] == S.zeros(1,R.cols)
        section,U,V = relation_section(M[1:,:])
        variants = []
        for original in ([False,True] if name == 'II' else [False]):
            total = sum(crit,S.zeros(6,1))+(original_extra if original else S.zeros(6,1))
            q = int((Omega*total)[0]);assert q%2 == 0
            difference = total-q*F[:,0]
            chain = section*(F.inv()*difference)[1:,0]
            assert R*chain == difference
            P,lam = (-q//2)%b,(-q)%b
            assert 2*P%b == lam
            variants.append(dict(original_II=original,total=vec(total),q=q,P=P,
                                 lambda_value=lam,exterior_chain=vec(chain)))
        coefficients = []
        for modulus in ([4,5] if b == 20 else [b]):
            nodes = [r for r in local if r.get('isotropy',1)%gcd(modulus,2 if modulus%2 == 0 else 5) == 0]
            assert len(nodes) == 1
            node = nodes[0];assert node['nu'] == modulus and node['d0'] == 1
            t = pow((a*node['kappa'])%modulus,-1,modulus)
            qparity = t%2
            character_E = S.Rational(modulus,2)*(qparity-a*t)
            assert character_E.is_Integer and int(character_E)%modulus == 0
            degree_E = -b//modulus
            h = S.Symbol('h',integer=True)
            numerator = S.expand(-3*(t*t*cusp['degree']*(cusp['character']+h)**2+degree_E*h*h))
            coeffs = [int(x)%modulus for x in S.Poly(numerator,h).all_coeffs()]
            assert not any(coeffs)
            lam = (-cusp['degree']-degree_E)%modulus
            assert all(v['lambda_value']%modulus == lam for v in variants)
            coefficients.append(dict(modulus=modulus,node=node['index'],normal_weight=t,
                character_C=cusp['character']%modulus,character_E=int(character_E)%modulus,
                degree_C=cusp['degree'],degree_E=degree_E,
                cube_numerator=str(numerator),coefficients_modulus=coeffs,lambda_value=lam))
        record = dict(OS=os,profile=name,a=a,b=b,zero=zero,monodromies=[integers(T) for T in returns],
                      fibre_basis=integers(F),fibre_inverse=integers(F.inv()),
                      relation_matrix=integers(R),relation_section=integers(section),
                      euclid_left=integers(U),euclid_right=integers(V),
                      local=local,variants=variants,coefficient_checks=coefficients)
        records.append(record)
        print('ROW',os,name,a,b,zero,'LOCAL_DEGREES',[r.get('degree',0) for r in local])
        for v in variants:
            print('  VARIANT original_II',v['original_II'],'q',v['q'],'P',v['P'],'lambda',v['lambda_value'])
        for c in coefficients:
            print('  FULL_COEFFICIENT',c)
        print('  PASS all period inverses; integral Cartier gradients; full Euclid relation section; actual critical chains')

m,e,r,b = S.symbols('m e r b',integer=True)
for sigma in [-1,1]:
    n = m*e+sigma
    C1,C2,C3,G = S.Matrix([b*n,m,0]),S.Matrix([-b*r,0,m]),S.Matrix([0,r,n]),S.Matrix([b*e,1,0])
    E1,E2,E3 = sigma*(C1-m*G),G,sigma*(C3-r*G-e*C2)
    assert (E1-S.Matrix([b,0,0])).applyfunc(S.expand) == S.zeros(3,1)
    assert (E3-S.Matrix([0,0,1])).applyfunc(S.expand) == S.zeros(3,1)
    for lhs,rhs in [(C1,sigma*E1+m*E2),(C2,-r*E1+m*E3),(C3,-e*r*E1+r*E2+n*E3)]:
        assert (lhs-rhs).applyfunc(S.expand) == S.zeros(3,1)
    print('ALL_INTEGER_THOM_IDENTITIES sigma',sigma,'PASS')
for x in range(20):
    a4,a5 = x%4,(4*x)%5
    assert (5*a4+4*a5)%20 == x
for a4 in range(4):
    for a5 in range(5):
        x = (5*a4+4*a5)%20
        assert (x%4,(4*x)%5) == (a4,a5)
print('FULL_CRT_MARKING (x4,x5)->5*x4+4*x5; inverse x->(x mod4,4*x mod5) PASS')
assert len(records) == 7 and sum(len(r['variants']) for r in records) == 11
OUT = LANE/'S6_SERIES_PUBLISH_III_02LM_fresh_geometry_v001.json'
with OUT.open('x') as stream:
    json.dump(dict(raw_sha256=EXPECTED,scope='fresh defining-period computation',rows=records),stream,indent=2)
    stream.write('\n')
saved = json.loads(OUT.read_text())
assert saved['rows'] == records
print('ROWS',len(records),'PATTERNS',sum(len(r['variants']) for r in records))
print('DATA_SHA256',sha256(OUT.read_bytes()).hexdigest())
print('SCOPE exact identities and integral maps; manifold framing supplied by the complete fresh proof')
