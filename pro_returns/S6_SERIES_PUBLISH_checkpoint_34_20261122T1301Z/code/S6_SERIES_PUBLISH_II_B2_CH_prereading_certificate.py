#!/usr/bin/env python3
"""Exact algebra and finite cubic multiplicity checks for 01CH. No file inputs."""
import itertools
import json
import sympy as s

checks = []


def check(name, condition, evidence):
    ok = bool(condition)
    checks.append({"name": name, "passed": ok, "evidence": evidence})
    if not ok:
        raise AssertionError(name)


def zero(expr):
    return s.cancel(expr) == 0


x, y, t, z, X, U, V, W, J, a, b, c = s.symbols("x y t z X U V W J a b c")
phi = a + b*y + c*t + y*t
F1 = x-y*phi
G = U*y**2 + V*y*F1 + W*F1**2
F = s.expand(F1*G)
P = (z-phi)*(U+V*(z-phi)+W*(z-phi)**2)
check("ambient coordinate forward inverse", zero(F1.subs(x, X+y*phi)-X), "X=x-y*phi; x=X+y*phi")
check("ambient coordinate inverse forward", zero((X+y*phi).subs(X, F1)-x), "Same analytic triangular coordinate map")
check("ambient coordinate Jacobian", s.det(s.Matrix([F1,y,t]).jacobian([x,y,t])) == 1, "Jacobian identically one")
check("cubic strict transform", zero(F.subs(x,y*z)-y**3*P), "F(yz,y,t)=y^3 P(z,y,t)")
check("strict transform root", zero(P.subs(z,phi)), "z=phi(y,t)")
check("simple root derivative", zero(s.diff(P,z).subs(z,phi)-U), "P_z at the root equals the inverted unit U")
check("factor residue", zero(G.subs(x,y*phi)-U*y**2), "G on F1 equals U*y^2")
check("derivative residue", zero(s.diff(F,x).subs(x,y*phi)-U*y**2), "F_x on F1 equals G on F1")
gb1 = s.groebner([X,U*y**2,U*J-1],X,y,U,J,order="lex")
gb2 = s.groebner([X,y**2,U*J-1],X,y,U,J,order="lex")
check("conductor ideal exact equality", gb1 == gb2, {"first":list(map(str,gb1.polys)),"second":list(map(str,gb2.polys))})
check("conductor ideal inverse multiplier", zero(J*(U*y**2)-y**2-(U*J-1)*y**2), "J is the explicit inverse of U in the localized ring")

partitions = [(1,1,1),(2,1),(3,)]
allocation_rows = []
for part in partitions:
    polynomial = s.prod((z-i)**m for i,m in enumerate(part))
    gcd = s.gcd(polynomial,s.diff(polynomial,z))
    check("cubic multiplicity partition "+str(part), s.degree(polynomial,z)==3 and s.degree(s.sqf_part(gcd,z),z)<=1,
          {"cubic":str(polynomial),"derivative_gcd":str(gcd)})
    for d in [2,3]:
        allocations = [aa for aa in itertools.product(*(range(m+1) for m in part)) if sum(aa)==d]
        row = []
        for aa in allocations:
            # A locally unibranch R_d contributes one normalization point at
            # each occupied root, regardless of its ramification multiplicity.
            attachments = sum(1 for m,k in zip(part,aa) if m>=2 and k>0)
            row.append({"component_multiplicities":aa,"possible_attachment_points":attachments})
        check("all degree-"+str(d)+" allocations for "+str(part), all(r["possible_attachment_points"]<=1 for r in row), row)
        allocation_rows.append({"total":part,"degree":d,"allocations":row})

u,v,tau = s.symbols("u v tau")
for k in [1,2]:
    check("A"+str(2*k)+" parametrization", zero((v**2-u**(2*k+1)).subs({u:tau**2,v:tau**(2*k+1)})), "u=tau^2, v=tau^(2k+1)")
    check("A"+str(2*k)+" field inverse", zero((v/u**k).subs({u:tau**2,v:tau**(2*k+1)})-tau), "tau=v/u^k")
    check("A"+str(2*k)+" integral equation", zero((tau**2-u).subs(u,tau**2)), "tau is integral over the cusp ring")

r,N0,zexc,rd,K,d,n,beta,cc = s.symbols("r N0 zexc rd K d n beta cc",integer=True)
eS = 2-r+N0+(n+1-beta)
check("ruled complement Euler", 4-(2+2*r-r)==2-r, "Euler of section plus r fibres is 2+r")
check("survivor count identity", zero((r-zexc-rd)-(r-N0-rd)-(N0-zexc)), "K-(r-N0-rdom)=N0-z")
check("surface lower gap identity", zero(((2-r+N0+K)-(d-1)-(N0-zexc)-(3-d-rd)).subs(K,r-zexc-rd)), "e_lower-(d-1)=(N0-z)+(3-d-rdom)")
check("graph Euler gap", zero((n+1-beta)-K-((n-cc-1)+(cc+beta-K)+2*(1-beta))), "eGamma-K=(n-c-1)+(c+beta-K)+2(1-beta)")

degree_rows = []
for degree in [2,3]:
    rows = []
    for n0 in range(6):
        for ex in range(n0+1):
            for dom in range(4-degree):
                for keep in range(7):
                    rr=ex+dom+keep
                    lower=2-rr+n0+keep
                    rows.append((n0,ex,dom,keep,lower))
    check("finite Euler count grid degree "+str(degree), all(row[-1]>=degree-1 for row in rows),
          {"N0_range":[0,5],"K_range":[0,6],"rows":len(rows),"minimum":min(row[-1] for row in rows)})
    degree_rows.append({"degree":degree,"rows":len(rows)})
for bta in [0,1]:
    rows=[]
    for nn in range(1,8):
        for comps in range(nn):
            for keep in range(comps+bta+1):
                rows.append((nn,comps,keep,nn+1-bta-keep))
    check("finite graph count grid beta "+str(bta),all(row[-1]>=0 for row in rows),
          {"n_range":[1,7],"rows":len(rows),"minimum_gap":min(row[-1] for row in rows)})

print(json.dumps({"tag":"01CH","method":"Polynomial identities, localized-ideal Groebner equality, exhaustive cubic multiplicity allocations, cusp normalization maps, and exact Euler gap decomposition","checks":checks,"exact_checks":len(checks),"all_passed":all(c["passed"] for c in checks),"scope":"Finite Euler grids support the separately proved universal symbolic gap identities; no geometric statement is inferred solely from a finite grid."},indent=2))
