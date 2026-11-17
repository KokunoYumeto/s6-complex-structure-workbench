"""Exact partial computations for C; no value of the S6 monodromy is claimed."""
from pathlib import Path
import json
import math
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

order=12
shifts=[4,-3,-1]
ram=[order//math.gcd(order,a) for a in shifts]
defect=sum(order-math.gcd(order,a) for a in shifts)
twogminus2=-2*order+defect
assert math.gcd(order,*shifts)==1
assert sum(shifts)==0
assert ram==[3,4,12]
assert twogminus2==4

# Untwisted W_A, using the independently checked I_(1,9) lattice.
G=s.diag(1,*([-1]*9))
F=s.Matrix([3]+[-1]*9)
O=s.eye(10)[:,9]
m=s.eye(10)[:,8]-O
v=s.Matrix([0,1,1,-1,-1,-1,0,0,1,0])
T=s.eye(10)+v*(F.T*G)-F*(v.T*G)+3*F*(F.T*G)
assert T.T*G*T==G
Tstar=T.inv()
n=m-F
assert Tstar*m==n
D=s.Matrix.hstack(s.eye(10)-Tstar,n,F)
B=-D.T*G*D
relation=s.Matrix(list(m)+[0,-1])
assert D*relation==s.zeros(10,1)
assert B*relation==s.zeros(12,1)
assert B.rank()==2
Bq=B[:11,:11]  # Eliminate A using A=m in H4(W_A).
assert Bq.rank()==2
snf=smith_normal_form(Bq,domain=ZZ)
smith=[abs(int(snf[i,i])) for i in range(11)]
assert [a for a in smith if a]==[1,11]
positive_gram=s.Matrix([[6,1],[1,2]])  # Coordinate order v,m.
assert positive_gram.det()==11
assert positive_gram[0,0]>0

# The first Pontryagin covector on H4(R+) is -4(a.F)-28h.
p=s.Matrix(list(-4*G*F)+[-28,0])
assert (p.T*relation)[0]==0
pq=p[:11,:]
solution,parameters=Bq.gauss_jordan_solve(pq)
solution=solution.subs({x:0 for x in parameters})
assert Bq*solution==pq
square=(pq.T*solution)[0]
assert square==s.Rational(4512,11)
signature=2
formal_combination=s.cancel((square-4*signature)/896)
assert formal_combination==s.Rational(79,176)

# Mixed circle-bundle obstruction on the cusp link.
angle,g,u,w,d,r=s.symbols('angle gamma u w delta r')
point=s.Matrix([angle,g,u,w,d])
def deck(p):
    a,g,u,w,d=p
    return s.Matrix([a+1,g,u,w+u,d-g])
def naive(p):
    a,g,u,w,d=p
    return s.Matrix([a,g+r,u,w,d])
def lifted(p):
    a,g,u,w,d=p
    return s.Matrix([a,g+r,u,w,d-r*a])
naive_defect=s.simplify(deck(naive(point))-naive(deck(point)))
assert naive_defect==s.Matrix([0,0,0,0,-r])
assert s.simplify(deck(lifted(point))-lifted(deck(point)))==s.zeros(5,1)
end_gauge=s.simplify(lifted(point).subs(r,1)-point-s.Matrix([0,1,0,0,0]))
assert end_gauge==s.Matrix([0,0,0,0,-angle])

out={
 'status':'PARTIAL; the S6 monodromy residue remains uncomputed',
 'Kummer_cover':{'equation':'y^12=t^4/(t-1)^3','shifts':shifts,
   'connected':True,'ramification_indices':ram,'RH_defect':defect,'genus':3},
 'untwisted_coboundary':{
   'boundary':'mapping torus of untwisted X(u); NOT the S6 mapping torus M_Phi',
   'cohomology_basis':'H2(R+) = L + Z H + Z A; H4(W_A) quotient A=m',
   'restriction_difference':D.tolist(),'intersection_matrix_before_quotient':B.tolist(),
   'intersection_matrix':Bq.tolist(),'intersection_smith':smith,
   'rank':2,'signature':signature,'p1_covector':list(pq),
   'rational_relative_p1_solution':list(solution),'p1_square':str(square),
   'formal_p1_signature_combination':str(formal_combination),
   'warning':'The displayed formal combination is NOT an Eells-Kuiper value for M_Phi. The boundary determinant class is nontrivial, and no finite log-transform/cusp surgery correction has been constructed.'},
 'cusp_lift':{'deck':'(a,g,u,w,d)->(a+1,g,u,w+u,d-g)',
   'naive_fractional_translation_defect':list(naive_defect),
   'equivariant_path_lift':'(a,g,u,w,d)->(a,g+r,u,w,d-r*a)',
   'endpoint_after_gamma_period_removed':list(end_gauge),
   'conclusion':'The quotient gamma loop has a delta gauge endpoint of q-degree -1; it is not an identity-ended loop upstairs.'}
}
print(json.dumps(out,indent=2,default=str))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
