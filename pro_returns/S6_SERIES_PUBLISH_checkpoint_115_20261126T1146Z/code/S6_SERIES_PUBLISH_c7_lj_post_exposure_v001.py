#!/usr/bin/env python3
"""New validation of every released historical LJ arithmetic assertion.

Reads only the frozen fresh LJ JSON and the exact retrieved historical
LJ output.  It does not execute the historical source or read its broad
input files.  Computed historical assignments are compared, not assumed.
"""
from pathlib import Path
from itertools import product
from datetime import datetime,timezone
from hashlib import sha256
from math import gcd
import json
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form

W=Path(__file__).resolve().parents[1]
fresh_path=W/"agents/continuation7_iii_mixed_three/S6_SERIES_PUBLISH_III_02LJ_fresh_data_v001.json"
old_path=Path("/tmp/S6_SERIES_PUBLISH_c7_LJ_historical/S6_SERIES_PUBLISH_manifolds_three_mixed_AH.json")
fresh=json.loads(fresh_path.read_bytes())["patterns"]
old=json.loads(old_path.read_bytes())
key=lambda r:(r["OS"],r["profile"],r["a"],r["b"],r["zero"])
oldkey=lambda r:(r["entry"],r["profile"],r["a"],r["b"],r["zero_index"])
newrows={}
for r in fresh:
    if key(r) in newrows:
        assert [x["T"] for x in r["locals"]]==[x["T"] for x in newrows[key(r)]["locals"]]
    newrows[key(r)]=r
