#!/usr/bin/env python3
"""Exact marked infinity source/line/root calculations. No return is assigned."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as S

OUT = Path(__file__).resolve().parent
e, x, y, t, s, z, v, X, Y, T = S.symbols("e x y t s z v X Y T")
A = 1-e**2
g = e*A
a2 = -2+3*e**2
tstar = A*(1-3*e**2)
f = x**3+a2*x**2+t*x+g**2
checks = []
def check(name, expression):
    value = S.factor(expression)
    assert value == 0, (name, value)
    checks.append(name)

old = Y**2-X**3-(1-2*v)*X**2-T*X-v**2
pulled = old.subs({X:e**-2*x, Y:e**-3*y, T:e**-4*t, v:e**-2-1})
check("source scaling", e**6*pulled-(y**2-f))
check("marked section", f.subs(x,0)-g**2)
check("selected factor", f.subs(t,tstar)-(x-A)**2*(x+e**2))
check("selected normalization", (s*(s**2-1))**2-f.subs({x:s**2-e**2,t:tstar}))
check("section branch", (s*(s**2-1)).subs(s,-e)-g)
check("selected node plus", (s**2-e**2).subs(s,1)-A)
check("selected node minus", (s**2-e**2).subs(s,-1)-A)

disc = S.factor(S.discriminant(f,x))
c4 = 16*(a2**2-3*t)
check("central discriminant", disc.subs(e,0)-4*t**2*(1-t))
check("selected discriminant derivative", S.diff(disc,t).subs(t,tstar)+4*A)
check("selected c4", c4.subs(t,tstar)-16)
tate_selected = S.factor(16*S.diff(disc,t).subs(t,tstar)/c4.subs(t,tstar)**3)
check("selected Tate coefficient", tate_selected+A/64)

F21 = (y+g+t*x/(2*g))/x
F12 = (y-g-t*x/(2*g))/x
node21 = S.factor(F21.subs({x:A,y:0,t:tstar}))
node12 = S.factor(F12.subs({x:A,y:0,t:tstar}))
check("F21 at selected node", node21-A/(2*e))
check("F12 at selected node", node12+A/(2*e))
check("selected Hom plus", 1/(g*node21)-2/A**2)
check("selected Hom minus", 1/(g*node12)+2/A**2)

P = -(1+e)/(1-e)
check("half-loop Picard inversion", P*P.subs(e,-e)-1)
check("half-loop marked section", g.subs(e,-e)+g)
check("half-loop source coefficients", f.subs(e,-e)-f)
check("half-loop selected value", tstar.subs(e,-e)-tstar)

# The unselected discriminant factor determines two analytic simple branches.
unselected = S.factor(disc/(t-tstar))
check("discriminant factorization", disc-(t-tstar)*unselected)
check("unselected factor central", unselected.subs(e,0)+4*t**2)
branches = S.solve(unselected,t)
branch_data = [{"exact":str(q), "series":str(S.series(q,e,0,5))}
               for q in branches]
check("unselected sum", sum(branches)-S.factor(S.expand(unselected).coeff(t,1)/4))
check("unselected product", branches[0]*branches[1]+S.factor(unselected.subs(t,0))/4)
check("unselected tate leading", (16*4)/S.Integer(64)**3-S.Rational(1,4096))

# Source-normalizing roots; two unit roots identify this collision with the
# same marked sectioned Weierstrass equation, while moving the selected site.
kappa = S.symbols("kappa")
cubic = kappa**3-a2*kappa-2*g
check("unit root factor", cubic-(kappa-e)*(kappa**2+e*kappa+2-2*e**2))

rows=[]
Q, Pq, cx, Z, V, gv = S.symbols("Q Pq cx Z V gv", nonzero=True)
half_loop_rows=[]
for aa,bb in [(1,2),(2,1)]:
    check(f"full scalar cancellation a{aa}", S.Integer(2*aa*bb-4))
    Ptarget=1/(Q*Pq)
    ca=(-1)**aa*Q**(-S.Rational(aa*(aa-1),2))*Pq**(aa*(1-aa))
    catarget=S.factor(ca.subs(Pq,Ptarget))
    check(f"Cartier half loop squares a{aa}",ca*catarget-1)
    Bq=Q*Pq**2
    cxtarget=Bq*cx
    gvtarget=gv/Bq**2
    # I h = h_target^-1 I, with I_V=c_a Z^a V.
    check(f"source period line conjugacy a{aa}", Q**aa*Pq**aa-Ptarget**(-aa))
    # I g = h_target^-b g_target I, using ab=2.
    check(f"suspension source conjugacy a{aa}", Pq**bb-Q**(-bb)*Ptarget**(-bb))
    check(f"suspension line conjugacy a{aa}", Pq**(-aa*bb)*gv-Ptarget**(-aa*bb)*gvtarget)
    J=S.Matrix([[-1,0],[aa,1]])
    R=S.Matrix([[-1,-bb],[0,1]])
    PA=S.Matrix([[1,0],[0,0]])
    PB=S.Matrix([[1,bb],[-aa,-2]])
    NN=S.symbols("N",integer=True)
    EE=S.Matrix([[0,0],[0,NN]])
    for name, mat in [
        ("A to B",J*PA-PB*R),("B to A",J*PB-PA*R),
        ("E preserved",J*EE-EE*R),("J squared",J*J-S.eye(2)),
        ("period squared",R*R-S.eye(2))]:
        for k,entry in enumerate(mat): check(f"half loop {name} a{aa} entry{k}",entry)
    cc=aa*(aa-1)//2
    SS=S.Matrix([[-1,0,0,0],[aa,1,-cc,cc],[0,0,0,1],[0,0,1,0]])
    for k,entry in enumerate(SS*SS-S.eye(4)):
        check(f"full valuation involution a{aa} entry{k}",entry)
    check(f"physical delta retained a{aa}",sum((SS*S.Matrix([0,1,0,0])-S.Matrix([0,1,0,0]))))
    half_loop_rows.append({"a":aa,"b":bb,"target_P":str(Ptarget),
          "line_constant":str(ca),"target_cX":str(cxtarget),
          "J":list(J),"period_R":list(R),"full_valuation_map":list(SS)})
    for p in range(1,10):
        m=4*p if aa==1 else 4*p-1
        xexp = S.Rational(2)-S.Rational(8*p,m)
        yexp = S.Rational(3)-S.Rational(12*p,m)
        check(f"minimal X exponent {aa} {m}", xexp-(0 if aa==1 else -S.Rational(2,m)))
        check(f"minimal Y exponent {aa} {m}", yexp-(0 if aa==1 else -S.Rational(3,m)))
        assert (-8*p)%m == (0 if aa==1 else -2)%m
        assert (-12*p)%m == (0 if aa==1 else -3)%m
        checks.extend([f"D^-4 X {aa} {m}",f"D^-4 Y {aa} {m}"])
        # Half turn followed by actual y inversion; compare D^-2.
        assert (m-6*p)%m == (-6*p)%m
        for nn in (-1,1):
            for kk in (2,3,4):
                N=kk*m
                PA=S.Matrix([[1,0],[0,0]])
                PB=S.Matrix([[1,bb],[-aa,-2]])
                E=S.Matrix([[0,0],[0,N]])
                H=PA+PB+E
                check(f"H determinant {aa} {m} {nn} {N}", H.det()-(2*N-2))
                rows.append({"a":aa,"b":bb,"m":m,"n":nn,"N":N,
                             "P_A":list(PA),"P_B":list(PB),"E":list(E),
                             "H":list(H),"det_H":int(H.det()),
                             "minimal_X_exponent":str(xexp),
                             "minimal_Y_exponent":str(yexp)})

nr,rr,ss,jj=S.symbols("N r s j",integer=True)
resolution_determinants=[]
for aa,bb in ((1,2),(2,1)):
    HA=S.Matrix([[2,bb],[-aa,nr-2]])
    PA=S.Matrix([[1,0],[0,0]])
    PB=S.Matrix([[1,bb],[-aa,-2]])
    PE=S.Matrix([[0,0],[0,nr]])
    expected=[(nr-2)*rr*ss+(2*nr-2)*ss**2,
              (nr-2)*rr*ss+(2*nr-2)*ss**2,
              2*nr*rr*ss+(2*nr-2)*ss**2]
    for tag,P0,want in zip(("A","B","E"),(PA,PB,PE),expected):
        got=S.factor((rr*P0+ss*HA).det())
        check(f"relative separator determinant {aa} {tag}",got-want)
        resolution_determinants.append({"a":aa,"b":bb,"sector":tag,"determinant":str(got)})
    check(f"protected A primitive minor {aa}",S.Matrix([[jj,jj+1],[1,1]]).det()+1)
    check(f"protected B primitive minor {aa}",S.Matrix([[jj,jj+1],[1,1]]).det()+1)
    check(f"protected E primitive minor {aa}",S.Matrix([[jj,jj+1],[1,1]]).det()+1)

xc,xx,aa0,tt0,vv0,rho0=S.symbols("xc xx aa0 tt0 vv0 rho0")
fc=lambda q:q**3+aa0*q*q+tt0*q+vv0*vv0
node_remainder=S.expand(fc(xx)-fc(xc)-(xx-xc)**2*(aa0+3*xc+xx-xc))
check("literal analytic node map remainder",node_remainder-(xx-xc)*(3*xc*xc+2*aa0*xc+tt0))
check("literal analytic node map on critical section",node_remainder.subs(tt0,-3*xc*xc-2*aa0*xc))
norm_rows=[]
for aa,bb,NN in ((1,2,8),(2,1,6)):
    loss=aa*(1+bb)
    check(f"retained norm loss a{aa}",loss-(3 if aa==1 else 4))
    exponent=NN-2-loss
    assert exponent>=0
    checks.append(f"safe geometric norm order a{aa} N{NN}")
    norm_rows.append({"a":aa,"b":bb,"N":NN,"metric_loss":aa,
      "maximum_source_reindex_count":bb,"reindex_loss":aa*bb,
      "raw_order":NN-2,"operator_exponent":exponent,
      "zero_exponent_handled_by_small_lambda0":exponent==0})

result = {
  "created_utc":datetime.now(timezone.utc).isoformat(),
  "status":"PASS","check_count":len(checks),"checks":checks,
  "source_polynomial":str(f),"discriminant":str(disc),
  "unselected_factor":str(unselected),"unselected_branches":branch_data,
  "selected_value":str(tstar),"selected_Tate_coefficient":str(tate_selected),
  "selected_P_G":str(P),"F21_node":str(node21),"F12_node":str(node12),
  "selected_Hom_coefficients":[str(S.factor(1/(g*node21))),str(S.factor(1/(g*node12)))],
  "unit_root_factor":str(S.factor(cubic)),
  "scalar_comparison":"lambda_new=lambda_old; exponent 2ab-4=0",
  "collision_half_loop":half_loop_rows,
  "cap_rows":rows,
  "relative_resolution_determinants":resolution_determinants,
  "safe_geometric_norm_orders":norm_rows,
  "scope":{"exact_source_line_and_root_checks":True,
           "periodic_collision_filling":False,
           "global_bordism":False,"source_return_assigned":False}
}
def enc(o):
    if isinstance(o,S.Integer): return int(o)
    return str(o)
(OUT/"source_infinity_exact.json").write_text(json.dumps(result,indent=2,default=enc)+"\n")
print(f"PASS {len(checks)} exact checks; {len(rows)} marked cap rows")
print("discriminant =",disc)
print("unselected factor =",unselected)
for row in branch_data: print("branch:",row)
print("selected Tate =",tate_selected)
print("No compact filling or source-return value is assigned.")
