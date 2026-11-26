"""Admit the common marked surface models after full proof comparison."""
from S6_SERIES_PUBLISH_c3_edit import *
import json

folder = ROOT / 'agents/continuation3_foundations/sec11'
prefix = 'S6_SERIES_PUBLISH_sec11_models_'
before = SOURCE.read_text()
after = before
guards = json.loads((folder / (prefix + 'guards.json')).read_text())
assert len(guards) == 8
for row in guards:
    assert after.count(row['old']) == 1, (row['key'], after.count(row['old']))
    after = after.replace(row['old'], row['new'], 1)
preserve_identifiers(before, after)
old_labels, old_tags = identifiers(before)
new_labels, new_tags = identifiers(after)
assert new_tags - old_tags == Counter({'tag-P354': 1})
assert not (old_tags - new_tags)
assert all(new_labels[k] == 1 for k in new_labels - old_labels)
assert all(new_tags[k] == old_tags.get(k, 1) for k in new_tags)

un66 = guards[2]
assert un66['old'].split(r'\end{proposition}', 1)[0] == un66['new'].split(r'\end{proposition}', 1)[0]
for label in ['push:src:E.5.2', 'push:src:E.5.3']:
    def statement(text):
        i = text.index(r'\label{' + label + '}')
        a = text.rfind(r'\begin{', 0, i)
        env = re.match(r'\\begin\{([^}]+)\}', text[a:]).group(1)
        b = text.index(r'\end{' + env + '}', i) + len(r'\end{' + env + '}')
        return text[a:b]
    assert statement(before) == statement(after), label

_, statuses = read_tsv(folder / (prefix + 'unit_progress.tsv'))
units = {r['unit'] for r in statuses}
assert units == {'subsec:II:section-preserving-rulings', 'subsec:II:vertical-field-divisors', 'subsec:II:torsion-interface-models'}
assert len(statuses) == 78
fields, progress = read_tsv(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv')
assert not any(r['paper'] == 'II' and r['unit_id'] in units for r in progress)
titles = {label: title for title, label in re.findall(r'^\\subsection\{([^\n]+)\}\\label\{([^}]+)\}', after, re.M)}
for row in statuses:
    kind = 'structure' if row['row'] == 'restructuring' else row['row']
    progress.append(dict(zip(fields, ['II', row['unit'], titles[row['unit']],
        'structure' if kind == 'structure' else 'defect', '' if kind == 'structure' else kind,
        'open' if kind in {'D14', 'D23', 'D24', 'structure'} else row['status'], now(),
        'CHECK_EVENTS.tsv: II-C3-ROOT-COMMON-MODELS-ADMISSION',
        row['basis'] + ' Complete old/current and receiving proofs read by foundations. Root read the complete final P354, UN80, merged UN70/83 and UN66 receiving proofs, comparison, all-class assessments and exact application maps. UN67 is moved intact. Original sec11 and remaining reduction units retain their open rows; no subdivision, independent-check, required-check or final-page credit.'])))
keys = [(r['paper'], r['unit_id'], r['defect_type'] or r['row_kind']) for r in progress]
assert len(keys) == len(set(keys))
for suffix, target, key in [
    ('defects.tsv', 'S6_SERIES_PUBLISH_defects_II.tsv', 'change_id'),
    ('CHECK_EVENTS.tsv', 'CHECK_EVENTS.tsv', 'event_id')
]:
    _, rows = read_tsv(folder / (prefix + suffix))
    if suffix == 'CHECK_EVENTS.tsv':
        assert all(r['type'] == 'used and rechecked in this run' and 'effort' in r['who'] for r in rows)
    print(suffix, append_rows(ROOT / target, rows, key))
SOURCE.write_text(after, newline='\n')
write_tsv(ROOT / 'S6_SERIES_PUBLISH_unit_progress.tsv', fields, progress)
add_event('lem:II:section-preserving-ruling;cdp:st:C.2.UN.80;cdp:st:C.2.UN.83;cdp:st:C.2.UN.70;cdp:st:C.2.UN.66',
    'II-C3-ROOT-COMMON-MODELS-ADMISSION', 'used and rechecked in this run',
    'Eight exact guards admitted after full foundations old/current/new proof comparison and root complete receiving-proof readings. P354 factors the same section-preserving ruled maps and descends the deck action. UN80 uses the explicit full reduced NC normalization, complete inverse boundary, given point map and connected elliptic fibration; the averaging coordinate has its stated inverse and every exceptional prime is polar. The common UN83/UN70 owner preserves all three surface models and the nonnegative-coefficient specialization, with the same residue, torsor, normal-order, pencil and quotient maps. The UN66 full statement is byte-identical; its shared marked-model proof now applies the preceding owner at the identity point map. Every old label and tag survives, with only new tag P354. Protected E.5.2/E.5.3 statements are byte-identical. Existing source-locus evidence is reused, not upgraded. Original sec11 and its remaining reduction proofs stay open. No independent-check, required-check, subdivision or final-page credit.',
    'Three new actual common-model subsections and bounded UN66 receiving proof', source=__file__)
print('Common models admitted; original section11 remainder and global gates stay open.')
