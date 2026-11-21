"""Archive the exact official equations personally opened for the setup maps."""
from pathlib import Path
import urllib.request,hashlib,json,datetime,concurrent.futures
B=Path(__file__).parent/'literature'
locators=['20.7.E26','20.7.E30','23.18.E5','23.18.E6']
def get(loc):
 url='https://dlmf.nist.gov/'+loc+'.tex'
 with urllib.request.urlopen(url,timeout=30) as r: data=r.read();status=r.status
 p=B/('S6_SERIES_PUBLISH_I_DLMF_'+loc.replace('.','_')+'.tex');p.write_bytes(data)
 return {'locator':loc,'url':url,'http_status':status,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'path':str(p.resolve())}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(get,locators))
r={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'actually_opened_scope':'Official rendered-HTML math at DLMF20.7.26 and20.7.30 (theta translation/inversion, pi-period convention),23.18.5–6 (eta modular law/unit multiplier). The eta translation law follows directly from the printed product. The general SL2 basis identity is their composition; no full DLMF chapter reading claimed.',
 'web_evidence_refs':['turn195026803view0','turn195026803view1','turn189990655view0'],
 'equations':rows,'mathematical_event_credit':False}
(B/'S6_SERIES_PUBLISH_I_DLMF_setup_scope_receipt.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(rows,indent=2))
