#!/usr/bin/env python3
"""Enumerate primitive section component contributions in the eight MW=Z cases."""
from fractions import Fraction as Q
from itertools import product
# Labels are multiplicity-one components from Shioda90 table8.16.
def A(n):return [(str(j),Q(j*(n-j),n)) for j in range(n)]
local={
 'E7':[('0',Q(0)),('nonzero',Q(3,2))],
 'E6':[('0',Q(0)),('1',Q(4,3)),('2',Q(4,3))],
 'D7':[('0',Q(0)),('vector',Q(1)),('spin+',Q(7,4)),('spin-',Q(7,4))],
 'D5':[('0',Q(0)),('vector',Q(1)),('spin+',Q(5,4)),('spin-',Q(5,4))]
}
for n in [2,3,4,5,7,8]:local['A'+str(n-1)]=A(n)
rows=[(43,['E7'],Q(1,2)),(45,['A7'],Q(1,8)),(46,['D7'],Q(1,4)),
      (47,['A6','A1'],Q(1,14)),(49,['E6','A1'],Q(1,6)),
      (50,['D5','A2'],Q(1,12)),(55,['A4','A3'],Q(1,20)),
      (56,['A4','A2','A1'],Q(1,30))]
for no,roots,h in rows:
 max_contr=sum(max(v for _,v in local[r]) for r in roots)
 assert max_contr<4-h
 found=[]
 for choices in product(*(local[r] for r in roots)):
  c=sum(v for _,v in choices)
  intersection=(h-2+c)/2
  if intersection.denominator==1 and intersection>=0:
   assert intersection==0
   found.append(tuple(label for label,_ in choices))
 assert found
 print('OS',no,'roots',roots,'h=',h,'max contribution=',max_contr,
       '4-h=',4-h,'P.O=0; component choices=',found)
print('Degree3 IV*+II+I2 pullback: chi=1, h=1/2, I6 contribution=3/2;')
print('correct intersection=',(Q(1,2)-2+Q(3,2))/2,
      'wrong-minus expression=',(Q(1,2)-2-Q(3,2))/2)
