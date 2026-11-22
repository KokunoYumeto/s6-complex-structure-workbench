from pathlib import Path
import csv, datetime as dt, difflib, hashlib, io, json, re

R=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
p=R/'S6_SERIES_PUBLISH_II.tex';old=p.read_bytes();s=old.decode()
assert sha(old)=='6cd47204ed8a2429e51a692d577831057fb1e6bb0d86ac7d5bc5e76240815a77'
ledger=(R/'CHECK_EVENTS.tsv').read_bytes();tags=(R/'S6_SERIES_PUBLISH_tags.tsv').read_bytes()
titles={
 '01AN':'Finite Picard translations for multiple fibres',
 '01AO':'Ambient cotangent vanishing on smooth multiple fibres',
 '01AY':'Twisted cotangent vanishing on reduced fibre supports',
 '01GC':'Euler sign under trivial torus monodromy',
 '01GE':'A compact torus fibration with trivial monodromy',
 '01GF':'Coherent and integral cohomology of the trivial-monodromy example',
 '01SX':'Comb members with more than two vector fields',
 '033N':'Singular fibres of the two-parameter threefold',
 '01CT':'Commuting semicomplete fields on a component cover',
 '01DA':'Cyclic covers of components with nonnegative Kodaira dimension',
 '01F0':'Anticanonical supports on class VII surfaces',
 '01F1':'Conductor Euler bounds',
 '01F2':'Euler number for class VII normalization',
 '01F3':'Zero Euler number for class VII normalization',
 '01C0':'Elliptic images and Picard restriction',
 '01C2':'Euler sign and equality for reducible fibres',
 '01C4':'Purity of support cohomology',
 '01EA':'Contractions and normal extensions of terminal ruled pairs',
 '01EC':'Leaf contractions, elliptic cores and Euler number',
 '01DP':'Ruling bases of normalization components',
 '01EM':'Canonical-flat cores in the Hopf-minimum case',
 '01EO':'Hopf minimal models at maximal canonical order',
 '01ES':'Exceptional divisors in the component boundary',
 '01ET':'Elliptic parents at marked Hopf interfaces',
 '01EP':'Root base change and birational descent from canonical-flat cores',
}
envs=re.findall(r'\\newtheorem\{([^}]+)\}',s)
catalogue=[];guards=[]
for m in re.finditer(r'\\begin\{('+'|'.join(map(re.escape,envs))+r')\}(?:\[([^\n]*?)\])?',s):
    assert m[2] is not None
    end=s.index('\\end{'+m[1]+'}',m.end())+len('\\end{'+m[1]+'}')
    block=s[m.start():end]
    tag=re.search(r'\\hypertarget\{tag-([^}]+)\}',block)[1]
    owner=re.search(r'\\label\{([^}]+)\}',block)[1]
    title=titles.get(tag,m[2])
    kind='D16' if tag in titles else 'D23'
    if tag not in titles and title[0].islower():title=title[0].upper()+title[1:]
    catalogue.append(dict(tag=tag,owner=owner,environment=m[1],old_title=m[2],new_title=title,
        review='Root read this complete header in the378-header census; the entire statement was additionally read for every substantive title replacement in this pass.',
        remaining_title_work=tag in ['02Y6','02XE','01GP','02UH']))
    if title==m[2]:continue
    old_header=m[0];new_header='\\begin{'+m[1]+'}['+title+']'
    # Bind the first owner label as well so a title collision cannot select another statement.
    first_line=block.splitlines()[0]
    assert first_line.startswith(old_header)
    new_line=new_header+first_line[len(old_header):]
    assert s.count(first_line)==1
    guards.append(dict(tag=tag,owner=owner,type=kind,old=first_line,new=new_line,
        mathematical_body_sha256=sha(block[len(first_line):].encode()),
        exact_map='Identity on every byte after the statement header, including hypotheses, conclusions, formulas, maps, citations and the entire proof.',
        reason='Replace a process/status/input title by the mathematical content of its fully read statement.' if kind=='D16' else 'Capitalize the first English word of the statement title consistently; no word or mathematical content changes.'))
assert len(catalogue)==378 and sum(g['type']=='D16' for g in guards)==25
new=s
for g in guards:
    assert new.count(g['old'])==1;new=new.replace(g['old'],g['new'],1)
