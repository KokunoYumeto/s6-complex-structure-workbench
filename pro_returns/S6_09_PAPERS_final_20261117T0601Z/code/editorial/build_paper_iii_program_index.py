"""Build Paper III's program catalogue from actual, separately scoped run records.

This is an indexer, not a runner.  It never executes a mathematical program.
Historical commands and outcomes are preserved separately from inspected,
archive-relative replay commands.  A retained file alone is not run evidence.
"""
from __future__ import annotations
from pathlib import Path
from collections import defaultdict, Counter
import ast
import hashlib
import json
import re
import shlex
import datetime

D = Path(__file__).resolve().parents[2]
ROOT = D.parent
REC = D / 'records'
ED = D / 'editorial'
W = D / 'work/cdp_audit'
META = {'reader': 'GPT-6 Astra (OpenAI, ChatGPT Pro mode)', 'effort': 'Pro',
        'date': '2026-11-17', 'scope': 'Execution-evidence and portable-path indexing; no new blanket proof or program verification.'}
RAW = (D / 'S6_09_PAPERS_III.tex').read_text()
CORE = RAW
REMOVED = []
# Generated concordances must not make their own filenames operative on rerun.
for marker in ['PROGRAM INDEX', 'III PROGRAM INDEX', 'RESULT INDEX', 'III RESULT INDEX', 'III PROVENANCE']:
    pat = r'% BEGIN GENERATED ' + re.escape(marker) + r'.*?% END GENERATED ' + re.escape(marker) + r'[^\n]*\n?'
    CORE, n = re.subn(pat, '', CORE, flags=re.S)
    if n:
        REMOVED.append({'marker': marker, 'blocks': n})
for name in ['III_result_index.tex', 'III_provenance.tex']:
    p = ED / name
    if p.exists() and p.read_text() in CORE:
        CORE = CORE.replace(p.read_text(), '')
        REMOVED.append({'exact_editorial_fragment': str(p.relative_to(D))})
SCAN = CORE.replace(r'\_', '_')
PROGRAM_RE = re.compile(r'(?<![A-Za-z0-9_-])(?:[A-Za-z0-9_.-]+/)*[A-Za-z0-9_][A-Za-z0-9_.-]*\.(?:py|jl|gp|sage|sh|cpp|c)\b')
USES = defaultdict(list)
# Do not inherit a previous source theorem merely because a supplement uses
# another label namespace. Retain every structural/result label, regardless
# of owner; equation and layout-QA anchors are not receiving results.
labels = []
environment_stack = []
statement_label_stack = []
statement_environments = {'theorem', 'proposition', 'lemma', 'corollary',
                          'remark', 'definition', 'problem', 'computed',
                          'statement'}
math_environments = {'equation', 'equation*', 'align', 'align*', 'gather',
                     'gather*', 'multline', 'multline*', 'displaymath',
                     'split', 'aligned', 'gathered', 'flalign', 'flalign*'}
for event in re.finditer(r'\\(begin|end)\{([^}]+)\}|\\label\{([^}]+)\}', SCAN):
    if event[1] == 'begin':
        environment_stack.append(event[2])
        statement_label_stack.append(None)
    elif event[1] == 'end':
        if event[2] in environment_stack:
            k = len(environment_stack) - 1 - environment_stack[::-1].index(event[2])
            environment_stack = environment_stack[:k]
            statement_label_stack = statement_label_stack[:k]
    elif not (set(environment_stack) & math_environments):
        key = event[3]
        if not key.startswith('qa:') and ':eq:' not in key and not key.startswith('eq:'):
            enclosing = [i for i, e in enumerate(environment_stack) if e in statement_environments]
            if enclosing:
                i = enclosing[-1]
                # A later paragraph anchor within the same numbered result
                # does not replace that result as the certificate receiver.
                if statement_label_stack[i] is not None:
                    continue
                statement_label_stack[i] = key
            labels.append({'position': event.start(), 'label': key,
                           'environment': environment_stack[-1] if environment_stack else 'structural'})
for m in PROGRAM_RE.finditer(SCAN):
    prior = [x for x in labels if x['position'] < m.start()]
    USES[Path(m[0]).name].append({
        'spelling': m[0], 'core_line': SCAN.count('\n', 0, m.start()) + 1,
        'preceding_label': prior[-1]['label'] if prior else None,
        'receiver_detection': 'Nearest structural or numbered-result label of any namespace; math-environment and layout-QA labels excluded; later paragraph anchors inside one numbered result retain its first result label.',
        'receiver_label_line': SCAN.count('\n', 0, prior[-1]['position']) + 1 if prior else None,
        'receiver_environment': prior[-1]['environment'] if prior else None,
        'excerpt': SCAN[max(0, m.start()-280):m.end()+600].strip()})

RUNS = defaultdict(list)
MANIFESTS = {}
ISSUES = []
HELPERS = {}
ADDITIONAL_READINGS = defaultdict(list)

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def rel(p):
    """Resolve a known archive/workspace path, never a basename search."""
    if p is None:
        return None
    p = str(p)
    if p.startswith(str(D) + '/'):
        return p[len(str(D))+1:]
    if p.startswith('deliverables/'):
        return p[len('deliverables/'):]
    return p

