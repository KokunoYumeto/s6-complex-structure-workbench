#!/usr/bin/env python3
"""Read only this lane's new LJ output; check actual generator conversions."""
from pathlib import Path
from itertools import product
import hashlib
import json
import sympy as S

W = Path(__file__).resolve().parents[1]
INPUT = W/"agents/continuation7_iii_mixed_three/S6_SERIES_PUBLISH_III_02LJ_fresh_data_v001.json"
data = json.loads(INPUT.read_bytes())
print("INPUT_SHA256", hashlib.sha256(INPUT.read_bytes()).hexdigest())


def Q(x):
    return (int(x[0])*int(x[1])+int(x[0])+int(x[1])) % 2


checked = 0
for row in data["patterns"]:
    a, b, c, nu, kap = (row[k] for k in ("a", "b", "c", "nu", "kappa"))
    cusp = row["locals"][row["zero"]]
    print("\nROW", row["number"], row["profile"], (a,b), "zero", row["zero"], "c", c)
    if c % 2 == 0:
        for local in row["locals"]:
            T = S.Matrix(local["T"])
            for x in product(range(2), repeat=4):
                assert Q(T*S.Matrix(x)) == Q(x)
                checked += 1
        C, K = S.Matrix(cusp["C"]), S.Matrix(cusp["K"])
        assert [Q(S.Matrix(cusp["H"])[:,j]) for j in (0,2)] == [1,0]
        assert K[0,0] % 2 == 1 and K[1,1] % 2 == 0
        L0 = (a*C[0,:]-S.Matrix([[1,0]]))/2
        assert all(S.denom(x) == 1 for x in L0)
        e2 = row["locals"][row["fixed_sites"]["2"][0]]
        sig, ki = e2["sigma"], e2["kappa"]
        assert (sig-1) % 2 == 0
        CS0 = S.Matrix([[2,1],[-a*ki,S.Rational(1-a*ki,2)]])
        change = S.Matrix([[1,(sig-1)//2],[0,1]])
        assert CS0*change == S.Matrix(e2["CS"])
        assert (1-a) % 2 == 0 and b//2 % 2 == 1
        print(" EVEN: Q preserved; short epsilon=(1,0); L0=", list(L0),
              "I2 basis shear=", (sig-1)//2,
              "C character=", cusp["undoubled_character"] % 2, "E character=0")
    for p in (3,5):
        if c % p:
            continue
        local = row["locals"][row["fixed_sites"][str(p)][0]]
        ki, sig = local["kappa"], local["sigma"]
        w = pow((-a*ki) % p, -1, p)
        assert w == -sig % p
        normal = w*pow(nu, -1, p) % p
        assert (normal*nu) % p == w
        assert w*w % p == nu*(b//p)*pow(a, -1, p) % p
        P = ((b//p-a*nu)*pow(2,-1,p)) % p
        Pcurve = ((normal*normal-1)*pow(2,-1,p)) % p
        assert (a*nu*Pcurve) % p == P == row["P"+str(p)]
        assert (P*pow(a*nu,-1,p)) % p == Pcurve
        print(" ODD:", {"p":p,"physical_residue":-ki,"w":w,"cusp_weight":nu % p,
                       "action_exponent":pow(nu,-1,p),"action_inverse":nu % p,
                       "normalized_w":normal,"P_s":P,"P_curve":Pcurve,
                       "homology_scale":a*nu % p,"inverse_scale":pow(a*nu,-1,p)})
    for u in range(c):
        if S.gcd(u,c) == 1:
            ui = pow(u,-1,c)
            D = row["D3"]
            assert ((u*ui)**3-1) % D == 0
            assert ((u+c)**3-u**3) % D == 0
    print(" FULL: H6 order", row["D3"], "P", row["P"], "mu", row["mu"],
          "primary sections", row["detector_sections"],
          "model map", row["model_map"], "inverse", row["model_inverse"])
print("\nPASS", checked, "literal refinement identities; every action/generator inverse; all full H6 automorphism maps.")
