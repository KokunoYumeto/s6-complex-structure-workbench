"""Record one reviewed obstruction and its new common defect criterion."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import io
import json

ROOT = Path(__file__).resolve().parents[1]
NOW = datetime.now(timezone.utc).isoformat()
EVIDENCE = 'agents/continuation7_iii_root/S6_SERIES_PUBLISH_III_02KS_cube_review.md'

def read(name, delimiter='\t'):
    with (ROOT / name).open(newline='') as stream:
        reader = csv.DictReader(stream, delimiter=delimiter)
        return reader.fieldnames, list(reader)

def write(name, fields, rows, delimiter='\t'):
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fields, delimiter=delimiter, lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    (ROOT / name).write_text(stream.getvalue(), newline='\n')

assert (ROOT / EVIDENCE).is_file()
fields, defects = read('S6_DEFECT_REGISTER.csv', ',')
assert not any(r['type_id'] == 'D27' for r in defects)
defects.append({
    'type_id': 'D27', 'class': 'statement',
    'defect': 'A claimed smooth identification contradicted by a preserved integral invariant',
    'what_it_looks_like': 'A statement identifies the constructed manifold with a smooth target whose integral cohomology products or characteristic invariants are incompatible under the induced isomorphism.',
    'places_found_in_V': 'Paper III, maps:src:D.2.18 (02KS), display D.V3 (026B/maps:eq:D.V3); the column name is inherited from the common register.',
    'examples_in_V_page_quote': 'D.V3 claims #^3(S2 x S4)#(S3 x S3)#twisted-suspension(N_m). An embedded cusp divisor has normal square6 and integral cube6. Every degree-two class on that target has square0. Diffeomorphism pullback and its orientation degree contradict the identification. No current printed-page claim is made.',
    'search_words': 'Read the complete smooth identification and its integral invariant maps; no token-only completion criterion.',
    'required_fix': 'Refute the affected conclusion by the exact preserved invariant and morphism, derive and verify a correct replacement in its full scope, compare every use, preserve permanent labels, and review the receiving proof. Apply this criterion to all five papers at their authorized stages without assuming other instances.',
    'priority': 'blocks publication',
})
write('S6_DEFECT_REGISTER.csv', fields, defects, ',')

fields, applications = read('S6_SERIES_PUBLISH_new_defect_applications.tsv')
for paper in ['I', 'II', 'III', 'IV', 'V']:
    applications.append({
        'defect_type': 'D27', 'paper': paper,
        'stage': 'current III unit review' if paper == 'III' else
                 'IV unit review after III' if paper == 'IV' else 'five-together review',
        'status': 'open', 'date_utc': NOW, 'evidence': EVIDENCE + '; S6_DEFECT_REGISTER.csv D27',
        'detail': 'Apply the exact smooth-identification invariant criterion unit by unit at this authorized stage. This open application claims no other found instance or paper reading; I, II and V retain their closed gates until the joint step.',
    })
write('S6_SERIES_PUBLISH_new_defect_applications.tsv', fields, applications)

fields, units = read('S6_SERIES_PUBLISH_unit_progress.tsv')
unique = {(r['paper'], r['unit_id'], r['unit_title']) for r in units if r['paper'] in {'III', 'IV'}}
for paper, unit_id, title in sorted(unique):
    units.append({'paper': paper, 'unit_id': unit_id, 'unit_title': title,
                  'row_kind': 'defect', 'defect_type': 'D27', 'status': 'open',
                  'date_utc': NOW, 'evidence': EVIDENCE,
                  'detail': 'New common D27 criterion; this unit has not yet received its full smooth-identification invariant review. No closure from adding the row.'})
write('S6_SERIES_PUBLISH_unit_progress.tsv', fields, units)

fields, events = read('CHECK_EVENTS.tsv')
event_id = 'publish:c7:III:02KS:divisor-cube-countercheck'
assert not any(r['event_id'] == event_id for r in events)
event = {f: '' for f in fields}
event.update(statement_id='maps:src:D.2.18', date=NOW[:10],
    who='GPT-6 Astra (OpenAI), ChatGPT Pro mode; numerical effort not separately exposed; root full narrow countercheck',
    type='targeted proof check',
    outcome='Root read the complete fresh geometric divisor counterexample, raw fixture, independent arithmetic/output, continuation-seven refinement, and new verifier/output. The actual lattice <(3,0),(4,1)> embeds each dP6 component. The unit-preserving Cartier normal map and Thom identity give an integral cube6. Exact suspension Mayer--Vietoris and connected-sum relative cocycle maps give square0 for every degree-two target class. Diffeomorphism pullback and orientation degree contradict D.V3 in either orientation; m=1,v=gamma is an allowed simply connected counterexample. The original proof remains closed to the fresh checker. This narrow result confirms D27 and does not admit the replacement, close 02KS, or supply unit/build/page credit. The intake logical check retains its narrower scope.',
    event_id=event_id, phase='root full review of the fresh geometric obstruction before original release',
    source_file='S6_SERIES_PUBLISH_III.tex', source_row='11213', source_event_type='targeted proof check',
    evidence_group=event_id, publish_input_file=EVIDENCE, publish_input_row='', date_utc=NOW,
    where=EVIDENCE + '; agents/continuation6_iii_carriers/S6_SERIES_PUBLISH_III_02KS_fresh_derivation.md; agents/continuation6_iii_carriers/S6_SERIES_PUBLISH_III_02KS_raw_definitions.json; code/S6_SERIES_PUBLISH_III_02KS_fresh_arithmetic.py; code/S6_SERIES_PUBLISH_III_02KS_fresh_arithmetic.out; agents/continuation7_iii_ks/S6_SERIES_PUBLISH_III_02KS_c7_fresh_derivation.md; code/S6_SERIES_PUBLISH_c7_ks_integral.py; code/S6_SERIES_PUBLISH_c7_ks_integral.out')
events.append(event)
write('CHECK_EVENTS.tsv', fields, events)

fields, required = read('S6_SERIES_PUBLISH_required_progress_III.tsv')
row = next(r for r in required if r['tag'] == '02KS')
assert row['status'] == 'open' and row['proof_status'] == 'embargoed'
row['notes'] += ' Root accepted the actual divisor-cube refutation of D.V3 in ' + EVIDENCE + '; event ' + event_id + '. D27 added to the common register. Full refinement and original comparison pending; no closure.'
row['assigned_checker'] = 'continuation7_iii_ks'
row['unresolved_inputs'] = 'Fresh refinement written; root reviewing the actual original-star model transport and primary recognition scope before individual release.'
write('S6_SERIES_PUBLISH_required_progress_III.tsv', fields, required)

summary = {'recorded_utc': NOW, 'event_id': event_id, 'defect_type': 'D27',
           'new_unit_criteria': len(unique),
           'open_unit_criteria': {p: sum(r['paper'] == p and r['status'] != 'done' for r in units) for p in ['III', 'IV']},
           'required_row_closed': False}
result = json.dumps(summary, indent=2) + '\n'
(ROOT / 'code/S6_SERIES_PUBLISH_c7_ks_cube_record.out').write_text(result, newline='\n')
print(result, end='')
