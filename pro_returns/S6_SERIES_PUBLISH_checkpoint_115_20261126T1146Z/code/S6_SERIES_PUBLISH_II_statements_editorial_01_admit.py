from pathlib import Path
import csv, datetime as dt, difflib, hashlib, io, json, re

R=Path(__file__).resolve().parents[1];out=R/'records/S6_SERIES_PUBLISH_II_statements_editorial_01'
sha=lambda b:hashlib.sha256(b).hexdigest()
index=json.loads((out/'proposal_index.json').read_text())
for row in index['files']:
    b=(R/row['path']).read_bytes();assert len(b)==row['bytes'] and sha(b)==row['sha256'],row['path']
guards=json.loads((out/'guards.json').read_text())
p=R/'S6_SERIES_PUBLISH_II.tex';old=p.read_bytes();s=old.decode();new=s
assert sha(old)==index['source_sha256']
for g in guards:
    assert new.count(g['old'])==1;new=new.replace(g['old'],g['new'],1)
back=new
for g in reversed(guards):
    assert back.count(g['new'])==1;back=back.replace(g['new'],g['old'],1)
assert back==s
for pattern in [r'\\label\{[^}]+\}',r'\\hypertarget\{[^}]+\}',r'\\tag\{[^}]+\}',r'\\StatementRecord\{[^}]+\}\{[^}]+\}\{[^}]+\}']:
    assert re.findall(pattern,s)==re.findall(pattern,new)
for tag in ['02Y6','02XE']:
    def blk(t):
        at=t.index('\\hypertarget{tag-'+tag+'}');a=t.rfind('\\begin{proposition}',0,at);b=t.index('\\end{proof}',at)+len('\\end{proof}');return t[a:b]
    assert blk(s)==blk(new)
now=dt.datetime.now(dt.timezone.utc).isoformat()
ep=R/'CHECK_EVENTS.tsv';eb=ep.read_bytes();er=csv.DictReader(io.StringIO(eb.decode()),delimiter='\t');existing=list(er);ef=er.fieldnames
event_rows=[]
for g in guards:
    event={k:'' for k in ef};eid='publish:'+sha(('editorial01:'+g['owner']+sha(g['new'].encode())).encode())[:24]
    event.update(statement_id=g['owner'],date='2026-11-22',who='GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6_SERIES_PUBLISH continuation 2 root',type='used and rechecked in this run',
        outcome='Root read the complete old statement and proof, then the complete proposed statement and proof, and compared every step. Removed draft-history language and duplicated proof-step decoration. All pre-existing displays, labels, tags, hypotheses, constructions and numerical values are preserved. '+('The old failed universal square-only identity is expressed by its already proved explicit half-period witness; the identity-induced degree-six isogeny and all cohomology maps remain in full.' if g['tag']=='01GP' else 'The published two rank-one fibres, rank-two hexagonal fibre and full4B* fibre remain; the exact Viaclovsky locators retain the original credit.')+' No new independent derivation, computational method or required-check closure is claimed. Evidence: records/S6_SERIES_PUBLISH_II_statements_editorial_01/manifest.json.',
        event_id=eid,phase='publication editorial comparison',source_file='records/S6_SERIES_PUBLISH_II_statements_editorial_01/guards.json',source_row=str(len(event_rows)+1),source_event_type='used and rechecked in this run',evidence_group='publish:editorial01:'+g['owner'],date_utc=now,where='Full owning statement and proof, tag '+g['tag'])
    assert not any(e['event_id']==eid for e in existing);event_rows.append(event)
def tail(rows,fields):
    st=io.StringIO(newline='');w=csv.DictWriter(st,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writerows(rows);return st.getvalue().encode()
et=tail(event_rows,ef)
dp=R/'S6_SERIES_PUBLISH_defects_II.tsv';db=dp.read_bytes();dr=csv.DictReader(io.StringIO(db.decode()),delimiter='\t');prior=list(dr);df=dr.fieldnames
defect_rows=[]
for g in guards:
    for c in g['changes']:
        row={k:'' for k in df};row.update(change_id=f'II-STATEMENTS-EDITORIAL-01-{len(defect_rows)+1:03}',type=c['type'],statement_id=g['owner'],old_location='Full owning block, tag '+g['tag'],old_page='pending integrated locator',new_location='Same owning block',new_page='pending integrated PDF',old_text=c['old'],new_text=c['new'],reason=c['reason'],review_status='Complete old/new statement and proof actually read by root; exact inverse and preservation guards pass. Rewording event only; no independent-check or page-reading credit.');defect_rows.append(row)
dtail=tail(defect_rows,df)
(out/'event_rows.tsv').write_bytes(('\t'.join(ef)+'\n').encode()+et)
(out/'defect_rows.tsv').write_bytes(('\t'.join(df)+'\n').encode()+dtail)
(out/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before statements_editorial01',tofile='II after statements_editorial01')))
manifest=dict(created_utc=now,source_before_sha256=sha(old),source_after_sha256=sha(new.encode()),
    guards=binding if False else dict(path=(out/'guards.json').relative_to(R).as_posix(),sha256=sha((out/'guards.json').read_bytes())),
    whole_old_and_new_proofs_actually_read=['01GP','033N'],exact_inverse=True,all_preexisting_displays_labels_and_tags_preserved=True,protected_R13_02XE_blocks_identical=True,
    ledger_before_sha256=sha(eb),ledger_after_sha256=sha(eb+et),ledger_rows_before=len(existing),events_added=2,event_type='used and rechecked in this run',event_ids=[e['event_id'] for e in event_rows],
    defects_before_sha256=sha(db),defects_after_sha256=sha(db+dtail),defect_rows_before=len(prior),defect_rows_added=len(defect_rows),
    required_rows_closed=0,global_defect_classes_closed=0,final_pdf_page_credit=0,
    statement_transport='01GP: the printed negation of a universal square-only identity is witnessed by the same explicit mu=1/2 family already in its proof; the explicit witness is moved into the statement and its maps retained.033N: the identical four fibre types and nilpotent ranks are stated with the same primary-source credit.',
    files=[dict(path=x.relative_to(R).as_posix(),bytes=x.stat().st_size,sha256=sha(x.read_bytes())) for x in sorted(out.iterdir())])
mp=out/'manifest.json';assert not mp.exists();mp.write_text(json.dumps(manifest,indent=2)+'\n')
p.write_text(new)
with ep.open('ab') as f:f.write(et)
with dp.open('ab') as f:f.write(dtail)
note=f'\n\n## Paper II positive mathematical statements and proof presentation — {now}\n\nRewrote the draft-history wording of01GP and033N after reading each complete old and new proof.01GP now states its existing explicit half-period witness and retains the degree-six isogeny and all direct-image calculations;033N states the same published fibre configuration with exact source credit. All old displays, labels, tags and numerical values remain. Added{len(defect_rows)} individual defect rows and two used-and-rechecked events; zero independent-proof, required-row closure, global-class or final-page credit. Record: `records/S6_SERIES_PUBLISH_II_statements_editorial_01/manifest.json`. Source SHA-256 `{sha(new.encode())}`.\n'
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
    with (R/name).open('a') as f:f.write(note)
print(json.dumps({k:v for k,v in manifest.items() if k!='files'},indent=2))
