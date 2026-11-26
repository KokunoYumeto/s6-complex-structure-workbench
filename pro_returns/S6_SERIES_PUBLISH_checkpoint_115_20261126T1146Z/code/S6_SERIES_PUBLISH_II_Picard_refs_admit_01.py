#!/usr/bin/env python3
"""Admit twelve identical-label reference transports and exact auxiliary metadata."""
from pathlib import Path
import argparse,collections,csv,datetime as dt,difflib,hashlib,io,json,re
from S6_SERIES_PUBLISH_II_title_census import fingerprint
R=Path(__file__).resolve().parents[1];P=R/'agents/continuation2_A/S6_SERIES_PUBLISH_II_A2_Picard_reference_transport_01_final_v1';PRE='S6_SERIES_PUBLISH_II_A2_Picard_reference_transport_01_';O=R/'records/S6_SERIES_PUBLISH_II_Picard_references_01'
csv.field_size_limit(100_000_000);sha=lambda b:hashlib.sha256(b).hexdigest()
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def bind(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(b),sha256=sha(b))
def rd(n):
 b=(R/n).read_bytes();x=csv.DictReader(io.StringIO(b.decode()),delimiter='\t');return b,list(x),x.fieldnames
def tab(rows,fields,header=True):
 o=io.StringIO(newline='');w=csv.DictWriter(o,fieldnames=fields,delimiter='\t',lineterminator='\n')
 if header:w.writeheader()
 w.writerows(rows);return o.getvalue().encode()
ap=argparse.ArgumentParser();ap.add_argument('--expected-source',required=True);args=ap.parse_args()
assert not O.exists();idxp=P/(PRE+'index.json');assert sha(idxp.read_bytes())=='7d70fc6a7edf347e5d807140d4a19983e22c09b320cb25f5b79d5000abc2ba33';idx=json.loads(idxp.read_text())
for f in idx['files']:
 b=(R/f['path']).read_bytes();assert len(b)==f['bytes'] and sha(b)==f['sha256'],f['path']
before=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();s=before.decode();assert sha(before)==args.expected_source
meta=json.loads((P/(PRE+'I_metadata.json')).read_text());auxp=R/'build/I_candidate19/S6_SERIES_PUBLISH_I.aux';aux=auxp.read_bytes();assert sha(aux)=='ffc8ace65191fb62b77cd378d41c492e279058a02d4e40511749af9f67bd1081'
for row in meta['mapping']:assert aux.decode().splitlines().count(row['exact_aux_line'])==1,row['label']
guards=json.loads((P/(PRE+'guards.json')).read_text());ranges=[];new=s;inv=[]
for g in guards:
 assert s.count(g['old'])==1,g['id'];a=s.index(g['old']);ranges.append((a,a+len(g['old']),g['id']))
 assert sha(g['old'].encode())==g['old_sha256'] and sha(g['new'].encode())==g['new_sha256']
for a,b in zip(sorted(ranges),sorted(ranges)[1:]):assert a[1]<=b[0],(a,b)
for g in guards:
 a=new.index(g['old']);inv.append(dict(id=g['id'],offset=a,old=g['old'],new=g['new']));new=new[:a]+g['new']+new[a+len(g['old']):]
back=new
for g in reversed(inv):
 a=g['offset'];assert back[a:a+len(g['new'])]==g['new'];back=back[:a]+g['old']+back[a+len(g['new']):]
assert back==s and fingerprint(new)==fingerprint(s)
preservation=[]
def project(t):return re.sub(r'\\(?:CompendiumRef\{I\}|SeriesRef)\{([^}]+)\}',lambda m:'REF{'+m[1]+'}',t)
for owner in idx['owners']:
 k=owner['short'];b=(P/(PRE+k+'_before.tex')).read_text();a=(P/(PRE+k+'_after.tex')).read_text()
 assert s.count(b)==1 and new.count(a)==1 and project(b)==project(a)
 assert re.findall(r'\\(?:label|hypertarget|tag)\{[^}]+\}',b)==re.findall(r'\\(?:label|hypertarget|tag)\{[^}]+\}',a)
 preservation.append(dict(owner=owner['owner'],before_sha256=sha(b.encode()),after_sha256=sha(a.encode()),same_label_projection_byte_identical=True))
for pat in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',r'\\tag\{[^}]+\}',r'\\StatementRecord\{[^}]+\}\{[^}]+\}\{[^}]+\}']:assert re.findall(pat,s)==re.findall(pat,new)
db,defs,df=rd('S6_SERIES_PUBLISH_defects_II.tsv');proposals=list(csv.DictReader((P/(PRE+'defects.tsv')).open(),delimiter='\t'));dr=[];byid={g['id']:g for g in guards}
for d in proposals:
 row={k:'' for k in df};row.update(change_id=f'II-PICARD-REFS-01-{len(dr)+1:03}',type=d['type'],statement_id=d['owner'],old_location=d['guard_id']+' / '+d['instance_scope'],old_page='exact receiving source span in sealed packet',new_location=d['owner'],new_page='pending integrated build',old_text=d['old_text'],new_text=d['new_text'],reason=byid[d['guard_id']]['reason'],review_status='A read all three complete original/revised blocks; root read complete comparison, all exact proof diffs, macro definitions and selected exact I auxiliary metadata. Current-source inverse and unchanged nonreference bytes verified. Final five-together regeneration remains open.');dr.append(row)
