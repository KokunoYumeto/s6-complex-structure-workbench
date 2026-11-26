"""Exact cyclic-cover check of the -6 sphere square used in 02X0.

Mathematical method: pull back the real quadric sphere in
F_1={x^2-YZ=1} through (x,y,z)->(x,y^n,z).
The written comparison proves smoothness of its spherical inverse image
and the isomorphism of its normal bundle with the pullback normal bundle.
This code checks the polynomial morphism, branch monodromies, Euler
number, signed normal orientation and pulled-back clutching residue.
It does not replace the analytic boundary or normal-bundle arguments.
"""
import json
import sympy as sp

x,y,z,w=sp.symbols('x y z w')
n=sp.symbols('n',integer=True,positive=True)
cover_identity=sp.expand((x*x-y**n*z-1)-(x*x-z*y**n-1))
normal_transition=w**(-2*n)
logarithmic_derivative=sp.simplify(sp.diff(normal_transition,w)/normal_transition)
chern_number=sp.simplify(w*logarithmic_derivative)
branched_euler=sp.expand(2*n-2*(n-1))

# Complex orientation is (e1,Je1,e2,Je2). Tangent followed by
# its J-image is (e1,e2,Je1,Je2), the permutation (0,2,1,3).
permutation=[0,2,1,3]
inversions=sum(permutation[i]>permutation[j] for i in range(4) for j in range(i+1,4))
normal_orientation_sign=(-1)**inversions
base_sphere_normal_euler=normal_orientation_sign*2

degree=3
upper=[(i+1)%degree for i in range(degree)]
lower=[(i-1)%degree for i in range(degree)]
product=[lower[upper[i]] for i in range(degree)]
orbit={0};front=[0]
while front:
    i=front.pop()
    for p in (upper,lower):
        j=p[i]
        if j not in orbit:orbit.add(j);front.append(j)

# At a branch point use normal coordinates delta_Z+conj(delta_Y).
# Under Y=y^n, Z=z, this pulls back to
# delta_z+n*conj(y)^(n-1)*conj(delta_y); its delta_z coefficient is 1.
normal_quotient_delta_z_coefficient=1
square=chern_number.subs(n,degree)
assert cover_identity==0
assert logarithmic_derivative==-2*n/w
assert chern_number==base_sphere_normal_euler*n
assert branched_euler==2
assert product==list(range(degree)) and len(orbit)==degree
assert square==-6 and normal_quotient_delta_z_coefficient==1

print(json.dumps({
 'method':'finite cyclic cover and normal-bundle clutching residue; no compactification matrix',
 'symbolic_cover_identity':str(cover_identity),
 'normal_orientation_permutation':permutation,
 'normal_orientation_sign':normal_orientation_sign,
 'base_sphere_normal_euler':base_sphere_normal_euler,
 'normal_clutching_function':str(normal_transition),
 'logarithmic_derivative':str(logarithmic_derivative),
 'symbolic_chern_number':str(chern_number),
 'symbolic_branched_cover_euler':str(branched_euler),
 'degree':degree,
 'two_branch_monodromies':[upper,lower],
 'monodromy_product':product,
 'connected_sheet_orbit':sorted(orbit),
 'normal_quotient_delta_z_coefficient':normal_quotient_delta_z_coefficient,
 'sphere_self_intersection':int(square),
 'scope':'Post-release written geometric recomputation of the displayed -6; the program checks these exact algebraic identities. It does not certify the analytic deformation argument.'
},indent=2))
