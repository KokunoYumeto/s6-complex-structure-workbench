from pathlib import Path
from collections import Counter
import contextlib, csv, datetime as dt, difflib, hashlib, io, json, re, runpy

R = Path(__file__).resolve().parents[1]
csv.field_size_limit(100_000_000)
def sha(b): return hashlib.sha256(b).hexdigest()
def bind(p):
    b = (R/p).read_bytes()
    return dict(path=p, sha256=sha(b), bytes=len(b))
def read(p): return json.loads((R/p).read_text())
def check(b):
    actual = bind(b['path'])
    assert actual['sha256'] == b['sha256'] and actual['bytes'] == b['bytes'], b['path']
def tsv(rows, fields, header=True, line='\n'):
    s = io.StringIO(newline=''); w = csv.DictWriter(s, fieldnames=fields, delimiter='\t', lineterminator=line)
    if header: w.writeheader()
    w.writerows(rows); return s.getvalue().encode()

prefix = 'agents/continuation2_C/S6_SERIES_PUBLISH_II_C2_mathematical_permutation_v2/S6_SERIES_PUBLISH_II_C2_permutation_'
index = prefix+'index.json'
assert bind(index)['sha256'] == '2dc7f7e229c41131acd55e3fc7a61926daf8c2e70953f239206a907d1934eda3'
idx = read(index)
for b in idx['files']: check(b)
g = read(prefix+'guards.json')
sp = R/'S6_SERIES_PUBLISH_II.tex'; oldb = sp.read_bytes(); old = oldb.decode()
assert sha(oldb) == g['source_sha256'] == 'c3a64cf42d87e27f5af964abc0680493ae70be933d4810a81c0e25db71d27c12'
validator = runpy.run_path(str(R/(prefix+'validate.py')))
output = io.StringIO()
with contextlib.redirect_stdout(output):
    proposed = validator['validate'](sp)
assert sha(proposed.encode()) == '72c34f091b2ea86c6786a9300a5404c1fd810a262ae934804d77bf06ef057795'

tag = 'P203'; owner = 'scope:II:positive-ruled-configuration'
tp = R/'S6_SERIES_PUBLISH_tags.tsv'; tb = tp.read_bytes()
tr = csv.DictReader(io.StringIO(tb.decode(), newline=''), delimiter='\t'); tags = list(tr); tagfields = tr.fieldnames
assert tag not in {x['tag'] for x in tags}
assert owner not in {x['label'] for x in tags}
assert '\\hypertarget{tag-'+tag+'}' not in old
remark = (R/g['remark']['path']).read_text()
newremark = remark
draft_edits = [
    (r'\hypertarget{tag-PLACEHOLDER-II-POSITIVE-RULED}{}', r'\hypertarget{tag-P203}{}'),
    (r'\label{scope:II:positive-ruled-configuration}', r'\label{scope:II:positive-ruled-configuration}'+'\n'+r'\StatementRecord{scope:II:positive-ruled-configuration}{proved}{P203}{}'),
    ('For the remaining positive-Euler ruled case, retain the morphism\n$f:Y\\to B$ of \\cref{sec:II:night-sign} and the hypothesis that\nevery reduced fibre support is irreducible or has normal crossings.\nLet $mS$ be the full irreducible fibre under consideration, with\n$e(S)>0$, and write',
     'Let $f:Y\\to B$ satisfy the hypotheses of \\cref{sec:II:night-sign},\nand assume that every reduced fibre support is irreducible or has\nnormal crossings. Let $mS$ be a full irreducible fibre with\n$e(S)>0$, and write'),
    ('using the actual maps in', 'using the maps in'),
    ('Thus the remaining image conductor has two rational normalized\ncomponents and one graph cycle. Its self-identifications,\nsingularities and generic transverse types are retained in the\nconfiguration used in the subsequent local arguments.\n', '')
]
for before, after in draft_edits:
    assert newremark.count(before) == 1
    newremark = newremark.replace(before, after, 1)
