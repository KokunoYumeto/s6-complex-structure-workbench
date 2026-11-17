"""Exact first-blowup identities for the coefficient-two D4 obstruction."""
from pathlib import Path
import json
import sympy as sp

u,x,z,v,w,s=sp.symbols('u x z v w s')
terms={}
for degree in (4,5):
    rows=[]
    for a in range(degree+1):
        for b in range(degree-a+1):
            c=degree-a-b
            if a+b>=3:
                rows.append((a,b,c))
    terms[degree]=rows

b_degrees=[c for a,b,c in terms[4] if b==1]
c_degrees=[c for a,b,c in terms[5] if b==0]
f4_line=[c for a,b,c in terms[4] if b==0]
assert max(b_degrees)==1
assert max(c_degrees)==2
assert max(f4_line)==1

b0,b1,c0,c1,c2=sp.symbols('b0 b1 c0 c1 c2')
B=b0+b1*w
C=c0+c1*w+c2*w*w
disc=sp.expand(B*B-4*C)
assert sp.Poly(disc,w).degree()==2
q=v*v+x*v*B+x*x*C
assert sp.expand(q.subs(v,x*s)/x**2-(s*s+B*s+C))==0

# The homogeneous degree-six discriminant has the prescribed fourth-order
# factor at the tangent direction of the critical axis.
X,Z=sp.symbols('X Z')
A_h=X
B_h=X**2*(b0*X+b1*Z)
C_h=X**3*(c0*X**2+c1*X*Z+c2*Z**2)
disc_h=sp.factor(B_h**2-4*A_h*C_h)
assert sp.expand(disc_h-X**4*((b0*X+b1*Z)**2-4*(c0*X**2+c1*X*Z+c2*Z**2)))==0

# All positive-integer solutions of 2=(d-2)n+a for d>=3 and a>=0.
solutions=[]
for d in range(3,9):
    for n in range(1,5):
        for a in range(5):
            if (d-2)*n+a==2:
                solutions.append((d,n,a))
assert solutions==[(3,1,1),(3,2,0),(4,1,0)]

out={
  'working_proof':'notes/part4_d4_pole_working.md',
  'normal_degree_restriction':'a+b>=3 for x^a u^b z^c',
  'f4_line_max_parameter_degree':max(f4_line),
  'f4_normal_derivative_max_parameter_degree':max(b_degrees),
  'f5_line_max_parameter_degree':max(c_degrees),
  'affine_double_cover_discriminant':str(disc),
  'homogeneous_discriminant':str(disc_h),
  'pole_solutions':[list(t) for t in solutions],
  'all_checks_passed':True,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('D4 coefficient-two pole and first-blowup checks: PASS')
print('Pole solutions (multiplicity, exceptional order, intrinsic pole):',solutions)
print('Affine double-cover discriminant:',disc)
print('Homogeneous discriminant:',disc_h)
print('The double cover has at most two branch points, including infinity.')
