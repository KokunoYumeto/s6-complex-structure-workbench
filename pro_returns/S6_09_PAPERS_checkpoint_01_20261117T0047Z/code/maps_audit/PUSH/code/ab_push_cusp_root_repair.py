"""Exact checks for the failed fractional-period cusp-root repair.

The proof in B.3.3 is general.  The finite loops below certify examples
and all residue pairs in the stated finite range, without numerical
approximations.  A nontrivial r-component shift cannot preserve a
reduced q-fibre in this class of repairs.
"""
from math import gcd
from pathlib import Path
import json

records=[]
for n in (2,12):
    count=0
    bad=0
    for d in range(1,61):
        for a in range(d):
            for b in range(d):
                if (n*b)%d:
                    continue
                shift=(n*b//d)%n
                isotropy=gcd(d,gcd(a,b))
                q_multiplicity_bound=d//isotropy
                if q_multiplicity_bound==1:
                    assert a==b==0
                    assert shift==0
                if shift:
                    assert q_multiplicity_bound>1
                    bad+=1
                count+=1
    records.append({'n':n,'root_degrees_checked':[1,60],
                    'integral_shift_cases':count,
                    'nonzero_shift_cases_forced_nonreduced':bad})
    print('n=',n,':',count,'integral-shift residue cases;',bad,
          'nonzero shifts all force q multiplicity >1')

examples=[]
for d,a,b in [(12,0,11),(24,0,22),(24,1,22),(36,0,33)]:
    shift=(12*b//d)%12
    multiplicity=d//gcd(d,gcd(a,b))
    assert shift==11
    assert multiplicity>=12
    examples.append({'d':d,'a':a,'b':b,'r_shift':shift,'q_multiplicity_lower_bound':multiplicity})
print('desired shift -1 mod12 examples:',examples)
Path(__file__).with_suffix('.json').write_text(json.dumps({'checks':records,'examples':examples},indent=2)+'\n')
print('ALL EXACT CHECKS PASSED')
