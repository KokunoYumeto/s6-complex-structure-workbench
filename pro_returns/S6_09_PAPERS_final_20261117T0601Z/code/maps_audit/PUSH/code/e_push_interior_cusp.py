"""Exact checks used in E.2.16; the infinite triangle argument is in prose."""
from pathlib import Path
import json
import sympy as sp

A1=sp.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=sp.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
A0=sp.Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
I=sp.eye(4)
common=(A1.T-I).col_join(A2.T-I).nullspace()
cusp=(A0.T-I).nullspace()
assert common==[sp.Matrix([1,0,0,0])]
assert len(cusp)==2
assert A1**3==I and A2**4==I

# Composition is right factor first, as in the proof.
a={1:2,2:3,3:1,4:4}
b={1:3,3:2,2:4,4:1}
ab={j:a[b[j]] for j in range(1,5)}
assert ab=={1:1,2:4,3:3,4:2}

ca,sa,cb,sb,L=sp.symbols('ca sa cb sb L', real=True)
R1=sp.Matrix([[ca,sa],[-sa,ca]])
R2=sp.Matrix([[cb,sp.exp(L)*sb],[-sp.exp(-L)*sb,cb]])
trace=sp.simplify(sp.trace(R1*R2))
assert sp.simplify(trace-(2*ca*cb-2*sp.cosh(L)*sa*sb))==0
assert sp.Rational(1,3)+sp.Rational(1,4)+sp.Rational(1,3)==sp.Rational(11,12)
assert sp.Rational(1,3)+sp.Rational(1,8)+sp.Rational(1,2)==sp.Rational(23,24)

out={
 'common_dual_invariants':[list(v) for v in common],
 'cusp_invariant_dimension':len(cusp),
 'exceptional_permutation_product':ab,
 'triangle_trace':str(trace),
 'status':'PASS',
 'scope':'Integral invariant ranks and exact representation identities; not a numerical proof of the analytic assertions.'
}
print(json.dumps(out,default=str,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,default=str,indent=2)+'\n')
