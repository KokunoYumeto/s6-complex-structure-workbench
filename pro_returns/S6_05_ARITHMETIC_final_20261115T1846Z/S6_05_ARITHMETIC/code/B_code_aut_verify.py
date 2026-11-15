"""Independent exhaustive certification of the code-group upper bound."""
from pathlib import Path
import json,subprocess
from sympy.combinatorics import Permutation,PermutationGroup
ROOT=Path(__file__).resolve().parents[1];REC=ROOT/'records'
d=json.loads((REC/'B_autJ_data.json').read_text());D=d['D']
# Pivot columns of the supplied RREF generator matrix are the standard basis.
piv=[next(i for i,x in enumerate(r) if x) for r in D]
assert all(D[i][piv[j]]==int(i==j) for i in range(5) for j in range(5))
ip=REC/'B_code_aut_exhaust.in';op=REC/'B_code_aut_exhaust.out';ip.write_text('\n'.join(' '.join(map(str,r)) for r in D)+'\n')
with ip.open() as a,op.open('w') as b:subprocess.run([str(ROOT/'code'/'B_code_aut_exhaust')],stdin=a,stdout=b,check=True)
perms=[]
for p,s in d['monomial_generators']:
 a=[]
 for i in range(12):q=2*p[i]+int(s[i]<0);a.extend([q,q^1])
 perms.append(Permutation(a))
G=PermutationGroup(perms);found=[]
for line in op.read_text().splitlines():
 if line.startswith('automorphism'):
  v=[]
  for t in line.split()[1:]:
   i,j=map(int,t.split(':'));q=2*i+j;v += [q,q^1]
  assert G.contains(Permutation(v));found.append(tuple(v))
assert len(found)==len(set(found))==int(G.order())==2880
print('all',len(found),'exhaustively found monomial automorphisms lie in the displayed generated group')
print(op.read_text().split('projective_classes ')[-1])