def load(name):
    p = D / name
    if not p.exists():
        ISSUES.append({'kind': 'missing_manifest', 'path': name})
        return None
    MANIFESTS[name] = {'path': name, 'sha256': digest(p)}
    return json.loads(p.read_text())

def cmd(x):
    return shlex.split(x) if isinstance(x, str) else list(x or [])

def artifact(p, expected=None, kind='output'):
    p = rel(p)
    result = {'path': p, 'kind': kind, 'exists': bool(p and (D/p).is_file())}
    if result['exists']:
        result['sha256'] = digest(D/p)
        result['bytes'] = (D/p).stat().st_size
        if expected:
            result['recorded_sha256'] = expected
            result['matches_recorded_sha256'] = result['sha256'] == expected
            if not result['matches_recorded_sha256']:
                ISSUES.append({**result, 'issue_kind': 'recorded_hash_mismatch'})
    else:
        ISSUES.append({'kind': 'missing_' + kind, 'path': p})
    return result

def add(manifest, index, raw, program, command, cwd='.', outputs=(), scope=None,
        exit_code='FROM_RECORD', priority=50, status=None, source_hash=None,
        note=None, inputs=()):
    program = rel(program)
    if exit_code == 'FROM_RECORD':
        exit_code = raw.get('exit_code', raw.get('returncode', raw.get('actual_exit_code')))
    if status is None:
        historical_status=str(raw.get('status','')).lower()
        if 'timed out' in historical_status or 'timeout' in historical_status:
            status='recorded_timeout'
        else:
            status = 'recorded_success' if exit_code == 0 else ('recorded_failure' if exit_code is not None else 'execution_outcome_unrecorded')
    recorded = raw.get('command')
    r = {'run_id': f'{manifest}#{index}', 'evidence_manifest': manifest,
         'evidence_record_index': index, 'program': program,
         'program_artifact': artifact(program, source_hash, 'program'),
         'historical_command': recorded,
         'historical_command_recorded': recorded is not None,
         'historical_cwd': raw.get('cwd', raw.get('execution_cwd', raw.get('actual_working_directory', raw.get('working_directory', raw.get('runner_working_directory'))))),
         'portable_command': list(command), 'portable_cwd': rel(cwd),
         'portable_command_basis': 'Inspected retained script entry point and archive layout; an archive-relative replay, not a fabricated historical invocation.',
         'exit_code': exit_code, 'execution_status': status,
         'scope': scope or raw.get('mathematical_scope') or raw.get('scope') or raw.get('statement_role') or raw.get('execution_scope'),
         'associated_results': raw.get('associated_source_ids', raw.get('results', [])),
         'outputs': [], 'inputs': [], 'priority': priority,
         'original_record': raw,
         'recorded_metadata': {k: raw[k] for k in ['reader','effort','date','run_date','read_scope','complete_program_read','full_code_read','program_changes','changes','modifications','status','failure_diagnosis','matches_retained_output','stdout_matches_retained_source_output','mathematical_json_fields_identical_to_original','mathematical_body_unchanged','numerical_scope','passed'] if k in raw}}
    if note:
        r['index_note'] = note
    for o in outputs:
        if isinstance(o, tuple):
            path, expected = o
        else:
            path, expected = o, None
        if path and rel(path) not in [x['path'] for x in r['outputs']]:
            r['outputs'].append(artifact(path, expected))
    for p in inputs:
        if p:
            r['inputs'].append(artifact(p, kind='input'))
    if not (D / rel(cwd)).is_dir():
        ISSUES.append({'kind': 'missing_working_directory', 'run': r['run_id'], 'path': rel(cwd)})
    if not r['outputs']:
        ISSUES.append({'kind': 'no_retained_output_in_run_record', 'run': r['run_id']})
    RUNS[Path(program).name].append(r)
    return r

# D: the author's exact archive-relative commands retain all arguments.
f = 'work/invariants_arithmetic/maps_D_program_manifest.json'
for i, r in enumerate(load(f) or []):
    p = r.get('archive_relative_program', r['program'])
    c = cmd(r.get('archive_relative_command', r['command']))
    c[0] = 'python3'
    outs = [(r.get('archive_relative_output', r.get('output')), r.get('output_sha256'))]
    for k in ['json_output', 'certificate']:
        if isinstance(r.get(k), str):
            outs.append(r[k])
    for a in r.get('generated_json_comparisons', []):
        outs.append((a['path'], a.get('sha256')))
    add(f, i, r, p, c, outputs=outs, source_hash=r.get('program_sha256'), priority=20)

# Fully documented receiving B and final small-program checks.
for f in ['work/maps_audit/maps_B_remaining_program_manifest.json', 'work/maps_audit/final_small_program_manifest.json']:
    data = load(f) or {}
    for i, r in enumerate(data.get('runs', [])):
        p = rel(r['executed_copy'])
        outs = [(r['stdout'], r.get('stdout_sha256')), r.get('stderr')]
        if r.get('original_json_comparison'):
            c = r['original_json_comparison']
            outs.append((c['rerun'], c.get('rerun_sha256')))
        if r.get('certificate'):
            outs.append((r['certificate'],r.get('certificate_sha256')))
        add(f, i, r, p, ['python3', Path(p).name], str(Path(p).parent), outs,
            source_hash=r.get('executed_sha256'), priority=10)
        if r.get('prior_failed_attempt'):
            failed_path=rel(r['prior_failed_attempt']);old=load(failed_path)
            if old:
                old=dict(old)
                if 'actual_argv'in old:old['command']=old['actual_argv']
                add(failed_path,0,old,p,['python3',Path(p).name],str(Path(p).parent),
                    [old['stderr']],scope=old.get('cause'),priority=90)

