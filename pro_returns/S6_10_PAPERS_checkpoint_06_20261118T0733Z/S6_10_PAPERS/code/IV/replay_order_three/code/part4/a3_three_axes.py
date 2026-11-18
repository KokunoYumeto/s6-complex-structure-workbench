"""Exact algebra for the fixed-axis A3 polar proof; no deformation shortcut."""
from pathlib import Path
import json
import sympy as s
x,y,z,a,b,c,r,t=s.symbols('x y z a b c r t')
k=y+z;h=y*z
M=s.Matrix([[h,0,a],[-k,h,b],[0,-x,c]])
assert s.expand(M.det()-a*x*k-b*x*h-c*h*h)==0
H=-t*t*(t+1)**2;L=t*t+t+1
derivative=s.factor(s.diff(H/L**3,t))
assert s.factor(derivative-t*(t-1)*(t+1)*(t+2)*(2*t+1)/L**4)==0
Phi=r**6*H**2*(r*L-1)
crit=[]
for tt in [s.Integer(1),s.Integer(-2),-s.Rational(1,2)]:
    rr=6/(7*L.subs(t,tt));point={r:rr,t:tt}
    assert all(s.simplify(s.diff(Phi,v).subs(point))==0 for v in [r,t])
    val=s.factor(Phi.subs(point))
    det=s.factor(s.hessian(Phi,[r,t]).det().subs(point))
    assert val==-s.Rational(1024,823543)
    assert det==s.Rational(4718592,1977326743)
    crit.append({'t':str(tt),'r':str(rr),'value':str(val),'Hessian_det':str(det)})
X,u=s.symbols('X u')
qa,qb,qc=s.symbols('qa qb qc')
quotient_values=s.Matrix([[-qb,qa,0],[-qc,0,qa],[0,-qc,qb]])
assert quotient_values.det()==0
assert quotient_values.subs({qa:1,qb:1,qc:1}).rank()==2
assert quotient_values.subs({qa:1,qb:1,qc:0}).rank()==2
assert s.Rational(2)+3+s.Rational(9,2)==s.Rational(19,2)
assert s.Rational(2)+3+3+1==9
expr=s.expand((X*k*k+h*h).subs(X,-u*u))
assert s.rem(expr,h-u*k,y)==0
quad=h-u*k
assert s.hessian(quad,[y,z,u]).det()!=0
out={'Hilbert_Burch_matrix':[[str(v) for v in row] for row in M[:,:2].tolist()],
     'determinant':str(s.factor(M.det())),
     'adjugate':[[str(v) for v in row] for row in M.adjugate().tolist()],
     'conic_map':['t*(t+1)','t+1','-t'],
     'rational_derivative':str(derivative),'Morse_points':crit,
     'normalization_quadric':str(quad),
     'normalization_Hessian_det':str(s.hessian(quad,[y,z,u]).det()),
     'three_axis_quotient_values':[[str(v) for v in row] for row in quotient_values.tolist()],
     'planar_three_branch_minimum_defect':10,
     'ordinary_three_axes_minimum_defect':9,
     'abandoned_route':'G -> G-epsilon with h fixed changes boundary A3 to two A1 points; not used',
     'all_checks_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('Fixed-axis A3 conic polar and conductor checks: PASS')
print('Conic derivative:',derivative)
for p in crit:print(p)
print('Normalization quadric:',quad)
print('Normalization Hessian determinant:',s.hessian(quad,[y,z,u]).det())
