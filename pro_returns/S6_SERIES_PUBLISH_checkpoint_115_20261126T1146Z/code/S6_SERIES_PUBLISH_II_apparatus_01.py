from pathlib import Path
import collections, csv, datetime as dt, difflib, hashlib, io, json, re

R=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
p=R/'S6_SERIES_PUBLISH_II.tex';old=p.read_bytes();s=old.decode()
assert sha(old)=='cc722e56465b617c896c6352b23803d8db2f98d5cfa9a00aedcc65717d8884ef'
ledger=(R/'CHECK_EVENTS.tsv').read_bytes();tags=(R/'S6_SERIES_PUBLISH_tags.tsv').read_bytes()
records=list(re.finditer(r'\\StatementRecord\{([^}]+)\}\{[^}]*\}\{([^}]+)\}',s))
guards=[]
def owner_at(pos):
    m=[m for m in records if m.start()<pos][-1]
    return m[1],m[2]
for m in re.finditer(r'\\Uses\{',s):
    end=m.end();depth=1
    while depth:
        if s[end]=='{':depth+=1
        elif s[end]=='}':depth-=1
        end+=1
    owner,tag=owner_at(m.start());text=s[m.start():end]
    guards.append(dict(owner=owner,tag=tag,kind='printed dependency list',old=text,new='',
        exact_map='The complete dependency text is copied verbatim to this statement\u2019s check-file entry. Every statement and proof byte remains unchanged.'))
assert len(guards)==18
for m in re.finditer(r'\\hyperlink\{outline-II-',s):
    end=s.index('\n\n',m.start());owner,tag=owner_at(m.start())
    text=s[m.start():end]
    assert 'full statement' in text
    guards.append(dict(owner=owner,tag=tag,kind='printed outline/back-link apparatus',old=text,new='',
        exact_map='The complete navigation text is copied verbatim to the corresponding main-theorem check-file entry. All target anchors, the actual outlines and every mathematical statement remain unchanged.'))
assert len(guards)==25 and len({g['tag'] for g in guards})==25
new=s
for g in guards:
    # The generic dependency phrase occurs three times.  Associate each exact
    # occurrence with its already verified owner rather than replacing by text.
    candidates=[m.start() for m in re.finditer(re.escape(g['old']),s)]
    candidates=[at for at in candidates if owner_at(at)==(g['owner'],g['tag'])]
    assert len(candidates)==1
    g['offset_before']=candidates[0]
for g in sorted(guards,key=lambda g:g['offset_before'],reverse=True):
    at=g['offset_before'];end=at+len(g['old'])
    assert new[at:end]==g['old']
    new=new[:at]+new[end:]
# The deleted strings are metadata outside all proof environments.  The exact
# inverse uses original offsets, avoiding any ambiguity in empty replacements.
reconstructed=new
for g in sorted(guards,key=lambda g:g['offset_before']):
    reconstructed=reconstructed[:g['offset_before']]+g['old']+reconstructed[g['offset_before']:]
assert reconstructed==s
proofs=lambda t:re.findall(r'\\begin\{proof\}.*?\\end\{proof\}',t,re.S)
assert proofs(s)==proofs(new)
for pattern in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\StatementRecord\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}',r'\\tag\{([^}]+)\}']:
    assert re.findall(pattern,s)==re.findall(pattern,new)
# Every external work cited in the removed lists remains cited in prose/proofs.
cites=lambda t:[key.strip() for m in re.finditer(r'\\cite\w*(?:\[[^\]]*\])?\{([^}]+)\}',t) for key in m[1].split(',')]
assert set(cites(''.join(g['old'] for g in guards)))<=set(cites(new))
assert not re.search(r'\\Uses\{',new) and not re.search(r'\\hyperlink\{outline-II-',new)
cp=R/'S6_SERIES_PUBLISH_checks_II.md';cb=cp.read_bytes();cs=cb.decode();cn=cs
for g in guards:
    anchor='<a id="tag-'+g['tag']+'"></a>'
    assert cn.count(anchor)==1
    a=cn.index(anchor);b=cn.find('<a id="tag-',a+len(anchor));b=len(cn) if b<0 else b
    block=cn[a:b];mark='### Check events\n'
    assert block.count(mark)==1
    supplement=('### Preserved dependency and navigation metadata\n\n'
       'Removed from the printed manuscript by the statement-header rule; retained verbatim here. '
       'This relocation adds no mathematical checking event.\n\n```tex\n'+g['old']+'\n```\n\n')
    block=block.replace(mark,supplement+mark,1);cn=cn[:a]+block+cn[b:]
