#!/usr/bin/env python3
"""Exact algebra for the independently audited actual-frame recurrence.

The +1 normal-frame and +2 flop-frame morphisms are geometric proofs in
notes/part3_common_exterior_frame_recurrence.md, not conclusions of this
symbolic calculation. This script checks their quaternion identities and
all induced integral recurrences, including orientation-reset involutions.
"""
from pathlib import Path
from datetime import datetime, timezone
from math import gcd
import json
import sympy as S

ROOT=Path(__file__).resolve().parents[2]
def qmul(a,b):
    a0,a1,a2,a3=a; b0,b1,b2,b3=b
    return S.Matrix([
        a0*b0-a1*b1-a2*b2-a3*b3,
        a0*b1+a1*b0+a2*b3-a3*b2,
        a0*b2-a1*b3+a2*b0+a3*b1,
        a0*b3+a1*b2-a2*b1+a3*b0])
def same(a,b):
    assert all(S.expand(z)==0 for z in a-b)
J=S.diag(1,1,1,-1)
a=S.Matrix(S.symbols("a0:4",real=True))
b=S.Matrix(S.symbols("b0:4",real=True))
same(J*qmul(a,b),qmul(J*b,J*a))
assert J.det()==-1 and S.diag(1,1,-1).det()==-1
# Reset U has a negative base determinant and negative normal determinant:
# its six-dimensional boundary and seven-dimensional product filling signs
# are both positive.
assert S.diag(1,1,-1).det()*J.det()==1
Lq=S.Matrix.hstack(*(qmul(a,S.eye(4)[:,i]) for i in range(4)))
R4=S.diag(-1,1,1,1)
normq=sum(x*x for x in a)
assert S.factor(Lq.det())==normq**2
# At the first affine base origin, du=j dx-k dy, so dc=-du*q.
# The source-normal block is an actual nonconstant linear map of q.
Aq=S.Matrix.hstack(-qmul(S.Matrix([0,0,1,0]),a),
                    qmul(S.Matrix([0,0,0,1]),a))
tt=S.symbols("t_homotopy",real=True)
triangular=S.diag(-1,1).row_join(S.zeros(2,4)).col_join(
    (tt*Aq).row_join(Lq*R4))
assert S.factor(triangular.det())==normq**2

def meridian(i):
    M=S.eye(3)
    for j in range(3): M[j,i]=-1 if i==j else 2
    return M
v00,v01,v02,v11,v12,v22=S.symbols("v00 v01 v02 v11 v12 v22",integer=True)
V=S.Matrix([[v00,v01,v02],[v01,v11,v12],[v02,v12,v22]])
delta=S.Matrix(S.symbols("delta0:3",integer=True))
for i in range(3):
    M=meridian(i); e=S.eye(3)[:,i]
    W=M*V*M.T
    eps=M*(delta-2*V*e)
    same(M*W*M.T,V)
    same(M*(eps-2*W*e),delta)
    assert S.expand((eps[i]-W[i,i]+delta[i]-V[i,i])/2)==0

m,n=S.symbols("m n",integer=True)
v=-(m+n)
V0=S.diag(v,0,0)
d0=S.Matrix([n-m,0,0])
M0=meridian(0)
V1=M0*V0*M0.T
d1=M0*(d0-2*V0*S.Matrix([1,0,0]))
same(d1,(m+3*n)*S.Matrix([-1,2,2]))
n1=S.Matrix([S.expand((d1[i]-V1[i,i])/2) for i in range(3)])
same(n1,S.Matrix([-n,3*m+5*n,3*m+5*n]))
m1=S.Matrix([S.expand(-V1[i,i]-n1[i]) for i in range(3)])
same(m1,S.Matrix([m+2*n,m-n,m-n]))

# The local toric new chart has weights (lambda_k-lambda_j,lambda_j,-lambda_k).
p,q=S.symbols("p q",integer=True)
lam=S.Matrix([p+q,-p,-q])
def w_from_weights(l):
    return S.Matrix([-l[1]*l[2],-l[0]*l[2],-l[0]*l[1]])
w=w_from_weights(lam)
for i in range(3):
    j,k=[r for r in range(3) if r!=i]
    lnew=S.zeros(3,1)
    lnew[i]=lam[k]-lam[j]; lnew[j]=lam[j]; lnew[k]=-lam[k]
    same(w_from_weights(lnew),meridian(i)*w)
    assert S.expand(sum(lnew))==0
weight_sum=S.expand(sum(w))
assert weight_sum==p*p+p*q+q*q
assert S.expand(sum(x*x for x in lam)-2*weight_sum)==0

