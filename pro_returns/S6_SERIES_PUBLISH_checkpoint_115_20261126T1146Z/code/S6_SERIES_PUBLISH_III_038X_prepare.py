#!/usr/bin/env python3
"""Prepare the fully compared 038X paragraph; never edit canonical files."""
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / 'agents/continuation6_iii_carriers'
PREFIX = 'S6_SERIES_PUBLISH_III_038X'
LABEL = 'wb:cusp-s12-one-copy-invariant'
SOURCE = ROOT / 'S6_SERIES_PUBLISH_III.tex'
source_bytes = SOURCE.read_bytes()
assert hashlib.sha256(source_bytes).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
source = source_bytes.decode()
fresh = D / (PREFIX+'_fresh_derivation.md')
FRESH_HASH = '62d2cc0fa88dc529afd03bf852d6ae69d4599c223ea8eecfaa5af61664fd0eba'
assert hashlib.sha256(fresh.read_bytes()).hexdigest() == FRESH_HASH
released = (D / (PREFIX+'_released_proof.tex')).read_text()
old = released[released.index('\\paragraph{The one-copy invariant'):].strip()
assert hashlib.sha256(old.encode()).hexdigest() == '694f598f66a66ebadf93566de988ff61f3d485ff8bdfb552549d6ab9e395e6ba'
assert source.count(old) == 1
start = source.index(old)
first = source.count('\n', 0, start)+1
last = source.count('\n', 0, start+len(old))+1
assert (first, last) == (27400, 27446)
receiver = D / (PREFIX+'_receiving.tex')
new = receiver.read_text().strip()
for pattern in [r'\\label\{([^}]+)\}', r'\\hypertarget\{(tag-[^}]+)\}']:
    assert Counter(re.findall(pattern, old)) == Counter(re.findall(pattern, new))
assert '\\StatementRecord' not in new
assert new.count('\\begin{equation}') == 2
bib = (D / (PREFIX+'_bibliography_additions.tex')).read_text()
keys = re.findall(r'\\bibitem\{([^}]+)\}', bib)
assert keys == ['CuspInvariantHatcherVB', 'CuspInvariantBaues1998']
assert all('{'+key+'}' in new for key in keys)
assert all('\\bibitem{'+key+'}' not in source for key in keys)


def write(path, fields, rows):
    with path.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t',
                                lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


write(D / (PREFIX+'_replacements.tsv'),
      ['statement_id', 'old_text', 'new_text', 'reason'],
      [dict(statement_id=LABEL, old_text=old, new_text=new,
            reason='Exact entire individually released invariant paragraph; full '
                   'original/fresh/receiver comparison of every claim, including '
                   'the framing-dependence example. Preserve038X/Y/Z and labels. '
                   'Fixed nu9 retained with exact inverse-unit twist. Adjacent '
                   'identities excluded. Two bibliography additions separately proposed.')])
defects = []


def defect(suffix, kind, before, after, reason):
    assert before in old
    assert not after or after in new
    defects.append(dict(change_id='c6-III-038X-'+suffix, type=kind,
                        statement_id=LABEL,
                        old_location=f'S6_SERIES_PUBLISH_III.tex:{first}-{last}',
                        old_page='', new_location=receiver.relative_to(ROOT).as_posix(),
                        new_page='', old_text=before, new_text=after, reason=reason,
                        review_status='proposed; complete comparison done; root '
                                      'admission and source/bibliography/page gates pending'))


header = next(line for line in old.splitlines() if line.startswith('\\StatementRecord'))
defect('header', 'D10', header, '',
       'Remove the machine header while preserving all three permanent tags and labels.')
defect('suspension-source', 'D18',
       "Toda's suspension calculation\nidentifies",
       'The suspension calculation in',
       'Use the directly opened Hatcher statement and initial suspension maps with '
       'precise locators. No claim of reading a further unlocated Toda calculation '
       'is made. New Hatcher VB and published Baues entries are separately proposed '
       'for the explicit framing witness; no copied primary-source bytes are packaged.')
defect('coefficient-isomorphism', 'D20',
       'Thus the one-copy class and its sixfold suspension are the\nsame integer modulo \\(12\\).',
       'has inverse $[a]_{12}\\mapsto a\\gamma$.',
       'Give the exact E6 group map, even-image inverse, coefficient homomorphism '
       'and inverse a->a gamma. Retain the fixed nu9 and prove all inverse '
       'identities and nullity equivalences rather than identifying coordinates implicitly.')
