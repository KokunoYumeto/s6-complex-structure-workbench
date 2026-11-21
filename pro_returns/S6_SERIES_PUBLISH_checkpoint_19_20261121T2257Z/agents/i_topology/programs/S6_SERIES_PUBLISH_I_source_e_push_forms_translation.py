"""Exact algebra for B.4.29's full-rank Tate translation counterexample."""
from pathlib import Path
import json
import sympy as S

x,A,v,u,B,y,t=S.symbols('x A v u B y t',nonzero=True)
j=S.symbols('j',integer=True,positive=True)
chart1=S.Matrix([[A*v,x*v,x*A],[1/x,0,0],[1/x,1/A,0]])
chart2=S.Matrix([[B*y,u*y,u*B],[1/u,1/B,0],[1/u,0,0]])
assert S.simplify(chart1.det())==1
assert S.simplify(chart2.det())==-1
assert S.exp(2*S.pi*S.I*j)==1
assert S.simplify(S.exp(2*S.pi*S.I*(j+S.Rational(1,2))))==-1
N=S.zeros(4);N[0,1]=1;N[2,3]=1
assert N.rank()==2 and N**2==S.zeros(4)
assert S.diff(1/t,t)==-1/t**2
assert S.diff(S.exp(1/t),t)==-S.exp(1/t)/t**2
assert S.simplify((x*A*v)/x)==A*v
assert S.simplify((x*A*v)/A)==x*v

result={'status':'PASS','N_rank':N.rank(),'N_squared_zero':True,
        'canonical_form_chart1_coefficient':str(S.simplify(chart1.det())),
        'canonical_form_chart2_coefficient':str(S.simplify(chart2.det())),
        'two_multiplicative_limits':['1','-1'],
        'first_horizontal_derivative':str(S.diff(1/t,t)),
        'essential_horizontal_derivative':str(S.diff(S.exp(1/t),t)),
        'scope':'Exact chart and form identities. Nonextension and proper-graph restriction are proved geometrically in B.4.29; no claim about differences of two extending sections.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
for key,value in result.items(): print(f'{key}: {value}')
