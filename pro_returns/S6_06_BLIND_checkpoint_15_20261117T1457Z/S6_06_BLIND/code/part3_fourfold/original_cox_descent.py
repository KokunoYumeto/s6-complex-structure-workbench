#!/usr/bin/env python3
"""Exact original c-period cochain and its sixfold cusp comparison.

This is the integral calculation for the pending original-loop Cox descent.
It does not divide a homotopy-sphere class.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as S
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT=Path(__file__).resolve().parents[2]
I=S.eye(4); zero=S.zeros(4,1)
T1=S.Matrix([[1,0,-6,2],[0,-1,1,1],[0,-1,0,1],[0,0,0,1]])
T2=S.Matrix([[1,6,0,-3],[0,0,-1,1],[0,1,0,0],[0,0,0,1]])
A1=T1.inv().T; A2=T2.inv().T; A0=(A1*A2).inv()
N1=I+A1+A1**2; N2=I+A2+A2**2+A2**3
J=S.Matrix([[0,0],[0,0],[1,0],[0,1]])
e1,e2,e3,delta=[I[:,i] for i in range(4)]
d0=S.zeros(28,14)
d0[0:4,0:4]=A1-I; d0[4:8,0:4]=A2-I
d0[8:12,4:8]=A1-I; d0[12:16,8:12]=A2-I
for i in range(3): d0[16+4*i:20+4*i,0:4]=I
d0[16:20,4:8]=-I; d0[20:24,8:12]=-I; d0[24:28,12:14]=-J
d1=S.zeros(20,28)
d1[0:4,8:12]=N1; d1[4:8,12:16]=N2
d1[8:12,0:4]=I; d1[8:12,8:12]=-I
d1[12:16,4:8]=I; d1[12:16,12:16]=-I
d1[16:20,0:4]=-A0; d1[16:20,4:8]=-A0*A1
for i,A in enumerate((A1,A2,A0)):
    d1[8+4*i:12+4*i,16+4*i:20+4*i]=-(A-I)
assert d1*d0==S.zeros(20,14)
def stack(parts): return S.Matrix.vstack(*parts)
def serial(M): return [[int(x) for x in M.row(i)] for i in range(M.rows)]
def ints(M): return [int(x) for x in M]
def preimage(A,b):
    D,U,V=[x.to_Matrix() for x in smith_normal_decomp(
        DomainMatrix.from_Matrix(A).convert_to(S.ZZ))]
    ub=U*b; y=S.zeros(A.cols,1); rank=A.rank()
    for i in range(rank):
        assert ub[i]%D[i,i]==0
        y[i]=ub[i]/D[i,i]
    assert all(x==0 for x in ub[rank:,:])
    x=V*y
    assert A*x==b and all(z.is_integer for z in x)
    return x

assert N1*e2==2*delta and N2*e2==2*delta
target=stack([2*delta,-2*delta,zero,zero,zero])
original=stack([A1*e2,-e2,e2,-e2,e2,zero,zero])
assert d1*original==target
assert original[24:28,:]==zero
assert original[0:4,:]+A1*original[4:8,:]==zero

# General integer preimages may always be put in the cusp-annulus-zero gauge.
def cusp_zero_preimage(b):
    x=preimage(d1,b)
    w=x[24:28,:]
    gauge=S.zeros(14,1); gauge[:4,:]=-w
    x=x+d0*gauge
    assert d1*x==b and x[24:28,:]==zero
    return x
target1=stack([2*delta,zero,zero,zero,zero])
target2=stack([zero,2*delta,zero,zero,zero])
x1=cusp_zero_preimage(target1); x2=cusp_zero_preimage(target2)

# Actual sixfold cover uses the logarithmic coefficients (4,-3) in the
# default positive-gamma sphere marking n0=1,n1=-1.
assert (A0-I)*e1==-delta
cover=stack([4*delta,-3*delta,4*delta,-3*delta,zero,zero,e1])
assert d1*cover==6*target
difference=cover-6*original
gauge=preimage(d0,difference)
assert d0*gauge==difference
data={
    "status":"Integral descent calculation; simultaneous smooth endpoint proof in progress",
    "A1":serial(A1),"A2":serial(A2),"A0":serial(A0),
    "cusp_nilpotent":serial(A0-I),
    "basis":["e1 (gamma)","e2","e3","delta"],
    "cochain_blocks":["p","q","r","s","u","v","w"],
    "d0":serial(d0),"d1":serial(d1),
    "default_positive_marking":{"n0":1,"n1":-1,"4n0+3n1":1},
    "c_to_c_minus_2_target":ints(target),
    "one_period_integer_primitive":{
        name:ints(original[4*i:4*i+4,:])
        for i,name in enumerate(("p","q","r","s","u","v","w"))},
    "one_period_cusp_annulus":ints(original[24:28,:]),
    "generic_two_delta1_primitive":ints(x1),
    "generic_two_delta2_primitive":ints(x2),
    "sixfold_logarithmic_primitive":{
        name:ints(cover[4*i:4*i+4,:])
        for i,name in enumerate(("p","q","r","s","u","v","w"))},
    "cover_minus_six_original_gauge":{
        "ordinary":ints(gauge[:4,:]),"finite0":ints(gauge[4:8,:]),
        "finite1":ints(gauge[8:12,:]),"cusp_invariant_coordinates":ints(gauge[12:14,:])},
    "checks":["d1d0=0","d1 original=target","cusp annulus zero",
              "p+A1q=0","(A0-I)e1=-delta","d1 cover=6 target",
              "cover-6 original=d0 gauge"]
}
(ROOT/"code/part3_fourfold/original_cox_descent.json").write_text(
    json.dumps(data,indent=2)+"\n")
with (ROOT/"records/literature_fourfold.md").open("a") as log:
    log.write("\n- "+datetime.now(timezone.utc).isoformat()
              +" — Executed own code/part3_fourfold/original_cox_descent.py; "
              "reason: compare the actual c-period and sixfold logarithmic cusp cochains "
              "without dividing a return class; material: full exact matrices, "
              "cusp-zero integral primitive and explicit integral gauge comparison.\n")
print("A0 =",A0)
print("one-period primitive =",data["one_period_integer_primitive"])
print("sixfold primitive =",data["sixfold_logarithmic_primitive"])
print("cover minus six original gauge =",data["cover_minus_six_original_gauge"])
print("PASS:",", ".join(data["checks"]))
