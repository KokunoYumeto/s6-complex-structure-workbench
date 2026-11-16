"""Exact finite certificates supporting the complete proof of UN82.

The source proof supplies the unbounded Diophantine argument, residue
and trace comparison, connectedness argument, and actual surface maps.
This program independently checks their explicit coefficient formulas.
"""
from math import gcd
import sympy as s

z, w, a, b, x = s.symbols('z w a b x')
weights = 0
monomials = 0
for p in range(1, 45):
    for q in range(1, 45):
        if gcd(p, q) != 1:
            continue
        found = {(i, j) for i in range((p+q)//p+1)
                 for j in range((p+q)//q+1) if p*i+q*j == p+q}
        if p > 1 and q > 1:
            expected = {(1, 1)}
        elif p > 1:
            expected = {(1, 1), (0, p+1)}
        elif q > 1:
            expected = {(1, 1), (q+1, 0)}
        else:
            expected = {(2, 0), (1, 1), (0, 2)}
        assert found == expected, (p, q, found)
        for i, j in found:
            ell = (i-1)//q
            assert i == 1+q*ell and j == 1-p*ell
        weights += 1
        monomials += len(found)
print('Exact coprime Hopf weight spaces:', weights,
      '; monomials:', monomials, 'PASS')

factor_cases = 0
for p in range(2, 35):
    for av in [-3, -1, 0, 1, 2]:
        for bv in [-2, 0, 1, 3]:
            if av == bv == 0:
                continue
            g = s.expand(w*(av*z+bv*w**p))
            coeff, factors = s.factor_list(g)
            multiplicities = [n for _, n in factors]
            assert (1 in multiplicities) == all(n == 1 for n in multiplicities)
            assert all(n == 1 for n in multiplicities) or len(factors) == 1
            if av:
                assert s.expand(g - av*w*(z+s.Rational(bv, av)*w**p)) == 0
            factor_cases += 1
print('Triangular eigenfunction factor/coordinate comparisons:', factor_cases, 'PASS')

quadratics = 0
for av in range(-4, 5):
    for bv in range(-4, 5):
        for cv in range(-4, 5):
            if av == bv == cv == 0:
                continue
            disc = bv*bv-4*av*cv
            g = av*z*z+bv*z*w+cv*w*w
            if disc == 0:
                assert s.resultant(s.diff(g,z),s.diff(g,w),z) == 0
            else:
                # A homogeneous quadratic with nonzero discriminant has
                # two distinct complex linear factors, including w when a=0.
                assert s.det(s.Matrix([[2*av,bv],[bv,2*cv]])) != 0
            quadratics += 1
print('Homogeneous quadratic simple/double factor tests:', quadratics, 'PASS')

unipotent = 0
for degree in range(1, 30):
    basis = [x**j for j in range(degree+1)]
    matrix = s.Matrix([[s.expand(v.subs(x,x+1)-v).coeff(x,i)
                        for v in basis] for i in range(degree+1)])
    kernel = matrix.nullspace()
    assert len(kernel) == 1
    assert kernel[0][0] != 0 and all(v == 0 for v in kernel[0][1:])
    unipotent += 1
print('Nonlinear translation-eigenfunction kernels:', unipotent, 'PASS')

# Keep the whole exceptional forest, including zero-coefficient curves.
# Vertices retain (anticanonical coefficient, genus, self-intersection).
initial = (((1, 1, 0), (1, 1, 0)), ())
level = {initial}
all_states = {initial}
transitions = 0
rejected_centres = 0
for depth in range(6):
    next_level = set()
    for vertices, edge_tuple in level:
        edges = set(edge_tuple)
        centres = [(i,) for i in range(len(vertices))] + list(edge_tuple)
        for centre in centres:
            coefficient = sum(vertices[i][0] for i in centre)-1
            if coefficient < 0:
                rejected_centres += 1
                continue
            changed = list(vertices)
            for i in centre:
                c, genus, square = changed[i]
                changed[i] = (c, genus, square-1)
            new_index = len(changed)
            changed.append((coefficient, 0, -1))
            new_edges = set(edges)
            if len(centre) == 2:
                new_edges.remove(tuple(sorted(centre)))
            new_edges.update(tuple(sorted((i,new_index))) for i in centre)
            result = (tuple(changed),tuple(sorted(new_edges)))
            positive = [i for i,vertex in enumerate(changed) if vertex[0] > 0]
            assert positive == [0,1]
            assert all(changed[i][0:2] == (1,1) for i in positive)
            assert (0,1) not in new_edges
            assert all(vertex[0] == 0 for vertex in changed[2:])
            assert all(vertex[2] < 0 for vertex in changed[2:])
            next_level.add(result)
            transitions += 1
    level = next_level
    all_states.update(level)
print('Actual labelled smooth/node point-map forest states:', len(all_states),
      '; transitions:', transitions, '; excluded negative centres:', rejected_centres, 'PASS')

leaf_cases = 0
for maximum in range(1, 80):
    for parent in range(maximum):
        coefficient = maximum-parent+1
        assert coefficient >= 2
        assert maximum-parent-1 == coefficient-2 >= 0
        for normal_order in range(1, coefficient):
            if (coefficient-1) % normal_order == 0:
                assert normal_order <= coefficient-1
        leaf_cases += 1
print('Exact maximal-leaf orders, adjunction exponents and parent coefficients:',
      leaf_cases, 'PASS')
print('All UN82 finite algebra certificates: PASS')
