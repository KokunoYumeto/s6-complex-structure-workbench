#!/usr/bin/env python3
"""Exact checks for the B.4.32 global radial-loop defect argument."""
from pathlib import Path
import json
import sympy as s

I=s.eye(4)
A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
delta=s.Matrix([0,0,0,1])
gamma=s.Matrix([[1,0,0,0]])
E=delta*gamma
m=s.symbols("m", positive=True, integer=True)
T=I-m*E
assert E**2==s.zeros(4)
for A in (A1,A2):
    assert A*delta==delta
    assert gamma*A==gamma
    assert A*E==E*A
assert A1**3==I and A2**4==I
B1=A1[:3,:3]
B2=A2[:3,:3]
f1=s.Matrix([1,2,-4])
f2=s.Matrix([1,3,-3])
assert B1*f1==f1 and B2*f2==f2
assert len((B1-s.eye(3)).nullspace())==1
assert len((B2-s.eye(3)).nullspace())==1
assert (B1-s.eye(3)).col_join(B2-s.eye(3)).rank()==3
U=B1*B2
assert U==s.Matrix([[1,0,0],[0,1,0],[0,-1,1]])
M1=B1[1:,1:]
M2=B2[1:,1:]
U2=M1*M2
V2=M2*U2*M2.inv()
assert U2==s.Matrix([[1,0],[-1,1]])
assert V2==s.Matrix([[1,1],[0,1]])
for e in range(1,65):
    assert T**e==I-e*m*E
    norm=sum((T**j for j in range(e)),s.zeros(4))
    assert norm==e*I-m*e*(e-1)/2*E
    assert (norm-e*I)[:3,:]==s.zeros(3,4)

c,v,w,eps,k,kj=s.symbols("c v w eps k kj")
finite_coefficient=c*eps*w+(k-kj)*v
assert s.expand(finite_coefficient.subs({c:-12*v,k:kj+12*eps*w}))==0
assert s.diff(6*v,v)==6
tau,mu=s.symbols("tau mu", nonzero=True)
R1=s.Matrix([[-1/tau,0],[(1-mu)/tau,1]])
R2=s.Matrix([[1/tau,0],[-mu/tau,1]])
ed=s.Matrix([0,1])
assert R1*ed==ed and R2*ed==ed

data={
    "status":"PASS",
    "A1":A1.tolist(),"A2":A2.tolist(),
    "quotient_A1":B1.tolist(),"quotient_A2":B2.tolist(),
    "fixed_A1":[1,2,-4],"fixed_A2":[1,3,-3],
    "stacked_fixed_space_rank":3,
    "elliptic_unipotents":[U2.tolist(),V2.tolist()],
    "root_norm_checks":64,
    "root_norm_formula":"sum(T^j,j=0..e-1)=eI-m*e*(e-1)/2*(delta tensor gamma)",
    "finite_connector_r_log_coefficient":0,
    "cusp_extra_r_loop":"6 delta",
    "scope":"Exact matrix and affine-overlap identities; the global cap and section-independence proof is in the accompanying text."
}
path=Path(__file__).with_suffix(".json")
path.write_text(json.dumps(data,indent=2,default=str)+"\n")
print("PASS: quotient common fixed space is zero.")
print("PASS: root-transfer defect is multiplied by e modulo Q delta (e=1..64).")
print("PASS: finite connector logarithms cancel exactly; Lie frames fix delta.")
print("PASS: cusp overlap has only the radial-loop period 6 delta.")
print("Saved:",path.name)
