"""Regenerate the 50 bounded requests and audit their exact saved replies.

No remote request or geometric validation is claimed by this archive audit.
"""
from pathlib import Path
from itertools import product
import hashlib,json,re

ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
SOURCE=ROOT/'sources/returns/S6_04_MAPS_MANIFOLDS/records'
profiles=json.loads((HERE/'manifolds_os_configurations.json').read_text())
orders={'II':6,'III':4,'IV':3,'I0*':2,'IV*':3,'III*':4,'II*':6}
rows=[]
for r in profiles:
    types=r['kodaira_types']; n=int(r['narrow_generators'][0][0])
    _,zero=min((int(t[1:]),i) for i,t in enumerate(types) if re.fullmatch(r'I[1-9][0-9]*',t))
    weights=[int(i==zero) for i in range(len(types))]
    additives=[i for i,t in enumerate(types) if not re.fullmatch(r'I[1-9][0-9]*',t)]
    for bits in product([0,1],repeat=len(additives)):
        logs=[None]*len(types)
        for i,bit in zip(additives,bits):
            if bit:logs[i]=['0','1/'+str(orders.get(types[i],2))]
        name='all21_%s_%s_%s'%(r['os_entry'],r['profile'],''.join(map(str,bits)) or 'none')
        payload=dict(os_entry=r['os_entry'],profile=r['profile'],P=[1],Q=[n],
                     linearization_divisor=weights,log_data=logs,coordinates='invariant')
        p=SOURCE/'manifolds_explorer_runs'/(name+'.json')
        saved=json.loads(p.read_text())
        assert saved['input']==payload,(name,'payload mismatch')
        answer=saved['response'];assert answer['api_version']==2
        groups=[x['label'] for x in answer['cohomology']]
        assert len(groups)==7
        rows.append({'case':name,'request':payload,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
                     'simply_connected':answer['fundamental_group']['trivial'],
                     'S6_for_supplied_smooth_model':answer['S6_for_supplied_smooth_model'],
                     'cohomology':groups,'qualification':answer.get('qualification')})
result={'requests_matched':len(rows),'simply_connected_outputs':sum(r['simply_connected'] for r in rows),
        'sphere_outputs':[r['case'] for r in rows if r['S6_for_supplied_smooth_model']],
        'scope':'Archived API-v2 payload/reply audit; no new remote reply or independent geometric attachment validation.',
        'rows':rows}
assert result['requests_matched']==50
assert result['simply_connected_outputs']==24
assert len(result['sphere_outputs'])==3
clutches=[]
for entry,n in [(45,8),(47,14),(55,20),(56,30)]:
    for clutch in [0,1]:
        p=SOURCE/'manifolds_explorer_runs'/f'semistable_{entry}_clutch{clutch}.json'
        saved=json.loads(p.read_text())
        expected=dict(os_entry=entry,profile='default',P=[n],Q=[1],
                      linearization_divisor=[0,0,0,0,1,0],
                      log_data=[None]*5+[[0,0,0,clutch]],coordinates='ambient')
        assert saved['input']==expected
        group=saved['response']['fundamental_group']
        assert group['description']==('trivial' if clutch else 'Z')
        clutches.append({'case':p.stem,'request':expected,'fundamental_group':group,
                        'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
result['integer_clutch_comparisons']=clutches
(HERE/'audit_explorer_archive.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
