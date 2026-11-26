#!/usr/bin/env python3
"""Prepare only the c7 KU staging packet and validate its exact guard.

The canonical manuscript, global events, global defects and frozen fresh
audit files are read-only inputs. No old KU algorithm is imported.
"""
from __future__ import annotations
import csv
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
STAGE = ROOT / 'agents/continuation7_iii_ku'
PREFIX = 'S6_SERIES_PUBLISH_III_02KU'
ID = 'maps:src:D.2.2'
WHO = ('GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical reasoning effort '
       'not separately exposed; seventh-continuation KU archive check')
NOW = datetime.now(timezone.utc).isoformat()

def digest(data):
    return sha256(data).hexdigest()

def write_tsv(path, fields, rows):
    with path.open('w', newline='', encoding='utf8') as f:
        out = csv.DictWriter(f, fieldnames=fields, delimiter='\t',
                             lineterminator='\n')
        out.writeheader()
        out.writerows(rows)

canonical_bytes = (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes()
assert digest(canonical_bytes) == (
    '9105ab47b763ccba7dc6fdfdeb504e191f171cec35e06d14ec67a9642ee5dca0')
canonical = canonical_bytes.decode('utf8')
release = (STAGE / f'{PREFIX}_released_original.tex').read_text()
start = release.index(r'\begin{computed}')
end = release.index(r'\end{computed}', start) + len(r'\end{computed}')
old = release[start:end]
assert digest(old.encode()) == (
    '453d58f7afbe7a0ee3f6f9fc5a8dcdd6ad47195321e98019879c09e3b2090354')
new_path = STAGE / f'{PREFIX}_receiving.tex'
new = new_path.read_text().rstrip('\n')
assert canonical.count(old) == 1
shadow = canonical.replace(old, new, 1)
assert shadow.count(new) == 1
assert shadow.replace(new, old, 1).encode() == canonical_bytes
old_line = canonical[:canonical.index(old)].count('\n') + 1
assert old_line == 8272
assert old_line + old.count('\n') == 8319

def identities(text):
    return {
        'labels': re.findall(r'\\label\{([^}]+)\}', text),
        'hypertargets': re.findall(r'\\hypertarget\{([^}]+)\}', text),
        'equation_tags': re.findall(r'\\tag\{([^}]+)\}', text),
    }

assert identities(old) == identities(new)
assert identities(new) == {
    'labels': [ID], 'hypertargets': ['tag-02KU'], 'equation_tags': []}

# These lexical checks establish source structure only, not a TeX build.
stack = []
for token in re.finditer(r'\\(begin|end)\{([^}]+)\}', new):
    side, env = token.groups()
    if side == 'begin':
        stack.append(env)
    else:
        assert stack and stack.pop() == env, (side, env)
assert not stack
depth = 0
for i, char in enumerate(new):
    slashes = 0
    j = i - 1
    while j >= 0 and new[j] == '\\':
        slashes += 1
        j -= 1
    if char in '{}' and slashes % 2 == 0:
        depth += 1 if char == '{' else -1
        assert depth >= 0, i
assert depth == 0
math_stack = []
for token in re.findall(r'\\[()\[\]]', new):
    if token in (r'\(', r'\['):
        math_stack.append(token)
    else:
        expected = {r'\)': r'\(', r'\]': r'\['}[token]
        assert math_stack and math_stack.pop() == expected
assert not math_stack
refs = re.findall(r'\\(?:c|C|Series)ref\{([^}]+)\}', new)
labels = set(re.findall(r'\\label\{([^}]+)\}', canonical))
assert set(refs) <= labels
bib = (ROOT / 'S6_SERIES_PUBLISH_references.bib').read_text()
keys = set(re.findall(r'@\w+\s*\{\s*([^,\s]+)', bib))
cites = re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}', new)
assert set(cites) <= keys
for forbidden in (r'\StatementRecord', r'\CompendiumRef', r'\path',
                  '.json', '.csv', 'API', 'code/', 'asked for in D.2',
                  'a02f2eacf5a8c3db7cf8cdfcdba50c0002ee91c7'):
    assert forbidden not in new, forbidden