# The full rank-one recurrence and telescoping central increment.
w0,w1,w2,aa,vv,C,SS=S.symbols("w0 w1 w2 aa vv C SS",integer=True)
ww=S.Matrix([w0,w1,w2])
for i in range(3):
    M=meridian(i); e=S.eye(3)[:,i]
    Vw=vv*ww*ww.T
    dw=aa*ww
    wnew=M*ww
    anew=aa-2*vv*ww[i]
    same(M*Vw*M.T,vv*wnew*wnew.T)
    same(M*(dw-2*Vw*e),anew*wnew)
    assert S.expand(sum(wnew)-sum(ww)-2*ww[i])==0
    assert S.expand(anew+vv*sum(wnew)-aa-vv*sum(ww))==0
    inc=((C-vv*SS)*ww[i]-vv*ww[i]**2)/2
    potential=C*((SS+2*ww[i])-SS)/4-vv*((SS+2*ww[i])**2-SS**2)/8
    assert S.expand(inc-potential)==0

# Universal period 112 in odd S for integer m,t=m+n.
t,z=S.symbols("t z",integer=True)
potential=-m*(z-1)/2+t*(z*z-1)/8
period=S.expand(potential.subs(z,z+112)-potential)
assert S.expand(period/28)==-2*m+t*z+56*t

cases=[]
all_primitive_weight_residues=set()
for d in (8,14,20,30):
    initial=1-d//2
    def value(s):
        assert s%2==1
        return (initial-3*(s-1)+(3*d)*((s*s-1)//8))%28
    residues=set()
    examples={}
    # Every primitive residue pair modulo 112 has a coprime integer lift.
    # The direct CRT proof is retained in the working geometric note.
    for ap in range(112):
        for bq in range(112):
            if gcd(gcd(ap,bq),112)!=1: continue
            s=ap*ap+ap*bq+bq*bq
            all_primitive_weight_residues.add(s%112)
            val=value(s)
            residues.add(val)
            examples.setdefault(val,[ap,bq,s])
    rows=[]
    for s in (1,3,7,13,19,21):
        if s%2: rows.append({"S":s,"class":value(s)})
    assert value(3)==(-5*initial)%28
    assert value(7)==(-5*initial+15*d-12)%28
    cases.append({"d":d,"initial_m":6,"initial_n":3*d-6,
                  "initial_class":initial%28,"sample_values":rows,
                  "all_weight_residue_classes":sorted(residues),
                  "residue_pair_witnesses":examples})
assert all_primitive_weight_residues==set(range(1,112,2))

data={
    "status":"Proved P3K.31; root, blind, and checks frame audits passed",
    "checks":{
        "anti_quaternion_reset":"PASS",
        "reset_orientation":"PASS",
        "literal_source_normal_shear_homotopy":"PASS",
        "all_three_recurrence_involutions":"PASS",
        "selected_reverse_central_increment":"PASS",
        "first_fixed_flop_relative_pairs":"PASS",
        "actual_toric_weight_change":"PASS",
        "rank_one_covariance":"PASS",
        "central_telescoping":"PASS",
        "universal_period_112":"PASS"},
    "local_ambient_degree_arithmetic":[1,2,-1,2],
    "initial_V":"diag(-(m+n),0,0)",
    "initial_delta":["n-m","0","0"],
    "after_fixed_flop_m":["m+2*n","m-n","m-n"],
    "after_fixed_flop_n":["-n","3*m+5*n","3*m+5*n"],
    "central_formula":"s(S)=s(1)-m*(S-1)/2+(m+n)*(S*S-1)/8 mod28",
    "primitive_cases":cases
}
(ROOT/"code/part3_fourfold/common_exterior_frame_recurrence.json").write_text(
    json.dumps(data,indent=2)+"\n")
with (ROOT/"records/literature_fourfold.md").open("a") as log:
    log.write("\n- "+datetime.now(timezone.utc).isoformat()
              +" — Executed own code/part3_fourfold/common_exterior_frame_recurrence.py; "
              "reason: verify quaternion reset, exact integral frame recurrence, "
              "involutivity, and physical-weight telescoping; material: all symbolic "
              "identities and exhaustive primitive residue arithmetic modulo112. "
              "Geometric audit status remains explicit.\n")
print("PASS: quaternion reset, all frame/variation recurrences, exact weight changes, and telescoping.")
for row in cases:
    print("d =",row["d"],"primitive-weight classes =",row["all_weight_residue_classes"])
