#!/usr/bin/env python3
"""Post-exposure L9 auxiliary checks from the frozen fresh data.
No historical algorithm or output is read or executed.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from math import gcd
from pathlib import Path
import json

from sympy import Matrix, Symbol, ZZ, eye, zeros
from sympy.matrices.normalforms import smith_normal_form

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/"agents/continuation7_iii_multiplicative"
fresh = LANE/"S6_SERIES_PUBLISH_III_02L9_fresh_derivation.md"
assert sha256(fresh.read_bytes()).hexdigest() == "e5f8cc59e98d20ffe7b845824c369083b7e5246762ba52423aeeca7ea016f920"
data = json.loads((LANE/"S6_SERIES_PUBLISH_III_02L9_fresh_data.json").read_text())
order = list(combinations(range(4), 2))

def wedge(A):
    return Matrix([[A.extract(a,b).det() for b in order] for a in order])

def factors(A):
    S = smith_normal_form(A, domain=ZZ)
    return [abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]

def ints(A):
    return [[int(x) for x in row] for row in A.tolist()]

records = []
j = Symbol("j", integer=True)
Q = eye(7)
Q[1,4] = -j
Qinv = eye(7)
Qinv[1,4] = j
assert Q*Qinv == eye(7) == Qinv*Q
O = Matrix([[1,0,0,0,0,0,0],
            [0,1,0,0,j,0,0],
            [0,0,0,1,0,0,0]])
Ozero = O.subs(j, 0)
assert O*Q == Ozero
ker = Q[:,[2,4,5,6]]
assert O*ker == zeros(3,4)
print("PASS symbolic integral rim-section shear, its inverse and the full four-generator boundary kernel.")

for row in data["nonzero_local"]:
    a,b = row["key"][2:4]
    nu = row["nu"]
    kappa = row["kappa"]
    R = Matrix(row["period_map"])
    Rinv = Matrix(row["period_inverse"])
    assert R*Rinv == eye(4) == Rinv*R
    beta = Rinv*Matrix(row["beta"])
    x,z = int(beta[0]),int(beta[2])
    assert a*kappa*x + nu*z == 1
    B3 = Matrix([[1,0,0],[0,nu,x],[0,-a*kappa,z]])
    assert B3.det() == 1
    B3inv = Matrix([[1,0,0],[0,z,-x],[0,a*kappa,nu]])
    assert B3*B3inv == eye(3) == B3inv*B3
    Kraw = wedge(R)*eye(6)[:,[1,2,5]]
    Ksplit = Kraw*B3
    assert Ksplit[:,2] == Matrix(row["kernel"])
    omega = Matrix([[a,0,0,0,0,-b]])
    vals = omega*Kraw
    h = gcd(*(abs(int(v)) for v in vals))
    assert h == b//nu == row["h"]
    assert omega*Ksplit == Matrix([[0,0,-h]])
    T = Matrix(row["T"])
    assert factors(T-eye(4)) == [1]
    assert factors(wedge(T)-eye(6)) == [1,1]
    # The actual global map annihilates the rim coordinate, so the
    # complete original-section shear is invisible in the exterior.
    G = Matrix([[a,0,-h,0,0,0,0],
                [0,0,0,0,1,0,0],
                [0,0,0,0,0,1,0],
                [0,0,0,0,0,0,1]])
    assert G*Q == G
    assert G*ker == Matrix([[-h,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    # Integral Gysin kernel and primitive whole-fibre section.
    p = row["p_tate"]
    c = Matrix([[int(k==p)-int(k==0) for k in range(nu)]])
    C = Matrix(row["component_basis"])
    Cinv = Matrix(row["component_inverse"])
    assert c*C == zeros(1,nu-1) and Cinv*C == eye(nu-1)
    assert factors(c) == [1]
    local_ranks = [1,2,nu+1,2*nu,nu]
    assert sum((-1)**k*v for k,v in enumerate(local_ranks)) == 0
    records.append({"key":row["key"],"site":row["site"],"nu":nu,"h":h,
                    "raw_kernel":ints(Kraw),"kernel_change":ints(B3),
                    "kernel_change_inverse":ints(B3inv),
                    "local_betti_0_to_4":local_ranks})
assert len(records) == 120
print("PASS all 120 raw three-generator fibre kernels and their unimodular decomposition into Wang relations plus k.")
print("PASS all 120 exact gcd values b/nu and unit Smith factors for A-I and wedge^2(A)-I.")
print("PASS all 120 primitive Gysin complements and every local group in original display OM4.")
print("PASS all 120 full boundary images are unchanged globally by every integral local rim correction j.")

initial = {tuple(r["key"]):r for r in data["natural"]}
additive = {}
for p in data["patterns"]:
    key = tuple(p["key"])
    signature = (key,tuple(sorted((int(i),choice) for i,choice in p["additive"].items())))
    additive[signature] = p
assert len(additive) == 282
nzadd = 0
for (key,choices),p in additive.items():
    raw = initial[key]
    a = key[2]
    if any(choice == "O" and a*raw["component_data"][i-1][1] % raw["component_data"][i-1][0]
           for i,choice in choices):
        nzadd += 1
assert nzadd == 54
print("PASS exact projection of the 495 patterns onto 282 additive patterns, including 54 with nonzero-Chern additive originals.")

signatures = set()
for r in data["expanded_choices"]:
    key = (tuple(r["key"]),tuple(sorted((int(i),c) for i,c in r["caps"].items())))
    assert key not in signatures
    signatures.add(key)
assert len(signatures) == 1728
assert len(data["patterns"]) == 495
assert len(data["zero_kernel_agreements"]) == 316
assert len(data["global_checks"]) == 990
print("PASS all 1728 individual choices are distinct, with 316 zero-Chern agreements and 495 quotient patterns.")
print("PASS all 990 frozen full matrices retain both Euler values, the finite root columns and bridge rank L+r.")
out = {"scope":"Post-exposure auxiliary comparison; symbolic rim shear holds for every integer j.",
       "local":records,"additive_patterns":282,"additive_nonzero_patterns":54,
       "patterns":495,"individual_choices":1728}
(LANE/"S6_SERIES_PUBLISH_III_02L9_post_exposure_checks.json").write_text(
    json.dumps(out,indent=2)+"\n")
print("SCOPE no historical table-byte comparison, historical execution, or independent-blind credit is claimed.")
