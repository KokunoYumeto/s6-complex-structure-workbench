from pathlib import Path
import csv, datetime as dt, difflib, hashlib, io, json, re

R=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
p=R/'S6_SERIES_PUBLISH_II.tex';old=p.read_bytes();s=old.decode()
assert sha(old)=='15494de2be677940c4fb80ff896254b4e6b305be2ab1816842acc1b99f4a65a1'
ledger=(R/'CHECK_EVENTS.tsv').read_bytes()
titles={
 '02XD':'Fundamental group and first two homology groups',
 '02Y3':'Euler characteristic of a tacnodal conductor',
 '02Y4':'Tacnodal supports of Euler number zero',
 '02Y5':'Components outside the pole divisor of a ruled fibre',
 '02XB':'Local exclusions for ordinary double curves',
 '02XC':'Pole coefficients over an ordinary triple curve',
 '02Y7':'Local models along a smooth tacnodal critical curve',
 '02Y8':'Product germs from a nonzero Hessian',
 '02XH':'Euler bound for uniform cuspidal ruled supports',
 '02XF':'Hessian defect at a nodal critical curve',
 '02XG':'Two identifications in the tacnodal ruled case',
 '02XI':'The contracted section and three-branch critical point',
 '02XJ':'Planar critical curves of ordinary triple type',
 '02XK':'Euler bound for uniform ordinary-triple ruled supports',
 '02XL':'Rational normalization for a nondegenerate quartic square',
 '02XM':'Conductor defects at three-branch critical points',
 '02XN':'Rational normalization at a three-axis critical point',
 '02Y9':'The defect of a tacnode with a transverse line',
 '02YA':'Defect bounds at nonordinary three-branch points',
 '02XP':'Euler bound for uniform tacnodal ruled supports',
 '02XX':'Classification and Euler numbers of torus-fibre supports',
 '01CY':'Descent of the rank-one component fibration',
 '01E8':'Unicyclic supports with elliptic quasi-bundle torsors',
 '01EH':'Elliptic fibrations and vertical point blowups',
}
guards=[]
for tag,title in titles.items():
    at=s.index('\\hypertarget{tag-'+tag+'}')
    start=s.rfind('\\begin{proposition}[',0,at)
    end=s.index('\\end{proposition}',at)+len('\\end{proposition}')
    block=s[start:end]
    assert '\\hypertarget{tag-'+tag+'}' in block.splitlines()[0]
    header=block.splitlines()[0]
    match=re.match(r'(\\begin\{proposition\})\[([^\n]+)\](.*)',header)
    assert match
    owner=re.search(r'\\label\{([^}]+)\}',header)[1]
    new=match[1]+'['+title+']'+match[3]
    assert header!=new and s.count(header)==1
    guards.append(dict(type='D16',owner=owner,tag=tag,old=header,new=new,
        original_statement_sha256=sha(block.encode()),statement_body_sha256=sha(block[len(header):].encode()),
        exact_map='Identity on the complete mathematical statement body and proof; only the optional title argument is replaced.',
        reason='Replace the run-number or process title by a short title describing the exact statement, after reading the full statement and its scope.'))

standing_start=s.index('\\paragraph{Standing torus-fibration setting.}')
standing_end=s.index('\\subsection',standing_start)
standing=s[standing_start:standing_end]
assert len(standing.encode())==599
assert sha(standing.encode())=='377151e024d56c1e5d777516f6b60819c7ab99b8c4a67c761e89e99614794cd9'
prefix='\\paragraph{Standing torus-fibration setting.} '
assert standing.startswith(prefix) and standing.endswith('\n')
body=standing[len(prefix):]
tag='P204';owner='def:II:standing-torus-fibration'
tagfile=R/'S6_SERIES_PUBLISH_tags.tsv';beforetags=tagfile.read_bytes()
assert tag not in s
tr=csv.DictReader(io.StringIO(beforetags.decode()),delimiter='\t');oldtags=list(tr);tagfields=tr.fieldnames
assert not any(x['tag']==tag or x['label']==owner for x in oldtags)
replacement='\\begin{definition}[The standing torus-fibration setting]\\hypertarget{tag-'+tag+'}{}\\label{'+owner+'}\n'
replacement+='\\StatementRecord{'+owner+'}{proved}{'+tag+'}{}\n'+body+'\\end{definition}\n'
guards.append(dict(type='D13',owner=owner,tag=tag,old=standing,new=replacement,
    statement_body_sha256=sha(body.encode()),
    exact_map='Identity on every byte of the standing setting body, from The ambient space through state their own assumptions. The paragraph wrapper becomes a numbered definition with a fresh permanent tag and label.',
    reason='Number the standing definition on which the irreducible-support statements depend, preserving every hypothesis and scope sentence verbatim.'))

new=s
for g in guards:
    assert new.count(g['old'])==1
    new=new.replace(g['old'],g['new'],1)
back=new
for g in reversed(guards):
    assert back.count(g['new'])==1
    back=back.replace(g['new'],g['old'],1)
assert back==s
for pattern,added in [(r'\\label\{([^}]+)\}',[owner]),(r'\\hypertarget\{([^}]+)\}',['tag-'+tag])]:
    a=re.findall(pattern,s);b=re.findall(pattern,new)
    for extra in added:
        assert b.count(extra)==1;b.remove(extra)
    assert a==b
