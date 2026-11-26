#!/usr/bin/env python3
"""Fresh L7/L8 calculation from the marked 21-profile fixture.

No target proof, historical target program/table, or completed pattern data
is read.  The natural component criterion is the admitted KX theorem.
All Smith maps below are verified with both inverses; these are auxiliary
computations for the separate geometric proof, not substitutes for it.
"""
from __future__ import annotations
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from functools import reduce
from itertools import combinations, product
from math import gcd, lcm
from pathlib import Path
import hashlib
import json
import re
import sympy as S
from sympy.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'agents/continuation7_iii_all_original'
RAW = ROOT / 'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
PREFIX = 'S6_SERIES_PUBLISH_III_all_original'
J = S.Matrix([[0, 1], [-1, 0]])
DELTA = S.Matrix([0, 0, 1, 0])
PAIRS = list(combinations(range(4), 2))


def entries(M):
    return [[int(M[i, j]) if M[i, j].q == 1 else str(M[i, j])
             for j in range(M.cols)] for i in range(M.rows)]


def integral(M):
    assert all(x.q == 1 for x in M), M
    return M


def smith(M):
    D, U, V = smith_normal_decomp(M, domain=S.ZZ)
    for i in range(min(D.shape)):
        if D[i,i] < 0:
            D[i,:] = -D[i,:]
            U[i,:] = -U[i,:]
    Ui, Vi = integral(U.inv()), integral(V.inv())
    assert U*M*V == D
    assert Ui*D*Vi == M
    assert U*Ui == Ui*U == S.eye(U.rows)
    assert V*Vi == Vi*V == S.eye(V.rows)
    ds = [abs(int(D[i, i])) for i in range(min(D.shape)) if D[i, i]]
    assert all(ds[i+1] % ds[i] == 0 for i in range(len(ds)-1))
    return D, U, V, Ui, Vi, ds


def smith_record(M):
    D, U, V, Ui, Vi, ds = smith(M)
    return dict(matrix=entries(M), D=entries(D), U=entries(U), V=entries(V),
                U_inverse=entries(Ui), V_inverse=entries(Vi), factors=ds)


def wedge(M):
    return S.Matrix([[M[i, k]*M[j, l]-M[i, l]*M[j, k]
                      for k, l in PAIRS] for i, j in PAIRS])


def exterior(x, y):
    return S.Matrix([x[i]*y[j]-x[j]*y[i] for i, j in PAIRS])


def bezout(values):
    row = S.Matrix([list(map(S.Integer, values))])
    D, U, V, _, _, ds = smith(row)
    assert ds == [1], values
    answer = V[:, 0]*U[0, 0]
    assert row*answer == S.ones(1, 1)
    return answer


def fixed(T):
    D, U, V, Ui, Vi, ds = smith(T-S.eye(4))
    assert ds == [1]*len(ds)
    r = len(ds)
    K, L = V[:, r:], Vi[r:, :]
    c = L*DELTA
    d, u, v, ui, vi, ss = smith(c)
    assert ss == [1]
    Q = ui.copy()
    Q[:, 0] *= int(v[0, 0])
    assert Q[:, 0] == c
    F, Fi = integral(K*Q), integral(Q.inv()*L)
    assert F[:, 0] == DELTA and Fi*F == S.eye(F.cols)
    assert (T-S.eye(4))*F == S.zeros(4, F.cols)
    return F, Fi


def primitive_cycle(A, g):
    B = A-S.eye(2)
    c = next(B[:, j] for j in range(2) if B[:, j] != S.zeros(2, 1))
    d = gcd(*map(abs, map(int, c)))
    u = c/d
    if next(x for x in u if x) < 0:
        u = -u
    c0 = bezout(u)
    r = S.Matrix([-c0[1], c0[0]])
    assert S.det(S.Matrix.hstack(u, r)) == 1
    B0 = u*u.T*J
    at = next((i, j) for i in range(2) for j in range(2) if B0[i, j])
    n = S.cancel(B[at]/B0[at])
    kap = S.cancel(g[next(i for i in range(2) if u[i])]/u[next(i for i in range(2) if u[i])])
    assert n.q == kap.q == 1 and n > 0 and g == kap*u and B == n*B0
    return int(n), u, r, int(kap)


