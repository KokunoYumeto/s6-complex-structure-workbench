#!/usr/bin/env python3
"""Post-exposure L2 auxiliary check, with no historical program input.

Enumerate from the literal component groups, test the complete exterior
maps by integral Hermite bases, and check the additional rank-one root
maps and the integral determinant.  The frozen fresh L2 files are read
neither as programs nor as derived inputs and are never rewritten.
"""
from pathlib import Path
from itertools import combinations
from math import gcd, prod
import json
from sympy import Matrix, Rational, eye, zeros, gcdex, symbols, simplify
from sympy.matrices.normalforms import hermite_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from sympy import ZZ

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / 'agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json'
rows = json.loads(RAW.read_text())['rows']
J = Matrix([[0, 1], [-1, 0]])
delta = Matrix([0, 0, 1, 0])
pairs = list(combinations(range(4), 2))


def integral_smith(A):
    S, U, V = smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(ZZ))
    S, U, V = S.to_Matrix(), U.to_Matrix(), V.to_Matrix()
    assert U*A*V == S and abs(U.det()) == abs(V.det()) == 1
    factors = [abs(int(S[i, i])) for i in range(min(S.shape)) if S[i, i]]
    return S, U, V, factors


def wedge(T):
    return Matrix([[T[i, k]*T[j, l]-T[i, l]*T[j, k]
                    for k, l in pairs] for i, j in pairs])


def mult_coordinates(A, g):
    N = A-eye(2)
    col = next(N[:, i] for i in range(2) if N[:, i] != zeros(2, 1))
    u = col/gcd(*map(lambda x: abs(int(x)), col))
    if next(x for x in u if x) < 0:
        u = -u
    s, t, d = gcdex(u[0], u[1])
    assert d == 1
    r = Matrix([-t, s])
    assert Matrix.hstack(u, r).det() == 1
    nu = next(N[i, j]/(u*u.T*J)[i, j]
              for i in range(2) for j in range(2) if (u*u.T*J)[i, j])
    kappa = next(g[i]/u[i] for i in range(2) if u[i])
    assert N == nu*u*u.T*J and g == kappa*u and nu > 0
    return int(nu), int(kappa), u, r


def component_zero(data, multiple):
    return all(multiple*coord[0] % modulus == 0
               for modulus, coord in zip(data['moduli'], data['rows']))


def natural_inputs(row):
    d = int(1/Rational(row['height_of_generator']))
    for z, typ in enumerate(row['fibers']):
        if not (typ.startswith('I') and typ[1:].isdigit()):
            continue
        nu = int(typ[1:])
        if d % nu:
            continue
        ab = d//nu
        comp = row['component_coordinates'][z]
        kappa = 0 if nu == 1 else int(comp['rows'][0][0])
        for a in range(1, ab+1):
            if ab % a:
                continue
            b = ab//a
            p, q = a*kappa % nu, b*kappa % nu
            if gcd(q, nu) != 1:
                continue
            degrees = [int(j == p)-int(j == 0)-int(j == (p-q) % nu)
                       + int(j == (-q) % nu) for j in range(nu)]
            zero_components = []
            for h in range(nu):
                target = [-2*int(j == h)+int(j == (h-1) % nu)
                          + int(j == (h+1) % nu) for j in range(nu)]
                if degrees == target:
                    zero_components.append(h)
            if not zero_components:
                continue
            if not all(i == z or component_zero(data, a) or component_zero(data, b)
                       for i, data in enumerate(row['component_coordinates'])):
                continue
            assert zero_components == [0] and gcd(a, b) == 1
            yield z, a, b


def marked_matrices(row, z, a, b):
    answer = []
    for i, (typ, aa, gg) in enumerate(zip(row['fibers'], row['elliptic_matrices'],
                                         row['generator_section_cocycle'])):
        A, g = Matrix(aa), Matrix(gg)
        if typ.startswith('I') and typ[1:].isdigit():
            nu, kappa, u, r = mult_coordinates(A, g)
            h = Rational(kappa, nu)*r
            weight = Rational(1, nu) if i == z else 0
        else:
            h, weight = (A-eye(2)).inv()*g, 0
        beta = -a*g.T*J*A
        T = eye(4)
        T[:2, :2], T[:2, 3], T[2, :2] = A, b*g, beta
        T[2, 3] = (beta*(b*h))[0]+weight
        assert all(x.q == 1 for x in T)
        answer.append(T)
    assert prod(answer, start=eye(4)) == eye(4)
    return answer


def fixed_basis(T):
    S, U, V, factors = integral_smith(T-eye(4))
    rank = len(factors)
    F = V[:, rank:]
    coords = (V.inv()*delta)[rank:, :]
    Sc, Uc, Vc, dc = integral_smith(coords)
    assert dc == [1]
    change = Uc.inv()
    change[:, 0] *= Vc[0, 0]
    F = F*change
    assert F[:, 0] == delta and (T-eye(4))*F == zeros(4, F.cols)
    return F, factors


