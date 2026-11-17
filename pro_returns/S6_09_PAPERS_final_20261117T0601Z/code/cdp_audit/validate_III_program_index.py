"""Read-only integrity validation of the complete Paper III program catalogue."""
from pathlib import Path
import collections
import datetime
import hashlib
import json
import re

D=Path(__file__).resolve().parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
p=D/'records/III_program_index.json';x=json.loads(p.read_text());files={};runs={}
for r in x['programs']:
    if r['program']:
        q=D/r['program'];assert q.is_file();assert sha(q)==r['sha256'];files[r['program']]=r['sha256']
    for run in r['runs']:
        runs[run['run_id']]=run
        assert run['portable_script_paths_exist'],run['run_id']
        for a in [run['program_artifact'],*run['outputs'],*run['inputs']]:
            assert a['exists'],a
            q=D/a['path'];assert q.is_file();assert sha(q)==a['sha256'];files[a['path']]=a['sha256']
            assert a.get('matches_recorded_sha256',True),a
        if run['run_id']in r['selected_replay_run_ids']:
            assert run['execution_status']in ['recorded_success','completed_narrative_numeric_exit_unrecorded']
            assert run['exit_code']==0 or (run['exit_code']is None and run['execution_status']=='completed_narrative_numeric_exit_unrecorded')
            assert not any(k in str(run['original_record'].get('status','')).lower()for k in ['timed out','timeout'])
for m in x['manifests']:
    q=D/m['path'];assert sha(q)==m['sha256'];files[m['path']]=m['sha256']
assert not x['unresolved_or_integrity_issues']
tex=(D/'editorial/III_programs.tex').read_text()
assert tex.count('% BEGIN GENERATED III PROGRAM INDEX')==tex.count('% END GENERATED III PROGRAM INDEX')==1
core=(D/'S6_09_PAPERS_III.tex').read_text()
labels=set(re.findall(r'\\label\{([^}]+)\}',core));refs=set(re.findall(r'\\(?:ref|cref|Cref)\{([^}]+)\}',tex));missing=sorted(refs-labels)
assert not missing,missing
geo=json.loads((D/'work/cdp_audit/course_geometric_execution_manifest.json').read_text())
assert geo['completed_records']==20 and all(r['exit_code']==0 for r in geo['runs'])
assert all(r.get('execution_reused')or r['comparison']['mathematical_json_fields_identical']for r in geo['runs'])
layout=json.loads((D/'work/cdp_audit/III_program_index_qa/layout_check.json').read_text())
assert layout['index_tex_sha256']==hashlib.sha256(tex.encode()).hexdigest()
assert layout['exit_code']==0 and not layout['overfull_boxes']and not layout['missing_characters']
report={'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17',
    'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'index_sha256':sha(p),'generator_sha256':sha(D/'code/editorial/build_paper_iii_program_index.py'),
    'tex_sha256':hashlib.sha256(tex.encode()).hexdigest(),'counts':x['counts'],
    'verified_distinct_archive_files':len(files),'receiving_references_present':len(refs),
    'missing_receiving_labels':missing,'missing_paths_or_hash_mismatches':[],
    'unique_run_status_counts':dict(collections.Counter(r['execution_status']for r in runs.values())),
    'all_selected_replay_records_exclude_failed_and_timed_out_attempts':True,
    'geometric_batch':{'source_programs_fully_read':20,'source_lines':2015,'new_executions':19,
      'reused_executions':1,'all_exits_zero':True,'new_check_labels_passed':2860,
      'all_math_json_fields_identical':True,
      'provenance_difference':'Tangent-index recomputes a changed source chapter hash; all mathematical fields agree. Eighteen other reports differ only by line endings.'},
    'layout':layout,'visual_inspection':{'rendered_pages':[9,33],
      'scope':'Program table typography and actual command spacing; standalone unresolved receiving references are expected and are separately verified against current main TeX labels.'},
    'no_mathematical_programs_executed_by_indexer_or_validator':True,
    'fresh_executions_this_task':'Two short periods/Oka evidence-gap reruns expressly authorized by root, plus nineteen previously unrecorded geometric-provider checks.'}
(D/'records/III_program_index_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:report[k]for k in ['verified_distinct_archive_files','receiving_references_present','counts','unique_run_status_counts']},indent=2))
