#!/usr/bin/env python3
"""02OG post-release comparison, independent of the frozen fresh program.

Inputs are the individually released proof, its supplied S,R definitions, and
the saved fresh data.  This program does not read the manuscript or KP files.
It checks exact maps and inverse maps, including all original auxiliary data.
"""
from pathlib import Path
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
OWN = ROOT / "agents/continuation6_iii_carriers"
fresh = json.loads((OWN / "S6_SERIES_PUBLISH_III_02OG_fresh_maps.json").read_text())
I = s.eye(2)
Omega = s.Matrix([[0, 1], [-1, 0]])
T = s.Matrix([[1, 1], [0, 1]])
S = s.Matrix([[0, -1], [1, 0]])
R = S*T
H0 = S*R.inv()*S.inv()
V0 = R.inv()*T*R
B0 = V0**3
C0 = (R*S*R.inv())*T**2*(R*S*R.inv()).inv()
assert H0 == s.Matrix([[0, 1], [-1, 1]])
assert V0 == s.Matrix([[2, 1], [-1, 0]])
assert B0 == s.Matrix([[4, 3], [-3, -2]])
assert C0 == s.Matrix([[5, 2], [-8, -3]])
assert H0*T**3*(-V0) == I
assert C0*H0*T**5*B0 == I
print("canonical matrices", *[m.tolist() for m in (H0,V0,B0,C0)])
print("canonical integral products I,I; inverses V,B",V0.inv().tolist(),B0.inv().tolist())

def inv(w):
    return [-v for v in w[::-1]]

def reduce_word(w):
    out=[]
    for v in w:
        if out and out[-1]==-v:
            out.pop()
        else:
            out.append(v)
    return out

def subst(w, images):
    out=[]
    for v in w:
        q=images[abs(v)]
        out.extend(q if v>0 else inv(q))
    return reduce_word(out)

def power(w,n):
    return (w if n>=0 else inv(w))*abs(n)

def conj(u,v):
    return u+v+inv(u)

def pinv(p):
    return [p.index(i) for i in range(len(p))]

def cycles(p):
    seen=set();out=[]
    for q in range(len(p)):
        if q not in seen:
            c=[];x=q
            while x not in seen:
                seen.add(x);c.append(x);x=p[x]
            out.append(c)
    return out

def connected(edges,vertices):
    seen={vertices[0]}
    while True:
        old=len(seen)
        for x,y in edges:
            if x in seen: seen.add(y)
            if y in seen: seen.add(x)
        if len(seen)==old: return len(seen)==len(vertices)

