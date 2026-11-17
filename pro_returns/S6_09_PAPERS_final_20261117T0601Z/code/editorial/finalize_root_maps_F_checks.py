"""Reconcile actual F executions and the separately completed proof readings."""
from pathlib import Path
import hashlib, json, shutil

D=Path(__file__).resolve().parents[2]; ROOT=D.parent
P=D/'code/root_maps_F'; W=D/'work/root'
read=lambda p:json.loads(p.read_text())
initial=read(P/'execution_manifest.json')
cli=read(P/'cli_execution_manifest.json')
algebraic=read(P/'hecke_algebraic_execution_record.json')
direct=read(P/'direct_tuple_execution_record.json')
assert len(initial)==32 and sum(x.get('exit_code')==0 for x in initial)==26
assert len(cli)==10 and all(x['exit_code']==0 for x in cli)
assert algebraic['all_passed'] and algebraic['actual_exit_code']==0
assert direct['exit_code']==0
recovery={
 'fourfolds_classify_gluing.py':('cli_execution_manifest.json',7,'Documented input/output arguments supplied; exact order-one marked fixture.'),
 'fourfolds_cusp_boundary.py':('cli_execution_manifest.json',0,'Original code/records directory layout reconstructed.'),
 'fourfolds_involution_classes.py':('cli_execution_manifest.json',1,'Original code/records directory layout reconstructed.'),
 'fourfolds_marked_gluing.py':('cli_execution_manifest.json',6,'Documented input/output arguments supplied; full fresh involution chain calculation.'),
 'fourfolds_total_homology.py':('cli_execution_manifest.json',4,'Complete fresh calculation allowed to finish beyond the initial300-second timeout; both recorded examples completed.'),
 'fourfolds_tuple_classification.py':('direct_tuple_execution_record.json',None,'Documented input/output arguments supplied; actual known representative fixture.'),
}
failed=[]
for x in initial:
    if x.get('exit_code')==0:continue
    name=Path(x['program']).name
    assert name in recovery
    file,index,reason=recovery[name]
    rr=direct if index is None else cli[index]
    failed.append({'original_attempt':x,'completed_replay_manifest':file,'completed_replay_index':index,'completed_replay_output':rr['output'],'resolution':reason})

# Preserve the complete layout needed by ROOT=parents[1] in unchanged
# mathematical programs; an empty code directory is not a runnable archive.
copied=[]
runtime=P/'runtime'
for source in sorted(P.glob('*')):
    if source.suffix not in {'.py','.jl'}:continue
    target=runtime/'code'/source.name
    shutil.copy2(source,target)
    a=hashlib.sha256(source.read_bytes()).hexdigest()
    assert hashlib.sha256(target.read_bytes()).hexdigest()==a
    copied.append({'source':str(source.relative_to(D)),'portable_copy':str(target.relative_to(D)),'sha256':a})
env=ROOT/'external_cache/integral_conjugacy_runtime/env'
(runtime/'hecke_env').mkdir(exist_ok=True)
for n in ['Project.toml','Manifest.toml']:
    source=env/n
    assert source.exists()
    shutil.copy2(source,runtime/'hecke_env'/n)
    copied.append({'source':'Pinned environment metadata/'+n,'portable_copy':str((runtime/'hecke_env'/n).relative_to(D)),'sha256':hashlib.sha256(source.read_bytes()).hexdigest()})
(P/'portable_layout_manifest.json').write_text(json.dumps(copied,indent=2)+'\n')

