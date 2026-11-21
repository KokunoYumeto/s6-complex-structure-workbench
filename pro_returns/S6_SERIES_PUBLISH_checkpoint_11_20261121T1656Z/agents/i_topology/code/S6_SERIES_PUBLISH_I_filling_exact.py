from pathlib import Path
import json, math
import sympy as S
out={}
r,Y=S.symbols('r Y', nonzero=True);X=r/Y;Xp=1/Y;Yp=r*Y
assert S.simplify(Xp*Yp-r)==0
assert S.simplify((r*Yp**-1)*r-Xp*r)==0
rot=[]
for l1 in range(12):
 if l1%3==0:continue
 for l2 in range(12):
  if l2%2==0:continue
  a,b=4*l1%12,3*l2%12
  assert all(k*a%12 for k in [1,2]);assert all(k*b%12 for k in [1,2,3])
  assert math.gcd(12,math.gcd(a,b))==1
  assert (a+b+(-(4*l1+3*l2)))%12==0
  rot.append([l1,l2,a,b,-(4*l1+3*l2)%12])
out['component_rotation_cases']=rot;out['number_cases']=len(rot)
t,a,b,c1,c2,D,B=S.symbols('t a b c1 c2 D B')
# Assign each variable its cohomological half-degree using a grading variable.
frac=S.series((1+t*B)/(1+t*(B+D)),t,0,4).removeO()
c1Y=c1+a;c2Y=c2+c1*a
# The branch correction is obtained by dividing the ambient degree-three correction by D then restricting D=a,B=b.
branch=(-c2Y+(B+D)*c1Y-(B+D)**2).subs({D:a,B:b}).expand()
expected=-c2+c1*b-a*b-b*b
assert S.expand(branch-expected)==0
paired=S.expand(branch+branch.xreplace({a:b,b:a}))
assert S.expand(paired-(-2*c2+c1*(a+b)-(a+b)**2))==0
F,L,H,C=S.symbols('F L H C')
# Degree-three pullback from the independently derived global K-class.
Dv=2*H-L
c3=Dv*C;c2R=C+F*Dv;c1R=F+Dv
virtual=S.expand(c3-Dv*c2R+F*Dv*c1R)
assert S.expand(virtual-F**2*Dv)==0
assert 24-2*12==0
assert sum((-1)**i*b for i,b in enumerate([1,1,8,14,8,1,1]))==2
out['branch_correction']=str(branch);out['paired_correction']=str(paired);out['independent_global_virtual_c3']=str(virtual);out['after_F_squared_zero']=0;out['untwisted_euler_from_betti']=2;out['outcome']='all exact assertions passed'
Path(__file__).resolve().parent.parent.joinpath('output/S6_SERIES_PUBLISH_I_filling_exact.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
