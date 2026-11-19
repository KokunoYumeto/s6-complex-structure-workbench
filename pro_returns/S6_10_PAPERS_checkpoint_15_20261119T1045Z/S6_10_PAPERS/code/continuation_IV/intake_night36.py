#!/usr/bin/env python3
"""Place all eleven cp36 source statements/arguments under explicit review.

This reversible source-placement operation awards no whole-proof check.
It expands all literal inputs; original files, their hashes and every
transformation are recorded. Status promotion is a separate owner action.
"""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re
csv.field_size_limit(16 * 1024 * 1024)

P=Path(__file__).resolve().parents[2]
W=P.parents[1]
N=W/'night36/S6_06_BLIND'
A=P/'analysis/continuation_IV'
BEGIN='% BEGIN CONTINUATION_NIGHT36_RECEIVING'
END='% END CONTINUATION_NIGHT36_RECEIVING'
ids=[f'P3K.{n}' for n in range(109,120)]
source_rows={r['id']:r for r in csv.DictReader((N/'S6_06_BLIND_results.csv').open())}
sha=lambda x:hashlib.sha256(x).hexdigest()
manifest=[]

def expand(path,seen,stack=()):
    path=path.resolve()
    if path in stack:raise ValueError('Cyclic source input: '+str(path))
    if not path.is_relative_to(N):raise ValueError('Source input outside verified cp36: '+str(path))
    raw=path.read_bytes();seen[str(path.relative_to(N))]=dict(file=str(path.relative_to(N)),sha256=sha(raw),size=len(raw))
    s=raw.decode()
    def sub(m):
        name=m[1] if m[1].endswith('.tex') else m[1]+'.tex'
        candidates=[N/name,path.parent/name]
        target=next((q for q in candidates if q.exists()),None)
        if target is None:raise ValueError('Missing source input '+name+' in '+str(path))
        return '\n% Expanded verified cp36 input: '+str(target.relative_to(N))+'\n'+expand(target,seen,stack+(path,))+'\n% End expanded verified cp36 input\n'
    return re.sub(r'\\input\{([^{}]+)\}',sub,s)

pieces=[BEGIN,r'''\subsection{Checkpoint36 source results with continuation review pending}

The following source statements and their complete supplied arguments are
retained here while their continuation checks are completed. Their source
records report proofs by GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro,
S6\_06\_BLIND, 16--18 November 2026. Each receiving status records the
current scope below; importing the source does not add a proof check.
The separate event ledger records the algebraic substeps already checked
with new code and every later mathematical comparison.
''']
additional_uses={
 'P3K.109':['night:P3F.35','night:P3F.46'],
 'P3K.113':['night:P3K.109','night:P3K.110'],
 'P3K.114':['night:P3K.109','night:P3K.110','night:P3K.113'],
}
for sid in ids:
    row=source_rows[sid];seen={};expanded=expand(N/row['where_proved'],seen)
    pattern=r'\\begin\{statement\}\{'+re.escape(sid)+r'\}\{[^}]*\}'
    uses=['night:'+x.strip() for x in row['depends_on'].split(';') if x.strip()]
    uses+=additional_uses.get(sid,[]);uses=list(dict.fromkeys(uses))
    uses_tex=(r'\cref{'+','.join(uses)+'}; ' if uses else '')+'the original source, point line, roots, characters, reference, selected fan and scalar range stated here'
    record=(r'\begin{theorem}[Source result '+sid+r' under continuation review]\label{night:'+sid+'}\n'
      +r'\StatementRecord{night:'+sid+'}{open}{Historical event: GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6\\_06\\_BLIND, 16--18 November 2026: targeted proof check, recorded producing-run re-derivation. Also checked in this writing by GPT-6 Astra (OpenAI), ChatGPT Pro mode, effort Pro, S6\\_10\\_PAPERS continuation, 19 November 2026: computation or formal certificate for the explicitly listed algebraic substeps in the event ledger; full continuation rederivation and renewed credit comparison remain pending.}{'+uses_tex+'}')
    expanded,n=re.subn(pattern,lambda m:record,expanded,count=1)
    if n!=1:raise ValueError('Expected one source statement '+sid)
    expanded,n=expanded.replace('\\end{statement}','\\end{theorem}',1),expanded.count('\\end{statement}')
    if n!=1:raise ValueError('Unexpected nested source statements '+sid)
    def receiving_proof_heading(match):
        heading=r'\begin{proof}[Supplied source argument; continuation review in progress]\mbox{}\par'
        if match.group(1):
            heading+='\n'+r'\noindent\textbf{'+match.group(1).rstrip('.')+r'.}\par\smallskip'
        return heading
    expanded=re.sub(r'\\begin\{proof\}(?:\[([^\]]*)\])?(?:\\mbox\{\}\\par)?',receiving_proof_heading,expanded,count=1)
    # Namespace actual internal labels by a bijective explicit map. Tags stay
    # exactly as the source prints them, as local proof locators.
    labels=sorted(set(re.findall(r'\\label\{([^}]+)\}',expanded))-{'night:'+sid})
    labelmap={label:'ivcp36:'+sid+':'+label for label in labels}
    for old,new in labelmap.items():
        for command in ['label','ref','eqref','pageref','autoref','cref','Cref']:
            expanded=expanded.replace('\\'+command+'{'+old+'}','\\'+command+'{'+new+'}')
    pieces.append(expanded)
    manifest.append(dict(id=sid,label='night:'+sid,source_status=row['status'],receiving_status='open',source_row=row,
      source_files=list(seen.values()),expanded_receiving_sha256=sha(expanded.encode()),
      internal_label_morphism=labelmap,explicit_receiving_uses=uses,
      transforms=['literal recursive input expansion','statement environment to receiving theorem with explicit open status','source argument proof heading','bijective internal label namespace'],
      proof_check_awarded_by_intake=False))