frozen = {
    STAGE / f'{PREFIX}_fresh_derivation.md':
    '9760a76042b595bbda8033782598bff9ffe747d72126541046fa8520e1e0a9e7',
    ROOT / 'code/S6_SERIES_PUBLISH_c7_ku_archive_audit.py':
    'b509b1036d6d2ff845096e61c3d6c338c0c8139ada795a25fa1405a5b82efd2a',
    ROOT / 'code/S6_SERIES_PUBLISH_c7_ku_archive_audit.out':
    'a0d8200cfb9086c5a1429c6984e45e0d8eeafda6bf2edbf0ce196d6db219706d',
}
for path, expected in frozen.items():
    assert digest(path.read_bytes()) == expected, path

replacements_path = STAGE / f'{PREFIX}_replacements.tsv'
write_tsv(replacements_path, ['statement_id', 'old_text', 'new_text'],
          [dict(statement_id=ID, old_text=old, new_text=new)])

def part(text, start, end):
    a = text.index(start)
    b = text.index(end, a) + len(end)
    return text[a:b]

scope = part(new, 'Consider the integral-cohomology', '{manExplorer26}.')
coverage = part(new, 'Reading these fields and applying',
                'coverage of the stated choices.')
groups = part(new, 'The degree-i output consists',
              'the integral universal coefficient sequence.')
defects = []

def defect(kind, suffix, before, after, reason):
    assert before in old, (kind, suffix, before)
    assert not after or after in new, (kind, suffix, after)
    line = old_line + old[:old.index(before)].count('\n')
    defects.append(dict(
        change_id=f'c7-III-02KU-{suffix}', type=kind, statement_id=ID,
        old_location=f'S6_SERIES_PUBLISH_III.tex:{line}', old_page='',
        new_location=str(new_path.relative_to(ROOT)),
        new_page='pending final typeset page concordance',
        old_text=before, new_text=after, reason=reason,
        review_status=('staged; root admission, source application and '
                       'final page review pending')))

defect('D01', 'execution-history',
       part(old, 'This is an audit of the retained requests and responses.',
            'This is the stated bounded archive audit.'), '',
       'Remove former execution, timeout and writing-history narration. '
       'The current pre-exposure proof and computation independently audit '
       'the raw records; they make no new remote run and do not reverify '
       'the unopened historical programs. The complete comparison preserves '
       'the precise status of each historical assertion.')
defect('D02', 'defensive-scope',
       part(old, 'We therefore do not promote this',
            'nor into the unbounded classification asked for in D.2.'), scope,
       'State the bounded marked-model output scope positively once at the '
       'start, preserving its mathematical limits.')
defect('D05', 'internal-request-reference',
       'nor into the unbounded classification asked for in D.2.', '',
       'The internal request reference has no role in the finite computation; '
       'its complete parameter set is now explicit in the statement and proof.')
defect('D06', 'catalogue-reference',
       r'\CompendiumRef{III}{maps:src:D.2.1}',
       part(new, 'Use the marked Mordell--Weil generator G', r'\end{center}'),
       'The canonical paper has no local maps:src:D.2.1 label. Print the '
       'exact 21 configurations and n data as the finite-input definition, '
       'as authorized by root. No extra catalogue theorem, permanent alias '
       'or topological validation claim is added.')
defect('D08', 'process-opening',
       part(old, 'Fifty specified inputs were evaluated', r'\cite{manExplorer26}.'),
       scope,
       'Express the object of the computation as the marked-model group '
       'outputs. The later sentence retains the exact fifty-input cardinality.')
