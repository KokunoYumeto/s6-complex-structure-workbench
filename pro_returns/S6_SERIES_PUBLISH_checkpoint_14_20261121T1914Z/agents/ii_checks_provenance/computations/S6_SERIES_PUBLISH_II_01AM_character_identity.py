"""Fresh universal cyclic-character calculation for the multiple fibre."""
import json

# Identity in Z[T]: (T^2+2T-3)=(T-1)(T+3).  Multiplying by
# R_m=1+...+T^(m-1) yields (T^2+2T)R_m-3R_m=(T^m-1)(T+3),
# universally for m.  This computes three invariant dimensions exactly.
factor=[-3,2,1]
product=[0,0,0]
for i,a in enumerate((-1,1)):
 for j,b in enumerate((3,1)):product[i+j]+=a*b
assert factor==product
samples=[]
for m in (3,4,5,7,12,31,100):
 weights=[(j+d+1)%m for d in (0,0,1) for j in range(m)]
 multiplicities=[weights.count(r) for r in range(m)]
 assert multiplicities==[3]*m
 assert [d+1 for d in (0,0,1)]==[1,1,2]
 assert all((d+1)%m for d in (0,0,1))
 invariants=[m-1,m-1,m-2]
 assert all(0<=j<m and (j+d+1)%m==0 for j,d in zip(invariants,(0,0,1)))
 samples.append({'m':m,'full_invariants':multiplicities[0],'reduced_invariants':0,'invariant_monomial_degrees':invariants})
print(json.dumps({'universal_character_identity':'(T^2+2T)R_m-3R_m=(T^m-1)(T+3)',
 'universal_invariant_degrees':['m-1','m-1','m-2'],
 'scope':'The factorization and geometric-series identity prove every m>=3. The listed finite cases are diagnostics only.',
 'diagnostics':samples,'all_assertions_passed':True},indent=2))
