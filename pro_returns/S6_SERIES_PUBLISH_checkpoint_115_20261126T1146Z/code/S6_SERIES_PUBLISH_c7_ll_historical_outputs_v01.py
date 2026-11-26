#!/usr/bin/env python3
"""Retrieve the cited historical LL outputs and expose only LL rows.

This program does not execute the historical algorithms. Shared AH
rows outside the seven released LL keys remain unprinted and embargoed.
The exact retrieved bytes stay in /tmp; selected LL data and provenance
are retained in this lane. Preserve this version and its combined output.
"""
from pathlib import Path
from hashlib import sha256
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
import json

LANE=Path('agents/continuation7_iii_residual_two_primary')
fresh=json.loads((LANE/'S6_SERIES_PUBLISH_III_02LL_fresh_localization_data.json').read_text())
keys={(r['OS'],'default',r['a'],r['c'],r['zero']) for r in fresh['rows']}
prefix=('https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/'
        'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7/'
        'pro_returns/S6_10_PAPERS_checkpoint_15_20261119T1045Z/S6_10_PAPERS/')
names=['fourfolds_D2_2power_AH','manifolds_even_critical_cycles','fourfolds_D2_frame_certificate']
result=[]
for name in names:
    attempts=[]
    received=None
    for directory in ['code/III/','records/']:
        url=prefix+directory+name+'.json'
        try:
            with urlopen(Request(url,headers={'User-Agent':'S6-series-source-audit'}),timeout=25) as r:
                content=r.read()
            parsed=json.loads(content)
            received=(url,content,parsed)
            attempts.append({'url':url,'status':'success','bytes':len(content)})
            break
        except (HTTPError,URLError,TimeoutError,ValueError) as e:
            attempts.append({'url':url,'status':'failed','error':str(e)})
            print('RETRIEVAL_FAILURE',url,str(e),flush=True)
    if received is None:
        result.append({'name':name,'attempts':attempts,'available':False})
        continue
    url,content,parsed=received
    raw=Path('/tmp')/('S6_SERIES_PUBLISH_c7_LL_historical_'+name+'.json')
    with raw.open('xb') as f:f.write(content)
    rows=parsed['rows']
    selected=[]
    for row in rows:
        key=tuple(row['key'])
        if key in keys:
            selected.append(row)
    required=7 if name=='fourfolds_D2_2power_AH' else 14
    assert len(selected)==required,(name,len(selected))
    entry={'name':name,'url':url,'raw_sha256':sha256(content).hexdigest(),
           'raw_bytes':len(content),'attempts':attempts,'available':True,
           'selected_LL_rows':selected,
           'scope':'Only seven LL keys; no historical algorithm executed.'}
    result.append(entry)
    print('RETRIEVED',name,'sha256',entry['raw_sha256'],'LL_ROWS',len(selected),flush=True)
    for row in selected:
        compact={'key':row['key']}
        for field in ['e','critical_linking','critical_link','refined_value_given_D44_proof',
                      'mu_mod_c','spin_lambda','remaining_refined_p']:
            if field in row:compact[field]=row[field]
        print(json.dumps(compact,sort_keys=True),flush=True)
output=LANE/'S6_SERIES_PUBLISH_III_02LL_historical_output_subset_v01.json'
with output.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print('SAVED_LL_SUBSET',str(output),sha256(output.read_bytes()).hexdigest(),flush=True)
