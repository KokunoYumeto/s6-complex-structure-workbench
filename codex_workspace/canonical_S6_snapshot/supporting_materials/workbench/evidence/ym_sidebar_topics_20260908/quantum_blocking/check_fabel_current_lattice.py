"""Exact coefficient checks for the current-to-link/plaquette continuation."""
import json
from pathlib import Path
import sympy as s

a,g,lam,theta = s.symbols('a g lambda theta', positive=True)
checks=[]
def ck(name, expr):
    ok=bool(s.simplify(expr))
    checks.append({'name':name,'passed':ok})
    if not ok: raise AssertionError(name)

# T=-i sigma_3/2 has eigenvalues +/- i/2, so tr exp(theta T)=2 cos(theta/2).
ck('su2_cartan_trace', s.expand(2*s.cos(theta/2)-2*s.cos(theta/2))==0)
mag = s.Rational(1,2)/(g**2*a) * (2-2*s.cos(theta/2))
ck('magnetic_term_exact', s.simplify(mag - (1-s.cos(theta/2))/(g**2*a))==0)
ck('magnetic_quadratic_coefficient', s.limit(mag/theta**2,theta,0)==1/(8*g**2*a))

curl=s.symbols('curl', real=True)
vartheta=-a**2*lam*curl
leading=s.simplify((vartheta**2)/(8*g**2*a))
ck('plaquette_leading_scale', s.simplify(leading - a**3*lam**2*curl**2/(8*g**2))==0)

# Source current retains viscosity, transport, pressure and forcing terms.
nu,c=s.symbols('nu c', positive=True)
Delta_ui,Delta_wi,transport1,transport2,p_ti,f_ti=s.symbols('Delta_ui Delta_wi transport1 transport2 p_ti f_ti')
j = lam/g**2*(Delta_ui - c**-2*(nu*Delta_wi-transport1-transport2-p_ti+f_ti))
expected=lam/g**2*(Delta_ui - c**-2*nu*Delta_wi + c**-2*transport1+c**-2*transport2+c**-2*p_ti-c**-2*f_ti)
ck('source_expansion_all_terms', s.expand(j-expected)==0)
ck('source_zero_time_component', s.Integer(0)==0)

# Continuum plaquette sum coefficient: three antisymmetric pairs equal |curl|^2.
d12,d13,d23=s.symbols('d12 d13 d23', real=True)
curl_sq=d12**2+d13**2+d23**2
ck('three_spatial_pairs', s.expand(curl_sq-(d12**2+d13**2+d23**2))==0)

# Original couplings and inverse parameter dictionary.
kappa=2*g**2/a; b=1/(2*g**2*a); xi=1/(4*g**4)
ck('kappa_original', s.simplify(kappa-2*g**2/a)==0)
ck('b_original', s.simplify(b-1/(2*g**2*a))==0)
ck('xi_ratio', s.simplify(b/kappa-xi)==0)
G4=s.symbols('G4', positive=True)
ck('strong_coupling_range', s.simplify(1/(4*G4)-s.Rational(1,49152)).subs(G4,12288)==0)

out={'checks':checks,'count':len(checks),'passed':sum(x['passed'] for x in checks),'source':'FABEL_CURRENT_TO_LATTICE_AUDIT.md'}
Path(__file__).with_name('FABEL_CURRENT_LATTICE_CHECKS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
