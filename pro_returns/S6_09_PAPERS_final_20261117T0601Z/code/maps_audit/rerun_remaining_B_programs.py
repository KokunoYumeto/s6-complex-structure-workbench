"""Run the eleven original mathematical certificates in the copied code tree."""
from pathlib import Path
import ast, concurrent.futures, datetime, hashlib, json, platform, subprocess, sys
import sympy

ROOT=Path(__file__).resolve().parents[3]
S=ROOT/'sources/returns/S6_04_MAPS_MANIFOLDS/code'
C=ROOT/'deliverables/code/maps_audit/MAPS/code'
W=ROOT/'deliverables/work/maps_audit'
O=W/'maps_B_remaining_program_runs'
O.mkdir(exist_ok=True)
META=dict(reader='GPT-6 Astra (OpenAI, ChatGPT Pro mode)',effort='Pro',date='2026-11-17')
SPECS={
 'maps_cw':(['B.5.2'],'Integral exterior invariants and finite pullback Gram determinants, cusp contraction saturation and finite attachment matrices; the printed geometric proof, not hardcoded output ranks, establishes the actual CW model and global homology.'),
 'maps_smoothing_monodromy':(['B.6.3'],'Exterior dual-action parabolic complexes, zero differentials, quotient dimensions, actual parameter action and explicit coboundaries; no geometric smoothing existence is inferred from matrices.'),
 'maps_mapping_torus_cohom':(['B.6.4'],'Nilpotent differential graded algebra, affine return defects, chain-map identity, cohomology and parabolic quotient dimensions, and critical trace evaluation. This supports the receiving constructible-sheaf argument; it is not independently a global model theorem.'),
 'maps_ordinary_shear_obstruction':(['B.6.7','B.6.8'],'Exact rational coboundary, Smith denominator6 and symbolic general first coordinate b/6-kN1; exact order6 uses the receiving primitive b=+/-1 hypothesis.'),
 'fourfolds_B6_cover':(['B.6.10'],'Degree12 connected cyclic covering, ramification, genus, exact eigendifferential valuations, section-height arithmetic and Fourier character decomposition in Q[x]/Phi12. The fixed-locus inputs and surface construction are geometric prerequisites.'),
 'fourfolds_B6_plumbing':(['B.6.11'],'Exact surface Gram matrix, radical, positive rank2 form of determinant11, and the conductor difference-pairing polynomial identity. The actual untwisted filling and intersection formula are receiving-proof inputs.'),
 'maps_component_periods':(['B.6.12','B.6.13'],'Full free-group braid action and cocycle evaluation in the two stated character components; exact cohomology actions, characteristic polynomials, base-character counts, holomorphic differential valuations and global lattice coinvariants. No existence of a seven-dimensional filling is inferred.'),
 'fourfolds_B6_torsor_local':(['B.6.13','B.6.14'],'Exact order3/order4 good-reduction charts and marked section coordinates, local torsion, a representative no-common-invariant calculation, and exact branch multiplicity12 by derivatives. Formal norm solvability and global analytic descent are printed proof inputs.'),
 'maps_free_circle':(['B.6.15'],'Symbolic Spin-c Eells–Kuiper coefficient identities, spin congruence substitution and twisted spin Dirac index. Its original conditional-scope warning is preserved; subsequent actual geometric evaluations are separate results.'),
 'manifolds_mapping_general':(['B.6.22','B.6.23'],'All-integer-parameter shear and transformed defects, peripheral identities, actual collar primitives and determinant cube contributions, including inverse convention; no finite multiplicity cutoff. Geometric marking and orientation calibration are receiving-proof inputs.'),
 'maps_trace_linking':(['B.6.24'],'All-positive-d exact rational free/trace cancellation, opposite-sign relation, and d=2 denominator contradiction. Identification of the actual boundary torsion generator and trace is a separate geometric prerequisite.')
}

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(name):
    ids,scope=SPECS[name];source=S/(name+'.py');copy=C/(name+'.py')
    if sha(source)!=sha(copy):raise RuntimeError('Unexpected altered certificate '+name)
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    p=subprocess.run([sys.executable,str(copy)],cwd=C,text=True,capture_output=True,timeout=180)
    (O/(name+'.stdout.txt')).write_text(p.stdout)
    (O/(name+'.stderr.txt')).write_text(p.stderr)
    original_json=S/(name+'.out.json');new_json=C/(name+'.out.json')
    json_comparison=None
    if original_json.exists():
        json_comparison=dict(original=str(original_json.relative_to(ROOT)),rerun=str(new_json.relative_to(ROOT)),
                             exact_byte_equal=original_json.read_bytes()==new_json.read_bytes(),
                             parsed_equal=json.loads(original_json.read_text())==json.loads(new_json.read_text()),
                             original_sha256=sha(original_json),rerun_sha256=sha(new_json))
    old_stdout=next((S/(name+x) for x in ['.stdout.txt','.out'] if (S/(name+x)).exists()),None)
    stdout_comparison=None
    if old_stdout is not None:
        stdout_comparison=dict(original=str(old_stdout.relative_to(ROOT)),original_sha256=sha(old_stdout),
                               exact_equal=old_stdout.read_text()==p.stdout,
                               whitespace_normalized_equal=' '.join(old_stdout.read_text().split())==' '.join(p.stdout.split()))
    passed=p.returncode==0 and (json_comparison is None or json_comparison['parsed_equal']) and (stdout_comparison is None or stdout_comparison['whitespace_normalized_equal'])
    row=dict(program=name+'.py',results=['MAPS:'+i for i in ids],source=str(source.relative_to(ROOT)),
             executed_copy=str(copy.relative_to(ROOT)),source_sha256=sha(source),executed_sha256=sha(copy),
             command=[sys.executable,str(copy.relative_to(ROOT))],cwd=str(C.relative_to(ROOT)),
             started_at_utc=start,exit_code=p.returncode,source_lines=len(source.read_text().splitlines()),
             syntactic_assertion_sites=sum(isinstance(x,ast.Assert) for x in ast.walk(ast.parse(source.read_text()))),
             complete_program_read=True,mathematical_scope=scope,original_json_comparison=json_comparison,
             original_stdout_comparison=stdout_comparison,stdout=str((O/(name+'.stdout.txt')).relative_to(ROOT)),
             stderr=str((O/(name+'.stderr.txt')).relative_to(ROOT)),all_available_outputs_agree=passed,
             program_changes='None; original and executed source hashes are identical.',**META)
    (O/(name+'.run.json')).write_text(json.dumps(row,indent=2)+'\n')
    return row

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    rows=list(pool.map(run,SPECS))
record=dict(metadata=META,python=platform.python_version(),sympy=sympy.__version__,
            scope='Eleven complete code readings and exact reruns; geometry and original theorem prerequisites remain separate.',runs=rows)
