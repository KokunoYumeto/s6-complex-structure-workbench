#!/usr/bin/env python3
"""Prepare the fully compared KP replacement, without editing the source."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
OWN = ROOT / 'agents/continuation6_iii_root'
PREFIX = 'S6_SERIES_PUBLISH_III_02KP'
LABEL = 'maps:src:D.2.15'
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
source = SOURCE.read_bytes()
assert hashlib.sha256(source).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
fresh = OWN / (PREFIX + '_fresh_derivation.md')
assert hashlib.sha256(fresh.read_bytes()).hexdigest() == '059f4fd30b6d744ed5d76a9a80173f25dd9eca20184ae9953ab6e284e4b18324'
statement = (OWN / (PREFIX + '_released_statement.tex')).read_text()
statement = statement[statement.index('\\begin{theorem}'):].strip()
proof = (OWN / (PREFIX + '_released_proof.tex')).read_text()
proof = proof[proof.index('\\begin{proof}'):].strip()
assert hashlib.sha256(proof.encode()).hexdigest() == '9ecf238b31a4db335bab2c70e409e6d9a151f70c99f9e0aa51c65fdcf9180849'
assert len(proof.splitlines()) == 221
sb, pb = statement.encode(), proof.encode()
assert source.count(sb) == source.count(pb) == 1
start = source.index(sb)
pstart = source.index(pb, start + len(sb))
assert not source[start + len(sb):pstart].strip()
end = pstart + len(pb)
old = source[start:end].decode()
first = source.count(b'\n', 0, start) + 1
last = source.count(b'\n', 0, end) + 1
assert source.count(b'\n', 0, pstart) + 1 == 10540
assert last == 10760
receiver = OWN / (PREFIX + '_receiving.tex')
new = receiver.read_text().strip()
newproof = new[new.index('\\begin{proof}'):]
for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{(tag-[^}]+)\}',
                r'\\tag\{([^}]+)\}']:
    assert Counter(re.findall(pattern, old)) == Counter(re.findall(pattern, new))
assert len(re.findall(r'\\hypertarget\{tag-', new)) == 5
assert new.count('\\begin{proof}') == new.count('\\end{proof}') == 1
assert '\\StatementRecord' not in new and '\\begin{enumerate}' not in new
assert '.json' not in new and '.py' not in new


def write(path, fields, rows):
    with path.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t',
                                lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


replacement = dict(statement_id=LABEL, old_text=old, new_text=new,
    reason='Complete theorem and proof replacement after the full fresh '
           'derivation and comparison of every original item and auxiliary '
           'assertion. All five tag/label pairs and D.I1--D.I4 are preserved. '
           'The receiver prints one integral homology and characteristic-class '
           'recognition proof; the fully checked original circle-surgery '
           'recognition route remains in the comparison record.')
write(OWN / (PREFIX + '_replacements.tsv'), list(replacement), [replacement])
defects = []


def defect(suffix, kind, before, after, reason):
    assert before in old
    assert not after or after in new
    defects.append(dict(change_id='c6-III-02KP-' + suffix, type=kind,
        statement_id=LABEL,
        old_location=f'S6_SERIES_PUBLISH_III.tex:{first}-{last}', old_page='',
        new_location=receiver.relative_to(ROOT).as_posix(), new_page='',
        old_text=before, new_text=after, reason=reason,
        review_status='proposed; full original and receiving proof read; '
                      'root admission and canonical/unit/page gates pending'))


header = next(line for line in statement.splitlines()
              if line.startswith('\\StatementRecord'))
defect('header', 'D10', header, '',
       'Remove the machine header and preserve every permanent identity.')
defect('hierarchy', 'D10',
       '\\begin{enumerate}[label={$\\langle1\\rangle$\\arabic*.},leftmargin=*]',
       '', 'Replace the generated thirteen-item proof hierarchy with connected '
           'mathematical sections. The full comparison retains every old item.')
defect('title', 'D16',
       '\\begin{theorem}[all-order $S^2\\times S^4$ outputs]',
       '\\begin{theorem}[Logarithmic families with smooth type $S^2\\times S^4$]',
       'Use a mathematical title without an output/process marker; parameter '
       'scope and all conclusions are unchanged.')
defect('proof', 'D09', proof, newproof,
       'Replace file-dependent computation prose by the four matrices, '
       'primitive graph/exterior frames, integer inverses, local normal-disc '
       'maps, cusp kernel lift, all-parameter finite quotient, full van Kampen '
       'maps, and canonical/cubic/Pontryagin calculation. Apply the opened '
       'Zhubr primary classification once. The complete original surgery '
       'route, fixed-curve null classes and all auxiliary claims were checked '
       'and are retained in the comparison. Missing historical sample bytes '
       'are not claimed replayed. No original mathematical conclusion is refuted.')
defect('defensive', 'D02',
       'In particular this quotient has no hidden two-torsion.',
       'Its kernel is $\\mathbb Z\\langle(-2,2)\\rangle$, with inverse',
       'Replace defensive wording by the exact integral boundary kernel and '
       'its inverse; the free quotient is proved with its index.')
defect('lattice-map', 'D20',
       'preserves the triangular fan and identifies this lattice\nwith $2\\mathbb Z\\oplus\\mathbb Z$.',
       '$(Z,V)\\mapsto(ZV,V^{-1})$; the inverse sends',
       'Specify the integral period-basis conversion and both torus maps '
       'under the fan involution. The fresh and printed valuation bases '
       'are related by the displayed unimodular matrix and inverse.')
write(OWN / (PREFIX + '_defects.tsv'), list(defects[0]), defects)

with (ROOT / 'CHECK_EVENTS.tsv').open(newline='') as stream:
    fields = next(csv.reader(stream, delimiter='\t'))
now = datetime.now(timezone.utc).isoformat()
eid = 'publish:c6:III:02KP:targeted'
event = dict.fromkeys(fields, '')
event.update(statement_id=LABEL, date=now[:10],
    who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not '
        'separately exposed; sixth-continuation root checker',
    type='targeted proof check', event_id=eid,
    phase='complete fresh derivation followed by individual full comparison',
    outcome='Full 650-line fresh proof completed and reread at '
        '2026-11-24T14:24:06.690902+00:00 before individual release at '
        '2026-11-24T14:24:07.054692+00:00. Fresh SHA256 '
        '059f4fd30b6d744ed5d76a9a80173f25dd9eca20184ae9953ab6e284e4b18324. '
        'Read the entire 221-line original proof, all thirteen items and '
        'every auxiliary assertion, and the complete receiving proof. '
        'Independent primary cubic/section realization, dessin enumeration, '
        'modular path/peripheral maps, section quotient and height, and '
        'all integral graph, exterior, local and finite attachment maps '
        'were derived with new programs and all outputs/maps fully read. '
        'The new post-release comparison uses determinantal divisors, '
        'column Hermite form, adjugate inversion and toric character maps; '
        'its full code and output were read. Verified both fixed curves, '
        'their normal framings and null classes, the complete original '
        'circle-surgery route, and GR25 Theorems A/B(2) in the primary '
        'publisher text. Receiver prints the fresh direct spin/cubic/p1 '
        'recognition through the opened Zhubr Theorems3/5 and Section4.1; '
        'the English rank-notation issue is explicitly scoped in the '
        'comparison/fresh record. All five permanent tag/label pairs and '
        'D.I1--D.I4 preserved. The original 630 sample inputs and historical '
        'JSON are absent from the restored inputs; no bytewise comparison '
        'or rerun count is asserted. Failed fresh geometry attempt retained '
        'with no credit. No mathematical conclusion refuted. Canonical '
        'source, paper-unit, build and page gates remain open.',
    source_file='S6_SERIES_PUBLISH_III.tex', source_row=str(first),
    source_event_type='targeted proof check', evidence_group=eid,
    publish_input_file=(OWN / (PREFIX + '_CHECK_EVENTS.tsv')).relative_to(ROOT).as_posix(),
    publish_input_row='2', date_utc=now,
    where='; '.join([
        *(str((OWN / (PREFIX + '_' + suffix)).relative_to(ROOT)) for suffix in
          ('fresh_derivation.md', 'comparison.md', 'receiving.tex',
           'replacements.tsv', 'comparison_maps.json')),
        'code/' + PREFIX + '_comparison.py',
        'code/' + PREFIX + '_comparison.out']))
write(OWN / (PREFIX + '_CHECK_EVENTS.tsv'), fields, [event])
assert SOURCE.read_bytes() == source
assert hashlib.sha256(fresh.read_bytes()).hexdigest() == '059f4fd30b6d744ed5d76a9a80173f25dd9eca20184ae9953ab6e284e4b18324'
for suffix in ('receiving.tex', 'comparison.md', 'replacements.tsv',
               'defects.tsv', 'CHECK_EVENTS.tsv'):
    path = OWN / (PREFIX + '_' + suffix)
    assert b'\r' not in path.read_bytes()
    print(path.relative_to(ROOT), hashlib.sha256(path.read_bytes()).hexdigest())
print('Complete exact guard:', first, last, '; original proof lines:',
      len(proof.splitlines()), '; receiver lines:', len(new.splitlines()))
print('Five permanent tag/label pairs; one replacement;', len(defects),
      'defects; one proposed event:', eid)
print('Canonical source and global records unchanged; completed', now)
