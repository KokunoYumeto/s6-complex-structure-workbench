"""Exact pre-release algebra for the Hopf zero-Euler characterization.

Integer equality cases are exhaustive because u,v are nonnegative and
u+v=r<=1.  Character extension is checked by Gaussian elimination in
both pivot cases, rather than the earlier Hopf adjugate calculation.
"""
import json
import sympy as S

c,q,g,b,n,r,u,v=S.symbols('c q g b n r u v',integer=True)
curve_e=c+q-2*g-b
rank=b+n-q
rewritten=c+n-2*g-r
assert S.expand(rewritten.subs(r,rank)-curve_e)==0
assert S.expand(rewritten.subs({c:g+u,n:g+v})-(u+v-r))==0
equality_cases=[]
for rr in (0,1):
    for uu in range(rr+1):
        for vv in range(rr+1):
            if uu+vv==rr:equality_cases.append([uu,vv,rr])
assert sorted(equality_cases)==[[0,0,0],[0,1,1],[1,0,1]]

a,B,C,d,U,V=S.symbols('a B C d U V')
P=S.Matrix([[a,B],[C,d]])
det=S.expand(P.det())
# Solve ell*P=(U,V).  For a!=0 eliminate the first unknown, then
# back substitute.  In the a=0 case invertibility forces B,C!=0.
y=S.cancel((V-U*B/a)/(d-C*B/a))
x=S.cancel((U-C*y)/a)
ell=S.Matrix([[x,y]])
assert (ell*P-S.Matrix([[U,V]])).applyfunc(S.cancel)==S.zeros(1,2)
y0=U/C
x0=S.cancel((V-d*y0)/B)
ell0=S.Matrix([[x0,y0]])
assert (ell0*P.subs(a,0)-S.Matrix([[U,V]])).applyfunc(S.cancel)==S.zeros(1,2)

mu,coeff=S.symbols('mu coeff',integer=True)
exceptional_canonical_coefficient=1+coeff-mu
solution=S.solve(exceptional_canonical_coefficient,coeff)[0]
assert solution==mu-1

print(json.dumps({
 'scope':'Exact Euler rearrangement, exhaustive nonnegative integer equality cases and the two Gaussian-elimination pivots for the rational character. Geometry and group normal forms are proved in the derivation.',
 'curve_euler':str(curve_e),'free_graph_rank':str(rank),
 'rewritten_euler':str(rewritten),'nonnegative_differences':['u=c-g','v=n-g'],
 'zero_euler_cases_u_v_r':equality_cases,
 'case_with_extra_rational_image':[1,0,1],
 'retained_cases_have_c_equals_g':[[0,0,0],[0,1,1]],
 'character_matrix':[[str(z) for z in row] for row in P.tolist()],
 'determinant':str(det),
 'gaussian_pivot_a_nonzero':{'second_coordinate':str(y),'first_coordinate':str(x),'composition_residual':['0','0']},
 'gaussian_pivot_a_zero':{'invertibility_forces':'B*C nonzero','second_coordinate':str(y0),'first_coordinate':str(x0),'composition_residual':['0','0']},
 'pole_blowup':{'exceptional_coefficient':str(solution),
     'Euler_increment_of_surface':'2-1=1','Euler_increment_of_a_rational_leaf':'2-1=1',
     'Euler_increment_of_subdivision':'2-2+1=1'},
 'no_extra_independent_computation_event':True
},indent=2))
