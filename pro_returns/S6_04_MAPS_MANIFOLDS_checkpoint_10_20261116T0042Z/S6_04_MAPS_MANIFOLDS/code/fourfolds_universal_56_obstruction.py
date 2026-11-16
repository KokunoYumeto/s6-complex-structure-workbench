"""Exact 3-adic middle-pairing certificate for Theorem F.2.27.

The displayed integer matrix represents the forced Z_3 conjugacy class,
not a claim that every global integral finite matrix has this basis.
The all-lattice reduction is proved in the accompanying manuscript.
"""
from itertools import combinations
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

ROOT=Path(__file__).resolve().parents[1]
basis=list(combinations(range(6),3))
M=s.zeros(6)
for source,target in [(0,0),(1,2),(2,3),(3,1)]:M[target,source]=1
M[4,4]=M[5,5]=-1
assert M**6==s.eye(6)
assert M.charpoly().as_expr().factor()==(s.Symbol('lambda')-1)**2*(s.Symbol('lambda')+1)**2*(s.Symbol('lambda')**2+s.Symbol('lambda')+1)
E=s.Matrix([[M.extract(I,J).det() for J in basis] for I in basis])

def exterior(terms):
    v=s.zeros(len(basis),1)
    for coefficient,indices in terms:
        if len(set(indices))<len(indices):continue
        sign=(-1)**sum(indices[i]>indices[j] for i in range(len(indices)) for j in range(i+1,len(indices)))
        v[basis.index(tuple(sorted(indices)))]+=coefficient*sign
    return v

# u(ab+bc+ca), abc, ude, (a+b+c)de.
K=s.Matrix.hstack(
    exterior([(1,(0,1,2)),(1,(0,2,3)),(1,(0,3,1))]),
    exterior([(1,(1,2,3))]),
    exterior([(1,(0,4,5))]),
    exterior([(1,(1,4,5)),(1,(2,4,5)),(1,(3,4,5))]))
assert (E-s.eye(20))*K==s.zeros(20,4)
assert 20-(E-s.eye(20)).rank()==4
SK=smith_normal_form(K,domain=s.ZZ)
assert [abs(int(SK[i,i])) for i in range(4)]==[1]*4

J=s.zeros(20)
for i,I in enumerate(basis):
 for j,Jj in enumerate(basis):
  if set(I).isdisjoint(Jj):
   word=I+Jj
   J[i,j]=(-1)**sum(word[a]>word[b] for a in range(6) for b in range(a+1,6))
Q=K.T*J*K
assert Q.T==-Q and Q.det()==9
SQ=smith_normal_form(Q,domain=s.ZZ)
assert [abs(int(SQ[i,i])) for i in range(4)]==[1,1,3,3]

# Independent wedge coefficient calculation by determinants of six columns.
Q2=s.zeros(4)
for a in range(4):
 for b in range(4):
  for i,I in enumerate(basis):
   if not K[i,a]:continue
   for j,Jj in enumerate(basis):
    if K[j,b]:
     columns=[s.eye(6)[:,t] for t in I+Jj]
     Q2[a,b]+=K[i,a]*K[j,b]*s.Matrix.hstack(*columns).det()
assert Q2==Q

P=M[1:4,1:4]
N=s.eye(3)+P+P**2
assert N==s.ones(3)
assert ((P-s.eye(3))**2-N).applyfunc(lambda x:int(x)%3)==s.zeros(3)
q=s.eye(3)[:,0]
orbit=s.Matrix.hstack(q,P*q,P**2*q)
assert abs(orbit.det())==1
assert N*q==s.ones(3,1)
cover_degree=6
assert cover_degree**4//int(Q.det())==144
index=12
assert index**2*Q.det()==cover_degree**4
assert index%3==0 and index%9!=0

out={'scope':'Forced local conjugacy over Z_3 after m=n=h=6; no global integral basis asserted',
     'matrix':M.tolist(),'invariant_degree3_basis':K.tolist(),
     'middle_pairing':Q.tolist(),'pairing_smith':[1,1,3,3],
     'pairing_determinant':int(Q.det()),'degree3_covering_index_for_this_integer_model':index,
     'universal_3_primary_covering_cokernel':'Z/3',
     'normal_form_argument':'Norm3 nonzero modulo3 forces one Jordan block of length3; an orbit basis is unimodular over Z3',
     'global_consequence':'The local Z/3 injects in E_inf^(1,3); its preimage has finite kernel E_inf^(2,2), hence Tor_3 H4 and Tor_3 H3 are nonzero.'}
(ROOT/'records/fourfolds_universal_56_obstruction.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print('Forced local matrix (cohomology or homology):')
print(M)
print('Primitive full invariant degree-three basis: rank4, all Smith factors1')
print('Middle skew pairing:')
print(Q)
print('Pairing Smith factors [1,1,3,3]; determinant9')
print('Independent exterior-determinant pairing agrees')
print('Norm3 is nonzero modulo3; orbit basis determinant',orbit.det())
print('Degree6 pullback: v3(index)=1, so universal local cokernel Z/3')
print('ALL EXACT LOCAL CERTIFICATES PASSED')
