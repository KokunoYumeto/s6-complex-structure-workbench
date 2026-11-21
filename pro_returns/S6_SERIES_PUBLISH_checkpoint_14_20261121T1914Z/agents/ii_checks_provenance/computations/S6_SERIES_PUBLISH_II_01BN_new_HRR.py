"""Fresh formal degree-three multiplication for the 01BN derivation.

Written from the Chern character and Todd expansions, without opening prior
programs or the target proof.  This verifies only the displayed polynomial.
"""
from fractions import Fraction as F
import json

# Monomial entries are exponents of (c1,c2,c3,l); weighted degrees are 1,2,3,1.
zero=(0,0,0,0)
def mul(a,b):
    out={}
    for x,c in a.items():
        for y,d in b.items():
            z=tuple(u+v for u,v in zip(x,y))
            if sum(e*w for e,w in zip(z,(1,2,3,1)))<=3:
                out[z]=out.get(z,F(0))+c*d
    return {k:v for k,v in out.items() if v}
ch={zero:F(3),(1,0,0,0):F(1),(2,0,0,0):F(1,2),
    (0,1,0,0):F(-1),(3,0,0,0):F(1,6),
    (1,1,0,0):F(-1,2),(0,0,1,0):F(1,2)}
td={zero:F(1),(1,0,0,0):F(1,2),(2,0,0,0):F(1,12),
    (0,1,0,0):F(1,12),(1,1,0,0):F(1,24)}
el={zero:F(1),(0,0,0,1):F(1),(0,0,0,2):F(1,2),(0,0,0,3):F(1,6)}
degree3={k:v for k,v in mul(mul(ch,td),el).items()
         if sum(e*w for e,w in zip(k,(1,2,3,1)))==3}
expected={(3,0,0,0):F(1,2),(1,1,0,0):F(-19,24),(0,0,1,0):F(1,2),
          (2,0,0,1):F(5,4),(0,1,0,1):F(-3,4),(1,0,0,2):F(5,4),
          (0,0,0,3):F(1,2)}
assert degree3==expected
after_b2_zero={k:v for k,v in degree3.items() if k[0]==k[3]==0}
assert after_b2_zero=={(0,0,1,0):F(1,2)}
print(json.dumps({'method':'fresh Fraction-based graded polynomial multiplication',
                 'degree_three':{','.join(map(str,k)):str(v) for k,v in sorted(degree3.items())},
                 'after_c1_and_l_vanish':{','.join(map(str,k)):str(v) for k,v in after_b2_zero.items()},
                 'all_assertions_passed':True},indent=2))
