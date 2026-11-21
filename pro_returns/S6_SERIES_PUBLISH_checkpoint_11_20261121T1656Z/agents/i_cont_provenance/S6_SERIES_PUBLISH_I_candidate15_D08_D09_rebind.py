#!/usr/bin/env python3
"""Carry the completed contextual audit through the exact candidate14-to15 edit map.

The assistant read all seven changed extracted contexts on candidate15. The
other 243 extracted contexts are byte-identical strings under the same defined
whitespace map. The source reconstruction proves the exact three deletions.
This occurrence binding creates no mathematical event or full-page credit.
"""
from pathlib import Path
from datetime import datetime, timezone
import collections
import copy
import csv
import hashlib
import json
import re
import fitz

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SOURCE_SHA = '45bf46fc14a50f7a148cdd34bf2be68b04cd89e1cb7d620191c6e8518f7249f8'
PDF_SHA = 'b72c6da6acddfd797c82837fbd086e222eeef8e4526ed736328affde474df780'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bind(path):
    return {'path': str(path.relative_to(ROOT)), 'sha256': sha(path), 'bytes': path.stat().st_size}


source = ROOT / 'S6_SERIES_PUBLISH_I.tex'
pdf = ROOT / 'build/I_candidate15/S6_SERIES_PUBLISH_I.pdf'
before_source = OUT / 'candidate14/inputs/S6_SERIES_PUBLISH_I.tex'
prior_path = OUT / 'candidate14/S6_SERIES_PUBLISH_I_cont_D08_D09_dispositions.json'
source_binding_path = OUT / 'S6_SERIES_PUBLISH_I_candidate15_source_count_rebinding.json'
edit_receipt_path = ROOT / 'agents/i_cont_edits/S6_SERIES_PUBLISH_I_candidate14_residue_receipt.json'
assert sha(source) == SOURCE_SHA
assert sha(pdf) == PDF_SHA
assert sha(prior_path) == '814664a3501d2c9e449183d9715ac36079a6a5df599d72f374ef81e688a58f85'
prior = json.loads(prior_path.read_text())
source_binding = json.loads(source_binding_path.read_text())
edit_receipt = json.loads(edit_receipt_path.read_text())
assert source_binding['source']['sha256'] == SOURCE_SHA
assert source_binding['exact_whole_source_reconstruction_from_three_edits']
before = before_source.read_text()
after = source.read_text()
mapped = before
for change in edit_receipt['changes']:
    assert mapped.count(change['old']) == 1
    mapped = mapped.replace(change['old'], change['new'], 1)
assert mapped == after

patterns = {
    'D08': re.compile(r'\b(?:actual|retain\w*|supplied|specified|fresh|executed|saved|receipt|candidate|survivor|verified|probe)\b', re.I),
    'D09': re.compile(r'\.py\b|\.jsonl?\b|code/|audit_|receipt|SHA-256|rows \(4|columns numbered|identities at their recorded scopes|--fresh', re.I),
}
for kind, pattern in patterns.items():
    assert pattern.findall(before) == pattern.findall(after), kind
    for change in edit_receipt['changes']:
        assert pattern.findall(change['old']) == pattern.findall(change['new']), (kind, change['guard_id'])

current = collections.defaultdict(list)
doc = fitz.open(pdf)
for page in doc:
    text = ' '.join(page.get_text().split())
    for kind, pattern in patterns.items():
        for match in pattern.finditer(text):
            current[kind].append({
                'page': page.number+1,
                'hit': match[0],
                'text_offset': match.start(),
                'context': text[max(0, match.start()-100):match.end()+200],
            })
for kind in patterns:
    inherited = [row for row in prior['rows'] if row['type'] == kind]
    assert [row['hit'] for row in inherited] == [row['hit'] for row in current[kind]]
assert len(current['D08']) == 192 and len(current['D09']) == 58

