"""Algebraic base-cover and characteristic-number calculations."""
import sympy as S
t,x,y,a,b,z=S.symbols('t x y a b z')
A=-3*t**3*(t-1);B=2*t**4*(t-1)**2
D=S.factor(-16*(4*A**3+27*B**2))
print('Weierstrass discriminant =',D)
print('c4 =',S.factor(-48*A))
print('j =',S.factor((-48*A)**3/D))
profiles={'0':(4,3),'1':(3,4),'infinity':(1,12)}
ram=sum(count*(e-1) for count,e in profiles.values())
print('degree12 branch profiles:',profiles)
print('ramification degree:',ram,'genus:',(-24+ram+2)//2)
assert ram==28
print('minimal discriminant orders: good at 0, good at 1, order12 at infinity')
print('degree discriminant=12, chi(O)=1, Euler=12, signature=-8')
h=S.Rational(1,6)*12
print('height(P)=',h)
for k in [0,1,2,3,6]:
 print('m, h(mP), (mP).O, (mP-O)^2 =',k,k*k*h,k*k-1,-2*k*k)
print('J formal characteristic combination for M=O(P-O):',S.Rational(-24-12*(-2),24))
print('For O(6P-O) that combination:',S.Rational(-24-12*(-72),24))
print('This last arithmetic does not identify an actual clutching sphere or its mapping class.')
