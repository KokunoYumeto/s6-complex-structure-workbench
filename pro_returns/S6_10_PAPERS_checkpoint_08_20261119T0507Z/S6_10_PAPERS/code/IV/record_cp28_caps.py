"""Completed mathematical reviews; their certificate executions are separate."""
from pathlib import Path
import csv,datetime,hashlib,json,re
W=Path(__file__).resolve().parents[2];R=W.parents[1];A=W/'analysis/IV'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checker='GPT-6 Astra Pro (OpenAI, ChatGPT; current writing, 18 November 2026)'
events=json.loads((A/'current_check_events.json').read_text())
idx=json.loads((W/'analysis/inventory_source_index.json').read_text())
blocks={v.get('label'):v for v in idx.values() if isinstance(v,dict)}
data=[
 ('IV-D-056','night:P3K.104','Complete selected-infinity reduced-cap progression and both signed norms',
  'Read and rederived the entire HC.1–5 proof and the complete SN.1–6 negative-quadratic companion. For m=3l+2,k=2l+1, the literal root substitution gives the full reduced IV equation and the three UV=X³ charts, with the displayed analytic inverse for the original base coordinate. The full chord translation, R=2G−[m]^{-1}((2m−1)G), gives mR=G; its Cartier comparison has every primitive ray(j,1), the actual units u/(u−L),1/(1−vL), and their module inverses. Re-derived the Miller exponent, the entire selected-height ratio(1−tc z^m)/(1−tr z^m), its normalized logarithmic root, the chord lift with central coefficient1 and the full norm coefficient4. Kept every finite character, both norms A^m=B^n and the unrestricted four-sector word A^4B^J. The signed target-sheet Lie identity retains the period cochain; the reference-relative Cauchy correction gives the full holomorphic annular arrow in the even parameter. The original cap remains on its actual large-sigma domain. The native/original map, residual quarter action and inverse endpoint retain all source and point-line coefficients. The weighted Hermitian norm proves contraction for H=A^n, H^m=B, giving a proper free cap and a free physical circle. Pushed the prescribed boundary horizontal fields through the full annular derivative, extended and circle-averaged them, and integrated over the actual parameter disc; this constructs the cap product with its required boundary and line map. The five-dimensional quotient body has vanishing product degree-six forms. Matched connections on the identical exterior and collars prove equality of each integer characteristic number. Re-derived the exact signed meridian inverse and reference change of basis, the fixed physical Euler restriction, the separate orbit and conifold restriction matrices, the primitive kernel/cokernel and the selected unknotted Hopf replacement. K68 then gives the actual physical-return convention. The ordinary K101 exterior is literally unchanged and the fan maps are the identity on the transported cap; the full theta reflection retains its target period. Hence every stated signed cap has initial pair(−4,8), native pair(2,−6), vertical pair(−4−12j(j−1),8) and precisely the K102 directed all-fan algorithm and fourteen odd values. The negative quadratic companion independently supplies the actual signed annular reference, contraction, cap-meridian basis and physical Euler map.'),
 ('IV-D-057','night:P3K.105','Complete M2 selected-infinity construction, every good cap and the full odd-ideal attachment',
  'Read and rederived every MB.1–7, MG.1–5 and MI.1–4 proof step. The construction begins with the actual M2 line and the three chronological translations by−G. The six Miller factors and single selected-height factor give the full genuine point-line period; all horizontal divisor and zero-section module factors are retained. Re-derived the complete three-chord source reset, its homogeneous O(−k) lift, the full point-to-theta ratio and divided differences, ordinary/selected character matrices and their inverses, native I2 unit maps and quarter action. The two O/T surface orbits and every residual stabilizer are computed from those maps. Read every chart and normal-row certificate. The strict, odd-point, interior, exceptional, refinement, p-chart, interface and moving contributions sum as separate integers to U pair(−4,8). The moving-cap comparison retains the two point/tensor maps, source framing and full phase diag(−2,2); its common scalar phase extends and its held-Cox conjugacy leaves the actual non-scalar phase diag(−4,0), giving c2=−4 with the explicitly reversed parameter coordinate. The actual dual-line, outer-boundary and Jin-interval arrows then give physical pair(−4,8), native pair(2,−6) and integer−1. For every m=3l the kernel quotient gives the smooth cubic root; both exact section equations and both E_P−E_O corrections are retained in the three quotient charts and their primitive pullback rays. The formal section R=[m]^{-1}(3G) preserves the full graph ideals with its inverse. Its normalized chord lift has central coefficient1; the complete selected Miller norm has coefficient4. Every signed norm, scalar root and finite character survives the reference-relative annular cochain and both endpoint directions. The weighted norm, compact graph/parallelogram domains and exact face pairings give the proper free quotient and the prescribed relative cap product. Its matched product connections preserve each characteristic integer. The separate Hopf orbit/conifold maps fix the physical line and cap orientation. All ordinary period windings and full fan prism maps agree through the explicit coefficient arrows with K102, giving every stated vertical and general fan value. Finally re-derived the complete three-step odd ideal matrix, including its neutral mixing term S3*u, central values K3=1,S3=6, physical weights, adjacent neutral/odd coordinate map, quotient blowup charts and inverse; this verifies the actual remaining two-torsion attachment rather than a diagonal substitute. No return is inferred by dividing through the auxiliary cubic-cover map.')]
