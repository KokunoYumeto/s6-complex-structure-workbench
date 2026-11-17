"""Retain and run the newly audited geometric-course finite checkers unchanged.

Only the 19 previously unrecorded checks are run.  The twentieth assigned
script, verify_almost_complex.py, reuses its existing documented execution.
The exact source chapter inputs are retained so source-dependent assertions
and recomputed hashes remain operative without any program modification.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import ast
import datetime
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[3]
D=ROOT/'deliverables'
SRC=ROOT/'sources/codex_workspace/courses/CG-S6'
DEST=D/'code/cdp_audit/course_geometric'
MANIFEST=D/'work/cdp_audit/course_geometric_execution_manifest.json'
NAMES='verify_framed_six_obstruction verify_receiving_whitney verify_higher_slides verify_middle_realization verify_morse_cancellation verify_spin_six verify_pontryagin_thom verify_relative_morse verify_handle_rearrangement verify_zero_top_handles verify_morse_trajectories verify_belt_complements verify_whitney_move verify_handle_chains verify_handle_pair_creation verify_framed_slides verify_smooth_duality verify_integral_duality verify_tangent_index verify_almost_complex'.split()
META={'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17','timezone':'UTC','agent':'/root/cdp_audit'}
NOTES={
'verify_framed_six_obstruction':'Exact quaternion norm/reflection and graph-frame matrices; all binary quadratic forms in genera 0–3, zero-line reductions and bounded belt sums; symbolic full local-singularity, double-point, collar and divided-difference identities. No geometric nullbordism or smooth-recognition conclusion follows solely from these checks.',
'verify_receiving_whitney':'Symbolic quaternion multiplication and Spin(4) lifts, exact nonorthogonal metric/corner frames in the three listed receiving dimensions, complete cutoff and flow derivatives, and the explicitly stated meeting-time examples. Does not certify global disk existence or the supported Whitney move.',
'verify_higher_slides':'Alternating prism boundary and time-first orientation through simplex degree 6; full symbolic crossing/shear matrices in indices 2–5; the two integer chain examples, five slide multiplicities and one graded chain-homotopy correction. The geometric slide and singular-homology proof are separate.',
'verify_middle_realization':'Seven dimension/index choices with all coordinates, scales, Hessians, inverses and transported fields; seam and variable-roof identities; two level dimensions, exact collar germs and complete worked chain examples. Does not establish global embedding, compactness or Morse realization.',
'verify_morse_cancellation':'Complete symbolic supported derivatives including the variable-radius term; one variable block completion, six rational parameter-box minima and six explicit unsafe-cutoff counterexamples; exact bump and derivative-gap formulas. Global flow and cancellation are proved separately.',
'verify_spin_six':'All 15 Lie algebra generators in the six-dimensional real exterior-square representation, four central scalars, exact Euler/Chern polynomials, original orientations, stable inverse maps and complexification inverse. Does not certify the family index or global homotopy argument.',
'verify_pontryagin_thom':'Full symbolic stereographic and radial derivatives in the stated dimensions, exact sheared-circle frame, complete six-dimensional exercise matrices and inverse composites, explicit homotopy endpoints/midpoint, suspension chart and stabilization. Does not prove tube existence, global relative regularity or the bordism theorem.',
'verify_relative_morse':'Exact jet determinant, noncommuting congruence velocity, hitting times and their derivatives; full handle embeddings at every index in dimensions 6 and 7, seam/corner/collar formulas, and eight source-bound exercise-domain checks. The actual chapter input is retained and parsed; those eight checks are not skipped.',
'verify_handle_rearrangement':'Full rounded-boundary and seam derivatives, radial determinant identities through normal dimension 7, all allowed core/belt index inequalities in dimensions 6 and 7, mixed collar inverse and seven explicit sorting interchanges. Does not certify the geometric interchange theorem.',
'verify_zero_top_handles':'Exact index-one flow and supported cancellation derivatives, the complete incidence matrix including its loop and integral kernel, all Hessian/permutation signs for dimensions 6 and 7 including extreme indices, and the stated seven-coefficient reversal. Does not establish the component-graph or cancellation proof.',
'verify_morse_trajectories':'Complete holonomy and time-column inverses, ellipsoid/hitting-time formulas, six cutoff derivatives and Hessian, exact rational bump/level gaps, and all mixed metric terms in the stated example. Global trajectory existence and critical-value lowering are separate arguments.',
'verify_belt_complements':'Exact collar maps and both tangent inverse composites, rank-one determinant identities in dimensions 2–4, full disk jet and double-point minors, stated dimension inequalities, quaternion covering and transport matrices, complete Gram/corner/Schur identities. Does not infer disk avoidance in the equality case 2+3=5.',
'verify_whitney_move':'Exact cutoff and flow derivatives, full intersection and tangency signs, both ambient inverse composites and corner charts, normal-scale/dilation/shear identities, and nonorthogonal frame/collar examples. Global supported motion and handle arrangement are separate.',
'verify_handle_chains':'Outward-normal/incidence signs for indices 1–6, both symbolic unit-pivot contractions with full Schur terms and homotopies, explicit six- and seven-dimensional chain contractions, exact negative-pivot torsion 483, and adjacent differential transformations. Does not infer geometric realization from a chain contraction.',
'verify_handle_pair_creation':'Full birth-parameter and variable-radius derivatives, exact bump/level gaps, level-map inverse and attaching-frame formulas, all six worked Hessian entries, four permutation signs and a noncommuting variable-time projection. Does not prove compact implantation or transversality.',
'verify_framed_slides':'Explicit based noncommutative word products, full crossing/holonomy derivatives and exact hitting factor, original mixed derivatives and Hessian, reverse signs/handle counts in dimensions 6 and 7, plus two source-delimiter checks. Those delimiter checks are editorial, not mathematical proof.',
'verify_smooth_duality':'Exact antiunitary exterior-frame, differential and adjoint signs in dimensions 1–6; one arbitrary symbolic two-by-two perturbation with complete resolvents, effective differential, chain maps and homotopy identities. Functional-analytic estimates are not certified by this finite algebra.',
'verify_integral_duality':'Formal coefficientwise cap-boundary identity through simplex dimension 8; the two original integral cover pairings and degree-three image indices; all 19-by-19 sampled integer rows per cover and complete exercise columns. General divisibility and duality proofs are separate.',
'verify_tangent_index':'Four finite zigzag transfers including their higher terms, 25 tensor-order/nilpotence combinations, exact Schur and orientation identities, full degree-six root polynomial and index signs. No operator-theoretic or global index conclusion is inferred from these tests.',
'verify_almost_complex':'Full source reread here; execution reuses the already recorded unchanged-mathematics portable run. Its finite octonion basis, symbol, gauge, clutching and 100 rational inequality checks do not establish convergence or replace the analytic proof.'}

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def archive(p):return str(p.relative_to(D))
def sourcepath(p):return str(p.relative_to(ROOT))
for part in ['checks','src','original_context','outputs']:(DEST/part).mkdir(parents=True,exist_ok=True)
prepared=[]
for name in NAMES:
    source=SRC/'checks'/(name+'.py')
    text=source.read_text()
    tree=ast.parse(text)
    literals=[x.value for x in ast.walk(tree) if isinstance(x,ast.Constant) and isinstance(x.value,str)]
    chapters=sorted({x for x in literals if x.startswith('src/') and x.endswith('.md')})
    outputs=sorted({x for x in literals if x.startswith('checks/') and x.endswith('.json')})
    assert len(chapters)==1 and len(outputs)==1,(name,chapters,outputs)
    chapter=SRC/chapters[0];original_out=SRC/outputs[0]
    original_copy=DEST/'original_context'/source.name
    shutil.copyfile(source,original_copy)
    row={**META,'program':source.name,'original_program':sourcepath(source),'original_program_sha256':sha(source),
         'original_context_copy':archive(original_copy),'source_line_count':len(text.splitlines()),
         'complete_source_program_read':True,'reading_scope':'Every original source line, all asserted identities, iteration ranges, input parsing and output behavior read; no chapter-proof reread is asserted by this program event.',
         'mathematical_scope':NOTES[name],'original_chapter':sourcepath(chapter),
         'original_chapter_sha256':sha(chapter),'original_output':sourcepath(original_out) if original_out.exists() else None,
         'original_output_sha256':sha(original_out) if original_out.exists() else None}
    if name=='verify_almost_complex':
        prior=json.loads((D/'code/maps_audit/course/additional_rerun_manifest.json').read_text())
        entry=next(r for r in prior if Path(r['script']).name==source.name)
        assert entry['original_sha256']==sha(source)
        row.update(execution_reused=True,execution_manifest='code/maps_audit/course/additional_rerun_manifest.json',
                   execution_record=entry,exit_code=entry['exit_code'],passed=entry['portable_passed'],
                   program_path=entry['script'].removeprefix('deliverables/'),
                   output=entry['portable_output'].removeprefix('deliverables/'),
                   command=entry['command'],cwd=entry['cwd'].removeprefix('deliverables/'),
                   executed_sha256=entry['adapted_sha256'],program_changes=entry['only_changes'])
        prepared.append(row)
        continue
    executed=DEST/'checks'/source.name
    target_chapter=DEST/chapters[0]
    shutil.copyfile(source,executed)
    shutil.copyfile(chapter,target_chapter)
    assert sha(source)==sha(executed)==sha(original_copy)
    assert sha(chapter)==sha(target_chapter)
    row.update(execution_reused=False,program_path=archive(executed),executed_sha256=sha(executed),
               program_changes='None. Exact original bytes are run in the reconstructed relative checks/src layout.',
               source_input=archive(target_chapter),source_input_sha256=sha(target_chapter),source_hash_recomputed=True,
               output=archive(DEST/outputs[0]),cwd=archive(DEST),portable_command=['python3','checks/'+source.name])
    prepared.append(row)

records=[r for r in prepared if r['execution_reused']]
def save():
    payload={'schema':'course-geometric-execution/1','metadata':META,'assigned_programs':20,
             'complete_program_reading_lines':sum(r['source_line_count']for r in prepared),
             'scope':'Nineteen new unchanged-program executions and one explicitly reused execution. Source inputs copied byte-for-byte; every source-dependent assertion retained. No finite certificate is treated as a geometric proof.',
             'historical_output_metadata':'Fields such as independent_review=false or historical remaining-work prose are retained original producer metadata. Current complete code readings and executions are recorded by this appended manifest; full chapter proofs are covered by the separate receiving-proof ledger.',
             'completed_records':len(records),'runs':sorted(records,key=lambda r:r['program'])}
    temp=MANIFEST.with_suffix('.tmp');temp.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n');temp.replace(MANIFEST)
save()

def run(row):
    row=dict(row);p=D/row['program_path'];out=DEST/'outputs'/(p.name+'.stdout.txt');err=DEST/'outputs'/(p.name+'.stderr.txt')
    command=[sys.executable,str(p)];t=time.monotonic()
    row['command']=command;row['actual_cwd']=str(DEST);row['started_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        r=subprocess.run(command,cwd=DEST,text=True,capture_output=True,timeout=240)
        stdout,stderr,exit_code=r.stdout,r.stderr,r.returncode
    except subprocess.TimeoutExpired as e:
        stdout=e.stdout or '';stderr=e.stderr or ''
        if isinstance(stdout,bytes):stdout=stdout.decode(errors='replace')
        if isinstance(stderr,bytes):stderr=stderr.decode(errors='replace')
        exit_code=None;row['status']='timed_out_after_240_seconds'
    out.write_text(stdout);err.write_text(stderr)
    row.update(stdout=archive(out),stdout_sha256=sha(out),stderr=archive(err),stderr_sha256=sha(err),
               exit_code=exit_code,elapsed_seconds=round(time.monotonic()-t,3))
    p_out=D/row['output']
    if p_out.exists():
        current=json.loads(p_out.read_text());row['output_sha256']=sha(p_out);row['passed']=current.get('passed')
        row['recorded_output_scope']=current.get('scope',current.get('limitations',current.get('limits')))
        row['source_input_hash_matches_output']=current.get('source_sha256')==row['source_input_sha256']
        if row['original_output']:
            old=ROOT/row['original_output'];original=json.loads(old.read_text())
            keys=sorted(set(original)|set(current));diff=[k for k in keys if original.get(k)!=current.get(k)]
            row['comparison']={'byte_identical':p_out.read_bytes()==old.read_bytes(),'parsed_json_identical':current==original,'differing_keys':diff,
                               'line_ending_normalized_byte_equal':p_out.read_bytes().replace(b'\r\n',b'\n')==old.read_bytes().replace(b'\r\n',b'\n'),
                               'mathematical_json_fields_identical':all(k in ['source_sha256','reader','date','effort','source_hash_recomputed']for k in diff)}
        row['outcome']='passed at the specified finite scope' if exit_code==0 and row['source_input_hash_matches_output'] else 'execution or input-integrity issue'
    else:
        row['outcome']='no expected certificate produced'
    return row

with ThreadPoolExecutor(max_workers=3) as pool:
    pending={pool.submit(run,r):r['program']for r in prepared if not r['execution_reused']}
    for fut in as_completed(pending):
        row=fut.result();records.append(row);save()
        print(json.dumps({k:row.get(k)for k in ['program','exit_code','elapsed_seconds','passed','outcome','comparison']}),flush=True)
print(json.dumps({'complete':len(records),'new_runs':19,'reused_runs':1,'failures':[r['program']for r in records if r.get('exit_code')!=0]}),flush=True)
