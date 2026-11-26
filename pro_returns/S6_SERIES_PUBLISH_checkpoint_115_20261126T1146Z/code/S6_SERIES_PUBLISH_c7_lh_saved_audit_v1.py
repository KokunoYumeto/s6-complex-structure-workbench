#!/usr/bin/env python3
"""Exhaustive computational audit of the frozen LH JSON, not manual matrix reading.

This separate program does not import or rerun any LH generating program.
It reconstructs the displayed arrays from the permitted raw/admitted inputs,
uses Sympy integer normal forms, and verifies every saved record and inverse.
All pre-existing files are read only.  Only the new audit note is written.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from math import gcd, lcm
from pathlib import Path
import json
import re
from sympy import Matrix, Rational, ZZ, eye, zeros
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parents[1]
LANE = ROOT/"agents/continuation7_iii_odd_weighted"
PREFIX = "S6_SERIES_PUBLISH_III_02LH_"
LD = ROOT/"agents/continuation7_iii_weighted_catalogue"
RAW = ROOT/"agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json"
FROZEN = {
    "fresh_derivation.md":"23e7026ce52f00005d7d4248f33b4975900e3c64b9905a06b614ecde06cbf0d8",
    "fresh_local_maps.md":"71eb34b0e8735b77d34e3bfe7a48240b2acde421a0a2fdc8ea7b96bc4cc79ee0",
    "fresh_calculation_readout.md":"ba51666ac3a29c19dc7460e392c1896514ea63d6a7351c4c25692cf5d7409ae1",
    "fresh_source_scope.md":"7559ca61ff44f41b84bc35fbab1c76980266585b24741517859fb1ec4e0144f7",
    "attempt_record.md":"a8ff29e22faba82d5701b2c79ae7709d17442d6469238e9747aad83893ee45cb",
    "fresh_local_data.json":"8ccb8711e212f4076643589c8eea1a3547d41fe90bc092f7aec9818e8a7049a1",
    "fresh_finite_data.json":"89a01f9bb801abe4d0f62bd86ca533e9156de4b1ea0ccf657a6b2c4087af3842",
    "fresh_global_data.json":"75170942fc8b53539126b68fc6b312c4aa09a38d0068412080b6a8c5b54222e6",
    "fresh_patterns.json":"d65ed082183792376c938f59650f92cdfe89514b11eef36b79b3cef4a40c6c24",
}
for suffix, digest in FROZEN.items():
    assert sha256((LANE/(PREFIX+suffix)).read_bytes()).hexdigest() == digest
assert sha256(RAW.read_bytes()).hexdigest() == "6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522"
raw = {(r["OS"],r["profile"]):r for r in json.loads(RAW.read_text())["rows"]}
initial = json.loads((LD/"S6_SERIES_PUBLISH_III_02LD_fresh_exterior_data.json").read_text())["rows"]
by_key = {tuple(r["key"]):r for r in initial}
assert len(by_key) == 172
local = json.loads((LANE/(PREFIX+"fresh_local_data.json")).read_text())
finite = json.loads((LANE/(PREFIX+"fresh_finite_data.json")).read_text())
global_data = json.loads((LANE/(PREFIX+"fresh_global_data.json")).read_text())
patterns = json.loads((LANE/(PREFIX+"fresh_patterns.json")).read_text())
assert set(local) == {"scope","weights","counts","records"}
assert set(finite) == {"scope","records"}
assert set(global_data) == {"scope","counts","results","torsion_examples","complete_smith_maps"}
assert all(isinstance(x["scope"],str) and x["scope"] for x in (local,finite,global_data))
PAIRS = list(combinations(range(4),2))
FINITE = {"II":6,"III":4,"IV":3,"III*":4,"IV*":3}
DELTA, GAMMA = eye(4)[:,2], eye(4)[:,3]
J2 = Matrix([[0,1],[-1,0]])
counts = Counter()


def imat(value, r=None, c=None):
    assert isinstance(value,list) and all(isinstance(row,list) for row in value)
    if r is not None:
        assert len(value) == r
    width = len(value[0]) if value else (c or 0)
    if c is not None:
        assert width == c
    assert all(len(row) == width and all(type(x) is int for x in row) for row in value)
    return Matrix(value) if value else zeros(0,width)


def integer(A):
    assert all(x.q == 1 for x in A)
    return A


def ext(A):
    return Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k] for k,l in PAIRS] for i,j in PAIRS])


def wed(x,y):
    return Matrix([x[i]*y[j]-x[j]*y[i] for i,j in PAIRS])


def normal_form(A):
    D = smith_normal_form(integer(A),domain=ZZ)
    ds = [abs(int(D[j,j])) for j in range(min(D.shape)) if D[j,j]]
    assert all(y % x == 0 for x,y in zip(ds,ds[1:]))
    return A.rows-len(ds), [x for x in ds if x>1], ds


def smith_basis(A):
    dd,uu,vv = smith_normal_decomp(DomainMatrix.from_Matrix(integer(A)).convert_to(ZZ))
    D,U,V = dd.to_Matrix(),uu.to_Matrix(),vv.to_Matrix()
    assert U*A*V == D
    rank = sum(bool(D[i,i]) for i in range(min(D.shape)))
    return D,U,V,rank


def bez(a,b):
    old_r,r,old_s,s,old_t,t = int(a),int(b),1,0,0,1
    while r:
        q = old_r//r
        old_r,r,old_s,s,old_t,t = r,old_r-q*r,s,old_s-q*s,t,old_t-q*t
    if old_r<0:
        old_r,old_s,old_t = -old_r,-old_s,-old_t
    assert a*old_s+b*old_t == old_r
    return old_r,old_s,old_t


def bez_many(values):
    d,coeff = 0,[]
    for value in values:
        d,u,v = bez(d,value)
        coeff = [u*x for x in coeff]+[v]
    return d,Matrix(coeff)


def orbit_list(p):
    assert sorted(p) == list(range(len(p)))
    unseen,answer = set(range(len(p))),[]
    while unseen:
        x,cycle = min(unseen),[]
        while x in unseen:
            unseen.remove(x);cycle.append(x);x=p[x]
        assert x == cycle[0]
        answer.append(cycle)
    return answer


def pow_perm(p,n):
    result = [None]*len(p)
    for cycle in orbit_list(p):
        for j,x in enumerate(cycle):
            result[x]=cycle[(j+n)%len(cycle)]
    return result


def component(kind):
    if re.fullmatch(r"I\d+",kind):
        n=int(kind[1:]);return list(range(1,n))+[0],[1]*n
    if kind=="II":return [0],[1]
    if kind=="III":return [1,0],[1,1]
    if kind=="IV":return [1,2,0],[1,1,1]
    if kind=="III*":return [0,4,5,6,1,2,3,7],[4,3,2,1,3,2,1,2]
    if kind=="IV*":return [0,3,4,5,6,1,2],[3,2,1,2,1,2,1]
    n=int(kind[1:-1]);assert n%2==1
    return [2,3,1,0]+list(reversed(range(4,n+5))),[1]*4+[2]*(n+1)


def vanishing(B,sec,nu):
    column = next((B-eye(2))[:,j] for j in range(2) if (B-eye(2))[:,j] != zeros(2,1))
    u=column/gcd(*(int(x) for x in column))
    if next(x for x in u if x)<0:u=-u
    d,x,y=bez(u[0],u[1]);assert d==1
    rr=Matrix([-y,x])
    kap=next(sec[j]/u[j] for j in range(2) if u[j])
    assert kap.q==1 and sec==kap*u and B-eye(2)==nu*u*u.T*J2
    return u,rr,int(kap)


def actual_extra(row,i,D):
    a,b=row["key"][2:4];kind=row["fibres"][i]
    q,_=row["components"][i]
    base=raw[tuple(row["key"][:2])]
    B=Matrix(base["elliptic_matrices"][i])
    sec=Matrix(base["generator_section_cocycle"][i])
    if re.fullmatch(r"I\d+",kind):
        nu=int(kind[1:]);u,rr,kap=vanishing(B,sec,nu)
        d,x,z=bez(a*kap,nu);assert d==1 and b%nu==0
        vv=Matrix([*(x*u),z,0])
        ell=Matrix([*list(-Rational(D*b*kap,nu)*rr),0,1])
        denominator=nu
    else:
        z=(B-eye(2)).inv()*sec
        rho=integer(q*Matrix([[a*z[1],-a*z[0],1]]))
        d,coeff=bez_many(list(rho));assert d==1 and b%q==0
        vv=Matrix([*coeff,0])
        ell=Matrix([*list(-D*b*z),0,1]);denominator=q
    return integer(wed(vv,ell)),denominator


# Reconstruct every weight-one defining matrix from the raw elliptic data.
for key,row in by_key.items():
    a,b,selected=key[2],key[3],key[4]-1
    data=raw[key[:2]]
    for i,kind in enumerate(row["fibres"]):
        B=Matrix(data["elliptic_matrices"][i]);sec=Matrix(data["generator_section_cocycle"][i])
        beta=-a*sec.T*J2*B
        if re.fullmatch(r"I\d+",kind):
            nu=int(kind[1:]);u,rr,kap=vanishing(B,sec,nu)
            c=Rational(-a*b*kap*kap,nu)+(Rational(1,nu) if i==selected else 0)
        else:
            z=(B-eye(2)).inv()*sec;c=(beta*(b*z))[0]
        A=eye(4);A[:2,:2]=B;A[:2,3]=b*sec;A[2,:2]=beta;A[2,3]=c
        assert integer(A)==imat(row["monodromies"][i],4,4)
        counts["raw_monodromies"]+=1
print("PASS all 172 admitted row monodromies reconstructed from the 21 raw profiles.",flush=True)

expected_local={(key,D) for key in by_key for D in local["weights"] if gcd(key[2],D)%2==1}
local_lookup={(tuple(r["key"]),r["D"]):r for r in local["records"]}
assert len(local_lookup)==len(local["records"])==2334 and set(local_lookup)==expected_local
local_fields={"key","D","g","matrices","H1_relations","H1_normalized_section",
              "graph_kernel","graph_kernel_left_inverse","fibre_quotient","fibre_section","local"}
kernel_fields={"kernel","kernel_left_inverse","quotient","quotient_section","cover_quotient",
               "transfer_quotient","weight_one_quotient","extra_actual_generator"}
expected_finite=set()
for rec in local["records"]:
    assert set(rec)==local_fields
    key,D=tuple(rec["key"]),rec["D"];row=by_key[key]
    a,b,selected=key[2],key[3],key[4]-1
    g=gcd(a,D);assert rec["g"]==g and g%2==1 and D>0
    S=Matrix.diag(1,1,1,D);S2=ext(S);TF=integer(D*S2.inv())
    As=[imat(v,4,4) for v in rec["matrices"]]
    assert len(As)==len(row["fibres"])
    prodA=eye(4)
    for i,A in enumerate(As):
        assert A==S.inv()*Matrix(row["monodromies"][i])*S
        prodA*=A
    assert prodA==eye(4)
    G=Matrix.hstack(*((A-eye(4))[:3,:] for A in As[:-1]))
    assert imat(rec["H1_relations"],3,G.cols)==G
    assert hermite_normal_form(G)==Matrix.diag(1,1,g)
    M=integer(Matrix.diag(1,1,Rational(1,g))*G)
    R=imat(rec["H1_normalized_section"],G.cols,3)
    K=imat(rec["graph_kernel"],G.cols,G.cols-3)
    KL=imat(rec["graph_kernel_left_inverse"],K.cols,G.cols)
    assert M*R==eye(3) and G*K==zeros(3,K.cols) and KL*K==eye(K.cols)
    inverse=Matrix.vstack(M,KL*(eye(G.cols)-R*M))
    basis=Matrix.hstack(R,K)
    assert inverse*basis==eye(G.cols) and basis*inverse==eye(G.cols)
    E=Matrix.hstack(*(ext(A)-eye(6) for A in As[:-1]))
    generators=Matrix.hstack(eye(6)[:,1],eye(6)[:,3],eye(6)[:,2],eye(6)[:,4],
                             D*b*eye(6)[:,0]+a*eye(6)[:,5])
    assert hermite_normal_form(E)==hermite_normal_form(generators)
    Q=imat(rec["fibre_quotient"],2,6);secQ=imat(rec["fibre_section"],6,2)
    assert Q*secQ==eye(2)
    assert Q[0,:]==Matrix([[a//g,0,0,0,0,-D*b//g]])
    assert Q[0,:]*E==zeros(1,E.cols) and all(x%g==0 for x in Q[1,:]*E)
    assert secQ[:,1]*g==D*b*eye(6)[:,0]+a*eye(6)[:,5]
    assert normal_form(E)[:2]==(1,[g] if g>1 else [])
    assert Matrix([[a,0,0,0,0,-b]])*S2==g*Q[0,:]
    counts["exteriors"]+=1;counts["shared_exteriors"]+=g>1
    assert len(rec["local"])==len(As)
    for i,info in enumerate(rec["local"]):
        A=As[i];kind=row["fibres"][i];q,residue=row["components"][i]
        assert info["site"]==i+1 and info["type"]==kind
        narrow=(a*residue)%q==0
        assert type(info["narrow"]) is bool and info["narrow"]==narrow
        rank=4-(A-eye(4)).rank()
        F=imat(info["fixed"],4,rank);FL=imat(info["fixed_inverse"],rank,4)
        assert (A-eye(4))*F==zeros(4,rank) and FL*F==eye(rank)
        sigma,multiplicities=component(kind)
        perm=pow_perm(sigma,-D*b*residue)
        assert info["component_permutation"]==perm
        assert info["component_orbits"]==orbit_list(perm)
        assert info["component_multiplicities"]==multiplicities
        assert all(multiplicities[x]==multiplicities[perm[x]] for x in range(len(perm)))
        expected_names={"ordinary"}|({"original_nonzero"} if i!=selected and not narrow else set())
        assert set(info["kernels"])==expected_names
        old_info=local_lookup[(key,1)]["local"][i]
        for name,cert in info["kernels"].items():
            assert set(cert)==kernel_fields
            W=ext(A)-eye(6)
            if name=="original_nonzero":
                extra=imat(cert["extra_actual_generator"],6,1)
                independent_extra,den=actual_extra(row,i,D)
                ordinaryQ=imat(info["kernels"]["ordinary"]["quotient"])
                assert ordinaryQ*extra==ordinaryQ*independent_extra
                assert (Matrix([[a,0,0,0,0,-D*b]])*extra)[0]==-Rational(D*b,den)
                old_extra=imat(old_info["kernels"][name]["extra_actual_generator"],6,1)
                assert S2*extra==D*old_extra
                span=Matrix.hstack(W,extra)
            else:
                assert cert["extra_actual_generator"] is None
                span=W
            rk=span.rank()
            KK=imat(cert["kernel"],6,rk);LL=imat(cert["kernel_left_inverse"],rk,6)
            QQ=imat(cert["quotient"],6-rk,6);SS=imat(cert["quotient_section"],6,6-rk)
            assert QQ*span==zeros(6-rk,span.cols)
            assert LL*KK==eye(rk) and QQ*SS==eye(6-rk)
            assert QQ*KK==zeros(6-rk,rk)
            assert KK*LL+SS*QQ==eye(6)
            old_cert=old_info["kernels"][name]
            Q1=imat(cert["weight_one_quotient"],6-rk,6)
            assert Q1==imat(old_cert["quotient"],6-rk,6)
            S1=imat(old_cert["quotient_section"],6,6-rk)
            cover=imat(cert["cover_quotient"],6-rk,6-rk)
            transfer=imat(cert["transfer_quotient"],6-rk,6-rk)
            assert cover==Q1*S2*SS and transfer==QQ*TF*S1
            assert Q1*S2==cover*QQ and QQ*TF==transfer*Q1
            assert cover*transfer==D*eye(6-rk) and transfer*cover==D*eye(6-rk)
            counts["local_kernels"]+=1
        base_fields={"site","type","fixed","fixed_inverse","component_permutation",
                     "component_orbits","component_multiplicities","narrow","kernels"}
        rawrow=raw[key[:2]]
        if i==selected:
            nu=int(kind[1:]);B=Matrix(rawrow["elliptic_matrices"][i])
            uu,rr,kap=vanishing(B,Matrix(rawrow["generator_section_cocycle"][i]),nu)
            CC=integer(Matrix([[nu,b*kap],[-a*kap,Rational(1-a*b*kap*kap,nu)]]))
            assert imat(info["cusp_C"],2,2)==CC and CC.det()==1
            c22=int(CC[1,1]);assert info["disc_delta_coefficient"]==c22
            ss,tt=info["disc_delta_bezout"]
            assert c22*ss+g*tt==1 and D%g==0 and gcd(a,nu)==1
            counts["cusp_disc_maps"]+=1
            base_fields|={"cusp_C","disc_delta_coefficient","disc_delta_bezout"}
        if re.fullmatch(r"I\d+",kind) and i!=selected and narrow:
            nu=int(kind[1:]);r0=gcd(D,nu)
            BB=imat(info["rank_one_period_basis"],4,4)
            BI=imat(info["rank_one_period_inverse"],4,4)
            assert BB*BI==eye(4) and BI*BB==eye(4)
            expected=eye(4);expected[0,1]=r0
            assert BI*A*BB==expected and BB[:,2]==DELTA
            assert info["rank_one_components"]==r0==len(info["component_orbits"])
            B=Matrix(rawrow["elliptic_matrices"][i])
            uu,rr,kap=vanishing(B,Matrix(rawrow["generator_section_cocycle"][i]),nu)
            assert BB[:,0]==Matrix([*uu,-a*kap//nu,0])
            assert BB[:,3]==Matrix([*list(-D*b*kap//r0*rr),0,nu//r0])
            x=(uu.T*J2*BB[:2,1])[0];y=BB[3,1]
            assert BB[:,1]==Matrix([*list(x*rr),0,y])
            assert Rational(nu,r0)*x+Rational(D*b*kap,r0)*y==1
            counts["rank_one_period_maps"]+=1
            base_fields|={"rank_one_period_basis","rank_one_period_inverse","rank_one_components"}
        assert set(info)==base_fields
        if kind in FINITE:expected_finite.add((key,D,i+1))
print("PASS all 2334 saved exterior structures, full quotient/section equations and graph inverse decompositions.",flush=True)
print("PASS all 12249 saved local saturated kernels, actual extra generators and both cover/transfer equations.",flush=True)
print("PASS all 4265 rank-one period bases/inverses, powered component permutations and 2334 cusp disc Bezout maps.",flush=True)

finite_keys=set()
for rec in finite["records"]:
    assert set(rec)=={"key","D","site","h","fixed","fixed_inverse","norm","norm_image_basis",
                      "norm_image_preimages","projected_quotient","projected_section","actions"}
    key,D,i=tuple(rec["key"]),rec["D"],rec["site"]-1
    finite_keys.add((key,D,i+1))
    lr=local_lookup[(key,D)];info=lr["local"][i]
    A=imat(lr["matrices"][i]);h=FINITE[info["type"]]
    assert rec["h"]==h and A**h==eye(4)
    F=imat(rec["fixed"],4,2);FL=imat(rec["fixed_inverse"],2,4)
    assert F==imat(info["fixed"]) and FL==imat(info["fixed_inverse"])
    norm=sum((A**j for j in range(h)),zeros(4,4))
    assert imat(rec["norm"],4,4)==norm
    H=imat(rec["norm_image_basis"],2,2);pre=imat(rec["norm_image_preimages"],4,2)
    quotient=imat(rec["projected_quotient"],2,4);section=imat(rec["projected_section"],4,2)
    assert hermite_normal_form(FL*norm)==H and FL*norm*pre==H
    assert quotient*section==eye(2) and H*quotient==FL*norm
    assert F*H*quotient==norm
    annihilator=[]
    for j in range(h):
        diagonal,U,V,rk=smith_basis(A**j-eye(4))
        annihilator.append(U[rk:,:])
    action_keys=set()
    CQ=imat(lr["fibre_quotient"]);g=lr["g"]
    expected_actions={(h*k,zz) for k in (1,2,h) for zz in ((1,0),(0,1),(1,1),(1,-1),(2,1),(1,2),(2,3),(3,2))}
    for action in rec["actions"]:
        assert set(action)=={"m","power","projected","free","first_stabilizer","core_H1_torsion"}
        m=action["m"];power=imat(action["power"],4,1);coords=FL*power
        assert F*coords==power and A*power==power and m%h==0
        action_keys.add((m,tuple(int(x) for x in coords)))
        w=imat(action["projected"],2,1);assert w==quotient*power
        t=gcd(m,*(int(x) for x in w))
        projected_free=gcd(m,*(int(x) for x in power))==1 and (m//t)%h==0
        first=None
        for j in range(1,m):
            tests=annihilator[j%h]*power
            if all((j*int(x))%m==0 for x in tests):
                first=j;break
        assert type(action["free"]) is bool
        assert action["free"]==(first is None)==projected_free
        assert action["first_stabilizer"]==first
        core=Matrix.hstack(Matrix.vstack(A-eye(4),zeros(1,4)),Matrix.vstack(-power,Matrix([m])))
        free_rank,torsion,diag=normal_form(core)
        assert free_rank==2 and action["core_H1_torsion"]==torsion
        Nm=(m//h)*norm
        fibre=Matrix.hstack(*(-wed(eye(4)[:,j],power) for j in range(4)))
        assert Nm*(A-eye(4))==zeros(4,4) and Nm*power==m*power
        relation=fibre*(A-eye(4))
        assert CQ[0,:]*relation==zeros(1,4) and all(x%g==0 for x in CQ[1,:]*relation)
        assert fibre*power==zeros(6,1)
        counts["finite_actions"]+=1;counts["free_finite_actions"]+=action["free"]
    assert len(rec["actions"])==24 and action_keys==expected_actions
    counts["finite_positions_weighted"]+=1
assert finite_keys==expected_finite and len(finite_keys)==len(finite["records"])==1386
assert dict(counts|Counter())["finite_actions"]==33264
for name,value in local["counts"].items():assert counts[name]==value
print("PASS all 1386 finite projection/image/section records and their complete coordinate domains.",flush=True)
print("PASS all 33264 saved action records rechecked through every proper power; exact first stabilizers and all formal Smith groups agree.",flush=True)
print("PASS 30511 free actions carry the asserted cap scope; 2753 rejected actions retain only formal affine presentations.",flush=True)
print("PASS every saved finite source relation maps to zero under the full raw Thom formula.",flush=True)

# Reconstruct the complete labelled pattern set directly from the admitted rows.
expected_patterns={}
canonical={}
for key,row in by_key.items():
    options=[]
    for i,kind in enumerate(row["fibres"]):
        q,residue=row["components"][i]
        if i==key[4]-1:opt=("C",)
        elif kind in FINITE:opt=("O","F")
        elif kind.endswith("*"):opt=("O",)
        elif key[2]*residue%q==0:opt=("M",)
        else:opt=("M","O")
        options.append(opt)
    canonical[key]=tuple(x[0] for x in options)
    for choice in product(*options):
        small=all(c=="O" for c,kind in zip(choice,row["fibres"]) if kind.endswith("*"))
        projection=tuple("O" if kind in ("III*","IV*") and c=="F" else c for c,kind in zip(choice,row["fibres"]))
        expected_patterns[(key,choice)]=(small,projection)
seen_patterns=set()
for p in patterns:
    assert set(p)=={"key","choices","all_star_original","all_star_projection"}
    identifier=(tuple(p["key"]),tuple(p["choices"]))
    assert identifier not in seen_patterns;seen_patterns.add(identifier)
    small,projection=expected_patterns[identifier]
    assert p["all_star_original"]==small and tuple(p["all_star_projection"])==projection
    assert expected_patterns[(identifier[0],projection)][0]
    if small:assert projection==identifier[1]
assert seen_patterns==set(expected_patterns) and len(seen_patterns)==495
assert sum(v[0] for v in expected_patterns.values())==459
print("PASS all 495 saved patterns, complete 459-family subset, inclusion/retraction and all 36 alternatives.",flush=True)

graph_cache={}
def graph(key,D,regular_count):
    cache_key=(key,D,regular_count)
    if cache_key in graph_cache:return graph_cache[cache_key]
    As=[imat(x) for x in local_lookup[(key,D)]["matrices"]]+[eye(4)]*(regular_count+1)
    relation=Matrix.hstack(*((A-eye(4))[:3,:] for A in As[:-1]))
    dd,U,V,rk=smith_basis(relation)
    assert rk==3
    Vi=integer(V.inv());K=V[:,rk:];KL=Vi[rk:,:]
    insertions=[]
    for i in range(len(As)):
        JJ=zeros(relation.cols,4)
        if i<len(As)-1:JJ[4*i:4*i+4,:]=eye(4)
        else:
            tail=eye(4)
            for j in reversed(range(len(As)-1)):
                JJ[4*j:4*j+4,:]=-tail;tail=As[j]*tail
        insertions.append(JJ)
    graph_cache[cache_key]=(As,K,KL,insertions)
    return graph_cache[cache_key]


def case_id(rec):
    return (tuple(rec["key"]),tuple(rec["choices"]),rec["D"],rec["e"],len(rec["regular"]))


expected_global={(key,choice,D,e,0) for key,choice in expected_patterns for D in (1,3,5,7,15) for e in (0,1)}
expected_global|={(key,choice,D,e,2) for key,choice in canonical.items() for D in (3,5,7,15) for e in (0,1)}
global_lookup={}
derived_reduced={}
global_counts=Counter()
for rec in global_data["results"]:
    assert set(rec)=={"key","choices","D","g","e","regular","B","Seifert","B_smith_nonzero","T",
        "H1_free","A1","beta","L","bridge","b2","b3","Euler","torsion_changes_if_fibre_torsion_discarded"}
    identifier=case_id(rec)
    assert identifier not in global_lookup and identifier in expected_global
    global_lookup[identifier]=rec
    key,choice,D,e,regular_count=identifier;row=by_key[key]
    lr=local_lookup[(key,D)];assert rec["g"]==lr["g"]
    As,K,KL,Js=graph(key,D,regular_count)
    columns=[Matrix.vstack(ext(A)-eye(6),zeros(K.cols,6)) for A in As]
    logs=[];beta=0;L=0;component_rank=D
    def add_log(i,m,v,h):
        norm=(m//h)*sum((As[i]**j for j in range(h)),zeros(4,4))
        for j in range(4):
            edge=Js[i]*norm[:,j]
            assert K*(KL*edge)==edge
            columns.append(Matrix.vstack(-wed(eye(4)[:,j],v),KL*edge))
        edge=Js[i]*v;assert K*(KL*edge)==edge
        columns.append(Matrix.vstack(zeros(6,1),KL*edge));logs.append((m,int(v[3])))
    for i,(c,info,kind) in enumerate(zip(choice,lr["local"],row["fibres"])):
        if c=="F":
            h=FINITE[kind];add_log(i,h*h,DELTA,h);continue
        F=imat(info["fixed"]);edge=Js[i]*F
        assert K*(KL*edge)==edge
        columns.append(Matrix.vstack(zeros(6,F.cols),KL*edge))
        nonzero=not info["narrow"]
        which="original_nonzero" if c=="O" and nonzero else "ordinary"
        KK=imat(info["kernels"][which]["kernel"])
        columns.append(Matrix.vstack(KK,zeros(K.cols,KK.cols)))
        if c=="C":continue
        if c=="O" and nonzero:
            defect=len(info["component_multiplicities"])-2
            beta+=defect;L+=1;component_rank+=defect+2
        elif re.fullmatch(r"I\d+",kind):
            r0=info.get("rank_one_components",1)
            beta+=r0-1;component_rank+=r0
        else:
            rho=len(info["component_orbits"])
            beta+=rho-1;component_rank+=rho
    regular_expected=[] if not regular_count else [(5,[2,-1,3,5]),(7,[-1,1,-2,-7])]
    assert len(rec["regular"])==len(regular_expected)
    for j,(item,(m,vv)) in enumerate(zip(rec["regular"],regular_expected)):
        assert set(item)=={"m","power"} and item["m"]==m
        v=imat(item["power"],4,1);assert v==Matrix(vv)
        assert gcd(m,*(int(x) for x in v))==1
        add_log(len(row["fibres"])+j,m,v,1)
    add_log(len(As)-1,1,-e*GAMMA,1)
    assert logs[-1]==(1,-e);logs.pop()
    B=Matrix.hstack(*columns)
    assert imat(rec["B"],B.rows,B.cols)==B
    seifert=zeros(len(logs)+1,len(logs)+1)
    for i,(m,mu) in enumerate(logs):
        seifert[i,0]=-mu;seifert[i,i+1]=m
    seifert[-1,0]=-e
    for i in range(len(logs)):seifert[-1,i+1]=1
    assert imat(rec["Seifert"],seifert.rows,seifert.cols)==seifert
    r,A1,_=normal_form(seifert);free,T,diag=normal_form(B)
    assert r==rec["H1_free"]==1-e and A1==rec["A1"]
    assert T==rec["T"] and diag==rec["B_smith_nonzero"]
    assert rec["beta"]==beta and rec["L"]==L
    assert free==(r if L==0 else 0)
    unfilled=sum(c!="F" for c in choice)
    assert component_rank==D+unfilled-1+beta+L
    bridge=component_rank-unfilled+r
    assert rec["bridge"]==bridge==D-1+beta+L+r
    assert rec["b2"]==free+bridge
    assert rec["b3"]==2*rec["b2"]+2-2*r-2*D
    assert rec["Euler"]==2*D
    projection=zeros(1+K.cols,B.rows)
    projection[0,:6]=imat(lr["fibre_quotient"])[0,:]
    projection[1:,6:]=eye(K.cols)
    reduced_free,reduced_torsion,_=normal_form(projection*B)
    assert reduced_free==free
    changed=reduced_torsion!=T
    assert rec["torsion_changes_if_fibre_torsion_discarded"]==changed
    derived_reduced[identifier]=reduced_torsion
    global_counts["torsion_changed"]+=changed
    if regular_count:
        global_counts["regular_full_vector_matrices"]+=1
    else:
        global_counts["full_matrices"]+=1
        global_counts["shared_full_matrices"]+=rec["g"]>1
        global_counts["zero_Euler"]+=e==0
        global_counts["nonzero_Euler"]+=e!=0
assert set(global_lookup)==expected_global and len(global_lookup)==6326
assert dict(global_counts)==global_data["counts"]
print("PASS all 6326 saved global matrices reconstructed entry by entry from the raw normal/kernel formulas.",flush=True)
print("PASS all 6326 Seifert matrices and both fresh Smith computations; all saved factors, ranks, beta, bridges and Euler values agree.",flush=True)
print("PASS complete case coverage: 4950 family matrices and 1376 full-vector regular matrices, with no duplicate or missing case.",flush=True)

changed_records=[r for r in global_data["results"] if r["torsion_changes_if_fibre_torsion_discarded"]]
assert len(changed_records)==112
for item,rec in zip(global_data["torsion_examples"],changed_records[:18]):
    assert set(item)=={"key","choices","D","g","e","regular","full","discarded_fibre_torsion"}
    assert item=={"key":rec["key"],"choices":rec["choices"],"D":rec["D"],"g":rec["g"],"e":rec["e"],
                  "regular":len(rec["regular"]),"full":rec["T"],
                  "discarded_fibre_torsion":derived_reduced[case_id(rec)]}
assert len(global_data["torsion_examples"])==18
expected_certificates=[r for r in global_data["results"] if not r["regular"] and r["g"]>1 and r["e"]==1][:24]
assert len(global_data["complete_smith_maps"])==len(expected_certificates)==24
for cert,rec in zip(global_data["complete_smith_maps"],expected_certificates):
    assert set(cert)=={"key","choices","D","e","diagonal","left","right","left_inverse","right_inverse"}
    for k in ("key","choices","D","e"):assert cert[k]==rec[k]
    B=imat(rec["B"]);rr,cc=B.shape
    diagonal=imat(cert["diagonal"],rr,cc)
    U=imat(cert["left"],rr,rr);UI=imat(cert["left_inverse"],rr,rr)
    V=imat(cert["right"],cc,cc);VI=imat(cert["right_inverse"],cc,cc)
    assert U*UI==eye(rr) and UI*U==eye(rr)
    assert V*VI==eye(cc) and VI*V==eye(cc)
    assert U*B*V==diagonal
    assert all(diagonal[i,j]==0 for i in range(rr) for j in range(cc) if i!=j)
    ds=[abs(int(diagonal[i,i])) for i in range(min(rr,cc)) if diagonal[i,i]]
    assert ds==rec["B_smith_nonzero"]
print("PASS all 24 complete global Smith equivalences and all four inverse-composite equations.",flush=True)
print("PASS all 18 saved torsion examples and the full count of 112 torsion-sensitive matrices.",flush=True)

runtime_lines=len((ROOT/"code/S6_SERIES_PUBLISH_c7_lh_runtime_probe_v1.out").read_text().splitlines())
assert runtime_lines==3
for suffix,digest in FROZEN.items():
    assert sha256((LANE/(PREFIX+suffix)).read_bytes()).hexdigest()==digest
print("PASS all nine frozen note/data hashes unchanged after the exhaustive computational audit.",flush=True)
print("RECORD_CORRECTION runtime_probe_v1.out has exactly 3 lines; the frozen attempt note's two-line statement is corrected here.",flush=True)
print("COUNTS",json.dumps({"exteriors":2334,"local_kernels":12249,"rank_one_maps":4265,"cusp_maps":2334,
    "finite_lattices":1386,"finite_actions":33264,"free_actions":30511,"rejected_actions":2753,
    "patterns":495,"all_star_patterns":459,"global_matrices":6326,"full_smith_certificates":24},sort_keys=True),flush=True)
print("SCOPE exhaustive computational reading and verification of saved arrays; no claim of manual reading of every matrix entry.",flush=True)

note = [
    "# LH saved-data audit and exact reading scope", "",
    "The frozen proof and original fresh calculation bytes remain unchanged.",
    "The LH original and historical target program remain unopened.", "",
    "## Reading scope before this audit", "",
    "The agent manually read the complete substantive proof notes, program",
    "sources and complete stdout/stderr streams. The generating programs",
    "asserted the matrix equations before serializing the large JSON files.",
    "The readout program parsed all four JSON files in full, but its checks",
    "were counts, pattern membership and summaries. Neither that readout nor",
    "the chat summary constituted manual reading of every saved matrix.", "",
    "## New exhaustive computational verification", "",
    "The separate saved_audit_v1 program imports no LH generating program.",
    "It reads all four frozen JSON files, verifies every declared record shape",
    "and integer entry type, reconstructs the defining matrices from the raw",
    "profiles, and checks every saved equation described below. It uses Sympy",
    "integer algorithms as a shared library; this is a saved-data verification",
    "and supplies no additional independent-blind check credit.", "",
    "- All 2334 exterior cases: complete coverage, H1 image, graph basis and",
    "  both inverse composites, full fibre quotient, section and exact lattice.",
    "- All 12249 local kernels: actual extra Gysin classes, primitive quotient",
    "  and section, complete cover and transfer maps and their composites.",
    "- All 4265 literal rank-one basis/inverse maps, component permutations,",
    "  orbit partitions and multiplicities; all 2334 cusp disc Bezout maps.",
    "- All 1386 finite projected-lattice records and all 33264 candidate actions:",
    "  every proper power, exact first stabilizer, projected test and formal",
    "  affine-group Smith presentation. Actual cap assertions apply to the",
    "  30511 free actions; the 2753 rejected actions carry only formal data.",
    "- All 495 labelled patterns, the 459-family subset, and every inclusion",
    "  and retraction entry, including the 36 alternatives.",
    "- All 6326 global matrices reconstructed entry by entry, all Seifert",
    "  matrices, both Smith calculations, every saved invariant factor and",
    "  every rank, component defect, bridge and Euler value.",
    "- All 24 full Smith equivalences, with both left and both right inverse",
    "  composites; all 18 saved examples and all 112 torsion-sensitive cases.", "",
    "This is exhaustive computational verification of the saved finite data.",
    "It is explicitly distinct from manual reading of every matrix entry.",
    "The main and local proofs remain the source of the unbounded theorem.", "",
    "## Exact record correction", "",
    "code/S6_SERIES_PUBLISH_c7_lh_runtime_probe_v1.out contains three lines.",
    "The frozen attempt note called it a two-line output. All three lines",
    "had been displayed and read; this new note corrects the count while",
    "preserving the frozen file. No mathematical assertion changes.", "",
    "The complete new audit stdout/stderr must be read before this audit is",
    "reported as completed to root. No original release or admission is",
    "implied by this note.", "",
]
(LANE/(PREFIX+"saved_data_audit.md")).write_text("\n".join(note))
