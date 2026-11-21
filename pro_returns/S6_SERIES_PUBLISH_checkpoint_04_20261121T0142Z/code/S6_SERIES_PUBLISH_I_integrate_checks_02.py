from pathlib import Path
import csv,datetime,hashlib,json
from S6_SERIES_PUBLISH_editing import Editor
r=Path(__file__).resolve().parents[1]
ed=Editor('I')
g=json.loads((r/'agents/i_provenance/S6_SERIES_PUBLISH_I_primary_citation_guards_01.json').read_text())
for x in g['changes']:
 ed.replace(x['old'],x['new'],'D24' if 'series-order' in x['id'] else 'D18',x['reason'],x['id'],count=x.get('expected_count',1))
ed.save()
g=json.loads((r/'agents/i_provenance/S6_SERIES_PUBLISH_I_shared_bib_guards_01.json').read_text())
p=r/'S6_SERIES_PUBLISH_references.bib';s=p.read_text();old=s
for x in g['changes']:
 assert s.count(x['old'])==x.get('expected_count',1)
 s=s.replace(x['old'],x['new'])
p.write_text(s)
(r/'records/S6_SERIES_PUBLISH_I_bibliography_guard_receipt.json').write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'before_sha256':hashlib.sha256(old.encode()).hexdigest(),'after_sha256':hashlib.sha256(s.encode()).hexdigest(),'source_guard':'agents/i_provenance/S6_SERIES_PUBLISH_I_shared_bib_guards_01.json'},indent=2)+'\n')

comparison={
 'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'label':'inv:D4.2','outcome':'All statements and both printed proof steps agree.',
 'step_1':[
 'The printed rank-one local system has the exact character (exp(2 pi i z),1) independently derived from the marked deck quotient. Its scalar Koszul maps agree up to the explicit sign convention on the second differential.',
 'The preread proof directly computes the rank-three logarithmic tangent representation and its contracting homotopy, whereas the printed proof obtains logarithmic tangent acyclicity from scalar twist acyclicity and the vertical tangent extension. Both yield vanishing of every direct-image stalk near the cusp.',
 'The preread local maps T/T(-log W) to the branch normal modules identify the quotient with nu_*K_S, exactly the input (D.10) used in the printed proof. Pullback of the twist is trivial on the rational normalization. H2(K_S)=C and the normal quotient is annihilated by q, proving the full length-one module.'
 ],
 'step_2':'The exceptional regular/root-fibre parameters remain the stated input inv:D4.3. Torus-twist acyclicity and root-atlas invariant descent give all other zero stalks; Leray on the base curve gives (0,0,1,0). No new blind credit is claimed for inv:D4.3.',
 'mathematical_disagreement':None,
 'scope':'Complete alternate derivation of the cusp module calculation from the toric model, including the exact normal quotient, followed by comparison with both target proof steps. Generic exceptional-set identification is an explicit established input.'}
(r/'records/S6_SERIES_PUBLISH_I_D42_comparison.json').write_text(json.dumps(comparison,indent=2)+'\n')
cols=['statement_id','date','who','type','outcome','event_id','phase','source_file','source_row','source_event_type','evidence_group']
rows=[]
for k,(typ,outcome,evidence) in enumerate([
 ('independent re-proof','PASS: complete preread alternate proof of the cusp module from the marked periodic toric model. Derived the character (exp(2pi iz),1), rank-three logarithmic tangent monodromy, explicit contraction, exact normal quotient nu_*K_S and its q-annihilated degree-two direct image. Compared both printed steps; generic regular/root exclusion is the explicit inv:D4.3 input. All conclusions agree.','records/S6_SERIES_PUBLISH_I_D42_comparison.json'),
 ('computation or formal certificate','PASS: exact symbolic rank-three Koszul complex with A=aU_gamma-I and B=U_u-I; det A=(a-1)^3. Verified d1d0=0 and all three contracting-homotopy identities over Q(a). This recomputes the vanishing directly for the logarithmic tangent representation, compared with the printed scalar-line/extension route.','records/S6_SERIES_PUBLISH_I_D42_preread_computation.json')],1):
 h=hashlib.sha256((typ+evidence).encode()).hexdigest()[:16]
 rows.append(dict(zip(cols,['inv:D4.2','2026-11-21','GPT-6 Astra (OpenAI), ChatGPT Pro mode; reasoning effort inherited, no separate numerical setting exposed; S6_SERIES_PUBLISH root',typ,outcome,'ce:publish-I-D42-'+h,'S6_SERIES_PUBLISH_I','work/'+evidence,str(k),typ,'eg:publish-I-D42-'+h])))
with (r/'records/S6_SERIES_PUBLISH_I_root_D42_CHECK_EVENTS.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=cols,delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'D42_comparison':'complete','new_event_rows':len(rows),'citation_guards':len(g['changes'])}))
