"""Exact attached-source matches and safe aliases, never surname-only matches."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3];W=ROOT/'deliverables/work/maps_audit'
META=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')
specs=[
 ('mapsEngel','Engel2026','sources/papers/arXiv_2609.38442_Engel_src/S6.tex',
  ['Lemma2.1 complete proof, source334–392; original rational elliptic surface setup288–334',
   'Lemma3.8 source842–863 and Remark8.3 source1685–1723, previously opened in the PaperI current-reader credit matrix; Remark8.3 reopened here'],
  'The actual narrow section6P has height6, (6P).O=2 and P.(6P)=2, giving the translation line bundle O(1). The regular invariant character and quotient idea are credited to Engel. The literal cusp extension needs the full corrected construction transferred to PaperI; the published remark alone is not treated as a proof of that correction.',
  ['MAPS:A.1.1','MAPS:A.1.2','MAPS:A.2.1','MAPS:B.6.11']),
 ('mapsVia2','ViaclovskyTwo2026','sources/papers/arXiv_2609.33785_Viaclovsky_two_parameter_src/Viaclovsky_S6_September_26_2026.tex',
  ['Proposition mum and its complete printed proof, source500–594',
   'Proposition4.2, label mat, complete statement/proof873–941',
   'Proposition5.4, label d2, complete statement/proof1264–1307'],
  'The actual one-component rank-one normalization, extending chosen section and primitive two independent rank-two periods are printed. The homological matrices in B4.1 are inverse transposes of the source cohomological matrices. The primitive shift evaluates to1/4 on the invariant character; the integral transgression d2(4psi)=1 follows with the same base orientation. Primitive rank-one fundamental-group specialization is also proved directly in the receiving argument by its nodal thimble, independently of the source’s cited Wang propositions.',
  ['MAPS:B.4.1']),
 ('mapsViaLog','Viaclovsky2026Log','sources/papers/arXiv_2610.39102_Viaclovsky_log_transformations_src/Logarithmic_S6_October_28_2026_Final.tex',
  ['Lemma2.1 label mono with its complete basis-change proof, source275–346',
   'Actual finite logarithmic data, origin subtraction and action construction, source364–454; prior full logprop/bound proof reading retained in CDP ledger'],
  'The source acts on columns with its explicit path convention. Its invariant vectors delta,u0,u1 and degrees3k,4l agree under the receiving unimodular comparison PV. Subtracting the pulled-back section conjugates the affine deck action to its linear group action before adding the finite torsion translation. This is the precise source marking used in the generalized quotient statement.',
  ['MAPS:B.4.1']),
 ('mapsLR','LiuRollenske2026','sources/papers/arXiv_2609.33826_Liu_Rollenske_src/S6_arxiv.tex',
  ['Lemma3.10 label product at1 and Proposition3.11 label monodromy and specialisation at1, complete proofs893–1014',
   'Propositions3.12–3.13, cusp and global marking, complete proofs1016–1243; Corollary3.16 complete proof1245–1283',
   'Proposition4.8 label Leray differentials, complete statement/proof1568–1671'],
  'The reduced typeII fibre is a product with two marked circles; the second is the global invariant character. At the cusp the primitive killed lattice is Zh1+Zh3 and xi=h4*. The exact common integral marking gives the displayed order4/order6 monodromies and logarithmic shift e4/4. The Mayer–Vietoris comparison evaluates local minus global extension on the positive meridian to1 and proves d2(4xi)=1 integrally. This is Liu–Rollenske2026, not Lehn–Rollenske–Schinko2019.',
  ['MAPS:B.4.1'])
]
rows=[]
for key,alias,p,loc,scope,apps in specs:
 rows.append(dict(key=key,alias_of=alias,source=p,sha256=hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),
                  opened_locators=loc,verification_scope=scope,applications=apps,
                  status='verified in the specified scope',**META))
(W/'attached_maps_source_checks.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
refs=json.loads((W/'references_verified.json').read_text())
for r in rows:
 old=next((x for x in refs if x.get('key')==r['key']),None)
 if old is None:refs.append(r)
 elif old!=r:
  old.setdefault('additional_dated_checks',[])
  if r not in old['additional_dated_checks']:old['additional_dated_checks'].append(r)
(W/'references_verified.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n')
aliases=[dict(old_key=r['key'],opened_key=r['alias_of'],kind='same attached source; exact operative scope independently opened',
              evidence='deliverables/work/maps_audit/attached_maps_source_checks.json#'+r['key'],locators=r['opened_locators']) for r in rows]
aliases.extend([
 dict(old_key='E26',opened_key='Engel2026',kind='same attached source',evidence='deliverables/work/invariants_arithmetic/references_verified.json#Engel2026; attached_maps_source_checks.json#mapsEngel',locators=['Original S6.tex; exact statement scopes must follow those records']),
 dict(old_key='mapsAC26',opened_key='AC2026',kind='same original manuscript; retain original-PDF priority over transcription',evidence='deliverables/work/maps_audit/credit_comparison_I.json#A.1.1; deliverables/work/invariants_arithmetic/references_verified.json#AC2026',locators=['Original PDF p.2 marked matrices; topology/canonical construction scopes recorded separately']),
 dict(old_key='Smale61',opened_key='Smale1961',kind='same original1961 paper',evidence='deliverables/work/maps_audit/references_verified.json#Smale1961',locators=['TheoremA p.391, dimension>=5 topological sphere conclusion; does not itself classify exotic smooth structures']),
 dict(old_key='rootIWX20',opened_key='IsaksenWangXu2023',kind='explicit citation replacement, NOT a version alias',evidence='deliverables/work/cdp_audit/maps_E/required_citation_transformations.json; deliverables/work/maps_audit/references_verified.json#IsaksenWangXu2023',locators=['Published2023 Table1 p.113, stable fourth stem zero. Replace edition and locator together.']),
 dict(old_key='mapsCrowleyNordstrom19',opened_key='mapsCrowleyNordstrom19',kind='new exact original source record, no alias required',evidence='deliverables/work/maps_audit/remaining_primary_source_checks.json',locators=['Authorv3,29December2018, §1.4 equations2–3 p.5; journal2019 metadata kept distinct']),
 dict(old_key='mapsCrowleyNordstrom21',opened_key='mapsCrowleyNordstrom21',kind='new exact published source record, no alias required',evidence='deliverables/work/maps_audit/remaining_primary_source_checks.json',locators=['Published2021 p.35, Lemma2.1 and equation2.1; online2020 noted explicitly']),
 dict(old_key='CrowleyNordstrom2020',opened_key='mapsCrowleyNordstrom21',kind='same published paper only at verified matching scope; actual receiving context must be checked',evidence='deliverables/work/maps_audit/remaining_primary_source_checks.json#mapsCrowleyNordstrom21; specialized PUSH owner verifies its own use',locators=['Published2021 p.35, Lemma2.1 and equation2.1; online2020 versus issue2021 distinction retained']),
])
for key in ['mapsKrylov03','mapsShioda90','mapsGriffiths68II','mapsRandalWilliams25','mapsJin26','ffDeligne','ffAlarconForstneric25','ffForstnericPrezelj02']:
 aliases.append(dict(old_key=key,opened_key=key,kind='new exact source record, no alias required',evidence='deliverables/work/maps_audit/remaining_primary_source_checks.json#'+key))
(W/'III_safe_citation_aliases.json').write_text(json.dumps(aliases,ensure_ascii=False,indent=2)+'\n')
discrepancy=dict(source=specs[-1][2],source_sha256=rows[-1]['sha256'],locator='Proposition4.8 proof, source1607–1612',
                original='The displayed Mayer–Vietoris obstruction is written as an element of H1(P1,Z).',
                correction='It belongs to H2(P1,Z), as already shown by the immediately preceding low-degree Leray exact sequence and the degree of the Mayer–Vietoris boundary.',
                mathematical_effect='Typographical degree error only; the unit computation and B4.1 receiving assertion are correct. Original source left unchanged.',**META)
(W/'LR_transgression_target_typo.json').write_text(json.dumps(discrepancy,ensure_ascii=False,indent=2)+'\n')
audit=json.loads((W/'results_audit.json').read_text());events=json.loads((W/'check_events.json').read_text());known={x.get('event_id') for x in events}
for r in rows:
 eid='new-maps-attached-source-scope-20261117:'+r['key'];event=dict(event_id=eid,results=r['applications'],scope=r['verification_scope'],outcome='Exact attached-source scope and marking verified; source identity distinguished from unrelated works.',source_check_keys=[r['key']],**META)
 if eid not in known:events.append(event)
 for a in audit:
  if 'MAPS:'+a['id'] not in r['applications']:continue
  a.setdefault('check_event_ids',[])
  if eid not in a['check_event_ids']:a['check_event_ids'].append(eid)
  a.setdefault('source_check_keys',[])
  if r['key'] not in a['source_check_keys']:a['source_check_keys'].append(r['key'])
(W/'results_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
(W/'check_events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
print('Saved four exact attached-source checks, safe aliases and the scoped LR degree typo.')
