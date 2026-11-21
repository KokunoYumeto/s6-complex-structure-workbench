"""Fresh elimination, gradient and transverse-jet checks for 01AK."""
import sympy as s
import json
x,y,z,t,a,b=s.symbols('x y z t a b')
I=[y*y-x*z,y*z*z-x**4,z**3-x**3*y]
F=4*x**7-15*x**3*y*z*z+10*x*x*y**3*z-3*x*y**5+4*z**5
fx,fy,fz=[s.diff(F,v) for v in (x,y,z)]
assert s.expand(fy+15*x*I[0]**2)==0
assert s.expand(fx+28*x*x*I[1]-14*x*y*z*I[0]+3*y*I[0]**2)==0
assert s.expand(fz-20*z*I[2]-10*x*x*y*I[0])==0
assert s.expand(z*z*I[0]-y*I[1]+x*I[2])==0
assert s.expand(x**3*I[0]-z*I[1]+y*I[2])==0
assert s.expand(5*x*fx+6*y*fy+7*z*fz-35*F)==0
for f in [F,fx,fy,fz]+I: assert s.expand(f.subs({x:t**5,y:t**6,z:t**7}))==0
G=s.groebner([x-t**5,y-t**6,z-t**7],t,z,y,x,order='lex')
eliminated=[q.as_expr() for q in G.polys if not q.as_expr().has(t)]
GI=s.groebner(I,z,y,x,order='lex')
GE=s.groebner(eliminated,z,y,x,order='lex')
assert list(GI)==list(GE)
sliceF=s.expand(F.subs({x:1,y:1+a,z:1+b}))
parts={k:s.expand(sum(c*a**mon[0]*b**mon[1] for mon,c in s.Poly(sliceF,a,b).terms() if sum(mon)==k)) for k in (2,3)}
assert parts[2]==25*b*b
assert s.expand(parts[3].subs(b,0))==-20*a**3
weights=[12,20,21]
allowed=[]
for i in range(3):
 for j in range(i,3):
  need=35-weights[i]-weights[j]
  mon=[]
  for ax in range(8):
   for ay in range(6):
    for az in range(6):
     if 5*ax+6*ay+7*az==need:mon.append((ax,ay,az))
  if mon:allowed.append({'generators':[i+1,j+1],'coefficient_monomials':mon})
assert allowed==[{'generators':[1,1],'coefficient_monomials':[(1,1,0)]}]
assert s.Poly(F,x,y,z).coeff_monomial(x**7)==4
assert s.Poly(x*y*I[0]**2,x,y,z).coeff_monomial(x**7)==0
print(json.dumps({'elimination_kernel_equals_I':True,'groebner_basis':[str(q) for q in GI],
 'exact_gradient_and_syzygy_identities':True,'transverse_degree_two':str(parts[2]),
 'transverse_degree_three':str(parts[3]),'cubic_on_hessian_radical':'-20*a**3',
 'weight35_terms_available_in_I_squared':allowed,
 'I_squared_nonmembership_witness':'x^7 coefficient is 4 in F and 0 in every allowed weight-35 product',
 'all_assertions_passed':True},indent=2))
