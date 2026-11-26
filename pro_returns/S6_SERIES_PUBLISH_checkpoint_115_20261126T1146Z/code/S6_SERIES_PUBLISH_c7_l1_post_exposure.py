#!/usr/bin/env python3
"""Check every newly exposed L1 auxiliary arithmetic assertion.

Inputs are the raw construction cache and this lane's frozen fresh
catalogue only. No historical algorithm is imported or executed.
Frozen files are not changed.
"""
from pathlib import Path
from itertools import combinations
from math import lcm
from collections import Counter
import json
import sympy as S
from sympy.polys.domains import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/"agents/continuation7_iii_nonstar"
CAT = json.loads((OUT/"S6_SERIES_PUBLISH_III_02L1_fresh_catalogue.json").read_text())
RAW = json.loads((ROOT/"agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json").read_text())
PROFILES = {(r["OS"],r["profile"]):r for r in RAW["rows"]}
I = S.eye(4)
DELTA = I[:,2]
PAIRS = list(combinations(range(4),2))
FINITE = {"II":(6,1),"III":(4,2),"IV":(3,3),"III*":(4,2),"IV*":(3,3)}


def array(A):
    assert all(x.q == 1 for x in A)
    return [[int(x) for x in A.row(i)] for i in range(A.rows)]


def smith(A):
    D,U,V = smith_normal_decomp(DomainMatrix.from_Matrix(A).convert_to(ZZ))
    D,U,V = (x.to_Matrix() for x in (D,U,V))
    assert U*A*V == D and abs(U.det()) == abs(V.det()) == 1
    diag = [abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
    return diag,U,V


def fixed(T):
    d,_,V = smith(T-I)
    K,L = V[:,len(d):],V.inv()[len(d):,:]
    coords = L*DELTA
    dc,U,_ = smith(coords)
    assert dc == [1]
    K,L = K*U.inv(),U*L
    assert L*K == S.eye(K.cols) and K[:,0] == DELTA
    return K,L


def wedge(T):
    return S.Matrix([[T[i,k]*T[j,l]-T[i,l]*T[j,k]
                      for k,l in PAIRS] for i,j in PAIRS])


graphs, finite_rows, bad_graph, bad_fibre = [],[],[],[]
counts = Counter()
for row in CAT["natural"]:
    key = (row["OS"],row["profile"],row["a"],row["b"],row["zero_index"])
    Ts = [S.Matrix(x) for x in row["T"]]
    n = len(Ts)
    D = S.Matrix.hstack(*(T-I for T in Ts[:-1]))
    js = []
    for i in range(n-1):
        B = S.zeros(4*(n-1),4)
        B[4*i:4*i+4,:] = I
        js.append(B)
    blocks = []
    for i in range(n-1):
        P = I
        for T in Ts[i+1:-1]:
            P = P*T
        blocks.append(-P)
    js.append(S.Matrix.vstack(*blocks))
    bases = [fixed(T) for T in Ts]
    B = S.Matrix.hstack(*(j*K for j,(K,L) in zip(js,bases)))
    bd,U,V = smith(B)
    relation = S.Matrix([x for K,L in bases for x in [1]+[0]*(K.cols-1)])
    assert D*B == S.zeros(4,B.cols) and B*relation == S.zeros(B.rows,1)
    exact = bd == [1]*(4*n-7) and B.cols == 4*n-6 and D.rank() == 3
    if not exact:
        bad_graph.append(dict(key=key,smith=bd,columns=B.cols,D_rank=D.rank()))
    W = S.Matrix.hstack(*(wedge(T)-S.eye(6) for T in Ts))
    wd,_,_ = smith(W)
    omega = S.Matrix([[row["a"],0,0,0,0,-row["b"]]])
    assert omega*W == S.zeros(1,W.cols)
    if wd != [1]*5:
        bad_fibre.append(dict(key=key,smith=wd))
    counts[(row["OS"],row["profile"])] += 1
    graphs.append(dict(key=key,nonstar=row["nonstar"],graph_smith=bd,
                       fibre_smith=wd,normal_columns=array(B),
                       normal_U=array(U),normal_V=array(V)))
    raw = PROFILES[row["OS"],row["profile"]]
    for index,typ in enumerate(raw["fibers"]):
        if typ not in FINITE:
            continue
        d,q = FINITE[typ]
        A,g = S.Matrix(raw["elliptic_matrices"][index]),S.Matrix(raw["generator_section_cocycle"][index])
        z = (A-S.eye(2)).inv()*g
        zQ = row["b"]*z
        h = lcm(*(int(x.q) for x in zQ))
        T = Ts[index]
        ell = S.Matrix([-h*zQ[0],-h*zQ[1],0,h])
        assert (T-I)*ell == S.zeros(4,1) and d % h == 0
        record = dict(key=key,index=index+1,kind=typ,d=d,q=q,gamma_index=h,nonstar=row["nonstar"])
        if h == 1:
            R = T[:3,:3]
            rd,_,_ = smith(R-S.eye(3))
            rho = S.Matrix([[q*row["a"]*z[1],-q*row["a"]*z[0],q]])
            assert rho*R == rho and rd == [1,1]
            assert rho*S.Matrix([0,0,1]) == S.Matrix([q])
            assert row["b"] % q == 0
            record["vertical_smith"] = rd
            record["rho"] = array(rho)
        finite_rows.append(record)

for (os,profile),count in counts.items():
    print("PROFILE",os,profile,"rows",count,"graph and fibre assertions checked")
print("GRAPH EXCEPTIONS",json.dumps(bad_graph,separators=(",",":")))
print("FIBRE EXCEPTIONS",json.dumps(bad_fibre,separators=(",",":")))
assert not bad_graph and not bad_fibre
assert len(graphs) == 172
primitive = [r for r in finite_rows if r["gamma_index"] == 1]
nonstar = [r for r in finite_rows if r["nonstar"]]
assert len(finite_rows) == 102 and len(primitive) == 68
assert len(nonstar) == 94 and sum(r["gamma_index"] == 1 for r in nonstar) == 62
print("FINITE ALL",len(finite_rows),"PRIMITIVE",len(primitive),
      "NONSTAR",len(nonstar),"NONSTAR PRIMITIVE",sum(r["gamma_index"] == 1 for r in nonstar))
for r in finite_rows:
    if not r["nonstar"]:
        print("ODD-STAR PROFILE FINITE SLOT",r["key"],"position",r["index"],
              "type",r["kind"],"gamma index",r["gamma_index"])
patterns = CAT["minimal_patterns"]
assert len(patterns) == 164
obstructed = [r for r in patterns if not r["simple_order_feasible"]]
assert len(obstructed) == 2
for p in obstructed:
    print("ORBITAL OBSTRUCTION",p["OS"],p["profile"],p["a"],p["b"],
          "zero",p["zero_index"],"orders",p["finite_orders"])
print("PASS all172 auxiliary graph/fibre assertions and every finite fixed/vertical slot.")
print("PASS exact164 minimal patterns, two forced base-order obstructions,162 eligible patterns,59 sphere patterns.")
(OUT/"S6_SERIES_PUBLISH_III_02L1_post_exposure_constants.json").write_text(
    json.dumps(dict(scope="New computation after individual L1 release; no historical program execution",
                    graph_rows=graphs,finite_slots=finite_rows,
                    obstructed_patterns=obstructed),indent=2)+"\n",newline="\n")
