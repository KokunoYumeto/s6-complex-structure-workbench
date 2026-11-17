"""Exact integral monodromy calculation on the degree-twelve component cover.

Conventions: words act by multiplying their matrices in written order;
the coset shifts of a,b are 4,-3 in Z/12.  No numerical arithmetic is used.
The final commutator provides an independent two-column certificate.
"""
from collections import deque
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.domains import ZZ

HERE=Path(__file__).resolve().parent
A=s.Matrix([[0,1],[-1,-1]])
B=s.Matrix([[0,-1],[1,0]])
I=s.eye(2)
assert A**3==I and B**4==I
letters={'a':(4,A),'b':(-3,B)}
words={0:''}
matrices={0:I}
queue=deque([0])
while queue:
    i=queue.popleft()
    for letter,(shift,M) in letters.items():
        j=(i+shift)%12
        if j not in words:
            words[j]=words[i]+letter
            matrices[j]=matrices[i]*M
            queue.append(j)
assert len(words)==12
generators=[]
columns=[]
for i in range(12):
    for letter,(shift,M) in letters.items():
        j=(i+shift)%12
        G=matrices[i]*M*matrices[j].inv()
        assert G.det()==1
        if G!=I:
            generators.append({'from':i,'letter':letter,'to':j,
                'schreier_word':[words[i],letter,words[j]+' inverse'],
                'matrix':G.tolist(),'det_G_minus_I':int((G-I).det())})
            columns.append(G-I)
relations=s.Matrix.hstack(*columns)
H=hermite_normal_form(relations)
S=smith_normal_form(relations,domain=ZZ)
assert H==I
commutator=A*B*A.inv()*B.inv()
assert commutator==s.Matrix([[1,-1],[-1,2]])
assert (commutator-I).det()==-1
out={'A':A.tolist(),'B':B.tolist(),'orders':[3,4],
     'cover_shifts':[4,-3],'tree_words':words,
     'nonidentity_schreier_generators':generators,
     'coinvariant_relation_matrix':relations.tolist(),
     'relation_column_HNF':H.tolist(),
     'relation_SNF_nonzero':[int(S[i,i]) for i in range(2)],
     'commutator':commutator.tolist(),
     'det_commutator_minus_I':int((commutator-I).det()),
     'coinvariant_group':'0',
     'scope':'Integral lattice calculation; geometric torsor and corner comparison require the separate proof.'}
(HERE/'torsor_schreier.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
print(json.dumps(out,indent=2,default=int))
