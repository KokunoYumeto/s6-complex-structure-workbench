"""Exact affine real-involution obstruction on the three real base arcs."""
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
A1=s.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2=s.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
M0=(A1*A2).inv()
H=s.Matrix([[1,0,0,0],[0,1,0,0],[-6,0,-1,0],[0,-1,0,-1]])
E=s.zeros(4);E[3,0]=1
gamma=s.Matrix([1,0,0,0]);delta=s.Matrix([0,0,0,1])
lines=[]
for name,a,alpha,scalars in [
 ('w_negative_imag',s.Rational(1,2),s.Rational(1,3),[-s.Rational(1,3),-s.Rational(4,3),-s.Rational(2,3)]),
 ('w_positive_imag',-s.Rational(1,2),s.Rational(1,2),[s.Rational(1,2),0,0])]:
 tau=-H+2*a*E
 for arc,G,scalar in zip(['t>1','0<t<1','t<0'],[s.eye(4),A2,M0.inv()],scalars):
  R=G.inv()*tau
  assert R**2==s.eye(4)
  C=s.eye(4)+R
  t=C*(alpha*gamma)+scalar*delta
  lines.append(f'{name}, {arc}: R={R.tolist()}, square_translation={list(t)}')
  assert all(x.q==1 for x in t)
  lattice=hermite_normal_form(C)
  for sign in [0,1]:
   rhs=t+sign*delta
   fixed=hermite_normal_form(C.row_join(rhs).applyfunc(s.Integer))==lattice
   lines.append(f'  half_delta={sign}: fixed={fixed}')
  minus=smith_normal_form(s.eye(4)-R,domain=s.ZZ)
  lines.append(f'  I-R Smith={list(minus.diagonal())}')
out='\n'.join(lines)+'\n'
print(out,end='')
Path(__file__).with_suffix('.out').write_text(out)