for eid,label,scope,derivation in data:
 assert not any(e['event_id']==eid for e in events),eid
 b=blocks[label]
 events.append(dict(event_id=eid,type='D',labels=[label],verdict='proved',scope=scope,
  derivation=derivation,checker=checker,recorded_at=now,source_checkpoint=28,
  source_block_sha256={label:hashlib.sha256((R/b['file']).read_text()[b['start']:b['end']].encode()).hexdigest()},
  source_file_sha256={label:b['sha256']},artifacts=['papers/IV/body.tex','code/IV/replay_cp28_caps/current_execution.json']))
events.append(dict(event_id='IV-C-013',type='C',labels=['night:P3K.104','night:P3K.105'],verdict='pass',
 scope='Five complete received program reads and current unchanged-byte executions',
 derivation='Read all five complete main programs, then executed byte-verified isolated copies at04:55:35–04:55:42UTC. negative_norm:3608 checks; reduced_caps:6870; m2_branch:2830; m2_odd_ideal:548; good_caps:4131. Every process exited0 and every certificate passed. The input ledger records source/copy hashes of all read inputs; current output hashes and exact stdout/stderr are separate. Symbolic identities include unrestricted cap exponents, annular cochains and parameter matrices; finite chart/character samples are identified as finite. These executions do not replace the geometric cap product, compactness or orientation proofs.',
 checker=checker,recorded_at=now,artifacts=['code/IV/replay_cp28_caps/input_manifest.json','code/IV/replay_cp28_caps/current_execution.json']))
b=blocks['night:P3K.75']
events.append(dict(event_id='IV-E-010',type='E',labels=['night:P3K.75'],verdict='open obligations reviewed; no theorem closure',
 scope='Checkpoint28 exact completed-versus-outstanding source-return audit',
 derivation='Read the full updated statement and its retained historical record. K104 closes the selected-infinity M6 reduced progression m=3l+2 with both norm signs and every retained character/reference/fan. K105 closes the entire selected-infinity M2 progression m=3l with both norm signs and every retained character/reference/fan. Thus these two previously outstanding selected-infinity cap scopes are removed. K75 remains Open: the M2 order-three base return, both selected-I3 generators and their remaining cap/norm/fan scopes, and additional singular-site/endpoint scopes still require their own full comparison maps. Historical attempted attachments remain identified as history; no current reading credit is assigned to an earlier source merely because K75 cites it.',
 checker=checker,recorded_at=now,source_checkpoint=28,
 source_block_sha256={'night:P3K.75':hashlib.sha256((R/b['file']).read_text()[b['start']:b['end']].encode()).hexdigest()},
 artifacts=['analysis/IV/checkpoint04_gate_review.json']))
