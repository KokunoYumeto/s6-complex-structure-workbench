#!/usr/bin/env python3
"""Exact duplication/Bezout height bounds used with Miller's BSD theorem.

No high-precision canonical-height routine is used in this certificate.
Integer homogeneous Bezout identities give a global height difference bound;
six exact doublings and Arb logarithms then enclose the canonical height.
"""
from pathlib import Path
from fractions import Fraction
import csv, json, math, sys
import sympy as S
from flint import arb, ctx

sys.set_int_max_str_digits(100000)
ctx.prec = 160
root = Path(__file__).resolve().parents[1]
x = S.symbols('x')
rows = {int(r['index']): r for r in csv.DictReader(open(root/'results_Crank.csv'))}
cases = [(3, 0, -2156, 38416), (5, 0, -140, 784), (7, 1, -38, 90)]
out = []
for idx, a3, a4, a6 in cases:
    # Completing the square leaves x and therefore its canonical height unchanged.
    A = S.Rational(a4)
    B = S.Rational(a6) + S.Rational(a3*a3, 4)
    fp = x**4-2*A*x*x-8*B*x+A*A
    gp = 4*(x**3+A*x+B)
    den = S.ilcm(*[z.q for z in S.Poly(fp,x).all_coeffs()+S.Poly(gp,x).all_coeffs()])
    fp, gp = S.expand(den*fp), S.expand(den*gp)
    common = S.igcd(*S.Poly(fp,x).all_coeffs(), *S.Poly(gp,x).all_coeffs())
    fp, gp = S.expand(fp/common), S.expand(gp/common)
    mat = S.Matrix([[S.expand(pol*x**j).coeff(x,k)
                     for pol in (fp,gp) for j in range(4)] for k in range(8)])
    solutions = [mat.inv()*S.eye(8)[:, k] for k in (0,7)]
    D = int(S.ilcm(*[v.q for sol in solutions for v in sol]))
    ints = [[int(v*D) for v in sol] for sol in solutions]
    for k, v in zip((0,7), ints):
        lhs = sum(v[j]*x**j for j in range(4))*fp + sum(v[4+j]*x**j for j in range(4))*gp
        assert S.expand(lhs-D*x**k)==0
    # Homogenization gives D Z^7 and D X^7 with degree-three cofactors.
    cbez = max(sum(abs(a) for a in v) for v in ints)
    cup = max(sum(abs(int(c)) for c in S.Poly(pol,x).all_coeffs()) for pol in (fp,gp))
    C = max(cbez, cup, 1)
    n, d = 0, 1
    doubles=[]
    fcoeff=[int(fp.coeff(x,j)) for j in range(5)]
    gcoeff=[int(gp.coeff(x,j)) for j in range(5)]
    for k in range(1,7):
        fn=sum(fcoeff[j]*n**j*d**(4-j) for j in range(5))
        gn=sum(gcoeff[j]*n**j*d**(4-j) for j in range(5))
        assert gn != 0
        gg=math.gcd(fn,gn)
        n,d=fn//gg,gn//gg
        if d<0:n,d=-n,-d
        doubles.append([str(n),str(d)])
    centre=arb(max(abs(n),abs(d))).log()/(2*4**6)
    radius=arb(C).log()/(6*4**6)
    height=centre+arb(0,radius.upper())
    # The derivative/period quotient error is bounded in C.6.R2.  The
    # very loose radius below also includes rounding of its saved decimal.
    lratio=arb(rows[idx]['Lprime_over_Omega'])+arb(0,'1e-55')
    bsd=lratio/(4*height)
    assert bsd>arb(1)/2 and bsd<arb(3)/2
    print('INDEX',idx,'D',D,'C',C)
    print('F',fp,'G',gp)
    print('Bezout Z7',ints[0],'Bezout X7',ints[1])
    print('height enclosure',height,'radius',radius)
    print('BSD quotient enclosure',bsd,'unique possible positive integer: 1')
    out.append(dict(index=idx,D=D,C=C,F=fcoeff,G=gcoeff,bezout=ints,
                    doublings=doubles,height=str(height),bsd=str(bsd)))
(root/'records/C_height_coarse_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('ALL THREE INTEGER BSD QUOTIENTS CERTIFIED EQUAL TO 1, assuming Miller Theorem 1.2 as verified.')
