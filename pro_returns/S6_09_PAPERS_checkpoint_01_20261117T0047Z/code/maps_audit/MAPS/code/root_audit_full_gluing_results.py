"""Independently recompute saved full-gluing Smith groups and duality checks."""
from pathlib import Path
import json
import sympy as S
from fourfolds_kuhn_cap_chains import homology_all
from fourfolds_vankampen import full_presentation

root=Path(__file__).resolve().parents[1]
inputs=[root/'code/fourfolds_total_homology_survivor.json',
        root/'code/fourfolds_total_homology_k3_2.json',
        root/'records/fourfolds_marked_involution_output.json']
certificates=[]
for source in inputs:
    data=json.loads(source.read_text())
    raw={int(n):a for n,a in data['reduced_differentials'].items()}
    matrices={}
    for n,a in raw.items():
        nr=len(a)
        nc=len(a[0]) if nr else len(raw.get(n+1,[]))
        matrices[n]=S.Matrix(nr,nc,[x for row in a for x in row])
    groups={n:h for n,h in homology_all(matrices).items() if n<=8}
    saved={int(n):h for n,h in data['homology'].items()}
    assert groups==saved,(source.name,groups,saved)
    group=full_presentation(data['matrices'],data['numerators'],data['orders'],data['clutch'])
    assert groups[1]=={'rank':group['H1_free_rank'],'torsion':group['H1_torsion']}
    ranks=[groups[n]['rank'] for n in range(9)]
    chi=sum((-1)**n*b for n,b in enumerate(ranks))
    assert chi==6
    mod2=[groups[n]['rank']+sum(t%2==0 for t in groups[n]['torsion'])+
          (sum(t%2==0 for t in groups[n-1]['torsion']) if n else 0)
          for n in range(9)]
    assert mod2==mod2[::-1] and mod2[0]==mod2[8]==1
    orientable=all(S.Matrix(M).det()==1 for M in data['matrices'])
    assert groups[8]=={'rank':int(orientable),'torsion':[]}
    if orientable:
        assert ranks==ranks[::-1]
        assert all(groups[n]['torsion']==groups[7-n]['torsion'] for n in range(8))
    record={'input':str(source.relative_to(root)),'integral_homology':groups,
            'independent_van_Kampen_H1':'passed','Euler':chi,
            'orientable':orientable,'mod2_Betti':mod2,
            'unit_cancellations':data['unit_cancellations'],
            'recomputed_Smith_and_duality':'passed'}
    certificates.append(record)
    print(source.name,record,flush=True)
(root/'records/root_full_gluing_audit.json').write_text(json.dumps(certificates,indent=2)+'\n')
print('ALL THREE FULL GLUING SMITH RESULTS, GROUP ABELIANIZATIONS AND DUALITY CHECKS PASSED')
