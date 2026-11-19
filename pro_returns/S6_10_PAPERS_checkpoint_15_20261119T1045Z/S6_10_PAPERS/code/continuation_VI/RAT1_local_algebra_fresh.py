#!/usr/bin/env python3
"""Fresh exact RAT1 certificates; Python Fraction arithmetic, no CAS library.

The old producer's import names only were inspected (SymPy); no producer body,
old certificates, or old output was read.  Buchberger elimination, polynomial
differentiation, and Laurent Taylor substitution below are newly authored.
These finite certificates accompany the written analytic argument; they do
not independently prove analytic faithful flatness or the global forest claim.
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from pathlib import Path
import json
import time


class P:
    def __init__(self, n, terms=None):
        self.n = n
        self.t = {tuple(e): Q(c) for e, c in (terms or {}).items() if c}

    def __add__(self, other):
        if not isinstance(other, P):
            other = P(self.n, {(0,) * self.n: other})
        assert self.n == other.n
        out = self.t.copy()
        for e, c in other.t.items():
            out[e] = out.get(e, Q(0)) + c
        return P(self.n, out)

    __radd__ = __add__

    def __neg__(self):
        return P(self.n, {e: -c for e, c in self.t.items()})

    def __sub__(self, other):
        return self + -other

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if not isinstance(other, P):
            return P(self.n, {e: c * other for e, c in self.t.items()})
        assert self.n == other.n
        out = {}
        for e, c in self.t.items():
            for f, d in other.t.items():
                ef = tuple(a + b for a, b in zip(e, f))
                out[ef] = out.get(ef, Q(0)) + c * d
        return P(self.n, out)

    __rmul__ = __mul__

    def __pow__(self, k):
        assert k >= 0
        out = P(self.n, {(0,) * self.n: 1})
        base = self
        while k:
            if k & 1:
                out = out * base
            base = base * base
            k //= 2
        return out

    def __bool__(self):
        return bool(self.t)

    def __eq__(self, other):
        return not (self - other)

    def deriv(self, i):
        out = {}
        for e, c in self.t.items():
            if e[i]:
                f = list(e)
                f[i] -= 1
                out[tuple(f)] = c * e[i]
        return P(self.n, out)

    def subst(self, values):
        assert len(values) == self.n
        out = P(values[0].n)
        for e, c in self.t.items():
            term = P(values[0].n, {(0,) * values[0].n: c})
            for v, k in zip(values, e):
                assert k >= 0
                term = term * v ** k
            out = out + term
        return out

    def coef(self, i, k):
        return P(self.n - 1, {e[:i] + e[i+1:]: c
                             for e, c in self.t.items() if e[i] == k})

    def monic(self):
        return self * (1 / self.t[max(self.t)]) if self else self

    def serial(self):
        return [{"exp": list(e), "coefficient": str(self.t[e])}
                for e in sorted(self.t, reverse=True)]


def var(n, i):
    e = [0] * n
    e[i] = 1
    return P(n, {tuple(e): 1})


def mono(n, exp, c=1):
    return P(n, {tuple(exp): c})


def divides(a, b):
    return all(x <= y for x, y in zip(a, b))


def remainder(f, basis):
    out = P(f.n)
    while f:
        e = max(f.t)
        c = f.t[e]
        for g in basis:
            d = max(g.t)
            if divides(d, e):
                f = f - mono(f.n, [x-y for x, y in zip(e, d)], c/g.t[d])*g
                break
        else:
            term = mono(f.n, e, c)
            out = out + term
            f = f - term
    return out


def buchberger(gens):
    """Lexicographic monomial order, exact rational S-polynomial reduction."""
    basis = []
    for f in gens:
        r = remainder(f, basis)
        if r:
            basis.append(r.monic())
    pairs = [(i, j) for j in range(len(basis)) for i in range(j)]
    tested = 0
    while pairs:
        i, j = pairs.pop(0)
        a, b = basis[i], basis[j]
        ea, eb = max(a.t), max(b.t)
        # Buchberger's relatively-prime leading-monomial criterion.
        if all(min(x, y) == 0 for x, y in zip(ea, eb)):
            continue
        lcm = tuple(max(x, y) for x, y in zip(ea, eb))
        s = mono(a.n, [x-y for x, y in zip(lcm, ea)])*a
        s = s - mono(a.n, [x-y for x, y in zip(lcm, eb)])*b
        r = remainder(s, basis)
        tested += 1
        if r:
            k = len(basis)
            basis.append(r.monic())
            pairs.extend((h, k) for h in range(k))
    # Independently retain the pair-remainder verification, without the
    # relatively-prime shortcut used in construction.
    full_pairs = 0
    for i in range(len(basis)):
        for j in range(i):
            a, b = basis[i], basis[j]
            ea, eb = max(a.t), max(b.t)
            lcm = tuple(max(x, y) for x, y in zip(ea, eb))
            sp = mono(a.n, [x-y for x, y in zip(lcm, ea)])*a
            sp = sp - mono(a.n, [x-y for x, y in zip(lcm, eb)])*b
            assert not remainder(sp, basis)
            full_pairs += 1
    return basis, {"basis_size": len(basis), "construction_pairs": tested,
                   "all_pairs_zero_verified": full_pairs}


def saturation_check(name, gs, F, localizer):
    n = gs[0].n
    products = [a*b for a, b in combinations_with_replacement(gs, 2)]
    # New variable is first: elimination of s in (I^2, 1-s*localizer).
    lift = lambda p: P(n+1, {(0,)+e: c for e, c in p.t.items()})
    sat_gb, sat_stats = buchberger([lift(p) for p in products] +
                                  [1-var(n+1, 0)*lift(localizer)])
    eliminated = [P(n, {e[1:]: c for e, c in p.t.items()}) for p in sat_gb
                  if all(e[0] == 0 for e in p.t)]
    target_gb, target_stats = buchberger(products+[F])
    elim_gb, elim_stats = buchberger(eliminated)
    assert all(not remainder(p, target_gb) for p in eliminated)
    assert all(not remainder(p, elim_gb) for p in products+[F])
    square_gb, square_stats = buchberger(products)
    assert remainder(F, square_gb)  # the new symbolic generator is necessary
    assert all(not remainder(var(n, i)*F, square_gb) for i in range(n))
    return {"name": name, "saturation_equals_I_square_plus_F": True,
            "F_not_in_I_square": True, "maximal_ideal_times_F_in_I_square": True,
            "saturation": sat_stats, "target": target_stats,
            "elimination": elim_stats, "ordinary_square": square_stats,
            "elimination_generators": [p.serial() for p in eliminated]}


def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def pole(p):
    return max([0]+[-e[0] for e in p.t])


def branch_check(name, gs, F, gamma, dual_A, dual_B, frame,
                 expected_wedge_factor, expected_q, expected_poles):
    # gamma, lifts and frame coefficients are Laurent polynomials in t.
    grads = [[g.deriv(j).subst(gamma) for j in range(3)] for g in gs]
    a = [sum(frame[0][k]*grads[k][j] for k in range(len(gs)))
         for j in range(3)]
    b = [sum(frame[1][k]*grads[k][j] for k in range(len(gs)))
         for j in range(3)]
    assert dot(a, dual_A) == 1 and dot(a, dual_B) == 0
    assert dot(b, dual_A) == 0 and dot(b, dual_B) == 1
    tangent = [g.deriv(0) for g in gamma]
    assert cross(a, b) == [expected_wedge_factor*t for t in tangent]
    # Full Taylor substitution; e is a formal displacement parameter and
    # u,v are coefficients in the verified dual normal lifts.
    lift4 = lambda p: P(4, {(e[0], 0, 0, 0): c for e, c in p.t.items()})
    u, v, eps = var(4, 1), var(4, 2), var(4, 3)
    W = [lift4(A)*u+lift4(B)*v for A, B in zip(dual_A, dual_B)]
    inputs = [lift4(g)+eps*w for g, w in zip(gamma, W)]
    expansions = [g.subst(inputs) for g in gs]
    assert all(e.coef(3, 0) == 0 for e in expansions)
    linear = [e.coef(3, 1) for e in expansions]
    quadratic = [e.coef(3, 2) for e in expansions]
    qF = F.subst(inputs).coef(3, 2)
    assert qF == expected_q
    linear_poles = [pole(p) for p in linear]
    quadratic_poles = [pole(p) for p in quadratic]
    coefficient_derivative_bound = max(pole(p) for p in W)
    assert linear_poles == [0]*len(gs)
    assert max(quadratic_poles) == expected_poles[0]
    assert coefficient_derivative_bound == expected_poles[1]
    # For any holomorphic b_ij, epsilon^3 in b_ij*g_i*g_j is
    # b_ij(0)*(L_i*Q_j+Q_i*L_j) + Db_ij(W)*L_i*L_j.
    all_product_cubic_bounds = []
    for i, j in combinations_with_replacement(range(len(gs)), 2):
        product_term = linear[i]*quadratic[j]+quadratic[i]*linear[j]
        bound = max(pole(product_term), coefficient_derivative_bound)
        all_product_cubic_bounds.append(bound)
    assert max(all_product_cubic_bounds) <= expected_poles[0]
    return {"name": name, "dual_frame_pairing_identity": True,
            "wedge_factor": expected_wedge_factor.serial(),
            "F_quadratic": qF.serial(),
            "generator_linear_taylor_poles": linear_poles,
            "generator_quadratic_taylor_poles": quadratic_poles,
            "arbitrary_coefficient_derivative_pole_bound": coefficient_derivative_bound,
            "all_products_cubic_pole_bound": max(all_product_cubic_bounds),
            "all_pair_cubic_bounds": all_product_cubic_bounds}


def main():
    started = time.monotonic()
    x, y, z = [var(3, i) for i in range(3)]
    g345 = [y*y-x*z, y*z-x**3, z*z-x*x*y]
    F345 = x**5+x*y**3+z**3-3*x*x*y*z
    gcuspline = [x*z, y*z, y*y-x**3]
    Fcuspline = z*gcuspline[2]
    assert x*F345 == g345[1]**2-g345[0]*g345[2]
    assert y*F345 == g345[1]*g345[2]+x*g345[0]**2
    assert z*F345 == g345[2]**2+x*g345[0]*g345[1]
    assert x*Fcuspline == gcuspline[0]*gcuspline[2]
    assert y*Fcuspline == gcuspline[1]*gcuspline[2]
    assert z*Fcuspline == gcuspline[1]**2-x*gcuspline[0]**2
    sats = [saturation_check('monomial_345', g345, F345, x),
            saturation_check('cusp_plus_line', gcuspline, Fcuspline, x+z)]
    t = var(1, 0)
    T = lambda k, c=1: mono(1, [k], c)
    Z = P(1)
    O = T(0)
    # Laurent polynomials in t,u,v for asserted quadratic outputs.
    q345 = mono(3, [-1,2,0], 3)+mono(3, [-2,1,1], -3)+mono(3, [-3,0,2])
    qcl = mono(3, [-2,1,1])
    branches = [
        branch_check('monomial_345', g345, F345, [t**3,t**4,t**5],
            [Z,Z,-T(-3)], [Z,T(-5,Q(1,3)),T(-4,Q(2,3))],
            [[O,Z,Z],[t,O,Z]], T(6), q345, (10,5)),
        branch_check('cusp_branch', gcuspline, Fcuspline, [t**2,t**3,Z],
            [Z,Z,T(-2)], [Z,T(-3,Q(1,2)),Z],
            [[O,Z,Z],[Z,Z,O]], -T(4), qcl, (6,3)),
        branch_check('smooth_branch', gcuspline, Fcuspline, [Z,Z,t],
            [T(-1),Z,Z], [Z,T(-1),Z],
            [[O,Z,Z],[Z,O,Z]], T(2), mono(3,[-1,0,2]), (2,1))
    ]
    # Additional frame relation and Hessian determinants.
    grads = [[g.deriv(j).subst([t**3,t**4,t**5]) for j in range(3)] for g in g345]
    a = grads[0]
    b = [grads[1][j]+t*a[j] for j in range(3)]
    assert grads[2] == [-2*t*t*a[j]+t*b[j] for j in range(3)]
    det345 = 3*T(-1)*T(-3) - (Q(-3,2)*T(-2))**2
    detcl = -(Q(1,2)*T(-2))**2
    assert det345 == T(-4,Q(3,4))
    assert detcl == T(-4,Q(-1,4))
    degree_table=[]
    for delta in range(3):
        det_degree=-2+2*delta
        product_degree=-6*det_degree+4*(2*delta)
        assert product_degree==12-4*delta
        special_preimages=0 if delta==0 else 1+delta
        smooth_attachments=product_degree//5
        r_bound=special_preimages+smooth_attachments
        assert r_bound == [2,3,3][delta]
        degree_table.append({'delta':delta,'det_normal_degree':det_degree,
                            'cusp_product_degree':product_degree,
                            'special_preimage_bound':special_preimages,
                            'smooth_attachment_bound':smooth_attachments,
                            'r_bound':r_bound})
    nonlci=[]
    for name,pole_bound in [('monomial_345',10),('cusp_plus_line',8)]:
        min_radical_degree=4
        assert 3*min_radical_degree>pole_bound
        nonlci.append({'name':name,'normal_determinant_degree':-2+6,
                       'minimum_radical_degree':min_radical_degree,
                       'cubic_pole_bound':pole_bound,'contradiction_gap':12-pole_bound})
    return {'status':'PASS','method':'New Fraction polynomial engine, lex Buchberger elimination, full S-pair verification, Laurent Taylor substitution; no SymPy',
            'saturations':sats,'branch_derivative_certificates':branches,
            'monomial_345_conormal_relation_verified':True,
            'quadratic_determinants':{'monomial_345':det345.serial(),'cusp_plus_line_cusp':detcl.serial()},
            'nonlci_degree_contradictions':nonlci,'lci_degree_and_attachment_table':degree_table,
            'analytic_scope':'Polynomial certificates only; analytic localization and intrinsic tangent-lift independence require the separately written proof.',
            'elapsed_seconds':round(time.monotonic()-started,3)}


if __name__ == '__main__':
    result=main()
    output=Path(__file__).with_suffix('.output.json')
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','method','elapsed_seconds']},indent=2))
    print(output)
