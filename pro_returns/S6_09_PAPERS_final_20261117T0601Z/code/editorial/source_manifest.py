"""Map received statements to exact source text; this is not a proof checker."""
from pathlib import Path
import csv, hashlib, json, re

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/work/root'
OUT.mkdir(parents=True,exist_ok=True)
ENVS=r'theorem|proposition|lemma|corollary|claim|problem|example|remark'
START=re.compile(r'\\begin\{('+ENVS+r')\}(?:\[([\s\S]*?)\])?')

def results_in(path):
    text=path.read_text()
    records=[]
    for match in START.finditer(text):
        env=match.group(1)
        end=text.find('\\end{'+env+'}',match.end())
        if end<0: raise ValueError((str(path),match.start(),'unclosed environment'))
        end+=len('\\end{'+env+'}')
        labels=re.findall(r'\\label\{([^}]+)\}',text[match.start():end])
        next_match=START.search(text,end)
        proof_start=text.find('\\begin{proof}',end)
        proof=''
        proof_end=end
        if proof_start>=0 and (next_match is None or proof_start<next_match.start()):
            depth=1
            for token in re.finditer(r'\\(begin|end)\{proof\}',text[proof_start+len('\\begin{proof}'):]):
                depth+=1 if token.group(1)=='begin' else -1
                if depth==0:
                    proof_end=proof_start+len('\\begin{proof}')+token.end()
                    proof=text[proof_start:proof_end]
                    break
        records.append({'environment':env,'title':match.group(2) or '',
          'labels':labels,'source_file':str(path.relative_to(ROOT/'sources')),
          'line':text.count('\n',0,match.start())+1,
          'statement':text[match.start():end], 'proof':proof,
          'statement_start':match.start(),'statement_end':end,'proof_end':proof_end,
          'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    return records

def closure(run,initial):
    seen=[]
    def visit(relative):
        p=ROOT/'sources/returns'/run/relative
        if not p.suffix:p=p.with_suffix('.tex')
        if p in seen:return
        if not p.exists():raise FileNotFoundError(p)
        seen.append(p)
        for inc in re.findall(r'\\input\{([^}]+)\}',p.read_text()):visit(inc)
    for rel in initial:visit(rel)
    return seen

def main():
    files={
      'S6_02_FAMILY':closure('S6_02_FAMILY',['sections/AB.tex','sections/CD.tex','sections/E.tex','sections/F.tex']),
      'S6_02_PUSH':closure('S6_02_PUSH',['sections/AB_push.tex','sections/C_push.tex','sections/D_push.tex','sections/E_push.tex'])}
    for run,paths in files.items():
        records=[r for p in paths for r in results_in(p)]
        (OUT/(run+'_statements.json')).write_text(json.dumps(records,indent=2))
        ids=list(csv.DictReader((ROOT/'sources/returns'/run/(run+'_results.csv')).open()))
        unmatched=[]
        mapping=[]
        for row in ids:
            sid=row['id']
            exact=[r for r in records if re.match(re.escape(sid)+r'(?:\D|$)',r['title'])]
            if len(exact)!=1:unmatched.append((sid,len(exact)))
            mapping.append({'source_run':run,'source_id':sid,'matches':[{k:r[k] for k in ['source_file','line','environment','labels']} for r in exact]})
        (OUT/(run+'_manifest.json')).write_text(json.dumps(mapping,indent=2))
        print(run,'canonical files',len(paths),'environments',len(records),'unmatched',unmatched)
    names=['candidate_geometry','exact_algebra','finite_filling_certificates','algebraic_dimension','analytic_canonical_ring','period_parameter_deformation','period_shift_classification']
    records=[r for name in names for r in results_in(ROOT/'sources/workbench'/(name+'.tex')) if r['environment'] not in ['remark','example']]
    (OUT/'working_edition_statements.json').write_text(json.dumps(records,indent=2))
    rows=[]
    for r in records:
        rows.append({'source_run':'WORKING_EDITION','source_id':r['labels'][0] if r['labels'] else r['source_file']+':'+str(r['line']),
          'source_file':r['source_file']+':'+str(r['line']),'paper':'I','kind':r['environment'].capitalize(),
          'statement_as_source':r['statement'],'taken_over_by':'','recorded_checks':'Pending mapping; not an absence finding.',
          'your_check':'Pending','check_outcome':'Pending'})
    with (OUT/'working_edition_inventory.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    print('Root working statements',len(rows))

if __name__=='__main__':main()