pieces.append(END)
fragment='\n\n'.join(pieces)+'\n'
fragment_path=P/'papers/IV/continuation_night36.tex';fragment_path.write_text(fragment)
placements=[]
for rel in ['papers/IV/body.tex','papers/IV/body_source.tex']:
    path=P/rel;s=path.read_text();old=sha(s.encode())
    if BEGIN in s:
        a=s.index(BEGIN);b=s.index(END,a)+len(END);s=s[:a]+fragment.rstrip()+s[b:]
    else:s=s.rstrip()+'\n\n'+fragment
    path.write_text(s);placements.append(dict(file=rel,before_sha256=old,after_sha256=sha(s.encode())))

inventory_path=P/'S6_10_PAPERS_inventory.csv'
with inventory_path.open() as f:reader=csv.DictReader(f);fields=reader.fieldnames;inventory=list(reader)
by={m['label']:m for m in manifest}
for row in inventory:
    if row['label'] not in by:continue
    m=by[row['label']];notes=json.loads(row['notes'])
    notes.update(receiving_text_pending=False,receiving_integration_pending=False,
      receiving_file='papers/IV/body.tex',receiving_fragment='papers/IV/continuation_night36.tex',
      source_proof_argument_retained_in_full=True,continuation_source_intake_manifest='analysis/continuation_IV/night36_receiving_intake.json',
      continuation_review_scope='Only explicit event records award checks; whole mathematical and three-check gates remain pending.',
      continuation_dependency_review_pending=True)
    notes['source_uses_received_cp36']=m['source_row']['depends_on']
    row.update(status='open',uses='; '.join(m['explicit_receiving_uses']),notes=json.dumps(notes,ensure_ascii=False))
with inventory_path.open('w',newline='') as f:wr=csv.DictWriter(f,fields);wr.writeheader();wr.writerows(inventory)

payload=dict(recorded_at=datetime.now(timezone.utc).isoformat(),source_checkpoint=36,rows=manifest,placements=placements,
 whole_proof_checks_awarded=0,source_arguments_omitted=0,scope='Complete source placement under explicit receiving open status; current substep checks remain in the event ledger.')
(A/'night36_receiving_intake.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'rows':len(manifest),'expanded_bytes':len(fragment.encode()),'source_files':len({f['file'] for m in manifest for f in m['source_files']}),'whole_proof_checks_awarded':0},indent=2))
