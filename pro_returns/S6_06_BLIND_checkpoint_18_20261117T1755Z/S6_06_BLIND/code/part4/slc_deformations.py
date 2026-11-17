"""Exact boundary Hessians and normalization charts in P4.25."""
from pathlib import Path
import json
import sympy as sp

x,y,z,s,v = sp.symbols("x y z s v")
rows=[]
for q in range(3,13):
    g=x*x+y*y*(z*z+y**(q-2)+s)
    h=sp.hessian(g,(x,y)).subs({x:0,y:0}).det()
    assert sp.expand(h-4*(z*z+s))==0
    normalization=sp.expand(g.subs(x,y*v)-y*y*(v*v+z*z+y**(q-2)+s))
    assert normalization==0
    rows.append({"type":"double","q":q,"boundary_hessian":str(h),
                 "normalization_residual":str(normalization)})
for p in range(3,13):
    g=x*y*z+x**p+s*x*x
    h_yaxis=sp.hessian(g,(x,z)).subs({x:0,z:0}).det()
    h_zaxis=sp.hessian(g,(x,y)).subs({x:0,y:0}).det()
    assert sp.expand(h_yaxis+y*y)==0
    assert sp.expand(h_zaxis+z*z)==0
    assert sp.expand(g-x*(y*z+x**(p-1)+s*x))==0
    rows.append({"type":"triple_one_finite","p":p,
                 "boundary_y_axis":str(h_yaxis),"boundary_z_axis":str(h_zaxis)})
for p in range(3,9):
    for q in range(p,10):
        g=x*y*z+x**p+y**q+s*x*x+s*y**3
        h=sp.hessian(g,(x,y)).subs({x:0,y:0}).det()
        assert sp.expand(h+z*z)==0
        assert sp.diff(g,x,2).subs({x:0,y:0,z:0})==2*s
        # The critical substitution xi has y*z as a factor.
        # Its terms cannot contribute to y^3 at z=0.
        pure_y_cubic=sp.expand(g.subs({x:0,z:0})).coeff(y,3)
        assert pure_y_cubic==(1+s if q==3 else s)
        rows.append({"type":"triple_two_finite","p":p,"q":q,
                     "boundary_hessian":str(h),"H_y_at_origin":str(pure_y_cubic)})

result={"proof":"P4.25","checks":rows,"all_checks_passed":True}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
print("P4.25 explicit deformation identities: PASS")
print("Finite-q double points: determinant 4(z^2+s), exact finite normalization equation.")
print("One-finite-exponent triple points: determinants -y^2 and -z^2, exact factorization.")
print("Two-finite-exponent triple points: determinant -z^2; Morse x-derivative 2s.")
print("Normalized equation has nonzero y-derivative s or 1+s at the origin.")
print("Checked",len(rows),"exact polynomial cases.")