reviewed_changed_contexts = {
    290: 'The period-column instruction and displayed gamma,u,w,delta,s,v data are unchanged. The proof begins on this page; the preceding statement tail is now on the previous page.',
    295: 'The choice of components dominating B and positive degree, Cohen-Macaulay property and finite flat map are unchanged. The current page continues into the trace sentence.',
    307: 'The retained rational function and its displayed line-bundle comparisons are unchanged. The proof begins on this page; the preceding statement tail is now on the previous page.',
    382: 'The same two program rows and receiving mathematical statements occur in the Programs table. Only the extracted page footer in this context changes from 333 to 332.',
    383: 'The same monodromy program filename ends the Programs-table page. Only the extracted footer changes from 333 to 332.',
    402: 'The same trace obstruction and trace section program rows occur in the Programs table. Only the extracted footer changes from 334 to 333.',
    403: 'The same trace section program filename ends the Programs-table page. Only the extracted footer changes from 334 to 333.',
}
ordinals = collections.Counter()
rows = []
changed_rows = []
for oldrow in prior['rows']:
    kind = oldrow['type']
    cur = current[kind][ordinals[kind]]
    ordinals[kind] += 1
    row = copy.deepcopy(oldrow)
    same_context = row['candidate14_context'] == cur['context']
    row.update({
        'candidate15_page': cur['page'],
        'candidate15_context': cur['context'],
        'candidate15_text_offset': cur['text_offset'],
        'candidate14_to15_context_exactly_equal': same_context,
        'disposition_inherited_from_completed_candidate14_context_review': True,
        'source_difference_binding': str(source_binding_path.relative_to(ROOT)),
    })
    if not same_context:
        index = row['scan_row_index_1based']
        assert index in reviewed_changed_contexts
        row['candidate15_changed_context_review'] = reviewed_changed_contexts[index]
        changed_rows.append(index)
    else:
        row['candidate15_changed_context_review'] = 'The exact extracted context is unchanged under the same page-text whitespace map.'
    assert not row['confirmed_defect']
    rows.append(row)
assert set(changed_rows) == set(reviewed_changed_contexts)

fuller_passages = copy.deepcopy(prior['fuller_source_passages_examined'])
for passage in fuller_passages:
    assert after.count(passage['text']) == 1
    position = after.index(passage['text'])
    passage['candidate15_exact_passage_preserved'] = True
    passage['candidate15_excerpt_start_line'] = after.count('\n', 0, position)+1

result = {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'paper': 'I',
    'candidate': 15,
    'source_sha256': SOURCE_SHA,
    'pdf_sha256': PDF_SHA,
    'source': bind(source),
    'pdf': bind(pdf),
    'page_count': len(doc),
    'inherited_completed_context_review': bind(prior_path),
    'source_delta_binding': bind(source_binding_path),
    'edit_receipt': bind(edit_receipt_path),
    'source_exact_reconstruction_verified': True,
    'source_pattern_occurrence_sequences_exactly_equal': True,
    'pdf_pattern_occurrence_sequences_exactly_equal': True,
    'correspondence': 'Within each defect type, the entire case-sensitive hit sequence is equal. The order-preserving bijection records all 250 candidate15 pages and contexts. The source is independently reconstructed using precisely the three recorded clause deletions, none of which changes either pattern sequence.',
    'counts': dict(collections.Counter(row['type'] for row in rows)),
    'previously_read_candidate14_contexts': 250,
    'candidate15_contexts_exactly_equal_to_candidate14': 243,
    'candidate15_changed_contexts_read': 7,
    'candidate15_changed_context_row_indices': changed_rows,
    'rows': rows,
    'fuller_previously_examined_source_passages': fuller_passages,
    'confirmed_new_defects': [],
    'proposed_guards': [],
    'page_reading_credit_added': 0,
    'mathematical_events_added': 0,
    'shared_files_modified': False,
    'scope': 'Contextual residue audit transfer through a verified whole-source edit map, complete PDF occurrence correspondence and actual reading of all seven changed extracted contexts. Complete rendered-page review retains its separate evidence and gate.',
}
dest = OUT / 'S6_SERIES_PUBLISH_I_candidate15_D08_D09_dispositions.json'
dest.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
fields = ['scan_row_index_1based', 'type', 'hit', 'candidate13_page', 'candidate14_page', 'candidate15_page', 'candidate14_to15_context_exactly_equal', 'disposition', 'reason', 'candidate15_changed_context_review', 'confirmed_defect', 'full_page_reading_credit', 'mathematical_check_event_added']
with (OUT / 'S6_SERIES_PUBLISH_I_candidate15_D08_D09_dispositions.tsv').open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t', extrasaction='ignore')
    writer.writeheader()
    writer.writerows(rows)
assert sha(source) == SOURCE_SHA and sha(pdf) == PDF_SHA
print(json.dumps({
    'receipt': str(dest.relative_to(ROOT)),
    'receipt_sha256': sha(dest),
    **{key: result[key] for key in ['source_sha256', 'pdf_sha256', 'page_count', 'counts', 'candidate15_contexts_exactly_equal_to_candidate14', 'candidate15_changed_contexts_read', 'candidate15_changed_context_row_indices', 'confirmed_new_defects', 'page_reading_credit_added', 'mathematical_events_added']},
}, indent=2))
