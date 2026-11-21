#!/usr/bin/env python3
"""Independent exterior-algebra and exact/analytic special-value calculations.

These checks verify the displayed identities at their explicit scope, without
claiming a complete proof of cohomology or branch continuation.
"""
from pathlib import Path
import hashlib, itertools, json
import sympy as S
import mpmath as mp

ROOT=Path(__file__).resolve().parents[1]
def wedge(a,b):
    out={}
    for I,x in a.items():
        for J,y in b.items():
            if set(I)&set(J):continue
            sign=(-1)**sum(i>j for i in I for j in J)
            K=tuple(sorted(I+J));out[K]=S.expand(out.get(K,0)+sign*x*y)
    return {K:S.factor(v) for K,v in out.items() if S.simplify(v)!=0}
x,y,a,m,b,r=S.symbols('x y a m b r',real=True)
D=r-6*m*m/y
period=S.Matrix([[6*a,x,1,0],[6*m,y,0,0],[b,a,0,1],[r,m,0,0]])
eta={(0,3):S.Integer(6),(1,2):S.Integer(1)}
eta_square=wedge(eta,eta)
z2={(0,):b+S.I*r,(1,):a+S.I*m,(3,):S.Integer(1)}
barz1={(0,):6*(a-S.I*m),(1,):x-S.I*y,(2,):S.Integer(1)}
barz2={(0,):b-S.I*r,(1,):a-S.I*m,(3,):S.Integer(1)}
gamma={k:S.I*(barz2.get(k,0)-m*barz1.get(k,0)/y)/(2*D) for k in set(barz1)|set(barz2)}
pair=wedge(wedge(eta,gamma),z2)
assert S.simplify(period.det()-y*D)==0
assert eta_square=={(0,1,2,3):12}
assert pair and list(pair.values())[0]!=0
rho=(1+S.sqrt(3)*S.I)/2
assert S.simplify((1+rho)*(2-rho)/3)==1
assert S.simplify((1+S.I)*(1-S.I)/2)==1
q=S.Rational(1,200)
sum_n5=q*(1+26*q+66*q**2+26*q**3+q**4)/(1-q)**6
e6_tail=S.Rational(504)*S.Rational(67,64)*(sum_n5-q)
assert e6_tail<S.Rational(1,2)
mp.mp.dps=90
rr=(1+mp.sqrt(3)*1j)/2
results=[]
for tau,mu,expected in [(rr,(2-rr)/3,mp.e**(mp.pi*1j/12)*mp.root(3,4)*mp.e**(mp.pi/(6*mp.sqrt(3)))),(1j,(1-1j)/2,mp.sqrt(2)*mp.e**(mp.pi/4))]:
    qq=mp.exp(2*mp.pi*1j*tau)
    value=2*mp.exp(mp.pi*1j*tau/6)*mp.sin(mp.pi*mu)
    for n in range(1,121):
        value*=1-2*qq**n*mp.cos(2*mp.pi*mu)+qq**(2*n)
    residual=abs(value-expected)
    assert residual<mp.mpf('1e-85')
    results.append({'tau':str(tau),'product':str(value),'absolute_residual':str(residual)})
out={'source_program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'real_period_determinant':str(S.factor(period.det())),
     'eta_square_marked_orientation':str(eta_square),
     'eta_square_complex_orientation':-12,
     'eta_gamma01_zeta2_pair':str(pair),
     'isogeny_kernel_identities':'(1+rho)(2-rho)/3=1; (1+i)(1-i)/2=1',
     'E6_tail_bound_at_r_le_1_over_200':str(e6_tail),
     'E6_tail_bound_decimal':str(S.N(e6_tail,24)),
     'special_values':results,
     'scope':'Exact exterior identities and an independent rational E6 tail bound; high-precision product values are floating corroboration only. This program does not certify all proof steps or a continued logarithm by itself.'}
p=ROOT/'records/S6_SERIES_PUBLISH_I_root_exact_checks.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