total = 0
retained_boundary_checks = 0
for row in rows:
    count = 0
    for z, a, b in natural_inputs(row):
        Ts = marked_matrices(row, z, a, b)
        N = len(Ts)
        D = Matrix.hstack(*[T-eye(4) for T in Ts[:-1]])
        SD, UD, VD, ds = integral_smith(D)
        assert ds == [1, 1, 1]
        Fs = [fixed_basis(T) for T in Ts]
        js = []
        for i in range(N-1):
            ji = zeros(4*(N-1), 4)
            ji[4*i:4*i+4, :] = eye(4)
            js.append(ji)
        last = zeros(4*(N-1), 4)
        for i in range(N-1):
            last[4*i:4*i+4, :] = -prod(Ts[i+1:N-1], start=eye(4))
        js.append(last)
        B = Matrix.hstack(*[ji*data[0] for ji, data in zip(js, Fs)])
        coords = VD.inv()*B
        assert coords[:3, :] == zeros(3, B.cols)
        assert hermite_normal_form(coords[3:, :]) == eye(4*N-7)
        rho = zeros(B.cols, 1)
        offset = 0
        for F, _ in Fs:
            rho[offset] = 1
            offset += F.cols
        assert B*rho == zeros(B.rows, 1) and B.cols == 4*N-6
        omega = Matrix([[a, 0, 0, 0, 0, -b]])
        So, Uo, Vo, do = integral_smith(omega)
        assert do == [1]
        W = Matrix.hstack(*[wedge(T)-eye(6) for T in Ts])
        wc = Vo.inv()*W
        assert wc[0, :] == zeros(1, W.cols)
        assert hermite_normal_form(wc[1:, :]) == eye(5)
        if row['OS'] == 50 and a % 2:
            assert all(all(d == 1 for d in factors) for F, factors in Fs)
            retained_boundary_checks += N
        count += 1
    total += count
    print(f"OS{row['OS']}/{row['profile']}: {count} natural rows; "
          "full graph Hermite basis and primitive exterior quotient verified")
assert total == 172
print(f"TOTAL: {total} natural rows; {retained_boundary_checks} retained OS50 boundary H1 groups free")

# Universal transitive rank-one quotient: c is prime to m, u*c+r*m=1.
m, c, u, p, q = symbols('m c u p q', nonzero=True)
r = (1-u*c)/m
F2 = Matrix([[m, 0, 0, 0, c, 0, 0],
             [0, m, 0, 0, 0, -c, 0],
             [0, 0, m, 0, 0, 0, -c],
             [0, u*q, -u*p, 1, 0, r*q, -r*p]])
K2 = Matrix([[-c, 0, 0], [0, c, 0], [0, 0, c],
             [0, -q, p], [m, 0, 0], [0, m, 0], [0, 0, m]])
S2 = Matrix([[r, 0, 0, 0], [0, r, 0, 0], [0, 0, r, 0],
             [0, 0, 0, 1], [u, 0, 0, 0], [0, -u, 0, 0], [0, 0, -u, 0]])
R2 = Matrix([[-u, 0, 0, 0, r, 0, 0],
             [0, u, 0, 0, 0, r, 0], [0, 0, u, 0, 0, 0, r]])
assert (F2*K2).applyfunc(simplify) == zeros(4, 3)
assert (F2*S2).applyfunc(simplify) == eye(4)
assert (R2*K2).applyfunc(simplify) == eye(3)
assert (eye(7)-S2*F2-K2*R2).applyfunc(simplify) == zeros(7)
assert F2[:, :4].det() == m**3 and K2[4:, :] == m*eye(3)
print("Rank-one quotient: exact boundary section, full-kernel retraction, vertical index m^3, normal projection m I3")

# Schur complement in arbitrary normal ranks 2, 3 and 4.
ranks = [2, 3, 4]
be = symbols('be')
Ps = [Matrix(n, n, lambda i, j: symbols(f'P{k}_{i}{j}')) for k, n in enumerate(ranks)]
fs = [Matrix(1, n, lambda i, j: symbols(f'f{k}_{j}')) for k, n in enumerate(ranks)]
M = zeros(1+sum(ranks))
M[0, 0] = be
E = eye(M.rows)
offset = 1
for n, P, f in zip(ranks, Ps, fs):
    M[offset, 0] = 1
    M[0, offset:offset+n] = -f*P
    M[offset:offset+n, offset:offset+n] = P
    E[0, offset:offset+n] = f
    offset += n
EM = (E*M).applyfunc(simplify)
assert EM[0, 0] == be+sum(f[0, 0] for f in fs)
assert EM[0, 1:] == zeros(1, sum(ranks))
assert E.det() == 1 and (E.inv()*EM-M).applyfunc(simplify) == zeros(M.rows)
print("All-sites determinant: arbitrary 2/3/4-dimensional normal matrices and every off-diagonal functional coefficient cancel by an explicit determinant-one row map")

row = next(x for x in rows if x['OS'] == 50 and x['profile'] == 'default')
Ts = marked_matrices(row, 2, 3, 4)
w = Matrix([1, 0, 2, 0])
L = Matrix([0, 3, 0, 1])
t = Matrix([0, 8, 0, 3])
H = Matrix.hstack(w, L, delta, t)
assert H.det() == 1 and H.inv()*Ts[1]*H == eye(4)+Matrix(4, 4, lambda i, j: int(i == 0 and j == 1))
assert L[3] == 1
star_order, star_n, rank_order, rank_n, b, peripheral = 2, -1, 3, 1, 4, 0
seifert = rank_order*star_n+star_order*rank_n-peripheral*star_order*rank_order
assert seifert == -1
kappa_star, kappa_rank = 1, rank_order**3
order = abs(kappa_star*kappa_rank*b*(Rational(peripheral)-Rational(star_n, star_order)-Rational(rank_n, rank_order)))
old_order = Rational(b, 2)
assert order == 18 and old_order == 2
print("Counterexample: OS50/default a=3 b=4 zero=I1@3; I3 H determinant 1, power L has component rotation 1 and gamma return 1")
print(f"Counterexample: star (m,n)=(2,-1), I3 root (3,1), e=0; Seifert determinant {seifert}; kappa=(1,27); full |H2|={order}; old ST12 value={old_order}")
print("SUCCESS: no frozen file or canonical file was written; all checks above used raw defining inputs or displayed universal matrices")
