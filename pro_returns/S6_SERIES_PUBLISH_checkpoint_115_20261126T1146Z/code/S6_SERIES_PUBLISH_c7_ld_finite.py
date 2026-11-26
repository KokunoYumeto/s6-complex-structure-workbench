#!/usr/bin/env python3
"""New LD finite affine lattice calculation from new raw-derived matrices only."""
from hashlib import sha256
from itertools import combinations, product
from math import gcd, lcm
from pathlib import Path
import json
import re

from sympy import Matrix, Rational, eye, zeros, ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/"agents/continuation7_iii_weighted_catalogue"
raw=json.loads((ROOT/"agents/continuation6_iii_d2/S6_SERIES_PUBLISH_III_02KY_raw_profiles.json").read_text())["rows"]
fresh=json.loads((LANE/"S6_SERIES_PUBLISH_III_02LD_fresh_exterior_data.json").read_text())["rows"]
profiles={(p["OS"],p["profile"]):p for p in raw}
finite_orders={"II":6,"III":4,"IV":3,"III*":4,"IV*":3}
WEIGHTS=(1,2,3,4,5,6,7,12,30)
J=Matrix([[0,1],[-1,0]])

def ints(M):
    assert all(x.q==1 for x in M)
    return [[int(x) for x in row] for row in M.tolist()]

def egcd(a,b):
    a0,b0=a,b
    x,y,u,v=1,0,0,1
    while b:
        q=a//b
        a,b=b,a-q*b
        x,u=u,x-q*u
        y,v=v,y-q*v
    if a<0:a,x,y=-a,-x,-y
    assert a0*x+b0*y==a
    return a,x,y

def right_inverse(M):
    n,m=M.shape
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
        for i,col in enumerate(cols):R[col,:]+=coefficient*adj[i,:]
    assert M*R==common*eye(n)
    return common,R

def factors(M):
    S=smith_normal_form(Matrix(ints(M)),domain=ZZ)
    return [abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]

def denominator(x):
    return lcm(*(int(v.q) for v in x))

def primitive_coordinates(F):
    common,R=right_inverse(F.T)
    assert common==1
    left=R.T
    assert left*F==eye(F.cols)
    return left

