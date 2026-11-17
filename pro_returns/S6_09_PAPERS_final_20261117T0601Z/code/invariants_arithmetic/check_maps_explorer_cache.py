#!/usr/bin/env python3
"""Independently reconstruct and check the archived 50+8 API requests.

This validates archival input/output correspondence and reported group
invariants. It does not impersonate a new API execution or prove the
unpublished geometric local-model comparison.
"""
from pathlib import Path
from itertools import product
import hashlib
import json
import re

CODE=Path(__file__).resolve().parent
RECORDS=CODE/'maps_D_project/records'
OUT=CODE/'maps_D_review'
OUT.mkdir(exist_ok=True)
API='https://threefold-explorer-api.onrender.com/api/compute'
profiles=json.loads((RECORDS/'manifolds_os_configurations.json').read_text())
table=json.loads((RECORDS/'manifolds_explorer_21.json').read_text())
table_by={x['case']:x for x in table}
assert len(profiles)==21 and len(table)==len(table_by)==50
orders={'II':6,'III':4,'IV':3,'I0*':2,'IV*':3,'III*':4,'II*':6}
checks=[]

def check(name,payload):
    path=RECORDS/'manifolds_explorer_runs'/(name+'.json')
    raw=path.read_bytes(); r=json.loads(raw)
    assert r['url']==API,(name,'URL')
    assert r['input']==payload,(name,'request mismatch')
    a=r['response']; assert a['api_version']==2
    for key in ['os_entry','profile','P','Q','linearization_divisor']:
        assert a['input'][key]==payload[key],(name,key)
    hs=a['cohomology']; assert [g['degree'] for g in hs]==list(range(7))
    assert hs[0]['rank']==hs[6]['rank']==1
    for k in range(7):
        assert hs[k]['rank']==hs[6-k]['rank'],(name,'free duality',k)
    for k in range(1,7):
        assert hs[k]['torsion']==hs[7-k]['torsion'],(name,'torsion duality',k)
    assert sum((-1)**k*hs[k]['rank'] for k in range(7))==a['euler_characteristic']
    fg=a['fundamental_group']; ab=fg['abelianization']
    if ab=='0':
        assert hs[1]['rank']==0 and hs[2]['torsion']==[]
    elif ab=='Z':
        assert hs[1]['rank']==1 and hs[2]['torsion']==[]
    elif re.fullmatch(r'Z/[0-9]+',ab):
        assert hs[1]['rank']==0 and hs[2]['torsion']==[int(ab[2:])]
    else:
        raise AssertionError((name,'unhandled abelianization',ab))
    sphere=(fg['trivial'] and all(g['rank']==0 and not g['torsion'] for g in hs[1:6]))
    assert a['S6_for_supplied_smooth_model']==sphere
    rec={'case':name,'request':payload,'archive_path':str(path.relative_to(CODE.parent.parent)),
         'archive_sha256':hashlib.sha256(raw).hexdigest(),
         'api_version':2,'pi1':fg['description'],'simply_connected':fg['trivial'],
         'euler':a['euler_characteristic'],'cohomology':hs,'sphere':sphere}
    checks.append(rec)
    return a

for p in profiles:
    types=p['kodaira_types']; n=p['narrow_generators'][0][0]
    mult=[(int(t[1:]),i) for i,t in enumerate(types) if re.fullmatch(r'I[1-9][0-9]*',t)]
    zero=min(mult)[1]
    additive=[i for i in range(len(types)) if all(i!=j for _,j in mult)]
    for bits in product([0,1],repeat=len(additive)):
        logs=[None]*len(types)
        for i,b in zip(additive,bits):
            if b: logs[i]=['0',f'1/{orders.get(types[i],2)}']
        name=f"all21_{p['os_entry']}_{p['profile']}_{''.join(map(str,bits)) or 'none'}"
        payload={'os_entry':p['os_entry'],'profile':p['profile'],'P':[1],'Q':[n],
                 'linearization_divisor':[int(i==zero) for i in range(len(types))],
                 'log_data':logs,'coordinates':'invariant'}
        a=check(name,payload); row=table_by[name]
        expected={'case':name,'os_entry':p['os_entry'],'profile':p['profile'],
                  'configuration':' + '.join(types),'P':1,'Q':n,'zero_index':zero+1,
                  'log_data':json.dumps(logs),'pi1':a['fundamental_group']['description'],
                  'euler':a['euler_characteristic'],
                  'H_cohomology':'; '.join(g['label'] for g in a['cohomology']),
                  'S6':a['S6_for_supplied_smooth_model'],'status':'remote exact result'}
        assert expected==row,(name,'table differs')
assert len(checks)==50
assert sum(x['simply_connected'] for x in checks)==24
spheres=[x['case'] for x in checks if x['sphere']]
assert spheres==['all21_43_default_1','all21_43_II_10','all21_49_III_11']

for e,n in [(45,8),(47,14),(55,20),(56,30)]:
    for clutch in [0,1]:
        name=f'semistable_{e}_clutch{clutch}'
        payload={'os_entry':e,'profile':'default','P':[n],'Q':[1],
                 'linearization_divisor':[0,0,0,0,1,0],
                 'log_data':[None]*5+[[0,0,0,clutch]],'coordinates':'ambient'}
        a=check(name,payload)
        assert a['fundamental_group']['description']==('trivial' if clutch else 'Z')
        assert a['euler_characteristic']==2

result={'scope':'archival exact response/input verification, not a live API rerun',
        'bounded_requests':50,'simply_connected':24,'not_simply_connected':26,
        'sphere_outputs':spheres,'semistable_comparisons':4,
        'current_API_execution':'separate probe timed out; see maps_D_explorer_fresh_probe.json',
        'geometric_limit':'database local-model attachment certificates are not proved by this cache check',
        'checks':checks}
target=OUT/'explorer_cache_independent.json'
target.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('PASS: 50 independently regenerated requests match every archived payload and table row.')
print('PASS: 24 simply connected, 26 not simply connected; exactly three recorded sphere outputs.')
print('PASS: all 58 response groups satisfy free/torsion duality, Euler, and abelianization checks.')
print('PASS: four semistable comparisons have pi1 Z at clutch0 and trivial at clutch1.')
print('SCOPE: archival API-v2 responses; no new live API or geometric database validation claimed.')
