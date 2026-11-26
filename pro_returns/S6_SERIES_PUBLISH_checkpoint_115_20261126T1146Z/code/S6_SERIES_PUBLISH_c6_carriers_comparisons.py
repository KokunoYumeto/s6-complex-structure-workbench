#!/usr/bin/env python3
"""Prepare exact individual 036Z/037K comparison records; never edit III.

The targeted check spans a saved fifth-continuation fresh derivation and
the sixth-continuation comparison. It is one check per statement. Reading
the saved derivation is not represented as a new independent derivation.
"""
from pathlib import Path
import csv
from datetime import datetime, timezone
import hashlib
import re

ROOT = Path(__file__).resolve().parent.parent
LANE = ROOT / 'agents/continuation6_iii_carriers'
OLD_LANE = ROOT / 'agents/continuation5_iii_carriers'
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
SOURCE_SHA = '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
FIELDS = next(csv.reader((ROOT / 'CHECK_EVENTS.tsv').open(), delimiter='\t'))
DEFECT_FIELDS = ['change_id', 'type', 'statement_id', 'old_location',
                 'old_page', 'new_location', 'new_page', 'old_text',
                 'new_text', 'reason', 'review_status']
NOW = datetime.now(timezone.utc).isoformat()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_tsv(path, fields, rows):
    with path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fields, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


source_bytes = SOURCE.read_bytes()
assert sha(source_bytes) == SOURCE_SHA
lines = source_bytes.decode().splitlines(keepends=True)
all_labels = set(re.findall(r'\\label\{([^}]+)\}', source_bytes.decode()))
specs = [
    ('036Z', 'wb:cusp-cone-moving-S4-null-homotopy', 26662, 26674,
     '3dbb12cd1637c0983999e780ee35bb776b9a258e300fe49a7e922e52e91c50c3',
     '2026-11-24T01:32:31+00:00', '2026-11-24T01:41:17Z',
     'f43e992e3806617dfb946a7aae24078d40b0bd41f7925080da5582688490a30a'),
    ('037K', 'wb:cusp-cone-sphere-map-homotopy-status', 26681, 26703,
     '13a587f03ed9baaab133652bcd5c4882782fd5fd8fa578cbd722b5cd4600a230',
     '2026-11-24T01:49:28+00:00', '2026-11-24T01:51:26Z',
     '24dfffbb91fc9acc05da778465a31da8fc54f8d28a5d749c8b0acd1ccf7c9fe5'),
]