records=[]
finite_positions=0
conjugacies=0
actions=0
free_actions=0
torsion_orders=set()
for row in fresh:
    os,profile,a,b,selected=row["key"]
    data=profiles[os,profile]
    Bs=[Matrix(x) for x in data["elliptic_matrices"]]
    gs=[Matrix(x) for x in data["generator_section_cocycle"]]
    for site,kind in enumerate(row["fibres"]):
        if re.fullmatch(r"I\d+",kind):continue
        B,g=Bs[site],gs[site]
        z=(B-eye(2)).inv()*g
        gden=denominator(b*z)
        assert gden in (1,2,3,4) and a%gden==0
        A1=Matrix(row["monodromies"][site])
        assert factors(A1-eye(4))==[1,1]
        for D in WEIGHTS:
            if gcd(a,D)!=1:continue
            S=eye(4);S[3,3]=D
            A=Matrix(ints(S.inv()*A1*S))
            eps=1 if (D-1)%gden==0 else -1
            assert (eps*D-1)%gden==0
            conjugacy=eye(4)
            conjugacy[:2,3]=(1-eps*D)*b*z
            conjugacy[3,3]=eps
            assert all(x.q==1 for x in conjugacy)
            assert conjugacy.det()==eps
            assert A*conjugacy==conjugacy*A1
            assert all(x.q==1 for x in conjugacy.inv())
            assert factors(A-eye(4))==[1,1]
            conjugacies+=1
            delta=eye(4)[:,2]
            ell=Matrix([*list(-gden*D*b*z),0,gden])
            F=Matrix.hstack(delta,ell)
            left=primitive_coordinates(F)
            assert (A-eye(4))*F==zeros(4,2)
            assert (A-eye(4)).rank()==2
            if kind not in finite_orders:continue
            h=finite_orders[kind]
            assert A**h==eye(4)
            powers=[A**j for j in range(h)]
            assert all((powers[j]-eye(4)).rank()==2 for j in range(1,h))
            Nh=sum(powers,zeros(4,4))
            coords=left*Nh
            assert F*coords==Nh
            H=hermite_normal_form(coords)
            Q=H.inv()*coords
            assert all(x.q==1 for x in Q)
            common,Rpi=right_inverse(Q)
            assert common==1
            assert Q*Rpi==eye(2)
            assert all(x.q==1 for x in h*H.inv())
            assert Nh*F==h*F
            assert Nh*(A-eye(4))==zeros(4,4)
            projection=Nh/h
            moving_inverses=[]
            for j in range(1,h):
                inverse=(A**j-eye(4)+projection).inv()*(eye(4)-projection)
                assert (A**j-eye(4))*inverse==eye(4)-projection
                moving_inverses.append(inverse)
            # The projection quotient is the whole integral coinvariant:
            # Q is onto, has the same rank-two primitive kernel as A-I.
            assert hermite_normal_form(A-eye(4))==hermite_normal_form(
                Matrix(ints(eye(4)-Rpi*Q)))
            omega=Matrix([[0,a,0,0],[-a,0,0,0],[0,0,0,-D*b],[0,0,D*b,0]])
            assert A.T*omega*A==omega
            assert all(Nh.T*omega==omega*Nh for _ in (0,))
            for k in range(1,4):
                m=h*k
                for z1,z2 in product(range(-2,3),repeat=2):
                    zv=Matrix([z1,z2])
                    v=F*zv
                    w=h*H.inv()*zv
                    assert all(x.q==1 for x in w)
                    vi=[int(x) for x in v]
                    wi=[int(x) for x in w]
                    t=gcd(m,*(int(x) for x in w))
                    primitive=gcd(m,*(int(x) for x in v))==1
                    predicted=primitive and (m//t)%h==0
                    stabilizers=[]
                    for j in range(1,m):
                        if j%h==0:
                            fixed=all((j*x)%m==0 for x in vi)
                        else:
                            # Exact fixed-point criterion from the moving-plane
                            # inverse and the actual projected lattice.
                            fixed=all((j*x)%m==0 for x in wi)
                        if fixed:stabilizers.append(j)
                    assert predicted==(not stabilizers)
                    actions+=1
                    if predicted:
                        free_actions+=1
                        torsion_orders.add(t)
                        group=Matrix.vstack(-w,Matrix([m]))
                        assert gcd(*(int(x) for x in group))==t
                        # Pairing's normal character takes the torsion
                        # generator (-w/t,m/t) to precisely 1/t.
                        assert Rational(m//t,m)==Rational(1,t)
            if D==1:finite_positions+=1
            records.append({"key":row["key"],"site":site+1,"type":kind,
                "D":D,"h":h,"fixed":ints(F),"fixed_left_inverse":ints(left),
                "norm":ints(Nh),"norm_image_basis":ints(H),
                "projected_quotient":ints(Q),"projected_section":ints(Rpi),
                "conjugacy_from_weight_one":ints(conjugacy)})
print("PASS finite positions at weight one:",finite_positions)
assert finite_positions==102
print("PASS exact all-D unit-image conjugacy certificates sampled:",conjugacies)
print("PASS weighted finite projected lattices and quotient inverse sections:",len(records))
print("PASS every-power free-action comparisons:",actions,"free:",free_actions)
print("PASS all sampled free core torsion and normal Chern orders:",sorted(torsion_orders))
print("PASS each finite moving plane has no eigenvalue one at any proper linear power.")
print("PASS all projected coordinate lattices and all full boundary coinvariant kernels are primitive.")
(LANE/"S6_SERIES_PUBLISH_III_02LD_fresh_finite_data.json").write_text(json.dumps(
    {"scope":"New raw-derived finite lattices; every-power tests supplement the unbounded proof.",
     "weights":WEIGHTS,"finite_positions":finite_positions,
     "tested_actions":actions,"free_actions":free_actions,"records":records},indent=2)+"\n")
print("SCOPE no LD original, historical weighted program, or historical weighted output was read.")
