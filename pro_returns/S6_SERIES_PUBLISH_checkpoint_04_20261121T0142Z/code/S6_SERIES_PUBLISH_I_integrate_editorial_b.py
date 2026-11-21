from pathlib import Path
import json,hashlib,datetime
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1]
p=r/'agents/i_analytic/S6_SERIES_PUBLISH_I_editorial_batch_b_guards.json'
d=json.loads(p.read_text());ed=Editor('I')
for x in d['guards']:
    ed.replace(x['old'],x['new'],'D12' if x['id'] in {'IA-B-06','IA-B-07','IA-B-08','IA-B-09'} else 'D09',
               x['reason'],x['id'],count=x.get('expected_count',1))
ed.save()
(r/'records/S6_SERIES_PUBLISH_I_editorial_b_integration.json').write_text(json.dumps({
    'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'guard_source':str(p.relative_to(r)),
    'guards_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
    'root_comparison':'All fourteen complete old/new guards actually read before integration. The two local expansion proofs preserve every displayed coefficient and exact lattice/root-coordinate map. The earlier differential-identity proof replaces the repeated differentiation in the equianharmonic proof.',
    'scope':'Presentation/proof-comparison only; no new independent derivation or computation is claimed by this integration.',
    'changes':['Restore the exact Siegel-function/local-height application.',
       'State the exact general-Weierstrass to short-model coordinate transport.',
       'Replace numerical agreement by the existing squarefree-polynomial root count.',
       'Move derivative identities and finite local expansions before the local/global maximum arguments.',
       'Retain polynomial recurrences and analytic inequalities while relocating program narration to records.']
},indent=2)+'\n')
