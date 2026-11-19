#!/usr/bin/env python3
from fractions import Fraction as Q
from pathlib import Path
import json
# New exact affine coefficient arithmetic, no old producer or output used.
# Every pair records the coefficients of 1,n.
C=(Q(2),Q(240))
p1sq=tuple(4*x for x in C)
p2=(C[0]+12,C[1])
sigma=tuple((7*p2[i]-p1sq[i])/45 for i in range(2))
assert p1sq==(8,960) and p2==(14,240) and sigma==(2,16)
lo,hi=(Q(-4)-sigma[0])/sigma[1],(Q(4)-sigma[0])/sigma[1]
assert (lo,hi)==(Q(-3,8),Q(1,8))
ceil_lo=-((-lo.numerator)//lo.denominator)
floor_hi=hi.numerator//hi.denominator
assert ceil_lo==floor_hi==0
assert (C[0],p1sq[0],p2[0],sigma[0])==(2,8,14,2)
result={"status":"PASS","method":"new exact rational affine arithmetic and integer interval endpoints","Todd_integer_interval":[str(lo),str(hi)],"only_integer":0,"characteristic_numbers":{"c2_squared":2,"p1_squared":8,"p2":14,"signature":2}}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
