#!/usr/bin/env python3
"""Decode the actually retrieved LQ historical source; retain exact bytes."""
from pathlib import Path
from hashlib import sha1,sha256
from datetime import datetime,timezone
import base64,json
ROOT=Path(__file__).resolve().parents[1]
calls=json.loads((ROOT/'code/S6_SERIES_PUBLISH_c7_lq_historical_fetch_v1.tool_result.json').read_text())
for item in calls:
    assert item['request']['ref']=='a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7'
    response=item['response']; assert response['isError'] is False
    data=response['structuredContent']; assert data['encoding']=='base64'
    raw=base64.b64decode(data['content'])
    assert sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==data['sha']
    p=ROOT/'agents/continuation7_iii_star_logs_receiving'/('S6_SERIES_PUBLISH_III_02LQ_historical_'+Path(item['request']['path']).name)
    assert not p.exists(); p.write_bytes(raw)
    print('RETAINED',p.name,'bytes',len(raw),'lines',len(raw.splitlines()))
    print('GIT_BLOB',data['sha'],'SHA256',sha256(raw).hexdigest())
print('PASS',datetime.now(timezone.utc).isoformat())
