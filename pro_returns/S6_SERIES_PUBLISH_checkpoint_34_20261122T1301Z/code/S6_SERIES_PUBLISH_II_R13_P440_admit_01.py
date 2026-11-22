#!/usr/bin/env python3
"""Admit the reviewed R13/P440 correction and its complete supporting proofs.

This is an exact append-only admission, not an independent mathematical check.
Every source mutation has a reversible byte map. The immutable research and
review packets record exposure, complete proof comparisons and computation.
"""
from pathlib import Path
import collections, csv, datetime as dt, difflib, hashlib, io, json, re

R = Path(__file__).resolve().parents[1]
OUT = R / 'records/S6_SERIES_PUBLISH_II_R13_P440_correction_01'
csv.field_size_limit(100_000_000)
sha = lambda b: hashlib.sha256(b).hexdigest()
NOW = dt.datetime.now(dt.timezone.utc).isoformat()
SOURCE_SHA = 'e7e832c3c23496d4a02c0a5c7257ed68cf263f84ed94373974a6066c4c40b629'
A = 'agents/continuation2_A/'
C = 'agents/continuation2_C/'
Y = A + 'S6_SERIES_PUBLISH_II_A2_Y6_final_v1_20261122/'
X = A + 'S6_SERIES_PUBLISH_II_A2_XE_P206_final_v1_20261122/'
P = C + 'S6_SERIES_PUBLISH_II_C2_R13_publication_P205/'
V = C + 'S6_SERIES_PUBLISH_II_C2_R13_P440_P206_review_v1/'

def js(path):
    return json.loads((R / path).read_text())

def binding(path):
    p = R / path
    b = p.read_bytes()
    return dict(path=str(p.relative_to(R)), bytes=len(b), sha256=sha(b))

def encode(obj):
    return (json.dumps(obj, indent=2, ensure_ascii=False) + '\n').encode()

def read_table(path, delim='\t'):
    b = (R / path).read_bytes()
    rd = csv.DictReader(io.StringIO(b.decode()), delimiter=delim)
    return b, list(rd), rd.fieldnames

def table_bytes(rows, fields, delim='\t', header=True):
    out = io.StringIO(newline='')
    w = csv.DictWriter(out, fieldnames=fields, delimiter=delim, lineterminator='\n')
    if header:
        w.writeheader()
    w.writerows(rows)
    return out.getvalue().encode()

def block(text, tag):
    at = text.index('\\hypertarget{tag-' + tag + '}')
    ms = list(re.finditer(r'\\begin\{(proposition|lemma|example|definition|theorem|remark)\}', text[:at]))
    m = ms[-1]
    if m[1] == 'definition':
        end = text.index('\\end{definition}', at) + len('\\end{definition}')
    else:
        end = text.index('\\end{proof}', at) + len('\\end{proof}')
    return text[m.start():end]

def guarded(text, guards):
    start = text
    inverses = []
    for g in guards:
        assert g['old'] and text.count(g['old']) == g.get('expected_count', 1) == 1, g['id']
        pos = text.index(g['old'])
        text = text[:pos] + g['new'] + text[pos+len(g['old']):]
        inverses.append(dict(id=g['id'], offset=pos, old=g['old'], new=g['new']))
    back = text
    for g in reversed(inverses):
        pos = g['offset']
        assert back[pos:pos+len(g['new'])] == g['new'], g['id']
        back = back[:pos] + g['old'] + back[pos+len(g['new']):]
    assert back == start
    return text, inverses

def compact_diff(old, new, name):
    return ''.join(difflib.unified_diff(old.decode().splitlines(True), new.decode().splitlines(True),
                                      fromfile=name+' before', tofile=name+' after')).encode()

assert not OUT.exists(), 'Never overwrite a prior admission.'
source_before = (R / 'S6_SERIES_PUBLISH_II.tex').read_bytes()
assert sha(source_before) == SOURCE_SHA
source = source_before.decode()

