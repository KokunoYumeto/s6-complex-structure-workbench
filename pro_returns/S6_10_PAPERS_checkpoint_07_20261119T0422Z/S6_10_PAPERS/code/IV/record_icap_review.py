from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re
W=Path(__file__).resolve().parents[2];R=W.parents[1];A=W/'analysis/IV'
N=R/'sources/newer_night/checkpoint29';now=datetime.now(timezone.utc).isoformat()
checker='GPT-6 Astra Pro (OpenAI, ChatGPT; current writing, 18 November 2026)'
label='iv:i3_all_reduced_caps';source='notes/part3_e6_selected_i3_all_caps_working.md'
proof=W/'papers/IV/i3_all_reduced_caps.tex'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
sections=[
 {'step':'Original selected height','review':'Recomputed the full discriminant and both analytic roots, t_c(0)=0,t_o(0)=1/54. Substitution v=8s/(1+4s+sqrt(1+12s)) gives s=v(v+4)/(4(v-2)^2) and t_c=v/(v-2)^3, exactly the SI3 source/normal coordinate. The full root-height ratio H=(1-t_c z^m)/(1-t_o z^m), invariant under the whole deck, has its unique logarithm zero at z=0 and the prescribed mth root. The nonconstant h_o(0,z) is retained.'},
 {'step':'Root source and Cartier graph','review':'Re-derived the actual original-source map t=z^-m,x=z^-2(l+1)X,y=z^-3(l+1)Y, and explicitly identified the infinity coordinates x0=q_infty^2 x=z^(2k)X,y0=q_infty^3 y=z^(3k)Y. The full analytic inverse of 2zc=V-U and the three UV=X^3 charts retain s,z. The symbolic deck exponents and mR=G via R=2G-[m]^-1((2m-1)G) hold for every l. Read the full OC source, translation and Cartier input in its current K103 scope. Reconstructed the ideal(tau,z^k), each primitive adjacent ray, both actual point-line coefficients and their inverse module maps through section coincidence, keeping the total-family generators separate.'},
 {'step':'Full generator, norm and sector squares','review':'The normalized chord numerator at tau=0 equals its denominator generator, fixing the central-one lift and whole-fibre ambiguity. The original B6 central equality4z² gives Bc=4, with all horizontal/vertical orders accounted in the same normal charts. The full norm identities Bc=HBo,beta_c=Hbeta_o,Ftilde_c=H^(1/m)Ftilde_o hold because each source translation fixes H. The signed and finite-character generators retain A^m=B^n and J=A^n,J^m=B for n=±1; inverse coefficients are evaluated at the inverse source point. Substituted the complete Pi/Lambda/integer reference cochain equation into Phi; the relative partition/Cauchy solve fixes the prescribed reference and includes the full disc logH.'},
 {'step':'Proper relative cap product','review':'Re-derived the finite weighted-norm telescope from J^m=B, uniform strictness on each chosen joint disc, proper compact shell and freeness of the physical circle. Each cap uses its common strict scalar range with the quadratic reference; no uniform range over unbounded m is asserted. Pulling the same boundary field through the full Phi derivative, extending relatively, averaging and radial integration constructs the actual cap product with exactly that boundary. Both line and tangent maps and the original identity source closing are retained.'},
 {'step':'Signed topology and characteristic comparison','review':'Checked C_mn inverse and the exact integral relation-basis map T_mn with C_mn T_mn=C_2,+ for n²=1, retaining determinant signs. Made the sphere reference explicit by the ordered w-arc to -sqrt(3/2), which gives r=0,t_c=-4/27 with the original M6 and selected Hom map; the current F41/K96/K98 maps supply the complete endpoint and collars. The physical Euler restriction(0,-1), the unimodular orbit matrix and primitive rank-one conifold matrix carry the actual Hopf/Gysin orientation. Product connections on each five-dimensional cap quotient make x³ and p1 x vanish individually; identical exterior connections and full collar derivatives match all transgressions. The K68 selected Hopf completion is disjoint and keeps the original quaternion, line and Jin reversal, so both integer equalities use the same physical coordinates.'},
 {'step':'Full fan range and branch reflection','review':'The same selected exterior and tube retain every IVP source/line/normal/collar map and the actual AFI native products, q-dependent inverses, directed Cox resets and target systems. Induction along their finite canonical fan word therefore carries the exact integer, not only its residue, to every chosen cap. The already fully checked K106 28 witnesses remain actual words. The full point-theta arrow(Z,V)->(Z^-1,P^6 V), followed by its exact target period to(Q/Z,V), carries the second branch and J fan. Both marked positive w-meridians have degree1 over s, and vertical values are S_(1-j).'}
]
review={'label':label,'recorded_at':now,'checker':checker,'source_checkpoint':29,
 'source_file':str((N/source).relative_to(R)),'source_sha256':sha(N/source),
 'full_peer_file':str((N/'notes/part3_e6_selected_i3_all_caps_fourfold_peer.md').relative_to(R)),
 'full_peer_sha256':sha(N/'notes/part3_e6_selected_i3_all_caps_fourfold_peer.md'),
 'receiving_file':str(proof.relative_to(W)),'receiving_sha256':sha(proof),
 'verdict':'proved','sections':sections,
 'dependencies':['night:P3F.41','night:P3K.68','night:P3K.96','night:P3K.98','night:P3K.103','night:P3K.104','night:P3K.106'],
 'scope':'Every reduced M6 cap m=3l+2,l>=0,n=±1, admitted finite character/full prescribed reference, every selected lattice-basis fan and both marked branches. For each cap and reference choose their common strict scalar range. No M2 selected-I3 cap or additional endpoint claim.',
 'computation_receipt':'code/IV/replay_cp29_icap/current_results.json',
 'independence':'Current complete rederivation after reading both historical complete texts; no blind-review or human-review claim. Historical audits remain separate.'}
