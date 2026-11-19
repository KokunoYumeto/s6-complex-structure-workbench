from pathlib import Path
import csv,datetime,json,hashlib
B=Path('/workspace/scratch/490d8ca4e928');W=B/'work/S6_10_PAPERS';A=W/'analysis/IV_K107';now=datetime.datetime.now(datetime.timezone.utc).isoformat()
uses=[
 ('night:P3F.41','SC.1 exact E6-B (a,b)=(2,3), m=3l good-root, n=±1 standard-sphere/cap data; actual source/orbit application through the specified ordered-rho interval.'),
 ('night:P3K.23','Only the retained quaternion common-link products, relative generators, exact conjugation and oriented commutator. The rejected -5A physical assertion is excluded.'),
 ('night:P3K.29','Only primitive integral common-exterior/relative-dual bases, variation symmetry and exact frame-change pairing. The rejected simultaneous scalar plumbing assertion is excluded.'),
 ('night:P3K.31','Only local derivative shear/product-frame comparison and the explicit complex normal reset J; no withdrawn scalar-fan polynomial or initial data is used.'),
 ('night:P3K.50','OR.2 actual bottom-and-side cylinder retraction and inverse-gauge endpoint extension. K107 uses the contraction of its own zero-degree disc-extending normal arrows; no old central label or L^6 value is imported.'),
 ('night:P3K.51','CT.3 integral graph-loop/relative-two-chain construction, endpoint caps and exact action-prism boundary identity. K107 substitutes its actual weights and zero local trace degrees.'),
 ('night:P3K.52','ST.1 exact stable-derivative prism, closed Spin lift and chain-rule signs, together with the extending local/ambient frame comparison. No old central class is imported.'),
 ('night:P3K.55','GF.2 normal-rescaling and protected-collar extension; GF.3 full Spin endpoint parity; GF.18–19 integral weighted trace/prism identities. The scalar-family values in GF.8/16/17 are not used for this disc-extending M2 family.'),
 ('night:P3K.57','IE.4,IE.5 and IE.7 local weighted normal-link/Stokes derivation only; the actual physical line is converted by K68. Whole source compound remains Refuted.'),
 ('night:P3K.68','PL.1–6 exact physical line/Hermitian dual, normal orientations, both cap maps, Hopf transfer and literal first-to-second inverse clutch.'),
 ('night:P3K.95','EC.25 source/root/Cartier interval and primitive orbit-filling argument, applied with the explicit M2,-3G,six-factor Hom data in the MO.6 replacement.'),
 ('night:P3K.96','EX.1–5 actual E6-B endpoint extension through the unselected type III fibre, M2 good-root Cartier correction and complete translation/norm lift; its full source coordinates are retained.'),
 ('night:P3K.103','OC.8 exact tau(3G) rational coordinate; OC.17–19 full annular cochains and inverses; OC.4 weighted contracting norm and relative cap product. K107 inserts its actual M2 data and compares each chosen good cap with its (3,1) good reference.')]
idx=json.loads((W/'analysis/inventory_source_index.json').read_text());deps=[]
for label,scope in uses:
 key='S6_06_BLIND:'+label.removeprefix('night:');loc=idx[key];p=B/loc['file'];t=p.read_text()
 deps.append({'label':label,'scope':scope,'source_file':loc['file'],'source_file_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'source_block_sha256':hashlib.sha256(t[loc['start']:loc['end']].encode()).hexdigest(),'review':'Operative passage and actual K107 application read; no whole-proof credit on the dependency is inferred.'})
obj={'label':'night:P3K.107','recorded_at':now,'uses':deps,'provenance_only':[{'label':'night:P3K.99','scope':'Same explicitly stated selected-node marking and E64/E81 foundational text reproduced completely in K107; K107 supplies its own M2 construction and complete calculation. No M6 numerical result is transferred.'}],'external_source_record_reuse':['IV-R-030','IV-R-004','IV-R-005']}
(A/'uses.json').write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
review=json.loads((A/'current_review.json').read_text());review['recorded_at']=now;review['final_dependency_review_at']=now;review['uses_record']='analysis/IV_K107/uses.json';review['operative_dependency_scope'].append('Further complete application checks: K50 OR.2 cylinder retraction, K51 CT.3 action prism, K52 ST.1 derivative prism, K55 GF.2–4 exact weighted trace/Spin framework, and K103 OC.8/OC.17–19 weighted norm/reference product. All actual K107 source, full-unit and boundary maps were substituted; scalar-family numerical data are excluded.')
(A/'current_review.json').write_text(json.dumps(review,indent=2,ensure_ascii=False)+'\n')
events=json.loads((A/'current_events.json').read_text())
for e in events:
 e['date']=now
 if e['event_id']=='IV-INV-D-010':
  e['scope']+=' Exact final dependency roles are in analysis/IV_K107/uses.json.'
  e['derivation']+=' The complete native-to-ordinary inverse-gauge cylinder and the graph/action/stable-derivative prism identities were also checked in K50 OR.2, K51 CT.3, K52 ST.1 and K55 GF.2–4. K103 OC.8 and OC.17–19 supply the exact tau(3G) coordinate, cochain square and weighted contraction norm with the actual M2 inputs.'
(A/'current_events.json').write_text(json.dumps(events,indent=2,ensure_ascii=False)+'\n')
with (W/'records/IV_K107_events.tsv').open('w',newline='') as f:
 wr=csv.DictWriter(f,fieldnames=list(events[0]),delimiter='\t');wr.writeheader();wr.writerows(events)
rp=A/'receiving_replacements.json';r=json.loads(rp.read_text());r['recorded_at']=now;rp.write_text(json.dumps(r,indent=2)+'\n')
md=A/'review.md';text=md.read_text();text+='\n## Final local dependency applications\n\n'+ '\n\n'.join('**'+label+'**: '+scope for label,scope in uses)+'\n\nFinal dependency application recording time: '+now+'. The single current full-proof event has this final time; the earlier draft timestamp remains only in the construction log.\n';md.write_text(text)
p=W/'analysis/inventory_overrides.json';over=json.loads(p.read_text());o=over.setdefault('S6_06_BLIND:P3K.107',{});o['main_or_supporting']='main';o['uses']='; '.join(label for label,scope in uses);o.setdefault('_notes',{}).update({'main_placement_reason':'Completed M2 order-three source return and full sixteen-class fan image; whole corrected export currently rederived with exact source/cap/reference maps.','current_full_export_review':'analysis/IV_K107/current_review.json','current_export_uses':'analysis/IV_K107/uses.json','receiving_corrections_required':'analysis/IV_K107/receiving_replacements.json','receiving_integration_pending':True});p.write_text(json.dumps(over,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'final_recorded_at':now,'whole_proof_event':'IV-INV-D-010','uses':len(uses),'receiving_integration_pending':True}))
