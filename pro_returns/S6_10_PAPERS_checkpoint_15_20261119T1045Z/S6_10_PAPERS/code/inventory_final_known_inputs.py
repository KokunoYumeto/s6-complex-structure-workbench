"""Reconcile eleven stale known-input reason cells; preserve their history.

This is citation/disposition metadata, with no new mathematical review verdict.
It does not edit TeX, bibliography, previews or AUX files.
"""
from pathlib import Path
import csv, datetime, hashlib, json

W = Path(__file__).resolve().parents[1]
R = W.parents[1]
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
WHO = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro)'
receipt = 'analysis/inventory_final_known_input_matches.json'
old_phrase = 'known: credited re-derivation retained in the compendium; exact citation pending current verification'

new_openings = [
    dict(id='FINAL-KNOWN-S-01', source_key='DGKXv1', file='analysis/I_sources/DGKXv1.pdf',
         locus='arXiv2610.00250v1, Proposition6.16 p85; Theorem7.1 and complete displayed proof pp86–87',
         used_by=['inv:E1.1'], scope='Opened the actual Kuranishi local-ring map and its displayed proof, and the complete intrinsic bi-anticanonical pencil proof, including the canonical section-space map and the base automorphism fixing the three distinguished fibres. This supplements the existing bounded source record; it is not a new receiving-proof review.'),
    dict(id='FINAL-KNOWN-S-02', source_key='AC2026', file='../../sources/original/AC26_original_manuscript.pdf',
         locus='Exact attached108-page manuscript: Lemma2.7 and complete proof pp9–10; Theorem9.1(i),(iii) statement p64; Lemma10.7 and complete proof p90; component-count derivation p91',
         used_by=['inv:E1.1','cdp:st:D.1.1','cdp:st:D.1.3'], scope='Opened the invariant/coinvariant lattice maps and their explicit integral generators, the exact algebraic-reduction/canonical-bundle statement, and the split-extension quotient and component-count maps. No whole reading of the proof of Theorem9.1 is claimed; this is a bounded exact-source match.'),
    dict(id='FINAL-KNOWN-S-03', source_key='GS2014', file='analysis/II_pending_primary/GrangerSchulze2014.pdf',
         locus='arXiv1109.2612v7: Theorems1.1 and1.3 p3; complete displayed proof of Theorem1.3 p12',
         used_by=['cdp:st:A.2.3'], scope='Opened the exact equivalence of weakly holomorphic logarithmic residues and normal crossings away from codimension at least two. Read the displayed p12 proof through Jacobian/conductor equality and the local smooth-component residue decomposition. Earlier Proposition3.4 duality reading remains separately scoped; no full article proof credit is inferred.'),
    dict(id='FINAL-KNOWN-S-04', source_key='CDP98', file='analysis/II_pending_primary/CDP1998.pdf',
         locus='Compositio112(1998), Lemma1.4 and complete displayed proof, printed p79 (PDFp3)',
         used_by=['cdp:st:E3'], scope='Opened the exact Moishezon b2>0 lemma and its projective modification/divisor-curve intersection proof. The unrelated false blanket local-freeness claim in Lemma1.5 remains rejected; this opening assigns no proof validity to it.'),
]
for s in new_openings:
    p = (W/s['file']).resolve()
    s.update(recorded_at=NOW, checker=WHO, file_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
             type='bounded source-locator opening and disposition match', adds_receiving_proof_credit=False)

v = json.loads((W/'analysis/current_bibliography_verification.json').read_text())['records']
def first(key, contains=None):
    found=[x for x in v[key] if contains is None or contains in x['locator']]
    assert found, (key,contains)
    return dict(source_key=key, **found[0])
def n(i):
    return dict(new_openings[i-1])