def graph(kind):
    """Component names, multiplicities, and actual generator permutation."""
    if kind == 'II':
        return ['C0'], [1], [0], 1
    if kind in ('III', 'IV'):
        q = 2 if kind == 'III' else 3
        return [f'C{i}' for i in range(q)], [1]*q, list(range(1, q))+[0], q
    if kind == 'III*':
        return ['O0','O1','A0','A1','B0','B1','C','S'], [1,1,2,2,3,3,4,2], [1,0,3,2,5,4,6,7], 2
    if kind == 'IV*':
        return ['O0','O1','O2','B0','B1','B2','C'], [1,1,1,2,2,2,3], [1,2,0,4,5,3,6], 3
    m = re.fullmatch(r'I(\d+)\*', kind)
    assert m, kind
    k = int(m.group(1))
    assert k in (1, 3)
    names = ['L0','R0','L1','R1']+[f'B{j}' for j in range(k+1)]
    return names, [1]*4+[2]*(k+1), [1,2,3,0]+[4+k-j for j in range(k+1)], 4


def permutation_power(p, n):
    ans = list(range(len(p)))
    for _ in range(n):
        ans = [p[x] for x in ans]
    return ans


def orbits(p):
    ans, seen = [], set()
    for j in range(len(p)):
        if j in seen:
            continue
        this, k = [], j
        while k not in seen:
            seen.add(k); this.append(k); k = p[k]
        assert k == j
        ans.append(this)
    return ans


def build_T(raw, a, b, zero):
    result = []
    for i, (kind, aa, gg) in enumerate(zip(raw['fibers'], raw['elliptic_matrices'], raw['generator_section_cocycle'])):
        A, g = S.Matrix(aa), S.Matrix(gg)
        if re.fullmatch(r'I\d+', kind):
            n, u, r, kap = primitive_cycle(A, g)
            assert kind == f'I{n}'
            z = S.Rational(kap, n)*r
            w = S.Rational(1, n) if i == zero else 0
        else:
            z = (A-S.eye(2)).inv()*g
            w = 0
        beta = -a*g.T*J*A
        T = S.eye(4)
        T[:2, :2] = A
        T[:2, 3] = b*g
        T[2, :2] = beta
        T[2, 3] = (beta*(b*z))[0]+w
        integral(T)
        result.append((T, A, g, z))
    assert reduce(lambda x, y: x*y[0], result, S.eye(4)) == S.eye(4)
    om = S.Matrix([[0,a,0,0],[-a,0,0,0],[0,0,0,-b],[0,0,b,0]])
    assert all(T.T*om*T == om for T, *_ in result)
    return result


def enumerate_natural(raw):
    answer = []
    h = Fraction(raw['height_of_generator'])
    for j, kind in enumerate(raw['fibers']):
        if not re.fullmatch(r'I\d+', kind):
            continue
        n, u, r, kap = primitive_cycle(S.Matrix(raw['elliptic_matrices'][j]), S.Matrix(raw['generator_section_cocycle'][j]))
        total = 1/(h*n)
        if total.denominator != 1:
            continue
        for a in range(1, total.numerator+1):
            if total.numerator % a:
                continue
            b = total.numerator//a
            p, q = a*kap % n, b*kap % n
            if gcd(q, n) != 1:
                continue
            if n > 1 and not (p == q and p in {1, n-1}):
                continue
            valid = True
            for i, component in enumerate(raw['component_coordinates']):
                if i == j:
                    continue
                for mod, row in zip(component['moduli'], component['rows']):
                    c = row[0]
                    if a*c % mod and b*c % mod:
                        valid = False
            if valid:
                assert gcd(a, b) == 1
                # Check the literal four-section divisor against the cycle column.
                d = [int(k == p)-int(k == 0)-int(k == (p-q) % n)+int(k == -q % n) for k in range(n)]
                col = [-2*int(k == 0)+int(k == 1 % n)+int(k == -1 % n) for k in range(n)]
                assert d == col
                answer.append((j, a, b))
    return answer