raw={
 "50":[s.Matrix([[3,7],[-1,-2]]),s.Matrix([[7,12],[-3,-5]]),s.Matrix([[-2,-1],[1,0]])],
 "56":[s.Matrix([[5,8],[-2,-3]]),s.Matrix([[27,37],[-19,-26]]),s.Matrix([[61,80],[-45,-59]]),s.Matrix([[4,3],[-3,-2]])]
}
original={
 "50":{"s":[1,0,3,2],"r":[2,1,3,0],"omit":[3]},
 "56":{"s":[1,0,4,5,2,3,9,8,7,6],"r":[2,1,3,0,6,8,7,4,9,5],"omit":[8,9]}
}
results={}
for key,o in original.items():
    sp,rp=o["s"],o["r"];n=len(sp);ri=pinv(rp)
    assert all(sp[sp[i]]==i and rp[rp[rp[i]]]==i for i in range(n))
    cp=[rp[sp[i]] for i in range(n)]
    sc,rc,cc=cycles(sp),cycles(rp),cycles(cp)
    assert connected([(i,sp[i]) for i in range(n)]+[(i,rp[i]) for i in range(n)],list(range(n)))
    assert [len(c) for c in cc] == ([3,1] if key=="50" else [5,3,2])
    ram=[sum(len(c)-1 for c in cs) for cs in (rc,sc,cc)]
    assert ram==([2,2,2] if key=="50" else [6,5,7])
    assert sum(ram)==2*n-2
    if key=="50":
        # The original centralizer claim, with explicit conjugation maps.
        matchings=[[1,0,3,2],[2,3,0,1],[3,2,1,0]]
        orbit=[];current=matchings[0]
        for _ in range(3):
            orbit.append(current)
            current=[rp[current[ri[i]]] for i in range(4)]
        assert sorted(orbit)==sorted(matchings) and current==matchings[0]
        print("50 the three matchings form one orbit under conjugation by r; inverse is conjugation by r^-1")
    # Original half-edge tree and its exact collapsed path reader.
    black={q:i for i,c in enumerate(rc) for q in c}
    white={q:i for i,c in enumerate(sc) for q in c}
    vs=[("q",i) for i in range(n)]+[("b",i) for i in range(len(rc))]+[("w",i) for i in range(len(sc))]
    edges=[(("q",q),("b",black[q])) for q in range(n)]
    edges += [(("q",q),("w",white[q])) for q in range(n) if q not in o["omit"]]
    assert len(edges)==len(vs)-1 and connected(edges,vs)
    chord={q:i+1 for i,q in enumerate(o["omit"])};e=len(chord)+1
    def walk_old(w,start=0):
        q=start;out=[]
        for v in w:
            if abs(v)==1:  # s; inverse uses the same filled white half-disk.
                dest=sp[q]
                if q in chord: out.append(chord[q])
                if dest in chord: out.append(-chord[dest])
            else:
                dest=(rp if v>0 else ri)[q]
                if dest==q: out.append(e if v>0 else -e)
            q=dest
        return q,reduce_word(out)
    tw=[1,2]
    vw=conj([-2],tw)
    hw=conj([1],[-2])
    bw=power(vw,3)
    cw=conj([2,1,-2],power(tw,2))
    words=[power(tw,3),vw,hw] if key=="50" else [power(tw,5),bw,cw,hw]
    expected=[[e,-1],[1],[-e]] if key=="50" else [[e,-2],[1],[-1,2],[-e]]
    got=[]
    for w,answer in zip(words,expected):
        endpoint,form=walk_old(w);assert endpoint==0 and form==answer;got.append(form)
    assert reduce_word(sum(got,[]))==[]
    # Bridge s,r to the fresh positive a,b symbols: a=s*r^-1*s^-1,b=s.
    af=[sp[ri[sp[i]]] for i in range(n)]
    an,bn=fresh[key]["surface"]["a"],fresh[key]["surface"]["b"]
    maps=[]
    for root_image in range(n):
        f={0:root_image};todo=[0];ok=True
        while todo and ok:
            q=todo.pop(0)
            for po,pn in ((af,an),(sp,bn)):
                q1=po[q];j=pn[f[q]]
                if q1 in f:
                    if f[q1]!=j:ok=False;break
                else:f[q1]=j;todo.append(q1)
        if ok and len(f)==n and len(set(f.values()))==n:
            maps.append([f[i] for i in range(n)])
    assert len(maps)==1
    bij=maps[0];bijinv=pinv(bij)
    assert all(bijinv[bij[i]]==i for i in range(n))
    surf=fresh[key]["surface"]
    aedges={int(k):v for k,v in surf["a_edges"].items()}
    bedges={int(k):v for k,v in surf["b_edges"].items()}
    def walk_new(w,start=0):
        q=start;out=[]
        for v in w:
            p=an if abs(v)==1 else bn;es=aedges if abs(v)==1 else bedges
            if v>0: dest=p[q];part=es[q]
            else: dest=pinv(p)[q];part=inv(es[dest])
            out.extend(part);q=dest
        return q,reduce_word(out)
    h=surf["tree_paths"][str(bij[0])]
    translated=[]
    for w in words:
        converted=subst(w,{1:[2],2:[-2,-1,2]})
        end,form=walk_new(conj(h,converted));assert end==0;translated.append(form)
    print(key,"cycles",sc,rc,cc,"ramification",ram,"tree",len(vs),len(edges))
    print(key,"original free peripheral words",got)
    print(key,"old-to-fresh sheets",bij,"inverse",bijinv,"root path",h)
    print(key,"old canonical peripherals in fresh graph",translated)
    results[key]={"sheets":bij,"inverse_sheets":bijinv,"root_path":h,"old_peripherals_in_fresh_graph":translated}

# Literal free isomorphisms comparing ordered target peripheral bases.  In the
# old graph alpha,beta,e map to the following fresh x,y,z words.
comparison_free={
 "50":({1:[2],2:[-1]}, {1:[-2],2:[1]},[[2],[1,-2]],[[2,1,-2],[2,-1,-2,-2],[2]]),
 "56":({1:[3],2:[2],3:[-1]}, {1:[-3],2:[2],3:[1]},[],[])
}
for key,(f,g,_,__) in comparison_free.items():
    for i in f: assert subst(f[i],g)==[i]
    for i in g: assert subst(g[i],f)==[i]
    if key=="50":
        oldrot=[[-2],[2,-1],[1]]
        mapped=[reduce_word(conj([2],subst(w,f))) for w in oldrot]
    else:
        # C,H,T^5,B, in the cover bridge; the period basis is changed separately.
        oldrot=[[-1,2],[-3],[3,-2],[1]]
        mapped=[subst(w,f) for w in oldrot]
    assert mapped==fresh[key]["surface"]["peripheral_words"]
    print(key,"exact target free maps",f,"inverse",g,"peripherals",mapped)

