"""Apply the reviewed atlas and two exact F14 source transports.

Every replaced passage and every inventory status transition is retained in
the receipt. Mathematical status does not award the remaining review gates.
"""
from pathlib import Path
import csv
import hashlib
import json
import re

R = Path(__file__).resolve().parents[1]
csv.field_size_limit(10**9)
receipt_path = R / 'analysis/I_atlas_and_F14_integration_05.json'
assert not receipt_path.exists(), 'This integration is one-shot.'
sha = lambda s: hashlib.sha256(s.encode()).hexdigest()
proposal = json.loads((R / 'audit_paper_i/open_atlas/integration_proposal.json').read_text())
pending = {}
before = {}
changes = []
for patch in proposal['patches']:
    path = Path(patch['file'])
    assert path.is_relative_to(R)
    if path not in pending:
        before[path] = pending[path] = path.read_text()
    text = pending[path]
    assert sha(patch['old']) == patch['old_sha256']
    assert text.count(patch['old']) == patch['occurrences'] == 1
    pending[path] = text.replace(patch['old'], patch['new'], 1)
    changes.append(patch)

# The assembler's documented fallback selects this existing owner map.
owner = R / 'audit_paper_i/main_index_I.json'
old_map = json.loads(owner.read_text())
new_map = json.loads((R / 'audit_paper_i/open_atlas/main_index_I_with_atlas.json').read_text())
for a, b in zip(old_map['main_theorems'], new_map['main_theorems']):
    assert a['letter'] == b['letter']
    if a['letter'] != 'D':
        assert a == b
before[owner] = owner.read_text()
pending[owner] = json.dumps(new_map, indent=2, ensure_ascii=False) + '\n'

iv = R / 'parts/IV.body.linked.tex'
before[iv] = pending[iv] = iv.read_text()
f14_patches = json.loads((R / 'audit_corrections/IV_F14_index_citation_patches.json').read_text())
for patch in f14_patches:
    old, new = patch['old_text'], patch['new_text']
    assert pending[iv].count(old) == 1
    pending[iv] = pending[iv].replace(old, new, 1)
for macro in ('label', 'tag'):
    pat = r'\\' + macro + r'\{[^}]+\}'
    assert re.findall(pat, before[iv]) == re.findall(pat, pending[iv])

# Preserve all earlier bibliography edits and append only the reviewed source.
bbl_path = R / 'analysis/source_bibliography_entries.json'
bbl = json.loads(bbl_path.read_text())
addition = json.loads((R / 'audit_paper_i/open_atlas/source_bibliography_entry.json').read_text())
assert not set(addition).intersection(bbl)
bbl.update(addition)
f14_source = json.loads((R / 'audit_corrections/IV_F14_primary_source_update.json').read_text())
f14_bbl_note = (
    '\n\\newblock Additional verified scope on 19 November 2026: '
    'Index Theorem (2.12), p.~556; associated-symbol Proposition (2.17), '
    'p.~559, with its structure-group setup on pp.~557--558; '
    'the Dolbeault-symbol derivation and Riemann--Roch Theorem (4.3), '
    'pp.~563--565. The actual inherited Spin-c symbol and its line twist '
    'are transported through their explicit graded characters.\n'
)
for entry in bbl['AtiyahSinger1968IIIE']:
    entry['text'] += f14_bbl_note
before[bbl_path] = bbl_path.read_text()
pending[bbl_path] = json.dumps(bbl, indent=2, ensure_ascii=False) + '\n'
bib_path = R / 'analysis/additional_references.bib'
before[bib_path] = bib_path.read_text()
atlas_bib = (R / 'audit_paper_i/open_atlas/additional_reference.bib').read_text()
assert 'AbateBracciSuwaTovena2010Atiyah' not in before[bib_path]
# Override the original AS entry without losing any original metadata.
from assemble_series import bib_entries
base_bib = (R.parent / 'S6_SERIES_GRIND_source/S6_GRIND_1_papers_cp15/S6_10_PAPERS_references.bib').read_text()
current_bib = bib_entries(base_bib)
current_bib.update(bib_entries(before[bib_path]))
as_entry = current_bib['AtiyahSinger1968IIIE']['text'].rstrip()
assert as_entry.endswith('}')
as_entry = as_entry[:-1].rstrip().rstrip(',') + ',\n  current_verification = {' + f14_source['bibliography_note_append'] + '}\n}'
pending[bib_path] = before[bib_path].rstrip() + '\n\n' + atlas_bib.rstrip() + '\n\n' + as_entry + '\n'

