"""Exact stabilizer arithmetic for P3F.33.

The proof covers all integers. This finite sweep checks the equivalent
closed criterion against each actual group element as a regression.
"""
from math import gcd
from pathlib import Path
import json

cases=0
for k in range(1,25):
    m=3*k
    for n in range(-25,26):
        for d in range(-25,26):
            predicted=gcd(gcd(k,abs(n)),abs(d))==1 and (n%3!=0 or k%3==0)
            bad=[]
            for j in range(1,m):
                if j%3==0:
                    r=j//3
                    fixed=(r*n)%k==0 and (r*d)%k==0
                else:
                    fixed=(j*n)%m==0 and (3*j*d)%m==0
                if fixed:
                    bad.append(j)
            assert predicted==(not bad),(k,n,d,bad)
            cases+=1
out={
 'statement':'P3F.33',
 'status':'Root-audited all-integer proof; finite sweep is a supplementary check',
 'free_criterion':'gcd(k,n,d)=1 and (3 does not divide n or 3 divides k)',
 'checked_cases':cases,
 'noncoprime_free_example':{'m':9,'n':3,'d':1},
 'fundamental_group':'Z/abs(n), with Z/0=Z',
 'sphere_sector':'n=+1 or -1',
 'higher_homology_noncoprime':'Not asserted',
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'Closed freeness criterion agrees with every group element in {cases} checked triples.')
print('Noncoprime free cap example: m=9,n=3,d=1.')
print('The all-integer proof and fundamental-group presentation are in P3F.33.')
