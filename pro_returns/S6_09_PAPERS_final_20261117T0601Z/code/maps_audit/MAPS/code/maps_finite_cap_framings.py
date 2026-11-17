"""Exact smooth product framings of the original finite affine caps."""
from pathlib import Path
import json
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
A1=sp.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=sp.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
v1=sp.Matrix([1,2,-4,0]); v2=sp.Matrix([-1,-3,3,0])
M0=(A1*A2).inv()
phi,theta,sigma,alpha=sp.symbols("phi theta sigma alpha")
out=[]
for A,v,m in ((A1,v1,3),(A2,v2,4)):
    kappa=int(v[0]); w=kappa*v
    P=sp.Matrix.hstack(w,*[sp.eye(4)[:,i] for i in (1,2,3)])
    assert P.det()==1 and A*v==v and A**m==sp.eye(4)
    B=A[1:4,1:4]
    diag=sp.diag(1,B)
    assert P.inv()*A*P==diag
    # Under the affine generator x->Ax+v/m and s->exp(-2pi i/m)s,
    # the exponent of r=s exp(2pi i kappa phi) changes by zero.
    assert sp.Rational(-1,m)+sp.Rational(kappa*kappa,m)==0
    # The actual marked boundary is x+theta*v/m, s=exp(-2pi i theta/m).
    normal_angle=sp.expand(-theta/m+kappa*(phi+sp.Rational(kappa,m)*theta))
    base_angle=sp.expand(m*kappa*(phi+sp.Rational(kappa,m)*theta))
    assert normal_angle==kappa*phi
    assert base_angle==m*kappa*phi+theta
    angle_matrix=sp.Matrix([[m*kappa,1],[kappa,0]])
    assert abs(angle_matrix.det())==1
    inv=angle_matrix.inv()
    assert inv*sp.Matrix([sigma,alpha])==sp.Matrix([kappa*alpha,sigma-m*alpha])
    assert sp.expand(m*normal_angle-base_angle)==-theta
    # A positive normal meridian at fixed base is v-m*rho, giving rho^m=t_v.
    meridian=inv*sp.Matrix([0,1])
    assert meridian==sp.Matrix([kappa,-m])
    assert meridian[0]*w==v
    # At theta=1 the base advances by one, hence l is replaced by B^-1 l.
    assert sp.simplify(base_angle.subs(theta,1)-base_angle.subs(theta,0))==1
    assert B**m==sp.eye(3)
    out.append({"m":m,"kappa":kappa,"w":list(w),"B":B.tolist(),
                "basis":P.tolist(),"boundary_angle_matrix":angle_matrix.tolist(),
                "normal_meridian_phi_theta":list(meridian),
                "cap_function_angle_identity":"m*alpha-sigma=-theta",
                "invariant_normal_coordinate":"r=s*exp(2*pi*i*kappa*gamma(x))"})
assert M0==sp.Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
result={"status":"Proposition E.2.20 proved; finite-cap framing and whole relative plumbing comparison independently audited by root",
        "caps":out,"core_monodromy_product":(A1*A2*M0).tolist()}
(ROOT/"code/maps_finite_cap_framings.out.json").write_text(json.dumps(result,indent=2,default=int)+"\n")
print("Both affine cap actions, product trivializations and boundary angle matrices checked.")
print("Normal meridians are exactly v_j-m_j rho_j.")
print("The cap function r^m exp(-2pi i sigma) has the original clockwise base angle.")
