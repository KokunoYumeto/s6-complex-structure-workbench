"""Exact elementary certificates for E.2.9; geometric bordism is proved in TeX."""
from fractions import Fraction
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

R=s.Matrix([[3,0,0,0,-1,0], [0,4,0,0,1,0],
            [0,0,3,0,0,-1], [0,0,0,4,0,1],
            [1,1,1,1,0,0]])
D=smith_normal_form(R,domain=s.ZZ)
diag=[abs(int(D[i,i])) for i in range(5)]
generator=s.Matrix([4,-3,-4,3,12,-12])
assert diag==[1]*5 and R*generator==s.zeros(5,1)
chi=2-2*(1-Fraction(1,3))-2*(1-Fraction(1,4))
assert chi==-Fraction(5,6)
# The stable groups and eta^3=12nu are primary theorem inputs, not
# computed by this elementary script. Both arithmetic consequences agree.
nu_squared_order=2
product_coefficient=(12*12)%nu_squared_order
assert product_coefficient==0
record={
 'abelian_relation_matrix':R.tolist(), 'smith_diagonal':diag,
 'primitive_abelian_character':list(generator),
 'orbifold_euler_characteristic':str(chi),
 'aspherical_target_integral_betti':[1,1,0,1,1],
 'stable_external_product_components':['0','0','0','eta^6=eta^2*eta^4=0'],
 'independent_arithmetic_reduction':'(12nu)^2=144nu^2=0 since pi6S has order2',
 'last_coefficient_mod_order':product_coefficient,
 'scope':'The proof that the transverse inverse image bounds over BG is geometric; no diffeomorphism classification is inferred.'
}
out=Path(__file__).resolve().parents[1]/'records/shifted_group_bordism.json'
out.write_text(json.dumps(record,indent=2,default=int)+'\n')
print(json.dumps(record,indent=2,default=int))
