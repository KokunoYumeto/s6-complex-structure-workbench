"""Print Paper II's source concordance and actual computation commands.

These indices report independently retained evidence; generation is not a
mathematical proof check. All distinct proofs remain in the manuscript.
"""
from pathlib import Path
import csv,re,json,ast,hashlib,shlex
OUT=Path(__file__).resolve().parents[2]
ROOT=OUT.parent
s=(OUT/'S6_09_PAPERS_II.tex').read_text()
labels=set(re.findall(r'\\label\{([^}]+)\}',s))
with (OUT/'S6_09_PAPERS_inventory.csv').open() as f:
    rows=[r for r in csv.DictReader(f) if r['paper']=='II']
def esc(x):
    return ''.join({'&':r'\&','%':r'\%','#':r'\#','_':r'\_\allowbreak ','$':r'\$','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}','\\':r'\textbackslash{}',',':r',\allowbreak{}'}.get(c,c) for c in str(x))
def path(x):return r'\path{'+str(x).replace(' ',r'}\ \path{')+'}'
short={'S6_03_CDP':'CDP','S6_02_PUSH':'PUSH','S6_01_INVARIANTS':'INV','WORKING_CDP':'WB--CDP','WORKING_INV':'WB--INV','WORKING_EDITION':'WB','working_edition':'WB','course_CG-S6':'CG--S6'}
tex=r'''% BEGIN GENERATED RESULT INDEX
\section{Result, source and verification concordance}\label{app:II:result-index}
Each row gives the actual location of a source statement. Shared statements
are printed once, with every distinct complete proof retained. This index
does not replace a proof. The accompanying inventory retains the exact
source file, wording changes, independent checks, historical reader scope,
source comparisons, and any former gap and its repair.

All current complete readings, independent derivations and original-source
hypothesis matches are by GPT-6 Astra (OpenAI, ChatGPT Pro mode, effort Pro),
17 November 2026. Recorded readings by Claude Fable 5.2 (Anthropic), effort
high or effort max, and Claude Opus 5.5 (Anthropic), effort max,
12--16 November 2026, retain their precise per-result scopes. A producer's
status badge is provenance, never an independent proof check. The notation
F denotes a full proof reading, D an independent derivation, S an opened
operative source and matched hypotheses, and C an actual computation rerun.
C is limited to the program's finite algebraic or numerical scope and does
not certify an analytic or geometric construction.

\begingroup\small
\begin{longtable}{@{}p{40mm}p{16mm}p{92mm}@{}}
\toprule Source result & Printed number & Verification and source scope\\\midrule
\endfirsthead
\toprule Source result & Printed number & Verification and source scope\\\midrule
\endhead
'''
missing=[]
for r in rows:
    lab=r['printed_label']
    if lab not in labels:
        missing.append((r['source_run'],r['source_id'],lab));num='Pending placement'
    else:num=r'\ref{'+lab+'}'
    if r['source_run']=='S6_01_INVARIANTS' and r['source_id']=='E2.3':
        desc='F, D: full partial argument checked. The Kuranishi clause is corrected by the complete period-section proof; the specified bundle splitting remains in the final part.'
    else:
        desc='F, S: the complete proof and operative source hypotheses checked; all content changes and independent derivations are recorded in the inventory.'
    credit=r['credited_to']
    if credit:desc+=' Credit: '+credit
    tex+=path(short.get(r['source_run'],r['source_run'])+' '+r['source_id'])+' & '+num+' & '+esc(desc)+r'\\'+'\n'
tex+=r'\bottomrule\end{longtable}\endgroup'+'\n% END GENERATED RESULT INDEX\n'
(OUT/'editorial/II_result_index.tex').write_text(tex)
(OUT/'records/II_index_missing.json').write_text(json.dumps(missing,indent=2)+'\n')

# Every actual CDP rerun is listed, along with the PUSH/INV programs used here.
programs={}
def add_record(p,rec,manifest):
    p=Path(p)
    if p.is_absolute():p=p.relative_to(OUT)
    elif str(p).startswith('deliverables/'):p=Path(*p.parts[1:])
    f=OUT/p
    assert f.exists(),('Missing executed program',p,manifest)
    name=p.name
    cwd=p.parent.parent if p.parent.name=='code' else p.parent
    cmd=['python3',str(p.relative_to(cwd))]
    if name=='verify_analytic_picard_completion.py':
        cmd+=['--json-output','analytic_picard_completion_results.json']
    if rec.get('command') and 'working_directory' in rec:
        cmd=rec['command'];cwd=Path(rec['working_directory'])
    elif rec.get('cwd')=='archive root (deliverables)':
        cwd=Path('.');cmd=['python3',str(p)]
    try:doc=ast.get_docstring(ast.parse(f.read_text())) or ''
    except Exception:doc=''
    role=rec.get('role') or doc.split('\n')[0] or rec.get('scope','Exact identities at the stated point of use.')
    output=rec.get('output',rec.get('log',''))
    if output.startswith('deliverables/'):output=output[len('deliverables/'):]
    if not output:
        candidates=list(f.parent.glob(name+'.output.txt'))+list(f.parent.glob(name+'.rerun.txt'))+list(f.parent.glob(name+'.txt'))
        if not candidates:candidates=list((OUT/'code/cdp_audit').rglob(name+'.output.txt'))
        output='; '.join(str(q.relative_to(OUT)) for q in candidates)
    item={'program':str(p),'name':name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),
          'role':role,'scope':rec.get('scope','The paper specifies the exact computation and its role.'),
          'command':cmd,'cwd':str(cwd),'output':output,'exit_code':rec.get('exit_code',rec.get('returncode',rec.get('exit'))),'manifest':str(manifest.relative_to(OUT))}
    programs.setdefault(str(p),item)
