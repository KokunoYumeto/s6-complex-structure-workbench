#!/usr/bin/env python3
"""Exact relative-group coordinates, including the reverse-flop audit.

No cross-edge identification in a periodic fan is inferred by this program.
"""
from pathlib import Path
import json
import sympy as s

m,n,c,r = s.symbols('m n c r', integer=True)
M = s.Matrix([[0,-1],[1,2]])
assert M.det() == 1
assert M.inv() == s.Matrix([[2,1],[-1,0]])
N = M-s.eye(2)
assert N*N == s.zeros(2)
forward = (-n, m+2*n, c+n)
reverse = (2*m+n, -m, c+m)
mf,nf,cf = forward
assert tuple(s.expand(z) for z in (2*mf+nf,-mf,cf+mf)) == (m,n,c)
t = m+n
power = (m-r*t, n+r*t, c+r*n+r*(r-1)*t/2)
mr,nr,cr = power
step = tuple(s.expand(z) for z in (-nr,mr+2*nr,cr+nr))
assert all(s.simplify(a-b)==0 for a,b in zip(step,[z.subs(r,r+1) for z in power]))
A,k = s.symbols('A k', integer=True)
initial = (-k+6*A,-6*A,A)
after = tuple(s.expand(z.subs({m:initial[0],n:initial[1],c:initial[2]})) for z in forward)
assert after == (6*A,-k-6*A,-5*A)
back = tuple(s.expand(z.subs({m:after[0],n:after[1],c:after[2]})) for z in reverse)
assert back == initial
data={
 'scope':'relative-group algebra in one marked exterior; not a cross-edge map',
 'forward': [str(z) for z in forward],
 'reverse': [str(z) for z in reverse],
 'integer_power': [str(z) for z in power],
 'fixed_edge_initial': [str(z) for z in initial],
 'fixed_edge_after': [str(z) for z in after],
 'fixed_edge_reverse': [str(z) for z in back],
 'geometric_limitation':'T^r is an algebraic iterate of the marked exterior map. It is not assigned to a sequence of different toric edge flops without their actual intervening normal-product identifications.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print('PASS: exact forward/reverse relative coordinates; fixed-edge inverse restores the original class.')