# Verify every immutable file listed in each complete review/proposal packet.
index_names = [
    Y+'S6_SERIES_PUBLISH_II_A2_Y6_index.json',
    X+'S6_SERIES_PUBLISH_II_A2_XE_P206_index.json',
    P+'S6_SERIES_PUBLISH_II_C2_P205_publication_index_final_v1.json',
    V+'S6_SERIES_PUBLISH_II_C2_Y6_full_comparison_index_v1.json',
    V+'S6_SERIES_PUBLISH_II_C2_R13_P440_P206_review_index_final_v1.json',
]
expected_index_shas = [
    'e00477eabcd451720b4fba5c89bc7c3f5718f0b208ad1763e8c654bc02169100',
    '6521a5614280c012f77caf69a110cae40283a84f01e009e768c218b8bb9aff16',
    'cf297742df692b417f37c2e4a4246da74ae48f157c8d91c5a665da3dd4412424',
    'a7f589b5d529100654ad06deb71e221e6119e043e0de02bcdaf09dde87f0c39a',
    '8950dbbb192d8611d56682a8364d753b7423ecf144a142f375764738e8034307',
]
verified = {}
packet_counts = []
for name, expected in zip(index_names, expected_index_shas):
    assert sha((R/name).read_bytes()) == expected, name
    entries = js(name)['files']
    for entry in entries:
        actual = binding(entry['path'])
        assert actual['bytes'] == entry['bytes'] and actual['sha256'] == entry['sha256'], entry['path']
        verified[entry['path']] = actual
    packet_counts.append(dict(index=binding(name), verified_bindings=len(entries)))

old_y = (R/'agents/ii_infra/released_proofs/02Y6/e2c1bb7f36a82389/S6_SERIES_PUBLISH_full_owning_block.tex').read_text()
old_x = (R/(A+'S6_SERIES_PUBLISH_II_A2_02XE_original_current_v1.tex')).read_text()
new_y = (R/(Y+'S6_SERIES_PUBLISH_II_A2_02Y6_proposed.tex')).read_text()
new_x = (R/(X+'S6_SERIES_PUBLISH_II_A2_XE_P206_combined.tex')).read_text()
new_p = (R/(P+'S6_SERIES_PUBLISH_II_C2_P205_proposal_final_v1.tex')).read_text()
assert block(source,'02Y6') == old_y and block(source,'02XE') == old_x
gy = js(Y+'S6_SERIES_PUBLISH_II_A2_Y6_guards.json')
gx = js(X+'S6_SERIES_PUBLISH_II_A2_XE_P206_guards.json')
ry, iy = guarded(old_y, gy)
rx, ix = guarded(old_x, gx)
assert ry == new_y and rx == new_x

consumer_data = js(X+'S6_SERIES_PUBLISH_II_A2_XE_consumer_guards.json')
assert consumer_data['source_sha256'] == SOURCE_SHA
source_guards = [dict(id='replace-R13-and-insert-P205', old=old_y, new=new_y+'\n\n'+new_p),
                 dict(id='replace-P440-and-extract-P206', old=old_x, new=new_x)]
consumer_replay = []
for c in consumer_data['consumers']:
    before = block(source, c['tag'])
    assert sha(before.encode()) == c['before_sha256'] and len(before.encode()) == c['before_bytes']
    after, inv = guarded(before, c['guards'])
    assert sha(after.encode()) == c['after_sha256'] and len(after.encode()) == c['after_bytes']
    source_guards.append(dict(id='consumer-'+c['tag'], old=before, new=after))
    consumer_replay.append(dict(owner=c['owner'], tag=c['tag'], before_sha256=c['before_sha256'],
                               after_sha256=c['after_sha256'], guards=len(c['guards']), inverse=inv))

program_p = js(P+'S6_SERIES_PUBLISH_II_C2_P205_programs_row_proposal_final_v1.json')
program_path = program_p['suggested_canonical_path']
assert not (R/program_path).exists()
program_content = (R/program_p['source']['path']).read_bytes()
assert sha(program_content) == program_p['source']['sha256']
program_rows = (R/(Y+'S6_SERIES_PUBLISH_II_A2_Y6_Programs_row.tex')).read_text() + '\n'
program_rows += (R/(X+'S6_SERIES_PUBLISH_II_A2_XE_P206_Programs_row.tex')).read_text() + '\n'
program_rows += ('Integral monodromies, local markings, invariant exterior maps, affine boundary sums and twistor row maps '
                 '(\\cref{ii:three-doubled-nodal-fibres}) & '
                 '\\href{https://raw.githubusercontent.com/KokunoYumeto/s6-complex-structure-workbench/'
                 '\\SsixRepositoryCommit/'+program_path+'}{\\nolinkurl{'+Path(program_path).name+'}} \\\\[3pt]\n')