defects=R/'S6_SERIES_PUBLISH_defects_II.tsv';db=defects.read_bytes()
rr=csv.DictReader(io.StringIO(db.decode()),delimiter='\t');prior=list(rr);fields=rr.fieldnames
rows=[]
for i,g in enumerate(guards,1):
    row={k:'' for k in fields};row.update(change_id=f'II-APPARATUS-01-{i:03}',type='D10',statement_id=g['owner'],old_location=g['kind']+', tag '+g['tag'],old_page='pending integrated locator',new_location='S6_SERIES_PUBLISH_checks_II.md#tag-'+g['tag'],new_page='check file',old_text=g['old'],new_text='Preserved verbatim in the statement check-file entry.',reason='Move printed dependency/back-link apparatus to the check file under section3.2; all mathematical statements and proofs remain byte-identical.',review_status='Root read every removed list and its surrounding source; exact inverse, complete proof identity and label/tag preservation verified. Zero proof or final-page credit.')
    rows.append(row)
st=io.StringIO(newline='');w=csv.DictWriter(st,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writerows(rows);tail=st.getvalue().encode()
out=R/'records/S6_SERIES_PUBLISH_II_apparatus_01';assert not out.exists();out.mkdir()
(out/'guards.json').write_text(json.dumps(guards,indent=2)+'\n')
(out/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before apparatus01',tofile='II after apparatus01')))
(out/'checks.diff').write_text(''.join(difflib.unified_diff(cs.splitlines(True),cn.splitlines(True),fromfile='II check file before apparatus01',tofile='II check file after apparatus01')))
(out/'defect_rows.tsv').write_bytes(('\t'.join(fields)+'\n').encode()+tail)
now=dt.datetime.now(dt.timezone.utc).isoformat()
manifest=dict(created_utc=now,source_before_sha256=sha(old),source_after_sha256=sha(new.encode()),check_file_before_sha256=sha(cb),check_file_after_sha256=sha(cn.encode()),
    execution_history=[dict(attempt=1,result='Pre-write guard rejected repeated generic Uses text; no file writes.',repair='Bind each occurrence to its exact owner and source offset under the unchanged full-source hash guard.'),dict(attempt=2,result='All guards and exact inverse passed.')],
    dependency_lists_relocated=18,navigation_paragraphs_relocated=7,metadata_preserved_verbatim=True,
    exact_inverse_verified=True,all_proof_blocks_byte_identical=True,all_labels_tags_and_equation_tags_unchanged=True,
    removed_external_citation_keys_still_cited=sorted(set(cites(''.join(g['old'] for g in guards)))),
    defect_rows_before=len(prior),defect_rows_added=len(rows),defect_sha256_before=sha(db),defect_sha256_after=sha(db+tail),
    ledger_sha256=sha(ledger),tags_sha256=sha(tags),events_added=0,required_rows_closed=0,global_defect_classes_closed=0,final_pdf_page_credit=0,
    remaining_D10_review='Historical refuted block02UH and final whole-source/page census remain open.',
    files=[dict(path=x.relative_to(R).as_posix(),bytes=x.stat().st_size,sha256=sha(x.read_bytes())) for x in sorted(out.iterdir())])
(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
p.write_text(new);cp.write_text(cn)
with defects.open('ab') as f:f.write(tail)
assert (R/'CHECK_EVENTS.tsv').read_bytes()==ledger and (R/'S6_SERIES_PUBLISH_tags.tsv').read_bytes()==tags
note=f'\n\n## Paper II printed dependency/navigation apparatus — {now}\n\nRelocated all18 printed Uses lists and seven main-theorem outline/back-link paragraphs verbatim into their25 check-file entries. Root read every removed list and its surrounding source. The source inverse is exact; every proof block, label, tag and equation tag is unchanged, and all external citation keys in the lists remain cited in the manuscript. Added25 D10 instance rows. D10 remains open for the historical02UH block and the whole-source/page census. Zero events, required-row closures or final-PDF credit. Record: `records/S6_SERIES_PUBLISH_II_apparatus_01/manifest.json`. Source SHA-256 `{sha(new.encode())}`.\n'
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
    with (R/name).open('a') as f:f.write(note)
print(json.dumps(manifest,indent=2))