assert proposed.count(remark) == 1
new = proposed.replace(remark, newremark, 1)
assert 'PLACEHOLDER-II-POSITIVE-RULED' not in new
assert Counter(re.findall(r'\\label\{([^}]+)\}', new)) == Counter(re.findall(r'\\label\{([^}]+)\}', old)) + Counter([owner])
assert Counter(re.findall(r'\\hypertarget\{([^}]+)\}', new)) == Counter(re.findall(r'\\hypertarget\{([^}]+)\}', old)) + Counter(['tag-'+tag])
for b in g['owners']:
    assert validator['block'](new, b['owner'])[2] == validator['block'](old, b['owner'])[2]
assert re.findall(r'(?<!\\)\\\[(.*?)(?<!\\)\\\]', remark, re.S) == re.findall(r'(?<!\\)\\\[(.*?)(?<!\\)\\\]', newremark, re.S)

dp = R/'S6_SERIES_PUBLISH_defects_II.tsv'; db = dp.read_bytes()
dr = csv.DictReader(io.StringIO(db.decode(), newline=''), delimiter='\t'); defects = list(dr); dfields = dr.fieldnames
oldpos = {x:i+1 for i,x in enumerate(g['original_region_owner_order'])}
newpos = {x:i+1 for i,x in enumerate([o for o in g['proposed_owner_order'] if o != g['fixed_earlier_owner']])}
# The fixed earlier owner is named explicitly in the guards; the in-section
# order is obtained directly from positions in the proposed source as a check.
in_section = g['original_region_owner_order']
newpos = {x:i+1 for i,x in enumerate(sorted(in_section, key=lambda x:validator['block'](new,x)[0]))}
bylabel = {x['label']:x for x in tags}
rows = []
def defect(kind, own, before, after, reason, old_location, new_location, page=''):
    rows.append(dict(change_id=f'II-C2-ORDER01-{len(rows)+1:03d}', type=kind, statement_id=own,
        old_location=old_location, old_page=page, new_location=new_location, new_page='pending integrated PDF',
        old_text=before, new_text=after, reason=reason,
        review_status='Root reviewed mathematical dependency order, full new prose and exact preservation validator; final rendered reading pending'))
for own in in_section:
    if oldpos[own] == newpos[own]: continue
    text = validator['block'](old, own)[2]
    defect('D14', own, text, text,
        'Move this complete unchanged owning statement/proof block to the verified premise order. Every mathematical byte, label and hypertarget is preserved; inverse reconstruction restores the entire original section.',
        f'sec:II:night-sign owner position {oldpos[own]}', f'sec:II:night-sign owner position {newpos[own]}', bylabel.get(own,{}).get('page',''))
oldregion = (R/g['original_cluster']['path']).read_text()
newregion = (R/g['proposed_cluster']['path']).read_text()
for gap in g['gaps']:
    text = oldregion[gap['original_region_char_start']:gap['original_region_char_end']]
    if not text.strip(): continue
    if oldpos[gap['after_owner']] == newpos[gap['after_owner']] and (gap['before_owner'] not in newpos or oldpos[gap['before_owner']] == newpos[gap['before_owner']]): continue
    defect('D14', gap['after_owner'], text, text,
        'Transport the original gap by the recorded fragment map: trailing mathematical material follows its owner and an existing subsection heading precedes its subject. Concatenating the fragments in original order reproduces this exact gap and hash.',
        f"gap {gap['id']} after {gap['after_owner']}", f"recorded owner/heading fragments for gap {gap['id']}")
for segment in g['proposed_segments']:
    if segment['kind'] == 'new_heading':
        heading = newregion[segment['proposed_char_start']:segment['proposed_char_end']]
        defect('D14', segment['id'], '', heading, 'Introduce a descriptive subsection boundary at the verified mathematical topic change while preserving the standing scope of the original section.', 'no heading at this boundary', 'before '+segment['id'])