oldrows={tuple(r["key"]):r for r in old["rows"]}
assert set(newrows)==set(oldrows) and len(newrows)==12 and len(fresh)==14
oldpatterns={(oldkey(r),tuple((i,"F" if c=="log" else "O") for i,c in r["additive_choices"])) for r in old["patterns"]}
newpatterns={(key(r),tuple((int(i),c) for i,c in r["options"].items())) for r in fresh}
assert oldpatterns==newpatterns
x,y,j=S.symbols("x y j",integer=True)
I4=S.eye(4); E3=I4[:,:3]; semis=0; adapted=0; finite=[]; changed=[]
print("START",datetime.now(timezone.utc).isoformat())
print("FRESH_SHA256",sha256(fresh_path.read_bytes()).hexdigest())
print("HISTORICAL_OUTPUT_SHA256",sha256(old_path.read_bytes()).hexdigest())
for K,r in sorted(newrows.items()):
    a,b,c=r["a"],r["b"],r["c"]
    oldr=oldrows[K]; Om=S.diag(a*S.Matrix([[0,1],[-1,0]]),S.Matrix([[0,-b],[b,0]]))
    primes=list(S.factorint(c)); angular=[]; images=[]; fixed={p:[] for p in primes}
    Q=lambda v:int(a*(v[0]+v[1]+v[0]*v[1]))%2
    print("\nROW",K,"c",c)
    for loc in r["locals"]:
        T=S.Matrix(loc["T"]); assert T.T*Om*T==Om
        images.append(T-I4)
        if c%2==0:
            assert a%2 and b%4==2
            for v in product((0,1),repeat=4):
                assert Q(T*S.Matrix(v))==Q(v); semis+=1
        if "nu" not in loc:
            continue
        i,n,kap=loc["site"],loc["nu"],loc["kappa"]; rr=-kap
        u,v=S.Matrix(loc["u"]),S.Matrix(loc["v"])
        B=S.Matrix.hstack(S.Matrix([*u,0,0]),S.Matrix([*v,0,0]),I4[:,2],I4[:,3])
        rho=T[2,3]; P=S.Matrix([[n,-b*rr],[a*rr,rho]])
        model=I4.copy();model[0,1]=n;model[2,1]=a*rr;model[0,3]=-b*rr;model[2,3]=rho
        assert B.det()==1 and B.inv()*T*B==model;adapted+=1
        H=S.Matrix(loc["H"])
        angular.append(H[:,[0,2]] if i==r["zero"] else H[:,0])
        if i==r["zero"]:
            assert P.det()==1
            psi=-a*rho*x*x-2*a*b*rr*x*y+b*n*y*y+a*x
            assert S.expand(psi.subs({x:x+n,y:y+a*rr},simultaneous=True)-psi)==-2*a*x
            assert S.expand(psi.subs({x:x-b*rr,y:y+rho},simultaneous=True)-psi)==2*b*y+b*rho-a*b*rr
            slopes=S.Poly(S.expand(psi.subs(y,y+1)-psi),x,y).coeffs()
            for p in primes:
                if p==2:
                    assert n%2 and rho%2 and b*n//2%2==1
                    assert all(S.denom((psi/2).subs({x:xx,y:yy}))==1 for xx,yy in product((0,1),repeat=2))
                else:
                    assert all(int(vv)%p==0 for vv in slopes)
                    assert a*(rho-b*rr)%p
            C=S.Matrix(loc["C"]); Kv=S.Matrix(loc["K"])
            X,Y=C*S.Matrix([x,y])
            pull=psi.subs({x:X,y:Y},simultaneous=True)
            assert S.expand(pull+(S.Matrix([[x,y]])*Kv*S.Matrix([x,y]))[0]-a*X)==0
            olddegree=-a*(rho-b*rr)
            actualdegree=a*(n-b*kap)
            print(" CUSP",{"nu":n,"kappa":kap,"rho":int(rho),
                          "physical_unit_wall_half_degree":int(olddegree),
                          "actual_prescribed_wall_half_degree":actualdegree,
                          "old_involution_character":1 if c%2==0 else None,
                          "actual_involution_character":r["t"] if c%2==0 else None,
                          "period_pullback":C.tolist(),"period_inverse":C.inv().tolist()})
        else:
            assert P.det()==0
            U=hermite_normal_form(P); assert U.shape==(2,1)
            u1,u2=map(int,U)
            if u1<0:u1,u2=-u1,-u2
            alpha=n//u1; beta=-b*rr//u1
            assert gcd(u1,u2)==1 and gcd(alpha,beta)==1 and a*u1%alpha==0
            assert P==S.Matrix([[alpha*u1,beta*u1],[alpha*u2,beta*u2]])
            psi=-S.Rational(a*u1,alpha)*j*(j-alpha)
            assert S.expand(psi.subs(j,j+alpha)-psi)==-2*a*u1*j
            assert S.expand(psi.subs(j,j+beta)-psi)==2*b*u2*j+b*rho-a*b*rr
            if c%2==0:
                assert alpha%2 or (a*u1//alpha)%2==0
                assert all(S.denom((psi/2).subs(j,jj))==1 for jj in range(4))
            for p in primes:
                if u1%p:continue
                assert n==p and alpha==1 and gcd(a*rr,p)==1
                assert S.expand(psi+a*p*j*(j-1))==0
                fixed[p].append(i)
                w=pow(a*rr,-1,p)
                if p!=2:
                    oldP=(w*w-1)*pow(2,-1,p)%p
                    correctP=(w*w*pow(r["nu"],-2,p)-1)*pow(2,-1,p)%p
                    assert oldP==oldr["primary"][str(p)]["refined_p"]
                    assert w==oldr["primary"][str(p)]["normal_weight"]
                    assert correctP*a*r["nu"]%p==r["P"+str(p)]
                    print(" ODD",{"p":p,"w":w,"nu":r["nu"],
                                  "old_curve_P":oldP,"correct_curve_P":correctP,
                                  "correct_fibre_P":r["P"+str(p)]})
    assert hermite_normal_form(S.Matrix.hstack(*angular))==E3
    assert hermite_normal_form(S.Matrix.hstack(*images))==E3
    assert all(len(vv)==1 for vv in fixed.values())
    assert {str(p):vv[0] for p,vv in fixed.items()}==oldr["fixed_elliptic_sites"]
    wrong2=(c%2==0 and oldr["primary"]["2"]["mod2_cube"]!=r["t"])
    wrong5=(c%5==0 and oldr["primary"]["5"]["refined_p_orbit"]!=int(r["P5"]!=0))
    if wrong2 or wrong5:changed.append(K)
    print(" GEOMETRIC_ARITHMETIC_PASS; changed_assignment",bool(wrong2 or wrong5))
for r in fresh:
    for loc in r["locals"]:
        if loc.get("option")=="F":
            assert loc["ell"][3][0]==1
            coeff=r["b"]//loc["q"]; assert coeff%r["c"]==0 and r["b"]%r["c"]==0
            finite.append({"key":list(key(r)),"site":loc["site"],"q":loc["q"],"fibre_coefficient":coeff})
assert semis==old["semicharacter_checks"]==464
assert adapted==old["adapted_matrix_checks"]==52
assert finite==old["finite_normal_checks"]
changed_patterns=[r["number"] for r in fresh if key(r) in changed]
assert changed_patterns==[1,2,5,6,7,10,14]
print("FINITE_NORMALS",finite)
print("COUNTS",{"patterns":len(fresh),"marked_rows":len(newrows),"semicharacters":semis,"adapted":adapted})
print("CHANGED_MARKED_KEYS",changed)
print("CHANGED_PATTERNS",changed_patterns)
print("COMPLETE",datetime.now(timezone.utc).isoformat())
print("PASS historical arithmetic assertions rechecked on frozen fresh data; assignment errors isolated; no historical execution.")
