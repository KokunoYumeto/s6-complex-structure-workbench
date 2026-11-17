"""Append exact final original-page scopes; retain every earlier reading."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[3];W=R/'deliverables/work/maps_audit'
meta=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')
rows=[
 dict(key='mapsHatcher02',alias_of='Hatcher2002',source='sources/external/maps_audit/hatcher.pdf',
  opened_locators=['Propositions4G.1–4G.2 and both complete proofs, printed pp458–459, original extracted text23020–23145','Earlier exact Theorems4.5,4.32,Corollary4.33 and their proofs retained under Hatcher2002'],
  verification_scope='B5.1 finite mapping-cylinder replacement: for a homotopy f_t:B→A, use the diagram with vertex B×I and edge f_t, and the other edge g composed with projection. Each endpoint diagram maps strictly to it by a homotopy equivalence on every vertex, so4G.1 gives homotopy equivalences of the double mapping cylinders. The actual collared cover of compact smooth X is paracompact and satisfies4G.2. This checks the required strict-diagram hypothesis rather than treating a merely homotopy-commuting square as strict.',
  extent='Both original statements and complete printed proofs opened and rederived; finite graph hypotheses matched explicitly.'),
 dict(key='Smale61',alias_of='Smale1961',source='sources/external/maps_audit/smale1961.pdf',
  opened_locators=['Theorem I pp392–393 and the explicit orientation-preserving sentence on p393','Theorem J p393, complete statement and preceding explanation; Theorem K p394 and its printed deductions from A,H,I'],
  verification_scope='FAMILY E2.2: in odd dimension7 the J-equivalence classes of smooth homotopy spheres coincide with oriented diffeomorphism classes. The orientation statement immediately before J is explicit. Theorem J is on p393, not p394. The gluing/isotopy equivalence still uses the separately checked Cerf result; J alone is not claimed to identify pi0 Diff+(S6).',
  visual_pages=['deliverables/work/maps_audit/smale1961_p393.png','deliverables/work/maps_audit/smale1961_p394.png'],
  extent='Original exact statements and their printed introductory deductions opened; no claim of rereading the entire handlebody proof in this event.'),
 dict(key='mapsAC26',alias_of='AC2026',source='sources/original/AC26_original_manuscript.pdf',
  opened_locators=['Original PDF p2 marked matrices, retained earlier PaperI reading','Original PDF p42 first paragraph and complete covering/meridian argument before section7.2; visually reopened in this event'],
  verification_scope='MAPS A1 fixed marking and B5.1 correction. The original p42 says multiplicity prevents a tubular neighbourhood. Its own finite free quotient (F x D2)/<h,zeta> is in fact a smooth associated normal disc bundle over F/<h>. MAPS B5.1 explicitly supplies the radial collapse and full affine drift straightening. The original meridian relation remains correct; its normal circle winds m times around the base. No holomorphic tubular projection is inferred.',
  visual_pages=['deliverables/work/maps_audit/AC26_p42.png'],
  extent='Exact original statement and full relevant meridian paragraph checked; the original PDF governs, not a transcription.'),
]
for r in rows:
 r.update(meta);r.update(status='verified in the specified scope',sha256=hashlib.sha256((R/r['source']).read_bytes()).hexdigest())
(W/'final_citation_source_checks.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
refs=json.loads((W/'references_verified.json').read_text())
for r in rows:
 old=next((x for x in refs if x.get('key')==r['key']),None)
 if old is None:refs.append(r)
 elif old!=r:
  old.setdefault('additional_dated_checks',[])
  if r not in old['additional_dated_checks']:old['additional_dated_checks'].append(r)
(W/'references_verified.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n')
aliases=json.loads((W/'III_safe_citation_aliases.json').read_text())
for r in rows:
 for a in aliases:
  if a['old_key']==r['key']:
   a['additional_exact_scope']=r['opened_locators'];a['additional_evidence']='deliverables/work/maps_audit/final_citation_source_checks.json#'+r['key']
(W/'III_safe_citation_aliases.json').write_text(json.dumps(aliases,ensure_ascii=False,indent=2)+'\n')
print('Saved exact Smale J/K and AC26 original p42 scopes.')
