#!/usr/bin/env python3
"""Prepare only 02KR's reviewed packet; do not mutate any global record."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import csv
import io
import re

root = Path(__file__).resolve().parents[1]
old_dir = root / 'agents/continuation6_iii_root'
folder = root / 'agents/continuation7_iii_kr'
prefix = 'S6_SERIES_PUBLISH_III_02KR_'
statement_id = 'maps:src:D.2.17'
folder.mkdir(exist_ok=True)


def write_tsv(path, columns, rows):
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, columns, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(out.getvalue(), newline='\n')


def release_body(name):
    lines = (old_dir / (prefix + name)).read_text().splitlines()
    assert all(x.startswith('%') for x in lines[:4])
    return '\n'.join(lines[4:]).rstrip('\n')


old_statement = release_body('released_statement.tex')
old_proof = release_body('released_proof.tex')
source_bytes = (root / 'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert sha256(source_bytes).hexdigest() == '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0'
source = source_bytes.decode()
assert source.count(old_statement) == source.count(old_proof) == 1
first = source.index(old_statement)
proof_first = source.index(old_proof, first + len(old_statement))
gap = source[first + len(old_statement):proof_first]
assert gap == '\n\n\n'
old = old_statement + gap + old_proof
assert source.count(old) == 1
start = source[:first].count('\n') + 1
end = source[:first + len(old)].count('\n') + 1
assert (start, end) == (11076, 11179)
assert sha256(old_proof.encode()).hexdigest() == 'd697f6761f16fe21a459b33e5256dd6829243a60f33c8e81b2db1f491f5d0dc2'
assert sha256((old_dir / (prefix + 'fresh_derivation.md')).read_bytes()).hexdigest() == '9aefcc70677fa2cdc3566fcecc1266ddddb2ea1677b19d65f9007ffc5e70121a'

previous_receiver = (old_dir / (prefix + 'receiving.tex')).read_text().rstrip('\n')
citation_changes = [
    (r'\cite[\S2.2 and Proposition 3.5(1),(3)]{manUU21}',
     r'\cite[\S2.4, (2.2), p.~6; Proposition 3.5(1),(3), pp.~8--10]{manUU21}'),
    (r'\cite[\S\S7.6--7.7]{manSS10}', r'\cite[\S7.6, pp.~33--34]{manSS10}'),
    (r'\cite[Theorem 6.8]{manSS10}', r'\cite[Theorem 6.8, p.~26]{manSS10}'),
    (r'\cite[Theorem B(b)]{manBarden65}',
     r'\cite[Theorem B(b), pp.~367--368]{manBarden65}'),
    ("Barden's oriented linking-coordinate map gives", 
     "Barden's oriented linking-coordinate map\n"
     r'\cite[Lemma F, p.~372; Theorem 2.2, p.~376]{manBarden65} gives'),
    (r'\cite[Theorem B(2), Proposition 5.6]{manGR25}',
     r'\cite[Theorem B(2), p.~3; Proposition 5.6(1), pp.~22--23]{manGR25}'),
]
receiver = previous_receiver
for old_cite, new_cite in citation_changes:
    assert receiver.count(old_cite) == 1
    receiver = receiver.replace(old_cite, new_cite)

for pattern in (r'\\label\{([^}]+)\}', r'\\hypertarget\{([^}]+)\}', r'\\tag\{([^}]+)\}'):
    assert sorted(re.findall(pattern, old)) == sorted(re.findall(pattern, receiver))
assert re.findall(r'\\label\{([^}]+)\}', receiver) == [statement_id]
assert re.findall(r'\\hypertarget\{([^}]+)\}', receiver) == ['tag-02KR']
assert receiver.count(r'\begin{proof}') == receiver.count(r'\end{proof}') == 1
assert receiver.count(r'\begin{corollary}') == receiver.count(r'\end{corollary}') == 1
assert r'\StatementRecord' not in receiver and 'manifolds\\_star\\_additive.py' not in receiver
assert receiver.count(r'\[') == receiver.count(r'\]')
envs = []
for match in re.finditer(r'\\(begin|end)\{([^}]+)\}', receiver):
    direction, env = match.groups()
    if direction == 'begin':
        envs.append(env)
    else:
        assert envs.pop() == env
assert not envs
depth = 0
for match in re.finditer(r'(?<!\\)[{}]', receiver):
    depth += 1 if match.group() == '{' else -1
    assert depth >= 0
assert depth == 0

receiving_path = folder / (prefix + 'receiving.tex')
receiving_path.write_text(receiver + '\n', newline='\n')
write_tsv(folder / (prefix + 'replacements.tsv'),
          ['statement_id', 'old_text', 'new_text', 'reason'], [{
    'statement_id': statement_id, 'old_text': old, 'new_text': receiver,
    'reason': ('Exact individually released corollary and own proof, source lines 11076--11179, '
               'with three-LF statement/proof gap. Every original auxiliary claim is compared; '
               'all parameters, group formulas and oriented conclusions stand. Complete actual '
               'additive-cap and transfer maps replace abbreviated arguments; direct framed '
               'reconstruction proves the unstabilized type. Historical execution sentence '
               'removed; exact primary locators supplied. The permanent label/target are preserved. '
               'Canonical application and unit/page gates remain separate.')
}])

defect_fields = ['change_id', 'type', 'statement_id', 'old_location', 'old_page',
                 'new_location', 'new_page', 'old_text', 'new_text', 'reason', 'review_status']
defects = []


def defect(suffix, kind, before, after, reason, staged=False):
    reference = previous_receiver if staged else old
    assert before in reference
    assert not after or after in receiver
    location = ('agents/continuation6_iii_root/' + prefix + 'receiving.tex'
                if staged else 'S6_SERIES_PUBLISH_III.tex')
    line = reference[:reference.index(before)].count('\n') + (1 if staged else start)
    defects.append(dict(zip(defect_fields, [
        'c7-III-02KR-' + suffix, kind, statement_id, location + ':' + str(line), '',
        str(receiving_path.relative_to(root)), '', before, after, reason,
        'complete checker comparison; root admission, canonical application and final page review pending'
    ])))


defect('header', 'D10',
       next(x for x in old_statement.splitlines() if x.startswith(r'\StatementRecord')), '',
       'Remove the machine header and move dependency citations to their mathematical applications.')
defect('hierarchy', 'D10', r'\begin{enumerate}[label={$\langle1\rangle$\arabic*.},leftmargin=*]', '',
       'Replace generated proof hierarchy by one connected proof; the complete six original items are compared.')
defect('title', 'D23', r'\begin{corollary}[two further original additive profiles]',
       r'\begin{corollary}[Two further original additive profiles]',
       'Capitalize the mathematical title with identical parameter scope.')
items = old_proof.split('\\item ')[1:]
assert len(items) == 6
items[-1] = items[-1].split(r'\end{enumerate}')[0]
items = [x.rstrip('\n') for x in items]
headings = [r'\emph{The actual marking and the line.}',
            r'\emph{The two original additive neighbourhoods.}',
            r'\emph{The complete exterior and regular log.}',
            r'\emph{The oriented reconstruction and its auxiliary surgery.}']
section_bounds = [receiver.index(h) for h in headings] + [receiver.rindex(r'\end{proof}')]
sections = [receiver[section_bounds[i]:section_bounds[i+1]].rstrip('\n') for i in range(4)]
defect('marking-and-line', 'D22', items[0], sections[0],
       'State the actual primitive-cycle and section-cocycle maps, component residues, height calculation '
       'and exact integral four-period lifts that identify these profiles with their claimed inputs.')
defect('original-caps', 'D22', items[1], sections[1],
       'Give the original-neighbourhood retraction, logarithm/torsion translation, mapping-torus sign map, '
       'physical-line gauge and full invariant/coinvariant maps instead of an abbreviated verbatim application.')
defect('boundary-and-meridian', 'D22', items[2], sections[1],
       'Give exact local specialization rows and sections, saturated fixed loops, complete boundary map '
       'and the coefficient-one relative meridian generator; every original value is verified unchanged.')
defect('whole-transfer', 'D22', items[3], sections[2],
       'Give the full graph and fibre inverse maps, complete normal transfer, exact source relation, '
       'fourteen-dimensional degree-one map, both zero-n lifts and duality coordinates for all groups.')
defect('direct-framed-reconstruction', 'D22', items[4], sections[3],
       'Prove the same oriented type by the explicit unstabilized framed reconstruction, controlling '
       'the full free Euler class; retain and check canonical triviality and projectable-spin surgery. '
       'No claim that a cancellation theorem is false is made.')
defect('historical-program', 'D09', items[5], '',
       'Remove historical program path and execution counts from the proof. The historical execution '
       'claim was not verified; unrestricted mathematics and separately recorded new computations support the result.')
for i, (before, after) in enumerate(citation_changes, 1):
    defect('receiver-locator-' + str(i), 'D18', before, after,
           ('Correct staged receiver local-log citation to Ulmer--Urzua section 2.4, equation (2.2), p.6; '
            'the primary source was reopened at the exact locus.' if i == 1 else
            'Supply the exact reopened primary statement/section and printed pages for this application.'), staged=True)
write_tsv(folder / (prefix + 'defects.tsv'), defect_fields, defects)

with (root / 'CHECK_EVENTS.tsv').open(newline='') as f:
    event_fields = csv.DictReader(f, delimiter='\t').fieldnames
now = datetime.now(timezone.utc)
event_id = 'publish:c7:III:02KR:targeted'
row = {k: '' for k in event_fields}
row.update({
    'statement_id': statement_id, 'date': now.date().isoformat(),
    'who': ('GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; '
            'sixth-continuation root fresh derivation and seventh-continuation 02KR comparison checker'),
    'type': 'targeted proof check',
    'outcome': ('Completes the frozen 944-line fresh derivation written and fully read before individual '
                'original release at 2026-11-24T16:55:27.031815+00:00, with full original and receiving '
                'comparison in continuation seven. Both original additive profiles, every free regular '
                'log, all integral groups including n=0, exact simple connectivity, both oriented signs, '
                'even m and m=1 agree. Every auxiliary original assertion is checked, including the '
                'coefficient-one relative meridian, the full primitive graph/transfer maps, canonical '
                'line, null fixed sphere and projectable spin surgery. Explicit framed reconstruction '
                'proves the same unstabilized type and replaces the unspecific cancellation invocation. '
                'New post-exposure Bareiss/Gaussian arithmetic checks literal receiver constants and '
                'the symbolic full transfer; thirty parameter/profile minor evaluations are arithmetic '
                'checks only. Staged UU locator corrected from section 2.2 to section 2.4, equation '
                '(2.2), p.6. Historical 1462/194 execution claim unverified and removed from the proof. '
                'No new D25/D26 or statement refutation is confirmed. This is one targeted sequence, '
                'not a new blind proof by the exposed c7 checker; root admission and source/unit/page '
                'gates remain pending.'),
    'event_id': event_id,
    'phase': 'frozen fresh derivation followed by individually authorized full original and receiving comparison',
    'source_file': 'S6_SERIES_PUBLISH_III.tex', 'source_row': '11076',
    'source_event_type': 'targeted proof check', 'evidence_group': event_id,
    'publish_input_file': str((folder / (prefix + 'CHECK_EVENTS.tsv')).relative_to(root)),
    'publish_input_row': '2', 'date_utc': now.isoformat(),
    'where': '; '.join(str(p.relative_to(root)) for p in [
        old_dir / (prefix + 'fresh_derivation.md'), old_dir / (prefix + 'fresh_root_review.md'),
        old_dir / (prefix + 'released_statement.tex'), old_dir / (prefix + 'released_proof.tex'),
        old_dir / (prefix + 'fresh_arithmetic.py'), old_dir / (prefix + 'fresh_arithmetic.out'),
        old_dir / (prefix + 'log_transfer.py'), old_dir / (prefix + 'log_transfer.out'),
        old_dir / (prefix + 'post_exposure.py'), old_dir / (prefix + 'post_exposure.out'),
        folder / (prefix + 'comparison.md'), folder / (prefix + 'auxiliary_review.md'),
        folder / (prefix + 'primary_reading.md'), receiving_path,
        folder / (prefix + 'replacements.tsv'), folder / (prefix + 'defects.tsv'),
        root / 'code/S6_SERIES_PUBLISH_c7_kr_review_arithmetic.py',
        root / 'code/S6_SERIES_PUBLISH_c7_kr_review_arithmetic.out'
    ]),
})
assert set(row) == set(event_fields)
write_tsv(folder / (prefix + 'CHECK_EVENTS.tsv'), event_fields, [row])

with (folder / (prefix + 'replacements.tsv')).open(newline='') as f:
    guard = next(csv.DictReader(f, delimiter='\t'))
assert source.count(guard['old_text']) == 1 and guard['new_text'] == receiver
assert (root / 'S6_SERIES_PUBLISH_III.tex').read_bytes() == source_bytes
print('PASS: exact released source guard lines 11076--11179; one permanent label/target preserved.')
print('PASS: one corollary/proof; balanced braces, environments and display delimiters.')
print('Prepared', len(defects), 'defect rows and one proposed targeted event; global records and manuscript unchanged.')
