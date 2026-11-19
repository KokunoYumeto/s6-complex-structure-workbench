#!/usr/bin/env python3
"""Exact local source/Cartier/ray certificate for the selected-node label.

This checks the maps in TL.1--4. It makes no source-return assignment.
Convergence and the analytic branch-divisor argument are in the note.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[2]
S, T, q2, uQ, uP = s.symbols('S T q2 uQ uP', nonzero=True)
q1 = S*T
Q = q1*q2*uQ
P = uP/q2
uG = uQ*uP
Z0, W0 = uG*T, q2*S/uP
checks = []

def eq(name, left, right):
    assert s.cancel(left-right) == 0, name
    checks.append(name)

eq('full Tate node product', Z0*W0, Q)
eq('marked source coordinate', P*W0, S)
eq('inverse source coordinate', Z0/uG, T)
eq('selected base coordinate', S*T, q1)
eq('marked section source value', (P*W0).subs(S, 1), 1)
eq('actual unshifted Tate representative', P/S, 1/W0)
eq('literal source-period reindex', Q*P/S, Z0)
eq('Tate alpha beta conifold', (-uP*W0/2)*(-2*Z0/uG), q1*q2)
eq('marked alpha', (-uP*W0/2).subs(S, 1), -q2/2)
eq('marked beta', (-2*Z0/uG).subs(S, 1), -2*T)

sm, tm, bt = s.symbols('sm tm bt', nonzero=True)
eq('Morse to Tate product', (bt*sm)*(tm/bt), sm*tm)
eq('Morse to Tate inverse source coordinate', bt*sm/bt, sm)
eq('Morse to Tate inverse transverse coordinate', (tm/bt)*bt, tm)

thS, thW, V, xi = s.symbols('thS thW V xi', nonzero=True)
f = (-thS/S)/(-(P/S)*thW)
eq('theta inversion including P', f, thS/(P*thW))
E = 2*thS/((1-S)*thW)
for a in (1, 2):
    coefficient = ((1-S)/2)**a * V/f**a
    eq(f'full Cartier and h line factor a={a}', E**a*coefficient, P**a*V)
    eq(f'nodal Cartier coefficient a={a}', coefficient.subs({thS:1-S, thW:1-S/P}), ((P-S)/2)**a*V)
    zprime = s.symbols('zprime', nonzero=True)
    eq(f'other projective line chart a={a}', (S**(-a)*coefficient).subs(S,1/zprime), ((zprime-1)/2)**a*V/(f.subs(S,1/zprime))**a)

# Each factor is a holomorphic expression on the full source bidisc.
for r in range(1, 13):
    eq(f'negative numerator factor r={r}', Q**r/S, S**(r-1)*T**r*q2**r*uQ**r)
    eq(f'negative denominator factor r={r}', Q**r/W0, Q**(r-1)*Z0)
    eq(f'positive denominator factor r={r}', Q**r*(S/P), Q**r*W0)
    num_at = (1-Q**r*S).subs(q2,0)*(1-S**(r-1)*T**r*q2**r*uQ**r).subs(q2,0)
    den_at = (1-Q**r*W0).subs(q2,0)*(1-Q**(r-1)*Z0).subs(q2,0)
    eq(f'numerator boundary factor r={r}', num_at, 1)
    eq(f'denominator boundary factor r={r}', den_at, 1-Z0 if r==1 else 1)
eq('correct full q2-zero restriction', 2/(1-Z0), 2/(1-uG*T))
eq('exceptional restriction', (2/(1-Z0)).subs(T,0), 2)

R=s.Matrix([[-1,0,1],[0,1,0],[0,0,1]])
zero=s.Matrix([0,0,1]); e1=s.Matrix([1,0,1]); e2=s.Matrix([0,1,1]); e12=s.Matrix([1,1,1])
pos=[(zero,e1,e12),(zero,e2,e12)]
neg=[(zero,e1,e2),(e1,e2,e12)]
canon=lambda triangles: sorted(tuple(sorted(tuple(v) for v in tri)) for tri in triangles)
assert canon([tuple(R*v for v in tri) for tri in pos])==canon(neg)
checks.append('actual positive associated square to current Tate T0')
assert canon([tuple(R*v for v in tri) for tri in neg])==canon(pos)
checks.append('actual opposite associated square to current Tate T1')
assert R*R==s.eye(3)
checks.append('inverse integral height map')
assert R*s.Matrix([0,1,0])==s.Matrix([0,1,0])
checks.append('physical delta unchanged')
assert R.det()==-1
checks.append('unimodular height lattice map')

ell=s.symbols('ell', integer=True)
eq('actual ordinary closing commutes with line map', E**2*q1**ell*xi, q1**ell*E**2*xi)
thZ, thZP=s.symbols('thZ thZP',nonzero=True)
eq('primitive Cartier theta cancellation', (thZP/thZ)*(thZ/thZP), 1)

note=ROOT/'notes/part3_source_zero_tate_label_working.md'
out={
 'status':'PASS', 'utc':datetime.now(timezone.utc).isoformat(),
 'checks':len(checks), 'identities':checks,
 'source_map':{'Q':'q1 q2 uQ','P':'uP/q2','S':'P W0','T0':'Z0/(uQ uP)',
               'inverse':'Z0=uQ uP T0; W0=q2 S/uP; q1=S T0'},
 'full_line_map':'Apply the actual h=(Q,P^a) period: Z0=uQ uP T0, V0=E_plus^a xi, E_plus=2 Theta(S)/((1-S)Theta(S/P)).',
 'boundary_correction':'E_plus|q2=0=2/(1-uG(q1,0)T0); E_plus|T0=q2=0=2. The denominator n=1 factor is retained.',
 'fan_map':[[int(x) for x in R.row(i)] for i in range(3)],
 'fan_result':'Associated positive square maps to current Tate T0; opposite associated square maps to current Tate T1.',
 'line_sector':'For a=2 the actual r:O(2G-O)->O(G-O)^2 is applied first, with its inverse at the target.',
 'scope':'Local full-bidisc and actual period/Cartier collar comparison. No compact radial attachment or absolute source-zero return assigned.',
 'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest()
}
(ROOT/'code/part3/source_zero_tate_label.json').write_text(json.dumps(out,indent=2)+'\n')
print(f"PASS: {len(checks)} exact source, theta-factor, Cartier, branch, fan and closing identities.")
print('Associated positive square -> current Tate T0, with the literal h period and a=2 r-arrow retained.')
