"""Exact local obstruction to a proposed ruled-equality counting shortcut.

The configuration is not a counterexample to the sign/equality theorem.
It shows that k=v need not put every blowup exceptional curve in the
resolved conductor when original vertical components are present.
"""
from pathlib import Path
import json
import sympy as sp

vertices={
    "H":{"square":-1,"conductor":2,"fibre":0},
    "F":{"square":0,"conductor":1,"fibre":1}}
edges={tuple(sorted(("H","F")))}
steps=[]
def blowup(name,centres):
    global edges
    for a in centres:vertices[a]["square"]-=1
    if len(centres)==2:edges.remove(tuple(sorted(centres)))
    vertices[name]={
        "square":-1,
        "conductor":sum(vertices[a]["conductor"] for a in centres)-1,
        "fibre":sum(vertices[a]["fibre"] for a in centres)}
    for a in centres:edges.add(tuple(sorted((name,a))))
    steps.append({"new":name,"centres":centres,
                  "new_data":dict(vertices[name])})

blowup("E",["H","F"])
blowup("G",["F","E"])
blowup("L",["G"])
blowup("P",["L"])
names=["F","E","G","L","P"]
M=sp.Matrix([[vertices[a]["square"] if a==b else
              int(tuple(sorted((a,b))) in edges)
              for b in names] for a in names])
mult=sp.Matrix([vertices[a]["fibre"] for a in names])
assert M*mult==sp.zeros(5,1)
A=M[:4,:4]
assert A.det()==4
assert all((-1)**j*A[:j,:j].det()>0 for j in range(1,5))
assert [vertices[a]["conductor"] for a in names]==[1,2,2,1,0]

x,y,z,u,epsilon=sp.symbols("x y z u epsilon")
g=x*x+y**3*z*z+y**5
normal=u*u+y*z*z+y**3
assert sp.expand(g.subs(x,y*u)-y*y*normal)==0
assert [sp.diff(normal,a).subs({u:0,y:0,z:0}) for a in (u,y,z)]==[0,0,0]
g_eps=g+epsilon*y**3
crosscap_coordinate=z*z+y*y+epsilon
assert sp.expand(g_eps-(x*x+y**3*crosscap_coordinate))==0

result={
 "status":"A local configuration, not a global counterexample",
 "steps":steps,"vertices":vertices,"edges":sorted(edges),
 "fibre_matrix":[list(map(int,M.row(i))) for i in range(5)],
 "fibre_multiplicities":list(map(int,mult)),
 "exceptional_A_matrix":[list(map(int,A.row(i))) for i in range(4)],
 "A_determinant":int(A.det()),"k":4,"v":4,
 "created_curves_in_A":3,"original_vertical_curves_in_A":1,
 "normalization":"u^2+y*z^2+y^3=0; x=y*u",
 "conductor":"y*B; its divisorial order along H=(u=y=0) is 2",
 "deformation":"x^2+y^3*(z^2+y^2+epsilon)",
 "all_checks_passed":True}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
print("Ruled-equality shortcut warning: exact configuration verified.")
print("k=v=4, but only 3 created exceptional curves belong to A.")
print("The remaining created curve P has conductor coefficient 0.")
print("A is negative definite D4, determinant",A.det())
print("Fibre multiplicities:",list(mult))
print("The complete fibre matrix kills that multiplicity vector.")
print("Finite normalization substitution x=y*u: exact identity verified.")
print("The epsilon deformation has local x^2+y^3*Z germs at z^2=-epsilon.")
