"""Exact affine obstruction to the ordinary-locus scalar-shear claim.

The induced homomorphisms on Lambda semidirect F2 differ by the two
affine defects.  Quotienting by the invariant delta direction permits
every circle-gauge correction and retains an obstruction of exact order6.
"""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
d1=s.Matrix([0,1,-1,-1]);d2=s.Matrix([0,0,-1,1])
E=s.zeros(4);E[3,0]=1;S=s.eye(4)-2*E
assert S*d1==d1 and S*d2==d2
D=s.Matrix.vstack(A1-s.eye(4),A2-s.eye(4))
d=s.Matrix.vstack(d1,d2)
rows=[0,1,2,4,5,6]
Dbar=D[rows,:3];dbar=d[rows,:]
solution=Dbar.gauss_jordan_solve(dbar)[0]
assert solution==s.Matrix([s.Rational(1,6),0,0])
assert Dbar*s.Matrix([1,0,0])==6*dbar
assert all((r*solution)[0].q!=1 for r in range(1,6))
smith=smith_normal_form(Dbar,domain=ZZ)
assert sorted(abs(smith[i,i]) for i in range(3))==[1,1,6]

# For a shear -h*theta with theta a globally defined gamma coordinate,
# base windings n1,n2 would have to be 1/3,-1/4 after the quotient step.
h,n1,n2=s.symbols('h n1 n2',nonzero=True)
lam=s.Matrix([h/12,0,0,0])
delta=s.Matrix([0,0,0,1])
res1=s.expand((h*d1/2+h*n1*delta-(A1-s.eye(4))*lam)[3])
res2=s.expand((h*d2/2+h*n2*delta-(A2-s.eye(4))*lam)[3])
forced=s.solve([res1,res2],[n1,n2])
assert forced=={n1:s.Rational(1,3),n2:-s.Rational(1,4)}

# K1 fixed-data comparisons for arbitrary coprime (3k,4l).
k,l,N0,N1=s.symbols('k l N0 N1',integer=True)
ell1=s.Matrix([0,0,-2*l*N0,0])
ell2=s.Matrix([0,-k*N1,0,0])
ell=s.Matrix.vstack(ell1,ell2)
general=s.Matrix([(4*l*N0-3*k*N1)/6,2*l*N0-k*N1,
                  2*k*N1-2*l*N0])
assert s.simplify(Dbar*general-ell[rows,:])==s.zeros(6,1)
assert s.expand(general[0]-(4*l*N0+3*k*N1)/6+k*N1)==0
M0=(A1*A2).inv()
ell0=-M0*(ell1+A1*ell2)
assert ell0[:2,0]==s.zeros(2,1)
assert Dbar*s.Matrix([-1,-3,4])==dbar-ell[rows,:].subs({k:1,l:1,N0:1,N1:-1})

out={
    'full_coboundary_rank':D.rank(),
    'full_augmented_rank':D.row_join(d).rank(),
    'quotient_delta_coboundary_matrix':Dbar.tolist(),
    'quotient_delta_defect':list(dbar),
    'unique_rational_solution':list(solution),
    'nonzero_smith_factors':[1,1,6],
    'order_of_obstruction_in_H1_quotient_local_system':6,
    'forced_base_windings_for_literal_minus_h_gamma_coordinate_shear':
       [forced[n1],forced[n2]],
    'sixfold_defect_after_integral_coboundary_g':list(6*d-D*s.Matrix([1,0,0,0])),
    'general_fixed_data_defects':[list(ell1),list(ell2)],
    'general_cusp_defect':list(ell0),
    'general_unique_rational_coboundary':list(general),
    'general_first_coordinate':'b/6-k*N1, where b=4*l*N0+3*k*N1=+1 or -1',
    'general_obstruction_order':6,
    'scope':'Obstruction on the ordinary bundle; no Theta7 residue is computed.'}
txt=json.dumps(out,indent=2,default=str)+'\n'
print(txt,end='')
Path(__file__).with_suffix('.out.json').write_text(txt)
