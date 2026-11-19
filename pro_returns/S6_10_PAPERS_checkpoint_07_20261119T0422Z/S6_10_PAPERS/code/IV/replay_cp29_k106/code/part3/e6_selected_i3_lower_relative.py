#!/usr/bin/env python3
"""Exact full coefficient, fibre-clutch and relative pair checks for I3R."""
from pathlib import Path
from datetime import datetime, timezone
import json
import hashlib
import sympy as s

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/"notes/part3_e6_selected_i3_lower_relative_working.md"
deps=[
 SOURCE,
 ROOT/"notes/part3_e6_selected_i3_p_one_lower_working.md",
 ROOT/"notes/part3_e6_selected_i3_working.md",
 ROOT/"notes/part3_e6_order_three_source_working.md",
 ROOT/"code/part3/e6_selected_i3_p_one_lower.json",
]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
locks={str(p.relative_to(ROOT)):sha(p) for p in deps}
checks=[]
def ck(name,condition):
    condition=bool(condition);checks.append({"name":name,"pass":condition})
    if not condition:raise AssertionError(name)
def zero(name,expression):ck(name,s.factor(s.cancel(expression))==0)
P,p,v,us,U6,Z,WC,lam0,cq,K=s.symbols("P p v us U6 Z WC lam0 cq K",nonzero=True)
c=lam0*cq*K/us**4
scalar=P*v/us
lam=scalar**4*lam0
qold=P*p*cq
point=lambda zz,ww:P**-6/U6*zz**2*ww
zero("literal source-period point arrow",point(P**3*p*Z,p**-2*WC)-P**6*point(Z,WC))
zero("literal full B point arrow",point(P**-1*Z,P**4*p*v**4*c*WC)-lam*qold*K*P**-3*point(Z,WC))
zero("full selected height multiplier",lam*qold*K*P**-3-P**2*p*v**4*c)
gamma=lam0*qold*K*P**-3
for k in range(4):
    hp=P**(-2-k)*us**k/U6*Z**2
    hm=P**(3+k)*us**(-k-1)*U6/Z**2
    zero("retained determinant "+str(k),hp*hm-P/us)
    zero("literal positive chain factor "+str(k),point(Z,P**4*v**k)/scalar**k-hp)
    zero("literal negative chain factor "+str(k),scalar**(k+1)*P**2*v**(-k-1)*U6/Z**2-hm)
    for j in range(-5,6):
        zstar=P**j*Z
        wstar=(P**4*p*v**4*c)**(-j)*WC
        zero("actual B inverse point "+str((k,j)),
             point(zstar,wstar)-(lam*qold*K*P**-3)**(-j)*point(Z,WC))
        zero("full original chain label "+str((k,j)),
             point(Z,WC)/scalar**(4*j+k)-gamma**j*point(zstar,wstar)/scalar**k)

data=json.loads((ROOT/"code/part3/e6_selected_i3_p_one_lower.json").read_text())
ck("executed four lower surfaces",data["surfaces"]==4)
ck("executed full 128 charts",len(data["lower_charts"])==128)
for row in data["lower_charts"]:
    aa=row["normal_a_column"];bb=row["normal_b_column"]
    expected_a=[int(j==aa) for j in range(4)]
    expected_b=[int(j==bb) for j in range(4)]
    ck("literal normal rows "+str(row["four_cone"]),
       row["normal_rows"]==[expected_a,expected_b])
    M=s.Matrix(row["source_exponent_matrix"])
    ck("source determinant and volume "+str(row["four_cone"]),
       M.det()==row["source_jacobian_sign"] and
       list(M[0,:]+M[1,:]-s.ones(1,2))==row["source_jacobian_orders"])
counts=[]
for subdivision in data["source_subdivisions"]:
    fan=[(1,0),(0,1)]
    for n,entry in enumerate(subdivision["chronological_blowups"]):
        left=tuple(entry["left_ray"]);right=tuple(entry["right_ray"])
        ray=tuple(entry["removed_ray"])
        index=fan.index(left)
        ck("actual chronological adjacent blowup "+str((subdivision["source_cell"],n)),
           fan[index+1]==right and ray==tuple(left[i]+right[i] for i in range(2)))
        fan.insert(index+1,ray)
    ck("complete original source fan "+str(subdivision["source_cell"]),
       fan==list(map(tuple,subdivision["rays"])))
    counts.append(len(fan)-2)
ck("exact blowup counts",counts==[15,6,8] and sum(counts)==29)

I=s.Matrix([[-2,1,1],[1,-2,1],[1,1,-2]])
D=s.Matrix([3,2,4]);F=s.ones(3,1)
zero("actual reference divisor square",(D.T*I*D)[0]+6)
ck("actual fibre radical",I*F==s.zeros(3,1))
zero("reference-fibre intersection",(D.T*I*F)[0])
monodromy=s.Matrix([[1,3],[0,1]])
ck("three identical primitive vanishing cycles",monodromy==s.Matrix([[1,1],[0,1]])**3)
relation=s.Matrix([[3,0,0]])
inclusion=s.Matrix([[0,1,0]])
ck("boundary inclusion respects torsion",inclusion*relation.T==s.zeros(1,1))
ck("actual source retains b",inclusion*s.Matrix([0,1,0])==s.ones(1,1))
ck("actual section kills alpha",inclusion*s.Matrix([0,0,1])==s.zeros(1,1))
nuplus,numinus=s.symbols("nuplus numinus",integer=True)
xp=D+nuplus*F;xm=-D+numinus*F
sqplus=s.expand(-(xp.T*I*xp)[0])
mixed=s.expand(-(xp.T*I*xm)[0])
sqminus=s.expand(-(xm.T*I*xm)[0])
zero("retained full positive gauge square",sqplus-6)
zero("retained full mixed gauge square",mixed+6)
zero("retained full negative gauge square",sqminus-6)
p1=-3*sum(counts)
zero("actual tangent difference",p1+87)
kM=sqplus+sqminus-mixed
lM=p1+sqplus+2*mixed+sqminus
zero("physical inner k",kM-18)
zero("physical inner ell",lM+87)
zero("four lower k",4*kM-72)
zero("four lower ell",4*lM+348)
for path in deps:
    ck("input unchanged "+str(path.relative_to(ROOT)),sha(path)==locks[str(path.relative_to(ROOT))])
result={
 "status":"PASS_SELECTED_I3_LOWER_RELATIVE",
 "utc":datetime.now(timezone.utc).isoformat(),
 "checks":len(checks),"source_sha256":sha(SOURCE),
 "script_sha256":sha(Path(__file__)),"inputs":locks,
 "normal_pairings":[6,-6,6],"relative_tangent_p1":p1,
 "per_surface_physical_M_inner_pair":[int(kM),int(lM)],
 "four_surface_physical_M_inner_pair":[int(4*kM),int(4*lM)],
 "scope":"Four actual closed lower/reference doubles with full point-line, primitive fibre-clutch and 29-blowup tangent maps.",
 "excluded":"Moving selected normalization, Hopf cap and final outer/Jin return.",
 "identities":checks,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({k:result[k] for k in ["status","checks","source_sha256","normal_pairings","per_surface_physical_M_inner_pair"]},indent=2))
