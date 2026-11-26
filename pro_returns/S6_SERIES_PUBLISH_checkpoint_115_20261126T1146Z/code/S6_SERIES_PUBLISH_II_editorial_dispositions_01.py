#!/usr/bin/env python3
"""Exact editorial disposition of 02UH and positive title for 01FH."""
from pathlib import Path
import collections,csv,datetime as dt,difflib,hashlib,io,json,re
R=Path(__file__).resolve().parents[1]
C=R/'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_02UH_editorial_v1'
OUT=R/'records/S6_SERIES_PUBLISH_II_editorial_dispositions_01'
csv.field_size_limit(100_000_000)
sha=lambda b:hashlib.sha256(b).hexdigest()
def binding(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(R)),bytes=len(b),sha256=sha(b))
def enc(x):return (json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode()
def rd(name,sep='\t'):
 b=(R/name).read_bytes();x=csv.DictReader(io.StringIO(b.decode()),delimiter=sep);return b,list(x),x.fieldnames
def tab(rows,fields,sep='\t',header=True):
 b=io.StringIO(newline='');w=csv.DictWriter(b,fieldnames=fields,delimiter=sep,lineterminator='\n')
 if header:w.writeheader()
 w.writerows(rows);return b.getvalue().encode()
assert not OUT.exists()
index=C/'S6_SERIES_PUBLISH_II_C2_02UH_editorial_index_final_v1.json'
assert sha(index.read_bytes())=='1f68a1f361db269b738a90c9ccc7cb0dc07c6a678b19590f05ed868005857e27'
ix=json.loads(index.read_text())
for x in ix['files']+ix['immutable_input_bindings']:
 b=(R/x['path']).read_bytes();assert len(b)==x['bytes'] and sha(b)==x['sha256'],x['path']
old=(R/'S6_SERIES_PUBLISH_II.tex').read_bytes();s=old.decode()
assert sha(old)==ix['source_baseline_sha256']
guards=json.loads((C/'S6_SERIES_PUBLISH_II_C2_02UH_guarded_changes_v1.json').read_text())['guards']
guards.append(dict(id='FH-title-001',scope='cdp:st:C2b',
 old='\\begin{proposition}[Counterexample: Nonnegativity of every fibre in unrestricted torus fibrations]\\hypertarget{tag-01FH}',
 new='\\begin{proposition}[Torus fibres of Euler numbers $-2$ and zero]\\hypertarget{tag-01FH}',
 expected_count=1,defect_ids=['D16'],reason='State the exact two Euler values proved by the unchanged complete blowup construction; remove the title framed around a rejected universal claim.'))
new=s;inverse=[]
for g in guards:
 assert new.count(g['old'])==g['expected_count']==1,g['id']
 p=new.index(g['old']);new=new[:p]+g['new']+new[p+len(g['old']):]
 inverse.append(dict(offset=p,old=g['old'],new=g['new'],id=g['id']))
back=new
for g in reversed(inverse):
 p=g['offset'];assert back[p:p+len(g['new'])]==g['new'];back=back[:p]+g['old']+back[p+len(g['new']):]
assert back==s
for pattern in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',r'\\tag\{[^}]+\}',r'\\StatementRecord\{[^}]+\}\{[^}]+\}\{[^}]+\}']:
 assert re.findall(pattern,s)==re.findall(pattern,new)
def proofblock(text,tag,env='proposition'):
 i=text.index('\\hypertarget{tag-'+tag+'}');a=text.rfind('\\begin{'+env+'}',0,i);b=text.index('\\end{proof}',i)+len('\\end{proof}');return text[a:b]
assert proofblock(s,'01RO','theorem')==proofblock(new,'01RO','theorem')
fh_old=proofblock(s,'01FH');fh_new=proofblock(new,'01FH')
assert fh_old[fh_old.index('\\hypertarget'):]==fh_new[fh_new.index('\\hypertarget'):]
now=dt.datetime.now(dt.timezone.utc).isoformat()
db,defects,df=rd('S6_SERIES_PUBLISH_defects_II.tsv');added=[]
for g in guards:
 for typ in g['defect_ids']:
  row={k:'' for k in df};row.update(change_id=f'II-DISPOSITIONS-01-{len(added)+1:03}',type=typ,statement_id=g['scope'],old_location=g['id'],old_page='inherited page; exact source fragment bound',new_location=g['scope'],new_page='pending integrated build',old_text=g['old'],new_text=g['new'],reason=g['reason'],review_status='Root read complete old/new02UH blocks, full editorial report, exact guards/diff, covering statement and complete G paragraph. Root read full01FH proof; its title alone changes. Exact inverse and all identities verified; final PDF review pending.');added.append(row)