assert [V0*m*V0.inv() for m in [H0,T**3,-V0]]==raw["50"]
assert [B0*m*B0.inv() for m in [C0,H0,T**5,B0]]==raw["56"]
Hfresh=s.Matrix([[4,-1],[-3,1]])
K=Hfresh.inv()*B0
assert K.det()==1
norm56=[s.Matrix([[-3,2],[-8,5]]),s.Matrix([[-1,3],[-1,2]]),T**5,s.Matrix([[1,0],[-3,1]])]
assert [K*m*K.inv() for m in [C0,H0,T**5,B0]]==norm56
print("56 old canonical to fresh normalized period map",K.tolist(),"inverse",K.inv().tolist())

t,u,x,y,v=s.symbols("t u x y v")
c4=t**2*(t+27)*(t+3)
c6=t**3*(t+27)*(t*t+18*t-27)
delta=t**7*(t+27)**2
assert s.expand(c4**3-c6**2-1728*delta)==0
j=(t+27)*(t+3)**3/t
assert s.factor(j-1728)==(t*t+18*t-27)**2/t
F=3*u*(u+8);H=u*(u*u-20*u-8)
base=27/(u-1);baseinv=1+27/t
assert s.cancel(base.subs(u,baseinv)-t)==0
assert s.cancel(baseinv.subs(t,base)-u)==0
assert s.cancel(j.subs(t,base)-1728*F**3/(F**3-27*H**2))==0
alpha=-s.Rational(81,2);beta=729*s.I/(4*s.sqrt(2))
xo=alpha*x/(u-1)**2;yo=beta*y/(u-1)**3
monic=yo**2-xo**3+c4.subs(t,base)*xo/48+c6.subs(t,base)/864
assert s.cancel(monic-beta**2*(y**2-4*x**3+F*x+H)/(u-1)**6)==0
assert s.cancel((xo/alpha*(u-1)**2)-x)==0
assert s.cancel((yo/beta*(u-1)**3)-y)==0
sold=(u-1)/27
assert s.cancel(sold**2*xo)==-x/18
assert s.simplify(sold**3*yo)==s.I*y/(108*s.sqrt(2))
assert s.cancel(base.subs(u,1/v)-27*v/(1-v))==0
assert s.cancel(xo.subs({u:1/v,x:x/v**2},simultaneous=True)-alpha*x/(1-v)**2)==0
assert s.simplify(yo.subs({u:1/v,y:y/v**3},simultaneous=True)-beta*y/(1-v)**3)==0
print("50 exact base map",base,"inverse",baseinv,"fiber factors",alpha,beta)
print("50 endpoint charts: old infinity (-x/18, i*y/(108*sqrt(2))); fresh infinity unit factors alpha/(1-v)^2,beta/(1-v)^3")
for key in ("50","56"):
    FF=s.sympify(fresh[key]["g2"]);HH=s.sympify(fresh[key]["g3"])
    DD=s.sympify(fresh[key]["delta"])
    assert s.expand((12*FF)**3-(216*HH)**2-1728*DD)==0
print("both monic c4=12F,c6=216H,Delta=F^3-27H^2 verified")

