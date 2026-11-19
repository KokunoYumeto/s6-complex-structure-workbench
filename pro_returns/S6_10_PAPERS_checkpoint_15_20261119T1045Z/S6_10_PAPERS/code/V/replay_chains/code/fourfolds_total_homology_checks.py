"""Independent global checks on the three completed F.2.35 integrations.

The first two full group tables are independently known from F.2.6 and
F.2.32.  Every example also checks the exact reduced d^2, van Kampen H1,
Euler number6, mod-two Poincare duality and the oriented/nonoriented top
groups.  No numerical approximation is used.
"""
import json
from pathlib import Path
import sympy as S
from fourfolds_vankampen import first_homology

root=Path(__file__).resolve().parents[1]
files=[root/'code/fourfolds_total_homology_survivor.json',
       root/'code/fourfolds_total_homology_k3_2.json',
       root/'records/fourfolds_marked_involution_output.json']
for number,path in enumerate(files):
    d=json.loads(path.read_text());H={int(n):v for n,v in d['homology'].items()}
    matrices=[S.Matrix(A) for A in d['matrices']]
    V=first_homology(matrices,d['numerators'],d['orders'],d['clutch'])
    assert H[1]=={'rank':V['rank'],'torsion':V['torsion']}
    D={int(n):S.Matrix(A) for n,A in d['reduced_differentials'].items()}
    for n in range(2,10):assert D[n-1]*D[n]==S.zeros(D[n-1].rows,D[n].cols)
    chi=sum((-1)**n*H[n]['rank'] for n in range(9));assert chi==6
    mod2=[H[n]['rank']+sum(a%2==0 for a in H[n]['torsion'])+
          (sum(a%2==0 for a in H[n-1]['torsion']) if n else 0) for n in range(9)]
    assert mod2==mod2[::-1] and mod2[0]==1
    if number==0:
        assert H=={n:{'rank':1 if n in (0,8) else 4 if n==4 else 0,
                      'torsion':[]} for n in range(9)}
    if number==1:
        tors={1:[18],2:[2]*5,3:[2]*10,4:[2]*10,5:[2]*5,6:[18]}
        assert H=={n:{'rank':1 if n in (0,8) else 4 if n==4 else 0,
                      'torsion':tors.get(n,[])} for n in range(9)}
    if all(M.det()==1 for M in matrices):assert H[8]=={'rank':1,'torsion':[]}
    else:
        assert H[8]=={'rank':0,'torsion':[]} and H[7]['torsion']==[2]
    print(path.name,'Euler',chi,'mod2 Betti',mod2,'ALL EXACT CHECKS PASSED')
