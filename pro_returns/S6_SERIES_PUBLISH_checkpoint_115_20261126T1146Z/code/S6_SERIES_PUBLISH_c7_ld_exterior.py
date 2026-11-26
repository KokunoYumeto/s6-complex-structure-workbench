#!/usr/bin/env python3
"""Fresh LD weighted defining matrices and primitive exterior maps.
Input is only the raw 21-profile construction fixture.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from math import gcd
from pathlib import Path
import json
import re

from sympy import Matrix, Rational, eye, zeros
from sympy.matrices.normalforms import hermite_normal_form

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/"agents/continuation7_iii_weighted_catalogue"
LANE.mkdir(exist_ok=True)
RAW=ROOT/"agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json"
raw_bytes=RAW.read_bytes()
assert sha256(raw_bytes).hexdigest()=="6bda97b01ba63c0a796e3141609ca12e163791b626024b79104817ec5defc522"
profiles=json.loads(raw_bytes)["rows"]
J=Matrix([[0,1],[-1,0]])
wedges=list(combinations(range(4),2))

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

def right_inverse(M):
    """Bezout of maximal minors, with all integer preimages retained."""
    n,m=M.shape
    assert n<=m
    terms=[]
    common=0
    for cols in combinations(range(m),n):
        block=M[:,list(cols)]
        det=int(block.det())
        if not det:continue
        new,x,y=egcd(common,det)
        terms=[(c,k*x) for c,k in terms]
        terms.append((cols,y))
        common=new
        if common==1:break
    R=zeros(m,n)
    for cols,coefficient in terms:
        adj=M[:,list(cols)].adjugate()
        for i,col in enumerate(cols):
            R[col,:]+=coefficient*adj[i,:]
    assert M*R==common*eye(n)
    return common,R

def ints(M):
    assert all(x.q==1 for x in M)
    return [[int(x) for x in row] for row in M.tolist()]

def exterior(M):
    return Matrix([[M.extract(rows,cols).det() for cols in wedges] for rows in wedges])

def vanishing(B,g,nu):
    col=next((B-eye(2))[:,j] for j in range(2) if (B-eye(2))[:,j]!=zeros(2,1))
    u=col/gcd(*(abs(int(x)) for x in col))
    if next(x for x in u if x)<0:u=-u
    assert B-eye(2)==nu*u*u.T*J
    _,x,y=egcd(int(u[0]),int(u[1]))
    r=Matrix([-y,x])
    k=next(g[j]/u[j] for j in range(2) if u[j])
    assert k.q==1 and g==k*u and gcd(int(k),nu)==1
    return u,r,int(k)

allrows=[]
profile_maps=[]
for profile in profiles:
    Bs=[Matrix(x) for x in profile["elliptic_matrices"]]
    gs=[Matrix(x) for x in profile["generator_section_cocycle"]]
    types=profile["fibers"]
    components=[(int(x["moduli"][0]),int(x["rows"][0][0])) if x["moduli"] else (1,0)
                for x in profile["component_coordinates"]]
    assert all(gcd(q,k)==1 for q,k in components)
    U2=Matrix.hstack(*(B-eye(2) for B in Bs[:-1]))
    U3=Matrix.hstack(*(Matrix.vstack(B-eye(2),-g.T*J*B) for B,g in zip(Bs[:-1],gs[:-1])))
    index2,R2=right_inverse(U2)
    index3,R3=right_inverse(U3)
    print("PROFILE",profile["OS"],profile["profile"],"ELLIPTIC_INDEX",index2,"LINE_INDEX",index3)
    profile_maps.append({"OS":profile["OS"],"profile":profile["profile"],
                         "elliptic_index":index2,"line_index":index3,
                         "elliptic_relations":ints(U2),"elliptic_preimages":ints(R2),
                         "line_relations":ints(U3),"line_preimages":ints(R3)})
    assert index2==index3==1
    hd=Fraction(profile["height_of_generator"])
    assert hd.numerator==1
    heightden=hd.denominator
    for selected,kind in enumerate(types):
        if not re.fullmatch(r"I\d+",kind):continue
        nu=int(kind[1:])
        if heightden%nu:continue
        ab=heightden//nu
        for a in range(1,ab+1):
            if ab%a:continue
            b=ab//a
            p=a*components[selected][1]%nu
            q=b*components[selected][1]%nu
            if gcd(q,nu)!=1:continue
            degrees=[int(j==p)-int(j==0)-int(j==(p-q)%nu)+int(j==(-q)%nu) for j in range(nu)]
            lap=[-2*int(j==0)+int(j==1%nu)+int(j==(-1)%nu) for j in range(nu)]
            if degrees!=lap:continue
            if any(i!=selected and a*k%q and b*k%q for i,(q,k) in enumerate(components)):continue
            assert gcd(a,b)==1
            matrices=[]
            for i,(B,g,kind) in enumerate(zip(Bs,gs,types)):
                beta=-a*g.T*J*B
                if re.fullmatch(r"I\d+",kind):
                    ni=int(kind[1:])
                    u,r,kappa=vanishing(B,g,ni)
                    c=Rational(-a*b*kappa*kappa,ni)+ (Rational(1,ni) if i==selected else 0)
                else:
                    z=(B-eye(2)).inv()*g
                    c=(beta*(b*z))[0]
                T=eye(4)
                T[:2,:2]=B;T[:2,3]=b*g;T[2,:2]=beta;T[2,3]=c
                assert all(x.q==1 for x in T)
                matrices.append(T)
            combined=eye(4)
            for T in matrices:combined=combined*T
            assert combined==eye(4)
            G1=Matrix.hstack(*((T-eye(4))[:3,:] for T in matrices[:-1]))
            index,R1=right_inverse(G1)
            assert index==1
            # Build the five exact wedge relations from the two universal
            # profile preimage systems, before imposing any cap.
            W=Matrix.hstack(*(exterior(T)-eye(6) for T in matrices[:-1]))
            # Exact polynomial wedge preimages. No weight is specialized in
            # these coefficient identities: E(D)=E0+D E1 and Z(D)=Z0+D Z1.
            count=len(matrices)-1
            Ang=zeros(6*count,2)
            Mixed=zeros(6*count,3)
            for i in range(count):
                for j,slot in enumerate((1,3)):
                    Ang[6*i+slot,:]=R2[2*i+j,:]
                for j,slot in enumerate((2,4)):
                    Mixed[6*i+slot,:]=R3[2*i+j,:]
            zero_weight=[]
            for T in matrices[:-1]:
                T0=T.copy();T0[:3,3]=zeros(3,1)
                zero_weight.append(T0)
            E0=Matrix.hstack(*(exterior(T)-eye(6) for T in zero_weight))
            E1=W-E0
            Eang=Matrix.hstack(eye(6)[:,1],eye(6)[:,3])
            assert E0*Ang==Eang and E1*Ang==zeros(6,2)
            Z0=Mixed-Ang*(E0*Mixed).extract([1,3],range(3))
            Z1=-Ang*(E1*Mixed).extract([1,3],range(3))
            G0=Matrix.hstack(eye(6)[:,2],eye(6)[:,4],a*eye(6)[:,5])
            G1w=Matrix.hstack(zeros(6,1),zeros(6,1),b*eye(6)[:,0])
            assert E0*Z0==G0
            assert E0*Z1+E1*Z0==G1w
            assert E1*Z1==zeros(6,3)
            # The H1 all-D Bezout section in the fresh proof.
            Ca=zeros(4*count,3)
            small=R3*Matrix.diag(a,a,1)
            for i in range(count):Ca[4*i:4*i+2,:]=small[2*i:2*i+2,:]
            assert G1*Ca==a*eye(3)
            # All four gamma columns scale under the literal weight cover.
            checks=[]
            for D in (1,2,3,4,5,6,7,12,30):
                if gcd(a,D)!=1:continue
                S=eye(4);S[3,3]=D
                Ts=[Matrix(ints(S.inv()*T*S)) for T in matrices]
                assert all(x.q==1 for T in Ts for x in T)
                productD=eye(4)
                for T in Ts:productD=productD*T
                assert productD==eye(4)
                omega=Matrix([[a,0,0,0,0,-D*b]])
                Ws=Matrix.hstack(*(exterior(T)-eye(6) for T in Ts[:-1]))
                assert omega*Ws==zeros(1,Ws.cols)
                target=Matrix.hstack(eye(6)[:,1],eye(6)[:,3],eye(6)[:,2],
                                     eye(6)[:,4],D*b*eye(6)[:,0]+a*eye(6)[:,5])
                assert hermite_normal_form(Ws)==hermite_normal_form(target)
                GD=Matrix.hstack(*((T-eye(4))[:3,:] for T in Ts[:-1]))
                assert hermite_normal_form(GD)==eye(3)
                common,alpha,betaD=egcd(a,D)
                assert common==1
                LD=Matrix.diag(*[1 if j%4==3 else D for j in range(4*count)])
                RD=alpha*Ca+betaD*LD*R1
                assert GD*RD==eye(3)
                assert Ws*(Z0+D*Z1)==G0+D*G1w
                checks.append(D)
            allrows.append({"key":[profile["OS"],profile["profile"],a,b,selected+1],
                            "fibres":types,"components":components,
                            "monodromies":[ints(T) for T in matrices],
                            "exterior_one_preimages":ints(R1),
                            "exterior_a_preimages":ints(Ca),
                            "wedge_angular_preimages":ints(Ang),
                            "wedge_mixed_preimages_constant":ints(Z0),
                            "wedge_mixed_preimages_linear":ints(Z1),
                            "checked_weights":checks})
assert len(allrows)==172
print("PASS all 172 rows derived from the defining residue equations; every literal monodromy and product verified.")
print("PASS all 21 primitive elliptic and line relation images have exact maximal-minor Bezout right inverses.")
print("PASS every permitted sampled weight has the exact primitive H1 quotient and wedge relation lattice.")
print("PASS all 172 all-D wedge preimage identities, coefficient by coefficient through degree two.")
print("PASS every all-D H1 Bezout formula has its exact integer a-section and weight-one section retained.")
out={"scope":"Fresh raw-only LD construction and primitive-exterior stage; all-parameter proof is separate.",
     "profiles":profile_maps,"rows":allrows}
(LANE/"S6_SERIES_PUBLISH_III_02LD_fresh_exterior_data.json").write_text(json.dumps(out,indent=2)+"\n")
print("SCOPE target original and historical weighted programs/outputs unopened.")
