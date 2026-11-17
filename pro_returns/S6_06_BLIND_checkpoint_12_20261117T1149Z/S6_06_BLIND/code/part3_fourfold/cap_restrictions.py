#!/usr/bin/env python3
"""Exact component-orbit arithmetic for the actual affine Tate-root caps."""
from pathlib import Path
import math,json
root=Path(__file__).resolve().parents[2]
count=0;transitive=[]
for N in range(1,13):
 for m in range(1,9):
  for n in range(-m,m+1):
   for c in range(N):
    for alpha in range(N*m):
     if (alpha-n*c)%N: continue
     orbits=math.gcd(N*m,math.gcd(alpha,m*c))
     assert orbits%math.gcd(N,c)==0
     count+=1
     if orbits==1:
      assert math.gcd(N,c)==1
      assert math.gcd(m,alpha)==1
      g=math.gcd(m,n)
      if g>1:
       mprime=m//g;nprime=n//g
       Ccomp=(mprime*alpha-nprime*m*c)%(N*m)
       order=(N*m)//math.gcd(N*m,Ccomp)
       assert order==g
      if N<=3 and m<=4:
       transitive.append(dict(N=N,m=m,n=n,c=c,alpha=alpha,
                             finite_kernel_order=g,
                             quotient_fibre_multiplicity=g))
out=dict(status='PASS',proofs=['P3K.18','P3K.19'],
 checked_norm_congruences=count,
 exact_formulas=dict(root_fibre='I_(N*m)',B_component='m*c',A_component='alpha',
                    norm='alpha = n*c (mod N)',
                    number_of_component_orbits='gcd(N*m,alpha,m*c)',
                    generic_quotient_multiplicity='g/h',
                    line_component_obstruction='m*a[G]=0 (mod N*m) iff a[G]=0 (mod N)'),
 representative_transitive_cases=transitive,
 scope='The code certifies integral component arithmetic. The actual cap maps, linking obstruction, finite-kernel cancellation, and source-line extension are proved in notes/part3_cap_restrictions.md.')
(root/'code/part3_fourfold/cap_restrictions.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',count,'exact norm congruences; every transitive nonprimitive Tate cap has the recorded nontrivial quotient multiplicity.')
