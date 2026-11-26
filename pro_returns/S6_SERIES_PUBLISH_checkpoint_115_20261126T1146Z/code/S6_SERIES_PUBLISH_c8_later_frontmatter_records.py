"""Finalize exact local front-matter edit statuses and exposed-reading events."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import csv

ROOT = Path(__file__).resolve().parents[1]
UNIT = ROOT / 'agents/continuation8_iii_integration/units/root/front_matter.tex'
LOCAL = ROOT / 'agents/continuation8_iii_later'
DEFECTS = LOCAL / 'S6_SERIES_PUBLISH_III_frontmatter_publication_defects.tsv'
EVENTS = LOCAL / 'S6_SERIES_PUBLISH_III_frontmatter_publication_CHECK_EVENTS.tsv'
REVIEW = LOCAL / 'S6_SERIES_PUBLISH_III_frontmatter_publication_review.md'
EXPECTED = '80fbc1d2a7678a4499960a08aad1c24b75b25cb843a590869e5cb6cb67659c1c'
assert sha256(UNIT.read_bytes()).hexdigest() == EXPECTED
source = UNIT.read_text()
with DEFECTS.open(newline='') as stream:
    reader = csv.DictReader(stream, delimiter='\t')
    fields = reader.fieldnames
    rows = list(reader)
status = ('Whole 600-line input, complete semantic edit program and all 761 final lines read; '
          'exact old/new blocks read at those occurrences and all row metadata read back; '
          'exposed source-local publication comparison only. Final counts, three-way provenance, '
          'reference expansion, actual placement, bibliography and PDF gates remain root-owned.')
with DEFECTS.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    for row in rows:
        row['review_status'] = status
        writer.writerow(row)

now = datetime.now(timezone.utc).isoformat()
who = 'GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed'
event_fields = ['statement_id','date','who','type','outcome','event_id','phase',
                'source_file','source_row','source_event_type','evidence_group',
                'publish_input_file','publish_input_row','date_utc','where']
scope = {
 'series:III:A': 'Full headline and four-step outline compared with complete J3 proof: original-sphere domain, exact based collapse/product homotopy, exterior agreement and designated-solid-torus zero image.',
 'series:III:B': 'Full headline and seven-step outline compared with complete J4/J5/J6 proofs: ordered framing, 6 nu-prime and 12 nu, real Adams value, compatible divisor frames, M and inverse, G and explicit homotopy. Actual intermediate factorization repaired; root owns the J6 admissible-sphere scope clarification.',
 'series:III:C': 'Full headline and seven-step outline compared with Q021 and the read retained-frame/J7 premises, full J8/J9 unit and exact cell statement/input: full defined sphere-map domain and separate p=-1 zero-drift cell-count datum.',
 'series:III:D': 'Full headline and five-step outline compared with the whole K2-K6 unit: absolute N^3 map, relative N^2 map, all endpoints, two obstruction scopes, global finite-flat degree N^2|G_N| and additional singular cusp component.',
 'series:III:E': 'Full headline and six-step outline compared with full current Q146/K9 proof and recorded bounded group/product premises: complete marked invariant, canonical M_d realization, prime-to-six domain and exact classification source scope.',
 'series:III:F': 'Full headline and seven-step outline compared with full L3 and SA proofs and exact current LP/LV/SB data/statements: 59/50 natural patterns, all weighted d, fixed OS45 parity/linking, complete free OS49 sector including n=0 and (9,3,1). No new SB refutation.',
 'series:III:G': 'Full headline and five-step outline compared with the admitted whole conifold review and newly read current M0/M1/M2 premises: fixed parameters, directed line, proper flat node family, primitive surgery map, oriented S3xS3 and algebraic dimension one.',
 'sec:results': 'Whole title, abstract and six introductory subsections compared with the complete controlling prompt: all original identifiers, evidenced provenance, exact sole records/commit macro uses, descriptive further results and actual approved body-order dependencies. Final event totals and joint provenance gates explicitly retained.'
}
with EVENTS.open('w', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=event_fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    for index, (label, outcome) in enumerate(scope.items(), 2):
        line = source[:source.index('\\label{' + label + '}')].count('\n') + 1
        row = dict(statement_id=label, date=now[:10], who=who,
                   type='used and rechecked in this run',
                   outcome=outcome + ' Exposed publication reading; no independent, blind or new required-check credit; no final PDF/reference/placement credit.',
                   event_id='publish:c8:III:frontmatter:' + label.replace(':','-'),
                   phase='continuation8-frontmatter-publication',
                   source_file=str(UNIT.relative_to(ROOT)), source_row=line,
                   source_event_type='used and rechecked in this run',
                   evidence_group='publish:c8:III:frontmatter-publication',
                   publish_input_file=str(EVENTS.relative_to(ROOT)), publish_input_row=index,
                   date_utc=now, where=str(REVIEW.relative_to(ROOT)))
        writer.writerow(row)

for path in (DEFECTS, EVENTS, REVIEW):
    assert b'\r' not in path.read_bytes(), path
print('COMPLETED_UTC', now)
print('SOURCE', len(source.splitlines()), EXPECTED)
for row in rows:
    print('EDIT', row['change_id'], row['type'], row['statement_id'],
          row['old_location'], row['old_page'], row['new_location'], row['new_page'],
          'OLD_CHARS', len(row['old_text']), 'NEW_CHARS', len(row['new_text']),
          'REASON', row['reason'])
print('ALL_EDIT_STATUSES', status)
with EVENTS.open() as stream:
    print(stream.read(), end='')
for number, line in enumerate(source.splitlines(), 1):
    if line.startswith('\\subsection{'):
        print('ACTUAL_SUBSECTION', number, line)
print('NEW_TAGS', 0, 'CANONICAL_WRITES', 0, 'DERIVED_WRITES', 0,
      'INDEPENDENT_CREDIT', 0, 'NEW_REQUIRED_CHECK_CREDIT', 0)
