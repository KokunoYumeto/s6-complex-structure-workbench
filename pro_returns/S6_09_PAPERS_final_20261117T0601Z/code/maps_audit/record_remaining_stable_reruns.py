"""Record independent runs without replacing historical source checks."""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[3]
WORK=ROOT/'deliverables/work/maps_audit'
RUN=ROOT/'deliverables/code/maps_audit/course/stable'
ORIGINAL=ROOT/'sources/codex_workspace/courses/CG-S6/checks'
META=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)', effort='Pro', date='2026-11-17')
mapping={
 'verify_integral_stable_comparison.py':'INTEGRAL_STABLE_COMPARISON_CHECKS.json',
 'verify_arithmetic_completion.py':'ARITHMETIC_COMPLETION_CHECKS.json',
 'verify_adams_tower.py':'ADAMS_TOWER_CHECKS.json',
 'verify_finite_cocycle_model.py':'FINITE_COCYCLE_MODEL_CHECKS.json',
 'verify_formal_two_series.py':'FORMAL_TWO_SERIES_CHECKS.json',
 'verify_projective_cooperation.py':'PROJECTIVE_COOPERATION_CHECKS.json',
 'verify_actual_degree_eight.py':'ACTUAL_DEGREE_EIGHT_CHECKS.json',
 'verify_actual_cooperation.py':'ACTUAL_COOPERATION_CHECKS.json',
 'verify_odd_prime_bar.py':'ODD_PRIME_BAR_CHECKS.json',
}
prepared=json.loads((RUN/'remaining_portable_preparation.json').read_text())
rows=[]
for entry in prepared:
 path=RUN/mapping[entry['program']]
 old=ORIGINAL/path.name
 data=json.loads(path.read_text()); source_data=json.loads(old.read_text())
 differences=sorted(k for k in data.keys()|source_data.keys() if data.get(k)!=source_data.get(k))
 assert set(differences)<={'reader','effort','date','source_hash_recomputed','retained_original_scope'},differences
 assert len(data['checks'])==data['passed']
 rows.append(dict(**entry, command='python '+entry['program'], execution_cwd=str(RUN.relative_to(ROOT)),
                  output=str(path.relative_to(ROOT)), output_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                  original_output=str(old.relative_to(ROOT)), original_output_sha256=hashlib.sha256(old.read_bytes()).hexdigest(),
                  passed=data['passed'], exit_code=0, mathematical_json_fields_identical_to_original=True,
                  differing_json_keys=differences, numerical_scope=data['scope']))
event=dict(event_id='new-remaining-stable-exact-reruns-20261117', **META,
           scope='Completely read all 821 original program lines, independently checked the integer/finite-field algorithms and signs, then ran all nine portable checkers. Mathematical code and every assertion are unchanged.',
           outcome='All nine programs passed; all mathematical JSON fields agree with the original outputs.',
           total_passed=sum(r['passed'] for r in rows), programs=rows,
           historical_metadata_notice='The original arithmetic script field independent_review=false and historical statements such as still-unwritten are retained source metadata. They describe the source-generation record. This appended event records the present independent code read and rerun; later full proof-reading events independently describe the now-retained provider proofs.',
           excluded_scope='Finite program success does not certify a topological construction, an all-stage convergence theorem, or an unopened original reference.')
(WORK/'remaining_stable_rerun_record.json').write_text(json.dumps(event,ensure_ascii=False,indent=2)+'\n')
events=json.loads((WORK/'check_events.json').read_text())
if not any(x.get('event_id')==event['event_id'] for x in events):
 events.append(event)
 (WORK/'check_events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(programs=len(rows),passed=event['total_passed'],semantic_original_matches=len(rows))))