defect('ordered-framing', 'D26',
       'After choosing a smooth chart in the open\ntarget cell, the differential of \\(g\\) supplies its normal three-framing.',
       'The inverse differential of the ordered coordinates $(r,c_1,c_2)$',
       'Specify the actual ordered target chart, inverse normal derivative, '
       'complement homotopy, relative based smoothing, and left/right suspended '
       'normal directions through the exact source and target maps.')
defect('framing-dependence-witness', 'D26',
       'The unframed diffeomorphism type \\(T^3\\), point-set surjectivity,\nand the zero ordinary homology map do not compute \\(a\\).',
       'two maps with this same embedded regular fibre and coefficients',
       'Supply the missing exact example: same embedded T3 and basepoint, '
       'bounding tau0 and supported tau0 theta^-1; explicit PT difference '
       'kJ(Ad), inverse-unit degree k for fixed nu9, coefficients0/1, identical '
       'surjectivity and ordinary homology data. Native g remains coefficient0.')
write(D / (PREFIX+'_defects.tsv'), list(defects[0]), defects)
with (ROOT / 'CHECK_EVENTS.tsv').open() as stream:
    fields = next(csv.reader(stream, delimiter='\t'))
now = datetime.now(timezone.utc).isoformat()
eid = 'publish:c6:III:038X:targeted'
row = dict.fromkeys(fields, '')
row.update(statement_id=LABEL, date=now[:10],
           who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately '
               'exposed; sixth-continuation carriers checker',
           type='targeted proof check', event_id=eid,
           phase='fresh derivation followed by individual authorized full comparison',
           outcome='Complete fresh derivation saved and reread at '
                   '2026-11-24T13:13:33UTC (SHA256 '+FRESH_HASH+'); root review '
                   'record13:15:54UTC and individual release '
                   '2026-11-24T13:16:21.624394+00:00. Read all47 original paragraph '
                   'lines and the full receiver, including every auxiliary and final '
                   'framing-dependence assertion. Checked exact suspension quotient '
                   'and inverse, all ranges and coefficient conventions, complete '
                   'torus parametrization/inverse, ordered PT normal frames, explicit '
                   'same-embedded-T3 framing difference via J, and inverse-unit '
                   'twist for coefficients0/1 with fixed nu9. Every source reading '
                   'scope stated truthfully; new programs/outputs fully read and '
                   'first structural equality failure preserved. No mathematical '
                   'conclusion refuted. One proposed targeted event for038X; source '
                   'application, bibliography insertion, unit/page gates open.',
           source_file='S6_SERIES_PUBLISH_III.tex', source_row=str(first),
           source_event_type='targeted proof check', evidence_group=eid,
           publish_input_file=(D / (PREFIX+'_CHECK_EVENTS.tsv')).relative_to(ROOT).as_posix(),
           publish_input_row='2', date_utc=now,
           where='; '.join((D / (PREFIX+'_'+suffix)).relative_to(ROOT).as_posix()
                          for suffix in ['fresh_derivation.md', 'comparison.md',
                                         'replacements.tsv', 'primary_reading.md']))
write(D / (PREFIX+'_CHECK_EVENTS.tsv'), fields, [row])
for suffix in ['receiving.tex', 'comparison.md', 'replacements.tsv', 'defects.tsv',
               'CHECK_EVENTS.tsv', 'bibliography_additions.tex']:
    assert b'\r' not in (D / (PREFIX+'_'+suffix)).read_bytes()
assert SOURCE.read_bytes() == source_bytes
assert hashlib.sha256(fresh.read_bytes()).hexdigest() == FRESH_HASH
print('038X source guard:', first, '-', last, '; original', len(old.splitlines()),
      'lines; receiver', len(new.splitlines()), 'lines; defects', len(defects))
print('Guard SHA256 without terminal LF:', hashlib.sha256(old.encode()).hexdigest())
print('All038X/Y/Z tags and labels preserved; one proposed event:', eid)
print('Two new bibliography entries proposed:', keys)
print('Canonical source and frozen fresh proof unchanged; LF outputs complete', now)
