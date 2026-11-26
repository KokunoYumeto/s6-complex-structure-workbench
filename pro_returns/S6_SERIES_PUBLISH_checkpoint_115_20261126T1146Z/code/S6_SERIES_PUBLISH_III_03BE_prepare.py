#!/usr/bin/env python3
"""Prepare the single 03BE comparison event and exact receiving guard."""
from pathlib import Path
import csv
import hashlib
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / 'agents/continuation6_iii_carriers'
P = 'S6_SERIES_PUBLISH_III_03BE'
LABEL = 'wb:h24:ret:q2-detected-quotient'
source_path = ROOT / 'S6_SERIES_PUBLISH_III.tex'
source_bytes = source_path.read_bytes()
assert hashlib.sha256(source_bytes).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
source = source_bytes.decode()
statement = (D / f'{P}_released_statement.tex').read_text()
statement = statement[statement.index('\\begin{corollary}'):].strip()
proof = (D / f'{P}_released_proof.tex').read_text()
proof = proof[proof.index('\\begin{proof}'):].strip()
assert hashlib.sha256(proof.encode()).hexdigest() == '9aa7d1505dfa0937ebb8e8edd57dc2e1f48b2772b58b4426a3c08cea083d6ad2'
assert hashlib.sha256((D / f'{P}_fresh_derivation.md').read_bytes()).hexdigest() == '989faac973a638cadd3b7146d3d4b3a465f2184b9b30d8c8231a76f81b43062b'
begin = source.index(statement)
proof_begin = source.index(proof, begin+len(statement))
assert not source[begin+len(statement):proof_begin].strip()
old = source[begin:proof_begin+len(proof)]
new_path = D / f'{P}_receiving.tex'
new = new_path.read_text().strip()
assert new.count('\\label{' + LABEL + '}') == 1
assert new.count('\\hypertarget{tag-03BE}{}') == 1
assert '\\StatementRecord' not in new
first = source.count('\n', 0, begin)+1
last = source.count('\n', 0, proof_begin+len(proof))+1
now = datetime.now(timezone.utc).isoformat()


def write(path, fields, rows):
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


write(D / f'{P}_replacements.tsv', ['statement_id', 'old_text', 'new_text', 'reason'],
      [dict(statement_id=LABEL, old_text=old, new_text=new,
            reason='Exact individual corollary and complete proof. Retain the '
                   'native pointed maps and every mathematical conclusion; '
                   'give the induced quotient map and its inverse explicitly, '
                   'remove the machine header, one-item enumeration and '
                   'repeated scope disclaimers. Fresh derivation preceded '
                   'individual release and full comparison.')])

defs = []


def defect(suffix, kind, before, after, why):
    assert before in old
    assert not after or after in new
    defs.append(dict(change_id='c6-III-03BE-'+suffix, type=kind,
                     statement_id=LABEL,
                     old_location=f'S6_SERIES_PUBLISH_III.tex:{first}-{last}',
                     old_page='', new_location=new_path.relative_to(ROOT).as_posix(),
                     new_page='', old_text=before, new_text=after, reason=why,
                     review_status='proposed; full original/receiving comparison '
                                   'done; root admission and final page review pending'))


header = next(line for line in statement.splitlines() if line.startswith('\\StatementRecord'))
defect('header', 'D10', header, '', 'Remove the machine record; preserve tag and label.')
defect('enumeration', 'D10',
       '\\begin{enumerate}[label={$\\langle1\\rangle$\\arabic*.},leftmargin=*]', '',
       'Write the proof as connected mathematical prose; the original has one item.')
defect('title', 'D16', statement.splitlines()[0], new.splitlines()[0],
       'Use a short mathematical title with the same detected quotient.')
defect('scope', 'D11',
       '; this calculation does not determine\nthat order or assert a splitting of the displayed quotient.', '.',
       'Keep the exact positive order and quotient assertions; the displayed inverse '
       'is explicitly a map into G/K. The check file verifies the limited '
       'consequences using concrete quotient diagrams.')
defect('proof-scope', 'D11',
       'These arguments prove all the assertions without inferring\nthe exact order of \\(\\alpha\\).', '',
       'Finish with the proved annihilator-parity statement, without repeating '
       'a limitation already reflected in the precise conclusion.')
write(D / f'{P}_defects.tsv', list(defs[0]), defs)

fields = next(csv.reader((ROOT / 'CHECK_EVENTS.tsv').open(), delimiter='\t'))
event_id = 'publish:c6:III:03BE:targeted'
row = dict.fromkeys(fields, '')
row.update(statement_id=LABEL, date=now[:10],
           who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not '
               'separately exposed; sixth-continuation carriers checker',
           type='targeted proof check',
           outcome='Fresh derivation completed 2026-11-24T11:26:34+00:00 '
                   '(SHA256 989faac973a638cadd3b7146d3d4b3a465f2184b9b30d8c8231a76f81b43062b) '
                   'before individual proof release 2026-11-24T11:30:17.546855+00:00. '
                   'Read the entire original statement, all 17 proof lines and '
                   'the complete receiving corollary/proof. The induced '
                   'postcomposition homomorphism, native H=p3q2 identity, '
                   'detected generator, quotient map and explicit inverse, '
                   'all signed odd multiples and every annihilator parity '
                   'agree. Concrete finite and infinite quotient examples '
                   'verify the calculation scope without identifying them '
                   'with the native group. No theorem refuted and no '
                   'separate computation event. Source application and '
                   'unit/page gates remain open.',
           event_id=event_id, phase='fresh derivation followed by authorized full original/receiving comparison',
           source_file='S6_SERIES_PUBLISH_III.tex', source_row=str(first),
           source_event_type='targeted proof check', evidence_group=event_id,
           publish_input_file=(D / f'{P}_CHECK_EVENTS.tsv').relative_to(ROOT).as_posix(),
           publish_input_row='2', date_utc=now,
           where='; '.join([(D / f'{P}_{suffix}').relative_to(ROOT).as_posix()
                            for suffix in ['fresh_derivation.md', 'comparison.md', 'replacements.tsv']]))
write(D / f'{P}_CHECK_EVENTS.tsv', fields, [row])
assert source_path.read_bytes() == source_bytes
print('03BE:', first, '-', last, ';', len(old.splitlines()), 'original lines;',
      len(new.splitlines()), 'receiving lines;', len(defs), 'defect rows; one proposed targeted check')
print('Source unchanged; exact replacement and all proposed rows prepared', now)
