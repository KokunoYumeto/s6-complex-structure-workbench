from pathlib import Path
import csv, datetime as dt, difflib, hashlib, io, json, re

R = Path(__file__).resolve().parents[1]
csv.field_size_limit(100_000_000)
def sha(b): return hashlib.sha256(b).hexdigest()
def bind(p):
    b=(R/p).read_bytes(); return dict(path=p,sha256=sha(b),bytes=len(b))
proposal='records/S6_SERIES_PUBLISH_II_bibliography_alias_proposal_01.json'
assert bind(proposal)['sha256']=='0fdf07720d76b0fd8f18f8387c343721ce1d2655bf90d0fd58c3d2daa1b7764f'
p=json.loads((R/proposal).read_text())
assert bind(p['primary_evidence']['path'])==p['primary_evidence']
sp=R/'S6_SERIES_PUBLISH_II.tex';oldb=sp.read_bytes();old=oldb.decode();new=old
assert sha(oldb)=='ebe3e533cc1c922b2a67524fe394e70f54cedf4723febe51507e65af66727ea6'
dp=R/'S6_SERIES_PUBLISH_defects_II.tsv';db=dp.read_bytes()
dr=csv.DictReader(io.StringIO(db.decode(),newline=''),delimiter='\t');previous=list(dr);fields=dr.fieldnames
pattern=r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}'
assert len(re.findall(pattern,old))==131
assert old.count('\\bibitem[Kerr, Laza and Saito(2022)]{KerrLazaSaito2022}')==1
rows=[]; guard_results=[]
for n,g in enumerate(p['guards'],1):
    assert new.count(g['old'])==g['expected_occurrences'],(n,g['old'])
    starts=[m.start() for m in re.finditer(re.escape(g['old']),new)]
    for pos in starts:
        labels=re.findall(r'\\label\{([^}]+)\}',new[:pos])
        owner=g.get('location',labels[-1] if labels else 'front matter')
        rows.append(dict(change_id=f'II-C2-BIBALIAS01-{len(rows)+1:03d}',type=g['type'],statement_id=owner,
            old_location=owner+f'; source line {new[:pos].count(chr(10))+1}',old_page='',
            new_location=owner,new_page='pending integrated PDF',old_text=g['old'],new_text=g['new'],
            reason=g.get('reason','Identify the cited work by the recorded exact author/title/edition/DOI map; retain its locator except for the four independently read published-page substitutions.'),
            review_status='Root read the identity maps, exact source locators and complete guards; mathematical displays and proof inference remain unchanged'))
    before=sha(new.encode());new=new.replace(g['old'],g['new'])
    guard_results.append(dict(number=n,occurrences=len(starts),before_sha256=before,after_sha256=sha(new.encode())))
assert len(rows)==74 and len(guard_results)==58
assert len(re.findall(pattern,new))==125
for pattern in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'(?<!\\)\\\[(.*?)(?<!\\)\\\]']:
    assert re.findall(pattern,old,re.S)==re.findall(pattern,new,re.S)
for m in re.finditer(r'\\cite[a-zA-Z]*\*?(?:\[[^\]]*\]){0,2}\{([^}]+)\}',new):
    assert not (set(k.strip() for k in m.group(1).split(',')) & set(p['aliases']))
assert not ({r['change_id'] for r in rows}&{r['change_id'] for r in previous})
s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
tail=s.getvalue().split('\n',1)[1].encode();assert db.endswith(b'\n')
rd=R/'records/S6_SERIES_PUBLISH_II_bibliography_alias_apply_01';assert not rd.exists();rd.mkdir()
(rd/'source.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='II.before',tofile='II.after')))
(rd/'defect_rows.tsv').write_text(s.getvalue())
(rd/'guard_replay.json').write_text(json.dumps(guard_results,indent=2)+'\n')
now=dt.datetime.now(dt.timezone.utc).isoformat()
manifest=dict(created_utc=now,proposal=bind(proposal),primary_evidence=p['primary_evidence'],
    source_before_sha256=sha(oldb),source_after_sha256=sha(new.encode()),
    defects_before_sha256=sha(db),defects_after_sha256=sha(db+tail),defect_rows_added=len(rows),
    guarded_edits=58,citation_occurrences=64,entries_before=131,entries_after=125,
    proposal_rebinding='The exact58 literal guards and their recorded multiplicities all pass after the mathematical permutation. Admission75 added only the distinct KLS2022 entry, so the entry counts are each increased by1 from the earlier proposal. No old guard is bypassed or weakened.',
    additional_primary_entry=bind('records/S6_SERIES_PUBLISH_II_YB_master_reference_01/manifest.json'),
    master_bibliography=bind('S6_SERIES_PUBLISH_references.bib'),master_changed=False,
    unchanged_labels_targets_displays=True,events_added=0,required_rows_closed=0,global_defect_rows_closed=0,final_page_reading_credit=0,
    scope='Six exact bibliographic aliases consolidated, four canonical entries cleaned and four locators moved to the actual published pages read. Other bibliography defects and the whole-paper final gates remain open.')
(rd/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
sp.write_text(new)
with dp.open('ab') as f:f.write(tail)
assert sp.read_bytes()==new.encode() and dp.read_bytes()==db+tail
text=f'''\n\n## Paper II exact bibliographic aliases and published locators — {now}\n\nThe prepared58 literal guards now apply after the mathematical permutation, with all recorded multiplicities unchanged. Sixty-four citation occurrences are mapped through the explicit work/edition identities, six duplicate entries are consolidated, four canonical entries cleaned, and the four CDP locators point to the actual published pages679,684,685,694 read earlier. The newer KLS2022 entry remains exact, giving125 entries from131. Seventy-four exact per-instance D18/editorial rows and the complete diff are in records/S6_SERIES_PUBLISH_II_bibliography_alias_apply_01. Source SHA256 {manifest['source_after_sha256']}. All labels, targets and mathematical displays remain unchanged. Historical master-bibliography aliases remain for the held papers. No check event or required/global/final-page row closes.\n'''
for name in ('PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md'):
    with (R/name).open('a') as f:f.write(text)
print(json.dumps(manifest,indent=2))