specs = {
 'inv:E1.1': ([first('DGKXv1'), n(1), n(2)], 'DGKXv1 Proposition6.16 p85 and Theorem7.1 pp86–87; AC26 Theorem9.1(i),(iii) p64'),
 'inv:E2.1': ([first('ViaclovskyCombs2026')], 'Viaclovsky comb manuscript Theorem1.1 p2, Theorems2.2–2.3 pp5–6, equation7.5 p26 and initial degree/Proposition9.1 pp29–30'),
 'cdp:st:A.2.3': ([first('GS2014'), n(3)], 'Granger–Schulze2014 Proposition3.4 pp9–10, Theorems1.1/1.3 p3 and proof p12'),
 'cdp:st:C.1.2': ([first('CDP98')], 'Campana–Demailly–Peternell1998 Corollary1.3 and proof p79, with the exact endpoint and Picard-component application retained'),
 'cdp:st:C.2.RAT.6': ([first('Arnold1976NormalForms'),first('MerleTeissier1977'),first('Steenbrink1989Spectrum')], 'Arnold1976 pp92,100–101; Merle–Teissier1977 Theorem2.1.1 and Corollary2.1.3, printed pp11–13; Steenbrink1989 pp165,167'),
 'cdp:st:D.1.1': ([first('AC2026','Lemma10.7'),n(2)], 'AC26 Lemma10.7 and complete proof p90'),
 'cdp:st:D.1.3': ([first('AC2026','Lemma10.7'),n(2)], 'AC26 Lemma2.7 and full integral-generator proof pp9–10, with the component-count derivation p91'),
 'cdp:st:E2': ([first('LRS2019')], 'Lehn–Rollenske–Schinko2019 Theorem3.1, Corollary3.2 p9 and Lemma3.3 proof pp9–10'),
 'cdp:st:E3': ([first('LRS2019'),n(4)], 'Campana–Demailly–Peternell1998 Lemma1.4 p79 and Lehn–Rollenske–Schinko2019 Theorem3.1/Corollary3.2 p9'),
 'cdp:st:E4': ([first('Viaclovsky2026Combs','Theorem 2.2')], 'Viaclovsky comb manuscript Theorem2.2 and full analytic degree-one-flatness proof p5'),
 'cdp:st:E19': ([first('AC26','Theorem7.17,Theorem7.22')], 'AC26 Theorem7.17 p57 and Theorem7.22 pp60–61; the separate E11 application retains its own receiving review'),
}

path=W/'S6_10_PAPERS_inventory.csv'
before_sha=hashlib.sha256(path.read_bytes()).hexdigest()
with path.open() as f:
    reader=csv.DictReader(f); fields=reader.fieldnames; rows=list(reader)
overrides_path=W/'analysis/inventory_overrides.json'
overrides=json.loads(overrides_path.read_text())
changes=[]
for label,(matches,locus) in specs.items():
    same=[x for x in rows if x['label']==label]
    assert len(same)==1,(label,len(same))
    row=same[0]
    assert row['paper']=='II'
    old=row['in_compendium_only_because']
    assert old==old_phrase or receipt in json.loads(row['notes']).get('current_citation_disposition_record',''),(label,old)
    reason='known: credited re-derivation retained in the compendium; current exact source-locus matches: '+locus+'. The matches retain their bounded recorded scope and add no independent receiving-proof review.'
    notes=json.loads(row['notes']); old_notes=row['notes']
    notes.setdefault('historical_compendium_reason_before_final_source_match',old_phrase)
    notes['current_citation_disposition_record']=receipt
    notes['current_citation_disposition_verified_at']=NOW
    notes['current_citation_disposition_scope']='Exact locator and credited-input matching only; historical checks and their original pending wording remain preserved.'
    row['in_compendium_only_because']=reason
    row['notes']=json.dumps(notes,ensure_ascii=False)
    row_key=notes['row_key']
    override=overrides.setdefault(row_key,{})
    override['in_compendium_only_because']=reason
    override.setdefault('_notes',{}).update({k:notes[k] for k in ['historical_compendium_reason_before_final_source_match','current_citation_disposition_record','current_citation_disposition_verified_at','current_citation_disposition_scope']})
    changes.append(dict(label=label,row_key=row_key,source_matches=matches,changed_cells=[
        dict(column='in_compendium_only_because',old=old,new=reason),
        dict(column='notes',old_sha256=hashlib.sha256(old_notes.encode()).hexdigest(),new_sha256=hashlib.sha256(row['notes'].encode()).hexdigest(),added_fields={k:notes[k] for k in ['historical_compendium_reason_before_final_source_match','current_citation_disposition_record','current_citation_disposition_verified_at','current_citation_disposition_scope']})]))

with path.open('w',newline='') as f:
    out=csv.DictWriter(f,fieldnames=fields);out.writeheader();out.writerows(rows)
overrides_path.write_text(json.dumps(overrides,indent=2,ensure_ascii=False)+'\n')
record=dict(recorded_at=NOW,checker=WHO,scope='Administrative current-disposition reconciliation of eleven exact compendium-only rows; historical pending text retained. No receiving theorem, source status, argument verdict, TeX, bibliography, preview or AUX changed.',inventory_before_sha256=before_sha,inventory_after_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),rows_changed=len(changes),cells_changed=2*len(changes),new_bounded_openings=new_openings,changes=changes)
(W/receipt).write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'rows_changed':len(changes),'cells_changed':2*len(changes),'receipt':receipt}))
