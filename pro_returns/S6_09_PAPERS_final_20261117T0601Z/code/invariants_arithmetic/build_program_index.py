"""Index completed computations and prepare only path-portable GP inputs."""
from pathlib import Path
import hashlib,json,re,shlex
ROOT=Path(__file__).resolve().parents[3]
ARCH=ROOT/'deliverables'
AR=ARCH/'code/invariants_arithmetic/arithmetic'
OUT=ARCH/'work/invariants_arithmetic'
BASE='code/invariants_arithmetic/arithmetic'
data=json.loads((AR/'writing_complete_computations.json').read_text())
rows=[]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def archive(p):
    p=str(p)
    for prefix in [str(ARCH)+'/', 'deliverables/']:
        if p.startswith(prefix):return p[len(prefix):]
    if p.startswith('invariants_arithmetic/'):return 'code/'+p
    if p.startswith(('code/invariants_arithmetic/','work/')):return p
    return BASE+'/'+p

roles={
 'Cspecial_division.py':(['ari:C.4.3','ari:C.5.1'],'Exact division-polynomial values, resultants, torsion exclusions and special arguments.'),
 'Cspecial_relations.py':(['ari:C.5.1'],'Exact algebraic elimination for the special torsion norm values.'),
 'Cspecial_reflection.py':(['ari:C.2.2'],'Exact real-structure matrix identities and affine defect checks.'),
 'Cspecial_torsion_numerics.py':(['ari:C.1.3','ari:C.5.1'],'Independent numerical theta/product checks; exact identities have separate proofs.'),
 'Cspecial_expansion_checks.py':(['ari:C.3.1','ari:C.3.2'],'Heat-equation and Ramanujan expansion coefficients at the order-four and order-three fibres.'),
 'C_ladder_algebra.py':(['fam:src:C.2.3','ari:C.8.4'],'Exact duplication/division ladder polynomials and nonzero denominators.'),
 'C_ladder_estimates.py':(['fam:src:C.2.3'],'Numerical diagnostics for analytically proved scalar inequalities; dispensable for proof.'),
 'C_local_analytic_bounds.py':(['ari:C.8.1','ari:C.8.2'],'Numerical diagnostics for the rational local estimates; printed Taylor remainders prove them.'),
 'Ccritical_rational_certificate.py':(['ari:C.8.14','ari:C.8.15'],'Exact flint rational recurrence, Cauchy majorants, and positive Bernstein coefficients.'),
 'Ccritical_rational_certificate_fraction.py':(['ari:C.8.14','ari:C.8.15'],'Independent fractions.Fraction implementation of the exact rational certificate.'),
 'Ccritical_scalar.py':(['ari:C.8.13','ari:C.8.14'],'Scalar bound checks for cusp and compact Cayley-disc arguments.'),
 'Ccritical_identity_check.py':(['ari:C.8.12','ari:C.8.14'],'Independent differential-identity and modular-ODE consistency check.'),
 'C_cm_class_polynomials.gp':(['ari:C.6.3'],'Exact rational CM j-values from class polynomials.'),
 'C_cm_models.gp':(['ari:C.6.2','ari:C.6.3'],'Minimal equations, transformed section points, conductors and exact local model data.'),
 'C_cm_local_heights.gp':(['ari:C.6.2','ari:C.6.3'],'Exact finite valuations and local-height constants in the (O) normalization.'),
 'C_cm_rank_lvalues.gp':(['ari:C.6.R1','ari:C.6.R2'],'Certified equal lower/upper algebraic rank bounds on eleven curves; numerical L-values are independently certified below.'),
 'Crank_torsion_local.gp':(['ari:C.6.T1'],'Finite-reduction torsion constraints over the indicated number fields.'),
 'Crank_torsion_final.gp':(['ari:C.6.T1','ari:C.6.T2'],'Exact torsion and quadratic-field height/point comparisons.'),
 'Crank_torsion_descent.gp':(['ari:C.6.T1'],'Simon descent over number fields with bnfcertify=1 and retained Sage helper sources.'),
 'Crank_saturation.cpp':(['ari:C.6.R1'],'Full eclib saturation of all nine rank-one section points with height-based index bounds.'),
 'Crank_coefficients.gp':(['ari:C.6.R2'],'Exact Fourier coefficient files for the first ten derivative sums.'),
 'Crank_derivatives.cpp':(['ari:C.6.R2'],'1024-bit derivative sums with explicit infinite and alternating-series tails.'),
 'Crank_cm_stream.cpp':(['ari:C.6.R2'],'Exact CM coefficient/moment stream and bounded Taylor blocks for the largest conductor; repeated precisions and cutoffs.'),
 'Crank_cm_theta_test.gp':(['ari:C.6.R2','ari:C.6.R5'],'Exact initial CM theta coefficients, with the printed modular-form valence argument providing global identification.'),
 'C_cm_height_arb.py':(['ari:C.6.5'],'1152-bit Arb enclosures for all eleven heights and normalized theta norms.'),
 'C_height_coarse_certificate.py':(['ari:C.6.R4'],'Exact integer coarse height bounds used to isolate the three BSD-proved leading factors.'),
 'B_C6_gz_exact_metadata.gp':(['ari:C.6.R5'],'Twist identities, minimal differential scaling, Heegner splitting, root numbers, torsion and coefficient tests.'),
 'B_C6_gz_setup.gp':(['ari:C.6.R5'],'Historical setup program; its operative exact claims are rerun by B_C6_gz_exact_metadata.gp and the independent coefficient generators.'),
 'B_C6_central_stream.cpp':(['ari:C.6.R5'],'Twelve directed-rounding 256-bit MPFR central/derivative enclosures with exact coefficient moments and tails.'),
 'B_C6_exact_factors.py':(['ari:C.6.R5'],'Original verifier for all six exact auxiliary ratios and rational leading factors, using the proved denominator bounds.'),
 'C7_cm_explicit.gp':(['ari:C.7.10'],'Exact CM enlargement endomorphism and period-determinant test.'),
 'C7_cm_enlargement_check.py':(['ari:C.7.10'],'Exact linear-algebra obstruction to the proposed CM enlargement.'),
 'C7_complexified_check.py':(['ari:C.7.11'],'Exact complexified compact-subgroup obstruction.'),
 'C_padic_example.py':(['ari:C.7.8'],'Exact valuation/unit example for the proposed p-adic norm method.'),
 'C_cm_250.gp':(['ari:C.6.3','ari:open:norm'],'250-digit CM norm and height data used only for exploratory relation searches.'),
 'C_cm_theta_pslq.py':(['ari:open:norm'],'Eleven numerical PSLQ searches; null returns do not prove algebraic independence or transcendence.'),
 'C7_norm_polynomial_search.py':(['ari:open:norm'],'Sixty-six bounded numerical polynomial searches; no exhaustive lower-bound certificate is claimed.'),
 'certify_period_derivative_table.py':(['ari:C.6.R2'],'Independent 1152-bit Arb real-period and derivative/period enclosures, without BSD input.'),
}

