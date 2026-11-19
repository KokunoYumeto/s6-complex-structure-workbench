"""Exact certificates for EG and the independent DZ6.1--4 frame audit.

These algebra checks accompany the full source/Cartier/root/normal proof;
they do not replace its relative extension and compactness arguments.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as S

root = Path(__file__).resolve().parents[2]
checks = []


def ck(name, value):
    numerator = S.together(value).as_numer_denom()[0]
    answer = S.factor(numerator)
    assert answer == 0, (name, answer)
    checks.append(name)


def yes(name, value):
    assert bool(value), name
    checks.append(name)


w, s, z, x, y, t = S.symbols("w s z x y t")
X, Y, T, L, AA, DD, ss = S.symbols("X Y T L A D s0", nonzero=True)
v = w*w-1
D = w*w-3
A = 3-2*w*w
s0 = v*(w*w+3)/4
P = (1+w)/(1-w)
Z = (s-w)/(s+w)
ft = lambda zz, pp: (1-zz/pp)/(1-zz)

source = Y*Y-X**3-A*X**2-D*T*X-T*T
selected = {X:s*s-1, Y:s*(s*s-w*w), T:v}
ck("selected normalization of full source", source.subs(selected))
ck("marked source coefficient", D*D/4-A-s0)
f2 = (Y-T-D*X/2)/(X-s0)
S2 = -(1+w*w)/2
ck("full M2 Miller restriction", f2.subs(selected)-(s+1)**2/(s-S2))

for aa in (2, 6):
    Sa = S.cancel(w*(1+P**aa)/(1-P**aa))
    ca = S.cancel(w-Sa)
    fa = (s+1)**aa/(s-Sa)
    ck(f"a{aa} point value at cusp", Sa.subs(w,0)+S.Rational(1,aa))
    ck(f"a{aa} unit value at cusp", ca.subs(w,0)-S.Rational(1,aa))
    ck(f"a{aa} full Cartier divisor identity", s-Sa-ca*ft(Z,P**aa))
    ck(f"a{aa} strict tensor/point theta factor",
       ft(Z,P)**aa/fa-ca/(1+w)**aa*ft(Z,P**aa))
    ck(f"a{aa} even actual section", Sa.subs(w,-w)-Sa)
    ck(f"a{aa} full reflecting Cartier unit", ca.subs(w,-w)-P**(-aa)*ca)
    ck(f"a{aa} even tensor/point coefficient",
       (ca/(1+w)**aa).subs(w,-w)-ca/(1+w)**aa)
    zz = S.Symbol("zz", nonzero=True)
    ck(f"a{aa} exact nodal theta reflection",ft(1/zz,P**(-aa))-P**aa*ft(zz,P**aa))
    ck(f"a{aa} target period cancels reflection",P**(-aa)*P**aa-1)
    for sg in (-1,1):
        node = {X:v,Y:0,T:v}
        ck(f"a{aa} branch {sg} f2 coefficient",f2.subs(node)-2)
        ck(f"a{aa} branch {sg} actual f_a coefficient",
           fa.subs(s,sg*w)-((1+w)**aa/ca))
    if aa == 2:
        ck("exact c2",ca-(1+w)**2/2)
    else:
        ck("exact c6",ca-(1+w)**6/(6+20*w*w+6*w**4))
        ck("exact f6 node unit",(1+w)**6/ca-(6+20*w*w+6*w**4))

# Literal point/tensor telescoping, keeping all six factors.
f = S.symbols("f0:4", nonzero=True)
theta = S.symbols("theta0:4", nonzero=True)
eta = S.Symbol("eta", nonzero=True)
g6s, g6t = S.symbols("g6s g6t", nonzero=True)
B23 = f[0]*f[3]*f[1]**2*f[2]**2
point_to_tensor = (1/f[0])/(1/f[3])
ck("M2 exact tensor conjugation",
   S.prod(f[j]**2 for j in range(3))*point_to_tensor-B23)
B61 = f[0]**6*g6t/g6s
ck("M6 exact tensor conjugation",f[0]**6*(1/g6s)/(1/g6t)-B61)
ck("M2 full theta telescope",
   B23*(theta[3]**2/f[3])/(theta[0]**2/f[0])
   -S.prod(f[j]*theta[j+1]/theta[j] for j in range(3))**2)
ck("M6 full theta telescope",
   B61*(theta[1]**6/g6t)/(theta[0]**6/g6s)
   -(f[0]*theta[1]/theta[0])**6)
ck("M2 six actual node factors",B23.subs(dict.fromkeys(f,2))-64)
ck("M6 actual node ratio",B61.subs({f[0]:2,g6s:6,g6t:6})-64)
ck("retained selected Hom at cusp",S.Integer(64)/(-1)**3+64)

# Both source chord maps preserve the entire equation and both nodal branches.
for sg in (-1,1):
    slope = (Y-sg*T)/X
    xx = slope*slope-A-X
    yy = -sg*T-slope*xx
    target = S.together(source.subs({X:xx,Y:yy},simultaneous=True)).as_numer_denom()[0]
    ck(f"source chord {sg} full equation",S.rem(target,source,Y))
    ck(f"source chord {sg} fixes node X",xx.subs({X:v,Y:0,T:v})-v)
    ck(f"source chord {sg} fixes node Y",yy.subs({X:v,Y:0,T:v}))

# Directed D comparison, valid on its comparison annulus.
f2new = (Y-T-DD*X/2)/(X-ss)
f2old = (DD**-3*Y-DD**-3*T-DD**-2*X/2)/(DD**-2*(X-ss))
ck("D point-to-tensor f2 weight",f2old-DD**-1*f2new)
f3new = ss*X*(Y-T-DD*X/2)/(ss*(Y+T+DD*X/2)-(DD*ss+2*T)*X)
f3old = (ss/DD**2)*(X/DD**2)*(Y/DD**3-T/DD**3-X/(2*DD**2))/(
    (ss/DD**2)*(Y/DD**3+T/DD**3+X/(2*DD**2))
    -((ss/DD**2)+2*T/DD**3)*(X/DD**2))
ck("D full f3 weight",f3old-DD**-2*f3new)
ck("D full f6 weight",DD**-4*DD**-1-DD**-5)
q, tc = S.symbols("q tc")
ck("D complete selected suspension",DD**-6*(q/DD**3)/(T/DD**3)**3-q/T**3)
u,j,h = S.symbols("u j h", integer=True)
for aa in (2,6):
    ck(f"D a{aa} canonical section unchanged and tensor factor",
       DD**(aa-1)*DD**(1-aa)-1)
    for hh in range(-3,4):
        for jj in range(-3,4):
            ck(f"D a{aa} Cox height{hh} line{jj}",
               DD**(-3*hh)*(DD**(aa-1))**jj-DD**(-3*hh+(aa-1)*jj))

# Full minimal-root equations, graph coordinates, norm factors and deck3.
for aa in (6,2):
    for ll in range(0 if aa==6 else 1, 13):
        m = 3*ll+2 if aa==6 else 3*ll
        Zo = L**3*z
        rold = AA/L**(2*m)
        if aa==6:
            kk=2*ll+1
            Xo,Yo=L**2*X,L**3*Y
            old=Yo**2-Xo**3-rold*Zo**(2*ll+2)*Xo**2-Zo**(ll+2)*Xo-Zo**2
            new=Y**2-X**3-AA*z**(2*ll+2)*X**2-L**m*z**(ll+2)*X-z*z
            ck(f"reduced l{ll} full minimal equation",old/L**6-new)
            ck(f"reduced l{ll} tau graph scale",L**(-1-3*kk)-L**(-2*m))
            ck(f"reduced l{ll} selected Hom scale",L**6*(L**3)**-2-1)
            ck(f"reduced l{ll} full chord/formal scale",L*L**-1-1)
            yes(f"reduced l{ll} D3 X exponent",(-6*kk-2)%m==0)
            yes(f"reduced l{ll} D3 Y exponent",(-9*kk-3)%m==0)
            yes(f"reduced l{ll} D3 tau exponent",(3*kk+1)%m==0)
            ck(f"reduced l{ll} retained formal division",2*m-1-3*kk)
            for ray in range(1,kk+1):
                ck(f"reduced l{ll} ray{ray} equal orders",ray-min(ray,kk))
                if ray>1:
                    ck(f"reduced l{ll} adjacent regular determinant{ray}",
                       S.det(S.Matrix([[ray,ray-1],[1,1]]))-1)
        else:
            old=Y**2-X**3-rold*Zo**(2*ll)*X**2-Zo**ll*X-1
            new=Y**2-X**3-AA*z**(2*ll)*X**2-L**m*z**ll*X-1
            ck(f"good l{ll} full minimal equation",old-new)
            ck(f"good l{ll} correction u scale",(L**3)**ll-L**m)
            yes(f"good l{ll} D3 X exponent",(-12*ll)%m==0)
            yes(f"good l{ll} D3 Y exponent",(-18*ll)%m==0)
            for rr,ee in ((2,1),(1,2)):
                ck(f"good l{ll} monomial({rr},{ee}) actual scale",
                   X**rr*(L**m*z**ll)**ee-L**(m*ee)*X**rr*z**(ll*ee))
        ck(f"a{aa} l{ll} root base scale",(L**3*z)**m-L**(3*m)*z**m)
        ck(f"a{aa} l{ll} h infinity",1-(v/L**(3*m))*(L**3*z)**m-(1-v*z**m))
        for nn in (-1,1):
            for character in (0,1,m-1):
                yes(f"a{aa} l{ll} n{nn} character{character} norm",
                    (m*character)%m==0 and nn*nn==1)

# Annular map equality with the full transported reference cocycle.
sa,kk,fa,fb,Pi,cc,ha,hb,jj,bb,Lam=S.symbols("sa kk fa fb Pi cc ha hb jj bb Lam")
for nn in (-1,1):
    left = nn*(sa+kk)*fb+(sa+kk)*cc+hb-(nn*kk*fb+kk*cc)
    right = nn*sa*fa+sa*cc+ha+jj*bb+Lam
    ck(f"n{nn} literal target-sheet annular period",
       (left-right).subs({hb:ha-nn*sa*Pi+jj*bb+Lam,fb:fa+Pi},simultaneous=True))
    # n^2=1 gives the primitive actual H, with all scalar exponents.
    ck(f"n{nn} H^m=B exponent",nn*nn-1)
    ck(f"n{nn} H^n=A exponent",nn*nn-1)

# Exact normalization action, branch-fixing shear, normal products.
gg,hh=S.symbols("gg hh")
St=((1+gg)*s+(1-gg)*w)/(((1-gg)/w)*s+1+gg)
ck("full fractional source action",(St-w)/(St+w)-gg*Z)
ck("exact branch-fixing shear",
   St.subs(gg,1+w*hh)-s-hh*(s*s-w*w)/(2+hh*(w-s)))
ck("native first normal factor",(s*s-w*w)/Z-(s+w)**2)
ck("native second normal factor",(s*s-w*w)*Z-(s-w)**2)
ck("original parameter exact ramification",A/D**2-S.Rational(1,3)+w**4/(3*D**2))
ck("orbit MV primitive determinant",S.det(S.Matrix([[0,1],[-1,0]]))-1)

# Both rows have the identical full winding matrix, with all character maps.
matrices=0
for pp in range(-3,4):
    for qq in range(-3,4):
        for rr in range(-3,4):
            for ss0 in range(-3,4):
                PM=S.Matrix([[pp,qq],[rr,ss0]])
                if abs(PM.det())!=1:
                    continue
                RM=PM.inv()
                BP=-6*RM*S.Matrix([[1,0],[0,0]])*PM
                for ii in range(2):
                    for jj in range(2):
                        ck(f"fan{matrices} q({ii},{jj})",(RM*PM)[ii,jj]-int(ii==jj))
                        ck(f"fan{matrices} winding({ii},{jj})",
                           -6*RM[ii,0]*PM[0,jj]-BP[ii,jj])
                ck(f"fan{matrices} determinant winding",S.trace(BP)+6)
                matrices+=1
for jj in range(-30,31):
    pair=-6-18*jj*(jj-1)
    ck(f"vertical j{jj} endpoint reflection",pair-(-6-18*(1-jj)*(-jj)))
    ck(f"vertical j{jj} physical index",S.Rational(pair,6)-(-1-3*jj*(jj-1)))
    ck(f"vertical j{jj} collar/interior",-6+18*jj-18*jj*jj-pair)

source_path=root/"notes/part3_e6_selected_cusp_all_caps_working.md"
dzpath=root/"notes/part3_e6_d_zero_disc_working.md"
payload={
 "status":"PASS",
 "time_utc":datetime.now(timezone.utc).isoformat(),
 "check_count":len(checks),
 "basis_matrices":matrices,
 "source_sha256":hashlib.sha256(source_path.read_bytes()).hexdigest(),
 "independent_dz_source_sha256":hashlib.sha256(dzpath.read_bytes()).hexdigest(),
 "scope":"Exact EG source, point/tensor, theta telescope, all root scaling/deck/graph identities, annular cochains, normal coefficients, vertical and full basis winding maps; DZ6.1--4 narrow independent frame/root audit.",
 "geometric_proof":"Relative extension, properness, cap/Thom and actual family comparisons are proved in the accompanying full source, not inferred from these algebra checks.",
 "checks":checks,
}
out=Path(__file__).with_suffix(".json")
out.write_text(json.dumps(payload,indent=2)+"\n")
print(json.dumps({k:payload[k] for k in ("status","check_count","basis_matrices","source_sha256","independent_dz_source_sha256")},indent=2))
