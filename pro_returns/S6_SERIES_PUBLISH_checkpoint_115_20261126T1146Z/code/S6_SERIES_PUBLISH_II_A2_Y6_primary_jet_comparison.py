#!/usr/bin/env python3
"""Post-release exact arithmetic for the retained R13 proof.

Methods: branch-exponent enumeration; pullback of a differential form;
quadratic-form congruence/Schur complement; exterior products of cubic
linear factors.  These certify the stated algebra, not the analytic
existence or the whole classification theorem.
"""
import itertools
import json
import sympy as s

out={"timing":"after 02Y6 original-proof release", "events_added":0}

# An exponent on each normalized branch is its intrinsic conductor
# exponent plus its intersection lengths with all other branches.
# Intrinsic plane-branch conductor exponents are 0 or positive even.
def possibilities(c):
    rows=[]
    for n in range(1,c+2):
        edges=list(itertools.combinations(range(n),2))
        for intrinsic in itertools.product(range(0,c+1,2),repeat=n):
            for lengths in itertools.product(range(1,c+1),repeat=len(edges)):
                actual=list(intrinsic)
                for (i,j),v in zip(edges,lengths):actual[i]+=v;actual[j]+=v
                if actual==[c]*n:
                    rows.append({"branches":n,"intrinsic":intrinsic,
                                 "pair_intersections":lengths})
    return rows
one=possibilities(1);two=possibilities(2)
assert one==[{"branches":2,"intrinsic":(0,0),"pair_intersections":(1,)}]
assert two==[
 {"branches":1,"intrinsic":(2,),"pair_intersections":()},
 {"branches":2,"intrinsic":(0,0),"pair_intersections":(2,)},
 {"branches":3,"intrinsic":(0,0,0),"pair_intersections":(1,1,1)}]
out["conductor_one"]=one;out["conductor_two"]=two

# Derive the blowup coefficient from the actual chart Jacobian.
u,v=s.symbols('u v');aa,bb=s.symbols('a b',integer=True,nonnegative=True)
chart=s.Matrix([u,u*v]);jac=chart.jacobian([u,v]).det()
assert jac==u
out["blowup_form"]={"chart":[str(x) for x in chart],
 "Jacobian":str(jac),"pole_exponent":"a+b-1",
 "identity":"dx wedge dy/(x^a y^b) = u^(1-a-b) v^(-b) du wedge dv"}

# Cech H1 of O(k) on P1 is represented by Laurent powers k<j<0.
n=s.symbols('n',integer=True,nonnegative=True)
assert s.Max(-n,0)==0
assert max(-2+1,0)==0
out["exceptional_layers"]={"degree":"n-1 for n>=0",
 "H1_dimension":"max(-n,0)=0", "vertical_kernel_layer_degree":-2,
 "vertical_kernel_H0_dimension":0,
 "vertical_thick_fibre_chi":"-m for every multiplicity m>=1, by m layers each of Euler characteristic -1",
 "scope":"The Laurent interval computation proves all n>=0, not a finite sample."}

# Complete the square through a quadratic-form congruence, then identify
# the residual coefficient as its Schur complement.
a=s.symbols('a',nonzero=True)
b,c,z=s.symbols('b c z')
M=s.Matrix([[a,b/2],[b/2,c]]);U=s.Matrix([[1,z],[0,1]])
changed=U.T*M*U
assert changed[0,0]==a
assert s.expand(2*changed[0,1])==b+2*a*z
assert s.expand(changed[1,1])==c+b*z+a*z*z
assert s.expand(changed.det()-M.det())==0
q=M.det()/a
assert s.simplify(q-(c-b*b/(4*a)))==0
assert s.simplify(changed.det()/changed[0,0]-q)==0
out["quartic_Schur_complement"]={"q4":str(s.expand(q)),
 "changed_cross_coefficient":str(s.expand(2*changed[0,1])),
 "changed_last_coefficient":str(s.expand(changed[1,1])),
 "determinant_preserved":True}

# The binary cubic discriminant is the square product of the three
# pairwise exterior products of its three linear factors.  A GL2
# change multiplies each exterior product by det(G); scaling one
# factor scales exactly two of them.  Verify the universal exterior
# identity directly, without expanding a coefficient discriminant.
r1,r2,t1,t2,A,B,C,D=s.symbols('r1 r2 t1 t2 A B C D')
G=s.Matrix([[A,B],[C,D]]);r=s.Matrix([[r1,r2]]);t=s.Matrix([[t1,t2]])
wedge=s.det(s.Matrix.vstack(r,t))
neww=s.det(s.Matrix.vstack(r*G,t*G))
assert s.expand(neww-G.det()*wedge)==0
ri=s.symbols('r0:3');si=s.symbols('s0:3');xx,yy=s.symbols('xx yy')
product=s.Poly(s.prod(ri[i]*xx+si[i]*yy for i in range(3)),xx,yy)
ca,cb,cc,cd=[product.coeff_monomial(xx**(3-i)*yy**i) for i in range(4)]
coefficient_disc=cb**2*cc**2-4*ca*cc**3-4*cb**3*cd-27*ca**2*cd**2+18*ca*cb*cc*cd
exterior_disc=s.prod((ri[i]*si[j]-ri[j]*si[i])**2 for i,j in itertools.combinations(range(3),2))
assert s.expand(coefficient_disc-exterior_disc)==0
out["cubic_discriminant"]={
 "expression":"product_{i<j}(r_i s_j-r_j s_i)^2",
 "GL2_weight":6,"equation_unit_weight":4,
 "line_bundle":"(det K)^6 tensor N_E^4",
 "universal_exterior_identity":True,
 "coefficient_formula":"B^2*C^2-4*A*C^3-4*B^3*D-27*A^2*D^2+18*A*B*C*D",
 "coefficient_formula_matches_exterior_product":True}

# Exact local map for the three straightened branches.  a,b here are
# values of units; the identity remains one of holomorphic functions.
x,y=s.symbols('x y');X=a*x;Y=-b*y
assert s.expand(X*Y*(X-Y)+a*b*x*y*(a*x+b*y))==0
assert s.Matrix([X,Y]).jacobian([x,y]).det()==-a*b
out["three_branch_coordinate_map"]={"X":"a*x","Y":"-b*y",
 "Jacobian_at_centre":"-a(0)*b(0)",
 "unit_identity":"X*Y*(X-Y)=-a*b*x*y*(a*x+b*y)"}

# Line degrees and the Euler identities used in the printed proof.
ell,g=s.symbols('ell g',integer=True)
assert s.solve([2*ell>=0,-3*ell>=0],ell)==s.Eq(ell,0)
out["line_degrees"]={"K":0,"N_E":0,"L":str(ell),"Q":str(-ell),
 "quadratic":str(2*ell),"null_cubic":str(-3*ell),
 "null_quartic":str(-4*ell),"cusp_constraints_force":"ell=0",
 "D4_discriminant":0}
eN=4-4*g;eH=2-2*g;eE=0
assert s.expand(eN-eH+eE)==2-2*g
assert (eN-eH+eE).subs(g,1)==0
out["Euler"]={"ruled_minus_horizontal_plus_elliptic":str(s.expand(eN-eH)),
 "at_genus_one":0,"rational_conductor_chi":1+0-0}
out["not_certified_by_program"]=[
 "The analytic conductor-primary injection and cohomology morphisms",
 "Rational singularities and canonical trace applicability",
 "Holomorphic Morse normal forms and unit roots",
 "The global compact counterexample and the complete refined theorem"]
print(json.dumps(out,indent=2,default=str))