def tsv(path,rows,cols):
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=cols,delimiter='\t');w.writeheader()
  for e in rows:w.writerow({k:json.dumps(e[k],ensure_ascii=False) if isinstance(e.get(k),(list,dict)) else e.get(k,'') for k in cols})
(A/'current_check_events.json').write_text(json.dumps(events,indent=2)+'\n')
tsv(A/'current_check_events.tsv',events,['event_id','type','labels','verdict','scope','derivation','checker','recorded_at','artifacts'])
searches=json.loads((A/'credit_searches.json').read_text())
paths=['work/S6_10_PAPERS/analysis/V/AC26_original_extracted.txt','sources/papers/arXiv_2609.38442_Engel_src/S6.tex','sources/papers/arXiv_2610.00250v1_Du_Guo_Kusakabe_Xie.tex','sources/papers/arXiv_2610.00250v2_Du_Guo_Kusakabe_Xie.tex','work/S6_10_PAPERS/analysis/IV/references/Jin2026v2.txt','work/S6_10_PAPERS/analysis/IV/references/ViacCombs_current.txt']
for label,terms in [('night:P3K.104',['selected.infinity','reduced.cap','annular','characteristic','monodromy']),('night:P3K.105',['three.step','three.*translat','good.cap','point.*theta','odd.ideal','infinity'])]:
 sources=[]
 for rel in paths:
  p=R/rel;lines=p.read_text().splitlines();hits=[]
  for term in terms:
   found=[dict(line=i,text=x.strip()[:320]) for i,x in enumerate(lines,1) if re.search(term,x,re.I)]
   hits.append(dict(term=term,count=len(found),first_locators=found[:6]))
  sources.append(dict(file=rel,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),hits=hits))
 assessment='No identical full selected-infinity cap theorem was established by these bounded searches of the AC original, Engel, DGKX v1/v2, Jin v2 and Viaclovsky Combs. The source and coefficient construction is proved in the exact checkpoint28 block; the standard equivariant integration input is Atiyah–Bott Theorem3.5 and equation3.8 pp8–9, and the physical return transfer uses the separately opened Jin v2 exact loci. Search absence is not a novelty verdict.'
 rec=dict(label=label,paper='IV',event_type='current credit search',recorded_at=now,checker=checker,
  terms=terms,sources=sources,assessment=assessment,
  related_material_read='Entire checkpoint28 theorem and every companion proof; all five new main programs; original Atiyah–Bott pp8–9. Earlier exact Jin/Engel/Viaclovsky source reads remain scoped in reference_checks.json.')
 old=next((i for i,x in enumerate(searches) if x.get('label')==label),None)
 if old is None:searches.append(rec)
 else:searches[old]=rec
(A/'credit_searches.json').write_text(json.dumps(searches,indent=2)+'\n')
tsv(A/'credit_searches.tsv',searches,['label','paper','event_type','recorded_at','checker','terms','assessment','related_material_read','sources'])
(A/'checkpoint04_gate_review.json').write_text(json.dumps(dict(recorded_at=now,source_checkpoint=28,
 gate_movement=[dict(label=x[1],event_id=x[0],scope=x[2],result='Closed by complete current proof review') for x in data],
 remaining_open='P3K.75 remains Open: M2 order-three base return; both selected-I3 generators and their remaining cap/norm/fan scopes; additional singular-site/endpoint scopes.',
 exact_reduction='All selected-infinity caps in the two progressions (M6,b1;m=3l+2) and (M2,b3;m=3l), both primitive norm signs, every retained finite character/full annular reference and selected lattice fan, are now completed.',
 exclusions='Packaging, layout, credit searches and older topology discrepancy repairs do not count as movement of this open mathematical gate.'),indent=2)+'\n')
print(json.dumps(dict(recorded_at=now,D_events=sum(e['type']=='D' for e in events),D_labels=len({l for e in events if e['type']=='D' for l in e['labels']}),new_proof_events=[x[0] for x in data])))
