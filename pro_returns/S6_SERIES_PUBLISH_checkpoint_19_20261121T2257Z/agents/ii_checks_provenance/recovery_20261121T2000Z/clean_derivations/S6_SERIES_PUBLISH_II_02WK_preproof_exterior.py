"""Universal exterior trace certificate, written before the WK proof release."""
from itertools import combinations,permutations
import sympy as s
import json
x=s.symbols('x0:16');B=s.Matrix(4,4,x)
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def minor_by_permutations(M,rows,cols):
    return s.Add(*(sign(p)*s.prod(M[rows[i],cols[p[i]]] for i in range(len(rows))) for p in permutations(range(len(rows)))))
traces=[s.Integer(1)]
dimensions=[1]
for k in range(1,5):
    basis=list(combinations(range(4),k));dimensions.append(len(basis))
    traces.append(s.expand(sum(minor_by_permutations(B,I,I) for I in basis)))
alternating=s.expand(sum((-1)**k*traces[k] for k in range(5)))
determinant=s.expand((s.eye(4)-B).det(method='domain-ge'))
assert s.expand(alternating-determinant)==0
transpose_traces=[s.Integer(1)]
for k in range(1,5):
    transpose_traces.append(s.expand(sum(minor_by_permutations(B.T,I,I) for I in combinations(range(4),k))))
assert traces==transpose_traces
assert dimensions==[1,4,6,4,1]
assert alternating.subs(dict(zip(x,(-s.eye(4)).reshape(16,1))))==16
assert alternating.subs(dict(zip(x,s.eye(4).reshape(16,1))))==0
print(json.dumps({'timing':'before 02WK target proof release',
 'method':'construct exterior diagonal matrix entries by signed permutation minors; compare their alternating trace with a separate exact determinant algorithm',
 'variables':16,'exterior_dimensions':dimensions,
 'trace_identity_zero_residual':True,'transpose_transport_checked':True,
 'identity_value':0,'minus_identity_value':16,
 'bound_scope':'universal root-of-unity/conjugate-pair argument in the frozen derivation; endpoint evaluations are checks, not the proof of the bound',
 'events_added':0,'all_assertions_passed':True},indent=2))
