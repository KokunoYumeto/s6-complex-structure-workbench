"""Prepare a bounded reference-only proposal; never write canonical files."""
from pathlib import Path
import csv, datetime, difflib, hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'S6_SERIES_PUBLISH_II_A2_Picard_reference_transport_01'
OUT = ROOT / 'agents/continuation2_A' / (PREFIX + '_working')
FINAL = 'agents/continuation2_A/' + PREFIX + '_final_v1'
OUT.mkdir(exist_ok=True)
SOURCE = ROOT / 'S6_SERIES_PUBLISH_II.tex'
s = SOURCE.read_text()
sha = lambda x: hashlib.sha256(x.encode() if isinstance(x, str) else x).hexdigest()
source_sha = sha(SOURCE.read_bytes())
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(name, value):
    (OUT / (PREFIX + '_' + name + '.json')).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

spec = {
    'fam:src:A.1.1': ('7.2', '42', '01PZ', 'proposition.7.2'),
    'fam:src:A.1.2': ('7.4', '43', '01Q0', 'proposition.7.4'),
    'fam:src:A.3.1': ('7.5', '44', '01Q2', 'proposition.7.5'),
    'inv:B3.1': ('23.7', '259', '01S7', 'proposition.23.7'),
    'mapsI:src:A.1.2': ('16.4', '114', '02PB', 'proposition.16.4'),
    'push:src:E.3.1': ('12.1', '77', '033I', 'proposition.12.1'),
    'pub:I:eq:PD7': ('7.8', '45', None, 'equation.7.8'),
    'pub:I:eq:PD8': ('7.9', '45', None, 'equation.7.9'),
    'pub:I:eq:PD11': ('7.12', '45', None, 'equation.7.12'),
}
aux_path = ROOT / 'build/I_candidate19/S6_SERIES_PUBLISH_I.aux'
aux = aux_path.read_text()
tags_path = ROOT / 'S6_SERIES_PUBLISH_tags.tsv'
with tags_path.open() as f:
    tag_rows = [r for r in csv.DictReader(f, delimiter='\t') if r['paper'] == 'I' and r['label'] in spec]
inventory_path = ROOT / 'S6_SERIES_PUBLISH_inventory.csv'
with inventory_path.open() as f:
    inv_rows = [r for r in csv.DictReader(f) if r['paper'] == 'I' and r['label'] in spec]
mapping = []
for label, (number, page, tag, dest) in spec.items():
    lines = [x for x in aux.splitlines() if x.startswith('\\newlabel{' + label + '}')]
    assert len(lines) == 1 and '{{' + number + '}{' + page + '}' in lines[0]
    assert '{' + dest + '}' in lines[0]
    if tag:
        t = [r for r in tag_rows if r['label'] == label]
        i = [r for r in inv_rows if r['label'] == label]
        assert len(t) == len(i) == 1 and t[0]['tag'] == i[0]['tag'] == tag
        assert i[0]['current_number'] == number and i[0]['current_page'] == page
    mapping.append(dict(label=label, paper='I', number=number, page=page, tag=tag,
                        aux_destination=dest, hyperlink_destination='tag-' + tag if tag else dest,
                        exact_aux_line=lines[0]))
cp_line = [x for x in (ROOT.parent / 'CP21_INDEX.tsv').read_text().splitlines()
           if x.startswith('build/I_candidate20/S6_SERIES_PUBLISH_I.aux\t')]
assert len(cp_line) == 1 and sha(aux_path.read_bytes()) in cp_line[0]
dump('I_metadata', dict(created_utc=now, source_snapshot_sha256=source_sha, mapping=mapping,
    files=[dict(path=str(p.relative_to(ROOT)), sha256=sha(p.read_bytes())) for p in [aux_path,tags_path,inventory_path]],
    exact_checkpoint_copy_row=cp_line[0],
    current_I_selected_inventory_fields=[{k:r[k] for k in ['paper','label','tag','kind','current_number','current_page','current_statement_owner']} for r in inv_rows],
    I_final_source_sha256='179fcc4e85fb7902aaf978bcd809cf9928ebc0a46cda5628d5096e6fa0011d74',
    I_final_pdf_sha256='62d84285f35aa6e6ce03b83efbcf2a96e880fda6206eb24c05ab8e66fe799dd6',
    published_v1_numbering_basis='Prompt 0.2 lists only two accents, a family-name clarification and a records link; admitted I candidate20 aux is the exact candidate19 copy above. No I source, PDF or build was opened or run for this transport.',
    final_reference_gate='Regenerate every cross-paper reference at the five-together stage. The deliverable-relative S6_SERIES_PUBLISH_I.pdf path is specified by the prompt; no remote-file existence claim is made.',
    exposure_limitation='An earlier metadata lookup printed II_03DS_current_I_input_transport.json including archived I statement/partial-proof extracts, and a cat of I_candidate19_source_AG_binding.json unexpectedly returned embedded old/current I proof text, truncated. These incidental metadata-embedded exposures were reported to root. They are not a complete I reread or a new check. Subsequent access used selected metadata fields and exact aux lines only.'))

