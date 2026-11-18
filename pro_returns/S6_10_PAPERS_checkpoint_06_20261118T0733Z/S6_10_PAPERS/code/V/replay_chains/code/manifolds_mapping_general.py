"""Exact all-order marked quotient cube algebra, B6.23.

The geometric higher-node split is B6.22 (maps). The actual multiplicative
collar comparison is the proof of B6.20 and manifolds_mapping_general_proof.tex.
All calculations below are symbolic, with no multiplicity cutoff.
"""
from pathlib import Path
import json
import sympy as s
A,B,h=s.symbols('A B h',integer=True)
P=4*A+3*B
A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
C1=s.eye(4);C1[2,0]=-1;C1[2,1]=1
C2=s.eye(4);C2[2,0]=1;C2[3,0]=-1
assert A1*A2*C1*C2==s.eye(4)
a1=s.eye(4)[:,2];a2=a1-s.eye(4)[:,3]
ell=[s.Matrix([0,0,-2*A,0]),s.Matrix([0,-B,0,0]),2*A*a1,-B*a2]
r=s.Matrix([-B,2*A-B,2*B-2*A,0])
matrices=[A1,A2,C1,C2]
d=[s.simplify(v+(s.eye(4)-M)*r) for M,v in zip(matrices,ell)]
expected=[s.Matrix([0,P,-P,-2*A-B]),s.Matrix([0,0,-P,2*A+B]),s.zeros(4,1),s.zeros(4,1)]
assert d==expected
Q=[]
for M,v in zip(matrices,d):
    lift=M.row_join(-v).col_join(s.Matrix([[0,0,0,0,1]]))
    Q.append(lift.extract([0,1,2,4],[0,1,2,4]))
assert s.simplify(Q[0]*Q[1]*Q[2]*Q[3])==s.eye(4)
assert s.simplify(Q[0]**3)==s.eye(4) and s.simplify(Q[1]**4)==s.eye(4)
G,U,W,K=[s.eye(4)[:,i] for i in range(4)]
eta=[-4*G-W+(P-2*A-B)*K,-3*G+U+(2*A+B)*K,s.zeros(4,1)]
beta=[-s.Rational(2,3)*A*K,-s.Rational(1,2)*B*K,s.zeros(4,1)]
lam=[(-U+W)/3,(-U+W)/2,s.zeros(4,1)]
b=[s.simplify(e-z) for e,z in zip(eta,beta)]
assert b[0]==-4*G-W+s.Rational(2,3)*P*K
assert b[1]==-3*G+U+s.Rational(1,2)*P*K
for i in range(3):assert s.simplify((Q[i].T-s.eye(4))*lam[i]-b[i])==s.zeros(4,1)
last=[-Q[3].T*Q[2].T*Q[1].T*eta[0],-Q[3].T*Q[2].T*eta[1],-Q[3].T*eta[2]]
last=[s.simplify(x) for x in last]
assert s.simplify(sum(last,s.zeros(4,1)))==G
assert (Q[3].T-s.eye(4))*W==G

def term(l,z):return s.simplify(3*h*s.Matrix.hstack(l,G,K,z).det())
contributions=[term(l,z) for l,z in zip(lam,b)]
current=W;lastvalue=0
for z in last:
    lastvalue+=term(current,z);current+=z
lastvalue=s.simplify(lastvalue)
contributions.append(lastvalue)
assert contributions==[h,-3*h/2,0,0]
assert sum(contributions)==-h/2
# The inverse mapping-torus convention reverses every collar contribution.
for i in range(3):
    invb=-Q[i].inv().T*b[i]
    assert s.simplify((Q[i].inv().T-s.eye(4))*lam[i]-invb)==s.zeros(4,1)
    assert s.simplify(term(lam[i],invb)+contributions[i])==0
record=dict(A='l*N0',B='k*N1',P=str(P),positive_period='h=2*k*l',
    integral_parameter_shear=[str(x) for x in r],
    transformed_defects=[[str(x) for x in v] for v in d],
    quotient_matrices=[[[str(x) for x in row] for row in M.tolist()] for M in Q],
    eta=[[str(x) for x in v] for v in eta],beta=[[str(x) for x in v] for v in beta],
    boundary_differences=[[str(x) for x in v] for v in b],
    primitives=[[str(x) for x in v] for v in lam],
    last_segments=[[str(x) for x in v] for v in last],
    raw_contributions=[str(x) for x in contributions],raw_cube='-h/2=-k*l',
    inverse_convention_verified=True,
    orientation='P=1 calibrated to minimal case; P=-1 by global fibre inversion reversing Euler and quotient orientation together',
    geometric_scope='Requires the actual higher-node marked split, B6.22; symbolic calculation holds all positive k,l and P=+-1.')
print(json.dumps(record,indent=2))
Path(__file__).with_suffix('.out.json').write_text(json.dumps(record,indent=2)+'\n')
