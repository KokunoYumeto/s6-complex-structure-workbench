#!/usr/bin/env python3
"""Prepare the fully compared 037J corollary without canonical mutations."""
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / 'agents/continuation6_iii_carriers'
PREFIX = 'S6_SERIES_PUBLISH_III_037J'
LABEL = 'wb:cusp-cone-sharp-global-R4-scope'
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
source_bytes = SOURCE.read_bytes()
assert hashlib.sha256(source_bytes).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
source = source_bytes.decode()
fresh = D / (PREFIX+'_fresh_derivation.md')
FRESH_HASH = 'e1b75c64a53264793030e28fbba0ff4710283b28ea6a9109310140ec10039bc4'
assert hashlib.sha256(fresh.read_bytes()).hexdigest() == FRESH_HASH
statement = (D / (PREFIX+'_released_statement.tex')).read_text()
statement = statement[statement.index('\\begin{corollary}'):].strip()
proof = (D / (PREFIX+'_released_proof.tex')).read_text()
proof = proof[proof.index('\\begin{proof}'):].strip()
assert hashlib.sha256(proof.encode()).hexdigest() == '6c1f8cf5d4a38467b7dd5766fe7654e25b7c73655d3d3548465273229cb7f740'
assert source.count(statement) == source.count(proof) == 1
start = source.index(statement)
pstart = source.index(proof, start+len(statement))
assert not source[start+len(statement):pstart].strip()
old = source[start:pstart+len(proof)]
first = source.count('\n', 0, start)+1
last = source.count('\n', 0, pstart+len(proof))+1
assert (first, last) == (27203, 27246)
assert source.count('\n', 0, pstart)+1 == 27226
receiver = D / (PREFIX+'_receiving.tex')
new = receiver.read_text().strip()
for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{(tag-[^}]+)\}']:
    assert Counter(re.findall(pattern, old)) == Counter(re.findall(pattern, new))
assert '\\StatementRecord' not in new
assert new.count('\\begin{proof}') == 1
assert new.count('\\begin{enumerate}') == 1


def write(path, fields, rows):
    with path.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t',
                                lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


write(D / (PREFIX+'_replacements.tsv'),
      ['statement_id', 'old_text', 'new_text', 'reason'],
      [dict(statement_id=LABEL, old_text=old, new_text=new,
            reason='Exact entire individually released corollary and own proof. '
                   'Full comparison includes all three realizations, compactness, '
                   'every fixed ambient metric, intrinsic diameter divergence, '
                   'the auxiliary vertex local pair, and exact decompactification '
                   'comparison. Stable tag/label preserved; adjacent identities excluded.')])
defects = []


def defect(suffix, kind, before, after, reason):
    assert before in old
    assert not after or after in new
    defects.append(dict(change_id='c6-III-037J-'+suffix, type=kind,
                        statement_id=LABEL,
                        old_location=f'S6_SERIES_PUBLISH_III.tex:{first}-{last}',
                        old_page='', new_location=receiver.relative_to(ROOT).as_posix(),
                        new_page='', old_text=before, new_text=after, reason=reason,
                        review_status='proposed; complete comparison done; root '
                                      'admission and source/page gates pending'))


header = next(line for line in statement.splitlines() if line.startswith('\\StatementRecord'))
defect('header', 'D10', header, '',
       'Remove the machine header while preserving the permanent identity.')
defect('proof-hierarchy', 'D10',
       '\\begin{enumerate}[label={$\\langle1\\rangle$\\arabic*.},leftmargin=*]', '',
       'Replace the generated one-item proof hierarchy by connected proof text. '
       'Retain the genuine three-part statement list.')
defect('metric-maps', 'D20',
       'Their intrinsic diameters tend to infinity because\ntheir intrinsic systoles do.',
       'Transport $d_T$ to each slice by $j_{\\nu,T}$.',
       'Name the physical flat intrinsic metric, induced first-fundamental-form '
       'path metric and restricted ambient distance, then prove their exact '
       'pullback/scaling maps and inclusion inequality. The original physical '
       'diameter divergence is verified by a shortest-period half-vector; no '
       'mathematical conclusion is refuted.')
defect('title', 'D16',
       '\\begin{corollary}[Sharp global meaning of the Euclidean limit]',
       '\\begin{corollary}[Three Euclidean realizations and their exact scope]',
       'Name the three actual realizations and the proved scope in the title; '
       'the permanent tag and label remain unchanged.')
write(D / (PREFIX+'_defects.tsv'), list(defects[0]), defects)
with (ROOT / 'CHECK_EVENTS.tsv').open() as stream:
    fields = next(csv.reader(stream, delimiter='\t'))
now = datetime.now(timezone.utc).isoformat()
eid = 'publish:c6:III:037J:targeted'
row = dict.fromkeys(fields, '')
row.update(statement_id=LABEL, date=now[:10],
           who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately '
               'exposed; sixth-continuation carriers checker',
           type='targeted proof check', event_id=eid,
           phase='fresh derivation followed by individual authorized full comparison',
           outcome='Complete fresh derivation saved and reread '
                   '2026-11-24T13:37:18UTC (SHA256 '+FRESH_HASH+'); root full '
                   'review preceded individual release2026-11-24T13:41:47.060321+00:00. '
                   'Read the entire original corollary, all21 own proof lines and '
                   'full receiver. Checked every quotient and inverse, exact '
                   'source-carrier restriction, intrinsic whole-ball map, zero-fibre '
                   'and beta comparison, all compactness obstructions, local pair '
                   'and Euclidean/half-space maps, every fixed-metric diameter '
                   'bound, physical intrinsic diameter divergence and scale '
                   'relations. Original auxiliary assertions all preserved. The '
                   'half-vector inequality is comparison-stage detail; fresh '
                   'whole-ball isometries already prove diameter divergence. '
                   'No mathematical conclusion refuted. One proposed targeted '
                   'event for037J; source application, unit and page gates open.',
           source_file='S6_SERIES_PUBLISH_III.tex', source_row=str(first),
           source_event_type='targeted proof check', evidence_group=eid,
           publish_input_file=(D / (PREFIX+'_CHECK_EVENTS.tsv')).relative_to(ROOT).as_posix(),
           publish_input_row='2', date_utc=now,
           where='; '.join((D / (PREFIX+'_'+suffix)).relative_to(ROOT).as_posix()
                          for suffix in ['fresh_derivation.md', 'comparison.md', 'replacements.tsv']))
write(D / (PREFIX+'_CHECK_EVENTS.tsv'), fields, [row])
for suffix in ['receiving.tex', 'comparison.md', 'replacements.tsv', 'defects.tsv', 'CHECK_EVENTS.tsv']:
    assert b'\r' not in (D / (PREFIX+'_'+suffix)).read_bytes()
assert SOURCE.read_bytes() == source_bytes
assert hashlib.sha256(fresh.read_bytes()).hexdigest() == FRESH_HASH
print('037J source guard:', first, '-', last, '; original', len(old.splitlines()),
      'lines; receiver', len(new.splitlines()), 'lines; defects', len(defects))
print('Guard SHA256 without terminal LF:', hashlib.sha256(old.encode()).hexdigest())
print('Permanent tag and label preserved; one proposed event:', eid)
print('Canonical source and frozen fresh proof unchanged; LF outputs complete', now)
