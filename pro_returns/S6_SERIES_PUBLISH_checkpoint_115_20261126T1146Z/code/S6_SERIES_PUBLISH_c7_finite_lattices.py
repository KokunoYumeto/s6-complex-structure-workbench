#!/usr/bin/env python3
"""Fresh finite-cap lattices from raw periods and fresh KX candidates.

No L1/L4/L6 original, historical target program or old output is read.
The input candidate list was independently derived by the root before
exposure to the KX original. This program derives the finite lattices by
integral quotient coordinates and independently checks every norm map.
"""
from pathlib import Path
from math import gcd, lcm
from collections import Counter
import hashlib
import json
import sympy as S
from sympy.polys.domains import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'agents/continuation7_iii_finite_general'
OUT.mkdir(parents=True, exist_ok=True)
RAW = ROOT / 'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
CANDIDATES = ROOT / 'agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02KX_fresh_candidate_data.json'
profiles = {(r['OS'], r['profile']): r for r in json.loads(RAW.read_text())['rows']}
candidates = json.loads(CANDIDATES.read_text())['natural']
finite = {'II': (6, 1), 'III': (4, 2), 'IV': (3, 3),
          'III*': (4, 2), 'IV*': (3, 3)}
I = S.eye(4)
J = S.Matrix([[0, 1], [-1, 0]])
delta = I[:, 2]
gamma = I[:, 3]


def array(M):
    assert all(x.q == 1 for x in M)
    return [[int(x) for x in M.row(i)] for i in range(M.rows)]


def decomp(M):
    D, U, V = smith_normal_decomp(DomainMatrix.from_Matrix(M).convert_to(ZZ))
    D, U, V = (x.to_Matrix() for x in (D, U, V))
    assert U * M * V == D
    assert abs(U.det()) == abs(V.det()) == 1
    return D, U, V


records = []
patterns = Counter()
print('RAW_SHA256', hashlib.sha256(RAW.read_bytes()).hexdigest())
print('FRESH_CANDIDATES_SHA256', hashlib.sha256(CANDIDATES.read_bytes()).hexdigest())
for row in candidates:
    prof = profiles[row['OS'], row['profile']]
    a, b = row['a'], row['b']
    assert gcd(a, b) == 1
    has_odd_star = any(t in ('I1*', 'I3*') for t in prof['fibers'])
    positions = []
    omega = S.zeros(4)
    omega[:2, :2] = a * J
    omega[2:, 2:] = -b * J
    for index, kind in enumerate(prof['fibers']):
        if kind not in finite:
            continue
        order, q = finite[kind]
        A = S.Matrix(prof['elliptic_matrices'][index])
        cocycle = S.Matrix(prof['generator_section_cocycle'][index])
        z = (A-S.eye(2)).inv() * cocycle
        zQ = b * z
        beta_row = -a * cocycle.T * J * A
        T = S.eye(4)
        T[:2, :2] = A
        T[:2, 3] = b * cocycle
        T[2, :2] = beta_row
        T[2, 3] = (beta_row * zQ)[0]
        array(T)
        assert T.T * omega * T == omega and T**order == I
        assert all(T**j != I for j in range(1, order))
        g = lcm(*(int(x.q) for x in zQ))
        assert g in (1, q)
        qv = q // g
        ell = S.Matrix([-g*zQ[0], -g*zQ[1], 0, g])
        K = S.Matrix.hstack(delta, ell)
        assert (T-I) * K == S.zeros(4, 2)
        KD, KU, KV = decomp(K)
        assert [abs(KD[i, i]) for i in range(2)] == [1, 1]
        D, U, V = decomp(T-I)
        assert [abs(D[i, i]) for i in range(4)] == [1, 1, 0, 0]
        quotient = U[2:, :]
        CQ = S.Matrix.hstack(quotient*delta/qv, quotient*ell/g)
        array(CQ)
        assert abs(CQ.det()) == 1
        coords = CQ.inv() * quotient
        section = U.inv()[:, 2:] * CQ
        assert coords * section == S.eye(2)
        beta, eta = section[:, 0], section[:, 1]
        assert coords*delta == S.Matrix([qv, 0])
        assert coords*ell == S.Matrix([0, g])
        assert beta[3] == 0 and eta[3] == 1
        N = sum((T**j for j in range(order)), S.zeros(4))
        assert N*beta == S.Rational(order, qv)*delta
        assert N*eta == S.Rational(order, g)*ell
        assert -(beta.T*omega*ell)[0] == S.Rational(b*g, qv)
        assert -(eta.T*omega*delta)[0] == -b
        assert S.Rational(b*g, qv).q == 1
        fixed_coordinates = S.Matrix.vstack(S.Matrix([[0,0,1,0]]),
                                             S.Matrix([[0,0,0,S.Rational(1,g)]]))
        assert fixed_coordinates*K == S.eye(2)
        rec = dict(OS=row['OS'], profile=row['profile'], a=a, b=b,
                   zero_index=row['zero_index'], finite_index=index+1,
                   kind=kind, order=order, q=q, g=g, qv=qv,
                   T=array(T), omega=array(omega), fixed_basis=array(K),
                   quotient_coordinates=array(coords), quotient_section=array(section),
                   beta=array(beta), eta=array(eta), norm=array(N),
                   smith_U=array(U), smith_Uinv=array(U.inv()),
                   smith_V=array(V), smith_Vinv=array(V.inv()),
                   fixed_Smith_U=array(KU), fixed_Smith_V=array(KV))
        records.append(rec)
        positions.append(rec)
        print('POSITION',len(records),row['OS'],row['profile'],a,b,
              'zero',row['zero_index'],'finite',index+1,kind,
              'order/q/g/qv',(order,q,g,qv),
              'ell',list(ell),'beta',list(beta),'eta',list(eta))
    if not has_odd_star:
        patterns['nonstar_rows'] += 1
        # Minimal original fillings have one component orbit and zero Chern.
        count = 1
        for r in positions:
            component_q = r['q']
            narrowP = a % component_q == 0
            transitiveQ = gcd(b, component_q) == 1
            kind = r['kind']
            # III*/IV* have interior fixed vertices: no one-orbit original.
            minimal_original = narrowP and transitiveQ and kind in ('II','III','IV')
            count *= 2 if minimal_original else 1
        patterns['minimal_patterns'] += count

totals = Counter((r['g']==1) for r in records)
assert len(records) == 102 and totals[True] == 68 and totals[False] == 34
assert dict(patterns) == {'nonstar_rows':148,'minimal_patterns':198}
print('COUNTS finite positions',len(records),'primitive gamma',totals[True],
      'nonprimitive gamma',totals[False])
print('COUNTS',dict(patterns))
data = dict(scope='Fresh raw-period finite lattice derivation; no target original exposure',
            positions=records, counts=dict(patterns))
(OUT/'S6_SERIES_PUBLISH_III_finite_fresh_lattices.json').write_text(
    json.dumps(data,indent=2)+'\n',newline='\n')
print('PASS every exact quotient and section inverse, primitive fixed basis, norm map, pairing, and count.')