for key,As in raw.items():
    n=len(As);Ps=[];P=I
    for A in As:Ps.append(P);P=P*A
    assert P==I
    qs=[s.Matrix(q) for q in (([-5,2],[-8,4],[0,1]) if key=="50" else ([-2,1],[0,0],[4,-3],[1,-1]))]
    ys=[p*q for p,q in zip(Ps,qs)]
    Ks=[p*A.inv()*p.inv() for p,A in zip(Ps,As)]
    prod=I
    for K in Ks: prod=prod*K
    assert prod==I and sum(ys,s.zeros(2,1))==s.zeros(2,1)
    h1,h2,k,ell,j1,j2=s.symbols("h1 h2 k ell j1 j2")
    hh=s.Matrix([h1,h2]);jj=s.Matrix([j1,j2])
    cs=[k*q+(A-I)*hh for q,A in zip(qs,As)]
    ds=[ell*q+(A-I)*jj for q,A in zip(qs,As)]
    zz=[s.Matrix(z) for z in fresh[key]["fixed_point_vectors"]]
    zc=[k*z+hh for z in zz];zd=[ell*z+jj for z in zz]
    for i,(K,P,A,c,z) in enumerate(zip(Ks,Ps,As,cs,zc)):
        yi=P*c;prong=P*(z+c)
        assert s.simplify((I-K)*prong-yi)==s.zeros(2,1)
        assert s.simplify(P.inv()*yi-c)==s.zeros(2,1)
        # In Fukae's reversed list, preceding circuits act in reverse order.
        preceding=I
        for j in range(i+1,n): preceding=preceding*Ks[j]
        Pnext=P*A
        assert preceding==Pnext
        assert (I-K)*Pnext==Pnext-P
    def wedge(a,b):return (a.T*Omega*b)[0]
    Bpair=0
    for i in range(n):
        beta_row=-cs[i].T*Omega*As[i]
        Bpair-=(beta_row*zd[i])[0]
        middle=I
        for j in range(i+1,n):
            Bpair-=(beta_row*middle*ds[j])[0]
            middle=middle*As[j]
    b_wedge=-sum(wedge(zc[i],ds[i]) for i in range(n))
    b_wedge+=sum(wedge(Ps[i]*cs[i],Ps[j]*ds[j]) for i in range(n) for j in range(i+1,n))
    assert s.expand(Bpair-b_wedge)==0
    assert s.expand(Bpair-k*ell/(12 if key=="50" else 30))==0
    diagonal=sum(wedge(zz[i],qs[i]) for i in range(n))
    cross=sum(wedge(ys[i],ys[j]) for i in range(n) for j in range(i+1,n))
    print(key,"Fukae circuits reversed",[K.tolist() for K in Ks[::-1]],"prefix charges",[y.T.tolist()[0] for y in ys])
    print(key,"Fukae inverse, prongs, null sweep and reverse preceding products exact; bilinear equality",s.expand(Bpair),"wedges",diagonal,cross)
    IIindex=0 if key=="50" else 1
    branch=(As[IIindex]-I).inv()*qs[IIindex]
    gauge=[q-(A-I)*branch for q,A in zip(qs,As)]
    generic_h=(As[IIindex]-I).inv()*cs[IIindex]
    generic_gauge=[c-(A-I)*generic_h for c,A in zip(cs,As)]
    generic_k=generic_gauge[1 if key=="50" else 0][1]
    assert s.expand(generic_k-k)==0
    assembly_h=generic_h-k*branch
    assert s.simplify(assembly_h-hh)==s.zeros(2,1)
    assert all(s.simplify(c-(A-I)*assembly_h-k*q)==s.zeros(2,1) for c,A,q in zip(cs,As,qs))
    print(key,"type-II gauge",branch.T.tolist()[0],[q.T.tolist()[0] for q in gauge])
    print(key,"receiver gauge and assembly maps recover the full symbolic (h1,h2,k), both inverse directions")
    if key=="50":assert gauge==[s.Matrix([0,0]),s.Matrix([-2,1]),s.Matrix([2,-1])]
    else:
        assert gauge==qs
        oldz=s.Matrix([-s.Rational(1,5),s.Rational(1,5)])
        diff=oldz-zz[2]
        assert diff==-s.Rational(1,15)*s.Matrix([4,-3])
        assert (As[2]-I)*diff==s.zeros(2,1)
        print("56 original versus fresh z3 difference",diff.T.tolist()[0],"in invariant kernel")

# Explicit reversal by adjacent inverse Hurwitz moves, checked in the free
# group on all puncture letters before imposing the product-one relation.
for n in (3,4):
    basis=[[i+1] for i in range(n)]
    history=[]
    for block in range(n-1,0,-1):
        for i in range(block):
            olda,oldb=basis[i],basis[i+1]
            basis[i:i+2]=[reduce_word(conj(olda,oldb)),olda]
            history.append(i)
    prefixes=[list(range(1,i+1)) for i in range(n)]
    want=[reduce_word(conj(prefixes[i],[i+1])) for i in range(n)][::-1]
    assert basis==want
    for i in history[::-1]:
        u0,v0=basis[i],basis[i+1]
        basis[i:i+2]=[v0,reduce_word(conj(inv(v0),u0))]
    assert basis==[[i+1] for i in range(n)]
    print(n,"Hurwitz adjacent positions",history,"reversed conjugate peripherals",want,"inverse recovered all generators")

(OWN/"S6_SERIES_PUBLISH_III_02OG_comparison_maps.json").write_text(json.dumps(results,indent=2)+"\n")
print("ALL POST-RELEASE COMPARISON ASSERTIONS PASSED")