# E originals and separately written exact exterior-page checker.
for f in ['code/cdp_audit/maps_E/execution_manifest.json', 'code/cdp_audit/maps_E/independent_execution_manifest.json']:
    for i, r in enumerate(load(f) or []):
        p = rel(r.get('executed', r.get('source')))
        add(f, i, r, p, ['python3', Path(p).name], str(Path(p).parent),
            [(r['output'], r.get('output_sha256'))], source_hash=r.get('executed_sha256',r.get('source_sha256')), priority=15)

# F: original attempt records plus the successful argument-bearing replays.
FP = 'code/root_maps_F/runtime'
layout = load('code/root_maps_F/portable_layout_manifest.json') or []
layout_hashes = {r['portable_copy']: r['sha256'] for r in layout}
f = 'code/root_maps_F/execution_manifest.json'
for i, r in enumerate(load(f) or []):
    name = Path(r['program']).name
    p = FP + '/code/' + name
    c = ['python3', 'code/' + name] + cmd(r.get('command'))[2:]
    add(f, i, r, p, c, FP, [(r['output'], r.get('output_sha256'))],
        source_hash=r.get('sha256'), priority=40,
        note='Original flat-directory attempt retained; portable copy has the identical mathematical source and reconstructed input layout.')
f = 'code/root_maps_F/cli_execution_manifest.json'
for i, r in enumerate(load(f) or []):
    c = cmd(r['command'])
    if any(a.endswith('.jl') for a in c):
        p = next(a for a in c if a.endswith('.jl'))
        portable = ['julia', '--startup-file=no', '--project=hecke_env', p]
        note = 'The original Python launcher uses a historical hardcoded cache. The portable command invokes Julia directly with the retained pinned environment; the actual launcher remains in the evidence record.'
    else:
        p = c[1]
        portable = ['python3'] + c[1:]
        note = None
    record_args=[a for a in c[2:] if a.startswith('records/')]
    inputs = [FP+'/'+a for a in record_args[:-1]] if len(record_args)>1 else []
    if p.endswith('test_fourfolds_conjugacy_actual.jl'):
        inputs.append(FP+'/records/fourfolds_conjugacy_actual_inputs.toml')
    outs = [(r['output'], r.get('output_sha256'))]
    if len(record_args)>1:
        outs.append(FP+'/'+record_args[-1])
    if p.endswith('test_fourfolds_conjugacy_actual.jl'):
        outs.append(FP+'/records/fourfolds_conjugacy_actual_tests.toml')
    rr = add(f, i, r, FP+'/'+p, portable, FP, outs,
        source_hash=layout_hashes.get(FP+'/'+p) if p.endswith('.jl') else r.get('program_sha256'),
        priority=5, note=note, inputs=inputs)
    if p.endswith('.jl'):
        rr['historical_launcher_artifact'] = artifact(FP+'/'+c[1], r.get('program_sha256'), 'launcher')
f = 'code/root_maps_F/hecke_algebraic_execution_record.json'
r = load(f)
if r:
    add(f, 0, r, FP+'/code/test_fourfolds_integral_conjugacy.jl',
        ['julia','--startup-file=no','--project=hecke_env','code/test_fourfolds_integral_conjugacy.jl'], FP,
        [(r['output'],r.get('sha256',{}).get('output')),(r['certificate'],r.get('sha256',{}).get('certificate'))], priority=5,
        note='Direct Julia replay avoids the historical runner cache path; six algebraic cases, not an enumeration of the infinite tuple set.')
f = 'code/root_maps_F/direct_tuple_execution_record.json'
r = load(f)
if r:
    add(f, 0, r, r['program'], cmd(r['command']), FP,
        [(r['output'],r.get('output_sha256')),(r['certificate'],r.get('certificate_sha256'))],
        inputs=[r['input']],source_hash=r.get('program_sha256'), priority=5)
load('code/root_maps_F/final_execution_reconciliation.json')

# Earlier small MAPS runs and only those PUSH programs operative in Paper III.
f = 'code/maps_audit/selected_reruns.json'
for i, r in enumerate(load(f) or []):
    name = Path(r['program']).name
    if r['program'].startswith('PUSH/') and name not in USES:
        continue
    p = 'code/maps_audit/' + r['program']
    add(f, i, r, p, ['python3', Path(p).name], str(Path(p).parent),
        [('code/maps_audit/'+r['output'],r.get('output_sha256'))],
        source_hash=r.get('program_sha256',r.get('sha256')), priority=70,
        note='The manifest records completion and output. When it omits the original command, the displayed command is the inspected portable replay only.')