at = source.index('\\section*{Programs}')
end = source.index('\\end{longtable}}', at)
program_anchor = source[end-300:end+len('\\end{longtable}}')]
source_guards.append(dict(id='Programs-three-scoped-computations', old=program_anchor,
                         new=program_anchor[:-len('\\end{longtable}}')]+program_rows+'\\end{longtable}}'))
source_after, source_inverse = guarded(source, source_guards)

# The complete earlier target identities survive. New statement/semantic labels
# are additions only; the admission does not renumber any existing equation.
identity_counts = {}
for name, pattern in [('labels', r'\\label\{[^}]+\}'),
                      ('hypertargets', r'\\hypertarget\{[^}]+\}'),
                      ('literal_equation_tags', r'\\tag\{[^}]+\}'),
                      ('statement_record_triples', r'\\StatementRecord\{[^}]+\}\{[^}]+\}\{[^}]+\}')]:
    a = collections.Counter(re.findall(pattern, source))
    b = collections.Counter(re.findall(pattern, source_after))
    assert not (a-b), (name, a-b)
    identity_counts[name] = dict(before=sum(a.values()), after=sum(b.values()), all_old_occurrences_preserved=True)
for label in ['night:P4R.13:elliptic-components','night:P4.40:positive-euler',
              'ii:three-doubled-nodal-fibres','ii:excess-one-curve-germs']:
    assert source_after.count('\\label{'+label+'}') == 1
assert source_after.count('\\hypertarget{tag-P205}') == 1
assert source_after.count('\\hypertarget{tag-P206}') == 1

# Retain every event, including old claims which the two new refutations amend.
event_before, events, event_fields = read_table('CHECK_EVENTS.tsv')
assert len(events) == 8405
recommend = js(A+'S6_SERIES_PUBLISH_II_A2_Y6_XE_P206_event_proposals_v1.json')
new_events = []
for index, proposed in enumerate(recommend['events'], 1):
    row = {k:str(proposed.get(k,'')) for k in event_fields}
    row.update(phase='publication correction and comparative proof review', source_row=str(index),
               source_event_type=proposed['type'])
    new_events.append(row)
GROUP = 'S6_SERIES_PUBLISH_II_A2_Y6_XE_shared_construction_20261122'
def event(owner, suffix, kind, scope, evidence, group=GROUP):
    row = {k:'' for k in event_fields}
    row.update(statement_id=owner, date='2026-11-22', date_utc=NOW,
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; inherited reasoning effort not separately exposed; continuation 2 C and root comparative review',
        type=kind, outcome=scope, event_id='publish:correction01:'+suffix,
        phase='publication correction and comparative proof review', source_file=evidence,
        source_event_type=kind, evidence_group=group, where=owner)
    new_events.append(row)
event('night:P4R.13','R13-comparison','used and rechecked in this run',
      'C and root fully read the original 13-item proof and exact corrected 15-item proof and compared every original step. The 14 original displays and their valid doubled-horizontal route are preserved; the rational-resolution exclusion and complete reduced-horizontal classification are supplied. C fully read the six consumer proofs and exact inference roles; root read the full scope reports and inference maps. The new statement has one or two elliptic image curves and Euler zero. The Greb analytic surface criterion was freshly opened at section 2.1 and Remark 2.1, printed page 415. This is an exposed comparative review and shares the construction evidence; no new independent whole-target derivation is claimed.',
      V+'S6_SERIES_PUBLISH_II_C2_Y6_full_comparison_review_v1.md')
event('ii:three-doubled-nodal-fibres','P205-comparison','used and rechecked in this run',
      'Publication of the completed compact construction: root and C read all 13 printed proof items and their exact analytic, quotient, lattice, specialization and global gluing maps; root previously read A\'s complete 39,959-byte audit before release of A\'s R13 target. C developed the global period construction after exposure to the target. The proof constructs a smooth compact threefold over P1 with b1=b2=0, e=0 and three full double nodal fibres, with two distinct elliptic image curves on each support. The construction and both original-statement refutations are one evidence group. No second example, pristine independent rediscovery or code-only proof claim is made.',
      P+'S6_SERIES_PUBLISH_II_C2_P205_publication_review_final_v1.md')
