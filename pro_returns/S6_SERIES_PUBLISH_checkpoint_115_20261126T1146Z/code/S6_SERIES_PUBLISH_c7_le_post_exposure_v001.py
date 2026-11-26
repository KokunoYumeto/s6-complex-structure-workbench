#!/usr/bin/env python3
"""LE post-exposure auxiliary checks from the frozen new exact data."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
from itertools import product
import json
import sympy as S

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"agents/continuation7_iii_mixed_torsion/S6_SERIES_PUBLISH_III_02LE_fresh_data_v001.json"
assert sha256(DATA.read_bytes()).hexdigest()=="8816e5af8593ed9758496217fe14a553fc8e4a2ee48ea7069d27d990ac9f9bf0"
rows=json.loads(DATA.read_text())["patterns"]
x,y,j=S.symbols("x y j",integer=True)
v=S.Matrix([x,y])
semichecks=0
print("Post-exposure auxiliary UTC",datetime.now(timezone.utc).isoformat(),flush=True)
for row in rows:
    a,b,p,nu,kappa=[row[k] for k in ("a","b","p","nu","kappa")]
    C=S.Matrix(row["C"])
    K=S.Matrix(row["K"])
    r=-kappa
    rho=C[1,1]
    physical=(-a*rho*x*x-2*a*b*r*x*y+b*nu*y*y+a*x)/2
    support=((v.T*K*v)[0]-x)/2
    linear=(a*C[0,:]-S.Matrix([[1,0]]))/2
    assert all(z.q==1 for z in linear)
    assert S.expand(physical.subs({x:(C*v)[0],y:(C*v)[1]},simultaneous=True)+support-(linear*v)[0])==0
    assert S.expand(physical.subs({x:x+nu,y:y+a*r},simultaneous=True)-physical+a*x)==0
    assert S.expand(physical.subs({x:x-b*r,y:y+rho},simultaneous=True)-physical-b*y-(b*rho-a*b*r)/2)==0
    for rawT in row["Ts"]:
        T=S.Matrix(rawT)
        for values in product(range(2),repeat=4):
            lam=S.Matrix(values)
            out=T*lam
            q=lambda z:(int(z[0])*int(z[1])+int(z[0])+int(z[1]))%2
            assert q(lam)==q(out)
            semichecks+=1
    for node in row["nodes"]:
        n,kk,d0=node["nu"],node["kappa"],node["d0"]
        short=S.Matrix([n//d0,-a*kk//d0])
        alpha=d0
        beta=S.Rational(b*kk,short[0])
        assert beta.q==1 and alpha in (1,3)
        kval=S.Rational(a*short[0],alpha)
        assert kval.q==1
        phi=-kval*j*(j-alpha)/2
        rho_n=beta*short[1]
        rr=-kk
        assert S.expand(phi.subs(j,j+alpha)-phi+a*short[0]*j)==0
        assert S.expand(phi.subs(j,j+beta)-phi-b*short[1]*j-(b*rho_n-a*b*rr)/2)==0
    ep=next(node for node in row["nodes"] if node["site"]==row["fixed_sites"][str(p)][0])
    w=ep["Tate_w"]
    normalized=w*pow(nu,-1,p)%p
    Pz=(normalized*normalized-1)*pow(2,-1,p)%p
    assert Pz==row["P_p"]*pow(a*nu,-1,p)%p
    for n in range(2*p):
        two,odd=n%2,n%p
        assert (p*two+(1-p)*odd)%(2*p)==n
    for unit in range(1,p):
        lift=(p+(1-p)*unit)%(2*p)
        inverse=(p+(1-p)*pow(unit,-1,p))%(2*p)
        assert lift*inverse%(2*p)==1
    print("ROW",row["number"],row["OS"],row["profile"],(a,b),"zero",row["zero"],
          "C",C.tolist(),"linear_gauge",list(linear),"delta_short",row["delta_short"],
          "cusp_character_mod2",row["cube2"],"physical_w",w,"common_w_over_nu",normalized,
          "z_generator_a_nu",a*nu%p,"P_in_z_marking",Pz,"P_primitive",row["P_p"],
          "full_P_mu",row["P_full"],row["mu"],"model_map",row["model_map"],"model_inverse",row["model_inverse"],flush=True)
print("SEMICHARACTER_ALL_16_SITE_VECTORS",semichecks,flush=True)
print("PASS: exact support pullback, both physical period differences, rank-one differences, all generator and inverse maps.",flush=True)
print("No original historical certificate was used; no fresh whole-check credit.",flush=True)
