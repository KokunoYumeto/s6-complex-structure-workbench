#!/usr/bin/env python3
"""Numerical search for an algebraic counterexample among the eleven CM norms.

This is a finite PSLQ search, not an algebraicity or transcendence certificate.
The source theta values agree independently with heights to >245 decimals.
Search both N and N^12; the latter removes the normalization radicals appearing
in the exact torsion formulas. Preserve every returned vector and residual.
"""
from pathlib import Path
import hashlib
import json
import time
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'records/C_cm_theta_pslq.json'
mp.mp.dps = 235
DEGREES = (4, 8, 12)
POWERS = (1, 12)
MAXCOEFF = 10**12
MAXSTEPS = 20000
TOL = mp.mpf('1e-210')
rows = []
started = time.time()
print('Working precision: 235 decimals; source agreement: >245 decimals.', flush=True)
print('Powers:', POWERS, 'degrees:', DEGREES, 'maxcoeff:', MAXCOEFF,
      'maxsteps:', MAXSTEPS, 'tolerance:', mp.nstr(TOL, 5), flush=True)
for source_row in json.loads(SOURCE.read_text()):
    norm = mp.mpf(source_row['N'])
    for power in POWERS:
        x = norm**power
        for degree in DEGREES:
            vals = mp.matrix([x**k for k in range(degree+1)])
            relation = mp.pslq(vals, tol=TOL, maxcoeff=MAXCOEFF,
                               maxsteps=MAXSTEPS)
            residual = None if relation is None else mp.nstr(
                abs(mp.fsum(c*v for c,v in zip(relation,vals))),220)
            row = dict(index=source_row['index'], j=source_row['j'], power=power,
                       degree=degree, relation=relation, residual=residual)
            rows.append(row)
            print(json.dumps(row), flush=True)
            payload = dict(source='records/C_cm_theta_pslq.json',
                           source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                           working_digits=235, tolerance='1e-210',
                           maxcoeff=MAXCOEFF, maxsteps=MAXSTEPS,
                           diagnostic_only=True, rows=rows)
            (ROOT/'records/C7_norm_polynomial_search.json').write_text(
                json.dumps(payload, indent=2)+'\n')
print('Searches:',len(rows),'returned relations:',
      sum(r['relation'] is not None for r in rows),
      'elapsed_seconds:',round(time.time()-started,3),flush=True)
print('A null result is not a proof excluding every bounded polynomial.',flush=True)
