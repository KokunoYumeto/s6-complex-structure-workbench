#!/usr/bin/env python3
"""Retain the actual follow-up retrievals and expose only needed helpers.
The full other helper modules are cached/parsed, not printed or executed.
"""
from pathlib import Path
from hashlib import sha1,sha256
from datetime import datetime,timezone
from itertools import islice
import ast,base64,json
ROOT=Path(__file__).resolve().parents[1]
LANE=ROOT/'agents/continuation7_iii_star_logs_receiving'
P='S6_SERIES_PUBLISH_III_02LQ_'
calls=json.loads((ROOT/'code/S6_SERIES_PUBLISH_c7_lq_historical_fetch_followups_v1.tool_result.json').read_text())
want={'manifolds_rankone_families.py':['decomp','ikernel','wedge','biv','bezout'],
      'manifolds_general_initial.py':['integer_solution'],
      'manifolds_weighted_profiles.py':['group']}
for call in calls:
    assert call['status']=='fulfilled'
    item=call['value']; response=item['response']; data=response['structuredContent']
    assert response['isError'] is False and data['encoding']=='base64'
    name=Path(item['request']['path']).name
    if name=='manifolds_star_log_caps.json':
        assert data['content']==''
        print('FETCH_FILE CONTENT ABSENT for nonempty blob',data['sha'],'retained as actual connector result')
        continue
    raw=base64.b64decode(data['content'])
    assert sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==data['sha']
    path=LANE/(P+'historical_'+name); assert not path.exists(); path.write_bytes(raw)
    print('RETAINED',name,'bytes',len(raw),'lines',len(raw.splitlines()),'SHA256',sha256(raw).hexdigest())
    if name in want:
        source=raw.decode(); tree=ast.parse(source)
        imports=[node for node in tree.body if isinstance(node,(ast.Import,ast.ImportFrom))]
        print('IMPORT_METADATA',ast.unparse(ast.Module(body=imports,type_ignores=[])))
        for function in want[name]:
            node=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name==function)
            text='\n'.join(source.splitlines()[node.lineno-1:node.end_lineno])+'\n'
            dest=LANE/(P+'historical_helper_'+function+'.py'); dest.write_text(text)
            print('EXACT_HELPER',name,node.lineno,node.end_lineno,function)
            print(text,end='')
            print('CALLED_NAMES',sorted({x.func.id for x in ast.walk(node) if isinstance(x,ast.Call) and isinstance(x.func,ast.Name)}))
blob=json.loads((ROOT/'code/S6_SERIES_PUBLISH_c7_lq_historical_fetch_blob_v1.tool_result.json').read_text())
assert blob['response']['isError'] is False
raw=blob['response']['structuredContent']['content'].encode('utf-8')
assert sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==blob['request']['blob_sha']
out=LANE/(P+'historical_manifolds_star_log_caps.json'); assert not out.exists(); out.write_bytes(raw)
print('RETAINED_TARGET_OUTPUT',len(raw),len(raw.splitlines()),sha256(raw).hexdigest())
canonical=ROOT/'S6_SERIES_PUBLISH_III.tex'
assert sha256(canonical.read_bytes()).hexdigest()=='9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
with canonical.open() as f: lines=list(islice(f,20692,20712))
used=[i for i,x in enumerate(lines) if x.strip()]
first,last=used[0],used[-1]
aux=''.join(lines[first:last+1]).rstrip('\n')
(LANE/(P+'released_following_auxiliary.tex')).write_text(aux+'\n')
print('AUXILIARY_INTERVAL',20693+first,20693+last,sha256(aux.encode()).hexdigest())
print(aux)
print('PASS',datetime.now(timezone.utc).isoformat())
