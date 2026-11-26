#!/usr/bin/env python3
"""Separate LD pre-exposure supplement: projected primitivity of delta +/- ell."""
from collections import Counter
from math import gcd, lcm
from pathlib import Path
import json

from sympy import Matrix, Symbol, eye, zeros, simplify
from sympy.matrices.normalforms import hermite_normal_form

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/"agents/continuation7_iii_weighted_catalogue"
profiles={(p["OS"],p["profile"]):p for p in json.loads((ROOT/
    "agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json").read_text())["rows"]}
rows=json.loads((LANE/"S6_SERIES_PUBLISH_III_02LD_fresh_exterior_data.json").read_text())["rows"]
ORDERS={"II":6,"III":4,"IV":3,"III*":4,"IV*":3}
D=Symbol("D",integer=True)
delta=eye(4)[:,2]
results=[];counts=Counter()
print("OS PROFILE a b ZERO SITE TYPE h g w_plus w_minus GCDS")
for row in rows:
    os,profile,a,b,selected=row["key"]
    raw=profiles[os,profile]
    for i,kind in enumerate(row["fibres"]):
        if kind not in ORDERS:continue
        h=ORDERS[kind]
        B=Matrix(raw["elliptic_matrices"][i])
        graw=Matrix(raw["generator_section_cocycle"][i])
        z=(B-eye(2)).inv()*graw
        g=lcm(*(int((b*x).q) for x in z))
        A=Matrix(row["monodromies"][i])
        ell=Matrix([*list(-g*b*z),0,g])
        F=Matrix.hstack(delta,ell)
        assert A**h==eye(4) and (A-eye(4))*F==zeros(4,2)
        N=sum((A**j for j in range(h)),zeros(4,4))
        # The inverse coordinates of a fixed vector are delta and gamma/g.
        C=Matrix.vstack(N[2,:],N[3,:]/g)
        assert F*C==N
        assert all(x.q==1 for x in C)
        C=Matrix([[int(x) for x in line] for line in C.tolist()])
        H=hermite_normal_form(C)
        assert C.rows==2 and H.shape==(2,2)
        plus=h*H.inv()*Matrix([1,1])
        minus=h*H.inv()*Matrix([1,-1])
        assert all(x.q==1 for x in plus) and all(x.q==1 for x in minus)
        wp=[int(x) for x in plus];wm=[int(x) for x in minus]
        gp=gcd(*wp);gm=gcd(*wm)
        assert gp==gm==1
        # A polynomial identity proves the conjugacy for all D; its
        # integrality uses D == epsilon (mod g), as in the written proof.
        AD=A.copy();AD[:3,3]=D*A[:3,3]
        ellD=Matrix([*list(-g*D*b*z),0,g])
        assert all(g0 in (1,2,3,4) for g0 in [g]) and a%g==0
        for eps in (1,-1):
            HD=eye(4);HD[:2,3]=(1-eps*D)*b*z;HD[3,3]=eps
            inverse=eye(4);inverse[:2,3]=-eps*(1-eps*D)*b*z
            inverse[3,3]=eps
            assert simplify(HD*inverse)==eye(4)
            assert simplify(inverse*HD)==eye(4)
            assert simplify(AD*HD-HD*A)==zeros(4,4)
            assert HD*delta==delta
            assert simplify(HD*ell-eps*ellD)==zeros(4,1)
            assert HD.det()==eps
        q=raw["component_coordinates"][i]["moduli"]
        q=int(q[0]) if q else 1
        assert g in (1,q)
        counts[(q,g)]+=1
        print(os,profile,a,b,selected,i+1,kind,h,g,wp,wm,(gp,gm))
        results.append({"key":row["key"],"site":i+1,"type":kind,
                        "h":h,"g":g,"q":q,"norm_coordinates":C.tolist(),
                        "projected_basis":H.tolist(),
                        "w_plus":wp,"w_minus":wm})
assert len(results)==102
print("PASS all 102 weight-one projected plus and minus vectors have coordinate gcd one.")
print("PASS all 204 polynomial conjugacy and inverse identities; delta fixed and ell sent to epsilon ell_D.")
print("COUNTS",sorted((q,g,n) for (q,g),n in counts.items()))
print("SCOPE new pre-exposure LD supplement; frozen LD files and target original were not changed or opened.")
# Sympy integers are serialized explicitly.
(LANE/"S6_SERIES_PUBLISH_III_02LD_primitive_examples_data.json").write_text(
    json.dumps({"scope":"Separate raw-derived LD example-primitivity supplement",
                "records":results},indent=2,default=int)+"\n")