event('ii:three-doubled-nodal-fibres','P205-computation','computation or formal certificate',
      'C ran and fully read the exact printed-data program and output, and root fully read both. It checks the displayed integral monodromies, local markings, nilpotents and orientation, invariant covectors, exterior-square minor, affine sums and exact twistor row identities. These finite computations support the printed algebra only; analytic existence, properness, specialization and the compact topological conclusion are established by the complete proof and its exposed comparative review. This computational event shares the compact-construction evidence group.',
      P+'S6_SERIES_PUBLISH_II_C2_P205_printed_data_check.out')
for c in consumer_data['consumers']:
    event(c['owner'],c['tag']+'-local-reference','used and rechecked in this run',
          'C fully reread the complete original and amended proof. The two guarded changes replace the dependency-header reference and the local ring-classification citation by P206. All other bytes, hypotheses, displays, maps and conclusions are identical. The exact branch-count and delta hypotheses match the extracted local lemma; the positive-Euler global exclusion is not used for this local inference. Root read the complete comparative review and both exact guards. No independent derivation or additional required-row closure is claimed.',
          V+'S6_SERIES_PUBLISH_II_C2_XE_P206_full_review_v1.md',
          'S6_SERIES_PUBLISH_II_A2_P206_local_algebra_20261122')
assert len(new_events) == 13
assert len({e['event_id'] for e in events+new_events}) == len(events)+len(new_events)
assert sum(e['type']=="refuted, with the refined statement's id" for e in new_events)==2
assert not any(e['type'] in ['targeted proof check','independent re-proof'] for e in new_events)
event_append = table_bytes(new_events,event_fields,header=False)
event_after = event_before + event_append
assert list(csv.DictReader(io.StringIO(event_after.decode()),delimiter='\t')) == events+new_events

defect_before, defects, defect_fields = read_table('S6_SERIES_PUBLISH_defects_II.tsv')
new_defects=[]
def defect(owner, tag, g):
    for kind in g['defect_ids']:
        row={k:'' for k in defect_fields}
        row.update(change_id=f'II-R13-P440-01-{len(new_defects)+1:03}',type=kind,statement_id=owner,
            old_location=tag+' / '+g['id'],old_page='inherited locator; exact old block is bound',
            new_location=tag+' / corrected owner or extracted local lemma',new_page='pending integrated build',
            old_text=g['old'],new_text=g['new'],reason=g['reason'],
            review_status='Applied after complete original/proposed proof comparison. Exact sequential guard and inverse pass. No final-page or global-defect-class credit.')
        new_defects.append(row)
for owner,tag,guards in [('night:P4R.13','02Y6',gy),('night:P4.40','02XE',gx)]:
    for g in guards: defect(owner,tag,g)
for c in consumer_data['consumers']:
    for g in c['guards']: defect(c['owner'],c['tag'],g)
defect('ii:three-doubled-nodal-fibres','P205',dict(id='full-compact-example',defect_ids=['D25'],old='',new=new_p,
       reason='Print the complete compact construction establishing both corrected statement scopes, including all local/global analytic and topological maps; no research-packet substitution for the mathematical proof.'))
defect('tab:II:programs','Programs',dict(id='three-program-citations',defect_ids=['D09'],old='',new=program_rows,
       reason='Place the three scoped program citations in the Programs table. Their new repository paths remain an explicit final provenance/pinned-link gate; no current remote existence is asserted by this admission.'))
defect_append=table_bytes(new_defects,defect_fields,header=False)

tag_before,tags,tag_fields=read_table('S6_SERIES_PUBLISH_tags.tsv')
for row in tags:
    if row['tag'] in ['02Y6','02XE']:
        row['publication_disposition'] += '; original assertion refuted on 2026-11-22; corrected at refined alias '+('night:P4R.13:elliptic-components' if row['tag']=='02Y6' else 'night:P4.40:positive-euler')+'; original permanent identity retained'
new_owners=[('P204','def:II:standing-torus-fibration','Definition'),
            ('P205','ii:three-doubled-nodal-fibres','Example'),
            ('P206','ii:excess-one-curve-germs','Lemma')]
for tag,owner,kind in new_owners[1:]:
    assert not any(x['tag']==tag or x['label']==owner for x in tags)
    row={k:'' for k in tag_fields}
    row.update(tag=tag,paper='II',number='pending build',page='pending build',label=owner,status='proved',
               kind='statement',current_owner=owner,publication_disposition='new permanent mathematical owner; full proof printed; exact exposed review and scoped computation recorded')
    tags.append(row)
