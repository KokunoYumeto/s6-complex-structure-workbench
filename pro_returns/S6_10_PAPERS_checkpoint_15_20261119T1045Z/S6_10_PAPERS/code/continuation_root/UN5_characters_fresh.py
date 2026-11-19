"""Exact primitive lifts for every possible bielliptic canonical character."""
from pathlib import Path
import json,math
import sympy as s
from sympy.ntheory.modular import crt
records=[]
for n in [2,3,4,6]:
    for a in range(n):
        for b in range(n):
            if math.gcd(math.gcd(a,b),n)!=1:continue
            B=b or n
            primes=[p for p in s.factorint(B) if n%p]
            residues=[((1-a)*pow(n,-1,int(p)))%p for p in primes]
            k=int(crt(primes,residues)[0]) if primes else 0
            A=a+n*k
            assert A%n==a and B%n==b
            assert math.gcd(A,B)==1
            records.append({'canonical_order':n,'residues':[a,b],'primitive_lift':[A,B]})
unit_orders={}
for trace,n in [(-2,2),(-1,3),(0,4),(1,6),(2,1)]:
    M=s.eye(2) if trace==2 else -s.eye(2) if trace==-2 else s.Matrix([[0,-1],[1,trace]])
    assert M**n==s.eye(2)
    assert all(M**d!=s.eye(2) for d in range(1,n))
    unit_orders[str(trace)]=n
out={'characters':records,'count':len(records),'integer_trace_to_finite_order':unit_orders,
 'scope':'All primitive residue characters for n=2,3,4,6 have exact primitive integral lifts. Their gcd-one proof implies surjectivity after reduction modulo every m divisible by n; no bounded numerical extension to all m is used.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'characters_checked':len(records),'unit_orders':unit_orders,'all_exact':True},indent=2))