(W/'maps_B_remaining_program_manifest.json').write_text(json.dumps(record,indent=2)+'\n')
events=json.loads((W/'check_events.json').read_text());known={x.get('event_id') for x in events}
audit=json.loads((W/'results_audit.json').read_text())
for r in rows:
    eid='new-maps-B-program-20261117:'+r['program']
    event=dict(event_id=eid,results=r['results'],scope=r['mathematical_scope'],
               outcome='All assertions passed and all available archived outputs agree.' if r['all_available_outputs_agree'] else 'Inspect exit status and exact comparison fields; no unconditional pass.',
               run_record=str((O/(Path(r['program']).stem+'.run.json')).relative_to(ROOT)),**META)
    if eid not in known:events.append(event)
    for x in audit:
        if 'MAPS:'+x['id'] not in r['results']:continue
        x.setdefault('check_event_ids',[])
        if eid not in x['check_event_ids']:x['check_event_ids'].append(eid)
        x.setdefault('program_check_records',[])
        if event['run_record'] not in x['program_check_records']:x['program_check_records'].append(event['run_record'])
(W/'check_events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n')
(W/'results_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(programs=len(rows),source_lines=sum(r['source_lines'] for r in rows),
                      exits={r['program']:r['exit_code'] for r in rows},
                      all_available_outputs_agree=all(r['all_available_outputs_agree'] for r in rows)),indent=2))