tag_after=table_bytes(tags,tag_fields)

inventory_before,inventory,inventory_fields=read_table('S6_SERIES_PUBLISH_inventory.csv',',')
other_inventory=[x.copy() for x in inventory if x['paper']!='II']
for row in inventory:
    if row['paper']!='II': continue
    if row['label'] in ['night:P4R.13','night:P4.40']:
        row['status']='proved'
        row['confidence_state']='Original assertion refuted; complete refined proof and all affected uses comparatively checked. No pristine whole-target independence claim.'
        row['completion_state']='Required mathematical correction/check resolved; full paper editorial, provenance, build and page-reading gates remain open.'
        row['assessment_source']='records/S6_SERIES_PUBLISH_II_R13_P440_correction_01/manifest.json'
        row['remaining_risk']='Final source-wide, provenance, integrated build and actual rendered-page review remain open.'
        row['current_statement_owner']=row['label']
    if row['label']=='scope:II:positive-ruled-configuration':
        row['confidence_state']='Cited-premise synthesis retained. R13 original uniqueness assertion is now refuted and corrected with the zero-Euler inference preserved; see correction01.'
    if row['label'] in [c['owner'] for c in consumer_data['consumers']]:
        row['uses']=row['uses'].replace('night:P4.40','ii:excess-one-curve-germs')
        row['assessment_source']='records/S6_SERIES_PUBLISH_II_R13_P440_correction_01/manifest.json'
for tag,owner,kind in new_owners:
    assert not any(x['label']==owner for x in inventory),owner
    row={k:'' for k in inventory_fields}
    row.update(paper='II',label=owner,source_run='S6_SERIES_PUBLISH',source_id=owner,kind=kind,status='proved',
        main_or_supporting='supporting',check_record='{}',source_paper='II',tag=tag,
        placement_state='printed in II',current_statement_owner=owner,current_number='pending build',current_page='pending build',
        writing_state='Complete numbered mathematical owner in current source.',
        confidence_state=('Verbatim standing-domain definition; metadata reconciliation adds no mathematical check.' if tag=='P204' else 'Complete exposed proof review and finite computations recorded at their actual scope.'),
        completion_state='Full paper publication gates remain open.',layout_check='pending integrated rendered-page review',
        remaining_risk='Final source-wide, provenance, integrated build and actual rendered-page review remain open.',
        assessment_source='records/S6_SERIES_PUBLISH_II_R13_P440_correction_01/manifest.json',
        current_source_sha256=sha(source_after.encode()))
    inventory.append(row)
assert [x for x in inventory if x['paper']!='II']==other_inventory
inventory_after=table_bytes(inventory,inventory_fields,',')

check_before=(R/'S6_SERIES_PUBLISH_checks_II.md').read_bytes()
checks=check_before.decode()
for tag in ['02Y6','02XE']:
    start=checks.index('<a id="tag-'+tag+'"></a>')
    end=checks.find('<a id="tag-',start+1)
    if end<0:end=len(checks)
    b=checks[start:end]
    notice=('### Current correction scope\n\nThe original unqualified assertion is refuted. The corrected owner retains this permanent tag and its original labels; refined alias `'+('night:P4R.13:elliptic-components' if tag=='02Y6' else 'night:P4.40:positive-euler')+'`. Full proof comparison, original-to-corrected step maps, compact construction and consumer checks are bound by `records/S6_SERIES_PUBLISH_II_R13_P440_correction_01/manifest.json`. Earlier events remain historical records.\n\n')
    at=b.index('### Check events');b=b[:at]+notice+b[at:]
    checks=checks[:start]+b+checks[end:]
for tag in ['P201','P202','P203','P204','P205','P206']:
    assert '<a id="tag-'+tag+'"></a>' not in checks
    row=next(x for x in tags if x['tag']==tag)
    uses=next((x.get('uses','') for x in inventory if x['tag']==tag),'')
    checks+=f'\n<a id="tag-{tag}"></a>\n\n## {tag} — II, number pending build\n\nLabel: `{row["label"]}`. Page: pending build.\n\nRecorded mathematical status: proved.\n\n### Recorded routes and present scope\n\nEvent associations are regenerated from the authoritative ledger; adding this entry adds no check.\n\n<a id="uses-{tag}"></a>\n### Uses and used by\n\nUses: {uses or "See the explicit current statement/proof references; final graph regeneration pending."}\n\nUsed by: final graph regeneration pending.\n\n### Entry provenance\n\nP201–P204 retain the already admitted numbered definitions and cited synthesis. P205 is the complete compact example; P206 is the extracted local argument. Exact admission and exposure scope: `records/S6_SERIES_PUBLISH_II_R13_P440_correction_01/manifest.json`.\n\n### Check events\n\n'