defect('D13,D14,D10', owner, '', newremark,
    'Give the existing XQ, X8 and Euler-bound synthesis a numbered remark after its premises. It names the full fibre and all conductor maps, retains the global support hypothesis, and makes no assumption on the other component or its transverse types. Allocate unused permanent tag P203. All existing proof blocks remain unchanged.',
    'implicit common positive ruled setup', 'after night:P4.51')
assert not ({r['change_id'] for r in rows} & {r['change_id'] for r in defects})
dtail = tsv(rows, dfields, False)
assert db.endswith(b'\n')
tagrow = dict(tag=tag, paper='II', number='pending build', page='pending build', label=owner,
    status='proved', kind='remark', current_owner=owner,
    publication_disposition='new numbered synthesis of the explicitly cited conductor and Euler results; permanent identity; final source/page review pending')
ttail = tsv([tagrow], tagfields, False, '\r\n' if b'\r\n' in tb else '\n')
assert tb.endswith(b'\n')

ip = R/'S6_SERIES_PUBLISH_inventory.csv'; ib = ip.read_bytes()
ir = csv.DictReader(io.StringIO(ib.decode(), newline='')); inventory = list(ir); ifields = ir.fieldnames
assert not any(r['label'] == owner for r in inventory)
irow = {k:'' for k in ifields}
irow.update(paper='II', label=owner, source_run='S6_SERIES_PUBLISH', source_id=owner,
    kind='Remark', status='proved', main_or_supporting='supporting', source_paper='II', tag=tag,
    uses='night:P4.51;night:P4R.7;night:P4R.9;night:P4.13;night:P4.26;night:P4.35',
    check_record='{}', notes='Existing positive ruled premise combination made explicit in a numbered remark; no new independent evidence group.',
    check_summary='Root read the full new synthesis and verified its exact maps and cited argument scope; final global and page review pending.',
    confidence_line='Cited-premise synthesis; no independent-check credit added.',
    placement_state='After all cited premises and before the positive-Euler local casework.',
    writing_state='Numbered synthesis inserted during exact mathematical permutation.',
    confidence_state='The original R13 blanket uniqueness claim remains open in its owning row; no closure is inferred here.',
    completion_state='Final publication gate remains open.',
    source_main_or_supporting='supporting', series_main_theorems='II:C',
    format_check='Numbered remark with permanent tag P203.', layout_check='pending integrated PDF',
    remaining_risk='Final source, provenance, global defect and rendered-page checks remain open.',
    assessment_source='records/S6_SERIES_PUBLISH_II_mathematical_order_01/manifest.json',
    literature_disposition='Synthesis of cited results in this paper.', current_source_sha256=sha(new.encode()),
    current_statement_owner=owner, publication_review_status='Root reviewed synthesis and exact permutation; final rendered review pending',
    current_number='pending build', current_page='pending build')
out = io.StringIO(newline=''); iw = csv.DictWriter(out, fieldnames=ifields, lineterminator='\r\n' if b'\r\n' in ib else '\n'); iw.writerow(irow)
itail = out.getvalue().encode(); assert ib.endswith(b'\n')