f = 'code/push/rerun_manifest.json'
for i, r in enumerate(load(f) or []):
    if r['program'] not in USES:
        continue
    p = 'code/push/code/' + r['program']
    add(f, i, r, p, ['python3',Path(p).name], str(Path(p).parent),
        [r['log']],source_hash=r.get('sha256'),priority=25)

# Stable/course checkers: distinguish mathematical equality from metadata edits.
f = 'work/maps_audit/remaining_stable_rerun_record.json'
data = load(f) or {}
for i, r in enumerate(data.get('programs', [])):
    cwd = rel(r['execution_cwd']);p=cwd+'/'+r['program']
    add(f, i, r, p, ['python3', r['program']], cwd,
        [(r['output'],r.get('output_sha256'))], scope=r.get('numerical_scope') or data.get('excluded_scope'),
        source_hash=r.get('portable_sha256'),priority=15)
f = 'work/maps_audit/stable_algebra_rerun_record.json'
data = load(f) or {}
byout = {Path(r['output']).name:r for r in data.get('outputs',[])}
stable = 'code/maps_audit/course/stable'
for i,(name,outname) in enumerate([
    ('calculate_original_coefficient_h28.py','ORIGINAL_COEFFICIENT_H28_CERTIFICATE.json'),
    ('verify_coefficient_rings.py','COEFFICIENT_RING_CHECKS.json'),
    ('calculate_degree_six_cobar.py','DEGREE_SIX_COBAR_CALCULATION.json'),
    ('verify_degree_six_cobar.py','DEGREE_SIX_COBAR_CHECKS.json')]):
    r = byout.get(outname)
    if not r:
        continue
    note = data.get('scope','')
    rr=add(f, i, r, stable+'/'+name,['python3',name],stable,
        [(r['output'],r.get('sha256'))],scope='Exact finite coefficient/cobar matrices and specified finite algebraic tests. All-length comparison and topological realization are proved separately.',
        status='completed_narrative_numeric_exit_unrecorded',priority=15,note=note)
    if name=='verify_coefficient_rings.py':
        a=byout.get('ORIGINAL_COEFFICIENT_H28_CERTIFICATE.json')
        if a:rr['outputs'].append(artifact(a['output'],a.get('sha256')))
for f, key in [('code/maps_audit/course/portable_rerun_manifest.json','path_metadata_only_changes'),
               ('code/maps_audit/course/additional_rerun_manifest.json',None)]:
    data=load(f) or ([] if key is None else {})
    for i,r in enumerate(data if key is None else data.get(key,[])):
        p=rel(r.get('portable_script',r.get('script')));cwd=rel(r['cwd'])
        add(f,i,r,p,['python3',Path(p).name],cwd,
            [(r.get('portable_output',r.get('output')),r.get('output_sha256'))],
            source_hash=r.get('portable_sha256',r.get('adapted_sha256')),priority=15,
            scope='The unchanged finite algebraic assertions and specified sample ranges; optional source-text/hash checks are provenance checks, not mathematical verification.',
            note=r.get('only_changes','Path/metadata adaptation only. Without an optional source argument, the recorded original source hash is retained and is not recomputed.'))

# New scoped writing checks, with original failed attempts left elsewhere intact.
f='work/cdp_audit/carrier_period_program_record.json';r=load(f)
if r:
    add(f,0,r,r['program'],['python3',rel(r['program'])],'.',
        [(r['stdout'],r.get('stdout_sha256')),r.get('stderr')],source_hash=r.get('program_sha256'),priority=15)
f='work/cdp_audit/III_program_gap_runs.json'
for i,r in enumerate(load(f) or []):
    add(f,i,r,r['program'],r['archive_relative_command'],'.',
        [(r['output'],r.get('output_sha256')),r['stderr']],source_hash=r.get('program_sha256'),priority=5)

# Additional complete geometric-provider code readings and finite executions.
f='work/cdp_audit/course_geometric_execution_manifest.json'
data=load(f) or {}
for i,r in enumerate(data.get('runs',[])):
    if r.get('execution_reused'):
        ADDITIONAL_READINGS[r['program']].append({'manifest':f,'record_index':i,'reading':r})
        continue
    rr=add(f,i,r,r['program_path'],r['portable_command'],r['cwd'],
        [(r['stdout'],r.get('stdout_sha256')),(r['stderr'],r.get('stderr_sha256')),
         (r['output'],r.get('output_sha256'))],source_hash=r.get('executed_sha256'),priority=15)
    rr['inputs'].append(artifact(r['source_input'],r.get('source_input_sha256'),'input'))

# Independently replayed modular construction: a separate execution of the same
# unchanged verifier, not a second theorem or a claim about the entire engine.
f='code/cdp_audit/modular_collision_review/execution_manifest.json'
r=load(f)
if r:
    p=r['inputs'][0]['executed_copy']
    add(f,0,r,p,['python3',Path(p).name],str(Path(rel(p)).parent),
        [(r['stdout'],r.get('stdout_sha256')),r['stderr'],(r['certificate'],r.get('certificate_sha256'))],
        source_hash=r['inputs'][0]['sha256'],priority=25,
        inputs=[a['executed_copy']for a in r['inputs'][1:]])