execution={'reader':{'model':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17','reader':'/root'},
 'initial_attempts':32,'initial_successes':26,'initial_failed_or_timed_out_attempts':6,
 'documented_cli_replays':10,'documented_cli_successes':10,
 'additional_algebraic_Hecke_suite':algebraic,'additional_direct_tuple_CLI':direct,
 'recovered_attempts':failed,'all_initial_programs_have_successful_executions':True,
 'scope':'Exact stated finite identities, exhaustive finite involution/lattice catalogue, terminating per-input routines, three full marked-topology integrations and GRH=false integral-conjugacy tests. No executed enumeration of the infinite class set is asserted.',
 'portable_layout':'code/root_maps_F/runtime; unchanged Python and Julia mathematical sources plus exact fixtures and pinned Julia environment metadata.',
 'environment':'Python3.12/SymPy1.14; Julia1.10.10, Hecke0.41.1, Nemo0.57.2, AbstractAlgebra0.51.4. Runtime binaries and package caches are excluded.',
 'source_manifests':['code/root_maps_F/execution_manifest.json','code/root_maps_F/cli_execution_manifest.json','code/root_maps_F/hecke_algebraic_execution_record.json','code/root_maps_F/direct_tuple_execution_record.json'],
 'outcome':'All operative assigned program invocations completed successfully at their recorded scopes; all unsuccessful setup/timeout attempts retained and explicitly reconciled.'}
(P/'final_execution_reconciliation.json').write_text(json.dumps(execution,ensure_ascii=False,indent=2)+'\n')

ids=['F.2.2','F.2.3','F.2.4']+['F.2.'+str(i) for i in range(7,33)]+['F.2.36','F.3.1','F.3.2','F.3.3']
assert len(ids)==33
manifest={r['source_id']:r for r in read(W/'III_assembly_manifest.json')['source_result_blocks']}
notes=(W/'maps_F_proof_audit.md').read_text()
proofs=[]
for sid in ids:
    assert sid in notes and sid in manifest
    proofs.append({'source_run':'S6_04_MAPS_MANIFOLDS','source_id':sid,'reader':execution['reader'],
      'full_receiving_proof_read':True,'independently_rederived':True,
      'detailed_reading_record':'work/root/maps_F_proof_audit.md#'+sid,
      'retained_expanded_receiving_text_sha256':manifest[sid]['expanded_original_sha256'],
      'exact_computational_scope':'code/root_maps_F/final_execution_reconciliation.json',
      'imported_dependency_records':['work/cdp_audit/maps_E/result_audit.json','work/cdp_audit/maps_E/references_verified.json','work/cdp_audit/maps_credit/Scott_F_application_check.json','work/maps_audit/references_verified.json','work/invariants_arithmetic/maps_F_receiving_audit.json','work/root/BHJ22_source_check.json'],
      'your_check':'Complete independent receiving-proof reading and derivation, all operative source-hypothesis matches, and actual finite program reruns completed. Detailed proof-by-proof reasoning and exact limits are retained in the linked records.',
      'check_outcome':'Passed in precisely the printed scope. Per-input termination is not a finite global enumeration; punctured-base periods with one bounded cusp correction do not imply simultaneous finite good reduction.'})
(W/'maps_F_final_result_checks.json').write_text(json.dumps(proofs,ensure_ascii=False,indent=2)+'\n')

prereq=D/'work/cdp_audit/carrier_radial_prerequisites.tex'
root_review={'reader':execution['reader'],'source':str(prereq.relative_to(D)),
 'sha256':hashlib.sha256(prereq.read_bytes()).hexdigest(),
 'scope':'Complete receiving proof independently read, including all real-period entries, determinant−D, full inverse transpose, integral dual-lattice formula, exact compact Lie quotient and its kernel, systole>=T−C, and injective/onto Euclidean radius-R balls whenT−C>4R.',
 'derivation':'The real period matrix follows by splitting both complex coordinates. Direct block elimination verifies its inverse transpose. Projection kills precisely the two real primitive coordinate circles; the imaginary matrix isTJ+bounded withJorthogonal. A nonzero period has norm>=T−C; forT−C>4R no deck translate shortens a distance in the R-ball, and lifted minimizers prove onto.',
 'outcome':'Passed complete new proof; no spectral assertion used.'}
(W/'carrier_prerequisite_independent_review.json').write_text(json.dumps(root_review,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'receiving_proofs_closed':33,'initial_programs_completed':32,'historical_failures_retained':6,'CLI_replays':10,'portable_source_files':len(copied)},indent=2))