guards=[]
def guard(old,new,owner,tag,classes,reason):
    assert old != new and s.count(old) == 1, (owner, old[:100], s.count(old))
    a=s.index(old); b=a+len(old)
    g=dict(id=f'A2-REF01-{len(guards)+1:02d}',owner=owner,tag=tag,old=old,new=new,
           expected_count=1,old_sha256=sha(old),new_sha256=sha(new),defect_ids=classes,reason=reason,
           source_snapshot_sha256=source_sha,source_character_span=[a,b],
           source_byte_span=[len(s[:a].encode()),len(s[:b].encode())],
           source_line_span=[s.count('\n',0,a)+1,s.count('\n',0,b)+1])
    guards.append(g)
    return g

owners = [('IC','wbII:prop:analytic-ah-boundary','03IH'),
          ('IN','wbII:prop:local-cusp-picard-obstruction','03IN'),
          ('DR','wbII:cor:candidate-conductor-actual','03DR')]
preservation=[]
for short,owner,tag in owners:
    f=ROOT / f'agents/continuation2_B/Picard_D12/final_v1/S6_SERIES_PUBLISH_II_B2_Picard_D12_{short}_proposed.tex'
    old=f.read_text(); assert s.count(old)==1
    new=old
    owner_guards=[]
    for m in re.finditer(r'\\CompendiumRef\{I\}\{([^}]+)\}',old):
        label=m.group(1)
        if label not in spec: continue
        a=old.rfind('\n',0,m.start())+1; b=old.find('\n',m.end())
        if b<0: b=len(old)
        before=old[a:b]; after=before.replace(m.group(0),'\\SeriesRef{'+label+'}')
        owner_guards.append(guard(before,after,owner,tag,['D04','D06'],
            'Replace the printed compendium/raw-label call by the exact current I number, page and destination for the identical label.'))
        assert new.count(before)==1;new=new.replace(before,after)
    for suffix,body in [('before',old),('after',new)]:
        (OUT/f'{PREFIX}_{short}_{suffix}.tex').write_text(body)
    (OUT/f'{PREFIX}_{short}_exact.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=f'{short}_before',tofile=f'{short}_after')))
    inverse=[dict(id=g['id']+'-inverse',old=g['new'],new=g['old'],expected_count=1) for g in reversed(owner_guards)]
    (OUT/f'{PREFIX}_{short}_inverse_guards.json').write_text(json.dumps(inverse,indent=2)+'\n')
    normalize=lambda x:re.sub(r'\\(?:CompendiumRef\{I\}|SeriesRef)\{([^}]+)\}',r'REF{\1}',x)
    assert normalize(old)==normalize(new)
    displays=lambda x:re.findall(r'\\\[(.*?)\\\]',x,re.S)
    labels=lambda x:re.findall(r'\\(?:label|hypertarget|tag)\{[^}]*\}',x)
    enums=lambda x:re.findall(r'\\begin\{enumerate\}(?:\[[^\n]*\])?',x)
    assert displays(old)==displays(new) and labels(old)==labels(new) and enums(old)==enums(new)
    assert old.count('\\item')==new.count('\\item')
    preservation.append(dict(owner=owner,tag=tag,short=short,before_sha256=sha(old),after_sha256=sha(new),
        before_bytes=len(old.encode()),after_bytes=len(new.encode()),calls_transported=len(owner_guards),
        item_tokens_preserved=old.count('\\item'),display_blocks_preserved=len(displays(old)),
        all_math_and_other_bytes_equal_after_exact_reference_token_projection=True,
        all_labels_tags_and_enum_formats_equal=True))
assert sum(x['calls_transported'] for x in preservation)==12

macro_before=[];macro_after=[]
for label,(number,page,tag,dest) in spec.items():
    target='tag-'+tag if tag else dest
    shown='I.'+number if tag else 'I.('+number+')'
    new='\\expandafter\\def\\csname SRef@'+label+'\\endcsname{\\href{S6_SERIES_PUBLISH_I.pdf\\#nameddest='+target+'}{'+shown+' (p.~'+page+')} }'
    existing=[x for x in s.splitlines() if x.startswith('\\expandafter\\def\\csname SRef@'+label+'\\endcsname')]
    if tag:
        assert len(existing)==1
        guard(existing[0],new,'shared I reference macro','', ['D06'],
              'Correct stale number/page metadata and align the relative PDF path with the specified final deliverable; preserve the exact permanent tag destination.')
        macro_before.append(existing[0]);macro_after.append(new)
    else:
        assert not existing
        macro_after.append(new)
insert='\n'.join(macro_after[-3:])+'\n'
anchor='\\expandafter\\def\\csname SRef@fam:src:A.3.1\\endcsname'
anchorline=[x for x in s.splitlines() if x.startswith(anchor)][0]
# Insert at the following unchanged line, so the six macro changes and insertion are disjoint.
pos=s.index(anchorline)+len(anchorline)+1
nextline=s[pos:s.find('\n',pos)]
assert nextline and s.count(nextline)==1
guard(nextline,insert+nextline,'three I equation reference definitions','',['D06'],
      'Provide current I equation numbers/pages with the exact destinations recorded in admitted I auxiliary metadata.')
(OUT/f'{PREFIX}_macros_before.tex').write_text('\n'.join(macro_before)+'\n')
(OUT/f'{PREFIX}_macros_after.tex').write_text('\n'.join(macro_after)+'\n')

candidate=s
for g in guards:
    assert candidate.count(g['old'])==1;candidate=candidate.replace(g['old'],g['new'])
inverse=[]
for g in reversed(guards):
    assert candidate.count(g['new'])==1
    inverse.append(dict(id=g['id']+'-inverse',old=g['new'],new=g['old'],expected_count=1))
    candidate=candidate.replace(g['new'],g['old'])
assert candidate==s
dump('guards',guards);dump('inverse_guards',inverse);dump('preservation',preservation)

unresolved=[]
for m in re.finditer(r'\\CompendiumRef\{I\}\{(wb:prop:period-input-audit|wb:thm:candidate-cusp-geometry|wb:prop:candidate-finite-fillings)\}',s):
    a=s.rfind('\n\n',0,m.start())+2;b=s.find('\n\n',m.end())
    if b<0:b=len(s)
    unresolved.append(dict(label=m.group(1),source_character_span=[m.start(),m.end()],
        source_line=s.count('\n',0,m.start())+1,exact_call=m.group(0),context=s[a:b],
        classes=['D04','D06'],status='open; exact numbered-current-I identity for this inference not established; no guessed replacement'))
assert len(unresolved)==5
dump('unresolved',dict(source_snapshot_sha256=source_sha,uses=unresolved,
    transferred_to_B=dict(label='wbII:eq:W:5.2',exact_call='\\CompendiumRef{II}{wbII:eq:W:5.2}',
        status='missing exact current label/tag/inventory owner; unnumbered nodal-counterexample introduction, reserved to B conormal/nodal consolidation; no transport proposed'),
    coverage='28 active CompendiumRef calls after B admission: twelve transported here, five unresolved historical I setup uses, one nodal same-paper orphan transferred to B, ten elsewhere.'))

existing=[]
body_start=s.index('\\begin{document}')
for label in spec:
    for m in re.finditer(re.escape('\\SeriesRef{'+label+'}'),s[body_start:]):
        at=body_start+m.start();a=s.rfind('\n',0,at)+1;b=s.find('\n',at)
        existing.append(dict(label=label,line=s.count('\n',0,at)+1,text=s[a:b],note='Shared macro change only; no receiving-proof edit or new whole-proof check claimed.'))
dump('shared_macro_occurrences',existing)
with (OUT/f'{PREFIX}_defects.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['id','type','owner','tag','guard_id','old_text','new_text','instance_scope','status'],delimiter='\t')
    w.writeheader()
    for g in guards:
        for d in g['defect_ids']:
            w.writerow(dict(id=g['id']+'-'+d,type=d,owner=g['owner'],tag=g['tag'],guard_id=g['id'],old_text=g['old'],new_text=g['new'],instance_scope='printed reference call' if g['tag'] else 'supporting macro-definition edit; not an additional printed instance',status='proposed; canonical source unchanged'))
    for j, row in enumerate(existing, 1):
        label=row['label']
        g=next(g for g in guards if g['old'].startswith('\\expandafter\\def\\csname SRef@'+label+'\\endcsname'))
        old_text=re.search(r'\{(I\.[^{}]+)\}',g['old']).group(1)
        new_text=re.search(r'\{(I\.[^{}]+)\}',g['new']).group(1)
        w.writerow(dict(id=f'A2-REF01-SHARED-{j:02d}-D06',type='D06',owner='existing printed SeriesRef call at snapshot line '+str(row['line']),tag='',guard_id=g['id'],old_text=old_text,new_text=new_text,instance_scope='printed expansion of unchanged call: '+row['text'],status='proposed shared-macro effect; receiving proof untouched'))
dump('verification',dict(created_utc=now,source_sha256=source_sha,guard_count=len(guards),
    transported_calls=12,shared_macro_updates=6,new_equation_definitions=3,disjoint_insertion_guards=1,
    exact_forward_inverse_replay=True,canonical_mutations=0,
    old_new_reference_projection='For every complete IC/IN/DR block, replace both CompendiumRef{I}{label} and SeriesRef{label} by REF{label}; the resulting texts are byte-identical.',
    new_independent_check_credit=0,I_source_or_PDF_opened=False,I_build_run=False))
print(json.dumps(dict(source_sha256=source_sha,guards=len(guards),owners=preservation,unresolved=len(unresolved),output=str(OUT)),indent=2))