def add(name,cmd,output,source=None,cwd=BASE,record=None,notes=None):
    source=source or AR/'code'/name
    source=Path(source)
    op=ARCH/archive(output)
    assert source.exists(),source
    assert op.exists(),op
    labels,role=roles.get(name,(['ari:C.6.R5'],'Exact coefficient input for the directed Gross–Zagier certificate.'))
    rows.append({'program':archive(source),'program_sha256':digest(source),
      'command':cmd,'cwd':cwd,'stdout_capture':str(op.relative_to(ARCH)),
      'output_sha256':digest(op),'statement_labels':labels,'statement_role':role,
      'record':record,'notes':notes or [],'run_status':'completed successfully; retained output checked',
      'command_shell':shlex.join(cmd)+' > '+shlex.quote(str(op.relative_to(ARCH)) if cwd=='.' else str(op.relative_to(ARCH/cwd)))})

# Portable GP inputs change only filesystem paths / runtime datadir overrides.
# Coefficient generators write to a fresh records/reproduction directory so a
# rerun never appends a second coefficient stream to the retained certificates.
portable=AR/'portable_gp';portable.mkdir(exist_ok=True)
gpm={};adapter=[]
for name in sorted(k for k in roles if k.endswith('.gp')):
    p=AR/'code'/name
    if not p.exists():continue
    s=p.read_text();t=re.sub(r'^default\(datadir,[^\n]*\);\s*\n','',s,flags=re.M)
    t=t.replace('S6_05_ARITHMETIC/','')
    if name in ['Crank_coefficients.gp','B_C6_gz_setup.gp']:
        t=t.replace('records/Crank_coeff_','records/reproduction/Crank_coeff_').replace('records/B_C6_aux_coeff_','records/reproduction/B_C6_aux_coeff_')
    q=portable/name;q.write_text(t)
    gpm[name]='portable_gp/'+name
    adapter.append({'source':archive(p),'portable_input':archive(q),
       'source_sha256':digest(p),'portable_sha256':digest(q),
       'changes':'Only remove machine-specific PARI datadir and normalize project/output paths; mathematical instructions retained.'})
(AR/'records/reproduction').mkdir(exist_ok=True)