dtail=tab(added,df,header=False)
eb,events,ef=rd('CHECK_EVENTS.tsv');event={k:'' for k in ef}
event.update(statement_id='cdp:st:C2b',date='2026-11-22',date_utc=now,who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited effort not separately exposed; S6_SERIES_PUBLISH continuation2 root',type='used and rechecked in this run',outcome='Read the complete 3139-byte original statement/proof and compared the revised block, which changes only the mathematical title. The explicit genus-two Jacobian embedding, two blowups, normal-crossing local chart, fibre Euler sums and integral Betti formulas remain byte-identical. The title now states the two proved Euler values -2 and zero. No new program, independent derivation or required-check closure is claimed.',event_id='publish:editorial-dispositions01:01FH-title',phase='publication editorial comparison',source_file='records/S6_SERIES_PUBLISH_II_editorial_dispositions_01/manifest.json',source_event_type='used and rechecked in this run',evidence_group='publish:editorial-dispositions01:01FH-title',where='01FH / cdp:st:C2b complete owning block')
assert event['event_id'] not in {x['event_id'] for x in events};etail=tab([event],ef,header=False)
tb,tags,tf=rd('S6_SERIES_PUBLISH_tags.tsv');ib,inv,inf=rd('S6_SERIES_PUBLISH_inventory.csv',',')
disp=json.loads((C/'S6_SERIES_PUBLISH_II_C2_02UH_metadata_disposition_proposal_v1.json').read_text())
for row in tags:
 if row['tag']=='02UH':
  assert row['status'] in ['false','false as stated'],row
  row['publication_disposition']=disp['proposed_publication_disposition']
other=[x.copy() for x in inv if x['paper']!='II']
for row in inv:
 if row['paper']=='II' and row['label']=='night:P3K.36':
  assert row['status']=='false as stated'
  record=json.loads(row['check_record']);record['editorial_anchor_disposition_20261122']=disp
  row['check_record']=json.dumps(record,ensure_ascii=False)
  row['writing_state']='Permanent anchors on a numbered mathematical cross-reference remark; original compound assertion remains refuted in records.'
  row['publication_review_status']='Exact02UH disposition reviewed; old required-owner resolution and full paper gates preserved.'
assert [x for x in inv if x['paper']!='II']==other
cp=R/'S6_SERIES_PUBLISH_checks_II.md';cb=cp.read_bytes();checks=cb.decode();a=checks.index('<a id="tag-02UH"></a>');b=checks.find('<a id="tag-',a+1);b=len(checks) if b<0 else b;part=checks[a:b];p=part.index('### Check events')
notice='### Permanent-anchor disposition\n\nThe original compound universal fan claim remains false as stated. Its permanent tag02UH and both labels now occur at a numbered reference remark, which identifies the checked parameter-covering theorem01RO and the existing IV fan calculations. This is the explicit disposition map in `agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_02UH_editorial_v1/S6_SERIES_PUBLISH_II_C2_02UH_editorial_report_v1.md`, not an equality between the historical compound claim and the retained covering theorem. The complete old text, numerical data and refutation history are preserved in that packet and ledger.\n\n'
checks=checks[:a]+part[:p]+notice+part[p:]+checks[b:]
rb=(R/'records/S6_SERIES_PUBLISH_additional_event_bundles.json').read_bytes();registry=json.loads(rb)
bundle=tab([event],ef);registry['bundles'].append(dict(path='records/S6_SERIES_PUBLISH_II_editorial_dispositions_01/event_rows.tsv',bytes=len(bundle),sha256=sha(bundle),admission_manifest='records/S6_SERIES_PUBLISH_II_editorial_dispositions_01/manifest.json'))
OUT.mkdir();(OUT/'guards.json').write_bytes(enc(guards));(OUT/'inverse.json').write_bytes(enc(inverse));(OUT/'event_rows.tsv').write_bytes(bundle);(OUT/'defect_rows.tsv').write_bytes(tab(added,df))
(OUT/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before dispositions01',tofile='II after dispositions01')))
changes=[('S6_SERIES_PUBLISH_II.tex',old,new.encode()),('S6_SERIES_PUBLISH_defects_II.tsv',db,db+dtail),('CHECK_EVENTS.tsv',eb,eb+etail),('S6_SERIES_PUBLISH_tags.tsv',tb,tab(tags,tf)),('S6_SERIES_PUBLISH_inventory.csv',ib,tab(inv,inf,',')),('S6_SERIES_PUBLISH_checks_II.md',cb,checks.encode()),('records/S6_SERIES_PUBLISH_additional_event_bundles.json',rb,enc(registry))]
for name,bef,aft in changes[3:]:
 (OUT/(Path(name).name+'.diff')).write_text(''.join(difflib.unified_diff(bef.decode().splitlines(True),aft.decode().splitlines(True),fromfile=name+' before',tofile=name+' after')))
root_reading=dict(
    scope='Full old and proposed02UH block; complete C report, guards, diff, disposition and exposure receipt; complete G statement/mechanism/history paragraph and covering01RO statement; full original3139-byte01FH and full proposed3105-byte01FH proof block.',
    proof_comparison='The01FH block differs only in its title. The02UH old false universal claim is disposed to a reference remark preserving permanent identity; its archive retains the numerical refutation and the exact theorem/cross-paper maps.',
    no_new_independent_or_targeted_check=True,
    other_paper_exposure='C disclosed a527-byte embedded IV proof in an unintended metadata print. No IV source or PDF was opened; no IV check credit is claimed. Root used the explicit metadata disposition and did not read the IV source.',
    final_pdf_page_credit=0,
    fh_before_sha256=sha(fh_old.encode()),fh_after_sha256=sha(fh_new.encode()),
    C_full_read_record='The full editorial report and its immutable evidence index bind the exact historical-to-current disposition. No universal fan polynomial is asserted in the revised block.')
(OUT/'root_reading.json').write_bytes(enc(root_reading))
manifest=dict(created_utc=now,source_before_sha256=sha(old),source_after_sha256=sha(new.encode()),
    C_index=binding(index),sealed_packet_bindings_verified=len(ix['files'])+len(ix['immutable_input_bindings']),
    guards=len(guards),exact_inverse=True,
    all_old_labels_hypertargets_equation_tags_statement_record_triples_preserved=True,
    covering_01RO_unchanged=True,fh_proof_body_byte_identical=True,
    events_added=1,event_types={'used and rechecked in this run':1},
    ledger_rows_before=len(events),ledger_rows_after=len(events)+1,
    defect_rows_added=len(added),defect_rows_before=len(defects),
    historical_02UH_status_preserved='false as stated',
    historical_02UH_required_owner_resolution_preserved='ii:LR:covering',
    required_rows_closed=0,global_defect_classes_closed=0,final_pdf_page_credit=0,
    limits=['The final source-wide class audits remain open.','The final integrated build and page-image reading remain open.','The metadata refresh must retain the historical02UH resolution by01RO without asserting equality of their statements.'],
    canonical_changes=[dict(path=n,before_bytes=len(b),before_sha256=sha(b),after_bytes=len(a),after_sha256=sha(a)) for n,b,a in changes],
    immutable_evidence=[binding(p) for p in sorted(OUT.iterdir())],
    code=binding(Path(__file__)))
mp=OUT/'manifest.json';mp.write_bytes(enc(manifest));mb=binding(mp)
for n,b,a in changes:assert (R/n).read_bytes()==b,n
for n,b,a in changes:(R/n).write_bytes(a)
assert (R/'CHECK_EVENTS.tsv').read_bytes().startswith(eb)
assert (R/'S6_SERIES_PUBLISH_II.tex').read_bytes()==new.encode()
note=f'''\n\n## Paper II: permanent-anchor disposition and fibre title — {now}\n\nThe historical compound fan claim02UH is now a numbered mathematical reference remark. Its permanent tag, both labels and inert historical status metadata remain; the original false assertion and complete numerical refutation remain in the checking records. The remark gives the exact reference map to covering theorem01RO and the already identified IV fan calculations. The obsolete02UH dependency on main theorem G is removed, and its mechanism and known/new entry point directly to the retained covering theorem. This makes no equality claim between the historical compound assertion and01RO.\n\nThe full01FH blowup construction was reread and compared. Its title now names the two Euler values it proves, -2 and zero; all mathematics in its statement and proof is byte-identical. The exact guards, inverse, comparison scope, twelve individual defect records and one exposed-reread event are bound in `{mb['path']}` (SHA-256 `{mb['sha256']}`). The source is `{sha(new.encode())}` and the ledger has {len(events)+1} rows. No required row, source-wide defect class or final PDF page is closed by this admission.\n'''
assert len(added)==12
for n in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
    with (R/n).open('ab') as f:f.write(note.encode())
receipt=dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=mb,
    canonical_after_bindings=[binding(R/n) for n,_,_ in changes],
    no_prior_events_deleted_or_changed=True,source_bytes=len(new.encode()),events_added=1,defect_rows_added=len(added))
(OUT/'admission_receipt.json').write_bytes(enc(receipt))
print(json.dumps({k:manifest[k] for k in ['created_utc','source_after_sha256','guards','ledger_rows_after','defect_rows_added','required_rows_closed','global_defect_classes_closed','final_pdf_page_credit']},indent=2))
print('Manifest:',mb['path'],mb['sha256'])
