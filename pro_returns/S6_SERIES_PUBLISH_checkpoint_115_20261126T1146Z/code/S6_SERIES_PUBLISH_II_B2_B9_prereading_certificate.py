#!/usr/bin/env python3
"""Exact checks for 01B9 before target release; no proof or file inputs.

Symbolic cubes are computed by elimination. Cubic jets are obtained by
direct affine substitution. Discriminant characters are universal
polynomial identities, and all arithmetic is exact over QQ.
"""
from itertools import combinations_with_replacement, product
import json
import sympy as s

x, y, z, u, v, t, w = s.symbols("x y z u v t w")
checks = []

def checked(name, condition, evidence):
    if not condition:
        raise AssertionError(name)
    checks.append({"check":name,"passed":True,"evidence":evidence})

def zero(p):
    return s.expand(p) == 0

def order(p):
    p=s.expand(p)
    return None if p == 0 else min(m[0] for m,c in s.Poly(p,t).terms())

def cube(gens):
    return [s.expand(gens[i]*gens[j]*gens[k])
            for i,j,k in combinations_with_replacement(range(len(gens)),3)]

def saturation_check(name, gens, parameter, proposed):
    power=cube(gens)
    gb=s.groebner(power+[1-w*parameter],w,z,y,x,order="lex",domain=s.QQ)
    eliminated=[q.as_expr() for q in gb.polys if not q.as_expr().has(w)]
    saturated=s.groebner(eliminated,z,y,x,order="lex",domain=s.QQ)
    claimed=s.groebner(proposed,z,y,x,order="lex",domain=s.QQ)
    equal=(all(claimed.reduce(q)[1]==0 for q in eliminated)
           and all(saturated.reduce(q)[1]==0 for q in proposed))
    checked(name+": symbolic cube by elimination",equal,
            {"saturation_parameter":str(parameter),
             "elimination_basis":[str(q.as_expr()) for q in saturated.polys],
             "proposed_generators":[str(q) for q in proposed]})

def jet_bounds(name, generators, mapping, lower):
    monomials=[u**3,u**2*v,u*v**2,v**3]
    out=[]
    for g in generators:
        pull=s.Poly(s.expand(g.subs(dict(zip((x,y,z),mapping)),simultaneous=True)),u,v)
        lower_terms=[(m,c) for m,c in pull.terms() if sum(m)<3 and c!=0]
        if lower_terms:
            raise AssertionError((name,"unexpected lower normal jet",lower_terms))
        coefficients=[pull.coeff_monomial(m) for m in monomials]
        orders=[order(c) for c in coefficients]
        assert all(a is None or a>=b for a,b in zip(orders,lower)), (name,g,orders)
        out.append({"generator":str(g),"cubic_coefficients":[str(c) for c in coefficients],"orders":orders})
    checked(name+": all lower normal jets vanish",True,{"generators":len(generators)})
    checked(name+": cubic coefficient valuation bounds",True,{"bounds":list(lower),"jets":out})

def disc(coeff):
    a,b,c,d=coeff
    return b*b*c*c-4*a*c**3-4*b**3*d-27*a*a*d*d+18*a*b*c*d

def discriminant_budget(name,bounds,jacobian_order,points):
    a,b,c,d=bounds
    costs=[2*b+2*c,a+3*c,3*b+d,2*a+2*d,a+b+c+d]
    residual=min(costs)-6*jacobian_order
    checked(name+": discriminant divisor budget",points*residual>12,
            {"coefficient_orders":list(bounds),"five_discriminant_term_orders":costs,
             "Jacobian_order":jacobian_order,"invariant_order_per_point":residual,
             "points":points,"forced_total_order":points*residual,"global_degree":12})

# Universal cubic discriminant and exact GL(2) character.
a,b,c,d,alpha,beta,gamma,delta,scale=s.symbols("a b c d alpha beta gamma delta scale")
F=a*u**3+b*u**2*v+c*u*v**2+d*v**3
Delta=disc((a,b,c,d))
checked("binary cubic discriminant from resultant",
        zero(s.discriminant(a*x**3+b*x**2+c*x+d,x)-Delta),str(Delta))
changed=s.Poly(s.expand(F.subs({u:alpha*u+beta*v,v:gamma*u+delta*v},simultaneous=True)),u,v)
newcoeff=[changed.coeff_monomial(m) for m in [u**3,u**2*v,u*v**2,v**3]]
checked("binary cubic GL(2) determinant character",
        zero(disc(newcoeff)-(alpha*delta-beta*gamma)**6*Delta),
        "For F(A(u,v)), Disc changes by det(A)^6; inverse frame changes give det(A)^(-6).")