defect('D09', 'program-and-summary-paths',
       part(old, 'The executable is', 'and the individual raw responses.'), '',
       'Move the historical executable and CSV/JSON bookkeeping out of the '
       'proof. The current independently written audit and full output are '
       'identified in the comparison for the later programs/records table. '
       'The old program and excluded summaries are not newly verified.')
defect('D09', 'old-audit-path',
       r'\path{code/III/audit_explorer_archive.py}', '',
       'Remove the older audit-program path from the mathematical proof; '
       'the complete historical comparison gives it no new execution credit.')
defect('D10', 'machine-header',
       r'\StatementRecord{maps:src:D.2.2}{proved}{02KU}{\SeriesRef{mapsD:repair:collision-realization}; \cite{manExplorer26}}',
       r'\textnormal{\small tag 02KU.}',
       'Preserve the label and hypertarget, print only the small permanent '
       'tag, and retain both mathematical dependencies at their exact scope '
       'in the receiving statement and proof.')
defect('D11', 'repeated-scope-paragraph',
       part(old, 'The proposition here concerns the executed computation,',
            'nor into the unbounded classification asked for in D.2.'), scope,
       'The model-output scope appears once at the beginning. The source '
       'documentation reading and unpublished-model limitation remain fully '
       'recorded in the comparison and source verification note.')
defect('D12', 'repeated-audit-assertion',
       part(old, 'For the archived computation, all fifty exact request payloads and',
            'comparisons were checked as well.'), coverage,
       'Replace repeated audit-result narration with one complete finite '
       'coverage proof, one group classification and the exact four clutch '
       'pairs. All eight clutch response results are preserved.')
defect('D16', 'mathematical-title',
       '[as a bounded exact computation]',
       '[Integral cohomology of a finite filling family]',
       'Give the computed result a mathematical title; its bounded scope '
       'remains in the statement itself.')
defect('D18', 'documentation-locator',
       r'\cite{manExplorer26}',
       r"\cite[documentation, ``How it works'']{manExplorer26}",
       'Add the exact primary documentation locus reopened and fully read '
       'in this continuation. Stage the existing bibliography key update '
       'with retrieval date, page hash and precise evidence scope.')

defect_fields = ['change_id','type','statement_id','old_location','old_page',
                 'new_location','new_page','old_text','new_text','reason',
                 'review_status']
write_tsv(STAGE / f'{PREFIX}_defects.tsv', defect_fields, defects)

event_fields = ['statement_id','date','who','type','outcome','event_id',
                'phase','source_file','source_row','source_event_type',
                'evidence_group','publish_input_file','publish_input_row',
                'date_utc','where']
events_path = STAGE / f'{PREFIX}_CHECK_EVENTS.tsv'
fresh_time = '2026-11-24T21:01:14.805542+00:00'
evidence = 'publish:c7:III:02KU:fresh-archive-audit'
events = []

def event(kind, suffix, outcome, source, phase, stamp, group):
    events.append(dict(
        statement_id=ID, date='2026-11-24', who=WHO, type=kind,
        outcome=outcome, event_id=f'publish:c7:III:02KU:{suffix}',
        phase=phase, source_file=source, source_row='1',
        source_event_type=kind, evidence_group=group,
        publish_input_file=str(events_path.relative_to(ROOT)),
        publish_input_row=str(len(events)+2), date_utc=stamp,
        where=('agents/continuation7_iii_ku/' + PREFIX + '_comparison.md; '
               'agents/continuation7_iii_ku/' + PREFIX + '_receiving.tex')))

event('targeted proof check', 'fresh-bounded-derivation',
      'Before original-proof exposure, derived the finite input product '
      'from the 21-profile claim-only catalogue, the exact monodromy-power '
      'orders, and the explicit marked-to-catalogue occurrence permutation '
      'with inverse. Proved bijective coverage of all 50 exact marked inputs, '
      'classified the reported integral groups and fundamental-group '
      'recognitions as 24 trivial, 21 infinite cyclic and five finite cyclic '
      'outputs, and obtained precisely the three asserted integral sphere '
      'patterns. For all eight supplementary clutch records, proved the '
      'four literal input translations by the fourth ambient basis vector '
      'and their inverses, with identical local-model dictionaries. The '
      'scope is the frozen archived outputs, without new remote execution '
      'or an independent proof of unpublished local cochain models. Root '
      'read the entire frozen derivation before releasing the original.',
      'agents/continuation7_iii_ku/' + PREFIX + '_fresh_derivation.md',
      'before whole original KU exposure; fresh bounded archive check',
      fresh_time, evidence)
