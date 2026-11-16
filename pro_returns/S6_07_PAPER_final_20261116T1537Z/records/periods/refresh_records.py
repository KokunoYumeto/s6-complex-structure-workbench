"""Refresh prose excerpts and exact proof comparisons after manuscript generation."""
from pathlib import Path
import json,re,difflib

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'deliverables/records/periods'
SRC=ROOT/'inputs/sources'
full=(OUT/'sections.tex').read_text()

def span(start,end):
    a=full.index(start);b=full.index(end,a)
    return full[a:b].strip()

def source_span(path,start,end):
    text=(SRC/path).read_text();a=text.index(start);b=text.index(end,a)
    return text[a:b].strip()

fam='returns/S6_02_FAMILY/sections/CD.tex'
special='returns/S6_05_ARITHMETIC/sections/C_special.tex'
analytic='returns/S6_05_ARITHMETIC/sections/C_analytic.tex'
measure='returns/S6_05_ARITHMETIC/sections/C_measure.tex'
critical='returns/S6_05_ARITHMETIC/sections/C_critical.tex'
push='returns/S6_02_PUSH/sections/E4_push.tex'
old=json.loads((OUT/'prose_records.json').read_text())
old={r['paper_label']:r for r in old}
rows=[]
def add(label,printed,run,sid,path,source,kind='Definition/record'):
    r=dict(old.get(label,old['periods:theta-definitions']))
    r.update(paper_label=label,statement_as_printed=printed,source_run=run,
             source_id=sid,source_file=path,source_statement=source,kind=kind,
             one_line=sid)
    r['wording_vs_source']='same content: notation and presentation changed as specified in notation.md; definition or recorded source computation, not an additional theorem. The exact printed text and source excerpts are retained in this row.'
    if label=='periods:special-computation-availability':
        r['wording_vs_source']='changed: editorial artifact inventory and historical/current distinction; source mathematics unchanged. Names of the two producing-run programs come from the verbatim C.1.2 proof excerpt; their absence is the current attached-archive inventory finding.'
    if label=='periods:norm-definition':
        r['wording_vs_source']='changed: joins the ARI C.1 theta-norm and general-lattice definitions with the definition L(t)=log N(mu(tau),tau) from the C.8 critical setup; notation N→mathcal N, eta→eta_D, Lambda→Lambda_ell, L→mathcal L. No mathematical definition is added.'
    if label=='periods:division-model':
        r['wording_vs_source']='changed: joins the ARI C.4 rational-model setup with only the local-height notation lambda_infinity(Q)=-log N(Q) from C.4.1; adds the explicit notice of the coordinate dictionary already recorded in notation.md. P→P^div, x,y→x_div,y_div, Delta→Delta_div, N→mathcal N. The source excerpts are verbatim parts, not a single contiguous source statement.'
    if label=='periods:certificate-record':
        r['wording_vs_source']='changed: editorial synthesis of FAM C.2.3, PUSH E.4.1–3 and REVIEW_S6_02_FAMILY §2, with current artifact inventory and historical/current distinction; all source numerical constants, counts and arithmetic details are unchanged. source_statement concatenates the verbatim FAM C.2.3 and PUSH E.4 sections; the historical status excerpt is separately identified by its exact locator.'
    r['source_excerpt_mode']='composite verbatim excerpts' if label in ['periods:norm-definition','periods:division-model','periods:certificate-record'] else 'single source excerpt'
    rows.append(r)

add('periods:theta-definitions',span('We use the odd Jacobi function',' The elliptic-logarithm interpretation'),
    'FAM','C.1 setup',fam,source_span(fam,r'We use the odd Jacobi function',r'\begin{proposition}'))
add('periods:special-computation-availability',span('The computation in FAM C.1.2',r'\subsection{The elliptic norm'),
    'FAM','C.1.2 artifact-availability record',fam,
    source_span(fam,r'The executable \texttt{cd\_numerics.py}',r'\end{proof}'),kind='Artifact record')
