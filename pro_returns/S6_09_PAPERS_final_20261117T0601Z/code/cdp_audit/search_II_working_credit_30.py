"""Execute bounded per-result attribution searches; no proof-status inference."""
from pathlib import Path
import concurrent.futures, hashlib, json, subprocess, datetime

D = Path(__file__).resolve().parents[2]
R = D.parent
W = D / 'work/cdp_audit/II_working_credit'
W.mkdir(parents=True, exist_ok=True)
plans = {
 'prop:missing-cotangent-filtration': ['conormal', 'cotangent', 'torsion'],
 'prop:missing-global-section-criterion': ['conormal', 'connecting', 'vanishing'],
 'lem:conormal-injective': ['conormal', 'nonzerodivisor', 'normal crossings'],
 'lem:conductor-square': ['conductor', 'Mayer.Vietoris', 'normalisation'],
 'prop:conductor': ['conductor', 'torsion section', '10.3'],
 'prop:nodal-counterexample': ['nodal', 'gluing parameter', 'endpoint'],
 'thm:cartier-duality': ['duality', 'Cohen.Macaulay', 'dualising'],
 'prop:cartier-duality-absolute': ['duality', 'Cartier', 'scheme.theoretic'],
 'lem:curve-flatness': ['flat', 'torsion.free', 'valuation ring'],
 'prop:analytic-base-change': ['base change', 'base.change', 'top degree'],
 'cor:surface-top-base-change': ['top.degree', 'scheme.theoretic', 'base.change'],
 'prop:pic0-pullback': ['Picard', 'exponential sequence', 'normalisation'],
 'prop:all-pic-restriction': ['Picard', 'restriction', 'normalisation'],
 'prop:leray-edge-restriction': ['Leray', 'transgression', 'first Chern'],
 'lem:picard-crossed-defect': ['crossed', 'pair.of.pants', 'cocycle'],
 'lem:picard-finite-norm': ['norm', 'finite cover', 'logarithmic'],
 'lem:picard-cusp-defect': ['speciali[sz]ation', 'Chern', 'cusp'],
 'prop:direct-boundary-picard': ['Picard', 'boundary', 'normalisation'],
 'cor:candidate-pic0-route': ['10.5', 'nonvanishing', 'conductor'],
 'thm:candidate-conductor': ['10.5', 'conductor', 'dualising'],
 'cor:candidate-conductor-actual': ['10.5', 'conductor', 'nonvanishing'],
 'lem:cdp-generic-endpoints': ['effective divisor', 'generic', 'vanishing'],
 'thm:corrected-cdp-global': ['vanishing', 'Euler characteristic', '2.4'],
 'cor:corrected-cdp-relative': ['2.4', 'higher direct image', 'vanishing'],
 'thm:corrected-cdp-fibrewise': ['conormal', 'injective', '692'],
 'test:cdp-comparison': ['10.6', 'counterexample', 'coinvariants'],
 'prop:local-cusp-picard-obstruction': ['support function', 'quadratic', 'Picard'],
 'prop:analytic-ah-boundary': ['Appell', 'semicharacter', 'crossed'],
 'lem:analytic-support-specialization': ['support function', 'piecewise.linear', 'Cartier divisor'],
 'thm:analytic-all-picard': ['Picard', 'normalisation', '10.5'],
}
base = json.loads((D/'work/cdp_audit/credit_comparison_239.json').read_text())[0]
corpora = {}
for name in ['AC26', 'E26', 'DGKX_v1', 'DGKX_v2']:
    corpora[name] = [f['path'] for f in base['found_in_'+name]['searched_files']]
corpora['elsewhere_attached'] = [f['path'] for f in json.loads((D/'work/cdp_audit/credit_elsewhere_searches_239.json').read_text())['files']]
files = {f:{'path':f,'sha256':hashlib.sha256((R/f).read_bytes()).hexdigest()} for fs in corpora.values() for f in fs}

def search(job):
    sid, corpus, patterns = job
    cmd = ['rg','-n','-i','--no-heading']
    for p in patterns:cmd += ['-e',p]
    cmd += corpora[corpus]
    p = subprocess.run(cmd,cwd=R,text=True,capture_output=True)
    assert p.returncode in (0,1),(sid,corpus,p.stderr)
    lines=p.stdout.splitlines()
    name=sid.replace(':','_')+'__'+corpus+'.txt'
    dest=W/'search_hits'/name;dest.parent.mkdir(exist_ok=True)
    dest.write_text(p.stdout)
    return {'source_run':'WORKING_CDP','source_id':sid,'corpus':corpus,
       'patterns':patterns,'command':cmd,'cwd':'.','exit_code':p.returncode,
       'searched_files':[files[f] for f in corpora[corpus]],
       'matched_lines':len(lines),'full_hit_file':str(dest.relative_to(D)),
       'full_hit_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
       'scope':'Executed whole-file bounded textual search. Hits alone are not a theorem match or proof reading; actual context comparisons are separately recorded.'}

jobs=[(sid,corpus,patterns)for sid,patterns in plans.items() for corpus in corpora]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    rows=list(pool.map(search,jobs))
report={'reader':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)','effort':'Pro','date':'2026-11-17',
 'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'source_results':30,'searches':len(rows),'records':rows,
 'negative_search_limit':'A negative query or absence of a full counterpart in the opened contexts is not an exhaustive novelty or priority assertion.'}
(W/'searches_150.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(W/'search_plan_30.json').write_text(json.dumps(plans,indent=2)+'\n')
print(json.dumps({'source_results':30,'searches':len(rows),'corpus_file_counts':{k:len(v) for k,v in corpora.items()},'matched_lines':sum(r['matched_lines'] for r in rows)},indent=2))