check_after=checks.encode()

completion_path='records/S6_SERIES_PUBLISH_required_check_completion_manifest.json'
completion_before=(R/completion_path).read_bytes();completion=json.loads(completion_before)
assert sum(x['paper']=='II' for x in completion['rows'].values())==196
for owner in ['night:P4R.13','night:P4.40']:assert owner not in completion['rows']
additional_path='records/S6_SERIES_PUBLISH_additional_required_checks_II.json'
additional_before=(R/additional_path).read_bytes();additional=json.loads(additional_before)
assert len(additional['rows'])==1 and additional['rows'][0]['id']=='check:night:P4.40'
# The immutable discovered-row definition remains open; the authoritative
# completion manifest resolves it during the next scheduled progress review.
assert additional['rows'][0]['status']=='open'

registry_path='records/S6_SERIES_PUBLISH_additional_event_bundles.json'
registry_before=(R/registry_path).read_bytes();registry=json.loads(registry_before)
event_bundle=table_bytes(new_events,event_fields)
event_bundle_path='records/S6_SERIES_PUBLISH_II_R13_P440_correction_01/event_rows.tsv'
registry['bundles'].append(dict(path=event_bundle_path,bytes=len(event_bundle),sha256=sha(event_bundle),
                               admission_manifest='records/S6_SERIES_PUBLISH_II_R13_P440_correction_01/manifest.json'))
registry_after=encode(registry)

root_review=dict(created_utc=NOW,reviewer='/root',
    current_full_reads=[Y+'S6_SERIES_PUBLISH_II_A2_02Y6_proposed.tex',Y+'S6_SERIES_PUBLISH_II_A2_Y6_comparison.md',
        X+'S6_SERIES_PUBLISH_II_A2_XE_P206_combined.tex',X+'S6_SERIES_PUBLISH_II_A2_XE_P206_comparison.md',
        X+'S6_SERIES_PUBLISH_II_A2_XE_consumer_guards.json',V+'S6_SERIES_PUBLISH_II_C2_Y6_full_comparison_review_v1.md',
        V+'S6_SERIES_PUBLISH_II_C2_XE_P206_full_review_v1.md',
        'code/S6_SERIES_PUBLISH_II_A2_Y6_primary_jet_comparison.py',A+'S6_SERIES_PUBLISH_II_A2_Y6_primary_jet_comparison_output.json',
        'code/S6_SERIES_PUBLISH_II_A2_P206_curve_algebra.py',A+'S6_SERIES_PUBLISH_II_A2_P206_curve_algebra_output.json'],
    earlier_root_full_reading_receipt=binding('records/S6_SERIES_PUBLISH_II_R13_root_research_09.json'),
    full_original_R13_and_P440_root_read=True,
    P205_root_full_reading='All 13 items and complete program/output read, bound in research09; no additional fresh independent proof claim.',
    consumer_reading='C read every complete old and amended proof. Root read both complete comparative reports, exact inference maps and all eight consumer guards; no root full-consumer reading claim.',
    primary_reading='Root freshly opened the official Numdam Greb2011 PDF at section2.1/Remark2.1, printed p415, source turn593998713view0. Extracted text was read; the screenshot placeholder confers no image-view credit. Earlier Grauert page-image reading is bound in rootresearch07 and the 1963 correction reading in batch77.',
    truncated_outputs='The initial combined P440/P206 output was truncated and received no credit; its complete content was subsequently read in two bounded chunks. Oversized metadata/census outputs confer no full-read credit; exact needed schemas and entries were separately retrieved. Historical program sources were fully read by A/C; root read their receipts, not those historical sources.',
    mathematical_verdict='Both exact refined blocks are supported by complete proofs; the single compact example establishes both original refutations; every affected local consumer uses the same extracted ring theorem.',
    new_independent_check_credit=0,final_page_credit=0)

