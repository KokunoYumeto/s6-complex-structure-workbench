from pathlib import Path
import csv, datetime as dt, difflib, hashlib, io, json, re

R=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
source=R/'S6_SERIES_PUBLISH_II.tex'
old=source.read_bytes();s=old.decode()
assert sha(old)=='20750b3f04ff0e5cc4cd949a1423647449e7d963fa76c6fbf3ef41a8a9536908'
ledger=(R/'CHECK_EVENTS.tsv').read_bytes()
assert sha(ledger)=='e0f20711c4867546863ae01f162d29919c641559b816ed9aa74c788f8ebd84ac'
macro=r'\newcommand{\StatementRecord}[4]{{\upshape\footnotesize[tag~\texttt{#3}]}\enspace\ignorespaces}'
assert s.count(macro)==1
with (R/'S6_SERIES_PUBLISH_inventory.csv').open() as f:inv=list(csv.DictReader(f))
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:pages={r['tag']:r['page'] for r in csv.DictReader(f,delimiter='\t')}
body=s[s.index(r'\begin{document}'):]
envs=re.findall(r'\\newtheorem\{([^}]+)\}',s)
pat=r'\\begin\{('+'|'.join(map(re.escape,envs))+r')\}(?:\[[^\n]*?\])?'
guards=[];tagged=0
for m in re.finditer(pat,body):
    end=body.find('\\end{'+m[1]+'}',m.end())
    assert end>=0
    block=body[m.start():end]
    tags=re.findall(r'\\hypertarget\{tag-([^}]+)\}',block)
    labels=re.findall(r'\\label\{([^}]+)\}',block)
    if not tags:continue
    tagged+=1
    if r'\StatementRecord{' in block:continue
    owner,tag=labels[0],tags[0]
    rows=[r for r in inv if r['paper']=='II' and r['tag']==tag]
    assert len(rows)==1 and rows[0]['label']==owner and rows[0]['current_statement_owner']==owner
    assert rows[0]['status']=='proved'
    header=body[m.start():body.index('\n',m.start())]
    assert '\\hypertarget{tag-'+tag+'}' in header and '\\label{'+owner+'}' in header
    line='\\StatementRecord{'+owner+'}{proved}{'+tag+'}{}'
    guards.append(dict(owner=owner,tag=tag,old=header,new=header+'\n'+line,
        reason='Restore the small visible permanent statement tag through the existing tag-only macro. Its status and dependency arguments are not printed. The mathematical statement and proof bytes are unchanged.'))
assert len(guards)==55
new=s
for g in guards:
    assert new.count(g['old'])==1
    new=new.replace(g['old'],g['new'],1)
back=new
for g in reversed(guards):
    assert back.count(g['new'])==1
    back=back.replace(g['new'],g['old'],1)
assert back==s
for pattern in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}']:
    assert re.findall(pattern,s)==re.findall(pattern,new)
assert new.count(r'\StatementRecord{')==s.count(r'\StatementRecord{')+55
out=R/'records/S6_SERIES_PUBLISH_II_visible_tags_01'
assert not out.exists();out.mkdir()
now=dt.datetime.now(dt.timezone.utc).isoformat()
(out/'guards.json').write_text(json.dumps(guards,indent=2)+'\n')
(out/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before tag restoration',tofile='II after tag restoration')))
defects=R/'S6_SERIES_PUBLISH_defects_II.tsv';beforedef=defects.read_bytes()
reader=csv.DictReader(io.StringIO(beforedef.decode()),delimiter='\t');oldrows=list(reader);fields=reader.fieldnames
newrows=[]
for i,g in enumerate(guards,1):
    row={k:'' for k in fields}
    row.update(change_id=f'S6_SERIES_PUBLISH_II_VISIBLE_TAGS_01_{i:03}',type='D10',statement_id=g['owner'],
        old_location='Statement header, tag '+g['tag'],old_page=pages.get(g['tag'],''),new_location='Same statement header',
        old_text=g['old'],new_text=g['new'],reason=g['reason'],
        review_status='Root read all55 old/new header pairs and exact inventory mappings; forward/inverse bytes and label/target preservation verified; no proof rewrite or check credit.')
    newrows.append(row)
stream=io.StringIO(newline='');writer=csv.DictWriter(stream,fieldnames=fields,delimiter='\t',lineterminator='\n');writer.writerows(newrows)
tail=stream.getvalue().encode()
(out/'defect_rows.tsv').write_bytes(('\t'.join(fields)+'\n').encode()+tail)
manifest=dict(created_utc=now,source_before_sha256=sha(old),source_after_sha256=sha(new.encode()),
    statements_with_tags=tagged,missing_visible_records_before=55,restored_visible_records=55,
    statement_record_count_before=s.count(r'\StatementRecord{'),statement_record_count_after=new.count(r'\StatementRecord{'),
    inventory_sha256=sha((R/'S6_SERIES_PUBLISH_inventory.csv').read_bytes()),
    exact_inverse_recovers_source=True,all_labels_targets_manual_equation_tags_unchanged=True,
    all_mathematical_statement_and_proof_bytes_unchanged=True,
    defect_rows_before=len(oldrows),defect_rows_added=55,defect_sha256_before=sha(beforedef),defect_sha256_after=sha(beforedef+tail),
    ledger_sha256=sha(ledger),events_added=0,required_check_closures=0,global_defect_closures=0,visual_reading_credit=0,
    review='All55 missing printed-tag header records and their unique inventory identities were read before this change. The existing macro prints only the small permanent tag. Its exact displayed definition was checked. The reversible insertion changes no theorem statement, hypothesis, formula, or proof. Remaining D10 apparatus still requires the whole-paper pass.',
    files=[dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p.read_bytes())) for p in sorted(out.iterdir())])
(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
source.write_text(new)
with defects.open('ab') as f:f.write(tail)
assert (R/'CHECK_EVENTS.tsv').read_bytes()==ledger
assert defects.read_bytes()[:len(beforedef)]==beforedef
text=f'\n\n## Paper II visible permanent tags — {now}\n\nRestored the small printed permanent tag in55 statement headers whose hypertargets and labels were already intact. Each exact owner/tag/status mapping was checked against the inventory. The existing macro prints only the tag; all mathematical statement and proof bytes, labels, targets and equation tags remain unchanged under the recorded exact inverse. Added55 individual D10 defect rows. No check event, required-check completion, whole-class D10 closure or page-reading credit was added. Record: `records/S6_SERIES_PUBLISH_II_visible_tags_01/manifest.json`. Current source SHA-256 `{sha(new.encode())}`.\n'
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
    with (R/name).open('a') as f:f.write(text)
print(json.dumps(manifest,indent=2))