event('computation or formal certificate', 'fresh-exact-archive-program',
      'New standard-library program, importing no prior KU algorithm, '
      'generated the expected 50-input set from the claim-only catalogue '
      'and audited every field used in its classification in all 58 raw '
      'records. Exact rational logarithmic vectors, weights, occurrence '
      'permutations, local families and multiplicities, degree-by-degree '
      'ranks and torsion, labels, Euler sums, duality/UCT consistency and '
      'recognition flags all passed. The complete output lists all 50 '
      'integral group sequences and all eight clutch results, and was read '
      'in full by checker and root. This certifies the bounded archive '
      'audit, not a rerun of the remote cochain engine or old programs. '
      'Shared evidence with the fresh targeted derivation, not a second '
      'independent engine computation.',
      'code/S6_SERIES_PUBLISH_c7_ku_archive_audit.py',
      'before whole original KU exposure; fresh bounded archive check',
      fresh_time, evidence)
event('used and rechecked in this run', 'complete-original-comparison',
      'After release at 2026-11-24T21:04:10.461485+00:00, read the entire '
      'argument-bearing original environment and compared every statement, '
      'auxiliary assertion and historical execution/rerunning/audit claim '
      'with the frozen fresh proof. The bounded 50-input result and all '
      'eight clutch records agree. Historical timeout and unopened old '
      'program assertions are removed from the mathematical text without '
      'new execution credit. The exact primary Explorer documentation was '
      'reopened and read completely. The admitted 02OG statement was read '
      'and invoked precisely for OS50/II and OS56/II. Tag and label are '
      'preserved; one unique whole-environment guard is reversible in '
      'memory. No new D25/D26/D27 finding, TeX build or page-reading credit '
      'is asserted.',
      'agents/continuation7_iii_ku/' + PREFIX + '_comparison.md',
      'after whole original KU exposure; full receiving-proof comparison',
      NOW, 'publish:c7:III:02KU:complete-original-comparison')
write_tsv(events_path, event_fields, events)

print('KU packet validation: PASS')
print('Canonical manuscript unchanged:', digest(canonical_bytes))
print('Guard: one complete original environment, exact lines 8272--8319; unique.')
print('In-memory replacement and inverse recover every original byte: PASS')
print('Permanent identities:', identities(new))
print('Environment, brace and inline/display delimiter balance: PASS')
print('Resolved reference targets:', sorted(set(refs)))
print('Resolved citation keys:', sorted(set(cites)))
print('Receiver workflow/file/protocol residue checks: PASS')
print('Frozen pre-exposure derivation, program and complete output hashes: unchanged.')
print('Staged replacements:', 1, 'events:', len(events), 'defect rows:', len(defects))
print('New mathematical refutations/refinements: none.')
print('TeX build/page review: not claimed; configured pdflatex format was unavailable.')
for suffix in ('receiving.tex','comparison.md','references.bib','replacements.tsv',
               'CHECK_EVENTS.tsv','defects.tsv'):
    path = STAGE / f'{PREFIX}_{suffix}'
    data = path.read_bytes()
    assert b'\r' not in data
    print(path.name, digest(data))
assert (ROOT / 'S6_SERIES_PUBLISH_III.tex').read_bytes() == canonical_bytes
for path, expected in frozen.items():
    assert digest(path.read_bytes()) == expected
print('Canonical and frozen inputs remain byte-identical after packet generation.')
