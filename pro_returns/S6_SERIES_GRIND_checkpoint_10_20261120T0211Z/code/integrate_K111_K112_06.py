"""Integrate the fully received new K111 filling and preserve its older route.

One-time edit. The mathematical source and every old formula are retained;
the unavailable original execution is moved to an explicit final problem.
"""
import collections
import csv
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sha = lambda data: hashlib.sha256(data).hexdigest()
manifest = json.loads((ROOT/'audit_sign/K111_guarded_integration.json').read_text())
active_path = ROOT/'audit_sign'/manifest['active_file']
final_path = ROOT/'audit_sign'/manifest['final_file']
assert sha(active_path.read_bytes()) == manifest['active_sha256']
assert sha(final_path.read_bytes()) == manifest['final_sha256']
assert manifest['active_sha256'] == '2365deca1c366e66b2dd5d4a7c0a37e9c801d8e11b3ce80c07eea3688e4e8699'
assert manifest['final_sha256'] == '45adbd82e7d1fbc41d48755e7ce5d55a1dbe9ba8d3ae3911640b9041bcad2c0b'
active = active_path.read_text()
archived = final_path.read_text()
assert r'\begin{pmatrix}-2&1\\1&-2\end{pmatrix}' in active
assert r'\begin{pmatrix}-2&1\1&-2\end{pmatrix}' not in active
receiving = ROOT/'audit_corrections/K111_auxiliary_boundary_comparison_05.md'
assert sha(receiving.read_bytes()) == '7c70e0fd26792cd94f3b2ea597d9b1fe53f41c7eaeacd8209d6f25b98c016b18'
body = ROOT/'parts/IV.body.linked.tex'
text = body.read_text()
before = sha(text.encode())
a = text.index(r'\label{night:P3K.111}')
p = text.index(r'\begin{proof}',a)
z = text.index(r'\subsection{The complete selected-I3 M2 return',p)
old = text[p:z]
assert sha(old.encode()) == '9b672f602b90136b7bf1171da9a04a7c552b7c9b36c0413d9859d1b485fa9485'
tags = lambda s: collections.Counter(re.findall(r'\\(?:tag|label)\{([^{}]*)\}',s))
oldtags = tags(old)
newtags = tags(active+archived)
assert newtags.pop('iv:open:K111:original_auxiliary_arrays') == 1
assert newtags == oldtags and sum(oldtags.values()) == 445
for guard in manifest['guards']:
    assert sha(guard['old_text'].encode()) == guard['old_sha256']
    assert old.count(guard['old_text']) == 1, guard['location']
    assert guard['old_text'] in archived, guard['location']
scope_patch = json.loads((ROOT/'audit_corrections/K111_inherited_scope_patch_05.json').read_text())[0]
assert scope_patch['new_text'] in active
for obsolete in ('136,442','143,270','149,774','2723','19124','2712','19092','3,888','324 source charts','321 rays'):
    assert obsolete not in active, obsolete
text = text[:p]+active+'\n\n'+text[z:]
for label in ('night:P3K.111','night:P3K.112'):
    old_record = r'\StatementRecord{'+label+'}{open}'
    assert text.count(old_record) == 1
    text = text.replace(old_record,r'\StatementRecord{'+label+'}{proved}',1)
body.write_text(text)
# This move must precede insertion of the archived final block: its final
# existing subsection ends at EOF, and must not acquire the archive.
subprocess.run([sys.executable,str(ROOT/'code/move_established_IV.py')],cwd=ROOT,check=True)
text = body.read_text()
label = 'iv:open:K111:original_auxiliary_arrays'
needle = r'\label{'+label+'}'
assert archived.count(needle) == 1 and needle not in text
record_prefix = r'\StatementRecord{'+label+r'}{open}'
assert archived.count(record_prefix) == 1
text += '\n\n'+r'\section{The unreconstructed original selected-I3 auxiliary atlas}'+'\n\n'+archived
assert text.index(r'\label{night:P3K.111}') < text.index(r'\part{Results not yet established}')
assert text.index(r'\label{night:P3K.112}') < text.index(r'\part{Results not yet established}')
assert text.index(needle) > text.index(r'\part{Results not yet established}')
body.write_text(text)

invpath = ROOT/'S6_SERIES_GRIND_inventory.csv'
with invpath.open() as stream:
    rows = list(csv.DictReader(stream)); columns = list(rows[0])
updated = []
for row in rows:
    if row['label'] in ('night:P3K.111','night:P3K.112'):
        assert row['status'] == 'open'
        row['status'] = 'proved'
        row['placement_state'] = 'printed in IV before the final part'
        row['completion_state'] = 'pending new-proof current rendered-layout verification and final source-credit integration'
        updated.append(row['label'])
assert set(updated) == {'night:P3K.111','night:P3K.112'}
assert not any(r['label'] == label for r in rows)
proposal = json.loads((ROOT/'audit_sign/K111_final_alternate_inventory.json').read_text())
row = {k:'' for k in columns}
row.update(label=label,paper='IV',source_paper='IV',source_run='S6_SERIES_GRIND',
           source_id='K111.original_auxiliary_arrays',source_inventory_row='series-new:K111.original_auxiliary_arrays',
           kind='Problem',status='open',main_or_supporting='supporting',source_main_or_supporting='supporting',
           uses='night:P3K.111',placement_state='printed in IV final part',
           writing_state='Complete original alternative and every formula preserved with the exact missing ordered arrays identified',
           confidence_state=proposal['confidence_state'],confidence_line=proposal['confidence_line'],
           remaining_risk=proposal['remaining_risk'],completion_state='pending current final-part layout and disposition review',
           credited_to='The exact original K111 auxiliary construction is preserved from the attached cp15 source; the new proved filling is separately identified.',
           notes=proposal['inventory_reason'])
rows.append(row)
with invpath.open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=columns);writer.writeheader();writer.writerows(rows)
receipt=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
             before_sha256=before,after_sha256=sha(text.encode()),
             active_sha256=manifest['active_sha256'],archived_input_sha256=manifest['final_sha256'],
             archived_integrated_sha256=sha(archived.encode()),
             received_boundary_report_sha256=sha(receiving.read_bytes()),
             guards=len(manifest['guards']),preserved_original_formula_tags=sum(oldtags.values()),
             newly_proved_labels=sorted(set(updated)),new_final_problem=label,
             root_review='All36 precise relocation guards, the entire revised proof20, the complete receiving boundary/inherited-scope report, and the one-line current/original proof diff were read before applying. Producing and independent computational work retain their separate named attribution.',
             retained_limit='No full graph projection is asserted for the counted interior. All failed graph-containment cases remain recorded. The absent older numerical arrays are preserved solely within the explicit final alternate-construction problem.',
             remaining='Current source build, references and rendered pages; final source-credit and whole-row completion metadata.')
(ROOT/'analysis/K111_K112_integration_06.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ('utc','guards','preserved_original_formula_tags','newly_proved_labels','new_final_problem')}))