(A/'ICAP_current_review.json').write_text(json.dumps(review,indent=2,ensure_ascii=False)+'\n')
events=json.loads((A/'current_check_events.json').read_text())
assert not any(e['event_id'] in {'IV-D-072','IV-C-016','IV-S-001'} for e in events)
events.append({'event_id':'IV-D-072','type':'D','labels':[label],'verdict':'proved',
 'scope':review['scope'],'derivation':' '.join(x['step']+': '+x['review'] for x in sections),
 'checker':checker,'recorded_at':now,'source_checkpoint':29,'source_sha256':review['source_sha256'],
 'receiving_block_sha256':review['receiving_sha256'],'artifacts':['analysis/IV/ICAP_current_review.json',str(proof.relative_to(W))]})
events.append({'event_id':'IV-C-016','type':'C','labels':[label],'verdict':'PASS',
 'scope':'Two byte-identical CP29 certificate programs executed in an isolated retained clone; source symbolic maps and finite supplementary cases remain distinct from the complete geometric proof.',
 'derivation':'Root program5083 assertions and separate peer program973 assertions passed unchanged; complete SHA/time/output receipts at the linked path. No general conclusion is inferred from sampling alone.',
 'checker':checker,'recorded_at':now,'artifacts':['code/IV/replay_cp29_icap/source_manifest.json','code/IV/replay_cp29_icap/current_results.json']})
events.append({'event_id':'IV-S-001','type':'S','labels':['night:P3K.75'],'verdict':'Open; explicitly narrowed receiving scope',
 'scope':'Receiving obligations only: remove the precise fully proved K106, K107 and ICAP domains, retain all additional selected-I3 line/cap and singular-site/endpoint obligations.',
 'derivation':'K106 closes the quadratic M6 selected-I3 main/fan result; ICAP carries the two integers and full native maps to all M6 reduced caps and both norm signs; K107 closes the M2 order-three entire good-cap progression. Source K75 cp29 block remains historically unchanged/Open; no whole-proof or completed-classification verdict is assigned.',
 'checker':checker,'recorded_at':now,'source_checkpoint':29,
 'source_proof_sha256':'b26135ef230cee7d3ffc3a3a50fe4cb93403b8f456f98889f629a592735b76c2',
 'artifacts':['analysis/IV/checkpoint29_receiving_reconciliation.json','analysis/IV/ICAP_current_review.json','analysis/IV_K107/current_review.json']})
(A/'current_check_events.json').write_text(json.dumps(events,indent=2,ensure_ascii=False)+'\n')
def tsv(p,rows,cols):
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cols,delimiter='\t');w.writeheader()
  for row in rows:w.writerow({k:json.dumps(row[k],ensure_ascii=False) if isinstance(row.get(k),(list,dict)) else row.get(k,'') for k in cols})
tsv(A/'current_check_events.tsv',events,['event_id','type','labels','verdict','scope','derivation','checker','recorded_at','artifacts'])
searches=json.loads((A/'credit_searches.json').read_text())
source_paths=['work/S6_10_PAPERS/analysis/V/AC26_original_extracted.txt','sources/papers/arXiv_2609.38442_Engel_src/S6.tex','sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie.tex','sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie.tex','work/S6_10_PAPERS/analysis/IV/references/Jin2026v2.txt','work/S6_10_PAPERS/analysis/IV/references/ViacCombs_current.txt']
for lab,terms in [(label,[r'selected[- ]I.?3',r'reduced cap',r'primitive norm',r'47\s*,\s*-4',r'monodromy']),('night:P3K.107',[r'order[- ]three',r'three.*translat',r'good cap',r'-3\s*,\s*-12',r'monodromy',r'fan'])]:
 sources=[]
 for rel in source_paths:
  p=R/rel;lines=p.read_text().splitlines();hits=[]
  for term in terms:
   found=[{'line':i,'text':line.strip()[:320]} for i,line in enumerate(lines,1) if re.search(term,line,re.I)]
   hits.append({'term':term,'count':len(found),'first_locators':found[:6]})
  sources.append({'file':rel,'sha256':sha(p),'hits':hits})
 rec=next((x for x in searches if x.get('label')==lab),None)
 if rec is None:rec={'label':lab,'paper':'IV','event_type':'bounded_current_credit_search','checker':checker};searches.append(rec)
 rec.update(recorded_at=now,terms=terms,sources=sources,assessment='No identical full source/cap/fan theorem was established by these bounded searches. Exact source and standard input credits remain stated in the proof; absence of a matched theorem is not a novelty verdict.',related_material_read='ICAP complete original and full peer texts currently rederived; K107 complete main+19 supporting texts independently reviewed at IV-INV-D-010. Standard equivariant integration, line comparison and local-group source loci retain their existing bounded current records; no new external whole-proof reading inferred.')
(A/'credit_searches.json').write_text(json.dumps(searches,indent=2,ensure_ascii=False)+'\n')
tsv(A/'credit_searches.tsv',searches,['label','paper','event_type','recorded_at','checker','terms','assessment','related_material_read','sources'])
print(json.dumps({'recorded_at':now,'proof_event':'IV-D-072','receiving_sha256':sha(proof),'source_sha256':review['source_sha256']}))
