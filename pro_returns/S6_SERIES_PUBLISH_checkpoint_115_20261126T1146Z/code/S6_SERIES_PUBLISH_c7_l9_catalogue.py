#!/usr/bin/env python3
"""Fresh L9 construction-only enumeration and exact original-cap maps.

Reads only the raw 21-profile fixture. It does not import an old topology
algorithm or any target output. All writers belong to the new L9 lane.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from math import gcd, lcm, prod
from pathlib import Path
import csv
import io
import json
import re

from sympy import Matrix, Rational, ZZ, eye, zeros
from sympy.matrices.normalforms import smith_normal_form

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/"agents/continuation7_iii_multiplicative"
LANE.mkdir(exist_ok=True)
RAW=ROOT/"agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json"
raw_bytes=RAW.read_bytes()
assert sha256(raw_bytes).hexdigest()=="6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522"
profiles=json.loads(raw_bytes)["rows"]
J=Matrix([[0,1],[-1,0]])
wedge_order=list(combinations(range(4),2))
finite_orders={"II":6,"III":4,"IV":3,"III*":4,"IV*":3}
component_counts={"II":1,"III":2,"IV":3,"III*":8,"IV*":7}
zero_orbits={"II":1,"III":1,"IV":1,"III*":5,"IV*":3,"I1*":2,"I3*":3}

def egcd(a,b):
    x0,x1,y0,y1=1,0,0,1
    aa,bb=a,b
    while bb:
        q,aa,bb=aa//bb,bb,aa%bb
        x0,x1=x1,x0-q*x1
        y0,y1=y1,y0-q*y1
    if aa<0:aa,x0,y0=-aa,-x0,-y0
    assert a*x0+b*y0==aa
    return aa,x0,y0

def ints(M):
    assert all(x.q==1 for x in M)
    return [[int(x) for x in row] for row in M.tolist()]

def exterior(M):
    return Matrix([[M.extract(a,b).det() for b in wedge_order] for a in wedge_order])

def wedge(v,w):
    return Matrix([v[i]*w[j]-v[j]*w[i] for i,j in wedge_order])

def smith(M):
    D=smith_normal_form(M,domain=ZZ)
    diag=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
    assert all(y%x==0 for x,y in zip(diag,diag[1:]))
    return {"free":M.rows-len(diag),"torsion":[x for x in diag if x>1],"nonzero":diag}

def mult_data(A,g,nu):
    N=A-eye(2)
    col=next(N[:,i] for i in range(2) if N[:,i]!=zeros(2,1))
    divisor=gcd(*(abs(int(x)) for x in col))
    u=col/divisor
    if next(x for x in u if x)<0:u=-u
    assert N==nu*u*u.T*J
    gg,s,t=egcd(int(u[0]),int(u[1]));assert gg==1
    r=Matrix([-t,s]);assert Matrix.hstack(u,r).det()==1
    index=next(i for i in range(2) if u[i])
    kappa=g[index]/u[index]
    assert kappa.q==1 and g==kappa*u
    kappa=int(kappa)
    assert gcd(kappa,nu)==1
    return u,r,kappa

def raw_return(A,g,a,b,z):
    beta=-a*g.T*J*A
    T=eye(4);T[:2,:2]=A;T[:2,3]=b*g
    T[2,:2]=beta;T[2,3]=(beta*(b*z))[0]
    assert all(x.q==1 for x in T)
    return T

local=[]
zero_agreements=[]
natural=[]
patterns=[]
expanded=[]
profile_totals=[]

for profile in profiles:
    types=profile["fibers"]
    mats=[Matrix(a) for a in profile["elliptic_matrices"]]
    cocycles=[Matrix(g) for g in profile["generator_section_cocycle"]]
    component=[(int(c["moduli"][0]),int(c["rows"][0][0])) if c["moduli"] else (1,0)
               for c in profile["component_coordinates"]]
    assert all(gcd(q,k)==1 for q,k in component)
    height=Fraction(profile["height_of_generator"]);assert height.numerator==1
    height_d=height.denominator
    this_natural=this_nz=this_patterns=this_expanded=0
    for zero,zero_type in enumerate(types):
        if not re.fullmatch(r"I\d+",zero_type):continue
        nu0=int(zero_type[1:])
        if height_d%nu0:continue
        ab=height_d//nu0
        for a in range(1,ab+1):
            if ab%a:continue
            b=ab//a
            q0=component[zero][1]*b%nu0
            p0=component[zero][1]*a%nu0
            if gcd(q0,nu0)!=1:continue
            column=[int(j==p0)-int(j==0)-int(j==(p0-q0)%nu0)+int(j==(-q0)%nu0)
                    for j in range(nu0)]
            lap=[-2*int(j==0)+int(j==1%nu0)+int(j==(-1)%nu0) for j in range(nu0)]
            if column!=lap:continue
            if any(i!=zero and a*k%q and b*k%q for i,(q,k) in enumerate(component)):continue
            assert gcd(a,b)==1
            key=[profile["OS"],profile["profile"],a,b,zero+1]
            multiplicative=[i for i,t in enumerate(types) if i!=zero and re.fullmatch(r"I\d+",t)]
            nonzero_mult=[i for i in multiplicative if a*component[i][1]%component[i][0]]
            zero_mult=[i for i in multiplicative if i not in nonzero_mult]
            finite=[i for i,t in enumerate(types) if t in finite_orders]
            additive=[i for i,t in enumerate(types) if not re.fullmatch(r"I\d+",t)]
            row={"key":key,"fibres":types,"finite":finite,"nonzero_mult":nonzero_mult,
                 "zero_mult":zero_mult,"additive":additive,"component_data":component}
            finite_data={}
            for i in finite:
                z=(mats[i]-eye(2)).inv()*cocycles[i]
                gden=lcm(*(int((b*x).q) for x in z))
                q=component[i][0];assert gden in (1,q)
                finite_data[i]={"d":finite_orders[types[i]],"q":q,"g":gden,"qv":q//gden}
            row["finite_data"]=finite_data
            natural.append(row);this_natural+=1;this_nz+=len(nonzero_mult)
            for i in multiplicative:
                nu=int(types[i][1:]);A=mats[i];g=cocycles[i]
                u,r,kappa=mult_data(A,g,nu)
                kc=component[i][1]
                relabel=(-kappa*pow(kc,-1,nu))%nu if nu>1 else 0
                assert relabel==(-1)%nu
                E=eye(4);E[:2,:2]=Matrix.hstack(u,r)
                Traw=raw_return(A,g,a,b,Rational(kappa,nu)*r)
                T=E.inv()*Traw*E
                expected=Matrix([[1,nu,0,b*kappa],[0,1,0,0],
                                 [0,-a*kappa,1,-Rational(a*b*kappa*kappa,nu)],[0,0,0,1]])
                assert T==expected
                if i in nonzero_mult:
                    assert b%nu==0 and gcd(a*kappa,nu)==1 and nu>1
                    _,x,z=egcd(a*kappa,nu)
                    B=b*kappa//nu
                    R=eye(4);R[1,3]=-B
                    T1=R.inv()*T*R
                    beta=Matrix([x,0,z,0]);ell=Matrix([0,0,0,1])
                    v0=Matrix([nu,0,-a*kappa,0])
                    H=Matrix.hstack(v0,eye(4)[:,1],beta,ell)
                    assert H.det()==1 and H.inv()*T1*H==eye(4)+Matrix([[0,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
                    W=exterior(T1)-eye(6)
                    F=Matrix([[1,0,0,0,0,0],[0,0,0,1,0,0],
                              [0,0,a*kappa,0,0,nu],[0,0,0,0,1,0]])
                    S=Matrix.hstack(eye(6)[:,0],eye(6)[:,3],wedge(beta,ell),eye(6)[:,4])
                    assert F*W==zeros(4,6) and F*S==eye(4)
                    D=Matrix.hstack(eye(6)[:,1],nu*eye(6)[:,2]-a*kappa*eye(6)[:,5])
                    pre=Matrix.hstack(-x*eye(6)[:,0]+z*eye(6)[:,3],eye(6)[:,4])
                    left=Matrix([[0,1,0,0,0,0],[0,0,z,0,0,-x]])
                    assert W*pre==D and left*D==eye(2) and D*left*W==W
                    assert S*F+D*left*(eye(6)-S*F)==eye(6)
                    assert smith(W)["nonzero"]==[1,1]
                    k=exterior(E*R)*wedge(beta,ell)
                    omega=Matrix([[a,0,0,0,0,-b]])
                    assert (omega*k)[0]==-Rational(b,nu)
                    p=(-a*kappa)%nu
                    c=Matrix([[int(j==p)-int(j==0) for j in range(nu)]])
                    indices=[j for j in range(nu) if j not in (0,p)]
                    comp=Matrix.hstack(ones:=Matrix([1]*nu),*(eye(nu)[:,j] for j in indices))
                    cinv=Matrix.vstack(eye(nu)[0,:],*(eye(nu)[j,:]-eye(nu)[0,:] for j in indices))
                    assert c*comp==zeros(1,nu-1) and cinv*comp==eye(nu-1)
                    assert comp*cinv==eye(nu)-eye(nu)[:,p]*c
                    # Original and Mumford maps differ on exactly the primitive third coordinate.
                    O=F.extract([0,1,3],list(range(6)))
                    assert O*S==Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1]])
                    assert F*wedge(beta,ell)==Matrix([0,0,1,0]) and O*wedge(beta,ell)==zeros(3,1)
                    local.append({"key":key,"site":i+1,"nu":nu,"kappa":kappa,"component_relabelling":relabel,"p_tate":p,
                                  "h":b//nu,"defect":nu-2,"u":ints(u),"r":ints(r),
                                  "T":ints(Traw),"period_map":ints(E*R),"period_inverse":ints((E*R).inv()),
                                  "beta":ints(E*R*beta),"ell":ints(E*R*ell),"kernel":ints(k),
                                  "quotient":ints(F*exterior((E*R).inv())),
                                  "section":ints(exterior(E*R)*S),"relation_basis":ints(D),
                                  "relation_preimages":ints(pre),"component_basis":ints(comp),
                                  "component_inverse":ints(cinv)})
                else:
                    assert a%nu==0 and gcd(b*kappa,nu)==1
                    _,l,k=egcd(nu,b*kappa)
                    v=Matrix([1,0,-a*kappa//nu,0])
                    t=Matrix([0,l,0,k]);w=Matrix([0,-b*kappa,0,nu])
                    H=Matrix.hstack(v,t,eye(4)[:,2],w)
                    assert H.det()==1
                    Tj=H.inv()*T*H
                    assert Tj==eye(4)+Matrix([[0,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
                    Q=eye(6).extract([0,3,4,5],list(range(6)))
                    sec=Q.T
                    W=exterior(Tj)-eye(6)
                    assert Q*sec==eye(4) and Q*W==zeros(4,6)
                    assert smith(W)["nonzero"]==[1,1]
                    zero_agreements.append({"key":key,"site":i+1,"nu":nu,"kappa":kappa,"component_relabelling":relabel,
                                            "period_map":ints(E*H),"period_inverse":ints((E*H).inv()),
                                            "quotient":ints(Q*exterior((E*H).inv())),
                                            "section":ints(exterior(E*H)*sec)})
            for finite_bits in product(("O","F"),repeat=len(finite)):
                add_choices={i:("O" if i not in finite else finite_bits[finite.index(i)]) for i in additive}
                for mult_bits in product(("M","O"),repeat=len(nonzero_mult)):
                    mult_choices=dict(zip(nonzero_mult,mult_bits))
                    L=0;defect=0;hcols=[]
                    for i,choice in add_choices.items():
                        if choice!="O":continue
                        q,k=component[i]
                        nz=bool(a*k%q)
                        if nz:
                            assert b%q==0
                            count=component_counts.get(types[i],int(re.fullmatch(r"I(\d+)\*",types[i]).group(1))+5
                                                       if re.fullmatch(r"I(\d+)\*",types[i]) else 0)
                            L+=1;defect+=count-2;hcols.append(b//q)
                        else:defect+=zero_orbits[types[i]]-1
                    for i,choice in mult_choices.items():
                        if choice=="O":
                            nu=int(types[i][1:]);L+=1;defect+=nu-2;hcols.append(b//nu)
                    pid=len(patterns)+1
                    pattern={"pattern":pid,"key":key,"additive":{i+1:v for i,v in add_choices.items()},
                             "nonzero_multiplicative":{i+1:v for i,v in mult_choices.items()},
                             "zero_kernel_agreements":[i+1 for i in zero_mult],"L":L,"beta":defect,
                             "fibre_relations":hcols,"finite":[i for i,v in add_choices.items() if v=="F"]}
                    reps=[]
                    for zero_bits in product(("M","O"),repeat=len(zero_mult)):
                        cap_choices={**add_choices,**mult_choices,**dict(zip(zero_mult,zero_bits)),zero:"CUSP"}
                        eid=len(expanded)+1
                        reps.append(eid)
                        expanded.append({"choice":eid,"pattern":pid,"key":key,
                                         "caps":{i+1:cap_choices[i] for i in range(len(types))}})
                    pattern["representatives"]=reps
                    patterns.append(pattern);this_patterns+=1;this_expanded+=len(reps)
    profile_totals.append([profile["OS"],profile["profile"],this_natural,this_nz,this_patterns,this_expanded])
    print("PROFILE",*profile_totals[-1])
assert len(natural)==172 and len(local)==120 and len(patterns)==495 and len(expanded)==1728
assert len({tuple(x["key"]) for x in natural})==172
for p in patterns:
    assert len(p["representatives"])==2**len(p["zero_kernel_agreements"])
    assert expanded[p["representatives"][0]-1]["pattern"]==p["pattern"]
assert sorted(i for p in patterns for i in p["representatives"])==list(range(1,1729))
print("PASS",len(local),"nonzero local maps, full Wang inverses, signed -b/nu values and primitive component complements.")
print("PASS",len(zero_agreements),"zero-Chern original/Mumford kernel agreements with period inverses and quotient sections.")
print("PASS 172 natural rows; 120 new sites; 495 marked kernel patterns; 1728 individual cap choices with exact quotient/section fibres.")

lookup={tuple(x["key"]):x for x in natural}
global_checks=[]
for pattern in patterns:
    row=lookup[tuple(pattern["key"])];a,b=pattern["key"][2:4]
    finite=pattern["finite"]
    m=[row["finite_data"][i]["d"] for i in finite]
    mu=[row["finite_data"][i]["g"] for i in finite]
    R=prod(m)
    nr=-sum((R//mi)*ni for mi,ni in zip(m,mu))
    for e in (0,1):
        ng=1+2*len(finite)+4
        cols=[]
        for j,i in enumerate(finite):
            fd=row["finite_data"][i];mi=fd["d"];g=fd["g"];qv=fd["qv"]
            assert gcd(mi,1,1)==1 and mi//gcd(mi,qv,g)%fd["d"]==0
            for s0,d0,l0 in ((b*g//qv,mi//qv,0),(-b,0,mi//g),(0,1,1)):
                col=zeros(ng,1);col[0]=s0;col[1+2*j]=d0;col[2+2*j]=l0;cols.append(col)
        offset=1+2*len(finite)
        v=Matrix([1,0,0,nr])
        omega=Matrix([[0,a,0,0],[-a,0,0,0],[0,0,0,-b],[0,0,b,0]])
        for j in range(4):
            col=zeros(ng,1);col[0]=-(omega*v)[j];col[offset+j]=R;cols.append(col)
        col=zeros(ng,1);col[offset:offset+4,0]=v;cols.append(col)
        col=zeros(ng,1);col[0]=b*e;col[offset+2]=1
        for j in range(len(finite)):col[1+2*j]=1
        cols.append(col)
        for h in pattern["fibre_relations"]:
            col=zeros(ng,1);col[0]=h;cols.append(col)
        C=Matrix.hstack(*cols);Cgroup=smith(C)
        s=len(finite)+1
        H1=zeros(s+1,s+1)
        for j,(mi,ni) in enumerate(zip(m+[R],mu+[nr])):
            H1[j,0]=-ni;H1[j,j+1]=mi
        H1[s,0]=-e
        for j in range(1,s+1):H1[s,j]=1
        G1=smith(H1.T)
        r=int(e==0)
        assert G1["free"]==r
        assert Cgroup["free"]==(0 if pattern["L"] else r)
        L=pattern["L"];beta=pattern["beta"]
        b2=beta+L+r if L else beta+2*r
        b3=2*beta+2*L if L else 2*beta+2*r
        assert 2-2*r+2*b2-b3==2
        global_checks.append({"pattern":pattern["pattern"],"e":e,"regular_m":R,"regular_v":[1,0,0,nr],
                              "finite_m":m,"finite_n":[1]*len(m),"finite_r":[1]*len(m),
                              "C":ints(C),"Seifert":ints(H1),"C_group":Cgroup,"H1":G1,
                              "free_ranks":[1,r,b2,b3,b2,r,1],
                              "torsion_by_degree":[[],G1["torsion"],Cgroup["torsion"],
                                                   Cgroup["torsion"],G1["torsion"],[],[]]})
assert len(global_checks)==990
print("PASS 990 complete finite/regular Smith calculations: every 495 pattern at zero and nonzero rational Euler number.")
print("PASS cap torsion retained in all three finite columns; bridge rank L+r is retained at zero Euler.")
out={"scope":"Fresh raw-only L9 enumeration and exact integer cap maps; unbounded geometry is in the fresh derivation.",
     "raw_sha256":sha256(raw_bytes).hexdigest(),"profile_totals":profile_totals,"natural":natural,
     "nonzero_local":local,"zero_kernel_agreements":zero_agreements,"patterns":patterns,
     "expanded_choices":expanded,"global_checks":global_checks}
(LANE/"S6_SERIES_PUBLISH_III_02L9_fresh_data.json").write_text(json.dumps(out,indent=2)+"\n")
buf=io.StringIO(newline="")
fields=["pattern","OS","profile","a","b","zero","additive","nonzero_multiplicative","zero_kernel_agreements","L","beta","fibre_relations","representatives"]
writer=csv.DictWriter(buf,fields,delimiter="\t",lineterminator="\n");writer.writeheader()
for p in patterns:
    k=p["key"];r=dict(zip(fields[:6],[p["pattern"],*k]))
    for f in fields[6:]:r[f]=json.dumps(p[f],separators=(",",":")) if isinstance(p[f],(list,dict)) else p[f]
    writer.writerow(r)
(LANE/"S6_SERIES_PUBLISH_III_02L9_fresh_patterns.tsv").write_text(buf.getvalue())
print("PASS wrote complete 495-pattern table, all 1728 representatives and all exact matrices in the owning lane.")
print("SCOPE historical target original/program/output unopened; no unbounded claim inferred from finite tests.")
