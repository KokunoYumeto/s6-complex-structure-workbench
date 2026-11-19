"""Exact fourfold moving-pencil and boundary-coordinate computation."""
from pathlib import Path
from fractions import Fraction
from math import floor,ceil
import json,hashlib
rows=[]
for m in range(1,21):
    n=6*m;low=ceil(Fraction(3*n,4));high=floor(Fraction(4*n,5));d=high-low
    rows.append({'anti_canonical_power':m,'L_power':n,'minimum_lambda_exponent':low,'maximum_lambda_exponent':high,'coarse_degree':d,'h0':max(0,d+1)})
assert rows[3]['L_power']==24 and rows[3]['h0']==2
assert rows[3]['minimum_lambda_exponent']==18 and rows[3]['maximum_lambda_exponent']==19
assert all(r['h0']<2 for r in rows[:3])
assert rows[19]['coarse_degree']==6
import sympy as s
t,R,H=s.symbols('t R H',real=True);u=1/(R-s.I*H)
assert s.simplify(s.im(1/u)+H)==0
ramified=[]
for m in range(1,13):
    assert s.diff(t**m,t)==m*t**(m-1)
    assert s.diff(t**(-m),t)==-m*t**(-m-1)
    ramified.append({'degree':m,'finite_derivative':str(s.diff(t**m,t)),'infinity_derivative':str(s.diff(t**(-m),t))})
out={'status':'PASS','moving_pencil':{'sections':['lambda^18','lambda^19'],'ratio':'lambda','power':'K^-4','coarse_line':'O(1)'},'root_line_table':rows,'boundary_curve':'u=1/(R-i*h(lambda)) tends to0 and Im(1/u)+h(lambda)=0','finite_cover_examples':ramified,'scope':'Exact root-line dimensions, explicit cancelled-monomial ratio, reciprocal boundary curve and coordinate derivatives; the analytic proof and universal finite-cover argument are in prederivations11.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS K^-4 moving pencil: lambda^18,lambda^19; ratio=lambda; boundary reciprocal identity')
