"""Fresh checks of ancillary formulas first encountered in released 01AK.

These are not represented as prereading independent derivation steps.
"""
import sympy as s
import json
x,y,z,t=s.symbols('x y z t', nonzero=True)
F=4*x**7-15*x**3*y*z*z+10*x*x*y**3*z-3*x*y**5+4*z**5
gs=[y*y-x*z,y*z*z-x**4,z**3-x**3*y]
sub={x:t**5,y:t**6,z:t**7}
H=s.hessian(F,(x,y,z)).subs(sub)
w=s.Matrix([7*t*t,0,-5]);assert s.simplify(H-2*t**21*w*w.T)==s.zeros(3)
assert s.diff(F,y,3).subs(sub)/6==-20*t**17
J=s.Matrix([[s.diff(g,v).subs(sub) for v in (x,y,z)] for g in gs])
a=J.row(0);b=J.row(1)+2*t**8*a
assert a==s.Matrix([[-t**7,2*t**6,-t**5]])
assert b==s.Matrix([[-6*t**15,5*t**14,0]])
assert J.row(2)==-3*t**9*a+t*b
ab=a.col_join(b)
minors=[s.expand(ab[:,list(ij)].det()) for ij in [(0,1),(0,2),(1,2)]]
assert minors==[7*t**21,-6*t**20,5*t**19]
velocity=s.Matrix([5*t**4,6*t**5,7*t**6])
contraction=[velocity[2],-velocity[1],velocity[0]]
assert all(s.simplify(m-t**15*c)==0 for m,c in zip(minors,contraction))
ell=5*t**8*a-2*b
assert s.simplify(t**(-5)*ell.T*ell-H/2)==s.zeros(3)
rad=s.Matrix([0,t**(-6),0])
assert (a*rad)[0]==2 and (b*rad)[0]==5*t**8
assert s.simplify(s.diff(F,y,3).subs(sub)*t**(-18)/6)==-20/t
# Exact numerical-semigroup conductor: every n=10,...,14 occurs, then +5
# covers every larger integer; the finite gaps below ten are determined here.
representable={5*i+6*j+7*k for i in range(4) for j in range(4) for k in range(4)}
gaps=[n for n in range(10) if n not in representable]
assert gaps==[1,2,3,4,8,9] and all(n in representable for n in range(10,15))
print(json.dumps({'all_assertions_passed':True,'semigroup_gaps':gaps,'conductor':10,
 'conormal_minors':[str(m) for m in minors],
 'exact_adjunction_factor':'a wedge b = t^15 i_(dparam/dt)(dx wedge dy wedge dz)',
 'hessian_factorization_verified':True,'quadratic_pole':5,'radical_cubic':'-20/t',
 'combined_tensor_pole':3*5+2*1,
 'timing_scope':'Ancillary formulas first read in released proof; these calculations add no prereading independence claim.'},indent=2))