# Two short repair certificates have explicit successful-rerun narratives, but
# no saved numeric exit or precise argv.  Preserve that limitation honestly.
f='work/maps_audit/check_events.json'
events=load(f) or []
repair_events={
 'new-H3-correction-20261117':('finite_degree_three_correction.py','Corrected degree-three finite-band matrix, its Smith factors 1,1,1,0 and primitive kernel (0,1,1,6). This finite certificate does not replace the same-degree Kronecker-pairing proof.'),
 'new-fourfold-actual-torsion-d2-20261117':('fourfold_torsion_transgression.py','Integral torsion orders and global residues in degrees 2,3,4 for the actual prism-transgression lemma. The cellular-prism geometry and other Leray inputs are proved separately.')}
for i,r in enumerate(events):
    if r.get('event_id') not in repair_events:
        continue
    name,scope=repair_events[r['event_id']];p='code/maps_audit/'+name
    outputs=['code/maps_audit/'+name.replace('.py','.rerun.txt')]
    cert='code/maps_audit/'+name.replace('.py','.json')
    if (D/cert).exists():outputs.append(cert)
    add(f,i,r,p,['python3',name],'code/maps_audit',outputs,scope=scope,priority=60,
        status='completed_narrative_numeric_exit_unrecorded',
        note='The cited receiving-check event explicitly records a successful rerun. Its numeric exit and original argv were not retained; the portable command is inspected from the unchanged script.')

# The two initial-data algorithms are called by these audited wrappers.
for name,wrapper,scope in [
    ('manifolds_general_initial.py','manifolds_general_initial_audit.py',
     'Imported implementation: local_lift, actual_lifts, satimage, ikernel and compute are exercised by the audited general-initial wrapper; there is no claim of a separate main-program invocation.'),
    ('manifolds_corrected_initial.py','manifolds_corrected_initial_audit.py',
     'Imported implementation: the corrected and general compute paths are exercised in the wrapper, including 42 full-matrix overlaps, 16 D50 examples, 212 new Smith calculations and 45 further checks; no separate main invocation is claimed.'),
    ('fourfolds_integral_conjugacy.jl','test_fourfolds_conjugacy_actual.jl',
     'Included Julia implementation of the lattice decision procedure. Two successful test drivers exercise it: six actual admissible tuple tests and six algebraic obstruction/positive cases. The infinite class set is not enumerated.')]:
    path = ('code/invariants_arithmetic/maps_D_project/code/' if name.endswith('.py') else FP+'/code/') + name
    rr = RUNS.get(wrapper, [])
    if name.endswith('.jl'):
        rr = rr + RUNS.get('test_fourfolds_integral_conjugacy.jl',[])
    HELPERS[name]={'name':name,'program':path,'program_artifact':artifact(path,kind='program'),
                   'wrapper':wrapper,'scope':scope,'executed_through_runs':[r['run_id'] for r in rr],
                   'runs':rr,'execution_status':'executed_as_imported_dependency'}

name='calculate_original_coefficient_h28.py'
HELPERS[name]={'name':name,'program':stable+'/'+name,
    'program_artifact':artifact(stable+'/'+name,kind='program'),
    'wrapper':'verify_coefficient_rings.py',
    'scope':'The coefficient verifier executes this entire matrix helper with runpy.run_path; its complete certificate is produced by that actual driver. The catalogue does not assert a separately recorded main-program invocation.',
    'executed_through_runs':[r['run_id']for r in RUNS['verify_coefficient_rings.py']],
    'runs':RUNS['verify_coefficient_rings.py'],
    'execution_status':'executed_as_imported_dependency'}

PURPOSE_OVERRIDE = {
 'fourfolds_integral_conjugacy.jl':'Simultaneous integral conjugacy using the semisimple quotient, radical lifting and exact lattice isomorphism.',
 'test_fourfolds_integral_conjugacy.jl':'Six positive and negative exact simultaneous-conjugacy tests, including a nonprincipal ideal and a cubic centre.',
 'test_fourfolds_conjugacy_actual.jl':'Six tests on the actual admissible six-dimensional tuples: three unimodular conjugates and three distinct-parameter obstructions.',
 'independent_cover_markings_attempt1.py':'Superseded auxiliary assertion demanding a literal second unit column; retained as a failed attempt.',
 'fourfolds_checks.py':'Finite elliptic coinvariants, affine-quotient homology and rational shifted-product differential matrices; it does not compute the fourfold exterior row.',
 'check_carrier_period_matrix.py':'Symbolic real-period inverse transpose, determinant and projected-period identities.'}
PURPOSE_OVERRIDE['fourfolds_vertical_correction_audit.py']='Independent exact finite audit of the component-supported correction calculation in D.2.50.'
PURPOSE_OVERRIDE.update({
 'verify_morse_cancellation.py':'Supported Morse-cancellation derivatives, exact cutoff inequalities and explicit unsafe-cutoff critical points.',
 'verify_spin_six.py':'The real six-dimensional exterior representation of SU(4), its Chern/Euler polynomials and stable inverse maps.',
 'verify_tangent_index.py':'Finite homological-perturbation transfers, torsion-line binomial relations and the full tangent-index characteristic polynomial.'})