back=new
for g in reversed(guards):
    assert back.count(g['new'])==1;back=back.replace(g['new'],g['old'],1)
assert back==s
for pattern in [r'\\label\{([^}]+)\}',r'\\hypertarget\{([^}]+)\}',r'\\tag\{([^}]+)\}']:
    assert re.findall(pattern,s)==re.findall(pattern,new)
for tag in ['02Y6','02XE']:
    def block(text):
        at=text.index('\\hypertarget{tag-'+tag+'}');a=text.rfind('\\begin{proposition}',0,at);b=text.index('\\end{proof}',at)+len('\\end{proof}');return text[a:b]
    assert block(s)==block(new)
defects=R/'S6_SERIES_PUBLISH_defects_II.tsv';before=defects.read_bytes()
rr=csv.DictReader(io.StringIO(before.decode()),delimiter='\t');prior=list(rr);fields=rr.fieldnames
rows=[]
for i,g in enumerate(guards,1):
    row={k:'' for k in fields};row.update(change_id=f'II-TITLES-02-{i:03}',type=g['type'],statement_id=g['owner'],old_location='Statement title, tag '+g['tag'],old_page='pending integrated locator',new_location='Same statement title',new_page='pending integrated PDF',old_text=g['old'],new_text=g['new'],reason=g['reason'],review_status='Root read the complete378-header census and each fully replaced statement; identity on mathematical bodies/proofs and exact inverse verified. No new proof or page-reading credit.')
    rows.append(row)
st=io.StringIO(newline='');w=csv.DictWriter(st,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writerows(rows);tail=st.getvalue().encode()
out=R/'records/S6_SERIES_PUBLISH_II_titles_02';assert not out.exists();out.mkdir()
(out/'header_census.json').write_text(json.dumps(catalogue,indent=2)+'\n')
(out/'guards.json').write_text(json.dumps(guards,indent=2)+'\n')
(out/'source.diff').write_text(''.join(difflib.unified_diff(s.splitlines(True),new.splitlines(True),fromfile='II before title pass02',tofile='II after title pass02')))
(out/'defect_rows.tsv').write_bytes(('\t'.join(fields)+'\n').encode()+tail)
now=dt.datetime.now(dt.timezone.utc).isoformat()
manifest=dict(created_utc=now,source_before_sha256=sha(old),source_after_sha256=sha(new.encode()),all_headers_actually_read=378,
    substantive_title_replacements=25,capitalization_changes=sum(g['type']=='D23' for g in guards),
    mathematical_statement_and_proof_bodies_byte_identical=True,exact_inverse_verified=True,
    all_labels_tags_and_equation_tags_unchanged=True,protected_R13_02XE_blocks_unchanged=True,
    defect_rows_before=len(prior),defect_rows_added=len(rows),defect_sha256_before=sha(before),defect_sha256_after=sha(before+tail),
    ledger_sha256=sha(ledger),tags_sha256=sha(tags),events_added=0,required_rows_closed=0,global_defect_classes_closed=0,final_pdf_page_credit=0,
    remaining_D16_headers=['02Y6','02XE','01GP','02UH'],
    files=[dict(path=x.relative_to(R).as_posix(),bytes=x.stat().st_size,sha256=sha(x.read_bytes())) for x in sorted(out.iterdir())])
(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
p.write_text(new)
with defects.open('ab') as f:f.write(tail)
assert (R/'CHECK_EVENTS.tsv').read_bytes()==ledger and (R/'S6_SERIES_PUBLISH_tags.tsv').read_bytes()==tags
note=f'\n\n## Paper II whole-header census and title pass02 — {now}\n\nActually read all378 current statement headers. Replaced25 further status/process/input titles after reading their complete statements, and capitalized{manifest["capitalization_changes"]} other title openings. Every statement body and proof remains byte-identical under the exact inverse; all labels and tags are unchanged. R13 and02XE remain untouched for the ongoing correction. Four headers still require the associated mathematical/editorial disposition:02Y6,02XE,01GP,02UH. Added{len(rows)} individual D16/D23 rows; no events, required-row closure, global-class closure or final-PDF credit. Record: `records/S6_SERIES_PUBLISH_II_titles_02/manifest.json`. Source SHA-256 `{sha(new.encode())}`.\n'
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
    with (R/name).open('a') as f:f.write(note)
print(json.dumps(manifest,indent=2))
