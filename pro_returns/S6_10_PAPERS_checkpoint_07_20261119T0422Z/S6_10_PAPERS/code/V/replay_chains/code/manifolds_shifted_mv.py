"""Full integral MV calculation for the shifted product of two sphere fibrations.

Cut the base into discs containing the two disjoint triples of critical
values. The pieces are E x F and F x E, E=S6 minus int(F x D2), F=T4.
Normal-circle sweep identifies H_k(E)=H_{k-1}(F) for 1<=k<=4.
The finite pullback indices and boundary isotropy determine each fibre
inclusion i_k up to two simultaneous signs. Both signs are checked.
The second boundary normal circle is the reverse of the first one.
Every group of the two pieces and their common boundary is free, so
the kernel part in MV is free and the remaining abelian extension splits.
"""
from pathlib import Path
from itertools import combinations, product
from math import comb
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

ROOT = Path(__file__).resolve().parents[1]
F = {k: list(combinations(range(4), k)) for k in range(5)}
F.update({k: [] for k in range(-6, 12) if k not in F})
E = {0: [()]}
E.update({k: F[k-1] if 1 <= k <= 4 else [] for k in range(1, 12)})
I = {1: {(0,): 1}, 2: {(0, 3): 6, (1, 2): 1},
     3: {(0, 1, 2): 1}, 4: {(0, 1, 2, 3): 1}}


def wedge_sign(a, b):
    if set(a) & set(b):
        return 0
    return (-1)**sum(x > y for x in a for y in b)


def phi(k, sign1=1, sign2=1):
    # r_k(alpha)=phi_k(alpha)+theta wedge alpha.
    # Isotropy at the five-dimensional boundary gives c_(5-k)=-c_k.
    coefficients = {1: 12*sign1, 2: 2*sign2, 3: -2*sign2, 4: -12*sign1}
    M = s.zeros(len(F[k]), len(F[k-1]))
    for j, alpha in enumerate(F[k-1]):
        pairing = sum(value*wedge_sign(alpha, beta)
                      for beta, value in I[5-k].items())
        for basis, value in I[k].items():
            M[F[k].index(basis), j] = coefficients[k]*pairing*value
    return M


def fibre_map(k, sign1=1, sign2=1):
    if k == 0:
        return s.ones(1)
    if 1 <= k <= 4:
        return phi(k, sign1, sign2).T
    return s.zeros(0, len(F[k]))


def basis(k):
    # Source labels ('f',p,alpha,beta) or ('m',p,alpha,beta), where
    # m means theta x alpha x beta, theta is always written first.
    source = []
    target = []
    for p in range(5):
        for alpha, beta in product(F[p], F[k-p]):
            source.append(('f', p, alpha, beta))
        for alpha, beta in product(F[p], F[k-1-p]):
            source.append(('m', p, alpha, beta))
    for p in range(5):
        for alpha, beta in product(E[p], F[k-p]):
            target.append((0, p, alpha, beta))
        for alpha, beta in product(F[p], E.get(k-p, [])):
            target.append((1, p, alpha, beta))
    return source, target


def matrix(k, sign1=1, sign2=1, second_signs=None):
    second_signs = (sign1, sign2) if second_signs is None else second_signs
    source, target = basis(k)
    index = {entry: j for j, entry in enumerate(target)}
    D = s.zeros(len(target), len(source))
    for j, (typ, p, alpha, beta) in enumerate(source):
        q = len(beta)
        if typ == 'f':
            A = fibre_map(p, sign1, sign2)
            B = fibre_map(q, *second_signs)
            for r, a in enumerate(E[p]):
                D[index[(0, p, a, beta)], j] += A[r, F[p].index(alpha)]
            for r, b in enumerate(E[q]):
                D[index[(1, p, alpha, b)], j] -= B[r, F[q].index(beta)]
        else:
            if p < 4:
                D[index[(0, p+1, alpha, beta)], j] += 1
            if q < 4:
                # Move theta past alpha: (-1)^p; reverse the normal circle:
                # -1; and use the second minus in MV: another -1.
                D[index[(1, p, alpha, beta)], j] += (-1)**p
    return D


def smith_data(D):
    S = smith_normal_form(D, domain=s.ZZ)
    diagonal = [abs(int(S[i, i])) for i in range(min(S.shape)) if S[i, i]]
    return dict(rows=D.rows, columns=D.cols, rank=len(diagonal),
                units=diagonal.count(1), torsion=[x for x in diagonal if x > 1])


def run():
    cases = []
    reference = None
    signs = ((1, 1), (1, -1), (-1, 1), (-1, -1))
    for (sign1, sign2), second_signs in product(signs, signs):
        result = []
        previous_kernel = 0
        print('Boundary-adjoint sign choices:', (sign1, sign2), second_signs, flush=True)
        for k in range(11):
            D = matrix(k, sign1, sign2, second_signs)
            data = smith_data(D)
            data['degree'] = k
            data['betti'] = data['rows']-data['rank']+previous_kernel
            previous_kernel = data['columns']-data['rank']
            result.append(data)
            if (sign1, sign2) == second_signs == (1, 1):
                print(data, flush=True)
        summary = [(d['betti'], d['torsion']) for d in result]
        if reference is None:
            reference = summary
        else:
            assert summary == reference
        assert [d['betti'] for d in result] == [1, 1, 1, 20, 63, 88, 63, 20, 1, 1, 1]
        for k in range(10):
            assert result[k]['torsion'] == result[9-k]['torsion']
        cases.append(dict(sign1=sign1, sign2=sign2,
                          second_signs=second_signs, groups=result))
    print('All sixteen independent adjoint sign choices agree; integral torsion duality verified.', flush=True)
    payload = dict(method='Direct normal-boundary MV, free-kernel extensions split',
                   fibre_maps=[fibre_map(k).tolist() for k in range(5)],
                   cases=cases)
    (ROOT/'records/manifolds_shifted_mv.json').write_text(
        json.dumps(payload, indent=2, default=int)+'\n')


if __name__ == '__main__':
    run()