def inspect_program(p):
    if not (D/p).exists():
        return {'purpose':'Missing retained program.', 'imports':[]}
    text=(D/p).read_text()
    doc='';imports=[];local=[]
    if p.endswith('.py'):
        try:
            tree=ast.parse(text)
            doc=ast.get_docstring(tree) or ''
            for node in ast.walk(tree):
                if isinstance(node,ast.Import):imports.extend(a.name for a in node.names)
                elif isinstance(node,ast.ImportFrom) and node.module:imports.append(node.module)
            for name in sorted(set(imports)):
                candidate=(D/p).parent/(name.split('.')[0]+'.py')
                if candidate.exists():local.append(str(candidate.relative_to(D)))
        except SyntaxError as e:
            ISSUES.append({'kind':'python_syntax_error','program':p,'message':str(e)})
    purpose=PURPOSE_OVERRIDE.get(Path(p).name)
    if not purpose:
        purpose=' '.join((doc.split('\n\n')[0] if doc else '').split())
    if not purpose:
        comments=[s.lstrip('# ').strip() for s in text.splitlines()[:24] if s.startswith('#') and not s.startswith('#!')]
        purpose=' '.join(comments[:3]) or 'Exact computations at the cited receiving-proof locations.'
    return {'purpose':purpose,'source_docstring':doc,'imports':sorted(set(imports)),
            'local_import_paths':local,'inspection':'Entry point, imports, path handling and retained command layout inspected for catalogue portability; prior full code-reading scopes remain in the source manifests.'}

def pick_runs(rs):
    good=[r for r in rs if r['execution_status'] in ['recorded_success','completed_narrative_numeric_exit_unrecorded'] and r['exit_code'] in [None,0]]
    good.sort(key=lambda r:r['priority'])
    chosen=[];seen=set()
    for r in good:
        # Different archive copies of the same unchanged no-argument program
        # are duplicate checks, not new parameter regimes. Preserve all in JSON.
        c=r['portable_command']
        if c[0]=='julia':signature=(Path(c[-1]).name,tuple(c[1:-1]))
        else:signature=(Path(c[1]).name,tuple(c[2:]))
        if signature not in seen:
            chosen.append(r);seen.add(signature)
    return chosen

PROGRAMS=[]
allnames=sorted(set(RUNS)|set(HELPERS)|{n for n in USES if not n.startswith('draw_')})
for name in allnames:
    helper=HELPERS.get(name)
    rs=helper['runs'] if helper else RUNS.get(name,[])
    selected=pick_runs(rs)
    if helper:
        p=helper['program'];status=helper['execution_status']
    elif selected:
        p=selected[0]['program'];status='recorded_success' if any(r['exit_code']==0 for r in selected) else 'completed_narrative_numeric_exit_unrecorded'
    elif rs:
        p=rs[0]['program'];status='historical_failed_auxiliary_only'
    else:
        candidates=list((D/'code').rglob(name))
        p=str(candidates[0].relative_to(D)) if candidates else None
        status='no_execution_evidence'
        ISSUES.append({'kind':'named_operative_program_without_execution_record','name':name,'retained_candidates':[str(x.relative_to(D))for x in candidates]})
    inspect=inspect_program(p) if p else {'purpose':'Named operative program not retained.','imports':[]}
    entry={'name':name,'program':p,'sha256':digest(D/p) if p and (D/p).exists() else None,
           'purpose':inspect['purpose'],'scope':helper['scope'] if helper else next((r['scope']for r in selected if r.get('scope')),None),
           'execution_status':status,'cited_in_core':name in USES,'printed_uses':USES.get(name,[]),
           'supplementary_audit_program':name not in USES,'source_inspection':inspect,
           'selected_replay_run_ids':[r['run_id']for r in selected],
           'runs':rs,'imported_implementation':bool(helper)}
    if ADDITIONAL_READINGS.get(name):entry['additional_complete_source_readings']=ADDITIONAL_READINGS[name]
    if helper:entry['helper_linkage']={k:v for k,v in helper.items() if k!='runs'}
    PROGRAMS.append(entry)

# Unavailable illustrations are provenance, not failed mathematical checks.
NONOPERATIVE=[]
for name in sorted(n for n in USES if n.startswith('draw_')):
    candidates=list((D/'code').rglob(name))
    NONOPERATIVE.append({'name':name,'kind':'illustration_generator','operative':False,
        'execution_status':'not_run','source_present_in_archive':bool(candidates),
        'archive_paths':[str(p.relative_to(D))for p in candidates],
        'printed_uses':USES[name],
        'role':'Historical illustration provenance only. No execution or mathematical certification is asserted; the complete textual proof remains operative.'})
f='work/maps_audit/III_course_illustration_retention_review.json'
for i,r in enumerate(load(f) or []):
    NONOPERATIVE.append({'name':Path(r['asset_url']).name,'kind':'illustration_asset','operative':False,
       'execution_status':'not_applicable','source_present_at_recorded_path':r['asset_present_at_original_relative_path'],
       'original_asset_path':r['asset_url'],'description':r['description'],
       'source':r['source'],'source_line':r['source_line'],'evidence_manifest':f,'evidence_record_index':i,
       'review_scope':r['checked_scope'],'role':r['status']})

