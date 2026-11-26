#!/usr/bin/env python3
"""Prepare only the individually compared 038T packet; do not edit source."""
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / 'agents/continuation6_iii_carriers'
PREFIX = 'S6_SERIES_PUBLISH_III_038T'
LABEL = 'wb:cusp-s12-all-higher-smashes-null'
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
source_bytes = SOURCE.read_bytes()
assert hashlib.sha256(source_bytes).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
source = source_bytes.decode()
fresh = D / (PREFIX+'_fresh_derivation.md')
FRESH_HASH = '84a5203f2378c1790f23976adde60165bc4e3662f09fd00a78fd5686aa215d90'
assert hashlib.sha256(fresh.read_bytes()).hexdigest() == FRESH_HASH
statement = (D / (PREFIX+'_released_statement.tex')).read_text()
statement = statement[statement.index('\\begin{corollary}'):].strip()
proof = (D / (PREFIX+'_released_proof.tex')).read_text()
proof = proof[proof.index('\\begin{proof}'):].strip()
assert hashlib.sha256(proof.encode()).hexdigest() == 'd9ff96da46ebb64fa64b50a3bc79078e1ab7c76c44eb3ee1a8093f33e6b81157'
start = source.index(statement)
pstart = source.index(proof, start+len(statement))
assert not source[start+len(statement):pstart].strip()
old = source[start:pstart+len(proof)]
first = source.count('\n', 0, start)+1
last = source.count('\n', 0, pstart+len(proof))+1
assert (first, last) == (27375, 27397)
receiver = D / (PREFIX+'_receiving.tex')
new = receiver.read_text().strip()
for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{(tag-[^}]+)\}']:
    assert Counter(re.findall(pattern, old)) == Counter(re.findall(pattern, new))
assert new.count('\\begin{proof}') == 1
assert '\\StatementRecord' not in new and '\\begin{enumerate}' not in new


def write(path, fields, rows):
    with path.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t',
                                lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


write(D / (PREFIX+'_replacements.tsv'),
      ['statement_id', 'old_text', 'new_text', 'reason'],
      [dict(statement_id=LABEL, old_text=old, new_text=new,
            reason='Exact entire original corollary and its complete own proof; '
                   'full authorized original/fresh/receiver comparison; preserve '
                   'permanent tag and label; following038X/038W scopes excluded.')])
defects = []


def defect(suffix, kind, before, after, reason):
    assert before in old
    assert not after or after in new
    defects.append(dict(change_id='c6-III-038T-'+suffix, type=kind,
                        statement_id=LABEL,
                        old_location=f'S6_SERIES_PUBLISH_III.tex:{first}-{last}',
                        old_page='', new_location=receiver.relative_to(ROOT).as_posix(),
                        new_page='', old_text=before, new_text=after, reason=reason,
                        review_status='proposed; complete comparison done; root '
                                      'admission and source/page gates pending'))


header = next(line for line in statement.splitlines() if line.startswith('\\StatementRecord'))
defect('header', 'D10', header, '', 'Remove the machine header while preserving tag and label.')
defect('enumeration', 'D10',
       '\\begin{enumerate}[label={$\\langle1\\rangle$\\arabic*.},leftmargin=*]', '',
       'Replace the one-item generated hierarchy with connected proof text.')
defect('integer-and-endpoint', 'D26',
       'For every based \\(g:S^6\\to S^3\\) and every \\(r\\geq2\\),',
       'For every continuous based map $g:S^6\\to S^3$ and every integer',
       'Make the integer range explicit. Treat r=2 directly through038V; use the '
       'associativity formula only for r>2, so a zero-fold smash convention is '
       'unnecessary. No original conclusion is refuted.')
write(D / (PREFIX+'_defects.tsv'), list(defects[0]), defects)
with (ROOT / 'CHECK_EVENTS.tsv').open() as stream:
    fields = next(csv.reader(stream, delimiter='\t'))
now = datetime.now(timezone.utc).isoformat()
eid = 'publish:c6:III:038T:targeted'
row = dict.fromkeys(fields, '')
row.update(statement_id=LABEL, date=now[:10],
           who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately '
               'exposed; sixth-continuation carriers checker',
           type='targeted proof check', event_id=eid,
           phase='fresh derivation followed by individual authorized full comparison',
           outcome='Complete fresh derivation saved and reread at 2026-11-24T12:43:40UTC '
                   '(SHA256 '+FRESH_HASH+'); root individual release '
                   '2026-11-24T12:44:08.838090+00:00 followed full review. Read the '
                   'entire original statement, all ten proof lines and complete '
                   'receiving proof. Checked exact ordered cube maps and inverses, '
                   'associativity, all integer cases including r=2, parameterized '
                   'smash quotient descent, every homotopy endpoint and fixed '
                   'basepoint. No theorem refuted. Exactly one proposed targeted '
                   'event for038T; source application, unit criteria and page gates open.',
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
print('038T source guard:', first, '-', last, '; original', len(old.splitlines()),
      'lines; receiver', len(new.splitlines()), 'lines; defects', len(defects))
print('Guard SHA256 without terminal LF:', hashlib.sha256(old.encode()).hexdigest())
print('Permanent tag and label preserved; one proposed event:', eid)
print('Canonical source and frozen fresh proof unchanged; LF outputs complete', now)
