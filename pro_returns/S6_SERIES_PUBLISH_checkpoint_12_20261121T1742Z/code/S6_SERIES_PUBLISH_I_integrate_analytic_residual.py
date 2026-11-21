from pathlib import Path
import json,datetime,hashlib
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1];ed=Editor('I')
p=r/'agents/i_analytic/S6_SERIES_PUBLISH_I_residual_guards.json';d=json.loads(p.read_text())
for x in d['guards']:
 kind='D16' if int(x['id'].rsplit('-',1)[1])>=14 else 'D09' if x['id'] in ['IA-RES-01','IA-RES-02','IA-RES-03','IA-RES-09'] else 'D07'
 ed.replace(x['old'],x['new'],kind,x['reason'],x['id'],x['expected_count'])
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_analytic_residual_integration.json').write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(ed.text.encode()).hexdigest(),'guard_file':str(p.relative_to(r)),'guard_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'guards':len(d['guards']),'scope':'Root read all new passages and the complete scoped comparison, including the three explicit A2.2 chart morphisms and source-parameter map. Source records retain the full removed proofs/metadata and three exposed reread events; no additional root independent event. Exact same-edition bibliography alias map is preserved.','bibliography_aliases':{'DuGuoKusakabeXie2026v1':'DuEtAl2026v1','Grauert1960D':'Grauert60','SS00':'SchroeerSiebert2002Root'},'remaining_bibliographic_flag':'BM95AB/BM97 remain as supplied preprint/journal edition records; the operative pagination is explicitly the Chapter I preprint. No unverified edition merge is asserted.'},indent=2)+'\n')
