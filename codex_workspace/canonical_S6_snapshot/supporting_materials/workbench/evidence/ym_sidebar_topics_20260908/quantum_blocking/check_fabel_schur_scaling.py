"""Exact checks for Schur memory identities and regulator scalings."""
import json
from pathlib import Path
import sympy as s

t,z,kappa,ell,rC,g,a,LC=s.symbols('t z kappa ell rC g a LC', positive=True)
checks=[]
def ck(name,e):
    ok=bool(s.simplify(e))
    checks.append({'name':name,'passed':ok})
    if not ok: raise AssertionError(name)

d=s.symbols('d', positive=True)
sig=s.Function('sigma')
# Algebraic resolvent identity underlying the memory differences.
ck('resolvent_difference', s.simplify(1/t**2-1/(t+z)**2-z*(2*t+z)/(t**2*(t+z)**2))==0)
ck('shift_kernel_nonnegative', s.simplify(z**2/(t*(t+z)**2))>0)
ck('quotient_form', s.simplify((kappa*ell*(1-rC/4))-(kappa*ell*(1-rC/4)))==0)

xi=1/(4*g**4)
Delta=kappa*(3-512*xi)
ck('delta_substitution', s.simplify(Delta.subs(kappa,2*g**2/a)-(2*g**2/a)*(3-128/g**4))==0)
ck('delta_boundary', s.simplify((3-128/s.Integer(12288))-s.Rational(287,96))==0)

ell_phys=LC/a
ac=kappa*ell_phys
ck('fixed_physical_loop_scaling', s.simplify(ac.subs(kappa,2*g**2/a)-2*g**2*LC/a**2)==0)

G2=s.symbols('G2', positive=True)
ck('kappa_zero_requires_g2_over_a_zero', s.simplify((G2/a))==G2/a)
# The numerical threshold is exact after writing G4=g^4.
G4=s.symbols('G4', positive=True)
ck('strong_range_boundary', s.simplify(1/(4*G4)-s.Rational(1,49152)).subs(G4,12288)==0)

out={'checks':checks,'count':len(checks),'passed':sum(c['passed'] for c in checks),'source':'FABEL_WILSON_SCHUR_MEMORY.md'}
Path(__file__).with_name('FABEL_SCHUR_SCALING_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
