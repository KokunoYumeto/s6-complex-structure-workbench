from pathlib import Path
import csv,json,hashlib,shutil
p=Path(__file__).resolve().parents[1]
# Preserve the old attribution and move that event to the adjacent lemma it actually reviews.
with (p/'CHECK_EVENTS.tsv').open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;events=list(r)
eid='s6sg:f2e0ffb1e08fc1af9919'
old=next(dict(e) for e in events if e['event_id']==eid)
assert old['statement_id']=='night:P3F.19'
for e in events:
 if e['event_id']==eid:e['statement_id']='iv:rank_two_specialization'
actor='GPT-6 Astra (OpenAI), ChatGPT Pro mode, reasoning effort inherited from root (not separately exposed), S6_SERIES_GRIND/corrections_audit'
outcome='Read actual F19 and freshly opened the attached Yang REPAIRED_v4_5 source, lines3210–3320, Lemma invariant closure and Theorem Fundamental group of the two completed families with its complete proof (attached-source edition Theorem7.2, pp.40–41). The complete presentation has central z, xy=z^ell0, x^m1=z^ell1, y^m2=z^ell2. The actual homomorphism z→0, x→1, y→−1 to Z/g, g=gcd(m1,m2), kills every relation for all admitted twists and is onto. For(4,6) and(3,6), g=2 and3; the canonical exact groups are credited to the source. The short cited proof is sufficient. This opening is of the attached repaired edition, not a new claim about original arXiv pagination. Corrected the previous adjacent-lemma audit attribution in IV_F19_attribution_correction.json.'
newid='s6sg:'+hashlib.sha256(('night:P3F.19|targeted proof check|'+outcome).encode()).hexdigest()[:20]
assert not any(e['event_id']==newid for e in events)
events.append(dict(statement_id='night:P3F.19',date='2026-11-19',who=actor,type='targeted proof check',outcome=outcome,event_id=newid,phase='S6_SERIES_GRIND'))
with (p/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
with (p/'IV_known_input_specializations.tsv').open(newline='') as f:
 r=csv.DictReader(f,delimiter='\t');tf=r.fieldnames;table=list(r)
oldrow=next(dict(r) for r in table if r['label']=='night:P3F.19')
replacement={'label':'night:P3F.19','source_locator':'Yang attached REPAIRED_v4_5, Lemma7.1/Theorem7.2, attached-source pp.40–41; TeX lines3210–3320','known_input':'Complete boundary fundamental-group presentation and canonical exact groups for Type B/C.','retained_map_or_calculation':'Kill the fibre loops and send the finite meridians to1,−1 and the cusp meridian to0 in Z/g, with g=gcd(m1,m2)=2 or3. Every relation is killed for every admitted twist; the first meridian maps to1.','condition_4_4_2_disposition':'Retain the already-short cited specialization. The canonical exact groups are explicitly credited to Yang; no long proof replacement is needed.','opening_and_check_scope':'Actual F19 proof read; attached Yang theorem and complete proof freshly opened. The adjacent iv:rank_two_specialization lemma has its own independent lattice/cross-line audit and is not attributed to F19.'}
for i,r in enumerate(table):
 if r['label']=='night:P3F.19':table[i]=replacement
with (p/'IV_known_input_specializations.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=tf,delimiter='\t');w.writeheader();w.writerows(table)
g=p/'code/build_IV_known_input_review.py';s=g.read_text();start=s.index("row(19,");end=s.index("row(20,",start)
newcall="row(19,"+','.join(repr(replacement[k]) for k in tf[1:])+')\n'
s=s[:start]+newcall+s[end:]
s=s.replace('F19’s integral cross-generator','the separate `iv:rank_two_specialization` integral cross-generator')
g.write_text(s)
rp=p/'IV_known_input_review.md';s=rp.read_text().replace('F19’s integral cross-generator','the separate `iv:rank_two_specialization` integral cross-generator');rp.write_text(s)
a=json.loads((p/'row_assessments.json').read_text());a['night:P3F.19']={'confidence_state':'proved at the stated source and twist scope','confidence_line':'The full attached Yang presentation admits the explicit onto quotient z→0, x→1, y→−1 in Z/g for every admitted twist, giving Z/2 and Z/3 quotients in Types B/C; the canonical exact groups are credited directly.','independent_routes':['Fresh reading of the attached source theorem and its complete van Kampen/Smith proof.','Direct check of every defining relation under the displayed cyclic quotient map.'],'remaining_risk':'No mathematical gap identified in this short specialization. Credit and locators concern the attached repaired source edition; no assertion about original arXiv text or pagination is made.','format_check':None,'layout_check':None,'completion_state':None};(p/'row_assessments.json').write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
receipt={'event_count_before':len(events)-1,'event_count_after':len(events),'retargeted_event_id':eid,'old_statement_id':'night:P3F.19','new_statement_id':'iv:rank_two_specialization','retargeted_event_outcome_unchanged':True,'new_F19_event_id':newid,'old_event_preserved':old,'old_table_row_preserved':oldrow,'corrected_table_row':replacement,'cause':'The previous review table assigned the adjacent rank-two specialization lemma scope to F19. The manuscript statement and rank-two proof are unchanged.','manuscript_edits':False}
(p/'IV_F19_attribution_correction.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
# Contact-sheet pass. Current sheet02 was changed by build14 and viewed by root.
vp=p/'IV_visual_QA_CP03.json'
shutil.copy2(vp,p/'IV_visual_QA_CP03_build12_receipt.json')
qa={'date_utc':'2026-11-19','actor':actor,'build':'13/14 CP03; IV1426pages','scope':'Actual contact-sheet visual inspection only, not every page of Paper IV.','finding':'No clipping, formula overlap, or missing glyphs visible on the inspected sheets. The inspected proof-step labels are separated after the common formatter repair.','root_comparison':'Root reports only IV02 changed between build13 and14; all other contact-sheet pixel hashes agree. Root viewed final IV02 cleanly.','sheets':[]}
pages=[[1,2,3,7],[17,18,19,142],[143,144,148,149],[150,356,713,1069],[1116,1117,1118,1127],[1131,1134,1135,1138],[1147,1155,1161,1162],[1163,1168,1174,1180]]
for i,pg in enumerate(pages,1):
 f=p.parent/'build/visual_qa'/f'QA_IV_{i:02}.png'
 qa['sheets'].append({'file':str(f.relative_to(p.parent)),'pages':pg,'file_sha256_current':hashlib.sha256(f.read_bytes()).hexdigest(),'actually_viewed_by_this_agent':'build13, with build14 pixel identity reported by root' if i!=2 else 'build13; changed final build14 sheet separately viewed by root','finding':'No visible clipping or missing glyphs. Proof labels remain legible.'})
vp.write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'events':len(events),'retargeted_event_id':eid,'new_F19_event_id':newid,'assessments':len(a),'QA':'IV01–08 receipt saved','writes':'paused after this command'},indent=2))