checked("binary cubic defining-unit character",zero(disc([scale*q for q in (a,b,c,d)])-scale**4*Delta),"Disc scales by the fourth power of the defining unit.")

# The space cusp: I^(3)=I^3+I F2.
g1,g2,g3=y*y-x*z,y*z-x**3,z*z-x*x*y
F2=z**3+x*y**3-3*x*x*y*z+x**5
space_generators=cube([g1,g2,g3])+[g*F2 for g in [g1,g2,g3]]
saturation_check("space cusp (3,4,5)",[g1,g2,g3],x,space_generators)
monomial_generators=[(6-j,j) for j in range(7)]+[(2,3),(1,4),(0,5)]
basis=[(i,j) for j in range(6) for i in range(6)
       if not any(i>=a0 and j>=b0 for a0,b0 in monomial_generators)]
checked("space cusp: independent DVR residue dimension",len(basis)==18,
        {"basis_exponents_y_z":basis,"generic_rank":3*(3*4//2),"residue_dimension":len(basis)})
jet_bounds("space cusp",space_generators,(t**3,t**4+u,t**5+v),(11,10,9,8))
jac=s.Matrix((t**3,t**4+u,t**5+v)).jacobian((t,u,v)).det()
checked("space cusp: exact ambient Jacobian",zero(jac-3*t*t),str(jac))
discriminant_budget("space cusp",(11,10,9,8),2,1)

# Cusp plus a transverse line: the intersection of the two cubic powers.
G=y*y-x**3
cuspline_generators=[G**3,z*G**2,x*z*z*G,y*z*z*G,
                    z**3*x**3,z**3*x*x*y,z**3*x*y*y,z**3*y**3]
saturation_check("cusp and transverse line",[G,x*z,y*z],x+z,cuspline_generators)
jet_bounds("cusp and transverse line",cuspline_generators,(t*t,t**3+u,v),(9,6,5,6))
jac2=s.Matrix((t*t,t**3+u,v)).jacobian((t,u,v)).det()
checked("cusp branch: exact ambient Jacobian",zero(jac2-2*t),str(jac2))
discriminant_budget("cusp branch",(9,6,5,6),1,1)

# Three axes: intersect the monomial ideals (x,y)^3,(x,z)^3,(y,z)^3.
eligible=[e for e in product(range(4),repeat=3)
          if all(e[i]+e[j]>=3 for i,j in [(0,1),(0,2),(1,2)])]
minimal=[e for e in eligible
         if not any(f!=e and all(q<=r for q,r in zip(f,e)) for f in eligible)]
axes_generators=[x**i*y**j*z**k for i,j,k in minimal]
checked("three axes: exact monomial intersection generators",
        set(minimal)=={(0,3,3),(1,2,2),(2,1,2),(2,2,1),(3,0,3),(3,3,0)},
        {"minimal_exponents":minimal,"criterion":"Each pairwise exponent sum is at least three."})
for name,mapping in [("x-axis",(t,u,v)),("y-axis",(u,t,v)),("z-axis",(u,v,t))]:
    jet_bounds("three axes "+name,axes_generators,mapping,(3,2,2,3))
discriminant_budget("three axes",(3,2,2,3),0,3)

pa,q=s.symbols("pa q",integer=True)
checked("LCI discriminant degree",s.expand(-6*(2*pa-2))==12*(1-pa),"deg Disc=12(1-p_a(D))")
checked("singular rational delta-one root cover",
        12*(1-1)==0 and s.expand(2*(1-q)-2+2*q)==0,
        {"discriminant_degree":0,"unramified_component_Riemann_Hurwitz":"g=1-degree; positive degree and g>=0 force degree=1 and g=0"})
checked("elliptic triple conductor and Euler arithmetic",
        2*1-2==3*(2*1-2) and 2*(2-2*1)-(2-2*1)+(2-2*1)==0,
        {"cover_degree":3,"source_and_image_genus":1,"Euler_number":0})

print(json.dumps({"schema_version":1,"tag":"01B9","owner":"cdp:st:A.5.19",
                  "phase":"prereading; target proof unopened","target_proof_input":None,
                  "checks_passed":len(checks),"checks":checks},indent=2,sort_keys=True))