assert len(dr)==34
eb,events,ef=rd('CHECK_EVENTS.tsv');ev=[]
for p in json.loads((P/(PRE+'event_proposals.json')).read_text())['events']:
 e={k:p.get(k,'') for k in ef};e['phase']='publication reference comparison';e['source_event_type']=e['type'];e['publish_input_file']='records/S6_SERIES_PUBLISH_II_Picard_references_01/manifest.json';assert e['type']=='used and rechecked in this run' and e['event_id'] not in {x['event_id'] for x in events};ev.append(e)
assert len(ev)==3 and len({e['evidence_group'] for e in ev})==1
rb=(R/'records/S6_SERIES_PUBLISH_additional_event_bundles.json').read_bytes();reg=json.loads(rb);bundle=tab(ev,ef);reg['bundles'].append(dict(path='records/S6_SERIES_PUBLISH_II_Picard_references_01/event_rows.tsv',bytes=len(bundle),sha256=sha(bundle),admission_manifest='records/S6_SERIES_PUBLISH_II_Picard_references_01/manifest.json'))
now=dt.datetime.now(dt.timezone.utc).isoformat();O.mkdir();(O/'inverse.json').write_bytes(enc(inv));(O/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before Picard references01',tofile='II after Picard references01')));(O/'event_rows.tsv').write_bytes(bundle);(O/'defect_rows.tsv').write_bytes(tab(dr,df))
(O/'root_review.json').write_bytes(enc(dict(recorded_utc=now,proof_reading='A actually read all complete before/after IC,IN,DR blocks. Root read all exact diffs, full comparison, all macro definitions and the exact selected metadata; root does not claim another complete after-block reading.',exact_preservation=preservation,auxiliary_metadata=bind(auxp),selected_auxiliary_lines=meta['mapping'],I_source_or_PDF_opened_by_root=False,incidental_A_exposure=meta['exposure_limitation'],no_independent_check_credit=True,unresolved='Five historical I uses remain open; the unnumbered nodal W.5.2 call remains assigned to B. Sixteen active CompendiumRef calls remain at this bound source.')))
changes=[('S6_SERIES_PUBLISH_II.tex',before,new.encode()),('S6_SERIES_PUBLISH_defects_II.tsv',db,db+tab(dr,df,False)),('CHECK_EVENTS.tsv',eb,eb+tab(ev,ef,False)),('records/S6_SERIES_PUBLISH_additional_event_bundles.json',rb,enc(reg))]
manifest=dict(created_utc=now,source_before_sha256=sha(before),source_after_sha256=sha(new.encode()),sealed_index=bind(idxp),verified_bindings=len(idx['files']),guards=len(guards),exact_inverse=True,identical_label_reference_transports=12,shared_macro_updates=6,new_equation_macros=3,printed_span_class_rows=27,supporting_macro_rows=7,defect_rows_added=34,defect_rows_after=len(defs)+34,events_added=3,event_groups=1,ledger_rows_after=len(events)+3,D16_projection_unchanged=True,required_rows_closed=0,global_defect_classes_closed=0,final_pdf_page_credit=0,exact_mathematical_map='Each old CompendiumRef(I,label) and its new SeriesRef(label) have the identical label. The auxiliary metadata gives the exact displayed number/page/target. Every other byte in all three receiving blocks is preserved.',unresolved_historical_calls=5,orphan_reference_transferred_to_B=1,five_together_regeneration_open=True,canonical_changes=[dict(path=n,before_sha256=sha(b),after_sha256=sha(a)) for n,b,a in changes],evidence=[bind(p) for p in sorted(O.iterdir())],code=bind(Path(__file__)))
mp=O/'manifest.json';mp.write_bytes(enc(manifest));mb=bind(mp)
for n,b,a in changes:assert (R/n).read_bytes()==b
for n,b,a in changes:(R/n).write_bytes(a)
note=f'''\n\n## Paper II: exact Picard cross-paper references — {now}\n\nTwelve inherited compendium calls now print the current I number and page for the identical label. Six existing shared macros are corrected and three equation macros use their exact admitted auxiliary destinations. The complete IC,IN,DR before/after proofs were read by A; the exact reference-token map preserves every other mathematical and source byte. Root checked the full comparison and exact diffs, and verified the nine selected auxiliary rows without opening I source or PDF. The disclosed incidental I snippets in A's earlier metadata outputs add no I review or check credit.\n\nFive historical I setup uses still lack an admitted current identity and remain open. The separate nodal W.5.2 call remains assigned to B. Final five-together cross-reference regeneration remains required. The nineteen exact guards, current-source inverse,27 printed-span/class rows and seven supporting macro rows are bound in `{mb['path']}` (SHA-256 `{mb['sha256']}`). Three exposed-reread events in one group bring the ledger to {len(events)+3} rows. No required row, global class or final page is closed.\n'''
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
 with (R/n).open('ab') as f:f.write(note.encode())
(O/'admission_receipt.json').write_bytes(enc(dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,canonical_after=[bind(R/n) for n,_,_ in changes])))
print(json.dumps({k:manifest[k] for k in ['created_utc','source_after_sha256','guards','defect_rows_after','ledger_rows_after']},indent=2));print('Manifest',mb['sha256'])