OUT.mkdir()
(OUT/'root_review.json').write_bytes(encode(root_review))
(OUT/'source_guards_and_inverse.json').write_bytes(encode(source_inverse))
(OUT/'owner_guard_replay.json').write_bytes(encode(dict(R13=iy,P440_P206=ix,consumers=consumer_replay)))
(OUT/'event_rows.tsv').write_bytes(event_bundle)
(OUT/'defect_rows.tsv').write_bytes(table_bytes(new_defects,defect_fields))
(OUT/'source.diff').write_bytes(compact_diff(source_before,source_after.encode(),'Paper II correction01'))
for name,old,new in [('tags',tag_before,tag_after),('inventory',inventory_before,inventory_after),('checks',check_before,check_after),('event_bundle_registry',registry_before,registry_after)]:
    (OUT/(name+'.diff')).write_bytes(compact_diff(old,new,name))

changes=[('S6_SERIES_PUBLISH_II.tex',source_before,source_after.encode()),
         ('CHECK_EVENTS.tsv',event_before,event_after),
         ('S6_SERIES_PUBLISH_defects_II.tsv',defect_before,defect_before+defect_append),
         ('S6_SERIES_PUBLISH_tags.tsv',tag_before,tag_after),
         ('S6_SERIES_PUBLISH_inventory.csv',inventory_before,inventory_after),
         ('S6_SERIES_PUBLISH_checks_II.md',check_before,check_after),
         (registry_path,registry_before,registry_after)]
manifest=dict(created_utc=NOW,scope='Two actual mathematical corrections, complete compact example, extracted local lemma, and exact consumer-reference transport.',
    source_before_sha256=sha(source_before),source_after_sha256=sha(source_after.encode()),
    exact_owner_guard_count=len(gy)+len(gx),consumer_guard_count=8,all_source_mutations_exactly_invertible=True,
    identity_counts=identity_counts,original_display_counts_preserved=dict(R13=14,P440=4),
    packet_verification=packet_counts,unique_sealed_bindings=len(verified),
    root_review=binding(str((OUT/'root_review.json').relative_to(R))),
    ledger_rows_before=len(events),ledger_rows_after=len(events)+len(new_events),events_added=len(new_events),
    event_types=dict(collections.Counter(x['type'] for x in new_events)),
    shared_construction_evidence_group=GROUP,new_independent_proof_events=0,
    defect_rows_before=len(defects),defect_rows_added=len(new_defects),
    required_rows_closed=['night:P4R.13','night:P4.40'],required_II_total=198,required_II_done=198,
    inherited_required_II_total=197,additional_discovered_error_rows=1,
    completion_kind='refuted and corrected with complete comparative proof checks',
    additional_required_registry_disposition='The discovered-row definition remains immutable; its done state is supplied by the authoritative completion manifest and scheduled progress review.',
    new_permanent_tags=['P205','P206'],new_inventory_rows=['P204','P205','P206'],
    new_check_entries=['P201','P202','P203','P204','P205','P206'],
    main_conclusion_scope='The audited consumers retain their proved zero-Euler or doubled-horizontal maps. The two original blanket assertions are explicitly refuted; no change to a main theorem is inferred or hidden.',
    proof_order='P206 precedes P440; the independent complete compact example P205 follows refined R13 and has no internal statement dependency.',
    publication_limits=['All25 global defect classes remain open.','Final integrated build and all actual final page readings remain open.','The three newly cited program paths require final pinned-commit provenance verification; this admission makes no remote-existence claim.','D19 must be rebased on this source.','III and IV remain unopened; I and V remain held closed.'],
    final_pdf_page_credit=0,global_defect_classes_closed=0,
    canonical_changes=[dict(path=n,before_bytes=len(b),before_sha256=sha(b),after_bytes=len(a),after_sha256=sha(a)) for n,b,a in changes],
    canonical_program_copy=dict(source=program_p['source'],destination=program_path,bytes=len(program_content),sha256=sha(program_content)),
    immutable_evidence=[binding(str(p.relative_to(R))) for p in sorted(OUT.iterdir())],
    code=binding('code/S6_SERIES_PUBLISH_II_R13_P440_admit_01.py'))
