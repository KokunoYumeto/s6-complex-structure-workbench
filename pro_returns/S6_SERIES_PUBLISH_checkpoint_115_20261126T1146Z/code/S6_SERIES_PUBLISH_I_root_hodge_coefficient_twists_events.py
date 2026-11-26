from pathlib import Path
import csv,json,hashlib,datetime
r=Path(__file__).resolve().parents[1]
fields=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group']
rows=[]
groups=[
 ('hodge','S6_SERIES_PUBLISH_I_hodge_editorial_comparison.json',None),
 ('coefficient','S6_SERIES_PUBLISH_I_coefficient_editorial_comparison.json',['inv:C3.8','inv:C3.8:operator-comparison','wb:rem:bcpr-literal-gauge','wb:rem:bcpr-global-gauge-boundary','fam:src:A.3.1']),
 ('twists','S6_SERIES_PUBLISH_I_twists_editorial_comparison.json',None),
 ('classification-collar','S6_SERIES_PUBLISH_I_classification_collar_comparison.json',['night:P5.6','fam:src:A.5.1','inv:C3.2','inv:A2.1'])]
for group,name,labels in groups:
 p=r/'records'/name;d=json.loads(p.read_text());sha=hashlib.sha256(p.read_bytes()).hexdigest()
 if labels is None: labels=list(d['proofs'])
 for lab in labels:
  if lab=='inv:C3.5':continue  # Heading only; no complete proof comparison in this batch.
  scope=d['scope']
  if lab=='fam:src:A.3.1':
   scope='Bounded exposed reread of the toric cusp-cover step against its exact attached-compendium chart-control proof: logarithmic barycentric coordinates, quotient-fan cone cover, and compact finite-subcover argument. No additional whole-proof or independent credit.'
  elif group=='coefficient' and lab!='inv:C3.8':
   scope='Complete exposed reread of the Green/harmonic comparison or the indicated coefficient-gauge passage, as recorded in the coefficient editorial receipt. All gauge weights, cocycle coboundaries and operator formulas retained. No independent derivation claimed.'
  rows.append(dict(zip(fields,[lab,'2026-11-21',
   'GPT-6 Astra (OpenAI), ChatGPT Pro mode, inherited effort; S6_SERIES_PUBLISH root',
   'used and rechecked in this run','PASS: '+scope,
   'publish-I-root-editorial-'+group+'-'+hashlib.sha256(lab.encode()).hexdigest()[:12],
   'Paper I publication comparison',str(p),'','used and rechecked in this run',
   'publish-I-root-editorial-'+group+'-'+sha[:16]])))
out=r/'records/S6_SERIES_PUBLISH_I_root_hodge_coefficient_twists_CHECK_EVENTS.tsv'
assert not out.exists()
with out.open('w') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'rows':len(rows),'evidence_groups':len(groups),'path':str(out)}))