assert re.findall(r'\\tag\{([^}]+)\}',s)==re.findall(r'\\tag\{([^}]+)\}',new)
for protected in ['02Y6','02XE']:
    def get_block(text):
        at=text.index('\\hypertarget{tag-'+protected+'}')
        start=text.rfind('\\begin{proposition}',0,at)
        end=text.index('\\end{proof}',at)+len('\\end{proof}')
        return text[start:end]
    assert get_block(s)==get_block(new)

defects=R/'S6_SERIES_PUBLISH_defects_II.tsv';beforedef=defects.read_bytes()
dr=csv.DictReader(io.StringIO(beforedef.decode()),delimiter='\t');oldrows=list(dr);fields=dr.fieldnames
with (R.parent/'S6_SERIES_GRIND_tags.tsv').open() as f:pages={r['tag']:r['page'] for r in csv.DictReader(f,delimiter='\t')}
rows=[]
for i,g in enumerate(guards,1):
    row={k:'' for k in fields};row.update(change_id=f'II-TITLES-DEFINITION-01-{i:03}',type=g['type'],statement_id=g['owner'],
        old_location='Statement title, tag '+g['tag'] if g['type']=='D16' else 'Standing torus-fibration setting paragraph',
        old_page=pages.get(g['tag'],'pending integrated locator'),new_location='Same mathematical statement' if g['type']=='D16' else 'Numbered standing definition, tag P204',new_page='pending integrated PDF',
        old_text=g['old'],new_text=g['new'],reason=g['reason'],
        review_status='Root read the complete statements and standing scope; exact identity on their mathematical bodies, exact inverse, protected R13/02XE blocks and label/tag preservation verified. No proof/check/page credit.')
    rows.append(row)
def tail(rows,fields):
    st=io.StringIO(newline='');w=csv.DictWriter(st,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writerows(rows);return st.getvalue().encode()
dtail=tail(rows,fields)
tagrow={k:'' for k in tagfields};tagrow.update(tag=tag,paper='II',number='pending build',page='pending build',label=owner,status='proved',kind='definition',current_owner=owner,publication_disposition='new numbered definition; verbatim transport of the standing setting; permanent identity')
ttail=tail([tagrow],tagfields)
out=R/'records/S6_SERIES_PUBLISH_II_titles_definition_01';assert not out.exists();out.mkdir()
(out/'guards.json').write_text(json.dumps(guards,indent=2)+'\n')
(out/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before title/definition edit',tofile='II after title/definition edit')))
(out/'defect_rows.tsv').write_bytes(('\t'.join(fields)+'\n').encode()+dtail)
(out/'tag_row.tsv').write_bytes(('\t'.join(tagfields)+'\n').encode()+ttail)
now=dt.datetime.now(dt.timezone.utc).isoformat()
manifest=dict(created_utc=now,source_before_sha256=sha(old),source_after_sha256=sha(new.encode()),
    titles_replaced=len(titles),definitions_numbered=1,statement_and_proof_bodies_unchanged=True,
    protected_blocks_byte_identical=['night:P4R.13','night:P4.40'],
    identity_and_inverse_verified=True,all_old_labels_targets_equation_tags_preserved=True,
    new_permanent_tag=tag,new_label=owner,
    defect_rows_before=len(oldrows),defect_rows_added=len(rows),defect_sha256_before=sha(beforedef),defect_sha256_after=sha(beforedef+dtail),
    tags_sha256_before=sha(beforetags),tags_sha256_after=sha(beforetags+ttail),
    ledger_sha256=sha(ledger),events_added=0,required_rows_completed=0,global_defect_classes_closed=0,final_pdf_page_credit=0,
    remaining='Complete the two mathematically affected R13/02XE titles after their exact comparison, then finish the whole-header D16 audit. Printed legacy references to Part4.2 still require exact receiving-map edits.',
    files=[dict(path=x.relative_to(R).as_posix(),bytes=x.stat().st_size,sha256=sha(x.read_bytes())) for x in sorted(out.iterdir())])
(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
p.write_text(new)
with defects.open('ab') as f:f.write(dtail)
with tagfile.open('ab') as f:f.write(ttail)
assert (R/'CHECK_EVENTS.tsv').read_bytes()==ledger
assert defects.read_bytes()[:len(beforedef)]==beforedef
assert tagfile.read_bytes()[:len(beforetags)]==beforetags
note=f'\n\n## Paper II mathematical statement titles and standing definition — {now}\n\nReplaced24 run-number/process titles after reading their exact statements. Every mathematical statement body and proof remains byte-identical. The599-byte standing-setting paragraph is now Definition tagP204, with its entire body verbatim and a fresh label. The R13 and02XE statement/proof blocks remain byte-identical for the ongoing mathematical comparison. Added25 individual D16/D13 rows; no check events, required-row closure, whole-class closure or PDF-page credit. The exact guard and inverse record is `records/S6_SERIES_PUBLISH_II_titles_definition_01/manifest.json`; source SHA-256 `{sha(new.encode())}`.\n'
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
    with (R/name).open('a') as f:f.write(note)
print(json.dumps(manifest,indent=2))