assessment_path = R / 'audit_paper_i/row_assessments.json'
assessments = json.loads(assessment_path.read_text())
previous_assessment = assessments['inv:C3.8']
atlas_assessment = json.loads((R / 'audit_paper_i/open_atlas/row_assessment_proposed.json').read_text())['inv:C3.8']
atlas_assessment['confidence_state'] = 'complete standard-family coefficient proof integrated; independent reconstruction and PDF gates pending'
atlas_assessment['remaining_risk'] = (
    'The complete standard-family proof has been integrated after full targeted receiving review. '
    'A separate reviewer is reconstructing it from the isolated statement and earlier inputs before reading this proof. '
    'The final source page locator, rendered-layout verification and global main-theorem assessment remain recorded gates. '
    'The complex Q differs from the metric harmonic lift by the proved C*d1g ambiguity; the claim concerns the stated standard family.'
)
atlas_assessment['format_check'] = 'Nine exact guarded replacements integrated; earlier operator proof and both gauge labels retained. Pending compiled inspection.'
atlas_assessment['completion_state'] = 'pending independent reconstruction, final source locator and rendered layout'
atlas_assessment['layout_check'] = 'pending build 19 and actual rendered-page inspection'
assessments['inv:C3.8'] = atlas_assessment
before[assessment_path] = assessment_path.read_text()
pending[assessment_path] = json.dumps(assessments, indent=2, ensure_ascii=False) + '\n'

inventory = R / 'S6_SERIES_GRIND_inventory.csv'
with inventory.open() as f:
    rows = list(csv.DictReader(f))
columns = list(rows[0])
status_changes = []
for row in rows:
    if row['label'] != 'inv:C3.8':
        continue
    assert row['status'] == 'open'
    status_changes.append({'source_inventory_row': row['source_inventory_row'],
                           'source_id': row['source_id'], 'old': 'open', 'new': 'proved',
                           'old_kind': row['kind']})
    row['status'] = 'proved'
    row['kind'] = 'Proposition' if row['source_id'] == 'C3.8' else 'Remark, canonical atlas consequence'
    row['credited_to'] = (
        'Original AC26 family data; DGKX v1 section 6.4 scalar cocycle preceding Lemma 6.14; '
        'Abate--Bracci--Suwa--Tovena Theorem 3.1 and proof p.10 for the Cech--Dolbeault conversion. '
        'The explicit local one-form cocycle, annular connections and evaluated coefficient system are proved here.'
    )
    row['credit_transport'] = 'a=c+delta, Omega_a=Pi_c; f=-eta_DGKX on all six generating arrow types; -barpartial(w0)c01/12=barpartial(w1*c01)/12.'
    row['source_credit_verdict'] = 'Known scalar input and general conversion credited; exact family-specific one-form formula compared at the listed primary-source scopes.'
    row['literature_disposition'] = 'Retain full exact coefficient construction and the earlier operator proof; source comparison in audit_paper_i/open_atlas/SOURCE_COMPARISON.md.'
    row['literature_searches'] += '\nCurrent atlas comparison and six bounded primary-literature searches: audit_paper_i/open_atlas/SOURCE_COMPARISON.md.'
    row['completion_state'] = atlas_assessment['completion_state']
assert len(status_changes) == 3

for path, value in pending.items():
    if path.suffix == '.tex':
        for env in ('proof', 'enumerate'):
            assert value.count(r'\begin{' + env + '}') == value.count(r'\end{' + env + '}'), (str(path), env)
    path.write_text(value)
with inventory.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()
    writer.writerows(rows)
receipt = {
    'atlas_changes': changes, 'F14_changes': f14_patches,
    'map_owner': str(owner.relative_to(R)),
    'map_changes_confined_to_D_and_block25_disposition': True,
    'status_changes': status_changes,
    'mathematical_status_does_not_award_whole_row_completion': True,
    'previous_atlas_assessment': previous_assessment,
    'source_metadata': f14_source,
    'files': {str(p.relative_to(R)): {'before_sha256': sha(before[p]), 'after_sha256': sha(s)} for p, s in pending.items()},
    'full_receiving_math_review': 'audit_root/I_coefficient_atlas_review_04.md',
    'independent_reconstruction_input': 'audit_root/I_atlas_statement_only_05.tex',
}
receipt_path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + '\n')
print(json.dumps({'atlas_replacements': len(changes), 'F14_replacements': len(f14_patches),
                  'inventory_promotions': len(status_changes), 'whole_row_done_awarded': 0}))
