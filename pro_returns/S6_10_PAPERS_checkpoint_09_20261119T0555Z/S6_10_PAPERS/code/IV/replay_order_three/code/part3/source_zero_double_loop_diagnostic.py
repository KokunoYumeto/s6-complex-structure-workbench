from pathlib import Path
import json
import sympy as s
r=Path(__file__).resolve().parents[2]
a,b,N=s.symbols('a b N',integer=True)
t=N-1
l=s.Matrix([2*(N+a-2),2*(1-b),2*(N-2)])
w=s.Matrix([0,1,-1]);d=s.Matrix([-2,-1,-1])
I=s.Matrix([t*w[i]+d[i]*(l[i]-t) for i in range(3)])
W=s.Matrix([t*w[i]-d[i]*(l[i]-t) for i in range(3)])
expectedI=s.Matrix([-2*(N+2*a-3),2*N+2*b-4,-2*N+4])
expectedW=s.Matrix([2*(N+2*a-3),2-2*b,-2])
assert all(s.expand(x)==0 for x in I-expectedI)
assert all(s.expand(x)==0 for x in W-expectedW)
V22=-I[2];delta2=W[0]-W[2]
assert s.expand((delta2-V22)/2-2*a)==0
out={'status':'PASS_ALGEBRA_ONLY','checks':7,
     'I':[str(s.expand(x)) for x in I],
     'W':[str(s.expand(x)) for x in W],
     'V22_expression':str(s.expand(V22)),
     'delta2_expression':str(s.expand(delta2)),
     'right_integer_expression':'2a',
     'actual_closed_plumbing_comparison':'not yet proved',
     'return_relation_assigned':False,
     'proof':'notes/part3_source_zero_double_loop_diagnostic.md'}
(r/'code/part3/source_zero_double_loop_diagnostic.json').write_text(json.dumps(out,indent=2)+'\n')
(r/'code/part3/source_zero_double_loop_diagnostic.out').write_text('PASS: 7 algebraic identities; actual closing/plumbing comparison and return unassigned.\n')
print('PASS: 7 algebraic identities; actual closing/plumbing comparison and return unassigned.')