def esc(s):
    return ''.join({'&':r'\&','%':r'\%','#':r'\#','_':r'\_\allowbreak{}','/':r'/\allowbreak{}','$':r'\$','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}','\\':r'\textbackslash{}'}.get(c,c) for c in str(s))

def description(s):
    """Resolve source-number prose while retaining verbatim provenance in JSON."""
    rendered = esc(s)
    for source_locator, printed_label in {
        'Theorem F.2.27': 'maps:src:F.2.27',
        'MAPS E1.4': 'maps:src:E.1.4',
        'Theorem D.1.6': 'maps:src:D.1.6',
        'Proposition B.6.15': 'maps:src:B.6.15',
    }.items():
        rendered = rendered.replace(esc(source_locator), r'\cref{' + printed_label + '}')
    return rendered

def path(s):
    # xurl is loaded by the master, so every long archive path can wrap.
    return r'\path{'+str(s).replace('}',r'\}').replace(' ',r'}\ \path{')+'}'

def finite_role(r):
    if r.get('scope'):
        return r['scope']
    return 'The exact identities and finite inputs displayed at its receiving-proof uses. Geometric realization, all-parameter arguments and source-theorem hypotheses are established in the printed proofs.'

TEX = r'''% BEGIN GENERATED III PROGRAM INDEX
\section{Programs, finite certificates and portable commands}
\label{app:III:programs}
All paths below are relative to the companion archive root. Change to the
displayed working directory and run the displayed command. The output column
identifies the retained output of the recorded execution; a replay may print
to the terminal or update its own explicitly named JSON/TOML certificate.
The complete execution catalogue is \path{records/III_program_index.json}.
It preserves each original command when recorded, all source and output
hashes, supplementary runs, unsuccessful attempts and their resolutions.
The indexer does not execute mathematical programs.

The recorded Python environment is Python~3.12.14, SymPy~1.14.0 and
NumPy~2.3.5 where those packages are imported. Standard-library-only
checkers do not need either package. For the Python dependencies, run
\path{python3}\ \path{-m}\ \path{pip}\ \path{install}\ \path{sympy==1.14.0}\ \path{numpy==2.3.5}
in a suitable environment. Keep the archived directory structure:
the reconstructed MAPS projects include their original imported engines and
exact JSON fixtures. The Julia tests use Julia~1.10.10, Hecke~0.41.1,
Nemo~0.57.2 and AbstractAlgebra~0.51.4. Their pinned project and manifest are
in \path{code/root_maps_F/runtime/hecke_env}. Install Julia and instantiate
that environment by running
\path{julia}\ \path{--startup-file=no}\ \path{--project=hecke_env}\ \path{-e}\ \texttt{'using Pkg; Pkg.instantiate()'}
from \path{code/root_maps_F/runtime}. Runtime binaries and package caches are
not included. The direct Julia commands below replace the historical
\path{run_hecke.py} launcher, which contains a machine-specific cache path;
the actual historical launcher invocation remains in the execution record.

These are finite, symbolic or per-input checks. A successful output does not
prove a geometric identification, a topological realization, an all-stage
comparison theorem or an exhaustive enumeration of an infinite class set.
The complete proofs and the exact finite ranges are given at the receiving
statements. Imported implementations are identified with the test driver
that actually called them. Repeated checks of the same unchanged program
with identical arguments are consolidated in the table; every recorded run
remains separately available in the JSON catalogue.

\begingroup\small\raggedright
\setlength{\tabcolsep}{3pt}
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{65mm}>{\raggedright\arraybackslash}p{88mm}@{}}
\toprule Program, purpose and scope & Working directory, command and retained output\\\midrule
\endfirsthead
\toprule Program, purpose and scope & Working directory, command and retained output\\\midrule
\endhead
'''
for r in PROGRAMS:
    if r['execution_status']=='historical_failed_auxiliary_only':
        continue
    selected=[x for x in r['runs'] if x['run_id'] in r['selected_replay_run_ids']]
    left=path(r['name'])+r'\par '+description(r['purpose'])
    if r['imported_implementation']:
        left+=r'\par\emph{Imported implementation.} '+description(r['scope'])
    elif r.get('scope') and r['scope'] not in r['purpose']:
        left+=r'\par '+description(finite_role(r))
    result_labels=list(dict.fromkeys(u['preceding_label']for u in r['printed_uses'] if u.get('preceding_label')))
    if result_labels:
        left+=r'\par Receiving locations: '+', '.join(r'\ref{'+a+'}'for a in result_labels[:3])+('.' if len(result_labels)<=3 else '; further uses are indexed in the JSON catalogue.')
    if not selected:
        right='No execution record located. The name is retained as an unresolved operative pointer; no passing status is assigned.'
    else:
        pieces=[]
        for q in selected:
            line=path(q['portable_cwd'])+r'\par '+path(shlex.join(q['portable_command']))
            for o in q['outputs']:
                if o['path'].endswith(('.stderr.txt','.err')) and o.get('bytes')==0:
                    continue
                line+=r'\par '+path(o['path'])
            line+=r'\par '+('Recorded exit '+str(q['exit_code'])+'.' if q['exit_code'] is not None else 'Successful completion recorded; numeric exit was not retained.')
            pieces.append(line)
        right=r'\par\medskip '.join(pieces)
    TEX+=left+' & '+right+r'\\[3pt]'+'\n'
