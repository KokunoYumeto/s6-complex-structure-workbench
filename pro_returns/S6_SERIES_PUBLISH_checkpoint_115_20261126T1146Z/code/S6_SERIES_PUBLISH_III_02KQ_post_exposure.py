#!/usr/bin/env python3
"""New post-release checks of the complete 02KQ auxiliary scope.

This does not import or rerun the frozen fresh program or any historical
KQ/KR code.  Constant four-period matrices are the released D.T6 marking,
with the other three matrices already derived before release.  Left and
right inverses are constructed by Bezout combinations of maximal-minor
adjugates, independently of the fresh Euclidean matrix algorithm.
"""
from functools import reduce
from itertools import combinations
from math import gcd
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

ROOT = Path(__file__).resolve().parents[1]
OWN = ROOT / 'agents/continuation6_iii_carriers'
I4 = s.eye(4)
e = [I4[:, i] for i in range(4)]
pairs = list(combinations(range(4), 2))


def wedge(T):
    return s.Matrix(6, 6, lambda i, j: T.extract(pairs[i], pairs[j]).det())


def smith(M):
    A = smith_normal_form(M, domain=ZZ)
    return [abs(int(A[i, i])) for i in range(min(A.shape))]


def left_inverse(K):
    """Bezout-combine adjugates of square row minors until LK=I."""
    rows, cols = K.shape
    L, d = s.zeros(cols, rows), 0
    for inds in combinations(range(rows), cols):
        Q = K.extract(inds, range(cols))
        a = int(Q.det(method='domain-ge'))
        if not a:
            continue
        u, v, g = map(int, s.gcdex(d, a))
        select = s.eye(rows).extract(inds, range(rows))
        L = u*L + v*Q.adjugate()*select
        d = g
        assert L*K == d*s.eye(cols)
        if d == 1:
            return L
    raise AssertionError(('nonprimitive columns', d))


def primitive_coordinates(q):
    """Five-vector completion by successive two-row Bezout rotations."""
    U = s.eye(5)
    for j in range(1, 5):
        a, b = int((U*q)[0]), int((U*q)[j])
        if not (a or b):
            continue
        u, v, d = map(int, s.gcdex(a, b))
        V = s.eye(5)
        V[0, 0], V[0, j] = u, v
        V[j, 0], V[j, j] = -b//d, a//d
        assert V.det() == 1
        U = V*U
    assert U*q == s.eye(5)[:, 0] and abs(U.det()) == 1
    H, E, r = U[1:, :], U.inv()[:, 1:], U[0, :]
    assert H*E == s.eye(4) and H*q == s.zeros(4, 1)
    assert E*H + q*r == s.eye(5)
    return H, E, r


def insert_block(M, row, col, block):
    M[row:row+block.rows, col:col+block.cols] = block


def encode(value):
    if isinstance(value, s.MatrixBase):
        return [[int(x) for x in row] for row in value.tolist()]
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, list):
        return [encode(v) for v in value]
    return value


params = [
    (1, 0, 0, 0, 0), (1, 0, 0, 0, 1), (1, 0, 0, 0, -1),
    (2, 1, 0, 0, 0), (4, 2, 0, 1, 0), (9, 0, 2, 3, 0),
    (10, -3, 4, 5, 0), (12, 3, 2, 5, 0),
    (6, 7, -5, 4, 1), (6, 7, -5, 4, -1),
    (18, 2, 3, 5, 6), (40, 4, 0, 5, 20),
    (60, 3, 0, 2, 30), (60, 3, 0, 2, -30),
    (84, 7, 0, 3, 42), (48, 0, 5, 2, 24),
]

