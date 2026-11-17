"""Exact finite checks for the ordinary-prime example in C.7.8."""
from math import isqrt
a1,a2,a3,a4,a6=0,0,1,-38,90
b2=a1*a1+4*a2;b4=2*a4+a1*a3;b6=a3*a3+4*a6
b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
disc=-b2*b2*b8-8*b4**3-27*b6**2+9*b2*b4*b6
pts=[(x,y) for x in range(5) for y in range(5)
     if (y*y+y-x*x*x+38*x-90)%5==0]
forms=[]
for a in range(1,isqrt(19//3)+1):
    for b in range(-a,a+1):
        if (b*b+19)%(4*a):continue
        c=(b*b+19)//(4*a)
        if a>c or ((abs(b)==a or a==c) and b<0):continue
        forms.append((a,b,c))
assert disc==-19**3 and len(pts)+1==7 and forms==[(1,1,5)]
assert 9*9+9==90
print('discriminant',disc,'F5 points',pts,'plus O; a5=-1')
print('reduced forms of discriminant -19:',forms)
print('ALL EXACT CHECKS PASSED')