for m in sorted((OUT/'code/cdp_audit').glob('execution_manifest*.json')):
    obj=json.loads(m.read_text());rr=obj.get('runs',[]) if isinstance(obj,dict) else obj
    for r in rr:
        p=r.get('executed') or 'code/cdp_audit/'+r['script']
        add_record(p,r,m)
m=OUT/'code/root_cdp/execution_manifest.json'
for r in json.loads(m.read_text()):add_record(r['program'],r,m)
m=OUT/'work/invariants_arithmetic/cdp_A5_program_runs.json'
for r in json.loads(m.read_text())['runs']:add_record(r['program'],r,m)
m=OUT/'code/invariants_arithmetic/invariants/writing_reruns.json'
for r in json.loads(m.read_text()):
    if r['program']!='d_exact.py':continue
    r={**r,'output':'code/invariants_arithmetic/invariants/'+r['output']}
    add_record('code/invariants_arithmetic/invariants/code/'+r['program'],r,m)
m=OUT/'work/root/comb_exact_execution.json'
r=json.loads(m.read_text());add_record(r['program'],r,m)

# Ignore the generated indices when determining manuscript program references.
core=re.sub(r'% BEGIN GENERATED (?:PROGRAM|RESULT) INDEX.*?% END GENERATED (?:PROGRAM|RESULT) INDEX','',s,flags=re.S)
names=set(x.replace('\\_','_').split('/')[-1] for x in re.findall(r'(?:code/)?[A-Za-z0-9_\\.-]+\.(?:py|gp|sage)\b',core))
push_manifest=OUT/'code/push/rerun_manifest.json'
push={r['program']:r for r in json.loads(push_manifest.read_text())}
for name in sorted(names):
    if any(r['name']==name for r in programs.values()):continue
    if name in push:
        add_record('code/push/code/'+name,push[name],push_manifest);continue
    fs=sorted((OUT/'code').rglob(name),key=lambda p:len(str(p)))
    assert fs,('Cited program absent',name)
    p=fs[0]
    # The INV manuscript's exact programs have actual rerun records in its
    # retained program manifest; do not infer a check from finding the file.
    run_records=[]
    for mf in (OUT/'code/invariants_arithmetic').glob('*.json'):
        try:obj=json.loads(mf.read_text())
        except Exception:continue
        rr=obj.get('runs',obj.get('results',[])) if isinstance(obj,dict) else obj
        if not isinstance(rr,list):continue
        for r in rr:
            if isinstance(r,dict) and name in str(r.get('program',r.get('script',''))):run_records.append((r,mf))
    if run_records:add_record(p,run_records[-1][0],run_records[-1][1])
    else:add_record(p,{},OUT/'work/invariants_arithmetic/programs_audit.json')

records=sorted(programs.values(),key=lambda r:r['program'])
(OUT/'records/II_program_index.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n')
tex=r'''% BEGIN GENERATED PROGRAM INDEX
\section{Programs, certificates and reproducible commands}\label{app:II:programs}
Paths are relative to the companion archive. Change to the stated working
directory and execute the displayed command. The calculations use Python~3,
with SymPy and mpmath where imported. Every named program and its output are
retained. The individual proofs state the exact finite rank, Smith form,
polynomial identity, local character, lattice or bounded enumeration checked.
No such certificate substitutes for the complete analytic occurrence or
properness proof. A finite list of examples is never extrapolated to an
unbounded parameter; the corresponding symbolic argument is printed.
The unchanged source output of \path{d_comb.py} retains an obsolete open
Kuranishi-status field. The full period-section proof in
\cref{cdp:st:E15} settles that question; the finite program checks its
displayed degrees and dimensions and makes no obstruction calculation.

\begingroup\small
\begin{longtable}{@{}p{48mm}p{56mm}p{44mm}@{}}
\toprule Program and purpose & Working directory; command & Retained output\\\midrule
\endfirsthead
\toprule Program and purpose & Working directory; command & Retained output\\\midrule
\endhead
'''
for r in records:
    out=path(r['output']) if r['output'] and '; ' not in r['output'] else 'Exact output paths and hashes are recorded in the run manifest.'
    tex+=path(r['name'])+r'\par '+esc(r['role'])+' & '+path(r['cwd'])+r'\par '+path(shlex.join(r['command']))+' & '+out+r'\\'+'\n'
tex+=r'\bottomrule\end{longtable}\endgroup'+'\n% END GENERATED PROGRAM INDEX\n'
(OUT/'editorial/II_programs.tex').write_text(tex)
print('II source rows',len(rows),'unplaced',len(missing),'programs',len(records),'with explicit output',sum(bool(r['output']) for r in records))