all_maps = {}
print('New 02KQ post-exposure auxiliary computation; no historical code or output input.')
for os, p, b in [(46, 4, 2), (50, 12, 1)]:
    j = 2*b-1
    T1 = (s.Matrix([[-1,-3,0,1],[0,-1,0,1],[-4,-8,1,3],[0,0,0,1]])
          if os == 46 else
          s.Matrix([[-1,-1,0,-1],[0,-1,0,1],[-12,-24,1,3],[0,0,0,1]]))
    T2 = (I4+s.eye(4)[:,0]*s.eye(4)[1,:] if os == 46 else
          s.Matrix([[1,3,0,-2],[0,1,0,0],[0,24,1,-16],[0,0,0,1]]))
    T3 = s.Matrix([[2,1,0,0],[-1,0,0,0],[0,0,1,1],[0,0,0,1]])
    T4 = s.Matrix([[0,1,0,-1],[-1,2,0,-1],[-p,p,1,-p],[0,0,0,1]])
    Ts = [T1, T2, T3, T4]
    assert reduce(lambda A, B: A*B, Ts, I4) == I4
    N = T1*T1-I4
    assert N == j*(e[0]+(p//2)*e[2])*s.Matrix([[0,2,0,-1]])
    assert N.rank() == 1 and N*N == s.zeros(4)
    assert smith(T1-I4) == [1,1,0,0]
    assert smith(wedge(T1)-s.eye(6)) == [1,1,1,1,0,0]
    product_T = s.diag(s.Matrix([[-1,-j],[0,-1]]),s.eye(2))
    assert smith(product_T-I4) == [1,4,0,0]

    # The actual affine D graph, its orbit invariants and PL intersection map.
    r = b+1
    G = -2*s.eye(4+2*b)
    edges = [(0,4),(1,4),(2,3+2*b),(3,3+2*b)]
    edges += [(4+k,5+k) for k in range(2*b-1)]
    for x, y in edges:
        G[x,y] = G[y,x] = 1
    orbits = [[0,1,2,3]] + [[4+k,3+2*b-k] for k in range(b)]
    Inv, Sec = s.zeros(4+2*b,r), s.zeros(4+2*b,r)
    for k, orb in enumerate(orbits):
        for c in orb:
            Inv[c,k] = 1
        Sec[orb[0],k] = 1
    pl = Inv.T*G*Sec
    boundary = s.Matrix([[1]+[2]*b])
    assert pl*s.ones(r,1) == s.zeros(r,1)
    assert boundary*pl == s.zeros(1,r)
    pl_basis = s.Matrix.hstack(s.eye(r)[:,0],pl[:,1:])
    assert abs(pl_basis.det()) == 1
    assert pl_basis.inv()[0,:] == boundary
    assert pl_basis*pl_basis.inv() == s.eye(r)

    ell = s.Matrix([-1 if os == 46 else -3,2,0,4])
    H2 = (I4 if os == 46 else
          s.Matrix.hstack(s.Matrix([1,0,8,0]),s.Matrix([0,1,0,1]),e[2],s.Matrix([0,2,0,3])))
    H3 = s.diag(s.Matrix([[1,0],[-1,1]]),s.eye(2))
    H4 = s.Matrix.hstack(s.Matrix([1,1,p,0]),e[1],e[2],s.Matrix([0,1,0,1]))
    Fs = [s.Matrix.hstack(e[2],ell), H2[:,[0,2,3]],
          H3[:,[0,2]], H4[:,[0,2,3]]]
    D = s.Matrix.hstack(s.zeros(4),T1-I4,T2-I4,T3-I4)
    js = [s.zeros(16,4) for _ in range(5)]
    for i in range(4):
        js[i][4*i:4*i+4,:] = I4
    js[4] = -s.Matrix.vstack(T1*T2*T3,T2*T3,T3,I4)
    assert D*js[4] == I4-T4.inv()
    B = s.Matrix.hstack(*[js[i+1]*Fs[i] for i in range(4)])
    K = s.Matrix.hstack(B,js[0]*e[0],js[0]*e[1],js[0]*e[3])
    L = left_inverse(K)
    C = left_inverse(D[:3,:].T).T
    assert D*K == s.zeros(4,13)
    assert D[:3,:]*C == s.eye(3)
    assert K*L*(s.eye(16)-C*D[:3,:]) == s.eye(16)-C*D[:3,:]
    assert L[10:,:]*js[0] == s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1]])
    Ra = [i for i in range(16) if i not in [11,12,15]]
    Rb = [i for i in range(16) if i not in [9,13,15]]
    Pa, Pb = s.eye(16).extract(Ra,range(16)),s.eye(16).extract(Rb,range(16))
    Ka,Kb = Pa*K,Pb*K
    printed_L = (Kb.adjugate()*Pb if os == 46 else
                 Ka.adjugate()*Pa-Kb.adjugate()*Pb)
    assert printed_L == L
    assert Kb.det() == (1 if os == 46 else -3)
    if os == 50:
        assert Ka.det() == -2
    B2 = s.Matrix.hstack(s.zeros(6),*[wedge(T)-s.eye(6) for T in Ts[:3]])
    Z = s.zeros(24,5)
    zrows = ({9:[-5,0,2,0,2],10:[-9,-1,6,1,3],11:[2,0,-1,0,-1],
              12:[12,2,-11,-3,-4],21:[-4,0,2,0,1]} if os == 46 else
             {8:[-94,-2,68,1,63],9:[3,0,-2,0,-2],10:[49,1,-38,-1,-35],
              12:[-94,-2,68,1,63],17:[2,0,-1,0,-1],21:[0,0,0,0,-1]})
    for row,values in zrows.items():
        Z[row-1,:] = s.Matrix([values])
    F = s.eye(6)[:,:5]; F[5,0] = p
    assert B2*Z == F and abs(s.Matrix.hstack(-s.eye(6)[:,5],F).det()) == 1
    omega = s.Matrix([[p,0,0,0,0,-1]])
    summary = {'N':N,'PL_intersection':pl,'PL_basis':pl_basis,
               'PL_basis_inverse':pl_basis.inv(),'PL_boundary':boundary,
               'K':K,'L':L,'C':C,'printed_Z':Z,'log_maps':[]}
    print('\nOS',os,': N=A_star^2-I =',N.tolist())
    print('actual/product H1 relation Smith: [1,1,0,0] / [1,4,0,0]')
    print('PL component-to-relative matrix:',pl.tolist(),'; boundary row:',boundary.tolist())
    print('Independent adjugate/Bezout inverses give LK=I13 and D0 C=I3.')
    print('Printed minor-adjugate formula and all printed exterior-cylinder rows verified.')

    for m,a,bb,c,n in params:
        assert reduce(gcd,[m,a,bb,c,n]) == 1
        v, q = s.Matrix([a,bb,c,n]), s.Matrix([-a,-bb,-c,-n,m])
        H, E, rq = primitive_coordinates(q)
        # Full 19-by-19 Mayer--Vietoris map, V first, local groups second.
        pieces = [(5,4,I4,H),
                  (3,2,s.Matrix.hstack(e[2],e[3]),s.eye(2)),
                  (4,3,H2[:,[1,2,3]],s.eye(3)),
                  (3,2,H3[:,[1,3]],s.eye(2)),
                  (4,3,H4[:,[1,2,3]],s.eye(3))]
        MV, S = s.zeros(19), s.zeros(19)
        col, localrow, localcol = 0,5,0
        for i,(d,k,sections,local) in enumerate(pieces):
            for f in range(d-1):
                MV[0,col+f] = sections[3,f]
            if i < 4:
                MV[1+i,col+d-1] = 1
            else:
                MV[1:5,col+d-1] = -s.ones(4,1)
            if i == 0:
                insert_block(MV,localrow,col,-H)
                S[col:col+5,localcol:localcol+4] = E
                S[col:col+5,14+i] = q
            else:
                insert_block(MV,localrow,col,-s.eye(k))
                S[col:col+k,localcol:localcol+k] = s.eye(k)
                S[col+d-1,14+i] = 1
            col,localrow,localcol = col+d,localrow+k,localcol+k
        assert (col,localrow,localcol) == (19,19,14)
        assert abs(S.det()) == 1
        MS = MV*S
        assert MS[5:,:14] == -s.eye(14) and MS[5:,14:] == s.zeros(14,5)
        A = MS[:5,:14]
        W = s.eye(19); W[:5,5:] = A
        Wi = s.eye(19); Wi[:5,5:] = -A
        assert W*Wi == s.eye(19)
        reduced = W*MV*S
        G5 = s.Matrix([[-n,0,0,0,0],[m,0,0,0,-1],
                       [0,1,0,0,-1],[0,0,1,0,-1],[0,0,0,1,-1]])
        assert reduced == s.Matrix.vstack(s.Matrix.hstack(s.zeros(5,14),G5),
                                         s.Matrix.hstack(-s.eye(14),s.zeros(14,5)))
        assert G5.det() == -n and abs(MV.det()) == abs(n)
        if n == 0:
            gen = s.Matrix([1,m,m,m,m])
            full_gen = S*s.Matrix.vstack(s.zeros(14,1),gen)
            assert MV*full_gen == s.zeros(19,1)
            assert reduce(gcd,map(int,full_gen)) == 1
        # Full 14-by-15 reduced H2 map BEFORE eliminating ten normal sweeps.
        R = s.Matrix([[-p*bb,p*a,n,-c,0],[m,0,0,0,a],
                      [0,m,0,0,bb],[0,0,0,m,n]])
        full = s.Matrix.vstack(s.zeros(1,15),s.Matrix.hstack(s.eye(13)[:,:10],s.zeros(13,5)))
        full[0,10:] = R[0,:]
        full[1:,10:14] = m*L*js[0]
        full[1:,14] = L*js[0]*v
        low = full[1:11,10:]
        inverse_source = s.eye(15); inverse_source[:10,10:] = low
        source = s.eye(15); source[:10,10:] = -low
        assert source*inverse_source == s.eye(15)
        rf = full*source
        assert rf[1:11,:10] == s.eye(10) and rf[1:11,10:] == s.zeros(10,5)
        assert rf.extract([0,11,12,13],range(10,15)) == R
        assert full*s.Matrix.vstack(s.zeros(10,1),q) == s.zeros(14,1)
        t = gcd(m,n,a,bb)*gcd(m,n,p,c)
        expected = [1]*11+[t,m,(m*abs(n)//t if n else 0)]
        assert smith(full) == expected
        assert smith(MV) == [1]*18+([abs(n)] if n else [0])
        print('log',(m,a,bb,c,n),'H1 Smith',[1]*18+[abs(n)],
              'H2 14x15 Smith',expected)
        if (m,a,bb,c,n) in [params[0],params[8],params[12]]:
            summary['log_maps'].append(dict(parameters=[m,a,bb,c,n],
                H=H,E=E,r=rq,MV=MV,source=S,source_inverse=S.inv(),
                target=W,target_inverse=Wi,normal=G5,
                full_H2=full,H2_source=source,H2_source_inverse=inverse_source))
    all_maps[str(os)] = summary

path = OWN/'S6_SERIES_PUBLISH_III_02KQ_post_exposure_maps.json'
path.write_text(json.dumps(encode(all_maps),indent=2)+'\n')
print('\nAll 32 full H1/H2 maps, inverse reductions, star powers, boundary groups and PL maps passed.')