for manifest in data['run_manifests']:
    name=Path(manifest['manifest']).name;recs=manifest['records']
    if name=='writing_saturation.json':
        add('Crank_saturation.cpp',['code/Crank_saturation'],recs['output'],record=archive(manifest['manifest']))
        continue
    for r in recs:
        if r.get('exit_code',r.get('exit',0))!=0 or r.get('stderr_errors') or r.get('errors'):continue
        if name=='writing_derivatives.json':
            i=r['index'];add('Crank_derivatives.cpp',['code/Crank_derivatives',f'records/Crank_coeff_{i}.dat'],r['output'],record=archive(manifest['manifest']))
        elif name=='writing_gz_regeneration.json':
            i,kind=r['index'],r['kind']
            output='code/'+(f'B_C6_derivative_{i}.out' if kind=='derivative' else ('B_C6_central_11.out' if i==11 else f'B_C6_central_file_{i}.out'))
            cmd=[str(a).replace(str(AR)+'/', '') for a in r['command']]
            add('B_C6_central_stream.cpp',cmd,output,record=archive(manifest['manifest']))
        elif name in ['writing_gp_reruns.json','writing_gp_reruns_second.json']:
            n=r['name'];add(n,['gp','-fq',gpm[n]],r['output'],record=archive(manifest['manifest']),notes=['Uses installed PARI datadir; pari-elldata is required where ellidentify or ellmaninconstant is used.'])
        else:
            n=Path(r['program']).name
            cmd=['python','code/'+n]
            add(n,cmd,r['output'],record=archive(manifest['manifest']))

for r in data['additional_runs']:
    p=ROOT/r['source'];n=p.name
    cmd=r.get('reproduction_command',r.get('command'))
    if n.endswith('.gp'):cmd=['gp','-fq',gpm[n]]
    cwd=BASE
    if n=='certify_period_derivative_table.py':
        cmd=['python','code/invariants_arithmetic/certify_period_derivative_table.py'];cwd='.'
    add(n,cmd,r['output'],source=p,cwd=cwd,record=BASE+'/writing_complete_computations.json')

add('Crank_coefficients.gp',['gp','-fq',gpm['Crank_coefficients.gp']],
    'outputs/writing_Crank_coefficients.txt',
    notes=['Retained certificate files are records/Crank_coeff_1.dat through Crank_coeff_10.dat. The portable generator writes fresh copies under records/reproduction; use those paths to recompute derivatives. Empty that reproduction directory before a repeated generation, because GP write appends.'])

# Deduplicate successful executions present in more than one audit manifest.
unique={}
for r in rows:unique[(r['program'],tuple(r['command']),r['stdout_capture'])]=r
rows=list(unique.values())

# Preserve every cited source filename and its actual archive destination,
# including historical output names replaced by stronger fresh transcripts.
cited={}
for p in (OUT/'sections').glob('ari_*.tex'):
    s=p.read_text()
    for m in re.finditer(r'\\path\{([^}]+)\}',s):
        value=m.group(1);base=Path(value).name
        direct=AR/value
        if not direct.exists():direct=AR/'code'/base
        targets=[r['stdout_capture'] for r in rows if Path(r['program']).stem==Path(base).stem]
        if base=='B_C6_gz_setup.out':targets=[BASE+'/outputs/writing_B_C6_gz_exact_metadata.gp.txt',BASE+'/records/B_C6_exact_factors.json']
        cited.setdefault(value,{'printed_name':value,'archive_path':archive(direct) if direct.exists() else None,
          'fresh_evidence':targets,'contexts':[]})['contexts'].append({'file':archive(p),'line':s[:m.start()].count('\n')+1})

builds=[]
for n in ['Crank_derivatives','Crank_cm_stream','B_C6_central_stream']:
    builds.append({'target':'code/'+n,'cwd':BASE,'command':['g++','-O2','-std=c++17','code/'+n+'.cpp','-o','code/'+n,'-lmpfr','-lgmp']})
builds.append({'target':'code/Crank_cm_stream_512','cwd':BASE,'command':['g++','-O2','-std=c++17','-DWORK_PREC=512','-DWORK_RAD=96','code/Crank_cm_stream.cpp','-o','code/Crank_cm_stream_512','-lmpfr','-lgmp']})
builds.append({'target':'code/Crank_saturation','cwd':BASE,'command':['g++','-O2','-std=c++17','code/Crank_saturation.cpp','-o','code/Crank_saturation','-lec','-lntl','-lpari','-lmpfr','-lgmp']})

obj={'checker':data['checker'],'effort':data['effort'],'date':data['date'],
 'archive_root':'The directory containing S6_09_PAPERS_I.tex and code/. All paths below are relative to that directory.',
 'runtime_requirements':data['runtimes'],
 'additional_python_requirements':['sympy','mpmath','numpy if imported by a retained diagnostic'],
 'commands_scope':'Recorded mathematical runs were completed. The archive commands use identical mathematical inputs with portable paths; standard system development libraries are required to rebuild C++ binaries.',
 'build_commands':builds,'portable_gp_inputs':adapter,'runs':rows,
 'cited_file_concordance':list(cited.values()),
 'superseded_setup_failures':data['superseded_setup_failures'],
 'historical_output_alias':{'code/B_C6_gz_setup.out':'No file of this name is in the supplied bundle. Replace the printed pointer by the fresh exact metadata transcript and the six factor certificates indexed here.'},
 'exact_conclusions':data['exact_conclusions']}
(OUT/'arithmetic_program_index.json').write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'successful_runs':len(rows),'distinct_programs':len({r['program'] for r in rows}),
 'cited_file_names':len(cited),'portable_gp_inputs':len(adapter),
 'missing_printed_paths':[k for k,v in cited.items() if not v['archive_path']]},indent=2))
