#!/usr/bin/env python3
"""Postrelease E11 check using rational Hilbert-series coefficient recurrence.

This does not use modular inverses, fractional residue degrees, or a search
over weighted monomials. The universal integer arguments are in the
comparison, so the finite check is explicitly an implementation certificate.
"""
from pathlib import Path
from fractions import Fraction as F
import math,json,hashlib

checked=0;max_degree=0;examples=[]
for k in range(1,81):
    for l in range(1,81):
        r,s=3*k,4*l
        if math.gcd(r,s)!=1:continue
        z=k*l;d=r+s;L=d-r*s
        query=[-z,-2*z,L,L-z,z-2*d]
        upto=max([0]+[max(n,-n-d) for n in query])
        max_degree=max(max_degree,upto)
        # (1-T^r)(1-T^s)H(T)=1.
        H=[0]*(upto+1);H[0]=1
        for n in range(1,upto+1):
            H[n]=(H[n-r] if n>=r else 0)+(H[n-s] if n>=s else 0)-(H[n-r-s] if n>=r+s else 0)
            assert H[n]>=0
        def value(n):return H[n] if n>=0 else 0
        def cohom(n):return [value(n),value(-n-d)]
        def coarse(n):
            a,b=cohom(n);return a-b-1
        assert coarse(-z)==coarse(-2*z)==coarse(L)==-1
        assert cohom(z-2*d)[0]==0
        assert coarse(L-z)==(-1 if k==1 else -2)
        checked+=1
        if (k,l) in [(1,1),(1,2),(3,1),(5,2),(79,80)]:
            examples.append({'k':k,'l':l,'cohomology':{str(n):cohom(n) for n in query},
                             'coarse_degree_L_minus_z':coarse(L-z)})

# Exact independent expansion of the degree-three HRR product ch(T)*td(T).
# Exponent triples are powers of c1,c2,c3, of respective weights1,2,3.
ch={(0,0,0):F(3),(1,0,0):F(1),(2,0,0):F(1,2),(0,1,0):F(-1),
    (3,0,0):F(1,6),(1,1,0):F(-1,2),(0,0,1):F(1,2)}
td={(0,0,0):F(1),(1,0,0):F(1,2),(2,0,0):F(1,12),(0,1,0):F(1,12),(1,1,0):F(1,24)}
degree3={}
for a,x in ch.items():
    for b,y in td.items():
        c=tuple(i+j for i,j in zip(a,b))
        if sum((j+1)*c[j] for j in range(3))==3:
            degree3[c]=degree3.get(c,F(0))+x*y
assert degree3=={(3,0,0):F(1,2),(1,1,0):F(-19,24),(0,0,1):F(1,2)}
assert degree3[(0,0,1)]*2==1

out={'schema':'S6_SERIES_PUBLISH.postrelease_different_method.v1','target':'01GI/cdp:st:E11',
     'timing':'After independent freeze4637fd206414… and complete target release/read.',
     'method':'Coefficient recurrence from (1-T^r)(1-T^s)H(T)=1, followed by weighted Serre duality and Euler characteristic.',
     'old_method':'Modular-inverse fractional-residue degree formula and direct monomial search.',
     'uses_modular_inverse':False,'uses_residue_degree_formula':False,'uses_weighted_monomial_search':False,
     'checked_pairs':checked,'range':'1<=k,l<=80, gcd(3k,4l)=1','maximum_coefficient_index':max_degree,
     'all_old_E11_identities_passed':True,'examples':examples,
     'universal_extra_degree_proof':'H1(O(L-z))=H0(O(13kl-2d)); A+2=l*a,B+2=k*b, 3a+4b=13 has unique positive solution(a,b)=(3,1), allowed exactly when k>1.',
     'HRR_degree_three':{'c1_cubed':'1/2','c1_c2':'-19/24','c3':'1/2'},
     'sphere_chi_T':1,'scope':'The written congruence proofs are universal; the finite run checks implementation only.',
     'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'events_added':0}
p=Path(__file__).with_name(Path(__file__).stem+'_output.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'output':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'checked_pairs':checked,'all_assertions_passed':True}))
