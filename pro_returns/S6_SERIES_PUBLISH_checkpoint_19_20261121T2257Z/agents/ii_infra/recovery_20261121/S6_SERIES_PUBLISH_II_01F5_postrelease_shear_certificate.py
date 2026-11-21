#!/usr/bin/env python3
"""Postrelease exact full-cohomology action, retaining every central shear."""
from pathlib import Path
import contextlib,io,runpy,json
with contextlib.redirect_stdout(io.StringIO()):
    n=runpy.run_path(str(Path(__file__).with_name("S6_SERIES_PUBLISH_II_01F5_form_certificate.py")))
S=n["S"];plus=n["plus"];scale=n["scale"];wedge=n["wedge"];eq=n["eq"];t=n["theta"]
r,p,z,q,m=S.symbols("r p z q m", nonzero=True)
pull=[t[0],t[1],plus(t[2],scale(r,t[0]),scale(p,t[1])),
      plus(t[3],scale(-2*z/m,t[0]),scale(-2*q/m,t[1]))]
basis=[(0,2),(1,2),(0,3),(1,3)]
expected=[p,-r,-2*q/m,2*z/m]
rows=[]
for (a,b),co in zip(basis,expected):
    old=wedge(t[a],t[b]);new=wedge(pull[a],pull[b])
    assert eq(new,plus(old,scale(co,wedge(t[0],t[1]))))
    rows.append({"basis":f"theta{a+1}{b+1}","added_exact_theta12_coefficient":str(co),
                 "explicit_primitive_coefficient_times_theta4":str(-co/2)})
print(json.dumps({
 "timing":"Postrelease comparison; no additional prereading or independent event.",
 "source_map":"Borcea (15), M=I,k=0,e=1,V=-(2/m)X4. X1->X1+rX3+zV, X2->X2+pX3+qV; X3,V fixed.",
 "actual_dual_pullbacks":[str(x) for x in pull],
 "basis_image_differences":rows,
 "exactness":"d(theta4)=-2 theta12, so every displayed difference is the derivative of its listed multiple of theta4.",
 "actual_H2_real_and_complex_matrix":"I4",
 "integral_free_lattice_action":"Identity: the free integral lattice injects into real cohomology.",
 "torsion_action_needed_for_F5":False,
 "projective_scalar_not_assumed":True,
 "old_target_computational_routine":"The released target uses a written group/shear proof; it cites no computer routine for this step.",
 "all_assertions_passed":True,"events_added":0
},indent=2))