add('periods:norm-definition',span('The elliptic lattice in this subsection','The theta formula gives'),
    'ARI','C.1 setup; C.8 critical setup',special+'; '+critical,
    source_span(special,'We write $',r'\begin{statement}')+'\n\n'+
    source_span(critical,'We continue to write',"We use\nEichler"))
add('fam:eq:cd-norm',span('The theta formula gives',r'\begin{proposition}[ARI C.1.1'),
    'FAM','C.2.1 proof, eq:cd-norm',fam,
    source_span(fam,r'\begin{equation}\label{eq:cd-norm}',r'\end{equation}')+'\n'+r'\end{equation}')
add('periods:division-model',span('For division-polynomial calculations',r'\begin{proposition}[ARI C.4.2'),
    'ARI','C.4 setup and local-height notation in C.4.1',special,
    source_span(special,'We use throughout this subsection',r'\begin{statement}')+'\n\n'+
    source_span(special,'On every complex\nelliptic curve the model-independent',r'Thus $D_{\rm part}='))
add('periods:measure-conventions',span('We take $dd^c=',r'\begin{announcement}[ARI C.8.9'),
    'ARI','C.8 measure conventions',measure,
    source_span(measure,r'We take $dd^c=',r'\begin{statement}'))
source_fam=source_span(fam,r'\begin{theorem}[C.2.3',r'\subsection{C.3.')
source_push=(SRC/push).read_text()
add('periods:certificate-record',span(r'\paragraph{Certificate block.}',r'\subsection{Local parameters'),
    'FAM;PUSH','FAM C.2.3; PUSH E.4.1–3; REVIEW_S6_02_FAMILY §2',
    fam+'; '+push+'; status/REVIEW_S6_02_FAMILY.md',source_fam+'\n\n'+source_push,kind='Computation record')
add('periods:local-expansion-constants',span(r'Put $G_\square=',r'\begin{proposition}[ARI C.3.1'),
    'ARI','C.3 setup',special,source_span(special,'Put $G=',r'\begin{statement}'))
add('periods:ladder-modular-conventions',span('Throughout this proof',r'\begin{proposition}[ARI C.8.1'),
    'ARI','C.8 analytic setup',analytic,
    source_span(analytic,'Throughout this section','We use the division identity'))

(OUT/'prose_records.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False))

records=json.loads((OUT/'records.json').read_text());proofs=[]
for r in records:
    s=(SRC/r['source_file']).read_text()
    p=re.search(r'\\begin\{(statement|proposition|theorem|corollary)\}\['+re.escape(r['source_id'])+r'[; ].*?\\end\{\1\}\s*\\begin\{proof\}(.*?)\\end\{proof\}',s,re.S)
    a=full.index(r'\label{'+r['paper_label']+'}')
    following=full[a:]
    q=re.search(r'\\end\{(?:proposition|computed|announcement)\}.*?\\par\s*\\begin\{proof\}(.*?)\\end\{proof\}',following,re.S)
    # Announcements and the interval descriptions have no printed proof.
    if r['status']=='A' or r['paper_label'] in ['fam:C.2.3','push:E.4.1']:
        continue
    if not p or not q:raise RuntimeError(r['paper_label'])
    orig=p[2].strip();printed=q[1].strip()
    proofs.append({'paper_label':r['paper_label'],'source_proof':orig,'proof_as_printed':printed,
                   'edits':'Notation concordance, numbered source paragraph steps, citation locators, and explicit attribution of source-run executable claims; no mathematical argument omitted.',
                   'diff':'\n'.join(difflib.unified_diff(orig.splitlines(),printed.splitlines(),fromfile=r['source_file'],tofile=r['paper_label'],lineterm=''))})
(OUT/'proof_comparisons.json').write_text(json.dumps(proofs,indent=2,ensure_ascii=False))
print(len(rows),'prose records;',len(proofs),'proof comparisons')
