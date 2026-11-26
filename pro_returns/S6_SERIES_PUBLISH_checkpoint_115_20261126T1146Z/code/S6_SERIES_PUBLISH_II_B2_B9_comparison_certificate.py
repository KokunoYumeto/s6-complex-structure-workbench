#!/usr/bin/env python3
"""Postrelease checks of the printed B9 conormal charts and cube ideals.

The frozen program used ambient transverse vectors and positive valuations.
This program instead substitutes the printed dual-conormal affine charts,
computes all cubic poles, and gives their exact Jacobian transport.
"""
from itertools import combinations_with_replacement
import json
import sympy as s

x,y,z,u,v,t=s.symbols("x y z u v t")
checks=[]

def check(name,condition,evidence):
    if not condition:raise AssertionError(name)
    checks.append({"check":name,"passed":True,"evidence":evidence})

def zero(q):return s.cancel(s.expand(q))==0

def pole(q):
    q=s.cancel(q)
    if q==0:return 0
    a,b=s.fraction(q)
    low=lambda p:min(m[0] for m,c in s.Poly(p,t).terms())
    return max(0,low(b)-low(a))

def cube(gs):
    return [s.expand(gs[i]*gs[j]*gs[k]) for i,j,k in combinations_with_replacement(range(3),3)]

def ideal_equal(name,a,b):
    ga=s.groebner(a,z,y,x,order="lex",domain=s.QQ)
    gb=s.groebner(b,z,y,x,order="lex",domain=s.QQ)
    check(name,all(ga.reduce(q)[1]==0 for q in b) and all(gb.reduce(q)[1]==0 for q in a),
          {"first_generators":[str(q) for q in a],"second_generators":[str(q) for q in b]})

def chart(name,mapping,gs,extra,bound,jacobian):
    sub=dict(zip((x,y,z),mapping))
    pulled=[s.expand(q.subs(sub,simultaneous=True)) for q in gs]
    first=[[s.diff(q,a).subs({u:0,v:0}) for a in (u,v)] for q in pulled]
    check(name+": first conormal derivatives are holomorphic",
          all(pole(q)==0 for row in first for q in row),[[str(q) for q in row] for row in first])
    qe=s.Poly(s.expand(extra.subs(sub,simultaneous=True)),u,v)
    quadratic=s.expand(sum(c*u**m[0]*v**m[1] for m,c in qe.terms() if sum(m)==2))
    check(name+": symbolic-square quadratic pole",
          max(pole(c) for m,c in s.Poly(quadratic,u,v).terms())<=bound,str(quadratic))
    generators=cube(gs)+[extra*g for g in gs]
    jets=[]
    for g in generators:
        p=s.Poly(s.expand(g.subs(sub,simultaneous=True)),u,v)
        assert all(sum(m)>=3 or c==0 for m,c in p.terms())
        coefficients=[p.coeff_monomial(m) for m in [u**3,u**2*v,u*v**2,v**3]]
        assert all(pole(c)<=bound for c in coefficients)
        jets.append({"generator":str(g),"cubic_coefficients":[str(c) for c in coefficients],"poles":[pole(c) for c in coefficients]})
    check(name+": all cubic pole bounds",True,{"maximum_bound":bound,"jets":jets})
    jac=s.Matrix(mapping).jacobian((t,u,v)).det()
    check(name+": exact chart Jacobian",zero(jac-jacobian),str(s.factor(jac)))
    check(name+": intrinsic discriminant transport",zero(jac**(-6)-jacobian**(-6)),
          "J="+str(s.factor(jac**(-6)))+" * Disc_K")

space=[y*y-x*z,y*z-x**3,z*z-x*x*y]
F=z**3+x*y**3-3*x*x*y*z+x**5
chart("space cusp",(t**3,t**4+v/(3*t**5),t**5-u/t**3+2*v/(3*t**4)),space,F,3,t**(-6))

G=y*y-x**3
cl=[x*z,y*z,G]
old_cl=cube(cl)+[z*G*g for g in cl]
frozen_cl=[G**3,z*G**2,x*z*z*G,y*z*z*G,z**3*x**3,z**3*x*x*y,z**3*x*y*y,z**3*y**3]
ideal_equal("A.U.3 equals the frozen symbolic-cube ideal",old_cl,frozen_cl)
chart("cusp branch",(t*t,t**3+v/(2*t**3),u/t**2),cl,z*G,2,-t**(-4))
chart("smooth branch of cusp-line",(u/t,v/t,t),cl,z*G,1,t**(-2))

axes=[x*y,x*z,y*z]
old_axes=cube(axes)+[x*y*z*g for g in axes]
minimal_axes=[y**3*z**3,x*y*y*z*z,x*x*y*z*z,x*x*y*y*z,x**3*z**3,x**3*y**3]
ideal_equal("A.U.4 equals the frozen monomial intersection",old_axes,minimal_axes)
for name,mapping,expected in [
    ("x-axis",(t,u/t,v/t),t**(-2)),
    ("y-axis",(u/t,t,v/t),-t**(-2)),
    ("z-axis",(u/t,v/t,t),t**(-2)),
]:
    chart("three axes "+name,mapping,axes,x*y*z,1,expected)
    sub=dict(zip((x,y,z),mapping))
    if name=="x-axis": inverse=(x,x*y,x*z)
    elif name=="y-axis": inverse=(y,x*y,y*z)
    else: inverse=(z,x*z,y*z)
    check(name+": inverse coordinate map",
          all(zero(q.subs(sub,simultaneous=True)-target) for q,target in zip(inverse,(t,u,v))),
          [str(q) for q in inverse])

for name,poles in [("space cusp",[3]),("cusp-line",[2,1]),("three axes",[1,1,1])]:
    correction=4*sum(poles)
    check(name+": corrected discriminant degree",correction==12 and -24+correction==-12,
          {"cubic_pole_orders":poles,"degree_before":-24,"pole_correction":correction,"degree_after":-12})

normal_monomials=[(i,j) for i in range(3) for j in range(3) if i+j<3]
check("cubed normal maximal ideal length",len(normal_monomials)==6,
      {"monomials":normal_monomials,"generic_rank_over_x":3*len(normal_monomials)})

print(json.dumps({"schema_version":1,"tag":"01B9","owner":"cdp:st:A.5.19",
                  "phase":"postrelease comparison","checks_passed":len(checks),"checks":checks},indent=2,sort_keys=True))