now = dt.datetime.now(dt.timezone.utc).isoformat()
rd = R/'records/S6_SERIES_PUBLISH_II_mathematical_order_01'
assert not rd.exists(); rd.mkdir()
(rd/'source.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile='II.before', tofile='II.after')))
(rd/'new_remark.tex').write_text(newremark)
(rd/'new_remark_draft_changes.json').write_text(json.dumps([dict(old=b,new=a) for b,a in draft_edits], indent=2)+'\n')
(rd/'defect_rows.tsv').write_bytes(tsv(rows,dfields))
(rd/'tag_row.tsv').write_bytes(tsv([tagrow],tagfields))
(rd/'inventory_row.json').write_text(json.dumps(irow,indent=2)+'\n')
(rd/'validation.out').write_text(output.getvalue())
manifest = dict(created_utc=now, source_before_sha256=sha(oldb), source_after_sha256=sha(new.encode()),
    packet_index=bind(index), packet_guard=bind(prefix+'guards.json'),
    tags_before_sha256=sha(tb), tags_after_sha256=sha(tb+ttail), new_tag=tag, new_owner=owner,
    inventory_before_sha256=sha(ib), inventory_after_sha256=sha(ib+itail), inventory_rows_added=1,
    defects_before_sha256=sha(db), defects_after_sha256=sha(db+dtail), defect_rows_added=len(rows),
    all_78_original_owner_blocks_byte_identical=True, all_77_original_gaps_exactly_reconstructible=True,
    original_labels_in_owner_blocks=182, original_hypertargets_in_owner_blocks=94,
    original_items_in_owner_blocks=469, original_displays_in_owner_blocks=491,
    logical_premise_pairs_ordered=271, contextual_premise_pairs_ordered=57,
    original_forward_logical_pairs_resolved=58, current_ledger=bind('CHECK_EVENTS.tsv'),
    current_completion_manifest=bind('records/S6_SERIES_PUBLISH_required_check_completion_manifest.json'),
    events_added=0, required_rows_closed=0, global_defect_rows_closed=0, final_page_reading_credit=0,
    actual_root_reading='Complete frozen order report and its rationale read in the prior review. Root then read the complete final implementation report, all eleven new headings, full numbered synthesis, complete validator and R18 rebinding. The validator proves exact inverse reconstruction of the original cluster from every owner and gap fragment. Unchanged original proof text carries its original full-reading records. Initial oversized repeat output of the old organization report was truncated and adds no new reading credit. No complete-paper or final-page reading is claimed.',
    scope='Exact mathematical permutation and numbered premise synthesis. Fixed early A.5.15/P4.18 and all outside-cluster bytes remain unchanged. R13 remains unresolved. Legacy interstitial editorial work and remaining whole-paper organization are open.')
(rd/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
# Every check above precedes the reversible canonical commit.
sp.write_text(new)
with dp.open('ab') as f: f.write(dtail)
with tp.open('ab') as f: f.write(ttail)
with ip.open('ab') as f: f.write(itail)
assert sp.read_bytes() == new.encode()
assert dp.read_bytes() == db+dtail and tp.read_bytes() == tb+ttail and ip.read_bytes() == ib+itail
assert bind('CHECK_EVENTS.tsv') == manifest['current_ledger']
assert bind('records/S6_SERIES_PUBLISH_required_check_completion_manifest.json') == manifest['current_completion_manifest']
text = f'''\n\n## Paper II conductor section ordered by its mathematical premises — {now}\n\nThe complete verified permutation is applied. All78 original owner blocks,182 labels,94 targets,469 items and491 displays are byte-identical; the77 original gaps reconstruct exactly from their transported fragments. The271 explicit logical premise pairs and57 contextual pairs precede their consumers, resolving all58 formerly forward logical pairs. The fixed earlier shared A.5.15/P4.18 block and every byte outside the section are unchanged. Eleven descriptive subsection headings and the numbered positive ruled synthesis are added; its unused permanent tag is P203. Root removed draft-only process phrasing and a closing repetition from that new synthesis, preserving every displayed formula. {len(rows)} exact structural defect rows, the full diff, inverse validation, new tag and inventory row are in records/S6_SERIES_PUBLISH_II_mathematical_order_01. Source SHA256 {manifest['source_after_sha256']}. No mathematical proof step or hypothesis changed, and no check event, required row, global defect class or rendered-page row closed. II remains192/197 with5 open checks; R13 remains open. The remaining interstitial editorial work, wider section organization, provenance and final PDF reading remain due.\n'''
for name in ('PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md'):
    with (R/name).open('a') as f: f.write(text)
print(json.dumps(manifest,indent=2))