for tag, label, first, last, fresh_sha, freeze, release, old_sha in specs:
    prefix = f'S6_SERIES_PUBLISH_III_{tag}'
    old = ''.join(lines[first-1:last]).rstrip('\n')
    new_path = LANE / f'{prefix}_receiving.tex'
    new = new_path.read_text().rstrip('\n')
    fresh_path = OLD_LANE / f'{prefix}_fresh_derivation.md'
    assert sha(fresh_path.read_bytes()) == fresh_sha
    assert sha(old.encode()) == old_sha
    released = (OLD_LANE / f'{prefix}_released_argument.tex').read_text()
    assert released[released.index('\\paragraph{'):].strip() == old
    assert source_bytes.decode().count(old) == 1
    assert new.count('\\label{' + label + '}') == 1
    assert new.count('\\hypertarget{tag-' + tag + '}{}') == 1
    assert re.findall(r'\\label\{([^}]+)\}', new) == [label]
    assert '\\StatementRecord' not in new
    for refgroup in re.findall(r'\\(?:c|C|eq|auto)?ref\{([^}]+)\}', new):
        assert set(refgroup.split(',')) <= all_labels
    for p in [new_path, LANE / f'{prefix}_comparison.md']:
        assert b'\r' not in p.read_bytes()

    replacement_reason = (
        'Individual authorized paragraph only; all mathematical conclusions '
        'preserved after full saved-fresh/original/receiving comparison. '
        'The fifth-continuation independent derivation and sixth-continuation '
        'comparison form one targeted check. Preserve label and tag; replace '
        'machine metadata and orphan prose by a numbered mathematical block. '
        'No neighboring identity or unit/page gate is closed by this guard.'
    )
    write_tsv(LANE / f'{prefix}_replacements.tsv',
              ['statement_id', 'old_text', 'new_text', 'reason'],
              [dict(statement_id=label, old_text=old, new_text=new,
                    reason=replacement_reason)])

    defect_rows = []

    def defect(suffix, kind, before, after, reason):
        assert before in old
        assert not after or after in new
        defect_rows.append(dict(
            change_id=f'c6-III-{tag}-{suffix}', type=kind, statement_id=label,
            old_location=f'S6_SERIES_PUBLISH_III.tex:{first}-{last}',
            old_page='', new_location=new_path.relative_to(ROOT).as_posix(),
            new_page='', old_text=before, new_text=after, reason=reason,
            review_status='proposed; complete comparison done; root admission, '
                          'source application and final page review pending'))

    header = next(line for line in old.splitlines() if line.startswith('\\StatementRecord'))
    defect('machine-header', 'D10', header, '',
           'Remove the machine record while keeping the exact permanent tag and label.')
    heading = old.splitlines()[0]
    new_heading = new.splitlines()[0]
    defect('orphan-paragraph', 'D13', heading, new_heading,
           'Give the mathematical text a numbered block: a lemma with its proof '
           'for 036Z, or a remark citing the proved homotopies for 037K.')
    if tag == '036Z':
        before = ('Thus the moving metric\nfour-spheres do not contradict the '
                  'fixed-target orientation obstruction:\ntheir fundamental '
                  'classes die in the ambient targets.')
        after = ('Thus the fundamental classes of both moving four-spheres '
                 'have zero\nimage in their ambient targets.')
        defect('orientation-wording', 'D02', before, after,
               'State the actual H4 pushforwards and their zero values, '
               'with the full based homotopies giving the result.')
        scope = ('All four original nullity assertions and both fundamental-class '
                 'pushforwards agree. Complete radial homotopies fix the based '
                 'meridians and descend jointly through the two fat-wedge '
                 'quotients. Every native interior height is covered. The exact '
                 'quotient markings and every endpoint are preserved.')
    else:
        defect('history-comment', 'D01',
               '% checked carrier correction: one-copy-status', '',
               'Remove production-history wording from the source comment.')
        before = ('In both cases the vanishing is a\ntheorem about the full '
                  'specified sphere-valued map, not merely its Hurewicz\nimage '
                  'or the inclusion of a moving four-sphere.')
        after = ('These formulas identify them on all of \\(X\\)\nwith the two '
                 'maps of the cited proposition, through the displayed\n'
                 'target homeomorphisms.')
        defect('full-map-wording', 'D02', before, after,
               'Replace the defensive contrast by exact global map identities '
               'and the explicit torus, quotient and suspension morphisms.')
        defect('repeated-scope', 'D11',
               'The retained-angle\nmap has a different target and is outside that assertion.', '',
               'The remark positively defines both named maps and preserves all '
               'claims about them; the repeated exclusion carries no further result.')
        scope = ('All positive-degree homology/cohomology assertions, ordinary '
                 'Hurewicz maps, equal-dimensional degree wording, both '
                 'one-copy nullities and every positive smash-power nullity '
                 'agree. The beta quotient-basis map and its inverse identify '
                 'the exact global maps with admitted 02Q7, including both '
                 'cusp endpoints and the fixed point x0. The homotopy proof '
                 'is cited once, without duplicating it. No 035Z or 038S '
                 'comparison credit is claimed.')
    write_tsv(LANE / f'{prefix}_defects.tsv', DEFECT_FIELDS, defect_rows)

    event_file = LANE / f'{prefix}_CHECK_EVENTS.tsv'
    event_id = f'publish:c6:III:{tag}:targeted-completed'
    event = {field: '' for field in FIELDS}
    event.update(
        statement_id=label, date=NOW[:10],
        who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not '
            'separately exposed; fifth-continuation carriers checker '
            '(pre-release derivation) and sixth-continuation carriers checker '
            '(full comparison)',
        type='targeted proof check',
        outcome=f'Saved fresh derivation completed {freeze}, SHA256 {fresh_sha}, '
                f'before recorded individual release {release}. Sixth-continuation '
                'checker read that saved work, the complete authorized original '
                'paragraph, and the complete receiving text; this reader claims '
                'no new independent re-derivation. ' + scope +
                ' No theorem refuted; no separate new computation event. '
                'Source application, unit restructuring and final page review remain open.',
        event_id=event_id,
        phase='completion of saved pre-release derivation by authorized original/receiving comparison',
        source_file='S6_SERIES_PUBLISH_III.tex', source_row=str(first),
        source_event_type='targeted proof check', evidence_group=event_id,
        publish_input_file=event_file.relative_to(ROOT).as_posix(),
        publish_input_row='2', date_utc=NOW,
        where='; '.join([fresh_path.relative_to(ROOT).as_posix(),
                         (LANE / f'{prefix}_comparison.md').relative_to(ROOT).as_posix(),
                         (LANE / f'{prefix}_replacements.tsv').relative_to(ROOT).as_posix()]))
    write_tsv(event_file, FIELDS, [event])
    print(tag, 'complete comparison:', len(old.splitlines()), 'original lines;',
          len(new.splitlines()), 'receiving lines;', len(defect_rows),
          'defect rows; one proposed cross-continuation targeted check')

assert SOURCE.read_bytes() == source_bytes
print('Canonical source and all global tables unchanged; prepared', NOW)