TEX+=r'\bottomrule\end{longtable}\endgroup'+'\n'
TEX+=r'''\subsection{Earlier unsuccessful attempts}
The complete run catalogue retains failed auxiliary assertions, missing-input
invocations and timeouts. They are not counted as successful checks. In
particular, the first independent covering-marking attempt demanded a
literal unit column; the corrected integer combination is checked by
\path{independent_cover_markings.py}. The first mapping-quotient invocation
lacked its engine/fixture layout and is followed by the unchanged successful
run. The initial F entry-point attempts are reconciled, with exact successful
argument-bearing replays, in
\path{code/root_maps_F/final_execution_reconciliation.json}.

\subsection{Illustration provenance without operative computation}
The following historical illustration helpers were not retained in the
attached materials and were not run. They supply no mathematical check.
The associated diagrams' full textual descriptions and mathematical
captions remain in the course-provider proofs.
'''
draws=[r for r in NONOPERATIVE if r['kind']=='illustration_generator']
TEX+='\n\n'.join(path(r['name']) for r in draws)+'\n\n'
TEX+=r'''The unavailable image assets are listed below. This records their absence;
it does not claim that the images were visually inspected. Each retained
description and adjacent mathematical caption was checked against the
complete textual argument, as scoped in
\path{work/maps_audit/III_course_illustration_retention_review.json}.
\begingroup\small\raggedright
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{62mm}>{\raggedright\arraybackslash}p{91mm}@{}}
\toprule Historical image & Retained description\\\midrule
\endfirsthead
\toprule Historical image & Retained description\\\midrule
\endhead
'''
for r in NONOPERATIVE:
    if r['kind']=='illustration_asset':
        TEX+=path(r['name'])+' & '+esc(r['description'])+r'\\[3pt]'+'\n'
TEX+=r'\bottomrule\end{longtable}\endgroup'+'\n% END GENERATED III PROGRAM INDEX\n'

# Validate replay scripts and literal argument fixtures without executing them.
for p in PROGRAMS:
    for r in p['runs']:
        c=r['portable_command'];cwd=D/r['portable_cwd']
        scripts=[a for a in c[1:] if a.endswith(('.py','.jl','.gp','.sage','.sh'))]
        r['portable_script_paths_exist']=all((cwd/a).is_file() for a in scripts)
        if not r['portable_script_paths_exist']:
            ISSUES.append({'kind':'portable_script_path_missing','run':r['run_id'],'cwd':r['portable_cwd'],'command':c})
        r['portable_literal_argument_paths']=[{'argument':a,'exists':(cwd/a).exists()} for a in c[2:] if a.startswith(('records/','code/')) and a.endswith(('.json','.toml'))]

counts={'named_programs_in_core':len(USES),
        'named_operative_programs':len([n for n in USES if not n.startswith('draw_')]),
        'catalogued_programs':len(PROGRAMS),'catalogued_run_records':sum(len(r['runs'])for r in PROGRAMS),
        'unique_execution_records':len({r['run_id']for p in PROGRAMS for r in p['runs']}),
        'imported_implementations':len(HELPERS),'nonoperative_drawing_helpers':len(draws),
        'nonoperative_image_assets':len([r for r in NONOPERATIVE if r['kind']=='illustration_asset']),
        'execution_status_counts':dict(Counter(r['execution_status']for r in PROGRAMS)),
        'issues':len(ISSUES)}
record={'schema':'paper-iii-program-index/1','generated_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'metadata':META,'source_snapshot':{'path':'S6_09_PAPERS_III.tex','sha256':hashlib.sha256(RAW.encode()).hexdigest(),
          'core_sha256':hashlib.sha256(CORE.encode()).hexdigest(),'excluded_generated_fragments':REMOVED},
        'counts':counts,'manifests':list(MANIFESTS.values()),
        'environment':{'python':'3.12.14','sympy':'1.14.0','numpy':'2.3.5',
          'julia':'1.10.10','Hecke':'0.41.1','Nemo':'0.57.2','AbstractAlgebra':'0.51.4',
          'pinned_julia_artifacts':[artifact(FP+'/hecke_env/Project.toml',kind='environment'),artifact(FP+'/hecke_env/Manifest.toml',kind='environment')],
          'binaries_and_package_caches_included':False},
        'scope':'Actual recorded executions, finite roles, imported implementations, portable commands, retained outputs and explicitly nonoperative illustrations. Presence alone never supplies a passing execution.',
        'programs':PROGRAMS,'nonoperative_illustrations':NONOPERATIVE,'unresolved_or_integrity_issues':ISSUES}
REC.mkdir(exist_ok=True);ED.mkdir(exist_ok=True)
(REC/'III_program_index.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
(ED/'III_programs.tex').write_text(TEX)
print(json.dumps(counts,indent=2))
if ISSUES:
    print(json.dumps(ISSUES,ensure_ascii=False,indent=2))