def original_data(kind, component, a, b, T, A, g, z):
    names, mult, gen, q = graph(kind)
    comp = component['rows'][0][0] if component['rows'] else 0
    assert q == (component['moduli'][0] if component['moduli'] else 1)
    p, qq = (a*comp) % q, (b*comp) % q
    pointperm = permutation_power(gen, qq)
    obs = orbits(pointperm)
    gamma_order = q//gcd(q, b*comp)
    zero = p == 0
    data = dict(type=kind, component_order=q, generator_component=comp,
                P_component=p, Q_component=qq, names=names, multiplicities=mult,
                forward_minus_Q=permutation_power(gen, (-qq) % q),
                plus_Q=pointperm, orbits=obs, rho=len(obs), zero_Chern=zero)
    # The boundary's integral fibre quotient is checked, not only its rank.
    BW = wedge(T)-S.eye(6)
    record = smith_record(BW)
    assert record['factors'] == [1,1,1,1]
    if zero:
        assert gamma_order == q
        h = integral(a*z)
        alpha = -h.T*J
        P = S.eye(4); P[2, :2] = alpha
        Pi = integral(P.inv())
        Tp = P*T*Pi
        assert list(Tp[2, :]) == [0,0,1,0]
        f0 = S.Matrix([[q,0,q*b*z[1],0,-q*b*z[0],0], [0,0,0,0,0,1]])
        f = integral(f0*wedge(P))
        first = bezout([q, q*b*z[1], -q*b*z[0]])
        section0 = S.zeros(6, 2)
        for index, coefficient in zip([0,2,4], first):
            section0[index, 0] = coefficient
        section0[5, 1] = 1
        section = wedge(Pi)*section0
        assert f*section == S.eye(2) and f*BW == S.zeros(2,6)
        fvector = [sum(mult[i] for i in ob) for ob in obs]
        assert all(x % q == 0 for x in fvector)
        W = [x//q for x in fvector]
        outer = next(k for k, ob in enumerate(obs) if 0 in ob)
        assert W[outer] == 1
        C = S.eye(len(obs)); C[:, outer] = S.Matrix(W)
        Ci = integral(C.inv())
        assert abs(C.det()) == 1 and C*Ci == S.eye(len(obs))
        ell = integral(S.Matrix([-q*b*z[0], -q*b*z[1], 0, q]))
        assert T*ell == ell
        data.update(defect=len(obs)-1, q_orbit=q, fibre_vector=fvector, W=W,
                    component_basis=entries(C), component_basis_inverse=entries(Ci),
                    line_map=entries(P), line_map_inverse=entries(Pi),
                    fibre_map=entries(f), fibre_section=entries(section), ell=list(map(int,ell)),
                    boundary_fibre_smith=record)
    else:
        assert qq == 0 and b % q == 0 and gcd(a, q) == 1
        ell = integral(S.Matrix([-b*z[0], -b*z[1],0,1]))
        R = S.eye(4); R[:,3] = ell
        Ri = integral(R.inv()); Tp = R.inv()*T*R
        assert list(Tp[:,3]) == [0,0,0,1] and list(Tp[3,:]) == [0,0,0,1]
        rho = integral(q*S.Matrix([[a*z[1], -a*z[0], 1]]))
        v0 = bezout(list(rho))
        assert rho*(Tp[:3,:3]-S.eye(3)) == S.zeros(1,3)
        beta0 = R*S.Matrix(list(v0)+[0])
        k = exterior(beta0, ell)
        fp = S.Matrix([[1,0,0,0,0,0], [0,0,rho[0],0,rho[1],rho[2]]])*wedge(Ri)
        section = S.Matrix.hstack(S.eye(6)[:,0], k)
        assert fp*section == S.eye(2) and fp*BW == S.zeros(2,6)
        omega = S.Matrix([[a,0,0,0,0,-b]])
        assert (omega*k)[0] == -S.Rational(b,q)
        # P occupies the corresponding multiplicity-one component of G's orbit.
        pindex = permutation_power(gen, p)[0]
        assert pindex != 0 and mult[pindex] == mult[0] == 1
        c = S.zeros(1,len(names)); c[0, pindex] = 1; c[0,0] = -1
        F = S.Matrix(mult)
        complement = [i for i in range(len(names)) if i not in (0,pindex)]
        K = S.zeros(len(names),len(names)-1)
        K[:,0] = F
        for k0, i in enumerate(complement,1):
            K[i,k0] = 1
        left = S.zeros(len(names)-1,len(names))
        left[0,0] = 1
        for k0, i in enumerate(complement,1):
            left[k0,i] = 1; left[k0,0] = -mult[i]
        assert c*K == S.zeros(1,K.cols) and left*K == S.eye(K.cols)
        data.update(defect=len(names)-2, h=b//q, ell=list(map(int,ell)),
                    split_map=entries(R), split_inverse=entries(Ri),
                    coinvariant_row=entries(rho), beta0=list(map(int,beta0)),
                    fibre_kernel=list(map(int,exterior(beta0,ell))),
                    fibre_pairing=-b//q, fibre_quotient=entries(fp),
                    fibre_section=entries(section), Chern_row=entries(c),
                    component_kernel_basis=entries(K), component_kernel_inverse=entries(left),
                    boundary_fibre_smith=record)
    return data


def exterior_data(monodromies, a, b):
    Ts = [x[0] for x in monodromies]
    N = len(Ts)
    D = S.Matrix.hstack(*[T-S.eye(4) for T in Ts[:-1]])
    Fs, Ls, js = [], [], []
    for i, T in enumerate(Ts):
        F, L = fixed(T); Fs.append(F); Ls.append(L)
        ji = S.zeros(4*(N-1),4)
        if i < N-1:
            ji[4*i:4*i+4,:] = S.eye(4)
        else:
            for j in range(N-1):
                tail = reduce(lambda x,y: x*y, Ts[j+1:N-1], S.eye(4))
                ji[4*j:4*j+4,:] = -tail
        js.append(ji)
        assert D*ji*F == S.zeros(4,F.cols)
    B = S.Matrix.hstack(*[j*F for j,F in zip(js,Fs)])
    dr, br = smith_record(D), smith_record(B)
    assert dr['factors'] == [1,1,1]
    assert br['factors'] == [1]*(4*N-7)
    rel = S.zeros(B.cols,1)
    offset = 0
    for F in Fs:
        rel[offset] = 1; offset += F.cols
    assert B.cols == 4*N-6 and B*rel == S.zeros(B.rows,1)
    W = S.Matrix.hstack(*[wedge(T)-S.eye(6) for T in Ts])
    wr = smith_record(W)
    assert wr['factors'] == [1]*5
    omega = S.Matrix([[a,0,0,0,0,-b]])
    assert omega*W == S.zeros(1,W.cols)
    uv = bezout([a,-b]); s0 = S.zeros(6,1); s0[0],s0[5] = uv
    assert omega*s0 == S.ones(1,1)
    return dict(D=dr, B=br, B_relation=list(map(int,rel)),
                fixed_bases=[entries(F) for F in Fs], fixed_inverses=[entries(L) for L in Ls],
                boundary_graph_maps=[entries(j) for j in js], wedge=wr,
                omega=entries(omega), fibre_section=list(map(int,s0)))


def main():
    raw_bytes = RAW.read_bytes()
    profiles = json.loads(raw_bytes)['rows']
    OUT.mkdir(parents=True, exist_ok=True)
    allrows, patterns7, patterns8, tally, local_tally = [], [], [], [], Counter()
    print('Raw fixture SHA256',hashlib.sha256(raw_bytes).hexdigest())
    print('Independent input: raw 21 profiles; admitted natural component criterion; explicit component graphs.')
    for raw in profiles:
        natural = enumerate_natural(raw)
        count7 = count8 = row7 = positive7 = nonzero8 = 0
        for zero,a,b in natural:
            name = f"{raw['OS']}:{raw['profile']}:z{zero+1}:a{a}:b{b}"
            mon = build_T(raw,a,b,zero)
            gd = exterior_data(mon,a,b)
            if b == 1:
                for i,kind in enumerate(raw['fibers']):
                    if i == zero or not re.fullmatch(r'I\d+',kind):
                        continue
                    n,u,r,kap = primitive_cycle(S.Matrix(raw['elliptic_matrices'][i]),S.Matrix(raw['generator_section_cocycle'][i]))
                    assert (a*kap) % n == 0 and gcd(b*kap,n) == 1
            local = []
            for i,(kind,component,mon0) in enumerate(zip(raw['fibers'],raw['component_coordinates'],mon)):
                if re.fullmatch(r'I\d+',kind):
                    continue
                d = original_data(kind,component,a,b,*mon0)
                d['site'] = i+1
                local.append(d)
                local_tally[(kind,'zero' if d['zero_Chern'] else 'nonzero',d['defect'])] += 1
            options7,options8 = [],[]
            for d in local:
                finite = not re.fullmatch(r'I\d+\*',d['type'])
                options7.append((['O'] if d['zero_Chern'] else [])+(['F'] if finite else []))
                options8.append(['O']+(['F'] if finite else []))
            ps7,ps8 = [],[]
            for choices in product(*options7):
                D = sum(d['defect'] for d,c in zip(local,choices) if c == 'O')
                p = dict(row=name, choices=[f"{d['site']}:{c}" for d,c in zip(local,choices)],D=D)
                patterns7.append(p); ps7.append(p); positive7 += D > 0
            for choices in product(*options8):
                chosen = [d for d,c in zip(local,choices) if c == 'O']
                L = sum(not d['zero_Chern'] for d in chosen)
                beta = sum(d['defect'] for d in chosen)
                p = dict(row=name, choices=[f"{d['site']}:{c}" for d,c in zip(local,choices)],L=L,beta=beta)
                patterns8.append(p); ps8.append(p); nonzero8 += L > 0
            row7 += bool(ps7); count7 += len(ps7); count8 += len(ps8)
            allrows.append(dict(id=name,OS=raw['OS'],profile=raw['profile'],zero_site=zero+1,a=a,b=b,
                                fibers=raw['fibers'],monodromies=[entries(t[0]) for t in mon],
                                exterior=gd, original_additive=local))
            print('ROW',name,'Dsmith='+str(gd['D']['factors']),
                  'Bsmith=1^'+str(len(gd['B']['factors'])), 'Wsmith=1^5',
                  'L7='+str(len(ps7)),'L8='+str(len(ps8)),
                  'local='+','.join(f"{d['site']}:{d['type']}:{'Z' if d['zero_Chern'] else 'C'}:{d['defect']}" for d in local))
        tally.append(dict(OS=raw['OS'],profile=raw['profile'],natural=len(natural),L7_rows=row7,
                          L7_patterns=count7,L7_positive=positive7,L8_patterns=count8,L8_nonzero=nonzero8))
    print('\nPROFILE TOTALS')
    for t in tally: print(json.dumps(t,sort_keys=True))
    print('\nORIGINAL LOCAL TYPES')
    for key,value in sorted(local_tally.items()): print(key,value)
    print('\nALL L7 PATTERNS')
    for i,p in enumerate(patterns7,1): print(i,p['row'],','.join(p['choices']), 'D='+str(p['D']))
    print('\nALL L8 PATTERNS')
    for i,p in enumerate(patterns8,1): print(i,p['row'],','.join(p['choices']),'L='+str(p['L']),'beta='+str(p['beta']))
    totals = dict(natural=len(allrows),L7_rows=len({p['row'] for p in patterns7}),L7_patterns=len(patterns7),
                  L7_positive=sum(p['D']>0 for p in patterns7),L8_rows=len({p['row'] for p in patterns8}),
                  L8_patterns=len(patterns8),L8_nonzero=sum(p['L']>0 for p in patterns8))
    b1rows = {r['id'] for r in allrows if r['b'] == 1}
    totals['L7_b1_defects'] = sorted({p['D'] for p in patterns7 if p['row'] in b1rows})
    assert totals == dict(natural=172,L7_rows=160,L7_patterns=228,L7_positive=30,
                          L8_rows=172,L8_patterns=282,L8_nonzero=54,L7_b1_defects=[0,1,2,4]),totals
    print('\nTOTALS',json.dumps(totals,sort_keys=True))
    print('All exact matrix identities, inverse compositions, primitive fibre sections and graph relations passed.')
    result = dict(input=str(RAW.relative_to(ROOT)),input_sha256=hashlib.sha256(raw_bytes).hexdigest(),
                  completed_utc=datetime.now(timezone.utc).isoformat(),
                  scope='Fresh L7/L8; target originals and historical target algorithms unopened.',
                  totals=totals,profiles=tally,rows=allrows,L7_patterns=patterns7,L8_patterns=patterns8)
    (OUT/(PREFIX+'_fresh_data.json')).write_text(json.dumps(result,indent=2)+'\n')
    for tag,ps in [('02L7',patterns7),('02L8',patterns8)]:
        cols = ['number','row','choices']+(['D'] if tag == '02L7' else ['L','beta'])
        lines = ['\t'.join(cols)]
        for i,p in enumerate(ps,1):
            lines.append('\t'.join([str(i),p['row'],','.join(p['choices'])]+[str(p[c]) for c in cols[3:]]))
        (OUT/f'S6_SERIES_PUBLISH_III_{tag}_fresh_patterns.tsv').write_text('\n'.join(lines)+'\n')


if __name__ == '__main__':
    main()