manifest_path=OUT/'manifest.json';manifest_path.write_bytes(encode(manifest))
manifest_binding=binding(str(manifest_path.relative_to(R)))
scopes={
 'night:P4R.13':'Original one-image assertion refuted by the complete compact construction. Corrected one-or-two elliptic conductor theorem proved on the original standing domain, including the rational exclusion, reduced-horizontal cases and all retained doubled-horizontal steps; all downstream uses compared.',
 'night:P4.40':'Original blanket ordinary-double ruled-support exclusion refuted by the same compact construction. Corrected positive-Euler exclusion fully proved; original local ring argument extracted as P206 and all four local consumers fully compared and retargeted.'}
for owner,scope in scopes.items():
    completion['rows'][owner]=dict(paper='II',status='done',recorded_utc=NOW,
        evidence_path=manifest_binding['path'],evidence_sha256=manifest_binding['sha256'],scope=scope,
        completion_kind='refuted and corrected with complete comparative proof checks')
completion['updated_utc']=NOW
completion_after=encode(completion)
(OUT/'completion_manifest.diff').write_bytes(compact_diff(completion_before,completion_after,'required check completion'))

# All input hashes are checked immediately before the first canonical mutation.
for name,before,after in changes:assert (R/name).read_bytes()==before,name
assert (R/completion_path).read_bytes()==completion_before
assert (R/additional_path).read_bytes()==additional_before
for name,before,after in changes:(R/name).write_bytes(after)
(R/completion_path).write_bytes(completion_after)
(R/program_path).write_bytes(program_content)
note=f'''\n\n## Paper II: two proved scope corrections and complete compact example — {NOW}\n\nThe original statements at tags02Y6 and02XE are refuted by the same fully proved compact torus fibration over P1: b1=b2=0, e=0, three full double nodal fibres, and two distinct smooth elliptic image curves on each support. The complete construction is now printed as Example P205. R13 now proves one or two elliptic image curves, retaining Euler zero and all thirteen valid original doubled-horizontal proof items; the rational and reduced-horizontal cases are supplied in full. P4.40 now states and proves the positive-Euler exclusion. Its original local excess-one curve-ring argument is printed once as Lemma P206; all four local consumers cite that lemma through exact guarded changes. Every original display, tag and label is retained.\n\nA froze its complete audit before its target release, with C's earlier target exposure and contribution of the global period construction expressly disclosed. C and root completed the recorded comparative reviews. The ledger appends two refutations, scoped computations and exposed rereads, grouped without multiplying the compact construction into independent evidence. No new targeted or independent re-proof event is asserted. The immutable admission is `{manifest_binding['path']}` (SHA-256 `{manifest_binding['sha256']}`).\n\nPaper II now has all198 required rows resolved: the197 inherited rows and the additional P4.40 correction row. This resolves its required mathematical checks; all25 source-wide defect classes, provenance, integrated build and final-page reading remain open. The source SHA-256 is `{sha(source_after.encode())}`; the ledger has {len(events)+len(new_events)} rows, SHA-256 `{sha(event_after)}`. This admission adds {len(new_defects)} individual defect records, no global defect closure and no final PDF reading credit. New program paths remain in the final pinned-link verification gate. Papers III/IV have not begun, and I/V remain closed until five-paper integration.\n'''
for name in ['PROGRESS_LEDGER.md','S6_SERIES_PUBLISH_report.md']:
    with (R/name).open('ab') as f:f.write(note.encode())
assert (R/'CHECK_EVENTS.tsv').read_bytes().startswith(event_before)
assert (R/'S6_SERIES_PUBLISH_II.tex').read_bytes()==source_after.encode()
assert sum(x['paper']=='II' for x in completion['rows'].values())==198
receipt=dict(recorded_utc=dt.datetime.now(dt.timezone.utc).isoformat(),manifest=manifest_binding,
    canonical_after_bindings=[binding(n) for n,_,_ in changes]+[binding(completion_path),binding(program_path)],
    additional_required_registry_unchanged=True,required_II_done=198,required_II_open=0,
    no_prior_events_deleted_or_changed=True,all_old_tags_and_labels_preserved=True,
    source_bytes=len(source_after.encode()),events_added=len(new_events),defect_rows_added=len(new_defects))
(OUT/'admission_receipt.json').write_bytes(encode(receipt))
print(json.dumps({k:manifest[k] for k in ['created_utc','source_after_sha256','ledger_rows_after','events_added','event_types','defect_rows_added','required_II_total','required_II_done','final_pdf_page_credit']},indent=2))
print('Manifest:',manifest_binding['path'],manifest_binding['sha256'])
