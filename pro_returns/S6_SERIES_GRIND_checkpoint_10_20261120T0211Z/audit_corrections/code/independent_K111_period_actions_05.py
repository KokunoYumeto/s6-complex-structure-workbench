"""Post-reading check of the two actual cocharacters on every saved period map."""
from pathlib import Path
import json,hashlib,time
import sympy as s
root=Path(__file__).resolve().parents[2]/'audit_sign'
start=time.perf_counter(); count=0; rows=[]
data=[('zero','K111_new_zero_endpoint_v2.json',[-1,0,0,0],[-1,1,0,0]),
      ('one','K111_new_one_endpoint.json',[0,1,0,0],[-1,0,0,0]),
      ('infinity','K111_new_infinity_endpoint.json',[1,0,0,0],[0,1,0,0])]
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
for ep,name,delta,second in data:
    d=json.loads((root/name).read_text())
    for j,p in enumerate(d['period_maps']):
        if 'lattice_matrix' in p:
            M=s.Matrix(p['lattice_matrix']);Mi=s.Matrix(p['inverse_lattice_matrix'])
        else:
            Bs=s.Matrix.hstack(*[s.Matrix(v) for v in d['cones'][p['source_chart']]['rays']])
            Bt=s.Matrix.hstack(*[s.Matrix(v) for v in d['cones'][p['target_chart']]['rays']])
            M=Bt*s.Matrix(p['matrix'])*Bs.inv()
            Mi=Bs*s.Matrix(p['inverse'])*Bt.inv()
        assert M*Mi==s.eye(4),(ep,j,'full inverse')
        count+=1
        M=M.tolist();Mi=Mi.tolist()
        for mat,label in [(M,'forward'),(Mi,'inverse')]:
            for co,clabel in [(delta,'physical'),(second,'second')]:
                assert [dot(r,co) for r in mat]==co,(ep,j,label,clabel)
                count+=1
            assert mat[2:]==[[0,0,1,0],[0,0,0,1]],(ep,j,label,'base parameters')
            count+=1
    rows.append({'endpoint':ep,'period_pairs':len(d['period_maps']),'cocharacters':[delta,second],
                 'sha256':hashlib.sha256((root/name).read_bytes()).hexdigest()})
out={'status':'PASS','checks':count,'endpoints':rows,'seconds':round(time.perf_counter()-start,6),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':'Every saved full native lattice period and inverse fixes both physical and second cocharacters and the two base parameters. Full units therefore have invariant arguments. Actual point/O unit-ratio action was independently checked in the companion boundary/normal program.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
