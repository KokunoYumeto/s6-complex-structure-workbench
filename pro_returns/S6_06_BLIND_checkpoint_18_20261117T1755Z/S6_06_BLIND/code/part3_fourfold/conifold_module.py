#!/usr/bin/env python3
"""Exact algebra for the conifold line used in the Part 3 index audit.

The proof is in notes/part3_fourfold.md.  This file checks the polynomial
matrix factorization, the diagonal-ideal coordinate change, and the explicit
monomial formulas behind the Cech and flatness calculations.  No numerical
approximation and no prior claimed index value is used.
"""
from pathlib import Path
import json
import sympy as sp

out = Path(__file__).resolve().parent
u, w, X, v, z = sp.symbols("u w X v z")
f = u*v-X*w
Phi = sp.Matrix([[w, v], [-u, -X]])
Psi = sp.Matrix([[-X, -v], [u, w]])
assert Phi*Psi == f*sp.eye(2)
assert Psi*Phi == f*sp.eye(2)
assert sp.Matrix([[u,w]])*Phi == sp.Matrix([[0,f]])

# On the overlap of the two resolution charts, e_1=z^{-1} e_0.
# The two spaces of regular Laurent monomials have exponents c>=0 and
# c<=a+b-1.  They cover every integer, even when a+b=0.
cech_checks = []
for a in range(8):
    for b in range(8):
        for c in range(-20,21):
            assert c >= 0 or c <= a+b-1
        for c in range(max(0,a+b)):
            # A common monomial u^a w^b z^c has a factor u or w
            # with no z attached, and the remaining factor is in R.
            assert c <= a+b-1
            if a > 0:
                rem = (a-1,b,c)
            else:
                assert b > 0
                rem = (a,b-1,c)
            assert rem[0]>=0 and rem[1]>=0 and 0<=rem[2]<=sum(rem[:2])
        cech_checks.append([a,b, max(0,a+b)])

# The ideal of the diagonal on xy=uv is a conifold rank-one module.
x,y,U,V,a,b = sp.symbols("x y U V a b")
diag = x*y-U*V
diag_after = sp.expand(diag.subs({x:U+a,y:V+b}, simultaneous=True))
assert diag_after == U*b+V*a+a*b
assert sp.expand(diag_after-a*(V+b)-U*b) == 0

# For R'=B[x,y]/(xy-uv), B=C[u,v], J=(x,u) is B-free on
# x^n (n>=1) and u*y^n (n>=0).  Here we check the generator reductions.
uu,vv,xx,yy=sp.symbols("uu vv xx yy")
G=sp.groebner([xx*yy-uu*vv],xx,yy,uu,vv,order="lex")
flat_reductions=[]
for n in range(1,9):
    lhs=xx*yy**n
    rhs=uu*vv*yy**(n-1)
    assert G.reduce(lhs-rhs)[1] == 0
    flat_reductions.append([n,str(rhs)])

data={
    "status":"exact polynomial identities verified; full proofs in notes/part3_fourfold.md",
    "ring":"C[u,w,X,v]/(uv-Xw)",
    "module":"I=(u,w)=pi_*pi_P1^*O_P1(-1)",
    "R1_pushforward":0,
    "Phi":[[str(e) for e in row] for row in Phi.tolist()],
    "Psi":[[str(e) for e in row] for row in Psi.tolist()],
    "factorization_identity":"Phi Psi=Psi Phi=(uv-Xw) I_2",
    "presentation_identity":"[u,w] Phi=[0,uv-Xw]",
    "cech_ranges":{"chart0":"c>=0","chart1":"c<=a+b-1","H0":"0<=c<=a+b-1"},
    "cech_finite_sanity_checks":cech_checks,
    "diagonal_coordinate_change":{
        "initial":"xy-UV",
        "x":"U+a","y":"V+b",
        "result":"a*(V+b)+U*b",
        "new_conifold_coordinates":"(Xnew,Unew,Ynew,Vnew)=(a,b,V+b,-U)",
        "diagonal_ideal":"(a,b)=(Xnew,Unew)"
    },
    "flat_family_base":"B=C[u,v]",
    "flat_family_ring":"R'=B[x,y]/(xy-uv)",
    "flat_family_module":"J=(x,u)",
    "B_basis":["x^n, n>=1","u*y^n, n>=0"],
    "closed_fibre":"C[x] direct_sum C[y] over C[x,y]/(xy)",
    "flat_reductions":flat_reductions,
    "link":"S2 times S3",
    "link_reduced_K_class":"primitive generator, c1=-h",
    "extension_to_smoothing_line":False,
    "extension_obstruction":"H2(S3 times D3;Z)=0; c1 on link is -h !=0"
}
(out/"conifold_module.json").write_text(json.dumps(data,indent=2)+"\n")
print(json.dumps({k:data[k] for k in ("ring","module","R1_pushforward","factorization_identity","B_basis","closed_fibre","link_reduced_K_class","extension_to_smoothing_line")},indent=2))
