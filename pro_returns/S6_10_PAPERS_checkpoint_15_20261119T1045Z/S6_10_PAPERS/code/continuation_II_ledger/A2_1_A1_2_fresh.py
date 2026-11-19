#!/usr/bin/env python3
"""New exact certificates for the prereading A.2.1/A.1.2 derivation.

The polynomial families below are exact identities; the graded module
calculations are bounded checks.  The all-r analytic proof is separate.
No stored predecessor program or target proof is imported.
"""
from __future__ import annotations
from datetime import datetime, timezone
from itertools import product
import json
from pathlib import Path
import sympy as S

ROOT = Path(__file__).resolve().parents[2]
checks = []

def check(name, value, evidence):
    ok = bool(value)
    checks.append({"name": name, "pass": ok, "evidence": evidence})
    if not ok:
        raise AssertionError(name)

def divisible(poly, divisor, variables):
    return S.rem(S.Poly(S.expand(poly), *variables),
                 S.Poly(divisor, *variables)).is_zero

for r in range(1, 6):
    x = S.symbols(f'x1:{r+1}')
    a = S.symbols(f'a1:{r+1}')
    F = S.prod(x)
    G = [S.sympify(S.prod(x[j] for j in range(r) if j != i)) for i in range(r)]
    s = sum(G)
    qnum = sum(a[i]*G[i] for i in range(r))
    check(f'r{r}:s_regular', S.gcd(F, s) == 1,
          {'F': str(F), 's': str(s), 'gcd': str(S.gcd(F,s))})
    for i in range(r):
        # In the polynomial ambient domain, (F):(G_i)=(F/gcd(F,G_i)).
        colon = S.cancel(F/S.gcd(F, G[i]))
        check(f'r{r}:colon_{i+1}', S.expand(colon-x[i]) == 0,
              {'colon_generator': str(colon)})
        others = [x[j] for j in range(r) if j != i]
        intersection = S.lcm(others) if others else S.Integer(1)
        check(f'r{r}:intersection_{i+1}', S.expand(intersection-G[i]) == 0,
              {'intersection_generator': str(intersection)})
        check(f'r{r}:idempotent_{i+1}', divisible(G[i]**2-G[i]*s,F,x),
              {'numerator': str(S.expand(G[i]**2-G[i]*s))})
        check(f'r{r}:universal_qdF_{i+1}',
              divisible(qnum*G[i]-a[i]*G[i]*s,F,x+a),
              {'numerator': str(S.expand(qnum*G[i]-a[i]*G[i]*s))})
        for j in range(r):
            gi = G[i].subs(x[j],0)
            sj = s.subs(x[j],0)
            actual = S.cancel(gi/sj)
            check(f'r{r}:branch_{i+1}_{j+1}', actual == int(i == j),
                  {'component': str(actual)})
            if i < j:
                check(f'r{r}:orthogonal_{i+1}_{j+1}',
                      divisible(G[i]*G[j],F,x),
                      {'quotient': str(S.cancel(G[i]*G[j]/F))})

def exponents(n, d):
    return [p for p in product(range(d+1), repeat=n) if sum(p)==d]

graded = []
for r in (2,3):
    for d in range(7):
        # R_d excludes precisely monomials divisible by F=x1...xr.
        rbasis = [p for p in exponents(r,d) if any(v==0 for v in p)]
        bbasis = [(i,p) for i in range(r) for p in exponents(r,d) if p[i]==0]
        A = S.zeros(len(bbasis),len(rbasis))
        indices = {p:j for j,p in enumerate(rbasis)}
        for k,(i,p) in enumerate(bbasis):
            A[k,indices[p]] = 1
        rank = A.rank()
        qdim = len(bbasis)-rank
        expected = (1 if d==0 else 0) if r==2 else (2 if d==0 else 3)
        check(f'r{r}:diagonal_injective_degree_{d}', rank==len(rbasis),
              {'rank':rank,'R_dimension':len(rbasis),'B_dimension':len(bbasis)})
        check(f'r{r}:torsion_quotient_degree_{d}', qdim==expected,
              {'quotient_dimension':qdim,'expected':expected})
        graded.append({'r':r,'degree':d,'R_dimension':len(rbasis),
                       'B_dimension':len(bbasis),'rank':rank,'T_dimension':qdim})

x,y,t = S.symbols('x y t')
F = y*y-x*x*x
dF = S.Matrix([S.diff(F,x),S.diff(F,y)])
u = S.Matrix([-3*y,2*x])
v = S.Matrix([-3*x*x,2*y])
sub = {x:t*t,y:t*t*t}
check('cusp:t_inverse_generator_map',
      all(S.cancel(z)==0 for z in dF.subs(sub)/t-u.subs(sub)),
      {'q':'t^-1','image':str(u)})
check('cusp:unit_generator_map', dF == v, {'q':'1','image':str(v)})
allowed_R = lambda k: k==0 or k>=2
allowed_inverse = [k for k in range(-8,13) if allowed_R(k+3) and allowed_R(k+4)]
check('cusp:fractional_valuation_window', allowed_inverse==list(range(-1,13)),
      {'range':[-8,12],'allowed':allowed_inverse})
quotient = [k for k in allowed_inverse if not allowed_R(k)]
check('cusp:quotient_basis', quotient==[-1,1], {'valuations':quotient})
generated = sorted({k-1 for k in range(0,14) if allowed_R(k)} |
                   {k for k in range(0,13) if allowed_R(k)})
check('cusp:two_fractional_generators_window', generated==list(range(-1,13)),
      {'valuations':generated})

out = {'created_utc':datetime.now(timezone.utc).isoformat(),
       'checker':'GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_10_PAPERS continuation',
       'target_proofs_opened':False,
       'scope':'Fresh exact polynomial and graded-module checks; general analytic proof in the before-read note.',
       'pass':all(c['pass'] for c in checks),'check_count':len(checks),
       'checks':checks,'graded_diagonal_maps':graded}
path = ROOT/'analysis/continuation_II_ledger/A2_1_A1_2_fresh.output.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'pass':out['pass'],'check_count':len(checks),'output':str(path)}))
