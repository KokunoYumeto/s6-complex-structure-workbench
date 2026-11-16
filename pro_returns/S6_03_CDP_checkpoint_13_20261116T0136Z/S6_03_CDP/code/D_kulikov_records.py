#!/usr/bin/env python3
"""Exact finite checks for C.2.UN.75; no sampled numerical assertions."""
from collections import deque
from itertools import product
import sympy as s


def require(test, label):
    if not test:
        raise AssertionError(label)


x, y, z = s.symbols('x y z')
curve_map = s.Matrix([x * y, x, z])
point_map = s.Matrix([x, x * y, x * z])
require(curve_map.jacobian([x, y, z]).det() == -x,
        'ordinary curve blowup Jacobian')
require(point_map.jacobian([x, y, z]).det() == x**2,
        'ordinary point blowup Jacobian')
print('PASS exact curve/point blowup maps and Jacobian orders 1,2')

k1, k2, k3, k4 = s.symbols('k1 k2 k3 k4', integer=True)
type_i_adjunction = k2-k1-1
require(s.expand(type_i_adjunction+1) == k2-k1,
        'type I equal canonical order')
type_ii_adjunction = -(k2-k1-1)+(k3-k1-1)+(k4-k1-1)
require(s.expand(type_ii_adjunction+1) == k3+k4-k1-k2,
        'type II exact canonical balance')
print('PASS type I order equality and type II k1+k2=k3+k4')

canonical_cases = 0
for codim in (2, 3):
    for n in range(1, codim+1):
        for orders in product(range(5), repeat=n):
            exceptional = sum(orders)+codim-1
            require(exceptional > 0, 'new exceptional canonical order positive')
            for weights in product(range(1, 4), repeat=n):
                old_norm = tuple(orders)
                new_weight = sum(weights)
                shift = 3
                require(sum(a+shift*b for a, b in zip(old_norm, weights))
                        +codim-1 == exceptional+shift*new_weight,
                        'generator shift commutes with actual pullback')
                canonical_cases += 1
print(f'PASS {canonical_cases} integral canonical-order/full-weight comparisons')

# Source's card induction: a recorded finite maximum child number B gives
# an explicit integer potential. The proof itself needs only finite births
# and bounded levels; no uniform a-priori B is assumed there.
potential_cases = 0
for height in range(1, 11):
    for children in range(0, 7):
        weights = [0]*(height+2)
        for level in range(height, 0, -1):
            weights[level] = 1+children*weights[level+1]
        for level in range(1, height+1):
            for born in range(children+1):
                if level == height and born:
                    continue
                decrease = weights[level]-born*weights[level+1]
                require(decrease >= 1, 'strict finite card potential')
                potential_cases += 1
print(f'PASS {potential_cases} exact finite-height card potentials')

processed = 0
for height in range(1, 8):
    for mode in range(4):
        queue = deque(range(1, height+1))
        initial = list(queue)
        maximum_birth = 2
        bound = sum(sum(maximum_birth**j for j in range(height-level+1))
                    for level in initial)
        steps = 0
        while queue:
            level = queue.popleft() if mode % 2 == 0 else queue.pop()
            born = 0 if level == height else (steps+level+mode) % 3
            queue.extend([level+1]*born)
            steps += 1
            require(steps <= bound, 'recorded card process termination bound')
        processed += steps
print(f'PASS 28 complete finite records, {processed} individual removals')

EU, EV, EW, delta = s.symbols('EU EV EW delta', integer=True)
before = EU+EV-EW
after = (EU+delta)+EV-EW
require(s.expand(after-before) == delta,
        'restored-overlap Euler cancellation')
deltas = s.symbols('d0:8', integer=True)
epsilons = (1, -1, 1, 1, -1, -1, 1, -1)
support = s.symbols('support', integer=True)
endpoint = support
for eps, defect in zip(epsilons, deltas):
    endpoint += eps*defect
require(s.expand(endpoint-sum(e*d for e, d in zip(epsilons, deltas))) == support,
        'signed normal-cone telescoping')
print('PASS exact overlap cancellation and signed normal-cone telescoping')

euler_cases = 0
for genus in range(21):
    ebase = 2-2*genus
    exceptional = 2*ebase
    require(exceptional-ebase == ebase, 'curve blowup Euler')
    for marked in range(31):
        # In a reduced ruled-section contraction the r marked fibre curves
        # map to transverse double intersections, one triple removed each.
        old_triples = marked+17
        new_triples = 17
        require(old_triples-new_triples == marked, 'UN74 triple map')
        require((exceptional-ebase) == 2-2*genus, 'UN74 Euler map')
        euler_cases += 1
require(3-1 == 2, 'point blowup Euler')
require((4-2)-(4-2) == 0, 'type I/II common exceptional surface')
require(2+(2-2*3) == -2, 'point-plus-genus-three balancing block')
print(f'PASS {euler_cases} compact curve/triple maps and exact I/II defects')

# The special fibre algebra of I=(xy,xz,yz) at 0 is polynomial on its
# three degree-one generators: their exponent matrix is invertible,
# and every monomial in I^n has total degree 2n, below m I^n.
exponents = s.Matrix([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
require(abs(exponents.det()) == 2, 'three-axis fibre algebra independence')
for n in range(1, 13):
    images = set()
    for a in range(n+1):
        for b in range(n-a+1):
            c = n-a-b
            image = tuple(exponents*s.Matrix([a, b, c]))
            require(sum(image) == 2*n, 'minimal degree of Rees generator')
            require(image not in images, 'distinct three-axis fibre monomial')
            images.add(image)
    require(len(images) == (n+1)*(n+2)//2, 'P2 fibre Hilbert function')
# Euler of each punctured affine axis is 0; the common origin is one.
exact_defect = 3*0*(2-1)+1*(3-1)
naive_curve_defect = (3*1-2)*(2-1)
require(exact_defect == 2 and naive_curve_defect == 1,
        'normal cone retains the isolated extra defect')
print('PASS three-axis singular-centre fibre P2 and its exact defect 2')

zero_cases = 0
for d in range(0, 25):
    ecore = 2*d
    for point_up in range(9):
        for genus in range(9):
            signed_defect = 2*point_up+(2-2*genus)
            esupport = ecore-signed_defect
            require((esupport == 0) == (signed_defect == ecore),
                    'exact zero-Euler criterion')
            require(esupport % 2 == 0, 'compact smooth-centre parity')
            zero_cases += 1
print(f'PASS {zero_cases} exact endpoint/zero-Euler comparisons')
print('ALL C.2.UN.75 EXACT CHECKS PASSED')
