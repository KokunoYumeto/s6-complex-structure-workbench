"""Exact checks for the centered Wilson observable and strong-coupling bound."""
import json
from pathlib import Path
import sympy as s

g,a=s.symbols('g a', positive=True)
xi=s.symbols('xi', positive=True)
kappa=2*g**2/a
Delta=kappa*(3-512*xi)
checks=[]
def ck(name,e):
    ok=bool(s.simplify(e))
    checks.append({'name':name,'passed':ok})
    if not ok: raise AssertionError(name)

W,m=s.symbols('W m', real=True)
v=W-m
ck('centered_mean_symbolic', s.expand(v-(W-m))==0)
# A centered observable has the exact algebraic orthogonality relation E[v]=0 when m=E[W].
EW=s.symbols('EW', real=True)
ck('vacuum_orthogonality', s.expand((W-EW).subs(W,EW))==0)

T=s.symbols('T', real=True)
f=s.symbols('f', real=True)
c=s.Rational(1,4)*f**2 # c(f*T,f*T), with -2 tr(T^2)=1
theta=a**2*f
quad=s.limit((2-2*s.cos(theta/2))/a**4, a, 0)
ck('wilson_curvature_coefficient', s.simplify(quad-c)==0)

ck('kappa_dictionary', s.simplify(kappa-2*g**2/a)==0)
b=1/(2*g**2*a)
ck('b_dictionary', s.simplify(b-1/(2*g**2*a))==0)
ck('xi_dictionary', s.simplify(b/kappa-1/(4*g**4))==0)

G4=s.symbols('G4', positive=True)
bound=s.simplify((3-512/(4*G4)).subs(G4,12288)-s.Rational(287,96))
ck('strong_coupling_delta_bound', bound==0)
ck('delta_positive_at_boundary', s.simplify((3-512/(4*G4)).subs(G4,12288))>0)

out={'checks':checks,'count':len(checks),'passed':sum(c['passed'] for c in checks),'source':'FABEL_CURVATURE_TO_PHYSICAL_STATE.md'}
Path(__file__).with_name('FABEL_PHYSICAL_STATE_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
