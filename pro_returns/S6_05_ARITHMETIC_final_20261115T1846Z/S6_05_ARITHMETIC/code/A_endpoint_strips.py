"""Exact endpoint identities and all small-height exceptions of A.4.5."""
import sympy as S
from math import isqrt
z=S.symbols('z',positive=True,integer=True)
A=S.sqrt(9*z*z-1)
cb=S.Rational(17,12)/S.sqrt(2)
sb=S.Rational(1,12)/S.sqrt(2)
cd=3*z/A;sd=1/A
assert S.simplify(cb*cb-sb*sb)==1
assert S.simplify(cd*cd-sd*sd)==1
for sign in [-1,1]:
 upper=S.simplify(S.sqrt(2)*A*(cb*cd+sign*sb*sd))
 assert upper==17*z/4+S.Rational(sign,12)
 print('s endpoint',sign,upper)
 t_end=S.simplify(S.sqrt(S.Rational(2,3))*A*(sb*cd+sign*cb*sd))
 assert S.simplify(t_end-(3*z+17*sign)/(12*S.sqrt(3)))==0
 print('t endpoint',sign,t_end)
# At z<=5 the whole strip has -1<t<2, so only t=0 or 1 need checking.
small=[]
for zz in range(1,6):
 assert (3*zz-17)**2<432 and (3*zz+17)**2<1728
 for tt in [0,1]:
  ss2=18*zz*zz-2+3*tt*tt; ss=isqrt(ss2)
  if ss*ss==ss2: small.append((ss,tt,zz))
assert small==[(4,0,1),(17,1,4)]
print('all small-height candidates:',small)
print('PASS: isolated exception is (4,0,1); every other strip point has 4s=17z')
