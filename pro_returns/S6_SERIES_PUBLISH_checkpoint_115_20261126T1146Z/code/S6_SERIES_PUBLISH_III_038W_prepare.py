#!/usr/bin/env python3
"""Prepare the fully compared 038W paragraph packet; do not edit source."""
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / 'agents/continuation6_iii_carriers'
PREFIX = 'S6_SERIES_PUBLISH_III_038W'
LABEL = 'wb:cusp-s12-nullity-scope'
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
source_bytes = SOURCE.read_bytes()
assert hashlib.sha256(source_bytes).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
source = source_bytes.decode()
fresh = D / (PREFIX+'_fresh_derivation.md')
FRESH_HASH = '254418b31bbdb4f89a39412ac57b785b101803d56e7939f0ff6ba8f38bbae48a'
assert hashlib.sha256(fresh.read_bytes()).hexdigest() == FRESH_HASH
released = (D / (PREFIX+'_released_proof.tex')).read_text()
old = released[released.index('\\paragraph{Scope}'):].strip()
assert hashlib.sha256(old.encode()).hexdigest() == '93ec40ef5adf0893c2c2834de2bf8658c8f2fcbd057132f397a012c29b6ed206'
assert source.count(old) == 1
start = source.index(old)
first = source.count('\n', 0, start)+1
last = source.count('\n', 0, start+len(old))+1
assert (first, last) == (27453, 27463)
receiver = D / (PREFIX+'_receiving.tex')
new = receiver.read_text().strip()
for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{(tag-[^}]+)\}']:
    assert Counter(re.findall(pattern, old)) == Counter(re.findall(pattern, new))
assert '\\StatementRecord' not in new


def write(path, fields, rows):
    with path.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t',
                                lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


write(D / (PREFIX+'_replacements.tsv'),
      ['statement_id', 'old_text', 'new_text', 'reason'],
      [dict(statement_id=LABEL, old_text=old, new_text=new,
            reason='Exact entire individually released Scope paragraph; complete '
                   'original/fresh/receiver comparison; exact postcomposition '
                   'and nonzero kernel proof, both metric families checked; '
                   'preserve permanent tag and label; adjacent identities excluded.')])
defects = []


def defect(suffix, kind, before, after, reason):
    assert before in old
    assert not after or after in new
    defects.append(dict(change_id='c6-III-038W-'+suffix, type=kind,
                        statement_id=LABEL,
                        old_location=f'S6_SERIES_PUBLISH_III.tex:{first}-{last}',
                        old_page='', new_location=receiver.relative_to(ROOT).as_posix(),
                        new_page='', old_text=before, new_text=after, reason=reason,
                        review_status='proposed; complete comparison done; root '
                                      'admission and source/page gates pending'))


header = next(line for line in old.splitlines() if line.startswith('\\StatementRecord'))
defect('header', 'D10', header, '', 'Remove the machine header while preserving tag and label.')
defect('scope-map', 'D26',
       'it does not imply null-homotopy of the earlier\nconical-target map',
       'This homomorphism has a nonzero kernel in the indicated dimension.',
       'The original gives no proof of the inference scope. Construct exact P and Q, '
       'prove P_*[Q]=0, and prove noninjectivity of that same P_* on pi12 by a '
       'retraction-detected nonzero kernel class. No unsupported assertion about '
       'native Q or an identification with the kernel witness is retained.')
defect('initial-map-compatibility', 'D26',
       'The theorem changes no point-set or metric statement.',
       'The same initial maps retain the point-set and metric properties',
       'Identify both moving four-sphere families, exact quotient restrictions, '
       'whole-ball isometries and inverses with the initial maps of the based '
       'homotopies. No claim about quotient or metric properties at intermediate '
       'homotopy times is made.')
write(D / (PREFIX+'_defects.tsv'), list(defects[0]), defects)
with (ROOT / 'CHECK_EVENTS.tsv').open() as stream:
    fields = next(csv.reader(stream, delimiter='\t'))
now = datetime.now(timezone.utc).isoformat()
eid = 'publish:c6:III:038W:targeted'
row = dict.fromkeys(fields, '')
row.update(statement_id=LABEL, date=now[:10],
           who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately '
               'exposed; sixth-continuation carriers checker',
           type='targeted proof check', event_id=eid,
           phase='fresh derivation followed by individual authorized full comparison',
           outcome='Complete fresh derivation saved and reread before '
                   '2026-11-24T12:55:01UTC (SHA256 '+FRESH_HASH+'); root review '
                   'record12:56:54UTC and individual release '
                   '2026-11-24T12:57:10.537998+00:00. Read all eleven original '
                   'paragraph lines and entire receiver. Checked exact conical '
                   'and sphere maps, quotient and inverse maps, based homotopy '
                   'retracts, full cellular matrix, all dimensions and endpoints, '
                   'nonzero kernel in pi12, and both moving-four-sphere initial '
                   'metric maps. No assertion about native Q beyond P_*[Q]=0. '
                   'Hatcher Cor4.33 full proof read before release. One proposed '
                   'targeted event for038W; source application, unit/page gates open.',
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
print('038W source guard:', first, '-', last, '; original', len(old.splitlines()),
      'lines; receiver', len(new.splitlines()), 'lines; defects', len(defects))
print('Guard SHA256 without terminal LF:', hashlib.sha256(old.encode()).hexdigest())
print('Permanent tag and label preserved; one proposed event:', eid)
print('Canonical source and frozen fresh proof unchanged; LF outputs complete', now)
