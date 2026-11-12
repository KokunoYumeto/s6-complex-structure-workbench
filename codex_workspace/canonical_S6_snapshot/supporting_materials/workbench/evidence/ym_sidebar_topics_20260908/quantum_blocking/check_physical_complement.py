"""Exact diagnostics for the physical morphism and raw inverse moments.

Finite checks supplement the full all-box measure/domain proofs. No sampled
matrix or approximate vector replaces the actual interacting vacuum.
"""
from pathlib import Path
import hashlib
import itertools
import json
import sympy as s

ROOT = Path(__file__).resolve().parent
count = 0
def check(test, label):
    global count
    if not bool(test):
        raise AssertionError(label)
    count += 1

def exact(value, label):
    if isinstance(value, s.MatrixBase):
        check(all(s.cancel(x) == 0 for x in value), label)
    else:
        check(s.cancel(value) == 0, label)

eye = s.eye(2)
pauli = (s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1))
matrices = [eye] + [s.Rational(3, 5)*eye + s.I*s.Rational(4, 5)*p for p in pauli]
matrices += [s.Rational(5, 13)*eye + s.I*s.Rational(12, 13)*p for p in pauli]
def product(items):
    result = eye
    for value in items:
        result = result * value
    return s.simplify(result)

for u in matrices:
    exact(u.H*u-eye, 'SU2 unitarity')
    exact(u.det()-1, 'SU2 determinant')
check(matrices[1]*matrices[2] != matrices[2]*matrices[1], 'noncommuting test inputs')

chains = 0
for m in range(2, 7):
    for offset in range(1, 7):
        links = [matrices[(offset+k) % len(matrices)] for k in range(m)]
        gauge = [matrices[(offset+2*k) % len(matrices)] for k in range(m+1)]
        z = product(links)
        changed = [gauge[k].H*links[k]*gauge[k+1] for k in range(m)]
        exact(product(changed)-gauge[0].H*z*gauge[m], 'ordered endpoint cancellation')
        recovered = links[:-1] + [product(links[:-1]).H*z]
        for old, new in zip(links, recovered):
            exact(new-old, 'Theta inverse on every fine link')
        exact(product(recovered)-z, 'Theta opposite inverse composition')
        internal = [eye] + [product(links[:k]).H for k in range(1, m)] + [eye]
        section = [internal[k].H*links[k]*internal[k+1] for k in range(m)]
        for value in section[:-1]:
            exact(value-eye, 'internal gauge fixes original prefix')
        exact(section[-1]-z, 'internal gauge preserves full product')
        for k in range(m):
            # The source action at inverse parameters equals our coordinate action.
            exact(gauge[k].H*links[k]*gauge[k+1]-changed[k], 'exact action dictionary')
            # Source/Baez inversion intertwiner, including reversed endpoint sides.
            exact((gauge[k]*links[k]*gauge[k+1].H).H
                  -gauge[k+1]*links[k].H*gauge[k].H, 'Baez inverse-link convention')
        chains += 1

t, z, kappa, xi, g, spacing = s.symbols('t z kappa xi g spacing', positive=True)
exact(1/t-1/(t+z)-z/(t+z)**2-z**2/(t*(t+z)**2), 'raw energy integrand')
exact(1/t-1/(t+z)-z/(t*(t+z)), 'raw memory integrand')
exact(1/t**2-1/(t+z)**2-(1-(t/(t+z))**2)/t**2, 'raw mass integrand')
Delta = 3*kappa*(1-512*xi/3)
exact(Delta.subs(xi, s.Rational(1, 49152))-s.Rational(287, 96)*kappa, 'physical endpoint threshold')
exact((1/Delta).subs(xi, s.Rational(1, 49152))-s.Rational(96, 287)/kappa, 'physical endpoint inverse')
exact(Delta.subs({xi: 1/(4*g**4), kappa: 2*g**2/spacing})
      -(2*g**2/spacing)*(3-128/g**4), 'original coupling and spacing')
exact((1/(4*g**4)).subs(g**4, 12288)-s.Rational(1, 49152), 'original range')
exact(s.Rational(96, 287)*4-s.Rational(384, 287), 'coarse face fine perimeter factor')
exact(s.Rational(45056, 3)/49152-s.Rational(11, 36), 'source contraction endpoint')

O = s.Matrix([[s.Rational(3,5), -s.Rational(4,5)], [s.Rational(4,5), s.Rational(3,5)]])
exact(O.T*O-s.eye(2), 'spectral coordinate unitary')
examples = 0
for vals in ((6, 9), (7, 13), (11, 17)):
    C = O*s.diag(*vals)*O.T
    lower = s.Rational(3)
    for b0, b1 in ((0,0), (1,2), (-3,1), (2,-5)):
        b = s.Matrix([b0, b1])
        d = s.Rational(3, 2)
        a = lower*d+(b.T*(C-lower*s.eye(2)).inv()*b)[0]+1
        spec_b = O.T*b
        mass = [x*x for x in spec_b]
        exact(sum(mass)-(b.T*b)[0], 'raw complement measure total mass')
        w0 = C.inv()*b
        M10 = (b.T*w0)[0]
        N0 = d+(w0.T*w0)[0]
        E0 = a-M10
        check(E0 >= lower*N0, 'actual lower bound keeps reconstructed mass')
        for shift in (s.Rational(0), s.Rational(1,100), s.Rational(1,3), s.Rational(2), s.Rational(100)):
            res = (C+shift*s.eye(2)).inv()
            w = res*b
            M1 = (b.T*w)[0]
            M2 = (w.T*w)[0]
            energy = a-M1-shift*M2
            norm = d+M2
            schur = a+shift*d-M1
            exact(w0-w-shift*C.inv()*res*b, 'full matrix resolvent difference')
            exact(energy-E0-sum(mass[i]*shift**2/(vals[i]*(vals[i]+shift)**2) for i in range(2)), 'raw energy spectral identity')
            exact(N0-norm-sum(mass[i]*(1/s.Rational(vals[i])**2-1/(s.Rational(vals[i])+shift)**2) for i in range(2)), 'raw norm spectral identity')
            exact(schur-E0-shift*d-sum(mass[i]*shift/(vals[i]*(vals[i]+shift)) for i in range(2)), 'raw Schur memory identity')
            theta = shift/(lower+shift)
            check(0 <= (w0-w).dot(w0-w) <= theta**2*a/lower, 'resolvent continuity inequality')
            check(0 <= energy-E0 <= theta**2*a, 'energy continuity inequality')
            check(0 <= N0-norm <= (1-(lower/(lower+shift))**2)*a/lower, 'mass continuity inequality')
            check(0 <= schur-E0-shift*d <= theta*a, 'memory continuity inequality')
            check(energy >= lower*norm, 'positive shift retains full physical gap')
            examples += 1

receipt = {'status': 'passed', 'exact_assertions': count,
           'noncommuting_chain_examples': chains, 'rational_spectral_examples': examples,
           'scope': 'Original SU2 chain/gauge inverse maps and constants; raw complementary spectral moments and full mass/energy/memory continuity. Analytic Haar, domain and all-box proofs remain in the manuscript and retained source.',
           'sha256': {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                      for name in ('check_physical_complement.py', 'physical_complement_bridge.tex', 'extensive_quantum_blocking.tex')}}
(ROOT/'PHYSICAL_COMPLEMENT_CHECKS.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps(receipt, indent=2))
