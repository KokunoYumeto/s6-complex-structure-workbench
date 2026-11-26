#!/usr/bin/env python3
"""Fresh LD complete pattern enumeration and exact weighted global matrices.

Only the raw defining fixture and this lane's newly derived exterior data
are read. Historical target programs and target output are not inputs.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import gcd, lcm, prod
from pathlib import Path
import json
import re

from sympy import Matrix, Rational, eye, zeros, ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/"agents/continuation7_iii_weighted_catalogue"
RAW=ROOT/"agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json"
profiles={(r["OS"],r["profile"]):r for r in json.loads(RAW.read_text())["rows"]}
rows=json.loads((LANE/"S6_SERIES_PUBLISH_III_02LD_fresh_exterior_data.json").read_text())["rows"]
FINITE={"II":6,"III":4,"IV":3,"III*":4,"IV*":3}
WEIGHTS=(1,2,3,5,31)
J2=Matrix([[0,1],[-1,0]])

def egcd(a,b):
    aa,bb=a,b
    x,y,u,v=1,0,0,1
    while bb:
        q=aa//bb
        aa,bb=bb,aa-q*bb
        x,u=u,x-q*u
        y,v=v,y-q*v
    if aa<0:aa,x,y=-aa,-x,-y
    assert a*x+b*y==aa
    return aa,x,y

def ints(M):
    assert all(x.q==1 for x in M)
    return [[int(x) for x in row] for row in M.tolist()]

def imat(M):
    return Matrix(ints(M))

def smith(M):
    Z=smith_normal_form(imat(M),domain=ZZ)
    factors=[abs(int(Z[i,i])) for i in range(min(Z.shape)) if Z[i,i]]
    assert all(y%x==0 for x,y in zip(factors,factors[1:]))
    return M.rows-len(factors),[x for x in factors if x>1]

def perm_power(p,n):
    n%=lcm(*(len(o) for o in orbits(p)))
    out=list(range(len(p)))
    for _ in range(n):out=[p[x] for x in out]
    return out

def orbits(p):
    unseen=set(range(len(p)));ans=[]
    while unseen:
        start=min(unseen);cycle=[];x=start
        while x not in cycle:
            cycle.append(x);unseen.remove(x);x=p[x]
        assert x==start
        ans.append(cycle)
    return ans

def component_model(kind):
    if re.fullmatch(r"I\d+",kind):
        n=int(kind[1:])
        return list(range(1,n))+[0],[1]*n,0
    if kind=="II":return [0],[1],0
    if kind=="III":return [1,0],[1,1],0
    if kind=="IV":return [1,2,0],[1,1,1],0
    if kind=="III*":
        return [0,4,5,6,1,2,3,7],[4,3,2,1,3,2,1,2],3
    if kind=="IV*":
        return [0,3,4,5,6,1,2],[3,2,1,2,1,2,1],2
    match=re.fullmatch(r"I(\d+)\*",kind)
    assert match and int(match[1])%2==1
    n=int(match[1])
    p=[2,3,1,0]+list(reversed(range(4,n+5)))
    return p,[1]*4+[2]*(n+1),0

def vanishing(B,g,nu):
    col=next((B-eye(2))[:,j] for j in range(2) if (B-eye(2))[:,j]!=zeros(2,1))
    div=gcd(*(abs(int(x)) for x in col))
    u=col/div
    if next(x for x in u if x)<0:u=-u
    assert B-eye(2)==nu*u*u.T*J2
    _,x,y=egcd(int(u[0]),int(u[1]))
    r=Matrix([-y,x])
    kappa=next(g[j]/u[j] for j in range(2) if u[j])
    assert kappa.q==1 and gcd(int(kappa),nu)==1
    return u,r,int(kappa)

def local(row,data,D):
    a,b=row["key"][2:4];selected=row["key"][4]-1
    matrices=[];fixed=[];details=[]
    S=eye(4);S[3,3]=D
    for i,kind in enumerate(row["fibres"]):
        A=imat(S.inv()*Matrix(row["monodromies"][i])*S)
        matrices.append(A)
        q,kc=row["components"][i]
        Pnarrow=(a*kc)%q==0
        sigma,multiplicity,outer=component_model(kind)
        forward=perm_power(sigma,-D*b*kc)
        if not re.fullmatch(r"I\d+",kind) and Pnarrow:
            old=perm_power(sigma,-b*kc)
            assert {frozenset(o) for o in orbits(old)}=={frozenset(o) for o in orbits(forward)}
            E=pow(D,-1,q) if q>1 else 1
            assert perm_power(forward,E)==old
        info={"type":kind,"q":q,"narrow":Pnarrow,
              "component_permutation":forward,"components":len(multiplicity),
              "orbits":orbits(forward),"multiplicities":multiplicity}
        delta=eye(4)[:,2]
        if re.fullmatch(r"I\d+",kind):
            nu=int(kind[1:])
            B=Matrix(data["elliptic_matrices"][i])
            g=Matrix(data["generator_section_cocycle"][i])
            u,r,kappa=vanishing(B,g,nu)
            us=Matrix([*u,0,0])
            if i==selected:
                F=Matrix.hstack(us,delta)
            elif Pnarrow:
                assert a%nu==0 and gcd(D,nu)==1 and gcd(b*kappa,nu)==1
                ell=Matrix([*list(-D*b*kappa*r),0,nu])
                F=Matrix.hstack(us,delta,ell)
                assert len(orbits(forward))==gcd(D,nu)==1
            else:
                assert b%nu==0
                ell=Matrix([*list(-Rational(D*b*kappa,nu)*r),0,1])
                F=Matrix.hstack(us,delta,ell)
                assert gcd(a*kappa,nu)==1
                info["h"]=b//nu
            info["nu"]=nu
        else:
            B=Matrix(data["elliptic_matrices"][i])
            g=Matrix(data["generator_section_cocycle"][i])
            z=(B-eye(2)).inv()*g
            gden=lcm(*(int((b*x).q) for x in z))
            ell=Matrix([*list(-gden*D*b*z),0,gden])
            F=Matrix.hstack(delta,ell)
            info["g"]=gden
            if not Pnarrow:
                assert b%q==0
                info["h"]=b//q
            else:
                component_coeffs=[sum(multiplicity[j] for j in o) for o in orbits(forward)]
                assert all(c%q==0 for c in component_coeffs)
                W=[c//q for c in component_coeffs]
                assert gcd(*W)==1 and 1 in W
                info["primitive_fibre"]=W
        F=imat(F)
        assert (A-eye(4))*F==zeros(4,F.cols)
        assert F.cols==4-(A-eye(4)).rank()
        # The gcd of its maximal minors proves the displayed fixed basis
        # is saturated; its rational span is already the whole kernel.
        divis=0
        for inds in combinations(range(4),F.cols):
            divis=gcd(divis,abs(int(F.extract(inds,range(F.cols)).det())))
        assert divis==1
        fixed.append(F);details.append(info)
    aggregate=eye(4)
    for A in matrices:aggregate=aggregate*A
    assert aggregate==eye(4)
    return matrices,fixed,details

def pattern_choices(row):
    zero=row["key"][4]-1
    opts=[]
    for i,kind in enumerate(row["fibres"]):
        a=row["key"][2];q,k=row["components"][i]
        if i==zero:opts.append(["C"])
        elif kind in FINITE:opts.append(["O","F"])
        elif re.fullmatch(r"I\d+\*",kind):opts.append(["O"])
        elif (a*k)%q==0:opts.append(["M"])
        else:opts.append(["M","O"])
    return list(product(*opts))

def graph_coordinates(matrices,row,D):
    # Append the ordinary regular site and the order-one clutch site.
    mats=matrices+[eye(4),eye(4)]
    n=len(mats);width=4*(n-1)
    G=Matrix.hstack(*((A-eye(4))[:3,:] for A in mats[:-1]))
    R1=zeros(width,3);Ca=zeros(width,3)
    stored1=Matrix(row["exterior_one_preimages"])
    storeda=Matrix(row["exterior_a_preimages"])
    R1[:stored1.rows,:]=stored1;Ca[:storeda.rows,:]=storeda
    aa,alpha,beta=egcd(row["key"][2],D);assert aa==1
    LD=Matrix.diag(*[1 if i%4==3 else D for i in range(width)])
    R=alpha*Ca+beta*LD*R1
    assert G*R==eye(3)
    P=eye(width)-R*G
    K=hermite_normal_form(imat(P))
    assert K.cols==width-3 and G*K==zeros(3,K.cols)
    U=Matrix.hstack(R,K)
    assert abs(U.det())==1
    inv=U.inv()
    assert all(x.q==1 for x in inv)
    read=inv[3:,:]
    assert read*K==eye(K.cols)
    suffix=[eye(4) for _ in range(n)]
    for i in reversed(range(n-1)):suffix[i]=mats[i]*suffix[i+1]
    def insert(i,v):
        out=zeros(width,1)
        if i<n-1:out[4*i:4*i+4,0]=v
        else:
            for j in range(n-1):out[4*j:4*j+4,0]=-suffix[j+1]*v
        assert G*out==zeros(3,1)
        x=read*out
        assert K*x==out and all(c.q==1 for c in x)
        return x
    return K,insert

table=defaultdict(lambda:Counter())
patterns=[];extra=[];individual_total=0;weighted_cases=0
global_results=[];zero_euler_cases=0;nonzero_euler_cases=0
nonzero_mult=zero_mult=0
for row in rows:
    os,profile,a,b,selected=row["key"]
    data=profiles[os,profile]
    key=(os,profile)
    table[key]["rows"]+=1
    choices=pattern_choices(row)
    zero_count=sum(i+1!=selected and re.fullmatch(r"I\d+",kind) is not None
                   and a*row["components"][i][1]%row["components"][i][0]==0
                   for i,kind in enumerate(row["fibres"]))
    nz_count=sum(i+1!=selected and re.fullmatch(r"I\d+",kind) is not None
                 and a*row["components"][i][1]%row["components"][i][0]!=0
                 for i,kind in enumerate(row["fibres"]))
    nonzero_mult+=nz_count;zero_mult+=zero_count
    table[key]["nonzero_multiplicative"]+=nz_count
    table[key]["patterns"]+=len(choices)
    table[key]["individual_choices"]+=len(choices)*2**zero_count
    individual_total+=len(choices)*2**zero_count
    for choice in choices:
        narrow=all(not(kind.endswith("*") and c=="F") for kind,c in zip(row["fibres"],choice))
        record={"key":row["key"],"choices":choice,"all_star_original":narrow}
        patterns.append(record)
        table[key]["all_star_original"]+=int(narrow)
        if not narrow:
            projection=tuple("O" if k in ("III*","IV*") else c for k,c in zip(row["fibres"],choice))
            assert projection in choices
            assert all(not(k.endswith("*") and c=="F") for k,c in zip(row["fibres"],projection))
            record["all_star_projection"]=projection
            extra.append(record)
    for D in WEIGHTS:
        if gcd(a,D)!=1:continue
        mats,fixed,details=local(row,data,D)
        K,insert=graph_coordinates(mats,row,D)
        target_rank=1+K.cols
        omega=Matrix([[0,a,0,0],[-a,0,0,0],[0,0,0,-D*b],[0,0,D*b,0]])
        for choice in choices:
            finite_sites=[i for i,c in enumerate(choice) if c=="F"]
            orders={i:FINITE[row["fibres"][i]] for i in finite_sites}
            R=prod(orders.values())
            mu={i:details[i]["g"] for i in finite_sites}
            nreg=-sum((R//orders[i])*mu[i] for i in finite_sites)
            assert sum(Fraction(mu[i],orders[i]) for i in finite_sites)+Fraction(nreg,R)==0
            for e in (0,1):
                columns=[];beta=0;L=0;log_records=[]
                def add_vertical(value,site,vec):
                    columns.append(Matrix.vstack(Matrix([value]),insert(site,vec)))
                for i,c in enumerate(choice):
                    info=details[i];A=mats[i];F=fixed[i]
                    if c=="F":
                        m=orders[i];v=F*Matrix([1,1])
                        Nm=sum((A**j for j in range(m)),zeros(4,4))
                        assert gcd(m,*(int(x) for x in v))==1
                        for j in range(4):
                            lam=eye(4)[:,j]
                            add_vertical(-(lam.T*omega*v)[0],i,Nm*lam)
                        add_vertical(0,i,v)
                        log_records.append((m,int(v[3])))
                    else:
                        for j in range(F.cols):add_vertical(0,i,F[:,j])
                        if c=="O":
                            if not info["narrow"]:
                                L+=1
                                beta+=info["components"]-2
                                columns.append(Matrix.vstack(Matrix([D*info["h"]]),zeros(K.cols,1)))
                            elif "nu" not in info:
                                beta+=len(info["orbits"])-1
                            else:
                                beta+=gcd(D,info["nu"])-1
                # Complete regular block and complete order-one clutch block.
                reg=len(mats);dummy=reg+1
                for site,m,v in (
                    (reg,R,Matrix([1,0,0,nreg])),
                    (dummy,1,Matrix([0,0,0,-e]))):
                    assert gcd(m,*(int(x) for x in v))==1
                    for j in range(4):
                        lam=eye(4)[:,j]
                        add_vertical(-(lam.T*omega*v)[0],site,m*lam)
                    add_vertical(0,site,v)
                    log_records.append((m,int(v[3])))
                B=Matrix.hstack(*columns)
                assert B.rows==target_rank
                c_rank,T=smith(B)
                s=len(log_records)
                H1=zeros(s+1,s+1)
                for i,(m,mu0) in enumerate(log_records):
                    H1[i,0]=-mu0;H1[i,i+1]=m
                for i in range(s):H1[s,i+1]=1
                r,A1=smith(H1)
                assert r==(1 if e==0 else 0)
                assert c_rank==(r if L==0 else 0)
                b2=D-1+beta+L+r+c_rank
                b3=2-2*r+2*b2-2*D
                assert b3==(2*beta+2*r if L==0 else 2*beta+2*L)
                assert min(b2,b3)>=0
                groups={
                    "H0":{"free":1,"torsion":[]},"H1":{"free":r,"torsion":A1},
                    "H2":{"free":b2,"torsion":T},"H3":{"free":b3,"torsion":T},
                    "H4":{"free":b2,"torsion":A1},"H5":{"free":r,"torsion":[]},
                    "H6":{"free":1,"torsion":[]}}
                assert sum((-1)**j*groups["H"+str(j)]["free"] for j in range(7))==2*D
                global_results.append({"key":row["key"],"D":D,"choices":choice,"e":e,
                    "log_orders_numerators":log_records,"beta":beta,"L":L,
                    "presentation_free_rank":c_rank,"groups":groups,
                    "boundary_matrix":ints(B),"Seifert_matrix":ints(H1)})
                weighted_cases+=1
                zero_euler_cases+=int(e==0);nonzero_euler_cases+=int(e==1)
print("OS PROFILE ROWS NZ_MULT PATTERNS ALL_STAR_ORIGINAL INDIVIDUAL_CHOICES")
for key,counts in table.items():
    print(*key,counts["rows"],counts["nonzero_multiplicative"],counts["patterns"],
          counts["all_star_original"],counts["individual_choices"])
assert len(patterns)==495 and len(extra)==36
assert sum(p["all_star_original"] for p in patterns)==459
assert nonzero_mult==120 and zero_mult==316 and individual_total==1728
print("PASS complete patterns:",len(patterns),"all-star-original subset:",495-len(extra),
      "extra finite-star families:",len(extra))
print("PASS all actual zero-Chern component powers and inverse exponents at each tested weight.")
print("PASS nonzero multiplicative positions:",nonzero_mult,"zero-Chern positions:",zero_mult)
print("PASS individual original/Mumford representatives and exact projection:",individual_total)
print("PASS full weighted boundary matrices and both Smith groups:",weighted_cases)
print("PASS zero Euler:",zero_euler_cases,"nonzero Euler:",nonzero_euler_cases)
print("PASS all primitive graph bases, cut-loop insertions, cap fixed bases, and component sections.")
print("PASS every computed free rank and Euler characteristic 2D, with complete torsion retained.")
(LANE/"S6_SERIES_PUBLISH_III_02LD_fresh_patterns.json").write_text(json.dumps(
    {"scope":"New independent exact pattern sets, no historical target input.",
     "patterns":patterns,"extra_finite_star_families":extra,
     "profile_counts":[{"OS":k[0],"profile":k[1],**v} for k,v in table.items()]},indent=2)+"\n")
(LANE/"S6_SERIES_PUBLISH_III_02LD_fresh_global_data.json").write_text(json.dumps(
    {"scope":"Complete new matrices for stated sample parameters; universal proof is in the fresh derivation.",
     "weights":WEIGHTS,"cases":global_results},indent=2)+"\n")
print("SCOPE LD original and historical weighted programs/outputs remain unopened.")
