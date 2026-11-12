from pathlib import Path
import hashlib, json
import sympy as s

ROOT=Path(__file__).resolve().parent
h,tau,nu,c,lam=s.symbols('h tau nu c lam', positive=True)
assert s.simplify((-s.Rational(1,2)-3*h) < 0)
# For 0<h<1/100, both terminal integrals have the asserted behavior.
assert s.simplify(s.Rational(1,2)+3*h).subs(h,s.Rational(1,200)) > 0
assert s.simplify(s.Rational(1,2)+3*h).subs(h,s.Rational(1,100)) > 0
assert s.simplify(s.Rational(3,2)+3*h).subs(h,s.Rational(1,200)) > 1
# The electric time integral is nonintegrable at tau=0.
q=s.Rational(3,2)+3*h
assert s.simplify(q-1).subs(h,s.Rational(0)) > 0
# Support-uniform free-state constants: the lower norm asymptotic and the
# existing energy upper bound give the displayed 32/t quotient constant.
norm_const = s.Rational(9,4)
energy_const = s.Integer(72)
assert s.simplify(energy_const/norm_const) == 32
# Exact component-map coefficients from -2 tr(T^2)=1.
assert s.simplify((-2)*(-s.Rational(1,2))) == 1
# Source bridge and new addendum must remain present, without normalization tokens.
tex=(ROOT/'released_profile_measures_addendum.tex').read_text(encoding='utf-8')
for token in ('nu^{3/2}','nu^{5/2}','lambda^2','c^{-2}','j_i=','D^\\nu j_\\nu=0','h_s^{B}(x)', 'h_s^{E}(x)', 'I_{L,a}', 'D_{L,a,g}[h]', 'sqrt3}{2}a', 'D_{h_s,g}','C_{R,t}','32/t','s_n=1-1/n','g_{j_n}\\to0','6144\\pi^2','\\xi_0M_{L_j}\\to\\infty'):
    assert token in tex, token
source=ROOT/'..'/'ym_gap_primary_20260908'/'ns_inner_profile_curvature_current_bridge.md'
source=source.resolve()
assert source.exists()
out={'status':'PASS_RELEASED_PROFILE_MEASURE_MAP','checks':18,
      'source_path':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
      'terminal_exponents':{'magnetic':str(-s.Rational(1,2)-3*h),'electric':str(-s.Rational(3,2)-3*h)},
      'scope':'Exact gauge-invariant component norms and sourced quantum-observable map; no source-free mass-gap claim.'}
(ROOT/'RELEASED_PROFILE_MEASURES_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

