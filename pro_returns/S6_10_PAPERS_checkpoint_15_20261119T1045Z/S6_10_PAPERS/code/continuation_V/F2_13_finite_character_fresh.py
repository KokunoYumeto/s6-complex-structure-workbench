"""Exact companion quotient characters, from the independently generated matrices."""
from pathlib import Path
import json
import sympy as S

root=Path(__file__).resolve().parents[2]
data=json.loads((root/'code/continuation_V/F2_13_companion_explore_fresh.output.json').read_text())
x=S.symbols('x');out={}
for case,d in data.items():
    a=S.Matrix(d['a5']);b=S.Matrix(d['b5'])
    pa=a.charpoly(x).as_expr();pb=b.charpoly(x).as_expr()
    expected=(x-1)*(x+1)**2*(x*x+(1 if case=='A' else -1)*x+1)
    assert S.expand(pa-(x**5-1))==0
    assert S.expand(pb-expected)==0
    assert (a-S.eye(5)).rank()==4 and (b-S.eye(5)).rank()==4
    assert all(a**j!=S.eye(5) for j in range(1,5))
    assert all(b**j!=S.eye(5) for j in range(1,6))
    out[case]={'a_characteristic':str(pa),'b_characteristic':str(pb),'fixed_ranks':[1,1],'exact_orders':[5,6]}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print('Both exact characters, fixed ranks and orders passed.')
