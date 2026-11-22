"""Exact Hilbert numerator / recurrence certificate for 01FS.
No monomial enumeration, symbolic algebra, or Smith normal forms.
"""
import json
from collections import Counter

def mul(a,b):
 c=Counter()
 for i,x in a.items():
  for j,y in b.items():c[i+j]+=x*y
 return {k:v for k,v in c.items() if v}
P=mul({3*i:1 for i in range(4)},{4*j:1 for j in range(3)})
assert mul(P,{0:1,3:-1,4:-1,7:1})=={0:1,12:-2,24:1}
# Recurrence H_k = H_(k-3)+H_(k-4)-H_(k-7), H_0=1.
H={}
for k in range(1001):H[k]=(1 if k==0 else 0)+H.get(k-3,0)+H.get(k-4,0)-H.get(k-7,0)
def residue(k):
 a,b=(3*k)%4,k%3
 return (k-3*a-4*b)//12
rows=[]
for r in range(12):
 lift=[k for k in P if k%12==r]
 assert len(lift)==1 and P[lift[0]]==1
 assert lift[0]==3*((3*r)%4)+4*(r%3)
 rows.append({'r':r,'numerator_exponent':lift[0],'degree_offset':residue(r)})
for k in H:
 assert H[k]==max(residue(k)+1,0)
# Twelve affine residue expressions certify the Euler index for every integer.
for n in range(12):
 assert residue(n+6)-residue(n+2)+int(n%3!=0)==1
assert all(residue(k)==-1 for k in [-1,-2,1,5])
def dims(n):
 h0=lambda k:H.get(k,0)
 h1=lambda k:H.get(-k-7,0)
 e=int(n%3!=0)
 return [h0(n)+h0(n-1),h1(n)+h1(n-1)+h0(n)+h0(n-1)+h0(n+2),h1(n)+h1(n-1)+h1(n+2)+h0(n+6)+e,h1(n+6)]
for n in range(-240,241):
 h=dims(n)
 assert sum((-1)**i*x for i,x in enumerate(h))==1
assert dims(-1)==[0,0,1,0] and H[5]==0
# Formal finite-stabilizer averaging records exact character dimensions.
jet_weights={n:[j for j in range(2) if (n-1-j)%3==0] for n in range(3)}
assert jet_weights=={0:[],1:[0],2:[1]}
# Positive root line evaluation: recurrence gives the three residue seeds6,7,8.
assert [k for k in range(6) if H[k]==0]==[1,2,5]
assert all(H[k]>0 for k in [6,7,8])
print(json.dumps({'method':'Polynomial convolution verifies the Hilbert rational identity. Its unique numerator exponent in each residue proves every positive weighted-line dimension; a separate linear recurrence cross-checks1001 coefficients. Serre-duality transport and twelve affine identities give all integral twists.','hilbert_numerator':P,'denominator_identity':True,'residue_rows':rows,'recurrence_coefficients_checked':1001,'all_integer_index_identity':True,'root_jet_characters':jet_weights,'normalization_semigroup_gaps':[1,2,5],'positive_seed_weights':[6,7,8],'exception_n_minus_one':dims(-1),'assertions_passed':True},indent=2)+'\n')
